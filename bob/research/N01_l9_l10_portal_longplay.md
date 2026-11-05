# N01 Review of act3-story 75597f2

No Godot was run. The commit adds `L10_DC` and `L9_DR` to `PORTAL_VISIBILITY_AREAS` and stops `l8_blade_for_daniel` while `gift` is `delivered`. The 58/58 line is the commit message. Those tests were not opened. The village change matches the accepted review of `77f63c7`: `stuck_id` records that note only for `unoffered` and `dropped` at `entry`. No new problem on that line.

## What the walk hides

DECODED, `scripts/lol2/region_visibility.gd` at `75597f2`. Each frame a walk starts in the camera's region. It crosses a creature-nav edge only when that edge lies in a narrowing horizontal window. Pitch is not read. `_angle` uses the camera's XZ facing. `NEAR` 160 widens a nearby edge to the full horizontal window. It does not add a region that shares no edge. A cluster with no reached region is hidden (`CLUSTER_SIZE` 24). Props and module meshes stay drawn. The deviation on the same commit says native portal rules are not decoded and vertical portals are ignored.

A shared nav edge still shows the next region when that edge is inside the yaw window, including when the camera looks down. A lower or far region with no such edge stays hidden even if the original frame shows it.

Nav floors, same tree. Marker `(x, y)` is nav `(x, -z)`.

L10_DC: 4320 regions, floors -157 to 175. Neighbor pairs whose floors differ by 80 or more: two. Region 3853 at marker (3096, 2255), floor 0, links region 3933 at floor -90. Region 3852 at (3320, 2256), floor 0, links region 3921 at floor -90. Other stacks of about 280 (surface 175 or 130 over -150 or -90) are not neighbors. One stack sits at (2928, 1320), floors -150 and 175, near the emperor door at (3205, 1327).

L9_DR: 6829 regions, floors -490 to 632. The magic-bridge chasm is a neighbor link, drop 244, floors 13 and -231. The pairs sit at (-1364, 2010), (-1392, 1779), (-1707, 1638), (-1710, 1791), and (-1710, 1910). Brady's bridge controls are (-1364, 1803) and (-1586, 1802). That pit is reached when its edge is in the yaw window, so it is not a hide. Non-neighbor stacks remain. The tower shaft near the gauntlets at (-3257, 1028) height -110: (-3248, 1488) floors 591 and -110, (-3249, 1540) floors 600 and -110, (-3544, 1284) floors 530 and -110, (-4123, 832) floors -60 and 632. Further non-neighbor drops: (1222, 1801) floors 30 and -490, and (2832, 10808) floors 530 and 0 near the statue home (4135, 10151).

## Longplay

Index `longplay_frames_act2plus/INDEX.txt`: `g_N = 6580 + (N-1)*30` seconds. Frames opened from `g_00048` through `g_00186`. Cemetery entry is the red portal on `g_00056` at 2:17:10, the same 137:10 the L10 preview deviation cites. `g_00145` at 3:01:40 is Dawn on the jungle shore. Gameplay between those two frames is the Cemetery and the Ruins. Cameras are not bound to regions. `g_00136`, `g_00138`, `g_00139`, and `g_00140` have no portrait and are not used as gameplay views.

| frame | time | grade | what the original shows | walk |
| --- | --- | --- | --- | --- |
| `g_00062` | 2:20:10 | LONGPLAY + LIKELY | Cemetery. A raised slab with an orb, and a lower floor in the gap around the slab. | The orb is a prop and stays drawn. The lower floor hides when it is one of the non-neighbor stacks. L10's only cross-floor nav links are the two 90-unit pairs at y 2255. The camera is not bound to those pairs. |
| `g_00071` | 2:24:10 | LONGPLAY + LIKELY | Cemetery surface. A crenellated parapet with a figure standing on it, and the open yard in front. | The figure stays drawn. The parapet mesh hides when that high region shares no nav edge with the yard. |
| `g_00080` | 2:29:40 | LONGPLAY | Cemetery yard. A low wall on the left, open ground, a long building, and a bare tree. | Connected yard floors still draw. Ground past a wall that is not a nav edge hides. |
| `g_00087` | 2:32:40 | LONGPLAY + LIKELY | Cemetery yard. A low brick wall, sky above it, and a building face beyond. | The sky is the panorama, not a region mesh. The building face hides on the same rule as `g_00080`. |
| `g_00095` | 2:36:40 | LONGPLAY + DECODED | A cracked bridge, a creature on the deck, a green far wall, and a black void beside the deck. | Not a hide. The void is the original already culling. The 244-unit bridge drop is a nav neighbor, so the walk can draw that pit when the edge is in the yaw window. |
| `g_00115` | 2:46:40 | LONGPLAY | Ruins yard. A dead tree, low buildings, and a dark door. | Same yard rule as `g_00080`. The door is an opening, not a measured window. |
| `g_00125` | 2:51:40 | LONGPLAY + LIKELY | Ruins. A facade of window panels, a roof plane, and the open space below the roof. | Pitch is ignored. A lower region that is not a nav neighbor stays hidden. The tower stacks above are the nearest decoded overlook. This frame is not bound to them. |
| `g_00116` | 2:47:10 | LONGPLAY | A double door with an arched opening on each side. | A side arch that is a nav edge still draws. No lower floor is visible in this frame. |

No opened gameplay frame shows a room through a glass pane. `g_00113` at 2:45:40 is four portrait panels and a column. `g_00073` at 2:25:40 is a stone lattice with one dark doorway. `g_00127` at 2:52:40 looks up a stair at a statue and shows the steps, which a nav link along the stair still draws.

`g_00035` at 126:40 is before this entry and is not the Ruins visit. The earlier L9 note that used it stays unbound.
