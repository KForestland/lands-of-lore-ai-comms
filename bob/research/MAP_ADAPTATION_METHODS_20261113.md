# G-16 step 2. Map adaptation methods

Read-only. No geometry was built and no Godot was run. The zone counts are the step 1 table posted 2026-11-13T17:46Z. The rule is `prepare_region_mover.overlaps` rules 1-5 (STEP 48, area above 4, not neighbours, no flag 0x80, floor-to-ceiling spaces meet) and then the two floor heights at the overlap centre within 24. Zone ids are that recount, largest pair-area first. They are not the published L14 labels. A shape check reloaded the pinned geometry and overlapped only inside each posted zone's own regions. Pair counts matched the table. L14 T3 came back 134 of the posted 135 pairs. The two sides are unchanged by that one pair.

The worked examples sit on branch `opus/l14-small-zones-20261113` at `b2b698c`. Reviews: `grok_research/review_R112_L14_T3_MOVE.md` and `grok_research/review_R114_L14_T14_TRENCH.md`. Both verdicts were MERGE. Those moves are held for r19h. They are not in the r19g playtest.

## What the three methods are

**(a) Shift a group up or down until the two layouts are stacked.** Plan x,z stays. Floor and ceiling move together in a shaped dip, or only the floor rises. The connection becomes a ramp, or a window sill stays where it was.

**(b) Slide a group sideways into open plan and lengthen or bend the corridor that joins it.**

**(c) Redraw a wing, with the original map as the guide.**

Floor figures below are the median of the regions' base floors. Ceiling figures are the median of each region's lowest ceiling corner. Depth is the overlap of the two volumes at the pair's centre. The ring count is how many other regions have their centre in the 200-unit band outside the zone box.

## (a) Vertical shift

### What the tool already does

`tools/prepare_geometry_move.py` on the b2b698c tree. `MOVES` lists L14 only, and two kinds.

`shaped_dip` lowers one side along a centreline. The drop is the least that puts the moved ceiling 5 under the other side's floor, eased at grade 0.72, and refused where it would put the moved floor through a KEEP layout. Cross-sections stay level. Shared vertices get one delta. Floor and ceiling take the same delta, so the crawl height is unchanged. Joins into the room side are refused. Regions near the joins become ramps.

`floor_raise` lifts a flat floor to a named height. The ceiling stays. Wall faces move only the points that sat on the old floor. A sloped floor is refused.

The producer writes three derived files and leaves the originals in place: `area_moved.json` (face points of the moved regions), `creature_nav/<AREA>.moved.json` (floor min and max of those regions), and `scripts/lol2/geometry_moves/<AREA>.json` (corner deltas, joins, and the sha256 of every input and output). `scripts/lol2/geometry_move.gd` serves those paths. A missing file or a hash mismatch loads the original and logs the refusal. Scene-tree meta `lol2_geometry_move_off` loads the original. `tools/prepare_region_mover.py` writes the moved overlap table when the spec exists. `act2_save.gd` stores the moved pack hash on the player. `act2_map.gd` adds `delta()` to a loaded height when the saved region is at least 0, the spec is live, and the save's hash is not already the moved pack.

The height-boundary packet is a second tool, used for the trench sills. It is not part of the dip.

### What breaks

Region ids stay. A script, a trigger, or a save that names a region still names the same region. A script that places a body by world position does not move. The producer never reads those coordinates.

On the T3 dip the spider passage was left alone because it sits outside the moved set. `l14_spider_passage.gd` is unchanged from `dacf858`. The wake point (1351, 40, -5396) and actor 68 at (1364, 0, -5442) lie in region 2568. 2568 is not a delta key, and neither are its neighbours. A later dip that does include a scripted point leaves that point at the old height.

Creature nav stores the new floor range for each moved region. A polyline of x,z in a script stays on the same plan, which is the right plan for a vertical move. An actor whose script sets y directly stays at the old y.

Atlas places in `atlas_places.gd` are world x,z. A vertical move leaves them on the same cell. Explored-atlas state is region ids, so it follows the same regions. A stack still shares one atlas cell. That is the stacked room the move just made.

Old saves move by the saved region id, once. A plan point that lies in both layouts follows whichever region the save stored. The room side and the tunnel side are disjoint keys, so a save stored as the room stays at the saved height and a save stored as the tunnel takes that region's drop. The owner's 01-16-21 bundle showed this on 2026-11-13T08:31Z: the player was not 100 lower, because the saved region was the wooden room. The carry is working as written. A save made while the spec is live stores the moved hash and is not shifted a second time.

