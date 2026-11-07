# BG01 — render the BF ledger rows

Base `c9295da`, after BF01–BF07, then BG00a and BG00. Patch `patches/ACT3P2/BG01_deviations_render.patch`. Not applied to the live tree.

BF01–BF07 add fourteen `0317-row-2026-11-07-d00` through `d13` pieces and do not render `docs/DEVIATIONS.md`. `tools/build_deviations.py build` inserts those rows. `--check` then matches 397 pieces. The older rows-versus-pieces count inside `deviations_ledger_test` is unchanged.

Printed:

`PASS deviations: docs/DEVIATIONS.md matches docs/deviations/ (397 pieces)`
