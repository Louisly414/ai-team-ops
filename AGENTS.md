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
## Cursor Cloud specific instructions

- 运行环境：仅需 Python 3.12 + git，脚本仅用标准库，无第三方依赖，无需 pip/npm 安装。
- 本仓唯一可运行代码是两个校验脚本（等同 CI 的 contractcheck / linecheck），从仓库根目录运行：
  - `python3 scripts/check_repo_contract.py`（校验目录契约；成功时无输出，exit 0）
  - `python3 scripts/check_blob_line_endings.py HEAD`（校验行尾；输出 JSON，exit 0）
- 非显然点：`check_blob_line_endings.py` 校验的是已提交的 git blob（经 `git show`），不是工作区文件；未提交改动不会被检测，且需完整 git 历史（CI 用 fetch-depth: 0）。
- 非显然点：`AGENTS.md`、`docs/TOOLCHAIN_ROADMAP.md`、`skills/novel_ops/SKILL.md`、`skills/evidence_ops/SKILL.md` 由 `.gitattributes` 强制以 CRLF 存储且是 linecheck 的 CRLF 严格目标，编辑后必须保持 CRLF，否则 linecheck 失败。
- 可执行的 RPA 产品在独立仓库 `ecom-rpa`；本仓仅含角色契约 / skills / evals / 文档，无需启动任何常驻服务。
