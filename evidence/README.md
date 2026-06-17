# evidence/

本目录存放 **可验收产物** 与 eval 跑分结果。

## 布局

```
evidence/
├── <domain>/           # novel_ops | research_ops | code_review | ...
│   └── <ticket>/
│       └── <timestamp>/
│           ├── manifest.json
│           └── ...
└── evals/              # 评测运行产物
    └── <benchmark>/
        └── <run_id>/
```

## manifest.json（必填）

```json
{
  "ticket": "TICKET-001",
  "owner": "luban",
  "generated_at": "2026-06-18T12:00:00+08:00",
  "artifacts": ["report.json"],
  "status": "completed",
  "result": { "ok": true }
}
```

## 规则

- **只认本目录与 monorepo `shared_workspace/evidence/` 的文件**，不认聊天。
- 禁止 token、secret、webhook、`.env` 内容。
- `result.ok=false` 时 status 不得为 completed。

详见 `skills/evidence_ops/SKILL.md`。
