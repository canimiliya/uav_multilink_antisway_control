# Research History Source Index

本索引用来核对 `docs/RESEARCH_HISTORY.md` 的关键陈述。Confidence 只表示旧仓库证据的直接程度，不表示方法本身在更广泛现实系统中的有效性。

| History section | Supporting commit/tag | Supporting files | Confidence |
|---|---|---|---|
| 项目问题、五连杆、2.5 kg cutter、三类任务 | `v1.0.0` / `62769122b6b75cd124c9cabc48aee2976a159f6b` | `README.md`; `docs/V2_RESEARCH_CONTRACT.md`; `reproducibility/v2/task_contract.json` | HIGH |
| 旧 direct-tip PID 失败及 anti-windup 根因 | `v3-research-final-2026-08-09` | `reproducibility/v3/r1r1/r1_pid_failure_audit.json`; `scripts/audit_v3_r1_pid_failures.py` | HIGH |
| corrected PID 冻结 | `v3-research-final-2026-08-09` | `reproducibility/v3/r1r1/pid_competence_audit.json`; `reproducibility/v3/r1r1/pid_freeze.json`; `reproducibility/v3/r1r1/gate.json` | HIGH |
| Full-LQR 成为 primary traditional comparator | `v3-research-final-2026-08-09` | `reproducibility/v3/r1/full_lqr_freeze.json`; `reproducibility/v3/r1/primary_traditional_baseline.json` | HIGH |
| OF-TSRMPC 的结构性限制 | `v2-research-final-2026-08-09` | `reproducibility/v2/r3r1/of_tsrmpc_failure_mechanism.json`; `reproducibility/v2/r3r1/failure_mechanism_audit.json` | HIGH |
| DR-TSRMPC 的 partial success 与 acquisition gate 失败 | `v2-research-final-2026-08-09` | `reproducibility/v2/r3r2/paired_traditional_comparison.json`; `docs/V2_FINAL_TECHNICAL_REPORT.md` | HIGH |
| V3 Self Holdout 失败及 3.5 m/s cohort | `v3-research-final-2026-08-09` | `docs/V3_FINAL_TECHNICAL_REPORT.md`; `reproducibility/v3/r4/holdout_results.csv`; `reproducibility/v3/r2/self_architecture_history.json` | HIGH |
| V3 Paper adaptation Development-ineligible | `v3-research-final-2026-08-09` | `reproducibility/v3/r3/paper_selection.json`; `reproducibility/v3/r3/paper_search_history.json`; `reproducibility/v3/r3/near_miss.json` | HIGH |
| V4 CART 修复 steady infeasibility 但 tail gate 失败 | `v4-research-final-2026-08-09` | `docs/V4_CART_OFMPC_DEVELOPMENT_REPORT.md`; `docs/V4_FINAL_TECHNICAL_REPORT.md`; `reproducibility/v4/r0/failure_mechanism_report.json` | HIGH |
| SATC 机制组成与 V5 Development freeze | `v5-research-final-2026-08-09` | `docs/V5_FINAL_TECHNICAL_REPORT.md`; `reproducibility/v5/final/mechanism_summary.json`; `reproducibility/v5/self/mechanism_report.json` | HIGH |
| SATC V5 Holdout Overall win、19/20、Strict gate false | `v5-research-final-2026-08-09` | `reproducibility/v5/final/claim_matrix.json`; `reproducibility/v5/final/metric_summary.json`; `reproducibility/v5/holdout/gate.json`; `reproducibility/v5/holdout/self_vs_primary.json` | HIGH |
| V6 Paper adaptations failed and Holdout stayed locked | `v6-research-final-2026-08-09` | `docs/v6/FINAL_PROJECT_TECHNICAL_REPORT.md`; `docs/v6/NEGATIVE_RESULTS.md` | HIGH |
| V7 Kang2026 failure | `v7-research-final-2026-08-10` | `docs/v7/FINAL_PROJECT_TECHNICAL_REPORT.md`; `docs/v7/NEGATIVE_RESULTS.md` | HIGH |
| V8 double-pendulum Paper adaptation failure | `v8-research-final-2026-08-10` | `docs/v8/FINAL_TECHNICAL_REPORT.md`; `reproducibility/v8/final/claim_matrix.json` | HIGH |
| V9 predictor competence failure | `v9-research-final-2026-08-10` | `docs/v9/V9_FINAL_TECHNICAL_REPORT.md`; `reproducibility/v9/predictor/predictor_freeze.json`; `reproducibility/v9/final/final_gate.json` | HIGH |
| V10 external-paper route closure | `v10-research-final-2026-08-10` | `docs/v10/V10_FINAL_TECHNICAL_REPORT.md`; `reproducibility/v10/final/claim_matrix.json`; `reproducibility/v10/final/final_gate.json` | HIGH |
| Native platform and direct-wrench audit | `native-stack-benchmark-v1` / `native-stack-benchmark-v1.2-governance` | `docs/native_stack/P2_R0_FINAL_REPORT.md`; `docs/native_stack/CURRENT_CONTROL_STACK.md`; `docs/native_stack/CONTROL_INTERFACE_SPEC.md` | HIGH |
| Native Traditional qualification failure | end head `150d6c125b790563c94a48cdb596f06ee12ad102` | `docs/native_stack/r1r3/P2_R1R3_FINAL_REPORT.md`; `docs/native_stack/r1r3/TRADITIONAL_QUALIFICATION_FAILURE_BOUNDARY.md`; `reproducibility/native_stack/r1r3/final/final_gate.json` | HIGH |
| Native Holdout not executed | end head `150d6c125b790563c94a48cdb596f06ee12ad102` | `reproducibility/native_stack/r1r3/final/holdout_status.json`; `reproducibility/native_stack/r1r3/final/evidence_manifest.json` | HIGH |
| Heading interface block | commit `8ecf04d` / `release/p3-r1b-four-task-meeting-demo` | `docs/clean_release/P3_R1B_HEADING_EXTENSION_BLOCK.md`; `artifacts/meeting_demo/yaw_interface_audit.json`; `third_party/udaan/udaan/control/quadrotor/geometric_attitude.py` | HIGH |
| Extreme T1/T3 failure boundary | P3-R1D / commit `7c60ea6` | `outputs/meeting_demo_recoverable_v4/P3_R1D_CONTROL_LOSS_AUDIT.md`; `outputs/meeting_demo_extreme_v3/STRESS_ESCALATION.md`; `outputs/meeting_demo_recoverable_v4/T3/10mps/*/metrics.json` | HIGH |
| Recoverable envelope and common stable boundary | P3-R1E/P3-R1F / commits `35ca100`, `8d9768f` | `outputs/meeting_demo_recoverable_v4/WIND_REJECTION_ENVELOPE.md`; `outputs/meeting_demo_boundary_v5/FINAL_THREE_SCENARIO_METRICS.md`; `outputs/meeting_demo_boundary_v5/T2_CONTROLLER_BOUNDARY_GAP.md` | HIGH |
| Final Freeze controller/scenario identity | `research-final-freeze-2026-08-12` / `73d3dbcfbe9388deafb98999c1696fb18e8d7825` | `docs/clean_release/RESEARCH_FINAL_FREEZE_MANIFEST.md`; `docs/clean_release/FINAL_THREE_SCENARIO_CONTRACT.md`; `reproducibility/frozen/model/model_5link_controlled.xml` | HIGH |
| T1/T2/T3 final archived values | `research-final-freeze-2026-08-12` | `outputs/meeting_demo_boundary_v5/FINAL_THREE_SCENARIO_METRICS.md`; `docs/clean_release/FINAL_THREE_SCENARIO_CONTRACT.md` | HIGH |
| Old repository storage motivation | P3-R1H Freeze audit | `docs/clean_release/LOCAL_STORAGE_AUDIT.md` | HIGH |
| OLD vs CLEAN functional parity | parity commit `88a6edbf116e480a7f55ab5b051bccbafb9d1353` | `docs/MIGRATION_PARITY_REPORT.md`; `tools/verify_migration_parity.py`; `evidence/frozen/T3_ARCHIVED_BOUNDARY.json` | HIGH |
| Items not fully recovered | cross-audit of the above evidence | `docs/V4_FINAL_TECHNICAL_REPORT.md`; `outputs/meeting_demo_recoverable_v4/P3_R1D_CONTROL_LOSS_AUDIT.md`; `docs/clean_release/RESEARCH_FINAL_FREEZE_MANIFEST.md` | MEDIUM |

## Cross-check record

- V5 Holdout claim was read from both formal JSON and final report; no Holdout rerun was performed during this archive task.
- T1/T2/T3 values were checked against Freeze manifest and boundary metrics; T3 remains historical-only.
- Native negative result and Holdout lock were checked from `final_gate.json` and `holdout_status.json`; no Native extension was started.
- Heading status was checked from the machine-readable API audit and the vendored function signature; no third-party source was modified.
- Clean parity was reused as archived evidence: T1/T2 time-series max difference `0`, metrics max difference `0`, functional parity `PASS`.
