# BG03 — beast-wall step only on that arrival

Base `c9295da`, after BF01–BF07, BG00a, BG00, BG01, and BG02. Patch `patches/ACT3P2/BG03_beast_arrival.patch`. Not applied to the live tree.

The step to (84, 22, 80) runs only when L19 selector is 1, the player is within 48 of the witnessed point (84, 22, 305), nav region 25 contains him, and the entry was a level change. Another L19 entry does not set the note and does not move him. A reload keeps the note and does not step again. `plays_movie` and `relocates_player` stay true. No BeastMovie node. hw01.vqa is still a different beat.

Printed on display :3:

`PASS l19_beast_wall_test: strand card, one step, only arrival 1 region 25`

`PASS earned blade save -> region 1312 -> L19 arrival 1, Luther steps through the strands; another L19 entry stays put`
