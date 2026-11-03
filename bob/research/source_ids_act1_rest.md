# Source ids for the remaining Act 1 MISSING beats

Read-only pack for the MISSING rows in `grok_research/act1_completeness_duck.md` that are not already sections of `source_ids_act1_pt3.md`. The duck table has 24 MISSING rows. Thirteen are the playtest pack: beats 14, 30, 31, 39, 40, 40a, 40b, 52, 53, 59, 63, 70, and 73. This file is the other eleven. Beats 49 and 66 are one Dawn scene, so the file has ten sections. Order is the owner blocker first, then the route, then the crate puzzles. This file only names original ids. Stories stay with Astra.

A placement is stored as native x, native y, height. Godot Z is the native y with the sign flipped, the same map as the playtest pack. Placements, static names, prop templates, and actor-def names were read from the level MIX this pass. Static names are the longest 30-byte cstring run of `u32(meta, 0x44)` slots: L1_DC at 25553 count 61, L3_DH at 24009 count 77, L4_HJ at 43522 count 98, L7_DH at 25006 count 47. Each geometry sha256 matched that level JSON's source pin. Quoted command bytes were compared with the MIX at the JSON `file_offset` and matched. A fish group marked below as read from the JSON was not byte-matched. Opcode 1, opcode 2, opcode 3, opcode 5, opcode 9, opcode 12, opcode 16, opcode 20, opcode 21, and opcode 198 were not entered. A level-change shape is only `020100001c`, and byte 5 stays unread. An opcode 1 or opcode 9 index is named only when it fits one table. Definition name-at-index stays LIKELY: GLOBAL.MIX key 3984507021, record base 496, stride 91, identity at +24, 30-byte names at 20734. The flute witness is still definition 96, `94-Iron flute`. A kind-4 identity is the dword only, so a grant stays LIKELY. Locals are named and not bound. Neighbor 65535 stays 65535.

## Password and the thief

Beat 43. Prima printed 66 (hintbook.txt 2338) says to hear a password, find the place for it, and meet a local thief. Grade DECODED for the placed rows below. Grade UNKNOWN for which row is the man the owner could not find, and for a password being spoken. Triage A 17-33-29 says that man is absent. No L4 actor-def name is thief, mauri, or password. The 57 local cstrings have none of those words either. L4_HJ.MIX sha256 `517afe6d59a4a06212bf4aea7eb42dfbb07826a4677fb77a4032674e64657e8f`.

Two controls share the confidante static names, about two units apart:

| id | static | stored x, y | height | region | flags |
| --- | --- | --- | --- | --- | --- |
| 123 | Confidante | -1283, 4228 | 24 | 3405 | 0x5482 |
| 112 | Confidante post fire | -1281, 4225 | 24 | 3404 | 0x5482 |

Control 123 kind-6 group 25764 contains opcode 198 byte 4 = 27, value 1. Slot 27 is `Met_Confidant`, unbound. Kind-9 group 25802 contains opcode 198 byte 4 = 39, value 1. Slot 39 is `Killed_Confidante`, unbound. The same group also has opcode 16 on u16 492, byte 4 = 5. Index 492 fits only a prop: prop 492, template City grass, stored `(-1270,4301)`, region 3408. Control 112 kind-9 group 25628 also writes slot 39 to 1. Groups 25628, 25764, and 25802 each contain opcode 2 `020100002700`, which is outside the level-change shape.

Region 3642, centroid `(-2422,5346)`, floor 0, is the den entry. Stream 0 group 7338 is four commands: opcode 9 byte 4 = 10 on u16 428 and u16 429, both props (prop 428 and prop 429 are Lantern, stored `(-1871,5460)` and `(-1899,5509)`, region 3716), opcode 9 byte 4 = 10 on u16 100, and opcode 12 `0c1086002c00`. Index 100 fits a prop and a control. Control 100 is static Kelsrick's stool, stored `(-1901,5509)`, region 3716, the same region as actor 64, def Kelsrick, stored `(-1892,5475)`. Opcode 12 was not entered. Its byte split is u16 134 at +2 and byte 4 = 44. Index 134 fits a prop and a control. Prop 134 is template L PALM, stored `(4504,-3398)`, region 3065. Control 134 is static Table, stored `(-2146,5296)`, height 0, heading 50224, flags 0x0082, region 3702, and that control has no group. Actors within 800 of the table are four DINO rows and Kelsrick. Kelsrick's def name is not the thief name.

