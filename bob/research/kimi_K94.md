• Review complete. I read the full diff `742dcab..5ac1bca`, re-traced the load/save/autosave flows, and checked the engine semantics the fix relies on against the Godot 4.6 source.

  ## K92 finding 1 — failed slot apply wedges save/load/autosave: FIXED

  - `game_save.gd:240` now calls `session.retain_previous(current, prior, metadata)` before `change_scene_to_packed`, keeping the outgoing scene off-tree instead of letting the engine destroy it.
  - `game_session.gd:143-147`: on `apply_slot_state` error, `rollback_load.call_deferred(error)` runs after the destination's `_ready` returns. `rollback_load` (`game_session.gd:109-133`) detaches and frees the failed destination, restores the full runtime checkpoint (so `pending_resume` and `changing_scene` return to their pre-load — empty/false — values), wipes all `RESUME_METAS` (including `lol2_slot_resume`) and restores the captured metadata, re-adds the previous scene as `current_scene`, restores camera and mouse mode, and surfaces "Load failed: …". All three locks from the K92 scenario are released, so subsequent F5/F9/panel loads, saves (`save_admission` sees no `lol2_slot_resume`), and the autosave scheduler are admitted again. The new `advance_play` early-return (`game_session.gd:186`) keeps the scheduler from observing the transitional state.
  - `apply_when_ready` (`game_session.gd:158`) now rolls back a destination that never becomes ready, closing the second wedge path.
  - I verified the two engine behaviors this depends on for 4.6: `Node.queue_free()` falls back to `SceneTree::get_singleton()` for off-tree nodes ([node.cpp:3472](https://raw.githubusercontent.com/godotengine/godot/4.6-stable/scene/main/node.cpp)), so the retained scene really is freed on commit and the failed scene on rollback; and `change_scene_to_node` skips the outgoing scene when `current_scene` is null ([scene_tree.cpp:1712-1717](https://raw.githubusercontent.com/godotengine/godot/4.6-stable/scene/main/scene_tree.cpp)), so no double-free. All load destinations reach `apply_pending`/`apply_when_ready`, and `apply_slot_state` resolves everywhere via inheritance (`act2_map`/`dark_halls`/`darker_jungle`/`dragon_level`/`act2_jungle_return` extend `jungle_walkthrough`, whose `apply_slot_state` wraps `apply_save`; `hive_review` defines its own) — no missing-method crash. `game_save_apply_failure_test.gd` exercises the exact K92 scenario (Cave packet with roach, combat disabled) including save/autosave/retry after the failed apply.

  ## K92 finding 2 — slot saves refused when natives aren't staged: FIXED (as the sanctioned deliberate-limitation branch)

  `game_save.gd:64` now refuses with an area-specific message ("Native script state for Dracoid Ruins is missing. Saves in this area require its native scripts to be staged."), the deviation row discloses the no-partial-fallback policy, and `game_save_missing_native_test.gd` covers manual feedback, autosave surfacing, slot preservation, and legacy readability. K92 explicitly allowed this resolution.

  ## K92 finding 3 — Old save load skipping per-area asset guards: FIXED

  `Areas.assets_error` (`game_areas.gd:180-194`) mirrors the gate's checks exactly (`museum/jungle/hive assets_ready()`, `dark_halls/darker/dragon arrival_assets_ready()`, `act2_map.map_assets_ready(area)` — all verified to exist, matching `original_game_gate.gd:286-347`), and `_queue_scene` (`game_save.gd:215-216`) invokes it before any session/meta/scene mutation, so slot loads and the panel's Old-save path share the guard. `game_save_legacy_assets_test.gd` drives the real Old save button with dispatched Enter input.

  ## Nothing else changed

  The remaining diff items are all in-scope: the two off-tree guards (`indexed_cave_wall_review.gd:82`, `museum_interface.gd:173`) needed because the retained scene is off-tree, the `_feedback` Label fallback, `_exit_tree` cleanup of `_load_previous`, the doc wording, and the three test/registry files. Residual non-issue, dropped: if a destination scene were externally freed mid-load, `apply_when_ready` returns without rollback — identical to pre-change behavior, and no in-tree path does that (loads are gated).

  APPROVE
