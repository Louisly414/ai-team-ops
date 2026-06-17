# evidence_ops — 证据落盘与验收

## 何时使用

- 任何需要 prove not describe 的任务前后。
- handoff 保存、savepoint、ticket 封板前自检。

## 流程

1. 规划路径：evidence/<domain>/<ticket>/<YYYYMMDD_HHMMSS>/
2. 写 manifest.json（见下方示例）
3. 禁止 secrets：不得含 token、webhook、.env 内容
4. 验收：玄策只读 manifest + 引用文件；不认聊天

## manifest.json 示例

```json
{
  "ticket": "TICKET-001",
  "owner": "luban",
  "generated_at": "2026-06-18T12:00:00",
  "artifacts": ["report.json", "screenshot.png"],
  "status": "completed",
  "result": { "ok": true }
}
```

## completed 硬门

```json
{
  "status": "completed",
  "result": { "ok": true }
}
```

result.ok=false 或缺 manifest → 不得 completed。

## 与 monorepo 关系

- 生产证据优先：ecom-rpa/shared_workspace/evidence/
- 本仓 evidence/：模板、示例、评测产物

## 常用命令（monorepo）

```bash
python scripts/ops/savepoint.py --json
```

## 角色

- 大禹：watchdog / reconcile 类 evidence
- 鲁班：RPA、网络、环境类 evidence
- 玄策：验收签字（指向路径，不口头）
