# Source ids STORY-066 through STORY-075

Read-only pack. STORY-066 is L14_HT. STORY-067 through STORY-075 are L16_CA. Placements, name tables, and command bytes were read from those MIX files this pass. The geometry streams were framed with the published opcode sizes. The JSON exports were not the source of the command lists. Opcode 1, opcode 3, opcode 9, opcode 12, opcode 16, opcode 18, opcode 20, opcode 21, opcode 196, opcode 197, opcode 198, and opcode 204 were not entered. A stored opcode 18 word pair is the two signed words at bytes +4 and +6. A level-change shape is only `020100001c`, and byte 5 stays unread. Definition name-at-index stays LIKELY: GLOBAL.MIX key 3984507021, record base 496, stride 91, identity at +24, handler at +0x42, 30-byte name slots at 20734. An opcode 9 u16 is a table fit by size only. Stories stay with Astra.

L14_HT.MIX sha256 `c294f9ab142b55c36fff545a1293c419c42353fedefbfe8b77b9c38a2d9a0719`. Template names are the 38-byte table at metadata 9592, count 66. Static names are the 30-byte run at metadata 31148, count 96. Locals are 28 slots after a 28-byte skip at geometry 423636, the same run as `source_ids_054_060.md`. Slot 22 is the cstring `go_to_level_16`. That cstring was not read as a destination.

L16_CA.MIX sha256 `810d39ae20a980c4b912fda9dbb05db7917b879fbfcc7cdf4a9f91d26707d2a4`. Template names are the 38-byte table at metadata 19958, count 136. Static names are the 30-byte run at metadata 44418, count 87. Locals are 24 slots after a 24-byte skip at geometry 1000261. Names: 0 Star_Elevator, 1 Got_mantle, 2 Hourglass_on, 3 Has_Water_been_started, 4 Is_Water_already_pooled_in_planter, 5 How_many_tower_keys_have_been_placed, 6 Trigger_1st_tower_pylon, 7 Trigger_2nd_tower_pylon, 8 Trigger_3rd_tower_pylon, 9 Trigger_4th_Tower_pylon, 10 How_may_orbs_have_been_charged, 11 Fire_puzzle_triggered, 12 Mantle_conveyed, 13 Belials_access, 14 Mikes_variable, 15 Ice_door_trigger, 16 Ice_fountain_trigger, 17 Item_room_trap, 18 Big_Doors, 19 Item_switcher, 20 Item_doors, 21 Hanging_drac, 22 Trap_solved, 23 Silverleaf_clue. None of those cstrings was bound to an opcode.

L16 arrivals, heading unconverted: selector 0 (5575, -9185) heading 16144 region 9655; selector 1 (-3860, 1341) heading 1 region 137; selector 2 (2107, -4183) heading 0 region 9603; selector 3 (-7820, -10696) heading 61895 region 9824.

L16 level-change commands re-found this pass: control 74, stream 1 group 42056, `020100001c31`; region 9822, stream 0 group 7268, `020100001c71`. L16 opcode 21 owners: actor 45, stream 1 group 54352, `15034f015200`, byte 4 = 82; region 233, stream 0 group 564, `1503a8021b00`, byte 4 = 27. Byte 4 was not read as a filename.

No L14 or L16 template or static cstring is chalice, box, brick, disk, bow, yellow, head, southwest, or dry. Stories stay with Astra.

## STORY-066

Grade DECODED for the chamber-door rows, for prop 170's level-change bytes, and for the absence of a chalice cstring. Grade UNKNOWN for a chalice object, for a destroyed idol, and for the city resurfacing.

L14 arrival selector 2 is (789, -10774), heading 0, region 2282. That is the region of the two chamber doors.

| id | static | stored x, y | height | region | floor | ceiling | neighbors | group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| control 78 | Chamber of Voice door, slot 67 | 688, -10873 | 0 | 2282 | 0 | 195 | 2264, 65535, 65535, 65535 | 17622 |
| control 79 | Chamber of Voice door, slot 67 | 638, -10752 | 0 | 2282 | 0 | 195 | 2264, 65535, 65535, 65535 | 17640 |

