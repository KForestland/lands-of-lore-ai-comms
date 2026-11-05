# R5 item, spell, and creature tables, 2026-11-02

Prep for a later items/RPG phase. `formula_finished` stays false. The level-3 Spark request amounts 40 and then 35 stay the request-amount term from the entered item11 report. They are not hit points, and they are not copied into this table. No creature hit-point, armour, or experience block was printed on the pages opened here. The Brady index line "Hit Points, 43" points at the War Cluster sentence on printed page 43.

Printed Brady page = PDF page − 1, confirmed on the Silverleaf page: `brady_ocr/p-042.txt` footers as page 41 and `brady_guide.txt` marks it `PDF PAGE 42 = PRINTED PAGE 41`.

## Spell names, two books

HINTBOOK `hintbook.txt` lines 520–733, chapter "What Luther Does". The contents give that chapter's start as printed page 9. These rows were not each pinned to a later printed page.

BRADY `brady_guide.txt` markers PDF 47–53 = printed 46–52.

| group level | HINTBOOK name | BRADY name |
|---|---|---|
| Heal 1 | Lesser Heal | Lesser Heal |
| Heal 2 | Damage Shield | Damage Shield |
| Heal 3 | Poison Cure | Poison Shield |
| Heal 4 | Greater Heal | Greater Heal |
| Heal 5 | Regenerate | Regenerate |
| Spark 1 | Lesser Spark | Lesser Spark |
| Spark 2 | Greater Spark | Greater Spark |
| Spark 3 | Chain Spark | Chain Spark |
| Spark 4 | Lightning | Lightning |
| Spark 5 | Lightning Storm | Lightning Storm |
| Summon 1–5 | Lesser Imp, Greater Imp, Ancient Imp, Imp Lord, Banish | Imp, Greater Imp, Ancient Imp, Imp Lord, Banish |
| Prism 1 | Blind | Blind |
| Prism 2 | Invisibility | Invisibility |
| Prism 3 | Hologram | Hologram |
| Prism 4 | Photon Blade | Sunray |
| Prism 5 | Trinity | Trinity |
| Mists 1–5 | Lesser Apparition, Greater Apparition, Ghost, Spectral Phantoms, Lich | Lesser Apparition, Greater Apparition, Ghost, Spectral Phantoms, Lich |
| Curse 1 | Dampen | Dampen Change |
| Curse 2 | Lizard to Luther | Change to Human |
| Curse 3 | Luther to Lizard | OCR on printed 48 reads "Tertbied bones to Lica"; the name was not recovered |
| Curse 4 | Luther to Beast | Change to Beast |
| Curse 5 | Expel Tha Curse | Expel Curse |

Heal 3, Prism 4, and Curse 2 through 5 use different names in the two books. The names stay in their own columns. Spark 3 is Chain Spark in both. Prima's sentence says the effect hops from target to target. Brady printed 51 says a sphere of electricity ricochets. Those two sentences stay book descriptions. The entered item11 report still names level 3 as effect 22 at handler `0xD1B7F`. Range and selected mana stay unread.

Prima gives no magic-point cost. It calls Lesser Spark cheap, Greater Spark a bit more, Lightning quite a bit, and Greater Heal expensive, and it says Greater Heal usually heals more than half the health bar. Brady gives no magic-point cost in this chapter. Brady printed 52 says the poison shield stays up for 30 seconds. That 30 is the book's duration, and the handler was not entered.

Both books say the beast has no magic. Prima says Curse 5 is used once, at the end. Brady printed 50 says a level-5 Control spell expels the curse at the end, and that the Mantle of the Ancients supplies the Control spells. Ancient Magic stones add the fifth level, up to nine charges, on Brady printed 49. A Force Pod is described as the same kind of charge. No charge count was read from the executable.

## Item effects read off Brady

OCR titles that are blurred are marked. Amounts are the printed sentences, not decoded handlers.

