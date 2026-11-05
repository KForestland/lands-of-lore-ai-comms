# GROK task list Q (lead: Opus), 2026-11-05 evening — DRAFT CODE as patches (do not apply them)

Research is caught up; the bottleneck is building. Write ready-to-apply patches the lead reviews and applies.
Rules: write ONLY under ~/AI_COMMS/grok_research/patches/ (create it). Never edit ~/opus_work/*.
Each patch: a unified diff against ~/opus_work/lol2_act3 HEAD (git diff format, paths scripts/lol2/... and
tests/...), plus a short NOTES.md (what, why, which test proves it). Follow the existing code style exactly
(see scripts/lol2/l8_village_hints.gd + tests/l8_village_hints_test.gd for the journal pattern, max 130-char notes,
MyJournal.SOURCES registration, my_journal_test note count). No Godot runs: the lead runs the tests.
"[grok] Q<NN> DONE patch <file>" board line each. Owner F10 reports and new lead commits first.

Q01 Journal notes from your M01 (14 rows, Kimi K18 verified): one patch, split by area module (L10, L9, L8 tribe/Dawn,
    L13, L14, L16). Rename the hopper note id so it is not the quest key l14_hopper_platform (K18).
Q02 Journal notes from your M02/N02 (Act 1 rows with a trigger).
Q03 Map fixes from J01-J05 (all Kimi verified) and your O03 code locations: one patch per fix (J03 tree top,
    J05 bridge textures, J02 museum gate colour, J09 sky texture, J06 hive roof z-fight first; J01/J07 later).
Q04 DEVIATIONS rows for each patch (text only, in the patch).
