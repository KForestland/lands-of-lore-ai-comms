## Discovered ids of a host's carried item_effects (all areas share player_item_controller.state()).
static func notes(host: Object) -> Array:
	var controller = host.get("item_effects") if host != null else null
	if controller == null or not is_instance_valid(controller) or not controller.has_method("state"): return []
	var journal = controller.state().get("journal", [])
	return journal if journal is Array else []

## Records a note the first time its moment is reached. Returns true only for a new note.
static func discover(host: Object, id: String) -> bool:
	if not hints().has(id):
		push_error("Unknown journal note: " + id)
		return false
	var controller = host.get("item_effects") if host != null else null
	if controller == null or not is_instance_valid(controller) or not controller.has_method("state"): return false
	var effects: Dictionary = controller.state()
	var journal: Array = effects.get("journal", [])
	if id in journal: return false
	journal.append(id)
	effects.journal = journal
	if host.has_method("save_feedback"): host.save_feedback(NOTICE)
	return true

===
43:func _process(delta: float) -> void:
45:	if elapsed < 1.0: return
All major claims verified. A few remaining details to check quickly:

1. l8_village_hints.gd poll once a second — `_process` with elapsed < 1.0 return ✓ (approximately once a second).
2. l16 hourglass leaf row: "aimed reach 130" ✓ (aimed(HOURGLASS,130.0)), plate reach 150 ✓. But the row says "aimed reach 130, facing dot > 0.9" ✓ (line 61: >0.9 shared).
3. l16_one_tower row: "Door movables 92, 93, 94 have no coordinates here" ✓ (DOORS := [92,93,94], no coords). "The fireball strikes..." line ✓ (line 96). opened set true — check line ~95. BALL_END ✓.
4. Character counts of hints — the spec claims chars counts (109, 92, etc.). I could verify quickly with python. That's part of the claim "each count below was rechecked on that string alone". Let me verify counts.
5. Also "l9_statue has no KEY const" — confirmed (no KEY const in l9_statue.gd; uses string). ✓
6. Also dry fountain prop 210 — spec says no host invented; just a statement, nothing to verify really. Could grep prop 210 existence but spec explicitly says out of list. Skip.
7. Also verify initial()/validate() claims: l13_exit_lock has `stone` field — check l13_exit_lock_state.gd for unlocked/stone and "gives the stone back" ("Take the Dreamstone back." / "You take back the Dreamstone." ✓ in interact lines). l8_temple_door same. Definition 136 ✓ both.
8. l14_shard_bowls hint: "E — Place green shard in suspended bowl" vs spec "E — Place green shard" — prefix match; note.
9. Character counts — run python.

Let me verify char counts and a couple last things.

• All structural claims verified. Last check: the claimed character counts of the hint strings.l10_tomb_oil 109 109 OK
l10_emperor_door 92 92 OK
l9_statue_human 97 97 OK
l9_flood_late 118 118 OK
l10_trees_need_dawn 107 107 OK
l8_not_initiated 111 111 OK
l13_citadel_sealed 112 112 OK
l13_dreamstone 106 106 OK
l14_scale_bowls 100 100 OK
l14_boulder_side 87 87 OK
l14_hopper_platform 94 94 OK
l14_chalice 94 94 OK
l16_hourglass_leaf 74 74 OK
l16_one_tower 100 100 OK


• All char counts verified. Compile the report table.

• Verification complete. Every check was run directly against `~/opus_work/lol2_act3/scripts/lol2` (read-only; no files created or edited).

