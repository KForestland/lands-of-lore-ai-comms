# Urbish Mines wall punch, 15 Nov 2026

Light note for the Enhanced backlog. No Classic work. No Godot.

The owner asked to reuse the Lands of Lore 1 Urbish Mines "punch the wall" mechanic on Enhanced-edition blocks: strike a weak wall and it breaks. Source of the ask: AI_COMMS/IMPROVEMENTS.md, 2026-11-15, owner via the lead.

Sources opened this pass:

- Closed LoL1 RE: `~/lands-of-lore-1-re` (closure memo 2026-03-20). Wall records: `data/wll_parsed.json`. Level tilesets: `docs/level_tileset_map.md`.
- Decompiled EMC: `<owner-media>` (`level12_inf.asm`, `level13_inf.asm`, `onetime_inf.asm`).
- English strings: `lol1_dialogue_decoded/lands_eng.json`.
- Engine: `~/scummvm-lol1-fork/engines/kyra/` (`lol.cpp`, `scene_lol.cpp`, `gui_lol.cpp`, `script_lol.cpp`, `scene_rpg.cpp`).
- Walkthrough copy: `ScotiaEraPrototype/RESEARCH/LoL1_Walkthrough.md`.
- LoL1 Godot tree `~/lol1_godot`: no punch, sledge, or breakable-wall handler.

## What the written steps say

The Computer Show walkthrough stops during Urbish Mine level 3. In that Urbish section the named walls are doors, a keyhole, a pit button, and one line: "Go through secret wall to (11)" on level 3, then a chest opened with lock picks. The steps do not say to strike it, and they do not name a tool.

The same file's only "break a wall" steps are in Draracle's Cave. Take the sledgehammer from the eastern corner of level 2. On the return to level 1, break the broken wall at (5) and the wall at (6). The item table says: Sledgehammer, Draracle's L2, Break walls. The office level of the mine says to take a pick axe. It does not say the pick breaks a wall.

Grade: WALKTHROUGH. These are the copied steps. They are not a decode of the executable.

## How a wall is marked

Tilesets from the closed RE, checked against ScummVM's level list: level 12 is URBISH (the office). Levels 13-16 are MINE1.

On levels 12, 13, 14, and 15 the WLL defines four wall types that share one look class. Level 16 does not define them.

| Type | Decimal | Level 12 shape | Levels 13-15 shape | Shared fields |
|------|---------|----------------|--------------------|---------------|
| 0x38 | 56 | 38 | 9 | VMP page 1, special type 1, flags 7, automap 210 |
| 0x39 | 57 | 39 | 10 | same |
| 0x3A | 58 | 40 | 12 | same |
| 0x3B | 59 | 41 | 11 | same |

A plain solid wall (0x01) uses VMP page 1, shape 0, flags 7, automap 255. These four types use that same page, so they render as a wall, and they add a decoration shape a plain wall does not have. Flags 7 keep bit 0 set, so the party cannot walk through. Special type 1 means a click on the shape runs the level script with flag 0x40 (`KyraRpgEngine::clickedWallShape`). Automap byte 210 is not the plain-wall byte 255.

This pass did not open the shape pictures, so it does not say the decoration is a drawn crack. The mark in the data is the shape index, the automap byte, and special type 1.

A different type, 0x1A, exists on every level including 12-16: VMP page 0 (no geometry), shape 0, flags 132, automap 63. After a successful step, if the entered cell's north wall byte is 0x1A, `LoLEngine::moveParty` clears all four wall bytes of that cell (`scene_lol.cpp`). That is a walk-in clear of an invisible cell, not a strike. This pass did not match any CMZ cell to that byte.

## What breaks the marked wall

The attack button sends flag 0x400 (1024) to the level script of the current cell, with the weapon in hand, or item 0 when the hand is empty (`clickedAttackButton`).

`level13_inf.asm` (from word 692) and the same sequence in `level12_inf.asm` (from word 2026) do this:

