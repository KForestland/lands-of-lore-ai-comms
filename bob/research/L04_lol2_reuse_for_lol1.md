# L04 What LoL2 can lend LoL1

No Godot was run. LoL2 paths are `~/opus_work/lol2_r15`. LoL1 is `~/lol1_godot` at `9987d7e`. Nothing below is a shared library today. A pattern can be copied. A LoL2 script cannot be dropped in.

## Reuse

| LoL2 piece | Lend the pattern | Do not copy the file |
| --- | --- | --- |
| Save | One carried packet that survives a level change, checked by a validator. LoL2 splits this across `museum_save.gd`, `jungle_save.gd`, `hive_save.gd`, `act2_save.gd`, and `save_value_rules.gd`. | Those files store free-space positions and LoL2 quest dictionaries. LoL1 has no save call. `game_state.gd` holds 100 flag bytes, 24 script words, money, lamp oil, and a visited-level mask in memory only. A LoL1 save has to add the block, facing, party, and the item block chains. |
| Inventory | Pickup, drop, and a full-pack refusal, with a test that plays the action. LoL2's bar is `player_item_controller.gd` and `museum_inventory.gd`. | LoL1 already has its own bar in `items.gd`: 285 types from ONETIME.INF, a hand cursor, and a scrolling strip. The LoL2 controller speaks definition ids and item effects the LoL1 table does not use. |
| Journal | The rule that a note is text, discovered once, and never changes the quest. `my_journal.gd` is that adapter. | LoL1 Classic has no such page. The walkthrough's atlas is an item from the king's library (LOL1-02). Putting LoL2 journal notes into LoL1 would be a new edition feature. |
| Atlas | Explored cells only, drawn from map data the player has walked. `museum_atlas.gd` does this for LoL2. | That script is the museum sheet. LoL1's atlas is the Magic Atlas item, and the port does not draw it yet. The LoL2 owner rule of no pause does not transfer. This pass did not read the LoL1 automap opcode. |
| Interface | A palette shader in front of a DOS frame, and tests that the frame matches a reference. | `classic_hud_source.json` is the LoL2 frame. LoL1 already loads `playfld.bin` in `walk.gd`. The portraits in `party.gd` are a different panel. |
| Regression runner | `tools/run_regressions.py` plus a registry row per test, headless first. | The LoL2 name list is LoL2 tests. LoL1's ten tests are still one-off `godot --script` commands. The runner can grow a LoL1 list later. It should not launch the LoL2 list against this tree. |
| F10 feedback | `playtest_feedback.gd`: a local panel, a screenshot, a note, `user://playtest_feedback`, no network. | The script reads `LOL2_FEEDBACK_DIR` and LoL2's mouse capture. LoL1 has no feedback node. The report folder can be the same shape when a LoL1 build exists. |
| Packaging | A launcher script and a version stamp, the way r15 ships `play_r15.sh`. | No LoL1 package script is in `lol1_godot`. The LoL2 `DATA` tree and the LoL1 CD `DATA` tree are different games. |

## What is different

Movement is a 32×32 block step, turn, and strafe (`level_data.gd`, `walk.gd`). LoL2 walks free in 3D. The view is the ScummVM block renderer in `view_renderer.gd`, not LoL2's meshes.

The party model holds up to four characters (`party.gd`). The starting heroes are Ak'shel, Michael, Kieran, and Conrad. `addCharacter` does not include the Lora and Paulson workaround, so those joins are not ported. The current game picks one hero. LoL2 is Luther alone.

Combat is real-time on that grid: monsters already walk on the original 6-tick timers (`README`, `monsters.gd`). Attacks, party damage, and death are the README's missing piece. LoL2 combat is not this timer and is not a source for the numbers.

Scripts stay the EMC interpreter (`emc.gd`) and, later, TIM. LoL2's native opcode host does not run LEVELn.INI. Spell rows and character templates already come from `static_tables.json`. They stay in this tree.
