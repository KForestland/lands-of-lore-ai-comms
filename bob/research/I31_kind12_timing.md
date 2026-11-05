# I31 region kind 12, enter or stand or leave

VA 0xF2DFD was not read this pass. Enter, stand, and leave stay unknown.

The host comment in `native_script_host.gd` says the kind-12 selection is the u16 at +4, which matches the region index, and the byte at +6, which is the event. It says event 2, at fixup VA 0xF2DFD, accepts when byte +7 is 0. Other events are not entered. That comment is the host. It does not say the event fires on entry, while standing, or on leaving.

L16 has 128 kind-12 records on region objects. Every one is 8 bytes, and byte +7 is 0.

| byte +6 | count | host |
| --- | --- | --- |
| 2 | 101 | the hosted check, byte +7 is 0 |
| 3 | 24 | not entered |
| 4 | 3 | not entered |

Regions 216, 217, and 218, the mantle copies, are event 2. The level-change regions already listed for L16, L17, and L20 are also kind 12. Their byte +6 was not re-tallied here. L17 has 21 region-object kind-12 records, L19 has 965, and L20 has 104. Those event bytes were not counted.

## Still open

Whether event 2 is enter, stand, or leave. Events 3 and 4. No frame.
