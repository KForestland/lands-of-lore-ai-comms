# BB03 — LoL2 picture scenes (read-only inventory)

For a later Enhanced graybox. The kit in `AI_COMMS/GRAYBOX_KIT_DESIGN_20261107.md` was not started. Hotspots become trigger volumes or markers and keep these same numbers. Proposed id, matching the kit's `<edition>:<area>:<kind>:<id>`: `classic:<stem>:trigger:<hotspot id>`. Sprite clicks and actor rects are separate kinds (`sprite`, `actor`) and are not hotspot ids.

The picture list is the opcode-12 stem table `scripts/lol2/room_stems.json` in the live Act 3 tree (read only). Source `LOLG.DAT`, 46 slots, table file offset 1899152. The file's own scope line: the archive name is the stem cut at the first underscore plus `.mix`, as `0xED470` builds it, and which room each archive opens in play is UNKNOWN except where a doc below pins it. Rects are inclusive unless a line says otherwise. Canvas pages that state it are 640x400.

## Scenes with a hotspot table in the files read

### Thieves' den — `thieves_den.gd`

Intent: the yard boards, the cellar, the slot door, and Mauri's den. One picture chain. Flag 17 is the cellar walk-in latch.

| Stem | Index | Picture | Hotspot | Rect (x1,y1,x2,y2) | Click |
|---|---|---|---|---|---|
| text_ | 44 | TEXT, the yard | 0 | 294,218–554,344 | room TCEL, exit |
| tcel_ | 16 | TCEL, the cellar | 0 | 0,247–162,378 | movie speaker 2, line 26, format 24 |
| tcel_ | 16 | | 1 | 317,255–383,307 | unhandled |
| tcel_ | 16 | | 2 | 250,170–381,302 | room TDOOR, exit |
| tcel_ | 16 | | 3 | 457,244–525,322 | unhandled |
| tcel_ | 16 | | 4 | 0,160–100,215 | unhandled |
| tcel_ | 16 | | 5 | 265,48–314,93 | unhandled |
| tcel_ | 16 | | 6 | 161,196–207,319 | unhandled |
| tdoor_ | 17 | TDOOR, the slot door | 0 | 147,109–471,399 | Confidante door. See below. Any other id is unhandled. |
| tint_ | 18 | TINT, Mauri's den | 0 | 72,63–207,246 | price / tunnel. See below. |
| tint_ | 18 | | 1 | 0,253–156,358 | movies 31/993, 31/506, 31/992 |
| tint_ | 18 | | 2 | 212,172–249,215 | movie 2/32/24 |
| tint_ | 18 | | 3 | 365,99–384,144 | movie 2/32/24 |
| tint_ | 18 | | 4 | 388,91–455,141 | unhandled |
| tint_ | 18 | | 5 | 287,194–376,238 | first click sets flag 20 and the 993/506/992 movies; later 993/994 and exit |
| tint_ | 18 | | 6 | 395,199–436,246 | movie 2/26/24 |
| tint_ | 18 | | 7 | 268,281–391,385 | movie 2/26/24 |

TDOOR hotspot 0: if flag 270 is set, nothing. If flag 63 is set and 271 is clear, sound 394. If Kelsrick is dead and flag 28 is clear, sound 394. Otherwise the first meeting sets 131 and 270 and plays the 475/509–511/476 lines. A later meeting sets 271 and opens TINT.

TINT hotspot 0: if flag 18 is set, clear it, load TINTTRAN, place and heading from `PLACE.TINT`, exit. If the Huline alert is set, movies 31/554, 31/556, 31/557, set flag 19, arm the price timer. If flag 23 is set, movie 31/519. Otherwise nothing.

TINT also has two sprite clicks, not hotspots. Sprite 0, while flag 21 is clear, gives 123-Pois paint. Sprite 1, while flag 22 is clear, gives 93-Skull key. Actor 0 is Mauri. A magic-item offer while flag 19 is clear plays movie 505 and takes the item. The same offer while flag 19 is set clears it and leaves through TINTTRAN.

### Rashar's shop — magic_ index 15, `MAGIC.MIX`

`magic_shop.gd`. Intent: the shop picture. Hotspot clicks are quips. The goods are sprite clicks.

| Id | Rect | Click |
|---|---|---|
| 0 | 150,6–495,151 | quip bit 0x100 |
| 1 | 180,211–250,264 | quip bit 0x200 |
| 2 | 4,6–141,364 | quip bit 0x800 |
| 3 | 507,2–629,242 | quip bit 0x1000 |
| 4 | 376,159–497,254 | quip bit 0x400 |

