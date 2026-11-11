• Review complete. I read the full diff (`cdac6d8..0496981`), all three changed source files end-to-end, both test files, and traced every new dependency into the surrounding engine code. The commit touches exactly 5 files (3 source, 2 tests) — nothing else changed.

  ## K90 findings — verdicts

  **1. Set-down on the local floor — fixed.** `cave_crate_stack.gd:251-270` raycasts from the carry spot downward (mask 1) and `try_use` (`cave_crate_stack.gd:293-294`) plants the crate on the hit. Key layer check holds: level floors/shell are a default-layer-1 `StaticBody3D` (`original_walk_review.gd:127-134`, no layer set), while crate bodies live on `SCENERY_LAYER = 1<<8` (`static_assemblies.gd:85`) — so the ray sees terrain but never a crate, and the player is excluded by RID. The `absf(normal.y) < 0.5` guard rejects wall hits, and a miss falls back to `_world_floor()`, preserving old behavior in the stack room. The carried crate has `collision_layer = 0` while carried (`cave_crate_stack.gd:324`), so no self-hit. The test's lip-drop and bridge-room drops exercise exactly the K90 scenarios.

  **2. Lifting the bottom rests the rest — fixed.** The lift branch (`cave_crate_stack.gd:305-310`) now calls `_rest(above)` on all non-carried crates before moving the lifted one. Because the floor ray ignores layer-256 crates, a crate that was stacked on the lifted one falls to the real floor or the next support via `support_top` inside `rest_all` — the lifted crate's stale position cannot prop it up. `rest_all`'s new `floors` parameter is backward-compatible; the only other caller (`tests/cave_crate_stack_test.gd:35`) uses the defaults.

  **3. Crate E input guards — fixed.** `_crate_e_allowed` (`cave_walkthrough.gd:654-668`) requires a captured mouse and rejects open inventory/video overlay, the drowning menu, both guard locks, and the captain intro. Every referenced member exists (`inventory:79`, `drowning_menu:129`, `video_overlay:150`, `guard_encounter:59`, `guard_controls:74`, `captain:53`; `intro_active()` at `cave_captain.gd:81`). The headless exemption is test-only accommodation, harmless in the shipped game.

  **4. Brazier Spark hint — fixed.** `_spark_mana` (`l10_braziers.gd:152-161`) reads `starting_magic.magic_state().player.mana >= 1`, which matches the real level-1 spark cost of 1 (`player_starting_magic.gd:153-155`), and the `magic_state()` shape is confirmed (`player_starting_magic.gd:51-54`, `player_magic_state.gd:4-6`). `spark_clear` (`l10_braziers.gd:137-151`) requires the first mask-3 hit from camera to aim to be the brazier's own layer-2 body, so walls block the hint. The "E — Light brazier" hint is restored alongside (`l10_braziers.gd:208-212`). `spark_target` feeds only the hint, so no other behavior changes.

  ## Non-defects noted and dropped

  - A player with 0 mana but free ancient-charge max-spark sees no hint (narrow false negative, hint-only).
  - Dropping a crate while standing on the stack and facing away can still embed it in the stack — pre-existing behavior, byte-identical to before this commit.
  - A creature (layer 2) between camera and brazier now hides the spark hint — correct LOS semantics, transient.

  APPROVE
