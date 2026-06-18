# Capability Registry

This file is the capability map for 玄策DT and the ai-team-ops workflow.

## Hard boundary

- Chat memory is not evidence.
- GitHub public pages can be read.
- Direct GitHub push is not available unless an explicit write-capable tool is present.
- Browser RPA may be available through controlled CDP owners, but external writes require explicit evidence.
- A task is not complete without evidence.

## Completion gates

A local worker job is complete only when:

```json
{
  "status": "completed",
  "result": {
    "ok": true
  }
}
```

For reads, also require:

```json
{
  "truncated": false
}
```

## Capability matrix

| Capability | Status | Evidence / gate |
|---|---|---|
| Read public GitHub raw files | available | raw URL readable |
| Write GitHub repo directly | not available in current chat | requires write-capable connector / CLI / authenticated git |
| Create repo edit packs | available | local evidence file with content |
| Validate remote Actions status | available by web/CDP | workflow page + local evidence |
| Run local broker read/write | available | getJob completed + result.ok true |
| Browser RPA | limited | CDP owner and evidence required |
| Novel candidate workflow | available | novel_ops skill + savepoint evidence |
| Artifact generation | conditional | use relevant system skill first |
| Spreadsheet generation | conditional | use spreadsheet skill and openpyxl/artifact_tool |

## Upgrade rule

Every new capability must include:

1. Trigger condition
2. Inputs
3. Procedure
4. Evidence output
5. Failure mode
6. Recovery path
