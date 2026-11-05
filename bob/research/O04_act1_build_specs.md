# O04 Ten beats that still block a finished game

No Godot was run. The duck (`act1_completeness_duck.md`) graded r13 plus `TRIAGE_20261103.md` and is stale. This pass read r15 `f6a5aa4` (the play build, clean), act3-story `75597f2` (dirty only in `region_visibility.gd`, not reviewed), and act1m `e3bbf68`. Newest owner file is still `TRIAGE_20261104.md`. Rank is what stops the campaign. Optional loot is not in the ten.

A fix below is safe only when the effect is already in a file. An unread opcode is named and not given a motion.

## The ten

### 1. Larkhon, before the tribe

Owner 23-25-07, Darker Jungle (7238, 2161). His save had `l8_journey` gift recovered, `admitted` false, `temple_visited` false, and no tribe. The triage says the chain is intact and he arrived too early. `054228d` only stops the sleep-expiry softlock. The join-first note is `1c33ac0`, on act3, not on r15.

Native ids, DECODED from the two trees. Actor body `"115"`. Regions 3277 and 3278 stay blocked until the dose is used. A level change of 12 while the dose is unused is refused; level 12 is `L12_CM`. Serum item definition 119. Silverleaf definition 117. Shaman output id `act2:L8_SJ:shaman_amaranth`. Tribe membership is `l8_tribe` phase `complete` or `departed`. `l8_journey_state` rejects `admitted` true unless `temple_visited` is already true and the gift is `recovered` or `returned`.

Trigger. `guidance_for` while the player is not a tribe member and the vapors are not mixed.

Effect. act3 returns journal id `larkhon_join_tribe` in that case, before `larkhon_must_sleep`. The hint text already stored there is: "Only the shaman can make the Larkhon sleep, and he helps his tribe alone. Show Daniel's blade to the village guard first." r15's `guidance_for` has no such branch and falls through to `larkhon_must_sleep`.

Adapter. None new. The branch and the hint row are the act3 edit. Do not add a second serum item.

Earned test. From the existing `act1-end-darker-jungle` save: `visit_temple`, then show Daniel's blade, and assert `admitted` true. With tribe phase still `idle`, near actor 115, the note id is `larkhon_join_tribe` and a level-12 change is refused. After the hosted shaman trade and the chest apply, regions 3277 and 3278 unblock. A save with `admitted` true and `temple_visited` false fails validation.

### 2. No earned arrival in the Dracoid city

H17 points 5 through 8. The later hosts are already on r15: `l10_emperor` opens the tomb, and `l10_silverleaf` grows on props 159 through 170 after the remains and the Dawn bracer exchange, when the bracers are no longer carried. `l8_shore` records the wake-up on selector 5 after `l9_escape`. What is not hosted is an earned save that walks there, and a map-resume F2 start. H17 left the L9 spawn bytes UNKNOWN. They stay unknown.

Trigger. The opcode 2 arm `0x1C` level change that the progression binder already commits. Level 9 loads `dragon_level.tscn`. This pass did not re-read the byte that chooses that level from the savage jungle.

Effect. Do not write a spawn coordinate. Do not add `playtest_starts` rows 5 through 8 until a map resume exists. Points 1 through 4 can be pinned on the darker-jungle scene only.

Adapter. None.

Earned test. The manifest still ends at `act1-end-darker-jungle`. A new row is an earned save with sha256, not a guessed position.

### 3. The ball over the southern dry fountain

H22. Brady 8794–8796: the south fountain's water is on before the arboretum and before the southeast firewall. That is the Act 3 step the book marks required. STORY-068.

Native ids, DECODED. Prop 210, template 5 Floating Chaos Orb, native (440, −10438), height 85, region 9806. It has no events. No command uses u16 210. Prop 96 on the same pad, group 2826, is opcode 1 on u16 56 and 57, opcode 3 identity `0xF40E4E1D`, opcode 9 on 96. Prop 626, the fountain at (−4111, −15457), region 4900, group 40538 stores local 16 `Ice_fountain_trigger`. The water flag is a different object: prop 221, group 5898, stores local 3 `Has_Water_been_started`, then 21 opcode 204s. Opcode 204 was not entered. Prop 602 is the greenhouse fireball and is not this ball.

