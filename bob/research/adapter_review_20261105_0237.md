# R2 adapter review, rows 0237–0252, 2026-11-05

No Godot was run. No opcode callee was entered. LOLG.DAT was not opened. The longplay was not opened. No DOSBox. Heads observed: r15 and r15_campaign2 are `f6a5aa4`, r12y is `56812f9`, and act3 is `d9e3aaf`. Newest owner file by mtime is `TRIAGE_20261104.md`, 2026-11-05 00:35:30 +0100.

These sixteen deviation files are absent from r12y. r15 only. This pass does not claim a match.

`adapter_review_20261104.md` already read 0241, 0242, 0243, 0244, and 0251, and it left the other files in 0227–0279 unreplaced. `adapter_review_20261105.md` keeps rows 0227–0308 in those reviews. The new behaviour since those files is the Hive lift. This pass does not reopen that lift. Row 0242’s elevator line is the Hive button gate, not the flute-lift speed.

Counts the rows give stay the rows. This pass did not recount markers, regions, frames, or trees.

## 0237 statue walk

Follow the statue as Human, with Dampen, then watch the statue and the worm. The water rises after the fight.

DECODED. `l9_statue_walk.gd` moves actor 76 only after the bowl receipt. `act2_creatures.gd` lines 6–19 clear that actor’s wake for the shared step, then the walk node writes the body. Line 48 uses 40 and gravity 128. Line 49 calls `try_step`, whose default maximum is 32. Marker values 0 through 11 are the row’s twelve. The fight starts only when `player_form` is 0, the statue has arrived, and the player is inside a source polygon. The movie pauses the tree. The return writes `(4111, 12, -9959)`. The comment names floor −20. That y is the host choice. Opcode 18 was not entered. Region 3565 is cleared with the receipt. Dampen is not read.

HINTBOOK lines 3792–3824. Place the remains in the bowl, follow the slow statue as Human, have Dampen, and watch the video. Those lines print no speed and no coordinate. The 40, the 128, and the paused movie stay the adapter. Dampen stays open, as the row already says. It is not seeded here.

## 0238 urn and ankh

The priest gives the urn, the ashes fill it, the priest gives the ankh, and the ankh opens the Emperor.

DECODED. `l9_pyre_state.gd` lines 37–54 and `l10_ankh_state.gd` lines 22–38 call `item_handlers.gd` `route` before the Kit transaction. Handler 0 is hosted as “no handler” at lines 149–152. The native dispatcher is not entered. `act2_items_catalog.gd` lines 50–51 name definition 78 and definition 97. The full-urn identity stays the row’s definition 168. The outer ankh recipe is retrievable. The Emperor inner recipe is not. No magnitude is written.

HINTBOOK lines 3443–3456 and 3464. The bracers make the priest intelligible, he gives the urn, then the ankh, and the ankh goes in the slab hole. The sarcophagus gives the remains. BRADY lines 8454–8456, printed page 208, and lines 8484–8491, printed page 209, say the same order: urn, ashes, ankh, then the tomb. Neither book prints a retrieve. The Kit retrieve stays the adapter. No simpler dispatcher replaces handler 0.

## 0239 dead bracers item

The bracers allow speech with the dead priest and the Emperor.

DECODED. `dead_bracers_item.gd` lines 5–14 route modes 14, 16, and 18. Mode 18 sets the local to 1 and returns 1. Mode 14 clears it and returns 0. Mode 16 returns 2. Other modes return 0. `available` is true only when a carried item has definition 59. It does not write a native bank. `l10_priest.gd` lines 40–48 and 56–60 show the priest and grant the urn only when that check passes. `l10_emperor_state.gd` line 63 uses the same check for the remains. No worn flag is stored. The 512 vectors stay the row. Handler `0x99b94` was not entered.

BRADY lines 3911–3917, printed page 95. Killing the priest gives the bracers, putting them in inventory is enough, and they give speech with the dead. HINTBOOK lines 3443–3445 say the dead bracers make the priest understandable. Those sentences print no request byte. The carried check stays. It is the inventory sentence, not a worn slot. The request table stays the adapter.

