# Owner r19g reports, 13 November 2026

Read-only. No patch. The four items on the board at 2026-11-13T15:43Z. Build playtest/r19g `ad1f778`, engine 4.7.2. Reported `h` is the body origin. Feet are `h − 32` (`player_form_body.gd` `FOOT_OFFSET`). Map X is Godot X and map Y is Godot Z. The covers report, the small statue, and the five WORKS reports are outside this note.

## Answers

Temple doors, bundle `report_2026-11-13T14-08-18_386707395`. He walked the lowered ritual sheet south of doors 92 and 93, climbed at the east, and crossed the door plane once, east of door 92. Body x 2499.1, h 68.4, from z −3027.1 to −2991.3, between t 372.027 and t 372.265. The Dreamstone slot is unset, so the door collision was on. The low sheet never reached the door plane.

Dawn at (−4228, −1539). The hintbook meeting is a talk: she wants the dead bracers. The port shows DAWNL8 in the fight-ready idle, fists up, 600/600, and she does not strike. The bracer exchange was already committed, so the E prompt is gone.

Flood at (1560, −1340). After the Belial statue and the worm, the hintbook ruins fill with water, the table and the grate rise, and the ruins stay flooded and inaccessible. He then wakes on the Savage Jungle shore. The port did run that ruins clock and did complete the escape. This jungle shaft stays a dry pit. A later level change into the ruins is refused with a sentence. Water to the top of this shaft is not drawn.

Tiger platform at (3895, −8899, −240). Brady’s switch, inside the snow tiger’s cave, raises a tower in the lake, and the Great Axe Blizzard is on that tower. Prima’s control is a globe, and Prima’s result is a square object and an axe with no stated use. Those stay two controls and two results. The deck under his feet is region 1899 at y −275. No command names it. The cave switch object is UNKNOWN. No L12 script places the axe on that deck.

## Temple doors

His words: “cant opend doors can cheat around tho”. Stand (2416.12, −2959.51), h 52.04, area L14_HT. 387 poses, t 256.491 to 376.357, all `MapL14_HT`. The last pose is that stand.

Doors from `assets/lol2/generated/maps/L14_HT/area.json`. Movable 92 is x 2412–2483, y 0–80, z −3029 to −3025. Movable 93 is x 2340–2411, the same y and z. Together they are a slab at z ≈ −3027. `l14_temple_doors.gd` builds `OriginalMainDoors92And93` from those faces and keeps `collision_layer` 1 until `l8_temple_door_state.gd` slot `temple:entrance1198` is committed. That slot accepts definition 136, the Dreamstone. The save has no `l8_temple_door` record. The carried Act 2 item is `act2:L14_HT:post_shard`. No Dreamstone.

The ritual had already run. `l14_priest_ritual` slots 369 and 370 are committed, `lowered` is 2.0, and the body is on slab 816. `FLOORS` gives region 828 the word −30, and `lowered` 2 puts that node at y −30. Fifty-five poses from t 311.7 to 367.7 stay at h 2.01–17.7, feet on that sheet: x 2316–2504, z −3614 to −3249. The northernmost of those is (2381, −3249) at t 364.849, about 222 south of the door plane.

At t 367.927 the body leaves that height near (2536, −3242). h goes 2, then 31, then 66, and settles at 52. The only packed floor quad there is ritual region 801, which the same owner holds at y −30, so the climb has left the sheet. The next stand with a non-ritual floor under it is (2552, −3178), floor region 797 at y 0. Along the east side, at (2508, −3113), the horizontal surfaces are floor 781 at y −80 and its ceiling at y 20, plus floor 793 at y 0. Feet at h 52 are on that y 20 ceiling.

The only crossing of z −3027 is the one sample above. Door 92 ends at x 2483, so the body origin is 16 units east of the slab, inside the door’s vertical span and past its east edge. At that xz the packed surfaces are floor 781 at y −80 and ceiling 781 at y 20. Feet at h 68.4 are about 36, above that ceiling, so the sample is a step across the corner. Wall region 792 runs from (2547, −3101) to the jamb (2483, −3025), y 0–80. The body is about 11 units off that segment, on the outside of the corner. Wall region 957 leaves the same jamb toward (2527, −2975), y 0–150. The player radius was not measured, so 16 units is the body-origin gap, not a proven width of the opening. One crossing only.

