# GROK task list Y (lead: Opus), 2026-11-06 — MAPS TO 100% (owner order: maps first). Patches, do not apply.
Base: act3-story a123d3f (NOT stacked on S/T/W/X; map fixes are separate). Same rules: explicit types, free test Nodes,
earned/probe tests, one DEVIATIONS row per adapter, short NOTES. Owner F10 reports are the source; quote them.

Y01 L8-CACHE-LADDER: the ladder to the Shaman's Treasure Cache does not climb (owner F10 11-04, Brady 175 pt 7).
Y02 L8-TREE-BRIDGE: knock over the tree to bridge the chasm on the way to the Larkhon (Brady step 51, owner F10 23:23:53).
Y03 PT3-L8-PLATFORM: L8 cannot raise the platform at (-1038,-2302) (owner F10 11-03).
Y04 PT3-CROUCH-MUSEUM: C crouch not working at Museum (-1869,-1092) (owner F10 11-03).
Y05 PT3-L14-TEMPLE + TEMPLE-PORTALS leftovers: spider burrows floor/tunnel, quill opens the door, doors as portal
    teleports into separate rooms. Portal visibility (region_visibility.gd) is in; list what still looks or plays wrong
    against the longplay frames (g_276/g_278 and your J10 notes), patch what you can.
Y06 MUSEUM-NICHE-LEVEL + MUSEUM-DUST: lid 52 niche click + one strike on prop 61 = +1 magic level; ceiling dust prop.
Y07 ATLAS-A1 (map work, AI_COMMS/ATLAS_AND_CODEX_PLAN_20261105.md section 6): storey grouping tool -> atlas/<AREA>.json
    (regions, storey id by floor height AND connectivity, kinds). Tool + a test over all areas; no renderer yet.
"[grok] Y<NN> DONE patch <file>" board line each. Owner F10 reports first.
