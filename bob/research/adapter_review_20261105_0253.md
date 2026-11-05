# R2 adapter review, rows 0253–0268, 2026-11-05

No Godot was run. No opcode callee was entered. LOLG.DAT was not opened. The longplay was not opened. No movie frame was opened. r15 is `f6a5aa4`. r12y is `56812f9`. These sixteen files are r15 only. They are absent from r12y. The same texts are in r13 `71d6c73`, except 0268, which is longer on r15. `adapter_review_20261104.md` re-read 0261, 0262, 0263, and 0267 and scanned the other files in 0227–0279. Those grades stay. Slice 7 stays on row 0308. `adapter_review_20261105.md` left 0227–0308 in those reviews. The Hive lift is not in this set. It was not reopened.

Hintbook line 226 titles "The Citadel of the Ruloi". Hintbook line 289 titles "Birthing Chamber". Brady line 342, printed page 10, and line 1075, printed page 28, print "Birthing Chambers". Those titles stay separate. They are not this web. A search of `brady_guide.txt` finds no "Ruloi". Brady prints "Ru-Loi" and, at line 1611, "Ru-loi".

## 0253 shaman serum and arena departure

Return after initiation and trade another Silverleaf for Amaranth Serum. The departure collapses the settlement rooms.

DECODED. `l8_shaman_trade.gd` lines 23–36 consume one definition 117 and grant `act2:L8_SJ:shaman_amaranth`. `act2_items_catalog.gd` line 48 names definition 119, "117-Amaranth sr", identity 77237872. That integer is the row's `049A8E70`. `l8_tribe.gd` lines 95–115 require membership, then one E beside actor 23, and write phase `departed` at (531, 32, −4414) with `rotation.y` of 90 degrees. The exit note's source argument is heading 180. This pass did not join 180 to 90 degrees. The HUD sentence is a summary. It is not a quotation.

HINTBOOK lines 3070–3077. A silverleaf starts the fight with Daniel, not to the death, and the next silverleaf buys a potion. Lines 3910–3911 name that potion amaranth, from the shaman. BRADY lines 3780–3781, printed page 93, and lines 8526–8527, printed page 210. After the initiation, the shaman gives Amaranth Serum. Those sentences print no coordinate and no identity. The Kit receipt and the room collapse stay the adapter. Heading 180 stays the source argument. The 90-degree turn stays the host.

This row grants the serum. It does not use it. Row 0308 stays separate. BRADY line 1556, printed page 42, still says Amaranth serum has no effect by itself. The shaman serum is refused and stays carried.

## 0254 tribe clubhouse

A member speaks to the guard, the paired doors open, and three Ancients' Stones can be taken.

DECODED. `l8_clubhouse.gd` lines 4–71 require tribe membership, wake actor 21 inside 300 units, and open movables 51 and 52 by the full stored angle word at once. Stones are `item32`, `item33`, and `item34`. `act2_items_source.json` lines 640–685 give each definition 68 and grade LIKELY. The child-bound hinges are the host's pivots.

HINTBOOK lines 3137–3141. After membership, the guard of the clubhouse opens the doors. Several Ancients' Stones are inside. BRADY lines 7520–7521, printed page 177. A Tuani Warrior may enter the hut, where some Ancient's Stones wait. Brady does not print "clubhouse". The names stay separate. "Several" and "some" do not replace the three source rows. Membership stays the printed gate. The 300-unit wake, the welcome sentence, and the hinges stay the adapter.

## 0255 Huline speech

E on a living Huline plays one original cue, then the older interaction continues.

DECODED. `l8_huline_speech_state.gd` lines 3–5 bind actor 93 to sound 237, actor 92 to 1012, and actors 23 and 82 to 1016. `l8_huline_speech.gd` lines 23–64 require Human form, reach, facing, and a clear ray, and store each id once. Actor 23 is eligible only in phase `complete`. Actor 82 must already be present. Selector 413 is not in the map. No quotation is written.

Books print no sound 237, 1012, or 1016. The cue map stays the row. The E trigger and the audio hold stay the adapter.

## 0256 east river and Larkhon passage

Mix the serum with a Silverleaf, activate it, and use it on the guardian.

DECODED. `l8_larkhon_state.gd` lines 28–47 deposit definition 117 and 119 and retrieve the vapors. `l8_larkhon.gd` lines 46–108 activate that dose and apply it to actor 115's upper chest. Regions 3277 and 3278 open. Regions 3455–3457 stay clear. `SLEEP` is 60. Lines 14–16 and 87–94 use that clock for the fall frames, selectors 9 then 8, and then hold the guardian asleep.

