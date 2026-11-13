# Spell core build spec, 2026-11-13

Read-only spec for Sol. Nothing here is built. Godot was not run. The port cited is r19-work `dacf858` at `~/opus_work/lol2_r18`. The needs note is the accepted census `grok_research/MAIN_QUEST_SPELL_ITEM_NEEDS_20261113.md`. Build this after Sol posts Cemetery READY, as the 01:51Z decision says.

The panel grows by exactly these casts: Curse 1 Dampen, Curse 2, Curse 3, Curse 5 Expel, Mists 1, Mists 3, Prism 5, Summon 3. Spark 3 is already on the panel. The oil change is to refuse charge 1. Stored scrolls of Spark, Prism, and Mists cast that school through the same functions. Nothing else. No Curse 4, no other level of any school, and no new damage table.

Mana figures marked PROPOSED are fixed adapter numbers in the same sense as the comment in `player_starting_magic.gd` that charge 3 costs 3. They are not native costs. A beat that does not need a hit point number does not get one.

## Panel

`player_starting_magic.gd` today offers Spark on key 1 and Healing on key 2. Q is charge 1, Ctrl+Q is charge 3, Shift+Q is charge 5. Costs already in that file: Spark charge 1 is 1 mana, Healing charge 1 is 2, charge 3 is 3, charge 5 is 10 unless an Ancient-stone charge makes it free. Charge 3 and charge 5 are refused while `player_curse.gd` phase is 1 or 3, except the citadel Healing charge 3 cure. `player_form_rules.gd` `can_cast` allows form 0 (human) and form 2 (lizard). Form 1 (beast) cannot cast. Those rules stay.

Add four schools to `select_spell`: key 3 Curse, key 4 Mists, key 5 Prism, key 6 Summon. The charge keys stay Q, Ctrl+Q, and Shift+Q. The wheel has no charge 2, so Curse 2 and Curse 3 share charge 3 and the current form picks which one, matching the book (Curse 2 only from lizard, Curse 3 only from human).

| School | Charge 1 (Q) | Charge 3 (Ctrl+Q) | Charge 5 (Shift+Q) |
| --- | --- | --- | --- |
| Spark | Spark, as now | Spark 3, as now | lightning aura, as now |
| Healing | Healing, as now | citadel cure only, as now | refused |
| Curse | Curse 1 Dampen | Curse 2 if lizard, Curse 3 if human | Curse 5 Expel |
| Mists | Mists 1 | Mists 3 | refused |
| Prism | refused | refused | Prism 5 |
| Summon | refused | Summon 3 | refused |

A school that is not learned yet refuses through the existing `refuse()` line and spends nothing. Spark and Healing start learned. The eight new casts start unlearned. Curse charge 3 and Curse charge 1 are allowed during curse phase 1 and phase 3. Every other school's charge 3 and charge 5 stay refused in those phases, as they are now. Curse 5 is also refused in those phases. It is not a way out of a morph.

## How a scroll teaches and casts

Prima, HINTBOOK 1593–1602: the first scroll of a new group adds that group. A later scroll of a group Luther already has casts the spell. Curse levels come from Dawn, not from those scrolls (HINTBOOK 708–710 and 1596–1597).

The owner's three names, Spark orb, Prism orb, and Mists of Doom orb, are not definition labels. The stored items of those schools are the scrolls below. Using one calls the same function as the panel. Glass globes and the chargers in `act2_chargers.gd` (Cemetery props 242 and 247, Ruins 1094) are a different system. Do not treat them as these scrolls.

Handler group 2 in `item_handlers.gd` (callee `0x8619C`, grade UNKNOWN) is the likely native learn-or-cast path. It is not hosted. The build uses the panel functions instead of decoding that callee.

On use of a carried scroll:

- If that school is not learned, learn only the levels in the table above, consume the scroll, and do not also fire a cast.
- If it is learned, cast the quest charge (Spark 3, Mists 1, Prism 5, or Summon 3) through the same receiver as the panel, then consume the scroll.
- A Spark scroll does not add Spark 2, 4, or 5. Spark 1 and Spark 3 are already known, so a Spark scroll takes the cast path.
- Heal scrolls are not this spec. Do not add Heal levels from them.

`museum_scrolls.gd` `record_consumption` already records a consumed museum scroll. Act 2 scrolls need the same consume-on-use. `act2_world_items.gd` already places every row in `act2_items_source.json` as an E pickup. The rows below are those placements. Positions are source `(x, height, y)`.

## Curse 1, Dampen

