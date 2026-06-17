# Toolchain Roadmap — AI Team Ops

## 现状（Phase 2）

| 层 | 组件 | 状态 |
| --- | --- | --- |
| 指挥 | 玄策 broker + remote worker | monorepo 生产 |
| 执行 | 白起/卫青 Codex，鲁班 Cursor | 已分工 |
| 半自动 | 青鸟 9225，飞书 gateway | 已部署 |
| 管道 | 大禹 pipeline watchdog/reconcile | 计划任务 Hidden |
| 证据 | evidence_ops + savepoint | 真源 monorepo |
| 本仓 | skills + evals + docs | Phase 2 已完成 |

## Phase 3（下一步）

- [ ] scripts/ 轻量 CLI：manifest 校验、eval 跑分
- [ ] skills 与 Cursor .cursor/skills 同步清单
- [ ] evals 自动化 → GitHub Actions on ai-team-ops
- [ ] 角色 inbox JSON schema 版本化

## Phase 4

- [ ] 竞品 agent 框架 diff 月度更新（见 COMPETITOR_LEARNING_NOTES）
- [ ] 统一 error_code registry 跨 monorepo
- [ ] 飞书卡片模板与 artifact_ops 绑定

## 原则

- 先 evidence 再 automation。
- 训练阶段全速侦察；正式阶段上架需 Louis 批准。
