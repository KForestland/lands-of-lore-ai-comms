# FOUNDATION PLAN: three structure jobs for Sol

Fable, 2026-11-11. Plan only, no game code. All anchors are `scripts/lol2/<file>:<line>` on r19-work **d5da60a**.
Method: Fable plans, Sol builds, Kimi reviews. These land after Thursday's r19 playtest build is cut.

Grades: PROVEN = I read the line. LIKELY = inferred. UNKNOWN = not checked.

| Plan | Tasks | State |
|---|---|---|
| 1 | F-14 + F-15: one player-combat module, one owner of Luther's health | **in this file** |
| 2 | F-16: area host base, owners register themselves | **in this file** |
| 3 | F-06 + F-07: one whole-game save, 10 slots, autosave, native script state | **in this file** |

---

# PLAN 1: one player-combat module and one health owner (F-14 + F-15)

## 1.0 The short version

- This is structure, not balance. **Every number, every refusal and every save key stays as it is today**, including the interim Act 2 scale (DEVIATIONS 0558) and the debug kill key.
- Today the strike rule is written out in 19 places and differs between them in five small ways (table 1.2). The module does not smooth those differences away: it makes each one a named option, so the later combat work (R-01, I-03) changes one file.
- Health lives in three stores, picked by an if-chain in `player_starting_magic.gd:82-89`. The plan puts it in one node and turns the three old stores into forwarding properties, so no test, save or caller has to change on day one.
- Eight commits. Commit 0 adds tests that pin today's behaviour before anything moves; each later commit must leave them green.
- Old saves keep loading because **no save key is renamed, added or removed** in this plan.

## 1.1 What exists today (PROVEN)

### Strike damage: one rule, two wrappers

| What | Where |
|---|---|
| Base damage: Beast form 12, Lizard form 1, human 8 armed / 4 empty hand | `player_form_rules.gd:8-11` |
| Item bonus (Champion Stone) added to the base | `player_item_controller.gd:165-168` → `player_item_effects.gd:96` |
| A second, older constant `PLAYER_DAMAGE := 8` used as a default argument | `cave_encounter_state.gd:7`, `:38` |

### Strike sites (19 files that compute or gate a player blow)

Columns: **Bonus** = adds the item bonus. **Empty hand** = what a human with no weapon gets. **Reach** = how the target is found. **Clock** = which cooldown it uses.

| # | Site | Anchor | Bonus | Empty hand | Reach | Clock |
|---|---|---|---|---|---|---|
| 1 | Shared creature host (Act 2/3, Dark Halls, audible) | `scripted_creature_population.gd:365-378`, aim `:358-363`, click `:401-403` | yes | hits for 4 | ray 110, mask 3 | own `strike_remaining` `:28`, `:149`, 0.45 `:13` |
| 2 | Jungle dinosaurs | `jungle_dino_population.gd:248-259`, aim `:240-246`, click `:282` | yes | hits for 4 | ray 110, mask 3 | own, **saved** `:24-26`, `:111-112`, 0.45 `:14` |
| 3 | Cave roach population | `cave_roach_population.gd:263-282` | **no** | hits for 4 | cone: 96, dot ≥ 0.9, clear ray | Cave model clock `:281` |
| 4 | Cave single roach | `cave_roach.gd:78-83`, model `cave_encounter_state.gd:38-48` | **no** | hits for 4 | cone: 96, dot ≥ 0.9, clear ray | Cave model clock, **saved** (`cave_roach.gd:173`, validator `:189`) |
| 5 | Cave encounter prototype | `cave_encounter.gd:139-146`, reach `:6` | no (default 8) | n/a | cone 96 | Cave model clock |
| 6 | Hive: guardians, return population, executioner | `hive_warriors.gd:66-92`, aim `:107-111`, click `:112-116` | yes | hits for 4 | ray 96, mask 7 | own `cooldown` `:9`, literal 0.45 `:68` |
| 7 | Jungle confidante | `jungle_confidante.gd:168-173`, click `:184` | yes | **refused** | own `_aimed()` | none |
| 8 | Jungle river dam | `jungle_river_dam.gd:261-265`, reach 140 `:20`, click `:364` | yes | refused | ray 140, mask 1 | none |
| 9 | Jungle bramble | `jungle_bramble.gd:185-191`, click `:274` | **no** | refused | own `aimed_id()` | none |
| 10 | Act 2/3 struck movers (doors, thorns) | `act2_progression.gd:1249-1256`, reach 140 `:37`, aim `:1232-1246`, click `:1358` | yes | refused | ray 140, layer 1 | none |
| 11 | Cave old orc | `cave_old_orc.gd:306-309`, click `:316` | no | refused | own `aimed()` | none |
| 12 | Cave stalactites | `cave_stalactites.gd:207-212`, click `:226` | no | refused | own `aimed()` | none |
| 13 | Cave pillar trap | `cave_pillar_trap.gd:310-314`, click `:328` | no | refused | own `aimed()` | none |
| 14 | Museum: hourglass, escape wall | `museum_walkthrough.gd:557-559` (`melee_ready`), `:582-590`, `:632-647` | no damage number | needs a **carried weapon-slot item** | own reach tests | none |
| 15 | Museum sword skeleton | `museum_walkthrough.gd:650-659` | no damage number | refused | `can_reach_item` | none |
| 16 | Museum click chain (crystal, ivory, urns, torch pilot) | `museum_walkthrough.gd:698-701` | none | each prop's own rule | each prop's own | none |
| 17 | Cave click chain (rapids, lift, chains, roaches) | `cave_walkthrough.gd:667-687` | none | each prop's own | each prop's own | none |
| 18 | Daniel's bout | `l8_tribe.gd:49-50`, entered from `act2_creatures.gd:158-159` | as site 1 | **human only**, melee only | as site 1 | as site 1 |
| 19 | Character sheet "attack" figure | `museum_inventory.gd:467` | no | shows 4 | n/a | n/a |

Also striking but with no damage number at all (they only ask "was I clicked while in range"): `l9_noble_rails.gd:38-52`, `l8_tree_bridge.gd:125`, `l16_se_oil.gd:143`, `l16_fountain_ball.gd:96`, `l16_dry_fountain.gd:169`, `l19_sewer_forms.gd:205-306`, `jungle_harvest.gd:143-158`, `jungle_bacatta.gd:143-163`, `jungle_bacatta65.gd:127-148`, `jungle_kityara.gd:168-180`, `jungle_drunk.gd:73-78`, `jungle_exit_woman.gd:128-140`, `jungle_chief_hut.gd:97-106`, `museum_crystal.gd:41`, `museum_ivory.gd:64`, `museum_empty_urns.gd:59`, `museum_torches.gd:317`, `cave_prop83_lift.gd:351`, `cave_rapids_trigger.gd:51`, `river_chain_interaction.gd:55`, `indexed_chain_event.gd:27-39`. These are left alone in this plan except where commit 6 says so. That makes 40 files in all, which matches the lead's count.

### What happens after a blow lands

