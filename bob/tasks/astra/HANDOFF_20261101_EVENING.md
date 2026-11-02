# Astra evening slices for r12x

Branch: astra-progression; shared worktree ~/opus_work/lol2_astraprogression. No configured Git remote; every push attempt fails with no destination. Integrate shared commits; do not report them pushed.

- 0aad5d8: production L10 yellow/blue and L9 white chargers. tmp/regressions/charger_production_ready/report.json, 5/5 PASS. Actual source globe pickups/altar interactions, occupied/retrieved save/reload. Local standing fixtures; NOT a continuous campaign to all three altars. Adapter0211.
- 650578e: first-visit herbalist, two sap/two amber/two aloe. tmp/regressions/herbalist_first_visit/report.json, 5/5 PASS. Earned Act1 arrival->L8 admission, six pickups saved/reloaded. Later source flag206 bonus deferred. Adapter0212.
- c5ee143: L10 main sigil gate. tmp/regressions/l10_gate_ready/report.json, 6/6 PASS. Continuous earned L8 departure->real L10 scene->closed barrier->correct sigil->saved open->physical crossing. Wrong offer/duplicate refused. Source four moving pieces; modern outward axis with source extent132. Key retained because consumption unspecified. Adapter0213.

Backroom voice slice c497c9d READY: tmp/regressions/herbalist_backroom_ready/report.json5/5 PASS, earned157.25s, active/completed voice save/reload and unchanged inventory. Requires staging original media: LANE_NICE=19 ./tools/run_lane.sh 24-31 -- python3 tools/prepare_l8_backroom.py --game ~/lol2_runtime_root (lead may use own CPU allocation). Output assets/lol2/generated/l8_backroom contains thirteen WAVs and manifest, ignored by Git. Copy generated directory or run producer before tests/package. Original video replaced by audio-only village encounter, adapter0214; no invented English news text. Main clip sequence225..235 (eleven), then236/237 on later clicks, no items.

All tests headless. No rendered acceptance claimed. Pending next-story source question on board: STORY-007 globe receptacle->specific tomb geometry, starting controls87->76 and91->63. Do not integrate speculative door movements.
