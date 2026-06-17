# AGENTS.md — AI Team Operations

本仓库定义 **玄策 AI 战队** 的协作契约、技能与评测基线。所有 agent（含 Custom GPT、Cursor、Codex、本地 worker）在本仓或关联 monorepo 执行任务时，**必须**遵守本文。

---

## 核心原则

### 只认 evidence，不认聊天记忆

- **事实以文件为准**：handoff、savepoint、`evidence/`、JSON 报告、截图路径。
- 聊天里说过「已完成」不算完成；**没有落盘证据 = 未证明**。
- 续接任务时先读 `latest_topic.md` / ticket handoff，再 grep 证据目录，**禁止**让用户重贴长上下文。

### completed 的硬定义

任务只有同时满足以下条件，才可标记为 **completed**：

```json
{
  "status": "completed",
  "result": { "ok": true }
}
```

缺少任一项 → 只能是 `in_progress`、`blocked` 或 `failed`，并写清 `error_code`、`failed_stage`、`suggested_fix`。

---

## 六角色分工

| 角色 | 代号 | 职责 | 典型产出 |
|------|------|------|----------|
| **玄策** | 指挥官 | 战略、派单、验收、风险闸门；不 idle | 裁定、handoff、`latest_topic.md`、飞书卡片 |
| **白起** | 主执行 | 主代码路径、高判断变更、经营向实现 | PR、脚本、Alpha 实验闭环 |
| **卫青** | 副执行 | 白起限额/阻塞时的接棒；常规任务 | 同白起，规模较小、接棒 receipt |
| **鲁班** | 技术救援 | 环境、selector、RPA、多文件工程 | patch、reconcile、CDP 9224 |
| **青鸟** | 搬运半自动 | 飞书字段、素材归档、表格、轻量 RPA | 结构化字段、素材路径、半自动 SOP |
| **大禹** | 管道治理 | 队列健康、降级接棒、跨角色管道不断流 | watchdog 报告、pipeline reconcile |

### 玄策

- 统一 ingress：`xuance_command_gateway` / broker job。
- 验收必须指向 **evidence 路径**，口头 pass 无效。
- 正式阶段：平台上架需 Louis 飞书批准；训练阶段不预阻塞研发速度。

### 白起

- 默认 CDP owner：**9223**。
- 每个 SKU/任务应推进 Alpha 12 问清单；gap = 更多侦察，不是 idle stop。

### 卫青

- 与白起同栈，**不**重复抢同一 ticket；接棒时写 inbox receipt 与 handoff 指针。

### 鲁班

- 默认 CDP owner：**9224**；Cursor Pro+ 重活用 Premium+Max。
- 可复用战术写入 weapon library；handoff 只写状态与下一步。

### 青鸟

- 默认 CDP owner：**9225**（与大禹共用端口锁）。
- 产出优先 **结构化 + 路径**，少写散文总结。

### 大禹

- 管道、队列、watchdog、降级路线；health check 结果落 JSON。
- 跨角色阻塞时升级 handoff，不 silently drop。

---

## 目录结构

```
ai-team-ops/
├── AGENTS.md          # 本文件 — 角色与契约
├── skills/            # 可安装/可引用的技能包
├── evals/             # 评测题与通过标准
├── docs/              #  toolchain、GitHub、MCP 等
├── tasks/             # 任务记录（ticket 级）
├── evidence/          # 证据归档（本仓示例/模板）
└── scripts/           # 可复用 ops 脚本（轻量）
```

---

## 协作流程

1. **tasks/** — 开 ticket：目标、owner、验收标准、证据目录约定。
2. **执行** — 按角色走对应 skill；产出写入 monorepo `shared_workspace/evidence/` 或本仓 `evidence/`。
3. **验收** — 玄策（或 Louis）对照 evals + `result.ok=true`。
4. **沉淀** — 可复用 SOP → `skills/` 或 monorepo weapon library；任务 closure → handoff。

---

## 禁止项

- 用聊天记忆代替 evidence 判 pass/fail。
- 无 `status=completed` + `result.ok=true` 宣称封板。
- handoff 堆知识 dump（知识进 weapon library / skills）。
- 写入 token、secret、`.env` 明文。

---

## 关联仓库

- 执行 monorepo：`ecom-rpa`（RPA、broker、shared_workspace）。
- 本仓：`ai-team-ops` — 角色契约、技能、评测与 ops 文档真源。

续接口令（monorepo）：**继续干活** → 读 `shared_workspace/handoff/xuance_session/latest_topic.md`。
