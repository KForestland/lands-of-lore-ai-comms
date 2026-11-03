# Source ids for the 15 Act 1 playtest mechanics

Read-only pack for section B of `playtest_feedback_20261023/TRIAGE_20261103.md`. The lead builds these mechanics. This file only names original ids.

An F10 map pair is Godot X and Godot Z after `native_translation` is removed (`playtest_feedback.gd`). A placement is stored as Godot `(native_x, height, -native_y)`. Native x is the reported X. Native y is the reported Y with the sign flipped. At the cave point that lands on the bridge gates at native y 16661. The unflipped sign had no object within 250 there.

Placements and name tables were read from the level MIX this pass. Command lists are the native-script JSON for that same MIX (`L1_DC.json`, `L3_DH.json`, `L4_HJ.json`, `L5_HC.json`, `L14_HT.json`). Each geometry sha256 matched that JSON's source pin. Opcode 1, opcode 2, opcode 3, opcode 5, opcode 9, opcode 16, opcode 18, opcode 20, and opcode 198 were not entered. A level-change shape is only `020100001c`, and byte 5 stays unread. An opcode 9 or opcode 1 index is named only when it fits one table. Definition name-at-index stays LIKELY: GLOBAL.MIX key 3984507021, record base 496, stride 91, identity at +24, 30-byte names at 20734. A kind-4 tail identity is the dword only. Locals are named and not bound.

## Cave gates

Report `(40,-16661)`, native `(40,16661)`. L1_DC.MIX sha256 `6384ec4d4d78f1aadfc1f154d924e1e20636af037cf5af68fe35af8478854345`.

Grade DECODED for the bridge placements. Grade UNKNOWN for the guard leaving, for every gate moving, and for a lever lifting bars. Prima printed 56 (hintbook.txt 2052) says to pull the lever next to the bridge. That sentence does not say a guard pulls the gates down.

Actor 2, def GGUARD, stored `(-48,16609)`, height -285, region 1132, flags 0x7582. The same region holds control 104, static Long trigger, stored `(-9,16615)`. Its kind-5 group 9994 is opcode 18 words `(44,16667,0)`, flags 0x0081, heading 18204, then opcode 1 byte 4 = 100 on u16 73 and u16 72. Both indexes fit a prop, a control, and a movable.

Prop 456, template Kenneth Speech, stored `(158,16640)`, region 1148. Kind-6 group 4376, predicate index 211, contains opcode 1 byte 4 = 100 on u16 65, 64, 69, 70, 68, and 66. Those indexes are not unique.

Switches and gates on this bridge, static names from the movable rows:

| id | static | stored x, y | region | event |
| --- | --- | --- | --- | --- |
| 64 | Switch | 404, 16635 | 1178 | 8034 |
| 65 | Switch | 404, 16661 | 1180 | 8064 |
| 66 | Switch | 404, 16684 | 1182 | 8094 |
| 67 | Switch | 404, 16707 | 1184 | 8124 |
| 68 | Port Door | 150, 16648 | 1159 | 8164 |
| 69 | Port Door | 242, 16513 | 1155 | 0 |
| 70 | Iron Gate | 242, 16496 | 1157 | 0 |
| 71 | Iron Gate | 133, 16651 | 1162 | 8176 |
| 72 | Switch | -124, 16697 | 1163 | 8190 |
| 73 | Iron Gate | 153, 16430 | 1116 | 0 |

Movable 72 is the switch west of the report. Kind-4 groups 12568 and 12592 are opcode 1 on u16 73 and u16 72, byte 4 = 100 then 0. Movable 67's kind-4 groups 12490 and 12514 are opcode 1 on u16 71 and u16 67, byte 4 = 100 then 0. Movables 64, 65, and 66 pair the same way with u16 70, 69, and 68. Port Door 69, Iron Gate 70, and Iron Gate 73 are event 0.

## Museum wall

Report `(-1880,-1049)`, native `(-1880,1049)`. L3_DH.MIX sha256 `bd85c12d4a2cff0cc200309e72a7771745ce5c78f1a83da4d60cba81d831ccac`.

Grade DECODED for the room's switch, door lid, and four scrolls. Grade UNKNOWN for which command opens a wall. Prima printed 57 (hintbook.txt 2099 and 2112) says to open the secret panel in the floor, and later to attack a crumbled wall. Neither sentence names this switch.

Movable 52, static Door Lid, stored `(-1882,1019)`, height 30, region 1475, flags 0x0582. Kind-4 group 12092 is opcode 16 on u16 61. Kind-6 group 12104 is opcode 16 on u16 61, byte 4 = 0. Index 61 fits a prop, a control, and a movable.

