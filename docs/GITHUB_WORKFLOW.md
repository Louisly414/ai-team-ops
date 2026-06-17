# GitHub Workflow — ai-team-ops

## 仓库

- **本仓**：https://github.com/Louisly414/ai-team-ops
- **执行 monorepo**：`ecom-rpa`（本地 `C:\Users\yuliu\ecom-rpa`，可独立 push）

## 本机前置

```powershell
gh auth status
# 应显示 Logged in to github.com account Louisly414
```

## 日常流程

```powershell
cd C:\Users\yuliu\ecom-rpa\ai-team-ops
git pull
# ... 编辑 skills / evals / docs ...
git add -A
git commit -m "docs: describe change"
git push
```

## 分支策略

| 类型 | 分支 |
|------|------|
| 文档/skills 小改 | 直接 `main` |
| 评测/schema 变更 | `feat/<ticket>` → PR |

## PR 模板（建议）

- Summary：为什么改
- Evidence：eval 或 manifest 路径
- Test plan：本地 grep / script 命令

## 与 monorepo 关系

- **不**把 `ecom-rpa` 全量塞进 ai-team-ops。
- 契约、技能、评测在本仓；RPA/证据在生产 monorepo。
- 跨仓引用用 **路径文字 + commit SHA**，不用聊天记忆。

## 安全

- 禁止 commit `.env`、token、webhook。
- 私有仓默认；公开前扫 secret。
