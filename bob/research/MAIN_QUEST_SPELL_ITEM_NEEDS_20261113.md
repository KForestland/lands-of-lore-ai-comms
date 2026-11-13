# Main-quest spell and item needs, 2026-11-13

Read-only. The port is r19-work and playtest/r19f, both `dacf858`. Script rows are from `~/opus_work/lol2_r18/scripts/lol2/`. Godot was not run.

A row is required when that level's main errand does not finish without the cast or the use. Extra loot, combat advice, and a path the book marks as optional stay on the "not required" line.

Prima printed folio is the form-feed index in `reference_hintbook/hintbook.txt` minus 12. HINTBOOK numbers are lines in that file. Brady printed page is the PDF page minus 1 in `reference_hintbook/brady_guide.txt`, and a Brady sentence is here only where that OCR line was read. The books stay in separate sentences. No longplay time is cited. The guides name each cast.

Port words: **real** means the cast, or the carried item, is what completes the beat. **Stand-in prompt** means an E or click line completes the beat and the named school is not cast. **Missing** means neither.

The cast panel is `player_starting_magic.gd`. It offers Spark and Healing only, at charges 1, 3, and 5. Charge 1 and charge 3 are rays. Charge 5 starts the lightning aura and does not hit a spark receiver. Charge 3 and charge 5 are refused while the curse phase is 1 or 3. There is no Curse, Summon, Prism, or Mists school on the panel.

## The short list

Spells the main quest names, and what the port does with them today:

| School and level | Where the quest names it | Port today |
| --- | --- | --- |
| Spark, level left unnamed | Ruins bridge, tower, bracers niche, chapel orbs; Hive brazier; Claw mail niche and blue bow; Citadel globes, egg light, elevator; Temple body | Real. Charges 1 and 3 both hit those receivers. |
| Spark 3 | Cemetery tomb oil. Dark Halls crystal door, and the same charge on the window exit. | Real. `l10_oil.gd` also accepts charge 1, which Prima forbids. |
| Curse 1, Dampen | Prima, ruins statue, so Luther stays human. | Missing. The fight checks human form and never casts Dampen. |
| Mists 1 | Four ghostly heads. | Stand-in prompt. |
| Curse 5, Expel | Mother beast. | Stand-in prompt. The script's level is the constant 5. |
| Prism 5, Trinity | Faux Scotia. | Stand-in prompt. |
| Summon 3 | White ball, with a pyrapod fireball as the other book method. | Missing. City trap accepts a Spark 3 ray instead. Armory E on the brick marks the ball done. |
| Mists 3 | One way to freeze the city fountain. The book also names a blizzard axe, a storm crystal, the blue bow, and an ice seed. | Missing. No freeze host in the L16 scripts. |
| Heal 3 | Prima tells you to open the citadel Belial fight with it. | Real only as that fight's poison cure. It is not a door. |
| Curse 2 and Curse 3 | The book's way to choose human or lizard. Several gates ask for a form. | Missing as casts. `player_curse.gd` morphs on its own. |

Heal 2, Heal 4, Heal 5, Spark 2, Spark 4, Spark 5, Summon 1, 2, 4, and 5, Prism 1 through 4, Mists 2, 4, and 5, and Curse 4 are not named as a lock on this chain.

The items the same errands use are in the level sections. The cast panel does not have to grow to "every spell." It does have to grow past Spark and Heal if Dampen, Mists 1, Curse 5, and Prism 5 stay real casts rather than prompts.

## Dracoid Cemetery, L10_DC

Prima chapter 9, running headers from printed 98. Brady's numbered cemetery steps are printed 101 and 209–210.

