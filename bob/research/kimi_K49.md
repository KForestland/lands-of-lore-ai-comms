# Kimi K49 — pre-merge review: grok BJ00 + fable claw (r19)

## Findings

1. **BJ00 applies cleanly on top of the lead change and keeps it.** `git apply --check` passes on r19-work `0adf21a`. The patch's context in `scripts/lol2/l8_temple_door.gd` quotes the lead's `SEALED` const and the K47 comment (base `l8_temple_door.gd:28-30`), and the patched file keeps `SEALED` verbatim, only wrapping it in `sealed_hint()` (`BJ00_l8_temple_next.patch:48-67`). The lead's ledger-0350 behavior is built on, not undone.

2. **BJ00 behavior matches the research and K47.** The door stays gated on the Dreamstone (`has_stone()`/`can_leave()` untouched); only the hint text changes, keyed off `l8_journey` (`temple_visited`/`gift`/`admitted`). After admission the line is only the sealed sentence, exactly as `l8_longplay_route.md:35` and `kimi_K47.md` prescribe. The owner's "closed because the priest was killed" reading is correctly treated as presentation, not gating.

3. **BJ00 village panel change is safe for existing tests.** Removing the "Show Daniel's blade" button while `gift != "recovered"` (`l8_journey.gd` hunk, patch:10-22) and splitting the `show_guard` refusal into two reasons (`l8_journey_state.gd` hunk, patch:35-44) breaks nothing: every existing caller (`l8_journey_live_test.gd:25`, `l8_herbalist_earned_test.gd:6`, `l8_departure_earned_test.gd:7`) reaches the guard with `gift == "recovered"`, and `l8_village_temple_first_test.gd:94-95` asserts only `not refused.ok`, not the old reason string.

4. **BJ00's earned test walks like a player.** `tests/l8_temple_next_earned_test.gd` extends the pinned-save earned chain (`l8_gift_earned_test.gd:4-5` INPUT/HASH), walks the real `l8_first_departure_walk.json` waypoints (`temple`/`village` keys exist), uses real `InputEventKey` presses, and the `"sealed-door"` walk label deliberately never matches `L8Journey.target()` so the walk runs to the door (comment at patch:112 is accurate per `l8_temple_earned_test.gd:18`). All referenced members exist: `door.POINT/SEALED/hint/reachable()`, `journey.box/target()/interact()` (`l8_journey.gd:13,39,69`), `starting_magic.interface_request`, `interface_hud.hint` (`jungle_walkthrough.gd:638-641`). Typed vars throughout; no test was loosened.

5. **Ledger collision confirmed: 0352 is used by both patches.** Grok's piece `0352-row-2026-11-08-l8-temple-next.md` and Fable's `0352-row-2026-11-08-l8-straw-pit-reload.md`; Fable's second commit takes 0353. The base already carries duplicate pairs (0350 ×2, 0351 ×2), and `build_deviations.py` sorts same-number pieces by filename, so the render stays deterministic — but the "one number per row" convention is violated again.

6. **BJ00 does not re-render `docs/DEVIATIONS.md`.** The patch adds the deviations piece but no ledger row. `tests/deviations_ledger_test.gd:11-12` runs `tools/build_deviations.py --check`, which currently passes on base (437 pieces) and will fail the moment BJ00's piece lands without a re-render.

7. **Fable patch applies cleanly and is self-consistent.** `git apply --check` passes; its ledger rows in `DEVIATIONS.md` are byte-identical to the new piece files and append in sorted order, so `--check` stays green after Fable alone. No file overlap with BJ00.

8. **Straw-pit reload fix is a presentation superset.** `l8_straw_trap.gd` `restore()` now shows ramp meshes/stakes whenever `sprung`, with only the exit slope gated on `_on_pit_floor()`; solids stay off in all cases, so no mechanic/cap changes. The existing earned test (`l8_straw_trap_earned_test.gd:76-106`) asserts ramps absent before springing and present after landing/reload — nothing asserts the old "hidden mid-fall" state, so it still passes.

