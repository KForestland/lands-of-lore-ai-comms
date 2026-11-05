# K09 Journal hints for the required steps

No Godot was run. Newest owner file is still `TRIAGE_20261104.md`. `my_journal.gd` loads notes only from the Act 1 planners plus `l8_larkhon_state.gd` and `l8_tree.gd`. A note appears only after `discover()`. No `l9`, `l10`, `l12`, `l13`, `l14`, or `l16` script is a source.

## Already written

Do not add these again. They are the Larkhon set, and they match the earned stage, including the owner's save:

| id | when it shows | characters |
| --- | --- | --- |
| `larkhon_join_tribe` | not a member of the tribe | 121 |
| `larkhon_ask_shaman` | a member, trade not done | 117 |
| `larkhon_serum_needs_leaf` | carrying def 119, not mixed | 94 |
| `larkhon_vapors_unactivated` | mixed, not yet used | 84 |
| `larkhon_must_sleep` | the other cases | 109 |

`tree_torches_unlit` is the great-tree side quest. It is not a required step of this chain. The radius on the Larkhon notes is still 600 around actor 115. Outside that radius even these five stay hidden.

## Missing, with a Luther line

Each line is at most 130 characters. The count is the hint alone. None of these has a `discover()` yet. The finale lines are HINTBOOK proposals for hosts that do not exist. They follow the hintbook, not Brady's other route.

| stuck | discover from | characters | line |
| --- | --- | --- | --- |
| Blade not in Daniel's hands | `l8_journey.gd` while the gift is unoffered or dropped | 108 | Daniel asked for his grandfather's blade. If the gift failed, the knife is still on the ground where we met. |
| Temple not seen | the same host, before `visit_temple` | 105 | The village will not open until I have seen the temple east of the road, and I must carry Daniel's blade. |
| Guard has not seen the blade | the same host, temple seen, not admitted | 94 | I have seen the temple. The guard at the great tree wants Daniel's blade before he lets me in. |
| No cemetery mark | the same host, admitted, key not taken | 97 | The shaman keeps the mark for the cemetery gate. He trades it only after the guard has let me in. |
| Oil will not light | `l10_oil.gd` when a close or weak spark fails | 109 | The tomb oil will not take a weak spark up close. A stronger spark, or dragon's blood, needs a safe distance. |
| Emperor's door shut | `l10_priest.gd` while urn, ashes, or ankh is missing | 92 | The priest's urn, the chapel ashes, and the ankh are what the Emperor's door is waiting for. |
| Statue will not keep the player | `l9_statue.gd` when the form is not human | 97 | The walking statue keeps me only if I follow as a man. The dampen spell is what holds that shape. |
| Late for the flood | `l9_flood.gd` on the drown branch | 118 | If I am late for the lifting table, the water wins and I must try the bowl again. At the end I can stand on the grate. |
| Trees stay dead | `l10_silverleaf.gd` while the bracers are carried | 107 | Dawn on the river wants the bracers from the ruins. While I still carry them, the cemetery trees stay dead. |
| Not initiated | `l8_tribe_state.gd` before the bout | 111 | The tribe's fight, and a silver leaf still in my pack, are what the shaman asks before he calls me one of them. |
| Citadel still sealed | `l13_egg_door.gd` before the globe | 112 | Something in the citadel is still sealed. A charged globe, then the upper halls, stand between me and the stone. |
| Dreamstone not taken, or left in a slot | `l13_exit_lock.gd` and `l8_temple_door_state.gd` | 106 | The Dreamstone is past the Hive Lord. Dawn's lock and the temple door both take it, and both give it back. |
| Scale bowls empty | `l14_shard_bowls.gd` with a shard still carried | 100 | The scale in the temple wants both crystal shards, one in each bowl, before the way behind it opens. |
| Boulder centre | the boulder host when the centre strip kills | 87 | The boulder in the centre of that hall kills. The safe way is the strip along the side. |
| Platform will not rise | `l14_hopper_platform.gd` with fewer than five bodies | 94 | Five hopper bodies belong on the wooden platform. My own weight is not enough to make it rise. |
| Chalice not used | `l14_chamber_voices.gd` while the doors are open and the stone is carried | 94 | The Chamber of Voices takes the Dreamstone into the chalice, and the stone does not come back. |
| Dry fountain | a new host on prop 210, not the detached fountain node | 104 | A ball hangs over the dry fountain at the south end of the city. If I break it, the water should return. |
| Hourglass only chimes | `l16_greenhouse.gd` when no leaf is placed | 74 | If the hourglass only chimes, the glass pyramid still wants a silver leaf. |
| One tower open, the rest missing | after the greenhouse doors open | 100 | One tower is open. The other three, and a box that fits a disk, are still between me and the centre. |
| Caverns, no host yet | STORY-079, when that host exists | 107 | Past the mantle, the caverns run toward a west wall of red strands. Cutting them is the way into the beast. |
| Baccata dying, no host yet | STORY-081 | 105 | Baccata is in the laboratory, and he will not last. Belial's horn has to come from him before he is gone. |
| Bars and guck, no host yet | STORY-082 | 119 | A man's hands break the bars. Only the lizard fits the gutter. Three switches across the guck raise it enough to cross. |
| Heads, no host yet | STORY-085 | 111 | Four ghostly heads share one room. A weak mist of doom on each calls something I must drag to the white circle. |
| Dawn's curse, no host yet | STORY-086 | 83 | Dawn says the curse goes into the mother, not into Belial while he is still unborn. |

The yellow figure is not given a line. K06 left it unrequired until the left-type-4 predicate is read, and a note that demanded it would fight the hosted hourglass.
