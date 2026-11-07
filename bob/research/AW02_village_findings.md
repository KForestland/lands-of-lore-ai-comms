# AW02 — game-theory pass on the Act 1 village

Read with `AW01_village_logic.md`. Each row is one place a choice can trap the player, skip a branch, or change the soul byte. Verdicts are OK, ours wrong, or original stuck. A row is "ours wrong" only when the live script disagrees with the source it claims to host, or with the hintbook line cited. No patch is attached here; `AW03_chain_stops.md` says which of these can stop the required chain.

The required chain is the honest one. HINTBOOK 2337–2342: the thief is not required, and the tavern is the stop to leave for last. HINTBOOK 2344–2349: hear Baccata out and do not attack. The monastery flute route in `docs/bacatta-rooms.md` is cited as that doc's earlier walk. It was not re-run for this pass.

## Findings

| id | original source | ours | verdict |
| --- | --- | --- | --- |
| F1 | HINTBOOK 2332–2336. After the rescue the gates are open and the stops have no required order, except the advice to leave the tavern last. | `admits` opens on `shared38==1`, alarm 0, `local24==0`. The cantina opens when flag 267 is clear. No flag in the files read forces the tavern to be last. | OK. The "last" sentence is advice. No native tavern-last flag was found this pass. |
| F2 | HINTBOOK 2344–2349. Keep Baccata's conversation moving. Do not start an attack. | First visit: promise, then relationship +1 and flag 34. Walk-out while flag 37 is set takes 0xE09 and leaves the relationship at 0 (`docs/bacatta-rooms.md`). Hostile and click-attack branches are still open in that doc. | OK for the promise path. The attack branch is unhosted. It is the branch the book tells the player not to take, so it does not stop the required chain. |
| F3 | HINTBOOK 2337–2341. The password leads to the thief. The diversion is not required. | Confidante local 27 opens TDOOR into TINT. Without `met`, the door sets 131 and 270 and stays shut. | OK. The side path is hosted. The required chain does not enter it. |
| F4 | The Confidante header: the first meeting does not run once the chief's hut is smoked (local 6). The 2026-10-26 flow note calls this a stuck point. | Journal note `hut_smoked_before_password` says the alley talker is lost. | OK. Original stuck, kept. |
| F5 | HINTBOOK 5682–5684. The thief gives the sword the armorer otherwise sells, after Kelsrick is killed. | TDOOR buzzes (sfx 394) when flag 63 is set and flag 271 is clear, and when Kelsrick is dead while flag 28 is clear. Firestorm is granted once, on the return after the deal, and flag 63 is the same flag Kit'yara's shop sets. | OK. The two swords are one sword. Buying it first, or killing him before the deal, closes the door. The honest shop path does not need the door. |
| F6 | HINTBOOK 5684–5685. After that kill, a switch yields the king's stones. The flood path does not. | No handler in `thieves_den.gd` grants those stones or flips that switch. AP06 BRANCH-08a is a later village sentence (sword, then the king's stones) and was not re-checked against this den. | Original payoff not in the den room chain. It does not stop the Act 1 tavern chain. Listed for later. |
| F7 | Longplay order in the 2026-10-26 flow note, step K: Poison Paint kills Kelsrick and the alarm stays down. | `jungle_kelsrick.gd` sends a coated melee hit to record 30402, whose only shared write is `GV_KELSRICK_DEAD`. The alert writes sit on other hit groups. This pass did not strike him in Godot. | OK as hosted. Not re-run. |
| F8 | The alarm header: shared 29 == 1 and local 32 == 0 runs group 27172, soul −2, gates shut, Kelsrick hostile. | The same predicate and the opcode 206 value 254 are in `jungle_village_alarm_source.json` record 2. | OK. DECODED delta −2. |
| F9 | Confidante header: second meeting soul +1, a hit soul −1. | Groups 25584 (+1, owner state 2), 25628 and 25802 (−1, local 39 = 1). | OK. DECODED. |
| F10 | HINTBOOK 2254–2257. The armorer keeps the fire sword and the broken-sword repair for a Power Orb. | Kit'yara's plans name the orb and can grant Firestorm. Rashar mends `12-Tho Broken` only after flag 49, which the Power Orb offer sets, and that offer adds 1 to the soul value passed in. | OK. Two sellers, two deals, as the journal note `thohan_sword_broken` already says. |
| F11 | Chapter 15 and the soul byte. Being cruel in the village is a real path. | The writes in AW01's soul table land on `GV_LUTHERS_SOUL`. AP06 says no save field compares that byte: the Act 3 good and evil routes are their own quest fields. | The deltas are hosted. Their later payoff is not joined to the Act 3 branch tests. That does not stop the village chain. Listed for later. |
| F12 | `docs/bacatta-rooms.md`: an early walk-out leaves `GV_BACATTA_RELATIONSHIP` at 0, and Dawn's prerequisite is that relationship. | Same doc. The promise path raises it. | OK. Original dead end if the player leaves mid-promise. The book tells the player to finish the conversation. |
| F13 | Tavern-return doc: maid lines 700–709 set the alert and flag 267, and the tavern stays shut. | Hosted as that table. | OK. A side trap, after the player has already left and come back. |
| F14 | HINTBOOK 2343. The drunk is a joke. | Control 110 plays a movie. No choice function. | OK. No branch to miss. |
| F15 | Force gate, named in the den journal note, when the Confidante is dead and the alarm is up. | The note calls it the documented fallback. The leaf predicate is the older escape contract. | OK as a fallback. The required chain leaves through the open gate after the promise, with the alarm still clear. |

