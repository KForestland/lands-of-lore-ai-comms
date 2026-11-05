# R2 adapter review, rows 0285–0300, 2026-11-05

No Godot was run. No opcode callee was entered. LOLG.DAT was not opened. The longplay was not opened. r15 is `f6a5aa4`. r12y is `56812f9` and has 228 deviation files. `cmp` finds none of these sixteen files there. Each one is r15 only. `adapter_review_20261103.md` already graded 0297–0300 and the 0280–0296 slice. Those grades stay. This pass reads the named hosts and both printed books. `adapter_review_20261105.md` is the Hive lift. That lift is not one of these rows.

Brady printed pages come only from the `PDF PAGE N = PRINTED PAGE M` lines. The rows' Prima 133–139 numbers are not Brady printed pages 133–139. Those Brady pages are later rooms, not this temple. The temple sentences below are Brady printed pages 115–119. Printed page 27 and printed page 104 are cited only for the Dracoid names. A later checklist repeats Brady. It is not merged into the hintbook.

`act2_map.gd` lines 157–173 attach the L14 hosts. `dragon_level.gd` lines 110–143 attach the L9 hosts.

## 0285 left hanging

Human E inside 145 and facing hides static assembly 124.

HINTBOOK lines 4384–4385 say click the left wall hanging. `l14_hanging.gd` lines 3 and 27–36 require Human, distance under 145, a forward dot above 0.9, and a finished ritual, then hide the assembly and clear its collider. The reach point is y 45. The row's source y is 0. The book prints no 145 and no E key. The caller stays unentered.

BRADY lines 4921–4923, printed page 115, say the concealed door is behind the tapestry, left of the first bowl altar. That sentence does not name a wall hanging. It is not the same click. The 145-and-facing join stays the adapter. `source_ids_054_060.md` still grades the hanging UNKNOWN. That grade stays.

The row's pending spider sentence does not stay. Row 0286 is that encounter.

## 0286 spiders

After the hanging opens, approach within 150 hides static 64 and wakes HIVEW actor 68. A real death respawns that same actor after 12 active seconds inside 700.

HINTBOOK lines 4396–4415 say the spiders spawn and some must be fought. Lines 4414–4415 say a wall crumbled. `l14_spider_passage.gd` lines 5 and 32–53 do the 150 approach, the one actor, and the 12-second clock. The approach point is y 40. The row's source y is 0. The book prints no 12 and no 150. Opcode 13 stays unentered.

BRADY lines 4938–4941, printed page 115, and lines 4943–4947, printed page 116, say Hive Warriors are everywhere downstairs, sometimes ignore you, and are not part of the puzzles. That is not the hintbook spawn sentence. The HIVEW label is the row's actor, not a Brady interval. The 12-second one-at-a-time clock stays the adapter.

## 0287 lower passage

The flute stays in region 219. G near the lowered ritual floor requests Lizard or Human.

HINTBOOK lines 4418–4419 say the flute is in a coffin. `l14_lower_passage.gd` lines 3 and 10–14 offer G within 400 of (2300, −30, −3350) after the ritual, and also at the later library, hall, bedroom, and machine points. `act2_world_items.gd` line 52 refuses a take while paused. The book prints no 400 and no G. The source-id pack still grades a coffin UNKNOWN. This row adds no coffin cstring.

BRADY lines 4973–4977, printed page 116, say an iron flute is inside an open coffin on the lower level. "Open" and "iron" are Brady's words. They still print no region 219. The G choice stays the adapter.

## 0288 machines

E on the pedestal moves the body in 2 seconds. G turns the trough. Long-edge-first starts a 15-second press. The statue then settles over 2 seconds.

HINTBOOK lines 4455–4472 say press the pedestal button, take the red-goo box, fit the long edge first, and catch the statue. `l14_machines.gd` lines 59–73 refuse a short edge, and lines 96–114 run the 2-second grind, the 15-second press, and the 2-second settle. The book prints no 2 and no 15. The native callee stays unentered. The source-id pack still grades the button, the goo box, and the caught statue UNKNOWN.

