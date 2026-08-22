# Reproducibility

## Environment

- Python 3.11.x
- MuJoCo 3.0.1
- NumPy 2.4.6
- SciPy 1.17.1
- OSQP 1.1.3
- Udaan submodule at commit `9eb1a2dcfe438ce7b4c4cd119072e4f3d8a6a816`

The exact application dependencies and pytest are pinned in `requirements-lock.txt`. The byte-frozen MuJoCo model is `reproducibility/model/model_5link_controlled.xml`, with SHA256 `19105873c0fcc891ebb85efe6c20c378d5b77b6bf9003559e43ae47ca03d153d`.

## Install and test

```bash
git clone --recurse-submodules https://github.com/canimiliya/uav_multilink_antisway_control.git
cd uav_multilink_antisway_control
python -m pip install -r requirements-lock.txt
python -m pip install -e .
pytest -q
```

If the repository was cloned without submodules, initialize them with `git submodule update --init --recursive` before installing the lock file.

## Evidence check

```bash
python scripts/verify_reproducibility.py
```

This checks the model SHA256, Udaan commit, controller evidence files, software version, and the archived T3 boundary. It does not retune controllers or rerun the formal benchmark.

## Randomness and benchmark scope

The formal records use frozen controller parameters, model XML, benchmark scenarios, and controller identities. The clean public demo is a short runtime smoke demonstration; it should not be substituted for the formal benchmark records in `docs/RESULTS.md`.
