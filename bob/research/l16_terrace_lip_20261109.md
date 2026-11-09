# L16 terrace lip — exit walk stopped here (2026-11-09)

Duck for the BJ09 continuation (oil-chain save to the L17 exit). The collider is posted; see section 9. BK04 not started.

## 1. The problem

Luther leaves the SE oil room, reverses the canal, and cannot get off the floor-30 bank onto the city terrace. Earned run in `/tmp/l16exit-act3` (detached fd6db6b, BK12 applied only in that scratch) stopped at (-4820, 62, 15639), against region 4959. Scratch left in place. Not a release.

## 2. On the chain

Yes. The centre (control 80), the mantle bars, the dragon, and the L17 exit are all past this bank. Parking it parks the walk.

## 3. What the game is doing

*Orient.* The bank is the canal side of the city. The terrace (floor 95) is the street you walk to the centre pad and the dragon. Not a key, not a spell, not a door.

## 4. What the player does

Walk up off the canal bank into the city. BK11 already walked the other way: the oil-chain route drops off the terrace. Its board line says region 4947 is 55 degrees, so the body slides onto region 4946. The oil shelf the other direction (floor 30 onto region 5294, floor 90, rise 60) is a jump, and that jump is posted.

## 5. Exact vs approximate

Exact: the body has to cross one of the region links below. No item, no control, no movable sits on them.

Approximate, and where the port misses: native movement is the region graph. The port builds one floor quad per region. These quads run from y=30 to y=100.

## 6. What was measured

Walkable pocket from region 4957, official neighbours, rise and drop at most 32: 81 regions, every floor 30.

Official exits from that pocket:

- Ten climbs of +65 onto floor 95: 4945->4932, 4947->4931, 4949->4968, 4953->4969, 4954->4970, 4958->4972, 4959->4971, 4961->4967, 4965->4930, 4966->4929.
- One drop of 80 into region 8876 (floor -50) at about (100, 13773). That pit is 18 regions, floors -60 and -50, and it does not reach control 80 or the south stairs.

Each of the ten quads is about 54 degrees (53 to 58 measured on the two triangles). The walk floor angle is 45, so the quad is not a floor. try_step rejects the same normal and only rises 32.

Jump in `move_grounded`: launch 200, gravity 320 per passed 1/60 step, same numbers the oil test uses. Discrete rise of the body origin is 64. Standing on floor 95 from floor 30 needs 65 (foot offset 32 both sides). The run reached y=126 from y=62 and came back down. The crest of the quad is y=100, and the shelf floor behind it is y=95 with a 5-unit source wall on the shared edge, so the arc also does not clear the crest (stand height 132).

Flat +45 ledges on the same bank (4905->4901 and the three neighbours, floor 75, edge length about 170 to 190) do not connect to control 80. Their component is nine regions, floors 75, 90, and 94.

No shared-edge route with a rise of 45 or less reaches control 80 without leaving the real neighbour graph. The south stairs the oil chain climbed (region 4886 floor 0, 4911 floor 20, 4915 floor 60, 4932 floor 95) are on the far side of this terrace. Getting there from the bank is one of the ten +65 links.

## 7. Options

- Pose Luther across the edge when he stands on it. That is a pop of 65. A player would see it. Not applied.
- Raise the global jump. Launch 202 clears a rise of 65 in the same discrete sum. That changes every jump in the game. Not applied.
- Region-aware floor, the same idea as Fable's L17 collision note: the body walks the region floor instead of the sloped quad. That is an engine change, and it is the lead's.

Smallest note for the lead: the native step is the region link. The port quad is the blocker. A pose was not applied.

## 8. What would unpark it

The body stands on floor 95 past one of those ten edges after walking up to it, with no pop, and the earned run then continues to control 80. BK04 stays behind that.

## 9. Collider hosted

The ten links keep their drawn floor quads. Collision on each quad is a prism from y=30 to y=95 at 40 degrees, the deck-ramp family (row 0339), scoped to these edges. Piece 0367. Patch `L16_terrace_lips.patch`, apply-checked on fd6db6b. The earned lip test walks from region 4956 onto region 4971. The oil-chain walk still reaches region 4946. The walk on to the L17 exit continues from here.
