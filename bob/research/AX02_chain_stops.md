# AX02 — chain-stopping Act 3 triggers

No trigger patch. None of the STORY-066 through STORY-093 rows is a walk-in the original starts by entering a place while the draft waits on E and the next required step never arms.

One earned-test aim is fixed so the door walk can be saved. `l16_ne_tower_earned_test.gd` placed Luther on the door's own x and z and called `look_at` on that door point, which sits 8 units straight above. The camera pitch became `-PI/2`. `jungle_save.gd` rejects a pitch outside −1.4..1.4 with "Invalid player view." The door flag was already set before that aim. The test now looks 40 units off that vertical. The walk still does not press E. The player script is unchanged.

The required travel joins are already region crossings:

- Region 233 starts the arrival elevator. `l16_arrival_elevator.gd` does not read KEY_E except to skip the movie.
- Region 1312, predicate null, requests L19 arrival 1. `l17_cavern_run.gd` does not cancel `enter_region`. The cut flag in `l17_beast_blade.gd` is not read by that trip.
- Region 2369 predicate 204 requests L20 arrival 1 when index 52 is 0. The existing `L19_to_L20_pred204_205` arrival adapter writes that 0 for selector 1. `adapter_exit_seeds` defaults true on the map. The curse clicks are not that gate. No second writer is added. The native writer of index 52 stays the framed L20 group 7704, which is not this arrival.

Rows that were the open candidates, and why they stay:

- STORY-078 control 74. Kind 5, group 42056, raw `020100001c31`, destination L17 arrival 1. The owner is `control:74`, not a region. `use_exit` supplies the caller bytes and does not change the predicate. The dragon module chops on left click, sets `pad_seen` on the pad, and does not consume KEY_E, so the host E still reaches the control. The caller is UNKNOWN. Converting this into a walk-on would invent a trigger the record does not store.
- STORY-092 and STORY-093. The book says attack with one of three weapons. No L20 opcode binds those weapons. The draft stores the flag on E at actor 75. The level change into that room is region 2369, which does not read the flag, and nothing after the flag reads it. The same E placeholder is used for the armory hack, the faux-Draracle strike, and the pillar shot. Those are hotspots, not region entries.
- STORY-086. Keep-clicking Dawn is a dialog. The port's use key is E. The trip out of the laboratory is the region above, not the click.
- STORY-066. Kind-4 doors and the chalice click match the book. The chamber script writes local 22 before prop 170.
- STORY-082. Standing in the right form sets the switches, which is easier than the book's shot. It does not lock a later region.
- STORY-088. `path_open` is forced false and the script adds no collision.

The greenhouse hourglass and the northeast door are a real order, and they match the book: the hourglass is a use, and the door flag is a walk with no E. The centre bars are a walk once that door flag is set. The four tower raises, the mantle grant, the beast movie, and the last video stay unhosted. They are gaps, not an E on a decoded region entry.

## Tests

Headless module tests on the detached `381b841` scratch, with AH02, AR01, and AR02 applied and not committed, printed PASS:

- `l16_ne_tower_test`, `l16_se_oil_test`, `l16_nw_traps_test`, `l16_sw_chips_test`, `l16_centre_tower_test`, `l16_dragon_room_test`
- `l17_cavern_run_test`, `l17_beast_blade_test`, `l19_beast_wall_test`, `l19_belial_horn_test`, `l19_sewer_forms_test`, `l19_drain_path_test`, `l19_ghostly_heads_test`, `l19_dawn_curse_test`
- `l20_pillars_scotia_test`, `l20_armory_test`, `l20_faux_draracle_test`, `l20_finale_test`
- `act3_journal_hints_test`, `l16_dry_fountain_test`

No player script changed. The diff is `patches/AX_fixes/AX02_ne_tower_view.diff`. It applies on the end of AH02 plus AR01 and AR02, including on live `4d3db38`. The earned lines below were printed on the detached `381b841` scratch.

Earned runs that printed PASS:

- `l16_arrival_elevator_earned_test`: walk into region 233, elevator movie, relocation to region 343. No E starts the ride.
- `l16_ne_tower_earned_test`: walk to region 6079, the door quad records the entrance, the centre stays down. No E.
- `l16_se_oil_earned_test`: left click burns prop 392, E takes the Dark Bow, the blue bow stays.
- `l16_nw_traps_earned_test`: brick, blue bow, level-three spark.
- `l16_sw_chips_earned_test`: pedestals stay clear.
- `l16_centre_tower_earned_test`: walk into the mantle hall. No E.
- `l16_dragon_room_earned_test`: chop of prop 241. The pad does not move Luther.
- `l17_cavern_run_earned_test`: control 74 kind 5, then region 1312.
- `l17_beast_blade_earned_test`: E at the west wall records hw01.vqa. The movie is not played.
- `l19_beast_wall_earned_test`: walk into region 1312 requests L19 arrival 1. No E for that trip.
- `l19_belial_horn_earned_test`: E takes the horn.
- `l19_sewer_forms_earned_test`: standing in form sets the switches. No E.
- `l16_dry_fountain_earned_test`: left click breaks prop 210, E takes one lichen.
- `l16_greenhouse_earned_test`: E on the pyramid and the hourglass.
- `l14_chamber_voices_earned_test`: E on the kind-4 door, click on the chalice, L16 arrival 1.

`l19_drain_path_earned_test` did not print PASS. The short-path walk fell below the recovery line on the first step (`fall recovery invalidates earned route`). The script already says the rapids are unmapped. That is not a walk-in waiting on E, so there is no floor patch. The heads, Dawn, pillar, armory, faux-Draracle, and finale earned tests did not run, because they read the drain save that was not written. Region 2369 stays the host `enter_region` path in the Dawn test, with the existing arrival adapter for index 52. That earned call was not reached.
