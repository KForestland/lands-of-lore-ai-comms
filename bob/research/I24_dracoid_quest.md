# I24 Dracoid quest in r14

r14 is `~/opus_work/lol2_r14` at `8732a39`. Scripts were read. The tests named below were not run. No Godot.

Printed Brady pages 35–44 are the gear and ingredient chapter. They do not contain this quest. The steps in the task are the Second Sphere hints. Urn, hotel railing, priest body, both sparks, and the ashes click are printed 96–97. The urn gift, the ankh, and the Emperor’s tomb are printed 102. Grade on those sentences is BRADY. The hosting notes are the r14 files, not a new native decode.

The owner save in `TRIAGE_20261104.md` is the Darker Jungle quicksave: `l8_journey` gift recovered, `admitted` false, `temple_visited` false, no `l8_tribe`. The triage says there is no L9 or L10 save from that playtest, and the lead already asked which step stopped him. That save did not reach these seven steps. The Larkhon serum stop is I25.

## Steps

| step | Brady | hosted in r14 | test file | what stops a player |
| --- | --- | --- | --- | --- |
| Empty urn | printed 102: the priest gives an urn for his ashes | `l10_priest.gd`, attached from `act2_map.gd`. Item `act2:L10_DC:priest_urn`. Speak only after tomb `154` is open and the Bracers of the Dead are carried. | `tests/l10_priest_earned_test.gd` (blue globe on tomb 154, then one urn) | Tomb 154 still sealed, no bracers, or a full inventory. The bracers themselves are the earlier spark on shield 312 in `l9_dead_bracers.gd`. |
| Hotel railing | printed 96: second floor of the west building, knock the east railing over and walk it north | `l9_noble_rails.gd`, attached from `dragon_level.gd`. Controls 478, 479, and 480. A left-click strike sets selector 1 and clears that body’s collision. | `tests/l9_chapel_earned_test.gd` (`finish_chapel`: closed rail 480 blocks the north crossing; the strike opens it; the walk continues to the west bank and bridge 471/472) | Lizard, `player_form` 2, cannot strike. A player who never strikes rail 480 stays on the balcony. The script does not add a fallen-rail walk body. The test walks through the opened gap. |
| Priest body on the platform | printed 97: drag the body onto the altar between the orbs | `l9_pyre.gd` prop 2406, altar at Godot (10884.8, 140, −12566.2). Human only. E drags, E places. | `tests/l9_ashes_earned_test.gd` | Not human. Leaving human drops the hold. The body must stay inside the chapel bounds in `l9_pyre_state.gd`. |
| Spark both pedestals | printed 97: spark the two Dragon Orbs | Same file. Orb props 1205 and 1206 expose `receive_spark`. One orb leaves phase 1. Both move to phase 2. | same ashes test, which casts Spark at each orb | Spark before the body is placed is refused. A second hit on the same orb does not count. Not human refuses the ignite. |
| Ashes | printed 97: click the urn on the ashes | Phase 2 burns for 4.2 seconds, then phase 3. E inserts `priest_urn` and the slot becomes `act2:L9_DR:item0`. | same ashes test | The burn must finish. A charged white globe is refused. The empty urn has to be the carried item. |
| Ankh | printed 102: ashes returned, priest gives the ankh | `l10_priest.gd` `exchange_ashes` offers `act2:L9_DR:item0` to `l10_ankh_state.gd` target `priest:ashes` and outputs `act2:L10_DC:priest_ankh`. | `tests/l10_ashes_return_earned_test.gd` and `tests/l10_ankh_earned_test.gd` | Human, tomb 154 still open, bracers still carried, and the filled urn. The slab refuses an ankh that was not earned here. |
| Emperor’s tomb | printed 102: click the ankh on the symbol, then one white, one yellow, and one blue orb | `l10_emperor_entry.gd` slab assembly 66. `l10_emperor.gd` boxes 125, 126, 127, inner 143, then the remains. | `tests/l10_ankh_earned_test.gd` (slab), `tests/l10_emperor_supply_earned_test.gd`, `tests/l10_emperor_earned_test.gd` | Human at the slab. The inner door wants three globes first. Without the bracers, `l10_emperor.gd` calls the silverleaf revisit instead of the remains. A full inventory refuses the remains. |

## Still open

The native group bytes behind these adapters were not re-read. Yellow in the book is the gold globe id in the r14 tests; that rename was not re-proven. Whether assembly mode 1 draws the rail on its side was not opened. No frame was opened.
