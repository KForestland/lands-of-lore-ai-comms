# Lands of Lore 2 Classic: the lead's plan from here to finished (Fable, 2026-11-12)

The owner made Fable lead on 12 November: plan the game A to Z, then delegate, monitor and review; build nothing. Working lanes: Opus 5.5, Sol, Grok.

This plan sits on top of two documents and does not repeat them:
- `fable_lane/MASTER_PLAN_COMPLETE_GAME.md` + `master_tasks.json` (137 tasks, eight phases, 10 November): still the full task list.
- `fable_lane/review_20261112/REVIEW_FINAL.md` (tonight): what blocks us and how we work.

## 1. The route, A to Z

Nine milestones. Each ends with something the owner does himself. The first four are the road to "the owner plays from New Game to the ending"; nothing from the later ones is started before that, except research that costs no build time.

| # | Milestone | Done when | Estimate (a guess, see section 6) |
|---|---|---|---|
| M1 | **The Cemetery passes** | Robot walks L10 from its F2 start to the ankh with no aids and no stops; the owner's 30-minute walk passes | 1.5 to 2.5 weeks |
| M2 | **Act 2 passes** (Savage Jungle, Cemetery, Ruins, Claw Mountains) | Same two bars for L8, L9, L12; saves keep opened lids, broken fronts, moved floors | + 2 to 3 weeks |
| M3 | **Act 3 passes** (Ruloi Citadel, Huline Temple, City of the Ancients, Hidden Caverns, Belial's levels) | Same two bars for L13, L14, L16, L17, L19, L20; the Temple no longer clips where the owner walks | + 3 to 5 weeks |
| M4 | **Start to end** | One build, New Game to the ending card, robot first, then the owner plays it through | + 1 to 2 weeks. Most likely **late January 2027**; earliest early January |
| M5 | Items and side content | Every item works or is shown absent; the optional areas and puzzles from the guides are in; the owner signs off each level | master plan phases 2 and 3 |
| M6 | Role-playing systems | Real combat, spells, creatures, bosses, forms; the owner plays each act without cheats | phase 4 |
| M7 | Story | Every line, both moral paths, both endings, every movie | phase 5 |
| M8 | Shell and sound | Title, menus, options, save slots UI, music, ambience | phase 6 |
| M9 | Release | A stranger installs it from their own copy and finishes it; version 1.0 | phase 7. Most likely **July to August 2027** |

Why M4 moved: on 10 November I put "a player finishes the main quest" at mid-December and wrote "if not, add a month". Tonight's review found two pieces of foundation the plan did not have (the object layer, the world state in saves) and a harder collision problem than expected. That is the month. The end date moves less, because the same foundation was hidden cost inside the later phases.

## 2. What changed in the task list

**Done and merged into the integration branch since 10 November** (per the board; I have not re-run anything): one combat module and one health owner (F-14, F-15), the area host (F-16), the whole-game save with native script state (F-06, F-07), autosave (F-18), the L19 passages (C-10), the Act 2/3 playtest starts (C-15). Ready and waiting for review: headless input rule, preload cycles, per-level smoke (F-04, F-05, F-17). Planned and ready to build: item grants (F-08).

**New tasks from the review** (to be added to `master_tasks.json`; ids G-xx):

| Id | Task | Lane | For |
|---|---|---|---|
| G-01 | Object table for all 15 levels (645 rows) | Grok | done; next: mark the rows a player must touch on the chain |
| G-02 | Object layer, Cemetery pilot to the ankh (open, slide, break, sockets; E and left click; minimum save) | Sol | M1, running |
| G-03 | Object layer on the remaining levels, from the table | Sol | M2, M3 |
| G-04 | World state in saves (lids, break stages, moved floors, struck objects) in F9 and the slots | Sol | M2 |
| G-05 | Which room the player is in on stacked floors, then "collide only with connected rooms" on L10, L14, L9, L8 | Grok (rule, 3-hour box), then Opus (build) | M1 to M3 |
| G-06 | Robot player: nightly real-input walk of one level from its F2 start along the try-list; stop list + 10 frames. Cemetery first | Grok | M1 onward |
| G-07 | Status page: one row per level, ends in "ready for you? yes/no" | Opus | owner's time |
| G-08 | F10 writes a full bundle (real save, inputs, frames, hashes, first point of failure) | Opus | owner's time |
| G-09 | One staging script and preflight for worktrees and test inputs | Opus | lanes' time |
| G-10 | Picture helper: hand-tagged viewpoints compared with longplay frames | later, after G-06 | optional |

**Parked until M4 is reached** (owner confirmed Classic first and 3D later; he has seen the rest of this list and not objected): real combat numbers, spells beyond the chain, side areas, the Enhanced edition, 3D art, music, the installer, item behaviour beyond chain items, the good and evil branches.

## 3. Who does what now

| Lane | Now | Next | Then |
|---|---|---|---|
| **Sol** (builder) | G-02 Cemetery object pilot | G-04 saves for what the pilot changes | F-08 item grants; G-03 other levels |
| **Grok** (research and robot) | G-05 rule, three-hour box | G-06 robot on the Cemetery | must-touch marks in the table; research only when a task names the byte, two hours, then the replacement |
| **Opus 5.5** (integration and build) | Integration branch, review fixes, playtest cuts | G-05 build once Grok's rule is in | G-08, G-07, G-09 |
| **Fable** (lead) | This plan; task files; review of every READY | Status of M1 daily; owner's try-list | Monday numbers |

Proposal that needs the owner's yes: **Opus keeps integration** (merging, cutting playtest builds, qualification) as a working lane, because the lead is not to build.

## 4. How I will run it

1. **Every READY is reviewed within the hour** by a fresh Claude reviewer that is not shown the builder's claims; I read the verdict and decide: merge, fix, or back.
2. **A task is a file with five lines at the top:** what the player will be able to do, the exact starting state, the proof (real input, no aids, first failing then passing), what is out of scope, the replacement if research runs out.
3. **Nothing goes to the owner before the robot has walked it clean.** His walk is one level, 30 minutes, every second day, with a one-page try-list.
4. **Research is on demand:** two hours, then the modern replacement, logged as a deviation.
5. **One status line a day on the board** per milestone: what moved, what is stuck, what I need from the owner.
6. **Four numbers every Monday:** stops per owner walk; days from READY to merged; share of work redone; robot stops found before the owner.
7. **I stop work that is not on the route.** A lane with nothing on the route gets the next route task, not its old queue.

## 5. What I need from the owner

1. Yes or no: Opus keeps integration and playtest builds.
2. Nothing else now. The first walk I will ask for is the Cemetery, when the robot reports it clean.

## 6. What I do not know

- Every duration above is a guess. The object layer is sized by Sol at 5 to 8 working days for the Cemetery and "2 to 3 weeks" for all 219 objects; nobody has built one yet.
- Whether the collision fix can be done at all without moving rooms; the first trial broke five Cemetery routes.
- What the Act 3 levels hide. Only the Cemetery has been examined at this depth; the others have had automated walks with aids.
- Act 1 was not re-examined; I rely on the owner's statement that it is largely done.
- Usage limits of the lanes (Kimi is out for the month; Grok and Sol have their own limits) can stall a week.

## 7. Milestone log
- **13 November 2026: M1 met.** The owner played r19g normally and called it "a great success": a full walk from the start of the game to the Ruloi Citadel now exists (Cemetery layer, rails, ashes, statue, Larkhon). The robot pressed the ankh on r19g with 0 game stops. Planned for late November to early December; reached 13 November.
- **Next milestone, set by the owner (M2b):** get the Dreamstone in the Ruloi Citadel (L13) and return to the Huline Temple (L14) with it, through the Temple chain (priest ritual, pews, doors 92/93, spider wall, headboard). Bars as before: robot first, then the owner's normal play. Open on the way: the owner's full Claw Mountains run (he names 2 issues there), the Temple upper-floor way (Opus), T3/T14 confirmation, spell core (Sol).
- **Correction, same day (owner):** the Cemetery was NOT clean to look at: "a lot of issues to refine away, the glitching over maps and textures, chest panels outside the rooms". M1 is met for walking and quests only. His priority stays: first the walk from start to finish doing all the quests; the look issues are "small fries" until then. His idea for the overlap: use the maps as guidance and redraw them so nothing overlaps. Lead's line: measure each level's true same-height overlaps (as done for the Temple: 20 zones), draw only the rooms connected to the player's room (as on the Claw Mountains, which he confirmed), hide objects with their room, and move or redraw only the zones that still overlap. A full redraw of a level is the last resort, decided per level after the measurement.
- **Owner decision, 13 November: the maps are adapted for modern use.** "It is going to be work but it solves a lot of problems." Standing approval to move or redraw rooms so no two share space, the original maps as guidance, each move a DEVIATIONS row. Order: (1) now: only overlaps that block the main quest (Temple upper-floor way, T3, T14); (2) after the start-to-finish walk: one adaptation pass per level - measure true same-height zones, finer connected-rooms drawing, move what remains, redraw a level only if the zone count makes moving the larger job. Temple first (20 zones known), then Cemetery, then the rest by zone count.
- **14 November 2026, about 07:40Z: the owner's milestone "the Dreamstone and back to the Temple" is WALKED BY THE ROBOT** on r19i with real input: Citadel F2 start -> globe, eye, elevator, vault, spires, dawn gate, 21 ledges, plates, bridge, all ruloi, web, boss, dark sword, Dreamstone, return pad, exit (second press takes the stone back) -> the same life walks across the Claw Mountains to the Temple entrance with the Dreamstone carried ("E - Place Dreamstone"). The Temple itself already walks from the entrance into the City of the Ancients (r19h). Still owed: the owner's own walk. Robot's chain map beyond: City -> Hidden Caverns -> Belial's caverns to the elevator to Dawn (cab fixed 14 Nov); Dawn and L20 not yet reached.
