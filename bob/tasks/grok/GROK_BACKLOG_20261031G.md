# Grok backlog #8 (20 items), 2026-10-31 ~17:00Z (lead: Opus) — finish the maps, then items, RPG, dialog

Start after backlog 6/7 items in progress are checkpointed (item 17 oracle still waits for "NEXT: grok-dosbox").
Rules (W6, workflow plan): read only; grade PROVEN / LIKELY / UNKNOWN; ENTER every call on the asked path
(ghidra_query.py decompile, native harness); "complete false" must name the exact next address to enter;
~45 min per item, depth over speed; CHECKPOINT per item; reports in backlog_20261031G/itemN_<name>/REPORT.md;
post "GROK BACKLOG 8 EMPTY" after item 20. Builders (fable, astra) take the LIKELY one-liners straight away.

## A. Maps and progression (finish the world)
1. **L17 predicate 0 / local 0**: who sets it (fable's open edge on the L17 exit).
2. **L9 kind-10 matcher**: the matcher body and its record layout (fable runs that group directly today).
3. **Control and prop event callers**: enter the calls that raise control/prop events (left UNKNOWN in backlog 5 item 9 and 6 item 1b); the builders' binder wires only movement entry and movable use.
4. **Act boundaries**: which level change / global ends Act 1, Act 2 and starts Act 3 (the globals a save must carry across).
5. **Museum region 1422 opener**: the reader of the five opcode-197 arm-10 marks (today an adapter).
6. **Dark Halls closing walls and moving bookcases** (owner): the groups, opcodes and motion (backlog 5 item 7 stayed UNKNOWN).
7. **Museum dragon click point** (owner 09-28-19): the point-and-click scene before the dragon movie: controls, items, groups.
8. **Hive mechanisms from the owner's playtest**: flute bridge slide (10-26-06), elevator bridge (10-26-38), door (10-26-54), puzzle (10-30-07), rock trap (10-31-19), traps (10-32-45): groups + opcodes per spot, and which the host lacks.
9. **Cave leftovers**: Kenneth lowering the wall (not the gates), the lever at the bridge, the two guards after the sound clip.
10. **The Huline village** (no own MIX, G92 counts UNKNOWN): where its actors, scripts and dialog live.

## B. Items (game-wide)
11. **Handler groups, top 10 by item count**: enter each group's shared callee (start with 0x80064) and give one LIKELY behaviour per group.
12. **Money**: confirm dword +0x145 as the money counter (writers, readers, display), and where money is earned.
13. **Item text**: where look/description text lives and how a definition indexes it (item 7 left it UNKNOWN).
14. **Take-item / has-item**: the opcode-3 argument dword (fable's grant census waits on it) and the take/has commands and predicates.
15. **Ghost rows 152-156**: handlers 5/36/68/85 shared with Long arm, Plasma staff, Dag Light, War blade: what those rows are.

## C. RPG
16. **Experience and level-up**: close the two banks (+0x159/+0x161, +0x15D/+0x162): which is XP, the level thresholds, what a level-up changes.
17. **Forms**: human / lizard / beast stat and ability modifiers (reach, damage, what each form can use or cast).

## D. Dialog and the rest
18. **Bacatta friendly and leading**: the writers of actor byte +0xB5 bits 0/2/3 and +0xA9/+0xAB in the Huline groups (owner's bug: Bacatta hostile and not leading after the Jungle).
19. **Spells**: the effect handler of each of the 18 spell slots (cost, target, effect), starting with the Act 1 spells.
20. **Creature template**: name the fields around +0x63/+0x65 (health cap etc.), attack/defence/speed, and the loot pointer, checked against astra's 558-actor census.

21. **(added 18:3xZ from fable's items half 2) Placement flag bits 0x0400 and 0x8000** on the 37-byte world-item placement rows
    (Cave 9 rows + Hive 4/10 carry 0x0402; L8 29/30 carry 0x8002): what the original does with each bit (hidden until an event?
    container? dormant?) and who clears it. Unblocks 13 more original world items.