Movable 79, static Switch, stored `(-1948,1017)`, height 45, region 1464, flags 0x0481. Kind-4 groups 12488 and 12512 are opcode 1 on u16 79, byte 4 = 100 then 0, and opcode 9 on u16 81, byte 4 = 21. Index 81 fits a prop, a control, and a movable: prop 81 is Light at `(-1997,1082)`, control 81 is Battle Tapestry at `(-3820,1084)`, and movable 81 is Cover at `(853,1894)`. The switch's groups do not name movable 52.

Items in the neighboring regions, all event 0: item 13 identity 0x139C102E, definition 75, `73-Spkscrl`; items 14 and 15 identity 0x7B8015C7, definition 148, `146-HlScrl`; item 16 identity 0x5C242DCE, definition 149, `147-SumScrl`.

## Museum dragon

Report `(3044,-1146)`, native `(3044,1146)`, region 1422. Grade DECODED for the only Dragon Door row. Grade UNKNOWN for a click that changes level. Prima printed 57 (hintbook.txt 2113) says to fly to the southern continent on the dragon.

Movable 82, static Dragon Door, stored `(3048,834)`, height 0, region 760, flags 0x0582. That is 312 units from the report, and region 760 is not a neighbor of region 1422. Kind-4 group 12536 is opcode 1 byte 4 = 100 and opcode 16 byte 4 = 2, both u16 82. Kind-4 group 12554 is opcode 9 byte 4 = 0x19, opcode 1 byte 4 = 0, and opcode 16 byte 4 = 1, all u16 82. No level-change command is in those groups.

The only L3 level-change found is stream 1 group 7306, `020100001c24`, on control 82, static Portal, stored `(-4058,1585)`, region 1416. Byte 5 stays unread. That control is not the dragon door.

## Jungle scroll

Report `(3015,-4098)`, native `(3015,4098)`. L4_HJ.MIX sha256 `517afe6d59a4a06212bf4aea7eb42dfbb07826a4677fb77a4032674e64657e8f`.

Grade DECODED for the summon scroll and the invisible platform at the same point. Grade UNKNOWN for a rumble, a dropping floor, and fire. No rumble sentence was found in the hintbook. Prima printed 71 names the Summon Group Scroll as a spell already taken from the museum. That is not this coordinate.

Item 82, identity 0x5C242DCE, definition 149, `147-SumScrl`, handler 12, stored `(3015,4178)`, height -118, region 3325, flags 0x0402, event 9668. The native-script JSON has no item objects, so the item's commands were not framed. Control 136, static Inviso platform, is the same point, `(3016,4178)`, height -120, region 3325, event 0.

Prop 0, template light, stored `(3017,4024)`, region 3318. Kind-2 group 30 is opcode 14, then opcode 196 on regions 3318 and 3321. No prop whose name contains fire was found within 800.

## Jungle switch

Report `(2951,-3525)`, native `(2951,3525)`. Grade DECODED for the imp switch, the imp door, and the imp stand. Grade UNKNOWN for the switch opening that door. No hintbook sentence was found for a switch behind a statue.

Movable 54, static Imp switch, stored `(2911,3535)`, height -125, region 4567, flags 0x0581. Kind-4 groups 27438 and 27462 are opcode 1 on u16 54, byte 4 = 100 then 0, and opcode 9 on u16 123, byte 4 = 21. Index 123 fits a prop and a control. Prop 123 is template light, stored `(2940,3535)`, region 3273. Its kind-6 group 514 is opcode 18 words `(2887,3694,-172)`, flags 0x0109, heading 0, target u16 57. Group 562 repeats that target with height word -240.

Control 57, static Imp stand, stored `(2888,3693)`, height -240, region 65535. Movable 55, static Imp door, stored `(2850,3693)`, height -170, region 4577, event 0. The switch groups do not name movable 55.

## Jungle hidden wall and hidden door

One triage row, two reports. Grade UNKNOWN for both. No hidden-wall or hidden-door sentence was found in the hintbook.

Hidden wall, report `(3196,-4160)`, native `(3196,4160)`. No wall-named row is within 600. The only door-named row inside that radius is movable 55, the imp door already under the switch section, 581 units away. The nearest eventful row is prop 2132, template Grass, stored `(3238,4247)`, region 1902. Kind-6 group 16376 is opcode 16 on itself, opcode 21 u16 2136 byte 4 = 78, and opcode 9 on prop 2136, byte 4 = 21. Prop 2136 is also Grass, stored `(3130,4261)`. Its group 16400 is opcode 2 `020100003900`, outside the level-change shape.

