# BK10 movies

`hw01.vqa` is not a MIX entry. `placenta.vqa` and `e224e.vqa` are unique FORM/WVQA entries. `placenta.vqa` is not `bb_brth.vqa`.

The hash is `ww_hash_v1`. Area reels use `SPHERE1`, `SPHERE2`, or `SPHERE3`, then the area, then the uppercased file, inside `DAT/<area>I.MIX`. One FORM/WVQA hit is the same bind `lookup_movie` uses for CITADEL. The CITADEL control hit `SPHERE2\L12_CM\CITADEL.VQA` in `L12_CMI.MIX` index 21, source sha256 `1194e316d7bde1d9c0b82a4519450c92f7ed558d328dbb02ea484dd07a45ff6d`, which is the pin in `tools/prepare_l12_citadel_movie.py`.

A plaintext miss in `MOVIES.MIX` is not absence. That archive stores hashed names. `citadel` and `bb_brth` are also absent as plaintext there.

## hw01.vqa

Grade DECODED for the absence under the known path patterns.

`L17_HC.MIX` stores the cstring at file 143215 and at file 652134. Those are names, not directory entries. The video inventory has no 0x342 placement named `hw01.vqa`. There is no `L17_HCI.MIX` under `~/lol2_runtime_root`. `HIVE1.MIX` through `HIVE4.MIX` do not contain the bytes `hw01`. `CDCACHE.MIX` does not contain them either.

The hash of `SPHERE3\L17_HC\HW01.VQA`, and the same file under `SPHERE1` and `SPHERE2`, plus bare `hw01.vqa`, `MOVIES\hw01.vqa`, `OUTTAKES\hw01.vqa`, and `WOMS\...\hw01.vqa`, matched no key in the 81 `DAT/*.MIX` headers. `hw12.vqa` and `hw14.vqa` missed the same way.

The west-wall card stays. It must not claim the reel played. No ogv was staged.

## e224e.vqa

Grade DECODED for the file. The ending-card use is not this file.

`lookup_movie` on `L19_BC` / `e224e.vqa` is exact:

| field | value |
| --- | --- |
| logical name | `SPHERE3\L19_BC\E224E.VQA` |
| archive | `DAT/L19_BCI.MIX` sha256 `7ca34b4942bad7702a5c7ff25ad72f48ec88a22a5af1a4a2e4718535dcfcb5d5` |
| index | 5 |
| key | 1194504581 |
| bytes | 10686006 |
| source sha256 | `2a4c3fa6163cf4ac5f6ddb38fa1777548a4d93b4ca6292036bf4a5db020b7363` |
| VQHD | version 2, flags 9, 1256 frames, 228 by 348, 15 fps |

The 0x342 record is prop 78, Dawn, region 1461, position (2802, -1000, -882). The quad corners are (2744.5, -1000, -882), (2859.5, -1000, -882), (2859.5, -929, -882), (2744.5, -929, -882). The bytes `Dawn good Luthe` sit after the cstring in `L19_BC.MIX` at file 58149 because the name is on that prop. That adjacency is not the ending reel. `e224e` is not in `movie_table.json`. The ending card still does not play it.

Staged like CITADEL: `tools/prepare_l19_e224e_movie.py` writes `assets/lol2/generated/l19_e224e/e224e.ogv`. Ogg sha256 `55c2cb6a62261139b95a7e50800035c552f0be19dfba1eda87ca2e2250aaaeec`. Audio is 1846320 samples at 22050 Hz, the same 83.7333 seconds as 1256 frames at 15 fps.

## placenta.vqa

Grade DECODED for the file. It is not the opcode-21 birth reel.

`lookup_movie` on `L20_BB` / `placenta.vqa` is exact:

| field | value |
| --- | --- |
| logical name | `SPHERE3\L20_BB\PLACENTA.VQA` |
| archive | `DAT/L20_BBI.MIX` sha256 `6e6960776cf5ecbc0a0b83f100d09322ff006cf3ebf04e343a8ce8d28dd8f3be` |
| index | 24 |
| key | 3224565000 |
| bytes | 755314 |
| source sha256 | `e5605c7362bbbed3bf29792608cb313f9979f2cf364540c3cba315c25d6da6da` |
| VQHD | version 2, flags 9, 60 frames, 640 by 340, 15 fps |

The 0x342 record is prop 242, Frank's Placenta, region 262, position (-1160, -20, -4258). The quad is 150 wide and 100 tall on that point: x -1235 to -1085, y -20 to 80, z -4258. `placenta` is not in `movie_table.json`.

`bb_brth.vqa` is a different entry in the same archive: index 25, key 3553117415, 8198192 bytes, sha256 `caf8eb9254a28ae24488d1c2be8dafd6a7ff67bf42752227634b8f3da34fd1f4`, 290 frames, 640 by 400, flags 1. Movie-table index 65 names that file. It was not staged. The birth card still does not play either reel.

`CDCACHE.MIX` contains the plaintext `placenta.vqa` three times, in the same neighborhood as the level cstring, not as a second movie.

Staged like CITADEL: `tools/prepare_l20_placenta_movie.py` writes `assets/lol2/generated/l20_placenta/placenta.ogv`. Ogg sha256 `1f5c28caf7afc65d8b762a86550f500bf6aaa72266a29ef72599f0a74355c1e9`. Audio is 88200 samples at 22050 Hz, 4.0 seconds, matching 60 frames at 15 fps.

## What the host does

`placed_vqa_billboard.gd` puts each ogv on those corners. The hit body is layer bit 20, so the mover ray on mask 1 does not reach it. The 0x342 enable was not entered, so the quad starts when the map loads. A native loop bit was not read, so the reel repeats. Ogg is the presentation.

Piece 0389. Registry order 1018, `l19_placed_vqa_test`. That stand test passed, and so did `deviations_ledger_test`, `l19_dawn_curse_test`, `l20_finale_test`, and `l17_beast_blade_test`. Patch `BK10_placed_reels.patch` sha256 `a1203fe5b59c3d5f3a046ef6377cf709a11203d724b460b5facc7eb5b4f4ce30`. The ogv files stay gitignored. The prepare scripts write them.
