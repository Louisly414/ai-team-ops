# research_ops — 侦察与结构化调研

## 何时使用

- 竞品、1688、平台规则、市场信号、Alpha 12 问 gap 填充。
- 需要 **可引用路径** 而非口头结论。

## 输入

- 关键词 / SKU / URL 列表（`tasks/`）。
- 约束：平台、地域、时间窗、禁止动作（no autoloop / no real-once）。

## 输出

```
evidence/research_ops/<ticket>/<timestamp>/
├── sources.json       # URL、抓取时间、method
├── findings.md        # 结构化结论
├── scores.json        # 可选：机会打分
└── result.json        # { "ok": true, "gaps_remaining": [] }
```

## 质量条

- 每条结论 **至少一条** source 指针。
- 无法访问 → `error_code` + `suggested_fix`，不是编造。
- gap 未填完 → `status: in_progress`，不是 completed。

## 角色

| 类型 | Owner |
|------|-------|
| 公域 SERP / 列表 | 青鸟 半自动 + 鲁班 selector |
| 深度代码/架构 | 白起 / 卫青 |
| 机会裁定 | 玄策 |

## 评测

见 `evals/research_eval.md`。
