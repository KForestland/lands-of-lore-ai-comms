# R2 adapter review fork 08, 2026-11-05

No Godot was run. No opcode callee was entered. The idle line still names ~/opus_work/lol2_r12y at 56812f9. These rows were read in ~/opus_work/lol2_r15 at f6a5aa4. All seven row files match the r12y copies. `thieves_den.gd`, `thieves_den_rooms.gd`, `item_definitions.gd`, the staged item definitions, and the den rooms manifest match. `thieves_den_state.gd` differs by one journal hint sentence. That sentence is outside these rows.

## 0079 jungle den

The row file matches. After a TINT `movie_flags` value whose bits include 0x80, `thieves_den_state.gd` appends a Luther reply when that line's staged clip exists. DECODED.

The staged TINT reply keys are 22. The row counts 19. THIEVES_DEN_DECODE §6 names those 19 files. Keys 486, 498, and 556 are also staged. `thieves-den.md` says each of those three shares a hash with a requested Mauri line. That hash was not recomputed. LIKELY.

Playback byte 0xABB58 was not entered. The 0x80 reading stays the row's interpretation.

HINTBOOK lines 2338–2341 and 5679–5683 name the password and the thief's sword. BRADY lines 3041–3047, marker PDF PAGE 78, printed 77, and lines 3063–3074, marker PDF PAGE 79, printed 78, name the password, Muari, and Firestorm. Those sentences print no 19. Books print no such number.

The 19-file match is the more faithful count. A simpler build plays those 19 and leaves 486, 498, and 556 silent. The inserter plays every staged reply. What stays open is byte 0xABB58.

PROPOSE Skip den replies 486 498 556 | row 0079 and the staged TINT reply set | a 0x80 line plays a reply only for the 19 named files.

## 0080 jungle den

The row file matches. Constants `TIMER_PRICE` 300 and `TIMER_FIRESTORM` 600 are still emitted. The price arm follows lines 554, 556, and 557 when the village is alert. The 600-tick arm follows the alert Firestorm scene and sets flag 18. DECODED.

Both effect names sit on the presentation drop list, so the saved clock never stores them. `tint_timer` only cancels a timer, and that handler is absent from HANDLERS. DECODED. No timeout runs.

Address 0x122F was not entered. The cancel stays the row's sentence.

HINTBOOK lines 5679–5686 and BRADY lines 3063–3074, printed 78, and lines 6739–6741, marker PDF PAGE 158, printed 157, name the kill and the tunnel. Those sentences print no 300 and no 600. Books print no such number.

The adapter stays the row. No printed source is more faithful. No simpler timeout is sitting in the host. What stays open is any native expiry past that cancel.

## 0081 jungle den

The row file matches. `is_magic_item` reads staged definition byte 0x43 bit 0 through `item_definitions.raw_byte`. That bit is set on 24 records, including 9-Firestorm and 147-SumScrl. DECODED.

`tint_offer` takes a held item when the bit is set and the state bit is clear. Flag 19 then plays the tunnel. Any other accepted offer plays line 505 and the item is still consumed. The offer call passes the state bit as false. A non-magic held item produces no effects, so the script does not start. An empty hand plays line 504. DECODED.

Slot 0xA4, array 0x96908, and allocation 0x5C548 were not entered. The writers stay the row's gap.

BRADY lines 3073–3074, printed 78: the tunnel requires killing Kelsrick or giving Muari something valuable. HINTBOOK lines 2338–2341: the thief route gets something nice without paying. Those stay two sentences. Both print no 24. Books print no such number.

The adapter stays the row. No printed list replaces the 24. What stays open is the state-bit writers.

## 0082 jungle den

The row file matches. With Met_Confidant clear, a wrong door answer steps the saved LCG once and takes the seed modulo 4. Draw 0 plays line 509, draw 1 plays 510, and any other draw plays 511. The seed starts at 20261027. The multiplier 1103515245, the addend 12345, and the mask 0x7fffffff match `liz_room_responses.gd` and `magic_shop_state.gd`. DECODED.

`add_fighting_xp(100)` runs once in the Firestorm scene, with flags 63 and 308. The draws go through `hive_rune_transaction.draws` from reward seed 324508639, and the host stores the seed the award leaves. DECODED. That LCG is the same adapter class as the LIZ and Rashar responses.

The row names the call at TDOOR 0x5B6. The host comment names TDOOR 0x5C6. The call was not entered. Both addresses stay the row's gap.

