# AZ03 — embedded colour-table search

The duck in `grok_research/AZ02_lol3_texture_colour_duck.md` picks a GL upload capture. This pass starts the file-side exclusion that capture replaces. It does not launch LoL3. `cdcache.wsx` was read and not modified. No bank bytes are stored here. `apitrace` is not installed. `winedbg` is on the machine. No `.trace` file was found under `lol3_out`. Displays `:0` and `:1` were already in use by the Act 3 regression.

The scratch script `/tmp/az-colour/search_embedded_table.py` slides an N×3 window across one CONVERT bank window and scores 256 neighbour pairs against a shuffle. The bank's own palette at `+0x6A2` is the baseline. A window of all zeros scores 0 and is rejected. A hit has to use at least 12 distinct sampled colours and a mean step under 20.

| Witness | N | Own palette ratio | Own step | Best window | Unique colours in that window |
| --- | --- | --- | --- | --- | --- |
| EWOD1_a slot 7 | 139 | 0.624 | 36.45 | offset 1430164, ratio 0.371, step 1.05 | 12 |
| EWOD1_a slot 21 | 251 | 0.679 | 45.76 | offset 589704, ratio 0.314, step 25.96 | 13 |
| KVOLC slot 3 | 184 | 0.773 | 48.47 | offset 691180, ratio 0.479, step 19.66 | 12 |

N is the index count. The smooth windows use 12 to 22 colours, not about N colours. A step near 1 is a flat accident. The rejected level palettes are already this smooth and are the wrong picture, so a lower ratio is not an identification. RGB555 windows were not scanned. No offset is accepted as the colour table.

The capture named in the duck is the remaining path. It was not run.
