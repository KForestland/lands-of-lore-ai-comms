• Review complete. I read the full diff `4cfd4f8..742dcab` (all game-code files, the new save/session/areas/panel modules, host integrations, and the changed/new tests), checked it against Plan 3 rev 2 and K85 items 9–11, and traced the load/save/autosave flows end-to-end. Findings:

  ## Defects

  **1. A failed slot apply permanently wedges all saving, loading and autosaving for the process — Moderate.**
  `scripts/lol2/game_session.gd:92-95` (`apply_pending`): when `host.apply_slot_state()` returns an error, the function returns without clearing `pending_resume`, without resetting `changing_scene`, and without removing the `lol2_slot_resume` tree meta (the meta is only removed on success at :97, `changing_scene` only cleared at :96). All three are left set by `_queue_scene` (`scripts/lol2/game_save.gd:229-235`). From then on:
  - every later load is refused: `_queue_scene` at `game_save.gd:206` — `session.changing_scene or not session.pending_resume.is_empty()` → "Wait until the area finishes loading.";
  - every later save is refused: `save_admission.gd:20-21` has `lol2_slot_resume` in `TRANSFERS` → `can_save()` returns "Wait until the area change finishes.";
  - autosave never fires again: `game_session.gd:124` (`changing_scene or not pending_resume.is_empty()`).

  Concrete failing scenario: save a slot in the Cave with the roach fought (or a chain door broken), then load that slot in a run where cave combat / the bridge route is disabled. Validation passes (`read_document` → `Areas.validate_area`), the scene swaps, then `_apply_save_state` returns "This save needs cave combat enabled." (`cave_walkthrough.gd:1298-1300`). The player gets one "Load failed" message and thereafter every F5/F9/panel/autosave attempt says "Wait until the area finishes loading." until the process is restarted — with no in-process recovery (`reset_legacy()` is only reachable from the opening gate). The legacy path this replaces (`_quickload_unrecorded`) failed the same way but left the game fully saveable. Any post-validation apply error (e.g. `area_owners.restore_all("load")` in `act2_map.gd:317`) wedges the same way. The error path should roll back `pending_resume`, `changing_scene` and the `lol2_slot_resume` meta, mirroring the rollback `_queue_scene` already does for its own failures.

  **2. Slot saves refused in progression areas when native scripts aren't staged — Minor.**
  `scripts/lol2/game_save.gd:64` requires `native_bank` to contain the current area for all `PROGRESSION_AREAS`, but `game_session.gd:40-47` (`snapshot_bank`) can only add that row when `host.progression` is bound, and `act2_map.gd:194-198` / `darker_jungle.gd:237-242` / `dragon_level.gd` only bind progression `if Binder.assets_ready(area_id)`. In a partially staged build (map pack present, native script bundle absent — the configuration `--map-preview=` and `_change_level`'s "not staged in this build" message already acknowledge), the legacy quicksave still writes fine, but F5 now fails with "Missing native state for the saved area." — the player cannot save at all in that level. Either tolerate a missing row (save without native state, as legacy loads already do) or surface it as a deliberate limitation.

  **3. The panel's "Old save" load skips the per-area asset guards the gate had — Minor.**
  `save_slots_panel.gd:101-104` → `game_save.gd:196-201` (`load_legacy`) → `_queue_scene`, which only checks `ResourceLoader.exists(doc.scene)` (`game_save.gd:216`). The pre-existing gate resume path additionally checks `assets_ready()` per area and shows an error instead of starting (`original_game_gate.gd:286,296,306,347`). Loading an old save whose area assets aren't staged in this build now loads a half-initialized scene instead of the old clean refusal.

  ## Checked and dropped (holds)

  - **K85-9 (Cave v1/v2)**: slot envelope keeps the inner Cave version opaque; `walkthrough_save.migrate_loaded` is applied on the slot path (`game_areas.gd:176-178`, `cave_walkthrough.gd:1296`) and legacy v1 migration is covered by `legacy_save_fixture_test.gd:35-39`. Holds.
  - **K85-10 (route handoff metas)**: both route handoffs are in `RESUME_METAS`/`TRANSFERS`, cleared on slot load and blocking saves while alive. Holds.
  - **K85-11 (Cave resume)**: `apply_slot_state` + `_apply_save_state` split exists, gated on `walkthrough_ready` via `apply_when_ready`; Museum's void `apply_save` wrapped correctly (`museum_walkthrough.gd:1195-1199`). Holds.
  - **Autosave gating**: refused while paused, dead, flying, in movies/conversations (via `can_save` + `world_active`), mid level-change (transition metas + `transition_pending` + `pending_resume`), and off-floor/in liquid; arrival fires only after ready + one physics frame; mid-fight saves are plan-sanctioned (C3's refusal list matches the old quicksave's). Holds.
  - **Corrupt slots**: damaged files surface as error rows, never crash the list, are overwritten cleanly, and `.bak` rotation/Continue-fallback work (`game_save_slots_test.gd:29-61`). Holds.
  - **Native bank round-trip**: string/int key canonicalization is symmetric, validated, and bank-over-`act2_struck` precedence is implemented (`act2_progression.gd:1292-1296`) with a dedicated test. Act1 levels (L1/L3/L4/L5/L7) are admitted by `NATIVE_AREAS` but no host produces rows for them — same as the pre-change meta bank, disclosed in plan 3.7; not a regression.
  - **Transfer metas across level change**: handoff metas are consumed before `can_save` passes and autosave can't fire while they're set; nothing captured mid-transfer.
  - The `scripted_creature_state.gd` attack-variant widening and the `act2_map.gd` body-fit change in this range are consistent with their tests.

  CHANGES NEEDED
