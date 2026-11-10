# Kimi K71 — L8 Darker Jungle quest chain as a player sees it (for Fable BJ12)

Lead spot-check: l8_journey.gd:55 village target suppression and scripted_creature_population.gd:401-404 revive-in-place confirmed.

## Chain table

Book lines are from `~/AI_COMMS/reference_hintbook/hintbook.txt`. All script paths are under `~/opus_work/lol2_r18/` (branch r19-work).

| # | Step (book) | Book line | Host file:line | Player trigger | Gate | Player-visible? |
|---|---|---|---|---|---|---|
| 1 | F2 'darker' start arrival | — | `tests/fixtures/dark_halls_earned_darker_arrival_state.json` (player at (-4577,32,1168), blade `jungle:kityara:Empty_hand` carried, no l8 state) | F2 playtest-start resume (`scripts/lol2/original_game_gate.gd:13`) | none | Y |
| 2 | Meet Daniel / offer blade / hoppers / pick up dropped blade | 2920–2930 | `scripts/lol2/l8_journey.gd:69` (`interact`), `l8_journey_state.gd:34-54` | E at entry anchor (-3854,32,1190), then panel buttons "Offer…", "Continue the meeting", "Pick up the dropped blade" | blade carried | Y ("E — Meet Daniel") |
| 3 | First Huline Temple visit (priest snatch) | 2932–2941, 2984 | `l8_journey.gd:122-126` (auto-`visit_temple`), `l8_journey_state.gd:55-58` | walk within 160 of temple anchor (758,32,2046) — no key press | none | Y (text notice only; no scene — "L8 has no opcode 21 for that snatch") |
| 4 | Show guard the blade → admitted | 2984–2992 | `l8_journey.gd:180-184`, `l8_journey_state.gd:59-65` | E at village anchor (676,32,-4541) → "Show Daniel's blade" | `temple_visited` AND `gift=="recovered"` | **N unless temple visited or blade recovered** — target suppressed (`l8_journey.gd:55`) and guard actor 113 starts `present:false` (`act2_populations/L8_SJ.json`) |
| 5a | Herbalist treehouse jars (sap/amber/aloe) | 2990–2992 | `l8_journey.gd:195-196`, `l8_herbalist.gd:21` | panel buttons "Herbalist — take …" | admitted | Panel-only; no hut/hotspot in the world |
| 5b | Shaman clicked "thoroughly" → cemetery key | 2993–3001, 3257 | `l8_journey.gd:198`, `l8_journey_state.gd:66-73` | panel button "Visit the shaman" → adds `l8:shaman:Dracoid_sigil` | admitted | Panel-only |
| 5c | Doorway right of the shaman (news) | 2995–2996 | `l8_journey.gd:194`, `l8_backroom.gd:34` | panel button "Visit the room behind the shaman" → audio voices 225–237 | admitted; audio staged | Panel-only, audio-only |
| 5d | Daniel's treehouse (return blade) | 2997–2999 | `l8_journey.gd:197`, `l8_journey_state.gd:40-43` | panel button "Visit Daniel and return the blade" | admitted, gift recovered | Panel-only |
| 6 | Travel L8 → Dracoid Cemetery (L10) | 3257–3259 | `scripts/lol2/act2_travel.json` edge `L8_SJ:region:908` group 564 → L10 selector 1 | walk into region 908 | none (physical) | Y (walk-in) |
| 7 | Cemetery main gate (the "key") | 3257 | `scripts/lol2/l10_main_gate.gd:42-49`, hint at :65 | E at gate AIM (-125,46,-995) → "E — Unlock with the Dracoid Sigil" | sigil in inventory | Y |
| 8 | Emperor's tomb: 3 globes + ankh → remains | ch. 9; 3443 | `scripts/lol2/l10_emperor.gd:61-71`, `l10_emperor_state.gd:37-68` | E at receptacles 125/126/127, ankh 143, then E at sarcophagus → room → E take remains | bracers carried to understand him | Y |
| 9 | Ruins → wet exit → wake at lake, ruins closed | 3024–3034 | `scripts/lol2/l8_shore.gd:12-24` | automatic on native level change L9_DR → L8 selector 5 (`act2_travel.json` `L9_DR:prop:104`) | `l9_escape.escaped` | Y (notice + Dawn20 spawns) |
| 10 | Dawn takes the bracers → Control Token | 3026–3033 | `scripts/lol2/l8_dawn.gd:22-31`, `l8_dawn_state.gd` | E at Dawn AIM (-4252,65,-1515) | shore arrived, Human form | Y ("E — Give Dawn the Bracers of the Dead") |
| 11 | Cemetery again, Emperor babbles, Silverleaf grows | 3046–3055, 3478–3482 | `scripts/lol2/l10_silverleaf.gd:30-37` (`revisit`) | E at Emperor's sarcophagus without bracers (`l10_emperor.gd:113` routes to `revisit`) | `l10_emperor.remains` + Dawn exchange done + no bracers | Y |
| 12 | Pick nine Silverleaf | 3051–3055 | `l10_silverleaf.gd:46-66`, `l10_silverleaf_harvest.gd` | E at grown tree props 159–170 (reach 150, aim dot>0.8) | grown; Human | Y ("E — Pick Silverleaf"); trees are scale-0 before growth (`l10_silverleaf.gd:28`) |
| 13 | Present leaf → initiation fight with Daniel | 3069–3074 | `l8_journey.gd:186-189`, `scripts/lol2/l8_tribe.gd:20-48` | panel button "Offer Silverleaf — begin initiation" → speech (Enter skips) → arena → left-click spar / E yield | admitted + `l10_silverleaf.grown` (`l8_tribe.gd:22`) + Human + at village | Y |
| 14 | Shaman takes a leaf → Amaranth potion | 3075–3078 | `l8_journey.gd:190-193`, `l8_tribe.gd:95-102`, `l8_shaman_trade.gd:23` | panel button "Offer Silverleaf to the shaman" → `act2:L8_SJ:shaman_amaranth` (def 119) | tribe member (`l8_tribe.gd:97`) | Y (panel-only) |
| 15 | Combine potion + leaf | 3119–3121 (book: slots in the tree-room back) | `scripts/lol2/l8_larkhon.gd:45-55` (`mix`) | inventory: select serum → "Mix with Silverleaf" button (`scripts/lol2/museum_inventory.gd:223-226,313`) → Larkhon Vapors | serum + any def-117 leaf carried, Human, not flying | **Weak** — bespoke button on the serum only; no drag-combine, no tree-room slots |
| 16 | Activate vapors, right-click Larkhon's upper chest | 3148–3157 | `l8_larkhon.gd:56-77`, `darker_jungle.gd:323-325` | inventory "Activate vapors" Use button, then right mouse on chest (≤180, dot>0.97) | vapors mixed+activated | Y (guidance hints near guardian) |
| 17 | Pass to Claw Mountains | 3155–3177 | `l8_larkhon.gd:78-87` (unblocks regions 3277/3278) | walk past sleeping guardian | dose applied | Y |