`region(id)` rejects an id outside 0..4. The quip bits are `QUIP_BITS[id]`. Lines the host may speak are 56, 21, 27, 58, 26, 33, 57, 20. Sprite clicks, separate ids: 0 gives 124-War cluster, 1 gives 131-Mana foil, 5 gives 138-SS5, and 4 then 3 then 2 give 57a-Fire crstl as flags 46, 47, and 48 allow. Actor 0 is the offer.

### LIZ — liz_ index 19, `LIZ.MIX`

`docs/liz-room.md` and `scripts/lol2/liz_room_source.json`. Intent: the wax picture off the village. Entry is VILLAGE hotspot 3 at (425,211)–(576,310), no flag test. VILLAGE hotspot 2 enters CAN when flag 267 is clear (`docs/bacatta-rooms.md` gives that rect as (244,220)–(386,310)).

Setup loads LIZTRAN while flag 268 is clear, then sets 268 either way.

| Id | Rect | Click |
|---|---|---|
| 0 | 91,282–146,339 | while flag 162 is clear: set 162, cue 100:2, give 71-Wax (identity 0xAE5ADACF). A second click does nothing. |
| 1 | 177,151–217,221 | quip bit 0x100 |
| 2 | 290,238–344,316 | quip bit 0x200 |
| 3 | 404,244–472,322 | quip bit 0x400 |
| 4 | 220,198–365,234 | quip bit 0x800 |

The quip host uses speaker 2 and the same eight lines as the magic shop, volume 24. Leave returns to VILLAGE.

### Cave pool — cfall_ index 32, `CFALL.MIX`

`docs/cave-cfall.md` and `cave_cfall_source.json`. Room 32. Intent: the pool picture. Both hotspots do the same thing.

| Id | Rect | Click |
|---|---|---|
| 0 | 334,301–639,399 | heal 5 (nothing when dead), movies (2,55,24) and (2,20,24), set flag 6, every click |
| 1 | 158,350–349,399 | the same |

Setup is callback 1. First update starts ambient 344 and, while flag 5 is clear, sets it and plays movie (2,26,24). Leave is exit. Flags 5 and 6 are used by no other room DLL of the 47 that note scanned. Entry regions 1815, 1817, 1818.

### Chamber of Voices — chv_ index 30, `CHV.MIX`

`docs/l14-chamber-voices.md` and the 2026-11-04 deviation. Intent: the chalice picture that spends the Dreamstone and opens the road to level 16.

Hotspot 0 only, rect (194,88)–(396,218), the golden chalice. Click or E offers the Dreamstone, which may be carried. On offer: consume it, speaker 2 cue 28, the CITY movie, set local 22 `go_to_level_16` = 1, fire prop 170 kind 6. Without the stone the chalice refuses and nothing is lost. The door in front of the picture waits on Belial (actor 90) dead, because the control +0x25 writer is untraced. Wrong-item cues 2:107 and 2:112 are not joined. The refusal is text.

### Herbalist — herb_ index 24, `HERB.MIX`

The 2026-11-01 deviation. Intent: three jars on the first visit. Rects are not in that row.

| Id | Click |
|---|---|
| 0 | flags 200 and 201, gives 109-Ironwod sap |
| 1 | flags 202 and 203, gives 110-Amber |
| 2 | flags 204 and 205, gives 108-Cave aloe |

`l8_herbalist.gd` is the later menu. Its header names the same three hotspot ids. Its definition numbers are 111, 112, and 110. Those are the menu's numbers. The WOM grants are the deviation's 109, 110, and 108. Flag 206 is a later bonus and is not these three clicks. SHAMAN hotspot 1 loads SHBAK. The backroom dialogue is not presented in that note.

### Monastery hall, garden, cellar

`docs/monastery-side-rooms.md`. The hall, the garden, and the cellar are the pictures that note covers. It says the library and office hotspots stay as they were. That note does not pin those two pictures to stem names.

| Place | Id | Click |
|---|---|---|
| Hall (MENT) | 2 | opens MGAR, the garden |
| Hall | 0 | opens MCEL, the cellar, only after flag 134 |
| MCEL | 1 | the passage. The original drops into Jungle pocket region 3191. The port workaround enters Dark Halls entry 1. |

Garden and cellar conversation flags are in that doc (Morgan, Rix, Dawn). Their other hotspot ids and rects were not in the lines read. Library and office hotspot tables were not read.

### Statue bowl — stat_ index 20, `STAT.MIX`

