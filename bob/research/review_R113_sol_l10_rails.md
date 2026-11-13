# R113. Cemetery rails and two named walls at 6d32a2f

Read-only. Branch `sol/generic-l10-r109-20261112`, worktree `~/opus_work/lol2_sol_generic_triage`, head `6d32a2fe330ba49be9f6c8bc4bbb4cc2ea13bf90`. The range `3033c3d..6d32a2f` is one commit: `6d32a2f` on parent `3033c3d0832a4976e4da13dc213413d674eb12a0`. Godot was not run. Sol's sitting logs were not replayed here.

## The nine R109 items

This commit does not edit the code of those nine closures. They stay as they were on `3033c3d`.

1. One boundary mechanism. Still one loader and one `HeightBoundaryCollision` body. The L10 packet grows from 3530 keys to 3532. The two new keys are the named walls below, not a second mechanism. Legacy plus OF6 stays 3168. The approved additions stay 362.
2. Convex mover contact. No file in this range touches mover tops, the use-ray bound, or the carry path.
3. Fresh full v4. The sitting Sol reports (10214.44 s, source stable) is on frozen `3033c3d`. This commit does not re-run it. Row 0640 now records that result and points the follow-up at row 0644. The mechanism sentence in 0640 still says 3530. The live packet is 3532, which 0644 states.
4. Reproducible rendered inputs. The 24-input stager is outside this diff. The new owner tests pin their own committed fixtures by sha256.
5. Cover at zero life. Unchanged.
6. Saved bounds. Unchanged. No reseating of a saved position.
7. Pause prompt. Unchanged.
8. Ledger. Rows 0637-0639 are not renumbered again. This commit rewrites the evidence half of row 0640 and adds row 0644.
9. Real E on the shelves and the Emperor. Unchanged.

## What the rails do for the player

`scripts/lol2/l10_fences.gd` is the only movement-facing edit. Jump speed, gravity, sprint, and the jump arc are not in this diff. No player-physics file changes.

Rails 74 and 174 are `ORDINARY_JUMP_RAILS`. Rail 75 is not.

A crossing still starts only from the high side: on the floor, more than 8 units toward the high side of the rail, feet within 18 of the rail height. The body then has to leave the floor while moving toward the low side (direction dot normal under -0.5). For 74 and 174 the sprint flag and Ctrl are no longer required, and they do not have to stay held while the fence is open. The fence collision drops until the body is 55 units past the rail plane or the player turns back. For 75, `admits` still requires sprint and Ctrl, and losing either of those closes the fence again. The sixth argument defaults to false, so a five-argument call keeps the old rule.

The Journal line for `l10_fence_tuck` now says a running jump clears the two lower crossings, and that the other rail still wants a Ctrl tuck. The code for 74 and 174 does not read the sprint key. A plain W+Space jump from the high side is enough. Holding Shift still works. The word "running" in the Journal is narrower than the code. The code matches the 01:42Z decision (W+Space, no Shift, no mid-air Ctrl).

## The two named walls

`tools/prepare_l10_boundary_packet.py` admits only source faces 9150 and 9179, and it refuses the packet if those keys overlap the older 362 additions or fail to match the map.

Checked against `assets/lol2/generated/maps/L10_DC/area.json` (sha256 `3003b704862d0b36381bace55fe43fa079378aab42d23480c4c843bcfc0edb56`, the same pin as the fixture and the packet):

- Face 9150, region 1455, kind `source_wall`. A sheet from (-653, 45, -4189) to (-654, 100, -4286). Key `source_wall|-653,-4189|-654,-4286|45|100`.
- Face 9179, region 1476, kind `source_wall`. A sheet at x -653 from z -4036 to -4132, y 45 to 100. Key `source_wall|-653,-4036|-653,-4132|45|100`.

The packet diff adds those two keys and removes none. Counts are 3532 selected, 3532 unique, `owner_named_keys` 2. The native 35..45 aperture keys stay, including `source_wall|-653,-4036|-667,-4036|35|45` and `source_wall|-653,-4189|-667,-4189|35|45`.

Both faces join the existing boundary body. They block the band from 45 to 100. They do not close the 10-high slot from 35 to 45. The grounded-approach test's shape query is an 8-high box at (-653.5, y, -4238), which sits on face 9150: clear at y 40, solid at y 60. Face 9179 is the same band on the next segment and is selected by the same key list. No terrain file and no map pack change.

## What else is in the commit

Production scripts in the range are `l10_fences.gd`, `l10_journal_hints.gd`, and `scripts/lol2/height_boundary/L10_DC.json`, plus the packet composer. The rest is docs (`DEVIATIONS.md`, rows 0640 and 0644, `docs/generic-l10-testing.md`) and tests.

`generic_l10_owner_rail_test.gd` loads the owner rail save and a fresh-v4 blue save, then holds W and taps Space with Shift and Ctrl up. It walks 74 and 174 that way and continues to the priest urn. `generic_l10_owner_grounded_approach_test.gd` loads the ok-here save and plays the recorded keys and mouse. It refuses the run if the body stands on the invalid roof. Neither test writes a pose, a resource, or a reseat. The long fixture is that recorded trace. Godot was not launched for this review, so those PASS lines are Sol's, not a new run.

No other collision set, save migration, or physics constant is in the diff.

VERDICT: MERGE
