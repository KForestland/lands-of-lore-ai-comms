# Class-C dossier, 12 November 2026

The 13 "this should happen" rows in `playtest_feedback_20261023/TRIAGE_r19a_20261112.md` section C. Owner coordinates below are screen order (x, horizontal-z, height). Godot and the native JSON are (x, height, z), with Godot z equal to the negation of the stored y word.

Sources read this pass: `opus_work/lol2_play_r19pre/scripts/lol2/native_scripts/{LEVEL}.json` (format `lol2-native-scripts-2`), the census at `grok_research/interactables_census/census.json`, and the port scripts in that same tree. No Godot was launched. Opcode 3, opcode 196's callee, opcode 198, opcode 204, and the opcode 18 callee were not entered here. A level-change shape is only opcode 2 prefix `020100001c`; byte 5 stays unread (`source_ids_066_075.md` line 3). Bit 0x0004 on opcode 18 is the proven direct-relocation bit; a flag word without it is not a relocation (`I29_opcode18_flags.md` lines 3 and 23). Kind 5 value 4 is a step-on (`BC01_dragon_telepad.md` lines 19–20). Kind 10 has no matcher arm (`native_script_host.gd:783`).

Grades: PROVEN, LIKELY, UNKNOWN. A census `port=` name is a row label. A script hosts the behavior only where a line below says it runs.

## 1. Temple floor and spiders

Report `2026-11-12T06-25-13`, L14_HT, owner (2993, −5231, 31). "the flor should erupt here and spiders should spawn out".

Nearest scripted object is control 80 at Godot (3051, 141, −5226), flat distance 58, height 110 above the stand, region 3138, flags 1153. Census: scripted control, port `l14_spider_burrow.gd`, groups 17658, 17728, 17734. Four floor props sit around the stand: prop 199 (2955, 0, −5158), prop 197 (2955, 0, −5350), prop 198 (3147, 0, −5158), prop 196 (3147, 0, −5350), each template index 50, each with the same port label.

Control 80's kind 6 value 7 group 17658 (file 11744416) calls opcode 9 arm 6 on controls 80 and 81 (`091050000600`, `091051000600`), opcode 20 on control 82, opcode 16 on control 81, and opcode 9 arm 2 on props 199, 198, 196, 197, 195, and 194. Arm 6 is undecoded (`native_script_host.gd:1612–1614`). Arm 2 is a LIKELY player-record release, and the adapter that would run it is off (`native_script_host.gd:1527–1535`). Kind 5 value 1 group 17728 is opcode 2 `020100001100`, which is outside the level-change shape. Kind 5 value 4 group 17734 is opcode 16 on control 80. No opcode 196 sits in these three groups, so no floor target is stored on them.

The eruption and the spawn stay UNKNOWN. The port receipt at `l14_spider_burrow.gd:10` is (3061, 0, −5374), reach 64, which is 158 from this stand. `use()` at lines 42–48 sets `struck` and prints "The ceiling groans." Lines 7 and 16 keep `FLOOR_MOVED` false.

Replacement: admit control 80's three groups from a stand on the floor under it. Leave the floor quads where the pack built them until arm 6 is entered.

## 2. Claw Mountains ruloi entrance

Report `2026-11-12T06-47-40`, L12_CM, owner (3063, −18712, −1198). "ruloi entrencae do not work".

Nearest object is prop 0 at (3099, −1180, −18773), flat distance 71, template index 33, region 3636. Census has no row. Its one event is kind 6 value 20 group 0 (file 9827916), opcode 2 `020100003900`. That prefix is outside the level-change shape. What arm 0x39 does stays UNKNOWN.

The level-change shape on this level's entrance is control 74 at (3684, −1292, −19361), flat distance 898, region 2434. Census: scripted control, port `l12_citadel.gd`, group 2808. Kind 5 value 4 group 2808 (file 9828720) is opcode 21 on prop 120, opcode 2 `020100001c2d`, then opcode 9 on actors 30 and 31. Byte 5 of that level change stays unread. The step-on admission is PROVEN for kind 5 value 4. The destination selector stays UNKNOWN.

`l12_citadel.gd:49–61` aims at (3684, −1240, −19361), plays the citadel movie, then calls `_change_level`. That host covers control 74. It does not read prop 0.

Replacement: keep the movie gate on control 74. Prop 0's arm 0x39 stays unhosted until that arm is entered.

## 3. Citadel teleporter

Report `2026-11-12T06-52-18`, L13_RC, owner (−4947, 1707, −867). "this is a teleporter".

