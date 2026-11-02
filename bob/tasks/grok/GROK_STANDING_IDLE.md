# GROK standing order: research + improvement when idle (owner 2026-11-02)

Applies whenever `python3 ~/AI_COMMS/BACKLOG/backlog.py next --lane grok` prints no row whose lane is grok (lane "any" rows such as BRANCH-* are builder work, NOT yours), no Astra question is
open on the board, and the renderer is not yours. Never stop just because the queue is empty. Rotate through these, one
pass at a time. Each pass ends with a file plus one board line.

R1  AHEAD-OF-ASTRA CARDS: for the next 5 STORY tasks after Astra's current one, write behaviour cards (what the player does,
    item, place, Prima/Brady page, acceptance check, which numbers are still unknown) -> grok_research/cards_<STORY>.md.
R2  ADAPTER REVIEW: read docs/deviations in the newest integration worktree (~/opus_work/lol2_r12y). For each adapter,
    is there now a printed/longplay source that makes it more faithful, or a simpler build? -> grok_research/adapter_review_<date>.md
R3  PLAYTEST REPORTS: read new F10 reports in AI_COMMS/playtest_feedback_* and MAPS/*/markers.json; group by cause and
    propose fixes with file/area -> grok_research/f10_triage_<date>.md
R4  ORIGINAL BUGS: list known original LoL2 bugs (fan sources: reference-lol2-fan-sources, landsoflore.de patches, German
    guide) not yet in the DEVIATIONS ledger, since the owner wants every one fixed -> grok_research/original_bugs.md
R5  ITEMS/RPG PREP: from Prima/Brady tables, write the item effects, spell levels, creature stats the later items/RPG phase
    will need, graded by source -> grok_research/rpg_tables.md
R6  IMPROVEMENT IDEAS: concrete quality-of-life or tooling ideas (tests that would have caught a past bug, faster checks)
    -> grok_research/ideas.md (Enhanced Edition ideas marked ENHANCED; Classic must stay original).

Rules: read-only on game code, no Godot, no DOSBox unless the lead grants the renderer. Never edit backlog.json task
status of other lanes. Proposed new tasks go as "PROPOSE <title> | source | acceptance" lines in grok_research/proposals.md;
the lead turns them into backlog tasks. Grade every claim HINTBOOK / BRADY / LONGPLAY / DECODED / GUESS. Keep status/grok.md
current. A real backlog task or Astra question always takes priority over the idle loop.
