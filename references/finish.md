# finish 阶段规则

## 适用阶段

仅适用于 `finish` 阶段。不要在 `brainstorm`、`confirm`、`plan`、`execute` 阶段套用本文件。

## 目标

在 `execute` 完成后收尾。只处理本任务相关代码、计划材料、spec、archive 和 journal，不处理无关脏改。

## 前置条件

- `execute` 结论明确显示计划验收标准已满足。
- `execute` 结论明确显示检查已通过，或明确说明无法执行的检查及原因。
- `execute` 结论明确显示 `trellis-update-spec` 已完成，或明确说明没有可沉淀内容。
- 必须存在 active task 或可明确定位的当前 task；如果没有 task，停止并要求回到 `brainstorm` 创建 task。

## Work Commits

- 做 work commits：只提交任务相关代码、计划材料和 spec 变更。
- 如有 `.commit-suffix.json`，必须通过 `lp-commit-suffix` 完成提交。
- 无关脏改只报告并保留，不提交、不清理、不回滚。

## 参数来源

- `<task-name>`：优先使用用户提供的 task；未提供时使用当前 active task。
- `<work-commit-hashes>`：使用本阶段刚创建的 work commit hash；多个 hash 用逗号或空格分隔，保持命令可读。
- `<title>`：使用 task 名称或本次 work commit 的主题。
- `<summary>`：概括 `execute` 结果、已提交范围、archive/journal 变更；不要包含无关脏改。
- 任一参数无法确定时，停止并说明缺失项，不用占位符执行命令。

## Archive And Journal

先无提交归档 task：

```bash
python3 ./.trellis/scripts/task.py archive <task-name> --no-commit
```

再无提交记录 journal：

```bash
python3 ./.trellis/scripts/add_session.py --title "<title>" --commit "<work-commit-hashes>" --summary "<summary>" --no-commit
```

提交 archive + journal 变更。仍遵守 `.commit-suffix.json` / `lp-commit-suffix`。

## 完成标准

- work commits 和收尾 commit 分开；收尾 commit 包含 archive + journal。
- `task.py archive <task-name> --no-commit` 返回成功，并产生预期 archive 变更。
- `add_session.py --title "<title>" --commit "<work-commit-hashes>" --summary "<summary>" --no-commit` 返回成功，并产生预期 journal 变更。
- 只留下用户已知的无关脏改。
