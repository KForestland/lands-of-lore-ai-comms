# Source ids STORY-054 through STORY-060

Read-only pack for the Huline Temple steps. Place is L14_HT unless a row says otherwise. Placements and name tables were read from L14_HT.MIX this pass. Template names are the first 38-byte table at metadata 9592, count 66. Static names are the first 30-byte table at metadata 31148, count 96. Actor-def names are the six records at metadata offset 34336, name at +135. Item identity dwords were read from the level MIX. Definition name-at-index stays LIKELY: GLOBAL.MIX key 3984507021, record base 496, stride 91, identity at +24, 30-byte name slots at 20734. Group command lists come from `scripts/lol2/native_scripts/L14_HT.json` and stay LIKELY. Opcode 3's callee was not entered, so a grant stays LIKELY. Opcode 9, opcode 1, opcode 16, opcode 18, opcode 198, opcode 207, and opcode 210 were not entered. A kind-4 body that ends in an identity is the identity dword only. That tail was not entered.

No template, static, actor-def, or metadata cstring is hanging, spider, coffin, cube, goo, headboard, crack, library, niche, machine, or floating. Stories stay with Astra.

Actor-def labels are 0 LAMPLT, 1 HL2, 2 HIVEW, 3 HIVEW, 4 B_HUMAN, 5 B_HUMAN. Counts are 41, 1, 34, and 20. None of those labels is spider.

The 41-byte cstring run at geometry 423636 has 28 slots and then a zero slot. Geometry u32 at 0xB4 is 423608. That is not the L13 base-plus-22 layout, and these slot numbers were not bound to local variables. Names: 0 Boulder_to_non_exist, 1 Counterweight, 2 Trigger_Special, 3 Pathway_Lit, 4 Idol_Count, 5 Balance_of_Scales, 6 How_many_crystals_have_been_placed, 7 Altar_Count, 8 Raising_Count, 9 Sanctuary_Check, 10 Reset_elevator, 11 Balance_puzzle_solved, 12 Open_Hive_Warrior_Door, 13 Trap_trigger, 14 Is_Luther_on_the_elevator, 15 Number_of_Columns_destroyed, 16 Is_Healing_pool_active, 17 Chamber_of_Voices_elevator, 18 Is_fire_trap_disarmed, 19 the 41 bytes `Make_the_weight_stuff_go_down_with_elevat` with no zero inside the slot, 20 Open_Death_Door, 21 Death_secret_wall, 22 go_to_level_16, 23 Luther_deactivated_switchplate, 24 Boulder_trap_activated, 25 Timer_non_existant, 26 Is_Grinder_active, 27 Hive_warrior_counter. `go_to_level_16` is that cstring. It was not read as a destination level.

Level-change commands re-found this pass are stream 0 group 1462 and stream 0 group 3836, both `020100001c68`, and stream 1 group 9210 `020100001c30` on prop 170, template Side Deco. No object event owns 1462 or 3836. Byte 5 stays unread. The region numbers for 1462 and 3836 stay the ones in `source_ids_042_053.md`. Arrivals, heading unconverted: selector 0 (2576, 3181) heading 60694 region 796; selector 1 (2411, 2413) heading 1 region 864; selector 2 (789, -10774) heading 0 region 2282; selector 3 (-1336, -11466) heading 0 region 4176.

## STORY-054

Grade UNKNOWN for the hanging and for the spiders.

Region 3244, floor -75, ceiling 20, neighbors 3242, 3427, 3246, and 3243, contains prop 86, template Lightning, stored (2413, 3617), height -75, event 566, and prop 187, template Caretaker's corpse. Neighbor region 3427 contains prop 168, template Inviso Light, stored (2523, 3616), event 3094. Region 951, floor -15, ceiling 150, neighbors 911, 948, 952, and 956, contains only prop 274, the other Caretaker's corpse. Neighbor 952 contains prop 283, template Willow4. Neighbor 956 contains control 105, static Blood Smear, event 0. No actor placement is in either neighborhood.

## STORY-055

Grade DECODED for the flute identity sites. Grade UNKNOWN for a coffin. No coffin cstring exists.

Item 77, identity 0xB40E38C4, definition 96, name slot `94-Iron flute`, handler 16, stored (1229, 3556), height -98, region 219, flags 0x0002, event 0. Region 219 and its four neighbors contain only that item.

