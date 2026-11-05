# R2 adapter review, rows 0269–0284, 2026-11-05

No Godot was run. No opcode callee was entered. LOLG.DAT was not opened. The longplay was not opened. r15 is `f6a5aa4`. r12y is `56812f9` and has 228 deviation files. These sixteen files are absent there. cmp says r15 only. That is not a match.

`adapter_review_20261103.md` left 0280–0284 in place because the Prima pages were not re-read. `adapter_review_20261104.md` left 0269–0279 in place. `adapter_review_20261105.md` keeps rows 0227–0308 in those reviews. The Hive lift is not in these files and was not reopened. This pass reads the named hosts and the printed sentences. It does not replace those adapters.

## 0269-row-2026-11-03-citadel-sword-altar

Enchant the equipped sword, then take the Dreamstone. Blades 50–68 vanish together after actor 40 dies.

DECODED. `l13_altar.gd` hides movables 50–68 when actor 40 health is at or below 0. E within 170 facing the altar or the pedestal runs `l13_altar_state.gd`. Definitions in `[4, 5, 14, 17, 20, 21, 71]` are admitted. Definition 20 becomes the enchanted Thohan. Every other admitted definition becomes the Dark Sword. `item_defense_data.gd` names 4 Short swd, 5 Fine longswd, 17 Reaver of GO, 20 Tho fixed, 21 Darkstorm, and 71 Tho enchant. Definition 14 was not named here. Handlers 57 and 60 stay unhosted.

HINTBOOK lines 1365–1367 and 4185–4197. Place the sword in use, presumably the fire sword or the repaired broken sword, on the altar before the dreamstone. The result is one Dark Sword. BRADY lines 4780–4787, printed page 112. Only Thohan’s Sword or Firestorm, and each has its own result. Enchant before taking the Dreamstone. Those two sentences disagree with each other. They are not merged. Neither prints E, 170, or the seven-definition list.

The seven-definition admission stays the row’s broader adapter. Printed more faithful is Brady’s pair, or the hintbook’s fire sword and repaired sword. No simpler build replaces the list.

## 0270-row-2026-11-03-citadel-return-pad

A Human jump on control 54, after the stone, moves the player to the entrance pose.

DECODED. `l13_return_pad.gd` accepts a jump inside 45 units, 10 to 90 above the pad, once. It writes `(-3267, 32, 6385)` and yaw `-PI`, then enables curse requests. The native kind-5 and opcode-18 motion stay unreplayed. The foot height 32 is the shared support, not an opcode height.

HINTBOOK line 4197 says make your way back down to Dawn. It prints no pad. Line 4062’s upstairs teleporter is the Ruloi search, not this control. BRADY lines 4794–4795, printed page 113. Find the teleporter in the Great Forge. That sentence is not this jump window. They stay separate.

The jump, the radius, and the latch stay the adapter. No printed number replaces them.

## 0271-row-2026-11-03-citadel-upper-elevator-call

E on the upper landing calls the lowered platform up. The player boards and uses the brain to descend.

DECODED. `l13_elevator.gd` `upper_call_reachable` requires Human, grounded, height `-1040`, still, within 360 of `(-4781, 24, 2981)`, and `y > -60`. `call_upper` starts the existing rise. Speed stays 60. No player teleport.

HINTBOOK lines 4098–4099 say spark the globe to descend. BRADY line 8051, printed page 196, says click the Brain Switch to lower the elevator. Those two descent verbs disagree. Neither is the upper-landing call. Lines 7995–7997 and 8053 remain other switches. The Nov 4 descent note is not reopened.

The upper-call E stays. No printed sentence replaces it.

## 0272-citadel-exit-lock

Place the earned stone, open door 105, and take the stone back before the level change.

