# AE05 L9_DR Dracoid Ruins

Base maps-y 4a32849. Godot was not run. Map.png was not regenerated.

`markers.json` had 51 rows. It now has 53.

| place | really missing? | host or marker | test |
| --- | --- | --- | --- |
| Dracoid Hotel | yes | No script string uses hotel. | none |
| path to the priest's body | yes as an object | Point 11 pyre marker stays. The path has no object. | none for the path |
| teleport chambers 4 and 7 | no | Markers m65 and palace teleport c154 stay. Region 2299 goes to L10 selector 2. Region 2301 goes to L8 selector 6. Sketch numbers stay unsplit. | `l9_bridge_earned_test.gd` covers the bridge door, not the sketch numbers |
| stairs orb and force field | yes as those names | `l9_tower.gd` lights props 1087, 1088, 1089, and 1090. The green-orb marker stays. No stair template. No forcefield placement. | `l9_tower_upper_earned_test.gd` |
| basement inset | yes as a measured room | Gauntlets row 53 stays at height -110. | none |
| Gorgonite Nodules | yes on L9 | No L9 item row uses that name. | none |
| left bowl | no | Prop 2622 (2480, 5913) h -5. Grade HINTBOOK+DECODED. Marker added. | `l9_statue_earned_test.gd` |
| flood table | no | Control 122, template 19, (2440, 9260) h 0. Grade BRADY+HINTBOOK+DECODED. Marker added. Control 121 is (2433, 8630) and has no host. | `l9_flood_escape_earned_test.gd` |
| wooden platform | yes as that name | Control 82, template 123, (2804, 10762) h 530. `l9_escape.gd` calls it a raft. | `l9_flood_escape_earned_test.gd` |
| wooden grate | yes as that name | Same control 82. The host name is raft. | `l9_flood_escape_earned_test.gd` |
| railing | no | `l9_noble_rails.gd` controls 478 (889, 5573) h 125, 479 (389, 5573) h 125, 480 (639, 5573) h 125. No marker uses the book word. | `l9_chapel_earned_test.gd` |
| bridge Dragon's Orb | no | `l9_magic_bridge.gd` prop 2648 (-1193, 1943) h 0. The bridge marker stays on controls 466 and 467. | `l9_bridge_earned_test.gd` |

The Dracoid Hotel has no host string. The priest path has no object. Sketch numbers 4 and 7 are unsplit. The stair sentence, the force-field sentence, and the basement inset have no separate placement. Gorgonite has no L9 row. Control 121 has no host. Brady printed 183 names a wooden platform. Prima printed 115 names a wooden grate. Control 82's host name is raft. Prima's railing word and the Noble rail template are separate strings. Prop 2648 is the bridge orb. Controls 466 and 467 are the bridge marker. No patch.
