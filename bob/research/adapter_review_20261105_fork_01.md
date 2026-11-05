# R2 adapter review fork 01, 2026-11-05

No Godot was run. No opcode callee was entered. The idle line still names ~/opus_work/lol2_r12y at 56812f9. These rows were read in ~/opus_work/lol2_r15 at f6a5aa4.

Each of the eight row files matches r12y byte for byte. The opened hosts match r12y byte for byte: `dark_halls.gd`, `dark_halls_route.gd`, `dark_halls_windows.gd`, `dark_halls_windows_source.json`, `routes.json`, `liz_room_responses.gd`, `cave_crystal_glow.gd`, `cave_stalagmite.gd`, `help_system.gd`, `cave_help.gd`, and `cave_help_source.json`.

## 0024 dark halls

The adapter stays the row.
DECODED: `dark_halls.gd` multiplies unshaded StandardMaterial3D albedo by Color(0.55, 0.47, 0.40).
It paints the background black and enables black exponential fog at density 0.0028.
That pair is the dim brown tint and the black distance fog.
LONGPLAY 75:18-85:38 stays the row's witness for "very dark."
HINTBOOK line 1742 says many areas have a low lighting level.
HINTBOOK lines 2427-2428 name this level the Dark Halls.
BRADY lines 3341-3342, printed page 83, call the halls long bricked passageways.
The hintbook file has no PDF page marker. The books print no tint and no fog density.
The tint is the simpler stand-in. The original depth shade table on this map stays open.

## 0025 dark halls

The 2026-10-22 sentence stays the live gate.
DECODED: `routes.json` lists seven Dark Halls leaves, regions 1394 and 1408-1413.
Each of those leaves has floor 700 and Jungle entry 6.
The same file lists region 1598 with regions 1598 and 1617, floor 760, `workaround_for` 1394, and the same entry 6.
`dark_halls_route.gd` admits a route only after `exits_open()`.
While the window node exists, that flag is the window puzzle done.
The row's broken-wall and sphere-room floor event stays unhosted, so floor 700 reachability stays open.
If window setup fails, `windows` is null and `exits_open()` is true, and the wall route would leave at once.
HINTBOOK lines 2537-2540: drag a crystal box to the bricked window, use a Spark, and jump.
HINTBOOK lines 2548-2550: after the light rumor, blow one hole and jump.
BRADY lines 3484-3487, printed page 86: enough explosives to destroy seven windows breaks a way out and destroys the Spectral Orb, which increases experience.
BRADY lines 3489-3491, printed page 86: one box at the sixth window going left opens an escape into the Huline Jungle.
The books print no region id, no floor 700, and no entry 6.
A sparked crate hole is the printed leave. This host's puzzle gate is the dated row.

## 0026 dark halls

The modern half stays the host.
DECODED: fifteen windows, controls 237-251, each store value 25877.
A Spark hit calls `open_window`. E opens the aimed pane inside 150 with facing above 0.8.
The top-right label is "Windows opened:" and the count over target 7, inside a 1000-unit dome radius.
The seventh opening runs `finish()` at once: soul delta 1, actors 58-75 removed, prop 242 hidden, and window 246 drawn as a painted jungle view.
The exits follow `done()`. An opened window is a bright pane plus a light shaft.
The JSON marks pit floor 740 `hosted` false. `finish()` removes the listed shades together.
LONGPLAY 85:42-89:58 stays the row's witness.
The event6 hit 25877 and the sound 546 wait stay the row's unread gap.
Empty selector 0 on the lit and broken props stays the row. Those selectors are not staged.
HINTBOOK lines 2530-2533: a shown crystal box and a level-three Spark remove the steel door.
HINTBOOK lines 2537-2540: one box at the seven-o'clock window, then a jump. HINTBOOK lines 2541-2543: a rumor that enough light destroys the blue ball and the ghosts.
BRADY lines 2121-2124, printed page 57: explosive crates blast holes through walls, locked doors, and bricked-up windows.
BRADY lines 3484-3487, printed page 86: seven destroyed windows open a way out and destroy the Spectral Orb, adding experience.
BRADY lines 3489-3491, printed page 86: the sixth window and one box let you escape to the Huline Jungle.
The books print no 15, no 237, no 150, no 25877, no 546, no actor 58, no window 246, and no floor 740. The owner line stays continue, modernize. The crate sentences are the more printed action. The shade pull, the pit rise, and the sound wait stay open.

## 0027 village liz

