# Fable task (lead: Opus), 2026-11-07 — the Huline Temple interior (owner parked it for you)

Read first: AI_COMMS/META_DUCK_METHOD_20261107.md (the method; its worked example IS this task), AI_COMMS/BLOCKER_RULE_20261107.md,
METHOD.md (public ai-comms), the board tail (act1_completion_20261017/COORDINATION.txt).
Owner reports: r16 F10 21-05-00 "geometry very wrong, still clipping things" (L14_HT around (2430,-3458)); r14 Temple reports in
playtest_feedback_20261023/TRIAGE_20261104.md; longplay frames g_276/g_278 (chambers floating in black, entered through doors).

Base: ~/opus_work/lol2_act3 branch act3-chain (create your own worktree from it; never edit lol2_act3 or lol2_r17).
What exists: region_visibility.gd (portal visibility: draws only regions reached through region edges in the view),
l14_hall_clear.gd (black hall opening), l14_temple_doors.gd, Z01 spider burrow + quill passage (first steps, not passable).

Task (meta duck first, write it into your NOTES):
1. Intent + player contract from the book and g_276/g_278: each door leads into a separate chamber that is the only thing visible,
   black around it; walking back returns you.
2. EXACT: which door leads to which chamber, the chambers' puzzles/gates. APPROXIMATE: how other chambers are kept out of view.
3. Likely cheapest faithful option: treat each chamber as its own visibility island (draw only the island you are in plus the
   door's view), instead of tuning portal edges face by face.
4. Prove like a player: an earned walk through every door + captures compared with g_276/g_278; the owner walks it.
Deliver as a branch + RELEASE notes; post "[fable] TEMPLE-ISLANDS ..." lines on the board. Rules: typed GDScript vars, tests print
PASS + registry json, ledger rows as docs/deviations pieces + tools/build_deviations.py build. Player-side effects before world
changes (owner rule 2026-11-07).
