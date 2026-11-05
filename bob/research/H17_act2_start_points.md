# H17 Eight F2 starts for Act 2 and the Act 3 entry

Proposal only. No manifest row was added. `scripts/lol2/playtest_starts.json` in `lol2_r14` already ends at `act1-end-darker-jungle` (sha256 `9606beab57fdb8d246e3f322ba328a1ae965dba1027dda7b4eef5cb55d4c6425`). `docs/playtest-starts.md` still says a map-format save is refused until the gate has a production map-save resume and `playtest_starts.gd` has a `map` kind. Points 5 through 8 need that branch. Points 1 through 4 stay on resume `darker` only if the test never leaves that scene.

Each row is an earned save in the sense of that doc: a campaign test writes it, and the manifest pins sha256, source test, source commit, input sha256, and identities. None of those files exist yet. No sha was invented.

The owner's 2026-11-04 save, as read in `TRIAGE_20261104.md`, had `l8_journey` gift recovered, `admitted` false, and `temple_visited` false. Those three field names are the triage's reading. This pass did not open the save.

## The eight

| # | id to add | earned step | input | identity to pin | resume |
| --- | --- | --- | --- | --- | --- |
| 1 | act2-tribe-admitted | From the darker-jungle arrival, show Daniel's gift to the Huline guard and finish the join. HINTBOOK 2982-2984. BRADY 3702-3703. | `act1-end-darker-jungle` | `admitted` true | `darker`, if still that scene |
| 2 | act2-temple-visited | Walk the Huline temple far enough that `temple_visited` becomes true. The temple's own puzzles are H18. | point 1 | `temple_visited` true | `darker` or the L14 map, UNKNOWN until the test leaves the scene |
| 3 | act2-larkhon-serum | After admission, complete the trade that puts the sleeping potion in hand. The owner had no serum because he was not admitted. The item index is UNKNOWN. | point 1 | the potion present. Dotted path UNKNOWN | `darker` |
| 4 | act2-larkhon-asleep | Use that potion on Larkhon. The save is after he sleeps. A later wake is not part of this start. | point 3 | a slept flag. The flag's path is UNKNOWN | `darker` |
| 5 | act2-dracoid-city | Arrive in the Dracoid city, `L9_DR`. | point 4 | player area L9, position the arrival spawn. Spawn bytes UNKNOWN | `map`, blocked |
| 6 | act2-dracoid-tomb | Finish the Dracoid chain through the Emperor's tomb, the step the owner said he could not finish. STORY-030 is that tomb, and it depends on STORY-029. | point 5 | the quest flag the tomb sets. Path UNKNOWN | `map`, blocked |
| 7 | act2-nine-silverleaves | Take nine silverleaves and return to the Wild Village, before offering one. STORY-031. HINTBOOK grade on that card, Prima pages 90 and 104. | point 6 | nine of that item. Which rows count is still UNKNOWN on the card | `darker` or `map`, UNKNOWN |
| 8 | act3-ancient-city | Arrive in the Ancient City, `L16_CA`. This is the Act 3 entry. | point 7, or whichever exit the campaign actually uses. The exit command's destination byte stays unnamed | area L16, arrival position UNKNOWN | `map`, blocked |

## What the lead would add before any of 5-8 can be chosen

The doc's three pieces, still unmet in this tree: a gate branch that reads the map save and applies it the way the other areas do, a `map` kind in `playtest_starts.gd`, and the manifest rows with real sha256 pins. Until those exist, F2 should keep showing only the Act 1 list.

## Grades

The knife, the two visits, and the nine leaves are HINTBOOK or the story cards already graded HINTBOOK. The field names `admitted` and `temple_visited` are the triage's report of one save. The eight ids and the resume column are a proposal. No frame was opened.
