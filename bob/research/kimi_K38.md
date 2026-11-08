# Kimi K38 — Fable MAPFIX x Grok BG07-BG21 review (2026-11-08)

Lead plan: after the r18a run: apply Grok BG07..BG21 per ORDER.md, then cherry-pick Fable's mapfix commits 350df5d + 9aa9499 from ~/opus_work/lol2_mapfix (the delivered .patch file is the wrong artifact), hand-merge jungle_review.gd, rebuild the ledger, rerun the Hive/Jungle look tests. Keep owner rows 16-53-49 (click) and 16-48-43 (stone animation) OPEN.

I have everything I need. One correction up front that shaped the whole review: the file `mapfix_9aa9499.patch` does **not** contain Fable's mapfix work — it contains the two *base* commits (`373b5d7` item_definitions, `c9295da` AV04 revert). The actual MAPFIX is two commits on the mapfix branch in `~/opus_work/lol2_mapfix`: `350df5d` (Hive fill + seed radius) and `9aa9499` (polygon-less clusters). I reviewed those.

  # K38 review — Fable MAPFIX + Grok BG14–BG20 vs TRIAGE_20261107

  ## Per-patch table

  | Patch | Owner report | Fixes it? | Test plays like a player? | Ledger / registry / typing |
  |---|---|---|---|---|
  | MAPFIX `350df5d` (Hive fill, seed_radius) | 17-27-27/35 roof gone; 17-30-51/17-32-57 grey planes; 17-28-43/29-06 pop-in | Yes, by neighbour-fill of 20 unbound faces + 600-unit view seeding; documented as adapter (native word16/17 unread). Open owner call: roof gets lava-ceiling 21 but longplay 40:40–43:40 shows dark rock — Fable flags this herself | Before/after captures at owner F10 poses (evidence folder); no earned test for the fill, `seed_radius` untested by a dedicated test | Pieces 0319/0320 + DEVIATIONS rows ✓; typed vars ✓ |
  | MAPFIX `9aa9499` (clusters) | 17-55-17 L10 "lacks this texture" | Yes — polygon-less floor subdivisions (28 L10 / 283 Hive / 110 L13) now always drawn; also explains the missing Hive step strips | `region_visibility_clusters_test` is headless data-only; captures at the owner pose are the visual proof | Piece 0321 ✓; registry order 846 ties `l8_opcode_followup_test` (legal, W16 equal-order rule) ✓ |
  | BG14 cat ladies | 16-40-18 "2 cat ladies" | Yes — native control 186 / E056E.VQA hosted, loiter + E-driven segments 0/2/4, saved state validated | Earned walk from (-900,-4350), aim, E, voice-playing check — good | Piece 0330 ✓; order 920 ✓; typed ✓. Media gitignored, prep tool required (see problems) |
  | BG15 bramble | 16-44-37/57 torn wall should block, burn/cut | Yes — controls 101–109 solid via `add_scripted_solids`, 3-cut walk, regrow timer, Spark permanent, save validation | Earned: walk blocked → 3 clicks → cross → regrow → blocked again → Spark → cross. Best test of the set | Piece 0331 ✓; order 921 ✓. Dead `expect_block` param (both branches identical) — cosmetic |
  | BG16 bridge opacity | 16-48-43 transparent lava/stone bridge | Partial — test-only guard that material 21 is opaque post-revert; "bad stone animation" half not addressed | Teleport pose + pixel probe (not earned); acceptable for a look-guard | No ledger row (ORDER.md acknowledges) ✓; order 924 ✓ |
  | BG17 cat height | 16-49-32 "3-metre cat" | Yes — quad scaled 44/128 (player height, the r12l Dawn precedent), prompt and aim point follow | Earned walk through the 7 source room points, then E; plus proportion/feet/prompt asserts — good | Piece 0332 ✓; order 922 ✓; pins authored 142.5×128 (intentional but brittle to media regeneration) |
  | BG18 weapon shelf | 16-52-10/23 missing bow/sword/bracer | Yes — 3 clickable pictures from longplay f_00580 wired to the existing purchase actions; icons z-ordered between background and patch (checked `monastery_room_view.gd` — correct) | Earned walk into the hut, door/enter sequence, clicks, double-buy refusal — good. Clicks are `gui_input.emit` at picture centre: rect placement vs the room art is *not* visually verified | Piece 0333 ✓; order 923 ✓; icons exist locally (gitignored generated assets, house pattern) |
  | BG19 falls sheet | 16-53-49 "no point and click" | **Questionable** — reinterprets the report as the AV04 grey sheet hiding the waterfall picture; guards the revert, verifies no `WaterSkirt` node and tiling. No click/hotspot is added or tested | Teleport pose + pixel probes; fine for what it tests | No ledger row ✓; order 925 ✓ |
  | BG20 gorge roof | 17-00-05 "need black roof" | Yes — native 744 ceilings lowered to the -10 opening instead of standing in the sky at 400; walls still clipped | Two teleport poses (in-gorge black ≥ 0.45, on-bank black ≤ 0.2); not an earned walk, acceptable for pure look | Piece 0334 ✓; order 926 ✓ |

  Cross-checks passed: BG14/BG15's `act_one_quest_state.gd` + `jungle_walkthrough.gd` hunks chain correctly (BG15's context includes BG14's lines — ORDER.md has them in the right sequence); BG15's `add_scripted_solids`/`solid_bodies`/`SCENERY_LAYER`/`set_mode` all exist in base `static_assemblies.gd`; BG14's prep tool imports (`decode`, `audio`, `parse_vqa_chunks`) resolve via `prepare_jungle_exit_movies.py`'s own imports; BG18's PNGs exist locally; BG07's `BRIDGE_DECKS` is what BG15-style scripted solids build on and precedes it per ORDER.

  ## Overlaps: Fable MAPFIX × BG07–BG20

  - **`scripts/lol2/jungle_review.gd` — real conflict.** MAPFIX `350df5d` inserts the `fill_untextured_surfaces` call between the `include_static_face` check and `var collision_kept := false`. **BG21**'s only jungle_review hunk (`@@ -133,15`) has exactly those two lines as adjacent context → fails in *both* apply orders (its context is split by Fable's insertion; and BG21's restructure removes a line Fable's hunk needs as trailing context). **BG20**'s hunks sit ≥3 lines below the insertion and only overlap in unchanged context → applies with a +3 offset, safe either order. BG21 also touches the same `_ready` clips block semantically (collision of clipped gorge walls, report 17-01-09) — same code region, different concern.
  - **`docs/DEVIATIONS.md` — every patch.** All Grok BG patches and both MAPFIX commits append at the tail; the Grok series chains its contexts patch-to-patch, so MAPFIX cannot be git-applied between/after them. Piece *numbers* collide too: Fable's 0319/0320/0321 are already taken by BG02/BG03/BG04 pieces (`e02`/`e03`/`e04`) — legal under W16 (equal numbers render in name order), but the numbers are misleading.
  - **Hive area (different files, same screen).** MAPFIX `hive_review.gd` (fill + seed_radius 600) changes what BG16's bridge camera and BG17's walk see at the same poses. Neither BG test was run against the MAPFIX hive — retest required after merge. No textual conflict (BG17 → `hive_conversation.gd`; BG16 → tests only).
  - **`scripts/lol2/region_visibility.gd`** — MAPFIX-only; no BG patch touches it. Clean.
  - **`scripts/lol2/jungle_walkthrough.gd`** — BG13→BG14→BG15 chain (handled by ORDER.md). MAPFIX branch does *not* touch it (the jungle_walkthrough hunk in the delivered patch file is the already-applied c9295da revert).
  - **No overlap**: BG08–BG12 (Museum), BG07 (`static_assemblies.gd` + tests), BG14/15's new files, `act_one_quest_state.gd`.

  ## Proposed safe apply order

  1. Finish the Grok series on r18-work exactly per ORDER.md: BG07 → BG13 (next), then BG14, BG15, BG17, BG18, BG16, BG19, BG20, BG21. It is internally chained (DEVIATIONS contexts, BG20→BG21 jungle_review, BG14→BG15 walkthrough/quest-state) and should apply clean onto `ca89b61`.
  2. `python3 tools/build_deviations.py --check` (expect the documented 414 pieces).
  3. Bring in MAPFIX by **3-way (cherry-pick/merge), not `git apply`**: pick `350df5d` then `9aa9499` from the mapfix branch. Expected conflicts: `jungle_review.gd` (small — keep BG21's restructured clips block, re-add Fable's 3-line fill call above `var collision_kept`) and `docs/DEVIATIONS.md` (take Grok's version; Fable's rows live in her pieces).
  4. `python3 tools/build_deviations.py build` to re-render the ledger (now 417 pieces), then `--check`.
  5. Re-run in the merged tree: `region_visibility_clusters_test`, `hive_bridge_opacity_earned_test`, `hive_conversation_height_earned_test`, `jungle_sunken_clip_test`, `jungle_gorge_roof_earned_test`, plus the BG07 bridge walk (Hive/Jungle look changed under them).

  ## Problems by severity

  **High**
  1. **Wrong artifact delivered.** `fable_lane/mapfix_20261108/mapfix_9aa9499.patch` contains base commits `373b5d7`+`c9295da` (item_definitions bump + AV04 revert) — zero mapfix content. Applied to r18-work it fails as already-applied and lands none of the fixes. The real work is branch commits `350df5d`+`9aa9499` in `~/opus_work/lol2_mapfix`; re-export with `git format-patch c9295da..9aa9499`.
  2. **jungle_review.gd: MAPFIX × BG21 is a hard conflict both directions** (see overlaps). It is a small manual merge, but it will not apply mechanically.

  **Medium**
  3. **BG19 probably doesn't fix the owner's report.** 16-53-49 was "no point and click"; the triage action was "identify the hotspot". BG19 verifies the waterfall *looks* right after the AV04 revert but adds/tests no click. Confirm the interpretation with the owner or keep the row open.
  4. **BG16 covers only half of 16-48-43** ("still bad stone animation" is unaddressed — opacity only). Track the animation half explicitly or the row will read as closed.
  5. **Ledger regeneration is mandatory after the merge**; ORDER.md's "414 pieces / `--check`" line goes stale the moment Fable's 3 pieces join (417), and her reused numbers 0319–0321 will confuse future numbering even though the tool permits ties.
  6. **Untested interplay in the Hive**: Fable's fill/seed_radius lands after Grok wrote BG16/BG17 against the un-filled hive; BG16's pixel band could plausibly change (more regions drawn, formerly grey faces now lava/rock). Step 5 above covers it, but it is a genuine unknown, not a formality.

  **Low**
  7. Fable's roof fill may draw the animated lava ceiling on roofs the longplay shows as dark rock — she flags it as an owner call; keep 17-27-27 open until the owner sees it.
  8. BG14 prep tool: hardcoded `/tmp/bg14-cat-cache` refuses reruns after a failed attempt; media is gitignored so the earned test hard-fails on machines without the material kit (house-consistent, but CI notes should say so — same for BG18's icons).
  9. BG15 test's `expect_block` parameter is dead (both return paths identical) — cosmetic.
  10. MAPFIX registry order 846 ties `l8_opcode_followup_test` — legal (W16), no action.
  11. BG16/BG19/BG20 tests are pose teleports rather than earned walks — acceptable for pure look guards, noted for the record; BG14/BG15/BG17/BG18 do walk like a player.

