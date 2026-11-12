R109: sol/generic-l10-ready-20261112 2600e70 (base 415ca7b) against integration r19-work 8a53cce. Read-only; nothing run.

FINDINGS

1. MAJOR (merge) - Two boundary mechanisms. This branch: act2_map.gd:230 (all L10 source walls out of the terrain), :234-257 (_l10_boundary_body), :287-293 (packet scripts/lol2/l10_height_boundary_faces.json merged into edge_block_keys). Integration: _height_boundary_walls/_height_boundary_body, packets in scripts/lol2/height_boundary/, keys kept apart. Both add a node named HeightBoundaryCollision. Text conflict after super._ready() (:159). L10 is not in the integration's HEIGHT_BOUNDARY_AREAS, so nothing doubles today. This loader has no map-hash or matched-key check (the integration's has): a missing or stale packet silently leaves the 362 walls open. The L10 pack hash matches in both worktrees now.

2. MAJOR - "Terrain byte-identical" holds only adapter off/on (tests/l10_map_test.gd:117-155), not against 415ca7b/r19e. At base the 3,168 older void walls were in the terrain trimesh (jungle_review.gd:302-305); :230 moves them out, about 6,336 triangles fewer. The integration's own note says one wall changed a stair contact 5,000 units away. Only Sol's own sittings cover this.

3. MAJOR (merge) - Two mover-collision changes meet. Integration _build_hinges builds convex TopSlab plus Sides; this branch adds pause admission (act2_progression.gd:1141-1161, generic_mover_contact.gd) and snaps generic movers (:1164). All lid evidence (crypt 67, lid 52, lid 117) was taken on hollow trimesh lids; a solid slab changes what intersect_shape reports. Text conflict near :1135. Rerun the contact, table and lid tests after merging.

4. MAJOR (merge) - About 20 registered rendered tests need 24 gitignored tmp/ files (saves, tmp/l10_owner_tour_graph.json): owner_positions, table_input, lid117, switch_reach, every continuation sitting. Without Sol's donor they fail, not skip.

5. MINOR - Ledger numbers 0626/0627/0628 exist on both branches with different rows; docs/DEVIATIONS.md and tests/area_owner_catalog_test.gd also conflict.

6. MINOR - Save bounds still follow the table: generic_object_world.gd:68,72 and generic_object_rules.gd:60,64 (exact field count, life <= start_life, position <= span). Lowering a start_life or span makes every save that visited L10 unloadable in all areas.

7. MINOR - Chargers, Emperor boxes and priest keep the 0.8 cone on E (act2_chargers.gd:47-54, l10_emperor.gd:57, l10_priest.gd:33); only left click got 0.97. Line of sight is kept.

8. MINOR - The pause prompt (generic_object_world.gd:195) shows only with the crosshair on the lid; otherwise it stops silently. museum_interface.gd:258 hides the swing when would_use() is true even if the use is refused.

9. MINOR - Cover 5 (template 66) has no damage frame: at zero life it looks intact but is not solid (:99). l10_tombs.gd:14,29: owns() is unconditional, the render error assert-only.

10. MINOR - The "0 blocked" replay uses traces walked with the walls already solid, so it cannot fail; the independent evidence is the 36 owner positions (35 reached).

R106 POINTS
1. IN - tomb sockets: crosshair ray, 256, receptacle collider only (l10_tombs.gd:72-76). See finding 7.
2. IN - zero life forces frame 3 and layer 0 (:94-101); table test takes contents.
3. IN - would_use gate; cover_input_test checks no swing.
4. PARTLY - unknown ids/areas warned and ignored, counts gone, missing key loads; finding 6.
5. IN - crossed_thresholds fires each band in order; life reaches 0.
6. IN - active() and tombs require form 0; chargers unchanged.
7. IN - preparation_error; owns() false, static frames stay.
8. IN - chest lid, door, pit lid, lid, sliding panel, crypt top.
9. IN - table rows plus lid-52 contact case; supplied poses, disclosed.

SOUND
- Counts: 362 new + 3,168 old = 3,530 faces; all 362 keys match the pack; no blocked wall lies on a breakable front.
- Boundary body: own StaticBody3D, layer 1/mask 1, two-sided. Player, creatures, weapon, use and pickup rays all hit it. Static: 65 live-floor regions withheld by the producer, never updated at runtime. Off L10: no-op.
- Lid pause: checks the player only; creatures and items cannot hold a lid. E always toggles, so no hard deadlock. Phase/position/fraction saved; blocked flag recomputed.
- Other levels: catalog empty off L10; kind-9 mode 3 still unhosted without dword_22; no native opcode-1 targets a generic movable.
- Saves: F5 and slot via quests.generic_objects; old saves load at source state.
- C appears only in hint text. Ledger rows present: use binding and socket rule (0627), pause prompt (0630), boundary and switch-61 aim (0631).
- Tests: real key/mouse events; assertions can fail; none removed. globe_room_wall rewritten for E (maus doors 124/125 no longer open on contact). The full sitting starts from the F2 developer start and walks fixture waypoints, no pose writes. Owner positions start from installed earlier F5s. Table, input and persistence tests place the player by coordinates, and say so.

NOT JUDGEABLE WITHOUT RUNNING
- Aim points near new walls: Emperor boxes 125/126/127 (bands -80..-30, 24-26 units away, walls 625-646); shelf items Amber 2-6, 10, 13, Dragon Blood 25-27, fire crystals 19-20, scrolls 7 and 21, sap 16, dagger 41 (walls 6705/6707, 7093-7115, 6696); switch 61 (5 units before wall 6301).
- Creatures at the new lower bands; lids against the integration's slabs; stair contacts after finding 2.

VERDICT: MERGE AFTER FIXES
