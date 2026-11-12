R103 review: sol/f05-f04-f17-r19-20261112 (12af024, f4d934c, 9126815 on 415ca7b). Read-only; nothing run.

FINDINGS

1. MAJOR - tests/registry/world_input_rendered_test.json:7 (needs.env) with tools/run_regressions.py:187-193,224. The only test that proves "visible mouse still refuses E in a real window" for the 106 migrated callers is SKIPPED, and the report still passes, whenever LOL2_HEADLESS_INPUT_FIXTURES is unset. Nothing in the repo sets it (only docs/world-input-sol.md:11 mentions it). Same for world_input_headless_test. tools/check_world_input.py and tools/test_world_input.py are not called by any runner or registry entry.

2. MAJOR - tests/museum_broken_thohan_test.gd:51. The old assertion "strict.use() with a visible mouse must not grant the sword" was replaced by `strict._mouse_ready() != (DisplayServer.get_name()=="headless")`, which restates the implementation and cannot fail. The per-owner negative guard is gone; with finding 1 it has no always-on replacement.

3. MINOR - tests/foundation_entry_contract_test.gd:17 and :41. `host.arrival_assets_ready() == entry.arrival_assets_ready()` compares a delegate with itself; `rows == Journal.hints()` compares the catalog with a dictionary built from the same catalog. Both always true. (Real protection is my_journal_test.gd:28, which pins 56 notes.)

4. MINOR - scripts/lol2/game_areas.gd:4-159 marked "affected: begin travel", but scripts/lol2/game_save.gd:230 really loads `doc.scene` from that table. A change to a level scene or host no longer selects whole-game save/load tests unless the test names the scene itself. Documented boundary, but it is under-selection.

5. MINOR - docs/world-input-sol.md:9 says "registry teleports5"; registry 1304/1305 say `"teleports": 2`. tests/my_journal_test.gd:2 and :78 still say 53 notes (assert is 56).

6. MINOR - tests/registry/act2_body_fit_*_earned_test.json and act3_walk_l19a_test.json: test_aids raised by 1 and line refs 143/144 -> 150/151 although tests/act2_body_fit_walk.gd is unchanged in this diff. The new lines are correct (base was stale); stricter disclosure, not weaker, but outside the three features.

CHECKED AND CLEAN

- Rebase damage: none found. No file deleted or renamed; no registry entry removed. All ten area_owners/*.gd gain one comment line only; OWNERS lists (including the merged l10_globe_door) are byte-identical. act2_map.gd removes only the registry/asset-check bodies, moved verbatim to act2_map_entry.gd. docs/DEVIATIONS.md: 3 rows added, 0 removed. Save code untouched except preload targets moved to *_state.gd leaves with verbatim validators.
- Journal: all 56 notes at 415ca7b (17 source files) compared by script against journal_hint_catalog.gd: identical ids, flags, text, guard text and order, including the BJ14 arrival note.
- F-04 player behaviour: all 152 removed / 158 added script lines compared mechanically. Every change is the mouse predicate swapped for available() or captured(); in a window both equal the old test. No handler gained or lost a pause, inventory, flight, form or once-per-press condition. Three older per-owner headless exceptions fold into the same rule.
- Lazy loading: host _ready bodies and registry prepare/restore order unchanged. original_game_gate.gd uses only members the entry scripts provide.
- F-17: fails (not skips) on headless, missing fixture or missing level; names itself a supplied-vantage smoke, logs TELEPORT, makes no earned claim.

COULD NOT CHECK

- Whether existing headless tests change result now that ~106 E/click handlers fire without capture. The handoff states "No whole sweep". A full headless sweep is needed before merge.
- That GDScript compiles and the 15 smoke cases pass on this head (not run by me; handoff reports 15/15).
- The selector counts (106 / 241).

VERDICT: MERGE AFTER FIXES
