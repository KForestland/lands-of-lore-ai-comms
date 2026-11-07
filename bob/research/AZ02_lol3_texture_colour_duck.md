# AZ02 meta duck — LoL3 texture colour

Method: `AI_COMMS/META_DUCK_METHOD_20261107.md`. Read-only. No game bytes were copied here. Sources: `AI_COMMS/LOL3_CLASSIC_PREP.md`, `lands-of-lore-3-re/docs/texture-028e-evidence.md`, `lol3_out/analysis/palette_order_20260926.md`.

## 1. The problem

CONVERT `0x028E` / `0x828E` textures decode to the right silhouette and the wrong colour. The span placement is exact on 26/26 sampled payloads. The colour has been open since the 2026-09-21 bake note and was measured again on 2026-09-26. The owner report is that the textures are structured and the palette is wrong.

## 2. Main chain

This is presentation of LoL3, and Classic LoL3 is not the game being finished. A grey index picture is still recognizable, so a later quest walk could be blocked out. The owner would still not accept the scene: the reported gold door is not gold. It stays the texture blocker. It is not parked as a refinement detail, because every LoL3 texture is waiting on the same colour stage.

## 3. What the game is trying to do

*Reveal* and *orient*. The wall, the door, and the prop have to be the objects the player recognizes, in the colours the retail scene uses. The span decoder already supplies the shape. The missing stage is the colour of those indices.

## 4. Player-visible contract

The player looks at a surface and sees the retail picture, not a grey ramp and not a rainbow. Evidence already in hand: the grey-index atlases match swords, figures, rocks, and the hex medallion; `own_vs_level.png` shows the bank palette and the level palettes both fail that picture; the CKEEP gold door is the named still. No new longplay frame was opened for this duck. A death, a flag, and an item do not change because a texel is the wrong colour.

## 5. Exact vs approximate

EXACT: the colour the player sees on a known surface has to match the retail frame. A gold door that renders olive, grey, or rainbow is wrong. The span placement of the indices is already exact and stays exact.

APPROXIMATE: the byte layout of the lookup, the shade rows, and the blend tables, once the uploaded texels match. Shade and translucency can be a later adapter. An invented palette that merely looks smooth is not a match.

## 6. Options

a. Decode a per-texture colour table out of the CONVERT bank. Cost: another file search. Risk: the 2026-09-26 directory read found no colour in the texture record, the N-byte remap scan was negative, and a smoother window is the same trap as the rejected level palettes (they already step about 12–15 and are the wrong colours). Proves nothing until a picture agrees.

b. Decode only the table that paints one known texture, and adapt shade and blend. Same missing table as (a). Smaller only after one texture's true colours exist.

c. Paint an intent-matching palette by eye. Cheap for one door. The owner would notice a wrong gold, and the result would be an adapter, not a decode. It does not travel to the next texture.

d. Capture the GL upload of one known texture. The uploaded texels are the colours the player sees. Cost: one traced load, not a new codec. Risk: the game has to run, and the trace has to name the texture. Proves the contract for every texture in that load. The 2026-09-26 RAM dump cannot replace it: `0x6601B8` was zeros and the texels were GPU-resident.

Pick: (d). File-side smoothness cannot certify the picture. The capture is the smallest step that can.

## 7. How to prove it

One BUPP1 load, the autosave the harness already reaches, under a GL trace. Compare one uploaded image with the retail view of that same surface. Grey atlases and neighbour scores are not that proof. This session does not run the game.

## 8. Unpark

A trace, or a screenshot whose pixels are aligned to one decoded index buffer. Until then the span decode stays accepted and the colour stays open. AZ03 is the file-side check that a smooth embedded window is not that table.
