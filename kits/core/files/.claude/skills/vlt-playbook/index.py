#!/usr/bin/env python3
"""The playbook index, read from each playbook's own frontmatter.

    python3 .claude/skills/vlt-playbook/index.py           # need -> playbook table (markdown)
    python3 .claude/skills/vlt-playbook/index.py --check   # exit 1 if a file breaks the convention

The convention lives in resources/playbooks/README.md. A playbook carries `need:`,
`state: live | dormant`, `domain:` and, when it has scripts, `tools:`; a companion carries
`companion_of: <playbook>.md` instead. The allowed domains are the `domains:` list in the
README's frontmatter, so the vault owns the set.
Stdlib only. Finds the vault from its own location, so the working directory does not matter.
"""
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
REL = "resources/playbooks"
FOLDER = VAULT / REL
TOOLS_HOME = "_agent/tools/"
STATES = ("live", "dormant")
SECTIONS = ("Prerequisites", "Commands", "Procedure", "Output", "Schedule", "Rules", "Known gaps")


def frontmatter(path):
    """Top-level keys as strings. A YAML block list under a key is joined with commas."""
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    out, key = {}, None
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith((" ", "\t")) and line.strip().startswith("- ") and key:
            item = line.strip()[2:].strip().strip("\"'")
            out[key] = f"{out[key]}, {item}" if out[key] else item
        elif ":" in line and not line.startswith((" ", "\t", "#", "-")):
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            out[key] = value
    return out


def listed(value):
    return [v.strip().strip("\"'") for v in value.strip("[]").split(",") if v.strip()]


def domains():
    readme = FOLDER / "README.md"
    return listed(frontmatter(readme).get("domains", "")) if readme.is_file() else []


def load():
    allowed = domains()
    playbooks, companions, problems = [], {}, []
    if not FOLDER.is_dir():
        return playbooks, companions, [f"{REL}/ does not exist"], allowed
    if not allowed:
        problems.append("README.md: no domains: list in its frontmatter (the allowed domain: values)")
    for path in sorted(FOLDER.glob("*.md")):
        if path.name == "README.md":
            continue
        fm = frontmatter(path)
        parent = fm.get("companion_of")
        if parent:
            if not (FOLDER / parent).is_file():
                problems.append(f"{path.name}: companion_of names {parent}, which is not in the folder")
            if fm.get("need"):
                problems.append(f"{path.name}: a companion carries no need: (its playbook is the entry point)")
            companions.setdefault(parent, []).append(path.name)
            continue
        if not fm.get("need"):
            problems.append(f"{path.name}: no need: (or companion_of:) in frontmatter")
        if fm.get("state") not in STATES:
            problems.append(f"{path.name}: state: must be one of {', '.join(STATES)}")
        if allowed and fm.get("domain") not in allowed:
            problems.append(f"{path.name}: domain: must be one of {', '.join(allowed)}")
        for tool in listed(fm.get("tools", "")):
            if not tool.startswith(TOOLS_HOME):
                problems.append(f"{path.name}: tools: names {tool}, which is not under {TOOLS_HOME}")
            elif not (VAULT / tool).exists():
                problems.append(f"{path.name}: tools: names {tool}, which does not exist")
        playbooks.append((path.name, fm))
    return playbooks, companions, problems, allowed


def unshaped(playbooks):
    """Playbooks that use none of the convention's section names (a note, never a failure)."""
    out = []
    for name, _ in playbooks:
        text = (FOLDER / name).read_text(encoding="utf-8", errors="replace")
        if not any(f"\n## {s}" in text for s in SECTIONS):
            out.append(name)
    return out


def table(playbooks, companions, allowed):
    rows = ["| Domain | Need | Read |", "|---|---|---|"]

    def order(item):
        name, fm = item
        domain = fm.get("domain")
        return (allowed.index(domain) if domain in allowed else len(allowed), fm.get("state") != "live", name)

    for name, fm in sorted(playbooks, key=order):
        read = f"`{REL}/{name}`"
        for extra in companions.get(name, []):
            read += f", then `{extra}`"
        need = fm.get("need") or "(no need: line)"
        if fm.get("state") == "dormant":
            need += " *(dormant: read its top callout first)*"
        rows.append(f"| {fm.get('domain') or '?'} | {need} | {read} |")
    return "\n".join(rows)


def main():
    playbooks, companions, problems, allowed = load()
    if "--check" in sys.argv:
        for p in problems:
            print(p)
        for name in unshaped(playbooks):
            print(f"note: {name} uses none of the convention's section names")
        print(f"{len(playbooks)} playbooks, {sum(len(v) for v in companions.values())} companions, "
              f"{len(problems)} problems")
        return 1 if problems else 0
    print(table(playbooks, companions, allowed))
    return 0


if __name__ == "__main__":
    sys.exit(main())