| Need | Source | Port |
| --- | --- | --- |
| Dracoid Sigil, used on the gate. The shaman gives it on L8. | Prima p.97, HINTBOOK 3256–3259. Gold doors come first, Prima p.98, HINTBOOK 3266–3271. `l10_main_gate.gd` `unlock` refuses any carried id except the sigil. | Real. E calls `unlock` with the sigil id, and the function still requires that id in the pack. |
| Empty glass globe on a charger, then the charged globe in the matching tomb or box. One gold globe is enough for the first stage. One white globe opens the switch tomb. Two blue globes are the minimum, one for the priest and one for the end. The third blue globe is the Valkyrie crossbow, which the book does not require. | Prima p.99–103, HINTBOOK 3320–3322 and 3418–3443. Brady printed 101, lines 4216–4221: two empty glass orbs on the blue altar. | Real. `act2_chargers.gd` `interact` takes a carried definition 98. `l10_emperor.gd` places the carried globe whose definition matches that box. |
| Human form to tip the barrel. This is a form, not a numbered spell. | Prima p.100, HINTBOOK 3355–3362. Brady printed 101, lines 4205–4208, says click the barrel, and does not name the form. | Real form check. `l10_barrel.gd` returns "You need human hands" unless `player_form` is 0. E tips it. |
| Spark 3, or a placed bottle of dragon's blood, on the oil, from far enough away. Prima forbids Spark 1 and Spark 2. | Prima p.100–101, HINTBOOK 3363–3410. Brady printed 101, lines 4212–4215: "Use your Spark Spell or Dragon's Blood on the oil," with no level, and the blast opens the catacombs. | Spark 3 is real: `l10_oil.gd` `ignite` accepts 1, 3, and 5 after the barrel's phase is 2, and the panel's charge 3 ray calls it. Charge 1 also ignites, which Prima forbids. Charge 5 on the panel never reaches this function. Dragon's blood is missing here. `player_dragon_blood.gd` can place a bottle, and `ignite` never reads one. |
| Bracers of the Dead, worn, so the priest can be understood. He then gives the urn. | Prima p.103, HINTBOOK 3440–3446. Brady printed 209, the step-42 lines: give the urn back and receive the ankh. | Real. `l10_priest.gd` `speak` refuses without `DeadBracers.available` on the pack. E speaks. The bracers come from the ruins niche below. |
| Urn, filled in the ruins, given back to the priest. He gives the ankh. | Prima p.103–104, HINTBOOK 3446 and 3454. Brady printed 209, steps 42–43. | Real. `l10_priest.gd` `exchange_ashes` trades the filled urn. |
| Ankh, placed in the slab, then used again inside. | Prima p.104, HINTBOOK 3454–3457. Brady printed 209, steps 43–44. | Real. `l10_emperor_entry.gd` and `l10_emperor.gd` take the ankh id from the pack. |
| Gold, then white, then blue globe, each in its box. Then take the remains. | Prima p.104, HINTBOOK 3458–3464. Brady printed 209, step 44, names yellow, blue, and white, and still wearing the bracers to hear the Emperor. | Real for the three globes and the remains pickup. `l10_emperor.gd` matches `State.COLORS`. The port does not add a separate bracers check on that speech in the lines read here. |
| Nine silverleaves, picked, then offered on L8. Picking is the cemetery errand. The offer is the L8 row. | Prima p.104, HINTBOOK 3481–3483. Brady printed 210, step 48: gather silverleaf and return to the settlement. | Real pickup. `l10_silverleaf_harvest.gd` `pick`. |

Not required on this level: bone-brazier sparks (Prima calls them useful, HINTBOOK 3429–3434; `l10_braziers.gd` accepts any spark and ignores the level), the third blue globe, and the Valkyrie crossbow.

## Dracoid Ruins, L9_DR

Prima chapter 10, running headers from printed 108. Brady's "to complete this level" list is printed 182–183, and the same errand is steps 36–47 on printed 209–210. The two books do not name the same spell at the statue.

