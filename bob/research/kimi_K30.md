# Kimi K30 — L19 drain walk fall diagnosis (2026-11-07)

Lead: correct - the Golden Doors 51/52 stayed closed; fixed (door click opens them, pose re-applied after load) and the finale horn save fixed; chain 10/10 to the finale.

All the evidence is in. Here is the report.

  ## K30 — Why `l19_drain_path_earned_test` falls and resets

  ### 1. The L19_BC `fall_reset_height`

  - Set only in `jungle_review.gd:105-110`: default `-2048`, then `min` over **every** `floor`-kind face point's y in `area.json`, minus a fixed 512 margin. Neither `act2_map.gd` nor `jungle_walkthrough.gd` overrides it (checked both).
  - Data: lowest floor point in `assets/lol2/generated/maps/L19_BC/area.json` is **y = −1250** → `fall_reset_height = **−1762**`.
  - So the log's sequence is consistent: the player sinks slowly below the floor (y = −114 at walk tick 300), keeps falling, and only later crosses −1762, which fires `resets += 1; reset_position()` (`jungle_review.gd:400-402`). The next `fight_nearby` then fails with `fall recovery invalidates earned route` (`tests/l9_chapel_earned_test.gd:3`) — exactly the FAIL in `tmp/regressions/act3c_affected/l19_drain_path_earned_test.log:740-741`.

  ### 2. Floors / regions under the route points

  Static floors (area.json, point-in-polygon on x,z):

  | point | face | region | floor y |
  |---|---|---|---|
  | (2550, −854) DOOR_AT | 3821 | 1931 | −100 |
  | (2557, −883.5) WALK[0] | 3833 | 1937 | −90 |
  | (2565, −883.5) WALK[1] | 3845 | 1943 | −100 |
  | (2621.5, −883.5) WALK[2] | 3845 | 1943 | −100 |

  Nav (`creature_nav/L19_BC.json`) agrees: region 1931 floor −100 (link →1937 at exactly `[2557.0, -883.5]`), 1937 floor −90 (link →1943 at `[2565.0, -883.5]`), 1943 floor −100. WALK[0]/WALK[1] are the nav shared-edge midpoints from `tools/build_nav_walk.py:50-60`; WALK[2] is the centre of 1943. Region 1932 (west neighbour, floor 0, no links) is a sealed zero-height region — matches the script header. **No floor is missing anywhere on the route.**

  ### 3. Collision coverage — the real problem

  - The floors above are ordinary `floor` faces: no `source_wall` flag, not in `excluded_faces`/`dynamic_floor_regions`, and `act2_map.include_collision_face` (act2_map.gd:236-251) only strips L10/L12/L13/L14/L16 specifics — so static collision **does** cover the floors.
  - But `DOOR_AT = Vector3(2550, -100, -854)` (`l19_drain_path.gd:16`) is **the placement origin of movable 51** — native placement `(x 2550, y 854, h −100)` in `native_scripts/L19_BC.json`. Movable 51's six faces (area.json faces 9039-9044) form a solid box **x 2545-2555, y −100..57, z −824..−884**; movable 52's box (9045-9050) covers **z −884..−944**. Together they fill the whole region-1931 corridor (x 2543-2557, z −824..−943) except two ~2-unit slivers the radius-8 capsule can't use.
  - Being kind-`movable` with kind-4 use records, they are scripted movers: `hinge_faces()` (act2_progression.gd:87-96) removes their faces from the static mesh, and `_build_hinges` (act2_progression.gd:353-412) rebuilds them as `AnimatableBody3D` collision posed by the native travel word. Mode byte +0x22 = 6 (rotary); angle word = 16384 (90°).
  - **Their runtime state is closed**: initial travel is not in the export, so `field(..., 0)` → 0 (act2_progression.gd:411; native_script_host.gd:469 comment). The earned save (`tmp/l19_sewer_forms_earned_save.json`) carries only quests/inventory/player — no native bank — and nothing in W01-W03 opens movables 51/52 (`l19_sewer_forms.gd` only documents movable 77 "does not move"). The door's kind-4 use toggles group 3854 (open, travel 16384) / 3998 (close), fired only by E through `act2_progression.use()` — but `aimed()` needs `dot > 0.7` with the camera forward (act2_progression.gd:458-470), and the player stands **at the door's own origin**, so the offset is straight down (dot ≈ 0); the drain path's own `_unhandled_key_input` (`l19_drain_path.gd:93-108`) consumes E anyway. The door never opens.
  - The route was planned with `--open-movables 51 52` (tools/build_nav_walk.py:24,31-39; deviation row `docs/deviations/0314-row-2026-11-06-a11-l19-drain-and-short-path-story-0.md`) — i.e. the plan assumed doors already open. The runtime never matches that assumption.
  - `git log` for the L19 files shows only the draft commits (0016f72 W04, 8b133c8 W03, …); the later "AR02_l19_l20" fix (2475c0e) touched only `l19_dawn_curse_earned_test.gd`/`l20_finale_earned_test.gd`, so this was never fixed.

  Result: the capsule is spawned embedded in the closed door-51 box, with its centre exactly on the floor plane (capsule bottom −132 vs floor −100). `move_and_slide` squirts it out downward through the backface-colliding floor; at tick 300 it is at (2545.4, −114.0, −858.5), still sinking; it eventually falls past −1762 → reset → FAIL.

  Note: even a fired open wouldn't fully save the current spawn — the center-hinge 90° swing (adapter: "hinge side and swing are not per-door proven", act2_progression.gd:10-11) leaves slab 51 at z −849..−859, x 2520..2580, which still contains (2550, −854).

  ### Likely cause

  Not a missing floor — the floors are present and collidable at the expected heights. The walk premise `--open-movables 51 52` is false at runtime: the Golden Doors are closed in the fresh scene (default travel 0, no saved native state, nothing fires their use), and `DOOR_AT` is movable 51's placement origin — the player is spawned inside the closed door's collision box and ejected down through the floor.

  ### Smallest fix

  Two small changes (a route-point-only or height-only fix cannot work — with the doors closed, no spot in region 1931 fits the capsule, and y = −100 is inside the box at any height):

  1. **Open the doors in the test setup** so the scene matches the earned plan: before placing the player, call `scene.progression.use(51)` and `scene.progression.use(52)` (the native kind-4 uses; predicate 206 selects the opening group 3854) and give the movers a few frames to swing.
  2. **Move `DOOR_AT` off the door origin to the band that is clear in both door poses**, e.g. `Vector3(2550, -68, -870)`: on region 1931's floor, clear of the closed boxes' successor slabs (open slabs sit at z −849..−859 and −909..−919), still within `REACH` 20 (distance 16) of the door origin for `at_door()`, and at standing height (floor −100 + capsule half-height 32) instead of embedded in the floor plane.

