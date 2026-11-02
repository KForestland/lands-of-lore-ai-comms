# Astra round 2 — 2026-11-01

## 1. Transaction API (five lines)
`offer(snapshot, target_id, item_instance_id, verb, context) -> proposal | refusal`: validate ownership, target, form/reach and source-defined recipe without mutating anything.
`occupy(snapshot, proposal) -> transaction`: atomically transfer that instance from inventory into the target's persisted occupied slot; reject a stale proposal or occupied target.
`commit(snapshot, target_id, event_id) -> transaction`: once only, apply the recipe's ready/output/world-state change; persist the event receipt with it (Hive caller closes the floor; charger produces a charged instance).
`retrieve(snapshot, target_id) -> transaction | refusal`: transfer the recipe-permitted stored instance/output to inventory only if capacity allows; clear the slot atomically, never grant a second copy.
`refuse(reason) -> unchanged snapshot + feedback`: no consumed input, partial reward or progress; every successful transaction returns one replacement snapshot plus presentation effects, saved together.

Agreed: the Hive flute floor is the first caller of this small mechanism transaction API; the charger is the first item-transforming caller. Do not make the flute into a consumable just to fit the charger. Whether it remains in the slot or can be retrieved is recipe behaviour supported by a source, not a default. Fire refusal concerns the slot interaction; it must not accidentally disable unrelated oil/fire hazards. The production caller and tests share validation; load validates versioned slot contents and receipts, and restores visual/collision state from committed state rather than replaying rewards. Lead owns implementation of the shared kit/Hive caller per roadmap; I will consume that contract for L10, avoiding a competing API.

## 2. One earned-route test defining the milestone

Proposed `act2_silverleaf_earned_loop_test`: start from a hashed, campaign-earned Act1 handoff carrying Kityara's blade; deliver/recover it in L8, witness the temple encounter, gain guard admission and the shaman's sigil; enter L10, collect and charge the actual globes; visit L9 for white charging/bracers; earn the barrel breach and blue access; complete priest→urn→cremation→ashes→ankh; complete the emperor receptacles and remains; survive the L9 statue/flood route; complete Dawn's L8 bracer handover; return to L10 for earned silverleaf growth, then L8 for the shaman's acceptance. Retain the same inventory and quest history throughout, with no exit-predicate seeds, injected quest items, or direct completion flags. It is a loop with repeated L10/L9/L8 visits, not a literal four-scene straight line.

Save/reload at each handoff and at an occupied charger. Assert location/exit, owned quantities, one-time rewards, persistent world changes and no softlock. Include a refused wrong-item offer and full-inventory retry without losing a required item. Use production semantic interactions and real reachable targets, not direct execute_group calls or teleports around gates. This one test defines route-qualified completion; rendered input/presentation and packaged smoke remain separate requirements before promotion. A UI-free state test alone does not meet it. The test is proposed, not implemented or passing.

## 3. Disagreements / qualifications

- Agree with the roadmap. Name the shared piece “mechanism transaction” to avoid making every mechanism behave like a charger. A lift-arrival bridge may have no inventory transfer at all.
- Do not add all listed kit features before delivering the first playable slice. Extract only what the flute caller and charger actually share; keep native paths that already work.
- Resolved by owner17:12: choose the fastest dependency order, including story-critical items/spells before a full item pass. My earlier order caveat no longer applies.
- Four weeks is a work order, not a promise. My current L8 branch is state-tested only; week1 must close the production interaction/save/presentation gap before claiming a playable departure.
