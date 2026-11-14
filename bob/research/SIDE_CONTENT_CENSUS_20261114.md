# Side content census, 2026-11-14

Port checked read-only. Marks use `~/opus_work/lol2_grok_tombposes/scripts/lol2` (project.godot 2026-11-14). The same names were searched under `~/opus_work/lol2_r18/scripts/lol2` when the tomb tree had no owner. No Godot run. One mark per row: in the port, partly, missing, unknown in the data.

## Guides on disk

- Prima, *Lands of Lore: Guardians of Destiny Unauthorized Game Secrets* (Edward Carmien): `~/AI_COMMS/reference_hintbook/hintbook.txt` and `lol2-hintbook.pdf`.
- BradyGames *Official Guide* (Keith / Barton), tesseract OCR: `~/AI_COMMS/reference_hintbook/brady_guide.txt` and `brady_lol2_official_guide.pdf`. The OCR header says printed page = PDF page − 1. This census quotes only the cave-hint sentences that were read (chapter 4 hints). Brady chapters 7–9 (maps and answers) were not mined, so Brady-only secrets outside those sentences are not rows.
- German secrets guide *Schon gewusst? – Lands of Lore II* (Onkel Dave): `~/AI_COMMS/reference_schon_gewusst_lol2/schon-gewusst-lol2.txt` and `schon-gewusst-lol2.pdf`. Every numbered section is a row. The guide says these quests do not finish the game.

Prima chapters 7–14 were not read line by line. Contents titles that were not matched to a sentence already in the tables are listed at the end and marked unknown in the data. No page numbers were assigned.

"missing" means the level's `scripts/lol2` owners were searched and no owner of that thing was found. "unknown in the data" means the guide does not name a mechanic, or the search hit a nearby file that was not the named thing.

## L1_DC Draracle’s Caverns

| Thing (guide name) | Mark | Evidence |
|---|---|---|
| Höhleneingang — form death videos; Prima, Beast at the entrance is "gory TV" | in the port | `cave_entrance_death.gd`: human / beast / lizard movies `luthrdie`, `bst-die`, `liz-die`. |
| Gladstonewache braten — Spark 1 on the puddle, sword plus "verbrannten Panzer" | partly | `cave_captain_state.gd` grants `5-Short swd` then `37-Brnt Chain` (`cave_captain_items.gd`). `cave_captain*.gd` has no puddle or water-Spark trigger. |
| Säule zerschlagen — ceiling on the guard, fight and magic experience; Brady, worn pillar drops the ceiling | in the port | `cave_pillar_trap.gd`: hit prop878, rubble, guard dies in regions 1934/0/1952, magic 200 and fighting 200. |
| Grasp / shove the blocking pillars (Prima "Grasp the middle pillar"; Brady "shove the pillar") | missing | `cave*.gd` has no drag-aside pillar. `cave_crate_stack.gd` says the pillar grasp is a different sentence and does not implement it. |
| Höhlenspülung / Prima "A Side Journey"; Brady, magic on the stalagmite, flood, then items | partly | `cave_prop83_lift.gd` and `cave_flood_movie.gd` play the flood. No `Halberd`, `3-Halberd`, Streitaxt, or "Meridian" placement under `cave*.gd`. Halberd exists only as a definition in `docs/item-definitions-source.json`. |
| Wasserfall der Heilung — drink for a full heal; Brady, the pool heals | partly | `cave_cfall.gd` / `cave_cfall_room.gd`: both pools drink and heal by the source amount (file comment: heal 5), not a full heal. |
| Geschenk des Orks — Prima, he dies before the gift; German guesses an Ancient Stone or an orc shield and two broken clubs | partly | `cave_old_orc.gd` plays the talk clips. No gift grant in that file. `cave_stone_manafoil.gd` is a separate `66-Ancients stn` on prop1050. |
| Stack the boxes; Prima, a mace upstairs; Brady, "Two orc maces and a shield" | partly | `cave_crate_stack.gd` shoves crates. It names two `2-Br Mace` rows and says no item is spawned. |
| Ancients' Stone in the dishes, chain-cut room (Prima) | partly | `cave_stone_manafoil.gd` grants `66-Ancients stn`. No dishes hotspot in `cave*.gd`. |
| Brücke zerstört? — Spark 3 or an arrow on the far pillars rebuilds the bridge | missing | `river_chain_interaction.gd` is the chain bridge. No far-pillar rebuild in `cave*.gd`. |
| Pull the lever by the bridge and take the items (Prima) | unknown in the data | "lever" hits in the cave scripts are not a bridge-loot owner. |
| Drarakelsequenzen — soldiers on the bridge, or Kenneth alone | unknown in the data | `cave_draracle_door.gd` is only leaves 74 and 77. No pursuit-movie owner in `cave_draracle*`. |

