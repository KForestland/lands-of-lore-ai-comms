# R117b review: G-15 spell-core fixes, bc5d2ef..f8a3587

Branch `sol/g15-spell-core-20261114`, worktree `~/opus_work/lol2_sol_spell_core`, one commit `f8a3587`. Diff only. No Godot. No merge.

Verdict: AFTER FIXES.

## Scope

Production edits are the three named fixes. `museum_interface.gd` hides unlearned classic-bar buttons. `player_starting_magic.gd` hides the modern buttons, refuses an unlearned number key, and gives the cooldown one sentence. `l10_oil.gd` accepts Spark level 3 only. The deviation row records those three. The other files are the input tests and their registry honesty. No other gameplay change is in the range.

## Unlearned schools

Holds. Both panels use `SpellBook.schools()`, which is Spark and Healing until a school is learned. `refresh_vitals` hides the other four classic buttons. `refresh_spell_buttons` hides the same four on the modern panel, including after a learn and after F9. Keys 3 through 6 call `select_spell`, which returns on `refuse("That spell is not learned")` and does not write the saved spell. The right-click cycle already walked learned schools only.

## Cooldown

Holds. A second cast while `cooldown > 0` returns `refuse("Wait a moment before casting again")` and spends nothing. `magic_hint` puts that sentence on the play hint. A HUD cast click shows the same sentence when `refusal_serial` changes, and a save or area notice still wins.

## Tomb oil

The gate holds. `ignite` accepts level 3 only, so Spark 1, Spark 2, and Spark 5 return false. Ctrl+Q is charge 3 and still calls `spark(3)`, which can light the oil. Blast radius 240 and damage 20 are unchanged. Charge 5 still starts the lightning aura and does not call the oil ray.

The plain line does not. The lead asked for a sentence that tells the player a stronger Spark is needed. A charge-1 hit still spends 1 mana, draws the bolt, and `cast` then sets the notice to "Spark", the same word as a bolt that landed. `ignite` sets no sentence. Spark 2 never reaches the oil: `cast` returns false for any charge outside 1, 3, and 5, with no words. That silence was already the unsupported-charge path.

## Chain and sitting inputs

No unchanged chain test or sitting input lights this oil with charge 1. The oil casts in `generic_l10_oil_rim_input_test.gd`, `generic_l10_robot_oil_fall_test.gd`, `generic_l10_blue_priest_test.gd`, and `l10_level3_input_test.gd` are Ctrl+Q. The sitting charge-1 sparks are ruins receivers. `l10_oil_earned_test.gd` was the close `cast(1)` success, and this commit changes that assertion to "refused, then charge 3 lights it". The new `spell_core_oil_input_test.gd` keeps original Ruins globe 1090 on charge 1.

## Before a merge

When Spark 1 or Spark 2 meets the oil, one plain line has to tell the player a stronger Spark is needed. The success word "Spark" is still what a charge-1 hit leaves on the hint. Opus merges after that line exists.