Both are flags 0x0482. Each kind 4 group is predicate 207, entry `0005000001`, and the children are opcode 12 `0c03aa001e00` (u16 170, byte 4 = 30) and opcode 9 `0903aa001500` (u16 170, byte 4 = 21). Opcode 12 was not entered. U16 170 fits more than one table. Prop 170 is the prop of that index.

Prop 170, template Side Deco, slot 10, stored (1080, -11330), height 0, region 4024, flags 0x0402. Region floor 0, ceiling 64, all four neighbors 65535. Kind 6 group 9210, value 20, predicate 50, entry `0003160001`. The only child is `020100001c30`. Byte 5 stays unread. Predicate bytes were not interpreted. Local slot 22 is the separate cstring `go_to_level_16`.

Prop 0, template Death Idol, stored (1071, -11521), height 0, shares region 4024 and is not a chalice. Its group 0 is opcode 16, opcode 8, opcode 13, opcode 13, and opcode 2 `020100002700`. That opcode 2 is outside the level-change shape. Prop 384, the other Death Idol, stored (-1701, 3170), region 4103, has opcode 3 identity 0x1200015E, byte +8 = 4. That identity is not the dreamstone 0xCE20AEE3.

The placed dreamstone on L14 is item 1, identity 0xCE20AEE3, definition 136, name slot `134-Dreamstone`, stored (3264, 2664), height -96, region 4073, flags 0x0002, event 0. Region 4073 is not region 4024 and not region 2282.

The other two L14 level changes stay the ones in `source_ids_054_060.md`: region 863 group 1462 and region 4176 group 3836, both `020100001c68`. Neither is on the chamber-door groups.

Movables 65 and 66, static Chamber of Voice door, slot 67. Movable 65 is (-549, -11298), height 0, region 2257, flags 0x0582, groups 19248 and 19278. Movable 66 is (-585, -11173), height 0, region 4126, flags 0x0582, groups 19308 and 19338. Each pair is opcode 1 on both movables, byte 4 = 100 under predicate 206 and byte 4 = 0 under predicate 207, plus opcode 16 on the same targets. Opcode 1 was not entered.

## STORY-067

Grade DECODED for arrival selector 1, for region 233's stored command bytes, and for control 78 naming control 194. Grade UNKNOWN for the ride. Opcode 18 and opcode 21 were not entered.

`docs/l16-arrival-elevator-source.md` already names this arrival. This pass re-read the bytes. The movie-table filename in that note was not re-read. Opcode 21 byte 4 is 27, and that byte is not a filename in the command body.

Arrival selector 1 is (-3860, 1341), heading 1, region 137.

Region 233, descriptor 2, list 40, kind 12 raw `080c3402e9000200`, stream 0 group 564. The group header is `f00000000200`. Children: opcode 21 `1503a8021b00` (u16 680, byte 4 = 27, byte 5 = 0) and opcode 18 `120100002bf10df7000004080080000a0000`. The opcode 18 byte +1 is 1, the u16 at +2 is 0, the signed words are (-3797, -2291, 0), flags are 0x0804, and the heading word is 32768.

Control 78, static Trigger plate, slot 66, stored (-3848, 1201), height 1, region 0, flags 0x0482. Region 0 has floor 0, ceiling 256, neighbors 233, 137, 205, and 209. Region 137 is the arrival region. Region 233 is the movie region. Kind 5 group 42098, value 4: opcode 16 `1010c2000000` and opcode 9 `0910c2001500`, both u16 194. Kind 5 group 42116, value 5: opcode 16 `1010c2000100` (byte 4 = 1) and opcode 9 `0910c2001500`, both u16 194. Controls number 326, so u16 194 fits a control. It also fits a prop.

Control 194, static door, slot 17, stored (-3849, 1163), height -2, region 0, flags 0x0482, the same neighbors. Its groups are 49010, 49034, 49058, and 49064. The children are opcode 7 and opcode 9 on u16 194. No opcode 2 and no opcode 18 sits on control 194.

Control 74, static Telepad, stored (2100, -4296), region 9615, is the other L16 level change, `020100001c31`. It is not a neighbor of region 137 or region 233.

## STORY-068

