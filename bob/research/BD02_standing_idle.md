# BD02 standing idle — R2 adapter review, rows 0309–0313

No Godot was run. No DOSBox. The longplay was not opened. r12y is still `56812f9` and its deviation files stop at 0226, so rows 0309–0313 are absent there. This pass reads them in r17 at `65c9984`. The tree was not edited. The last R2 slice ended at 0308. The next slice after this one is 0314.

## 0309 L8 first Huline Temple visit

`l8_journey.gd` uses REACH 160. While the target is the temple, `_process` calls `interact("visit_temple")` without E. Actor 113 still spawns from `temple_visited`. The E panel remains for the other targets. HINTBOOK 2932–2941. The snatch is still not an opcode 21 movie. No simpler native build.

## 0310 Drowning veil and jump clock

`river_drowning_state.gd` keeps LIMIT 15. `counting` stays true while the body is inside the polygon and airborne, and `liquid_drowning.gd` passes that into `advance`, so a jump inside the water does not zero the clock. Standing above the surface, or leaving the polygon, resets it. The veil in `drowning_overlay.gd` is the owner r16 request. No printed duration replaces 15. No simpler build.

## 0311 Jungle water gaps

`jungle_water_skirts.gd` draws material 808 and adds no collision. The row names regions 2559 and 260 from owner r16. Same-bed edges stay open above the bed. No simpler build that would also hide the backdrop.

## 0312 L8 temple journal note

`l8_village_hints.gd` keeps the id `l8_see_temple_first`. The sentence says the temple is east of the entry, on the far side of the map, that the village stays closed until Luther has been there, and that a scene plays. HINTBOOK 2932–2941. Both editions use that sentence. No simpler build.

## 0313 L9 statue alcove

`l9_statue.gd` calls `enter()` on the walk into region 3185 and does not require E for that entry. The E hint remains when the remains have not been offered. HINTBOOK 3789–3799. The left-bowl click is unchanged. No simpler build.

No PROPOSE line. Rows 0314 through 0316 stay for the next R2 pass.
