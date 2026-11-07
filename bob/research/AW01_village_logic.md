# AW01 — Act 1 Huline village as a state machine

Live scripts on `stack-ah01` `cfba754` when this note was first posted. Three sentences were corrected after K27: the drunk writes alarm local 7, group 3926 belongs to region 1921, and a magic item offered at the den before flag 19 is taken and only movie 505 plays. Unapplied AV, AU, AS, and AR diffs are not in this tree. Grades: DECODED for an opcode or flag read out of a source JSON or the GDScript that interprets it this pass; HINTBOOK for `reference_hintbook/hintbook.txt`; the tavern sentences are the existing `docs/bacatta-rooms.md` and `docs/tavern-return.md` audits, not a new DLL read. No WOM line was opened. No Godot run.

## What the village is for

HINTBOOK 2242–2246 and 2332–2349. An old man at the gate says a girl is missing. After she is rescued, the gates open. The player tours the village and leaves the tavern for last, meets Baccata, and does not start a fight. The password and the thief are a side path. The honest route is the one that continues to the monastery.

The required chain in these files is: gate speech, Hive rescue, gate opens, tavern promise (`GV_BACATTA_RELATIONSHIP` raised, flag 34 set), then Dawn. Shops, the drunk, the Confidante, Mauri, Poison Paint, and the soul byte are beside that chain.

## Graph

```text
gate elder (speech, no choice)
    |  shared_flag_38 == 1, shared29 alarm still 0, local24 still 0
    v
gate opens (local24=1) --> village speech plays out (local15=1)
    |
    +-- Kit'yara (WPN): intro sets GV_LUTHER_KNOWS_ABOUT_DANIEL
    |       orb talk sets GV_KNOWLEDGE_OF_POWER_ORB
    |       grants: short sword, long arm, gargoyle bracers, Firestorm (flag 63)
    +-- Rashar (MAGIC): curse drain on the intro; Power Orb + broken sword -> soul set to current+1
    |       later offer of the broken sword -> Thohan's fixed; throwing dagger -> Dagger of Light
    |       killing him: soul-1, flag 52, he is gone
    +-- Confidante: first talk sets Met_Confidant (local27)
    |       second talk (owner state 2): soul+1
    |       a hit on either meeting: Killed_Confidante, soul-1
    +-- yard region 3642 --> TEXT --> TCEL --> TDOOR
    |       password (Met_Confidant) --> TINT Mauri
    |       no password: flags 131 and 270, door stays shut
    |       Firestorm already (63) or Kelsrick already dead before the deal (28): door buzzes
    |       Mauri: Poison Paint, Skull Key, then the deal
    |       return after Kelsrick is dead: Firestorm, fighting xp, flag 308
    |       alert: tunnel (flag 18) or a price (flag 19)
    |       attack Mauri: damage -1
    +-- Kelsrick: offer with an item; a hit
    |       poison-mask record 30402 sets GV_KELSRICK_DEAD
    |       other hit records set GV_HULINE_ALERT
    |       death group 31122: soul-1 and GV_KELSRICK_DEAD
    +-- drunk (control 110): the movie plays; no choice table in the live script
    +-- LIZ: hotspots 1-4 draw one unused quip from lines 56,21,27,58,26,33,57,20
    +-- CAN first visit: lines through the promise, then relationship+1 and flag 34
    |       leave while flag 37 is still set: relationship stays 0
            later visit with Left_Village==3 and flag 34: maid lines 700-709, alert=1, flag 267, tavern stays shut
    |
    v
alarm, only if shared29==1 and local32==0 (group 27172): soul-2, gates shut, Kelsrick hostile
    |
    v
monastery Dawn, after the promise has raised the relationship
```

## Gate elder and the opening

`jungle_village_state.gd` and `jungle_village_gate.gd`. No player line. Walking into region 2443 calls `admits` with `quest_state.shared_flag_38`. Admission runs when that flag is 1, `shared29` is 0, and `local24` is 0. The gate comment names a clear `shared_flag_38` as the pre-rescue stuck point. `shared29` is `GV_HULINE_ALERT`. `local24` is the admission, and it stays in 0..1. The speech clock is 415/15 seconds. `local15` becomes 1 only when that clock finishes. `local46` stays 0 while the speech runs.

