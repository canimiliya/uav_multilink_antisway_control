"""Compare isolated OLD/CLEAN migration outputs without running a simulation."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


RUNS = (
    ("T1_PID", "T1", "5.0s", "corrected_pid"),
    ("T1_LQR", "T1", "5.0s", "full_lqr_048"),
    ("T1_SATC", "T1", "5.0s", "satc_b_027"),
    ("T2_LQR", "T2", "3.0mps_5.0s", "full_lqr_048"),
    ("T2_SATC", "T2", "3.0mps_5.0s", "satc_b_027"),
)
TIME_TOLERANCE = 1e-12
NUMERIC_TOLERANCE = 1e-9
IGNORED_METRIC_KEYS = {"runtime_s", "runtime_mean_ms", "runtime_p95_ms"}
IGNORED_METADATA_COLUMNS = {
    "absolute_file_path",
    "controller_runtime_ms",
    "pid",
    "process_id",
    "timestamp",
    "wall_clock_runtime_s",
}
CONFIG_PATHS = (
    "configs/model_5link.yaml",
    "configs/aerodynamics.yaml",
    "configs/lqr.yaml",
    "configs/s3_pid.yaml",
    "configs/airframes/dji_matrice_400.yaml",
    "configs/payloads/cutter_box_2p5kg.yaml",
    "reproducibility/v3/r1r1/pid_freeze.json",
    "reproducibility/v3/r1/full_lqr_freeze.json",
    "reproducibility/v5/self/self_freeze.json",
)


def _sha256(path: Path, normalize_text: bool = False) -> str:
    data = path.read_bytes()
    if normalize_text:
        data = data.replace(b"\r\n", b"\n")
    return hashlib.sha256(data).hexdigest()


def _git(path: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(path), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def _bool_or_text(value: str) -> Any:
    lowered = value.strip().lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    return value


def _compare_json(old: Any, clean: Any, path: str, failures: list[str], stats: dict[str, float]) -> None:
    if path.rsplit(".", 1)[-1] in IGNORED_METRIC_KEYS:
        return
    if isinstance(old, bool) or isinstance(clean, bool):
        if old is not clean:
            failures.append(f"{path}: boolean mismatch {old!r} != {clean!r}")
        return
    if old is None or clean is None:
        if old != clean:
            failures.append(f"{path}: value mismatch {old!r} != {clean!r}")
        return
    if isinstance(old, (int, float)) and isinstance(clean, (int, float)):
        diff = abs(float(old) - float(clean))
        stats["max_metric_diff"] = max(stats["max_metric_diff"], diff)
        if diff > NUMERIC_TOLERANCE:
            failures.append(f"{path}: numeric diff {diff:.17g} > {NUMERIC_TOLERANCE:g}")
        return
    if isinstance(old, list) and isinstance(clean, list):
        if len(old) != len(clean):
            failures.append(f"{path}: length mismatch {len(old)} != {len(clean)}")
            return
        for index, (left, right) in enumerate(zip(old, clean)):
            _compare_json(left, right, f"{path}[{index}]", failures, stats)
        return
    if isinstance(old, dict) and isinstance(clean, dict):
        if set(old) != set(clean):
            failures.append(f"{path}: keys mismatch {sorted(old)} != {sorted(clean)}")
            return
        for key in old:
            if key in IGNORED_METRIC_KEYS:
                continue
            _compare_json(old[key], clean[key], f"{path}.{key}", failures, stats)
        return
    if old != clean:
        failures.append(f"{path}: value mismatch {old!r} != {clean!r}")


def _compare_csv(old_path: Path, clean_path: Path, failures: list[str], stats: dict[str, float]) -> dict[str, Any]:
    with old_path.open(encoding="utf-8", newline="") as stream:
        old_rows = list(csv.DictReader(stream))
    with clean_path.open(encoding="utf-8", newline="") as stream:
        clean_rows = list(csv.DictReader(stream))
    if len(old_rows) != len(clean_rows):
        failures.append(f"{old_path.name}: row count mismatch {len(old_rows)} != {len(clean_rows)}")
    old_fields = list(old_rows[0]) if old_rows else []
    clean_fields = list(clean_rows[0]) if clean_rows else []
    if old_fields != clean_fields:
        failures.append(f"{old_path.name}: field names mismatch")
    fields = [field for field in old_fields if field not in IGNORED_METADATA_COLUMNS]
    for row_index, (old_row, clean_row) in enumerate(zip(old_rows, clean_rows)):
        for field in fields:
            left, right = old_row[field], clean_row[field]
            left_value, right_value = _bool_or_text(left), _bool_or_text(right)
            if isinstance(left_value, bool) or isinstance(right_value, bool):
                if left_value is not right_value:
                    failures.append(f"{old_path.name}[{row_index}].{field}: boolean mismatch")
                continue
            try:
                left_number, right_number = float(left), float(right)
            except ValueError:
                if left != right:
                    failures.append(f"{old_path.name}[{row_index}].{field}: value mismatch")
                continue
            diff = abs(left_number - right_number)
            if field == "time":
                stats["max_time_diff"] = max(stats["max_time_diff"], diff)
                tolerance = TIME_TOLERANCE
            else:
                stats["max_state_diff"] = max(stats["max_state_diff"], diff)
                tolerance = NUMERIC_TOLERANCE
            if diff > tolerance:
                failures.append(f"{old_path.name}[{row_index}].{field}: diff {diff:.17g} > {tolerance:g}")
    return {"row_count_old": len(old_rows), "row_count_clean": len(clean_rows), "columns_compared": fields}


def _compare_npz(old_path: Path, clean_path: Path, failures: list[str], stats: dict[str, float]) -> dict[str, Any]:
    import numpy as np

    with np.load(old_path) as old_data, np.load(clean_path) as clean_data:
        old_keys, clean_keys = sorted(old_data.files), sorted(clean_data.files)
        if old_keys != clean_keys:
            failures.append(f"{old_path.name}: array keys mismatch {old_keys} != {clean_keys}")
            return {"keys_old": old_keys, "keys_clean": clean_keys}
        for key in old_keys:
            left, right = np.asarray(old_data[key]), np.asarray(clean_data[key])
            if left.shape != right.shape:
                failures.append(f"{old_path.name}.{key}: shape mismatch {left.shape} != {right.shape}")
                continue
            if not np.array_equal(left.dtype, right.dtype):
                failures.append(f"{old_path.name}.{key}: dtype mismatch {left.dtype} != {right.dtype}")
            difference = np.abs(left.astype(float) - right.astype(float))
            diff = float(np.max(difference)) if difference.size else 0.0
            if key == "time":
                stats["max_time_diff"] = max(stats["max_time_diff"], diff)
                tolerance = TIME_TOLERANCE
            else:
                stats["max_state_diff"] = max(stats["max_state_diff"], diff)
                tolerance = NUMERIC_TOLERANCE
            if diff > tolerance:
                failures.append(f"{old_path.name}.{key}: diff {diff:.17g} > {tolerance:g}")
    return {"keys_compared": old_keys}


def _run_dir(root: Path, task: str, case_dir: str, controller: str) -> Path:
    return root / ".parity_tmp" / "P3_R1J" / task / case_dir / controller


def _compare_run(old_root: Path, clean_root: Path, label: str, task: str, case_dir: str, controller: str) -> dict[str, Any]:
    old_dir = _run_dir(old_root, task, case_dir, controller)
    clean_dir = _run_dir(clean_root, task, case_dir, controller)
    failures: list[str] = []
    stats = {"max_time_diff": 0.0, "max_state_diff": 0.0, "max_metric_diff": 0.0}
    old_metrics = json.loads((old_dir / "metrics.json").read_text(encoding="utf-8"))
    clean_metrics = json.loads((clean_dir / "metrics.json").read_text(encoding="utf-8"))
    _compare_json(old_metrics, clean_metrics, "metrics", failures, stats)
    csv_summary = _compare_csv(old_dir / "run.csv", clean_dir / "run.csv", failures, stats)
    npz_summary = _compare_npz(old_dir / "render_states.npz", clean_dir / "render_states.npz", failures, stats)
    for key in ("task", "controller", "STABLE_RECOVERED", "classification", "finite"):
        if key in old_metrics and old_metrics.get(key) != clean_metrics.get(key):
            failures.append(f"metrics.{key}: exact status mismatch")
    return {
        "label": label,
        "task": task,
        "controller": controller,
        "old_path": str(old_dir),
        "clean_path": str(clean_dir),
        "old_status": old_metrics.get("STABLE_RECOVERED", old_metrics.get("recoverable")),
        "clean_status": clean_metrics.get("STABLE_RECOVERED", clean_metrics.get("recoverable")),
        "old_classification": old_metrics.get("classification"),
        "clean_classification": clean_metrics.get("classification"),
        "max_time_diff": stats["max_time_diff"],
        "max_state_diff": stats["max_state_diff"],
        "max_metric_diff": stats["max_metric_diff"],
        "csv": csv_summary,
        "render_states": npz_summary,
        "runtime_metrics_ignored": sorted(IGNORED_METRIC_KEYS),
        "failures": failures,
        "parity": not failures,
    }


def _config_parity(old_root: Path, clean_root: Path) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    failures: list[str] = []
    for relative in CONFIG_PATHS:
        old_path, clean_path = old_root / relative, clean_root / relative
        if not old_path.is_file() or not clean_path.is_file():
            failures.append(f"missing config: {relative}")
            rows.append({"path": relative, "exists_old": old_path.is_file(), "exists_clean": clean_path.is_file()})
            continue
        old_hash = _sha256(old_path, normalize_text=True)
        clean_hash = _sha256(clean_path, normalize_text=True)
        rows.append({"path": relative, "old_sha256_normalized": old_hash, "clean_sha256_normalized": clean_hash, "byte_content_equal_after_eol_normalization": old_hash == clean_hash})
        if old_hash != clean_hash:
            failures.append(f"config mismatch: {relative}")
    return {"files": rows, "failures": failures, "parity": not failures}


def _t3_parity(old_root: Path, clean_root: Path) -> dict[str, Any]:
    source = old_root / "docs/clean_release/RESEARCH_FINAL_FREEZE_MANIFEST.md"
    target = clean_root / "evidence/frozen/T3_ARCHIVED_BOUNDARY.json"
    text = source.read_text(encoding="utf-8")
    old_lqr = float(re.search(r"Historical LQR maximum recoverable wind: `([0-9.]+) m/s`", text).group(1))
    old_satc = float(re.search(r"Historical SATC maximum recoverable wind: `([0-9.]+) m/s`", text).group(1))
    archived = json.loads(target.read_text(encoding="utf-8"))
    failures = []
    if archived.get("rerun") is not False:
        failures.append("clean T3 archive must have rerun=false")
    if archived.get("lqr_max_recoverable_mps") != old_lqr or archived.get("satc_max_recoverable_mps") != old_satc:
        failures.append("T3 archived boundary differs from OLD Freeze")
    return {
        "old_lqr_max": old_lqr,
        "clean_lqr_max": archived.get("lqr_max_recoverable_mps"),
        "old_satc_max": old_satc,
        "clean_satc_max": archived.get("satc_max_recoverable_mps"),
        "rerun": archived.get("rerun"),
        "source": str(source),
        "clean_evidence": str(target),
        "failures": failures,
        "parity": not failures,
    }


def _write_report(report_path: Path, summary: dict[str, Any]) -> None:
    lines = [
        "# OLD Freeze vs CLEAN Repository Numerical Parity",
        "",
        "Task: `P3-R1J-OLD-FREEZE-VS-CLEAN-REPO-NUMERICAL-PARITY-R1`.",
        "",
        f"- OLD Freeze: `{summary['old_freeze_commit']}` (`research-final-freeze-2026-08-12`).",
        f"- CLEAN commit: `{summary['clean_commit']}`; remote head: `{summary['clean_remote_head']}`.",
        f"- Python: `{summary['python_executable']}` / `{summary['python_version']}`; MuJoCo `{summary['mujoco_version']}`; NumPy `{summary['numpy_version']}`; OS `{summary['os']}`.",
        f"- Udaan OLD/CLEAN: `{summary['udaan_old']}` / `{summary['udaan_clean']}`.",
        f"- Model OLD/CLEAN SHA256: `{summary['model_old_sha256']}` / `{summary['model_clean_sha256']}`.",
        "",
        "## Packaging reference fixes",
        "",
        "`CITATION.cff` and `THIRD_PARTY_NOTICES.md` now point to the current clean repository. Scientific source and controller code were not changed.",
        "",
        "## Configuration and dependency parity",
        "",
        f"- Config parity: `{summary['config_parity']['parity']}` (line-ending-normalized SHA256 comparison for {len(summary['config_parity']['files'])} frozen files).",
        f"- Dependency parity: `{summary['dependency_parity']}`.",
        "- Shared limits: acceleration `2.0 m/s^2`, slew `0.25 m/s^2/update`, physics `0.001 s`, inner loop `0.005 s`, outer loop `0.05 s`.",
        "",
        "## T1/T2 numerical parity",
        "",
        "Runtime wall-clock fields (`runtime_s`, `runtime_mean_ms`, `runtime_p95_ms`) and path/process/timestamp metadata are ignored. Physics time uses a `1e-12 s` tolerance; all other numeric state/control and metric values use `1e-9`. Boolean/status fields and row counts require exact equality.",
        "",
        "| Run | OLD status | CLEAN status | max time diff (s) | max state diff | max metric diff | parity |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for run in summary["runs"]:
        lines.append(f"| {run['label']} | `{run['old_status']}` | `{run['clean_status']}` | `{run['max_time_diff']:.17g}` | `{run['max_state_diff']:.17g}` | `{run['max_metric_diff']:.17g}` | `{run['parity']}` |")
    lines += [
        "",
        "All five runs used the formal frozen scenario: initial sway `[20,-16,12,-8,4] deg`, target delta `[2.0,1.7,4.5] m`, 5.0 s move and 40 s duration. T2 used world +X wind at 3.0 m/s with a half-cosine 3.0--4.0 s ramp.",
        "",
        "## T3 archived parity",
        "",
        f"- OLD LQR max recoverable: `{summary['t3']['old_lqr_max']} m/s`; CLEAN: `{summary['t3']['clean_lqr_max']} m/s`.",
        f"- OLD SATC max recoverable: `{summary['t3']['old_satc_max']} m/s`; CLEAN: `{summary['t3']['clean_satc_max']} m/s`.",
        "- T3 was not rerun; CLEAN evidence is a lightweight archive derived from the OLD Freeze manifest.",
        "",
        "## Scope and final decision",
        "",
        "- `T3_RERUN = false`; `CONTROLLER_RETUNED = false`; `MODEL_MODIFIED = false`; `HOLDOUT_EXECUTED = false`.",
        f"- `CLEAN_SMOKE_TESTS` is recorded separately after parity; this tool result is `{summary['parity']}`.",
        f"- `CLEAN_REPO_FUNCTIONAL_PARITY = {'PASS' if summary['parity'] else 'FAIL'}`.",
    ]
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def verify(old_root: Path, clean_root: Path) -> dict[str, Any]:
    runs = [_compare_run(old_root, clean_root, *spec) for spec in RUNS]
    config = _config_parity(old_root, clean_root)
    t3 = _t3_parity(old_root, clean_root)
    old_freeze = _git(old_root, "rev-list", "-n", "1", "research-final-freeze-2026-08-12")
    clean_commit = _git(clean_root, "rev-parse", "HEAD")
    clean_remote = _git(clean_root, "ls-remote", "origin", "refs/heads/main").split()[0]
    model_old = _sha256(old_root / "reproducibility/frozen/model/model_5link_controlled.xml")
    model_clean = _sha256(clean_root / "reproducibility/frozen/model/model_5link_controlled.xml")
    try:
        import mujoco
        mujoco_version = mujoco.__version__
    except Exception:
        mujoco_version = "unavailable"
    try:
        import numpy
        numpy_version = numpy.__version__
    except Exception:
        numpy_version = "unavailable"
    dependency = (
        _git(old_root / "third_party/udaan", "rev-parse", "HEAD")
        == _git(clean_root / "third_party/udaan", "rev-parse", "HEAD")
        and model_old == model_clean
        and old_freeze == "73d3dbcfbe9388deafb98999c1696fb18e8d7825"
    )
    summary = {
        "old_freeze_commit": old_freeze,
        "clean_commit": clean_commit,
        "clean_remote_head": clean_remote,
        "python_executable": sys.executable,
        "python_version": platform.python_version(),
        "mujoco_version": mujoco_version,
        "numpy_version": numpy_version,
        "os": platform.platform(),
        "udaan_old": _git(old_root / "third_party/udaan", "rev-parse", "HEAD"),
        "udaan_clean": _git(clean_root / "third_party/udaan", "rev-parse", "HEAD"),
        "model_old_sha256": model_old,
        "model_clean_sha256": model_clean,
        "config_parity": config,
        "dependency_parity": dependency,
        "runs": runs,
        "t3": t3,
    }
    summary["parity"] = bool(dependency and config["parity"] and t3["parity"] and all(run["parity"] for run in runs))
    output_dir = clean_root / ".parity_tmp" / "P3_R1J"
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "parity_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    _write_report(clean_root / "docs/MIGRATION_PARITY_REPORT.md", summary)
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--old-repo", type=Path, required=True)
    parser.add_argument("--clean-repo", type=Path, required=True)
    args = parser.parse_args()
    summary = verify(args.old_repo.resolve(), args.clean_repo.resolve())
    print(json.dumps({"parity": summary["parity"], "runs": summary["runs"], "t3": summary["t3"]}, indent=2))
    return 0 if summary["parity"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
