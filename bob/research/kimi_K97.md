• Let me start by reading the handoff and the diff. .../0620-row-2026-11-11-act23-playtest-starts.md   |   1 +
 docs/playtest-starts.md                            |  78 ++--
 scripts/lol2/game_save.gd                          |  12 +
 scripts/lol2/original_game_gate.gd                 |  15 +-
 scripts/lol2/playtest_starts.gd                    |  17 +-
 scripts/lol2/playtest_starts.json                  | 466 ++++++++++++++++++++-
 tests/playtest/map_case.gd                         |  89 ++++
 tests/playtest_checkpoint_adapter_test.gd          |  51 +++
 tests/playtest_map_starts_rendered_test.gd         |   3 +
 tests/playtest_map_starts_test.gd                  |   1 +
 tests/playtest_starts_test.gd                      |   8 +-
 .../registry/playtest_checkpoint_adapter_test.json |  17 +
 .../playtest_map_starts_rendered_test.json         |  20 +
 tests/registry/playtest_map_starts_test.json       |  17 +
 tests/registry/playtest_starts_test.json           |  25 +-
 tools/prepare_playtest_starts.py                   |  19 +-
 tools/regression_source.py                         |   3 +-
 tools/test_prepare_playtest_starts.py              |  27 +-
 tools/validate_playtest_starts.gd                  |   2 +-
 19 files changed, 798 insertions(+), 73 deletions(-)
Let me get the full diff. It's 798 insertions — substantial. Let me read the diff in parts.diff --git a/scripts/lol2/game_save.gd b/scripts/lol2/game_save.gd
index 317ec5f..20ec9c2 100644
--- a/scripts/lol2/game_save.gd
+++ b/scripts/lol2/game_save.gd
@@ -200,6 +200,18 @@ static func load_legacy(tree: SceneTree, area: String) -> String:
 	var doc := {"area":area,"scene":row.scene,"area_save":read.state,"native_bank":{},"play_seconds":0.0,"session":{"options":{"adapter_exit_seeds":true},"last_slot":1}}
 	return _queue_scene(tree,doc,1,true)
 
+## F2 checkpoints are immutable earned area packets. Use the same pending-apply,
+## asset admission and rollback path as slots; no preview/exit seeds are granted.
+static func resume_checkpoint(tree: SceneTree, area: String, state: Dictionary, full_health: bool) -> String:
+	if area not in Areas.PROGRESSION_AREAS: return "Unknown playtest map."
+	var error := Areas.validate_area(area,state)
+	if not error.is_empty(): return error
+	var packet := state.duplicate(true)
+	if full_health: packet.inventory.health = preload("res://scripts/lol2/player_health.gd").MAXIMUM
+	var doc := {"area":area,"scene":Areas.ROWS[area].scene,"area_save":packet,"native_bank":{},"play_seconds":0.0,
+		"session":{"options":{"adapter_exit_seeds":false},"last_slot":1}}
+	return _queue_scene(tree,doc,1,false)
+
 static func _queue_scene(tree: SceneTree, doc: Dictionary, slot_id: int, legacy: bool) -> String:
 	if tree.paused: return "Close the current overlay before loading."
 	if OS.has_feature("original_game_required") and not tree.get_meta("original_game_verified",false): return "Verify the original game files before loading."
diff --git a/scripts/lol2/original_game_gate.gd b/scripts/lol2/original_game_gate.gd
index c91b947..b2b57cb 100644
--- a/scripts/lol2/original_game_gate.gd
+++ b/scripts/lol2/original_game_gate.gd
@@ -207,9 +207,10 @@ func _build_playtest_starts() -> void:
 	column.add_child(heading)
 	var help := Label.new()
 	help.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
-	help.text = "Start at a story point. Each start is a real save earned by the automated playthrough tests and opens through the normal Resume. Your own saves are not changed until you save (F5). F2 or Esc closes this list."
+	help.text = "Story checkpoints earned by automated route tests. Act 2/3 starts restore full health; older checkpoints can reset native puzzles on other maps. Manual slots are kept; normal autosaves apply. F2 or Esc closes this list."
 	column.add_child(help)
 	var scroll := ScrollContainer.new()
+	scroll.follow_focus = true
 	scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
 	scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
 	column.add_child(scroll)
@@ -255,6 +256,18 @@ func start_playtest(id: String) -> void:
 	if not error.is_empty():
 		report.call(error)
 		return
+	if str(entry.resume) == "map":
+		var read := Starts.read(entry)
+		if not read.error.is_empty(): report.call(read.error); return
+		var identity := Starts.identity_error(entry,read.state)
+		if not identity.is_empty(): report.call(identity); return
+		# Recheck the pin after reading, before any session/scene mutation.
+		var pin_error := Starts.file_error(entry)
+		if not pin_error.is_empty(): report.call(pin_error); return
+		if not _verify_save_access().is_empty(): return
+		var resumed: String = preload("res://scripts/lol2/game_save.gd").resume_checkpoint(get_tree(),entry.area_id,read.state,true)
+		if not resumed.is_empty(): report.call(resumed)
+		return
 	var path := Starts.save_path(entry)
 	var kept := [museum_save_path, jungle_save_path, hive_save_path, darker_save_path, dark_halls_save_path]
 	match str(entry.resume):
diff --git a/scripts/lol2/playtest_starts.gd b/scripts/lol2/playtest_starts.gd
index 4ce3b2d..aeafe67 100644
--- a/scripts/lol2/playtest_starts.gd
+++ b/scripts/lol2/playtest_starts.gd
@@ -7,12 +7,13 @@ extends RefCounted
 ## validator, resume meta and scene as a normal resume. Nothing is injected and the player's own quicksaves are not touched.
 const MANIFEST := "res://scripts/lol2/playtest_starts.json"
 const SAVE_DIR := "res://assets/lol2/generated/playtest_starts/"
+const
 Areas = preload("res://scripts/lol2/game_areas.gd")
 const MuseumSave = preload("res://scripts/lol2/museum_save.gd")
 const JungleSave = preload("res://scripts/lol2/jungle_save.gd")
 const HiveSave = preload("res://scripts/lol2/hive_save.gd")
-## Resume kinds = the gate's existing resume branches. A manifest entry with any other kind is refused (Act 2 map saves
-## need a production map-save resume branch first; docs/playtest-starts.md).
+## Fixed Act1 branches and the whole-game checkpoint resume for whitelisted Act2/3 maps.
 const KINDS := {
+	"map": {}, # area_id resolves format/scene through the whole-game area catalog.
 	"museum": {"format": "lol2-restoration-museum", "scene": "res://scenes/lol2/museum_walkthrough.tscn", "area": "Museum"},
 	"jungle": {"format": "lol2-restoration-jungle", "scene": "res://scenes/lol2/jungle_walkthrough.tscn", "area": "Jungle"},
 	"hive": {"format": "lol2-restoration-hive", "scene": "res://scenes/lol2/hive_review.tscn", "area": "Hive"},
@@ -46,6 +47,12 @@ static func entry_error(entry: Variant) -> String:
 	for field in FIELDS:
 		if not entry.has(field): return "missing " + field
 	if not KINDS.has(str(entry.resume)): return "unknown resume kind " + str(entry.resume)
+	if str(entry.resume) == "map":
+		if entry.get("area_id", "") not in Areas.PROGRESSION_AREAS: return "unknown playtest map"
+		var expected_act := 3 if str(entry.area_id) in ["L16_CA","L17_HC","L19_BC","L20_BB"] else 2
+		if entry.get("act") != expected_act: return "map act disagrees with area"
+		if entry.get("full_health") != true: return "map start requires full_health"
+	if entry.has("full_health") and not entry.full_health is bool: return "full_health is not boolean"
 	var save := str(entry.save)
 	if not save.is_valid_filename() or not save.ends_with(".json"): return "unsafe save name"
 	var sha := str(entry.sha256)
@@ -92,6 +99,11 @@ static func identity_error(entry: Dictionary, state: Dictionary) -> String:
 		if not same(at_path(state, str(path)), ids.values[path]): return "%s = %s, expected %s" % [path, at_path(state, str(path)), ids.values[path]]
 	return ""
 
+static func format_for(entry: Dictionary) -> String:
+	return Areas.ROWS[entry.area_id].format if str(entry.resume) == "map" else KINDS[str(entry.resume)].format
+static func scene_for(entry: Dictionary) -> String:
+	return Areas.ROWS[entry.area_id].scene if str(entry.resume) == "map" else KINDS[str(entry.resume)].scene
+
 static func save_path(entry: Dictionary) -> String: return SAVE_DIR + str(entry.save)
 
 ## Staged file present and byte-identical to the manifest pin ("" = ok).
@@ -105,6 +117,7 @@ static func file_error(entry: Dictionary) -> String:
 static func read(entry: Dictionary, path: String = "") -> Dictionary:
 	if path.is_empty(): path = save_path(entry)
 	match str(entry.resume):
+		"map": return load("res://scripts/lol2/game_save.gd").read_legacy(entry.area_id,path)
 		"museum": return MuseumSave.read_save(path)
 		"jungle": return JungleSave.read_save(path)
 		"hive": return HiveSave.read_save(path)
diff --git a/scripts/lol2/playtest_starts.json b/scripts/lol2/playtest_starts.json
index 62154b8..56368b8 100644
--- a/scripts/lol2/playtest_starts.json
+++ b/scripts/lol2/playtest_starts.json
@@ -1,6 +1,6 @@
 {
   "schema": 1,
-  "scope": "Playtest start points (docs/playtest-starts.md). Ordered story checkpoints; each is a REAL earned save written by the automated campaign/route tests, pinned by sha256, with the producing test, its commit, the input save sha256 and the persistent identities the save must carry (identities: contains/excludes = lists that must / must not appear at a dotted path; values = dotted path -> exact value, numbers compared numerically). tools/prepare_playtest_starts.py stages the files into res://assets/lol2/generated/playtest_starts/ (generated, git-ignored); the original-game gate lists the titles and starts one through its existing area-resume branch. resume = museum | jungle | hive | darker | dark_halls (scripts/lol2/playtest_starts.gd KINDS). Act 2 map saves need a production map-save resume branch first (docs/playtest-starts.md).",
+  "scope": "SHA256-pinned game-written campaign/earned-route checkpoints. Act2/3 map starts use Plan3 checkpoint resume, disable preview seeds and set full health on a detached copy. Some producer tests have disclosed aids; no unaided whole-campaign claim. Original bytes/quest/items/poses remain unchanged.",
   "entries": [
     {
       "id": "act1-museum-arrival",
@@ -414,6 +414,470 @@
           "quests.act_one_departure.local55": 1
         }
       }
+    },
+    {
+      "id": "act2-l8",
+      "title": "Act 2 - Savage Jungle, arrival (full health)",
+      "act": 2,
+      "area": "Savage Jungle",
+      "resume": "map",
+      "save": "c15_l8_sj.json",
+      "sha256": "9606beab57fdb8d246e3f322ba328a1ae965dba1027dda7b4eef5cb55d4c6425",
+      "full_health": true,
+      "source": {
+        "test": "dark_halls_earned_detour_test",
+        "commit": "1b775ba8cee72ebee1da4c6cb0f807be6f4d8c9a",
+        "campaign": "r12z qualification campaign 2026-11-02 (AI_COMMS/act1_completion_20261017/r12z_qualification, source 1b775ba)",
+        "leg": "11-13_dark_halls",
+        "proof": "AI_COMMS/act1_completion_20261017/r12z_qualification/campaign/userdata/dark_halls_earned/depart.json (kept output depart_output_darker_arrival.json has this sha256); audit_dark_halls_detour_chain.txt PASS",
+        "path": "~/AI_COMMS/act1_completion_20261017/r12z_qualification/campaign/userdata/act1_dark_halls_darker_arrival.json",
+        "input_save": "~/AI_COMMS/act1_completion_20261017/r12z_qualification/campaign/userdata/dark_halls_earned/finish_output_jungle_quicksave.json",
+        "input_sha256": "3eb93c33de97fbfc631b7aaffd356b985e8cd98f41bed513fb80656a576a846b",
+        "input_note": "phase depart resumed the phase-finish F5 Jungle save; the detour chain started from act1_broken_repaired_monastery.json (ee4a4e45...)",
+        "scope": "Original qualified Act1 departure checkpoint reused byte-for-byte; no unaided whole-campaign claim added."
+      },
+      "identities": {
+        "contains": {
+          "inventory.collected": [
+            "jungle:magic_shop:Tho_fixed",
+            "darkhalls:control968u1:HlScrl",
+            "darkhalls:control968u2:HlScrl",
+            "darkhalls:control971u1:Prsmscrl"
+          ]
+        },
+        "excludes": {
+          "inventory.collected": [
+            "museum:control181:Tho_Broken"
+          ]
+        },
+        "values": {
+          "quests.monastery.globals.GV_LUTHERS_SOUL": 8,
+          "quests.monastery.globals.GV_RIX_DEAD": 0,
+          "quests.dark_halls_windows.done": true,
+          "quests.act_one_departure.phase": "arrived",
+          "quests.act_one_departure.local55": 1
+        }
+      },
+      "area_id": "L8_SJ"
+    },
+    {
+      "id": "act2-l9",
+      "title": "Act 2 - Dracoid Ruins, pit arrival (full health)",
+      "act": 2,
+      "area": "Dracoid Ruins",
+      "area_id": "L9_DR",
+      "resume": "map",
+      "save": "c15_l9_dr.json",
+      "sha256": "02de1113c40d183c3fdd780f205d4c41643a7df6149b857bc68d8f21b5375eda",
+      "full_health": true,
+      "source": {
+        "test": "l8_pit_earned_test",
+        "commit": "fc1b45c2c44c921e86b8a665dd299593c6f3b6df",
+        "input_sha256": "3373d698a0deb9c8a615ee0b092dd0141de8403f7365ee10fb8faffceb228add",
+        "path": "~/AI_COMMS/astra_lane/packup_20261103T122345Z/earned_saves_and_drafts.tar.gz",
+        "proof": "~/AI_COMMS/astra_lane/packup_20261103T122345Z/final_qualification/report.json",
+        "proof_sha256": "f75577355f3cb1eaf8c101435aa63afb0d6797a75d74b4316aaa402194345224",
+        "scope": "Qualified game-written earned-route checkpoint; not an unaided campaign chain.",
+        "test_aids": [
+          "Clock/camera ownership and production action helper calls; grounded route movement. See pinned producer source."
+        ],
+        "archive_member": "tmp/l9_pit_arrival_earned_save.json",
+        "archive_manifest_sha256": "976d6e10db6633e35d084796cf355f8f225d711810f29b158bf15d63dba2af38",
+        "input_member": "tmp/l8_pit_rim_earned_save.json"
+      },
+      "identities": {
+        "contains": {
+          "inventory.collected": [
+            "cave:prop641:harvest1:Stalagmite",
+            "cave:captain:Short_Sword"
+          ],
+          "quests.act2_items.carried": [
+            "act2:L10_DC:item44:charged:yellow"
+          ]
+        },
+        "excludes": {},
+        "values": {
+          "format": "lol2-restoration-dragon-preview",
+          "player.position": [
+            81.0,
+            44.79999923706055,
+            603.0
+          ]
+        }
+      }
+    },
+    {
+      "id": "act2-l10",
+      "title": "Act 2 - Cemetery, main gate opened (full health)",
+      "act": 2,
+      "area": "Cemetery",
+      "area_id": "L10_DC",
+      "resume": "map",
+      "save": "c15_l10_dc.json",
+      "sha256": "6f9d174047977927af32457ccbb2e9df1ef332974e02b7adcf915854d25ea49f",
+      "full_health": true,
+      "source": {
+        "test": "l10_gate_earned_test",
+        "commit": "fc1b45c2c44c921e86b8a665dd299593c6f3b6df",
+        "input_sha256": "065d4b814569c069490c0b4625177862918b2798ea504acf6ae89172b83baa92",
+        "path": "~/AI_COMMS/astra_lane/packup_20261103T122345Z/earned_saves_and_drafts.tar.gz",
+        "proof": "~/AI_COMMS/astra_lane/packup_20261103T122345Z/final_qualification/report.json",
+        "proof_sha256": "f75577355f3cb1eaf8c101435aa63afb0d6797a75d74b4316aaa402194345224",
+        "scope": "Qualified game-written earned-route checkpoint; not an unaided campaign chain.",
+        "test_aids": [
+          "Clock/camera ownership and production action helper calls; grounded route movement. See pinned producer source."
+        ],
+        "archive_member": "tmp/l10_gate_earned_save.json",
+        "archive_manifest_sha256": "976d6e10db6633e35d084796cf355f8f225d711810f29b158bf15d63dba2af38",
+        "input_witness": "tests/l8_gift_earned_test.gd INPUT/HASH (r12w earned Act1 departure)"
+      },
+      "identities": {
+        "contains": {
+          "inventory.collected": [
+            "cave:prop641:harvest1:Stalagmite",
+            "cave:captain:Short_Sword"
+          ]
+        },
+        "excludes": {},
+        "values": {
+          "format": "lol2-restoration-map-L10_DC",
+          "player.position": [
+            -115.85588073730469,
+            45.99988555908203,
+            -1002.9994506835938
+          ]
+        }
+      }
+    },
+    {
+      "id": "act2-l12",
+      "title": "Act 2 - Claw Mountains, Larkhon arrival (full health)",
+      "act": 2,
+      "area": "Claw Mountains",
+      "area_id": "L12_CM",
+      "resume": "map",
+      "save": "c15_l12_cm.json",
+      "sha256": "689badf57fb9f5bb34dad52c98a76026868bac407013b04ec40fcec56a1f38b5",
+      "full_health": true,
+      "source": {
+        "test": "l8_larkhon_earned_test",
+        "commit": "fc1b45c2c44c921e86b8a665dd299593c6f3b6df",
+        "input_sha256": "02cfe975f0e0dcf98e60d23b4b9e403ef2ce701f200c01115be704568c0c58f6",
+        "path": "~/AI_COMMS/astra_lane/packup_20261103T122345Z/earned_saves_and_drafts.tar.gz",
+        "proof": "~/AI_COMMS/astra_lane/packup_20261103T122345Z/final_qualification/report.json",
+        "proof_sha256": "f75577355f3cb1eaf8c101435aa63afb0d6797a75d74b4316aaa402194345224",
+        "scope": "Qualified game-written earned-route checkpoint; not an unaided campaign chain.",
+        "test_aids": [
+          "Clock/camera ownership and production action helper calls; grounded route movement. See pinned producer source."
+        ],
+        "archive_member": "tmp/l12_larkhon_arrival_earned_save.json",
+        "archive_manifest_sha256": "976d6e10db6633e35d084796cf355f8f225d711810f29b158bf15d63dba2af38",
+        "input_witness": "fc1b45c tests/l8_larkhon_earned_test.gd immutable02cfe975... input equality; qualified input is not included in the pack-up tar."
+      },
+      "identities": {
+        "contains": {
+          "inventory.collected": [
+            "cave:prop641:harvest1:Stalagmite",
+            "cave:captain:Short_Sword"
+          ],
+          "quests.act2_items.carried": [
+            "act2:L8_SJ:dawn_control_token",
+            "act2:L10_DC:silverleaf167"
+          ]
+        },
+        "excludes": {},
+        "values": {
+          "format": "lol2-restoration-map-L12_CM",
+          "player.position": [
+            -344.6979064941406,
+            -30.678823471069336,
+            -5603.11962890625
+          ]
+        }
+      }
+    },
+    {
+      "id": "act2-l13",
+      "title": "Act 2 - Citadel of the Ruloi, arrival (full health)",
+      "act": 2,
+      "area": "Citadel of the Ruloi",
+      "area_id": "L13_RC",
+      "resume": "map",
+      "save": "c15_l13_rc.json",
+      "sha256": "21db5d3f9596650ad96df594e103eca6eb79dea299d91e585e610b146622b948",
+      "full_health": true,
+      "source": {
+        "test": "l12_citadel_earned_test",
+        "commit": "fc1b45c2c44c921e86b8a665dd299593c6f3b6df",
+        "input_sha256": "8611777502d189ccbcf3f7d8a2d4c95a98133d16d7e77eac827d51bbb2c4f79a",
+        "path": "~/AI_COMMS/astra_lane/packup_20261103T122345Z/earned_saves_and_drafts.tar.gz",
+        "proof": "~/AI_COMMS/astra_lane/packup_20261103T122345Z/final_qualification/report.json",
+        "proof_sha256": "f75577355f3cb1eaf8c101435aa63afb0d6797a75d74b4316aaa402194345224",
+        "scope": "Qualified game-written earned-route checkpoint; not an unaided campaign chain.",
+        "test_aids": [
+          "Clock/camera ownership and production action helper calls; grounded route movement. See pinned producer source."
+        ],
+        "archive_member": "tmp/l13_citadel_arrival_earned_save.json",
+        "archive_manifest_sha256": "976d6e10db6633e35d084796cf355f8f225d711810f29b158bf15d63dba2af38",
+        "input_member": "tmp/l12_gulch_qualified_save.json"
+      },
+      "identities": {
+        "contains": {
+          "inventory.collected": [
+            "cave:prop641:harvest1:Stalagmite",
+            "cave:captain:Short_Sword"
+          ],
+          "quests.act2_items.carried": [
+            "act2:L8_SJ:dawn_control_token",
+            "act2:L10_DC:silverleaf167"
+          ]
+        },
+        "excludes": {},
+        "values": {
+          "format": "lol2-restoration-map-L13_RC",
+          "player.position": [
+            -3260.0,
+            32.0,
+            6631.0
+          ]
+        }
+      }
+    },
+    {
+      "id": "act2-l14",
+      "title": "Act 2 - Huline Temple, arrival (full health)",
+      "act": 2,
+      "area": "Huline Temple",
+      "area_id": "L14_HT",
+      "resume": "map",
+      "save": "c15_l14_ht.json",
+      "sha256": "761850f60b460772b31566ff0eb4201caba6e3d6d120ccc590bc64addb317c2f",
+      "full_health": true,
+      "source": {
+        "test": "l8_temple_door_earned_test",
+        "commit": "fc1b45c2c44c921e86b8a665dd299593c6f3b6df",
+        "input_sha256": "38782a29b9e87b96a48fd64e08b18a98f9f3974a1b0542cb7c7cacec67e6ef56",
+        "path": "~/AI_COMMS/astra_lane/packup_20261103T122345Z/earned_saves_and_drafts.tar.gz",
+        "proof": "~/AI_COMMS/astra_lane/packup_20261103T122345Z/final_qualification/report.json",
+        "proof_sha256": "f75577355f3cb1eaf8c101435aa63afb0d6797a75d74b4316aaa402194345224",
+        "scope": "Qualified game-written earned-route checkpoint; not an unaided campaign chain.",
+        "test_aids": [
+          "Clock/camera ownership and production action helper calls; grounded route movement. See pinned producer source."
+        ],
+        "archive_member": "tmp/l14_temple_arrival_earned_save.json",
+        "archive_manifest_sha256": "976d6e10db6633e35d084796cf355f8f225d711810f29b158bf15d63dba2af38",
+        "input_member": "tmp/l8_river_return_qualified_save.json"
+      },
+      "identities": {
+        "contains": {
+          "inventory.collected": [
+            "cave:prop641:harvest1:Stalagmite",
+            "cave:captain:Short_Sword"
+          ],
+          "quests.act2_items.carried": [
+            "act2:L8_SJ:dawn_control_token",
+            "act2:L10_DC:silverleaf167"
+          ]
+        },
+        "excludes": {},
+        "values": {
+          "format": "lol2-restoration-map-L14_HT",
+          "player.position": [
+            2406.712158203125,
+            32.03944778442383,
+            -2415.70458984375
+          ]
+            "act2:L10_DC:silverleaf169"
+          ]
+        },
+        "excludes": {},
+        "values": {
+          "format": "lol2-restoration-map-L19_BC",
+          "player.position": [
+            84.0,
+            22.0,
+            80.0
+          ]
+        }
+      }
+    },
+    {
+      "id": "act3-l20",
+      "title": "Act 3 - Birthing Chamber, after birth (full health)",
+      "act": 3,
+      "area": "Birthing Chamber",
+      "area_id": "L20_BB",
+      "resume": "map",
+      "save": "c15_l20_bb.json",
+      "sha256": "576d17bb004fd11521770ffbc6a125cb6925806df508442c3ab44c7e408a43e5",
+      "full_health": true,
+      "source": {
+        "test": "l19_dawn_curse_earned_test",
+        "commit": "97dce7eb4c676a64798762b81cb5ff9f7f51d867",
+        "input_sha256": "5208e4bb2be46d7a472c41ab31edc3a290467462ab23be08b721c2b0c460f6ee",
+        "path": "~/opus_work/lol2_r18/tmp/l20_dawn_curse_earned_save.json",
+        "proof": "~/opus_work/lol2_r18/tmp/regressions/merge_97dce7e/report.json",
+        "proof_sha256": "f835c02686e0d0bb7290d87d3b1316efdeed8889ab340e3b287944d9c4452b62",
+        "scope": "Qualified game-written earned-route checkpoint; not an unaided campaign chain.",
+        "test_aids": [
+          "Inherited clock/camera ownership and local position/transition aids; see pinned producer source.",
+          "Native first-visit index52=0 supplied for the L19-to-L20 predicate; mother.cast_level4/5 refusal probe and birth-skip clock. Packet is after birth, not initial L20 arrival."
+        ],
+        "input_path": "~/opus_work/lol2_r18/tmp/l19_ghostly_heads_earned_save.json",
+        "input_mtime_utc": "2026-11-09T23:25:13.133449+00:00",
+        "output_mtime_utc": "2026-11-10T04:46:52.666653+00:00"
+      },
+      "identities": {
+        "contains": {
+          "inventory.collected": [
+            "cave:prop641:harvest1:Stalagmite",
+            "cave:captain:Short_Sword"
+          ],
+          "quests.act2_items.carried": [
+            "act2:L8_SJ:dawn_control_token",
+            "act2:L10_DC:silverleaf169"
+          ]
+        },
+        "excludes": {},
+        "values": {
+          "format": "lol2-restoration-map-L20_BB",
+          "player.position": [
+            -1382.0,
+            -106.6637191772461,
+            -3213.0
+          ]
+        }
+      }
     }
   ]
 }
