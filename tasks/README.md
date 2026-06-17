# tasks/

本目录存放 **ticket 级任务记录**（ai-team-ops 仓内示例与模板）。

## 命名

```
tasks/<TICKET-ID>_<short_slug>.md
```

示例：`tasks/NETWORK-STABILITY-001_reconcile.md`

## 模板

```markdown
# TICKET-ID — 标题

- **Owner**: luban | baiqi | xuance | ...
- **Status**: in_progress | blocked | completed
- **Created**: 2026-06-18

## 目标

一句话可验收目标。

## 验收标准

- [ ] evidence 路径：...
- [ ] result.json → `"ok": true`

## 结果

（完成后填 evidence 指针；completed 仅当 status=completed + result.ok=true）
```

## 与 monorepo 关系

生产任务真源在 `ecom-rpa/shared_workspace/handoff/` 与飞书；本目录用于 **ops 仓自洽示例** 与 eval fixture。