He stops on the north side at the report stand. Under (2416, −2959) the packed floors are region 955 at y 0 and region 3360 at y −80, and region 3360’s ceiling is y 20. Feet at h 52 sit on that ceiling.

Opus closes this east-of-92 way once the floor-0 walk to the pew works. This note does not patch the temple.

## Dawn

Bundle `report_2026-11-13T15-25-04_4992379789`. Words: “dawn looks she wants to fight me”. Stand (−4228.42, −1539.17), h 32.04, scene `darker_jungle.tscn`, save area L8_SJ. The picture shows DAWNL8 600/600, fists raised, a dark water plane behind her, and no E line. The prompt bar is the ordinary Tab / Atlas / Journal line.

Actor 20 in `act2_populations/L8_SJ.json` is definition 13 DAWNL8 at (−4252, 0, −1515), health 600, behavior 14, `present` false in the pack. The stand is about 34 units from that point. The save has her present, unwoken, rise −1, live mode 0, health 600. Mode 0 is idle.

L8 `dormant_pose` is `idle`. `scripted_creature_population.gd` `present` shows `clips.idle` for an unwoken actor when that pose is idle, and the comment there calls idle the fight-ready stand. A `peaceful` clip would be the calm stand. DAWNL8 has idle selector 0, 11 frames, and no `peaceful` clip, so frame 0 of idle is what is drawn. Her `attacks` list is empty, and `advance_live` forces idle and returns 0 in that case, so she does not strike. `act2_creatures.gd` `peaceful_actor` does not include actor 20.

`l8_shore.gd` spawns actor 20 on a level change into selector 5 after `l9_escape.escaped`, and sets `l8_shore.arrived`. Selector 5 is native (−4292, 1623), region 66, beside her. The atlas place named riverbank is (−4086, −1596). The atlas lake shore (1730, 2968) is a different place. The nearest water regions to the stand are 32, 59, and 62, surface 70, about 160 units away. That is the plane in the picture.

`l8_dawn.gd` aims at (−4252, 65, −1515) and offers “E — Give Dawn the Bracers of the Dead” only while the exchange is not completed, within 150, facing dot 0.8. Both the 15:25 and the 15:27 saves already have slot `dawn:bracers` committed. The prompt is gone. The idle clip is unchanged by that receipt.

Hintbook `reference_hintbook/hintbook.txt` 3475–3479 and 3861–3864: after the flood he wakes on the Savage Jungle lake shore, and Dawn wants the dead bracers and talks. That meeting is not a fight. No longplay frame of this meeting was opened for this note.

Grade. HINTBOOK for the talk. PORT for the fight-ready idle in the screenshot and in the unwoken clip path. She did not attack.

## Flood

Bundle `report_2026-11-13T15-27-10_5118091053`. Words: “after the staue of belial destrys the snake demigod water to the top here”. Stand (1560.11, −1340.33), h 32.04. The picture looks down a dry tree-pillar shaft: stepped ledges, a grate on the bottom floor, no water surface. He stands on region 396, floor y 0. The shaft floors beside that rim are regions 388, 389, 393, 394, 395, 428, 429, 437, 439, 440, 441, 463, and 466 at y −500, and 391 and 392 at y −400.

`assets/lol2/generated/liquid/L8_SJ.json` has 40 regions. The nearest to this stand is about 3800 units away. None of them fill this shaft. The water beside Dawn is the west set, around x −6700 to −4150.

The atlas names “Pit to the Dracoid Ruins” at (1245, −1392), reveal 140, exit to L9_DR. `tests/fixtures/l8_pit_descent_walk.json` uses pit (1245.25, −1392.5), and its walk passes (1581.5, −1344.5), about 28 units from his stand. Hintbook 3333–3334: enter the ruins through the pit in the Savage Jungle. Hintbook 3468–3475: this stage leaves the Dracoid Ruins flooded and inaccessible. Hintbook 3816–3864: the Belial statue fights the worm (“sploots”), water rises in the corridor, lifts the table, then the grate, and he wakes on the Savage Jungle lake shore. The worm is his snake demigod.

The 15:27 save, and the 15:25 save before it, already have `l9_statue_walk` arrived and `fight_done`, `l9_flood` elapsed 68.65 and dead false, `l9_escape` boarded, escaped, lift 16, raft 5, and `l8_shore` arrived. `l9_flood.gd` raises the L9 water meshes when `fight_done` is set. `l9_flood_source.json` scope says the opcode 204 −1 arm, the floor-flag 0x10 water presentation, the floating-table motion, and flood damage are not hosted by that extract. `l9_escape.gd` then calls `use_exit("control:82")`, which is selector 5. `act2_progression.gd` refuses a later change to level 9 while `l8_shore` is closed, with the sentence “The ruins are flooded. This entrance is closed.” That sentence does not draw water in this shaft.

