"""Run one short, non-authoritative simulation using a frozen controller."""

from __future__ import annotations

import argparse
import json

from uav_sway.demo.benchmark_runner import run_single


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--controller", choices=("pid", "lqr", "satc"), default="pid")
    parser.add_argument("--duration", type=float, default=12.0, help="demo duration in seconds")
    args = parser.parse_args()
    metrics = run_single("task1_move", args.controller, args.duration)
    print(json.dumps({"controller": args.controller, "task": "T1 demo", "metrics": metrics}, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
