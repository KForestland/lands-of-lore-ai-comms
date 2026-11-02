# ASTRA task G (lead: Opus), 2026-11-02: STORY-007 UNBLOCKED -> L10 Cemetery chain

Your 19:05Z block on STORY-007 is lifted. Grok answered at 19:15Z: ~/AI_COMMS/review_20261101/l10_tomb_doors.md
- Receptacle 87 -> doorway control 88 (template 22, (1084,4097), heading 16384, solid 131x50x100).
- Receptacle 91 -> doorway control 92 (template 22, (-102,2495), heading 49152).
- Same split on the other rows: the template-22 control next to each receptacle is the door. The template-51 neighbours
  (76, 63) are NOT doors. Controls 125/126/127 are not doorways.
LEAD DECISION (owner workaround rule): bind the matching-colour globe -> consume -> door opens as a MODERN adapter.
Selector 1 = open. Door motion = adapter matching the longplay (no decode). One DEVIATIONS piece. Decoy globes
(swords inside) are refused without loss.

Base: astra-progression c497c9d. r12x (your 252fbbd + STORY-001..003 + KIT-CHARGER) is being qualified by the lead now.
Rebase onto r12x-integration 3cd04ee if you need it (it adds only an item_definitions_test pin: 296 Act 1 ids, for your
L8 Dracoid Sigil).

Order (backlog, claim each with BACKLOG/backlog.py): STORY-007 -> STORY-008 ... -> STORY-027, then ROUTE-TEST
act2_silverleaf_earned_loop_test (milestone 1). Use the mechanism transaction API (scripts/lol2/mechanism_transaction.gd)
for every receptacle/charger. Same rules as before: headless, earned saves, no seeding, adapters logged, CHECKPOINT on the
board after each READY slice, status/astra.md current. If a step needs a number no source gives, ask Grok in ONE board line
and go on with the next independent step meanwhile.

## Extra capacity (owner 2026-11-02: Astra has 2 resets; Fable unavailable)
- Keep going past ROUTE-TEST: STORY-028 onward in order (L8 silverleaf return, L12, L13 dreamstone, L8 temple ...).
- If your chain blocks and Grok has not answered yet, pull a Fable item meanwhile (lead hands these over while Fable is
  out): item handler hosting behind scripts/lol2/item_handlers.gd for the items your slices use (globes, urn, ankh,
  bracers, silverleaf, amaranth potion). Claim it on the backlog with lane astra and post a board line.
- At each reset: re-read this file + the board tail + status/astra.md, then continue. No re-planning needed.
