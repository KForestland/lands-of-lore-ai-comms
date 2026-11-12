# Clean baseline of r19-work, 12 November 2026: known failures and their owners (lead)

Baseline: sharded, isolated user data, r19-work 25cac0f. 1173 tests, 53 skipped by design (chain drivers, LOL2_DH_INPUT_SHA), 10 failures; rerun alone: 9 consistent, 1 flaky. Report: `opus_work/sweeps/baseline_25cac0f/report.json`. From now on a branch is judged against this set: a new failure outside it is a stop; a test in it does not block a merge but has an owner.

| Test | What fails | Kind | Owner | When |
|---|---|---|---|---|
| l14_temple_chain_a | "fall recovery invalidates earned route": Luther falls on the Temple chain walk | likely a real game fault (collision) | Opus, with G-05 and Sol's boundary tool | with G-05 |
| atlas_readable_l14 | Atlas shows 13 of 17 Temple places | real, pre-existing | Grok (queue 6b) | after the robot |
| atlas_readable_l9 | Atlas, Ruins | real, pre-existing | Grok (same item) | after the robot |
| of10_f10_label | freed object in dispose_unattached | real or test fault, F10 path | Opus | next small task |
| legacy_save_fixture | L19_BC legacy writer bytes differ | save compatibility, needs a look | Sol | after the Cemetery pilot |
| hive_interface | an assertion | unknown | Opus to name the cause in one line | next small task |
| hive_boulder_contact_earned_walk | input hash mismatch | fixture drift | Opus | next small task |
| classic_hud_acceptance | Cave 960x540 Save click | stale test; fixed on Sol's tools branch 8807870 | closes when 8807870 merges | with that merge |
| all_maps_indexed | missing import cache sprite_474 in the staged worktree | environment | Opus (staging preflight) | next small task |
| l19_dawn_curse_earned | passes alone | FLAKY | listed in FLAKY.md; Opus to say why once | later |
