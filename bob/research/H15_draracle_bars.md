# H15 Third Draracle visit and the hall bars

Beat 18. `L3_DH.MIX` sha256 `bd85c12d4a2cff0cc200309e72a7771745ce5c78f1a83da4d60cba81d831ccac`. Static slot 55 at the 30-byte run whose slot 55 is `Bar` (file 5944852) and slot 58 is `Iron Door`. The table-start pointer was not read from a header. Locals: slot 0 `Entrance_door` at the `First_bars` alignment, slot 17 `First_bars` file 5901351, slot 19 `Draracle_return` file 5901433.

## What the book says

HINTBOOK 2074-2078: see the Draracle twice, because each visit tells more. A third visit annoys him. The sentence does not say he bars a hall. HINTBOOK 2092 says the museum entrance is blocked after you enter the museum. That sentence was not joined to these four bars.

The annoyance is OPTIONAL. Two visits are the book's useful step.

## The four bars

Movables, static slot 55 `Bar`, flags 0x0181, byte 34 = 0, no events. Byte 34 is not the hinge value 6.

| movable | native x, y | height | region |
| --- | --- | --- | --- |
| 71 | -3789, 1122 | -120 | 1151 |
| 72 | -3789, 1100 | -120 | 1157 |
| 73 | -3789, 1076 | -120 | 1163 |
| 74 | -3789, 1052 | -120 | 1169 |

They share x. The y values step by 22, then 24, then 24.

## The group that names them

Region 1174, kind 12 value 0, event 2, predicate index 45 `0003110000`. That is operator 0, left kind 3, index 17, right kind 0, last byte 0. Left kind 3 reads a local, so this is `First_bars` == 0. Group 1364, file 5883564, MIX match. The commands that name the bars are opcode 1 byte 4 = 100 on u16 71, 72, 73, and 74, then opcode 198 `c60000001101` storing 1 at local 17. The same group ends with opcode 1 byte 4 = 0 on u16 77.

Movable 77, static slot 58 `Iron Door`, native (−4060, 844), height 0, flags 0x0182, region 1182, byte 34 = 6, no events of its own.

Opcode 1 was not entered, so percent 100 is the command byte, not a proven slide. The group does not test `Draracle_return`.

## The visit counter is a different local

`Draracle_return` is stepped 0, then 1, then 2, then 3:

| when | group | file | write |
| --- | --- | --- | --- |
| region 1220, predicate `0003130000` (local 19 == 0) | 1486 | 5883686 | opcode 198 sets local 19 to 1 |
| region 1220, predicate `0003130001` (local 19 == 1) | 1522 | 5883722 | opcode 198 sets local 19 to 2 |
| control 79 kind 4 value 0, predicate `0003130002` (local 19 == 2) | 6976 | 5841358 | opcode 20 on u16 79, opcode 198 sets local 19 to 3 |

Group 6976 is the third step, and it does not name movables 71-74. No predicate in the table compares local 19 with 3. The bar drop and the third-visit write are separate.

## Opens

- Opcode 1 on the bars. Byte 34 is 0.
- Whether region 1174 is reached only after visit 3. Its predicate is `First_bars` == 0.
- Control 79's placement was not re-copied this pass. Its group is 6976.
- The rest of group 1364 (opcode 206, opcode 9, opcode 6) was not decoded.
- No longplay frame was opened.

## Grades

HINTBOOK 2074-2078 for two useful visits and a third that annoys him. DECODED for the four bar rows, group 1364, local 17, and the three writes of local 19. The join "third visit bars the hall" stays open. FRAME open.