## L3_DH Draracle’s Museum

| Thing (guide name) | Mark | Evidence |
|---|---|---|
| Zurück zum Drarakel — two more videos; Prima, see him twice, a third visit annoys him | partly | `museum_draracle.gd`: local19 0 plays `e032e`, local19 1 plays `e033e`. Dawn/Baccata and a third clip are not in that header. |
| Eingang zum Museum — push the tapestry; Prima, east wall, violet stones | in the port | `museum_curtain.gd`, control81. Violet stones were not a separate owner. |
| Skelettschlüssel — niches narrate the exhibits; Prima, triangular stone | in the port | `museum_key_locks.gd`, 17 Sk-key locks. |
| Direkter Weg zu "Alle Fackeln entzünden" — key in the floor, skip the long axe | partly | `museum_key_locks.gd` names movable55, the SS1 panel. The shortcut past the long axe was not separated from the long-arm route. |
| Alle Fackeln entzünden — long axe, lizard duct, two Höhlenaloes, Spark on the flame, magic level; Prima, "Axe of the Long Arm" | partly | `museum_torches.gd` flares prop61, one magic level, 35 torches. `museum_long_arm.gd` is prop153. The two duct aloes were not checked in `museum_aloe.gd`. |
| Magierollen — 1 summon, 1 spark, 2 healing; Prima, secret-room scrolls, one new spell group | partly | `museum_scroll_state.gd`: two Spark, two Healing, one Summon (`museum:item12`–`item16`). Spark count is two, not the German one. |
| Drachenstein — Spark 1 on the brown crate; Prima, "dragon gem" | partly | `museum_dragon_heart.gd` is prop216 and item25. The crate-explosion Spark is not in that header. |
| Magischer Transmitter — sword shards, key, charge empty fire crystals once; Prima, bash the blue gem for fire crystals | partly | `museum_crystal.gd`: melee on prop297 reveals items 6/5/4; Spark 1/1 is refused. No one-charge wall fill. |
| Zwei Elfenbeinspäne — smash the vases; Prima, two ivory chips | in the port | `museum_ivory.gd`, urns 189/195, items 17/18. |
| Versteck Blitzschlagkristall; Prima, Spark the brown blob in the barred alcove | in the port | `museum_lightning_crystal.gd`, `56a-Ltng cr`, region1010. |
| Wurmsprung — invisible platform, 2 Heldensteine, 2 Ahnensteine, later a transporter | partly | `museum_worm.gd` is the prop163 movie only. No stone grants in that file. |
| Unbekannter Raum auf Karte | unknown in the data | The guide says the room's function is unknown. No owner of an unlabeled museum room. |

## L4_HJ Huline Jungle (shrine, village, hive approach)

