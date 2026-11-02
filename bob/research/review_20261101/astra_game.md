# Astra game review — 2026-11-01

Scope: Q1–Q6, meta-analysis requested by the owner. Code inspected in promoted r12w `d46a181`; my unfinished work is `astra-progression aa3835c`. No rendered playthrough or new campaign qualification was performed for this review. “Missing” below means no verified end-to-end player implementation in the inspected paths, not proof that no useful native command exists.

Sources: Prima printed98–105, 113–117; Brady printed186–189 (PDF pages187–190), with the printed187 scan checked visually. The shared Brady text was only form-feed placeholders when read. I extracted/OCRed the relevant PDF pages in my own worktree, `tmp/game_review_brady/`, on CPUs24–31 nice19; I did not alter the lead's OCR output. OCR is a finding aid, not a reason to silently accept garbled wording. The owner's Bugs and Complaints reference supplies reported regression targets, not independently reproduced defects.

## Q1 — Corrections to the picture

The overall diagnosis is right: the Act1 campaign has qualification evidence; Act2/3 does not have a qualified story campaign. But these corrections matter:

- **My first L8 departure is a state subsystem, not a built playable story section.** `l8_journey_state.gd` has atomic gift/admission/key transactions; its test exercises JSON roundtrips and independently invokes the existing exit. There is no production spatial interaction/UI binding or complete save-host integration yet. The dashboard's “implemented first departure” needs that qualification. This is my responsibility, not merely a documentation problem.
- **“Maps only” is too pessimistic about infrastructure, but reasonable about story completion.** r12w has items, generic creatures, movers, blockers and native exit dispatch. L10's control150/group19732 writes the native teleport-enabling local11; `native_host_op197_test` checks that. This is not a completed emperor quest. Preserve these working mechanisms while supplying missing player actions and quest conditions.
- `act2_travel_graph_test` loads scenes, invokes region/control events, and can apply arrival adapters. It does not walk the book's route with earned inventory. Its 41/41 result establishes connected destinations and arrivals, not campaign solvability.
- The binder's `item_request` and `room_request` currently append logs. Successfully executing such a group is not the same as putting an item in the inventory or presenting an NPC interaction.
- **L13 Ruloi Citadel is absent from the lead's journey table.** It is indispensable: the dreamstone obtained there leads to the L8 temple return and L14. Put it explicitly between the Claw journey and the temple, not inside an unexplained “Claw complete.”
- “Act1 playable” must mean the qualified campaign path, not every optional mechanism. Keep the owner's Hive/Dark Halls/Baccata failures visible as separate acceptance failures; a green campaign does not refute them.
- I would not call all RPG/spell work nonexistent: player health/mana, equipment and particular spell effects already exist. The missing claim is a coherent, source-grounded progression/effect system covering the whole campaign. I have not audited all handlers, so I cannot certify the lead's exact handler counts.

## Q2 — Biggest risk

**Local success being mistaken for global solvability.** We can implement every named puzzle and still strand the player because a globe was consumed twice, a reward was dropped with a full inventory, the bracers were surrendered too early, a return visit reset state, or two implementations own the same reward. More opcode coverage does not address this risk.

Reduce it with one continuously earned L8→L10↔L9→L8 loop, checkpoints saved at its boundaries, and one owner for each consequence. Tests must retain the same inventory and quest history across transitions. No fixture should inject the very key, flag or resource that the preceding slice is supposed to earn. The owner rule lets us implement known behaviour directly; it does not justify silently adding unlimited quest resources or skipping the errands.

## Q3 — Shared building blocks, in priority order

