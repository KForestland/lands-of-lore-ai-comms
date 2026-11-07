# BG17 — Hive conversation woman height

Base `c9295da`, after BF01–BF07 and BG00a through BG15. BG16 added no patch. Patch `patches/ACT3P2/BG17_hive_conversation_height.patch`. Not applied to the live tree.

Owner r17 16-49-32 at Hive (-1179, -8839), height -203: "3 meater long cat, should be same or lower heitgt". That figure is the conversation woman, control 75, template 6, movie E070E, standing at (-1133, -235, -8885). The pack draws her 142.5 by 128. Cat statues are elsewhere, and Dawn was already scaled.

The pack is left at that authored size. At runtime the quad, its sideways shift, the "E — Speak" prompt, and the aim point scale by 44/128. 44 units is the player height Dawn already uses from owner r12l (2026-10-28 15:30:39). Her feet stay on y=-235. Native sprite projection stays unread.

A Human walked the room-to-conversation points from the rune room (-1218, -8725) to (-1174, -8843), looked at her middle, and pressed E. The line started. The quad was 44 units tall, the same proportions, and the pack was still 128.

Printed rendered, display :2, 6.92s:

`PASS hive cat: walked from the rune room to the woman at (-1174,-8843), and she stands about the player's height`

The existing conversation admission test also passed (5.23s, display :2) after the aim point moved to her middle.

Ledger `--check` is 411 pieces. The stack from BF01 through BG15 and BG17 applies on `c9295da`.

Grade: Adapter (owner rule 2026-10-30).
