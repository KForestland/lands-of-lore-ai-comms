# L10 and L14 move proposals (2026-11-13)

Read-only. Godot was not run. Nothing was moved. The geometry is the unmoved archive `all_maps_20260922`. Zone ids are the G-16 recount (largest pair-area first). A pair is `prepare_region_mover.overlaps` rules 1–5 (area above 4, floor bases within 48, not neighbours, no flag 0x80, spaces meet) and then centre floors within 24. Inside every zone below, that pair count matches the recount.

A side is one neighbour-component inside the zone. Joins are neighbour links from that side to a region outside the zone. Clearance is 10. After the shift, every moved `floor_base` differs from every partner `floor_base` by more than 48. An open roof (`ceiling_base = floor_base + 1300`) is not a stone ceiling. Free space is a third region whose plan overlaps the side and whose body is wholly under the side's lowest floor or wholly over its highest finite ceiling.

The move is one rigid vertical dy of one finite side, and that side has to be one end of every pair in the zone. Where a one-region side fits, that region is the transform. Otherwise the smaller side is the transform, and the dy is the smaller direction whose final body does not strictly enter a third finite body. Touching at a boundary is not an entry. The producer's ramp length and its 0.72 grade cap were not measured. A plan hit is not the same as standing in the region. Chain fixtures here have no height. Owner feet are body height minus 32.

Method (a) only. No producer writes an x,z shift. No zone below is assigned to a sideways move or a redraw.

## Scan

| Zone | Move |
| --- | --- |
| L14 T0 | no move fits |
| L14 T1 | 4106 down 74, no outside join |
| L14 T2 | 1461, 1463, 1464 down 130 |
| L14 T3 | already moved, no second shift |
| L14 T4 | 4073 down 53, no outside join, four items on the lid |
| L14 T5 | 1502, 1503 up 110 |
| L14 T6 | 1451, 1456 up 90 |
| L14 T7 | 4062 down 49, no outside join |
| L14 T8 | 863, 864 up 74 |
| L14 T9 | 4074 down 74, no outside join |
| L14 T10 | 3344, 3357, 3364, 3365, 3366 down 130 |
| L14 T11 | already moved, no second shift |
| L14 T12 | already moved, no second shift |
| L14 T13 | no move fits |
| L14 T14 | no move fits on this pack |
| L14 T15 | 3268, 3418 down 100 |
| L14 T16 | 2329 down 74, no outside join |
| L10 T0 | no move fits |
| L10 T1 | 136, 138, 139, 140, 141 up 110 |
| L10 T2 | 214 up 110 |
| L10 T3 | 143, 146, 147, 148, 149 up 110 |
| L10 T4 | 405 up 110 |
| L10 T5 | 263 up 110 |
| L10 T6 | 844, 846 up 95 |
| L10 T7 | 83, 2473 up 95 |
| L10 T8 | 1533 up 110 |
| L10 T9 | 826, 847 up 95 |
| L10 T10 | 86, 2387 up 95 |
| L10 T11 | 849 up 95 |
| L10 T12 | 2388 up 95 |
| L10 T13 | 3607, 3635 up 130 |
| L10 T14 | 1934 up 110 |
| L10 T15 | 2435, 2436 up 110 |
| L10 T16 | 2232 up 210 |
| L10 T17 | 2204 up 210 |
| L10 T18 | 991 up 72 |

## L14

### T0 — no move fits

92 regions, 151 pairs, area 304844.6, box x 1205..2234, z -2964..-1826. Seven sides: 1, 1, 1, 2, 14, 33, 40. All 151 pairs run between the roofed 40 and the six open patches. The open patches are floor -100, ceiling 1200, and they are not neighbours of the roof or of each other. The roof is floors -120, -103, -96, ceiling -59..-20, 27 joins into covered rooms at floors -138, -129, -120, and -71.

The finite drop of that roof is 90: ceiling -20 becomes -110, ten under the open floor -100, and the floors end more than 48 apart. The final body is -210..-110. That body enters five third regions, all floor -155 and ceiling -51: 3610 (overlap 14.3), 3614 (124.2), 3618 (140.4), 3619 (298.5), and 3620 (257.8). There is no second direction. The open ceiling is not a stone ceiling to rise above, and raising the open patches would lift them into the ledge floors at 125..164.

On the roof: `prop_1049` records 397, 398, 400, 401. Movable 83's plan falls in 3573, and its height is 177, so it is not standing on this floor. Chain plan: 11 points on the roof and 2 on the 33-region patch, all from `l14_ledge_maze_walk.json`, no height in the fixture. The T0 study measured those bodies on the raised ledges outside T0, except two jump lips that sit only in T0. No owner pose is in a T0 quad. Nothing is placed on the open patches. Free space under the roof, wholly below floor -120, was not found. The nearest floor wholly above the roof ceiling is 140.

### T1 — 4106 down 74

