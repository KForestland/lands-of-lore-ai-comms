# Kimi K35 — Dark Halls puzzles groundwork (read-only, 2026-11-07)

Lead: accepted as the brief for DARKHALLS-PUZZLES. Order: P3 wall slides -> P4 bookcase doors 51/58/59 -> P5 crouch in every area -> P8 crates (also fixes clipping) -> P9 escape blast -> P7 atrium/bell fruit -> P10 orb machine -> P6 trap hardening -> P2 lockouts/bashing. Grok list BH after BG.

All research is done. Here is the groundwork document.

  ---

  # K35 — DARKHALLS-PUZZLES groundwork (read-only)

  **Scope note on naming:** the triage row says "L3_DH", but `L3_DH.MIX` is the Museum level. The Dark Halls detour is **L7_DH** (`DAT/L7_DH.MIX`, scene `scenes/lol2/dark_halls.tscn`, host `scripts/lol2/dark_halls.gd`). Everything below uses L7_DH.

  **Evidence base:** hintbook lines 2398–2550 (`~/AI_COMMS/reference_hintbook/hintbook.txt`), `DARK_HALLS_REQUIREMENT.md`, the 15 r17 `report.json`+screenshots under `~/AI_COMMS/playtest_feedback_20261023/report_2026-11-07T17-*`, the L7 native script dump (`scripts/lol2/native_scripts/L7_DH.json`), the static-slot name table at MIX file 5052795 (47 names, slot 0 `Bookcase1` … slot 22 `Spy Slider`, 32 `Holey wall`, 35 `Windows for Final`, 38 `Slab`, 40 `Iron Door`, 41 `Lockout wall`), and the existing research notes `grok_research/H10_dark_halls_bookcases.md`, `H12_crystal_crate_door.md`, `MAP_L7_DH_legend.md`, `AC05_L7_DH_map_mark.md`, `grok_dark_halls_review_20261023/DARK_HALLS_REMAINING_MECHANICS.md`.

  Coordinates below are native (x, y); Godot z = −native y. Report positions come from each `report.json`.

  ---

  ## P1 — Entry breach (monastery cellar → Dark Halls)

  1. **Intent:** optional side entrance: stack boxes in the monastery storage room, climb, attack the bookshelf to breach into the Dark Halls.
  2. **Contract:** hintbook 2398–2404 ("Stack up some boxes next to the bookshelf, climb up, and attack the bookshelf with a spell or a weapon. You have just breached an entrance into the Dark Halls").
  3. **Hosted?** Shortcut only: MCEL hotspot 1 jumps straight to L7 entry 1 (`docs/DEVIATIONS.md` row 2026-10-21; `dark_halls_route.gd:67-72` `enter_directly()`). Box stacking + strike NOT hosted; native pocket route (L4 region 3205) is bypassed.
  4. **Native ids:** MCEL hotspot 1 → slot 0xE0 (5618, −2369); L4 pocket regions 3190–3233; region 3205 event 4 group 6292 → L7 entry 1 (−3043, 2007), region 47.
  5. **Smallest plan:** keep the shortcut; hosting the pocket + breach is a separate monastery task, not Dark Halls puzzle work. No owner report maps here in r17.

  ## P2 — Ghost population and "You cannot leave, Luther" door lockouts

  1. **Intent:** the halls are a gauntlet of SHADE ghosts; doors slam/lock and Luther chops through them.
  2. **Contract:** hintbook 2439–2444 (fight ghosts one at a time), 2469–2474 (use Spark), 2477–2479 ("Luther may have to chop through a door … 'You cannot leave, Luther!'"), 2492–2494 ("the halls close behind you").
  3. **Hosted?** Partially. 19 SHADEs + 31 Rats spawn awake and hunt on sight (`dark_halls.gd:159-180`, `dark_halls_population_source.json`) — DEVIATIONS 2026-10-21: no region wake groups, cast = close hit with Rat stats. Door bashing (kind 9) and the region-83 door-56 lock are **not** hosted (`dark_halls_doors_source.json` `not_hosted`; `dark_halls_doors.gd:11`). `Lockout wall` (slot 41) is walk-through scenery (DEVIATIONS 2026-10-21).
  4. **Native ids:** actors 24, 58–75 (SHADEs), actor 57 (Rix); door kind-9 hit sequence (selectors 1/2/3, group 13798); region 83 group 76 (door 56 lock); local `Door_destroyed` (movable 56 group 13634); slot 41 `Lockout wall`.
  5. **Smallest plan:** host region wake groups for shades; host kind-9 door bashing on doors 56/57 (3 hits → group 13798, travel word); then the Lockout wall. No direct r17 report; it underpins P6.

  ## P3 — Peephole wall slots ("Spy Slider") — 5 owner reports

  1. **Intent:** small metal slides in walls slide open so Luther can look through (one shows candles).
  2. **Contract:** implicit (hintbook 2433 "click on all the bookshelves to find all the secret accesses" covers secrets generally); Brady printed 84 names "metal slides, and one shows candles" (per `AC05_L7_DH_map_mark.md:11`).
  3. **Hosted?** **No.** Each is a control with two kind-4 uses (predicates 206/207): use 1 = op20 sound 631 + op16 state 1 (open), use 2 = sound 630 + state 0 (close). Control 236's groups also link/unlink prop 465 (op9 prop 0x11/0x12); control 890's groups switch prop 416's selector (op6 byte4 1/2) — the candles (`Candles_lit` candidate).
  4. **Native ids** (found by matching the 5 report positions; a 6th exists unreported):

  | report | native pos | control | groups |
  |---|---|---|---|
  | 17-06-40 | (−2397, 2344) h97 | **1041** (−2378, 2349) | 12468/12490 |
  | 17-09-10 | (154, 3602) h352 | **1013** (159, 3571) | 12380/12402 |
  | 17-09-43 | (−1576, 2704) h352 | **1015** (−1581, 2649) | 12424/12446 |
  | 17-15-00 | (1979, 1294) h462 | **236** (1979, 1270) | 7744/7772 (+prop 465) |
  | 17-15-54 | (3219, 605) h572 | **890** (3221, 568) | 11198/11226 (+prop 416) |
  | — | (−1013, 1971) h343 | **891** | 11254/11276 |

     Static slot 22 `Spy Slider`. Note control 236 sits next to the window family 237–251 but is a slide, not a counting window.
  5. **Smallest plan:** one `dark_halls_slides.gd` on the loot/door adapter pattern: E within reach/facing fires the control's kind-4 pair through the native script host; draw the slide's open/closed selector; log sounds 630/631. State: `quests.dark_halls_slides {control: bool}`.

  ## P4 — Secret bookcase doors (movables 51/58/59) — 3 owner reports

  1. **Intent:** three bookshelves are secret doors that slide aside (Brady: NE bookcase at the end of the first long hall; one at the western end of the southern hallway; hintbook 2526–2528 adds one more before the blue-ball room).
  2. **Contract:** hintbook 2431–2435 ("click on all the bookshelves to find all the secret accesses"), 2480–2481 (Healing Scroll "in the room with the sliding bookcase"), 2526–2528 ("yet another sliding bookcase").
  3. **Hosted?** **No.** All three are static slot 0 `Bookcase1` movables whose motion is undecoded (DEVIATIONS 2026-10-21: "sliding bookcases 51/58/59 … stay walk-through"; `dark_halls.gd:132-141`). H10 decoded their use groups: 51 → group 12512 (op20 sound, op1 percent 100, op9 0x0e); 59 → group 13914 (same shape); 58 → groups 13858/13886 (op1 100/0 + op16 state 1/0, two-use). No grants in the groups; they only open.
  4. **Native ids:** movable **51** (−1177, −570) h750 region 767 ← report **17-19-42** "the books are a door" (−1247, 564*); movable **58** (1778, 3579) h420 region 179 ← report **17-13-57** "a door and not a book case" (1804, 3644); movable **59** (−2528, 3892) h85 region 153 ← report **17-08-18** "press e on the book here open the door\bookchase" (−2544, 3846). (*report y is Godot z; native y = −564.) Loot controls near 59 (968 Healing scroll, 971 Prism) are hosted separately by `dark_halls_loot.gd`.
  5. **Smallest plan:** extend the doors host pattern (`dark_halls_doors.gd` via `native_script_host.gd`, kind-0x20 slot N = movable N) to movables 51/58/59: E fires kind 4; bind op1 percent to a slide translation (motion adapter — byte 34 ≠ 6, so a slide, not a hinge swing); solid while closed. State alongside `dark_halls_doors`.

  ## P5 — Crouch (web crawl) — 1 owner report

  1. **Intent:** low crawlspaces (web-covered) require crouching.
  2. **Contract:** no hintbook line (crouch is a general mechanic; the report screenshot shows a ~half-height webbed opening with a floor grate).
  3. **Hosted?** **No** in the Dark Halls. Crouch exists only in the Museum (`museum_review.gd:211-227`, hold C, Human only; body `player_form_body.gd:10-12` CROUCH_HEIGHT 32). `dark_halls.gd` extends `jungle_walkthrough.gd`, which has no crouch. Webs are slots 13/14/15/33 (`WEB CEILING/FLOOR/FLOOR BIG`, `Lg Web`).
  4. **Native ids:** report 17-07-18 at native (−3054, 2605) h155, near entry 1 (region 47). Native ceiling of the crawlspace regions not yet extracted (verification step).
  5. **Smallest plan:** lift the Museum crouch (`set_crouch`, C-hold) into the shared walk base so every area gets it (the triage action already says "crouch for every area"); then verify the passage's native ceiling admits only a crouched capsule.

  ## P6 — Door-57 trap room ("kill 2 spirits to get out") — 1 owner report

  1. **Intent:** entering the room slams and locks the door; killing the shade(s) unlocks it.
  2. **Contract:** hintbook 2477–2479 (door chop / "You cannot leave").
  3. **Hosted?** **Yes, as an adapter** (`dark_halls_doors.gd:232-278`): grounded entry into region 1338 springs the trap (group 794's op18/op13 not hosted, so only the closing is applied: travel 0, locked), SHADE 73 is moved beside the trap and woken; SHADE 73's death fires actor73 kind6 value10 → group 15750 → unlock. E on the locked door gives feedback.
  4. **Native ids:** door movable **57**, region **1338**, group **794**, actor **73**, unlock group **15750** (15756 unhosted); trap polygon x −1719..−1538, native y 1858–1876, floor 310. Report 17-11-19 at native (−1627, 1956) — the trap room.
  5. **Open fidelity point — "2 spirits":** the bytes wake only actor 73, and only 73's death unlocks. But SHADE **actor 24** (health 120, behavior 6) stands at native (−1307, 2033), ~330 from the room, and our population wakes everything from the start, so in practice two shades converge there. Verify against the longplay whether the original trap involves two shades; if the bytes are confirmed, the owner's "2" is the room's population, not the unlock condition.
  6. **Smallest plan:** host group 794 properly (op18 move + op13 wake via the native host) instead of the closing-only adapter; keep the 73-death unlock; add door bashing (P2) as the alternate escape.

  ## P7 — Solarium/atrium: chains → roof opens → sunlight → bell fruit — 1 owner report

  1. **Intent:** pull the chains, the roof panels slide open, sunlight destroys the two ghosts, and fruit grows in the round bed.
  2. **Contract:** hintbook 2498–2507 ("chains near its entrance … dead trees … Two ghosts await … Pull the chains and let the sunshine in! … the sunlight destroys the ghosts … interesting and clickable fauna grow").
  3. **Hosted?** **No.** Only a static presentation adapter: the bed floors (regions 1435–1504, material 96→97) and the 12 `prop_114` plants draw pre-grown (`dark_halls.gd:18-34`; DEVIATIONS 2026-10-31: "the growth itself (op14 timers) stays with the native host"). The chains are inert scenery; the roof does not move; no sunlight kill.
  4. **Native ids** (report 17-13-29 at native (1695, 3422), matching): chain = control **252** (1878, 3621) h420, kind-5 event → group 8526 (op20 sound 1084 on prop 639 — the click rattle; the roof-opening producer is unresolved). Roof = movables **52–55** at (1659–1917, 2970–3228) h625, kind-6 groups 12564/13062: op18 slide each panel, op9 link sky props 203–210, op6 selector on prop 216, op204 on bed regions 1435–1504, op14 growth timers ×21 on props 217/218, sound on prop 243; group 13490 sets **local0 = 2** (`Atrium_sunlit` candidate) + prop 243 selector 2. `MAP_L7_DH_legend.md` marks control 252 as "Chain". The two ghosts: not pinned to actor ids yet (none of the 18 grid shades 58–75 sits in the atrium; likely a wake/spawn pair — open).
  5. **Smallest plan:** E/click on chain 252 → run the decoded movable groups through the native host (roof slide translation adapter, sky props shown, bed swap, plants grow over the 21 timer steps, sounds logged); kill any shade inside the atrium polygon on "sunlight" (adapter, pending the native kill record); set local0. Verify look against longplay 81:30 frames f_00978/f_00979.

  ## P8 — Crystal crates, the steel (Iron) door, Colin's Amulet / Gauntlets — 1 owner report + 1 clipping report

  1. **Intent:** some crates open to reveal crystals = explosives. Open a crate, shove it next to the steel door, level-3 Spark → door gone; loot inside. Same trick opens the escape (P9). Owner 17-17-34: "exploxe boxes, blow up the wall with scar and break it".
  2. **Contract:** hintbook 2525–2533 ("Take one of the boxes … crystals inside are showing. Move it next to the door … level three Spark Spell. Kaboom! No more door. … Colin's Amulet and Gauntlets of Might").
  3. **Hosted?** **No.** The 89 breakable crates (slots 20/21 `crate 20rwc`/`crate 10rwc`) are walk-through scripted pieces (`dark_halls.gd:132-137`; DEVIATIONS 2026-10-21) — which is also why they clip through each other (**17-18-15** at native (2082, 813): the ~900-series crate controls are placed overlapping). The Iron Door (control **84**, slot 40, (−1243, 614) h750, kind-6 value 21 → group 7656) is walk-through. Colin's Amulet (control **71**, group 7608 op3 grant) IS hosted as a plain E pickup (`dark_halls_items.gd:9`) — the door gating is missing. "Gaunt strike" world-item row 5 is hosted (`area_world_items_state.gd`, AC05).
  4. **Native ids:** crate family = 89 controls with kind-3 (open→crystals, group 8732 shape) + kind-9 value 17 (Spark hit → group 8750 shape: op15 swap, op16 state 2), controls 55–70, 445–453 and the ~900-series clusters at native (1900–2150, 750–1000) where the owner stood. Iron Door control 84; nearest crate 448. Local `Blowout_happens` (named in GLOBAL.MIX, writer not traced).
  5. **Smallest plan:** host the crate two-group shape (E/click = open crystals; Spark receiver like the windows' `Receiver` in `dark_halls_windows.gd:21-26`); give crates solid boxes (fixes the clipping) and a shove/drag adapter (cave_crate_stack precedent); on detonation, fire kind-6 value 21 on control 84 when adjacent (the native broadcast is unproven — H12 lists it as an open point) and damage actors/player in a radius.

  ## P9 — Escape: bricked window at seven o'clock / the crack — overlaps 17-17-34

  1. **Intent:** drag a second crystal crate to the bricked-up window at ~7 o'clock of the round room, Spark it, jump through the hole to the jungle. Rumor: enough light destroys the blue ball (hintbook 2541–2550).
  2. **Contract:** hintbook 2534–2540.
  3. **Hosted?** **Replaced by an adapter:** the hosted exit is the window puzzle (P10): 7 of 15 dome windows → orb ends → window 246 "breaks open" and all 7 exit regions open (`dark_halls_windows.gd:141-153`, `dark_halls.gd:171-173`, `dark_halls_route.gd:63`). The crate-blast escape is NOT hosted. Window **246** (native (−2760, −337), SW ≈ 7 o'clock of the dome) event 3 value 1 → group 8280 = op197 on exit region **1413**. Exit regions 1394, 1408–1413 (floor 700) → L4 entry 6. The owner's crack screenshot at native (2005, 901) is a **different** wall — likely slot 32 `Holey wall` / slot 39 `Hole` scenery near the crate room (Brady's "the crack"); whether it opens natively is unverified.
  4. **Smallest plan:** after P8, detonating a crate adjacent to window 246 runs group 8280 (op197 region 1413) and opens the exits; keep the window-counter route as the alternate original path (hintbook's "rumor" reading). Identify the (2005, 901) crack assembly and check for a native break record before promising it.

  ## P10 — Domed-hall orb machine ("orb levitates and spawns spirits") — 1 owner report

  1. **Intent:** entering the dome, the orb (prop 242) rises to height 900 and starts pulling the grid shades in one by one; the pit floor later rises to 740; opening 7 of the 15 windows destroys the orb (soul +1) and breaks the escape window.
  2. **Contract:** hintbook 2525–2528 ("This huge round room spawns ghosts like there's no tomorrow!"), 2541–2550 (the light rumor).
  3. **Hosted?** **Partially.** Hosted: the 15 window controls 237–251 open on Spark/E (adapter), the "Windows opened n/7" HUD, at 7 the orb ends at once: soul +1, shades 58–75 removed, orb hidden, window 246 lit (`dark_halls_windows.gd:100-163`). **Not hosted** (`dark_halls_windows_source.json` `pit.hosted:false` + `DARK_HALLS_REMAINING_MECHANICS.md`): region **1596** entry → group **1066** (orb rises 370→900, timers start — report 17-21-59's "orb levitates"); orb timers (groups 2022/2040, 24 s/27 s); the one-by-one shade pull (groups 2406…2730, actors 67,68,69,70,64,63,62,61,60,59 → orb → high point → scatter, hostile bits); pit floor rise (group **2792**, op196 regions 1688–1694 → 740, speed 50); the sound-546 gate before group 2082.
  4. **Native ids:** prop **242** (orb, start group 2046, end group 2082), prop 64/70 side actors, regions 1596 (trigger), 1688–1694 (pit), locals 5/7/9, actors 58–75.
  5. **Smallest plan:** implement the review note's section 8 in-memory state machine (enter_1596 → timer expiries → kind-6 raises), wire the pull to the existing creature owner, rise the pit floor with the hive `UNITS_PER_SPEED=2.5` adapter; keep the hosted counter/finish as group 2082's modern stand-in.

  ## P11 — Rix (no r17 report; completeness)

  - **Intent/contract:** hintbook 2510–2517 (plasma-bolt staff, close to melee; staff is poor as a weapon). Hosted: hostile melee fighter, death → soul −1 + GV_RIX_DEAD, E on corpse → Plasma staff (`dark_halls_rix.gd`; DEVIATIONS 2026-10-21/2026-10-30 incl. the fanfix `rix_fanfix_208_207`). Not hosted: talk/give (soul +2 "save Rix" branch — blocked on opcode-2 arm 0x26 conversation lock; original bug makes him unsaveable anyway). Report 17-15-54's slot sits in his hall but is P3.

  ## P12 — Foliage clipping (17-20-11) — presentation, not a puzzle

  - Screenshot: a green vine/foliage billboard z-cutting a wooden post in the crate storeroom at native (−1239, −130) h792. Props are drawn as fixed-Y billboards (`dark_halls.gd:63-77`); identify the prop record and adjust placement/ordering in a refine pass. Not a blocker.

  ---

  ## Owner report → puzzle map

  | report | owner said | puzzle | hosted today |
  |---|---|---|---|
  | 17-06-40 | wall slot/look thingy won't open | P3 Spy Slider control 1041 | no |
  | 17-07-18 | can't crouch/bow down | P5 crouch at the web crawl | no (Museum-only) |
  | 17-08-18 | E on the book opens door/bookcase | P4 movable 59 | no |
  | 17-09-10 | can't open the slot | P3 control 1013 | no |
  | 17-09-43 | can't open the slot | P3 control 1015 | no |
  | 17-11-19 | trapped, kill 2 spirits to get out | P6 door-57 trap (shade 73; shade 24 nearby) | yes, adapter — verify "2" |
  | 17-13-29 | moves the roof, sunlight grows the bell fruit | P7 solarium/atrium | no (static pre-grown adapter only) |
  | 17-13-57 | a door and not a bookcase | P4 movable 58 | no |
  | 17-15-00 | slot not working | P3 control 236 | no |
  | 17-15-54 | slot don't work | P3 control 890 (Rix's hall) | no |
  | 17-17-34 | explode boxes, blow up the wall with spark | P8 crates + P9 breakable wall | no |
  | 17-18-15 | boxes clip through each other | P8 crates walk-through (collision) | no |
  | 17-19-42 | the books are a door | P4 movable 51 | no |
  | 17-20-11 | green foliage clipping | P12 presentation | n/a |
  | 17-21-59 | orb levitates and spawns spirits on entry | P10 region-1596 orb start / shade pull | no (window counter hosted) |

  **Suggested backlog order** (smallest faithful first): P3 slides → P4 bookcases → P5 crouch (shared lift) → P8 crates (fixes 17-18-15 too) → P9 escape blast → P7 atrium → P10 orb machine → P6 trap hardening → P2 lockouts/bashing.

