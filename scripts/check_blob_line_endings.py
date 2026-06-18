#!/usr/bin/env python3
"""Validate selected Git blobs for line endings and no BOM.

This script checks committed blobs, not only working-tree files.
It is designed for the ai-team-ops repo after the CRLF/raw-reader issue.

By default, only legacy markdown targets require CRLF bytes. Other targets must
have reasonable line counts and no BOM. Pass --strict-crlf to require CRLF on all.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys

TARGETS = [
    "AGENTS.md",
    "README.md",
    "docs/TOOLCHAIN_ROADMAP.md",
    "docs/GITHUB_WORKFLOW.md",
    "docs/MCP_AND_EXTENSIONS.md",
    "docs/COMPETITOR_LEARNING_NOTES.md",
    "skills/novel_ops/SKILL.md",
    "skills/evidence_ops/SKILL.md",
    "skills/research_ops/SKILL.md",
    "skills/code_review/SKILL.md",
    "skills/artifact_ops/SKILL.md",
    "skills/github_ops/SKILL.md",
    "skills/rpa_ops/SKILL.md",
    "skills/self_upgrade_ops/SKILL.md",
    "evals/generalist_benchmark.md",
    ".github/ISSUE_TEMPLATE/task.yml",
    ".github/pull_request_template.md",
]

CRLF_STRICT_TARGETS = {
    "AGENTS.md",
    "docs/TOOLCHAIN_ROADMAP.md",
    "skills/novel_ops/SKILL.md",
    "skills/evidence_ops/SKILL.md",
}


def git_blob_bytes(ref: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{ref}:{path}"])


def analyze(data: bytes) -> dict:
    text = data.decode("utf-8", errors="replace")
    crlf = data.count(b"\r\n")
    lf = data.count(b"\n")
    return {
        "blob_bytes": len(data),
        "blob_splitlines": len(text.splitlines()),
        "crlf_count": crlf,
        "lf_count": lf,
        "lf_only_count": lf - crlf,
        "bom_present": data.startswith(b"\xef\xbb\xbf"),
        "first_200_repr": repr(text[:200]),
    }


def validate_item(path: str, item: dict, *, strict_crlf: bool) -> list[str]:
    errors: list[str] = []
    min_lines = 2 if path.endswith((".yml", ".yaml")) else 3
    if item["blob_splitlines"] < min_lines:
        errors.append("blob_splitlines_too_low")
    if item["bom_present"]:
        errors.append("bom_present")
    if strict_crlf or path in CRLF_STRICT_TARGETS:
        if item["crlf_count"] <= 0:
            errors.append("crlf_missing")
        if item["lf_only_count"] != 0:
            errors.append("lf_only_present")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check committed blob line endings")
    parser.add_argument("ref", nargs="?", default="HEAD", help="Git ref to inspect")
    parser.add_argument(
        "--strict-crlf",
        action="store_true",
        help="Require CRLF on every target (not just legacy markdown)",
    )
    args = parser.parse_args()

    commit = subprocess.check_output(["git", "rev-parse", args.ref], text=True).strip()
    result = {"commit": commit, "strict_crlf": args.strict_crlf, "files": {}}
    ok = True

    for path in TARGETS:
        data = git_blob_bytes(args.ref, path)
        item = analyze(data)
        item["errors"] = validate_item(path, item, strict_crlf=args.strict_crlf)
        result["files"][path] = item
        if item["errors"]:
            ok = False

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