| printed page | item as read | effect as printed |
|---|---|---|
| 40 | Aloe Leaf | heals 5 |
| 40 | Cave Aloe | heals 5 |
| 40 | Stone of the Cobra | cuts melee and missile recovery time in half |
| 41 | Ironwood Sap | no effect by itself |
| 41 | Amber | no effect by itself |
| 41 | Venom Sac | ingested: 5% Greater Poisoning, 20% Lesser Poisoning |
| 41 | Lamplight Eggs | low-light vision for 1 minute |
| 41 | Brook Flounder | an eye in the back of the head for 1 minute |
| 41 | Gorgonite Modules | 5% chance of beast form for 1 minute |
| 41 | Silverleaf | 5 Magic Points |
| 42 | Mandrake Root | unconscious 5 seconds, protection 0, Magic +20, Health +40 |
| 42 | Amaranth Serum | no effect by itself |
| 42 | Tar Crystals | no effect by itself |
| 42 | Rainbow Sulfite | 5% chance of lizard form |
| 42 | Black Lichen | heals 20 |
| 43 | Champion Stone | Sap plus Amber, or found; Strength +20 for 1 minute |
| 43 | Poison Paint | Venom Sac plus Lamplight Eggs; Lesser Poisoning if ingested; Lesser Poison on blade attacks |
| 43 | War Cluster | Venom Sac plus Amber; Hit Points +20% for 1 minute; death if it wears off inside the danger zone |
| 43 | Force Pod | Poison Paint plus War Cluster; acts like an Ancient's Stone |
| 44 | Acid Sac | Lamplight Eggs plus Tar Crystals; thrown, opponent hit points and combat points −25% for 15 seconds |
| 44 | Pod of the Changeling | Champion Stone plus Acid Sac; Mega-beast for 1 minute; no effect if already the beast |
| 44 | Pyro Pod (OCR "PYRA POD") | Tar Crystals plus Mandrake Root; Spark group becomes Fire Spark for 2 minutes |
| 44 | Mana Foil (OCR "Inans Foit") | Silverleaf plus Rainbow Sulfite; Magic Points +50 |

Deviation `0115` already records Mana foil definition 133, handler 43, as a native +50 mana call. This pass did not re-enter that call. Deviation `0221` already uses Silverleaf +5. The printed sentence agrees with that 5. The Aloe 5 and the Mandrake 40 are book heal amounts. They are separate from the Spark request amounts 40 and 35.

## Creature stats

No bestiary table of creature hit points, attack, or experience was on printed Brady 40–52 or in the Prima spell chapter. None is published here. Printed 53–58, read in the next section, also have none. The index line "Hit Points, 43" still points at the War Cluster sentence.

## Item rows the first table did not carry

BRADY `brady_guide.txt` and the matching `brady_ocr` page files. Printed page = PDF page − 1. These rows sit on printed 39, on the top of printed 40 before Aloe Leaf, at the bottom of printed 43, and at the top and bottom of printed 44. The rows already in the first table are not repeated. OCR titles that are blurred stay as read. No handler was entered. `formula_finished` stays false.

| printed page | title as read | effect as printed |
|---|---|---|
| 39 | OCR "BEzodr's RinG" | protects from Lesser Poison |
| 39 | GREATER BEZOAR'S RinG | protects from Greater Poison |
| 39 | CATRING | halves the damage from a fall; does not enable a longer fall |
| 39 | JEWELED SCARAB | protects from the effects of Ancient Magic and reduces damage |
| 39 | OCR "Iron Rop" | protects from electrical attacks; the sentence compares it to a lightning rod |
| 39 | KENNETH'S CHARM | some protection from physical and magical attacks, and increases strength |
| 39 | POWER ORB | total hit points +10%; if removed while only that extra 10% remains, you die |
| 40 | OCR "KELEn's RinG" | a bare-handed blow causes the damage of a tiger's claws, and a loud snarl; beneficial as the lizard |
| 40 | OCR "VEL's Fruit" | red fruit; negate the effects of any poison |
| 43 | LARKHON VAPORS | Silverleaf plus Amaranth Serum; knocks out the Larkhon, required for the Citadel of the Ru-loi; also knocks you out for a few seconds, with no beneficial effects |
| 44 | OCR "SATH SAC" | Venom Sac plus Tar Crystals; ingested, Greater Poisoning; applied to weapons, Greater Poisoning on the damage |
| 44 | OCR "Ininp CLUSTER" | Gorgonite Nodules plus Rainbow Sulfite; psychic detection; the entire automap of the current level, including secret areas |
| 44 | STONE OF THE GORGON | Black Lichen plus Gorgonite Nodules; a touch turns the opponent to stone |

The Power Orb trade sentence on printed 39 is broken in the OCR ("Sword Fir", "Thohan's Broken Sword"). The sword name was not recovered. The Champion Stone row in the first table omits the same printed-43 sentence: it enables use of the OCR name "Reamer of Great Orc." That name was not joined to any other book's weapon name.