| Need | Source | Port |
| --- | --- | --- |
| Spark, level not named, on the black orb. The bridge rises. | Prima p.111, HINTBOOK 3676–3679. Brady printed 94, line 3842: "Cast a spark spell against the Pedestal to activate a magic bridge." | Real. `l9_magic_bridge.gd` `activate` runs from `receive_spark`, so panel charges 1 and 3 both do it. |
| Spark, level not named, on the two tower globes. One drops the upstairs field. One opens the basement stair. Charge two white globes on the charger in that room. | Prima p.111, HINTBOOK 3690–3700. | Real spark. `l9_tower.gd` `light` has no level argument. Real globe. The same `act2_chargers.gd` insert. |
| Spark, level not named, on the niche after the large Saar, to take the Bracers of the Dead. | Prima p.112, HINTBOOK 3710–3711. Brady printed 182, list item 2: kill the Ssar Priest to get the bracers, and it does not name the spark. | Real spark. `l9_dead_bracers.gd` `release` also requires actor 79's health at 0. |
| Drag the priest's body onto the altar. Spark, level not named, on both orbs. Click the urn on the ashes. | Prima p.112, HINTBOOK 3739–3748. Brady printed 182, list item 4, and printed 209, steps 38–39: spark both Dragon orb pedestals, then click the urn. | Real. `l9_pyre.gd` `ignite` takes either spark charge. `urn` inserts the urn id. E drags, lays, and fills. Human form is required (`player_form` 0). |
| Emperor's remains, placed in the bowl. The statue walks. | Prima p.114, HINTBOOK 3792–3804. Brady printed 183, list item 6, and printed 209, step 45. | Real. `l9_statue.gd` is the offer host the walk reads through `l9_statue_state.gd` `offered`. |
| Curse 1, Dampen, so the worm room is entered as human. | Prima p.114, HINTBOOK 3805–3812. Brady's list and step 45 do not name Dampen or a form. | Missing. `l9_statue_walk.gd` `begin_fight` requires `player_form` 0 and does not read a spell. The journal line in `l9_journal_hints.gd` mentions Dampen. A human can pass without casting it. A player stuck in another form cannot cast Dampen to get out. |
| The wooden grate at the flood. Prima: pick it up and throw it, or stand on it until it floats. Brady: push the platform into the water and step on. | Prima p.115, HINTBOOK 3840–3846. Brady printed 183, list item 7, and printed 210, the lines after step 45. | Real for standing on raft 82. `l9_escape.gd` raises it while `aboard(82)` after the table lift. The throw and the push are missing. |

Not required: door-floating (Prima says the level can be finished without it, HINTBOOK 3602–3606), the hard river route (HINTBOOK 3755–3771; the chapel errand is the same once you arrive), and the green-leaf caption at HINTBOOK 3648, which sits on the figure and is not a separate lock in the paragraph.

## The rest of the chain

Order is the Prima walk. Cemetery and ruins are visited more than once. Each level is listed once.

### L1_DC, Draracle's Caves

No required cast and no required item use to leave. The exit is the bridge and the flight south. Prima contents p.56, HINTBOOK 2050–2056 and 2113–2114.

The museum, which this chapter enters next, is where the dragon's-blood bottles and the Summon scroll are picked up. Those uses are on later rows. Spark on the museum's brown blob is marked optional in the same chapter: "You don't have to open this gate here" (HINTBOOK 2104–2106).

### L3, Museum inside the Halls

| Need | Source | Port |
| --- | --- | --- |
| Summon scroll, right-clicked on Luther, if a later beat is played as Summon 3. The white-ball beats have another book method, so the scroll is not a lock by itself. | Prima contents p.58, HINTBOOK 2097–2101 and 2132–2133. | Pickup is real. `museum_scrolls.gd` `use` adds the scroll to the pack. Learning a school from it is missing. The cast panel never gains Summon. |

### L4_HJ, Huline Jungle

No required cast to leave the jungle. A bramble opens to the sword as well as to Spark (`jungle_bramble.gd`). Spark is the lasting method in the earlier bramble note, and the sword is enough to pass.

### L5_HC, Hive Caves

