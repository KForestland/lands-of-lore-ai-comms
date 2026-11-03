# Source ids STORY-076 through STORY-085

Read-only pack. The task file puts this range on L17_HC and L19_BC. The readable rows do not all sit there. STORY-076, STORY-077, and STORY-078 are L16_CA. STORY-079 is L17_HC. STORY-080 through STORY-085 are L19_BC. Command bytes below were framed from those MIX files this pass. Opcode 1, opcode 3, opcode 9, opcode 18, opcode 21, and opcode 198 were not entered. A level-change shape is only `020100001c`, and byte 5 stays unread. Definition name-at-index stays LIKELY, same GLOBAL.MIX layout as `source_ids_066_075.md`. An opcode 3 identity is the stored dword. The grant effect stays LIKELY. Stories stay with Astra.

L16 rows already listed in `source_ids_066_075.md` are not repeated in full. L16 locals used here are slot 0 Star_Elevator, slot 1 Got_mantle, slot 6 Trigger_1st_tower_pylon, slot 7 Trigger_2nd_tower_pylon, slot 8 Trigger_3rd_tower_pylon, slot 9 Trigger_4th_Tower_pylon, slot 12 Mantle_conveyed, slot 13 Belials_access, and slot 21 Hanging_drac. None was bound to an opcode.

No template or static cstring on these three archives is box, hole, yellow, figure, bar, guck, strand, frond, ghost, fountain, or spider. L19 static Bar door has zero placements.

## STORY-076

Place L16_CA. Grade DECODED for the four pylon and iris rows in the STORY-069 table, and for the center Shape rows being event 0. Grade UNKNOWN for a square hole, for a box, and for a yellow eight-sided figure.

Static Tower Hole, Teleporter, heaven stair, and Staged Button have zero placements. No movable is stored with x from 11000 to 16000 and y from -9000 to -4000. The four Iris Door controls are the only door rows on the four pylon regions.

Ten Shape props sit on the ring around prop 615, the center Tower at (13273, -6464), event 0. All ten are height 80, flags 0x0002, event 0.

| id | template | stored x, y | region |
| --- | --- | --- | --- |
| prop 365 | Shape 4 | 4858, -6515 | 8906 |
| prop 366 | Shape 4 | 4865, -7551 | 9224 |
| prop 367 | Shape 4 | 6182, -6522 | 8883 |
| prop 368 | Shape 4 | 6174, -7551 | 10080 |
| prop 369 | Shape 3 | 6318, -7422 | 8900 |
| prop 370 | Shape 3 | 4750, -7422 | 8924 |
| prop 371 | Shape 1 | 6311, -7170 | 8895 |
| prop 372 | Shape 1 | 4728, -7156 | 8918 |
| prop 373 | Shape 2 | 4721, -6904 | 8914 |
| prop 374 | Shape 2 | 6297, -6911 | 8893 |

Templates Bool and Bright Star have zero placements. The pylon groups copied under STORY-069 contain no opcode 198, so the four Trigger_Nth_tower_pylon cstrings were not bound. Local slot 0 remains the cstring Star_Elevator.

## STORY-077

Place L16_CA. Grade DECODED for four Mantle props with event 0. Grade UNKNOWN for a fight, for bars of light, and for taking a mantle. No placed item on L16 is named mantle. Static Mantle Gate has zero placements.

| id | stored x, y | height | region | floor | ceiling |
| --- | --- | --- | --- | --- | --- |
| prop 331 | 5443, -9749 | 10 | 223 | 0 | 200 |
| prop 332 | 5578, -9751 | 10 | 228 | 0 | 200 |
| prop 333 | 5636, -9879 | 10 | 214 | 0 | 200 |
| prop 348 | 5384, -9879 | 10 | 215 | 0 | 200 |

All four are template Mantle, flags 0x0002, event 0. Local slot 1 is Got_mantle. Local slot 12 is Mantle_conveyed. Local slot 13 is Belials_access. L16 actor-def labels are VISC, HL3, bacl16, VISC, B_HUMAN, and B_HUMAN. None of those labels is Belial.

## STORY-078

