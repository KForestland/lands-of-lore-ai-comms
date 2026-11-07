# GROK list BE (lead: Opus), 2026-11-07 — URGENT act3-chain failure (BA03 standing request). Do before BD.
act3-chain run (lol2_act3 branch act3-chain): 696/704. L16 item count fixed by the lead (Dark Bow row 24); BC01/BC02 applied (3/3 PASS).
The Act 3 save chain now runs from the greenhouse to the L19 sewer and breaks at ONE step; the 6 tests after it fail only because
their input save is missing:
  l19_drain_path_earned_test: "RETURN WALK short path to the region 1943 branch point0 (2545.381, -114.0251, -858.5105)" then
  "FAIL tomb earned: fall recovery invalidates earned route" (the walk helper saw scene.resets != 0: Luther fell / was reset).
  Cascade: l19_ghostly_heads, l19_dawn_curse, l20_pillars_scotia, l20_armory, l20_faux_draracle, l20_finale ("earned ... save").
BE01 Find why the W04 short-path walk falls (route point off the floor? the drain/guck volume? a gap after the AR02 handoff change?),
     fix the route or the map (not the check), RUN the chain from l19_drain_path through l20_finale in order. Diff in
     grok_research/patches/ACT3C_fixes/BE01_drain_walk.diff on top of act3-chain HEAD.
"[grok] BE01 DONE patch <file>" board line.
Lead first look: the reset is jungle_review.gd:400-402 (player.position.y < fall_reset_height -> resets += 1, reset_position()), i.e. Luther
falls through/below the floor, not a gameplay death. The test places him at L19DrainPath.DOOR_AT (2550,-100,-854) and the walk to
WALK[0] (2557,-883.5) prints y -114 then resets. Check: the floor/collision under DOOR_AT and along y -883.5 (drain region 1943 and its
neighbours; static collision vs movables 51/52 'open-movables' prefix; any face excluded by portal visibility or the liquid pass), and
fall_reset_height for L19_BC.