Hidden door, report `(918,-3664)`, native `(918,3664)`. Movable 52, static Imp door, stored `(1045,3692)`, height 0, region 4766, flags 0x0582, 130 units from the report. The only opcode 1 in its groups is group 27414, byte 4 = 0, on u16 52 and u16 51. Both indexes fit every object table. Movable 51, static Imp switch, stored `(1073,3727)`, height 50, region 4570. No other door-named row is closer.

## Cat lady and the knife

Report `(775,-1718)`, native `(775,1718)`. Grade DECODED for the Kityara control. Grade UNKNOWN for a knife and for Daniel. Prima printed 85–86 (hintbook.txt 2908–2921) is the knife given to Daniel after the jungle tunnel. That paragraph was not found in this control's commands.

Control 0, static Kityara, stored `(808,1802)`, height -14, region 3767, flags 0x9481. Prop 64, template Dead Kityara, stored `(837,1786)`, same region. Kind-4 tails on the control are identity 0x87F22ADE (`83-Power orb`), 0x7F859FB9 (`110-Amber`), and 0x64C08B10 (`109-Ironwod sap`). None is a knife. No L4 actor def is named Daniel. The nearest actors are TIG_CUB 42 and TIG_FEM 48, both more than 500 units away.

## The man who should follow

Report `(3375,-4072)`, native `(3375,4072)`, region 3785. Grade DECODED for the nearest actor. Grade UNKNOWN for hearing him and for following. Actor 61, def BACL4, stored `(3550,4152)`, height 0, region 3785, flags 0x7582, 192 units from the report. His list has 20 records. The first groups use opcode 16, opcode 13, opcode 9, opcode 14, opcode 2, opcode 8, and opcode 5. None of those was entered. No follow command was read.

## Spider attack

Report `(5154,-3751)`, native `(5154,3751)`. Grade UNKNOWN. No actor def is named spider. The ten SSAR placements are near `(7232..7296,-1056..-1312)`, more than 5000 units away. The nearest actors are GGuard 59 `(5634,3583)`, GGuard 60 `(5689,3706)`, and GGuard 58 `(5658,3938)`. The nearest movables are Bridge Tunnel 61 and 58, both event 0. A hive spider sentence on Prima printed 71 was not matched to this jungle point.

## Hive elevator

Report `(-2543,-7633)`, native `(-2543,7633)`. L5_HC.MIX sha256 `a1979e60d401ae308e430f69a7163ff07a7f704aeb233769add85e7cc0960bf8`.

Grade DECODED for the placed flute, the elevator control, and the eight call buttons. Grade UNKNOWN for the flute calling the lift, and for the lift starting at the bottom. Prima printed 77 (hintbook.txt 2665–2669) says to use the flute at an open pit to summon the elevator, and that the tower has eight squares.

Item 3, identity 0xB40E38C4, definition 96, `94-Iron flute`, handler 16, stored `(-2253,7472)`, region 1265, flags 0x0002, event 0. That is 332 units from the report.

Control 125, static Elevator Controls, stored `(-2640,7652)`, height -235, region 772, flags 0x2482. The eight kind-3 groups are 7364, 7470, 7576, 7682, 7788, 7894, 8000, and 8106. Each contains opcode 5 on u16 76 through 83, opcode 20 on u16 125, opcode 198 index 20 with byte 5 running from 1 through 8, and opcode 196 on regions 772, 773, and 774. Index 76 through 83 each fit a prop, a control, and a movable. Local 20 is the cstring `El_Level`. It was not bound. Controls 76, 77, 82, and 83 are static Light panel. Controls 78 through 81 were not re-read.

Call Button controls 126 through 132, static slot 21, events 3550 through 3634 step 14. Stored points: `(-2290,7421)`, `(-2370,7894)`, `(-2640,7943)`, `(-2843,7797)`, `(-2886,7536)`, `(-2751,7342)`, `(-2489,7285)`. Their groups were not copied.

The only flute-identity opcode 3 on L5 is prop 208, template lg boulder, stored `(1604,4896)`, group 1410, byte +8 = 4. That prop is not this elevator.

## Hive buttons

Report `(-3509,-7128)`, native `(-3509,7128)`, region 753. Grade DECODED for the three lock controls. Grade UNKNOWN for an order of four presses and for a top-floor clue. The hintbook's button sentences on printed 77 are the elevator button and the cat pedestals. Neither says four presses.