Book name: Dampen. HINTBOOK 716–722. Cast it in the moment before a shapeshift to stay as you are. The beast cannot cast, and the beast is forced back to Luther. At the ruins statue, Prima says to have Dampen mastered so the worm room is entered as human (HINTBOOK 3805–3812). Brady's statue steps do not name Dampen. The census already records that split.

Where it is learned. Monastery Dawn gives the Dampen charm, definition index 72, name `70-Dampen ch`, handler 27. `player_item_controller.gd` consumes the held charm and sets the dampened flag. `docs/monastery-dawn-dampen.md` says that use cancels a pending curse warning. The charm stays. Granting the charm learns Curse 1. The panel cast is the repeatable version.

How it is cast. Curse, charge 1. PROPOSED mana 1. No damage.

What receives it. `player_curse.gd`. The cast is legal only in phase 1 (the warning, `message()` returns "The curse stirs…"). It returns phase to 0, clears the timer, and leaves `player_form` as it is. It does not change a form that has already landed, and it does not make a lizard human. That is Curse 2. `l9_statue_walk.gd` `begin_fight` still requires `player_form == 0`. `l9_journal_hints.gd` already says the dampen spell is what holds that shape. No world script casts Dampen today.

Stand-in to remove. None. Do not remove the charm.

Proof, real input. Red on the current port: during a phase-1 warning the form still changes, and a non-human body never enters `begin_fight`. Green: Curse charge 1 during the warning spends 1 mana, the form stays 0, and `begin_fight` runs when the statue arrives. The same cast in phase 0 or phase 2 refuses and spends nothing. The charm still cancels one warning on its own use.

## Curse 2, Lizard to Luther

Book name: Lizard to Luther. HINTBOOK 723–724. It works only when Luther is the lizard.

Where it is learned. Savage Jungle shore. `l8_dawn.gd` `interact` takes the Bracers of the Dead and grants `act2:L8_SJ:dawn_control_token`, definition index 76, name `74-Control tokn`, handler 28. The feedback line calls it another piece of magic for controlling the curse. Acquiring that definition learns Curse 2, Curse 3, and Curse 5 together. A second copy is the live world row `act2:L8_SJ:item31` at (-1621, 50, 938), region 2934. Picking up either copy learns the three casts. Do not require the token to be consumed. Its handler effect stays UNKNOWN.

The Lizard seal, definition index 79, name `77-Lizard seal`, handler 29, is an excluded dormant row on L8 at (-1472, 230, -2713), region 3740, flags 4098. It is not a live pickup. Do not spawn it. The Bestial Disk from `l13_dawn_prison.gd` is Curse 4 (HINTBOOK 728–730) and stays off the panel.

How it is cast. Curse, charge 3, and only when `player_form` is 2. PROPOSED mana 2. No damage. Refused as human, as beast, and during phase 1.

What receives it. `player_curse.gd`. Set the form to 0 and leave phase 0. Do not copy the crevasse 60-second timer. Story curses (`request_cave_curse`, `request_region631_curse`) stay as they are.

Places that only test the form, and do not gain a new prompt: `l10_barrel.gd` (human hands), `l9_pyre.gd`, `l9_statue_walk.gd` `begin_fight`, `l10_priest.gd`, `l10_emperor.gd`, `l19_sewer_forms.gd` (human breaks the bars and shoots the switches). The sewer file says no opcode tests the form. The checks stay.

Stand-in to remove. `l12_crevasse.gd` `choose_form` and the E lines "Change to Lizard for the crevasse" and "Return to Human". The file's own comment says that E is the adapter until a curse-control UI exists. The spark on the rocks stays: `spark` still accepts charges 1 and 3, and still requires human.

Proof, real input. Red: at the crevasse the E is the only form change, and key 3 does nothing. Green: after the token, Ctrl+Q as a lizard sets form 0, spends 2 mana, and the crevasse E is gone. Ctrl+Q as a human does not call Curse 2. The rock spark still opens only for a human.

## Curse 3, Luther to Lizard

Book name: Luther to Lizard. HINTBOOK 725–727. It is the cast for a small gap.

Where it is learned. The same Control Token grant as Curse 2.

How it is cast. Curse, charge 3, and only when `player_form` is 0. PROPOSED mana 2. No damage. Refused as a lizard, as the beast, and during phase 1.

What receives it. `player_curse.gd`. Set the form to 2 and leave phase 0. Not the 60-second `request_timed_form(2, 60.0)` the crevasse uses. The form stays lizard until Curse 2 or a story curse changes it.

The crevasse is the place the census names for a chosen lizard body (`l12` ice route). `l19_sewer_forms.gd` also expects a lizard in the gutter. Those checks stay. L17 lizard help is not a lock and gets no new prompt.

