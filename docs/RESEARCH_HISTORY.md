# UAV 多连杆抗摆控制：关键科研历史归档

本文件是从旧科研仓库恢复的“研究问题—尝试—失败—修正—关闭—最终方案”叙事，不是 Git 提交流水账。它只保留会改变研究结论的路线和证据；大体量 CSV、NPZ、视频、Native raw outputs、benchmark bank 和训练数据仍留在旧科研仓库，不在此迁移。

## 归档边界与阅读方法

- OLD 完整科研仓库：`D:\Desktop\my_project\uav_multilink_antisway_control_final`
- 科学 Freeze：tag `research-final-freeze-2026-08-12`，commit `73d3dbcfbe9388deafb98999c1696fb18e8d7825`
- Scientific base：`d45e1ab7e1f340d138d870560d7915777b6ce2ef`
- 本次归档的 CLEAN 起点：`98361f68f5d8105659a65a4942502ce169ddd60a`
- 数值 parity 归档提交：`88a6edbf116e480a7f55ab5b051bccbafb9d1353`

历史判断优先使用冻结 commit/tag、冻结 JSON/CSV/manifest、正式报告和 reproducibility evidence。文中把“证据直接写明的结论”和“根据多个证据归纳的解释”分开；解释若不是直接测量结果，会标为 inference。无法从旧仓库完整恢复的事项标为 `NOT FULLY RECOVERED`，不用记忆补写。

## 0. 项目最初要解决什么问题

### 为什么会做这件事

目标是让一个 6-DoF UAV 携带五个被动刚性连杆和约 2.5 kg cutter，在风扰下把 cutter tip 带到三维目标，同时抑制连杆摆动，并满足安全、速度和持续到达条件。难点不是“飞到一个点”本身，而是快速移动会激发多连杆柔性摆动，风又会对 UAV、连杆和 cutter 施加分布式扰动；位置、姿态、链摆和有限的加速度/变化率权限必须同时协调。

### 当时怎么定义问题

最早的正式 V2 契约把问题写成三类任务：无风三维 setpoint、固定/随机分布式风下的三维 setpoint，以及从零开始加风时保持平衡位置和 cutter 平衡方向。控制器只能看到当前因果状态和终点，不能读取未来风；正式输出是 world-frame cutter-tip position，任意全局姿态控制不在范围内。

### 最初结果与限制

早期公开基线曾把 LS-PMPC 作为主要验证方法，同时保留 PID、Full-State LQR 和 Task-LQR。早期 Task-LQR 在 calm 情况有改善，但 crosswind position 变差、acquisition 未达到，因此没有形成最终 robust task-space winner。这个早期公开结果不是当前 Freeze 的最终 claim；后续研究重新冻结了 corrected PID、Full-LQR 和 SATC。

### 关键证据

- tag `v1.0.0` / commit `62769122b6b75cd124c9cabc48aee2976a159f6b`
- `README.md`
- `docs/V2_RESEARCH_CONTRACT.md`
- `reproducibility/v2/task_contract.json`

## 1. 最早的控制思路：PID 与基础 benchmark

### 为什么先做 PID

PID 是最容易解释、实现和复现的传统起点，可以先回答“这个 plant、任务和安全定义是否能被一个经典闭环控制”。它也是后续高级方法必须面对的 baseline，而不是为了给新方法让出有利比较条件。

### 当时怎么做

早期基线包括 Cascaded PID/PD、Full-State LQR 和 Task-Space LQR，使用相同 plant、actuator limits、wind、sample bank、terminal gate 和 safety gate。V3 进一步保留了旧 PID 失败样本，重新设计 equilibrium-anchored cascaded relative-tip correction + UAV PID/PD，并把 derivative-on-measurement、bounded correction、正确的 saturation/slew-aware conditional integration 固定下来。

### 出现了什么问题

旧 direct-tip PID 在七个 development case 中重现了 attitude 或 tip-height safety failure。失败不是简单的“增益太小”：高增益直接围绕柔性五连杆 tip 做加速度闭环，却没有把 UAV 锚定到 equilibrium-mapped reference，向下或耦合对角目标会激发大幅 UAV/chain motion。另一个已确认问题是 anti-windup sign test 方向反了，使约束把积分推向更深饱和时仍接受积分。

### 后来怎么处理

旧 PID 作为负结果保留，不覆盖原证据；之后只在明确的 V3-R1R1 protocol 中做 targeted correction，并冻结 `V3CascadedTaskPID / hybrid_x007_y041_z041`。修正后的 PID 通过 V3 competence gate，但仍只是传统 baseline，不是最终抗风方法。

