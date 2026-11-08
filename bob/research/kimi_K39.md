# Kimi K39 — r18 player-visible changes (373b5d7..r18-work), 2026-11-08

Lead: source material for WHATS_NEW_r18 (lead writes the owner text after qualification).

All data gathered. Here are the release notes.

  # r18 release notes — changes since r17 (373b5d7..r18-work)

  ## (a) Fixes from the owner's r17 playtest reports

  - **16-30-49** — Museum: the broken Thohan sword now comes away from its case when you look at it level and press E; a held item is put away first (adapter).
  - **16-33-54** — Museum: the niche wall plate in the scroll hall now stands out from the wall and a level look presses it; it slides up and the opening is clear — no more softlock (adapter).
  - **16-36-49 / 16-36-57** — Museum: the ceiling dust pile hangs down from the ceiling again instead of lying flat (adapter).
  - **16-37-36** — Museum: the long beam slides into its low slot and stays at its placed height, and the dragon door then opens (adapter).
  - **16-37-59** — Museum: clicking inside the dragon chamber starts the dragon journey; E still works too (adapter).
  - **16-39-14** — Jungle: the two planks on the ground only appear after the beast breaks the village doors, not before (adapter).
  - **16-40-18** — Jungle: the two cat ladies now stand in the clearing and tell you about the missing cats when you press E (adapter).
  - **16-44-37 / 16-44-57** — Jungle: the torn bramble wall now blocks the path; three sword cuts open it (it grows back), and a spark burns it down for good (adapter).
  - **16-49-32** — Hive: the cat woman in conversation is drawn about Luther's height instead of three metres tall (adapter).
  - **16-52-10 / 16-52-23** — Jungle shop: the bow, sword, and bracer are visible pictures in Huline's shop and each can be clicked (adapter).
  - **16-54-13** — Jungle: every stream bridge deck is solid now — Human and Lizard can walk across all of them (adapter).
  - **17-00-05** — Jungle: a black roof now closes the river gorge from inside, so sky and treetops no longer show through (adapter).
  - **17-01-09** — Jungle: the hidden wall above the gorge bank no longer blocks the walk along the south bank (adapter).
  - **17-36-46** — Jungle: Dawn's voice now plays at her body, so her line at the talk spot can be heard (adapter).
  - **17-50-18 / 17-50-38 / 17-50-53** — Darker Jungle: the floating bark sheets above the hedges are no longer drawn; the hedges themselves stay (adapter).
  - **17-59-34** — Darker Jungle: a hedge wall on the map boundary now stops the player; hedges between two regions stay walkable (decoded, not an adapter).
  - **17-53-55 / 17-55-42** — Darker Jungle village: the guard now tells Luther on screen to visit the Huline Temple first (east of the entry, far side of the map) instead of silently refusing entry (adapter).
  - **17-57-09 / 18-08-06** — Darker Jungle: the tree bridge can actually be chopped with a held weapon and walked across, and the cache ladder now climbs to the ledge and leaves you standing there (adapter: flush deck and landing).
  - **18-06-16** — Darker Jungle village: verified by an earned walk that the guard is present on the first approach after the temple visit (test only).
  - **16-48-43** — Hive lava bridge: verified by an earned test that the bridge floor material is opaque and draws the stone from the owner's position (test only — see the still-open list for the rest).
  - **16-53-49** — Jungle waterfall: verified by an earned test that the waterfall picture draws textured again (it was flattened by the reverted grey sheets) (test only — see the still-open list).

  ## (b) Act 3 is now playable end to end

  - **Ending**: one blow with the blue bow, the Dark Sword, or Belial's Horn starts the ending — chasm, the vow, the slump, Luther with Dawn, the Draracle drops in and leaves — each beat waits two seconds, a finished flag is stored, and a credits stub follows the last card (adapter; the ending movie is not in the table, so it plays as cards).
  - **Faux Draracle**: in Human form, any weapon drops the false Draracle; the crystal keys then open in order and the door leaf rises (adapter — the leaf's native move is not decoded).
  - **Mother and birth**: Dawn's third click grants the Ruby of Truth; ancient-magic level 5 sends it into the mother; the birth plays and a later blow drops the demons and opens the birth door; two seconds after the demons fall the mother dies on her own and L20 stays cleared across a save (adapters; the birth movie is a card).
  - **Pillars and armory**: five fire shots plus a level-five Trinity open a visible path and Scotia falls; one Human blow in the armory hacks the western block, breaks the three props, and stops the pillars (adapters).
  - **Heads, sewer, horn**: four head shots drag a token onto a white circle beside a red fountain; Human form raises the sewer bars, Lizard form enters the gutter; taking the horn shows "Baccata is dead" (adapters).
  - **Beast wall / L17**: red strand and frond meshes show at the beast wall, a card plays the beast scene, and Luther takes one step in on arrival 1 only; the L17 west wall is cut by a Human blade and records its movie as a card (adapters).
  - **L16 towers**: the NE lift carries Luther up once the greenhouse doors are open; burning the SE oil reveals the Dark Bow and opens a drain mouth; four placed ivory chips in the SW show the force field, gargoyle, ice fountain, and ceiling drop; dropping the centre foe raises a Mantle Gate leaf (adapters).

  ## (c) Dark Halls (owner reports 17-06-40..17-21-59, in part)

  - **Wall slides**: the six wall slots toggle open and closed with E and show the original shutter texture variants (adapter: E aiming replaces the native object click; no panel translation; slide sounds are logged, not played).
  - **Bookcase doors**: three bookcases now work as doors — two open and stay open, one toggles — with solid leaves that slide sideways (the sideways direction is a presentation adapter).
  - **Crouch everywhere**: the Human crouch (hold C) now works in every area, not just the Museum, and standing back up under a low ceiling fits you properly — the native Dark Halls crawl gap is an earned target (adapter).
  - The ledger still marks slides, bookcases, and crouch **in progress**: some earned walks, original-motion comparisons, and owner acceptance remain open gates.

  ## (d) Huline Temple — visibility islands

  - The temple now draws room by room using the pack's own room records: you see into another room only through a genuine opening, so upper halls no longer show through lower rooms and vice versa (adapter; drawing only — collision, doors, trials, saves unchanged).
  - The background is a black void, and the night panorama appears only through ceilings that have no surface in the original, as the longplay shows (adapter ceiling polygons).

  ## (e) Maps and look (Hive, Jungle, L8, L10)

  - **Hive**: floors and ceilings whose native material is undecoded (the roof, the lava-river segment, the slab) now take a neighbouring real material instead of the grey-green placeholder (adapter).
  - **Hive**: the view walk seeds around the camera, so the deep hall's walls no longer pop in only after you take a step (adapter; owner 17-28-43/17-29-06).
  - **L10 (and Hive, L13)**: stair-step floor regions without nav polygons are now always drawn — fixes the missing floor texture the owner stood on at L10 ("lacks this texture", 17-55-17) and the sky-stripes hole (adapter).
  - Jungle gorge roof/bank, L8 hedge risers and boundary hedges, and the Jungle bridge decks are map fixes too, listed under (a) with their report ids.

  ## (f) Other

  - **Water on the player side**: when the camera goes below a liquid surface you get a blue-green tint, fog, and muffled audio; while the 15-second clock runs Luther sinks, and drowning slides him to the bed; one draw-only water sheet with the real water material covers Jungle region 2559 — nothing else was touched (adapter).
  - **Reverted grey water sheets**: the r17 water sheets and side skirts that painted flat grey over every stream, under bridges, and as floating slabs (owner 16-53-33, 16-54-53, 16-55-51, 16-56-02) are withdrawn; the two original water gaps stay until a limited fix with the real material lands (region 2559 got its sheet via the item above; region 260 remains open).

  ## Still NOT reachable or NOT visible

  - **Movies are still cards, not films**: the ending (e224e.vqa), the birth (placenta.vqa), the beast scene, and the L17 wall-cut movie (hw01.vqa) all play as named cards because the movies are not in the movie table.
  - **Open owner rows**: 16-53-49 (the waterfall picture draws again but there is still no point-and-click hotspot), 16-48-43 (the bridge floor is verified opaque, but the owner's "bad stone animation" complaint stands), 16-23-39 (Cave crates still can't be pushed or stacked), 16-25-58 (the door before the Draracle chamber is still not drawn), 18-14-46 (L10 broadly unfinished in look), 18-22-43 (L12 texture issues), 18-19-21 (the L12 stone creature still walks instead of sitting still as a turret), 18-23-15 (a portal effect stays permanent after use), plus refine-phase rows: Museum slow descent (16-32-09), blocky jungle top (16-46-36), Hive gas look (16-47-07/17-47-23), L12 flame flicker (18-18-43).
  - **Temple lighting**: the islands work is visibility/drawing only; the Temple's native lighting is not reproduced (the ledger notes the native renderer's portal screen-clipping is not reproduced).
  - **The rest of the Dark Halls puzzles**: the two-spirit trap room, the roof/sunlight bell-fruit, the explosive boxes and spark wall, the ghost orb room, box clipping, foliage clipping, and the extra effects of props 465/416 are still not hosted; slides/bookcases/crouch remain marked in progress pending owner acceptance.
  - **Sounds**: the flute still has no sound (17-28-09), the audio start glitch (17-47-13..17-49-12) is unfixed, and the Dark Halls slide sounds are only logged — sound work is deferred ("sounds later" per the owner).

