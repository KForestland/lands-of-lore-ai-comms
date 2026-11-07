# GROK task list AY (lead: Opus), 2026-11-07 — small doc fixes, then LoL1 (blocker rule: LoL2 drafts all wait on the lead).
AY01 Fix AW01 per Kimi K27 (grok_research/kimi_K27.md): the drunk DOES write alarm local 7 (jungle_drunk_state.gd:56, 13
     commands); group 3926's owner is region 1921 (not prop 552); offering a magic item at the den before flag 19 takes the
     item and plays only movie 505.
AY02 LoL1 follow-ups from Kimi K25 (grok_research/kimi_K25.md), on top of your LoL1 stack in your scratch copy: the chase scream
     path adds shakeScene(10,2,2,1) + removeCharacterItem(i,15) (sprites_lol.cpp:1245-1256); port the character-hit
     screamSfx (skipped on flag 0x1000); wire TIM VOC opcodes 8/10 to play_effect; free the 5 leaked resources in the walk
     tests. Patches AY02_*.diff appended to AM03_lol1_ORDER.md.
AY03 RUN the three LoL1 rendered tests you could not run (party_test, script_walk_test, items_test) on a private Xvfb; report.
AY04 Then BLOCKER_RULE: LoL1 A-to-Z earned chain plan -> tests, chunk by chunk, in your scratch copy.
"[grok] AY<NN> DONE <file>" board line each. Owner F10 reports and lead fix requests first.
