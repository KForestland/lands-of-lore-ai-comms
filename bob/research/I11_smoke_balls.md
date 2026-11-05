# I11 four smoke balls

Place L16_CA. No frame was opened. No Godot was run. Template 61 is the cstring `Ball O Smoke`. Template 58 is `Pyramid`. Template 75 is `Silverleaf Pyramid`. Static 44 is `FireWall Door`. Name-at-index stays LIKELY. Opcode 1, opcode 9, opcode 15, and opcode 18 were not entered. Bit 0x0004 is clear on every ball opcode 18, so none of them is the direct-relocation form. Flag 0x0812 was not read. Opcode 2 arms 0x0B and 0x0C are I30.

Hintbook lines 4835–4841: after the three northwest objects, a fireball bursts from the glass pyramid and travels until it hits a tower door, which opens. Grade HINTBOOK. Lines 4891–4894: a plant bursts from the glass pyramid and a fireball wafts to the doors, which open. Grade HINTBOOK. Lines 4948–4950: the southwest pyramid shatters and a fireball floats to the tower and opens the door. Grade HINTBOOK. Lines 4917–4920: after the oil and the bow, retreat east and the path to the tower opens. That paragraph does not say fireball. Grade HINTBOOK. Each tower's opening is REQUIRED. The stored path is the same shape on all four. Brady was not re-read for this path.

## The four paths

Each ball has one opcode 18 on itself. Kind byte 3, height word 0, flags 0x0812. The words are the stored fields. They sit on a FireWall door row. The ball's own place is the other end.

| prop | place, Godot y flipped | region | words | doors on that row, no events |
| --- | --- | --- | --- | --- |
| 600 | (−9896, 899), Godot (−9896, −899), height 115 | 5484 | (−9877, 4536, 0) | movables 86 (−9870, 4533) region 3234, 87 (−9820, 4533) region 3224, 88 (−9919, 4533) region 3233 |
| 601 | (−9797, −13070), Godot (−9797, 13070), height 15 | 6960 | (−9808, −14344, 0) | movables 89 (−9759, −14335) region 3432, 90 (−9859, −14335) region 3433, 91 (−9809, −14335) region 3434 |
| 602 | (2289, 648), Godot (2289, −648), height 18 | 6098 | (2290, 2951, 0) | movables 92 (2242, 2947) region 3017, 93 (2342, 2947) region 3016, 94 (2292, 2947) region 3018 |
| 603 | (429, −12857), Godot (429, 12857), height 22 | 6775 | (1703, −12835, 0) | movables 95 (1704, −12841), 96 (1704, −12891), 97 (1704, −12791), all region 2860 |

600 moves north about 3637. 601 moves south about 1274. 602 moves north about 2303, the greenhouse x. 603 moves east about 1274, the oil y. Those deltas are the stored words minus the placement. They are not a proven speed.

## Who names the ball

| pyramid | place | record | what it stores on the ball |
| --- | --- | --- | --- |
| 641, LIKELY Pyramid | (−9897, 841), region 5484, the ball's region | kind 3, group 41010, value 8 | opcode 9 byte 4 = 3 and byte 4 = 21 |
| 604, LIKELY Pyramid | (−9793, −12994), region 6943 | kind 3, group 37944, value 8 | the same two opcode 9s on 601 |
| 605, LIKELY Silverleaf Pyramid | (2287, 599), region 6098, the ball's region | kind 6, group 38056, value 2, predicate entry `0005000002` | the same two opcode 9s on 602 |
| 606, LIKELY Pyramid | (370, −12854), region 6775, the ball's region | kind 6, group 38148, value 2, predicate entry `0005000000` | the same two opcode 9s on 603 |

Opcode 9 was not entered. The two predicate entries are operator 0 and left type 5. Left type 5 was not entered. Prop 605's left type 4 predicates are I13. These two are not those.

## The command that names the door indexes

The second record on each ball holds one opcode 2, one opcode 9, one opcode 15, three opcode 1s, and one opcode 9 on the ball.

| ball | record | opcode 2 | opcode 9 u16, byte 4 = 3 | opcode 15 u16 | opcode 1 u16s, byte 4 = 100 |
| --- | --- | --- | --- | --- | --- |
| 600 | kind 6, group 37640, value 6 | `020100000b05` | 6 | 137 | 88, 86, 87 |
| 601 | kind 6, group 37708, value 6 | `020100000c05` | 5 | 138 | 90, 91, 89 |
| 602 | kind 10, group 37776, value 0 | `020100000c05` | 7 | 136 | 92, 94, 93 |
| 603 | kind 10, group 37844, value 0 | `020100000b05` | 8 | 135 | 97, 95, 96 |

Kind 10 is I12. The opcode 1 indexes are the FireWall door indexes in the table above, and each index also fits a prop and a control. Index 88 also fits the Block trap. Index 89 fits the Fire trap. Index 90 fits the Ice trap. Index 92 fits the Dracoid and the Tapestry. The command does not pick the table. The opcode 18 words pick the FireWall door row, not those other rows.

Opcode 15's u16 likewise fits three tables. The prop with that index is a Light Source on the same door band: 137 at (−9871, 4505), 138 at (−9806, −14314), 136 at (2280, 2916), 135 at (1679, −12842). The movable with that index is a different FireWall door, at x −838. The command does not pick the table.

The opcode 9 u16s 5, 6, 7, and 8 each fit an actor, a prop, a control, and a movable. None of those rows is the door.

## Still open

Opcode 9 as the pyramid's release. Opcode 1 as the open. Which table the u16 names. Flag 0x0812 and its speed. Arms 0x0B and 0x0C. Kind 10. Left type 5. The southeast book's silence on a fireball. No frame.
