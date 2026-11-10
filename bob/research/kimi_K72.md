• Review complete. I read the full patch (1125 lines) and traced every stated risk through the base tree at b3e384e. Findings below.

  ## Stated risk 1 — first-arrival sampling (`atlas_explored.gd:155` → `note.call_deferred()`)

  Verified the placement order for every affected host; the deferral is correct and writes no quest state:

  - `act2_map.gd:163` attaches the tracker inside `super._ready()`, and the native arrival override lands at `act2_map.gd:165-168` — synchronously later in the same `_ready`, before the deferred flush. Same shape in `dragon_level.gd:53` (attach) vs `dragon_level.gd:121` (placement). The old inline call genuinely sampled the temporary pack spawn; the deferred call cannot.
  - Hive: `hive_review.gd:115` registers `attach_hive_route.call_deferred()`, and the Jungle→Hive handoff (position + exploration packet) is applied in the route node's own `_ready` (`hive_route.gd:15-33`). The tracker's `note.call_deferred()` is registered later in `hive_review._ready`, and Godot's deferred queue is FIFO — so the sample runs after handoff placement.
  - `note()` itself (`atlas_explored.gd:172-203`) only writes the host's `atlas_explored` presentation var; its one quest touch is erasing the legacy transport key from `quest_state`, which is the intended self-healing migration. Checked and held — no defect.

  ## Stated risk 2 — Cave/Museum/Hive tracker vs saves

  - All three hosts already had `atlas_explored` as a top-level save field (`cave_walkthrough.gd:1228/1293`, `museum_walkthrough.gd:902/920`, `hive_review.gd:428/442`); the patch only populates it. Save format unchanged, no writer puts the key inside `quests` (jungle quicksave releases it at `jungle_walkthrough.gd:473-475`, hive at `hive_review.gd:426-427`).
  - Old-save migration: `taken()` → `migrate()` marks the host area full only when the key is absent (`atlas_explored.gd:86-112`); fresh arrivals get `initial()` before attach in all three patched `_ready`s, so migration can't fire on a new game. Reload replaces the var wholesale from the save, so no exploration loss; the tracker then only re-adds regions actually visible from the restored position.
  - `_plot_state` (new, `museum_atlas.gd`) reads live owner packets without writes: `key_locks.state`/`museum_torches.state` and `hive elevator.checkpoint` all exist (`museum_key_locks.gd:16`, `museum_torches.gd:29`, `hive_elevator.gd:5`), the PLOT `done` paths match the real state shapes (`loaded` array, `pilot_state` 0/1, `played_flute` bool, `exit_region` -1 enum, `switches` array, etc.), and `step_done` is read-only — the new `atlas_remaining_places_test.gd` explicitly asserts the packet is byte-identical after reading.

  ## Stated risk 3 — Jungle/Hive transport key

  - Senders write it only into duplicated quest dicts (`jungle_walkthrough.gd` patch, `hive_review.gd:288` area) — runtime `quest_state`/`carried_quest_checkpoint` are never polluted.
  - Receivers erase it: `jungle_walkthrough.gd:579-581`, `hive_review.gd:358-360`; both quicksave paths release it before disk write. All validators on the path (`act_one_quest_state.gd:48+`, `act2_save.gd:7-18`, `jungle_save.gd:42`) are per-key tolerant, so the key causes no rejection; `hive_conversation.gd:160-184` reads only its own keys. The packet travels only through tree meta (`hive_route.gd:78`, `act2_progression.gd:379/210`, `act_one_departure.gd:103`) — never to disk raw. Checked and held — no quest-state write, no save change.

  ## Stated risk 4 — lift audio at 96 kHz Dummy

  Not hiding a real defect. `lift_seek_check.gd` enforces three rate-independent deterministic gates — saved remainder restored exactly, exactly one `_sync_sound` during load, derived offset exact — and those passed at 44100 Hz. The failing term is only the 60 ms wall-clock window on device-observable playback position. The Dummy driver mixes in 4096-frame blocks: 92.9 ms at 44100 Hz (> the 60 ms window) vs 42.7 ms at 96000 Hz (< it), so a perfectly correct `play(offset)` (`cave_prop83_lift.gd:122-124`, a one-line deterministic seek) can read back outside the window purely from driver quantization. The standalone known-correct seek reproducing 12/32 violations at 44100 with no game code involved confirms environmental cause. Caveat worth keeping: the 60 ms assertion is only meaningful where the driver quantum < 60 ms — it's a test-environment limitation, documented in the handoff, not masked game logic.

  Related test relaxation (`hive_boulder_audio_live_test.gd`): sound — `Audio.active` (the deterministic physics-clock gate) is retained; the added `finished`-signal observer distinguishes natural mixer completion from an explicit `stop()` (which emits no signal in Godot 4), so a real tail cut still fails.

  ## Checked and dropped

  - Cave→Museum transition drops L1_DC exploration (`_completion_state()` carries no atlas packet): one-way transition, the Museum Atlas only slices L3_DH, the cave quicksave retains it, and pre-patch the cave had no exploration at all — no regression.
  - Deferred-sample ordering for receivers applying handoffs after the tracker: all sender paths now carry the key, so any pre-handoff sample is overwritten by `apply_area_handoff`. Dropped.
  - Recovery test (`act1_recovery_branch_test.gd`) `atlas_violations` would fail loudly (not silently pass) if a 40-frame walk legitimately collapsed regions→full; test-only, not triggered.
  - Zoom ceiling 512: only two clamp sites (`museum_atlas.gd:214,368`) and three test assertions updated; grep confirms no other 12.0-ceiling assumptions. Registry orders 1100–1109 don't collide (existing max 1033). Scenes for all nine wrappers exist.

  No real defects found in the patch.

  APPROVE
