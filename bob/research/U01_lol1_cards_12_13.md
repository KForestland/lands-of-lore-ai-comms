# U01 LoL1 cards 12 and 13

No Godot was run. `~/lol1_godot` is master `9987d7e`, clean. `~/lol1_scripts_decompiled` is absent. The asm used here is the archive copy at `<owner-media>`. Maps are `~/AI_COMMS/MAPS_LOL1/`. Item types are the M04 table. Level English names are the M03 names.

The step source is the Westwood clue book, *Lands of Lore: The Throne of Chaos*, read as the OCR transcript at `https://archive.org/stream/Lands_of_Lore_Cluebook/Lands_of_Lore_Cluebook_djvu.txt`. Grade HINTBOOK. A printed map number in that book is a map key. It is a block id only when a script or a marker names the same block. A garbled OCR word was not used as an id.

A second full text was read: `https://www.kerstins-spieleloesungen.de/loesungen/lands1.htm`. That page is a fan solution. Where it and the clue book differ, both sentences stay. The Computer Show walkthrough in `LoL1_Walkthrough.md` still stops in the mine and only names the tower and Cimmeria. Those three names stay beside the ordered steps. P07 is unchanged.

## Level files

| engine level | English name | area | clue book floor |
| --- | --- | --- | --- |
| 18 | Tower Level 1 | TOWER1 | White Tower level 1 |
| 19 | Tower Sub-level | TOWER1 | White Tower sub-level |
| 20 | Tower Level 2 | TOWER1 | White Tower level 2 |
| 21 | Tower Level 3 | TOWER1 | White Tower level 3 |
| 26 | Dungeons | RUIN | Dungeons under the castle |
| 27 | Castle Level 1 | CIMMERIA | Castle Cimmeria level 1 |
| 28 | Castle Level 2 | CIMMERIA | Castle Cimmeria level 2 |
| 29 | Castle Level 3 | CIMMERIA | Castle Cimmeria level 3 |

The file order puts the sub-level at 19, between tower levels 1 and 2. The clue book visits it after tower level 3, through the ivory key. `LEVEL18.INF` strings include `LYLE` and `JANA`. M03 already says no Jana id exists in `charDefaults`. That stays.

Most stair `loadNewLevel` calls push script parameters, so the destination block is UNKNOWN. Three calls push constants:

- `LEVEL21.INF` function 199 calls `loadNewLevel(20, 199, direction)`. The direction is `getDirection`. Grade LIKELY for the link. The clue book says a pit on tower level 3 drops into the minotaur room on tower level 2. The script does not name a minotaur on block 199. Those two sentences stay.
- `LEVEL24.INF` function 427 calls `loadNewLevel(26, 427, 2)`. M03 already recorded this edge and left it off the walkthrough. The clue book says Vulture's Chasm never stays crossable. The function and the chasm stay unmerged.
- `LEVEL26.INF` function 734 calls `loadNewLevel(23, 857, direction)` after `moveBlockObjects`. Grade LIKELY. Catwalk Caves 1 is level 23. The clue book's catwalk-to-dungeon stair block stays UNKNOWN.

`olol_moveBlockObjects` in `script_lol.cpp` still rewrites level 21, destination level 21, block `0x3E0` (992) to level 20, block `0x0247` (583). That redirect stays the chunk 7 stair fix from P06.

## LOL1-12 White Tower

Grade HINTBOOK for the order. Grade LIKELY for the script calls below, except the ivory key, which the level 21 marker already grades LIKELY because a tainted branch precedes the create.

The clue book order is:

1. On tower level 1, find Lyle. Helping him pays silver. Attacking him leaves a pouch. Leaving him makes him offer the Amber Ring, and a second help gives the ring. A west niche, opened by a north button, also holds the ring.
2. Put the Amber Ring in the niche marked "Ring for Admittance". That opens Jana's room. Defeat Jana. She can drop the great sword Trouble, and a niche holds a mystic key for a lock on tower level 3.
3. On tower level 2, take the fireball scroll and the mystic keys. The minotaur drops the great maul Thunder, dwarvish scale mail, and a minotaur horn. The horn opens the west wall.
4. On tower level 3, a ghost at the stairs warns the party off. Use Vaelan's Cube on the wraiths. The pit past two buttons drops to the minotaur room. The ivory key on this floor opens the sub-level stair on level 1.
5. On the sub-level, put the four roaming items into the four niches. The old woman gives the Crucible of Faith. The blue mystic key from tower level 3 opens her lock.
6. Leave, gather the four elixir ingredients, and return. The ingredients are hornet honey, swamp water, a bloodstone, and earth powder. Place the crucible on the neck of the Altar DeBlanca and put the four ingredients in it.
7. Take the finished elixir to Geron in Yvel. The woods meeting with Scotia, who is wearing Dawn's face, sits between that return and the castle. Giving her Dawn's Key loses the key until Cimmeria level 3. Arguing or fighting her makes her leave after more than half her health, in lizard form, then she flies.