3 regions, 2 pairs, box x 83..643, z 1311..2256. Smaller side is 4106 alone: floor 0, ceiling 64, joins 0. Faces: 1 floor, 1 ceiling, 4 boundary. `prop_574` record 81. No item, no movable, no chain point, no owner pose, no script point. Nothing wholly above or below. The other side is 2304 and 2308, floor 0, ceiling 0..380, 3 joins at floors 0 and 190.

Down 74. Floor 0 becomes -74 and ceiling 64 becomes -10, ten under the other floor. The moved region has no outside neighbour. No collide check was run.

### T2 — 1461, 1463, 1464 down 130

7 regions, 6 pairs, box x -153..217, z -2063..-1553. Smaller side floor 190, ceiling 270..290, 2 joins at floor 190. Faces: 3 floor, 3 ceiling, 6 boundary. Movable 89 (template 24) at (32, 190, -2061) is in 1461, and `l14_trials.gd` door 89 is the same point, feet 198, inside 1461. The other side is 1305, 1308, 1492, 1493, floor 170..190, ceiling 240..345, 5 joins at 160 and 190. `prop_1049` records 395 and 396 are in 1308. 1305 and 1308 are in `l14_tilt.gd` `LOWER_CEILINGS`. No chain point and no owner pose.

Down 130. Ceiling 290 becomes 160, ten under floor 170, and the floors differ by more than 48. The two joins become steps of 130. Door 89 and movable 89 go with the side. The tilt ceilings stay. This is the same shift as the small-zones note.

### T3 — already moved

73 regions, 135 pairs. The tunnel side is the 24 regions from 2520, and the room side is the 49 regions that include 2768. The move file already dips that tunnel by 100 and ramps 2516, 2519, 2541, 2544, 2546, 2548, and 2551. Held for r19h. No second shift.

### T4 — 4073 down 53

5 regions, 4 pairs, box x 3019..3409, z -2839..-2596. The finite side is 4073 alone: floor -96, ceiling -59, joins 0. Faces: 1 floor, 1 ceiling, 4 boundary. Four items are tagged to it, all at height -96: Dreamstone (3264, -96, -2664), Cry shard, Jkar idol, Statuette. One chain plan point (3295, -2611) from `l14_ledge_maze_walk.json`, no height. No owner pose. Nothing wholly above or below. The other side is 533, 534, 535, 536, open roofs at floor -100.

Down 53. Ceiling -59 becomes -112, twelve under the open floor, and the floor bases differ by 49. The four items are on the moved region. The moved region has no outside neighbour. No collide check was run.

### T5 — 1502, 1503 up 110

5 regions, 4 pairs, box x 217..653, z -2195..-1772. Smaller side floor 190, ceiling 310..345, 5 joins at floors 190 and 280. Faces: 2 floor, 2 ceiling, 3 interior, 1 boundary. `prop_1049` record 393 is in 1502. The ledge-maze plan point (521.5, -1950.5) lies in 1502 and in 1467. The other side is 1465, 1467, 1468, floor 180..190, ceiling 272..290. Door 90 and movable 90 are in 1465 and stay. No owner pose. Nothing wholly above or below the smaller side.

Up 110. Floor 190 becomes 300, ten over ceiling 290. The joins at 190 become steps of 110. The joins at 280 become a step of 20. Same shift as the small-zones note.

### T6 — 1451, 1456 up 90

4 regions, 3 pairs, box x -706..-147, z -2220..-1732. Both sides have two regions. 1451 and 1456 are floor 190, ceiling 310..345, 5 joins at 190 and 280. `prop_1049` record 394 is in 1456. Nothing wholly above. The other side is 1459 and 1460, floor 180..190, ceiling 270. Door 88 and movable 88 are in 1459. The fire-path plan point (-681, -1776.5) is in 1460. No owner pose.

Up 90. Floor 190 becomes 280, ten over ceiling 270, and level with the joins at 280. The three floor-190 joins become steps of 90. Door 88 stays. Same shift as the small-zones note.

### T7 — 4062 down 49

9 regions, 8 pairs, box x 2191..2490, z -2294..-2000. The finite side is 4062 alone: floor -100, ceiling -80, joins 0. Faces: 1 floor, 1 ceiling, 4 boundary. `prop_529` record 157. No chain, no owner, no script. The nearest floor wholly above is region 4043 at 0. Nothing wholly below. The other side is eight open roofs at floor -100.

Down 49. Ceiling -80 becomes -129, under the open floor -100, and the floor bases differ by 49. The new floor is -149, twenty-nine under 4043. The moved region has no outside neighbour. No collide check was run.

### T8 — 863, 864 up 74

4 regions, 3 pairs, box x 2164..2482, z -2486..-2045. Three sides. The walk is 863 and 864: floor 0, ceiling 80, 1 join at floor 0. The entry plan point (2415, -2486) is in 864, no height. Lid 4043 is floor 0, ceiling 64, joins 0, `prop_574` record 159, with region 4062 wholly under it at ceiling -80. Region 660 is an open roof, floor 11. No owner pose.

