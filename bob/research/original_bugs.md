# R4 original bugs, 2026-11-02

List only. The deviations ledger and `ORIGINAL_BUGS_TO_FIX.md` were not edited. No backlog status was changed. Grades below are the source that was opened, and they are not a retail-page grade unless the line says HINTBOOK or BRADY.

## Sources opened

- `~/AI_COMMS/act1_completion_20261017/ORIGINAL_BUGS_TO_FIX.md` already has rows 1 through 14. Owner rule there: gameplay bugs are fixed in Classic and Enhanced; technical DOSBox, Glide, and memory crashes are out of the port.
- `~/AI_COMMS/reference_hintbook/Lands_of_Lore_Bugs_and_Complaints_AI_Reference.md` is a compiled October 2026 fan note (wiki, GOG, Reddit, and the other sites named in its header). Grade: compiled fan reference. It is not HINTBOOK and not BRADY.
- German guide `~/AI_COMMS/reference_schon_gewusst_lol2/schon-gewusst-lol2.txt` sections 4.1 through 4.4. Grade: fan guide.
- Official patch notes in the landsoflore.de community-installer payload, `PATCH.TXT` section 5 (patch 1.06 to 1.30). Grade: patch notes. The shipping MIX was not re-read, so the two patch sentences were not checked against current bytes.
- r12y `56812f9` `docs/deviations`, word search only.

`landsoflore.de` itself was not fetched. The local payload and the guide's forum links are the copies on disk.

## Already a deviation row

| bug | where it already sits | deviation |
|---|---|---|
| 1 Rix curse never lifts | ORIGINAL_BUGS row 1; fan guide 4.4 | `0161` names the load-time 208→207 fanfix. `0023` still records the unsavable talk branch. |
| 8 Clipped Draracle roaches | ORIGINAL_BUGS row 8; compiled fan note | `0169` names original-bug fix 8 for roaches 50 and 51. |
| 9 Misclipped plasma bolts | ORIGINAL_BUGS row 9; compiled fan note | `0155` names original-bug fix 9, map side, host still pending in that row. |

## In ORIGINAL_BUGS, no deviation title states the bug

Searched r12y deviations for the bug's own words. Nearby rows are a different subject and are named so they are not counted as coverage.

| ORIGINAL_BUGS | source opened this pass | nearest other deviation |
|---|---|---|
| 2 Waterfall lizard change can fail | row text only; the hidden switch was not re-read | `0049` is gorge wall drawing |
| 3 Daniel sword softlock if the Wild Ones leave first | row text; fan note's dead-end complaint | `0208` and `0209` host the first-departure sequence and do not name that softlock |
| 4 Wrong statue sound in the Dark Halls | fan guide 4.1: the black statue plays a Wild Jungle line, "Du, nein, Ihr habt die Stärke und die Ehre eines Tohani-Kriegers." | no row contains that sentence |
| 5 Cantina memory crash | compiled fan note; patch notes do not mention it | technical, and ORIGINAL_BUGS already excludes it |
| 6 Cemetery barrel fails to tip | compiled fan note; PATCH.TXT 5.2 says the 1.30 patch makes the Dracoid Cemetery barrel push and roll in all circumstances | no tip-failure row. `0066` is the village Confidante barrel |
| 7 Temple bowl feeds aloe early and skips the Caretaker zap | compiled fan note; PATCH.TXT 5.1 says extra aloe and poison paint on the Huline Temple altar no longer lock out the lightning strike | `0212` is the herbalist jar menu |
| 10 Curse still transforms after it is expelled | compiled fan note, trigger unread | `0018` is the first curse duration |
| 11 Storm Crystal on Dawn while leaving the Hive with the rune copy can freeze | compiled fan note | `0058` picks up a Storm item and does not name this freeze |
| 12 Stationary Ssar or Skeletal Guardians do not die from range | compiled fan note | no row names that failure |
| 13 Cemetery ghost or Silver Leaf missed when the Bracers of the Dead go to Dawn wrongly | compiled fan note | `0221` is Silverleaf +5 mana; `0225` is the bracer shield after the fight |
| 14 A discarded key item dead-ends the game | compiled fan note, complaint | no row states a no-drop rule |

## Fan-guide sections that are not bugs

Section 4.2 is a garden-door route. Section 4.3 is a peephole crate reward list. They were not added as bugs.

## Proposal

No new PROPOSE line. Rows 1 through 14 already exist in `ORIGINAL_BUGS_TO_FIX.md`. Adding a second backlog title would duplicate that list. The three deviation rows above are the ones this pass could point at by name.

## Recheck for task 16

The r12y deviations directory still has 228 markdown files. A search for the waterfall-lizard failure, the Daniel softlock, the Tohani statue line, a barrel that will not tip, the temple-bowl lockout, a curse that continues after it is expelled, the Storm Crystal freeze, a stationary Ssar, and a no-drop rule still does not add a deviation title. Rows 1, 8, and 9 remain the ones named by 0161, 0169, and 0155. The ledger was not edited.
