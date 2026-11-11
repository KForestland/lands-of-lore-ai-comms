# OF9. Dracoid Cemetery fall under the map

Owner F10, 2026-11-10, between T23-40-20 and T23-41-20. He was underground in the catacombs, passed through a wall, and could not continue. The playtest build named in the queue is r19-work `fee8b8a`. The report JSON still says build `act1_opus_20261108_r18` and area `Jungle`. The camera node is `MapL10_DC`. The area string is OF10 and was not changed.

Patch on `grok/of9` (worktree `~/opus_work/lol2_grok_of9`, parent `fee8b8a`). Piece `docs/deviations/0508-row-2026-11-11-l10-void-walls.md`. The lead renders `DEVIATIONS.md` (`tools/build_deviations.py build`) for 0359, 0507, and 0508. `tests/deviations_ledger_test.gd` compares the piece count to the rendered file and will fail on this branch until that build. `docs/DEVIATIONS.md` was not edited.

## Grades

| Claim | Grade |
| --- | --- |
| T23-40-20 is the player at map (2537.2, -1818.9), origin height -118, camera node `MapL10_DC`, 2026-11-10T23:40:09 | PROVEN (`report_2026-11-10T23-40-20_3410048341`) |
| T23-41-20, 31 seconds later, is the L10 start (-542, 32, -856), and the text is that he clipped a wall, fell, and could navigate below the top of the map | PROVEN (`report_2026-11-10T23-41-20_3470153407`). The clip coordinate itself is not in the JSON |
| That start is the pack arrival, and `reset_position` writes it when `player.position.y` drops below `fall_reset_height` | PROVEN (`area.json` start `[-542, 32, -856]`; `jungle_review.gd` `move_grounded`) |
| Region 4148 holds (2537.2, -1818.9). Its four native neighbours exist. Region 4004, the south neighbour, has native neighbours `[None, 1706, None, 4148]` | PROVEN (`geometry.json`, geometry sha256 `ef89467deb4073f6d60e70baa45bd5ec55b422f1d28b518b16f7cab86434d5e3`) |
| Those two null sides are source-wall faces 13722 and 13721, wall records 2849 and 2848, y -150 to -75, endpoints (2335,-1739)-(2400,-2080) and (2448,-2112)-(2624,-2000) | PROVEN (`area.json`) |
| Before this patch an L10 source wall was drawn and did not collide, unless it was already on `edge_block_keys`. L10 was not in `EDGE_RULE_AREAS` | PROVEN (`jungle_review.gd` `source_drawn_only`; `act2_map.gd`) |
| The wall he walked through is one of those two | LIKELY. One hop from the room he stood in, full height, no bit0 blocker, and the reset matches the fall rule. The report does not store the crossing |
| Putting those sides, and the same class elsewhere, on the movement body stops the walk through walls 2849 and 2848 and leaves the side into region 4148 open, with resets 0 | PROVEN by `tests/l10_catacomb_void_wall_test.gd` on this patch |
| Health field 1 in the reset report, while `fighting.health` stayed 36 | UNKNOWN. `reset_position` does not write health. Left alone |
| 135 null-neighbour sides that have no source wall | Left open. He reported a wall. No second collision was invented for them |

## What changed

`scripts/lol2/l10_void_edges.json` lists 3165 `(region, edge)` pairs. A pair is a native `neighbors[edge] == null` source wall whose outward 10-unit probe, at three points along the edge, meets no other walkable polygon within 48 of the wall base. 368 null-neighbour walls failed that probe and are absent, so a stacked room is not sealed. Sides that already have a neighbour are absent, including 4004 edge 1 (region 1706) and edge 3 (region 4148).

`act2_map.gd` `_l10_void_walls` loads that list for `L10_DC` only, before `super._ready()`, and sets `edge_block_keys`. `jungle_review.gd` already puts a keyed source wall on the movement mesh (`region_edge_blocks`). L10 was not added to `EDGE_RULE_AREAS`. That classifier would mark walls that sit on real portals. `REGION_COLLISION_AREAS` was not changed.

Every one of the 3165 rows matches a `source_wall` face. The scene counter is required to be above 3000; the test does not print the exact counter.

`tests/l10_map_test.gd` used to bound shell triangles by twice the non-wall face count, which was the drawn-only rule. The bound now allows two triangles per void wall. The rule changed, so the expected bound changed with it. No other map test was edited.

## Tests

Memory before the walk was about 25 GiB available. No other Godot process. Launcher `/tmp/godot_dummy.sh` (`--audio-driver Dummy`).

`python3 ~/opus_work/ai_tools/godot_check.py --project ~/opus_work/lol2_grok_of9 --godot /tmp/godot_dummy.sh --changed-since ~/opus_work/lol2_r18 scripts tests` reported 3 scripts, 0 failed.

`/tmp/godot_dummy.sh --headless --path ~/opus_work/lol2_grok_of9 --script res://tests/l10_catacomb_void_wall_test.gd` printed `PASS L10 catacomb void walls: region 4004 edges 0 and 2 hold, the side into 4148 stays open, resets 0`. Exit 0. No `FAIL` line. The walk starts in region 4004, pushes through both walls, then walks the open side to (2537.2, -118, -1818.9).

`/tmp/godot_dummy.sh --headless --path ~/opus_work/lol2_grok_of9 --script res://tests/l10_map_test.gd` printed the existing `PASS l10 map` line. Exit 0.

`tests/deviations_ledger_test.gd` was not run. It cannot pass until the lead rebuilds `DEVIATIONS.md`.
