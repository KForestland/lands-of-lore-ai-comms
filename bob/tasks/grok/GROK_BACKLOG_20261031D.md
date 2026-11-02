# Grok standing backlog #5, 2026-10-31 (lead: Opus): MAPS FIRST (owner direction 13:20Z)

The owner wants all maps finished first, then the game-wide items and systems.
Same rules as before:
- Read only. Grade every claim PROVEN, LIKELY or UNKNOWN.
- Post a CHECKPOINT after each item. Post "GROK BACKLOG 5 EMPTY" at the end.
- Time-box each item to about 45 minutes, and end each item with "LIKELY: ..." one-liners plus witness bytes.
- Reports go in backlog_20261031D/itemN_<name>/REPORT.md.
- Fable and Astra build from these one-liners straight away.

1. **Act 2/3 travel graph.** For each of L8, L9, L10, L12, L13, L14, L16, L17, L19 and L20, list every level change (op2 0x1C; byte 5 = selector<<5 | level): source group and event, destination level, selector, and the opening condition (predicate or global), if any. Add the Act 1 exits into L8. Goal: the previews become connected levels.
2. **Arrival records.** For every level and selector in item 1: the arrival position, heading and region (the start record), with file offsets, so each arrival can be pinned.
3. **L8 tree tops** (owner playtest): in the darker jungle the tops of the huge round, wood-coloured trees show in the port. How does the original hide them? Draw distance or fog constants per level, a canopy or ceiling record the pack drops, a clip height, or a view-pitch limit? Name the bytes.
4. **Scripted movers per Act 2/3 level** (doors, lifts, bridges, moving walls): counts per level, the opcodes and arms they use, and which of those the host does not have yet (gap list for the builders).
5. **The L8 Claw Mountains exit** (OPEN 6, second pass): op2 arm 0x18 and op9 arm 8, which keep exit regions 3277/3278 sealed.
6. **The Museum ending click point** (owner 09-28-19): before the dragon journey movie there is a point-and-click scene with the dragon, maybe with dragon's blood. Find the controls, item ids and groups that run it, and the movie that follows.
7. **The Dark Halls closing walls** (owner): walking forward closes walls; bookcases move when a button is found or pressed with E. List the groups and opcodes, so the lead can check that the host covers each one.
8. **Museum region 1422 opener** (one pass): the indirect calls left unentered by the 12:26Z answer.
9. **Added 13:15Z from Astra's exit checkpoints:** the remaining Act 2/3 exit blockers on the current host. One LIKELY sentence each, plus witnesses:
   - L12 region 734 / group 0: opcode 2 arm 0x24 (runs before the travel to L8/4);
   - L17 movable 50 / group 3896: opcode 1 mode 1 (exit to L16/2);
   - L9 prop 104 / group 2168: the kind-2 matcher (exit to L8/5);
   - what calls control and prop events (the binder wires only movement entry and movable use).
