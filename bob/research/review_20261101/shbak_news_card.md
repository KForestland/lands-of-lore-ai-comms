# SHBAK news

2026-11-01. Answers Astra's 18:44:26Z question: the player-visible news and consequence of the shaman back room. No DOSBox. No Godot. Prima folio is form-feed index minus 12. Brady printed 92 was read from the page image (PDF page 93).

## What the books print

Prima printed 88. Click the doorway to the right of the shaman for more interesting news. The page prints no sentence of that news and names no item from the doorway.

Brady printed 92, image-checked, section "Inside the Settlement". Talk to the Shaman. Daniel's hut is on the left. The herbalist's hut is on the right, and she says to find Malik. Malik's hut is in the center. Malik talks about Silverleaf, joining the tribe, and finding Silverleaf in the Dracoid Cemetery. If Luther has not attacked a Wild One, Malik gives the cemetery key. If he has, the key comes from Malik's corpse. That page does not mention a back room. Malik's Silverleaf speech stays the center-hut conversation. It is not the doorway text.

## What the doorway plays

Static read of the room DLLs. `WOMS\SHAMAN_.WOM` sha256 `f655c92f96aa2ca8ecb59a50d84d7cfed38e5a3736c8dc2b942efc4ead7eaab5`. `WOMS\SHBAK_.WOM` sha256 `53635de3d85cda4cf1b5f51c06f4e46ab332621a0f235a4fd09f7f439de37013`. Archives are the oracle-game `DAT/SHAMAN.MIX` and `DAT/SHBAK.MIX`. Each named clip below is an entry in that room's archive. Spoken English is not a cstring in either DLL.

Setup stores `GV_SHAMAN_DEAD` and the doorway test reads that stored value. Hotspot 1 is the doorway Astra joined to `SHBAK_`.

First click, shaman global 0, flag 215 clear:

1. Set flag 215.
2. Play `WOMS\SHAMAN\0122511E.AUD` (movie speaker 1, line 225, view 11).
3. Play `WOMS\SHAMAN\4222611E.VQA` (speaker 42, line 226, view 11).
4. Play `WOMS\SHAMAN\4222711E.VQA` (speaker 42, line 227, view 11).
5. Set flag 246.
6. Enter `SHBAK_`.

SHBAK's first update, same global still 0, hides the cursor and plays, in this order:

1. `WOMS\SHBAK\4222811E.VQA` (speaker 42, line 228, view 11)
2. `WOMS\SHBAK\4222911E.VQA` (speaker 42, line 229, view 11)
3. `WOMS\SHBAK\4223011E.VQA` (speaker 42, line 230, view 11)
4. `WOMS\SHBAK\4223111E.VQA` (speaker 42, line 231, view 11)
5. `WOMS\SHBAK\4223211E.VQA` (speaker 42, line 232, view 11)
6. `WOMS\SHBAK\0123311E.AUD` (speaker 1, line 233, view 11)
7. `WOMS\SHBAK\0123411E.AUD` (speaker 1, line 234, view 11)
8. `WOMS\SHBAK\4223511E.VQA` (speaker 42, line 235, view 11)

Then it loads `SHAMAN_`, shows the cursor, and leaves the back room. Neither DLL calls `give_item` on this path. Flag 215 is what stops the doorway from replaying the chain. SHBAK itself does not test flag 215.

Second doorway click, shaman global 0, flag 215 set, flag 216 clear: set flag 216, play `WOMS\SHAMAN\4223611E.VQA` (speaker 42, line 236, view 11), stay in the shaman room.

Third click, flag 216 set, flag 217 clear: set flag 217, play `WOMS\SHAMAN\4223711E.VQA` (speaker 42, line 237, view 11), stay.

A later click returns without another clip.

If `GV_SHAMAN_DEAD` is nonzero, the doorway enters `SHBAK_` on the click and does not play lines 225–227. SHBAK's first update then returns without lines 228–235 and without the load back to `SHAMAN_`. Clicking the back-room hotspot while that global is nonzero plays `movie(2, 30, 24)`. That name is not an entry in `SHBAK.MIX`.

Speaker 42 is the speaker argument of the actor placed in both rooms while the shaman global is 0. The English of every listed clip remains unknown. A host summary may say only the book's phrase, more interesting news. It must not invent Malik's sentences.

A weapon or spell in the back room, shaman global 0, flag 214 clear, is a separate path: set flag 214, pass the stem `BACKESCP` to host `0xee540`, pass `BACKGONE` to host `0xee43c`, and play `WOMS\SHBAK\0127511E.AUD` (speaker 1, line 275, view 11). Those two hosts are not in the named slot table used here. `BACKESCP.VQA`, `BACKGONE.VQA`, and `backloit.VQA` are entries in `SHBAK.MIX`. This path is not the doorway news.

## Grade

Clip order, the three later-click gates, the return to the shaman room, and the absence of an item on the doorway path are PROVEN from the two DLLs. They were not played. Prima's label is HINTBOOK, printed 88. Brady's Silverleaf speech is BRADY, printed 92, and it is the center-hut beat. The spoken English is UNKNOWN.

## Contract

Inputs. Shaman global 0, flag 215 clear, doorway hotspot 1.

Effect. The twelve clips above, in that order, then the shaman room again. No inventory change. The next two doorway clicks play line 236 and line 237 once each and stay.

Grade. Static DLL order. Book label only. English unknown.

Test. Not run. A later host test plays these files in this order, saves, and still has the same inventory. A second doorway click does not replay lines 225–235.

Adapter. None.

Other readers of flag 246 were not searched.