## 0240 empty globe

Collect an empty globe and charge it at the matching altar.

DECODED. `act2_charger_state.gd` lines 36–41 accept definition 98 and call `route` on insert. Handler 0 stays the ordinary-item route. The charged suffix is yellow, white, or blue. No empty-globe spell is added. The charger anchors stay the earlier adapter.

HINTBOOK lines 3267–3268, 3317–3319, and 3335–3336. Gold, then the other colours, and a blank in the tower if only one globe is held. BRADY lines 8405–8406, printed page 207, say an empty globe lies by the Yellow altar. Gold and Yellow are not the same sentence. They stay unmerged. The yellow key stays the host. No book number replaces the route.

## 0241 amaranth

Amaranth serum has no effect alone.

BRADY line 1556, printed page 42. “Amaranth serum has no effect by itself.” Line 1609, printed page 43, is the later mix with Silverleaf. Those sentences stay separate. The 2026-11-04 grade stands: this matches the no-effect-alone sentence, and handler 98 was not entered.

DECODED. `item_catalog.gd` line 203 marks definition 119 as `amaranth_serum`. `player_item_controller.gd` lines 59–68 consume that kind and write no health or mana, except the shaman identity. `item_handlers.gd` line 33 still names handler 98 as consume. The shaman id does not stay on that consume. Deviation 0308 refuses it, and the serum stays carried. Other definition 119 rows still take the consume. Item 26 stays unverified, as 0308 already says. HINTBOOK lines 3163–3165 say to reload a flung potion. They do not name a health write.

## 0242 Hive headless input

Headless play must drive the same Hive actions as the HUD, without seeding the route.

DECODED. `player_starting_magic.gd` lines 100–108 waive mouse capture only while `interface_request` is set, and `world_active` still refuses pause, flight, death, and the modal locks. `hive_warriors.gd` line 57, `hive_review.gd` line 176, `hive_route.gd` line 14, and `hive_elevator.gd` line 125 accept that pair. Captured play is unchanged. This is the button aim gate. It is not the Hive lift speed, and that lift is not reopened.

No book sentence names a headless request. The 2026-11-04 grade stands. The admission stays the adapter.

## 0243 departure headless input

Reach the outbound region on foot and play the departure.

DECODED. `act_one_departure.gd` lines 49–51 require floor contact inside a source polygon, and they accept `interface_request` only together with `world_active`. Health, pause, flight, the HUD, and the shop and dialogue locks still refuse. No inventory value is written on that gate.

No book sentence names that admission. The 2026-11-04 grade stands. The admission stays the adapter.

## 0244 ruins flood

After the statue fight, the water rises.

DECODED. `l9_flood_state.gd` line 4 sets `SPEED` to 2. The comment names the row’s `(source speed 1 * 10) / 4`. Early floors use that continuous speed. Opcode 196 and opcode 204 are not replayed. `river_drowning_state.gd` line 5 sets the shared limit to 15. The row already says that 15 was measured for Cave Human and not for L9. The later 30-second schedule lives in the same height function and belongs to row 0246. It does not replace the early 2.

HINTBOOK lines 3823–3831. The water rises slowly, and a late arrival means a reload. Those lines print no 2 and no 15. The 2026-11-04 grade stands. 2 units/s stays the adapter.

## 0245 tower blank pickup

One empty globe can be taken beside the white charger when the arrival has only one globe.

DECODED. `act2_items_catalog.gd` lines 3–6 place `act2:L9_DR:tower_blank` at `(-3610, 150, -850)`, definition 98. The catalog integer `4086156423` is the row’s identity `F38DCC87`. `act2_world_items.gd` line 20 adds that one placement on L9. Lines 57–58 use reach 96 and facing dot 0.97. It is one world pickup. It is not granted by counting globes.

HINTBOOK lines 3335–3336. A blank can be found in the tower when only one glass globe is held. That sentence prints no coordinate. The point stays the row’s modern pickup. The lead authorization stays the row. This pass did not reopen that note. No census was repeated.