Place L16_CA. Grade DECODED for the Dragon row and for the Dragon Statue being a different row. Grade UNKNOWN for a chop, for a picture, for a one-way teleporter, and for a mantle prerequisite. Static Teleporter has zero placements.

Prop 241, template Dragon, stored (1625, -4417), height 52, region 9476, floor 50, ceiling 155, neighbors 9492, 9475, 9460, 9477, flags 0x4481. Kind 9 group 6384: opcode 9 on u16 241 byte 4 = 18, opcode 9 on u16 73 byte 4 = 3 and byte 4 = 21, opcode 16, opcode 5, and three opcode 7. Kind 6 group 6438: opcode 9 on u16 241 byte 4 = 17, opcode 5, and two opcode 7. U16 73 fits a prop, a control, and a movable. The dragon groups contain no opcode 198, so Hanging_drac was not bound.

Prop 144, template Dead dragon, stored (1623, -4946), height 35, region 9965, flags 0x0082, event 0. Props 237 through 240, template Sm Dragon, and props 141 through 143, template Sm dead drag, sit in that same neighborhood and are event 0. Prop 211, template Dragon Statue, stored (261, -10600), height 50, region 9783, flags 0x0002, event 0. That coordinate is not the dragon's coordinate.

Control 74, static Telepad, stored (2100, -4296), region 9615, is the level change `020100001c31` from STORY-067. Arrival selector 2 is (2107, -4183), region 9603. The regions differ. The telepad's neighbors are 9604, 9614, 9606, and 9616, and 9603 is not among them.

## STORY-079

Place L17_HC.MIX sha256 `23d7cecf44e83515934083ae101eb4b023dfb748d34e5e0b6eb3c8aca75cc793`. Grade DECODED for the cave template names and for movable 50's level-change bytes. Grade UNKNOWN for green spiders, brown spiders, and an exit. No spider cstring and no exit cstring exist. Items are zero.

Static names, metadata 8534, count 13: Green ceil, Green flr, Purp flr, Purp ceil, Fish skel, Scratches, Floor gems, Teleport circle, and five Spare BD slots. Prop templates include Wide guts, Long guts, Gut stub, Intestine, Hive Duct, stalag1 through stalag4, Yellow Crystal, Red Crystal, Green Crystal, Purple Crystal, and Lichen. The one local, after a 1-byte skip at geometry 159043, is Platform_trigger.

Actor defs: 0 HIVEW count 58, 1 HIVEGRD count 4, 2 B_HUMAN count 10, 3 B_HUMAN count 10. A definition label is not an encounter.

Arrivals, heading unconverted: selector 0 (-4721, -6700) heading 61004 region 109; selector 1 (1434, 7075) heading 32768 region 131; selector 2 (-5732, -5829) heading 49152 region 1311; selector 3 (8089, -2128) heading 53703 region 1315.

Level-change commands: movable 50, stream 1 group 3896, `020100001c50`; region 1312 group 1632 and region 1313 group 1638, both `020100001c33`; region 1318 group 1644, `020100001c70`. Byte 5 stays unread. The one opcode 18 is region 1293, stream 0 group 1566, words (-6084, -6404, 0), flags 0x0005, heading 18386. Opcode 18 was not entered. No opcode 21 was found.

Movable 50, static Teleport circle, stored (1439, 7256), height 135, region 118, flags 0x0581. Group 3896 contains opcode 198 byte 4 = 0, opcode 9 on props 308, 307, 309, and 310 with byte 4 = 17, opcode 1 on movable 50 with byte 4 = 0, and the level-change above. Those four props are the colored crystals at (1308 to 1561, 7144 to 7382). Local slot 0 is Platform_trigger. Opcode 198 byte 4 = 0 was not bound to it.

Wide guts props with events include prop 99, stored (-6243, -5890), region 1302, flags 0x4482. Its groups are opcode 5, opcode 16, opcode 20, and opcode 9 on itself. Hive Duct prop 153, stored (-4993, -7063), region 79, has opcode 2 `020100000c05` and `020100000b05`, both outside the level-change shape.

## STORY-080