DECODED. `l13_exit_lock.gd` uses E within 170. Commit hides door 105 at once and unblocks region 489. `can_leave` requires the slot empty and the same stone carried. `act2_progression.gd` refuses level 12 until that leave check. `native_script_host.gd` stages arm `0x1C` as `0x223C8 = byte 5 & 0x1F` and `0x223CC = (byte 5 & 0xE0) >> 5`. `act2_travel.json` pins `020100001c4c` as level 12, selector 2. Byte 5 is not given a new name. The opcode 3 callee stays unentered.

HINTBOOK lines 4206–4208. Put the dreamstone in the wall slot, then retrieve it. BRADY lines 4797–4798, printed page 113. Click the Dreamstone on the lock, and do not forget to retrieve it. Slot and click stay separate. Neither prints the instant open or the leave guard.

The slot, the instant door, and the leave guard stay. The host’s level-12 / selector-2 map stays.

## 0273-claw-river-rafts

Three rafts follow seven source points in a loop. A standing rider is carried by the platform.

DECODED. `l12_river_rafts.gd` moves ids 50, 51, and 55 through the seven points at `SPEED` 120. Phase is the nearest start. Pause freezes the clock. Boarding is ordinary motion.

HINTBOOK lines 4211–4221. Jump down onto an ice floe and ride. Be Human for the niche jump. BRADY lines 4538–4555, printed pages 107 and 108. Wait for a large floe and ride the circle. Neither prints 120 or the seven coordinates.

Speed, phase, continuous motion, and rider carry stay the adapters.

## 0274-claw-niche-armor

Human Spark 1 or 3 on the niche reveals the dormant chain mail. E takes it and equips it.

DECODED. `l12_niche_armor.gd` reveals identity item 5 at once. E within 155 equips it. `act2_items_catalog.gd` names definition 54, defense 40. The floor-animation join stays unentered.

HINTBOOK lines 4225–4230. Spark the tripod. Obsidian chain mail appears. Put it on. Lines 1539–1541 call it the hidden Claw armor and print no spark. BRADY lines 4557–4558, printed page 108. Cast some light and you may find useful armor. Spark and “some light” are not merged. Neither prints defense 40.

The immediate reveal and the equip stay. No printed number replaces them.

## 0275-claw-raft-bank-jump

A Human sprint jump off a raft near the glacier bank uses a larger launch. Other jumps stay at 200.

DECODED. `l12_river_rafts.gd` `jump_speed` applies only while riding, Human, sprinting, and within 400 of `(3144, -12218)`. Rise uses bank top `-1090`, the foot, and 24 clearance. Travel uses landing `(3190, -12190)` and run speed 144. The launch is the larger of the two ballistic terms. Impulse 200 and gravity 320 still peak at 62.5 elsewhere.

HINTBOOK line 4234. Hop off near the left bank. No form and no impulse. BRADY lines 4560–4561, printed page 108. Leap where the bank is lower. Lines 4563–4564 say a lizard, or wait to become one, for that leap. The lizard sentence is not the Human ballistic. They stay separate.

The enlarged Human launch stays. No printed impulse replaces it.

## 0276-claw-crevasse-form-choice

Spark 1 or 3 opens rock gate 91. E requests Lizard for 60 seconds, or Human, near the entrance or the grotto, if the Dreamstone is carried.

DECODED. `l12_crevasse.gd` opens control 91 with no native timing. `choose_form` calls `request_timed_form(2, 60.0)` or `request_human` within 180 of `(3000, -1058, -13600)` or `(3300, -1078, -14530)`. Handler 28 stays unhosted.

HINTBOOK lines 4236–4239. Turn into the Lizard, crawl the ice tunnel, and change back at will. No 60 seconds and no spark on a gate. BRADY lines 4575–4577, printed page 108, name the grotto and then a sparked body. That body spark is row 0277, not this gate.

The Spark opening and the 60-second choice stay.

## 0277-claw-frozen-blue-bow

Spark on the ice figure shows a modern bow for 3 seconds. It drops 70 units. E catches it, or the figure refreezes.

