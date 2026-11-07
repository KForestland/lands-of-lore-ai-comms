# BB01 — Where the LoL1 ending items are placed

The one save still stops. No placement patch was written. This pass did not re-run the chain. The existing run is the BA01 stop:

`STOP BA chain chunk 8 ending: cold script 555 does not place shard 281, cold script 846 does not place Dawn 198, Whole Truth 280 is only the 281+220 merge, load_file still refuses LOLFINAL.TIM, and playEndSequence is not reached`

A faithful patch cannot put shard 281, Whole Truth 280, or Dawn 198 onto that save. Each native create sits behind a played beat this chain has not reached, or it requires the party to already hold the item. Hand-placing the items, or setting flag 578 or flag 586, would skip those beats.

## What was scanned

Decompiled EMC, 60 files, `<owner-media>` (`LEVEL01` through `LEVEL29` `.inf` and `.ini`, plus `ITEM.INF` and `ONETIME.INF`). A hit counts only when the pushes immediately before the syscall are plain numbers and the item type is the last push (stack position 0), which is how ScummVM reads `makeItem`, `giveItem`, `createHandItem`, and `createLevelItem` (`script_lol.cpp`).

ScummVM TIM: ingame opcode 3 is `tlol_giveItem` (`script_lol.cpp`, the ingame table at 0x00). Command layout is length, delay, opcode, then parameters (`script_tim.cpp`). Opcode 0x19 calls that table. All 157 `.TIM` entries in the 132 paks under `<owner-media>` were walked in memory. The only `giveItem` calls are `O01E.PAK` `KING1.TIM` type 185 and `O01A.PAK` `GERIM2.TIM` type 244. Types 198, 220, 280, and 281 are absent. The outro opcode table used for `LOLFINAL.TIM` does not include `giveItem`.

## The three items

| Item | Native create | When it runs |
|---|---|---|
| Shard 281 | `LEVEL28.INF` function 555, words 7110, 7117, and 7124 | Late in the castle dialogue, after the click and wall tests in that function. A cold call does not get there (BA01). |
| Whole Truth 280 | No script create, no TIM give | Only the inventory click that merges properties 281 and 220 (`gui_lol.cpp` `clickedInventorySlot`). |
| Dawn 198 | `LEVEL24.INF` function 846, word 3086 | Only on the path that already finds 198 in the party. |

`ONETIME.INF` only defines them. `setItemProperty` name-string ids are 198 → 16799, 220 → 16743, 280 → 17097, 281 → 16991. Those words do not place an object.

### Shard 281

Function 555 starts at word 6612. The three creates are:

- word 7110 `createLevelItem(281, 0, 0, level 28, block 520, x 128, y 64, flying 0)`
- word 7117 `giveItem(281, 0, 0)`
- word 7124 `createHandItem(281, 0, 0)`

The two tests in front of them choose which one runs. `getItemInHand` returning 0 jumps to the hand create. A nonempty pack jumps to `giveItem`. The floor create is the remaining arm. None of those words is a level-load spawn. BA01 already called function 555 cold, with flags clear, and the count of 281 stayed 0.

### Whole Truth 280

No `.inf`, `.ini`, or `.TIM` creates type 280. `clickedInventorySlot` deletes the hand item and the slot item when one property is 281 and the other is 220, plays `truth.wsa` for 25 frames, and `makeItem(280, 0, 0)` into the slot. The BA01 port records that merge and does not play the movie. The one save holds neither 281 nor 220, so the merge does not run.

Ruby 220, the other half of that merge, is also unplaced on this save. Its creates are all in `LEVEL11.INF`:

- Words 2087 `giveItem(220)` and 2099 `createHandItem(220)`, then flag 284 is set. These words sit before the first ORDR entry (function 1024). `getItemInHand` returning 0 skips them.
- Words 2197 `makeItem(220)` then `giveItemToMonster`, and only while flag 284 is clear and flag 81 is clear.
- Function 45 (ORDR word 6067) returns at once when flag 84 is set. Later, if the hand item's property index is 259, it deletes the hand item and `createHandItem(220)` at word 6349, then sets flag 81 at word 6384. A separate arm `makeItem(259)` and gives that object to a monster. Property 259 is an `ONETIME.INF` definition (name string 16825), not a floor spawn.

Level load does not place 220. A cold enter of level 11 was not run in this pass. The static script has no level-init create of 220.

### Dawn 198

Function 846 starts at word 2920.

- If flag 586 is clear, or flag 312 is set, the function returns at word 2938.
- If the facing is not 2, it returns.
- `checkPartyForItemType(-1, 198, 0)` then a logical `negate`. The arm that does not find 198 sets flag 312 and returns. The arm that finds 198 also sets flag 312, plays the scene, and at word 3086 does `createLevelItem(198, 0, 0, level 29, block 1021, x 128, y 0, flying 8)`.

That is the only create of type 198 in the 60 files. It places another 198 for a party that already holds one. The lack path places nothing.

Flag 586 is set in one place: `LEVEL22.INF` function 145, word 5806, `setGameFlag(586)` with value 1, and only when flag 312 tests clear. Function 145 itself starts behind flag 375 and a long scene. Nothing in the scanned scripts gives 198 before that test. The cold call of 846 in BA01, with flags 586 and 312 clear, returns before the create.

## The outro, and why LOLFINAL.TIM is refused

`ITEM.INF` function 31 is the only `setGameFlag(578)`. It runs when register 0 equals 1024, `getItemPara` case 4 (the property index) equals 280, and monster stat 8 equals 2. That is the fight with the Whole Truth. Forcing the flag is not the fight.

`LEVEL29.INF` function 1028 tests flag 578 at word 1200. A clear flag jumps to word 1227 and skips the outro. A set flag falls through. Both arms of the following compare still reach word 1224 `fadeToBlack` and word 1225 `playEndSequence`.

`olol_playEndSequence` (`script_lol.cpp`) maps hero id -9 / -5 / -1 to outro character 1 / 3 / 2 and calls `showOutro`. `showOutro` (`sequences_lol.cpp`) loads `LOLFINAL.TIM` on the outro opcode table and `LOLFINAL.DIP`. The retail file is present: ENG `FINALE2.PAK`, 5378 bytes, `FORM` / `AVTL`, and the DIP beside it is 819 bytes (BA01). Native code does not refuse the name.

The port refuses it. `load_file` in the BA01 stack returns empty and appends `LOLFINAL.TIM` to `refused` before any file table. The importer reads `DATA/*.PAK` and does not read `DATA/ENG`. `play_end_sequence` in that same patch reads the ENG pak in memory, records the tags, maps the hero, records `quitGame`, and does not call it. The one save never reaches that call. `tests/tim_opening_test.gd` still requires the direct `load_file` refusal, so the refusal stays.

## What would have to be read before a chain patch

A walked castle scene whose own results reach the shard creates in function 555. A native source for ruby 220 that this save can actually enter (the level 11 dialogue or the 259 transform). A native source for Dawn's key that does not already require the key, which these scripts do not contain. Then item function 31 on the monster whose stat 8 is 2. Then an outro opcode table, with the opening `load_file` refusal left in place. Until those exist, the one save stops on the BA01 line.
