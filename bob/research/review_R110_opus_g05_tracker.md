# R110. Temple region tracker at 0f600bd

Read-only. Branch `opus/g05-tracker-l14-20261112`, worktree `~/opus_work/shards/lol2_shard_2`, head `0f600bd44c7637aad98259a7e5282023fd190f60`. The range `8a53cce..0f600bd` is six commits: `d58bebb` (wall 8416 band −80..0, pew waypoints, ledger 0633), `8a71298`, `87652e1`, `90dd0f1`, `6919aca`, `0f600bd`. Fifteen files, +3265/−12. Compared with `grok_research/REGION_STACK_MOVER_20261112.md`. Pinned `DAT/L14_HT.MIX` sha256 `c294f9ab142b55c36fff545a1293c419c42353fedefbfe8b77b9c38a2d9a0719`. Geometry file offset `11406344`, region stride `0x2C` at geometry `0x1CCFA`, 4275 regions. This pass did not launch Godot.

`TRACKER_AREAS` is `L14_HT` only. Meta `lol2_region_tracker_off` leaves the tracker off. The shipped table is `scripts/lol2/region_mover/L14_HT.json`, source sha prefix `c294f9ab142b55c3`.

## 1. The stacked-floor rule

`tracker_tick` keeps the tracked region while the plan point is inside its four-vertex quad. The test is `Geometry2D.is_point_in_polygon` on x and z.

`_tracker_step` reads the four neighbour words in slot order. The search is breadth-first, up to `TRACKER_HOPS` (3), through neighbours the segment crosses. The finder at `0xF40AC` tries the four slots of the current hint once. A miss halves the step. The 3-hop search can accept a neighbour's neighbour. That is wider than one finder step.

Flag bit `0x20` and the run word are unread. `act2_map.gd` has no read of `row[4]`. Flag bit `0x80` is skipped by `_tracker_pick` and is never a reason to keep a record. The shipped L14 table has 0 regions with bit `0x20`, 0 with bit `0x80`, and 0 nonempty runs. Those two walks have no L14 record to act on.

The finder does not read the floor word when it chooses. The guard accepts a landing when the interpolated floor at the end point is at or below the feet plus 48, or when the region is in `floor_decks` or `floor_motion`. A higher landing is refused. Equal floors in a fresh pick keep the earliest record. A plan move over 150, a point outside the quad, or feet more than 64 from the tracked floor picks again. Ledger 0637 names this feet rule.

## 2. The 560 pairs

`tools/prepare_region_mover.py` lists a pair when the clipped area is above 4, the base floors differ by at most 48, neither region lists the other, and neither has bit `0x80`. `L14_HT_overlaps.json` has 560 pairs and 389 regions.

A full scan of those 560 against the shipped table: 0 neighbour links either way, 0 floor gaps over 48, 0 with bit `0x80`, 0 with bit `0x20`, 0 with a fresh clip area of 4 or below. 68 pairs share a floor. 473 differ by 8 to 48. 228 have slope bit `0x04` on one side. Two of those share a floor: 1451/1459, area 463.6, and 1456/1459, area 5485.8, both floor 190, flags `0x0200`/`0x0214` and `0xc208`/`0x0214`. Neither pair names the other. Two stored areas differ from a fresh clip by under 0.4 (559/1317, 3392.5 against 3392.2; 586/1317, 176.8 against 176.5). Both stay far above 4.

Ten pairs, indices 15, 55, 111, 167, 223, 279, 335, 391, 447, and 503, were read from the MIX. Floor word `+0x14`, flags `+0x1C`, the four neighbour words, and the four vertices match the table on every record. None of the ten lists the other.

| Index | Pair | Area | Floors | Flags |
| --- | --- | --- | --- | --- |
| 15 | 36 / 3890 | 1089.6 | −80 / −80 | `0x0200` / `0x0200` |
| 55 | 562 / 3573 | 1603.9 | −100 / −120 | `0x0200` / `0x0200` |
| 111 | 592 / 3584 | 1033.4 | −100 / −120 | `0x0200` / `0x0200` |
| 167 | 959 / 4074 | 3216.6 | 0 / 0 | `0x0200` / `0x0200` |
| 223 | 1976 / 3563 | 3600.5 | −100 / −120 | `0x0200` / `0x0200` |
| 279 | 2093 / 3609 | 409.0 | −100 / −120 | `0x0200` / `0xc208` |
| 335 | 2133 / 4026 | 15118.5 | 190 / 160 | `0x020c` / `0x0200` |
| 391 | 2525 / 2707 | 181.9 | 45 / 0 | `0xa20c` / `0x0200` |
| 447 | 2527 / 2773 | 190.5 | 45 / 0 | `0xa20c` / `0x0200` |
| 503 | 2534 / 2771 | 108.5 | 0 / 0 | `0x0200` / `0x0200` |

Region 4074's four neighbour words are empty. Pair 2133/4026 is a slope at 190 over a flat at 160. Pairs 2525/2707 and 2527/2773 are slopes at 45 over flats at 0. Pair 36/3901, inside the 560 and outside this ten, is floors −80/−55, area 1079.8, flags `0x0200`/`0x0202`, and neither names the other. No pair in the scan is a neighbour step.