Up 74 of 863 and 864. Floor 0 becomes 74, ten over 4043's ceiling 64, and 63 above 660's floor 11. The pair with 660 leaves the list because the floor bases differ by more than 48. The body is still inside 660's open volume. The one join becomes a step of 74. The lid stays.

### T9 — 4074 down 74

5 regions, 4 pairs, box x 1866..2088, z -4107..-3682. The lid is 4074: floor 0, ceiling 64, joins 0. Faces: 1 floor, 1 ceiling, 4 boundary. `prop_1059` record 85. Shard-bowl plan points fall in 4074 and in the other side (959, 961), no height. The other side is 959, 961, 1067, 1073, floor 0, ceiling 80..120, 8 joins at floor 0. Nearest ceiling wholly under the lid is -229. No owner pose.

Down 74. Ceiling 64 becomes -10, ten under the room floors. The rooms stay, so a plan point that also lies in 959 or 961 stays unless the save stored region 4074.

### T10 — 3344, 3357, 3364, 3365, 3366 down 130

8 regions, 9 pairs, box x 2269..2606, z -3002..-2619. The finite side is floor -80, ceiling 20, 9 joins at -80 and -60. No prop and no item. One priest-approach plan point (2500, -2805) is in 3366. The other side is 609, 610, 631, open roofs at floor -100. Entry and priest-approach plan points sit in that open side. No owner pose in the current report set falls in either side. Nothing wholly below the finite side.

Down 130. Ceiling 20 becomes -110, ten under the open floor. The open side stays. The nine joins become steps of 130 to 150. This is the finite side the small-zones note shifted down 130. That note called the zone T12.

### T11 — already moved

8 regions, 7 pairs. Regions 36 and 38 are the trench floors the move file raises to 25, together with 34 and 40. The corridor side is 3882, 3889, 3890, 3894, 3906. Region 3902 is the pocket the small-zones note measured separately. No second shift.

### T12 — already moved

5 regions, 4 pairs. Region 34 is in that same floor raise. The corridor side is 3874, 3877, 3879, 3884. Region 40 had no pair. No second shift.

### T13 — no move fits

2 regions, 1 pair, box x 1332..1552, z -1935..-1823. Region 3593 is floor -120, ceiling -20, 3 joins at -120 and -71. One ledge-maze plan point (1473, -1929.5), no height. Region 2108 is an open roof at floor -100. Nothing wholly below 3593. The nearest floor wholly above the ceiling is 140.

Down 90 would put the ceiling at -110, ten under the open floor. The final body -210..-110 enters five regions at floor -155, ceiling -51: 3622 (overlap 8.9), 3623 (362.5), 3629 (36.7), 3630 (162.2), and 3631 (303.3). No second direction.

### T14 — no move fits on this pack

2 regions, 1 pair, area 744.5, box x 656..1839, z -4945..-4689. Region 2517 is floor -50, corners -50..-40, ceiling 30..40, 2 joins at -60 and -40. Chain plan (1583, -4772) and (1583, -4800). One owner pose, (1546.9, -4806), feet -43, inside 2517. Region 3185 is floor -60, corners -70..-60, ceiling -10..0, 2 joins at -70 and -60. Fourteen chain plan points, no height. `l14_library.gd` at (1672, 96, -4912) falls in the plan and the feet are at 64, above this ceiling. Nothing wholly below either region.

On this unmoved pack the separating arithmetic is 2517 down 120 or 3185 down 60. Neither is the proposal. 3185 is the KEEP the T3 dip was capped against, and ramp 2516 is a T3 delta. The small-zones note's down 120 of 2517 was measured before that ramp moved. The next dy belongs on the moved pack.

### T15 — 3268, 3418 down 100

7 regions, 7 pairs, box x 2585..2828, z -3884..-3757. Smaller side floor -80, ceiling 20, 4 joins at floor -80. Shard-bowl plan points sit in 3268. `l14_lower_passage.gd` at (2800, 0, -3800), feet -32, is inside 3268. Nearest ceiling wholly below is -389. Regions 341 and 2493 are wholly above, floor 30. The other side is 321, 322, 355, 373, 374, floor -70, ceiling 60, 10 joins at -70 and -20. No owner pose. No prop.

Down 100. Ceiling 20 becomes -80, ten under floor -70. The four joins become steps of 100. The script point and the shard-bowl plan points are on the moved side.

### T16 — 2329 down 74

2 regions, 1 pair, box x -1373..-1121, z -4427..-4049. Region 2329 is floor 0, ceiling 64, joins 0. `prop_1049` records 365, 366, 367, 368. Region 3219 is floor 0, ceiling 300, joins 0. No chain, no owner, no script. Nothing wholly above or below.

Down 74. Ceiling 64 becomes -10, ten under 3219's floor. The moved region has no outside neighbour. No collide check was run.

## L10

Down is blocked on most of these zones by cellars at floor -150, ceiling -75, or floor -135, ceiling -80, under the sheet. The fit is the upward dy.

### T0 — no move fits

