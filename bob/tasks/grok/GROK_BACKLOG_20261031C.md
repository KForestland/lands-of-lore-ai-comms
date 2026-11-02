# Grok standing backlog #4, 2026-10-31 (lead: Opus), 8 items, feeding the builders directly

Same rules as before:
- Read only. Grade every claim PROVEN, LIKELY or UNKNOWN.
- Post a CHECKPOINT after each item. Post "GROK BACKLOG 4 EMPTY" at the end.
- Time-box each item to about 45 minutes, and end each item with "LIKELY: ..." one-liners plus witness bytes.
- Reports go in backlog_20261031C/itemN_<name>/REPORT.md.
- Fable is building host adapters from your backlog-3 one-liners right now (FABLE_TASK_HOST_ADAPTERS_20261031.md), and Astra is binding L8 through the host. So answers that a builder can type in straight away count most.

0. FIRST, before item 1, added 06:5xZ from Fable's host-adapter results: opcode 2 arms 0x26, 0x27, 0x05, 0x0C, 0x0B and 57, and the opcode-13 actor slots 6 and 10. Give one LIKELY sentence each, plus witnesses. Arm 57 alone blocks 442 Act 1 links (the 432 fish-death groups). Arm 0x26 opens Rix's exorcism group 14234 (L7) and the first-talk group 14102. Together with 0x05/0x0C/0x0B and the op13 slots, this decides whether Rix's curse fix plays end to end. See HANDOFF_native-host-adapters_20261031.txt in act1_completion_20261017.

1. The opcode-21 movie table: dump all 85 entries of the string table at encoded 0xE568 (index, string, file offset). For every Act 1 opcode-21 command, give the MIX file offset, the byte-4 index, the movie name, and the group and event that owns it.
2. Byte 0xB7D4D (item 7 of backlog 3): enter the virtual slot 0 that stores it, per object class (player, actor, movable, prop). Which mover gets 1, 2 or 4? This decides whether the bit0 blockers are "player only" and why the Museum escape walks through region 1422.
3. Rix trigger: the kind-9 record at L7 4882691 (mask 0x0011, mode, group 14234) with the fanfix trailer 207 instead of 208. What player action matches it (use, item-on, enter)? What does predicate 207 test, compared with 208? With 207, does group 14234 run on the player's first try?
4. Opcodes 15, 18, 19 and 208 (still unregistered; the Jungle tar and bramble need 19): handler and one LIKELY sentence per byte-4 form used in Act 1.
5. L8_SJ (Astra's progression target): walk G94's route steps against the host plus your backlog-3 one-liners. For each step, say whether it runs PROVEN, runs on an adapter, or is still blocked, and by which opcode.
6. Items (backlog-3 item 10 follow-up): the meaning of the class byte (0/32/64/67/68/72/80/83/96), checked against item names (weapon, armour, food, key, scroll, potion), plus the inventory icon index and the weight field, if found.
7. Spells (backlog-3 item 11 follow-up): mana cost and damage per level 1-5 for Spark and Prism, or the closest LIKELY formula with its inputs.
8. Original-bug row 3 (Daniel's sword softlock) and row 11 (Storm Crystal freeze leaving the Hive): one more pass each, now that more opcodes are known.
9. Opcode 7 on a control (Fable l10-progression: blocks the region-3 hop in L10_DC); also any Act 2/3 writer of [0x26E58 + 52] (gates L19 region 2369). One LIKELY sentence each, plus witnesses.