## Likely player blockers (ranked)

1. **The Wild Village special scene has no world hotspots at all — one E-panel at the guard spot does everything.** The book's "several views" (herbalist treehouse with jars, shaman, doorway right of the shaman, Daniel's treehouse; hintbook 2984–3009) are four buttons inside a single panel that only opens within 160 of (676,32,-4541) (`l8_journey.gd:169-203`). `darker_jungle.gd:257-274` attaches no other village interaction hosts, and the milestone doc says "STORY004 B1 room-view navigation remains open" (`docs/act2-wild-village-earned-loop.md`). A player hunting for "the point to click" on the treehouses finds nothing clickable — this matches the owner's report verbatim.
2. **Arriving at the village before the temple/blade gives total silence.** `l8_journey.gd:55` skips the village target unless `temple_visited` or `gift ∈ {recovered, returned}`; the guard (actor 113) starts `present:false` and is only spawned after the temple visit (`l8_journey.gd:104-105`, `act2_populations/L8_SJ.json`); and `l8_village_hints.gd:20-27` (`stuck_id`) has **no** journal-note case for `place=="village"` with gift `unoffered`/`delivered`. So the natural "walk to the big tree first" player sees no guard, no prompt, no hint, no note. (The 2026-11-07 fix only covers the blade-recovered-temple-unvisited case.)
3. **The cemetery key is only reachable through that same panel.** "Visit the shaman" (`l8_journey.gd:198` → `l8_journey_state.gd:66-73`) silently adds the sigil; its label never mentions the cemetery or a key. If the player can't open the panel (blocker 2), the L10 gate just refuses: "The Dracoid Sigil opens this gate." (`l10_main_gate.gd:45`).
4. **"Serum from the small hut" does not exist.** The serum is granted only by the post-initiation panel trade (`l8_tribe.gd:95-102` → `l8_shaman_trade.gd`); the herbalist "hut" yields only sap/amber/aloe (`l8_herbalist.gd:3-4`); the backroom is audio-only with no item (`l8_backroom.gd`); the tree-room (`tests/l8_tree_room_earned_test.gd`) hosts the shard slot, not the book's amaranth+leaf slots (hintbook 3119). Before initiation the trade button is never even shown (`l8_journey.gd:190`).
5. **The combine step is discoverable only by accident.** Mixing lives behind a serum-specific "Mix with Silverleaf" button in the inventory (`museum_inventory.gd:223-226`), not the book's drag-item-on-item recipe and not the tree-room slots. In-game guidance (`larkhon_serum_needs_leaf`) only appears near the Larkhon (`l8_larkhon.gd:18-25,103-105`). The chest dose then needs a dot>0.97 aim cone (`l8_larkhon.gd:67`).
6. Chain logic itself is complete end-to-end (key→gate→Emperor→remains→escape→shore→Dawn→revisit→growth→harvest→initiation→trade→mix→dose→L12) with consistent cross-map persistence (`act2_items_catalog.gd:107-118` keeps the non-catalog sigil across saves).

