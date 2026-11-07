# AW04 — L8 tribe village as a state machine, and the findings

Live scripts on `stack-ah01` `cfba754`. The unapplied AV01 temple walk-in is not in this tree: the live panel still offers "Approach the priest" on E. Grades: HINTBOOK for `reference_hintbook/hintbook.txt` 2900–3166; DECODED for the flags and item ids in the scripts named below. No new WOM line was opened. Dawn's shore meeting and the Larkhon are outside the village scene. They are in this file because the book places them on the same chain, and the task names them.

## What this village is for

HINTBOOK 2900–2941 and 2979–3077. Give Daniel his grandfather's blade, pick the blade up when the hoppers interrupt, see the temple scene, show the blade to the guard, and only then enter. The shaman sends Luther to the cemetery. Nine silverleaves, an initiation that is not to the death, then one more leaf for the shaman's potion. The herbalist's jars and the doorway beside the shaman are part of the same scene. The clubhouse opens after membership. The Larkhon sleeps only for a mixed, activated dose on the upper chest.

The required chain in these files is: `offer_daniel` → `hopper_interruption` → `recover_blade` → `visit_temple` → `show_guard` → `visit_shaman` (the sigil) → cemetery silverleaf → `initiation` → `shaman_silverleaf` → mix → activate → upper chest.

## Graph

```text
entry, gift unoffered
    | Offer the blade (id jungle:kityara:Empty_hand)
    v
delivered -- Continue --> dropped -- Pick up --> recovered
    |
    | temple_visited (notice: a creature seizes the priest)
    v
show the blade to the guard --> admitted
    |
    +-- Visit the shaman --> key_awarded, item l8:shaman:Dracoid_sigil (definition 102)
    +-- Herbalist: sap, amber, aloe, two of each, after admission
    +-- Doorway: backroom sequences 225-235, then 236, then 237 (three visits)
    |
    | silverleaf definition 117, and l10_silverleaf.grown, human, admitted
    v
initiation: intro speech, then the bout
    | either stamina reaches 0
    v
complete -- E facing Daniel --> departed, placed at (531, 32, -4414)
    |
    +-- one other silverleaf --> Amaranth Serum (definition 119)
    +-- E on the clubhouse guard --> doors open; the stones are not granted by that talk
    |
    v
mix leaf + serum --> Larkhon Vapors --> activate --> right-click upper chest
    v
used receipt stays true, and the L8 to level-12 change is allowed
```

Dawn stands on the lake shore after the wet ruins, which is after this village's first visit and after the cemetery. She takes the bracers and gives the control token. Baccata hangs in a trap on the same map, south of the cemetery path in the book. Neither one is a button inside the village panel.

## Daniel, the hoppers, the temple, the guard, the shaman's key

`l8_journey_state.gd` `act` and `l8_journey.gd` `permitted` / `refresh`. Reach is 160. The live anchors are entry (−3854, 32, 1190), temple (758, 32, 2046), and village (676, 32, −4541). The village anchor is refused until `temple_visited`. The entry anchor is refused once the blade is recovered or returned. Validate refuses admission without the temple and a recovered or returned blade, a returned blade before admission, and the key before admission.

| id | action | precondition | consequence | next |
| --- | --- | --- | --- | --- |
| D1 | Offer grandfather's blade | at entry, gift `unoffered`, the blade id is carried | gift `delivered`, blade leaves the inventory | "Daniel accepts his grandfather's blade." |
| D2 | Continue the meeting | gift `delivered` | gift `dropped` | "Hoppers interrupt the meeting. Daniel drops the blade as he leaves." Actors 81, 92, and 93 are removed once the gift is dropped, recovered, or returned. |
| D3 | Pick up the dropped blade | gift `dropped`, blade not already carried, inventory under 64 | gift `recovered`, blade returns | "You recover Daniel's blade." |
| D4 | Approach the priest | at the temple, not yet visited | `temple_visited` | "At the temple, a creature seizes the priest." Actor 113 spawns. |
| D5 | Show Daniel's blade | at the village, temple visited, gift `recovered`, blade carried | `admitted`. The blade stays in the inventory. | "The guard recognizes the blade and admits you." |
| D6 | Visit Daniel and return the blade | admitted, gift `recovered`, blade carried | gift `returned`, blade leaves | "You return the blade to Daniel in the village." |
| D7 | Visit the shaman | admitted, key not awarded, key not carried, room in the inventory | `key_awarded`, append `l8:shaman:Dracoid_sigil` | "The shaman asks for silverleaf and gives you the cemetery key." |

HINTBOOK 2904–2922: the knife goes on Daniel's chest, a wrong click is "Uh oh", the hoppers make him drop it, and the knife is required at the village. HINTBOOK 2932–2941: the first temple approach plays the snatch. HINTBOOK 2979–2984: show the gift to the guard; attacking him is the hard path. The live panel has no attack button.