1. **Atomic quest/inventory transactions and persistence.** Offer a specific carried instance; validate prerequisites and capacity; commit consumption, reward and milestone together. Save in-flight charger contents, opened doors and one-time NPC rewards. Define version migration and cross-area restore before scaling the errands. Extend existing quest/save code rather than replacing it with a new platform.
2. **One semantic interaction path.** Real aiming/input and headless tests invoke the same command with target, offered item/spell and player form. Production validates reach/obstruction. Retain rendered tests for input, target discovery and feedback. A direct state-method test is necessary but not sufficient.
3. **Small reusable mechanisms extracted from a real puzzle.** Start with one globe charger: insert → visibly occupied/charging → ready → retrieve. Then keyed receptacles and multi-input doors. Preserve item identity and reject the wrong item; do not start with an all-purpose puzzle language.
4. **NPC encounter sequencing.** Prerequisite → interaction/presentation → one-time inventory consequence → resume. Use existing room/movie presentation where applicable; log a modern summary fallback honestly. Do not require a complete dialogue editor before the shaman can hand over his key.
5. **Dependency/ownership manifest and observability.** Record owner, source pages, prerequisites, effects, optional status and save boundary per milestone. Distinguish audited, state-tested, runtime-bound, route-qualified, rendered-qualified and promoted. Debug traces should explain refused actions without appearing in normal player UI.

Creature tables and combat tuning are needed for completeness but should not block the charger/errand interfaces. Implement story-critical spells/items as those interactions need them; defer broad combat polish under the owner's phase order.

## Q4 — Four-week order, not a delivery promise

| Window | Intended outcome and acceptance boundary |
|---|---|
| Week1 | Finish one real L8 guard/shaman departure; then L10 key gate, first globe and charger. Add transaction/save/interaction foundations only as these require them. Accept actual inventory consequences after save/reload, not just state test PASS. Triage Act1 owner's route-breaking defects in parallel with an explicitly assigned owner. |
| Week2 | Complete the coupled L10/L9 priest/emperor/flood loop and L8 silverleaf return. Reuse chargers and offers; exercise consumable scarcity, optional detours and returns. This is the first convincing Act2 campaign milestone. |
| Week3 | L8 sleep-potion/Larkhon → L12 traversal → **L13 dreamstone** → L8 return; then L14 puzzle sequences. Add the item/spell effects these paths require, and establish the RPG model/tables before claiming combat balance. |
| Week4 | L16 city/tower visits and then L17/L19/L20 finale in dependency order; broaden route-critical effects, dialogue and full-campaign persistence. If prior milestones slip, carry them forward rather than publishing a calendar-driven “complete” claim. Sound and polish remain later. |

This is a dependency ordering with review points, not an estimate that a complete faithful game will fit four weeks. A full completion claim also needs optional routes, player-visible presentation, all required systems and exported-build qualification.

## Q5 — Dracoid Cemetery, spoken as a player

Page numbers below are printed pages. P = Prima; B = Brady. Native fragments should remain; “modern” means implement the documented behaviour and bind it to the actual world target, not a menu that advances the story from anywhere.

**What works now:** L10 scene/geometry, arrivals, generic population/items and exit binder are present. The checked-in travel and native-op197 tests cover infrastructure. I did not run a rendered L10 playtest today. **No complete Cemetery story-route test exists in the inspected work.** Names in the last column are proposed acceptance checks, not existing passing tests.