| id | static | stored x, y | height | group pairs |
| --- | --- | --- | --- | --- |
| 116 | Lock L1 | -3471, 7167 | -981 | 6676, 6698, 6726 and the value-1 copies 6760, 6782, 6810 |
| 115 | Lock L2 | -3454, 7148 | -951 | 6532, 6560 and the value-1 copies 6604, 6632 |
| 114 | Lock L3 | -3437, 7131 | -981 | 6408, 6436 and the value-1 copies 6470, 6498 |

All three are flags 0x0402, region 753. Their opcode 16 commands name u16 114, 115, and 116. Each of those indexes fits a prop and a control, so the command target stays unnamed. The placed rows at those indexes are these locks. Lock L2's groups 6560 and 6632 also opcode 198 index 16 value 0 and opcode 196 on region 760. Local 16 is `Spout_2`, unbound.

Glyph controls 117 through 120 sit at about `(-1859..-1886,7696)`, height -205, region 283, event 0. They were not joined to region 753.

## Hive boulder

Report `(-3345,-6074)`, native `(-3345,6074)`. Grade DECODED for the two buttons and the boulder cover. Grade UNKNOWN for a boulder leaving the wall, for a broken floor, and for a cellar. Prima printed 80 (hintbook.txt 2787–2796) is a room with two rolling boulders and a healing scroll. That paragraph was not matched to this coordinate.

Control 135, static Button, stored `(-3399,6143)`, height -1629, region 682. Control 134, static Button, stored `(-3288,5995)`, same height and region. Each kind-3 list opcode 16s the other index, opcode 20s u16 70, and opcode 196s region 685. Index 70 fits a prop and a control. Prop 70 is Inviso Light, stored `(-3259,6150)`, region 685, event 0. Control 133, static Boldr Covr, stored `(-3179,6229)`, height -1675, region 590, event 0. Control 0, static Ladder, stored `(-3142,6190)`, region 595. Local 5 is `Boulder_Fall`. No opcode 198 index 5 was in the button groups that were copied.

## Temple spider

Report `(3061,-5374)`, native `(3061,5374)`. L14_HT.MIX sha256 `c294f9ab142b55c36fff545a1293c419c42353fedefbfe8b77b9c38a2d9a0719`.

Grade UNKNOWN. No spider cstring, and no actor within 800. No burrow sentence was found in the hintbook.

Control 81, static Collapsable Ceiling, stored `(3052,5484)`, height 141, region 3109. Control 80, the same static, stored `(3051,5226)`, height 141, region 3138. Control 81's groups opcode 16 and opcode 9 on u16 81 and u16 80. Those indexes fit a prop, a control, an actor, and a movable. Prop 196 and prop 197, template Column, opcode 9 on prop 209. Prop 209 is Torch in claw, stored `(2608,5152)`, not a spider. Control 82, static Hive Warrior Door, stored `(3055,5272)`, region 3138, event 0.

## Temple quill

Report `(2251,-5103)`, native `(2251,5103)`. Grade DECODED for the inkwell, the switch, and the two door leaves. Grade UNKNOWN for a quill opening a door. A quill sentence on Prima printed 150 is a force field. It was not matched to this room.

Prop 344, template Inkwell, stored `(2211,5110)`, height 125, region 2339. Kind-3 group 13364 is opcode 9 on u16 91, opcode 5 on u16 350 and u16 343, and opcode 196 on regions 1614 and 4197. Index 91 fits more than one table. Props 350 and 343 are both Lamp, stored `(1888,5136)` and `(1888,5032)`.

Prop 8, template Switch, stored `(2245,5209)`, height 115, region 2354. Kind-4 groups 116 and 146 are opcode 1 on u16 0 and u16 1, byte 4 = 0 then 100. Both indexes fit every object table. The nearby door leaves are movable 0, static left, `(2264,5312)`, region 2345, event 0, and movable 1, static right, `(2264,5230)`, region 2347, event 0. Prop 0 and prop 1 are the Death Idol and an Inviso Light on other regions, so the opcode 1 targets stay unnamed.

Item 2, identity 0xE0649CBA, `66-Ancients stn`, and item 3, identity 0x8013FE62, `Cocos Cap`, are event 0 in this room. Neither is a quill.

## Temple doors

Report `(-310,-2304)`, native `(-310,2304)`. Grade DECODED for two door rows with empty event lists. Grade UNKNOWN for a teleporter. No level-change command is owned by either row.

Movable 88, static Nice Door, stored `(-305,2132)`, height 190, region 1459, flags 0x0182, event 0, 172 units from the report. Movable 89, static Nice Door, stored `(32,2061)`, height 190, region 1461, event 0. No actor is within 800. The three L14 level changes remain stream 0 groups 1462 and 3836, both `020100001c68`, and stream 1 group 9210 `020100001c30`. None is on movable 88 or 89.
