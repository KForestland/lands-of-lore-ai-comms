# R2 adapter review, rows 0223–0236, 2026-11-05

No Godot was run. No DOSBox was run. No opcode callee was entered. LOLG.DAT was not opened. The longplay was not opened. Newest owner file is still `TRIAGE_20261104.md`. r15 is `f6a5aa4`, act3-story is `d9e3aaf`, and r12y is `56812f9`. The board tail is the 20:05:11Z grok receipt for rows 0177–0192. That line is not a new commit and not an Astra question.

`0223`, `0224`, and `0225` match r12y. `0226` differs. The three `0227` files and `0228` through `0236` are r15 only. `adapter_review_20261102.md` left Astra's 0227–0231 absent from r12y `56812f9`. They stay absent. This pass does not reverse that file on 0223–0226.

Hintbook lines are LF lines in `hintbook.txt`. Brady printed pages come only from a `PDF PAGE N = PRINTED PAGE M` marker. Cemetery and Cemetary stay separate. Saar and Ssar stay separate. Gold and yellow stay separate. No Brady line read here contains Ruloi.

## 0223 low fences

MATCH. The high-side running jump with mid-air crouch stays the printed direction rule. The collision guard stays the adapter.

DECODED. `l10_fences.gd` lines 4 and 20–43. Controls 74, 75, and 174 use signs 1, -1, and 1. `admits` requires the high side, an airborne body, sprint, Ctrl, and a direction below -0.5. A passing body drops the fence layer. `restore` puts the layer back. Upper floors above the fence height plus 85 are not blocked.

HINTBOOK lines 3285–3289. Luther runs, jumps, and crouches in midair to leap the low fences. Lines 3296–3298 say the other direction does not work. Lines 3312–3314 say the higher fences are one-way and that going up is the wrong way. Those sentences print no control id and no reach.

BRADY line 4383, printed page 104, spells Cemetary and does not describe these fences. Other Brady lines spell Cemetery. A cemetery-page search returned no low-fence sentence. The crouch-and-jump at line 3968, printed page 96, is a hole, not these fences. Those sentences stay unmerged.

No printed number replaces the guard, the Ctrl binding, or the load reset. The 2026-11-02 reading stays.

## 0224 tomb door collision

MATCH. Opened doors drop their own collider. The base-map filter stays the collision adapter.

DECODED. `act2_map.gd` lines 194–195 drop every L10 static-assembly face whose index is a tomb door or a tomb receptacle. `l10_tombs.gd` lines 23–24 and 65–69 keep a source-sized body and set its layer to 0 only after the slot is committed. Closed doors stay solid. Reach 140 and facing 0.8 are the E test at lines 70–76.

Books print globe-opened tombs. They print no door index and no face filter. No printed number replaces the filter. The 2026-11-02 collision reading stays.

## 0225 dead bracers shield

MATCH. The spark-after-the-fight sentence stays. It is not replaced by a simpler number.

DECODED. `l9_dead_bracers.gd` lines 2 and 25–45. Shield 312 is the rendered collision plane. `release` returns while actor 79 still has health. A later Spark stores `released` and clears the layer. Item 55 is not generated here.

HINTBOOK lines 3710–3711. When the fight is over, a spark spell disarms the force field that guards the dead bracers in the niche. That sentence prints no shield index and no save flag.

BRADY lines 3908–3912, printed page 95. Talk to the Ssar Priest, fight him, and win. Killing the Ssar Priest gives access to the Bracers of the Undead. That page does not say Spark. Line 4120, printed page 99, says Bracers of the Dead. Undead and Dead stay unmerged. Saar and Ssar stay unmerged.

The shield flag, the collision plane, and the save gate stay the adapter.

## 0226 mirror room return

DIFFER. r12y leaves opcode 18 height word 0 and player-move semantics UNKNOWN, and it calls same-area movement a modern adapter. r15 says flags `0x0404` and `0x0C04` select native direct relocation on the +4/+6 pair and heading +12, that clear bit `0x0100` means raw +8 does not assign height, and that grounding to floor+32 remains a host adapter. Spark, grounding, and persistence stay modern in both texts.

DECODED. `l9_mirrors.gd` lines 2, 34–37, and 43–63. A saved opened flag poses movables 65 and 66 from `angle_word` and does not dispatch groups 8602 or 8620. A body-radius touch of regions 3640–3644, 3655, or 2300 writes the stored landing and heading. The comment on line 49 says the opcode 18 height word is not decoded. `l9_mirror_source.json` stores landings (-3027, 232, -8232) and (-1627, 52, -1046). Those y values are the row's floors 200 and 20 plus 32. The file's own grade still calls movement and grounding an adapter.

