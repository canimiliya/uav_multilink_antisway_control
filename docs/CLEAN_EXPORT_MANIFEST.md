# Clean Export Manifest

Task: `P3-R1I-CLEAN-REPO-WHITELIST-BOOTSTRAP-AND-MINIMAL-EXPORT-R1`

## Provenance

| Field | Value |
|---|---|
| `SOURCE_REPOSITORY` | `D:\Desktop\my_project\uav_multilink_antisway_control_final` |
| `SOURCE_REMOTE` | `https://github.com/canimiliya/uav_multilink_antisway_control_final.git` |
| `SOURCE_FREEZE_TAG` | `research-final-freeze-2026-08-12` |
| `SOURCE_FREEZE_COMMIT` | `73d3dbcfbe9388deafb98999c1696fb18e8d7825` |
| `SOURCE_SCIENTIFIC_HEAD` | `d45e1ab7e1f340d138d870560d7915777b6ce2ef` |
| `NEW_REPOSITORY` | `D:\Desktop\my_project\uav-multilink-antisway-control` |
| `NEW_REMOTE` | `https://github.com/canimiliya/uav_multilink_antisway_control.git` |
| `NEW_BRANCH` | `main` |
| `SOURCE_FREEZE_VERIFIED` | `true` |
| `OLD_GIT_HISTORY_IMPORTED` | `false` |
| `LIVE_VIEWER_COPIED` | `false` |
| `VIDEOS_COPIED` | `false` |

The source Freeze was verified with `git rev-list -n 1 research-final-freeze-2026-08-12`, which returned the exact `SOURCE_FREEZE_COMMIT`. Scientific files below were materialized from that tag with `git archive`; they were not copied from the old working tree. `SHA256_OLD` means the SHA256 of the bytes emitted by that Windows `git archive` extraction, while `SHA256_NEW` is the clean-repository file hash.

## Frozen identities and dependency

| Item | Value |
|---|---|
| Model | `reproducibility/frozen/model/model_5link_controlled.xml` |
| `MODEL_SHA256` | `19105873c0fcc891ebb85efe6c20c378d5b77b6bf9003559e43ae47ca03d153d` |
| PID | `V3CascadedTaskPID` / `hybrid_x007_y041_z041` |
| Full-LQR | `V3FullStateLQR` / `full_lqr_048` |
| SATC | `SATC-OFMPC` / `satc_b_027` |
| `UDAAN_REMOTE` | `https://github.com/vkotaru/udaan.git` |
| `UDAAN_COMMIT` | `9eb1a2dcfe438ce7b4c4cd119072e4f3d8a6a816` |
| `UDAAN_IMPORT` | smoke-gated in `tests/clean_smoke/` |

## Freeze-derived files

