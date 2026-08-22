# Methods

All three controllers use the same MuJoCo model, disturbance definition, task-space output, control rates, and actuator limits.

| Method | Implementation | Frozen identity |
|---|---|---|
| PID | Cascaded task PID with equilibrium anchoring and bounded correction | `V3CascadedTaskPID` / `hybrid_x007_y041_z041` |
| Full-State LQR | Full-state linear feedback over UAV and five-link states | `V3FullStateLQR` / `full_lqr_048` |
| SATC-OFMPC | Causal task coordination around the frozen LQR backbone with constrained predictive correction | `SATC-OFMPC` / `satc_b_027` |

The controller observes UAV position and velocity, body attitude and angular velocity, five link angles and rates, cutter-tip task state, the current reference, and the previously applied physical command. The runtime does not pass future reference samples or wind truth into the controller.

The controller source remains in the historical implementation modules under `src/uav_sway/v3`, `src/uav_sway/v4`, and `src/uav_sway/v5`; their public identities are documented above so users do not need to infer the method from directory numbering.
