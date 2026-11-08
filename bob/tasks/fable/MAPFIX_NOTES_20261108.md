# Fable MAPFIX (FABLE_TASK_20261107B.md): map look fixes from the owner's r17 playthrough, 2026-11-08

Worktree ~/opus_work/lol2_mapfix, branch mapfix from act3-chain c9295da (temple-islands stays frozen for its sweep).
Captures: before/after per spot with the owner's F10 pose (tmp/pose_capture.gd; LOL2_SCENE/LOL2_POSES, optional LOL2_PACK ray probe
that names the pack face under five screen points). Evidence folder: fable_lane/mapfix_20261108/.

## Meta duck (short)
1. Problem: 14 owner F10 rows (TRIAGE_20261107 lines 23-48) on the Hive, Darker Jungle, L10 and L12 look.
2. Main chain: no; presentation only. Owner order: maps first, so they are worth a pass now; nothing here changes movement or gates.
3. Intent: *atmosphere* + *orient*: the Hive reads as roofed lava caves with one continuous river; the deep hall is one hall;
   the Jungle village is huts in a dark wood; the L10 tomb pit is a floor that collapsed into the catacombs.
4. Contract per spot (what the owner sees): listed below with the fix or the finding.
5. EXACT: nothing here. APPROXIMATE: which texture an unbound surface gets, when a cluster is drawn, how a clipped polygon is textured.
6. Cheapest faithful: data-driven neighbours and the walk seed, no hand-placed geometry.
7. Proof: before/after captures at the owner's poses; affected tests; owner playtest.

## Hive (hive_review, L5_HC)
- 17-27-27 / 17-27-35 "roof gone, grey/green plane": 20 faces of the Hive pack have no material (8 ceilings, 8 walls, 4 floors;
  their region records carry word16/17 = region+1, undecoded). They were drawn in the placeholder grey-green; the r16 ROOF_SKIP
  excluded one of them (654). FIX: jungle_review `fill_untextured_surfaces` (Hive on): such a floor/ceiling takes the nearest
  textured same-kind face at the same height (the Jungle floorless rule extended to ceilings); ROOF_SKIP no longer excluded.
  Result: the roof is drawn again with its neighbours' material (the animated lava ceiling 21 that region 282 carries in the
  pack; whether the original's roof there is lava-lit rock or dark rock is for the owner: longplay 40:40-43:40 shows dark
  rock ceilings over lava floors). After 9aa9499 the formerly hidden step strips (ornament 234) also show along the roof edge.
- 17-30-51 "green texture in the lava": region 188's floor was unbound -> now the lava (material 21) like regions 187/221;
  the river is continuous as in longplay 41:00 (f_00493).
- 17-32-57 "looks wrong": the plane under the slab was unbound floor 1446 (region 506) -> now its neighbour's rock.
- 17-28-43 / 17-29-06 "texture gone until I move in": the platform regions 936/938 (floor -1579) share no region edge with the
  hall (a chasm); the view walk stopped at its first region. FIX: region_visibility `seed_radius` (Hive 600): every region within
  600 units of the camera (700 in height) seeds the walk. Result: the hall's walls and floor are drawn at the owner's pose.
- 16-48-43 lava/stone bridge transparent texture: not touched here (Grok BG row; the bridge visuals are a known item).

## Darker Jungle (L8)
- 17-50-18 / 17-50-38 / 17-50-53 "structure out of place": the ray probe names source walls with material 130 (64x64 bark/rock)
  spanning height 60-200 (faces 7526, 7546, 7540, 7544 and one more; raw 8200000080011000, surface code 1, regions 516/531/533/534).
  Material 130 is otherwise a 0-64 low wall (48 faces, codes 4-7). The five 60-200 spans hang above the ground like a tilted roof.
  Not fixed: the original's placement of these upper spans is not known (likely the raised hut platform's upper walls, or a
  producer height for code-1 spans). -> Grok/lead question with the face ids.
- 17-59-34 "walls can be clipped through": the hedge walls (source walls, material 276) only carry the projectile layer (native
  movement is region-based); the ray shows no RegionBlocker there, so the native bit0 blockers do not cover region 1388/1389.
  Not fixed (a world/collision change; the owner's rule puts player-side first). -> list for the lead: blocker gap at (1842,2500).

## L10 (MapL10_DC)
- 17-55-17 "lacks this texture" RESOLVED (commit 9aa9499): the player stood on a stair step (regions 61-63, faces 68-70,
  record_role floor_subdivision) whose nav regions have NO polygon; region_visibility.clusters() gave each a one-region
  cluster with no edges, the view walk never reached it, so the step's floor was never drawn and the sky panorama's nadir
  showed through the hole as a fan of stretched stripes. Proof chain (captures at the owner's pose): oil pit no, sector light
  no, shader no (plain materials), props no, assemblies no, ALL meshes hidden -> the fan stays (= the sky), portal
  visibility off -> the floor is there. Fix: polygon-less regions stay out of the clusters and are always drawn (28 in L10,
  283 in the Hive, 110 in L13). Test region_visibility_clusters_test PASS; ledger 0321. The same fix draws the Hive's
  missing step strips (lava river banks, slab room seam).
- Side note, not applied: act2_map allows looking down 80 degrees (pitch_limit 1.4) where the original's view is limited
  (darker_jungle uses the panorama's 37.6 degrees); at steep angles the panorama's nadir is a stripe fan wherever a floor
  is missing. A native look limit for the Act 2/3 hosts would hide such holes and match the original -> owner/lead call.
- 18-14-46 "a lot of work": the great hall; nothing specific to fix from one line -> ACT2-MAP-REVIEW stays.

## L12 / DragonLevel (18-22-43)
- The report is from the DragonLevel host (dragon_level.tscn), not L12. The camera at (-2962, 314, -7396) stands 60 units from
  prop 1020 (template 8, 187x111, material prop_882) with props 1021/1022 (159x229, prop_728) beside: the owner saw three
  billboards from inside their radius (a shield and fur). Nothing is misplaced in the pack; the look is the billboard up close.
  No fix; note for the lead (billboard props close up read as a texture error).
