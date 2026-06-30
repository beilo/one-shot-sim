# execute 阶段规则

## 适用阶段

仅适用于 `execute` 阶段。不要在 `brainstorm`、`confirm`、`plan`、`finish` 阶段套用本文件。

## 目标

由主会话直接实现、检查和沉淀，不使用 channel，不使用子代理。只支持 task-backed 路径。

## 前置条件

- task 已存在且有完整规划文档。用户未提供 task 时，默认当前 active task。
- 没有 active task、没有 task 文件或只有旧 no-task 状态时，停止并要求回到 `brainstorm` 创建 task。
- 已确认不使用 Trellis channel runtime。
- 已确认不使用任何子代理。

## 必须顺序

1. 读取当前 task 的 PRD、design、implement 计划材料和相关 spec/research。
2. 只修改本任务相关文件；发现无关脏改时报告并保留。
3. 按计划材料实现。有疑问按推荐方案继续，除非遇到破坏性风险、无法判断文件归属或缺少关键上下文。
4. 主会话执行 `trellis-check`；检查逻辑只围绕本任务 diff、task artifacts 和相关 spec。
5. 主会话执行 `trellis-update-spec`；有沉淀内容就更新 spec，没有则明确说明。

## 检查范围

- 只检查本任务改过的文件。
- 不做全量 lint/typecheck，除非 task 规划明确要求或局部验证无法覆盖风险。
- 不 review 无关 diff。
- 不要求 channel done/error 证据。

## 完成标准

- 主会话已完成任务实现。
- 主会话已完成 `trellis-check`，或明确报告局部检查无法执行的原因。
- 主会话已完成 `trellis-update-spec`，或明确说明没有可沉淀内容。
- 手动挡：输出 `execute` 结论和 `finish` 入口，然后停止等待用户继续。
- 自动挡：输出 `execute` 结论，并直接进入 `finish`。

## 错误完成

- 主会话无法继续执行时，输出 `execute` 错误结论。
- 不进入 `finish`。
