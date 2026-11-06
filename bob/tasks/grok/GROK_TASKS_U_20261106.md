# GROK task list U (lead: Opus), 2026-11-06 — LoL1 Classic research (owner asked). Read-only research, no Godot edits.
Base: ~/lol1_godot (check HEAD; specs were written at 9987d7e), your L01-L07, M03-M05, N04, O05, P01-P08.
Behaviour reference: ~/scummvm-lol1-fork/engines/kyra/, decompiled scripts ~/lol1_scripts_decompiled/,
RE repo notes (github KForestland/lands-of-lore-1-re), level maps ~/AI_COMMS/MAPS_LOL1/.

U01 The P07 gap: chunk 8 (White Tower, Cimmeria, cards LOL1-12/13) has no step source. Find one: a full LoL1 walkthrough
    or hint book (GameFAQs, the Westwood hint book, landsoflore.de, the German secrets guide if it covers LoL1) and write
    LOL1-12/13 as step cards with level numbers + block ids checked against MAPS_LOL1 and the decompiled scripts.
U02 Same check for LOL1-07..11 where P06 says "as far as the walkthrough is written": fill any missing steps.
U03 One table grok_research/lol1_story_full.md: every card LOL1-01..13 -> levels, key blocks/flags, items, NPCs, cutscenes,
    the EMC calls each level reports missing (from level_scripts.gd's missing counter if it can be read without running).
U04 Re-check L06 sizes against U01-U03 and the current tree; write one short updated plan, L06b, with the order and risks.
"[grok] U<NN> DONE <file>" board line each. Start only after list T is done. Owner F10 reports first.
