# plan 阶段规则

## 适用阶段

仅适用于 `plan` 阶段。不要在 `brainstorm`、`confirm`、`execute`、`finish` 阶段套用本文件。

## 规则

基于当前 planning task 进入 Trellis Plan Flow 阶段。`plan` 不创建 task；task creation 必须已经在 `brainstorm` 完成。

- 必须读取当前 task 的 `prd.md`。
- 如存在 `research/*.md`，必须读取与本任务相关的 research。
- 如果缺少 active task，停止并要求回到 `brainstorm` 创建 task；不走 no-task 路径。
- 如果缺少目标、边界、约束、验收标准或关键取舍，回到 `brainstorm` 或 `confirm`，不要进入实现。
- 如果 Plan Flow 里出现真实未决问题、破坏性风险或需求冲突，停止并说明阻塞点；不要擅自继续。
- Plan Flow 的“执行前确认”只在手动挡生效；自动挡 / 法拉利下，完整规划材料加无未决问题即视为已批准执行。
- 产出 task 规划文档后，明确当前处于 `plan`。手动挡停止等待用户继续；自动挡运行 `task.py start` 后直接进入 `execute`。

## 完成标准

- 需求、约束、验收标准清楚。
- task 已存在，并产出完整规划文档。
- 有真实未决问题、破坏性风险或需求冲突时已停止等待。
- 手动挡：输出 `plan` 结论、task 名称和规划产物路径，然后停止等待用户明确批准 `execute`。
- 自动挡：输出 `plan` 结论、task 名称和规划产物路径，运行 `task.py start`，然后直接进入 `execute`。
