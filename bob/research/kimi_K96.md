• # Pre-merge review: F-05, F-04, F-17

  Scope note first: the described stack is inaccurate. F-05 (`71145fb`) and F-04 (`4e128cb`) are **sibling commits, each directly on `8b55af4`** — F-04 is not on F-05, and the range `8b55af4..75414b5` contains only F-04 + F-17. I reviewed F-05 via its own diff. The two branches overlap in 10 files (e.g. `act2_progression.gd`, `cave_walkthrough.gd`, `l8_baccata.gd`), so merging both requires a real merge; Sol's handoff reports a clean combined-index apply, and the overlaps are in different functions (preload/static moves vs. input predicates), so this is expected to merge textually.

  ## F-05 (71145fb) — preload/dependency split

  No defects found. I checked every moved hunk against its origin:

  - All extractions are verbatim with delegation: the four `*_entry.gd` modules, `jungle_assets.gd` (the moved body of `jungle_walkthrough.assets_ready()`, which now delegates to it), `journal_hint_catalog.gd` (all 18 hint arrays match the removed originals in text and order), and the eight L8 `*_state.gd` save contracts (validators/initializers byte-identical, including `l8_tree_state.gd`'s torch table and `l8_backroom_state.gd`'s SEQUENCES).
  - No script loads a different or missing module at runtime. `original_game_gate.gd` now preloads entry modules whose FORMAT/DEFAULT_PATH/readiness are identical to the hosts' (and the hosts still expose them, delegating — so the remaining callers I found by grep at head, e.g. `tests/dark_halls_doors_test.gd:91` using `dark_halls.gd` FORMAT and the four map tests using `act2_map.gd` registry(), get identical values). Callers moved to the state modules (`act2_progression.gd:363` → `l8_shore_state.closed`, `act2_world_items.gd:57` → `l8_clubhouse_state.STONES`, the eight validators in `act_one_quest_state.gd`) invoke the same logic. `my_journal.gd` reads the same arrays in the same order via the catalog instead of `load()`-ing owners; the journal IDs/text are unchanged.
  - `tools/affected_tests.py` is conservative by default (every `res://` string literal, class reference, preload — including inside overridden methods — and directory prefix is an edge; deleted paths select via `@exists:`). The only exclusions are the `# affected: begin identity/travel` comment blocks; I programmatically verified no `load`/`preload` exists inside any marked block at `71145fb`, and the tool raises on one. All Python tools parse.

  ## F-04 (4e128cb) — shared input admission

  No defects found. The three stated risks do not materialize:

  - **Without a captured mouse / menu open / twice?** `world_input.gd:5` `available() = captured() or DisplayServer headless`. On any windowed backend `available()` is identical to the old predicate, so a real player's admission is unchanged everywhere. Pause/flight/inventory/interface-cursor/actor-lock/modal guards are untouched — verified in the hunks of `l10_emperor.gd`, `l8_dawn.gd`, `l10_silverleaf.gd`, `cave_walkthrough.gd`, `dark_halls_doors.gd`. The `interface_request` bypass in `hive_route.gd:14` / `hive_warriors.gd:57` was neither widened nor removed. No double-execution path was introduced (no event flow was restructured; only predicates were swapped).
  - **Substitution fidelity, independently verified:** 145 removed raw capture comparisons ↔ 145 added helper calls; every added line in `scripts/` is a `world_input` call (or the two `admitted` uses in `dark_halls_doors.gd`, or the new helper itself). Remaining `MOUSE_MODE_CAPTURED` references are assignments, capture toggles, and saved defaults only. `captured()` was correctly retained for non-action controls — movement axes, jump gates, mouse-look, capture toggles, lava/drowning/encounter/chamber-arrival clocks (`cave_walkthrough.gd:1013,1018,1023,1036,1698`), and the modal motion-swallow in `cave_guard_controls.gd`.
  - Tests are consistent with the new rule: the two component tests drop their `_mouse_ready()` overrides and assert the production predicate matches the backend; `l19_switch_shot_test.gd` now forces visible mode instead of the HUD-magic override; the new headless/rendered contract tests exercise real E plus the guard negatives. Evidence (`f04_rendered_equivalence.json`, targeted logs) matches what I verified independently.

  The only behavior change is headless-only admission, which is the commit's stated purpose and is test-facing.

  ## F-17 (75414b5) — rendered per-level smoke

  No defects found. No production gameplay file is touched (only tests, docs, the runner, and a snapshot-list line in `tools/regression_source.py`).

  - Fixture integrity: all 15 scene paths exist at head; every production interface the shared case calls exists (`jungle_source_pickups.target/collected/ITEM/sprite`, `l17_beast_blade.at_wall/blade_ready/state().cut`, `l19_drain_path.at_door/doors_open/state().door_clicked`, `hive_warriors.aimed_hit`, `hive_chasm.trigger/activated`, `cave_collectible.can_collect`, `set_equipped_item` on the three hosts). Wrapper area strings match their registry names.
  - Harness integrity: the case itself refuses headless, requires `InputRule.available() and captured()` and `interface_request == false`, dispatches real `Input.parse_input_event` press/release pairs, and asserts before→after state. `tools/run_rendered_smoke.py` enforces exactly the 15 registered cases, sequential 60s timeouts, a fresh private profile, source-pinned receipts, and fails on any skip. Order-1341 ties are explicitly allowed by `run_regressions.py` (W16, name order).
  - Evidence corroborates: `final15_v2` logs show 15/15 PASS at 3.8–14.2s, and all three negative controls (headless, no_click, no_e) fail with exactly the expected assertions. The clock holds and supplied vantages are disclosed in `tests/smoke/README.md` and the registry notes — appropriate for smoke scope, not an earned-walk claim.

  ## Verdicts

  - F-05 `71145fb`: APPROVE
  - F-04 `4e128cb`: APPROVE
  - F-17 `75414b5`: APPROVE