HINTBOOK lines 3146–3157. Jump the east river as Human, combine the potion and the leaf, left-click to activate, and right-click the Larkon's upper chest. The same page also spells "Larkan". Lines 3177–3178 say it still sleeps, then wakes after the exit. BRADY lines 1609–1612, printed page 43, and lines 4396–4401, printed page 105. Combine Silverleaf with Amaranth Serum and use the Larkhon Vapors on the Larkhon. The spellings stay separate. The books print no 60 and no region. The recipe and the chest aim stay the printed actions. The two deposits, the 60-second frame clock, and the missing throw stay the adapter. The row's wake does not stay. The host holds the guardian asleep, which is row 0307. Timer words 780 and 720 stay UNKNOWN.

## 0257 Claw glacier and ice crossing

Avoid the logs, keep to the right wall, and cross the ice.

DECODED. `l12_glacier.gd` lines 9–63 and `l12_glacier_state.gd` lines 5–22 own floors 919–930 and assemblies 52–57. Entry in region 932 or 916 starts a move from −590 toward −1090 at speed 50. The clock adds `delta * 60` and calls `floor_motion_step.gd` `advance_one`. That file's comment names 6507B. This pass did not enter 6507B. Started motion hides the six logs. No ice-platform host was opened.

HINTBOOK lines 3962–3975. Do not take the logs on the way in. Stay by the right wall or the avalanche catches Luther. Lines 3980–3991. One running leap from the ice ledge, as Human. BRADY lines 4453–4462 and 4477–4478, printed page 106. Pass the avalanche along the right wall, then jump from one ice platform to the next. Lines 7939–7940, printed page 192, say the same platform descent and a further leap. The single leap and the platform chain stay separate. Neither replaces the other. Speed 50, the 60 Hz clock, and the log removal stay the adapter. Control 91 stays unhosted.

## 0258 Kenneth, Baccata, and the citadel entrance

Search Kenneth, throw the picture, speak with Baccata, and play the entrance movie.

DECODED. `l12_citadel.gd` lines 4–77 and `l12_citadel_state.gd` lines 4–38 search the body at (4599, −590, −14076), arm the picture, and convert it to the charm on an upward ground hit. Actor 30 appears only after the earned rescue, inside 300 units. Talk must precede the movie. The aim comment is deck top −1251 plus 11. Catalog lines 45–46 are definition 81 and definition 90. Charm statistics are not written.

HINTBOOK lines 3992–4000. After the river, meet Baccata, then search Kenneth, throw the picture, take the charm, and trigger the citadel scene. BRADY line 4468, printed page 106, and lines 8554–8558, printed page 211. Kenneth's body marks the chasm, before the platforms and before Baccata. Lines 7898–7901, printed page 191. Throw the picture down. A charm is inside. The two orders stay separate. The host follows the row's body-before-Baccata order. The ground-hit conversion, the summary speech, the aim lift, and the movie skip stay the adapter.

## 0259 first citadel iris

Spark the first globe to open the way toward the egg chamber.

DECODED. `l13_egg_door.gd` lines 2–49 accept Spark level 1 or 3, hide assembly 106, and clear region 1226. Mana stays on `PlayerStartingMagic`. The open is instant.

HINTBOOK lines 4086–4090. Light the globe with a spark to reach the egg chamber. BRADY lines 4600–4613, printed page 109. Click an orb switch, then an eyeball switch, and run to the Egg Chamber. The spark sentence and the click sentences stay separate. The book-to-switch join and the instant hide stay the adapter. Iris animation and actor 37 stay unhosted.

## 0260 citadel eye and basin

Open the chamber, destroy the light, and take the exposed items.

DECODED. `l13_eggs.gd` lines 2–75 take Human E at the eye and hide irises 107 and 108. Spark on vent 265 hides 265 and 364. `DRAIN_TIME` is 2. The basin node drops 20 units across that time. Items 145, 146, and 147 are refused until the drain finishes. Equipment is not written.

HINTBOOK lines 4091–4096. Destroy the light over the eggs. The basin empties and items are uncovered. BRADY lines 4623–4628, printed page 109, and lines 7980–7982, printed page 194. Destroy the central light vent. The acid drains and the pool can be searched. Brady names Coward's Shield, Crossbow Myriad, and Halberd Bastion. This pass did not join definitions 50, 32, and 19 to those names. The 20-unit drop and the 2-second rate stay the adapter. Egg retaliation stays unhosted. The elevator is no longer pending in the host. That later slice is 0261.

