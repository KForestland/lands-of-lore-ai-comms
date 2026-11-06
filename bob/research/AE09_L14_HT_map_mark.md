# AE09 L14_HT Huline Temple

Base maps-y 4a32849. Godot was not run. Map.png was not regenerated.

`markers.json` had 27 rows. It now has 45. No game patch.

Brady printed 114 through 120 is the walkthrough. Printed 197 through 203 is the map list. Hintbook chapter 12 is the Prima temple text. Grades stay on the rows below.

| place | really missing? | host or marker | test |
| --- | --- | --- | --- |
| Huline priest body | no | Caretaker corpse p274. Marker added. BRADY+HINTBOOK+DECODED. Prop 187 stays the other corpse. | `l14_priest_slab_earned_test.gd` |
| First altar bowls | no | Bowls p369 and p370. Markers added. HINTBOOK+DECODED. West and east stay unread. | `l14_priest_ritual_earned_test.gd` |
| Balance bowls | no | Scale Tray p405 and p406. Markers added. BRADY+HINTBOOK+DECODED. Bowls stays a different template. | `l14_shard_bowls_earned_test.gd` |
| Healing-pool shard | no | post shard control 71. Marker added. BRADY+HINTBOOK+DECODED. | `l14_post_shard_earned_test.gd` |
| Flute recess | no | Flute Deco m76. Marker added. BRADY+DECODED. The flute item stays row 77. | `l14_flute_slot_earned_test.gd` |
| Life Idol | no | Prop 371. Marker added. DECODED. Goddess of Life0 and the Jkar idol reward stay other names. | `l14_ledge_maze_earned_test.gd` |
| Second and third trial idols | no | Justice Scale p372 and prop 384. Markers added. DECODED. | `l14_tilt_earned_test.gd`, `l14_fire_paths_earned_test.gd` |
| Printed 201 rows | no | Amber 24, Gorgonite 34, Ancients stn 2, MoDScrl 20, HlScrl 50, Cry shard 4, Jkar idol 5. Markers added. BRADY+DECODED. | `l14_item_test.gd` |
| Storm crystal | no | 65a-Storm row 17. Marker added. HINTBOOK+DECODED. | `l14_item_test.gd` |
| Venom Sacs | yes | No L14 row of that name. No patch. | none |
| Death God, Bowl, Bowl 1, Bowl 2 | yes | No placement under those names. No patch. | none |
| Oil Puddle and Oil pit | yes | The two covers stay marked. Those two templates have no placement. No patch. | `l14_flute_slot_earned_test.gd` |
| Library | no | `l14_library.gd`. Special Book stays the pin. Button placement words were not re-read. No patch. | `l14_library_earned_test.gd` |
| Three path doors | no | `l14_trials.gd` movables 88, 89, and 90. Path names stay off those doors. Placement words were not re-read. No patch. | `l14_ledge_maze_earned_test.gd` |
| Tapestry and bedroom | no | `l14_hanging.gd` assembly 124. `l14_bedroom.gd` movables 0 and 1. Stored origins were not re-read. No patch. | `l14_hanging_earned_test.gd`, `l14_bedroom_approach_earned_test.gd` |
| Chalice | world object yes | `l14_chamber_voices.gd` uses a frame rect. No world coordinate. No patch. | `l14_chamber_voices_earned_test.gd` |

Priest's Room, Statuette Room, Chapel, and Kitchen stay room words without templates. Brady point 10 is still three dots, and the two Invisible Doors plus four Sec Cath Dor movables were not split into them. Regions 863 and 4176 still share `020100001c68`, and byte 5 stays unread on both. Prop 170's `020100001c30` byte 5 stays unread.
