# L06b LoL1 Classic plan, after the clue book

No Godot was run. `~/lol1_godot` is still master `9987d7e`, clean, the same commit L06 and P01 through P08 used. L06 is unchanged. Sizes below are GUESS, in lane-days. The owner's three weeks stays the budget named in L06.

`level_scripts.gd` still starts `missing` empty and counts a call only when a playthrough hits the default arm. The static counts in `lol1_story_full.md` are the check used here. Tower and castle files still show 16 to 49 unimplemented names, so the later chunks do not shrink on the strength of that counter. `playCharacterScriptChat`, `moveBlockObjects`, `triggerDoorSwitch`, and `loadTimScript` are the names a chunk will meet first.

Combat, TIM, character select, compass, and sound are still absent, as L02 recorded. This pass did not re-run the ten tests.

## What changed since L06

L06 chunk 7 stopped where the Computer Show text stops, at the burned nests, and gave that chunk five days. U02 keeps that stop as one sentence and adds the clue book's mine through level 16: the Larkhon, the bloodstone, and Paulson. The five-day guess covers the lake through the nests. The rest of the mine is three more days.

L06 chunk 8 had no size, because no ordered source existed. U01 read the Westwood clue book. Chunk 8 can start. The fan page's one-visit elixir mix, the head, and the figurine corners stay unmerged. The build follows the clue book.

L06 has no chunk for Upper Opinwood, Yvel, and the Catwalk. L03 called that LOL1-14 and left it without steps. The clue book walks those places between the mine and the castle: honey, the woods barrier, Sadie's earth powder, Geron, the city fight, and the catwalk down to the dungeons. Chunk 8 depends on them. They get their own chunk, 7b, rather than being folded into the tower.

## Order

1. Save and load. Two days. Unchanged.
2. Hero select. Two days. Unchanged.
3. Combat. Six days. Unchanged. The large-fireball width stays 63. A White Tower sound id of 255 stays silent. Jana, the wraiths, the Larkhon, and Scotia need this chunk before their levels are playable.
4. TIM for LOL1-01, LOL1-02, and LOL1-05. Four days. Unchanged. `loadTimScript` is still an unimplemented name on level 1.
5. Cards LOL1-02 through LOL1-05. Four days. Unchanged. The string spellings Duble ring and Nathanial's Key stay a display fix in this chunk.
6. Party joins through Lora. Four days. Unchanged. The Lora-then-Paulson guard stays here, and it is required when chunk 7 reaches level 16 block 549.
7. Cards LOL1-07 through LOL1-11, now through Paulson on Mines Level 4. Eight days: the old five, plus three for the floors past the nests. The stair rewrite stays in this chunk. `script_lol.cpp` still sends level 21, destination level 21, block `0x3E0` (992) to level 20, block `0x0247` (583).
7b. The clue book path L03 called LOL1-14. Levels 17, 22, 23, 24, and 25. Four days. Honey, the cube on the barrier, earth powder, Geron's key, and the catwalk. Floppy-only Dawn's Key stays outside the plan. Type 198 is still placed by the CD script on level 29 block 1021, which is a recovery call, not a reason to import the floppy item.
8. Cards LOL1-12 and LOL1-13. Six days. Tower levels 18 through 21, then dungeon 26 and castle 27 through 29, in the clue book order. The elixir is mixed on the return visit. Item 281, Shard of truth, is required because the clue book names it. The Whole Truth is type 280. The Computer Show text still never names either item, and that sentence stays.
9. Sound. Two days, after the levels that call it. Unchanged.

The guesses now add to 42 days. L06's earlier total was about five weeks with chunk 8 unsized. The three-week budget still holds only if a later pass finds that `level_scripts.gd` already covers a level. The static counts say it does not cover the tower or the castle.

## Risks

The clue book's printed numbers are map keys. Most stairs pass the destination through script parameters, so a step can name a floor and still have an UNKNOWN arrival block. Building a stair from a printed number would invent a block.

Function 517 on level 16 adds Paulson only after flag tests. Treating that call as unconditional would add him in the wrong room. The cube on block 611 is inside the same function, on a block the markers already use for armor.

The fan page mixes the elixir on the first tower visit and gives figurine corners. The clue book returns to the altar after four ingredients and does not give corners. Implementing either recipe as if both had said it drops the other source.

L05's five open titles stay open. Two of them sit on this chunk: the Cimmeria niche that eats items, and Scotia's third form against the Whole Truth. The clue book says to use the Whole Truth before the Executioner Beast. That is a step. It is not a root cause for the open title.

`moveBlockObjects` is unimplemented, and level 19's static list ranks it first. The chunk 7 rewrite has to be inside that call before tower level 3 is played. A later pass that ports the call without the rewrite brings the eaten-item stair back.

Chunk 8's dialogue is `playCharacterScriptChat`. That name is unimplemented on levels 18 through 29. A walk that only ports `loadNewLevel` and item creates will pass the doors and skip Lyle, Jana, Dawn, Richard, and Scotia.
