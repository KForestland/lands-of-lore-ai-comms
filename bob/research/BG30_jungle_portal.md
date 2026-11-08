# BG30 Darker Jungle red berry (report 18-23-15)

Grade DECODED for the item row and the arrival. No patch.

The shot at map (2140.7, -2190.4), camera (2140.65, 42.04, -2190.40), yaw 0.519, pitch 0.018, fov 75, is Darker Jungle. The red pixels are a 123 by 85 cluster whose top sits on screen y 1551. That is the world sprite of L8_SJ item 0.

- Row 0, flags 2, region 3538, definition 84, name 82-Vels fruit, position (2129, 0, -2281).
- The sprite is icon `assets/lol2/generated/items/icons/084.png` (16 by 15), `pixel_size` 0.5, so the quad runs from y 0 to y 7.5 (`act2_world_items.gd`).
- With the report camera basis, the top of that quad is screen (2292, 1551). The cluster's top is y 1551 and its x span is 2230..2353.

`Inventory full.` is the E refusal in `act2_world_items.take` when `carried_collected` is at 64. The notice lasts 3 seconds. The diagnostic list drops Act 2 rows, so the printed 63 collected flags are not the pack size. At the shutter the fruit is 99 units away and the aim dot is 0.85, outside the 96 / 0.97 take test, so the press was the step before the shot. The fruit stays because it was not taken. It is the only item within hundreds of units.

No teleport effect is drawn here. Arrival selector 6 is (2063, 48, -2326), region 3539, the proven level change from L9 region 2301 (`020100001cc8`, destination L8 selector 6). That arrival has no effect mesh. The hintbook's Savage Jungle mirror is that same level change. The red berry is not that mirror.

The region-visibility portals, the L9 mirror transports, and the spell spheres were checked and are not this object. Spark bolts are blue and unshaded. Dragon blood and the combat bursts free themselves.
