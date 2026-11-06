Base maps-y 4a32849. Godot was not run. Map.png was not regenerated.

| place | really missing? | host or marker | test |
| --- | --- | --- | --- |
| Arrival elevator | no | Marker Arrival elevator plate c78 (-3848, 1201) h 1. Host `l16_arrival_elevator.gd`. HINTBOOK 4666-4668. BRADY printed 123. Elevator Door is not the template name. | `l16_arrival_elevator_earned_test.gd` |
| Southern dry fountain orb | no | Marker Dry fountain orb p210 (440, -10438) h 85. Host `l16_dry_fountain.gd`. HINTBOOK 4788-4814. BRADY printed 124 is a separate procedure. Prop 602 stays the NE greenhouse Ball O Smoke. Prop 626 stays the fountain marker. | `l16_dry_fountain_test.gd`, `l16_dry_fountain_earned_test.gd` |
| Hourglass | no | Marker Hourglass p627 (2293, 1070) h 45. Host `l16_greenhouse.gd`. HINTBOOK 4873-4894. BRADY printed 125. The host aim point uses Vector3 y 75. | `l16_greenhouse_earned_test.gd` |
| Scarab | no | Marker Scarab item11 (2230, -6116) h 55. Host `act2_world_items.gd`. BRADY printed 132. Label Scarab stays LIKELY. Jeweled was not added. | `l16_item_test.gd` |
| Yellow figure | yes | No host. No patch. | none |
| NW brick, fire, frozen vapor | yes | Props 88, 89, and 90 are placed. NW Ball O Smoke p600 is already marked. HINTBOOK 4824-4834 and BRADY printed 125-126 name different objects. No patch. | none |
| Oil fountain and Dark Bow | yes | Prop 392 is placed at (-2201, -12864). Item row 24 is excluded as dormant at (-2546, -12858). No patch. | none |
| Floorless silverleaf room | yes | Control 75 is the greenhouse plate. No patch. | none |
| Starry Tower, mantle, live dragon | yes | Tower p615 and Telepad c74 are already marked. Prop 241 is (1625, -4417). Mantle props 331, 332, 333, and 348 have no events. No story host. No patch. | none |
| Canal | no | Marker Watergate c123. BRADY printed 219 point 8 says Canal. The control name Cannal has no placement. | none |
| Ivory chips | no | Item rows 12, 22, and 23. Host `act2_world_items.gd`. The room markers already stand. | `l16_item_test.gd` |
| Cavern exits | no | Telepad c74 reads as level 17 selector 1. Region 9822 reads as level 17 selector 3. DECODED. Belial was not written on either marker. | `act2_progression_levels_test.gd` |

The yellow figure has no host. The northwest lists stay separate. The oil spark has no host. Hintbook 4931 names the Dark Bow. Hintbook 4935 names a blue bow. Those two names stay separate. The floorless silverleaf room has no host. The box, the disk, the Starry Tower figure, the mantle walk, and the live-dragon chop have no hosts. `l16_fountain_ball.gd` is not attached. `markers.json` had 24 rows. It now has 28.
