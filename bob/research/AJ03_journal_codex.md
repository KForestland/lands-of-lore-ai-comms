# AJ03 Codex tabs

Patch `grok_research/patches/AJ03_journal_codex.diff` stacks on AJ02. Unapplied.

My Journal keeps Notes as the page J opens. Items, Creatures, Characters, and Lore come from `data/lol2/codex.json`. An item line shows when the carried list or the spent list has that catalog id, or when `item_effects.codex` lists it. A creature, character, or lore line shows after `discover()`. The optional key is version 1. An old save without the key still loads. Item lines use the stored "I have held" text. Other lines say "I have met" or "I have heard of".

Test `journal_codex_test` prints `PASS: My Journal codex tabs show held items and discovered creatures, characters, and lore`. Registry order 870.
