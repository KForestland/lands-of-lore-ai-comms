"""Check gradual opcode-18 control flow with explicitly substituted math helpers.
Requires unicorn; use the same executable as check_opcode18_direct.py.
This does not verify helper math, collision, or gameplay.
"""
import argparse
import hashlib
import json
from pathlib import Path
import struct
from unicorn import Uc, UC_ARCH_X86, UC_MODE_32, UC_HOOK_CODE
from unicorn.x86_const import UC_X86_REG_ESP, UC_X86_REG_EIP, UC_X86_REG_EAX
from check_opcode18_direct import HASH, CMD, OBJ, HEADING, AUX, WORK, STACK, STOP, pack


def replay(data, flags=8, distance=10 << 16, step=1 << 16, height=0,
           speed=8, target_speed=10, accumulator=0, tick=1, heading=0x1234):
    vm = Uc(UC_ARCH_X86, UC_MODE_32)
    vm.mem_map(0x10000, 0x500000)
    vm.mem_write(0x65bb0, data[0x9cbb0:0x9d0f7])
    record = bytearray(18)
    record[:2] = bytes([18, 2])
    struct.pack_into('<hhhHH', record, 4, 10, 0, height, flags, 0x8000)
    record[15:18] = bytes([target_speed, accumulator, 0])
    vm.mem_write(CMD, bytes(record))
    vm.mem_write(OBJ, pack(0, 0, 0))
    vm.mem_write(HEADING, pack(heading))
    vm.mem_write(AUX, pack(99))
    vm.mem_write(0x22c5a, pack(tick))
    vm.mem_write(STACK, pack(STOP, CMD, WORK, speed, OBJ, HEADING, AUX))
    vm.reg_write(UC_X86_REG_ESP, STACK)
    calls = []
    def read(addr):
        return struct.unpack('<I', vm.mem_read(addr, 4))[0]
    def hook(uc, address, size, unused):
        if 0x65bb0 <= address < 0x660f7:
            return
        sp = uc.reg_read(UC_X86_REG_ESP)
        if address == 0x111c34:
            # Caller expects direction/distance output at argument 1.
            uc.mem_write(read(sp + 4), pack(0x2000, distance))
            calls.append(dict(helper='direction_distance', distance=distance))
        elif address == 0x1118f4:
            uc.mem_write(read(sp + 4), pack(0, step))
            calls.append(dict(helper='step', speed=read(sp + 12), step=step))
        elif address == 0x1366ea:
            uc.reg_write(UC_X86_REG_EAX, 0)
            calls.append(dict(helper='height_angle', substituted=0))
        elif address == 0xdd8f4:
            uc.reg_write(UC_X86_REG_EAX, 0)
            calls.append(dict(helper='height_step', substituted=0))
        else:
            raise AssertionError(f'unexpected execution at {address:x}')
        uc.reg_write(UC_X86_REG_EIP, read(sp))
        uc.reg_write(UC_X86_REG_ESP, sp + 4)
    vm.hook_add(UC_HOOK_CODE, hook)
    vm.emu_start(0x65bb0, STOP, count=2000)
    assert vm.reg_read(UC_X86_REG_EIP) == STOP
    assert vm.reg_read(UC_X86_REG_ESP) == STACK + 4
    return dict(result=vm.reg_read(UC_X86_REG_EAX) & 255,
                position=list(struct.unpack('<iii', vm.mem_read(OBJ, 12))),
                heading=read(HEADING), flags=struct.unpack('<H', vm.mem_read(CMD+10, 2))[0],
                state=list(vm.mem_read(CMD+16, 2)),
                movement=list(struct.unpack('<iii', vm.mem_read(WORK, 12))), calls=calls)

def main():
    if not __debug__:
        raise SystemExit('Run without -O; assertions perform the checks.')
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('executable',type=Path)
    data=ap.parse_args().executable.read_bytes()
    assert hashlib.sha256(data).hexdigest()==HASH, 'unsupported build'
    cases=[]
    def run(name,**kw):
        r=replay(data,**kw);cases.append(dict(case=name,observed=r));return r
    def speed(r):return next(c['speed'] for c in r['calls'] if c['helper']=='step')
    r=run('ramp_up');assert speed(r)==9 and r['result']==0 and r['position']==[0,0,0]
    r=run('ramp_down',speed=12);assert speed(r)==11
    r=run('fixed_speed',flags=0x88);assert speed(r)==10
    r=run('accumulator_saturation',accumulator=250,tick=10);assert r['state'][0]==255 and speed(r)==10
    r=run('preserve_heading',flags=8);assert r['heading']==0x1234
    r=run('force_heading',flags=0x808);assert r['heading']==0x8000
    r=run('turn_toward_path',flags=0);assert r['heading']>0x1234 and r['heading']<0x2000
    r=run('arrival',distance=1<<16);assert r['result']==1 and r['position']==[10<<16,0,0] and r['flags']&0x20 and r['heading']==0x1234
    r=run('arrival_heading',flags=0,distance=1<<16,heading=0x8000);assert r['result']==1 and r['heading']==0x8000
    r=run('height_pending',flags=0x108,distance=1<<16,height=5);assert r['result']==0 and not r['flags']&0x20 and r['position']==[0,0,0]
    print(json.dumps(dict(method='Original control flow; four explicitly substituted math helpers; no gameplay',executable_sha256=HASH,cases=cases),indent=2))

if __name__=='__main__':main()
