• Audit complete. I verified the plan's anchors and claims against `~/opus_work/lol2_r18` at d5da60a, and ran my own searches for `strike`, `melee_damage`, `set_health`, `.health=` writes, `receive_damage`, `set_meta`, and file writers. Most of the plan holds: all 19 strike sites exist as described (I re-derived the `melee_damage(` call list — it matches exactly), the 41-uncalled-restores finding checks out precisely (62 owners with `restore()` − 21 called = 41, and each named owner verified), the owner-convention counts (110 attach / 106 `(map)` / 36 distinct owns / 112 node-name lookups outside the three hosts) reproduce exactly, the class hierarchy claims hold, the debug-kill attachment points are exactly the two cited, the interim scale and native-bank anchors are right, and L9↔L8 travel exists for the F-07 acceptance test. What follows is only what does not hold.

  ## Plan 1 — player combat / health owner

  **1. The "Writers that bypass the switch" table (marked PROVEN) misses three writers.**
  - `scripts/lol2/hive_warriors.gd:156` — the guardians' own windup attack writes `health = maxi(0,health-player_defense.incoming(review,15))` directly. This is the *primary* Hive damage path to Luther, and it is absent from the plan.
  - `scripts/lol2/hive_executioner_live.gd:115` — the executioner's live attack writes `guards.health` (Warriors) directly.
  - `scripts/lol2/monastery_rooms.gd:335` — the Morgan orb heal writes `get_parent().health` (store C, jungle family) directly.
  Fix: add all three to the table, to commit 8's file list, and to commit 9's source-scan expectations. Behaviorally the forwarding-property design tolerates them, but a review checklist built from this table would miss them.

  **2. The through-switch census is wrong.** Plan says "23 `set_health` calls in 20 files" and enumerates 22 anchors. The real 23rd call is `scripts/lol2/dark_halls_crates.gd:365` — `magic.call("set_health", …)`, invisible to a `set_health(` grep — making it 21 files. Fix the count and add the crate caller.

  **3. "Two of them saved" (1.2 item 5) is wrong — three cooldown clocks are saved.** Besides the dino (`jungle_dino_population_state.gd:32-33,54`) and the roach snapshot (`cave_roach.gd:174`), the Hive `cooldown` is saved inside `hive_encounter` (`hive_warriors.gd:161` checkpoint → `hive_review.gd:248`, validated at `act_one_quest_state.gd:45`). This contradicts the plan's own save table, which lists `hive_encounter`. Fix C3/Q1 wording and include the Hive clock in the commit-0 fixture comparison.

  **4. Save-table row mislabeled.** "`health` in the Cave save — `cave_walkthrough.gd:809`": line 809 is the "health" key of `_completion_state()`, the Cave→Museum *transfer packet* (set into `lol2_cave_completion` at :788), not the Cave save. The Cave quicksave (`_save_state`, :1177-1233) carries health only inside the roach snapshot, which is the row above. Fix the label to "Cave→Museum transfer packet".

  **5. Melee-reward row incomplete.** The "after a blow lands" table lists rewards at "sites 4, 6" only; melee rewards also fire at site 1 (`scripted_creature_population.gd:347`, `cave_melee_reward`) and site 3 (`cave_roach_population.gd:252`). No design impact (rewards live inside `receive_damage`, not the `after_landed` tail), but the table should say sites 1, 3, 4, 6.

  Trivial anchor slips: `dev_diagnostics.gd` reader spans :126-128, not :126-127 (store-C read is :128); the `damage_to_player_scale` override is `act2_creatures.gd:141-142`, not :140-141.

  ## Plan 2 — area host registry

  **6. Attach-list counts wrong (marked PROVEN).** "`act2_map.gd:207-316`, 95 calls under nine `if area_id==` blocks": the range contains 93 attach lines (88 owner preloads) under **8** blocks (:212, :225, :247, :251, :267, :294, :303, :310). The claim "two blocks exist for L16 (:251 and the tail near :262)" is false: :251-266 is one block; :262 is `l16_journal_hints` inside it. The golden-order test makes this harmless in practice, but the stated facts are wrong — fix the counts and drop the second-L16-block claim.

  **7. Source-index anchor off by one.** The mesh-side literal L10 source-index list is at `act2_map.gd:130`, not ":128-129" (2.1 and commit 4).

  **8. KEY count.** "85 files have a KEY const" — `grep -l "const KEY" l<N>_*.gd` gives 90 (86 use it against `quest_state`). Nothing rides on it; correct or drop the number.

  ## Plan 3 — one whole-game save

  **9. The version/migration claim is false for the Cave.** "Each in its own format with `version == 1` hard-coded" and "No migration code exists" (3.0/3.1, PROVEN): the Cave save is version **2** (`walkthrough_save.gd:6`), its validator accepts v1 (:91), and a v1→v2 migration exists (:241-242). Consequently 3.4's "inside a slot, `area_save` is today's shape with today's `version: 1`" is wrong for the Cave. The opaque-wrap design is unaffected, but these sentences must be corrected — and they establish that per-area inner versions already differ, which C8 should acknowledge.

  **10. The meta inventory is incomplete.** 3.7 claims "I listed every `set_meta("lol2_…")`", but two cross-scene transfer metas are set via constants and were missed: `lol2_hive_route_handoff` (`hive_route.gd:3`, set :78, consumed :20-32) and `lol2_dark_halls_route_handoff` (`dark_halls_route.gd:6`, set :92). Both carry a full `area_handoff` (inventory + quests) between scenes — exactly the category the table documents. They are transient (consumed on arrival), so they can stay as metas like rows 2/4, but the table and C5 should name them explicitly, and Sol's commit-3 trace should include them. (Also `lol2_museum_checkpoint`, `museum_walkthrough.gd:7`/`:450`, a same-scene session cache.)

  **11. The Cave is missing from the load-side migration.** Commit 5 names only `act2_map.gd` and `dragon_level.gd` as gaining the resume read, but the Cave has no resume path at all *and* no `apply_save(state)` — its load is `_quickload_unrecorded` (`cave_walkthrough.gd:1273+`), which applies inline from a file path. A slot saved in the Cave cannot be restored through the commit-5 pattern ("read meta in `_ready`, call `apply_save`") without new Cave code. C3 lists the Cave as "to be checked" but commit 5 never resolves it. Fix: name `cave_walkthrough.gd` explicitly in commits 3 and 5 and specify the dict-apply adapter for it (note Museum's `apply_save` returns `void`, not `String` — `museum_walkthrough.gd:923` — so the C3 signature column needs adjusting too).

  Minor, non-blocking: 2.5's "797 of 1,077 tests" matches neither the 1,149 `*_test.gd` files nor the 1,112 registry rows at d5da60a (likely a stale quote from the master plan).

  Everything else I checked — strike-site table (all 19, including reach/mask/bonus/empty-hand/cooldown columns), the 21 click-only owners, the three health stores and the switch (`player_starting_magic.gd:82-89`), the max-30 literal list, test-count claims (48/50/23/15/13/5 all reproduce), Plan 2's host tables and the 41-owner list, Plan 3's 15 save files and formats, the native bank anchors and the "never written to disk" claim (only the four save modules write save files; the bank travels only via tree meta) — holds as written.

  PLAN NEEDS CHANGES