| Thing (guide name) | Mark | Evidence |
|---|---|---|
| Hidden Shrine / Tür bei Beschwörungsrolle — lizard tunnel or a switch, gargoyles, summon scroll, falling floor, spikes, long axe (Prima chapter 6; German 3.1) | partly | Jungle world rows include summon-area loot (`jungle_world_items_catalog.gd`). `jungle*.gd` has no gargoyle, spike, or shrine owner. `jungle_inner_gate.gd` is Kelsrick's gate, not this door. |
| Nische in Gang bei Beschwörungsrolle — 2 healing, 2 guardian orbs, 1 shield, 2 spark, 2 stones, 5 dragon blood, 2 lightning crystals | in the port | `jungle_world_items_catalog.gd` rows 20–21 HlScrl, 29–30 Guardian orb, 15 Guard shield, 18–19 Spkscrl, 16–17 Rock, 24–28 Drag Blood, 22–23 Ltng cr. Pickup: `jungle_world_items.gd`. |
| Echsengeheimnis — 8 Höhlenaloe, 2 Ahnensteine, 1 Sturmkristall | partly | Catalog rows include eight Cave aloe (7–14), Ancients stn, and Storm. `jungle_world_items.gd` does not gate them to the lizard. |
| Dschungeltür — inner lever, open five seconds | missing | No five-second jungle door in `jungle*.gd`. |
| Langarmaxt bei Kit'yara if the museum was skipped | missing | `jungle_kityara.gd` has no Long arm grant. |
| Teich trockenlegen — hit the geyser; lizard burrow with a talking stone, 2 fire crystals, 1 storm crystal, 3 ancient stones | partly | `jungle_river_dam.gd` breaks prop250, sinks the floors, opens the burrow. It names items 41/42/68–72. Catalog shows 41/42 Fire crstl and 68 Storm. The talking stone and a count of three stones were not in that comment. |
| Fels vor Höhleneingang — stand clear, Spark the liquid | partly | `jungle_oil_fire.gd` is Spark on the oil-pool rock (prop1350), the pool Prima puts before the Hive, not named as the cave-mouth rock. |
| Hulinenmagier — only the broken Thohan broadsword plus the hollow-hand dagger, output Dolch des Lichts | missing | No dagger-of-light trade under `jungle*.gd`. `l8_shaman_trade.gd` is the Savage Jungle. |
| Obdachloser Huline — he wants water; the guide has no method | missing | No homeless / thirst owner in `jungle*.gd`. |
| Kelsrick meucheln — poison paint on the weapon, one hit, village does not notice | partly | `jungle_kelsrick.gd` passes `last_poison` into the hit (`docs/poison-paint.md` cited there). `R-p paint` is catalog row 39. The one-hit quiet kill is not in the header. |
| Kelsrick tötet Luther — a short video | unknown in the data | `jungle_kelsrick.gd` hosts the fight. A player-death movie was not in the lines read. |
| Zweiter Auftrag des Passwortgebers | unknown in the data | `thieves_den.gd` and `jungle_kelsrick.gd` were not a second commission. |
| Stein neben Hulinendorf als Zünder — oil into the village, 5 stones if blasted, 6 if the ruler is killed by hand | unknown in the data | `jungle_oil_fire.gd` is not that stone. `jungle_chief_hut_state.gd` mentions a raised-water fire, not the 5-vs-6 stones. |
| Kampf Vielarmiger Tod vs Monsterspinne — lure him, watch through the peephole, a level | missing | No spider-versus-death owner in `jungle*.gd`. |
| Mulde in Lavasee — five gas stones, if left alone the hollow floods | missing | No gas-vent owner in `jungle*.gd`. |
| Verschiebbare Säule — niche where Shalla was; the guide rejects the "stops the collapse" claim | partly | `hive_shalla_state.gd` places her; cry groups stay unrun. `hive_pillar.gd` is "Visual review only". |
| Indyfallenabwehrknöpfe — a platform that fails; the stone breaks into the rune room | partly | `hive_boulder_sequence.gd` runs the boulder. The failing buttons are not in that header. |
| Unbekannte Räume Eins und Zwei | unknown in the data | The guide does not name a function. |

## L7_DH Dark Halls, and the monastery on the jungle approach

| Thing (guide name) | Mark | Evidence |
|---|---|---|
| Falsche Sounddatei bei Statue — Tohani-warrior line | missing | No "Tohani" string in `dark_halls*.gd` or `monastery*.gd`. |
| Tür im Gemüsegarten — locked click; exit from the closet past Rix | missing | `dark_halls_atrium.gd` is the garden bed (chain, roof, bell fruit), not that door. |
| Sprengkiste unter Guckloch — 2 prism, 1 summon, 1 healing, 1 ancient stone, 1 spark | unknown in the data | `dark_halls_loot_source.json` was searched for those names and not matched to a peephole. It does name `85-Colims amult` and `14-Plasma staff`. |
| Rix' Fluch aufheben — the guide lists failed tries, including a CD exorcism movie | partly | `dark_halls_rix.gd`: death sets GV_RIX_DEAD and E gives the plasma staff. "Talk and give-item branches are not hosted." |
| Stahltür aufsprengen — crate, then a rat, 13 crates, a talking stone, feud gloves, Colim's amulet | partly | `dark_halls_crates.gd` blows the steel door. `85-Colims amult` is in `dark_halls_loot_source.json`. The rat, 13 crates, stone, and gloves were not in that header. |
| Zwei Fenster auf eine Kiste — one crate covers two windows; Kelim's amulet | partly | The same crate file says the shove also opens the seven-o'clock window. It does not place one crate on two windows. |
| Geisterkugel verschieben — the guide thinks it does nothing | partly | `dark_halls_orb.gd`: the orb rises and shades come. No player shove of the orb. |

