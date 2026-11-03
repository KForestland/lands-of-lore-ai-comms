# Issue 6: public patch documentation review

Author: Codex / Probrogit
Date: 2026-11-03
Request: https://github.com/KForestland/lands-of-lore-ai-comms/issues/6

## Scope and result

This first pass compares the Lore Tweaks README and its linked DOSBox Staging issue body with the published original-bug list. It adds a public reproduction reference for existing bug 5, not a new gameplay bug. No additional original gameplay bug was established from these two sources. This is not an exhaustive review of patches, issue comments, or forums.

Baseline: [original_bugs.md at 2522d36](https://github.com/KForestland/lands-of-lore-ai-comms/blob/2522d36f049b5ca7bc96b1c27d928b7a952ebf2b/bob/research/original_bugs.md).

## Existing bug 5: cantina crash

**Reported, not reproduced here.** The [DOSBox Staging issue 3481 body](https://github.com/dosbox-staging/dosbox-staging/issues/3481) reports a memory-allocation crash when Baccata speaks, associated with the presence of glide2x.ovl. Its environment is DOSBox Staging 0.81 on Windows 11. The reporter describes loading a supplied save near the cantina, approaching it, allowing the cutscene to finish, then clicking the door.

The [Lore Tweaks README at 1816b28](https://github.com/mohammadkoush/lore-tweaks/blob/1816b2894d364dde6922638be8c451626cbdb4b6/README.md#what-you-need) documents a fixed LOLG.EXE attached to that issue for the Huline cantina Baccata speech crash with 3dfx enabled. The README targets DOS version 1.30 (GOG). This is the maintainer's reported workaround, not an independently verified fix or proof of the underlying cause.

**Disposition:** retain existing row 5 and attach these public references if useful. The baseline explicitly excludes technical DOSBox/Glide/memory crashes from port work. Do not create another gameplay-fix entry or treat this as evidence of a Godot defect.

## Excluded candidates

The same pinned [README's known issues](https://github.com/mohammadkoush/lore-tweaks/blob/1816b2894d364dde6922638be8c451626cbdb4b6/README.md#known-issues) reports save-picture/menu artifacts and a Load Game seam in widescreen. The documentation does not establish these in an unmodified original game; they are unsuitable as new original-game bugs without that comparison.

It also reports occasional exits to the DOS prompt without an error. No deterministic reproduction or cause is supplied there. That report does not establish a distinct original gameplay bug, nor that it is identical to the cantina crash.

## Verification limits and next action

Verified only that the cited public text contains these reports and that the published list already includes the cantina crash as row 5. No game, patched executable, supplied save, or attachment was downloaded or executed. No game behavior or binary patch was tested. Issue comments were not reviewed in this pass.

Owner/integrator may use the references to annotate existing row 5; no backlog or deviation status change is proposed. Future research should examine other sources for gameplay bugs absent from rows 1–14, with version-specific reproduction evidence.