Control 53 at (−4955, −899, 1711), flat distance 9, height −899 against the owner's −867, region 987, flags 1154. Census has no row. One event: kind 5 value 4 group 8134 (file 6854311), opcode 18 kind 1 target 0, words (−3258, −5589, 0), flags 0x0485. Bit 0x0004 is set, so this is a PROVEN direct relocation of the player. Kind 5 value 4 makes the trigger a PROVEN step-on. A landing that uses the placement axis on the first two words is LIKELY Godot (−3258, 0, 5589). The third stored word is 0. The opcode 18 callee was not entered, so the landing stays LIKELY.

The port has no script for control 53. The accepted Citadel robot (`robot/L13_RC/20261112_7501c30-v1g`) stood near the point, aimed empty, and dropped through the floor at height about −1092, region 987. The row was BLOCKED.

Replacement: a step-on at control 53 runs group 8134 with the stored words and flags 0x0485, and the floor under the control has to hold the player at the control's height. The destination name stays the stored words.

## 4. Citadel vault opener

Report `2026-11-12T06-58-25`, L13_RC, owner (−4576, 1765, −1008). "this open the valut".

Prop 250 at (−4534, −1040, 1767), flat distance 42, template index 13, region 995, flags 1666. Census has no row. Two aimed records both end on movable 84:

- Kind 4 value 0, predicate 206, group 4366 (file 6852947): opcode 6 three times, opcode 9 on prop 250, opcode 7, opcode 16, opcode 9 kind 32 target 84 (`092054001500`), opcode 7.
- Kind 4 value 0, predicate 208, group 4456 (file 6852971): the same shape, then opcode 1 on movable 76 with byte 4 = 0, then opcode 9 on movable 84 again.

Kind 4 value 0 matches when the host passes `arg_c` 0 (`native_script_host.gd:771–780`). Opcode 9 arm 0x15 is a LIKELY enqueue of that object's kind 6 record with caller byte 0x14, and `opcode9_enqueue` is off (`native_script_host.gd:1546–1557`). Whether movable 84 then opens stays UNKNOWN. Predicate 206 stays in the row.

Movable 84 at (−4426, −1040, 1753) has its own kind 6 groups 9904 and 9922, which set opcode 16 and opcode 1 byte 4 = 100 or 0 on itself. Movable 83 at (−4181, −1040, 1177) is the other platform. Its groups write movables 83 and 75. It is the Class B stall the robot already graded RED, and it is a different object from this opener.

The port has no script for prop 250. The same robot stood at (−4593, −1008, 1741), 29 from the owner point, crosshair empty, real E with no change. That row is RED.

Replacement: aimed E on prop 250 runs groups 4366 and 4456, including the enqueue of movable 84. Keep predicate 206. Leave movable 83 on its own platform row.

## 5. City gas toward three doors

Report `2026-11-12T07-01-57`, L16_CA, owner (2198, −869, 32). "this gass\passma\thing shoul go to the 3 doors and blow them up".

Nearest object is prop 570 at (2093, 15, −910), flat distance 113, template index 74, region 6362. The L16 name slice that names template 0 `Altar`, 55 `Fountain`, and 61 `Ball O Smoke` does not name index 74 (`source_ids_066_075.md` line 242). Census has no row. Twenty events. Its kind 4 groups 31042, 31072, and 31102 each contain an opcode 3 `030100003cc973de04000000` (identity 0xDE73C93C, byte +8 = 4) plus opcode 16 and opcode 5. The identity was not named this pass. Control 154 at (1981, 15, −964) calls opcode 9 on props 516, 570, 590, 518, and 517 from five kind 4 groups (file 18728272 onward). That is five props. What they do stays UNKNOWN.

The three-door record is a farther object. Prop 602, template 61 Ball O Smoke, at (2289, 18, −648), flat distance 239, region 6098. Census ports `l16_dry_fountain.gd`, `l16_fountain_ball.gd`, and `l16_greenhouse.gd`, groups 37758 and 37776. Kind 6 group 37758 is opcode 18 on itself, words (2290, 2951, 0), flags 0x0812. Bit 0x0004 is clear, so that command is not a relocation (`I29` line 25). Kind 10 group 37776 (file 18725340) is opcode 2 `020100000c05`, opcode 9, opcode 15 on prop 136, and opcode 1 byte 4 = 100 on movables 92, 94, and 93. Those three movables are the FireWall doors (`I01_ne_tower_walkway.md` line 3, name LIKELY). The kind 10 matcher does not run this record (`native_script_host.gd:783`, `I12_kind10_matcher.md`).

