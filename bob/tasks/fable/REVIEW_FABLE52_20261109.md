# Review for the lead (Fable 5.2, 2026-11-09, read-only)

Sources: board (last ~150 lines), RESTART_HANDOFF_20261109, GROK_TASKS_BK/BJ, Kimi K45-K70 (headers and verdicts; I did not
re-read every review body), my own BJ11 walks on 8601810/c6a7b8e and ONE L19 sitting on b3e384e. Items marked (unverified
on b3e384e) were seen on older bases and may be cleared by BK07b/BK08d-f/BK09b.

## 1. Five biggest blockers to a playable main chain A-Z (ranked)

1. **The player body does not fit native passages (L19 first, Thursday-critical).** The blood pool channel is 24-30 wide and
   the Human capsule is 30 (stop at (-180,11,-1372), reproduced on b3e384e); the rapids "low area" (regions 760-759) has 20
   units of clearance and act2_map has no crouch at all. The earned tests teleport past both, so every suite is green while a
   player cannot reach the bars. Resolve: ONE lead decision on a body-vs-world rule, not per-spot fixes: a small world-collision
   radius for all forms (creature/prop contact radii unchanged) plus an auto-duck that lowers the capsule to the clearance
   (floor at the Lizard's 8). Lane: lead decides, Fable builds (it sits beside region-aware collision), Kimi reviews. No timers
   involved, so it does not hit the no-invented-rates rule.
2. **Liquid versus moved floors in L19.** After the flood the body floats over the raised channel deck and stalls at
   (651,-3,-2081) before region 133 (reproduced on b3e384e). The bank-model liquid surface is static while opcode 196 moves the
   bed. Resolve: liquid surface/bed follow the live region floor (progression.regions), or the flooded channel regions leave
   the liquid set while raised. Lane: Fable (liquid host) with Grok's deck API. Also decide what the owner sees for guck with
   no drain (BK13 cadence is unknown; Sol 3a correctly stopped): tell him plainly in WHATS_NEW.
3. **L19 -> L20 gate and the L20 birth beat are still adapters with holes.** Index 52 of the 0x26E58 bank is supplied by a
   seed; saving right after the birth is refused ("Absent creature has live state"); BK14 (birth via the op18 consumer) is in
   flight. A player who saves after the birth loses the session. Resolve: Grok BK14 + a save-validator fix for creatures the
   mother host clears; add a save/reload step to the L20 earned chain. Lane: Grok, Kimi review.
4. **"Green suite" is not "walkable": nobody has walked L19/L20 end to end on b3e384e.** Cab -> ring step, doors 64/65 and
   53/54, the L20 doorways and east-lip shots were each fixed in isolation after my findings but not re-walked as one chain
   (unverified on b3e384e). Resolve: before qualifying r19, one lane runs the three survey sittings
   (act3_walk_l19a/l19b/l20 in lol2_bj11r, LOL2_SURVEY=1) and posts the stop list; treat that list, not the suite count, as
   the qualification gate for Act 3. Lane: next Fable session or Sol (see fable_lane/BJ11_HANDOFF.md).
5. **Unhosted native handlers behind doors and scenes.** Door 73's kind-4 group is opcode 7 (my E bind on kind 6 caller 2 is
   an adapter, unmerged); opcode 22 is a stub; opcode 2 arms 0x23/0x25/0x35 stop groups (L20 group 7704); hw01.vqa is not in
   any MIX so the beast scene stays a card. Each one is a silent dead end for a player. Resolve: Grok lists every group on the
   main chain L16-L20 that ends "unhosted/rejected" when fired (the native host already reports status), ranked by chain
   order; fix or adapter-bind in that order. Lane: Grok, with Kimi tracing the top three.

## 2. Process and workflow (what slows us, what to change)

1. **Tests that place the player hide stops.** Rule: an "earned" test may not set player.position between two anchors; if it
   must, it prints TELEPORT and the registry row carries "teleports": N. The lead tracks the total per level; zero is the goal.
2. **Headless input paths are untested.** Handlers guarded by mouse capture never ran in any sweep until BK08d. Add one
   rendered (Xvfb) smoke test per level that sends a real click and a real E; keep helper calls only below that.
3. **Kimi is the merge bottleneck (5-hour limits, reviews queue behind each other).** Batch by merge unit, not by patch; give
   Kimi the diff plus the one risk to check; let trivial test-only and ledger-only patches merge on the lead's read. Use Kimi's
   prep traces (K50/K52/K55/K60/K67 were high value) before a lane starts, since they prevented more rework than reviews caught.
4. **Number collisions cost a rebase every merge.** Give each lane a reserved block per day (ledger and registry), as Sol
   already does (1100+, 0400-0402). Render DEVIATIONS.md only at merge; lanes ship pieces only.
5. **Staging gaps cause false reds** (indices_478.png, chain saves, pinned monastery save, liquid pack, reels). One
   `tools/stage_worktree.sh <dest>` owned by the lead that copies generated assets, untracked materials, chain saves and
   user://tests inputs; every lane uses it. My last three sweeps each lost a test to this.
6. **Findings get lost in long board lines.** One line per stop: `STOP <level> <x,z> <region> <what> <owner lane>`; the lead
   keeps a single open-stops table (level order) instead of re-deriving it from prose. Board posts via a tiny script with an
   absolute path (I lost one post to a cwd slip).
7. **Survey before fix.** The survey-mode walk (continue past each stop, list all) gave the lead a full Act 3 stop list in
   one afternoon; first-stop-fix-repeat serialises on other lanes' merges. Use survey mode first on any new level.
8. **Lanes idle while the owner's screen is busy.** Let lanes pull the next task from the task file themselves when they post
   READY (the standing backlog rule already allows it); pasting becomes the exception.

## 3. Quick wins

- Run the three survey sittings on b3e384e and publish the stop table before Thursday (1-2 hours of machine time).
- WHATS_NEW_r19: say that the pool channel and the low area can stop the player, and give the owner the F9/Journal way round;
  its L19 line currently reads as walkable.
- Port the Museum's hold-C crouch to act2_map as-is (already owner-approved behaviour); it does not solve the 20-unit crawl
  but removes the 60-high doorway class.
- Merge the two small geometry adapters from bj11-act3-walk-r2 after a gate: blood pool as liquid (surface = drawn plane) and
  door-gap floors (L19 region 1932); both are scoped and ledgered (0364 amended, 0386).
- Stage tmp/l16_dragon_room_earned_save.json and indices_478.png in every lane worktree now.
- Add save + reload after the L20 birth and at the cab bottom to the earned chain: both are known save hazards.
