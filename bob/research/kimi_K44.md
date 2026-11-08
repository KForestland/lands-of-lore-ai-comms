# K44 — Atlas readability prep (LoL2 r18)

## Current Atlas (file:line)

The Atlas is a single `Control` drawn in `_draw()`, embedded as a page of the Character/Journal sheet:

- `scripts/lol2/museum_atlas.gd:1` — the whole Atlas. Created and wired in `scripts/lol2/museum_interface.gd:102-121` (page "atlas", zoom/pan/My position/Overview/Section buttons). Opened with **M** (`toggle_atlas`, `museum_interface.gd:472-480`; also the Compass button, `museum_interface.gd:359-362`). It does not pause (game keeps running; `atlas_opened_from_game` restores the cursor, `museum_interface.gd:495`).
- **Geometry source** — `museum_atlas.gd:4` `geometry_path` (default `museum_review/museum.json`). Each walkthrough hands its own geometry over: `jungle_walkthrough.gd:206` `interface_hud.geometry_path = geometry_file` (so the Jungle Atlas reads `assets/lol2/generated/jungle_review/jungle.json`); the Cave passes `atlas_offset` instead (`cave_walkthrough.gd:463`).
- **Two draw modes** (`museum_atlas.gd:30-67, 77-110`):
  - **Faces mode** (`data.faces`, kind=="floor"): builds floor polygons in x/z, then a perimeter multiset over all polygon edges; edges used by exactly one polygon become `edges` (`:46-67`) — i.e. only the *outer outline* is drawn, as a dark 5px line + light 1.5px line (`:84-86`). Shared edges (interior walls *and* open passages alike) cancel out and draw nothing.
  - **Sliced/region mode** (`data.regions` or `creature_nav/<area>.json`, `_index_storeys` `:397-446`): one slice per nav region. Storeys from `group_storeys` (`:341-395`: union-find over nav links, ±32 floor tolerance, numbered by median floor); `band()` (`:314-318`) bright/faded/hidden vs viewed storey (`viewed_storey` `:465-470`, PgUp/PgDn `:130-132`); "sections" (piled rooms) via `section_depths` (`:141-226`) for `SECTION_AREAS` (`:19`: L9_DR, L10_DC, L16_CA, L14_HT). Each region polygon is outlined at 1px in the fill/fade color (`:100-104`) — every region border shows uniformly, no wall/opening distinction.
- **Explored filter** — `use_filter()` `:480-487` + `_shown(region, player_region)` `:489-503`: regions hidden unless in the saved `atlas_explored` dict (per area `{full: bool, regions: [ids]}`), or the player stands in them.
- **Explored tracking** — `scripts/lol2/atlas_explored.gd`: attached per map (`attach` `:143-149`); each frame `note()` (`:172-203`) adds the current region (`progression.current_region` or `region_visibility.region_at_nav`) plus every currently visible region from `region_visibility.visible_regions`. Saved as its own top-level save key (`jungle_walkthrough.gd:471-473`, `cave_walkthrough.gd:1216`); old saves migrate to "full" (`migrate` `:102-112`).
- **Player marker** — gold dot + heading line (`museum_atlas.gd:105-110`).
- Tests: `tests/atlas_storey_draw_test.gd`, `tests/atlas_sections_test.gd`, `tests/atlas_explored_test.gd`.

**Not present anywhere in the Atlas:** wall-vs-opening distinction, door gaps, level-exit marks, location labels, plot markers, north arrow, legend.

## Edge data

