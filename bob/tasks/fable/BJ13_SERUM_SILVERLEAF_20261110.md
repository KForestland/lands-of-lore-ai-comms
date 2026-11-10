# BJ13: serum and Silverleaf as a player gets them (lead, 2026-11-10; owner top priority for Thursday's r19)
METHOD TRIAL (owner 2026-11-10): Fable writes the plan (fable_lane/BJ13_PLAN.md), the lead builds it. The steps below are the plan's input; Fable does not code them.
Owner: "the main problem is the village in savage jungle"; "the items seems be the contention here. serum and silver leaf".
Start after BJ12's affected gate and the F2 full-health commit. Stack on bj12-l8-quests. Limits: max 2 Godot, MemAvailable >= 10 GiB, Dummy audio.
Ledger 0550-0599, registry 1250-1299. Post STOP lines and READY per fix on the board, signed [fable].

Hint book: Emperor's spirit -> leaves grow on the dead cemetery trees, pick nine (~3040) -> initiation at the village -> shaman: offer a leaf, he gives the
amaranth potion (3075) -> combine potion + leaf BY HAND (the Claw Mountains river passage, ~3150) -> left click on Luther, right click the Larkhon's upper chest.
Tree-platform room: back-of-room slots make another potion from amaranth + leaf (3119). Longplay frames from 109:40 (longplay_frames_act2plus).

In order:
1. Walk both items end to end as a player from the F2 start on real input, no test aids: can he see the leaves on the trees after the Emperor, pick them, see them
   in the pack with the right icon and name, offer one, get the serum, keep it across save/reload, and is it clear at each step what to do next? Publish the STOP list first.
2. Fix those stops in chain order.
3. FIRST FIX, ahead of the rest of the stops: the mixing slots in the raised tree room (book 3119: amaranth potion + Silverleaf in the slots at the back of the room make the Larkhon potion). Ledger 0551 says these are not hosted; tests/l8_tree_room_earned_test.gd hosts only the shard slot. Real input, real items, save/reload.
4. By-hand combine: pack item dropped on pack item (serum on leaf and leaf on serum), as the book says. Keep the existing buttons as well.
5. Only then, if time allows before Wednesday's cutoff: the real village views. room_stems.json has VILLAGE, HERB, SHAMAN and DANIEL from LOLG.DAT, VILLAGE_.VQA is already
   converted (assets/lol2/generated/bacatta_rooms), and monastery_room_view.gd is the working pattern. Say first if the other three VQAs cannot be sourced.
   Owner's reference shots: ~/Downloads/LoL2_P3_106..111_L8-WildVillage_*.png. The current text panel stays until the art version passes.
OWNER 2026-11-10 answered: the "small hut" is where the potion and leaf are mixed, i.e. the raised tree room. The serum itself still comes from the shaman (book 3075).