## 0261 citadel elevator descent

The row binds Spark and nearby E. Brady says click the brain.

DECODED. `l13_elevator.gd` lines 15–82 start at height −40 and speed 60. Spark level 1 or 3, or nearby Human E, sets the remaining distance. The same 60 Hz clock and `advance_one` step move floors 147, 148, 149, 153, 154, 159, and 163. A support ray carries the player. Gate 102 hides at −1040. The current `activate` also toggles back to −40. That toggle is 0263. `call_upper` is outside this set and was not regraded.

BRADY lines 4636–4638, printed page 110, lines 7984–7985, printed page 194, and line 8051, printed page 196. Click the brain, or the Brain Switch, to descend. None of those sentences prints Spark. HINTBOOK lines 4098–4099 say to spark the globe in the elevator. That sentence stays separate. It does not restore the Spark binding. The 20261104 simpler build stays. The Spark binding does not stay. The click stays. The 6507B step and the 60 Hz clock stay as that review left them. This pass did not enter the native multiplier.

## 0262 citadel maiden room

Jump into the green plate and use the upper-left switch. The women stay until the enemies are dead.

DECODED. `l13_prison.gd` lines 19–88 open on a Human jump within 45 units of the plate, with the foot 10 to 90 units over it. The upper-left control plays the refusal while any actor 21–39 has health, and the release only when none does. The world pauses. Escape leaves. The 100-by-100 plate size stays the row. It is not in this host.

HINTBOOK lines 4127–4136. Jump into the circular green thing. Trip the upper-left switch. The maidens stay until all of the Ruloi are dead. BRADY lines 4691–4693, printed page 111. The women cannot be freed unless all the Ru-Loi are dead. Lines 8000–8001, printed page 194. Spark the device left of the cell, then pull the switch. The jump and the spark-first step stay separate. The host follows the jump and the upper-left switch. The spark-first step stays unhosted. BRADY lines 4707–4708, printed page 111, print a total of 19 Ru-Loi. Hintbook does not print 19 in this paragraph. The names stay separate. The overlay and the live health test stay the adapter.

## 0263 citadel elevator return

The same floors return to −40.

DECODED. `l13_elevator.gd` lines 56–60 refuse a second press while `remaining` is not 0 and set `remaining` to 1000 when the height is −1040. The carry and gate 102 stay the descent host. No actor health or inventory is written.

The Brady descent sentences above name the way down. They were not read as authorizing this return. HINTBOOK lines 4060–4061 name a ramp and a teleporter for Ruloi who retired upstairs. That route stays separate from these seven floors. The lead-authorized return stays the adapter. Native groups 6962 and 7088 stay unentered.

## 0264 raised Ruloi approach

After the vent breaks, some actors move toward the player.

DECODED. `act2_creatures.gd` lines 79–96 run only on L13 after `vent_broken`. A live actor 21–39 moves when the player is 80 to 400 below and within 640 planar units. Speed is `scripted_creature_state.gd` line 12, value 48. Hits stay on the existing melee and Spark.

HINTBOOK line 4016. The Ruloi fly. Lines 4064–4072. Some lurk high, and a spark can show them. BRADY lines 4646–4649, printed page 110. The Ru-Loi attack, then fly away. "Fly away" is not this approach. The 80, 400, and 640 limits stay the adapter. Native flight stays unhosted.

## 0265 ground spires and Dawn's entry

Light two globes, then jump into Dawn's prison.

DECODED. `l13_spires.gd` lines 25–60 accept Spark 1 or 3 on the source ids and finish at once. Both 170 and 171 hide walls 472 and 507 and raise the region-457 ceiling node by 128. `l13_dawn_prison.gd` lines 53–57 then admit the same 45-unit jump band. The visit requires that pair.

HINTBOOK lines 4086 and 4123–4126. Light globes with a spark. Two globes open the way to Dawn's prison. BRADY lines 4695–4705, printed page 111. A brain switch and a teleport disk lead to Dawn, and the Dreamstone is required to rescue her. The globe pair and the brain-switch path stay separate. The instant light and the 128-unit ceiling move stay the adapter. The absolute −912 stays the row.

## 0266 Dawn's Dreamstone

Use the stone, keep it, and take the gift.

DECODED. `l13_dawn_release.gd` lines 21–36 refuse a full inventory, require definition 136, return that same stone, and add one Bestial Disk. `l13_dawn_prison.gd` lines 75–89 play cue 500, then 600 when the relationship is 1 or 2, otherwise 951. Catalog line 43 is definition 136, "134-Dreamstone". Line 44 is definition 80, "78-Bestial disk". Soul and actor removal are not written.

