# K03 Act 2 chain, part 3

No Godot was run. Newest owner file is still `TRIAGE_20261104.md`. HINTBOOK 3021–3076 is the return, the nine leaves, the fight, and the potion. BRADY printed 210, file marker PDF PAGE 211, lines 8512–8533, is Dawn, the Emperor, nine leaves are not numbered there, then steps 49–51. BRADY printed 177, lines 7506–7513, is the same potion in shorter form. The kill-the-shaman cache on that page is a different sentence and stays unmerged.

## Steps

Shore and Dawn. HINTBOOK 3021–3032: the wet exit wakes you on the lake shore; give Dawn the bracers; she talks about reflecting magic. BRADY lines 8512–8513: you are back on the banks of the Bane; talk to Dawn. Host: `l8_shore.gd`, `l8_dawn.gd`. Dawn is actor 20. The exchange completes before silverleaf may grow (`l10_silverleaf.gd` validate). Earned tests `l8_shore_earned_test.gd` (native shore selector 5, ruins stay shut) and `l8_dawn_earned_test.gd`. Verdict: HOSTED+TESTED.

Baccata, then the Emperor with no bracers, then the leaves. HINTBOOK 3034–3056: cut Baccata down just south of the cemetery path; the Emperor cannot be understood without the bracers; silverleaf then grows on the dead trees; pick nine and return. BRADY steps 48 and the leaf sentence at 8515–8517: last cemetery trip, then the bushes. Host: `l8_baccata.gd`, `l10_silverleaf.gd` props 159–170, `l10_silverleaf_harvest.gd`. Growth requires the Emperor remains flag and the Dawn exchange. Earned tests `l8_baccata_earned_test.gd`, `l10_silverleaf_growth_earned_test.gd` (12 props), `l10_silverleaf_harvest_earned_test.gd` (nine harvests, then the village with all nine). Verdict: HOSTED+TESTED.

Initiation. HINTBOOK 3068–3074: offering a silverleaf starts the fight with Daniel at once, not to the death, and Luther is then in the tribe. BRADY printed 92, lines 3759–3776, and step 49: give the leaf to the shaman and fight Daniel; if you killed Kityara he shows no mercy. Host: `l8_tribe.gd` / `l8_tribe_state.gd`. A leaf is definition 117. The bout starts only if `l8_journey.admitted` and the leaves have grown. Daniel in the bout is actor 23. Stamina is separate from campaign hit points. Earned tests `l8_initiation_earned_test.gd` and `l8_initiation_yield_earned_test.gd`. Verdict: HOSTED+TESTED for the nonlethal yield. The kill-Daniel branch is not this host.

Serum. HINTBOOK 3075–3076: offer the shaman another silverleaf; keep the potion for the Claw Mountains. BRADY step 50 and printed 177: Amaranth Serum after the fight. Host: `l8_shaman_trade.gd`. The leaf must be a second definition-117 item, not the one spent on the fight. Reward id `act2:L8_SJ:shaman_amaranth`, definition 119. Earned test `l8_shaman_trade_earned_test.gd`. Verdict: HOSTED+TESTED. Brady's kill-the-shaman cache is not this exchange. The tree-torch shard slot is a different object (`l8_tree_slot_state.gd`, definition 105).

Vapors and the Larkhon. HINTBOOK chapter 8 opening, lines 2868–2872, names the sleeping potion and the Larkon at the Claw Mountains. BRADY step 51 and printed 177, lines 7511–7513: mix serum with silverleaf; knock the tree, cross the logs, use the vapors on the upper chest. Host: `l8_larkhon.gd`. Mix needs definitions 117 and 119 and writes `act2:L8_SJ:larkhon_vapors`. The dose is a right-click on actor 115's upper chest while the vapors are active. Regions 3277 and 3278 stay blocked until the dose. The 60-second clock only plays the fall; the passage stays open after it (DEVIATIONS 0307, named in the script). Earned tests `l8_larkhon_earned_test.gd` (river jump, recipe, chest, native L12 selector 1) and `l8_larkhon_expiry_earned_test.gd`. Verdict: HOSTED+TESTED. The knocked-tree bridge is not inside the Larkhon test. That walk is the owner's L8-TREE-BRIDGE row and was I27. This pass did not re-read that file.

## Journal, including the owner's blocker

`l8_larkhon.gd` writes one note when the player is within 600 of actor 115, and only for the stage already earned:

| id | when |
| --- | --- |
| `larkhon_join_tribe` | not a tribe member. Tells him to show Daniel's blade to the guard first. |
| `larkhon_ask_shaman` | member, serum trade not done. Another silverleaf for the shaman. |
| `larkhon_serum_needs_leaf` | definition 119 is carried. Serum does nothing alone. |
| `larkhon_vapors_unactivated` | the mix exists and is not active. Activate, then the upper chest. |
| `larkhon_must_sleep` | none of those gaps. The creature is simply awake. |

The owner's save (gift recovered, admitted false, temple not visited, no tribe, no trade) matches the first row. `l8_guidance_test.gd` checks that placement. It is not an earned walk from the shore. Verdict for the note: HOSTED-UNTESTED.

Nothing in `my_journal.gd` covers Dawn, Baccata, the nine leaves, or the initiation. A player standing on the shore is not told to give up the bracers. Verdict: MISSING. Fix: `discover` from `l8_dawn.gd` while the bracers are still carried, and from `l8_tribe.gd` when the player is in the village with a leaf and is not yet a member. Anchors already exist. Wording is the K09 list.

## Still open

The mercy difference if Kityara died. Killing the shaman for the cache serum. The knocked-tree bridge as part of this earned walk. A journal line before the player has found actor 115.
