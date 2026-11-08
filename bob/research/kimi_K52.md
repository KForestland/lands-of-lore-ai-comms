# Kimi K52 — L14 Huline Temple chain + STORY-066 trace (prep for Fable BJ08)

Lead spot-check: l14_chamber_voices.gd exists with _travel at :116, attached in act2_map.gd, tmp/l16_arrival_earned_save.json exists — confirmed. STORY-066 is HOSTED (backlog 'todo' is stale).

## Entry to L14
- L8 temple door: `scripts/lol2/l8_temple_door.gd` (CanvasLayer at POINT Vector3(758,32,2046)), state in `l8_temple_door_state.gd`. Human form + world active, reach 170, facing 0.85. E: insert Dreamstone (definition 136, id `act2:L13_RC:dreamstone`) → slot occupied → must retrieve → `can_leave()` → "enter" calls `host.progression.use_exit("prop:1198")` (l8_temple_door.gd:20).
- `act2_progression.gd:479-482`: for L8_SJ prop:1198 with L8TempleDoor present, requires `can_leave()`, then `native.call("set_local",13,1)` — earned Kit receipt supplies the untraced predicate-136 writer (DEVIATIONS 2026-11-03 row "Earned Temple Dreamstone entrance", STORY-049).
- Native exit edge: act2_travel.json `L8_SJ:prop:1198` — kind 6, value 20, group 11612, raw `020100001c2e` → opcode 2 arm 0x1C, level 14, selector 1, grade PROVEN, position (758,0,2046). Predicate: entry index 136, trailer `04138800` (local 13 == 1).
- L14 arrival: act2_maps.json L14_HT selector 1 → native (2411, 2413), heading_units 1, region 864, floor 0 (LIKELY grade, Grok backlog5 item2).
- In L14, the same receipt opens main doors 92/93 immediately — `l14_temple_doors.gd` (owns movables 92/93; no native events → modern association, DEVIATIONS 401).
- Chain: BJ07 output `tmp/l8_river_return_qualified_save.json` → `tests/l8_temple_door_earned_test.gd` walks fixture `tests/fixtures/l8_temple_approach.json`, insert/retrieve/enter → writes `tmp/l14_temple_arrival_earned_save.json`. Qualified: `tmp/l14_temple_arrival_qualified_save.json`. Then `tests/l14_temple_entry_earned_test.gd` (interior entry) → `l14_temple_entry_earned_save.json`.

## L14 main chain table (STORY-049..066)
Order per hintbook ch.12 (lines 4345-4737 in hintbook.txt):