### 最终结论

`PARTIAL`: corrected PID 成为可比较、可复现的 baseline；旧 direct-tip PID 的失败成为后续设计约束，而不是被删除的“坏实验”。

### 留下的经验

多连杆系统里，tip error 不能脱离 equilibrium mapping、UAV anchor、saturation 和 slew 一起设计。安全通过和指标更好也必须分开报告。

### 关键证据

- tag `v3-research-final-2026-08-09`
- `reproducibility/v3/r1r1/r1_pid_failure_audit.json`
- `reproducibility/v3/r1r1/pid_competence_audit.json`
- `reproducibility/v3/r1r1/pid_freeze.json`
- `reproducibility/v3/r1r1/gate.json`
- `scripts/audit_v3_r1_pid_failures.py`

## 2. Full-LQR：为什么从 PID 转向完整状态

### 为什么要转向 Full-LQR

PID 主要按外部位置误差工作，难以直接协调 UAV 平动、姿态、五个连杆角度和速度。Full-State LQR 把完整冻结状态放进同一个线性反馈框架，使连杆内部模态和 UAV 状态不再被当作看不见的扰动。

### 当时怎么做

V3 冻结了 `V3FullStateLQR / full_lqr_048`，使用完整五连杆状态、固定 Q/R、共同 world-frame acceleration authority、幅值上限 `2.0 m/s^2`、外环周期 `0.05 s` 和 slew 上限 `0.25 m/s^2/update`。它随后成为 primary Traditional comparator。

### 出现了什么结果

在 V3 frozen Development 上，`full_lqr_048` 为 75/75 safety-valid、54/75 task-success，3-D position RMSE `0.0882018898 m`。相较于 corrected PID 的 `0.2323863569 m`，Full-LQR 成为更强的传统参考。后续 V5 Holdout 仍使用它作为固定 primary comparator。

### 后来怎么处理

Full-LQR 参数、实现和 comparator 身份被冻结，不因后续 SATC 或 Paper 路线的结果而 retune。Native-Stack 后来还把 native Full-LQR/LQI 单独在另一套治理协议下审计；那一结果不能倒写 V3/V5 的历史。

### 最终结论

`SUCCESS AS TRADITIONAL BASELINE`: Full-LQR 不是“最终新方法”，但它提供了最重要的传统强 baseline 和公平的 primary comparator。

### 关键证据

- tag `v3-research-final-2026-08-09`
- `reproducibility/v3/r1/full_lqr_freeze.json`
- `reproducibility/v3/r1/primary_traditional_baseline.json`
- `reproducibility/v3/r1r1/gate.json`

## 3. 中间控制器探索：从 residual compensation 到 SATC

下面只保留改变研究方向的尝试，不把每个 candidate ID 机械罗列出来。

### 3.1 OF-TSRMPC 与 DR-TSRMPC

#### 为什么尝试

LQR 能稳定名义状态，但风扰和模型残差会造成 steady-state error；因此先尝试 offset-free 和 disturbance-rejection 结构，希望在任务空间中估计并补偿未知扰动。

#### 实际怎么做

OF-TSRMPC 使用任务空间预测、residual/offset compensation 和 QP；DR-TSRMPC 继续使用 causal residual、bounded correction 和 constraints，并在同一冻结 benchmark 上与传统 baseline 配对比较。

#### 问题与根因

OF-TSRMPC 的 residual 实际对应 output-equation mismatch，而不是完整的未建模 state-dynamics residual。beta 从 `0.05`、`0.15` 到 `0.30` 时 success 完全不变，核心指标相对变化低于 1%，说明调这个参数不能改变结构性限制。它相对 Task-LQR 的 position、ramp 和 acquisition 优势很小，且整体 Development eligibility 未成立。

DR-TSRMPC 在 Development 上确实改善了 success、3-D position 和 ramp rejection，但 acquisition gate 没有改善；正式 paired acquisition 结果没有形成正的总体优势。因此这是有价值的 `CLOSED_PARTIAL_SCIENTIFIC_SUCCESS`，不是 Advanced > Traditional。

#### 后来怎么处理

OF 路线关闭；DR 的 residual、QP、约束和 failure evidence 被保留，并作为后续 Self/SATC 的工程材料。没有通过放宽 gate、重用 Holdout 或扩大 candidate budget 来把 partial result 改成 winner。

