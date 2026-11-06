# GROK task list AO (lead: Opus), 2026-11-06 — LoL1 Classic chunks 8 and 9: the end of the game + sound (drafts, stacked on
AK..AN, scratch copy, RUN the tests). Specs: P07 + your U01 step source (White Tower, Cimmeria, cards LOL1-12/13), P08 (sound).

AO01 Chunk 8: cards LOL1-12 and -13 from U01 (White Tower, Cimmeria, the final fight and ending); same missing-EMC-call rule.
AO02 Chunk 9 sound per P08: fill playSoundEffect (215 VOC) and music (67 files) after the levels that call them; no change
     to earlier chunks' logic. A headless test that the calls resolve to existing files.
AO03 ORDER.md updated (AK01..AO02), each with its test and PASS/FAIL from your run; plus one A-to-Z earned-walk plan for LoL1
     (which save each chunk test starts from and ends with), like LoL2's act3_chain_status.md.
"[grok] AO<NN> DONE patch <file>" board line each. Owner F10 reports first; LoL2 fix requests from the lead first.