41 regions, 63 pairs, area 147662.9, box x 2668..3899, z -2330..-1728. Six sides: 1, 1, 1, 1, 18, 19. The 18 is floor 0, corners down to -90, ceiling 100..200, 18 joins. The 19 is floor 0, ceiling 130..175, 16 joins, with `prop_123` record 92, `prop_649` record 423, and `prop_648` record 436. The singles are 306 (floor 0, ceiling 175), 3906 and 3911 (floor 20, ceiling 200, `prop_629` records 249 and 250), and 3934 (floor 20, ceiling 200, joins 0). No one of these sides is an end of every pair, so one rigid dy does not clear the zone.

Chain plan points fall on both large sides (`l10_emperor_supply_walk.json`, `l10_blue_walk.json`), no height. One owner pose, (2760.2, -2133), feet -150, is in the plan of both large sides and below both floors. Cellars at ceiling -75 sit under parts of the sheet. This pass does not name a centreline of smaller dips.

### T1 — 136, 138, 139, 140, 141 up 110

24 regions, 42 pairs, box x -311..650, z -4259..-3786. The moved side is floor 0, ceiling 130, 11 joins at 0, 90, and 130. Props: `prop_123` records 88 and 89, `prop_620` record 167, `prop_648` record 430, `prop_649` record 451. Supply-walk plan points sit here. Movables 81 and 82, height 35, fall in this plan and also in 1082 and 1083, and height 35 is inside both volumes. One script point in 136 is feet -150, below the floor. The other large side is 17 regions, floor 0..10, ceiling 100. Nearest cellar ceiling under the moved side is -75. Nothing wholly above.

Up 110. Floor 0 becomes 110, ten over the other ceiling. Joins at 0 become steps of 110. Joins at 90 and 130 become steps of 20 and 0. The 17-region side stays.

### T2 — 214 up 110

42 regions, 41 pairs, box x -974..-69, z -2290..-1798. Region 214 is the sheet: floor 0, corners up to 50, ceiling 130, 4 joins at 0, 30, 50, and 90. Props: `prop_123` records 86 and 98, `prop_648` record 433. Four blue-walk plan points, no height. No owner pose. Forty-six cellar regions sit under it, nearest ceiling -40, which is why the sheet does not go down. The other 41 regions are the cells, floors 0..35, ceiling 100.

Up 110. The low floor becomes 110, ten over those ceilings. The cells stay.

### T3 — 143, 146, 147, 148, 149 up 110

12 regions, 12 pairs, box x 2893..3693, z -4203..-3774. Moved side floor 0, ceiling 130..175, 7 joins at 0, 130, and 175. `prop_620` record 162. Sixteen chain plan points, including the fresh-two-blue and robot-oil stands, no height. The other side is seven regions, floor 0..10, ceiling 100. Nothing wholly below the moved side. Region floors at 130 sit over the other side.

Up 110. Joins at 0 become steps of 110. Joins at 130 and 175 become steps of 20 and 65.

### T4 — 405 up 110

10 regions, 9 pairs, box x -764..-311, z -4339..-4189. Region 405 is the sheet: floor 0, ceiling 175, 3 joins at 0 and 90. No prop. One silverleaf plan point. `l10_globe_room_wall_test.gd` has feet 0 and feet 8 inside 405. Cellars under it, nearest ceiling -75. The cells include 1444, 1447, 1448, 1452, 1455, 1498, 1500, floor 0..10, ceiling 100, and the fall-trace points whose feet are inside those cells. Movables 64 and 65 stand in 1450 and 1453. No owner pose in the bundle set.

Up 110 of 405. The cells, the movables, and the fall-trace feet stay. The two test points that sit in 405 follow the sheet.

### T5 — 263 up 110

8 regions, 7 pairs, box x 725..1602, z -1322..-1103. Region 263 is floor 0, ceiling 90, 4 joins at 0 and 90. No prop, no chain, no owner, no script. Cellars under it, nearest ceiling -30. The other regions are floors 0..10, ceilings 64..100.

Up 110. Floor 0 becomes 110, ten over the tallest of those ceilings.

### T6 — 844, 846 up 95

8 regions, 8 pairs, box x 2356..2576, z -2934..-2753. Moved side floor 15, corners up to 100, ceiling 95..115, 6 joins at -20, 0, 100, and 130. `prop_580` record 465. No chain and no owner. Cellars under it at ceiling -75. The other side is six regions, floor 10..35, ceiling 45..100. Floors at 130 are wholly above that other side.

Up 95. Floor 15 becomes 110, ten over ceiling 100. Joins land as steps from -130 to 20.

### T7 — 83, 2473 up 95

8 regions, 8 pairs, box x 1940..2169, z -2933..-2753. Same shape as T6. `prop_580` record 463. Emperor-supply and blue-walk plan points fall in 83 and also in 478, which stays. No owner pose. Cellars at ceiling -75. The other side is 461, 466, 467, 469, 472, 478.

Up 95. The shared plan points stay in 478 unless a save stored 83 or 2473.

### T8 — 1533 up 110

