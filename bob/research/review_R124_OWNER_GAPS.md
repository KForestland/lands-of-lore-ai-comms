# R124 — owner gaps d32721e

Review only. Worktree `~/opus_work/lol2_grok_r124`, branch `grok/r124-20261114`, HEAD `d32721e0d108`. That is Sol's READY head. His tree was not edited. Generated assets and native scripts are symlinks to his tree. The three owner files are the pinned bytes in `tests/fixtures/owner_gaps_inputs`.

Two prints were added on this worktree only: the slot read just before F9, and the HUD just after F9. They do not change the load.

## Hold

Do not land this. All three boots refused F9, so the lever, the shaft water, and the aloe were not used.

The owner's file reads. The HUD is `Load failed: An autosave is finishing. Try again shortly.`

| Check | Slot read | F9 |
|---|---|---|
| L12 tiger, pin f070a936 | area L12_CM, error empty | refused, scene unchanged |
| L8 shaft, pin 6d292fd0 | area L8_SJ, error empty | refused, scene unchanged |
| L14 aloe, pin 8e9d46d9 | area L14_HT, error empty | refused, scene unchanged |

`game_save.gd` `_queue_scene` returns that sentence when `save_in_progress()` is true. The fresh area's arrival autosave was still writing. `can_save` is not the gate here. The same sentence is what refused F5 on the R123 spire and the Cemetery gate.

The three gaps themselves were not observed.
