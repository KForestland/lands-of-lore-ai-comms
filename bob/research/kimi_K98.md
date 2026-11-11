• Let me start by reading the plan and the K95 audit.This is a substantial audit task. I need to verify the plan's claims against the code at ~/opus_work/lol2_sol_playtest_starts. The plan anchors are on commit 742dcab, branch sol/foundation-whole-game-save-20261111. Let me check the git state there first, then verify K95's four gaps, then hunt for new gaps.

  Let me delegate the heavy verification to subagents in parallel, but first I should check the repo state myself. Actually, this is a large audit — lots of file reads. Let me plan:

  1. Verify git commit in the playtest tree (does it match 742dcab?).
  2. K95 gap A: source guard — check that plan rev2 commit 9 now names builders/serializers as must-stay-clean. Verify the named files/lines exist in code: mechanism_transaction.gd:72,104; l10_emperor_state.gd:67; l13_altar_state.gd:36; l13_dawn_release.gd:35; l10_silverleaf_harvest.gd:25; l10_priest.gd:53; l8_journey_state.gd:52,71; l8_herbalist.gd:32; serializers act2_map.gd:338, darker_jungle.gd:292, dragon_level.gd:175, act2_jungle_return.gd:49; area_world_items.gd:79; jungle_world_items.gd:53; act2_world_items.gd:89; walkthrough_save.gd:155-159; jungle_walkthrough.gd:504,592. Also verify the guard rules would actually not match these (e.g., do builders use .duplicate()?). Rule 2: "a local bound to a live store without .duplicate(" — check builders duplicate.

  3. K95 gap B: history modes — verify table 2.9 against code, especially the "always" vs "once" claims at the cited lines. That's ~24 sites. Also verify l16_fountain_ball sync-first order.

  4. K95 gap C: player_dragon_blood.gd:29 — verify it's a live-pack removal.

  5. K95 gap D: jungle_walkthrough.gd:504, 592 — verify they're dictionary-key erases, and :454 is the assignment.

  New gaps to hunt:
  - Grant sites in scripts/lol2 the plan doesn't list: grep for .append( / carried_collected / act2_items writes etc. K95 said no missed sites on da76748, but the plan anchors 742dcab — different commit. Need to check the actual tree at the current checkout.
  - Save/load double-grant paths: the whole-game save from Plans 1-3 — check slot file structure, whether native grant ids (act2:<AREA>:grant<N>) validate, whether restore path works. Also check "the catalog rule builds the row from the table whatever the action is" — that's future code, fine.
  - Inventory-full behaviour: capacity checks, hive ancient stone 23.
  - Wrong file or field names: verify sample of cited file:line anchors.
  - Acceptance tests that cannot fail: analyze commit 0 tests — e.g., "item_grant_census_test ... fails when a writer appears or disappears" — is that testable? The census fixture is pinned; a new writer appears → source scan finds it not in fixture → fail. OK. But "item_grant_history_spelling_test ... for each 'always' site that can be reached twice from a test ... if one exists" — could be vacuous. Also the commit-8 native test "press E again, still one copy" — fine.

  This is a lot of verification. Strategy: use the explore subagents in parallel for the heavy census verification, while I check the key anchors myself. Given context constraints, delegating makes sense. Let me launch a few explore agents:

  Agent 1: Verify K95 gap A closure — check guard-rule coverage: read the pure builders and serializers in the code tree, confirm whether they operate on duplicates (so rule 2's "without .duplicate(" would exempt them), and confirm file:line anchors. Also check for any live-store writers NOT in the plan's lists (the census completeness) — actually that's agent 2.

  Agent 2: Census completeness — grep scripts/lol2 for all mutations of carried_collected / carried_inventory / carried() / act2_items / pack-shaped aliases, and compare against the plan's lists (I'll give the lists). Find unlisted grant sites. Also check `set(`/`call(` dynamic writes.

  Agent 3: Table 2.9 verification — read the 24 sites and confirm guard/packet spelling and order claims; verify l16_fountain_ball sync-before-history; verify l19_belial_horn and l19_dawn_curse guarded.

  Agent 4: Save/load analysis — the whole-game save (Plan 3): find the slot file structure, save/load code paths (jungle_save.gd, museum_save.gd, walkthrough_save.gd, act2_items_catalog sync/restore), look for double-grant or lost-item paths across save/load: e.g., restore() rebuilds pack from packet — what happens to Act 1 items in an Act 2 host? Does sync filter out items not in catalog (risk: lost items)? Check act2_items_catalog.gd:107-118 and :116 combined limit. Also check jungle_walkthrough apply_save double-application, museum_walkthrough:183/204 cave transfer double-grant on reload.

  Also verify dragon blood and the two loaders (small — I can do myself).

  First, check the git state of the playtest tree.

• I'll start by checking the repo state of the code tree, then verify the K95 gaps and hunt for new ones.fde4d19 Add pinned Act 2 and Act 3 checkpoint starts to F2
5ac1bca Fix whole-game load rollback and staged-asset refusals
742dcab grok G4: walk the cemetery fixtures west of the OF9 wall
sol/c15-act23-starts-20261111
?? assets/lol2/dark_halls/
?? assets/lol2/doors/indices_478.png


• The tree is at fde4d19, two commits past 742dcab, on branch sol/c15-act23-starts-20261111, not the branch the plan names. Line numbers may have drifted. K95 audited da76748 (r19-work). So anchors may drift; the plan says function names are the stable key.

  Let me check quickly what changed between 742dcab and HEAD to see if it touches item files. tests/game_save_legacy_assets_test.gd              |  41 ++
 tests/game_save_missing_native_test.gd             |  38 ++
 tests/helpers/game_save_cases.gd                   |   9 +
 tests/playtest/map_case.gd                         |  89 ++++
 tests/playtest_checkpoint_adapter_test.gd          |  51 +++
 tests/playtest_map_starts_rendered_test.gd         |   3 +
 tests/playtest_map_starts_test.gd                  |   1 +
 tests/playtest_starts_test.gd                      |   8 +-
 tests/registry/game_save_apply_failure_test.json   |  17 +
 tests/registry/game_save_legacy_assets_test.json   |  17 +
 tests/registry/game_save_missing_native_test.json  |  17 +
 .../registry/playtest_checkpoint_adapter_test.json |  17 +
 .../playtest_map_starts_rendered_test.json         |  20 +
 tests/registry/playtest_map_starts_test.json       |  17 +
 tests/registry/playtest_starts_test.json           |  25 +-
 tools/prepare_playtest_starts.py                   |  19 +-
 tools/regression_source.py                         |   3 +-
 tools/test_prepare_playtest_starts.py              |  27 +-
 tools/validate_playtest_starts.gd                  |   2 +-
 31 files changed, 1094 insertions(+), 83 deletions(-)
 scripts/lol2/museum_interface.gd         |   1 +
 scripts/lol2/original_game_gate.gd       |  15 +-
 scripts/lol2/playtest_starts.gd          |  17 +-
 scripts/lol2/playtest_starts.json        | 466 ++++++++++++++++++++++++++++++-
 8 files changed, 589 insertions(+), 13 deletions(-)
fde4d19 Add pinned Act 2 and Act 3 checkpoint starts to F2
5ac1bca Fix whole-game load rollback and staged-asset refusals
Scripts/lol2 changed only in museum_interface.gd, original_game_gate.gd, playtest_starts — none of the item-grant files. But 5ac1bca "Fix whole-game load rollback and staged-asset refusals" — check whether it touches save files that matter (game_save?). Let me see the full diff file list for scripts. scripts/lol2/game_areas.gd               |  16 ++
 scripts/lol2/game_save.gd                |  23 +-
 scripts/lol2/game_session.gd             |  63 ++++-
 scripts/lol2/indexed_cave_wall_review.gd |   1 +
 scripts/lol2/museum_interface.gd         |   1 +
 scripts/lol2/original_game_gate.gd       |  15 +-
 scripts/lol2/playtest_starts.gd          |  17 +-
 scripts/lol2/playtest_starts.json        | 466 ++++++++++++++++++++++++++++++-
 8 files changed, 589 insertions(+), 13 deletions(-)
game_save.gd and game_session.gd changed since 742dcab — relevant to the save/load audit (whole-game save from Plans 1-3). Item-grant owner files are unchanged, so plan anchors on those should hold.

  Now let me dispatch parallel exploration. I'll do:

  1. My own quick checks: dragon blood, jungle_walkthrough loaders, act2_items_catalog, l16_fountain_ball (core K95 verifications).
  2. Agent A (explore, thorough): census completeness — find any grant/write site in scripts/lol2 not in the plan's lists. I'll pass the plan's full lists.
  3. Agent B (explore, thorough): verify table 2.9 guard/packet/order per site + the "cap:false" claims + refusal texts spot check.
  4. Agent C (explore, medium): save/load double-grant/lost-item paths — whole-game save in game_save.gd/game_session.gd (note the recent changes), apply_save paths in jungle/museum walkthroughs, act2 catalog sync/restore, cave→museum transfer, world-item histories. Look for: double-grant on load, lost items, inventory-full behavior at load (does restore enforce 64 and drop items?).

  Let me first do my own key reads in parallel.
func inventory_state() -> Dictionary:
	return {"item_effects":item_effect_checkpoint.duplicate(true),"collected":carried_collected.duplicate(), "equipped_item":equipped_item, "equipped_armor":equipped_armor,"health":health,"player_form":player_form,"curse":curse.snapshot()}

func apply_inventory_handoff(state: Variant) -> String:
	var error := Save.validate_inventory(state)
	if not error.is_empty(): return error
	error = preload("res://scripts/lol2/player_fighting_transport.gd").transport_error(state,quest_state)
	if not error.is_empty(): return error
	if state.has("museum_control181"): quest_state["museum_control181"] = state.museum_control181.duplicate(true)
	if state.has("magic"):
		quest_state.player_magic_reward_state = preload("res://scripts/lol2/player_magic_state.gd").restore(state.magic).checkpoint
	if state.has("fighting"): preload("res://scripts/lol2/player_fighting_transport.gd").merge(quest_state,state.fighting)
	item_effect_checkpoint=preload("res://scripts/lol2/player_item_state.gd").canonical(state.get("item_effects",preload("res://scripts/lol2/player_item_state.gd").initial()))
	carried_collected = state.collected.duplicate()
	if is_instance_valid(source_pickups): source_pickups.restore()
	if is_instance_valid(world_items): world_items.restore()
	if is_instance_valid(oil_fire): oil_fire.present()
	if is_instance_valid(river_dam): river_dam.present()
	if is_instance_valid(causeway): causeway.present()
	if is_instance_valid(plank_bridge): plank_bridge.restore()
	health = int(state.get("health",PlayerHealth.MAXIMUM))
	jump_requested = false
	player_form = int(state.get("player_form",0))
	curse.restore(state.get("curse",Curse.initial()))
	FormBody.apply(player,camera,player_form,false)
	equipped_item = state.equipped_item
	equipped_armor = state.equipped_armor
	if is_instance_valid(interface_hud): interface_hud.refresh_equipment()
	return ""

