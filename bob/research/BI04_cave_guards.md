# BI04 cave guards — native talk outcome

Research only. No patch. A change to who dies, or to the wall/switch order, is a mechanics question for the owner.

## Duck

1. Two F10 notes on r18, 2026-11-08. At (1366,-12223) the figure is gone and the HUD says "Guard defeated." At (40,-16654) the caged guard is gone after the talk, and the wall comes down, then the switch at the bridge.
2. The cell talk is on the way to the bridge and the Draracle. The orc is the side chamber next to the locked dishes room. Neither vanish blocks a door the bytes leave shut.
3. The orc speech is a reveal, and he dies before the gift. The cell speech is a reveal, and the wall then opens the way. The bridge lever next to the bridge is a separate pull.
4. Orc: walk up, talk, he speaks, he is gone. Cell: see the guard through the bars, the speech plays, the slab drops in front of the bars, the guard sprite is removed when that slab arrives, and the bridge-row switch starts in the same end group. Lever 67 / gate 71 is not in that group.
5. Exact: the orc clears, the cell sprite hides on the wall callback, opcode-1 order inside group 4376, lever 67 stays a player use. Approximate: movie framing and how fast the travels look.
6. No new adapter. The host already runs these groups. Keeping either figure, or moving the switch into a later group, would invent a mechanic.
7. No new walk. The proof is the groups plus the longplay frames named below. The longplay route did not play the orc conversation.

## Pose (1366,-12223) — old orc, control 136

Map pair is Godot X/Z with `native_translation` removed. Native point (1366, 12223). Control 136, static slot 20, stored (1452, 12257), port z -12257. Planar distance 92. Camera yaw -1.385 and pitch -0.105 look at that anchor (dot about 0.98). Actor 53, the nearest GGUARD, is behind the camera.

HINTBOOK lines 2041-2046: an old orc speaks of a gift and dies before he leads you to it. Grade HINTBOOK.

DECODED, `scripts/lol2/cave_old_orc_source.json`, L1_DC.MIX sha256 6384ec4d4d78f1aadfc1f154d924e1e20636af037cf5af68fe35af8478854345. Kind-4 group 10932 (owner state 4) sets local 3 to 1, starts segment 5, and sets state 6. Kind-6 group 10978 (local 3 == 1) then runs opcode 8 byte 4 = 1 (clear the movie) and opcode 16 byte 4 = 7 (state 7, gone). A hit does the same clear: kind-9 group 11068 when local 51 is 0, group 11004 when local 51 is 1. He does not stay and he does not walk off.

LONGPLAY: `longplay_deep/cave/REFERENCE.md` says this route never plays the conversation. The seated figure at 10:47-10:58 was not confirmed as him. No death frame is cited.

The words "Guard defeated." are not in these groups. They are printed only by `scripted_creature_population.gd` `receive_damage` when a definition 1 or 2 actor reaches health 0. A sword hit is 8 points (`player_form_rules.gd`) against 140 or 150 health, so that sentence is a killing blow. Left click on a population body always strikes, because `peaceful_actor` returns false. That combat rule is not this talk, and it is not changed here.

## Pose (40,-16654) — cell guard, prop 456

Native (40, 16654). Prop 456, template Kenneth Speech, stored (158, 16640). The red-tabard figure is that movie, not actor health.

LONGPLAY f_00147 (12:10) and f_00153 (12:40): the guard stands behind the spiked bars with the green glow. f_00154 (12:45): a dark slab fills that view and the guard is not visible. The cave reference says the slab drops at 12:42. Grade LONGPLAY for the bars and the slab. Grade DECODED for the hide.

DECODED, `scripts/lol2/cave_guard_sequence_source.json`, same MIX. Control 104 kind 5 value 4 runs group 9994: viewpoint (44, 16667), then opcode 1 byte 0x64 on indexes 73 and 72. That group does not name the wall or a guard. The speech end is prop 456 group 4376, predicate owner state 5. Its opcode 1 byte 0x64 order is 65, 64, 69, 70, then 68, then 66. Opcode 16 in that same group sets 65, 64, and 66 to state 1. Movable 68 is the Port Door at (150, 16648), the wall. Movable 66 is the Switch at (404, 16684), the bridge-row switch whose own groups name 68. Lever 67 and gate 71 are not in group 4376. HINTBOOK 2051-2052: pull the lever next to the bridge. That pull stays kind-4 groups 12490 and 12514.

The sprite comes off when the wall arrives. Movable 68 kind 6 value 15 is group 12538: opcode 9 kind 3 target 456 byte 4 = 2 (hide the prop), then opcode 16 sets movable 68 state to 1. No command in 9994, 4376, or 12538 stores actor health. He is not defeated.

Actors 1 and 2 (GGUARD, present false) spawn on region 23, north of the bridge, not on this talk. Stream 0 group 6 is not group 4376.

The order the owner reported matches the bytes: the wall's opcode 1 is before switch 66's opcode 1, in the same end group. The slab is the wall's travel. The switch starts in that group. It does not wait for group 12538.

## Host

`cave_old_orc.gd` already clears on group 10978 and on the hit groups. `cave_guard_encounter_state.gd` already applies 4376 at the speech end and applies 12538 when movable 68 reports value 15, which sets `prop_present` false. No patch.
