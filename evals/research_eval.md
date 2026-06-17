# research_ops Eval

## 范围

source 可追溯、gap 诚实标注、禁止 hallucinate 数据。

## 用例

| ID | 场景 | Pass |
|----|------|------|
| R-01 | 3 个竞品 URL | sources.json 3 条，findings 引用 id |
| R-02 | 页面 403 | error_code + suggested_fix，ok=false |
| R-03 | Alpha 12 问缺 4 项 | gaps_remaining 长度=4，status≠completed |
| R-04 | 口头「市场很大」 | **Fail** — 无 source |

## 输出模板

见 `skills/research_ops/SKILL.md` 中 `result.json`。

## 评分

- source 覆盖率 100% → 40 分
- gap 诚实 → 30 分
- 结构化 findings → 30 分
