# Local Asset Preservation Manifest

Task: `P3-R1L-FINAL-LOCAL-ASSET-PRESERVATION-AND-DELETION-READINESS-R1`

This manifest records the local-only assets preserved before any future OLD-repository cleanup. No OLD file was deleted or modified. The machine-readable source of truth is [`evidence/preservation/local_asset_manifest.json`](../evidence/preservation/local_asset_manifest.json).

## Repository anchors

| Item | Value |
|---|---|
| OLD repository | `D:\Desktop\my_project\uav_multilink_antisway_control_final` |
| OLD remote | `https://github.com/canimiliya/uav_multilink_antisway_control_final.git` |
| OLD Freeze tag | `research-final-freeze-2026-08-12` |
| OLD Freeze commit | `73d3dbcfbe9388deafb98999c1696fb18e8d7825` |
| Scientific base | `d45e1ab7e1f340d138d870560d7915777b6ce2ef` |
| CLEAN parity/history commit | `56ec73c5712d3b63d182340943a18dc5129e6018` |
| Bundle | `research-local-preservation-2026-08-12.zip` |

## Selection

The Preservation Bundle contains 42 assets, 17,809,454 bytes before the bundle manifest. It contains final T1/T2 media, final boundary figures and summaries, selected boundary metrics, all 16 boundary audit artifacts, and the legacy optional MuJoCo viewer. Every entry has an OLD-relative source path, bundle-relative path, byte size, and SHA256 in the machine manifest.

The CLEAN working copy contains only the two preferred local showcase videos, outside Git history:

| Local path | OLD source | SHA256 match |
|---|---|---|
| `local_media/final_showcase/T1_FINAL_LQR_vs_SATC_WIDECAM.mp4` | `outputs/meeting_demo_boundary_v5/T1/T1_FINAL_LQR_vs_SATC_WIDECAM.mp4` | `true` |
| `local_media/final_showcase/T2_FINAL_LQR_vs_SATC_WIDECAM_WINDHUD.mp4` | `outputs/meeting_demo_boundary_v5/T2/T2_FINAL_LQR_vs_SATC_WIDECAM_WINDHUD.mp4` | `true` |

## Preservation list

### Final T1/T2 media — 11 files

| Bundle path | Size bytes | SHA256 | Classification |
|---|---:|---|---|
| `final_showcase/gallery/T1_full_lqr_048.mp4` | 867096 | `84aba5df731c89b271527258fbc45b715c5b56c6c112e752e54f166feeef07bd` | FINAL_T1_T2_MEDIA |
| `final_showcase/gallery/T1_hybrid_x007_y041_z041.mp4` | 2470191 | `daa595d419c4dabaf0babb282b08bb3b23045f89063fda7d2ca5639e9cff9fe2` | FINAL_T1_T2_MEDIA |
| `final_showcase/gallery/T1_satc_b_027.mp4` | 741505 | `e379f588133f2542a2cbba0f531499a551b00a45e7943e5e7b5cdeca14876608` | FINAL_T1_T2_MEDIA |
| `final_showcase/T1/T1_FINAL_LQR.mp4` | 1216319 | `eb6bb42c2d46ed48bbcc1a458d75ab85c46a9c00836e4549acd9511c53b9fc5e` | FINAL_T1_T2_MEDIA |
| `final_showcase/T1/T1_FINAL_LQR_vs_SATC.mp4` | 2238447 | `052db99cd55beaa7a2a03a639956ad4485878c742cd95728d628af56161c1bad` | FINAL_T1_T2_MEDIA |
| `final_showcase/T1/T1_FINAL_LQR_vs_SATC_WIDECAM.mp4` | 1086911 | `83e125bad6f55a6fdc33a8985061caff87ff89edbc3b42734ce4bcfac4272b3b` | FINAL_T1_T2_MEDIA |
| `final_showcase/T1/T1_FINAL_SATC.mp4` | 918909 | `f8947d3e5f67a447e50ce2bb1d53e076a80a29cf3ff92e650d944d7d1474d6b4` | FINAL_T1_T2_MEDIA |
| `final_showcase/T2/T2_FINAL_LQR.mp4` | 1095381 | `75dd9d564c8219afcc36de576dbf999c1a4359ffb720b1f2d2c494092a1bcaba` | FINAL_T1_T2_MEDIA |
| `final_showcase/T2/T2_FINAL_LQR_vs_SATC.mp4` | 2381437 | `e065ef63e67f87517872b4e4e5aeee02bffa13451cf2922acb9b09e26dabdb29` | FINAL_T1_T2_MEDIA |
| `final_showcase/T2/T2_FINAL_LQR_vs_SATC_WIDECAM_WINDHUD.mp4` | 1074091 | `f88abbd00dc889b74dd198577490eb081c05835f153fc4e6f85d4fbe359a2eae` | FINAL_T1_T2_MEDIA |
| `final_showcase/T2/T2_FINAL_SATC.mp4` | 1148796 | `498d5c6d09d76ec5430484af109c962d72c02b7b83fdfc781f80d66dd3123e7c` | FINAL_T1_T2_MEDIA |

### Boundary audit artifacts — 16 files