The follow-up owner (`jungle_followup_state.gd`) arms when `local18==0` and `shared29==0`. It speaks when `local18==1`, `shared18==0`, and `local46==0`. Phases that validate are 0, 1, 2, 40, and 50. HINTBOOK 2242–2246 is the missing-girl speech. HINTBOOK 2332–2333 is the open gate after the rescue.

Journal note `gate_closed_before_shalla`: the gate stays shut until the Hive rescue.

## Kit'yara, the armorer

`weapon_shop_state.gd` and `weapon_shop_data.gd`. Room names `WPNEXT` and `WPN`. One movie cursor. Plans present in the data file: `intro`, `orb`, `orb_known`, `orb_preknown`, `longarm`, `gargoyle`, `gargoyle_after_sword`, `shortsword`, `refuse`, `offer_orb`, `offer_orb_repeat`, `offer_dagger`.

| id | action | precondition | consequence | next |
| --- | --- | --- | --- | --- |
| WPN-intro | enter and let the intro finish | room WPN, sequence intro | flags 69, 65, 66, 67; `GV_LUTHER_KNOWS_ABOUT_DANIEL=1` | she will trade |
| WPN-orb | the orb conversation | plan `orb` / `orb_known` / `orb_preknown` / `offer_orb` | flag 254; `GV_KNOWLEDGE_OF_POWER_ORB=1` | the Power Orb is named |
| WPN-buy | take a listed weapon | the matching plan | grants `5-Short swd`, `7-Long arm`, `42-Gargoyle br`, or `9-Firestorm` | flag 63 is Firestorm, shared with the den |
| WPN-refuse | offer she will not take | plan `refuse` | no grant in the plan name | stay |

HINTBOOK 2253–2257: she sells a bow and bracers, and she keeps the fire sword and the broken-sword repair until there is a Power Orb. The broken-sword repair itself is Rashar's, below. `jungle_kityara_state.gd` is the world actor behind the shop: six offers, and kill records that do opcode 206 index 0 with value 255 (signed −1) and set shared 25 `GV_KITYARA_DEAD`. Those kill records were counted, not each walked.

## Rashar, the magic seller

`magic_shop.gd` `offer` and `killed`. HINTBOOK 2336 calls this stop the shaman and says to take what you can. The curse drain is the intro's `mana_debit` of 1000 on movie line 419, and only while flag 52 is clear.

| id | action | precondition | consequence | next |
| --- | --- | --- | --- | --- |
| MAG-intro | first update | flag 52 clear, and not the later-visit pairs 55/56 or 56/57 or 58 | flag 58, flag 53 at line 404, flag 54 at line 409, mana −1000 at line 419, timer armed | he has drained the curse |
| MAG-orb-sword | hand him `83-Power orb` | flag 49 clear, flag 52 clear, a broken Thohan sword is also held | flag 49, orb consumed, `GV_LUTHERS_SOUL` set to the passed soul plus 1, movie 442 | the mend is not in this step |
| MAG-mend | hand him `12-Tho Broken` | flag 49 set, flag 52 clear | sword consumed, fighting experience +100, grant `21-Tho fixed` | done |
| MAG-name-orb | hand him `12-Tho Broken` | flag 49 clear | movies 423–428, `GV_KNOWLEDGE_OF_POWER_ORB=1` | he names the price |
| MAG-dagger | hand him `10-Th Dagger` | flag 52 clear | dagger consumed, grant `28-Dag Light` | no soul write |
| MAG-other | hand him anything else | flag 52 clear | movie 429 | no grant |
| MAG-empty | click him with an empty hand | flag 53 set; flag 55 gates the timer | no grant | the timer may re-arm |
| MAG-kill | message 7 | flag 52 clear | flag 52, soul set to the passed soul minus 1, movies 432, he stops | he stays dead (flag 52 refuses later offers) |
| MAG-timer | timer expires | flag 52 clear | movies 430–431, then the visit flags, leave | out |

Messages 11 and 12 acknowledge and change nothing. Quips use an eight-line mask (`quip_plan`). Journal note `thohan_sword_broken` points at this mend.

