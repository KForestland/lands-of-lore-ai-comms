• Review complete. I read the full diff `b3e384e..HEAD` (4 commits) plus the surrounding code of every touched script, the item catalog, the journal registry, and the new earned tests. Findings:

  ## Stated risk 1 — museum_inventory.gd (shared pack)

  - **can-drop/drop forwarding (line 191, 488-508):** checked, holds. The ItemList previously rejected every drop; `_can_combine` still rejects everything except the 117+119 pair, and only when the host has an `L8Larkhon` node (darker jungle). Equip drops go to the equipment slot Buttons' own forwarding (line 143), untouched; a leaf dropped on a non-recipe item is exercised by `tests/l8_hand_combine_earned_test.gd` and mixes nothing. Self-drops and same-kind pairs fail the `{117,119}` kind check. Dragging onto the grid cannot shadow slot drops (dispatch is per-control). Dropped as a concern.
  - **Reserved panel width (lines 240-244):** checked, holds. Gated on `is_instance_valid(mix_button)`; `mix_button` is created only when the parent has `L8Larkhon` (line 225), so museum/jungle/hive/cave/L9-L19 packs skip the block entirely — zero layout change elsewhere. `detail_text` is a `Label`, so `get_line_height()` is valid. Dropped.
  - **"Use" relabel (line 326):** checked, holds. It only replaces the old `"Play flute"` fallback for non-flute items — before this change, dragon's blood and any unlabeled `use_kind` genuinely rendered "Play flute". The flute itself still gets "Play flute", and no test or script depends on the old wrong label (grepped). Dropped.
  - **Recipe relabel/details (lines 179, 373-376):** checked against `act2_items_source.json` — definitions 117/119/128 map only to Silverleaf/Serum/Vapors rows (the one other 119 row, `act2:L8_SJ:item26`, *is* an Amaranth Serum). No other area's items are renamed. Dropped.

  ## Stated risk 2 — F2 full health

  Checked, holds. `start_full_health` is set only inside `start_playtest` from the entry (`original_game_gate.gd:260`) and cleared immediately after `_verify_and_start` returns (line 262), including the early-return paths. Only the `act1-end-darker-jungle` entry pins `full_health` (`playtest_starts.json:383`), and the mutation applies only in the `resume_darker` branch (`original_game_gate.gd:321`). `STARTS_KEY` is `KEY_F2`; the plain darker resume of the same file keeps the saved 19 — asserted by `tests/playtest_start_full_health_test.gd` (30 via F2, 19 via plain resume). Dropped as a concern.

  ## Stated risk 3 — drowned-R return and village-first guard

  - **liquid_drowning.gd:151-163:** teleport fires only when reviving while `drowning.dead`, within 80 of `died_at`, and still inside a water polygon; an F9 load standing elsewhere just resets the clock. `last_dry` is recorded only when alive, on the floor, and outside every water polygon — `polygon_at` (no vertical window) is deliberately used so a fall *above* the lake doesn't count as dry. Old saves unaffected (new fields are runtime-only). One contrived edge — quickload into a save made while swimming within 80 of the drown spot teleports to a stale-but-dry bank — is benign by design; checked and dropped. No stranding or drown loop found; `tests/l8_lake_bank_earned_test.gd` walks in on foot, drowns, R-revives, then waits a full clock on the bank.
  - **Village-first (l8_journey.gd):** the guard panel is always closable (Escape at line 159, back button), a dead-player E guard was added (line 166), and the guard spawn in `restore_world` is idempotent (`scripted_creature_state.spawn` returns false once present). The shaman-trade re-open path leaves `paused=true` with the panel re-shown by the button callback's `refresh()` (line 182) — verified there's no paused-with-no-UI window in the real input path. Old saves: admission still implies `temple_visited`, and the branch order in `refresh()` (line 202-209) maps every old `gift`/`admitted`/`temple_visited` combination onto the same UI as before; no state format change. `leave_arena` E-anywhere matches the hint that already displayed anywhere, and phase `complete` only exists inside the arena. Dropped as concerns.

  ## Findings

  1. **Trivial — `tests/act1_journal_hints_test.gd:45`:** the PASS string says "48 notes" while the assertion on line 36 (and both sibling journal tests) correctly use 49. Purely cosmetic; the check itself passes/fails correctly, so this does not block merge.

  Non-blocking note: the working tree has an untracked `assets/lol2/doors/indices_478.png` — outside the reviewed range and not part of the merge, mentioned only in case it was meant to be committed.

  APPROVE