Place L19_BC.MIX sha256 `59cd77a17e8fce0286281fdea17e134fc88436cbc0c77b1a5f4039e5edde3380`. Grade DECODED for the sewer and lab cstrings and for prop 222's horn identity. Grade UNKNOWN for red strands, for a green frond, and for a mapped exit. No strand cstring and no frond cstring exist.

Static names, metadata 7743, count 20, include Golden Door, Metal beam, Sewer door, Switch, Sewer frame, Sewer seal, Bridge, Summoning disk, Fake wall, and Bar door. Bar door has zero placements. Sixteen Metal beam controls are event 0. Prop templates include Blood bowl, Ooze normal, Ooze small, Ooze pipe, Beaker0 through Beaker3, Dawn good, Remains, and Skull.

Locals, 13 slots after a 13-byte skip at geometry 297237: 0 Sewer_block_1, 1 Blood_bowl_timer_on, 2 Drop_down_sewer_door, 3 Lab_elevator, 4 Lab_elevator_two, 5 Evil_Dawn_encounter, 6 Good_Dawn_encounter, 7 Good_Dawn_item_click, 8 Click_on_Good_Dawn, 9 Level_entered, 10 Evil_Dawn_is_now_a_monster, 11 Imp_summoner, 12 Imp_doors_open.

Actor defs: 0 DAWNL19 count 1, 1 SWARMER count 28, 2 SEWER count 17, 3 BELSTAT count 1, 4 IMP_BEL count 1, 5 B_HUMAN count 10, 6 B_HUMAN count 10. Actor 39, def 0, stored (1939, 891), height -125, region 2182. Actor 32, def 3, stored (18, 596), height -10, region 616.

Arrivals: selector 0 (1405, 1253) heading 4798 region 1691; selector 1 (84, -305) heading 49152 region 25; selector 2 (3201, 872) heading 49152 region 2365; selector 3 (1260, 1431) heading 0 region 1715.

Level changes: region 22 stream 0 group 0 `020100001c51`; region 2369 groups 15784 and 15790, `020100001c34` and `020100001c54`. Byte 5 stays unread.

Prop 222, template Ooze pipe, stored (120, -525), height 0, region 687, flags 0x0402. Kind 6 group 2778: opcode 21 `152038004000` (u16 56, byte 4 = 64), opcode 3 `03010000902cbe0c01000000`, opcode 198 byte 4 = 9, opcode 9 u16 269 byte 4 = 21. The opcode 3 identity is 0x0CBE2C90, definition 22, name slot `23-Hrn Belial`, handler 0, byte +8 = 1. Group 2814 repeats opcode 21 with byte 4 = 58 and a second opcode 3 of the same identity, byte +8 = 1, whose u16 at +2 is 32. Props number 270, so u16 269 fits only a prop: prop 269, Blood bowl, stored (13, 899), region 686. Opcode 21 byte 4 was not read as a filename. Local slot 9 is Level_entered. Opcode 198 was not entered.

Prop 223, the other Ooze pipe at (39, -526), region 687, has opcode 3 of the Darkbow identity 0xD58C34FE, byte +8 = 4, in group 2862. That is not the horn.

## STORY-081

Place L19_BC for the horn command. Grade LIKELY for the horn identity on prop 222, because opcode 3 was not entered. Grade UNKNOWN for Baccata and for taking the horn before a death. The L16 actor-def label bacl16 is not an L19 actor. L19's single BELSTAT placement is actor 32, region 616. Prop 222 is region 687. Those regions were not joined.

The horn bytes are the two opcode 3 commands under STORY-080. No placed item on L19 exists. The item count is 0, so the horn is not a placed row.

## STORY-082

Place L19_BC. Grade DECODED for three Switch movables on one stored y and for the one Sewer door. Grade UNKNOWN for bars, for a gutter, for guck, and for a Human or Lizard test. No guck cstring exists. Ooze normal, Ooze small, and Ooze pipe are the ooze templates.