Acceptance for this card, from the clue book: the elixir has been mixed at the altar. Curing Richard and the last fight are the next card.

The fan page puts the elixir mix on the first tower visit, calls the crucible a head, and has Lyle give the ring as the first conversation. Those three sentences stay beside the clue book.

Script checks:

- Amber Ring is type 226. `LEVEL18.INF` function 559 places it on level 18 block 73 and also calls `giveItem` on type 226. Both calls sit behind a wall-type test and an inventory test. The level 18 marker file does not list block 73.
- Ivory Key is type 184. `LEVEL21.INI` function 1 places it on level 21 block 37. The marker file says the same and grades it LIKELY.
- Mystic Key type 192 is placed on level 18 block 548, and type 196 on block 393, both from `LEVEL18.INI` function 1. Type 195 is placed on level 21 block 591 from `LEVEL21.INI` function 1. The level 21 marker lists block 591.
- Minotaur Horn is type 172. `LEVEL20.INI` function 1 calls `makeItem` on it. No block was on that call.
- Crucible of Faith is type 260. No constant `createLevelItem` or `giveItem` names it. `LEVEL18.INF` function 40 compares the item in hand with type 260, sets game flag 347, and changes a wall. The creation block stays UNKNOWN. The fan page's head and this type stay unmerged.
- Vaelan's Cube type 264 is placed by `LEVEL16.INF` function 517 on level 16 block 611, and by `LEVEL26.INF` functions 414 and 834. The woods barrier and the tower wraiths both use a cube in the clue book. Which placement is which cube stays unmerged.

## LOL1-13 Castle Cimmeria

Grade HINTBOOK for the order. The castle steps assume the elixir already exists.

1. Finish the dungeon alliance. The clue book says either the Knowles or the Xeobs. The reward is a key up into the castle, and a cube if that patron has one. Nathanial's Key is in the dungeon.
2. On castle level 1, use the dungeon diamond on the crystal ball that holds Dawn. Take the cobra statuette from the northeast trap, and the dragon figurine from the south niche after the atlas room. The atlas room hides four plates. The centre south corridor of that room is the stair to level 2.
3. On castle level 2, take the unicorn figurine from the niche behind the switch. The noir key and the adder key open further doors. King Richard is in the casket room. The clue book says the four figurines and the elixir free him.
4. On castle level 3, the humanoid figurine is behind the buttons at the sum puzzle. The atlas reads `1 + 1 = 2` when that wall has moved. Dawn's Key is in that niche if it was given away in the woods. The gold key and the silver key open the way on.
5. Place the four pyramid keys on the casket. The names in the clue book are Dawn's, Geron's, Nathaniel's, and Paulson's. Apply the elixir. Richard gives his ring and the clue book names that ring the Shard of Truth.
6. Click the Shard of Truth on the Ruby of Truth. The result is the Whole Truth. On Scotia, click the Whole Truth on a character portrait while the blue glow is up. That destroys the Nether Mask. After that she stays in her own form and can be fought. The clue book says the third change, the Executioner Beast, is the form to avoid. L05 leaves that title open. It stays open.

Acceptance: Richard is awake, the Whole Truth has been used, and Scotia is defeated in her own form.

The fan page gives pedestal corners: cobra lower left, human lower right, dragon upper right, unicorn upper left. The clue book names the four figurines and does not give corners. The corner recipe stays the fan sentence.

The reference's Whole Truth sentence matches the clue book: Ruby of Truth plus Shard of Truth. The Computer Show text still never names either item. That older sentence stays.

Script checks:

- Nathanial's Key is type 199. `LEVEL26.INI` function 1 places it on level 26 block 75. The marker grades that LIKELY.
- Shard of truth is type 281. `LEVEL28.INF` function 555 places it on level 28 block 520 and calls `giveItem` on type 281. The calls sit behind a wall-type test. Grade LIKELY. The level 28 marker file does not list block 520.
- The Whole Truth is type 280. `LEVEL28.INF` and `LEVEL29.INF` push that type. No constant `createLevelItem` in this pass put it on a block. The inventory click that builds it stays a clue book step. The creation block stays UNKNOWN.
- Dawn's Key is type 198. `LEVEL24.INF` function 846 places it on level 29 block 1021. Grade LIKELY. The level 29 marker on block 1021 is a different INI item, type 22. The recovery sentence in the clue book and this call stay unmerged.
- Diamond is type 221. A constant floor block for the dungeon chest was not found. Block UNKNOWN.
- Statuette is type 255, one row for every figurine name in the item table. `LEVEL28.INI` places that type three times, and `LEVEL27.INI` places it once. Which placement is the cobra stays UNKNOWN.
- Death Key type 202 is placed on level 29 block 211, Oily key type 205 on block 200, Gold Key type 179 on block 915, and Dull key type 204 on block 995, all from `LEVEL29.INI` function 1. The dull-key marker grades its own call DECODED. The clue book's chest contents stay a separate sentence from those four blocks.
- Ruby of Truth stays type 220 from the swamp give in U02. No second ruby is created here.
