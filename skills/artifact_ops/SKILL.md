# artifact_ops — 交付物打包与 handoff

## 何时使用

- ticket 结束：汇总 evidence、写 handoff、更新 `latest_topic.md`（monorepo）。
- 飞书卡片、JSON 报告、weapon library 条目提炼。

## 交付清单

| 类型 | 路径约定 |
|------|----------|
| 任务 closure | `tasks/<ticket>.md` 更新状态 |
| 证据索引 | `evidence/.../manifest.json` |
| 续接点 | monorepo `shared_workspace/handoff/xuance_session/latest_topic.md` |
| 可复用战术 | monorepo `shared_workspace/knowledge_base/ecom_weapon_library/` |

## handoff 必填字段

- 更新时间、ticket、已完成 / 上一条裁定
- **下一步（一条可执行动作）**
- 证据路径（report、handoff、savepoint）
- 硬约束（enabled、real-once、CDP port owner）
- 续接口令：`继续干活`

## 禁止写入 handoff

- token、secret、webhook、`.env`
- 知识 dump（应进 weapon library 或本仓 `skills/`）

## completed

```json
{
  "status": "completed",
  "result": { "ok": true },
  "evidence_paths": ["..."]
}
```

## 角色

- **玄策**：artifact 验收与 latest_topic 落盘。
- **青鸟**：飞书字段与素材路径整理。
- **大禹**：pipeline 状态块 append。
