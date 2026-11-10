# Gap audit of the master plan (lead, 2026-11-10). Fable folds this into MASTER_PLAN_COMPLETE_GAME.md and master_tasks.json after BJ14.
Full evidence: grok_research/kimi_K78.md (content vs hint book) and kimi_K79.md (systems and reverse engineering).

Fold in:
1. K78 gaps 1-3: L16 side rooms (storeroom, chalice dream, transformation exhibits, Silverleaf chasm, four chip quests); L9 door rafting and Saar death-match room; level-5 spell charge gating and no-target fizzle.
2. K79 gaps 1-10: difficulty levels (Easy/Medium/Hard; byte 0xB7FB2, part of the R-01 decode); F-11 must cover all region event bytes 0/1/2/3/4/5/7/9, not 1 and 4; native timer and event-producer service; options parity (gamma, mouse sensitivity, bobbing); compass; A-01 widened to the HMI/MIDI path and X-02 depends on A-01; imp altar drain; player-facing failure behaviour; fog and distance shading in M-17; Extras menu replay.
3. K79's ranked reverse-engineering list: assign each to a task for Grok or Sol.
4. Owner since your update: D9 guck drain is very slow, about 5 minutes wading to be fully drained (owner-set value; M-16). The imp altar drain is a separate thing the owner will check in DOSBox. D10 music order: decode, else rip the CD music from the player's own copy, YouTube OST as a fallback for private playtests.
5. My mechanical check: all deps valid, no cycles, all 574 rows triaged. Six tasks depend on later phases: M-10 on S-20, M-15 on R-10, I-04 on R-01, I-07 on R-06, I-10 on R-03, U-06 on X-01. Each needs reordering or a stated reason.

Then re-read the whole plan once for cohesion and say on the board what changed and whether the date range moves. Plan only. End the plan with PLAN READY.
