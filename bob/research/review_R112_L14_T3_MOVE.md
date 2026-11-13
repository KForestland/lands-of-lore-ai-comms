# R112. L14 T3 tunnel move at 128ff7f

Read-only. Branch `opus/l14-t3-tunnel-move-20261113`. Review head `128ff7f77cf5e804678a6946056fc99169838999`. Parent `f1b7378441a2ec62d2ca461b34a60a127543cc7f` is the head named in the 03:01Z assignment. The 03:05Z board line moved the review to `128ff7f`. That commit is overlap rule 5 on top of the shaped dip. Base `dacf85884136f9dbdb224e255077636b9c2ef99e`. Godot was not run. The crawl test was not re-run. The pair lists were recomputed with `tools/prepare_region_mover.py` from this head against the pinned L14 geometry. The frames are `opus_lane/g05/t3`.

## a) Overlap pairs

A pair counts when the plan area is over 4, the base floors differ by at most 48, neither region lists the other, neither has flag 0x80, and the floor-to-ceiling spaces meet somewhere over that plan.

Recount, and both lists match the files committed at this head:

- Native geometry, rule 5, no move: 528 pairs. `dacf858`, without rule 5, is 560. Region 36 with 3890 is still a pair, area 1089.6.
- Moved corners (the spec's 31 `corner_deltas` added to floor and ceiling): 330 pairs.
- One end in the 24 moved regions or the 7 ramp regions, the other in the 79 room regions: 198 before the move, 0 after. 528 minus those 198 is 330.
- Pairs that still touch the moved set: ramp 2516 with corridor 3185, area 6319.8, and ramp 2519 with 3185, area 2136.0. Both areas are the same on `dacf858`. Corridor 3185 is the layout option A was told to leave. The room ids and the delta keys are disjoint.

`f1b7378` still counted 153 tunnel-room pairs, because it predates rule 5. Those volumes no longer meet once the dip is applied, so they leave the list at `128ff7f`.

A grid of points that lie in both a moved quad and a room quad does not find the tunnel ceiling above the room floor. Corners that lie inside a room stay at least 5 under that floor. One clip-edge sample, region 2538 against room 2685, sits about 3.6 under the floor and still clear of it. No shared plan vertex among the 31 regions carries two different deltas.

## b) What the frames show

Coordinates are the on-screen HUD. They match `poses.json`. The yellow region tag on two frames does not contain the camera plan, so the regions below are the quads that do.

Pose 1, (1273, -5066), height 0. Before: the rock crawl fills the view. The plan is in tunnel 2529 and in room 2768. After: the wooden room, a run of carved panels, a door, and the stone walls. No rock tunnel and no hole in the floor.

Pose 2, (1388, -5076), height 0. The before file and the after file are the same bytes. Both show the wooden room: beams, a table, and a bench, on room 2768. This yaw does not look into the tunnel.

Pose 3, (1400, -5010), height 0. The before file and the after file are the same bytes. Both show the wooden floor and a stone wall. No opening. The plan is in tunnel 2520 and in rooms 2726 and 2795.

Pose 4, (1030, -5240), height 0. Before: the rock tunnel. The plan is in tunnel 2539 and in room 2687. After: the wooden floor and the stone wall. No hole and no floating piece.

West ramp, (1478, -4918). The plan is in ramp 2519. Before is the level rock tunnel at height 0. After, the tunnel slopes down and keeps going. Floor and ceiling stay one tunnel. Near-black pixels are 8.7 percent before and 8.6 percent after. That is the stone mortar.

Under the room, (1214, -5082), height -85, region 2535. After is a rock tunnel. The moved floor there is -85 and the moved ceiling is -5. The room floor above is 0. The wooden room is not visible from this point.

Toward the east ramp, (998, -5252), height -90.3, region 2545. After, the rock tunnel rises ahead. The ceiling is closed.

East ramp back, (1023, -5464), region 2546. Before is the level rock tunnel at height 0. After, the same tunnel slopes up, height -63.2. Near-black pixels are 8.3 percent before and 7.8 percent after. It reads as the tunnel going on.

The seven ramp regions are 2516, 2519, 2541, 2544, 2546, 2548, and 2551. The five joins are 2521 to 2519, 2538 to 2544, 2538 to 2548, 2542 to 2541, and 2545 to 2544. The frames cover the west ramp, the dip, and the east ramp. They do not show a black gap, an open seam, or a piece floating off the tunnel.

## c) Spider passage

`l14_spider_passage.gd` is unchanged from `dacf858`. The wake point is (1351, 40, -5396). Actor 68 is at (1364, 0, -5442). Both plans lie only in region 2568, floor 0, ceiling 80. 2568 is not one of the 31 moved regions. Its neighbours are 2788, 2564, 2569, and 2567, and none of those are moved. The four crumbling-wall faces (static assembly 64) run from height 0 to 80 and carry no region tag, so the producer leaves them. The gate, the spawn, and the wake point stay at the height of the passage they stand in. The dipped tunnel does not reach this passage.

## d) Meta switch off

`geometry_move.gd` `spec()` returns an empty dictionary when scene-tree meta `lol2_geometry_move_off` is set. `pack_path` then returns the original path, `assets/lol2/generated/maps/L14_HT/area.json`. That file is gitignored. Its sha256 on the `dacf858` worktree is `0653fedcb349bda3f9e51b4a6640056d31efa4caa0e25f5e0a4addf2ec5332a1`, the same on the later worktree, and the same as `inputs.pack` in the spec. The original creature-nav hash matches `inputs.nav`. A hash mismatch on the moved pack also returns the original path.

The moved pack is not in the commit. The copy on the small-zones worktree hashes to `88df268cbdb73fd6bcfea689ec5366eed1bcdc406148ea3a8b25c22b3361d28a`, which is the later T14 spec. This head pins `outputs.pack` `058a179b90c5b5f75c65ca23056794292cf069863722673d69410e6720cc9a79`. This head refuses the T14 file and loads the original until the T3 pack is regenerated. The off switch does not read the moved file.

Rule 5 is also in the unmoved tracker table (560 pairs to 528). With the move off, the game loads that table. The map pack it loads is the `dacf858` pack. `mover_path` checks that the moved tracker file exists and does not check its hash.

## e) Old-save carry

`apply_save` adds `delta()` to the saved height only when the saved region is at least 0, the spec is live, and `player.geometry_move` is not the moved pack hash. `delta()` returns 0 unless that region id is a key of `corner_deltas`. The 79 room ids and those 31 keys are disjoint. A save taken while the spec is live stores the moved pack hash and is not shifted again.

(1273, -5066) is in room 2768, delta 0, and in tunnel 2529, delta -85. (1388, -5076) is in room 2768, delta 0, and in tunnel 2520, delta -84.85. A save whose region is the room stays at its saved height. A save whose region is the tunnel is carried with that region's drop, including where the old plan also lay in the room.

VERDICT: MERGE
