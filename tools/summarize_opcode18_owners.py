"""Summarize opcode-18 owners from a local lol2_export_scripts.py JSON export.
Outputs metadata and decoded fields only; no raw scripts or media.
Region kind-11 links are deliberately not inferred by this tool.
"""
import argparse
import json
import struct
from pathlib import Path


def summarize(document):
    if document.get('format') != 'lol2-native-scripts-2' or document.get('unsupported'):
        raise ValueError('Need a complete lol2-native-scripts-2 export')
    rows = []
    for group in document['groups']:
        owners = []
        for obj in document['objects']:
            for event in obj['events']:
                if (event.get('stream'), event.get('group')) == (group['stream'], group['group']):
                    predicate = event.get('predicate')
                    owners.append(dict(ref=obj['ref'], record_kind=event['kind'],
                                       event=event.get('event'), value=event.get('value'),
                                       event_file_offset=event['file_offset'],
                                       predicate_index=predicate['index'] if predicate else None))
        for command in group['commands']:
            if command['opcode'] != 18:
                continue
            raw = bytes.fromhex(command['raw_hex'])
            if len(raw) != 18 or raw[0] != 18:
                raise ValueError('Malformed opcode-18 command')
            rows.append(dict(stream=group['stream'], group=group['group'],
                             command_offset=command['offset'], file_offset=command['file_offset'],
                             kind=raw[1], target=struct.unpack_from('<H',raw,2)[0],
                             destination=list(struct.unpack_from('<hhh',raw,4)),
                             flags=struct.unpack_from('<H',raw,10)[0],
                             heading=struct.unpack_from('<H',raw,12)[0], owners=owners))
    return rows


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('export',type=Path)
    args=parser.parse_args()
    print(json.dumps(summarize(json.loads(args.export.read_text(encoding='utf-8-sig'))),indent=2))

if __name__=='__main__':main()
