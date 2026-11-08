# Kimi K45 — Act 2/3 gap audit (L8 -> L20), for the post-r19 phase

Lead note: BACKLOG.md statuses can be stale (e.g. PT3-L8-LARKHON-SLEEP/PLATFORM still 'todo' though draft rows exist 2026-11-03; tree bridge/ladder fixed by BG00a + BI08). Treat each item as 'verify with an earned walk', not as proven open.

## L8 Darker Jungle (ranked)
Ranked gaps for L8:
1. Village gate findability/quest chain: owner blocked twice (11-06 21-12-26 "journey stops here", 11-07 17-53-55 "can't enter the Huline tree village", 11-08 15-32-38 "no cat person here"). Journal note improved but still open (TRIAGE_20261107.md:31 grok BG FIRST). Evidence: TRIAGE_20261106.md:10, TRIAGE_20261107.md:31, TRIAGE_20261108.md:20. Also guard appears only on second approach (TRIAGE_20261107.md:43).
2. Larkhon sleep blocks exit to Claw Mountains — PT3-L8-LARKHON-SLEEP todo P0 (BACKLOG.md:659); ledger 442 says larkhon stays asleep after first dose fix, but backlog still open; plus guidance added (431). Owner 11-03 report.
3. Raised platform doesn't rise — PT3-L8-PLATFORM P0 todo (BACKLOG.md:660); DEVIATIONS.md:466 draft (torch solids stay on layer 1).
4. Tree bridge chop doesn't work in real play (TRIAGE_20261107.md:41, grok BG FIRST; DEVIATIONS 465 draft, 526 walkable fix); cache ladder one-time only (TRIAGE_20261108.md:19 OPEN P?; 464).
5. L8 collision: "many walls can be clipped through" (TRIAGE_20261107.md:44); hedges (DEVIATIONS 550-551, 2026-11-08).
6. Trap not set/hidden (TRIAGE_20261108.md:22 BI10 OPEN).
7. Village guard first-approach (18-06-16).
8. Portal effect stays permanent (TRIAGE_20261107.md:49).
9. SOUL-ADDS-L8_SJ todo (BACKLOG.md:178) — 21 native soul changes missing, so good/evil state wrong downstream.
10. Too dark spot (TRIAGE_20261108.md:21, LATER Fable).
11. Silverleaf loop is the only done route test (ROUTE-TEST done, BACKLOG.md:46) — rest of L8 journey is draft/adapter E-panels (DEVIATIONS 327-328).

## Act 2 levels (L9, L10, L12, L13)
L9_DR:
- dragon_level.tscn not a maps/ pack; preview OPEN with "no progression scripts" originally (DEVIATIONS:207), progression attached via act2_progression but everything adapter.
- PT-L9-WALLS done (owner: walk through walls) — region wall ownership (416).
- STORY-011..014, 024-027 done-astra on cards; act2_route.md lines 29-33 all "not hosted end-to-end" (bridge orb, tower globes, priest ashes, emperor statue, flood escape).
- Flood escape adapters (365, 367, 368).
- Ember/Emperor? Fine.

L10_DC:
- Owner: "a lot of work needs to be done in this map" (TRIAGE_20261107.md:45), missing texture (40).
- Globe charger chain: KIT-CHARGER done; STORY-006..010, 015-023 done-astra; but KIT-RECEPTACLES todo (emperor boxes) (BACKLOG:155) — emperor's tomb (STORY-022) depends on it.
- Barrel: original bug BUG-002 todo (BACKLOG:180); act2_route.md:22.
- Silverleaf growth/harvest done (items), but STORY-030 depends on bracers talking to the dead (ITEM-059 done).

L12_CM / L13_RC:
- Owner L12 reports: stationary stone creature moves (TRIAGE_20261107.md:47), texture issues (48), flame no flicker (46).
- STORY-036..048 done-astra; but ledger rows are drafts (378-399). Ruloi circuit: 19 Ruloi via "real combat" (385). Citadel bridge (388), first Belial (389), sword altar (390), dreamstone exit lock (393).
- CITADEL-BRAIN-CLICK adapter P2 todo (BACKLOG line ~?): "Brain Switch click lowers the citadel elevator" — from the sed tail, near end. I saw "CITADEL-BRAIN-CLICK" in the last backlog chunk. Yes.
- SOUL-ADDS-L12_CM 16 changes todo (170).
- Larkhon passage: STORY-035 done-astra but PT3-L8-LARKHON todo.

