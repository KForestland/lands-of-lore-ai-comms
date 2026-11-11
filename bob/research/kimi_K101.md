# K101 (Claude reviewer): Sol C-10 follow-up 121d4e4 + 6150362 on 007eaf8 - VERDICT: APPROVE

All K99 findings fixed or disclosed (both bars clicks assert native -40 first; clock 1/60 asserted everywhere; aids disclosed). New L19 floor save packet: old saves load, L19-only, validated before any change, right order.

MINOR 1 act2_progression.gd:444 - opcode-18 pose slot clear narrowed to L19_BC for every area, undisclosed (ledger 0624 says no L10/L9 change). No effect today (native_script_host.gd:1001 clears it), but revert or disclose.
MINOR 2 act2_progression.gd:1335-1342 - L19 struck-ref reset does nothing on real L19 data; ledger overstates; incomplete if a struck movable is added (no travel[id]/_pose update).
MINOR 3 tests/l19_floor_save_test.gd:42 - "not carried through the floor delta" check cannot fail.
MINOR 4 tests/act2_floor_checkpoint_test.gd:26 - PASS text claims more than it covers.
