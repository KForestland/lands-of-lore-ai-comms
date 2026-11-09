# L16 dragon-room mouth — movable 103

Place L16_CA. Walk 3 stopped on movable 103 (`/tmp/l16exit-act3/tmp/regressions/l16walk3/l16_exit_earned_test.log`). Walk 4 crossed that mouth and stopped on the tapestry plane (`l16walk4`). Name-at-index stays LIKELY. Opcode 197 arms 6/7 were already hosted as bit 2 of byte +0x19, not the movement-drop bits.

## Duck

1. The oil-chain walk reaches the dragon-room mouth and stays there. Region 8456, pose about (1623, 62, 5348). Three sittings of this walk have died; this is the first stop at the mouth. The earlier two died on actor 46 and on doors 82/83.

2. It is on the chain. The L17 exit is the chop and control 74. Kimi's board line says that exit only needs the dragon chop.

3. Intent: the player walks into the dragon room, chops the dragon, and the blood opens the door behind it. Hintbook lines 5269–5288. Brady printed 234. Grade HINTBOOK for the chop and the secret door. The mouth itself is not named as a switch.

4. Contract: walk in from the city, chop prop 241, the door behind the dragon opens, the telepad is one-way. This mouth is north of the tapestry (control 92 at Godot z 5181). The dragon is at Godot z 4417. The blood plate is control 73. Neither names movable 103.

5. EXACT: the solid bit, the travel word, and which region bits a command sets. A travel-100 write is not in the data, so it was not added. APPROXIMATE: nothing here is only presentation. Dropping the trimesh would ignore the solid bit, so it was not applied.

6. Cheapest faithful option that was not taken: leave the drawn faces and stop colliding this one movable while region 9622's drop bits stay clear. That matches a region mover crossing a region the blocker pack does not list. It contradicts word +8 bit 0x80, so it waits for a decision. A second prism is not this shape. A teleport is not this shape.

7. The walk already stands at the reported pose. The L17 arrival save did not run.

## What the walk had already crossed

One sitting from the oil-chain save. Save and reload is only at the L17 arrival, and that line did not run. In order: the canal reverse, the terrace link, control 80, door 100, actor 46, door 84, props 128 and 127, doors 82 and 83, region 218 at about (5511, 32, 9876), control 79 at (−3923, −8, 7619), then the dragon approach through fixture point 61. The next goal is fixture point 0, (1623, 5180), control 92. The body never reached the chop.

## The slab

Movable 103, placement `55062feb00001e0082059625324f0000dc745a0034747f0000000000010094003b0106022d12000000`. Godot (1621, 30, 5329). Byte +0x20 is 59. The 30-byte static run at file 19098082, checked against index 0 and the known neighbours, has index 59 `Door`. Grade LIKELY. Byte +0x22 is 6 (rotary). Byte +0x24 is 45. Word +8 is 0x0582, so bit 0x80 is set.

The local faces are a slab: x 1596–1646, y 30–130, z 5325–5333. Materials 1236 and 1288, plus a small plaque on the faces. Five more faces of source index 103 sit near (−11670, 8410) and are not this corridor. Region 9622 is the only floor between region 8456 (south edge z 5340) and region 8457 (north edge z 5320): x 1596–1647, z 5320–5340, floor 30. It is absent from `region_blockers/L16_CA.json`. The side gaps to the source walls at x 1580 and x 1660 are 16 and 14, and those strips are not region 9622.

`_build_hinges` gives every movable face a trimesh. It does not read bit 0x80. At travel 0 a mode-6 hinge does not yaw, so the slab stays across the floor. The stall pose is on the north side of that slab.

## Commands

Movable 103 has three events and no kind 4.

- Kind 6 value 16, group 50346, `0606aac41000`. One command: opcode 197 arm 7, `c59096250700`, region 9622. Arm 7 sets bit 2 of byte +0x19 on the 42-byte region record. Arms 0–5 are the bits the movement check drops a region on. Arm 7 is not those bits.
- Kind 6 value 15, group 50352, `0606b0c40f00`. Opcode 14 arm 3 starts the timer on movable 103.
- Kind 2 value 48, group 50360, `0a02b8c4300105002c01`. Opcode 14 arm 4 stops that timer. Opcode 1 is `012067000000`, travel 0.

The only opcode 1 in L16 whose target is movable 103 is that travel 0. Kind 6 values 15 and 16 are the cave-gate shape (raised / lowered callbacks while a movable is already travelling). Nothing here writes a non-zero travel, so those callbacks have nothing to ride.

Movable 73, the same static slot, at native (−9801, −13277), has the same three events: opcode 197 arm 7 on region 10066, the timer, and travel 0. Movables 104–111 are the same slot with flags 0x0182 (bit 0x80 clear) and no events. They sit at x 1473–1766, off this corridor.

Prop 241 and control 73 do not name movable 103. Region 8456's kind 12 group 6868 starts a timer on prop 421. Region 9622's group 7126 stops it. Prop 421's kind 2 group is opcode 15 on the side pillars 433–442, not the door.

## Frames

g_00319 at 4:28:40 looks down an open hall at the winged mural. g_00321 at 4:29:40 is inside, beside that mural and a gold column. No opened frame shows the slab swinging. Hintbook 5278-5288 says the door that opens is behind the dragon, after the blood. Grade LONGPLAY for the open hall and the interior. Grade HINTBOOK for the blood door.

## Adapter

Collision on movable 103 only is removed. The drawn faces stay. Region 9622 is unchanged. Piece 0368. Walk 4 logged `MOUTH 103 collision dropped, meshes 3` and entered region 8457.

## Tapestry plane

Walk 4 then stood at about (1623, 62, 5196), region 8457, short of fixture point (1623, 5180). The collider is face 30077, static assembly 92, one quad x 1560-1680, y 30-130, z 5181, material 425. Movable 92 is the north-east FireWall at Godot z -2947 and is not this face. Control 92 shares the tapestry placement. Kind 4 does not clear the solid bit. Kind 6 value 2 (group 42286) runs opcode 9 arm 8, which does. The control-event caller is not known, so that event is not hosted. g_00319 and g_00321 already show the player inside at the mural, and no opened frame shows this plane swinging. Collision on static assembly 92 only is omitted. The drawn face stays. Piece 0369. The earned walk is the check. BK04 waits on that walk.
