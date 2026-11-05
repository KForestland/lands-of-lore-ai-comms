# I07 four chip spots

Place L16_CA. No frame was opened. No Godot was run. Names are the I03 tables. Name-at-index stays LIKELY. Opcode 1, opcode 3's grant, opcode 8, opcode 9, opcode 18, opcode 20, opcode 198, and opcode 204 were not entered. The opcode 196 floor formula applies only where byte 6 is 0.

Hintbook lines 5114–5123: spark the globes, take the chip behind the force field, and the room goes dark and floods. Lines 5131–5141: walk a straight line to the gargoyle. Lines 5151–5166: freeze the fountain, break the ice, take the chip. The book's methods are a level-three mist, the lake axe, a storm crystal, the blue bow, and an ice seed. Lines 5171–5200: two boxes on two raised squares, then a third box at the ledge, then run when the ceiling drops. Grade HINTBOOK. Each chip is REQUIRED for the four. The freeze method is any one of the book's list.

## Force field

Movable 79, LIKELY Force Field, is (−5641, −4771), height −70, region 8197, floor −70, ceiling 70. Godot (−5641, 4771). Group 49736 is opcode 20 on itself. Group 49746 is opcode 9 raw `09040c000d00`, u16 12, byte 4 = 13. Index 12 fits more than one table. Item 12, the ivory chip, is (−5644, −4532), region 10120, floor −35, ceiling 70. That is 239 units north. Region 10120 is not a neighbor of 8197.

Props 460 and 461, LIKELY Blue Dracoid Orb, at (−6079, −4680) and (−5219, −4680), each opcode 1 the force field with byte 4 = 100 and opcode 198 with byte 4 = 19. Local slot 19 is the cstring `Item_switcher`. The opcode was not entered. Their opcode 196 on region 10121 has byte 6 = 1, so the floor formula does not apply. Props 462 and 463 name region 8211, and props 464 and 465 name region 8206, both with byte 6 = 9. Same limit. No globe cstring is on these rows. Sparking them stays the book.

## Gargoyle walk

Three LIKELY Ivory Chip Gargoyle props. Prop 400 at (−7544, −3171), region 8626, has no events. Prop 399 at (−9653, −3160), region 8510, group 14678 is opcode 198 byte 4 = 22, opcode 5, opcode 3 `03010000090c2e0404000000` (identity 0x042E0C09, byte +8 = 4), and opcode 16. Local slot 22 is `Trap_solved`. The opcode was not entered. Prop 223 at (−4406, −1537), region 8186, floor 50, ceiling 200, group 6126 is 21 opcode 196 commands. Nineteen use word +4 = 50 and two use 40. Byte 6 is 1 and byte 7 is 7, so the floor formula does not apply. The straight walk stays the hintbook sentence.

## Fountain

The ivory opcode 3 with byte +8 = 1 is control 72, LIKELY Chip, at (−2283, −11613), sharing region 8680 with Geyser prop 419. That group was copied in the earlier pack and was not re-copied here. Region 8680 is floor 45, ceiling 420. No weapon identity is in the commands this pass read. The freeze methods stay HINTBOOK.

Prop 626, LIKELY Fountain, is a different row: (−4111, −15457), height 90, region 4900, floor 90, ceiling 300. Godot (−4111, 15457). Group 40538 is opcode 198 byte 4 = 16. Local slot 16 is the cstring `Ice_fountain_trigger`. The opcode was not entered. The same prop also stores opcode 2 raw `020100001800` and two copies of `020100000b05`. Arm 0x0b is I30. Group 40640 is opcode 9 byte 4 = 21 on prop 221, the Light Source at (−3767, −15326). Prop 221's group is 21 opcode 204 commands. Opcode 204 was not entered.

## Two small drops

Controls 71 and 108, LIKELY Push/Pull object, are the two scripted slides.

| control | native | opcode 196 region | current floor | target | speed | delta | opcode 18 words | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 71 | (−5214, −1470) | 8020 | 22 | 18 | 8 | −4 | (−4967, −1562, 0) | 0x0004 |
| 108 | (−5250, −1641) | 8116 | −28 | −32 | 8 | −4 | (−5011, −1364, 0) | 0x0004 |

Byte 6 is 0, so this is the accepted formula. Bit 0x0004 is set and the target is the control itself, not u16 0. Control 107 at (−3951, −1379) is the third Push/Pull and has no events. Four Urn props and three Geyser props sit in the same neighborhood. The book’s two vases and three fountains were not matched one-to-one. The ceiling drop stays UNKNOWN.

## Still open

Opcode 9 on u16 12. The globe spark. The gargoyle floors, because byte 6 is 1. Which freeze method the original accepts. The ceiling. No frame.
