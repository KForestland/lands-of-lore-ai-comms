# Source ids STORY-086 through STORY-093

Read-only pack for the finale cards. The task file places this range on L20_BB. L20_BB.MIX sha256 `ea3c167f95626dab4bb509429edae6fed903f80b3364757d0b951001de2f8490`. One identity the book names on these cards, the ruby, was found on L19_BC instead, and that cross-archive row is under STORY-086. Command bytes were framed from the MIX this pass. Opcode 1, opcode 3, opcode 9, opcode 18, opcode 21, and opcode 198 were not entered. A level-change shape is only `020100001c`, and byte 5 stays unread. Definition name-at-index stays LIKELY, same GLOBAL.MIX layout as `source_ids_066_075.md`. An opcode 3 identity is the stored dword. The grant effect stays LIKELY. Stories stay with Astra.

L20 static names, metadata 10431, count 18: Valve Door, R door, L door, Fire pillar, Ice pillar, Summon, Slam wall, Frame, Block, Trigger, Final gateway, Floor Grate, Crystal Key, and five spare slots. Prop templates include Frank's Placenta, Belial Birthed, Ice pillar, Fire source, Ice source, Phy source, Pool Guard, Rift, Crystal, and Death obj. Template Belial Birthed has zero placements. No template or static cstring is Dawn, Luther, ruby, pillar-as-blue, chasm, or brick.

Locals, 27 slots after a 27-byte skip at geometry 239030: 0 Sac_attack_counter, 1 Phy_defense, 2 Ice_def, 3 Fire_def, 4 Evil_Luther_speech_tracker, 5 Good_Luther_speech_Tracker, 6 Luther_1Good_2Evil, 7 Pool_guardian, 8 Fire_trap, 9 Belials_Health, 10 Belials_Magic, 11 Belials_Equipment, 12 Health_depth, 13 Breastplate, 14 Gauntlets, 15 Bracers, 16 Ring, 17 Belials_eq_totals, 18 Birth_sac_damage_track, 19 Equip_Bel_app, 20 Final_Belial_Trigger, 21 Evil_Belial_talking, 22 Good_Belial_Talking, 23 Turrets, 24 First_health_prmpt, 25 Explosions, 26 Trigger_plate. None was bound to an opcode except where a copied command's opcode 198 byte 4 is named as a number below.

Actor-def labels: 0 DRARACLE count 1, 1 DRAR_PH count 1, 2 through 10 BELIAL, 11 HIVEGRD count 2, 12 SCOTIA count 2, 13 IMP_BEL count 12, 14 HIVEGRD count 8, 15 B_HUMAN count 10, 16 B_HUMAN count 10, 17 EYE count 11, 18 EYE count 1. BELIAL placement counts by def byte are 2:1, 3:5, 4:2, 5:2, 6:2, 7:2, 8:2, 9:2, 10:3. A label is not an encounter. No actor def is Dawn or Luther.

Arrivals, heading unconverted: selector 0 (-7387, 4890) heading 49298 region 1243; selector 1 (-2383, 4261) heading 16384 region 316; selector 2 (-2398, 3206) heading 16384 region 1523; selector 3 (-3328, 3104) heading 0 region 595; selector 4 (-928, 1632) heading 0 region 101; selector 5 (-2944, 1152) heading 0 region 521.

Level-change commands, all stream 0, all `020100001c53`: region 1475 group 3786, region 1476 group 3792, region 1477 group 3798, region 1478 group 3804, region 1479 group 3810, region 1484 group 3816, region 1485 group 3822, region 1486 group 3828, region 1487 group 3834, region 1488 group 3840. Byte 5 stays unread.

Opcode 21 owners, byte 4 shown, not read as a filename: prop 4 group 62 byte 4 = 73; prop 5 group 80 byte 4 = 70; prop 6 group 98 byte 4 = 72; prop 7 groups 122 and 140 byte 4 = 69; prop 87 group 770 byte 4 = 65; prop 109 group 1072 byte 4 = 71; regions 1615 through 1619, groups 3918, 3924, 3930, 3936, and 3942, byte 4 = 73, 72, 71, 70, and 69. L20 opcode 3 of horn, ruby, sword, mantle, bow, ghost, prism, or curse: none found.

Placed items, all event lists noted, all height -50, flags 0x0402:

