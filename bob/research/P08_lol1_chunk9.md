# P08 LoL1 chunk 9: sound

No Godot was run. The tree is `~/lol1_godot` at `9987d7e`, clean. L06 chunk 9 fills `playSoundEffect` after the levels that call it. The 215 VOC files and the 67 music files are already extracted. This chunk does not move earlier chunks. Combat still treats sound 255 as silence. TIM may call the player. A missing-call list does not grow because of this name.

## Data

`QUIET_CALLS` in `level_scripts.gd` includes `playSoundEffect`, `hideMouse`, `showMouse`, `delay`, and `stopPortraitSpeechAnim`. The default arm returns 1 for those names and does not increment `missing`. EMC `olol_playSoundEffect` calls `snd_playSoundEffect(stackPos(0), -1)`. TIM `tlol_playSoundEffect` calls `snd_playSoundEffect(param[0], -1)`.

`LoLEngine::snd_playSoundEffect` returns immediately when the track is 1 and the last track is −1 or 1, and when the engine is quitting. It stores the track as the last track, then returns when the track is −1 or the track is at least `_ingameSoundIndexSize / 2`. `volume &= 0xFF`, so the EMC value −1 becomes 255. The first entry of `{223, 159, 95, 47, 15, 0}` that is less than the volume is replaced by the paired entry of `{255, 191, 127, 63, 30, 0}`. A VOC index other than −1 whose name is not EMPTY plays that voice when it is present. On DOS, a missing VOC selects the MT32, GM, or PC-speaker index for the current device. Track 168 on that path becomes 167. The index arrays themselves were not copied.

`placeMonster` returns before the environmental sound when `sounds[0]` is 0 or 255. The comment says the last valid track number is 249. This chunk does not invent a VOC for 0 or for 255.

Counted this pass: `<owner-media>` has 215 files, and `lol1_music` has 67. `lands-of-lore-1-re/data/music_inventory.json` still names output `~/lol1_music`. The files that were counted are the archive directories. L01 splits the 67 as XMI 18, C55 17, ADL 16, and PCS 16. A VOC body was not opened.

## Behaviour

`playSoundEffect` plays the VOC the index names, at the volume the call passes after the mask and the two tables. An EMC call passes volume −1 and the player hears it as 255, then through the table. A track the index rejects is silence. Music stays on the 67-file set. Tracks 0 and 255 stay silent. Earlier chunks keep their own scope: chunk 3 does not gain a file for 255, chunk 4 does not gain a substitute TIM, and chunks 5 through 7 do not add this call from the missing list.

## Tests

1. `playSoundEffect` of a track whose index names a file among the 215 plays that file. `missing` does not gain `playSoundEffect`.
2. Track −1 plays nothing. Track 0 plays nothing. Track 255 plays nothing. Track 1 plays nothing when the last track was −1 or 1.
3. An EMC call with volume −1 reaches the volume step as 255. The first table entry less than 255 is 223, so the played volume is 255. A volume of 160 maps to 191, because 223 is not less than 160 and 159 is.
4. A track at or past `_ingameSoundIndexSize / 2` plays nothing and does not open a file outside the 215.
5. A TIM `playMusicTrack` loads from the 67-file set. A name outside that set is not played.