`l16_greenhouse.gd` hosts an adapter for prop 602: silverleaf on the plate, hourglass, a drift at 120 units/s from (2289, 18, −648) to (2290, 18, −2951), then `progression.fire("prop:602", 10)` at line 95 and `_open_doors()` poses movables 92, 93, and 94 to travel 100 (lines 52–56). The header (lines 8–11) says the 120 and the door poses are the adapter. Prop 570 is outside that script.

Replacement: keep the greenhouse adapter on prop 602. Prop 570 and control 154 stay a separate row until opcode 3 of identity 0xDE73C93C and control 154's opcode 9 arms are entered.

## 6. City box into a slot

Report `2026-11-12T07-02-41`, L16_CA, owner (15946, 3923, 132). "need to puch this box in the slott".

Control 119 at (15948, 100, 4005), flat distance 82, slot byte 50, region 7655, flags 13698. Census has no row. Slot 50 is the Key Object slot (`I02_ne_tower_interior.md` lines 9–11, name LIKELY). One event: kind 10 value 0 group 43204 (file 18726962). The group is opcode 204 on region 7644, opcode 20 on control 119 byte 4 = 192, opcode 9 on prop 398, opcode 9 on control 119, and opcode 18 on control 119, words (16002, −3958, 0), flags 0x0804. Bit 0x0004 is set, so the opcode 18 is a PROVEN direct relocation of control 119 (`I29` lines 13 and 23). A landing that flips the second word is LIKELY Godot (16002, 0, 3958), 66 from the stand. Opcode 204 and opcode 9 in the same group stay UNKNOWN. Kind 10 does not match, so the port never reaches the relocation.

Replacement: give control 119 a kind 10 match that runs group 43204, including the stored relocation. The push verb stays the owner's until the kind 10 compare's two arguments are read (`I12`).

## 7. Ivory chip in the hands

Report `2026-11-12T07-04-37`, L16_CA, owner (−4260, 1533, 82). "ivory chip in the hands here i think".

Prop 223 at (−4406, 50, 1537), flat distance 146, region 8186. Census has no row. The name Ivory Chip Gargoyle is LIKELY (`source_ids_066_075.md` line 169). Kind 4 value 0, predicate 206, group 6090 (file 18712604): opcode 16, opcode 9 on prop 223 (`0903df001500`, arm 0x15), opcode 3 `03010000090c2e0404000000`, opcode 5. The opcode 3 identity is 0x042E0C09, definition 107, name slot `105-Ivory chip`, handler 90 (line 135 of the same note, name LIKELY). Opcode 3 was not entered, so the grant stays UNKNOWN and the identity match stays LIKELY. Group 6126 is opcode 196 on regions 8167 through 8187. The accepted floor formula is a signed word at byte +4, byte 6 = 0, byte 7 = speed (`I03_starry_tower.md` line 30). Those words were not read this pass, so the floor targets stay UNKNOWN.

`l16_sw_chips.gd` places carried chips on controls 173–176. It does not read prop 223.

Replacement: aimed E on prop 223 runs group 6090 and can grant identity 0x042E0C09 once opcode 3 is hosted. The region floors in group 6126 wait on a read of their target words.

## 8. Puzzle box

Report `2026-11-12T07-04-57`, L16_CA, owner (−3896, 1399, 2). "pussle box".

Control 107 at (−3951, −30, 1379), flat distance 59, slot byte 53, region 8146, flags 386, zero events. Slot 53 is Push/Pull (`source_ids_066_075.md` line 173). Census labels the port `l16_centre_tower.gd` with an empty group list. That script's header (lines 11–13) says the box, the disk, and the yellow figure have no row in the four corner towers, and that Push/Pull controls 71, 107, and 108 are a different set. Its hall point is (5443, 32, 9749). `act2_progression.gd:43` lists control 107 in `STRUCK_SKIP`, so the generic strike binder also leaves it alone. The nearest props (470, 474, 467, 469, 472) carry a single unlinked kind 1 record each.

The puzzle at this stand stays UNKNOWN. The centre-tower mantle host is a different place.

Replacement: leave control 107 eventless. A puzzle box here needs a command that is not on this control.

## 9. Ivory chips in the southwest

Report `2026-11-12T07-12-10`, L16_CA, owner (−9499, 12902, 32). "ivoriy chips inn here".