## Dead ends that are real, and who owns them

The player can close the side path and still finish the honest chain:

- Smoke the hut before the Confidante speaks. The password is gone. The tavern path does not use it.
- Kill the Confidante. Soul −1, local 39 set, the door never opens. The tavern path does not use it.
- Buy Firestorm from Kit'yara, then find the slot door. The door buzzes. The sword is already in hand.
- Kill Kelsrick before Mauri has spoken (flag 28). The door buzzes. The honest shops and the tavern do not use Mauri.
- Attack Mauri. Damage −1.
- Walk out of the cantina while flag 37 is set. The relationship stays 0. This one does sit on the required chain: Dawn's prerequisite, as the room doc states it, is that relationship. It is the original early-exit, and the hintbook tells the player not to abandon the conversation.

The player cannot, on the required chain, get stuck by skipping the thief, the drunk, LIZ, or Rashar's mend. Those are rewards and jokes.

## Orders

The original allows the shops, the drunk, the alley, and the den in any order, with two hard doors: the Confidante will not give the word after the hut is smoked, and the slot door will not open without the word, without the deal, or after Firestorm is already taken. Ours implements those doors.

Ours does not implement a tavern-last lock. The book does not state one as a flag.

Ours does not implement Baccata's attack. The book states that attack as a mistake, not as a step.

## Soul, and what it pays later

The village adds or subtracts `GV_LUTHERS_SOUL` at the Confidante (+1 once, −1 on a hit), the alarm (−2 once), Kelsrick's death group (−1), Kit'yara's kill records (−1), Bacatta's region-1921 and prop-552 groups (+2, +1, or −1), Bacatta65's record 79 (−1), and Rashar (+1 for the orb while the broken sword is held, −1 if he is killed). Kelsrick's writer clamps the stored soul to 0..10. Rashar's writer sets the global to the value the caller passed, plus or minus one.

`GV_BACATTA_RELATIONSHIP` is a different byte (index 13). The promise raises it. The early walk-out leaves it at 0. The prop-552 attack sets it to 0 and also subtracts 1 from `GV_DAWN_RELATIONSHIP`. That relationship is what the cantina doc says Dawn reads. AP06's Act 3 good and evil routes do not read the soul byte. A village soul delta therefore does not, by itself, select those endings in the hosted tests.