| # | STORY | Step | Host | Native vs adapter | Test / saves |
- 049: temple door, dreamstone in/out — l8_temple_door.gd + l14_temple_doors.gd — adapter join on native prop1198/group11612 PROVEN travel — l8_temple_door_earned_test.gd, l14_temple_entry_earned_test.gd; l14_temple_arrival/entry saves.
- 050: priest body to slab — l14_priest_body.gd (corpse prop274 → slab region 816) — modern carry/placement adapter — l14_priest_slab/supplies tests.
- 051: aloe west bowl (prop 370, item72/aloe 109), poison east bowl (prop 369, item68/poison 125), floor lowers (opcode 196 words), Spark body vanishes — l14_priest_ritual.gd — adapter (Kit + interpreted opcode196 + spark receiver) — l14_priest_ritual_earned_test.gd.
- 052: green shard from wooden post — l14_post_shard.gd (control71 Crystal Switch, group 16904 opcode 3 identity D0421BDE/def 105) — modern E pickup of source identity — l14_post_shard_earned_test.gd.
- 053: jungle tree torches/stairs/shard slot (out in L8, tree with raised platform) — l8_tree.gd / l8_tree_slot_state.gd — modern spark receivers + Kit slot; DEVIATIONS 405 — act2_temple_tree_earned_loop_test.gd; tmp/act2_temple_tree_loop_*.
- 054: left wall hanging + spider fight — l14_hanging.gd (control 124 at 2260,-3706) opens passage; spiders l14_spider_passage.gd (respawn 12s adapter 0286), l14_spider_burrow.gd (controls 80/81, draft/pending per DEVIATIONS 470) — adapters — l14_hanging_earned_test, l14_spider_earned_test.
- 055: flute from coffin in southern spider run — original flute77 in lower region 219; pickup via generic take; the lower corridor requires Lizard/Human form choice adapter l14_lower_passage.gd (DEVIATIONS 408) — l14_flute_earned_test.gd, l14_flute_approach; flute id act2:L14_HT item? Actually "Temple flute96" per deviation 421. l14_flute_slot accepts Temple flute96 or Hive flute.
- 056: nine stone cubes chokepoint — NOT hosted as a mechanism (Stone cube exists only as item def 59 in act2_items_source.json); book-optional step. Backlog marks done astra regardless.
- 057: corpse-table button, conveyor, red-goo box into second machine long-edge first, statue appears (catch) — l14_machines.gd (control75 body, machine3902, item65 statue) — l14_machines_earned_test.gd.
- 058: bedroom headboard push, Lizard crack behind red altar, two buttons in sequence, library exit button — l14_bedroom.gd + l14_library.gd (buttons 146/147/148, stairs) — l14_bedroom_approach/crack, l14_library tests.
- 059: statue into empty niche → second green shard — l14_niche.gd (item65 → niche126, yields item67) — l14_niche_earned_test.gd.
- 060: one shard per floating bowl (bowls 405/406) → passage opens — l14_shard_bowls.gd — l14_shard_bowls_earned_test.gd.
- 061: spiral staircase (Dreamstone slot 72!) + bridge to three doors; left=ledge maze idol 371 (l14_trials.gd), middle=tilt room buttons 142-145 idol 372 (l14_tilt.gd), right=fire paths buttons 60/61/62 + bridge 56/57 idol 384 (l14_fire_paths.gd). Note the spiral requires placing the Dreamstone in original slot 72 and taking it back (l14_spiral.gd, DEVIATIONS 417). Tests: l14_spiral, l14_ledge_maze, l14_tilt, l14_fire_paths (+returns).
- 062: flute into angled oil slot (movable 76), oil covers 77/78 translate; blade trap bypass — l14_flute_slot.gd + l14_trap_route.gd (boulder, doors 80/81) — l14_flute_slot, l14_blade_bypass, l14_boulder_side tests.
- 063: three idols on pedestals (cases 85/86/87) → opening — l14_idol_pedestals.gd — l14_idol_room/idol_pedestals tests.
- 064: kill five hoppers (ids 91-95), corpses on wooden platform, step on — l14_hopper_platform.gd — l14_hopper_room/corpses/platform tests.
- 065: faux-Belial as Beast — l14_belial.gd: F descend on weighted elevator (hopper platform complete), E talk, G form choice requires Dreamstone carried; permits_hit reflects non-melee and refuses non-Beast — adapter 0305 — l14_belial_entry/combat/exit/return_entry tests.
- 066: CHV — see next section.