## The Confidante

`jungle_confidante_state.gd` and `jungle_confidante_source.json`. Locals: 20 trigger, 27 `Met_Confidant`, 39 `Killed_Confidante`. Controls 112 (second meeting) and 123 (first). Both start absent (placement bit 0x1000).

| id | action | precondition | consequence | next |
| --- | --- | --- | --- | --- |
| CON-1 | stand in the hold and let control 123 finish | header: sighted barrel links 123; region 3408 predicate 198 holds him; local 6 (hut smoked) is the header's block | end sets local 27 | password known; he unlinks |
| CON-2 | the second meeting, control 112, owner state 2 | predicate 208 is owner_state==2; header ties that to the state-2 end | opcode 206 index 0 value 1 (soul +1), group 25584 | he unlinks |
| CON-hit | a landed hit on 112 or on 123 | kind 9, one-shot, no predicate on records 3 and 7 | local 39=1, opcode 206 index 0 value 255 (soul −1), groups 25628 and 25802 | death segment |

HINTBOOK 2337–2341: hear a password, then find the door. The diversion is not required. The header's first-meeting block when the hut is already smoked is the original stuck point. Journal note `hut_smoked_before_password` (den flag 131) says the alley talker is lost.

## Thieves' den (TEXT, TCEL, TDOOR, TINT)

`thieves_den.gd` and `thieves_den_state.gd`. Entry is region 3642 into TEXT. Context flags the host passes in: `kelsrick_dead`, `alert`, `met_kelsrick`, `met_confidant`, `firestorm`.

| id | action | precondition | consequence | next |
| --- | --- | --- | --- | --- |
| DEN-yard | click TEXT hotspot 0 | in TEXT | room TCEL | cellar |
| DEN-yard-else | any other TEXT hotspot | in TEXT | handled 0 | stay |
| DEN-cellar-door | TCEL hotspot 2 | in TCEL | room TDOOR | the slot door |
| DEN-cellar-barrel | TCEL hotspot 0 | in TCEL | movie speaker 2 line 26 | stay |
| DEN-cellar-else | any other TCEL hotspot | in TCEL | handled 0 | stay |
| DEN-door-shut | TDOOR hotspot 0 | flag 270 set | handled 0 | stay |
| DEN-door-sword | TDOOR hotspot 0 | flag 63 set and flag 271 clear | sfx 394 only | stay; Firestorm already taken |
| DEN-door-early-kill | TDOOR hotspot 0 | Kelsrick dead and flag 28 clear | sfx 394 only | stay; the deal was never heard |
| DEN-door-no-word | TDOOR hotspot 0 | `met` false, and the two locks above clear | flags 131 and 270, movies 475 / 509-or-510-or-511 / 476 | door dies (270) |
| DEN-door-word | TDOOR hotspot 0 | `met` true | flag 271, room TINT | Mauri |
| DEN-paint | click sprite 0 | flag 21 clear | flag 21, grant `123-Pois paint`, movies 502 and 503 | once |
| DEN-key | click sprite 1 | flag 22 clear | flag 22, grant `93-Skull key`, movie 29 | once |
| DEN-first | TINT first update | flag 28 clear | flag 28, the 477–501 movies, flags 29, 30, 31; lines 498–499 only if `met_kelsrick` | the deal is heard |
| DEN-return-alive | a later visit | flag 23 or 24 set, Kelsrick alive, alert clear | flag 23 plays movies 515–518; flag 24 plays 525–527 and returns to TCEL | he will not pay yet |
| DEN-return-alert-alive | a later visit | flag 23 or 24 set, Kelsrick alive, alert set | flag 23 plays movies 550–553; flag 24 plays 575–577 | no Firestorm |
| DEN-pay | a later visit | flag 24 or 23 set, Kelsrick dead, flag 308 clear | `_firestorm`: movie 600; if flag 63 was clear, grant `9-Firestorm` and local `Luther_has_firestorm`; if alert, movies 603–606, timer, flag 18; always flag 63, fighting xp +100, flag 308 | paid once |
| DEN-tunnel | hotspot 0 | flag 18 set | clear 18, room TINTTRAN, place the tunnel point | outside |
| DEN-price | hotspot 0 | flag 18 clear, alert set | movies 554, 556, 557, flag 19, price timer | he wants payment |
| DEN-pay-price | offer a magic item | flag 19 set, holding a magic item | take the item, clear 19, movies 558 and 560, tunnel | outside |
| DEN-offer-else | offer a non-magic item, or an empty hand | in TINT | movie 504, or handled 0 when the item is not magic and the state bit is clear | stay |
| DEN-offer-magic-early | offer a magic item while flag 19 is clear | in TINT | take the item, movie 505 only | stay; the item is lost |
| DEN-attack | spell or weapon | flag 27 clear | flag 27, movies 993 and 994, damage −1 | dead |
| DEN-leave | Back | in TINT | sets the first clear flag among 23, 24, 25, then back to TCEL | visit counter |

