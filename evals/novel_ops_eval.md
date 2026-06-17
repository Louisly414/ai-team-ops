# novel_ops Eval

## 范围

大纲结构、草稿质量、metadata 完整性、平台约束遵守。

## 用例

| ID | 输入 | Pass 标准 |
|----|------|-----------|
| N-01 | 2000 字玄幻开篇 | outline + draft + metadata.ok=true |
| N-02 | 含禁用题材 | result.ok=false + 明确 blocker |
| N-03 | 仅聊天输出 | **Fail** — 无 evidence 目录 |

## 验收 JSON

```json
{
  "status": "completed",
  "result": { "ok": true },
  "word_count": 2000,
  "self_check_passed": true
}
```

## 执行

1. 读 `skills/novel_ops/SKILL.md`
2. 跑用例，产物入 `evidence/novel_ops/eval/<run_id>/`
3. 玄策对照本文件签字
