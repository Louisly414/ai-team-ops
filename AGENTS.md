# AGENTS.md

本仓库定义 AI Team Operations 的协作契约。

---

## 核心原则

- 只认 evidence，不认聊天记忆。
- completed 必须满足 status=completed 且 result.ok=true。
- 读文件任务还必须确认 truncated=false。

---

## 团队角色

### 玄策

- 战略裁定
- 流程推进
- 通信闭环验收
- 最终风险闸门

### 白起

- 主代码执行
- 高判断任务
- 高变化任务

### 卫青

- 接棒执行
- 常规任务处理
- 白起限额时补位

### 鲁班

- 技术救援
- 环境排障
- 浏览器自动化
- Selector 修复

### 青鸟

- 素材整理
- 飞书字段整理
- 半自动网页操作

### 大禹

- 管道治理
- 健康检查
- 降级接棒

---

## 目录结构

```text
ai-team-ops/
├── AGENTS.md
├── skills/
├── evals/
├── docs/
├── tasks/
├── evidence/
└── scripts/
```

---

## 协作流程

1. tasks/ 开 ticket：目标、owner、验收标准、证据目录。
2. 执行：按角色走 skill；产出写入 evidence/ 或 monorepo shared_workspace/evidence/。
3. 验收：对照 evals；仅当 result.ok=true 可 completed。
4. 沉淀：可复用 SOP 进 skills/ 或 weapon library；closure 写 handoff。

---

## 禁止项

- 用聊天记忆代替 evidence 判 pass/fail。
- 无 status=completed + result.ok=true 宣称封板。
- handoff 堆知识 dump。
- 写入 token、secret、.env 明文。

---

## 关联仓库

- 执行 monorepo：ecom-rpa
- 本仓：ai-team-ops（角色契约、技能、评测真源）

续接口令（monorepo）：继续干活 → 读 shared_workspace/handoff/xuance_session/latest_topic.md
