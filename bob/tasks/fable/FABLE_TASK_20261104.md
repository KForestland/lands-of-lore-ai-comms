# FABLE: Act 1 Hive missing mechanics (lead: Opus), 2026-11-04

Owner is sick and resting 11-04/05 and playtests r14 (play.sh = r14 8732a39). Astra (Codex) is out of usage; Grok is in research mode.
Owner rule (feedback-focus-a-to-z-path): build known original behaviour directly; decode only the unknowns.
Workaround rule: if a native trigger stays untraced after a time-box, ship a DEVIATIONS-logged adapter that matches the longplay.

Branch: `act1-hive-missing` from r14 **8732a39**. Own worktree, e.g. ~/opus_work/lol2_fable_hive (copy tmp/ from lol2_r14 without regressions/ and userdata/; set your own XDG_DATA_HOME in tmp/godot_host.sh).
Never write in lol2_r14 or lol2_act1m (the lead's branch `act1-missing` covers beats 14/30/31/53).
Sources: AI_COMMS/grok_research/act1_completeness_duck.md (rows 63/70/73), kimi_K6.md + kimi_K7.md (hintbook specs),
source_ids_act1_pt3.md, hive-elevator-preparation.md, owner F10 reports in playtest_feedback_20261023/TRIAGE_20261103.md section B.

Order (time-box about 60 min each, log what stays open, move on):
1. **Beat 63, flute lift (report 17-41-36, Hive -2543,-7633):** the 8-stop lift starts at the BOTTOM and comes up when the flute is played at the pit; then floors 2-8 are selectable. Owner keeps the flute (r13 choice).
2. **Beat 70, four buttons (17-43-48, Hive -3509,-7128):** hit the buttons in the correct order; the clue is on the top floor. Find the 4th button and the order (native script first, longplay frame index second).
3. **Beat 73, boulder cellar (17-45-07/36, Hive -3345,-6074):** a boulder falls from the wall, breaks the floor and opens a hidden cellar.
Also look at D-section Hive wall clipping (17-42-38/43-05/43-17) if it is in the same rooms.

Gates: godot_check, affected_tests vs 8732a39, affected set PASS headless; one earned walk test per beat. Then READY on the board + status/fable.md + a handoff. The lead integrates into r15.
