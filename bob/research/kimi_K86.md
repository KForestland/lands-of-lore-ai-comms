• Review complete. I read the full diff `6e711d8..f7013ef`, the four research notes, the L10_DC pack data, the nav polygons, and the surrounding collision plumbing (`region_edge_rule.gd`, `jungle_review.gd` build path). Findings:

  ## Stated risk 1 — OF6: walls and maus doors 124/125

  **Wall sealing is correctly wired.** The three extra want-keys `[1444,0] [1447,0] [1452,0]` in `act2_map.gd:363` match real `source_wall` faces (walls 5503/5505/5514 at z −4286, spanning x −654..−375 contiguously — I verified in `area.json`). `_l10_void_walls` runs at `act2_map.gd:155`, before `super._ready()` builds the shell, so `edge_block_keys` is populated in time. `classify()` never puts `source_wall` faces in `rule.pass`, so the walls stay drawn — no invisible-wall problem. The y 10..100 base gap on 5505/5514 is not passable: a radius-15 capsule still intersects the face. Existing count-based tests (`l10_map_test.gd:111`, `l10_catacomb_void_wall_test.gd:35`) use `> 3000` / upper bounds that absorb +3 walls and −12 excluded door faces.

  **No trap, in or out.** Doors open on contact from *either* side (`l10_globe_door.gd:117` `_near` is a pure distance check) and never close, so the room can't seal the player. I verified the swing math against the actual geometry (124: x −352..−344, z −3824..−3774; hinge at (−352, −3824); yaw −π/2): the arc sweeps the hinge's northwest quadrant — west of the closed plane — so the east approach (the only way to first open them) is never swept, and the open leaf (x −402..−352, z −3824..−3816) leaves the z −3795 lane clear by ~6 units past the radius-15 body, matching the walked test. `owns()` correctly ignores the `static_assembly` faces that coincidentally share `source_index` 124/125. On save/reload the doors rebuild shut, but contact reopens them, and a player triggering from the west stands inside the arc — however `sync_to_physics = false` means the leaf can't push or carry him; worst case is a momentary overlap and depenetration pushout from an 8-thick leaf. Checked, dropped as a trap; at most cosmetic.

  **One real defect (Low):** `l10_globe_door.gd:126-128` — `_near` ignores Y. Nav region 1773 (floor −150) underlies the whole door corridor (verified: it covers (−372,−3795), (−330,−3795), (−348,−3760), (−400,−3795)). A player walking that catacomb passes within 20 horizontally of the doors, so both leaves swing open 150 units beneath him with no contact. Concrete scenario: explore the catacomb first, then arrive at the surface corridor and find the maus doors already open. No quest state gates them, so impact is limited to a pre-opened door and an untriggered animation; severity Low.

  ## Stated risk 2 — OF1: double-door facing

  **No collateral facing/texture damage.** The Draracle change is a pure U-mirror swap on faces 2 and 3 of leaf 74 only (closed and open poses), verified by diffing old vs new JSON: vertices, hulls, leaf 77, and all metadata untouched; the only consumers are `cave_draracle_door.gd` (mesh building) and `walkthrough_save.gd:131` (`validate` reads only `full_travel`/`uses`, unaffected). The jungle change at `jungle_village_gate.gd:65` fires only for `leaf.index == 78` + `material_0742.png`; leaf 78 has exactly two such faces (the two broad faces) in all 101 frames, so the flip is exactly the intended face swap with no edge/top faces hit; leaf 79 untouched. The subclass `jungle_followup_gate.gd` inherits `prepare_pose` but its `gates.json` contains only leaf 70 — condition never fires. No other level loads either data file. The general "bake mirrors face 3 regardless of the flag" issue in other movables is a pre-existing, unaddressed matter — not a regression from this diff.

  ## OF4 / OF5

  No behavior change — test-only commits with registry rows (`suite: core`, orders 667/668). The tests' assertions match the notes' claims; nothing to flag.

  The three new `docs/deviations/05xx-row-*.md` lines are consistent with the code; the rendered DEVIATIONS.md is not in the diff and not treated as a defect.

  APPROVE
