# Fable side task while the temple-islands sweep runs (lead: Opus, 2026-11-07)

Map look fixes from the owner's r17 playthrough (AI_COMMS/playtest_feedback_20261023/TRIAGE_20261107.md). These are NOT on Grok's
list (Grok: BG rows + Dark Halls BH04+); do not touch the Dark Halls or Grok's rows.
In a NEW worktree from act3-chain c9295da (not your temple-islands tree, its sweep must stay frozen):
1. Hive (hive_review): 17-27-27/17-27-35 roof gone but a green/grey plane remains (restore the roof, remove the plane);
   17-28-43/17-29-06 texture missing until you walk in (portal-visibility pop-in: check NEAR / the portal edge there);
   17-30-51, 17-32-57 green texture / looks wrong; 16-48-43 lava/stone bridge transparent texture.
2. Darker Jungle L8: 17-50-18, 17-50-38, 17-50-53 structure/textures out of place; 17-59-34 walls you can clip through.
3. L10 (17-55-17 missing texture; 18-14-46 "a lot of work needed") and L12 (18-22-43 texture issues): list what is wrong per spot
   with captures vs the longplay, fix the clear ones.
Meta duck first; player-side/presentation fixes before world changes; capture tests (before/after) + ledger pieces
(tools/build_deviations.py build). Post "[fable] MAPFIX ..." lines. Owner F10 screenshots are in the report folders.
