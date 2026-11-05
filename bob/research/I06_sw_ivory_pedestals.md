# I06 SW ivory pedestals

Place L16_CA. No frame was opened. No Godot was run. Names are the I03 tables. Name-at-index stays LIKELY. Opcode 1, opcode 2, opcode 3's grant, opcode 9, opcode 14, opcode 15, opcode 18, and opcode 20 were not entered.

Hintbook lines 4941–4954: with four ivory chips, place one on each pedestal in the southwest foyer. The pyramid shatters, a fireball opens the tower door, and the box goes through the shimmering disk. Grade HINTBOOK. Brady printed 127 and printed 233 step 9 say the same placement, the shatter, and the tower. Grade BRADY. Placing four chips is REQUIRED. Two of them may be the museum carry. No museum save was read, so that carry stays UNKNOWN.

## The four receptacles

Controls 173–176 are LIKELY Ivory Chip Block, height 30, flags 0x0402. Each region is about 8 units wide, floor 0, ceiling 180.

| control | native | Godot | region |
| --- | --- | --- | --- |
| 173 | (−10089, −12935) | (−10089, 12935) | 7126 |
| 174 | (−9949, −12936) | (−9949, 12936) | 7102 |
| 175 | (−9645, −12936) | (−9645, 12936) | 7109 |
| 176 | (−9505, −12936) | (−9505, 12936) | 7115 |

Each kind 4 group (48698, 48738, 48778, 48818), value 3, is the same five commands: opcode 9 byte 4 = 21 on prop 139, opcode 20 on that block, opcode 9 byte 4 = 21 on control 172, opcode 2 raw `020100001800`, and opcode 5 on the block. `020100001800` is not the level-change shape `020100001c`. None of the four groups contains opcode 3. They do not grant a chip.

Props 618–621, LIKELY Pipe, sit on those same four x values at y −13030, height about −25. Each has one kind 1 record. Kind 1 was not read as commands.

The placed ivory rows are items 12, 22, and 23, identity 0x042E0C09, name slot `105-Ivory chip` LIKELY. They are at (−5644, −4532), (5491, −10096), and (−2853, 1534). None is in this foyer. Three is the placed count. A fourth placed chip was not found.

## Pyramid, ball, doors

Prop 604, LIKELY Pyramid, is (−9793, −12994), height −18, region 6943, floor 0, ceiling 150. Group 37944 is opcode 9 on prop 601, byte 4 = 3 and byte 4 = 21.

Prop 601, LIKELY Ball O Smoke, is (−9797, −13070), height 15, region 6960, floor 0, ceiling 150. Group 37690 is opcode 18 on itself, words (−9808, −14344, 0), flags 0x0812. Bit 0x0004 is clear. The words sit on FireWall doors 89, 90, and 91 at y −14335, x −9759, −9859, and −9809. Those doors have no events. Godot for the ball is (−9797, 13070).

The same group has opcode 2 raw `020100000c05` and opcode 1 byte 4 = 100 on u16 90, 91, and 89. Each of those indexes also fits a prop and a control. The movable fit is these three doors. The command does not pick the table. Arm 0x0c is I30.

Control 172, LIKELY crystal wall, is (−9795, −13206), region 10065, floor 0, ceiling 150. Group 48656 is opcode 14, opcode 20 on prop 140, opcode 9 byte 4 = 21 on pyramid 604, and opcode 7. The chip blocks name this wall, and the wall names the pyramid.

## The disk

Past the doors, control 115, LIKELY Key Object, is (−9798, −14609), height 100, region 3453, floor 100, ceiling 800. Godot (−9798, 14609). Group 43132 is opcode 9 byte 4 = 3 on control 122 and opcode 9 byte 4 = 2 on itself. Control 122 is the star-field key at (10605, −9187). Opcode 9 was not entered, so this is the stored link, not a proven transport. Gates 169 and 170 at (−9803, −14528) and (−9803, −14518), region 3443, have no events. No box name is stored here.

## Still open

Opcode 9 along the chip, wall, pyramid, and key chain. Opcode 2 arm 0x18 on the blocks. The fourth chip and the museum carry. The box. No frame.
