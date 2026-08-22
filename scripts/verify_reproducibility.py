"""Validate the public frozen model, evidence, and controller identities."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


EXPECTED_MODEL_SHA256 = "19105873c0fcc891ebb85efe6c20c378d5b77b6bf9003559e43ae47ca03d153d"
EXPECTED_UDAAN_COMMIT = "9eb1a2dcfe438ce7b4c4cd119072e4f3d8a6a816"


def verify(root: Path) -> dict[str, object]:
    manifest = json.loads((root / "reproducibility/manifest.json").read_text(encoding="utf-8"))
    model_path = root / manifest["model"]["path"]
    model_sha256 = hashlib.sha256(model_path.read_bytes()).hexdigest()
    udaan = root / "third_party/udaan"
    udaan_head = subprocess.run(
        ["git", "-C", str(udaan), "rev-parse", "HEAD"],
        check=False,
        capture_output=True,
        text=True,
    ).stdout.strip()
    checks = {
        "model_sha256": model_sha256 == EXPECTED_MODEL_SHA256 == manifest["model"]["sha256"],
        "udaan_commit": udaan_head == EXPECTED_UDAAN_COMMIT,
        "manifest": manifest["software_version"] == "1.0.0",
    }
    controller_paths = {
        "pid": "reproducibility/controllers/pid_freeze.json",
        "full_lqr": "reproducibility/controllers/full_lqr_freeze.json",
        "satc": "reproducibility/controllers/satc_ofmpc_freeze.json",
    }
    evidence = {}
    results: dict[str, object] = {}
    for name, relative in controller_paths.items():
        path = root / relative
        payload = json.loads(path.read_text(encoding="utf-8"))
        evidence[name] = {"path": relative, "exists": path.is_file(), "keys": sorted(payload)}
        if name == "pid":
            selected = payload["selected"]
            results[name] = {
                "safety_samples": selected["safe_sample_count"],
                "task_successes": selected["task_success_count"],
                "position_rmse_3d_m": selected["position_rmse_3d_m"],
                "orientation_rmse_deg": selected["orientation_rmse_deg"],
            }
        elif name == "full_lqr":
            selected = payload["selected"]
            results[name] = {
                "safety_samples": selected["safe_sample_count"],
                "task_successes": selected["task_success_count"],
                "position_rmse_3d_m": selected["position_rmse_3d_m"],
            }
        else:
            overall = payload["metrics"]["overall"]
            results[name] = {
                "safety_samples": overall["sample_count"],
                "task_successes": round(overall["success_rate"] * overall["sample_count"]),
                "position_mean_m": overall["position_mean_m"],
                "position_p90_m": overall["position_p90_m"],
                "orientation_mean_deg": overall["orientation_mean_deg"],
            }
    t3 = json.loads((root / "reproducibility/benchmarks/t3_archived_boundary.json").read_text(encoding="utf-8"))
    checks["t3_archived"] = t3["rerun"] is False
    checks["all_controller_evidence"] = all(item["exists"] for item in evidence.values())
    checks["udaan_pin"] = udaan_head == EXPECTED_UDAAN_COMMIT
    return {"pass": all(checks.values()), "checks": checks, "model_sha256": model_sha256, "udaan_head": udaan_head, "controllers": evidence, "results": results, "t3": t3}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    result = verify(parser.parse_args().root.resolve())
    print(json.dumps(result, indent=2))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
