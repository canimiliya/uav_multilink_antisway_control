# UAV Multi-Link Anti-Sway Control

This repository is the minimal clean export of the frozen MuJoCo simulation for a UAV carrying five passive rigid links and a 2.5 kg cutter payload.

The frozen controller lineup is:

- PID: `V3CascadedTaskPID`, `hybrid_x007_y041_z041`
- Full-LQR: `V3FullStateLQR`, `full_lqr_048`
- SATC: `SATC-OFMPC`, `satc_b_027`

T1, T2, and the archived T3 boundary are the formal frozen scenarios. This repository is currently at the clean-export bootstrap stage; formal old-vs-clean parity is a separate task and has not been run here.

Source provenance:

- Freeze tag: `research-final-freeze-2026-08-12`
- Freeze commit: `73d3dbcfbe9388deafb98999c1696fb18e8d7825`
- Scientific base HEAD: `d45e1ab7e1f340d138d870560d7915777b6ce2ef`

The five-link MuJoCo model is byte-frozen. Udaan is retained as a submodule at commit `9eb1a2dcfe438ce7b4c4cd119072e4f3d8a6a816`. The minimal source, frozen configs/evidence, and smoke tests are documented in `docs/CLEAN_EXPORT_MANIFEST.md`.

This export intentionally contains no historical experiment banks, generated outputs, videos, caches, native-stack research history, or interactive `live_viewer.py`.