HINTBOOK 5682–5685 (chapter 15): kill Kelsrick and the thief gives the sword the armorer otherwise sells; the king's stones come after that kill and a switch; the flood path does not give the stones. The stones and the switch are not a handler in `thieves_den.gd`.

## Kelsrick

`jungle_kelsrick.gd` and `jungle_kelsrick_source.json`. Actor 64. E while aimed uses a non-empty held item (`use` → `State.offer`). An empty hand does nothing. Damage is mirrored into kind-9 hit records.

| id | action | precondition | consequence | next |
| --- | --- | --- | --- | --- |
| KEL-offer | E with an item, aimed | present, alive, not in a clip or a hold | `State.offer` effects | the source offer groups |
| KEL-poison | a coated melee hit | script comment: flags word 0x20/0x40, record 30402 mask 0x60 fires alone | group 30402 opcode 199 index 11 = 1 (`GV_KELSRICK_DEAD`) | no alert command in that group |
| KEL-loud | other kind-9 hits | group 30456 predicate 31 (owner state != 3 and local 52 == 0); group 30544 predicate 132 (owner state == 3 and local 52 == 0) | opcode 199 index 29 = 1 (`GV_HULINE_ALERT`) | the alarm can arm |
| KEL-state40 | event 6 | predicate 246, owner state == 40, group 30756 | opcode 199 index 29 = 1 | alert |
| KEL-death | event 6 value 11 | group 31122, no predicate | opcode 206 index 0 value 255 (soul −1) and opcode 199 index 11 = 1 | dead; this group does not open the den |

The soul writer in `jungle_kelsrick.gd` stores `GV_LUTHERS_SOUL` clamped to 0..10. The comment calls that cap the verified runtime table. This pass did not re-enter that table.

## The drunk, LIZ, the gate Bacatta, the cantina

The drunk is control 110 (`jungle_drunk.gd`). The live script is a sight, a reach, a movie, and a voice. No choice function was found. HINTBOOK 2343: talk to him for humor. Alarm local 7 is named `Has_Luther_had_drunken_encounter`. The drunk script writes it. `jungle_drunk_state.gd` emits a local-7 effect for an opcode-198 command whose target is local 7, and `jungle_drunk.gd` stores that value on the alarm locals. The drunk source holds 13 of those commands: `c60000000701` on the encounter and `c60000000702` at retirement.

LIZ (`liz_room_responses.gd`): hotspots 1–4 each fire once per visit. The line is one unused entry of 56, 21, 27, 58, 26, 33, 57, 20. A full mask clears the low eight bits. No soul write in `liz_room_source.json`.

Bacatta at the village doors (`jungle_bacatta57.gd`): region 3501 starts group 10162 when `GV_BACATTA_RELATIONSHIP==0`. Doors 56/57 shut. She is removed at region 3157 once `GV_MET_BACATTA==1`. Striking her makes the peaceful body hostile. No soul opcode in `jungle_bacatta57_source.json`.

Bacatta in the world before the first meeting, while the alert is up (`jungle_bacatta65.gd`): prop 553 talk, actor 65. E with a carried item is the offer. A melee hit is kind 9. Source records: several set `GV_MET_BACATTA`; one adds 1 to `GV_BACATTA_RELATIONSHIP`; record 79 subtracts 1 from soul and from the relationship and sets `GV_MET_BACATTA`.