## Act 3 levels (L14, L16, L17, L19, L20)
L14_HT:
- STORY-066 todo (BACKLOG:115) — the chalice/city-resurface hinge to Act 3; ledger 446 draft.
- Owner: geometry very wrong, PARKED for Sol/Fable (TRIAGE_20261106.md:9); PT3-L14-TEMPLE (BACKLOG:663); islands rendering (525, 528); portal visibility pop-in.
- Many draft rows 402-428.

L16_CA:
- STORY-067..078 todo (BACKLOG:116-127); drafts 447-453, 463, 483-488, 501-503, 507-508, 521-524.
- "Mantle Gate has zero placements, so the door id stays unbound" (487).

L17_HC / L19_BC / L20_BB:
- STORY-079..093 todo (BACKLOG:128-142); drafts 489-500, 509-520, 529, 531, 533.
- Missing content flagged in drafts: L19 beast wall "No strand row and no frond row are placed. No beast movie number is stored" (490); L19 sewer "Bar door has no placement... No gutter volume is stored" (493); hw01.vqa not in movie_table (520).
- ENDINGS todo (148); BRANCH-01..08 todo (15-25); SOUL-ADDS-L19/L20 (171/173).
- Cross-level handoffs arrival-only predicate adapters (DEVIATIONS 305-310) — e.g., L8->L14 local13 writer UNKNOWN, L19->L20 campaign-start value UNKNOWN.
- SPELL-CURSE-5 todo blocks STORY-087; SPELL-MISTS-1 todo blocks STORY-085; ITEM-022 Hrn Belial todo (STORY-081/092); ITEM-069 Ruby todo (BRANCH-04); ITEM-136 Dreamstone todo though it's used in STORY-041/044/049/066.

Cross-cutting:
- ENGINE-PLAYTEST-STARTS-ACT2 todo P0 (BACKLOG:657) — no resume for map saves, owner must replay.
- KIT-QUESTSTORE todo (40) — cross-level quest persistence.
- NPC-DAWN/BACATTA/RULOI dialog order todo (429/143).
- ACT2-MAP-REVIEW not in BACKLOG.md despite triage saying "-> backlog" (evidence: grep found only in triage files).

## Top 15 overall (ranked, with evidence file:line and one-line task)

Rank by chain-blocking impact:
1. STORY-066 chalice (L14->L16 hinge) todo — BACKLOG.md:115. Task: host the dreamstone-chalice room (CHV) end-to-end with the city-resurface and L16 arrival.
2. L8 village findability/entry: owner stopped twice — TRIAGE_20261106.md:10, TRIAGE_20261107.md:31. Task: in-world guide + guard present on first approach after temple visit, earned test from owner save.
3. PT3-L8-LARKHON-SLEEP P0 — BACKLOG.md:659. Task: earned walk Larkhon dose -> sleep -> passage opens to L12.
4. STORY-067..078 L16 chain todo — BACKLOG.md:116. Task: convert the 11-05/06 draft rows into earned per-tower tests and close the cards.
5. STORY-079..093 final sequence todo — BACKLOG.md:128-142. Task: same for L17/L19/L20.
6. ENGINE-PLAYTEST-STARTS-ACT2 — BACKLOG.md:657. Task: act2_save.gd resume branch so the owner can test maps without replaying.
7. L8 tree bridge + ladder fail in real play (probe-only tests) — TRIAGE_20261107.md:41-42, TRIAGE_20261108.md:19. Task: earned walk tests for control 114 tree and control 69 ladder incl. second climb.
8. Cross-level handoff seeds are arrival-only adapters — DEVIATIONS.md:305-310. Task: trace the native writers (local13, control82, second-array52) and replace the arrival predicates.
9. KIT-RECEPTACLES todo blocks Emperor's tomb (STORY-022) — BACKLOG.md:155. Task: keyed multi-input receptacle mechanism (emperor boxes) with transaction receipts.
10. L14 geometry/portal problems, parked — TRIAGE_20261106.md:9, BACKLOG.md:663. Task: unpark with Sol/Fable or continue portal-visibility islands work (DEVIATIONS.md:525).
11. Soul changes not hosted in L8/L12/L19/L20 — BACKLOG.md:170,171,173,178. Task: host opcode-206 soul writes so branch predicates read real values.
12. Required spells missing: SPELL-CURSE-5 (STORY-087), SPELL-MISTS-1 (STORY-085) — BACKLOG.md:353,359. Task: implement curse L5 and mists L1 effects used by the finale.
13. Key quest items with no handler: Dreamstone ITEM-136, Hrn Belial ITEM-022, Ruby of trth ITEM-069, Ivory chip ITEM-107 — BACKLOG.md:320,206,253,291. Task: per-item handlers per book.
14. L8 collision/map gaps (walls clip, hedges, hidden wall) — TRIAGE_20261107.md:44, 28. Task: static-collision audit for L8 + portal visibility fixes.
15. ENDINGS + BRANCH-01..08 todo — BACKLOG.md:148,15-25. Task: implement soul-driven endings after the linear finale exists.