## 0246 ruins lift escape

Jump onto the table, ride to the tunnel, then stand on the raft until the exit.

DECODED. `l9_escape.gd` keeps bodies 122 and 82. Lines 37–41 move the table 160 on x and −300 on z during the first 8 seconds, raise y to 120, then raise toward `regions[6304]` minus 59 over the second 8 seconds. Duration 16 is `l9_escape_state.gd` line 3. Floor 420 stays the row. The raft clock runs 5 seconds at 2 units each, which is the row’s 10. Completion sets control 82 `byte_0x25` to 2 and calls `use_exit`. The kind-5 chain stays the row. It was not entered. Native timing stays UNKNOWN, as the row says. This table is not the Hive lift.

HINTBOOK lines 3825–3846. Jump onto the table, then either throw the grate or stand on it. The hosted branch is the stand-on sentence. The throw stays unhosted. BRADY lines 4105–4113, printed page 99, say to push the platform into the water and step onto it. That push stays a separate sentence. The 160 and −300 drift stays the row’s clearance adapter. No simpler native motion was entered.

## 0247 shore return

The raft exit wakes Luther beside Dawn and closes the way back into the ruins.

DECODED. `l8_shore.gd` lines 12–20 spawn actor 20 only when a level change arrives on selector 5 with the raft receipt. The feedback line is the wake. `act2_progression.gd` lines 280–282 refuse every later level-9 change once that receipt is set. The coordinate `(-4292, 48, -1623)` stays the row. It is not in the shore script.

HINTBOOK lines 3021–3023 and 3468–3471. The wet exit ends asleep on the bank with Dawn, and the ruins are then flooded and inaccessible. BRADY lines 4306–4311, printed page 103, wake him on the Bane with Dawn and say the ruins entrance has changed. Those sentences print no selector. The level-9 refusal stays the adapter. No native closure flag was read.

## 0248 shore Dawn exchange

Offer the bracers and receive the next curse-control item.

DECODED. `l8_dawn_state.gd` lines 22–33 exchange `act2:L9_DR:item55` for `act2:L8_SJ:dawn_control_token` in one Kit transaction. The catalog integer `3421151171` is the row’s identity `CBEA9FC3`, definition 76. `l8_dawn.gd` lines 14–31 require the shore receipt, Human form, reach 150, facing dot 0.8, a clear ray, and `world_active`. The feedback is a summary, not a quotation. Definition 142 is not granted.

HINTBOOK lines 3027–3033. Give Dawn the bracers, listen about reflecting magic, and take the next curse-control item. BRADY lines 4120–4125, printed page 99, say she gives a Control Charm, and that giving the bracers is a choice. Charm and Token stay unmerged. The required exchange follows the hintbook sequence. Brady’s optional sentence stays separate. The summary stays the adapter. Original speech stays unjoined.

## 0249 Baccata trap

Cut Baccata down, speak, and see him leave.

DECODED. `l8_baccata.gd` lines 29–31 invert the idle frames on a billboard at `(4549, 100, -1006)`. Lines 55–66 accept a carried sword, longsword, dagger, or blade label and do not spend it. The second use starts the departure. Lines 71–76 move the body by `(0, -20, 20)` for 5 seconds. The row calls that south. The spoken line is a summary. Attack and leave are not hosted.

HINTBOOK lines 3037–3045. He is in a trap south of the cemetery path. Cut him down. He gives information and wanders off. BRADY lines 4313–4320, printed page 103, add attack and leave as choices. Those choices stay unhosted, as the row says. The inverted billboard and the 5-second steer stay the adapter. No hanging animation was decoded.

## 0250 emperor silverleaf growth

Return without the bracers. The failed talk makes silverleaf grow on the dead trees.

DECODED. `l10_emperor.gd` lines 111–113 send a bracer-less entry to `l10_silverleaf.gd` `revisit`. Lines 31–37 of that file require the remains receipt and the Dawn exchange, refuse while the bracers are carried, and set `grown` without granting a leaf. Lines 25–29 hide props 159 through 170 until then. The list is those twelve ids. The feedback is a narration. No room flag is replayed.

