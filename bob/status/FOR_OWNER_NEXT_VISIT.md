# For your next visit (lead, updated 14 November 2026, 15:00)

## News first (14 November, morning)
- **The robot reached the ending.** With real keyboard input it has now walked every level from the Ruloi Citadel to the end of the game: Citadel, Dreamstone, back to the Temple, City of the Ancients, Hidden Caverns, Belial's caverns, Dawn, the final level, Expel into the mother beast, Belial, the ending. This was done in separate sittings from set-up starts, not yet as one continuous life; that run is ordered next.
- **Your milestone "the Dreamstone and back to the Temple" is walked by the robot** in one life. Your own walk is the other half.
- **All eight main-quest spells are built** (Dampen, Curse 2, 3 and 5, Mists 1 and 3, Prism 5, Summon 3). The "press E" stand-ins at the crevasse, the ghostly heads, the mother beast and the false Scotia are gone: you cast now. Number keys pick a school, Q casts, Ctrl+Q and Shift+Q are the stronger charges.
- **A question on the stored spells:** what was built is scrolls for Spark, Mists and Prism (first use teaches the spell, later scrolls cast it and are used up). The Cemetery chargers and glass globes are unchanged. Is that what you meant by "the orbs are stored spells", or should a charged orb itself cast when used?

## Play this: build r19l (newest)
```
~/lol2_playtests/play_r19l.sh
```
Play normally, F10 where something is wrong. In the order I would find most useful:
1. **Huline Temple** from its arrival start (F2). The robot walks all of it now; your walk is the other half of your milestone.
2. **Claw Mountains** (F2), your full run with the two issues you know of. Changing form is now a spell: press 3, then Ctrl+Q.
3. **Ruloi Citadel** (F2) to the Dreamstone, if you have time: globe, eye, elevator, vault, light the spires with Spark, the 21 steps, the plates, kill every Ruloi before the web opens, the boss, the altar, the Dreamstone.

New since r19i, in plain words:
- **Temple:** no floor sheet sticks up in front of the closed doors 92/93.
- **Cemetery:** drawn room by room as in the original. Inside the Emperor's tomb the yard's floor no longer cuts across your view; the tomb reads as a room.
- **Belial's caverns:** corridor door 73 opens after you raise the channel. At the end of the long corridor the switch opens the way into the lift to Dawn; the lift opens its doors at both ends; saving while riding keeps the ride going; the door to the final level works.
- **Magic:** one spell book with the school pages; eight main-quest casts; scrolls that store a spell; old saves keep the spells they should have.
- **Claw Mountains:** turning into the lizard works right where you arrive (it was refused on sloped ground).
- **Cemetery objects:** chest panels, lids and crypt fronts are drawn only with their own room. One crypt doorway that showed a red void with floating blocks now shows the stone room. Tell me if your "chest panels outside the rooms" is gone; if not, F10 at that view.
- **Citadel:** the teleporter pad works when you step further onto it from its corner.

Not in r19l, so you do not look for it: the remaining Temple overlap zones (see the decision below), the starry floor and the chips in the City, the tiger-cave switch and the jungle shaft flood (Sol is building those from your words).

## A decision I need from you: what "no overlap" should mean
You decided the Classic maps must be adapted so rooms do not overlap. After a night of trying it on two levels, here is what we know.
- **Moving a room up or down works where the thing moved is closed in:** the Temple spider tunnel (now under the wooden room) and the Emperor's tomb floor in the Cemetery. Both are in your build and both fixed what you saw.
- **It does not work on open, roofless ground.** Raising a piece of the Cemetery yard or a roofless Temple room puts your eyes above the wall tops of the rooms around it; you look into rooms that have no roof drawn. Opus built one (Temple zone T6) and measured the Cemetery ones: 18 of 19 Cemetery zones and 6 Temple zones fail for this reason or because there is no room for a ramp or stair at the join.
- **Most overlap zones are not visible to a player at all.** None of the ten worst "other room shows through" views in the Cemetery lies in an overlap zone; the room tracking already keeps you out of the wrong room there.

My recommendation: change the goal from "no two rooms share space in the data" to "**nothing a player can see or feel**". That means: fix every spot you or the robot report (as with the tunnel, the trench, the tomb), keep the room tracking for the rest, and redraw a wing only where a reported spot cannot be fixed any other way. A full no-overlap redraw of the Temple and Cemetery would be months of map building for places nobody can see.
If you still want true zero overlap, the honest route is redrawing wings from the original map, starting with the Temple, and I would plan it after the start-to-finish walk.

## Two pictures for you to judge (no playing needed)
The Temple's remaining overlaps are harder than expected, so I want your eye before anything is built. Left column = now, right column = proposal.
1. `~/AI_COMMS/opus_lane/l14_sky_preview/L14_sky_before_after_sheet.png` - the Temple with a real night sky behind everything. Today the Temple is black wherever the original is black (for example the void around the ledge maze); with this change those places show the starry sky. Yes or no?
2. `~/AI_COMMS/opus_lane/t6_on_sky/T6_on_sky_sheet.png` - one overlapping room raised by 90 with three new short stairs, on top of that sky. Does a raised room with added stairs look acceptable to you as a way to end overlaps?
(For comparison, the same raised room WITHOUT the sky change, which I rejected: `~/AI_COMMS/opus_lane/t6_pilot/T6_before_after_sheet.png`.)

## In work while you play
- Sol: what a save keeps on every Act 2/3 level (already found and fixed: raised Temple floors were lost on load), then the tiger-cave switch, the jungle shaft flood and the Temple plant bed from your words. Item grants are built and waiting for review.
- Grok: one continuous life from the Citadel to the ending on r19k/r19l (three attempts stopped on the robot's own route in the Temple; the fourth is next), and three reviews.
- Opus: the general "loading a save does not replay a room's entry event" rule is built and waits for Grok's review.

## Sunday 15 November
The weekly review. I will ask you for the usage screenshots.

One-screen status per level: `~/AI_COMMS/status/STATUS.md`.
