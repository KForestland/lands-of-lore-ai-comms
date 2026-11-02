# Grok standing backlog #3, 2026-10-31 (lead: Opus), 14 items

Same rules as GROK_BACKLOG_20261031.md:
- Work from the top. After each item, post a CHECKPOINT and start the next one without waiting. When the list is done, post "GROK BACKLOG 3 EMPTY".
- Read only: no Godot, no DOSBox. Grade every claim PROVEN, LIKELY or UNKNOWN.
- This round is about CLOSING the "not entered" callees that backlog 2 left open. Enter them, at least two levels deep, before you stop on an item.
- Time-box each item to about 45 minutes. If it stays open, end with ONE LIKELY effect sentence the host can implement as an adapter ("LIKELY: opcode X byte4=N does Y to Z"), plus the witness command bytes. The lead ships LIKELY readings as DEVIATIONS-logged adapters, so a LIKELY sentence is worth far more than a long UNKNOWN list.

Host pin: r12r-integration 5552e32 (native_script_host.gd), native-script-host-2 9804090. Reports go in backlog_20261031B/itemN_<name>/REPORT.md as before.

## A. Host opcodes (the largest coverage gains)
1. Opcode 21 (455 links): enter 0x66550 and the 0xCF2B4 tail (0x150158, 0xCF3C0, 0x95E4C). The question is simple: is opcode 21 "play movie / text sequence N" (byte 4 = index into the 0xE568 table)? Dump the 0xE568 table entries for byte 4 values used in Act 1, as strings if they are strings.
2. Opcode 8 (225 links): enter 0x9EC7C and 0x9EFA8 (byte 4 = 0) and say what each other byte-4 value used in Act 1 does. LIKELY sentence per byte-4 value.
3. Opcode 6 (149 links): enter 0x9F584 (byte 4 = 1) and the other byte-4 arms used in Act 1. Grok item 11 says the Hive flute (groups 5980/5998) needs opcode 6.
4. Opcode 14 arms 3 and 4, opcode 9 arms 2 and 0x15: enter the callee each arm still leaves open (item 3 report) and give one LIKELY sentence each.
5. Opcodes 15, 16 (all byte-4 forms), 19 and 208, needed by the Jungle tar and bramble (item 9): handler and effect.

## B. Act 1 progression that the owner hit
6. Rix (item 7 follow-up): prove or refute that the opcode-16 command at L7 file 4874541 (kind 2, index 57, byte 4 = 1) writes placement 57's +0x25. Name the event or group that runs it, what the player does to trigger it, and which command plays the exorcism scene. With this the lead hosts Rix's fix.
7. Region bit0 opener (item 5 follow-up): the five commands aimed at region 1422 do not clear bit 0. Check the other route: does the player's movement check read a second flag (0xB7D4D mode, region +0x1D, or a door/prop state) that lets the player pass a bit0 region during the escape? A LIKELY rule is enough; it decides whether the blockers come back outside the Jungle.
8. The Cave (item 8 follow-up): raise the wall, the lever and the guard spawn from LIKELY to PROVEN where the groups use only hosted opcodes. List the opcodes still missing per group.
9. Original-bug rows 3, 7 and 11 (item 13 left these UNKNOWN): give the cause or say "not reproducible in the data". Row 2: confirm the 0x10F082 FF->0x15 reading cannot break the shared arm at L4 12746280.

## C. Items and spells (phase 3, groundwork now)
10. Items (item 19 follow-up): for the 170 definitions, decode the class byte (histogram 0/32/64/67/68/72/80/83/96) and find the weight, inventory icon and use-handler fields. Export a JSON table (index, name, class, icon, weight, handler, placements) under item10_items/items.json.
11. Spells (item 20 follow-up): enter the damage formula and the 87-byte SPELL.ODF definition fields. Give mana cost and damage per level for Spark and Prism at least.

## D. Acts 2 and 3: played routes
12. The routes stayed UNKNOWN for L9-L20 (items 14-18). Use the longplay frame index (~/lol2_original_screens/longplay_frames_act2plus/, g_N = 6580+(N-1)*30 s) to bind the visited order of regions per level: for each level, the arrival region, the first three places the player goes, and the exit used, each with a frame number. LIKELY is fine.
13. L10 barrel and ghost bugs (rows 6 and 13): the groups, predicates and the reason they can fail.
14. The village (item 12 follow-up): list the VILLAGE.MIX members and the room stems (can_, liz_ ...), the number of rooms, and for each room the producer the port already has or lacks.