Grade DECODED for the single Fountain row, for the 14 Lichen rows, and for the black-lichen identity on each of those rows. Grade UNKNOWN for which fountain is the southern dry one, for a ball above it, and for the book's nine.

Template Fountain is one row. Prop 626, stored (-4111, -15457), height 90, region 4900, floor 90, ceiling 300, neighbors 4899, 4898, 4897, 4896, flags 0x4682. No Ball O Smoke is in region 4900 or those four neighbors. The group's opcode 198 is `c60000001001`, u16 0, byte 4 = 16. Local slot 16 is the cstring Ice_fountain_trigger. Opcode 198 was not entered, so the byte was not bound to that slot. The same groups also contain opcode 2 `020100001800` and `020100000b05`, both outside the level-change shape.

The other fountain-named rows are a different template or a different place. Prop 392, template Oil fountain, is (-2201, -12864), region 3661. Props 1 through 4, template Silverleaf fount, are all in region 6098 near (2230 to 2343, 536 to 650). None of those coordinates was joined to prop 626.

Template Lichen is 14 props, all height 15, flags 0x1402, stored x 1848 to 2733 and y 240 to 938. Ids 518, 521, 522, 527, 528, 533, 534, 539, 540, 545, 546, 551, 552, and 557. Each has one opcode 3 `03010000cceb4dca04000000`, identity 0xCA4DEBCC, byte +8 = 4. Definition 122, name slot `120-Black lichn`, handler 41. Fourteen is the placed count. It was not reduced to nine. No cstring is the word black by itself.

Prop 518, the row at (2053, 938), region 6360, is the one whose full list was copied. Kind 4 group 22408, predicate 209, entry `0005000003`: opcode 9 `090306021500` (u16 518, byte 4 = 21) and the opcode 3 above. The other thirteen rows carry the same opcode 3 identity and the same byte +8. Their other children were not copied one by one.

## STORY-069

Grade DECODED for the four Tower Pylon rows and the four Iris Door rows that share their regions. Grade UNKNOWN for a southwest tower, for an order, for a box, and for a shimmering disk. No box cstring exists. Static Tower Hole, Teleporter, heaven stair, and Staged Button have zero placements.

| pylon | stored x, y | region | iris | iris group | opcode 18 words | opcode 18 flags |
| --- | --- | --- | --- | --- | --- | --- |
| prop 489 | 14872, -6468 | 6463 | control 111 | 43060 | (14871, -6474, 0) | 0x0912 |
| prop 490 | 13228, -4877 | 6513 | control 109 | 42988 | (13234, -4879, 0) | 0x0912 |
| prop 491 | 11619, -6485 | 6017 | control 110 | 43024 | (11618, -6485, 0) | 0x0912 |
| prop 492 | 13236, -8104 | 6004 | control 112 | 43096 | (13234, -8101, 0) | 0x0912 |

Each pylon is template Tower Pylon, height 0, flags 0x1402, ceiling 5000. Each iris is static Iris Door, slot 52, height 0, flags 0x0402, the same region as its pylon. Each iris group is kind 6 value 20 and also has opcode 9 on that pylon's index, byte 4 = 3, plus opcode 9 on a Pylon Light. Those lights are props 450, 449, 448, and 451, template Pylon Light, stored on the same four coordinates. Opcode 18 was not entered. The signed words match the iris and pylon coordinates. That match is the stored numbers, not an entered move.

Each pylon's own kind 4 group (20286, 20344, 20402, 20460) is opcode 16, opcode 20, opcode 9 u16 445 byte 4 = 21, and opcode 5. Prop 445 is template Altar, stored (19999, -6490), event list not copied. A later kind 6 on each pylon is opcode 9 on itself, byte 4 = 2.

Prop 615, template Tower, stored (13273, -6464), height -999, region 6517, floor -1000, ceiling 5000, flags 0x0002, event 0. Region 6517 is not one of the four pylon regions. No movable has stored x from 11000 to 16000 and stored y from -9000 to -4000. The Push/Pull rows are controls 71 and 108, near (-5200, -1500), and they are under STORY-074.

A fifth Tower Pylon, prop 595, stored (2293, 171), region 6114, is in the greenhouse band and is under STORY-070.

## STORY-070

