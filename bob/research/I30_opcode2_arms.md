# I30 opcode 2 arms 0x10, 0x0B, and 0x0C

The calls at 0xD8B94 and 0xD8A1C were not entered. File offset is VA + 0x37000. LOLG.DAT length 1977007.

The dispatch that reaches these arms is the compare tree, not a jump table.

At 0xD872D, `cmp ah, 0x11` / `jb 0xD8897` sends ah below 0x11 to 0xD8897. That was the only jump to 0xD8897 in VA 0xD6000..0xDA000. At 0xD8897, `cmp ah, 8` sends ah above 8 on to 0xD88A6. There `cmp ah, 0x0C` sends ah below 0x0C to 0xD8927 and ah equal to 0x0C to 0xD7C18. At 0xD8927, `cmp ah, 0x0A` leaves ah equal to 0x0B to fall into 0xD8936. After the 0x0C test, `cmp ah, 0x0E` and `cmp ah, 0x0F` peel off 0x0D, 0x0E, and 0x0F. The fall-through at 0xD88CD is ah above 0x0F and, from the parent, below 0x11. That is arm 0x10.

## Arm 0x10 at 0xD88CD

If the byte at [0x223D4] is not 0, the arm jumps to 0xD89F6. Otherwise it reads [esi+5], adds the byte at [ebx+0x162], and caps the sum at 30. While the byte at [ebx+0x162] is still below that sum, it takes the dword at [that byte * 4 + 0xE810], subtracts the dword at [ebx+0x15D], and calls 0xD8B94. The call was not entered, so the write that would advance the byte is not in this window. The byte was not renamed from a string.

## Arms 0x0B and 0x0C

Both arms leave immediately when the byte at [0x223D4] is not 0. Both compute byte-at-register-plus-5 times 100: times 4, minus the byte, shift left 3, add the byte, shift left 2. Arm 0x0B at 0xD8936 reads [esi+5] and calls 0xD8A1C. Arm 0x0C at 0xD7C18 reads [edx+5] and calls 0xD8B94. Neither call was entered. A direct store of the product is not in either window.

## Stored commands

L16. Arm 0x10 is one command, `020100001002`, on prop 378. The last byte is 2. Arm 0x0B `020100000b05` is on props 600, 603, and 626 (626 has it twice). Arm 0x0C `020100000c05` is on props 601 and 602. The last byte on those is 5, so the product above is 500 when that register is the command.

L17. Props 153, 154, 155, and 156 each store both `020100000b05` and `020100000c05`. L19 and L20 store none of these three raws.

## Still open

The two calls. What the byte at [ebx+0x162] is. The byte at [0x223D4]. Whether esi and edx are the command pointer on these arms.
