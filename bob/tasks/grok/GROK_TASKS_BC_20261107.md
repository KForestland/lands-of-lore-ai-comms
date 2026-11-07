# GROK task list BC (lead: Opus), 2026-11-07 — two Act 3 fixes from Kimi K28 (grok_research/kimi_K28.md). Before BB items.
Base: lol2_act3 branch act3-chain (applied). Patches in grok_research/patches/ACT3C_fixes/. RUN tests.
BC01 STORY-078 dragon-room telepad: in our port walking onto it only sets pad_seen and travel needs aimed E (l16_dragon_room.gd:82-90).
     Meta duck it: a one-way teleport is walked onto. Check the longplay (I33 frames) and the native control 74 kind 5 record; if the
     original travels on step-in, make it walk-on (adapter, ledger row), earned walk without E.
BC02 STORY-072 white ball: book 4831-4832 = a third-level summoned IMP or a fireball from the spark spell altered by a PYRAPOD breaks the
     ice ball; our port breaks it with any spark of level >= 3 (l16_nw_traps.gd:25,119-121). Match the book (imp level 3 or pyrapod-spark);
     if a spell system piece is missing, keep the adapter, log it, and post an owner question on the board.
BC03 Fix the AX01 citation nits (088 -> line 5506; 074 -> 5155-5164; 069 add 4842-4847/4896-4897/4921-4923; 092 frame times).
"[grok] BC<NN> DONE patch <file>" board line each.