HINTBOOK lines 4137–4139. The dreamstone frees Dawn and is not used up. BRADY lines 8029–8030, printed page 195. Click the Dreamstone on the lock. Take the Bestial Disk. The books print no relationship test. The return and the one disk stay the printed result. The chooser and the skipped native stores stay the adapter. No stone is seeded.

## 0267 disappearing bridge

Cross while the plates are visible, after the side ledges.

DECODED. `l13_bridge.gd` lines 2–42 own controls 90–100 in the row's order, plus iris 84. Life is 3 seconds, spacing 0.45, period 9. Iris 84 stays solid until the Dawn pair is lit, then it loses collision. Hidden plates have no collision. The east-landing test starts the wave. The clock pauses when the world is inactive.

HINTBOOK lines 4123–4124 and 4153–4160. After the globes, a bridge high up appears and disappears. Pink side ledges lead to it. A fireball crosses as it appears. BRADY lines 8008–8011, printed page 195. The plasma bridge exists for a few seconds. "A few seconds" does not replace 3. Pink ledges and plasma stairs stay separate. The 20261104 reading stays: 3 seconds is timer word 180 at 60 Hz. The 0.45 spacing, the 9-second period, and the Dawn binding on iris 84 stay the adapter. Effect 14 was not entered. Brady lines 7995–7997 and 8053 remain a different Brain Switch, as that review said.

## 0268 first Belial admission

Cross the web, play the movie, and open with third-level Healing against poison.

DECODED. `l13_belial.gd` lines 4–49 require a grounded Human within 125, facing source point (−5482, 4, −155), after all actors 21–39 are dead. Completion writes the player to (−2974, −1108, −2680) and `rotation.y` of −PI/2. Poison subtracts 1 health every 2 seconds. `player_starting_magic.gd` lines 148–164 cure it with Healing at charge 3, even at full health, debit 3 mana, and add 6 health up to 30. The r15 row now reads flag `0x0004` as direct relocation and leaves the `0x0293` record's motion unestablished. The r13 sentence left those command semantics UNKNOWN. This pass did not enter the command. Heading 4000 was not re-derived into −PI/2.

HINTBOOK lines 4166–4174. Wait for the scene, then cast a third-level healing spell against poison. Lines 531–533 name Heal 3 "Poison Cure" and say it shields against poison for a time. BRADY lines 8013–8015, printed page 195. The web opens onto a meeting with a Hive Lord. "Belial's spawn" and "Hive Lord" stay separate. BRADY line 4654, printed page 110, says a Level 2 healing spell in the cavern fight. BRADY line 1723, printed page 47, names Level 3 Poison Shield. Lines 1955–1960, printed page 52, say that shield stays up for 30 seconds. Those sentences do not replace each other. The 1-health tick, the permanent clear, cost 3, and the 6-point heal stay the adapter. Boss health stays outside this entry.

## Grade

DECODED for the host stores and clocks named above. HINTBOOK for lines 226, 289, 531–533, 3070–3077, 3137–3157, 3177–3178, 3910–3911, 3962–3991, 3992–4000, 4016, 4060–4072, 4086–4099, 4123–4139, 4153–4174. BRADY for lines 342, 1075, 1556, 1609–1612, 1723, 1955–1960, 3780–3781, 4396–4401, 4453–4481, 4600–4638, 4646–4654, 4691–4708, 7511–7521, 7898–7901, 7939–7940, 7980–8001, 8008–8015, 8029–8030, 8051, 8053, 8526–8527, and 8554–8558, on the printed pages named above. LIKELY stays the three stone rows. No GUESS was added. LONGPLAY was not opened. No frame was named.

The 20261104 simpler build stays. On 0261 the Spark binding does not stay. The click stays. The row 0256 wake does not stay. The asleep hold of row 0307 stays. No printed number replaces 60, 50, 20 units, 2 seconds, 3 seconds, 0.45, 9, 128, 80, 400, 640, or the 1-health tick. No simpler native build replaces the other adapters.

## Still open

The post-arena branch, the 180-to-90 heading join, native door pivots, the Huline trigger, timers 780 and 720, control 91, iris and spire animation, the basin multiplier, the elevator multiplier, groups 6962 and 7088, the corpse counter, native flight, soul and relationship stores, effect 14, the poison packet, flag `0x0004`, and the `0x0293` motion stay unentered. The movies were not opened.
