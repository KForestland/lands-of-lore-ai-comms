• # Pre-merge review: 3a932b3 "Preserve ordinary climbs before Act 2 body fitting"

  Reviewed the full diff against bf8b21f, the complete current text of `act2_body_fit.gd`, `act2_map.gd`, `jungle_review.gd`, `walk_step.gd`, `walk_feel.gd`, the class chain (`jungle_review` ← `jungle_walkthrough` ← `act2_map`; fit hosts are exactly L10/L12/L13/L14/L16/L17/L19/L20), and the evidence in `sol_lane/task3c_gulch_fix_20261110` (WALK_GATE_SUMMARY: 228/228 pass, 0 stalls, only the known pre-3c L16 tower-probe reset; all six changed source hashes in `final_candidate_hashes.json` match the committed files byte-for-byte; worktree clean apart from the known untracked runtime assets).

  ## Defects found

  None that block merge.

  ## Concerns checked and dropped

  - **Camera/eye bookkeeping across `allow_fit=false` transitions** (`act2_body_fit.gd:119-121,174-177`): walked the arithmetic for fit→unfit; the camera is restored to exactly its pre-fit height on the transition frame and stays stable afterward. No drift.
  - **`needs_world_fit` false positives from resting contact** (`act2_body_fit.gd:102-112`): worst-case resting floor/wall contact depth is `safe_margin + query.margin` = 2·safe_margin+0.01; the threshold is 2·safe_margin+0.02, and even a false positive is self-correcting because `begin`'s trimmed `_fits` probe then reports the body fits and no resize happens. Held.
  - **Blocked timer accumulating during airborne/jump frames** (`act2_map.gd:468-470`): a fit can be admitted at jump apex against an overhang, but only when the small body genuinely fits a linked region with real support below; no support exists to "drop" mid-air and velocity is unchanged. Dropped.
  - **Direction-change reset is per-frame (dot<0.95)**: walk_feel easing rotates velocity only ~3°/tick at walk speed, so the "same direction" requirement survives smooth turns and resets correctly on real reversals. A 90° corner turn can carry up to ~0.5 s of prior blockage around the corner — but admission still requires the full body to genuinely not fit plus support ahead, so no fall vector. Observation only.
  - **Rapids test no longer requires a resize** (`tests/act2_body_fit_walk.gd:181`): disclosed in the registry note and deviation row; physical crossing, region-visit, F5/F9, no-reset and contact assertions all remain, and the blood scenario plus the contract test still pin actual fitting. Disclosed weakening, not a hidden one.
  - **`jungle_review.gd` refactor**: pure extraction (`_try_grounded_step`/`_move_grounded_body`); order and semantics for all non-act2 hosts (L8/L9/L11/L15/L18) are identical to bf8b21f.
  - **Movers/doors**: fit probes exclude mover RIDs and layers 2|256, so a closed native door reads as "fits" and never triggers a duck-through. Held.

  ## Move-order walk (the question asked)

  **Stair step-up.** Per frame: velocity set → jump check → ordinary full-body step (`jungle_review.gd:486`, swept rise ≤32, overhead clearance checked) runs *before* any fit decision; the fit override (`act2_map.gd:451-453`) only suppresses it when a fit is already active or the full body already deeply overlaps terrain. A successful step zeroes velocity, which forces the timer-reset branch (`act2_map.gd:458`). The 0.5 s wait can only delay a *new* fit; it never delays the step, and the step never removes support because it is swept with the full body. If the rise truly defeats the full body in a linked region, admission waits for 0.5 s of <5 cm/tick travel, then the *fitted* body gets its own step attempt (`act2_map.gd:463`). No support drop, no new stall.

  **Jump.** `velocity.y > 0` at launch and through ascent; the timed admission branch requires `velocity.y <= 0.0` (`act2_map.gd:460`), so a jump is always launched and resolved with the full body — the ordinary step/jump gets first chance exactly as documented. An already-active fit deliberately persists through the jump with its valid fitted shape.

  **Reload inside a tight passage.** First physics frame after `apply_save`: `needs_world_fit()` probes the *complete* original body (untrimmed foot, overridden query shape/transform) and admits fitting immediately on deep overlap — no 0.5 s wait — while the ordinary step is suppressed so nothing shoves the interpenetrating full body. Test 1307 verifies idle settling in a freed-and-reloaded fresh scene with resets==0. This is exactly the v4-candidate regression class (fresh reload stalling/falling) and the fix is targeted at it.

  **Narrow floor edge.** A new fit requires (a) real blockage for 0.5 s in one direction, (b) linked-region motion, (c) `_supported`: an actual floor with normal.y>0.7 within ~32 below, 2 units ahead, and (d) min 8×8 size with unchanged foot offset. Over the L12 gulch the ray finds nothing → no fit → the full body keeps its rim support; the failure mode that dropped Luther (shrinking the radius off the supporting lip) is guarded at admission, and `finish()` restores the full shape plus a mover/prop contact clamp after every move.

  ## Routes I'd still watch (residual, not defects in this diff)

  - **L16_CA avenue/terrace parapet edges**: the earlier candidate's avenue falls came from linked polygons extending past parapets with support within 32 below; the guards now fail safe (no fit without genuine blockage + support), and `l16_terrace_lip_earned_test` plus the full L16 suite pass, but a <32-deep drop beside a squeezable blockage remains the structurally exposed case.
  - **L17_HC cave throat (regions 1236/562 overlap)**: `_linked_motion` depends on the region pick that `apply_save` itself flags as ambiguous there; a wrong pick makes admission fail toward *no fit* (full body, original behavior) — a possible 0.5 s hesitation at a genuine tight spot, not a fall.
  - **L12_CM shallow crevasse/raft-bank squeezes**: the support ray reaches the crevasse floor, so a genuine 0.5 s blockage there can legitimately fit and descend; covered by the crevasse/gulch/return suites with resets==0, including the new reload-before-cap test.

  All three fail toward "keep the full body" rather than toward an unearned fall, and all are exercised by the 228-test gate on the exact committed hashes.

  APPROVE
