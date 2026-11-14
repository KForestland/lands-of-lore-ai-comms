# R119 review: G-15 casts, aa73c8d..c437c8d

Branch `sol/g15-casts-20261114`, detached worktree `~/opus_work/lol2_grok_r119`, head `c437c8dbbc3310acdeb5a5f9ca677c200fbc3dc7`. Sol's branch was left where it is. No merge.

Verdict: MERGE.

## Scope

Seven commits: Dampen `754d94f`, Curse 2 `6495d02`, Curse 3 `7ee2938`, Expel `6724724`, migration `ace0019`, Mists 1 `2ec3456`, Mists 3 `c437c8d`.

Production scripts in the range are the six casts, the teaching hooks that learn them, the single teaching table, and the removal of the three stand-ins. `player_curse.gd` receives Curse 1, Curse 2, and Curse 3. `l19_dawn_curse.gd` receives Curse 5 on L20 only. `l19_ghostly_heads.gd` receives Mists 1. `l16_fountain_freeze.gd` receives Mists 3 and `L16_CA.gd` registers it. `l12_crevasse.gd` loses the E form shortcut. `monastery_rooms.gd` learns Dampen from the charm grant. `l8_dawn.gd` and definition 76 in `act2_world_items.gd` learn the Control group. `player_starting_magic.gd` starts a fresh book and migrates a legacy packet that has no book. `game_save.gd` `resume_checkpoint` calls `prepare_start` on a detached copy. `playtest_starts.gd` is a comment. Docs, tests, and registry rows accompany that set.

Spell receivers in `scripts/lol2` are those four hosts plus the dispatcher. Prism 5 and Summon 3 are names in the teaching table and in `CASTS`. This range adds no Prism receiver and no Summon receiver. R120 is those two casts.

## How the checks were run

Rendered Xvfb, Godot 4.7.2, audio Dummy, clock `time_scale` 1 and physics 60. The tests refuse a headless display and refuse any other clock. Keys are real `InputEventKey` taps. `stand_at` writes `global_position` and is a disclosed teleport. `learn_spell_group` is a disclosed lesson. The positive Expel uses a schema-valid Dawn packet (`clicks` 2, `curse_said` true, the curse line) after the pre-Dawn refusal. None of this is an earned walk from the cab.

Logs: `/tmp/r119_r3.log` for the teaching unit, Dampen, Curse 3, and Curse 2. That process stopped on the first Expel assertion and did not reach Mists, the legacy save, or the statue. `/tmp/r119_r4.log` reran the official Expel script and then Mists 1, Mists 3, the legacy teaching input, and the statue continuation. All five printed PASS, exit 0, with no Parse Error and no SCRIPT ERROR. The four earlier passes also have no Parse Error and no SCRIPT ERROR.

## a) Each cast, and the stand-in

Dampen holds. `g15_dampen_input_test.gd` prints `PASS G15 Curse1 actual keys cancel warning/cost1/save-reload; phase0/2 negatives, normal uncancelled morph`. Charge 1 during the warning spends 1 and returns phase 0. Phase 0 and phase 2 refuse. The statue continuation `g15_dampen_statue_input_test.gd` prints `PASS G15 Dampen actual Q/cost1 then real W original statue path: movie54 begins as human, resets0`. The body stays human and movie 54 begins.

Curse 2 holds. `g15_curse2_input_test.gd` prints `PASS G15 Curse2 real CtrlQ from natural lizard, fixed cost2, no form timer, phase1 refusal and F5/F9`. Ctrl+Q from the lizard sets form 0, spends 2, and stores duration 0. Phase 1 refuses it.

Curse 3 holds. `g15_curse3_input_test.gd` prints `PASS G15 Curse3 real CtrlQ persistent source lizard/cost2/F5F9, next CtrlQ Curse2/cost2`. Ctrl+Q from the human sets form 2, spends 2, and the form stays until the next Ctrl+Q spends 2 and returns the human. The crevasse 60-second timer is not this path.

Expel holds on the official rerun. `g15_expel_input_test.gd` prints `PASS G15 Expel actual E negative/ShiftQ cost5/native birth/E demons/F5F9`. Before Dawn's words, Shift+Q leaves `glob_entered` false and spends nothing, and the hint is `The mother shoots a fireball back. She does not die.` E at the mother leaves the flag false. Curse charge 1 and charge 3 leave it false. After the Dawn packet, Shift+Q sets `glob_entered`, spends 5, and the hint is `The curse enters the mother.` Birth leaves Luther alive with resets 0. A second Shift+Q spends nothing. A later E still runs the demons-fall beat. F5/F9 keeps both flags.

The first suite process stopped on that same pre-Dawn sentence and printed no hint, mana, or position. A same-tree probe of that first Shift+Q, body on the mother at flat distance 0, measured `glob_entered` false, mana still 20, and the fireball sentence on the HUD hint. The official script was then run again, unchanged, and passed through birth, the demons E, and F5/F9. The stop was not reproduced.

