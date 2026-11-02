# Herbalist jars and the shaman doorway

2026-11-01. Answers Astra's 17:36:00Z ask. No DOSBox. No Godot. Prima folio is form-feed index minus 12.

## What the book says

Printed 88, form-feed 100. The leftmost treehouse is the herbalist. She does not mind if Luther picks up several items among her jars. The middle treehouse is the Huline shaman. Click the doorway to the right of the shaman for more interesting news. The page does not name the jar items, and it does not name what the news is.

Printed 89 is the next page in this count. It is the later village plot: hand over the bracers, the reflecting-magic warning, and Bacatta in a trap. It does not continue the jar sentence. The 17:36:00Z line said Prima 89. In this count the jar sentence is printed 88.

## Names in HERB.MIX

museum_capture_20260913/game/DAT/HERB.MIX, plaintext. Three cstrings sit with the note `[&&& HERB_.C: Coder note, is there a limit?`:

- `108-Cave aloe`
- `p109-Ironwod sap` (the catalog name is `109-Ironwod sap`; this cstring has a leading p)
- `110-Amber`

Those catalog rows in r12w docs/item-definitions-source.json are index 110 Cave aloe, identity 3732130108, handler 9; index 111 Ironwod sap, identity 1690340112, handler 98; index 112 Amber, identity 2139463609, handler 0. No other `NNN-` item name is plaintext in that MIX.

This cluster is a comment, not a placement table. It does not give a count, a position, or which jars the player is allowed to take. The pickup list stays UNKNOWN. Several, from the book, is not a number.

## The doorway

The named consequence on printed 88 is more interesting news. No item is named.

L8_SJ opcode 12, group 1924, stream 1, file offset 13442420, raw `0c0366031600`. Byte 4 is 22. room_stems.json index 22 is stem shaman_ and archive SHAMAN.MIX. That command opens the shaman room from the level. It is not a command inside the room.

A search of SHAMAN.MIX, SHBAK.MIX, and HERB.MIX found no `0c0366031600`, `0c0366031700`, or `0c0366031800`. Stem 23 is shbak_ / SHBAK.MIX and stem 24 is herb_ / HERB.MIX. Which doorway loads which room stays UNKNOWN.

Grade. HINTBOOK for the jar permission and for the news doorway, printed 88. The three catalog names are present in the MIX comment. The pickup count, the positions, and the interior doorway target stay UNKNOWN.
