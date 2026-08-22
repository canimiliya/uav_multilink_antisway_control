# Results

The values below are read from the committed controller freeze records and the archived benchmark boundary. They are not newly tuned results.

## Frozen controller records

| Controller | Safety | Task success | Position metric | Orientation metric |
|---|---:|---:|---:|---:|
| PID (`hybrid_x007_y041_z041`) | 75/75 | 40/75 | 3-D RMSE: 0.232386 m | RMSE: 0.554671° |
| Full-State LQR (`full_lqr_048`) | 75/75 | 54/75 | 3-D RMSE: 0.088202 m | recorded in freeze evidence |
| SATC-OFMPC (`satc_b_027`) | 120/120 | 112/120 | mean: 0.097127 m; p90: 0.139230 m | mean: 0.703799° |

## Formal scenario status

The committed numerical comparison records the following status. T1 and T2 are recorded frozen comparisons; they are not rerun by the documentation cleanup. T3 is explicitly archived.

| Scenario | PID | Full-State LQR | SATC-OFMPC | Evidence status |
|---|---:|---:|---:|---|
| T1: nominal move | FAIL | PASS | PASS | recorded frozen comparison |
| T2: 3 m/s +X wind | not part of the retained comparison row | PASS | PASS | recorded frozen comparison |
| T3: wind boundary | — | max recoverable 3 m/s | max recoverable 5 m/s | archived boundary; not rerun |

T3 must not be interpreted as a fresh clean-repository experiment. Its record is retained because it is part of the scientific provenance.
