# evidence_ops Eval

## 范围

manifest 规范、secret 扫描、completed 硬门、与 savepoint 联动。

## 用例

| ID | 场景 | Pass |
|----|------|------|
| E-01 | 新建 ticket evidence | manifest.json 含 artifacts 列表 |
| E-02 | manifest 含 API key 样例 | **Fail** — 必须拒写 |
| E-03 | ok=true 但无 artifact 文件 | **Fail** |
| E-04 | savepoint 后 latest_state 更新 | 路径可 grep |

## 自动检查（建议脚本）

```bash
# 伪代码：扫描 manifest 禁止键
rg -i "token|secret|webhook|\.env" evidence/
```

## Pass 定义

所有 E-0x 通过 + 样例 manifest 可被玄策 **仅读文件** 验收。
