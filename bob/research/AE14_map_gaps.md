# AE14 map gaps

Base maps-y 4a32849. Godot was not run. Map.png was not regenerated. AE01 and AE03 are unapplied patches. AE02 has no item row, so it has no patch. AE04 through AE13 added markers only. No live game tree was edited.

| gap | really missing? | host or patch | test |
| --- | --- | --- | --- |
| L1 Fire Pit giant | separate giant, yes | Actor 44 is definition 4, health 10, at (−155, 14685) h −265. Marker added. Unapplied `cave_firepit_roach_state_test`, order 862. | `grok_research/patches/AE01_firepit_roach/` |
| L1 south-exit death and tunnel roach | no | Hosted in AD. Controls and actor 0 stay those records. | AD01 |
| L3 speaking stone | no | Hosted in AD. Movable 55 stays 68-SS1. | AD02 |
| L4 waterfall crystal | yes | No item row. Shop rows 22 and 23 stay the shop pile. Water Button is control 97. No patch. No marker. | none |
| L4 burrow SS3 | no | Hosted in AD. Item 72 stays 136-SS3. | AD03 |
| L5 Shalla | placement no, spawn yes | Control 75, template 6, native (−1133, 8885) h −235, flags 0x5402. Marker added. Actor 20 stays Dawn. Unapplied `hive_shalla_state_test`, order 864. Groups stay unrun. | `grok_research/patches/AE03_shalla/` |
| L5 entrance and lizard tunnel | no | Hosted in AD. | AD04 |
| L7 iron door motion | motion yes | Place is control 84. Motion stays the 2026-10-21 deviation. No new patch. | none |
| L7 prism scroll | no | Hosted in AD. SS6 stays 139-SS6. | AD05 |
| L8 Tuani Hut | yes | No script string. No marker. | none |
| L8 Crystal Shard, Scroll, Dagger, Lizard Seal | yes on L8 | No L8 item row under those names. The tree host takes `act2:L14_HT:post_shard`. | `l8_tree_room_earned_test.gd` for the shard take |
| L8 Dampen Charm | yes on L8 | Monastery slot `70-Dampen ch`. The editor marker Cat/Dampen stays. | none for an L8 charm row |
| L8 War Blade | name yes | Excluded dormant row 50 is native (−1465, 2708) h 230. The record has no name. | none |
| L8 Dracoid Sigil | place yes | Key `l8:shaman:Dracoid_sigil`, definition 102. No placed coordinate. | `l8_journey_state_test.gd` |
| L8 clubhouse and tree | no | Actor 21 stays definition 1 name WILD. Control 114 is the tree. Markers added. | `l8_clubhouse_earned_test.gd`, `l8_tree_bridge_test.gd` |
| L9 Dracoid Hotel | yes | No script string uses hotel. | none |
| L9 priest path, stairs, force field, basement inset | yes as those names | The pyre marker, the green-orb marker, and Gauntlets row 53 stay their own records. | none for those names |
| L9 Gorgonite Nodules | yes on L9 | No L9 item row uses that name. | none |
| L9 wooden platform and grate | name yes | Control 82, template 123. The host name is raft. | `l9_flood_escape_earned_test.gd` |
| L9 left bowl and flood table | no | Prop 2622 and control 122. Markers added. | `l9_statue_earned_test.gd`, `l9_flood_escape_earned_test.gd` |
| L10 book places in the AE06 table | no | Markers added for the railings, Holy Switch c66, Dragangel c150, the bone braziers, Beozar ring row 33, and Ancients stn rows 37–39. Greater Bezoar’s Ring stays the Claw slot. | the hosts named in AE06 |
| L10 Freeman's gate | no | Control 67 has no Brady number. No new marker. | none |
| L12 Ice Seeds | yes | No L12 item row. Stalagtite has no click host. | none |
| L12 Dreamstone | no L12 row | The carried id is `act2:L13_RC:dreamstone`. | `l12_crevasse_earned_test.gd` |
| L12 ice rafts, chain row, Kenneth | no | Markers added. Row 5 stays `55-Obs chain`. Greater Bezoar’s Ring stays off row 4. | the hosts named in AE07 |
| L13 Slave Caverns, second teleporter, maiden switch, citadel herbs | yes | No world coordinate for the switch. No patch. | none, or the prison screen test for the button |
| L13 Plasma Steps, Iris 2, Iris 3 | name yes | The plasma platform and Web 1 stay their own names. | `l13_pink_steps_earned_test.gd`, `l13_eggs_earned_test.gd` |
| L13 Ru-Loi count | count open | The active list has 20 actors named RULOI. No patch. | `l13_lower_ruloi_earned_test.gd` |
| L13 basin, brain, Hive Lord, Mandrake, Venom sac | no | Markers added. Darkstorm, Dark Sword, and Thohan's Enchanted Sword stay award names. | the hosts named in AE08 |
| L14 Venom Sacs, Death God, Bowl names | yes | No placement under those names. | none |
| L14 Oil Puddle and Oil pit | name yes | The two covers stay marked. Those templates have no placement. | `l14_flute_slot_earned_test.gd` |
| L14 Chalice | world object yes | `l14_chamber_voices.gd` uses a frame rect. No world coordinate. | `l14_chamber_voices_earned_test.gd` |
| L14 priest, bowls, shard, flute, idols, printed 201 rows | no | Markers added. The post shard catalog point is (3043, 5684) h 30. Control 71 at that plan point has height 0. Item 67 stays (2691, 3887) h −70. | the hosts named in AE09 |
| L16 yellow figure, northwest objects, oil spark, Dark Bow, silverleaf room, tower figure, mantle, live dragon | yes | Props that exist keep their own names. Prop 602 stays the NE greenhouse Ball O Smoke. Prop 210 is the southern dry fountain orb. No patch. | none for those book objects |
| L16 elevator, hourglass, scarab, canal word | no | Markers added for the plate, prop 210, the hourglass, and the scarab row. Watergate c123 stays Watergate. Cannal has no placement. | the hosts named in AE10 |
| L17 Hive Mother, fleshy columns, valve, organ | yes | Wide guts and Hive Duct keep those names. No patch. | none |
| L17 exit quads | place no | Regions 1312 and 1313 read as level 19 selector 1. No single stored point. | none |
| L17 begin, return, crystals, creatures | no | Teleport circle m50 was added. HIVEW and HIVEGRD stay the population names. L5 places stay off this map. | `l17_creature_test.gd`, `act2_exit_blockers_test.gd` |
| L19 Ruby of Truth | yes | No row under L19_BC. | `l19_item_test.gd` |
| L19 lizard path and the other room names | yes as those names | SEWER stays SEWER. No patch. | `l19_creature_test.gd` |
| L19 BELSTAT | no | Actor 32, marker added. Baccata and the Statue of Belial stay off the label. | `l19_creature_test.gd` |
| L20 first and second empowerment chambers | yes | No template of those names. Scotia's homes stay their own name. | `l20_creature_test.gd` for the homes |
| L20 Ruby of Truth, blue pillars, blue orbs, moving platforms, Expel Curse Here | yes | No row and no script host under those words. | `l20_item_test.gd` for the ruby search |
| L20 womb, third chamber, final battle, Scotia, faux-Draracle, armor rows | no | Existing markers. Actor 47 DRAR_PH stays unmarked. Dragonscale Armor stays off the armor rows. | the hosts named in AE13 |

Marker counts: L1 38, L3 26, L4 41, L5 16, L7 15, L8 34, L9 53, L10 62, L12 56, L13 48, L14 45, L16 28, L17 9, L19 22, L20 24.
