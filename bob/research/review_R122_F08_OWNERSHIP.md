# R122 review: F-08 item ownership at a95a90c

Verdict: MERGE.

Head `a95a90cc4e131c75ee8b36ca1e4dcb2e17a36b86` on `sol/f08-ownership-20261114` in `~/opus_work/lol2_sol_workorder2_items_next`, parent `9d1061c`. Commits 2-9 are `be6de4e`, `165dd68`, `7c69d03`, `c91b024`, `d466a2f`, `3a76bcf`, `2273465`, `3e90435`, `a95a90c`. This lane did not edit the tree. Untracked `assets/lol2/dark_halls/` and `assets/lol2/doors/indices_478.png` are not in the commits.

Doc followup `16f2cc184cbc5c0a19e897e8f3174658de5d5150` on `sol/f08-ledger-fix-20261114` is four ledger files (`docs/DEVIATIONS.md` and the 0643 row pieces). No script, scene, or test changes. Take it with the gameplay head.

## Seven MINORs

1. Pure builders are unchanged against `9d1061c`: `l10_emperor_state.gd`, `l13_altar_state.gd`, `l13_dawn_release.gd`, `l8_journey_state.gd`, `l10_silverleaf_harvest.gd`, `l8_herbalist.gd`, `player_item_effects.gd`. `l10_priest.gd` and `l10_silverleaf.gd` only move callers onto `Grants.commit`.
2. `commit` defaults `cap` false. An oversized commit without `cap` succeeds. Cave `grant` and `commit` refuse with `push_error` and change nothing. Re-ran `tests/item_grants_test.gd`: PASS (shared contract, Cave refusals, scope map, cap defaults, duplicates, history, sync, text, Journal, HUD).
3. `l12_frozen_bow.gd`, `l14_hopper_platform.gd`, and `l16_dry_fountain.gd` use `duplicate:"allow"`. Each owner checks capacity before it writes its own taken state. A second call is stopped by that owner's own guard.
4. `act2_world_items.gd` `take` returns when `grant` is not ok, then re-reads `quest_state.act2_items` and sets `carried` from the live pack. A second E does not append.
5. `native()` refuses unless `opcode3_item_grant` is true and `global_223d4` is 0. The host stages that effect only when the adapter is on and the global is 0. Shipped table is 876 commands: 862 log, 14 owner, 0 grant. Log-row grades cite DEVIATIONS 0191. The 14 owner-row grades say the callee and argument are still UNKNOWN and do not contain the digits 0191. `docs/item-grant-native-dispatch.md` cites 0191. That is a documentation miss on the owner rows.
6. `tests/item_grant_tables_test.gd` walks the native groups itself and pins the per-level counts (total 876) and `action` in `log` or `owner`. No live grant row, so there is no rendered press-E-again case. The dispatch test asserts the second group runs while the pack stays one copy.
7. Host-to-scope is written in `item_grants.gd` and the unit test checks one id per family. `f08/CAPACITY_TEXTS.json` has 19 refusal spellings. The census fixture's `capacity_refusal_texts` length is 16. Old-save test pins the 36 golden packets by sha256 `dc9ca133b30471f7c4e42372e23994294e469aba3fdceb372aa8987761a9b792` plus 2 pre-stamp packets. Goldens were not regenerated.

## Section 13

`duplicate:"skip"` skips only the append. Text, HUD, history, sync, and Journal still run, and the result carries `added`. A full pack on skip still runs effects and does not take the cap refusal. `sync` with `history:"none"` works. `sync_first` without `sync` is an error. The same unit run pins those.

## Real input

Private display :231, Dummy audio, `time_scale` 1, physics 60. Place and aim are named aids. `act2_creatures` held on the two maps. Keys were E, I, Escape, F5, F9. The script did not call `grant`, `take`, or `commit`.

| Level | Stand | Result |
| --- | --- | --- |
| Museum summon scroll `museum:item16:Summon_Scroll` | (-1937, 32, -1128), aimed at the sprite | E once, count 1. Second E still 1. F5 "Museum saved." F9 count 1, no other pack change, pose kept |
| L8 control token `act2:L8_SJ:item31` | (-1608, 61, 900), region 2934 floor 0 | E "Control tokn taken.", history true, count 1. Second E still 1. F9 count 1, no other pack change, pose kept |
| L14 mists scroll `act2:L14_HT:item20` | pad (1933, -93, -1221); the room floor at y -100 blocks the ray from the rim | E "MoDScrl taken.", history true, count 1. Second E still 1. Pitch on the pad is past the save limit of 1.4 rad, so the body was moved to the rim (1910, -68, -1221) and the camera leveled, then F5 "L14_HT preview saved." F9 count 1, pose kept. Slot 1 carries `item20`, `act2:L8_SJ:dawn_control_token`, and `act2:L10_DC:silverleaf167` once each |

Inventory buttons on the three levels were Unequip, Use, Hold in hand or Hold for exhibit, Mix with Silverleaf on L8, and Close. None says Drop. This build has no player ground-drop (commit 10 / I-17 stays deferred). The walked check is pickup, a second E that does not copy, and F5/F9 keeping the same id.

Dampen, the other mists and prism placements, and the Dawn shore exchange go through `Grants.grant`, `Grants.commit`, or `Grants.pack` in source. The live walks are the museum summon scroll, the L8 world token, and the L14 mists scroll.

This lane does not apply the merge.