## Diagnostics record every outcome, including early refusals that show no message (docs/dev-diagnostics.md).
func quicksave(path: String = "") -> String:
	var error: String = preload("res://scripts/lol2/game_save.gd").quicksave(self) if path.is_empty() else _quicksave_unrecorded(path)
	return preload("res://scripts/lol2/dev_diagnostics.gd").record(self, "save", error)
func quickload(path: String = "") -> String:
	var error: String = preload("res://scripts/lol2/game_save.gd").quickload(self) if path.is_empty() else _quickload_unrecorded(path)
	return preload("res://scripts/lol2/dev_diagnostics.gd").record(self, "load", error)
func _quicksave_unrecorded(path: String = "") -> String:
	if path.is_empty(): path = area_save_path
	if get_tree().paused: return "Close the current overlay before saving."
	if flying: return "Return to walking mode before saving."
	return Save.write_save(path, area_snapshot(), area_save_format)

func area_snapshot() -> Dictionary:
	_sync_exit_checkpoint()
	var quests: Dictionary = preload("res://scripts/lol2/atlas_explored.gd").release(quest_state.duplicate(true))
	return {"format":area_save_format,"version":1,"inventory":inventory_state(),"quests":quests,
		"atlas_explored":preload("res://scripts/lol2/atlas_explored.gd").stored(self),
		"player":{"position":[player.position.x,player.position.y,player.position.z],
		"yaw":wrapf(player.rotation.y,-PI,PI),"pitch":camera.rotation.x}}

func _quickload_unrecorded(path: String = "") -> String:
	if path.is_empty(): path = area_save_path
	if get_tree().paused: return "Close the current overlay before loading."
	var result := Save.read_save(path,area_save_format)
	if not result.error.is_empty(): return result.error
	return apply_save(result.state)

func apply_save(state: Variant) -> String:
	var error := Save.validate(state,area_save_format)
	if not error.is_empty(): return error
	# Fighting transport is checked against the incoming quests by Save.validate.
	var inventory: Dictionary = state.inventory.duplicate(true)
	inventory.erase("fighting")
	apply_inventory_handoff(inventory)
	var packet: Dictionary = state
	var loaded: Dictionary = packet.get("quests",Save.Quests.initial()).duplicate(true)
	atlas_explored = preload("res://scripts/lol2/atlas_explored.gd").taken(packet, preload("res://scripts/lol2/atlas_explored.gd").area_of(self))
	quest_state = preload("res://scripts/lol2/atlas_explored.gd").release(loaded)
	preload("res://scripts/lol2/player_fighting_transport.gd").merge(quest_state,preload("res://scripts/lol2/player_fighting_transport.gd").pack(quest_state))
	if state.inventory.has("fighting"): preload("res://scripts/lol2/player_fighting_transport.gd").merge(quest_state,state.inventory.fighting)
	if quest_state.has("hive_ambush"): quest_state.hive_ambush = preload("res://scripts/lol2/hive_ambush_state.gd").canonical(quest_state.hive_ambush)
	if quest_state.has("hive_rune_population"): quest_state.hive_rune_population=preload("res://scripts/lol2/hive_rune_population_state.gd").canonical(quest_state.hive_rune_population)
	if quest_state.has("hive_return_population"): quest_state.hive_return_population = preload("res://scripts/lol2/hive_return_population_state.gd").canonical(quest_state.hive_return_population)
	if quest_state.has("hive_curse"): quest_state.hive_curse = preload("res://scripts/lol2/hive_curse_state.gd").canonical(quest_state.hive_curse)
	if quest_state.has("jungle_dino_population"): quest_state.jungle_dino_population = preload("res://scripts/lol2/jungle_dino_population_state.gd").canonical(quest_state.jungle_dino_population)
	if quest_state.has("player_magic_reward_state"): quest_state.player_magic_reward_state = preload("res://scripts/lol2/player_magic_state.gd").restore(quest_state.player_magic_reward_state).checkpoint
	if state.inventory.has("magic"): quest_state.player_magic_reward_state = preload("res://scripts/lol2/player_magic_state.gd").restore(state.inventory.magic).checkpoint
	set_development_mode(false)
	player.position = Vector3(state.player.position[0],state.player.position[1],state.player.position[2])
Gap C confirmed: `player_dragon_blood.gd:29` does `controller.carried().erase(id)` — live-pack removal. And plan rev2 has it in 2.7 and commit 10. Note: plan says line 29 — code shows line 29 `saved.spent.append(id);controller.carried().erase(id)`. Confirmed.

  Gap D: `apply_save` — in this checkout, apply_save is at a different line. Let me find lines: the sed showed lines 440-520. `apply_save` begins around line 497 or so. `inventory.erase("fighting")` confirmed — dictionary-key erase on duplicated packet. Plan says `:504` and `:592`. Line numbers drifted slightly. Let me get exact line numbers.

  Now let me check line numbers and then dispatch the subagents.jungle_walkthrough.gd:444:func apply_inventory_handoff(state: Variant) -> String:
jungle_walkthrough.gd:499:func apply_save(state: Variant) -> String:
jungle_walkthrough.gd:504:	inventory.erase("fighting")
jungle_walkthrough.gd:577:func apply_area_handoff(state: Variant) -> String:
jungle_walkthrough.gd:592:	inventory.erase("fighting")
jungle_walkthrough.gd:886:func _kityara_grant(identity: int) -> void:
cave_walkthrough.gd:803:func carried_items() -> Array:
		return host.carried_inventory.item_effects
	return host.item_effect_checkpoint
func carried() -> Array:
	if host.has_method("carried_items"): return host.carried_items()
	return host.carried_inventory.collected if host.get("carried_inventory")!=null else host.carried_collected
func equip_offhand(id: String) -> bool:
	if host.player_form != 0 or (id != "" and (not preload("res://scripts/lol2/player_equipment.gd").offhand(id) or id not in carried())): return false
	var previous: String = str(state().get("offhand", ""))
	last_equip_route = Handlers.route(Catalog.definition(id), 10) if not id.is_empty() else (Handlers.route(Catalog.definition(previous), 11) if not previous.is_empty() else {})
	if id.is_empty(): state().erase("offhand")
	else: state().offhand = id
	return true
const SERUM_REFUSAL := "The Amaranth Serum does nothing on its own. Keep it to mix with a Silverleaf."
func use(id: String) -> bool:
	if host.player_form!=0 or Catalog.use_kind(id) == "" or id not in carried(): return false
	if not is_instance_valid(host.inventory): return false
	last_route = Handlers.route(Catalog.definition(id), Handlers.mode_for_use_kind(Catalog.use_kind(id)))
	if int(last_route.get("handler", -1)) > 0 and not bool(last_route.get("hosted", false)):
		if host.has_method("save_feedback"): host.save_feedback(str(last_route.get("refusal", "")))
		return false
	var current:=state()
	if Catalog.use_kind(id)=="dragon_blood":return dragon_blood.place(id)
	# Poison Paint (definition 125, handler 10 mode 0x0C): one coat on the weapon, refused at nine (weapon_poison.gd).
	if Catalog.use_kind(id)=="poison_paint":
		if not is_instance_valid(host.starting_magic) or host.starting_magic.health() <= 0: return false
		if not preload("res://scripts/lol2/weapon_poison.gd").use(host,id): return false
		current.spent.append(id)
		return true
	# Sap (handler98) and Vels fruit (handler20) consume the held item. Fruit also clears player status +1B5 and
	# turns its indicator off; the port has no status model, so that cure has nothing to clear (docs/vels-fruit-use.md).
	if Catalog.use_kind(id) in ["ironwood_sap","vels_fruit","amaranth_serum"]:
23:func _ready() -> void:
27:func state() -> Dictionary:
32:func carried() -> Array:
35:func equip_offhand(id: String) -> bool:
43:func use(id: String) -> bool:
134:func crystal_charges(id: String) -> int:
136:func crystal_burnt(id: String) -> bool:
140:func recharge_crystal(id: String) -> bool:
146:func advance(delta: float) -> void:
165:func _process(delta: float) -> void: advance(delta)
166:func melee_damage(base: int) -> int:
170:func status() -> String:
K95 gaps C and D verified at the exact plan line anchors (jungle_walkthrough.gd:504, :592 erase "fighting"; player_dragon_blood.gd:29 erase through carried()). Plan rev2 moved both correctly. Note `carried()` is at line 32-34 here (plan says 33-34 — fine).

  Now dispatch parallel explore agents for the heavy work:

  Agent 1: Census completeness — find grant sites not in plan lists.
  Agent 2: Table 2.9 verification (24 sites guard/packet/order).
  Agent 3: Save/load double-grant/lost-item analysis + inventory-full behavior + whole-game save structure (game_save.gd, game_session.gd — note these changed after 742dcab).

  I'll write detailed prompts. Give each agent the plan path so they can read tables themselves.Excellent results. Now let me verify the most important claims myself where they drive the verdict, particularly:

  1. The sync_first discrepancy: l16_dry_fountain.gd:156-158 vs plan's claim "only l16_fountain_ball.gd:85-86 needs it" (plan line 332). Verify directly.
  2. player_item_controller.gd:68,75,96,105,113,124 — are these erases, contradicting 2.3 classification? Check.
  3. Museum save has checkpoint.collected, not inventory.collected — verify (museum_walkthrough.gd:921-926).
  4. act2_map.gd:338 filter claim.
  5. Commit 9 guard rule 2 vs jungle_harvest spent alias (minor).
  6. The commit-8 acceptance test concern: "press E again, still one copy" only proves same-row; fine.

  Also check plan line numbers for quoting: plan line 332 says sync_first only fountain ball. Plan line 341 (Save paragraph). Let me verify the key code spots quickly.func take(index: int) -> Dictionary:
	var nxt := apply_take(state(), index)
	if nxt == state() or nxt.taken == state().taken: return {"ok": false, "reason": "Nothing to take."}
	if host.carried_collected.size() >= 64: return {"ok": false, "reason": "Make room for the lichen."}
	var id := clump_id(index)
	host.quest_state[KEY] = nxt
	host.carried_collected.append(id)
	Items.sync(host)
	if not host.quest_state.act2_items.collected.has(id): host.quest_state.act2_items.collected.append(id)
	restore()
	return {"ok": true, "reason": "Black Lichen (%d taken)." % nxt.taken.size()}