#### 关键证据

- tag `v2-research-final-2026-08-09`
- `reproducibility/v2/r3r1/of_tsrmpc_failure_mechanism.json`
- `reproducibility/v2/r3r2/paired_traditional_comparison.json`
- `docs/V2_FINAL_TECHNICAL_REPORT.md`
- `docs/V2_FINAL_CLAIM_MATRIX.md`

### 3.2 V3 Self：3D-DR-TSRMPC

#### 为什么尝试

V2 暴露了输出残差与真实多连杆状态之间的差距，因此 V3 把 Self 路线扩展到冻结 20D error state，加入 causal bounded residual、steady compensation 和 constrained linear QP。

#### 实际怎么做

先在 14-case frozen Development core 上筛选，再把前六名放到完整 75-case Development；selected candidate 是 `self_a_034`，backbone 为 `task_lqr_009`。它没有读 future wind、future target、fallback、Traditional override 或 Holdout。

#### 失败与原因

V3 Holdout 的正式结论是 `V3_SELF_DEVELOPMENT_WIN_NOT_CONFIRMED_ON_HOLDOUT`。失败集中在新 constant-3.5 m/s cohort：12 个 paired cases 全部 favor Full-LQR，Self 平均 position RMSE `0.711379 m`，Full-LQR `0.212308 m`，且两者都没有 acquisition。其它 calm、2.0 m/s、stochastic 和 ramp cohort 中 Self 可以更好，但 aggregate gate 和 bootstrap 仍失败。

#### 后来怎么处理

不重调 Self、不进行第二次 V3 Holdout；把“某些 cohort 有效、强风 tail 不足”作为下一轮机制设计的输入。

#### 最终结论

`NEGATIVE RESULT`: Self 证明了 residual/QP 方向有局部价值，但没有证明在冻结 Holdout 上是可靠的总体方法。

#### 关键证据

- tag `v3-research-final-2026-08-09`
- `docs/V3_FINAL_TECHNICAL_REPORT.md`
- `reproducibility/v3/r2/self_architecture_history.json`
- `reproducibility/v3/r2/self_search_history.json`
- `reproducibility/v3/r4/holdout_results.csv`

### 3.3 V3 Paper adaptation

#### 为什么尝试

为了检验“近期 Paper 方法是否能超过传统 baseline”，V3 选择了有完整公开方程、能映射到共同三轴 acceleration interface 的 LV2026-SPACC 路线。

#### 实际怎么做

先冻结 Paper source、适配协议、搜索预算和 14-case/75-case Development 顺序，再执行不扩展的 candidate search。

#### 问题与关闭

最好的 `paper_a_001` safety 和 success 通过，但 position RMSE `0.0848384751 m` 超过 immutable contract 的 position limit `0.0837918 m`，acquisition `5.23 s` 也超限；因此不是 Development-qualified candidate。Paper 没有进入 Holdout，也没有通过换 Paper 或加参数来挽救。

#### 最终结论

`NEGATIVE RESULT / DEVELOPMENT-INELIGIBLE`: 这是五连杆共同接口下的 adaptation 结果，不是否定原论文在原平台上的方法。

#### 关键证据

- `reproducibility/v3/r3/paper_selection.json`
- `reproducibility/v3/r3/paper_search_history.json`
- `reproducibility/v3/r3/near_miss.json`
- `docs/V3_FINAL_TECHNICAL_REPORT.md`

## 4. V4 CART-OFMPC：第一次明确修机制

### 为什么会做这个阶段

V3 的 postmortem 指向持续强风下的 residual clipping、amplitude/slew 限制和 steady equilibrium infeasibility。V4 不再只换增益，而是试图让控制器知道“请求的平衡输入是否物理可行”，并显式管理 residual trust、anti-windup 和 slew。

### 当时怎么做

CART-OFMPC 引入 constraint-feasible steady target、causal one-step residual estimator、bounded steady-target active-set QP、residual trust、bounded anti-windup debt，以及直接约束 physical acceleration 和 slew 的 finite-horizon task-space QP。

### 出现了什么问题

它确实打断了 V3 的 persistent-equilibrium amplification chain：best near-miss 中 residual clipping 约 `3.53%`，slew activity `9.71%`，远低于旧机制的约 `69.74%` 和 `62.55%`；overall position 比 Full-LQR 改善 `19.88%`。但 strong success 只有 `10.81%`，strong position P90 比 Full-LQR 差 `94.04%`，并有 7 个 catastrophic simultaneous-onset pairs。所有 18 个 full-bank Stage-B candidates 都没通过 tail gates。

