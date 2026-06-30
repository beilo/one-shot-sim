# Changelog

## 2026-06-30

- 发布独立仓库版本，新增 `README.md`、`install.sh` 和安装自检说明，方便外部用户安装 `one-shot-sim`。
- 修复安装脚本在 `set -u` 下退出时清理临时目录触发未绑定变量的问题。

## 2026-06-26

- 将 `one-shot-sim` 调整为 task-first 流程：`brainstorm` 创建或定位 planning task，`confirm` 输出 PRD/research/阻塞/下一步结论并等待用户确认，`plan` 不再创建 task。
- 移除 no-task 执行和收尾路径，旧 no-task 状态不迁移，遇到时要求回到 `brainstorm` 创建 task。
- 同步 Trellis Manager 源码内置版 finish 规则：自动挡启动 one-shot-sim 后，允许 finish 自动执行 work commit、task archive、journal 记录和收尾 commit。

## 2026-06-11

- 将 Trellis one-shot-sim 的默认模式从手动挡调整为自动挡。
- 保留 `step0` / `step1` 不自动合并或跳过，避免需求讨论和方案拷打被默认自动推进吞掉。
- 增加显式手动挡触发词：`手动挡`、`manual mode`、`只跑当前阶段`、`不要自动推进`、`不要自动跑到最后`。
