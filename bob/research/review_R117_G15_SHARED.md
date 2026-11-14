# R117 review: G-15 shared spell core, bc5d2ef

Branch `sol/g15-spell-core-20261114`, worktree `~/opus_work/lol2_sol_spell_core`, head `bc5d2ef`, base `84d1fbc`. One commit, 10 files, +394/-16. No merge. This review read the diff and the spec `grok_research/SPELL_CORE_SPEC_20261113.md`. It did not boot Godot. Opus held the only Godot, on another tree. Sol's PASS receipts are his.

Verdict: AFTER FIXES.

## (a) An old save still loads, and Spark and Healing play as before

Holds in the code. `Magic.initial()` has no `spellbook`. `hive_magic_reward.restore` copies a spellbook only when the key is present, and `player_spell_book_test.gd` checks that an old packet round-trips byte for byte. Spark and Healing never enter `cast_quest_spell`: `cast()` returns to the old body when the school is spark or heal. That body is the same citadel Healing III cure, the same costs (1, 3, 10), and the same `spark()` ray. The label still says Level 3 Spark and Max Spark. This review did not boot a pre-commit save on the branch.

## (b) The panel shows schools the player has not learned

Fails. The spec says the panel grows only by casts the player has learned, and Spark and Healing start learned. The classic spell bar in `museum_interface.gd` always builds six buttons (heal, spark, curse, mists, prism, summon). `refresh_vitals` does not hide the unlearned ones. The debug grid in `player_starting_magic.gd` always builds the same six, and it is hidden only when the classic HUD is up. Keys 3 through 6 call `select_spell` for those schools even when they are unlearned. The right-click cycle does use `SpellBook.schools()`, which is spark and heal until a school is learned. That part matches. The buttons on screen do not.

## (c) Cost and refusal text is plain. Cooldown is silent

The refusal strings are plain: "That spell is not learned", "That charge is not available", "The curse is changing your form", "Not enough mana", "The spell has no effect here", "This form cannot cast", "Healing is blocked", "Already at full health". Costs are the spec table: curse 1/2/3/5 cost 1, 2, 2, 5; mists 1/3 cost 1, 3; prism 5 costs 5; summon 3 costs 3. Cooldown is not a message. `cast()` returns false when `cooldown > 0`, before `refuse()`, for the old schools and the new ones. The input test checks that a repeated Q leaves state unchanged and does not check a line of text. The same silence was already there for Spark and Healing. A plain cooldown line is the fix.

## (d) Nothing casts that the spec does not list

Holds. `CASTS` is exactly curse1, curse2, curse3, curse5, mists1, mists3, prism5, summon3. Beast form casts nothing. Curse charge 3 is curse3 in human form and curse2 in form 2. An unlearned school or an unknown charge refuses and spends nothing. No production script implements `accepts_player_spell` / `receive_player_spell`. A quest Q with no admitting child refuses "The spell has no effect here" and spends nothing. The input test's receiver is a fixture. Production quest effects remain 0/8, as the handoff says.

## (e) The tomb oil still takes its Spark

Holds. `l10_oil.gd` is not in the diff. `spark()` still calls `receive_spark_level(charge)` or `receive_spark()` on a `spark_receiver`. The oil ignites at the charge it is given, including charge 1. The spec's later "refuse charge 1" page is not in this commit. That is remaining work, not a change to the oil.

## What to fix before a merge

Hide curse, mists, prism, and summon on both panels until that school is learned, and do not let keys 3-6 select an unlearned school. Say the cooldown in the same plain refusal line, or record that silence is the chosen text. Do not merge on this head.