Wait — some of these conflict: e.g. ENDINGS depends on finale. Order them sensibly by "what would stop a player first". Actually ranked by first-encounter order along the chain makes sense too, but "Top 15 overall (ranked)" presumably by priority. I'll rank by blocker severity × position on chain.

Also L8 section ranked, Act 2 section (L9, L10, L12, L13), Act 3 section (L14, L16, L17, L19, L20). The levels: the task says "For each level on the main chain (L8 first, then L9 onward to L20)". Missing L11/L15/L18 — verified no references (grep empty). Good; I can note the chain skips them (no data).

One more check: DEVIATIONS line numbers 305-310 — I have them from the grep output (lines 305-310 with the arrival-predicate table). Good.

Also confirm the L8 "double-view audit" and "TEMPLE-PORTALS" open. TRIAGE_20261106.md:9 says PARKED for Sol/Fable (TEMPLE-PORTALS stays open). OK.

Also worth noting in L8: "L8 journey" state: the whole first-departure chain is modern E-panels (DEVIATIONS.md:327-328) not native.

Also TRIAGE_20261107.md:44 is "many walls can be clipped through" Darker Jungle (1842,2499). And DEVIATIONS.md:551 hedges open between regions.

Let me double check a couple of line numbers I'll cite in DEVIATIONS.md: 327-328 (L8 first departure), 464-466 (ladder/tree/platform), 525-528 (L14 islands). From the earlier grep: 464 L8 cache ladder draft, 465 L8 tree bridge draft, 466 L8 raised platform draft, 525 L14 Huline Temple islands, 526 L8 tree bridge and cache ladder can be walked, 527 L8 village guard sends Luther to temple. And 202 act2_progression. 305-310 arrival predicates. 490 L19 beast wall, 493 sewer forms, 520 hw01 card. 487 Mantle Gate zero placements. 446 STORY-066 draft. Good.

Cite BACKLOG.md line 3 for the totals? Not needed.

Now write the report. Keep it Markdown with the requested headings. Evidence file:line format.

• All evidence gathered. Here is the audit.

## L8 Darker Jungle (ranked)

1. **Village entry still strands the player** — the owner's journey stopped at the village great tree twice (temple_visited FALSE, journal note too vague), and r17's fix was "owner told the route in chat", not an in-game solution; the follow-up "guard says visit the temple first" is marked grok BG FIRST but not landed. Evidence: `~/AI_COMMS/playtest_feedback_20261023/TRIAGE_20261106.md:10`, `TRIAGE_20261107.md:31`. Related: guard/Daniel appears only on the *second* approach (`TRIAGE_20261107.md:43`), and r18 reports "no cat person here to enter the village" (`TRIAGE_20261108.md:20`, BI09 research OPEN).
2. **Larkhon sleep — the exit to Claw Mountains — is an open P0** — backlog `PT3-L8-LARKHON-SLEEP` (todo): "L8 journey stops; Larkhon must be poisoned/put to sleep" (`~/AI_COMMS/BACKLOG/BACKLOG.md:659`). Ledger rows 2026-11-03 (dose receipt, guidance whisper within 600 units) are draft fixes (`~/opus_work/lol2_r18/docs/DEVIATIONS.md:431-443`), not closed work.
3. **Raised platform does not rise — open P0** — `PT3-L8-PLATFORM` todo (`BACKLOG.md:660`); the draft at `DEVIATIONS.md:466` notes the five torch solids stay on layer 1.
4. **Tree bridge and cache ladder fail in real play (probe-only tests)** — owner r17 17-57-09 "can't chop down the tree" and 18-08-06 "ladder does not work" (`TRIAGE_20261107.md:41-42`); r18 "the ladder only works one time… can strand above/below", OPEN (P?) (`TRIAGE_20261108.md:19`). Drafts exist (`DEVIATIONS.md:464-465`, walk-fix `:526`) but each is grok-BG-FIRST / OPEN.
5. **Whole first-departure chain is modern E-panels, not native** — gift/recovery/temple/guard/shaman are "explicit… modern quest state" bindings (`DEVIATIONS.md:327-328`); only the silverleaf loop has a done route test (`BACKLOG.md:46` ROUTE-TEST).
6. **Collision/map holes** — "many walls can be clipped through" (`TRIAGE_20261107.md:44`); hedge risers not drawn and hedges between regions stay open (`DEVIATIONS.md:550-551`, 2026-11-08); r16 stream-bed gaps went to grok AS04 (`TRIAGE_20261106.md:11-12`).
7. **Trap shown pre-sprung** — should be armed and hidden (`TRIAGE_20261108.md:22`, BI10 OPEN).
8. **21 native soul changes not hosted** — `SOUL-ADDS-L8_SJ` todo (`BACKLOG.md:178`); without them the good/evil value that later branches read is wrong from the start.
9. **Minor:** portal effect stays after use (`TRIAGE_20261107.md:49`); unreadably dark spot parked for the lighting lane (`TRIAGE_20261108.md:21`).

