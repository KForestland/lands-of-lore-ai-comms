# Kimi K34 — BF01-BF07 (Act 3 playable) review (read-only, 2026-11-07)

Lead: apply after fix-ups (grok list BG). Must fix: (1) render DEVIATIONS.md after the 14 new pieces; BF03 mother: OWNER says she DIES after birthing Belial (patch keeps her alive) + gate the boxes to L20 only + the area's monsters gone afterwards; (3) BF06 beast-wall step must be tied to the beast-wall arrival, not any first L19 entry; (4) BF01 ending beats paced in seconds, a chasm prop, a game_finished flag + end screen. Low items 5-9 = refinement later (logged adapters).

# K34 review — ACT3P BF01..BF07 vs K31/K32/K33 + hintbook, base 373b5d7 (act3-chain, clean tree)

  Method note: per instructions I ran no `git apply`; apply-ability was judged by reading every hunk's context lines against the base files at 373b5d7. All context lines matched verbatim, and the per-patch file sets are disjoint (verified below), so order BF01→BF07 is safe.

  ## BF01_ending (K32 brief — ACT3-PLAYABLE-ENDING)

  | check | result | evidence |
  |---|---|---|
  | Shows the contract / honest adapter | PASS (minimal) | Book 5557-5576 (one blow, any of 3 weapons → chasm, vow "never to return", slump, Luther+Dawn video, Draracle drops in and vanishes, "that's the game") is rendered as an auto-advancing caption card ending on "The game is finished."; e224e.vqa honestly logged absent (`SCENE_NAME := "ending-adapter"`, row d00). No in-world chasm prop though — K32's suggested minimum was a prop/decal chasm + Belial figure. |
  | Earned test proves visible result | PASS w/ caveat | `tests/l20_finale_earned_test.gd` starts from the faux-draracle earned save, real E press with the carried chain weapon, waits frames, asserts the "The game is finished." card + `finished()` state, save/reload keeps it. Caveat: teleports to `AT_75` (pre-existing idiom), and the intermediate captions are never asserted visible (they last ~1 frame each, see problem list). |
  | Applies on 373b5d7 | YES | All contexts match `scripts/lol2/l20_finale.gd` and both test files (verified lines 4-6, 42-44, 68, 82-113 of the script; lines 85-109 of the earned test). |
  | Ledger as pieces | PASS format / FAIL workflow | New `0317-row-2026-11-07-d00-...` one-row piece, 5 cells, correct convention — but the rendered `docs/DEVIATIONS.md` is not regenerated (see Problem 1). |
  | Typed calls / PASS / registry | PASS | New `finished()` is static; `stage` typed `Label`; PASS lines updated; no new test files → registry json (name/suite/mode/order only) needs no change. |

  ## BF02_faux_draracle (K33 Beat A)

  | check | result | evidence |
  |---|---|---|
  | Shows the contract / honest adapter | PASS w/ caveat | Real kill now: E in Human form with any weapon → `killed=true`, body box hides, keys 0-1-2 gate on the kill, door leaf rises, "Belial begins to speak." card at actor 75 — matches book 5535-5546. Caveat: not the K33 plan (no `act2_creatures` spawn, no native 28-frame death clip) — a plain BoxMesh; honestly logged in row d01 ("the visible body is the module's own mesh", "opcode 1 was not entered, so the leaf is an adapter"). One E = one-hit kill; Beast/Lizard refused — "fight him any way you please" is narrower than the book. |
  | Earned test proves visible result | PASS | Starts from armory earned save; keeps negative checks (Beast form, empty hand, key-2-before-0); asserts `FauxBody` hidden, `SPEECH` line, leaf risen, `belial_seen` card; save/reload keeps kill+room+leaf. Teleports between spots (pre-existing idiom). |
  | Applies on 373b5d7 | YES | Contexts match base `l20_faux_draracle.gd` (incl. `static func moves_doors` → instance conversion) and both tests. No outside callers of the converted `moves_doors`/`stops_pillars`-style statics (grep-verified). |
  | Ledger as pieces | PASS format / FAIL workflow | Row d01 one-line piece; DEVIATIONS.md not rebuilt (Problem 1). |
  | Typed calls / PASS / registry | PASS | `_box` returns typed `MeshInstance3D`; tests use `as Label`/`as MeshInstance3D`; PASS lines updated. |

  ## BF03_mother (K33 Beat B) — the mother-alive check

  | check | result | evidence |
  |---|---|---|
  | Mother stays alive, demons are the kills | PASS | `mother_body.visible = true` unconditionally in `_show()`; the killable entity is a separate `DemonWave` box hidden by `demons_killed`; birth door opens on demon kill. A bad form/level cast shows "The mother shoots a fireball back. She does not die." — the book's no-kill rule (5483-5484) is honored and there is no code path that kills the mother. Matches the K33 lead correction exactly. |
  | Shows the contract / honest adapter | PASS w/ caveats | Ruby genuinely granted: new catalog row (definition 69, identity 4227368151, handler 101, icon `069.png` exists) through the existing `act2_items` packet + `Items.sync()` path; survives save and the L19→L20 handoff (test-asserted). placenta.vqa honestly logged as not in `movie_table.json`; birth shown as a card. Caveats: glob and fireball return are caption-text only (no projectile), the "demon fight" is a second E press (no creature wave as K33 planned), and the player is never prompted for that second E. All logged in row d02. |
  | Earned test proves visible result | PASS w/ caveat | 3 real E clicks on Dawn → ruby in `carried_collected`; L19 save/reload; handoff to L20 keeps curse line, horn, ruby; level-5 E → glob card + `MotherBody` visible; second E → demons fall + door rises + mother visible; save keeps it. Negative checks (Beast form, level 4) retained — but they don't assert the new fireball caption appears. Teleports to `DAWN_AT`/`MOTHER_AT` (idiom). |
  | Applies on 373b5d7 | YES | Contexts match `act2_items_catalog.gd` row() horn/blue-bow adjacency, `l19_dawn_curse.gd` (incl. the `_cast_curse` reorder), and both tests. `Items.initial/sync/valid` and `death_stored()`-style host fields all exist at base. |
  | Ledger as pieces | PASS format / FAIL workflow | Row d02; Problem 1. |
  | Typed calls / PASS / registry | PASS | `codex_coverage_test` enumerates a hardcoded candidate list (horn not in it either) → unaffected; `item_definitions_test`'s 42 slot checks are Act-1 keyed → unaffected; `act2_item_case` counts placed rows only → unaffected. |

  ## BF04_pillars_armory (K31 flags: path shut, brick/ball/fireball unset, Scotia not a kill)

  | check | result | evidence |
  |---|---|---|
  | Shows the contract / honest adapter | PASS w/ caveat | Pillars: five fire shots + Trinity → `path_open`, leaf rises, `ScotiaBody` hidden — matches "level-five prism spell (Trinity) and away she goes" (5492-5511). Armory: one Human E on control 62 breaks props 195/196/197 and stops pillars. Caveat: the book (5522-5534) wants three distinct attacks (hack/shoot brick, pyrapod-spark or level-3 imp on the white ball, blue bow on the fireball) plus a timed return; the patch flattens to one blow. Trinity still has no cast-level enforcement (`TRINITY_LEVEL==5` is a constant, only form-gated). Rows d03/d04 honest. |
  | Earned test proves visible result | PASS | Starts from the pillars earned save; keeps ice-pillar/Beast-form negatives; asserts leaf height, Scotia hidden, sources hidden, `stops_pillars()`; save/reload keeps both. Teleport idiom. |
  | Applies on 373b5d7 | YES | Contexts match `l20_armory.gd`, `l20_pillars_scotia.gd`, all four tests. Static→instance conversions (`stops_pillars`, `opens_path`, `moves_pillars`) have no callers outside their own updated tests (grep-verified). |
  | Ledger as pieces | PASS format / FAIL workflow | Rows d03/d04; Problem 1. |
  | Typed calls / PASS / registry | PASS | `Array[MeshInstance3D]`, typed `_box`; PASS lines updated. |

  ## BF05_heads_sewer_horn (K31 flags: circle/fountain/demon unset; bar-break/gutter unplaced; horn grant untied to Baccata's death)

  | check | result | evidence |
  |---|---|---|
  | Shows the contract / honest adapter | PARTIAL | Horn: caption "Baccata is dead. The pipe yields Belial's Horn." ties the grant to the death narratively while honestly keeping `death_stored()` false (book 5410-5413). Heads: 4th shot drags a skull-token box onto a white-circle box by a red-fountain box (book 5460-5468) — but the book's demon spawn → demon kill → corpse drag → "a door opens" (route to Dawn) is skipped; DEMON/PLATE/FOUNTAIN/STONE stay -1 (logged). Sewer: Human-proximity bar-leaf raise + Lizard-proximity gutter mouth — book (5414-5427) says "attack the bars until they all break" (an action, not proximity); the guck-rise/dam payoff stays absent. Rows d05-d07 honest. |
  | Earned test proves visible result | PASS w/ caveat | All three start from the chained saves; assert token at `CIRCLE_AT`, bar leaf raised, gutter lowered, caption text, no death flag; saves keep state. Caveats: sewer bar/gutter visuals are proximity-driven and never enter `quest_state` (not saved, re-derived); the test doesn't check them after reload; horn test uses the pre-existing `death_stored()` (exists at base :31). |
  | Applies on 373b5d7 | YES | Contexts match all three scripts and five test files (verified incl. `_process`/`_unhandled_key_input` blocks). |
  | Ledger as pieces | PASS format / FAIL workflow | Rows d05-d07; Problem 1. |
  | Typed calls / PASS / registry | PASS | Statics kept static where tests call them so; PASS lines updated. |

  ## BF06_beast_wall_l17_movie (K31 flags: beast wall empty, hw01 named not played)

  | check | result | evidence |
  |---|---|---|
  | Shows the contract / honest adapter | PASS w/ caveat | Strand + frond meshes placed, beast scene as a card, and Luther now does get moved — book-true ("Watch Luther get sucked into the beast", 5383-5398). L17 cut shows the honest "hw01.vqa is not in the movie table" card. Reload does not re-move (move is inside the noted-flip branch). Caveat: the flip/teleport has no arrival gate — ANY first active L19 frame with `noted=false` yanks Luther to `STEP_AT` (84,22,80), ~225 units; only book-true for the beast-wall arrival. Rows d08/d09 honest. |
  | Earned test proves visible result | PASS | Chain-safe: starts from the blade earned save, real region-1312 → L19 arrival-1 level change; pose check (`ARRIVAL` (84,22,305)) runs before mouse capture so `world_active()` is false until `prepare()`+capture — the teleport then fires in the two awaited frames and the test asserts both distances. Verified against `player_starting_magic.gd:91,106` (mouse-capture gate). Downstream L19 saves all carry `noted=true`. |
  | Applies on 373b5d7 | YES | Contexts match `l17_beast_blade.gd`, `l19_beast_wall.gd`, both tests (incl. the kept `no BeastMovie node` check). |
  | Ledger as pieces | PASS format / FAIL workflow | Rows d08/d09; Problem 1. |
  | Typed calls / PASS / registry | PASS | PASS lines updated; statics unchanged. |

  ## BF07_l16_towers (K31 flags: NE lift doesn't carry, drain unhosted, SW field off, centre fight not hosted)

  | check | result | evidence |
  |---|---|---|
  | Shows the contract / honest adapter | PASS w/ caveat | NE: the lift now carries Luther once to `ARRIVAL` (16082,100,3886) — book-true transport (4842-4847, 5224-5236) but explicitly logged as "an adapter against that decode" (opcode 18 target u16 0 ≠ player). SE: drain mouth appears with the flame; doors 80/81/98 stay put (book's "path to the tower opens" via doors still unhosted, logged). SW: four-chips → field/gargoyle/ice-fountain/ceiling boxes show; pyramid stays whole, doors 89-91 shut (book's payoff is actually "the glass pyramid shatters… a fireball… opens the door" — the patch shows the side-quest set pieces instead; logged). Centre: Human E + weapon drops the actor-45 box and raises a Mantle Gate leaf; the book's "just walk into them → mantle of the ancients → immortal" payoff (5250-5268) is not shown. Rows d10-d13 honest. |
  | Earned test proves visible result | PASS w/ caveat | NE test keeps the real LIP walk then teleports to the door quad; asserts arrival at `ARRIVAL` and the honest hint line. SE/Centre earned tests assert drain/FoeBody/MantleGate visibility and save-keeping; centre adds the missing `key()` helper (parent chain `l12_logs…`→`l9_chapel…` defines none — convention is per-test helpers ✓). Caveat: the SW earned test proves the field by direct `quest_state` injection via `apply_place` then resets — not a player action; disclosed in row d12 (chain save holds no chip; no 4th L16 ivory placement exists). |
  | Applies on 373b5d7 | YES | Contexts match all four scripts and six test files; `state()` size-4 with optional `foe_down` and the 3-or-4 `validate()` keep old saves loading. |
  | Ledger as pieces | PASS format / FAIL workflow | Rows d10-d13; Problem 1. |
  | Typed calls / PASS / registry | PASS | All `new()` calls typed; PASS lines updated; no registry changes needed. |

  ## Problem list, by severity

  1. **High — the ledger is left stale; `deviations_ledger_test` goes red.** The patches add 14 row pieces (`0317-row-…-d00..d13`) but no patch includes the re-rendered `docs/DEVIATIONS.md`. The tool's own docstring says "create the piece and run build". At base, `python3 tools/build_deviations.py --check` is green ("matches docs/deviations/ (381 pieces)"); after applying BF01–BF07 it exits 1 (14 rendered rows missing from the committed file), failing the first check of `tests/deviations_ledger_test.gd`. Context: that test's second check (`rows == pieces`) appears already failing at base — 370 dated rows in DEVIATIONS.md vs 335 `-row-` pieces, because 35 rows live in non-`-row-` pieces like `0272-citadel-exit-lock.md` (the W16 "two lanes" naming). The patches can't fix that, but they do introduce the new --check failure. Fix: include the `build` output (the rendered DEVIATIONS.md diff) in one of the patches or a follow-up commit.
  2. **Medium — BF03 spawns the mother/demon/door boxes on L19 too.** `l19_dawn_curse.gd` attaches on both L19_BC and L20_BB (`act2_map.gd:218,220`); `_ready()` unconditionally builds `MotherBody`/`DemonWave`/`BirthDoor` at the L20 coordinate `MOTHER_AT` (-1160,-20,-4258) and `_show()` forces `mother_body.visible = true`, `demons.visible = true` until `demons_killed`. On the L19 instance these boxes sit at that coordinate in L19 space — if it's in-bounds there, players see a stray green/red/brown box. Not area-gated, not logged.
  3. **Medium — BF06's beast-wall step fires on any first L19 entry.** The noted-flip in `l19_beast_wall.gd::_process` has no proximity or arrival-selector check; the first frame `world_active()` is true with `noted=false` teleports Luther to `STEP_AT` (225 units). Correct for the beast-wall arrival (which is the earned chain's first L19 entry), wrong for any other first arrival route.
  4. **Medium — BF01's ending beats are sub-visible and the "game finished" is only a caption.** `_advance()` steps one beat per `_process` frame, so chasm→vow→slump→Dawn→Draracle→vanish flash past in ~5 frames; a player sees only the final card. There is no in-world chasm prop (K32's suggested minimum), no `game_finished` quest flag beyond the finale state, and no end screen/credits stub (K32 step 4); the frame-capture comparison vs `g_00389`/`g_00390` (K32 step 5) is also absent.
  5. **Low — BF02/BF03 combat is not the creature pipeline the K33 brief planned.** Faux Draracle = one Human-form E press on a box (one-hit kill; other forms refused, which the book doesn't say); demons = a second E press; no fireball/glob projectile (caption text only). All honestly logged as adapters, but weaker than the brief's `act2_creatures` route, and BF03's earned test doesn't assert the fireball caption on the refused casts.
  6. **Low — BF04 armory flattens the book's three distinct object attacks into one blow**, and drops the book's "the objects return" timer; the Trinity cast still isn't level-checked (`TRINITY_LEVEL` is a constant, not an enforcement).
  7. **Low — BF05 ghostly heads skips the demon spawn/kill/corpse-drag and the "a door opens" payoff** (the route to Dawn's elevator); the token teleports onto the circle on the 4th shot. Logged, but the beat's gate outcome stays unshown.
  8. **Low — BF05 sewer bars/gutter are proximity-triggered, unsaved, and never reset**: standing near the door as Human raises the leaf (book: "attack the bars until they all break"); the visuals aren't in `quest_state` and the leaf stays raised forever once shown; `stage.text` can go stale.
  9. **Low/systemic — the earned tests keep the teleport idiom and one stages state directly.** Every earned test starts from the previous beat's earned save (chain intact, no free E where the original needs none — form/level negatives are kept), but moves Luther with `player.position =` between spots; BF07's SW-chips test injects `quest_state` to show the field. The BF07 centre-foe fight also prefers the Dark Bow the chain may carry — fine — but none of this is a real walk-in-fight-out proof. These are disclosed in the ledger rows, so honesty is preserved; they are weaker than the K32/K33 "prove like a player … owner playtest" bar.

  Bottom line: all seven patches should apply cleanly in order on 373b5d7, are honestly logged as one-row pieces, keep types/PASS lines/registry consistent, and BF03 does keep the mother alive with the demons as the kills. The one suite-breaking defect is the un-rendered `docs/DEVIATIONS.md` (Problem 1); Problems 2-4 are real behavior risks worth a follow-up; the rest are logged simplifications.