Mists 1 holds. `g15_mists1_input_test.gd` prints `PASS G15 Mists1 real E negative/Q1 four heads/cost1/wrongcharge/duplicates/fifth/F5F9`.

Mists 3 holds. `g15_mists3_input_test.gd` prints `PASS G15 Mists3 actual CtrlQ source626/frozen visual/cost3, Mists1 negative/repeat/F5F9`. The chip break stays unhosted, which is what the spec left unnamed.

Stand-ins are gone from the three files. `l12_crevasse.gd` no longer has `choose_form` or the E lines that changed form. `l19_ghostly_heads.gd` accepts `mists1` only, and the input test's E leaves `shot` unchanged. `l19_dawn_curse.gd` keeps E as the demons-fall beat after `glob_entered`. The spoken curse line remains Dawn's line. The mother hint now names Shift+Q.

## b) r19i Claw save

Holds. The pin `res://tmp/g15_inputs/r19i_claw_slot.json` matches sha256 `b3fe96a441904a72620ecd11f02f12654f777ddaded429f58bd3eca4a5738f6c` (430863 bytes, the r19i `slot_01.bak`). F9 loads it as L12_CM at (-1177, 32, -5857), health 30, resets 0. The migrated book is Curse 1, Curse 2, Curse 3, Curse 5, Prism 5, and Summon 3. Ctrl+Q spends 2 and sets form 2 with notice `Curse 3`. The same test's return Ctrl+Q spends 2 and restores form 0. F5/F9 keeps the migration, and the pin bytes stay the same. The pass line is `PASS real r19i Claw F9 migration + seven real F2 starts, actual CtrlQ both directions on F2/oldsave, F5F9`.

## c) F2 starts

Holds for the four named chapters, read from the live books after a real F2 key, not from the table alone.

Claw Mountains L12_CM, Citadel L13_RC, and Temple L14_HT each carry `curse1`, `curse2`, `curse3`, `curse5`, `prism5`, `summon3`. City L16_CA carries those six plus `mists1` and `mists3`. The same City set is what F2 wrote for L17_HC, L19_BC, and L20_BB. On Claw, real W leaves the sloped arrival onto flat tread 1269, then Ctrl+Q spends 2 each way, human to lizard and back, with no extra teaching aid.

Prism 5 and Summon 3 are in those books because the migration table marks their chapters already past. Their receivers are not in this head.

## d) Fresh book

Holds on the new-game packet. `SpellBook.initial()` is an empty `learned` list. `fresh_magic()` stores that book on the fallback, and `magic_state()` returns the fallback when the quest packet has no magic state. `_process` migrates only a packet that has no book, so the fresh book stays empty on a late map. `g15_spell_teaching_test.gd` asserts the empty fallback, asserts migrate of that book on L20_BB adds nothing, and asserts an explicit modern empty book is left empty even with a Dawn receipt and even on L20. It prints `PASS G15 single-table legacy lessons, old input unchanged, fresh/modern no grants, receipts/spent, all seven F2 chapter capability contracts`. Lessons still arrive from the charm grant, the Control Token, a past-chapter legacy packet, or `prepare_start` on an F2 copy. This check is that unit plus the fallback code. A title-screen New Game click was not part of the run.

## e) Nothing outside the six casts

Holds. The new `accepts_player_spell` hosts are player curse, the mother, the four heads, and the fountain. Costs in `CASTS` for this stack are Curse 1 = 1, Curse 2 = 2, Curse 3 = 2, Curse 5 = 5, Mists 1 = 1, Mists 3 = 3. The table also names `prism5` at 5 and `summon3` at 3, which is the migration row the lead included, and no script receives them here.

## f) Four heads, Mists 1 only

Holds. `HEADS` is 67, 69, 68, 70. At each stand, E leaves `shot` unchanged, Ctrl+Q (Mists 3) leaves `shot` unchanged and spends nothing, and Q (Mists 1) appends that head and spends 1. A second Q on the same head spends nothing. After the fourth, `dragged` is true. Skull 66 stays out of `shot` and the cast there spends nothing. F5/F9 reloads `dragged` and the four ids. That is the leg the saved flag completes.

## g) Fountain prop 626

Holds. The host asserts record 626 in region 4900. Mists 1 at the aimed fountain leaves `frozen` false and spends nothing. Ctrl+Q spends 3, sets `frozen`, and shows the frozen source mesh on that record. A second Ctrl+Q spends nothing. F5/F9 keeps `frozen` and the mesh. The axe, the storm crystal, the bow, and the ice seed are still not this host, and the chip id stays unhosted.

## Before the walk

Opus merges. The mother walk needs this head on the play tree: Expel is Curse charge 5 at the mother after Dawn's curse line, and the r19-work head that posted the cab exit does not have that cast yet.