DECODED. `l12_frozen_bow.gd` uses `WINDOW` 3 and a 70-unit drop. The award is `act2:L12_CM:blue_bow`, definition 35, source name 36-Darkbow, label Blue Bow. The catalog grade says the native same-region item is Shard 31. Index 36 stays unnamed. No pyrapod object was searched.

HINTBOOK lines 1523–1527 and 4240–4245. The glacier bow is the Long Bow Shard, also called the Blue Bow. Melt it with a pyrapod fire spell or a spark, and grab it before it sinks. Lines 1370–1372 are a different Dark Bow, in the City. BRADY lines 1276–1278, printed page 34, name the Great Bow Shard and ice shards. Lines 1286–1293, same page, name a different Dark Bow that drains health. Lines 4578–4581, printed page 108, say spark a body and grab an unnamed artifact. Those names are not merged.

The definition-35 label, the 3 seconds, and the 70-unit drop stay the workaround. No proven bow identity replaces them.

## 0278-claw-return-logs

After the Citadel exit receipt, controls 52–57 return. Floors 914 and 915 lose underside collision. Their tops stay.

DECODED. `l12_glacier.gd` shows those six logs when the exit lock is committed, even if the avalanche has started. `upper_shape.backface_collision` is off only then. Heights are not reset. The native underside walk stays unentered.

HINTBOOK lines 3962–3971 and 4246–4249. Save the log climb for the return, and expect falls. BRADY lines 4566–4569, printed page 108. The wooden logs are the way out, and the jumps can kill. Neither prints a restoration or a one-sided floor.

The six-log restore and the one-sided pair stay.

## 0279-jungle-return-river-jump

After the exit-lock receipt, one Human sprint jump from the low east bank uses a larger launch. Other jumps stay at 200.

DECODED. `darker_jungle.gd` `jump_launch_speed` requires the receipt, a sprint, Human, within 35 of `(5399, 1873.5)`, and foot `y` from `-180` to `-130`. Rise is west floor 0 minus the foot plus 24. Travel uses `(5100, 1880)` and 144. The same two ballistic terms as 0275 are used. `sqrt(640 * rise)` is `sqrt(2 * 320 * rise)`.

HINTBOOK lines 3173–3175, 4263, and 4304–4305. On the way back, jump the jungle river as Human. Lines 4210–4211 are the Claw cave mouth: that jump back cannot be made, so use the floe. Those are different rivers and are not merged. No impulse is printed.

The local ballistic stays. No printed strength replaces it.

## 0280-temple-dreamstone-entry

E at the L8 approach offers the earned stone, retrieves it, and only then uses prop 1198. The same receipt opens L14 doors 92 and 93.

DECODED. `l8_temple_door.gd` is Human E within 170 of `(758, 32, 2046)`. `act2_progression.gd` `use_exit` sets local 13 only when `can_leave` is true, then fires the original exit. `l14_temple_doors.gd` hides movables 92 and 93 on that receipt. The predicate writer stays UNKNOWN. Slot 72 is not this input.

HINTBOOK lines 4304–4308. Use the dreamstone at the temple south of the river, and retrieve it. BRADY lines 4875–4884, printed page 114. Click the Dreamstone above the doors. Use-and-retrieve and click-above-the-doors stay separate. Neither prints local 13, doors 92 and 93, or an immediate open.

The E slot, the local-13 receipt, and the modern door pair stay.

## 0281-temple-priest-carry

E carries corpse 274 to rectangle 816 and lays that same billboard lengthwise.

DECODED. `l14_priest_body.gd` follows the player at 36 forward and 28 down. Place uses the transaction on the world-body id, not an inventory grant. Reach is 150. Slab support is y 2. Corpse 187 is untouched.

HINTBOOK lines 4328–4340. Pick up the priest near the entrance and fit him lengthwise on the low rectangle before the bowls. BRADY lines 4915–4919, printed page 115. Drag the Caretaker onto the raised altar, and lightning incinerates him. Low rectangle and raised-altar lightning are not merged. The Brady lightning is not this place action.

