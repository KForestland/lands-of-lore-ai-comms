# I25 L8 village admission

r14 `~/opus_work/lol2_r14` at `8732a39`. The owner save in `TRIAGE_20261104.md` is `l8_journey` gift `recovered`, `admitted` false, `temple_visited` false. No `l8_tribe` and no shaman trade. Scripts read: `l8_journey.gd`, `l8_journey_state.gd`. Tests named below were not run. The script comment cites hintbook printed 86–89 and 98. Those pages were not re-read.

`larkhon_join_tribe` is not in the r14 `scripts/lol2` tree. The triage puts that journal note on act3-story `1c33ac0`.

## Next steps from this save

The encounter picker in `l8_journey.gd` `target()` skips a site that is already done. Gift `recovered` hides the entry site. `temple_visited` false hides the village site. The live site is the temple.

1. Walk to the temple anchor `Vector3(758, 32, 2046)`, plus `native_translation` when the host has one. Reach is 160 and the camera ray has to be clear. E opens the panel. The button is "Approach the priest", action `visit_temple`. That sets `temple_visited`. The notice is "At the temple, a creature seizes the priest." If creature 113 is in the population, `restore_world` spawns it. Test file: `tests/l8_temple_earned_test.gd`.

2. The village anchor `Vector3(676, 32, -4541)` then becomes reachable. E, button "Show Daniel's blade", action `show_guard`. `l8_journey_state.gd` accepts it only when `temple_visited` is true and gift is `recovered`, and the carried id is `jungle:kityara:Empty_hand`. The blade stays in the inventory. `admitted` becomes true. The triage did not list the bag, so this pass does not know whether that blade id is still carried. If it is absent, the guard refuses with "Show the guard Daniel's blade." Test files: `tests/l8_journey_state_test.gd` refuses admission before the temple, then accepts this order; `tests/l8_departure_earned_test.gd` checks the guard does not consume the blade; `tests/l8_herbalist_earned_test.gd` calls `show_guard` as its admission setup.

Showing the blade at the village before the temple cannot happen through `target()`, and `act` also refuses with "The village encounter is not ready."

## What opens after admission

Still on the village panel, and only after `admitted`:

- "Visit the shaman" runs `visit_shaman` and adds one `l8:shaman:Dracoid_sigil` (the comment says original definition 102). A full inventory refuses. A second visit refuses.
- "Visit Daniel and return the blade" is `offer_daniel` at the village. It consumes the blade and sets gift `returned`. It is refused before admission.
- Herbalist sap, amber, and aloe, and the backroom, check `admitted` and refuse with "Enter the village first."
- Initiation wants a carried item whose catalog definition is 117, and `L8Tribe` phase `idle`. `l8_tribe.gd` also refuses unless `l10_silverleaf.grown` is true. That is after the cemetery, not the next click.

## What does not admit him

Standing at the Larkhon does not set `admitted`. Entry, herbalist, backroom, and the shaman key all stay closed while `temple_visited` is false. The Dracoid chain in I24 is later than this guard.