| item | def | name slot | identity | stored x, y | region |
| --- | --- | --- | --- | --- | --- |
| 0 | 64 | 63-Rng Drakfire | 0x6F276CB7 | -4264, 3527 | 714 |
| 1 | 53 | 54-DF bracers | 0xCFBCE9F7 | -4251, 3085 | 1557 |
| 2 | 52 | 53-Dr armor | 0xF5E97D26 | -2486, 2490 | 1602 |
| 3 | 51 | 52-Dr Gaunt | 0xD3B7782E | -2526, 3535 | 681 |

Handlers are 65, 53, 51, and 52. None of those name slots is the ruby. Local slots 13 through 16 are the cstrings Breastplate, Gauntlets, Bracers, and Ring. They were not bound.

## STORY-086

Grade DECODED for the absence of a Dawn template on L20, and for the ruby identity on L19 prop 78. Grade UNKNOWN for clicking Dawn until a curse line. The L20 actor defs do not include Dawn.

L19 prop 78, template Dawn good, stored (2802, 882), height -1000, region 1461, flags 0xD482. The copied groups include opcode 198 byte 4 = 8 with values 1 and 2, and opcode 198 byte 4 = 7 with values 1, 2, and 3. L19 local slot 8 is Click_on_Good_Dawn. L19 local slot 7 is Good_Dawn_item_click. Opcode 198 was not entered. Kind 6 group 1566 contains opcode 3 `03010000d784f8fb00000000`, identity 0xFBF884D7, definition 69, name slot `67-Ruby of trth`, handler 101, byte +8 = 0. That is the only opcode 3 of this identity found on L19 or L20 this pass. L19 actor 39, def DAWNL19, stored (1939, 891), region 2182, is a different region from prop 78.

L20 has the Luther cstrings in local slots 4, 5, and 6. No Luther placement was found under an actor-def label.

## STORY-087

Grade UNKNOWN for a curse cast, for a purple glob, for demons left behind, and for breaking a door. No curse cstring and no glob cstring exist. The ten level-change commands are the list at the top of this file. Their byte 5 was not read as a destination.

Prop 242, template Frank's Placenta, stored (-1160, 4258), height -20, region 262, flags 0x4681, event list 3624. The command body was not copied. Template Belial Birthed has zero placements. Local slot 18 is Birth_sac_damage_track and was not bound.

L door and R door movables are the door rows whose commands were copied. Movables 50 and 51, stored (-4731, 4826) and (-4731, 4876), region 871, flags 0x4582, opcode 1 each other with byte 4 = 100. Movables 53 and 54, stored (-3579, 4754) and (-3529, 4754), region 812. Movables 55 and 99, stored (-1055, 3237) and (-1055, 3187), region 218. Which of these is the door in the curse sentence was not derived.

## STORY-088

Grade DECODED for the Fire pillar and Ice pillar movable rows as placements. Grade UNKNOWN for blue pillars, for a path opening, and for a faux-Scotia fight. No blue cstring exists. The pillar command bodies were not copied, so no shoot effect was read.

Fire pillar movables, static slot 3, flags 0x0582, height -50, every one with a nonzero event list: 57 through 61 at y 4299, x -3340 to -3636, regions 780, 782, 784, and 788; and 85 through 98 across regions 668, 635, 594, 601, 720, 566, 638, 665, 588, 669, 632, 629, 659, and 579. Ice pillar movables, static slot 4, same flags and height, also every one with a nonzero event list: 62 through 84. Prop templates Fire source, Ice source, and Phy source are single rows: prop 197 (-3619, 3431) region 1576, prop 196 (-2650, 2924) region 1540, and prop 195 (-3880, 2630) region 636. Their bodies were not copied.

Actor 48, def SCOTIA, stored (-3539, 3877), height -50, region 766, flags 0x7582. Actor 47, def DRAR_PH, stored (-3576, 3986), height -50, region 766, flags 0x7582. The second SCOTIA is actor 65, stored (-2207, 1180), height -50, region 74. No opcode 3 of a prism identity was found on L20. Definition 7, name slot `8-Prism`, identity 0xE50DCDD9, was not a placed L20 item.

## STORY-089

Grade UNKNOWN for moving pillars and for stairs that lead back up. The ice and fire pillar rows are the table under STORY-088. Their command bodies were not copied. The level-change regions 1475 through 1479 and 1484 through 1488 are the only level-change owners found, and byte 5 stays unread. No stair cstring exists.

## STORY-090

Grade DECODED for six Block controls whose copied child is opcode 20. Grade UNKNOWN for an armory, for a spinning brick, for a white ball, and for a fireball. No brick cstring exists.

