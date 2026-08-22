# Limitations

- This is simulation-only research software; there is no hardware or flight validation.
- Aerodynamic disturbances use a distributed approximation rather than a complete fluid model.
- The payload consists of passive planar rigid-link hinges.
- The controller observes causal state and the current reference; it does not receive wind truth or future reference samples.
- T3 is an archived wind-boundary record and was not rerun in the public cleanup.
- The results do not establish dynamic online replanning, learning-based control, PX4/ROS 2 integration, or real-world performance.
- Cutter orientation and heading control are not claimed as independently validated capabilities.
