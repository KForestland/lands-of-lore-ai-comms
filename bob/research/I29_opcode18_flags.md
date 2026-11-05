# I29 opcode 18 flags

The opcode 18 callee was not entered. Bit 0x0004 is the already proven direct-relocation bit. A command whose flag word does not have that bit is not a relocation. No byte was read as a speed.

L16 has 77 opcode 18 commands. Twenty-nine have bit 0x0004 set. Forty-eight do not.

| flag | count | bit 0x0004 |
| --- | --- | --- |
| 0x0008 | 18 | clear |
| 0x0112 | 14 | clear |
| 0x0804 | 12 | set |
| 0x0C04 | 9 | set |
| 0x0004 | 6 | set |
| 0x0812 | 4 | clear |
| 0x0912 | 4 | clear |
| 0x0A81 | 4 | clear |
| 0x0009 | 2 | clear |
| 0x0005 | 1 | set |
| 0x0404 | 1 | set |
| 0x0809 | 1 | clear |
| 0x0908 | 1 | clear |

0x0804 includes bit 0x0004, so those twelve are the relocation form. The extra bit 0x0800 was not given a drift meaning. The twelve owners are region 233 (target 0), prop 609, props 637–639, controls 119, 120, 122, and controls 185–188. The three signed words are the stored coordinates. They were not read as a velocity.

0x0812 does not include bit 0x0004. The four commands sit on props 600, 601, 602, and 603, target the same prop, height word 0. They are not relocations. No speed was read.

0x0004 by itself is six commands: prop 418 twice (target 0), prop 640, and controls 71, 108, and 121.

L19 has 23 opcode 18 commands and every flag word has bit 0x0004 clear. The four skull commands are 0x0112. L17 has one, flags 0x0005, so the bit is set. L20 has 68: 49 with the bit, 19 without. The L20 words were not split into a speed.

## Still open

What 0x0800, 0x0812, 0x0912, 0x0112, and 0x0A81 do. A speed field. Target 0.
