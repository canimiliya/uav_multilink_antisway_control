# OLD Freeze vs CLEAN Repository Numerical Parity

Task: `P3-R1J-OLD-FREEZE-VS-CLEAN-REPO-NUMERICAL-PARITY-R1`.

- OLD Freeze: `73d3dbcfbe9388deafb98999c1696fb18e8d7825` (`research-final-freeze-2026-08-12`).
- CLEAN commit: `98361f68f5d8105659a65a4942502ce169ddd60a`; remote head: `98361f68f5d8105659a65a4942502ce169ddd60a`.
- Python: `D:\anaconda\envs\uav_sway\python.exe` / `3.11.15`; MuJoCo `3.0.1`; NumPy `2.4.6`; OS `Windows-10-10.0.26100-SP0`.
- Udaan OLD/CLEAN: `9eb1a2dcfe438ce7b4c4cd119072e4f3d8a6a816` / `9eb1a2dcfe438ce7b4c4cd119072e4f3d8a6a816`.
- Model OLD/CLEAN SHA256: `19105873c0fcc891ebb85efe6c20c378d5b77b6bf9003559e43ae47ca03d153d` / `19105873c0fcc891ebb85efe6c20c378d5b77b6bf9003559e43ae47ca03d153d`.

## Packaging reference fixes

`CITATION.cff` and `THIRD_PARTY_NOTICES.md` now point to the current clean repository. Scientific source and controller code were not changed.

## Configuration and dependency parity

- Config parity: `True` (line-ending-normalized SHA256 comparison for 9 frozen files).
- Dependency parity: `True`.
- Shared limits: acceleration `2.0 m/s^2`, slew `0.25 m/s^2/update`, physics `0.001 s`, inner loop `0.005 s`, outer loop `0.05 s`.
- Controller identities: PID `V3CascadedTaskPID / hybrid_x007_y041_z041`, Full-LQR `V3FullStateLQR / full_lqr_048`, SATC `SATC-OFMPC / satc_b_027`.

## T1/T2 numerical parity

Runtime wall-clock fields (`runtime_s`, `runtime_mean_ms`, `runtime_p95_ms`) and path/process/timestamp metadata are ignored. Physics time uses a `1e-12 s` tolerance; all other numeric state/control and metric values use `1e-9`. Boolean/status fields, row counts, and `render_states.npz` keys/shapes/dtypes require exact equality; its `time` and `qpos` arrays are compared numerically.

| Run | OLD status | CLEAN status | max time diff (s) | max state diff | max metric diff | parity |
|---|---:|---:|---:|---:|---:|---:|
| T1_PID | `False` | `False` | `0` | `0` | `0` | `True` |
| T1_LQR | `True` | `True` | `0` | `0` | `0` | `True` |
| T1_SATC | `True` | `True` | `0` | `0` | `0` | `True` |
| T2_LQR | `True` | `True` | `0` | `0` | `0` | `True` |
| T2_SATC | `True` | `True` | `0` | `0` | `0` | `True` |

All five runs used the formal frozen scenario: initial sway `[20,-16,12,-8,4] deg`, target delta `[2.0,1.7,4.5] m`, 5.0 s move and 40 s duration. T2 used world +X wind at 3.0 m/s with a half-cosine 3.0--4.0 s ramp.

## T3 archived parity

- OLD LQR max recoverable: `3.0 m/s`; CLEAN: `3.0 m/s`.
- OLD SATC max recoverable: `5.0 m/s`; CLEAN: `5.0 m/s`.
- T3 was not rerun; CLEAN evidence is a lightweight archive derived from the OLD Freeze manifest.

## Scope and final decision

- `T3_RERUN = false`; `CONTROLLER_RETUNED = false`; `MODEL_MODIFIED = false`; `HOLDOUT_EXECUTED = false`.
- `CLEAN_SMOKE_TESTS = PASS` (`11 passed`: 8 clean smoke tests plus 3 parity unit tests).
- `CLEAN_REPO_FUNCTIONAL_PARITY = PASS`.
