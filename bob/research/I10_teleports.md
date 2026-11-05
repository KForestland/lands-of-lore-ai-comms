# I10 L16 teleports

Place L16_CA. No frame was opened. No Godot was run. Template names are the 38-byte run at file 19073622. Static names are the 30-byte run at file 19098082. Name-at-index stays LIKELY. Opcode 18 was not entered. Bit 0x0004 is the already-accepted direct-relocation bit. The other flag bits were not re-read. Target u16 0 is not the player. Opcode 2 arm 0x1C byte 5 stays unread. A level-change shape is only `020100001c`.

The one placed Telepad is control 74, already filed in I09. The hintbook's one-way sentence stays there. Static Teleporter, index 7, has zero placements. Static Telepad, index 27, has one placement.

## Two level changes

| owner | native | command | byte 5 |
| --- | --- | --- | --- |
| kind 12 region 9822, group 7268 | the region is x −7822..−7739, y −10834..−10750, floor −530, ceiling −440 | `020100001c71` | 0x71 |
| control 74, LIKELY Telepad, group 42056 | (2100, −4296), region 9615, height 15 | `020100001c31` | 0x31 |

Godot for the telepad is (2100, 4296). Each group has that one command. Region 9823 joins 9822 to 9824. They are not the same region. The destination level is not named.

## Twenty-nine direct relocations

Seventy-seven opcode 18 commands are stored. Twenty-nine have bit 0x0004 set. Forty-eight do not, so they are not this form.

Rows already filed, not re-derived: the four city gate regions 3107, 3243, 3443, and 2846 (I03); keys 119–122 (I02); prop 609 and Fire Burst props 637–640 and Wall o Fire controls 185–188 (I04); push objects 71 and 108 (I07). Each of those object rows targets itself. The four gate rows target 0.

New rows. Kind byte, words, and flags are the stored command. The landing region is the quad that contains the words.

| owner | native place | words | flags | lands |
| --- | --- | --- | --- | --- |
| region 233 kind 12, group 564 | x −3910..−3800, y 1059..1160, floor 0, ceiling 100, neighbor of 137 | (−3797, −2291, 0) | 0x0804 | 343, floor 0, ceiling 600 |
| region 4812 kind 12, group 2974 | x −6989..−6847, y −4168..−4002, floor 30, ceiling 130 | (−6790, −4082, 0) | 0x0005 | 4810, the east neighbor, same floor |
| region 7667 kind 12, group 5164 | x 15769..15968, y −4178..−3989, floor 100, ceiling 800 | (2281, 3004, 0) | 0x0c04 | 3113, floor 0, ceiling 800 |
| region 7708 kind 12, group 5182 | x 10635..10853, y −4131..−3960, floor 100, ceiling 800 | (−9882, 4590, 0) | 0x0c04 | 3231, floor 0, ceiling 800 |
| region 7272 kind 12, group 5128 | x 15719..15938, y −9194..−9013, floor 100, ceiling 800 | (1770, −12832, 0) | 0x0c04 | 2877, floor 0, ceiling 800 |
| region 7629 kind 12, group 5146 | x 10615..10790, y −9216..−9007, floor 100, ceiling 800 | (−9802, −14373, 0) | 0x0404 | 3452, floor 0, ceiling 800 |
| prop 418, LIKELY Sleepytime Goblet, group 14940 | (−6426, −560), height 105, region 4784 | (−6424, −586, 0) | 0x0004 | 4783, floor 80 |
| prop 418, group 14972 | same prop | (13725, 283, 0) | 0x0004 | 8831, floor 200, ceiling 5000, x 12100..14740, y −40..560 |
| control 79, LIKELY Null Front Gate, group 42134 | (5520, −5494), region 244 | (−3923, −7619, 0) | 0x0c04 | 7831 |
| control 80, LIKELY Null Front Gate, group 42152 | (−3920, −7760), height −259, region 7831 | (5517, −5640, 0) | 0x0c04 | 243 |

Godot flips the stored y. Region 233's words are not on region 233. The same group also stores opcode 21 on u16 680. Opcode 21 was not entered. Region 4812's other command is opcode 12 on u16 400. Opcode 12 was not entered. Flag 0x0005 keeps bit 0x0001, which was not read. The four star-corner regions sit on the same floor-100 quads as the I03 arrivals and point back at the city door bands. Landing quads 3113, 3231, 2877, and 3452 are the neighbor cells of those bands. They are not the smoke-ball commands. Those are flags 0x0812 and bit 0x0004 is clear.

Prop 418's other groups are opcode 2 raw `020100001800`, opcode 16, opcode 5, opcode 20, and opcode 14 on itself. Arm 0x18 is not a level change. The far word (13725, 283) is on the plain north of the pit, not on prop 615. Controls 79 and 80 each have this one command. Each word sits in the other gate's neighborhood. Control 80 itself is in region 7831. Ten Light Source props share region 243.

## The probe

The lead's point (2289, −1427) is native (2289, 1427) under the map sign flip. That point is inside region 6078, floor 70, ceiling 590, x 2205..2370, y 1410..1605. Neighbors include 6066 and 6074. I01 already has the nav cut on 6066→6078 and 6078→6074. The hourglass, prop 627, is (2293, 1070), region 6088. No opcode 18 word is within 400 of (2289, 1427), of (2289, −1427), or of the greenhouse y 648 at that x. The 87 geometry markers are homes plus one `Enters city` at (−4032, −2157), region 0. None is the probe. No stored relocation and no level change names this point.

## The other forty-eight

Bit 0x0004 is clear, so these are not the direct form. Flag tallies: 18 of 0x0008, all on prop 607 (I04); 14 of 0x0112, twelve of them the mantle copies on regions 216, 217, and 218 (I08 filed 217 and 218) and two on control 72 with height words 155 and 150; 4 of 0x0812, smoke balls 600–603; 4 of 0x0912, iris doors 109–112; 4 of 0x0a81, Jack's Doors 84, 85, 99, and 100, target 0; 2 of 0x0009 and 1 of 0x0809, prop 377 on target 420; 1 of 0x0908, prop 445 on target 80. Effects of those flags stay I29.

## Still open

Who target 0 is. Byte 5 of both level changes. Flag bits other than 0x0004. Kind 12 timing. Opcode 12, opcode 14, and opcode 21 on the new rows. No frame.
