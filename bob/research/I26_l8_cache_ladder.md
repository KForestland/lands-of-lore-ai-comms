# I26 L8 cache ladder

Owner report 23-20-29, F10 (−1076, −2621), native (−1076, 2621). That point is region 678, floor −10, ceiling 390, bbox (−1110, 2486)–(−970, 2764). r14 `8732a39` has no ladder script under `scripts/lol2/l8_*.gd`. The triage is right that the port has no climb. No Godot was run.

## The click

Control 69 is stored at (−1034, 2606), height −10, flags `0x0482`, region 678. Static byte 32 is 32. The 30-byte name run at L8 file 13805419, name at byte 0, walks 52 names. Index 32 is `ladder`. That name join is LIKELY.

Its only event is kind 4, stream 1 group 12668, value 0, no predicate. The group is two commands:

- opcode 20 on u16 69, raw `141045000c0380000a14`. Not entered.
- opcode 18, raw `1201000014fc1e0a64000403a44f00320000`. Kind byte 1, target u16 0, signed words at +4, +6, and +8 are (−1004, 2590, 100). The flag word at +10 is `0x0304`. Bit `0x0004` is set, so this is the direct-relocation form. Bit `0x0100` is clear, so the third word was not classified as a height by that bit. The word at +12 is `0x4FA4`. The other flag bits were not re-proven. Target u16 0 was not named. The callee was not entered.

The destination xy (−1004, 2590) is region 657, floor 100, ceiling 390. The owner point and control 69 stay in region 678, floor −10, and that region has the same ceiling, 390. This is one hop from the low floor onto the floor-100 shelf. No other opcode 18 destination sits inside 800 units of the shaft.

## Nearby records that are not the hop

Props 1339, 1340, 1341, and 1342 are static slot 16, height 100, around the shaft. Each group is opcode 20, opcode 16, opcode 207, opcode 9, opcode 5, and opcode 6 on that prop. Those opcodes were not entered. They were not named as rungs. r14 `l8_tree.gd` uses these same prop indexes, plus prop 1338, as the five spark torches of the raised platform. That script is the torch stairs, not control 69.

The cache loot is the other cluster. Control 66 at (−1464, 2710), height 220, region 3740, is a separate click. One of its groups grants opcode 3 identity `0xD0421BDE`. That identity was not named. The circlet item row in `MAPS/L8_SJ/NOTES.md` stays the Brady loot row.

## The book

Brady printed 175 point 7 is the label "The Shaman's Treasure Cache." Printed 176 says a Crystal Shard is required to enter, and lists Kiernan's Circlet, Amaranth Serum, the War Blade, a scroll, and a Dampen Charm. Those pages do not say ladder. The book's "click the ladder" lines are the hive. Grade on the cache page is BRADY. The group bytes are the stored commands. Opcode 20 and the rest of opcode 18 stay unentered.

## Still open

Who target u16 0 is, what opcode 20 plays, what the slot-16 props do, and whether the shard gate is control 66. No frame was opened.