The complete list, sizes, and SHA256 values is maintained in the machine manifest. These are the 16 files copied from `artifacts/meeting_demo_boundary_v5/`: `INVALID_T2_STAGE1_DURATION_RETRY.md`, `job_registry_final.json`, `job_registry_initial.json`, `parallel_execution_audit.json`, `run_manifest.json`, `t1_boundary.json`, `t2_boundary.json`, `t3_existing_evidence.json`, `tracking_test.png`, `visual_polish_first_frame.png`, `visual_polish_first_frame_final.png`, `visual_polish_first_frame_v2.png`, `visual_polish_first_frame_v3.png`, `visual_polish_last_frame.png`, `visual_polish_last_frame_final.png`, and `visual_polish_last_frame_v3.png`.

### Boundary metrics — 7 files

| Bundle path | Size bytes | SHA256 | Classification |
|---|---:|---|---|
| `metrics/boundary/T1/4.0s_full_lqr_048_metrics.json` | 1642 | `62da91f9c3747fca926ebcd1d5246dfacd5b692f59703cb8f0bb013b7748fe06` | BOUNDARY_METRIC |
| `metrics/boundary/T1/5.0s_full_lqr_048_metrics.json` | 1601 | `63a291f0825661ea901436138956ffa9343725f47cc0b3c3f52c7f9839c971bf` | BOUNDARY_METRIC |
| `metrics/boundary/T1/5.0s_satc_b_027_metrics.json` | 1587 | `3c6462de55e073591d7e15e96fdd806591cf5ac8c345377df54a8a8d4f5fded6` | BOUNDARY_METRIC |
| `metrics/boundary/T1/6.0s_full_lqr_048_metrics.json` | 1614 | `80ec4f79c0777c9ddc39523b318c957d077c6f1f6c0a2f24bf83b04ed4e05733` | BOUNDARY_METRIC |
| `metrics/boundary/T2/3mps_full_lqr_048_metrics.json` | 1770 | `0061971783bd4958ac2b6980fed56dbe5623447f8f533c61d88bf5be81cc6903` | BOUNDARY_METRIC |
| `metrics/boundary/T2/3mps_satc_b_027_metrics.json` | 1766 | `7ab5ea73d4bea51a0d32b42bcc5c4973d6f865fde869bb19c3ec5881bffe2126` | BOUNDARY_METRIC |
| `metrics/boundary/T2/5mps_satc_b_027_metrics.json` | 1799 | `01984a7c9b44f7791db32b718c49a9a98f116730f79605a72cd67486f6cf8c7f` | BOUNDARY_METRIC |

### Final figures, summaries, and viewer — 8 files

| Bundle path | Size bytes | SHA256 | Classification |
|---|---:|---|---|
| `metrics/final/FINAL_THREE_SCENARIO_ENVELOPE.png` | 98009 | `66414dbbb82cba38786fbe54a614f3dcdd31ab68f27abd614610d2993f122147` | FINAL_BOUNDARY_FIGURE |
| `metrics/final/FINAL_THREE_SCENARIO_METRICS.md` | 780 | `42f65fb084b64b323ea2ffc4f9d2aa25c20e98f729c3c98270632ff4dbcd9f49` | FINAL_METRICS |
| `metrics/final/P3_R1G_RENDER_MANIFEST.json` | 1249 | `139f5c05f4c53f787ea58ad242509b23444b817330cabb3c61df66f300d03c1a` | FINAL_MANIFEST |
| `metrics/final/T1_move_duration_envelope.png` | 55753 | `6c1c09dd012b0e1116a13613d4bc9dc3e227a0a073141426822eb34b318e92ed` | FINAL_BOUNDARY_FIGURE |
| `metrics/final/T1_T2_boundary_overview.png` | 100539 | `16f0a4317045ecfbea6e77b85f1cd4fa4990f0b7762f7c92a324305f5b7d32de` | FINAL_BOUNDARY_FIGURE |
| `metrics/final/T2_composite_wind_envelope.png` | 49877 | `3c6afbbbfcc62b130d262b946d36eade8ed11c79a53c863348ec6a497a761ff3` | FINAL_BOUNDARY_FIGURE |
| `metrics/final/T2_CONTROLLER_BOUNDARY_GAP.md` | 172 | `a8fe2682f9bc7a335a722880bd1ae3c1eb49ed8c0eb49001281197381ee75ced` | FINAL_BOUNDARY_AUDIT |
| `viewer/live_viewer.py` | 6065 | `e6d1828a14604e3bf33640b935685c5e4fe5e7f736d1245b2b7fd8a174bbd928` | LEGACY_OPTIONAL_VIEWER |

## Explicit exclusions

- `reproducibility/v2` run banks, candidate grids, `training_bank.npz`, `render_states.npz`, boundary-sweep CSV files, caches, `.pytest_cache/`, and `__pycache__/`: regenerable or runtime data.
- Native raw outputs, native benchmark banks, debug logs, and the old failed-video collection: either recoverable from OLD Git history, summarized by the research archive, or not needed for the preserved final showcase.
- Full `outputs/meeting_demo_recoverable_v4/T3/`: T3 is already represented by the tracked CLEAN evidence `evidence/frozen/T3_ARCHIVED_BOUNDARY.json` with LQR 3 m/s and SATC 5 m/s; `T3_LOCAL_MEDIA_DUPLICATION_REQUIRED = false`.
- `.vscode/`: editor-local configuration only.
- No scientific source, model, controller, parameter, scenario, or OLD repository file was modified or deleted.

## Status labels

- `live_viewer.py`: `STATUS = LEGACY_OPTIONAL_VIEWER`; `NOT_FROZEN_SCENARIO_IMPLEMENTATION = true`.
- Bundle integrity is established only after the zip is created, extracted, and rehashed; the final readiness report records those results.
- This manifest is archival preservation, not a new scientific result.