13 regions, 12 pairs, box x -1104..-371, z -1723..-1224. Region 1533 is floor 0, corners up to 50, ceiling 195, 3 joins at 0, 50, and 90. Props: `prop_123` record 84, `prop_649` records 419, 444, 446, `prop_648` record 428. No chain and no owner. Nothing wholly above or below this sheet in the third-region test. The other regions are floors 0..35, ceiling 100.

Up 110. The low floor becomes 110, ten over those ceilings.

### T9 — 826, 847 up 95

6 regions, 6 pairs, box x 2354..2573, z -3227..-3063. Same shape as T6. `prop_580` record 468. No chain and no owner. One cellar, ceiling -80. The other side is 2338, 2345, 2352, 2354, floor 10..35, ceiling 45..100.

Up 95.

### T10 — 86, 2387 up 95

6 regions, 5 pairs, box x 1939..2170, z -3227..-3063. Same shape as T6. `prop_580` record 464. No chain point on the moved side. The owner pose (2009.1, -3125.4), feet 10, is inside region 479, which is on the side that stays. Cellars under the moved side, nearest ceiling -75. The other side is 465, 479, 481, 484.

Up 95. The owner pose stays.

### T11 — 849 up 95

2 regions, 1 pair, box x 2354..2573, z -3063..-2933. Region 849 is floor 15, ceiling 95, 4 joins at -20, 0, and 130. `prop_580` record 466. Region 2342 is floor 0, ceiling 100, `prop_540` record 508. No chain and no owner. Cellars under 849, nearest ceiling -75. Floors at 130 are wholly above 2342.

Up 95. Floor 15 becomes 110, ten over 2342. Region 2342 and its prop stay.

### T12 — 2388 up 95

2 regions, 1 pair, box x 1939..2169, z -3063..-2933. Region 2388 is floor 15, ceiling 95, 4 joins at 0 and 130. `prop_580` record 467. Region 492 is floor 0, ceiling 100, and holds the lid117 plan point (2071, -3006.5), no height. Cellar 1717, ceiling -75, is under 2388. Floors at 130 are wholly above 492.

Up 95 of 2388. Region 492 stays. Dropping 492 lands in the cellars, which is why the sheet is not the side that moves.

### T13 — 3607, 3635 up 130

3 regions, 2 pairs, box x 2349..2669, z -2624..-2358. The moved side is floor 10, ceiling 100, 4 joins at 10 and 35. No prop. Region 191 is floor 0, ceiling 130, `prop_648` record 437, and eight emperor-supply plan points. Cellars under both sides, nearest ceiling -75. Nothing wholly above the moved side.

Up 130. Floor 10 becomes 140, ten over 191's ceiling. The supply plan points stay on 191. Joins become steps of 130 and 105.

### T14 — 1934 up 110

3 regions, 2 pairs, box x 1854..2624, z -4288..-3665. Region 1934 is the sheet: floor 0, ceiling 175, 3 joins at 0 and 90. Props: `prop_123` record 107, `prop_649` records 421 and 458. Two silverleaf plan points, no height. Cellars under it, nearest ceiling -75. The other side is 1202 and 1203, floor 10, ceiling 100.

Up 110. The cells stay.

### T15 — 2435, 2436 up 110

4 regions, 3 pairs, box x 2304..2624, z -2148..-1730. Moved side floor 0, ceiling 130, 6 joins at 0, 70, and 90. Props: `prop_123` record 93, `prop_649` record 425. Six script points in `l10_catacomb_void_wall_test.gd` fall in the plan at feet -150 to -152, below the floor. Cellars under it, nearest ceiling -75. The other side is 3611 and 3614, floor 10, ceiling 100.

Up 110. Those script feet are not in the moved body.

### T16 — 2232 up 210

5 regions, 4 pairs, box x 3016..3100, z -1461..-1294. Region 2232 is floor 0, ceiling 175, 4 joins at 0 and 5. No prop, no chain, no owner, no script. Cellars under it, nearest ceiling -75. The other side is 3796, 3797, 3798, 3799, floor -20, ceiling 200, 8 joins at -50 and -30.

Up 210. Floor 0 becomes 210, ten over ceiling 200. The joins become steps of about 210. The down direction enters the cellars.

### T17 — 2204 up 210

5 regions, 4 pairs, box x 3313..3397, z -1461..-1294. Same shape as T16. Region 2204 is floor 0, ceiling 175, 4 joins at floor 0. The other side is 3791, 3792, 3793, 3794, floor -20, ceiling 200. Nothing placed. No chain and no owner. Cellars at ceiling -75.

Up 210. The joins become steps of 210.

### T18 — 991 up 72

2 regions, 1 pair, box x -309..258, z -1942..-1687. Region 991 is floor 0, ceiling 175, 4 joins at 0 and 130. Three owner-tour plan points, no height. Cellars under it, nearest ceiling -40. Region 3592 is floor 22, ceiling 62, 1 join at floor 0. Nothing wholly above 991. Region 217 at floor 130 is wholly above 3592.

