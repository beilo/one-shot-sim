#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${ONE_SHOT_SIM_REPO_URL:-https://github.com/beilo/one-shot-sim.git}"
INSTALL_DIR="${ONE_SHOT_SIM_INSTALL_DIR:-$HOME/.agents/skills/one-shot-sim}"
BRANCH="${ONE_SHOT_SIM_BRANCH:-main}"

log() {
  printf '%s\n' "$1"
}

fail() {
  printf '安装失败：%s\n' "$1" >&2
  exit 1
}

validate_skill_dir() {
  local dir="$1"

  # 保留显式校验，是为了让坏包在安装阶段失败，而不是等 agent 运行时才暴雷。
  test -f "$dir/SKILL.md" || return 1
  test -f "$dir/CHANGELOG.md" || return 1
  test -f "$dir/scripts/flow_state.py" || return 1

  local stage
  for stage in brainstorm confirm plan execute finish; do
    test -f "$dir/references/$stage.md" || return 1
  done
}

clone_to_target() {
  local target="$1"
  local parent
  parent="$(dirname "$target")"
  mkdir -p "$parent"

  local tmp
  tmp="$(mktemp -d)"
  ONE_SHOT_SIM_TMP="$tmp"
  trap 'rm -rf "${ONE_SHOT_SIM_TMP:-}"' EXIT

  log "下载 one-shot-sim：$REPO_URL"
  git clone --depth 1 --branch "$BRANCH" "$REPO_URL" "$tmp/repo" >/dev/null
  validate_skill_dir "$tmp/repo" || fail "下载内容缺少必要文件"

  if [ -e "$target" ] || [ -L "$target" ]; then
    local backup
    backup="$target.backup.$(date +%Y%m%d%H%M%S)"
    log "发现已有安装，备份到：$backup"
    mv "$target" "$backup"
  fi

  mv "$tmp/repo" "$target"
  log "安装完成：$target"
}

command -v git >/dev/null 2>&1 || fail "需要 git，但当前系统找不到 git"

if [ -d "$INSTALL_DIR/.git" ]; then
  current_remote="$(git -C "$INSTALL_DIR" remote get-url origin 2>/dev/null || true)"
  if [ "$current_remote" = "$REPO_URL" ]; then
    log "更新已有安装：$INSTALL_DIR"
    git -C "$INSTALL_DIR" fetch --depth 1 origin "$BRANCH" >/dev/null
    git -C "$INSTALL_DIR" checkout "$BRANCH" >/dev/null
    git -C "$INSTALL_DIR" pull --ff-only origin "$BRANCH" >/dev/null
    validate_skill_dir "$INSTALL_DIR" || fail "更新后缺少必要文件"
    log "更新完成：$INSTALL_DIR"
    exit 0
  fi
fi

clone_to_target "$INSTALL_DIR"
