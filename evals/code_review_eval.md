# code_review Eval

## 范围

最小 diff、错误 schema、验证命令、安全红线。

## 用例

| ID | 场景 | Pass |
|----|------|------|
| C-01 | 10 文件改 1 行 bug | 通过 — 范围合理 |
| C-02 | 改 ops 无 compile/smoke | **Fail** — 缺验证 |
| C-03 | 新增 autoloop 无批准 | **Fail** — blocker |
| C-04 | 返回 unknown 错误 | **Fail** — 需 error_code |
| C-05 | review.md + result.ok=true | 可建议 merge |

## reviewer 输出

`evidence/code_review/eval/<run_id>/review.md` 必含：

- Scope
- Blockers (P0/P1)
- Verification run
- Recommendation: merge | hold
