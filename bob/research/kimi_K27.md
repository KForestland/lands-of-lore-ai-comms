# Kimi K27 — AW01-AW03 Act 1 village logic vs lol2_act3 (read-only, 2026-11-07)

Lead spot-check: jungle_drunk_state.gd:56 emits local7 writes and the drunk source holds the 0701/0702 commands - Kimi is right, AW01 wording is wrong. No dead-end/unreachable claim contradicted. Doc corrections only (grok to fix AW01: drunk writes alarm local 7; group 3926 = region 1921; den magic-item offer before flag 19 loses the item, movie 505). No code action.

Verification complete. Here is the report.

  ## K27 — verification of AW01/AW02/AW03 against `lol2_act3`

  Scope checked: every named flag, GV, item id, NPC/actor id, group/record number, opcode value, and the cited precondition/consequence logic in `scripts/lol2/*`, `assets/lol2/generated/items/definitions.json`, `docs/bacatta-rooms.md`, `docs/tavern-return.md`, and `~/AI_COMMS/reference_hintbook/hintbook.txt` (the path AW01 cites as `reference_hintbook/hintbook.txt` lives under AI_COMMS, not the repo).

  | claim | kind | found | evidence | ok |
  |---|---|---|---|---|
  | Gate admission: `shared_flag_38==1`, shared29==0, local24==0; region 2443 | flag/precondition | yes | `jungle_village_state.gd:2,37-38`; field at `act_one_quest_state.gd:9` | ok |
  | shared29 = `GV_HULINE_ALERT`; speech clock 415/15; local15 set at clock end; local46 stays 0 | flag/timer | yes | `jungle_village_state.gd:4,6,31-32` | ok |
  | Follow-up: arms local18==0 & shared29==0; speaks local18==1, shared18==0, local46==0; phases 0,1,2,40,50 | precondition | yes | `jungle_followup_state.gd:10,18-20` | ok |
  | Journal note `gate_closed_before_shalla` | quest key | yes | `jungle_village_state.gd:8` | ok |
  | WPN intro: flags 69/65/66/67 + `GV_LUTHER_KNOWS_ABOUT_DANIEL=1`; rooms WPNEXT/WPN | flag/GV | yes | `weapon_shop_data.gd:3` (intro plan), `weapon_shop_state.gd:19` | ok |
  | WPN orb: flag 254 + `GV_KNOWLEDGE_OF_POWER_ORB=1`; grants `5-Short swd`/`7-Long arm`/`42-Gargoyle br`/`9-Firestorm`; flag 63 = Firestorm; 12 plans | flag/item | yes | `weapon_shop_data.gd:3`; all 11 item ids in `assets/lol2/generated/items/definitions.json` | ok |
  | Kit'yara: six offers; kill records opcode 206 idx0 val 255 (−1) + shared 25 `GV_KITYARA_DEAD` | soul/opcode | yes | `jungle_kityara_source.json` offers=6; 12 records with `ce00000000ff` + `c70000001901` | ok |
  | MAG-intro: flag 52 clear, not 55/56,56/57,58; flag 58, 53 at line 404, 54 at 409, mana −1000 at 419, timer | flag/precondition | yes | `magic_shop.gd:140-152` | ok |
  | MAG-orb-sword: `83-Power orb`, flag 49 clear, broken sword held → flag 49, consume, `GV_LUTHERS_SOUL` = passed+1, movie 442 | soul/item | yes | `magic_shop.gd:107-109` | ok |
  | MAG-mend: `12-Tho Broken` + flag 49 → consume, xp +100, `21-Tho fixed` | item | yes | `magic_shop.gd:98-100` | ok |
  | MAG-name-orb: broken sword, flag 49 clear → movies 423–428, `GV_KNOWLEDGE_OF_POWER_ORB=1` | GV | yes | `magic_shop.gd:101-103` | ok |
  | MAG-dagger: `10-Th Dagger` → `28-Dag Light`, no soul write | item | yes | `magic_shop.gd:104-106` | ok |
  | MAG-other → movie 429; MAG-empty needs flag 53, flag 55 gates re-arm; MAG-kill msg 7 → flag 52, soul−1, movies 432; MAG-timer → 430–431 + visit flags; msg 11/12 no-op | flag/soul | yes | `magic_shop.gd:110-135,155-157` | ok |
  | Confidante locals 20/27 `Met_Confidant`/39 `Killed_Confidante`; controls 112/123; both start absent (0x1000); region 3408 pred 198; local 6 = hut smoked | flag/NPC | yes | `jungle_confidante_state.gd:5,7,25-28`, source `local_names` | ok |
  | CON-2: group 25584, predicate 208 = owner_state==2, opcode 206 idx0 val +1 | soul/opcode | yes | source record 25584 cmd `ce0000000001`, predicate 208 | ok |
  | CON-hit: groups 25628/25802, kind 9 one-shot, no predicate, local39=1 + `ce00000000ff` (−1) | soul/opcode | yes | source records + `hits` block | ok |
  | Journal note `hut_smoked_before_password` (den flag 131) | quest key | yes | `thieves_den_state.gd:15` | ok |
  | Den entry region 3642 → TEXT; context flags kelsrick_dead, alert, met_kelsrick, met_confidant, firestorm | region/precondition | yes | `thieves_den_state.gd:16,192-193,201-204` | ok |
  | TEXT hot0→TCEL else handled 0; TCEL hot2→TDOOR, hot0→movie(2,26); TDOOR flag270→shut; flag63&!271→sfx394; kelsrick_dead&!28→sfx394; !met→flags 131+270, movies 475/509-511/476; met→flag 271, TINT | flag/precondition | yes | `thieves_den.gd:42-86` | ok |
  | DEN-paint flag21→`123-Pois paint` movies 502/503; DEN-key flag22→`93-Skull key` movie 29 | flag/item | yes | `thieves_den.gd:104-108` | ok |
  | DEN-first: flag28→movies 477–501, flags 29/30/31, 498–499 only if met_kelsrick | flag | yes | `thieves_den.gd:172-177` | ok |
  | DEN-return-alive: 23→515–518, 24→525–527+TCEL; alert-alive: 23→550–553, 24→575–577 | precondition | yes | `thieves_den.gd:180-195` | ok |
  | DEN-pay: kelsrick dead, flag 308 clear → movie 600, grant `9-Firestorm`+`Luther_has_firestorm` if 63 clear; alert→603–606+timer+flag18; always 63, xp+100, 308 | flag/item | yes | `thieves_den.gd:158-167,187-188,196-197` | ok |
  | DEN-tunnel flag18→clear+TINTTRAN; DEN-price alert→554/556/557+flag19+timer; DEN-pay-price flag19+magic→take item, clear 19, 558/560, tunnel | flag | yes | `thieves_den.gd:120-122,135-137` | ok |
  | DEN-attack: flag27 clear → flag 27, movies 993/994, damage −1; DEN-leave sets first clear of 23/24/25 → TCEL | flag | yes | `thieves_den.gd:142-155` | ok |
  | No king's-stones/switch handler in `thieves_den.gd` (F6) | gap claim | yes | grep `stone|king` → no matches | ok |
  | Kelsrick actor 64; E+item → `use`→`State.offer`, empty hand nothing; kind-9 hit mirror | NPC/precondition | yes | `jungle_kelsrick_source.json` actor 64; `jungle_kelsrick.gd:5,131-134` | ok |
  | KEL-poison: record 30402 mask 0x60, no predicate, only `c7…0b01` (`GV_KELSRICK_DEAD`=1), no alert cmd | opcode | yes | source group 30402 commands | ok |
  | KEL-loud: 30456 pred 31 (owner!=3 & local52==0), 30544 pred 132 (owner==3 & local52==0), both `c7…1d01` (`GV_HULINE_ALERT`=1) | opcode | yes | source groups + predicates 31/132 | ok |
  | KEL-state40: group 30756, event 6, pred 246 = owner_state==40 → alert | opcode | yes | source group 30756 + predicate 246 | ok |
  | KEL-death: group 31122 event 6 val 11, no predicate, `ce…00ff` (soul −1) + `c7…0b01` | soul/opcode | yes | source group 31122 | ok |
  | Soul writer clamps 0..10 | soul | yes | `jungle_kelsrick.gd:253`; `shared_global_defaults.gd:11-16` | ok |
  | Drunk = control 110, sight/reach/movie, no choice table | NPC | yes | `jungle_drunk.gd:2,72-75` (no choice fn) | ok |
  | Drunk does **not** write alarm local 7 (`Has_Luther_had_drunken_encounter`) | flag | **contradicted** | `jungle_drunk_state.gd:56`, `jungle_drunk.gd:58`; source has 13 `c6…07xx` commands | **NO** |
  | LIZ hotspots 1–4, once per visit, lines [56,21,27,58,26,33,57,20], full mask clears low 8 bits; no 199/206 in `liz_room_source.json` | quip/opcode | yes | `liz_room_responses.gd:3-10`; source scan = 0 | ok |
  | Bacatta57: region 3501 → g10162 when `GV_BACATTA_RELATIONSHIP==0`; doors 56/57 shut; removed at region 3157 once `GV_MET_BACATTA==1`; no soul opcode in its source | NPC/GV | yes | `jungle_bacatta57.gd:2-4,93`; source scan = 0 | ok |
  | Bacatta65: prop 553, actor 65, kind4 offer / kind9 hit; record 79 = soul−1, rel−1, set `GV_MET_BACATTA`; several records set MET_BACATTA (4), one adds rel+1 (1) | NPC/opcode | yes | `jungle_bacatta65.gd:3,7-8`; source record[79] `ce…00ff,ce…0dff,c7…1201` | ok |
  | Soul table: 25584 +1; 25628/25802 −1; 27172 −2 (`ce…00fe`); 31122 −1; Kit'yara −1; 10816 +1/+1 (soul, rel idx13); 11072 −1,−1,set0 (soul, `GV_DAWN_RELATIONSHIP` idx12, rel); bacatta65 rec79 −1/−1; Rashar GDScript ±1 | soul/opcode | yes | all command bytes decoded as claimed; shared_names maps 0/11/12/13/18/25/29 | ok* |
  | Soul table row "Bacatta **prop 552** group 3926 (+2)" | owner label | mislabeled | `jungle_bacatta_source.json`: group 3926 owner_kind=**region**, owner **1921** | **NO** (minor) |
  | Alarm: group 27172 pred 192 (shared29==1 AND local32==0), soul −2, gates 78/79 & 74/75 → 0, doors 56/57 → 100, local7=2, Kelsrick bundle; g21372 (local33==1) / g21418 (local52==1) set shared29=1; no timer stop cmds | flag/soul/opcode | yes | `jungle_village_alarm_state.gd:4-13`; source records[2]=27172/pred 192; cmds `ce…fe`, `01204a/4b…00`, `012038/39…64`, `c6…0702`; preds 166/49 | ok |
  | CAN table (enter flag 267/flag 41/148 frames; setup `GV_MET_BACATTA=1`; talk flags 34/45→45, 625–636, 32/33 after 628/632, 37 after 636; promise 640–648 msg10 clears 37; leave rel+1 + flag 34, 656/657; early 0xE09 rel 0, 637/638, 676/677; maid Left_Village==3 & flag 34 → 700–709, `GV_HULINE_ALERT`=1, flag 267, shut; revisit flags 42/43/44; Left_Village local 36: 0→2 @3501, 2→3 @3805) | flag/GV | yes | `docs/bacatta-rooms.md:3-5,17-24`; `docs/tavern-return.md:12,16-17,26,30,83` | ok |
  | Journal notes `thohan_sword_broken`, `village_hostile_gate_shut` (flag 18, Force-gate fallback) | quest key | yes | `weapon_shop_state.gd:8`, `thieves_den_state.gd:18`, `thieves_den_rooms.gd:9` | ok |
  | HINTBOOK 2242–2246 (missing girl), 2332–2349 (gate open, tavern last, shaman, thief optional, drunk, Baccata, don't attack), 2253–2257 (armorer/orb), 5682–5685 (sword for kill, king's stones after switch) | citation | yes | `~/AI_COMMS/reference_hintbook/hintbook.txt` at those lines | ok |
  | F12 dead end: early cantina exit leaves `GV_BACATTA_RELATIONSHIP` 0 = Dawn's prerequisite | dead-end claim | yes | `docs/bacatta-rooms.md:22-24,30-31` | ok |
  | F1: no tavern-last flag; F11: soul byte stored but Act 3 branch tests don't read it; F14: drunk no branch; F15: Force-gate fallback documented | gap claims | yes | no tavern-last flag found; `monastery_quest_state.gd:58` reads soul only for validation bounds, no route compare; `thieves_den_state.gd:18` names Force gate fallback | ok |

  ### Problems

  1. **Drunk / local 7 claim is wrong (AW01 §drunk, line 151).** "Alarm local 7 … is not written by the drunk script read here." The hosted drunk script does write it: `jungle_drunk_state.gd:56` emits `{"type":"local7",…}` for any opcode-198 command targeting local 7, `jungle_drunk.gd:58` applies it to `host.village_alarm.state.locals["7"]`, and `jungle_drunk_source.json` contains 13 such commands (`c60000000701` on encounter, `c60000000702` at retirement). The name is right (`jungle_village_alarm_source.json` local_names), the "not written" is not.
  2. **Soul-table mislabel (AW01 line 189).** "Bacatta prop 552 group 3926" — group 3926's owner is **region 1921**, not prop 552 (`jungle_bacatta_source.json`). The +2 opcode is correct, and AW02 §Soul states the ownership correctly, so this is an internal inconsistency between AW01 and AW02.
  3. **DEN-offer-else omits the item loss (AW01 den table).** Offering a **magic** item while flag 19 is clear is not just "movie 504 or 505": the item is taken (`take_held_item`, `thieves_den.gd:135`) and only movie 505 plays — the player loses the item for nothing. Worth one extra clause in the row.
  4. **Nuance on F11 (not a contradiction).** `monastery_quest_state.gd:58` does read `GV_LUTHERS_SOUL`, but only to bounds-check it in `validate()` — no branch or comparison selects on it, and no Act 3 route test reads it. The claim stands; the wording "no save field compares that byte" is still accurate.

  No claimed dead end or unreachable branch was contradicted by the code: hut-smoked lockout (local 6 / journal flag 131), Confidante-kill lockout (local 39), Firestorm-first door buzz (`thieves_den.gd:75`), Kelsrick-early-kill buzz (`thieves_den.gd:76`), attack-Mauri damage −1 (`thieves_den.gd:144`), and the flag-37 early walk-out (`docs/bacatta-rooms.md:23-24`) are all hosted exactly as described.