| Need | Source | Port |
| --- | --- | --- |
| Iron flute, played at the pit so the lift rises, and later set in the oil-trap slot. Prima says that without the flute and two bits of wax you cannot continue. | Prima p.77–78, HINTBOOK 2659–2668 and 2684–2686. | Real lift signal. `hive_elevator_state.gd` `play_flute`. The slot floor is `hive_flute_floor.gd`. |
| Spark, level not named, on the brazier beside the falling floor, on the way to the rune screen. | Prima p.78, HINTBOOK 2691–2693. | Real Spark 1. `hive_rune_light.gd` `cast` is the charge-1 path in `player_starting_magic.gd`, and the hint is "Q — Cast Spark". A fire crystal can light the same brazier through `ignite`. |
| Wax, clicked on the runes, twice. | Prima p.78, HINTBOOK 2695–2698. | The wax pickup is `hive_wax.gd` `collect`. The double click on the runes was not re-read in a rune script this pass, so that use stays ungraded rather than called real. |

### L7_DH, Dark Halls

| Need | Source | Port |
| --- | --- | --- |
| Prism scroll, right-clicked on Luther. Prism 5 is a later lock and the book gives it no second method. | Prima contents p.70, HINTBOOK 2486–2488. | The item exists as `darkhalls:control971u1:Prsmscrl` in `dark_halls_items.gd`. Using it to learn Prism is missing. Trinity below does not check the pack. |
| Spark 3 on a crystal crate set beside the steel door. A further Spark, level not numbered in the paragraph, blows the bricked window that is the stated exit. | Prima p.72, HINTBOOK 2528–2540. The contents list titles the blue ball on p.73. | Real, and both blasts ask for charge 3. `dark_halls_crates.gd` `on_spark` returns false unless the crate is open and `charge` is 3. |

Healing scrolls in the same halls are for the ghost fights. They are not a lock.

### L8_SJ, Savage Jungle

| Need | Source | Port |
| --- | --- | --- |
| Silverleaf, offered at the village after the cemetery has grown it. The initiation follows. A few sparks in that bout are combat, not a lock. Prima says a sword and a few sparks end it. | Prima contents p.88, HINTBOOK 3069–3073. | Real item. `l8_tribe.gd` `offer` consumes a carried silverleaf once `l10_silverleaf.grown` is set. The bout itself is left-click or E to yield. |
| A second silverleaf, offered to the shaman, who gives Amaranth Serum. | Prima contents p.88, HINTBOOK 3075–3077. | Real. `l8_tribe.gd` `offer_shaman`. |
| Amaranth Serum mixed with a silverleaf, activated on Luther, then right-clicked on the Larkhon's upper chest. Human form. This is the way into the Claw Mountains. | Prima contents p.91, HINTBOOK 3146–3157. | Real. `l8_larkhon.gd` `offer`. The hint is the right-click line, and the function still applies the carried vapors. |
| Dreamstone, used on the temple door, after the citadel. Retrieve it. | Prima p.130, HINTBOOK 4304–4309. | Real. `l8_temple_door_state.gd` `insert`. |

Not required to finish the level: Spark on the tree torches and the shard chest (Prima contents p.92, HINTBOOK 3104–3113; `l8_tree.gd` `spark` accepts charges 1 and 3). That room makes a spare soothing potion. The first serum is the one the Larkhon row uses. A heal after the river jump is rest (HINTBOOK 3150–3151), and health also returns over time in the spell chapter.

### L12_CM, Claw Mountains

| Need | Source | Port |
| --- | --- | --- |
| Spark, level not named, on the river niche tripod. Obsidian mail appears. Prima calls it a key item for continued success. | Prima contents p.127, HINTBOOK 4223–4225. | Real. `l12_niche_armor.gd` `spark` accepts charges 1 and 3. E only takes the mail after that. |
| Lizard form through the ice tunnel, then human again. | Prima contents p.127, HINTBOOK 4236–4239. | Form check only. Curse 3 is missing as a cast. |
| A fire spell from a pyrapod, or a spark, to melt the blue bow out of the ice. The bow is the city's fireball method and the armory's fireball method. | Prima contents p.127, HINTBOOK 4240–4245. | Spark is real. `l12_frozen_bow.gd` `spark` accepts charges 1 and 3, then E catches the bow. The pyrapod swap is missing. `l16_nw_traps.gd` says the pyrapod handler is not hosted. |

### L13, Citadel of the Ruloi

