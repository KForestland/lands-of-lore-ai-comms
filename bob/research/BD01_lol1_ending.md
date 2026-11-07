# BD01 — LoL1 ending adapter

Method: `AI_COMMS/META_DUCK_METHOD_20261107.md`. The patch is `grok_research/patches/BD01_lol1_ending.diff`. It applies after BA01. Live `~/lol1_godot` stayed master `9987d7e`. No retail bytes were copied into this file or into the repo.

## 1. The problem

The one save `user://lol1_ay_az.json` reaches the White Tower and then stops. Shard 281, the Whole Truth 280, and Dawn 198 stay at count 0. `load_file("LOLFINAL.TIM")` returns empty and records a refusal. The final fight does not start. BA01 and BB01 left it there. This list is the next time-box.

## 2. Main chain

This is the end of LoL1. The player cannot finish the game while the save stops here.

## 3. What the game is trying to do

The assigned intent is the final reveal (the Whole Truth, the Shard, and Dawn), the last fight, and the ending scene. In player terms that is a *reveal*, then the last *threat*, then the outro.

## 4. Player-visible contract

Grade HINTBOOK for the clue-book order. Grade DECODED for the script sites below.

1. The chieftain gives the Ruby of Truth. It is carried. LEVEL11's four creates of type 220 sit behind dialogue this save does not enter. No floor block.
2. Richard, freed by the four figurines and the elixir, gives his ring. The clue book names that ring the Shard of Truth. Function 555's create of 281 stays behind that castle dialogue.
3. Dawn's key is the one handed over in Yvel Woods. The castle level 3 niche is the recovery if it was given away. Function 846 places 198 only when the party already holds 198.
4. Click the Shard on the Ruby. The result is the Whole Truth. `truth.wsa` is 25 frames and is not played.
5. On Scotia, click the Whole Truth on a character portrait while the blue glow is up. That destroys the Nether Mask. She stays in her own form and can be fought. The clue book says the third change, the Executioner Beast, is the form to avoid. L05 leaves that title open.
6. Acceptance in the clue book: Richard is awake, the Whole Truth has been used, and Scotia is defeated in her own form. The outro is `LOLFINAL.TIM`.

This pass scanned the decompile for syscalls 15 `makeItem`, 17 `createLevelItem`, 73 `createHandItem`, and 76 `giveItem` whose item type is 198, 220, 280, or 281. Eight sites, and no create of 280:

- `level11_inf.asm`: giveItem 220, createHandItem 220, makeItem 220, createHandItem 220
- `level24_inf.asm`: createLevelItem 198 (function 846)
- `level28_inf.asm`: createLevelItem 281, giveItem 281, createHandItem 281 (function 555)

Whole Truth 280 stays the inventory click of 281 and 220. TIM files still do not give these types (BB01).

## 5. Exact vs approximate

EXACT: the three walkthrough items and their order, the 281+220 click, flag 578 only while property 280 is in hand, `playEndSequence` as the outro caller, the save staying on level 24 with Michael, Timothy, 41 credits, and flag 347, and `load_file` still refusing `LOLFINAL.TIM`.

APPROXIMATE, and logged: the grants themselves, because the native creates are not reachable from this save. The monster lookup in item function 31 (opcodes -89 and -106) is unread, so no monster is spawned and stat 8 is not read from a live slot. `truth.wsa` is not played. `fadeToBlack` is not ported. The outro opcode table is not run, so the movie is not played. The tags FORM and AVTL are read from the ENG pak in memory.

Flags 586 and 312 stay clear. The castle niche is not used as the first key.

## 6. Options

a. Keep decoding function 555, the level 11 chieftain, and a first create of 198. That is the same hole BA01 and BB01 already named. This pass did not find a new create.

b. Port more of the castle dialogue without a path the one save can enter. That spends the box and still places nothing.

c. A logged adapter that grants 220, 281, and 198 at the walkthrough moments, uses the existing click for 280, records the function 31 result, and lets function 1028 call `playEndSequence`.

Pick: (c). It is the smallest step that lets this one save reach the ending. It is an adapter. It is not a decoded placement.

LEVEL29.INF function 1028, decoded from the INF words: the entry mask at word 1198 is `0xFFFF`. If flag 578 is clear, the `ifNotJmp` at word 1205 goes to word 1227 and does not call `playEndSequence`. If the flag is set, the unread op -69 returns 0 in this port, `0 < 0` is false, and the `ifNotJmp` at word 1220 jumps to word 1224 (`fadeToBlack`) then word 1225 (`playEndSequence`). Word 1226 jumps to 1729, a `popFrame` with no prologue on this function, which would resume at ip 0. The adapter sets `s.ip = -1` after the outro call so that resume does not run. That stop is off unless `ending_stop_after_outro` is set.

## 7. Proof

Headless Godot `4.7.2.stable.flathub.ed1daf0bf`, `DISPLAY` unset, isolated `XDG_DATA_HOME`. The chain exited 0.

`tests/lol1_az_chain_test.gd` on `user://lol1_ay_az.json`:

- `PASS AZ chain hero`
- `PASS AY chain chunk 1` through `PASS AY chain chunk 7`
- `PASS AZ chain chunk 8 tower`
- `PASS adapter carried ruby 220, shard 281, and Dawn key 198, the click made 280, flag 578 is the mask fight, and playEndSequence started while load_file still refuses LOLFINAL.TIM`
- `PASS AZ chain chunk 9 sound`

The cold asserts still run first: script 555 leaves the shard count unchanged, script 846 leaves Dawn's key unchanged, and `load_file("LOLFINAL.TIM")` is empty and refused before the adapter runs. After the adapter the same refusal still holds, Michael maps to outro character 2, the TIM is 5378 bytes with FORM and AVTL, and the DIP is 819 bytes. The save chunk 9 reloads is still level 24, credits 41, ids -1 and 2, flag 347 set.

Entering level 21 still prints `EMC LEVEL21.INF: step limit reached at 53`, then the chunk PASSes. The pre-existing index `1` and `shapeIndex` SCRIPT ERRORs still print, then the chunks PASS.

`tests/lol1_ba_ending_test.gd` printed the same mechanics PASS as BA01. `tests/tim_opening_test.gd` printed `PASS: LOLINTRO runs to its end, the keep starts at 557 facing north, and throne and poisoning each play once`.

## 8. What unparks a native ending

A walked castle scene whose own results reach the shard create in function 555. A level 11 path this save can enter that gives ruby 220. A first create of Dawn's key that does not already require the key. Item function 31 with opcodes -89 and -106 so the monster id is real and stat 8 can be read. An outro opcode table for `LOLFINAL.TIM`, with the opening `load_file` refusal left in place. Until those exist, this adapter is the logged path.
