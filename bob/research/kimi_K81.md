• # Pre-merge review: 6dfef01 "Host L19 guck drain at the owner-set D9 rate"

  Reviewed the full diff against cbf19b6 plus the host code it hooks into (`act2_map.gd`, `jungle_review.gd`, `act2_progression.gd`, `player_starting_magic.gd`, `liquid_drowning.gd`, save chain `act2_save.gd` → `jungle_save.gd` → `act_one_quest_state.gd`), the real L19 geometry data, and Sol's evidence (`READY.json`, `acceptance_v4` report + log, `affected_v2`). I did not run Godot; I re-verified the risk list statically.

  ## Owner risk list — each checked against the code

  **Kill faster than ~5 min?** No. `l19_guck_drain_state.gd:24-30` debits `delta * maximum / 300` health and `delta * maximum / 150` mana per tick, delta-based so tick-rate independent (unit test proves 1/60/240 Hz equivalence). From full health 30, death is at 300 s of active contact. The earned log shows 291.8 s because the F9-restored remainder of 0.818 points was carried — exactly the predicted value, not an acceleration. No other path decrements health.

  **Run outside the guck?** No. Contact is a foot ray (`l19_guck_drain.gd:27-39`) resolved to the actual supporting shape: static regions are matched by `R<region>` shape name against regions parsed from `geometry_file` (I confirmed L19's `area.json` has `floor` faces with material `211__front`/`266__front` in 60+ regions, and `265__front` floors exist and are correctly excluded), and opcode-196 decks are matched by region key against `progression.floor_decks[...].get_node("Collision")` (an `AnimatableBody3D` on layer 1, matching the ray mask). Dry overlays are hit first by the ray and fail the guck-region lookup; non-guck decks fail the same lookup. The node is only attached for `area_id=="L19_BC"` (`act2_map.gd:292`), and L19 is in `REGION_COLLISION_AREAS` so `region_collision_body` is the per-region body this code expects.

  **Keep draining after he leaves?** No. `wading()` is re-evaluated every physics tick; on the dry bank the ray hits a non-guck region shape and the fractions simply stop advancing. The earned test verifies frozen clock/health plus resumed mana regeneration over 12 s on the bank.

  **Double-count across save/reload?** No. The integer values (health in inventory, mana in `player_magic_reward_state`) and the sub-point remainders (`quests.l19_guck_drain`) are saved and restored as one consistent snapshot; `advance()` resumes from the remainder instead of re-charging it. Save validation hooks in through `act_one_quest_state.validate` (`act_one_quest_state.gd:50-52`), which is on the Act 2 save path via `jungle_save.gd:42`, so malformed remainders are rejected on load. F5/F9 and fresh-map recreation are exercised in the earned test.

  **Break regeneration or drowning?** No. The regen hold (`player_starting_magic.gd:242-244`) is scoped to hosts that have an `L19GuckDrain` child and only while `wading()` — all other maps and all dry time are untouched. Drowning is untouched code; the drain dies through the same `set_health(0)` → `player_fallen()` (`jungle_review.gd:442-444`) "You fell · R / F9" flow, and while drowned `world_active()` is false so the drain cannot stack onto a corpse.

  ## Concerns checked and dropped

  - Idle-frame `intersect_ray` from `player_starting_magic._process` via `guck.wading()`: the codebase already raycasts from non-physics callbacks (`spark()`/`crystal_fire()` via `_unhandled_input`), and the project uses default GodotPhysics, where the space is unlocked outside the physics flush. Dropped.
  - Jump exclusion is partial (ray spans feet ± 2 units, so takeoff/landing still counts as contact): worst case is fractions of a second of extra exposure per hop, in the "slightly more drain" direction only. Not a defect.
  - Health rate scaling when earned fighting maximum > 30 can drain a 30-HP Luther in under 300 s: this is exactly the owner-set D9 adapter ("greater of the port's 30 full health or earned fighting maximum"), documented in the deviation row. Not a defect.
  - The four new `.gd` files have no `.gd.uid` companions while the repo mostly checks them in: cosmetic only — Godot regenerates them and the acceptance suite ran green without them. Dropped.
  - Rendered `docs/DEVIATIONS.md`: not part of the patch (per instructions, not a defect).

  ## Evidence cross-check

  `READY.json` and `acceptance_v4/report.json` agree: 18/18 pass across `moving_floor_v2` (2), `affected_v2` (15), `acceptance_v4` (1, the full 1279 s real-input wade, PASS line confirmed in the log). Registry orders 1308/1309 don't collide (1300–1307 are taken by unrelated tests). No staging issues in the commit itself; the touched files match the evidence hashes per Sol's ledger claim, and my independent read of the data files (guck materials, region sets, deck structure) matches what the code assumes.

  I found no real defects.

  APPROVE
