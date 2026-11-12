# Your job 4: thirteen spots in one build (about 15 minutes) — build r19e

This replaces job 3 (r19d): it has all of r19d's spots plus the walls you walked through, the vault, the Ruloi entrance,
one question and one new look in the Hive. Each command starts the game paused where you pressed F10 on 12 November
(spots 1 and 2: just before the wall you walked through).

| Command | Level | You wrote | What should be different |
|---|---|---|---|
| `~/lol2_playtests/play_r19e_spot.sh 1` | Temple | "clipping through the wall" | walk forward: the wall at the edge of that room stops you; you no longer fall out of the map |
| `~/lol2_playtests/play_r19e_spot.sh 2` | Claw Mountains | "clip through wall" | walk forward: the ice wall stops you |
| `~/lol2_playtests/play_r19e_spot.sh 3` | Citadel | "stuck when jumping on vault" | you can walk off the vault top |
| `~/lol2_playtests/play_r19e_spot.sh 4` | Citadel | "texture here" | no dark slab in the tunnel, from your side and from inside the tube looking back |
| `~/lol2_playtests/play_r19e_spot.sh 5` | Claw Mountains | "ruloi entrance do not work" | a hint line says the way in is on the deck; walk on to the deck, press E there, the entrance plays and you arrive in the Citadel |
| `~/lol2_playtests/play_r19e_spot.sh 6` | City | "wrong texture here" | the painted patch is gone; the building continues |
| `~/lol2_playtests/play_r19e_spot.sh 7` | City | "the texture on houses look wrong" | the wooden panels are gone; green-tiled house fronts |
| `~/lol2_playtests/play_r19e_spot.sh 8` | City | "flickering texture" | no flicker; a gold wall |
| `~/lol2_playtests/play_r19e_spot.sh 9` | Temple | "black next room" | the doorway shows the hall with its benches |
| `~/lol2_playtests/play_r19e_spot.sh 10` | Temple | "texture floating" | the planes overhead are gone; a normal ceiling |
| `~/lol2_playtests/play_r19e_spot.sh 11` | Temple | "texture black rectangle here is wrong" | the black shape is gone from your side; you see the wall |
| `~/lol2_playtests/play_r19e_spot.sh 12` | Temple | "texture in the air" | QUESTION: the original's data has no roof over part of the room behind the lintel, so you see a strip of sky. Is that right, or should there be a roof? |
| `~/lol2_playtests/play_r19e_spot.sh 13` | Hive | (new, nothing reported) | starts at the Hive entry. Walk to the long hall near X -930 Y -7554 (the location line at the top of the screen) and look up at the lowered ceiling panels: they now have their sides, as the original draws them. Tell us if anything there looks wrong. |

- Spots 1-12 start paused with "Loaded at your report - press any key to continue". Look around with the mouse first.
- Right: close the game, next one. Still wrong, or something new: **F10**, a few words, confirm.
- Spot 11: the black shape was put there on purpose to match the longplay from the other side. If you think it should not exist at all, say so.

Tell the lead afterwards: "all thirteen fine", or which numbers are not (and your answer to 12).

For the lead: build playtest/r19e 8a53cce, worktree lol2_play_r19e, your save data ~/lol2_playtests/r19e/userdata.
Spots 1 and 2 load derived bundles (his own pose just before the wall; AI_COMMS/opus_lane/spots/*/SPOT.txt). Spot 13 is
the F2 start act1-hive-entry (no bundle in the Hive has a save). All 13 checked on a private display with scratch data:
1-12 hold at their pose, 13 starts, 0 script errors.
