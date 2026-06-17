# Competitor Learning Notes

竞品与社区框架的 **可借鉴点**（非抄代码）。更新时附 source URL + 日期。

## 2026-06 — 观察摘要

| 来源 | 借鉴 | 不借鉴 |
|------|------|--------|
| Cursor Agent + Skills | 技能文件化、handoff 与 skill 分离 | 无 evidence 门的「已完成」口语 |
| OpenAI Codex / ACP | 后台执行、PTY 会话 | 跨仓 secret 注入 |
| 通用 RPA 框架 | selector 版本化、retry schema | 无限 autoloop |
| GitHub Actions eval | PR 上跑 benchmark | 把生产密钥进 CI log |

## 玄策战队差异化

1. **只认 evidence** — 聊天不算数。
2. **六角色 + CDP 锁** — 并行不抢端口。
3. **completed 硬 JSON** — `status=completed` + `result.ok=true`。
4. **weapon library vs handoff** — 知识不堆 handoff。

## 待跟进

- [ ] 竞品「eval harness」目录结构对比 → 反哺 `evals/`
- [ ] 飞书 bot 卡片 vs Slack Block Kit 字段映射（青鸟）

## 更新协议

- 新条目：日期 + 来源 + 1 条 actionable
- 可执行项进 `docs/TOOLCHAIN_ROADMAP.md` Phase 列表
