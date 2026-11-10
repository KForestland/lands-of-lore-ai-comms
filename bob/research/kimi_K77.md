• # Pre-merge review — Task3c auto-fit body (036c3cba on b3e384e)

  Scope reviewed: `scripts/lol2/act2_body_fit.gd` (new), the `act2_map.gd` hook at `scripts/lol2/act2_map.gd:437-442`, its interaction surface (`player_form_body.gd`, `player_crouch.gd`, `walk_feel.gd`, `walk_step.gd`, `region_blockers.gd`, `jungle_review.gd` movement/reset, `act2_progression.gd` regions/movers/decks), the three new tests and fixtures, and the handoff/acceptance evidence in `AI_COMMS/sol_lane/task3c_20261110/` (GATE_AUDIT 43/43, both receipts `passed: true`, `resets==0`, `teleports: 0`, door uses 64/65/69).

  ## How the mechanism actually constrains movement (verified in code)

  - The reduced cylinder exists only synchronously inside `move_grounded`: `begin()` swaps shape+offset and `force_update_transform()`, `super.move_grounded()` runs `move_and_slide`/`walk_step` with full collision, `finish()` restores the original shape/offset and flushes before any other node runs. `RegionBlockers._physics_process` (`region_blockers.gd:44-60`) therefore never sees the transient radius, so the portal chamfer clearance is not rebuilt smaller.
  - Admission (`act2_body_fit.gd:74-105`) requires a full `cast_motion` clearance (fraction ≥ 0.999, margin grown) over the frame's real lookahead, a linked-region gate, a downward support ray, and a floor of 8×8 — exactly the Lizard body that already legitimately exists in these maps (`player_form_body.gd:4-6`, and L19 sewer forms exist in `act2_map.gd:294`).
  - The `finish()` full-form sweep (`act2_body_fit.gd:140-152`) excludes only concave terrain bodies, region blockers, and floor decks — I verified scenery/prop bodies are `BoxShape3D` grandchildren (`static_assemblies.gd:173,206`) so they are *not* misclassified into `world_rids`, and movers/creatures stay in the sweep.

  ## Stated-risk concerns — checked and dropped

  - **Walk through walls**: dropped. Movement collision is untouched during the move; the admission probe itself requires total motion clearance. The small body can only occupy space that physically admits it.
  - **Into closed doors**: dropped. Movers are excluded from the *admission probe* only; they still collide during the move and are included in the full-form clamp sweep, so the player cannot end a frame past a door the full form can't cross. The witness stalled at closed movers 64/65 until real E opened them (receipt `native_door_uses: [64, 65, 69]`).
  - **Out of the map**: dropped. Requires a genuine ≥8×8 hole in collision geometry; the fitted body is bounded below by the existing Lizard form, and region blockers (layer 512, present in the player's mask and not masked out of the probe) still collide with the small body.
  - **Stuck when space doesn't return**: dropped. Restoration is re-evaluated every `begin()` (first branch), `move_grounded` runs every physics frame even idle, so re-fit happens before any `move_and_slide`; eye restore via `prior_eye`/`eye_adjustment` is non-accumulating, and `walk_feel.bob` only touches `v_offset` so it can't desync the bookkeeping.
  - **Creature/prop contact change**: dropped. The ordinary shape is on the RID between frames (asserted every sample by the walk witness); the sweep preserves outgoing contact, verified against independent full-body references in `act2_body_fit_contract_test.gd` including incoming-creature contact.
  - **Form changes**: dropped. `begin()` captures whatever shape/camera the form owner set that frame; `finish()` restores that capture; the `prior_normal` guard drops stale eye adjustments on shape change. Form admission (`Body.apply` check_space) runs its own probe and never observes the transient cylinder.
  - **Save/reload**: dropped. No saved fields; the shape is always restored at save time; after F9 the first (even idle) tick re-fits before movement. Both witnesses physically repeat the crossing after F9.
  - **Crouch key**: dropped. `player_crouch.update` runs before `move_grounded` in `jungle_review._physics_process` (`jungle_review.gd:452`), so begin sees the crouch shape/camera and restores it; witness verifies 32 on hold, 46 on release. Crouch refusal under a sub-32 header behaves as before.

  ## Residual observations (not blocking defects)

  - Conditional/latent, low: if the player ever fell below `fall_reset_height` *while fitted* (`jungle_review.gd:491`), the `finish()` sweep from the pit to the reset point could clamp against a prop on that line and undo `reset_position()`. This needs a genuine out-of-map hole reachable in a fitted state — none evidenced (both witnesses report `resets==0`), and out-of-map falls in open air are not fitted so the sweep doesn't run.
  - Transient/cosmetic: a save taken mid-passage reloads with the full body geometrically overlapping a low header until the first tick re-fits; there is no crush system and movement re-fits before `move_and_slide`, so the practical effect is nil.
  - The probe's exclusion of layers 2|256 (creatures/scenery) only over-admits fit; movement and the sweep still enforce those contacts.

  The rendered `docs/DEVIATIONS.md` row is accepted as documentation, per instructions.

  APPROVE
