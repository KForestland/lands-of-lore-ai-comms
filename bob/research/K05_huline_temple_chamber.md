# K05 Huline Temple through the Chamber of Voices

No Godot was run. Newest owner file is still `TRIAGE_20261104.md`. HINTBOOK chapter 12, lines 4566–4641, is the fire paths, the flute, the boulder, the three pedestals, the hoppers, the faux-Belial, and the chalice. BRADY printed 203, file marker PDF PAGE 204, lines 8224–8260, is the "to complete this level" list, and printed 214 step 81 is the front door. The door itself is K04. No `l14` script is in `my_journal.gd`.

The earned tests below all print PASS for a real walk and a save. Verdict for each row is HOSTED+TESTED. Rendered presentation is not claimed.

| step | guide | host | earned test |
| --- | --- | --- | --- |
| Main doors, stone kept | BRADY step 81 | `l14_temple_doors.gd`, movables 92 and 93, slot `temple:entrance1198`, definition 136 | `l14_temple_entry_earned_test.gd` |
| Body, aloe, poison, lightning | BRADY lines 8240–8242 | `l14_priest_body.gd`, `l14_priest_ritual.gd` | `l14_priest_slab`, `l14_priest_supplies`, `l14_priest_ritual` |
| Healing-pool shard | BRADY line 8243 | the post-shard pickup | `l14_post_shard_earned_test.gd` |
| Machines and the statuette | BRADY lines 8244–8246 | `l14_machines.gd` | `l14_machines_earned_test.gd` |
| Library button, then the niche | BRADY lines 8250–8251 | `l14_library.gd`, `l14_niche.gd` | `l14_library`, `l14_library_exit`, `l14_niche_approach`, `l14_niche` (shard 67) |
| Two shards in the scale bowls | BRADY line 8252 | `l14_shard_bowls.gd`, trays 405 and 406 | `l14_shard_bowls_approach`, `l14_shard_bowls` |
| Dreamstone raises the spiral | BRADY line 8253 | `l14_spiral.gd`, slot 72, stone retrieved | `l14_spiral_earned_test.gd` |
| Three paths, three idols | HINTBOOK 4566–4572; BRADY lines 8254–8255 | `l14_ledge_maze.gd`, `l14_tilt.gd`, `l14_fire_paths.gd`, `l14_idol_pedestals.gd` | `l14_ledge_maze` (idol 371), `l14_tilt` (idol 372), `l14_fire_paths` (idol 384), `l14_idol_pedestals` (fourteen stairs) |
| Boulder kept to the side | HINTBOOK 4586–4589; BRADY line 8256 | the boulder walk | `l14_boulder_side_earned_test.gd` |
| Flute, oil, blade bypass | HINTBOOK 4576–4585 | `l14_flute.gd`, `l14_flute_slot.gd` | `l14_flute` (flute 77), `l14_flute_slot`, `l14_flute_approach`, `l14_blade_bypass` |
| Five hoppers, then the platform | HINTBOOK 4600–4609 | `l14_hopper_platform.gd` | `l14_hopper_room`, `l14_hopper_corpses`, `l14_hopper_platform` |
| Faux-Belial, Beast form | HINTBOOK 4616–4631. The citadel fight stays a different Belial. | `l14_belial.gd`, actor in the chamber test is 90 | `l14_belial_entry`, `l14_belial_combat` (Beast melee) |
| Chamber of Voices | HINTBOOK 4636–4641: put the dreamstone in the chalice; it is destroyed; the city resurfaces. BRADY lines 8214–8221 and 8259–8260. | `l14_chamber_voices.gd` | `l14_chamber_voices_earned_test.gd` |

The chamber host is the lead's STORY-066. Doors are `Vector3(688, 40, 10873)` and `Vector3(638, 40, 10752)`. E opens them after Belial, actor 90, is dead. The script says the native door predicate 207 writer was not traced. The chalice hotspot is rect (194, 88, 202, 130) on the 640×400 frame. The offered item is `act2:L13_RC:dreamstone`. The click consumes it. The script comment names opcode 2 arm 0x1C on prop 170, group 9210, and native L16 arrival 1. Byte 5 of that arm stays unread. The earned test is what checks the arrival.

Side earned tests, not the minimum list: hanging 124, spider HIVEW 68, bedroom crack, the return walks (`l14_fire_return`, `l14_ledge_return`, `l14_tilt_return`, `l14_belial_exit`, `l14_shard_return`). Same verdict.

## Journal

A player stuck at the bowls, the boulder, the hoppers, or the chalice gets no My Journal line. Verdict: MISSING. Fix: `discover` from `l14_priest_ritual.gd` when the body is on the slab and a bowl is empty, from the boulder host when the centre strip kills, and from `l14_chamber_voices.gd` when the doors are open and the stone is still carried. Wording is the K09 list.

## Still open

Predicate 207's writer. Byte 5 of the level change. The journal lines.
