#!/usr/bin/env python3
"""Validate selected Git blobs for CRLF line endings and no BOM.

This script checks committed blobs, not only working-tree files.
It is designed for the ai-team-ops repo after the CRLF/raw-reader issue.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

TARGETS = [
    "AGENTS.md",
    "docs/TOOLCHAIN_ROADMAP.md",
    "skills/novel_ops/SKILL.md",
    "skills/evidence_ops/SKILL.md",
]


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


def main() -> int:
    ref = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    commit = subprocess.check_output(["git", "rev-parse", ref], text=True).strip()
    result = {"commit": commit, "files": {}}
    ok = True

    for path in TARGETS:
        data = git_blob_bytes(ref, path)
        item = analyze(data)
        result["files"][path] = item
        if item["blob_splitlines"] <= 2:
            ok = False
        if item["crlf_count"] <= 0:
            ok = False
        if item["lf_only_count"] != 0:
            ok = False
        if item["bom_present"]:
            ok = False

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