## Dark Halls bookshelf

Beat 50. Prima printed 68 (hintbook.txt 2400) says to stack boxes, climb, and attack the bookshelf left of the library. Grade DECODED for the bookcase, the lockout door, and the nearby level-change. Grade UNKNOWN for stacking, climbing, and a strike that runs that level change. L4_HJ, same archive as the password section.

Control 79, static Bookcase2, stored `(5315,-2194)`, height 0, flags 0x4482, region 3200. Across groups 18766, 18798, 18810, and 18822 the commands are opcode 15, opcode 5, opcode 9, and opcode 197 on u16 79. Index 79 fits a prop, a control, an item, and a movable. None of those four groups contains `020100001c`.

Region 3205, centroid `(5255,-2207)`, floor 0, ceiling 130, neighbors 3207, 65535, 3211, 3204, 450. Event 4 group 6292 is opcode 9 byte 4 = 3 on u16 78, then `020100001c27`. Byte 5 stays unread. Index 78 fits a prop, a control, an item, and a movable. Control 78, static Lockout door, stored `(5299,-2197)`, height 76, flags 0x1081, region 3211, has no group. Movable 78, static right gate, is the village gate at `(-1378,5289)`, a different place. Region 3200 is not a neighbor of region 3205. They both name neighbor 3211. Region 3191, centroid `(5629,-2425)`, group 6226 is opcode 9 byte 4 = 16 on u16 6017, which fits only a prop. That group has no level-change command.

The same pocket holds the crate controls. Within 400 of the region 3205 centroid the static names are 10 x 10 crate, 20 x 20 crate, and 40 x 40 crate, plus control 140 Door Frame. Their event lists were not copied. The bookcase groups do not name those crate indexes.

## Draracle bars

Beat 18. Prima printed 56 says the third visit bars the hall. Grade DECODED for the four bar rows, the Draracle door, and region 1174's group. Grade UNKNOWN for the bars moving and for the visit count that runs the group. L3_DH.MIX sha256 `bd85c12d4a2cff0cc200309e72a7771745ce5c78f1a83da4d60cba81d831ccac`.

| id | static | stored x, y | height | region | flags | byte 34 | byte 36 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 71 | Bar | -3789, 1122 | -120 | 1151 | 0x0181 | 0 | 100 |
| 72 | Bar | -3789, 1100 | -120 | 1157 | 0x0181 | 0 | 100 |
| 73 | Bar | -3789, 1076 | -120 | 1163 | 0x0181 | 0 | 100 |
| 74 | Bar | -3789, 1052 | -120 | 1169 | 0x0181 | 0 | 100 |

Heading is 0 on all four. None of the four has a group. Region 1174, centroid `(-3448,1088)`, floor 0, event 2, predicate index 45, entry `0003110000`. That entry was not interpreted. Stream 0 group 1364, 19 commands, includes opcode 1 byte 4 = 100 on u16 71, 72, 73, and 74, then opcode 198 byte 4 = 17, value 1, then opcode 1 byte 4 = 0 on u16 77. Slot 17 is `First_bars`, unbound. Each of those five indexes fits a prop, a control, and a movable. Movable 77, static Iron Door, stored `(-4060,844)`, flags 0x0182, region 1182, is the row at index 77. The same group also has opcode 9 byte 4 = 16 on u16 136, 82, 137, 139, and 138. Index 82 fits a prop, a control, and a movable. Indexes 136, 137, 138, and 139 fit a prop and a control. The props at those indexes are Torch, StalagPole 1, Torch, Floor Lamp, and Floor Lamp. StalagPole 1 is stored `(3094,1114)`, region 1424.

Control 79, static Draracle door, stored `(-3625,372)`, height 0, heading 16384, flags 0x0402, region 1220. Kind-4 group 6976, predicate 55, is opcode 20 on u16 79 and opcode 198 byte 4 = 19, value 3. Slot 19 is `Draracle_return`, unbound. Kind-8 group 6998 is opcode 20 on u16 79. Index 79 fits a prop, a control, and a movable. Those two groups do not contain the opcode 1s on u16 71 through 74.

