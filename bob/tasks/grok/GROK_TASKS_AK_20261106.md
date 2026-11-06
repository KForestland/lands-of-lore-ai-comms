# GROK task list AK (lead: Opus), 2026-11-06 — LoL1 Classic, first build chunks (drafts; the lead applies later).
Owner order stays LoL2 first; these are prepared while the LoL2 drafts wait for the lead. Project ~/lol1_godot
(HEAD 9987d7e, clean; GPL-3.0-or-later, logic from ScummVM Kyra ~/scummvm-lol1-fork/engines/kyra/). Work in a
scratch copy, never in ~/lol1_godot. Data: <owner-media> via tools/import_lol1.py.
Specs: your O05 (chunk 1), P01 (chunk 2), L06b plan. Same code rules as LoL2 (typed vars, tests print PASS, free Nodes).

AK01 Chunk 1 save/load per O05: flag bytes, script words, money, lamp oil, block, facing, the hero, item chains, live
     monsters; write + read back; a round-trip test. Patch grok_research/patches/AK01_lol1_save.diff.
AK02 Chunk 2 hero select per P01: the selection screen with the four templates (Ak'shel, Michael, Kieran, Conrad), the
     choice saved by AK01; test. Patch AK02_lol1_hero_select.diff (stacked on AK01).
AK03 NOTES: how to run the tests headless in lol1_godot, and what the owner should see when he starts it.
"[grok] AK<NN> DONE patch <file>" board line each. Owner F10 reports first; LoL2 stack-fix requests from the lead first.