Stand-in to remove. The same crevasse E as Curse 2. One removal covers both.

Proof, real input. Green continues the Curse 2 trial: Ctrl+Q as a human sets form 2, spends 2 mana, and the body fits the crevasse check that used to be the E. A second Ctrl+Q returns to human by Curse 2. The story warning can still start on its own.

## Curse 5, Expel

Book name: Expel the Curse. HINTBOOK 731–733. Usable once, at the end. The contents line titles the same beat "Expel Curse."

Where it is learned. The same Control Token grant. There is no separate Expel item. The cast succeeds only at the mother, so having it on the panel earlier does not open another lock. One success sets a saved flag and further Curse 5 casts refuse.

How it is cast. Curse, charge 5. PROPOSED mana 5. No damage number. The book does not give one, and the port's result is a quest flag.

What receives it. `l19_dawn_curse.gd` `_cast_curse`. `cast_level` is the constant 5. `accepts_level` accepts only 5. The first success at `MOTHER_AT` sets `glob_entered` and runs the birth relocation, which is what the E does now. The later E, "The demons fall", sets `demons_killed` and is not the spell. Leave that E. Dawn's talk E on L19, which increments `clicks` and can grant the ruby, also stays.

Stand-in to remove. The hint and the E branch "Expel the curse into the mother (ancient magic, level five)". After the change, that E does not set `glob_entered`. A cast that fails `curse_said`, `can_cast`, or `accepts_level` still shows the existing line "The mother shoots a fireball back. She does not die."

Proof, real input. Red: E at the mother sets `glob_entered` with no Curse school. Green: that E does nothing to the flag, Curse charge 5 at the mother sets `glob_entered`, spends 5 mana, and a second Curse 5 refuses. Curse charge 1 and charge 3 at the mother do not set it. The demons-fall E still works after the birth.

## Mists 1

Book name: Lesser Apparitions, one of Mists 1 and 2 (HINTBOOK 683–686). The quest use is one cast on each of four ghostly heads (HINTBOOK 5460–5462). The spell chapter's damage sentence is not this beat. No damage number.

Where it is learned. Definition index 150, name `148-MoDScrl`, handler 34. First use learns Mists 1 and Mists 3 and consumes the scroll. Live rows placed by `act2_world_items.gd`:

| Id | Position (x, height, y) | Region |
| --- | --- | --- |
| `act2:L14_HT:item20` | (1934, -125, -1223) | 3670 |
| `act2:L14_HT:item21` | (1370, -125, -1213) | 3648 |
| `act2:L14_HT:item47` | (-2979, 160, 311) | 3921 |
| `act2:L14_HT:item48` | (-1987, 160, 675) | 3943 |
| `act2:L14_HT:item49` | (-3753, 160, -696) | 3962 |
| `act2:L16_CA:item26` | (12609, 200, -1485) | 8828 |

Any one of them is enough. A later MoD scroll casts Mists 1 and is consumed.

How it is cast. Mists, charge 1. PROPOSED mana 1.

What receives it. `l19_ghostly_heads.gd`. Near a head, the cast appends that head to `shot`. When `shot` holds every head, `dragged` becomes true, which is what the E does now. A cast that is not near a head refuses and spends nothing. The imp-body hint stays.

Stand-in to remove. The hint "E — Level-one Mist of Doom at the head" and the E branch that appends the head.

Proof, real input. Red: E marks a head, and key 4 does nothing. Green: E does not mark a head, four Mists charge-1 casts mark the four heads and set `dragged`, and each cast spends 1 mana.

## Mists 3

Book name: Ghost, a level of Mists of Doom (HINTBOOK 687–690). The quest use is one way to freeze the city fountain (HINTBOOK 5151–5166). The same paragraph also names a blizzard axe, a storm crystal, the blue bow, and an ice seed. Those four are not this build.

Where it is learned. The same MoD scroll as Mists 1.

How it is cast. Mists, charge 3. PROPOSED mana 3. No damage.

What receives it today. Nothing. No L16 script reads a mists cast or a freeze flag. `l16_fountain_ball.gd` is the dry fountain and its own header says it is not this puzzle. `l16_sw_chips.gd` draws an `ice_fountain` mesh only after four ivory chips are placed. That mesh is not the freeze.

What to add. One new host, `l16_fountain_freeze.gd`, with a saved `frozen` flag. Mists charge 3, aimed at the fountain, sets `frozen`. Mists charge 1 does not. The prop and the coordinate of that fountain are not in the scripts read for this spec. Do not invent them. Sol names the prop in the build note from the city map. After `frozen` is set, breaking the ice and taking the chip is the book's next step. The chip's item id was not in those scripts either, so this page does not name one.

