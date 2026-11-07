# BG00a — L8 tree bridge and cache ladder

Base `c9295da`. Patch `patches/ACT3P2/BG00a_l8_bridge_ladder.patch`. Not applied to the live tree.

Owner r17: control 114 (17-57-09) and control 69 (18-08-06) did nothing in play. The old tests called `use()` after a teleport.

A Human walks to the west bank. An empty hand does not fell the tree. A catalog weapon and the left-click chop unlink assembly 114 and link assembly 116. The stored log slab is 12 wide and the human radius is 15, so a flush deck carries the body from the west-bank floor across the hole. The log mesh stays. E at the cache ladder moves to the opcode 18 ledge and stays there through physics. Opcode 9 and opcode 20 stay unplayed. Headless has no captured mouse, so the input gate treats a headless display as playing. A real window still requires capture.

There is no atlas objective pin for this. Ledger piece `0318-row-2026-11-07-e00-l8-walkable-bridge-ladder.md`.

Printed on display :3:

`PASS l8 cache ladder: E at control 69 moves to the stored ledge`

`PASS l8 tree bridge: E at control 114 links the placed log`

`PASS earned L8 tree bridge: Human walked up, chopped with a weapon, and crossed the log; the cache ladder climb stayed on the ledge`