HINTBOOK lines 3046–3054. Without the bracers the Emperor is noise, nothing is on the ground, and the dead trees then grow silverleaf. BRADY lines 4322–4342, printed page 103, say the same failed talk and then ask what is growing. Neither sentence prints a prop index. The narration stays the adapter. The twelve ids stay the source list.

## 0251 silverleaf harvest

Pick silverleaves from those trees and carry them to the village.

The 2026-11-04 grade stands. Props 159 through 170 are twelve grants of definition 117, identity `0E347A01`. Nine placed item rows do not exist. The printed nine does not replace the twelve. This pass does not choose which trees are the nine. The row’s own earned route already names nine and leaves three standing.

DECODED. `l10_silverleaf_harvest.gd` lines 18–26 give one persistent identity per tree and refuse a second pick. `act2_items_catalog.gd` line 37 stores identity `238320129`, which is `0E347A01`. `act2_creatures.gd` lines 63–66 mark actor 113 peaceful after village admission. `scripted_creature_population.gd` lines 149–152 and 310–311 then give that actor no chase and no damage. The faction rule stays undecoded, as the row says.

HINTBOOK lines 3054–3055. Pick nine silverleaves and go to the Wild Village. BRADY line 4344, printed page 103, says collect up to three from the new bushes. BRADY line 8516, printed page 210, says gather as much as you can. Those three counts stay unmerged. None of them replaces the twelve grants.

## 0252 tribe initiation

Offer one silverleaf, hear the shaman, and finish a nonlethal fight with Daniel.

DECODED. `l8_tribe_state.gd` lines 37–48 accept definition 117 and set stamina 500 and 600. `l8_tribe.gd` lines 35–44 play the staged audio, then place the player at `(2679, 32, -4187)` with yaw −45. The row’s source call is `place(2679, 4187)` facing 45 and floor 0. The y 32 is the host foot. That call is not an opcode 18 record, as the row says. Actor 23 is spawned there. Lines 49–55 and 61–76 keep campaign health unchanged, require a melee hit, approach at 40, and subtract 8 stamina every 1.2 seconds. Spells do not pass `receive_strike`. The ARENA movie stays unhosted.

HINTBOOK lines 3069–3074. One silverleaf starts the initiation. Fight Daniel, not to the death. A few blows or spark spells end it. The nonlethal end stays. The spark sentence stays unhosted. BRADY lines 8523–8524, printed page 210, say give the silverleaf and fight Daniel to be initiated. They print no stamina. Actor 23 stays the row’s modern choice. The stamina rules stay the adapter.

## Grade

r15 only. DECODED for the hosts cited above. HINTBOOK for the statue, urn, globe, flood, table, shore, Baccata, silverleaf, and initiation sentences. BRADY for line 1556 printed page 42, lines 1609 printed page 43, lines 3911–3917 printed page 95, lines 4105–4125 printed page 99, lines 4306–4344 printed page 103, lines 8405–8406 and 8454–8498 printed pages 207–209, and lines 8516 and 8523–8524 printed page 210. Gold and Yellow stay unmerged. Nine, three, and “as much as you can” stay unmerged. Charm and Token stay unmerged. LONGPLAY was not opened. No GUESS and no new LIKELY.

The shaman serum consume does not stay. Deviation 0308 refuses it and leaves that one item carried. The other adapters stay. No printed number replaces 40, 128, 2 units/s, 15 seconds, the tower point, the table drift, or the twelve grants. No simpler native build was entered. Handler 98 and the Hive lift stay as the earlier reviews left them.

## Still open

Dampen, native statue steering, the opcode 18 floor word as a write, the handler 70 caller, the native item dispatcher, opcodes 196 and 204, fixed-point water ticks, an L9 drowning measurement, native table and raft timing, the throw-the-grate branch, Dawn’s original speech, Baccata’s conversation and the attack or leave choices, native silverleaf regrowth, the faction rule, item 26, the initiation host calls, and the printed spark-spell bout stay unentered.
