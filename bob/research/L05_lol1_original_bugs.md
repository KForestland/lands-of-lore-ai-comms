# L05 LoL1 original bugs and fan patches

No Godot was run. The owner rule is that an original bug is fixed in both editions. Classic is `~/lol1_godot`. Enhanced is not started. A fix made in one edition is repeated in the other. Cut content is not in this list.

The March plan is `~/AI_COMMS/LOL1_PATCH_MODULE_PLAN_2026-03-26.md`. The code notes are the ScummVM fork `~/scummvm-lol1-fork`. The one fan patch on disk is `~/lol1-patches/patches/001_string_typos/manifest.json`.

## Confirmed, and named in both places

Dawn's Key is the plan's floppy v1.05 softlock. The plan says v1.22 and the CD already fix it. The CD data this port imports does not include it. A floppy-1.05 tree would. The ScummVM note at `script_lol.cpp` about item 264 is a different sentence: on an unpatched floppy, Vaelan's cube can be equipped as a weapon, and the workaround forces its type to 0. Those two were not merged.

Lora can be kept in the party past the point where she should leave. Meeting Paulson in the Urbish mine with three people then crashes, or cannot add him. `lol.cpp` `addCharacter` drops her items on the current block and frees the slot. `party.gd` says that workaround is not ported.

White Tower level 3. Throwing an item toward the stairs (level 21, destination block 0x3E0) deletes it. `script_lol.cpp` sends that move to level 20, block 0x0247. The port has no combat throw yet, so this path is not reachable.

## Confirmed in ScummVM, not in the March short list

A click one pixel outside the view button could pick up an item and lock the game. `gui_lol.cpp` clips the search to the button. The port's inventory test does not cover that edge.

White Tower monsters can carry sound id 255. The original happens to read silence. A port should treat 255 as no sound. `sprites_lol.cpp`.

Large fireballs read the wrong item-flag field, so their width is usually 63 instead of 256. That is why they fly down a corridor. `items_lol.cpp` keeps 63 on purpose. Changing it to 256 would block the corridor. Both editions keep 63.

A damage target above 3 is treated as a character id and matched to a party slot. `lol.cpp` calls it a script bug and does not name the scene.

Portrait speech can freeze. `lol.cpp` resets the portrait timer when speech ends in that state. The port does not animate speech yet.

French automap labels are shifted two pixels left. `drawMapPage`. English is unchanged.

Some TIM scripts ask for a WSA that is not loaded. `animator_tim.cpp` skips the frame. The port does not run TIM yet.

## Data bugs

"Duble ring" is the retail spelling in English, French, and German. "Nathanial's Key" is the English spelling. Patch 001 writes those four byte replacements into a GOG CD `STARTUP.PAK`. It has not been imported into `lol1_godot`. Both editions show the corrected names. The DOS file and the port each need the change. The plan also names a leading null on the NECROSAP shape string in `level23_inf`. No patch file for that null is in `lol1-patches/patches`.

## Named, and not confirmed

The plan leaves five open, with no root cause: Heal III and IV underhealing, a King Richard dialogue hang, a Castle Cimmeria niche that eats items, Scotia's third form against the Whole Truth, and an endless cave-dweller spawn. They stay open. They are not fixed from the plan's titles alone.

## Not bugs

The plan's shuriken and Jana restores are cut content. The version folders under `lol1-patches/versions` (Talba ring, magic atlas, all-items) were not graded. They are not in the bug list. Official floppy CPU patches are a DOS loader issue. Godot does not carry them.
