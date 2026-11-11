# K102 (Claude reviewer): ITEM_GRANT_PLAN rev 3 (F-08) on fde4d19 - VERDICT: PLAN NEEDS WORK

K98: all 3 MAJOR and the MINORs closed or soundly rejected. Census complete (~90 lines in 63 files, none missed). No drift.

New:
1. MAJOR source guard blind to ItemGrants.pack(host).append/erase and to host.get("carried_collected") aliases (area_world_items.gd:74, jungle_world_items.gd:60, jungle_source_pickups.gd:39, museum_broken_thohan.gd:131). Add both forms to rules 1-2 plus probes.
2. MAJOR commit 8 switches on L8 prop 99 (serum, def 119) although it fails condition 4: act2_items_catalog.gd:75 shaman_amaranth has the same def; l8_shaman_trade.gd:24 does not see the native grant id -> two serums, and the native serum skips the shaman trade (sequence break). Drop prop 99 or make the shaman owner refuse on any same-definition id.
3. MINOR table 2.1 still lists pure builders as live add sites (l10_emperor_state:67, l13_altar_state:36, l13_dawn_release:35, l8_journey_state:44/52/71, l10_priest:52-53, l10_silverleaf_harvest:24-25); commit 10 lists static rule functions with no host.
4. MINOR ItemGrants.commit adds a 64 cap check 31 sites lack today (a 66-item pack could no longer use an item); no refusal text; Cave host unspecified.
5. MINOR no duplicate:"allow"; a refusal after the owner writes "taken" loses the item (l16_dry_fountain:155, l14_hopper_platform:78, l12_frozen_bow:55).
6. MINOR act2_world_items.gd:86-90 can drop the history write after migration (stale local packet).
7. MINOR native path omits gates: opcode3_item_grant adapter and global 0x223D4 (native_script_host.gd:1701-1706); cite DEVIATIONS 0191.
8. MINOR commit 7/8 tests that cannot fail (tool vs itself; "press E again" passes if the group never re-fires).
9. MINOR 16 refusal texts, not 4; "fifteen golden saves" do not exist at fde4d19; known(host,id) needs a defined host->scope map.
