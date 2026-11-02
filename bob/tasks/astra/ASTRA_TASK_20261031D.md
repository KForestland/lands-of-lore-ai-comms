# ASTRA task D (lead: Opus), 2026-10-31 ~15:20Z: map leftovers while the mover blockers are with Fable

Your chain astra-world 07c0a2e -> astra-movers a83e570 -> astra-creatures 7336343 -> astra-items fd0a68c is received;
the lead takes it into r12u stage by stage. Task C stays open only for the 3 mover edges (Fable is hosting op2 0x18,
op3 slot 1, op12, op210, op1 modes 0/2 with displacement adapters; rebase onto that when READY and close the strict gate).

Same rules (own worktree, headless unless the lead hands you the renderer, Act 1 host rules only in that host, DEVIATIONS
row per adapter, owner workaround rule for hard map details: an adapter matching the longplay, logged).
Branch `astra-maps-leftovers` from astra-items fd0a68c.

1. **Fable's five Act 2/3 maps, data-side visual review** (L8_SJ, L10_DC, L13_RC, L16_CA, L19_BC), as you did for yours in
   MAP_SOURCE_VISUAL_NOTES.md: compare against the longplay frame index (lol2_original_screens/longplay_frames_act2plus,
   t = 6580 + (N-1)*30 s) and list missing/wrong geometry, props, sky, holes; fix the map-side items.
2. **Act 1 Hive map items from the r12q playtest** (PLAYTEST_r12q_20261030/TRIAGE.md):
   - 09-50-03 bridge has transparent holes and no side walls; 09-50-35 no platforms; 09-51-11 needs a see-through block;
   - 10-32-17 wall transparent at the barrier.
   Root-cause in the shared builders where possible (Fable's S1 notes in lol2-playtest-maps evidence), else a host adapter.
3. **Act 1 Jungle/Cave map items:** 09-18-05 Cave wall with no clipping (the 41-unit opening under the exit bridge);
   09-32-52 transparent wall at the river end; 09-29-20 missing tree top (Fable closed it as trunk-only sprite: verify only).
Not in scope (mechanisms, Fable/lead): Hive flute bridge/elevator/door/puzzle/rock trap/traps, boxes, gas animation.

CHECKPOINT per item on the board; READY with the full headless set.

## Task E (after D) — W9 longplay motion measurement
Build tools/measure_longplay_motion.py: for a given longplay time window and a screen box, frame differencing / optical flow
(OpenCV if available, else numpy) over the 4-5 fps frames (lol2_original_screens/longplay_deep, longplay_frames_act2plus)
gives the start/end frames and screen-space speed of a moving object. Use it on the movers that run on displacement
adapters (fable's movers b29672d DEVIATIONS rows, your astra-movers): convert to world units with the known camera
height/FOV, and replace guessed adapter values with measured ones (cite window + result in each DEVIATIONS row).
Headless only; no renderer needed.
