"""Shared frozen linear-system controllability helpers."""

from __future__ import annotations

import numpy as np


def controllability_basis(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Return the SVD basis used by the frozen linear-model audit."""
    a = np.asarray(a, dtype=float).reshape(20, 20)
    b = np.asarray(b, dtype=float).reshape(20, 3)
    matrix = np.column_stack([np.linalg.matrix_power(a, k) @ b for k in range(20)])
    u, _, _ = np.linalg.svd(matrix, full_matrices=False)
    # Match the rank convention used by the frozen linear-model audit.
    rank = int(np.linalg.matrix_rank(matrix, tol=1.0e-10))
    return u[:, :rank]
