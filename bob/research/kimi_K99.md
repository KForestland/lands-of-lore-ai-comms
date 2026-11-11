# K99 (Claude reviewer, Kimi monthly quota out): Sol C-10 007eaf8 vs da76748 - VERDICT: CHANGES

OK: test/ledger-only diff; sitting at default 60 Hz/scale 1; no position writes in the sitting; arrival pose checked; no paths/names; ledger 0621 unique.

1. MAJOR tests/act3_walk_l19a_test.gd:13-17 - the bars check cannot fail in the F9 repeat. F9 (act2_save.gd save_host / act2_map.gd:430-455 apply_save) does not restore progression.regions, so floors 40/61 likely stay at -20 after pass 0; pass 1 breaks on tick 1 and passes even if the click does nothing. Fix: assert 40/61 at native -40 right before each click; if F9 leaves them raised, report a save/restore STOP (that would also be a player bug: loading a save taken before the click would show raised floors).
2. MAJOR (disclosed) tests/act2_body_fit_walk.gd:187 - the rapids run does not exercise auto-fit (B1 fallback) and still runs at time_scale 2 / 120 ticks (line 131). Lead: B1 is the accepted master-plan fallback for C-10; accepted, but the clock must be stated in the handoff.
3. MINOR act2_body_fit_walk.gd:140-141 - adapter_exit_seeds=false and lol2_map_start_selector are undisclosed aids (probably nil effect).
4. MINOR registry test_aids/honesty fields are checked by nothing in this tree (checker lives on an unmerged branch).
5. MINOR registry order 1344 collides with area_owner_catalog_test on the foundation branches (ties allowed; renumber at integration).
6. MINOR act3_walk_l19a_test.gd:10 - clock recorded but not asserted.
