# H22 The ball over the southern dry fountain

L16_CA.MIX sha256 prefix `810d39ae20a980c4`. JSON is the act3 export. Template names are the 38-byte table whose index 55 is the cstring `Fountain` and whose index 61 is `Ball O Smoke`. That alignment is LIKELY. Opcode 9, opcode 5, opcode 7, opcode 204, and left kind 5 were not entered. No longplay frame was opened.

## Prop 626 is the freeze fountain

Prop 626 is the only template-55 row. Native (−4111, −15457), height 90, flags `0x4682`, region 4900. That region’s center is (−4110.5, −15457), floor 90, ceiling 300. Godot y is 15457. No Ball O Smoke sits in region 4900. Props 600–603 are the four template-61 rows and they are elsewhere. Region 6098 is the greenhouse.

The only opcode 198 whose byte 4 is 16 is stream 1 group 40538, file 18695484, MIX match, on this prop. The command is `c60000001001`: store 1 at local index 16. The 41-byte local run that starts at `Star_Elevator` puts `Ice_fountain_trigger` at slot 16. Group 40640, predicate `0005000004`, is `0903dd001500` (opcode 9, byte 4 = 21, u16 221), then opcode 5 and opcode 16 on 626. U16 221 fits only a prop. Prop 221 is the light at (−3767, −15326), region 4968, the neighbor basin. Opcode 9 was not entered, so byte 21 is not a call of that light’s group.

## The ball

Prop 210, template u16 5 (`Floating Chaos Orb`), native (440, −10438), height 85, flags `0x0002`, region 9806. Godot (440, 10438). Region 9806 is the pad under it: center (438.5, −10436), floor 50, ceiling 350, about 77 by 104, neighbors 9805, 9804, 9803, 9802. The orb is 35 above that floor. It has no events. No command in this export uses u16 210. A second template-5 row, prop 665 at (−3315, −3357), also has no events and is not on this pad.

The scripted object on the same pad is prop 96, template u16 122 (`Stone cb`), (415, −10438), height 75, flags `0x0402`, region 9806. Its one record is kind 4, group 2826, file 18657772, MIX match:

- opcode 1, byte 4 = 0, on u16 56 and u16 57
- opcode 3 `030100001d4e0ef404000000`, identity `0xF40E4E1D`, byte 8 = 4
- opcode 9, byte 4 = 2, on u16 96

Movables 56 and 57 are (371, −10402) and (371, −10467), height 50, region 9805, and they have no events. U16 56 and 57 also fit other tables. The identity is not `0xCA4DEBCC`. GLOBAL.MIX holds the dword once and no name cstring was read off that record.

Brady 5303–5312 says the dry fountain is at the end of the north-south street at the extreme south, a sphere floats over it, and Mist of Doom then a sword shatters it. Hintbook 4800–4814 says the same street, a raised pad, destroy the ball, water returns, black lichen grows. No command on prop 210 or prop 96 is a spell. The shatter stays the book sentence.

## What writes the water local

One command stores local index 3. Stream 1 group 5898, file 18660844, MIX match, kind 6 value 20 on prop 221: opcode 9 byte 4 = 21 on u16 617, then `c60000000301`, then 21 opcode 204s, then opcode 9 byte 4 = 21 on u16 219. `c60000000301` stores 1 at local index 3. Slot 3 of the same run is the cstring `Has_Water_been_started`. Opcode 204 was not entered. The region u16s are 4948, 4946, 4955, 4964, 4963, 4960, 4952, 4956, 4951, 4957, 4895, 4950, 4906, 4907, 4905, 4908, 4902, 4903, 4904, 4901, and 4900. Region 4900 is prop 626’s pad. Each opcode 204 tail in this group is `ffff2b00`.

Nothing in the southern-pad groups names prop 221 or writes local 3. The water store sits in the ice-fountain basin. The byte that names prop 221 from prop 626 was not entered.

Readers of that local, predicate bytes only: prop 607 at (−2355, −13447) has kind 6 value 20 groups 38172 (`0003030000`) and 38340 (`0003030001`). Both are nine opcode 18s. Flag word `0x0008` on the first command of 38172 does not include `0x0004`, so that command is not the direct-relocation case. Control 189 at (−2715, −12848) has group 48954 on `0003030000`. Left kind 3 index 3 is the local read already entered for that predicate shape. The compared byte is 0 or 1 as written in the record.

## Black lichen outside the greenhouse

The 14 template-72 rows stay in x 1848–2733, y 240–938. They are not these.

Props 265 through 329 are 65 rows, template u16 108 (`Lick Pik`), flags `0x0402`, height 90 (47 rows) or 95 (18 rows). Stored x runs −5066 to 3860 and y runs −15765 to 67, which includes the ice-fountain basin (prop 315 is (−3486, −15577), region 4968). Each has a kind-4 record with predicate `0005000002`. Prop 265’s group 6770, file 18661716, MIX match, is the pattern: opcode 3 `03010000cceb4dca04000000` (identity `0xCA4DEBCC`, byte 8 = 4), opcode 16 byte 4 = 3, opcode 5, opcode 7, all on u16 265. The other 64 groups are the same four opcodes on their own index. Left kind 5 was not entered, so the predicate is not named “state 2.”

On the same prop, predicate `0005000000` kind 2 group 6712 is opcode 14 byte 4 = 4 on itself, opcode 14 byte 4 = 3 on the next index, then opcode 16 byte 4 = 1 on itself. Predicate `0005000001` kind 6 value 2 group 6752 is opcode 16 byte 4 = 2 on itself. That is the write that the grant’s predicate byte can see. Arms 3 and 4 were not closed. No one group sets all 65. The book’s nine was not reduced: 65 of these grants, plus the 14 greenhouse grants.

## Required

Brady 8794–8796: turn the south fountain’s water on before the arboretum and before the southeast firewall. That is the step the book marks required. The orb’s own hit group is still missing.

## Grades

HINTBOOK 4800–4814 and BRADY 5303–5312 for the sphere, the freeze, and the lichen. BRADY 8794–8796 for required. DECODED for prop 210’s placement and empty list, prop 96 group 2826, prop 626 group 40538’s slot-16 store, group 5898’s slot-3 store, and the 65 `0xCA4DEBCC` grants on props 265–329. The command that destroys prop 210, the spell, opcode 204, and a frame stay open.
