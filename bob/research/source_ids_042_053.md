# Source ids STORY-042 through STORY-053

Read-only pack so later steps can use the original ids without a per-step question. Placements, template and static names, item identity dwords, and arrival selectors were read from the level MIX and from GLOBAL.MIX key 3984507021 this pass. Group command lists for L13 groups already walked from the MIX this session are DECODED. Other group ids come from `scripts/lol2/native_scripts/<AREA>.json` and stay LIKELY until that command is re-walked. Definition name-at-index stays LIKELY: record base 496, stride 91, identity at +24, 30-byte name slots at 20734. No record stores a name pointer.

Stored placement is int16 x, int16 y, int16 height. Arrival heading words are not converted. Opcode 2 is a level change only when the first five bytes are `020100001c`. Byte 5 is unread, so no destination level is named. Opcode 18 was not entered. A group id that exists on both streams is not a unique owner. The stream-0 level-change rows below are the region kind-12 owners. Stories stay with Astra.

## STORY-042

Place L13_RC. Grade LIKELY for the book join of these plasma rows to the pink steps and the bridge. The static cstring is `plasma platform`, not a pink-step cstring.

Side rows, static plasma platform, slot 10, flags 0x1081, event 0, no group:

| id | stored x, y | height | region |
| --- | --- | --- | --- |
| control 55 | -2838, -251 | -60 | 867 |
| control 56 | -2894, -242 | -10 | 867 |
| control 57 | -2913, -322 | -460 | 854 |
| control 58 | -2962, -288 | -410 | 854 |
| control 59 | -2876, -288 | -260 | 874 |
| control 60 | -2922, -269 | -210 | 874 |
| control 61 | -2916, -252 | -110 | 870 |
| control 62 | -2899, -304 | -360 | 878 |
| control 63 | -2933, -280 | -310 | 876 |
| control 64 | -2978, -294 | -510 | 840 |
| control 65 | -2862, -270 | -160 | 870 |
| control 66 | -2953, -345 | -660 | 842 |
| control 67 | -3016, -299 | -710 | 848 |
| control 68 | -3033, -298 | -810 | 850 |
| control 69 | -2931, -333 | -560 | 840 |
| control 70 | -2996, -298 | -610 | 844 |
| control 71 | -3016, -348 | -860 | 850 |
| control 72 | -3076, -290 | -1010 | 275 |
| control 73 | -2981, -350 | -760 | 846 |
| control 74 | -3051, -303 | -910 | 275 |
| control 75 | -3058, -346 | -960 | 275 |

Bridge rows, static plasma platform, height 12, flags 0x1482. Stream 1:

| id | stored x, y | region | groups |
| --- | --- | --- | --- |
| control 90 | -3207, 129 | 319 | 8290, kind 2 group 8316 |
| control 91 | -3850, 130 | 316 | kind 2 group 8336 |
| control 92 | -3720, 130 | 319 | 8356, kind 2 group 8382 |
| control 93 | -3600, 130 | 319 | 8402, kind 2 group 8428 |
| control 94 | -3480, 130 | 319 | 8448, kind 2 group 8474 |
| control 95 | -3340, 130 | 319 | 8494, kind 2 group 8520 |
| control 96 | -3780, 130 | 316 | 8540, kind 2 group 8560 |
| control 97 | -3660, 130 | 319 | 8580, kind 2 group 8606 |
| control 98 | -3540, 130 | 319 | 8626, kind 2 group 8652 |
| control 99 | -3410, 130 | 319 | 8672, kind 2 group 8698 |
| control 100 | -3270, 130 | 319 | 8718, kind 2 group 8744 |

The opcode 9 and opcode 14 u16 at byte +2 is the target index. Kind 6 targets, in control order 90 then 92 through 100: 100, 96, 97, 98, 99, 91, 92, 93, 94, 95. Control 91 has no kind 6 group. Kind 2 targets, in order 90 through 100: 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100. No opcode 1 travel word was in those groups. A visible-time count was not read. These target indexes are LIKELY, from the export raw.

Control 84, static Iris 1, stored (-3897, 134), height 5, region 539, flags 0x0481. Stream 1 groups 8210 and 8250, predicates 206 and 207. Opcode 20 and opcode 9 name index 84.