The byte that would fill regions 388–466 was not read. The ruins clock did run, and he did escape. The missing picture is water in this jungle shaft.

Grade. HINTBOOK for water filling the ruins and closing them. PORT for a dry −500 shaft and a refusal sentence on the way back in.

## Tiger cave and the lake platform

Bundle `report_2026-11-13T15-39-42_5869815142`. Words: “the pussele is the switch inside the tiger cave and rasies this plaform with blizard axe”. Stand (3894.78, −8899.07), h −240.34, area L12_CM. Feet are about −272. The picture is a flat frozen sheet, four braziers ahead, ice cliffs behind. No raised tower and no axe are in the frame.

The floor under the stand is region 1899, y −275, x 3771–3975, z −9015 to −8783. Movable 66 has an empty event list. Its placement decodes to (3928, −8909). The only command in `native_scripts/L12_CM.json` whose target is 66 is group 2654 opcode 20. That is not a floor command. No command of any opcode targets region 1899. Fifty-three opcode 196 commands exist on this level. Region 1899 is not among them.

The accepted opcode 196 formula, from `I03_starry_tower.md`, applied here and not re-proved: the signed word at byte +4 is an absolute floor target, byte 6 is 0, byte 7 is speed. Prop 185, placement (3752, 0, −8638), has one event, kind 2, value 48, group 824. Kind 2 value 48 is not labeled as a use or as a region entry in a source comment read for this note. Group 824 then runs nine opcode 196 commands. Their packed floors are all y −275, just north of region 1899:

| Regions | Word | Speed byte |
| --- | --- | --- |
| 1901 | −175 | 0x0a |
| 1828, 1897, 1905, 1907 | −150 | 0x0a |
| 1902, 1898, 1900, 1906 | −200 | 0x0a |

Byte 6 is 0 on all nine, so this is the form the formula accepts. From y −275 those targets are higher. The commands do not name region 1899 and do not name movable 66. Prop 185 sits on that north edge, about 298 units from the stand.

The other L12 opcode 196 form has byte 6 = 9 and word 20, on regions 3002–3019. Those floors sit around x 1410–1720, z −3660 to −3280. They are not this deck. The host refuses byte 6 = 0x09. That refusal is not this platform.

Cave tigers are definition 5, name STIGER. Actor 37 is present, health 1200, behavior 14, at (3354, −250, −6926), about 2046 units from the stand. Actor 29 is the same definition, present false, at (3356, −250, −6586). Actor 37’s groups are 6562, 6568, 6574, 6592, 6620, and 6628. They are opcodes 5, 16, 13, and 198 on the actor, plus one opcode 198 with target 0. None of them is opcode 196. Prop 193 near that cave, group 974, is opcodes 9, 16, and 5 on props 193 and 253. It does not move a floor. Outdoor STIGER actors 24–28, definition 6, stand around z −6270 at y 0.

No `l12_*.gd` owner hosts a tiger switch, this deck, or the axe. The only hit under those scripts for those words is a comment in `l12_river_rafts.gd`.

Books, already split in `review_20261101/l12_claw_cards.md` and not merged here. Prima printed 119–120: chop the tiger, go in as the lizard, light the globe, a square object rises, the Beast grabs an axe, and that axe has no stated use. Brady printed 191 and printed 211 steps 53–54: enter the snow tiger’s lair as a lizard, throw the switch in the small cave, cross the ice floes to the Great Axe Blizzard on the tower that rose. The switch and the globe stay two controls. The square object and the tower stay two results. The unnamed axe and the Great Axe Blizzard stay two names. The Great Axe Blizzard is not the War Axe Traitor. His sentence matches Brady.

`item_handlers.gd` group 35, handler 84, grade UNKNOWN, likely a cold on-strike effect. No L12 script places that item on region 1899 or on movable 66.

Grade. HINTBOOK and BRADY for the split, with his sentence on the Brady side. PORT for a deck that stays at y −275 with no command naming it. The cave switch object is UNKNOWN. G-03 can host the row later. This note does not patch it.
