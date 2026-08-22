from __future__ import annotations

import json
from pathlib import Path

from scripts.verify_reproducibility import verify


ROOT = Path(__file__).resolve().parents[1]


def test_frozen_evidence_is_self_consistent() -> None:
    result = verify(ROOT)
    assert result["pass"] is True


def test_archived_boundary_is_not_presented_as_a_rerun() -> None:
    evidence = json.loads((ROOT / "reproducibility/benchmarks/t3_archived_boundary.json").read_text(encoding="utf-8"))
    assert evidence["rerun"] is False
    assert evidence["lqr_max_recoverable_mps"] == 3.0
    assert evidence["satc_max_recoverable_mps"] == 5.0