Control 103, static Web 1, stored (-5482, 155), height 4, region 559. Stream 1 group 8770, predicate 15: opcode 9 index 103 byte 4 = 0x15, opcode 198 index 14 value 1, opcode 21 byte 4 = 31, opcode 18 `1201000062f4780a000085000040000a0000` (signed words -2974, 2680). Group 8812, predicate 16: opcode 21 byte 4 = 60, opcode 18 `120100006bf4780a000085000040000a0000` (signed words -2965, 2680). Opcode 18 was not entered.

Control 101, static Web 1, stored (-3091, 2679), height -1148, region 577, event 0. Region 577 floor -1140, ceiling -925. The group 8770 stored point sits in that region's four vertex words.

Actor 40, definition label HL1, stored (-2431, 2688), height -1180, region 1408, flags 0x6582. Export kind 5 group 10310 includes opcode 18 `12010000e3f5830a00009302004000320000` (signed words -2589, 2691). Later export kind 6 groups run 10370 through 10916 on predicates 206 through 219. That group list is LIKELY. No physical route from control 103 to region 1408 was walked.

No level-change-shaped command is on these objects.

## STORY-043

Place L13_RC. Grade DECODED for the identity dwords below. Name join LIKELY. Opcode 3 callee was not entered, so a grant stays LIKELY.

Prop 325, template Pedestal, stored (-2343, 4538), height -1050, region 915. Kind 4 group 6298 body ends `37f26c8e`, identity 0x8E6CF237, definition 8, name slot `9-Firestorm`, handler 1. Its children opcode 9 index 175. Kind 4 group 6346 body ends `011c5b81`, identity 0x815B1C01, definition 20, name slot `21-Tho fixed`, handler 0. Its children opcode 9 index 174. Both groups contain opcode 2 `020100001800`, which is outside the level-change shape. Predicate on both records is 18.

Prop 174, template Thohan's Sword, same stored x, y as 325, height -990, region 915. Kind 4 group 296 contains opcode 3 `030100009ac2bcf804000000`, identity 0xF8BCC29A, definition 71, name slot `69-Tho enchant`, handler 60, byte +8 = 4.

Prop 175, template Firestorm, stored (-2344, 4535), height -990, region 915. Kind 4 group 392 contains opcode 3 `03010000ff1cfe6404000000`, identity 0x64FE1CFF, definition 21, name slot `22-Darkstorm`, handler 57, byte +8 = 4.

Prop 326, template Dreamstone Pedestal, stored (-2710, 4183), height -1050, region 899. No prop uses template 3 Dreamstone. Groups 6406 and 6502 contain opcode 3 identity 0xCE20AEE3, definition 136, name slot `134-Dreamstone`, handler 0, byte +8 = 1. Group 6610 has that identity in the kind 4 body and no opcode 3 child. Opcode 2 bytes in 6406 are `020100001001` and `020100000f01`. Group 6610 has `020100001800`. Those are outside the level-change shape.

## STORY-044

Place L13_RC. One static Dream Stone Lock exists. It is control 104, stored (-3391, -6670), height 70, region 488, flags 0x0402. Region 488 is arrival selector 0. Kind 4 group 8922 contains opcode 3 identity 0xCE20AEE3, byte +8 = 4. Group 8870 contains opcode 2 `020100001800` and no opcode 3. The lock groups do not contain `020100001c`.

The only L13 level-change command is stream 0 group 706, `020100001c4c`, owned by region 489 kind 12. Byte 5 is 0x4C and was not read as a destination. Whether control 104 reaches region 489 was not traced.

Teleporter statics, opcode 12 and opcode 18 not entered:

| id | stored x, y | height | region | stream 1 group |
| --- | --- | --- | --- | --- |
| control 51 | -6251, 3061 | -1045 | 1195 | 8074, opcode 12 byte 4 = 28, plus opcode 18 |
| control 52 | -4090, 2833 | -1045 | 771 | 8104, opcode 12 byte 4 = 29, plus opcode 18 |
| control 53 | -4955, -1711 | -899 | 987 | 8134, opcode 18 only |
| control 54 | -2347, 3828 | -1049 | 936 | 8152 and 8188 |

Control 105, static Front Door, stored (-3263, -6700), height 0, region 487, event 0.

Arrivals, heading unconverted:

| selector | stored x, y | heading word | region |
| --- | --- | --- | --- |
| 0 | -3344, -6564 | 28089 | 488 |
| 1 | -3260, -6631 | 1 | 487 |
| 2 | -2336, 4192 | 0 | 636 |
| 3 | -2176, -4160 | 0 | 323 |

## STORY-045

Place L12_CM. Item 5 identity 0x715F1D00, definition 54, name slot `55-Obs chain`, handler 0, stored (-59, 14165), height -1170, region 3026, flags 0x1002. No L12 opcode 3 uses that identity. No L12 template or static cstring is tripod. The spark target that would create this row was not found. Grade DECODED for the placed row. Grade UNKNOWN for the tripod.

Ice floe movables 56 through 66, static `ice floe`, event 0, height -275. Ice Ledge controls 95 through 101, event 0. Big ole Ice raft was not a separate scripted row in the named dump. Book Human and the niche jump stay unjoined.

## STORY-046

Place L12_CM. Control 89, static Melt man, stored (3381, 14629), height -1110, region 2734. Stream 1 group 3076 is opcode 9 index 36. Item 36, identity 0x0ACCC5CE, definition 31, name slot `32-Shard`, handler 62, stored (3356, 14610), height -1090, region 2734, flags 0x1412. That is the same region as the Melt man. It is not definition 35 `36-Darkbow`.

No placed row and no opcode 3 on L12, L8, L4, or L14 uses identity 0xD58C34FE (`36-Darkbow`). The blue-bow grant stays UNKNOWN.

Control 74, static Ice Bridge, stored (3684, 19361), height -1292, region 2434. Stream 1 group 2808 is opcode 21 byte 4 = 13, then opcode 2 `020100001c2d`, then opcode 9 indexes 30 and 31. Byte 5 is 0x2D and is unread. Controls 75 and 76 are the same static and region, event 0. Further Ice Bridge controls 78 through 86 are event 0.

Log controls 68 through 73, static Log 1 or Log 2, event 0, stored x about 2883 to 3064, y about 11513 to 11731, heights -904 to -1077, regions 964, 966, and 967.

## STORY-047

Place L12_CM for the logs above, then L8_SJ for the sleeper. Actor 115, definition label LARKHON, stored (7265, -2143), height 0, region 3457, flags 0x6482. Stream 1 group 21504 includes opcode 9 index 115 and opcode 2 `020100001800`. Groups 21682 and 21700 are opcode 9 index 115. The kind 2 count words were already reported and were not converted to seconds.

No second LARKHON placement was in the actor table. The return exit's destination byte stays unread. L8 stream 1 prop 1198, template twsttree2, stored (758, -2046), region 1513, group 11612 is opcode 2 `020100001c2e` and opcode 198 index 13 value 0. That is a unique stream-1 level change. It is not joined to the sleeper.

## STORY-048

The river-to-jungle command was not singled out beyond the level-change rows. Destination bytes stay unread. Grade UNKNOWN for which row is the book jump.

L12 level changes: region 734 kind 12 owns stream 0 group 0 `020100001c88`. Prop 0 also has a kind 6 word 0, and stream 1 group 0 is a different command, so prop 0 is not a unique owner. Control 74 owns `020100001c2d` as in STORY-046.

L4_HJ region kind 12 owners, all stream 0:

| region | group | raw |
| --- | --- | --- |
| 2604 | 4846 | 020100001c45 |
| 2809 | 5208 | 020100001c25 |
| 3186 | 6100 and 6124 | 020100001c28 |
| 3187 | 6130 and 6154 | 020100001c28 |
| 3188 | 6160 and 6184 | 020100001c28 |
| 3189 | 6190 and 6214 | 020100001c28 |
| 3205 | 6292 | 020100001c27 |

L8 region kind 12 owners include regions 908, 2352, 2353, 2360, 3132, 3277, 3569, 3570, and 3573. Prop 0 and prop 30 share group numbers with two of those and are not unique owners. Prop 1198's unique command is under STORY-047.

Arrival selectors, heading unconverted. L12: selector 0 (2784, 18222) region 1948; selector 1 (-347, 5603) region 735; selector 2 (3211, 18903) region 3642. L8: selectors 0 through 9 are present, including selector 1 (-4577, -1168) heading 16384 region 2359. L4 row order is selectors 0, 1, 3, 4, 5, 6, 7, 8, 9. Selector 2 is absent from those nine rows.

## STORY-049