Grade DECODED for the silverleaf cluster, the hourglass, and the 14 black-lichen grants. Grade UNKNOWN for a yellow figure, for an hourglass-opens-tower effect, and for which plots are watered. No yellow cstring exists. Templates Bool, Bright Star, Big City, and City Minature have zero placements.

Region 6098, floor 3, ceiling 375, neighbors 6097, 6096, 6095, and 6094, contains props 1 through 4 (Silverleaf fount), prop 602 (Ball O Smoke, stored (2289, 648), height 18), prop 605 (Silverleaf Pyramid, stored (2287, 599), height -15), and control 75 (Silverleaf plate, stored (2287, 593), height 4, flags 0x0482).

Control 75 kind 4 group 42062, body ends in `017a340e`. Children: opcode 9 `09104b000e00` (u16 75, byte 4 = 14), opcode 2 `020100001800` outside the level-change shape, opcode 5 `05035d020400` (u16 605), opcode 16 `10035d020100` (u16 605). Kind 8 group 42092 is opcode 9 `090353020d00`, u16 595, byte 4 = 13. U16 595 fits only a prop: prop 595, the fifth Tower Pylon, stored (2293, 171), region 6114.

Prop 605's group 38056 is opcode 9 on prop 602, byte 4 = 3 and byte 4 = 21, then opcode 16 and opcode 5 on 605. Group 37986 is opcode 14 and opcode 198 `c60000001701`, byte 4 = 23. Local slot 23 is the cstring Silverleaf_clue. The opcode was not entered.

Prop 627, template Hourglass, stored (2293, 1070), height 45, region 6088, floor 45, ceiling 375, neighbors 6099, 6087, 6080, 6083. Group 40684 is opcode 20 and opcode 9 on prop 605, then opcode 9 byte 4 = 21 on props 502, 503, 504, 505, 506, 507, 508, 515, 514, 513, 512, 511, 510, and 509, in that order. Those fourteen indexes fit only props, and each of those props is template Altar. Stored x is 1152 for 502 through 508 (y 960 down to 192) and 3392 for 509 through 515 (y 192 up to 1024). Local slot 2 is the cstring Hourglass_on. The hourglass group has no opcode 198.

Prop 602's group 37758 is opcode 18 words (2290, 2951, 0), flags 0x0812, heading 0, raw `12035a02f208870b00001208000000280000`. Opcode 18 was not entered. Movables 92, 93, and 94, static FireWall Door, sit at (2242, 2947), (2342, 2947), and (2292, 2947).

The 14 Lichen rows of STORY-068 sit in this same x 1848 to 2733, y 240 to 938 band. Fourteen Puddle pooling controls, slot 47, share those lichen regions: controls 148 through 158 and 160 through 162. Control 148, stored (1923, 247), region 6302, was copied in full. Its kind 4 group 45160 ends in identity 0xCA4DEBCC and the child opcode 9 is u16 527, byte 4 = 3. Prop 527 is one of the Lichen rows. The same control has other kind 4 tails, including identity 0xBFDDCCA3, and those children were not reduced to a plant name here. Opcode 198 on control 148 is byte 4 = 4 and later byte 4 = 0. Local slot 4 is the cstring Is_Water_already_pooled_in_planter. The opcode was not entered.

Fourteen Watergate controls, slot 48, height about 77, stored x 1736 to 2840 and y 223 to 985: controls 123 through 134 and 163 and 164. Their command bodies were framed with the other statics and were not copied into this pack.

## STORY-071

Grade DECODED for the oil-fountain row and for the placed Darkbow. Grade UNKNOWN for a head statue, for burning oil, and for a blue bow. No head cstring exists. No placed row on L16 is named blue bow. The only bow identity placed on L16 is the Darkbow below. No opcode 3 of that identity was found on L16.

Prop 392, template Oil fountain, stored (-2201, -12864), height -5, region 3661, floor -5, ceiling 200, neighbors 3665, 3662, 3658, 3649, flags 0x4402. Kind 9 group 14558: opcode 9 `090418000300` (u16 24, byte 4 = 3), opcode 1 on u16 98, 81, and 80 with byte 4 = 100, opcode 198 `c60000000b01` (byte 4 = 11), opcode 9 u16 608 byte 4 = 21, opcode 9 u16 392 byte 4 = 2. U16 24 fits an item and also a prop, a control, an actor, and a movable. Item 24 is the Darkbow, and that fit is the table size, not an entered opcode 9. Local slot 11 is the cstring Fire_puzzle_triggered. Opcode 198 was not entered.

