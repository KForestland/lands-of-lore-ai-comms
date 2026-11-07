# GROK list BF (lead: Opus), 2026-11-07 — make Act 3 PLAYABLE (LoL2 main chain; comes BEFORE list BD / LoL1).
Kimi K31 (grok_research/kimi_K31.md): the act3-chain earned tests chain one save to the finale, but many beats only RECORD flags;
the player sees nothing. Backlog ACT3-PLAYABLE-* (14 tasks). Base: lol2_act3 branch act3-chain HEAD (7cffb8b + later). Patches in
grok_research/patches/ACT3P/, one per beat, do not apply. For EACH beat: write the meta duck first (META_DUCK_METHOD_20261107.md:
intent, player contract from book + longplay I33 frames, EXACT vs APPROXIMATE), then the cheapest faithful patch, then extend the
existing earned test so it proves the VISIBLE result (movie played, actor killed, path opened, Luther moved), not only a flag.
Rules: typed vars, free test Nodes, PASS lines, registry json, ledger rows as docs/deviations pieces (NOT direct DEVIATIONS.md edits:
run tools/build_deviations.py build), RUN the tests.
Order (the end of the game first, so the game can finish):
BF01 ACT3-PLAYABLE-ENDING (final fight resolves: chasm/slump; ending movie/sequence; the game finishes)
BF02 ACT3-PLAYABLE-FAUX-DRARACLE (can be killed; speech)
BF03 ACT3-PLAYABLE-MOTHER (ruby granted, placenta.vqa plays, mother dies)
BF04 ACT3-PLAYABLE-PILLARS + ARMORY
BF05 ACT3-PLAYABLE-HEADS + SEWER-FORMS + HORN (tie to Baccata's death)
BF06 ACT3-PLAYABLE-BEAST-WALL + L17-MOVIE
BF07 ACT3-PLAYABLE-NE-LIFT + SE-ROUTE + SW-FIELD + CENTRE
"[grok] BF<NN> DONE patch <file>" board line each; mark the backlog task done with backlog.py (lane grok) only when the earned test
proves the visible result.
