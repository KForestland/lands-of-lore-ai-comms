# BI01 jungle bramble (meta duck)

1. Problem: BG15's solid brambles are the right gate, and the earned walks fail because the walker never swings. r18b stuck on control 103 (jungle_to_village waypoint 27) and control 109 (monastery_to_hive waypoint 80).
2. Main chain: yes. Those two walks are the jungle-to-village and monastery-to-hive routes.
3. Intent: gate. The player cuts or burns the torn wall, then walks through before it grows back.
4. Contract: walk up, aim, three sword strikes, the wall opens, walk through. Later the timer grows it back. Spark burns it and it stays down. Owner r17 16-44-37 and 16-44-57.
5. EXACT: controls 101-109, template 10, flags 0x4481, solid bit 0x80, sword mask 0x080E/0x0004 states 0 then 1 then 2 then open (selector 3, state 3), timer 0 regrows (selector 5, state 4), Spark mask 0x0091/0x0003 stays open (selector 4, state 5). The carried blade is the one the save already equipped. APPROXIMATE: the swing animation.
6. Cheapest faithful: re-apply 3fe7946 and teach the walks to aim and left-click. The walls stay solid. The walker is not placed past them.
7. Prove with the existing route walks plus the bramble earned test.

Grade DECODED for the state machine. Grade HINTBOOK for the owner's "cut the torn wall."