Item 24, identity 0xD58C34FE, definition 35, name slot `36-Darkbow`, handler 58, stored (-2546, -12858), height -5, region 3663, flags 0x1002, event 0. Region floor -5, ceiling 200, neighbors 3620, 3618, 3665, and 3647. Neighbor 3665 is also a neighbor of the oil fountain. Neighbor 3618 contains Fire Burst prop 638. Neighbor 3647 contains Fire Burst prop 640.

Fire Burst props 637 through 640, template Fire Burst, flags 0x1442, stored near x -2624 to -2620 and y -12557 to -13135, regions 3638, 3618, 3642, and 3647. Their command bodies were not copied.

Movable 98, static Fire door, stored (684, -12855), height 155, region 10210, flags 0x0182, event 0. Movables 80 and 81, static Sm fire door, stored (222, -13264) and (63, -13262). Movables 95, 96, and 97, static FireWall Door, stored at x 1704 and y -12841, -12891, and -12791. Prop 603, Ball O Smoke, stored (429, -12857), region 6775, has opcode 18 words (1703, -12835, 0), flags 0x0812. Those numbers sit on the firewall-door coordinates. Opcode 18 was not entered.

## STORY-072

Grade DECODED for the three trap rows and for the ball and pyramid in region 5484. Grade UNKNOWN for a spinning brick, for a blue bow, and for which object is the white ball. No brick cstring exists.

| id | template | stored x, y | height | region | floor | ceiling |
| --- | --- | --- | --- | --- | --- | --- |
| prop 88 | Block trap | -10576, 750 | 100 | 3851 | 100 | 500 |
| prop 89 | Fire trap | -10442, 1838 | 125 | 4159 | 100 | 500 |
| prop 90 | Ice trap | -8868, 3286 | 125 | 5833 | 100 | 500 |

All three are flags 0x4482. Each opens with opcode 9 on itself, byte 4 = 8 and byte 4 = 18, then opcode 16. A later group is opcode 17 u16 91 byte 4 = 1 and opcode 9 u16 91 byte 4 = 21. U16 91 fits more than one table. Prop 89 and prop 90 then opcode 9 themselves with byte 4 = 2. Prop 88's matching group is opcode 7, byte 4 = 1, instead of that opcode 9.

Region 5484, floor 100, ceiling 500, neighbors 5492, 5626, 5476, and 5485, contains prop 600, Ball O Smoke, stored (-9896, 899), height 115, flags 0x1402, and prop 641, Pyramid, stored (-9897, 841), height 100, flags 0x0482. Prop 600 group 37622 is opcode 18 words (-9877, 4536, 0), flags 0x0812, raw `120358026bd9b81100001208000000280000`. Movables 86, 87, and 88, static FireWall Door, sit at (-9870, 4533), (-9820, 4533), and (-9919, 4533). Prop 641 group 41010 is opcode 9 on prop 600, byte 4 = 3 and byte 4 = 21. Group 40946 is opcode 20 on prop 391, the Shape 3 at (-9859, 3450), region 4313.

The other Ball O Smoke rows are prop 601 (-9797, -13070), prop 602 in the greenhouse, and prop 603 beside the oil fountain. They are not in region 5484.

## STORY-073

Grade DECODED for three placed ivory-chip rows and for the opcode 3 sites of that identity. Grade UNKNOWN for four chips and for two chips carried in from the museum. This pass did not read a museum save.

Identity 0x042E0C09, definition 107, name slot `105-Ivory chip`, handler 90.

| item | stored x, y | height | region | flags | event |
| --- | --- | --- | --- | --- | --- |
| 12 | -5644, -4532 | -35 | 10120 | 0x8402 | 19098, opcode 9 u16 220 byte 4 = 21 |
| 22 | 5491, -10096 | 0 | 9653 | 0x0002 | 0 |
| 23 | -2853, 1534 | 0 | 7420 | 0x0002 | 0 |