| Need | Source | Port |
| --- | --- | --- |
| Spark, level not named, on the globes: egg-chamber door, elevator, and the globes that raise the bridge to Dawn. | Prima contents p.124–125, HINTBOOK 4086–4099 and 4118–4126. | Real. `l13_egg_door.gd` `light`, `l13_elevator.gd` `activate`, and `l13_spires.gd` `light` accept charges 1 and 3. |
| The light over the eggs. Prima says shoot it so the basin drains. | HINTBOOK 4092–4096. | Real as Spark 1 or 3. `l13_eggs.gd` `break_vent`. The eye switch beside it is a separate E, `open_eye`. |
| Dreamstone, used to open Dawn's cell, and not consumed. Then the same stone in the exit slot, and retrieved. | Prima contents p.126–127, HINTBOOK 4137–4139 and 4203–4208. | Real. `l13_dawn_release.gd` and `l13_exit_lock_state.gd` `insert`, which refuses anything except definition 136. |
| Heal 3, as the first action of the Belial-spawn fight, against poison. Ancient-stone Heal 5 is offered as a spend, not a lock. | Prima contents p.126, HINTBOOK 4173–4178. | Real for this one fight. `player_starting_magic.gd` charge 3 on Healing calls `l13_belial.gd` `cure` when `cure_available` is true. The fight can be scripted without treating this as a door. |

Placing the old sword on the altar makes the Dark Sword (HINTBOOK 4185–4196). Later fights accept the blue bow or the horn in its place, so the altar is the book's weapon step and not the only way through the last fight.

### L14_HT, Huline Temple

| Need | Source | Port |
| --- | --- | --- |
| Dreamstone on the entrance. Already the L8 door row. | Prima p.130, HINTBOOK 4304–4309. | Real, as above. |
| Aloe in the western bowl and poison in the eastern bowl, after the body is on the slab. | Prima p.132, HINTBOOK 4348–4352. | Real. `l14_priest_ritual.gd` `offer`. E offers, and the function still takes the carried reagent. |
| Spark, level not named, on the body after the floor descends. | Prima p.132, HINTBOOK 4353–4355. | Real. `l14_priest_ritual.gd` `spark` accepts charges 1 and 3. |
| Two green crystal shards, one from the wooden post and one from the niche, both set so the way on opens. | Prima p.132, HINTBOOK 4376–4377. The journal line in `l14_journal_hints.gd` names both bowls. | Real take for the post shard, `l14_post_shard.gd`. Real bowl use, `l14_shard_bowls.gd`, which lists both shard ids. |

### L16_CA, City of the Ancients

| Need | Source | Port |
| --- | --- | --- |
| Destroy the ball over the dry fountain. Prima says any means. Nine lichen clumps follow. | Prima contents p.145, HINTBOOK 4805–4814. | Real as a left-click strike. `l16_dry_fountain.gd` and `l16_fountain_ball.gd` say "Left click — Strike the floating ball." A spark receiver also calls `break_ball("spark")` / `break_orb("spark")`. No school is required. |
| Northwest room. Blue bow on the fireball. Summon 3, or a pyrapod fireball, on the white ball. A hit on the spinning brick. | Prima contents p.147, HINTBOOK 4830–4834. | Blue bow is real. `l16_nw_traps.gd` `break_fire` requires the bow in hand, then a left click. Summon 3 and the pyrapod are missing. `break_ice` returns false below level 3, and the hint says a level-three spark breaks the white ball. That ray is a stand-in for the two book methods. The brick is a real left click, `break_brick`. |
| Ivory chip, set in the pedestal and retrieved. | Prima contents p.155, HINTBOOK 5094–5109. | Real. `l16_sw_chips.gd` "E — Set an ivory chip on the pedestal." |
| Spark, level not named, on the globes that reveal the force-field chip. | Prima contents p.155, HINTBOOK 5115–5116. | Not re-opened as its own receiver this pass. Left ungraded. |
| Fountain chip. Mists 3 is one freeze. The same paragraph names the blizzard axe, a storm crystal, the blue bow, and an ice seed. | Prima contents p.156, HINTBOOK 5151–5166. | Missing. The L16 scripts have no mists, freeze, or ice-seed host. |
| Southeast oil. Spark, level not named. A bow appears. | Prima contents p.149, HINTBOOK 4915–4920. | The spark receiver calls `l16_se_oil.gd` `burn("spark")`. A left click also calls `burn("melee")` with no cast. The click is a stand-in prompt beside a real spark path. |
| Silverleaf in the greenhouse pyramid, then the hourglass. | HINTBOOK 4888–4894. | Real. `l16_greenhouse.gd` E lines for the leaf and the hourglass. |
| Dreamstone is not spent by the towers. The chip and the leaf are the uses that must be carried. |  |  |