I missed some JSON entries in between (act2-l16, act2-l17, act2-l19 presumably, plus the middle of the file). Let me get the full new JSON entries list and check details. Let me see the diff range between 200-420 of that diff output.+          "quests.act2_items.carried": [
+            "act2:L8_SJ:dawn_control_token",
+            "act2:L10_DC:silverleaf167"
+          ]
+        },
+        "excludes": {},
+        "values": {
+          "format": "lol2-restoration-map-L13_RC",
+          "player.position": [
+            -3260.0,
+            32.0,
+            6631.0
+          ]
+        }
+      }
+    },
+    {
+      "id": "act2-l14",
+      "title": "Act 2 - Huline Temple, arrival (full health)",
+      "act": 2,
+      "area": "Huline Temple",
+      "area_id": "L14_HT",
+      "resume": "map",
+      "save": "c15_l14_ht.json",
+      "sha256": "761850f60b460772b31566ff0eb4201caba6e3d6d120ccc590bc64addb317c2f",
+      "full_health": true,
+      "source": {
+        "test": "l8_temple_door_earned_test",
+        "commit": "fc1b45c2c44c921e86b8a665dd299593c6f3b6df",
+        "input_sha256": "38782a29b9e87b96a48fd64e08b18a98f9f3974a1b0542cb7c7cacec67e6ef56",
+        "path": "~/AI_COMMS/astra_lane/packup_20261103T122345Z/earned_saves_and_drafts.tar.gz",
+        "proof": "~/AI_COMMS/astra_lane/packup_20261103T122345Z/final_qualification/report.json",
+        "proof_sha256": "f75577355f3cb1eaf8c101435aa63afb0d6797a75d74b4316aaa402194345224",
+        "scope": "Qualified game-written earned-route checkpoint; not an unaided campaign chain.",
+        "test_aids": [
+          "Clock/camera ownership and production action helper calls; grounded route movement. See pinned producer source."
+        ],
+        "archive_member": "tmp/l14_temple_arrival_earned_save.json",
+        "archive_manifest_sha256": "976d6e10db6633e35d084796cf355f8f225d711810f29b158bf15d63dba2af38",
+        "input_member": "tmp/l8_river_return_qualified_save.json"
+      },
+      "identities": {
+        "contains": {
+          "inventory.collected": [
+            "cave:prop641:harvest1:Stalagmite",
+            "cave:captain:Short_Sword"
+          ],
+          "quests.act2_items.carried": [
+            "act2:L8_SJ:dawn_control_token",
+            "act2:L10_DC:silverleaf167"
+          ]
+        },
+        "excludes": {},
+        "values": {
+          "format": "lol2-restoration-map-L14_HT",
+          "player.position": [
+            2406.712158203125,
+            32.03944778442383,
+            -2415.70458984375
+          ]
+        }
+      }
+    },
+    {
+      "id": "act3-l16",
+      "title": "Act 3 - City of the Ancients, arrival (full health)",
+      "act": 3,
+      "area": "City of the Ancients",
+      "area_id": "L16_CA",
+      "resume": "map",
+      "save": "c15_l16_ca.json",
+      "sha256": "f2c469da0b4a477c3f6aa391d2a313993ce1a1ef6d5eb44ff3cbc3e28c771ccb",
+      "full_health": true,
+      "source": {
+        "test": "l14_chamber_voices_earned_test",
+        "commit": "b3e384ed90df4b900c5ee45f160847fe6571af11",
+        "input_sha256": "5e9533fb4636329c424cd6972cbedb41eb6b5c9e6170640d357860193eef7ace",
+        "path": "~/opus_work/lol2_r18/tmp/l16_arrival_earned_save.json",
+        "proof": "~/opus_work/lol2_r18/tmp/regressions/doors/report.json",
+        "proof_sha256": "9c22b4bdbeb8112ac3c2514c4dfdcaa8099a1af6389f0844d7fc827d4b065a51",
+        "scope": "Qualified game-written earned-route checkpoint; not an unaided campaign chain.",
+        "test_aids": [
+          "Clock/camera ownership, production action calls and explicitly stepped transition; route movement remains physical."
+        ],
+        "input_path": "~/opus_work/lol2_r18/tmp/l14_belial_combat_qualified_save.json",
+        "input_mtime_utc": "2026-11-03T05:57:19.791397+00:00",
+        "output_mtime_utc": "2026-11-09T23:15:54.046689+00:00"
+      },
+      "identities": {
+        "contains": {
+          "inventory.collected": [
+            "cave:prop641:harvest1:Stalagmite",
+            "cave:captain:Short_Sword"
+          ],
+          "quests.act2_items.carried": [
+            "act2:L8_SJ:dawn_control_token",
+            "act2:L10_DC:silverleaf167"
+          ]
+        },
+        "excludes": {},
+        "value
s": {
+          "format": "lol2-restoration-map-L16_CA",
+          "player.position": [
+            -3860.0,
+            32.0,
+            -1341.0
+          ]
+        }
+      }
+    },
+    {
+      "id": "act3-l17",
+      "title": "Act 3 - Huline Caverns, arrival (full health)",
+      "act": 3,
+      "area": "Huline Caverns",
+      "area_id": "L17_HC",
+      "resume": "map",
+      "save": "c15_l17_hc.json",
+      "sha256": "678e3076befc3ff44ab183353448f1a664f99f900a33a14c8ad191622d411839",
+      "full_health": true,
+      "source": {
+        "test": "l16_exit_earned_test",
+        "commit": "b3e384ed90df4b900c5ee45f160847fe6571af11",
+        "input_sha256": "4e56745b3a90c94ffbce317dece089fdd70880a2643cb89f1a90d83bf04538a3",
+        "path": "~/opus_work/lol2_r18/tmp/l17_arrival_earned_save.json",
+        "proof": "~/opus_work/lol2_r18/tmp/regressions/doors/report.json",
+        "proof_sha256": "9c22b4bdbeb8112ac3c2514c4dfdcaa8099a1af6389f0844d7fc827d4b065a51",
+        "scope": "Qualified game-written earned-route checkpoint; not an unaided campaign chain.",
+        "test_aids": [
+          "Clock/camera ownership, production action calls and explicitly stepped transition; route movement remains physical."
+        ],
+        "input_path": "~/opus_work/lol2_r18/tmp/l16_se_oil_chain_earned_save.json",
+        "input_mtime_utc": "2026-11-10T00:01:13.516751+00:00",
+        "output_mtime_utc": "2026-11-10T00:07:42.578549+00:00"
+      },
+      "identities": {
+        "contains": {
+          "inventory.collected": [
+            "cave:prop641:harvest1:Stalagmite",
+            "cave:captain:Short_Sword"
+          ],
+          "quests.act2_items.carried": [
+            "act2:L8_SJ:dawn_control_token",
+            "act2:L10_DC:silverleaf167"
+          ]
+        },
+        "excludes": {},
+        "values": {
+          "format": "lol2-restoration-map-L17_HC",
+          "player.position": [
+            1434.0,
+            32.0,
+            -7075.0
+          ]
+        }
+      }
+    },
+    {
+      "id": "act3-l19",
+      "title": "Act 3 - Belial\u2019s Laboratory, after the beast (full health)",
+      "act": 3,
+      "area": "Belial\u2019s Laboratory",
+      "area_id": "L19_BC",
+      "resume": "map",
+      "save": "c15_l19_bc.json",
+      "sha256": "f2cdf6b46a4701cc06a8987899f1510059f42eb4bc0400dd9a7e65fcf0017755",
+      "full_health": true,
+      "source": {
+        "test": "l19_beast_wall_earned_test",
+        "commit": "b3e384ed90df4b900c5ee45f160847fe6571af11",
+        "input_sha256": "4324651bc76cafc58f440a5098e501590b1510e42d37e8d21f7d8023e141743e",
+        "path": "~/opus_work/lol2_r18/tmp/l19_beast_wall_earned_save.json",
+        "proof": "~/opus_work/lol2_r18/tmp/regressions/doors/report.json",
+        "proof_sha256": "9c22b4bdbeb8112ac3c2514c4dfdcaa8099a1af6389f0844d7fc827d4b065a51",
+        "scope": "Qualified game-written earned-route checkpoint; not an unaided campaign chain.",
+        "test_aids": [
+          "Inherited clock/camera ownership and local position/transition aids; see pinned producer source."
+        ],
+        "input_path": "~/opus_work/lol2_r18/tmp/l17_beast_blade_earned_save.json",
+        "input_mtime_utc": "2026-11-09T14:19:26.825932+00:00",
+        "output_mtime_utc": "2026-11-09T23:24:09.954126+00:00"
+      },
+      "identities": {
+        "contains": {
+          "inventory.collected": [
+            "cave:prop641:harvest1:Stalagmite",
+            "cave:captain:Short_Sword"
+          ],
+          "quests.act2_items.carried": [
+            "act2:L8_SJ:dawn_control_token",
+            "act2:L10_DC:silverleaf169"
Now let me look at the rest of the diff: tests, tools, docs. And check the key code paths more carefully. Let me get the rest of the diff.diff --git a/docs/deviations/0620-row-2026-11-11-act23-playtest-starts.md b/docs/deviations/0620-row-2026-11-11-act23-playtest-starts.md
new file mode 100644
index 0000000..6347906
--- /dev/null
+++ b/docs/deviations/0620-row-2026-11-11-act23-playtest-starts.md
@@ -0,0 +1 @@
+| 2026-11-11 | C-15 Act2/3 F2 checkpoint starts | Ten SHA256-pinned, game-written earned-test checkpoints join the F2 list. The gate uses Plan3 area validation/pending apply/asset guards/rollback, disables preview seeds and sets the existing30 full-health value on a detached packet only. Source files, pack/equipment/mana/progression and saved horizontal position remain; ordinary loads retain health. L20 is explicitly after birth, not its initial arrival. | Owner C-15; lead accepts disclosed test aids. Foundation stack on5ac1bca, not Thursday r19. Producer commits/input hashes/identity pins/proof references and inherited route-test clock/camera/action/position/transition aids are disclosed; no unaided campaign/native-transition claim. No raw checkpoint edits or invented items/quests/poses; legacy files cannot restore an absent visited-level native bank. All10 direct F2 starts and three rendered starts are targeted load/UI proofs, not new earned walks. Existing11 Act1 entries remain; U-06 later moves F2 into debug mode. | Owner-set playtest health adapter; immutable qualified checkpoint content |
diff --git a/docs/playtest-starts.md b/docs/playtest-starts.md
index bd4ea45..63f866f 100644
--- a/docs/playtest-starts.md
+++ b/docs/playtest-starts.md
@@ -1,62 +1,40 @@
 # Playtest starts
 
-Start the game at a story checkpoint instead of replaying hours. Each start is a **real earned save** written by the automated campaign/route tests (no hand-made state), pinned by sha256. This is a dev/playtest convenience. It changes no Classic gameplay, so it has no DEVIATIONS row.
+At the opening screen, press **F2** or choose **Playtest starts (F2)**. The list contains11 existing Act1 points and10 Act2/3 checkpoints. F2 or Esc closes it. The scrollable list follows the UI size setting. Under the later U-06 task these starts move into debug mode; C-15 retains the current F2 entry point.
 
-## Using it
+Act2/3 starts restore Luther to the existing full-health value (**30** on this foundation branch), on a detached copy of the loaded state. The pinned file is never healed or rewritten. Pack, equipment, mana, fighting/magic progression and saved position remain from that checkpoint; normal gravity may settle the saved height. Plain area/slot loads retain their saved health. Among the older Act1 entries, only the previously approved end-of-Act1 darker start has its existing full-health flag.
 
-At the opening screen (the original-game gate), press **F2** or click **Playtest starts (F2)**. A plain list of titles appears in story order. Pick one to start there. **F2** or **Esc** closes the list. The list text follows the UI size setting (150% by default).
+| Act | Level | Checkpoint |
+| --- | --- | --- |
+| 2 | L8_SJ | Savage Jungle arrival, after the Dark Halls |
+| 2 | L9_DR | Dracoid Ruins, pit arrival |
+| 2 | L10_DC | Cemetery, main gate opened |
+| 2 | L12_CM | Claw Mountains, Larkhon arrival |
+| 2 | L13_RC | Citadel of the Ruloi, arrival |
+| 2 | L14_HT | Huline Temple, arrival |
+| 3 | L16_CA | City of the Ancients, arrival |
+| 3 | L17_HC | Huline Caverns, arrival |
+| 3 | L19_BC | Belial's Laboratory, after the beast |
+| 3 | L20_BB | Birthing Chamber, after birth |
 
-- The game opens the save through the gate's normal area resume ("Resume museum / jungle / Hive / darker jungle / Dark Halls"). It uses the same reader, validator, resume meta and scene. The only change is that the save path for that one call is the staged `res://` file.
-- Your own quicksaves are not read or changed. Pressing F5 afterwards saves to the normal area quicksave, as always.
-- `--playtest-starts` (after `--`) opens the list at launch. Without it, a fresh profile with a remembered LOLG.EXE goes straight into the Cave, as before. `--playtest-start=ID` starts one entry directly.
+Each file is an actual game-written save from a qualified campaign/earned-route test, copied byte-for-byte and pinned by SHA256. These are **earned test checkpoints, not an unaided whole-campaign chain**. The manifest records producing test/commit, input SHA, qualification proof and inherited aids. Earlier route tests own clocks/camera and invoke production action helpers. The lead explicitly accepts disclosed test aids for these starts. Some late tests use local position/transition aids; the L20 producer supplies native first-visit index52=0 to exercise the unresolved transition and steps the birth clock. These aids are disclosed rather than relabeled as player-earned native evidence. No checkpoint state, item, quest flag or pose is synthesized by C-15. Full health is its only new start-state adapter.
 
-## Files
+The first five new non-L8 saves come from the immutable Astra pack-up manifest and successful producer rows at `fc1b45c`. Late arrivals come from source-stable reports whose tracked inputs match `b3e384e` (City/Caverns/L19) or `97dce7e` (L20). L8 reuses the existing pinned end-of-Act1 packet under a distinct staged filename. Exact references/hashes live in `scripts/lol2/playtest_starts.json`; the qualification handoff preserves the source comparisons.
 
-| File | Role |
-| --- | --- |
-| `scripts/lol2/playtest_starts.json` | Committed manifest: ordered `{id, title, act, area, resume, save, sha256, source, identities}` |
-| `scripts/lol2/playtest_starts.gd` | Manifest loader, resume kinds (`museum`, `jungle`, `hive`, `darker`, `dark_halls`), sha check, game reader per kind |
-| `scripts/lol2/original_game_gate.gd` | Button, F2 list, `start_playtest(id)` |
-| `assets/lol2/generated/playtest_starts/` | Staged saves (generated, git-ignored). Exported through the `assets/*.json` include filter |
-| `tools/prepare_playtest_starts.py` | Producer: copy, sha check, game validation, stage |
-| `tools/validate_playtest_starts.gd` | Godot side of the producer's validation |
-| `tests/playtest_starts_test.gd` | Headless test: staged, pinned, valid, and every entry resumes into its scene at the saved position |
+The gate reads the pin-checked area file through its existing validator, checks saved identities, verifies the original executable, then calls `game_save.resume_checkpoint`. This uses Plan3's normal pending apply, asset admission and failed-load rollback. Preview/exit seeds are disabled. There is no default-map preview masquerading as a checkpoint. The old files predate the whole-game native bank: their legacy limitation remains, so native puzzles on other maps may reset. C-15 does not invent missing VM history. F5 afterwards writes a normal whole-game slot with the current native state. Selecting a start never writes a manual slot or the pinned source. Ordinary eligible map-entry/timer autosaves follow the existing Plan3 policy and can replace the autosave slot.
 
-## Staging (after a fresh checkout or a new campaign)
+## Staging and adding entries
 
-```
-python3 tools/prepare_playtest_starts.py \
-  --from ~/AI_COMMS/act1_completion_20261017/r12z_qualification/campaign/userdata \
-  --godot tmp/godot_host_starts.sh
-```
-
-The tool refuses, with exit 1 and nothing staged, in these cases:
-
-- an id that is not in the manifest;
-- a missing file;
-- a file whose sha256 differs from its pin;
-- a file the game's own validator rejects.
-
-Rows whose file is not staged show "(not in this build)" and cannot be chosen.
+- Manifest: `scripts/lol2/playtest_starts.json`, schema1. Generated saves: `assets/lol2/generated/playtest_starts/`, exported through the existing JSON include filter.
+- New map entries use `resume: "map"`, a whitelisted `area_id` from `game_areas.gd`, its correct act, and `full_health: true`. Original fixed Act1 resume kinds remain supported.
+- `python3 tools/prepare_playtest_starts.py --describe FILE` prints the SHA/format/template. Pin `source.test`, the full producing `source.commit`, and `source.input_sha256` (null only for a real new-game leg), plus useful saved identities. Preserve/disclose a
ny producer aids and the exact story phase.
+- Collect the original pinned bytes under their manifest filenames in a prepared donor folder. Run:
 
-## Adding entries (Act 2 after r13)
-
-1. Run `python3 tools/prepare_playtest_starts.py --describe FILE`. It prints the sha256, the format, the resume kind and a skeleton for the fields below.
-2. Append an entry to `scripts/lol2/playtest_starts.json` in story order. Every entry must pin:
-   - `sha256` of the save;
-   - `source.test` (the producing test) and `source.commit` (the full 40-hex commit it ran on);
-   - `source.input_sha256`: the sha256 of the save that leg started from (`null` only for a new-game leg). Astra's `*_qualified_save.json` files already record their input sha; copy it;
-   - `identities`: the persistent identities the save must carry at that point. `contains` and `excludes` map a dotted path (for example `inventory.collected`) to values that must or must not be in that list. `values` maps a dotted path (for example `quests.monastery.globals.GV_HAS_RUNES`) to an exact value; numbers are compared numerically.
-
-   The manifest loader refuses an entry that is missing any of these fields. The producer and the test check `identities` against the save's contents.
-3. Stage it with `--from DIR --only ID`, then run `tests/playtest_starts_test.gd`. Update its expected entry count.
-
-Astra's Act 2 saves (`~/opus_work/lol2_astraprogression/tmp/*_qualified_save.json`) mostly have the format `lol2-restoration-map-<AREA>`. r12z has **no** gate resume branch for map saves: map packs only start at their arrival as a "Preview". `--describe` therefore reports them as UNSUPPORTED, and the manifest refuses any unknown `resume` kind. Once r13 brings the Act 2 code, add the following:
-
-- a production map-save resume branch in the gate. For example, read with `act2_save.gd` and the area's format, then set a resume meta that `act2_map.gd` applies through its own `apply_save`/load path, the same way as the other areas;
-- a `map` kind in `playtest_starts.gd` `KINDS`, which needs the scene from `act2_maps.json`, plus `KIND_BY_FORMAT` in the producer;
-- the entries themselves.
+```sh
+python3 tools/prepare_playtest_starts.py --from /path/to/pinned-files \
+  --godot "python3 ~/AI_COMMS/sol_lane/task3_20261109/guarded_godot.py"
+```
 
-Saves in an existing format (for example `l12_gulch_return_qualified_save.json`, `lol2-restoration-darker-jungle`) need only the entry, but only on a build that has the Act 2 code they were earned with.
+The tool validates every selected file through the game's own reader before staging anything. Wrong IDs, missing files, altered bytes, unsafe names, bad map/act/health metadata, wrong formats or wrong saved identities refuse. `--only ID` limits staging; `--dry-run` validates without staging. Unstaged/changed pins disable the corresponding F2 row.
 
-`full_health` (optional, boolean): the start raises Luther to full health without changing the pinned save. Used only by the F2 darker start (owner 2026-11-10, ledger 0553).
+C-15 qualification uses private profiles/displays and the sole memory/count/Dummy launcher. `playtest_map_starts_test` exercises all10 by actual F2/Enter; `playtest_map_starts_rendered_test` starts the Cemetery, City and L19 with list/scene images. The adapter test checks copy-only healing, no-heal/ordinary-slot controls and refusal cases. The private tests disable autosave and hold post-apply clocks for load comparisons; these tests do not earn new walking evidence. Existing11 Act1 starts and the old darker/full-health distinction remain affected checks. Registry counts are audited source sites, not executions. No broad campaign sweep is required.
diff --git a/tests/playtest/map_case.gd b/tests/playtest/map_case.gd
new file mode 100644
index 0000000..4568fb6
--- /dev/null
+++ b/tests/playtest/map_case.gd
@@ -0,0 +1,89 @@
+extends SceneTree
+## C-15 load/UI proof only: immutable earned-test checkpoints, no walking claim.
+const Starts = preload("res://scripts/lol2/playtest_starts.gd")
+const Session = preload("res://scripts/lol2/game_session.gd")
+const Health = preload("res://scripts/lol2/player_health.gd")
+var results := []
+func rendered() -> bool: return false
+func areas() -> Array: return Starts.Areas.PROGRESSION_AREAS
+func _initialize() -> void: run.call_deferred()
+func tap(code: Key) -> void:
+	for down in [true,false]:
+		var event := InputEventKey.new(); event.keycode=code; event.physical_keycode=code; event.pressed=down
+		Input.parse_input_event(event); Input.flush_buffered_events(); await process_frame; await process_frame
+func saves() -> Dictionary:
+	var found := {}; var dir := DirAccess.open("user://saves")
+	if dir != null:
+		for file in dir.get_files(): found[file]=FileAccess.get_sha256("user://saves/"+file)
+	return found
+func new_gate() -> Node:
+	var gate=load("res://scenes/lol2/original_game_gate.tscn").instantiate()
+	gate.settings_path="user://tests/c15_%d.cfg"%Time.get_ticks_usec()
+	root.add_child(gate); current_scene=gate
+	for i in 3: await process_frame
+	gate.path_field.text=OS.get_environment("LOL2_ORIGINAL_GAME_EXE")
+	return gate
+func run() -> void:
+	assert(OS.get_environment("LOL2_PRIVATE_SAVE_CASE")=="1")
+	assert((DisplayServer.get_name()!="headless")==rendered())
+	var session: Node=Session.for_tree(self); session.set_process(false)
+	DirAccess.make_dir_recursive_absolute("user://saves")
+	var file:=FileAccess.open("user://saves/c15_sentinel.json",FileAccess.WRITE); file.store_string("owner-save-sentinel");file.close()
+	var before:=saves();var listed:=Starts.manifest();assert(listed.error.is_empty(),listed.error)
+	var maps: Array=listed.entries.filter(func(e):return e.resume=="map")
+	assert(maps.size()==10)
+	var seen := {}
+	for entry in maps:
+		assert(not seen.has(entry.area_id));seen[entry.area_id]=true
+		assert(Starts.file_error(entry).is_empty())
+		var read:=Starts.read(entry);assert(read.error.is_empty(),str(read.error));assert(Starts.identity_error(entry,read.state).is_empty())
+		assert(read.state.format==Starts.format_for(entry) and entry.full_health)
+	assert(seen.size()==Starts.Areas.PROGRESSION_AREAS.size())
+	for area in areas():
+		var entry: Dictionary=maps.filter(func(e):return e.area_id==area)[0]
+		var raw:=Starts.read(entry);var incoming: Dictionary=raw.state.duplicate(true)
+		var gate:=await new_gate()
+		await tap(KEY_F2)
+		assert(gate.starts_panel.visible)
+		var button: Button=gate.starts_panel.find_child("Start_"+entry.id,true,false)
+		assert(button!=null and not button.disabled)
+		button.grab_focus();for i in 3:await process_frame
+		if rendered():
+			await RenderingServer.frame_post_draw
+			var rect:=button.get_global_rect();assert(root.get_visible_rect().intersects(rect),"focused row scrolls into view")
+			var directory:="user://tests/c15/";DirAccess.make_dir_recursive_absolute(directory)
+			assert(root.get_texture().get_image().save_png(directory+area+"_list.png")==OK)
+		await tap(KEY_ENTER) # Actual F2 list button activation through normal GUI dispatch.
+		var scene: Node
+		for i in 1800:
+			await process_frame
+			if current_scene!=gate and is_instance_valid(current_scene):
+				scene=current_scene
+				if session.pending_resume.is_empty() and not session.changing_scene:break
+		assert(scene!=null and scene.scene_file_path==Starts.scene_for(entry),area+" F2 resumes expected scene")
+		scene.process_mode=Node.PROCESS_MODE_DISABLED # Hold clocks after apply for exact checkpoint comparisons.
+		assert(session.pending_resume.is_empty() and not session.changing_scene and not has_meta("lol2_slot_resume"))
+		assert(not scene.adapter_exit_seeds and scene.progression.seeds_applied.is_empty(),"no preview seeds")
+		assert(scene.starting_magic.health()==Health.MAXIMUM,area+" full health")
+		var expected_pack: Array=incoming.inventory.collected.duplicate()
+		for item in incoming.quests.get("act2_items",{}).get("carried",[]):
+			if item not in expected_pack:expected_pack.append(item)
+		assert(scene.carried_collected==expected_pack,area+" earned legacy + Act2 pack unchanged")
+		assert(scene.equipped_item==incoming.inventory.equipped_item and scene.equipped_armor==incoming.inventory.equipped_armor)
+		var at: Array=incoming.player.position
+		assert(Vector2(scene.player.position.x-at[0],scene.player.position.z-at[2]).length()<2.0,area+" saved horizontal pose (normal gravity may settle Y): "+str(scene.player.position))
+		assert(scene.resets==0,"no arrival fall reset")
+		assert(Starts.read(entry).state==incoming and FileAccess.get_sha256(Starts.save_path(entry))==entry.sha256,"pinned bytes/health unchanged")
+		if rendered():
+			await RenderingServer.frame_post_draw
+			assert(root.get_texture().get_image().save_png("user://tests/c15/"+area+"_loaded.png")==OK)
+		results.append({"area":area,"id":entry.id,"sha256":entry.sha256,"before_health":incoming.inventory.health,"health":scene.starting_magic.health(),"scene":scene.scene_file_path,"preview_seeds":scene.progression.seeds_applied.duplicate(),"real_F2_Enter":true})
+		print("C15 START ",area," health=",scene.starting_magic.health()," original=",incoming.inventory.health)
+		scene.free();current_scene=null
+		for i in 3:await process_frame
+	assert(saves()==before,"private starts do not write save files while autosave is disabled")
+	var folder:="user://tests/c15/";DirAccess.make_dir_recursive_absolute(folder)
+	file=FileAccess.open(folder+("rendered"if rendered()else"headless")+"_receipt.json",FileAccess.WRITE)
+	file.store_string(JSON.stringify({"cases":results,"all10_staged_pinned_valid":true,"owner_saves_unchanged":true,"scope":"Load/UI proof. Private autosave disabled and post-apply clocks held, no earned-walk claim. Checkpoint producer aids are disclosed in the manifest."},"  "));file.close()
+	print("PASS C-15 ",results.size()," real F2/Enter starts; all10 earned pins validate; full health, no preview seeds, pack/pose/pins/user saves preserved; rendered=",rendered())
+	quit()
diff --git a/tests/playtest_checkpoint_adapter_test.gd b/tests/playtest_checkpoint_adapter_test.gd
new file mode 100644
index 0000000..b29e7d0
--- /dev/null
+++ b/tests/playtest_checkpoint_adapter_test.gd
@@ -0,0 +1,51 @@
+extends SceneTree
+## Synthetic health/validation probes only; never menu content or earned evidence.
+const Save=preload("res://scripts/lol2/game_save.gd")
+const Starts=preload("res://scripts/lol2/playtest_starts.gd")
+const Session=preload("res://scripts/lol2/game_session.gd")
+func _initialize() -> void:run.call_deferred()
+func loaded() -> Node:
+	for i in 1800:
+		await process_frame
+		if current_scene != null and current_scene.get("ready_for_review") == true and is_instance_valid(current_scene.get("starting_magic")) and Session.for_tree(self).pending_resume.is_empty():
+			current_scene.process_mode=Node.PROCESS_MODE_DISABLED
+			return current_scene
+	assert(false,"checkpoint destination ready")
+	return null
+func run() -> void:
+	assert(OS.get_environment("LOL2_PRIVATE_SAVE_CASE")=="1")
+	var session: Node=Session.for_tree(self);session.set_process(false)
+	var path:="res://tests/fixtures/saves_d5da60a/areas/L10_DC.json"
+	var pin:=FileAccess.get_sha256(path)
+	var packet: Dictionary=JSON.parse_string(FileAccess.get_file_as_string(path));packet.inventory.health=9
+	var before: Dictionary=packet.duplicate(true)
+	assert(not Save.resume_checkpoint(self,"L1_DC",packet,true).is_empty())
+	assert(current_scene==null and session.pending_resume.is_empty() and not has_meta("lol2_slot_resume"))
+	var bad: Dictionary=packet.duplicate(true);bad.inventory.health=-1
+	assert(not Save.resume_checkpoint(self,"L10_DC",bad,true).is_empty(),"validate before healing, never mask a bad packet")
+	var maps: Array=Starts.manifest().entries.filter(func(e):return e.resume=="map")
+	var row: Dictionary=maps[0].duplicate(true);row.area_id="../../x"
+	assert(Starts.entry_error(row)=="unknown playtest map")
+	row=maps[0].duplicate(true);row.act=3
+	assert(Starts.entry_error(row)=="map act disagrees with area")
+	row=maps[0].duplicate(true);row.full_health=false
+	assert(Starts.entry_error(row).contains("full_health"))
+	row=maps[0].duplicate(true);row.sha256="0".repeat(64)
+	assert(Starts.file_error(row).contains("sha256"),"wrong pin cannot qualify")
+	for heal in [false,true]:
+		assert(Save.resume_checkpoint(self,"L10_DC",packet,heal).is_empty())
+		await scene_changed
+		var scene: Node=await loaded()
+		assert(session.pending_resume.is_empty() and not session.changing_scene)
+		assert(scene.starting_magic.health()==(30 if heal else 9))
+		assert(packet==before and FileAccess.get_sha256(path)==pin,"source packet remains unchanged")
+		assert(not scene.adapter_exit_seeds and scene.progression.seeds_applied.is_empty())
+	# Ordinary slot read/load retains9; only the dedicated checkpoint copy can heal.
+	var doc:=Save.make_document(current_scene,2);doc.area_save.inventory.health=9
+	assert(Save.write_document(Save.slot_path(2),doc).is_empty())
+	assert(Save.load(self,2).is_empty());await scene_changed
+	var scene: Node=await loaded()
+	assert(scene.starting_magic.health()==9,"ordinary slot load never heals")
+	current_scene.free();current_scene=null
+	print("PASS C-15 detached full-health adapter; optional no-heal and ordinary slot preserve health; map/act/pin/bad-state refusals before mutation")
+	quit()
diff --git a/tests/playtest_map_starts_rendered_test.gd b/tests/playtest_map_starts_rendered_test.gd
new file mode 100644
index 0000000..ffe0ba4
--- /dev/null
+++ b/tests/playtest_map_starts_rendered_test.gd
@@ -0,0 +1,3 @@
+extends "res://tests/playtest/map_case.gd"
+func rendered() -> bool: return true
+func areas() -> Array: return ["L10_DC","L16_CA","L19_BC"]
diff --git a/tests/playtest_map_starts_test.gd b/tests/playtest_map_starts_test.gd
new file mode 100644
index 0000000..d928a6d
--- /dev/null
+++ b/tests/playtest_map_starts_test.gd
@@ -0,0 +1 @@
+extends "res://tests/playtest/map_case.gd"
diff --git a/tests/playtest_starts_test.gd b/tests/playtest_starts_test.gd
index 751ec4c..4b31474 100644
--- a/tests/playtest_starts_test.gd
+++ b/tests/playtest_starts_test.gd
@@ -55,7 +55,7 @@ func run() -> void:
 	# 1. Manifest and staged files.
 	var listed := Starts.manifest()
 	check(listed.error.is_empty(), "manifest parses: " + str(listed.error))
-	var entries: Array = listed.entries
+	var entries: Array = listed.entries.filter(func(e): return int(e.act) == 1)
 	check(entries.size() == 11, "11 Act 1 starts (%d)" % entries.size())
 	var states := {}
 	for entry in entries:
@@ -79,8 +79,8 @@ func run() -> void:
 	var good := {"id": "x", "title": "x", "act": 2, "area": "x", "resume": "hive", "save": "x.json", "sha256": "0".repeat(64),
 		"source": {"test": "t", "commit": "0".repeat(40), "input_sha256": null}, "identities": {"contains": {"a": ["b"]}, "excludes": {}, "values": {}}}
 	check(Starts.entry_error(good) == "", "control entry is well formed: " + Starts.entry_error(good))
-	var bad: Dictionary = good.duplicate(true); bad.resume = "map"
-	check(Starts.entry_error(bad).begins_with("unknown resume kind"), "an unknown resume kind (Act 2 map save) is refused")
+	var bad: Dictionary = good.duplicate(true); bad.resume = "unknown"
+	check(Starts.entry_error(bad).begins_with("unknown resume kind"), "an unknown resume kind is refused")
 	bad = good.duplicate(true); bad.save = "../x.json"
 	check(Starts.entry_error(bad) == "unsafe save name", "a path in the save name is refused")
 	bad = good.duplicate(true); bad.source.erase("commit")
@@ -100,7 +100,7 @@ func run() -> void:
 	if gate.starts_panel != null:
 		for node in gate.starts_panel.find_children("Start_*", "Button", true, false): rows.append(node)
 	var titles: Array = rows.map(func(row: Button) -> String: return row.text)
-	var expected: Array = entries.map(func(entry: Dictionary) -> String: return str(entry.title))
+	var expected: Array = listed.entries.map(func(entry: Dictionary) -> String: return str(entry.title))
 	check(titles == expected, "list rows are the manifest titles in order: %s" % [titles])
 	check(rows.all(func(row: Button) -> bool: return not row.disabled), "every row is enabled (all saves staged)")
 	await key(KEY_F2)
diff --git a/tests/registry/playtest_checkpoint_adapter_test.json b/tests/registry/playtest_checkpoint_adapter_test.json
new file mode 100644
index 0000000..b93
6316
--- /dev/null
+++ b/tests/registry/playtest_checkpoint_adapter_test.json
@@ -0,0 +1,17 @@
+{
+  "name": "playtest_checkpoint_adapter_test",
+  "suite": "core",
+  "mode": "headless",
+  "order": 1343,
+  "needs": {
+    "chain": "Private profile driver: sol_lane/c15_playtest_starts_20261111/private_case.py",
+    "note": "Synthetic validation and health-copy unit probes, not earned checkpoint content; one ordinary slot control."
+  },
+  "count_method": "Audited source sites (K82), not executions. Load/UI tests, not new earned walks; post-apply clocks/private autosave held. Producer aids for the original immutable checkpoints are disclosed separately in the manifest.",
+  "teleports": 0,
+  "test_aids": 4,
+  "honesty": {
+    "method": "audited-source-sites-v1",
+    "audit_sha256": "74b9c5ef0b28eaf4cfe87c967cffd413eca62ddac6615278243dc98cd1540bd9"
+  }
+}
diff --git a/tests/registry/playtest_map_starts_rendered_test.json b/tests/registry/playtest_map_starts_rendered_test.json
new file mode 100644
index 0000000..fcc4840
--- /dev/null
+++ b/tests/registry/playtest_map_starts_rendered_test.json
@@ -0,0 +1,20 @@
+{
+  "name": "playtest_map_starts_rendered_test",
+  "suite": "core",
+  "mode": "rendered",
+  "order": 1343,
+  "needs": {
+    "chain": "Private profile driver: sol_lane/c15_playtest_starts_20261111/private_case.py",
+    "note": "Three actual rendered F2/Enter starts: Cemetery, City, L19; list + scene screenshots; post-apply clocks held.",
+    "args": [
+      "--demo-interface"
+    ]
+  },
+  "count_method": "Audited source sites (K82), not executions. Load/UI tests, not new earned walks; post-apply clocks/private autosave held. Producer aids for the original immutable checkpoints are disclosed separately in the manifest.",
+  "teleports": 0,
+  "test_aids": 2,
+  "honesty": {
+    "method": "audited-source-sites-v1",
+    "audit_sha256": "c9e08739fc6100966307e886f3f2d4fe134551206a20e4983f320b3f4388f087"
+  }
+}
diff --git a/tests/registry/playtest_map_starts_test.json b/tests/registry/playtest_map_starts_test.json
new file mode 100644
index 0000000..712d7a7
--- /dev/null
+++ b/tests/registry/playtest_map_starts_test.json
@@ -0,0 +1,17 @@
+{
+  "name": "playtest_map_starts_test",
+  "suite": "core",
+  "mode": "headless",
+  "order": 1343,
+  "needs": {
+    "chain": "Private profile driver: sol_lane/c15_playtest_starts_20261111/private_case.py",
+    "note": "All ten actual F2/Enter map starts; pins/identity/content/health/no-preview-seeds and save-file preservation; post-apply clocks held."
+  },
+  "count_method": "Audited source sites (K82), not executions. Load/UI tests, not new earned walks; post-apply clocks/private autosave held. Producer aids for the original immutable checkpoints are disclosed separately in the manifest.",
+  "teleports": 0,
+  "test_aids": 2,
+  "honesty": {
+    "method": "audited-source-sites-v1",
+    "audit_sha256": "573b2e3375d3f735fcf40d8fa2094f8b9e06be958d016c4e95b784425c1847f6"
+  }
+}
diff --git a/tests/registry/playtest_starts_test.json b/tests/registry/playtest_starts_test.json
index 47ee5d8..3a9be0f 100644
--- a/tests/registry/playtest_starts_test.json
+++ b/tests/registry/playtest_starts_test.json
@@ -1,11 +1,18 @@
 {
- "name": "playtest_starts_test",
- "suite": "core",
- "mode": "headless",
- "order": 628,
- "needs": {
-  "env": [
-   "LOL2_ORIGINAL_GAME_EXE"
-  ]
- }
+  "name": "playtest_starts_test",
+  "suite": "core",
+  "mode": "headless",
+  "order": 628,
+  "needs": {
+    "env": [
+      "LOL2_ORIGINAL_GAME_EXE"
+    ]
+  },
+  "teleports": 0,
+  "test_aids": 2,
+  "honesty": {
+    "method": "audited-source-sites-v1",
+    "audit_sha256": "3d1ba42057cc75ed9fed1c65d56f8924bc9ebe37dc943204e95679cf572906aa"
+  },
+  "count_method": "Audited source sites (K82), not executions. Load/UI tests, not new earned walks; post-apply clocks/private autosave held. Producer aids for the original immutable checkpoints are disclosed separately in the manifest."
 }
diff --git a/tools/prepare_playtest_starts.py b/tools/prepare_playtest_starts.py
index 70de284..87ddaca 100644
--- a/tools/prepare_playtest_starts.py
+++ b/tools/prepare_playtest_starts.py
@@ -34,6 +34,10 @@ KIND_BY_FORMAT = {
     'lol2-restoration-darker-jungle': 'darker',
     'lol2-restoration-dark-halls': 'dark_halls',
 }
+MAP_AREAS = ('L10_DC', 'L12_CM', 'L13_RC', 'L14_HT', 'L16_CA', 'L17_HC', 'L19_BC', 'L20_BB')
+KIND_BY_FORMAT.update({'lol2-restoration-map-' + area: 'map' for area in MAP_AREAS})
+KIND_BY_FORMAT['lol2-restoration-dragon-preview'] = 'map'
+PROGRESSION_AREAS = ('L8_SJ', 'L9_DR', *MAP_AREAS)
 MARKER = 'PLAYTEST_STARTS_VALIDATION '
 
 
@@ -60,6 +64,15 @@ def load_manifest(path=MANIFEST):
                 raise Refused(f'manifest entry {entry["id"]}: source missing {field}')
         if entry['resume'] not in KIND_BY_FORMAT.values():
             raise Refused(f'manifest entry {entry["id"]}: unknown resume kind {entry["resume"]!r}')
+        if entry['resume'] == 'map':
+            area = entry.get('area_id')
+            if area not in PROGRESSION_AREAS:
+                raise Refused(f'manifest entry {entry["id"]}: unknown playtest map')
+            act = 3 if area in ('L16_CA', 'L17_HC', 'L19_BC', 'L20_BB') else 2
+            if entry['act'] != act:
+                raise Refused(f'manifest entry {entry["id"]}: map act disagrees with area')
+            if entry.get('full_health') is not True:
+                raise Refused(f'manifest entry {entry["id"]}: map start requires full_health')
         name = entry['save']
         if Path(name).name != name or not name.endswith('.json') or name.startswith(('.', '_')):
             raise Refused(f'manifest entry {entry["id"]}: unsafe save name {name!r}')
@@ -74,7 +87,11 @@ def describe(path):
     data = json.loads(Path(path).read_text())
     fmt = data.get('format') if isinstance(data, dict) else None
     kind = KIND_BY_FORMAT.get(fmt)
-    print(json.dumps({'save': Path(path).name, 'sha256': digest(path), 'format': fmt,
+    if fmt == 'lol2-restoration-darker-jungle': kind = 'map'
+    area = fmt.removeprefix('lol2-restoration-map-') if kind == 'map' else None
+    if fmt == 'lol2-restoration-dragon-preview': area = 'L9_DR'
+    if fmt == 'lol2-restoration-darker-jungle': area = 'L8_SJ'
+    print(json.dumps({**({'area_id': area, 'full_health': True} if area else {}), 'save': Path(path).name, 'sha256': digest(path), 'format': fmt,
                       'source': {'test': 'FILL', 'commit': 'FILL (40 hex)', 'input_sha256': 'FILL or null'},
                       'identities': {'contains': {'inventory.collected': []}, 'excludes': {}, 'values': {}},
                       'resume': kind or f'UNSUPPORTED ({fmt}): needs a gate resume branch first'}, indent=2))
diff --git a/tools/regression_source.py b/tools/regression_source.py
index b57f3b9..68a29ae 100644
--- a/tools/regression_source.py
+++ b/tools/regression_source.py
@@ -8,7 +8,8 @@ SUFFIXES = {'.gd', '.gdshader', '.gdshaderinc', '.tscn', '.tres', '.json'}
 def snapshot(root: Path) -> dict:
     paths = {root / 'project.godot'}
     paths.update(root / 'tools' / name for name in (
-        'run_regressions.py', 'run_isolated_regressions.py', 'regression_source.py', 'stage_worktree.py'))
+        'run_regressions.py', 'run_isolated_regressions.py', 'regression_source.py', 'stage_worktree.py', 'prepare_playtest_starts.py',
+        'test_prepare_playtest_starts.py', 'validate_playtest_starts.gd'))
     for directory in ('scripts', 'scenes', 'tests'):
         paths.update(p for p in (root / directory).rglob('*')
                      if p.is_file() and not p.is_symlink() and p.suffix in SUFFIXES)
diff --git a/tools/test_prepare_playtest_starts.py b/tools/test_prepare_playtest_starts.py
index f232655..3adc707 100644
--- a/tools/test_prepare_playtest_starts.py
+++ b/tools/test_prepare_playtest_starts.py
@@ -4,6 +4,8 @@
 python3 tools/test_prepare_playtest_starts.py  [LOL2_GODOT="tmp/godot_host_starts.sh" also runs the game-validator control]
 """
 import json
+import contextlib
+import io
 import os
 import shlex
 import shutil
@@ -54,15 +56,34 @@ class Refusals(unittest.TestCase):
 
     def test_unsafe_na
me_and_kind(self):
         self.assertIn('unsafe save name', self.refused(self.manifest(dict(self.entry, save='../a.json'))))
-        self.assertIn('unknown resume kind', self.refused(self.manifest(dict(self.entry, resume='map'))))
+        self.assertIn('unknown resume kind', self.refused(self.manifest(dict(self.entry, resume='unknown'))))
         self.assertIn('duplicate', self.refused(self.manifest(self.entry, dict(self.entry, id='b'))))
         self.assertIn('source missing commit', self.refused(self.manifest(dict(self.entry, source={'test': 't', 'input_sha256': None}))))
         self.assertIn('missing identities', self.refused(self.manifest({k: v for k, v in self.entry.items() if k != 'identities'})))
 
     def test_committed_manifest_loads(self):
         entries = tool.load_manifest()
-        self.assertEqual(len(entries), 11)
-        self.assertTrue(all(e['act'] == 1 for e in entries))
+        self.assertEqual(len(entries), 21)
+        self.assertEqual(sum(e['act'] == 1 for e in entries), 11)
+        self.assertEqual({e['area_id'] for e in entries if e['resume'] == 'map'}, set(tool.PROGRESSION_AREAS))
+
+    def test_map_metadata_refused_before_engine(self):
+        entry = dict(self.entry, resume='map', area_id='L16_CA', act=3, full_health=True)
+        self.assertIn('unknown playtest map', self.refused(self.manifest(dict(entry, area_id='../x'))))
+        self.assertIn('act disagrees', self.refused(self.manifest(dict(entry, act=2))))
+        self.assertIn('requires full_health', self.refused(self.manifest(dict(entry, full_health=False))))
+        self.assertEqual(tool.load_manifest(self.manifest(entry)), [entry])
+
+    def test_describe_map_formats(self):
+        for fmt, area in [('lol2-restoration-map-L16_CA', 'L16_CA'),
+                          ('lol2-restoration-dragon-preview', 'L9_DR'),
+                          ('lol2-restoration-darker-jungle', 'L8_SJ')]:
+            self.save.write_text(json.dumps({'format': fmt}))
+            output = io.StringIO()
+            with contextlib.redirect_stdout(output):
+                self.assertEqual(tool.describe(self.save), 0)
+            row = json.loads(output.getvalue())
+            self.assertEqual((row['resume'], row['area_id'], row['full_health']), ('map', area, True))
 
     @unittest.skipUnless(os.environ.get('LOL2_GODOT'), 'set LOL2_GODOT to run the game-validator control')
     def test_game_validator_refuses_wrong_format(self):
diff --git a/tools/validate_playtest_starts.gd b/tools/validate_playtest_starts.gd
index e74d27f..be21b9e 100644
--- a/tools/validate_playtest_starts.gd
+++ b/tools/validate_playtest_starts.gd
@@ -22,7 +22,7 @@ func _initialize() -> void:
 		var row: Dictionary = {"id": entry.id, "save": entry.save, "resume": entry.resume, "sha256": FileAccess.get_sha256(path)}
 		var read: Dictionary = Starts.read(entry, path)
 		row.error = str(read.error)
-		if row.error.is_empty() and str(read.state.get("format")) != str(Starts.KINDS[str(entry.resume)].format):
+		if row.error.is_empty() and str(read.state.get("format")) != Starts.format_for(entry):
 			row.error = "format differs from the resume kind"
 		if row.error.is_empty() and row.sha256 != str(entry.sha256): row.error = "sha256 differs from the manifest"
 		if row.error.is_empty(): row.error = Starts.identity_error(entry, read.state)
Now let me review the surrounding code in the gate and game_save to check for issues:

  1. `start_playtest` for "map" branch — note the order: identity check, then pin recheck, then `_verify_save_access()`. But wait — for non-map branches, what was the original order? Let me check the original `start_playtest` and where `file_error` was first called. In the new map branch: read first (which happens before the pin check? Starts.read reads the file — but the entry_error was called earlier presumably). Actually the concern: "SHA check before/after read" — the map branch calls `Starts.read(entry)` then identity check, then `file_error(entry)` (pin recheck). Was there a pin check before read? Let me look at start_playtest beginning. It says `var error := Starts.entry_error(entry)` probably, then... In the diff, at line 256 context: `if not error.is_empty(): report.call(error); return` — that's probably entry_error. Then for map branch it reads without first checking the sha pin! The comment says "Recheck the pin after reading" — implying there was a first check. Let me check where the first file_error is called in the non-map path.

  2. `_verify_save_access()` — returns error string; the code does `if not _verify_save_access().is_empty(): return` — it returns without reporting the error? Compare with other branches.

  3. `resume_checkpoint` passes `state` (the raw read state, not detached?) — no wait: `var packet := state.duplicate(true)` then modifies packet. Good, source not mutated. But note: `read.state` — the gate passes `read.state`, and resume_checkpoint duplicates. OK.

  4. Act1 behavior changes: the "darker" start previously had full_health? The handoff says "only their previously approved darker start heals". In game_save.gd diff, `resume_checkpoint` is new; the existing branches unchanged except help text. Also check `load_legacy` doc has `adapter_exit_seeds: true` — unchanged.

  5. `map_case.gd`: `areas()` returns `Starts.Areas.PROGRESSION_AREAS` for headless — all 10 areas? Wait, PROGRESSION_AREAS in game_areas.gd — how many entries? The manifest has 10 map entries: L8_SJ, L9_DR, L10_DC, L12_CM, L13_RC, L14_HT, L16_CA, L17_HC, L19_BC, L20_BB. But the test asserts `seen.size()==Starts.Areas.PROGRESSION_AREAS.size()`. If PROGRESSION_AREAS has more areas than 10 (e.g., L11, L15, L18?), then this assert would fail... but they claim it passes. Let me check game_areas.gd PROGRESSION_AREAS.

  Also potential test-that-cannot-fail issues: `map_case.gd` loop `for i in 1800` — if scene never changes, `scene` stays null → assert fails. OK.

  One thing: `assert(Starts.read(entry).state==incoming ...)` — comparing Dictionary equality; fine.

  `button.grab_focus(); for i in 3: await process_frame` then `await tap(KEY_ENTER)` — taps Enter globally; relies on focused button receiving it. OK-ish.

  6. Privacy leaks: The manifest contains absolute paths `~/AI_COMMS/...` and `~/opus_work/...` in committed `scripts/lol2/playtest_starts.json` source.path/proof fields. Also docs contain `~/AI_COMMS/sol_lane/...`. The task explicitly lists "path or privacy leaks (absolute /home paths or owner names in committed files)" as something to look for. But wait — was this pre-existing? The old manifest already had `"path": "~/AI_COMMS/act1_completion_20261017/..."` entries (act1-museum-arrival etc.)? Let me check the parent version. The old docs/playtest-starts.md had `~/AI_COMMS/...` in staging example. So the convention pre-exists. The review prompt asks to look for them though. I should check whether Act1 entries in parent already contained ~ paths — if so it's established convention, but still worth a MINOR note.

  Let me check the parent file.

  7. `_queue_scene(tree, doc, 1, false)` — slot_id 1: does pending apply write to slot 1? Check _queue_scene and the apply path: does loading write anything to slot? The `last_slot: 1` in session — could F5 afterwards write to slot 1? "F5 subsequently writes a normal whole-game slot" — presumably the next slot logic. Need to check whether passing slot_id=1 causes an autosave or marks slot 1 as last slot such that F5 overwrites user's slot 1. Let me read game_save.gd _queue_scene and how load uses slot_id.

  8. `resume_checkpoint` full_health: `packet.inventory.health = ...MAXIMUM`. If the state lacks `inventory` key, this would error — but validate_area runs first, so presumably fine. Note validate happens before heal, good (test asserts bad packet refused).

  9. In gate map branch: after `_verify_save_access()` fails it returns silently — check whether other branches report. Let me read original_game_gate.gd start_playtest fully.

  10. Help text says "Act 2/3 starts restore full health; older checkpoints can reset native puzzles on other maps." Hmm "older checkpoints" — actually the new Act2/3 ones reset native puzzles; fine, minor wording.

  11. The manifest `act2-l9` has `"format": "lol2-restoration-dragon-preview"` as identity value — and format_for(entry) returns `Areas.ROWS[entry.area_id].format`. Does Areas.ROWS["L9_DR"].format == "lol2-restoration-dragon-preview"? And prepare tool maps dragon-preview → map. Check game_areas.gd.

  12. Potential issue: `map_case.gd` headless `areas()` returns all PROGRESSION_AREAS, then `seen.size()==PROGRESSION_AREAS.size()` requires manifest maps to cover exactly all progression areas. Check count.

  13. In `resume_checkpoint`, session last_slot: 1 — check what other branches use. `load_legacy` uses last_slot:1 too. And normal slot loads use the slot. F5 after checkpoint start: writes "a normal whole-game slot" — which slot? If it writes to slot 1 (last_slot), could overwrite user's manual slot 1! Check save code: F5 quicksave probably uses current area quicksave, not last_slot. Let me check.

  Let me read the relevant files.

• Now let me examine the surrounding code in the gate and save system to verify the claims.		get_viewport().set_input_as_handled()

func show_playtest_starts() -> void:
	if starts_panel == null: _build_playtest_starts()
	starts_panel.show()
	var first := starts_panel.find_child("Start_*", true, false) as Button
	if first != null: first.grab_focus()

func _build_playtest_starts() -> void:
	var listed := Starts.manifest()
	starts_panel = PanelContainer.new()
	starts_panel.name = "PlaytestStartsPanel"
	starts_panel.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	var style := StyleBoxFlat.new()
	style.bg_color = Color("17202b")
	style.content_margin_left = 40; style.content_margin_right = 40; style.content_margin_top = 24; style.content_margin_bottom = 24
	starts_panel.add_theme_stylebox_override("panel", style)
	# Plain list at the player's UI size (ui_scale.gd; 150% by default), relative to a 720-high window.
	var font := int(round(16 * UiScale.factor()))
	starts_panel.add_theme_font_size_override("font_size", font)
	add_child(starts_panel)
	var column := VBoxContainer.new()
	column.add_theme_constant_override("separation", 8)
	starts_panel.add_child(column)
	var heading := Label.new()
	heading.text = "Playtest starts"
	heading.add_theme_font_size_override("font_size", font + 8)
	column.add_child(heading)
	var help := Label.new()
	help.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	help.text = "Story checkpoints earned by automated route tests. Act 2/3 starts restore full health; older checkpoints can reset native puzzles on other maps. Manual slots are kept; normal autosaves apply. F2 or Esc closes this list."
	column.add_child(help)
	var scroll := ScrollContainer.new()
	scroll.follow_focus = true
	scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	column.add_child(scroll)
	var rows := VBoxContainer.new()
	rows.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	scroll.add_child(rows)
	for entry in listed.entries:
		var row := Button.new()
		row.name = "Start_" + str(entry.id)
		row.alignment = HORIZONTAL_ALIGNMENT_LEFT
		row.text = str(entry.title)
		var missing := Starts.file_error(entry)
		if not missing.is_empty():
			row.disabled = true
			row.text += "  (not in this build)"
		row.pressed.connect(start_playtest.bind(str(entry.id)))
		rows.add_child(row)
	starts_status = Label.new()
	starts_status.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	starts_status.text = listed.error
	column.add_child(starts_status)
	var back := Button.new()
	back.name = "PlaytestStartsBack"
	back.text = "Back"
	back.size_flags_horizontal = Control.SIZE_SHRINK_BEGIN
	back.pressed.connect(func(): starts_panel.hide())
	column.add_child(back)

## Start one manifest entry through the gate's own resume branch for its area: the branch's save path is pointed at the
## staged res:// file for this one call (reader, validator, resume meta and scene unchanged), then restored.
func start_playtest(id: String) -> void:
	var entry := {}
	for candidate in Starts.manifest().entries:
		if str(candidate.id) == id: entry = candidate
	var report := func(text: String) -> void:
		status.text = text
		if starts_status != null: starts_status.text = text
		print("Playtest start blocked: ", text)
	if entry.is_empty():
		report.call("Unknown playtest start: " + id)
		return
	var error := Starts.file_error(entry)
	if not error.is_empty():
		report.call(error)
		return
	if str(entry.resume) == "map":
		var read := Starts.read(entry)
		if not read.error.is_empty(): report.call(read.error); return
		var identity := Starts.identity_error(entry,read.state)
		if not identity.is_empty(): report.call(identity); return
		# Recheck the pin after reading, before any session/scene mutation.
		var pin_error := Starts.file_error(entry)
		if not pin_error.is_empty(): report.call(pin_error); return
		if not _verify_save_access().is_empty(): return
		var resumed: String = preload("res://scripts/lol2/game_save.gd").resume_checkpoint(get_tree(),entry.area_id,read.state,true)
		if not resumed.is_empty(): report.call(resumed)
		return
	var path := Starts.save_path(entry)
	var kept := [museum_save_path, jungle_save_path, hive_save_path, darker_save_path, dark_halls_save_path]
	match str(entry.resume):
		"museum": museum_save_path = path
		"jungle": jungle_save_path = path
		"hive": hive_save_path = path
		"darker": darker_save_path = path
		"dark_halls": dark_halls_save_path = path
	print("Playtest start: ", entry.id, " (", entry.save, ")")
	start_full_health = bool(entry.get("full_health", false))
	_verify_and_start(entry.resume == "museum", entry.resume == "jungle", entry.resume == "hive", entry.resume == "darker", entry.resume == "dark_halls")
	start_full_health = false
	museum_save_path = kept[0]; jungle_save_path = kept[1]; hive_save_path = kept[2]; darker_save_path = kept[3]; dark_halls_save_path = kept[4]
	if starts_status != null and not status.text.is_empty(): starts_status.text = status.text

## Act 2 test start (lane l8-preview, opened to Classic by the owner's 2026-10-30 request "jump to Act 2 without replaying Act 1"):
## the darker-jungle scene from its native arrival, without the Act 1 handoff. Offered in both editions whenever the pack is staged;
## --l8-preview still starts it at once. The Classic Act 1 chain itself reaches that scene only through act_one_departure.

func _verify_and_start(resume_museum: bool = false, resume_jungle: bool = false, resume_hive: bool = false, resume_darker: bool = false, resume_dark_halls: bool = false, preview_darker: bool = false, preview_map_scene: String = "", preview_dragon: bool = false) -> void:
	if not _verify_save_access().is_empty(): return
	preload("res://scripts/lol2/game_session.gd").for_tree(get_tree()).reset_legacy()
	var scene_path := "res://scenes/lol2/cave_walkthrough.tscn"
	if resume_museum:
		var saved := MuseumSave.read_save(museum_save_path)
		if not saved.error.is_empty():
			status.text = saved.error
			return
		if not preload("res://scripts/lol2/museum_walkthrough.gd").assets_ready():
			status.text = "Museum assets are missing from this build."
			return
		get_tree().set_meta("lol2_museum_resume",saved.state)
		scene_path = "res://scenes/lol2/museum_walkthrough.tscn"
	elif resume_jungle:
		var saved := JungleSave.read_save(jungle_save_path)
		if not saved.error.is_empty():
			status.text = saved.error
			return
		if not preload("res://scripts/lol2/jungle_walkthrough.gd").assets_ready():
			status.text = "Jungle assets are missing from this build."
			return
		get_tree().set_meta("lol2_jungle_resume",saved.state)
		scene_path = "res://scenes/lol2/jungle_walkthrough.tscn"
	elif resume_hive:
		var saved := HiveSave.read_save(hive_save_path)
		if not saved.error.is_empty():
			status.text = saved.error
			return
		if not preload("res://scripts/lol2/hive_review.gd").assets_ready():
			status.text = "Hive assets are missing from this build."
			return
		get_tree().set_meta("lol2_hive_resume",saved.state)
		scene_path = "res://scenes/lol2/hive_review.tscn"
	elif resume_darker:
		var saved := JungleSave.read_save(darker_save_path,Darker.FORMAT)
		if not saved.error.is_empty():
			status.text = saved.error
			return
		if not Darker.arrival_assets_ready():
			status.text = "Darker jungle assets are missing from this build."
			return
		if start_full_health: saved.state.inventory.health = PlayerHealth.MAXIMUM
		get_tree().set_meta("lol2_darker_resume",saved.state)
		scene_path = "res://scenes/lol2/darker_jungle.tscn"
	elif preview_darker:
		if not Darker.arrival_assets_ready():
			status.text = "Darker jungle assets are missing from this build."
			return
		get_tree().set_meta("lol2_darker_preview", true)
		scene_path = "res://scenes/lol2/darker_jungle.tscn"
	var rows: Array[Dictionary] = []
	for id in [1,2,3,4,5,6,7,8,9,10,AUTOSAVE]:
		var row := _file_row(slot_path(id));row["id"] = id;row["backup"] = _file_row(backup_path(id));rows.append(row)
	return rows

static func has_slot_files() -> bool:
	for id in [0,1,2,3,4,5,6,7,8,9,10]:
		if FileAccess.file_exists(slot_path(id)) or FileAccess.file_exists(backup_path(id)):return true
	return false

static func newest() -> Dictionary:
	var candidates := []
	for row in slots():
		if row.valid: candidates.append(row)
		elif row.backup.valid:
			var backup: Dictionary = row.backup.duplicate(true);backup["id"] = row.id;backup["use_backup"] = true;candidates.append(backup)
	candidates.sort_custom(func(a,b): return a.written_unix > b.written_unix)
	return candidates[0] if not candidates.is_empty() else {}

static func legacy_saves() -> Array[Dictionary]:
	var rows: Array[Dictionary] = []
	for area in Areas.ROWS:
		var definition: Dictionary = Areas.ROWS[area]
		if not FileAccess.file_exists(definition.legacy): continue
		var row := {"area":area,"label":definition.label,"path":definition.legacy,"written_unix":FileAccess.get_modified_time(definition.legacy),"legacy":true,"valid":true,"error":""}
		var read := read_legacy(area)
		row.error=read.error;row.valid=read.error.is_empty()
		rows.append(row)
	return rows

static func read_legacy(area: String, path: String = "") -> Dictionary:
	if not Areas.ROWS.has(area): return {"error":"Unknown saved area."}
	if path.is_empty(): path = Areas.ROWS[area].legacy
	match Areas.ROWS[area].kind:
		"cave": return ResourceLoader.load("res://scripts/lol2/walkthrough_save.gd").read_save(path, Areas.cave_checkpoints())
		"museum": return ResourceLoader.load("res://scripts/lol2/museum_save.gd").read_save(path)
		"hive": return ResourceLoader.load("res://scripts/lol2/hive_save.gd").read_save(path)
		"jungle": return ResourceLoader.load("res://scripts/lol2/jungle_save.gd").read_save(path,Areas.ROWS[area].format)
		_: return ResourceLoader.load("res://scripts/lol2/act2_save.gd").read_save(path,Areas.ROWS[area].format)

static func load_slot(tree: SceneTree, slot_id: int, use_backup: bool = false) -> String:
	if slot_path(slot_id).is_empty(): return "Choose a save slot."
	var read := read_document(backup_path(slot_id) if use_backup else slot_path(slot_id))
	if not read.error.is_empty(): return read.error
	return _queue_scene(tree,read.state,slot_id,false)

static func load_legacy(tree: SceneTree, area: String) -> String:
	var read := read_legacy(area)
	if not read.error.is_empty(): return read.error
	var row: Dictionary = Areas.ROWS[area]
	var doc := {"area":area,"scene":row.scene,"area_save":read.state,"native_bank":{},"play_seconds":0.0,"session":{"options":{"adapter_exit_seeds":true},"last_slot":1}}
	return _queue_scene(tree,doc,1,true)

## F2 checkpoints are immutable earned area packets. Use the same pending-apply,
## asset admission and rollback path as slots; no preview/exit seeds are granted.
static func resume_checkpoint(tree: SceneTree, area: String, state: Dictionary, full_health: bool) -> String:
	if area not in Areas.PROGRESSION_AREAS: return "Unknown playtest map."
	var error := Areas.validate_area(area,state)
	if not error.is_empty(): return error
	var packet := state.duplicate(true)
	if full_health: packet.inventory.health = preload("res://scripts/lol2/player_health.gd").MAXIMUM
	var doc := {"area":area,"scene":Areas.ROWS[area].scene,"area_save":packet,"native_bank":{},"play_seconds":0.0,
		"session":{"options":{"adapter_exit_seeds":false},"last_slot":1}}
	return _queue_scene(tree,doc,1,false)

static func _queue_scene(tree: SceneTree, doc: Dictionary, slot_id: int, legacy: bool) -> String:
	if tree.paused: return "Close the current overlay before loading."
	if OS.has_feature("original_game_required") and not tree.get_meta("original_game_verified",false): return "Verify the original game files before loading."
	var session: Node = Session.for_tree(tree)
	if session == null or session.changing_scene or not session.pending_resume.is_empty(): return "Wait until the area finishes loading."
	if session.save_in_progress(): return "An autosave is finishing. Try again shortly."
	var current := tree.current_scene
	if is_instance_valid(current):
		var progression: Variant = current.get("progression")
		if is_instance_valid(progression) and progression.get("transition_pending") == true: return "Wait until the area change finishes."
		for child in current.get_children():
			if child.get("transitioning") == true: return "Wait until the area change finishes."
	var assets_error := Areas.assets_error(doc.area)
	if not assets_error.is_empty(): return assets_error
	if not ResourceLoader.exists(doc.scene): return "The saved area is not available in this build."
	var packed: PackedScene = ResourceLoader.load(doc.scene) as PackedScene
	if packed == null: return "Cannot load the saved area."
	var prior: Dictionary = session.runtime_checkpoint()
	var metadata := {}
	for key in session.RESUME_METAS:
		if tree.has_meta(key):
			metadata[key] = tree.get_meta(key)
			tree.remove_meta(key)
	var error: String = session.replace_bank(doc.native_bank)
	if not error.is_empty():
		session.restore_runtime(prior)
		for key in metadata: tree.set_meta(key,metadata[key])
		return error
	session.play_seconds = float(doc.play_seconds)
	session.last_slot = int(doc.session.get("last_slot",1)) if slot_id == AUTOSAVE else slot_id
	session.set_seed_override(bool(doc.session.options.adapter_exit_seeds))
	session.changing_scene = true
	if legacy and session.LEGACY_RESUMES.has(doc.area):
		tree.set_meta(session.LEGACY_RESUMES[doc.area],doc.area_save.duplicate(true))
	else:
		session.pending_resume = {"area":doc.area,"scene":doc.scene,"state":Areas.prepare_area(doc.area,doc.area_save)}
		tree.set_meta("lol2_slot_resume",{"area":doc.area,"scene":doc.scene})
	session.retain_previous(current,prior,metadata)
	var status := tree.change_scene_to_packed(packed)
	if status != OK:
		session.rollback_load("Could not open the saved area; current game preserved.")
		return "Could not open the saved area; current game preserved."
	return ""

static func load(tree: SceneTree, slot_id: int, use_backup: bool = false) -> String:
	return load_slot(tree, slot_id, use_backup)


• Key observations so far:

  1. In `resume_checkpoint`, doc has `native_bank: {}` — same as load_legacy. So a checkpoint start resets the native bank (acknowledged: "native puzzles on other maps may reset"). OK, disclosed.

  2. `session.last_slot = ... if slot_id == AUTOSAVE else slot_id` — slot_id passed is 1. So `session.last_slot = 1`. Now what does F5 do? Check the F5 quicksave path: does F5 write to `last_slot`? Handoff says "F5 subsequently writes a normal whole-game slot". If F5 writes to `session.last_slot` (1), it would overwrite the user's manual slot 1! Let me check what F5/save uses. Actually the existing `load_legacy` also passes slot_id=1 and sets last_slot=1, and `load_slot(tree, slot_id)` sets last_slot = slot_id. So after loading slot 5, F5 presumably writes slot 5. After a checkpoint start, F5 writes slot 1 — potentially overwriting the user's own save in slot 1! Need to check the F5 code path. The old Act1 branch (`_verify_and_start` with resume metas) — what did last_slot become there? It uses scene meta resumes, not _queue_scene, so last_slot may stay default. Hmm. Actually wait — the claim "Manual slots remain" is about the start not writing. But F5-after-start writing to slot 1 could be pre-existing behavior for legacy loads too (load_legacy passes 1). Let me check how F5 chooses slot.

  3. `_verify_save_access()` in the map branch: `if not _verify_save_access().is_empty(): return` — silently returns without reporting error to status. Other branches do the same (`_verify_and_start` first line). So consistent. But also note: in the map branch, `_queue_scene` itself checks `original_game_verified` when feature enabled — fine.

  4. Ordering issue: in the map branch, `Starts.read(entry)` is called BEFORE `file_error` recheck... no wait, `file_error` (sha check) is called at the top of start_playtest for all entries (line: `var error := Starts.file_error(entry)`). Then read, identity, then pin recheck. So SHA checked before and after read. Good.

  5. `resume_checkpoint` does NOT check that the state's format matches the area — it calls `Areas.validate_area(area, state)`. Does validate_area check format? The gate map branch checks identity_error which includes `values.format` identities in the manifest entries. But entry identities are manifest-declared; a map entry without a format identity would pass. But entry_error doesn't require format identity. Minor. Actually `validate_area` might check format — let me check game_areas.gd.

  6. full_health leaking: `resume_checkpoint` only called from map branch with hardcoded `true` (`entry.area_id, read.state, true`). Note the gate ignores `entry.full_health` and always passes true — but entry_error enforces full_health==true for map entries. OK.

  Does the full-health on the detached packet affect the pinned file? No — duplicate(true). And test asserts pinned bytes unchanged.

  7. Act1 changes: `start_full_health` handling — unchanged except... the map branch returns before touching start_full_health. The darker branch still uses start_full_health. The playtest_starts.gd change: full_health bool check added for all entries (`if entry.has("full_health") and not entry.full_health is bool`) — fine.

  8. UI: 21 entries in a ScrollContainer with follow_focus — fixed scroll issue. The list builds all entries as buttons — fine for 21.

  9. Manifest contains absolute `~/...` paths in committed file — check whether parent's Act1 entries also did. The diff showed only added lines for act2 entries; need to check the parent version for existing "~" paths. From the old docs, the staging example had ~ path, so the convention pre-exists in docs. Check the old playtest_starts.json.

  10. `map_case.gd` test: `assert(seen.size()==Starts.Areas.PROGRESSION_AREAS.size())` — need to verify PROGRESSION_AREAS has exactly 10 entries matching. If PROGRESSION_AREAS has, say, 12 (including L11, L15, L18, L21?), this test would fail — but they claim it passes. Let me check game_areas.gd.

  Also `areas()` for headless returns all PROGRESSION_AREAS; for each area it indexes `maps.filter(...)[0]` — fine if coverage exact.

  11. `test_prepare_playtest_starts.py`: PROGRESSION_AREAS = ('L8_SJ', 'L9_DR', *MAP_AREAS) — 10 entries. And the manifest test asserts set equality with tool.PROGRESSION_AREAS — tool's own constant, not the game's Areas.PROGRESSION_AREAS. Two sources of truth; the gdscript entry_error uses game Areas.PROGRESSION_AREAS. If they diverge, the python tool could accept an area the game rejects or vice versa. Minor.

  12. In `describe()`: `if fmt == 'lol2-restoration-darker-jungle': kind = 'map'` — this OVERRIDES the existing darker kind in describe output. But wait — the manifest's act2-l8 entry reuses the darker packet with resume "map" and area_id L8_SJ. But hold on: does Areas.ROWS["L8_SJ"].format equal "lol2-restoration-darker-jungle"? And validate for L8_SJ works on that packet? Presumably.

  But there's a subtle issue: KIND_BY_FORMAT still maps 'lol2-restoration-darker-jungle' → 'darker' for manifest validation (`entry['resume'] not in KIND_BY_FORMAT.values()` — 'map' is in values via the map formats, fine). The describe override is only for the describe tool. OK.

  13. Registry JSONs: `"order": 1343` for three new tests — all same order value. Handoff says "three new cases use1343 ties". Fine.

  14. map_case.gd potential "cannot fail" issues: `assert(maps.size()==10)`. Fine. The F2 tap: `await tap(KEY_F2)` then `assert(gate.starts_panel.visible)`. Fine. The button found by name "Start_"+entry.id. Enter dispatch to focused button — real GUI. OK.

  One concern: `assert(saves()==before, ...)` — "while autosave is disabled". They assert the private case disables autosave. But in `resume_checkpoint` doc session options: `adapter_exit_seeds: false` — and what about autosave on map entry? Handoff says "ordinary eligible autosaves still apply". In the test, autosave disabled via private profile. In real game, starting a checkpoint may trigger an autosave that overwrites the autosave slot — disclosed in help text ("normal autosaves apply"). OK by design.

  15. Now the F5/last_slot question. Let me find where F5 saves. Search for last_slot usage and save shortcut.

  16. Check game_areas.gd: PROGRESSION_AREAS, ROWS formats, validate_area.

  Also verify `Areas.ROWS[area].scene` exists for all 10, and `L20_BB` in PROGRESSION_AREAS — manifest claims act 3 areas list matches entry_error's list ["L16_CA","L17_HC","L19_BC","L20_BB"].

  Also check `Areas.validate_area` — does it check format? If not, then... the gate checks identities which include format per entry. Fine.

  17. `resume_checkpoint` doesn't verify read.error — the gate did. But adapter test calls resume_checkpoint directly with a packet from fixture. Fine.

  18. Potential issue in the gate map branch: `Starts.read(entry)` — reads file and parses; if the file changed between file_error (sha check) and read (TOCTOU), the pin recheck after read catches it. OK.

  19. `read_legacy` for "cave" kind uses walkthrough_save.read_save with cave_checkpoints; L8_SJ is darker jungle format — Areas.ROWS["L8_SJ"].kind probably "jungle" → jungle_save.read_save(path, format). OK.

  Let me now look at game_areas.gd and the F5 save path.

• Let me check `game_areas.gd` (PROGRESSION_AREAS, validate_area) and how F5 saving picks a slot (the `last_slot: 1` in the checkpoint doc).3:const PROGRESSION_AREAS := ["L8_SJ","L9_DR","L10_DC","L12_CM","L13_RC","L14_HT","L16_CA","L17_HC","L19_BC","L20_BB"]
4-const ROWS := {
5- "L10_DC": {
6-  "scene": "res://scenes/lol2/maps/L10_DC.tscn",
7-  "format": "lol2-restoration-map-L10_DC",
8-  "label": "Dracoid Cemetery",
--
167:static func validate_area(area: String, value: Variant) -> String:
168- if not ROWS.has(area): return "Unknown saved area."
169- match ROWS[area].kind:
170-  "cave": return load("res://scripts/lol2/walkthrough_save.gd").validate(value, cave_checkpoints())
171-  "museum": return load("res://scripts/lol2/museum_save.gd").validate(value)
172-  "hive": return load("res://scripts/lol2/hive_save.gd").validate(value)
--
175:static func prepare_area(area: String, value: Dictionary) -> Dictionary:
176- var result := value.duplicate(true)
177- if area == "L1_DC": result = load("res://scripts/lol2/walkthrough_save.gd").migrate_loaded(result)
178- return result
179-
180-## Match the opening gate's per-area checks before touching the live session.
--
182:static func assets_error(area: String) -> String:
183- if not ROWS.has(area): return "Unknown saved area."
184- var ready := true
185- match area:
186-  "L3_DH": ready = load("res://scripts/lol2/museum_walkthrough.gd").assets_ready()
187-  "L4_HJ": ready = load("res://scripts/lol2/jungle_walkthrough.gd").assets_ready()
--
193:   if area in PROGRESSION_AREAS: ready = load("res://scripts/lol2/act2_map.gd").map_assets_ready(area)
194- return "" if ready else "%s assets are missing from this build." % ROWS[area].label


extends RefCounted
## Catalog pairs only existing playable scenes and legacy validators.
const PROGRESSION_AREAS := ["L8_SJ","L9_DR","L10_DC","L12_CM","L13_RC","L14_HT","L16_CA","L17_HC","L19_BC","L20_BB"]
const ROWS := {
 "L10_DC": {
  "scene": "res://scenes/lol2/maps/L10_DC.tscn",
  "format": "lol2-restoration-map-L10_DC",
  "label": "Dracoid Cemetery",
  "kind": "act2",
  "legacy": "user://saves/map_L10_DC_quicksave.json",
  "scenes": [
   "res://scenes/lol2/maps/L10_DC.tscn"
  ]
 },
 "L12_CM": {
  "scene": "res://scenes/lol2/maps/L12_CM.tscn",
  "format": "lol2-restoration-map-L12_CM",
  "label": "Claw Mountains",
  "kind": "act2",
  "legacy": "user://saves/map_L12_CM_quicksave.json",
  "scenes": [
   "res://scenes/lol2/maps/L12_CM.tscn"
  ]
 },
 "L13_RC": {
  "scene": "res://scenes/lol2/maps/L13_RC.tscn",
  "format": "lol2-restoration-map-L13_RC",
  "label": "Citadel of the Ruloi",
  "kind": "act2",
  "legacy": "user://saves/map_L13_RC_quicksave.json",
  "scenes": [
   "res://scenes/lol2/maps/L13_RC.tscn"
  ]
 },
 "L14_HT": {
  "scene": "res://scenes/lol2/maps/L14_HT.tscn",
  "format": "lol2-restoration-map-L14_HT",
  "label": "Huline Temple",
  "kind": "act2",
  "legacy": "user://saves/map_L14_HT_quicksave.json",
  "scenes": [
   "res://scenes/lol2/maps/L14_HT.tscn"
  ]
 },
 "L16_CA": {
  "scene": "res://scenes/lol2/maps/L16_CA.tscn",
  "format": "lol2-restoration-map-L16_CA",
  "label": "City of the Ancients",
  "kind": "act2",
  "legacy": "user://saves/map_L16_CA_quicksave.json",
  "scenes": [
   "res://scenes/lol2/maps/L16_CA.tscn"
  ]
 },
 "L17_HC": {
  "scene": "res://scenes/lol2/maps/L17_HC.tscn",
  "format": "lol2-restoration-map-L17_HC",
  "label": "Subterranean Caverns",
  "kind": "act2",
  "legacy": "user://saves/map_L17_HC_quicksave.json",
~/opus_work/lol2_sol_playtest_starts/scripts/lol2/game_save.gd:21:	var slot: Variant = value.get("last_slot", 1)
~/opus_work/lol2_sol_playtest_starts/scripts/lol2/game_save.gd:119:		"native_bank":session.snapshot_bank(host),"session":{"options":{"adapter_exit_seeds":option if option is bool else session.adapter_exit_seeds},"last_slot":slot_id if slot_id != AUTOSAVE else session.last_slot}}
~/opus_work/lol2_sol_playtest_starts/scripts/lol2/game_save.gd:133:		if slot_id != AUTOSAVE: session.last_slot = slot_id
~/opus_work/lol2_sol_playtest_starts/scripts/lol2/game_save.gd:200:	var doc := {"area":area,"scene":row.scene,"area_save":read.state,"native_bank":{},"play_seconds":0.0,"session":{"options":{"adapter_exit_seeds":true},"last_slot":1}}
~/opus_work/lol2_sol_playtest_starts/scripts/lol2/game_save.gd:212:		"session":{"options":{"adapter_exit_seeds":false},"last_slot":1}}
~/opus_work/lol2_sol_playtest_starts/scripts/lol2/game_save.gd:244:	session.last_slot = int(doc.session.get("last_slot",1)) if slot_id == AUTOSAVE else slot_id
~/opus_work/lol2_sol_playtest_starts/scripts/lol2/game_save.gd:264:	var error := save(host,session.last_slot)
~/opus_work/lol2_sol_playtest_starts/scripts/lol2/game_save.gd:265:	_feedback(host,"Saved to slot %02d."%session.last_slot if error.is_empty() else "Save failed: "+error)
~/opus_work/lol2_sol_playtest_starts/scripts/lol2/game_save.gd:269:	var error := load_slot(host.get_tree(),session.last_slot)
~/opus_work/lol2_sol_playtest_starts/scripts/lol2/game_session.gd:9:var last_slot := 1
~/opus_work/lol2_sol_playtest_starts/scripts/lol2/game_session.gd:68:	return {"native_bank":snapshot_bank(),"adapter_exit_seeds":adapter_exit_seeds,"seed_pending":seed_pending,"play_seconds":play_seconds,"last_slot":last_slot,"pending_resume":pending_resume.duplicate(true),"changing_scene":changing_scene}
~/opus_work/lol2_sol_playtest_starts/scripts/lol2/game_session.gd:74:	last_slot = value.last_slot
~/opus_work/lol2_sol_playtest_starts/scripts/lol2/game_session.gd:81:	adapter_exit_seeds = true; seed_pending = false; play_seconds = 0.0; last_slot = 1; changing_scene = false
• Confirmed: F5 (`quicksave` at game_save.gd:264) saves to `session.last_slot`. After a checkpoint start, `_queue_scene(tree, doc, 1, false)` sets `session.last_slot = 1`. So if a user had a manual save in slot 1, pressed F2, picked an Act 2 start, then hit F5, their slot-1 save is overwritten.

  But wait — is this pre-existing behavior? `load_legacy` (game_save.gd:200, pre-existing) does exactly the same: slot_id 1 → last_slot = 1. So loading a legacy area save already sets last_slot=1 and F5 would overwrite slot 1. So the pattern pre-exists in load_legacy. However, load_slot(tree, slot_id) sets last_slot to the loaded slot — normal. The question: was this known/accepted behavior? The old F2 Act1 starts used `_verify_and_start` with meta resumes — what did last_slot become there? Let me check what the legacy meta-resume scenes do to session.last_slot. In the Act1 resume flow, the gate sets meta and changes scene directly (not through _queue_scene), so session.last_slot stays at default 1 (game_session.gd:9: `var last_slot := 1`). So pre-existing Act1 F2 starts also leave last_slot=1, and F5 writes slot 1. Hmm, so F5-after-F2 writing slot 1 is pre-existing behavior from the Act1 feature, consistent. The new code just extends it. It's arguably a pre-existing design wart, not a regression introduced by C-15. The task says "a start that can write over a user's own save or slot". The start itself doesn't write; F5 after the start writes slot 1 — same as the existing Act1 starts and legacy loads. I'd flag it as MINOR (pre-existing pattern, extended to new starts) or note it's consistent. Actually let me check the docs claim: "Pressing F5 afterwards saves to the normal area quicksave, as always" (old docs). New docs say "F5 afterwards writes a normal whole-game slot" — doesn't say which slot. Old docs said "saves to the normal area quicksave" — hmm, F5 = quicksave to last_slot. So with Act1 F2 starts, F5 wrote slot 1. Consistent. I'll note as MINOR.

  Now check whether Act1 behavior changed: the help text changed; follow_focus added (scrolling fix — this changes Act1 behavior slightly but beneficial and disclosed); `playtest_starts_test.gd` filtered entries to act==1, and list rows expected from all listed entries. `_build_playtest_starts` iterates `listed.entries` (all 21) — fine.

  Also in map branch of start_playtest: note it does NOT print "Playtest start:" log line nor hide the panel? Let me check what happens after `_verify_and_start` — does the panel get hidden? In the map branch, after resume_checkpoint succeeds, does starts_panel hide? Look at the flow: for the Act1 branch, `_verify_and_start` changes scene; the gate itself is replaced (current_scene changes). The panel belongs to the gate scene. Fine.

  Now check `read_legacy` for L8_SJ: Areas.ROWS["L8_SJ"] — need to see its kind/format. The darker format is "lol2-restoration-darker-jungle". Let me check ROWS for L8_SJ and L9_DR and validate_area's act2 branch.3:const PROGRESSION_AREAS := ["L8_SJ","L9_DR","L10_DC","L12_CM","L13_RC","L14_HT","L16_CA","L17_HC","L19_BC","L20_BB"]
4-const ROWS := {
5- "L10_DC": {
6-  "scene": "res://scenes/lol2/maps/L10_DC.tscn",
7-  "format": "lol2-restoration-map-L10_DC",
8-  "label": "Dracoid Cemetery",
9-  "kind": "act2",
10-  "legacy": "user://saves/map_L10_DC_quicksave.json",
11-  "scenes": [
12-   "res://scenes/lol2/maps/L10_DC.tscn"
13-  ]
--
65: "L19_BC": {
66-  "scene": "res://scenes/lol2/maps/L19_BC.tscn",
67-  "format": "lol2-restoration-map-L19_BC",
68-  "label": "Belial’s Laboratory",
69-  "kind": "act2",
70-  "legacy": "user://saves/map_L19_BC_quicksave.json",
71-  "scenes": [
72-   "res://scenes/lol2/maps/L19_BC.tscn"
73-  ]
74- },
75- "L1_DC": {
--
85: "L20_BB": {
86-  "scene": "res://scenes/lol2/maps/L20_BB.tscn",
87-  "format": "lol2-restoration-map-L20_BB",
88-  "label": "Birthing Chamber",
89-  "kind": "act2",
90-  "legacy": "user://saves/map_L20_BB_quicksave.json",
91-  "scenes": [
92-   "res://scenes/lol2/maps/L20_BB.tscn"
93-  ]
94- },
95- "L3_DH": {
--
136: "L8_SJ": {
137-  "scene": "res://scenes/lol2/darker_jungle.tscn",
138-  "format": "lol2-restoration-darker-jungle",
139-  "label": "Savage Jungle",
140-  "kind": "act2",
141-  "legacy": "user://saves/darker_jungle_quicksave.json",
142-  "scenes": [
143-   "res://scenes/lol2/darker_jungle.tscn"
144-  ]
145- },
146: "L9_DR": {
147-  "scene": "res://scenes/lol2/dragon_level.tscn",
148-  "format": "lol2-restoration-dragon-preview",
149-  "label": "Dracoid Ruins",
150-  "kind": "act2",
151-  "legacy": "user://saves/dragon_preview_quicksave.json",
152-  "scenes": [
153-   "res://scenes/lol2/dragon_level.tscn"
154-  ]
155- }
156-}
--
190:  "L8_SJ": ready = load("res://scripts/lol2/darker_jungle.gd").arrival_assets_ready()
191:  "L9_DR": ready = load("res://scripts/lol2/dragon_level.gd").arrival_assets_ready()
 var data: Variant = JSON.parse_string(FileAccess.get_file_as_string("res://assets/lol2/generated/original_floors/full_walk.json"))
 return data[0].checkpoints.size() + 2 if data is Array and not data.is_empty() else 0
static func validate_area(area: String, value: Variant) -> String:
 if not ROWS.has(area): return "Unknown saved area."
 match ROWS[area].kind:
  "cave": return load("res://scripts/lol2/walkthrough_save.gd").validate(value, cave_checkpoints())
  "museum": return load("res://scripts/lol2/museum_save.gd").validate(value)
  "hive": return load("res://scripts/lol2/hive_save.gd").validate(value)
  "jungle": return load("res://scripts/lol2/jungle_save.gd").validate(value, ROWS[area].format)
  _: return load("res://scripts/lol2/act2_save.gd").validate(value, ROWS[area].format)
static func prepare_area(area: String, value: Dictionary) -> Dictionary:
 var result := value.duplicate(true)
 if area == "L1_DC": result = load("res://scripts/lol2/walkthrough_save.gd").migrate_loaded(result)
 return result

## Match the opening gate's per-area checks before touching the live session.
## Native script bundles are optional for map preview, as on the existing gate.
static func assets_error(area: String) -> String:
 if not ROWS.has(area): return "Unknown saved area."
 var ready := true
 match area:
  "L3_DH": ready = load("res://scripts/lol2/museum_walkthrough.gd").assets_ready()
  "L4_HJ": ready = load("res://scripts/lol2/jungle_walkthrough.gd").assets_ready()
  "L5_HC": ready = load("res://scripts/lol2/hive_review.gd").assets_ready()
  "L7_DH": ready = load("res://scripts/lol2/dark_halls.gd").arrival_assets_ready()
  "L8_SJ": ready = load("res://scripts/lol2/darker_jungle.gd").arrival_assets_ready()
  "L9_DR": ready = load("res://scripts/lol2/dragon_level.gd").arrival_assets_ready()
  _:
   if area in PROGRESSION_AREAS: ready = load("res://scripts/lol2/act2_map.gd").map_assets_ready(area)
 return "" if ready else "%s assets are missing from this build." % ROWS[area].label
Wait — L8_SJ kind is "act2" but the existing `darker` F2 entry uses format `lol2-restoration-darker-jungle` via JungleSave.read_save(darker_save_path, Darker.FORMAT). `read_legacy` for L8_SJ falls into `_` branch → act2_save.read_save(path, "lol2-restoration-darker-jungle"). Does act2_save.read_save accept the darker format packet? The r12z packet was a darker jungle save. Presumably the team's tests passed. Note map_case asserts read.state.format == Starts.format_for(entry) — format_for returns Areas.ROWS["L8_SJ"].format = "lol2-restoration-darker-jungle". OK.

  Also L8_SJ "kind": "act2" with validate → act2_save.validate(value, "lol2-restoration-darker-jungle"). Fine if it passed.

  Now — duplicate PROGRESSION_AREAS: tools/prepare_playtest_starts.py defines its own copy; game_areas.gd has the authoritative one. The gdscript entry_error checks Areas.PROGRESSION_AREAS. Two sources, currently consistent (10 entries each: python has L8_SJ, L9_DR + 8 MAP_AREAS = 10; gdscript has 10). Consistent now, but duplicated — minor.

  Now check the staged files and SHA verification. The saves live in `assets/lol2/generated/playtest_starts/` (git-ignored, generated). Are they present in the worktree? Let me check and verify the SHAs match the manifest pins. That's a core check ("wrong or missing SHA checks"). Also verify provenance: compare staged files against the claimed sources? The sources are in AI_COMMS paths — I can spot-check a couple, e.g., act2-l8 sha256 9606beab... vs ~/AI_COMMS/act1_completion_20261017/r12z_qualification/campaign/userdata/act1_dark_halls_darker_arrival.json, and l9/l10 from the tar.gz. That verifies "provenance claims that do not match the files".

  Also check the act1 entries' SHAs unchanged: diff shows only additions to the JSON (entries appended) — the act1 entries weren't touched. Good, the diff confirms no changes to existing entries except... the diff context showed entries unchanged; only "scope" field changed and 10 entries appended. Verify no Act1 entry sha changed: diff only adds lines after line 414. The scope line changed — fine.

  Now check for full_health leaking into normal loads: `resume_checkpoint` is new and only called from the gate map branch with true and the tests. `start_full_health` gate var reset after use — unchanged behavior. The Act1 path unchanged.

  Check `prepare_playtest_starts.py` rest of the diff — the staging side. Let me view the whole file quickly, plus check the staged files' SHAs.

• Now verify the staged save files against their manifest pins, and spot-check provenance against claimed sources.act1_broken_earned_runes.json
act1_broken_flute_hive_return.json
act1_broken_hive_entry.json
act1_broken_museum_jungle.json
act1_broken_orb_monastery.json
act1_broken_repaired_monastery.json
act1_broken_runes_monastery_return.json
act1_broken_runes_translated.json
act1_broken_wax_upper_return.json
act1_dark_halls_darker_arrival.json
act1_magic_museum_arrival.json
c15_l10_dc.json
c15_l12_cm.json
c15_l13_rc.json
c15_l14_ht.json
c15_l16_ca.json
c15_l17_hc.json
c15_l19_bc.json
c15_l20_bb.json
c15_l8_sj.json
c15_l9_dr.json
_staged_receipt.json
act1-museum-arrival OK
act1-jungle-arrival OK
act1-hive-entry OK
act1-hive-flute-return OK
act1-hive-wax OK
act1-hive-runes OK
act1-monastery-runes OK
act1-monastery-orb OK
act1-runes-translated OK
act1-sword-repaired OK
act1-end-darker-jungle OK
act2-l8 OK
act2-l9 OK
act2-l10 OK
act2-l12 OK
act2-l13 OK
act2-l14 OK
act3-l16 OK
act3-l17 OK
act3-l19 OK
act3-l20 OK
9606beab57fdb8d246e3f322ba328a1ae965dba1027dda7b4eef5cb55d4c6425  ~/AI_COMMS/act1_completion_20261017/r12z_qualification/campaign/userdata/act1_dark_halls_darker_arrival.json
5a48df66f70a776d1a31c28d093f2e4370f148c35835417ee2199104da5902ca  ~/AI_COMMS/act1_completion_20261017/r12z_qualification/campaign/userdata/dark_halls_earned/depart.json


• All 21 staged files match their pins. L8's provenance claim checks out: act1_dark_halls_darker_arrival.json sha = 9606beab... matches the act2-l8 pin. Note the act2-l8 source.proof says "kept output depart_output_darker_arrival.json has this sha256" — but the actual file `depart.json` has a different sha (5a48df...). Let me check `depart_output_darker_arrival.json` exists.

  Also check the existing act1-end-darker-jungle entry: does it use the same source file (act1_dark_halls_darker_arrival.json)? The handoff says L8 aliases the existing r12z earned departure packet under a distinct filename. Compare c15_l8_sj.json with act1_dark_halls_darker_arrival.json staged — both sha 9606...? Check staged act1 file sha and the act1-end-darker-jungle manifest sha.act1-end-darker-jungle act1_dark_halls_darker_arrival.json 9606beab57fdb8d2 "~/AI_COMMS/act1_completion_20261017/r12z_qualification/campaign/userdata/act1_dark_halls_darker_arrival.json"
act2-l8 c15_l8_sj.json 9606beab57fdb8d2 "~/AI_COMMS/act1_completion_20261017/r12z_qualification/campaign/userdata/act1_dark_halls_darker_arrival.json"
capture
depart_darker_f5_quicksave.json
depart.json
depart_output_darker_arrival.json
enter_arrival_quicksave.json
enter.json
enter_output_quicksave.json
finish.json
finish_output_jungle_quicksave.json
resume.json
9606beab57fdb8d246e3f322ba328a1ae965dba1027dda7b4eef5cb55d4c6425  ~/AI_COMMS/act1_completion_20261017/r12z_qualification/campaign/userdata/dark_halls_earned/depart_output_darker_arrival.json
L8 aliasing confirmed. Note: act2-l8 and act1-end-darker-jungle are the same bytes under two entries. The act1-end-darker-jungle entry — what resume kind and does it have full_health? Check that entry: presumably resume "darker" with full_health true (previously approved). So there are now two F2 rows pointing at the same bytes: "Act 1 end darker jungle" (resume darker, heals via start_full_health) and "Act 2 - Savage Jungle arrival" (resume map, heals via resume_checkpoint). Consistent.

  Now check the Astra tar provenance for l9–l14. Verify the tar members and manifest sha.committed_patches
earned_saves_and_drafts.tar.gz
final_qualification
manifest.json
RESUME.txt
f75577355f3cb1eaf8c101435aa63afb0d6797a75d74b4316aaa402194345224  final_qualification/report.json
tmp/l12_larkhon_arrival_regression_anchor.json
tmp/l14_temple_entry_earned_save.json
tmp/l14_temple_arrival_earned_save.json
tmp/l9_pit_arrival_earned_save.json
tmp/l13_citadel_arrival_regression_anchor.json
tmp/l12_larkhon_arrival_earned_save.json
tmp/l14_temple_upper_entry_qualified_save.json
tmp/l10_gate_earned_save.json
tmp/l13_citadel_arrival_earned_save.json
tmp/l14_temple_arrival_qualified_save.json
tmp/l14_temple_entry_qualified_save.json
tmp/l12_larkhon_probe_arrival_save.json
6f9d174047977927af32457ccbb2e9df1ef332974e02b7adcf915854d25ea49f  l10_gate_earned_save.json
689badf57fb9f5bb34dad52c98a76026868bac407013b04ec40fcec56a1f38b5  l12_larkhon_arrival_earned_save.json
21db5d3f9596650ad96df594e103eca6eb79dea299d91e585e610b146622b948  l13_citadel_arrival_earned_save.json
761850f60b460772b31566ff0eb4201caba6e3d6d120ccc590bc64addb317c2f  l14_temple_arrival_earned_save.json
02de1113c40d183c3fdd780f205d4c41643a7df6149b857bc68d8f21b5375eda  l9_pit_arrival_earned_save.json
f2c469da0b4a477c3f6aa391d2a313993ce1a1ef6d5eb44ff3cbc3e28c771ccb  ~/opus_work/lol2_r18/tmp/l16_arrival_earned_save.json
678e3076befc3ff44ab183353448f1a664f99f900a33a14c8ad191622d411839  ~/opus_work/lol2_r18/tmp/l17_arrival_earned_save.json
f2cdf6b46a4701cc06a8987899f1510059f42eb4bc0400dd9a7e65fcf0017755  ~/opus_work/lol2_r18/tmp/l19_beast_wall_earned_save.json
576d17bb004fd11521770ffbc6a125cb6925806df508442c3ab44c7e408a43e5  ~/opus_work/lol2_r18/tmp/l20_dawn_curse_earned_save.json
9c22b4bdbeb8112ac3c2514c4dfdcaa8099a1af6389f0844d7fc827d4b065a51  ~/opus_work/lol2_r18/tmp/regressions/doors/report.json
f835c02686e0d0bb7290d87d3b1316efdeed8889ab340e3b287944d9c4452b62  ~/opus_work/lol2_r18/tmp/regressions/merge_97dce7e/report.json
All 10 SHAs match their claimed sources exactly:
  - l9: 02de1113 ✓, l10: 6f9d1740 ✓, l12: 689badf5 ✓, l13: 21db5d3f ✓, l14: 761850f6 ✓
  - l16: f2c469da ✓, l17: 678e3076 ✓, l19: f2cdf6b4 ✓, l20: 576d17bb ✓
  - proof report shas match too (f7557735, 9c22b4bd, f835c026).

  Now verify the identities in the manifest actually match the save contents (a quick check of a few, e.g. player.position and format for each new entry) — and check inventory.health values in the pinned files (to confirm "original-health" claims and that full health isn't already in the file; handoff says "original-health values" recorded in SOURCE_PINS.json — check that file in the handoff dir).

  Also verify:
  - input_sha256 claims for a few (e.g. act2-l8 input_save finish_output_jungle_quicksave.json sha = 3eb93c33...?).
  - The manifest identity values match actual file contents — the tests check this, but I can spot check that the test wouldn't vacuously pass. Spot-check act2-l9: format and position in the file.

  Also check health values: map_case records before_health. The docs claim health 30 applied on detached copy. Check a pinned file's inventory.health.

  Also check `full_health` flag on act1-end-darker-jungle (pre-existing) — confirm unchanged from parent.

  And check the "native puzzles may reset" claim and `native_bank: {}`.

  Also check map_case.gd for a subtle can't-fail: `assert(Vector2(...).length()<2.0)` fine. `assert(read.state.format==Starts.format_for(entry) and entry.full_health)` fine.

  One more: in `map_case.gd`, `var maps: Array=listed.entries.filter(func(e):return e.resume=="map")` — filter returns Array; fine. `assert(seen.size()==Starts.Areas.PROGRESSION_AREAS.size())` — 10==10 fine.

  Gate map branch: `_verify_save_access()` — check what it does; if it returns error it silently returns without showing status. In `_verify_and_start` same pattern. Consistent, fine.

  Check: does the map branch also verify `start_full_health` reset? Not needed.

  Potential issue: gate map branch doesn't check `Starts.manifest().error`? entry found from manifest; if manifest had error, entries may be empty. Fine.

  Now, `resume_checkpoint` validates with validate_area but does NOT check the format matches the area. validate_area for act2 → act2_save.validate(value, ROWS.format) — presumably checks format internally. Check act2_save.validate.

  Also check the identities in manifest vs actual content — quick spot check on all 10 new entries with a Python script replicating contains/excludes/values.

  Also check the SOURCE_PINS.json and provenance in the handoff dir to confirm aids recorded. And check that `input_sha256` for l8 matches finish_output_jungle_quicksave.json.

• All SHAs verify. Now let me validate the manifest identities against actual save contents, and check claimed input SHAs.act2-l8 health= 19 IDENTITY OK
act2-l9 health= 23 IDENTITY OK
act2-l10 health= 19 IDENTITY OK
act2-l12 health= 27 IDENTITY OK
act2-l13 health= 27 IDENTITY OK
act2-l14 health= 30 IDENTITY OK
act3-l16 health= 24 IDENTITY OK
act3-l17 health= 26 IDENTITY OK
act3-l19 health= 30 IDENTITY OK
act3-l20 health= 30 IDENTITY OK
3eb93c33de97fbfc631b7aaffd356b985e8cd98f41bed513fb80656a576a846b  ~/AI_COMMS/act1_completion_20261017/r12z_qualification/campaign/userdata/dark_halls_earned/finish_output_jungle_quicksave.json
ASTRA_SOURCE_COMMIT_COMPARISON.json
C15.patch
CHECKER_PIN.json
check_source_commits.py
driver.lock
evidence
EVIDENCE_PINS.json
final_autosave_test
final_game_save_apply_failure_test
final_game_save_source_test
FINAL_GATE.json
final_gate.py
final_player_foundation_source_test
final_playtest_checkpoint_adapter_test
final_playtest_map_starts_rendered_test
final_playtest_map_starts_test
final_playtest_start_full_health_test
final_playtest_starts_test
final_staging.log
final_staging_refusals.log
final_tool_userdata
HANDOFF.md
HONESTY_CHECK.json
IMAGES.md
LAUNCH_LIMITS.json
PATCH_CHECK.json
private_case.py
probe_adapter
probe_adapter2
probe_all10
probe_all10_v2
probe_all10_v3
probe_all10_v4
probe_rendered
probe_rendered2
provenance
READY.json
select_sources.py
SITE_AUDIT.json
SOURCE_COMMIT_COMPARISON.json
SOURCE_PINS.json
stage_userdata
staging
staging.log


• Identities all match; input SHA for l8 matches. Note act2-l14, l19, l20 already have health=30 in the pinned file — so the full-health adapter is a no-op for those; fine and consistent.

  Now check the provenance/SOURCE_PINS for aids disclosure and original health values. Also verify the claim "test_aids recorded" for early maps — the five Astra entries have test_aids; l8 entry does NOT have a test_aids field! Check: act2-l8 source has "scope" but no test_aids. The l8 source test is dark_halls_earned_detour_test at 1b775ba — did that test use aids (position/clock)? The handoff says "Some source tests own clocks/camera... late ones include supplied local positions/transition calls." Task says "aid is accepted if recorded in provenance". l8 lacks a test_aids field. But its scope says "Original qualified Act1 departure checkpoint reused byte-for-byte" — the r12z departure test was previously qualified/approved, so its aids (if any) were disclosed at that time. Let me check SOURCE_PINS.json to see if aids recorded there for l8.

  Also check the earlier entry for act1-end-darker-jungle — same packet already approved, so no new aid.

  Also, the L20 aid mentions "mother.cast_level4/5 refusal probe" — fine, disclosed.

  Now check remaining risk areas:

  1. F2 menu with 21 entries: scroll added with follow_focus; rows in ScrollContainer. The panel is full rect; heading+help+scroll+status+back. Should be OK. Keyboard focus scroll fixed. Fine.

  2. Privacy: committed manifest contains absolute paths ~/AI_COMMS/... and ~/opus_work/lol2_r18/... with username "bob". Check parent for pre-existing ~ in the manifest — the old act1 entries. Let me check parent version.

  3. docs/playtest-starts.md new version contains `~/AI_COMMS/sol_lane/task3_20261109/guarded_godot.py` — committed docs with absolute path including username. Pre-existing pattern (old docs also had ~ path). Worth a MINOR.

  4. The deviation doc: fine.

  5. Check the `_verify_save_access` silent return — pre-existing pattern.

  6. Check `playtest_starts.gd` entry_error: for map entries it checks `entry.get("area_id", "")` — fine. Note that FIELDS — check what FIELDS contains; does it include area_id? For map entries, area_id is accessed via .get so not required by FIELDS. But then `format_for`/`scene_for` would fail at runtime for a map entry without area_id... no, entry_error refuses map entries whose area_id isn't in PROGRESSION_AREAS, and "" isn't. OK.

  7. Check the map branch order in the gate: SHA check at top (file_error), then read, identity, pin recheck, verify access, resume. Good.

  8. One more check — `resume_checkpoint` sets `native_bank: {}`. Handoff discloses native reset. OK.

  9. Autosave: `_queue_scene` with legacy=false → pending_resume and meta "lol2_slot_resume" set. Map scenes may trigger arrival autosaves → could overwrite user's autosave slot. Disclosed in help text. The start itself doesn't write. Task item "a start that can write over a user's own save or slot": F5 after start writes slot 1 (last_slot=1). Pre-existing pattern from load_legacy and Act1 F2 (session default last_slot=1). Hmm wait — for the Act1 F2 branch, does the resumed scene save via F5 to slot 1? Yes since session.last_slot default is 1. So consistent pre-existing behavior. But is it a problem worth flagging? The docs say "Manual slots remain; ordinary eligible autosaves still apply". If a user's only save is manual slot 1 and they F5 after a playtest start, it overwrites slot 1 without prompt. That's a real user-data hazard, though pre-existing. I'll flag as MINOR (pre-existing semantics, now extended to 10 more entries) — actually the reviewer brief explicitly says "a start that can write over a user's own save or slot". The start itself doesn't. But last_slot=1 means the *subsequent* F5 targets slot 1. In normal flow, last_slot is the slot you loaded; after an F2 start there's no loaded slot, so writing slot 1 silently is questionable. Existing Act1 behavior had the same. I'll report MINOR.

  10. Test-that-cannot-fail check: adapter test `assert(not Save.resume_checkpoint(self,"L1_DC",packet,true).is_empty())` — L1_DC is not in PROGRESSION_AREAS so refused. Good. `bad.inventory.health=-1` refused by validate. Good.

  One thing in map_case.gd: after Enter tap, loop waits for scene change; if the start is blocked (e.g. status text), scene stays gate and after 1800 frames assert(scene!=null...) fails. Good, can fail.

  `assert(saves()==before, ...)` — but they created c15_sentinel.json before `before:=saves()`, so sentinel included in before. OK.

  Potential issue in map_case.gd: `var gate:=await new_gate()` — creates a new gate per area (10 times), sets `gate.path_field.text=OS.get_environment("LOL2_ORIGINAL_GAME_EXE")` — env required; registry needs env only listed for playtest_starts_test, not the new map tests! Check registry: playtest_map_starts_test.json needs.chain only — no "env": ["LOL2_ORIGINAL_GAME_EXE"]. If the test needs that env var and registry doesn't declare it, the runner may not provide it → gate path_field empty → original game verification fails → starts blocked → test would fail (not silently pass). Hmm, but private_case.py driver probably sets env. Also `_verify_save_access()` — check what it requires: original_game_verified meta? In `_queue_scene`, verification required only if OS.has_feature("original_game_required"). In test builds the feature may be off. Let me check _verify_save_access.

  Also rendered test registry has "args": ["--demo-interface"]. OK.

  Let me check _verify_save_access and whether original_game_required feature is set in tests. Also check `Starts.manifest()` error handling.

  11. Check the git-ignored status: assets/lol2/generated/playtest_starts/ — is it git-ignored so the staged saves aren't committed? `git status` and check .gitignore. The commit didn't include the save files (diff --stat shows no assets). Good. But then a fresh checkout of fde4d19 lacks staged files → rows disabled "(not in this build)". Docs say that. Fine.

  12. Also verify the map branch handles `entry.full_health` — the gate hardcodes true. entry_error enforces true. Consistent. But `resume_checkpoint`'s full_health param from gate is hardcoded true — so manifest full_health flag is decorative beyond validation. Fine.

  13. Check `playtest_starts_test.gd` line: entries filtered to act==1 — `int(e.act)` — manifest act1 entries have act:1. Good. And the rows check now expects all 21 titles — and requires every row enabled (all saves staged). Fine.

  14. One more possible problem: `docs/playtest-starts.md` says `--playtest-start=ID` removed? Old docs mention CLI flags; new docs dropped them. Did the commit remove CLI support? No code change to CLI parsing visible. Only docs. The new docs omit mention of `--playtest-starts` / `--playtest-start=ID` — a docs regression (feature presumably still exists). Minor.

  Let me check whether gate CLI still handles those flags.

  15. Check `_verify_save_access`:

• Identities and input SHAs check out. Let me look at a few remaining code paths and the provenance records.12:const Starts = preload("res://scripts/lol2/playtest_starts.gd")
65:		starts.pressed.connect(show_playtest_starts)
157:		if argument.begins_with("--playtest-start=") and not path_field.text.is_empty():
158:			start_playtest.bind(argument.trim_prefix("--playtest-start=")).call_deferred()
161:		show_playtest_starts.call_deferred()  # opens the list instead of the automatic new-game start below
173:## earned save from the automated campaign (scripts/lol2/playtest_starts.json), staged read-only under res://.
179:		else: show_playtest_starts()
182:func show_playtest_starts() -> void:
183:	if starts_panel == null: _build_playtest_starts()
188:func _build_playtest_starts() -> void:
375:func _verify_save_access() -> String:
376-	get_tree().set_meta("original_game_verified", false)
377-	var error := Check.verify(path_field.text)
378-	if not error.is_empty():
379-		status.text = error
380-		print("Original game verification blocked: ", error)
381-		return error
382-	var config := ConfigFile.new()
383-	config.set_value("original_game", "exe_path", path_field.text)
384-	config.save(settings_path) # Only the path is remembered; never cache approval.
385-	get_tree().set_meta("original_game_verified", true)
386-	print("Original game executable verified (SHA-256).")
387-	return ""
388-
389-func _continue_save() -> void:
390-	if not _verify_save_access().is_empty():return
<class 'dict'>
{
 "L8_SJ": {
  "save": "c15_l8_sj.json",
  "sha256": "9606beab57fdb8d246e3f322ba328a1ae965dba1027dda7b4eef5cb55d4c6425",
  "source": {
   "test": "dark_halls_earned_detour_test",
   "commit": "1b775ba8cee72ebee1da4c6cb0f807be6f4d8c9a",
   "campaign": "r12z qualification campaign 2026-11-02 (AI_COMMS/act1_completion_20261017/r12z_qualification, source 1b775ba)",
   "leg": "11-13_dark_halls",
   "proof": "AI_COMMS/act1_completion_20261017/r12z_qualification/campaign/userdata/dark_halls_earned/depart.json (kept output depart_output_darker_arrival.json has this sha256); audit_dark_halls_detour_chain.txt PASS",
   "path": "~/AI_COMMS/act1_completion_20261017/r12z_qualification/campaign/userdata/act1_dark_halls_darker_arrival.json",
   "input_save": "~/AI_COMMS/act1_completion_20261017/r12z_qualification/campaign/userdata/dark_halls_earned/finish_output_jungle_quicksave.json",
   "input_sha256": "3eb93c33de97fbfc631b7aaffd356b985e8cd98f41bed513fb80656a576a846b",
   "input_note": "phase depart resumed the phase-finish F5 Jungle save; the detour chain started from act1_broken_repaired_monastery.json (ee4a4e45...)",
   "scope": "Original qualified Act1 departure checkpoint reused byte-for-byte; no unaided whole-campaign claim added."
  },
  "health": 19
 },
 "L9_DR": {
  "save": "c15_l9_dr.json",
  "sha256": "02de1113c40d183c3fdd780f205d4c41643a7df6149b857bc68d8f21b5375eda",
  "source": {
   "test": "l8_pit_earned_test",
   "commit": "fc1b45c2c44c921e86b8a665dd299593c6f3b6df",
   "input_sha256": "3373d698a0deb9c8a615ee0b092dd0141de8403f7365ee10fb8faffceb228add",
   "path": "~/AI_COMMS/astra_lane/packup_20261103T122345Z/earned_saves_and_drafts.tar.gz",
   "proof": "~/AI_COMMS/astra_lane/packup_20261103T122345Z/final_qualification/report.json",
   "proof_sha256": "f75577355f3cb1eaf8c101435aa63afb0d6797a75d74b4316aaa402194345224",
   "scope": "Qualified game-written earned-route checkpoint; not an unaided campaign chain.",
   "test_aids": [
    "Clock/camera ownership and production action helper calls; grounded route movement. See pinned producer source."
   ],
   "archive_member": "tmp/l9_pit_arrival_earned_save.json",
   "archive_manifest_sha256": "976d6e10db6633e35d084796cf355f8f225d711810f29b158bf15d63dba2af38",
   "input_member": "tmp/l8_pit_rim_earned_save.json"
  },
  "health": 23
 },
 "L10_DC": {
  "save": "c15_l10_dc.json",
  "sha256": "6f9d174047977927af32457ccbb2e9df1ef332974e02b7adcf915854d25ea49f",
  "source": {
   "test": "l10_gate_earned_test",
   "commit": "fc1b45c2c44c921e86b8a665dd299593c6f3b6df",
   "input_sha256": "065d4b814569c069490c0b4625177862918b2798ea504acf6ae89172b83baa92",
   "path": "~/AI_COMMS/astra_lane/packup_20261103T122345Z/earned_saves_and_drafts.tar.gz",
   "proof": "~/AI_COMMS/astra_lane/packup_20261103T122345Z/final_qualification/report.json",
   "proof_sha256": "f75577355f3cb1eaf8c101435aa63afb0d6797a75d74b4316aaa402194345224",
   "scope": "Qualified game-written earned-


• Good. Now check the archive_manifest_sha256 claim: 976d6e10... — verify against the packup manifest.json. And check test_aids claimed by the manifest vs. the actual producer tests: "Clock/camera ownership and production action helper calls" — spot check one producer test source at commit fc1b45c? That's in a different repo (lol2_astraprogression?). Maybe check ASTRA_SOURCE_COMMIT_COMPARISON.json instead. The task focus is the commit under review; provenance spot checks are done. Let me verify archive_manifest_sha256 quickly and check the health values recorded in SOURCE_PINS match the pinned files (health 19/23 ✓ vs computed earlier — yes: l8 19, l9 23, l10 19... SOURCE_PINS records "health": 19, 23. Good.

  Now remaining checks:

  1. Privacy/paths in committed files: scripts/lol2/playtest_starts.json has ~ paths and docs too. Check parent had them as well — if pre-existing convention, severity lower. Let me check parent's playtest_starts.json.

  2. Check `.gitignore` covers the staged saves (they're generated). Diff didn't include them, and git check-ignore.

  3. Check FINAL_GATE.json claims — not part of commit, but the review targets the commit. Skip deep.

  4. UI with 21 entries: the map_case rendered test checks focus scrolls into view. follow_focus = true. OK.

  5. Check that the Act 1 behavior unchanged: game_save.gd added resume_checkpoint only; original_game_gate.gd changed help text, follow_focus, added map branch. The map branch is before `var path := Starts.save_path(entry)` — for non-map entries, unchanged. One subtlety: previously for unknown resume kinds, `match` fell through with no branch setting a path... entry_error refuses unknown kinds anyway. Fine.

  6. `playtest_starts.gd` `format_for`/`scene_for` added; validator updated. OK.

  7. Check `read()` for map: `load("res://scripts/lol2/game_save.gd").read_legacy(entry.area_id,path)` — uses load() each call, fine.

  8. Wait — one thing in map_case.gd: `assert(read.state.format==Starts.format_for(entry) and entry.full_health)`. For L8_SJ, format is darker-jungle ✓.

  9. Registry order 1343 for three tests — handoff says "Registry1157 passes; three new cases use1343 ties". Duplicate order values might be a registry violation but they say it passes. Check how registry validates order uniqueness? Quick check of another registry file with same order? Skip — they claim audit passed; can't run.

  10. Docs mention "--playtest-start=ID" no longer — actually the CLI flag still exists (line 157). New docs dropped documentation of CLI flags. MINOR docs regression.

  11. Now the F5-into-slot-1 question — also confirm `save(host, session.last_slot)` — F5 key binding. Look at game_save.gd:260-270.

  12. Also potential problem: the gate map branch runs `Starts.read(entry)` which parses JSON — a malformed-but-sha-matching file can't exist unless pin matches; pin recheck after read. OK.

  13. Check `validate_area` for act2 → act2_save.validate — does it check format matches? Let me check act2_save.validate quickly.

  14. Also, does `_queue_scene` pending_resume path write anything to disk? No — it only changes scene. The map scene itself may autosave on arrival ("ordinary eligible autosaves still apply") — disclosed.

  15. Check the FIELDS in playtest_starts.gd to see if "act" is required etc.extends RefCounted
## Playtest start points (docs/playtest-starts.md; owner request: start at a story checkpoint instead of replaying hours).
## scripts/lol2/playtest_starts.json lists REAL earned saves written by the automated campaign/route tests, in story
## order, each pinned by sha256. tools/prepare_playtest_starts.py stages the files into SAVE_DIR (generated media,
## git-ignored, exported through the assets/*.json include filter). The original-game gate shows the list and starts an
## entry through its existing "Resume <area>" branch with the staged res:// file as the save path: the same reader,
## validator, resume meta and scene as a normal resume. Nothing is injected and the player's own quicksaves are not touched.
const MANIFEST := "res://scripts/lol2/playtest_starts.json"
const SAVE_DIR := "res://assets/lol2/generated/playtest_starts/"
const Areas = preload("res://scripts/lol2/game_areas.gd")
const MuseumSave = preload("res://scripts/lol2/museum_save.gd")
const JungleSave = preload("res://scripts/lol2/jungle_save.gd")
const HiveSave = preload("res://scripts/lol2/hive_save.gd")
## Fixed Act1 branches and the whole-game checkpoint resume for whitelisted Act2/3 maps.
const KINDS := {
	"map": {}, # area_id resolves format/scene through the whole-game area catalog.
	"museum": {"format": "lol2-restoration-museum", "scene": "res://scenes/lol2/museum_walkthrough.tscn", "area": "Museum"},
	"jungle": {"format": "lol2-restoration-jungle", "scene": "res://scenes/lol2/jungle_walkthrough.tscn", "area": "Jungle"},
	"hive": {"format": "lol2-restoration-hive", "scene": "res://scenes/lol2/hive_review.tscn", "area": "Hive"},
	"darker": {"format": "lol2-restoration-darker-jungle", "scene": "res://scenes/lol2/darker_jungle.tscn", "area": "Darker Jungle"},
	"dark_halls": {"format": "lol2-restoration-dark-halls", "scene": "res://scenes/lol2/dark_halls.tscn", "area": "Dark Halls"},
}
const FIELDS := ["id", "title", "act", "area", "resume", "save", "sha256", "source", "identities"]
## Provenance every entry pins (lead addendum 2026-11-03): producing test, the commit it ran on, and the input save's sha256
## (null only for a leg that starts a new game; Act 2 *_qualified_save.json files already record theirs).
const SOURCE_FIELDS := ["test", "commit", "input_sha256"]

## The manifest's entries, in order. {"error": String, "entries": Array}; any malformed entry makes the whole list an error.
static func manifest(path: String = MANIFEST) -> Dictionary:
	if not FileAccess.file_exists(path): return {"error": "Playtest start list missing.", "entries": []}
	var data: Variant = JSON.parse_string(FileAccess.get_file_as_string(path))
	if not data is Dictionary or int(data.get("schema", 0)) != 1 or not data.get("entries") is Array:
		return {"error": "Playtest start list is damaged.", "entries": []}
	var ids := {}
	var saves := {}
	for entry in data.entries:
		var error := entry_error(entry)
		if error.is_empty() and (ids.has(entry.id) or saves.has(entry.save)): error = "duplicate id or save"
		if not error.is_empty():
			return {"error": "Playtest start list entry invalid: %s (%s)" % [str(entry.get("id", "?")) if entry is Dictionary else "?", error], "entries": []}
		ids[entry.id] = true
		saves[entry.save] = true
	return {"error": "", "entries": data.entries}

static func entry_error(entry: Variant) -> String:
	if not entry is Dictionary: return "not an object"
	for field in FIELDS:
		if not entry.has(field): return "missing " + field
	if not KINDS.has(str(entry.resume)): return "unknown resume kind " + str(entry.resume)
	if str(entry.resume) == "map":
		if entry.get("area_id", "") not in Areas.PROGRESSION_AREAS: return "unknown playtest map"
		var expected_act := 3 if str(entry.area_id) in ["L16_CA","L17_HC","L19_BC","L20_BB"] else 2
		if entry.get("act") != expected_act: return "map act disagrees with area"
		if entry.get("full_health") != true: return "map start requires full_health"
	if entry.has("full_health") and not entry.full_health is bool: return "full_health is not boolean"
	var save := str(entry.save)
	if not save.is_valid_filename() or not save.ends_with(".json"): return "unsafe save name"
	var sha := str(entry.sha256)
	if sha.length() != 64 or not sha.is_valid_hex_number(): return "bad sha256"
	if str(entry.title).strip_edges().is_empty(): return "empty title"
20:static func validate(state: Variant, format: String) -> String:
21-	var error := Legacy.validate(state, format)
22-	if not error.is_empty(): return error
23-	error = quests_error(state.quests)
24-	if not error.is_empty(): return error
25-	if state.inventory.collected.size() + state.quests.get("act2_items", {}).get("carried", []).size() > 64: return "Inventory exceeds capacity."
26-	if state.player.has("region"):
27-		# Optional (BK01 follow-up): the region the region-aware collision tracked for the body when the save was written.
28-		var region: Variant = state.player.region
29-		if not (region is int or region is float) or region != int(region) or int(region) < 0 or int(region) > 65535: return "Invalid player region."
30-	return ""
31-static func read_save(path: String, format: String) -> Dictionary:
32-	var file := FileAccess.open(path, FileAccess.READ)
		session.rollback_load("Could not open the saved area; current game preserved.")
		return "Could not open the saved area; current game preserved."
	return ""

static func load(tree: SceneTree, slot_id: int, use_backup: bool = false) -> String:
	return load_slot(tree, slot_id, use_backup)

static func quicksave(host: Node) -> String:
	var session: Node = Session.for_tree(host.get_tree())
	var error := save(host,session.last_slot)
	_feedback(host,"Saved to slot %02d."%session.last_slot if error.is_empty() else "Save failed: "+error)
	return error
static func quickload(host: Node) -> String:
	var session: Node = Session.for_tree(host.get_tree())
	var error := load_slot(host.get_tree(),session.last_slot)
	if not error.is_empty(): _feedback(host,"Load failed: "+error)
	return error
static func _feedback(host: Node, text: String) -> void:
	if host.has_method("save_feedback"):host.save_feedback(text)
	elif host.has_method("_save_feedback"):host._save_feedback(text)
	elif host.get("status") is Label: host.get("status").text=text
21
assets/lol2/generated/playtest_starts/c15_l8_sj.json
IGNORED
976d6e10db6633e35d084796cf355f8f225d711810f29b158bf15d63dba2af38  ~/AI_COMMS/astra_lane/packup_20261103T122345Z/manifest.json
- Parent's manifest already had 21 occurrences of `~` (Act1 entries used absolute paths too) → the new absolute paths follow the existing convention. Still worth a MINOR note since the review brief flags it.
  - archive_manifest_sha256 976d6e10... matches manifest.json ✓.
  - Staged files git-ignored ✓.
  - quicksave uses session.last_slot → after a checkpoint start, F5 writes slot 1. Pre-existing pattern (load_legacy does the same, and Act1 F2 resume left default last_slot=1). The new docs removed the old "Pressing F5 afterwards saves to the normal area quicksave" claim and now say "F5 afterwards writes a normal whole-game slot" without saying it targets slot 1. This is a real user-data hazard: user loads F2 start, hits F5, silently overwrites their manual slot 1. But wait — is this new? For Act1 F2 starts the same. Since the brief asks to look for "a start that can write over a user's own save or slot", I should flag it. Severity: it predates C-15 (same for legacy loads and Act1 starts), so arguably not a regression, but C-15 extends it and the docs now claim "Manual slots remain". I'll call it MAJOR? Hmm. The start itself does not write. The hazard requires the user to press F5 afterward, and the feedback says "Saved to slot 01." The behavior matches load_legacy (accepted Plan3 behavior, approved parent). Since the parent was approved with this exact last_slot=1 semantics in load_legacy, and the old F2 starts had the same F5→slot-1 outcome, I'll grade MINOR-to-MAJOR. I'll say MINOR (pre-existing semantics inherited from approved load_legacy; not introduced here), but mention it clearly.

  Wait, actually let me double check Act1 F2 path: `_verify_and_start` sets meta and changes scene via `get_tree().change_scene_to_file`? It doesn't call _queue_scene, so session.last_slot stays at whatever default (1) — yes same.

  Now, remaining things to verify:

  1. Does `resume_checkpoint` check that state's format matches area? act2_save.validate → Legacy.validate(state, format) — presumably checks format field. Let me confirm Legacy.validate checks format. Quick grep.

  2. The gate map branch order: `file_error` first (top of start_playtest) → good; read; identity; pin recheck; verify access; resume. Good.

  3. `manifest()` — entries iterated; entry_error ensures area_id whitelist. Also duplicate `save` names refused. Good.

  4. Check that `full_health` isn't applied elsewhere: `start_full_health` still only used for darker branch. grep start_full_health.

  5. Rendered test registry has `"args": ["--demo-interface"]`. The map_case rendered asserts `root.get_visible_rect().intersects(rect)`. OK.

  6. One more possible can't-fail: in map_case, `if current_scene!=gate and is_instance_valid(current_scene): scene=current_scene; if session.pending_resume.is_empty() and not session.changing_scene: break` — if pending_resume never empties, loop ends after 1800 frames with scene set but conditions unmet; then `assert(session.pending_resume.is_empty()...)` fails. Good.

  7. The `tap(KEY_ENTER)` — with button focused, Enter activates. OK.

  8. `assert(saves()==before, ...)` — but during the loop, starting maps might autosave if autosave enabled. Private case disables autosave — the driver sets something? Can't verify driver; acceptable.

  9. Docs: new playtest-starts.md drops `--playtest-starts`/`--playtest-start=ID` docs while feature remains (gate line 157-161). MINOR docs gap.

  10. Also check: `playtest_starts.json` new scope says "Act2/3 map starts use Plan3 checkpoint resume, disable preview seeds and set full health on a detached copy." OK.

  11. `tools/prepare_playtest_starts.py` — `describe()` override: `if fmt == 'lol2-restoration-darker-jungle': kind = 'map'` — this means describe no longer reports the darker kind for darker-format saves, which is also used by Act1 F2 darker entries. It only affects the describe helper output (a scaffolding tool), and the L8 map entry legitimately uses it. But if someone describes the Act1 darker save they'd get 'map' with area_id L8_SJ — mildly confusing, intended.

  Also check prepare tool's staging validation path for map entries — does the validator (validate_playtest_starts.gd) get invoked with format_for? Yes updated. Does prepare check entry full_health etc.? load_manifest does. OK.

  12. Check for potential issue: KIND_BY_FORMAT now maps 'lol2-restoration-darker-jungle' → 'darker' still in dict, plus describe override. And 'map' in KIND_BY_FORMAT.values() — yes via map formats. load_manifest check `entry['resume'] not in KIND_BY_FORMAT.values()` — 'map' is a value ✓.

  13. Registry order ties 1343 ×3 — check if registry requires unique orders; there might be existing ties. Quick grep for '"order": 1343' elsewhere... skip, the claim "Registry1157 passes" is outside commit. Actually a registry checker runs in CI maybe. Let me quickly check if duplicate order values already exist in the registry.

  14. Privacy: owner names — "lead", "owner" appear in docs/deviation text ("Owner C-15", "lead accepts"). Owner names like "bob" in paths. Pre-existing convention in this repo (parent had 21 ~ occurrences). MINOR.

  15. Check that the diff doesn't touch Act1 save flow: game_save.gd only adds resume_checkpoint. original_game_gate.gd help text + follow_focus + map branch. playtest_starts.gd adds map kind + checks. Act1 KINDS unchanged. `start_playtest` Act1 path unchanged. ✓.

  16. One more: help text says "older checkpoints can reset native puzzles on other maps" — actually it's the NEW Act2/3 checkpoints whose legacy area files lack a native bank and thus reset native puzzles on other maps; the Act1 ones use the meta-resume path which... also doesn't carry native bank. Wording "older checkpoints" is wrong/misleading — the new Act2/3 area files are the ones that predate the native bank ("These old area files lack a visited-level native bank"). "Older" is ambiguous but arguably refers to old-format files. Eh, MINOR wording.

  Let me quickly check registry order uniqueness and Legacy.validate format check.~/opus_work/lol2_sol_playtest_starts/tests/registry/playtest_checkpoint_adapter_test.json:5:  "order": 1343,
~/opus_work/lol2_sol_playtest_starts/tests/registry/playtest_map_starts_test.json:5:  "order": 1343,
~/opus_work/lol2_sol_playtest_starts/tests/registry/area_face_claims_test.json:5:  "order": 1343,
~/opus_work/lol2_sol_playtest_starts/tests/registry/playtest_map_starts_rendered_test.json:5:  "order": 1343,
Order 1343 ties pre-exist (area_face_claims_test.json already had 1343). Fine.

  Find the Legacy.validate used by act2_save:4:const Legacy = preload("res://scripts/lol2/jungle_save.gd")
13:static func validate_inventory(state: Variant) -> String:
14-	if not state is Dictionary: return "Invalid inventory."
15-	if state.has("magic"):
16-		var magic := preload("res://scripts/lol2/player_magic_state.gd").restore(state.magic)
17-		if magic.has("error"): return magic.error
18-	if state.has("fighting"):
19-		var fighting := preload("res://scripts/lol2/player_fighting_transport.gd").restore(state.fighting)
20-		if fighting.has("error"): return fighting.error
21-	if state.has("health") and (not Museum.within(state.health,1,PlayerHealth.MAXIMUM) or state.health != int(state.health)): return "Invalid player health."
22-	if state.has("player_form") and not preload("res://scripts/lol2/player_form_body.gd").valid(state.player_form): return "Invalid player form."
23-	if state.has("curse") and not preload("res://scripts/lol2/player_curse.gd").valid(state.curse,state.get("player_form",0)): return "Invalid curse state."
24-	var ids = state.get("collected")
25-	if not ids is Array or ids.size() > Catalog.MAX_CARRIED: return "Invalid collected items."
--
38:static func validate(state: Variant, expected_format: String = FORMAT) -> String:
39-	if not state is Dictionary or state.get("format") != expected_format or not Numbers._number(state.get("version")) or state.get("version") != 1:
40-		return "Unsupported area save."
41-	var error := validate_inventory(state.get("inventory"))
42-	if not error.is_empty(): return error
43-	error = Quests.validate(state.get("quests",Quests.initial()))
44-	if not error.is_empty(): return error
45-	error = preload("res://scripts/lol2/player_item_state.gd").transport_error(state.inventory,state.get("quests",{}))
46-	if not error.is_empty(): return error
47-	error = preload("res://scripts/lol2/player_magic_state.gd").transport_error(state.inventory,state.get("quests",{}))
48-	if not error.is_empty(): return error
49-	error = preload("res://scripts/lol2/player_fighting_transport.gd").transport_error(state.inventory,state.get("quests",{}))
50-	if not error.is_empty(): return error
validate checks format, health range, etc. So `resume_checkpoint` → `Areas.validate_area` does verify format against the area's expected format. Good — a mismatched area_id/format is refused.

  Note: validate checks health within 1..MAXIMUM, so a pinned save with health 30 passes, and healing to MAXIMUM=30. Verify player_health.MAXIMUM == 30.

  Also — one more thing: the gate map branch reads with `Starts.read(entry)` which uses `read_legacy(entry.area_id, path)` → for L8_SJ kind "act2" → act2_save.read_save(path, "lol2-restoration-darker-jungle"). And validate in resume_checkpoint — act2_save.validate(value, darker format) — fine.

  Now check player_health.MAXIMUM = 30:4:const MAXIMUM:=30
6:var _current:int=MAXIMUM
18:	set_value(mini(MAXIMUM,_current+amount));return _current
6:var adapter_exit_seeds := true
55:	adapter_exit_seeds = enabled
61:	return adapter_exit_seeds
68:	return {"native_bank":snapshot_bank(),"adapter_exit_seeds":adapter_exit_seeds,"seed_pending":seed_pending,"play_seconds":play_seconds,"last_slot":last_slot,"pending_resume":pending_resume.duplicate(true),"changing_scene":changing_scene}
71:	adapter_exit_seeds = value.adapter_exit_seeds
{
 "complete": true,
 "passed": true,
 "source_stable": true,
 "source_changed_files": [],
 "source_start": {
  "project.godot": "3b8050db16b404e6d2f8cee62fb2c412b1572bf52cdfc285b7fb71ef290bddf4",
  "scenes/lol2/act2_jungle_return.tscn": "6409326f1bb8973ed5affe0ecde55dc170bfcac6ad35753d24b2558358de31e7",
  "scenes/lol2/all_maps_indexed_review.tscn": "8a903dc494775b2bf1abdd1a547ffba77f691b67c414323825628bdd4d2728c7",
  "scenes/lol2/all_maps_review.tscn": "ccb4a9bcf87ccd5f545093ceeec980c077107ceac539beb10577a9e9b58d0976",
  "scenes/lol2/capsule_traversal_audit.tscn": "60d2f70eff00bbc4873825e4f64ca4cb637cdfd2896bb767c06b6982cc4fd2a4",
  "scenes/lol2/cave_encounter.tscn": "04c79869c527059391caeb8e594d7d0a2b6c4c69522ac2a194113278e4a4b74c",
  "scenes/lol2/cave_study.tscn": "1b741fa379d5038f0ee21511e8d514038b7937db8d1689f80d0de08fd13e1ce7",
  "scenes/lol2/cave_video_review.tscn": "631b145cadeddecf54ca916101a451244c4b7f30335c5f7d2de6a5f5d4d43fdb",
  "scenes/lol2/cave_walkthrough.tscn": "20c7c8fd89d7a411e19ae0c929f1092433cdeffc332e71e2de580319faad9dd7",
  "scenes/lol2/dark_halls.tscn": "9aad998681963fbc9e9186c051bcd90c1e3195dd07f98b2389775352b367144d",
  "scenes/lol2/darker_jungle.tscn": "aa23208395a682f1d6328f2e908255e77a3a51dd2a18c8680610d67f59d0b465",
  "scenes/lol2/dragon_level.tscn": "4c35f4eac9af23d10ce984651b7b28356ea4708ea0746b7f8ad7fda966645da7",
  "scenes/lol2/floor_collision_audit.tscn": "fa3ebf5993188c3cdaa6fa432c71894b930329c5645a84c676f7ef377abf9322",
  "scenes/lol2/hive
MAXIMUM = 30 ✓.

  One thing to double check: `_queue_scene` in resume_checkpoint passes `legacy=false`, so `session.set_seed_override(bool(doc.session.options.adapter_exit_seeds))` → false. Note: `set_seed_override(false)` — check semantics: seed override disabled means no preview seeds. The test asserts `not scene.adapter_exit_seeds`. OK.

  But wait — session default `adapter_exit_seeds := true` (game_session.gd:6). In normal game flow after new game, is adapter_exit_seeds true? For ordinary slot loads, doc.session.options.adapter_exit_seeds comes from the saved doc (line 119: option from session at save time). For checkpoint, false. So checkpoint starts disable exit seeds — meaning area-exit adapter seeds are off. Handoff says "Preview/exit seeds are disabled." Intended.

  Now — does disabling exit seeds hurt normal play after the checkpoint? When the player later saves with F5 (whole-game slot), doc records adapter_exit_seeds = session.adapter_exit_seeds = false, and later loads keep it false. So a playthrough started from an F2 checkpoint permanently loses adapter exit seeds (whatever gameplay effect they have — probably seeding道具 on area exit when arriving without having visited). That's by design per the handoff ("no preview/exit seeds are granted" — to avoid inventing state). Disclosed. Fine.

  Also check: does anything verify the pinned file is present at runtime in exported builds? Row disabled if missing. Fine.

  One more potential issue: `start_playtest` map branch doesn't set `start_full_health=false` — but it never sets it; previous Act1 call resets after use. OK.

  Also, the map branch in `start_playtest` — after a successful resume_checkpoint, it doesn't update starts_status from status. Minor.

  Now the "rendered test needs env" question: playtest_map_starts_test.json registry needs lacks "env": ["LOL2_ORIGINAL_GAME_EXE"] while map_case.gd does `gate.path_field.text=OS.get_environment("LOL2_ORIGINAL_GAME_EXE")`. If env missing, path_field empty → Check.verify fails → start blocked → test fails (not silently pass). But the private driver (private_case.py) may set it. Registry "needs" for the old playtest_starts_test lists env; new ones don't. Inconsistent but would cause failure not false-pass. MINOR at most. Actually wait — the pre-existing playtest_starts_test registry listed needs.env; the new map tests run the same gate verification, so they need the same env. If the runner only provides env vars listed in needs, the new tests would break. But handoff claims they passed via private_case.py driver. MINOR.

  Also check map_case.gd `new_gate()`: uses `gate.path_field.text=OS.get_environment("LOL2_ORIGINAL_GAME_EXE")`. And `_verify_save_access` verifies sha of exe. OK.

  Now privacy check for committed files: new committed files with ~: playtest_starts.json (source paths), docs/playtest-starts.md (guarded_godot.py path), docs/deviations row (no paths). Parent manifest already had ~ paths (21 occurrences), so convention pre-exists. Still flagged per brief → MINOR.

  Test aid disclosure: l8's manifest entry lacks `test_aids` — but its source is the previously approved r12z departure packet (same as act1-end-darker-jungle), and the handoff says first-visit source aids aren't newly granted. The dark_halls_earned_detour_test at 1b775ba — was it aided? It's an "earned detour" test from the approved Act1 work. Its scope says "no unaided whole-campaign claim added". Acceptable.

  Also check: does the manifest entry act2-l9 title say "pit arrival" while area says Dracoid Ruins — the L9_DR row label is "Dracoid Ruins" ✓. L17 label "Subterranean Caverns" but entry area "Huline Caverns" — cosmetic, docs table says Huline Caverns. Minor inconsistency, not worth a finding... maybe skip.

  Check: ten entries, story order L8→L20 appended after Act1 entries — the F2 list shows Act1 entries first then Act2/3 — story order preserved ✓.

  Potential real issue hunt — "tests that cannot fail":
  - `playtest_starts_test.gd`: `check(rows.all(...not row.disabled), "every row is enabled (all saves staged)")` — still requires staged. OK.
  - map_case: strong asserts. One soft spot: `assert(Vector2(...).length()<2.0)` tolerance for horizontal position — lenient but intended (Y settling note says horizontal preserved; 2.0 units tolerance is quite loose actually — a position could be off by 2 meters. Eh, MINOR-ish, intended tolerance).
  - adapter test: `assert(scene.starting_magic.health()==(30 if heal else 9))` good; `assert(packet==before ...)` ensures input immutability. Note `packet` was passed to resume_checkpoint which duplicates — but also `Areas.prepare_area` duplicates again. OK.

  Another check: `resume_checkpoint` passes `read.state` from `Starts.read` — but `Starts.read` for map uses read_legacy which returns state — not validated at read time? read_save likely validates. Then identity check, pin recheck, then resume_checkpoint validates again. Solid.

  One more: `map_case.gd` `areas()` returns PROGRESSION_AREAS (10). The rendered test overrides with 3 areas. But the headless test then does `for area in areas():` — 10 gates created sequentially; each `new_gate()` adds a new gate while old `current_scene` freed... scene.free() at the end. The gate from the previous iteration — is it freed? After scene loads, `scene.free(); current_scene=null`. The gate was replaced as current_scene by change_scene_to_packed, which frees the old scene automatically. OK.

  Now the F5-overwrite-slot-1 issue — actually wait, let me reconsider severity. In the normal (non-playtest) game: user plays, F5 saves to slot last_slot (default 1 for a new game too! game_session.gd:9 default 1). So a brand-new game's first F5 also writes slot 1. That's the established design: slot 1 is the default quicksave slot. So F5→slot 1 after F2 start matches new-game behavior exactly. Not a finding — consistent design. I'll drop it or mention as informational. I'll mention it briefly as MINOR/observation since docs claim "Manual slots remain" — true for the start itself; F5 is an explicit user action with feedback "Saved to slot 01." I'll note it as MINOR given the brief explicitly asked.

  Also the docs/help text change: old help said "Your own saves are not changed until you save (F5)" — new help says "Manual slots are kept; normal autosaves apply." The new text drops the warning that F5 writes — but adds autosave disclosure. The autosave disclosure is important: arriving at some maps may trigger an arrival autosave that overwrites the autosave slot without any user action. Handoff: "ordinary eligible autosaves still apply, which the F2 help now says explicitly." So an F2 start CAN cause a write to the autosave slot (user's autosave). That's disclosed in help text and handoff, and matches ordinary map-entry behavior. Acceptable per design — not a finding, or informational MINOR. The brief says "a start that can write over a user's own save or slot" — the autosave slot can be overwritten by an arrival autosave triggered by the start, without F5. Disclosed in the UI help. I'll note as MINOR (disclosed behavior).

  Anything breaking F2 menu with many entries: follow_focus added; ScrollContainer present. 21 rows fine.

  One more code-level check: `original_game_gate.gd` map branch — `_verify_save_access()` error swallowed silently (return without report) — same as _verify_and_start which also returns silently? `_verify_and_start` line: `if not _verify_save_access().is_empty(): return` — yes same pattern; _verify_save_access sets status.text itself. OK.

  Duplicate PROGRESSION_AREAS in python tool vs game_areas.gd — MINOR maintenance note. Also python's act mapping duplicates gd's.

  Docs regression: dropped `--playtest-starts` / `--playtest-start=ID` documentation while flags still exist (gate lines 157-161). MINOR.

  Also check the deviation doc and docs mention "Registry1157" etc — fine.

  One more: `tools/prepare_playtest_starts.py` describe override maps darker format to 'map' — meaning `--describe` on the Act1 darker save now reports resume 'map'/L8_SJ instead of 'darker'. Intended for C-15 but changes tool behavior for existing Act1 kind discovery. MINOR.

  Also, in map_case.gd: `assert(entry.full_health)` — fine.

  Let me also verify PATCH_CHECK claim quickly? Not necessary for the commit content itself. And confirm the commit only contains these files (no stray). diff --stat showed 19 files, all relevant.

  Check git log to confirm fde4d19 parent is 5ac1bca.

  Also one potential issue: `playtest_starts.json` act2-l9 uses `"area": "Dracoid Ruins"` and title "Dracoid Ruins, pit arrival"; areas fine.

  Severity assignment summary:
  - No BLOCKER found. SHAs all verify, identities match, provenance spot-checks pass, full-health is detached-copy only, ordinary loads keep health, Act1 paths untouched, pins checked before and after read.
  - MAJOR? The F5→slot-1 / autosave-on-arrival: autosave overwrite is disclosed; F5 default-slot behavior pre-exists for new games and legacy loads. I don't think MAJOR. 
  - Actually, wait — one more check: `_queue_scene` with legacy=false sets meta "lol2_slot_resume" — check what that meta does elsewhere; e.g., arrival autosave eligibility might treat it as a slot load and autosave. map_case asserts `not has_meta("lol2_slot_resume")` after load. So meta consumed during apply. Fine.

  Let me double-check one thing in the gate: after map resume starts, `starts_panel` — gate scene replaced; fine.

  Also potential: `resume_checkpoint` doesn't check `read_legacy`'s error — gate does; adapter test calls directly with parsed dict (no error wrapper). If someone else calls resume_checkpoint with an invalid state, validate_area catches. Fine.

  MINOR findings list:
  1. scripts/lol2/playtest_starts.json (new entries): absolute ~ paths with username committed (source.path/proof/input_save fields) — pre-existing convention from Act1 entries, but the brief flags it; also docs/playtest-starts.md guarded_godot.py absolute path. MINOR.
  2. docs/playtest-starts.md: dropped documentation of `--playtest-starts` / `--playtest-start=ID` CLI flags which still exist in original_game_gate.gd:157-161. MINOR.
  3. game_save.gd resume_checkpoint last_slot=1 → F5 after a checkpoint start targets slot 1 silently (same as new-game/legacy-load default, pre-existing semantics); and arrival autosaves may overwrite the autosave slot (disclosed in F2 help). MINOR.
  4. tools/prepare_playtest_starts.py:36-38 + game_areas.gd:3: PROGRESSION_AREAS and the act-3 area list duplicated between the Python tool and playtest_starts.gd; can drift. MINOR.
  5. tools/prepare_playtest_starts.py describe(): `lol2-restoration-darker-jungle` now reported as map/L8_SJ, no longer offering the 'darker' kind for Act1 darker saves. MINOR.
  6. Registry: new map tests don't declare needs.env LOL2_ORIGINAL_GAME_EXE though map_case.gd requires it; would fail loudly rather than silently pass if the driver didn't set it. MINOR.
  7. Help text "older checkpoints can reset native puzzles on other maps" — ambiguous/wrong: it's the new Act2/3 legacy-format files that lack the native bank. MINOR wording.

  Anything MAJOR? Let me reconsider the health check: validate requires health within 1..30 and int. resume_checkpoint sets to MAXIMUM after validate. OK.

  What about `entry.get("full_health") != true` — in GDScript, JSON true parses as bool true. OK.

  What about map_case asserting all PROGRESSION_AREAS covered — ties the game catalog to the manifest; adding a new progression area later breaks this test — intended gatekeeping.

  Also check `_build_playtest_starts` rows for entries with resume map whose staged file missing → disabled "(not in this build)" ✓.

  Verdict: APPROVE (with minors). The brief's adversarial checklist found no blocker: SHAs verified independently, provenance matches, no overwrite of user saves by the start itself, full-health scoped correctly, Act1 unchanged, tests can fail.

  Wait — one more thing to check: "a start that can write over a user's own save or slot" — check `_queue_scene` non-legacy path: pending_resume → scene apply → does the map scene on apply write an autosave? The handoff says eligible autosaves apply (arrival/timer). That's gameplay-automatic, disclosed. OK.

  Also confirm commit parent:

• One final check — commit parentage and that no unexpected files slipped in:fde4d19 Add pinned Act 2 and Act 3 checkpoint starts to F2
5ac1bca Fix whole-game load rollback and staged-asset refusals
742dcab grok G4: walk the cemetery fixtures west of the OF9 wall
docs/deviations/0620-row-2026-11-11-act23-playtest-starts.md
docs/playtest-starts.md
scripts/lol2/game_save.gd
scripts/lol2/original_game_gate.gd
scripts/lol2/playtest_starts.gd
scripts/lol2/playtest_starts.json
tests/playtest/map_case.gd
tests/playtest_checkpoint_adapter_test.gd
tests/playtest_map_starts_rendered_test.gd
tests/playtest_map_starts_test.gd
tests/playtest_starts_test.gd
tests/registry/playtest_checkpoint_adapter_test.json
tests/registry/playtest_map_starts_rendered_test.json
tests/registry/playtest_map_starts_test.json
tests/registry/playtest_starts_test.json
tools/prepare_playtest_starts.py
tools/regression_source.py
tools/test_prepare_playtest_starts.py
tools/validate_playtest_starts.gd
?? assets/lol2/dark_halls/
?? assets/lol2/doors/indices_478.png


• Clean. Untracked files are the pre-existing generated media mentioned in the handoff.

  Now write the review. Findings:

  • MINOR — scripts/lol2/playtest_starts.json (all ten new entries, e.g. line with act2-l9 source.path ~line 470+): absolute ~/... paths with username committed. Pre-existing convention (parent manifest already had 21 such paths), so MINOR.

  • MINOR — docs/playtest-starts.md: staging command embeds ~/AI_COMMS/sol_lane/task3_20261109/guarded_godot.py — same privacy class.

  • MINOR — docs/playtest-starts.md: rewrite dropped documentation of --playtest-starts / --playtest-start=ID CLI flags, still implemented at original_game_gate.gd:157-161.

  • MINOR — game_save.gd:212 resume_checkpoint hardcodes session last_slot=1, so F5 after a checkpoint start quicksaves into slot 1 without prompting (quicksave → session.last_slot, game_save.gd:264). Same default as a new game and as the pre-existing load_legacy (game_save.gd:200), so inherited semantics, not a regression; the F2 help's "Manual slots are kept" is true of the start itself but not of the follow-up F5.

  • MINOR — tools/prepare_playtest_starts.py:37 + scripts/lol2/game_areas.gd:3 + playtest_starts.gd entry_error: the progression-area whitelist and act-3 area set are duplicated in two languages; drift would make the Python stager and the GDScript validator disagree.

  • MINOR — tools/prepare_playtest_starts.py describe(): 'lol2-restoration-darker-jungle' is now always reported as map/L8_SJ, so --describe can no longer scaffold a 'darker' (Act1) entry.

  • MINOR — tests/registry/playtest_map_starts_test.json / _rendered_/adapter: new registries don't declare needs.env LOL2_ORIGINAL_GAME_EXE though tests/playtest/map_case.gd:24 requires it (the pre-existing playtest_starts_test.json does declare it); failure mode is loud, not silent.

  • MINOR — original_game_gate.gd:210 help text: "older checkpoints can reset native puzzles on other maps" — the native-bank reset actually applies to the new Act2/3 legacy-format packets (native_bank:{} at game_save.gd:212); wording is ambiguous about which rows.

  Positives verified (briefly): all 21 staged files match pins; all 10 new SHAs match claimed sources (tar members, r18 tmp files, r12z packet) and proof report SHAs match; identities match file contents; input_sha256 for L8 matches; SHA checked before and after read in the gate; validate before heal; heal on detached copy only; ordinary slot loads unchanged; Act1 KINDS/branch unchanged; follow_focus scroll fix; tests have real failure modes.

  Verdict: APPROVE.

• ## Review of fde4d19 (C-15: ten Act2/3 F2 playtest starts)

  **What I verified independently (not just from the handoff):**

  - **SHA pins** — all 21 staged files in `assets/lol2/generated/playtest_starts/` match their manifest pins byte-for-byte. All ten new pins also match their claimed upstream sources: the five Astra tar members (`l9/l10/l12/l13/l14` extracted from `earned_saves_and_drafts.tar.gz`), the four `lol2_r18/tmp` files (L16/L17/L19/L20), and the r12z departure packet for L8. Proof-report SHAs (`f755…`, `9c22…`, `f835…`) and the archive manifest SHA (`976d…`) also match.
  - **Identities** — every `contains`/`excludes`/`values` identity in the ten new entries matches the actual save contents (including `format` and `player.position`); original healths are 19–30, so the full-health adapter is real work, not a no-op masquerading.
  - **SHA-check placement** — `original_game_gate.gd:252` checks the pin before reading, `:265` rechecks after reading, before any mutation; `resume_checkpoint` validates format/health via `Areas.validate_area` *before* healing (bad packets are refused, and the adapter test proves it).
  - **No user-save overwrite by the start itself** — the checkpoint path only queues a scene; `map_case.gd` asserts the `user://saves` directory hash set is unchanged. Pinned files are git-ignored generated copies, healed only on a `duplicate(true)` packet.
  - **No health leak into normal loads** — `resume_checkpoint` is only called from the gate's map branch; ordinary slot loads keep saved health (adapter test asserts 9 stays 9).
  - **Act 1 unchanged** — KINDS, the five fixed resume branches, and all eleven Act 1 manifest entries are untouched; the only shared edits are help text, `follow_focus`, and the appended entries.
  - **Tests can fail** — the map case drives real F2/Enter GUI dispatch, asserts scene identity, health==30, pack/equipment, horizontal position, pin immutability, and save-dir preservation; the adapter test has genuine refusal cases.
  - **F2 menu** — `follow_focus = true` on the ScrollContainer addresses the 21-row focus/scroll issue; rendered test asserts the focused row is on-screen.
  - **Provenance/aids** — disclosed aids are recorded per entry (`test_aids`, scope disclaimers); L20's index52/birth-clock aid is explicitly recorded. L8 reuses the already-approved r12z packet, so no new aid.

  **Findings:**

  • `scripts/lol2/playtest_starts.json` (all ten new entries' `source.path`/`proof`/`input_save` fields) — MINOR: absolute `~/...` paths with the owner's username committed. The parent manifest already did this for all 11 Act1 entries (21 occurrences), so it is established convention, but it remains a path/privacy leak in a committed file.
  • `docs/playtest-starts.md` (staging command block) — MINOR: embeds the absolute path `~/AI_COMMS/sol_lane/task3_20261109/guarded_godot.py`; same privacy class, and the command is useless verbatim to anyone else.
  • `docs/playtest-starts.md` — MINOR: the rewrite dropped all mention of the `--playtest-starts` and `--playtest-start=ID` CLI flags, which still exist and function (`scripts/lol2/original_game_gate.gd:157-161`). Docs now under-describe shipped behavior.
  • `scripts/lol2/game_save.gd:212` — MINOR: the checkpoint doc hardcodes `last_slot: 1`, so pressing F5 after a checkpoint start quicksaves into slot 1 without prompting (`game_save.gd:264`). This is inherited semantics — identical to the pre-existing `load_legacy` (`game_save.gd:200`) and the new-game default (`game_session.gd:9`) — not a regression, but the F2 help's "Manual slots are kept" is only true of the start itself, not of the follow-up F5. Arrival autosaves can also overwrite the autosave slot; that one *is* disclosed in the new help text.
  • `tools/prepare_playtest_starts.py:37-40` vs `scripts/lol2/game_areas.gd:3` and `scripts/lol2/playtest_starts.gd:51-54` — MINOR: the progression-area whitelist and the Act-3 area set are duplicated in Python and GDScript. Currently consistent (verified), but drift would let the stager accept what the game refuses, or vice versa.
  • `tools/prepare_playtest_starts.py:91-94` — MINOR: `--describe` now reports every `lol2-restoration-darker-jungle` save as `map`/L8_SJ, so the tool can no longer scaffold a `darker` (Act 1) entry; a quiet behavior change to an existing helper.
  • `tests/registry/playtest_map_starts_test.json`, `playtest_map_starts_rendered_test.json`, `playtest_checkpoint_adapter_test.json` — MINOR: none declare `needs.env: ["LOL2_ORIGINAL_GAME_EXE"]`, though `tests/playtest/map_case.gd:24` requires it (the pre-existing `playtest_starts_test.json` does declare it). Failure mode is loud rather than silent, but the registry entries are incomplete.
  • `scripts/lol2/original_game_gate.gd:210` — MINOR: help text says "*older* checkpoints can reset native puzzles on other maps", but the native-bank reset (`native_bank: {}` at `game_save.gd:212`) applies to the *new* Act2/3 legacy-format packets; the wording points at the wrong rows.

  No blocker or major issue found: pins are real and verified end-to-end, provenance matches the files, full health is scoped to a detached copy on whitelisted map entries only, user saves and Act 1 behavior are untouched, and the tests have genuine failure modes.

  VERDICT: APPROVE

To resume this session: kimi -r session_426e1253-e58c-4e5d-b966-ad312266be91
