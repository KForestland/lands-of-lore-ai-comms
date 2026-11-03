"""Exact-build height and flood checks; supplied regions/clock, no gameplay.
Requires unicorn. Reads local LOLG.DAT; emits no game bytes.
"""
import argparse, hashlib, json, struct
from pathlib import Path
from unicorn import Uc, UC_ARCH_X86, UC_MODE_32, UC_HOOK_CODE
from unicorn.x86_const import UC_X86_REG_ESP, UC_X86_REG_EIP, UC_X86_REG_EAX
from check_opcode18_direct import HASH, pack
OBJ, REGION, LINK, CMD, DESC, STACK, STOP = 0x300000,0x310000,0x320000,0x330000,0x340000,0x400000,0x500000

def machine(data,ranges):
    vm=Uc(UC_ARCH_X86,UC_MODE_32);vm.mem_map(0,0x510000)
    for a,b in ranges:vm.mem_write(a,data[a+0x37000:b+0x37000])
    return vm

def call(vm,entry,args,hook):
    vm.mem_write(STACK,pack(STOP,*args));vm.reg_write(UC_X86_REG_ESP,STACK)
    vm.hook_add(UC_HOOK_CODE,hook)
    vm.emu_start(entry,STOP,count=10000)
    assert vm.reg_read(UC_X86_REG_EIP)==STOP and vm.reg_read(UC_X86_REG_ESP)==STACK+4
    return vm.reg_read(UC_X86_REG_EAX)

def height(data,direct,floor,depth,start,sloped=False):
    ranges=[(0xd0204,0xd024f),(0xaf260,0xaf4a6)]
    vm=machine(data,ranges);calls=[]
    vm.mem_write(OBJ+8,pack(start));vm.mem_write(OBJ+12,pack(LINK));vm.mem_write(LINK+4,pack(REGION))
    vm.mem_write(OBJ+0x14,pack(0x20000000));vm.mem_write(OBJ+0x227,b'\xff')
    vm.mem_write(REGION+0x14,struct.pack('<h',floor));vm.mem_write(REGION+0x27,bytes([depth]))
    vm.mem_write(REGION+0x1c,struct.pack('<H',4 if sloped else 0))
    def u32(a):return struct.unpack('<I',vm.mem_read(a,4))[0]
    def hook(uc,a,size,_):
        if any(lo<=a<hi for lo,hi in ranges):return
        sp=uc.reg_read(UC_X86_REG_ESP)
        if a==0xaf0e0:uc.reg_write(UC_X86_REG_EAX,REGION);calls.append('supplied_region_binding')
        elif a==0xf4614:uc.reg_write(UC_X86_REG_EAX,123<<16);calls.append('substituted_slope_height')
        elif a==0xaf9a4:uc.reg_write(UC_X86_REG_EAX,1);calls.append('substituted_collision_pass')
        elif a in (0x1548d8,0x14f8a4):calls.append('substituted_scratch_copy_or_clear')
        else:raise AssertionError(f'unexpected call {a:x}')
        uc.reg_write(UC_X86_REG_EIP,u32(sp));uc.reg_write(UC_X86_REG_ESP,sp+4)
    call(vm,0xd0204,[OBJ,int(direct)],hook)
    actual=struct.unpack('<i',vm.mem_read(OBJ+8,4))[0]
    expected=(123<<16 if sloped else (floor-depth)<<16) if direct else start
    assert actual==expected
    assert bool(vm.mem_read(OBJ+0x227,1)[0]&0x10)==(not direct)
    return dict(direct=direct,floor=floor,region_byte27=depth,sloped=sloped,height=actual,substitutions=calls)

def flood(data,floor,ceiling,target,rate,ticks):
    ranges=[(0x65518,0x6583a),(0xf3a5c,0xf3b03)]
    vm=machine(data,ranges)
    command=struct.pack('<BBHBBh',208,0x90,0,1,rate,target)
    vm.mem_write(CMD,command);vm.mem_write(0x22d0c,pack(REGION));vm.mem_write(0x22d10,pack(DESC))
    vm.mem_write(0xbbb4,pack(ticks));vm.mem_write(0x2b534,pack(1))
    vm.mem_write(REGION+4,b'\xff'*8)
    vm.mem_write(REGION+0x14,struct.pack('<hh',floor,ceiling))
    vm.mem_write(DESC+0x17,b'\x01')
    def hook(uc,a,size,_):
        assert any(lo<=a<hi for lo,hi in ranges),f'unexpected execution {a:x}'
    result=call(vm,0x65518,[CMD,0],hook)
    step=rate*ticks//60
    changed=step>0 and step<=ceiling-floor-1 and floor+step<=target
    # Bounded cases below never enter the other ceiling branch.
    assert step<=ceiling-floor-1
    newfloor=struct.unpack('<h',vm.mem_read(REGION+0x14,2))[0]
    assert newfloor==floor+(step if changed else 0)
    assert bool(vm.mem_read(REGION+0x28,1)[0]&0x20)==changed
    assert vm.mem_read(REGION+0x27,1)[0] == (min(255,step) if changed else 0)
    assert result==(0 if changed or step==0 else 1)
    return dict(floor=floor,target=target,rate=rate,ticks=ticks,step=step,new_floor=newfloor,result=result,dirty=changed)

def main():
    if not __debug__:raise SystemExit('Run without -O')
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('executable',type=Path)
    data=p.parse_args().executable.read_bytes();assert hashlib.sha256(data).hexdigest()==HASH
    assert data[0x39024:0x39026] == b'MZ'
    assert 0x39024 + struct.unpack_from('<I',data,0x39024+0x3c)[0] == 0x3bcb4
    assert struct.unpack_from('<I',data,0x1c1024+0x5c20+0x18)[0] + 0x59024 == 0xd0204
    cases=[height(data,*a) for a in [(True,200,0,20<<16),(True,20,0,200<<16),(True,100,30,0),(True,-10,5,0),(False,200,0,20<<16),(True,0,0,0,True)]]
    water=[flood(data,*a) for a in [(0,200,70,3,20),(0,200,70,3,60),(69,200,70,3,60),(70,200,70,3,20),(0,200,70,3,1)]]
    print(json.dumps(dict(executable_sha256=HASH,height_cases=cases,flood_cases=water,scope='Synthetic region and clock state. Height binding/slope/collision/scratch helpers substituted; flood code uses original instructions without helper substitutions on these paths.'),indent=2))
if __name__=='__main__':main()