已确认的机制是：negative-x target 与 fixed +x wind 构成明确的方向分区，catastrophic 区域伴随低 trust、高 correction 和高 slew。更细的 onset-time/vector-angle 解释因 R1 没有保存 time-series，只能标为 hypothesis。

### 后来怎么处理

CART 只得到 mechanism improvement，不冻结 candidate；V4 Holdout 不执行，不用 Holdout 反救；建议进入新 research version，重点处理 abrupt simultaneous onset。

### 最终结论

`CLOSED_WITH_MECHANISM_IMPROVEMENT_BUT_NO_QUALIFIED_SELF`。

### 关键证据

- tag `v4-research-final-2026-08-09`
- `docs/V4_CART_OFMPC_DEVELOPMENT_REPORT.md`
- `docs/V4_FINAL_TECHNICAL_REPORT.md`
- `reproducibility/v4/r0/failure_mechanism_report.json`
- `reproducibility/v4/r0/v3_failure_postmortem.json`

## 5. SATC-OFMPC 是怎样一步一步形成的

### 为什么 SATC 会出现

SATC 不是凭空设计出来的。它是在 V3 的 constant-3.5 m/s failure、V4 的 simultaneous-onset tail failure 和已经验证有效的 Full-LQR/CART 组件之后，针对“扰动 shock、offset、物理约束和传统 backbone 相互冲突”这个具体问题形成的。

### 形成过程

1. **继承可用基础**：保留 CART 的 constraint-feasible offset model、bounded residual compensation、task-LQR backbone 和 physical acceleration/slew constraints。
2. **处理 shock**：加入 causal shock detection，用 reference shock 和 innovation shock 识别“目标突然变化”和“扰动突然变化”不是同一件事。
3. **避免切换冲击**：加入 rate-limited/bumpless offset engagement，使 offset 不会在一个更新中突然接管。
4. **处理控制器冲突**：加入 final physical-input coordination、geometric disturbance-task conflict index、cancellation 和 robust LQR blending；目标是检测 backbone 要求与扰动补偿方向互相抵消的时刻。
5. **保留物理余量**：加入 slew reserve/headroom 与 bounded debt/anti-windup，避免补偿把可用控制余量全部耗尽。
6. **冻结而不追溯调参**：V5 在 Development 上用预注册 budget 筛选 36 个 full-bank candidates，3 个通过 20/20 gates，并在独立 Stage C 重复；最终冻结 `SATC-OFMPC / satc_b_027`。post-freeze ablation 只解释机制，不反过来选参数。

### 实际结果

V5 Development 的 `satc_b_027` position RMSE `0.097127 m`、success `93.33%`、strong P90 `0.144855 m`、zero catastrophic pairs。随后在一次性 96-case Holdout 上，它保持 100% safety、55.21% success、position RMSE `0.0968265310 m`；相对 Full-LQR 的 position improvement 是 `29.10%`，paired-bootstrap 95% CI 为 `[0.033754, 0.045756] m`，directional tail gates 全部通过且 catastrophic pairs 为 0。

### 为什么最后冻结成现在的方案

它是唯一一条同时留下了可解释 failure closure、Development qualification、unseen Holdout Overall win 和可复现实验边界的 self-developed 路线。它不是 Strict all-metric winner：normal-regime acquisition 相对 legacy `self_a_034` 变差 `11.27%`，超过预注册的 `10%` 上限；所以最高 claim 只能是 `V5_SELF_OVERALL_HOLDOUT_WIN`，不能写 `STRICT_ALL_METRIC_WIN`。

### 最终结论

`SUCCESS WITH EXPLICIT SCOPE`: SATC 是当前冻结方案，但结论限于冻结 MuJoCo 五连杆 benchmark 的 Overall Holdout，不延伸到原论文 superiority、硬件、真实飞行或 Strict 全指标胜出。

### 关键证据

- tag `v5-research-final-2026-08-09`
- `docs/V5_FINAL_TECHNICAL_REPORT.md`
- `docs/v6/METHOD_EVOLUTION.md`
- `reproducibility/v5/final/mechanism_summary.json`
- `reproducibility/v5/self/mechanism_report.json`
- `reproducibility/v5/final/metric_summary.json`
- `reproducibility/v5/final/claim_matrix.json`
- `reproducibility/v5/holdout/gate.json`
- `reproducibility/v5/holdout/self_vs_primary.json`

