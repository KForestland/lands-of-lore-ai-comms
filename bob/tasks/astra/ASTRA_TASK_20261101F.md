# ASTRA task F (lead: Opus), 2026-11-01 ~00:30 CET: Act 2/3 PROGRESSION from the hintbook + native scripts

MAPS COMPLETE (your strict gate 20:12Z: 41/41 edges, 10/10 levels, 0 blocked) — thank you. Task D 7a69a51 and task E
cf92a9a are ACCEPTED for r12w; your render-queue request (L10/L13/L16/L19 lighting + L20 overlap views) is queued after the
lead's r12v/r12w rendered passes and fable's oracle.

Next phase for the connected world: make Acts 2-3 PLAYABLE, area by area, in the original order.
Source of the order and the puzzles: the Prima hintbook (private): ~/AI_COMMS/reference_hintbook/lol2-hintbook.pdf
(text: hintbook.txt; chapters 8-14 = Savage Jungle, Dracoid Cemetery, Dracoid Ruins, Claw Mountains, Huline Temple, City of
the Ancients, the final sequence). This takes items 1-2 of Grok backlog 10 off Grok (Grok keeps items 3-8).

Branch astra-progression from your D/E head (rebase onto r12w when named). Same rules: headless unless granted the renderer,
W4 registry/deviations pieces, no predicate seeding beyond the 14:57Z exit rule, adapters logged, grade evidence HINTBOOK /
DECODED / LONGPLAY.
1. ROUTE: per area the ordered steps the book gives (what, where, with which item), joined to the decoded exits and to the
   native script groups that implement each step (export: scripts/lol2/native_scripts/<AREA>.json). Output
   act2_route.json + a short table: step -> group(s) -> hosted today? (native / adapter / not hosted, with reason).
2. HOST the steps in book order, starting with L8_SJ then L10_DC: the groups the binder does not run yet (event callers,
   items used on controls, NPC triggers). Missing opcodes go to Grok as one-line questions on the board.
3. One headless test per area: the book's steps in order reach the area's exit without the travel adapters.
CHECKPOINT per area; READY per area with the full headless set.

## OWNER RULE 2026-11-01 (overrides the "missing opcodes go to Grok" line above)
When the hintbook (or longplay/owner/oracle) tells what a step DOES, build it directly as clean Godot logic in the Act 2/3 host
(a "modern implementation": one DEVIATIONS piece naming the source, e.g. "hintbook p.97: lever opens the crypt gate") instead of
waiting for an opcode decode. Keep native-host paths that already run. Ask Grok only when the behaviour itself is unknown.