Place L14_HT. Movable 72, static Dreamstone Slot, stored (606, 3464), height 30, region 2490. Stream 1 group 19666 is opcode 3 `03010000e3ae20ce04000000`, identity 0xCE20AEE3, definition 136, name slot `134-Dreamstone`, byte +8 = 4. Group 19620 is opcode 9 `090400001b00`, u16 at byte +2 = 0, byte 4 = 0x1B, and opcode 2 `020100001800`, outside the level-change shape. The opcode 9 target 0 was not joined to a placement.

Movables 92 and 93, static Main Doors, stored (2447, 3027) and (2376, 3027), height 0, region 786, event 0.

L14 arrivals: selector 0 (2576, 3181) heading 60694 region 796; selector 1 (2411, 2413) heading 1 region 864; selector 2 (789, -10774) heading 0 region 2282; selector 3 (-1336, -11466) heading 0 region 4176.

The level changes on L14 are region 863 and region 4176, both `020100001c68`, plus prop 170, template Side Deco, stream 1 group 9210 `020100001c30`, predicate 50. Byte 5 stays unread. Which of these is the temple door's exit is UNKNOWN. The door static and the slot are different objects.

## STORY-050

Place L14_HT. Two template rows are `Caretaker's corpse`. Prop 187, stored (2403, 3617), height -75, region 3244, stream 1 group 10738, opcode 9 u16 values 193, 192, and 187. Prop 274, stored (2493, 2856), height 0, region 951, stream 1 group 12774, opcode 9 u16 value 274. Which corpse is the priest was not joined. Grade UNKNOWN for that join. The rows themselves are DECODED placements.

Pew controls 128 through 135, event 0, stored x 2938 to 3139, y 4137 to 4407.

Prop 200, template Bowls, stored (1504, 6217), height 122, region 2926. Stream 1 group 11562 opcode 3 identity 0x0A02A378, definition 125, name slot `123-Pois paint`. Prop 201, template Bowls, stored (1663, 6218), height 122, region 2918. Group 11620 opcode 3 identity 0xBFDDCCA3, definition 109, name slot `107-Aloe`, handler 9. The book words west and east are not in the name table. No placed item on these levels has a name slot containing poison. Item 68 is a placed `107-Aloe` at (2950, 4609), height 10, region 140, flags 0x0002.

## STORY-051

Same bowls as STORY-050. Prop 200's opcode 3 is the `123-Pois paint` identity. Prop 201's opcode 3 is the `107-Aloe` identity. The spark that removes a corpse was not a separate opcode on those two bowl groups. Props 187 and 274 remain the two corpse rows. Grade LIKELY for the identity match. Grade UNKNOWN for which corpse the spark addresses.

## STORY-052

Place L14_HT. Template Post props 240 through 251, event 0, stored y from -6082 to -6810. None has a group. No cry-shard item sits on those coordinates.

Placed identity 0xD0421BDE, definition 105, name slot `103-Cry shard`, handler 0:

| item | stored x, y | height | region | flags | copies at that point |
| --- | --- | --- | --- | --- | --- |
| 4 | 3211, 2681 | -96 | 4073 | 0x0002 | one, beside item 1 Dreamstone |
| 7-11 | 1226, 3605 | 0 | 1025 | 0x1002 | five records |
| 12-16 | 1230, 3307 | 0 | 1032 | 0x1002 | five records |
| 67 | 2691, 3887 | -70 | 379 | 0x0082 | one |

The wooden-post join stays UNKNOWN. The catalog cstring is `103-Cry shard`. It was not renamed to the book's green shard.

Item 1, identity 0xCE20AEE3, definition 136, stored (3264, 2664), height -96, region 4073, flags 0x0002, is a placed Dreamstone beside item 4.

## STORY-053

The jungle-tree stair owner was not joined. L8 template `unlit torch` prop 1338, stored (-1121, 2146), height 100, region 675, has stream 1 group 11638: opcode 20, opcode 16, opcode 207, opcode 9, opcode 5, opcode 6. Other torch and hang rows were not given a stair group. L4 has no template cstring `stair`. L8 prop 1198's level change is the unique stream-1 exit listed under STORY-047, byte 5 0x2E unread.

The shard taken back to the temple is the same identity as STORY-052 if it is `103-Cry shard`. No command was found that moves item 67, or the stacked rows, back to movable 72. That return command stays UNKNOWN.
