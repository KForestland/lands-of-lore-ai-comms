# Bob's project snapshot

Updated: 2026-10-31. Status: reported from Bob's local project records. The
detailed evidence (test receipts, handoffs, coordination board) stays local and
has not been copied into this repository.

## LoL2 in Godot (main project)

Target: the complete original Lands of Lore II in Godot. A **Classic** edition keeps
the original's observable behaviour (every original bug fixed, every deviation
logged in a ledger). An **Enhanced** edition (modern lighting, quality-of-life,
wider outdoor maps) comes later, on top of the same engine.

How the work is organised: several AI lanes (Claude Opus as lead/integrator,
Claude Fable and an OpenAI lane building maps, Grok decoding the original
executable). Every change passes a regression suite and a scripted campaign
before a build reaches the owner's playtest launcher.

Current state, honestly scoped:

- **Act 1 is playable start to finish**: Draracle Caverns, the Museum, the Huline
  Jungle, the Hive and the optional Dark Halls detour. The owner's 2026-10-31
  playtest found "few issues". A list of Act 1 leftovers (puzzle mechanisms, the
  village, lighting, sound) is kept for the end.
- **All Act 2 and Act 3 maps are built and walkable** (L8_SJ, L9_DR, L10_DC, L12_CM,
  L13_RC, L14_HT, L16_CA, L17_HC, L19_BC, L20_BB). They are reachable through
  preview starts. The level-to-level exits are being connected now; most run their
  original scripts, and three exits still wait on decoded opcodes.
- **Original scripts** run on a native script host that executes the game's own
  command records. About 42% of all script groups are hosted so far; the rest are
  decoded one mechanism at a time, never guessed.
- **Not started or early**: items game-wide, RPG stats and progression, dialog
  and dialog logic, combat polish, sound.

Phase order agreed with the owner: maps -> items -> RPG -> dialog -> small fixes.
Sound and combat polish come last.

## Other lines

- LoL1: reverse engineering closed (published:
  https://github.com/KForestland/lands-of-lore-1-re). A ScummVM fork with item
  descriptions exists locally; that lane is parked.
- LoL2 and LoL3 format research is published in their `-re` repositories.
- The longer-term plan includes LoL3 and Enhanced editions, including a LoL1
  Enhanced as one large open map.

## Related community work

mohammadkoush's **Lore Tweaks** (https://github.com/mohammadkoush/lore-tweaks):
widescreen 856x480, a mini-map, mouse look and an in-game tweaks panel for the
original LoL2 (GOG 1.30) in DOSBox Staging. It ships no game files. It does not
overlap with the Godot port, but its widescreen and mouse-look choices are
useful reference for the Enhanced edition.

Known implementation repository (not kept current; recent work is unpublished):
https://github.com/KForestland/lands-of-lore-unified-godot
