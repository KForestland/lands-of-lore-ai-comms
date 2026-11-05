# M01 K09 notes, paste spec

No Godot was run. Read at `lol2_act3` `77f63c7`. These ids are proposals. They are not in `JOURNAL_HINTS`, and `MyJournal.discover` rejects an id until its script is on `my_journal.gd` `SOURCES`. `enhanced_guard` is never shown. Each hint is the K09 line, copied, and each count below was rechecked on that string alone. Classic and Enhanced show the same note. Do not reuse `l8_blade_for_daniel`, `l8_see_temple_first`, `l8_show_guard_blade`, or `l8_shaman_cemetery_mark`.

Out of this list: the dry fountain (prop 210), the yellow figure, and the finale lines (caverns, Baccata, bars, heads, Dawn's curse). No host is invented for them.

Village poll shape, for the lead to paste beside each hook: once a second, if the stuck test below is true, `MyJournal.discover(host, id)`. Quest state is not changed. `NEAR` 420 belongs only to `l8_village_hints.gd`. The radii below are the ones in each host.

## Paste rows

`flag` is the quest key the stuck test reads. Dreamstone, the statue, and the Emperor door each have one id and two hooks.

| id | chars | flag | hint |
| --- | --- | --- | --- |
| `l10_tomb_oil` | 109 | `l10_oil` | The tomb oil will not take a weak spark up close. A stronger spark, or dragon's blood, needs a safe distance. |
| `l10_emperor_door` | 92 | `l10_priest` | The priest's urn, the chapel ashes, and the ankh are what the Emperor's door is waiting for. |
| `l9_statue_human` | 97 | `l9_statue` | The walking statue keeps me only if I follow as a man. The dampen spell is what holds that shape. |
| `l9_flood_late` | 118 | `l9_flood` | If I am late for the lifting table, the water wins and I must try the bowl again. At the end I can stand on the grate. |
| `l10_trees_need_dawn` | 107 | `l10_silverleaf` | Dawn on the river wants the bracers from the ruins. While I still carry them, the cemetery trees stay dead. |
| `l8_not_initiated` | 111 | `l8_tribe` | The tribe's fight, and a silver leaf still in my pack, are what the shaman asks before he calls me one of them. |
| `l13_citadel_sealed` | 112 | `l13_egg_door` | Something in the citadel is still sealed. A charged globe, then the upper halls, stand between me and the stone. |
| `l13_dreamstone` | 106 | `l13_exit_lock` | The Dreamstone is past the Hive Lord. Dawn's lock and the temple door both take it, and both give it back. |
| `l14_scale_bowls` | 100 | `l14_shard_bowls` | The scale in the temple wants both crystal shards, one in each bowl, before the way behind it opens. |
| `l14_boulder_side` | 87 | `l14_trap_route` | The boulder in the centre of that hall kills. The safe way is the strip along the side. |
| `l14_hopper_platform` | 94 | `l14_hopper_platform` | Five hopper bodies belong on the wooden platform. My own weight is not enough to make it rise. |
| `l14_chalice` | 94 | `l14_chamber_voices` | The Chamber of Voices takes the Dreamstone into the chalice, and the stone does not come back. |
| `l16_hourglass_leaf` | 74 | `l16_greenhouse` | If the hourglass only chimes, the glass pyramid still wants a silver leaf. |
| `l16_one_tower` | 100 | `l16_greenhouse` | One tower is open. The other three, and a box that fits a disk, are still between me and the centre. |

`enhanced_guard` for every row: `same note in both editions (grok K09)`.

## Stuck tests

Grades are DECODED from the named script unless a row says HINTBOOK.

| id | module | key | stuck when | anchor or hook |
| --- | --- | --- | --- | --- |
| `l10_tomb_oil` | `l10_oil.gd` node `L10Oil` | `l10_oil` `{"version":1,"burned":false}` and `l10_barrel.phase==2` | not burned, barrel has finished its roll (`phase` 2 means `switch` true and `distance` 1426) | Poll `player.global_position.distance_to(AIM) < 240`. `AIM` is `Vector3(-1443, 12, -3307)`. Event: `ignite(level)`. |
| `l10_emperor_door` | `l10_priest.gd` and `l10_emperor_entry.gd` | `l10_priest.urn_given`, `l10_ankh` slots | door shut, and the urn, the ashes, or the ankh is missing. Door shut: `Ankh.committed(l10_ankh, "emperor:slab66")` is false. Urn missing: `urn_given` false. Ashes missing: `Ankh.committed(l10_ankh, "priest:ashes")` false. Ankh missing: `"act2:L10_DC:priest_ankh"` not carried and not occupying the slab slot. | Priest `AIM` `Vector3(3396, 70, -3010)`, camera distance `<= 140`, facing dot `>= 0.8`. Slab `SLAB_AIM` `Vector3(3207, 45, -2321)`, same reach. Hooks: `speak`, `exchange_ashes`, `L10EmperorEntry.offer`. |
| `l9_statue_human` | `l9_statue.gd` node `L9Statue`, and `l9_statue_walk.gd` | `l9_statue` has no `KEY` const; the string is `l9_statue`. Walk key is `l9_statue_walk`. | `player_form != 0` in the alcove, or at the fight while `arrived` and not `fight_done`. Form 0 is the human gate in both files. | Alcove polygon `(x,z)` `(2609.85,-5979.78)`, `(2513.3,-5971.09)`, `(2506.31,-6000.48)`, `(2609.13,-6011.12)`, and `abs(y-32)<15`. Hook: `enter` refuses `Enter the courtyard alcove as Human.` Walk hook: `begin_fight` returns false while `player_form != 0`. |
| `l9_flood_late` | `l9_flood.gd` node `L9Flood` | `l9_flood` via `l9_flood_state.gd`. Runs only when `l9_statue_walk.fight_done`. | `dead` becomes true. That is `breath >= 15` (`river_drowning_state.gd` `LIMIT`) while submerged. | Hook the line `set_health(0)` / `You drowned. F9 loads your earned save.` No Godot grate node. Source control 82 is at source `(2804, 10762)`, height 530 (`docs/l9-flood-source.md`). That coordinate is not converted here. |
| `l10_trees_need_dawn` | `l10_silverleaf.gd` node `L10Silverleaf` | `l10_silverleaf` `grown == false`, and `dead_bracers_item.gd` `available(carried)` (definition 59) | trees still dead because the bracers are carried | Hook `revisit` when it returns `You can still understand the Emperor with the bracers.` Place is the remains polygon, not a tree radius: player `y` in `[-30, 0]` and `(x,z)` inside `(3154,-1297)`, `(3256,-1297)`, `(3256,-1244)`, `(3154,-1241)`. Remains aim `Vector3(3205, -8, -1285)`. Props 159–170 have no constant positions. |
| `l8_not_initiated` | `l8_tribe.gd` node `L8Tribe` | `l8_tribe.phase == "idle"` | before the bout. Also `l8_journey.admitted` and `l10_silverleaf.grown`. Do not record during `intro`, `fight`, `complete`, or `departed`. Leaf definition 117 is what `offer` accepts; the note still applies when the leaf is not in the pack. | Village `Vector3(676, 32, -4541)` plus `native_translation`, `L8Journey.REACH` 160. Hook: `offer` refuses `Offer the Silverleaf at the Wild Village as Human.` or `Bring Silverleaf from the cemetery after meeting the shaman.` |
| `l13_citadel_sealed` | `l13_egg_door.gd` node `L13EggDoor` | `l13_egg_door.opened == false` | globe not charged | Event: `light(level)` while `opened` is false. `AIM` `Vector3(-3254, 43.5, 5330)`. The spark body is a sphere of radius 24. This file has no walk radius. `light` accepts levels 1 and 3 only, and only in form 0. |
| `l13_dreamstone` | `l13_exit_lock.gd` and `l8_temple_door.gd` | `l13_exit_lock` and `l8_temple_door` | `can_leave()` is false at that lock. `can_leave` is unlocked, slot occupied empty, and `stone` still carried. Definition 136. Both locks give the stone back. | Exit slot `Vector3(-3391, 70, 6670)`, camera distance `< 170`, facing dot `> 0.85`. Temple `POINT` `Vector3(758, 32, 2046)`, same reach. Hooks: `interact` on each. One id, two calls. |
| `l14_scale_bowls` | `l14_shard_bowls.gd` node `L14ShardBowls` | `l14_shard_bowls` | `complete` is false, and `"act2:L14_HT:post_shard"` or `"act2:L14_HT:item67"` is still carried. `complete` is slots `"405"` and `"406"` both committed. | Bowl 405 `Vector3(1176, 48, -3307)`, bowl 406 `Vector3(1181, 48, -3601)`. Camera distance `< 145`, facing dot `> 0.9`. Hook: `offer`, or the `E — Place green shard` hint. |
| `l14_boulder_side` | `l14_trap_route.gd` node `L14TrapRoute` | `l14_trap_route` | centre strip kills. `triggered`, `elapsed` in `[0.75, 1.5]`, `abs(x-29)<62`, `abs(z-1136)<55`, feet `p.y-32` in `[130, 180]`. | Hook `set_health(0)` / `The boulder crushes you. F9 loads your earned save.` The kill box is the anchor. Side doors, the safe way in this file: 81 at `Vector3(-62, 180, -413)`, then 80 at `Vector3(-51, 180, 580)`, camera distance `<= 130`, facing dot `>= 0.9`. `open_door("80")` refuses `Follow the side passage.` until 81 is open. This is not the Hive boulder and not cave prop 1333. |
| `l14_hopper_platform` | `l14_hopper_platform.gd` node `L14HopperPlatform` | `l14_hopper_platform` | `complete` is false: one of slots `"91"` through `"95"` is not committed. | `POINT` `Vector3(41, 310, 5919)`, camera distance `< 145`, facing dot `> 0.86`. Hook: `place` refuses `The platform needs a defeated hopper's body.` or `Approach the wooden platform from its side.` |
| `l14_chalice` | `l14_chamber_voices.gd` node `L14ChamberVoices` | `l14_chamber_voices.offered == false` | stone still carried (`act2:L13_RC:dreamstone` or definition 136) and the room is open or the door will open it. `offered` is the only saved flag. `inside` is not saved. | Doors `Vector3(688, 40, 10873)` and `Vector3(638, 40, 10752)`, camera distance `< 130`, facing dot `> 0.7`, and actor `"90"` health `<= 0`. Hook: `open_room` or `offer` before `offered` is set. While Belial lives the door says the chamber stays sealed; that is a different line. |
| `l16_hourglass_leaf` | `l16_greenhouse.gd` node `L16Greenhouse` | `l16_greenhouse.silverleaf == ""` | the chime. `use_hourglass` returns `The hourglass chimes and ticks for a while.` when `silverleaf` is empty or `fireball > 0`. The stuck arm is the empty leaf. | Hourglass `Vector3(2293, 75, -1070)`, `aimed` reach 130, facing dot `> 0.9`. Plate, where the leaf goes: `Vector3(2287, 34, -593)`, reach 150. Item definition 117. |
| `l16_one_tower` | `l16_greenhouse.gd` only | `l16_greenhouse.opened == true` | this tower's doors have opened. The other three towers and the disk box are not fields in this file. No `l16` script names them. | Hook the frame that sets `opened` true (`The fireball strikes the tower doors and they open.`). Arrival point `BALL_END` `Vector3(2290, 18, -2951)`. Door movables 92, 93, 94 have no coordinates here. Do not invent the other towers. |

## Oil, unmerged

HINTBOOK, the K09 line: a weak spark up close does not light the oil, and a stronger spark or dragon's blood needs a safe distance.

DECODED, `ignite`: levels other than 1, 3, and 5 return false before any distance test. Levels 1, 3, and 5 burn the oil whenever `phase==2` and it is not already burned, then, if the player is inside 240 and not protected, health drops by `BLAST_DAMAGE` 20. There is no branch that refuses a close spark. The note uses the hosted fields. It does not add a refuse the file does not have.

## `stuck_id` shape

Same shape as `l8_village_hints.gd`. One function is not enough, because these keys live on different maps. Each host can call `discover` when its row's test is true.

```gdscript
# spec only — not applied
static func stuck_id(quests: Dictionary, place: String) -> String:
	var oil: Dictionary = quests.get("l10_oil", {})
	var barrel: Dictionary = quests.get("l10_barrel", {})
	if place == "l10_oil" and oil.get("burned", false) == false and int(barrel.get("phase", 0)) == 2:
		return "l10_tomb_oil"
	return ""
```

The other thirteen tests are the table. `place` is the host name, not a new quest field.
