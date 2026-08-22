# Research notes

The retained negative results explain the scope of the public claims:

- Direct tip-only PID caused safety failures when it ignored equilibrium mapping and the UAV anchor. The corrected cascaded PID is retained as a reproducible baseline, not as the strongest anti-wind method.
- Full-State LQR became the traditional comparator because it includes the UAV and five-link internal states in one fixed feedback law.
- Predictive residual variants improved selected metrics but did not establish a consistent acquisition advantage. SATC-OFMPC is retained with its frozen parameters and evidence rather than being retuned here.
- Failure boundaries are scientific evidence. They are not replaced by later short demos or presentation renders.