The 2026-11-02 deviation. Intent: the left bowl takes the Emperor's remains and starts the statue. Hotspot 0 rect (145,185)–(275,329). It references 75-Emp remains, takes the held item, and writes `animate_statue`. Other hotspot ids were not in that row.

### Temple door — tmpldor_ index 38, `TMPLDOR.MIX`

The 2026-11-01 deviation. Intent: the Dreamstone at the door. Hotspot 1 checks the held Dreamstone name and reversible flag 272. Hotspot 2 writes named local 13. Rects were not in that row. The row says room presentation is not hosted by that subsystem test.

### Hive rune pictures — runes_ 11, runecl_ 10

`scripts/lol2/hive_rune_rooms_source.json`. The file says these rects are recorded hotspot-call arguments, not a native trace re-derived for this note.

RUNES (`RUNES_.WOM`): id 1 (0,44)–(127,345), id 2 (160,161)–(214,263), id 3 (384,92)–(452,168), id 4 (404,184)–(451,236). What each click does was not in that recipe.

RUNECL (`RUNECL_.WOM`): id 0 (181,130)–(430,274), id 1 (181,275)–(430,388). `hive_rune_transaction.gd` says hotspot 0 admits a held item whose definition name is 71-Wax. Hotspot 1's click was not in that file.

### Bacatta — can_ index 13, `CAN.MIX`

`docs/bacatta-rooms.md`. Intent: the first meeting, the promise, and the relationship. The entry hotspot is the village one above. Inside CAN, the doc records the conversation (lines 625–636, the promise 640–648, the walk-out 0xE09) and says hostile and click branches remain open. A numbered hotspot table for the CAN picture was not in that doc.

### Chief's hut — chut_ index 14, `CHUT.MIX`

`docs/jungle-chut-room.md` says attack branches and stone hotspots remain open. The 2026-10-25 deviation says the same, and names flag 150 stone hotspots as not hosted. `monastery_rooms.gd` draws two stone sprites at (274,169) and (374,169). Those are sprite slots 0 and 1 in that function. They are not a finished hotspot-id table.

### L13 prison — dslave_ index 28, `DSLAVE.MIX`

The 2026-11-02 deviation. Intent: the Dreamstone receptacle frees Dawn and she gives 78-Bestial disk. The row describes the Dreamstone check, the cues, relationship 2, and soul 2. It does not give a hotspot id. Full native hotspot updates are unhosted. No id is invented here.

### Dragon lair — dragon_ index 33, `DRAGON.MIX`

The stem is in the opcode-12 table. A search of the Act 3 `.gd` and `.md` files found no `DRAGON_.WOM` hotspot table. The picture and the hotspot ids are not in the port files read for this pass.

## The other stems

Picture and hotspot table were not read this pass. The stem and the archive are from `room_stems.json` only.

| Index | Stem | Archive |
|---|---|---|
| 0 | pool_ | POOL.MIX |
| 1 | cave_ | CAVE.MIX |
| 2 | skel_ | SKEL.MIX |
| 6 | moff_ | MOFF.MIX |
| 7 | mlib_ | MLIB.MIX |
| 8 | wpn_ | WPN.MIX |
| 9 | sever_ | SEVER.MIX |
| 12 | village_ | VILLAGE.MIX |
| 21 | empt_ | EMPT.MIX |
| 22 | shaman_ | SHAMAN.MIX |
| 23 | shbak_ | SHBAK.MIX |
| 25 | daniel_ | DANIEL.MIX |
| 26 | hut1_ | HUT1.MIX |
| 27 | hut2_ | HUT2.MIX |
| 29 | slaves_ | SLAVES.MIX |
| 31 | balcony_ | BALCONY.MIX |
| 34 | hive1_ | HIVE1.MIX |
| 35 | hive2_ | HIVE2.MIX |
| 36 | hive3_ | HIVE3.MIX |
| 37 | hive4_ | HIVE4.MIX |
| 39 | settle1_ | SETTLE1.MIX |
| 40 | settle2_ | SETTLE2.MIX |
| 41 | settle3_ | SETTLE3.MIX |
| 42 | settle4_ | SETTLE4.MIX |
| 43 | wpnext_ | WPNEXT.MIX |
| 45 | altar_ | ALTAR.MIX |

Village is partly known from the two entry hotspots in the LIZ and Bacatta notes. The rest of that picture's hotspots were not read. Weapon shop `wpn_` and `wpnext_` are named as shops in the Act 1 completion note. Their hotspot ids were not read. Shaman hotspot 1 is the one load of SHBAK above. Altar is a different picture from the statue bowl. The statue note says the bowl is room 20 STAT, not later ALTAR region 5945.