----
func take(record: int) -> Dictionary:
	if record not in LICHEN or not state().broken or record in state().taken.map(func(v): return int(v)): return {"ok":false,"reason":"Nothing to take."}
	if host.carried_collected.size() >= 64: return {"ok":false,"reason":"Make room for the lichen."}
	var id := "act2:L16_CA:lichen%d" % record
	var s := state().duplicate(true); s.taken.append(record); host.quest_state[KEY] = s
	host.carried_collected.append(id); Items.sync(host)
	if not id in host.quest_state.act2_items.collected: host.quest_state.act2_items.collected.append(id)
	restore()
	return {"ok":true,"reason":"Black Lichen (%d taken)." % s.taken.size()}
		if id == preload("res://scripts/lol2/l8_shaman_trade.gd").SERUM:
			if host.has_method("save_feedback"): host.save_feedback(SERUM_REFUSAL)
			return false
		current.spent.append(id)
		carried().erase(id)
		return true
	# Dampen charm (definition72, handler27 0x979A8): consumes the held charm and sets player byte 0x23ABD bit0. No
	# native reader of that bit is established; modern adapter (lead-authorised): a pending curse warning is cancelled.
	if Catalog.use_kind(id) == "dampen_charm":
		if not is_instance_valid(host.starting_magic) or host.starting_magic.health() <= 0: return false
		current.spent.append(id)
		carried().erase(id)
		current.dampened = true
		current.ancient_charges = use.counter
		current.spent.append(id)
		carried().erase(id)
		return true
	if Catalog.use_kind(id) == "silverleaf":
		current.spent.append(id)
		if not host.has_method("carried_items"): carried().erase(id)
		host.starting_magic.commit(magic)
		current.spent.append(id)
		if not host.has_method("carried_items"): carried().erase(id)
		magic.player.mana = preload("res://scripts/lol2/mana_foil_effect.gd").apply(int(magic.player.mana),int(magic.player.maximum))
		# Cave retains harvest history; its inventory filters consumed IDs.
		if not host.has_method("carried_items"): carried().erase(id)
		return true
	var result:=Effects.use(current.champion,carried(),id,{"held":true,"gate_223d0":0,"action_flags":0,"caller_bit0":false,"gate_223d4":0})
	if result.has("error") or not result.applied: return false
	current.champion=result.state
	current.spent.append(id)
	if host.get("carried_inventory")!=null: host.carried_inventory.collected=result.inventory
	else: host.carried_collected=result.inventory
	return true
	save_feedback("Museum saved." if error.is_empty() else "Save failed: " + error)
	return error

func area_snapshot() -> Dictionary:
	var state := {"format": Save.FORMAT, "version": 1, "checkpoint": checkpoint_state(),
		"atlas_explored": preload("res://scripts/lol2/atlas_explored.gd").stored(self),
		"player": {"position": [player.position.x,player.position.y,player.position.z],
		"yaw": wrapf(player.rotation.y,-PI,PI), "pitch": camera.rotation.x}}
	return state

----
func inventory_state() -> Dictionary:
	preload("res://scripts/lol2/act2_items_catalog.gd").sync(self)
	var result := super.inventory_state()
	result.collected = result.collected.filter(func(id): return not preload("res://scripts/lol2/act2_items_catalog.gd").valid(id) or preload("res://scripts/lol2/act2_items_catalog.gd").legacy_equipment(id))
	return result

----
static func validate(state: Variant, format: String) -> String:
	var error := Legacy.validate(state, format)
	if not error.is_empty(): return error
	error = quests_error(state.quests)
	if not error.is_empty(): return error
	if state.inventory.collected.size() + state.quests.get("act2_items", {}).get("carried", []).size() > 64: return "Inventory exceeds capacity."
	if state.player.has("region"):
		# Optional (BK01 follow-up): the region the region-aware collision tracked for the body when the save was written.