Three is the placed count. Region 7420 also holds item 3, the dreamstone, item 4, the iron flute, and item 10, the cry shard, all event 0. Prop 220, template Light Source, stored (-5647, -4678), is the prop index named by item 12's opcode 9. The opcode was not entered.

Opcode 3 of the ivory identity, byte +8 shown:

| owner | group | byte +8 |
| --- | --- | --- |
| prop 223, Ivory Chip Gargoyle | 6090 | 4 |
| prop 399, Ivory Chip Gargoyle | 14678 | 4 |
| prop 592 | 36430, four commands in that group | 4 |
| control 0, Ivory Chip Block | 41082 | 4 |
| control 70, Ivory Chip Block | 41716 | 4 |
| control 95, Ivory Chip Block | 42334 | 4 |
| control 72, Chip | 41878 | 1 |

Prop 592's placement was read for `source_ids_054_060.md` and was not re-printed this pass. The opcode 3 owner is this pass. No opcode 3 of the dreamstone identity 0xCE20AEE3 was found on L16.

Local slot 5 is the cstring How_many_tower_keys_have_been_placed. No opcode in the groups copied above uses opcode 198 byte 4 = 5. The cstring was not bound.

## STORY-074

Grade DECODED for the force-field row, the gargoyle grants, the geyser row, and the chip-block rows. Grade UNKNOWN for sparked globes, for a straight walk, for freezing the fountain, and for a collapsing room. Prop 626's ice-fountain cstring is under STORY-068 and was not bound.

Movable 79, static Force Field, slot 55, stored (-5641, -4771), height -70, region 8197, floor -70, ceiling 70, neighbors 65535, 10117, 65535, 8198, flags 0x0582. Group 49736 is opcode 20. Group 49746 is opcode 9 `09040c000d00`, u16 12, byte 4 = 13. U16 12 fits more than one table. Item 12, the ivory chip at (-5644, -4532), region 10120, is the nearby placed chip. Neighbor 10117 is not region 10120.

Six Blue Dracoid Orb props sit just south of that force field, flags 0x4482, height -70: props 460 through 465, stored x -6079 to -5219 and y -4680 to -5020, regions 8217, 8209, 8201, and 8199. Their command bodies were not copied. No globe cstring is on those rows. The Pole w/ globe on top rows are props 401 through 404, 446, 447, 494, and 495, at the four pylon rooms of STORY-069, x 10609 to 15975. They are not neighbors of region 8197.

Prop 223, Ivory Chip Gargoyle, stored (-4406, -1537), height 50, region 8186, is the opcode 3 site in STORY-073. Its second group, 6126, is twenty opcode 196 commands on region indexes 8167 through 8187. Opcode 196 was not entered. Prop 399, the second gargoyle, stored (-9653, -3160), height 150, region 8510, grants the same identity and has opcode 198 byte 4 = 22. Local slot 22 is the cstring Trap_solved. The opcode was not entered. Prop 400, the third gargoyle, stored (-7544, -3171), region 8626, event 0.

Prop 419, template Geyser for freezing, stored (-2280, -11620), height 45, region 8680, floor 45, ceiling 420. Control 72, static Chip, stored (-2283, -11613), height 165, shares region 8680, flags 0x8402. Control 72 group 41818 is opcode 16 and opcode 18 words (-2283, -11620, 155), flags 0x0112, heading 0. Group 41878 is the ivory opcode 3 with byte +8 = 1, then opcode 9 on u16 72, byte 4 = 2. Prop 419 group 15242 is opcode 198 byte 4 = 15. Local slot 15 is the cstring Ice_door_trigger. The opcode was not entered. Three more Geyser for freezing rows, props 483, 484, and 485, sit near (-4700, -1475 to -1650). Their bodies were not copied.

Push/Pull controls, slot 53. Control 71, stored (-5214, -1470), height 20, region 8028, flags 0x0582, group 41770: opcode 196, opcode 9 u16 478, opcode 9 u16 71 byte 4 = 4, opcode 18 words (-4967, -1562, 0), flags 0x0004, heading 0. Control 108, stored (-5250, -1641), height -30, region 8121, flags 0x2582, group 42940: opcode 18 words (-5011, -1364, 0), flags 0x0004. Control 107, stored (-3951, -1379), event 0. Opcode 18 was not entered.

