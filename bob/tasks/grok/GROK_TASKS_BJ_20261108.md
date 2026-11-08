# List BJ (lead: Opus), 2026-11-08 — Darker Jungle (L8) main chain, then Act 2/3. AFTER list BI and the Atlas fixes.
Owner 11-08: Act 1 is almost done; next focus the Darker Jungle, then Act 2 and 3 maps and quest progression.
Gap audit: grok_research/kimi_K45.md (backlog statuses may be stale -> PROVE each with a walk, do not trust 'todo').
Method: one owner-like EARNED WALK first, fix what it hits, in order. Base: r19-work (or r19 when built). Rules as always
(meta duck line, like a player, ledger pieces, typed vars, registry, affected tests PASS).

BJ00 (grok, FIRST after BI10 - owner 2026-11-08): the owner skips Act 1 and tests from Act 2 (F2 playtest start "darker"),
  aiming for the Claw Mountains. Owner: "the temple is closed since the priest is killed beforehand". WATCH THE LONGPLAY and
  draw conclusions: frames every 30 s from 109:40 in ~/lol2_original_screens/longplay_frames_act2plus/g_N.jpg
  (index notes: memory lol2-act2plus-survey; full video on Arikv, see reference-lol2-longplay-video). Write the original L8 route
  as the player sees it, step by step with frame numbers: arrival -> Huline Temple (what happens to the priest, is the temple
  open or shut afterwards, what opens next) -> village -> Larkhon -> the way to the Claw Mountains (L12). Then compare with our
  build (r19-work) from the "darker" playtest start: where does our flow differ or dead-end (is the temple shut before the visit
  ran? does the village still need the visit?). Report on the board + grok_research/l8_longplay_route.md; then fix the first
  dead end (BJ01 continues from there). Mechanics changes -> lead/owner.

BJ01 (grok): L8 main-chain earned walk, from the Act 1 departure save into L8 to the exit to Claw Mountains:
  arrival -> Daniel's blade -> Huline Temple visit -> village admitted (guard) -> shaman / cache / tree bridge / platform ->
  Larkhon put to sleep -> passage to L12. Save/reload at each step. The FIRST place it stops = a finding (report on the board
  with position + reason), then fix it (or ask the lead if it is a mechanics question). Repeat until the walk reaches L12.
BJ02 (grok): close or confirm PT3-L8-LARKHON-SLEEP and PT3-L8-PLATFORM with that walk (draft rows 2026-11-03 exist).
BJ03 (fable): L8 map holes: "many walls can be clipped through" (r17 F10 at (1842,2499) and others in TRIAGE_20261107),
  portal effect stays after use; the dark spot (r18 15-37-14 at (-1712,1218)) via a light source (owner lighting rule).
BJ04 (grok, research): L8 soul changes (21 native opcode-206 writes unhosted, SOUL-ADDS-L8_SJ) - list where each fires on the
  chain; host the ones on the main path so later branches read a real value.
Then Act 2 (L10/L9/L12/L13) and Act 3 (L14 STORY-066 hinge, L16, L17/L19/L20) the same way: one earned walk per act, fix in
order. Lead writes those lists after BJ01 reaches L12.

BJ01 DONE 2026-11-08 21:08Z: the darker start reaches native L12/1 by an earned walk (BJ01_l8_chain_l12.patch).
BJ06 (grok, in parallel with Fable's BJ05 on L12): L13 Ruloi Citadel earned walk from the L13 arrival (tmp/l13_citadel_arrival_
  earned_save.json, or Fable's BJ05 output when it lands) along the main chain: globes/egg basin -> elevator -> maidens ->
  Dawn -> pink steps -> bridge -> first Belial -> Dark Sword altar -> Dreamstone -> wall slot + exit lock -> back into L12
  (selector 2). Map from grok_research/kimi_K50.md rows 7-8 (hosts l13_*.gd, all adapters). First stop = finding, fix,
  repeat. Then BJ04 (L8/L12 soul writes on the walked path).
