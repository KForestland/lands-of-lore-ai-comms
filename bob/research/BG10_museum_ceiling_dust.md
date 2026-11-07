# BG10 — Museum ceiling dust

Base `c9295da`, after BF01–BF07 and BG00a through BG09. Patch `patches/ACT3P2/BG10_museum_ceiling_dust.patch`. Not applied to the live tree.

Owner r17 16-36-49 and 16-36-57 at (2557, 20): the dust pile looked worn away and should drop as in the last version. Y06 (`d740198`) turned flag 0x80 flat and switched the billboard off. The parent of that commit hung the same quads upright. Template 13 record 347 sits at (2671, 80, 9), 56 wide and 10 tall, in region 741. That room's floor is 0 and its ceiling is 90, so the upright quad fills the gap from the anchor up to the ceiling. The frame flag stays the row flip. The lie-flat turn is not in the record.

A Human walked from (2700, 20) to (2557, 20) and looked up at record 347.

Printed headless, 5.76s:

`PASS ceiling dust: walked to (2557,20), looked up, and the pile hangs under the ceiling`

The niche strike test also printed `PASS museum niche strike and upright ceiling dust` (1.82s). Ledger `--check` is 405 pieces.