Movable 76, static Flute Deco, stored (-114, 1516), height 180, region 1307, flags 0x0502. Region floor is 180. Kind 4 group 20258 body ends in identity 0xB40E38C4. Its stream 1 commands are opcode 20, opcode 198 index 13 value 1, opcode 198 index 18 value 1, opcode 5, opcode 196, opcode 1 `01204d006400`, opcode 1 `01204e006400`, and opcode 2 `020100001800`. That opcode 2 is outside the level-change shape. Group 20322 repeats the opcode 198 index 13, the opcode 5, and the opcode 196. This is the only L14 event whose own raw contains the flute identity.

Prop 137, template Tripod, stored (1615, -195), height 0, region 4072, flags 0x0402. Kind 5 group 7066 is an opcode 3 list. One command is `03010000c4380eb404000000`, the flute identity, byte +8 = 4. The same list also grants, each with byte +8 = 4: definition 54 `55-Obs chain`, definition 42 `43-Deathstroke`, definition 21 `22-Darkstorm`, definition 32 `33-Myriad`, definition 65 `64-Rng regen`, definition 47 `48-Gau Might`, definition 136 `134-Dreamstone`, definition 108 `106-Jkar idol` three times, definition 103 `101-Statuette` two times, and definition 105 `103-Cry shard` three times. Two opcode 2 commands in that group are `020100000e14` and `020100000d14`, outside the level-change shape. Kind 6 group 7030 is opcode 210 and was not entered. Kind 2 group 7292 is opcode 2 `020100003d28`, outside the level-change shape. The tripod is not a coffin.

## STORY-056

Grade DECODED for the placed rows and for the absence of an L14 command. Grade UNKNOWN for which nine are thrown and for the fireball-room chokepoint.

Definition 60, name slot `59-Stone cube`, identity 0xF40E4E1D, handler 45. L14 has no placed row of that identity and no command that contains it. L4, L8, L12, L16, and L20 also have no placed row. The other level MIX files were not scanned for placements. The native-script export directory has opcode 3 of this identity only in L16 and L20.

L13 items 3 through 19 are seventeen placed rows of that identity. Stored x runs from -3329 to -3288, y from 444 to 470, height -1230, region 315, flags 0x0002, event 0. L13 has no opcode 3 of that identity. Seventeen is the placed count. It was not reduced to nine.

Opcode 3 of the same identity also exists outside L14. L16 prop 96, template `Stone cb`, stored (415, -10438), height 75, region 9806, kind 4 group has opcode 3 `030100001d4e0ef404000000`, byte +8 = 4, plus opcode 9 `090360000200`, u16 at byte +2 = 96, byte 4 = 2. That target table was not resolved. L16 prop 103, template `Item obj`, stored (-198, -9754), height 125, region 9758, has one opcode 3 `030100001d4e0ef401000000`, byte +8 = 1, among other kind 4 groups that grant other identities. L16 prop 592, template Altar, stored (-2950, 1580), height 0, region 7420, kind 5 group includes one opcode 3 of the cube identity, byte +8 = 4. L20 prop 241, template Crystal, stored (-2135, 3706), height 0, region 375, kind 5 group has two opcode 3 commands of the cube identity, both byte +8 = 1. Those four props are not an L14 chokepoint, and the command counts are not nine.

L14 template Fire is props 379, 380, and 381, stored near (22, 925), (25, 1115), and (35, 1320), heights 137, 143, and 130, regions 749, 749, and 750. Template Fire 2 is props 222 through 229, stored x -28 to 92 and y 957 to 1251, height 133, region 749. Template MoD Flames is a separate set, props 97 through 135, and was not joined to this room.

## STORY-057

Grade UNKNOWN for which button, for a red-goo box, and for the statue that is caught. No goo cstring exists.

Control 73, static Examining Table, stored (2150, 3906), height -80, region 3850, flags 0x0482. Region floor and ceiling are -80 and 20. The same region contains prop 87, template Lightning, stored (2148, 3912). Neighbors are 3851, 487, and 3852. Neither corpse region is a neighbor. Stream 1 group 17152 is opcode 5. Group 17158 is opcode 9 u16 86, byte 4 = 3, and opcode 20. Index 86 exists on more than one table, so the opcode 9 target stays unnamed.

The two corpse rows remain prop 187, region 3244, and prop 274, region 951. Their neighborhoods are under STORY-054. No Button, Button Frame, or 'Button placement is in those neighborhoods.