HINTBOOK names for the same recipes stay in this paragraph and are not copied into the Brady column. `hintbook.txt` lines 1262–1273: Lamplight eggs plus Venom sac is "Poison"; Tar crystals plus Poison sac is "Death sac"; Silverleaf plus Amaranth potion is "Arkan sleep potion"; Gorgonite nodule plus Rainbow sulfite is "Mind cluster"; Black lichen plus Gorgonite nodule is "Stone of the gorgon." Line 1138 says a death sac poisons a weapon and is "presumably stronger" than the poison from lamplight eggs and venom sacs. Line 1183 says a mind cluster shows the whole level, with unexplored areas in white. Line 1218 says the Stone of the Gorgon turns a foe to stone "for a while." Lines 3146–3157 tell the player to combine an amaranth potion with a silverleaf and use the result on the Larkan, and a nearby line spells the creature Larkon. Those hintbook names and the Brady titles above stay unmerged. Poison Paint is not renamed Poison. Larkhon Vapors is not renamed Arkan sleep potion. The OCR title SATH SAC is not renamed Death sac. The ingredient pair on that Brady row is Venom Sac plus Tar Crystals; the hintbook Death sac pair is Tar crystals plus Poison sac.

Printed 45 is the chapter title only (OCR "Spel antl Magic"). It adds no effect row.

## Effect pictures, printed 52–58

BRADY. The spell-name table above is not repeated. These are the picture sentences on the pages after that table. Amounts appear only where the sentence prints one.

Printed 52: Lightning is a bolt from the bottom of the screen, also associated with Lightning Crystals. Healing is a flash on the portrait and a chord, and health is restored, with no amount. The Poison Shield sentence of 30 seconds is already in the spell section and is not repeated.

Printed 53: a Summon Imp that is inappropriate asks why it was summoned, then vanishes. Blind temporarily stuns, with no duration. An untitled paragraph, title not recovered, describes a stationary replica of yourself and says it works best with invisibility. That paragraph was not labelled Hologram.

Printed 54: the Mists of Doom body says the apparitions become more numerous as the group level rises. Damage Shield is a blue halo. While it lasts, resistance to physical and marginal attacks is 50%. The duration of that 50% is not printed. "Marginal" was not defined.

Printed 54–58, section "OTHER MAGICAL EFFECTS". A successful attack is a major picture and a blocked attack is a minor picture. No hit-point number is printed for these pictures.

| printed page | picture as read | item or spell the sentence names |
|---|---|---|
| 55 | Fire Fizzle, a puff of flame when a fire spell's major picture is blocked | a fire-oriented spell |
| 55 | Electrical Fizzle, small sparks, when an electrical spell's major picture is blocked | an electrically oriented spell |
| 55 | Stone Wall, a rock slab, otherwise permanent, bashable "for a long while" | a Stone Cube |
| 55 | Ice Wall, a pillar that can be broken and "melts quickly" in heat | an Ice Seed |
| 56 | Storm, a vortex that consumes the opponent or fizzles if the enemy is too powerful | not named as an item |
| 56 | Firestorm, fiery bolts | the Great Sword Firestorm |
| 56 | Rapid-Fire Fireballs, a stream | the Crossbow Noble Valkyrie |
| 56 | Magic Drain, blue spheres, magic levels grow if completely successful | Dark Bow and the Great Sword Darkstorm |
| 57 | Guardian Orb's Sword, a spectral blade | the Guardian Orb |
| 57 | Fiery Explosion, "considerable damage", different sizes | Dark Halls explosive crates, and "numerous devices and spells" |
| 57 | Petrify, a temporary stone statue | the Stone of the Gorgon |
| 57 | Acid, a spray that temporarily reduces protection and causes damage | not named as the Acid Sac |
| 58 | Fireball, a sphere of fire, "potent" | a Fire Crystal |
| 58 | Poison Cloud Trap, randomly emits poisonous vapor | found in the Hive Caves and elsewhere |
| 58 | Health Drain, red spheres | Darkstorm |
| 58 | Plasma Sphere | Rixx's staff and the magic of the Ru-Loi |

The Acid picture's missing percent is not the Acid Sac's printed 25%. Petrify's "temporarily" and the hintbook's "for a while" were not turned into a second count. No prop index was joined to the Hive vapor, the Dark Halls crates, or the swords. Printed 58 then starts the First Sphere hints. Those walkthrough pages were not copied into this table.

