# AD06 map gaps

Base maps-y 4a32849. Each row was checked in `scripts/lol2` and the tests before a marker was added. No game patch was written. Godot was not run. Map.png was not regenerated.

| gap | really missing? | host or patch | test |
| --- | --- | --- | --- |
| L1 south-exit death | no | `cave_entrance_death.gd` control 135 (−1453, 3144) h 83. Marker added. | `cave_entrance_death_test.gd` |
| L1 tunnel giant cockroach | no | `cave_wild_roach.gd` actor 0, definition 5, name ROACH, (177, 10282) h −250. Marker added. | `cave_wild_roach_state_test.gd` |
| L1 Fire Pit giant | yes | No patch. Population actor 44 is definition 4, health 10, at (−155, 14685). | `cave_roach_population.gd` hosts the nest and does not name a giant |
| L3 speaking stone | no | `museum_key_locks.gd` movable 55, 68-SS1, (853, 1919) h 255. Marker added. Picture props 109–125 stay the 2026-10-23 deviation. | `museum_key_locks_live_test.gd` |
| L4 speaking stone | no | `jungle_river_dam.gd` item 72, 136-SS3, (−3811, 3899) h −70. Marker added. | `jungle_river_dam_all_items_test.gd` |
| L4 waterfall crystal | yes | No patch. Shop rows 22 and 23 stay the shop pile at y 3855. | none for the pool click |
| L5 entrance | no | `hive_route.gd` arrival 1 (848, 4447) h 24. Marker added. | `hive_route_test.gd` |
| L5 Shalla | yes | No patch. Actor 20 stays Dawn. | none for a Shalla placement |
| L5 lizard tunnel out | no | `hive_route.gd` region 835 (3057, 5813) floor −235. Marker added. | `hive_small_route_test.gd` |
| L7 iron door | place no, motion yes | Control 84 (−1243, 614) h 750. Marker added. Motion stays the 2026-10-21 deviation. | none for the door motion |
| L7 prism name | no | `dark_halls_items.gd` controls 971 and 975, name 149-Prsmscrl. Markers added. SS6 stays 139-SS6. | `dark_halls_loot_test.gd`, `dark_halls_earned_detour_test.gd` |

Marker counts: L1 37, L3 26, L4 41, L5 15, L7 15.