Static Button controls, slot 25. Opcode 196 words are omitted here. The other commands are the ones listed.

| id | stored x, y | height | region | stream 1 commands besides opcode 196 |
| --- | --- | --- | --- | --- |
| 51 | 911, 4219 | 30 | 3013 | group 16502 opcode 16 and opcode 7 |
| 60 | -3808, 709 | 185 | 3962 | groups 16640 and 16646, opcode 9 u16 57 byte 4 = 0x15 |
| 61 | -3023, -323 | 185 | 3921 | groups 16652 and 16658, opcode 9 u16 179 byte 4 = 0x15 |
| 62 | -2039, -710 | 185 | 3943 | groups 16664 and 16670, opcode 198 index 21 value 1, then value 0 |
| 142 | -399, 973 | 385 | 2132 | opcode 198 index 1 values 1, then 2, then 3; then index 11 value 1; opcode 207 |
| 143 | -399, -327 | 385 | 2132 | same command shape as 142 |
| 144 | 428, -356 | 385 | 2133 | same command shape as 142 |
| 145 | 428, 944 | 385 | 2133 | same command shape as 142 |
| 146 | 2467, 5291 | 35 | 2361 | opcode 196 only, groups 18364 and 18478 |
| 147 | 1923, 4350 | 35 | 1517 | group 18580, one opcode 196 |
| 148 | 1672, 4912 | 96 | 1512 | group 18592, opcode 196 |
| 149 | 106, -2201 | 160 | 3218 | opcode 20, opcode 16, opcode 1, opcode 198 index 0 value 1, then a later group value 0 |
| 150 | -43, -2200 | 160 | 3218 | same command shape as 149 |

Index 57 exists on more than one table. Index 179 fits only the prop table: prop 179, template Balance, stored (-1068, 1244), region 4023, event 0. That fit is the table size, not an entered opcode 9.

Static Button Frame controls 87, 155, and 156 are event 0: (2718, 4221) region 104, (1476, 2460) region 564, and (1465, 1412) region 1907. Movable 'Button rows: 67 (2718, 4224) region 104 group 19368 opcode 196; 82 (6516, 1366) region 701 event 0; 83 (1479, 2461) region 564 group 20352 opcode 196; 84 (1468, 1412) region 1907 group 20394 opcode 196.

Static Statue controls 55, 152, 153, and 154 are event 0, flags 0x0001: (-1190, 3457) region 4080 height 208; (-2391, 3315) region 4092 height 210; (-2251, 3456) region 4093 height 211; (-1065, 3287) region 4082 height 208. Control 74, static Death Statue, stored (1654, 1137), height -91, region 3498, groups 17180 and 17336, contains opcode 196 and opcode 9. The opcode 9 indexes 58 through 63 each exist on more than one table.

## STORY-058

Grade LIKELY for the Pillow cstring rows as pillow placements. Grade UNKNOWN for a headboard, a crack, a red altar, an order, and a library. Headrolls has zero placements. Altar top has zero placements. No crack, library, or red cstring exists.

Template Pillow props:

| id | stored x, y | height | region | floor | group |
| --- | --- | --- | --- | --- | --- |
| 5 | 1068, -11644 | 0 | 4024 | 0 | stream 1 group 84, opcode 20; stream 0 group 84 is a different command |
| 7 | -769, -5318 | 0 | 3907 | 0 | stream 1 group 100, opcode 20 |
| 348 | 2227, 5269 | 120 | 2340 | 120 | event 0 |
| 349 | 2205, 5307 | 120 | 2343 | 120 | event 0 |

Props 348 and 349 sit next to template Switch props 8 and 345. Prop 8, stored (2245, 5209), height 115, region 2354, floor 115, groups 116 and 146. Group 116 has opcode 1 `012001000000` and `012000000000`. Group 146 has opcode 1 `012000006400` and `012001006400`. Both groups also have opcode 5 and opcode 16. Opcode 1 was not entered. Prop 345, stored (2248, 5332), height 115, region 2344, floor 115, groups 13480 and 13504, opcode 5 and opcode 16. Button control 146 is the Button in that y range. None of these names is headboard.

Controls 165 and 166, static altar pieces, stored (2413, 3299) and (2413, 3350), height 0, region 816, event 0. Altar_Count is slot 7 of the 28-slot run. Altar_Open is a separate cstring at geometry 426694, outside that run. Neither cstring was bound to a predicate id.