| OLD_PATH | NEW_PATH | SHA256_OLD | SHA256_NEW | BYTE_IDENTICAL | WHY_REQUIRED |
|---|---|---|---|---|---|
| `.gitmodules` | `.gitmodules` | `e1094e9224eddef27deeb97dfff74d81ab6be3cd64eb112795176e26aad9d057` | `e1094e9224eddef27deeb97dfff74d81ab6be3cd64eb112795176e26aad9d057` | true | pinned Udaan submodule declaration |
| `LICENSE` | `LICENSE` | `5866c43749313b38e9a3e4ec31ec1a8e8fbad993874559d614d91db92c93f289` | `5866c43749313b38e9a3e4ec31ec1a8e8fbad993874559d614d91db92c93f289` | true | minimal clean-repo metadata or dependency packaging |
| `CITATION.cff` | `CITATION.cff` | `1e00e818eb8f9d7033fb8eb4a9ba3ad8497265fcc4fc26c8fe253b5c82bc448a` | `1e00e818eb8f9d7033fb8eb4a9ba3ad8497265fcc4fc26c8fe253b5c82bc448a` | true | minimal clean-repo metadata or dependency packaging |
| `THIRD_PARTY_NOTICES.md` | `THIRD_PARTY_NOTICES.md` | `5cf6d616c455ec11869711306f67455dbde15db478fab7eeae9410f29cc65826` | `5cf6d616c455ec11869711306f67455dbde15db478fab7eeae9410f29cc65826` | true | minimal clean-repo metadata or dependency packaging |
| `pyproject.toml` | `pyproject.toml` | `d76b20bcd50b6481194fd37a0c95936e56f2b9407fc1869926a4637da4c3913d` | `d76b20bcd50b6481194fd37a0c95936e56f2b9407fc1869926a4637da4c3913d` | true | minimal clean-repo metadata or dependency packaging |
| `requirements-lock.txt` | `requirements-lock.txt` | `ae050639873ea1750a5827157a51d3182da99707c9e3f3a4347249fab8329cc1` | `ae050639873ea1750a5827157a51d3182da99707c9e3f3a4347249fab8329cc1` | true | reproducible runtime dependency pins |
| `src/uav_sway/__init__.py` | `src/uav_sway/__init__.py` | `3da666098b6a214aebf44dceff477ff3b15d8424fad6fa08bd6f4082c0e6944f` | `3da666098b6a214aebf44dceff477ff3b15d8424fad6fa08bd6f4082c0e6944f` | true | package import boundary |
| `src/uav_sway/control/__init__.py` | `src/uav_sway/control/__init__.py` | `15e708570e560dba1cfedc957d113aae73dd16db6bbaaebbd197c1328a414a68` | `15e708570e560dba1cfedc957d113aae73dd16db6bbaaebbd197c1328a414a68` | true | required Udaan geometric inner-loop dependency |
| `src/uav_sway/control/base.py` | `src/uav_sway/control/base.py` | `aa02e85ec66e74906f4a4e755599a0138c30bf77b87822c9ea810fa77404cb74` | `aa02e85ec66e74906f4a4e755599a0138c30bf77b87822c9ea810fa77404cb74` | true | required Udaan geometric inner-loop dependency |
| `src/uav_sway/control/acceleration_limiter.py` | `src/uav_sway/control/acceleration_limiter.py` | `5e97a3816bc4e9c2fc70632556a17c58ac18d1397cb3b9c1218fdb4721d68d87` | `5e97a3816bc4e9c2fc70632556a17c58ac18d1397cb3b9c1218fdb4721d68d87` | true | transitive package-import dependency |
| `src/uav_sway/control/full_state_lqr.py` | `src/uav_sway/control/full_state_lqr.py` | `5e2665edde55f2e0b50d426af8dcbac50f78045b12eb3fd68c8ba39ce69799ec` | `5e2665edde55f2e0b50d426af8dcbac50f78045b12eb3fd68c8ba39ce69799ec` | true | transitive package-import dependency |
| `src/uav_sway/control/position_pid.py` | `src/uav_sway/control/position_pid.py` | `a9164adaac3dc3f57e20a66e321efad8c787303ef0005abec93f850dd3cc18a1` | `a9164adaac3dc3f57e20a66e321efad8c787303ef0005abec93f850dd3cc18a1` | true | transitive package-import dependency |
| `src/uav_sway/control/geometric_inner_loop.py` | `src/uav_sway/control/geometric_inner_loop.py` | `109f89c75c99358941ab023bff0b8bba1bdb3baa841209b9bad786fe261bae65` | `109f89c75c99358941ab023bff0b8bba1bdb3baa841209b9bad786fe261bae65` | true | required Udaan geometric inner-loop dependency |
| `src/uav_sway/demo/__init__.py` | `src/uav_sway/demo/__init__.py` | `b3063ac9250c1bc92b398fa3f8ea75b6cf105c3495ab0633b03e2aaa0c1e871c` | `b3063ac9250c1bc92b398fa3f8ea75b6cf105c3495ab0633b03e2aaa0c1e871c` | true | formal demo runner or MuJoCo Renderer entrypoint |
| `src/uav_sway/demo/meeting_runner.py` | `src/uav_sway/demo/meeting_runner.py` | `c1b7f4c85abcc8e2bfbaa35cb5930a6d423d663f5fa8175f290d786bcaaeb2a9` | `c1b7f4c85abcc8e2bfbaa35cb5930a6d423d663f5fa8175f290d786bcaaeb2a9` | true | formal demo runner or MuJoCo Renderer entrypoint |
| `src/uav_sway/demo/recoverable_runner.py` | `src/uav_sway/demo/recoverable_runner.py` | `824a047ecd781bb0c75bc6d4a0c422f585fe9228758614f31ffe59c7374c8abd` | `824a047ecd781bb0c75bc6d4a0c422f585fe9228758614f31ffe59c7374c8abd` | true | formal demo runner or MuJoCo Renderer entrypoint |
| `src/uav_sway/demo/visual_polish.py` | `src/uav_sway/demo/visual_polish.py` | `7fbb32ac5214f57c9b20abe63f3541e264d55277276b011467c781cf32b3fd34` | `7fbb32ac5214f57c9b20abe63f3541e264d55277276b011467c781cf32b3fd34` | true | formal demo runner or MuJoCo Renderer entrypoint |
| `src/uav_sway/disturbances/__init__.py` | `src/uav_sway/disturbances/__init__.py` | `db07e6695b51d24c65306035db1872d01fd38084ca04ce17a1b173a01815abfc` | `db07e6695b51d24c65306035db1872d01fd38084ca04ce17a1b173a01815abfc` | true | required wind/aerodynamic dependency |
| `src/uav_sway/disturbances/aerodynamics.py` | `src/uav_sway/disturbances/aerodynamics.py` | `c4af5a8f9472408d1a639357bc7b5ed086483cb5e3c87f7419d30fccb87493ce` | `c4af5a8f9472408d1a639357bc7b5ed086483cb5e3c87f7419d30fccb87493ce` | true | required wind/aerodynamic dependency |
| `src/uav_sway/disturbances/wind_applier.py` | `src/uav_sway/disturbances/wind_applier.py` | `35fea3fdf08e1f29a27a088fcc4d17b6ca4f64288f0933cee61806898477d370` | `35fea3fdf08e1f29a27a088fcc4d17b6ca4f64288f0933cee61806898477d370` | true | required wind/aerodynamic dependency |
| `src/uav_sway/disturbances/wind_io.py` | `src/uav_sway/disturbances/wind_io.py` | `6550dd26d2ebd330534ad54d0386dc80e43f711c0aef73ee670d3fc92526562c` | `6550dd26d2ebd330534ad54d0386dc80e43f711c0aef73ee670d3fc92526562c` | true | transitive package-import dependency |
| `src/uav_sway/disturbances/wind_profiles.py` | `src/uav_sway/disturbances/wind_profiles.py` | `deccd7a96d6cb12a0ba0e75aeba2e6bcde0aa3527225113ab38a4fab1d158772` | `deccd7a96d6cb12a0ba0e75aeba2e6bcde0aa3527225113ab38a4fab1d158772` | true | transitive package-import dependency |
| `src/uav_sway/models/__init__.py` | `src/uav_sway/models/__init__.py` | `831bfc8c2bd65188e1d4ca4c416daa97ad934133863de8db24063920ca43fbc2` | `831bfc8c2bd65188e1d4ca4c416daa97ad934133863de8db24063920ca43fbc2` | true | required model-config loader dependency |
| `src/uav_sway/models/model_config.py` | `src/uav_sway/models/model_config.py` | `96e5388379d91d2b0fff94d160fb1d165fb87b31268eabe5d0cf80828d5e0dd4` | `96e5388379d91d2b0fff94d160fb1d165fb87b31268eabe5d0cf80828d5e0dd4` | true | required model-config loader dependency |
| `src/uav_sway/mpc/__init__.py` | `src/uav_sway/mpc/__init__.py` | `e65b33adb270d495850cfc48cb1e38310881bb417c2abfd9e3d964ae8ff88f9d` | `e65b33adb270d495850cfc48cb1e38310881bb417c2abfd9e3d964ae8ff88f9d` | true | required OFMPC solver/QP dependency |
| `src/uav_sway/mpc/osqp_solver.py` | `src/uav_sway/mpc/osqp_solver.py` | `e0a01193ea40b6456692f21f09c5ef0be6db06840a46bf1786f7088169a9cef4` | `e0a01193ea40b6456692f21f09c5ef0be6db06840a46bf1786f7088169a9cef4` | true | required OFMPC solver/QP dependency |
| `src/uav_sway/mpc/qp_builder.py` | `src/uav_sway/mpc/qp_builder.py` | `329b324f263fc0f35ce7b9e1975236f947351a27d53174627e07d29908eacbfb` | `329b324f263fc0f35ce7b9e1975236f947351a27d53174627e07d29908eacbfb` | true | required OFMPC solver/QP dependency |
| `src/uav_sway/mpc/preview_model.py` | `src/uav_sway/mpc/preview_model.py` | `0af8fbd636fc8fa1b31d434fd80c9da3e7deea07ba65bc833a2c5f2af700c486` | `0af8fbd636fc8fa1b31d434fd80c9da3e7deea07ba65bc833a2c5f2af700c486` | true | transitive package-import dependency |
| `src/uav_sway/native_stack/__init__.py` | `src/uav_sway/native_stack/__init__.py` | `97e59d5412a87cc45d339f70aacf01ec8c20495eb9a0d6826d31ee3f85b7293d` | `97e59d5412a87cc45d339f70aacf01ec8c20495eb9a0d6826d31ee3f85b7293d` | true | required generic runtime bridge/sensor/actuator dependency |
| `src/uav_sway/native_stack/actuation.py` | `src/uav_sway/native_stack/actuation.py` | `23950cc2dee0817f94e76886301c243f9ba5e94892ff9fa9f6e0fe3c18cbf070` | `23950cc2dee0817f94e76886301c243f9ba5e94892ff9fa9f6e0fe3c18cbf070` | true | required generic runtime bridge/sensor/actuator dependency |
| `src/uav_sway/native_stack/api.py` | `src/uav_sway/native_stack/api.py` | `43dfa6b235b89e443fc12af4bff9d5fa88ba88e966f9f813fafa062592480ac3` | `43dfa6b235b89e443fc12af4bff9d5fa88ba88e966f9f813fafa062592480ac3` | true | required generic runtime bridge/sensor/actuator dependency |
| `src/uav_sway/native_stack/controller.py` | `src/uav_sway/native_stack/controller.py` | `16f06b3e6f36d4c690cff50c1f7ae9b1f82cb09e91c36391d086417dcc59b78f` | `16f06b3e6f36d4c690cff50c1f7ae9b1f82cb09e91c36391d086417dcc59b78f` | true | required generic runtime bridge/sensor/actuator dependency |
| `src/uav_sway/native_stack/r1r1_controllers.py` | `src/uav_sway/native_stack/r1r1_controllers.py` | `8ae414179e4cf53059425531a77e1becf58c3d73abcdc4f013d13ce44853454b` | `8ae414179e4cf53059425531a77e1becf58c3d73abcdc4f013d13ce44853454b` | true | required generic runtime bridge/sensor/actuator dependency |
| `src/uav_sway/native_stack/sensors.py` | `src/uav_sway/native_stack/sensors.py` | `1e42bee11fb61d3c504de0f7a6839589c5f924d52442d92988f139bdddaba284` | `1e42bee11fb61d3c504de0f7a6839589c5f924d52442d92988f139bdddaba284` | true | required generic runtime bridge/sensor/actuator dependency |
| `src/uav_sway/native_stack/case_semantics/__init__.py` | `src/uav_sway/native_stack/case_semantics/__init__.py` | `01e10e9c2547de228f866def89cc30781b452e43db512be84778f879eb78aa90` | `01e10e9c2547de228f866def89cc30781b452e43db512be84778f879eb78aa90` | true | transitive package-import dependency |
| `src/uav_sway/native_stack/case_semantics/authoritative.py` | `src/uav_sway/native_stack/case_semantics/authoritative.py` | `356bc6cc873a48e504b335089ee8b0aaabd91623204042d5e5a24a08adf8b77a` | `356bc6cc873a48e504b335089ee8b0aaabd91623204042d5e5a24a08adf8b77a` | true | transitive package-import dependency |
| `src/uav_sway/native_stack/case_semantics/resolver.py` | `src/uav_sway/native_stack/case_semantics/resolver.py` | `31d4ab9d5c39ad480f0dc3e08b82e9e93e162c85e0b8039a09d26fb236e47f67` | `31d4ab9d5c39ad480f0dc3e08b82e9e93e162c85e0b8039a09d26fb236e47f67` | true | transitive package-import dependency |
| `src/uav_sway/native_stack/logging.py` | `src/uav_sway/native_stack/logging.py` | `ea7b33380d182d0f3427c41b8da125631eaa8a6a20715eab2ef158123df84041` | `ea7b33380d182d0f3427c41b8da125631eaa8a6a20715eab2ef158123df84041` | true | transitive package-import dependency |
| `src/uav_sway/native_stack/references.py` | `src/uav_sway/native_stack/references.py` | `2b267e4f979d284acc57e49d8a99d38b8c6b7f59b771a552c5ecc5b14d54c517` | `2b267e4f979d284acc57e49d8a99d38b8c6b7f59b771a552c5ecc5b14d54c517` | true | transitive package-import dependency |
| `src/uav_sway/native_stack/runner.py` | `src/uav_sway/native_stack/runner.py` | `5bde93b7a815f2c26251e70bcdfd8dfea94560cd8e80cd6d5fd3944d2b419539` | `5bde93b7a815f2c26251e70bcdfd8dfea94560cd8e80cd6d5fd3944d2b419539` | true | transitive package-import dependency |
| `src/uav_sway/native_stack/safety.py` | `src/uav_sway/native_stack/safety.py` | `478ccfd81c9179a0b5936007496a258e04e4f62255b544e6bf8dbf451a2e47fe` | `478ccfd81c9179a0b5936007496a258e04e4f62255b544e6bf8dbf451a2e47fe` | true | transitive package-import dependency |
| `src/uav_sway/native_stack/scheduler.py` | `src/uav_sway/native_stack/scheduler.py` | `7c4b7a4f7583a6c35db58546b027b136456516b679cb0e2aecc5987839d73b79` | `7c4b7a4f7583a6c35db58546b027b136456516b679cb0e2aecc5987839d73b79` | true | transitive package-import dependency |
| `src/uav_sway/task_space/__init__.py` | `src/uav_sway/task_space/__init__.py` | `45b2cfc39dd5446d2ddd54821d3667fe708130fff0ba8f332413a780ea1541cc` | `45b2cfc39dd5446d2ddd54821d3667fe708130fff0ba8f332413a780ea1541cc` | true | required task-space state/reference dependency |
| `src/uav_sway/task_space/state.py` | `src/uav_sway/task_space/state.py` | `5bb492bd546691728b61e5538e61751e1deac941795d1361c3d60e94e351175f` | `5bb492bd546691728b61e5538e61751e1deac941795d1361c3d60e94e351175f` | true | required task-space state/reference dependency |
| `src/uav_sway/task_space/v2_reference.py` | `src/uav_sway/task_space/v2_reference.py` | `97bb414acb29fdcbbb79bb2c4e6c50f6d102c6243c3a7b656916913109496b7e` | `97bb414acb29fdcbbb79bb2c4e6c50f6d102c6243c3a7b656916913109496b7e` | true | required task-space state/reference dependency |
| `src/uav_sway/task_space/reference.py` | `src/uav_sway/task_space/reference.py` | `f58099a6e4493c3c1245cc2eb4742abcf9f00a1dbe7fe9781c09773af4a11755` | `f58099a6e4493c3c1245cc2eb4742abcf9f00a1dbe7fe9781c09773af4a11755` | true | transitive package-import dependency |
| `src/uav_sway/v3/__init__.py` | `src/uav_sway/v3/__init__.py` | `f9afc2f53b84ba38ef0b303ed4682ea80ff211a44d7ccf6cbb54ff4c34a3868f` | `f9afc2f53b84ba38ef0b303ed4682ea80ff211a44d7ccf6cbb54ff4c34a3868f` | true | package import boundary |
| `src/uav_sway/v3/contracts.py` | `src/uav_sway/v3/contracts.py` | `ccc87072fffbeadd710b16ae7845112257950025f60de21c000abba37577a175` | `ccc87072fffbeadd710b16ae7845112257950025f60de21c000abba37577a175` | true | direct V3 controller contract/observation dependency |
| `src/uav_sway/v3/controllers.py` | `src/uav_sway/v3/controllers.py` | `242e1283cf43e09bc3eda63396cb6305557eb56e39d0edfee34bf15befd86be9` | `242e1283cf43e09bc3eda63396cb6305557eb56e39d0edfee34bf15befd86be9` | true | formal PID and Full-LQR controller implementations |
| `src/uav_sway/v3/dr_tsrmpc.py` | `src/uav_sway/v3/dr_tsrmpc.py` | `1cabee6f817c69c12a3eb8f3d0cee92790ce2a094a9b097d5c049e8893743c8a` | `1cabee6f817c69c12a3eb8f3d0cee92790ce2a094a9b097d5c049e8893743c8a` | true | transitive V3/SATC controller dependency |
| `src/uav_sway/v3/metrics.py` | `src/uav_sway/v3/metrics.py` | `7955d841392e72b720978e6a921c951c623ffd6993f92ec50b1c50d42baa9e47` | `7955d841392e72b720978e6a921c951c623ffd6993f92ec50b1c50d42baa9e47` | true | transitive V3/SATC controller dependency |
| `src/uav_sway/v3/observation.py` | `src/uav_sway/v3/observation.py` | `9b78ace1a698db5ef344b2b73517bcc790e724b89a766b5230be36c11def3d16` | `9b78ace1a698db5ef344b2b73517bcc790e724b89a766b5230be36c11def3d16` | true | direct V3 controller contract/observation dependency |
| `src/uav_sway/v4/__init__.py` | `src/uav_sway/v4/__init__.py` | `b5d129dd555e40f161b2e8ef15733cac9398ae20134af12cd8cc7539d348328c` | `b5d129dd555e40f161b2e8ef15733cac9398ae20134af12cd8cc7539d348328c` | true | package import boundary |
| `src/uav_sway/v4/cart_ofmpc.py` | `src/uav_sway/v4/cart_ofmpc.py` | `9d0216cd3473e75be67802d56938dfbd4a106b2d6189c08415bcdc240d41b0da` | `9d0216cd3473e75be67802d56938dfbd4a106b2d6189c08415bcdc240d41b0da` | true | formal SATC OFMPC dependency |
| `src/uav_sway/v5/__init__.py` | `src/uav_sway/v5/__init__.py` | `e4bf2537721f61e057618cad75d36152e48c6bff3587c0726b1bc0dd1e1791de` | `e4bf2537721f61e057618cad75d36152e48c6bff3587c0726b1bc0dd1e1791de` | true | package import boundary |
| `src/uav_sway/v5/satc_ofmpc.py` | `src/uav_sway/v5/satc_ofmpc.py` | `ae58a9ba4ec13aceacd99e80bb7291ffba9f1b72accd988177e1182164d04546` | `ae58a9ba4ec13aceacd99e80bb7291ffba9f1b72accd988177e1182164d04546` | true | formal SATC OFMPC dependency |
| `configs/model_5link.yaml` | `configs/model_5link.yaml` | `0a42eeb88588fd621043ab3e17c644b7ed292faac58db92f65f017a42a6489aa` | `0a42eeb88588fd621043ab3e17c644b7ed292faac58db92f65f017a42a6489aa` | true | formal runtime configuration dependency |
| `configs/airframes/dji_matrice_400.yaml` | `configs/airframes/dji_matrice_400.yaml` | `48d2c15fbce52aeeb69524bb797dbbdd6d2b0712b99053a20d5e5f0c8f4acb2e` | `48d2c15fbce52aeeb69524bb797dbbdd6d2b0712b99053a20d5e5f0c8f4acb2e` | true | model config dependency |
| `configs/payloads/cutter_box_2p5kg.yaml` | `configs/payloads/cutter_box_2p5kg.yaml` | `9b2907a70b08478298499af6718c6688d4e5f41ddb90a899a6843439dce71331` | `9b2907a70b08478298499af6718c6688d4e5f41ddb90a899a6843439dce71331` | true | model config dependency |
| `configs/aerodynamics.yaml` | `configs/aerodynamics.yaml` | `6f601366d2bec58d7ff32551c0cc5a49f7a19f9a550ed20b56abaf367136bbfb` | `6f601366d2bec58d7ff32551c0cc5a49f7a19f9a550ed20b56abaf367136bbfb` | true | formal wind/aerodynamic model |
| `configs/s3_pid.yaml` | `configs/s3_pid.yaml` | `824f3d9de275beb8ac2b87af519d508c575850f17ad00007359a2228084037f6` | `824f3d9de275beb8ac2b87af519d508c575850f17ad00007359a2228084037f6` | true | frozen PID runtime rates/limits |
| `configs/lqr.yaml` | `configs/lqr.yaml` | `b205e3c829e4e5c8b4fe94d3d0327bc92a23aa862039a658ed60ad0d9bed08e8` | `b205e3c829e4e5c8b4fe94d3d0327bc92a23aa862039a658ed60ad0d9bed08e8` | true | frozen LQR runtime rates/limits |
| `reproducibility/frozen/model/model_5link_controlled.xml` | `reproducibility/frozen/model/model_5link_controlled.xml` | `19105873c0fcc891ebb85efe6c20c378d5b77b6bf9003559e43ae47ca03d153d` | `19105873c0fcc891ebb85efe6c20c378d5b77b6bf9003559e43ae47ca03d153d` | true | byte-frozen MuJoCo plant |
| `reproducibility/v3/r0/linear_model_audit.json` | `reproducibility/v3/r0/linear_model_audit.json` | `47e26957c833c51e086362136dd40d61d1c991caa6b46e9e8d9e8a810afa24e5` | `47e26957c833c51e086362136dd40d61d1c991caa6b46e9e8d9e8a810afa24e5` | true | transitive SATC linear-model evidence dependency |
| `reproducibility/v3/r1/task_metric_alignment_audit.json` | `reproducibility/v3/r1/task_metric_alignment_audit.json` | `ceeb273d746236ab584ad5f1088ba50db140d5a850eb31e1101273fc221f29c3` | `ceeb273d746236ab584ad5f1088ba50db140d5a850eb31e1101273fc221f29c3` | true | transitive SATC task-output evidence dependency |
| `reproducibility/v3/r1/task_lqr_freeze.json` | `reproducibility/v3/r1/task_lqr_freeze.json` | `c54c0b71cd588150694597152957f7e6444e32462a229a61f5169d418bc6348d` | `c54c0b71cd588150694597152957f7e6444e32462a229a61f5169d418bc6348d` | true | transitive SATC frozen backbone gain |
| `reproducibility/v3/r1/full_lqr_freeze.json` | `reproducibility/v3/r1/full_lqr_freeze.json` | `159959198453e40300ef216ed497d935c085a3ed946bea8c862631ef1e6b9e6c` | `159959198453e40300ef216ed497d935c085a3ed946bea8c862631ef1e6b9e6c` | true | Full-LQR frozen evidence and gain |
| `reproducibility/v3/r1r1/pid_freeze.json` | `reproducibility/v3/r1r1/pid_freeze.json` | `8b53d2c32d909bacdcf525bec1ff89726619a29cfc8efde91ecdbde968abc6b5` | `8b53d2c32d909bacdcf525bec1ff89726619a29cfc8efde91ecdbde968abc6b5` | true | PID frozen evidence and parameters |
| `reproducibility/v5/self/self_freeze.json` | `reproducibility/v5/self/self_freeze.json` | `4ca7e1a9d29d3d1215313e11bdb2d925ac35199bc50a5545c4e963cd01271d02` | `4ca7e1a9d29d3d1215313e11bdb2d925ac35199bc50a5545c4e963cd01271d02` | true | SATC frozen evidence and parameters |