## Dawn and the rune copy

Beats 49 and 66, one scene. Prima printed 68 (hintbook.txt 2392) says to give Dawn one rune copy on leaving the Hive, then give Julian the second in the library and take a Power Orb. Prima printed 78 (hintbook.txt 2701) says Dawn is waiting in the jungle light. Grade DECODED for the one Dawn actor and for group 29704. Grade UNKNOWN for speech, for handing over a rune, and for the library visit. Triage C 17-48-05 says Dawn does not speak. No second row uses static slot 56, `Dawn after Hive Cave`: that slot has zero control placements and zero movable placements.

Actor 63, def DawnL4, stored `(-5710,-3937)`, height -100, heading 39321, flags 0x7582, region 2888. Kind-4 group 29704, predicate 23, contains opcode 198 byte 4 = 17, value 1. Slot 17 is `Gave_Dawn_Runes`, unbound. The same group has opcode 2 `020100000b05`, `020100000c05`, and `020100001800`, all outside the level-change shape, then opcode 9 byte 4 = 20 and opcode 16 byte 4 = 3 on u16 63. Index 63 fits a prop, a control, an actor, an item, and a movable. The group has no opcode 3.

L4 has no Julian actor def. The thirteen def names are TIG_ROG, TIG_MAL, TIG_FEM, TIG_CUB, DINO, BACL4, L4WW, Kelsrick, DawnL4, GGuard, VILLAGER, B_HUMAN, and SSAR. Identity 0x87F22ADE, definition 85, `83-Power orb`, handler 37, has no placed L4 item and no L4 opcode 3. Other Dawn cstrings on this level, unbound here, are slot 19 `Has_Dawn_been_triggered`, slot 25 `Dawn_touch_with_item`, slot 26 `Dawn_dam_out_cave`, and slot 28 `Met_Dawn`. Actor 63 has further groups whose heads are opcode 5, opcode 8, opcode 9, and opcode 16 on u16 63. Those heads were not copied.

## Giant Fish

Beat 33. Prima printed 63 (hintbook.txt 2229) says the man at the bridge is eaten by the Giant Fish. Grade DECODED for the river regions that carry the fish-shaped command list. Grade UNKNOWN for the clip playing. Drowning on this river is a separate hosted beat and is not given new ids here.

The stored river point used for the search is `(5452,4100)`. A region counted when its event byte is 4 and its group contains opcode 2 `020100003900` plus opcode 21 whose byte 4 is 28. That count is 432. Opcode 2 `020100003900` is outside the level-change shape. Opcode 21 `1503a1001c00` is u16 161, byte 4 = 28, byte 5 = 0. Index 161 fits a prop and a control. `movie_table.json` index 28 is the cstring `fishdeth`, file `fishdeth.vqa`. That name-at-index stays LIKELY. Opcode 21 was not entered.

Nearest eight centroids:

| units | region | center | group | commands |
| --- | --- | --- | --- | --- |
| 81 | 4384 | 5383, 4058 | 16886 | opcode 21, opcode 2 |
| 144 | 4388 | 5431, 3958 | 17064 | opcode 198, opcode 21, opcode 2 |
| 207 | 4365 | 5323, 4262 | 16478 | same three |
| 217 | 4385 | 5241, 4049 | 16904 | same three |
| 229 | 4389 | 5303, 3926 | 17088 | same three |
| 310 | 4368 | 5180, 4250 | 16550 | same three |
| 346 | 4386 | 5112, 4034 | 16928 | same three |
| 356 | 4431 | 5156, 3902 | 17562 | same three |

Groups 16886 and 17064 were byte-matched to the MIX. The opcode 198 in 17064 is `c60000003101`, byte 4 = 49, value 1. Slot 49 is `Stop_Hive_Warrior_OT`, unbound. Region 4384's group has no opcode 198. The other six nearest groups were read from the JSON and were not each byte-matched.

## Cave mace and the roach crates