9. **Atlas marker done-rules verified against real state.** `l8_larkhon` → slots `larkhon:chest`/`mix:serum` (`l8_larkhon_state.gd:4,7-8`), `l8_shaman_trade` → `shaman:silverleaf` (`l8_shaman_trade.gd:5-6`), `l8_dawn` → `dawn:bracers` (`l8_dawn_state.gd:4,7`), `l13_egg_door.opened` (`l13_egg_door.gd:3,18`), `l13_exit_lock` → `citadel:exit_lock104` (`l13_exit_lock_state.gd:4-5`); `committed` is the real mechanism_transaction field (`mechanism_transaction.gd:30-33`). Journal notes `l13_citadel_sealed`/`l13_dreamstone` exist (`l13_journal_hints.gd:7-8`). Markers only encode what Journal notes say — no invented knowledge.

10. **All L12/L13 Atlas coordinates match the host constants exactly** — e.g. Baccata (2858,-18172) = `l12_citadel.gd:5`, citadel gate (3684,-19361) = `entrance_aim()` `l12_citadel.gd:49`, icy river (2018,-11533) ∈ `l12_river_rafts.gd:5`, Dreamstone (-2710,-4183) = `l13_altar.gd:5`. Names are sourced to the hint book in each row's `source` field. `area_id` is set on both scenes; `area_of`, `viewed_storey()`, `slices` polygons/storeys, `toggle_atlas()` all exist.

11. **Registry order collisions are explicitly tolerated.** BJ00 takes order 937 (headless) and Fable's L12 test takes 937 (rendered), L13 takes 938; base already has 935 ×2 and 936 ×2, and `check_registry.py:37-39` allows ties ("equal orders allowed; ties run in name order").

12. **Minor blemish:** `tests/atlas_readable_l12_test.gd:46-61` contains a dead marker-check block guarded by `var note := ""` (L12 has no plot markers, unlike L13). Harmless copy-paste, not a failure mode.

## Problems

1. **BJ00 breaks the deviations ledger check.** `docs/deviations/0352-row-2026-11-08-l8-temple-next.md` is added without re-rendering `docs/DEVIATIONS.md`; `deviations_ledger_test` (registered suite test) will go red. Fix before merge: run `python3 tools/build_deviations.py build` (or `--check` to confirm).
2. **Ledger number 0352 doubly assigned** (Grok temple-next vs Fable straw-pit-reload). Tooling tolerates it, but since one piece must move anyway for problem 1, renumber Grok's piece to `0354-row-2026-11-08-l8-temple-next.md` (0353 is Fable's) and then render — one step fixes both.
3. Cosmetic only: shared registry order 937 (allowed) and the dead `note := ""` block in the L12 test. No action required.

## Merge order and verdict

1. **Fable `claw_eb2eb48.patch` first** — self-contained, ledger green on its own, no overlap with BJ00.
2. **Grok `BJ00_l8_temple_next.patch` second** — applies on `0adf21a` either way; preserve the lead's `l8_temple_door.gd` sealed-hint change (the patch already does).
3. **Immediately after:** rename Grok's piece to 0354 and run `tools/build_deviations.py build`, then run the affected tests: `deviations_ledger_test`, `l8_temple_next_earned_test`, `l8_temple_earned_test`, `l8_gift_earned_test`, `l8_village_temple_first_test`, `l8_straw_trap_earned_test`, `atlas_readable_l8/l12/l13_test`.

**Verdict: merge both, conditional on the ledger re-render (ideally with the 0354 renumber).** Both patches are presentation/adapter-level, earned-tested, faithful to the longplay/hint-book evidence, and neither undoes the lead's r19-work door change. Note I did not execute the test suite — verification was static (patch application, symbol/state-path/coordinate checks, and the base ledger check, which passes).

