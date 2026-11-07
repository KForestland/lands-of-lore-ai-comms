# Fable lane: Huline Temple interior as visibility islands (TEMPLE-ISLANDS), 2026-11-07

Worktree ~/opus_work/lol2_temple, branch temple-islands from act3-chain c9295da. Nothing in lol2_act3 or lol2_r17 touched.
Task: AI_COMMS/fable_lane/FABLE_TASK_20261107.md. Method: AI_COMMS/META_DUCK_METHOD_20261107.md.

## Meta duck (written before the fix)

1. **Problem.** L14 Huline Temple interior still clips after portal visibility: owner F10 r16 21-05-00 at Godot (2430, -3458) h32
   "geometry very wrong, still clipping"; r14 (11-03) 18-01-10 garden (2625,-2699), 18-01-36/44 hall (2876,-3362) "texture/geometry
   wrong", 18-10-50 (-310,-2304) h222 "the doors are portals like in game, their textures clip the main map". Portal visibility
   (region_visibility.gd, 2026-11-05) and the Y05 black hall quad helped; owner parked it 11-06 for Sol/Fable.
2. **Main chain?** Yes (Act 2 path to the Chamber of Voices), but movement, doors, trials and gates already work (l14-three-doors.md:
   STORY-061 complete with earned walks). Only presentation is wrong; it blocks "maps 100%" (owner order: maps first).
3. **Intent.** *Atmosphere* + *orient* + *gate*: a sacred building of separate chambers. The player must read each room as one
   place: the entry hall (Brady 197 pt 1-2), the hangings/ritual room, the chapel, the lower halls (Brady 199) with the three-door
   room (pts 17-19) whose doors open on three trial chambers (ledge maze, tilt room, fire paths), then the oil pool/blades/boulder
   corridor to the niches and the elevator. Longplay: g_264-g_269 entry rooms (243-245 min), g_275 three-door room (door with the
   blue glyph banner, rock walls, starry night sky above), g_276-g_278 ledge maze (ledges floating in black), g_280-g_281 tilt room
   (black ceiling), g_285-g_286 pedestal court (night sky).
4. **Player contract.** Walk through a door -> you are in that chamber and see only it: its own walls, its floor, black or the
   night sky above where it has no roof. No other chamber shows through a wall, above a wall, or under the floor. Walking back
   returns you to the room you came from. Nothing else (no trigger, no timer); the trials' own gates are already hosted.
5. **EXACT vs APPROXIMATE.** EXACT (untouched here): which door leads where (l14_trials.gd: door 90 -> ledge maze, 89 -> tilt,
   88 -> fire paths; corridor 80/75/57/23 -> oil pool), puzzles, idols, gates, saves. APPROXIMATE (this lane): how the hidden
   chambers are kept out of view, and the background colour where the original clears to black.
6. **Options.**
   a. Decode the native renderer's portal rule: weeks, not needed (the data already names the rooms).
   b. Tune portal edges face by face (what r14-r16 did): endless, each fix moves the leak.
   c. Black quads over leaks (Y05): hides one hole at a time.
   d. **Visibility islands from the data (chosen).** Every face of the L14 pack carries the native `render_sector` (255 rooms;
      4,275 nav regions, none spans two rooms). The room is the island: static faces and props are batched per room instead
      of per 24-region cluster (clusters mixed rooms and stacked storeys, so one reached region drew pieces of other rooms),
      and the view walk may leave a room only through an opening: a shared region edge whose floor/ceiling spans overlap by
      24+ units after the wall faces on that edge are subtracted. Stacked rooms (floor-0 halls over the -80/-100 rooms, 674
      room pairs overlap in plan) share no opening, so they stay hidden. Cost: ~150 lines, data-driven, L14 only (switch).
      Risk: a room reached through a real opening is drawn whole (that is how rooms work; walls occlude the rest).
7. **Proof.** Captures at the four owner poses + two longplay stand-ins (g_275 three-door room, g_276 ledge maze) before/after,
   headless test printing PASS with a registry json (islands well-formed, owner poses never draw a stacked room), affected
   tests, then the owner walks it.

Meta checks: solving the player's problem (rooms), not the data's; same class as the Jungle/Hive portal fix, finished with the
data the producer already emits; evidence order kept (pack data > longplay > Brady > owner words); the owner would notice
(stacked rooms show through), so it is worth doing now.

## Findings worth keeping (data facts, L14_HT.json sha256 c294f9ab...)
- 255 render sectors (-1 = movables), 16,185 faces, 4,275 regions; 344 regions have no ceiling face (sky in the original too:
  g_275 shows the starry sky over the three-door room; the pack's map_sky/L14_HT panorama is that night sky).
- Ledge maze (sectors 17/111): void floor at -200 is material 595 = pure black; ceilings 1600-2110 are stone 473 (the original
  shows black above: distance shading, not geometry -> lighting phase, L14 has no sector_shades table yet).
- Trial chambers are connected by real corridors in the data (77 -> 82/81/80 ...); no teleport is needed for the doors.
- Owner's "doors are portals": the original's doors stand in walls of a room that is drawn alone; ours showed far corridors
  and other rooms through the gaps -> islands.
