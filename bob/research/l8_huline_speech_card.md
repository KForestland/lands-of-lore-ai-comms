# PT-L8-HULINE-SPEECH card

Grade DECODED except where a line says otherwise. No Godot. Name table not re-read. Kind 8 was not entered, so its value is not a clip index.

## Hosted backroom, clips 225–237

`l8_backroom.gd` sequences are `[225–235]`, `[236]`, `[237]`. The manifest filenames match the entered `WOMS\%s\%02d%03d%02d%c` shape: stem, speaker, line, view, then `E`. View is 11 on all thirteen.

| line | stem | speaker | file |
|---|---|---|---|
| 225 | SHAMAN | 01 | AUD |
| 226, 227 | SHAMAN | 42 | VQA |
| 228–232 | SHBAK | 42 | VQA |
| 233, 234 | SHBAK | 01 | AUD |
| 235 | SHBAK | 42 | VQA |
| 236, 237 | SHAMAN | 42 | VQA |

That slice is the shaman doorway. It does not list the other villagers.

## Original L8 commands

L8 has four opcode-21 commands. Byte 4 is 12, 37, 30, and 80. None of those is a line 225–237. Owners: region 908 group 564, region 3132 group 1670, region 3277 group 1908, and actor 93 kind 5 value 16 group 19486 (`15032c065000`, byte 4 = 80, target 1580). The same group’s opcode 2 is `020100003900`, which is not a level change.

Kind-8 values that fall inside 225–237 belong only to actor 93: value 229 group 18566, value 237 group 18582. Both groups are opcode 20, the entered sound command. Selector is the u16 at byte 4.

| actor | event | group | selector | volume | flags |
|---|---|---|---|---|---|
| 93 | kind 8 value 229 | 18566 | 237 | 128 | 0x41 |
| 93 | kind 8 value 237 | 18582 | 1010 | 128 | 0x41 |
| 93 | kind 8 value 241 | 18542 | 997 | 1 | 0x41 |
| 93 | kind 8 value 241 | 18598 | 1010 | 128 | 0x81 |
| 93 | kind 6 value 0 | 18488 | 1010 | 120 | 0x00 |
| 93 | kind 6 value 0 | 18518 | 1009 | 200 | 0x91 |
| 93 | kind 6 value 0 | 18710 | 1011 | 128 | 0x81 |
| 93 | kind 6 value 0 | 18806 | 279 | 140 | 0x41 |
| 92 | kind 6 value 0 | 17970 | 1012 | 128 | 0x81 |
| 93 | kind 8 value 23, opcode-20 index 92 | 18830 | 1011 | 128 | 0x04 |
| 23 | kind 8 value 247 | 15636 | 1016 | 128 | 0xC1 |
| 23 | kind 8 value 250 | 15834 | 1019 | 128 | 0xC1 |
| 23 | kind 8 value 251 | 15844 | 1020 | 128 | 0xC1 |
| 23 | kind 6 value 0 | 15606 | 1015 | 128 | 0xE1 |
| 23 | kind 6 value 0 | 15804 | 1018 | 128 | 0xC1 |
| 82 | same selectors 1015, 1016, 1018, 1019, 1020 | 17254, 17284, 17454, 17484, 17494 | those five | see raw `ff`/`ffdd` tails | flags differ from actor 23 |

Actor 113’s kind 6 value 20 group 19832 is opcode 20 `14037f049d0180111532`: kind byte 3, index 1151, selector 413. The command does not name actor 113. Actor 81 and actor 20 have no opcode 20 or 21 in their own groups.

Selector 237 and WOM line 237 are the same integer in two tables. They were not joined. Deviation `0209` already calls actor 93 Daniel, actor 113 the guard, and actors 81 and 92 the companions. Those names were not re-read from the name table.

## The report point

F10 native (−3982.58, 1142.37). Actor 93’s stored int16 pair is (−3854, −1190). The port’s published point flips that y to 1190. Distance from the report to (−3854, 1190) is 137 units. The report was not bound to the actor.
