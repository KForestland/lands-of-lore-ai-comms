# For your next visit (lead, updated 15 November 2026, 07:50)

## News first (14 November)
- **One unbroken life from the Citadel to the ending** (23:14Z, on the code of your build r19n): no reload, no aids, no deaths. Seven earlier lives stopped, six on the robot's own route and one on a real fault: Mists of Doom was only taught by an optional scroll, so a player could get stuck at the four ghostly heads. That is fixed in r19n.
- **Act 1 from New Game** is walked by the robot through the Cave, the Museum, the Jungle, the flute route, the wax and the runes; it stalls on the walk back with the runes, which only happens in the robot's long run (a clean test of the same path passes). Opus is finding out what stands in the way.
- **The robot reached the ending.** With real keyboard input it has now walked every level from the Ruloi Citadel to the end of the game: Citadel, Dreamstone, back to the Temple, City of the Ancients, Hidden Caverns, Belial's caverns, Dawn, the final level, Expel into the mother beast, Belial, the ending. This was done in separate sittings from set-up starts, not yet as one continuous life; that run is ordered next.
- **Your milestone "the Dreamstone and back to the Temple" is walked by the robot** in one life. Your own walk is the other half.
- **All eight main-quest spells are built** (Dampen, Curse 2, 3 and 5, Mists 1 and 3, Prism 5, Summon 3). The "press E" stand-ins at the crevasse, the ghostly heads, the mother beast and the false Scotia are gone: you cast now. Number keys pick a school, Q casts, Ctrl+Q and Shift+Q are the stronger charges.
- **A question on the stored spells:** what was built is scrolls for Spark, Mists and Prism (first use teaches the spell, later scrolls cast it and are used up). The Cemetery chargers and glass globes are unchanged. Is that what you meant by "the orbs are stored spells", or should a charged orb itself cast when used?

## Play this: build r19o (newest)
```
~/lol2_playtests/play_r19o.sh
```
Your saves from r19n are carried over. **Monday's run: continue from the Ruloi Citadel toward the ending** - the Dreamstone, the Temple, the City of the Ancients, the Hidden Caverns, Belial's caverns, the final level. Only the robot has walked that stretch. F10 where you stop or something is wrong.
A newer build (r19p: this plus the hut wall, objects on nine more levels, the items, and the belt if its review passes) may replace this line before you start; use whatever stands here.

New in r19o, the three fixes from your run on 15 November:
- **Cemetery yard:** you no longer get stuck under the low ledge along the wall.
- **Cemetery passage:** the door now opens flat to the wall, so you fit past it.
- **Ruloi Citadel:** pressing E at a dark globe or a closed door tells you which spell to cast (1, then Q). The spires, the eye, the vent, the lift and the web explain themselves the same way, and each sentence goes into your Journal.

Not fixed yet from your run: the invisible wall at the hut mixer in the Savage Jungle (cause found, fix next), the Dark Halls crates, barrels and box, the Hive puzzle, the clipping around the Emperor's stairs, the Temple overlap you marked.

Keys: number keys pick a spell school, Q casts, Ctrl+Q and Shift+Q are the stronger charges; changing form is 3 then Ctrl+Q; Dark Halls bookcases slide on E.

## Decided on 15 November (for the record)
- Maps: the goal is that they work with no glitching, not zero overlap in the data.
- The Cemetery glass orbs are stored spells the player can use (yellow Spark, white Prism, blue Mists of Doom is my provisional mapping - please confirm the colours, and what the white orb did).
- A five-slot item belt, as smart as possible; F uses the active item on yourself.
- The good and evil paths wait until the game is playable.
- All five review ideas: the robot plays like you, your inputs are replayed on each build, an unstick safety net, no silent refusal, one-key note types on F10.

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


## Added 15 Nov evening (lead)
- **One thing to avoid on Monday:** keep at least ONE Silverleaf. The City of the Ancients pyramid needs one, and the inventory lets you spend them for mana. Your City save holds six.
- The build for Monday is being decided between r19o2 and r19o3 (r19o plus Citadel fixes found by the robot playing your own save: pink steps, the Ruloi above the lift, the pad hint). The launcher line will be written at the top of this file before you are home.