Freeze-derived export count: `69` (50 source files plus 19 metadata/config/evidence files).

All 69 files are byte-identical to the corresponding files in the Windows `git archive` extraction. No scientific source file was edited or retuned.

## New clean-repository packaging files

These files are intentionally new and therefore have no `OLD_PATH` or byte-identical source counterpart:

| NEW_PATH | BYTE_IDENTICAL | WHY_REQUIRED |
|---|---|---|
| `README.md` | false | short project, object, controller, T1/T2/T3, provenance, and clean-export status |
| `.gitignore` | false | ignore generated outputs, caches, logs, and local VS Code settings |
| `tests/clean_smoke/test_clean_smoke.py` | false | minimal model/controller/config/Udaan integrity gate |
| `docs/CLEAN_EXPORT_MANIFEST.md` | false | export provenance, SHA256 audit, and whitelist record |

## Explicit exclusions

The new repository contains no copied old `.git/` directory and no imported old Git history. The following are intentionally excluded from this bootstrap:

- `reproducibility/v2/` run banks and historical candidate grids;
- V3--V10 development grids, benchmark history, Native-stack governance/history, Holdout outputs, and training banks;
- `outputs/`, `artifacts/`, `.benchmarks/`, caches, debug logs, raw CSV banks, old render states, MP4/GIF media;
- `scripts/meeting_demo/live_viewer.py` (`DO_NOT_COPY_LIVE_VIEWER_YET = true`);
- `.vscode/` local editor settings.

`NO_LARGE_HISTORY_DATA_COPIED = true`.

## Scope flags

```text
EXPORT_MODE = FREEZE_TAG_WHITELIST_ONLY
PARITY_EXECUTED = false
VIDEO_EXPORT = false
CONTROLLER_RETUNED = false
MODEL_MODIFIED = false
HOLDOUT_EXECUTED = false
OLD_REPO_FILES_DELETED = 0
```