## 6. 后续 Paper 路线为什么陆续关闭

这些路线不改变 SATC 的 Freeze；它们说明为什么最终没有继续替换传统 baseline 或 SATC。

### V6：Yu 2026 与 SEP-NMPC

Yu 最佳候选 `yu_b_007` 只有 `40.83%` safety、`0%` success、position RMSE `5.6509 m`；SEP 最佳 `sep_b_002` 虽有 `100%` safety，但 success `1.67%`、position RMSE `0.4564 m`，并有 54 个 strong catastrophic pairs。两者都未 Development qualify，所以 V6 Holdout 未执行。

### V7：Kang2026 FAS-DOB

`kang_b_001` safety `100%`，但 success `0.69%`、position RMSE `0.37311 m`，相对 Full-LQR `0.14703 m` 明显更差；144 个 paired position deltas 全部 favor Full-LQR，candidate 只过 `2/7` gates。V7 Holdout 保持锁定。

### V8：Xu2025 CBS-FTDO

modal reduction 的 small-signal parity 通过，但 closed-loop qualification 失败；诊断候选 `xu_v8_077` safety `47.92%`、success `0.69%`、position RMSE `2.1982 m`，72 个 strong catastrophic pairs。这个阶段说明“小信号等价”不能替代闭环资格。

### V9：Neural Predictor

官方方法的 loading、训练 smoke、wrapper 和数值评估都能运行，但 frozen validation competence gate 不通过。`np_v9_14` 的 force RMSE `0.87555`、torque RMSE `0.19361`、all-channel RMSE `0.89670`，没有同时达到 force/torque 各至少 5% 优于 simple estimator 的要求；因此没有 NP-MPC controller、没有 Development/ Holdout performance。

### V10：FxTDO-MPC

最终 Paper 路线的 `fxtdo_v10_020` safety 为 `100%`，但 success `0%`、position mean `15.445775 m`，72 个 strong cases 全部 catastrophic，只过 `2/9` gates。可能机制是有限 horizon correction 对冻结离散模型的 authority/scale 不足，且 fixed-time settling 没有被验证；这是证据支持的诊断，不是 retune 授权。

### 共同处理原则

每条 Paper 路线都在 Development gate 失败处停止，不把原论文在其原平台的效果写成失败，也不打开对应 Holdout。V10 之后正式关闭 external-paper route：`NO_V11`，不自动再换一篇论文。

### 关键证据

- tags `v6-research-final-2026-08-09`、`v7-research-final-2026-08-10`、`v8-research-final-2026-08-10`、`v9-research-final-2026-08-10`、`v10-research-final-2026-08-10`
- `docs/v6/FINAL_PROJECT_TECHNICAL_REPORT.md`
- `docs/v6/NEGATIVE_RESULTS.md`
- `docs/v7/FINAL_PROJECT_TECHNICAL_REPORT.md`
- `docs/v8/FINAL_TECHNICAL_REPORT.md`
- `docs/v9/V9_FINAL_TECHNICAL_REPORT.md`
- `docs/v10/V10_FINAL_TECHNICAL_REPORT.md`
- `reproducibility/v10/final/claim_matrix.json`

## 7. Native-Stack 路线：为什么启动、做到了什么、为什么关闭

### 为什么启动 Native-Stack

这条路线不是为了给 SATC 再造一个有利 benchmark，而是为了回答一个边界问题：在明确的 physical direct-wrench、sensor envelope、multirate scheduler 和 Governance-v2 资格门槛下，传统 PID/LQI 是否仍然 competent。它同时审计了旧 formal runner 是否真的使用了冻结的物理执行路径。

### 做到了什么

Native v1 审计冻结了 MuJoCo model、direct body-z thrust + body torque path、1000 Hz physics、200 Hz inner/wind 和 20 Hz outer scheduler；旧路径与 physical wrench 在确定性输入上通过 parity。Native Development 是 200 cases，Holdout 是 140 cases，但 Holdout `execution_allowed=false`、authoritative runs `0`。

### 为什么失败

在 Governance-v2 的 200-case Development 中，最好的 native PID 和 Full-LQR/LQI 都是 100% safety、0 catastrophic，但 nominal success 只有 `0.470` 和 `0.520`，moderate-wind success 只有 `0.147` 和 `0.0588`，低于 `0.70` nominal 和 `0.50` moderate gate。失败属于冻结资格门槛下的传统控制性能失败，不是 benchmark、plant、runner 或治理协议 bug。

