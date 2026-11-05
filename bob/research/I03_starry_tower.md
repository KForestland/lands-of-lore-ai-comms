# I03 Starry Tower

Place L16_CA. No frame was opened. No Godot was run. Static names are the 30-byte run at file 19098082, 87 names. Template names are the 38-byte run at file 19073622, 136 names. Name-at-index stays LIKELY. Opcode 9, opcode 20, and opcode 204 were not entered. Target u16 0 on opcode 18 is not the player.

Hintbook lines 5224–5236: you arrive in one of four corner towers, put the box in the square hole where you entered, and do not push it back through the disk. Outside, click the yellow eight-sided figure. One portion of the center tower rises, and a similar structure rises in the city. Four visits finish it. Grade HINTBOOK. Brady printed 131: push the dragon box through the sphere, slide it into the hole, touch the golden crystal that appears on the plain, and one section of the Grand Tower rises in the Netherworld and in the city. Four sections. Grade BRADY. Both clicks are REQUIRED. Looking around the plain is the book's aside.

## Arrival is four gate regions

Kind 12 on four city gate regions stores an opcode 18 with bit 0x0004 set. That bit is the direct-relocation form. The target u16 is 0. The other bits in `0x0c04` were not read. Kind 12 timing is I31, so these rows are stored commands, not a proven step-on.

| city region | gates, native | opcode 18 words | flags | destination region | floor, ceiling | corner key |
| --- | --- | --- | --- | --- | --- | --- |
| 3107 | 165, 166 at (2286, 3141) and (2286, 3131) | (16082, −3886) | 0x0c04 | 7658 | 100, 800 | control 119 (15948, −4005) |
| 3243 | 167, 168 at (−9876, 4718) and (−9876, 4727) | (10467, −3668) | 0x0c04 | 7722 | 100, 800 | control 120 (10666, −3970) |
| 3443 | 169, 170 at (−9803, −14528) and (−9803, −14518) | (10444, −9314) | 0x0c04 | 7600 | 100, 800 | control 122 (10605, −9187) |
| 2846 | 171 at (1893, −12835) | (15978, −9312) | 0x0c04 | 7267 | 100, 800 | control 121 (15892, −9211) |

Godot positions flip the stored y. The NE arrival is (16082, 3886). Each of those groups also has opcode 9, byte 4 = 21, on one Pole w/ globe on top: props 402, 403, 447, and 494. Opcode 9 was not entered, so the pole is not the yellow figure.

Each destination quad is a few hundred units on a side and its floor is 100, the same as the key room next to it. None of the four is a pit. Static Tower Hole is index 64 and has zero placements. No template and no static name is box. Bool and Bright Star have zero placements. No item row sits in this band. The square hole and the box stay UNKNOWN as placed rows.

The four corner clusters, and nothing else within 600 of each pylon, are the corner contents. Each corner has the Key Object, one Jumbo Gate with no events, and two poles. The four Iris Doors (controls 109–112) and Tower Pylons (props 489–492) sit on the mid-sides, floor 0, ceiling 5000. Their opcode 18 flags are 0x0912, bit 0x0004 clear, and the target is the pylon itself. That is the same shape as the NE smoke ball, not this arrival.

## Center structure

Prop 615, LIKELY template Tower, is stored (13273, −6464), height −999, region 6517, flags 0x0002, event 0. Godot (13273, 6464). Region 6517 floor is −1000 and the ceiling is 5000. The quad is about x 13115–13291, y −6479 to −6354. Seven neighboring regions share floor −1000 and cover about x 13115–13463, y −6632 to −6307. The mesh sits one unit above that pit floor. It has no events of its own.

Three altars in region 8301 hold the raises. Region 8301 is x 19930–20069, y −6798 to −6031, floor 0, ceiling 200, and all four neighbors are 65535. It does not connect to the plain. The five altars in that room are props 398, 445, 487, 614, and 616.

The opcode 196 floor formula already accepted is: signed word at +4 is an absolute floor target, byte 6 is 0, byte 7 is speed, and delta is target minus the current floor. Applied here, not a new callee proof:

| altar | native | group | regions | current floor | target | speed | delta |
| --- | --- | --- | --- | --- | --- | --- | --- |
| prop 487 | (20003, −6112) | 20160 | 6492, 6435, 6036, 6525 | 80 | 1200 | 50 | 1120 |
| prop 614 | (19998, −6238) | 38598 | 6460, 6410, 6423, 6003, 6028, 6517, 6516, 6464 | −1000 | 850 | 50 | 1850 |
| prop 616 | (20002, −6367) | 38718 | twenty regions around the pit, including 6523 and 6030 | 10 | 500 | 20 | 490 |

Each of those groups also has opcode 20 on prop 615. Opcode 20 was not entered. The four pads in group 20160 sit just outside the pit corners. Group 38598 is the pit, including the tower's own region 6517. Group 38718 is the floor-10 ring. A fourth floor group that names this pit was not found. Stream 0 groups 4578, 4584, and 4606 are opcode 9 on prop 615, byte 4 = 16, and no object or region event points at them.

Props 365–374, the Shape rows, are a statue hall around (5500, −7000), height 80, event 0. No command in the JSON targets them. They are not a ring around prop 615. Little Tower prop 486 at (−3916, −8166), height −1000, is named only by opcode 20 from altar prop 592. The city's copy of the rising structure stays UNKNOWN.

The plain's sky props are event 0: Nebula, Nebula 2, Nebula 3, Small Planet, and Jumbo Planet, height 600 or 1241. Their regions are floor −1000. They are not the crystal.

## Still open

The square hole, the box, and the yellow eight-sided mesh. Which command reaches the three closet altars, since opcode 9 was not entered. The fourth raise. Opcode 20 on prop 615. Kind 12 timing. Target u16 0. No frame.