## Act 2 levels

**L9 Dracoid Ruins.** Scene is the one-off `dragon_level.tscn` (not a maps/ pack); its preview row says "no progression scripts yet" and blockers disabled (`DEVIATIONS.md:207`). Every route row is "not hosted end-to-end": bridge orb, tower globes, priest ashes, emperor statue, flood escape (`~/opus_work/lol2_r18/docs/act2_route.md:29-33`). Owner hit walk-through walls in r12x — `PT-L9-WALLS` done, but region-wall ownership work followed (`DEVIATIONS.md:416`). Flood/table/raft and shore return are draft adapters (`DEVIATIONS.md:365-368`).

**L10 Dracoid Cemetery.** Owner verdict 18-14-46: "a lot of work needs to be done in this map" (`TRIAGE_20261107.md:45`), plus a missing texture (`:40`). The Emperor's tomb three-globe boxes (STORY-022, done-card) depend on `KIT-RECEPTACLES` (todo, `BACKLOG.md:155`). The barrel is a known original bug, `BUG-002` todo (`BACKLOG.md:180`), and `act2_route.md:22` flags its interaction/collision/fire trigger as unjoined. STORY-006..023 are "done astra" cards, but the underlying rows are adapters (coloured tomb doors shared-transaction, `DEVIATIONS.md:334`).

**L12 Claw Mountains / L13 Ruloi Citadel.** STORY-036..048 done as cards, but implemented as draft rows (glacier, Kenneth/charm, egg basin, elevator, maidens, bridge, first Belial, sword altar, exit lock, rafts, crevasse — `DEVIATIONS.md:378-399`). Owner r17: the stone creature that should be a stationary turret walks around (`TRIAGE_20261107.md:47`), texture issues (`:48`), flame doesn't flicker (`:46`). The brain-switch elevator is an adapter, `CITADEL-BRAIN-CLICK` todo (`BACKLOG.md` tail row). 16 native soul changes unhosted (`BACKLOG.md:170`). The L8→L12 gate is the open Larkhon P0 above.

## Act 3 levels

**L14 Huline Temple.** **STORY-066 (dreamstone into chalice, city resurfaces — the Act 2→3 hinge) is todo** (`BACKLOG.md:115`; draft row `DEVIATIONS.md:446`). Geometry is so wrong the owner parked it for the Sol/Fable lane (`TRIAGE_20261106.md:9`); temple renders in "islands" with black background (`DEVIATIONS.md:525-528`); `PT3-L14-TEMPLE` (burrows, quill, portal doors) todo (`BACKLOG.md:663`). Steps 049–065 are done-cards over draft rows (`DEVIATIONS.md:401-428`).

**L16 City of the Ancients.** STORY-067..078 all todo (`BACKLOG.md:116-127`); drafts cover elevator, dry fountain, greenhouse, oil fountain, NW traps, ivory pedestals, centre tower, dragon room (`DEVIATIONS.md:447-524`) — but note the self-admitted holes: "Mantle Gate has zero placements, so the door id stays unbound" (`:487`), tower-chain saves load each other (`:501`). Ivory chip item itself has no handler (`BACKLOG.md:291`).

