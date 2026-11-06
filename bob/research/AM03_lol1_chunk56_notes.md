# AM03 LoL1 chunks 5 and 6

The patches stay unapplied on `~/lol1_godot`. That tree stays master `9987d7e`. `~/opus_work/lol2_act3` stays `stack-ah01` `a04c73a`. Apply order is `grok_research/patches/AM03_lol1_ORDER.md`: AK01, AK02, AL01, AL02, AM01, AM02. `git apply --check --whitespace=nowarn` accepted that order on a scratch copy of `9987d7e`. The scratch copies were removed.

Chunk 5 is the keep, the thugs, Roland, and the poisoning walk. Chunk 4 still owns the TIM flags. Chunk 6 is the party joins. The poisoning call from AL02 still only sets `poisoning_played`.

## Godot

Godot `4.7.2.stable.flathub.ed1daf0bf` ran headless in the scratch copy. The binary was `/var/lib/flatpak/app/org.godotengine.Godot/current/active/files/bin/godot-bin` with `LD_LIBRARY_PATH=~/opus_work/lol2_gameplay_20261014/tmp/godot_host_libs` and `XDG_DATA_HOME=/tmp/am-godot-data`. The scratch symlinked `assets/lol1/generated` to the live tree's imported data. That symlink is not in the diffs.

`keep_cards_test.gd` printed:

```
PASS: the north gate reaches block 106, the return reaches block 589, and the drawn names are Double ring and Nathaniel's Key
```

The same run then printed `WARNING: 34 ObjectDB instances were leaked at exit` and `ERROR: 5 resources still in use at exit`. The test `queue_free`s the walk. The process exit is not clean.

`party_join_test.gd` printed:

```
PASS: Timothy, Baccata, and Lora join in order, and Paulson replaces Lora at level 16 block 0x225
```

A verbose rerun of that test printed `WARNING: 11 ObjectDB instances were leaked at exit` (GDScript resources and RefCounted objects) and `ERROR: 5 resources still in use at exit`.

These already-present tests also printed PASS on the same scratch: `tim_opening_test.gd`, `combat_test.gd`, `hero_select_test.gd`, and `save_roundtrip_test.gd`. Their PASS lines are the ones already in those files. Each walk-scene test also printed `ERROR: 5 resources still in use at exit` and an ObjectDB leak warning (16, 56, and 71 instances for tim, hero, and save). `combat_test.gd` printed two `Nonexistent 'int' constructor` errors from `monsters.gd` `_face_event` and from the character-damage assert, then its PASS line. `monsters.gd` is unchanged in this list. `tim_opening_test.gd` printed three script errors on the reload present (`face_bank` missing on a character dictionary, a monster property index, and `shapeIndex`) and then its PASS line. Hero select and the save round trip printed the monster property and `shapeIndex` errors on present and still printed their PASS lines. This list does not change the character fields stored in the version-1 packet.

`party_test.gd`, `script_walk_test.gd`, and `items_test.gd` each wait on `RenderingServer.frame_post_draw`. Under `--headless` that wait did not finish. No PASS line is claimed for those three. `script_walk_test.gd` reaches that wait after its asserts and before its print.

## Chunk 5

A new game is level 1 block 557 direction 0. `run_level_script(621, 0x41)` with direction 2, then `after_scripts()`, arrives at level 2 block 106 direction 2. DECODED: `level01_inf.asm` `func_621` pushes 2, 106, 2 and calls `loadNewLevel`. `checkMonsterTypeHostility` stays unimplemented and stays in `missing`. The arrival above happened with that call still returning 0.

The return destination is DECODED at `level02_inf.asm` lines 542–546: push 0, push 589, push 1, syscall 60. That load sits before `func_1024` and before the `func_74` label. The labeled `func_74` body does not contain that load. PROBED: `run_level_script(74, 1)` with direction 0, then `after_scripts()`, arrives at level 1 block 589 direction 0. The test calls function 74. It does not require the writ, and type 244 stays absent.

Entering levels 3, 4, 5, and 6 leaves these placements, which `LEVEL*.INI` function 1 creates: Roland's key type 166 at level 4 block 41, the thug key type 167 at level 5 block 165, the lantern type 249 at level 5 block 97, type 245 at level 6 block 168, and rock type 99 at level 5 blocks 195 and 102. Type 245 is absent from level 5. The rock's raw name is Rock. A reload keeps 166, 167, 249, and 245 on those blocks, and type 244 stays absent.

English `lands.json` index 358 stays `Duble ring` and index 436 stays `Nathanial's Key`. The draw path maps those to Double ring and Nathaniel's Key. The hand message uses the mapped spelling. `patched_item_name` maps `Anneau Duble` to `Anneau Double` and `Duble-Ring` to `Double-Ring`. French and German `Nathanial's Key` stay as read. `lang_string` still returns the retail string. Only `LANDS.ENG` is imported.

`LEVEL04` contains ATTACK and BLUFF. `ogre_accepts` is true for bluff and for fight. `ogre_only` stays empty. The ogre block, the required choice, the burnt-scroll type, and the saber were not read.

`createLevelItem` and global var 11 were already implemented, so they were not missing names. No atlas item is added. A placed-item name containing Atlas stays at count 0. `compass_broken` stays 0. The compass widget is still absent. README still lists compass and sound as later work. `playSoundEffect` stays out of `missing`. Every missing name after the gate, the return, and levels 3 through 6 was inside the test's listed set. Dialogue and animation calls in that set stay unimplemented.

## Chunk 6

Syscall 75 is `addRemoveCharacter`. A negative id clears flag bit 0 on the first active character in the first four slots, sets `selected` to 0 when that slot was selected, and leaves the record in the array. A positive id calls `add_character` with the walk's level and block.

`count()` still counts every flag bit 0. `leading_count()` stops at the first clear bit and is the write index. From Michael alone, id 2 adds Timothy: hit points 27 and 27, magic 5 and 5, skills 3, 2, 1, item types 93, 131, 153, 162, face bank `face02`. `script80_runs` stays 0. Clearing Timothy's flag makes `leading_count()` 1. The next add writes slot 1. Id 3 is Baccata: hit points 22, magic 18, skills 1, 1, 3, types 108, 149, 145, 153, 129. `count()` is 2.

Id 4 is Lora. The table's current hit points are 25 and the maximum is 48. Magic is 5. Skills are 1, 4, 1. Types are 137 and 162. The spec's hit points 48 are that maximum. Clearing her flag leaves the record, drops her out of `count()`, and requires no scroll type. The riddle-scroll create was not read.

A packed party of three returns false for id 6 at level 16 block 0x226, and returns false when Lora is in index 1. With Lora in index 2, level 16, and block 0x225, the call returns true, writes Paulson (id 6, face bank `face06`) over index 2, leaves `count()` at 3, and does not append a fourth record. Her two nonzero items are placed with `place_move` at offsets 0, 0 and flying 0. The test set `items.current_level` to 16, so that call used `set_position`, and both items ended on block 0x225 with flying 0. `run_scripts` was false for that call, so the loaded level 1 INF did not run at block 0x225. `script80_runs` stays 0. `add_character` does not call `run_item_script`.

`display_lora_paulson_workaround` becomes true on that success and stays false on the two failures. The message string was not read. The flag is absent from the version-1 save section. The join does not play a face frame. `nextAnimUpdateCountdown` is rolled from 7 through 18. `characterUpdateEvents` is not written by the join.

`play_poisoning_once` sets `poisoning_played`, leaves the party as Michael, and a second call returns false. Baccata is not added there. The tim opening test still finds no Baccata after its own poisoning calls.
