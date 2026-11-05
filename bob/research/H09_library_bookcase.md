# H09 Library bookcase into the Dark Halls

Beat 50. Monastery storeroom on `L4_HJ`. `L4_HJ.MIX` sha256 `517afe6d59a4a06212bf4aea7eb42dfbb07826a4677fb77a4032674e64657e8f`. JSON `L4_HJ.json` in `lol2_r14`. Static names are 30-byte cstrings from file 13284825 (`planks`, slot 0) through slot 97. The table-start pointer was not read from a header. Geometry entry file 12409578, region records 44 bytes, floor and ceiling signed words 10 and 11.

No owner report is newer than `TRIAGE_20261104.md`.

OPTIONAL for finishing the game. BRADY 3343-3346: the Halls are reached from inside the Monastery, and it is not absolutely necessary to enter. The same pages say the rooms hold useful items.

## What the books say the player does

HINTBOOK 2398-2404: after Julian's office, take the door left of the library, talk to the person there, enter the storage area, stack boxes next to the bookshelf, climb, and attack the bookshelf with a spell or a weapon. That breaches the Dark Halls. Come back to this spot after the Halls and continue the jungle.

BRADY 3320-3323: Julian is the door ahead, Dawn is the archway left, and the extreme-left door is a room of boxes. The first visit may meet the explorer Rixx.

BRADY 3351-3372: the way in is a room other than Julian's or Dawn's. The door on the left of the entrance, then the door straight ahead, is the storeroom. Move and stack the boxes to reach the hole. The door to the right inside the storeroom leads back to the Monastery.

## Bookcase

Control 79, static slot 71 `Bookcase2` (file 13286955), native (5315, -2194), height 0, flags 0x4482, region 3200. Godot (5315, 2194). Four events, all kind 9, no predicate. The event link at file 12767124 matches the MIX.

| value | group | file | commands |
| --- | --- | --- | --- |
| 17 | 18766 | 12747070 | opcode 15 on u16 246, opcode 5 on 79 byte 4 = 4, opcode 9 on 79 byte 4 = 0x12, opcode 197 `c5908b0c0000` on region 3211 |
| 14 | 18798 | 12747102 | opcode 5 on 79, byte 4 = 1 |
| 14 | 18810 | 12747114 | opcode 5 on 79, byte 4 = 2 |
| 14 | 18822 | 12747126 | opcode 5 on 79 byte 4 = 3, opcode 9 on 79 byte 4 = 0x12, opcode 197 on region 3211 |

Groups 18766, 18798, 18810, and 18822 match the MIX. Opcodes 5, 9, 15, and 197 were not entered. Kind 9 admission was not re-entered. None of the four groups contains `020100001c`.

Region 3200 center (5373, -2182), floor 0, ceiling 130, neighbors 3199, 3197, 3211, 3190. The bookcase sits on the west edge of that quad, against region 3211.

## Lockout and the level change

Control 78, static slot 75 `Lockout door`, native (5299, -2197), height 76, flags 0x1081, region 3211. No events.

Region 3211 center (5299, -2197), floor 75, ceiling 125, neighbors 3205, none, 3200, none. It is the thin quad between the bookcase region and region 3205. The bookcase groups name this region with opcode 197. What that command does stays open.

Region 3205 center (5255, -2206), floor 0, ceiling 130, neighbors 3207, none, 3211, 3204. Kind 12 value 0, group 6292, file 13029270, MIX match: opcode 9 byte 4 = 3 on u16 78, then opcode 2 `020100001c27`. Byte 5 stays unnamed. Index 78 also fits other tables. Control 78 is the lockout door on region 3211. Movable 78 is the village right gate at a different place.

Control 140, static slot 37 `Door Frame`, native (5181, -2232), region 3226, no events.

No L4 opcode 12 uses room index 7 (`mlib_`). The breach command in this pocket is the opcode 2 on region 3205, not a monastery-room load.

## Crates

44 controls in the pocket (native x 5200-5800, y -2500 to -1900) use static slots 31 `40 x 40 crate`, 32 `20 x 20 crate`, or 33 `10 x 10 crate`. Every one of them has an empty event list. Heights already differ. One column near (5472, -2000), region 3201: control 176 `40 x 40 crate` height 0, control 160 `20 x 20 crate` height 40, control 141 `10 x 10 crate` height 60. No command in the bookcase groups names a crate index. A player stack is the book's action. A script that moves a crate was not found.

## Opens

- Whether kind 9 on control 79 is the spell or weapon strike. The groups do not contain the level-change command.
- Opcode 197 on region 3211, opcode 9 byte 4 = 0x12, and opcode 5 bytes 1, 2, 3, and 4.
- Opcode 2 byte 5 = 0x27. The destination level is not named from that byte.
- No L4 actor stands in this pocket, so the hintbook person and Brady's Rixx are not a placed row here.
- No longplay frame was opened.

## Grades

HINTBOOK 2398-2404 and BRADY 3320-3323, 3351-3372, 3343-3346 for the route, the stack, the strike, and optional entry. DECODED for control 79, control 78, the 44 crate rows, regions 3200/3205/3211, and the quoted groups. FRAME open.