## Gear chapter, printed 32–38, 2026-11-05

No Godot was run. BRADY `brady_guide.txt` lines 1187–1443, markers PDF PAGE 33–39 = printed 32–38. No handler was entered. `formula_finished` stays false. OCR headers that are blurred stay out of the name column when the body names the item. Darkstorm's spheres, the Valkyrie fireball, the Dark Bow, the Guardian Orb, the Stone Cube, the Ice Cube, the Fire Crystal, the Lightning Crystal, and the Storm Crystal are already in the picture table and are not repeated.

| printed | item as the body names it | effect as printed |
| --- | --- | --- |
| 32 | Thohan's Sword (header OCR "@QHAnN'S GREAT SWORD") | Negates 50% of non-magical damage, regenerates 1 point per minute, summons a Large Imp below 10% hit points, and a 10% chance of Lightning Storm on each strike. Found broken. Rashar reforges it for a Power Orb. Full potential needs it enchanted. |
| 32 | Halberd Bastion | An iron gate when an enemy is within 10 feet. The gate lowers hit chance and damage. No amounts. |
| 32 | Longbow Defender | 50% chance on a hit to knock the opponent back a few feet. |
| 33 | header OCR "TIET OF EXILE" | One use, then it disappears after banishing the target. The name was not recovered. |
| 33 | Rixx's Plasma Staff | Plasma spheres at missile range. In melee it is only a poor striking stick. It lights torches. |
| 33 | Crossbow Snare | 25% chance to ensnare and stun briefly. |
| 33 | Dagger of Light | In the melee slot it throws daggers of light. |
| 33 | War Blade | From Kityara after the wax impressions, or from her body. Required to enter the Second Sphere. |
| 33 | Longbow Shift | Picks fire, lightning, or a physical blow. It does not fire if the opponent takes none of the three. |
| 34 | Great Bow Shard | Ice shards that shatter into smaller shards. No count. |
| 34 | header OCR "Crossspow InyrisD" | Three bolts, and each bolt that hits releases a Chain Spark. The name was not recovered. |
| 35 | Death Stroke Shield | 50% chance to negate a blow that would have killed the wearer. |
| 35 | Bracers of Valor | Negate the recoil of the War Axe Traitor. |
| 35 | Gauntlets of Might | Increase strength. No amount. |
| 35 | Gargoyle Bracers | Summoning spells cost 25% less magic. |
| 35 | Kieran's Circlet | Protection like a good suit of plate. No other body armor at the same time. |
| 36 | Stone Bracers | Lower armor protection, and immune to all poison. No amount on the armor loss. |
| 36 | Coward's Target Shield | Invisible, with strength and protection at zero. An attack makes the wearer visible for 10 seconds. |
| 36 | Fire Shield | Protects against fire and is extremely susceptible to cold or ice. No amounts. |
| 36 | Reflective Plate Mail | Little physical protection. Reflects spells at half strength. Draws the wearer's own Chain Spark. |
| 36 | Dragonscale Armor | Some protection from Ancient Magic, no amount. With the Dragonfire Bracers the suit burns both sides, and the armor keeps 75% of that flame off the wearer. With the gauntlets as well, the wearer is invulnerable to the flame. |
| 36 | Dragonscale Gauntlets | Protect from 25% of the armor's fire, and some Ancient Magic, no amount. |
| 37 | Dragonfire Bracers | Flame at melee range. Bracers alone: the wearer takes the same damage as the opponent. With the gauntlets: the wearer takes 75%. With the armor: the wearer takes 25%. |
| 37 | Ring of Drakefire | Alone, Spark spells become Fire Spark. With the dragon armor pieces, Fire Spark costs half the magic. |
| 38 | Stroke Dagger | One throw. It becomes a triple-strength lightning bolt. |
| 38 | Ring of Regeneration | Death while worn regenerates the wearer once. The ring then disintegrates. |
| 38 | Dragon Gem | An amulet. Some protection from physical attack. No amount. |
| 38 | Colim's Amulet | Limited protection from hostile magic, especially a magic drain. No amount. |

The armor page and the bracer page agree that armor plus bracers leaves the wearer taking 25% of the flame. They do not agree once the gauntlets are added: the armor page says invulnerable, and the gauntlet page says 25% of the armor's fire. Those two sentences stay unmerged. The bracer page's 75% is the gauntlets without naming the armor. It is not the three-piece case.

