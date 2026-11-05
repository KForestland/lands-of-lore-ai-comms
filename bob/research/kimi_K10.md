## STORY-076 — verification against `L16_CA.json`

| claim | found? | note |
| --- | --- | --- |
| prop 365 (4858,−6515) region 8906 | yes | exact; template u16 30, h 80, flags 0x0002, 0 events |
| prop 366 (4865,−7551) region 9224 | yes | exact; template 30, h 80, flags 0x0002, ev 0 |
| prop 367 (6182,−6522) region 8883 | yes | exact; template 30, h 80, flags 0x0002, ev 0 |
| prop 368 (6174,−7551) region 10080 | yes | exact; template 30, h 80, flags 0x0002, ev 0 |
| prop 369 (6318,−7422) region 8900 | yes | exact; template 29, h 80, flags 0x0002, ev 0 |
| prop 370 (4750,−7422) region 8924 | yes | exact; template 29, h 80, flags 0x0002, ev 0 |
| prop 371 (6311,−7170) region 8895 | yes | exact; template 27, h 80, flags 0x0002, ev 0 |
| prop 372 (4728,−7156) region 8918 | yes | exact; template 27, h 80, flags 0x0002, ev 0 |
| prop 373 (4721,−6904) region 8914 | yes | exact; template 28, h 80, flags 0x0002, ev 0 |
| prop 374 (6297,−6911) region 8893 | yes | exact; template 28, h 80, flags 0x0002, ev 0 |
| Shape 1/2/3/4 template split (2+2+2+4 rows) | yes (structurally) | four distinct template ids 27/28/29/30 in the claimed groupings; names "Shape N" are not in the export. Note: those templates also have other placements elsewhere (props 184–188, 204, 213–216, 391) — the ten ring rows are not the only uses |
| All ten h 80, flags 0x0002, event 0 | yes | verified for all ten |
| Center prop 615 Tower (13273,−6464), event 0 | yes | exact (h −999, region 6517, flags 0x0002); sole prop with template 57. "Ring around" it is interpretive — the ring sits ~7000 units west |
| No movable with x 11000–16000, y −9000..−4000 | yes | scanned all 201 movables: zero hits |
| Tower Hole / Teleporter / heaven stair / Staged Button / Bool / Bright Star zero placements | n/a | static/template names are not stored in this export, so placement-by-name cannot be checked |
| Four Iris Door controls the only door rows on the four pylon regions | n/a | no ids, coords, or regions named in STORY-076 itself (defers to STORY-069's table); nothing concrete to check |
| Pylon groups (STORY-069) contain no opcode 198 | n/a | the pylon group ids are not named here, so they cannot be identified; opcode 198 does occur 70× elsewhere in the file |
| Trigger_Nth_tower_pylon cstrings unbound; local slot 0 = Star_Elevator | no | export contains zero cstrings; unverifiable |

## STORY-077 — verification against `L16_CA.json`

| claim | found? | note |
| --- | --- | --- |
| prop 331 (5443,−9749) h 10 region 223 | yes | exact; template 46, flags 0x0002, ev 0 |
| prop 332 (5578,−9751) h 10 region 228 | yes | exact; template 46, flags 0x0002, ev 0 |
| prop 333 (5636,−9879) h 10 region 214 | yes | exact; template 46, flags 0x0002, ev 0 |
| prop 348 (5384,−9879) h 10 region 215 | yes | exact; template 46, flags 0x0002, ev 0 |
| All four template Mantle, flags 0x0002, event 0 | yes (structurally) | all four share template u16 46, and template 46 has **exactly** these four placements; the name "Mantle" is not in the export |
| floor 0 / ceiling 200 | no | no floor/ceiling geometry in this export |
| No placed item named "mantle"; static Mantle Gate zero placements | n/a | no name strings anywhere in the export |
| Local slot 1 = Got_mantle, 12 = Mantle_conveyed, 13 = Belials_access | no | no cstrings in the export |
| Actor-def labels VISC, HL3, bacl16, VISC, B_HUMAN, B_HUMAN; none is Belial | no | 47 actor rows exist but carry no label strings; unverifiable |

## STORY-078 — verification against `L16_CA.json`

| claim | found? | note |
| --- | --- | --- |
| prop 241 Dragon (1625,−4417) h 52 region 9476 flags 0x4481 | yes | exact; sole prop with template u16 110 |
| …floor 50, ceiling 155, neighbors 9492/9475/9460/9477 | no | no floor/ceiling/neighbor geometry in this export |
| Kind 9 group 6384 | yes | prop 241's kind-9 event record links to group 6384 |
| …6384: op 9 u16 241 byte 4 = 18; op 9 u16 73 byte 4 = 3 and = 21; op 16; op 5; three op 7 | yes | exact: `0903f1001200`, `091049000300`, `091049001500`, op 16, op 5, then 0703… ×3 — 8 commands, all matching |
| Kind 6 group 6438: op 9 u16 241 byte 4 = 17; op 5; two op 7 | yes | kind-6 event links to 6438; `0903f1001100`, op 5, 0703… ×2 — exact |
| U16 73 fits a prop, a control, and a movable | yes | prop:73, control:73, movable:73 all exist |
| Dragon groups contain no opcode 198 | yes | 6384 opcodes [9,9,9,16,5,7,7,7], 6438 [9,5,7,7] — no 198. The cstring Hanging_drac itself is not in the export |
| prop 144 Dead dragon (1623,−4946) h 35 region 9965 flags 0x0082 ev 0 | yes | exact; sole prop with template 112 |
| props 237–240 Sm Dragon, same neighborhood, ev 0 | yes | template 111, exactly these 4 rows; (1543–1710, −4303..−4488), adjacent to prop 241; all ev 0 |
| props 141–143 Sm dead drag, same neighborhood, ev 0 | yes | template 113, exactly these 3 rows; (1547–1709, −4829..−5007), adjacent to prop 144; all ev 0 |
| prop 211 Dragon Statue (261,−10600) h 50 region 9783 flags 0x0002 ev 0; not the dragon's coordinate | yes | exact; sole template-98 row; ~11 km of x from prop 241 |
| control 74 Telepad (2100,−4296) region 9615 | yes | exact (h 15, flags 0x0482); static byte 27, unique among controls |
| …level change `020100001c31` | yes | control 74's group 42056 is a single opcode-2 command with exactly that raw hex |
| Arrival selector 2 = (2107,−4183) region 9603; regions differ from 9615 | partial | no placement at (2107,−4183) exists and region 9603 holds no placed object — arrival selectors are geometry-side data absent from this export; region mismatch (9603 vs 9615) is consistent |
| Telepad neighbors 9604/9614/9606/9616, 9603 not among them | no | no neighbor geometry in this export |
| Static Teleporter zero placements | n/a | name not stored in the export |

## Summary

Every concrete id, coordinate, region, height, flag, event count, group number, and opcode byte pattern named in STORY-076/077/078 checks out exactly — including the full command contents of groups 6384, 6438, and 42056 (`020100001c31`), the empty movable band, and the exclusive template sets for Mantle (46) and the dragon family (110/111/112/113/98). Unverifiable from this export: all cstrings and static/template/actor labels, floor/ceiling/neighbor geometry, the arrival-selector row, and the STORY-069 cross-references (iris-door regions, pylon groups), since none of those name checkable ids here.

