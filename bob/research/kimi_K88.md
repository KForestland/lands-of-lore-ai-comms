• Review complete. I read the diff `f7013ef..2461984`, the full `l10_globe_door.gd`, the L10_DC geometry pack and nav regions, and both changed tests. The worktree is clean at the reviewed commit.

  ## The K86 defect and its fix

  My K86 low finding was that `_near` in `scripts/lol2/l10_globe_door.gd` measured distance in XZ only, and nav region 1773 (floor −150, player origin ≈ −118) underlies the whole door corridor, so the maus doors opened from the catacomb below.

  The fix at `scripts/lol2/l10_globe_door.gd:135-139` clamps Y to the leaf's vertical span and measures true 3D distance to the closed bounding box. I verified the inputs against the data:

  - In `assets/lol2/generated/maps/L10_DC/area.json`, both movables 124/125 span y 0..100 exactly (124: z −3824..−3774; 125: z −3874..−3824), matching the updated header comment.
  - Scanning `creature_nav/L10_DC.json` for every walkable region covering the door footprint, the only below-surface floors are −150 and −135 (player origin ≈ −118/−103, and the test also asserts the −43 ceiling point). All are ≥ 43 units below y 0 — outside REACH 20. The doors can no longer trigger from underneath. K86 defect is genuinely closed.

  ## Doors still open at floor height — checked, holds

  The surface corridor and east yard put the player at y ≈ 32 (or at worst y ≈ 0 given the nav floor), which is inside [0, 100], so the vertical term is zero and the trigger is pixel-identical to the old 2D check for any legitimate surface approach. The pre-existing walk portion of `tests/l10_globe_room_wall_test.gd:93-101` (shut-lane ray, then the push lane through door 124 to globe 46) is unchanged and still exercises the opening. Checked, no defect.

  ## Test additions and the double-door free

  - The new catacomb block in `tests/l10_globe_room_wall_test.gd:61-88` is geometrically consistent with the data: the `lane_z` selector keys off `leaf.zmin >= -3824.0`, which correctly maps door 124 → −3795 and door 125 → −3849 (both lane centers verified against the pack). The under/ceiling/level `_near` assertions all compute correctly against REACH 20.
  - `tests/of1_double_door_facing_test.gd` now routes every exit (five failure paths plus success) through `release()`, which frees the off-tree `door` and the in-tree `host` (whose child `gate` goes with it). On the early failure paths `host` is still null and `is_instance_valid` guards it correctly. The earlier leak is fixed; no path quits without releasing.

  ## Nothing else changed

  The diff touches exactly three files; the hinge, mesh, and collision construction in the door script are byte-identical, and `_near` has no other callers. I could not execute the tests (review was read-only, no Godot), so runtime pass/fail is unverified, but the logic and data checks above all hold statically.

  No real defects found.

  APPROVE
