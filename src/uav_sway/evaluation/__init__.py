"""Evaluation and frozen-model audit helpers."""

from .metrics import (
    build_full_lqr_q,
    build_task_lqr_q,
    build_task_metric_alignment,
    load_linear_model_matrices,
    solve_discrete_lqr,
)

__all__ = [
    "build_full_lqr_q",
    "build_task_lqr_q",
    "build_task_metric_alignment",
    "load_linear_model_matrices",
    "solve_discrete_lqr",
]
