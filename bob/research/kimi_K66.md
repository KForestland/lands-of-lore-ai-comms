# Kimi K66 — WHATS_NEW_r19 draft material (lead verifies before publishing)

# WHATS_NEW_r19 — draft material

LoL2 build r19 (2026-11-09) — start with `~/lol2_playtests/oct23/play_r19.sh` once the qualified build lands (qualification is running now, target Wednesday evening). Same save folder as r14–r18. Contains everything in r18 plus:

## FIXED FROM YOUR r18 PLAYTEST
- The drowning veil now spans the whole window, and jumping on the Cave river bridge no longer starts the drowning clock (only jumping from the water counts).
- The cat ladies stand on the clearing floor instead of in the ground.
- Cave crates can be shoved at human reach and stay where you push them.
- The Cave Draracle door is there again and opens when you use it.
- The green rectangle and the floating dark beam in the Jungle sky are gone (bogus ceiling spans, not drawn anymore).
- The cat-woman talk in the Jungle that only fired when you jumped now starts when you simply walk up.
- Baccata's voice is audible where you meet him.
- The L8 cache ladder works both ways, as often as you like.
- The straw pit on the Larkhon approach is armed and hidden until you walk into it.
- The pitch-dark L8 spot is now lit by the skull torches.
- The L8 temple door says plainly it is sealed and only the Dreamstone opens it, instead of looking broken.
- Closed as original behaviour, not bugs: the cave guard who vanishes after talking (he dies in the original) and there being no Huline at the village entrance before your temple visit.
- Still parked for later: the Hive texture pass, the museum wall redo.

**Held back from r18, now in:** the Jungle bramble walls block until 3 sword cuts (they regrow; Spark burns them for good); the Jungle bridge decks are solid to walk on; the L8 boundary hedges block; Sol's Dark Halls work is restored (sliding panels, bookcase doors, crouch everywhere).

## THE MAIN CHAIN NOW (from the F2 Darker Jungle start — every step walked in testing)
- **L8:** priest scene → village guard → Daniel's blade → the tribe → shaman: Silverleaf + Amaranth → Larkhon Vapors → the Larkhon sleeps → the pass to the Claw Mountains. Rescuing Baccata is optional again (our gate at the citadel was removed — see below).
- **L12 Claw Mountains:** out of the gulch → avalanche valley → glacier drop → ice hops → Kenneth's body and charm → Baccata in the tunnel → the citadel scene (Space skips the movie) → L13.
- **L13 Ruloi Citadel:** egg basin → elevator → maidens → free Dawn → pink steps → the bridge → first Belial → Dark Sword altar → the Dreamstone → out.
- **Back through L12:** ice cave → river raft → Spark the niche tripod (obsidian mail) → floe back → crevasse as the Lizard → melt the frozen figure and catch the blue bow → glacier logs → gulch → the L8 river return → the temple door (Dreamstone in, take it back).
- **L14 Huline Temple:** priest to the slab → aloe/poison ritual → two green shards → the hanging and spiders → the flute → machines → bedroom and library → floating bowls → spiral stair (Dreamstone slot — remember to take it back) → the three trials → flute in the oil slot → blade/boulder bypass → idols on pedestals → hopper platform → faux Belial as the Beast → the Chamber of Voices: offer the Dreamstone → the city resurfaces → L16.
- **L16 City of the Ancients:** arrival elevator → dry fountain → greenhouse → the NE tower lift to the starry floor → burn the prop at the SE oil fountain (doors open, the Dark Bow) → centre pads → the mantle → dragon room → the exit to L17.
- **L17 caverns:** through the throat on foot → cut the red strands with a blade → carried across to the exit block → walk to the L19 arrival.
- **L19:** strike the bars (the guck floods the corridor) → G at the gutter mouth to crawl through as the Lizard → shoot the three wall switches with the bow → the bars open → wade the guck → take Belial's Horn from the shaft rim → the ghostly heads → Dawn's elevator (the golden doors recall the cab, the lever rides down) → Dawn's room → L20.
- **L20:** attack the closed doors to open them → the mother → five fire shots open the blue-pillar deck → Trinity's carrier carries you across → armory, faux Draracle, the ending sequence (as in r18).

## NEW
- **The readable Atlas (M):** real walls vs openings, named places, ways out, and plot markers from your Journal notes that clear when done — Jungle, L8, L12, L13 and L14 so far. Storeys no longer shatter the map into pieces; small windows keep the classic sheet.
- Act 3 prompts and captions now read as game text instead of builder's notes.
- Your first good/evil soul point on the L8 shore is recorded properly.

## HONEST STATUS / WHERE IT STOPS
- **L19 clicks:** hitting the bars and shooting the switches respond to scripted strikes, but real mouse clicks on them currently do nothing — known, being fixed now; if it misses the build, that is your real end point in L19. F10 it.
- The L19 blood pool is wadeable now, but the narrow channel can still wedge the body; a fix is in flight.
- The guck is proper liquid (wade/swim) but no longer drains health or mana — removed on purpose: the original drain rate is not decoded yet, and we do not invent numbers.
- The carry across the L17 pit after cutting the strands is a stand-in (the original beast scene is not decoded).
- The L20 birth: the mother dies as before, but the original's post-birth relocation still does not fire, and there is no real door at her room (the original data has none).
- Movies not yet decoded (the birth film and friends) remain caption cards.
- The L12 avalanche is still a stand-in effect; the gorilla village, tiger cave and lake platform are inert side content; the L14 stone cubes are not hosted (optional in the book).
- L16: the Mantle Gate and the box/disk/yellow figure have no entries in the original data and stay unbound; the dragon-room mouth and one tapestry are walk-through, matching the longplay.
- **Removed on purpose:** the Baccata requirement at the citadel entrance (our invention — the original has no such check, and it could dead-end you) and the guck drain (above).
- Dark Halls: the restored panels, bookcases and crouch are in; the follow-up puzzles (blast crates, window escape, atrium, orb) are still being built and are **not** in r19.

## PLEASE TEST
1. The Atlas (M) as you go: are walls, exits, place names and Journal markers right and readable — especially L8 and L12?
2. L8 route: temple → guard → Daniel's blade → tribe → shaman → Larkhon dose → the pass. Clear without any hints from me?
3. The straw pit: hidden until you fall in, escapable, and still right after a save/reload?
4. L12 and L13, one sitting each: does anything stall (avalanche, Kenneth, Baccata, movie skip, elevator, Belial, Dreamstone)?
5. L14: watch Dreamstone custody — the spiral slot must give it back, you need it carried for the Beast fight, and the chalice consumes it. Report any dead end.
6. L16 into L17: starry floor, oil doors, dragon room, the terrace ramps, then the caverns and the strand cut.
7. L19/L20: the bars, the gutter, the bow switches, guck wading (tell me if no damage feels wrong), the horn from the rim, Dawn's elevator, hit-to-open doors, blue pillars and the carrier, the ending. Anything stuck: Journal first, then F10.

---

Two caveats for you: r19 is not qualified yet (the combined sweep was still running at the last board entry, and the L19 real-click fix BK08d was still in progress), so the notes above describe r19-work HEAD `c6a7b8e` plus explicitly flag what may still change before Thursday. Also, the Dark Halls detour is off your Darker Jungle route — I kept it to one held-back line each in sections 1 and 4.

