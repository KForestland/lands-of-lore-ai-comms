# BG08 — Museum broken Thohan

Base `c9295da`, after BF01–BF07 and BG00a through BG07. Patch `patches/ACT3P2/BG08_museum_broken_thohan.patch`. Not applied to the live tree.

Owner r17 16-30-49 at (985,-2515) h42: the broken Thohan sword in the case would not come away. Group 11954 grants `12-Tho Broken` from an empty hand. The blade is a fixed-Y quad whose centre sits about 14 units above a level eye at that spot, so the 0.97 centre cone misses a level look. The same 4° rectangle used for the other Museum sprites accepts that look, and the case contact stays excluded from the ray. A different item in the hand still shows the take. E puts that item away, then grants the blade. The centre cone still returns it.

Printed on display :2, 5.69s:

`PASS broken thohan: walked to (985,-2515), a level look took the sword, and a held longsword was put away`

The walk is rendered because a headless mouse mode stays visible and the pickup requires capture. Ledger `--check` is 403 pieces.
