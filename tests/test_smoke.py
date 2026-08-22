from __future__ import annotations

import hashlib
import json
from pathlib import Path

import mujoco


ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "reproducibility/model/model_5link_controlled.xml"
EXPECTED_MODEL_SHA256 = "19105873c0fcc891ebb85efe6c20c378d5b77b6bf9003559e43ae47ca03d153d"


def test_model_hash() -> None:
    digest = hashlib.sha256(MODEL.read_bytes()).hexdigest()
    assert digest == EXPECTED_MODEL_SHA256


def test_model_load() -> None:
    model = mujoco.MjModel.from_xml_path(str(MODEL))
    # One free UAV joint plus five suspended-link hinge joints.
    assert model.njnt == 6


def test_pid_import() -> None:
    from uav_sway.controllers.classical import V3CascadedTaskPID

    assert V3CascadedTaskPID.__name__ == "V3CascadedTaskPID"


def test_lqr_import() -> None:
    from uav_sway.controllers.classical import V3FullStateLQR

    assert V3FullStateLQR.__name__ == "V3FullStateLQR"


def test_satc_import() -> None:
    from uav_sway.controllers.satc_ofmpc import SATCOFMPC

    assert SATCOFMPC.__name__ == "SATCOFMPC"


def test_frozen_config_presence() -> None:
    required = [
        "configs/model_5link.yaml",
        "configs/airframes/dji_matrice_400.yaml",
        "configs/payloads/cutter_box_2p5kg.yaml",
        "configs/aerodynamics.yaml",
        "configs/s3_pid.yaml",
        "configs/lqr.yaml",
        "reproducibility/model/linear_model_audit.json",
        "reproducibility/model/task_metric_alignment_audit.json",
        "reproducibility/controllers/task_lqr_freeze.json",
        "reproducibility/controllers/full_lqr_freeze.json",
        "reproducibility/controllers/pid_freeze.json",
        "reproducibility/controllers/satc_ofmpc_freeze.json",
    ]
    for relative in required:
        path = ROOT / relative
        assert path.is_file(), relative
        if path.suffix == ".json":
            json.loads(path.read_text(encoding="utf-8"))


def test_frozen_runtime_configs_load() -> None:
    from uav_sway.disturbances.aerodynamics import load_aerodynamic_config
    from uav_sway.models.model_config import load_model_config

    model_config = load_model_config(ROOT / "configs/model_5link.yaml")
    aero_config = load_aerodynamic_config(ROOT / "configs/aerodynamics.yaml")
    assert model_config.n_links == 5
    assert model_config.payload.mass_kg == 2.5
    assert aero_config.wind_axis.tolist() == [1.0, 0.0, 0.0]


def test_udaan_import() -> None:
    from udaan.control.quadrotor import GeometricAttitudeController
    from udaan.manif import SO3, TSO3

    assert GeometricAttitudeController is not None
    assert SO3 is not None
    assert TSO3 is not None
