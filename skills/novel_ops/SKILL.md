# novel_ops — 小说/内容生产流水线

## 何时使用

- 章节大纲、人设卡、连载节奏、平台发文草稿。
- 需要将创意落成可验收文件（outline、chapter draft、metadata.json）。

## 输入

- tasks/<ticket>.md：题材、字数、禁忌、目标平台。
- 可选：reference 路径、竞品笔记（docs/COMPETITOR_LEARNING_NOTES.md）。

## 输出（evidence 必填）

```text
evidence/novel_ops/<ticket>/<timestamp>/
├── outline.md
├── chapter_draft.md
├── metadata.json
└── self_check.md
```

## 完成标准

```json
{
  "status": "completed",
  "result": { "ok": true }
}
```

仅当 metadata.json 中 ok=true 且编辑自检通过。

## 角色默认

| 步骤 | Owner |
| --- | --- |
| 大纲/结构 | 玄策裁定 + 白起/卫青起草 |
| 素材整理 | 青鸟 |
| 技术导出/自动化 | 鲁班 |

## 禁止

- 只输出聊天摘要无文件。
- 虚构已发布无截图或平台 evidence。
