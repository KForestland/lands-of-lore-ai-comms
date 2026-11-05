# K01 Act 2 chain, part 1

No Godot was run. Newest owner file is still `TRIAGE_20261104.md`. Grades: HINTBOOK for the hintbook lines, BRADY for the Brady lines, DECODED for the script and test text. The two books disagree on hut order and on killing the shaman. Those sentences stay unmerged.

The mechanical steps below are hosted. A player who has not reached the Larkhon still has no My Journal line for this chain. The one line that names it is `larkhon_join_tribe`, and it is written only within 600 units of actor 115.

## Steps

Arrival. HINTBOOK 2866–2872: the Savage Jungle is the hub, and the goal is the Huline Temple. BRADY printed 89, file marker PDF PAGE 90, lines 3571–3586: Luther is on the east bank of the River Bane after Baccata leaves, and he cannot go back. Host: `darker_jungle.gd` loads native arrival `L8_SJ` from the save selector. Earned test `l8_gift_earned_test.gd` opens the pinned Act 1 arrival save and walks native points near selector 1 to the Daniel anchor. Verdict: HOSTED+TESTED. The dragon movie is not in that test.

Daniel's gift. HINTBOOK 2896–2922: put the curved knife on Daniel's chest, hear "Grandfather's blade", then pick the knife up when the hoppers scatter. BRADY printed 89, lines 3585–3598: one of the three Wild Ones is Daniel; click Kityara's knife; they scatter; pick up the knife; go south. Host: `l8_journey.gd` / `l8_journey_state.gd`. Anchor `Vector3(-3854, 32, 1190)`, actor 93, reach 160. Actions `offer_daniel`, `hopper_interruption`, `recover_blade`. Blade id `jungle:kityara:Empty_hand`. Earned test `l8_gift_earned_test.gd` (it prints STORY-001) walks there, refuses a wrong offer, and save/reloads each action. Verdict: HOSTED+TESTED. The test's own note says rendered presentation is not qualified. No hopper movie is claimed (DEVIATIONS, the first-departure row).

Temple, first visit. HINTBOOK 2934–2938: the first approach plays the priest being snatched. BRADY printed 89–90, lines 3597–3611: the temple is the south tapering path; the Caretaker speaks, then Belial's first incarnation appears. BRADY printed 91, lines 3685–3686: the settlement stays closed until that talk. Host: same panel, anchor `Vector3(758, 32, 2046)`, prop 1198, action `visit_temple`. That sets `temple_visited` and makes guard actor 113 present. Earned test `l8_temple_earned_test.gd` (STORY-002) walks `l8_first_departure_walk.json` to the temple, commits, save/reloads, then walks to the village anchor. Verdict: HOSTED+TESTED. The scene text is a summary, not the movie.

Village admission. HINTBOOK 2979–2984: show Daniel's gift to the guard; do not attack. BRADY printed 92, lines 3694–3703: the guard shoots; show the knife; without it you fight in. Host: anchor `Vector3(676, 32, -4541)`, actor 113, action `show_guard`. The blade stays in inventory. Admission requires `temple_visited` and gift `recovered`. Earned test `l8_departure_earned_test.gd` calls `show_guard` with the blade and checks it is not consumed. Verdict: HOSTED+TESTED. The fight-your-way-in branch is not this action.

Return the blade, then the shaman. HINTBOOK 2991–3005: hand the gift to Daniel in his treehouse, click the shaman, and go to the Dracoid Cemetery because no silverleaf is growing yet. The same page puts the herbalist on the left and Daniel on the left. BRADY printed 92, lines 3730–3753: Daniel's hut is left, the herbologist is right, Malik is center; Malik asks for silverleaf from the cemetery and, if you have not attacked the Wild Ones, gives the cemetery key; if you have attacked them, the book says to kill him for the key. Host: `offer_daniel` at the village consumes the blade only after admission. `visit_shaman` appends `l8:shaman:Dracoid_sigil` (the script comment names original definition 102, `100-Drac sigil`). Earned test `l8_departure_earned_test.gd` runs `show_guard`, `offer_daniel`, `visit_shaman`, save/reloads each, then walks the native departure and checks level 10 selector 1. Verdict: HOSTED+TESTED for the peaceful key. The kill-Malik key is not this host.

Cemetery gate. The chapter-8 send-off is the cemetery errand, not the tombs. Host: `l10_main_gate.gd` unlocks with the same sigil id. Earned test `l10_gate_earned_test.gd` changes into L10 with the sigil, walks to the gate, checks the closed gate blocks, refuses a wrong item, unlocks, save/reloads, and walks past the leaves. Verdict: HOSTED+TESTED.

## Journal a lost player would see

`my_journal.gd` does not load `l8_journey.gd`. Nothing is written at actor 93, prop 1198, or actor 113.

`l8_larkhon.gd` writes a note when the player is within 600 of actor 115. If `l8_tribe` is not a member, the id is `larkhon_join_tribe`: "Only the shaman can make the Larkhon sleep, and he helps his tribe alone. Show Daniel's blade to the village guard first." That is the owner's r14 case (gift recovered, admitted false, temple not visited). `l8_guidance_test.gd` checks that id on a placed probe. It is not an `*_earned_test.gd` walk. Verdict: HOSTED-UNTESTED.

The five steps before the Larkhon have no note. Verdict: MISSING. Fix: from `L8Journey`, `discover` when `target()` is set and the next action is still open. Anchors already in `TARGETS`. Three ids are enough: blade still unoffered at the entry anchor; blade recovered and temple not visited; temple visited and not admitted. Wording belongs on the K09 list. Do not invent a second admission flag.

## Still open

The fight-in admission and the kill-Malik key. The FMV at Daniel and at the temple. Whether a player who never walks near actor 115 is told the order temple, then guard, then shaman.
