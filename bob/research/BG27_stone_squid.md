# BG27 stone squid

Owner r17 18-19-21. The capture is Dragon Level, camera (4682, 26, -4512), yaw -2.829. The corner names StSquid. Strike landed is the player's hit.

The nearest StSquid is actor 58, definition 0, at (4883, 2, -4535), about 200 units off, behavior byte 6, flags 0x4482, present. Actors 61 and 68 are the opening pair, far from this pose, same definition and the same byte.

`prepare_act2_creatures.py` stores placement byte 37 and does not read it. The live population hunts on sight. One profile names byte 6 Wander for a Jungle villager. That name was not replayed for StSquid.

The attack the port plays is selector 2: kind 1 hit, frame 5, 100 percent, damage 15. Selector 3 uses the same pictures and adds kind 3, frame 4, value 82. Those frames are a lunge, not a bolt in the sprite. Kind 3 value 82 was not decoded, so no plasma was added.

No patch. Smallest adapter, not applied: hold definition 0 at its placement. The shot stays unread.
