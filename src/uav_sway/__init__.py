"""MuJoCo simulation and controllers for UAV multi-link anti-sway control."""

__version__ = "1.0.0"

CONTROLLER_IDENTITIES = {
    "pid": ("CascadedTaskPID", "hybrid_x007_y041_z041"),
    "full_lqr": ("FullStateLQR", "full_lqr_048"),
    "satc": ("SATC-OFMPC", "satc_b_027"),
}

__all__ = ["__version__", "CONTROLLER_IDENTITIES"]