## L5_HC Hive Caves

No German section. Prima contents name "Big Ore Sword", "Because He's the Waxman", and "The Purposeful Tourist". Those chapter bodies were not read. `hive_reaver_amber.gd` takes a sword in the Reaver alcove and can collapse it. `hive_wax.gd` picks up `hive:item0:Wax`. They are not marked as those titles. See the unread-title list.

## L8_SJ Savage Jungle

| Thing (guide name) | Mark | Evidence |
|---|---|---|
| Untergrundsystem — entrances in large trees, 3 Steine der Ahnen | unknown in the data | `l8_tree.gd` is the torch platform ("Tree with Raised Platform"), not this tunnel. |
| Echsengang in die Dracoidenruinen | missing | No lizard passage to the ruins in `l8_*.gd`. |
| Leiter — left click teleports Luther up | partly | `l8_cache_ladder.gd`: E climbs control 69 both ways. Not a left-click teleport, and the group has no return hop in the source. |
| Verschlossenes Gebäude — tribe member, or lizard if the village was slaughtered; 3 ancient stones, 2 guardian orbs | partly | `l8_clubhouse.gd` opens for a tribe member and names Ancients' Stones. No lizard-slaughter branch and no guardian orbs in that header. |

## L10_DC Dracoid Cemetery

German 6 is side content. Prima's charger chain is the solving route; it is included because those puzzle names were read in the contents and the owners cite them.

| Thing (guide name) | Mark | Evidence |
|---|---|---|
| Gebäude mit Schräge — lizard up the slope, reflective plate, 3 ancient stones | missing | No "Reflective" owner in `l10*.gd`. |
| Statuenrätsel — fireballs through the next statue; the guide treats it as broken | missing | No statue-fireball owner in `l10*.gd`. |
| Säule außerhalb Gebäude — spells do nothing | missing | No such column owner in `l10*.gd`. |
| Säule in Gebäude — on the automap, no known use | missing | Same search. |
| Platten neben Sarg — two plates slide; lamp pulls Luther down | missing | `l10_tombs.gd` is the globe plates, not these coffin plates. |
| Glaskugel unter Schädel | missing | No skull-globe owner in `l10*.gd`. |
| Beschwörungsrollen und Steinquader | missing | No summon-scroll column owner in `l10*.gd`. |
| Zwei Räume hinter Schädelwand — empty | missing | No skull-wall rooms in `l10*.gd`. |
| Unbekannte Kartenabschnitte | unknown in the data | The guide does not name a function. |
| Gold Globe Charger, White Charger, Blue Globe Charger (Prima contents) | in the port | `l10_tombs.gd`, `l10_emperor.gd`: yellow, white, and blue globes. |
| But the Barrel Didn't Tip Over (Prima contents) | in the port | `l10_barrel.gd`, switch61 / movable74, barrels 477/177/176. |
| But I Can't Light the Oil (Prima contents) | in the port | `l10_oil.gd`. |
| Silverleaf at Last (Prima contents) | in the port | `l10_silverleaf.gd`, trees 159–170. |

## L9_DR Dracoid Ruins

| Thing (guide name) | Mark | Evidence |
|---|---|---|
| Raum hinter Mauer — lizard hop, 2 stone cubes | missing | No wall-hop cubes in `l9*.gd`. |
| Wasserröhren für Zugang zur Dracoidenkneipe — attack the pipes; the door floats up | missing | `l9_flood.gd` is the post-fight rising water, not these pipes. |
| Echsengang zur Dracoidenkneipe — out on the bar | missing | No lizard bar exit in `l9*.gd`. |
| Bierfass — the guide leaves it as beer | missing | No beer barrel in `l9*.gd`. |
| Einbrechende Wand — beds fly, two mutated dracoids | missing | No collapsing-wall owner in `l9*.gd`. |
| Geheimgang hinter Bücherregal — 3 lightning daggers left; right, Vels fruit, a healing scroll, a lit column toward the Belial statue | missing | Bookcases are `dark_halls_bookcases.gd` (L7), not L9. |
| Kampf in Arena — near death teleports you to the many-armed death | missing | No arena owner in `l9*.gd`. |
| Überdachung — columns that will not fall | missing | No canopy owner in `l9*.gd`. |
| Gegenüber See — a torch and nothing else | missing | No far-shore torch owner in `l9*.gd`. |
| Bett des Dracoidenkönigs — gargoyle opens the traitor axe; needs the Claw Mountain bracers | missing | No `Ax Traitor` or gargoyle bed in `l9*.gd`. |
| Knopf am Königsstuhl — chair slides, Ring der Heilung | missing | No chair-button owner in `l9*.gd`. |
| Knopf an Stuhl an großer Tafel — the guide says the button does nothing | missing | Same search. |
| Verschlossene Tür — skeleton key; a lightning crystal and Coco's cap | missing | No locked-door pair of those items in `l9*.gd`. |
| Unbekannte Kartenbereiche | unknown in the data | The guide does not name a function. |