BRADY lines 4930–4936, printed page 115, say click the button near the body, drag the trough, and take the statuette when it appears. Brady does not print the long edge or the catch before it falls. Those hintbook sentences stay. The timers stay the adapter.

## 0289 bedroom

Human E slides movables 0 and 1 by 82 over 2 seconds. Ceiling 2358 blocks from below only.

HINTBOOK lines 4516–4518 say push the headboard, use the Lizard at the crack behind the red altar, and return to Human. `l14_bedroom.gd` lines 32–43 and 64 do the 145-facing E, the 82-unit slide, and the one-sided ceiling. The form point is `l14_lower_passage.gd` line 11, within 400 of (2200, 100, −5270). The book prints no 82 and no floor word. Opcode 1 stays unentered. The source-id pack still grades the headboard, the crack, and the red altar UNKNOWN.

BRADY lines 4958–4965, printed page 116, say click a bedpost, spark the candle and lamps, and click the feather quill. That is not the headboard sentence. The headboard slide stays the adapter.

## 0290 hall buttons

E on 146 lowers nine floors over 2 seconds. E on 147 waits for that motion, then lowers floor 1518 and two walls by 120 over 2 seconds.

HINTBOOK lines 4519–4521 say press the two hall buttons in order or nothing happens. `l14_library.gd` lines 4–5, 63–77, and 84–95 do that order and the 2-second clocks. The extra G point at (1820, 100, −5088) is `l14_lower_passage.gd` line 11. The book prints no floor word. Opcode 196 stays unentered.

BRADY lines 5008–5011, printed page 117, say click the wooden door to the right of the altar. That door is not the two-button order. The ordered 2-second motion stays the adapter.

## 0291 library exit

E on 148, after the library opens, lowers floor 1614 by 40, raises its ceiling 20, and raises ceiling 4197 by 100, over 2 seconds.

HINTBOOK lines 4522–4523 say press the wall button to leave the library, then turn right to the south. `l14_library.gd` lines 78–90 do the three shifts over `exit_time` capped at 2. The book prints no 40, 20, or 100. Opcode 196 stays unentered.

BRADY lines 5013–5014, printed page 117, say the button is on the south wall and opens the Statuette Room. That is not the hintbook leave-then-turn-south sentence. The height shifts stay the adapter.

## 0292 niche approach

The route walks around hanging 122. After the library exit, G is offered within 300 of (2800, 0, −3800).

HINTBOOK lines 4523–4525 say turn south, enter the northeast doorway, and notice the statues in niches. `l14_lower_passage.gd` line 11 is the 300-unit offer. `l14_niche.gd` does not move the player. The book prints no 300. The form choice stays the adapter.

BRADY lines 5016–5018, printed page 117, say the Statuette Room is the dark room between the first bowl altar and the chapel. That place is not the hintbook curved-wall route. Neither sentence replaces the 300-unit workaround.

## 0293 statue niche

Kit accepts item 65 once into control 126. Grates 73 and 74 slide 40. Movable 75 rises 18. Floors 381, 379, and 323 rise 70. Shard 67 rides with them over 2 seconds.

HINTBOOK lines 4525–4527 say place the statue in the empty niche and take the green shard on the pedestal. `l14_niche.gd` lines 49–71 do the one receipt and those offsets. `act2_world_items.gd` lines 44 and 50 keep shard 67 hidden until `raised` is 2. The book prints no 40, 18, 70, or 2. Opcode 1 stays unentered. Control 126's statuette identity stays the source-id DECODED. The empty niche and which shard is second stay that pack's UNKNOWN.

BRADY lines 5020–5023, printed page 117, say place the statuette on the empty shelf and an altar appears with a crystal shard. "Shelf", "altar", and "crystal" are not the hintbook "niche", "pedestal", and "green shard". The motion stays the adapter.

