# AK03 LoL1 chunks 1 and 2: how to run the tests, and what the owner sees

No Godot was run. The patches were not applied to `~/lol1_godot`. That tree stays master `9987d7e`. Apply `grok_research/patches/AK01_lol1_save.diff`, then `grok_research/patches/AK02_lol1_hero_select.diff`. `git apply --check --whitespace=nowarn` accepted that order on a scratch copy of `9987d7e`. The scratch copies were removed.

L06b chunks 1 and 2 are unchanged: save and load, then the four-template screen. The packet is the O05 adapter, version 1. It is not a retail DOS or ScummVM save. No test writes a retail save byte.

## Headless tests

From `~/lol1_godot`, after the two patches, with the imported data already in `assets/lol1/generated`:

```sh
godot --headless --path . --script res://tests/save_roundtrip_test.gd
godot --headless --path . --script res://tests/hero_select_test.gd
```

`party_test.gd` stays the portrait check and is not replaced. Each new test prints its own PASS lines. A missing `playfld.bin` stops the walk scene with the existing "Game data missing" line. These tests were not run here.

`save_roundtrip_test.gd` checks the six O05 cases. A missing file keeps block 557, direction 0, credits 41, brightness 3, lamp oil 0, flags 0, every `vars2` entry `0x100`, inventory types 216, 217, and 218, and the requested hero. The round trip writes flag 10, script var 3, credits, lamp oil, compass, a stepped block facing south, a known item id in the hand and in inventory slot 4, then reads them back, including `next_assigned` and frame `0x8000` on a free slot. Each of the four hero ids reloads as one character. `raceClassSex` stays 0, 0, 2, and 4 on Michael, Conrad, Kieran, and Ak'shel. An unknown id adds nobody. Three `add_character` calls stay three after the load, and the refused id is absent. After the opening ticks, the 30 live monster slots match the saved slots. That load does not call `monsters.reset`. A version other than 1 is rejected. Credits stay 41 and the party stays the new-game hero.

`hero_select_test.gd` checks the five P01 cases. A click in each 32 by 32 box, then accept at (88, 180), stores Ak'shel −9, Michael −1, Kieran −8, or Conrad −5, and runs the new-game items 216, 217, and 218. A click outside the four boxes leaves the index unset. Cancel leaves the party empty and does not make those items. An index outside 0..3 does not call `add_character`. The accepted id survives the chunk 1 packet. The packet has no specialty string. The `hero` export still defaults to Conrad. Setting it to one of the four names adds that hero with no click.

## What the owner sees

Press Play on `scenes/lol1/walk.tscn`. Generated data must already be imported.

When `user://lol1_save.json` is missing, the main scene shows four faces and no fifth. The boxes are (0x060, 0x7F), (0x09A, 0x7F), (0x0D4, 0x7F), and (0x10F, 0x7F), each 32 by 32, in the order Ak'shel, Michael, Kieran, Conrad. The three attribute numbers under each name are the unnamed bytes from `_charPreviews`: 15 8 5, 6 10 15, 8 6 8, and 10 12 10. A click inside a box shows that face and two framed rectangles. Accept is (88, 180), 41 by 15. Cancel is (196, 180), 41 by 15. Accept starts Gladstone at block 557 facing north as that hero, with the three starting items. Cancel returns to the four faces and stores nobody.

The pixels inside each box are the imported `face09`, `face01`, `face08`, and `face05` banks. CHAR.CPS, CHARCHI.CPS, BACKGRND.CPS, ITEMICN.SHP, and CHARGEN.WSA are not in the generated UI set, so this draft does not decode them. The names use the table spelling Ak'shel. The manual spelling Ak' Shel stays a different source and is not stored. FONT9P draws the names and the three numbers. The TIM lines on that screen were not read and are not drawn. KING01, KING02, and KING03 wait for chunk 9. The control that writes selection value 100 was not read and is not in this chunk. The ZH_TWN accept and cancel rectangles are in the hit test and are off unless `zh_twn` is set.

A version-1 file at `user://lol1_save.json` loads on the main scene and skips the screen. Tests do not load that file unless `load_save` is set, so the existing walk tests still start a new game from the `hero` export. A version other than 1 is ignored. On the main scene the selection screen shows. In a test that forced the load, credits stay 41 and the hero stays the new-game export.

There is no new save key. `SaveGame.write_to(path, walk)` writes the adapter JSON. The main scene reads `user://lol1_save.json` on the next start.

The packet stores the live level's 400 item slots, the 1024-length `assigned`, `draw`, and `bdir` chains, the 48 inventory ids, the party, and the 30 monster slots. `bdir` still starts at 5 when a level is begun. Temp monsters for other visited levels were not read and are not in the packet. `visited_levels` is stored. Wall edits are not in the packet. A loaded level attaches its INF and does not run the first-visit script again, and it does not call `monsters.reset` or `make_item(216 + i)`. The level's own `LEVELnn` string file is loaded with it. Specialty words from the walkthrough, the reference, and the manual stay unmerged. No specialty name is stored.