## 3. Steps the guard can refuse

`_tracker_guard` returns at once when the from-region is absent from `overlap_regions`, when that region is in `floor_decks` or `floor_motion`, or when the feet are more than 48 from its static floor.

The library stair is outside the list: 2358 floor 10, neighbours include 1567; 1567 floor 105, neighbours include 2358. The gallery is outside the list: 2638 floor 340, neighbours include 2640; 2640 floor 428. Slab 164 (floor −80) and pew 856 (floor 0) are outside the list. Region 3264 is outside the list, so the guard does not judge the chain walk off that empty slot. No script under `scripts/lol2` with an L14 name writes `floor_motion`.

The feet rule still refuses a linked neighbour when every corner of that neighbour is more than 48 above the overlap region's floor and the body is within 48 of that floor. There are 108 such links, from 78 overlap regions. On 104 of the from-regions, flag bits `0x01` and `0x02` are both clear, so the finder's per-step reject does not apply to them. The finder would enter the neighbour. The smallest are six rises of 49, regions 3593, 3595, 3597, 3598, 3606, and 3608 (floor −120) onto slopes whose low corner is −71, and flat rises of 50. Region 321 is on the list, floor −70, flags `0x0200`, corners all −70, and it names 328 and 372. Both are floor −20, flags `0x0200`, corners all −20, and both are off the list. A step from 321 into 328 or 372 is refused while the body is within 48 of −70.

Region 36 to 35 is one of the 108. Region 35 is floor 55, flags `0x0213`, corners all 55. The spot test requires that refusal. The lowered stairs, the gallery descent, and a deck registered in `floor_decks` or `floor_motion` stay outside the guard.

## 4. Camera in one region, body in another

The play camera is a child of the body (`jungle_review.gd` adds it to the player). `player_form_body.gd` and `act2_body_fit.gd` write `camera.position.y` only. Standing eye 42 and crouch eye 28 are both measured from the same body origin, minus the 32-unit foot offset, so the crouch eye is 4 below that origin and the standing eye is 10 above it. The plan point stays the body's origin. A crouch or a ledge does not move the play camera into another plan region.

`tracked_region_for` returns the tracked region while the camera plan point is inside that quad. A point outside the quad returns −1, and `region_visibility.compute` then starts from `_region_of` (progression `region_at`, or the nearest nav floor). A free camera or a render pose outside the quad can start on the other sheet.

`apply_save` sets `tracked_region` from the saved key when the body is still inside that quad, before it returns. The camera's plan point is the body's, so the first drawn frame of a save that kept the key starts in that region. The test calls `tracked_region_for` on the body plus 42 up, which shares the body's plan point.

## 5. Saves

The new key is optional `player.region`. A missing key passes validation. A present key must be an integer from 0 through 65535. `snapshot_host` writes it when `region_collision_enabled` or `tracker_on` is true and `last_collision_region` is at least 0. L10 is absent from `TRACKER_AREAS`, so a save there writes no new key.

A missing key loads as −1 and the pick runs. At Godot (3311, −3519), stored (3311, 3519), the only two quads are 36 and 3890, both floor −80, and the pick keeps 36. The null-hint scan in `TEMPLE_R36_3890_20261112.md` returns 36 at that point as well. An old save standing there loads as 36, and the west edge then blocks. A new save writes the key. The test saves while tracked in 3890 inside the overlap and requires the load to stay 3890.

At the test's west start, Godot (3316, −3600), the pick is 3901 (floor −55) over 36 (floor −80). The test assigns `tracked_region = 36` before that walk.

## 6. The test

`tests/l14_region_tracker_test.gd` is headless, registry order 1353. Each check calls `fail` and `quit(1)`. The walk calls `move_grounded`, and that function runs `tracker_tick` and `_tracker_guard` on L14. The test sets `original_game_verified`, turns `physics_process` off, and assigns `tracked_region = 36` for the west cases. It presses no keys. This pass did not re-run it. Opus's PASS line is unread here. A missed assertion exits 1.

## The included wall commit

`d58bebb` adds wall 8416 as a band from −80 to 0 under region 821, and moves the pew waypoints in `l14_temple_chain_a` and `l14_priest_supplies_earned_test` through (2436, −3445) and (2540, −3420). The narrow test expects the lower ray to stop and the upper ray at height 30 to pass. Opus's READY still has `l14_temple_chain_a` as the one open L14 route. Region 3264 is outside this guard. The floor-0 sheet from region 856 is the posted measuring note.

## Before merge

The ledger file on this branch is `docs/deviations/0637-row-2026-11-12-g05-region-tracker-l14.md`. Sol reserved 0637–0640 on the board at 21:30Z. r19-work at `8a53cce` has 0632, 0633, 0634, and 0636, and has no 0637 file. The lead already told Opus to take the next free number after that block.

The ten Temple route poses are still unrendered. The lead asked for them before merge. This review did not render them.

The 108 linked rises sit past the approved 48 cutoff. They are reported in section 3. This verdict does not add a third code change for them.

VERDICT: MERGE AFTER FIXES
