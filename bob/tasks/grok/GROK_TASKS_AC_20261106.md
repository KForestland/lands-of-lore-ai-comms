# GROK task list AC (lead: Opus), 2026-11-06 — map completeness audit + the book (Codex) data. Same rules as before.

AC01-AC05 MAP-MARK audit, one per area: L1_DC, L3_DH, L4_HJ, L5_HC, L7_DH. MAPS/<AREA>/markers.json exists already; check
     that EVERY Brady map point (MAPS/brady_maps) and every Prima/hintbook point for that area (puzzles, NPCs, items, story
     steps, original bugs) has a marker, and that each marker has matching geometry/host in act3-story a123d3f. Output per
     area: missing markers added (edit markers.json is OK, it is your research file), and a short "no matching geometry or
     host" list = map gaps for the lead. Then `python3 backlog.py done MAP-MARK-<AREA> grok "<file>"` in AI_COMMS/BACKLOG.
AC06 Codex C1 (AI_COMMS/ATLAS_AND_CODEX_PLAN_20261105.md sections 5 + 8): a generator tools/lol2/build_codex.py ->
     data/lol2/codex.json with four sections: Items (from item_catalog.gd + act2_items_catalog.gd + item census + hint book
     item list), Creatures, Characters, Lore. Entries short, in Luther's wizard-book voice, only what Luther knows after
     meeting/holding the thing (owner decision: no future uses). Patch + a test that every catalog item has an entry.
"[grok] AC<NN> DONE <file>" board line each. Owner F10 reports first.
