# I02 NE tower interior

Past the FireWall doors, native x 1900–2700 and y 2940–5200 holds nine objects. The three doors are movables 92–94. The interior six are below. Static names are the 30-byte run at L16 file 19098082, 87 names, name at byte 0. The join is LIKELY. No frame was opened.

| object | native | Godot | height | region | slot | name | events |
| --- | --- | --- | --- | --- | --- | --- | --- |
| control 165 | (2286, 3141) | (2286, −3141) | 100 | 3107, floor 100, ceiling 800 | 25 | Gate | none |
| control 166 | (2286, 3131) | (2286, −3131) | 100 | 3107 | 25 | Gate | none |
| control 117 | (2279, 3227) | (2279, −3227) | 100 | 3133, floor 100, ceiling 800 | 50 | Key Object | kind 10, stream 1 group 43168, value 0 |

Group 43168 is opcode 9 on control 119, byte 4 = 3, raw `091077000300`, then opcode 9 on control 117, byte 4 = 2, raw `091075000200`. Opcode 9 was not entered. Control 119 is the same Key Object slot, stored (15948, −4005), height 100, region 7655. That is the far pylon band, not this street.

The same pair repeats at the other three doorways. Gates 167 and 168 with key 116 sit by the northwest doors. Gates 169 and 170 with key 115, and gates 171 with key 118, sit on the south doorways. Keys 120, 121, and 122 are the other three far-band Key Objects, at x 10666, 15892, and 10605.

## Stairs, box, disk

`heaven stair` is static index 20. No control, movable, or prop has static byte 20. `Teleporter` is index 7 and `Telepad` is index 27. Neither byte appears on the nine objects in this strip. `Push/Pull object` is index 53. It is also absent here. The earlier pack puts the Push/Pull controls at the STORY-074 force field, not in this tower.

There is no `disk` cstring and no `Box` name in that 87-name run. A four-byte `Box` at file 14424350 sits inside binary, not a name record.

Hintbook lines 4842–4847, after the moving-wall room (white ball, fireball, spinning brick), say go up the stairs, push the box through the shimmering disk, and the box is transported. That paragraph is the northwest room's exit. Grade HINTBOOK. It was not matched to a placed object in the northeast interior. What the push does stays unknown. The only stored command here is the two opcode 9 bytes, and they do not include opcode 18.

Props 161, 163, and 167 are slot 70, LIKELY `Blood plate`, higher up the same avenue. Each has one kind-1 record, which is not an object-group kind, so the body was not read as commands.

## Still open

Opcode 9. Whether control 117's link to control 119 is the disk. The book's stairs. No frame.