Up 72. Floor 0 becomes 72, ten over ceiling 62. The join at 0 becomes a step of 72. The join at 130 becomes a step of 58. The tour plan points are on 991.

## L9 copy piles

These are not moves. Each pile is one plan quad stored on several region ids, same floor and same ceiling. The producer change is a dedup: draw and collide one copy. Portal visibility is already on for L9. This pass did not write a dy for any real L9 zone.

| Zone | Regions | Floor | Ceiling | Pairs | Box |
| --- | --- | --- | --- | --- | --- |
| T0 | 418, 3220, 3232, 3239, 3253, 3260 | 0 | 100 | 15 | 955..1077, -4516..-4421 |
| T3 | 412, 3214, 3218, 3241, 3252, 3256 | 0 | 100 | 15 | 937..1042, -4692..-4592 |
| T4 | 419, 3216, 3230, 3238, 3254, 3262 | 0 | 100 | 15 | 1035..1144, -4527..-4421 |
| T5 | 413, 3226, 3233, 3245, 3249, 3258 | 0 | 100 | 15 | 1032..1129, -4692..-4588 |
| T6 | 414, 3229, 3236, 3246, 3247, 3264 | 0 | 100 | 15 | 1059..1164, -4651..-4561 |
| T7 | 415, 3228, 3235, 3243, 3250, 3265 | 0 | 100 | 15 | 1059..1164, -4564..-4488 |
| T8 | 417, 3231, 3237, 3255, 3259 | 0 | 100 | 10 | 906..1002, -4538..-4431 |
| T9 | 409, 3213, 3217, 3242, 3261 | 0 | 100 | 10 | 906..986, -4601..-4519 |
| T10 | 411, 3215, 3219, 3240, 3251 | 0 | 100 | 10 | 906..1000, -4672..-4572 |
| T12 | 416, 3227, 3234, 3244, 3248, 3263 | 15 | 75 | 15 | 1144..1187, -4564..-4488 |

The other seventeen L9 zones have distinct quads. They are T1, T2, T11, T13, T14, T15, T16, T17, T18, T19, T20, T21, T22, T23, T24, T25, and T26. No move is proposed for them in this pass.

## Section 2 — what a moved or redrawn wing keeps

The lead named L10 T0, L14 T0, L14 T13, and L14 T14 as the candidates for a sideways move or a redrawn wing. These four pages say what that wing would have to preserve. They are not a build order and not a dy. No method is assigned. No producer writes an x,z shift, and no producer redraws a wing. A plan hit is not the same as standing in the region. Chain fixtures here have no height unless a jump record carries one. Owner feet are body height minus 32. Geometry is the same unmoved archive as section 1.

### L10 T0

41 regions, 63 pairs, box x 2668..3899, z -2330..-1728. Six sides: four singles and two floor-0 sheets, 18 regions and 19 regions. The methods note's "20 and 21" is the older split. No side is an end of every pair, which is why section 1 gives this zone no vertical dy. The 200-unit ring holds 236 other regions.

**Doors.** No door, no movable, and no item is tagged to the zone. Tomb door 88, template 22, aim "87", is the door the earned tomb test opens after the charger, and that charger sits outside this box. The fixture array named `door` in `l10_tomb_walk.json` does pass (2728, -2112) and (2704, -1912). Those two plans are the exit-stairs stretch, the same two plans as `l10_blue_walk.json`. A wing keeps them on the walk back toward the surface. The tomb door itself stays outside the box.

**Sightlines.** The 19-region sheet is floor 0, ceiling 130..175. The 18-region sheet is floor 0, corners down to -90, ceiling 100..200. They share plan along the stair departure and at (2728, -2112). Under parts of that plan, cellar region 2729 is floor -150, ceiling -75. Two floor-20 regions carry props: 3906 and 3911. The published L10 show-through frames sit outside this box, so they are not this zone's views. The wing keeps one walkable corridor at floor 0. The cellar stays a layer below that corridor. The blue return checks `player.position.y > 25`, which is the corridor. The one owner pose in the current set, (2760.2, -2133), feet -150, is in 2729, below both sheets, in the plan of both.

**Script points.** No script Vector3 falls in the zone. Five prop records stay at the recorded heights. `prop_123` record 92 at (2757, 0, -2017) and `prop_648` record 436 at (2793, 0, -1776) are in region 792 on the 19-region sheet. `prop_649` record 423 at (3596, 0, -2176) is in region 1876 on that same sheet. `prop_629` record 249 at (3373, 20, -2037) is in 3906, and record 250 at (3046, 20, -2035) is in 3911. Scripts did not match those material strings to an object name. The records and the heights are what a wing keeps.