## 0294 shard bowls

Props 405 and 406 each take one distinct shard. Both commits lower the rear floors 170, the front walls 100, and wall 1302 by 70, over 2 seconds.

HINTBOOK lines 4528–4531 say one shard in each floating bowl, then the passage behind them. `l14_shard_bowls.gd` lines 5 and 59–78 do the two slots and those drops. The book prints no 30 and no 2. The row's refusal to read word 130 as floor 30 stays. Opcode 196 stays unentered. Scale Tray is not renamed Bowl. The source-id pack still says Bowl, Bowl 1, and Bowl 2 have zero placements, and the floating bowl stays UNKNOWN.

BRADY lines 5025–5029, printed page 117, say place a crystal shard in each bowl of the balance, and a secret door opens. "Balance" and "secret door" are not the hintbook floating bowls and rear passage. The geometry drops stay the adapter.

## 0295 region walls

The global L9 pack is on. Tower fields use that body. Region 3565 follows the statue offering on the same body.

`dragon_level.gd` lines 36 and 110–111 set `region_blockers_enabled` and attach `L9_DR`. `assets/lol2/generated/region_blockers/L9_DR.json` has 125 blocked regions, 116 edges, and 79 dynamic regions. `l9_tower.gd` lines 43–65 disable the local TowerFields body when `RegionBlockers` exists and write the source regions onto the shared body. `l9_tower_source.json` lists 49 unique regions. `l9_statue_walk.gd` lines 24–27 call `set_region_blocked(3565, not enabled())`. `region_blockers.gd` lines 159–164 rebuild only a dynamic region. Region 3565 is in that pack.

HINTBOOK lines 3578–3605, chapter 10, print lizard floor cracks and floating doors. They print no edge count. BRADY lines 1013–1020, printed page 27, name "The Dracoid Ruins" and, as a separate sentence, "The Dracoid Cemetery". BRADY lines 4376 and 4383, printed page 104, say some Catacombs walls can be passed and spell one "Cemetary". Hintbook lines 189 and 205 title "Dracoid Cemetery" and "The Dracoid Ruins". Those four names stay separate. None of them is this join. The shared body stays. No book number replaces it.

## 0296 spiral

Kit inserts the earned Dreamstone into movable 72. Thirty-nine floors move from 0 toward the source words over 4 seconds.

HINTBOOK lines 4536–4539 say the spiral staircase and the bridge come before the three doors. `l14_spiral.gd` lines 3–7 and 74–78 place the reach point at (606, 40, −3464) and scale the words by `raised/4`, capped at 4. The row's source height is 30. The host y 40 is the reach point, not a new source height. The book prints no floor word. Opcode 196 stays unentered.

The sentence that the three door puzzles remain pending does not stay. Rows 0297, 0298, and 0299 are the live doors.

BRADY lines 5031–5035, printed page 117, say click the Dreamstone on the receptacle to raise a spiral stone stairway, then face three pathways. That agrees on the stone and the stair. It prints no 4 seconds. The 4-second reading of the 39 words stays the adapter.

## 0297 left trial

Human E raises door 90 by 80. Doors 89 and 88 stay closed until their later receipts.

HINTBOOK lines 4548–4550 say careful footwork, a walk or run and jump, then the statue. `l14_trials.gd` lines 5, 46–54, and 67–68 raise only an opened door by 80, and the sequence admits 90 first. The book prints no 80, no E, and no door index. Opcode 3 stays unentered. The raise stays the adapter.

The pending middle and right doors do not stay. Rows 0298 and 0299 open them.

BRADY lines 5037–5047, printed page 117, call this the Path of Life, add a lizard for longer jumps, and name Chain Sparks. The hintbook does not print the lizard or the sparks on this maze. Those Brady sentences stay separate. Neither replaces the 80-unit raise.

## 0298 middle tilt