## L12_CM Claw Mountains

| Thing (guide name) | Mark | Evidence |
|---|---|---|
| Dawns Höhle — evil Luther, ambush after the Ruloi | missing | No Dawn ambush in `l12*.gd`. |
| Pagode in See — Blizzard axe from the nearest floe, without entering | missing | No `Blizzard` string in `l12*.gd`. |
| Eisschollensurfen — full loop, cave with a recipe, a bezoar ring, Obsidian mail after three stakes are burned | partly | `l12_niche_armor.gd`: Spark reveals `act2:L12_CM:item5`, feedback "Obsidian chain mail". No recipe, ring, or three stakes in that file. |
| Eisschollen anhalten — Summon blocks a floe; repeat to join them | missing | `l12_river_rafts.gd` moves rafts 50/51/55. No Summon stop. |
| Kenneths Anhänger — four clicks, throw the fake, the real one is a status boost | partly | `l12_citadel.gd`: one search gives the picture; breaking it gives the charm. Not four clicks or a thrown pendant. |
| Unbekannter Raum on the map, near the shard longbow | unknown in the data | The guide does not name a function. |

## L13_RC Citadel of the Ruloi

| Thing (guide name) | Mark | Evidence |
|---|---|---|
| Brutraum — break the egg device, drain the acid, Myriadenarmbrust, Bastionshellebarde, Feiglingsschild | in the port | `l13_eggs.gd` drains the basin and gates items 145–147. `act2_items_catalog.gd` names that basin placement `33-Myriad`, `20-Bastion`, `51-Cowards sh`. |
| Amboss — only Thohan's broadsword and Firestorm | missing | No anvil or Firestorm forge in `l13*.gd`. `l13_altar.gd` is the boss gate. |
| Unbekannter Raum auf Karte | unknown in the data | The guide does not name a function. |

## L14_HT Huline Temple

| Thing (guide name) | Mark | Evidence |
|---|---|---|
| Bett — both column switches, or a left click; 1 ancient stone, 1 Coco's cap. Prima, push the headboard | partly | `l14_bedroom.gd` pushes the headboard and opens the passage. Those two items are not in that file. |
| Türen im Gang mit drei Feuerbällen — six doors, lava seals the rest; two summon scrolls | unknown in the data | `l14_fire_paths.gd` exists. It was not matched to the six doors. |
| Spawnflamme der Spinnen — click to stop the spiders; the guide says it fails | unknown in the data | `l14_spider_burrow.gd` and `l14_spider_passage.gd` were not matched to a spawn flame. |
| Rezept hinter Banner — tear the banner for a strong-poison recipe; wall behind gives 2 guardian orbs and a Valkyrie crossbow | missing | No banner, poison recipe, or Valkyrie row in `l14*.gd`. |
| Katzenring — crouch at two statues; one cup aloe, one poison paint, drawer with the ring | missing | No crouch, cup, or cat ring in `l14*.gd`. |
| Unbekannter Raum auf Karte | unknown in the data | The guide does not name a function. |

Prima contents "Three Puzzles", "Three Statues", and "The Faux-Belial" were not read. They are in the unread list. `l14_tilt.gd`, `l14_trials.gd`, and `l14_belial.gd` were not matched to those titles. `l14_belial.gd` is the Hive Lord fight.

## L16_CA City of the Ancients

