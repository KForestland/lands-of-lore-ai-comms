R106 review: sol/generic-l10-pilot-20261112 78d5eaf (base 415ca7b). Read-only; nothing run.

FINDINGS (by severity)

1. MAJOR - E is swallowed near every unopened socket. scripts/lol2/l10_tombs.gd:72-76 now admits any receptacle within 256 units with no facing or wall test, and try_use (:95-108) always consumes E. Input runs last-child-first, so L10Tombs gets E before world items, chargers, main gate and the binder (act2_map.gd:192-203). Globe 55 (1272,15,-1853) lies 232 from socket 158 (1041,40,-1857): from the socket side "E - Take" does nothing, or silently spends a carried charged yellow globe through the wall (not retrievable). Same for globes 52, 56, 45 and scroll item7. Left click still takes. Ledger 0627 names the 256/no-facing rule, not this side effect.

2. MAJOR - Broken fronts stay solid, contents stay sealed. generic_object_world.gd:66-68: only the selector frame changes; the box stays on layer 1 forever, and the final group (life <= 20) sets no selector, so the front ends on frame 3. Items sit behind the panels (Amber 2-6 behind 248, Dragon Blood behind 265, SS9 behind 242, HlScrl behind 253/254); the pickup ray (act2_world_items.gd:71) uses mask 1, so they likely stay untakeable. Disclosed in 0627; fronts 253/247/265 gain damage frames only.

3. MAJOR - A use click still swings. museum_interface.gd:252-256 calls show_swing() in _input on every captured left click, before generic_object_world.gd:185-195 marks it handled. The weapon animation plays while the chest opens (no damage).

4. MAJOR (later builder) - Save validation is census-exact. generic_object_world.gd:24-43 rejects the whole load unless counts equal 56/29, every id exists, area is L10_DC and version is 1; validate_all_quests (area_owner_registry.gd:141-149) applies it in every area. Changing one census row or enabling a second area makes every save that visited L10 unloadable. An unknown id refuses the load.

5. MAJOR - Not one data-driven layer for the acceptance list. Movables and covers are data-driven; sockets, tomb doors, Emperor boxes, door 143, remains and priest stay per-object owners, wired by name in generic_object_world.gd:153-175. Hard-coded: catalog.gd:7,14,20 ("L10_DC"); world.gd:19,27,51 (L10 paths), :42 (template 1 = 3 selectors), :147 (noun; lid 52 and all sliders read "crypt top"); l10_tombs.gd:5 (13 glow ids), :68, :94 (99/100/101 maps); act2_chargers.gd:7 (props 247/242/1094).

6. MINOR - Left click within the 0.8 cone and 140 of a charger or priest is use, not attack (world.gd:159-162,173): a swing at a monster there inserts a globe or talks.

7. MINOR - Overkill skips the break: only the first crossed threshold row runs (native_script_host.gd:876-884). At 28 damage (8 plus the +20 weapon bonus) 44 to 16 fires row 40, then 16 to 0 fires nothing; strike refuses at life 0 (world.gd:124).

8. MINOR - Missing generated data: setup errors are assert-only (world.gd:49,54), stripped in release; owns() (:18-20) still removes the map's static frames, leaving invisible solid covers. Without native_scripts the owner is skipped silently and the old contact door adapter is gone too; l10_globe_door.gd is dead code.

9. MINOR - Tests. All but the headless rules test use real key/mouse events; assertions can fail; none skips silently. Starts are teleports with clocks held (input, persistence, cover, prop, globe-room-wall) or pinned saves; five saves live in gitignored tmp/. "Legacy packet" in persistence_test is a current-format packet. globe_room_wall moved its lane from z -3795 to -3824 to fit the new doors. No test: 85, 109, 117, 52, fronts 253/247/265 (only 241), socket 158/door 159, globes 50/55, boxes 125/126/127, door 143. Covered: 86, 107, globe 48, 154/155, remains.

SOUND
- C is not a use key (only player_crouch.gd:13); E and left click only.
- Movables and covers: one camera ray, mask 1|2, reach 256 (covers 140); nearest body on the crosshair, not through walls.
- State sits in quests.generic_objects.areas.L10_DC (movables: position/phase/travel/fraction; breakables: life/selector), written through snapshot_host, so both F5 and slots. A missing key loads at source state. Mid-motion phases 2/3 save and resume.
- Dead, paused, inventory, cursor and actor-lock block use (world.gd:137-138). Form is not checked.
- Other levels: catalog empty off L10; kind-9 mode 3 stays unhosted without dword_22.

NOT CHECKABLE WITHOUT RUNNING
- Whether all 56 movables get a hinge body; whether lids, sliders (31 units in 2 ticks) or 90-degree doors embed or push the player (no occupancy test); the globe 48 ray; findings 2 and 3 on screen.

VERDICT: PROOF SOUND AFTER FIXES
