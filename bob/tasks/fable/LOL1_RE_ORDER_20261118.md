# LoL1 reverse-engineering: last unknowns (lead order, 2026-11-18)

Owner decision, 18 Nov 2026: the scope is now **documentation and understanding of LoL1, then LoL2, then LoL3**. No rebuild work. Order: LoL1 last unknowns -> LoL1 GitHub cleanup -> LoL2 -> LoL3.

This is research and documentation only: how the original files and rules work. Nothing here builds or changes a game.

## Rules for every lane

- Every claim cites its evidence: a file and byte offset in the game data, or a ScummVM source file and line. Mark each claim CONFIRMED (checked on the data) or UNCONFIRMED.
- Check both editions where they can differ (reference corpus = CD; LANDSoL = second edition; say which one you read).
- Work in your own git worktree of the public repo, on your own branch. **No push, no GitHub.** The lead reviews, the owner approves publication.
  `git -C ~/lands-of-lore-1-re worktree add ~/lol1_re_<lane> -b <lane>/lol1-unknowns-20261118`
- No extracted game assets and no raw game files in the repo (see the README asset policy). Tables of numbers, format descriptions and tools are fine.
- One long order: do not stop between items. If an item is blocked, write one line why and take the next.
- Post STARTED / READY / BLOCKED lines on the board (COORDINATION.txt) and keep AI_COMMS/status/<lane>.md current.
- Keep it light: no Godot, no long sweeps. Python and reading only.

## Sources

- Game data (CD): `<owner-media>`
- ScummVM reference: `~/scummvm-lol1-fork/engines/kyra/` (and `devtools/create_kyradat` for tables taken from the executable)
- Decompiled level scripts (archived): `<owner-media>` (read in place; string listings in the .asm are garbled, read strings from the INI TEXT chunk)
- Public repo: `~/lands-of-lore-1-re` (docs/closure_memo.md is the current state)
- Godot port notes with facts found in September: `~/lol1_godot` (tools/import_lol1.py, tools/extract_syscalls.py)

## GROK: six small unknowns (items 1-6)

Output: one file per item in `docs/unknowns/` of your worktree, plus a READY line per item.

1. **SHP header per edition.** The memo says 12 bytes with a 2-byte prefix. The Godot port found that CD shapes have no prefix (ScummVM LOL_CD_FLAGS, useAltShapeHeader=false). Settle it for CD and for floppy/LANDSoL with byte dumps of three shapes each.
2. **WLL header bytes 0-3** ("unknown" in docs/level_tileset_map.md). What are they, and who reads them.
3. **Level 24 CMZ: 9 bytes per block** where every other level has 4. What are the extra 5 bytes, and why only this level.
4. **YVEL2.VCN/VMP.** Which code or script loads it, and when (the docs guess "Level 22 sub-area").
5. **ADV, DRV, TBL files.** What each is, which program reads it, and what the format is as far as it is data and not driver code.
6. **TIM opcode table.** A complete table: opcode number, name, parameters, what it does, how many of the 139 scripts use it. Source: ScummVM script_tim.cpp plus data/tim_analysis.json.

## SOL: scripts and game rules (items 7-8)

Output: docs and tools in your worktree; a READY line per item.

7. **EMC2 level scripts.**
   a. A decompiler tool in `tools/` that reads INF/INI and writes a readable listing with correct strings (from the TEXT chunk) and named functions.
   b. `docs/emc2_scripts.md`: container layout (ORDR, TEXT, DATA), the full opcode table, and the full LoL1 function table (number, name, parameters, effect) for the CD edition, with floppy differences.
   c. A test that decompiles all 60 scripts without an unknown opcode or function.
8. **Game rules and tables from the executable.**
   a. Where each table sits in the executable (offset, record layout): items (285 types), item properties, monsters, spells, character definitions, experience levels.
   b. `docs/game_rules.md`: combat (hit chance, damage, armour), magic (cost, effect per level), experience and skills, monster behaviour modes, light, and time, as formulas in plain words with the source line beside each.
   c. `docs/savegame_format.md`: the save file, field by field.
   Do 7 first, then 8a, 8c, 8b.

## OPUS: structure, missing tools, review (item 9)

Output: your worktree; a READY line per item.

