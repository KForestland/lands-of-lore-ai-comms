# BG00 — village guard, Huline Temple first

Base `c9295da`, after `BG00a_l8_bridge_ladder.patch`. Patch `patches/ACT3P2/BG00_village_temple_first.patch`. Not applied to the live tree.

Owner r17 17-53-55 stood at the village tree with the blade recovered and `temple_visited` false. The journal note was already recorded and was not enough. The encounter used to skip the village until the temple flag, so E did nothing.

The guard line is on the encounter label and the HUD: "The village guard: Visit the Huline Temple first. It is east of the entry, on the far side of the map." E opens that sentence and does not offer admission. Showing the blade does not admit him. `show_guard` and `visit_shaman` require the temple visit. There is no atlas objective pin in this project, so none was added.

Printed on display :2:

`PASS earned L8 village: the guard says to visit the Huline Temple first, and the blade is not admitted`

`PASS l8_village_hints_test: four village-chain notes, owner state -> see the temple first, once, in My Journal`

`PASS L8 bound semantic actions and actual save/reload; production map walk/render still pending`
