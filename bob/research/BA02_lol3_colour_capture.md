# BA02 — LoL3 colour, capture step

`grok_research/AZ02_lol3_texture_colour_duck.md` already picked option (d): a GL upload capture of one known texture. An eye-matched palette per texture family was the option the duck rejected. This step stays on the capture path. No family palette was written. LoL3 was not launched. No texture bytes and no PNGs were copied here. `lol3_out`, `lol3_classic_godot`, `lol3_runtime_root`, and `lands-of-lore-3-re` were not edited.

`apitrace` is not installed. `wine` is `/usr/bin/wine`. `winedbg` is `/usr/bin/winedbg`. No `.trace` file was found under `lol3_out` or in the 23 `lol3_runtime_trace*` directories linked from `lol2_out`. The PNGs already under `lol3_out/godot_import` and `lol2_out/lol3_analysis` are decode probes. They are not a retail frame aligned to one index buffer.

The retail launch already in `lol3_runtime_root/launch.sh` is:

```
cd <owner-media>
wine explorer /desktop=LoL3,1024x768 LOL3.EXE -16MB -NO_ASSERTS
```

The capture the owner would run later, after `apitrace` is installed, and on a display that the Act 3 regression is not using:

```
cd <owner-media>
apitrace trace -o /tmp/lol3-colour.trace wine explorer /desktop=LoL3,1024x768 LOL3.EXE -16MB -NO_ASSERTS
```

Load the BUPP1 autosave the AZ02 duck already names, then dump one `glTexImage` whose width and height match one decoded CONVERT `0x028E` buffer from that load. Compare those texels with the retail picture of that same surface. This session did not run that command.

What unparks the colour is unchanged: a trace, or a screenshot whose pixels align to one decoded index buffer. Until then the span decode stays accepted and the colour stays open.