The live journal sentence for `l8_see_temple_first` is still "The village will not open until I have seen the temple east of the road, and I must carry Daniel's blade." AV05, which rewrites that sentence, is not applied on this tree.

## Initiation

`l8_tribe.gd` and `l8_tribe_state.gd`. Offer from the village panel only while the phase is `idle`, a carried item has definition 117, `l8_journey.admitted` is set, and `l10_silverleaf.grown` is set. The offer also refuses a non-human form, flight, or a paused tree. The leaf is consumed. Phase becomes `intro` with player stamina 500 and Daniel stamina 600.

The intro plays the staged clips, then phase `fight` places the player at (2679, 32, −4187) and wakes actor 23. Daniel closes while in sight, and every 1.2 s in range he takes 8 off the player. The player's melee on actor 23 lowers Daniel's stamina. Either stamina reaching 0 sets phase `complete` and the notice "The initiation ends without a death. You are accepted into the tribe." E during the fight calls `yield_bout`, which does nothing while both sides are still at full stamina. After `complete`, E while facing actor 23 (within 180, dot at least 0.8, human) sets `departed`, places the player at (531, 32, −4414), and sets yaw to 90 degrees. The notice is "You return to the Wild Village after your initiation." `member` is phase `complete` or `departed`. Deviation row 0253 names that exit heading as 180. The live assignment is 90 degrees.

HINTBOOK 3069–3074: offering a silverleaf starts the fight at once, the fight is not to the death, and a few blows end it. HINTBOOK 3054–3056: bring nine silverleaves. The scripts count leaves by definition 117. They do not count to nine.

## The shaman's potion

`l8_shaman_trade.gd`. A second definition-117 item, after `member` is true, and not the leaf already sitting in the initiation slot. Output `act2:L8_SJ:shaman_amaranth`, definition 119 in the Larkhon mixer. Once. Human form. The panel shows this button only when the initiation is complete and the trade is not.

HINTBOOK 3075–3077: offer him a silverleaf and he gives the potion. The script's notice on the earlier key button already says he asks for silverleaf. The potion is the later exchange.

## The herbalist

`l8_herbalist.gd`. After admission, three kinds, two ids each: sap definition 111, amber 112, aloe 110. A full inventory of 64 refuses. A second take of the same id refuses. Flag 206 is named in the header as a later bonus and is not granted here.

HINTBOOK 2991–2992: the leftmost treehouse is hers, and she does not mind the jars being taken. The live action is a panel button, "Herbalist — take …", rather than a click on a jar in the scene.

## The backroom

`l8_backroom.gd`. After admission, three visits, in order: lines 225–235, then 236, then 237. Enter skips a line. A fourth start is refused. Playback is the staged wav. The speech card already says 225–237 are SHAMAN and SHBAK, view 11.

HINTBOOK 2993–2996: click the shaman through, and click the doorway to his right. The serum and the sigil do not read `l8_backroom.completed`. The doorway is news, not a gate.

## Dawn

`l8_dawn_state.gd`. Shore only: the exchange validates only when `l8_shore.arrived` is set. She accepts `act2:L9_DR:item55` (the bracers) and gives `act2:L8_SJ:dawn_control_token`. Once. Human form. No soul write in this file.

HINTBOOK 3021–3033: after the wet exit she is on the bank, she wants the bracers, and she talks about magic that reflects. The hosted action is the exchange. The reflecting-magic lines are not a choice in this state.

## The Larkhon

`l8_larkhon.gd` and `l8_larkhon_state.gd`. Not a speaker.

| id | action | precondition | consequence | next |
| --- | --- | --- | --- | --- |
| L1 | mix | human, a definition-117 leaf and a definition-119 serum carried, not yet mixed | both leave, `act2:L8_SJ:larkhon_vapors` is carried | "You mix Silverleaf with Amaranth Serum to make Larkhon Vapors." |
| L2 | activate | the vapors are carried and mixed, not yet used, not already active | `active` | the feedback says to use the right button on the upper chest |
| L3 | offer onto the chest | human, world active, aim within 180 on the upper chest (65% of the look height), active | the vapors stay in the chest slot, `sleep` starts at 60, `asleep` stays true after the clock | "The Larkhon falls asleep. The cave entrance is clear." `act2_progression.gd` allows the L8 to level-12 change only when `used` is true. Otherwise the feedback is "The Larkhon guards the cave entrance." |

HINTBOOK 3146–3165: Human jump, combine the potion and a leaf, left-click to activate, right-click the upper chest, and a miss means another dose or a reload. The jump itself is not a function in `l8_larkhon.gd`. Guidance notes, in order, tell the player to join the tribe, ask the shaman, mix the leaf, then activate. DEVIATIONS 0306 and 0307 already record the guidance and the lasting sleep.

## The clubhouse and Baccata's trap

