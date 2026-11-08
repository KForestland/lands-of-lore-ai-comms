# BG23 Jungle Dawn voice

Grade: DECODED.

Owner r17 17-36-46 at Jungle (-5761, 4004): "cant hear what she is saying". The camera is on the river floor at height -100. That spot is the player place written by region 2842, group 5246, opcode 18: x -5761, z 4004. The same group starts E065E segment 1 (HTalk000DN750-753), which is not a repeating idle.

Dawn's AudioStreamPlayer3D was a child of the JungleDawn node and was never moved. That node is at the world origin, about 7000 from the talk spot. unit_size 300 and ATTENUATION_DISABLED stay as set on 2026-11-03 and 2026-11-05. max_distance 1200 still silences the player past that sphere, so the line at the origin could not be heard. Hive Dawn20 and the other Jungle talkers already set the voice on the body.

The voice now follows actor 63, 40 units up, when the talk starts and while the clip is shown. The earned test walks into region 2812, then from (-5761, 4004) across the open river edge into region 2842. The source places the player back on that spot, segment 1 plays, and the mix at the camera is above silence. The words in the wav begin about 0.9 seconds into the segment.

Patch: `grok_research/patches/ACT3P2/BG23_jungle_dawn_voice.patch`. Unapplied.
