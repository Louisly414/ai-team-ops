# code_review — 代码审查技能

## 何时使用

- PR 前自检、鲁班/白起互审、封板前 diff 审查。
- Bugbot / security review 子任务触发前的人类或 agent 清单。

## 审查顺序

1. **意图** — diff 是否匹配 ticket 一句话目标？
2. **范围** — 是否最小 diff？有无无关文件？
3. **正确性** — 边界、错误 schema（`error_code` / `failed_stage` / `suggested_fix`）。
4. **证据** — 改脚本是否附 runnable check（compile / smoke）？
5. **安全** — 无 secret、无 force push、无 autoloop 未授权。

## 输出

```
evidence/code_review/<ticket>/<timestamp>/
├── review.md          #  findings: pass/fail per item
├── diff_scope.txt     # 文件列表
└── result.json        # { "ok": true|false, "blockers": [] }
```

## Pass 条件

- 无 P0 blocker。
- 所有 P0 脚本变更有验证命令记录。
- `result.ok=true` 才可建议 merge。

## 角色

- **白起/卫青**：实现方自检。
- **鲁班**：环境/RPA/多文件工程审查。
- **玄策**：是否满足 ticket 验收，不代写大段 code review 散文。

## 评测

见 `evals/code_review_eval.md`。
