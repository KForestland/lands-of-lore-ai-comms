# BG02 — the mother dies after the birth

Base `c9295da`, after BF01–BF07, BG00a, BG00, and BG01. Patch `patches/ACT3P2/BG02_mother_dies.patch`. Not applied to the live tree.

The player still does not kill her. Level 5 still enters the mother, the birth card still plays, and the demons are still the kills. Two seconds after the demons fall she dies. The creatures of L20 are set absent and stay absent across a save. MotherBody, DemonWave, and BirthDoor are built only on L20_BB. placenta.vqa is still not in the movie table.

Printed on display :3:

`PASS l19_dawn_curse_test: Dawn clicks, level 5, birth card, the mother dies only after the demons`

`PASS earned Dawn's ruby, the birth, and the mother's death: the player did not kill her, and the area's creatures are gone`
