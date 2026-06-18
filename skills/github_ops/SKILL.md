# github_ops — GitHub Repository Operations

## When to use

Use this skill when the task involves GitHub repo structure, commits, PRs, workflows, issue templates, Actions, or raw file verification.

## Core boundary

Do not claim direct GitHub write access unless a write-capable tool exists in the current environment.

## Normal workflow

1. Identify repo and branch.
2. Read remote files through raw URLs or connector if available.
3. Compare requested state vs observed state.
4. If direct write is unavailable, produce a repair pack for 鲁班.
5. After 鲁班 pushes, verify remote files and Actions.
6. Write local evidence under `shared_workspace/ai_team_comm/github/`.

## Remote verification checklist

- File raw URL opens.
- Key content exists.
- Workflow appears in Actions if relevant.
- Latest run status is recorded.
- Any warning is recorded separately from failure.

## Failure modes

- Remote raw line count display may be unreliable.
- GitHub CDN may lag branch refs.
- Empty dirs do not exist in Git unless `.gitkeep` is committed.
- Git normalizes text unless `.gitattributes` overrides it.

## Evidence

Store verification in local evidence with:

- repo
- branch or commit
- paths checked
- observed status
- limitations
- next action
