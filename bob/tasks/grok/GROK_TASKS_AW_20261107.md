# GROK task list AW (lead: Opus), 2026-11-07 — owner idea: the GAME LOGIC of dialog and player choices, village first.
Owner: "perhaps we should game-logic / game-theory the dialog and player choices in the village and later do the same in
the dark jungle." Goal: one model per village of every conversation and choice, so no branch, condition or consequence
is missing or wrong in the main chain. Read-only research first; patches only for real defects. Do list AV first.

Sources: native conversation/script records (level scripts, Bacatta/village/tavern/Confidante packets), hintbook +
Brady + Prima village chapters, longplay frames (Act 1 village part of 32:33-109:44), grok branch_graph.md / AP06_branches.md,
our scripts (jungle_village_state.gd, jungle_bacatta57/65*, the tavern, Confidante, Kelsrick, Dawn, thieves den, shops).

AW01 Act 1 Huline VILLAGE as a state machine: every NPC, every line/choice the player can make, its preconditions (items,
     flags, soul value, form, time/order), its consequences (flags, items, soul value, hostility, movies, doors), and
     where each path leads. One file grok_research/AW01_village_logic.md: a table per NPC + one graph (mermaid or text)
     of the whole village.
AW02 Game-theory pass on AW01: dead ends (a choice that blocks the main chain), unreachable branches, choices that do
     nothing, orders the original allows that ours refuses (and the reverse), soul-value effects (good/evil) and their
     later payoffs. Each finding: original source | ours | verdict (OK / ours wrong / original bug to fix per the ledger).
AW03 Patches only for "ours wrong" findings that can stop or break the main chain, each with an earned walk; list the rest
     for refinement later (owner order: main chain first).
AW04 The same model for the DARKER JUNGLE (L8) tribe village (Daniel, the guard, the shaman, the tribe initiation, Dawn,
     the Larkhon, the herbalist, the backroom): AW04_l8_village_logic.md + findings, same format.
"[grok] AW<NN> DONE <file>" board line each. Owner F10 reports first.
