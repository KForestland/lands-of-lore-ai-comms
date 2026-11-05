# GROK task list I — 36 tasks (lead: Opus), 2026-11-05. Do these AFTER finishing list H (H01-H22).

Goal: finish the game A-to-Z. The lead builds Act 3 (branch act3-story, ~/opus_work/lol2_act3) and fixes owner
playtest blockers. You research so the lead never has to guess. Read-only: no Godot, no code edits.
For each task: native ids (scripts/lol2/native_scripts/<AREA>.json in ~/opus_work/lol2_act3), decoded groups +
predicates, Godot positions (x, -native y), hintbook/Brady lines, longplay frame (Act 2+: ~/lol2_original_screens/
longplay_frames_act2plus/g_NNNNN.jpg, g_N = 6580+(N-1)*30 s; Act 3 city is about g_296..g_344, finale g_348..g_390),
player steps, REQUIRED or OPTIONAL. Grade every claim HINTBOOK / BRADY / DECODED / FRAME. Mark what stays UNKNOWN.
Write grok_research/I<NN>_<slug>.md, one board line "[grok] I<NN> DONE ..." each, keep status/grok.md current.
Time-box ~45 min each. New owner F10 reports in playtest_feedback_20261023 ALWAYS go first (triage table on the board).
The lead's Act 3 notes so far: docs/l14-chamber-voices.md, docs/l16-arrival-elevator.md, DEVIATIONS rows 2026-11-04/05.

## A. Ancient City (L16_CA) - the lead's next builds, in this order
I01 How does the player PHYSICALLY reach the NE tower's FireWall Doors (movables 92-94, native ~(2290,2947))? The nav
    regions 10205/10198/3018/3127 are an island in creature_nav; walking south from the hourglass falls through the world.
    Find the real walkway (bridges, canal crossings, other movables/doors, stairs, teleports) from the greenhouse (2289,648).
I02 STORY-069 NE tower interior: stairs, the box, the shimmering disk; what pushing the box through it does (level/teleport).
I03 STORY-076 Starry Tower: the square hole where you arrive, the yellow eight-sided figure, the center structure section.
I04 STORY-071 SE tower: oil under the head statue, burning it, the Dark Bow, the blue bow rule.
I05 STORY-072 NW tower: fireball destroyed with the blue bow, white ball (level-3 imp / pyrapod spark), spinning brick.
I06 STORY-073/075 SW tower: four ivory chips, four pedestals, the disk.
I07 STORY-074 chip spots: force field behind sparked globes, straight walk to a gargoyle, prop 626 freeze-and-break
    fountain, collapsing room with boxes on two raised squares.
I08 STORY-077 center tower: entry after the 4th raise, last faux-Belial, horizontal bars of light, the mantle.
I09 STORY-078 dragon room (chop the real dragon), one-way teleporter after the mantle.
I10 L16 list of every Telepad / level change / opcode 18 relocation with source and destination (who moved the lead's
    probe from (2289,-1427) to the arrival point - fall reset or a teleporter?).
I11 Each tower's Ball O Smoke (props 600, 601, 603) path and which FireWall doors each opens (602 = NE, done).
I12 Decode the kind-10 record matcher (the host says "matcher for record kind 10 was not entered"): what event kind 10 is
    and what input it needs.
I13 Silverleaf Pyramid prop 605 predicates with left type 4 ('0604780404', '0604cf0405'): decode left type 4.

