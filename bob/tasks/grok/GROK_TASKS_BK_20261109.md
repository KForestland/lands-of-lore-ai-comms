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
BK08 L20 "attack the door": wire kind-9 STRUCK events to melee hits on movables 50-54 (predicate owner-state 0) so the
  chase route opens natively.
BK09 L20 blue pillars path (STORY-088) across the chasm and the moving pillars (STORY-089) over the 419-unit gap to the armory.
BK10 research: are hw01.vqa / placenta.vqa / e224e.vqa in the MIX files? If yes, stage them like CITY/CITADEL.
Spells (Trinity, Mists of Doom 1, Curse 5) as real casts stay in the backlog (SPELL-*) unless a walk needs them.
