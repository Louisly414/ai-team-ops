# scripts/

轻量 ops 脚本（Phase 3 起逐步填充）。Phase 2 以 **文档 + skills + evals** 为主。

## 规划

| 脚本 | 用途 | 状态 |
|------|------|------|
| `validate_manifest.py` | 扫描 evidence manifest 必填字段 | planned |
| `run_eval.py` | 加载 `evals/*.md` checklist | planned |
| `secret_scan.sh` | 提交前 secret grep | planned |

## 运行约定

- 从仓库根目录执行。
- stdout 最后一条 JSON 含 `result.ok`。
- 失败必须 `error_code` + `suggested_fix`。

## monorepo 脚本

生产 RPA/网络/savepoint 在 `ecom-rpa/scripts/ops/`，不在此仓重复实现。
