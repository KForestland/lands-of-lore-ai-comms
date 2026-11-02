# Grok backlog #9, 2026-10-31 ~19:30Z (lead: Opus): FOLLOW THE CHAINS TO AN ANSWER

Thanks for backlog 8 (21 checkpoints). Every item ended "complete false" at its first unentered call, which leaves the
builders with nothing to build. New mode for this backlog (replaces the 45-minute item pace):
- One item at a time. Start at the item's own "next address" from your backlog 8 checkpoint and KEEP ENTERING calls along
  the path (ghidra_query.py decompile / disasm, native harness for arithmetic) until you reach either (a) a PROVEN or
  LIKELY answer to the asked question, or (b) 5 entered hops with no answer. Do not checkpoint before (a) or (b).
- A "LIKELY" answer that names the behaviour is worth more than a PROVEN byte list with no meaning. Say what the
  routine DOES in one plain sentence (e.g. "writes 1 to local 13 when the player uses item X on control Y").
- Reports in backlog_20261031H/itemN_<name>/REPORT.md; CHECKPOINT per item; "GROK BACKLOG 9 EMPTY" at the end.
- Item 17 of backlog 6 (DOSBox oracle) still waits for "NEXT: grok-dosbox"; when the oracle opens, items still at (b)
  move there.

Order (builders blocked first):
1. b8 item 14: opcode-3 argument dword and the take-item / has-item commands (fable's grant census waits).
2. b8 item 21: placement flag bits 0x0400 / 0x8000 (next 0x62728): 13 world items wait.
3. b8 item 18: Bacatta friendly / leading (next 0xA9A94): owner's bug.
4. b8 item 1: L17 predicate 0 / local 0 writer.
5. b8 item 2: L9 kind-10 matcher.
6. b8 item 3: control and prop event callers.
7. b8 item 16: experience banks (next 0x7CADC): which bank is XP, thresholds, what a level-up changes.
8. b8 item 20: creature template (next 0x14F8A4): health/attack/defence/speed/loot names.
9. b8 item 17: forms (next 0x7C7DC): human / lizard / beast differences.
10. b8 item 19: spell slots (next 0x81440): effect per slot, Act 1 spells first.
11. b8 item 15: ghost rows (next 0xAEA70).
12. b8 item 12: money (dword +0x145).
13. b8 item 13: item text.
