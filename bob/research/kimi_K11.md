## STORY-079 — verified vs `L17_HC.json`

| claim | found? | note |
|---|---|---|
| MIX sha256 `23d7cecf…5cc793` | yes | `source.sha256` matches exactly |
| Static names, metadata 8534, count 13 (Green ceil…Teleport circle, 5× Spare BD) | not-in-export | no name strings anywhere in JSON; "8534" is a geometry offset, not JSON data |
| Prop template names (Wide guts, Hive Duct, crystals, etc.) | not-in-export | only numeric template ids exist (e.g. prop 99 → 6, prop 153 → its id, crystals → 11–14) |
| Local slot 0 = Platform_trigger @ geometry 159043 | not-in-export | string absent; offset is geometry-entry data |
| Actor defs 0/1/2/3 with counts 58/4/10/10 | yes | histogram of byte @32 over all 82 actor placements: exactly {0:58, 1:4, 2:10, 3:10}; labels (HIVEW etc.) unverifiable |
| Arrivals selectors 0–3 (coords, headings, regions 109/131/1311/1315) | not-in-export | hex patterns (`8fed`, `3cee`, …) absent; arrival data lives in the geometry entry |
| Level-change: movable 50, stream 1 group 3896, `020100001c50` | yes | movable:50 links stream 1 group 3896; group's final command is op2 with that exact raw |
| Region 1312→group 1632 & 1313→1638 `020100001c33`; 1318→1644 `020100001c70` | yes | region objects 1312/1313/1318 (kind-12 records) link those exact groups; each group is a single op2 with the exact raw |
| Single opcode 18: region 1293, stream 0 group 1566, words (−6084,−6404,0), flags 0x0005, heading 18386 | yes | `opcode_use['18']==1`; region:1293→group 1566; raw `120100003ce8fce600000500d247…` decodes to exactly those values |
| No opcode 21 | yes | no "21" in `opcode_use`; no group command uses it |
| Movable 50: stored (1439,7256), h 135, region 118, flags 0x0581, static Teleport circle | yes (name partial) | all numeric fields exact; byte @32 = 7 (matches Teleport circle's position in the claimed name list; name itself absent) |
| Group 3896 roster: op198 b4=0; op9 on props 308/307/309/310 b4=17; op1 on movable 50 b4=0; level-change | yes | all commands present with exact raws (group has 16 commands total; claimed subset confirmed) |
| Props 307–310 = crystals at (1308–1561, 7144–7382) | yes | coords all inside the claimed box; four distinct template u16s (13, 14, 12, 11) |
| "Op198 b4=0 not bound to Platform_trigger" | partial | command exists (target 0, b4=0); binding claim rests on a local-slot name not in the export |
| Prop 99: (−6243,−5890), region 1302, flags 0x4482; groups = op5, 16, 20, op9 on itself | yes | placement exact; groups 2146 (ops 5/16/20) and 2174 (ops 5/16/9, target 99) |
| Prop 153: (−4993,−7063), region 79; op2 raws `020100000c05` / `020100000b05` | yes | placement exact; groups 2926/2964 open with those raws — byte4 0x0c/0x0b, outside the `1c` level-change shape |
| "Byte 5 stays unread"; no spider/exit cstring; items zero | yes / not-in-export | all level-change raws share `02 01 00 00 1c XX`; zero spider/exit string hits; no item table exists |

## STORY-080 — verified vs `L19_BC.json`

| claim | found? | note |
|---|---|---|
| MIX sha256 `59cd77a1…de3380` | yes | `source.sha256` matches exactly |
| Static names, metadata 7743, count 20 (Golden Door…Bar door) | not-in-export | zero string hits; "7743" only inside a stream sha |
| Bar door zero placements | not-in-export | name absent, cannot bind a slot |
| Sixteen Metal beam controls are event 0 | partial | control static-slot 1 has exactly 16 placements, all with empty event lists — count/shape match; label unverifiable |
| Prop template names (Blood bowl, Ooze pipe, Beaker0–3, …) | not-in-export | only u16 template ids (222 & 223 → 9, 269 → 2) |
| Locals 0–12 at geometry 297237 (incl. slot 9 Level_entered) | not-in-export | zero string hits; offset absent |
| Actor defs 0–6, counts 1/28/17/1/1/10/10 | yes | histogram of byte @32 over 68 actors exact; labels unverifiable |
| Actor 39: def 0, (1939,891), h −125, region 2182 | yes | all fields exact |
| Actor 32: def 3, (18,596), h −10, region 616 | yes | all fields exact; it is the only def-3 actor |
| Arrivals selectors 0–3 | not-in-export | no coord/heading tuples anywhere in the JSON |
| Level change: region 22, stream 0 group 0, `020100001c51` | yes | group 0/stream 0 contains that exact op2; region-22 kind-12 record links it |
| Region 2369 → groups 15784/15790, `020100001c34` / `020100001c54` | yes | both groups exist with exact raws; two region-2369 records link them respectively |
| Prop 222: (120,−525), h 0, region 687, flags 0x0402, Ooze pipe | yes (coords) / partial (name) | all numerics exact; template u16 = 9 |
| Prop 222 kind-6 → group 2778 | yes | kind-6 event links 2778 (also 2814, 2850) |
| Group 2778: op21 `152038004000`, op3 `03010000902cbe0c01000000`, op198 b4=9, op9 u16 269 b4=21 | yes | all four commands byte-exact (op3: identity 0x0CBE2C90, byte+8=1, u16@+2=0) |
| Group 2814: op21 b4=58; op3 same identity, byte+8=1, u16@+2=32 | yes | `152038003a00`; `03022000902cbe0c01000000` — exact |
| definition 22, name slot `23-Hrn Belial`, handler 0 | not-in-export | external definition table; only raw identity bytes verifiable |
| Props number 270 → u16 269 fits only a prop | yes | `object_tables.prop` = 270, max index 269 |
| Prop 269 (Blood bowl): (13,899), region 686 | yes (coords) / partial (name) | numerics exact; template u16 = 2 |
| Prop 223: other Ooze pipe, (39,−526), region 687; op3 identity 0xD58C34FE byte+8=4 in group 2862 | yes | coords + same template u16 (9) as 222; group 2862 has op3 raw `03010000fe348cd504000000` |

## STORY-081 — verified vs `L19_BC.json`

| claim | found? | note |
|---|---|---|
| Horn bytes = the two op3 commands of STORY-080 | yes | `03010000902cbe0c01000000` (2778) and `03022000902cbe0c01000000` (2814), byte-exact |
| bacl16 is not an L19 actor | not-in-export (confirmed absent) | zero "bacl16" hits; no actor-def labels in export at all |
| L19's single BELSTAT placement = actor 32, region 616 | partial | actor 32 is the only def-3 placement, region 616 exact; label unverifiable |
| Prop 222 is region 687 | yes | region u16@10 = 687 |
| Regions 616/687 not joined | n/a | interpretive; both region ids verified as stored |
| No placed item on L19; item count 0 | yes | no item table in `object_tables` or `objects`; the string "item" appears 0 times in the JSON |

## Summary

Every checkable numeric claim in all three stories verified exactly — both sha256 hashes, all actor-def histograms and named placements, every level-change/opcode-18/opcode-21/opcode-3 raw byte string, and all group rosters (2778, 2814, 2862, 3896, 1632/1638/1644, 1566) — with zero discrepancies. The only non-confirmations are data classes genuinely absent from these script exports: all cstrings (statics, templates, locals, actor labels, item names), arrival-selector tuples, and geometry offsets, plus "item count 0" affirmatively confirmed by the absence of any item table.

