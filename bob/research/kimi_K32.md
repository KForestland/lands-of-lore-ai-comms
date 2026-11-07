# Kimi K32 — meta-duck groundwork: the LoL2 ending (ACT3-PLAYABLE-ENDING), 2026-11-07

Lead: accepted as the BF01 brief. Plan: keep the one-blow start; add the scripted chasm/vow/slump beat (adapter, persists over save); decode MOVIES.MIX e224e.vqa (else a logged adapter showing the book's two beats); file 'game finished' + end screen; earned walk proves it. Note the book's own warning that the shipped ending looks truncated (5551-5568).

All sources gathered. Here is the groundwork report.

  # K32 — Groundwork: making the LoL2 ENDING playable (ACT3-PLAYABLE-ENDING)

  Backlog item: `ACT3-PLAYABLE-ENDING`, area L20_BB, priority 1, status `todo` — "Final fight resolves (chasm, slump) and the ending movie/sequence plays; game finishes" (`BACKLOG/backlog.json:11030`). Method: the meta duck (`META_DUCK_METHOD_20261107.md`). Branch `act3-chain` confirmed in `~/opus_work/lol2_act3`.

  ## 1. The game's INTENT for the ending

  The ending is a **reveal** + **reward** beat, deliberately not a real boss fight: after the long chase through Belial's lair, the player lands one blow with any of the three legendary weapons and the game takes over — Belial is separated from Luther by a chasm, vows never to return, and slumps, and a final video closes the story (Luther with Dawn; the Draracle drops in, announces he is leaving, and vanishes — the last of the Ancients gone, Luther left standing). The hintbook itself flags that the shipped scene feels truncated — "There has to be a bug here!" (hintbook.txt:5551-5554, 5567-5568) — so the *intent* is a cinematic resolution, and the book's wording warns us the original may show less than designed. In duck terms: the fight is a *gate* on story, not on skill; one hit is the whole mechanic.

  ## 2. PLAYER CONTRACT, in order

  Trigger → what the player sees/hears/does, with evidence:

  1. **Approach** — after the faux-Draracle dies, the player forces a door, saves, runs down a hall, attacks a second door; "Belial begins to speak" (hintbook.txt:5543-5546). The final-room trigger record exists natively: Control 61 "Trigger" at (-3493, 3843), region 763; locals `Final_Belial_Trigger`, `Evil_Belial_talking`, `Good_Belial_Talking` not yet bound (`act3_tail_ids.md:18`).
  2. **Fight starts on one blow** — Belial summons a gold point of light by his head (hintbook.txt:5555-5556). The player hits him once with the **blue bow, the Dark Sword, or Belial's horn — all have the same effect** (hintbook.txt:5557-5558). Belial casts spells (pink Ruloi pillars) and can be chased around the room meanwhile (hintbook.txt:5559-5561). Last longplay frames: `g_00389` at 303:40 — "the horned figure in fire"; `g_00390` at 304:10 — "a dark figure over a patterned floor" (`I33_act3_frames.md:35`).
  3. **The resolution cut** — "a jump in the graphics, and all of a sudden Belial is on the other side of a chasm from Luther. He speechifies… vowing never to return, before he slumps over" (hintbook.txt:5563-5565). No frame shows the chasm or the slump (`I33_act3_frames.md:35`: "no chasm and no slump").
  4. **The final video** — "Luther with that vixen mystic, Dawn, when the Draracle drops in to say he's leaving. And leave he does, vanishing in an instant" (hintbook.txt:5574-5576). Not on any longplay frame: "the last frames are the fire" (`I33_act3_frames.md:36`). The video is a movie, not an in-world scene — natively there is no Dawn actor on L20 (`act3_tail_ids.md:19`).
  5. **Game over** — "that's the game" (hintbook.txt:5583). Nothing is filed after the last scene natively (X05 notes: `X05_finale/NOTES.md:3`).

  What can go wrong: the book suspects the original ending is buggy/truncated (hintbook.txt:5567-5568), so our target is the *book-described* sequence above, at least as much as the longplay shows (fire frame → dark figure frame → movie).

  ## 3. EXACT vs APPROXIMATE

  **EXACT (mechanics — changes go to the owner):**
  - The three named weapons (blue bow, Dark Sword, Belial's horn) all start the same flag; other items do not (book 5557-5558; native: actor 75 is the only def-byte-2 BELIAL placement, `act3_tail_ids.md:18`; already encoded as `WEAPONS` in `l20_finale.gd:10`).
  - One blow ends the fight — no real combat phase to win.
  - The chasm separation and the slump happen as a scripted beat, then the ending movie plays, then the game is finished (and stays finished over save/reload).

  **APPROXIMATE (presentation — adapter allowed, logged in DEVIATIONS):**
  - How the chasm appears (the book itself calls it "a jump in the graphics" — likely a cut/movie), the vow speech rendering, the slump animation, exact spell effects during the one-blow phase, and the movie playback mechanism itself.

  ## 4. What `l20_finale.gd` records vs shows today

  File: `~/opus_work/lol2_act3/scripts/lol2/l20_finale.gd` (113 lines), header at lines 2-6.

  Records (quest state `l20_finale`, schema at lines 21-22):
  - E near actor 75 (within 20 units of `AT_75`, line 93) with one of the three weapons equipped sets `started=true` and stores the weapon id (lines 96-102) — matches the book's "same effect" rule.
  - E near actor 46 (`AT_46`, line 105) after `started` sets `draracle_seen=true` (lines 106-112).
  - Everything else is **forced to the negative**: `chasm=-1` (lines 100, 111), `slumped=false` (line 101), `appeared/vanished/dawn_here=false` (lines 108-110); `validate()` actively *rejects* any state with a slump, appear, vanish, Dawn, or a chasm ≠ -1 (lines 42-44). Constants `VOW=""`, `SCENE_NAME=""`, `DAWN_ON_L20=false` (lines 12-14); `plays_movie()`, `after_movie()`, `moves_player()` all return `false` (lines 27-34).

  Shows: only two hint labels — "E — the blue bow, the Dark Sword, and the horn start the same flag." (line 86) and "E — actor 46. No movie plays. Dawn stays off L20." (line 88). No Belial, no chasm, no slump, no Dawn, no Draracle, no movie, no end-of-game. Tests exist: `tests/l20_finale_test.gd`, `tests/l20_finale_earned_test.gd` (fixture `res://tmp/l20_finale_earned_save.json`, X05 `NOTES.md:5`).

  ## 5. Native records / movie files involved, and presence in the project

  | Item | Evidence | In project? |
  |---|---|---|
  | Actor 75, BELIAL (def byte 2), (-1238, 3207), region 177 | `act3_tail_ids.md:18` | Recorded in `l20_finale.gd:8,15`; no actor placed |
  | Actor 46, DRARACLE, (-6921, 4828), region 1272, event list 4668 | `act3_tail_ids.md:17,19` | Recorded in `l20_finale.gd:9,16`; no actor placed |
  | Control 61 "Trigger" (-3493, 3843), region 763; locals `Final_Belial_Trigger`, `Evil/Good_Belial_talking` | `act3_tail_ids.md:18` | Not bound |
  | Opcode-21 movie table, 85 names from LOLG.DAT | `scripts/lol2/movie_table.json` | Present; **neither `placenta` nor `e224e` is in it** (`bb_brth` is index 65, `beli` index 1 — not joined to the finale by research) |
  | "Belial's birth" scene (STORY-087, book line 5487) → `placenta.vqa`, name-matched to prop 242 "Frank's Placenta", stored on L20 at file offset 5066703 | `act3_tail_ids.md:13`, `I23_finale_movies.md:17,19` | **No** — no `.vqa` files exist in the project at all; no generated `.ogv`; `l19_dawn_curse.gd:23-25` records it as `IN_MOVIE_TABLE := false` |
  | Final video (STORY-093, book 5574-5576) → candidate `e224e.vqa`, stored on L19 at 58149 with `Dawn good Luthe` in the following bytes | `act3_tail_ids.md:12,19`, `I23_finale_movies.md:13,19` | **No** — same; adjacency "not read as a reel"; MOVIES.MIX key UNKNOWN |
  | MOVIES.MIX (28 VQA entries, keys unjoined to names) | `I23_finale_movies.md:23-58` | Archive itself not in the project |
  | Playback idiom | `scripts/lol2/l13_belial_movie.gd` (CanvasLayer + VideoStreamPlayer + generated `movie.json`→`.ogv`); opcode-21 staging in `native_script_host.gd:1845-1858` | Present and proven on other movies |

  ## 6. Smallest faithful plan so the game visibly finishes

  Duck step 6, cheapest faithful first — option **b/c** (decode what carries the EXACT items; adapter for the rest):

  1. **Keep the fight-start mechanic as-is** — it already matches the book exactly (three weapons, one flag, E at actor 75). No change.
  2. **Add the resolution beat on `started`** (approximate, logged in DEVIATIONS): freeze input, cut to Belial across a chasm (a placed prop/decal chasm + Belial figure is enough — the book itself describes a graphics jump), show his "never to return" vow as caption text, then the slump (figure falls or disappears). Set the real flags: `chasm`, `slumped`, and relax `validate()` (`l20_finale.gd:42-44`) to accept them. This is the one EXACT state change: the beat must fire on the first blow and persist over save/reload.
  3. **Play the ending movie after the beat**: preferred — decode the MOVIES.MIX key for `e224e.vqa` (and `placenta.vqa` for the birth), extract to `.ogv` under `assets/lol2/generated/`, play through the proven `l13_belial_movie.gd` pattern with a `movie_players.json` row. Until that decode lands, a logged adapter may show the two book beats (Luther with Dawn; Draracle appears, says he's leaving, vanishes) so the game *visibly finishes* — flagged as adapter, never as decoded.
  4. **File "game finished"** after the movie: an end state in `quest_state` plus an end screen/credits stub; nothing else follows the last scene natively (X05 `NOTES.md:3`), so no further chain work is blocked.
  5. **Prove like a player**: extend `l20_finale_earned_test.gd` so the earned walk (from `l20_faux_draracle_earned_save.json`) does exactly steps 1-4, plus captures compared against longplay frames `g_00389`/`g_00390` — then owner playtest, per the backlog acceptance line.

  No files were modified; this is groundwork only.