Movables 74, 75, and 76, static Switch, stored (-323, 2124), (-304, 2124), and (-281, 2124), height 42, regions 36, 34, and 32, flags 0xC581. Movable 74 was copied. Kind 5 group 5882 is opcode 16 and opcode 1 `01204a006400` (u16 74, byte 4 = 100). Kind 6 group 5930 ends in opcode 1 `01204d006400` (u16 77, byte 4 = 100). Kind 6 group 6182 has opcode 1 `01204d000000` (u16 77, byte 4 = 0). Movable 77 is the Sewer door below. Movables 75 and 76 have event lists 3632 and 3676. Their children were not copied, so they were not asserted to match 74.

Movable 77, static Sewer door, stored (-344, 1621), height -38, region 738, flags 0x0581. Its copied group 7898 is opcode 196 only. Two Sewer seal movables also have event lists. Their bodies were not copied. Sixteen Metal beam controls are event 0, and Bar door has zero placements.

## STORY-083

Place L19_BC. Grade DECODED for the paired opcode 1 values on the north switches. Grade UNKNOWN for draining and for running through.

Movables 50, 71, and 72 are the other three Switch rows: (1535, 3282) region 213, (1622, 3609) region 609, and (1629, 3246) region 606. Movables 50 and 71 were copied and match. Each has two kind 4 groups. One group is opcode 198 byte 4 = 2 with value 1, then opcode 1 byte 4 = 100 on movables 70, 50, 71, and 72. The other group is opcode 198 byte 4 = 2 with value 0, then opcode 1 byte 4 = 0 on those same four. Local slot 2 is Drop_down_sewer_door. Opcode 198 was not entered. Movable 70 is the Bridge, stored (1586, 3413), region 214, flags 0x0581. Movable 72's children were not copied.

## STORY-084

Place L19_BC. Grade UNKNOWN for a short path, for a right-then-right route, and for rapids. Eighteen Golden Door movables have event lists. One was copied.

Movable 51, static Golden Door, stored (2550, 854), height -100, region 1931, flags 0x0582. Group 3854: opcode 198 byte 4 = 4 with value 0, opcode 196, opcode 16, and opcode 1 byte 4 = 100 on movables 51 and 52. Group 3998 is opcode 1 byte 4 = 0 on 51 and 52. Local slot 4 is Lab_elevator_two. The opcode was not entered. The other seventeen Golden Door coordinates were read and were not reduced to a path.

## STORY-085

Place L19_BC. Grade DECODED for four Skull rows in one rectangle, for the Summoning disk, and for the IMP_BEL actor in that disk's region. Grade UNKNOWN for ghostly heads, for mists of doom, for a white circle, and for a red fountain. No ghost cstring and no fountain cstring exist.

| id | template | stored x, y | height | region | flags |
| --- | --- | --- | --- | --- | --- |
| prop 67 | Skull | 1451, 1131 | -60 | 1671 | 0xC681 |
| prop 69 | Skull | 1018, 1128 | -60 | 1626 | 0xC681 |
| prop 68 | Skull | 1028, 1892 | -60 | 1669 | 0xC681 |
| prop 70 | Skull | 1451, 1891 | -60 | 1685 | 0xC681 |
| prop 66 | Skull | 2426, 882 | -75 | 1972 | 0x0402 |

Prop 65, template Light, stored (1306, 1444), region 1706, group 66, has four opcode 18 commands, flags 0x0112, height word -60, words (1450, 1132), (1019, 1128), (1026, 1893), and (1450, 1893), with u16 targets 67, 69, 68, and 70. Those words match the four rectangle skulls. Each of props 67 through 70 then has opcode 18 on itself, flags 0x0313, height word -20, with the stored x and y jittered by a few units. Opcode 18 was not entered. Prop 66's group is opcode 15 and opcode 9 on itself. It is the fifth skull and is not in the rectangle.

Control 57, static Summoning disk, stored (1240, 1454), height -120, region 1706, flags 0x0482. Its group 3660 is opcode 5 only. Actor 31, def IMP_BEL, stored (1247, 1445), height -120, region 1706, flags 0xFC82. Prop 65 shares that region. Local slots 3 and 4 are Lab_elevator and Lab_elevator_two. Neither cstring was bound to the disk group.

The ruby identity is not this card. It is on L19 prop 78 and is recorded under STORY-086 in `source_ids_086_093.md`, because that is the card whose book sentence names the ruby.
