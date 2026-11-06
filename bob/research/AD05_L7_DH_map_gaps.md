# AD05 L7_DH iron door and the prism name

Base maps-y 4a32849. The live scripts were searched. Map.png was not regenerated. No game patch.

## Iron door

The place is already in the pack. The motion stays unread.

Control 84 in `L7_DH.json` is (−1243, 614), height 750. H12 reads static slot 40 as Iron Door. This pass matched that coordinate and did not re-read the name table. The 2026-10-21 Dark Halls deviation leaves the Iron Door walk-through. H12's door group has no Spark command. A motion patch would invent the shove. A marker was added. No door-motion test exists. Godot was not run.

## Prism name

Already hosted by `dark_halls_items.gd`.

The label is Prism scroll. The source name is 149-Prsmscrl.

- Control 971 at (−2595, 3634), height 85, one grant.
- Control 975 at (−2331, 2393), height 55, two grants.

Hintbook 2486 hides the scroll in a bookcase. Which of the two controls that sentence means stays unread. Markers were added for both. The world-item row 139-SS6 stays SS6. Tests `dark_halls_loot_test.gd` and `dark_halls_earned_detour_test.gd`. Godot was not run.

`markers.json` had 12 rows. It now has 15.
