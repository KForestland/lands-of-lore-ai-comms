# Kimi K64 — pre-merge review: sol Task 1 (Dark Halls P3/P4/P5 on r19)

## Findings (numbered, file:line)
## Problems (numbered or none)
## Merge order and verdict

File:line refs — use the patch line numbers or target file lines? Better cite target file:line as they will appear. I know approximate line numbers from the diff hunks:
- player_form_body.gd:51-53 (meta records)
- player_crouch.gd:6-26
- dark_halls_bookcases.gd:84-99 (aimed), specifically exclusion at ~93-95
- tests/dark_halls_bookcases_test.gd:36-58 (oblique + intervening wall)
- tests/dark_halls_slice_test.gd:123-138 (new gate block; hunk at @@ -120,6 +120,23 → new lines ~123-138)
- tools/build_dark_halls_objects_walk.py:13-30 (shared_portal), 46-48 (use)
- tests/chamber_route_test.gd:46-49 (patch 2/4)
- tests/hive_elevator_post_click_test.gd:27-31 (patch 4/4)
- dark_halls.gd:100-107 setup, 148-149 include_static_face
- act_one_quest_state.gd:495-500

Keep it tight.

• All checks are complete. Here is the review.

## Findings

1. **Crouch/form fix is at the right layer** (`scripts/lol2/player_form_body.gd:51-53`, `scripts/lol2/player_crouch.gd:6-27`). The r18 failure was `museum_review._physics_process` recomputing form from the stale scene field `player_form` and calling `apply(player, camera, 0, …)`, rebuilding a Human capsule over a direct form change. `museum_lightning_crystal_test.gd:39` does exactly such a direct change (`apply(scene.player, scene.camera, 2, false)`). The patch makes `Body.apply` record `lol2_form`/`lol2_crouched` metadata on the body itself, and the shared tick now reads that meta, so a directly applied form 1/2 survives the tick (`player_crouch.gd:8-10`). The test itself is untouched — the fix is in the engine, not the assertion.
2. **Low-header reload case also covered**: `apply(..., check_space=false)` marks `lol2_pose_recheck`; the first tick re-fits the Human under the ceiling with the existing clearance query (`player_crouch.gd:15-21`). No serialized state added. `dark_halls_crouch_earned_test.gd` is a real earned walk (pinned monastery save, cellar clicks, live combat, F5/reload), not a synthetic substitute.
3. **Intervening-wall rejection is real** (`scripts/lol2/dark_halls_bookcases.gd:84-99`). The old ray hit the target leaf first and stopped; the new ray excludes only the player and the target leaf's own body and rejects the shelf on *any* remaining hit along the full camera→leaf-center line. The component test (`tests/dark_halls_bookcases_test.gd:37-58`) proves both directions at the actual earned58 pose: oblique approach accepted, a 5-unit obstruction at the ray midpoint rejected ("Intervening wall admitted" fail retained), removal restores the target. Not loosened.
4. **Slice fix keeps the solids and uses the gate** (`tests/dark_halls_slice_test.gd:123-139`). The wp31/region-390 stall was the walk hitting the newly solid bookcase59 leaf. The slice now aims and dispatches a real E `InputEvent` for a visible, reachable, closed bookcase ahead and *fails* if it does not open (`return fail("Route E did not open bookcase…")`) — no goal placement, no removed solids, no E without a visible aimed target. The separate earned tests (`dark_halls_bookcases_earned_test.gd:66-72`) do the full live-input approach59 → E → walk-through → reload proof.
5. **Earned58 jamb fix is planner/test-only, as claimed** (commit 3/4, `tools/build_dark_halls_objects_walk.py:13-30,46-48`). Native neighbor edge 179→180 spans 133 units but the actual floor opening is 61; the full-edge midpoint (1806.5) put the 30-unit capsule in the jamb. `shared_portal` clips each neighbor edge to the destination floor polygon and rejects portals narrower than the existing Human diameter. Only three generated waypoints change in `tests/dark_halls_objects_walk.json` (58, 1013, 1041); zero runtime/geometry/collision changes. Not a geometry hack.
6. **Applicability verified**: all 11 modified-file pre-image blobs match `r19-work` (0603225) exactly; `git apply --check` against the current `r19-bk` (8601810) worktree fails *only* on `tests/chamber_route_test.gd` — r19-bk already contains byte-identical post-image `5e3d72e` (its "0003 chamber_route_test opens the Draracle leaves"). Sol's commit 2/4 is a confirmed duplicate of Fable's already-integrated `42d9c2c`; skip it when landing on the bk-merged tree.
7. **No numbering collisions**: registry orders 1010–1017 (8 new files) vs r19-work max 990 and r19-bk max 1002 — clean. Ledger pieces reuse 0317, but W16 (`tools/build_deviations.py:28-30`) explicitly allows equal numbers rendering in name order, and I simulated the render: r19-work pieces + Sol's 4 pieces produce **byte-identical** output to the patch's hand-edited `docs/DEVIATIONS.md`, so `--check` passes. Each piece is one row.
8. **Overlap with r19-bk is disjoint at the hunk level**: r19-bk touches `act2_map.gd`, `jungle_review.gd` (region-collision, hunks far from Sol's line-407 `_physics_process` insertion — I verified the function bodies are identical across branches), `act_one_quest_state.gd` (lines 95–130 vs Sol's 492+), `DEVIATIONS.md` (rows at 570+ vs Sol's at 521). `player_form_body.gd`, `player_crouch.gd`, `original_walk_review.gd` are untouched by r19-bk. `act2_map.gd` extends `jungle_walkthrough`, so Act 2/3 maps inherit the crouch tick as documented ("derived areas inherit").
9. **Commit 4/4 (hive elevator observer) is a justified test-timing fix** (`tests/hive_elevator_post_click_test.gd:27-31`): source sound 388 is 35 ms, shorter than the old 3-frame wait; `playing` is now sampled at E dispatch while the persistent contract (`clicks == 1`, `checkpoint.target == 1`) is retained. Stated reason, no game-rule change — but note it is outside Task 1's P3/P4/P5 scope.
10. **Conventions held**: native kind-4 use groups dispatched through `native_script_host`, travel magnitudes from source bytes (100/60/116), strict boolean save validation, disk rollback tested, sounds logged-not-invented, bookcase leaf collision follows the established `dark_halls_doors.gd:87` pattern (`player.collision_mask |= SCENERY_LAYER`). Docs honestly mark adapters (slide direction, E-reach, state→texture-mode coupling).

## Problems

1. **The qualification sweep is still running and not green.** `coverage.json`: `complete=false`, `passed=false`, 7/792 passed, 774 missing. Live status: q0 183/197, q1 93/199, q2 58/198, q3 97/198. HANDOFF itself says "NOT READY yet". Three dispositions to watch: (a) q0 `act1_recovery_museum_test` F9≠F5 mismatch on `checkpoint.curse.*`/`player_form` — has an accepted retry receipt (`sol_r19_recovery_r16`), but it's a form-adjacent failure in a form-touching patch, so the final audit must confirm it stays an accepted retry, not a primary failure; (b) q1 village route timed out at 1500 s, retried at 3000 s and passed in the primary root (declared harness deadline change, not a game timer — legitimate); (c) q1 `hive_elevator_post_click_test` failure is the known old-assertion flake that commit 4/4 fixes, covered by the f6c6a3e delta receipt. **Merge must wait for `coverage.json` to report complete/passed.**
2. **Untracked media dependency**: chamber/Draracle hosting needs `assets/lol2/doors/indices_478.png`, which is *untracked and uncommitted* in both Sol's roots and the lead worktree (present in `git status` now). If a clean checkout or `git clean` removes it, chamber tests silently revert to the unhosted-door behavior. Flag for the lead to decide whether to track it or document the staging step.
3. Minor, non-blocking: `dark_halls.gd:100-107` push_errors on bookcase/slide setup failure but doesn't `queue_free`/null the node (the `windows` path right above does both). Cosmetic inconsistency, not a merge blocker.
4. Patch checksum: the printed `a6d0bc8c…` in HANDOFF is the historical 3-commit hash; the actual 4-commit file is `c271f52f15fd93d6bd92badd23f5e49b3631370db0be92b59a7b19780a9a9a39`. HANDOFF discloses this ("use sha256sum for its current checksum") — just don't verify against the stale value.

## Merge order and verdict

1. Merge **r19-bk first** (as planned), then Sol's patch **without commit 2/4** (chamber_route_test is already byte-identical in r19-bk). Everything else applies cleanly onto r19-bk; no renumbering needed on either side. After merge, re-run `tools/build_deviations.py --check` and `tools/check_registry.py` on the combined tree (both verified compatible here).
2. **Verdict: content APPROVED, but HOLD the merge until qualification completes.** The three r18 failures are fixed for the right reasons (engine fixes, not test loosening; the only test loosening is the hive observer sampling with a stated, sound reason). The crouch tick can no longer override a direct form change, the bookcase ray genuinely rejects intervening walls while accepting the oblique approach, and the earned58 fix is a planner correction with runtime geometry untouched. Merge gate: `coverage.json` complete/passed from the four isolated shards at frozen 44e2798 plus the f6c6a3e delta receipt — re-check `python3 status.py` / `audit_coverage.py` before landing.

