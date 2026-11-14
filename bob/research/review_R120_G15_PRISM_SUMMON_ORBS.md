# R120 review: Prism 5, Summon 3, stored scrolls, c437c8d..12d9d56

Branch `sol/g15-casts-20261114`, detached worktree `~/opus_work/lol2_grok_r120`, head `12d9d56ee49fa36294cdf41c66594cc9bd9d2d74`. Sol's branch was left where it is. No merge.

Verdict: MERGE.

## Scope

Three commits: Prism 5 `cf4b375`, Summon 3 `dc389f3`, stored scrolls `12d9d56`.

Production edits are `l20_pillars_scotia.gd`, `l16_nw_traps.gd`, `l20_armory.gd`, `player_item_controller.gd`, `player_starting_magic.gd` (`use_stored_spell_from_interface` only), `item_catalog.gd`, `item_handlers.gd`, and the Museum scroll receipt helpers in `museum_inventory.gd`, `museum_scrolls.gd`, and `museum_scroll_state.gd`. The teaching table is not in this range. `act2_chargers.gd` is not in this range, and no glass-globe receiver is in this range. Docs, tests, and registry rows accompany the three commits.

## How the checks were run

Rendered Xvfb, Godot 4.7.2, audio Dummy, clock `time_scale` 1 and physics 60. The map tests refuse a headless display and refuse any other clock. Keys and inventory clicks are real input events. `stand_at` writes `global_position`. `learn_spell_group` and the scroll grants are disclosed fixtures. The Museum test sets the intro to complete, then takes the placed Summon scroll with E. None of this is an earned walk.

Log `/tmp/r120.log`, 2026-11-14T09:13Z to 09:15Z, display :354. Eight tests, each exit 0, no Parse Error and no SCRIPT ERROR.

## Prism 5 at the faux Scotia

Holds. `g15_prism5_input_test.gd` prints `PASS G15 Prism5 actual E negative/ShiftQ cost5/carrier/path separation/wrongcharges/duplicate/F5F9`.

E at `SCOTIA_AT` leaves `trinity` false. The E branch that used to set Trinity is gone from `l20_pillars_scotia.gd`. The pillar-shot E branch remains. Prism charge 1 and charge 3 leave `trinity` false and spend nothing. Shift+Q sets `trinity` and `pillars_moved`, spends 5, hides the faux Scotia body, and shows the existing carrier. `path_open` stays false because no pillar shot was recorded. A second Shift+Q spends nothing. F5/F9 keeps `trinity` and `pillars_moved`, and `path_open` stays false.

## Summon 3, City white ball

Holds. `g15_summon_city_input_test.gd` prints `PASS G15 Summon3 City real Spark3 negative/SummonCtrlQcost3/same body/F5F9`.

`receive_spark_level` on the ice body returns false. Ctrl+Q on Spark still spends 3 and leaves `ice` false. Summon charge 1 spends nothing. Summon Ctrl+Q sets `ice`, spends 3, and clears collision on body 90, the same ice prop. F5/F9 keeps the broken body. The brick click and the blue-bow fireball stay on their own input. No pyrapod and no summoned actor were added.

## Summon 3, armory

Holds. `g15_summon_armory_input_test.gd` prints `PASS G15 Summon3 armory real E brick-only/CtrlQball/bluebow click/all3 stop/F5F9`.

Summon 3 before the brick spends nothing and leaves `ball` false. E at control 62 sets `hacked` only. Summon Ctrl+Q aimed at source 196 sets `ball`, spends 3, and leaves `fire` and `stopped` false. A left click with the sword in hand leaves `fire` false. A left click with the blue bow at source 197 sets `fire` and `stopped`, and the bow stays in the pack. F5/F9 keeps `stopped` and the bow. `validate` rejects `stopped` unless `hacked`, `ball`, and `fire` are all true.

## Stored scrolls, where they are

The owner's Spark, Prism, and Mists orbs are these scroll definitions. Summon is the same kind of scroll. Positions below are the source tables. This review picked up one of them in the world: the Museum Summon scroll, by E. The other uses were grants of those source ids.

