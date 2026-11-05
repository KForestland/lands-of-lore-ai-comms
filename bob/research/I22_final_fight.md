# I22 faux-Draracle and the final fight

Place L20_BB. No frame was opened. No Godot was run. Static name-at-index stays LIKELY. Opcode 1, 2, 3, 8, 9, 13, 14, 16, 20, and 22 were not entered. The definition field is the u16 at byte 32. A low byte that matches a short label was not used as the definition.

Hintbook lines 5535–5568: Belial raises a faux-Draracle. The Dark Sword works. Force the next door, save, then force the last door. Belial speaks. The blue bow, the Dark Sword, and Belial's horn have the same effect, and one blow starts the chasm scene. He vows never to return and slumps. Lines 5574–5576: the last video is Luther with Dawn, and the Draracle appears and vanishes. Grade HINTBOOK. The fight and the two doors are REQUIRED. The three-weapons sentence is the book's, not a measured tie.

Brady printed 142: with the Ruby of Truth, a good Luther dispels the Draracle's image. An evil Luther meets the real Draracle after Belial. Darkstorm and the Horn of Belial are potent, and Dragonscale armor matters. A spectral image may appear at the very end. Grade BRADY. That good/evil split, and "potent" rather than "the same effect," stay off the hintbook sentences.

## Doors and keys

Controls 0, 1, and 2 are static slot 17, `Crystal Key`. Each kind-4 group stores opcode 1 with byte 4 = 100 on a pair of u16s, and opcode 2 `020100001800`, which is outside the level-change shape.

| key | native | Godot | region | opcode 1 u16s |
| --- | --- | --- | --- | --- |
| 0 | (−4636, 4913) | (−4636, −4913) | 842 | 51, 50 |
| 1 | (−3485, 4749) | (−3485, −4749) | 804 | 53, 54 |
| 2 | (−1043, 3120) | (−1043, −3120) | 417 | 99, 55 |

Movable 51, static slot 1 `R door`, is (−4731, 4876), region 871. Movable 50, slot 2 `L door`, is (−4731, 4826), the same region. Movables 53 and 54 are `L door` and `R door` at (−3579, 4754) and (−3529, 4754), region 812. Movables 55 and 99 are `L door` and `R door` at (−1055, 3237) and (−1055, 3187), region 218. Those indexes also fit other tables. Movable 52, static slot 10 `Final gateway`, is (−3554, 4740), region 795. Its only command is opcode 14. No key's opcode 1 names 52.

## The two actors

Actor 46, definition u16 1280, is (−6921, 4828), height −50, region 1272. Godot (−6921, −4828). Nineteen events. The opcode tally is 9, 13, 16, 22, 8, and 2. There is no opcode 1 and no opcode 3. The cstring `DRARACLE` was not joined to definition 1280.

Actor 75, definition u16 1282, is (−1238, 3207), height −10, region 177. Godot (−1238, −3207). It is the only actor with that u16. Its groups store opcode 1 on u16 55 and 99 with byte 4 = 100 and with byte 4 = 0, the same pair key 2 names. They also store three opcode 3 commands, identity 0xE0649CBA, byte +8 = 1, on u16 557, 556, and 555. That identity is definition 68. The prior item table's name slot is `66-Ancients stn`. The name was not re-read from the name record, and the grant stays LIKELY.

## Weapons

No L20 opcode 3 contains the horn identity `902cbe0c`, the darkbow identity `fe348cd5`, or the ruby identity `d784f8fb`. Definition 21's identity `ff1cfe64` occurs once, on prop 241 group 7410, in `03010000ff1cfe6401000000` (target 0, byte +8 = 1), among a list of other opcode 3s. GLOBAL file 5996664 holds those bytes. The name at file 6015597 is `22-Darkstorm`. The name and the grant stay LIKELY. Prop 241 is the Crystal at (−2135, 3706). It is not actor 75.

The chasm, the slump, and the last video stay the book. No command copied here names a VQA.

## Still open

Which actor is the faux-Draracle. Which door is the last one. Whether one weapon differs from another. The chasm. The ending movie's filename. No frame.