- **Region graph (the core edge source)** — `assets/lol2/generated/creature_nav/<AREA>.json` (14 areas; L4_HJ = Jungle, 4787 regions). Top keys `version/area/source_sha256/regions`; each region row is `[polygon [[x,z],…], floor_y, ceiling, links]` where `links` = `[[neighbour_region, x, z](shared-edge midpoint), …]` (verified row 0: `[[20,-134,-6],[26,-20,-118],…]`). Loaded by `region_visibility.gd:47-51`. **An edge with a link = walkable/opening; an edge with no link on either side = wall/boundary** — exactly the rule the owner wants.
- **Wall faces to refine "door gap"** — faces exports: `jungle_review/jungle.json` (11216 faces: 4787 floor, 5969 wall, 460 ceiling; face = `{region, kind, material, uv, points}`; also `start`, `arrival_region`, `wall_bindings`, `source_walls` keys), plus `museum_review/museum.json`, `darker_jungle/area.json`, `hive_review/hive.json`, and `maps/<AREA>/area.json` (map packs add `render_sector`, `arrivals`, `start_selector`). `region_visibility.gd:_classify_openings` (`:125-162`) already computes, per inter-region edge, whether the two regions' floor/ceiling spans overlap ≥ `OPENING = 24.0` after subtracting wall spans on that edge — reusable as-is to decide "linked but blocked vs open gap".
- **Doors** — no door table. Doors are scripted owners of faces: `l8_temple_door.gd`/`l14_temple_doors.gd` (Huline Temple), `l10_tomb_state.gd` `doors()`, `l13_egg_door.gd`, `museum_wheel_door.gd`, `museum_dragon_door.gd`, etc.; their positions come from the owned faces/props, not from data. Also `darker_jungle/boundary_edges.json` (original boundary edge index list for L8_SJ).
- **Level exits** — `scripts/lol2/act2_travel.json`: top-level `edges` list, one record per native exit: `{area, owner: "region:N"|"prop:N", destination (area), level, selector, position, static_grade: PROVEN|ADAPTER, blocked_reason}` plus per-area `arrivals` (selector, position, heading, region). **Caveat: no row has `area == "L4_HJ"`** (only three L8_SJ→L4_HJ entries); the Jungle's own exits live in code:
  - Jungle ↔ Hive: `hive_route.gd` + `assets/lol2/generated/hive_routes/routes.json` — route entries with `polygon`, `region`, `floor`, `ceiling`, `destination`, `arrival`; scene change `jungle_walkthrough.tscn` ↔ `hive_review.tscn` (`hive_route.gd:4,58-79`). This is the "Hive entrance" exit marker.
  - Jungle pocket → Dark Halls: `dark_halls_route.gd` (region 3205, `monastery_rooms.gd:72-74`).
  - Act One departure: `act_one_departure.gd` (movie, then scene change, `:104`).
  - Act 2/3 level changes: `act2_progression.gd` (scene map `:20`, `change_scene_to_file` `:303`, `arrival_pose` used with `start_selector`, `act2_map.gd:98-105`).
  - `act2_progression.gd` also exposes `current_region` (consumed by `atlas_explored.gd:187-190`).

## Names

- **Area names** (sheet title bar, hard-coded): `jungle_walkthrough.gd:9` `"Huline Jungle"`; `cave_walkthrough.gd:458` `"Draracle's Caverns"`; `hive_review.gd:119` `"Hive Caves"`; `museum_interface.gd:7` `"Draracle's museum"`.
- **Named places with world positions** — only one exists: `l8_journey.gd:7` `TARGETS := {"entry": Vector3(-3854,32,1190), "temple": Vector3(758,32,2046), "village": Vector3(676,32,-4541)}` (native-translation space; `l8_village_hints.gd:29-35` matches the player against them with `NEAR = 420`). This is the template a name table should follow. The temple target coincides with the PROVEN L8_SJ→L14_HT exit prop position `[758, 0, 2046]` in `act2_travel.json`.
- **Hint-book names** — `~/AI_COMMS/reference_hintbook/hintbook.txt` (plus `brady_guide.txt`): "Huline Jungle" (ch. listing), "The Wild Village", "Huline Tribal Clubhouse", "Your First Visit to the Temple", "Chapter Twelve: Huline Temple", "The Huline Jungle Hub". Good short-label source per the owner's evidence order (game text > hint book > longplay).
- **Game text strings** — `assets/lol2/generated/help_system/texts.json` (help topics, not places); `data/lol2/codex.json` (`Items/Creatures/Characters/Lore` — character/item names, not locations).
- **Place names inside journal hints** (see below): "the temple east of the entry", "the village", "the great tree", "the cemetery gate" (`l8_village_hints.gd:9-12`); "the lift at the bottom of the pit", "the big river by the land bridge" (`act1_journal_hints.gd:7-9`).

## Plot-point sources

