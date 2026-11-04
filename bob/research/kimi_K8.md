## STORY-071

| claim | found? | note |
| --- | --- | --- |
| Prop 392 exists, stored (-2201, -12864), height -5, region 3661, flags 0x4402 | YES | placement_hex decodes exactly to these values |
| Region 3661 floor -5, ceiling 200, neighbors 3665/3662/3658/3649 | NOT IN FILE | region:3661 absent; no region descriptors in export |
| Prop 392 kind-9 event → group 14558 | YES | event (kind 9, group 14558, value 17) |
| g14558: op9 `090418000300` (u16 24, byte4=3) | YES | verbatim |
| g14558: op1 on 98, 81, 80, byte4=100 | YES | `012062006400` / `012051006400` / `012050006400` (0x64=100) |
| g14558: op198 `c60000000b01` (byte4=11) | YES | verbatim; it is the **only** op198 byte4=11 in the whole file |
| g14558: op9 u16 608 byte4=21; op9 u16 392 byte4=2 | YES | `090360021500`, `090388010200` |
| u16 24 fits prop/control/actor/movable tables | YES | prop:24, control:24, actor:24, movable:24 all exist (sizes 681/326/47/201) |
| Item 24 = Darkbow, identity 0xD58C34FE, def 35, handler 58, stored (-2546,-12858), region 3663, flags 0x1002 | NOT IN FILE | export has no item table; name/identity strings absent |
| Region 3663 floor/ceiling/neighbors 3620/3618/3665/3647 | NOT IN FILE | region:3663 absent |
| No opcode 3 of identity 0xD58C34FE on L16 | YES (confirmed) | bytes `fe348cd5` occur 0 times anywhere in the file |
| Fire Burst props 637–640, flags 0x1442, x -2624..-2620, y -12557..-13135, regions 3638/3618/3642/3647 | YES | all four placements decode exactly; names not in file |
| "Their command bodies were not copied" | PARTLY | props 637–640 do have event links to groups 40850–40940, and those groups exist in the file |
| Prop 638 in region 3618; prop 640 in region 3647 | YES | placement regions match |
| Movable 98 (684, -12855), height 155, region 10210, flags 0x0182, event 0 | YES | exact; no events on the object |
| Movables 80 (222,-13264), 81 (63,-13262) | YES | exact (flags are 0x0183, not claimed) |
| Movables 95/96/97 at x 1704, y -12841/-12891/-12791 | YES | exact |
| Prop 603 (429,-12857), region 6775, op18 words (1703,-12835,0), flags 0x0812 | YES | placement exact; group 37826 body `12035b02a706ddcd00001208…` = 603, 1703, -12835, 0, flags 0x0812 (placement flags are 0x1402; 0x0812 is the command-body field) |
| Local slot 11 = cstring Fire_puzzle_triggered; "no head cstring"; no "blue bow" row | NOT IN FILE | no cstrings or template names in export; op198 byte4=11 exists, the name binding is unverifiable |

## STORY-072

