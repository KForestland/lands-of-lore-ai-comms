# OF4. The glass globe at (155, -3704)

Owner F10 T23-36-20. "cant pick up orb". Camera `(154.9, -32.96, -3704.2)`, location height -43, so the body origin is -43 and the feet are at -75. Screenshot: the globe sits in the sky beside a pillar. No code change beyond the OF9 collision. This note is the globe site.

## Grades

| Claim | Grade |
| --- | --- |
| The globe he is looking at is item 47, `96-E Globe`, file position `(188, 0, -3756)`, region 1125 | PROVEN. Nearest globe to the report. Horizontal distance 62 |
| Region 1125's floor is y 0. A body standing on it has origin y 32. Origin -43 puts the feet on y -75 | PROVEN. Arrival origin is floor+32 (`area.json` start height 32 on floor 0). Camera y is origin+10 |
| y -75 is the ceiling of underground region 1795, whose floor is -150. The surface floor of region 1123 (y 0) also covers that xz | PROVEN (`geometry.json`, `area.json` faces 1714 and 3029) |
| From origin y -43, aimed at item 47, `take` returns false | PROVEN (`tests/l10_surface_globe_test.gd`) |
| From origin y 32 at the same xz, the same `take` collects `act2:L10_DC:item47` | PROVEN (same test) |
| Region 1769 edge 2, wall record 3105, y -150 to -75, native neighbour null, is one of the OF9 void walls. A walk through it stays in the room, resets 0 | PROVEN (same test; the edge is in `l10_void_edges.json`) |
| That wall is the opening he used | LIKELY. It is a wide room within 500 of the gap, and the feet match the ceiling he stood on. The report does not store the path |
| The globe must be lowered, or it is scripted to float | Not found. The file height is 0, on the surface floor. BJ14 S6 is the pickup prompt for other globe rows (44, 56, 8, 45, 9, 43), not this height |

## What was not this globe

OF5 at (1358, -1269) is the stone chest. The nearest placed globe is 590 away. Movable 83 (template 8, a flat slab at source (1374, 1196)) has no script events. Not fixed here.

OF6 at (-529, -4058) took item 46, `96-E Globe` at (-537, 0, -4079), and the report shows "E Globe taken." The take works once he is in the room. The clip that got him in is not this fix.

## Test

`/tmp/godot_dummy.sh --headless --path ~/opus_work/lol2_grok_of9 --script res://tests/l10_surface_globe_test.gd`

Printed `PASS L10 surface globe: item 47 is refused under the floor and taken from it, region 1769 edge 2 holds, resets 0`. Exit 0.

No new deviation piece. The collision is piece 0508.
