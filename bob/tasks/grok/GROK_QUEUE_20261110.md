# Grok queue, 2026-11-10 (written by Fable for the owner's request)

Pull the next task yourself after posting READY for the one before. Each task is one question, sized for one to four hours. If a task passes four hours, post what you have with grades and move on.

Rules that hold for every task:
- Grade every claim PROVEN, LIKELY or UNKNOWN. An UNKNOWN with what you tried is a finished task.
- Write one note per task in `grok_research/` and one board line. Host nothing unless the task says 'patch'.
- A patch goes on your own branch with a test, and you name the commit. Limits: 2 Godot at once, 10 GiB free before each launch, `--audio-driver Dummy`.
- Where a task says 'or absent', a proof of absence closes it (owner decision D4: list, do not invent).
- Paths below are under `~/AI_COMMS/` or the game tree unless they start with `/`. Hint-book line numbers come from Kimi's audits (`grok_research/kimi_K78.md`, `kimi_K79.md`); I did not re-check each one.

Order: what lets a player get through Act 2 comes first (part A), then what blocks a release (part B), then the rest (part C). Inside a part, take them top to bottom unless a dependency says otherwise.

## OWNER F10, playtest 2026-11-10 night (take these before Q01; lead triage). Build: lol2_play_r19pre = r19-work fee8b8a.
- OF1 Double doors: "the left door is <- should be ->" at Cave (x -58, y -17638, h -261) and at the Jungle (x -1270, y -5249, h 32), reports AI_COMMS/playtest_feedback_20261023/report_2026-11-10T22-33-46_* and T22-47-41_*. Same fault in two areas, so likely one shared door path: find why the left leaf opens or faces the wrong way, fix it once, earned test on both doors.
- OF2 Jungle thorns: "hidden wall here ... could destroy by sword, the roots have not grown back visibly but the wall was there" at (x -3632, y 2230, h -38), reports T23-00-41_* and T23-01-17_*. The cut roots vanish but their collision stays. Fix so the collision goes with the roots (and comes back only if the roots visibly regrow, as the original does), earned test.
- NOTE: the reports below say "Jungle" but the screenshots read "L 10 Dc": they are the Dracoid Cemetery (act2 maps inherit the Jungle label in F10; fix the label too, OF10).
- OF4/OF5/OF6 Cemetery globes: "can't pick up orb" at (155,-3704) where a glass globe floats high in the air near the tower (screenshot T23-36-20); "can't open the crates to get the orb" at (1358,-1269), a stone chest (T23-37-32); "got the orb by cheating, clip through the wall" at (-529,-4058). Find which globes are out of reach, and how the original lets the player reach them (open the chest, lower the globe); fix, earned real-input test. Check against Fable's BJ14 globe stops (S6).
- OF7 Catacomb braziers: "need lighting magic or something that produces light, the braziers do not light up when hit" at (2148,-1521, h -118). The book lights them with a spark (STORY-008); check spark lights them, melee does not, and that the dark catacomb is playable; Journal hint if needed.
- OF8 Atlas underground: "the undermap does not show right information" at (2537,-1819, h -118). Atlas Section view of the L10 catacombs (Sol's Task 3b work); find what is wrong against the explored rooms.
- OF9 Fall through the world: "can not navigate below, clip through wall and fall down and can navigate down below the top of map, can't continue from this point", reset to (-542,-856) (the L10 reset point). Between T23-40-20 (2537,-1819 underground) and T23-41-20. Find the wall Luther can pass through near the catacomb and the drop below the map; fix collision; earned walk with resets 0. TOP PRIORITY of these: it ended the playtest.
- OF3 Texture look: "the textures look not right" at (-167,-966) (T23-33-43): stretched black block over a gate mechanism. Lower priority.
- OF10 F10 label: act2 maps report area "Jungle"; should name the map (L10 Dracoid Cemetery etc.).

## Already yours, in this order (unchanged)

| # | Task | State on the board |
|---|---|---|
| T1 | Kind-2 timer expiry walk | Posted 20:44Z (`R03_kind2_timer_20261110.md`). Open part is Q12 below |
| T2 | I-03 item numbers | Posted 21:08Z. Open part is Q47 below |
| T3 | R-01 damage formula and creature health units | Posted 14:33Z and 21:26Z. Follow-ups are Q01-Q06 |
| T4 | F-10 soul (opcode 206) | Hosted, posted 13:08Z. Follow-ups are Q14 and Q61 |

If any of the four is not finished in your own view, finish it first.

## Part A: a player gets through Act 2

### Q01. Creature blow amounts, Act 2
- **Question:** What amount does each L8, L9 and L10 creature definition put in context+0x1E when it strikes Luther, at difficulty byte 1?
- **Read:** `grok_research/R01_damage_formula_20261110.md`, `R02_creature_health_unit_20261110.md` (strike 0xA6C69, 0x62728); definition records in the level archives; `scripts/lol2/act2_populations/L8_SJ.json`, `L9_DR.json`, `L10_DC.json` (placement_hex, definitions).
- **Done when:** A table: level, definition, name, native blow amount, read site (analysis address + file offset of the definition byte). LAMPLT, StSquid, WILD, SKEL and the Saar at least. Grade each.
- **Unblocks:** BJ14 F9 (Luther dies in the Jungle; the port's 15 per blow is not native); R-01; R-14.
- **Depends on:** none

### Q02. Luther's own strike before the weapon byte
- **Question:** Your I-03 note adds the weapon's signed byte +0x40 at context+0x16. What is the amount before that add, and which player words feed it?
- **Read:** `grok_research/I03_item_numbers_20261110.md`; the five strike callers; player object at [0x23348].
- **Done when:** The formula with read sites, and two worked numbers: short sword and fine longsword for a Luther with the stats found in Q03. No host.
- **Unblocks:** R-01; BJ14 F9 (the port's flat 8).
- **Depends on:** Q03 helps, not required

### Q03. Luther's health, might and level by experience
- **Question:** What do the progression tables at D8A1C / D8B94 (stats 151 / 155) give for health, might and magic per level, and what feeds dword +0x14D (player health cap)?
- **Read:** The two tables in LOLG.DAT (pinned sha in `A01_music_20261110.md`); `R01_damage_formula_20261110.md` (slot +0x88 / +0x84).
- **Done when:** A table level -> health cap, might, magic, experience threshold, with file offsets. One line: the health cap of a new Luther and of a level a player plausibly has leaving Act 1.
- **Unblocks:** R-01; the F2 Darker Jungle start (today 30 health); BJ14 F9 option C.
- **Depends on:** none

### Q04. Health and level at the Darker Jungle arrival, from footage
- **Question:** What health and mana does Luther show in the longplay and in the owner's YouTube frames when he arrives in the Darker Jungle?
- **Read:** `~/lol2_original_screens/longplay_frames_act2plus/g_N.jpg` (every 30 s from 109:40); `~/lol2_original_screens/youtube_playthrough_20261110/` (README lists the Act 2 frames).
- **Done when:** Three or more frames named, with the HUD bars read as a fraction and, if a number shows, the number. Say plainly if the HUD shows no number.
- **Unblocks:** Sets the F2 start's stats with Q03; BJ14 F9.
- **Depends on:** none

### Q05. How armour lowers a blow
- **Question:** Where in 0x62728 does worn armour reduce the amount, and what does the Burnt Chain give?
- **Read:** `I03_item_numbers_20261110.md` (the three class 0x43 records that add through the other equipment slots); `scripts/lol2/player_defense.gd` (the port's scalar).
- **Done when:** The subtraction or scale with its read site; the Burnt Chain's number and two other armours'. State whether the port's scalar agrees.
- **Unblocks:** R-01; I-04; BJ14 F9.
- **Depends on:** none

### Q06. How often a creature strikes, and from how far
- **Question:** What sets the time between two blows and the reach for LAMPLT (L8) and StSquid (L9)?
- **Read:** Definition bytes of both records; behaviour 14 in the placement rows; `scripts/lol2/scripted_creature_population.gd:190-200` for what the port does.
- **Done when:** Seconds between blows and reach in world units, native against port, with the definition offsets.
- **Unblocks:** BJ14 F9; R-12 (creature families).
- **Depends on:** none

### Q07. Who the 61 LAMPLT creatures are and when they attack
- **Question:** Records named LAMPLT (definitions 9, 10, 11, 200 health, flags 25986, behaviour 14) fill the Darker Jungle. Which creature is it in the book, and does the original make them hostile on sight everywhere, or only near, or only at night?
- **Read:** `act2_populations/L8_SJ.json` (actors 29-34, 46-48, 52-56, 60-63, 68-70, 78-80 and the rest); `reference_hintbook/hintbook.txt` Savage Jungle chapter; longplay frames from 109:44.
- **Done when:** The book's name for it, the flag bits that decide hostility and wake distance, and one longplay minute showing the player passing or fighting them.
- **Unblocks:** BJ14 S1-S3; R-14.
- **Depends on:** none

### Q08. Spark and Heal: cost and amount per level
- **Question:** What mana does each level of Spark and Heal cost and what amount does it deal or heal?
- **Read:** `grok_backlog_20261028/G01_outgoing_damage`, `G02_scroll_effects`; the spell table in LOLG.DAT; hint book spell chapter.
- **Done when:** A table for levels 1-5 of both spells: mana, amount, read site, grade. Note what Max Spark does to the caster natively (the port sets health to 1 and protects for about 10 s).
- **Unblocks:** BJ14 S4 (squids); R-06.
- **Depends on:** none

### Q09. Mana: cap by level and how it comes back
- **Question:** What is Luther's mana cap by level and what restores it over time?
- **Read:** Same tables as Q03; the player tick that adds to the mana dword.
- **Done when:** Cap per level and the regeneration rule (amount per interval) with read sites, or UNKNOWN with what was tried.
- **Unblocks:** BJ14 S4; R-05.
- **Depends on:** Q03

### Q10. Stone squids: are they meant to be fought?
- **Question:** Actors 61 and 68 on L9 have 800 health. Does the book or the footage show the player killing them, passing them, or using something on them?
- **Read:** `hintbook.txt` Dracoid Ruins chapter; `act2_populations/L9_DR.json`; longplay frames after the pit.
- **Done when:** Book lines quoted with line numbers, one footage minute, and the native flags that say whether they chase.
- **Unblocks:** BJ14 S4; a design call the lead can take to the owner.
- **Depends on:** none

### Q11. What the placement 'reward_scale' and 'loot' fields do
- **Question:** Placement rows carry reward_scale (8, 10, 12, 15) and a loot dword. What reads them?
- **Read:** `act2_populations/*.json` (placement_hex, placement_offset); the creature death path.
- **Done when:** The read sites and meaning of both fields; five worked rows.
- **Unblocks:** R-17 (loot drops); experience in R-01.
- **Depends on:** none

### Q12. What writes the two kind-2 clocks
- **Question:** Your timer note leaves open what writes dword [0x22C5A] and word [0x22C58]. Find the writers and the unit.
- **Read:** `grok_research/R03_kind2_timer_20261110.md`.
- **Done when:** Writers with analysis addresses, the unit (ticks per second), and whether the clock stops in menus and movies.
- **Unblocks:** F-20 (timer service); the flood time in Q18.
- **Depends on:** none

### Q13. Region events: host the native order and arguments (small patch)
- **Question:** Your event-byte note says the host still passes 0 for event 1, omits event 4's third argument, fires 2 before 4, and never fires event 3 on the region left. Fix those four in the binder.
- **Read:** `grok_research/R02_region_event_bytes_20261110.md`, `F11_region_events_20261110.md`; `scripts/lol2/act2_progression.gd:481`.
- **Done when:** A commit on your branch with a unit test per rule and the list of groups that newly commit per level. `act2_exit_seed_test`, `act2_progression_levels_test`, `l10_progression_test` still pass.
- **Unblocks:** F-11 acceptance; M-09, M-12.
- **Depends on:** none

### Q14. L8 group 7888: opcode 9 kind 4 arm 0x1B
- **Question:** The shore soul group stops at this arm. Decode it.
- **Read:** `grok_research/F10_opcode206_20261110.md` (file 13448414).
- **Done when:** What the arm reads and writes, the callee entered, and either a hosted arm with a test or the reason it cannot be hosted yet.
- **Unblocks:** S-11 (soul census); F-12.
- **Depends on:** none

### Q15. Winged statue, control 150 on L10: touch or use?
- **Question:** The hint book says to walk into the statue; the port needs E. What raises the control natively?
- **Read:** `scripts/lol2/act2_progression.gd:1312-1331`; `native_scripts/L10_DC.json` control 150 records; hint book Dracoid Cemetery chapter.
- **Done when:** The record kind and event that fire the passage, and one sentence: bump, use, or both.
- **Unblocks:** BJ14 F2 (S7).
- **Depends on:** none

### Q16. L10 fences 74 and 174: the native rule
- **Question:** What does the original require to cross the two high fences?
- **Read:** `scripts/lol2/l10_fences.gd:33-43` (the port: airborne + sprint + Ctrl); the fence movables in `static_collision_L10_DC.json`; hint book lines on the fences.
- **Done when:** The native condition with its evidence, or 'not in the data: the port rule is an adapter' with the book lines that describe the move.
- **Unblocks:** BJ14 F6 (S8).
- **Depends on:** none

### Q17. L9 noble rail, controls 478-480
- **Question:** Kind-5 groups 17302 / 17320 / 17338 select the broken rail. What raises them natively: a weapon blow, any use, a jump?
- **Read:** `scripts/lol2/l9_noble_rails.gd:1-5`; `native_scripts/L9_DR.json`; `grok_control_events/FINDINGS.md` (kind-5 dispatch).
- **Done when:** The kind-5 value and the player action that raises it; say whether an unarmed Luther can break it.
- **Unblocks:** BJ14 F6 (S9).
- **Depends on:** none

### Q18. Is the walking statue (L9 actor 76, BELSTAT) meant to take damage?
- **Question:** It has 200 health in the placement row. Can the player hurt or kill it natively?
- **Read:** `act2_populations/L9_DR.json` actor 76; its definition flags; `scripts/lol2/l9_statue_walk.gd`.
- **Done when:** The flag or code path that makes it invulnerable, or proof that it is not. If it can die, say what the original does then.
- **Unblocks:** BJ14 N7 (possible softlock).
- **Depends on:** none

### Q19. L9 flood: how long the player has
- **Question:** What starts the rising water after the statue fight and how many seconds until Luther drowns?
- **Read:** `scripts/lol2/l9_escape.gd`, `l9_flood*.gd`; kind-2 records in `native_scripts/L9_DR.json`; your timer formula.
- **Done when:** The native record(s), the countdown in seconds from your formula, and the port's value beside it.
- **Unblocks:** BJ14 F6 (S12).
- **Depends on:** Q12 for the clock unit

### Q20. L10 priest: ashes to ankh in one use or two?
- **Question:** The port needs two presses and shows the same line twice. What is the native sequence?
- **Read:** `scripts/lol2/l10_priest.gd:61-76`; the priest's groups in `native_scripts/L10_DC.json`; hint book.
- **Done when:** The groups in order with what each gives or says; one sentence on whether one use should hand over the ankh.
- **Unblocks:** BJ14 F3 (S10).
- **Depends on:** none

### Q21. Dragon's blood on L10
- **Question:** The Journal and Atlas mention dragon's blood in the Cemetery but nothing is wired. Find its native rows.
- **Read:** `scripts/lol2/l10_journal_hints.gd`, `atlas_places.gd` (search 'blood'); item rows in `L10_DC` data; hint book.
- **Done when:** Where it is found, what it is used on, the groups involved, and whether it is on the main chain.
- **Unblocks:** M-11.
- **Depends on:** none

### Q22. Yellow tombs and the gold globe
- **Question:** The yellow tombs take the gold globe. Is it lost, returned, or exchanged natively?
- **Read:** `scripts/lol2/l10_tombs.gd`; tomb groups in `native_scripts/L10_DC.json`; hint book.
- **Done when:** The native outcome per tomb colour and globe colour as a small table.
- **Unblocks:** M-11; a possible dead end for the player.
- **Depends on:** none

### Q23. Saar defeat: the capture room
- **Question:** The book says losing to a Saar does not kill Luther; he wakes in a chamber of Saar. Find the redirect.
- **Read:** `hintbook.txt:3612-3625` (cited by `kimi_K78.md`); Saar definition and the player death path.
- **Done when:** The trigger (which check sends him there instead of death), the room's region and arrival point, or 'absent from the data' with what was searched.
- **Unblocks:** R-21.
- **Depends on:** none

### Q24. Door rafting on L9
- **Question:** The book describes dragging a floor door into the river and steering it. Find the records.
- **Read:** `hintbook.txt:3585-3606` and `3755-3771` (from `kimi_K78.md`); movable rows in the L9 data; `scripts/lol2/l9_escape.gd` (raft 82).
- **Done when:** Which movables float, what makes them carry the player, and the steering input, or 'not found' with the search.
- **Unblocks:** M-22.
- **Depends on:** none

### Q25. The book's three ruin secrets
- **Question:** Serpent statue, the ring behind the locked gate, the palace secret: in the data or not?
- **Read:** `hintbook.txt:5698-5702`; L9 item and control rows.
- **Done when:** For each: the item or control id and how it opens, or 'absent' with the evidence.
- **Unblocks:** M-22 (D4: list, do not invent).
- **Depends on:** none

### Q26. L12: tiger cave and lake platform triggers
- **Question:** Your F-11 note says these are not region event 1 or 4 records. What are they?
- **Read:** `grok_research/F11_region_events_20261110.md`; `native_scripts/L12_CM.json`.
- **Done when:** The record kind, event and groups for each, and what stops them today.
- **Unblocks:** M-12.
- **Depends on:** none

### Q27. L12: gorilla groups stop at opcode 210 arm 10
- **Question:** Decode arm 10.
- **Read:** `F11_region_events_20261110.md` (groups 1218-1868); `A01_music_20261110.md` (opcode 210 at file 0x9C954).
- **Done when:** What the arm does; hosted as a no-op or as the real call, with a test that the six groups run to their end.
- **Unblocks:** M-12; A-02.
- **Depends on:** none

### Q28. L12 arrival from the Larkhon cave
- **Question:** What does the original play or say when Luther first arrives in the Claw Mountains?
- **Read:** First-entry groups in `native_scripts/L12_CM.json`; longplay frames at the first L12 minute.
- **Done when:** The groups with their speech and movie requests, and what the port plays today.
- **Unblocks:** BJ14 N3 (no line on arrival).
- **Depends on:** none

### Q29. Dawn at the gulch (L12 event 4)
- **Question:** With event 4 now fired, does the Dawn-at-the-gulch group run to its end?
- **Read:** Memory of BJ05: 'Dawn-at-gulch event-4 unhosted'; `native_scripts/L12_CM.json`.
- **Done when:** A chain-fire print for that group: runs, or stops at which opcode and arm.
- **Unblocks:** M-12.
- **Depends on:** Q13

### Q30. L14 event-9 regions
- **Question:** 31 unique kind-12 records on L14 use event 9. What are they for?
- **Read:** `R02_region_event_bytes_20261110.md`; `native_scripts/L14_HT.json`.
- **Done when:** A table of the 31: region, byte +7, group, what the group does; which need the height argument.
- **Unblocks:** F-11; M-14.
- **Depends on:** none

## Part B: release blockers

### Q31. Music: which archive slot is which stem
- **Question:** 33 AUD entries, 34 stems, mapping UNKNOWN (name hashes missed).
- **Read:** `grok_research/A01_music_20261110.md`; LOCAL.MIX (33 HMI entries and their order); track lengths.
- **Done when:** A table slot -> stem with a grade per row. Try: the Westwood id hash over other path spellings, slot order against the HMI order, and length against the HMI song length.
- **Unblocks:** A-01 acceptance; A-02.
- **Depends on:** none

### Q32. Music: the trigger table
- **Question:** Turn the 108 opcode-210 commands in 48 groups into a per-level table.
- **Read:** `A01_music_20261110.md`; `native_scripts/*.json`.
- **Done when:** Rows: level, group, the record that raises it (region, control, timer), arm, stem. Mark the 74 'none' rows.
- **Unblocks:** A-02.
- **Depends on:** none

### Q33. Opcode 210 arms 4-9
- **Question:** They store a scaled word; 'volume' is LIKELY. Settle it.
- **Read:** `A01_music_20261110.md`.
- **Done when:** What reads the stored word (fade, volume, tempo) with the read site.
- **Unblocks:** A-02.
- **Depends on:** none

### Q34. Music converter producer (small tool with a test)
- **Question:** Write the producer that turns the player's DMUSIC.MIX into 33 audio files outside the repo.
- **Read:** Your in-memory decoder; `tools/` producer conventions; the F-03 staging tool.
- **Done when:** One command, no machine paths, output hashes in a manifest, a test that decodes one track and checks length and peak. Nothing original is committed.
- **Unblocks:** A-01; X-02.
- **Depends on:** Q31 for names (numbered files are fine until then)

### Q35. Converter input manifest
- **Question:** Which original files do the producer tools read?
- **Read:** `tools/prepare_*.py` and the other producers; `~/lol2_runtime_root/`.
- **Done when:** A table: original file, size, sha256, which producers read it. List producers that read a machine path.
- **Unblocks:** X-01, X-02.
- **Depends on:** none

### Q36. How to recognise the player's copy
- **Question:** What tells a GOG copy from a CD copy, and which files does a launch check need?
- **Read:** LOLG.EXE / LOLG.DAT (pinned sha256 in your A-01 note); the install's file list; version strings.
- **Done when:** The identifying strings and hashes for this copy and what would differ on a CD copy (LIKELY is fine, say so).
- **Unblocks:** X-01.
- **Depends on:** none

### Q37. OPTTEXT.TRR and ERRTEXT.TRR
- **Question:** Decode both string tables.
- **Read:** The two files in the runtime root; the TRR reader used for CREDITS.TRR if one exists.
- **Done when:** Two tables in `grok_research/` with every string; for options, the value range from OPTIONS.INI.
- **Unblocks:** F-21; U-04; X-10.
- **Depends on:** none

### Q38. Movie audit, part 1: the 85 opcode-21 names
- **Question:** Which of the 85 names exist in the player's MIX files?
- **Read:** `grok_research/BK10_movies.md`; `native_scripts/*.json`.
- **Done when:** A table of 85: name, level, group, in which archive or absent, converted or not.
- **Unblocks:** S-20; U-02.
- **Depends on:** none

### Q39. Movie audit, part 2: shell reels
- **Question:** Intro, teasers, endings, credits: which files, and what plays them?
- **Read:** The runtime root's movie archives; the manual's Extras section (`gog_manual.txt:1874-1890`).
- **Done when:** A list of the shell reels with archive, length and the code that requests each.
- **Unblocks:** S-20; U-01 (Extras); S-12.
- **Depends on:** none

### Q40. Room archive audit
- **Question:** 46 room-view stems: which are referenced by a script and which are not?
- **Read:** S-23's stem list (SHBAK, HUT1/2, DSLAVE, SLAVES, BALCONY, HIVE1-3, SETTLE2-4 and the hosted ones); opcode requests in `native_scripts`.
- **Done when:** A table of 46: stem, archive, referenced by which group, hosted today or not.
- **Unblocks:** S-23; M-10 (village views).
- **Depends on:** none

## Part C: the rest

### Q41. Speech census, Act 2 first (L8, L9, L10)
- **Question:** Every opcode-20 speech request on these three levels against what the port plays.
- **Read:** `native_scripts/L8_SJ.json`, `L9_DR.json`, `L10_DC.json`; the 716 converted WAVs.
- **Done when:** A table: level, group, clip, raising record, played by the port (yes/no).
- **Unblocks:** S-02; S-04.
- **Depends on:** none

### Q42. Speech census, L12-L14
- **Question:** Same for L12, L13, L14.
- **Read:** Same sources.
- **Done when:** Same table.
- **Unblocks:** S-02.
- **Depends on:** none

### Q43. Speech census, L16-L20
- **Question:** Same for L16, L17, L19, L20.
- **Read:** Same sources.
- **Done when:** Same table.
- **Unblocks:** S-02; S-05.
- **Depends on:** none

### Q44. Speech census, Act 1
- **Question:** Same for L1, L3, L4, L5, L7.
- **Read:** Same sources.
- **Done when:** Same table.
- **Unblocks:** S-02; S-03.
- **Depends on:** none

### Q45. Level-5 spells: the charge cost
- **Question:** Do Regenerate, Trinity, Banish and Expel take an Ancients' Stone charge per cast?
- **Read:** `hintbook.txt:505-507`, `1143-1145`, `1294-1296`; `scripts/lol2/ancient_stone_effect.gd`; the cast path.
- **Done when:** The read and decrement site, or the proof there is none.
- **Unblocks:** R-22; R-11.
- **Depends on:** none

### Q46. No-target fizzle
- **Question:** Where does a spell with no target fizzle and keep its mana?
- **Read:** `hintbook.txt:510-511`; the cast path.
- **Done when:** The check with its site and which spells it covers.
- **Unblocks:** R-22.
- **Depends on:** none

### Q47. Item numbers, the rest
- **Question:** Charges, price, weight and description text stayed UNKNOWN in I-03.
- **Read:** `grok_research/I03_item_numbers_20261110.md`.
- **Done when:** For each of the four: the definition offset and reader, or UNKNOWN with what was tried. One task, stop at four hours.
- **Unblocks:** I-03; I-14 (shops).
- **Depends on:** none

### Q48. Compass
- **Question:** What does the HUD compass do natively?
- **Read:** `scripts/lol2/museum_interface.gd:389-392`; `gog_manual.txt:91`, `924-926`.
- **Done when:** The draw or action site, or proof it is only the heading spot.
- **Unblocks:** U-08.
- **Depends on:** none

### Q49. Imp altar drain
- **Question:** The owner remembers a drain 'from the altar in the top levels'. Find it.
- **Read:** `grok_research/BK13_guck_effect.md` (the liquid-effect switch and its callers).
- **Done when:** The record that produces it, or 'none found' with the call sites searched. The owner checks DOSBox in parallel.
- **Unblocks:** M-23.
- **Depends on:** none

### Q50. L16 Secret Storeroom
- **Question:** Find the storeroom's rows.
- **Read:** `hintbook.txt:4975-5011`; `native_scripts/L16_CA.json`; `docs/DEVIATIONS.md:489`.
- **Done when:** Regions, controls, items and groups for the force field, the statue chip, the ball of light and the key; or absent.
- **Unblocks:** M-21.
- **Depends on:** none

### Q51. L16 chalice dream
- **Question:** Find the 'Hall of Alchemy' rows.
- **Read:** `hintbook.txt:5017-5030`, `1169-1173`.
- **Done when:** The trigger (mandrake in the chalice), the timer and the room; or absent.
- **Unblocks:** M-21.
- **Depends on:** Q12 for timers

### Q52. L16 Transformations-R-Us
- **Question:** Find the exhibit rows.
- **Read:** `hintbook.txt:5052-5069`.
- **Done when:** The transmutation table (item in -> item out) and the door rows; or absent.
- **Unblocks:** M-21; I-12.
- **Depends on:** none

### Q53. L16 Silverleaf chasm
- **Question:** Find the chasm rows.
- **Read:** `hintbook.txt:5073-5109`.
- **Done when:** The pedestal chip, the light's branch, the floor timer and bell; or absent.
- **Unblocks:** M-21.
- **Depends on:** none

### Q54. L16 chip quests, 1: Water Torture and Leap of Faith
- **Question:** Find both rooms' rows.
- **Read:** `hintbook.txt:5115-5203`.
- **Done when:** Triggers, timers and prize rows for the two rooms; or absent.
- **Unblocks:** M-21.
- **Depends on:** none

### Q55. L16 chip quests, 2: Dancing in the Fountain and Be a Blockhead
- **Question:** Find both rooms' rows.
- **Read:** `hintbook.txt:5115-5203`.
- **Done when:** The five freeze methods as native checks, the box rows and the ceiling trap; or absent.
- **Unblocks:** M-21.
- **Depends on:** none

### Q56. L19 locals 0 and 2
- **Question:** Who writes and reads them?
- **Read:** `grok_research/BK18_chain_split_20261110.md`, `BK17_main_chain_stops_20261110.md`.
- **Done when:** Writer and reader groups for each local and the player action behind the write.
- **Unblocks:** C-12.
- **Depends on:** none

### Q57. L19 locals 3 and 9
- **Question:** Same question.
- **Read:** Same notes.
- **Done when:** Same.
- **Unblocks:** C-12.
- **Depends on:** none

### Q58. L19 local 11 and gate index 52
- **Question:** Same question, and which group writes index 52.
- **Read:** Same notes.
- **Done when:** Same, with the group that writes 52.
- **Unblocks:** C-12.
- **Depends on:** none

### Q59. L20 opcode 2 arm 0x23
- **Question:** Enter the callee BK18 left unentered (group 7704).
- **Read:** `BK18_chain_split_20261110.md`.
- **Done when:** What the arm does; hosted with a test or the blocker named.
- **Unblocks:** C-14.
- **Depends on:** none

### Q60. L20 opcode 13 index 4
- **Question:** Actors 46 and 75.
- **Read:** `BK18_chain_split_20261110.md`.
- **Done when:** What index 4 selects; hosted with a test or the blocker named.
- **Unblocks:** C-14.
- **Depends on:** none

### Q61. Soul adds as player actions
- **Question:** Turn the 83 native soul adds into a table of what the player does to earn each.
- **Read:** `grok_research/F10_opcode206_20261110.md`, `BJ04_soul_writes.md`, `soul_events.md`.
- **Done when:** 83 rows: level, group, amount, raising record, the action in plain words, runs in the port today (yes/no).
- **Unblocks:** S-11; S-10.
- **Depends on:** none

### Q62. L13 basin: the 39 dormant rows
- **Question:** What wakes them?
- **Read:** `act2_populations/L13_RC.json` (scripted_dormant, wake_targets).
- **Done when:** The rule (flag bits and waking record) and five worked rows.
- **Unblocks:** M-13; I-13.
- **Depends on:** none

### Q63. L4 global 0x223D6
- **Question:** Region 3205 group 6292 does not commit while this global is unknown. What is it?
- **Read:** `F11_region_events_20261110.md`.
- **Done when:** Writers, meaning, and the value at level entry.
- **Unblocks:** F-11; M-04/M-05 (Jungle).
- **Depends on:** none
