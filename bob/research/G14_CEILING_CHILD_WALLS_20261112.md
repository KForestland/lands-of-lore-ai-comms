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

## The 134 walls the child-flag height turns on

2026-11-12, append. Read-only. Same LOLG.DAT. The re-export at `lol2_out/all_maps_20261112_ceilingchild` was read and was not written again. Opus's list is `opus_lane/g14/CEILING_CHILD_CHANGES_20261112.json`: 142 rows, the 8 already proved and 134 new. Each new row was replayed through original 0x115250 (`ChildWallReplay`, draw byte at object +0x44). The caller height is the wall region's own flag 0x20. That flag is clear on all 134, so the caller reads owner word 11.

PROVEN. The same call on the eight already proved records repeats the accepted result. L13 1813 and 1815 keep the draw byte clear, corners at 137 and 147. L5 2492 through 2497 keep the draw byte set, span Y 0..10.

The walk back to the owner passes earlier children whose flag 0x20 is set. The height used here is the wall region's own flag, and the eight-record check above is what shows that this is the same word as the accepted proof.

The draw byte is set on all 134. The corner span is the child surface, word 10, through the caller height. Replaying the same 134 with owner word 10, the September choice, clears the draw byte on every one. That is the height that left them out of the September export. The spans below match Opus's new spans on all 134 rows.

### L13, 112 walls

Draw byte set. Two caller heights.

Stack, caller 160. That is owner word 11 on owners 0, 15, 30, 94, 109, and 124. Owner word 10 is −40.

| Span | Walls | Regions |
|---|---|---|
| 61..160 | 36 | 8, 14, 23, 29, 38, 44, 102, 108, 117, 123, 132, 138 |
| 104..160 | 20 | 9, 24, 39, 43, 103, 107, 118, 122, 133, 137 |
| 107..160 | 4 | 13, 28 |
| 127..160 | 24 | 10, 12, 25, 27, 40, 42, 104, 106, 119, 121, 134, 136 |
| 135..160 | 12 | 11, 26, 41, 105, 120, 135 |

Region 8 is in the first row. Records 1613, 1615, and 1616, span 61..160. These 96 walls are the stack end caps.

Tube, caller 147. That is owner 468 word 11. Owner word 10 is −40.

| Span | Walls | Region | Records |
|---|---|---|---|
| 60..147 | 3 | 482 | 1828, 1829, 1830 |
| 62..147 | 3 | 476 | 1819, 1820, 1822 |
| 104..147 | 2 | 481 | 1825, 1826 |
| 109..147 | 2 | 477 | 1816, 1818 |
| 127..147 | 2 | 480 | 1567, 1568 |
| 129..147 | 2 | 478 | 1469, 1470 |
| 137..147 | 2 | 479 | 1809, 1811 |

These 16 walls are the tube end caps. Records 1809 and 1811 are codes 10 and 8 of region 479. The draw byte is set and the band is Y 137..147. Records 1813 and 1815 of that same region stay the accepted clear draw byte.

### L5 Hive, 22 walls

Draw byte set on all 22. Records 95 through 116. Caller height 0, owner 188 word 11. Owner word 10 is −235. Child surface is −104. Span Y −104..0 on every wall. Regions 205, 206, 207, 208, 209, 210, 211, 212, 213, 216, 217, 218, 219, and 220. Regions 214 and 215 stay the accepted band Y 0..10.

Owner 188 has floor −235 and ceiling 0. Its footprint is x −1146..−712, map y 7480..7623. These 22 walls are the ceiling-child faces inside that footprint.

### Act 1 longplay, Hive regions 205–220

LONGPLAY. The 5-second grid stores no player position. Opened in full: f_00489 at 40:40, f_00522 at 43:25, and f_01100 at 91:35. Sheeted f_00481 through f_00530 (40:00–44:05), f_00551 through f_00559 (45:50–46:30), and f_01093 through f_01104 (91:00–91:55).

f_00489 is the red cracked floor and a soft red cloud, with a black opening ahead. f_00522 is that hall with a bright yellow patch on the floor and the blue curse flash. f_01100 is the step from the lava floor onto the green patterned tile. f_00551 through f_00558 stay in the red hall, and f_00559 is the jungle mouth.

Owner 188 is interior. The four Hive arrivals are regions 676, 463, 832, and 642. The opened frames show the lava hall and the tile step. The region 188 footprint is absent from them, so none of these frames is a view of regions 205–220.