Control 176 at (−9505, 30, 12936), flat distance 35, slot byte 45, region 7115. Census: scripted control, port `l16_sw_chips.gd`, group 48818. Slot 45 is Ivory Chip Block (`source_ids_066_075.md` lines 175–185, name LIKELY). Kind 4 value 3 group 48818 (file 18729196): opcode 9 on prop 139 arm 0x15, opcode 20 on control 176 byte 4 = 207, opcode 9 on control 172, opcode 2 `020100001800` (outside the level-change shape), opcode 5. Arm 0x15 is the LIKELY enqueue, adapter off. The rest of the group stays UNKNOWN. Control 175, 150 away, has the same shape in group 48778.

`l16_sw_chips.gd:3–6` and `141–151` take a carried chip id on E and record the pedestal. Line 4 states that prop 604 stays whole and doors 89–91 stay shut. The script does not fire group 48818.

Replacement: the place gesture can stay. Firing group 48818, and whatever prop 604 and doors 89–91 do after the enqueue, waits on those opcodes.

## 10. Huline, everything moves

Report `2026-11-12T07-19-17`, L17_HC, owner (−4953, 6455, 32). "here everting moves".

Nearest scripted object is prop 156 at (−5123, 92, 6383), flat distance 185, template index 17, region 83, flags 17411. Census has no row. Three kind 9 groups (file 4787530):

- 3226: opcode 2 `020100000c05`, opcode 16 on prop 156, opcode 14 on prop 87, opcode 9 on prop 156, opcode 5.
- 3264: opcode 2 `020100000b05` and the same following shape.
- 3302, predicate 206: opcode 208 and opcode 20 on prop 156 byte 4 = 105.

Both opcode 2 prefixes are outside the level-change shape. Actor 42 at (−5129, 165, 6382) has one opcode 3 of kind 192. Prop 87's kind 2 group 2132 is opcode 13 on actor 42. None of these commands has a decoded "move everything" effect. The motion stays UNKNOWN.

`l17_beast_blade.gd`, `l17_beast_carry.gd`, and `l17_cavern_run.gd` do not name prop 156. The beast carry is region 1293 group 1566 (`l17_beast_carry.gd:18`), a different number.

Replacement: host prop 156's three kind 9 groups once opcode 14, opcode 208, and the two opcode 2 arms are entered. Until then the stand has no motion script.

## 11. Laboratory, next map

Report `2026-11-12T07-22-31`, L19_BC, owner (882, −1494, −98). "the next map loding is incorect".

Props 174, 173, and 175, the three nearest objects (flat distances 150, 160, and 216), have zero events. Census has no rows. Movables 64 and 65 at (650, −125, −1485) and (650, −125, −1545), about 232 away, each have one kind 4 value 0 predicate 206 group that sets opcode 16 and opcode 1 byte 4 = 100 on both bodies. That is a door pair. It is not a level change.

L19's level-change commands are three, and none is an object event at this stand (`source_ids_076_085.md` line 83):

- Region 22, kind 12 event 2, stream 0 group 0, `020100001c51`, predicate null (file 6198274).
- Region 2369, kind 12 event 2, group 15784, `020100001c34`, predicate 204 entry `0002340000`.
- Region 2369, kind 12 event 2, group 15790, `020100001c54`, predicate 205 entry `0002340001`.

Byte 5 stays unread in that source-id note. A later trigger note grades the two region 2369 commands as level 20 selectors 1 and 2 and grades the travel BLOCKED because nothing proven writes the predicate array (`AX01_act3_triggers.md` STORY-087). The published mark for region 2369 is stored (3321, 875), Godot (3321, −875) (`AE12_L19_BC_map_mark.md` line 13, `BK17_main_chain_stops_20261110.md` line 5). That mark is 2516 from this stand.

Which command loaded a map at (882, −1494) stays UNKNOWN. The port's region 2369 seed is the arrival adapter in the AX01 note, and it is the other place.

Replacement: a wrong load at this stand needs the command that actually ran there. Region 2369 stays the laboratory exit at its own mark.

## 12. Laboratory door blocked

Report `2026-11-12T07-23-11`, L19_BC, owner (958, −2453, −93). "the door is blocked".

Movable 60 at (865, −125, −2481), flat distance 97, and movable 59 at (865, −125, −2421), flat distance 98, region 2371, flags 1410, static byte 0. Census has no row for either. Each has the same three shapes:

- Kind 4 value 0, predicate 206 (groups 4842 and 4662, files 6158349 and 6158313): opcode 198, opcode 196 on regions 1894–1902, opcode 16 set, opcode 1 byte 4 = 100 on both movables.
- Kind 4 value 0, predicate 207 (groups 4986 and 4806): opcode 16 clear and opcode 1 byte 4 = 0 on both.
- Kind 6 value 16: opcode 197 on region 2371.

