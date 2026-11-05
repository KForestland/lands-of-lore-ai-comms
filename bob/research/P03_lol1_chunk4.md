# P03 LoL1 chunk 4: opening and throne TIM

No Godot was run. The tree is `~/lol1_godot` at `9987d7e`, clean. L06 chunk 4 is TIM for the opening and the throne room, cards LOL1-01, LOL1-02, and LOL1-05. No other cutscene is in this chunk. The portrait click is chunk 2. The keep walk is chunk 5. `LOLFINAL.TIM` is the outro at `sequences_lol.cpp` line 1120 and is not loaded here.

## Data

The non-demo new game calls `chooseCharacter` after `loadSoundFile(0)` and `playTrack(6)`. `chooseCharacter` sets the language file `LOLINTRO.DIP`. The intro player loads `LOLINTRO.TIM` with `_timIntroOpcodes` (`sequences_lol.cpp` line 247) and sets `LOLINTRO.DIP` again (line 256). That file name is not among the 139 names in `lands-of-lore-1-re/data/tim_analysis.json`.

That inventory parsed 139 files. All 139 are AVFS. Every file has an AVTL chunk. 51 also have TEXT. The opcode names in the format notes are 0 initFunc0, 1 stopCurFunc, 2 initWSA, 3 uninitWSA, 4 initFunc, 5 stopFunc, 6 wsaDisplayFrame, 7 displayText, 8 loadVocFile, 9 unloadVocFile, 10 playVocFile, 12 loadSoundFile, 14 playMusicTrack, 15, 16, and 24 return-1, 20 setLoopIp, 21 continueLoop, 22 resetLoopIp, 23 resetAllRuntimes, 25 execOpcode, 26 initFuncNow, and 27 stopFuncNow. The interpreter named there is `TIMInterpreter`, with 10 functions and 6 WSA slots. AVTL is uint16 little-endian. The first values are function entry offsets. An instruction is length, delay, opcode, parameters. The opcode is the low byte of the third word.

`TimAnimator::displayFrame` draws only when `anim->wsa` is set. The comment says some scripts ask for a frame of an animation that is not there. The draw is skipped and the function returns after the screen update when the page is 0.

KING1.TIM is in O01E.PAK. Its TEXT strings include THRNDOOR, RICHARD1, RICHARD2, and RICHARD3. KINGSIT.TIM is in O28A.PAK and has AVTL only. SCOTIA1.TIM lists XFORM and SCOTIA. Those strings name files. They do not say which card plays which TIM. None of the three is assigned here as the throne scene or the poisoning. INTRO.PAK and INTROVOC.PAK are named in the edition comparison. This pass did not open them.

N04 leaves the throne function number unread. The earned start that chunk 5 already asserts is block 557, direction 0. LOL1-05, from L03, is the return: Scotia poisons King Richard, Dawn keeps him alive and gives a spell book, Baccata joins, and Timothy leaves. The joins are chunk 6. The walkthrough mentions a fallen cup and a shield shape. What the player must do with them is not written.

The port runs no TIM. `level_scripts.gd` has no TIM opcode. Sound opcodes 8, 9, 10, 12, and 14 may call the quiet `playSoundEffect`. Filling that call is chunk 9.

## Behaviour

Play `LOLINTRO.TIM` for the opening, then hand the accepted index to chunk 2. Play the throne TIM once for LOL1-02 at the earned start, and do not play that grant again after a reload. Play the LOL1-05 return once: the king is poisoned and Dawn's spell book has been given. The cup and the shield shape get no extra click.

A WSA slot whose movie is null skips the frame and the TIM function continues. No other TIM file is played. Until the throne script's own flag is read, the player stores one boolean `throne_played` in the chunk 1 packet, and the same for `poisoning_played`. Those two names are adapters. They are not retail field names.

## Tests

1. The opening player asks for the name `LOLINTRO.TIM`. A missing file does not substitute KING1.TIM, KINGSIT.TIM, or SCOTIA1.TIM.
2. After the opening, the hero id is the chunk 2 choice. The keep starts at block 557, direction 0, once.
3. A save taken after the LOL1-02 throne TIM reloads with `throne_played` set and does not play that TIM again. The same holds for `poisoning_played` after LOL1-05.
4. LOL1-05 does not itself add Baccata or remove Timothy. Those calls stay in chunk 6.
5. A null WSA slot does not draw and does not stop the TIM function.
6. `LOLFINAL.TIM` is not loaded.
