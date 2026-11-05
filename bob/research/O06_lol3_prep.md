# O06 LoL3 prep: what is decoded, what is missing, first chunks

No game was run. Sources are the memory note `lol3-convert-028e`, the 2026-11-03 planning file, `LOL3_CLASSIC_PREP.md`, `LOL3_CURRENT_SPEC.md`, `LOL3_MASTER_PLAN.md`, `LOL3_HANDOFF.md`, the public RE docs under `lands-of-lore-3-re/docs/`, and `lol3_classic_godot/README.md`. The March layer-6 notes are structural byte labels. They are not script opcodes, and none are added here.

Owner order, 2026-11-04: LoL2 Classic, then LoL1 Classic, then LoL3 Classic, then Enhanced. Gathering can run during LoL1. The Enhanced Gladstone slice waits until Classic is done. Souls, the gimmick worlds, and the C&C replacement are Enhanced, not these chunks.

## Decoded

Containers. WSX peel is 51 of 52 DAT files. An LMF file has a record table at `0x100`. Each record is 16 bytes: `u32 rel_offset`, `u32 size`, `u32 marker`, `u32 aux`. The sampled count is 38. Payload base is `0x100 + count * 16`. Nested directory sizes follow `(2^n + 2) * 16 + 12` for n from 1 to 10. Marker `0xCDCDCDCD` is the directory fill.

Maps. A `.map` is the same table38 family. CKEEP field 0 is repeating 8-byte records `(u16 0, i16 x, u16 0, i16 z)`, about 341 points. Field 2 floor polygons are partial. The Godot scaffold draws those outlines on placeholder floors and loads in Godot 4.7.

Textures. CONVERT flags `0x028E` and `0x828E` are one span per row: `u16 A`, `u16 B`, `u8 data[B]`. Mode `A & 0xC000` is 0 for a copy and `0x4000` for a skip. All 26 saved mip0 payloads exact-consume. Grey index pictures show real silhouettes. The placement proof is KVOLC slot 3, 126 by 91. Flag `0x008B` is raw 8bpp when `size == w * h`. The decoder is `lol3_out/tools/probe_028e_resume_atlas.py`.

Other assets. 25 PCM wavs. 9 of 19 MOVIES1–4 entries are VQA turned into webm. Runtime traces show the game reading WSX families, including `LOCAL.WSX`, `DAT/GLOBAL.WSX`, `QWOD0S.WSX`, music banks, and `SAVEGAME/$AUTOSAV.XXX`. Compact table38 labels that the current spec already uses are field 0 names, field 1 a decorator catalog, field 2 placements, field 3 entity names. Those labels are the spec's, and they are partial.

Level companion names from `LOL3.DAT` strings, still working labels: `.map`, `.odf`, `.lmf`, `.tex`. The same note names `_Uncompress_Texture_Column`, `_Get_Texture`, and the floor, wall, slant, and sprite draw calls. Those are string names, not entered functions.

## Missing

Colour. The bank palette at `+0x6A2`, scaled by 4, is rainbow noise. The RGB555 bake is a separate `u16[256]` LUT and was not read. The CKEEP CONVERT bank that would hold `xtb5door2` is still missing. A VGA palette PNG in the Godot tree is a preview asset and is not that LUT. Cross-bank palettes were rejected by the evidence note.

Geometry. The 16-byte leaf is not known to be vertices, a BSP, or compressed. No walkable mesh replaces the placeholder floor.

`.tex` / LEVED. A separate format from the CONVERT spans. Door `xtb5door2` is the unit test and is open. Retail packs are not whole-file LZO. `0xecdb0` is named LZO1X for convert-path buffers only.

Movies. 10 MOVIES3/4 entries are not identified.

One WSX DAT file is still unpeeled. Extraction provenance for `lol3_extracted` is still open: the staged files are real, and the rebuild script is missing.

Save. The trace saw `$AUTOSAV.XXX`. The record layout was not read.

Scripts. No LoL3 opcode was entered for this inventory. The QWOD0 and SWOD4 byte roles in the March notes stay container structure.

Planning checklist in `LOL3_PLANNING_PHASE_20261103.md` section 1 is still unchecked: a guide pack, a longplay frame index, owner notes, a bug ledger, and a story map of guilds and endings.

The Godot host has no earned route, no items, no dialog, and no combat.

## First chunks

Same shape as L06. A later chunk does not reopen an earlier one. No day count: build waits until LoL1 Classic is out, and the gather can run before that. No chunk invents a vertex layout, a palette, or an opcode.

1. Source pack. Fill planning section 1 from the web scrub and the videos the owner already named. One guide, one full longplay with a frame clock, and a one-page story map. No Godot scene. Enhanced souls and the C&C replacement are written down and not built.

2. One coloured texture. Keep the 26-payload span decoder. Recover the bake LUT, or capture one frame of KVOLC slot 3, and show the gold that the grey index picture does not. Stop if the CKEEP door bank is still absent. Do not recolour from the VGA preview PNG.

3. One CKEEP floor. Use the field0 outline that already draws. Read the 16-byte leaf before any vertex is stored. Until that read, the scaffold keeps the placeholder. This chunk does not texture the floor.

4. Walk the outline. In `lol3_classic_godot`, move on the CKEEP field0 points with the existing Godot 4.7 load. No monsters, no doors, no level change. A test is: the camera stays inside the point cluster already measured (`x` about −2000..3000, `z` about −5600..−500) and a reload returns to the same point. There is no save format yet, so the test stores the adapter position only.

5. Names for that one room. Copy field 0 and field 3 strings that the current spec already extracted for CKEEP. Do not add English names for unlabeled records.

6. The other companion of that room. `.tex` for `xtb5door2`, or the missing CONVERT bank, whichever the door unit test already points at. Colour from chunk 2 is applied only if that chunk closed. This chunk does not start a second level.

7. Autosave inventory. List the files under `SAVEGAME/` and the byte length of `$AUTOSAV.XXX`. Do not write a field layout. A later chunk, after a read, can be the LoL1-style packet. This one only proves the file is the one the trace opened.

8. Story cards for Gladstone only, after chunk 1's guide and longplay agree. One card per required step, with the same unknown line L06 used when the walkthrough stopped. Guild paths and the five portal worlds wait. The five worlds are not named here; the evidence names file stems (CKEEP, KVOLC, EWOD1, BUPP1, QWOD0, SWOD4) and does not join them to a portal list.

9. Script opcodes. Not started until a function is entered. The draw-call strings above are the index, not the chunk's result.