| Effect | Where | Which sites |
|---|---|---|
| Hit feedback | `combat_feedback.gd:11` `landed()` | most |
| Weapon poison coat is spent | `scripted_creature_population.gd:375` | site 1 only |
| Item hit recorded | `item_handlers.gd` `record_hit`, called at `scripted_creature_population.gd:376`, `jungle_dino_population.gd:256`, `hive_warriors.gd:78` | sites 1, 2, 6 (return population only) |
| Net of Exile, Prism | `net_hit` / `prism_hit` (`scripted_creature_population.gd:381-398`, dino `:262-`) | sites 1, 2, 6 |
| Melee reward (experience) | `cave_melee_reward.gd` via `cave_roach.gd:90`; `hive_live_melee_reward.gd` via `hive_return_population.gd:121` | sites 4, 6 |

### The interim Act 2 scale and the debug key

- `act2_creatures.gd:132-141`: `INTERIM_SCALE := 4`, six areas, two excluded actors (Daniel 23, Belial 90).
- Outgoing: `act2_creatures.gd:160` multiplies the amount **on the receiving side**. Incoming: `scripted_creature_population.gd:134` (hook, returns 1.0) overridden at `act2_creatures.gd:140-141`, applied at `scripted_creature_population.gd:201-203`.
- Debug kill: `debug_kill.gd:26-51` calls `pop.aimed()`, `pop.receive_damage()`, `pop.peaceful_actor()`, `pop.state.actors`, `pop.bodies`. Attached at `act2_map.gd:208` and `darker_jungle.gd:255`.
- So both sit on the creature side. **The module must not touch them**; it only has to hand `receive_damage` the same amount as today and leave those five population members in place.

### Health: three stores and a switch

| Store | Where | Used in |
|---|---|---|
| A. `roach.model.player_health` | `cave_encounter_state.gd:16` | Cave |
| B. `Warriors.health` | `hive_warriors.gd:6` | Hive |
| C. `host.health` | `jungle_walkthrough.gd:52`, `museum_walkthrough.gd:67` | Museum, Jungle, Dark Halls, all of Act 2/3 (they extend `jungle_walkthrough.gd`) |

- The switch: `player_starting_magic.gd:82-89` (`health()`, `set_health()`). A copy of it: `player_form_rules.gd:17-22` (full health on a form change). A third reader: `dev_diagnostics.gd:126-127`.
- With no store present `health()` answers 30 (`:85`), and `set_health()` would fail on `host.health` (`:89`). LIKELY only reachable in the Cave before the roach exists.
- Maximum 30 is a literal in at least: `player_starting_magic.gd:154`, `:164`; `player_item_controller.gd:158`; `player_form_rules.gd:20`, `:22`; `cave_encounter_state.gd:5`; `hive_warriors.gd:6`; `hive_review.gd:217`; `scripted_creature_population.gd:405`; `jungle_dino_population.gd:286`; `museum_inventory.gd:464`; `liquid_drowning.gd:147`; validators `cave_roach.gd:186`, `museum_walkthrough.gd:30`, `act_one_quest_state.gd:35`.

**Writers that bypass the switch (PROVEN):**

| Writer | Anchor |
|---|---|
| Cave roach population damage | `cave_roach_population.gd:150-155` |
| Cave single roach and prototype | `cave_encounter_state.gd:61-62` |
| Cave instant deaths | `cave_walkthrough.gd:1014`, `:1059` |
| Cave recovery | `cave_roach.gd:163` |
| Hive return population | `hive_return_population.gd:171`, `:183` |
| Hive boulders | `hive_boulders.gd:155-158` |
| Hive R retry | `hive_review.gd:216-217` |

**Writers through the switch:** 23 `set_health` calls in 20 files (creatures `scripted_creature_population.gd:203`, `jungle_dino_population.gd:147`; revive `:405`, `:286`; Heal `player_starting_magic.gd:164`; aloe `player_item_controller.gd:163`; and traps, bosses, drowning, poison: `l14_belial.gd:68`, `l13_belial.gd:45`, `player_dragon_blood.gd:56`, `dawn_player_damage.gd:82`, `dawn_modern_combat.gd:107`, `:130`, `l10_oil.gd:114`, `thieves_den_rooms.gd:228`, `player_spark_aura.gd:31`, `cave_cfall_room.gd:159`, `l9_flood.gd:45`, `l14_trap_route.gd:57`, `jungle_village_alarm.gd:173`, `museum_key_locks.gd:300`, `act2_creatures.gd:123`, `liquid_drowning.gd:188`).

**Where health is saved (keys must not change):**

| Key | Written at |
|---|---|
| `player_health` inside the roach snapshot | `cave_roach.gd:173`, restored `:213`, validated `:186` |
| `health` in the Cave save | `cave_walkthrough.gd:809` |
| `health` in the Museum checkpoint and transfer | `museum_walkthrough.gd:13`, `:186`, `:196`, `:457`, `:1001`, validated `:30` (1..30) |
| `health` in the Jungle / Act 2 inventory packet | `jungle_walkthrough.gd:436`, read `:455` |
| `health` in the Hive inventory state (living only; erased at 0) | `hive_review.gd:289-290`, `player_continuity.gd:25-27` |
| `health` in `hive_encounter` | `act_one_quest_state.gd:31-35` |

### Tests that reach into these internals

Counted by grep in `tests/`: `starting_magic.health/set_health` 48 files; `.strike()` 50; `strike_remaining` 23; `Warriors.health` 22; `model.player_health` 15; `host.health` style 13; `melee_damage` 5; the interim scale 1 (`act2_interim_combat_scale_test.gd`); `debug_kill_test.gd`.
This is why the plan keeps every one of those names alive as a forwarder. Rewriting 150 tests is not part of F-14/F-15.

## 1.2 The five differences the module must keep

1. **Item bonus or not.** Sites 1, 2, 6, 7, 8, 10 add it; sites 3, 4, 5, 9, 11, 12, 13 do not. LIKELY an accident of who wrote which host, but it is today's behaviour.
2. **Empty hand.** Creatures take 4 from a bare fist; props and the confidante refuse a weaponless human; the Museum hourglass and wall want a carried weapon-slot item; Daniel wants human form.
3. **"Armed" has three definitions.** `equipped_item != ""` (most), `player_equipment.weapon(...)` (Hive, `hive_warriors.gd:74`), and "carried and in the weapon slot" (Museum `melee_ready`).
4. **Reach.** Ray 110 (creatures), cone 96 with dot 0.9 (Cave), ray 96 (Hive), ray 140 (dam, movers), plus each prop's own test.
5. **Cooldown.** 0.45 s everywhere it exists, but on four separate clocks (Cave model, shared host, dinosaurs, Hive), two of them saved; props have none. It starts on any attempt in the Cave model and the Hive, and only on an aimed attempt in the two population hosts (`scripted_creature_population.gd:403` checks `aimed()` first).

## 1.3 Contract

**C1. One rules file.** `scripts/lol2/player_combat.gd` (static functions, no state) is the only file that names a damage number, a reach, a cone or the cooldown length.

