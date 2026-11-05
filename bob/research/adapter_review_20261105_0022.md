# R2 adapter review, row 0022, 2026-11-05

No Godot was run. No opcode callee was entered. The idle line still names `~/opus_work/lol2_r12y` at `56812f9`. The row file, `tools/prepare_dark_halls_loot.py`, `scripts/lol2/dark_halls_loot.gd`, `scripts/lol2/dark_halls_items.gd`, and `scripts/lol2/dark_halls_rix.gd` were opened in `~/opus_work/lol2_r15` at `f6a5aa4` and match the r12y copies byte for byte. `item_defense_data.gd` differs. Its five `darkhalls:` rows match, including Stone bracers -30, Fire shield 15, and Plasma staff 0. The next unopened file is `0023-row-2026-10-21-dark-halls.md`.

## 0022 Dark Halls loot

The row gives eight controls their source items on E, facing them, within 110 units. First use is predicate 206 and second use is predicate 207. Scrolls are carried and not usable. Stone bracers and the Fire shield take the modern offhand slot at defense -30 and +15. Prop 212 and Rix's Plasma staff are not hosted. Status in the row is pending.

`dark_halls_loot.gd` stores `REACH` 110 and a facing cone of 0.75. Its comment calls that a modern adapter and says the native click-on-object hit is not used. The producer maps predicate 206 to the first grant and 207 to the second. Those predicates were not entered. The item names on the eight controls are Stone bracers, Fire shield, Colim's amulet, two Healing scrolls, a Prism scroll, an Ancients' Stone then a Spark scroll, two Prism scrolls, and a Healing scroll then a Summon scroll.

GLOBAL.MIX definition byte 0x41 is the signed defense the generator stores. Index 46 `47-Stone bracrs` is -30. Index 44 `45-Fire shield` is 15. Index 13 `14-Plasma staff` is 0. Definitions sha256 prefix `b399b5c8bfea3597`.

The row's "Plasma staff is not hosted" is behind the script. `dark_halls_rix.gd` gives group 14496, predicate 216, on E after actor 57 is dead, still inside the 110 reach. Talk and the give branches (soul +2) stay unhosted. Prop 212's six-item event stays unhosted. The Ancients' Stone is the one grant marked with a use. The scrolls stay carried.

HINTBOOK lines 2480-2481: Ancients' Stones in the room with the beds, and the Healing Scroll in the sliding bookcase. Lines 2485-2488: the Prism scroll is in a bookcase, right-click it on Luther, and load Healing scrolls in slots six to ten. Lines 2512-2517: the guest's staff shoots plasma bolts and is inferior as a weapon. Line 2532: Colin's Amulet and the Gauntlets of Might are past the blasted door. Those lines print no 110, no -30, and no +15.

BRADY lines 3382-3383: the first storeroom's bookcase has a prism scroll. Lines 3418-3424: Rixx attacks with his Plasma Staff, and killing him lets you take it. Lines 3436-3438: the crack room holds a crossbow and a shield. Lines 7354-7355: after the iron door, a bookcase holds Colim's Amulet. Lines 6993-6998 name Stone Bracers, Fire Shield, Gauntlets of Striking, and Colim's Amulet, with no defense number. Lines 1441-1442 say Colim's amulet blocks magic drain. That protection sentence stays off the halls find. The crack-room shield stays off the Fire shield control. Hintbook's amulet-and-gauntlets room stays off Brady's bookcase amulet.

No printed number replaces 110 or the facing cone. No simpler native build while the click hit and the scroll-use callee stay unread. The offhand slot and the two defense bytes stay the row.

## Still open

Predicate 206, predicate 207, and predicate 216 were not entered. The native click test was not read. Scroll use was not read. Prop 212's six items stay unknown, as the producer says.