The carry, the follow, and the alignment stay. The native drag join stays unentered.

## 0282-temple-priest-ritual

West aloe and east poison, then a 2-second floor drop, then Spark on the placed body.

DECODED. `l14_priest_ritual.gd` offers item 68 to prop 370 and item 72 to prop 369, only after the body is placed. The host floor map has 22 keys, the row’s unique count. Motion reaches those targets in 2 active seconds. Assemblies 165 and 166 stay at top 2. Spark 1 or 3 after the drop hides billboard 274. The ceiling clip stays the local adapter. Opcode 196 stays unentered.

HINTBOOK lines 4349–4355. Aloe in the western bowl, poison in the eastern bowl, a slow descent, then spark the body. BRADY lines 4910–4913, printed page 115. Aloe in the blue bowl, poison in the red, then the floor lowers. West/east and blue/red are not merged. Brady’s lightning stays on the placement sentence, not on this spark.

The 2-second motion, the bowl order, and the Spark binding stay. No printed duration replaces 2.

## 0283-temple-post-shard

E at control 71 awards one Cryshard. The wooden-post name stays UNKNOWN.

DECODED. `l14_post_shard.gd` uses Human reach 125 and facing at `(3043, 30, -5684)`. One grant, id `act2:L14_HT:post_shard`. The icon is shown until taken. The other commands in the group stay unhosted. Opcode 3 byte +8 stays unentered.

HINTBOOK lines 4375–4377. North of the pews, grab the green shard in a wooden post. BRADY lines 4924–4925, printed page 115. Click the pedestal by the healing pool for a Crystal Shard. Wooden post, Crystal Switch, and pedestal stay three names. The host does not rename the control.

The northern pickup stays the workaround. No printed noun replaces Crystal Switch.

## 0284-jungle-tree-torches-slot

Five Spark hits raise eleven floors in 2 seconds. E at the door face uses the same shard and opens movable 50.

DECODED. `l8_tree.gd` requires five distinct torch hits, levels 1 or 3. The floor map has 11 keys. Rise completes in 2 active seconds. The lit mark is Museum `flame_0`. The slot proxy is `(-1430, 250, -2575)`, reach 170. `l8_tree_slot_state.gd` accepts definition 105 and retrieves that instance. Opcode 9 index 50 stays unentered. `region_blockers.gd` ends ground strip 2417 at ceiling 220, with headroom 0. The lower strip stays blocked.

HINTBOOK lines 3104–3112 and 4353–4365. Spark every torch, climb the new steps, use the shard on the bamboo door, and take it back. BRADY’s torch lines that were opened are other rooms. They are not this tree. No book sentence prints 2 seconds, the door-face proxy, or region 2417.

The Spark counter, the 2-second rise, the door proxy, and the strip cut stay.

## Grade

DECODED for the host stores named above. HINTBOOK for the Claw, jungle-return, temple, and tree sentences. BRADY for printed pages 34, 107, 108, 112, 113, 114, 115, and 196. LONGPLAY was not opened. No frame is graded.

No printed number replaces the reaches, the 60-second form, the 2-second floors, the jump launches, the raft speed, or the bow window. No simpler build replaces these adapters. The seven sword definitions stay the row’s admission. The blue-bow label stays the workaround. The upper-call E stays. The Hive lift stays out of this file.

## Still open

The altar offer dispatcher and sword handlers 57 and 60. The return pad’s kind-5 and opcode-18 motion. The exit lock’s opcode 3 callee, and byte 5 unnamed beyond the host split. Raft opcode 18. The niche floor join. Native jump strength. The crevasse hit binding and handler 28. Opcode 9 index 36, and any pyrapod. Glacier underside selection. Prop 1198’s predicate writer. The priest drag join. Opcode 196 and stacked-ceiling selection. The post’s event 4 to 3 path. The tree’s opcode 207 counter and opcode 9 index 50.