HINTBOOK lines 3682–3685. One of three teleporting mirrors takes you to the cemetery. Another goes to the Savage Jungle. The third stays in the ruins. Those lines print no coordinate and no flag.

BRADY line 2453, printed page 65, is the Shining Path mirror. It is not this ruins room. No Brady line read here prints these endpoints.

No printed number replaces the flag reading, the body-radius touch, the Spark flag, or the grounded landing. The 2026-11-02 opcode-18 reading stays.

## 0227-row-2026-11-02-statue-aim.md

r15 only. The visible E point stays a modern aim. It does not match r12y.

DECODED. `act2_progression.gd` lines 153–168. On L10, control 150 kind 6 caller 9 moves the E point from the placement origin to the box centre, then two units out along heading. The comment says the origin sits inside the panel.

HINTBOOK lines 3317–3319. A globe placed in the charger claws is clicked again to retrieve it. Those lines print no control 150 and no clearance.

BRADY lines 4166–4167, printed page 100, click an empty orb on a claw altar and click again to take it. That page prints no aim offset.

The two-unit clearance and the E key stay the adapter.

## 0227-row-2026-11-02-tavern-bacatta-promise.md

r15 only. The friendly leave-taking stays the printed path. The two-second window stays the adapter. It does not match r12y.

DECODED. `monastery_conversation.gd` lines 17–24, 162–170, 205–228, and 253–258. Flag 37 starts a 2-second timer. The deadline clears 37 and plays the promise. A later exit raises `GV_BACATTA_RELATIONSHIP` by 1 and sets flag 34. An exit while 37 is set stores relationship 0. The code spells Bacatta.

HINTBOOK lines 2344–2349. The tavern is where you meet Baccata. Clicks keep the talk moving, and an attack is not to be started by accident. Lines 2416–2419 say to follow Baccata to the bridge and listen while he negotiates. Both lines spell Baccata. They print no line number and no flag.

BRADY lines 3032–3036, printed page 77. Inside the cantina, Baccata gives Luther a few hours' grace, and he must be talked to before Dawn. Lines 3499–3504, printed page 86, say a click wakes Baccata and he escorts you across the river. An attack means fighting the guards instead. Baccata stays Baccata. It is not merged with Bacatta.

The timer, the skipped-line window, and the unhosted `+0x118` and `+0x114` calls stay the adapter.

## 0227-row-2026-11-02-world-item-twin-placements.md

r15 only. One sprite and one E owner stay the adapter. It does not match r12y.

DECODED. `act2_world_items.gd` lines 24–27 skip a placement when `hosts_twin` is true. `area_world_items.gd` lines 87–104 and 156–158 keep the area sprite, migrate an older `act2:L8_SJ` twin into the area history, and show `E — Take`.

HINTBOOK lines 1267–1268 name Lamplight eggs as recipe ingredients. They print no second sprite.

BRADY lines 1527 and 1591, printed pages 41 and 43, are the same eggs as ingredients. Line 8327, printed page 205, says to pick Lamplight Eggs up in the Huline Jungle. None of those lines prints a hidden twin.

No printed row number replaces the single owner.

## 0228 caretaker barrel

r15 only. Human, top, and a push toward the north tomb follow the hintbook. Brady's click does not replace them.

DECODED. `l10_barrel.gd` lines 5–9, 29–31, 59–61, and 76–97. The switch opens only after tomb 109. The tip requires Human, the top, reach 140, and a body south of z -1952. Roll speed is 160. A live actor inside 40 horizontal and 80 vertical units stops the roll. The panel withdraws upward by its height plus 8. The comment says that axis is not a decoded hinge.

HINTBOOK lines 3349–3362. A white globe opens the marked tomb. The switch is flipped. Human Luther sidles past the barrel, faces it, and touches the top. A nudge sends it north. It breaks and leaks oil. Lines 3378–3380 repeat Human form and a touch near the top. Those lines print no 160 and no 140.

BRADY lines 4205–4208, printed page 101. Go inside and click the barrel, then bump and push it. It rolls into the first mausoleum and releases oil. Click and sidle stay unmerged. That page prints no speed.

The timed roll, the wait radius, and the upward panel stay the adapter. No simpler native barrel build was read.

## 0229 level-three Spark

r15 only. Cost 3, range 768, and damage 16 stay the adapter. Books print the name and not those numbers.

