# OF8. The Atlas at the catacombs showed the surface cemetery

Owner F10, "the undermap do snow right information", at (2537.2, -1818.9, h -118). The screenshot is the Magic Atlas titled Dracoid Cemetery. The drawn plan is the surface grounds, with the Emperor's door label. The player is underground.

## Grades

| Claim | Grade |
| --- | --- |
| The stand is inside catacomb region 4148 (floor -150, x 2335..2784, z -2000..-1681) and surface region 2435 (floor 0, a smaller quad over part of that hall) | PROVEN. creature_nav/L10_DC.json |
| Before this patch both regions were storey 0. Region 4148 was section 0. That page held 602 regions below -40 and 1222 above -20 | PROVEN. Headless probe of group_storeys and section_depths before the patch |
| The join was a stair chain. Neighbours within 32 units of floor were one component, and the pile test never split a component, so the hall and the surface stayed one storey | PROVEN. museum_atlas.gd group_storeys, STOREY_STEP 32. The two regions are not a single step apart (150 vs 0) |
| After the patch, region 4148 and region 2435 are different storeys. The stand's page has more than 100 regions below -40 and none above -20 | PROVEN. tests/atlas_storey_draw_test.gd PASS, exit 0 |
| A piled map (L9, L10, L16, L14) no longer paints the neighbouring storey on the same page, and the open fit uses the floor you are on. PgUp and PgDn still change storey | PROVEN in the presenter. The band() fade for other maps is unchanged; the storey test still checks it |
| The Claw Mountains storey counts stayed {1: 2940, 0: 704}. L16 and L14 moved by tens of regions, not a new fragment storm | PROVEN. Same probe after the patch. L9 gained one storey (7 became 8) |
| The native automap's own floor rule was not read | UNKNOWN. This Atlas is the port's map. The comment in museum_atlas.gd says it is not a reconstruction of the native discovery rules |

## What changed

`scripts/lol2/museum_atlas.gd` refuses a ramp link that would put two overlapping rooms more than 32 units apart into one component. On a section map the draw, the place labels, the plot markers, and the fit stay on the storey under the player.

Commit e8373696996ca87ea4f4e8ae9fe6c2802d104110 on grok/of9. Piece 0515. The test is the existing tests/atlas_storey_draw_test.gd, registry order 850, still headless. Lead runs tools/build_deviations.py build. This lane did not.

`/tmp/godot_dummy.sh --headless --path ~/opus_work/lol2_grok_of9 --script res://tests/atlas_storey_draw_test.gd`

Printed `PASS atlas storey draw: bright, faded, hidden`. Exit 0.

`tests/atlas_sections_test.gd` printed `PASS atlas sections: Floor and Inside N`. Exit 0.

godot_check: 22 scripts, 0 failed.