Stand-in to remove. None. The gap is the missing cast.

Proof, real input. Red: no cast sets a freeze flag, because the flag does not exist. Green: Mists charge 3 at the named fountain sets `frozen` and spends 3 mana. Mists charge 1 there does not. The axe, the storm crystal, the bow, and the ice seed still do not freeze it.

## Prism 5, Trinity

Book name: Trinity. HINTBOOK 661–667. At the end it removes the specters Belial summons. The quest lock is the faux Scotia (HINTBOOK 5501–5506). No second book method. No damage number. The port's result is the `trinity` flag.

Where it is learned. Definition index 151, name `149-Prsmscrl`, handler 33. Prima puts the scroll in a Dark Halls bookcase, right-clicked on Luther (HINTBOOK 2486–2488). Hosted Dark Halls pickups in `dark_halls_items.gd`: `darkhalls:control971u1:Prsmscrl`, `darkhalls:control975u1:Prsmscrl`, `darkhalls:control975u2:Prsmscrl`. Further live world rows: `act2:L9_DR:item12` and `item20` at about (2482, 110, -2748), region 2007; `act2:L14_HT:item18` (1934, -125, -1510), region 3659; `act2:L14_HT:item19` (1370, -125, -1510), region 3637; `act2:L16_CA:item25` (14251, 200, 1382), region 7484. The first use learns Prism 5 only. A later scroll casts Prism 5 and is consumed. `l20_pillars_scotia.gd` does not check the pack today, and it still does not. The learned flag is the gate.

How it is cast. Prism, charge 5. Charges 1 and 3 refuse. PROPOSED mana 5.

What receives it. `l20_pillars_scotia.gd`. Within reach of `SCOTIA_AT`, the cast sets `trinity`, and sets `path_open` and `pillars_moved` the way the E does now. Pillar shots stay on their own input: left click on the east lip, and the E that records a shot. Those are not Trinity.

Stand-in to remove. The hint "E — Trinity (prism, level five) at the faux Scotia" and the E branch that sets `trinity`.

Proof, real input. Red: E at Scotia sets `trinity`. Green: that E does not, Prism charge 5 does, spends 5 mana, and Prism charge 1 and charge 3 do not. The pillar-shot E still records a shot.

## Summon 3

Book name: Ancient Imp. HINTBOOK 607–616. The imp's magical attack is what some locks accept. The two locks are the white ball in the northwest city room, with a pyrapod fireball as the other book method (HINTBOOK 4830–4834), and the same pair in the armory (HINTBOOK 5522–5532). The pyrapod handler is not hosted. Do not add it.

Where it is learned. Definition index 149, name `147-SumScrl`, handler 12. Museum: `museum:item16:Summon_Scroll` in `museum_scroll_state.gd`, taken by `museum_scrolls.gd` `use`. Prima puts that scroll in the museum secret room (HINTBOOK 2097–2101 and 2132–2133). Also `darkhalls:control976u2:SumScrl`, and live world rows `act2:L9_DR:item5`, `act2:L10_DC:item34`, `act2:L10_DC:item35`, `act2:L14_HT:item22`, `act2:L14_HT:item23`, `act2:L16_CA:item27`. First use learns Summon 3 only.

How it is cast. Summon, charge 3. PROPOSED mana 3. No separate damage number. The ball either breaks or it does not.

What receives it.

City. `l16_nw_traps.gd` `break_ice`. The ice receiver's `receive_spark_level` calls `break_ice`, and `break_ice` returns false below level 3. The file header says a spark of charge 3 or more breaks the ice ball, and that this charge test is the logged adapter for the unhosted imp and the unhosted pyrapod. `receive_spark` already returns false, so charge 1 does not break it. Change: `receive_spark_level` returns false. Summon charge 3, on that same body, calls `break_ice(3)`. The hint "A level-three spark breaks the white ball" becomes a Summon 3 hint. Brick click and blue-bow fireball stay.

Armory. `l20_armory.gd`. One E at `AT_62` sets `hacked`, `ball`, `fire`, and `stopped` together. `validate` rejects `ball` or `fire` while `hacked` is false, so the brick stays first. After the split: that E sets `hacked` only. Summon charge 3 sets `ball` only when `hacked` is already true. The fire flag is set by the blue bow in hand, the same `accepts_fire` rule as `l16_nw_traps.gd` (`act2:L12_CM:blue_bow`), and only when `hacked` is true. `stopped` becomes true only when `hacked`, `ball`, and `fire` are all true. The bow is not consumed.

