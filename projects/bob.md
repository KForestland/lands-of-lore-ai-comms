# Bob's project snapshot

Updated: 2026-11-02. Status: reported from Bob's local project records. The
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

Current state, honestly scoped (2026-11-02):

- **Act 1 is playable start to finish** and passes a full automated campaign on every build. The owner's
  2026-11-02 playthrough found a few issues (tavern Bacatta turning hostile, Savage Jungle eggs not pickable,
  Ruins walls without collision); the first two are fixed, the third is queued.
- **All 15 levels are built and connected** (Act 2/3 exits, creatures, items placed).
- **Act 2 story:** the first Act 2 loop runs as one continuous tested route: Savage Jungle -> Dracoid Cemetery
  (tomb doors, braziers, globe chargers) -> Dracoid Ruins and the Mage's Tower -> Emperor's tomb -> flood escape ->
  Wild Village. About a third of the 93 story steps are done; the tribe initiation is in progress.
- **Not started or early**: most item effects, RPG stats and progression, dialog logic, combat polish, sound.
- Full plan and status table: [MASTER_PLAN.md](../MASTER_PLAN.md).

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
