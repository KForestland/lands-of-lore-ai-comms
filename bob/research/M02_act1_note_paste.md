# M02 Act 1 notes still missing from SOURCES

No Godot was run. Act 1 hosts were read in `lol2_act1m` at `e3bbf68`. `my_journal.gd` there has the same eight SOURCES rows as before the village notes. Those eighteen `when` ids are already built. None of them is a row in `act1_completeness_duck.md`'s MISSING list. `lol2_act3` `77f63c7` adds `l8_village_hints.gd` and `larkhon_join_tribe`. Those are the K09 village and Larkhon lines, not this list.

A paste row needs a module and a stuck field that were read. The other MISSING beats stay without a note.

## Paste

Ids are proposals. `discover` rejects them until the script is on SOURCES. `enhanced_guard` is never shown.

| id | chars | flag | hint |
| --- | --- | --- | --- |
| `hive_flute_at_pit` | 68 | `hive_elevator` | The lift waits at the bottom of the pit. The iron flute calls it up. |
| `jungle_river_drown` | 92 | `` | The big river by the land bridge pulls me under if I stay in it. The bank is the way across. |

`enhanced_guard` for both: `same note in both editions (grok M02)`.

| id | module | key | stuck when | anchor or hook |
| --- | --- | --- | --- | --- |
| `hive_flute_at_pit` | `hive_elevator.gd` plus `jungle_walkthrough.gd` `use_inventory_item` | `hive_elevator` | `played_flute` is false and `trigger_at_player()` is 282. Fresh state in this tree is `height` `-1579` (`STOPS[7]`), `target` 7, `armed` false. `play_flute` sets `flute_signal` to 1 only when `monastery:item94:Iron_Flute` is carried, and only an armed poll then sets `played_flute`. | Pit lip polygon `(x,z)` `(-2370,-7695)`, `(-2240,-7696)`, `(-2240,-7536)`, `(-2371,-7536)`, with `abs(player.y - 32 - (-235)) <= 48`. That polygon is what returns trigger 282 when the hall trigger was missed. Hook: the poll while trigger 282 and not `played_flute`. |
| `jungle_river_drown` | `liquid_drowning.gd` | none. The clock is `river_drowning_state.gd` on the node (`elapsed`, `dead`). It is not a quest field. `LIMIT` is 15. | `dead` becomes true. Lizard (form 2) is under when the feet are below the surface. Human and beast are under when the head is below it. | Hook `tick` at `set_health(0)` and the feedback `You drowned. R returns to the checkpoint; F9 loads your save.` The water is the polygon from `assets/lol2/generated/liquid/<area>.json` under the feet (`region_at`). No single coordinate. |

## Unmerged

HINTBOOK, duck beat 63: play the flute at the pit and an eight-stop tower rises. DECODED, this tree: the lift starts at the bottom and the flute at trigger 282 sends it toward stop 0. Speed 96 and the one-second poll have no printed source. `lol2_act3` `77f63c7` `hive_elevator_state.gd` still starts at `height` `-235`, `target` 0. Do not paste this note onto that initial.

HINTBOOK, duck beat 33: the Giant Fish eats the player. DECODED: `liquid_drowning.gd` sets health to 0. It does not play a fish. Opcode 2 arm 57 was not entered. No fish note.

The Hive oil slot (`hive_flute_floor.gd`, key `hive_flute_floor`, control 122 at `Vector3(-1834.5, -1617, -6456.5)`, reach 110) is hosted. Before the commit the oil is a walkable floor. That is not a stuck point, so it has no note.

## MISSING beats with no paste

Duck file `act1_completeness_duck.md`. No quest key was read for these, so no anchor is given.

| beat | why there is no row |
| --- | --- |
| 10 | Cave crate stack and the mace grant are unhosted in the duck. |
| 14 | Guard gates and the lever are placements. The three effects are UNKNOWN there. |
| 18 | Bar movables 71–74 are not rendered. |
| 30 | Museum wall switch. Movable 79's open effect is UNKNOWN. |
| 31 | Dragon-picture flight. Blood pickup is a different hosted item and is not this stuck point. |
| 39, 40 | Shrine trap. Rumble, drop, and fire are UNKNOWN. The Museum long-arm drop is a different host and already has `long_arm_before_passage`. |
| 40a, 40b | Statue switch, hidden wall, hidden door. Mechanisms UNKNOWN. |
| 43 | The duck's missing password man is not identified. The den's six notes are already in SOURCES. |
| 49, 66 | `jungle_dawn.gd` has a voice. This pass did not find a rune-copy field to hook. |
| 50 | The cellar hotspot is a different shortcut. No bookcase-strike key was read. |
| 52 | `jungle_kityara.gd` grants by identity. No blade field was read. Daniel's blade note is the K09 village line, not this meeting. |
| 53 | E at Bacatta already sets the HUD to `E — Talk to Bacatta`. No follow stuck field was read. |
| 59 | No spider at the jungle point in the duck's source-id note. |
| 70 | Four-button order. Three locks, no fourth, order UNKNOWN. |
| 73 | Boulder cellar. Floor-break UNKNOWN. |
| 77, 79 | Sliding bookcases and Prism use are not decoded. Museum Prism is a different item. |
| 83, 84 | Crystal crates and the iron door are still scripted pieces in the duck. The dome-window puzzle is a different host. |

`l8_not_initiated` and the other thirteen K09 rows are M01. They are not repeated here.
