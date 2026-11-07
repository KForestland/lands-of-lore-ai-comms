# Kimi K33 — meta-duck groundwork: Faux Draracle (L20) + the Mother Beast (L19), 2026-11-07

Lead: accepted as the BF02/BF03 briefs. Correction to the lead's backlog wording: the MOTHER must NOT die (book: expel the curse into her at ancient-magic level 5; the birth follows; the DEMONS are the real kills). Both beats can use the existing creature/combat pipeline (spawn via act2_creatures, receive_damage -> death clip). Movies placenta.vqa / e224e.vqa need the MOVIES.MIX decode, else logged adapters.

# Kimi K33 — meta-duck groundwork: the FAUX DRARACLE (STORY-091) and the MOTHER BEAST (STORY-086/087), 2026-11-07

  Both beats are record-only today: quest state validates, no creature is shown, no kill is possible, no movie plays. Method: the meta duck (`META_DUCK_METHOD_20261107.md`). Sources: hintbook.txt, `I33_act3_frames.md`, `act3_tail_ids.md`, X01/X04 NOTES under `grok_research/patches`. Key new finding vs. K32's assumptions: **the project's live creature system (`act2_creatures.gd` → `scripted_creature_population.gd`) already runs on L19_BC and L20_BB with native sprites and death clips for exactly these actors** — a real kill needs no new combat machinery.

  ---

  ## Beat A — the FAUX DRARACLE in L20 (STORY-091)

  ### A1. Intent
  *Gate* with a *threaten* wrapper. Belial conjures a Draracle look-alike to block the last corridor; killing it is the condition to force the doors and reach Belial's room. The book deliberately downplays difficulty — "much less of a challenge than Scotia was, so fight him any way you please" (hintbook.txt:5541-5542) — so it is a story gate, not a skill test: any weapon works, and the kill is what unlocks the path.

  ### A2. Player contract, in order
  1. **Setup** — after the brick/white-ball/fireball room (STORY-090), "you confront Belial, who creates a faux-Draracle for you to fight" (hintbook.txt:5535-5536). No longplay frame shows the creation or the fight (`I33_act3_frames.md:34`: "the faux-Draracle was not named by the picture").
  2. **The fight** — "fight him any way you please. The Dark Sword works pretty well" (hintbook.txt:5541-5542). Any weapon, free-form combat.
  3. **Kill gates the doors** — "After the faux-Draracle is dead, force the door open" (hintbook.txt:5543). Native door records: movable 52 "Final gateway" (-3554, 4740), region 795, group 9472, opcode 14 only; and the three Crystal Key door pairs (movables 50/51 region 871, 53/54 region 812, 55/99 region 218, each with opcode 1) (`act3_tail_ids.md:17-18`).
  4. **The hall** — save in the hall, "run down the hall and attack the door. Go through once you have it open" (hintbook.txt:5543-5546).
  5. **Belial's room** — "Belial begins to speak" (hintbook.txt:5546). Native: Control 61 "Trigger" (-3493, 3843), region 763; actor 75 BELIAL (def byte 2) at (-1238, 3207), region 177; locals `Final_Belial_Trigger`, `Evil/Good_Belial_talking` unbound (`act3_tail_ids.md:18`).

  ### A3. EXACT vs APPROXIMATE
  **EXACT (mechanics):** a real, killable faux-Draracle actor; any weapon may kill it; `killed=true` is the gate for forcing the doors and for the key/door sequence in order (0→1→2); entering Belial's room only after the doors; all of it persists over save/reload.
  **APPROXIMATE (presentation):** Belial's creation flash, the Draracle's attack look (the book names none — "fight him any way you please"), sprite scale/timing, any speech (no speech cstring was copied, `l20_faux_draracle.gd:5`).

  ### A4. What `l20_faux_draracle.gd` records vs shows
  File: `~/opus_work/lol2_act3/scripts/lol2/l20_faux_draracle.gd` (116 lines).
  - Records: E near actor 46 with any equipped weapon sets `struck=true` but **forces `killed=false`** (lines 97-103); three "keys" recorded in order at fixed spots after `struck` (lines 105-115); `room` = all three keys (lines 60-61); `belial_seen` near actor 75 only after `room` (lines 84-88). `validate()` **rejects any state with `killed != false`** (line 32); `moves_doors()` returns `false` (lines 24-25); `SPEECH=""` (line 11).
  - Shows: only two hint labels — "E — strike actor 46. The kill stays false." (line 90) and "E — record the next key. The doors stay still." (line 92). No Draracle, no Belial, no fight, no door motion.
  - Tests: `tests/l20_faux_draracle_test.gd`, `tests/l20_faux_draracle_earned_test.gd` (earned walk from `res://tmp/l20_armory_earned_save.json`, X04 NOTES:5).

  ### A5. Native records and presence in the project
  | Item | Evidence | In project? |
  |---|---|---|
  | Actor 46, DRARACLE, (-6921, 4828), region 1272, event list 4668; opcodes 9, 13, 16, 22, 8, 2 (no opcode 1/3; bodies not copied) | `act3_tail_ids.md:17` | **Yes, as data**: `scripts/lol2/act2_populations/L20_BB.json` row actor 46, def 0, health 2500, behavior 14, `present: false`, loot 10344876 |
  | DRARACLE sprite set | population def 0 | **Yes**: `assets/lol2/generated/act2_creatures/L20_BB/sprites.json` def 0 "DRARACLE" — idle 12, walk 24, rise 14, **death 28 frames**, corpse 1; `attacks: []`; currently `peaceful_adapter: true` |
  | Prop 111 "Rift" (-6821, 4827), region 1192 | `act3_tail_ids.md:17` | Record only |
  | Movable 52 "Final gateway" + 3 Crystal Key door pairs | `act3_tail_ids.md:17-18` | Record only; `l20_faux_draracle.gd:3-4` notes opcode 1 not entered, doors stay put |
  | Control 61 trigger, actor 75 BELIAL | `act3_tail_ids.md:18` | Record only (also `l20_finale.gd:8,15`) |
  | Movies for STORY-091 | `act3_tail_ids.md:17` | "None joined" — no movie in this beat |
  | Creature/combat host | `act2_map.gd:137` attaches `act2_creatures.gd` per area | **Live on L20_BB today**; spawn/wake/attack/death pipeline in `scripted_creature_population.gd`, proven on museum skeletons and cave guards |

  ### A6. Smallest faithful plan — yes, the existing creature system can host a real kill
  1. **Spawn actor 46 through `act2_creatures`**: the population row exists with `present: false`; the spawn path already exists (`native_field` bit `0x16` → `State.spawn`, `act2_creatures.gd:47-50`). Trigger it when the player reaches the post-armory corridor (adapter trigger, logged in DEVIATIONS, until actor 46's opcode 9/13/16 bodies are decoded).
  2. **Make it fight**: clear `peaceful_adapter` for L20 def 0 and give it an offense. `attacks` is empty in the source clip table, so any attack visual is an adapter — but the book requires none ("fight him any way you please"). A minimal spell-toss adapter using the existing `dawn_projectile_world.gd` machinery is enough.
  3. **Real kill → real flag**: the existing `receive_damage` → death-clip (28 native frames) → corpse pipeline does the kill; on death set `killed=true` in `l20_faux_draracle`, relax `validate()` (`l20_faux_draracle.gd:32`), and let `killed` gate the three key/door records and actual door movement (opcode-1 door pairs via the existing movable machinery). Persist over save via the existing `quest_state` + `restore_from_quests` path.
  4. **Belial's room**: on `room`, entering region 177 shows actor 75 (already in the population, `present: false`, behavior 6) and hands off to the K32 finale.
  5. **Prove like a player**: extend `l20_faux_draracle_earned_test.gd` — earned walk kills the Draracle with a real weapon strike, forces the doors in order, reaches actor 75; capture vs. the (currently unbound) longplay window; owner playtest.

  ---

  ## Beat B — the MOTHER BEAST in L19/L20 (STORY-086/087)

  ### B1. Intent
  *Reveal* + *teach* + *gate*. Dawn reveals the real plan — do **not** kill Belial in the womb; help him be born by expelling Luther's curse into the mother beast — and teaches the one mechanic the beat gates on: cast the curse at ancient-magic **level five**. The cast triggers the birth scene, the demon fight, and the chase. The ruby of truth is a *reward* offer of deliberately unclear purpose (hintbook.txt:5479-5480).

  ### B2. Player contract, in order
  1. **Meet Dawn** — "After you exit from the elevator, you meet Dawn. Continue to 'speak' with her by clicking on her" (hintbook.txt:5474-5475). Frames: `g_00378` at 298:10 and `g_00379` at 298:40 — "a light-haired woman in a white blouse and dark vest, in the green chamber" (FRAME for the figure; no curse line on screen; the name Dawn stays the book) (`I33_act3_frames.md:29`).
  2. **The reveal** — killing Belial in the womb is not the answer; expel the curse into the mother beast (hintbook.txt:5476-5478).
  3. **The ruby** — keep clicking and "she offers Luther the ruby of truth" (hintbook.txt:5478-5480). Native: prop 78 "Dawn good" (2802, 882), region 1461, opcode 3 identity 0xFBF884D7, definition 69, name slot `67-Ruby of trth`, handler 101, group 1566 (`act3_tail_ids.md:12`).
  4. **The mother room** — two rooms; the inner one holds the mother beast; attacking it "all you get for your trouble are fireballs shot back in Luther's face" (hintbook.txt:5481-5484). Native host: prop 242 "Frank's Placenta" (-1160, 4258), region 262 (`act3_tail_ids.md:13`).
  5. **The cast** — "use the curse spell at the ancient magic level-level-five" (hintbook.txt:5484-5485).
  6. **The glob and the birth** — "a purple glob shoots from Luther and enters the mother beast. At this point, the 'Belial's birth' scene plays" (hintbook.txt:5486-5487). No frame shows it (`I33_act3_frames.md:30`: "no purple glob").
  7. **The chase begins** — Belial chats, "sets some demons on Luther and runs away. Kill the demons… Attack the door to get through" (hintbook.txt:5488-5491). Which door of the three pairs is the curse door was not derived (`act3_tail_ids.md:13`).

  ### B3. EXACT vs APPROXIMATE
  **EXACT (mechanics):** click-Dawn sequence to the curse line before any cast works; level-5 ancient cast is the *only* accepted trigger (`accepts_level` pins 5, `l19_dawn_curse.gd:40-41`); the glob entering the mother gates the birth scene and the demon spawn; the ruby offer must actually grant definition 69 (item in — currently blocked); the demons must be really killable and their death gates the exit door; order and persistence over save/reload. The mother herself is **not** killed — attacking her only returns fireballs (hintbook.txt:5483-5484); that no-kill rule is itself EXACT.
  **APPROXIMATE (presentation):** the purple glob visual, the birth movie playback mechanism, the fireball return, Dawn's vanish, the demon wave composition ("demons" stay UNKNOWN natively, `act3_tail_ids.md:13`).

  ### B4. What `l19_dawn_curse.gd` records vs shows
  File: `~/opus_work/lol2_act3/scripts/lol2/l19_dawn_curse.gd` (140 lines), attached on both L19_BC and L20_BB (`act2_map.gd:218,220`).
  - Records: three E-clicks on Dawn's position on L19 — second sets `curse_said` + the book sentence as `line` (lines 117-129, constant at 21); third sets `ruby_offered` but **`grants_ruby()` returns `false`** (lines 43-44). On L20, E near the mother position with a casting-capable form and `cast_level == 5` sets `glob_entered` (lines 131-140). **`demons_killed` is forced false everywhere** (lines 60, 87, 127, 138); `DEMONS := -1`, `DOOR := -1` (lines 27-28); `plays_movie()` / `relocates_player()` return `false` (lines 46-50); `IN_MOVIE_TABLE := false` (line 25). All positions are invisible constants (`DAWN_AT`, `ACTOR_AT`, `MOTHER_AT`, lines 29-31).
  - Shows: only two hint labels — "E — keep clicking Dawn. The curse line is not a stored cstring." (line 105) and "E — ancient-magic level 5. placenta.vqa stays unplayed." (line 107). No Dawn, no mother, no glob, no demons, no movie.
  - Tests: `tests/l19_dawn_curse_test.gd`, `tests/l19_dawn_curse_earned_test.gd` (earned walk from `res://tmp/l19_ghostly_heads_earned_save.json`, carries the key onto L20_BB, X01 NOTES:5). The journal hint row already exists (`act3_journal_hints.gd:11`).

  ### B5. Native records and movie files, and presence in the project
  | Item | Evidence | In project? |
  |---|---|---|
  | Prop 78 "Dawn good" (2802, 882), region 1461; actor 39 DAWNL19 (1939, 891), region 2182 | `act3_tail_ids.md:12` | **Yes, as data**: `act2_populations/L19_BC.json` actor 39, def 0, health 1000, `present: false`; sprites `act2_creatures/L19_BC/sprites.json` def 0 "DAWNL19" (idle 41, walk 10, rise 12, death 64, corpse 1; `peaceful_adapter: true`) |
  | Ruby of truth: definition 69, identity 4227368151 (0xFBF884D7), handler 101 | `act3_tail_ids.md:12`; constants at `l19_dawn_curse.gd:15-17` | Identity recorded; grant not wired (`grants_ruby()` false) |
  | Prop 242 "Frank's Placenta" (-1160, 4258), region 262 — the mother beast host; template "Belial Birthed" has **zero placements** | `act3_tail_ids.md:13` | Record only; no visual on the map today |
  | `placenta.vqa` (the "Belial's birth" scene, hintbook.txt:5487), name-matched to prop 242, stored on L20 at file offset 5066703 | `act3_tail_ids.md:13`, `I23_finale_movies.md:17,19` | **No** — no `.vqa` files exist in the project; **not in `movie_table.json`** (`l19_dawn_curse.gd:25`); no generated `.ogv` |
  | `curse.vqa` — movie table index 15 | `scripts/lol2/movie_table.json:116-120` | Name present in the table; no extracted media |
  | Demons / door after the birth | `act3_tail_ids.md:13` | UNKNOWN natively; candidate hosts exist in the L20 population (defs 11/14 HIVEGRD, 13 IMP_BEL, all with native sprites) |
  | Playback idiom | `scripts/lol2/l13_belial_movie.gd` (CanvasLayer + VideoStreamPlayer + generated `.ogv`) | Present and proven (K32 §5) |
  | Demon-kill host | `act2_creatures.gd` live on L20_BB (`act2_map.gd:137`) | **Yes** — same kill pipeline as Beat A |

  ### B6. Smallest faithful plan — the demon kills can be hosted; the mother must NOT die
  1. **Show Dawn**: spawn actor 39 (DAWNL19) through `act2_creatures` as a peaceful interaction owner — the admitted-village-guard pattern already exists (`act2_creatures.gd:63-66`, DEVIATIONS0251). The click-to-talk sequence (curse line at click 2, offer at 3) is already exact in the state machine; keep it.
  2. **Really grant the ruby**: wire the third click to definition 69 / identity 4227368151 through the existing inventory/handler path (handler 101 recorded); flip `grants_ruby()` and relax `validate()`. This is an EXACT item-in.
  3. **The mother room**: place a mother-beast visual at prop 242's position (region 262). No native sprite exists (Belial Birthed has zero placements), so this is a logged adapter — the green organic chamber plus a large placed mass matches frames g_00365/g_00375/g_00372. Attacks on it return a fireball adapter (`dawn_projectile_world.gd`) and never a kill — that refusal is the book's rule.
  4. **The cast and the glob**: accept only ancient-magic level 5 (already pinned); launch a purple projectile adapter from Luther into the mother and set `glob_entered`. Then the birth: preferred — decode the MOVIES.MIX key for `placenta.vqa` and play it via the proven `l13_belial_movie.gd` pattern; until then, a logged adapter beat (never presented as decoded), as in the K32 plan.
  5. **The demons and the door — real kills, existing system**: spawn a small hostile wave from the L20 population's own native defs (HIVEGRD/IMP_BEL sprites already extracted) via `act2_creatures`; their deaths through the standard `receive_damage` → death-clip pipeline set `demons_killed=true`, which gates the exit door record (opcode-1 door pairs). No new combat code is needed anywhere in this beat.
  6. **Prove like a player**: extend `l19_dawn_curse_earned_test.gd` — earned walk clicks Dawn to the ruby (verify the item lands in inventory), casts at level 5 at the mother, watches the glob/birth beat, kills the demons for real, forces the door; captures vs. `g_00378`/`g_00379` (Dawn) and the green-chamber frames; owner playtest.

  ---

  No files were modified; this is groundwork only.

