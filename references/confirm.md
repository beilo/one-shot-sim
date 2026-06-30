# confirm 阶段规则

## 适用阶段

仅适用于 `confirm` 阶段。不要在 `brainstorm`、`plan`、`execute`、`finish` 阶段套用本文件。

## 目标

确认当前 planning task 的 `prd.md` 和 research 是否足够进入 `plan`。对外进度块仍显示 `confirm 执行确认`。

## 前置条件

- 当前仓库存在 `.trellis`。
- 当前对话已有 active task，或能从 `brainstorm` 输出中定位到刚创建的 planning task。
- 当前 task 至少包含 `prd.md`。
- 不支持 no-task 路径；如果没有 task，停止并要求回到 `brainstorm` 创建 task。

## 必须顺序

1. 读取当前 task 的 `prd.md`。
2. 检查目标、边界、约束、验收标准和未决问题是否足够支撑规划。
3. 对能通过代码、文档、spec、已有 task 或历史记录回答的问题，直接研究，不再询问用户。
4. 如有必要，创建或更新当前 task 的 `research/*.md`。无研究必要时，明确说明无需 research。
5. 输出固定四项结论块：

```text
confirm 结论：
- PRD：<已清楚 / 需要补充 + 原因>
- research：<已完成 / 无需 research / 需要补充 + 路径或原因>
- 阻塞问题：<无 / 列出问题>
- 下一步：<等待用户确认进入 plan / 回到 brainstorm>
```

6. 自动挡也必须停下等待用户明确确认进入 `plan`。

## 完成标准

- 已读取并检查当前 task 的 `prd.md`。
- repository-answerable 问题已经通过研究处理，或明确说明无需 research。
- 已输出 `PRD`、`research`、`阻塞问题`、`下一步` 四项结论。
- 用户明确确认可以进入 `plan`。

## 阻塞处理

- `prd.md` 缺目标、边界或验收标准时，回到 `brainstorm`。
- research 发现需求冲突、破坏性风险或无法判断文件归属时，停止并说明。
- 发现旧 no-task 状态时，停止并要求回到 `brainstorm` 创建 task；不迁移旧状态。
