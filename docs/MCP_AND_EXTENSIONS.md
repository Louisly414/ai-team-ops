# MCP and Extensions

## Cursor MCP（monorepo 侧）

| Server | 用途 |
|--------|------|
| plugin-notion-workspace | Notion 任务/文档（可选） |
| plugin-figma-figma | 设计协作（可选） |
| plugin-datadog-datadog | 生产监控（可选） |
| user-openclaw | OpenClaw 集成 |

**规则**：调用 MCP 前读 tool schema；失败写 `error_code`，不 silent skip。

## Browser / RPA 扩展

- CDP port owner：白起 9223 / 鲁班 9224 / 青鸟+大禹 9225
- 优先 monorepo 脚本：`cdp_rpa_session.py`、reconcile、watchdog

## Custom GPT（玄策）

- 设备授权 ≠ `gh` CLI；各登各的。
- 玄策桌面模式：broker job，只读 evidence + 白名单 ops。

## 扩展选型原则

1. 能否产出 **路径型 evidence**？
2. 是否增加 autoloop/real-once 风险？
3. 能否 Hidden 后台跑（Windows 计划任务）？

## 待评估

- [ ] ai-team-ops 专用 MCP：manifest 校验器
- [ ] eval runner GitHub Action
