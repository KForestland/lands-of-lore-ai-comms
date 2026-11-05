# I00 Huline Temple portals

`L14_HT.MIX` sha256 prefix `c294f9ab142b55c3`. JSON is the act3 export. Geometry entry file 11406344, marker 18, 4275 regions. Godot y is the native y with the sign flipped. Owner 18:10:50 Godot (−310, −2304) is native (−310, 2304). Owner 18:01 Godot x 2625..2884, y −3375..−2698 is native y 2698..3375. Static names are the 30-byte run anchored by index 67 `Chamber of Voice door` and index 36 `Dreamstone Slot`. That alignment is LIKELY. Opcode 18 was not re-entered past the `0x0004` bit already read. Opcode 2 byte 5 stays unnamed. Opcode 9 and opcode 12's room cstring were not entered. No frame was opened.

## Doors the owner clicked

Three movables, static slot 24 (`Nice Door`), byte 34 = 6, no events:

| movable | native | region | floor | ceiling |
| --- | --- | --- | --- | --- |
| 88 | (−305, 2132) height 190 | 1459 | 190 | 270 |
| 89 | (32, 2061) height 190 | 1461 | 190 | 270 |
| 90 | (380, 2124) height 190 | 1465 | 190 | 272 |

Movable 88 is the 18:10:50 point. None of the three owns an opcode 18 or a level change. The same xy is inside more than one region. (−305, 2132) is also in 1451, 1456, 1472, and 1485, all floor 190, ceilings 345, 310, 345, and 470. (380, 2124) is also in 1470, 1484, 1502, and 1503. The door quad is the ceiling-270 box. Taller boxes share its footprint. That is the clip.

## Direct-relocation landings on those doors

Bit `0x0004` is the proven direct-relocation bit. These four commands have it. Target u16 is 0. That index was not named.

| owner | native, region | group | predicate | flags | destination words |
| --- | --- | --- | --- | --- | --- |
| prop 384 | (−1701, 3170), region 4103 floor 220 | 15378 | `0005000000` | `0x0485` | (−234, 2215, 0) |
| prop 372 | (−38, −3209), region 2297 floor 210 | 15210 | `0005000000` | `0x0485` | (31, 2153, 0) |
| prop 371 | (7620, 2095), region 2390 floor 310 | 15150 | `0005000000` | `0x0405` | (314, 2213, 0) |
| prop 221 | (−83, −6389), region 2618 floor 300 | 12072 and 12198 | `0005000000` and `0005000001` | `0x0004` | (42, −11041, 0) both |

Group 15210 also holds opcode 2 `020100000b05` and `020100000c05`, which are not the level-change shape, plus an opcode 3. Those arms were not entered. The file match for 15210 is the group raw at file 11727792.

The first destination sits in the stacked shells over door 88 (regions 1451 and 1485). The second is region 1483, floor 190, ceiling 470, beside door 89. The third sits in 1470 and 1484, beside door 90. Prop 221's destination is region 2141, floor 350, ceiling 2860, box x −8..100, y −11057..−11036. The other flag bits on these words were not re-read.

## Level changes

| owner | where | group | command |
| --- | --- | --- | --- |
| region 863, kind 12 event 2 | center (2417, 2307), floor 0, ceiling 80, box x 2357..2475, y 2258..2356 | 1462, file 11783030, MIX match | `020100001c68` |
| region 4176, kind 12 event 2 | center (−1330, −11456), floor 40, ceiling 156 | 3836 | `020100001c68` |
| prop 170 | (1080, −11330), region 4024 | 9210 | `020100001c30` |

Byte 5 is unnamed. The same `0x68` is used at the east pad and at the far south pad. Region 863's footprint is also region 663 (floor −100, ceiling 1200, box x 2356..2482, y 2282..2360) and region 4043 (floor 0, ceiling 64). The level-change pad is the short box inside the tall one. Kind 12's fire time was not entered.

## Voice-door room load

Controls 78 and 79, slot 67, region 2282 (floor 0, ceiling 195, box x 609..1055, y −10936..−10549). Native (688, −10873) and (638, −10752). Groups 17622 and 17640, predicate `0005000001`, MIX match on 17622: opcode 12 `0c03aa001e00` (u16 at +4 = 30) then opcode 9 byte 4 = 21 on u16 170. The room cstring for index 30 was not read. The lead note in `docs/l14-chamber-voices.md` calls that index `chv_`. This pass did not re-prove that name.

## The 18:01 pocket

Native window x 2500..3000, y 2600..3500 holds 106 regions.

| floor | count | union box (min x, max x, min y, max y) | ids |
| --- | --- | --- | --- |
| 0 | 66 | (2284, 3211, 2528, 3585) | the floor-0 set in that window |
| −80 | 16 | (2269, 3153, 2778, 3541) | 40, 781, 3254, 3255, 3257, 3258, 3259, 3260, 3263, 3344, 3360, 3366, 3419, 3420, 3421, 3422 |
| −100 | 8 | (2473, 3045, 2560, 2830) | 537, 552, 630, 631, 638, 639, 640, 644 |

84 of the cross-floor overlaps in the window are floor −80 against floor 0. 31 are floor −100 against floor 0. Controls 165 and 166, slot 15 (`altar pieces`), sit at (2413, 3299) and (2413, 3350), region 816, and have no events. Stream 0 group 1360, which no object event names, is opcode 18 on u16 166 and u16 165 to (2413, 3362) and (2413, 3288), flags `0x0093`. Bit `0x0004` is clear, so that pair is not the direct-relocation case. The point (2413, 3362) is in region 163 (floor −80, ceiling 20) and region 816 (floor 0, ceiling 125).

## Not door teleports

Prop 385's opcode 18s target 385 itself, flags `0x0012` and `0x0093`, bit `0x0004` clear. Prop 399 group 15772 is fourteen opcode 18s on u16 90–103, flags `0x0081`, bit `0x0004` clear. The word at +8 on those is 15430, 28012, 27392, or 0. Bit `0x0100` is clear, so that word was not read as a height.

## Grades

DECODED for the three door movables having no events, the four `0x0004` destinations, the three level-change commands, the two opcode 12 bytes, and the floor boxes above. The room cstring, opcode 2 byte 5, kind 12's moment, and a frame stay open. The owner rows are the reports. The stacked floors are the geometry those reports sit on.