### 后来怎么处理

正式结果是 `P2_GOVERNANCE_V2_TRADITIONAL_QUALIFICATION_FAILED`；`COMPETENT_TRADITIONAL_COUNT=0`，因此没有执行 SATC search、Paper search 或 Holdout。Native extension 状态关闭为 `CLOSED_NEGATIVE_RESULT`。没有用旧 R1R1/R1R2 结果覆盖本轮失败，也没有把未执行路线写成负性能结果。

### 为什么决定停止而不是无限救援

继续追加配置会把“冻结资格失败”变成事后扩大预算，破坏 preregistered gate；同时，当前路线已经完成了平台、runner、scheduler、物理接口和控制器资格边界的审计。是否开启全新授权路线应由 owner 决定，而不是由本归档自动启动。

### 最终结论

`P2_GOVERNANCE_V2_TRADITIONAL_QUALIFICATION_FAILED`；Native 研究 extension `CLOSED_NEGATIVE_RESULT`。

### 关键证据

- Native end head：`150d6c125b790563c94a48cdb596f06ee12ad102`
- source tag `native-stack-benchmark-v1.2-governance`
- `docs/native_stack/r1r3/P2_R1R3_FINAL_REPORT.md`
- `docs/native_stack/r1r3/TRADITIONAL_QUALIFICATION_FAILURE_BOUNDARY.md`
- `reproducibility/native_stack/r1r3/final/final_gate.json`
- `reproducibility/native_stack/r1r3/final/holdout_status.json`
- `docs/native_stack/P2_R0_FINAL_REPORT.md`

## 8. Heading / cutter orientation 路线为什么关闭

### 为什么曾经检查 Heading

项目曾希望把“cutter XYZ + cutter heading”升级为更完整的演示或控制能力。但在把它写入主线任务前，必须先确认底层 Udaan attitude API 是否真的提供独立 yaw/heading channel。

### 实际发现

审计得到的接口是：

```text
compute(t, state, thrust_force, desired_att=None)
```

其中第一个运行参数 `t` 是 time，不是 yaw；实现主要从 `thrust_force` 推导 desired attitude。虽然签名存在 `desired_att`，审计没有建立一个可独立控制、可验证的 cutter heading 通道。

### 最终状态

```text
CUTTER XYZ: SUPPORTED
CUTTER ORIENTATION: MEASURED_BUT_NOT_INDEPENDENTLY_CONTROLLED
FULL 6DOF POSE: NOT SUPPORTED
HEADING: NOT_VERIFIED
```

因此 P0 interface gate 阻断，未创建 wrapper、heading preset、Task-4 run 或新动画；没有修改 Udaan、模型、控制器或参数。这个结果只说明当前接口不支持已验证的 heading claim，不说明模型永远不能增加 heading 能力。

### 最终结论

`BLOCKED_AT_INTERFACE / NOT_VERIFIED`。

### 关键证据

- commit `8ecf04d` / branch `release/p3-r1b-four-task-meeting-demo`
- `docs/clean_release/P3_R1B_HEADING_EXTENSION_BLOCK.md`
- `artifacts/meeting_demo/yaw_interface_audit.json`
- `third_party/udaan/udaan/control/quadrotor/geometric_attitude.py`

## 9. 极限场景失败：为什么必须保留

### T1：4 s aggressive transition

四秒快速移动把大初始摆动和快速 reference transition 叠加到一起。旧 boundary evidence 的结论是：LQR 进入 `TASK_CONTROL_LOST`，SATC 进入 `SAFETY_FAILURE`；SATC 记录了历史 height violations。它不是“展示失败”，而是告诉我们从 4 s 往上搜索 common recoverable envelope 时，安全和恢复能力必须同时检查。

### T3：10 m/s wind

在 world +X 方向的 10 m/s 风下，LQR 和 SATC 都是 `DISTURBANCE_OVERWHELMED_BOTH`。冻结空气动力包含 speed-squared drag，因此 10 m/s 的 quadratic drag 项约为 5 m/s 的四倍；这个场景明确超出当前任务控制能力，不能作为 successful demo 或 Holdout claim。

### 失败的科研价值

这些失败帮助定位了合理的可恢复包络：它们说明系统在什么地方会失去控制、为什么要把“有压力的 stress demo”和“可公开的 common-stable demo”分开。失败边界本身是科研结果，不是无效工作。

### 关键证据