Sightlines change with the kind. The T3 frames at `opus_lane/g05/t3` show the wooden room where the tunnel used to share the view, and they show the rock tunnel from under the room. The T14 frames at `opus_lane/g05/t14` are the same bytes before and after: the window drawing is untouched. The four sill openings became collision (y 55 to 75) because a short body could enter the trench and the trench had no other exit. A window the player must look through can keep its drawing. A window the player must walk through cannot take a floor raise that closes it.

Joins crack when a neighbour of a moved edge is left out of the ramp set. The dip refuses a grade steeper than 0.72 and refuses a drop through the KEEP. The trench raise refuses a floor that reaches the ceiling. Props and static assemblies that have no region tag stay where they were. The crumbling-wall assembly on the spider passage is that case. A prop standing on a moved floor floats or sinks unless its faces carry that region id.

### Which kind of zone it fits

**Passage under a room.** The overlap graph is two-sided, the smaller side is one neighbour-connected walk, and that walk has joins outside the room. This is `shaped_dip`.

The worked passage is this recount's L14 T3. Smaller side 24 regions, one walk, five outside joins, floor median 45. Larger side 49 regions, one walk, floor median 0, ceiling median 160, including room 2768. The tunnel ids start at 2520. Pair area 47428, depth at the overlap centres median 69.8. It is on the chain and it is an owner zone. The producer moved those 24 regions plus seven ramp regions (2516, 2519, 2541, 2544, 2546, 2548, 2551). Rule-5 pairs with one end in the moved set and the other in the room went from 198 to 0. Native rule-5 pairs went from 528 to 330. The two pairs that remain on the moved set are ramp 2516 and ramp 2519 against corridor 3185. The dip was told to leave 3185.

The same shape, not yet moved: L9 T1 (15 and 18 regions, each one walk, depth median 126, chain) and L16 T0 (16 and 45 regions, each one walk, depth median 173). L16 T0 sits in a plan box of 275 by 425.

**Trench whose lower band shares a corridor.** Floors match. One side's ceiling is the corridor (about 20) and the other side's ceiling continues above it (about 90). This is `floor_raise` of the tall side, and the windows stay drawn.

The worked trench is this recount's L14 T11 and L14 T12, not this recount's T14. T11 holds regions 36 and 38 plus corridor cells including 3890. T12 holds region 34 plus corridor cells including 3874 and 3877. Region 40 is in the raised set and had no rule-5 pair before or after. Floors are -80. Trench ceiling is 90. Corridor ceiling is 20. Depth is 100. The raise takes the trench floor to 25, so the volumes no longer meet. Fourteen pairs went to 0. The sill regions 33, 35, 37, and 39 are not delta keys.

**One sheet over many cells.** One side is a single region whose box covers the other side. One transform on that region clears the zone. L10 T2 is one region (box 905 by 484, floor 0, ceiling 130) over 41 cells. L10 T4, T5, T8, and T14 are the same shape. L14 T4 and L14 T7 are single regions with no neighbour outside the zone.

**Two interleaved layouts.** Both sides are large and at least one side is several walks. The plan ring 200 units outside the zone box already holds other regions, so a sideways slide has nowhere to go. Fit is still (a), done piece by piece along a centreline that has to be named. L14 T0 is 40 regions in one walk (floor median -120, ceiling median -20) against 52 regions in six walks (floor median -100, ceiling median 1200), 151 pairs, area 304845, depth median 80, chain, ring count 178. L10 T0 is 20 and 21 regions, floors 0, depth median 130, area 147663, chain, owner, ring count 236.

**The kept pair.** This recount's L14 T14 is regions 2517 and 3185, one pair, area 744.5, depth 38.8, chain, owner. Corridor 3185 is the KEEP in the T3 spec. The dip was capped so it would not take the tunnel floor through that corridor. This pair stays on the unmoved table. The next measurement of it belongs on the moved pack. A further drop of 3185 undoes the cap.

## (b) Sideways move

No producer writes an x,z shift. `prepare_geometry_move.py` has two kinds and both return a height delta. Stretching that producer would move the wrong axis.

A sideways move breaks every consumer that stores plan position. Script coordinates, trigger x,z, creature polylines, Atlas places, fixture points, and saves all stay in the old plan while the floor leaves. The vertical save-carry does not help, because `delta()` is a height. The connection has to be rebuilt as new quads, and every shared vertex along the bend has to move once or the corridor cracks. Neighbour links that pointed at the old edge point at empty space. Windows that looked across the old line look at the new wall, or at a gap. Portal drawing follows the new neighbours only after the nav and the overlap table are regenerated. None of that regeneration exists for an x,z move.

It fits a zone that fails (a) for a named reason (a KEEP floor, a window the player walks through, a slope the raise refuses) and whose plan ring is empty for the length of the slide. The large zones in this table do not have that ring. L14 T0, L14 T3, and L10 T0 have 178, 139, and 236 other regions in the 200-unit ring. No current zone is assigned to (b).