| claim | found? | note |
| --- | --- | --- |
| Prop 88 (-10576,750) h100 region 3851; prop 89 (-10442,1838) h125 region 4159; prop 90 (-8868,3286) h125 region 5833; all flags 0x4482 | YES | all three placements decode exactly |
| Region floor 100 / ceiling 500 for 3851/4159/5833 | NOT IN FILE | those region records absent |
| Each opens with op9 self byte4=8, op9 self byte4=18, then op16 | YES | groups 2208/2280/2352: `0903..000800`, `0903..001200`, `1003..000100` on targets 88/89/90 |
| Later group: op17 u16 91 byte4=1 and op9 u16 91 byte4=21 | YES | groups 2250/2322/2394: `11035b000100`, `09035b001500` |
| "U16 91 fits more than one table" | YES | fits prop/control/movable (not actor, size 47) |
| Props 89/90 then op9 self byte4=2; prop 88 has op7 byte4=1 instead | YES | g2322 `090359000200`, g2394 `09035a000200`, g2250 `070358000100` |
| Prop 600 (-9896,899) h115 flags 0x1402, region 5484 | YES | exact |
| Region 5484 floor/ceiling/neighbors 5492/5626/5476/5485 | NOT IN FILE | region:5484 absent |
| Prop 600 group 37622 op18 words (-9877,4536,0), flags 0x0812, raw `120358026bd9b81100001208000000280000` | YES | raw hex matches byte-for-byte; linked via kind-6 event |
| Movables 86/87/88 at (-9870,4533), (-9820,4533), (-9919,4533) | YES | exact |
| Prop 641 (-9897,841) h100 flags 0x0482, region 5484 | YES | exact |
| Prop 641 group 41010: op9 on prop 600, byte4=3 and byte4=21 | YES | `090358020300`, `090358021500` |
| Group 40946: op20 on prop 391; prop 391 at (-9859,3450) region 4313 | YES | two op20s target 391; placement exact ("Shape 3" name not in file) |
| Props 601 (-9797,-13070), 602, 603 not in region 5484 | YES | regions 6960, 6098, 6775; 602 at (2289,648) — "greenhouse" label unverifiable |
| No brick cstring | NOT IN FILE | no cstrings in export |

## STORY-073

| claim | found? | note |
| --- | --- | --- |
| Identity 0x042E0C09 exists | YES | LE bytes `090c2e04` appear 34 times in file, 10× in opcode-3 commands |
| Definition 107, name slot `105-Ivory chip`, handler 90 | NOT IN FILE | no item-definition data in export |
| Items 12/22/23 rows (coords, regions 10120/9653/7420, flags, events) | NOT IN FILE | no item table in export |
| Item 12 event 19098 = op9 u16 220 byte4=21 | NOT FOUND | group 19098 does not exist among the 2136 script groups |
| Region 7420 also holds items 3, 4, 10 | NOT IN FILE | no item table (prop 592's placement region is 7420, consistent with the story's aside) |
| Prop 220 (-5647,-4678), template Light Source | YES / name unverifiable | coords exact; no template names in file |
| Prop 223 group 6090, op3 ivory, byte+8=4 | YES | owner link kind-4→6090; `03010000090c2e0404000000` |
| Prop 399 group 14678, op3 ivory, byte+8=4 | YES | owner link kind-4→14678; same body |
| Prop 592 group 36430, four ivory op3 commands, byte+8=4 | YES | owner link kind-5→36430; group has 27 commands, exactly 4 carry `090c2e04` |
| Control 0 group 41082, op3 ivory, byte+8=4 | YES | owner link kind-4→41082 |
| Control 70 group 41716, op3 ivory, byte+8=4 | YES | owner link kind-4→41716 |
| Control 95 group 42334, op3 ivory, byte+8=4 | YES | owner link kind-4→42334 |
| Control 72 group 41878, op3 ivory, byte+8=1 | YES | owner link kind-4→41878; `03010000090c2e0401000000` |
| No opcode 3 of identity 0xCE20AEE3 (dreamstone) on L16 | YES (confirmed) | bytes `e3ae20ce` occur 0 times in the file |
| Local slot 5 = cstring How_many_tower_keys... | NOT IN FILE | no cstrings in export |
| No opcode 198 byte4=5 in the copied groups | YES (confirmed) | no op198 byte4=5 anywhere in the file |

The seven claimed ivory opcode-3 sites account for exactly all 10 opcode-3 commands carrying `090c2e04` in the export — no others exist.

**Summary:** Every concrete id, coordinate, flags value, group number, and raw opcode byte string named in STORY-071/072/073 verifies exactly against `L16_CA.json`, including the negative claims (no opcode 3 of 0xD58C34FE or 0xCE20AEE3, no op198 byte4=5, g14558 holding the sole op198 byte4=11). The only unverifiable parts are inherently absent from this export: item-table rows (items 3/4/10/12/22/23/24, incl. the missing group 19098), template/cstring names, and region floor/ceiling/neighbor data; one minor wrinkle is that Fire Burst props 637–640 do have linked script groups in the file despite the "not copied" remark.