Opcode 1 was not entered (`source_ids_066_075.md` line 3). The 100/0 pair is the same byte the door hosts already treat as travel, so a paired open and shut is LIKELY. The opcode 196 floor targets were not read, so a floor sitting in the doorway stays UNKNOWN. Why the door is blocked stays UNKNOWN.

The port has no script for movables 59 and 60.

Replacement: aimed use runs the predicate 206 groups (travel 100 on both) and the predicate 207 groups (travel 0 on both). Read the opcode 196 words before moving those floors.

## 13. Blood altar that drains

Report `2026-11-12T07-24-27`, L19_BC, owner (1973, −888, −93). "this is the blod alter that drains".

Nearest object is actor 39 at (1939, −125, −891), flat distance 34, region 2182, flags 30082, def 0. Census: scripted actor, port `l19_dawn_curse.gd`. Def 0 is DAWNL19, stored (1939, 891), and that identity is DECODED (`source_ids_076_085.md` line 79, `AE12_L19_BC_map_mark.md` line 14). The actor's groups are pose and sound (opcode 16, opcode 8, opcode 14, opcode 2) plus opcode 9 on props 2 and 3. No command on actor 39 is a decoded drain.

The template named Blood bowl is prop 269, stored (13, 899), region 686 (`source_ids_076_085.md` line 85). That is a different room. Local slot 1 is the cstring `Blood_bowl_timer_on` (line 77). It was not found on actor 39's groups.

`l19_dawn_curse.gd:47` clicks Dawn at (2802, −1000, −882), reach 30, which is 829 from this stand. `_click_dawn` (lines 221–233) counts clicks, says the curse line, and grants the ruby. It does not change health or a floor at actor 39.

The body at the stand is Dawn. The drain stays UNKNOWN.

Replacement: Dawn's click stays on prop 78's point. A drain at actor 39 needs a command that is not in actor 39's groups. Prop 269 remains the Blood bowl row.

## Build list

| # | Stand | Native row | Original effect | Port | Replacement while it stays undecoded |
| --- | --- | --- | --- | --- | --- |
| 1 | L14 (2993, −5231, 31) | control 80 groups 17658, 17728, 17734 | UNKNOWN erupt and spawn | receipt 158 away, floor stays | admit the three groups; leave the floor |
| 2 | L12 (3063, −18712, −1198) | prop 0 group 0, arm 0x39 | UNKNOWN | movie gate is control 74, 898 away | keep the gate on control 74 |
| 3 | L13 (−4947, 1707, −867) | control 53 group 8134 | PROVEN step-on relocation, landing LIKELY (−3258, 0, 5589) | none; robot BLOCKED | step-on plus the stored words, and a floor |
| 4 | L13 (−4576, 1765, −1008) | prop 250 groups 4366 and 4456 | UNKNOWN open of movable 84 | none; robot RED | aimed E runs both groups; predicate 206 stays |
| 5 | L16 (2198, −869, 32) | prop 570, and prop 602 at distance 239 | 570 UNKNOWN; 602's three doors are the kind 10 group | greenhouse adapter on 602 only | keep 602's adapter; leave 570 separate |
| 6 | L16 (15946, 3923, 132) | control 119 group 43204 | PROVEN relocation form inside an unhosted kind 10 | none | match kind 10 and run the stored relocation |
| 7 | L16 (−4260, 1533, 82) | prop 223 groups 6090 and 6126 | LIKELY ivory identity; grant and floors UNKNOWN | none | aimed E can grant 0x042E0C09 once opcode 3 is hosted |
| 8 | L16 (−3896, 1399, 2) | control 107, zero events | UNKNOWN | centre-tower script disclaims it | leave it eventless |
| 9 | L16 (−9499, 12902, 32) | control 176 group 48818 | enqueue LIKELY; rest UNKNOWN | place gesture; doors stay shut | gesture can stay; fire 48818 when the arms are hosted |
| 10 | L17 (−4953, 6455, 32) | prop 156 groups 3226, 3264, 3302 | UNKNOWN | none | host the three kind 9 groups when the arms are entered |
| 11 | L19 (882, −1494, −98) | props 173–175 have zero events | UNKNOWN at this stand | region 2369 is 2516 away | find the command that ran here; leave 2369 at its mark |
| 12 | L19 (958, −2453, −93) | movables 59 and 60 | LIKELY paired travel 100/0; the block UNKNOWN | none | run the 206 and 207 groups; read the floor words first |
| 13 | L19 (1973, −888, −93) | actor 39 DAWNL19 | Dawn DECODED; the drain UNKNOWN | Dawn click is 829 away | keep Dawn's click on prop 78; the drain needs its own command |
