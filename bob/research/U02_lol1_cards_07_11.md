# U02 LoL1 cards 07 through 11

No Godot was run. The tree is `~/lol1_godot` at `9987d7e`, clean. P06's five cards stay the cards. This file fills the stops P06 marked unknown, from the same Westwood clue book used in U01. Grade HINTBOOK. The Computer Show sentences in L03 stay. A disagreeing clue book sentence is a second sentence.

The archive asm and the M04 item types are the same files named in U01. A printed clue book number is a map key. A block id below comes from a script push or from a marker.

## LOL1-07 Lake Dread

P06 acceptance stays the far side of the lake. The fallen keep stays a second return, separate from the poisoning.

The clue book, Northlands point 11, puts Timothy here after the Draracle, in his last moments, telling of the fallen keep and sending the party after Dawn. Point 14 puts Victor at the lake. He arranges the crossing and gives a longsword.

The Computer Show sentence stays: Victor says Dawn already took the boat. The clue book does not use that sentence. The longsword gift and the boat sentence stay unmerged.

Level 10's English name is Opinwood, area FOREST1. M03 says `level10.json` contains the substring Lake Dread, and that the lake sentence and the Opinwood name were not merged. The clue book lists Lake Dread as Opinwood point 1. No `loadNewLevel` in `LEVEL10.INF` pushes a constant destination. The crossing block stays UNKNOWN.

## LOL1-08 Opinwood

The green skull, the paid beggar, and the wagon refusal stay the acceptance.

Clue book, Opinwood:

- Point 11. A stump may contain a Green Skull.
- Point 12. The beggar can be helped, left, or attacked. Help costs 5 silver crowns. After that, clicking the riddle scroll on him can write one answer onto the scroll.
- Point 15. Droek's wagon. He keeps the party away from Dawn until the Ruby of Truth is carried.
- Point 10 is the longsword Flayer. Point 13 is a chest with a Kane leather jerkin and a lightning scroll. P06 already leaves both off the required list. The clue book does the same.

Green Skull is type 266. This pass found no constant `createLevelItem` for type 266. The stump block and the Upper Opinwood chest block stay UNKNOWN. Upper Opinwood is level 17. The clue book point 11 there is a chest that contains a green skull, an emerald blade, an ebony staff, and 10 silver crowns. That chest is a second source of the same item. The Opinwood stump and the Upper Opinwood chest stay two sentences.

Lightning scroll is type 235. Longsword placement for Flayer was not read as a type id. Neither is required.

## LOL1-09 Gorkha Swamp

Level 11 is Gorkha Swamp, area SWAMP. Acceptance stays the Ruby of Truth carried.

The clue book writes one crossing. Cast Freeze, spell row 2, at level 1. An unfrozen sinkhole drowns the party. No second path is written. P06 left that question unread. The hint book answers it with Freeze and with drowning.

The witch doctor is point 18. Clicking the riddle scroll on him writes one of the four riddle answers and costs 100 silver crowns. He also sells fireball wands at 300 silver crowns. The Computer Show sentence says he translates the riddle. The price and the count of four stay the clue book sentence.

The Computer Show sentence gives the chieftain a brass helmet. M03 says Lands has no brass-helmet item name. That sentence stays. The clue book says the Hurzels stole the ceremonial mask, one Hurzel carries it, and the chieftain trades the Ruby of Truth and the trident Mantis for it. Stealing the ruby and attacking the chieftain are the other two choices, and either one sets the tribe to war.

Ceremonial Mask is type 259. `LEVEL11.INF` function 45 calls `makeItem` on type 259. Ruby of Truth is type 220. Label `L_132` calls `giveItem` and `makeItem` on type 220. Functions 281 and 653 jump to that label. Function 45 calls `createHandItem` on type 220. The `giveItem` later in function 45 pushes type 125. None of the ruby calls carries a floor block. Grade DECODED for those call sites. The mask block stays UNKNOWN.

The same sinkholes are later an elixir step. With an empty vial, swamp water is taken from a frozen hole. Swamp Vial is type 212. That use is after the ruby. It does not change the card's acceptance.

## LOL1-10 Dawn

