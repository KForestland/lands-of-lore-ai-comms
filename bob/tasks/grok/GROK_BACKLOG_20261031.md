# Grok standing backlog #2, 2026-10-31 (lead: Opus), 20 items

Same rules as GROK_BACKLOG_20261030.md:
- Work from the top. After each item, post a CHECKPOINT and start the next one without waiting.
- If an item is blocked, skip it and say why. When the list is done, post "GROK BACKLOG 2 EMPTY".
- Read only: no Godot, no DOSBox. Grade every claim PROVEN, LIKELY or UNKNOWN.
- Time-box each item. Where an effect stays unknown, give a LIKELY reading plus a witness, so the lead can ship a DEVIATIONS-logged adapter. The owner accepts workarounds that play as intended.

Host pin for script work: native-script-host-2 9804090 (export: scripts/lol2/native_scripts/<AREA>.json; `tools/verify_native_scripts.py --coverage` in the agent worktree ~/opus_work/lol2_lead_20261019/.claude/worktrees/agent-a781e661460697afa).

## A. The script host (each item unlocks more scripts in every level)
1. Opcode 21, the top Act 1 blocker with 455 links. Give the handler, the effect per class, and its arguments.
2. Opcode 8, slot +0xAC per class (225 links). Opcode 197 (161). Opcode 6 (149).
3. Opcode 14 arms 3 and 4 (184/179). Opcode 9 arms 2 (0xB49EC) and 0x15 (127).
4. The kind-3, kind-10 and kind-2 record matchers, region event slot 4, and predicate left/right type 4.
5. Which opcode, flag or event opens a bit0 (player-impassable) region by script. Witness: the Museum escape into region 1422. This decides whether the blockers can come back outside the Jungle.
6. The per-object command queue (0x26E6C, epilogue 0x663B8): the order and timing between the two queues (split at C3) and opcode 196's multi-tick behaviour. Give enough for the host to sequence groups that play over time (door swings, traps).

## B. Act 1 leftovers (owner playtest, Phase E)
7. Rix: your checkpoint says actor 57 is not proven to be Rix. Close it from the actor table (template, name, sprite, position against the owner's 10-18-53 point) and group 14234's commands. Also say what sets +0x25 to 1 and what plays the exorcism movie.
8. The Cave: Kenneth lowers the wall, not the gates; the bridge lever opens the room; two guards spawn on the sound at the bridge (owner reports 09-21-34 and 09-22-23). Find the event groups and say what the original really does, with longplay witnesses at 5:06-13:24 (f_00062-f_00162).
9. The Jungle: the thieves' guild password man (10-05-07), the cat guy's animation (10-03-18), tar ignition (10-00-25), the cub's poison gland (09-36-08), and bramble burn/regrow (09-44-46). The fan guide 3.12 is a witness: ~/AI_COMMS/reference_schon_gewusst_lol2/schon-gewusst-lol2.txt.
10. The Baccata bridge sequence: the order (walk and talk with Baccata, then the bridge collapses as you cross) and its timing (owner reports 10-44-26 and 10-44-51). Find the groups and timers.
11. The Hive: the bridge slide with the flute and the elevator floor, the door, the puzzle, the rock trap and the Flying Knives (10-26-06 to 10-32-45). Give the records and groups with host status.
12. The village and monastery (G92 says there is no MIX). Find where their data really lives: room archives, WOMS, other files. Give a hosting plan, because the owner says the village "needs to be understood".

## C. Original-game bugs (owner: fix all; list at ~/AI_COMMS/act1_completion_20261017/ORIGINAL_BUGS_TO_FIX.md)
13. Check rows 2, 3, 7, 8 and 11 against the data. For each: what makes it fail in the original, and the smallest load-time fix. Add any new original bug you find as a row.

## D. Acts 2 and 3: progression reads (the maps are being built now by Fable and Astra)
14. L9_DR, the dragon: the route from the arrival to the exits, with the groups, items, NPCs and predicates, the host opcodes missing, and longplay witnesses at 119:10-128:40.
15. L10_DC (the Dracoid cemetery per Fable): the same output. The fan guide's section 6 is a witness, including the barrel and ghost bugs on the bug list.
16. L12_CM and L13_RC: the same output.
17. L14_HT and L16_CA: the same output (the Ruloi counter 19/19 is on screen at 202:40-212:40).
18. L17_HC, L19_BC and L20_BB: the same output, including the end of the game.

## E. Items (the third phase in the owner's order)
19. The full LoL2 item table across all acts: every item definition (name, icon, type, weight, effects, use script), with its source offsets, and where each item is placed or granted per level. The owner wants every item built in one pass.
20. The spells: the per-level spell data for Spark, Prism and the rest, at levels 1-5 (cost, damage, effect records, visual frames). This is for the later Enhanced spell-effects pass and for the Classic values.