**Walk order.** On the Emperor-supply loop the player leaves the Emperor stairs going south at x=3207. The zone contains (3207, -2190) on the 19-region sheet, then (3207, -2240) and (3207, -2290) on both sheets. (3207, -2140) is still outside, and (3207, -2350) has already left. The route then goes to the original breach, the blue charger, the two fence jumps, and the gold altar, and it comes back through `yellow_return` and `exit_stairs`. Those returns re-enter the zone only at (2728, -2112) and (2704, -1912), on the floor-0 sheets, with 2729 under them. The blue earned test uses the same exit stairs and requires the body above ground. Silverleaf harvest and the silverleaf return clip the same three stair points, south and then north. The fence-low walk does not enter the zone. The tomb pickup and the tomb `door` array use the same two exit-stairs plans on the way to a door outside the box.

A moved or redrawn wing keeps that order: the stair clip, the long route outside the zone, the exit-stairs return, the five props, and one floor-0 corridor. The supply walk stands on that corridor. The cellar stays below it.

### L14 T0

92 regions, 151 pairs, box x 1205..2234, z -2964..-1826. Seven sides. The roof is 40 regions, floors -120, -103, and -96, ceilings -59..-20, with 27 joins into 22 covered rooms at floors -138, -129, -120, and -71. The other six sides are open patches, floor -100, ceiling 1200. Section 1 found no vertical direction that stays clear of the floor -155 cellars, and no upward direction. The 200-unit ring holds 178 other regions.

**Doors.** No door is inside the zone. Door 90 is (380, 230, -2124), outside the box. `l14_trials.gd` answers "The left-hand door opens onto the ledge maze." The chain opens that door, walks through to about (500, -1960), then takes `maze.entry`, which ends at (1200, -1945). The wing keeps that approach. Door 90 stays with the trial hall. Doors 89 and 88 are the other two trial doors and sit outside this box as well.

**Sightlines.** The body on this route is on the raised ledges. The chain checks `player.position.y > 110` after every step and every jump. Those ledges are regions outside the zone, floors 130..160, open ceilings. Their plans lie on the roof. At the two jump lips the plan lies on the roof and on the 33-region open patch together. The roof is under the route. The six open patches are the open volume those ledges sit in. Five of the six contain no chain point, and they still join the raised floors at 125..164. A wing that fills that open volume, or that lifts the roof into the ledges, closes the route the player is walking. The floor -155 cellars under the roof stay under it. They are a layer below the maze, and they are not its floor.

**Script points.** No script Vector3 and no item. Four `prop_1049` records sit on the roof: 397 at (1568, -128, -2220) in 3564, 398 at (1741, -127, -2218) in 3568, 400 at (1418, -120, -1958) in 3595, and 401 at (1894, -120, -1986) in 3608. Movable 83, template 27, is recorded at (1479, 177, -2461) in 3573. Height 177 is above the roof ceiling, so the record is not a body standing on the roof floor. The plan stays with the room that height belongs to.

**Walk order.** After the entry, the first ledge (1291, -1927) is region 1914, floor 140, outside T0. The next step, (1382, -1944), is in the roof's plan and in region 1913, floor 140, ceiling 240. The step after that, (1473, -1929.5), is L14 T13. Four steps later the route is on the roof's plan again, (1781, -1889) through (1795.5, -2040.5), under open ledges 2113, 2112, 2096, and 2095 (floors 130, 140, 150, and 160). The one jump inside the box is 2095 to 575, gap 155.6, height -15, landing floor 145. The lip (1818, -2077) is covered room 3598 (floor -120, ceiling -20) and open roof 2072 (floor -100). The landing lip (1927, -2188) is covered room 3570 and open roof 1974. Neither lip has a raised quad. The two centres, (1817.25, -2045.5) and (1967.75, -2241.25), and the next two steps stay on the roof's plan under 2095, 575 (floor 145), 576 (floor 135), and 577 (floor 150). The route then leaves the box, reaches the exit hall and the first idol, and comes back by the same ledges in reverse. The return jump uses the same gap, with the landing floor shifted by the height.

Eleven chain plans fall on the roof and two fall on the 33-region patch. Those two are the jump lips, which also fall on the roof. No owner pose falls in a T0 quad. The wing keeps the raised route, the jump, the four roof props, and movable 83's plan. The roof and the open patches stay under that route.

### L14 T13

2 regions, 1 pair, box x 1332..1552, z -1935..-1823. Region 3593 is floor -120, ceiling -20, three joins. Region 2108 is an open roof, floor -100, ceiling 1200. Section 1's drop of 90 lands in the floor -155 cellars 3622, 3623, 3629, 3630, and 3631. That drop is a constraint on a vertical move. No dy is named here. This pass did not recount the 200-unit ring of this small box.

**Doors.** No door, no movable, no item, and no prop.

**Sightlines.** One chain plan, (1473, -1929.5), lies in 3593 and in region 2115 (floor 150, open ceiling 1450). The stack at that plan is those two regions. The chain test requires `player.position.y > 110`, so the body is on 2115. Region 3593 is the covered floor under that footprint. 3593 joins 3587 (floor -71, ceiling -20), 3586 (floor -120, ceiling -45), and 3595 (floor -120, ceiling -20). Region 3595 is on the L14 T0 roof and holds `prop_1049` record 400. The open side joins ledge 2115, room 1916 (floor 140, ceiling 240), open 2107, and ledge 2105 (floor 130). A wing keeps the open air of 2115, the covered room under it, and the join from 3593 into the T0 roof. The body stays on 2115. Region 3593 stays the room below that step.

