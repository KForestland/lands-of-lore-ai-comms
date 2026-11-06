# Kimi K23 — SEEN+HOSTED map rows vs longplay frames + act3 hosts (read-only, 2026-11-06)

Lead: only 5 SEEN+HOSTED rows exist; frames match in all checked rows. The two 'host missing' rows (L17 Hive Mother, L20 chambers) are hosted by grok's UNAPPLIED Act 3 stack (AH02: X01 dawn curse etc.), not by act3-story yet - they become real when the lead applies AH02 (next after AH01). Track: re-check L17/L20 after AH02 lands.

All checks are done. Here is the spot-check report.

  # K23 spot-check: SEEN+HOSTED rows

  **Coverage note:** Only **5** rows classed SEEN+HOSTED exist across `AE14_map_gaps.md` and `AG01–AG04` (verified by grep). I checked all 5; a 10-row sample is not possible.

  | row | frame | what the frame shows | host found | ok |
  |---|---|---|---|---|
  | L13 Ru-Loi count (AE14:37, AG02:7) | `g_00187` | Dark pillared corridor; HUD top-right reads "Remaining Rulo…" (text clipped at window edge) above "19/19" — matches the claim | Yes — `scripts/lol2/l13_prison.gd:42` has `all_ruloi_dead()`; `act2_populations/L13_RC.json` has 21 actor rows, 20 of definition 1 named RULOI; `tests/l13_lower_ruloi_earned_test.gd` + registry JSON exist | yes (see note 3) |
  | L17 Hive Mother (AE14:49, AG01:7) | `g_00382` | Horned, muscular pale-haired figure standing beside a red tendril mass in a dark organic cavern, no HUD — matches | **No** — no "X01", "Frank", "placenta", prop 242, "Wide guts", or "Hive Duct" anywhere in `scripts/lol2` or `assets/lol2/generated` (text); cited test `l19_dawn_curse_test` (order 812) does not exist in `tests/` or `tests/registry/` | **no — host and test missing** |
  | L20 empowerment chambers (AE14:56, AG01:10) | `g_00371`, `g_00378`, `g_00384` | `g_00371`: dark pillar hall with glowing green bands on pillars, green/black checkered floor. `g_00378`: furnished green marble room with a woman (Dawn) standing center. `g_00384`: green marble hall, red figure on a raised platform. All match; no chamber number printed, as stated | **No** — `act2_populations/L20_BB.json` has 0 regions, 0 controls, no "chamber"/"empower(ment)" strings; no `l20_*.gd` scripts exist; "Scotia's homes" resolves only to a SCOTIA actor definition | **no — frame seen, host not found** |
  | L8 Crystal Shard, Dampen, sigil (AG03:10, from AF04) | none cited ("Not reopened") | No frame to verify — row was carried over from AF04 without a frame | Yes — `scripts/lol2/l8_tree_slot_state.gd:11` checks definition 105 ("Crystal Shard"); name "103-Cry shard" in `act2_items_source.json`; "70-Dampen ch" in `item_catalog.gd:49`; key `l8:shaman:Dracoid_sigil` in `item_catalog.gd:121` and `l8_journey_state.gd`; tests `l8_tree_room_earned_test.gd`, `l8_journey_state_test.gd` exist | yes (host only; SEEN part unverifiable) |
  | L9 raft (AG03:14, from AF04) | none cited ("Not reopened") | No frame to verify — carried over from AF04 | Yes — `scripts/lol2/l9_escape.gd` implements raft control 82 (header: "Modern physical lift adapter, original table122 and raft82 geometry"; `control:82` progression at line 68); `l9_flood_source.json` references control 82; `tests/l9_flood_escape_earned_test.gd` exists | yes (host is a modern adapter, see note 4) |

  ## Problems

  1. **Sample size shortfall:** only 5 SEEN+HOSTED rows exist (3 in AE14, 2 in AG files inherited from AF04), so "pick 10 rows" cannot be satisfied; I checked all of them instead.
  2. **L17 Hive Mother — host missing (flagged):** the frame (`g_00382`) genuinely shows the horned figure beside the red tendril mass, but nothing named X01, Frank's Placenta, or prop 242 exists in the repo, and the cited test `l19_dawn_curse_test` (order 812) is absent from `tests/` and `tests/registry/`. The SEEN+HOSTED class is not reproducible for this row.
  3. **L20 empowerment chambers — host missing (flagged):** the three frames do show three distinct green rooms as described, but no chamber/empowerment room records exist in `L20_BB.json` (no regions, no controls) and no `l20_*.gd` scripts exist. "Scotia's homes stay their own name" maps only to a SCOTIA actor definition, not to any room host.
  4. **L13 Ru-Loi minor discrepancy:** host and test are present and the frame matches, but `L13_RC.json` has `counted: []` and `counter_target: 0`, so the 19/19 counter shown in the frame is not data-backed in the population file (consistent with the row's own admission that the 20th name "was not derived").
  5. **No frame to re-verify for the two AF04-inherited rows:** the L8 and L9 raft rows are marked "Not reopened" in AG03, so only the host side could be checked. Hosts check out, though the L9 raft host (`l9_escape.gd`) is self-described as a modern lift adapter rather than an original record.

