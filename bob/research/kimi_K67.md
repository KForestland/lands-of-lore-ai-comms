# Kimi K67 — L20 movable 52 + doorway 50/51 (research for grok BK08e)

## Movable 52
## Doorway 50/51
## Smallest fixes

• All the evidence is in. Here is the research report for Grok's BK08e.

## Movable 52

**Records on `movable:52`** (`scripts/lol2/native_scripts/L20_BB.json`, placement at file 15551017): exactly **one** record — kind-6, caller byte **0x0F** (melee-strike caller), group 9472, no predicate (event file 15529507, raw `060600250f00`). No kind-9, no kind-2, no kind-4. Fable's "no kind-9 record" is confirmed — but note the door's **actor twin** `actor:52` *does* have four kind-9 records (groups 17468/17960/18022/18418); their groups only arm/animate the actor (op2 arm6, op8 arm1, op13 ×2 on `actor:52`), so striking the grate rattles it without moving it. Group 9472 itself is just a feedback loop: op14 arm 3 starts `prop:2`'s timer (group 24 → enqueue `prop:2` k6 0x14 → group 42 stops it, enqueues `prop:109`).

**Placement**: mode byte +0x22 = **0** (not rotary), angle byte +0x24 = 110, position (-3554, -50, -4740). Its 36 pack faces are the whole **barred grate** (x −3604..−3504, y −50..202, z −4745..−4735) standing just north of slabs 53/54 (z −4758..−4750), its centre exactly on their seam.

**Groups moving `movable:52`** (kind byte 0x20 = movable class, `native_script_host.gd:1032`):
- **Group 12732** (file 15503525): `op1 travel 100 on movable:52` (`012034006400`) + opcode 22 (voice line). Caller: `actor:47` (DRAR_PH, 1600 hp, at (-3576,-50,-3986)) kind-6 **caller 0x0B**, no predicate (file 15525689).
- **Group 12898** (file 15503691): `op1 travel 100 on movable:52` alone. Caller: `actor:48` (SCOTIA, 1500 hp, at (-3539,-50,-3877)) kind-6 **caller 0x0B**, no predicate (file 15525723).
- No opcode-9 arm anywhere targets `movable:52` (the op9s on "52" in groups 1362/1584–1746/2808 are kind 0x02 = **actor**:52). Group 2808 (prop:130, the combination panel) does op9 arm 3 + op18 on `actor:52`, gated by predicate 71 (`060453044e` — left/right type 4, **unhosted** at `native_script_host.gd:861-891`).

**Native open chain**: kill guardian 47 or 48 → the death caller 0x0B fires the actor's kind-6 → opcode 1 stages travel 100 on the mode-0 grate (via adapter `opcode1_other_modes`, on by default, `native_script_host.gd:1159,1183-1186`) → travel = (110×100)/100 = 110 → `_pose` non-rotary branch slides the grate **up 260 units** (bounds.y 252 + 8, `act2_progression.gd:936-945`). The port has all of this working **except the caller**: nothing fires actor kind-6 caller 0x0B on creature death — `scripted_creature_population.gd:339-351` zeroes health and prints "defeated" with no native fire (the one precedent is `dark_halls_doors.gd:271`, which fires caller **10** for SHADE 73's end).

## Doorway 50/51

**Placement** (files 15550935/15550976): both **mode 6 rotary**; angle bytes 85 (50) and 65 (51) → mode-6 angle words ((2N%360)<<16)/360 = 30947 (**170°**) and 23665 (**130°**) (`native_script_host.gd:340-346`). Hinge origins are the placement positions (-4731,-50,-4826) / (-4731,-50,-4876) — the **centres** of the leaves (leaf 50 spans z −4851..−4801, leaf 51 z −4901..−4851, both x −4735..−4727, y −50..75; a double door across a 100-wide opening between regions 1019 and 871).

**Strike → travel 100**: kind-9 records (extra `0184`, predicate 206 = context byte +0x25 == 0) group 9278 on `movable:50` (file 15529409) and group 9384 on `movable:51` (file 15529465); each group does op16 (+0x25=1), op9 arm 0x0E (sets the +0x15 bit 0x80 "open" flag, `native_script_host.gd:1499`), op5 arm 3, then `op1 travel 100` on **both** leaves.

**Open pose in the port** (`act2_progression.gd:928-932`): rotary → rotate the hinge about the placement centre by −travel/65536·TAU. Leaf 50 ends at 170° (10° off its closed line, footprint z −4850.6..−4801.4 — essentially the closed box); leaf 51 ends at 130° (diagonal, z −4892.1..−4859.9, x −4750.1..−4711.9). **Both leaves stay inside the opening**; the widest gap is ≈9 units at the seam vs the capsule radius 15 (`player_form_body.gd`). Collision is the leaf trimesh on layer 1 built at `act2_progression.gd:895-911` and it rotates with the hinge, so **the leaves' own collision keeps the doorway shut** — this is what stops Fable's walk.

**No region blocker is involved**: `assets/lol2/generated/region_blockers/L20_BB.json` has only static regions 260–264/322–346 (none near (-4731,-4851)) and zero dynamic (all five L20 opcode-197s are arm 10 list-marks, not bit toggles). The nav graph natively **links 1019 ↔ 871** through this doorway (`creature_nav/L20_BB.json`), and there is no `wall` face at x=−4735, y −50..75 — only the lintel (face 5063, y 75..125). (Side note: region kind-11 records fire groups 264/276/288/300/312/324 — opcode 196 with flags byte 0x08 on the 0x22d0c records of regions 50–55 — which the host refuses at `native_script_host.gd:1943-1945`; they are floor-rate writes, not the block.)

## Smallest fixes

1. **Movable 52 (grate stays shut)** — fire the native death caller. Where a creature's health reaches 0 (`scripted_creature_population.gd:349`, or an `act2_creatures.gd` L20 hook for actors 47/48), call `native.fire_event("actor:<id>", 6, {"caller_byte": 11})`, mirroring the caller-10 precedent at `dark_halls_doors.gd:271`. Group 12898 (SCOTIA) then runs as-is and `_pose` lifts the grate. Group 12732 (DRAR_PH) additionally needs opcode 22 registered (currently unhandled → the group is refused at `native_script_host.gd:926-932`); a one-line sound/voice stub like `_op_sound` (opcode 20, `native_script_host.gd:391`) is enough. No predicate or record patching required — both records are predicate-free.
2. **Doorway 50/51 (open leaves still block)** — honour the native "opened" flag instead of re-posing geometry. The native data genuinely swings these centre-hinged leaves to 170°/130° (PROVEN hinge-at-placement-origin, `act2_progression.gd:10`), i.e. the native unblock is not geometric; the strike group's op9 arm 0x0E sets byte +0x15 bit 0x80 (`native_script_host.gd:1499`). Smallest port fix: in `act2_progression.gd` (near the `_pose` commit, `:334-335`), when a movable's staged state has `bit_0x15_0x80 == 1` (or travel reaches its full angle word), drop the mover body's collision layer (`:897`) so the opened leaves no longer stop the capsule. Log it as an adapter in `docs/DEVIATIONS.md` (the native +0x55 continuation that unblocks was never entered, per the host note at `native_script_host.gd:1092-1093`). Do **not** move the hinge to an edge — that contradicts the proven native model.

