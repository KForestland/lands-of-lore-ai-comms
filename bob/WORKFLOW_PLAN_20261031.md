# Workflow improvement plan (lead: Opus), 2026-10-31 — owner approved ("make this an actionable plan and execute")

| # | Action | Owner | When | Done when |
|---|---|---|---|---|
| W1 | `AI_COMMS/LEAD_STATE.md`: lead's live state (builds, merge order, open decisions, who has what), updated at every lead decision | lead | now | file exists; updated on every ACCEPT/DECISION line |
| W2 | Per-lane status files `AI_COMMS/status/<lane>.md` (task, branch/head, state READY/BLOCKED/RUNNING, next) — 5 lines, overwritten, not appended | each lane | now | four files present and current |
| W3 | Affected-test selection by content: generated media counts as changed only if its sha256 differs | lead (ai_tools/affected_tests.py) | now | an r12u-style restage selects < 631 |
| W4 | Merge-conflict removal: tests self-register (one `tests/registry/<name>.json` each, discovered by run_regressions.py); DEVIATIONS rows one file each under `docs/deviations/`, `tools/build_deviations.py` renders DEVIATIONS.md | lead | right after r12u qualifies (announced freeze ~30 min) | two lanes add tests/rows in parallel with no textual conflict |
| W5 | Deterministic timing tests (frame-count clocks, no wall time), then parallel render lanes (own Xvfb display + `taskset` CPU set per lane) | fable (after item rewiring) | next week | jungle_harvest_live_test etc. pass 10/10 under a concurrent full headless run |
| W6 | Grok depth rule: fewer items per batch, every call on the asked path must be ENTERED (decompile via ghidra_query.py / native_harness.py), "complete false" needs the exact next address | grok | now (backlog rules) | second passes name classes/fields |
| W7 | Original-game oracle: DOSBox memory-write watch from an original save at the right moment answers "who writes X" questions | grok-dosbox lane + lead | when saves exist (owner/web) | first blocked predicate answered by a watch hit |
| W8 | Differential script test: run a script group in native_harness and in the host, diff the resulting state | fable/lead | after W5 | one Act 1 group diffed clean |
| W9 | Longplay motion measurement (frame differencing/optical flow) for mover displacement and timing; replaces guessed adapter values | astra (task E) | after task D | movers' adapter values cite measured px/s |
| W10 | Reference material: Prima hintbook PDF (mocagh.org), BradyGames official guide (owner may buy), Computer Hope walkthrough, ScummVM Blade Runner VQA, C&C GPL source (LCW/AUD/MIX), hmi2mid (music, later) | lead indexes; lanes cite | now | AI_COMMS/REFERENCES.md |
