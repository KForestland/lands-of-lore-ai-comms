# Kimi K2 — verification of grok source_ids_066_075.md, STORY-067 + STORY-068 vs L16_CA.json

Run 2026-11-04 by Kimi Code CLI (read-only). Lead spot-checked: 2136 groups; group 4834 raw starts f00000004c00090372020800; extra opcode 9 command 090372020700 (u16 626, byte 4 = 7) exists.

| claim | found? | note |
| --- | --- | --- |
| Arrival selector 1 = (-3860, 1341), heading 1, region 137 | no | JSON has no arrival-selector table; byte pattern `ecf03d05` does not appear anywhere in the file |
| Region 233 record: descriptor 2, list 40, kind 12, raw `080c3402e9000200`, stream 0, group 564 | yes | exact match in `region_lists` (list_offset 40, descriptors [2], group 564, stream 0) |
| Group 564 header `f00000000200` | yes | matches `header_hex` |
| Child opcode 21 `1503a8021b00` (u16 680, byte 4 = 27, byte 5 = 0) | yes | decodes as claimed |
| Child opcode 18 `120100002bf10df7000004080080000a0000`, byte+1 = 1, u16@+2 = 0, words (-3797, -2291, 0), flags 0x0804, heading 32768 | yes | all five decoded values match the stored bytes |
| Control 78: stored (-3848, 1201), height 1, region 0, flags 0x0482, slot 66 | yes | all fields in `placement_hex`; trailing slot byte 0x42 = 66. The name "Trigger plate" is not in the JSON |
| Region 0 floor 0, ceiling 256, neighbors 233/137/205/209 | no | region geometry (floor/ceiling/neighbors) is not exported in this JSON at all |
| Kind 5 groups 42098 (value 4) and 42116 (value 5) on control 78, with opcode 16 `1010c2000000` / `1010c2000100` and opcode 9 `0910c2001500`, u16 194 | yes | events and both group raws match byte-for-byte |
| Controls number 326; u16 194 fits a control and also a prop | yes | `counts.object_tables.control` = 326; prop table = 681, so 194 fits both |
| Control 194: stored (-3849, 1163), height -2, region 0, flags 0x0482; groups 49010, 49034, 49058, 49064; children only opcode 7 and opcode 9 on u16 194; no opcode 2/18 | yes | placement matches (slot byte 0x11 = 17); the four group raws contain only opcodes 7/9 on 0x00C2 = 194. Name "door" not in JSON |
| Control 74: stored (2100, -4296), region 9615, level change `020100001c31` | yes | placement matches; its group 42056 is exactly `020100001c31`. Name "Telepad" and the neighbor claim are not checkable here |
| Bottom line: 2136 groups; opcode 198 writes slot 0 ("Star_Elevator") zero times | yes (counts) / n/a (name) | groups = 2136; of 70 opcode-198 commands, zero have byte 4 = 0. The cstring itself is not in the JSON |

## STORY-068

| claim | found? | note |
| --- | --- | --- |
| Prop 626: stored (-4111, -15457), height 90, region 4900, flags 0x4682 | yes | all four fields match `placement_hex` (template word = 55). Floor 90 / ceiling 300 / neighbors 4899–4896 not checkable (no region geometry in JSON) |
| Opcode 198 `c60000001001` (u16 0, byte 4 = 16) on prop 626, and it is the one opcode-198 write on that prop | yes | in group 40538; no other prop-626 group contains opcode 198 |
| Local slot 16 = cstring `Ice_fountain_trigger` | no | the JSON contains no cstrings at all; name lives in GLOBAL.MIX |
| Opcode 2 `020100001800` and `020100000b05` in prop 626's groups, both outside the level-change shape | yes | group 40476 and group 40588 respectively; byte 4 is 0x18/0x0b, not 0x1c |
| No Ball O Smoke in region 4900 or its four neighbors | partly | region scan: only prop 626 sits in 4900 and nothing at all is placed in 4896–4899; prop 602 (Ball O Smoke per STORY-070) is in 6098. Consistent, but names aren't in the JSON |
| Prop 392 stored (-2201, -12864), region 3661 | yes | matches. Name "Oil fountain" not in JSON |
| Props 1–4 in region 6098, x 2230–2343, y 536–650 | yes | (2343,649), (2230,650), (2231,537), (2342,536), all region 6098. Name "Silverleaf fount" not in JSON |
| 14 Lichen props: ids 518, 521, 522, 527, 528, 533, 534, 539, 540, 545, 546, 551, 552, 557; height 15, flags 0x1402, x 1848–2733, y 240–938 | yes | all 14 exist and every one matches height, flags, and the coordinate band |
| Each lichen row carries opcode 3 `03010000cceb4dca04000000` (identity 0xCA4DEBCC, byte +8 = 4) | yes | found in a group of each of the 14 props |
| Definition 122, name slot `120-Black lichn`, handler 41 | no | definition/name-table data is GLOBAL.MIX material, absent from this JSON |
| Prop 518: stored (2053, 938), region 6360 | yes | matches |
| Prop 518 kind 4 group 22408, predicate 209, entry `0005000003`; children opcode 9 `090306021500` (u16 518, byte 4 = 21) + the opcode 3 | yes | event link, predicate entry, and both command raws match exactly |
| Prop 219: stored (-2403, -16035), height 0, region 9659, flags 0x0482, stream 1 group 4834 starting with opcode 9 on u16 626, byte 4 = 8 | yes | placement, event (kind 6, stream 1), and group 4834's first command `090372020800` all match; template word = 0 as claimed |
| "The other opcode 9 commands on that index are prop 626's own two, byte 4 = 16" | partly | 40476 and 40510 (both prop 626's, byte 4 = 16) confirmed — but there is also a third opcode 9 on u16 626: stream-0 group 3096, `090372020700` (byte 4 = 7), owned by prop 101, which the note omits |
| Props 600–603 template u16 61 | yes | placement word at +32 is 61 for all four |

**Bottom line:** Every byte-level claim in STORY-067 and STORY-068 that is actually represented in `L16_CA.json` — group numbers, raw command hex, event kinds/values, predicates, coordinates, heights, flags, regions, slots, template words, and the counts (326 controls, 2136 groups, 70 opcode-198 commands none writing slot 0, 14 lichen rows) — verifies exactly as written, with one small exception: the STORY-068 summary says prop 626's two byte-4=16 commands are "the other" opcode 9s on u16 626, but a third one exists (stream-0 group 3096, byte 4 = 7, on prop 101's event list). The claims that cannot be checked from this file are the name/cstring layer (Trigger plate, Telepad, Fountain, Lichen, `Ice_fountain_trigger`, `Star_Elevator`, definition 122 `120-Black lichn`), region geometry (floors, ceilings, neighbor lists), and the arrival-selector row — none of that data is exported in the JSON, so those statements are neither confirmed nor contradicted here.

To resume this session: kimi -r session_120ac12a-99fb-4cfa-9839-cad857813fdf
