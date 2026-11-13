# R115 review: L14 upper way at 36bf776

Verdict: MERGE.

Head `36bf7767b5ba427325b8ce58d7153167df19b868` on `opus/l14-upper-way-20261113`, base `1b1177c`. The diff against that base is five files: `l14_priest_ritual.gd`, `l14_ritual_ceiling_collision.json`, the L14 owner pin, `l14_temple_chain_a_test.gd`, and `tools/build_l14_ritual_ceiling_collision.py`. `scripts/lol2/height_boundary/L14_HT.json` is not in the diff.

Robot folder `robot/L14_HT/20261113_36bf776-r115`. Plain keys, private display `:225`, Dummy audio, one Godot of this worktree. Clock `Engine.time_scale = 4` and `physics_ticks_per_second = 240`. F2 pin `c15_l14_ht`, sha256 `761850f60b460772b31566ff0eb4201caba6e3d6d120ccc590bc64addb317c2f`. Resets stayed 0.

## (a) Clipped ceilings

The 51 added ceilings are the `UPPER_CEILINGS` list. The builder keeps a ceiling triangle only where no floor of height at least -30 covers it, and `attach()` draws the original ceiling mesh, then replaces only the collision faces from the json.

Look-up frames, body at height -48 (feet on floor -80):

| Frame | Stand | Up-ray | What the frame shows |
| --- | --- | --- | --- |
| `frames/lookup_covered_3368.png` | region 3368, under the floor-0 way | hits y 0, the upper floor | stone ceiling, no sky |
| `frames/lookup_open_3264.png` | region 3264, no floor at or above -30 over the centroid | hits y 20, the ceiling collision | stone ceiling, no sky |
| `frames/lookup_3877_gap.png` | region 3877, the patch also under floor region 33 at y 55 | hits y 55 | stone ceiling, no sky |

The 3877 collision gap is real. The drawn sheet is still there, so a player under it does not see a hole. A jump from floor -80 (launch 200, gravity 320) does not reach y 20.

The first stand on the lower sheet was placed. The upper-way neighbour component has no step of 30 or less onto that sheet. The log names each placement. From region 3264 the rest was plain W.

## (b) 8416 and the pew void

Same rays as `tests/height_boundary_narrow_test.gd`, on the booted scene: the lower ray through 8416 is blocked, the ray on the upper floor is open, and the east-edge ray at region 3859 is blocked. The band file is unchanged. The pew leg ended at (2953, 40, -4532), tracked region 145, on the floor, resets 0. The owner's fall path was not replayed as a walk.

## (c) Lower sheet

Plain W from the placed stand on region 3264 through the neighbour portals to region 3877. He stayed on the floor at height -48, tracked 3877, resets 0. Where no upper floor covers the sheet, the up-ray still hits the ceiling at y 20.

## (d) Robot

Opus's floor-0 points from `tests/l14_temple_chain_a_test.gd`.

| Leg | Result |
| --- | --- |
| Entrance, `l14_entry_walk.json` | on the floor at height 48, tracked 856, resets 0 |
| Priest, then E | "You carry the priest's body." Tracked 951, height 17 |
| Carry `[[2416,-2948], ... [2370,-3328]]` plus the slab point | on the floor at height 48, tracked 856, resets 0. Frame `slab_stand.png` |
| E on the slab | "You lay the body lengthwise on the stone rectangle." Frame `priest_placed.png` |
| Pews `[[2394,-3327], ... [2950,-4550]]` | on the floor at height 40, tracked 145, resets 0. Frame `pews.png` |

## Candidate and r19-work

`lol2_candidate_r19g` is at `1b1177c` with no tracked changes (untracked `assets/lol2/dark_halls/` and `assets/lol2/doors/indices_478.png` only). `1b1177c` is not an ancestor of `r19-work`. `r19-work` is `dacf858`. `36bf776` is not in `r19-work` either.
