#!/usr/bin/env python3
"""Validate the ai-team-ops repository contract."""

from __future__ import annotations

from pathlib import Path
import sys

REQUIRED = [
    "AGENTS.md",
    "README.md",
    "skills/novel_ops/SKILL.md",
    "skills/evidence_ops/SKILL.md",
    "skills/research_ops/SKILL.md",
    "skills/code_review/SKILL.md",
    "skills/artifact_ops/SKILL.md",
    "skills/github_ops/SKILL.md",
    "skills/rpa_ops/SKILL.md",
    "skills/self_upgrade_ops/SKILL.md",
    "evals/generalist_benchmark.md",
    "docs/TOOLCHAIN_ROADMAP.md",
    "capabilities/CAPABILITY_REGISTRY.md",
    "scripts/check_blob_line_endings.py",
    ".github/workflows/linecheck.yml",
    ".github/ISSUE_TEMPLATE/task.yml",
    ".github/pull_request_template.md",
]

MUST_CONTAIN = {
    "AGENTS.md": ["只认 evidence", "status=completed", "result.ok=true"],
    "README.md": ["Do not trust chat memory", "truncated"],
    "skills/evidence_ops/SKILL.md": ["truncated", "result.ok"],
    "capabilities/CAPABILITY_REGISTRY.md": ["Capability matrix", "Hard boundary"],
}


def main() -> int:
    root = Path.cwd()
    ok = True
    for rel in REQUIRED:
        path = root / rel
        if not path.exists():
            print(f"MISSING {rel}")
            ok = False
            continue
        if path.is_file() and path.stat().st_size == 0:
            print(f"EMPTY {rel}")
            ok = False

    for rel, needles in MUST_CONTAIN.items():
        text = (root / rel).read_text(encoding="utf-8", errors="replace")
        for needle in needles:
            if needle not in text:
                print(f"MISSING_TEXT {rel}: {needle}")
                ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
