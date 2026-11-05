# J14 Niches, alcoves, and short tunnels

No Godot was run. Hintbook lines 1743–1746 say the automap is how you find side corridors, niches and alcoves, and that the small tunnels and cracks only the Lizard can use are hard to see without it. These lists are the geometry that matches that description. They are not a native "niche" flag. The form check that would prove a crack is Lizard-only was not read.

## Niches and alcoves

A niche here is a region with exactly one neighbour and a floor area between 20 and 800. One way in, small footprint.

| area | niches |
| --- | --- |
| L1_DC | 15 |
| L3_DH | 20 |
| L4_HJ | 7 |
| L5_HC | 3 |
| L7_DH | 34 |
| L8_SJ | 2 |
| L9_DR | 23 |
| L10_DC | 83 |
| L12_CM | 4 |
| L13_RC | 1 |
| L14_HT | 19 |
| L16_CA | 0 |
| L17_HC | 0 |
| L19_BC | 7 |
| L20_BB | 12 |

L10 has the most one-door pockets. L7 is next. L16 and L17 have none under this size rule.

## Short tunnels

A short tunnel is a connected run of 4 to 40 regions, each with headroom 8 to 24 and area under 1500, and the run's total area under 25000. Headroom is the ceiling base minus the highest floor corner.

| area | runs | regions |
| --- | --- | --- |
| L1_DC | 2 | 11 |
| L3_DH | 0 | 0 |
| L4_HJ | 3 | 44 |
| L5_HC | 5 | 51 |
| L7_DH | 0 | 0 |
| L8_SJ | 33 | 286 |
| L9_DR | 0 | 0 |
| L10_DC | 0 | 0 |
| L12_CM | 3 | 15 |
| L13_RC | 0 | 0 |
| L14_HT | 10 | 40 |
| L16_CA | 0 | 0 |
| L17_HC | 0 | 0 |
| L19_BC | 0 | 0 |
| L20_BB | 0 | 0 |

The L4 run of 23 regions is the known tiny-form pocket. All 26 regions 2739–2747 and 4526–4542 are present. Floor −70, ceiling −50, headroom 20. Three of them are over 1500 square units, so the run above counts 23. The earlier jungle-gate note calls that pocket tiny-form only. This pass did not re-read the form check.

L5's five runs sit on the thin −921 and −811 slabs (headroom 20). L8's 33 runs are short rooms grouped by neighbour, not a named Lizard path. L14's ten runs are four-region pockets at floor 0, ceiling 40.

## Still open

Which of these the Lizard can enter and the Human cannot. The hintbook names that difference. The region lists above are the candidates to draw on the atlas. No form test was run.