HINTBOOK lines 5679–5681: hear the password, then try the door that needs it. BRADY lines 3041–3045, printed 77: a shady character gives the password, and it opens a cellar door where you meet Muari. Those sentences print no 0..3 and no 100. Books print no such number.

The adapter stays the row. No printed draw replaces the LCG. Cross-room RNG order stays unclaimed. What stays open is the unread call site.

## 0083 jungle den

The row file matches. An OptionButton stands in for the held item. Magic items are listed first. Empty hand is the first entry. A click on Mauri's actor rect calls `offer_item`, message 5, which is `tint_offer`. DECODED.

Back and Escape call leave, callback 8. F sends message 7 and Q sends message 6. `attack` runs only while the open room is TINT, and both messages start `tint_attack`. `monastery_rooms.gd` uses the same 7/6 pair, and the library gate is room MLIB. `magic_shop_rooms.gd` has the same selector. Its key handler covers F5 and F9. DECODED.

HINTBOOK lines 2348–2349: move the conversation with mouse-clicks, and do not start an attack by accident. The Brady den pages print no F, no Q, and no selector. Books print no such number.

The adapter stays the row. No printed control is more faithful. The original held-item cursor stays unopened. What stays open is that cursor path.

## 0084 jungle den

The row file matches. Hotspot 5 is the coin click at TINT callback 0x73C. The first click in a visit sets flag 20 and plays 993, 506, and 992. The next click plays 993 and 994 and `exit_room`, with no place. Each TINT first update clears flag 20. DECODED.

Damon's attack, messages 6 and 7 while flag 27 is clear, sets flag 27, plays those same two lines, applies `damage(-1)`, and `exit_room`, with no place. The port sets health to 0. Address 0x9F4 was not entered. Closing the chain restores the world at the current position and sets the entrance latch from current contact. Region 3642 opens on a rising edge. DECODED.

HINTBOOK lines 2348–2349 warn against an accidental attack. BRADY line 6732, printed 157: taking weapons from Muari brings his bodyguard. Those stay two sentences. They print no -1, no 993, and no 3642. Books print no such number.

The adapter stays the row. No printed placement is more faithful. No simpler exit adds a place. What stays open is the death routine past health 0. The port sets health to 0 and shows the R/F9 line.

## 0085 jungle den

The row file matches. `tdoor_click` still emits `sfx` 388 at volume 150 for a knock and `sfx` 394 at volume 200 for a refusal. Yard setup still emits ambient 351. The cursor hide and show effects are emitted around the door and the attack. All of those names sit on the presentation drop list, so the room layer never plays them. DECODED.

No walk handler plays 384, 385, 386, or 387. Callback 11 is not a function in the three room scripts. Clip 3199106E is an archive name in `thieves_den_source.json` and is not requested by those scripts. DECODED.

The TDOOR actor rect is still 0, 31, 0, 0, 5, 5 in the click router. A hit there returns the npc, and the click stops, because the offer runs only in TINT. The door hotspot starts at x 147. The voice clip stays unplayed.

The den passages in both books print no 388, no 394, no 351, and no 384. Books print no such number.

The unplayed sounds stay the row. A simpler build omits that 5 by 5 rect from the router. What stays open is a traced consumer for the rect and for clip 3199106E.

## Receipts

- 0079 jungle den: Staged TINT replies are 22 keys and the inserter plays each non-empty 0x80 clip. The row's faithful count is 19 files. Byte 0xABB58 stays unread. Books print no 19.
- 0080 jungle den: Price and Firestorm arm 300 and 600 tick timers that the host drops, and callback 10 only cancels. No timeout runs. Books print no 300 and no 600.
- 0081 jungle den: Payment accepts the 24 staged definitions with byte 0x43 bit 0 set and forces the state bit clear, so a non-magic offer starts no line. Writers of that bit stay unread. Books print no 24.
- 0082 jungle den: The wrong door answer and the 100 fighting draws use a saved per-room LCG of the LIZ and Rashar class. Call sites 0x5B6 and 0x5C6 stay unread. Books print no 0..3 and no 100.
- 0083 jungle den: A hand selector offers the held item to Mauri, Back and Escape leave, and F and Q send attack messages 7 and 6 inside TINT, as in the library. Books print no such keys.
- 0084 jungle den: A second coin click and Damon's attack close the den with no placement and leave Luther in region 3642 until he steps out and back. Books print no -1 and no 3642.
- 0085 jungle den: Knock, refusal, walk sounds, yard ambient, and the cursor view calls stay unplayed, and clip 3199106E stays unrequested. The 5 by 5 door rect still swallows a corner click. Books print no such sound ids.