All key claims verified directly:

  1. **sync_first discrepancy CONFIRMED**: `l16_dry_fountain.gd:156-158` — pack append, `Items.sync(host)`, then guarded history append. Identical pattern to fountain ball. Plan line 332 says "only `l16_fountain_ball.gd:85-86` needs it" and commit 2 (plan line 374) says "(`sync_first` for the fountain ball)" only. Since plan itself argues order doesn't change result (sync only rebuilds carried from pack — actually wait, does sync affect the history write? sync rebuilds packet.carried from pack; history appends to packet.collected. For the in-place sites, sync(host) mutates the live packet's carried field; then history appends to collected. If sync ran after history instead, end state is identical. So behaviour-equal, but the plan promises to keep each site's order ("the site keeps its order anyway") and commit 2 would migrate dry fountain with sync-after-history, changing operation order against its own rule. MINOR/MAJOR? It's an internal contradiction that a migrator would hit. Given the plan stakes correctness on "keep each site's order" (risk 3, line 426), I'd rate MAJOR-ish... actually it's a factual error in the plan that contradicts its own table; the resulting behaviour is provably equal. I'll call it MAJOR because the plan's migration instruction is wrong (fountain ball singled out, dry fountain would be migrated with the wrong option spelling relative to its promise), but honestly the end state is identical → MINOR to MAJOR. The instruction says grades: BLOCKER/MAJOR/MINOR. I'd say MAJOR since "only ... needs it" is factually wrong and commit 2 text omits dry fountain.

  2. **player_item_controller.gd:68,75,96,105,113,124 are erases** — confirmed: those lines are `carried().erase(id)`. Plan table 2.3 lists `player_item_controller.gd:68,75,96,105,113,124,130,131` as "use" — replace whole pack. Only :130-131 assign. The erase lines are live-pack removals through the accessor alias — the exact pattern the plan moved dragon_blood to 2.7 for, and commit 10 + guard rule 1 covers erases only via the 2.7 list. Since these six lines are inside a function listed in 2.3 (migrated in commit 5 with ItemGrants.commit for the :130-131 assignment), what happens to the erases? Commit 5 replaces the assignment with commit(); the erase lines remain until commit 10, but commit 10 covers "the 12 functions of 2.7 plus the removals listed under it" — player_item_controller.gd use's erases are NOT in 2.7 (2.7 has player_item_effects.gd:82, player_dragon_blood.gd:29, jungle_walkthrough.gd:750, etc.). So the six live-pack erase lines in player_item_controller.gd are in neither 2.7 nor commit 10's scope. Also guard rule 1 before commit 10 "reports, not fails" erases, and after commit 10 the guard enforces erases — but player_item_controller.gd use isn't in the allow-list and would still contain `carried().erase(id)` → commit 10 leaves the tree failing its own guard, or the erase enforcement can never be turned on. That's a real hole: MAJOR.

  Wait — but also note 2.7's `player_item_effects.gd:82` `use` — agent-0 said it duplicates. But the erase in controller is at :68 etc. Actually the controller use calls Effects.use at :124 which returns result.inventory, then :130-131 assigns. The erases at :68,75,96,105,113,124... let me recount: sed showed lines 64-76, 94-98, 104-106, 112-114, 123-132. Erases appear at :68 (`carried().erase(id)` after serum), :75 (dampen), :96, :105, :113 (silverleaf — conditional `if not host.has_method("carried_items"): carried().erase(id)`), :124? The last block: `var result:=Effects.use(...)` at :124 area, assignment at :130-131. Hmm the plan says :124,130,131. Line 124 might be `current.spent.append(id)` before assignment... whatever — the six erase lines confirmed by agent and my read.

  3. **Museum save field**: confirmed — `area_snapshot` at museum_walkthrough.gd:921-926 has `checkpoint`, no `inventory` key. Plan §3 Save paragraph (line 341) says "The pack is written where it is today (`inventory.collected` in each area's save...)" — wrong for Museum (checkpoint.collected) and Cave (no pack list; per-owner keys). The plan's own 2.4 even says the Cave has no store. MINOR factual error in the save paragraph — though the intent ("no new keys") holds. MINOR.

  4. **§1.2 combined-64 list incomplete**: act2_save.gd:25 confirmed (`if state.inventory.collected.size() + ...carried.size() > 64`). Plan line 40 lists only :116, act2_map.gd:324, darker_jungle.gd:274 — misses act2_save.gd:25, dragon_level.gd:161, act2_jungle_return.gd:37. MINOR.

  5. **Old-save test "equal field by field" issue**: restore() rebuilds pack as legacy + packet.carried, so live pack order changes across act2 save/load. The commit-9 test (plan line 397) says "the pack, packet and histories are equal field by field". If "pack" means the live pack on an act2 host with interleaved act1/act2 items, order is not preserved — test as specified would fail on a golden that has interleaved items... actually would it? The test loads old saves and compares pack, packet, histories to... what reference? "every save from commit 0 and the fifteen golden saves from Plan 3 load, and the pack, packet and histories are equal field by field" — equal to what? Presumably to the values recorded before migration (commit 0 pins). The order rearrangement is pre-existing behaviour, identical before and after F-08, so pinned-before vs after would match. Hmm — the agent's framing was that load→live pack order differs from save order, but for the migration test comparing before-F08 vs after-F08, both would rearrange identically. So this is weaker. But the load-time history migration (jungle_source_pickups restore writing quest_state, world-item restores migrating carried→history) means a load can mutate state; if the test compares post-load state against the save bytes, histories may gain entries — again pre-existing, equal before and after. So as a migration regression test it's fine as long as it compares like-for-like. The real risk: "equal field by field" is ambiguous; if they compare loaded pack against the save file's inventory.collected for act2 hosts, it fails even on unmodified code — the test as specified cannot pass, or must be quietly weakened. That is "an acceptance test that cannot fail / cannot pass" material. Actually the instruction asks for "acceptance tests that cannot fail". Let me look for those:

  - `item_grant_history_spelling_test` (plan line 369): "for each 'always' site that can be reached twice from a test (call the function again on a state where its own guard lets it through, if one exists)" — the "if one exists" escape hatch means if no harness can reach a site twice, that row silently tests nothing. The test can pass vacuously for rows where second-fire isn't reachable. MINOR/MAJOR? It's a test-design weakness the plan itself flags ("if one exists"). It cannot fail for those sites. I'd flag MINOR-MAJOR.

  - Commit 7 test (plan line 384): "with all rows 'log' a fired group changes nothing in the pack (same as today)" — fine, can fail.

  - Commit 8 test (line 386): "walk to the object, press E, the item is in the pack... save, reload, press E again, still one copy" — the agent noted this only proves the same-row case; a grant id duplicating a definition of a held placement id isn't tested. That's a coverage gap, MINOR.

  - Census test (line 367): "fails when a writer appears or disappears, so every later commit must update the fixture on purpose" — wait, that says the fixture must be updated when commits intentionally migrate writers... but migration doesn't remove writers from the source, it changes them to call ItemGrants. Actually after migration, e.g. l12_citadel.gd:25 no longer appends directly — it calls ItemGrants.grant. The census scan counts writers of the pack; after commit 2, those direct writes disappear from owner files. So the fixture must be updated per commit — the plan says that. OK.

  6. **Source guard rule 2 vs jungle_harvest spent alias**: jungle_harvest.gd:124-126 passes live `item_effects.state().spent` into jungle_harvest_state.gd which erases. If guard rule 3 ("a call that passes a live store... to a function not on the rule-function list") is scoped to the pack only, jungle_harvest.gd:125 is already listed in 2.2 as passing a packet with spent to the rule function jungle_harvest_state.gd:97 which IS on the rule-function list. OK fine. But rule 1's erase enforcement after commit 10: jungle_harvest_state.gd does `inventory.spent.erase(item)` — on a parameter, inside a listed rule function. Rule 1 matches direct writes where `carried_collected` etc. is followed by `.erase` — `inventory.spent.erase` doesn't match those names. Fine.

  But the bigger guard hole: **player_item_controller.gd erases** (point 2). Also `carried().erase(id)` matches guard rule 1 ("carried()" followed by .erase). After commit 10, guard enforces erases; player_item_controller.gd:68 etc. still contain them and the file is not allow-listed → tree red. Unless commit 10 is meant to migrate them — but commit 10 says "the 12 functions of 2.7 ... plus the removals listed under it". player_item_controller.gd:68-124 is not among them. So the plan's commit 10 leaves the guard failing, or forces unplanned edits. MAJOR.

  Also check: `player_item_controller.gd` `use` is in table 2.3 (way C) — migrated in commit 5: "player_item_controller.gd:130-131 (item use writes back a pack) is in this commit too". So commit 5 handles only the assignment. The erase lines linger. Under guard rule 1, before commit 10, erases are "reported, not failed" — fine; after commit 10 they fail. So commit 10 must include them but doesn't list them. Confirmed gap. MAJOR.

  7. **Misclassification `l9_pyre.gd:109,111` in 2.8 as loaders** — they're E-key dispatch calling urn() — actually is that a misclassification that matters? 2.8 lists "l9_pyre.gd:109,111 _unhandled_input" with Text=yes. It's listed under "Loaders and validators (not grants...)". The lines are an input handler that triggers urn (way C, listed in 2.3 as l9_pyre.gd:72,74). If the census fixture pins it as kind "loader", that's wrong kind but harmless? The allow-list of commit 9 includes "the loaders of 2.8" — l9_pyre.gd:109,111 presumably contains `urn("retrieve")` calls, not pack writes, so guard wouldn't match anyway. MINOR misclassification. Let me verify quickly.

  8. **`l8_herbalist.gd:32` description in 2.2** — 2.2 row says "appends to the `carried` it is given"; agent says :31 duplicates. Plan 2.3 note already lists l8_herbalist.gd:30-33 pick as a builder. And commit 9's must-stay-clean list (line 395) includes `l8_herbalist.gd:32`. But wait — commit 6 (line 382) migrates `l8_herbalist.gd:32`! If l8_herbalist pick is a pure builder that "stays as it is, for good" (line 195 says builders stay), then why does commit 6 migrate it? Let me check the code: is the caller l8_herbalist.gd itself the owner (interact calls pick and assigns)? Table 2.1 lists `l8_herbalist.gd:32 pick` with Cap=yes, History=yes. Table 2.3's builder note lists `l8_herbalist.gd:30-33 pick` as a builder. 2.2 lists `l8_herbalist.gd:32` as a caller that "appends to the carried it is given". Contradiction between 2.2 and 2.3/commit-9 list. And commit 6 migrates it — if it's a pure builder, commit 6 should only touch its caller (make the caller use ItemGrants.commit or grant). The plan is internally inconsistent here. Let me read l8_herbalist.gd.

  9. **area_world_items.gd:79 vs :81** line drift — trivial MINOR.

  10. **act2_world_items.gd:89 filter without legacy_equipment exclusion** — transient packet.carried contains legacy id until next sync. Plan commit 3 keeps it deliberately ("keeps its own packet.carried line"). Since it self-heals at next save (inventory_state calls sync), and validate tolerates... The plan keeps it as-is, fine — it's flagged behavior. Not a gap in the plan, though worth noting the plan doesn't mention the difference between the two spellings. MINOR.

  11. **Commit 8 / 3.1 native guard hole**: `native` refuses "when the base id is already in collected" — base id of the grant id is itself, so a grant row whose definition duplicates a held placement id (e.g. player already holds act2:L8_SJ:itemN of the same definition) would still grant. Plan's defense: the three evidence conditions (no hand-written owner gives the same item at the same place). But the condition is about owners at the same place, not about the same definition reachable elsewhere. Agent flagged: validate won't protect; only evidence conditions. The plan acknowledges risk 1 partially. Is this a "double-grant path"? The same item (same definition) could be granted both via a native grant row and via a hand-written owner elsewhere, giving two copies where the original gives... actually in the original game could you get two copies? Unknown. This is speculative; the plan's conditions are the guard. I'll flag as MINOR (test only proves same-row case; definition-level duplicate not guarded).

  12. **walkthrough_save.gd:246 migrate_loaded writes state.collected = []** — unlisted save-copy write. Plan's 2.8 lists walkthrough_save.gd:155-159 but not :246. If the census fixture is built from the same search, :246 (state.collected = []) might match the scan (assigns a local named collected? The search was for appends/erases/assigns of carried_collected etc. — `state.collected = []` — depends). Worth a MINOR: census may miss it or the guard may trip on it. Actually guard rule 1 matches `carried_collected`...`=` — `state.collected = []` doesn't match. Fine, MINOR at most. Actually wait — it's a v1→v2 migration that EMPTIES the pack? Let me check walkthrough_save.gd:246. If migrate_loaded sets state.collected = [] that could be a lost-item path for old saves! Let me read it.

  Also should double check hive_flute_floor assign claim (risk 4) and hiveReview carried_inventory. Probably fine.

  Also check "295 test files read / 85 write" claims? Hard to verify quickly; skip or spot-check with a grep count.

  Let me verify: l8_herbalist.gd, l9_pyre.gd:105-115, walkthrough_save.gd:240-250, and count test files reading/writing carried_collected.

• Two more verifications: the `l8_herbalist` builder contradiction, `l9_pyre` dispatch lines, `walkthrough_save.gd:246`, and the test-count claims.extends RefCounted
## Fresh-visit HERB_.WOM hotspot0/1/2 grants, flags200..205; later flag206 bonus is separate.
const KINDS := ["sap","amber","aloe"]
const DEFINITIONS := {"sap":111,"amber":112,"aloe":110}
static func ids() -> Array:
 var result:Array=[]
 for kind in KINDS:
  for n in 2:result.append("jungle:herb:"+kind+":"+str(n))
 return result
static func valid(id: Variant)->bool:return id is String and id in ids()
static func kind(id: String)->String:return id.get_slice(":",2) if valid(id) else ""
static func definition(id: String)->int:return DEFINITIONS.get(kind(id),-1)
static func initial()->Dictionary:return {"version":1,"collected":[]}
static func validate(state: Variant)->String:
 if not state is Dictionary or state.size()!=2 or state.get("version")!=1 or not state.get("collected") is Array:return "Invalid herbalist state."
 var seen:={}
 for id in state.collected:
  if not valid(id) or seen.has(id):return "Invalid herbalist pickup identity."
  seen[id]=true
 return ""
static func pick(state: Dictionary, inventory: Array, requested: String, admitted: bool)->Dictionary:
 var error:=validate(state)
 if not error.is_empty():return {"ok":false,"reason":error}
 if not admitted:return {"ok":false,"reason":"Enter the village first."}
 if requested not in KINDS:return {"ok":false,"reason":"Choose a jar."}
 if inventory.size()>=64:return {"ok":false,"reason":"Inventory full."}
 for id in ids():
  if kind(id)!=requested or id in state.collected:continue
  if id in inventory:return {"ok":false,"reason":"This item is already carried."}
  var next:=state.duplicate(true)
  var carried:=inventory.duplicate()
  next.collected.append(id);carried.append(id)
  return {"ok":true,"state":next,"inventory":carried,"notice":{"sap":"You take ironwood sap.","amber":"You take amber.","aloe":"You take cave aloe."}[requested]}
 return {"ok":false,"reason":"There is no more to take from this jar."}
====
 elif state().phase==3 and reachable(ALTAR+Vector3.UP*12):hint.text="E — Take filled urn" if not state().slots.get(State.TARGET,{}).get("occupied","").is_empty() else "E — Fill urn with ashes"
