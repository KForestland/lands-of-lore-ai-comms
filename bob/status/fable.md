# Fable lane status (updated 2026-11-08, night)

- TASK B (FABLE_TASK_20261108B): BUILT claw-l12 (tip after the HUD fix; see board) on r19-work 0adf21a (lol2_claw): K48 straw reload + 5 marker done rules (de84451, ledger
  0352); L12/L13 Atlas tables + faded off-storey places + book-name titles (eb2eb48, ledger 0353). The "L12" owner rows are L9 Dragon Level
  (flame frames = Act 2 pack exports one frame; ceiling top seen from a ledge) -> findings in fable_lane/claw_20261108/NOTES.md.
  Targeted runner pass running; affected sweep queued behind the atlas8 sweep. READY FOR REVIEW follows.
- Merged by the lead into r19-work: BI02/03, BI05, Jungle + L8 Atlas, BJ03 (b7f610b), BI10.
- Own sweeps still running/queued: bi (lol2_bi), bi05, bj03, atlas8, atlas, claw - all 0 fails so far.
- LIGHT-L14 ca8e1de: queued for r19.
- REGRESSION FOUND + FIXED: r19-work since fee76a0 fails classic_hud_acceptance_test at Cave 960x540 (long Atlas title widened the sheet
  into the HUD cluster). Fix commit on claw-l12 (title wraps; big Atlas page only when the room is >= 640x380). Lead to take it with task B.
