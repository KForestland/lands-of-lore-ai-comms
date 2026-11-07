# LoL1 rendered tests

Godot `4.7.2.stable.flathub.ed1daf0bf` on private Xvfb `:97` (`1280x720x24`). No `--headless`. The display was not `:0` or `:1`. The renderer was llvmpipe. Each process exited 0. None printed `5 resources still in use`.

The scratch was `/tmp/ay-lol1`, master `9987d7e` plus the ten LoL1 diffs and the AY02 edits. The live tree was not edited. The scratch was removed after the run. The tests wrote `tmp/party_screen.png`, `tmp/portraits.png`, `tmp/northland_arrival.png`, and `tmp/item_view.png` in that scratch.

`party_test.gd` printed: `PASS: four heroes from kLoLCharacterDefs with their starting gear and portrait panels`

`script_walk_test.gd` printed: `PASS: Gladstone scripts ran; the guard stepped aside (525 -> 524); inner door opened; entrance guard blocks the way out; gate script took the party to level 2 block 106 facing south`

`items_test.gd` printed: `PASS: 285 item types from ONETIME.INF; 4 items placed by the level scripts; view saved from block 168 facing 0`