## B. Finale (STORY-079..093, L17_HC / L19_BC / L20_BB)
I14 STORY-079/080 Subterranean Caverns: running for the exit, red strands on the west wall, the beast route.
I15 STORY-081 Belial's Horn from Baccata before he dies.
I16 STORY-082/083 bars as Human, gutter as Lizard, shooting, the switches and the guck.
I17 STORY-084 the short path (door, right, right, south, east...) as region ids.
I18 STORY-085 four ghostly heads, level-one mists of doom, the demon, the drag.
I19 STORY-086/087 Dawn's advice and casting the curse at ancient-magic level five into the mother beast.
I20 STORY-088/089 blue pillars, faux-Belial, moving pillars and stairs.
I21 STORY-090 Armory: left spinning brick, white ball with a pyrapod.
I22 STORY-091..093 faux-Draracle, Belial's room, the final fight (blue bow / Dark Sword / horn), the last scene + ending movies.
I23 Every finale movie (VQA names, MIX entries, frame counts) in play order, so the lead can stage them.

## C. Act 2 blockers from the owner's r14 playtest (TRIAGE_20261104.md)
I24 The Dracoid quest (Brady 35-44: urn, Dracoid Ruins hotel railing, priest body on the platform, Spark both pedestals,
    ashes, ankh, Emperor's tomb): for each step, is it hosted in the r14 code (grep scripts/lol2/l9_*, l10_*), which test
    covers it, and what would stop a player. Owner: "cant finish the drackoid quest".
I25 L8 village admission chain from the owner's state (l8_journey gift=recovered, admitted=false, temple_visited=false):
    the exact next player steps and the code that gates each (l8_*.gd).
I26 L8-CACHE-LADDER: the ladder at Godot (-1076,-2621) under the Shaman's Treasure Cache (h222): native records, how the
    original climbs it.
I27 L8-TREE-BRIDGE: knock over the tree near (5063,1888) to bridge the chasm to the Larkhon (Brady step 51): records.

## D. Engine decodes that unblock many steps
I28 Opcode 14 arm 5 (if H21 not finished).
I29 Opcode 18 relocation/drift modes (flags 0x0004 / 0x0804 / 0x0812): which are teleports, which are drifts, speed.
I30 Opcode 2 arm 0x10 (+N magic level) and arm 0x0C/0x0B rewards: confirm stores (lead decoded 0x10 at 0xD88CD).
I31 Region kind-12 descriptor events: when does the original fire them (enter, stand, leave)?

## E. Maps and longplay support
I32 MAP-MARK L16_CA: put every tower, puzzle, telepad and chip spot into MAPS/L16_CA/markers.json with grades.
I33 Longplay frame table for Act 3: each STORY-066..093 step -> the g_ frame(s) that show it.
I34 MAP-MARK L17_HC, L19_BC, L20_BB the same way.
I35 Hive beats 63/70/73 follow-ups if H01/H02 left open items.
I36 When everything above is done: GROK_STANDING_IDLE.md loop (proposals, verifying lead commits' DEVIATIONS rows).

## PRIORITY INSERT (owner 2026-11-05): do this right after H22, before I01
I00 TEMPLE-PORTALS (L14_HT): list every portal/teleport door in the Huline Temple (owner F10 18:10:50 at (-310,-2304): "the
    doors are teleporters, not real doors; their textures clip into the main map"; 18:01 reports at (2625..2884,-2698..-3375)
    "textures all wrong; geometry wrong"). For each: the door object, its group (opcode 18 relocation / level change), the
    source and destination region + coordinates, and which separate "room" geometry sits stacked inside or overlapping the
    main temple (regions, floors, bounding boxes). Output a table the lead can turn into teleports + per-room visibility.

## OWNER ORDER 2026-11-05 ~01:50: MAPS TO 100% FIRST, then quest chains (guides/walkthroughs), then Act 3.
New order for you after H22: I00 (Temple portals) -> MAP-MARK-L1_DC, L3_DH, L4_HJ, L5_HC, L7_DH (backlog, same format
as your Act 2 levels) -> a MAP GAP LIST: every owner F10 map/texture/clipping/collision report in playtest_feedback_20261023
(TRIAGE_20261103.md sections D/E and later reports) that is still open in r14, one row each with area, coords, what is wrong,
and the native faces/regions involved -> then I24-I27 (Act 2 quest chain) -> then the rest of list I.