```
const COOLDOWN := 0.45
const REACH_CREATURE := 110.0   const REACH_CAVE := 96.0
const REACH_HIVE := 96.0        const REACH_PROP := 140.0
const CONE_DOT := 0.9

enum Armed { EQUIPPED_NAME, EQUIPMENT_WEAPON, CARRIED_WEAPON_SLOT }

static func armed(host, rule := Armed.EQUIPPED_NAME) -> bool
static func may_strike(host, empty_hand_allowed: bool, armed_rule := Armed.EQUIPPED_NAME) -> bool
static func damage(host, with_item_bonus: bool, armed_rule := Armed.EQUIPPED_NAME) -> int
static func aim_ray(host, reach: float, mask: int) -> Dictionary        # the intersect_ray result
static func aim_cone(host, point: Vector3, reach: float, clear_mask: int, exclude: Array) -> bool
static func cooldown_ready(remaining: float) -> bool
static func cooldown_tick(remaining: float, delta: float) -> float
static func after_landed(host, owner, id: String, opts: Dictionary) -> bool   # poison, record_hit, net, prism, feedback
```

- `damage()` is `Forms.melee_damage(form, armed)` plus, when asked, the item bonus. `player_form_rules.melee_damage` keeps its numbers and becomes the private table behind it.
- `host` is the playable scene. The Hive passes its `review` node; `armed()` reads `carried_inventory.equipped_item` there and `equipped_item` elsewhere, exactly as today.
- `after_landed` takes flags `{poison, record, net, prism}` so each site keeps the set it has today.

**C2. Each strike site becomes one call with its options spelled out.** Example, site 1:
`PlayerCombat.damage(host, true)`; site 3: `PlayerCombat.damage(host, false)`. The option values are table 1.1, read across. A reviewer can check the whole migration against that table.

**C3. Storage of cooldown clocks does not move.** The four clocks stay where they are saved; only the arithmetic and the 0.45 come from the module. (Merging them is a behaviour change; see 1.8 Q1.)

**C4. One health owner.** `scripts/lol2/player_health.gd`, a `Node` named `PlayerHealth`, one per playable scene, reachable as `host.player_health_owner`.

```
const MAXIMUM := 30
var current: int            # 0..MAXIMUM, clamped on write
signal changed(before: int, after: int)
func value() -> int
func set_value(v: int) -> void
func lose(amount: int) -> int        # returns the new value; never below 0
func heal(amount: int) -> int        # never above MAXIMUM
func restore_full() -> void
func fallen() -> bool
```

- `player_starting_magic.health()` and `set_health()` stay, as one-line forwarders. All 23 callers and 48 tests keep working untouched.
- The three old stores stay **as names** and become forwarding properties:
  - `cave_encounter_state.gd:16` `player_health`: property; forwards to a bound owner when one is bound, else keeps its own integer (unit tests build the model alone).
  - `hive_warriors.gd:6` `health`: property forwarding to the scene's owner.
  - `jungle_walkthrough.gd:52`, `museum_walkthrough.gd:67` `health`: property forwarding to the owner.
- Every save and restore line in 1.1 keeps reading and writing those names, in the same order, so the saved bytes are identical and the last-writer-wins order on load is unchanged.
- No store present (Cave before the roach): reads still answer 30. Writes are now kept instead of failing. This is the one intended difference, and only where today's code errors.

**C5. Not in scope, and must not change:** creature AI and creature damage amounts; `player_defense.gd`; the 0.4 incoming factor; the interim scale; R recovery and its messages; spells (`spark` at `player_starting_magic.gd:180-206` stays); rewards; any number.

## 1.4 Migration order

One commit each. After every commit: the commit-0 tests, the affected-tests set, and `--check-only` on every touched script.

| # | Commit | Touches | Why it is safe |
|---|---|---|---|
| 0 | **Pin today's behaviour.** Add the tests of 1.6 and the saved fixtures. No game code | `tests/` only | Shows the tests pass on d5da60a before anything moves |
| 1 | Add `player_combat.gd` with constants, `armed`, `may_strike`, `damage`, cooldown helpers. Nothing calls it yet | 1 new file + its unit test | Dead code |
| 2 | Creature sites 1, 2, 3, 4, 5, 6 take damage, cooldown length and reach constants from the module. Local consts (`scripted_creature_population.gd:13-14`, `jungle_dino_population.gd:14-15`, `cave_encounter_state.gd:7`, `:9`, `cave_encounter.gd:6`, literal at `hive_warriors.gd:68`) become aliases of the module's, not deleted | 7 files | Same values through one more hop; alias names keep tests compiling |
| 3 | Prop sites 7 to 13 and the sheet figure (19) use `may_strike` and `damage` | 8 files | Each is a two-line swap |
| 4 | `aim_ray` / `aim_cone` replace the hand-built ray queries at sites 1, 2, 3, 4, 6, 8, 10. `aimed()` stays as a method on both population hosts (debug kill and tests call it) | 7 files | Same origin, direction, length, mask and exclusions, copied from the anchors |
| 5 | `after_landed` replaces the copied tail at sites 1, 2, 6 | 3 files | Flags reproduce each site's set |
| 6 | Museum `melee_ready` (site 14) and sword skeleton (15) call `may_strike` with `CARRIED_WEAPON_SLOT` / `EQUIPPED_NAME`. Sites 16, 17 and the "no number" list stay as they are | 1 file | Two predicates |
| 7 | **Health owner.** Add `player_health.gd`; attach it in the three scene bases; turn stores A, B, C into forwarding properties; `player_starting_magic.gd:82-89`, `player_form_rules.gd:17-22` and `dev_diagnostics.gd:126-127` use the owner | about 9 files | Every old name still reads and writes the same number |
| 8 | Replace the literal 30s listed in 1.1 with `PlayerHealth.MAXIMUM`, and the bypass writers' arithmetic with `lose()` / `restore_full()`. Save validators keep the bound 30 through the same constant | about 14 files | Mechanical; value identical |
| 9 | A source-scan test that fails if a damage number, `0.45`, or a `melee_damage(` call appears outside the module, and if any file other than `player_health.gd` assigns to a health store. Remove the alias consts from commit 2 where no test uses them | tests + cleanup | Keeps the 20th copy from appearing |

Commits 1 to 6 are F-14; 7 and 8 are F-15; 9 closes both. If the Act 1 hosts fight back, the fallback from the task sheet holds: land commits 2 to 5 for sites 1, 2, 6, 10 first, and the Cave sites after.

**Where the owner node is attached (commit 7):** `jungle_review.gd` `_ready` (covers Hive, Jungle, Dark Halls, Act 2/3), `museum_review.gd` `_ready`, and `cave_walkthrough.gd` setup. It must exist before any load path runs: `museum_walkthrough.gd:186`, `jungle_walkthrough.gd:455`, `cave_roach.gd:213`. I did not trace the `_ready` order in each; Sol must check it and, if a load runs first, create the owner lazily in the property getter.

## 1.5 How old saves keep loading

