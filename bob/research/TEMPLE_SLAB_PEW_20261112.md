# Temple slab room to the pew floor

Read-only. No build. The plan coordinates are the table helper's `(x, z)`, with `z` the stored `y` negated, the same pair the chain test walks. Pinned `DAT/L14_HT.MIX` sha256 `c294f9ab142b55c36fff545a1293c419c42353fedefbfe8b77b9c38a2d9a0719`. Geometry file offset `11406344`, region stride `0x2C` at geometry `0x1CCFA`. Neighbor words are `+0x04` through `+0x0A` (`0xFFFF` empty). Floor is the signed word `+0x14`. Word `+0x16` is the ceiling when flag bits `0x08` and `0x80` are clear. The point test is `Table.inside` in `opus_lane/tools/trace_replay_tracker.py` on `opus_lane/g05/L14_HT_table.json`. Grades are PROVEN, LIKELY, or UNKNOWN.

## The two sheets at the slab

`(2370, -3328)` lies in two regions.

| Region | Floor | Ceiling | Flags | Neighbors |
| --- | --- | --- | --- | --- |
| 164 | −80 | 20 | `0x0200` | 3236, 163, 780, empty |
| 856 | 0 | 125 | `0x0200` | 859, 855, 812, 851 |

Bits `0x20` and `0x80` are clear on both, so the finder keeps whichever of the two is already the hint. PROVEN from the MIX and from the keep rule in `REGION_STACK_MOVER_20261112.md`.

## Floor −80 has no step onto floor 0

Region 164's floor −80 sheet is 120 regions, built by walking neighbor words whose floor word is −80. The floors of the regions named from that sheet, and absent from it, are −300, −100, −75, −70, −60, −58, −55, −50, −30, 20, and 70. A floor-0 neighbor is absent. PROVEN from the MIX.

The east line of the chain, from `(2370, -3328)` toward `(2500, -3328)`, leaves region 163 at about `(2494, -3328)`. Region 163's slots are 3237, empty, 781, 164. The empty slot is the second. The only region that holds the point there is 821, floor 0. PROVEN.

The south corridor Opus walked, 3237 then 3420 then 3262 then 3261 then 3264, stays on this sheet. Region 3264's slots are empty, 3261, 3267, 3269. Its floor is −80 and its ceiling is 20. `(3017, -3873)` is inside region 1056 only. PROVEN.

## The way to `(3000, -3900)`

That point is inside region 1058 only, floor 0, ceiling 125. The one-unit walk along the chain's own bends, hint 856, stays on floor 0 and arrives there. Each landing is a MIX neighbor of the region it leaves. PROVEN.

| Order | Region | Centroid | Floor | Ceiling word | Flags | Slot taken |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 856 | (2325, −3364) | 0 | 125 | `0x0200` | |
| 2 | 812 | (2394, −3327) | 0 | 125 | `0x2200` | 2 of 856 |
| 3 | 816 | (2413, −3328) | 0 | 125 | `0x0200` | 2 of 812 |
| 4 | 814 | (2433, −3327) | 0 | 125 | `0x2200` | 1 of 816 |
| 5 | 821 | (2513, −3362) | 0 | 125 | `0x0200` | 0 of 814 |
| 6 | 818 | (2605, −3398) | 0 | 110 | `0x4200` | 1 of 821 |
| 7 | 820 | (2635, −3402) | 0 | 95, bit `0x08` set | `0xc208` | 3 of 818 |
| 8 | 819 | (2664, −3414) | 0 | 80 | `0xc200` | 1 of 820 |
| 9 | 21 | (2827, −3374) | 0 | 125 | `0x0200` | 1 of 819 |
| 10 | 22 | (2907, −3466) | 0 | 125 | `0x0200` | 3 of 21 |
| 11 | 23 | (2997, −3540) | 0 | 125 | `0x0200` | 3 of 22 |
| 12 | 24 | (3089, −3681) | 0 | 125 | `0x0200` | 2 of 23 |
| 13 | 1056 | (3093, −3863) | 0 | 125 | `0x0200` | 3 of 24 |
| 14 | 1058 | (3013, −3828) | 0 | 125 | `0x0200` | 0 of 1056 |

Regions 812 and 814 are three units wide in `x`. A step that jumps those three units leaves 816 with 821 holding the point, and 821 is absent from 816's slots. The seam point `(2432.5, -3328)` is inside 814. PROVEN for the slots and the widths.

Region 820's flag bit `0x08` is set, so its word 95 is stored and is not the ceiling. The other thirteen ceiling words above are ceilings. PROVEN as stored bytes.

## Stairs on the floor −80 sheet

These are the climbs that sheet does have. Both end on a region that names the same sheet.

Floor 70 lip, the highest neighbor: 164, 3236, 3253, 3247, 3234, 3233. Regions 3234 and 3233 are floor 70, ceiling 210, flags `0x0202`, about ten units wide. Their four slots are empty, each other, and the −80 regions 3247, 3235, 3245. PROVEN.

Floor 20 lip through the south treads: 164, 3236, 3253, 3247, 3248 (−80), 3246 (−70), 3244 (−75), 3242 (−70), 3240 (−80), 3423 (−80), 3424. Region 3424 is floor 20 and ceiling 20, flags `0x0202`. Twelve regions of that shape are named by the sheet: 3271, 3272, 3288, 3289, 3424, 3432, 3864, 3865, 3871, 3873, 3892, 3893. Each has floor 20, ceiling 20, flags `0x0202`. PROVEN.

The sloped neighbors of that tread run are 3427 (corners −75 to −55), 3425 (corners −70 to −50), and 3429 (corners −70 to −50), flags `0x0206`, so bit `0x04` selects the slope call. Their ceiling word is 20. PROVEN from the MIX records read with the tread run.

Flag bit `0x02` is set on 3234, 3233, and the twelve floor-20 lips. A per-step change onto bit `0x02` is rejected when byte `[0xB7D4D]` is 2. Which value the player returns there stays UNKNOWN, as in the stack note.
