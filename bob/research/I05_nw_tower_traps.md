# I05 NW tower traps

Place L16_CA. No frame was opened. No Godot was run. Names are the I03 tables. Name-at-index stays LIKELY. Opcode 1, opcode 2 arm 0x0b, opcode 5, opcode 7, opcode 9, opcode 15, opcode 16, opcode 17, opcode 18, and opcode 20 were not entered.

Hintbook lines 4824–4841: a white ball, a fireball, and a spinning brick hover over moving walls. The blue bow destroys the fireball. A third-level imp, or a spark altered by a pyrapod, destroys the ice ball. Hitting the brick destroys it. A door opens and the pyramid's fireball opens the tower door. Grade HINTBOOK. Brady printed 233: an edged weapon destroys the solid square, Mist of Doom destroys the ball of flame, and a fire spell destroys the frozen vapor. Grade BRADY. The two books do not name the same weapon for the same object. Both require destroying the three objects. The weapon stays the book's sentence.

## The three hovering rows

| prop | template | native | Godot | height | region | floor, ceiling |
| --- | --- | --- | --- | --- | --- | --- |
| 88 | Block trap | (−10576, 750) | (−10576, −750) | 100 | 3851 | 100, 500 |
| 89 | Fire trap | (−10442, 1838) | (−10442, −1838) | 125 | 4159 | 100, 500 |
| 90 | Ice trap | (−8868, 3286) | (−8868, −3286) | 125 | 5833 | 100, 500 |

Flags are 0x4482. Each kind 9 group is opcode 9 on itself, byte 4 = 8 and byte 4 = 18, then opcode 16. No item identity is in those bytes, so no command stores the blue bow, the imp, or a weapon. Each later group names prop 91 with opcode 17 byte 4 = 1 and opcode 9 byte 4 = 21.

Prop 91, LIKELY Light Source, is (−9902, 1148), height 0, region 5613, floor 0, ceiling 500. Its group 2424 applies the accepted opcode 196 formula (byte 6 is 0) to six regions in the strip x −10000 to −9800, y 1064 to 1600. The floor target is 100 and the speed is 5. Five of those regions are floor 0, so the delta is 100. Region 5589 is already floor 200, so the delta is −100. U16 91 also fits a control and a movable. The prop is the one at this coordinate.

## Walls, pyramid, doors

Thirty-five movables, LIKELY Battlement piece, sit in this band, height 0, flags 0x2182, and every one of them has no events. Their regions are floor 0, ceiling 500. Prop 622, LIKELY Altar, at (−8922, −166), region 9660, is the only owner of stream 1 group 39468. That group is 32 opcode 196 commands on those battlement regions. The signed word at +4 is −100, byte 6 is 12, and byte 7 is 15. The accepted floor formula needs byte 6 = 0, so it does not apply. What the walls do stays open.

Prop 641, LIKELY Pyramid, and prop 600, LIKELY Ball O Smoke, share region 5484, floor 100, ceiling 500, at (−9897, 841) and (−9896, 899). The pyramid's group 41010 is opcode 9 on prop 600, byte 4 = 3 and byte 4 = 21. Group 40946 is opcode 20 on prop 391, the Shape 3 at (−9859, 3450), height 198, region 4313. Prop 600 group 37622 is opcode 18 on itself, words (−9877, 4536, 0), flags 0x0812. Bit 0x0004 is clear. The words sit on the three FireWall doors, movables 86, 87, and 88, at y 4533, x −9870, −9820, and −9919. Those doors have no events.

The same group also has opcode 2 raw `020100000b05` and opcode 1 byte 4 = 100 on u16 88, 86, and 87. Those three indexes each fit a prop, a control, and a movable. The movable fit is the three doors. The prop fit is the Block trap and two Light Sources. The command does not pick the table. Arm 0x0b is I30.

## Still open

Which weapon the original accepts. Opcode 17 on the light. The battlement motion, because byte 6 is 12. The table of u16 86, 87, and 88. No frame.
