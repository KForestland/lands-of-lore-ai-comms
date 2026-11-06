# AE14 map gaps

Base maps-y 4a32849. Updated by AG05. Godot was not run. Map.png was not regenerated. No new game patch was written. Former (c) rows are now SEEN+HOSTED or NOT SEEN from the longplay frames. No SEEN+MISSING row remains, so none stays open for a patch.

| gap | class | host or patch | test |
| --- | --- | --- | --- |
| L1 Fire Pit giant | (a) | Actor 44, definition 4, health 10. Unapplied AE01, order 862. | `cave_firepit_roach_state_test` |
| L1 south-exit death and tunnel roach | (a) | Hosted in AD. | AD01 |
| L3 speaking stone | (a) | Movable 55 stays 68-SS1. | AD02 |
| L4 waterfall crystal | NOT SEEN as that item | `f_00617` at 51:20 shows two white-and-yellow piles. They were not joined to the lightning identity. Water Button c97 stays its own marker. Shop rows 22 and 23 stay the shop pile. | none |
| L4 burrow SS3 | (a) | Item 72 stays 136-SS3. | AD03 |
| L5 Shalla | (b) | Unapplied AE03, control 75. Actor 20 stays Dawn. Groups stay unrun. | `hive_shalla_state_test` order 864 |
| L5 entrance and lizard tunnel | (a) | Hosted in AD. | AD04 |
| L7 iron door motion | NOT SEEN | Place stays control 84. The sampled halls stills do not show the door move. | none |
| L7 prism scroll | (a) | Hosted in AD. SS6 stays 139-SS6. | AD05 |
| L8 Tuani Hut | NOT SEEN under that name | `g_00012` at 1:55:10 is a hut interior. The name was not on screen. No marker. | none |
| L8 Crystal Shard | (a) | Definition 105, name 103-Cry shard. Host `l8_tree_slot_state.gd`. The approach point is a modern proxy. | `l8_tree_room_earned_test.gd` |
| L8 Scroll, Dagger of the Open Hand, Lizard Seal | NOT SEEN | No catalog row. No opened frame shows them. | none |
| L8 Dampen Charm | (a) | Catalog 70-Dampen ch. Editor marker Cat/Dampen stays. | none for an L8 row |
| L8 War Blade | NOT SEEN | Excluded row 50 has no name. No opened frame names the blade. | none |
| L8 Dracoid Sigil | (a) | Key `l8:shaman:Dracoid_sigil`, definition 102. No coordinate. | `l8_journey_state_test.gd` |
| L8 clubhouse and tree | (a) | Actor 21 stays WILD. Control 114 stays the tree. | `l8_clubhouse_earned_test.gd`, `l8_tree_bridge_test.gd` |
| L9 Dracoid Hotel | NOT SEEN | No script string. No hotel front on the opened frames. | none |
| L9 priest path, stairs, force field, basement inset | NOT SEEN | No object under those names. | none |
| L9 Gorgonite Nodules | NOT SEEN | `g_00035` shows crates. No L9 row. SSAR stays SSAR. | none |
| L9 wooden platform and grate | (a) | Raft control 82. Marker added. | `l9_flood_escape_earned_test.gd` |
| L9 left bowl and flood table | (a) | Prop 2622 and control 122. | `l9_statue_earned_test.gd`, `l9_flood_escape_earned_test.gd` |
| L10 book places in the AE06 table | (a) | Marked in AE06. | the hosts named in AE06 |
| L12 Ice Seeds | NOT SEEN | `g_00180` is an ice corridor. Catalog 62-ice seed has no row. Stalagtite has no click host. | none |
| L12 Dreamstone | (a) | Carried id `act2:L13_RC:dreamstone`. | `l12_crevasse_earned_test.gd` |
| L12 ice rafts, chain row, Kenneth | (a) | Marked in AE07. | the hosts named in AE07 |
| L13 Slave Caverns | NOT SEEN | No region of that name. | none |
| L13 second teleporter | NOT SEEN as a second record | `g_00216` shows one green barred opening. Control 104 stays the only teleporter. | `l13_return_pad_earned_test.gd` |
| L13 maiden switch | (a) | Screen button in `l13_prison.gd`. Entry is Front Door c52. | `l13_prison_refusal_earned_test.gd` |
| L13 Tar Crystals, Silverleaf, Aloe | NOT SEEN on L13 | No L13 row. | none |
| L13 Plasma Steps, Iris 2, Iris 3 | (a) | Plasma platform and Web 1 stay their own names. | `l13_pink_steps_earned_test.gd`, `l13_eggs_earned_test.gd` |
| L13 Ru-Loi count | SEEN+HOSTED | `g_00187` reads Remaining Ruloi 19/19. `all_ruloi_dead()` stays. The 20-name list stays. No actor was removed. | `l13_lower_ruloi_earned_test.gd` |
| L13 basin, brain, Hive Lord, Mandrake, Venom sac | (a) | Marked in AE08. | the hosts named in AE08 |
| L14 Venom Sacs | NOT SEEN on L14 | The rows are on L13. | none |
| L14 Death God | NOT SEEN | `g_00249` is a cauldron. `g_00275` is the sun-trimmed door. | none |
| L14 Bowl | (a) | Bowls p369 and p370. | `l14_priest_ritual_earned_test.gd` |
| L14 Bowl 1 and Bowl 2 | NOT SEEN | Directions stay unread. | none |
| L14 Oil Puddle and Oil pit | (a) | Covers m77 and m78. | `l14_flute_slot_earned_test.gd` |
| L14 Chalice | (a) | Frame rect in `l14_chamber_voices.gd`. No world pin. | `l14_chamber_voices_earned_test.gd` |
| L14 priest, bowls, shard, flute, idols, printed 201 rows | (a) | Marked in AE09. | the hosts named in AE09 |
| L16 Dark Bow | (a) | Excluded row 24, name 36-Darkbow. Marker added. | `l16_item_test.gd` |
| L16 yellow figure, northwest list, oil spark, silverleaf room, tower figure, mantle, live dragon | NOT SEEN as those actions | `g_00328` has the pyramid and no figure on it. `g_00351` is a many-limbed creature and was not measured onto a placement. | none |
| L16 elevator, hourglass, scarab, canal word | (a) | Marked in AE10. Cannal has no placement. | the hosts named in AE10 |
| L17 Hive Mother | SEEN+HOSTED | `g_00382` shows the tendril mass after Dawn. The cast host stays X01 at Frank's Placenta prop 242. The picture was not measured onto that prop. | `l19_dawn_curse_test` order 812 |
| L17 columns, valve, organ | NOT SEEN as three objects | `g_00362` is a fleshy ring. Gut templates keep their names. | none |
| L17 exit quads | (a) | Regions 1312 and 1313. No single point. | none |
| L17 begin, return, crystals, creatures | (a) | Marked in AE11. | `l17_creature_test.gd` |
| L19 Ruby of Truth | (a) | Definition 69 on Dawn good p78. The grant stays LIKELY. | X01 does not grant it |
| L19 lizard path and the other room names | NOT SEEN as those words | The green hall and the golden doors are on screen. SEWER stays SEWER. Golden Door stays control 137. | `l19_creature_test.gd` |
| L19 BELSTAT | (a) | Actor 32. Baccata stays off the label. | `l19_creature_test.gd` |
| L20 first and second empowerment chambers | SEEN+HOSTED as rooms | `g_00371`, `g_00378`, and `g_00384` are three green rooms. No frame prints a chamber number. | none |
| L20 Expel Curse Here | (b) | X01 cast at Frank's Placenta p242. No curse command is stored. | `l19_dawn_curse_test` order 812 |
| L20 blue pillars, blue orbs, moving platforms | NOT SEEN | `g_00367` is a green pillar row. `g_00383` is a still railed corridor. X02 leaves blue at -1. | `l20_pillars_scotia_test` order 814 |
| L20 Ruby of Truth | (a) | No L20 row. The record is L19 definition 69. | `l20_item_test.gd` |
| L20 womb, third chamber, final battle, Scotia, faux-Draracle, armor rows | (a) | Existing markers. Actor 47 stays unmarked. | the hosts named in AE13 |

Open SEEN+MISSING rows: none.

Marker counts stay L1 38, L3 26, L4 42, L5 16, L7 15, L8 34, L9 54, L10 62, L12 56, L13 48, L14 45, L16 29, L17 9, L19 22, L20 24.
