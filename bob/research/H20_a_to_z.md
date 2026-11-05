# H20 What still blocks finishing, one page per act

The 2026-11-03 duck (`act1_completeness_duck.md`) counted 86 beats, 35 HOSTED, 24 MISSING, 27 UNKNOWN. It is stale. `lol2_r14` HEAD is `8732a39` (`act1_opus_20261104_r14`). These four commits are not ancestors of that HEAD: `3642265` (cave lever), `91db679` (dragon click), `330b027` (lift at the bottom), `85d1b31` (Bacatta prompt). `db5efe5` (mid-river drowning, Bacatta leaves) and `1c33ac0` (journal: join the tribe first) are on `act3-story`, not in r14. r14 does contain the voice reach `047a849` and the L8 guidance `054228d` (no sleep-expiry softlock).

Ordered by what stops a player reaching the end.

## Act 1

A tested route already finishes this act. The F2 row `act1-end-darker-jungle` is a real earned save, sha256 `9606beab57fdb8d246e3f322ba328a1ae965dba1027dda7b4eef5cb55d4c6425`, soul 8, runes translated, warblade flag 1.

From a new game, the holes still in this tree, in the order the player meets them:

1. Cave crates do not move (H16). The mace records are 85 above them. The owner clipped the wall instead. The roaches are on the way out.
2. Beat 14, the guard pulling the gates, is still the duck's MISSING row. The lever commit is not in r14.
3. Beat 30, the museum wall switch, is still MISSING in the duck. Beat 31, the dragon picture that flies you south, is still MISSING here. The dragon-click commit is not in r14. Dragon's blood itself was already hosted in the duck's note.
4. Hive lift beat 63 still starts wrong in the duck. The bottom-wait commit is not in r14.
5. Bacatta (beat 53): r14 has the louder voice. The prompt commit and the "he leaves after the film" commit are not in r14. The Nov 4 owner said the sequence worked on the r14 playtest and then asked him to disappear. That disappear fix is `db5efe5`, outside this HEAD.
6. Mid-river drowning fix is the same outside commit. The bridge path is the route. The Giant Fish movie (H14) is optional.

Not on the way to the end: the four Hive buttons and the boulder cellar (H01, H02), the jungle shrine and statue (H03, H04), the fish, and the Dark Halls. The Halls entry in this build is the cellar hotspot, not the bookcase strike (H09). Slides, Prism, the steel door, and the one hole are researched and not hosted (H10-H13). The knife meeting worked for the owner on this build ("the sword cat lady works perfect").

## Act 2

The stop that blocks the rest of the game is the one the owner hit on 23:25. `TRIAGE_20261104.md`: he reached the Larkhon with `admitted` false and `temple_visited` false, so there was no serum and the Dracoid chain did not start. The triage calls that order, not a broken chain. The journal line that tells him to join first is `1c33ac0`, which is not in r14. r14's `054228d` only stops the sleep-expiry softlock. Permanent sleep stays.

Next, in story order, still without an earned F2 save (H17): temple effects the owner reported are not the scripts on those points (H18), the Dracoid tomb (STORY-030), nine silverleaves back at the village (STORY-031), then the initiation. Map-format saves still cannot be F2 starts. `docs/playtest-starts.md` refuses them until a map resume kind exists.

These do not block the ending. He reached the Larkhon without them: the cache ladder and the knocked-down tree (P2 in that triage). Ruins walls: the owner trap in `TRIAGE_20261102.md` had no coordinate. r14 now sets `region_blockers_enabled` true and enables the 125 static bit0 regions (H19). The doc does not claim he has walked them since.

## Act 3

r14 is not the city build. `lol2_act3` is on `act3-story` at `1c33ac0`. Without a played L16 route, the game cannot be finished from this tree. The lead's P1 inside the city is the dry-fountain ball (H22, not written yet). The city gates use opcode 14 arm 5 as a no-op (H21, not written yet). The finale maps L17, L19, and L20 are the I-list after that. No frame was opened.
