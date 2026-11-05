# I16 sewer bars and switches

Place L19_BC. No frame was opened. No Godot was run. Static slot 0 is `Golden Door`, slot 1 `Metal beam`, slot 2 `Sewer door`, slot 3 `Switch`, slot 7 `Bridge`. Name-at-index stays LIKELY. Opcode 1, opcode 9, opcode 16, and opcode 198 were not entered. The opcode 196 floor formula applies where byte 6 is 0. Local slot 2's cstring is `Drop_down_sewer_door`. The join stays unbound.

Hintbook lines 5416–5427: as Human, break the bars. As Lizard, enter the gutter. Shoot the three switches. A dam forms and the guck rises, then jump the sewer. Grade HINTBOOK. Brady printed 136: the bars are where the blood flows, the sword breaks them, the Lizard fits the opening, and three switches across an acid canal take missile hits. One throw closes the flood gate. The next clears the slime, and the floor under the slime rises. Grade BRADY. The bars, the form change, and the three hits are REQUIRED in both books. The hintbook's rising guck and Brady's rising floor are different sentences.

## Bars

Static Bar door is slot 19 and has zero placements. Sixteen controls, LIKELY Metal beam, are event 0. No command read here tests Human or Lizard. The bars and the gutter stay the books.

## The colinear switches

Movables 74, 75, and 76, LIKELY Switch, are (−323, 2124), (−304, 2124), and (−281, 2124), height 42, regions 36, 34, and 32. Godot y is −2124. Each has the same shape.

One kind-6 group ends in opcode 1 byte 4 = 100 on movable 77. The paired group ends in opcode 1 byte 4 = 0 on the same door. Ahead of that opcode 1, each group stores opcode 196 commands with byte 6 = 0. The first set uses word +4 = −45 and byte 7 = 25. The second set uses byte 7 = 2 and words −55, −65, −75, −85, −95, and −40. The accepted formula makes those absolute floors. The current floors were not read, so the direction is not the book's rise.

Movable 77, LIKELY Sewer door, is (−344, 1621), height −38, region 738. Godot (−344, −1621). Its group 7898 is ten opcode 196 commands, word +4 = −20, byte 6 = 0, byte 7 = 2.

## The other three switches

Movables 50, 71, and 72, LIKELY Switch, are (1535, 3282) region 213, (1622, 3609) region 609, and (1629, 3246) region 606. They are not on one line. Each has two kind-4 groups. One is opcode 198 byte 4 = 2, byte 5 = 1, then opcode 1 byte 4 = 100 on movables 70, 50, 71, and 72. The other is opcode 198 byte 5 = 0 and opcode 1 byte 4 = 0 on those four.

Movable 70, LIKELY Bridge, is (1586, 3413), height 100, region 214. Godot (1586, −3413). Its two groups are opcode 9 on itself, byte 4 = 16. Opcode 9 was not entered.

## Still open

Which trio the books mean. The current floors under the opcode 196 targets. A Human or Lizard test. A guck mesh. No frame.