HINTBOOK lines 2405–2408: the Power Orb buys the Great Sword Firestorm, or it pays to repair the broken museum sword. Lines 5682–5689: killing Kelsrick also yields the sword the armorer sells for the orb, and the repaired sword as the darksword is called the best weapon only as a rumor. Those sentences do not carry the 50%, the 1 point per minute, or the 10% storm. They stay out of the Brady column.

## Melee weapons, printed 30–31, 2026-11-05

No Godot was run. No handler was entered. `formula_finished` stays false. BRADY `brady_guide.txt` lines 1113–1185, markers PDF PAGE 31–32 = printed 30–31. Printed 29 is the chapter title only (OCR "Weapons, Soot, ae Geur") and adds no effect row. The printed-32 row for Thohan's Sword is already in the gear section and is not repeated. The footer "36." on the prism page is a page number, not a chance.

| printed | item as the body names it | effect as printed |
| --- | --- | --- |
| 30 | Axe of the Long Arm (header OCR "AXE OF THE Lonc Arm") | Returns when thrown. Melee and ranged. The range slot must be empty to throw it. |
| 30 | Long Sword Prism (header OCR "Lonc SworpD Prism") | 25% chance to blind indoors, 75% outdoors. The sentence says it is especially effective against Phantom Dracoids and Dark Halls specters. |
| 31 | Great Sword Firestorm (header OCR "GREAT SWORD FiRESTORIn") | 50% chance of a storm of fire. Empowered at the Shrine of the Ancients, it becomes Darkstorm. |
| 31 | Gauntlets of Striking | More damage than a bare-handed blow. No amount. 50% chance to stun. |
| 31 | War Axe Traitor | A great deal of damage. No amount. The wearer takes that same damage unless the Bracers of Valor are worn. |
| 31 | Dracoid Ornamental Dagger | Saps an opponent's magic if that opponent is trying to cast. |
| 31 | Reaver of the Great Orc | Found in the Executioner's Cave. The wearer cannot use it without a Champion Stone, and drops it when the stone wears off. |
| 31 | Great Axe Blizzard | 25% chance to freeze on a hit. The freeze is a short time. A follow-up blow shatters that enemy. |

The Champion Stone's +20 strength for 1 minute is already in the first item table. It is not repeated. The index lists Reaver of the Great Orc on printed 31 and 43. The printed-43 body still reads OCR "Reamer of Great Orc" and was left under that spelling in the earlier section.

HINTBOOK lines for the same eight names stay in this paragraph. Lines 1299–1303: the Axe of the Long Arm returns after a throw and is called only marginally useful. Line 2317: that axe can clear the shrine's stone spikes. Lines 1493–1496: the Long Sword Prism is the first strong sword and is left behind in the Huline Jungle. No 25% and no 75%. Lines 1436–1438: the nice Huline route gains the Great Sword Firestorm. No 50%, and no shrine. Lines 1431–1433 and 5159–5160: the Great Axe Blizzard comes from the Claw lake, deals cold, and freezes fountains. No 25% and no shatter. Lines 1561–1566: the Reaver is too large; Gauntlets of Might may let Luther use it, and a champion's stone is only a rumor. Lines 1321–1323: the Bracers of Valor may be what lets Luther use the Reaver, and otherwise do little. Brady's valor row, already filed, negates the Traitor axe's recoil and does not name the Reaver. The hintbook valor sentence and the Brady traitor sentence stay unmerged. Hintbook has no sentence for the Gauntlets of Striking or the Dracoid Ornamental Dagger. Line 2106 names a rainbow sword beside the Axe of the Long Arm. That rainbow sword is not called the Long Sword Prism. Lines 1364–1368 name a Dark Sword made on the dreamstone altar. That name is not the printed-31 Darkstorm.

## Hintbook tool lines that disagree, 2026-11-05

No Godot was run. No handler was entered. `formula_finished` stays false. These are HINTBOOK `hintbook.txt` lines 1294–1670, the tools list. A Brady row already filed is named only so the two sentences stay apart. Nothing in that earlier row was rewritten. Items whose hintbook line has no amount and no different mechanic are left out.