- `outputs/meeting_demo_recoverable_v4/P3_R1D_CONTROL_LOSS_AUDIT.md`
- `outputs/meeting_demo_extreme_v3/STRESS_ESCALATION.md`
- `docs/clean_release/EXTREME_WIND_CONTEXT.md`
- `outputs/meeting_demo_recoverable_v4/T3/10mps/*/metrics.json`

## 10. Recoverable Envelope：从过激场景回到公平场景

### 搜索得到的边界

- T1：6 s stable、4 s fail，搜索后选择共同 `5 s`。
- T2：移动任务中 5 m/s 过强，搜索后选择共同 `3 m/s world +X`。
- T3：历史 archived boundary 为 LQR `3 m/s`、SATC `5 m/s`；T3 不在本次 Freeze/迁移中重跑。

### 为什么主展示必须用 COMMON_STABLE

T1 和 T2 的主比较要求两种核心 controller 都在同一条件下 stable；否则只展示 SATC 能撑住而 LQR 已失败的 scenario，会把 controller capability boundary 和公平比较混在一起。最终 public showcase 因此使用 common `5 s`、common `3 m/s`，而把 SATC-only 或双方都失败的极限场景保留为历史边界。

### 关键证据

- tag `v3-research-final-2026-08-09`、`v5-research-final-2026-08-09`
- commits `7c60ea6`、`35ca100`、`8d9768f`
- `outputs/meeting_demo_recoverable_v4/WIND_REJECTION_ENVELOPE.md`
- `outputs/meeting_demo_boundary_v5/FINAL_THREE_SCENARIO_METRICS.md`
- `outputs/meeting_demo_boundary_v5/T2_CONTROLLER_BOUNDARY_GAP.md`
- `docs/clean_release/FINAL_THREE_SCENARIO_CONTRACT.md`

## 11. Holdout 的最高科学结论

### 从正式 Freeze evidence 恢复的数字

V5 一次性执行了 96 个 Holdout samples、5 个 participants、480 authoritative runs，没有 retry 或 compromise。SATC `satc_b_027` 的总体结果为：

- Safety `100%`
- Success `55.21%`
- Position RMSE `0.0968265310 m`
- Full-LQR position RMSE `0.1365705883 m`
- Position improvement `29.10%`
- Acquisition median `2.415 s`
- Paired bootstrap 95% CI `[0.033754, 0.045756] m`
- Strong position improvement vs Full-LQR `34.41%`
- Strong position improvement vs legacy Self `80.11%`
- Directional tail gates passed; catastrophic pairs `0`

### Claim 边界

正式最高 claim 是：

```text
V5_SELF_OVERALL_HOLDOUT_WIN
```

不能写 `STRICT_ALL_METRIC_WIN`，因为 normal-regime acquisition 相对 legacy `self_a_034` 变差 `11.27%`，超过 `10%` gate；V5 正式记录为 `19/20` gates，strict gate false。也不能把它写成 original Paper superiority、Paper-vs-SATC、real flight 或 full industrial validation。

### 交叉核对

本次只读取并交叉核对 V5 Freeze 的 `claim_matrix.json`、`metric_summary.json`、`holdout/gate.json`、`self_vs_primary.json` 和 V5 final report，没有重跑 Holdout。

### 关键证据

- tag `v5-research-final-2026-08-09`
- `docs/V5_FINAL_TECHNICAL_REPORT.md`
- `reproducibility/v5/final/claim_matrix.json`
- `reproducibility/v5/final/metric_summary.json`
- `reproducibility/v5/holdout/gate.json`
- `reproducibility/v5/holdout/self_vs_primary.json`
- `reproducibility/v5/holdout/execution_manifest.json`

## 12. 最终三场景：Freeze 后留下什么

### T1

```text
initial sway = [20, -16, 12, -8, 4] deg
move = 5 s
wind = 0 m/s
PID = fail
Full-LQR = stable
SATC = stable
```

### T2

```text
initial sway = [20, -16, 12, -8, 4] deg
move = 5 s
wind = world +X, 3 m/s
onset = 3 s
ramp = half-cosine, 3--4 s
Full-LQR = stable
SATC = stable
```

T2 selected evidence gives post-wind RMS `0.304384 m` for LQR and `0.323038 m` for SATC；这是一项 functional capability comparison，不是 Holdout。

### T3（历史归档，不重跑）

```text
hover, zero initial sway, world +X
LQR max recoverable = 3 m/s
SATC max recoverable = 5 m/s
```

