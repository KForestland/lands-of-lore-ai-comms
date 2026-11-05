# J01 L1 crate wall and the unmoved boxes

Owner 17-03-39. F10 (532, −12371) is native (532, 12371). That point is inside region 1081 and on its edge 3. No Godot was run. No longplay frame was opened. `L1_DC.MIX` sha256 prefix `6384ec4d`.

## The wall

Region 1081 is one quad, floor −215, ceiling −43, flags `0x0200`. Neighbors are none, 1087, 1082, and 1102. Edge 3 names region 1102. Region 1102 is floor −130, ceiling −62, flags `0x0A10`. Bit `0x10` is set. The two regions do not share a vertex pair. The geometric span builder defers both directions as a special connector, so it emits no boundary face and no interior face on that edge.

The wall review does draw the riser. Record 1485, region 1081, descriptor 304, addressing 16. Godot quad: (474, −130, −12338), (586, −130, −12403), (586, −215, −12403), (474, −215, −12338). Native x,y is (474, 12338) to (586, 12403), heights −215 up to −130. That is the 85-unit step to the next floor. The playtest point lies on that footprint.

The same edge also draws record 1484, descriptor 134, addressing 8, from height −62 to −43 (the band above region 1102's ceiling). Side closers 1486 and 1487 are descriptor 304, addressing 16. Material files are `wall_review/material_304_variant_0.png` and `material_134_variant_0.png`.

`original_walk_review.gd` builds collision from floor faces plus the geometric shell only. `textured_cave_review.gd` draws `wall_review/walls.json` and leaves that collision in place. Record 1485 is drawn and is not in the collision set. Grade DECODED for the records, the deferral, and those two scripts. The owner's "clipped through the wall" is this riser.

The short lip that does collide is record 1488, descriptor 85, edge 0, neighbor none, about (586, 12403) to (597, 12383). Record 1489, also descriptor 85, is the interior span on edge 2 toward region 1082 (floor and ceiling both 425). Those are not the seam the point sits on.

## The boxes

H16 stands. Seven crate controls, all height −215, none with an event. No opcode 18 targets them. `static_collision_L1_DC.json` gives each a solid box, `scripted` false:

| control | template | native | box |
| --- | --- | --- | --- |
| 94 | 25 Small crate | (429, 12278) region 1085 | 10×10×10 |
| 95 | 25 Small crate | (412, 12264) region 1085 | 10×10×10 |
| 96 | 26 Medium Crate | (650, 12243) region 1087 | 20×20×20 |
| 97 | 26 Medium Crate | (623, 12218) region 1087 | 20×20×20 |
| 112 | 26 Medium Crate | (593, 12350) region 1087 | 20×20×20 |
| 121 | 26 Medium Crate | (564, 12367) region 1081 | 20×20×20 |
| 122 | 26 Medium Crate | (635, 12271) region 1087 | 20×20×20 |

Control 121 is the box in the hole. A 20-unit box does not make an 85-unit step. HINTBOOK 2033–2048: stack the boxes, climb, take the mace, use it on the roaches, do not keep it. The two mace records are height −130, the upper floor, at (417, 12444) region 1092 and (471, 12480) region 1099. The push is not an opcode in this file. The solids block the player and do not move.

## Still open

Which longplay frame shows the stack. The item-pickup callee for the mace. Definition 13572's name.