| Player's step | Sources | r12w evidence / gap | Implementation and proving check |
|---|---|---|---|
| I arrive carrying the shaman's sigil and use it on the main gate. | P98; B187 step1 | Arrival exists; earned shaman reward and its gate interaction are not qualified. My branch's reward is state-only. | Modern owned-item offer plus existing gate/mover if suitable. Proposed `cemetery_gate`: no key/wrong key refuse; right key opens; reload retains opening. Do not assume the key is consumed without evidence. |
| I find empty glass globes, enter the southern catacombs and use the gold/yellow charger. | P99–100; B186,188–189 | Placed items and generic control support exist; pickup→charging→retrieval is not verified. | Modern charger transaction. Proposed `cemetery_charger`: place an actual instance, retrieve transformed instance exactly once; full inventory and reload while occupied cannot lose or duplicate it. Gold/Yellow is guide terminology for the corresponding required charger; bind using source item definitions. |
| I go to the ruins/Mage's Tower for white globes and the Bracers of the Dead, then return. | P100–101; B187–189; B182 for ruins sequence | L8/L9/L10 connections exist. Teleport control150/group19732 has a host test, but that test does not earn this expedition. | Preserve native travel, modern tower/item encounters where missing. Proposed `ruins_white_return`: carry the same quest inventory through the earned route; cannot use an unearned shortcut just because the travel test can activate it. |
| I use a white globe at the western tomb, operate its switch, tip the opposite barrel as Human, and roll it into the target tomb. | P101–102; B184 map point7; B189 white-orb and oil-breach description | No verified target offer, tipping/rolling/collision sequence. Movable support is not proof of this barrel. | Modern deterministic interaction/physics using actual geometry. Proposed `cemetery_barrel`: correct form and target; obstruction cannot permanently destroy the only route; save during motion restores coherently. Fix the reported failure-to-tip behaviour rather than reproduce it. |
| I ignite the spilled oil from a safe position and the breach opens. | P101–102; B189 blue-altar access | No verified oil/fire/breach chain. | Modern fire-target reaction and one persistent breach. Proposed `cemetery_breach`: no spill/wrong effect refuse; qualifying fire opens once; reload and repeated fire do not reset it. Prima recommends Spark3 for safe range and warns against close-range lower levels; that is NOT evidence that only level3 can ignite oil. |
| I reach the blue charger and prepare enough globes for the priest and emperor. | P103; B187,189 | Charger interaction and earned access unqualified. | Reuse charger. Proposed resource-ledger check retains required globes after optional spending. B189 gives minimum five: two white, two blue, one yellow; P's route agrees. Do not turn the optional crossbow into a required expenditure. |
| I open the priest's tomb with blue, communicate using the dead bracers and receive his urn. | P103; B187 | Room/item requests log; full conversation and inventory grant unhosted. | Modern encounter using existing presentation where available. Proposed `priest_urn`: bracer requirement, blue-gate state, capacity-safe one-time urn, repeated talk. Brady wording varies between possessing and wearing bracers; record that distinction rather than silently assert an equip requirement everywhere. |
| I return to the ruins, place the priest's body on the pyre, energize the two orbs, collect ashes in the urn and return for the ankh. | P103–104 and113–114; B182,187 | Geometry/native room candidates exist; corpse→cremation→urn→reward campaign sequence missing. | Modern multi-area errand, retaining native machinery where it runs. Proposed `priest_ashes_roundtrip`: no ashes before cremation; correct urn transformation; one ankh; interrupted/repeated visits safe. |
| I use the ankh and put one gold/yellow, one white and one blue globe in the matching emperor receptacles, then take his remains. | P104; B187–189 | EMPT room request exists but does not provide this interaction. Teleport local11 write exists separately. | Modern receptacle set and encounter; native exit retained. Proposed `emperor_receptacles`: every insertion order reaches the same completed set unless a source mandates order; wrong colors refuse; partial set reloads; remains once. Prima calls gold/white/blue a working order, not the only valid order. |
| I take the remains to Belial's statue in the ruins, witness the worm fight, escape the flood and meet Dawn in L8. | P104,115–117; B188 | Connected exit infrastructure; the causal story/hazard chain is not complete. | Modern statue/flood encounter with physical escape and persistent outcome. Proposed `emperor_flood_return`: earn flooding, escape, retain quest history and apply Dawn's bracer handover once. Do not let a travel-only exit masquerade as surviving the flood. |
| I revisit the emperor, find silverleaf growing and return to the shaman with a supply, keeping some for later use. | P104–105; B188 | Source plant data may exist; the earned growth/harvest/return path is not qualified. | Modern completed-errand plant activation and inventory. Proposed `silverleaf_return`: none before resolution, growth after resolution survives reload, collection works without the surrendered bracers, later-city leaf remains obtainable. P advises nine leaves; B188 advises retaining an unmixed leaf for the City. Neither justifies requiring exactly nine to unlock the first reward. |