- No key in 1.1's save table changes name, type or range. The plan never writes a new key.
- Loads still assign to `health`, `player_health` and `Warriors.health`. Those names now forward to the owner, so a file written on d5da60a restores to the same number.
- Saved cooldown clocks (`strike_remaining` in the roach snapshot and the dinosaur state) are untouched (C3).
- The Hive rule "a living health travels, a death checkpoint keeps zero in `hive_encounter`" (`hive_review.gd:287-290`) is two different keys read from the same property; it holds as long as the reads stay where they are.
- Proof, not argument: commit 0 stores one save per area written by d5da60a under `tests/fixtures/saves_d5da60a/`, and a test loads each after every commit and compares health, form, equipped item and (where saved) the cooldown.

## 1.6 Tests

**Written in commit 0, on unchanged code:**

| Test | Kind | Pins |
|---|---|---|
| `player_combat_table_test` | headless | For form 0/1/2 × armed/empty × Champion on/off, the amount each of sites 1 to 13 hands to its receiver. A spy receiver records it. Expected values are today's: 8, 4, 12, 1, with or without the bonus per table 1.1 |
| `player_combat_refusal_test` | headless | Empty-hand human: creatures accept, props refuse, Museum wants a carried weapon, Daniel wants human form |
| `combat_cave_real_click_test` | **real input**, rendered | Cave roach: clicks to defeat, one hit only for two clicks inside 0.45 s, health after a creature blow |
| `combat_hive_real_click_test` | real input | Guardian 24 health: three armed clicks; cooldown; Warriors health after a blow |
| `combat_jungle_real_click_test` | real input | Dinosaur: clicks to defeat; saved `strike_remaining` survives F5/F9 |
| `combat_act2_real_click_test` | real input | L8 roaming creature of 200 health falls to 7 armed clicks (8 × 4 = 32 a blow); its blow costs Luther a quarter. Daniel (excluded) takes unscaled blows |
| `combat_prop_real_click_test` | real input | Bramble: empty hand does nothing, armed click cuts |
| `health_one_value_test` | headless | In each of the five scene types, write through each old name and read through every other: all agree |
| `health_saved_fixture_test` | headless | The d5da60a fixture saves load to the recorded values |
| existing, must stay green | | `act2_interim_combat_scale_test`, `debug_kill_test`, `area_health_handoff_test`, `player_continuity_*` (8), `act1_recovery_*` (5), `cave_defeat_recovery_anchor_test`, `cave_melee_reward_test`, `hive_live_melee_reward_test`, `cave_fighting_handoff_test`, `playtest_start_full_health_test`, `l8_tribe_serum_earned_test`, `combat_feedback_inventory_test`, `l19_bars_strike_test` |

- The real-input tests can use the rig in `lol2_bj12/tmp/bj14/` (`run.sh`, `bot.gd`: private Xvfb, really captured mouse, events through `Input.parse_input_event`). Sol's own BJ14 note applies: send discrete keys from a process frame, not a physics callback.
- Test aids must be declared in the registry row (checkpoint start, health top-up). None of these tests may set a position during the fight.
- `health_one_value_test` fails on d5da60a by design in one place only: it cannot be written before commit 7 for scenes where two stores exist at once. Write it in commit 0 as "each scene has exactly one live store and `starting_magic.health()` reads it", then tighten it in commit 7.

