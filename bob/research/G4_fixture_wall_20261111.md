# G4 fixture points off the OF9 wall

The two cemetery goals that sit against the solid wall at x=-64 are now at x=-85. Z is unchanged. Terrain was not edited.

Sol reproduced both stalls on the inherited route. Departure stopped at player about (-79.05, 32, -363.14) with goal (-68.5, -360.5). The Silverleaf harvest return stopped at about (-79.05, 32, -139.39) with goal (-69, -137). The wall plane is x=-64, normal (-1, 0, 0). The body center cannot reach a goal five units off that plane. x=-85 is west of the stop Sol measured.

`tests/l10_ruins_departure_earned_test.gd` loads `ruins_pit_earned_walk.json` and walks it with physics. Its cemetery points (-68.5, -360.5) and (-69.0, -137.0) are now (-85.0, -360.5) and (-85.0, -137.0).

`tests/l10_silverleaf_growth_earned_test.gd` does not load that file. It walks `l10_silverleaf_return_walk.json`, and Sol's growth case passed. The second stall is `l10_silverleaf_harvest_earned_test.gd`, which walks `l10_silverleaf_harvest_walk.json`. The same goal (-69, -137) there is now (-85, -137).

The rendered walks were not re-run. Another lane's Godot was up, and both tests are full earned physics routes. The goals are the points Fable walked past the wall.
