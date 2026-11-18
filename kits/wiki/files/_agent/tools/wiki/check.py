#!/usr/bin/env python3
"""Three structural checks on the wiki. Run by _agent/tools/checks/run.py.

    python3 _agent/tools/wiki/check.py

1. Every page carries the four attestation keys, each with a value.
2. A page with superseded_by: names a page that exists.
3. The index and the folder agree: every page has an index row, every index row has a page.

The rules these read are in _meta/wiki.md and _meta/frontmatter.md.
Stdlib only; finds the vault from its own location. Exit 1 on any finding.
"""
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
REL = "resources/wiki"
WIKI = VAULT / REL
ATTESTATION = ("author", "trust", "verified_by", "verified_at")
ROW = re.compile(r"^\s*[-*]\s+\[\[([^\]|#]+)")
BLIND = ("does not check: whether a claim is true or still current, links between pages, "
         "category: against the index headings, or sources: against the sources folder")


def frontmatter(path):
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    out = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return out
        if ":" in line and not line.startswith((" ", "\t", "#", "-")):
            key, _, value = line.partition(":")
            out[key.strip()] = value.strip().strip("\"'")
    return None


def slug(value):
    """A page name from a wikilink, a path or a file name."""
    value = value.strip().strip("\"'").strip("[]").split("|")[0].split("#")[0].strip()
    name = value.rsplit("/", 1)[-1]
    return name[:-3] if name.endswith(".md") else name


def main():
    pages = sorted(p for p in WIKI.rglob("*.md") if p.name != "index.md") if WIKI.is_dir() else []
    stems = {p.stem for p in pages}
    problems = []

    for path in pages:
        fm = frontmatter(path)
        name = path.relative_to(WIKI).as_posix()
        if fm is None:
            problems.append(f"{name}: no readable frontmatter")
            continue
        for key in ATTESTATION:
            if not fm.get(key):
                problems.append(f"{name}: no {key}:")
        successor = fm.get("superseded_by")
        if successor and slug(successor) not in stems:
            problems.append(f"{name}: superseded_by names {slug(successor)}, which is not a page")

    index = WIKI / "index.md"
    if pages and not index.is_file():
        problems.append(f"{REL}/index.md does not exist, so no page has an index row")
    elif index.is_file():
        rows = {slug(m.group(1)) for line in index.read_text(encoding="utf-8", errors="replace").splitlines()
                if (m := ROW.match(line))}
        for path in pages:
            if path.stem not in rows:
                problems.append(f"{path.relative_to(WIKI).as_posix()}: no row in the index")
        for row in sorted(rows - stems):
            problems.append(f"index.md: a row names {row}, which is not a page")

    for p in problems:
        print(p)
    print(f"{len(pages)} pages in {REL}/, {len(problems)} problems; {BLIND}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
