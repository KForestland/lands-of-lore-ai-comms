# BG12 — Museum dragon click

Base `c9295da`, after BF01–BF07 and BG00a through BG11. Patch `patches/ACT3P2/BG12_museum_dragon_click.patch`. Not applied to the live tree.

Owner r17 16-37-59 at Museum (3049, -1114): "point to click here the drogon has a point to click." The camera looks into the alcove (pitch -0.19, yaw about 0). That spot is inside the authored region 1422 chamber. E already starts the journey from there. A left click did not. The click now uses that same gate. E still starts it. The original hotspot dispatch stays unread.

A Human walked through the chamber mouth to (3049, -1114), looked into the alcove, and clicked.

Printed rendered, display :2, 6.29s:

`PASS dragon click: walked to (3049,-1114), looked into the alcove, and a click started the journey`

Ledger `--check` is 407 pieces.

Grade: Adapter (owner rule 2026-10-30).
