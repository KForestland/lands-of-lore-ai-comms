• Review complete. I read the plan, all three commit diffs in full, every touched production file in context, the dependency code paths, the shared input-walk test, and Sol's evidence bundle (`HANDOFF.md`, `QUALIFICATION.json`, integration patch). No files edited, no Godot launched, no sub-agents.

  ## Real defect

  **1. Two registered journal tests still assert the pre-F6 global note count — suite regression. Medium.**
  `3ec87d8` adds 3 rows to the journal hint tables (l10 `l10_fence_tuck`, l9 `l9_rotten_rail` + `l9_flood_table`), raising `MyJournal.hints().size()` from 49 to 52. The commit updated `tests/my_journal_test.gd:28` (49→52) but missed:
  - `tests/act1_journal_hints_test.gd:36` — `check(MyJournal.hints().size() == 49, ...)`
  - `tests/act3_journal_hints_test.gd:51` — same assertion

  Both are registered (`tests/registry/act1_journal_hints_test.json`, `act3_journal_hints_test.json`), both passed at base `2f8bc88` (verified: count was 49 there), and both now fail: actual 52 ≠ expected 49. Sol's 31-test qualification gate did not include either file, and the fee8b8a integration patch (`BJ14_F1_F2_F6_on_fee8b8a.patch`) doesn't touch them either — after integration the count is 53, so they fail there too. Fix is mechanical (52 canonical / 53 integrated), but as shipped the branch turns two previously-green tests red.

  ## Stated risks — checked, dropped

  - **Prompts only when the action works (item/reach/form):** F1's prompt is literally `target()`, the same admission E uses (`act2_world_items.gd:95-109`); the shield explanation requires unreleased bracers, aim, and occlusion by nothing but `L9DeadBracers.barrier` — pickup admission unchanged (`:60-76`; `barrier` exists at `l9_dead_bracers.gd:4`). Slab hint is gated on human form + `world_active()` exactly like `offer()` refuses (`l10_emperor_entry.gd:69-84`), and "Retrieve the ankh" is backed by `Kit.retrieve` (`mechanism_transaction.gd:95`). PICKUP_LABELS keys match the catalog (globes = def 98, bracers = def 59). Dropped.
  - **Statue walk-in accident/double fire:** needs aim dot > 0.7 within 120 with a clear ray, contact inside the source box's courtyard face, a movement key pressed toward the statue, captured mouse, no HUD cursor, no input lock (`act2_progression.gd:515-530`). Group 19732's final command (opcode 198, raw `…0b 01`) writes local11=1, which the guard at `:517` checks every physics frame, covering even the deferred level-change window. The `current_region == 42` re-fire only runs when already in region 42. Dropped.
  - **Journal notes save and stay once:** `MyJournal.discover` is idempotent and ids live in the `item_effects` journal packet, a live reference that travels with saves/handoffs (`my_journal.gd:55-67`, `player_item_controller.gd:26-31`); the three new ids resolve through `SOURCES`. Dropped.
  - **HUD/Journal change:** `shown_page` is set only in `open_page`, the sole `sheet.show()` path; both changed conditions (`museum_interface.gd:581,611`) are equivalent to the old ones for Character/Atlas and stop the overwrite only on the Journal page. Character page refresh still works. Dropped.

  ## Also checked and dropped

  - Mode-3 rail bodies in `l9_noble_rails.nearby()`: child 0 is the full 250-unit rail bar (bounds −126..124), so the coverage is correct; null bodies were impossible (pre-existing `restore()` would already crash).
  - Help text claims: C crouch exists (`player_crouch.gd:13`), Ctrl tuck exists (`l10_fences.gd:33`).
  - Slab hint lacks the `cursor_active` check the other two new hints have — matches the pre-existing priest hint convention in the same map (`l10_priest.gd:59`); cosmetic only.
  - Full-pack (≥64) edge where "E — Retrieve the ankh" shows but retrieve refuses — refusal feedback is printed; trivial.
  - Missing `.gd.uid` for the new script — 358 uid files vs 648 scripts; path-based preloads; not a defect.
  - Test count arithmetic in `act2_journal_hints_test.gd` (18) and `my_journal_test.gd` (52) is correct for the canonical branch, and the integration patch's 19/53 resolution is consistent.

  CHANGES NEEDED
