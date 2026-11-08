# Fable lane status (updated 2026-11-08, late night)

- BJ05 (FABLE_TASK_20261108C, L12 Claw Mountains owner-like walk): worktree lol2_bj05, branch bj05-claw-walk on r19-work b4a10bc.
  - Commit 1d3f58f: tests/l12_main_chain_walk_test.gd (arrival -> gulch -> valley -> glacier -> ice caves -> Kenneth (E, inventory,
    right-click) -> ice hops -> far cave -> Baccata (E) -> citadel movie -> L13; quicksave/reload at every stop); Atlas storeys are
    pile levels, not nav fragments (L12 gulch drew 6 of 66 explored regions; fixed, ledger 0355); atlas_readable_l12 walks the
    earned gulch route. Four readable-Atlas tests + storey/sections PASS.
  - Commit 2 (pending its test run; lead to take or drop, mechanics): citadel entrance no longer waits for the Baccata talk
    (native control 74 has no predicate; without the L8 rescue the player was held forever). Ledger 0356.
  - Findings on the board: Baccata dead end; Dawn at the gulch unhosted (region event 4 never entered by the binder); explored
    pollution in the STORY-035 arrival save; event-4/1 region owners in L12 never fire.
  - Evidence: fable_lane/bj05_20261108/ (NOTES.md, captures, probe log, longplay sheet).
- Merged by the lead into r19-work: BI02/03, BI05, Jungle + L8 Atlas, BJ03, BI10, task B (claw-l12 + a23cfb4 HUD fix).
- Sweeps: bi 692/692 PASS; bi05/bj03/atlas8/atlas still running (bases carry the pre-fix classic_hud_acceptance fail); claw affected running.
- LIGHT-L14 ca8e1de: queued for r19.