Ivory Chip Block controls, slot 45:

| id | stored x, y | height | region | note |
| --- | --- | --- | --- | --- |
| 0 | -12466, -8269 | 60 | 8286 | group 41082 ivory opcode 3, byte +8 = 4; also opcode 1 u16 112 byte 4 = 100 then 0 |
| 70 | 2168, -7670 | 15 | 2598 | group 41716 ivory opcode 3, byte +8 = 4 |
| 95 | -12444, -8269 | 60 | 8288 | group 42334 ivory opcode 3, byte +8 = 4 |
| 173 | -10089, -12935 | 30 | 7126 | group 48698, no opcode 3 in the copied children |
| 174 | -9949, -12936 | 30 | 7102 | list 18934, body not copied |
| 175 | -9645, -12936 | 30 | 7109 | list 18946, body not copied |
| 176 | -9505, -12936 | 30 | 7115 | list 18958, body not copied |

Item 29, identity 0x178B0A33, definition 94, name slot `92-Sk key`, handler 0, stored (-12561, -8217), height 65, region 8286, flags 0x2002, event 0. That is the region of control 0. Control 98, static crystal wall, stored (-11770, -8215), region 8296, and control 172, static crystal wall, stored (-9795, -13206), region 10065, have event lists. Their bodies were not copied.

Pedestal 1 and Pedestal 4 are under STORY-075 and are event 0. They were not joined to these chip blocks.

## STORY-075

Grade DECODED for the pedestal rows being event 0, and for the four iris doors being the only door static on the four pylon regions. Grade UNKNOWN for four chips on four pedestals, for a last tower, and for a disk that opens. Static names with zero placements include Tower Hole and Mantle Gate.

Pedestal 2 and Pedestal 3 have zero placements. The placed pedestals are all height 200, flags 0x0082, event 0.

| id | template | stored x, y | region |
| --- | --- | --- | --- |
| prop 222 | Pedestal 1 | 14396, 243 | 8832 |
| prop 411 | Pedestal 1 | 13174, 1812 | 8827 |
| prop 412 | Pedestal 1 | 14279, -1409 | 7485 |
| prop 413 | Pedestal 1 | 13114, -1112 | 7481 |
| prop 414 | Pedestal 1 | 14553, -351 | 8833 |
| prop 415 | Pedestal 1 | 12817, -18 | 8832 |
| prop 416 | Pedestal 1 | 12867, 902 | 8829 |
| prop 417 | Pedestal 1 | 14204, 955 | 8829 |
| prop 405 | Pedestal 4 | 14801, -842 | 8834 |
| prop 406 | Pedestal 4 | 12604, 1548 | 8827 |
| prop 407 | Pedestal 4 | 13719, 1389 | 8828 |
| prop 408 | Pedestal 4 | 12706, 558 | 8830 |
| prop 409 | Pedestal 4 | 12557, -482 | 8833 |
| prop 410 | Pedestal 4 | 13412, -1514 | 7485 |

Those regions also hold the placed reagent and scroll rows, items 13 through 21 and 25 through 28, all height 200, event 0. Examples: item 14 `R-Manafoil` (13189, 1768) region 8827; item 16 `R-Pyrapod` (13442, -1449) region 7484; item 26 `148-MoDScrl` (12609, 1485) region 8828. None of those identities is the ivory chip. The ivory items are the three rows in STORY-073, and none of them is height 200 in this pedestal band.

The four pylon regions and their Iris Door controls are the table in STORY-069. No fifth Iris Door was in the static-name selection. Prop 615, the center Tower at (13273, -6464), event 0, remains the only template-Tower row. Which of the four pylons is southwest was not derived. No axis was read from the MIX.

## Resolved

