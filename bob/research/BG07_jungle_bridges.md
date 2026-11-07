# BG07 — Jungle bridges

Base `c9295da`, after BF01–BF07 and BG00a through BG06. Patch `patches/ACT3P2/BG07_jungle_bridges.patch`. Not applied to the live tree.

Owner r17 16-54-13 at about (-3731,-2083): the bridges had no collision. The grey sheet in that shot was the withdrawn AV04 water. With the sheets gone, deck 227 and the river planks 213, 214, 210 and 212 already held a Human and a Lizard. Source slabs 219, 221, 222, 223 and 224 (material 0655, 5 or 10 tall) dropped both forms. Those five source boxes are solid now. Human and Lizard do not break plank 210.

Printed on display :6, 60.40s:

`PASS jungle bridges: Human and Lizard crossed slabs 219, 221, 222, 223, 224, 227 and the river plank chain`

Also on display :6: `jungle_bridge_deck_test` PASS 20.33s, `jungle_props_test` PASS 9.60s, `static_raised_decks_test` PASS 13.99s. Ledger `--check` is 402 pieces.
