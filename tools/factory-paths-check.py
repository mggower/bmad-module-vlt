#!/usr/bin/env python3
"""factory-paths-check: every concrete path a factory skill names must resolve on disk.

Born in P-8 (the cycle + factory/ move) so the reorganization has a gate like every
other build: a factory skill (or CLAUDE.md, or the lifecycle map) that references a
path which does not exist is a broken instruction. Placeholder paths (anything with
<...>, {...}, *, or a bare NN/N template segment) are skipped — the check targets
concrete references only.

Usage: uv run tools/factory-paths-check.py   (exit 0 = every path resolves)
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FACTORY_SKILLS = [
    "acceptance-discharge", "cycle-closeout", "build-brief", "ideation-scaffold",
    "inbox-capture", "issue-triage", "lifecycle-status", "roadmap-roundtable",
    "vlt-release",
]

SCAN_FILES = (
    [p for name in FACTORY_SKILLS
       for p in (ROOT / ".claude" / "skills" / name).rglob("*.md")
       if ".analysis" not in p.parts and p.name != ".memlog.md"]
    + [ROOT / ".claude" / "skills" / "vlt-lifecycle.md", ROOT / "CLAUDE.md"]
)

# Path-like tokens rooted at a directory this repo actually owns.
PATH_RE = re.compile(
    r"(?<![\w/.-])"
    r"((?:factory|tools|skills|\.claude|\.claude-plugin|\.github)/[\w./{}<>*\-]+)"
)

PLACEHOLDER = re.compile(r"[<>{}*]|(?:^|/)(?:NN|N)(?:-|/|$)|X\.Y\.Z|vX\b")


def is_placeholder(token: str) -> bool:
    return bool(PLACEHOLDER.search(token))


def main() -> int:
    missing = []
    checked = 0
    for f in SCAN_FILES:
        rel = f.relative_to(ROOT)
        text = f.read_text(encoding="utf-8", errors="replace")
        for lineno, line in enumerate(text.splitlines(), 1):
            for m in PATH_RE.finditer(line):
                token = m.group(1).rstrip(".,;:)`'\"")
                token = re.sub(r":\d+(?:[-,]\d+)*$", "", token)  # strip file:line refs
                if is_placeholder(token):
                    continue
                checked += 1
                if not (ROOT / token).exists():
                    missing.append((str(rel), lineno, token))
    if missing:
        print(f"factory-paths-check FAIL — {len(missing)} unresolved path(s) "
              f"({checked} checked):")
        for rel, lineno, token in missing:
            print(f"  {rel}:{lineno}  {token}")
        return 1
    print(f"factory-paths-check PASS — {checked} concrete path references resolve "
          f"({len(SCAN_FILES)} files scanned)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