The cantina room (`docs/bacatta-rooms.md`, `docs/tavern-return.md`):

| id | action | precondition | consequence | next |
| --- | --- | --- | --- | --- |
| CAN-enter | hotspot 2 | flag 267 clear | room CAN | first visit plays the 148-frame intro and sets flag 41 |
| CAN-setup | setup | not (Left_Village==3 and flag 34) | `GV_MET_BACATTA=1` | Bacatta is installed |
| CAN-talk | let it play | flags 34 and 45 clear; sets 45 at the start | lines 625–636; flags 32 and 33 after 628 and 632; flag 37 after 636 | the promise is pending |
| CAN-promise | message 10 | flag 37 set | lines 640–648, clear 37 | then the ordinary leave |
| CAN-leave | walk out after the promise | flag 37 clear | relationship +1, flag 34, Luther 656, Bacatta 657 | Dawn can take this relationship |
| CAN-early | walk out while 37 is set | flag 37 still set | 0xE09: flag 34, relationship 0, Luther 637/638, Bacatta 676/677 | the promise is skipped |
| CAN-maid | a later visit | flag 34 set and Left_Village==3 | lines 700–709, `GV_HULINE_ALERT=1`, flag 267, room closes | the tavern stays shut |
| CAN-revisit | a later visit, flag 42/43/44 still clear | flag 34 set, Left_Village is not that maid case | the matching short lines, or 0xE09 when 44 is taken | see the tavern-return table |

`Left_Village` (local 36) goes 0→2 at region 3501 and 2→3 at region 3805. Hostile and click-to-attack branches are still open in that doc. HINTBOOK 2344–2349: keep the conversation moving and do not start an attack.

## The alarm

`jungle_village_alarm_state.gd`. Group 27172 runs when shared 29 is 1 and local 32 is 0. Effects named in the header and present as commands: soul opcode 206 index 0 value 254 (signed −2); gates 78/79 and 74/75 to 0; Bacatta57 doors 56/57 to 100; local 7=2; Kelsrick hostility forwarded to his owner. Groups 21372 (local 33 == 1) and 21418 (local 52 == 1) set shared 29 to 1. Bells and arrow timers have no stop command in the header.

Journal note `village_hostile_gate_shut` (den flag 18): Mauri's tunnel is the way past the palisade once the village is roused. The same note names Force gate as the fallback when the Confidante is dead.

## Soul writes found in the village sources

| where | opcode | index | signed value | name |
| --- | --- | --- | --- | --- |
| Confidante group 25584 | 206 add | 0 | +1 | `GV_LUTHERS_SOUL` |
| Confidante groups 25628 and 25802 | 206 add | 0 | −1 | `GV_LUTHERS_SOUL` |
| Alarm group 27172 | 206 add | 0 | −2 | `GV_LUTHERS_SOUL` |
| Kelsrick group 31122 | 206 add | 0 | −1 | `GV_LUTHERS_SOUL` |
| Kityara kill records (117 and the repeats counted with it) | 206 add | 0 | −1 | `GV_LUTHERS_SOUL`, and shared 25 `GV_KITYARA_DEAD` |
| Bacatta region 1921 group 3926 | 206 add | 0 | +2 | `GV_LUTHERS_SOUL` |
| Bacatta prop 552 group 10816 | 206 add | 0 and 13 | +1 and +1 | soul and `GV_BACATTA_RELATIONSHIP` |
| Bacatta prop 552 group 11072 | 206 add, then 199 set | 0, 12, 13 | −1, −1, set 0 | soul, `GV_DAWN_RELATIONSHIP`, `GV_BACATTA_RELATIONSHIP` |
| Bacatta65 record 79 | 206 add | 0 and 13 | −1 and −1 | soul and relationship |
| Rashar offer and kill | GDScript set | `GV_LUTHERS_SOUL` | passed value +1, or −1 | not an opcode 206 in that file |

`liz_room_source.json` and `tavern_return_source.json` contain no opcode 199 or 206. The cantina relationship write is the room doc's leave, not those two JSON files.