`l8_clubhouse.gd`. E while aimed at (−1791, 55, 1068), human, within 160, and `member`, sets `opened`. The function does not add the three stone ids. `validate` refuses those ids in `collected` unless `opened` is already true. Actor 21 stands once the doors are open or the player is within 300 of (−1791, 32, 1068). HINTBOOK 3137–3141: after membership, the guard bids Luther welcome, opens the doors, and the stones inside can be taken.

`l8_baccata.gd`. After `l8_shore.arrived`, human, in reach of the trap. Phase 0: E with a carried sword, longsword, dagger, or blade cuts him down. Phase 1: E again, he speaks, phase 2 walks him for 5 seconds, phase 3 he is gone. No attack and no "leave him hanging" branch in this function. HINTBOOK 3037–3045 is the cut-down. Brady's printed 103, in `bacatta_timeline.md`, adds attack or leave. Those two are not hosted.

## Findings

| id | original source | ours | verdict |
| --- | --- | --- | --- |
| L8-1 | HINTBOOK 2916–2922 and 2932–2941. The knife must be given, recovered, and shown, and the temple scene comes before the village. | `validate` refuses admission without both, and the village anchor is dark until `temple_visited`. | OK. |
| L8-2 | HINTBOOK 2904–2908. The knife is placed on Daniel's chest. A bad click is a failed gift. | One button, "Offer grandfather's blade", and it succeeds whenever the id is carried. There is no failed-gift state. | The success path matches. The fussy failure is absent. It does not stop the chain: the button completes the gift. Listed for later. |
| L8-3 | HINTBOOK 2979–2982. Attacking the guard is a hard, hostile path. | The village panel has Show, Visit, Offer, Herbalist, and the doorway. No attack. | The required path is the show. The hostile path is unhosted. It does not stop the chain. |
| L8-4 | HINTBOOK 2991–2996. Jars are picked up in the scene. The shaman is clicked through. The doorway is clicked. | Herbalist, shaman, and doorway are buttons on the E panel, at the village anchor, after admission. The grants and the three backroom visits do happen. | OK for items and order. The trigger is the panel. The serum does not wait on the doorway. |
| L8-5 | HINTBOOK 3069–3074. The offer starts a non-lethal fight, and a few blows end it. | Either stamina hitting 0 accepts Luther, including his own hitting 0. Yield does nothing at full stamina. The leaf must already have been grown in the cemetery. | OK. Losing still joins, which is the book's "not to the death." The script does not require nine leaves. |
| L8-6 | HINTBOOK 3075–3077. A further silverleaf buys the potion, after the initiation. | `exchange` refuses unless `member` is true, and it refuses the leaf already stored on the initiation. | OK. |
| L8-7 | HINTBOOK 3027–3033. Dawn wants the bracers on the shore. | The exchange requires `l8_shore.arrived` and the bracer id, and it gives the token. No dialogue choices. | OK for the item. The speech is not a state machine in this file. |
| L8-8 | HINTBOOK 3146–3165. Mix, activate, right-click the upper chest. A miss can be retried if ingredients remain. | One mix, one activation, one chest offer. `asleep` stays true afterwards. Another dose is not a second state. | OK for the success path. A second dose is not hosted. The book allows one if the first was flung out of reach. Listed for later. |
| L8-9 | Brady printed 103, via `bacatta_timeline.md`. Cut him down, attack him, or leave him. HINTBOOK 3041–3043 is only the cut. | Phase 0 accepts a blade and phase 1 speaks. No attack, no leave. | OK against the hintbook path. Brady's other two choices are unhosted. They are not the required cut. |
| L8-10 | Soul. The hintbook village pages read here do not name a soul change. | No soul write in `l8_journey_state.gd`, `l8_tribe_state.gd`, `l8_shaman_trade.gd`, `l8_herbalist.gd`, `l8_dawn_state.gd`, `l8_larkhon_state.gd`, or `l8_backroom.gd`. | OK. No delta to apply. |
| L8-11 | Deviation row 0253 names the post-bout exit heading as 180, at the SETTLE1 point (531, 4414). | `leave_arena` writes yaw `deg_to_rad(90)`. The position matches. | The heading numbers disagree. The exit still runs, so the chain is not stopped. Listed for later. |
| L8-12 | HINTBOOK 3158–3165. The sleeping Larkhon is the way into the mountains. | `act2_progression.gd` refuses L8 to level 12 until `l8_larkhon.used` is true, and says the guardian is still at the entrance. | OK. The dose is the gate. |

No L8 row is an "ours wrong" that stops this chain. The panel contains every required action, in an order the validators also enforce, and the level-12 change waits on the dose. L8-2, L8-3, L8-5's missing count of nine, L8-8's missing second dose, L8-9's missing Brady branches, and L8-11's heading are the refinement list. No patch and no earned walk for this file.
