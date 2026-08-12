# OLD Local Repository Deletion Readiness

Task: `P3-R1L-FINAL-LOCAL-ASSET-PRESERVATION-AND-DELETION-READINESS-R1`

This is the final preservation/readiness audit before any separately authorized deletion of the OLD local repository. The deletion itself was not performed in this task.

## Current state

| Item | Result |
|---|---|
| OLD repository | `D:\Desktop\my_project\uav_multilink_antisway_control_final` |
| OLD current size | `1.828862 GB` (`1,963,725,304` bytes; full directory including `.git`) |
| OLD Freeze tag | `research-final-freeze-2026-08-12` |
| OLD Freeze commit | `73d3dbcfbe9388deafb98999c1696fb18e8d7825` |
| OLD remote Freeze verification | `true`; remote annotated tag dereferences to the Freeze commit |
| Scientific base | `d45e1ab7e1f340d138d870560d7915777b6ce2ef` |
| OLD files deleted | `0` |
| OLD source/model/controller/parameter/scenario changes | `0` |

The OLD worktree still contains the pre-existing untracked `.parity_tmp/`, `.vscode/`, and `scripts/meeting_demo/live_viewer.py`. They were inspected; none is an unknown important asset. No OLD cleanup command was run.

## Preconditions confirmed

- `RESEARCH_FREEZE_REMOTE_VERIFIED = true`.
- `CLEAN_FUNCTIONAL_PARITY = PASS`, from `docs/MIGRATION_PARITY_REPORT.md`.
- T1/T2 time-series maximum difference: `0`.
- T1/T2 metrics maximum difference: `0`.
- `RESEARCH_HISTORY_ARCHIVED = true`, in `docs/RESEARCH_HISTORY.md` and `docs/RESEARCH_HISTORY_SOURCE_INDEX.md`.
- CLEAN parity/history commit before this task: `56ec73c5712d3b63d182340943a18dc5129e6018`.
- CLEAN local HEAD and `origin/main` were equal before this task: `56ec73c5712d3b63d182340943a18dc5129e6018`.

## Preservation result

The preservation manifest is [`docs/LOCAL_ASSET_PRESERVATION_MANIFEST.md`](LOCAL_ASSET_PRESERVATION_MANIFEST.md). The machine-readable manifest is [`evidence/preservation/local_asset_manifest.json`](../evidence/preservation/local_asset_manifest.json).

