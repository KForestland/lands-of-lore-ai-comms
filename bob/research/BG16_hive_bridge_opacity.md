# BG16 Hive bridge

LONGPLAY f_00489 (40:40) and f_00527 (43:50) show the lava floor as opaque cracked stone. The cracks are the texture, not a hole.

L5_HC floor material 21 has flags 0x00e1. The alpha bit is clear, so the exporter writes opaque RGB and does not set alpha_cutout. `hive.json` lists only `sourcewall_228` as a cutout. The playable material uses `TRANSPARENCY_DISABLED`. The three-frame strip and review_fps 1.6 were left alone.

Stood at the owner pose (-1140, -203, -6018), yaw -1.434, pitch -0.216. The floor draws the stone. No blend was removed.
