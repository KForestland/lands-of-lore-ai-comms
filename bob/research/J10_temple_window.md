# J10 L14 temple window after portal visibility

No Godot was run. `L14_HT.MIX` sha256 prefix `c294f9ab`. The portal walk below is the same rule as `region_visibility.gd` in act3-story `44a6d98` (clusters of 24, an edge within 160 units passes the full view, otherwise the horizontal window). `PORTAL_VISIBILITY_AREAS` is `L14_HT` only. The start region is the nav region whose floor is closest to the player height.

## What the fix hides

18-01-10, report `report_2026-11-03T18-01-10_149234627`, "texure error here". Camera Godot (2625.3, 42.0, −2698.8), native (2625.3, 2698.8), yaw 0.348. That point is inside region 918 (floor 0, ceiling 110) and inside region 630 (floor −100, ceiling 1200). The closer floor is 0, so the walk starts at 918.

Region 630 is not a nav neighbor of 918. Its cluster is 278: regions 532–537, 552, 609, 610, 614, 630, 631, 638–640, 644, 670–677. Nothing in that cluster is reached from 918, in either look direction. Those faces go away. The one filling the shot is face 9152, region 630, material `182`, heights −100 to 156, at native about (2635, 2649). Texture `47f5b112c200646a0843.png`. The same shell has face 9154 (region 631, material 182, −100 to 145) and face 9168 (region 640, material 182, −100 to 150).

The same walk from the hall does not reach the floor −80 rooms. Face 12894, region 3255, material `221`, heights −80 to 20, is in that set. Cluster 278 and those −80 clusters stay hidden at both poses.

## What is still drawn in the hall

18-01-36 and 18-01-44 are the same room. Reports `report_2026-11-03T18-01-36_175200253` ("texure is all worng") and `report_2026-11-03T18-01-44_183341579` ("gemotry is worng"). Cameras native (2876.3, 3361.9) and (2884.7, 3375.9), eye height 42, yaw −0.538. Both are region 21, floor 0, ceiling 125. The walk reaches regions 17, 16, 0, and 12. Cluster 0 (the batch that stays on) is regions 0–3, 5–7, 12, 17, 20–28, 30, 819, 835, 837, 838, 1055. Cluster 3 is only 15 and 16, and 16 is reached, so it stays on too.

The wood is the original room. Longplay `g_268` shows the carved face panel and the skull frieze. Those keys are material `495` (`aae3b5f537e69dbcf911.png`, the face panel) and material `496` (`c723b1e047c513b3a8de.png`, the skull frieze). Floor and ceiling are material `473` (`9a92798449ff90c8154c.png`, the stone tiles). Face 8230 is region 17, material 496, heights 95 to 125, native (2709, 3312) to (2889, 3269). Face 8240 continues it, region 25, material 496, heights 95 to 125, to (3091, 3348).

Under that frieze the wall is only a 15-unit strip. Face 8228, region 16, material `181` (`f54ade4501accbdd849b.png`, stone with two wood bands), heights 80 to 95, native x 2743 to 2900, y 3254 to 3266. Face 8245, region 30, material 181, heights 80 to 95, continues it to x 3107. Region 16's edge 2 is the neighbor 15 edge, from (2900, 3254) to (2743, 3266). No wall face covers heights 0 to 80 on that edge. Region 15's own lower faces 8225 and 8226 sit on the far side, native y about 3234, not on this edge. That opening is the gap in the 18-01-36 and 18-01-44 shots, including the two blue rectangles. There is no material key on it. The port background there is the L14 sky pack (`act2_map.gd`). Longplay `g_276` and `g_278` clear that kind of opening to black.

## What is still drawn in the garden

Cluster 334 stays on, because the walk starts in it. The stone lips above the garden ceiling stay:

| face | region | material | heights |
| --- | --- | --- | --- |
| 1810 | 918 | 473 | 110 |
| 9634 | 915 | 473 | 110 to 135 |
| 9656, 9657 | 933 | 473 | 135 to 150 |
| 9670 | 940 | 473 | 135 to 150 |

Face 9634 is the step on the shared edge of 918 (ceiling 110) and 915 (ceiling 135), about 32 units from the camera. That is the stone slab still in the upper part of the 18-01-10 shot after the 182 wall is hidden. Region 918's floor face 1809 is also material 473. The green ground and the willow in that shot are not an `area.json` prop within 120 units.

## Longplay g_262 to g_286

`g_268` is this hall's wood. `g_262` is the dark rock corridor, the other room the garden was seeing (material 182). `g_276` and `g_278` are the rock platforms in a black void. `g_286` is a pale stone court, the same stone family as material 473. `g_272`, `g_280`, and `g_284` are other temple spots, not this window.

## Still open

Which mesh draws the willow and the green ground at region 918. A native portal rule was not read. The 24-region batch still shows every region in cluster 0 once region 21 is reached, including regions the walk itself did not enter.
