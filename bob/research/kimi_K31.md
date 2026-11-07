# Kimi K31 — r17 player-visible changes (0ae8f39..act3-chain HEAD), 2026-11-07

Lead: IMPORTANT correction to the lead's own claim 'the Act 3 chain runs to the finale': the earned TESTS chain one save from the greenhouse to the finale, but many Act 3 beats are record-only (flags set, nothing visible): no movies (hw01, placenta, ending), no Faux Draracle kill, no final-fight resolution or ending sequence, sewer form shortcuts unplaced, beast wall empty, NE lift does not carry Luther. Act 3 in r17 = a walkable SKELETON, not a playable story. WHATS_NEW_r17 must say so. Next main-chain work: make each record-only beat real (backlog ACT3-PLAYABLE-*).

I have everything I need. Here is the report.

  # LoL2 player-visible changes — `0ae8f39..HEAD` (branch act3-chain)

  Range start: `0ae8f39` (2026-11-06). Sources: `git log`/`git show --stat`, `docs/DEVIATIONS.md` rows dated 2026-11-05..2026-11-07, and `~/AI_COMMS/playtest_feedback_20261023/TRIAGE_20261106.md`. "Adapter" below means the ledger row says adapter — the original game logic was not decoded; the behavior is a host-side stand-in.

  ## (a) Fixes for the owner's r16 playtest

  - **Drowning clock no longer resets when you jump in deep water** — the 15-second drowning clock keeps running while you're airborne inside the water, and a blue-green veil now rises up the screen as you drown (both editions, also the Cave river). Commits `2cb652c` (jump clock) and `deeb9f9` (veil; adapter). Test: `tests/liquid_drowning_test.gd` (covers both the clock and the veil overlay).
  - **The first temple visit registers just by walking up to it** — no more E prompt; the priest scene notice still shows. Without this, the village stayed closed even after recovering Daniel's blade (adapter; the snatch movie is not stored, so no movie plays). Commit `728f353`. Test: `tests/l8_temple_earned_test.gd`.
  - **Jungle streams no longer show see-through gaps** — water surfaces and side skirts are drawn at the two r16 stream spots so the backdrop doesn't show through (draw-only; no collision added; adapter). Commit `9f617e0`. Test: `tests/jungle_water_gap_test.gd`.
  - **The "see the temple first" journal note now says where the temple is** — east of the entry, far side of the map, village stays closed until you've been there. Commit `35eb774`. Test: `tests/l8_village_hints_test.gd`.

  Not fixed from the triage: the L14 Huline Temple clipping (owner-parked for the Sol/Fable lane); mid-river drowning itself needed no action (owner retracted).

  ## (b) Maps

  All six of these are ledger rows marked **draft / status pending** — owner confirmation outstanding.

  - **The L8 cache ladder works** — E at the ladder moves you up to the cache (adapter; the creak sound stays unplayed). Commit `d740198`. Test: `tests/l8_cache_ladder_test.gd`.
  - **The L8 tree bridge works** — E knocks the tree down and the fallen log becomes a walkable bridge (adapter). Commits `d740198`, `7e8c326` (tree/log became scripted solids; test-only follow). Tests: `tests/l8_tree_bridge_test.gd`, `tests/l8_map_test.gd`, `tests/l8_preview_test.gd`, `tests/darker_jungle_tunnel_arch_test.gd`.
  - **Spark can now reach the five torches on the L8 raised platform** — the stair collision was moved off the spark ray's mask (adapter). Commit `d740198`. Test: `tests/l8_platform_test.gd`.
  - **Crouching works in the Museum** — hold C as Human to use a low capsule (standing height unchanged; adapter, the book prints no crouch height). Commit `d740198`. Test: `tests/museum_crouch_test.gd`.
  - **The Museum niche switch now pays out** — after clicking the wall switch, one melee strike on the prop awards a magic level, and ceiling dust quads lie flat (adapter). Commit `d740198`. Test: `tests/museum_niche_dust_test.gd`.
  - **The L14 temple hall opening is blacked out and re-clipped** like the longplay shows (adapter; the spider burrow and quill passage stay unread at this spot, and the wider temple clipping is parked). Commit `d740198` (+ test-only fix `4a32849`). Test: `tests/l14_hall_clear_test.gd`.
  - **The L14 quill passage opens** after the two lamps take a spark (decoded opcode 196 words; passage sound stays unplayed). Commit `d712610`. Test: `tests/l14_temple_passages_test.gd`.
  - **Spider burrow strike is recorded** — but flag: the floor quads do not move and the passage stays on the hanging wall; a player cannot pass through here yet. Commit `d712610`. Test: `tests/l14_temple_passages_test.gd`.

  ## (c) Atlas and My Journal

  - **The Atlas (M key) now draws storeys** — current storey solid green, next storey faint, PgUp/PgDn step between storeys, and the atlas no longer pauses the game. Commit `d712610`. Test: `tests/atlas_storey_draw_test.gd`. Note: the storey *grouping* tool (`tools/lol2/atlas_explored.py`) has no renderer by itself; the drawing above is the visible part.
  - **The Atlas tracks where you've been** — explored regions are remembered per area and drawn on the map; saved as their own save field, with old saves migrating cleanly. Commits `d712610`, `cfba754`, `381b841` (save/load int fix). Test: `tests/atlas_explored_test.gd`.
  - **Atlas sub-area sections** — on L9, L10, L14 and L16 a Section control steps through "Floor / Inside N" depth layers. Commit `d712610`. Test: `tests/atlas_sections_test.gd`.
  - **Six new My Journal notes for Act 3 trouble spots** (dry fountain, cavern exit, Belial's horn, sewer crossing, ghostly heads, the curse). Commit `5568f40`. Tests: `tests/act3_journal_hints_test.gd`, `tests/my_journal_test.gd`. The matching Act 1/Act 2 findability checks add **no** new notes (registry only): `tests/act1_findable_test.gd`, `tests/act2_findable_test.gd`.

  ## (d) Act 3 story (L16 → L17 → L19 → L20)

  Everything in this group is an **adapter** per the ledger, and the whole chain is still marked draft. The earned tests chain saves from the greenhouse to the finale, but several beats are record-only — flagged individually.

  **L16 towers** (`809f0b9`, `dff6763`, `b405411`, `50f689d`, `ae4b231`; chain `cf66b63`; test-only fix `856789c`)
  - NE tower: enter through the opened FireWall doors after the greenhouse. Flag: the tower lift does not carry you (decoded target is "not the player"); Tower Hole/box/yellow figure have no placements. Tests: `tests/l16_ne_tower_test.gd`, `tests/l16_ne_tower_earned_test.gd`.
  - SE oil fountain: burn the oil and the **Dark Bow** appears and can be taken (item accounting in `67d28fb`, `tests/act2_item_case.gd`). Flag: the drain is not hosted; no earned route reaches the fountain (the test places you there). Tests: `tests/l16_se_oil_test.gd`, `tests/l16_se_oil_earned_test.gd`.
  - NW traps: break the three trap props — melee, the blue bow (kept), or a spark of charge 3+. Flag: the book's break is a summoned imp / pyrapod fireball; those don't exist in the cast table, so the spark-3 adapter stands (`5767404`, BC02). Tests: `tests/l16_nw_traps_test.gd`, `tests/l16_nw_traps_earned_test.gd`.
  - Ivory pedestals: place four ivory chips to set the SW flag. Flag: force field, gargoyle walk, ice fountain and ceiling drop stay off. Tests: `tests/l16_sw_chips_test.gd`, `tests/l16_sw_chips_earned_test.gd`.
  - Centre tower: reachable via the S01 lip. Flag: Mantle Gate is unbound and the actor behind the bars has no fight hosted — nothing to do there yet. Tests: `tests/l16_centre_tower_test.gd`, `tests/l16_centre_tower_earned_test.gd`.

  **L16 dragon room → L17** (`52b5580`, chain `3494602`, telepad fix `5767404` BC01)
  - Chop the dragon prop, then **walk onto the telepad** (no E) to travel to L17. Tests: `tests/l16_dragon_room_test.gd`, `tests/l16_dragon_room_earned_test.gd`.

  **L17** (`42dab82`, `6d43c4f`; handoff `260840f`; order fix `62f890a`)
  - Cavern run: the level-change exits to L19 and back to L16 work off the progression host. Tests: `tests/l17_cavern_run_test.gd`, `tests/l17_cavern_run_earned_test.gd`.
  - West-wall blade: E with a weapon equipped cuts the wall open. Flag: the scene movie (`hw01.vqa`) is named but not played. Tests: `tests/l17_beast_blade_test.gd`, `tests/l17_beast_blade_earned_test.gd`.

  **L19** (`72970af`, `8459347`, `8b133c8`, `0016f72`, `66c222c`, `d082277`; handoff `2475c0e`; finale doors `7cffb8b`)
  - Beast wall: flag — nothing visible happens here yet: no strand/frond rows placed, no beast movie stored or played, Luther is not moved. Tests: `tests/l19_beast_wall_test.gd`, `tests/l19_beast_wall_earned_test.gd`.
  - **Belial's Horn**: E at the prop grants the horn, and it is now a proper held, saved hand item (before, the finale save was refused with "Invalid equipment"). Flag: the grant is not tied to Baccata's death (no death flag). Tests: `tests/l19_belial_horn_test.gd`, `tests/l19_belial_horn_earned_test.gd`, `tests/l20_finale_earned_test.gd`.
  - Sewer forms: the three switches record in Human form. Flag: the Human bar-break and the Lizard gutter are **not** placed — the form shortcuts the book describes don't exist yet. Tests: `tests/l19_sewer_forms_test.gd`, `tests/l19_sewer_forms_earned_test.gd`.
  - **Clicking the Golden Doors now opens them** (book 5442) — before, they stayed shut and the earned walk fell through the door box (Kimi K30). Flag: the drain flag exists but is not required; rapids unmapped. Tests: `tests/l19_drain_path_test.gd`, `tests/l19_drain_path_earned_test.gd`.
  - Ghostly heads: E records the four heads with a casting form. Flag: demon body, white circle and red fountain are unset; the Ancients' Stone grant stays on L20. Tests: `tests/l19_ghostly_heads_test.gd`, `tests/l19_ghostly_heads_earned_test.gd`.
  - Dawn and the mother: E gives the curse line, then the ruby offer; the level-5 curse on the mother records. Flag: the offered item is not granted and `placenta.vqa` is unplayed. Tests: `tests/l19_dawn_curse_test.gd`, `tests/l19_dawn_curse_earned_test.gd`. The earned walk continues to L20 (`2475c0e`).

  **L20** (`60d62a8`, `f886aaf`, `0f28758`, `a8401d5`, `7cffb8b`)
  - Fire pillars and Scotia: E records pillar strikes and a level-5 Trinity. Flag: the shot does not open a path, "blue" is unset, and two actors stay off the fight. Tests: `tests/l20_pillars_scotia_test.gd`, `tests/l20_pillars_scotia_earned_test.gd`.
  - Armory: E hacks the westernmost block with a weapon. Flag: brick, white ball and fire ball are unset; pillars don't stop. Tests: `tests/l20_armory_test.gd`, `tests/l20_armory_earned_test.gd`.
  - Faux Draracle: strike, then the three keys record in order. Flag: "killed" stays false — he cannot actually be killed — and no speech is stored. Tests: `tests/l20_faux_draracle_test.gd`, `tests/l20_faux_draracle_earned_test.gd`.
  - **Finale**: the last fight starts when you hold the blue bow, the Dark Sword, or Belial's Horn — the horn now survives saving. Flag: the chasm is unset, no slump, **no ending movie plays and nothing is filed after the last scene** — the game has no visible ending sequence yet. Tests: `tests/l20_finale_test.gd`, `tests/l20_finale_earned_test.gd`.

  ## (e) Other

  - **L9 statue alcove opens on walk-in** (STORY-024) — entering the courtyard alcove starts the scene without E; with the Emperor's remains the bowl view pauses the world, without them you get "Huh?" once per visit (adapter). Commit `e8ba81f`. Test: `tests/l9_alcove_walkin_earned_test.gd`.
  - **Cave Fire Pit giant roach record** — actor 44 pinned at the native pit coordinate; the roach population is live in the Cave. Commit `d712610`. Test: `tests/cave_firepit_roach_state_test.gd`.
  - **Hive Shalla record — not player-visible**: the control-75 record is stored but never spawned and its groups never run; a player cannot see Shalla. Commit `d712610`. Test: `tests/hive_shalla_state_test.gd`.
  - **Codex data and generator — not player-visible**: `tools/lol2/build_codex.py` and `data/lol2/codex.json` exist, but no game script reads `codex.json`; only the coverage test loads it. Commits `d712610`, `a04c73a`. Test: `tests/codex_coverage_test.gd`.
  - **L8 ladder/tree sounds decoded — not audible**: `creaky2.aud` identified but playback stays off. Commit `d712610`. Test: `tests/l8_opcode_followup_test.gd`.

  Not player-visible (no behavior change): ledger bookkeeping `4d3db38`, `77a2a7f`, `e21eb43`; test/registry-only commits `4aa13e8`, `856789c`, `a04c73a`, `4a32849`, `e138d1a`, `7e8c326`.

