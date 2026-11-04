# Kimi K1 — verification of grok source_ids_066_075.md, STORY-066 vs L14_HT.json

Run 2026-11-04 by Kimi Code CLI (read-only). Lead spot-checked: group 9210 with command 020100001c30 and group 19248 present in r13 L14_HT.json.

| claim | found? | note |
| --- | --- | --- |
| L14_MIX sha256 `c294f9ab…0719` (header) | yes | matches `source.sha256` |
| Control 78: (688, −10873), h 0, region 2282, flags 0x0482, static slot 67 | yes | byte 32 = 0x43 = 67 |
| Control 79: (638, −10752), same fields | yes | identical decode |
| Both: kind 4, groups 17622/17640, predicate 207, entry `0005000001` | yes | stream 1, exact match |
| Children `0c03aa001e00` + `0903aa001500` (u16 170, bytes 30/21) | yes | both groups, exact bytes |
| Region 2282 floor 0 / ceiling 195 / neighbors 2264,65535,65535,65535 | not in JSON | export has no region geometry |
| Prop 170: template u16 10, (1080, −11330), h 0, region 4024, flags 0x0402 | yes | exact |
| Prop 170: kind 6 group 9210, value 20, predicate 50, entry `0003160001`, only child `020100001c30` | yes | exact; byte 5 = 0x30 as claimed |
| Region 4024 floor 0 / ceiling 64 / neighbors all 65535 | not in JSON | no region geometry in export |
| Prop 0: template u16 17, (1071, −11521), h 0, region 4024 | yes | exact |
| Prop 0 group 0 (stream 1) = opcodes 16, 8, 13, 13, 2 `020100002700` | yes | exact sequence |
| Prop 384: (−1701, 3170), region 4103, opcode 3 identity 0x1200015E, byte +8 = 4 | yes | `030100005e01001204…` in group 15378 |
| Item 1 dreamstone: identity 0xCE20AEE3, def 136, `134-Dreamstone`, (3264, 2664), h −96, region 4073, flags 0x0002, event 0 | not in JSON | export has no item table (`item:1` absent) |
| Region 863 group 1462 and region 4176 group 3836, both `020100001c68` | yes | region objects link those groups; bytes exact |
| Level-change shape `020100001c` occurs exactly 3× (1462, 3836, 9210) | yes | census over all 1062 groups |
| Movable 65: (−549, −11298), h 0, region 2257, flags 0x0582, groups 19248+19278 | yes | exact; static byte 32 = 67 |
| Movable 66: (−585, −11173), region 4126, groups 19308+19338 | yes | exact; static byte 32 = 67 |
| Movable pairs: opcode 1 byte 4 = 100 under pred 206, byte 4 = 0 under pred 207, plus opcode 16, on u16 65+66 | yes | exact in all four groups |
| "U16 170 fits more than one table" | questionable | export table sizes (actor 96, control 168, movable 104, prop 412) fit only prop; item table absent from JSON |
| Arrival selector 2 = (789, −10774), heading 0, region 2282 | not in JSON | no arrival/selector data in export |
| Local slot 22 cstring `go_to_level_16` | not in JSON | no locals table in export |
| Resolved §066: prop 137 template u16 2, (1615, −195), h 0, flags 0x0402, region 4072, stream 1 group 7066 | yes | exact |
| Group 7066: 16 opcode-3 commands; dreamstone `e3ae20ce` ×1, flute `c4380eb4` ×1, `5e010012` ×3; opcode 2s `020100000e14`, `020100000d14` | yes | exact counts |
| Prop 137 kind 2 group 7292 = `020100003d28` | yes | exact |
| Movable 72: static byte 36, (606, 3464), h 30, flags 0x0502, region 2490, stream 1 group 19666, dreamstone identity ×1 | yes | byte 32 = 0x24 = 36; exact |
| Opcode 198 writes slot 4 / 20 / 22 zero times across all 1062 groups | yes | full census: 0 occurrences each |

**Bottom line:** every id, group number, coordinate, flag, predicate, and command byte in STORY-066 that is checkable against `L14_HT.json` verifies exactly. Unverifiable-from-this-file claims are the item-1 dreamstone row (no item table), the arrival selector, region floor/ceiling/neighbors, the locals cstring, and the template/static name strings (only their numeric indexes are in the export). One soft mismatch: "u16 170 fits more than one table" — within the export's table sizes it fits only the prop table.

To resume this session: kimi -r session_96153c94-0d38-4981-885b-d2f5e962fe7b
