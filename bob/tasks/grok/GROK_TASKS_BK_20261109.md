# List BK (lead: Opus), 2026-11-09 — make Act 3 walkable (from Fable's BJ10 survey)
Source: fable_lane/bj10_20261109/NOTES.md "Mechanics for the lead" (11 items) + grok_research/act3_chain_status.md.
Lead rule: these restore NATIVE behaviour the port has not hosted yet (not new mechanics) -> build them from the original
data; if a step has no native evidence, log it as an adapter that matches the longplay (owner workaround rule) and say so.
Order = the walk order (L17 -> L19 -> L20). Earned walks like a player; ledger pieces one row each; Kimi before merge.

FABLE (geometry/presentation/body):
BK01 L17 throat (-4616,-2094) region 562: 38-40 units of clearance stops Human AND a 16-unit Lizard (stall at
  (-4589,32,-2087) on a down-facing face). Find why (collision ceiling vs the native gap); the original mover is region-based,
  so a linked region path must be passable by the form the original uses (longplay g_00360: Lizard). Fix the collision, not
  the body sizes, unless the native body data says otherwise.
BK02 L19 bloody room: no geometry over the pool (player falls out of the world) -> pack export gap; fix the export/pack.
BK03 L19 guck channel / pool: blocked -10/-100 pairs are walls; host them as the native hazard/dam floors where the data shows.

GROK (native hosts):
BK04 L17 beast scene relocation (STORY-080): cutting the strands carries Luther from the pocket into the exit block
  (regions 1279-1314; region 1312 = L19 arrival 1). Decode the native carry (opcode 18 / group) and host it.
