# BA01 — LoL1 ending stop

Method: `AI_COMMS/META_DUCK_METHOD_20261107.md`. The patch is `grok_research/patches/BA01_lol1_ending.diff`. It applies after AZ01. Live `~/lol1_godot` stayed master `9987d7e`. No retail bytes were copied into this file or into the repo.

## 1. The problem

The one save `user://lol1_ay_az.json` reaches the White Tower and then stops. Shard 281, the Whole Truth 280, and Dawn 198 stay at count 0. `load_file("LOLFINAL.TIM")` returns empty and records a refusal. The final fight does not start. This is the AZ01 stop, from 2026-11-07.

## 2. Main chain

This is the end of LoL1. The player cannot finish the game while the save stops here.

## 3. What the game is trying to do

The assigned intent is the final reveal, the fight, and the ending. In player terms that is a *reveal* (the masked form breaks) and then the last *threat*, and then the outro.

## 4. Player-visible contract

Evidence is the original scripts and ScummVM, ahead of the clue book.

Dawn 198 is one `createLevelItem` in the whole decompile, in `LEVEL24.INF` function 846. The body runs only when flag 586 is set and flag 312 is clear. Direction must then be 2. `checkPartyForItemType` looks for property 198. If the party lacks it, the script sets flag 312 and returns. If the party already holds it, the script removes it and places type 198 on level 29 block 1021, flying 8. A fresh game, and this save after entering level 24, have flags 586 and 312 clear, so function 846 returns at its first `popRetOrPos` and places nothing. Level 22 sets flag 586 only when flag 312 is clear. Nothing in the decompile gives 198 before that create. Cold-calling 846 cannot place the key.

Shard 281 is a later `createLevelItem` in `LEVEL28.INF` function 555 (type 281, level 28, block 520), after the hand and `checkInventoryFull` gates. A cold call does not reach it. A probe that treated every rectangle as a hit, and set wall 257 side 0 to 16, still exited through the dialogue calls and queued function 557. `ORDR[557]` is 65535, so that continuation is empty. The shard count stayed 0. Those probe writes are not in the patch.

Whole Truth 280 is not a floor item. `LoLEngine::clickedInventorySlot` deletes properties 281 and 220, either way around, and `makeItem(280, 0, 0)`. The movie is `truth.wsa`, 25 frames. No script creates 280. This save has neither 281 nor 220.

The fight start is item function 31, event register 0 equal to 1024, property 280, on a monster whose stat 8 equals 2. That sets flag 578, deletes the hand item, and reloads the monster shapes. Function 1028 (`0x404`) is the monster-death script. When flag 578 is set it reaches `playEndSequence`. Setting flag 578 by hand is not the fight. This save never sets it.

`LOLFINAL.TIM` is in `DATA/ENG/FINALE2.PAK` (also the FRE and GER paks). The ENG entry is 5378 bytes and starts `FORM` / `AVTL`. `LOLFINAL.DIP` beside it is 819 bytes. `FINALE.EXE` names both files. The port's `load_file` refuses the name before the file table, so the opening chunk cannot play the outro. The importer reads `DATA/*.PAK` and does not read `DATA/ENG`. The refusal is that loader limit. The filename is present. No flag gates the name.

## 5. Exact vs approximate

EXACT: the flag and direction gates on 846, the single create of 198, the 555 create staying behind the castle dialogue, the 281+220 inventory merge, flag 578 as the fight flag, `playEndSequence` as the outro caller, and `load_file` still refusing `LOLFINAL.TIM`.

APPROXIMATE: the 25 frames of `truth.wsa`, and the outro movie. The opening TIM opcode table is not `_timOutroOpcodes`, so this patch does not execute the movie.

Hand-placing 281, 220, or 198, or setting flag 578 or flag 586, would invent the unread castle, ruby, and woods beats. That option was not taken.

## 6. Options

a. Keep decoding function 555 until a real button result reaches the shard create, and find a native source for 220 and for 198 that does not already require 198. That is the castle scene and the ruby give. They are still unread.

b. Port the small exact calls the scripts already name, and leave the one save stopped. `checkRectForMousePointer` uses the mouse and returns 0 while the mouse is off-screen (`mouse_x` and `mouse_y` start at -1). `giveItem`, `checkInventoryFull` (1 only when all 48 slots are empty), and `checkPartyForItemType` match ScummVM. The inventory click merges 281 and 220 into 280 and counts the merge. `playEndSequence` reads `LOLFINAL.TIM` and `LOLFINAL.DIP` from the ENG pak in memory, records FORM/AVTL, maps hero -9/-5/-1 to character 1/3/2, records `quitGame`, and does not call it. `load_file` still refuses the name.

c. Place the three items and set flag 578 so the save prints an ending. That would be a fake walk.

Pick: (b). It is the smallest step that keeps every exact gate and does not invent a placement.

## 7. Proof

Headless Godot `4.7.2.stable.flathub.ed1daf0bf`, `DISPLAY` unset, isolated `XDG_DATA_HOME`. Exit 0.

`tests/lol1_az_chain_test.gd` on `user://lol1_ay_az.json`:

- `PASS AZ chain hero`
- `PASS AY chain chunk 1` through `PASS AY chain chunk 7`
- `PASS AZ chain chunk 8 tower`
- `STOP BA chain chunk 8 ending: cold script 555 does not place shard 281, cold script 846 does not place Dawn 198, Whole Truth 280 is only the 281+220 merge, load_file still refuses LOLFINAL.TIM, and playEndSequence is not reached`
- `PASS AZ chain chunk 9 sound`

Entering level 21 still prints `EMC LEVEL21.INF: step limit reached at 53`, then the chunk PASSes. The pre-existing index `1` and `shapeIndex` SCRIPT ERRORs still print, then the chunks PASS.

`tests/lol1_ba_ending_test.gd` is a separate boot. It does not write the story save. It printed:

`PASS BA ending mechanics: checkRect stays a no-click until the mouse is inside, only an empty pack is full, giveItem and checkParty see property 198, the 281+220 click makes 280, and playEndSequence finds LOLFINAL.TIM in FINALE2.PAK without lifting the load_file refusal`

That run also checked Michael maps to outro character 2, the TIM is 5378 bytes with FORM and AVTL, and the DIP is 819 bytes.

`tests/tim_opening_test.gd` printed `PASS: LOLINTRO runs to its end, the keep starts at 557 facing north, and throne and poisoning each play once`. `load_file("LOLFINAL.TIM")` is still empty and still in `refused`.

## 8. What unparks the ending

A walked castle scene whose own results reach the shard create in function 555, a native source for ruby 220, and a native source for Dawn's key that does not already require the key. Then item function 31 on the monster whose stat 8 is 2, which sets flag 578. Then an outro opcode table for `LOLFINAL.TIM`. Until those exist, this one save stops where the STOP line says.