9. a. Split docs/closure_memo.md into one page per format under `docs/formats/` (what it is, layout table, how it was confirmed, the tool that reads it). Keep the memo as history; correct nothing by guessing, mark open points and link to Grok's item.
   b. Add the missing tools so each documented format has a reader in `tools/`: CPS, VOC, FNT, XXX (automap legend), DAT (decorations), TLC, VCN/VMP if level_renderer.py does not cover them alone. Each with `--help` and a one-line check against the CD data.
   c. A status table `docs/STATUS.md`: per format and per rules topic: documented / tool / confirmed on data / open. This replaces the "99.999%" claim with facts.
   d. Review Grok's and Sol's READY items as they arrive (fresh read against the data); post PASS or the defect on the board.
   e. Draft the README cleanup (duplicate "Then read" list, status claims that match STATUS.md). Draft only; publication waits for the owner.

## After this order

GitHub cleanup of the LoL1 repo (owner approves the push), then the same pass for LoL2 (first job: collect what the rebuild lanes decoded into the RE docs), then LoL3.

[fable/lead]

## Added 13:45Z: the public repo must shine (owner)

Owner: "want the github to shine and be understandable, perhaps tools". He has given the lead standing access to push the LoL1/2/3 repos after lead review. Quality bar for everything that goes public:

- **Front page (README):** what the game is, what this repo gives you, one picture of a tool result (our own render of a level map or a format diagram, no game art dumps), a 5-minute quick start that works on a fresh clone with the user's own game files, and the status table.
- **Tools are welcome and are part of the result.** Every tool: runs from a fresh clone, takes the game folder as an argument (no ~ paths), has --help that changes nothing, never writes outside the output folder it is given, and has one example command with its expected output in tools/README.md.
- **One page per format**, readable alone, with a small layout diagram or table and a worked example (bytes -> meaning).
- **A "how the game works" set** (scripts, rules, save format) written for a reader who has only the game.
- **A glossary** (PAK, CMZ, EMC2, TIM, block, wall type...) and a "start here by goal" list (I want to read maps / decode text / understand scripts / mod a save).
- No game assets, no raw game files, public name Kevin, plain English.

OPUS owns this bar for LoL1 (it extends items 9a-9e); Sol and Grok write their pages to it.

## Round 2 (lead, 13:58Z): open questions and the release branch

Round 1 is complete and reviewed (Sol 7/8a/8b/8c PASS, Grok 1-6 PASS). The open list is `docs/OPEN_QUESTIONS.md` on branch opus/lol1-unknowns-20261118 (worktree ~/lol1_re_opus), Q1-Q18. Same rules as round 1. A question that cannot be closed gets a page saying what was measured, what was tried, and what would settle it; that counts as done.

**GROK (file and script questions):** Q3 (Level 24 extra 5 bytes per block: find the reader in the executables and the level 24 scripts; note Opus's hint about wall types 46, 53-57), Q11, Q9, Q10, Q12, Q13, Q14, Q16, then Q1 for the demo only if a demo copy is on the Arikv drive (do not download one). One page per question in docs/unknowns/.

**SOL (executable questions):** Q17 (native save fields ScummVM skips, from the save and load routines in both executables), Q18 (native in-memory item and monster records), Q7 remainder (magic effects, light, time, regeneration, monster mode transitions and the WLL flag bits and special types, each checked in the executables), Q8 (what the 0x7E routine changes), Q15 (ADL layout field by field; what C55 is). Also fix the review defects: cite upstream ScummVM line numbers (see Opus 13:42Z), emc2_scripts.md:283.

**OPUS (release branch):** create branch `release/lol1-20261118` in your worktree from your branch; merge sol/lol1-unknowns-20261118 and grok/lol1-unknowns-20261118; one consistent tree (docs/unknowns linked from the format pages, no "being added" wording left, no lane names, no machine paths). Then the quality bar in full: final README.md, glossary, start-here-by-goal, a worked example on every format page, tools/README.md with one example and expected output per tool. Proof: a fresh `git clone` of the branch into a temp folder, `python3 tools/check_all.py --data <CD DATA>` passes, and a second stranger read. Check the asset policy (no game files; quoted game text only as short examples). Post READY for lead review; the lead reviews and pushes. After that, keep reviewing round 2 READY lines and fold PASSED answers into the release branch.
