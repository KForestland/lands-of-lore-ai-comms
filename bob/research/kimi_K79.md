• I have what I need. Everything below was verified against the tree, the data, or the manual; anything I suspected but found covered (weather — not a LoL2 system; first-person weapon art — WPN.MIX/WPNEXT.MIX turn out to be shop *room* archives already inside S-23's 46 stems; particles — the original is sprite-based; save slots/autosave, movies, projectiles, doors/movers, traps, sound buses, performance/memory, Windows) is dropped.

  # Audit: systems and engine gaps in the master plan

  ## Gap 1 — Difficulty levels: a classic gameplay system with no task and no code

  **Missing:** The original has three player-selectable difficulty levels (Easy/Medium/Hard, default Medium) that scale combat. No task builds the option or the scaling, and nothing in the tree implements it.

  **Evidence:**
  - Manual: `AI_COMMS/reference_hintbook/gog_manual.txt:1214-1219` ("There are three difficulty levels… the adjustment of the difficulty level can be made in the Options/Game controls system"), `:1863-1866` ("Difficulty Levels offers three choices; Easy, Medium, and Hard"), `:1914`.
  - Disassembly: `AI_COMMS/grok_research/BK13_guck_effect.md:80` — "Difficulty byte `0xB7FB2` and the scalar argument can change it first" (inside the damage path). `scripts/lol2/hive_damage_calculation.gd:3` already names an upstream "difficulty stage" in an adapter comment.
  - `master_tasks.json` (read in full): no occurrence of difficulty; U-04's option list (line 1650) is "volumes, video (scale, fullscreen, vsync), key bindings, subtitles, UI scale" only. This also undercuts D1/R-01: "use the original numbers" is ambiguous until the decode says which numbers the difficulty byte scales.

  **Nearest task:** R-01 (model) and U-04 (option UI).
  **Proposed task — "Classic difficulty levels (Easy/Medium/Hard)"** (RE: grok; option: sol). Decode what byte `0xB7FB2` multiplies (incoming damage? creature health at spawn?) as part of the R-01 formula decode; expose the setting in Options, persisted in the F-06 save. Acceptance: the owner switches between Easy and Hard and the same Act 2 creature takes a clearly different number of blows; a reload keeps the setting.

  ## Gap 2 — F-11 fires the wrong slice of region events; events 0, 3, 5, 7, 9 have no owner

  **Missing:** F-11 (`master_tasks.json:136`) hosts "region events 1 and 4 (today only event 2)". A census of the exported native scripts shows region kind-12 records with event bytes 0, 1, 2, 3, 4, 5, 7, 9 — and events 0 and 3 are mass triggers, not noise.

  **Evidence:** my count over `scripts/lol2/native_scripts/*.json` (byte +6 of each kind-12 record, the field `native_script_host.gd:855` names the event): **0:478, 1:918, 2:3132, 3:632, 4:1254, 5:4, 7:2, 9:62**. L19 has four records per region — events 0, 1, 2, 3 at 478 each, every one carrying a nonzero group. L14 has 62 records at event 9. Today the binder fires only event 2 (`act2_progression.gd:481`: `fire("region:%d" % index, 2, {})`). The semantics are not even decoded: `grok_research/I31_kind12_timing.md` — "Whether event 2 is enter, stand, or leave. Events 3 and 4. No frame." The plan's "1 and 4" generalizes from L12 (which happens to have 1:12, 4:12); it cannot be right game-wide without a census.

  **Nearest task:** F-11.
  **Proposed task — "Region-event census and full dispatch"** (grok). Per level: table event byte → groups → what raises it natively (entry/exit/standing/direction), then fire each or list it with an adapter. Acceptance: the chain-fire probe reports stops=0 including side regions on L19 and L14, and a player walking in and out of a census-picked L19 region triggers the same groups the original does.

  ## Gap 3 — Native timers and event producers are per-feature adapters; no task builds the clock/dispatch service

  **Missing:** Kind-2 records are the objects' timers, and they are numerous (L20: 1,861; L8: 933; L14: 398 in my count). The host explicitly declines to run them: `native_script_host.gd:102` — "the expiry walk that fires a listed record's group … was not entered: the host … leaves the clock to the world side (adapter kind2_timer_expiry)". Where a timer matters today it is a hand-set per-feature number (`hive_reaver_amber_state.gd:5` — "adapter 7.5 s"). Related: the kind-5 form-change dispatch is decoded (`grok_control_events/FINDINGS.md:69-93` — walker `ADA30` fires kind-5 values 7–12 selected by Luther's form byte), and L4 alone has 114 kind-5 records; R-09/R-18 change forms but no task fires form-gated groups, and F-12's table is per-opcode — a group whose opcodes are all hosted but whose record kind is never raised never appears in it.

  **Nearest task:** F-12 (opcodes) — but this is dispatch, not opcodes.
  **Proposed task — "Native timer and event-producer service"** (RE: grok, build: sol). Decode the expiry walk behind `0xB8BA0` (FINDINGS.md:133-141 replays prop 93's timer, count 300, group 1696), run listed kind-2 records on the game clock, and fire kind-5 form events from the R-18 form change. Acceptance: Museum prop 93's treasure timer fires on its own after the native countdown with no per-area code; changing to Lizard and back fires the form-gated groups the census lists for that area.

  ## Gap 4 — Options parity: gamma, mouse sensitivity, bobbing are absent from U-04

  **Missing:** Classic options the manual documents that U-04's list omits: Gamma Correction, Mouse Sensitivity (slider), Bobbing toggle (manual `gog_manual.txt:1801-1873`; also `OPTIONS.INI` `[Video] Video_Gamma_Correction`, `[Miscellaneous] Mouse_Sensitivity, Bobbing`). Gamma is not cosmetic here — the plan itself tracks owner complaints about darkness (M-08 fixes light sources; a gamma control is the orthogonal, player-side knob).

  **Nearest task:** U-04.
  **Proposed task — "Classic option parity: gamma, mouse sensitivity, bobbing"** (sol, modern; time-boxed look at `OPTTEXT.TRR` for the original ranges). Acceptance: the owner sets gamma and sensitivity in Options, feels both in play, and both persist across a restart.

  ## Gap 5 — Compass: the HUD button is an admitted adapter; the native action was never established

  **Missing:** `scripts/lol2/museum_interface.gd:389-392` — the compass button "opens the atlas (adapter; the native compass action is not established)". The manual describes the compass as a live heading indicator: `gog_manual.txt:91` and `:924-926` ("The blue highlight spot revolves around the Portrait to indicate Luther's current heading"). No task touches it; the plan's "Classic HUD: Yes" row (MASTER_PLAN line 78) papers over it.

  **Nearest task:** M-18 (Atlas v2).
  **Proposed task — "Compass: establish the native behaviour"** (grok, S). Find the native compass read/action in the disassembly or prove it is purely the heading marker; either build the heading indicator or ledger the Atlas-button adapter explicitly. Acceptance: the player can read his heading from the HUD as the manual describes, on every level.

  ## Gap 6 — A-01's music scope names only DMUSIC.MIX; the MIDI/HMI path is unexamined, and the music producer is not in the converter chain

  **Missing:** The install carries a full HMI MIDI stack — `HMIDET.386`, `HMIDRV.386`, `HMIMDRV.386`, `MELODIC.BNK`, `DRUM.BNK`, `TEST1.HMI` in `~/lol2_runtime_root/`, and `OPTIONS.INI [Audio] Audio_Music_Type=Digital` (i.e. Digital **or MIDI**). A-01 (`master_tasks.json:1710`) reads "identify and decode DMUSIC.MIX (81 MB, format unconfirmed)"; if DMUSIC turns out to hold only the digital tracks, the MIDI tracks and instrument banks are a second decode surface with zero existing research (no grok_research note touches music at all). Separately, X-02 chains "the 249 producers" but has no dependency on A-01 — the music decoder has to become a converter producer or X-01's "no original media" acceptance fails on the soundtrack.

  **Nearest task:** A-01.
  **Proposed change:** widen A-01 in place: identify DMUSIC.MIX *and* state which path (digital vs HMI MIDI) the game actually plays per area, including what the .BNK banks are for; add the dependency edge X-02 ← A-01. Acceptance unchanged, plus: the track table records which format each track came from.

  ## Gap 7 — The owner's "altar drain" (D9) has no task

  **Missing:** `OWNER_DECISIONS_MASTER_PLAN_20261110.md` line 14 (D9) records a second drain: "a drain 'from the altar in the top levels': not identified yet". M-16 (`master_tasks.json:716`) covers only the L19/L20 guck drain and its switches. No task identifies the altar drain.

  **Nearest task:** M-16.
  **Proposed task — "Identify the altar drain"** (grok, S). Search the drain call sites (the BK13 liquid-effect switch and its callers) for an altar-triggered variant in the upper-level archives; either host it under M-16 or bring the owner the evidence that it does not exist so D9 is closed. Acceptance: the owner is shown the native record that produces the drain he remembers, or signs off that there is none.

  ## Gap 8 — No player-facing failure behaviour anywhere

  **Missing:** What the player *sees* when something is broken: a corrupt save slot, a failed or half-finished conversion, missing media at runtime. F-06's "strict validators" (MASTER_PLAN line 68) say saves are rejected, not what rejection looks like; U-03's acceptance never shows a bad slot; X-01's manifest verifies at conversion time but nothing covers in-game behaviour when a file is absent. The original ships its own error text (`ERRTEXT.TRR` — unexamined by any tool or note).

  **Nearest task:** X-01.
  **Proposed task — "Failure surfaces"** (sol, modern, S). Corrupt a slot → the Load screen says so and offers the autosave; conversion fails → the report names the failed producer and the fix; a missing asset in-game → placeholder plus log line, never a crash. Acceptance: delete one converted file on a clean install, start the game, and reach a message that names the file and the remedy.

  ## Gap 9 — Fog/distance shading has no owner

  **Missing:** Fog exists only as per-level handiwork: `dark_halls.gd:124-139` (exponential black fog matched to longplay 75:18), `player_water_view.gd:3-7` (underwater fog), `l8_night.gd:10-23` (night "fog_only" fade). M-17's review names "clipping, textures, sky, sector light" (`master_tasks.json:731`) — never fog — and M-08 is Act 1 light sources only. Outdoor distance fade on L8, L12 and L16 against the longplay is nobody's task.

  **Nearest task:** M-17.
  **Proposed change:** widen M-17 in place to name fog/distance shading per level with a longplay reference per outdoor level. Acceptance: the owner signs off the distance fade on L8, L12 and L16 against the same longplay minutes, or each difference is ledgered.

  ## Gap 10 — Extras/movie replay from the menu (minor)

  **Missing:** The original's Extras menu replays the intro, the teasers and the credits from the shell (manual `gog_manual.txt:1874-1890`). U-02 plays the intro only on New Game; U-07 covers credits. No replay path exists, and S-20's audit table will hold the converted reels with no player way to re-see them.

  **Nearest task:** U-01.
  **Proposed change:** fold into U-01/U-02: an Extras entry that replays the intro and any already-seen movie. Acceptance: the owner re-watches the intro from the main menu without starting a new game.

  ---

  ## Reverse-engineering jobs still needed, ranked

  Ranked by what blocks the most downstream work or the release itself. Lanes per the plan's split (grok = native data/decode, sol = engine build).

  1. **Combat damage formula, including the difficulty byte `0xB7FB2`, and creature-health units** — grok. (R-01/R-02 + Gap 1.) Blocks all of P4 and is the plan's own risk #2; the difficulty byte is inside the same unfinished formula (`BK13_guck_effect.md:80`), so one decode pass should answer both.
  2. **Music: DMUSIC.MIX format + whether the HMI/MIDI path (.BNK banks) is a real source + per-area/event track triggers** — grok. (A-01, Gap 6.) A hard 1.0 gate since D10; zero research exists today; start immediately as the plan says.
  3. **Event-dispatch census: region event bytes 0/1/3/4/5/7/9 semantics (enter/stand/leave are open per I31), kind-5 form dispatch, kind-6 producers** — grok, then sol for the binder. (Gaps 2 and 3.) Main-chain groups hide here; cheaper than discovering them one stop at a time in the L9–L14 surveys.
  4. **Kind-2 timer expiry walk (0xB8BA0 chain) and the countdown clock** — grok. (Gap 3.) Replaces a growing pile of hand-set timer adapters with one service.
  5. **Opcode remainder in chain order, incl. confirming opcodes 17 and 206 from the disassembly** — grok. (F-09/F-10/F-12; already tasked — confirmed correctly scoped and correctly early.)
  6. **L19/L20 unread locals and the chain predicates** (locals 0/2/3/9/11, gate 52, opcode 2 arm 0x23, opcode 13 index 4) — grok. (C-12/C-14; already tasked and correctly placed as the P1 blocker.)
  7. **Item definition numbers: the 21 undecoded bytes (damage, speed, charges, value)** — grok. (I-03; already tasked; correctly ahead of the I-04 batch.)
  8. **L16 towers: one more day on the native rows before the book/longplay adapter** — grok. (M-15/D5; already tasked with the right time-box.)
  9. **Movie and room-archive audits: which of the 85 reels and 46 stems actually exist in the player's MIX files** — grok. (S-20/S-23; already tasked; audit rather than decode, but it gates S-12/S-21/S-22.)
  10. **Altar drain identification** — grok, small. (Gap 7; needed to close D9 cleanly.)
  11. **Compass native action** — grok, small. (Gap 5.)
  12. **`OPTTEXT.TRR`/`ERRTEXT.TRR` string tables** — grok or sol, small. (Gaps 4 and 8; original option ranges and error texts, useful and cheap.)

  A note on what is *not* a gap, since the plan gets credit for it: the F-12 chain-fire probe design means main-chain opcode gaps cannot stay hidden, X-01/X-02 correctly treat the converter as a release blocker rather than an afterthought, and the R-recovery removal order in §2.5 is internally consistent with F-15/F-18/U-05. The two findings I weight highest are Gap 2 (632 event-3 region records and a full 0/1/2/3 set per L19 region, against a task hard-coded to events 1 and 4) and Gap 1 (difficulty is decoded-adjacent, player-facing, classic, and absent from all 127 tasks).