Spark, definition 75, `73-Spkscrl`. Museum `item12` and `item13` at (-1937, 30, -1168) and (-1915, 30, -1168). Dark Halls `control974u2:Spkscrl`. Act 2 `L10_DC` item21 and item22, region 1539, near (-486, 40, -2332) and (-495, 40, -2346).

Prism, definition 151, `149-Prsmscrl`. Dark Halls `control971u1`, `control975u1`, and `control975u2`. Act 2 `L9_DR` item12 and item20, region 2007, near (2482, 110, -2748). `L14_HT` item18 region 3659 and item19 region 3637. `L16_CA` item25 region 7484 at (14251, 200, 1382).

Mists, definition 150, `148-MoDScrl`. `L14_HT` item20, item21, item47, item48, and item49. `L16_CA` item26 region 8828 at (12609, 200, -1485).

Summon, definition 149, `147-SumScrl`. Museum `item16` at (-1937, 30, -1163). Dark Halls `control976u2:SumScrl`. Act 2 `L9_DR` item5 region 3158, `L10_DC` item34 and item35 region 4013, `L14_HT` item22 and item23, `L16_CA` item27 region 8828 at (13728, 200, -1368).

Healing definition 148 stays unhosted. The contract test asserts that, and it asserts handlers 32, 12, 34, and 33 are mode 1 only with native grade UNKNOWN.

## Using a scroll

Holds. Right-click in the inventory queues one request, the inventory closes, and `use_stored_spell_from_interface` calls the same `cast` the panel uses. A successful learn or cast consumes that source id, appends it to spent, and updates a Museum receipt when the scroll is one. The pickup does not respawn. There is no charge counter and no recharge. A refusal keeps the scroll and the mana.

An unlearned school can still be used. The first Mists scroll learns `mists1` and `mists3`, spends no mana, and records no head. The first Prism scroll learns `prism5`, spends no mana, and leaves `trinity` false. The first Summon scroll learns `summon3`, spends no mana, and leaves the ice intact. The Museum test takes `museum:item16:Summon_Scroll` with E and the right-click does that same learn. Spark is already a starting school, so the Spark scroll takes the cast path: notice `Level 3 Spark`, cost 3, consumed once.

A later scroll casts. The second Mists scroll at head 67 records that head and spends 1. The second Prism scroll sets Trinity and spends 5. The second Summon scroll breaks the same City body 90 and spends 3. The selected school stays Spark. A Mists scroll with no head in reach stays in the pack. A second Mists scroll during cooldown stays in the pack and the hint is `Wait a moment before casting again`. F5/F9 keeps the spent ids.

Pass lines:

- `PASS G15 stored mappings/mode1-only/native UNKNOWN/Heal excluded/Museum receipt reconstruction/consumed ID bounds`
- `PASS stored Spark3 + Mists first-learning/later-Q1/same receiver/refusal/F5F9 via actual I/grid rightclick`
- `PASS stored Prism learn then same Trinity5 cost5 via actual paused inventory/rightclick, F5F9`
- `PASS stored Summon learned then charge3 same ice body via actual I/rightclick/F5F9`
- `PASS actual Museum Summon E pickup -> actual I/rightclick learning -> F5/F9 receipts/spent/no respawn`

## Teaching rows

This range does not edit `player_spell_teaching.json`. Prism 5 and Summon 3 remain the chapter rows reviewed on `c437c8d`.

## Cemetery chargers and glass globes

This range does not edit `act2_chargers.gd` or a glass-globe receiver. Spark's existing `cast` path is what a stored Spark scroll calls at charge 3. The charge-1 globe receiver is the same function as before these three commits. I did not replay Cemetery props 242 and 247 in this run.

## Before the walk

Opus merges. r19-work was still `250a37c` when this review was written. That head has the L20 door and does not have Expel, Prism 5, or Summon 3. The mother walk needs the merged play head.