Acceptance stays the pyramid key carried, as P06 wrote it from the Computer Show text. That text says Dawn gives empty flasks and the pyramid key after she is shown the ruby and the riddle.

The clue book names four pyramid keys: Dawn's, Geron's, Nathaniel's, and Paulson's. Dawn's Key is type 198. Empty flask is type 211. The constant flask creates this pass found are both in `LEVEL8.INI` function 1, on blocks 117 and 469. Function 0 does not create them. M03 left those separate from Dawn's gift. They stay separate.

No constant `giveItem` of type 198 was found on level 10. The wagon's give block stays UNKNOWN. `LEVEL24.INF` function 846 places type 198 on level 29 block 1021. The clue book says a key handed to Scotia in Yvel Woods is found again on Cimmeria level 3. Grade LIKELY for the placement call. The woods loss and the level 29 block stay unmerged until a branch read joins them.

Droek's refusal until the ruby is the same gate as LOL1-08 point 15. Showing the ruby is what opens the wagon.

## LOL1-11 Urbish Mine

P06 stops at burned nests. These facts stay: the Computer Show text uses the green skull on a giant slug, puts a silver key on mine level 3, and burns nests with fireballs. The party list says Paulson joins. That text's steps never say he joins.

The clue book continues, and it uses different names.

| engine level | English name | area | clue book floor |
| --- | --- | --- | --- |
| 12 | Urbish Mining Co. | URBISH | Urbish Mining Co. |
| 13 | Mines Level 1 | MINE1 | mine level 1 |
| 14 | Mines Level 2 | MINE1 | mine level 2 |
| 15 | Mines Level 3 | MINE1 | mine level 3 |
| 16 | Mines Level 4 | MINE1 | deepest level, where Paulson is |

Clue book order after the skull is in hand:

1. At the mining company door, a Larkhon is released. Right-click a Green Skull on a portrait. Thrown weapons also work, and the book calls that way very hard. Leaving by a forest exit and coming back through the swamp is a way past it.
2. Visit Dwight on the company level and take a pick. A pick on mine level 3 sits inside a nest of avian worms.
3. On mine level 4, kill the rock beasts for a Bloodstone. Find the gear, the cleared stairs, the Shiny Key, and the Rusty key in Orin's remains.
4. The south hidden door on that deepest level leads to Paulson. Take his pyramid key. Take his Vaelan's Cube when he has one. The cube is for Scotia's barrier in Upper Opinwood. The book says Dawn is the other person who may have a cube.
5. The teleporters and the pump gear are why the party changes floors more than once. The gear from mine level 4 and coal from the company level start the pump. The company stairs and the mine stairs were not given constant destination blocks. Those blocks stay UNKNOWN.

Silver key is type 173. `LEVEL15.INI` function 1 places it on level 15 block 55, offset 0,128. The marker grades that DECODED. That matches the Computer Show "level 3" sentence and the English name Mines Level 3.

Bloodstone is type 273. `LEVEL16.INI` has functions 0 and 1. Label `L_18`, reached by `jmp` from function 1, calls `makeItem` on type 273 and then `giveItemToMonster`. No block argument. Grade DECODED for that call. The rock-beast sentence and this call stay unmerged.

Vaelan's Cube is type 264. `LEVEL16.INF` function 517 places it on level 16 block 611. The same function calls `addRemoveCharacter(6)`. Id 6 is Paulson. The function tests game flags, including flag 230 and flag 78, before those calls. Grade LIKELY. The level 16 markers on block 611 are other INI items, chain mail type 134 and a great helm type 140 among them. The cube shares the block number with those rows.

M03's Lora workaround stays in force: on level 16, block `0x225` (549), adding Paulson while slot 2 is Lora drops her items and removes her. That engine path is ScummVM, and `party.gd` still omits it.

The giant slug and the Larkhon stay two creatures. The fireball nests and the avian-worm nest stay two sentences. The mask temple from the Computer Show stop is still without a step. The clue book says Scotia uncovered the Nether Mask in these mines. It does not give a temple room. That sentence stays a mention.

Paulson is now three sentences. The party list names him. The Computer Show steps never say he joins. The clue book says to find him on the deepest level and take his key, and function 517 can add id 6.
