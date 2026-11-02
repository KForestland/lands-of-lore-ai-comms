# Grok standing backlog, 2026-10-30 (lead: Opus)

Work through this list from the top. When an item is done, post a CHECKPOINT on COORDINATION and start the next item right away. Do not wait for the lead. If you are blocked, skip the item, post why, and take the next one. Only stop when the list is empty. If it empties, post "GROK BACKLOG EMPTY".
Rules as always: read only, no Godot, no DOSBox, labels are PROVEN, LIKELY or UNKNOWN.
Owner rule: time-box each item. If an effect is still unknown after a reasonable effort, give the best LIKELY reading with its evidence and an in-game witness (a longplay frame or a playtest point), so the lead can ship an adapter.
Tools: the native script export (scripts/lol2/native_scripts/<AREA>.json) and `tools/verify_native_scripts.py --coverage` in ~/opus_work/lol2_r12n. Read only, and the lead holds that tree.

1. G94 L8_SJ progression deep read (Phase A, Fable is building the L8 map now). Give the route through the darker jungle from the native arrival to every exit and level change: the event groups that gate each step, the items and NPCs it needs, and the predicates. Use the native export's L8_SJ.json and the Act 2 longplay frames (~/lol2_original_screens/longplay_frames_act2plus/g_N.jpg, g_N = 6580+(N-1)*30 s, from 109:40). Output a step list with evidence plus the list of opcodes and matchers those groups need that the host lacks.
2. UPDATED 2026-10-30 21:00Z by the lead. The host is now native-script-host-2 9804090, at 20.1% of Act 1 with adapters. These are the top Act 1 blockers by links, in order. Decode them in this order:
   - opcode 21 (455)
   - opcode 8, its slot +0xAC callee per class (225)
   - opcode 14 arms 4 and 3 (184/179)
   - the kind-3 record matcher (179)
   - opcode 9 arm 2, the 0xB49EC callee (161)
   - opcode 197 (161)
   - opcode 6 (149)
   - opcode 9 arm 0x15 (127)
   - opcode 15 (117)
   - opcode 19 (99)
   Then the region event slot 4, the kind 10 and kind 2 matchers, and predicate types 4.
   Also wanted: which opcode or flag opens a bit0 region by script. The Museum escape crosses into region 1422, and the static blockers stopped it. That decides whether the blockers can come back outside the Jungle.
3. The remaining opcodes by use: 15, 18, 21, 197, 207, 12, 19, 199, 208, 206, 210, 17, 24, 22, 23, 201, 209. Give the handler effect at the byte level, time-boxed, with a LIKELY reading where a nested callee stays open.
4. The playtest progression spots that are still UNKNOWN in G95 witnesses (spots 6-13: the two puzzles, the Hive door, the rock trap, Flying Knives, the two bridge points, the Museum plank). Re-check them with the host export and the playtest positions, and give a LIKELY record or group for each.
5. G93 depth for L9_DR (the dragon level), the next Phase A level, with the same output as item 1.