**Script points.** None.

**Walk order.** In `l14_ledge_maze_walk.json` this point is ledges[2], walk 2115. The step before it is (1382, -1944), on the T0 roof's plan and on region 1913. The step after it is (1558.5, -1914.5), outside this box, on region 2116 (floor 140) with covered room 3587 under that plan. The player is already on the raised route, takes this one step, and continues. The same step is walked again on the way back from the idol. A moved or redrawn wing keeps that one footprint between those two neighbours, at the raised height, with 3593 remaining the room below.

### L14 T14

Regions 2517 and 3185, one pair, area 744.5. The pair box is 3185's box, x 656..1839, z -4945..-4689. Region 2517's own box is x 1478..1604, z -4844..-4719. Region 2517 is floor -50, corners -50..-40, ceiling 30..40, and it joins 2516 (floor about -40) and 2518 (floor about -60). Region 3185 is floor -60, corners -70..-60, ceiling -10..0, and it joins 3472 (floor -70) and 3186 (floor -60). No prop, no item, no movable, and no door. The unmoved separating arithmetic, 2517 down 120 or 3185 down 60, is not a proposal. Region 3185 is the KEEP the T3 dip was capped against. Ramp 2516 is already a T3 delta on the moved pack. The next dy belongs on that pack. This pass did not recount a 200-unit ring for this pair.

**Doors.** None in the zone. Library buttons 146 at (2467, 35, -5291) and 147 at (1923, 35, -4350) are outside the box. After button 148 the chain walks the opened library exit at (1735, -5041.5) and (1845, -5088), south of the box. The hall on the way to button 147 passes region 1517, also outside the box.

**Sightlines.** Three visits share this plan. The bedroom stair, the library, and the niche are the upper visit. Spider and flute are a floor-0 visit over 3185. The stone corridor is the lower visit. At (1583, -4772) the plan is 2517 and region 1352 (floor 30, ceiling 130). At (1583, -4800) it is 2517 and region 1381 (floor 40, ceiling 140). Region 2517's ceiling corners are 30..40, and region 1381's floor is 40, so the upper room meets that ceiling or sits just above it. From (1583, -4826) through (1583, -4907) the plan is 3185 and the stair regions 1379, 1376, 1373, and 1370 (floors 50, 60, 70, and 80). Spider and flute cross 3185 at (1357.5, -4820) on region 1399 and at (1350.5, -4890) on region 1400, both floor 0, ceiling 80. Library crosses at (1725, -4879) on 1514 (floor 50, ceiling 130) and at (1725, -4910) on 1515 (floor 60, ceiling 140). Niche crosses (1625, -4907) on 1369 (floor 80), (1625, -4880) on 1372 (floor 70), and (1625, -4852) on 1377 (floor 60). The small-zones note's route camera `overlap_2517_3185` is (1544, -4826), in both regions' plans. A wing keeps every one of these walks. The lower corridor stays off the floor of the bedroom stair. The upper walk keeps its floor over the stone corridor. Region 3185 stays the KEEP.

**Script points.** `l14_library.gd` button 148 is (1672, 96, -4912). Feet at that height are 64, above 3185's ceiling. The plan is in 3185 and in region 1512 (floor 96, ceiling 108). The button is the upper floor. The exit walk reaches it from (1725, -4879) and (1725, -4910), which stand on 1514 and 1515.

**Walk order.** Chain A reaches this plan before the bedroom. The spider corridor crosses 3185 on 1399 and 1400, then continues south. The flute approach crosses the same two points on the way back. The body there is on the floor-0 rooms. Chain B comes later, from the opened hanging. The upper bedroom route runs south along x=1583, crosses 2517 on floors 30 and 40, crosses 3185 on floors 50 through 80, and leaves the zone at (1583, -4929) onto region 1367, floor 90. The bedroom check is `player.position.y > 145`, past this zone. After the headboard and the crack, the two hall buttons are outside this plan. The library walk then crosses 3185 on the way to button 147, and the library exit walk crosses it again on the way to button 148. The niche approach crosses 3185 on the upper floors and leaves north onto floor 50 and below, over region 2518.

The lower corridor is a separate visit. The owner crawl on 255a2e4 ended at (1531, -10, -4802), feet -42, region 2517, in the stone corridor. The east ramp of that tunnel is (1052, 32, -5546), feet 0, region 2554. This pass's owner reader found one L14_HT pose in the current report set, (1546.9, -4806), feet -43, inside 2517. At that plan the other region is 1380, floor 50, ceiling 140, and the body at feet -43 is inside 2517. The small-zones note counted 29 poses in four bundles inside 2517, sample feet about -9 to -7, and 27 poses in 3185. This pass did not remeasure that older count. A wing keeps the stone corridor at 2517's height, joined to ramp 2516, and keeps the upper stair where the chain walks it.