- **My Journal** — `scripts/lol2/my_journal.gd`: discovered note ids stored in the carried `item_effects` packet under `"journal"` (discovery order, travels through saves/handoffs, `:48-67`). All hint tables are enumerated in `SOURCES` (`:7-25`): `jungle_village_state`, `monastery_quest_state` (CAN/CHUT), `thieves_den_state`, `weapon_shop_state`, `museum_long_arm_state`, `museum_torches`, `l8_larkhon_state`, `l8_tree`, `l8_village_hints`, `l9/l10/l13/l14/l16_journal_hints`, `l8_tribe_dawn_hints`, `act1_journal_hints`, `act3_journal_hints`. Each row = `{when (stable id), flag, hint, enhanced_guard}`; the "when" condition (`stuck_id`, e.g. `l8_village_hints.gd:20-27` over `l8_journey` flags `gift/temple_visited/admitted/key_awarded`) is precisely "what Luther has learned / step still open" — ready-made show/clear semantics for markers. Docs: `docs/my-journal.md`. **No pins feature exists** (grep finds pins only in playtest provenance text) — the 11-05 "pins in My Journal" is not yet implemented as data.
- **Quest state** — `act_one_quest_state.gd:9` `initial()`: `jungle_dagger_collected`, `weapon_shop`, `act_one_departure` (phase idle/movie/arrival/arrived), `hive_curse`, `hive_elevator`, `hive_wax_collected`, `monastery`, `magic_shop`, `thieves_den`, `weapon_poison`, `jungle_village`, `hive_room_entered`, `hive_chasm`, `hive_nest`, `conversation`, plus `l8_journey` and `l8_temple_door`. Act 2/3: per-area states restored in `act2_map.gd:286-305`. `dev_diagnostics.gd:76` already builds a quest summary from live owners.
- **Quest-step locations** — today only `l8_journey.TARGETS`; everything else ties steps to trigger polygons inside the respective owner scripts (e.g. `hive_elevator.gd` `PIT_LIP` in `act1_journal_hints.gd:22-24`, `jungle_exit_encounter` region-event2 polygons).

## Gaps and smallest plan for one area (Jungle, L4_HJ)

**Gaps**

1. *Edges*: faces mode draws only the outer perimeter; interior walls and openings are indistinguishable (both erased). Sliced mode draws every region border uniformly. Nav links and the opening classification exist but the Atlas never uses them.
2. *Exits*: L4_HJ has no `act2_travel.json` exit rows; its exits are code constants (hive_route routes.json, dark_halls_route, act_one_departure) — nothing exposes them to the Atlas.
3. *Names*: no name+position table for L4 (only L8's three TARGETS). No labels anywhere.
4. *Plot points*: journal notes and quest flags have no map positions; no marker drawing; no pins.
5. *Chrome*: no north arrow, no legend.

**Smallest plan (Jungle end to end)**

1. **Edges** — in `museum_atlas.gd`'s sliced path for L4_HJ: build the shared-edge multiset from `creature_nav/L4_HJ.json`; draw an edge as a wall line when neither side lists a link; skip linked edges; mark as a door gap where a link exists but `region_visibility`-style opening classification against `jungle_review/jungle.json` wall faces says open — reuse `_classify_openings` logic (`region_visibility.gd:125-162`). Respect the existing explored filter and storey fade.
2. **Exits** — read `hive_routes/routes.json` polygons (Jungle side) and draw them as the marked "Hive entrance" gap; same treatment for the dark_halls pocket later. Position only, shown once its region is explored.
3. **Names** — one small staged table (e.g. `atlas_places` for L4_HJ) in the `l8_journey.TARGETS` shape: `{name, position, reveal}` for Huline Village (chief hut), Huline Temple door, Hive entrance, land-bridge river crossing, beehives — names from the hint book, positions from the scripts above; reveal = region explored. Draw at room/area centroid, current storey only.
4. **Plot markers** — map journal note ids + quest flags to those same anchors: `l8_journey` flags → temple/village/entry markers, `act1_journal_hints` river note → river crossing, `act_one_departure` phase → departure point; show only when the note is discovered / flag open, clear when the step completes. No new quest plumbing.
5. **Earned test** — extend the `atlas_explored_test.gd` pattern: load a real Jungle save in `jungle_walkthrough`, open the atlas page, assert wall edges/door gaps/labels/markers render only for explored regions (capture for the owner's review), matching the direction's acceptance line.


Lead spot-check: museum_atlas.gd:4 geometry_path, l8_journey.gd:7 TARGETS, act2_travel.json has 0 L4_HJ exit rows — confirmed.
