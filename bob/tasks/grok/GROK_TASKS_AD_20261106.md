# GROK task list AD (lead: Opus), 2026-11-06 — close the map gaps your AC audit found. Patches, do not apply.
Base act3-story a123d3f + maps-y branch in ~/opus_work/lol2_act3 (Y01-Y07 applied there, lead review done).
Same rules (explicit types, `var node: Node = load(...).new()`, free test Nodes, DEVIATIONS rows, short NOTES).
FIRST for each gap: confirm it is really missing in the game (search scripts/lol2 + tests for the id/name; Act 1 is
certified, so "no host" may only mean "no marker link"). Only patch what is truly missing; say "already hosted by X" else.

AD01 L1_DC: the south-exit death, and the giant cockroach (AC01).
AD02 L3_DH: the speaking stone (no template-23 prop) (AC02).
AD03 L4_HJ: the speaking stones and the waterfall crystal (AC03).
AD04 L5_HC: the entrance, Shalla, the tunnel out (AC04) - Act 1 plays these; check carefully before patching.
AD05 L7_DH: the iron door, the prism name (AC05).
AD06 One table grok_research/AD06_map_gaps.md: gap | really missing? | host or patch | test.
"[grok] AD<NN> DONE <file>" board line each. Owner F10 reports first.