func _unhandled_input(event: InputEvent):
 if event is not InputEventKey or not event.pressed or event.echo or event.keycode!=KEY_E or not active() or Input.mouse_mode!=Input.MOUSE_MODE_CAPTURED or is_instance_valid(host.inventory):return
 var result: Dictionary
 if state().phase==0:result=place() if state().holding else grab()
 elif state().phase==3:
  var occupied: String=state().slots.get(State.TARGET,{}).get("occupied","");result=urn("retrieve") if not occupied.is_empty() else urn("insert",State.URN)
 else:return
 if result.ok:host.save_feedback(result.reason);get_viewport().set_input_as_handled()
	if not error.is_empty():
		return {"error": error}
	return {"error": "", "state": migrate_loaded(parser.data)}

static func migrate_loaded(value: Dictionary) -> Dictionary:
	var state := value.duplicate(true)
	if state.version == 1:
		state.version = VERSION
		state.collected = []
	return state

static func write_save(path: String, state: Dictionary, checkpoint_count: int) -> String:
	var error := validate(state, checkpoint_count)
	if not error.is_empty():
		return error
====
242:static func migrate_loaded(value: Dictionary) -> Dictionary:
299
132


• Findings:

  1. **l8_herbalist.gd:24 `pick` is a pure builder** — `var carried:=inventory.duplicate()` at :30, append at :32 to the copy, returns {"inventory": carried}. So:
     - Table 2.1 lists `l8_herbalist.gd:32 pick` as a function that "adds to a pack" (way A append) — wrong, it appends to a duplicate.
     - Table 2.2 lists `l8_herbalist.gd:32` as a caller that "appends to the carried it is given" — wrong, it duplicates first.
     - 2.3's builder note lists `l8_herbalist.gd:30-33 pick` as a builder — right.
     - Commit 6 (plan line 382) migrates `l8_herbalist.gd:32` — but builders "stay as they are, for good" (line 195). Contradiction: either commit 6 edits the builder (against line 195) or the entry means the caller (who assigns result.inventory — who is the caller? Probably l8_village or jungle host calls Herbalist.pick and assigns carried_collected = result.inventory). Let me check the caller — grep for Herbalist.pick usage. If the caller assigns the whole pack, the caller is a way-C site missing from table 2.3! Let me check.

  2. **l9_pyre.gd:109,111**: `_unhandled_input` calls `urn("retrieve")` / `urn("insert", State.URN)` — dispatch, not a loader. Classified in 2.8 as loader/validator. Misclassification — MINOR (commit-0 fixture would pin kind "loader" for a dispatch).

  3. **walkthrough_save.gd:246**: v1→v2 migration sets `state.collected = []` — empties the pack on migration of a v1 save! Is that a lost-item path? It says version 1 → VERSION; collected reset. Which save format is this — walkthrough_save.gd is the Cave's save (per plan 2.8: "walkthrough_save.gd:155-159 (Cave...)"). Hmm, `state.collected = []` in the cave save migration. That would drop all cave collected items for v1 saves. Whether v1 saves exist in the wild (golden saves from Plan 3 are presumably current version). It's a migration losing the pack — but maybe v1 never had a pack or the shape changed entirely. This is pre-existing behaviour, out of the plan's scope, but the plan's claim "Old saves keep loading because no save key is added..." is about F-08 not changing anything, fine. Still worth flagging as MINOR: census/serializer list incomplete (walkthrough_save.gd:246 unlisted; if the commit-0 census scan is rerun it may or may not match depending on pattern). Actually the bigger deal: plan's old-save claim relies on "no key added, renamed or removed" — fine.

  Hmm, is it a real lost-item path? For a cave v1 save, yes, collected is wiped by migration. Do v1 cave saves exist? walkthrough_save VERSION — let me check quickly what VERSION is and whether v1 saves could exist (e.g., golden saves). This could matter for the commit-9 old-save test if any golden is cave v1. Quick check: grep VERSION in walkthrough_save.gd and see if any test fixture has version 1 cave save.

  4. Test counts: plan says "295 test files that read them and the 85 that write them" (line 13). My grep: 299 test files mention carried_collected/carried_inventory (read or write), 132 match write patterns. 299 vs 295 — close but my regex differs; 132 vs 85 is a big difference, though my write regex is broader (includes `carried_collected =` anywhere, and `.append` directly on the name; the plan's count method unknown — LIKELY grade? The plan states it as fact in §0). This is a MINOR unverifiable/likely-wrong count. Careful: plan counts may have used a different definition. Flag MINOR.

  5. K95 gap A verification: guard rules now name builders as must-stay-clean. Verified builders duplicate before mutation (l8_herbalist, l10_emperor_state, l10_priest, etc. per agent-0). But there's a remaining hole: guard rule 1 matches `carried()` followed by `.erase` — player_item_controller.gd:68,75,96,105,113 erases are NOT in any allow-list and NOT in commit 10's scope. Also does guard rule 1 match `carried().erase` before commit 10? "Erase and its relatives are only enforced after commit 10; before that they are reported, not failed." After commit 10 they fail → tree red unless player_item_controller use is migrated or allow-listed. Commit 10 covers "the 12 functions of 2.7 plus the removals listed under it" — the "Also PROVEN removals" list (line 241) doesn't include player_item_controller either. So confirmed MAJOR gap: plan's own guard would fail at commit 10 on player_item_controller.gd erases... wait, actually would the guard match them? Rule 1: "A line where ... `carried()` ... is followed by ... `.erase`..." → `carried().erase(id)` matches. Yes.

  Also, wait — is `player_item_effects.gd:82 use` a removal? Agent-0 said it duplicates then remove_at on the copy — a builder; live write via controller :130-131. It's listed in 2.7 as a removal — misclassification (MINOR), and commit 10 would migrate it to ItemGrants.remove which... operates on the live pack — changing a builder into a live remover? The function `use(current, inventory, id)` returns a result; migrating it to ItemGrants.remove(host, id) would change its signature/behavior. Plan says "No behaviour change". If it's actually a pure function with its own tests (like other builders), routing it through ItemGrants.remove contradicts "builders stay as they are". Let me verify player_item_effects.gd:82 quickly.

  6. Museum/Cave save-field error in §3 (line 341): confirmed. MINOR.

  7. sync_first contradiction: confirmed MAJOR... let me decide grade. The plan's contract says keep each site's order; commit 2 text says "sync_first for the fountain ball" only, while l16_dry_fountain has the same sync-before-history order. A migrator following commit 2 would pass plain sync for dry fountain → order change (though end state equal). The plan explicitly stakes "each later commit keeps it green" with the site fixture test pinning pack+packet after each site — would the fixture catch an order-only change with equal end state? No. So behaviour stays green but the plan's own "keep the order" rule is violated by its migration instruction. Factually wrong sentence ("only ... needs it"). MAJOR (wrong instruction in the plan), though zero runtime impact. I'll say MAJOR-lite... I'll grade MAJOR since the instruction is wrong and the plan's core promise is "no behaviour change, keep each site's spelling."

  Hmm, actually since end state provably equal (sync rebuilds carried from pack; the history append touches collected; order between them doesn't interact), and the plan itself notes this, calling it MAJOR overstates. But the wrong "only" could lead a migrator to not even consider dry fountain. I'll grade it MAJOR because it's a contradiction between section 3 and table 2.9 that affects a migration instruction.

  8. player_item_controller erase hole: MAJOR (guard would go red at commit 10, or the enforcement can't be enabled).

  9. l8_herbalist caller check needed. Let me grep for callers of Herbalist.pick / "pick(" with herbalist.

  Also need to double check K95 gap A closure fully: are there any live-store writers among "must-stay-clean" list that actually DON'T duplicate? Agent-0 verified all builders duplicate. Serializers write result/filter — fine. area_world_items.gd:81 vs plan's :79 drift — MINOR.

  Also commit 9 guard rule 3: "A call that passes a live store, or such an alias, as an argument to a function that is not on the rule-function list." Allowed: "the rule functions of 2.2 as callees for rule 3". But 2.2's l8_herbalist row is wrong (it duplicates, doesn't take the live pack — actually its caller passes the live pack as `inventory` argument!). Let me check the caller of Herbalist.pick: if the caller passes `carried_collected` directly as `inventory`, then pick duplicates it — so it's a live store passed as argument to a function; is l8_herbalist.pick on the rule-function list? 2.2 lists it (with a wrong description). So allowed. But since pick duplicates, the builder guard probe ("x.duplicate().append(id) must pass") is fine.

  Let me find the herbalist caller and check player_item_effects.gd:82.

• Two more spot checks: the `l8_herbalist` caller and `player_item_effects.gd:82`../act_one_quest_state.gd:358:	if state.has("l8_herbalist"):
./atlas_places.gd:60:			"source": "l8_journey TARGETS village; hint book ch.8 'the Wild Village' (herbalist and shaman treehouses, the guard at the great tree)"},
./l8_journey.gd:16:## The Wild Village is a special scene with several views (HINTBOOK 2984-3009: the herbalist's treehouse, the shaman's, the
./l8_journey.gd:17:## doorway right of the shaman, Daniel's). "" is the clearing; "herbalist" / "shaman" / "daniel" are the approached views.
./l8_journey.gd:89:		var taken: Dictionary = herb.pick(host.quest_state.get("l8_herbalist",herb.initial()),host.carried_collected,action.get_slice(":",1),state().admitted)
./l8_journey.gd:91:			host.quest_state.l8_herbalist=taken.state
./l8_journey.gd:246:		"herbalist":
./l8_journey.gd:247:			if notice.is_empty(): text.text = "The herbalist's treehouse. She does not mind if Luther takes from her jars."
./l8_journey.gd:263:			if notice.is_empty(): text.text = "The Wild Village. The herbalist's treehouse is on the left, the shaman's in the middle, Daniel's on the right. " + next_step()
./l8_journey.gd:266:			add_view("Approach the herbalist's treehouse","herbalist")
====
	if gate_reason != "":
		return _rejected(current, pack, described.kind, gate_reason, "admission", 0)
	if described.kind != "champion_stone":
		return _rejected(current, pack, described.kind, str(described.reason), "effect", -1)
	if pack.find(item_id) < 0:
		return _rejected(current, pack, described.kind, "Champion Stone is not in the inventory.", "pack", -1)
	var consumed := int(parsed.gate_223d4) == 0
	if consumed: pack.remove_at(pack.find(item_id))
	var before := BONUS if current.active else 0
	var next := {"version": VERSION, "active": true, "timer": _extend(int(current.timer))}
	return {"applied": true, "reason": "", "rejected_by": "", "kind": "champion_stone", "state": next, "inventory": pack, "consumed": consumed, "activated": before == 0, "bonus_before": before, "bonus": BONUS, "source_result": 1}

static func maintain(state: Variant, delta: Variant) -> Dictionary:
	var restored := restore(state)
	if restored.has("error"): return restored
	if not Numbers._integer(delta, 0xffffffff): return {"error": "Invalid stone timer delta."}
	if not restored.state.active: return {"error": "Inactive Champion Stone has no event 8."}
	var timer := _sub(int(restored.state.timer), int(delta))
	var expired := not _positive(timer)
	return {"state": {"version": VERSION, "active": not expired, "timer": timer}, "expired": expired, "bonus_before": BONUS, "bonus": 0 if expired else BONUS, "timer": timer}



• Confirmed:

  - `l8_journey.gd:89` passes the **live** `host.carried_collected` to `herb.pick(...)` and then (line ~91-93 presumably) assigns `host.carried_collected = taken.inventory`. So the herbalist pick IS a way-C transaction: pure builder + caller assigning the whole pack. The plan's 2.2 row describing l8_herbalist.gd:32 as "appends to the carried it is given" is wrong (it appends to a duplicate). But more importantly: is `l8_journey.gd:89`'s pack assignment listed anywhere? Table 2.3 lists `l8_journey.gd:92,111 interact` — line 92 might be the pack assignment `host.carried_collected=taken.inventory`. Let me check lines 89-113 of l8_journey.gd. If :92 is that assignment, it's covered. And commit 6 says "l8_herbalist.gd:32" is migrated — should actually say the caller l8_journey.gd:89-93 / the builder stays. Commit 9's must-stay-clean list includes l8_herbalist.gd:32 — good. But commit 6 instructs migrating l8_herbalist.gd:32, contradicting both the builder-stays rule and the guard's must-stay-clean list (a file could be edited in commit 6 then asserted clean in commit 9 — "clean" means matching the guard rules, and pick duplicates so it stays clean regardless). Still, the instruction "migrate l8_herbalist.gd:32" is wrong-ish: there's nothing to migrate there; the caller is in l8_journey.gd (commit 5, table 2.3). MINOR-MAJOR inconsistency.

  - `player_item_effects.gd:82`: `pack.remove_at(pack.find(item_id))` — need to see where pack comes from. Let me look above line 75: presumably `var pack = inventory.duplicate()`. Agent said so. So it's a builder mutating a copy, listed in 2.7 as a removal — misclassified. Commit 10 would route it through ItemGrants.remove → changes a pure builder's contract; contradicts "builders stay as they are". MINOR-MAJOR.

  Let me check l8_journey.gd:88-113 and player_item_effects pack origin quickly. Also check the K95 gap A remaining question — done mostly.

  Then I have enough for the report. Let me also quickly count: plan §0 says "62 functions in 53 files" add — agent-0 confirmed all exist. Fine.

  One more check on K95 gap B closure: plan introduced two modes and table 2.9 — agent-1 verified all 24 rows. Gap closed.

  Gap A closure: guard redefined to live-store writes with builders/serializers named must-stay-clean + probe. Verified builders duplicate. Closed — except the newly found erase hole (player_item_controller) which is a NEW gap, and arguably l8_herbalist commit 6 inconsistency.

  Gap C: closed (dragon blood moved to 2.7, commit 10, guard rule 1). Verified :29.

  Gap D: closed (2.8 listing, key erase verified at :504, :592).

  Also: hive_flute_floor.gd:214 assign claim (risk 4) — agent-0 confirmed `collected.assign(...)` at :214, listed. Fine.

  Old-save "equal field by field" test concern: given load-time migrations (world-item restores add history entries; jungle_source_pickups sets quest flags), a load→save round trip changes save bytes for pre-history saves. The commit-9 old-save test says "load, and the pack, packet and histories are equal field by field" — equal to what reference? If reference is the recorded post-load state from commit 0 (pinned), then fine — can fail, works. If it's comparing against the on-disk save bytes, then for act2 hosts the pack order (legacy+packet.carried) differs from interleaved inventory.collected... wait no — inventory.collected on act2 hosts contains only act1/legacy ids (act2 filtered out), and restore builds legacy + packet.carried. The live pack after load = inventory.collected + packet.carried, which is NOT what's in any single saved field. If the test compares live pack to `inventory.collected` field it fails on unmodified code — test cannot pass as literally specified for act2 hosts. That ambiguity is worth a MINOR (test spec ambiguous; as literally written it would fail even pre-migration for act2 hosts, or must be silently reinterpreted).

  Enough. Quick final checks.		return {"ok":true}
	if action.begins_with("herb:"):
		var herb = preload("res://scripts/lol2/l8_herbalist.gd")
		var taken: Dictionary = herb.pick(host.quest_state.get("l8_herbalist",herb.initial()),host.carried_collected,action.get_slice(":",1),state().admitted)
		if taken.ok:
			host.quest_state.l8_herbalist=taken.state
			host.carried_collected=taken.inventory
			notice=taken.notice
		return taken
	if action in ["initiation","shaman_silverleaf"]:
		var at_table: bool = opened=="village"
		close()
		var trade:Dictionary=host.get_node("L8Tribe").offer(offered) if action=="initiation" else host.get_node("L8Tribe").offer_shaman(offered)
		host.save_feedback(trade.get("reason",""))
		if action=="shaman_silverleaf" and at_table:
			# BJ12: the trade leaves Luther at the shaman's table, where the serum and a leaf can be mixed at once.
			opened = "village"; view = "shaman"
			Input.mouse_mode = Input.MOUSE_MODE_VISIBLE
			get_tree().paused = true
			notice = str(trade.get("reason","")) + (" It does nothing alone: mix it with a Silverleaf, here or from the pack." if trade.ok else "")
		return trade
	var result := State.act(state(),host.carried_collected,action,offered)
	if not result.ok: return result
	# No awaits/signals between these writes: one synchronous transaction.
	host.quest_state[KEY] = result.state
	host.carried_collected = result.inventory
	if host.get("equipped_item") == State.BLADE and State.BLADE not in result.inventory:
		host.equipped_item = ""
====
	if reason == "" and not described.usable: reason = str(described.reason)
	return {"admitted": admitted, "usable": admitted and described.usable, "reason": reason, "kind": described.kind}

static func use(state: Variant, inventory: Variant, item_id: Variant, gates: Variant) -> Dictionary:
	var restored := restore(state)
	if restored.has("error"): return restored
	var pack_error := _inventory_error(inventory)
	if pack_error != "": return {"error": pack_error}
	var parsed := _gates(gates, true)
	if parsed.has("error"): return parsed
	var described := describe(item_id)
	if described.has("error"): return described
	var current: Dictionary = restored.state
	var pack: Array = inventory.duplicate()
	var gate_reason := _gate_reason(parsed)
	if gate_reason != "":
		return _rejected(current, pack, described.kind, gate_reason, "admission", 0)
Confirmed:
  - `l8_journey.gd:92` is `host.carried_collected=taken.inventory` — the herbalist pack assignment. Table 2.3 lists `l8_journey.gd:92,111 interact` — so covered as way C. And commit 6's "l8_herbalist.gd:32" entry is therefore wrong/pointless: the builder stays (per line 195 and commit 9's must-stay-clean list which includes l8_herbalist.gd:32), and the actual migration target (l8_journey.gd:89-92) is in commit 5 via table 2.3. So commit 6 lists a site that must NOT be edited. MAJOR or MINOR? A migrator told to "migrate l8_herbalist.gd:32" might edit the builder, violating line 195 and tripping commit 9's probe. I'd call it MAJOR (contradictory migration instructions across commits).

  Hmm wait, let me re-read commit 6 line 382: "...; `l8_herbalist.gd:32`." Ambiguous what "migrate" means for it. Given line 195 says builders stay "for good", listing it as a migration target in commit 6 is at minimum confusing/contradictory. MAJOR-lite. I'll grade MAJOR given the adversarial-audit context.

  - `player_item_effects.gd:71`: `var pack: Array = inventory.duplicate()` then `:82` `pack.remove_at(...)` — confirmed builder on a copy. Listed in 2.7 as a removal ("player_item_effects.gd:82 use"). Commit 10 would wrap it in ItemGrants.remove — but it's a pure function whose caller (player_item_controller.gd:124-131) assigns the result; migrating it as a "removal" through ItemGrants.remove(host, id) would change its pure contract. Actually wait — maybe commit 10 intends the removal to happen through the controller. But the entry in 2.7 names player_item_effects.gd:82. Misclassification, MINOR-MAJOR. It parallels K95 gap D (loaders misclassified as removals) — a residual of the same kind. I'll grade MINOR since the line is at least listed and the actual live write (controller :130-131) is covered in commit 5; the danger is commit 10 editing a pure builder unnecessarily.

  Hmm — actually there is a subtle issue: after commit 5 migrates the controller's :130-131 to ItemGrants.commit, and commit 10 turns on the erase guard... `player_item_effects.gd:82` is `pack.remove_at` on a duplicated local — guard rule 1 requires the live-store names; `pack` is bound to `inventory.duplicate()` — rule 2: "a local bound to a live store WITHOUT .duplicate(" — it has .duplicate( → not matched. Fine, stays clean. So the practical impact is only the wrong-kind fixture pin and possibly a wrong commit-10 edit. MINOR.

  Now the erase-guard hole for player_item_controller.gd:68,75,96,105,113,124 — wait, is :124 also an erase? From my sed of 123-132: line ~124 is `var result:=Effects.use(...)`. Hmm. The plan's 2.3 row lists lines 68,75,96,105,113,124,130,131. Erases at 68,75,96(?),105(?),113,124(?). My sed showed erases at: 68 (`carried().erase(id)`), 75 (dampen block), then in 94-98 block: `current.spent.append(id); carried().erase(id)` at ~96; 104-106: erase at ~105; 112-114: erase at ~113; 123-132: `if not host.has_method("carried_items"): carried().erase(id)` at ~124. So six erases at 68,75,96,105,113,124 and the two assignment lines 130-131. Confirmed: six live-pack erases through the accessor, classified as way-C "replace whole pack". 

  Impact analysis:
  - Commit 5 migrates :130-131 to ItemGrants.commit. The six erase lines remain, now adjacent to the new commit call.
  - Commit 9's guard: before commit 10, erases reported not failed. After commit 10, erase enforcement on → `carried().erase(id)` in player_item_controller.gd matches rule 1, file not allow-listed → guard fails. Commit 10's scope: "the 12 functions of 2.7 ... plus the removals listed under it" — line 241's "Also PROVEN removals" list doesn't include player_item_controller. So commit 10 leaves the tree red, or requires unplanned migration of controller.use's erase lines to ItemGrants.remove. MAJOR.

  Also dragon blood's erase is covered (in 2.7 now). Good.

  Another check: `_consume_hand_item` jungle_walkthrough.gd:749-753 — in 2.7. Fine.

  Now assemble the final report. Also mention:
  - §3 Save paragraph wrong about Museum/Cave/incomplete for act2 hosts (line 341) — MINOR.
  - §1.2 line 40 combined-64 list incomplete (misses act2_save.gd:25, dragon_level.gd:161, act2_jungle_return.gd:37) — MINOR. Wait, plan line 40 says checked at ":116, act2_map.gd:324 and darker_jungle.gd:274" — missing three sites. MINOR.
  - area_world_items.gd:79 → actually :81 line drift — MINOR (the plan says anchors may drift, function names stable; and it's a serializer listed by line). Barely worth it. I'll fold into a minor line.
  - Table 2.9 order column omissions (sync missing for 5 rows) — MINOR.
  - l8_dawn/l8_larkhon copies lack Items.initial() fallback — the header says "several start from Items.initial()" — accurate ("several"), but the flagged normalization in §3 (line 331) says for both act2 modes the API reads with `get("act2_items", Items.initial())` — for l8_dawn.gd:26-27 (raw `.act2_items.duplicate(true)`), today it would error if key missing, after migration it wouldn't — that's the same flagged normalization category as in-place sites, but 2.9's Packet column says "copy" for l8_dawn without noting the missing fallback, and §3 only flags the normalization for "the 'in place' sites". l8_dawn is an L8 (Act 2 start) site — can act2_items be missing there? quest_state.get... l8_dawn uses host.quest_state.act2_items directly, so presumably always present in act2 hosts. MINOR nuance; the normalization flag list is incomplete (l8_dawn, l8_larkhon, l8_tribe, l10_emperor, l10_priest raw-read sites also gain the initial() fallback). MINOR.
  - history_spelling_test "if one exists" escape — can pass vacuously for always-sites not reachable twice. MINOR (test cannot fail for those rows).
  - commit-8 test only proves same-row idempotency; definition-level duplicate (placement id + grant id for same definition) not guarded by catalog validate — the plan's 3.1 conditions are the only guard; no test for that. MINOR.
  - walkthrough_save.gd:246 migrate_loaded sets state.collected=[] — unlisted serializer write; also v1→v2 cave migration wipes collected — potential lost-item path for v1 cave saves (do any exist? golden saves are presumably v2). Flag MINOR with the caveat. Actually — could this bite the commit-9 old-save test? If any golden save is cave format v1, loading wipes the pack. The plan claims old saves load with pack intact. Let me quickly check walkthrough_save VERSION and whether fixtures contain version 1. Quick grep.

  Also the "295 test files / 85 write" counts: my grep found 299 read / 132 write-ish. Different methods; plan's numbers unverifiable and likely undercounted for "write" (132 by a simple pattern). MINOR.

  Let me do the last quick check on walkthrough_save VERSION and v1 fixtures.

• Last check: the `walkthrough_save.gd` v1→v2 migration and whether any golden/fixture save is cave v1.6:const VERSION := 2
91:	if not _number(value.get("version")) or (value.version != 1 and value.version != VERSION):
93:	if value.version == VERSION and not Collectible.validate_ids(value.get("collected")):
245:		state.version = VERSION
253:	if state.version != VERSION:


• No v1 walkthrough fixtures found in tmp/ or tests/fixtures (no output for the second grep — actually it printed nothing, meaning no matches). So the v1 wipe is theoretical. I'll fold it into a MINOR.

  I have everything. Now write the final audit report.

  Structure:
  1. K95 gap re-check (4 gaps, each with plan line quote + code proof).
  2. New findings, each starting with '• ' (file:line, severity, concrete failure).
  3. VERDICT line.

  Format requirement: "End with findings, each starting with '• ' (file:line, BLOCKER/MAJOR/MINOR, concrete failure). The last line must be exactly VERDICT: PLAN OK or VERDICT: PLAN NEEDS WORK."

  So the findings bullets should be at the end. I'll write the K95 re-audit section first (with quotes), then the findings list, then verdict.

  Grades for new findings:
  1. player_item_controller.gd:68,75,96,105,113,124 — six live-pack erases via `carried().erase(id)` classified in table 2.3 as whole-pack replacement; not in 2.7, not in commit 10's scope; guard rule 1 (`carried()` + `.erase`) fails them once commit 10 turns erase enforcement on → tree red or forced unplanned edit. MAJOR.

  2. l16_dry_fountain.gd:157 — plan line 332/374 claims sync-first is needed "only" by l16_fountain_ball; dry fountain has the identical order (append :156, sync :157, history :158) — commit 2 would migrate it with post-history sync against the plan's own keep-each-site's-order rule. MAJOR. (Impact: end state equal; but instruction factually wrong.)

  3. commit 6 (plan line 382) lists l8_herbalist.gd:32 as a migration target, but the code (l8_herbalist.gd:30-32) duplicates the pack and is a pure builder that line 195 says stays "for good" and commit 9 names must-stay-clean; the actual write is the caller's assignment l8_journey.gd:92, already in table 2.3/commit 5. Contradictory instructions. MAJOR.

  4. §3 Save paragraph (line 341): "the pack is written ... inventory.collected in each area's save" — false for Museum (checkpoint.collected, museum_walkthrough.gd:921-926, no inventory key) and Cave (no pack list, per-owner keys); incomplete for act2 hosts (act2 ids filtered into quests.act2_items.carried, act2_map.gd:338). Commit-9 old-save test "pack ... equal field by field" inherits this: on act2 hosts the live pack is the union of two fields, and restore (act2_items_catalog.gd:117) rebuilds legacy+packet.carried, so live pack order is not the saved order. MINOR.

  5. §1.2 (plan line 40): combined-64 check list misses act2_save.gd:25 (the disk-save guard), dragon_level.gd:161, act2_jungle_return.gd:37. MINOR.

  6. player_item_effects.gd:82 misclassified as a removal in 2.7: line 71 duplicates the pack (`var pack: Array = inventory.duplicate()`), :82 remove_at on the copy; live write is the caller's assignment (player_item_controller.gd:130-131). Commit 10 would wrap a pure builder in ItemGrants.remove, contradicting "builders stay as they are". MINOR.

  7. l9_pyre.gd:109,111 misclassified as loaders in 2.8: they are the E-key dispatch calling urn("retrieve")/urn("insert",...) (l9_pyre.gd:106-111) — the grant path is the way-C urn at :72,74 in 2.3. Commit-0 fixture pins a wrong kind. MINOR.

  8. Table 2.9 Order column omits trailing Items.sync for five rows (l12_citadel.gd:42, l8_dawn.gd:30, l8_larkhon.gd:59, l19_belial_horn.gd:70, l19_dawn_curse.gd:246) and the copy-without-initial()-fallback sites (l8_dawn.gd:26, l8_larkhon.gd:56, l8_tribe.gd:100, l10_emperor.gd:68, l10_priest.gd:77) are not covered by §3's flagged normalization, which only names the "in place" sites — after migration these gain a missing-key fallback they don't have today, an unflagged normalization. MINOR.

  9. item_grant_history_spelling_test (plan line 369): "for each 'always' site that can be reached twice from a test ... if one exists" — rows where no double-fire harness exists test nothing; the test cannot fail for those rows, yet commit 9 treats "act2 vs act2_once" as proven. MINOR.

  10. Commit-8 native test (line 386) proves only same-row idempotency; catalog validate (act2_items_catalog.gd:95-106) checks duplicates per base id, so a grant id act2:<AREA>:grant<N> and a placement id act2:<AREA>:itemM for the same definition coexist — the 3.1 evidence conditions are the only guard against that double-grant, and no test covers it. MINOR.

  11. Census/serializer list incomplete: walkthrough_save.gd:246 (`state.collected = []` in v1→v2 migrate_loaded) is a write the 2.8 serializer table doesn't list; benign for the guard (name doesn't match) but the commit-0 census fixture will rediscover it. Also area_world_items.gd:79 anchor drifted (normalization at :81). MINOR.

  12. §0 counts "295 test files read, 85 write" — a grep finds 299 test files touching the stores and 132 with write-shaped lines; method unknown, numbers likely off. MINOR? This is weak; maybe skip or keep as minor. I'll include briefly.

  Actually let me not pad. Keep the strongest. I'll include 12 as a minor note within the K95 section? No — keep findings list. I'll drop #12 to keep the report tight? The instruction says find wrong file/field names etc. The count discrepancy is verifiable-ish but methods differ; I'll include it as MINOR with the caveat.

  Also should I double check claim "295 test files" - the plan says "the 295 test files that read them and the 85 that write them keep working". My counts: 299 read, 132 write-shaped. The write regex I used includes any `carried_collected =` in tests, which the plan may not count (maybe they count only appends). Ambiguous. I'll mention it as MINOR with "method-dependent".

  BLOCKERs: none — no missed grant sites, census complete, save/load has no double-grant/lost-item path found, and the K95 gaps are genuinely closed. Verdict: PLAN NEEDS WORK due to the three MAJORs.

  For the K95 section, quote plan lines and code:

  Gap A (source guard): plan lines 388-397 (commit 9 redefined: live-store-only three rules, builders/serializers "must stay clean", probe). Verified builders duplicate: l8_herbalist.gd:30-32 (`var carried:=inventory.duplicate()`), player_item_effects.gd:71, l10_priest.gd:52, l12_frozen_bow.gd:56 etc. Serializers act2_map.gd:338 filter on result. Closed in substance (new residual issues listed separately).

  Gap B (history modes): plan lines 326-332 (two modes "act2"/"act2_once", table 2.9). Verified table 2.9 row by row — all 24 rows match code (examples: l12_citadel.gd:25 unconditional in-place; l16_fountain_ball.gd:86 guarded). Closed, with the dry-fountain sync_first residual.

  Gap C (dragon blood): plan lines 235 (2.7 row), 399 (commit 10), 389 (guard rule 1). Code: player_dragon_blood.gd:29 `saved.spent.append(id);controller.carried().erase(id)`. Closed.

  Gap D (two loaders): plan lines 254-255 (2.8 rows). Code: jungle_walkthrough.gd:504 and :592 `inventory.erase("fighting")` on a duplicated dictionary; assignment at :454. Closed.

  Write the final answer in the requested format.

