# AE04 L8_SJ Savage Jungle

Base maps-y 4a32849. Godot was not run. Map.png was not regenerated.

`markers.json` had 32 rows. It now has 34.

| place | really missing? | host or marker | test |
| --- | --- | --- | --- |
| clubhouse | no | Actor 21 definition 1 name WILD, present false, (-1791, -1068) h 0. Marker label stays WILD. Prima's guard stays the host sentence. Doors 51 and 52 are (-1741, -976) and (-1781, -976). | `l8_clubhouse_earned_test.gd` |
| Tuani Hut | yes | No script string uses that name. No marker uses that name. | none |
| Teleport from Dracoid Ruins | no | Marker arrival selector 6 (2063, 2326) stays. `act2_travel.json` region 2301, body `020100001cc8`, destination L8 selector 6, grade PROVEN. | none for point 9 |
| knock-over tree | no | Control 114 (5096, -1916) h 0. Grade BRADY+DECODED. Marker added. Control 116 is (5252, -1908) h 0. | `l8_tree_bridge_test.gd` |
| Crystal Shard | yes on L8 | No L8 item row. `l8_tree.gd` takes `act2:L14_HT:post_shard`. | `l8_tree_room_earned_test.gd` |
| Scroll | yes | No L8 item row uses that name. | none |
| Dracoid Sigil | no | `l8_journey_state.gd` key `l8:shaman:Dracoid_sigil`, definition 102. No placed coordinate. | `l8_journey_state_test.gd` |
| Dampen Charm | yes on L8 | Monastery definition `70-Dampen ch`. Editor marker Cat/Dampen stays. Slot `74-Control tokn` is row 31. | none for an L8 charm row |
| Dagger of the Open Hand | yes | No item row uses that name. | none |
| War Blade | name yes | Excluded dormant row 50 is native (-1465, 2708) height 230. The position array is [-1465, 230, -2708]. The record has no name. The cache marker already cites that cluster. | none |
| Hopper Tunnels | no | Brady175-8 Lamplight sac marker stays under Brady's name. | none |
| shore after the flood | no | `l8_shore.gd` uses arrival selector 5 (-4292, 1623), region 66. Actor 20 is (-4252, 1515) h 0. No new marker. | `l8_shore_earned_test.gd` |
| Lizard Seal | yes on L8 | No L8 item row uses that name. | none |

The Tuani Hut name, the Crystal Shard, the Scroll, the Dagger of the Open Hand, and the Lizard Seal have no L8 placement row. The Dampen Charm is the monastery definition `70-Dampen ch`. Excluded rows 49 and 50 keep cache positions and carry no names in `act2_items_source.json`. The editor label Teleport from Ruins is unbound. Brady printed 99 names the banks of the Bane River. Prima names the Savage Jungle lake on the wet exit. Selector 5 keeps the arrival record. Prima printed 92 says jump the river. Control 114 is Brady's knock-over tree. No patch.
