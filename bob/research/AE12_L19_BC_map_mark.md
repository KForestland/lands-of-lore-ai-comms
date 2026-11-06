Base maps-y 4a32849. Godot was not run. Map.png was not regenerated.

| place | really missing? | host or marker | test |
| --- | --- | --- | --- |
| Begin | no | Arrival selector 1 (84, −305), grade DECODED. Brady printed 226 point 1 stays off that label. | `l17_level_test.gd`, `l19_map_test.gd` |
| Gateway Room | no | St Belial homes (25, −302) and (9, −304), grade DECODED. The room name stays off them. | none for the room name |
| Statue of Belial / Baccata | no | BELSTAT actor 32 (18, 596) h −10, present false, grade DECODED. Marker added. Brady printed 135 and printed 228 step 1 stay off the label. Prima printed 166 stays off the label. Horn stays Ooze pipe p222 (120, −525). Item rows are 0. | `l19_creature_test.gd` |
| Blood Bowl Room | no | Brady226-11 (88, 1815), grade HINTBOOK+BRADY+DECODED. Prima printed 167 has no coordinate. | none for the fountain count |
| Summoning Chamber | no | Brady226-12 (1583, 3618), grade HINTBOOK+BRADY+DECODED. The arrival label stays unbound. | none |
| skulls and Belial's Imp | no | Skull p67 (1451, 1131), grade HINTBOOK+DECODED. Imp's Home (1241, 1448). Actor 31 IMP_BEL is (1247, 1445) h −120, grade DECODED. The book imp name stays off the home. | `l19_creature_test.gd` |
| golden doors | no | Golden Door (162, 1607) and Golden Door m51 (2550, 854), grade BRADY+DECODED and DECODED. Printed 228 steps 6 and 7 stay one cluster. | none |
| Switches | no | Switch m74 (−323, 2124) h 42, grade DECODED. Brady printed 136 says three. They stay unsplit. | none for the rise |
| Exit to the Birthing Chamber | no | Region 2369 (3321, 875), grade DECODED. Printed 226 point 14 stays off it. | `act2_progression_levels_test.gd` |
| Dawn | no | Dawn homes, Dawn Evil's Home, Dawn good p78, actor 39 (1939, 891), grade DECODED. | `l19_creature_test.gd` |
| Ruby of Truth | yes | No row under L19_BC. No patch. | `l19_item_test.gd` |
| Lizard Path, Pit, Slime Tunnels, Slime Canal, Green Hallway, Elevator, iron door | yes | No template under those names. SEWER and Sewer door stay their own names. No patch. | `l19_creature_test.gd` loads SEWER |

markers.json had 21 rows. It now has 22. The new row is BELSTAT a32. Printed 226 points 3, 4, 6, 7, 8, 10, and 13, the iron door, and a placed ruby have no joined host. Printed 227 has digits and no legend. Prima printed 166 names Baccata, the horn, the bars, the gutter, three switches, a door, the guck, four heads, a fountain, and an elevator, and those sentences have no coordinates. Brady printed 138 names the elevator destination Belial's Birthing Chamber. Printed 235 step 31 names Belial's Laboratory. Both sentences stand. Brady printed 136 names Light Swarmers. The population name is SWARMER. The two names stay unjoined. No game patch.