The Button rows are the table in STORY-057. Controls 149 and 150 share region 3218. Controls 142 and 143 share region 2132. Controls 144 and 145 share region 2133. No command on those groups was read as a library door.

## STORY-059

Grade DECODED for the statuette identity on control 126 and for the cry-shard opcode 3 on control 71. Grade UNKNOWN for an unoccupied niche, a machine, and which placed shard is the second.

Control 126, static Temp Wall Hole, stored (2854, 3913), height 20, region 432, flags 0x0482. Region floor 20, ceiling 30. Kind 4 group 17940 body ends in identity 0x23F81E25, definition 103, name slot `101-Statuette`, handler 0. Commands are opcode 20, opcode 9 `090337010300` u16 311 byte 4 = 3, opcode 9 `09107e000200` u16 126 byte 4 = 2, opcode 2 `020100001800`, and opcode 1 `01204b006400`. Props number 412, controls 168, actors 96, movables 104, and items 78, so u16 311 fits only a prop: prop 311, template Warrior, stored (2849, 3911), height 20, region 432, flags 0x1002, event 0. The same neighborhood contains prop 310 Warrior (2849, 3902) region 433 event 0, prop 312 Warrior (2848, 3923) region 446 event 0, and movable 75, static Goldbar Door, stored (2845, 3913), height 40, region 432, flags 0x0502. Its group is opcode 1 `012049006400` and `01204a006400` only.

Placed statuettes, identity 0x23F81E25, event 0: item 0 (770, 3654) height 0 region 4274 flags 0x0002; item 6 (3242, 2711) height -96 region 4073 flags 0x0002; item 65 (3325, 3617) height -54 region 3901 flags 0x3102. Prop 137's group 7066 grants that identity twice, as listed under STORY-055. Template Statuette has zero prop placements.

Control 71, static Crystal Switch, stored (3043, 5684), height 0, region 3097, flags 0x0482. Kind 3 group 16904 contains opcode 3 `03010000de1b42d004000000`, identity 0xD0421BDE, definition 105, name slot `103-Cry shard`, handler 0, byte +8 = 4. The same group has opcode 9 u16 186, which fits only prop 186, template Lite Beam, stored (3037, 5878), height 15, region 3060. Kind 4 group 17088 body ends in the same cry-shard identity, and its child command is opcode 5, not opcode 3. The twelve placed `103-Cry shard` rows are items 4, 7 through 11, 12 through 16, and 67 in `source_ids_042_053.md`. No command was found that marks one of them as the second.

## STORY-060

Grade DECODED for the six Bowls rows and for what identity each kind-4 body carries. Grade UNKNOWN for a floating bowl and for the passage behind them. Templates Bowl, Bowl 1, and Bowl 2 have zero placements. No kind-4 body and no opcode 3 on a Bowls row uses identity 0xD0421BDE.

| id | stored x, y | height | region | floor | identity at the kind-4 tail |
| --- | --- | --- | --- | --- | --- |
| prop 200 | 1504, 6217 | 122 | 2926 | 120 | 0x0A02A378, definition 125, `123-Pois paint`, group 11562 opcode 3 byte +8 = 4 |
| prop 201 | 1663, 6218 | 122 | 2918 | 120 | 0xBFDDCCA3, definition 109, `107-Aloe`, group 11620 opcode 3 byte +8 = 4 |
| prop 284 | 3030, 4507 | 42 | 133 | 40 | kind 4 group 13042 body ends in the poison identity; child commands are opcode 16, opcode 207, opcode 2 `020100001800`, opcode 5 |
| prop 285 | 3059, 4507 | 42 | 133 | 40 | kind 4 group 13114 body ends in the aloe identity; same child shape |
| prop 369 | 2441, 3691 | 27 | 806 | 25 | kind 4 group 14532 body ends in the poison identity; children opcode 2 `020100001800`, opcode 207, opcode 5 |
| prop 370 | 2375, 3691 | 27 | 806 | 25 | kind 4 group 14844 body ends in the aloe identity; same child shape |

Props 200 and 201 are the STORY-050 bowls. Each stored height is two above that region's floor. Region 806 also holds control 67 Death Block and control 68 Life Block, both event 0. Region 133 also holds control 69 Death Block and control 70 Life Block, both event 0. The level-change commands are the three listed at the top of this file. None sits on these bowl groups.
