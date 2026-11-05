## STORY-074 — verification against `L16_CA.json`

| claim | found? | note |
| --- | --- | --- |
| Movable 79: static slot 55, (−5641,−4771), h −70, region 8197, flags 0x0582 | yes | exact match; byte 32 = 55 |
| …floor −70, ceiling 70, neighbors 65535/10117/65535/8198 | no | no geometry/region-descriptor data in this export; unverifiable |
| Group 49736 is opcode 20 | yes | single command, opcode 20, target 79 |
| Group 49746 is opcode 9 `09040c000d00`, u16 12, byte 4 = 13 | yes | raw hex identical; u16 = 12, byte 4 = 0x0d |
| Item 12 ivory chip (−5644,−4532), region 10120 | no | export has no item table; those coords appear nowhere |
| Props 460–465: flags 0x4482, h −70, x −6079..−5219, y −4680..−5020, regions 8217/8209/8201/8199 | yes | all six rows match exactly (template u16 79) |
| "Their command bodies were not copied" | misleading | bodies **are** in the export (e.g. group 18798 = opcode 198 + opcode 1); "not copied" can only mean into the story doc |
| "No globe cstring on those rows" | n/a | export contains zero cstrings anywhere, so nothing contradicts it |
| Pole w/ globe props 401–404, 446, 447, 494, 495, x 10609–15975 | yes | all 8 found, x range 10609–15975, template u16 54 |
| Poles are not neighbors of region 8197 | no | no neighbor data in export; unverifiable |
| Prop 223 (−4406,−1537), h 50, region 8186 | yes | exact match |
| …second group 6126 = twenty opcode 196 commands on regions 8167–8187 | partial | group 6126 linked as prop 223's 2nd group; **21** commands (not 20), all opcode 196, targets exactly 8167–8187 (21 distinct values) |
| Prop 399 (−9653,−3160), h 150, region 8510 | yes | exact match |
| …opcode 198 byte 4 = 22 | yes | group 14678, raw `c60000001601`, byte 4 = 0x16 |
| …cstring Trap_solved (slot 22) | no | no cstrings in export |
| Prop 400 (−7544,−3171), region 8626, event 0 | yes | exact match; 0 events |
| Prop 419 (−2280,−11620), h 45, region 8680 | yes | exact match; floor 45 / ceiling 420 not in export (no geometry) |
| Control 72 (−2283,−11613), h 165, region 8680, flags 0x8402 | yes | exact match; static byte 71 |
| Group 41818: opcode 16 + opcode 18 words (−2283,−11620,155), flags 0x0112, heading 0 | yes | raw `1210…15f7 9cd2 9b00 1201…`; all fields match |
| Group 41878: ivory opcode 3 byte +8 = 1, then opcode 9 u16 72 byte 4 = 2 | yes | `03010000090c2e04**01**…`, `0910 4800 02` |
| Prop 419 group 15242: opcode 198 byte 4 = 15 | yes | raw `c60000000f01` |
| …cstring Ice_door_trigger | no | no cstrings in export |
| Props 483/484/485 near (−4700, −1475..−1650) | yes | (−4695,−1650), (−4701,−1475), (−4700,−1562), template 81; "bodies not copied" again only means not quoted — groups 19314+ exist |
| Control 71 (−5214,−1470), h 20, region 8028, flags 0x0582, slot 53 | yes | exact match |
| Group 41770: opcode 196, opcode 9 u16 478, opcode 9 u16 71 byte 4 = 4, opcode 18 words (−4967,−1562,0), flags 0x0004, heading 0 | yes | all four commands and every field match |
| Control 108 (−5250,−1641), h −30, region 8121, flags 0x2582 | yes | exact match |
| Group 42940: opcode 18 words (−5011,−1364,0), flags 0x0004 | yes | matches; group also holds 196/9/9 the claim omits |
| Control 107 (−3951,−1379), event 0 | yes | exact match; 0 events |
| Chip-block rows 0/70/95/173/174/175/176: coords, heights, regions, slot 45 | yes | all seven rows match exactly; every one has static byte 45 |
| Group 41082: ivory opcode 3 byte +8 = 4 | yes | `…2e04**04**…` |
| …also opcode 1 u16 112 byte 4 = 100 then 0 | partial | 41082's own opcode 1 has byte 4 = 0; the byte-4 = 100 command (`012070006400`) is in control 0's **other** group 41052. The pair is real but spans two groups |
| Groups 41716 / 42334: ivory opcode 3, byte +8 = 4 | yes | both match |
| Group 48698: no opcode 3 in copied children | yes | opcodes are 9, 20, 9, 2, 5 |
| Controls 174/175/176: lists 18934/18946/18958 | yes | list_offsets match exactly |
| …"body not copied" | misleading | bodies exist: groups 48738/48778/48818 are fully present |
| Item 29, identity 0x178B0A33, def 94, `92-Sk key`, (−12561,−8217), h 65, region 8286, flags 0x2002 | no | no such row; identity bytes `330a8b17` absent; **no** object anywhere has flags 0x2002 |
| Controls 98 (−11770,−8215) rg 8296 and 172 (−9795,−13206) rg 10065 have event lists | yes | exact coords/regions; 2 and 4 events respectively; both static byte 11 |
| Prop 626's cstring under STORY-068, unbound | consistent | prop 626 exists; group 40538 has the single opcode 198 byte 4 = 16 (`c60000001001`) as STORY-068 states; no cstring in export |

