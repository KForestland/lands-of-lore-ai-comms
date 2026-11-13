# R114. L14 T14 trench floor raise at b2b698c

Read-only. Branch `opus/l14-small-zones-20261113`. Head `b2b698c8cb9969d7690526799cbecf46867c1cb9`. Parent `128ff7f77cf5e804678a6946056fc99169838999` is the T3 head R112 marked MERGE. One commit. Godot was not run. The pair lists were recomputed with `tools/prepare_region_mover.py` from this head against the pinned L14 geometry. The frames are `opus_lane/g05/t14`.

The move is the floor-only raise the lead accepted at 03:09Z. Regions 34, 36, 38, and 40 go from floor -80 to floor 25. The ceiling stays 90. The four sill openings become collision, drawing unchanged.

## a) Overlap pairs

A pair counts when the plan area is over 4, the base floors differ by at most 48, neither region lists the other, neither has flag 0x80, and the floor-to-ceiling spaces meet over the overlap.

Recount, and the moved list matches the file committed at this head (316 pairs):

- Native geometry, rule 5, no move: 528 pairs. Region 36 with 3890 is a pair, area 1089.6.
- Trench against the corridor, before the raise, 14 pairs: 34/3874 area 739.0, 34/3877 area 928.9, 34/3879 area 471.6, 34/3884 area 1119.1, 36/3882 area 636.6, 36/3890 area 1089.6, 36/3894 area 586.0, 36/3897 area 597.3, 36/3901 area 1079.8, 36/3902 area 39.0, 36/3905 area 361.9, 36/3906 area 974.5, 38/3889 area 12.5, 38/3906 area 171.2. After the raise: 0. Region 40 is in the raised set. It had no rule-5 pair before and none after.
- Corridor 3890 stays floor -80, ceiling 20. The trench floor is 25 and its ceiling is 90, so the two volumes do not meet. 3890 is not an overlap region after the move.
- Pairs that still touch the T3 moved set are the same two R112 left in place, and the areas match the unmoved table: ramp 2516 with corridor 3185 area 6319.8, and ramp 2519 with 3185 area 2136.0.
- T3 `corner_deltas` are unchanged from `128ff7f`. The new floor deltas are +105 on 34, 36, 38, and 40, all four corners. Their ceiling deltas are 0. The sill regions 33, 35, 37, and 39 are not keys.

## b) What the frames show

Four cameras, each 42 above the hall floor, aimed at one sill. `sill_33_to_trench_34`, `sill_35_to_trench_36`, `sill_37_to_trench_38`, and `sill_39_to_trench_40`. Each before file is the same bytes as its after file. The sheet shows the hall's wooden wall, carved panels, a black window opening, and the stone ceiling above. The trench floor is not in that view. There is no new gap, seam, or floating piece in the wood. The black opening is the window that was already there.

In the moved pack, which matches `outputs.pack` `88df268cbdb73fd6bcfea689ec5366eed1bcdc406148ea3a8b25c22b3361d28a`:

- Four trench floors move from -80 to 25. Sixteen trench walls move only the points that sat on the old floor. Those points go to 25. Points that were already above -80 stay, including the tops at 55 and 90. No trench ceiling point moves.
- Wall 8260, region 36, was the sheet at x 3298 from y -80 to 55, z -3650 to -3446. It now runs from y 25 to 55. It no longer occupies the corridor band -80 to 20.
- No face of the corridor regions, the four sills, or hall region 26 changes a point.

## c) Spider passage

`l14_spider_passage.gd` is unchanged from `dacf858`. The wake point and actor 68 stay in region 2568. 2568 is not a delta key. This commit does not move that passage, so its gate and spawn heights stay where they were.

## d) Meta switch off

`geometry_move.gd` and `apply_save` are unchanged in this commit. `spec()` returns an empty dictionary when scene-tree meta `lol2_geometry_move_off` is set, and `pack_path` then returns `area.json`. That file's sha256 is `0653fedcb349bda3f9e51b4a6640056d31efa4caa0e25f5e0a4addf2ec5332a1`, the same as `inputs.pack`, and the same pin R112 checked against `dacf858`. The moved pack is not read while that switch is off.

The sill bands are a second switch. `lol2_height_boundary_off` skips the packet. With only the geometry switch off, the sill polygons stay. The deviation row says the same thing. The tracker test sets the geometry switch so it still exercises the original 36/3890 overlap.

## e) Old-save carry

`apply_save` adds `delta()` only when the saved region is at least 0, the spec is live, and `player.geometry_move` is not the moved pack hash. `delta()` is 0 unless that region is a key of `corner_deltas`. None of the corridor ids in the 14 pairs is a key. A save whose region is 3890 stays at its saved height. A save whose region is 36 is carried up 105.

The owner plan (3299, -3536.5) lies in both 36 and 3890. The saved region decides, as it did for the tunnel and the room in R112. The test start (3262, -3520) lies only in 3890.

## f) Sills, player, bands 55 to 75

The height-boundary packet keeps the same 6 `block_face_keys`. Collision polygons go from 1 to 5. The old polygon is region 163, y -80 to 0, and it is unchanged. The four new polygons are the sill openings:

- 33 to 34, y 55 and 75, x 3298 to 3301, z -3793 to -3699
- 35 to 36, y 55 and 75, x 3298, z -3611 to -3517
- 37 to 38, y 55 and 75, x 3193 to 3265, z -3410 to -3340
- 39 to 40, y 55 and 75, x 3003 to 3091, z -3269 to -3238

They are polygons on the existing `HeightBoundaryCollision` body. That body is the same default static body the other named walls use. Its layer is 1. This commit does not give it a separate player-only bit. A mover that already meets those walls meets these bands. The packet's map hash is the original pack hash, so the check against the moved pack still uses the original hash. Drawing does not change.

## g) Corridor under the trench

After the raise, 3890 is not an overlap region, so the tracker guard does not refuse a step out of it. At z -3520 the segment from x 3262 to x 3313 stays inside 3890 the whole way. From x 3300 that plan also lies in 36. The tracked region stays 3890 while the point remains in 3890. Wall 8260 no longer fills the corridor height, and the new sill polygons start at y 55, above that corridor. The narrow test's older ray at y -50 through 3890 is still the assertion that this band is open. Godot was not run. The walk in `l14_small_zones_test` was not re-run.

VERDICT: MERGE
