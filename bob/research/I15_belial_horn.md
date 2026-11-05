# I15 Belial's horn

Place L19_BC. No frame was opened. No Godot was run. Template slot 9 is the cstring `Ooze pipe`. Template slot 2 is `Blood bowl`. Name-at-index stays LIKELY. Opcode 3's grant, opcode 9, opcode 21, and opcode 198 were not entered. Local slots are 41-byte records. Slot 9's cstring is `Level_entered`. The join from opcode 198 byte 4 to that slot stays unbound.

Hintbook lines 5410–5413: Baccata gives Belial's horn, tells Luther to save Dawn, and then dies. Keep the horn. Grade HINTBOOK. That gift is REQUIRED. Brady printed 142 names the Horn of Belial as a weapon in the final fight. That sentence is not the gift. Grade BRADY for the weapon line only.

## The grant

Prop 222, LIKELY Ooze pipe, is (120, −525), height 0, region 687. Godot (120, 525). Two kind-6 records, both value 9, store the horn identity.

| group | commands |
| --- | --- |
| 2778 | opcode 21 `152038004000` (u16 56, byte 4 = 64); opcode 3 `03010000902cbe0c01000000`; opcode 198 `c60000000901` (byte 4 = 9, byte 5 = 1); opcode 9 `09030d011500` (u16 269, byte 4 = 21) |
| 2814 | opcode 21 `152038003a00` (byte 4 = 58); opcode 198 byte 4 = 9, byte 5 = 1; opcode 9 `090220000300` (u16 32, byte 4 = 3); opcode 3 `03022000902cbe0c01000000` (target u16 32) |

Both opcode 3 commands carry identity `0x0CBE2C90`, bytes `902cbe0c`, and byte +8 = 1. GLOBAL file 5996755 holds that dword on definition 22, name slot `23-Hrn Belial`. The name stays LIKELY. The grant stays LIKELY. The geometry header dword at +0x6C is 0, so this pass found no placed item row for the horn.

Prop 269, LIKELY Blood bowl, is (13, 899), height −30, region 686. Godot (13, −899). It is the only prop 269. U16 269 does not fit another prop. U16 32 fits actor 32 and would also fit a prop or a control if one existed. Actor 32, definition u16 3, is (18, 596), region 616, one event. Region 616 is not region 687. The command does not say the actor is Baccata.

## What is not the giver

The MIX cstring `First time player enters: Good Bacatta` is not a placement name. No placement field read here is Baccata. Prop 223, the other Ooze pipe at (39, −526), same region 687, stores opcode 3 of the Darkbow identity `0xD58C34FE` with byte +8 = 4, among a list of other identities. That is not the horn.

## Still open

Who hands the horn over. Whether actor 32 is Baccata. Opcode 21 byte 4 as a scene name. The two predicate trailers, indexes 34 and 33. No frame.