## STORY-075 — verification against `L16_CA.json`

| claim | found? | note |
| --- | --- | --- |
| Props 222, 411–417 = Pedestal 1 at the 8 listed (x, y, region) rows | yes | all 8 match exactly; all share template u16 23, and **no other prop** uses template 23 |
| Props 405–410 = Pedestal 4 at the 6 listed (x, y, region) rows | yes | all 6 match exactly; all share template u16 26, unique to these props |
| Placed pedestals all height 200, flags 0x0082, event 0 | yes | all 14 rows: h 200, flags 0x0082, 0 events |
| Pedestal 2 and Pedestal 3 have zero placements | consistent | only two pedestal template ids (23, 26) appear; names themselves not in export |
| Items 13–21 and 25–28 in those regions, height 200, event 0 | no | no item rows exist in the export; the only height-200 objects are 18 props (14 pedestals + props 145, 160, 161, 558) |
| Item 14 (13189,1768) rg 8827; item 16 (13442,−1449) rg 7484; item 26 (12609,1485) rg 8828 | no | none of these coordinates appears anywhere in the file |
| Item names `R-Manafoil`, `R-Pyrapod`, `148-MoDScrl` | no | export contains no name strings at all |
| Prop 615, center Tower at (13273,−6464), event 0 | yes | exact match (h −999, region 6517, flags 0x0002, 0 events) |
| …only template-Tower row | yes (structurally) | prop 615 is the sole prop with template u16 57; the name "Tower" is not in the export |
| Four iris doors / four pylon regions / no fifth Iris Door | n/a | no ids, coords, or opcodes named in STORY-075 itself (it defers to STORY-069's table); names not in export |
| "Tower Hole" and "Mantle Gate" static names with zero placements | no | names unverifiable — no cstrings in this export |

## Summary

Every concrete object id, coordinate, region, flag, group id, and opcode byte pattern named in STORY-074 and STORY-075 was checked against the export and matches, with three discrepancies: group 6126 contains **21** (not twenty) opcode-196 commands, control 0's "byte 4 = 100 then 0" spans two groups (41052 + 41082), and several "body not copied" notes are about the story document, since those group bodies are present in the file. All "item" rows (items 12–29), every cstring/name, and all floor/ceiling/neighbor geometry are absent from `L16_CA.json`, so those claims are unverifiable from this source — nothing in the file contradicts them, but nothing supports them either.

