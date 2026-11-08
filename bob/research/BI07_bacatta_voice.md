# BI07 Jungle Baccata voice

The owner at (3539,-4154) cannot hear Baccata. The line is playing. The player that plays it was left on the host, about 5400 away, and max_distance 1200 cuts it.

## Duck

1. Owner r18, F10 15-26-05, Jungle (3539,-4154), camera (-0.121, -1.913, 0). "cant hear him barrcata." Actor 61 stands at (3550, 0, -4152), about 10 away. Prop 552 is at (3592, -15, -4145), about 53 away.
2. On the chain. This is the meeting that starts the escort. A silent line stops the player from hearing the talk. The lead asked for the line to be audible at talk range.
3. Intent: you walk up to Baccata and hear him. Reveal, then the escort.
4. Contract: walk into region 1921, walk up to prop 552, press E. The wake clip (prop selector 1) has no audio. The next selectors do. At the reported pose that line is inside max_distance and on the speaker. Unit size 300, attenuation disabled, max_distance 1200, and the Master bus stay.
5. Exact: which clip the host starts, the three owners (prop 552, actor 61, guard 60), unit size 300, ATTENUATION_DISABLED, max_distance 1200, Master bus. Approximate: the source sits 40 above the speaker, the same presentation Dawn uses. Grade DECODED for the positions and the reach. The mouth offset is the Dawn adapter.
6. Cheapest faithful: park the existing player on the speaker when the line starts, and keep it there while the clip shows. Raising max_distance would also play a source left at the origin. Moving the body would invent a new stance.
7. Earned: walk from the open floor west of region 1921 into it (the south edge is a bit0 wall). Walk the open floor from (3312,-3712), outside reach, to a stand west of the prop (the ground north and east of him is blocked). Press E. The listener then stands at the reported pose. PASS heard prop552 there. Actor 61's own clips start after that prop sequence, past 60 seconds, and use the same placement on his body.

## Source

Host scripts/lol2/jungle_bacatta.gd. Actor 61 source position (3550, 0, -4152). Prop 552 (3592, -15, -4145). The three talk players were children of the host and were never moved. Escort one-shots were already parked on body 61. Region 1921 group 3894 predicate 119 links the prop. Region 1912's south edge and regions 3786 and 3787 are bit0 blocked, so the walks stay on the open floor.