| claim | found? | note |
| --- | --- | --- |
| All 20 module files exist (l10_oil … l8_village_hints) | yes | All present in `scripts/lol2` |
| Proposed 14 ids are new; not in any JOURNAL_HINTS | yes | No match anywhere in `.gd` files — but see note on `l14_hopper_platform` below |
| `my_journal.gd` `SOURCES` + `discover` rejects unknown ids | yes | `my_journal.gd:7` SOURCES list; `discover` push_errors "Unknown journal note" and returns false for ids not in `hints()` (`my_journal.gd:47-50`) |
| `l8_village_hints.gd`: NEAR 420, 1-second poll, `MyJournal.discover` call, 4 do-not-reuse ids present | yes | `NEAR := 420.0` (line 7); `_process` gates on `elapsed < 1.0` (line 45); ids `l8_blade_for_daniel` etc. all in its JOURNAL_HINTS (lines 9–12); `enhanced_guard` string matches verbatim |
| l10_tomb_oil: KEY `l10_oil` `{"version":1,"burned":false}`, AIM `(-1443,12,-3307)`, 240 radius, `ignite(level)` levels 1/3/5, BLAST_DAMAGE 20, barrel `phase==2` = switch true & distance 1426 | yes | `l10_oil.gd:4-7,110-114`; barrel phase/distance contract in `l10_barrel.gd:15-22` (d≤1426, phase 2 requires switch and d==1426). No close-range refuse branch — matches "Oil, unmerged" note |
| l10_emperor_door: `l10_priest.urn_given`, AIM `(3396,70,-3010)`, 140 / 0.8 reach, `speak`/`exchange_ashes`; SLAB_AIM `(3207,45,-2321)` same reach, `L10EmperorEntry.offer` | yes | `l10_priest.gd:5,8,17,32-33,37,67`; `l10_emperor_entry.gd:4,17,63-67` |
| Ankh slots `emperor:slab66` / `priest:ashes`, `Ankh.committed`, item `act2:L10_DC:priest_ankh` | yes | `l10_ankh_state.gd:7-8,12`; item id in `act2_items_catalog.gd:55` and referenced in `act_one_quest_state.gd:255` |
| l9_statue_human: no KEY const (string `l9_statue`), walk key `l9_statue_walk`, alcove polygon 4 pts + `abs(y-32)<15`, `enter` refuses "Enter the courtyard alcove as Human.", `begin_fight` false while `player_form != 0`, fields `arrived`/`fight_done` | yes | `l9_statue.gd:5,16-20,34-35`; `l9_statue_walk.gd:13,21,65-66`. Polygon coords match verbatim |
| l9_flood_late: state via `l9_flood_state.gd`, enabled only when `l9_statue_walk.fight_done`, `dead` at `breath >= 15` (river_drowning_state LIMIT), hook `set_health(0)` + "You drowned. F9 loads your earned save.", no grate node | yes | `l9_flood.gd:11,44-45`; `l9_flood_state.gd:3,21-22`; `river_drowning_state.gd:5`. No "grate" in l9_flood.gd. Source control 82 at (2804,10762) height 530 confirmed in `docs/l9-flood-source.md:7` |
| l10_trees_need_dawn: KEY `l10_silverleaf` `grown`, `dead_bracers_item.available` (definition 59), `revisit` refuse line, remains polygon + y∈[-30,0], aim `(3205,-8,-1285)` | yes | `l10_silverleaf.gd:3,10,30-33`; `dead_bracers_item.gd:10-11`; polygon/aim in `l10_emperor.gd:7,54` ("remains" entry) |
| l8_not_initiated: KEY `l8_tribe` `phase == "idle"` (phases idle/intro/fight/complete/departed), `l8_journey.admitted`, `l10_silverleaf.grown`, offer def 117, village `(676,32,-4541)` + `native_translation`, REACH 160, both refuse strings | yes | `l8_tribe_state.gd:4,10,13,26,37-39`; `l8_tribe.gd:20-22`; `l8_journey.gd:6-7` (TARGETS), `REACH := 160.0` (line 6) |
| l13_citadel_sealed: KEY `l13_egg_door` `opened`, AIM `(-3254,43.5,5330)`, spark sphere radius 24, `light(level)` levels 1 & 3 only, form 0, no walk radius | yes | `l13_egg_door.gd:3-4,18,38,40-41` |
| l13_dreamstone: `l13_exit_lock` + `l8_temple_door`, `can_leave()` = unlocked & slot empty & `stone` carried, def 136, both give stone back, SLOT `(-3391,70,6670)` 170/0.85, temple POINT `(758,32,2046)`, `interact` hooks | yes | `l13_exit_lock.gd:4,29-30,38`; `l8_temple_door.gd:3,15,19` ("Use the Dreamstone and take it back first.") |
| l14_scale_bowls: KEY `l14_shard_bowls`, `complete` = slots "405"+"406" committed, bowls `(1176,48,-3307)` / `(1181,48,-3601)`, 145 / 0.9, shards `post_shard`/`item67`, `offer` hook | yes | `l14_shard_bowls.gd:2,5-6,16,55,59`. In-game hint is the longer "E — Place green shard in suspended bowl" (line 83) — spec's `E — Place green shard` is a prefix, fine |
| l14_boulder_side: KEY `l14_trap_route`, kill box `elapsed∈[0.75,1.5]`, `abs(x-29)<62`, `abs(z-1136)<55`, feet∈[130,180], `set_health(0)` + crush line, doors 81 `(-62,180,-413)` / 80 `(-51,180,580)`, 130 / 0.9, `open_door("80")` refuses "Follow the side passage." until 81 open | yes | `l14_trap_route.gd:2,4,38,45,56-57` |
| l14_hopper_platform: KEY, `complete` = slots "91"–"95" all committed, POINT `(41,310,5919)`, 145 / 0.86, `place` refuses both quoted strings | yes | `l14_hopper_platform.gd:2-4,16-19,70,81-84`. Note: proposed journal id `l14_hopper_platform` is textually identical to the existing quest key `KEY="l14_hopper_platform"` — distinct namespaces (journal id vs quest key), but worth flagging |
| l14_chalice: KEY `l14_chamber_voices`, `offered` only saved flag, `inside` not saved, doors `(688,40,10873)` / `(638,40,10752)`, 130 / 0.7, actor "90" health ≤ 0, dreamstone `act2:L13_RC:dreamstone` / def 136, `open_room`/`offer` hooks | yes | `l14_chamber_voices.gd:8,10-11,21,24,26,54,60,63-66,70,93` |
| l16_hourglass_leaf: KEY `l16_greenhouse` `silverleaf == ""`, `use_hourglass` chimes when leaf empty or `fireball > 0`, HOURGLASS `(2293,75,-1070)` reach 130 dot 0.9, PLATE `(2287,34,-593)` reach 150, def 117 | yes | `l16_greenhouse.gd:12-14,24,61,64-66,80-83,103-110` |
| l16_one_tower: `opened == true`, fireball line "The fireball strikes the tower doors and they open.", BALL_END `(2290,18,-2951)`, door movables 92/93/94 with no coordinates | yes | `l16_greenhouse.gd:16,18,96`; DOORS is a bare id array, no coords |
| `stuck_id` sample shape (oil test referencing `l10_oil.burned` + `l10_barrel.phase`) | yes | Field names match `l10_oil.gd`/`l10_barrel.gd` initial()/validate() exactly |
| All 14 claimed hint character counts | yes | Rechecked by script: every row matches exactly (74–118 chars) |

Summary: All 14 paste rows and every named anchor, constant, quest-state key, field, function, and quoted string in the spec were verified present in the codebase with matching values; nothing in the stuck-test table is contradicted by the source. Two minor caveats only: the proposed id `l14_hopper_platform` collides textually with the existing quest key of the same name (harmless but confusing), and the shard-bowl in-game hint reads "E — Place green shard in suspended bowl" where the spec quotes the shorter prefix.