| id | static | stored x, y | height | region | flags | group |
| --- | --- | --- | --- | --- | --- | --- |
| control 62 | Block | -1375, 1719 | -110 | 126 | 0x8481 | 8922, opcode 20 |
| control 63 | Block | -1209, 1729 | -110 | 137 | 0x8481 | 8932, opcode 20 |
| control 64 | Block | -1041, 1720 | -110 | 129 | 0x8481 | 8942, opcode 20 |
| control 65 | Block | -870, 1729 | -110 | 138 | 0x8481 | 8952, opcode 20 |
| control 66 | Block | -701, 1718 | -110 | 130 | 0x8481 | 8962, opcode 20 |
| control 67 | Block | -547, 1726 | -110 | 141 | 0x8481 | 8972, opcode 20 |

Each is kind 5 value 1. Opcode 20 was not entered. No Ball O Smoke template exists on L20. The L16 ball and pyramid rows are under STORY-072 and were not joined to these blocks.

## STORY-091

Grade DECODED for the Draracle actor, the DRAR_PH actor, and the two Scotia actors as placements. Grade UNKNOWN for a kill, for forcing doors, and for which door is his room.

Actor 46, def DRARACLE, stored (-6921, 4828), height -50, region 1272, flags 0x7582, event list 4668. Prop 111, template Rift, stored (-6821, 4827), height -30, region 1192, flags 0x1602, event list 1016. The regions differ. The command bodies were not copied. Actor 47 and actor 48 share region 766, as listed under STORY-088. Actor 65 is the other Scotia.

Movable 52, static Final gateway, stored (-3554, 4740), height -50, region 795, flags 0x0582. Its group 9472 is opcode 14 only. Crystal Key controls 0, 1, and 2 are the rows that opcode 1 the door movables, and they are under STORY-092.

## STORY-092

Grade DECODED for the three Crystal Key rows and for the placed armor items. Grade UNKNOWN for a blue bow, for the Dark Sword, for Belial's horn, and for a chasm. No horn opcode 3 and no Darkbow opcode 3 were found on L20. The horn identity's opcode 3 is L19 prop 222, in `source_ids_076_085.md`. The only placed Darkbow row found in this series is L16 item 24.

| control | stored x, y | height | region | opcode 1 targets, byte 4 = 100 |
| --- | --- | --- | --- | --- |
| 0 Crystal Key | -4636, 4913 | -12 | 842 | movables 51 and 50, the R door and L door at (-4731, 4876) and (-4731, 4826) |
| 1 Crystal Key | -3485, 4749 | -15 | 804 | movables 53 and 54, the L door and R door at (-3579, 4754) and (-3529, 4754) |
| 2 Crystal Key | -1043, 3120 | 35 | 417 | movables 99 and 55, the R door and L door at (-1055, 3187) and (-1055, 3237) |

Each key group also has opcode 2 `020100001800`, which is outside the level-change shape, and opcode 9 byte 4 = 18 and byte 4 = 14 on those same indexes. U16 50 and u16 51 each fit a prop, a control, an actor, and a movable. The movable rows of those indexes are the doors named above. The fit is the index plus that static name, not an entered opcode 1.

Actor 75, def byte 2, label BELIAL, stored (-1238, 3207), height -10, region 177, flags 0x7582, event list 8444. That is the only placement of def byte 2. The other BELIAL defs are the counts at the top of this file, and their individual coordinates were not copied. Local slot 20 is Final_Belial_Trigger. Local slots 21 and 22 are Evil_Belial_talking and Good_Belial_Talking. None of those was bound. The actor 75 command body was not copied.

Control 61, static Trigger, stored (-3493, 3843), height -49, region 763, flags 0x0482. Group 8676: opcode 198 `c60000001a01` (byte 4 = 26), opcode 18 words (-3494, 3806, 0), flags 0x0293, heading 62441, raw `120100005af2de0e00009302e9f3003c0000`, opcode 2 `020100002600` outside the level-change shape, and opcode 9 on u16 61. Local slot 26 is Trigger_plate. Opcode 198 was not entered. Later groups are opcode 9 on u16 57 through 64. Each of those indexes fits a prop, a control, a movable, and an actor. The names at those indexes were not re-read this pass.

## STORY-093

Grade DECODED for one DRARACLE placement and for the Luther cstrings being locals rather than actor defs. Grade UNKNOWN for Dawn standing with Luther and for the Draracle appearing and vanishing.

Actor 46 is the only DRARACLE row, under STORY-091. Local slots 4, 5, and 6 are the three Luther cstrings. L20 has no Dawn template and no Dawn actor def. The Dawn good prop and the DAWNL19 actor are the L19 rows under STORY-086. No command copied on L20 was read as an appear or a vanish.