**Limits for every run:** at most 2 Godot at once in a lane (Sol's own cap stands), MemAvailable ≥ 10 GiB before each launch, `--audio-driver Dummy`.

## 1.7 Risks

| Risk | Guard |
|---|---|
| A site quietly gains or loses the item bonus or the empty-hand rule | `player_combat_table_test` runs per site, not per rule |
| Node order: the health owner does not exist when a load runs | Lazy creation in the getter; fixture test |
| Typed property on a `RefCounted` model (`cave_encounter_state`) used standalone by unit tests | The property keeps a local value when no owner is bound |
| `model.set(key, value)` restore at `cave_roach.gd:213` and `var health := 30` initialisers bypass a setter | LIKELY fine in Godot 4.7 (`set()` calls the setter); UNKNOWN, so the fixture test covers it |
| Ray change of one unit moves which creature is hit | Commit 4 copies origin, length, mask and exclusions per anchor; real-click tests count clicks |
| Wide test selection: `jungle_review.gd` and `act2_*` touch most of the suite | Commits 2 to 6 avoid the scene bases; only commit 7 touches them, so only one commit needs the wide gate |
| The interim scale is removed later and someone hunts for it in the module | It stays in `act2_creatures.gd:128-141` with its own comment; this plan's C5 says so |
| R-01 arrives with per-weapon damage before this lands | Then `damage()` is the one place to add an item argument; land commits 1 to 3 first if the order gets tight |

## 1.8 Open questions for the lead (none blocks the build)

- **Q1. One cooldown clock per scene?** Today four clocks let a player strike two owners inside 0.45 s (for example a creature of the shared host and a Hive guardian are never in one scene, but a dinosaur and a shared-host creature LIKELY can be). Merging is cleaner and changes behaviour slightly, and two clocks are saved. My advice: keep them apart now, merge in R-01.
- **Q2. The bonus difference (1.2 item 1).** Seven sites ignore the Champion Stone. Keep for now; decide in R-01.
- **Q3. One click dispatcher.** 19 owners each listen for the left button and rely on scene-tree order to decide who wins. A single dispatcher with registered targets is the right end state and belongs with plan 2 (owners registering themselves), not here. This plan leaves every click handler where it is.

## 1.9 What I could not confirm

- I read the code; I did not run anything for this plan. No test named above was executed on d5da60a.
- Whether any scene has two health stores live at once (for example a Hive scene whose host also carries `health` from a parent class). `hive_review.gd` extends `jungle_review.gd`, not `jungle_walkthrough.gd`, so LIKELY not.
- The `_ready` order against the load paths in each scene base.
- Whether a dinosaur and a shared-host creature can stand in one scene (Q1).
- Whether `museum_skeleton_population` and `hive_return_population` receive player blows anywhere other than through sites 6 and 15; I found no other caller by grep.
- Whether fixture saves from d5da60a can be produced headless for every area, or need a rendered run.
- The exact count behind "about 40 files": mine is 19 sites with a rule plus 21 click-only owners.
- `cave.gd`, `all_maps_review.gd`, `original_walk_review.gd` and the other review scenes were not read; they have no strike code by grep.

---

# PLAN 2: area host base, owners register themselves (F-16)

## 2.0 The short version

- Today a new owner script needs edits in up to five hand-written lists in its host. The plan replaces them with one per-level list file plus a small registry node, and then lets each owner declare what it needs (face claims, restore on load).
- Order of attachment, node names and saved keys do not change. The list files reproduce today's order line for line.
- One finding needs a decision before the last step: **41 owners have a `restore()` that no host calls after a load** (list in 2.1). Some LIKELY refresh themselves every frame; some may be real "wrong after F9" bugs. The plan registers them all but turns their restore on one level at a time, each with a save/reload test.

## 2.1 What exists today (PROVEN)

**Three host scripts carry Act 2/3**, all extending `jungle_walkthrough.gd`:

| Host | Levels | Attach list | Restore list (load) | Restore list (level arrival) |
|---|---|---|---|---|
| `act2_map.gd` | L10, L12, L13, L14, L16, L17, L19, L20 | `:106`, `:207-316`, 95 calls under nine `if area_id==` blocks | `apply_save` `:420-446`, 14 owners by node name | `apply_area_handoff` `:448-456`, **no owner restores** |
| `darker_jungle.gd` | L8 | `:254-275` | `apply_save` `:277-288`, 5 owners | `apply_area_handoff` `:290-`, same 5 |
| `dragon_level.gd` | L9 | `:135-149` | `apply_save` `:151-159`, 2 owners | `apply_area_handoff` `:161-170`, same 2 |

`act2_jungle_return.gd` and `dark_halls.gd` are two more hosts of the same family with their own `apply_save` (`:26`, `:205`).

**The five hand-written lists in `act2_map.gd`:**

1. Attach: `:207-316`. Order matters: some run only `if progression != null` (L16 `:251`, L17 `:247`, L19 `:294`, L20 `:303`), and two blocks exist for L16 (`:251` and the tail near `:262`).
2. Faces kept out of the static mesh before the base builds it: `:126-142`, per level, calling each owner's static `owns(face)`.
3. Faces kept out of collision: `include_collision_face` `:323-336`, again `owns(face)` per level, plus literal source-index lists for L10 (`:332-336`).
4. Restore after load: `:431-445`.
5. Special set-up arguments: `:183` (assembly ids per level).

**Owner conventions (counted by grep over `scripts/lol2/l<N>_*.gd`):**

- 110 owner files have a static `attach`. 106 take `(map)`; the others: `(map, area)` ×2, `(map, level)`, `(map, which = "tribe")`, `(map, which = "citadel")`, `attach_lift`, `attach_entry`; plus `placed_vqa_billboard.gd` `attach_dawn` / `attach_placenta`.
- Each sets a literal node name (`l10_fences.gd:10` "L10Fences", `l12_frozen_bow.gd:28` "L12FrozenBow") and keeps its state in `host.quest_state[KEY]` (85 files have a `KEY` const).
- 62 have `restore()`. 100 have a static `validate`; at least eight of those are called by name from `act_one_quest_state.gd:51-72`.
- 36 distinct `owns`-style calls appear in `act2_map.gd`.
- **112 lookups by node name** (`has_node("L…")`, `get_node("L…")`) exist outside the three hosts: owners find each other by name. Names are therefore part of the contract.

**Owners with `restore()` that no host calls on load (41):**
L8: Baccata, Tree. L9: Tower, MagicBridge, DeadBracers, Mirrors, NobleRails. L10: MainGate, Tombs, Braziers, Barrel, Oil, EmperorEntry, Emperor, Silverleaf. L14: TempleDoors, PriestBody, PriestRitual, PostShard, Hanging, Bedroom, Library, Niche, ShardBowls, Spiral, Trials, Tilt, FirePaths, FluteSlot, TrapRoute, IdolPedestals, HopperPlatform, Belial, SpiderPassage, Machines. L16: NwTraps, Greenhouse, SwChips, DryFountain, SeOil, FountainBall.
(Found by matching each owner's literal node name against the restore lists. An owner restored through another path, for example from `_process`, still appears here.)

## 2.2 Contract

**C1. One list file per level:** `scripts/lol2/area_owners/<AREA>.gd`, a constant array in today's order.

```
const OWNERS := [
  {"script": "l10_main_gate.gd"},
  {"script": "l10_emperor_entry.gd", "attach": "attach_entry"},
  {"script": "l8_tribe_dawn_hints.gd", "args": ["remains"]},
  {"script": "l16_nw_traps.gd", "needs": "progression"},
  ...
]
```

Adding an owner to a level is one line in that level's file. No host script is edited. (Fully automatic discovery by scanning the folder is possible but loses the explicit order; I advise against it.)

**C2. A registry node** `scripts/lol2/area_owner_registry.gd`, child `AreaOwners` of the host, with:

```
func attach_all(host, area_id) -> void          # runs the list in order, honouring "needs"
func owners() -> Array[Node]
func claims_static(face) -> bool                # replaces act2_map.gd:126-142
func claims_collision(face) -> bool             # replaces the owner part of :323-336
func restore_all(reason: String) -> String      # "load" or "arrival"; today's order first
func validate_quests(quests) -> String          # calls each listed script's static validate, when present
```

**C3. What an owner may declare (all optional; absence = today's behaviour):**

| Member | Meaning |
|---|---|
| `static func owns(face) -> bool` | face is drawn by the owner, not the static mesh (already exists in 36) |
| `static func owns_collision(face) -> bool` | face is left out of collision; defaults to `owns` |
| `func restore() -> void` | rebuild the visible state from `quest_state` |
| `const RESTORE_ON := ["load"]` or `["load", "arrival"]` | when the registry calls `restore()`. **Default is empty**: an owner not in today's lists is not called until its level is switched on in commit 7 |
| `static func validate(value, quests) -> String` | called by the registry for its `KEY` |
| `const KEY` | the quest key it owns; the registry rejects two owners with one key |

**C4. Unchanged:** node names; attach order; `quest_state` keys; the `(map)` signature; `act2_creatures`, `debug_kill`, `act2_world_items`, `act2_chargers`, sector light, blockers, body fit and progression set-up stay in the host where they are (`act2_map.gd:108-112`, `:190-208`, `:317-320`). They are engine parts, not level owners.

**C5. Where it stops (the task's fallback):** Cave and Museum trees are not touched. Hive and Act 1 Jungle are not converted in this plan; `dark_halls.gd` and `act2_jungle_return.gd` only if their lists turn out to be the same shape.

## 2.3 Migration order

| # | Commit | Touches | Safe because |
|---|---|---|---|
| 0 | **Pin today.** A test that loads each of the ten levels and records the ordered list of owner node names, the set of face indices excluded from the mesh, and the set excluded from collision. Golden files under `tests/fixtures/area_owners_d5da60a/` | tests | Golden data from unchanged code |
| 1 | Add the registry and the ten list files, generated from `act2_map.gd:207-316`, `darker_jungle.gd:254-275`, `dragon_level.gd:135-149`. Nothing uses them. A test checks each list against the commit-0 golden order | new files | Dead code, checked against golden |
| 2 | `act2_map.gd` attaches through the registry; the 95 hand calls go. Golden order test must be identical | 1 host | Same calls, same order |
| 3 | Same for `darker_jungle.gd` and `dragon_level.gd` | 2 hosts | Same |
| 4 | Face claims: `:126-142` and the owner half of `:323-336` ask the registry. The literal L10 source-index lists (`:128-129`, `:332-336`) move into the L10 list file as data, not into owners | 1 host + 1 list | Golden face sets must be identical |
| 5 | Restore: the three `apply_save` lists and the two handoff lists become `restore_all("load")` / `restore_all("arrival")`. The owners in today's lists get `RESTORE_ON` matching exactly where they are called now (so `act2_map` owners get `["load"]` only) | 3 hosts, about 20 owners | Same owners, same order, same occasions |
| 6 | Validation: `act2_save.quests_error` (`act2_save.gd:7-18`) also runs `registry.validate_quests`. The eight by-name calls in `act_one_quest_state.gd:51-72` stay until a test shows the registry covers them | 2 files | Adds checks; removes none |
| 7 | **The 41.** One commit per level: for each unlisted owner, a test saves mid-state, reloads and compares what the player sees or can do. If it already passes, set `RESTORE_ON := ["load"]` anyway (harmless, uniform). If it fails, that is a found bug: set it and note it in WHATS_NEW | owners + tests | Per level, each with its own proof |
| 8 | A source-scan test: no `preload(".../l<N>_….gd").attach` and no `get_node("L…").restore` in any host script | tests | Keeps the lists from growing back |

Commits 0 to 6 are the task. Commit 7 is the follow-up the finding calls for; if time is short it can be its own task, but the registry makes it cheap.

## 2.4 Old saves

Nothing in this plan writes, renames or removes a saved key. Commit 6 adds validation: a save that was accepted before must still be accepted, so the commit-0 fixtures from plan 1 (and plan 3's) are run through `validate_quests` before the commit lands; any owner validator that rejects a real d5da60a save is left out of the registry call and listed.

## 2.5 Tests

| Test | Kind | Shows |
|---|---|---|
| `area_owner_order_test` (commit 0) | headless, per level | Same owner names in the same order as d5da60a |
| `area_face_claims_test` (commit 0) | headless, per level | Same excluded face sets (mesh and collision) |
| `area_owner_new_owner_test` | headless | A dummy owner added through a test-only list attaches, claims a face, restores and validates with no host edit: the task's acceptance |
| existing save/reload tests for L8 to L20 | as they are | Still pass |
| `area_restore_<level>_test` (commit 7) | **real input where the state is visible**: open/cut/take something on real keys, F5, change it, F9, look and use | The 41, one level at a time |
| `bj14_sol_input_walk.gd` and the Act 2 earned tests | as they are | The chain still walks |

`act2_map.gd` selects 797 of 1,077 tests (plan section 1.2 of the master plan). Commits 2, 4 and 5 touch it, so batch them for one wide gate if the lead agrees; the golden tests give fast feedback in between.

## 2.6 Risks

| Risk | Guard |
|---|---|
| Order drift: an owner that reads a sibling in `_ready` now attaches earlier or later | Golden order test; list files are generated from the code, not retyped |
| `needs: progression` blocks: on a level without staged scripts today's code skips the owners | The `needs` field; test with progression absent (meta `lol2_map_preview` style load) |
| Turning on a restore that an owner was never written to survive twice | Default off; commit 7 per level with a test |
| A static `validate` stricter than what old saves hold | 2.4 |
| Owners that take extra arguments or have two attach functions | `attach` and `args` fields; 9 such cases are listed in 2.1 |
| Plan 1's open question Q3 (one click dispatcher) pulls scope in | Not in F-16. The registry's `owners()` list is what a dispatcher would use later |

## 2.7 What I could not confirm

- Whether each of the 41 is a real defect; I matched names only and ran nothing.
- That attach order matters at each point; I assume it does everywhere.
- The exact line range of the second L16 block and every `owns` call (lines longer than my read width were cut at 230 to 260 characters; Sol should generate the lists by script from the file, not from this text).
- Whether `dark_halls.gd` and `act2_jungle_return.gd` have owner lists of the same shape.
- Whether any test depends on the host having no child named `AreaOwners`.

---

# PLAN 3: one save for the whole game (F-06 + F-07)

## 3.0 The short version

- Today there are 15 separate one-file quicksaves, one per area, each in its own format with `version == 1` hard-coded. The opening screen has five separate Resume buttons and none for L9 to L20.
- **The native script state of every level is never written to disk (PROVEN).** It lives in a scene-tree meta that dies with the process. So F-07 is confirmed, and it is worse than the task sheet said: it is lost for the level you stand in too, not only for the others.
- The plan does not rewrite the 15 area formats. It adds **one slot file** that wraps the current area's save exactly as that area writes it today, plus the native bank for all levels, plus the few values that today travel between scenes in memory. Ten slots and one autosave slot.
- Old quicksaves keep loading through the code that loads them now, and appear in the load list as "old save".

## 3.1 What exists today (PROVEN unless marked)

**Files and formats**

| Area | File (`user://saves/`) | Format string | Code |
|---|---|---|---|
| Cave | `cavern_quicksave.json` | `lol2-restoration-walkthrough` | `walkthrough_save.gd:5-9`, `cave_walkthrough.gd:1262-1273` |
| Museum | `museum_quicksave.json` | `lol2-restoration-museum` | `museum_save.gd:4-5`, `museum_walkthrough.gd:900-913` |
| Jungle | `jungle_quicksave.json` | `lol2-restoration-jungle` | `jungle_save.gd:4-5`, `jungle_walkthrough.gd:468-490` |
| Hive | `hive_quicksave.json` | `lol2-restoration-hive` | `hive_save.gd:2-3`, `hive_review.gd:428-437` |
| Dark Halls | `dark_halls_quicksave.json` | `lol2-restoration-dark-halls` | `scenes/lol2/dark_halls.tscn:11-12` |
| L8 | `darker_jungle_quicksave.json` | `lol2-restoration-darker-jungle` | `scenes/lol2/darker_jungle.tscn:11-12` |
| L9 | `dragon_preview_quicksave.json` | `lol2-restoration-dragon-preview` | `dragon_level.gd:35-36` |
| L10 to L20 (8) | `map_<AREA>_quicksave.json` | `lol2-restoration-map-<AREA>` | `scenes/lol2/maps/<AREA>.tscn` (for example `L12_CM.tscn:13-14`) |

- The Act 2/3 shape (`act2_save.gd:52-66`): `{format, version: 1, inventory, quests, atlas_explored, player: {position, yaw, pitch, region?}}`.
- `quests` is the host's whole `quest_state`. It already carries every Act 2/3 owner's state for every level (plan 2), the creature packets `act2_creatures_<AREA>` (`act2_save.gd:9-14`), the item packet `act2_items`, and a partial native record store `act2_struck` (`act2_progression.gd:41`, written near `:1297`, restored `:1299-`).
- Version: `jungle_save.gd:38` rejects anything but `version == 1`. No migration code exists. One helper, `atlas_explored.gd` `migrate`, reshapes old atlas data.
- Writing is already careful: temp file, re-read and validate, then rename (`act2_save.gd:37-51`), 4 MiB cap (`:6`).
- A save is refused while paused or flying (`act2_save.gd:53-54`).

**What travels between scenes in memory only**

| Tree meta | Set at | Holds |
|---|---|---|
| `lol2_act2_native_bank` | `act2_progression.gd:377-382` on leaving a level; read `:217-220`, `:1211-1218` | Per level: native `state`, `locals`, `locals_e58`, `record_state`, `struck_durability` |
| `lol2_act2_handoff` | `act2_progression.gd:383`, read `:213-216`, `act2_jungle_return.gd:21-24` | The pack and quests for the next level (transient) |
| `lol2_adapter_exit_seeds` | `act2_progression.gd:387` | A flag |
| `lol2_darker_handoff`, `lol2_jungle_handoff`, `lol2_cave_completion` | `act_one_departure.gd:103`, `museum_walkthrough.gd:1081`, `cave_walkthrough.gd:788` | Act 1 one-way transfers (transient) |

`act2_save.save_host` writes none of the first row. The native host itself has the fields (`native_script_host.gd:146-153`) and a `reset_state()` (`:331`), but no snapshot or restore function.

**Loading from the opening screen**

- `original_game_gate.gd:77-99`: five buttons, Resume museum / jungle / Hive / darker jungle / Dark Halls. Each reads its file and sets a meta (`:291`, `:301`, `:311`, `:322`, `:352`).
- The host applies it in `_ready`: `museum_walkthrough.gd:382-384`, `jungle_walkthrough.gd:361-363`, `hive_review.gd:186-189`, `darker_jungle.gd:249-251`, `dark_halls.gd:118-120`.
- No resume path for the Cave, L9 or L10 to L20 (LIKELY: I saw no meta for them).

**In-game save UI:** `museum_interface.gd:143-149` (buttons "Save · F5", "Load · F9"), action at `:665`, path at `:52` and `jungle_walkthrough.gd:210`.

## 3.2 Contract

**C1. The slot file.** `user://saves/slot_01.json` … `slot_10.json`, and `autosave.json`.

```
{
  "format": "lol2-game", "version": 1,
  "written_unix": 1794300000, "play_seconds": 5321,
  "label": "Dracoid Cemetery",          # shown in the list
  "area": "L10_DC", "scene": "res://scenes/lol2/maps/L10_DC.tscn",
  "area_save": { ...exactly what this area's host writes today, its own format and version inside... },
  "native_bank": { "L8_SJ": {state, locals, locals_e58, record_state, struck_durability}, "L10_DC": {...}, ... },
  "session": { "adapter_exit_seeds": false }
}
```

- `native_bank` holds every visited level **including the current one**, snapshotted at save time with the same five fields the level change writes (`act2_progression.gd:378-381`).
- `area_save` is not reinterpreted. Its inner validator stays the judge of it.
- Same write discipline as today: temp file, validate, rename; the previous file is kept as `.bak`. Cap 8 MiB (4 for the area save as now, 4 for the bank; UNKNOWN real size, measure in commit 0).

**C2. One module** `scripts/lol2/game_save.gd` (static):

```
static func slots() -> Array[Dictionary]             # 11 rows: id, exists, label, area, written, play time, or an error text
static func save(host, slot_id) -> String            # "" or a message for the player
static func load(tree, slot_id) -> String            # validates, sets session + resume, changes scene
static func autosave(host, reason) -> String         # reason: "timer" | "arrival"
static func legacy_saves() -> Array[Dictionary]      # the 15 old quicksaves that exist
static func validate(doc) -> String
static func migrate(doc) -> Dictionary               # runs steps from doc.version up to current
```

**C3. Every playable host answers the same three calls** (most already do under other names):

| Call | Today |
|---|---|
| `area_snapshot() -> Dictionary` | New thin function. The dictionary each `_quicksave_unrecorded` builds before writing (Act 2/3: `act2_save.gd:56-66`; Jungle `jungle_walkthrough.gd:474-477`; Museum `:900-`; Hive `:428-`; Cave `:1262-`) |
| `apply_save(state) -> String` | Exists on every host of the jungle family; Museum, Cave to be checked |
| `can_save() -> String` | New. "" or the reason: paused, flying, fallen (health 0), a movie or conversation running, a level change pending |

Fallback if splitting a host's save function proves risky: the slot writer calls the host's existing `_quicksave_unrecorded(path)` with a work file and embeds the parsed result. Same bytes, no refactor.

**C4. Native state (F-07).** `native_script_host.gd` gets `snapshot() -> Dictionary` and `restore(d) -> String` for `state`, `locals`, `locals_e58`, `record_state`, with a validator (keys are strings, values integers or dictionaries of integers; finite; bounded count). `act2_progression.gd` uses them in the three places it now copies fields by hand (`:219-220`, `:378-379`, and the struck overlay `:1211-1218`), and the bank moves from the raw tree meta into the session holder of C5. `act2_struck` in `quest_state` stays as it is and keeps working for old saves; when both are present the bank wins (it is the fuller copy), and a test shows they agree.

**C5. One session holder.** An autoload `GameSession` (`scripts/lol2/game_session.gd`) holds `native_bank`, `adapter_exit_seeds`, `play_seconds`, `last_slot`, and the pending resume. The tree metas of 3.1 row 1 and 3 are read and written through it. (Rows 2 and 4, the transient handoffs, stay as metas in this plan.)

**C6. Autosave (owner decision D3).**
- Every 10 minutes of unpaused play, and on entering a map once the arrival has settled (after `apply_area_handoff` has run and the first physics frame has passed).
- Only when `can_save()` is empty; otherwise it retries every 5 seconds until it can. It never writes at health 0.
- Writes `autosave.json`; the previous one becomes `autosave.bak`. A one-line HUD note, no pause.
- The 10 minutes is the owner's number, not an invented one.

**C7. Keys and UI (kept minimal; the real menus are the shell phase).**
- F5 saves to the last used slot (slot 1 on a new game). F9 loads it. Both behave as now from the player's seat.
- The Tab interface's two buttons (`museum_interface.gd:143-149`) open a plain list of the ten slots plus autosave: label, area, date, play time. Pick to save or load; saving over a used slot asks once.
- The opening screen gets "Continue" (newest of all slots and the autosave) and "Load" (the same list, plus old saves). The five Resume buttons stay until the shell phase removes the developer screen.

**C8. Versions and migrations.** `game_save.gd` holds `CURRENT := 1` and an ordered list of steps `{from, to, apply(doc) -> doc}`. A step may change anything inside the document, including `area_save.quests`. A document with a higher version than the game knows is refused with a clear message. From this plan on, **a change to any saved shape comes with a step and a fixture of the old shape**; that becomes a review rule.

## 3.3 Migration order

| # | Commit | Touches | Safe because |
|---|---|---|---|
| 0 | **Fixtures and measurements.** One real save per area written by d5da60a (15 files) under `tests/fixtures/saves_d5da60a/` (shared with plan 1). A test loads each through today's path. Measure the native bank size after visiting L8, L10, L9 | tests | Unchanged code |
| 1 | `native_script_host.snapshot()/restore()` + validator + unit test (round trip on all 15 loaded levels; restore of a hand-broken snapshot is refused) | 1 file + test | New functions only |
| 2 | `GameSession` autoload; `act2_progression.gd` reads and writes the bank and the exit-seed flag through it, using commit 1. The tree meta stays mirrored for one commit so tests that set it still work, then goes in commit 8 | 2 files + project.godot | Same data, one holder |
| 3 | `area_snapshot()` and `can_save()` on each host family (jungle family first: Act 2/3, L8, L9, Jungle, Dark Halls; then Hive; then Museum; then Cave). `_quicksave_unrecorded` becomes "snapshot, then write": same file out | 4 to 7 files | Each host's own save test compares bytes before and after |
| 4 | `game_save.gd`: `save`, `validate`, `slots`, `migrate` (no steps yet). Writing only; nothing loads a slot | 1 new file + tests | Additive |
| 5 | `game_save.load`: sets the session, sets one meta `lol2_slot_resume`, changes scene. Every host family reads that meta in `_ready` beside its existing resume meta (anchors in 3.1) and calls `apply_save`. `act2_map.gd` and `dragon_level.gd` gain the resume read they lack. The native bank is in the session before the scene loads, so `act2_progression.gd:217-220` restores the level as it does after a level change | about 8 files | Reuses each host's own apply path |
| 6 | F5/F9 and the Tab buttons go to the slot; the list panel; "Continue" and "Load" on the opening screen; old saves listed and loaded through the unchanged resume metas | `museum_interface.gd`, `original_game_gate.gd`, hosts' key handling | Old path still present underneath |
| 7 | Autosave: timer and arrival hook, HUD note, `.bak` rotation | `game_session.gd`, host base | Additive; off under `--no-autosave` for tests |
| 8 | Migration proof: a deliberate version 2 with one real step (move the exit-seed flag, or fold `act2_struck` into the bank if the lead wants it), with the version-1 fixture kept. Remove the mirrored tree meta of commit 2 | `game_save.gd`, tests | Fixture test |
| 9 | Source-scan test: no host writes a save file except through `game_save.gd` or its own unchanged legacy function; no direct `lol2_act2_native_bank` meta access | tests | Guard |

Commits 1, 2 and 5 together are F-07; the rest is F-06. If F-06 has to be cut short, commits 1 to 5 alone already give "save in L8, quit, start, load, L10/L9 state as left".

## 3.4 How old saves keep loading

- The 15 old files are never rewritten or deleted. Their formats, validators and resume metas stay in the code.
- `legacy_saves()` lists the ones that exist; the load list shows them under the slots as "Old save: <area>, <date>". Loading one runs today's path exactly (`original_game_gate.gd:291-352` style). For L9 and L10 to L20, which have no resume button today, commit 5's new `_ready` read gives them one.
- An old save has no native bank. It loads with fresh native state for every level, **which is what it does today**; the list row says "level puzzles on other maps may be reset". Nothing gets worse.
- The first F5 after loading an old save writes a slot. From then on the player is on the new format.
- Inside a slot, `area_save` is today's shape with today's `version: 1`, so every inner validator and every fixture keeps working. Future shape changes go through C8.

## 3.5 Tests

| Test | Kind | Shows |
|---|---|---|
| `legacy_save_fixture_test` (commit 0) | headless | All 15 d5da60a saves still load, at every commit |
| `native_snapshot_roundtrip_test` | headless | Snapshot, reset, restore gives equal state on each level |
| `game_save_roundtrip_test` | headless, per host family | Save to a slot, read back, the inner area save equals what the old quicksave writes |
| `game_save_slots_test` | headless | Ten slots and the autosave are written and read independently; a damaged file shows as a row with an error and does not break the list; `.bak` is offered |
| **`game_save_quit_load_test`** (the F-07 acceptance) | **two processes, real input in the first** | Process 1: in L9 move a native floor or door by its real control; travel to L8; F5; quit. Process 2: start, Continue, travel to L9: the floor or door is as left. Fails on d5da60a (write it in commit 0 as an expected failure) |
| **`game_save_whole_game_test`** (the F-06 acceptance) | two processes, real input | Save in L8 with a changed pack, an open L10 tomb and a broken L9 rail; quit; load; all three as left |
| `game_save_migration_test` | headless | A version-1 fixture loads through the commit-8 step |
| `autosave_test` | rendered, real time scaled by test clock only if the game already has one; otherwise a 600 s constant read from `GameSession` and a test hook that advances play time | Fires at 10 minutes of play and on arrival; not while paused, fallen, flying or in a movie; never at health 0 |
| `save_keys_real_input_test` | real input | F5, change something, F9: restored. Tab → Save → slot 3 → Load slot 3 |
| existing | | Every `*_save*`, `player_continuity_*`, `area_health_handoff_test`, and the Act 2 earned tests |

Process-restart tests need a private `user://` per test (the trap recorded on 2026-10-10: isolate `user://` in test projects).

## 3.6 Risks

| Risk | Guard |
|---|---|
| The native bank restored into a level whose owners rebuilt themselves from `quest_state` disagree with it | Order on load is fixed: bank into the native host first (as on a level change today, `act2_progression.gd:217-220`), then `apply_save`, then owners' restore. `game_save_whole_game_test` covers three owners; plan 2's commit 7 covers the rest |
| Size: ten levels of native state on every autosave | Measured in commit 0; write off the main thread only if it shows a hitch (do not build that first) |
| A crash while writing | Temp file + rename + `.bak`, as today |
| Autosave at a bad moment (mid-jump over a pit, drowning) locks the player | `can_save()` also requires the player on the floor and not in liquid; the autosave is one of eleven slots, and `.bak` holds the one before |
| Act 1 areas have different save shapes (Museum uses a `checkpoint`) | The slot never reads inside `area_save`; only the host does |
| Jungle ↔ Hive ↔ rooms: state of the area you are not in may live in a meta I did not find | 3.7; Sol traces each pair in commit 3 and adds what he finds to `session` |
| Test selection: commit 3 and 5 touch every host base | Batch them for one wide gate each |
| Save scumming or R recovery rules change later (owner D6: game over + reload) | Not here. `Continue` and `load` are the hooks that work will call |

## 3.7 What I could not confirm

- I ran nothing. No size, timing or load was measured.
- That the native bank is the only cross-level state outside `quest_state`. I listed every `set_meta("lol2_…")` in `scripts/lol2`; a static var or an autoload holding state would not show up in that search.
- Whether Act 1 areas keep each other's state anywhere between visits (Jungle while in the Hive, the rooms, the monastery). The one-way transfers are in 3.1; the round trips I did not trace.
- Whether `atlas_explored` in an area save covers all levels or only the current one (`atlas_explored.gd:96-100` reads one host field).
- Whether the Museum and Cave hosts have an `apply_save(state)` that takes a dictionary, or only a path-based load.
- Whether fixture saves for all 15 areas can be produced without playing to each (dev checkpoints exist for Act 1 and my BJ14 `ck_before_*.json` files cover L8, L9, L10 on bf8b21f, not d5da60a).
- The exact lines of the Museum, Hive and Cave save builders beyond the function heads I cite.
- Whether play time is counted anywhere today (I assume not).
- Slot count and autosave rhythm come from owner decision D3; the autosave-on-arrival detail ("after the arrival has settled") is my reading of it.

PLAN READY
