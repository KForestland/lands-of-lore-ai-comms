# H13 Blue-ball room, the bricked window, and the light rumor

Beat 84. `L7_DH`, same archive as H10. Two different window sets are in the file. The crate that names the hole is not one of the fifteen `Windows for Final` controls.

OPTIONAL for finishing. BRADY 7033-7037: completing the sphere is the knife and the bridge. The Halls exit is how the book leaves this level after entering it. BRADY 3343-3346 still says the Halls are not required.

## What the books say

HINTBOOK 2534-2550: the round room spawns ghosts. The bricked window is at about seven o'clock, where the automap's brown lines are open. Drag the crystal box there, Spark it, and jump through the hole. A rumor says enough light destroys the blue ball and the ghosts. That takes several boxes, and you still blow one window and jump.

BRADY 3469-3491: bricked windows ring the circular room. One explosive crate at the sixth window to the left opens an exit back to the Huline Jungle. Seven windows destroy the Spectral Orb and give experience. BRADY 7359-7365 is the same sixth window, and the orb starts making Shades when you enter. The hintbook's blue ball and Brady's Spectral Orb are two printed names for that center object. No cstring `Spectral`, `Orb`, `Ball`, or `blue ball` is in `L7_DH.MIX`.

## The hole and the one crate that names it

Control 86, static slot 39 `Hole`, native (−2376, 2292), height 61, region 30. No events. Region 30 is the tiny quad on that point, floor 61, ceiling 90, neighbors none, 31, none, 104. Its only group is 0, file 4860407: opcode 2 `020239000600` (arm 6, not arm 0x1C) and opcode 198 `c60000000a00` (byte 4 = 10, value 0). Arm 6 was not entered. This is not the level-change shape.

Control 973, static `crate 20rwc`, native (−2328, 2326), height 55, region 32, about 60 units from the hole. Region 32 floor 55 sits against region 31. Same crate shape as H12, plus extra commands in the hit group.

- Kind 3 value 1, no predicate, group 12160, file 4872567: opcode 9 byte 4 = 0x11 and opcode 16 byte 4 = 1, both on u16 973.
- Kind 9 value 17, predicate `0005000001`, group 12178, file 4872585, MIX match, six commands: opcode 204 `cc906800f9010300`, opcode 197 `c5901e000000` on region 30, opcode 9 byte 4 = 3 on u16 86, opcode 15 on u16 973, opcode 16 byte 4 = 2, opcode 9 byte 4 = 2.

Left kind 5 was not entered. Opcodes 197, 204, 15, and 9 were not entered. The hit group does name the hole control and the hole's region. A jump command is not in the group. There is one `Hole` control in the level.

## The seven exit regions

Stream 0 groups 856, 874, 892, 910, 928, 946, and 964, files 4949896 through 4950004, are seven copies of opcode 199 `c70000000301` (byte 4 = 3, value 1) and opcode 2 `020100001cc4`. Byte 5 stays unnamed. The owners are regions 1394, 1408, 1409, 1410, 1411, 1412, and 1413, kind 12 value 0. Their floors are 700 and their centers run from (−3748, −80) to (−2786, −356). That is the book's count of seven, on a different floor from the hole. Nothing in those groups names control 86.

## The fifteen high windows

Controls 237-251, static slot 35 `Windows for Final`, height 785, are the other set. Each kind-6 group includes `cf0000000501`. Byte 4 is 5. Slot 5 at the local table is `Blowout_happens`. Opcode 207 was not re-entered. These fifteen are the domed-hall counter from the earlier Dark Halls note, not control 86.

Prop 242, template 25, native (−2155, 207), height 370, region 1690, is the object whose kind-2 groups 2022 and 2040 are gated by predicate `0503050006`: operator 5, left kind 3, index 5, right kind 0, last byte 6. Left kind 3 reads a local, so this test reads `Blowout_happens` against 6. Operator 5 was not entered. Group 2022 is opcode 9 byte 4 = 0x15 on u16 838 and opcode 201 `c90000000805`. Group 2040 is opcode 17 `1103f2000100`. Both match the MIX. The predicate table also contains `0403050006`, and no event cites it. This prop was not joined to the blue ball.

## Opens

- Opcode 197 and opcode 9 on the hole. The jump, and whether region 30's arm 6 is an exit.
- The destination of byte 5 = 0xc4 on the seven regions.
- Operator 5 against local 5. Brady's seven and the compare-to-6 were not merged.
- A placed mesh for the blue ball or the Spectral Orb.
- No longplay frame was opened.

## Grades

HINTBOOK 2534-2550 for the seven-o'clock window, the jump, and the light rumor. BRADY 3469-3491 and 7359-7365 for the sixth window, the seven-window orb, and the jungle exit. DECODED for control 86, control 973, group 12178, the seven arm-0x1C regions, and the fifteen window commands. FRAME open.
