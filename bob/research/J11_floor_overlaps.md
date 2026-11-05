# J11 Overlapping floor polygons

No Godot was run. Source is `all_maps_20260922/<AREA>/geometry/geometry.json` (the same region outlines the area packs draw). Polygons were normalized to counter-clockwise before the clip. Hive outlines are stored clockwise, and a clip that keeps that winding reports no overlap. A pair counts when the overlap area is over 1 square unit and the floor-to-ceiling spans share more than 1 unit of height. A span that only meets, or sits within 2 units, is a touch and is not in the rank. Regions with no ceiling number, a polygon under half a square unit, or a height under 1 unit were left out. On L5 that keeps 1002 of 1292 regions. The L5 pair 758×911 (area 571, shared height 250) is the one already posted in J07, so the count is the same test.

## Rank

Portal visibility matters in this order. The hub is the region that sits in the most pairs.

| area | overlap pairs | regions in those pairs | touch pairs | height mix | hub (pair count) |
| --- | --- | --- | --- | --- | --- |
| L10_DC | 1950 | 1324 | 72 | 838 thin (1–16), 452 mid, 660 tall | 217 (77), 1534 (73) |
| L14_HT | 1907 | 1060 | 72 | 65 thin, 1100 mid, 742 tall | 3268 (33), 781 (32) |
| L9_DR | 910 | 632 | 141 | 54 thin, 314 mid, 542 tall | 1641 (14), 5016 (14) |
| L16_CA | 206 | 157 | 0 | 199 tall | 8138 (18), 8139 (15) |
| L8_SJ | 54 | 70 | 16 | 14 mid, 40 tall | 3397 (9) |
| L20_BB | 38 | 22 | 0 | all tall | 684 (7) |
| L19_BC | 36 | 24 | 0 | 21 mid, 14 tall | 1914 (16) |
| L4_HJ | 28 | 22 | 0 | all tall | 1905 (7), 1902 (7) |
| L12_CM | 25 | 20 | 0 | 23 tall | 3410 (8), 3411 (8) |
| L5_HC | 21 | 22 | 15 | 10 thin, 9 mid, 2 tall | 401 (10) |
| L7_DH | 20 | 20 | 0 | all tall | 1389 (4), 1414 (4) |
| L17_HC | 9 | 6 | 0 | all mid, same 0..64 | 562, 1228, 561, 565 (3 each) |
| L1_DC | 2 | 4 | 0 | both tall | 1101×1102 and 1108×1332 |
| L3_DH | 0 | 0 | 0 | | |
| L13_RC | 0 | 0 | 0 | | |

Thin means the shared height is 1 to 16 units. Mid is 17 to 64. Tall is over 64. L10's 838 thin pairs are slabs sitting a few units inside a taller room. L14 and L9 are mostly real stacked volumes.

## What the big pairs are

L10's largest is regions 1876 and 3920, area about 23537, heights 0..130 and 0..200. Region 217 is in 77 pairs and region 1534 is in 73. Turn the walk on here first.

L14's largest is 2132×2287, area about 84452, heights 190..590 and 140..220. Region 781, one of the floor −80 shells from the 18:01 window, is in 32 pairs. Region 3268 is in 33. The temple walk in `44a6d98` is already the right area. L9 is the next one (910 pairs, no single region over 14).

L4's 28 pairs are all tall. Regions 1901, 1902, and 1905 (floor 0, ceiling 68 or 128) sit inside the shells 3330–3335 (floor −500, ceiling 400). That is the jungle sky shell over the walkable ground. L12 is the same shape: regions 3409, 3410, and 3411 (floor −1190, ceiling −440) cover the −950..−750 floors, 25 pairs.

L16's 206 pairs sit on a few tall boxes. Region 8138 (18 pairs) and 8139 (15) cover rooms whose heights are about −30..230 against 50..170. L19's 36 pairs mostly use region 1914 (16 of them). L20's 38 pairs are 22 regions, all tall, hub 684. L7's 20 pairs are the high band around 700..950, hubs 1389 and 1414. L8's hub is 3397 (floor 0, ceiling 64) inside rooms that run 0..200.

L17's 9 pairs are the same floor 0 and ceiling 64 copied: 561, 562, and 565 each overlap 1228, 1235, and 1236. Those are coplanar floors, not a tall shell.

L5's tall pair is the J07 one, 758×911 and 758×907. The ten thin pairs are region 401 (floor −1050, ceiling −912) over the −921..−891 slabs 1196, 1205, 1206, and 1208. The 15 touches are stacked floors that meet, such as region 678's ceiling −1259 against region 796's floor −1259.

L1 has two small pairs: 1101×1102, area 27, both heights −130..−62, and 1108×1332, area 9. L3 and L13 have none.

## Still open

Whether the original portal clip hides each of these, or only the ones with no shared nav edge. The rank is the draw order for trying the L14 walk on the next area: L10, then L9, then L16.
