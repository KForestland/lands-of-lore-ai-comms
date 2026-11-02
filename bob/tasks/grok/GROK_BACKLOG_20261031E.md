# Grok standing backlog #6, 2026-10-31 ~14:10Z (lead: Opus): ITEMS GAME-WIDE + map follow-ups

Owner direction 2026-10-31: finish the maps, then items (all items at once, game-wide), RPG, dialog.
Backlog 5 is done (thanks). Same rules: read only; grade every claim PROVEN / LIKELY / UNKNOWN; a CHECKPOINT
per item; ~45 min time-box per item ending in "LIKELY: ..." one-liners plus witness bytes; reports in
backlog_20261031E/itemN_<name>/REPORT.md; post "GROK BACKLOG 6 EMPTY" at the end.
Base facts: ITEM_CENSUS_AND_PLAN_20261025.md (170 defs, 91-byte records, 663 world placements, 107 handlers),
engine_contracts_20261027/ITEM_USE_DISPATCHER_CONTRACT.md, WEAPON_STATS_COMBINED_20261028.md.

Map follow-ups first (they unblock the builders today):
1. **Arrival pins.** Backlog 5 item 2 left all 26 arrivals LIKELY. Pin the live arguments at call 0x14F4D6 and the
   prefix at object +0x558 for at least the L8 hub arrivals (selectors 1-5) so Astra can mark them PROVEN.
2. **L8 tree tops, renderer side** (Fable's question in L8_TREE_TOPS_FINDING_20261031.md): does the native assembly
   renderer (type-0 children, 0x5A91D path) cull by winding, and what does the night sector shade (level 16-60 with
   near/span) do to a face at the 3000-unit far end? One answer each.


**1b. PRIORITY (added 14:2xZ from Astra's world gate, 26 of 41 Act 2/3 edges blocked):** who sets these script values
in the original (a writer in another level, a global carried across levels, an item use, a dialog, the level-entry setup)?
One LIKELY sentence + witness bytes each:
   - L8 prop 1198, predicate 136: needs local 13 = 1 (the only decoded op198 writer is its own exit group, which resets it to 0);
   - L14 prop 170, predicate 50: needs local 22 = 1 (no op198 writer in the area);
   - L19 region 2369: needs second-array 52 = 0/1 (what the campaign start leaves there);
   - L10 local 11: native writer control 150 / group 19732 exists; what calls control 150's event.
   Also: are "locals" per-level and saved, or reset on entry? This decides whether a writer in another level can count.

**1c. PRIORITY (added from Astra's movers step, 14:23Z):** the opcodes that still stop whole mover groups. One LIKELY
sentence + witness bytes each, so the host can run them: opcode 2 arm 0x18 (re-check against backlog 5 item 5),
opcode 3 slot 1, opcode 12, opcode 210 (L8 full groups), and opcode 1 target modes 0 and 2 (L13, 35 targets).

**1d. PRIORITY (fable 15:20Z):** opcode 2 arm 0x3C (byte 4 = 60) of 0xD7890: first command of L8 movable 53 group 13278 and movable 54 group 13320 (151 L8 commands). One LIKELY sentence + witness bytes. It is the last blocker of the maps-complete gate; do it before the item second passes.

Items (the game-wide item map):
3. **Grant sources.** 53 definitions are never placed in the world. For each: which script command (opcode/arm),
   actor loot, shop table or spell creates it, per level, with group ids. Include the generic "give item" / "take
   item" / "has item" commands and predicates (opcode, arm, operand layout).
4. **Handler table, classified.** All 107 handlers at 0xC860: for each, a one-line class (weapon strike, heal, spell
   scroll, key/quest use, reagent/recipe, throwable, no-op) from what it calls, and the shared sub-routines. Mark
   which ones are already hosted (7 Prism, 16 Flute, 86 ...). Group by class so builders can host a whole class at once.
5. **Record stats.** The varying offsets 28/32/40-45/52/55-58/61/63/64/67-73/75-85: trace the readers (weapon request
   0x89115, equipment sum, inventory UI, shop price). Name damage, speed, value, weight, slot, charges where proven.
   Settle +0x46 (the weapon note calls it "selector count"; the icon producer reads decimal 46/47 = 0x2E/0x2F).
6. **Descriptor rows +0x47** (4 x 5 bytes): the ops each row byte selects (on-hit effects, spell effects).
7. **Item text.** Where the item description/look text lives (LOCALLNG / TRR / GLOBAL), and its index from the definition.
8. **Equipment and inventory rules.** Slots and which class bytes go where, two-hand rule, stacking/charges, the
   ghost rows 152-156 (handlers 5/36/68/85 shared with Long arm, Plasma staff, Dag Light, War blade).

## Continue straight into backlog 7 when 6 is done (do not post EMPTY until item 16)

RPG, dialog, magic and combat systems, game-wide (owner order after items: RPG -> dialog -> small stuff).
Reports in backlog_20261031F/itemN_<name>/REPORT.md; same rules and time-box.

9. **Character stats.** The player record: health, mana, strength/might, protection, skills (fighter / mage / rogue?),
   experience and level-up rules, per-form (human / lizard / beast) modifiers. Offsets, readers, level-up table.
10. **Experience sources.** What grants XP (kills, scripts, spells used, skills used) and how much: opcode/arm and the formula.
11. **Dialog engine.** How a conversation runs: the opcodes that start talk, show a line, offer choices and branch;
    where the lines live (TRR / LOCALLNG keys) and how a group id maps to them. One worked example: Bacatta in the
    Huline village (the owner's broken case: after leaving the Jungle, Bacatta is hostile and does not lead).
12. **NPC state.** Friendly/hostile/follow flags for actors, what flips them, and the village groups that set Bacatta
    friendly + leading. List the bytes the port must keep.
13. **Spells.** The spell table (Prism, Spark, Dampen, Mind clustr, ...): cost, effect handler, targeting, the
    spell-learning sources (scrolls SS1-SS9, recipes R-*), and how casting runs (opcode or item handler).
14. **Creature combat stats.** The per-creature template: health, attack, defence, speed, damage, resistances, loot
    table pointer, for every creature in all 15 levels (the port borrows Rat stats for Shades).
15. **Shops and trade.** Any vendor tables (items, prices, currency) and the opcodes that open them.
16. **Save state.** The globals and per-level state the original keeps across levels (so the port saves the same set).

## Item 17 — W7 ORACLE (grok-dosbox; starts only when the lead posts "RENDER ... NEXT: grok-dosbox")

The original game can answer "who writes X" directly. Material: 30 original saves in ~/lol2_runtime_root/SAVEGAME
(owner's 2024 playthrough; $MUSEUM_/$MUSEUM2 known Museum; the rest unmapped), the instrumented DOSBox source
~/dosbox_src/dosbox-0.74-3 (trace watches, March), launcher notes ~/lol2_out/dosbox_gameplay/README.md
(keep tracing in a SEPARATE launcher and an isolated game copy; never write the reference game folder).
a) Map each save to level, region and position (save header bytes; report the table).
b) For each still-UNKNOWN writer the builders need (L8 local 13 / pred 136, L14 local 22 / pred 50, L19 second-array 52,
   opcode 2 arm 0x3C if 1d stays open): load the nearest save, arm a memory-write watch on the value's address,
   play/teleport to the trigger, report the writing instruction and the call stack. One run = one PROVEN answer.
c) Write the launcher + watch recipe down (ORACLE_RECIPE.md) so any lane can rerun it.
