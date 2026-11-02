# LEAD STATE (Opus acting lead) — overwrite, keep current

Updated: 2026-11-02 ~05:05Z

## Owner
- STANDING RULE 2026-11-01: known behaviour (hintbook/longplay/owner/oracle) -> build modern directly, one DEVIATIONS piece; decode only unknowns.
- Phase order: maps -> items -> RPG -> dialog -> small fixes; sound/combat polish last. Quality over speed.
- "Just plow along"; next owner playtest Monday 2026-11-02 or Tuesday 2026-11-03: have a FULL PASS build on play.sh by then.
- L8 night look A: OWNER APPROVED 2026-11-01. Drowning 15 s: OWNER APPROVED.
- Open with owner: does the original drown Luther in the Cave river? (river_drowning_state.gd is based on his recollection)
- Workaround rule: hard map details -> logged adapter matching the longplay; exits/movers adapters allowed (only original-route exits, per-host revert flag, DEVIATIONS row).

## Builds
- play.sh: r12x 3cd04ee (PROMOTED 2026-11-02 ~05:00Z, FULL PASS, same audit profile as r12w); fallback play_r12w.sh; WHATS_NEW_r12x.txt. Renderer released to grok.
- Next r12y: astra STORY-007 029b7ae, 008 11b940f, 010 f683b92 (+011/012 coming) + HIVE-FLUTE-FLOOR (lol2_kit).
- (old) r12w d46a181 (PROMOTED 2026-11-01 ~14:20 CET, FULL PASS); play_map.sh AREA; WHATS_NEW_r12w.txt
- r12u-integration fb901ec (d3225c8 + regenerated act2_travel.json), worktree ~/opus_work/lol2_r12u. Staging order: rsync generated media from previous build; prepare_native_scripts --all; L3 1422; L16; L8; L8 shade rows; act2 travel/creatures/items. Affected 467 running -> tmp/regressions/r12u_affected.
- r12w PLAN (promote for Monday): r12v + fable w4-registry tip (chamfer + Museum blockers ON, drowning, items half 2, registry). r12v not promoted (source_walls_test fails by the Museum-flag revert).
- r12v qualification round 2 DONE 2026-11-01 00:59 CET: chain/audits/build/package/smoke PASS; build act1_opus_20261031_r12v NOT promoted. Next: build+qualify r12w (QUALIFY_TEMPLATE.sh with new C/Q/P names), stage liquid packs (HANDOFF_drowning_20261031.txt), include fable 4cbbb8e + astra 7a69a51/cf92a9a, then short packaged run and promote to ~/lol2_playtests/oct23/play.sh.
- r12w-integration fa0020d RUNNING (affected 512 + QUALIFY_TEMPLATE, CPUs 0-15); script /tmp/.../scratchpad/r12w_run.sh; staging log AI_COMMS/act1_completion_20261017/r12w_staging.log.

## Render order after r12u
- lead r12u qualification -> fable W5 proof -> grok-dosbox oracle.
- QUALIFICATION RUN SETTINGS (all needed): --timeout 1200; LOL2_VILLAGE_ESCAPE_SAVE=AI_COMMS/act1_completion_20261017/r12f_qualification/campaign/userdata/act1_broken_runes_monastery_return.json (pinned sha af23a676...; NOT r12t's); LOL2_EARNED_SAVES=classic_review_20261007/lead/act1_r18_campaign_20261013T114244Z/saves; LOL2_BOULDER_EARNED_SAVE=opus_work/fixtures/act1_unfold_earned_defeated.json; LOL2_ORIGINAL_GAME_EXE=lol2_runtime_root/LOLG.EXE. Staging: rsync generated media + scripts/lol2/native_scripts from previous build, then producers.
- r12v-integration f50d945 (~/opus_work/lol2_r12v): affected 446/450 (fails = lead setup only); fixes: registry helpers listed; village tests rerun with --timeout 1200.

## Lanes
- fable (Claude session bob-a8, SendMessage works): movers b29672d full headless; next item families behind item_handlers.gd.
- astra (polls board): task D map leftovers (ASTRA_TASK_20261031D.md); task C last 3 edges wait on Grok 1d.
- grok (polls board): backlog 6: 1d opcode 2 arm 0x3C (PRIORITY, last maps blocker), then items 4/5 second passes.
- codex: inactive today.

## Maps-complete gate
- MAPS COMPLETE 2026-10-31 20:12Z (astra strict gate PASS on f50d945: 41/41 edges, 10/10 levels, 0 blocked; adapters logged).

## Workflow plan
- AI_COMMS/WORKFLOW_PLAN_20261031.md (W1-W10).
