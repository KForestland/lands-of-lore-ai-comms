# G-16 counts after the furniture rule, 2026-11-14

Read-only. No building and no geometry patch. The archive is `all_maps_20260922`. The pair rule is `prepare_region_mover.overlaps` on the r19i tool (rules 1-5: area above 4, floor bases within 48, not neighbours, no flag 0x80, floor-to-ceiling spaces meet) and then the two interpolated floor heights at the overlap centre within 24. That recount matches the 2026-11-13T17:46Z table on every level before the new rule.

Rule 6, accepted 2026-11-14T01:06Z: drop any pair where either region has all four nav links null. A region like that is a block, not a room. Zone ids below are the 17:46Z ids. Survivors are not renumbered. Chain and owner labels are those ids with the removed zones taken off. Point membership was not shot again.

## Counts

| Level | 17:46Z zones, regions, true/rule5 | After rule 6 |
| --- | --- | --- |
| L1_DC | 0, 0, 0/0 | unchanged |
| L3_DH | 0, 0, 0/0 | unchanged |
| L4_HJ | 0, 0, 0/0 | unchanged |
| L5_HC | 1, 6, 6/9 | unchanged. Chain T0, owner T0 |
| L7_DH | 2, 14, 12/20 | unchanged. Chain none, owner none |
| L8_SJ | 13, 46, 34/44 | 11 zones, 34 regions, 24 true. Drops T0 (region 3397) and T11 (region 3567). Chain T6 T7 stays |
| L9_DR | 27, 210, 316/434 | 25 zones, 206 regions, 314 true. Drops T22 (region 3583) and T24 (region 3525). Chain T1 T2 T14 T18 T20 T25 T26 stays |
| L10_DC | 19, 204, 231/371 | 19 zones, 202 regions, 229 true. T0 loses region 3934 (2 pairs) and stays. Chain and owner labels stay, including T0 and owner T0 T10 |
| L12_CM | 1, 3, 2/2 | unchanged |
| L13_RC | 0 | unchanged |
| L14_HT | 17, 241, 350/528 | 12 zones, 216 regions, 330 true. See below |
| L16_CA | 4, 71, 91/95 | unchanged |
| L17_HC | 1, 6, 9/9 | unchanged. Chain T0 |
| L19_BC | 1, 4, 3/10 | unchanged |
| L20_BB | 0 | unchanged |

## L14

Whole zones that leave: T1 (4106 with 2304 and 2308), T4 (4073 with 533, 534, 535, 536), T7 (4062 with 606, 608, 658, 1969, 1970, 1971, 2066, 2067), T9 (4074 with 959, 961, 1067, 1073), T16 (2329 and 3219). Those are the sealed boxes. T8 stays as 660, 863, and 864; region 4043 had no neighbours and its pairs drop.

Chain that remains: T0 T3 T5 T6 T8 T10 T11 T13 T14 T15. T4 and T9 leave it. Owner stays T3 and T14. The six walked zones T2, T5, T6, T8, T10, and T15 all remain. No L14 zone is being built. T6 stays Opus's parked stair pilot.