**L17 Subterranean Caverns / L19 Belial's Chamber / L20 finale.** STORY-079..093 all todo (`BACKLOG.md:128-142`). Drafts exist but name missing content: L19 beast wall — "No strand row and no frond row are placed. No beast movie number is stored" (`DEVIATIONS.md:490`); sewer — "Bar door has no placement… No gutter volume is stored" (`:493`); hw01.vqa not in the movie table (`:520`). Required capabilities are unbuilt: SPELL-CURSE-5 for STORY-087 (`BACKLOG.md:353`), SPELL-MISTS-1 for STORY-085 (`BACKLOG.md:359`), Belial's Horn (`:206`), Ruby of Truth (`:253`), Dreamstone handler (`:320`). ENDINGS todo (`:148`); all eight good/evil BRANCH tasks todo (`:15-25`); soul writes for L19/L20 todo (`:171`,`:173`). Cross-level handoffs run on arrival-only predicate adapters whose native writers are UNKNOWN (`DEVIATIONS.md:305-310`). NPC dialogue order for Dawn/Baccata/Ruloi todo (`BACKLOG.md:429`,`:143`).

## Top 15 overall (ranked)

1. **L8 village-entry findability** — owner stopped twice, fix still open. `TRIAGE_20261106.md:10`, `TRIAGE_20261107.md:31`. Task: land the BG-FIRST guard/journal fix with an earned test from the owner's save.
2. **STORY-066 chalice (L14→L16 hinge)** — `BACKLOG.md:115`. Task: host the CHV room end-to-end: dreamstone consumed, city resurfaces, L16 arrival.
3. **Larkhon sleep blocks L8→L12** — `BACKLOG.md:659`. Task: earned walk — mix dose, apply to Larkhon, passage to Claw Mountains opens; close PT3-L8-LARKHON-SLEEP.
4. **L8 raised platform P0** — `BACKLOG.md:660`, `DEVIATIONS.md:466`. Task: make torch-spark raise the platform with a walk test; close PT3-L8-PLATFORM.
5. **Act 2 playtest starts / map-save resume** — `BACKLOG.md:657`. Task: act2_save.gd resume branch so the owner can test L8+ maps without replaying Act 1.
6. **Tree bridge + cache ladder broken in real play** — `TRIAGE_20261107.md:41-42`, `TRIAGE_20261108.md:19`. Task: replace probe tests with earned walks for control 114 and control 69 (incl. repeat climbs).
7. **Cross-level handoff predicates are arrival-only adapters** — `DEVIATIONS.md:305-310`. Task: trace the native writers (local13, control82, second-array52) and remove the seeded arrivals.
8. **Emperor's tomb receptacles** — `BACKLOG.md:155` blocks STORY-022. Task: KIT-RECEPTACLES keyed multi-input doors with transaction receipts.
9. **STORY-067..078 (L16) cards todo over drafts** — `BACKLOG.md:116-127`. Task: promote each draft row to an earned test, starting with the tower chain and the unbound Mantle Gate (`DEVIATIONS.md:487`).
10. **STORY-079..093 (L17/L19/L20) cards todo** — `BACKLOG.md:128-142`. Task: same promotion; first fill the named holes at `DEVIATIONS.md:490,493,520`.
11. **Soul writes unhosted (L8 21, L12 16, L19 1, L20 4)** — `BACKLOG.md:170,171,173,178`. Task: host opcode-206 soul changes so branch/endings read a real value.
12. **Finale-required spells missing** — `BACKLOG.md:353,359`. Task: implement Curse L5 (Expel) and Mists of Doom L1 as used by STORY-085/087.
13. **L14 Temple geometry parked, render islands** — `TRIAGE_20261106.md:9`, `DEVIATIONS.md:525-528`, `BACKLOG.md:663`. Task: unpark TEMPLE-PORTALS with Sol/Fable or continue the portal-visibility island work; requalify PT3-L14-TEMPLE.
14. **Quest-item handlers absent** — Dreamstone, Hrn Belial, Ruby of Truth, Ivory chip: `BACKLOG.md:320,206,253,291`. Task: per-item handlers per book behaviour before the steps that consume them.
15. **ENDINGS + BRANCH-01..08** — `BACKLOG.md:148`,`:15-25`. Task: after the linear finale exists, implement soul-chosen endings and the Baccata/Dawn/Draracle branch scenes.

Two meta-notes: `ACT2-MAP-REVIEW` is referenced as a backlog entry in the triage files but does not exist in BACKLOG.md (grep finds it only in `TRIAGE_20261106.md:10` / `TRIAGE_20261107.md:45`) — worth adding. And the level numbering genuinely skips L11/L15/L18: no scenes, packs, or references exist for them, so the main chain is L8 → L10 ↔ L9 → L12/L13 → L14 → L16 → L17 → L19 → L20.