| Thing (guide name) | Mark | Evidence |
|---|---|---|
| Elfenbeinspan-Podest — one chip opens two areas; the chip comes back out | partly | `l16_sw_chips.gd`: pedestals 173–176 take a chip. Its header says doors 89–91 stay shut and a fourth L16 ivory placement was not found. |
| Zwei Silberblattsträucher — run to the white ball, the floor lifts | unknown in the data | Not the greenhouse below. No bush-lift owner in `l16*.gd`. |
| Eiswand mit Feder auf Tisch — ball breaks the ice; feather; skeleton key, talking stone, and the named ingredient list | unknown in the data | `l16_fountain_freeze.gd` is prop626, the ice-fountain trigger, not a feather on a table. |
| Alraunen-Kelch — mandrake root, then all 9 recipes and four scrolls | missing | No mandrake or chalice in `l16*.gd`. |
| Balkon — the guide says Anu killed Belial here and finds no use | missing | No balcony owner in `l16*.gd`. |
| Verschiebbare Statuen — by the jewel scarab | missing | No movable-statue owner in `l16*.gd`. |
| Unbekannte Kartenabschnitte | unknown in the data | The guide does not name a function. |
| Prima greenhouse, as cited by the owner: silverleaf in the glass pyramid, hourglass, fireball opens the tower doors | in the port | `l16_greenhouse.gd`. This is not German 11.2. |

## L17_HC Subterranean Caverns

No German section. Prima chapter 14, "Subterranean Caverns", was not read. No row.

## L19_BC Belial’s Laboratory

No German section. Prima "Belial's Laboratory" and "Belial's Summoning Room" were not read. No row.

## L20_BB Birthing Chamber

| Thing (guide name) | Mark | Evidence |
|---|---|---|
| Waffenkammer — all four dragon parts, quickly; Mists 5 may help. Prima contents, "The Armory" | in the port | `l20_armory.gd`: controls 62–67, one blow on 62, Summon 3 on the white ball, a blue-bow click on the fireball. |
| Unbekannte Räume auf Karte | unknown in the data | The guide does not name a function. The German text still headers this page "Stadt der Ahnen". |

## Prima contents titles whose chapters were not read

Marked unknown in the data. A same-area owner is noted only so it is not mistaken for a match.

| Title | Mark | Search |
|---|---|---|
| Big Ore Sword | unknown in the data | `hive_reaver_amber.gd` takes an unnamed sword. Chapter body not read. |
| Because He's the Waxman | unknown in the data | `hive_wax.gd` is `71-Wax` style hive item0. Chapter body not read. |
| The Purposeful Tourist (third through eighth floors) | unknown in the data | No floor-tour owner matched. |
| Hopper Tunnels | unknown in the data | Chapter body not read. |
| Fishy, Fishy, Fishy, Fish? | unknown in the data | Chapter body not read. |
| Torches on Platform | unknown in the data | `l8_tree.gd` lights five torches. Not matched to this title. |
| Three Puzzles (Amaze Me, Tilt Me, Fire Me) | unknown in the data | `l14_tilt.gd` and `l14_trials.gd` not matched. |
| Three Statues and Another Puzzler | unknown in the data | `l14_idol_pedestals.gd` not matched. |
| The Faux-Belial (temple chapter) | unknown in the data | `l14_belial.gd` is the Hive Lord, not read against this title. |
| Secret Storeroom | unknown in the data | No storeroom string in `l16*.gd`. |
| Dragon Special Scene Area | unknown in the data | `l16_dragon_room.gd` not read against this title. |
| Silverleaf Chasm | unknown in the data | Not `l16_greenhouse.gd`. |
| Chip Quest: Water Torture, Leap of Faith, Dancing in the Fountain, Be a Blockhead | unknown in the data | Not matched to `l16_sw_chips.gd`. |
| Starry Tower | unknown in the data | No starry-tower owner read. |
| The Last Faux-Belial | unknown in the data | Chapter body not read. |

## Counts

German sections: 96. Other rows: 9 read Prima or Brady sentences that are not the same German section (pillar shove, crate maces, dishes stone, bridge lever, three cemetery charger rows counted as one, barrel, oil, silverleaf, greenhouse) plus 15 unread Prima titles.

| Mark | Count |
|---|---|
| in the port | 14 |
| partly | 30 |
| missing | 41 |
| unknown in the data | 35 |
| Total rows | 120 |

in the port: entrance deaths, pillar-trap ceiling, museum curtain, skeleton key, ivory chips, lightning crystal, summon-corridor niche loot, Ruloi basin weapons, cemetery globe chargers, barrel, oil, silverleaf trees, greenhouse, armory.

Brady chapters 7–9 were not mined. Those pages can add rows this file does not have.