## Tests that bypass the player

- `tests/l8_journey_live_test.gd` — teleports `host.player.position` to each anchor and calls `journey.interact()` directly; its own PASS line admits "production map walk/render still pending".
- `tests/l8_journey_state_test.gd`, `tests/silverleaf_use_contract_test.gd` — pure state-machine/unit fixtures, no scene at all.
- `tests/l8_gift_earned_test.gd` — physical walk to the entry, but every action is a direct `journey.interact()` call; no E key, no panel.
- `tests/l10_silverleaf_growth_earned_test.gd` — walks physically, but growth is triggered by direct `emperor.interact("remains")` after `camera.look_at`; no E key.
- `tests/l10_silverleaf_harvest_earned_test.gd` — direct `leaves.pick(tree)` calls; the E-pick path in `l10_silverleaf.gd:_unhandled_input` is unexercised.
- `tests/l8_initiation_earned_test.gd` — direct `journey.interact("initiation", leaf)`; the bout drives `pop.strike()` with scripted `camera.look_at`, and `tests/l8_shaman_trade_earned_test.gd` calls `tribe.leave_arena()` / `journey.interact("shaman_silverleaf")` directly.
- `tests/l8_larkhon_earned_test.gd` — mostly honest (real inventory Mix/Use buttons, real jump), but the chest dose is a direct `guardian.offer()` after `look_at`; the right-click input path (`l8_larkhon.gd:106-109`) is untested.
- Only `tests/l8_village_temple_first_test.gd` drives the real E key into the village panel — and only for the refusal case. The positive admitted-village button flow (show_guard → visit_shaman → key → herbalist/backroom/Daniel buttons) is never exercised through the actual UI a player uses.

## Smallest fixes

1. Remove the target suppression at `l8_journey.gd:55` (always let the village target resolve) and spawn guard 113 from map start — the panel/hint already degrades gracefully (TEMPLE_FIRST / NEED_DANIEL lines), so a village-first player gets an explanation instead of silence.
2. Add the missing `stuck_id` case in `l8_village_hints.gd:20-27` for place=="village" with gift `unoffered`/`delivered` ("Meet Daniel at the entry; take back the dropped blade").
3. Put world-anchored E hints (reusing the existing reach/ray pattern) at the herbalist treehouse, shaman view, backroom doorway, and Daniel's treehouse that open the same panel actions — or implement the STORY004 B1 room-view navigation. Relabel "Visit the shaman" → "…— receive the cemetery key" and the trade button to name the Amaranth Serum.
4. Surface the Mix step: journal note whenever serum+leaf are both carried (not just near the Larkhon), or a generic drag-onto-item combine in `museum_inventory.gd`.
5. Drive one earned test through the real E-panel for the admitted-village buttons and the right-click Larkhon dose, replacing the direct `interact`/`offer` calls.
6. Lake fall: yes, there is a death/recovery. (5372, 2889) sits in liquid region 3320 (floor −550, surface 53; `assets/lol2/generated/liquid/L8_SJ.json`), so feet at −486 are submerged: the 15 s drowning clock (`river_drowning_state.gd:5`) kills via `set_health(0)` with "You drowned. R returns to the checkpoint; F9 loads your save." (`liquid_drowning.gd:173-177`). But R actually revives at 30 hp **in place on the lake bed** (`scripted_creature_population.gd:401-404`), still submerged, so the player drowns again — there is no out-of-world kill plane or bank respawn. Smallest fix: revive at the nearest bank point (or make the notice honest about reviving in place), and cap repeated drowning loops.

