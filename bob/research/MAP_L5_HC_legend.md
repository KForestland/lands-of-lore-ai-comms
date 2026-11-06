# MAP-MARK L5_HC

Brady printed 154 is the Hive Caves map, points 1–11. The picture is `MAPS/brady_maps/b-155.png`. Printed 155 is what can happen there: the Executioner, the nest armor, the Hive Warrior, Shalla, the Reaver, the cave-in, and the Amber Cave.

The three flute markers already in `markers.json` were left in place. Nine rows were added. The file had 12 after that pass. AC04 added the Hive Warrior. It now has 13.

Locals are the 41-byte run at file 5981266. Slot 4 is `Lizard_Collapse`, 5 is `Boulder_Fall`, 6 is `Exec_Travel`, 20 is `El_Level`, 25 is `Shalla_cries`. Name-at-index stays LIKELY.

Item rows are the geometry section at file 5787745. Count 27. Offset 158609. Stride 37.

| point | marker | open |
| --- | --- | --- |
| 1 Entrance | not marked | no entrance cstring joined |
| 2 Executioner's Nest | actor 36 (−642, 6462) stores `Exec_Travel`. Regions 839 and 1066 do too. | the nest armor |
| 3 Chasm boulders | region 473 (−1489, 6489), floor −1674, stores `Boulder_Fall` | |
| 4 Lizard tunnel | control 124 (−1119, 6114) stores `Lizard_Collapse` | |
| 5 Lava pool | prop 278 (−189, 6654) stores `Spout_1` | the rock islands |
| 6 Elevator | control 125 (−2640, 7652) stores `El_Level`, beside the existing flute markers | `Elevator_Noise` has no opcode 198 |
| 7 Hive Warrior | actor 33 (−4796, 6374), added in AC04 | |
| 8 Shalla | not marked | local 25 is never stored and never compared in a group |
| 9 Reaver | control 121 (1527, 7529), opcode 3 identity item19 index 17 | the cave-in |
| 10 Amber | six item rows around (437, 5131). Three other deposits were not chosen as the cave. | |
| 11 Lizard tunnel out | not marked | |

Wax runes at (−3031, 6108) and wax at (−3716, 6949) are marked. Brady's rune sentence names the Huline Ruins. These rows are on the hive.

Kind 12 fire time was not entered. No frame was opened. Map.png was not regenerated.

AC04 close: markers.json is 13 rows. Point 7 is marked. Points 1, 8, and 11 stay open. The gap list is grok_research/AC04_L5_HC_map_mark.md.
