# Kimi K50 — L12 Claw Mountains main chain trace (prep for Fable BJ05)

Lead spot-check: l12_citadel.gd:63 (Baccata appears only with l8_baccata phase 3), act2_progression.gd:277 (Larkhon dose gate), tmp/l12_larkhon_arrival_earned_save.json exists — confirmed.

## Arrival

L12_CM is reached from L8_SJ (Darker Jungle, `scenes/lol2/darker_jungle.tscn`) through the Larkhon pass:

- **Edge**: `act2_travel.json` edge `L8_SJ:region:3277:…` → `L12_CM` level 12, **selector 1**, grade ADAPTER. Region 3277's native group 1908 carries the level-change command bytes (`020100001c2c` = level 12); pinned by `tools/verify_l8_larkhon_source.py`.
- **Gate**: `act2_progression.gd:_change_level` (scripts/lol2/act2_progression.gd:277) refuses the crossing unless `l8_larkhon_state.used()` — the Larkhon Vapors dose receipt (mix Amaranth Serum + Silverleaf, activate, apply to the guardian's chest; host `scripts/lol2/l8_larkhon.gd`, doc `docs/l8-larkhon.md`). Once used, the guardian stays asleep forever and passage regions 3277/3278 stay cleared (DEVIATIONS row 0307/0440 softlock fix). Refusal appends a context journal hint.
- **Arrival pose**: `act2_progression.gd:72 arrival_pose()` reads the L12 pack `assets/lol2/generated/maps/L12_CM/area.json` arrivals: **selector 1 = source (−347, 5603), region 735** — the bottom of the icy gulch, matching the task's "rock cleft onto snow". Selector 2 = (3211, 18903) region 3642 = the return arrival from L13. Selector 0 = (2784, 18222) region 1948.
- The earned-arrival save for the walk start exists: `tmp/l12_larkhon_arrival_earned_save.json` (STORY-035 output; regression anchor `tmp/l12_larkhon_arrival_regression_anchor.json`, SHA de88903c…).

## Main chain in L12 (ordered)

| # | Step (book, ch. 11 Claw Mountains) | Story | Host file:line | Native/adapter | Test → qualified save |
|---|---|---|---|---|---|
| 1 | Climb out of the icy gulch, NE path, take the **non-gorilla** branch (hintbook.txt:3924-3926) | STORY-036 | none — physical walk over original ravine ramp (region 735→756) and raised controls 113/112/110/107/109/111/106/108; Act2Map owns movement | native terrain, no adapter (docs/l12-gulch.md) | `tests/l12_gulch_earned_test.gd` → `tmp/l12_gulch_qualified_save.json` |
| 2 | Avalanche valley: hug the right-hand wall; glacier floor drops (book 3972-3974) | STORY-037 | `scripts/lol2/l12_glacier.gd:59` (one-shot trigger regions 932/916; moves floors 919-930, hides logs 52-57) | **ADAPTER** — modern trigger + 60 Hz clock substitute for prop335/group1068; native avalanche control91/prop436 unhosted (DEVIATIONS 0378) | `tests/l12_ice_earned_test.gd` (+ l12_glacier_moving_earned_save) |
| 3 | Ice ledge → platform hops → running leap as Human into the far cave (book 3989) | STORY-037 | none — ordinary jumps across original platforms 104/101/103/98/102/99/100/95 into region 2417 | native terrain | same test → `tmp/l12_ice_crossed_earned_save.json` |
| 4 | Search Kenneth's body → picture; throw it at ground → Kenneth's charm (book 3994) | STORY-038 | `scripts/lol2/l12_citadel.gd:20` (`search_body`), `:36` (`throw_picture`), state in `l12_citadel_state.gd` | **ADAPTER** — once-only E search; atomic Kit picture→charm conversion; native impact handler unhosted (DEVIATIONS 0379) | `tests/l12_citadel_earned_test.gd` (4/4 PASS) |
| 5 | Meet/hear Baccata in the ice tunnel (book 3993) | STORY-038 | `scripts/lol2/l12_citadel.gd:44` (`talk`), appearance at `:63` gated on `l8_baccata` phase 3 (earned L8 rescue) | **ADAPTER** — one-shot text summary; native speech branches unjoined | same test |
| 6 | Citadel-entry special scene → level change to L13 (book 3999) | STORY-038 | `scripts/lol2/l12_citadel.gd:50` (`begin_entry`), intercept in `act2_progression.gd:288`; edge `L12_CM:control:74` → L13/1, grade ADAPTER | **ADAPTER presentation over native command** — movie 13 CITADEL staged as Ogg (`l12_citadel_movie.gd`; assets **installed** at `assets/lol2/generated/l12_citadel/citadel.ogv`), plays paused, then native handoff | same test → `tmp/l13_citadel_arrival_earned_save.json` (L13 arrival 1) |
| 7 | *Inside the citadel = L13_RC* (book 4089-4210): globes/egg basin, elevator, maidens, Dawn, pink steps, bridge, Belial spawn, Dark Sword altar, dreamstone | STORY-039…044 | `l13_egg_door.gd`, `l13_eggs.gd`, `l13_elevator.gd`, `l13_prison.gd`, `l13_spires.gd`, `l13_dawn_prison.gd`, `l13_dawn_release.gd`, `l13_bridge.gd`, `l13_belial.gd`, `l13_altar.gd`, `l13_return_pad.gd` | all **ADAPTERs** over pinned source bytes (DEVIATIONS 0380-0390) | `tests/l13_*_earned_test.gd` suite |
| 8 | Dreamstone in the wall slot, take it back, exit (book 4206) | STORY-044 | `scripts/lol2/l13_exit_lock.gd:30` (`can_leave`), gate at `act2_progression.gd:276` | ADAPTER slot UI over native region 489 command (PROVEN) → L12 selector 2 | `l13` exit tests |
| 9 | Ice cave to the opening over the river; drop onto a floe (book ~4214) | STORY-045 | `scripts/lol2/l12_river_rafts.gd` (movables 50/51/55 follow source opcode18 waypoints) | **ADAPTER** — continuous 120 u/s motion, rider carry (DEVIATIONS 0394) | `tests/l12_exit_cave_earned_test.gd` → `tmp/l12_exit_cave_qualified_save.json`; `l12_river_niche_earned_test.gd` → `tmp/l12_river_niche_qualified_save.json` |
| 10 | River-level niche: Spark the tripod → obsidian chain mail, wear it (book 4225) | STORY-045 | `scripts/lol2/l12_niche_armor.gd:31` (Spark 1/3 reveals item5 = def 54, E equips) | **ADAPTER** (DEVIATIONS 0395) | `tests/l12_niche_armor_earned_test.gd` → `tmp/l12_niche_armor_qualified_save.json` |
| 11 | Leave the floe at the glacier-log bank (sprint-jump the 91-unit lip) | STORY-046 | `scripts/lol2/l12_river_rafts.gd:75` (`jump_speed` ballistic within 400 of bank vertex 3144,-12218) | **ADAPTER** (DEVIATIONS 0396/0275) | `tests/l12_river_return_earned_test.gd` → `tmp/l12_river_return_qualified_save.json` |
| 12 | Cross ice bridge; as Lizard crawl the crevasse (book 4236-4239) | STORY-046 | `scripts/lol2/l12_crevasse.gd:33-46` — Spark 1/3 opens original control 91 gate; E toggles Human/Lizard via curse controller, **requires the earned Dreamstone carried** | **ADAPTER** (DEVIATIONS 0397) | `tests/l12_crevasse_earned_test.gd` → `tmp/l12_crevasse_qualified_save.json` |
| 13 | Melt the frozen figure, catch the blue bow before it sinks (book 4240) | STORY-046 | `scripts/lol2/l12_frozen_bow.gd:45,51` — Spark starts a 3 s sink window, E catches def 35 Darkbow ("Blue Bow") | **ADAPTER** — native bow identity UNKNOWN; modern reward at the original Melt-man 89 position (DEVIATIONS 0398/0277) | `tests/l12_frozen_bow_earned_test.gd` → `tmp/l12_frozen_bow_qualified_save.json` |
| 14 | Climb the glacier logs back up (book 4254) | STORY-047 | `scripts/lol2/l12_glacier.gd:47-54` — restores logs 52-57 and makes floors 914/915 one-sided **after the earned L13 exit-lock receipt** | **ADAPTER** (DEVIATIONS 0399/0278) | `tests/l12_logs_approach_earned_test.gd` → `tmp/l12_logs_approach_qualified_save.json`; `l12_return_logs_earned_test.gd` → `tmp/l12_return_logs_qualified_save.json` |
| 15 | Reverse the valley to the gulch; exit region 734 → L8 (book 4254-4263; Larkhon still asleep) | STORY-047/048 | native region 734 group 0 command; `act2_travel.json` edge grade **PROVEN** → L8 selector 4 (arrival region 3449) | native | `tests/l12_gulch_return_earned_test.gd` → `tmp/l12_gulch_return_qualified_save.json` (182-waypoint walk, real scene transfer) |

## Exit to the next level

The "next level" is two-stage, matching the book:

1. **L12 → L13 (Ruloi Citadel)** — control:74 edge (ADAPTER grade, position 3684,-1292,-19361). Gated by `L12Citadel.begin_entry` (l12_citadel.gd:50): requires `state().talked` (Baccata heard) and movie assets; the movie overlay completes/skips → saved `movie_seen` receipt → deferred native `_change_level` to L13 arrival 1.
2. **L13 → back through L12 → L8 → L14 (Huline Temple)** — the book's real route onward. L13 exit gated by `l13_exit_lock.can_leave()` (slot unlocked, stone retrieved and carried). The final L12 exit (region 734, PROVEN) lands in L8 at selector 4; then STORY-048's east-bank river return jump (ballistic ADAPTER 0279, `docs/l8-river-return.md`, `tmp/l8_river_return_qualified_save.json`) and the corridor into the jungle, where the L14 temple door (`act2_temple_door_state.gd`, STORY-049) takes the Dreamstone. Re-entry L8→L12 afterwards only needs the used-dose receipt (Larkhon never re-wakes, DEVIATIONS 0440).

## Existing walks/saves

Every step above is already earned-qualified individually; each test replays from the previous step's immutable qualified save (all under `tmp/`, reports in `tmp/regressions/…/report.json`):

- Arrival: `l12_larkhon_arrival_earned_save.json` (+ regression anchor)
- Gulch: `l12_gulch_qualified_save.json` (SHA 86117775…, the STORY-036/037/038 anchor)
- Ice route: `l12_ice_crossed_earned_save.json`
- Citadel approach: `tmp/l13_citadel_arrival_earned_save.json` (L13 arrival with charm)
- Return leg: `l12_exit_cave_qualified_save.json`, `l12_river_niche_qualified_save.json`, `l12_niche_armor_qualified_save.json`, `l12_river_return_qualified_save.json`, `l12_crevasse_qualified_save.json`, `l12_frozen_bow_qualified_save.json`, `l12_logs_approach_qualified_save.json`, `l12_return_logs_qualified_save.json`, `l12_gulch_return_qualified_save.json`
- Walk fixtures: `tests/fixtures/l12_*_walk.json` (gulch, valley, cave, exit cave, logs approach, return logs…)
- Other: `tests/l12_map_test.gd`, `l12_creature_test.gd`, `l12_item_test.gd`, `l12_level_test.gd`, `l12_mover_test.gd`, `atlas_readable_l12_test.gd`

No single test walks the whole L12 chain end-to-end — coverage is per-step relay on the qualified-save chain. BJ05's owner-like walk can follow exactly this relay order.

## Likely first stops for BJ05

1. **Baccata dependency is a hard hidden gate.** `l12_citadel.gd:63` only spawns actor 30 if `quest_state.l8_baccata.phase == 3` (the earned L8 trap rescue). Without it, `begin_entry` refuses forever with "Speak with Baccata before entering the citadel" while Baccata never appears — an unwinnable state with no guidance. Verify Grok's BJ01 handoff save carries phase 3 before starting; if an owner can reach the citadel without the rescue, that's the first finding.
2. **The avalanche is a substitute, not the native event.** The book's avalanche (control 91 / prop 436 / group 2312) and its audio/shake/damage are unhosted; the hosted effect is the separate prop335 floor-drop with a modern region 932/916 trigger (DEVIATIONS 0378). Expect a presentation gap when entering the valley.
3. **Gorilla village and tiger cave are unhosted side content.** Gorilla actors 38-45 exist as population only; the hut bracers, the tiger-cave Lizard tunnel, and the globe-raised lake platform with the axe have no host scripts, no journal notes, nothing. Off the main chain, but an owner poking around will find them inert.
4. **Citadel entry needs the movie** — assets are installed (`assets/lol2/generated/l12_citadel/citadel.ogv`), so no blocker expected; saves are refused during the overlay (Esc/Space skips).
5. **Return-leg earned gates to re-verify live**: crevasse form-choice requires the Dreamstone actually carried (`l12_crevasse.gd:33`); log restoration and one-sided floors 914/915 require the L13 exit-lock receipt (`l12_glacier.gd:49`); the 3-second frozen-bow catch window is real and refreezes on expiry.
6. **Maps note**: `L12_CM.tscn` has `map_blockers_enabled = false` — bit0 blocker edges are off; the L12/L13 gates rely on the hosts' own RegionBlockers rows instead. Atlas L12 places exist (`atlas_places.gd`, 6 places + 2 ways out) but no earned L12 walk fixture fed them yet (DEVIATIONS 0565) — a fresh owner walk is exactly what's missing.

