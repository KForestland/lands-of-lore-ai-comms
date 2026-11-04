# H08 Dawn's rune copy and Julian's Power Orb

Beat 49. Jungle and Hive exits. `L4_HJ.MIX` and `L4_HJ.json`. Opcode 2 and the item-grant callee were not entered. No level MIX in `DAT/L*.MIX` contains the bytes `Julian`.

No new owner F10 after `TRIAGE_20261103.md`.

## What the player hands over

Two wax impressions of the runes, made in the Hive (H02). One goes to Dawn. One goes to Julian.

HINTBOOK 2387-2397: on the way out of the Hive you meet Dawn and give her a copy. Back at the Monastery, speak with Dawn in the library, then hand Julian the second copy. He gives a Power Orb.

HINTBOOK 2701-2704: as soon as you see the jungle light, Dawn is waiting. Give her a copy. That is all the Hive requires.

BRADY lines 7306-7317: outside the cave mouth, give Dawn one copy. In the library she translates it and, when you leave, gives a Dampening Spell Charm. Then Julian takes the remaining impression, gives a different translation, and offers a Power Orb. Take it.

The charm and the orb are two gifts in Brady. The hintbook names only the Power Orb, from Julian. They were not merged.

## Dawn at the cave mouth

Actor 63 is at (-5710, -3937), height -100, region 2888, definition u16 9480. Static slot 56 at file 13286505 is `Dawn after Hive Cave`. The actor's own static byte was not read (actors store a definition, not that static slot). The name is the level's static table.

Region 2842, floor -100, center about (-5838, -4106), kind 12 group 5246 (file 13028224) runs on predicate `0604a1049e`. The group:

- opcode 9 on actor 63
- opcode 198 `c60000001301` sets local slot 19 to 1
- opcode 8 twice on actor 63
- opcode 2 `020100002600` (arm 0x26) and opcode 2 on actor 63
- opcode 18 words (-5761, -4004, 0), flags 0x0092

Slot 19, counting from `villager` at file 13153135, is `Has_Dawn_been_triggered` (file 13153914). This is the arrival speech trigger. Bit 0x0004 is clear on the opcode 18, so the pose is those words only.

Her kind-4 value-3 group 29704 (file 12758008) runs when predicate `0003110000` passes. That is local slot 17 equal to 0. Slot 17 at file 13153832 is `Gave_Dawn_Runes`. The group sets it to 1 (`c60000001101`), opcode 2 arms `0b05`, `0c05`, and `18`, and opcode 16 sets actor 63's state to 3. The click that hands her the copy is this group. Which inventory row it removes was not entered.

## The orb

Julian's Power Orb is the book reward for the second impression (HINTBOOK 2395-2397, BRADY 7315-7317). No Julian placement and no orb-grant group were in the jungle file under that name. The library visit is a later scene. `Kityara_Given_Orb` (H06, slot 23) is the later trade, after this orb exists.

## Required or optional

REQUIRED. The two copies are the Hive's required product (HINTBOOK 2703-2704, BRADY 7306-7317). The Power Orb is what you then trade at the armorer for Firestorm, or spend repairing the museum sword (HINTBOOK 2405-2407). Brady's Dampening Spell Charm is the library gift. The must-do lines name the orb, not the charm.

## Frame

No longplay frame was opened.

## Still open

- The inventory row removed by group 29704, and the row Julian adds for the orb.
- Which level holds the library Dawn and Julian. `Julian` is not a cstring in the level MIX files that were scanned.
- Predicate `0604a1049e` on the arrival region. Operator 6 is the G76 both-nonzero reading. The two sides were not entered.
- A longplay frame of the cave-mouth handoff.

Grades: actor 63, region 2842, both local names, and both group byte strings are DECODED. The two copies, the charm, and the orb are HINTBOOK and BRADY as cited. The frame is open.
