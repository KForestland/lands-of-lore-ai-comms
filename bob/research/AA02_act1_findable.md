# Act 1 findable

Grade HINTBOOK for the book steps in `act1_duck.md`. The learning column is a current journal id or a `hint.text` line read in `scripts/lol2` on act3-story a123d3f. No Godot. This pass adds no `JOURNAL_HINTS` row.

## Required path

| Step | How the player learns | Id to add |
| --- | --- | --- |
| 1. Leave the prison, cross the caves, leave the museum with the summon spell. Chapter 5. | The prison and cave conversation scripts were not opened this pass. `museum_scroll_state.gd` names `museum:item16:Summon_Scroll`. No journal id names that spell. | none |
| 2. Cross the thorn doors. The Hive entrance is past the oil pool. hintbook.txt 2286–2294. | `jungle_oil_fire.gd` takes positions from JSON. No stored thorn-door point was read. No `hint.text` in that file. | none. No hosted moment. |
| 3. Hive ravine, spider, mother in the alcove. hintbook.txt 2594–2630. | `hive_interface.gd` shows "E — Take wax" and "E — Examine rune room". `hive_chasm.gd` shows "You climb back out of the gorge." The spider and mother scripts were not opened this pass. | none |
| 4. Village gates, shaman, tavern last, meet Baccata. hintbook.txt 2332–2349. | Journal `gate_closed_before_shalla`. The tavern meeting is the open Bacatta gap in `act1_duck.md`. | none for the meeting. No hosted moment. |
| 5. Do not cross the long monastery bridge as the Beast. Julian wants two wax copies and gives the iron flute. hintbook.txt 2358–2387. | Monastery journal rows on this base are `tavern_after_farewell`, `kelsrick_attacked_then_hut`, and `stones`. The Beast-bridge and wax lines were not opened this pass. | none |
| 6. Summon the Hive elevator with the flute, floor seven, oil, blades, brazier, two wax copies. hintbook.txt 2659–2702. | Journal `hive_flute_at_pit`. The lift, wax, and rune-room lines are the Hive prompts above. The oil slot and blade hall were not opened this pass. | none |
| 7. Dawn's copy, Julian's copy, the Power Orb, the Dark Halls detour. hintbook.txt 2392–2404. | Journal `long_arm_before_passage` is the axe niche. The handoff conversations were not opened this pass. | none |
| 8. Trade the Power Orb, take the gift for Daniel, follow Baccata to the bridge, enter the Savage Jungle. hintbook.txt 2405–2422. | Journal `thohan_sword_broken` names the Power Orb price. The bridge meeting is the same unhosted Bacatta gap. | none |

`jungle_river_drown` stays the river lesson. The eight required steps do not name that river.

## Patch

`tests/act1_findable_test.gd`, registry order 854. It locks the five hosted ids above. It creates no Node. The note count stays 39 until AA04.