Stand-in to remove. The spark path into `break_ice`. The armory E no longer sets `ball`, `fire`, or `stopped`.

Proof, real input. Red: a Spark charge 3 ray breaks the city white ball, and one E in the armory sets all four flags. Green: Spark charge 3 leaves the white ball, Summon charge 3 breaks it and spends 3 mana, the armory E sets only `hacked`, Summon charge 3 then sets `ball`, and the blue bow sets `fire`. `stopped` waits for all three.

## Spark 3 on the tomb oil

Spark 3 is already cast by Ctrl+Q. This page is the oil gate only. Do not add Spark levels, and do not retune Spark damage (charge 1 is 8, charge 3 is 16, both already in `spark()`).

Book. Prima forbids Spark 1 and Spark 2 on the oil and names Spark 3 (HINTBOOK 3363–3410). Brady printed 101, lines 4212–4215, says "Spark Spell or Dragon's Blood" and does not name a level. The 01:51Z decision follows Prima: charge 1 is refused.

Where it is cast from. The panel, already learned. A Spark scroll, once Spark is known, also casts Spark 3. Cemetery rows `act2:L10_DC:item21` and `item22` are `73-Spkscrl`, definition index 75, handler 32, both in region 1539 near (-486, 40, -2332) and (-495, 40, -2346). Museum items 12 and 13 are the same definition. Dark Halls `darkhalls:control974u2:Spkscrl` is another copy. Jungle rows 18 and 19 name the same scroll and are outside this oil beat.

What receives it. `l10_oil.gd` `ignite`. Today `level not in [1, 3, 5]` is the refusal, `receive_spark` calls `ignite(1)`, and `receive_spark_level` passes the ray's charge. The barrel phase must already be 2. Change the accepted set to `[3]` only. Charge 1 returns false. Charge 5 returns false. `BLAST_RADIUS` 240 and `BLAST_DAMAGE` 20 stay. They are the existing blast, not a new damage table. Dragon's blood still does not light this oil. `ignite` never reads a bottle. That gap is not this page.

Dark Halls already requires charge 3. `dark_halls_crates.gd` `on_spark` returns false unless `charge` is 3. Leave it.

Other Spark receivers keep charges 1 and 3. The census lists them: ruins bridge, tower, bracers niche, chapel orbs, Hive brazier, Claw niche and the frozen bow, citadel globes, Temple body. This spec does not edit those.

Stand-in to remove. The charge-1 success. There is no E prompt on the oil.

Proof, real input. Red: after the barrel is tipped, Spark charge 1 ignites the oil. Green: charge 1 does not, charge 3 does, and the blast numbers are unchanged. A ruins globe still lights from charge 1, so the refusal is the oil and not every Spark receiver.

## The three stored casts, and the missing holder

The owner, board 01:42Z, called the Cemetery orbs stored spells: a Spark orb, a Prism orb, and a Mists of Doom orb, from the sunken city, and said another holder was missing at (468, -1805, -88).

No definition label is "Spark orb", "Prism orb", or "Mists of Doom orb". The items that store those schools are the scrolls in the sections above: `73-Spkscrl`, `149-Prsmscrl`, and `148-MoDScrl`. Their use rule is the scroll section at the top. The phrase "sunken city" is the owner's. This spec does not assign that phrase to a map.

The aimed wall is not a fourth orb. Sol's note `sol_lane/generic_l10_20261112/integration_8a53cce/OWNER_R19F_FOLLOWUP_20261113.md` reads the owner bundle `report_2026-11-13T01-35-21_1514177624` at (468.3966, -87.9525, -1805.428). The screenshot shows no holder. The hosted chargers are not at that point. The nearest prop, 379 at (492, -120, -1512), is behind the view and has no events. Sol says it must not be labeled as the holder, and that the native identity is not established. This spec adds no prop, no charger, and no spell payload at that coordinate.

## Not in this build

Curse 4, Heal 2 and Heal 4 and Heal 5, Spark 2 and Spark 4 and Spark 5, Summon 1, 2, 4, and 5, Prism 1 through 4, Mists 2, 4, and 5. The pyrapod. The fountain's axe, storm crystal, bow, and ice seed. Dragon's blood on the oil. A damage table for any of the new casts. The Lizard seal dormant row. Any new object at (468, -1805).

## Proof set

One real-input pass per page above, red on `dacf858` and green on the build. The oil charge-1 refusal is checked beside one unchanged charge-1 receiver, the ruins globe. Old saves load with Spark and Healing learned and the new schools unlearned. No Godot run was used to write this spec.
