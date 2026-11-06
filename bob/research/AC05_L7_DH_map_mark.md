# AC05 MAP-MARK L7_DH

Base act3-story a123d3f. The native pack matches that commit. There is no numbered Brady map. Printed 83–85 are prose. Map.png was not regenerated.

`markers.json` had 9 rows. This pass added three. It now has 12.

Added:

- Gaunt strike, item row 5 (−1125, 969), height 750, region 1576, slot 13-Gaunt strike. `area_world_items_state.gd` hosts it. Prima folio 70 names Gauntlets of Might. The two names were not merged.
- Ancients' stone, item row 27 (−2077, 1672), height 0, region 1353, beside the amulet. Rows 2 and 3 are the same slot at height 310. Which sentence owns which row was not chosen.
- Peephole slides, control 237 (−1468, 571), height 785. Controls 237–251 sit on a ring at height 785. Brady printed 84 names metal slides, and one shows candles. The candle slide was not singled out.

No matching geometry or host:

- Healing Scroll. No item slot of that name.
- Prism scroll. The SS6 row stays marked and was not renamed.
- The iron door and the bricked window. Movables 56 and 57 exist, and so does the peephole ring. They were not joined to the iron door or to the seven-o'clock crack.
- Plasma staff. No separate drop point. Actor 57 is already marked. `dark_halls_items.gd` hangs the staff on `darkhalls:actor57:Plasma_staff`.
- Seven copies of opcode 2 body `020100001cc4`, byte5 196, on regions 1394 and 1408–1413. Byte5 196 is level 4 selector 6. None was named, and none was called the escape hole.
- Chapter 15 has no coordinate bug in this area.