Beat 10. Prima printed 56 (hintbook.txt 2047) says to stack the boxes, climb to a mace, and use it on the cockroaches. Grade DECODED for the crate controls and the two mace items in that room. Grade UNKNOWN for dragging, stacking, and striking with the mace. L1_DC.MIX sha256 `6384ec4d4d78f1aadfc1f154d924e1e20636af037cf5af68fe35af8478854345`. The movable table has 80 rows, so indexes 96 and 122 are not movables.

The crate-room rows are controls. Actors 33 and 34, def Roach, are height -215, flags 0x6102, region 1087. Actor 33 is stored `(628,12271)`, seven units from Medium Crate 122. Actor 34 is stored `(651,12244)`, one unit from Medium Crate 96. Def Roach also places actors 25 through 32, 35, and 43 in this same room.

| id | static | stored x, y | height | region | flags |
| --- | --- | --- | --- | --- | --- |
| 94 | Small crate | 429, 12278 | -215 | 1085 | 0x2982 |
| 95 | Small crate | 412, 12264 | -215 | 1085 | 0x2982 |
| 96 | Medium Crate | 650, 12243 | -215 | 1087 | 0x2982 |
| 97 | Medium Crate | 623, 12218 | -215 | 1087 | 0x2982 |
| 112 | Medium Crate | 593, 12350 | -215 | 1087 | 0x2982 |
| 121 | Medium Crate | 564, 12367 | -215 | 1081 | 0x2982 |
| 122 | Medium Crate | 635, 12271 | -215 | 1087 | 0x2982 |

Controls 94, 96, and 122 have no group. The mace items are identity 0x8FCB4F6D, definition 1, `2-Br Mace`, handler 0. Item 17 is stored `(417,12444)`, height -130, region 1092, flags 0x0402. Item 20 is stored `(471,12480)`, height -130, region 1099, flags 0x0402. The JSON has no item objects, so those lists were not framed. Item 5 is the same identity at `(329,16631)`, height -285, region 1171, the bridge room. Push box controls 0 and 1 are stored near `(-442,10758)`, and Box controls 2 through 5 are stored near y 11017. Those six are outside the roach room.

## Dark Halls sliding bookcases

Beat 77. Prima printed 70 (hintbook.txt 2481) names the room with the sliding bookcase. Grade DECODED for three movable rows. Grade UNKNOWN for the slide. L7_DH.MIX sha256 `40b394ebb3cfcfd9f332c4707f2f9e9e7de76d89b82836cec211772ca456b8e7`.

| id | static | stored x, y | height | heading | region | flags | group |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 51 | Bookcase1 | -1177, -570 | 750 | 49152 | 767 | 0x0582 | 12512 |
| 58 | Bookcase1 | 1778, 3579 | 420 | 32768 | 179 | 0x0582 | 13858 and 13886 |
| 59 | Bookcase1 | -2528, 3892 | 85 | 0 | 153 | 0x0582 | 13914 |

Group 12512 is opcode 20, opcode 1 byte 4 = 100, and opcode 9 byte 4 = 14, all on u16 51. Groups 13858 and 13886 are opcode 20, opcode 1, and opcode 16 on u16 58, byte 4 = 100 then 0 on the opcode 1. Group 13914 is opcode 20, opcode 1 byte 4 = 100, and opcode 9 byte 4 = 14 on u16 59. Indexes 51, 58, and 59 each fit a prop, a control, an actor, and a movable. Groups 12512, 13858, 13886, and 13914 were byte-matched. Bookcase controls are a different table. The ones that grant an item are in the next two sections.

## Prism scroll

Beat 79. Prima printed 71 (hintbook.txt 2486) says the Prism spell group is hidden in a bookcase and is right-clicked the way the Museum summon scroll was. Grade DECODED for two bookcase controls that carry the identity. Grade LIKELY for the grant. Grade UNKNOWN for the right-click use.

Identity 0xFC3E18D8, definition 151, `149-Prsmscrl`. Control 971, static Bookcase2, stored `(-2595,3634)`, height 55, region 154. Kind-4 group 12130, predicate 206, is opcode 3 `03010000d8183efc04000000` (dword 0xFC3E18D8, byte 8 = 4), opcode 199, and opcode 16 byte 4 = 1 on u16 971. Index 971 fits only a control.

