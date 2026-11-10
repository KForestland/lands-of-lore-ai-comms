• Audit complete. I read the full plan (127 tasks), the owner decisions, all 15 hintbook chapters plus the item/creature/spell chapters, and then verified each suspected gap against the code tree, dropping every one that turned out to be covered (solarium — `dark_halls_atrium.gd`; dam — `jungle_river_dam.gd`; Beast bridge — `jungle_bridge_break.gd`; Kelsrick path — `jungle_kelsrick.gd`; ironwood sap — `jungle_harvest_source.json`; cave flood/Halberd — `cave_flood_movie.gd`; Dark Sword altar — `l13_altar.gd`; ruby of truth — `l19_dawn_curse.gd`; ancient-charge state — `tests/player_ancient_charge_state_test.gd`; and more).

  Three gaps survived verification.

  ## Gap 1 — City of the Ancients (L16): every side room and minor puzzle is missing from the plan

  **What is missing.** The hintbook names five L16 side experiences, none of which appears in any task or in code:

  - **Secret Storeroom** — quill pen behind a force field, ivory chip in the gold-bars statue, chasing the *right* branch of the ball of light, a second skeleton key behind a chip door, ceiling collapse on pickup (`hintbook.txt:4975-5011`).
  - **Chalice / "Hall of Alchemy"** — mandrake root in the chalice puts Luther to sleep; a timed dream room with scrolls, spells and recipes (`hintbook.txt:5017-5030`). The book explicitly warns to carry mandrake into the city for this (`hintbook.txt:1169-1173`).
  - **Transformations-R-Us** — exhibit room that transmutes a placed item into another (the renewable source for a ring of regeneration and ice seeds), with exhibit doors that can crush Luther (`hintbook.txt:5052-5069`).
  - **Silverleaf Chasm** — ivory chip in the street pedestal, ball-of-light chase (*left* branch this time), floor appears on a timer with a warning bell (`hintbook.txt:5073-5109`).
  - **The four Chip Quest rooms** — Water Torture (timed flood + darkness), Leap of Faith (walk the straight line), Dancing in the Fountain (freeze it by one of five named methods), Be a Blockhead (box-stacking + ceiling-crash escape) (`hintbook.txt:5115-5203`).

  **Evidence.** `master_tasks.json:699-713` (M-15) scopes L16 to towers, box/disk, Starry Tower raisings and the centre fight only; the phrase "four ivory chips and their four city spots" gestures at chips but the four chip-quest *mechanics* are nowhere named. `MASTER_PLAN_COMPLETE_GAME.md:45` admits towers/box/disk/figure are unbuilt but never mentions these rooms. The L16 code is chain/towers only: `scripts/lol2/` contains `l16_arrival_elevator`, `l16_centre_*`, `l16_dragon_*`, `l16_dry_fountain`, `l16_fountain_ball`, `l16_greenhouse`, `l16_ne_tower`, `l16_nw_traps`, `l16_se_oil`, `l16_sw_chips`, `l16_terrace_lips` — nothing else. `docs/DEVIATIONS.md:489` shows the team knows the storeroom only as a hintbook citation, not as planned work. S-23 (`master_tasks.json:1575-1588`) might host a room *view* but not the puzzle loops (chalice trigger, dream timer, transmutation, floor timer).

  **Nearest task:** M-15 (its scope stops at the towers).

  **Proposed task — "L16 side rooms: storeroom, chalice dream, transformation exhibits, silverleaf chasm, four chip quests."** Lane **grok** (the plan already found no native rows for box/disk/figure, so these rooms need the same D5-style reverse engineering + book/longplay adapter rule). Acceptance: the player enters each room by its book trigger and walks out with its prize — skeleton key and ingredient hoard from the storeroom, at least one scroll/recipe from the timed Hall of Alchemy, one transmuted item from Transformations-R-Us, a silverleaf from the chasm before the floor vanishes, and one ivory chip from each of the four chip quests.

  ## Gap 2 — Dracoid Ruins (L9): door rafting and the Saar death-match room are in no task

  **What is missing.** (a) **Door rafting** — dragging a floor door into the river, hopping aboard, grabbing on and steering with the keys; it is the book's documented "hard way" for the priest's errand (`hintbook.txt:3585-3606`, `3755-3771`). (b) **The Saar death-match room** — losing to a Saar does not kill Luther; he wakes red in a chamber full of Saar, and the same room is findable empty by exploring (`hintbook.txt:3612-3625`). This is also a non-death defeat consequence that U-05's "every death shows the game-over screen" framing (D6) does not contemplate. (c) The book's named ruin secrets — serpent statue, ring behind a locked gate, palace secret (`hintbook.txt:5698-5702`) — which under D4 must at least be adjudicated (in the data, or listed absent), and no task does that for L9.

  **Evidence.** `master_tasks.json:639-652` (M-11) enumerates only "Valkyrie crossbow, barrels (BUG-002), optional tombs, tower extras". The L9 scripts cover bracers, the statue walk, pyre, mirrors, magic bridge, tower, noble rails, flood and the escape grate — `l9_escape.gd:1-2` is explicitly only the final grate raft ("original table122 and raft82 geometry"), not free door rafting. There is no Saar file anywhere (R-14 will build the creature fight, not the capture room), and no serpent/locked-gate-ring/palace-secret content.

  **Nearest task:** M-11.

  **Proposed task — "L9 optional mechanics: door rafting, Saar death-match capture room, adjudicate the book's ruin secrets."** Lane **grok** for the native rows (door-buoyancy records, the defeat-redirect trigger), sol build. Acceptance: the player drags a door into the river, rides and steers it to the low eastern arch on the priest's-errand route; a player downed by a Saar wakes in the capture chamber and can fight out or die to the game-over screen; each of the three named secrets is foundable in play or listed as absent-from-data with the evidence.

  ## Gap 3 — Spell rules: ancient-magic charge gating and the no-target fizzle are in no task's scope

  **What is missing.** Two book-documented spell rules: level-5 spells consume "a special kind of magic found or created" — i.e. an Ancients' Stone / Force Pod charge per cast (`hintbook.txt:505-507`, `1294-1296`, `1143-1145`) — and "if there is no logical target for a spell, it fizzles, saving Luther the expenditure in Mana" (`hintbook.txt:510-511`). The charge rule gates all four level-5 spells, two of which are on the main chain (Expel at the mother, Trinity at the faux Scotia), yet the spell-core task's scope is "schools, levels, mana cost, learning, spell bar, casting power by hold" and the boss acceptances say only "is a cast, not an E prompt" — nobody owns whether those casts require a charge, and if they do, nobody owns guaranteeing the player holds a stone at those story beats.

  **Evidence.** `master_tasks.json:1113-1126` (R-05 scope, no charge or fizzle), `1204-1220` (R-11 story casts, no charge), `1143-1156`/`1173-1186` (R-07/R-09 acceptances silent on charges). Code has charge *state* (`scripts/lol2/ancient_stone_effect.gd`, `tests/player_ancient_charge_state_test.gd`) but no task wires it as a per-cast cost, and "fizzle" appears nowhere in `scripts/lol2/` or `tests/`.

  **Nearest task:** R-05.

  **Proposed task — "Spell rules: level-5 ancient-magic gating and no-target fizzle."** Lane **grok** (confirm the native charge-cost and fizzle sites in the disassembly, one-day box, then book-rule adapter per plan §4.2). Acceptance: with zero charges the player cannot cast Regenerate, Trinity, Banish or Expel until using an Ancients' Stone (one charge consumed per cast); casting Spark at bare floor fizzles and costs no mana; and the L20 chain is proven with the rule on — a player reaching the mother and the faux Scotia holds, or can earn, the stone each cast needs.

  Everything else the book names — all 15 areas, both endings and every named movie, all 30 spells, the named creature kinds, the item families, and the optional rooms I checked (shrine, clubhouse, thieves' den, treehouse room, hopper tunnels, Dark Halls entry/exit, L12 side areas) — lands in at least one existing task, verified against code where the plan's claim was doubtful.