| Item | Result |
|---|---:|
| Local-only important assets enumerated | `42` |
| Asset bytes preserved in Bundle | `17,809,454` bytes (`16.984419 MB`) |
| Bundle file count | `43` (`42` assets + `manifest.json`) |
| Bundle size | `17,370,281` bytes (`16.565591 MB`) |
| Bundle SHA256 | `5e2b513e9bb58c540d1e4a9bd74c6c29064110202ade427413ec577d5ac94d28` |
| Bundle local integrity | `PASS` |
| Preservation Release | [`research-assets-preservation-2026-08-12`](https://github.com/canimiliya/uav_multilink_antisway_control/releases/tag/research-assets-preservation-2026-08-12) |
| Release type | GitHub prerelease |
| Release target | CLEAN parity commit `56ec73c5712d3b63d182340943a18dc5129e6018` |
| Preservation Release uploaded | `true` |
| Downloaded Bundle SHA256 | `5e2b513e9bb58c540d1e4a9bd74c6c29064110202ade427413ec577d5ac94d28` |
| Remote preservation verified | `true` |

The downloaded Release ZIP was extracted into `.preservation_verify/remote_extract/`. All 42 manifest assets were present and rehashed: `HASH_MISMATCH_COUNT = 0`. The Release asset server reported the same SHA256 digest as the local ZIP.

## Local showcase media

The two preferred final videos were copied to CLEAN `local_media/final_showcase/` and are ignored by Git:

| File | SHA256 match with OLD |
|---|---:|
| `local_media/final_showcase/T1_FINAL_LQR_vs_SATC_WIDECAM.mp4` | `true` |
| `local_media/final_showcase/T2_FINAL_LQR_vs_SATC_WIDECAM_WINDHUD.mp4` | `true` |

`T3_LOCAL_MEDIA_DUPLICATION_REQUIRED = false`. T3 remains represented by the tracked CLEAN evidence `evidence/frozen/T3_ARCHIVED_BOUNDARY.json` with historical LQR `3 m/s` and SATC `5 m/s`; T3 was not rerun and its full old media directory was not copied.

## Four-way OLD asset classification

The following disjoint classification covers the complete current OLD directory, including `.git`; sizes were recomputed from the current files.

| Category | Files | Size GiB | Meaning |
|---|---:|---:|---|
| `A_REMOTE_RECOVERABLE` | 3,148 | `1.551930` | OLD Git history/tracked evidence and the Udaan checkout, recoverable from remotes |
| `B_PRESERVED_IN_RELEASE` | 42 | `0.016586` | Local-only final/boundary assets preserved and remotely verified in the Release |
| `C_REGENERABLE` | 653 | `0.207404` | `.parity_tmp`, caches, run CSV/NPZ banks, and other regenerable runtime data |
| `D_DISCARDABLE_HISTORY` | 46,432 | `0.052941` | Non-final local media, editor configuration, and historical/debug material not needed for the clean result |
| **Total** | **50,275** | **1.828862** | **Current OLD directory** |

`UNKNOWN_UNBACKED_IMPORTANT_FILES = 0`: every current OLD file is covered by one of the four classes, and every class-B asset has a byte-preserving remote copy. `.vscode/` is editor-local only. `live_viewer.py` is preserved in the Release as `LEGACY_OPTIONAL_VIEWER`, with its original SHA256; it is not a frozen scenario implementation.

## Size accounting

Measurement basis: PowerShell recursive file sizes, binary MB/GB units. CLEAN worktree size excludes `.git`, `.preservation_tmp`, and `.preservation_verify`, but includes `local_media/final_showcase/`.

| Measurement | Size |
|---|---:|
| `CLEAN_WORKTREE_AND_LOCAL_MEDIA_SIZE_MB` | `36.627228 MB` |
| `CLEAN_GIT_SIZE_MB` | `56.952024 MB` |
| `PRESERVATION_TMP_SIZE_MB` | `33.565205 MB` |
| `.preservation_verify/` size, informational | `50.564818 MB` |
| OLD current size | `1.828862 GB` |
| Expected reclaimable if OLD is deleted while current preservation and verification workspaces are retained | `1.746703 GB` |

Deleting only OLD would release `1.828862 GB`; the lower expected-reclaimable figure subtracts the currently retained `.preservation_tmp/` and `.preservation_verify/` workspaces. No deletion has occurred.

## Validation restrictions respected

- CLEAN tests: `11 passed` (`tests/clean_smoke` and `tests/migration_parity`).
- T1/T2 formal simulations were not rerun.
- T3 was not rerun.
- Holdout was not run.
- PID, Full-LQR, SATC, XML/model, parameters, and scenarios were not modified.
- OLD `git clean`, deletion, output clearing, reproducibility clearing, `.git` deletion, reset, rebase, force push, and tag mutation were not performed.

## Final decision

All required preservation gates passed:

```text
FREEZE_REMOTE_VERIFIED = true
CLEAN_FUNCTIONAL_PARITY = PASS
RESEARCH_HISTORY_ARCHIVED = true
LOCAL_ONLY_IMPORTANT_ASSETS_ENUMERATED = true
PRESERVATION_MANIFEST_CREATED = true
PRESERVATION_BUNDLE_CREATED = true
BUNDLE_LOCAL_INTEGRITY = PASS
PRESERVATION_RELEASE_UPLOADED = true
REMOTE_PRESERVATION_VERIFIED = true
UNKNOWN_UNBACKED_IMPORTANT_FILES = 0
FINAL_T1_VIDEO_LOCAL_COPY = true
FINAL_T2_VIDEO_LOCAL_COPY = true
CLEAN_TESTS = PASS
OLD_REPO_FILES_DELETED = 0
OLD_LOCAL_REPO_DELETION_READY = true
```

`OLD_LOCAL_REPO_DELETION_READY = true` means the OLD repository may be deleted only after a separate explicit owner authorization. This task stopped without deleting it.
