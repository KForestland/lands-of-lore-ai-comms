# MONDAY 16 NOVEMBER: play this (lead, updated 03:50Z after your night test)

```
~/lol2_playtests/play_r19o8.sh
```

Your saves are carried over, including the ones from your test last night. **Load your last save at the web and go on.** F10 where you stop or something looks wrong.

**What stopped you last night, and what changed:**
- The web refused you because of a rule WE had added (every Ruloi dead). The original has no such rule at the web; it is gone. **E at the web now starts a movie of about 70 seconds (game paused, wait it out), then the boss.** The robot did exactly this from your last save: web, movie, boss, altar, Dreamstone, return pad, entrance slot, out.
- **Heal before the boss.** Your save arrives there nearly dead; the robot healed (2, then Ctrl+Q) and won with the sword in about 44 hits.
- **Altar first, then the Dreamstone** (the game says so).
- The black "orb" you tried is a real switch from the original that we have not built yet. It stays silent on this build; it is on the list.
- Mana comes back by itself (about 16 a minute). The game now says so when a cast is refused.
- All "every Ruloi dead" now belongs only to freeing the women, as you said; their line counts how many remain and names the light fixture above the eggs (break it with Spark).

**The way home with the Dreamstone:** the Journal tells you. At the ice opening: jump onto an ice floe (the original way), or **E - Climb down to the icy gulch** (our shortcut). Then the jungle, the Temple door (place the stone, take it back, enter).

**In the Temple:** every step of the ritual is named on screen when you face it. One place needs a trick: to get back up from the low passage, be the lizard, back well away from the ledge, then run and jump (the screen says so on this build).

**At the Temple boss (Hive Lord):** G changes you to the Beast; if you stand on a step edge the screen now tells you to move onto open floor, and the change comes. Five hits as the Beast. A Dreamstone left in a slot comes back to your pack by itself when you walk away.

**In the City of the Ancients (state 07:00Z, still being walked):** the main road is: south-avenue fountain (strike the floating ball) -> glass pyramid (one Silverleaf) and hourglass -> then TURN AWAY from the tower doors it opens -> the canal -> the oil stair -> ignite the oil -> take the Dark Bow -> the dragon room (chop the dragon) -> the telepad to the Hidden Caverns. **Do not go up the tower lift to the starry floor** (not finished: nothing to do there and the floor ends in a fall), and leave the four tower sections and the ivory chips. **In the City, keep to the streets, and step up onto raised walkways head-on.** On this level the drawn walls did not stop the body, and a low step onto an arcade can let you slip under its floor; either way you fall into the void and the game now says "You fall and wake at the arrival lift." Tonight's build closes the amphitheater and the bank terrace. A second build, `play_r19o9.sh`, closes about 5,400 more walls in the City; if you keep falling there, quit and start that one (your saves are copied). It stays the second choice tonight: the robot walked the canal road on it cleanly through the oil stair and three doors, then was stopped at one corner further on that is not yet explained.

**Closed doors along the City canal show no prompt: face them and press E.**

**Keep at least ONE Silverleaf** for the City of the Ancients pyramid.

Walked by the robot on your own save, no help (state 05:00Z): the Citadel from your stop to the exit; the Claw Mountains both ways down; the Darker Jungle; the Temple door; the whole Huline Temple - ritual, three trials, three idols, the hopper platform, the Hive Lord (five hits as the Beast, you end at 24 health), the chalice - and the arrival in the City of the Ancients. The City, the Hidden Caverns, Belial's caverns and the final level are still ahead of it; what it finds there I add below.

For reading, if you like: `AI_COMMS/grok_research/L13_PLAYER_WALKTHROUGH_20261116.md` - the original Citadel in 14 steps from your longplay and the hint book (the elevator is a ride, not a cutscene; the original shows a "Remaining Ruloi N/19" counter, which we will add).

Fallbacks: `play_r19o7.sh`, `play_r19o6.sh`, `play_r19o5.sh`, `play_r19o4.sh`, `play_r19o.sh`.

**Decision for you:** should the "E - Climb down" shortcut stay in Classic? I lean yes, as an option.

**A job only you can do (security, 10 minutes, not urgent tonight):** the folder `~/AI_COMMS` is a git repository whose remote address contains a GitHub access token in plain text (in `.git/config`). Nothing of yours has been pushed from it, and we have now excluded your F10 bundles and saves from that repository. But the token should be replaced: on GitHub, revoke that token and make a new one; then set the remote without the token and let a credential helper hold it. Ask me and I walk you through it step by step.

---

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