## (c) Redraw a wing

No producer redraws a wing from the original map. The original map is the guide the lead already named. A redraw breaks the same plan-position consumers as (b), and it also breaks region ids when the new wing does not keep them. Saves, Atlas exploration, triggers, and scripts that name a region then point at nothing.

The overlap graphs that are not two-sided are the L9 copy piles, and those are not wings. Ten L9 zones store one plan quad on five or six region ids: T0, T3, T4, T5, T6, T7, T8, T9, T10, T12. Unique quad count is 1 in each. T0 is regions 418, 3220, 3232, 3239, 3253, 3260, one quad, box 122 by 95, pair area 103125. The chain fixtures do not land in these ten. The owner reports do not either. The fix is to draw and collide one copy. That is a cull, not a new wing. Portal visibility is already on for L9 (`act2_map.gd` `PORTAL_VISIBILITY_AREAS` is L14, L10, L9, L16, L19, L20, L12). The cull hides regions the portal walk does not reach. It does not delete a second copy of the same quad from collision.

No zone in this recount is assigned to a redraw. The largest real zone, L14 T0, is two sides. One dip is the smaller job. A level redraw stays the last resort the lead named, for a level whose zones are not two sides and are not copies.

## Cost

These are the commits and the counts already on the branch. They are not a cost.

T3: `bba6b44`, `27cce62`, `f1b7378`, then rule 5 in `128ff7f`. The shaped-dip commit touches 8 files (the deviation row, the spec, the producer, the move test, the moved tracker). Rule 5 touches 5 files. Twenty-four tunnel regions, seven ramps, 198 room pairs cleared. Review R112, Godot not re-run in that review. The frames are `opus_lane/g05/t3`.

T14: `b2b698c`, 12 files, four floors raised 105 to y 25, fourteen pairs cleared, four sill polygons added, drawing unchanged. Review R114, Godot not re-run in that review. The frames are `opus_lane/g05/t14`. Ledger rows 0642 and 0650.

@opus: one paragraph of real numbers when you can. Hours on T3 and on T14, how many times the producer was regenerated, which tests you ran, and which files a later zone of the same kind touches. The elapsed time between those commit stamps is not that paragraph.

## Order of levels

The table is the unmoved geometry. T3, T11, and T12 on L14 are the worked pair of moves, measured here before those moves. The lead's order stands: Temple, then Cemetery, then the other levels. Inside a level, chain zones and owner zones come before the rest. Copy piles are a one-copy check, not a move. Nothing below is a build.

1. L14 remaining. Skip T3, T11, and T12. Leave this recount's T14 (2517 with 3185) until it is recounted on the moved pack. Next real zone is T0, method (a), then the smaller chain zones T4, T5, T6, T8, T9, T10, T13, T15. Single regions with no outside neighbour (T1, T7, T16) get a collide check before any shift.
2. L10. Nineteen zones, owner T0 and T10, chain on ten zones. T0 is the interleaved pair. T2, T4, T5, T8, and T14 are one sheet over cells, one transform each. The Cemetery look pass stays with Sol and then Opus. This order is only the overlap pass.
3. L9. Do the ten copy piles before any dip. The real zones are the other seventeen. Chain: T1, T2, T14, T18, T20, T25, T26. T1 and T2 are the large passage-shaped zones. Portal cull is on.
4. L8. Thirteen small two-side zones. Chain T6 and T7. No owner point landed in a zone. Portal cull is off, so the new floor is what hides the stack.
5. L16. Four zones, seventy-one regions, no chain hit and no owner hit. T0 is the dense passage shape in a 275 by 425 box. Portal cull is on.
6. L7. Two zones, fourteen regions, floors and ceilings both 725 to 925, quads all distinct, portal cull off, no chain hit and no owner hit. Method (a) if a frame shows two layers. The ring is occupied, so not (b).
7. L5. One zone, six regions, chain and owner, depth median 30. Method (a). Portal cull is off.
8. L17. One zone, six regions, chain, same floor 12 and ceiling 52. The two trios are different quads (561, 562, 565 against 1228, 1235, 1236), sharing one volume. A frame that shows one cavern means draw one. A frame that shows two rooms means (a).
9. L12 and L19 when those levels are walked. L12 is one zone, three regions, area 152, no chain fixture and no owner hit. L19 is one zone, four regions, a strip against three cells, no chain fixture and no owner hit. Portal cull is on for both.
10. L1, L3, L4, L13, and L20 have no zone under this rule. The older tall-stack counts are a different table. A zero here means this rule found no same-height overlap. It does not clear any other fault on that level.

Q13 stays parked.
