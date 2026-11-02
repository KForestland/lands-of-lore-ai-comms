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
