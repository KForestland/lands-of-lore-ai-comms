# Lands of Lore — Master Plan

Owner: Kjetil (KForestland). Updated: 2026-11-05.
Fan project, non-commercial. Lands of Lore is © Westwood Studios / Electronic Arts. No original game files are
distributed: the remakes read the data from the player's own copy of the games.

## Vision

Give the Lands of Lore series back to the players who loved it, and introduce it to new ones. This is a long-term
effort ("if it takes 10 years, we will do it").

1. **Classic editions** of Lands of Lore 1, 2 and 3: the original games, faithfully remade in the Godot engine.
   They keep the original look, story and behaviour, fix every original bug, and log every deviation in a public
   ledger.
2. **Enhanced editions** after that: optional modern lighting, quality-of-life features, wider outdoor maps, and
   compatibility between LoL 1–3. They add story threads from the unified *Chronicles of Time* outline and ruins from
   the age of the Ancients.
3. **New stories later**: the LoL 4–6 and Chronicles outlines in [outlines/](outlines/README.md) are design
   context for the future, not current work.

## Order of work

| Step | Game | State |
|---|---|---|
| 1 | LoL1 reverse engineering | **Done and published** ([lands-of-lore-1-re](https://github.com/KForestland/lands-of-lore-1-re)) |
| 2 | LoL2 reverse engineering | Largely done, published ([lands-of-lore-2-re](https://github.com/KForestland/lands-of-lore-2-re)) |
| 3 | **LoL2 Classic in Godot** | **In progress, main project** (details below) |
| 4 | LoL3 Classic | After LoL2 is finished |
| 5 | LoL1 Enhanced, then the other Enhanced editions | After LoL2 and LoL3 are finished |
| 6 | 3D characters/items/creatures for the Enhanced editions | Not before 1–2 years from now; LoL1 assets first |

## LoL2 Classic: phases and status (2026-11-05)

Phase order (owner, 2026-11-05): **maps to 100% → quest chains complete (from the guides) → Act 3 story → items → RPG →
dialog → small fixes**. Sound and combat polish come last. Quality comes before speed; estimates are for orientation.

| Area | Done | Notes |
|---|---|---|
| Maps / world | ~90% | All 15 levels built and connected. Open: Huline Temple portal doors and overlapping rooms, texture/clipping reports. Atlas v2 (floor slices, explored-only) planned |
| Act 1 | ~90% | Playable start to finish; owner confirmed the Bacatta escort, the Confidante route and the cat-lady knife (r14). Next build adds the dragon picture click, Hive flute lift, lever/talk prompts |
| Act 2 story | ~70% | Story steps 7–65 built and tested in earned runs; owner playtest found quest-chain gaps (village admission → Dracoid quest → serum → Larkhon) being fixed |
| Act 3 story | ~10% | 3 of 28 steps built (Chamber of Voices → city rises, Ancient City arrival elevator, north-east greenhouse fireball) |
| Items | ~25% | All 170 original items placed and carriable; effects hosted one by one |
| Creatures / combat / spells / RPG | ~10% | Act 1 combat works; creature/spell tables collected |
| NPCs / dialog | ~20% | Act 1 conversations, first Act 2 encounters; speech volume fixed after owner report |
| Sound / music | ~20% | Act 1 mostly |
| Polish / Enhanced | ~5% | Plan approved (below) |

Overall LoL2 Classic: **about 55–60%**.

Rough timeline (orientation only; depends on AI usage limits and playtests):
- Classic maps at 100%: 1–2 weeks.
- Classic playable A to Z (every story step, start to end): mid-December 2026.
- Classic with all systems (items, creatures, spells, RPG, dialog, sound): February–March 2027.
- Gray-box version (same quest chain, box geometry and box characters): early 2027, right after the A-to-Z chain.
- Enhanced art pass: aiming for summer 2027.

### New workflow for Enhanced (approved 2026-11-05)

One story, one save, one quest logic for every edition. Tools ("pipes") run on all levels at once:
1. Gray-box generator: decoded level geometry → simple box levels.
2. Box people: every quest character/creature/prop as a labelled box with the same id.
3. Quest walk: the existing automated walk tests run on the gray box too, proving the chain end to end.
4. Art import: AI-generated 3D models replace gray boxes by id with one import rule.
5. Owner playtests stay the final check.
Then refine → test → refine, level by level: textures, tessellation, lighting, and sightlines that show places and
hidden areas so the hint system can be lighter. Rules and tools evolve by iteration on what works.

## How the work is done

- The owner makes the design calls and playtests every build; he does not write code.
- Several AI "lanes" share the work through this repository and a local coordination board:
  - Claude Opus is the lead and integrator.
  - Astra (OpenAI) builds the story progression (away until ~2026-11-09; the lead builds Act 3 meanwhile).
  - Grok researches the original game and the strategy guides.
  - Claude Fable is a second builder.
  - Kimi runs small verification tasks on a timer.
- **Evidence order:** the original game's own data and scripts, then the printed guides (Prima, Brady), then the
  owner's longplay video, then the owner's memory. When a detail is hard to trace, a logged adapter that matches the
  original's visible behaviour is allowed, and every such deviation is recorded in the ledger.
- **Quality gates:** every build passes a regression suite, a scripted Act 1 campaign, an export/package check and a
  packaged smoke test before it reaches the owner's playtest launcher.

## Collaboration

We are happy to exchange findings with other Lands of Lore researchers and fan projects. See
[COLLABORATION.md](COLLABORATION.md) for what we can offer and the open questions where help is welcome.

## Credits (so far)

- Westwood Studios: the original games; Frank Klepacki: the original music.
- Amy Schmidt (landsoflore.de): the tested Rix rescue fix, used as the source for that bug fix.
- Onkel Dave: "Schon gewusst? – Lands of Lore II" fan guide, used as a reference witness.
- smgtoxa (LoL1 project) and MohammadKoush (Lore Tweaks): collaborators in this workspace.