T3 的数值是 historical archived result；本归档没有把它重新执行。

### 关键证据

- tag `research-final-freeze-2026-08-12`
- `docs/clean_release/RESEARCH_FINAL_FREEZE_MANIFEST.md`
- `docs/clean_release/FINAL_THREE_SCENARIO_CONTRACT.md`
- `outputs/meeting_demo_boundary_v5/FINAL_THREE_SCENARIO_METRICS.md`
- `outputs/meeting_demo_boundary_v5/T2_CONTROLLER_BOUNDARY_GAP.md`

## 13. 为什么迁移到 Clean Repo

### 迁移动机

旧科研仓库同时保存源码、完整 reproducibility bank、失败实验、CSV/NPZ、视频、渲染和本地 debug，因此本地体量约 `1.785518 GiB`；其中 `outputs` 约 `0.541646 GiB`、`reproducibility` 约 `0.750533 GiB`。Clean repo 的目的不是重写科学结果，而是只保留可运行的 source/dependency closure、冻结 manifest、必要测试和可读的历史说明，降低本地保存成本。

### 迁移如何验证

Clean 从 `98361f68f5d8105659a65a4942502ce169ddd60a` bootstrap；parity 工具只读取 OLD/CLEAN 已有的 isolated outputs 和 frozen evidence，不执行仿真。结果是：

```text
OLD vs CLEAN T1/T2 time-series max difference = 0
OLD vs CLEAN metrics max difference = 0
CLEAN_REPO_FUNCTIONAL_PARITY = PASS
```

这说明 Clean 可以承接当前冻结工作流；它不等于旧仓库已经可以删除。旧仓库仍必须完整保存，直到 owner 另行批准并完成独立存档核验。

### 关键证据

- old tag `research-final-freeze-2026-08-12`
- `docs/clean_release/LOCAL_STORAGE_AUDIT.md`
- Clean `docs/MIGRATION_PARITY_REPORT.md`
- Clean `tools/verify_migration_parity.py`
- Clean commit `88a6edbf116e480a7f55ab5b051bccbafb9d1353`

## 14. 当前 Freeze 不包含的未来方向

以下方向只是明确讨论过的 future work，不属于当前 Freeze，本次没有启动：

- output-feedback；
- EKF / UKF / nonlinear observer；
- 真实传感器状态估计；
- hardware validation；
- 完整 cutter orientation / heading 控制与独立验证。

另外，Native R1R4、Governance V3、Benchmark V1.3 和 Native Paper stage 都没有因为归档而开启。未来任何一项都必须有新的授权、协议和独立 evidence。

## 15. 这段研究过程最重要的经验

这不是泛泛的项目管理口号，而是从上述真实结果归纳出的研究规则：

1. 不要为了新算法去改 benchmark；先把传统强 baseline 和公平接口冻结。
2. 失败边界也是科研结果；必须保留 failure、root cause、停止理由和适用范围。
3. 多连杆控制要同时审查 model、controller authority、reference mapping、saturation 和 safety，不能只看 solver status 或单个均值。
4. Holdout 只能一次、只能按预注册规则使用；不能用 Holdout 反向调参，也不能把一个 Overall win 写成 Strict all-metric win。
5. 复杂新路线失败后要及时停止；否则追加预算会把“探索”变成事后救援，损害结论可信度。
6. Demo capability、formal scientific claim、Native qualification 和 real-world validation 必须分开。
7. “模型/接口无法支持某个能力”必须由 API audit 和 evidence 证明，不能从视觉效果猜测 heading 或 full 6DoF control。

## 16. 仍然没有被旧证据完整恢复的事项

以下内容没有在本次文档中补猜：

- V1 之前的个人动机、最初代码原型和未进入 Git 的早期实验：`NOT FULLY RECOVERED`。
- P3-R1D 中每个 4 s failure 的完整 raw trace 与逐时刻 causal attribution：正式 postmortem 有分类和边界，但不是完整 mechanism reconstruction，故逐时刻机制为 `NOT FULLY RECOVERED`。
- V4 simultaneous-onset 失败的完整 onset-time/vector-angle 因 R1 未保存对应 time-series：正式文件只支持已确认的 direction partition 与低-trust/high-correction/high-slew 机制，细节仍是 hypothesis。
- 旧仓库所有中间 candidate 的完整调参过程：只归档改变研究方向的关键尝试，完整 bank 仍在 OLD。

这些未恢复项不会改变当前 Freeze、V5 claim 或 Clean parity 结论。