## STORY-066 status
Hosted. `scripts/lol2/l14_chamber_voices.gd` (attached act2_map.gd:235). Original CHV room30 assets: assets/lol2/generated/l14_chamber_voices/ (background.png, voices.ogv, city.ogv, cue_2_28.wav — all present).
- Door: E at doors (688,40,10873)/(638,40,10752) after Belial (actor 90) dead — adapter because door groups 17622/17640 predicate 207 (control +0x25) writer untraced.
- Voices movie plays; click chalice hotspot (194,88,396,218 on 640x400) or E offers Dreamstone (carried or held); consumed from carried_collected; cue 2:28; CITY movie (city resurfaces) plays; then `_travel()`: native set_local(22,1) (go_to_level_16) + fire prop:170 kind 6 caller 0x14 → native group 9210 predicate 50 → opcode 2 arm 0x1C → L16 arrival 1 (act2_travel.json edge L14_HT:prop:170, PROVEN, position 1080,0,11330).
- The level change: act2_progression reads globals 0x223C8/0x223CC → level 16 selector 1; scene change to L16_CA with meta lol2_map_start_selector.
- Missing/adapters (DEVIATIONS 2026-11-04 row 444): door predicate 207 writer untraced → Belial-death gate is adapter; CHV callback hosting presentation-level; refusal cues 2:107/2:112 not joined (text line "The voices wait for the Dreamstone."); dreamstone may be carried not just held; save-after-offer re-runs travel from the door.
- Tests: tests/l14_chamber_voices_earned_test.gd — full earned walk from tmp/l14_belial_combat_qualified_save.json: walk to doors, real E, refusal without stone, Esc leave/reopen, real click offers, CITY, native level change request 16/1, real scene change to L16_CA, arrival check at (-3860, -1341 Godot), Dreamstone gone, writes tmp/l14_chamber_voices_earned_save.json + tmp/l16_arrival_earned_save.json.
- Gap: no qualified save for chamber_voices or l16 arrival (only earned), so the hinge isn't re-qualified; also backlog STORY-066 row still says 'todo' — stale; hosting exists since 2026-11-04.

## L16 arrival
- Selector 1 (from prop170 edge): native (-3860, 1341), heading_units 1, region 137, floor 0 (act2_maps.json L16_CA arrivals; DEVIATIONS 247: preview start moved here, pinned by l16_map_test.gd).
- Godot position x=-3860, z=-1341; test asserts within 2.0.
- tmp/l16_arrival_earned_save.json exists (Dreamstone absent from inventory — destroyed).
- Next step STORY-067 already hosted: l16_arrival_elevator.gd + tests/l16_arrival_elevator_earned_test.gd (region 233 group 564 movie 27 ELEVATOR.VQA, opcode 18 relocation to (-3797,-2291)) — reads tmp/l16_arrival_earned_save.json.

## Likely first stops for BJ08
1. Input save: tmp/l14_temple_arrival_earned_save.json (BJ07 output via l8_temple_door_earned_test) — verify it exists/current; qualified variant l14_temple_arrival_qualified_save.json.
2. Walk order matches qualified save chain: temple_entry → priest_slab/supplies → priest_ritual → post_shard → (L8 tree loop already earned: act2_temple_tree_loop_qualified_save) → hanging → spider → flute (form-choice lower corridor) → machines → bedroom → library → niche → shard_bowls → spiral (Dreamstone slot 72!) → trials (ledge/tilt/fire) → flute_slot → blade/boulder bypass → idol pedestals → hopper corpses/platform → belial entry/combat (Beast, Dreamstone must be carried for the G form choice) → chamber_voices → l16 arrival.
3. Watch points: Dreamstone retention — spiral slot 72 takes and returns the stone; Belial G-form requires it carried; CHV consumes it — an owner walk that leaves the stone in a slot breaks 065/066. Spider respawn adapter (12s). l14_spider_burrow is draft/pending (DEVIATIONS 470) and hall_clear draft (466), quill draft (469) — optional side content. STORY-056 cubes not hosted (optional). CHV door reach (130u, dot 0.7) at two door points; the city movie then auto-travels — no player input needed after offer. No qualified save past belial_exit — the CHV + L16 arrival leg is the least re-qualified stretch, so it's the likely first real stop.

Also mention: branch r19-work confirmed, tests extend l12_logs_approach_earned_test.gd walk helper.

Format: keep table readable. Write final answer now.

• Research complete. Here is the BJ08 preparation brief (read-only; branch confirmed `r19-work` at c611100).

## Entry to L14