- Continue only when register 0 equals 1024.
- Read item parameter 10. That parameter is `ItemProperty.itemScriptFunc` (`olol_getItemPara`). An item id of 0 returns 0 before any property is read, so an empty hand passes.
- The branch runs only when that value is 0.
- It then reads a wall type, and when a counter matches an argument it writes wall type 58 or 59, plays sound 187, and can write 0 onto a face.

`ONETIME.INF` sets `itemScriptFunc` to 0 on the Pick (item 28, might 7), the Sledge (item 59, might 15), the Long sword (item 81, might 20), the Dagger (item 44), and the Mace (item 90). Bows and arbalests use script function 11, so they do not take this branch. The check does not read might and does not require the Pick or the Sledge. Seventy-nine weapon rows (type 5) have script function 0. Thirty-three do not.

The number of hits is an argument of that script call (the counter on a helper face is compared to it). This pass did not list those call arguments. No hit count is stated.

Grade of the strike: DECODE of the engine and of the level-12 and level-13 scripts. The per-wall hit count is UNREAD.

## What a click does instead

Special type 1 runs flag 0x40, the use event. In the same level-13 subroutine that path reads the item in hand and compares its property index to 245. Item 245 is Lockpicks (`nameStringId` 16735, LANDS.ENG "Lockpicks", script function 255). It then calls `characterSkillTest` with skill slot 1. The three skill slots are stored in order, and `calculateCharacterStats` comments them as Fighter, Rogue, Mage, so slot 1 is Rogue. The test is 1d100 against skill level + modifier + 25. The failure line is LANDS.ENG string 84, id 16468: "You failed to open the lock."

That is a lockpick check. It is not the punch. Might is a separate stat and is not read here either.

## Two other wall removers, not this mechanic

Ice. `processMagicIce` sets block flags bit 0x10 when the spell level is above 2. `breakIceWall` runs if an ice-damaged monster survives, and the attack button calls it when the cell ahead already has bit 0x10. It clears that bit, plays `shatter.wsa`, and plays sound 166. That is the ice spell. It is not an Urbish punch.

Vaelan's Cube. `processMagicVaelansCube` zeroes the four wall bytes of the cell ahead when that face's VMP page is 1 or 2, wall-flag bit 0 is clear, and the level is not 22. The 0x38-0x3B walls have flags 7, so bit 0 is set and the cube does not take them. On level 13, type 0x2E is VMP page 1 with flags 132 (bit 0 clear), so the cube can clear that type. That is a different wall.

`item_inf.asm` never calls `setWallType`. The sledgehammer line in the walkthrough is not an item-script opcode found here.

## What lies behind

Not read. This pass did not decode a CMZ, so it does not name the cell or the contents past a 0x38 face. The walkthrough's one Urbish secret wall, on mine level 3, is said to lead to a chest. The steps do not say that wall is struck, and this note does not equate that sentence with types 0x38-0x3B.

Grade of the room behind: UNREAD. Grade of the walkthrough sentence: WALKTHROUGH.

## Enhanced use

Parked with the Enhanced edition, after Classic start to end. A LoL2 wall block can carry this as its own data, not as a Classic opcode:

- Mark it the way the WLL marks 0x38-0x3B: the solid wall material, plus a decoration the plain wall does not have, blocked until it breaks, with a map mark that is not the plain-wall mark.
- A melee strike opens or advances it. The original accepts an empty hand and any weapon whose script function is 0. It rejects a bow. It does not test strength. The hit budget is per wall, and it stays unset until those script arguments are listed.
- A click is a separate event. On the original subroutine that event is the lockpick test, with "You failed to open the lock."
- Do not reuse the ice shatter or the cube dissolve for these blocks. The cube only clears a wall whose flag bit 0 is already clear.
- The invisible 0x1A walk-in clear is a third mechanic and is not this strike.

If it is built later, the deviation row should cite this note and say the hit count and the room behind each Urbish face are still unread. It should not be added to the Classic mine.
