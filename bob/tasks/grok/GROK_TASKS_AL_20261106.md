# GROK task list AL (lead: Opus), 2026-11-06 — LoL1 Classic chunks 3 and 4 (drafts, stacked on AK01/AK02, scratch copy).
Same base, rules and sources as list AK. Specs: P02 (chunk 3 combat), P03 (chunk 4 TIM opening + throne room).

AL01 Chunk 3 combat on the walking grid per P02: monster attack modes, a party attack, damage, death; numbers from the
     original tables (not LoL2); keep the ScummVM accidental large-fireball width 63 and the silent White Tower sound 255.
     Tests with fixed seeds. Patch AL01_lol1_combat.diff.
AL02 Chunk 4 TIM per P03: the opening and the throne room (cards LOL1-01, -02, -05) via loadTimScript/runTimScript, the start
     square function 557 playing the opening dialogue. Patch AL02_lol1_tim.diff + a test that the opening runs to its end.
AL03 NOTES: what the owner sees and does in chunks 1-4, start to the first fight.
"[grok] AL<NN> DONE patch <file>" board line each. Owner F10 reports first; LoL2 fix requests from the lead first.