BK05 L19 bars + gutter (STORY-082): movable 77 move, gutter volume, Lizard form change in L19 (like L14's lower passage).
BK06 L19 switch shooting: controls 74-76 across the guck need a real bow shot (aim + projectile hit), not E at an anchor.
BK07 L19 elevator to Dawn (shaft -150 -> -975) and the L20 mother door after the birth ("DOOR = -1").
BK08 L20 "attack the door" (READ grok_research/kimi_K55.md FIRST; lead decision: generic struck binder in act2_progression, not a per-door host; the doors are pairs 50+51 and 53+54, plus 55+99; three adapters logged; exclude bespoke-hosted controls; save the record_state or log the reset): wire kind-9 STRUCK events to melee hits on movables 50-54 (predicate owner-state 0) so the
  chase route opens natively.
BK09 L20 blue pillars path (STORY-088) across the chasm and the moving pillars (STORY-089) over the 419-unit gap to the armory.
BK10 research: are hw01.vqa / placenta.vqa / e224e.vqa in the MIX files? If yes, stage them like CITY/CITADEL.
Spells (Trinity, Mists of Doom 1, Curse 5) as real casts stay in the backlog (SPELL-*) unless a walk needs them.

## Added 2026-11-09 from Grok's BJ09 stop (L16 comes before L17 in the walk order -> do these FIRST)
BK11 (grok): L16 doors 80/81/98 do not move and the greenhouse nav does not reach the SE oil room; the floor where the walk
  stops (15557,32,4132 region 7669) does not connect to the SE oil. Decode the native door moves (opcode 1/18 on the drain
  mouth / flame) and the link; host them so the walk reaches the oil fountain.
BK12 (grok): L16 box, disk and yellow figure have zero placements, and the Mantle Gate is unbound (door id -1). Find their
  native placement/presence (or the event that spawns them) and bind the Mantle Gate to its native door; adapter only where
  the data has nothing, logged.
Order for Grok: BK11 -> BK12 -> (BJ09 walk on to the L17 exit) -> BK04 ...
BK13 (grok, research, when free): decode the L19 guck effect on the player (liquid materials 211/265: damage? mana drain? rate per tick?) so Fable's guck host can use native values (lead removed the invented 1 mana/0.5 s + 1 health/4 s).

## LEAD DECISION 2026-11-09 (from Kimi K60): build the missing NATIVE ENGINE pieces first, then BK05-BK07 mostly run from data
BK00a (grok, before finishing BK05): opcode 196 handler (region floor motion: word +2 region, word +4 target height, byte 7
  rate; stage like 197, world side animates the region floors and carries the player) - G97 step4_op196 REPORT.md has the
  proven store list.
BK00b: opcode 207 handler (local counter add: signed byte 5 onto local slot byte 4; H13 note).
BK00c: opcode 199 handler (the L19->L20 gate write 0x26E58[52]; retire the preview seed act2_progression.gd:28-30).
BK00d: an opcode-18 PLAYER consumer: when a staged opcode-18 targets the player (kind 1, target 0, flags 0x0004 absolute
  horizontal words, 0x0100 height), move Luther there with the heading - this retires pose adapters (BK04 region 1293, the
  L16 centre pads, the birth relocation group 770). Keep each existing adapter until its walk passes on the native path.
Each: unit test of the handler + the affected earned walks re-run; ledger rows (native, not adapter). Then BK05/BK06/BK07 per
grok_research/kimi_K60.md (bow-shot binding on movables 74-76 is the only genuinely new mechanic there).
BK00e (grok, from Kimi K61 problem 1, BEFORE retiring any pose adapter): the 0xB7D5E opcode-18 slot is filled by any opcode-18
  command but cleared only by player poses; per your own decode the native reader (0xB2ACA) clears after EVERY command. Clear
  the slot on every consumed command (player or not) so later native player poses still fire; unit test with a non-player
  op18 followed by a player op18.
BK00f (grok, FIRST - r19-bk sweep regressions from BK00a, Kimi K61 problem 4): claim_moving_floors turns the floor faces of
  EVERY opcode-196-targeted region into deck meshes in every binder level at load. The r19-bk sweep (bksh_*) fails:
  l10_progression_test ("all source mover + tomb-door faces left the static mesh (588 vs 578)"), l10_emperor_earned_test and
  l10_silverleaf_growth_earned_test (stop at (3202.7,-18,-1310.1) toward goal (3207,0,-1270), EMPT trigger 3789),
  l9_statue_earned_test + l9_statue_question_earned_test (STAT alcove 3185 point 98 at (2554.9,32,-5960.3)). Fix: claim a
  region as a deck only when a 196 group targeting it actually runs (lazy claim at first motion), or keep the static face +
  collision until then; prove the five tests pass again on r19-bk plus your fix.
BK00g (grok, FIRST): l9_tower_approach_earned_test passes on r19-work 0603225 but FAILS on r19-bk 0f098a7 (after BK00f+e):
  "alcove waypoint (-2921.36, 0.0, -1107.502) from (-3296.155, 32.0409, -1182.057)". Find which BK change (op18 player
  consumer posing on the source-word Tower transport? a 196/199/207 group now running in L9?) and fix; the other 9 L9/L10
  reruns pass after BK00f (tmp/regressions/bkfix).
BK07b/BK08b (from Kimi K63): BK07 restore must claim the cab region decks on a fresh-boot load (saved heights != native) and
  always write local 4 from the save; BK08 header/row 0379: the struck ray reaches MOVABLES only (controls are layer 256) and
  it also arms L9 movables 72-85/131/132 (first sword hit fires their kind-9 records) - say so in the row; L9 earned walks
  must be in the merge sweep.

BJ11 (fable, from 2026-11-09 afternoon): with r19-bk 8601810 (engine handlers + L17/L19/L20 hosts + your collision work), walk Act 3
  end to end like a player in as few sittings as possible: L17 arrival (tmp/l17_arrival_earned_save.json) -> throat -> strands
  -> exit block -> L19 arrival -> bars/guck/switches (bow) -> elevator to Dawn -> heads/ruby -> L20 -> mother/birth -> struck
  doors -> blue pillars (grok BK09) -> moving pillars -> armory -> faux Draracle -> Belial -> ending. First stop = finding,
  fix (presentation/geometry yours; mechanics -> lead), repeat. Base: ~/opus_work/lol2_r18 branch r19-bk (read-only;
  your own worktree from it).
BK08c (grok, FIRST, blocks the r19-bk merge): on r19-bk 8601810 the L9/L10/L17/L19/L20 suite is 124/125; l19_bars_strike_test now
  FAILS ("a Human strike runs the bars; region 40 rises to -20 and Luther rises (y -8.0); region 61 rises") - it passed on
  0f098a7 before BK07/BK08/Fable 0001-0003 were added. Likely the BK08 struck binder consumes the left click on movable 77
  (or Fable's region-aware collision on L19 changes the strike ray). Make the bars strike and the struck binder coexist
  (one handler per hit; bespoke L19 bars host wins for movable 77 like the bramble/dam exclusions), rerun l19_bars_strike_test,
  l20_struck_doors_test and the L19 suite on r19-bk.
BK08d (grok, FIRST): Fable's probe (board 2026-11-09 BJ11 for @grok BK08c, tmp/probe_shot.gd in lol2_bj11) shows the PLAYER's real
  left click reaches neither the L19 bars (77) nor the switches 74-76 on 8601810; the tests only pass because they call
  strike_from_camera()/shot_from_camera() directly. On r19-bk d4d0a42 (BK08c applied) prove the real click path: the tests
  must send an InputEventMouseButton through the viewport (like a player) for the bars strike AND the three bow shots; fix the
  input routing (struck binder / _unhandled_input order / set_input_as_handled) so the hosts receive the click.
BK09b (grok, from Fable BJ11 2026-11-09): the five fire shots are recorded on E near AT_57..AT_61 on the WEST side, but the player
  arrives on the EAST lip (region 1477, x -2776) and cannot reach them before the deck exists (the earned test teleports to
  AT_57). Book: "shoot the blue pillars to create a path" from where you stand. Give each pillar a shot hit receiver
  (shot_from_camera, like the L19 switches) reachable from the east lip; earned test without the teleport.
BK08e (grok): L20 doorways: (a) movable 52 sits between 53 and 54 and has no kind-9 record - how does it open natively? (b) the
  50/51 doorway still stops the walk after both leaves travel - check the open pose/collision of the leaves and any blocker
  region. Fable's probe notes in the BJ11 round-4 board line.
BK08f (grok, before BK08e merges; Kimi K69 problem 1): _apply_open_bit drops mover collision for EVERY movable whose +0x15 bit
  0x80 is set, so hosted E-use/enqueue/region-entry groups in L9 (55/58/59), L14 (85/86/87, 58-63), L16 (66) and L19 (61/62)
  now make visually closed doors walk-through. Scope the collision drop to L20 movables 50/51 (the decided adapter), ledger row
  0391 says so; other levels keep their current behaviour until each is checked against the longplay. Also (backlog): BK08e's
  guardian-kill test uses direct strikes - move to real input when convenient; actor:46's caller-0x0B record (group 12398)
  still never fires.