JSON pass over L14_HT.json and L16_CA.json. Both sha256 values match the header. Command bytes in this section come from those exports and were not re-read from the MIX, so they stay LIKELY. Opcode 2 was classified only by the level-change shape `020100001c`. Opcode 3, opcode 9, opcode 18, opcode 21, opcode 196, and opcode 198 were not entered. Placement numbers are placement_hex: signed words at bytes 0 and 2, height at byte 6, flags at byte 8, region at byte 10. A prop template is the u16 at byte 32. A movable static is the byte at byte 32. No axis was read. No museum save was read. The grades above stay as written.

STORY-066. Dreamstone identity 0xCE20AEE3 is stored as opcode 3, byte +8 = 4, on two rows. Prop 137, template u16 2, stored (1615, -195), height 0, flags 0x0402, region 4072, stream 1 group 7066, holds that identity once among 16 opcode 3 commands. The same group holds flute identity 0xB40E38C4 once and identity 0x1200015E three times. The other identities in the group were not named. Its opcode 2 commands are `020100000e14` and `020100000d14`. Kind 2 group 7292 is opcode 2 `020100003d28`. All three sit outside the level-change shape. Movable 72, static byte 36, stored (606, 3464), height 30, flags 0x0502, region 2490, stream 1 group 19666, holds the dreamstone identity once. The grant stays LIKELY. Props 0 and 384, the Death Idol rows, are template u16 17 in this export. Movables 65 and 66, the chamber doors, are static byte 67. Prop 137 and movable 72 are the other indexes, in regions 4072 and 2490. Across all 1062 groups, opcode 198 writes slot 4 Idol_Count zero times, slot 20 Open_Death_Door zero times, and slot 22 go_to_level_16 zero times. The level-change commands remain the three already listed. A chalice object, a destroyed idol, and the city resurfacing stay UNKNOWN.

STORY-067. Across all 2136 L16 groups, opcode 198 writes slot 0 Star_Elevator zero times. Region 233's opcode 21 byte 4 remains 27 and was not read as a filename. The ride stays UNKNOWN.

STORY-068. Slot 16 remains the one opcode 198 write on prop 626 group 40538, and it stays unbound. Prop 219, template u16 0, stored (-2403, -16035), height 0, flags 0x0482, region 9659, stream 1 group 4834, starts with opcode 9 on u16 626, byte 4 = 8. U16 626 fits only a prop. The other opcode 9 commands on that index are prop 626's own two, byte 4 = 16. Props 600 through 603 are template u16 61. Prop 219 is template u16 0, in region 9659. The southern fountain, a ball above it, and the book's nine stay UNKNOWN. Fourteen remains the placed lichen count.

STORY-069. Opcode 198 writes slots 6, 7, 8, and 9 zero times. The iris opcode 18 words in the export match the stored numbers in the table above. A southwest tower, an order, a box, and a shimmering disk stay UNKNOWN.

STORY-070. Opcode 198 byte 4 = 4 is 28 commands in 28 groups. Those groups belong to the 14 puddle controls already listed, 148 through 158 and 160 through 162. Each control has byte 5 = 1 and byte 5 = 0. The slot stays unbound. Opcode 198 writes slot 2 Hourglass_on zero times. A yellow figure, an hourglass-opens-tower effect, and which plots are watered stay UNKNOWN.

STORY-071. Slot 11 remains the one opcode 198 write on prop 392 group 14558. The export has zero opcode 3 commands of identity 0xD58C34FE. A head statue, burning oil, and a blue bow stay UNKNOWN.

STORY-072. A spinning brick, a blue bow, and which object is the white ball stay UNKNOWN. U16 88, 89, and 90 still fit more than one table.

STORY-073. The export's ivory opcode 3 owners are the rows already tabulated, including four commands in prop 592 group 36430 and control 72 with byte +8 = 1. Opcode 198 writes slot 5 How_many_tower_keys_have_been_placed zero times. Four chips, and two chips carried from the museum, stay UNKNOWN.

STORY-074. Opcode 198 writes slot 10 How_may_orbs_have_been_charged zero times. Slot 15, slot 16, and slot 22 remain the single writes on props 419, 626, and 399. Sparked globes, a straight walk, freezing the fountain, and a collapsing room stay UNKNOWN.

STORY-075. Four chips on four pedestals, a last tower, and a disk that opens stay UNKNOWN. Which of the four pylons is southwest was not derived.
