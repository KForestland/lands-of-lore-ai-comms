# BG27 stone squid

Owner r17 18-19-21. The capture is Dragon Level, camera (4682.495, 36.028, -4512.624), rotation (-0.180, -2.829, 0). The corner names StSquid. "Strike landed." is the player's hit.

The nearest StSquid is actor 58, definition 0, at (4883, 2, -4535), about 200 units off, behavior byte 6, flags 0x4482, present. Actors 61 and 68 are the opening pair, far from this pose, same definition and the same byte. One Jungle profile names byte 6 Wander. That name was not replayed for StSquid, so byte 6 is not the stationary decode.

Selector 3 uses the same 14 pictures as selector 2 and adds frame-event kind 3 value 82 at frame 4. Those frames are a lunge, not a bolt in the sprite. Value 82 is unread.

The population now holds only actor 58 on its placement. At that frame it fires the existing plasma bolt (`dawn_spell_bolts.cast_plasma`), ranged at the player in sight. Melee damage from the clip is not applied for him. Actors 61 and 68 still hunt and still strike, because the opening walk meets 68 and 61 comes onto the path. Freezing every definition 0 would leave 61 off that path.

Grade: adapter, logged until event 82 is decoded. Patch `grok_research/patches/ACT3P2/BG27_stone_squid.patch`, against r18-work `3b6a929`. Unapplied.

PASS squid: approached actor 58 at (4883,-4535), it stayed, and the plasma bolt hit. The opening earned walk still defeats actors 61 and 68.