DECODED. `player_starting_magic.gd` lines 101–104, 152–153, 180–184, 232, and 252. Ctrl+Q calls `cast(3)`. `museum_interface.gd` line 389 does the same for Ctrl-click through `cast_from_interface`. Charge 3 costs 3, travels 768, and deals 16 with effect 22. Charge 1 stays cost 1, range 384, and damage 8. The comment on line 152 calls the level-3 triple a modern adapter.

HINTBOOK lines 3406–3410. The oil needs a level-three spark with enough range. A level-one or level-two spark that can reach the oil also catches Luther. Those lines print no 3, no 768, and no 16.

BRADY lines 1699–1701, printed page 46. Level 3 is named Chain Spark. Launch is a left-click or the S key. That page prints no cost and no range. S and Q stay unmerged.

The request amounts 40 and 35 stay outside this host. Finished mana, range, and damage were not entered. No simpler formula replaces the triple.

## 0230 oil collapse

r15 only. Staying clear of the blast is printed. Accepting a level-1 Spark is less faithful than the hintbook.

DECODED. `l10_oil.gd` lines 4–7 and 110–115. Ignition requires barrel phase 2 and a Spark level of 1, 3, or 5. Radius 240 deals 20 unless protection is on. The flash lasts half a second. The floor swap is immediate. `act2_map.gd` line 192 keeps those faces out of the base collision.

HINTBOOK lines 3363–3367 and 3406–3410. Dragon's blood, a level-three spark, or some other means lights the oil from a fair distance. Level-one and level-two are refused because a cast that reaches is a cast that catches the caster. The black pool is the mark of a good spill, lines 3394–3396.

BRADY lines 4212–4215, printed page 101. Spark or Dragon's Blood hits the oil. The caster must be close enough to hit and not too close. The explosion opens another catacomb entrance. Brady names no level. That silence is not merged with the hintbook's level-three rule.

The 240, the 20, and the half-second stay the adapter. The host's level-1 admission does not follow lines 3408–3410. No printed number replaces the clip or the saved burned flag.

## 0231 priest urn

r15 only. The priest gives one urn when the bracers let Luther understand him. The E gate stays the adapter.

DECODED. `l10_priest.gd` lines 37–53. Tomb 154 must be open. The carried bracers are tested and not consumed. One `priest_urn` is granted with the history. A full pack refuses. The billboard is 120 by 100 at 15 frames per second, lines 28–29. Reach is 140, lines 31–35.

HINTBOOK lines 3443–3448. The dead bracers from the Mage's Tower make the priest intelligible. He gives the container the OCR reads as "um". The body is burned to ash in the ruins. The word on the line is um. It is not silently rewritten.

BRADY lines 4245–4253, printed page 102. Without the Bracers of the Undead the priest is not understood. He gives an Urn for his ashes. Line 4120, printed page 99, says Bracers of the Dead. Undead, Dead, and the hintbook's dead bracers stay three phrases.

No printed reach replaces the 140. The visibility test and the errand sentence stay the adapter.

## 0232 noble rail and chapel path

r15 only. The hintbook breaks the north rail. Brady knocks the east rail. Those sides stay unmerged.

DECODED. `l9_noble_rails.gd` lines 2–4 and 38–48. Controls 478, 479, and 480 break on a landed melee ray of length 96 and stay broken in the save. Bridge 471 is added as a solid in its initial state, lines 27–28. `static_assemblies.gd` lines 63–66 lists balcony decks 481, 482, and 483 as raised decks.

HINTBOOK lines 3726–3738. The two-story building is marked for the priest's errand. Upstairs, the north railing breaks. The west bank leads north to a bridge, then the east bank, then a tunnel, then the chapel.

BRADY lines 3980–3986, printed page 96. Touch or bump the loose railing. Knock it over on the east side and walk on the fallen rail, then follow it north. East and north stay unmerged. Walking the fallen rail is not the hintbook's path along the bank.

The melee flag and the deck exception stay the adapter. No printed control id replaces them.

## 0233 chapel cremation

r15 only. Drag, both orbs, and the urn on the ashes are printed. The 4.2-second burn stays the adapter.

DECODED. `l9_pyre.gd` lines 49–99 and `l9_pyre_state.gd` line 10. E grabs the body. It follows at 120 units per second and places within 100 of the altar. Both orb receivers must Spark before phase 2. The burn clock runs to 4.2 seconds and the fire frame steps at 10 per second. The filled urn is a Kit output, not the unpickable world item.

HINTBOOK lines 3738–3752. The body is dragged onto the altar. A spark spell hits both orbs. The container is clicked on the ash. The return is back through the way just used.

