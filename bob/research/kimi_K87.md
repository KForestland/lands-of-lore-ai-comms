• # Pre-merge review: sol/foundation-combat-health-20261111 (d5da60a..323aec5)

  I reviewed the full source diff (40 scripts, 2 new modules), the Plan 1 revision-2 contract, and my K85 audit items 1–5, checking each changed hunk against the parent code for behavior drift. **I found no behavior-changing defects.** Details below.

  ## Contract verification (all hold)

  - **K85-1 (three omitted writers)**: all three are routed through the owner — `hive_warriors.gd:168` (guardian windup), `hive_executioner_live.gd:116`, `monastery_rooms.gd:336` (Morgan orb, same `heal(h, 30)` calculation). Each is `maxi(0, h−x)` ≡ `PlayerHealth.lose` / same-value `write_host`.
  - **K85-2 (dynamic crate call)**: `dark_halls_crates.gd` untouched; facade `set_health` still exists as a one-line forwarder (`player_starting_magic.gd:84`), so `call("set_health", …)` resolves identically.
  - **K85-3 (third saved clock)**: Hive `cooldown` clock kept in `hive_warriors.gd:26`, still in `checkpoint()` (:173), validator bound `0.45` → `PlayerCombat.COOLDOWN` (same value, `act_one_quest_state.gd:47`). Cave and dino saved clocks untouched.
  - **K85-4 (Cave transfer label)**: no root `health` key added to the Cave save; `_completion_state()` still the only transfer packet (`cave_walkthrough.gd:814`), quicksave still carries health only inside the roach snapshot (same keys in `cave_roach.gd:171-177`).
  - **K85-5 (reward sites 1,3,4,6)**: no receiver file in the diff; rewards live inside `receive_damage`, which is untouched.
  - **Numbers**: every literal replacement is value-identical (30→`MAXIMUM`, 0.45→`COOLDOWN`, 96/110/140 reaches, mask 1/2/3/7, dot 0.9, quantum 1/1024 in the dino tick, `hit_from_inside` flags, exclusion RIDs). Cooldown gating positions preserved (dino ticks only when `>0`; Cave model unconditional; Hive sets clock before dispatch, as before).
  - **Strike options per site**: bonus flags match table 1.1 (sites 1,2,6,7,8,10 with bonus; 3,4,5,9,11,12,13 without); armed rules match (`EQUIPPED_NAME` default, `EQUIPMENT_WEAPON` for Hive reading `carried_inventory`, `CARRIED_WEAPON_SLOT` = old `melee_ready` including `can_use_weapon`); refusal order before aim/damage preserved everywhere; `after_landed` flags reproduce each site's tail (site 1 adds poison spend to `self.last_poison`; Hive return branch records with the `carried_inventory` item string and keeps the `has_method` guards).
  - **Interim Act 2 scale / debug kill**: `act2_creatures.gd` untouched; `debug_kill.gd` untouched and its API (`aimed()`, `receive_damage`, `peaceful_actor`, `state.actors`, `bodies`) survives on both populations.
  - **Saves**: no key renamed, added, or removed; validators get the same bounds via constants; last-writer order on load unchanged (Hive: inventory health supersedes encounter snapshot at `hive_review.gd:384-385`, as before); raw-write semantics kept (no clamp, 46/−3 preserved per the [Sol] correction).
  - **Hierarchy/attach**: owner constructed in `cave_walkthrough`, `jungle_review` (→ jungle family incl. `act2_map`, `darker_jungle`, `dragon_level`, `dark_halls`, `act2_jungle_return`, `hive_review`), `museum_review` (→ `museum_walkthrough`); every `_ready` chain calls `super`, no shadowing `health` vars anywhere in the family, no pre-existing `_notification` to shadow, no preload cycles through `player_combat`/`player_health`.

  ## Concerns checked and dropped

  - **JSON floats into the new typed setters** (`cave_roach.gd:213` `model.set("player_health", …)` — Godot parses JSON numbers as float): the identical `model.set` path existed at d5da60a into typed int vars, and the fixture quickload of `cave.json` (health 19) plus the legacy no-roach reset is exercised by `health_saved_fixture_test`, which deviation row 0612 records as passing at head. Cannot construct a failing scenario beyond what their gate already covers.
  - **`hive_warriors` `_pending_health` flush**: only reachable pre-tree (standalone tests); in-scene the parent's owner var is initialized before children enter the tree.
  - **`bind_health(preserve_live=false)` on quickload without roach**: resets the owner to 30, matching the old fresh-model behavior exactly.
  - **`cave_encounter` standalone model**: intentionally unbound, preserving the prototype review's pre-existing facade quirk (documented in `docs/foundation/player-combat-health.md:44-46`) — same as d5da60a.
  - **Boulder math**: `hive_damage_calculation.gd:74-75` gives `remaining = current − min(current, x)` ≡ `lose(loss)` — identical result.
  - **`scripts/lol2/*.gd.orig/.rej`**: pre-existing at d5da60a, not introduced by this branch.
  - **Rendered `docs/DEVIATIONS.md` rows**: not a defect, per instructions.

  Note: I did not run Godot or the test suite (per instructions); the equivalence arguments above are source-level, backed by the test evidence recorded in the branch's own deviation rows.

  APPROVE
