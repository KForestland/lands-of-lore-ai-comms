# BG15 — Jungle torn bramble

Base `c9295da`, after BF01–BF07 and BG00a through BG14. Patch `patches/ACT3P2/BG15_jungle_bramble.patch`. Not applied to the live tree.

Owner r17 16-44-37 at Jungle (-3342, 663), and 16-44-57 a step further along the same curtain: the torn wall can be burned by Spark or cut with a weapon, and a cut wall grows back. That curtain is L4_HJ controls 101-109, template 10, flags 0x4481. The solid bit 0x80 is set. The assemblies are scripted, so the generic builder drew them and added no collision. The walk went through.

Spark matches the first kind-9 record (mask 0x0091/0x0003, mode 4, byte +8 is 5) and clears the solid bit: selector 4, owner state 5. It stays open. A sword matches mask 0x080E/0x0004 and walks states 0, 1 and 2. The third cut clears the bit (selector 3, state 3) and starts timer 0. That timer is flag 0x10, so the count is seconds at 60 ticks. When it ends the wall is solid again (selector 5, state 4). Durability on the placement is 6, and 5 on control 109, so one armed cut is enough to pass the mode-4 threshold. The test walks only control 109. The same host stands the other eight.

Unread, so not played: mask 0x0200 touch damage (opcode 19), opcode 14 arm 5, kind 6 caller 2 (state 4 back to selector 0), control 109's extra kind-6 callers 0x14 and 9, opcode 7 index 2, opcode 20, and any other effect of flag 0x4000. The regrown wall stays on selector 5.

The aim boxes sit on layer 2, which the jungle creatures also give the player. Each aim box is a collision exception on the player, and an open wall leaves the physics space the same way a hidden assembly does.

A Human walked into control 109 and stopped. Three sword cuts opened it. The walk crossed. The wall grew back and the walk stopped again. Spark burned it, and the walk crossed.

Printed rendered, display :2, 21.95s:

`PASS bramble: walked up to the torn wall at (-3342,663), three sword cuts opened it, it grew back, and Spark burned it down`

Ledger `--check` is 410 pieces. The stack from BF01 through BG15 applies on `c9295da`.

Grade: Adapter (owner rule 2026-10-30).