### L17, Subterranean Caverns

No required cast. Prima says run for the exit, and killing the spiders is optional (HINTBOOK 5363–5366). The red strands are cut with an attack (HINTBOOK 5383–5385). Lizard form is a help, not a lock.

### L19, Belial's Laboratory

| Need | Source | Port |
| --- | --- | --- |
| Human form to break the bars, then lizard form through the gutter, then human again to shoot the three switches. | Prima contents p.166, HINTBOOK 5416–5423. | Form changes are the curse timer, not Curse 2 or Curse 3. Those casts are missing. |
| Mists 1, one cast on each of the four ghostly heads. | Prima contents p.167, HINTBOOK 5460–5462. | Stand-in prompt. `l19_ghostly_heads.gd` shows "E — Level-one Mist of Doom at the head" and the E key appends the head. No Mists cast exists. |
| Curse 5, Expel, into the mother beast. | Prima contents p.167, HINTBOOK 5477–5486. The contents map on printed 160 titles the same beat "Expel Curse." | Stand-in prompt. `l19_dawn_curse.gd` shows "E — Expel the curse into the mother (ancient magic, level five)". `cast_level` is the constant 5, and `accepts_level` only accepts 5. The player never selects the school. |

Belial's horn is a gift from Baccata on this level (HINTBOOK 5411–5413). It is one of three weapons that work on the last Belial. Keeping it is the book's advice. The port grant was not the question of this row.

### L20, Birthing chamber, armory, and the last fight

| Need | Source | Port |
| --- | --- | --- |
| Prism 5, Trinity, on the faux Scotia. | Prima contents p.168, HINTBOOK 5501–5506. | Stand-in prompt. `l20_pillars_scotia.gd` shows "E — Trinity (prism, level five) at the faux Scotia" and the E key sets `trinity`. |
| Armory. Hit the spinning brick. Summon 3, or a pyrapod spark, on the white ball. Blue bow on the fireball. | Prima contents p.169, HINTBOOK 5522–5532. | Stand-in prompt for all three. `l20_armory.gd` shows "E — Hack the spinning brick" and that E sets `hacked`, `ball`, `fire`, and `stopped` together. |
| One blow on the last Belial, with the blue bow, the Dark Sword, or Belial's horn. Prima says they have the same effect. | HINTBOOK 5557–5558. | The prompt is "E — Attack Belial" in `l20_finale.gd`. Which weapon is in hand was not asserted in the lines read. The three weapons are alternates in the book, so none of them is the only item. |

## What this sizes

The shared spell core the quest text actually names is Spark, with level 3 kept distinct for the cemetery oil and the Dark Halls crate. Prima adds four casts the panel does not have: Dampen, Mists 1, Curse 5, and Prism 5. Those four are a prompt or a missing cast on `dacf858`. Summon 3 and Mists 3 can stay off the core if the other book method for each beat is the one that gets built. Heal 3 is the citadel fight's opening advice, and the port already cures poison there.

The item list is longer than the spell list. The locks are the sigil, the glass globes, the bracers, the urn, the ankh, the remains, silverleaf, the amaranth dose, the dreamstone, aloe, poison, the two temple shards, the flute, the wax, the blue bow, and the ivory chip. Dragon's blood is the oil's other method in both books, and the oil script does not see it.
