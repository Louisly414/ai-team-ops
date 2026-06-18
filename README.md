# ai-team-ops

AI Team Operations repository for the 玄策 team.

This repo is the shared rule, skill, evaluation, and evidence hub for multi-agent collaboration.

## Core rule

Do not trust chat memory as completion evidence.

A task is complete only when its evidence satisfies the relevant rule, for example:

```json
{
  "status": "completed",
  "result": {
    "ok": true
  }
}
```

For file reads, also verify:

```json
{
  "truncated": false
}
```

## Directory map

```text
AGENTS.md                 Team roles and collaboration rules
skills/                   Skill definitions
skills/novel_ops/         Novel/content workflow
skills/evidence_ops/      Evidence and completion rules
skills/research_ops/      Research workflow
skills/code_review/       Code review workflow
skills/artifact_ops/      Docs/slides/sheets workflow wrapper
evals/                    Evaluation rubrics
docs/                     Toolchain and GitHub docs
tasks/                    Task records
evidence/                 Evidence manifests
scripts/                  Local validation scripts
.github/                  GitHub issue, PR, and workflow files
```

## Current hardening

The repo includes a blob line-ending manifest because some raw readers display LF/CRLF files as 1-2 visual lines.

Use `scripts/check_blob_line_endings.py` and the `linecheck` GitHub workflow to verify the committed blob state.

## Normal workflow

1. Create or update a task.
2. Assign an owner.
3. Change files.
4. Run local checks.
5. Commit and push.
6. Use evidence paths or manifests for acceptance.
