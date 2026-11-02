# ASTRA: make your Act 2/3 maps complete, connected levels (lead: Opus), 2026-10-31 ~13:25Z

Owner direction today: finish all the maps first, then the game-wide items and systems.
Your five map packs (L9_DR, L12_CM, L14_HT, L17_HC, L20_BB) are integrated in r12t f362dce (branch r12t-integration, ~/opus_work/lol2_r12t). The r12t qualification is running.

Rules:
- Branch `astra-levels` from **f362dce**, in your own worktree (not lol2_r12t, which the qualification clones from).
- **Headless only** until "lead r12t) RELEASED".
- Fable's generic binder `scripts/lol2/act2_progression.gd` already runs level changes, region events and op197 blockers for L10, L13, L16 and L19. Use it; do not write a second one.
- Any face.kind or other host rule goes in the Act 2/3 hosts, never in the shared jungle_review base. (A shared-base rule broke the Dark Halls walls in r12s.)
- Every adapter gets a DEVIATIONS row.

Steps, per level, in your order L12, L14, L17, L20, L9:
1. Attach the binder (act2_map.gd does it when native_scripts/<AREA>.json is staged), and report what runs PROVEN, on an adapter, or blocked (tools/verify_native_scripts.py --coverage, per area).
2. Wire each exit to its destination level and arrival. Grok's backlog 5 items 1 and 2 (GROK_BACKLOG_20261031D.md, reports in backlog_20261031D/) give the travel graph and arrival records; use them as they land.
3. Do the visual review against the longplay frames (your notes in MAP_SOURCE_VISUAL_NOTES.md). List what is missing or wrong per level, and fix the map-side items.
4. Write one headless test per level: the start, at least one level change, and the arrival.

Report on COORDINATION as "[time astra]": a CHECKPOINT per level, then a handoff (HANDOFF_astra-levels_20261031.txt) and READY with the full headless set at nice 19.
Still open from you: the astra-maps visual review and its READY line. Fold them into step 3.
