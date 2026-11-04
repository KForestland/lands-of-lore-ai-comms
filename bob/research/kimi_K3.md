# Kimi K3 — verification of grok source_ids_066_075.md, STORY-069 + STORY-070 vs L16_CA.json

Run 2026-11-04 by Kimi Code CLI (read-only). Lead spot-checked: groups 42062, 45160, 37758, 40684 present.

| claim | found? | note |
|---|---|---|
| Props 489/490/491/492 at (14872,-6468)/(13228,-4877)/(11619,-6485)/(13236,-8104), regions 6463/6513/6017/6004, height 0, flags 0x1402 | YES | exact on all four; all template u16 56 |
| Controls 111/109/110/112 = Iris Door slot 52, height 0, flags 0x0402, same region as pylon | YES (numeric) | static byte 32 = 52 on all four; coords/regions exact; name "Iris Door" not in export |
| Iris groups 43060/42988/43024/43096, kind 6 value 20 | YES | each is a kind-6 value-20 event of the stated control, stream 1 |
| Iris groups contain opcode 9 on pylon index byte 4 = 3, opcode 9 on Pylon Light, opcode 18 words ≈ pylon coords, flags 0x0912 | YES | e.g. 43060: `0903e9010300` (489), `1203e901173ab6e6…1209…` = (14871,-6474,0) flags 0x0912, `0903c2010300` (450); words exact on all four |
| Lights are props 450/449/448/451 "stored on the same four coordinates" | PARTIAL | all four template u16 95 in the right regions, but coords differ by 1–4 units (e.g. 14869,-6475 vs pylon 14872,-6468), not identical |
| Pylon kind-4 groups 20286/20344/20402/20460 = opcode 16, opcode 20, opcode 9 u16 445 byte 4 = 21, opcode 5 | YES | raw sequence `1003…`, `1403…`, `0903bd011500`, `0503…` on all four |
| Prop 445 = Altar at (19999,-6490) | YES (numeric) | coords exact; template u16 0 (= "Altar" per the doc's own Resolved name table; name not in export) |
| Later kind 6 on each pylon = opcode 9 on itself byte 4 = 2 | YES | groups 20338/20396/20454/20512, each `0903…0200` self-targeted |
| Prop 615 = Tower, (13273,-6464), h -999, region 6517, flags 0x0002, event 0 | YES (numeric) | exact; events list empty; unique template u16 57; name not in export |
| No movable with x 11000–16000, y -9000…-4000 | YES | zero movables in that box |
| Push/Pull controls 71 and 108 near (-5200,-1500) | YES (numeric) | (-5214,-1470) and (-5250,-1641), both static byte 53 |
| Fifth Tower Pylon prop 595, (2293,171), region 6114 | YES (numeric) | exact; same template u16 56 as the four pylons |
| Region ceilings 5000 / region 6517 floor -1000, ceiling 5000 | NOT VERIFIABLE | region geometry is not in this export (only 125 event-bearing region records) |
| "No box cstring"; Tower Hole / Teleporter / heaven stair / Staged Button zero placements | NOT VERIFIABLE | export contains no name strings at all |
| Resolved: opcode 198 writes slots 6,7,8,9 zero times | YES | byte-4 histogram over all 70 opcode-198 commands: no 6/7/8/9 |

### STORY-070

| claim | found? | note |
|---|---|---|
| Region 6098 holds props 1–4, prop 602 (2289,648) h18, prop 605 (2287,599) h-15, control 75 (2287,593) h4 flags 0x0482 | YES | all placements exact, all region 6098; props 1–4 at (2230–2343, 536–650), template u16 135 |
| Region 6098 floor 3, ceiling 375, neighbors 6097/6096/6095/6094 | NOT VERIFIABLE | no region geometry in export |
| Control 75 kind-4 group 42062, body ends `017a340e`; children `09104b000e00`, `020100001800`, `05035d020400`, `10035d020100` | YES | event raw `0a044ea40300017a340e`; group commands exactly as listed, in order |
| Control 75 kind-8 group 42092 = `090353020d00` (u16 595, byte 4 = 13) | YES | group body is exactly that command |
| U16 595 fits only a prop | YES | 595 ≥ actor/control/movable table sizes (47/326/201), < 681 props |
| Prop 605 group 38056 = opcode 9 on 602 (byte 4 = 3, 21), then opcode 16 + opcode 5 on 605 | YES | `09035a020300`, `09035a021500`, `10035d020300`, `05035d020e00` |
| Prop 605 group 37986 = opcode 14 + opcode 198 `c60000001701` (byte 4 = 23) | YES | exact; local-slot name "Silverleaf_clue" not in export |
| Prop 627 = Hourglass, (2293,1070), h45, region 6088 | YES (numeric) | exact; template u16 8; region floor/neighbors unverifiable |
| Group 40684 = opcode 20 + opcode 9 on 605, then opcode 9 byte 4 = 21 on 502–508,515,514,513,512,511,510,509 in that order; no opcode 198 | YES | 16 commands, exact target order `f601…fc01, 0302…fd01` wait — decoded: 502–508 then 515→509 descending, all byte 4 = 0x15; no `c6` present |
| Props 502–515 all Altar; x=1152 for 502–508 (y 960→192), x=3392 for 509–515 (y 192→1024) | YES (numeric) | all template u16 0; coordinates exact (y step 128) |
| Prop 602 group 37758 = opcode 18 raw `12035a02f208870b00001208000000280000`, words (2290,2951,0), flags 0x0812, heading 0 | YES | byte-exact |
| Movables 92/93/94 FireWall Door at (2242/2342/2292, 2947) | YES (numeric) | exact coords; static byte 44, same as STORY-072's FireWall movables 86–88; name not in export |
| 14 Puddle controls slot 47: 148–158 + 160–162 | YES | all 14 exist with static byte 47; control 148 at (1923,247) region 6302 exact |
| Puddle controls "share those lichen regions" | PARTIAL | only 10 of 14 puddle regions match a lichen region (lichen-only: 6200, 6213, 6357, 6360; puddle-only: 6242, 6249, 6376, 6377) |
| Control 148 kind-4 group 45160 ends in identity 0xCA4DEBCC, child opcode 9 = u16 527 byte 4 = 3; other tails incl. 0xBFDDCCA3 | YES | the identity is the tail of the kind-4 **event record** (`0a0468b00300cceb4dca`), not the F0 group body; group 45160 does contain `09030f020300` (527, byte 4 = 3); 0xBFDDCCA3 tails the group-45088 event record |
| Opcode 198 on control 148 "byte 4 = 4 and later byte 4 = 0" | WORDING SLIP | actual bytes are `c60000000401` and `c60000000400` → byte 4 = 4 both times, byte 5 = 1 then 0 (matches the doc's own Resolved wording) |
| 14 Watergate controls slot 48: 123–134 + 163–164, h≈77, x 1736–2840, y 223–985 | YES | all static byte 48; x range exactly 1736–2840, y 223–985, heights 74–77 |
| Resolved: opcode 198 byte 4 = 4 → 28 commands in 28 groups on exactly those 14 controls, each with byte 5 = 1 and 0 | YES | verified per-control: all 14 have both byte-5 variants |
| Resolved: opcode 198 writes slot 2 (Hourglass_on) zero times | YES | no byte-4 = 2 anywhere in the export |
| "No yellow cstring"; Bool / Bright Star / Big City / City Minature zero placements | NOT VERIFIABLE | no name strings in export |

**Bottom line:** Every id, coordinate, group number, and command byte that STORY-069 and STORY-070 actually pin down checks out against `L16_CA.json` — all eight pylon/iris placements, all eight cited groups' raw bytes (20286-series, 43060-series, 42062, 42092, 38056, 37986, 40684, 37758, 45160), the altar and puddle/watergate control inventories, and both Resolved-section opcode-198 tallies are byte-exact. The only substantive wobbles are two overstatements ("same four coordinates" for the Pylon Lights — off by 1–4 units; puddle controls "share those lichen regions" — only 10 of 14 overlap) and one mislabeled byte ("byte 4 = 0" should be "byte 5 = 0"). Everything name- or geometry-based (template/static cstrings, "no box/yellow cstring", zero-placement templates, region floor/ceiling/neighbors) is simply not present in this export and remains unverifiable here, consistent with the doc's own MIX-sourced caveat.
