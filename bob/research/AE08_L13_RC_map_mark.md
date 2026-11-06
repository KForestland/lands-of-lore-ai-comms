# AE08 L13_RC Ruloi Citadel

Base maps-y 4a32849. Godot was not run. Map.png was not regenerated.

`markers.json` had 38 rows. It now has 48. No game patch.

Brady printed 109 through 114 is the walkthrough. Printed 193 through 196 is the map list. Hintbook chapter 11 is the Prima citadel text. Grades stay on the rows below.

| place | really missing? | host or marker | test |
| --- | --- | --- | --- |
| Orb switch / globe | no | Switch p420. Marker added. BRADY+HINTBOOK+DECODED. The three words stay separate. | `l13_egg_door_earned_test.gd` |
| Central light | no | Green Vent p265. Marker added. Light p364 stays Light. BRADY+HINTBOOK+DECODED. | `l13_basin_earned_test.gd` |
| Basin weapons | no | Rows 145, 146, and 147. Markers added. BRADY+DECODED. Prima names none of the three. | `l13_basin_earned_test.gd` |
| Elevator brain | no | Brain switch p362. Marker added. BRADY+DECODED. Prima's globe stays a different word. | `l13_elevator_earned_test.gd` |
| Hive Lord actor | no | HL1 actor 40. Marker added. DECODED. The editor home stays a second pin. | `l13_altar_earned_test.gd` |
| Web doorway | no | Template 0 control 103. Marker added. DECODED. Web 1 stays controls 84, 107, and 108. | `l13_belial_entry_earned_test.gd` |
| Mandrake Root | no | 116-Mandrake row 53. Marker added. BRADY+DECODED. | `l13_item_test.gd` |
| Venom Sacs | no | 111-Venom sac row 78. Marker added. BRADY+DECODED. | `l13_item_test.gd` |
| Plasma steps | name yes | Cliff climb and the plasma platform stay marked. No template is named Plasma Steps. | `l13_pink_steps_earned_test.gd` |
| Slave Caverns | yes | No region of that name. No patch. | none |
| Second green-pool teleporter | yes | Control 104 is the only teleporter. The forge return is Front Door control 54, already on the forge marker. No patch. | `l13_return_pad_earned_test.gd` |
| Upper-left maiden switch | yes | `l13_prison.gd` uses a screen button. No world coordinate. No patch. | `l13_prison_refusal_earned_test.gd` |
| Iris 2 and Iris 3 | name yes | `l13_eggs.gd` owns assemblies 107 and 108. NOTES name those controls Web 1. No patch. | `l13_eggs_earned_test.gd` |
| Citadel Tar Crystals, Silverleaf, Aloe | yes | No L13 item row uses those names. No patch. | none |
| Count of 19 Ru-Loi | count open | The active list has 20 actors named RULOI. The prison gate checks actors 21 through 39. No patch. | `l13_lower_ruloi_earned_test.gd` |

Force field, globe, and altar stay unmatched template names. Dreamstone template 3 has no L13 item row. The pedestal grant is `l13_altar.gd`. Darkstorm, Dark Sword, and Thohan's Enchanted Sword stay award names on that same host. Region 489 still carries the one `020100001c` body, and byte 5 stays unread. A 2026-11-02 board line calls control 102 Web 1. NOTES call control 102 template 0. Those two names stay unmerged.
