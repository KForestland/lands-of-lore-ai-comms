# L14 small overlap zones — measurement for a geometry move (2026-11-13)

Read-only. Godot was not run. Nothing was moved. T3 is not proposed again (lead approved it at 01:49Z). T0 waits. The guard list was not edited.

Sources: true pairs `opus_lane/g05/overlap_true_pairs.json` (364 rows), zone boxes `overlap_zones_true.txt`, geometry `~/lol2_out/all_maps_20260922/L14_HT/geometry/geometry.json` (archive sha256 `c294f9ab142b55c36fff545a1293c419c42353fedefbfe8b77b9c38a2d9a0719`, 4275 regions), faces, props, movables, and markers in that export. Items from `scripts/lol2/act2_items_source.json` on r19-work `dacf85884136`. Owner poses: 18 L14_HT bundles under `playtest_feedback_20261023`, 5993 poses. Chain points: the 17 fixtures the three `l14_temple_chain_*` tests load. Script points: `Vector3` literals in `scripts/lol2/l14*.gd` and `tests/l14*.gd`.

The pair file's floor columns disagree with geometry `floor_base` on 112 of 364 rows, so every floor and ceiling below is the geometry corner span. Pairing the 364 rows by shared region reproduces all 20 zone boxes, pair counts, and region counts in `overlap_zones_true.txt`.

## How a side and a move were measured

A zone is one connected component of the true pairs. A side is a connected component of the neighbour graph inside that zone (an edge if either region lists the other). "Joins" are directed neighbour links from that side to a region outside the zone. Inbound links were counted the same way.

This split reproduces `all_zones_sides.txt` on every two-sided zone, including T3 (sides 24 and 49, span -20..80 against 0..160, 5 joins, down at least 90, up at least 190, nothing below, next floor above at 160). On a tie the side file names one side. This note lists every side.

Open roof: `ceiling_base = floor_base + 1300` on 631 of 4275 regions. That ceiling is the outdoor sentinel (a floor of -100 has ceiling 1200; a floor of 130 has ceiling 1430). It is not a stone ceiling, and it is not a side to drop.

