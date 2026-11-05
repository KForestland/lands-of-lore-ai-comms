## STORY-082

| claim | found? | note |
|---|---|---|
| Movables 74/75/76 at (-323,2124), (-304,2124), (-281,2124) | yes | exact word0/word1 match |
| Height 42, regions 36/34/32, flags 0xC581 | yes | word3=42; word5=36/34/32; word4=0xC581 (stored signed -14975) |
| Movable 74 kind-5 event → group 5882 = opcode 16 + opcode 1 `01204a006400` | yes | group 5882 commands: `10204a000100`, `01204a006400`; u16 target 74, byte4=0x64=100 |
| Kind-6 group 5930 ends in `01204d006400` (u16 77, byte4=100) | yes | last of 20 commands in group 5930, exact match |
| Kind-6 group 6182 has `01204d000000` (u16 77, byte4=0) | yes | present (not last; 10 further opcode-196 commands follow) |
| Movables 75/76 event lists 3632 / 3676 | yes | list_offset fields are exactly 3632 and 3676 (74's is 3588) |
| Movable 77 at (-344,1621), height -38, region 738, flags 0x0581 | yes | all four fields match |
| Group 7898 is opcode 196 only | yes | 10 commands, all opcode 196 |
| "Switch"/"Sewer door" template names; two Sewer-seal movables; 16 Metal beam controls event 0; Bar door zero placements | not verifiable | no names in JSON; 28 movables and 114 controls have/ lack events, but template identity can't be resolved from this file |
| No guck cstring; Ooze template names | vacuous | true that no guck/ooze strings exist — but the JSON contains zero cstrings of any kind, so this proves nothing about the source |

## STORY-083

| claim | found? | note |
|---|---|---|
| Movable 50 (1535,3282) region 213; 71 (1622,3609) region 609; 72 (1629,3246) region 606 | yes | exact matches |
| Each has two kind-4 groups | yes | 50→3762/3808, 71→5652/5698, 72→5744/5790, all kind 4 |
| Group A: opcode 198 byte4=2 value 1, then opcode 1 byte4=100 on 70,50,71,72 | yes | `c60000000201` then `0120..006400` ×4 in that order |
| Group B: opcode 198 byte4=2 value 0, then opcode 1 byte4=0 on the same four | yes | `c60000000200` then `0120..000000` ×4 (5698 orders them 70,71,72,50 — same set) |
| Movable 70 "Bridge" at (1586,3413), region 214, flags 0x0581 | yes | coords/region/flags match; "Bridge" name not in file |
| Movables 50 and 71 copied and match | yes (substance) | their group pairs are content-identical modulo op-1 ordering |
| Local slot 2 = Drop_down_sewer_door; "opcode 198 was not entered" | not verifiable | no local-slot names or cstrings in JSON |

Minor omission: each of these groups also opens with an opcode-20 command (`14204600b80180000c14`) that the claim doesn't mention.

## STORY-084

| claim | found? | note |
|---|---|---|
| Movable 51 at (2550,854), height -100, region 1931, flags 0x0582 | yes | all match (word4=1410=0x0582) |
| Group 3854: opcode 198 byte4=4 value 0, opcode 196, opcode 16, opcode 1 byte4=100 on 51 and 52 | yes | `c60000000400`, 10× opcode 196, 2× opcode 16 (`..000100`), `012033006400`/`012034006400` |
| Group 3998: opcode 1 byte4=0 on 51 and 52 | yes (partial) | both `0120..000000` present, but group 3998 also contains two opcode-16 commands (`102033000000`/`102034000000`) the claim omits |
| Eighteen Golden Door movables have event lists | not verifiable | 28 movables (indices 50–77) have event lists; no "Golden Door" names to filter by |
| Local slot 4 = Lab_elevator_two; "opcode was not entered" | not verifiable | no slot names/cstrings in JSON |

## STORY-085

| claim | found? | note |
|---|---|---|
| Props 67/69/68/70 coords (1451,1131), (1018,1128), (1028,1892), (1451,1891); height -60; regions 1671/1626/1669/1685; flags 0xC681 | yes | all 16 values match decoded placements |
| Prop 66 (2426,882), height -75, region 1972, flags 0x0402 | yes | exact match |
| Prop 65 (1306,1444), region 1706, group 66, four opcode-18 commands | yes | group 66 holds exactly 4 opcode-18 commands; prop 65 has no other group |
| Opcode-18 payloads: flags 0x0112, height word -60, words (1450,1132), (1019,1128), (1026,1893), (1450,1893), targets 67/69/68/70 | yes | all four commands match byte-for-byte; words sit 1–2 units off the four skulls' stored coords, as claimed |
| Props 67–70 each have opcode 18 on themselves, flags 0x0313, height word -20 | yes | 4 per prop, target=own index, `ecff`=-20, `1303`=0x0313 |
| …with x,y "jittered by a few units" from stored | **no (as stated)** | prop 67's op-18 coords are ≈(1489–1501, 1463–1466) vs stored (1451,1131) — Δy≈332; prop 68's ≈(998–1004, 1464–1467) vs (1028,1892). The four copies are jittered relative to *each other* (a few units), and cluster near the disk y≈1464, but they are not near the props' own stored coordinates |
| Prop 66's group = opcode 15 + opcode 9 on itself | yes | group 204: `0f03420037034200`, `090342000200`, both target 66 |
| Control 57 at (1240,1454), height -120, region 1706, flags 0x0482; group 3660 = opcode 5 only | yes | all fields match; group 3660 is the single command `051039000100` |
| Actor 31 at (1247,1445), height -120, region 1706, flags 0xFC82; prop 65 shares region | yes | word4=-894=0xFC82; prop 65 region also 1706 |
| "Skull"/"Light"/"Summoning disk"/IMP_BEL names; local slots 3/4 Lab_elevator(_two); no ghost/fountain cstring; ruby deferral to STORY-086 | not verifiable | zero cstrings exist anywhere in this JSON, so name claims can't be confirmed or denied from it (the "no ghost/fountain cstring" statements are true but vacuous here) |

## Summary

Every numeric claim — ids, coordinates, heights, regions, flags, group numbers, and opcode byte strings — verifies exactly against `L19_BC.json`, with two wording issues: STORY-084's group 3998 also carries two opcode-16 commands the claim omits, and STORY-085's "stored x and y jittered by a few units" is wrong as stated (props 67–70's own opcode-18 coordinates sit ~300+ units away in y; they are only jittered relative to each other). All template/def/local-slot/cstring claims are unverifiable from this file because the JSON contains no symbolic names whatsoever.

