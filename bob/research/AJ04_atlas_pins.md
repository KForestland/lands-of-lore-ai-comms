# AJ04 Atlas pins

Patch `grok_research/patches/AJ04_atlas_pins.diff` stacks on AJ03. Unapplied. Apply AJ01, AJ02, AJ03, then AJ04.

Pin here on the Atlas writes a note, an area, and a position into the optional `item_effects.pins` list. My Journal lists that pin on the Pins tab. The Atlas draws a small square on the matching area. Opening the Atlas still leaves the game running. No quest arrow. An old save without the list has no pins. `atlas_explored` is unchanged.

Test `journal_pins_test` prints `PASS: Atlas Pin here stores a note, area, and position in My Journal and on the Atlas`. Registry order 872.
