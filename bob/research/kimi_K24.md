# Kimi K24 — AH02 Act 3 stack save-chain audit (read-only, 2026-11-06)

Lead: P1 (registry order 801/803 inverted after the AB04 swap) and P3 (L19->L20 joint opens L20 fresh and carries only the dawn-curse packet; horn/items dropped; finale sets the horn instead of proving it is carried) are real -> grok list AR. P2/P4 are fine because ORDER.md applies the whole stack. P5/P6 doc nits.

# K24 — AH02 act3 stack: earned-test save-chain audit

  Scope: `ORDER.md` + all 23 diffs in `~/AI_COMMS/grok_research/patches/AH02_act3_stack/`. Diffs 19–22 (AB01–AB04) add no test files — they rewire the `reads` path of earlier earned tests; diff 23 (AA04) adds only a headless journal test (no earned test). The table shows the **final post-stack state** (AB rewiring applied), since `ORDER.md` mandates applying all diffs in order.

  | NN | diff | earned test | reads | writes | link ok | registry | PASS line | typed |
  |---|---|---|---|---|---|---|---|---|
  | 01 | S01_ne_tower | l16_ne_tower_earned_test | tmp/l16_greenhouse_earned_save.json (AH01 base) | tmp/l16_ne_tower_earned_save.json | ✓ origin | ✓ same diff (787) | ✓ | ✓ |
  | 02 | S02_se_oil | l16_se_oil_earned_test | tmp/l16_ne_tower_earned_save.json (rewired by AB01; originally greenhouse) | tmp/l16_se_oil_earned_save.json | ✓ | ✓ (789) | ✓ | ✓ (fixed by AB01; untyped as introduced) |
  | 03 | S03_nw_traps | l16_nw_traps_earned_test | tmp/l16_se_oil_earned_save.json (AB01) | tmp/l16_nw_traps_earned_save.json | ✓ | ✓ (791) | ✓ | ✓ (fixed by AB01) |
  | 04 | S04_sw_chips | l16_sw_chips_earned_test | tmp/l16_nw_traps_earned_save.json (AB01) | tmp/l16_sw_chips_earned_save.json | ✓ | ✓ (793) | ✓ | ✓ (fixed by AB01) |
  | 05 | T01_centre_tower | l16_centre_tower_earned_test | tmp/l16_sw_chips_earned_save.json (AB01) | tmp/l16_centre_tower_earned_save.json | ✓ | ✓ (795) | ✓ | ✓ (fixed by AB01) |
  | 06 | T02_dragon_room | l16_dragon_room_earned_test | tmp/l16_centre_tower_earned_save.json (AB02) | tmp/l16_dragon_room_earned_save.json | ✓ | ✓ (797) | ✓ | ✓ (fixed by AB02) |
  | 07 | T03_cavern_run | l17_cavern_run_earned_test | tmp/l16_dragon_room_earned_save.json (AB03; originally read nothing) | tmp/l17_cavern_run_earned_save.json | ✓ | ✓ (799) | ✓ | ✓ (fixed by AB03) |
  | 08 | T04_beast_wall | l19_beast_wall_earned_test | tmp/l17_beast_blade_earned_save.json (AB04; AB03 had cavern save; originally nothing) | tmp/l19_beast_wall_earned_save.json | ⚠ see P1 | ✓ (801) | ✓ | ✓ (fixed by AB04) |
  | 09 | W01_beast_wall_blade | l17_beast_blade_earned_test | tmp/l17_cavern_run_earned_save.json | tmp/l17_beast_blade_earned_save.json | ✓ (reads 07, not 08) | ✓ (803) | ✓ | ✓ |
  | 10 | W02_belial_horn | l19_belial_horn_earned_test | tmp/l19_beast_wall_earned_save.json | tmp/l19_belial_horn_earned_save.json | ✓ | ✓ (805) | ✓ | ✓ |
  | 11 | W03_sewer_forms | l19_sewer_forms_earned_test | tmp/l19_belial_horn_earned_save.json | tmp/l19_sewer_forms_earned_save.json | ✓ | ✓ (807) | ✓ | ✓ |
  | 12 | W04_drain_short_path | l19_drain_path_earned_test | tmp/l19_sewer_forms_earned_save.json | tmp/l19_drain_path_earned_save.json | ✓ | ✓ (809) | ✓ | ✓ |
  | 13 | W05_ghostly_heads | l19_ghostly_heads_earned_test | tmp/l19_drain_path_earned_save.json | tmp/l19_ghostly_heads_earned_save.json | ✓ | ✓ (811) | ✓ | ✓ |
  | 14 | X01_dawn_curse | l19_dawn_curse_earned_test | tmp/l19_ghostly_heads_earned_save.json | tmp/l19_dawn_curse_earned_save.json **and** tmp/l20_dawn_curse_earned_save.json | ✓ | ✓ (813) | ✓ | ✓ |
  | 15 | X02_pillars_scotia | l20_pillars_scotia_earned_test | tmp/l20_dawn_curse_earned_save.json | tmp/l20_pillars_earned_save.json | ✓ | ✓ (815) | ✓ | ✓ |
  | 16 | X03_armory | l20_armory_earned_test | tmp/l20_pillars_earned_save.json | tmp/l20_armory_earned_save.json | ✓ | ✓ (817) | ✓ | ✓ |
  | 17 | X04_faux_draracle | l20_faux_draracle_earned_test | tmp/l20_armory_earned_save.json | tmp/l20_faux_draracle_earned_save.json | ✓ | ✓ (819) | ✓ | ✓ |
  | 18 | X05_finale | l20_finale_earned_test | tmp/l20_faux_draracle_earned_save.json | tmp/l20_finale_earned_save.json | ✓ finale reached | ✓ (821) | ✓ | ✓ |
  | 19–22 | AB01–AB04 | (none added; rewire reads of 02–08) | — | — | — | — | — | — |
  | 23 | AA04_act3_findable | (no earned test; adds headless act3_journal_hints_test) | — | — | — | ✓ (858) | ✓ | ✓ |

  Chain after full apply: greenhouse → 01 → 02 → 03 → 04 → 05 → 06 → 07 → **09 → 08** → 10 → 11 → 12 → 13 → 14 → 15 → 16 → 17 → 18 (finale). Declared branches: the STORY-080 swap (AB04 DEVIATIONS entry) puts the L17 blade cut before the L19 lab entry; AB01–AB03 DEVIATIONS entries declare the serial rewiring of the S/T chain. All `attach()` helpers use typed `var n: Node = load(...).new()`; base class `tests/l12_logs_approach_earned_test.gd` exists in the base tree.

  ## Problems

  1. **P1 — Run-order inversion at 08/09.** Post-AB04, `l19_beast_wall_earned_test` (diff 08, registry order **801**) reads `l17_beast_blade_earned_save.json`, written by `l17_beast_blade_earned_test` (diff 09, registry order **803**). Registry order was never renumbered, so a runner executing in registry order hits T04 before W01 and the input save does not exist on a clean run. The swap is *declared* (AB04's DEVIATIONS row), but the registry contradicts it.
  2. **P2 — Chain is only serial after the AB diffs.** As introduced, tests 02–08 all read the greenhouse save directly (parallel branches) or read no save at all (07, 08). The "one chain" property holds only in the final tree; any partial application (or review of an individual diff in isolation) shows broken links. ORDER.md mitigates this by mandating full-order application.
  3. **P3 — L19→L20 handoff inside test 14 is thin.** `l19_dawn_curse_earned_test` frees the L19 scene, opens L20 fresh (not from the just-written save), and injects only the `l19_dawn_curse` packet (`scene.quest_state["l19_dawn_curse"] = packet`). All other accumulated chain state (horn, heads shots, sewer/drain flags, carried items) is dropped at this joint, and no later test checks it — e.g. test 18 starts the finale by setting `scene.equipped_item = "act2:L19_BC:horn"` without verifying the horn is carried. Also, test 14's first output `l19_dawn_curse_earned_save.json` is a dead intermediate: written, reloaded only inside test 14, never read by any other test.
  4. **P4 — Typed-variable rule violated in intermediate states.** Diffs 02–07 introduce the scene as untyped `var scene = load(...).instantiate()`; only the later AB0x hunks add `: Node`. Final tree is clean everywhere, but the stack relies on its own fix-up diffs.
  5. **P5 — ORDER.md dangling reference.** Line 3: "AB01 through AB04 stay separate diffs, in the AB05 order" — no AB05 exists in the stack (presumably means the listed order).
  6. **P6 — Registry order gap (minor, informational).** Earned orders run 786–821 contiguously; AA04's headless test takes 858. The 822–857 gap presumably belongs to base-tree tests, but nothing in the stack documents it.

  No missing registries, no missing PASS lines, and no unresolved `load().new()`/`instantiate()` typing in the final tree.