- **Door host**: `scripts/lol2/l8_temple_door.gd` (CanvasLayer at native (758,32,2046)) with `l8_temple_door_state.gd`. Human form + active world, reach 170 / facing 0.85. E cycles: insert Dreamstone (definition 136, instance `act2:L13_RC:dreamstone`) → slot occupied → **retrieve it back** → `can_leave()` → `interact("enter")` calls `host.progression.use_exit("prop:1198")` (`l8_temple_door.gd:20`).
- **Predicate supply**: `act2_progression.gd:479-482` — for L8_SJ `prop:1198` the earned Kit receipt runs `native.call("set_local",13,1)`, supplying the untraced predicate-136 writer (DEVIATIONS row 2026-11-03 "Earned Temple Dreamstone entrance", STORY-049).
- **Native edge**: `act2_travel.json` `L8_SJ:prop:1198` — kind 6 value 20, group 11612, `020100001c2e` = opcode 2 arm 0x1C → **level 14, selector 1, grade PROVEN**, predicate entry index 136 (`04138800` = local13==1).
- **L14 arrival**: `act2_maps.json` L14_HT selector 1 → native (2411, 2413), heading_units 1, region 864, floor 0 (LIKELY, Grok backlog5 item2). The same receipt then opens main doors 92/93 immediately — `l14_temple_doors.gd` owns movables 92/93 (no native events; modern association, DEVIATIONS 401).
- **Test/save chain**: `tests/l8_temple_door_earned_test.gd` reads BJ07's `tmp/l8_river_return_qualified_save.json` (SHA-pinned), walks `tests/fixtures/l8_temple_approach.json`, refuses remote/wrong-item/paused/full inserts, then insert→retrieve→enter → writes **`tmp/l14_temple_arrival_earned_save.json`** (qualified twin `l14_temple_arrival_qualified_save.json` exists). `tests/l14_temple_entry_earned_test.gd` continues into the interior.

## L14 main chain

Ordered per hintbook ch.12 (`hintbook.txt:4345-4735`, Prima p.129-141) and the STORY cards; all hosts attach in `act2_map.gd:219-244`.

