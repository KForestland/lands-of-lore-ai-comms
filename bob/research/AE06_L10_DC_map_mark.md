Base maps-y 4a32849. Godot was not run. Map.png was not regenerated.

| place | really missing? | host or marker | test |
| --- | --- | --- | --- |
| narrow stairs | no | No Stair or Entrance template. The walks are fixture routes. No patch. | `l10_catacomb_earned_test.gd`, `l10_blue_earned_test.gd` |
| second catacomb entrance | no | Barrel c176 is already marked. `l10_oil.gd` owns the blast. Xplosion Trigger c62 stays its own name. No patch. | none for a second entrance name |
| fences / boards / Railing | no | Railing c74 (−1316, 2963) h −90, c75 (−408, 3434) h −91, c174 (1589, 2054) h −120. Grade HINTBOOK+BRADY+DECODED. Prima printed 99, Brady printed 208, and template 17 stay three names. | `l10_fence_earned_test.gd` |
| sword globes | no | E Globe rows are already marked. Every globe slot is 96-E Globe. No patch. | none for a sword-globe name |
| Holy Switch | no | Holy Switch c66 (3207, 2319) h 30. Grade HINTBOOK+DECODED. SLAB_AIM is (3207, 2321) h 45. Prima printed 103 names the slab. Brady printed 101 stays on the white-door switch sentence. | `l10_ankh_earned_test.gd` |
| Death Angel / Dragangel | no | Dragangel c150 (−667, 979) h 30. Grade BRADY+DECODED. Brady printed 104, Prima chapter 9, and template 27 stay three names. Region 42 stays (−646, 953). | `l10_progression_test.gd`, `native_host_op197_test.gd` |
| catacomb braziers | no | Bone Brazier p234 (914, 3989) h −150 and p235 (1650, 3014) h −150. Grade HINTBOOK+DECODED. Prima printed 99. Courtyard controls 113 and 114 stay template 42. | `l10_catacomb_earned_test.gd` |
| Bezoar Ring | no | 86-Beozar ring row 33 (−410, 3726) h 35, id `act2:L10_DC:item33`. Grade BRADY+DECODED. Brady printed 104. Greater Bezoar’s Ring stays the Claw slot. | `act2_world_items.gd` places the row |
| Ancient Magic Stones | no | 66-Ancients stn rows 37–39, region 78. Grade DECODED. Brady printed 104 room join is LIKELY and stays off the slot. | `act2_world_items.gd` places the rows |
| Mists of Doom | no | SumScrl rows 34 and 35 are already marked. Brady printed 103 stays its own sentence. HlScrl row 7 stays its own slot. No patch. | none for that scroll name |
| Freeman's gate | no | Control 67 (−127, 1148) h 14 has no Brady number. No new marker. | none |

markers.json had 51 rows. It now has 62. The new rows are the three Railings, Holy Switch c66, Dragangel c150, Bone Braziers p234 and p235, Beozar ring row 33, and Ancients stn rows 37–39. Template 23 has 47 placements. The other baskets stay on `l10_braziers.gd` without a pin. The stair string Stair Step is a texture, and the earned tests walk floors. Freeman's gate stays off the Brady numbers. No game patch.