| lines | name as read | hintbook sentence | filed Brady sentence it is not merged with |
| --- | --- | --- | --- |
| 1294–1296 | Ancients' Stone | Right-click on the spell circle. One level-five ancient spell. No charge count. | Printed 49: right-click over the portrait, up to nine charges. The nine stays on that page. |
| 1306–1309 | Bezoar rings | Protection, and not worth the spots they use. No poison named. | Printed 39: lesser poison, and greater poison, on the two rings. |
| 1314–1317 | Bracers of the Dead | Key to the cemetery quests. Found near the top of the mage's tower. | No effect row in the filed Brady chapters. |
| 1335–1338 | Colim's Amulet | No change to Luther's statistics. | Printed 38: limited protection from hostile magic, especially a magic drain. |
| 1341–1343 | Coward's shield (OCR "CowARD's Buusryt") | Wearing it makes Luther invisible. | Printed 36: also strength and protection at zero, and an attack shows the wearer for 10 seconds. |
| 1348–1353 | Crossbow Multiplex | Three spark spells that bounce. It cannot fire again until those sparks end. | Printed 34, name not recovered: three bolts, and each hit releases a Chain Spark. |
| 1356–1361 | Dagger of the Empty Hand | About one third as powerful as the Dark Sword. The same sentence then says that allows roughly four times as many attacks, and that a greater net attack is only possible. Found only after the Huline Temple. | No effect row in the filed Brady chapters. |
| 1364–1368 | Dark Sword | Place a sword on the dreamstone altar before taking the stone. | Printed 31 names Darkstorm, not this altar. |
| 1382–1387 | Dragon's Blood | Not a potion. Right-click, then throw or place it. It explodes soon. Keep one for the cemetery. | No effect row in the filed Brady chapters. |
| 1390–1393 | Dragon Gem | Adds to might. No amount. | Printed 38: some protection from physical attack. No amount there either. |
| 1411–1413 | Gargoyle Bracers | The Huline armorer's gift. They help protect him. No amount. | Printed 35: summoning spells cost 25% less magic. |
| 1448–1452 | Ice seeds | Raise icy spikes. They can freeze a fountain. | Printed 55: an Ice Seed raises an ice pillar that breaks, and melts quickly in heat. |
| 1457–1461 | Cat's-eye ring, header not recovered | Found in the Hive. It speeds the attack rate. No amount. | Not joined to printed 40 OCR "KELEn's RinG" (tiger claws and a snarl). |
| 1470–1476 | Kieran's Circlet | Harder for an enemy to hit from behind, or no bonus for that hit. | Printed 35: protection like plate, and no other body armor at the same time. |
| 1499–1501 | Longbow Defender | Shoots two arrows. | Printed 32: 50% chance to knock the opponent back. |
| 1503–1507 | Longbow Shift | Sometimes a line of electricity, sometimes a fizzle. | Printed 33: the wielder picks fire, lightning, or a physical blow. |
| 1535–1536 | Net of Exile | Makes creatures go away. Called marginal. | Printed 33, name not recovered: one use, then it banishes and disappears. |
| 1569–1574 | Ring of Regeneration | Heals faster than usual, and spends itself on a fatal hit. | Printed 38: one regeneration at death, then the ring disintegrates. The faster heal is only in the hintbook. |
| 1626–1629 | Stone Cube | Thrown, it grows stalagmites. | Printed 55: a Stone Cube raises a rock slab. |
| 1636–1639 | Storm Crystal | A mega-snowstorm. | Printed 56: a Storm vortex. The crystal is not named on that picture row. |
| 1644–1649 | Stroke Dagger | A lightning stroke. Holding them makes Luther tougher, and the daggers matter less. | Printed 38: one throw, and it becomes a triple-strength lightning bolt. |
| 1656–1659 | Valkyrie Crossbow | Shoots a fireball. | Printed 56 names the Crossbow Noble Valkyrie and a stream of fireballs. |
| 1662–1664 | Vel's Fruit | A rumor that it cures poison. | Printed 40: negate the effects of any poison. |
| 1668–1670 | War Blade | Daniel's gift from his mother. Give it to him. | Printed 33: from Kityara after the wax, or from her body, and required for the Second Sphere. |

Lines 1531–1532 say the silver mail should be swapped for platemail. Lines 1539–1540 call the Obsidian Chainmail the best armor and hide it in the Claw Mountains. Lines 1548–1549 put the platemail breastplate in the executioner's nest. No percent is printed on those lines. Brady line 2477 says a suit of chain mail and a fine long sword only go so far. That sentence was not given a percent either. Printed 50 says the Mists fifth level, Lich, turns Luther into an invulnerable undead lich for a few moments. No count. The fifth-level names already in the spell table are not repeated.