Control 975, static Bookcase3, stored `(-2331,2393)`, height 55, region 33. Kind-4 group 12272, predicate 206, is the same opcode 3 with byte 8 = 4, opcode 199, and opcode 16 byte 4 = 1 on u16 975. Kind-4 group 12302, predicate 207, repeats the opcode 3 and ends opcode 16 byte 4 = 2 on u16 975. Index 975 fits only a control. Both groups were byte-matched. Movable 59, the sliding Bookcase1 at `(-2528,3892)`, is the nearby sliding row and is not one of these two controls.

## Steel door, amulet, and gauntlets

Beat 83. Prima printed 72 (hintbook.txt 2528) says to keep the crystals showing, put a box by the steel door, and cast Spark, then take Colin's Amulet and the Gauntlets of Might. Grade DECODED for the iron door, the crate controls beside it, and the amulet rows. Grade LIKELY for the amulet dword. Grade UNKNOWN for Spark and for the gauntlets. The gauntlet identity is not on this level.

Control 84, static Iron Door, stored `(-1243,614)`, height 750, flags 0x4482, region 1589. Kind-6 group 7656 is opcode 14, opcode 16, opcode 5, and opcode 9 on u16 84. Index 84 fits a prop and a control. Prop 84 is template Death2, stored `(-1989,1)`, region 1708. The group does not contain slot 6. Slot 6 is `Door_destroyed`. That cstring is written by movable 56, static Door, stored `(-2612,2459)`, region 1542, group 13634, a different door.

113 controls use a crate static name (`crate 20rwc` or `crate 10rwc`). 89 of those 113 have a group. The crate controls within 800 of the iron door are 55 through 70 and 445 through 453, all `crate 20rwc`. Controls 64, 65, 69, and 70 are height 771. The others in that set are height 750. The closest is control 448, stored `(-1243,530)`, 84 units from the door on the same stored x, region 1248. Its groups 8732 and 8750 are opcode 9 and opcode 16 on u16 448. Index 448 fits a prop and a control. Prop 448 is template Candle, stored `(-1003,1840)`. Those groups do not contain u16 84. Control 55's groups are the same shape on u16 55, and index 55 fits every object table. No crate static name contains the word crystal.

Colin's amulet is identity 0xAA4608D9, definition 87, `85-Colims amult`, handler 97. Control 71, static Bookcase1, stored `(-1075,727)`, height 750, region 1587, is about 200 units from the iron door. Kind-4 group 7608 is opcode 3 `03010000d90846aa00000000` (byte 8 = 0) and opcode 16 byte 4 = 1 on u16 71. Index 71 fits a prop, a control, and an actor. Prop 71 is template Death2, stored `(-1861,321)`, region 1695. Item 30 is the same identity, stored `(-2077,1682)`, height 0, flags 0x0002, region 1353, the same point as item 26 `41-Mail shirt`. The JSON has no item objects, so item 30's list was not framed.

Gauntlets of Might are identity 0x2B5E32FC, definition 47, `48-Gau Might`, handler 99. L7 has no placed item of that identity and no opcode 3 of that dword. Item 5, identity 0xF071C0B5, definition 12, `13-Gaunt strike`, handler 107, stored `(-1125,969)`, height 750, region 1576, is a different definition in the same height band as the iron door.

## Bricked window

Beat 84. Prima printed 72 (hintbook.txt 2537) says to drag another crystal box to the bricked-up window at seven o'clock, Spark it, and jump out. Grade DECODED for the Hole control and the crate whose group names that index. Grade UNKNOWN for the drag, the blast, and the jump. The fifteen dome windows are a different static name and are the other puzzle.

Control 86, static Hole, stored `(-2376,2292)`, height 61, flags 0x1002, region 30, has no group. Control 973, static crate 20rwc, stored `(-2328,2326)`, height 55, region 32, is about 80 units from that hole. Kind-9 group 12178 contains opcode 9 byte 4 = 3 on u16 86, then opcode 16 and opcode 9 on u16 973. Index 86 fits a prop and a control. Prop 86 is template Death1, stored `(-1690,-40)`, region 1709. Index 973 fits only a control. The group was byte-matched. Controls 237 through 251 are static Windows for Final, height 785, and their groups were not read as this hole.

## Stopped

All eleven remaining MISSING rows are in the ten sections above. Nothing in this file was started and left unfinished.
