# Game discussion, 2026-11-01 (lead: Opus) — "what is left to make LoL2 a complete game?"

Owner's ask: spend today on meta analysis with Grok and Astra; discuss the game and what needs to be done.
Method (rubber duck): walk the whole game as a PLAYER, segment by segment in the hintbook's order, and say plainly what our
playtest build r12w does there today. Then the systems a player touches everywhere. Then questions for each lane.
Sources: Prima hintbook chapters 5-14 (hintbook.txt), Brady official guide (Ch. 4-9 spheres; OCR in brady_guide.txt),
PROGRESS.md, the board. Statuses are the lead's honest read; correct them.

## 1. The player's journey (Prima chapter order)

| Segment (Prima ch.) | What the player does | r12w today |
|---|---|---|
| Draracle's Caves (5) | prison escape, Kenneth, guards, curse, lift, side journey | PLAYABLE. Leftovers: Kenneth lowers the wall not gates, bridge lever, 2 guards after the clip, boxes, orc clip |
| Draracle's Halls / Museum (5) | Belial, exhibits, hourglass, escape wall, dragon | PLAYABLE (blockers on). Leftovers: dust prop, dragon click point |
| Huline Jungle (6) | village, Baccata, Kelsrick, thieves, shops, hidden shrine, Wossname, blue ball | PLAYABLE end to end. Village dialogue weak; Baccata hostile after leaving (owner bug) |
| Hive Caves (7) | rescue, Big Orc sword, Waxman, floors 3-8, getting out | PLAYABLE route. Owner reports: flute bridge, elevator bridge, door, puzzle, rock trap, traps not working |
| Dark Halls (optional, Act 1) | Rix, windows puzzle, crates, shades | PLAYABLE slice. Closing walls / moving bookcases missing |
| Savage Jungle L8 (8) | gift to Daniel, temple, wild village, Sleeping Beauty, horse/hopper tunnels, fishing, torches, clubhouse, Claw Mountains trips | MAP + night look DONE; first departure (gift, temple, guard, key) built modern on astra-progression (NOT in r12w); rest not built |
| Dracoid Cemetery L10 (9) | gold/white/blue globe chargers, barrel, oil, priest's errand, emperor's errand, Silverleaf | MAP only (walkable, exits). No steps |
| Dracoid Ruins L9 (10) | combat, Saar death match, Mage's tower (white orb charger), priest/emperor errands | MAP only |
| Claw Mountains L12 (11) | (to read) | MAP only |
| Huline Temple L14 (12) | (to read) | MAP only |
| City of the Ancients L16 (13) | (to read) | MAP only |
| Final sequence L17/L19/L20 (14) | Belial's chamber, the end | MAP only |

Honest summary: Act 1 is a game; Acts 2-3 are ten connected, walkable, populated maps with almost no story yet.

## 2. Systems the player touches everywhere

| System | r12w today | Gap |
|---|---|---|
| Movement, forms (human/lizard/beast), curse | done (original curse rules) | lizard drowning outside 4 areas |
| Items | 170 defs, icons, pick-up, inventory, one router for use/equip/on-hit; ~14 handlers hosted | most item EFFECTS (107 handlers) not built; new Act 1 items' E pickup unproven |
| Spells (heal group, Spark, Summon, Prism, Mists of Doom; 30 total) | Spark, Prism (+ some Act 1) | most spells, learning from scrolls/recipes |
| RPG (stats, XP, levels, skills) | none visible | whole system |
| Dialog / NPCs / shops | rooms with movies/hotspots in Act 1; shops partly | general dialog runner, NPC state (friendly/hostile/follow), Act 2/3 NPCs |
| Creatures / combat | Act 1 tuned per area; Act 2/3 placed, generic AI, borrowed stats | real stats (Brady/Prima tables), behaviours, combat polish |
| Puzzles / mechanisms (chargers, orbs, levers, doors, lifts) | native host + adapters; movers done | a generic mechanism kit for Act 2/3 (chargers, errands) |
| Save / load | per area; handoff between areas | save versioning (W24), one save across the whole game |
| Automap (Atlas), Journal, Help | exist | Act 2/3 coverage |
| Sound / music | some clips | music (HMI), ambience, most sfx (last phase) |
| Enhanced edition | ideas + lighting plan | later |

## 3. Questions — each lane answers in review_20261101/<lane>_game.md

For BOTH:
Q1. Correct my table: where is my status wrong (too optimistic or too pessimistic)?
Q2. The single biggest risk to finishing Classic LoL2, and how you would reduce it.
Q3. Which SHARED systems must exist before Act 2/3 story can be built fast (e.g. quest-state store, NPC dialog runner,
    errand/charger kit, generic mechanism kit, creature stat tables)? Rank them.
Q4. Your proposed ORDER of work for the next 4 weeks (areas and systems), given the owner's phase order
    (maps done -> items -> RPG -> dialog -> small fixes; known behaviour built modern directly).
Q5. RUBBER DUCK one segment end to end: walk it as the player, step by step, with the hintbook/Brady page for each step,
    and say per step: what our build does today, what is missing, native or modern, which test proves it.
    ASTRA: Dracoid Cemetery (Prima ch.9, Brady sphere maps). GROK: Hive Caves (Prima ch.7) — the owner's broken
    mechanisms there (flute bridge, elevator bridge, door, puzzle, rock trap, traps).

ASTRA only: Q6. Rough size per Act 2/3 area in "slices" (W22), and what would make you 2x faster.
GROK only: Q7. Which unknowns truly need the oracle or decoding (numbers/formulas no book gives), and which can stop
    under the owner rule. Turn the Brady Ch.2/3 tables into the plan for items/spells.

Lead will synthesize the answers into ROADMAP_20261101.md, post disagreements back for one more round, then show the owner.
