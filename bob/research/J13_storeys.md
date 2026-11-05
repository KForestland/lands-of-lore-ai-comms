# J13 Storey grouping

No Godot was run. Source is `all_maps_20260922/<AREA>/geometry/geometry.json`. `render_maps.py` cuts storeys with a fixed 160-unit band (`storeys()`, band 160, keep a band only when it has 25 regions and it stacks on another band). That cut splits a ramp whose floor crosses the band line.

## Rule used here

Flat neighbours (floor-corner spread of 8 or less) join when their floor mids differ by 12 or less. A sloped region joins every neighbour whose floor interval overlaps the slope. One ramp therefore stays one storey, together with the landings it touches. Two flat floors further than 12 apart stay separate even when a long staircase of flat steps connects them the long way. A component of 8 or more regions is one atlas page.

The wide floor span on the biggest page is the ramp-connected ground, not many floors squeezed into one band. The later rows are the separate pages.

## Counts

| area | regions | components | pages (8 or more) | pages (25 or more) | biggest page |
| --- | --- | --- | --- | --- | --- |
| L1_DC | 1954 | 45 | 11 | 3 | 1691, floors −440..81 |
| L3_DH | 1499 | 112 | 26 | 12 | 643, floors −70..40 |
| L4_HJ | 4787 | 105 | 26 | 7 | 3410, floors −214..120 |
| L5_HC | 1292 | 89 | 26 | 11 | 392, floors −635..−5 |
| L7_DH | 2014 | 105 | 13 | 3 | 1481, floors 55..760 |
| L8_SJ | 3961 | 92 | 22 | 10 | 3178, floors −90..200 |
| L9_DR | 6829 | 354 | 57 | 26 | 753, floors −121..632 |
| L10_DC | 4320 | 629 | 28 | 7 | 1908, floors −100..65 |
| L12_CM | 3644 | 64 | 17 | 14 | 1087, floors −200..140 |
| L13_RC | 1449 | 83 | 21 | 8 | 507, floors −1050..−740 |
| L14_HT | 4275 | 323 | 44 | 13 | 2076, floors −469..120 |
| L16_CA | 10582 | 835 | 101 | 45 | 3476, floors 0..146 |
| L17_HC | 1340 | 12 | 3 | 2 | 1286, floors −140..80 |
| L19_BC | 2870 | 158 | 30 | 14 | 802, floors −130..−110 |
| L20_BB | 1853 | 53 | 19 | 8 | 708, floors −50..−15 |

L16 has the most separate pages (101 of 8 or more, 45 of 25 or more). L9 is next (57 / 26). L17 is three pages. L4's ground page is 3410 regions because the hillside ramps connect floors −214 through 120. The next L4 pages are 434 regions (−11..50), 268 (−85..−40), and 150 (−30..−20).

## Still open

A slope whose two landings are themselves full floors joins those floors into one page. That is the ramp rule. A floor the player would still want as its own picture, inside that joined span, was not split again.
