# self_upgrade_ops — Capability Upgrade Protocol

## When to use

Use this skill when the user asks to improve, expand, harden, benchmark, or compare the assistant/team capabilities.

## Principles

- Do not claim model-level changes.
- Upgrade workflows, skills, tests, tools, and evidence paths.
- Prefer official docs and current sources for changing platform facts.
- Convert insights into repo files and regression checks.

## Upgrade loop

1. Read current evidence or repo state.
2. Identify capability gap.
3. Map gap to file changes.
4. Add or update a skill.
5. Add or update an eval.
6. Add automation where possible.
7. Add evidence/manifest for verification.
8. Document limitations.

## Required output

Every upgrade pack should include:

- target files
- exact content or patch
- local check command
- commit message
- acceptance criteria

## Scorecard dimensions

- evidence reliability
- GitHub workflow integration
- RPA safety
- code review quality
- artifact generation
- research freshness
- project continuity
- failure honesty
- handoff clarity
- regression test coverage
