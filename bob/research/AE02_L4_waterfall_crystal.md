# AE02 L4 waterfall crystal

Base maps-y 4a32849. Godot was not run. Map.png was not regenerated. No game patch.

The L4 item table is the geometry section at file 12409578. The archive sha256 matches `L4_HJ.json`. Count at +0x6C is 88. Stride is 37. Names come from `assets/lol2/generated/items/definitions.json`.

Two rows are `56a-Ltng cr`, definition 55, identity 2228495501. Row 22 is (1889, 3855), height −60, region 4675. Row 23 is (1884, 3855), height −60, region 4675. Both flags are 2. They stay the shop pile. No other row is a lightning crystal. No row has the dormant bit 0x1000. `L4_HJ.json` groups and object placements contain zero copies of identity bytes `8d24d484`.

The 30-byte assembly-name table (metadata +0x44 count 98, end +0x14) names Waterfall at index 8, Whirlpool at 21, Water Button at 66, and Water Gate at 67. Static-assembly placements are geometry +0x18, count +0x64, stride 33, template byte 32. Waterfall and Whirlpool have zero placements. Water Gate is control 96 at (−3073, 5033), height −43. Water Button is control 97 at (−1947, 5487), height 35.

Control 97 kind 3 links groups 21102 and 21120. Each group is opcode 198, then opcode 5 target 427. Prop 427 is template 101, name fountain, at (−1744, 5346), height 0. The 2026-10-30 deviations row says opcode 5 stores a selector. Those groups do not carry the lightning identity. The hintbook lines 2250–2253 still name a pool click west of the westernmost bridge that reveals a Lightning Crystal. Brady PDF page 153, printed 152, still names a Lightning Crystal in the waterfall. Neither sentence has an item row. Luther's reward from that click is not in the item table. No marker was added. Shop rows 22 and 23 stay the shop pile.
