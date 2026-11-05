# H10 Dark Halls secret bookshelves 51, 58, 59

Beat 77. `L7_DH.MIX` sha256 `40b394ebb3cfcfd9f332c4707f2f9e9e7de76d89b82836cec211772ca456b8e7`. JSON `L7_DH.json`. Static names are the 47 printable 30-byte records that start at file 5052795 (`Bookcase1`). The table-start pointer was not read from a header. Slot 0 is `Bookcase1`.

No owner report is newer than `TRIAGE_20261104.md`.

OPTIONAL loot. HINTBOOK 2480-2487 treats the Stones, the Healing Scroll, and the Prism scroll as worth taking. BRADY 3343-3346 says the Halls themselves are not required to finish.

## The three rows

All three are movables, static slot 0 `Bookcase1`, flags 0x0582. Byte 34 is 2, 4, and 2. The hinge path's byte 34 = 6 does not match these rows, so a door-hinge swing is not this placement. Groups match the MIX.

| movable | native x, y | height | heading | region | byte 34 | byte 36 | use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 51 | -1177, -570 | 750 | 49152 | 767 | 2 | 100 | kind 4 value 0, no predicate, group 12512 |
| 58 | 1778, 3579 | 420 | 32768 | 179 | 4 | 60 | kind 4 value 0, two predicates |
| 59 | -2528, 3892 | 85 | 0 | 153 | 2 | 116 | kind 4 value 0, no predicate, group 13914 |

Godot positions are (x, −y): 51 (‑1177, 570), 58 (1778, −3579), 59 (−2528, −3892).

Group 12512, file 4872919, on 51: opcode 20 `14203300bd0280000a14`, opcode 1 `012033006400` (byte 4 = 100), opcode 9 `092033000e00` (byte 4 = 0x0e). All three name u16 51.

Group 13914, file 4874321, on 59: the same three opcodes, targets u16 59, opcode 1 byte 4 = 100, opcode 9 byte 4 = 0x0e.

Movable 58, file 4874265 and 4874293:

- Predicate `0005000000` (operator 0, left kind 5, index 0, right kind 0, last byte 0). Group 13858: opcode 20, opcode 1 byte 4 = 100, opcode 16 byte 4 = 1.
- Predicate `0005000001` (same shape, last byte 1). Group 13886: opcode 20, opcode 1 byte 4 = 0, opcode 16 byte 4 = 0.

Left kind 5 was not entered. Opcodes 1, 9, 16, and 20 were not entered. 51 and 59 have no second use and no opcode 16. Only 58 writes a state byte.

## What sits next to them

The groups grant nothing. No opcode 3 on 51, 58, or 59. No opcode 18.

Region 767 (movable 51) is the small quad centered (−1141, −572), floor 750, ceiling 828, neighbors 768, 764, 766, 761. Those neighbors hold no control except a `Lg Web` on 764. The group does not name another object.

Region 179 (movable 58) is centered (1806, 3579), floor 420, ceiling 525, neighbors none, 180, none, 182. Region 180 continues to 1509. Within 400: crate control 253 and `DoorFrame0` control 252. No item grant within 500.

Region 153 (movable 59) is the long quad centered (−2528, 3762), floor 85, ceiling 163. The movable sits at the north end, y 3892. Neighbor 152 touches only 153. Neighbor 154, center (−2645, 3762), holds the bookcase controls, including control 971 (`Bookcase2` at (−2595, 3634), the Prism grant) and control 968 (`Bookcase2` at (−2809, 3891), identity `0x7B8015C7`). Those grants are H11's controls. They are not commands of movable 59.

Beds are elsewhere (clusters near (−1900, 1900) height 310, and near (−200, 0) height 640). The Stones room in HINTBOOK 2480-2481 was not joined to movable 51, 58, or 59. No Healing Scroll opcode 3 sits within 500 of these three.

## Which sentence is which shelf

BRADY 7006-7014, two clicks: the bookcase to the northeast at the end of the first long hall opens a secret door, and a bookcase at the western end of the southern hallway reveals a passageway. HINTBOOK 2433 says to click every bookshelf. HINTBOOK 2526-2528 adds one more sliding bookcase before the round blue-ball room.

Three movables, two Brady clicks, one later hintbook slide. Placing 58 (the northeastern point) on Brady's first click, 51 (the southern point) on the southern hallway, and 59 (the western-north point, beside the Prism cases) on the last slide is GUESS. The bytes do not name a door index other than the movable itself.

## Opens

- Opcode 1 byte 4 = 100 or 0 on these rows. Motion is not shown. Byte 34 is not the hinge value 6.
- Left kind 5 on movable 58.
- Opcode 9 byte 4 = 0x0e on 51 and 59.
- Which shelf is Brady's secret door, which is the southern passage, and which is the blue-ball hall.
- Where the Healing Scroll and the bed-room Stones are placed.
- No longplay frame was opened.

## Grades

HINTBOOK 2433, 2480-2481, 2526-2528 and BRADY 7006-7014 for the clicks and the loot those rooms are said to hold. DECODED for the three movables, the four groups, and the neighbor regions. GUESS for matching each movable to a printed sentence. FRAME open.