The adapter stays the row.
DECODED: `liz_room_responses.gd` stores eight line ids: 56, 21, 27, 58, 26, 33, 57, and 20.
Hotspots 1 through 4 each set one once-per-entry bit.
A saved per-room LCG picks an unused line and stores the seed.
`monastery_rooms.gd` plays the chosen line as a LIZ quip.
Address f133c was not entered.
The native global RNG stream stays the row's gap.
The books print no such line list and no LCG constant.
A fixed line per hotspot would be simpler.
This saved history is the hosted substitute.
The unread native stream stays open.

## 0028 cave

The adapter stays the row.
DECODED: `cave_stalagmite.gd` draws descriptor 122 and then 123 on the ordinary shard.
`cave_crystal_glow.gd` binds 124.png and 125.png.
It checks the 256 by 128 upper blend table and packs the glow through a shared depth viewport.
The glow path uses unshaded indices.
The native shade-row choice stays unimplemented.
The row's +2 to 6 ms per frame on the RX 9070 XT stays the Grok bench witness.
No bench was rerun.
BRADY lines 2268-2271, printed page 61: break a piece of green crystal from a stalagmite and use it as a crude weapon.
HINTBOOK lines 2063-2064: whack stalagmites in a stream-room niche and a flood scene plays.
Those sentences print no descriptor index and no frame time.
The books print no such number.
The extra depth view is the hosted glow.
A flat shard would be simpler and would drop the blend.
Shade-row choice and the frame cost stay open.

## 0029 all

The art half stays the row.
DECODED: `prepare_help_system.py` states that help.pcx is absent from the GOG data.
It also states that the red-eye icon is absent from shipped shapes.
The page texture is PRCHUNRL.PCX.
The icon is intrface.shp shape 119.
`help_system.gd` places the text on anchors 0.22 to 0.78 and 0.21 to 0.70, the scroll centre.
Layout 15BB18 was not entered.
`page_text` writes the placeholder [key] wherever the original page has @.
The port's real keys sit in the "In this version" note.
That live text is row 0031.
Row 0029's sentence that @ becomes this version's keys is ahead of `page_text`.
The books print no shape 119 and no layout address.
The parchment is the stand-in while help.pcx is missing.
The undecoded layout stays open.

## 0030 cave

The adapter stays the row.
DECODED: T on the open help page flips `state.enabled`.
`cave_walkthrough.gd` writes and restores that state as `help` on the Cave save.
`cave_help.gd` is the only `request()` caller found under `scripts`.
Topics 1, 2, 3, 6, 7, and 8 have Cave hooks.
The source names prop 422, topic 4, as a timer whose starter is untraced.
That starter stays the row's gap.
There is still no options menu.
The books print no T switch and no prop 422.
The books print no such number.
The untraced combat timer stays open.

## 0031 all

The adapter stays the row.
DECODED: `page_text` keeps the original helptext.trr wording and shows each @ as [key].
`open_page` appends the "In this version" note for that topic.
Left and Right wrap all eight topics.
F1 opens the banner topic while a banner is up, and otherwise the latest announced topic.
The page footer names F1, the arrows, and T.
HINTBOOK line 1735 says the automap key cannot be reassigned.
That sentence prints no help-page browser.
This Brady search has no F1 help-page hit.
The books print no eight-topic count and no placeholder key.
The version note is the simpler reading aid beside the original wording.
Placement of those original keys stays with the unread layout from row 0029.

## Receipts

- 0024 dark halls: Dark Halls lighting stays a brown albedo tint and black distance fog, the depth shade table stays open, the longplay window stays the darkness witness, and the books print no tint and no fog density.
- 0025 dark halls: Jungle entry 6 stays shut until the window puzzle is done, including the floor 760 wall route, floor 700 reachability stays unhosted, and the books print no region ids, with their crate-hole sentences left separate.
- 0026 dark halls: Fifteen dome windows open on Spark or E inside 150, the seventh ends the orb at once with soul plus 1, the books' crate sentences stay separate, and sound 546, the shade pull, and pit floor 740 stay open.
- 0027 village liz: LIZ hotspots stay on eight saved lines and four once-per-entry bits with a per-room LCG, the native global RNG stream stays unread, and the books print no such line list.
- 0028 cave: Cave crystal descriptors 122 through 125 stay on the shared-depth blend with shade rows unshaded, the row's frame-cost range stays open, and the books print no descriptor index and no millisecond cost.
- 0029 all: Help page art stays the parchment scroll and interface shape 119 with the text in the scroll centre, layout 15BB18 stays unread, and the books print no such art ids.
- 0030 cave: Help messages toggle with T on the help page, the seen bits stay in the Cave save, prop 422 combat help stays unhosted, and the books print no such switch.
- 0031 all: Help pages keep the original wording plus a version note, Left and Right browse eight topics, F1 reopens the latest topic, and the books print no eight-topic browser.