| STORY | Step (book) | Host file | Native vs adapter | Earned test / saves (tmp/) |
|---|---|---|---|---|
| 049 | Dreamstone into door, take back, enter | `l8_temple_door.gd:16-27`, `l14_temple_doors.gd` | Native PROVEN travel group 11612; slot/door joins modern | `l8_temple_door_earned_test.gd`, `l14_temple_entry_earned_test.gd`; `l14_temple_arrival_*`, `l14_temple_entry_*` |
| 050 | Dead priest onto stone rectangle | `l14_priest_body.gd` (corpse prop274 → slab region 816) | Modern carry/placement; native drag UNKNOWN | `l14_priest_slab_earned_test.gd`, `l14_priest_supplies_earned_test.gd` |
| 051 | Aloe west bowl (prop370), poison east (prop369), floor descends, Spark body | `l14_priest_ritual.gd` (bowls 369/370, 23 opcode-196 floor words) | Original identities/floor targets; Kit + motion + spark adapter | `l14_priest_ritual_earned_test.gd`; `l14_priest_ritual_*` |
| 052 | Green shard from wooden post | `l14_post_shard.gd` (control71 "Crystal Switch", group 16904 → def 105) | Source identity, modern E pickup | `l14_post_shard_earned_test.gd` |
| 053 | Jungle tree: spark torches, stairs rise, shard in slot, retrieve | `l8_tree.gd` + `l8_tree_slot_state.gd` (torch props 1338-1342, control66) | Modern spark receivers/Kit; DEVIATIONS 405 | `act2_temple_tree_earned_loop_test.gd`; `act2_temple_tree_loop_*` (this save feeds the hanging test) |
| 054 | Left wall hanging → spider fight | `l14_hanging.gd` (control 124), spiders `l14_spider_passage.gd` (12s respawn adapter 0286), `l14_spider_burrow.gd` (**draft/pending**, DEVIATIONS 470) | Adapters | `l14_hanging_earned_test.gd`, `l14_spider_earned_test.gd` |
| 055 | Flute from coffin (southern spider run) | original flute77, lower region 219; form-choice adapter `l14_lower_passage.gd` (Lizard crawl, DEVIATIONS 408) | Adapter for the short seam | `l14_flute_earned_test.gd`, `l14_flute_approach_earned_test.gd`; `l14_flute_*` |
| 056 | (Optional) nine stone cubes at chokepoint | **not hosted** — Stone cube is only item def 59 in `act2_items_source.json` | — | none (book-optional) |
| 057 | Corpse-table button, conveyor, red-goo box long-edge first, catch statue | `l14_machines.gd` (control75 body → machine3902 → `act2:L14_HT:item65`) | Adapter | `l14_machines_earned_test.gd` |
| 058 | Bedroom headboard, Lizard crack behind red altar, two buttons in sequence, library exit | `l14_bedroom.gd` + `l14_library.gd` (buttons 146/147/148) | Adapters | `l14_bedroom_approach/crack_earned_test.gd`, `l14_library_earned_test.gd`, `l14_library_exit_earned_test.gd` |
| 059 | Statue into empty niche → second green shard | `l14_niche.gd` (item65 → niche126 → item67) | Adapter | `l14_niche_earned_test.gd` |
| 060 | One shard per floating bowl → passage | `l14_shard_bowls.gd` (bowls 405/406) | Adapter | `l14_shard_bowls_earned_test.gd` |
| 061 | Spiral stairs + bridge; three trials: ledge maze / tilt room / fire paths, one idol each | `l14_spiral.gd` (**Dreamstone slot 72** at (606,40,-3464)), `l14_trials.gd` (doors 88/89/90, idol 371), `l14_tilt.gd` (buttons 142-145, idol 372), `l14_fire_paths.gd` (buttons 60-62, bridge 56/57, idol 384) | Adapters over original floors/buttons; DEVIATIONS 417-420 | `l14_spiral_`, `l14_ledge_maze_`, `l14_tilt_`, `l14_fire_paths_` + return tests |
| 062 | Flute into angled oil slot; blade/boulder bypass | `l14_flute_slot.gd` (movable 76, covers 77/78; Temple flute96 or Hive flute), `l14_trap_route.gd` (doors 80/81, boulder) | Adapter; DEVIATIONS 421 | `l14_flute_slot_`, `l14_blade_bypass_`, `l14_boulder_side_earned_test.gd` |
| 063 | Three idols on three pedestals | `l14_idol_pedestals.gd` (cases 85/86/87) | Adapter | `l14_idol_room_`, `l14_idol_pedestals_earned_test.gd` |
| 064 | Kill 5 hoppers, corpses on platform, step on | `l14_hopper_platform.gd` (ids 91-95, weighted lift) | Adapter | `l14_hopper_room_`, `l14_hopper_corpses_`, `l14_hopper_platform_earned_test.gd` |
| 065 | Faux-Belial, Beast form only | `l14_belial.gd` — F descends the lift, E talk, G form choice **requires the Dreamstone carried** (`l14_belial.gd:63`); `permits_hit` reflects ranged and refuses non-Beast melee | Adapter 0305 | `l14_belial_entry/combat/exit/return_entry_earned_test.gd` |

## STORY-066 status