Trigger. The book's shatter. No spell command was read on prop 210 or prop 96.

Effect. Do not invent one. Do not point the ice-basin store at prop 210.

Adapter. None until a command that removes prop 210 is read.

Earned test, after that read. The shatter sets local 3, and region 4900 is the fountain that changes. The test fails if prop 210 is still eventless.

### 4. Ancient City gates, opcode 14 arm 5

H21. H20 names these as the city-gate stop. Across the act3 JSON set, 478 commands are opcode 14 with byte 4 = 5. `L16_CA` has five. Three match the MIX:

| group | owner | raw head |
| --- | --- | --- |
| 672 | region 2286, kind 12 | `0e20020005000000` then opcode 1 on u16 2 and u16 1, byte 4 = `0x64` |
| 698 | region 2317 | same three commands |
| 3004 | region 4832 | same three commands |

Movable 2 at (2431, −669), region 10581, is the only index-2 object with a kind-2 record. That record's byte +4 is `0x30` and byte +6 is 4. Arm 5 stores `(4 * word at encoded 0x223A8)` into word +8. The word was not read. Opcode 1 was not entered, so `0x64` is not "open."

Trigger. Region entry on 2286, 2317, or 4832.

Effect. Do not add a slide. Do not treat arm 5 as a no-op in a new script, and do not treat it as an open either.

Adapter. None until `0x223A8` and opcode 1 are read.

Earned test. None until that product is known. A test that asserts a door percent would be guessing.

### 5. Kenneth's gates, the part still open

Duck beat 14. Owner reports through 11-03 17-05-51. `cef69bc` and merge `5b57410` host the pool, the flood movie, and lever 67 / gate 71. `79ca69b` hosts the see-through bars. The wall-then-gates order and the two-guard spawn have no commit on either head.

Placements, from the earlier id pass, DECODED. Movable 72 in region 1163, groups 12568 and 12592, opcode 1 on u16 73 and u16 72. Switches 64, 65, 66, and 67 are regions 1178, 1180, 1182, and 1184. Port door 69 and iron gates 70 and 73 are event 0. The spawn's actor ids were not read.

Trigger. The talk that should move the wall, then the gates, then leave a guard and spawn two more. That order was not entered.

Effect. Do not restage lever 67. Do not invent two actors.

Adapter. None until the spawn group is read.

Earned test. The existing gate-71 path still opens. A second assertion, that two new guards exist after the talk, waits on the unread group and fails closed until then.

### 6. Cave crates and the mace

Duck beat 10. H16. HINTBOOK 2033–2048: stack the boxes, take the mace, use it on the roaches, do not keep it. The owner clipped the wall. An earned Act 1 save exists, so this room is not the only way out of the act. It is the book's way through the fire room, and the push is still absent.

DECODED. Controls 94 and 95, small crates, region 1085. Controls 96, 97, 112, and 122, medium crates, region 1087. Control 121, medium crate, region 1081. All height −215, no events. No opcode 18 in `L1_DC` targets these seven. Two records of dword `0x8FCB4F6D` sit at height −130: file 7323635 (417, 12444) region 1092, and file 7323746 (471, 12480) region 1099. Actors 33 and 34 stand on the cluster. The push is not a command in this file.

Trigger. None stored.

Effect. Do not add a drag. Do not turn the crates into a stair.

Adapter. A drag host is new work, and it waits on the motion bytes.

Earned test. None that passes today. The test that belongs here is: after a read push, control 121 can change region, the height −130 record can be taken once, and the mace is not still carried at the cave exit.

### 7. The password man

