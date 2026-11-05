# d9e3aaf portal edges

act3-story `d9e3aaf`, parent `75597f2`. Two files: `scripts/lol2/region_visibility.gd` and one row in `docs/DEVIATIONS.md`. No Godot was run. List O is already on the board (O01 2026-11-05T13:59:01Z through O07 2026-11-05T14:19:01Z). Those files were not rewritten. Newest owner file is still `TRIAGE_20261104.md`.

## What the walk crosses

DECODED from `region_visibility.gd` at `d9e3aaf`. Setup still starts from the camera's region. The window is still the horizontal field of view. Pitch is still unread. `NEAR` 160 still opens a nearby edge to the full horizontal window. Clusters are still groups of at most 24 creature-nav neighbors. A reached region still shows its whole cluster.

The new links are polygon edges whose rounded endpoints match. An edge shorter than 0.5 is skipped. `roundi` is half away from zero. On the nav packs this pass counted:

| Area | Nav pairs | Shared plan edges | New pairs | New pairs whose floors differ by 80 or more |
| --- | --- | --- | --- | --- |
| L10_DC | 4975 | 6766 | 1791 | 300 |
| L9_DR | 8315 | 11630 | 3315 | 602 |
| L14_HT | 4706 | 7444 | 2738 | 818 |

Every creature-nav pair on these three maps is already one of the shared plan edges. The fallback that keeps a nav link when the endpoints miss is present and adds no pair here. One L10 edge key and 43 L9 edge keys name three or more regions.

`PORTAL_VISIBILITY_AREAS` is unchanged. The walk is still on for L14, L10, and L9.

## N01 frames

N01's longplay table stays the picture. Cameras were not bound to regions, and this pass did not open the jpegs again.

The two L10 drops N01 named, regions 3853–3933 and 3852–3921, are nav neighbors and share one plan edge. They were already reachable.

L9 regions 721 and 728, floors 30 and -490 near marker (1222, 1801), are not nav neighbors and share one plan edge. The new walk can cross that drop when the edge is inside the yaw window.

L9 regions 3943 and 3991, floors 591 and -110 near the gauntlets at marker (-3248, 1488), share no plan edge and are not nav neighbors. That shaft stays out of the walk. Regions 6425 and 6468, floors 530 and 0 near marker (2832, 10808), are the same: no shared edge. `g_00062`, `g_00071`, `g_00087`, and `g_00125` stay unbound to a region, so this pass does not call those frames fixed.

The deviation row still says native portal rules are not decoded and vertical portals are ignored. That sentence matches the code: the test is yaw, and a stack with no common plan segment stays hidden.

## Tests and the journal

`tmp/vis_edges.log` ends `103/103 passed`, report `tmp/regressions/vis_edges/report.json`. That log was read. It was not re-run. The deviation row on this commit still prints `58/58 L9+L10 tests PASS`.

M01's note ids are not in this commit. The diff does not touch `my_journal.gd`. Those ids stay proposals until a script is on `SOURCES`.

## Still open

A stacked pair with no common plan segment. Pitch. The native portal rule. Which longplay camera stands on regions 721, 3943, or 6425.
