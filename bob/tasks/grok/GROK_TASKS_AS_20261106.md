# GROK task list AS (lead: Opus), 2026-11-06 — from the OWNER's r16 playtest (TRIAGE_20261106.md). Do right after list AR.
Base: lol2_act3 branch stack-ah01 (cfba754 + AQ01). Same rules (typed, PASS line, registry, DEVIATIONS, RUN tests).

AS01 PROGRESSION BLOCKER, L8 first temple visit. Hintbook 2932-2941: "To activate the Wild Village area, you must first visit
     the Huline Temple. When you approach for the first time, Luther triggers a special scene" (the old priest is snatched by
     a Belial-like creature). Our port (l8_journey.gd) makes it an "E - Visit the temple" panel at ONE point (REACH 160) with
     no scene, so the owner walked past it and the village never opened (his save: gift recovered, temple_visited false).
     Fix: approaching the initial Huline Temple area triggers the scene automatically (native trigger region/record if you
     can find it; else an approach radius matching the longplay), plays the native movie if one exists (find its number;
     longplay frames around the first L8 temple visit), then sets temple_visited and spawns actor 113 as now. Keep the
     order knife -> temple scene -> village (correct per the book). Earned test from the recovered-blade save: walk to the
     temple, scene fires without E, village opens.
AS02 Drowning feedback (owner idea): water creeping up the screen while the 15 s clock runs (a rising blue-green overlay with
     a wavy top edge, full at death), both editions; plus the jump bug: river_drowning_state.advance() resets the clock when
     a jump lifts the head above the surface - keep the clock while airborne inside the water region, reset only when out
     of the region or standing above the surface. Tests: overlay height follows elapsed/LIMIT; a jump loop in mid-river
     still drowns at ~15 s.
AS03 l8_see_temple_first journal text: say where the temple is (east of the entry on the far side of the map, per the book)
     and that a scene plays there when you arrive.
"[grok] AS<NN> DONE patch <file>" board line each.
AS04 Owner r16 F10 21-35-51 Jungle (-4603,-3412) h -8 "texture transparent/gap here": a stream bed shows the jungle backdrop
     through a gap at mid-height and has no water drawn. F10 21-36-45 Jungle (-3408,-4454) h -38 (Lizard under water) "need
     water texture there, transparent/gap here": below the surface the sides are open to the backdrop. Find the regions,
     check their native walls/water (liquid surfaces were propagated for bank-less regions 11-05; side walls under the
     surface may be missing or culled by portal visibility), compare with the longplay; patch + a capture test (both
     screenshots are in AI_COMMS/playtest_feedback_20261023/report_2026-11-06T21-3*/screenshot.png).