### Focused duck: “the charger works”

**Knot:** Map, item placements and generic native commands exist. The real unresolved claim is whether a player can put an owned globe in a world charger, leave/reload, and get exactly one correctly charged globe back. A command log or a direct item grant cannot decide this.

**Facts:** r12w's binder logs item requests; the guides describe insert/charge/retrieve; the exit test bypasses the full resource journey. **Builder read (proposed):** an occupied charger temporarily owns the particular globe; retrieval transfers it back atomically. Existing inventory and scene transition systems should retain their responsibilities.

**Clone-me risks:** (1) a state-only test hides a missing interaction target; (2) using generic definition IDs loses duplicate globe instances; (3) a permanently seeded test globe hides depletion caused by optional doors.

**Flip point:** Does the same owned instance survive the transfer into the charger across save/reload, or is the output merely a fresh grant with no accounted input?

**One exact next check:** In the production L10 scene, use the real semantic interaction target to insert one earned empty globe, save/reload while the charger owns it, retrieve the charged globe, then attempt retrieval again; assert one input removed, one output present, second retrieval refused, and no unrelated inventory changed. This single check tests the missing ownership boundary better than more opcode coverage. It is proposed, not run or passing today.

## Q6 — Rough size and what would make me faster

A slice means a player-visible, persisted sequence ending in a useful milestone, including refusal/reload tests and runtime binding. These are planning ranges, not measured velocity or weeks. Shared cross-area handoffs must be allocated once in the ownership table, not independently built twice.

| Area | Planning slices | Main scope |
|---|---:|---|
| L8 | 6–8 | gift/temple/admission/key; return encounters; initiation; serum/Larkhon; dreamstone return; optional branches |
| L10 | 7–9 | key/chargers; barrel/breach; priest; emperor; silverleaf and returns |
| L9 | 6–8 | bridges/orbs; tower/bracers/white charger; priest body; statue/flood; exits |
| L12 | 3–5 | avalanche/ice traversal; Baccata/Kenneth encounter; citadel and return; optional rewards |
| L13 | 4–6 | entry/eggs/lifts; prisoners; boss; dreamstone retrieval/exit; optional forge |
| L14 | 8–11 | corpse/bowls, shards, machines/statue, three puzzle rooms, hazards/platform, apparition, chalice |
| L16 | 7–10 | corner puzzles, chips, repeated tower-box visits, mantle, dragon exit |
| L17 | 2–4 | cavern/interior passages and transition; precise book-to-map boundaries still need confirmation |
| L19 | 4–6 | laboratory/liquid/rapids/corpse circle and story transitions; boundary ownership to settle |
| L20 | 3–5 | boss pursuit, moving hazards/armory, final encounter/endings |

The ranges should shrink after two actually playable slices establish effort. “2x faster” is a target, not something I can promise. The biggest likely gains are: stop unnecessary decoding of known behaviour; reuse one proven transaction/charger/encounter pattern; get spatial target and item-instance identities into each task up front; require one clear milestone per handoff; and reuse earned save fixtures. My own correction is to stop presenting isolated state tests as progress that a player can already experience.

## Five-line handoff contract

CONTRACT inputs: promoted r12w code/tests, branch aa3835c, Prima cited pages, Brady scans/OCR cited above.
CONTRACT effect: distinguish infrastructure and state-only work from playable story; prioritize one persisted Cemetery item-transfer boundary and the coupled L8/L10/L9 loop.
CONTRACT grade: code observations PROVEN by inspection; book behaviour HINTBOOK/BRADY; slice ranges and implementation proposals are estimates, not native facts.
CONTRACT test: the single next check is earned globe insertion → occupied-charger save/reload → retrieval → duplicate refusal in production L10.
CONTRACT adapter: known missing behaviour implemented directly under the owner rule, with explicit ownership and DEVIATIONS; no new gameplay change made for this review.
