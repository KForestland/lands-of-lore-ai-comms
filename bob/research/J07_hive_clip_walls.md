# J07 L5 clipping walls

Owner 17-42-38 / 43-05 / 43-17. The window is native x −3689..−3507, y 7143..7394. F10 y is the negation of that. No Godot was run. No longplay frame was matched. `L5_HC.MIX` sha256 prefix `a1979e60`. Faces are `hive_review/hive.json`.

Floor polygons in this window do overlap, once each outline is walked counter-clockwise. The overlap is area, not a shared edge.

## The corridor against the upper room

Region 758 is floor −1011, ceiling −639, flags `0x2204`. The exported corners are flat. Its floor is face 1900, material `234` (`material_234.png`). Its ceiling is face 1901, material `21` (`material_21.png`).

Two upper regions share that footprint and the height band −941..−691:

| pair | area | other floor / ceiling | other faces |
| --- | --- | --- | --- |
| 758 ∩ 911 | 571 | −941 / −691, material `234` / `231` | floor 2393, ceiling 2394 |
| 758 ∩ 907 | 359 | −941 / −691, material `234` / `231` | floor 2376, ceiling 2377 |

Both upper floors are `material_234.png`. Both ceilings are `material_231.png`.

The walls cross inside that overlap:

| face | region | record | resource | heights | where |
| --- | --- | --- | --- | --- | --- |
| 1902 | 758 | 1826 | 65 | −1011..−639 | edge (−3694, 7215)–(−3650, 7277). The middle of this edge is inside 911 and 907. |
| 2396 | 911 | 1536 | 225 | −941..−691 | edge (−3641, 7250)–(−3688, 7223). The whole edge is inside 758. |
| 2379 | 907 | 1534 | 210 | −941..−691 | crosses 758 faces 3793 and 3794 at (−3633, 7263) |

Face 3793 is record 1825, resource 65, heights −1011..−921. Face 3794 is record 1824, resource 65, heights −891..−639. Keys: `material_65.png`, `material_225.png`, `material_210.png`.

The west sample (−3689, 7143) is region 751, floor −1011, ceiling −639. Region 757 is the next room on that floor. The overlap starts on region 758.

## Thin slabs inside the upper room

These regions are 30 units tall (floor −921, ceiling −891) and their floors sit inside the upper room. Floor material `21`, ceiling material `65`.

| pair | area | thin faces |
| --- | --- | --- |
| 907 ∩ 1178 | 470 | floor 3160, ceiling 3161. Region 1178 has no wall records. |
| 907 ∩ 1176 | 273 | floor 3152, ceiling 3153 |
| 907 ∩ 1175 | 122 | floor 3148, ceiling 3149 |
| 910 ∩ 1191 | 140 | floor 3195, ceiling 3196 |
| 910 ∩ 1178 | 107 | the same 1178 faces |
| 910 ∩ 1175 | 91 | the same 1175 faces |

Region 1179 is sloped (flags `0xa20c`). Floor corners are −911, −911, −921, −921. Ceiling corners are −901, −901, −891, −891. It overlaps region 910 by area 470 and region 909 by area 44. Faces 3162 and 3163.

## The east slot

Region 752 is floor −981, ceiling −921, footprint about (−3536, 7184)–(−3485, 7235). Its floor does not meet the pairs above. On region 756 edge 2 the pack draws face 3791 (record 1817, resource 65, −1011..−981) and face 3792 (record 1818, resource 65, −921..−639). The open band between them is −981..−921, the height of region 752.

## Still open

Which longplay frame shows region 758 against 907 and 911. Whether the original portal clip hides the crossing quads. That clip was not read.
