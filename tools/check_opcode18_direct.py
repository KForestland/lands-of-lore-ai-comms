"""Replay bounded opcode-18 branches from a user's own executable.
Requires unicorn. No game bytes are emitted. Synthetic inputs, not gameplay.
"""
import argparse
import hashlib
import json
import struct
from pathlib import Path
from unicorn import Uc, UC_ARCH_X86, UC_MODE_32
from unicorn.x86_const import UC_X86_REG_ESP, UC_X86_REG_EAX, UC_X86_REG_EIP

HASH = '9aa18fe51164a159f33cd6361737ba2eeeb0d797042d718793047cc6d2077647'
CMD, OBJ, HEADING, AUX, WORK, STACK, STOP = (0x300000, 0x310000, 0x320000, 0x330000, 0x340000, 0x400000, 0x500000)
def pack(*values):
    return struct.pack('<' + 'I' * len(values), *(v & 0xffffffff for v in values))

def replay(data, flags, entry=0x65bb0, kind=2):
    vm = Uc(UC_ARCH_X86, UC_MODE_32)
    vm.mem_map(0x10000, 0x500000)
    # Only the inspected routines are mapped; unexpected calls fail the checks.
    vm.mem_write(0x65bb0, data[0x9cbb0:0x9d12e])
    record = bytearray(18)
    record[0:2] = bytes([18, kind])
    struct.pack_into('<hhhHH', record, 4, -123, 456, -7, flags, 0x8000)
    record[14:18] = bytes([3, 10, 91, 73]) if entry == 0x660f8 else bytes([3, 10, 0, 0])
    vm.mem_write(CMD, bytes(record))
    vm.mem_write(OBJ, pack(11, 22, 33))
    vm.mem_write(HEADING, pack(0x1234))
    vm.mem_write(AUX, pack(99))
    vm.mem_write(0x22c5a, pack(1))
    args = [CMD, WORK, 8, OBJ, HEADING, AUX] if entry == 0x65bb0 else [CMD]
    vm.mem_write(STACK, pack(STOP, *args))
    vm.reg_write(UC_X86_REG_ESP, STACK)
    vm.emu_start(entry, STOP, count=1000)
    assert vm.reg_read(UC_X86_REG_EIP) == STOP, 'did not return within instruction budget'
    assert vm.reg_read(UC_X86_REG_ESP) == STACK + 4, 'unexpected stack balance'
    return dict(result=vm.reg_read(UC_X86_REG_EAX) & 255,
                position=list(struct.unpack('<iii', vm.mem_read(OBJ, 12))),
                heading=struct.unpack('<I', vm.mem_read(HEADING, 4))[0],
                auxiliary=struct.unpack('<i', vm.mem_read(AUX, 4))[0],
                flags=struct.unpack('<H', vm.mem_read(CMD + 10, 2))[0],
                state=list(vm.mem_read(CMD + 16, 2)))

def main():
    if not __debug__:
        raise SystemExit("Run without -O: assertions are the verification checks.")
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('executable', type=Path)
    a = ap.parse_args()
    data = a.executable.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != HASH:
        raise SystemExit('Unsupported executable hash; inspect this build before extending support.')
    cases = []
    for flags in (4, 0x104):
        r = replay(data, flags)
        assert r['result'] == 2
        assert r['position'] == [-123 << 16, 456 << 16, (-7 << 16) if flags & 0x100 else 33]
        assert r['heading'] == 0x8000 and r['auxiliary'] == 99
        assert r['flags'] == flags | 0x20
        cases.append(dict(case=f'direct_{flags:04x}', observed=r))
    r = replay(data, 0x24)
    assert r['result'] == 3 and r['position'] == [11, 22, 33]
    assert r['heading'] == 0x1234 and r['state'] == [0, 0]
    cases.append(dict(case='already_complete', observed=r))
    r = replay(data, 4, kind=1)
    assert r['result'] == 2 and r['auxiliary'] == -6
    cases.append(dict(case='kind1_auxiliary_signed_byte14', observed=r))
    for flags, expected in ((0x34, 4), (0x36, 0x16)):
        r = replay(data, flags, entry=0x660f8)
        assert r['flags'] == expected and r['state'] == [0, 0]
        cases.append(dict(case=f'rearm_{flags:04x}', observed=r))
    print(json.dumps(dict(executable_sha256=digest, method='Original x86 in Unicorn; synthetic inputs, no gameplay',
                         code_sha256=hashlib.sha256(data[0x9cbb0:0x9d12e]).hexdigest(), cases=cases), indent=2))

if __name__ == '__main__':
    main()
