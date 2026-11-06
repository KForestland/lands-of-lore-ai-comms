# Kimi K16 — verify K02_act2_cemetery_ruins.md + K03_act2_serum_larkhon.md names against lol2_r15 (read-only, 2026-11-06)

Lead spot-check: l9_chapel.gd and l9_bracers.gd do not exist in r15 (real hosts l9_pyre.gd, l9_dead_bracers.gd) - CONFIRMED, doc naming error only. larkhon_join_tribe absent in r15 - correct; it was added on act3-story 11-05 and ships in r16 (see kimi_K15.md). Nothing to fix in code.

Let me read the two files first.Now I need to extract every named script file, test file, function, constant, and id from both docs and verify each exists in ~/opus_work/lol2_r15.

  From K02:
  - TRIAGE_20261104.md (owner file, likely in AI_COMMS? "Newest owner file is still TRIAGE_20261104.md" — probably should check in lol2_r15 too; the task says check in lol2_r15. I'll check both but flag per task.)
  - l10_main_gate.gd
  - l10_catacomb_earned_test.gd
  - l10_gold_earned_test.gd
  - l10_barrel.gd
  - l10_oil.gd
  - `ignite` (function)
  - `BLAST_RADIUS` (constant)
  - l10_two_empty_earned_test.gd
  - l10_barrel_earned_test.gd
  - l10_oil_earned_test.gd
  - l10_blue_earned_test.gd
  - l10_fence_earned_test.gd
  - l10_priest.gd
  - prop 158
  - id `act2:L10_DC:priest_urn`
  - id `act2:L9_DR:item55`
  - def 78
  - l10_priest_earned_test.gd
  - l9_chapel.gd, l9_pyre.gd
  - body 2406, pyre 301, orbs 1205 and 1206
  - l10_ruins_departure_earned_test.gd, l9_opening_earned_test.gd, l9_chapel_earned_test.gd, l9_ashes_earned_test.gd, l10_ashes_return_earned_test.gd
  - l9_tower.gd, l9_bracers.gd, l9_mirrors.gd
  - l9_tower_approach_earned_test.gd, l9_two_white_earned_test.gd, l9_bracers_earned_test.gd, l9_mirror_return_earned_test.gd
  - l9_tower_blank_earned_test.gd
  - l10_ankh_state.gd, l10_emperor.gd
  - l10_ankh_earned_test.gd, l10_emperor_supply_earned_test.gd, l10_emperor_earned_test.gd
  - l9_statue.gd (region 3185, prop 2622), l9_statue_walk.gd, l9_flood.gd, l9_escape.gd (table 122, raft 82)
  - l9_statue_earned_test.gd, l9_statue_follow_earned_test.gd (movie 54), l9_flood_earned_test.gd, l9_flood_escape_earned_test.gd
  - `discover` (function call), my_journal? not in K02 named
  - l9_*.gd / l10_*.gd no discover() call — check grep discover in those files.

  From K03:
  - TRIAGE_20261104.md
  - l8_shore.gd, l8_dawn.gd
  - Dawn is actor 20
  - l10_silverleaf.gd (validate function)
  - l8_shore_earned_test.gd, l8_dawn_earned_test.gd
  - l8_baccata.gd, l10_silverleaf_harvest.gd, props 159–170
  - l8_baccata_earned_test.gd, l10_silverleaf_growth_earned_test.gd, l10_silverleaf_harvest_earned_test.gd
  - l8_tribe.gd / l8_tribe_state.gd
  - definition 117
  - `l8_journey.admitted` — check l8_journey file and `admitted`
  - actor 23 (Daniel)
  - l8_initiation_earned_test.gd, l8_initiation_yield_earned_test.gd
  - l8_shaman_trade.gd
  - id `act2:L8_SJ:shaman_amaranth`, definition 119
  - l8_shaman_trade_earned_test.gd
  - l8_tree_slot_state.gd, definition 105
  - l8_larkhon.gd
  - definitions 117 and 119, writes `act2:L8_SJ:larkhon_vapors`
  - actor 115
  - regions 3277, 3278
  - DEVIATIONS 0307
  - l8_larkhon_earned_test.gd, l8_larkhon_expiry_earned_test.gd
  - journal note ids: larkhon_join_tribe, larkhon_ask_shaman, larkhon_serum_needs_leaf, larkhon_vapors_unactivated, larkhon_must_sleep
  - l8_guidance_test.gd
  - my_journal.gd
  - `discover`

  Strategy: first glob for all the filenames in lol2_r15, then grep within specific files for the ids/functions/constants. Let me batch this efficiently with grep searches.

  Let me start with globbing the filenames. Actually, Grep files_with_matches with patterns for filenames is easier via Glob with pattern like "**/l10_*.gd". Let me do a series of Glob calls in parallel, plus Grep calls for ids.

  Files to glob:
  - TRIAGE_20261104.md (in lol2_r15)
  - K02: l10_main_gate.gd, l10_catacomb_earned_test.gd, l10_gold_earned_test.gd, l10_barrel.gd, l10_oil.gd, l10_two_empty_earned_test.gd, l10_barrel_earned_test.gd, l10_oil_earned_test.gd, l10_blue_earned_test.gd, l10_fence_earned_test.gd, l10_priest.gd, l10_priest_earned_test.gd, l9_chapel.gd, l9_pyre.gd, l10_ruins_departure_earned_test.gd, l9_opening_earned_test.gd, l9_chapel_earned_test.gd, l9_ashes_earned_test.gd, l10_ashes_return_earned_test.gd, l9_tower.gd, l9_bracers.gd, l9_mirrors.gd, l9_tower_approach_earned_test.gd, l9_two_white_earned_test.gd, l9_bracers_earned_test.gd, l9_mirror_return_earned_test.gd, l9_tower_blank_earned_test.gd, l10_ankh_state.gd, l10_emperor.gd, l10_ankh_earned_test.gd, l10_emperor_supply_earned_test.gd, l10_emperor_earned_test.gd, l9_statue.gd, l9_statue_walk.gd, l9_flood.gd, l9_escape.gd, l9_statue_earned_test.gd, l9_statue_follow_earned_test.gd, l9_flood_earned_test.gd, l9_flood_escape_earned_test.gd
  - K03: l8_shore.gd, l8_dawn.gd, l10_silverleaf.gd, l8_shore_earned_test.gd, l8_dawn_earned_test.gd, l8_baccata.gd, l10_silverleaf_harvest.gd, l8_baccata_earned_test.gd, l10_silverleaf_growth_earned_test.gd, l10_silverleaf_harvest_earned_test.gd, l8_tribe.gd, l8_tribe_state.gd, l8_journey (l8_journey.gd presumably), l8_initiation_earned_test.gd, l8_initiation_yield_earned_test.gd, l8_shaman_trade.gd, l8_shaman_trade_earned_test.gd, l8_tree_slot_state.gd, l8_larkhon.gd, l8_larkhon_earned_test.gd, l8_larkhon_expiry_earned_test.gd, l8_guidance_test.gd, my_journal.gd

  I can glob "**/l9_*.gd", "**/l10_*.gd", "**/l8_*.gd" and "**/my_journal.gd", "**/TRIAGE_20261104.md" — three big globs covering everything. But l8/l9/l10 might have many files; that's fine.

  Then grep for:
  - `BLAST_RADIUS`, `func ignite` or `ignite`
  - `act2:L10_DC:priest_urn`
  - `act2:L9_DR:item55`
  - `act2:L8_SJ:shaman_amaranth`
  - `act2:L8_SJ:larkhon_vapors`
  - journal note ids (larkhon_...)
  - `admitted` in l8_journey
  - `discover` in l9_*.gd / l10_*.gd
  - region 3185, prop 2622, table 122, raft 82, props 159–170, definition 117/119/105/78, prop 158, actor 115/20/23, body 2406, pyre 301, orbs 1205/1206, regions 3277/3278 — these are ids within scripts; checking them precisely requires reading the specific scripts. Given the task scope, I should check the numeric ids in the relevant files.

  This is a fair amount of work. Let me do it myself with parallel greps.

  First batch: globs for files.

I'll verify both docs against the project. First, locating all named files.

The default working directory is the scratchpad, not lol2_r15. I need to pass path=~/opus_work/lol2_r15.

The globs defaulted to the scratchpad; rerunning against the project root.

Missing files so far:

  K02:
  - `l9_chapel.gd` — NOT in the l9 list. There is `l9_chapel_earned_test.gd` test but no `scripts/lol2/l9_chapel.gd`. MISSING.
  - `l9_bracers.gd` — NOT in l9 list. There is `l9_dead_bracers.gd` and test `l9_bracers_earned_test.gd`. MISSING (though l9_dead_bracers.gd may be the actual host — mismatch worth flagging).
  - `l10_ruins_departure_earned_test.gd` — exists ✓
  - All others seem present. Let me double-check K02 list against results:
    - l10_main_gate.gd ✓
    - l10_catacomb_earned_test.gd ✓
    - l10_gold_earned_test.gd ✓
    - l10_barrel.gd ✓
    - l10_oil.gd ✓
    - l10_two_empty_earned_test.gd ✓
    - l10_barrel_earned_test.gd ✓
    - l10_oil_earned_test.gd ✓
    - l10_blue_earned_test.gd ✓
    - l10_fence_earned_test.gd ✓
    - l10_priest.gd ✓
    - l10_priest_earned_test.gd ✓
    - l9_chapel.gd ✗
    - l9_pyre.gd ✓
    - l10_ruins_departure_earned_test.gd ✓
    - l9_opening_earned_test.gd ✓
    - l9_chapel_earned_test.gd ✓
    - l9_ashes_earned_test.gd ✓
    - l10_ashes_return_earned_test.gd ✓
    - l9_tower.gd ✓
    - l9_bracers.gd ✗ (l9_dead_bracers.gd exists)
    - l9_mirrors.gd ✓
    - l9_tower_approach_earned_test.gd ✓
    - l9_two_white_earned_test.gd ✓
    - l9_bracers_earned_test.gd ✓
    - l9_mirror_return_earned_test.gd ✓
    - l9_tower_blank_earned_test.gd ✓
    - l10_ankh_state.gd ✓
    - l10_emperor.gd ✓
    - l10_ankh_earned_test.gd ✓
    - l10_emperor_supply_earned_test.gd ✓
    - l10_emperor_earned_test.gd ✓
    - l9_statue.gd ✓
    - l9_statue_walk.gd ✓
    - l9_flood.gd ✓
    - l9_escape.gd ✓
    - l9_statue_earned_test.gd ✓
    - l9_statue_follow_earned_test.gd ✓
    - l9_flood_earned_test.gd ✓
    - l9_flood_escape_earned_test.gd ✓

  K03:
    - l8_shore.gd ✓
    - l8_dawn.gd ✓
    - l10_silverleaf.gd ✓
    - l8_shore_earned_test.gd ✓
    - l8_dawn_earned_test.gd ✓
    - l8_baccata.gd ✓
    - l10_silverleaf_harvest.gd ✓
    - l8_baccata_earned_test.gd ✓
    - l10_silverleaf_growth_earned_test.gd ✓
    - l10_silverleaf_harvest_earned_test.gd ✓
    - l8_tribe.gd ✓
    - l8_tribe_state.gd ✓
    - l8_journey.gd ✓ (referenced as `l8_journey.admitted`)
    - l8_initiation_earned_test.gd ✓
    - l8_initiation_yield_earned_test.gd ✓
    - l8_shaman_trade.gd ✓
    - l8_shaman_trade_earned_test.gd ✓
    - l8_tree_slot_state.gd ✓
    - l8_larkhon.gd ✓
    - l8_larkhon_earned_test.gd ✓
    - l8_larkhon_expiry_earned_test.gd ✓
    - l8_guidance_test.gd ✓
    - my_journal.gd ✓
    - TRIAGE_20261104.md — not in lol2_r15 (probably lives in AI_COMMS). Flag as not found in lol2_r15.

  Now grep for functions/constants/ids:

  K02:
  - `ignite` in l10_oil.gd (and l10_barrel?) — grep "ignite" in scripts/lol2/l10_oil.gd
  - `BLAST_RADIUS` — grep across scripts
  - `act2:L10_DC:priest_urn`
  - `act2:L9_DR:item55`
  - `discover(` in l9_*.gd and l10_*.gd — the doc says "No discover() call exists in l9_*.gd or l10_*.gd" — verify claim: grep should return nothing.
  - prop 158 in l10_priest.gd
  - def 78 (gift def) in l10_priest.gd?
  - body 2406, pyre 301, orbs 1205/1206 in l9_pyre.gd (and chapel?) — check l9_pyre.gd
  - region 3185, prop 2622 in l9_statue.gd
  - table 122 and raft 82 in l9_escape.gd
  - movie 54 in l9_statue_follow_earned_test.gd? The doc says "movie 54" in statue follow test print.

  K03:
  - `validate` in l10_silverleaf.gd
  - `admitted` in l8_journey.gd (or l8_journey_state.gd)
  - definition 117 in l8_tribe.gd / l8_shaman_trade.gd / l8_larkhon.gd
  - definition 119 in l8_shaman_trade.gd / l8_larkhon.gd
  - `act2:L8_SJ:shaman_amaranth`
  - `act2:L8_SJ:larkhon_vapors`
  - definition 105 in l8_tree_slot_state.gd
  - actor 115, regions 3277/3278, "DEVIATIONS 0307" or "0307" in l8_larkhon.gd
  - journal note ids: larkhon_join_tribe, larkhon_ask_shaman, larkhon_serum_needs_leaf, larkhon_vapors_unactivated, larkhon_must_sleep in l8_larkhon.gd (and my_journal.gd)
  - Dawn actor 20 in l8_dawn.gd
  - actor 23 Daniel in l8_tribe.gd
  - props 159–170 in l10_silverleaf.gd
  - `discover` — check exists in my_journal.gd or as a function (doc says fix via discover; anchors exist)

  Let me run a batch of greps. For evidence lines, use output_mode content with -n, head limits.

  Batch 1 greps:
  1. Grep "ignite" path=scripts/lol2/l10_oil.gd content
  2. Grep "BLAST_RADIUS" path=~/opus_work/lol2_r15/scripts content
  3. Grep "priest_urn" path=root content (id string)
  4. Grep "act2:L9_DR:item55" 
  5. Grep "discover" glob l9_*.gd and l10_*.gd in scripts/lol2 — check claim of absence. Pattern "discover" path=scripts/lol2 glob="l9_*.gd" plus glob l10.
  6. Grep "158" in l10_priest.gd — need "prop 158"; grep pattern "158".
  7. Grep "2406|301|1205|1206" in l9_pyre.gd — careful, 301 may appear elsewhere. Use pattern "2406|1205|1206" and separately "301". Maybe pattern "2406|1205|1206|[^0-9]301[^0-9]".
  8. Grep "3185|2622" in l9_statue.gd.
  9. Grep "122|[^0-9]82[^0-9]" in l9_escape.gd.
  10. Grep "movie 54|54" in l9_statue_follow_earned_test.gd — pattern "54".

  Batch 2 (K03):
  11. Grep "validate" in l10_silverleaf.gd
  12. Grep "admitted" in l8_journey.gd and l8_journey_state.gd
  13. Grep "117" in l8_tribe.gd, l8_shaman_trade.gd, l8_larkhon.gd
  14. Grep "shaman_amaranth|119" in l8_shaman_trade.gd
  15. Grep "larkhon_vapors" in root
  16. Grep "105" in l8_tree_slot_state.gd
  17. Grep "115|3277|3278|0307" in l8_larkhon.gd
  18. Grep "larkhon_join_tribe|larkhon_ask_shaman|larkhon_serum_needs_leaf|larkhon_vapors_unactivated|larkhon_must_sleep" in scripts
  19. Grep "actor 20|\b20\b" in l8_dawn.gd — pattern "20" 
  20. Grep "23" in l8_tribe.gd
  21. Grep "15[9]|16[0-9]|170" in l10_silverleaf.gd
  22. Grep "discover" in my_journal.gd and scripts generally

  That's a lot but manageable. I can put many Grep calls in parallel. Grep path accepts a file path. Let me do batch of ~12 parallel calls, then batch 2.

All file locations are resolved. Now grepping for the functions, constants, and ids named in the docs.

K02 checks mostly confirmed. Note:
  - `discover` absent from l9_*.gd and l10_*.gd scripts — confirms doc's claim.
  - l9_chapel.gd missing as a script (only test exists).
  - l9_bracers.gd missing as a script; l9_dead_bracers.gd exists instead.

  Now K03 greps.

K02 internals verified so far. Now the K03 internals.

A few more things to verify:

  K02:
  - `l9_chapel.gd` — confirmed not in scripts/lol2. But maybe it exists elsewhere? The glob covered whole repo `**/l9_*.gd`, so l9_chapel.gd doesn't exist anywhere in lol2_r15. But wait, the chapel logic might live in l9_pyre.gd. K02 names `l9_chapel.gd` as host — it's MISSING.
  - `l9_bracers.gd` — not in glob results; `l9_dead_bracers.gd` is the actual script. MISSING as named (mismatch).
  - prop 158 — confirmed in l10_priest.gd:3 ("prop158") and docs.
  - def 78 — confirmed ("def78" in l10_priest.gd:3, "definition":78 in catalog).
  - K02 journal section says "Fix: one discover on l10_oil.gd..." — discover exists in my_journal.gd:46. ✓ (but as noted, no calls in l9/l10 — matches the doc's own claim).
  - `ignite` accepts spark levels 1, 3, 5 — check l10_oil.gd line ~110 to verify levels. The doc claims it; I could read lines 105-120 for confirmation. Might be good for the evidence but the task only requires existence of named function `ignite` and constant `BLAST_RADIUS` — both confirmed at lines 110 and 6.
  - `l8_journey.admitted` — confirmed in l8_journey.gd:56 and l8_journey_state.gd.

  K03 remaining:
  - `act2:L8_SJ:larkhon_vapors` id — grep showed "larkhon_vapors" matches but those were `larkhon_vapors_unactivated` note id and maybe the item id. Need to check the exact item id string `act2:L8_SJ:larkhon_vapors`. Let me grep.
  - Dawn actor 20 — confirmed l8_dawn.gd.
  - actor 23 Daniel — confirmed l8_tribe.gd.
  - actor 115 — confirmed l8_larkhon.gd:31.
  - regions 3277/3278 — confirmed line 83.
  - DEVIATIONS 0307 — confirmed line 14.
  - definition 117 — confirmed in l8_tribe? Actually l8_tribe.gd grep pattern included 117 but results showed lines 22, 44, 51, 63, 70, 106 — no 117 line shown for l8_tribe. Hmm, the head_limit 15 shouldn't have cut; maybe l8_tribe.gd doesn't contain "117". The doc says "A leaf is definition 117" in the Initiation paragraph about l8_tribe/l8_tribe_state. Definition 117 confirmed in l8_shaman_trade.gd and l8_larkhon.gd. Let me check l8_tribe.gd and l8_tribe_state.gd for 117.
  - Also `larkhon_join_tribe` — the note ids grep didn't show `larkhon_join_tribe` anywhere! The state file has must_sleep, ask_shaman, serum_needs_leaf, vapors_unactivated — but no larkhon_join_tribe. l8_larkhon.gd returns "larkhon_must_sleep" as default at line 24, and there's no join_tribe note. So `larkhon_join_tribe` is MISSING. Let me double-check with a full-repo grep for "larkhon_join_tribe" and "join_tribe".
  - The K03 journal table says first row `larkhon_join_tribe` for not-a-tribe-member; l8_larkhon.gd:24 returns "larkhon_must_sleep" — but the state table line 13 has must_sleep with flag "" as first entry. Hmm — so maybe the actual first row behavior is "must_sleep" not "join_tribe". The doc's table lists 5 ids; only 4 exist. Flag larkhon_join_tribe as missing.
  - Also verify `act2:L8_SJ:shaman_amaranth` — confirmed at l8_shaman_trade.gd:7.
  - definition 119 — confirmed in l8_shaman_trade (via catalog? line 20 uses definition(s.leaf)!=117; 119 not literally in shaman_trade). K03 says reward id act2:L8_SJ:shaman_amaranth, definition 119. Definition 119 appears in l8_larkhon.gd:22,45. Check the catalog for shaman_amaranth definition 119. Let me grep act2_items_catalog.gd for 119.
  - `l10_silverleaf.gd validate` ✓ line 11.
  - props 159–170 ✓ line 4.
  - DEVIATIONS 0307 named ✓.
  - `l8_guidance_test.gd` ✓ exists.
  - 60-second clock — not a name to verify per se.
  - "native L12 selector 1" and "native L8 selector 5" / "native shore selector 5" — selectors; could check but they're runtime-level. The docs name "selector 5" for l9_flood_escape (L8 selector 5). I could grep for it in l9_flood_escape_earned_test.gd and l8_shore/l8_larkhon tests. Let me quickly grep "selector" in those tests.

  Also K02: "movie 54" confirmed. Region 3185 ✓, prop 2622 ✓. Table 122, raft 82 ✓. body 2406, pyre 301, orbs 1205/1206 ✓.

  Also K02 mentions `l10_main_gate.gd` (K01) ✓ exists.

  TRIAGE_20261104.md — glob in lol2_r15 found nothing. Check AI_COMMS? The task says "check it exists in ~/opus_work/lol2_r15". So flag as not present there (it lives in AI_COMMS presumably). Quick check in AI_COMMS to note where it is.

  Additional greps:
  1. "larkhon_join_tribe" whole repo
  2. "act2:L8_SJ:larkhon_vapors" whole repo
  3. 117 in l8_tribe.gd / l8_tribe_state.gd
  4. 119 + shaman_amaranth in act2_items_catalog.gd
  5. TRIAGE_20261104 in AI_COMMS
  6. selector checks: "selector" in l9_flood_escape_earned_test.gd, l8_shore_earned_test.gd, l8_larkhon_earned_test.gd
  7. spark levels in l10_oil.gd ignite — read lines 105-125 to verify "accepts levels 1, 3, 5" claim? The task asks to verify names exist, not claims. But "level one and two are too short" is a doc claim; the names to verify: `ignite`, `BLAST_RADIUS`. Both confirmed. I'll read briefly for evidence anyway — maybe skip; grep evidence lines suffice. Actually a quick read of l10_oil.gd lines 108-120 to confirm ignite exists and uses levels.All verified. Findings:

  Missing/mismatched:
  1. K02 `l9_chapel.gd` — no such script in lol2_r15 (only the test `l9_chapel_earned_test.gd` and `l9_pyre.gd` exist).
  2. K02 `l9_bracers.gd` — no such script; the bracers host is `scripts/lol2/l9_dead_bracers.gd` (and `dead_bracers_item.gd`). Name mismatch.
  3. K03 `larkhon_join_tribe` — not found anywhere in lol2_r15; the l8_larkhon notes table only defines 4 ids, and the "not a tribe member" case falls through to `larkhon_must_sleep` (l8_larkhon.gd:24) — actually let me check: l8_larkhon.gd lines 21-24: mixed→vapors_unactivated; def119 carried→serum_needs_leaf; tribe member and not trade→ask_shaman; default→must_sleep. So a non-member with no serum gets "must_sleep", not "join_tribe". So the doc's first journal row names an id that doesn't exist, and the actual behavior differs (must_sleep shown to non-members). Mismatch.
  4. TRIAGE_20261104.md — not in lol2_r15; it's in ~/AI_COMMS/playtest_feedback_20261023/TRIAGE_20261104.md. The doc says "Newest owner file" — it's an AI_COMMS file, so arguably out of scope, but I should flag per the task (check existence in lol2_r15 → not there).

  Interesting note: larkhon_vapors definition — K03 says "writes act2:L8_SJ:larkhon_vapors" and catalog says definition 128 for vapors (not named in doc, fine). K03 says "Mix needs definitions 117 and 119" ✓ (catalog 117, 119; l8_larkhon.gd:45).

  Also K03: "Dawn is actor 20" ✓ l8_dawn.gd:2,16. "Daniel in the bout is actor 23" ✓ l8_tribe.gd. "definition 117" for leaf — in l8_tribe_state.gd:26,39 (doc said host l8_tribe.gd / l8_tribe_state.gd — 117 appears in state file, fine).

  K02: prop 158, def 78 ✓. body 2406, pyre 301, orbs 1205/1206 ✓. region 3185, prop 2622 ✓. table 122, raft 82 ✓. movie 54 ✓ (test lines 42-43). `ignite` levels [1,3,5], phase 2 ✓ l10_oil.gd:110-111. BLAST_RADIUS ✓ :6. `discover` absent in l9/l10 ✓ (confirms doc claim); discover defined in my_journal.gd:46 ✓.

  K03: `l8_journey.admitted` ✓. selectors: shore selector 5 ✓, flood escape L8 selector 5 ✓, L12 selector 1 ✓.

  STORY-008/STORY-009 — doc mentions STORY-008/STORY-009 tags in tests; not necessary to check but could. Skip — the named ids check was the requirement; STORY ids are arguably "ids". Quick check might be good but I've already done a lot. Let me do one quick grep for STORY-008 and STORY-009 to be thorough.

One last check on the STORY tags the docs cite.

All checks complete. Now produce the Markdown report: one table per source doc (name | kind | exists yes/no | path:line evidence), then a short list of missing/mismatched items.

  K02 table entries (order as they appear):
  1. TRIAGE_20261104.md — doc file — no (not in lol2_r15; found at ~/AI_COMMS/playtest_feedback_20261023/TRIAGE_20261104.md)
  2. discover() in l9_*/l10_* — claim of absence — yes (claim holds; no matches)
  3. l10_main_gate.gd — script — yes — scripts/lol2/l10_main_gate.gd
  4. l10_catacomb_earned_test.gd — test — yes
  5. l10_gold_earned_test.gd — test — yes (STORY-009 at :33)
  6. STORY-008 — id — yes (tests/l10_catacomb_earned_test.gd:29, scripts/lol2/l10_braziers.gd:2)
  7. STORY-009 — id — yes (l10_gold_earned_test.gd:33, l10_fence_earned_test.gd:45)
  8. l10_barrel.gd — script — yes
  9. l10_oil.gd — script — yes
  10. ignite — function — yes — l10_oil.gd:110 (accepts levels [1,3,5], phase 2 — line 111)
  11. BLAST_RADIUS — constant — yes — l10_oil.gd:6
  12. l10_two_empty_earned_test.gd — yes
  13. l10_barrel_earned_test.gd — yes
  14. l10_oil_earned_test.gd — yes
  15. l10_blue_earned_test.gd — yes
  16. l10_fence_earned_test.gd — yes
  17. l10_priest.gd — yes
  18. prop 158 — id — yes — l10_priest.gd:3
  19. act2:L10_DC:priest_urn — item id — yes — l10_priest.gd:6
  20. act2:L9_DR:item55 — item id — yes — dead_bracers_item.gd:3, act2_world_items.gd:55
  21. def 78 — id — yes — l10_priest.gd:3, act2_items_catalog.gd:50
  22. l10_priest_earned_test.gd — yes
  23. l9_chapel.gd — script — NO (only l9_chapel_earned_test.gd; chapel logic likely in l9_pyre.gd)
  24. l9_pyre.gd — yes
  25. body 2406 / pyre 301 / orbs 1205,1206 — ids — yes — l9_pyre.gd:2,8,37
  26. l10_ruins_departure_earned_test.gd — yes
  27. l9_opening_earned_test.gd — yes
  28. l9_chapel_earned_test.gd — yes
  29. l9_ashes_earned_test.gd — yes
  30. l10_ashes_return_earned_test.gd — yes
  31. l9_tower.gd — yes
  32. l9_bracers.gd — NO (actual host: l9_dead_bracers.gd)
  33. l9_mirrors.gd — yes
  34. l9_tower_approach_earned_test.gd — yes
  35. l9_two_white_earned_test.gd — yes
  36. l9_bracers_earned_test.gd — yes
  37. l9_mirror_return_earned_test.gd — yes
  38. l9_tower_blank_earned_test.gd — yes
  39. l10_ankh_state.gd — yes
  40. l10_emperor.gd — yes
  41. l10_ankh_earned_test.gd — yes
  42. l10_emperor_supply_earned_test.gd — yes
  43. l10_emperor_earned_test.gd — yes
  44. l9_statue.gd — yes; region 3185, prop 2622 — l9_statue.gd:2
  45. l9_statue_walk.gd — yes
  46. l9_flood.gd — yes
  47. l9_escape.gd — yes; table 122, raft 82 — l9_escape.gd:18 etc.
  48. l9_statue_earned_test.gd — yes
  49. l9_statue_follow_earned_test.gd — yes; movie 54 at :42-43
  50. l9_flood_earned_test.gd — yes
  51. l9_flood_escape_earned_test.gd — yes; L8 selector 5 at :53

  K03 table:
  1. TRIAGE_20261104.md — no (same)
  2. l8_shore.gd — yes
  3. l8_dawn.gd — yes; actor 20 — l8_dawn.gd:2,16
  4. l10_silverleaf.gd — yes; validate at :11; props 159–170 at :4
  5. l8_shore_earned_test.gd — yes; selector 5 at :22
  6. l8_dawn_earned_test.gd — yes
  7. l8_baccata.gd — yes
  8. l10_silverleaf_harvest.gd — yes
  9. l8_baccata_earned_test.gd — yes
  10. l10_silverleaf_growth_earned_test.gd — yes
  11. l10_silverleaf_harvest_earned_test.gd — yes
  12. l8_tribe.gd — yes; actor 23 at :44,:51,:63
  13. l8_tribe_state.gd — yes; def 117 at :26,:39
  14. l8_journey.admitted — field — yes — l8_journey.gd:56, l8_journey_state.gd:9
  15. definition 117 — yes — catalog :37, l8_tribe_state.gd:39
  16. l8_initiation_earned_test.gd — yes
  17. l8_initiation_yield_earned_test.gd — yes
  18. l8_shaman_trade.gd — yes
  19. act2:L8_SJ:shaman_amaranth — yes — l8_shaman_trade.gd:7
  20. definition 119 — yes — catalog :48, l8_larkhon.gd:22
  21. l8_shaman_trade_earned_test.gd — yes
  22. l8_tree_slot_state.gd — yes; def 105 at :11,:33
  23. l8_larkhon.gd — yes
  24. act2:L8_SJ:larkhon_vapors — yes — l8_larkhon_state.gd:5, catalog :47
  25. actor 115 — yes — l8_larkhon.gd:31
  26. regions 3277/3278 — yes — l8_larkhon.gd:83
  27. DEVIATIONS 0307 — yes — l8_larkhon.gd:14
  28. l8_larkhon_earned_test.gd — yes; L12 selector 1 at :90
  29. l8_larkhon_expiry_earned_test.gd — yes
  30. larkhon_join_tribe — NO
  31. larkhon_ask_shaman — yes — l8_larkhon.gd:23, state:14
  32. larkhon_serum_needs_leaf — yes — l8_larkhon.gd:22
  33. larkhon_vapors_unactivated — yes — l8_larkhon.gd:21
  34. larkhon_must_sleep — yes — l8_larkhon.gd:24
  35. l8_guidance_test.gd — yes
  36. my_journal.gd — yes; discover at :46

  Missing/mismatched list:
  - l9_chapel.gd (K02 host) — no script file; chapel logic appears to live in l9_pyre.gd; only the test exists.
  - l9_bracers.gd (K02 host) — actual host is scripts/lol2/l9_dead_bracers.gd (plus dead_bracers_item.gd). Name mismatch.
  - larkhon_join_tribe (K03 journal table) — no match anywhere; l8_larkhon.gd has no tribe-membership branch — a non-member falls through to larkhon_must_sleep (line 24). So the first journal row's id doesn't exist and behavior differs from the table.
  - TRIAGE_20261104.md — not in lol2_r15 (owner file lives in ~/AI_COMMS/playtest_feedback_20261023/); both docs reference it as an AI_COMMS owner file, so this is arguably expected — note it.

  Write the final report.

Verification complete. All greps were run against `~/opus_work/lol2_r15`; paths below are relative to it.

  ## K02 — `K02_act2_cemetery_ruins.md`

  | name | kind | exists | evidence |
  | --- | --- | --- | --- |
  | `TRIAGE_20261104.md` | doc file | **no** (not in repo) | only at `~/AI_COMMS/playtest_feedback_20261023/TRIAGE_20261104.md` |
  | "No `discover()` in `l9_*.gd`/`l10_*.gd`" | negative claim | yes (claim holds) | grep for `discover` in `scripts/lol2/l9_*.gd` and `l10_*.gd`: no matches |
  | `l10_main_gate.gd` | script | yes | `scripts/lol2/l10_main_gate.gd` |
  | `l10_catacomb_earned_test.gd` | test | yes | `tests/l10_catacomb_earned_test.gd` (STORY-008 print at :29) |
  | `l10_gold_earned_test.gd` | test | yes | `tests/l10_gold_earned_test.gd` (STORY-009 print at :33) |
  | STORY-008 / STORY-009 | id tags | yes | `scripts/lol2/l10_braziers.gd:2`; `tests/l10_fence_earned_test.gd:45` |
  | `l10_barrel.gd` | script | yes | `scripts/lol2/l10_barrel.gd` |
  | `l10_oil.gd` | script | yes | `scripts/lol2/l10_oil.gd` |
  | `ignite` | function | yes | `scripts/lol2/l10_oil.gd:110`; levels `[1,3,5]` + barrel phase 2 gate at :111 — matches the doc |
  | `BLAST_RADIUS` | constant | yes | `scripts/lol2/l10_oil.gd:6` |
  | `l10_two_empty_earned_test.gd` | test | yes | `tests/l10_two_empty_earned_test.gd` |
  | `l10_barrel_earned_test.gd` | test | yes | `tests/l10_barrel_earned_test.gd` |
  | `l10_oil_earned_test.gd` | test | yes | `tests/l10_oil_earned_test.gd` |
  | `l10_blue_earned_test.gd` | test | yes | `tests/l10_blue_earned_test.gd` |
  | `l10_fence_earned_test.gd` | test | yes | `tests/l10_fence_earned_test.gd` |
  | `l10_priest.gd` | script | yes | `scripts/lol2/l10_priest.gd` |
  | prop 158 | id | yes | `scripts/lol2/l10_priest.gd:3` |
  | `act2:L10_DC:priest_urn` | item id | yes | `scripts/lol2/l10_priest.gd:6`; `scripts/lol2/act2_items_catalog.gd:50` |
  | `act2:L9_DR:item55` (bracers) | item id | yes | `scripts/lol2/dead_bracers_item.gd:3`; `scripts/lol2/act2_world_items.gd:55` |
  | def 78 (urn gift) | id | yes | `scripts/lol2/l10_priest.gd:3`; catalog `"definition":78` |
  | `l10_priest_earned_test.gd` | test | yes | `tests/l10_priest_earned_test.gd` |
  | `l9_chapel.gd` | script | **no** | no `l9_chapel.gd` anywhere; only `tests/l9_chapel_earned_test.gd` exists (chapel logic appears folded into `l9_pyre.gd`) |
  | `l9_pyre.gd` | script | yes | `scripts/lol2/l9_pyre.gd` |
  | body 2406 / pyre 301 / orbs 1205, 1206 | ids | yes | `scripts/lol2/l9_pyre.gd:2`, `:8`, `:37` |
  | `l10_ruins_departure_earned_test.gd` | test | yes | `tests/l10_ruins_departure_earned_test.gd` |
  | `l9_opening_earned_test.gd` | test | yes | `tests/l9_opening_earned_test.gd` |
  | `l9_chapel_earned_test.gd` | test | yes | `tests/l9_chapel_earned_test.gd` |
  | `l9_ashes_earned_test.gd` | test | yes | `tests/l9_ashes_earned_test.gd` |
  | `l10_ashes_return_earned_test.gd` | test | yes | `tests/l10_ashes_return_earned_test.gd` |
  | `l9_tower.gd` | script | yes | `scripts/lol2/l9_tower.gd` |
  | `l9_bracers.gd` | script | **no** | actual host is `scripts/lol2/l9_dead_bracers.gd` (plus `dead_bracers_item.gd`) — name mismatch |
  | `l9_mirrors.gd` | script | yes | `scripts/lol2/l9_mirrors.gd` |
  | `l9_tower_approach_earned_test.gd` | test | yes | `tests/l9_tower_approach_earned_test.gd` |
  | `l9_two_white_earned_test.gd` | test | yes | `tests/l9_two_white_earned_test.gd` |
  | `l9_bracers_earned_test.gd` | test | yes | `tests/l9_bracers_earned_test.gd` |
  | `l9_mirror_return_earned_test.gd` | test | yes | `tests/l9_mirror_return_earned_test.gd` |
  | `l9_tower_blank_earned_test.gd` | test | yes | `tests/l9_tower_blank_earned_test.gd` |
  | `l10_ankh_state.gd` | script | yes | `scripts/lol2/l10_ankh_state.gd` |
  | `l10_emperor.gd` | script | yes | `scripts/lol2/l10_emperor.gd` |
  | `l10_ankh_earned_test.gd` | test | yes | `tests/l10_ankh_earned_test.gd` |
  | `l10_emperor_supply_earned_test.gd` | test | yes | `tests/l10_emperor_supply_earned_test.gd` |
  | `l10_emperor_earned_test.gd` | test | yes | `tests/l10_emperor_earned_test.gd` |
  | `l9_statue.gd` (region 3185, prop 2622) | script + ids | yes | `scripts/lol2/l9_statue.gd:2` |
  | `l9_statue_walk.gd` | script | yes | `scripts/lol2/l9_statue_walk.gd` |
  | `l9_flood.gd` | script | yes | `scripts/lol2/l9_flood.gd` |
  | `l9_escape.gd` (table 122, raft 82) | script + ids | yes | `scripts/lol2/l9_escape.gd:18`, `:46–69` |
  | `l9_statue_earned_test.gd` | test | yes | `tests/l9_statue_earned_test.gd` |
  | `l9_statue_follow_earned_test.gd` (movie 54) | test + id | yes | `tests/l9_statue_follow_earned_test.gd:42–43` ("MOVIE54") |
  | `l9_flood_earned_test.gd` | test | yes | `tests/l9_flood_earned_test.gd` |
  | `l9_flood_escape_earned_test.gd` (native L8 selector 5) | test + id | yes | `tests/l9_flood_escape_earned_test.gd:53` (`level==8 and selector==5`) |
  | `discover` (proposed journal fix) | function | yes | `scripts/lol2/my_journal.gd:46` (`static func discover`) |

  ## K03 — `K03_act2_serum_larkhon.md`

  | name | kind | exists | evidence |
  | --- | --- | --- | --- |
  | `TRIAGE_20261104.md` | doc file | **no** (not in repo) | only in `~/AI_COMMS/playtest_feedback_20261023/` |
  | `l8_shore.gd` | script | yes | `scripts/lol2/l8_shore.gd` |
  | `l8_dawn.gd` (Dawn = actor 20) | script + id | yes | `scripts/lol2/l8_dawn.gd:2`, `:16` (`actors["20"]`) |
  | `l10_silverleaf.gd` + `validate` | script + function | yes | `scripts/lol2/l10_silverleaf.gd:11` (`static func validate`); props 159–170 at `:4` |
  | `l8_shore_earned_test.gd` (shore selector 5) | test + id | yes | `tests/l8_shore_earned_test.gd:22` |
  | `l8_dawn_earned_test.gd` | test | yes | `tests/l8_dawn_earned_test.gd` |
  | `l8_baccata.gd` | script | yes | `scripts/lol2/l8_baccata.gd` |
  | `l10_silverleaf_harvest.gd` | script | yes | `scripts/lol2/l10_silverleaf_harvest.gd` |
  | `l8_baccata_earned_test.gd` | test | yes | `tests/l8_baccata_earned_test.gd` |
  | `l10_silverleaf_growth_earned_test.gd` | test | yes | `tests/l10_silverleaf_growth_earned_test.gd` |
  | `l10_silverleaf_harvest_earned_test.gd` | test | yes | `tests/l10_silverleaf_harvest_earned_test.gd` |
  | `l8_tribe.gd` / `l8_tribe_state.gd` | scripts | yes | `scripts/lol2/l8_tribe.gd`, `scripts/lol2/l8_tribe_state.gd` |
  | leaf = definition 117 | id | yes | `scripts/lol2/l8_tribe_state.gd:26`,`:39`; catalog `act2_items_catalog.gd:37` |
  | `l8_journey.admitted` | state field | yes | `scripts/lol2/l8_journey.gd:56`; `l8_journey_state.gd:9` |
  | Daniel = actor 23 | id | yes | `scripts/lol2/l8_tribe.gd:44`,`:51`,`:63` |
  | `l8_initiation_earned_test.gd` | test | yes | `tests/l8_initiation_earned_test.gd` |
  | `l8_initiation_yield_earned_test.gd` | test | yes | `tests/l8_initiation_yield_earned_test.gd` |
  | `l8_shaman_trade.gd` | script | yes | `scripts/lol2/l8_shaman_trade.gd` |
  | `act2:L8_SJ:shaman_amaranth`, def 119 | item id | yes | `scripts/lol2/l8_shaman_trade.gd:7`; catalog `act2_items_catalog.gd:48` |
  | `l8_shaman_trade_earned_test.gd` | test | yes | `tests/l8_shaman_trade_earned_test.gd` |
  | `l8_tree_slot_state.gd`, def 105 | script + id | yes | `scripts/lol2/l8_tree_slot_state.gd:11`,`:33` |
  | `l8_larkhon.gd` | script | yes | `scripts/lol2/l8_larkhon.gd` |
  | `act2:L8_SJ:larkhon_vapors` | item id | yes | `scripts/lol2/l8_larkhon_state.gd:5`; catalog `act2_items_catalog.gd:47` |
  | defs 117 + 119 for the mix | ids | yes | `scripts/lol2/l8_larkhon.gd:45` |
  | actor 115 (upper chest) | id | yes | `scripts/lol2/l8_larkhon.gd:31`,`:61` |
  | regions 3277 / 3278 | ids | yes | `scripts/lol2/l8_larkhon.gd:83` |
  | DEVIATIONS 0307 | doc ref | yes | `scripts/lol2/l8_larkhon.gd:14`,`:84` |
  | `l8_larkhon_earned_test.gd` (native L12 selector 1) | test + id | yes | `tests/l8_larkhon_earned_test.gd:90` (`level==12 and selector==1`) |
  | `l8_larkhon_expiry_earned_test.gd` | test | yes | `tests/l8_larkhon_expiry_earned_test.gd` |
  | `larkhon_join_tribe` | journal note id | **no** | no match anywhere in the repo (see below) |
  | `larkhon_ask_shaman` | journal note id | yes | `scripts/lol2/l8_larkhon.gd:23`; `l8_larkhon_state.gd:14` |
  | `larkhon_serum_needs_leaf` | journal note id | yes | `scripts/lol2/l8_larkhon.gd:22`; `l8_larkhon_state.gd:15` |
  | `larkhon_vapors_unactivated` | journal note id | yes | `scripts/lol2/l8_larkhon.gd:21`; `l8_larkhon_state.gd:16` |
  | `larkhon_must_sleep` | journal note id | yes | `scripts/lol2/l8_larkhon.gd:24`; `l8_larkhon_state.gd:13` |
  | `l8_guidance_test.gd` | test | yes | `tests/l8_guidance_test.gd` |
  | `my_journal.gd` | script | yes | `scripts/lol2/my_journal.gd` |

  ## Missing / mismatched items

  1. **`l9_chapel.gd` (K02)** — no such script in the repo. Only `tests/l9_chapel_earned_test.gd` exists; the chapel logic appears to be hosted in `scripts/lol2/l9_pyre.gd`. The doc's "Host: `l9_chapel.gd`" names a file that was never created.
  2. **`l9_bracers.gd` (K02)** — no such script. The bracers host is `scripts/lol2/l9_dead_bracers.gd` (with item identity in `scripts/lol2/dead_bracers_item.gd`). The test `l9_bracers_earned_test.gd` does exist, so this is a naming mismatch in the doc, not missing coverage.
  3. **`larkhon_join_tribe` (K03)** — no match anywhere in the repo. `l8_larkhon.gd:21–24` only returns the other four note ids; there is no tribe-membership branch, so a non-member player near actor 115 falls through to `larkhon_must_sleep`. The doc's first journal-row id does not exist and the described behavior differs from the code.
  4. **`TRIAGE_20261104.md` (both docs)** — not present in `lol2_r15`; it lives in `~/AI_COMMS/playtest_feedback_20261023/TRIAGE_20261104.md`. Likely intentional (it's the AI_COMMS "owner file"), flagged only because the check scope was the repo.

  Everything else — all other script/test filenames, the `ignite`/`BLAST_RADIUS`/`validate`/`discover` functions and constants, and every numeric id (props 158/159–170/2406/301/1205/1206/2622/122/82, region 3185, regions 3277/3278, actors 20/23/115, definitions 78/105/117/119, movie 54, selectors) — verified present with the evidence above. The K02 claim that no `discover()` call exists in `l9_*.gd`/`l10_*.gd` is also confirmed true.

