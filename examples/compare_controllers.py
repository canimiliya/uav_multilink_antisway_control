"""Run the same short demonstration for all three frozen controllers."""

from __future__ import annotations

import argparse
import json

from uav_sway.demo.benchmark_runner import run_single


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--duration", type=float, default=12.0)
    args = parser.parse_args()
    results = {controller: run_single("task1_move", controller, args.duration) for controller in ("pid", "lqr", "satc")}
    print(json.dumps(results, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
