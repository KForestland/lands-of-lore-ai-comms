# L02 lol1_godot, one page

No Godot was run. The tree is `~/lol1_godot`, branch `master`, clean. Last commit `9987d7e` (2026-09-26 04:39 +0200), "README: correct the not-yet list". The commit before it, `91cd361`, adds monsters. Nothing has been committed since 26 September. Godot 4.7. Main scene `scenes/lol1/walk.tscn`. Licence GPL-3.0-or-later because the logic is ported from ScummVM Kyra.

## What the tree contains

The README's milestone is Gladstone Keep on foot. Importer `tools/import_lol1.py` reads a DOS CD `DATA` directory into `assets/lol1/generated/`, which is gitignored. That directory is present and has `level01` through `level29`. The view, PLAYFLD frame, smooth step and turn, door timer, EMC level scripts, English text, 285 item types, the inventory bar, the four heroes' portraits, and monster placement plus walk AI are in the scripts. A new game is block 557. The keep gate goes to the Northland Forest.

Still named as missing in the README: combat (attack modes, party attacks, damage), TIM dialogue scenes, the character-selection screen, the compass, and sound. A view click does not yet use the original shape hit test. Calls the EMC port does not implement are logged by name.

## Tests on disk

Ten scripts, none launched this pass:

`view_parity_test.gd`, `walk_smoke_test.gd`, `smooth_scroll_test.gd`, `script_walk_test.gd`, `emc_init_test.gd`, `text_test.gd`, `items_test.gd`, `inventory_test.gd`, `party_test.gd`, `monsters_test.gd`.

The README says the view matches a Python reference on 584 of 584 views. That number is the README's, not a result from today. `items_test.gd` asserts 285 item types. `monsters_test.gd` checks that a Gladstone guard is drawn and blocks a step. There is no save test, no combat test, and no TIM test.
