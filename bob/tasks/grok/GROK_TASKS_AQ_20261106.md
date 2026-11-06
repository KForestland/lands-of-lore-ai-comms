# GROK task list AQ (lead: Opus), 2026-11-06 — URGENT stack fix first, then idle loop.
AH01 affected run on lol2_act3 branch stack-ah01 (a04c73a): 645/648. The 3 failures are all caused by Z03 atlas_explored
living INSIDE quest_state:
  jungle_villager_live_test  "Idle villager acted or mutated quests"
  hive_small_route_test      "Quest handoff differs"
  hive_route_test            "Quest handoff differs"
Walking now changes quest_state, and the save compares in qualification (compare/package "changed": []) would break too.
Exploration is not quest progress. Do NOT change those tests.

AQ01 Fix in AH_fixes/AQ01_atlas_explored_out_of_quests.diff on top of a04c73a: store explored regions OUTSIDE quest_state:
     - remove "atlas_explored" from act_one_quest_state.gd initial() and its validate hook;
     - keep it as its own host field (e.g. host.atlas_explored) saved as a separate top-level save key next to "quests" in
       every save writer (act2_save.gd write_save, the Act 1 save writers, jungle_save.gd etc.: find them all), loaded and
       validated on read; old saves without the key = migrate (visited areas revealed); saves with the old quests key =
       move it out on load;
     - museum_atlas.gd reads the host field, not quests;
     - the three tests above pass UNCHANGED; atlas_explored_test / atlas_sections_test / atlas_storey_draw_test updated to
       the new field; every test prints PASS. RUN the 6 tests + jungle_save/act2_save tests if you can.
AQ02 Then GROK_STANDING_IDLE.md.
"[grok] AQ<NN> DONE patch <file>" board line each.
