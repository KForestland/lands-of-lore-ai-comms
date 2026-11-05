# P07 LoL1 chunk 8: White Tower and Cimmeria, waiting on a step source

No Godot was run. The tree is `~/lol1_godot` at `9987d7e`, clean. L06 chunk 8 is cards LOL1-12 and LOL1-13. The walkthrough stops in the mine and only names the tower and Cimmeria. The reference's Whole Truth sentence is not a step list. This chunk starts when a second step source is read. No size until then. This file names the sources, the two unmerged endings, and the tests that become valid with that source. It gives no steps.

## Data

The walkthrough is `~/ScotiaEraPrototype/RESEARCH/LoL1_Walkthrough.md`. It stops during Urbish Mine level 3. The reference is `~/lands-of-lore-ai-comms/outlines/GAME1_LOL1_CLASSIC_REFERENCE.md`.

LOL1-12 in the walkthrough names three events and does not order them: mix the elixir, cure King Richard, confront Scotia. Acceptance is not written.

LOL1-12 in the reference puts Jana, Lyle, and a pit to a hidden floor here, and does not put the last fight here.

LOL1-13 in the walkthrough says several levels, Scotia's final form, and the end. Acceptance is not written.

LOL1-13 in the reference says the fight uses the Whole Truth, made from the Ruby of Truth and a Shard of Truth. The walkthrough never names the shard or the Whole Truth.

M04 item 281 is stored as Shard of truth, shape 57, flags 1536. That row is a name and a table record. It is not a Cimmeria step. L05 leaves five titles open, among them Scotia's third form against the Whole Truth and a Castle Cimmeria niche that eats items. They stay open. They are not fixed from the titles.

A second step source is a text that orders player actions. The walkthrough's three names are not that text. The reference sentence is not that text.

## Behaviour

Nothing in this chunk is built from the sentences above. The two endings stay unmerged. No tower flag, no Cimmeria flag, and no Whole Truth item is added. Item 281 stays the table row it already is.

When a second step source is read, the chunk plays that source's ordered steps. A step that appears in only one of the two old sentences, and is absent from the new source, is not implemented. Item 281 is used when the new source names that item.

## Tests

Until that source is read, each test fails closed: the chunk adds no scene.

1. The new source's ordered tower steps are the ones played. The walkthrough's three events and the reference's Jana, Lyle, and pit stay written beside them until the source picks.
2. The new source's ordered Cimmeria steps are the ones played. Item 281 is required only when the source names it. The Whole Truth is required only when the source names it.
3. A test that demands a step the new source does not list fails. No lane-day size is assigned before the source exists.