The occupied half rises 150 in 4 seconds, holds 20, and swaps over 8. Four high buttons level the floor and lower barrier 2291 over 2 seconds. Unsolved skirts reach 40.

HINTBOOK lines 4554–4561 say the center tilts and two high buttons on each side open the far door. `l14_tilt.gd` lines 70–88, 108, and 125–134 match 4, 20, 8, the 2-second settle, and the outer walls from 190 to 40. The book prints none of those numbers. Opcode 196 and kind 15 stay unentered.

The solved 40-unit skirt does not stay. Row 0300 and `l14_tilt.gd` line 100 shrink a settled half to a 1-unit plate. The unsolved skirt stays. The lowered barrier faces do not stay as collision. Row 0300 and `l14_tilt.gd` lines 109–111 retire them when settled.

BRADY lines 5079–5092, printed page 118, say kill Lamplights to slow the floor, then press two switches, tilt again, and press two more. The hintbook does not print the Lamplights or the second tilt. The timed cycle stays the adapter.

## 0299 fire paths

Three distinct presses lower bridge parts 56 and 57 by 132 over 4 seconds. Button 61 raises six near floors over 2 seconds. Arrival on far landing 3981 raises gate 55 by 120 over 2 seconds.

HINTBOOK lines 4566–4572 say three fire paths, lingering is the damage, and three buttons lower a bridge on the far right. `l14_fire_paths.gd` lines 60–77 do the 132, the 4-second lower, the step words, and the 120-over-2 gate. The book prints no 132, no 4, and no hit-point number. The callers stay unentered. The amounts stay the adapter.

BRADY lines 5053–5069, printed page 118, call this the Path of Death, name floating heads and a level-1 Mist of Doom, and then say three buttons lower a bridge. The heads and the spell are not in the hintbook paragraph. The bridge sentence agrees. Neither book prints 132. The drop stays the adapter.

## 0300 flute and oil

Either the temple flute, definition 96, or the Hive flute `monastery:item94:Iron_Flute` slides covers 77 and 78 by 195 and down 5 over 2 seconds.

HINTBOOK lines 4578–4584 say insert the flute in the angled slot and cover the oil. `l14_flute_slot.gd` lines 23 and 68–73 accept either flute and apply `Vector3(-195, -5, 0)` over `covered` capped at 2. The book prints no 195, no 5, and no 2. Accepting either flute stays the owner's 01:05 permission in the row, not a book count. The hintbook's Hive Caves reminder does not by itself name the temple placement.

BRADY lines 5110–5118, printed page 119, say an Iron Flute in the recess covers half the oil pool. "Half" and "Iron Flute" are Brady's words. They print no 195. The slide stays the adapter. The solved tilt skirts and the retired barrier faces are this row's own sentences on `l14_tilt.gd`. They do not replace this slide.

## Grade

HINTBOOK for lines 4384–4385, 4396–4415, 4418–4419, 4455–4472, 4516–4531, 4536–4539, 4548–4550, 4554–4561, 4566–4572, and 4578–4584. BRADY for printed pages 27, 104, 115, 116, 117, 118, and 119, kept as separate sentences. DECODED for the host stores, the L9 pack counts 125, 116, and 79, the 49 tower regions, and region 3565 on the shared body. LONGPLAY was not opened. The 2026-11-03 grades are not reversed.

No printed number replaces 145, 12, 400, 2, 15, 82, 300, 40, 18, 70, 170, 4, 80, 20, 8, 132, 120, 195, or 5. No simpler native build replaces these adapters. The hanging's pending spiders do not stay. The pending doors in 0296 and 0297 do not stay. The solved 40-unit skirt and the settled barrier faces in 0298 do not stay.

## Still open

The hanging caller, opcode 13, the coffin cstring, the machine callee, opcode 1, opcode 196, the niche occupancy, word 130, the native tower field reader, the spiral height mode, opcode 3, kind 15, and the fire-path and flute modes stay unentered.
