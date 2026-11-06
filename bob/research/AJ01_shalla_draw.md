# AJ01 Shalla drawn

Base is stack-ah01 a04c73a. Patch `grok_research/patches/AJ01_shalla_draw.diff` is unapplied.

hive_review passes assembly 75 to `static_assemblies.setup` as its own mesh. hive_shalla.gd names that mesh Shalla. The one initial face leaves the shared L5 colour batch, so she is drawn once at native (-1133, 8885), height -235. Godot position (-1133, -235, -8885). Groups 5808, 5872, 5892, 5912, and 5932 stay unrun. No collision body, no quest key, and no save field. Actor 20 stays Dawn.

Test `hive_shalla_draw_test` prints `PASS: Shalla assembly 75 is drawn at (-1133, -235, -8885) with no collision`. Registry order 866.

Hive wax and lift walks stay unchanged. The tests that prove them are `hive_lift_wax_walk_test`, `hive_curse_wax_walk_test`, `hive_boulder_contact_earned_walk_test`, and `hive_wax_test`.
