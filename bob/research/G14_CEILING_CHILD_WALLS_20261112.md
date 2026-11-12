# Ceiling-child wall bottoms, and the room 28 roof

2026-11-12. Read-only. LOLG.DAT sha256 `b27a35341c6e877e40b1540b6482748e7a750c605fefe6452431b18a5d766775` (file offset = VA + 0x37000). Geometry is the September export under `lol2_out/all_maps_20260922`. Grades are PROVEN, LIKELY, or LONGPLAY.

## The bottom the original uses

PROVEN. Both callers test the child's flag 0x20, then read a height from the owner.

At 0x11557c the walk steps back one region (0x2c) while flag 0x80 is set. When the owner is found, the test is on edi, the child:

- Flag 0x20 set: dword at owner+0x12, arithmetic shift 16. That is owner word 10. The jump at 0x1155aa skips the other load.
- Flag 0x20 clear: dword at owner+0x14, same shift. That is owner word 11.

The height is shifted back up and pushed to 0x115250.

The map builder at 0xf584c does the same test. Object byte +0x9e bit 0x40 means this region is a child (region flag 0x80 copied there). The child path at 0xf5912 tests the current region's flag 0x20 and loads dword +0x12 or +0x14 from the region saved at [esp+0x20]. Non-children store themselves there (0xf593b) and the pointer advances by 0x2c (0xf5b44), so the saved region is the last non-child. 0xf5952 shifts that height and 0x114584 calls 0x115250.

The draw byte is object +0x44, written at 0x115520. It is set when one bottom corner is below its top (0x11550d). A caller height above the child surface clears it, and that wall is not drawn.

`_owner_height_fixed` in `map_source_walls.py` tests the owner's flag 0x20 after the walk. That picks the other word exactly when the child has no flag 0x20 and the owner has it. Floor children (the child has 0x20) agree. Ceiling children whose owner has no flag 0x20 agree.

## Citadel tube, pack faces 3255 and 3256

PROVEN. These are the two walls of region 479, source records 1813 (code 2, edge 2) and 1815 (code 0, edge 0). Region 479 is a ceiling child of 468: child flags 0x2C0 (0x40 and 0x80, no 0x20), child surface word 10 = 137. Owner 468 flags 0x260 (0x20 and 0x40), word 10 = -40, word 11 = 147.

The original caller height is 147. Replay of 0x115250 for both codes: the draw byte is clear, and the corners sit at Y 137 and Y 147. The original does not draw this slab.

The port caller height is -40. The same replay sets the draw byte and returns Y -40 and Y 137, which is the exported span.

## The 22

Opus counted 22 walls that reach below the ceiling child's own surface: L13 2, L3_DH 6, L5_HC 14 (`CAUSES_ITEM2_20261112.md`).

PROVEN from the September `source_walls.json`. Ceiling-child walls (flags 0x80 and 0x40) whose exported bottom is below the child's word 10: 36 walls on 22 regions. L5_HC 18 walls / 14 regions, L3_DH 10 / 4, L9_DR 6 / 3, L13_RC 2 / 1.

LIKELY the published 22. The walls whose bottom sits 40 or more under the child surface are exactly L13 2, L3 6, L5 14. The note does not state that cut. No other split of this export lands on those three counts. True bottoms:

The port's height is wrong on 8 of them. PROVEN by the flag test and by replay.

| Walls | Region | Owner | Original bottom | What the original draws | Export |
|---|---|---|---|---|---|
| 1813, 1815 (pack 3255/3256) | L13 479 | 468 | 147 | draw byte clear, no slab | -40..137 |
| 2495, 2496, 2497 | L5 214 | 188 | 0 | a band Y 0..10 | -104..10 |
| 2492, 2493, 2494 | L5 215 | 188 | 0 | a band Y 0..10 | -104..10 |

Regions 214 and 215 use the same flags as 479 (child 0x2C0, owner 0x260). Child surface is 10. Owner word 10 is -235 and word 11 is 0. Replay of caller height 0 sets the draw byte and returns Y 0 and Y 10. Replay of the port's -235 returns Y -104 and Y 10, the exported span.

The other 14 already use the original bottom. PROVEN by the flag test: the child has no 0x20 and the owner has no 0x20, so both paths read owner word 11, and the export bottom is that word.

- L3_DH 1122, 1124, 1125 (region 550) and 1144, 1145, 1146 (region 554), owner 549. Bottom 125, top 165.
- L5_HC 2296, 2295, 2294, 2293 (regions 230, 232, 234, 236, owner 225) and 2380, 2381, 2382, 2383 (regions 276, 277, 278, 279, owner 265). Bottom -107. Tops are -67 or -57.

Fourteen more walls in the same export sit under the child surface by less than 40. They are not in the 22. Their caller height already matches the original, for the same flag reason.

- L3_DH 1130, 1132 (region 551) and 1137, 1138 (region 553). Bottom 125, top 145.
- L5_HC 2393, 2292, 2379, 2378 (regions 228, 238, 275, 280). Bottom -107, top -82.
- L9_DR 3940/3941 (region 3392), 2977/2978 (region 5344), 2985/2986 (region 5346). Sloped. One corner is 1 under the child surface (263 against 264, 112 against 113). The other end is the owner ceiling, 290 or 120.

## Temple room 28 from under the room 21 lintel

LONGPLAY. That look is not in the 30-second Act 2+ grid.

Opened in full: g_00266, g_00268, g_00269, g_00270, g_00275, g_00282. Sheeted g_00241 through g_00295, and the Citadel stretch g_00181 through g_00240. Clock is 6580+(N-1)*30 seconds.

- g_00268 at 4:03:10 is the carved-wood wall beside an opening, seen at eye level. The opening shows the next room's stone floor and wall. No sky, and no view up through a roof.
- g_00270 at 4:04:10 has a dark blue block in an opening, about rgb 30, 39, 96, while the inventory covers the right half. No carved-wood lintel and no beige band.
- g_00275 at 4:06:40 is the three-door room. A dark blue sky fills the top of the frame above the doorway. Samples there vary (about rgb 21, 32, 78 through 38, 46, 85), so it is not one flat pixel. This is not the view from under the room 21 lintel.
- g_00282 at 4:10:10 is a carved-wood corridor with a stone-block ceiling. No sky.

The Citadel tube was not on that grid either. g_00187 at 3:22:40 is the pillared hall with Remaining Ruloi 19/19. g_00205 at 3:31:40 is a rough rock wall. g_00216 at 3:37:10 is the green barred opening. None is the round tube. The tube grade above stands on the replay.
