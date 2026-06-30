# one-shot-sim

`one-shot-sim` 是 Trellis 一轮完成的简化版 skill。它不依赖 channel runtime，也不启动子代理，由主会话按固定阶段直接推进：

```text
brainstorm -> confirm -> plan -> execute -> finish
```

适合想保留 Trellis 任务、PRD、规划、执行、检查、收尾节奏，但不想引入多代理编排的人。

## 安装

```bash
curl -fsSL https://raw.githubusercontent.com/beilo/one-shot-sim/main/install.sh | bash
```

默认安装到：

```text
~/.agents/skills/one-shot-sim
```

自定义安装目录：

```bash
ONE_SHOT_SIM_INSTALL_DIR=/path/to/skills/one-shot-sim bash install.sh
```

## 使用

在支持 agent skills 的环境里说：

```text
使用 one-shot-sim
```

常用说法：

```text
one-shot-sim
简化版一轮完成
一轮完成
法拉利模式
拖拉机模式
```

默认是自动挡。`confirm` 阶段仍会停下，要求你明确确认后才进入 `plan`。

## 阶段

- `brainstorm`：创建或定位 planning task，并把需求写入 `prd.md`。
- `confirm`：检查 `prd.md` 和 research 是否足够进入规划。
- `plan`：完成规划产物，并在自动挡中启动 task。
- `execute`：主会话直接实现、检查和沉淀。
- `finish`：提交任务改动、适用时归档 task、记录 journal，并提交收尾变更。

## 状态文件

运行态状态默认写入：

```text
~/.one-shot/flow-state/one-shot-sim/<conversation_id>.json
```

状态文件依赖 `CLAUDE_CODE_SESSION_ID`、`CLAUDE_SESSION_ID` 或 `CODEX_THREAD_ID` 识别当前对话。识别不到时，skill 会停止自动推进并要求你确认阶段。

## 自检

```bash
python3 -m unittest tests/test_contract.py
```

## 更新

重复运行安装命令即可。如果目标目录已经是本仓库的 git clone，安装脚本会执行 `git pull --ff-only`；否则会备份旧目录后重新安装。
