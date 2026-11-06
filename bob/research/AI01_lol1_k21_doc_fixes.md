# AI01 LoL1 doc corrections, 2026-11-06

No Godot was run. `lol1_godot` stayed read-only. The decompile is `<owner-media>`. U01 and `U04_lol1_l06b.md` were searched. Neither file holds these four sentences.

## Freeze scroll

`level08_inf.asm` function 335 calls `createLevelItem` on type 234, block 368, after the wall-type test on side 3. Type 234 is Freeze scroll in M04. Riddle Scroll stays type 241. This function does not place it. The walkthrough beat stays in L03.

`lol1_story_full.md` LOL1-06 item cell now names that create. M03's cave-item row now names it too. Grade DECODED for the create.

## Ruby of Truth

`level11_inf.asm` has no function 132. Label `L_132` holds `giveItem` of type 220 at asm 2087 and `makeItem` of type 220 at asm 2197. Functions 281 and 653 jump to that label. The same label also calls `createHandItem` on type 220 at asm 2099.

Function 45 calls `makeItem` on type 259 and `createHandItem` on type 220 at asm 6347. Its `giveItem` at asm 6376 pushes type 125. None of the ruby calls carries a floor block. Grade DECODED for those call sites. The chieftain-trade sentence stays the clue book. The mask block stays UNKNOWN.

K21's line that `giveItem(220)` sits inside function 45 at asm 6347 and asm 6376 does not match those bytes. The story cell and the U02 paragraph name `L_132` for the give and the make, and function 45 for `createHandItem`.

## Empty flask

Both constant `createLevelItem` calls of type 211 are in `level08_ini.asm` function 1, blocks 117 and 469. Function 0 has no push of 211. The other push of 211 is asm 227, inside function 1, and it is an `initMonster` argument. U02 and M03 now say function 1. Dawn's gift stays a separate sentence. Grade DECODED for the two creates.

## Bloodstone

`level16_ini.asm` has functions 0 and 1. Label `L_18` calls `makeItem` on type 273 and then `giveItemToMonster`. Function 1 reaches that label by `jmp`. The `makeItem` has no block argument. Grade DECODED for that call. The rock-beast sentence stays unmerged.