• # Re-audit of ITEM_GRANT_PLAN.md rev 2 (F-08) against `~/opus_work/lol2_sol_playtest_starts` @ fde4d19

  Tree is two commits past the plan's 742dcab anchor; `git diff 742dcab..HEAD -- scripts/` touches only `game_save.gd`, `game_session.gd`, `game_areas.gd`, `original_game_gate.gd`, `playtest_starts.*` — no pack writers, so the census anchors are comparable.

  ## 1. The four K95 gaps

  **A. Source guard vs. builders/serializers — CLOSED.** Plan line 389-391 now restricts the guard to "writes to the live store only" (three rules: direct, alias "without `.duplicate(`", live store as argument), and lines 393-395 name the pure builders, `mechanism_transaction.gd:72,104`, the four `inventory_state()` serializers and the history normalizations as must-stay-clean, with a probe that `x.duplicate().append(id)` must pass. I verified the named builders really do duplicate before mutating: `l8_herbalist.gd:30-32` (`var carried:=inventory.duplicate()`), `player_item_effects.gd:71`, `l10_priest.gd:52` (`var next_items:=items.duplicate(true)`), `l12_frozen_bow.gd:56`, `l9_pyre.gd:73`, and the serializers write result/save dictionaries (`act2_map.gd:338` filters the dictionary returned by `super.inventory_state()`). One residual hole and two residual misclassifications — findings 1, 6, 7 below.

  **B. History mode smoothing — CLOSED.** Plan lines 326-329 now define `"act2"` (append unconditionally) vs `"act2_once"` (append if absent), and table 2.9 was read line by line. I re-verified all 24 rows against the code: every Guard and Packet spelling matches — e.g. `l12_citadel.gd:25` `host.carried_collected.append(...);host.quest_state.act2_items.collected.append(...);Items.sync(host)` (always, in place), `l16_fountain_ball.gd:86` `if not id in host.quest_state.act2_items.collected: ...append(id)` (once, in place), `l10_priest.gd:49` refuses when the urn is already in `collected`, `act2_world_items.gd:82` refuses when already carried and `:87` appends unconditionally with a hand-rebuilt `packet.carried` at `:89` and no sync. The "in place → missing key no longer raises" normalization is flagged at plan line 331. Closed, with the `sync_first` residual in finding 2.

  **C. Dragon blood removal — CLOSED.** Plan line 235 now lists `player_dragon_blood.gd:29` in 2.7 with the note "a live-pack removal through the accessor", commit 10 (line 399) includes it, and guard rule 1 matches `carried()` + `.erase` (line 389). Code confirms: `player_dragon_blood.gd:29` `saved.spent.append(id);controller.carried().erase(id)`.

  **D. Two loaders misclassified as removals — CLOSED.** Plan lines 254-255 now list both in 2.8 with the correct description. Code confirms: `jungle_walkthrough.gd:504` and `:592` are `inventory.erase("fighting")` on `state.inventory.duplicate(true)` — a dictionary-key erase on a copied transport packet; the pack assignment is `carried_collected = state.collected.duplicate()` at `:454`.

  Census completeness was also re-run independently: every mutation line of `carried_collected` / `carried_inventory.collected` / `carried()` / the act2 packet in `scripts/lol2/*.gd` is attributable to a plan-listed function; no unlisted live-pack grant or removal site exists (no `set("carried_collected")`, no dangerous `call` dispatch, `l14_machines.gd` enters via the listed `act2_world_items.gd` take). The save/load sweep found **no double-grant path** (all loaders replace the pack; all world-item restores migrate carried→history toward "taken", e.g. `jungle_world_items.gd:67-68`; the cave→museum transfer meta is single-shot and stripped on slot load by `game_session.gd:64`) and **no silent lost-item path** (all capacity/history failures refuse the whole save or load, with the 5ac1bca rollback).

  ## 2. Findings

  - `player_item_controller.gd:68,75,96,105,113,124` — MAJOR — six lines are `carried().erase(id)`, live-pack removals through the accessor (the exact pattern K95-C moved dragon blood to 2.7 for), but table 2.3 (plan line 191) files them as way-C "replace the whole pack". They are not in 2.7, not in commit 10's scope (line 399), and not allow-listed — so when commit 10 turns on erase enforcement, guard rule 1 (line 389: "`carried()` ... followed by ... `.erase`") fails the tree, or commit 10 must do an unplanned migration of `use()`.
  - `l16_dry_fountain.gd:157` — MAJOR — plan line 332 says `opts.sync_first` is needed "only `l16_fountain_ball.gd:85-86`", and commit 2 (line 374) grants it to the fountain ball alone, but the dry fountain has the identical order: append at :156, `Items.sync(host)` at :157, guarded history append at :158 (the plan's own table 2.9 records it: "pack, (line 157), history"). Migrating per commit 2 changes the dry fountain's operation order against the plan's own keep-each-site's-order rule (risk 3, line 426).
  - `l8_herbalist.gd:30-32` — MAJOR — commit 6 (plan line 382) lists `l8_herbalist.gd:32` as a migration target, but the function duplicates the pack (`var carried:=inventory.duplicate()`) and is a pure builder that line 195 says stays "for good" and commit 9 (line 395) names must-stay-clean; the actual live write is the caller's `host.carried_collected=taken.inventory` at `l8_journey.gd:92` (already in table 2.3/commit 5). The 2.2 row (line 153, "appends to the `carried` it is given") is also wrong. A migrator following commit 6 edits a builder the rest of the plan forbids touching.
  - `museum_walkthrough.gd:921-926`, `cave_walkthrough.gd:1184-1240`, `act2_map.gd:338` — MINOR — §3's Save paragraph (plan line 341: "The pack is written where it is today (`inventory.collected` in each area's save...)") is false for the Museum (pack is `checkpoint.collected`; the area save has no `inventory` key) and the Cave (no pack list; ten per-owner keys), and materially incomplete for every Act 2 host, where `inventory_state()` filters act2 ids out of `inventory.collected` into `quests.act2_items.carried`. The commit-9 old-save test's "pack, packet and histories equal field by field" (line 397) inherits this: on act2 hosts the live pack is the union of two saved fields, rebuilt as legacy+`packet.carried` by `act2_items_catalog.gd:117`, so live pack order is not the saved order and the test as literally specified either fails on unmodified code or must be silently reinterpreted.
  - `act2_save.gd:25`, `dragon_level.gd:161`, `act2_jungle_return.gd:37` — MINOR — §1.2 (plan line 40) says the combined 64 limit is checked at ":116, `act2_map.gd:324` and `darker_jungle.gd:274`", missing these three, including `act2_save.gd:25` — the one that actually guards disk saves and legacy loads.
  - `player_item_effects.gd:82` — MINOR — listed in 2.7 (plan line 236) as a removal, but line 71 binds `var pack: Array = inventory.duplicate()` and :82 `remove_at`s the copy; the live write is the caller's assignment at `player_item_controller.gd:130-131`. It is a builder; commit 10 routing it through `ItemGrants.remove` would contradict "builders stay as they are" and change a pure function's contract.
  - `l9_pyre.gd:109,111` — MINOR — listed in 2.8 (plan line 257) as loaders/validators, but those lines are the E-key dispatch calling `urn("retrieve")` / `urn("insert", State.URN)` (`l9_pyre.gd:106-111`); the grant path is the way-C `urn` at :72,74 already in 2.3. The commit-0 census fixture would pin a bogus "loader" kind — the same class of error K95-D caught.
  - `l8_dawn.gd:26`, `l8_larkhon.gd:56`, `l8_tribe.gd:100`, `l10_emperor.gd:68,125`, `l10_priest.gd:77` — MINOR — these copy sites read `host.quest_state.act2_items.duplicate(true)` with no `Items.initial()` fallback, so §3's flagged normalization (plan line 331: "a missing packet no longer raises an error") applies to them too, but the plan flags it only for the "in place" sites; table 2.9's Order column also drops the trailing `Items.sync` for five rows (`l12_citadel.gd:42`, `l8_dawn.gd:30`, `l8_larkhon.gd:59`, `l19_belial_horn.gd:70`, `l19_dawn_curse.gd:246`), inviting a migrator to misplace the sync.
  - `tests/item_grant_history_spelling_test.gd` (plan line 369) — MINOR — "for each 'always' site that can be reached twice from a test ... if one exists": for sites where no double-fire harness exists the row tests nothing and cannot fail, yet commit 9 treats the act2/act2_once split as proven by this test.
  - `act2_items_catalog.gd:95-106` vs plan line 386 — MINOR — `validate`'s duplicate check is per base id, so `act2:<AREA>:grant<N>` and a placement id `act2:<AREA>:itemM` for the same definition coexist happily; the only guard is the 3.1 evidence conditions, and the commit-8 acceptance test ("press E again, still one copy") proves only same-row idempotency, never the definition-level double-grant.
  - `walkthrough_save.gd:246` — MINOR — `migrate_loaded` writes `state.collected = []` (v1→v2), a `collected` write absent from the 2.8 serializer list; benign for the guard (name doesn't match) and no v1 cave fixture exists, but the commit-0 census fixture will rediscover it, and it is a pack-wipe on any v1 cave save. Also `area_world_items.gd`'s history normalization is at `:81`, not the `:79` cited at plan line 268.
  - Plan line 13 — MINOR — "the 295 test files that read them and the 85 that write them": a plain grep finds 299 test files touching the stores and 132 with write-shaped lines (`carried_collected =` / `.append` / `.erase`); method-dependent, but the 85 is likely undercounted and is stated as fact.

  VERDICT: PLAN NEEDS WORK

To resume this session: kimi -r session_c86fd9e0-9edc-468e-840c-c479b57b3d55
