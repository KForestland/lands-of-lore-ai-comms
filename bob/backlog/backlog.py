#!/usr/bin/env python3
"""Lane tool for the LoL2 MASTER BACKLOG (backlog.json). File-locked, so lanes never overwrite each other.

  backlog.py next --lane LANE [--n 5]     highest-priority todo tasks for LANE (or lane 'any') whose depends are done
  backlog.py claim ID LANE                 mark claimed (refused if someone else holds it)
  backlog.py done ID LANE "receipt"        mark done with a receipt (commit, test report, board line)
  backlog.py block ID LANE "reason"        mark blocked with the reason (lead re-plans)
  backlog.py release ID LANE               give a claim back
  backlog.py show ID | stats
Also post the claim/done on COORDINATION.txt as usual; the lead regenerates BACKLOG.md with build_backlog.py.
"""
import fcntl, json, sys
from pathlib import Path

F = Path(__file__).resolve().parent / 'backlog.json'


def load_locked():
    fh = open(F, 'r+'); fcntl.flock(fh, fcntl.LOCK_EX)
    return fh, json.loads(fh.read())


def save(fh, data):
    fh.seek(0); fh.truncate(); fh.write(json.dumps(data, indent=1)); fh.flush(); fcntl.flock(fh, fcntl.LOCK_UN); fh.close()


def main(a):
    if not a: print(__doc__); return 1
    cmd = a[0]
    fh, data = load_locked()
    tasks = {t['id']: t for t in data['tasks']}
    try:
        if cmd == 'next':
            lane = a[a.index('--lane') + 1] if '--lane' in a else 'any'
            n = int(a[a.index('--n') + 1]) if '--n' in a else 5
            ready = [t for t in data['tasks'] if t['status'] == 'todo' and t['lane'] in (lane, 'any')
                     and all(tasks.get(d, {}).get('status') == 'done' for d in t['depends'])]
            for t in ready[:n]: print(f"P{t['priority']} {t['id']} [{t['type']} {t['area']}] {t['title']}\n    source: {t['source']}\n    accept: {t['acceptance']}")
            if not ready: print('nothing ready for', lane)
        elif cmd in ('claim', 'done', 'block', 'release'):
            tid, lane = a[1], a[2]; t = tasks[tid]
            if cmd == 'claim':
                if t['status'] == 'claimed' and t['claimed_by'] != lane: print(f'REFUSED: claimed by {t["claimed_by"]}'); return 2
                t['status'], t['claimed_by'] = 'claimed', lane
            elif cmd == 'done': t['status'], t['claimed_by'], t['note'] = 'done', lane, (a[3] if len(a) > 3 else '')
            elif cmd == 'block': t['status'], t['claimed_by'], t['note'] = 'blocked', lane, (a[3] if len(a) > 3 else '')
            else: t['status'], t['claimed_by'] = 'todo', ''
            print(cmd, tid, '->', t['status'], t['claimed_by'])
        elif cmd == 'show': print(json.dumps(tasks[a[1]], indent=1))
        elif cmd == 'stats':
            s = {}
            for t in data['tasks']: s[t['status']] = s.get(t['status'], 0) + 1
            print(len(data['tasks']), 'tasks', s)
        else: print(__doc__); return 1
    finally:
        save(fh, data)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