**Hosted** (despite the backlog's stale `todo`) — `scripts/lol2/l14_chamber_voices.gd`, attached at `act2_map.gd:235`; DEVIATIONS row 2026-11-04 (line 444). Media assets all present in `assets/lol2/generated/l14_chamber_voices/` (`background.png`, `voices.ogv`, `city.ogv`, `cue_2_28.wav`).

- **CHV room**: original room30 hosted as a paused 640x400 room — background frame 30, the voices movie, golden-chalice hotspot0 (194,88,396,218). Door: E at (688,40,10873)/(638,40,10752), gated on Belial (actor 90) dead.
- **Dreamstone destroyed**: `offer()` (`l14_chamber_voices.gd:93-105`) erases the stone (carried or held) from `carried_collected`, sets `l14_chamber_voices.offered`, plays cue 2:28 + the **CITY movie** (the resurface), then `_travel()`.
- **Level change**: `_travel()` (`:116-120`) runs native `set_local(22,1)` (`go_to_level_16`) and fires prop170's kind-6 record with caller 0x14 → native **group 9210, predicate 50** → opcode 2 arm 0x1C → **L16 arrival 1** (edge `L14_HT:prop:170` in `act2_travel.json`, PROVEN, pos (1080,0,11330)). `act2_progression` reads globals 0x223C8/0x223CC and does the real scene change (meta `lol2_map_start_selector`).
- **Missing/adapters**: door groups 17622/17640 need control +0x25==1 (predicate 207) — writer untraced, so Belial's death gates the door (adapter); CHV callback hosting (slots 0x8c/0x6c/0x44) is presentation-level; refusal cues 2:107/2:112 not joined (text line instead); stone may be carried, not only held; a save after the offer re-runs travel from the door.
- **Test**: `tests/l14_chamber_voices_earned_test.gd` — from `tmp/l14_belial_combat_qualified_save.json`: physical walk to the doors, real E, refusal keeps the stone, Esc leave/reopen, real chalice click consumes it, CITY, native request {level 16, selector 1}, real scene change, arrival assert, then writes `tmp/l14_chamber_voices_earned_save.json` and **`tmp/l16_arrival_earned_save.json`** (both exist on disk).
- **Gap**: no *qualified* save for CHV or the L16 arrival — the hinge exists only as earned outputs, and the backlog row was never flipped to done.

## L16 arrival

- Selector **1** from the prop170 edge: native **(-3860, 1341), heading_units 1, region 137, floor 0** (`act2_maps.json` L16_CA arrivals; Godot (−3860, z=−1341); DEVIATIONS 2026-10-31 row moved the preview start here, pinned by `tests/l16_map_test.gd`). The CHV test asserts the player lands within 2.0 units and that the Dreamstone stays gone across the change.
- The next step is already hosted: **STORY-067** arrival elevator — `scripts/lol2/l16_arrival_elevator.gd`, `tests/l16_arrival_elevator_earned_test.gd` reads `tmp/l16_arrival_earned_save.json` (trigger plate control 78 → doorway panels → region 233 group 564 movie 27 ELEVATOR.VQA → opcode 18 relocation to (−3797,−2291)).

## Likely first stops for BJ08

1. **Input**: `tmp/l14_temple_arrival_earned_save.json` (BJ07's hand-off via `l8_temple_door_earned_test`); re-run that test if the save predates the r19 merge. The walk order is exactly the qualified-save relay: temple_entry → priest_slab/supplies → priest_ritual → post_shard → (L8 tree loop, `act2_temple_tree_loop_qualified_save`) → hanging → spider → flute (Lizard lower corridor) → machines → bedroom/crack → library → niche → shard_bowls → spiral → ledge/tilt/fire trials → flute_slot → blade/boulder bypass → idol pedestals → hopper corpses/platform → belial entry/combat → chamber_voices → l16 arrival.
2. **Dreamstone custody is the fragile thread**: the spiral slot 72 takes the stone and must be retrieved (`l14_spiral.gd`, committed-but-retrievable); Belial's G form-choice refuses without it carried; CHV destroys it. An owner-like walk that parks the stone in a slot breaks 065→066 — this is the most likely first real stop.
3. **Least re-qualified leg**: everything up to `l14_belial_exit_qualified_save.json` has qualified saves; the CHV → L16 hop exists only as earned saves, so expect the first finding there (CHV door reach is 130 units / dot 0.7 at two door points; after the offer, travel is automatic — no further input).
4. **Known rough edges to walk past, not fix first**: `l14_spider_burrow.gd` and `l14_hall_clear.gd` are draft/pending (DEVIATIONS 466/470), the quill passage is draft (469), spider respawn is a 12s modern adapter, and STORY-056 (stone cubes) is unhosted but book-optional.