BRADY lines 4014–4016, printed page 97. Drag the priest's body onto the altar between the Dragon Orbs. Spark those orbs. Click the Urn from the Cemetery on the ashes. That agrees with the hintbook on the three actions. It prints no duration.

No printed second count replaces 4.2. The drag speed and the E radius stay the adapter.

## 0234 priest ankh

r15 only. The ankh goes in the slab and the tomb rises. The instant 100 and 90 stay the adapter.

DECODED. `l10_priest.gd` lines 67–76 trade the full urn for the ankh and leave the bracers carried. `l10_emperor_entry.gd` lines 36–37 and 51–57 raise the listed floors by 100 and ceiling 3937 by 90 in one step when the slab slot commits. Overlapping floors and the lower ceilings are clipped to the stair holes. Reach and facing match the other E tests, lines 62–66.

HINTBOOK lines 3455–3457. The priest gives an ankh. It is placed in the ankh-shaped hole beside his tomb. That opens the Emperor's tomb.

BRADY lines 4262–4274, printed page 102. The ashes buy the Dracoid Ankh. A click of the Ankh on the Ankh symbol raises the Emperor's tomb out of the ground. That page prints no 100 and no 90.

The instantaneous lift, the clip, and the two-E exchange stay the adapter. The opcode 18 travel was not entered.

## 0235 emperor receptacles

r15 only. Three charged globes, the ankh again, and the sarcophagus are printed. Colour names and order stay unmerged.

DECODED. `l10_emperor.gd` lines 6–7, 39–43, and 100–128. Boxes 125, 126, and 127 show mode 3 while occupied. Inner door 143 opens when all three and the ankh are committed. Any completion order works, and removal closes the set. The room is a paused 640 by 400 view. The coffin hotspot is (293, 102) size (53, 144). E inside the room grants the remains once.

HINTBOOK lines 3458–3464. Each coloured globe goes in the box of the same colour. Gold, then white, then blue definitely works, and the lines also say there may be more than one way. The sarcophagus is clicked for the dead Emperor's remains.

BRADY lines 4276–4279, printed page 102, require one White Orb, one Yellow Orb, and one Blue Orb. Lines 4296–4302, printed page 103, use the Ankh again while the Bracers of the Undead are worn, then click the sarcophagus. Yellow is not gold. The two orders stay unmerged.

The any-order host follows the hintbook's "more than one way" and does not follow a single Brady order. The Kit receipts and the room grant stay the adapter. No printed frame count replaces the 30-frame claim in the row. That media file was not opened.

## 0236 statue bowl

r15 only. Without the remains the alcove asks the question. With them, the left bowl is the hintbook target. Brady's altar stays separate.

DECODED. `l9_statue.gd` lines 31–40. E inside the source polygon, as Human, returns `Huh?` when the remains are not carried and opens the paused room when they are. The left bowl occupies one remains instance. The walking statue, the worm, and the movie are not in this file.

HINTBOOK lines 3789–3798. Entering the courtyard alcove before the remains makes Luther ask "Huh?". The corpse goes in the big bowl on the left of the special screen. Later lines say the statue walks. This host stops before that walk.

BRADY lines 4301–4302, printed page 103. The remains go on the altar in front of the Statue of Belial. Bowl and altar stay unmerged. That page prints no "Huh?".

The Kit offer and the saved visited flag stay the adapter. The walking path stays open.

## Grade

DECODED for the hosts named above. HINTBOOK for the fence paragraph, the spark-after-the-fight sentence, the three mirrors, Baccata at the tavern and the bridge, the barrel sidle, level-three oil, the priest's container, the north rail, both chapel orbs, the ankh hole, the globe boxes, and the left-bowl question. BRADY for Chain Spark on printed page 46, Baccata on printed pages 77 and 86, the Ssar Priest on printed page 95, the east rail on printed page 96, the altar and the Urn on printed page 97, the barrel click and the blast on printed page 101, the Urn and the Yellow Orb on printed page 102, and the sarcophagus on printed page 103. Cemetary on printed page 104 stays a different spelling. LONGPLAY was not opened.

No printed number replaces the fence guard, the tomb-door filter, the shield flag, or the opcode-18 reading. `0225` keeps its printed spark sentence. The three `0227` files and `0228` through `0236` are r15 only. No simpler native build replaces the cost, the range, the damage, the burn clock, or the lift.

## Still open

The opcode 18 callee, the barrel hinge, native kind-9 Spark coupling, finished Spark mana and damage, the level-1 oil admission against hintbook lines 3408–3410, dialogue timing, the walking statue, and the emperor movie file stay unentered. Gold and yellow stay unresolved. North and east stay unresolved. Bowl and altar stay unresolved.