Clearance is 10, the same gap as the approved T3 shift. A shift also has to put the two `floor_base` values more than 48 apart, or the pair stays on the overlap list (the guard's step is 48). The number given is the smallest rigid shift that does both. Free space is a third region whose plan overlaps the side and whose whole body is under the side's lowest floor or over its highest ceiling.

A plan hit is not the same as standing in the region. Where a pose or a chain point is cited, the note says whether the feet (or the only co-holder) are inside that region's floor..ceiling.

Atlas is a plan, so a vertical shift does not move it. What does follow is named per zone: faces, joins (they become ramps), props, items, movables, and script or chain points that sit in the shifted regions. A saved player whose region is one of those, or whose feet are in the old band and not on the unmoved floor, would load at the shifted height. That is the same save consequence already stated for T3. It was not re-derived here.

## The 12 zones

### T2 — trial door 89, west of the three doors

Regions 1305, 1308, 1461, 1463, 1464, 1492, 1493. Box x -153..217, z -2063..-1553. Six pairs, area 51325.

| Side | Regions | Span | Joins out |
| --- | --- | --- | --- |
| smaller (3) | 1461, 1463, 1464 | floor 190, ceiling 270..290 | 2: 1461→1471 (floor 190), 1463→1462 (floor 190) |
| other (4) | 1305, 1308, 1492, 1493 | floor 170..190, ceiling 240..345 | 5, at floors 160 and 190 |

Volumes overlap. Down at least 130, up at least 165. No third floor entirely above or below the smaller side. Faces on the smaller side: 3 floor, 3 ceiling, 6 boundary.

Trial door 89 is only in 1461: `l14_trials.gd` `DOORS["89"]` at (32, 230, -2061), and movable template 24 index 89 at (32, -2061) height 190. That point is not in the other side. Two props (`prop_1049`, records 395 and 396) sit in 1308, which is the side not moved. 1305 and 1308 are also in `l14_tilt.gd` `LOWER_CEILINGS`. No chain fixture point and no owner pose falls in T2.

Proposed move: shift 1461, 1463, 1464 down 130. Ceiling 290 becomes 160, ten under 1308's floor 170, and the floors differ by 110. The two joins, now both at 190, become ramps. Door 89 and movable 89 go with them. Shifting the 4-region side instead would move tilt ceilings 1305 and 1308; that side's upward shift is also 130, so the door is the reason to move the 3-region side and not the tilt ceilings.

### T5 — trial door 90

Regions 1465, 1467, 1468, 1502, 1503. Box x 217..653, z -2195..-1772. Four pairs, area 27290.

Smaller side: 1502, 1503. Floor 190, ceilings 310 and 345. Five joins: 1502→1501 and 1502→1500 (floor 280), 1502→1492, 1503→1494, 1503→1489 (floor 190). Other side: 1465, 1467, 1468, floor 180..190, ceiling 272..290, two joins. Volumes overlap. Down at least 175, up at least 110. Nothing above or below the smaller side. Faces on it: 2 floor, 2 ceiling, 3 interior, 1 boundary. One prop (`prop_1049`, record 393) in 1502.

Door 90 is only in 1465: `DOORS["90"]` at (380, 230, -2124), movable template 24 index 90. The ledge-maze chain point (521.5, -1950.5) lies in both 1467 and 1502. No owner pose.

Proposed move: shift 1502 and 1503 up 110. Floor 190 becomes 300, ten over 1468's ceiling 290. Door 90 stays. Joins at 190 need a ramp of 110; joins 1500 and 1501 are already at 280, so they become a 20 step.

### T6 — trial door 88 (tie, 2 and 2)

Regions 1451, 1456, 1459, 1460. Box x -706..-147, z -2220..-1732. Three pairs, area 23232.

Both sides have two regions. The side file's pick is 1451, 1456: floor 190, ceiling 310..345, five joins (to 1486, 1496, 1492 at floor 190, and to 1454, 1455 at floor 280). The other side is 1459, 1460: floor 180..190, ceiling 270, two joins. Volumes overlap. For 1451/1456, down at least 175, up at least 90. Nothing above that side. Faces: 2 floor, 2 ceiling, 1 boundary, 3 interior. One prop (`prop_1049`, record 394) in 1456.

Door 88 is only in 1459: `DOORS["88"]` at (-305, 230, -2132), movable template 24 index 88. The fire-path chain point (-681, -1776.5) is only in 1460. No owner pose.

Proposed move: shift 1451 and 1456 up 90. Floor 190 becomes 280, ten over ceiling 270, and flush with joins 1454 and 1455. Door 88 stays. The three floor-190 joins need a ramp of 90.

### T8 — tilt hall against a 2-unit lip

Regions 764, 2133, 4028. Box x 3..430, z -1197..612. Two pairs, areas 3163 and 14022.

Count-smaller side is one region, 2133: floor 190, ceiling corners 440 and 590, four joins (2134 and 2683 at floor 190, 2131 at 190, 2129 at 400). The other side is 764 and 4028: floor 180, ceiling 182, five joins (to floors 140 and 160). The volumes do not overlap. The lip's ceiling is 182 and the hall floor is 190, a gap of 8. The floors differ by 10, which is why the pair is still on the list.

Up at least 2 would put the hall ten above the lip and leave the floors 12 apart, so the pair would stay. Up 40 would clear the 48 test (floors 50 apart) and nothing sits above 2133. That shift would lift the whole tilt half. `l14_tilt.gd` treats 2132 and 2133 as the moving floors. 764 and 4028 are in `LOWER_CEILINGS`.

No chain point is in T8. Script points that fall in 2133 (priest ritual, quill, tilt, two tests) are outside the lip quads. Movable template 10 index 95 at (91, 81) height 180 is in both 764 and 2133. Under the hall, the nearest third ceiling is region 758 at 162. Nothing above.

Proposed move: do not shift 2133. Shift 764 and 4028 down 40. Floor 180 becomes 140, fifty below the hall floor, ceiling becomes 142, still under the hall. Joins 761 and 4027 are already floor 140. Joins 767 and 4029 are the same kind of lip at 160..162 and are not in this zone; they would sit 20 above the dropped lip. Faces on the lip: 2 floor, 2 ceiling, 4 interior, 1 boundary.

### T9 — the other tilt half

Regions 766, 2132, 4034. Box x -401..3, z -1197..612. Same shape as T8. 2132 is the hall (floor 190, ceiling 440..590, four joins). 766 and 4034 are the lip (floor 180, ceiling 182). Volumes do not overlap. Nearest ceiling under the hall is region 760 at 162. Nothing above.

`l14_tilt.gd` lifts 2132 (`n.position.y = lift` when `id == 2132`) and lists 766 and 4034 in `LOWER_CEILINGS`. Movable template 10 index 100 at (-24, 70) height 180 is in both 766 and 2132. No chain point. The same script points that fall in the huge quad of 2132 are outside the lip.

Proposed move: shift 766 and 4034 down 40, same as T8. Do not shift 2132.

### T12 — open ground over a ceiling-20 room

Regions 609, 610, 631, 3344, 3357, 3364, 3365, 3366. Box x 2269..2606, z -3002..-2619. Nine pairs, area 7440.

Count-smaller side is 609, 610, 631: floor -100, ceiling 1200. That is the open-roof sentinel, not a room. Five joins, four of them also open roofs, plus 631→632 at floor 145 (ceiling 1445, the same sentinel). The finite side is 3344, 3357, 3364, 3365, 3366: floor -80, ceiling 20, nine joins at floors -80 and -60. Volumes overlap because the open body runs from -100 to 1200. Dropping the open side would be at least 1290. Nothing entirely below the finite side.

Faces on the finite side: 5 floor, 5 ceiling, 3 boundary, 5 interior. No prop and no item is tagged to these regions.

Owner poses land in the open side inside its height: 609 has 12 poses in 7 bundles (sample feet 28.5), 631 has 32 poses in 6 bundles (sample feet 17). Poses whose plan falls in the finite side are standing in another region: the stored 3366 samples are feet 76 at (2476, -2832), which is inside region 952 (floor -15, ceiling 150) and above 3366's ceiling. 3344's samples are feet 52..80. Chain: entry (2415, -2665) is in 609 and region 944 (floor 0), not in the finite room. Priest approach (2483.5, -2776) is in 631 and region 951 (floor -15). Priest approach (2500, -2805) is in 631, 951, and 3366, so that one plan point is on the room being moved. The fixture has no height.

Proposed move: shift the finite side down 130. Ceiling 20 becomes -110, ten under the open floor -100. Do not move 609, 610, or 631. The nine joins become ramps. The priest-approach point in 3366 follows the room.

### T13 — three rooms of three, and a flat sheet at height 20

Regions 18, 19, 20, 835, 837, 838, 3288, 3289, 3432. Box x 2500..2897, z -3749..-3456. Ten pairs, area 5588. Three sides, each of three regions.

| Side | Regions | Span | What it overlaps | Joins |
| --- | --- | --- | --- | --- |
| A | 18, 19, 20 | floor 0, ceiling 80..125 | the sheet only | 4, all at floor 0 |
| B | 835, 837, 838 | floor 0, ceiling 80..110 | the sheet only | 7, all at floor 0 |
| sheet | 3288, 3289, 3432 | floor 20, ceiling 20, flag 514 | A and B | 8, down to floors -80 and -50 |

A and B do not overlap each other. The side file's "smaller span 0..110, down at least 120, other 0..125" is side B measured against the union of the other spans. B's own pairs are only with the sheet, whose body is the plane at 20. A 120 drop is the cost of burying B under A, which it does not meet.

The sheet has 3 floor faces and 3 ceiling faces and no wall. Niche and shard-bowl chain point (2646, -3550) is in 835 and in 3432. Owner poses: 837, 838, and 3432, 11 poses each. Stored samples at (2599, -3554) and (2629, -3532) have feet 83 and 59, inside B's room and above the sheet. Route camera `overlap_837_3432` is the same plan. Side A's owner samples at feet -48 are inside region 3278 (floor -80, ceiling 20), below A's floor, so those poses are the lower room showing through A's quad.

Proposed move: shift the sheet down 70. Floor and ceiling 20 become -50, which is more than 48 from the room floors at 0 and ten under those floors. The -50 joins are then level; the -80 joins stay a step down. Sides A and B, including the chain point's room 835, stay. Nearest third ceiling under B is region 3428 at -4; the sheet's own footprint has no third region entirely below it.

### T14 — r36 / 3890, plus a one-region pocket

Regions 36, 38, 3882, 3889, 3890, 3894, 3902, 3906. Box x 3139..3382, z -3653..-3251. Seven pairs, area 3509. Region 36 is in this zone. Three sides.

Count-smaller side is 3902 alone. Floor -80, ceiling corners -49 and -31, flag 522. It overlaps only region 36, area 39. Four joins: 3901 (floor -55), 3898 and 3880 (floor -30), 3899 (floor -80). Down at least 59, up at least 180. Nothing below. Next floor above the footprint is region 14 at 0. Faces: 1 floor, 1 ceiling, 3 interior. `l14_machines.gd` `INSERT` is (3257, -55, -3615), inside 3902. The target id on that script is `temple:machine3902`. No owner pose is in 3902.

That pocket is not the r36/3890 overlap. Those are the other two sides, both floor -80:

- 36 and 38, ceiling 90. Three joins: 36→35 and 38→37 at floor 55 (flag 531, bit 0 set), and 38→40 at floor -80. Reachable from the arrivals along some neighbour path. A walk that refuses flag bit 0 does not reach them, because 35 and 37 have that bit.
- 3882, 3889, 3890, 3894, 3906, ceiling 20. Eight joins at floors -80, -30, and 20. Reachable without crossing bit 0.

Volumes overlap. Separating them is down at least 110 for the ceiling-20 side, or up at least 110 for 36/38. Up for the ceiling-20 side is blocked by region 35 at floor 55 over that footprint. Nothing is entirely above ceiling 90.

Chain point (3319, -3507) is in 36 and 3882 (`l14_machines_walk.json` and `l14_bedroom_approach.json`). Chain point (3208.5, -3487) is in 3890 and region 26 (floor 0, ceiling 125), not in 36. Owner stood in both 36 and 3890 at once: (3299, -3536.5), feet -48, bundle `report_2026-11-12T06-31-54_583141606`. Also walked: 3890 (10 poses, 5 bundles), 3882 (9/5), 3906 (3/1), 3889 (3/1), 3894 (1). Not 38.

Proposed moves, both required if the whole zone is to leave the list:

1. Shift 3902 down 60. Ceiling -31 becomes -91, ten under region 36's floor. The machine insert goes with it. This does not separate 36 from 3890.
2. Shift 3882, 3889, 3890, 3894, 3906 down 110. Ceiling 20 becomes -90, ten under the shared floor -80. Region 36 stays, so the owner pose at feet -48 stays in 36 and leaves the ceiling-20 body. The chain point in 3882 follows the drop. Eight joins become ramps.

### T15 — region 34 over a ceiling-20 run

Regions 34, 3874, 3877, 3879, 3884. Box x 3167..3383, z -3847..-3659. Four pairs, area 3259.

Smaller side is 34. Floor -80, ceiling 90. One join, 34→33, floor 55, flag 531 (bit 0 set). Same reach pattern as region 36: the open neighbour walk reaches it; the bit-0-refusing walk does not. Other side: 3874, 3877, 3879, 3884, floor -80, ceiling 20, nine joins at -80, -30, and 20. Volumes overlap. For region 34, down at least 180, up at least 110. Nothing entirely above ceiling 90. The ceiling-20 side has region 33 at floor 55 above it, so raising that side is blocked. Faces on 34: 1 floor, 1 ceiling, 3 boundary.

Owner pose (3323.4, -3701.2), feet -48, is in both 34 and 3877 (one pose). Also 3874 and 3877, three poses each, and 3879, two poses, all one bundle. No chain fixture. Route camera `overlap_34_3874` is (3314.9, -3740.8), in both quads. Hits on the number 34 in other scripts are `canvas.layer = 34`, not this region.

Proposed move: shift region 34 up 110. Floor -80 becomes 30, ten over the other ceiling 20. The join to 33 stays a step (33 is floor 55) and is still flag bit 0. The four-region side stays, so the owner pose leaves 34's body only if 34 is the region being shifted; the pose is in both, so after the shift the feet at -48 remain in the ceiling-20 side.

### T16 — open roof over a floor -120 piece (tie, 1 and 1)

Regions 2108 and 3593. One pair, area 1196. Box x 1332..1552, z -1935..-1823.

2108 is the open roof: floor -100, ceiling 1200, four joins (2105 at 130, 2107 at -100, 1916 at 140, 2115 at 150). 3593 is floor -120, ceiling -20, three joins (3587 floor about -71, 3586 and 3595 at -120). The side file's pick is 3593. Volumes overlap between -100 and -20. For 3593, down at least 90, up at least 1330 (that up figure is the open sentinel). Nothing below 3593. Next floor above it is 2105 at 130. No owner pose. Faces on 3593: 1 floor, 1 ceiling, 1 boundary, 1 interior.

Ledge-maze chain point (1473, -1929.5) is in 3593 and in region 2115 (floor 150, ceiling 1450). It is outside 2108's box. The fixture has no height, so the point is the low piece and a high neighbour at once.

Proposed move: shift 3593 down 90. Ceiling -20 becomes -110, ten under the open floor -100. Do not move 2108. The three joins become ramps. The ledge-maze plan point follows 3593; 2115 stays.

### T17 — a small quad on a large one (tie, 1 and 1)

Regions 2517 and 3185. One pair, area 744. Box of the pair x 656..1839, z -4945..-4689, which is 3185's box. 2517's own box is x 1478..1604, z -4844..-4719.

2517: floor corners -50..-40, ceiling 30..40, flag 21004, two joins (2516 floor about -40, 2518 floor about -60). 3185: floor corners -70..-60, ceiling -10..0, flag 20492, two joins (3472 and 3186). The side file's span -70..0 is 3185. Volumes overlap. For 2517, down at least 120, up at least 60. Up is blocked: region 1381, floor 40, is already the next floor over 2517, and a 60 rise would enter it. Nothing below 2517.

Owner: 29 poses in 4 bundles inside 2517, stored samples feet about -9 to -7, which is inside 2517's height. 3185 has 27 poses; the sample at feet -9 is inside its ceiling band, and samples at feet 107 and 150 are region 1370 (floor 80, ceiling 180) showing through 3185's plan. Chain: bedroom approach (1583, -4772) is in 2517 and region 1352 (floor 30), not in 3185. Hanging-spider, flute-approach, library, and niche points are in 3185 and another region, not in 2517. Route camera `overlap_2517_3185` is (1544, -4826), in both. Faces on 2517: 1 floor, 1 ceiling, 2 boundary. No prop, no item.

Proposed move: shift 2517 down 120. Ceiling 40 becomes -80, ten under 3185's floor -70. 3185 stays, so the spider, flute, library, and niche points stay. The bedroom point and the owner poses in 2517 follow the drop. Two joins become ramps.

### T18 — a five-region knot on the -80 corridor

Regions 321, 322, 355, 373, 374, 3268, 3418. Box x 2585..2828, z -3884..-3757. Seven pairs, area 255. Every pair area is between 14 and 103; the sum is the whole zone.

Count-smaller side is the corridor: 3268, 3418, floor -80, ceiling 20, four joins, all at floor -80. The other side is five tiny regions around x 2664..2698, z -3884..-3864: floor -70, ceiling 60, ten joins at -70 and -20. Volumes overlap. For the corridor, down at least 100, up at least 150. Under it, region 3390's ceiling is -389, so a 100 drop is empty. Over the corridor, region 340 is floor 20. The knot has nothing entirely above or below it. Knot faces: 5 floor, 5 ceiling, 5 interior. Corridor faces: 2 floor, 2 ceiling, 2 boundary. No prop is tagged to either side.

The knot has no chain point and no owner pose. The corridor does, in plan only. Stored owner samples (48 poses, 5 bundles) at (2748, -3799) are feet 52, inside region 1443 (floor -20, ceiling 80) and above 3268's ceiling. Chain points in 3268 also lie in 372 or 1444, and the ones checked are outside the knot's quads. `l14_lower_passage.gd` has (2800, 0, -3800), in 3268 and 1444, also outside the knot. A hit on the number 322 in a fire-path test is a deck height, not region 322. A hit on 3268 in `l14_hall_clear.gd` is the z of a camera at (2926, 42, -3268), not region 3268.

Proposed move: shift the knot (321, 322, 355, 373, 374) up 100. Floor -70 becomes 30, ten over the corridor ceiling 20. The corridor stays, so the chain plan and the owner poses stay. Ten joins become ramps. Count says the corridor is the smaller side; it is the walked piece, and the knot is the whole of the overlap area, so the shift is the knot.

## The six no-join zones

Reachability is a directed walk: from the four arrivals (regions 796, 864, 2282, 4176) along each region's neighbour words. That walk reaches 4169 of 4275 regions. A second walk that refuses to enter flag bit 0 was used only as a note on regions 34, 36, and 38. No `l14*.gd` script names these orphan ids, and no other script teleports the player to them. The id appears in the region table and the overlap list, and the item rows below. It does not appear as a warp.

Each orphan's four neighbour words are -1, and no outside region lists it. So the walk cannot enter it. A pose can still have its plan inside the orphan, because the orphan shares that plan with a reached region. That is the overlap, not a path.

| Zone | Orphan | Span | Reached from an arrival | What shares the plan | Owner / chain on the orphan's quad |
| --- | --- | --- | --- | --- | --- |
| T1 | 4106 | floor 0, ceiling 64 | no | prop `prop_574` record 81 at (277, 0, 2058) is also in reached 2304 (floor 0, ceiling 380) | neither |
| T4 | 4073 | floor -96, ceiling -59 | no | items in reached 534 as well as 4073 | chain point (3295, -2611) is in 4073 and in reached 548 (floor 160); no owner pose |
| T7 | 4062 | floor -100, ceiling -80 | no | prop `prop_529` record 157 at (2310, -100, -2136) is also in reached 1970 and in 4043 | neither |
| T10 | 4043, not 660 | floor 0, ceiling 64 | no | prop `prop_574` record 159 at (2306, 0, -2191) is also in reached 606 and in 4062 | no pose in 4043 |
| T11 | 4074 | floor 0, ceiling 64 | no | prop `prop_1059` record 85 at (1966, 0, -3931) is also in reached 961 | owner poses and one chain point, see below |
| T19 | 2329 and 3219 | 2329 is 0..64; 3219 is 0..300 | neither | four `prop_1049` records 365–368 are only in 2329 | neither |

T4's items, all tagged region 4073, height -96, and also inside 534 (floor -100, ceiling 1200): row 1 Dreamstone (3264, -2664), row 4 Cry shard (3211, -2681), row 5 Jkar idol (3212, -2731), row 6 Statuette (3242, -2711). The open side 533–536 is reached. The orphan is not.

T10 is three sides, not one orphan plus a room. 4043 is the 0-join region. 660 is a different one-region side, floor 11, ceiling 1311 (open roof), four joins, and it is reached. 863 and 864 are floor 0, ceiling 80. 864 joins 942 and is arrival selector 1. Owner: 34 poses in 6 bundles on 864, sample feet 32. Chain entry (2415, -2486) is on 864. Those are the reached side.

T11: shard-bowl chain point (1960.5, -3946.1) is in 959 and 4074. Owner sample (2005.3, -3913.7), feet 32, is in 961 and 4074, inside both heights. Further owner poses on the reached side: 961 (13 poses, 6 bundles), 1073 (31/5), 959 (4/4), 1067 (4/4), and 11 poses in 5 bundles whose plan is inside 4074. The neighbour walk still does not enter 4074. The owner was on 961, in the overlap.

T19: both regions are orphans. The four props are not in 3219 and not in any other region. Nothing walked there.

These six are not given a move. The reached side of T1, T4, T7, T10, and T11 is real ground (T4 and T7 are open roofs with a finite orphan laid on them). T19 has no reached side. Dropping any of them from the guard list is a later decision; this note only measures the walk.

## Not in this note

T3 stays the approved tunnel shift. T0 (92 regions, seven sides, open roofs at -100 and -120) was not studied. The slab-to-pew path and the r36-versus-3890 order note are already posted; T14 above is the overlap measurement, not a replacement for either.