Duck beat 43. Owner 17-33-29: he is not there, so the play stopped. HINTBOOK grades the password, the thief, and the unpaid take as optional. Those two sentences stay separate.

DECODED for what is placed. Control 123, Confidante, region 3405, is not that man. Region 3642 is the den and is a different room. No L4 actor def is thief, mauri, or password. The den rooms are `b052a4b`. The journal line `a5346bf` names the armorer's glen and does not place the man.

Trigger. None read.

Effect. Do not spawn an actor.

Adapter. None.

Earned test. The hosted confidante can still set the password note, and the den still opens, with no new man in the village. That test guards the optional path. It does not claim the book stops the game here.

### 8. Museum wall switch

Duck beat 30. Owner 17-09-20. The player guide does not describe this switch (the earlier book pass left it UNKNOWN). Leaving the museum on r15 is the dragon picture, commit `91db679`. That commit is not an ancestor of act3.

DECODED. Movable 79, region 1464. Kind-4 groups 12488 and 12512 do not name door lid 52. Movable 52 is the door lid at (−1882, 1019), region 1475. Dragon door 82, region 760, has no `020100001c` in its own groups.

Trigger. Use of movable 79.

Effect. Do not opcode-1 door 52 from this switch. The open was not read.

Adapter. On act3 only, the r15 dragon-travel commit is the hosted south exit. Do not write a second travel. The wall switch stays unread on both trees.

Earned test. On r15, the dragon click still changes level. A test that movable 79 opens lid 52 fails until a command names that lid.

### 9. Hive flute lift, story tree only

Duck beat 63. HINTBOOK 2665–2668: the flute calls the pit elevator. r15 `f6a5aa4` waits at the bottom and plays the flute on the return. act1m `e3bbf68` is that commit's twin. Neither hash is an ancestor of act3 `75597f2`, so the story tree still starts the lift wrong.

Trigger and effect. The ones already in `f6a5aa4`. This pass did not reopen that diff.

Adapter. Bring that commit onto the story tree. Do not write a second lift. The second whistle (hintbook 2699–2700) stays unhosted on both and is not this row.

Earned test. The hive-return test that r15 already runs, on act3, with the lift at the bottom before the flute.

### 10. Dragon picture, story tree only

Duck beat 31. The click that flies south is r15 `91db679`. Dragon's blood pickup was already hosted in the duck. act3 does not contain `91db679`. Native door 82 still has no level-change bytes (row 8).

Trigger. Use of the picture the r15 commit already binds.

Effect. The travel in that commit. Do not invent a `020100001c` the door groups do not store.

Adapter. Bring `91db679` onto the story tree.

Earned test. That commit's travel test, on act3. Blood pickup stays a separate assertion and already passes.

## Not in this ten

These duck rows are optional, or the play build already hosts them. They are not specs.

| beat | why it is out |
| --- | --- |
| 49, 66 | Dawn's handoff and the Power Orb are hosted on both trees. Actor 63, group 29704 sets `Gave_Dawn_Runes`. `MOFF_EXIT_ORB` grants `monastery:item83:Power_Orb`. The prompt is `7cd6348`. Brady's charm and the hintbook's orb stay two gifts. |
| 52 | The owner confirmed the knife on r14. `l8_journey` offers Daniel's blade. |
| 53 | The 23-03-14 sequence worked on r14. His leaving after the film is act3 `db5efe5` only. |
| 18, 33, 39, 40, 40a, 40b, 59 | H15, H14, H03, H04, H05, H07 grade them optional, or not the required fight. |
| 50, 70, 77, 79, 83, 84 | The Halls are not required (Brady 3343–3346). Four buttons are loot (H01). The cellar hotspot already enters the Halls. Prism makes the end harder and the hintbook says it is still possible (H11). |
| 73 | The wax copies are the hosted hive route (duck beat 65). The boulder floor-break stays unread. Do not add a smash. |
| 63, 31 on r15 | Hosted. Rows 9 and 10 are the story tree only. |
