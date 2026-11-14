# R123 — G-04 saves 5b95974 on the load-rule tree

Review only. Local worktree `~/opus_work/lol2_grok_r123`, branch `grok/r123-20261114`, HEAD `f7acd0fa77c4`. Parents `5b95974` (G-04) and `6d31407` (r19-work, which contains load rule `95f1083`). This commit is not on r19-work. Sol's tree was not edited. Diagnostic prints were added only on this review tree, in the spire, gate, and cell tests, so a refused F5 records `can_save`, the floor flag, and the HUD. They do not change the save.

## Hold

Do not land this on r19-work. F5 is refused while G-04's autosave thread is still writing. The HUD is `Save failed: An autosave is finishing. Try again shortly.` `game_save.gd` `quicksave` returns that string when `game_session.gd` `save_in_progress()` is true, before it writes the slot. The player can be on the floor with an empty `can_save()`. The slot file stays the previous save.

## What passed

Load-rule census, headless, exit 0. `1302 regions with an entry, 853 re-armed groups, 130 REARM commands still written, 574 skipped because the save holds the target.` `PASS load region rule: every entry-group opcode in 15 levels is on one list; L19 1943 re-arms without its lever press.`

Rendered, private display, real E / F5 / F9:

- Temple floor 83. `PASS G04 actual E/F5/F9 L14 native floor physical checkpoint; held stand aid, no event re-fire.` This is the double-restore check. The saved floor was not applied a second time.
- Ruins door 115. `PASS G04 realE/F5/F9 exact mid-motion native door and physical collision.`
- Crypt lid 86. `PASS B local rendered realE moves crypt top86.`
- Cemetery cover 241 and chest 107. `PASS` including `F5/F9 life/frame persist.`
- City fountain 626. `PASS G15 Mists3 actual CtrlQ source626/frozen visual/cost3, Mists1 negative/repeat/F5F9.`
- r19l owner slot. `PASS r19l owner slot loads L16_CA at (-4111.0, 107.0, 15386.0) resets 0.` The slot file was copied into the test home before launch. `load_slot` reads slot 1.
- Expel cell 52, second run only. Own area, transfer to L14, F5/F9, and the return to L20 all returned. First run stopped at `Actual F5 writes a new whole-game slot: g15_expel_other_level`.

## What failed

Same HUD on the rerun, display `:247`, fresh `XDG_DATA_HOME`:

- Citadel spire 170. The light check had already passed on the first run (the script reached the F5 read). Rerun: on the floor at `(-3344, 32, 6564)`, `can_save` empty, HUD the autosave refusal. The slot left on disk was the previous test's `L14_HT`, so the lit spire was not recorded. Exit 1.
- Cemetery gate halves. In-memory `make_document` admitted (`can`, `validate`, and the world error were all empty, floors clock 0). F5 then hit the same HUD. The slot's quests had no `generic_objects`, so halves 70-73 were not shown part-open or open after a real save. Exit 1.
- Placed Temple flute. The fresh worktree had no `res://tmp/l14_flute_approach_qualified_save.json`. The G-04 file matches pin `d691b1ffa7f4de91c7fdc2cafa72771414573f9f179ac1d8f20c0850ed2fb22e` and was copied in. The place round got through real E and the first F5/F9. The retrieve round's F5 did not change the slot hash: `Actual F5 writes a new whole-game slot: g04_flute_retrieved`. That log does not print the HUD. The next two tests on the same home printed the autosave refusal.

## Not claimed

No second restore of a saved door pose was observed. Opcode 1 stays off the re-arm list. The floor test is the real-input proof that a held floor target is not played again. The hold is the F5 race, not the load rule.
