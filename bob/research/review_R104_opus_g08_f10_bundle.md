R104 review: opus/sweep-fixes-20261112 (worktree ~/opus_work/lol2_opus_fix), read-only
Scope note: 415ca7b..7e95962 holds only 581757c + 7e95962. The door-count fix is 7627965 (branch HEAD, outside the stated range); reviewed too.

FINDINGS

1. MAJOR scripts/lol2/playtest_bundle.gd:59-66,81-89. The recorder is a child of the unconditional PlaytestFeedback autoload (project.godot:24), so every player gets a full-resolution viewport readback (get_image) plus resize every 3 s for the whole session. Periodic hitch risk in normal play, and in every rendered test. No dev/playtest gate.

2. MAJOR playtest_bundle.gd:92-107. freeze() calls make_document without can_save(). Dead, falling, in water, mid-conversation, mid-transition (exactly the typical stops) yield a save the game itself refuses to write; bundle.json does not record the can_save() reason. It also does not state what the area packet omits (e.g. cave plate state "is not saved", cave_entrance_death_test.gd:78; creature/timer coverage is per area). Reproduction fidelity is unstated.

3. MAJOR game_save.gd:190-194. No load path accepts the bundle file: load_slot reads only user://saves/slot_NN.json. save.json is format-identical and validated (write_document), but must be hand-copied over a slot. No loader, no instruction in the manifest.

4. MAJOR playtest_bundle.gd:145-146,160 and playtest_feedback.gd:180. bundle.json carries absolute paths ("project", "log_file"), and log_tail.txt is the raw engine log (contains "PLAYTEST FEEDBACK SAVED: /home/<user>/..." lines). Home path leaks if a report is shared publicly.

5. MINOR playtest_feedback.gd:68. freeze() runs after pause and input suspension, before the panel is shown, with no readiness guard; a script error in area_snapshot during loading leaves the game paused with no panel (Esc still closes).

6. MINOR playtest_bundle.gd:36-39. Keys are recorded in every text field except the F10 note (original_game_gate.gd:52 path field). History is the last 120 s only, frames the last 30 s; first_error has no timestamp, so the first point of trouble is not tied to inputs. Failed frame PNGs are omitted silently (line 127).

7. MINOR tests/playtest_bundle_test.gd:58. Validates save.json, never loads it; no refusal-state or write-failure case; note text set directly.

8. MINOR tests/cave_entrance_death_test.gd:85-92. The old scene is retained (game_session.gd:94-104) until commit; if that takes more than 3 frames the loop breaks on the old Cave and fails (flaky). On a rebuilt scene owner_state==0 is true by construction; quicksave/quickload results are unchecked.

CLEAN
- Recording runs from startup, not from F10; memory is bounded (120 s, 10 frames); the note is not recorded.
- Bundle failures go to "unavailable"; report.json is still written. Writes stay in the unique report folder; no overwrite; no player slot touched.
- Save contains pose, inventory/health, area packet, native bank: the same as a slot.
- Test uses real input events (W, mouse, click, F10, Ctrl+Enter), checks hashes, can fail.
- Door count: legitimate. area.json has exactly 12 faces for movables 124/125 (6 each) = 590-578; expectation is computed from l10_globe_door.owns, not hard-coded; owner commit da76748 is an ancestor.
- Cave fix: legitimate stale test (quickload now goes through the whole-game load and rebuilds the scene).

NOT CHECKED
- Nothing was run: no test results, no measured hitch, no real bundle inspected.
- Per-area snapshot coverage (creature health, moved floors, timers) beyond the Cave.
- Behaviour of area_snapshot before readiness, and release-build error behaviour.

VERDICT: MERGE AFTER FIXES
