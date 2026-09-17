#!/usr/bin/env python3
"""Cycle 16 build-3 — the at-rest instrument for acceptance check (4) Lane, census half
(brief F17; §Verification 9).

Phase 1 runs `skills/vlt-lint/scripts/lint-page-facts.py --web-census` FOR REAL over
`build-3-web-census/` (real files on disk) and compares its JSON and its `--web-census-line`
to the HAND-WRITTEN oracle `build-3-expected-web-census.json` — written before the script was
ever run. The fixture carries every form that must count (quoted and unquoted URLs, flow and
block sequences, `sources:` and `grounding:`, both keys on one file) and every control that
must not (a wikilink entry, a bare `.md` path, a URL in a prose `## Sources` section, a
`sources:` scalar, a file with no frontmatter).

Phase 2 runs the persist gate over a rendered report and asserts it ACCEPTS the instrument's
line and REJECTS an off-by-one — the recount is by string equality, so a hand-composed census
cannot land.

Run: python3 factory/cycles/16-closed-loops/fixtures/build-3-web-census-harness.py
"""
import json
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
C15 = os.path.join(REPO, "factory", "cycles", "15-nothing-reads-it-back", "fixtures")
FACTS = os.path.join(REPO, "skills", "vlt-lint", "scripts", "lint-page-facts.py")
GATE = os.path.join(REPO, "skills", "vlt-lint", "scripts", "lint-report-check.py")
FIXTURE = os.path.join(HERE, "build-3-web-census")
ORACLE = os.path.join(HERE, "build-3-expected-web-census.json")
PARA = os.path.join(C15, "build-5-para")
WIKI = os.path.join(HERE, "build-1-wiki")
INDEX = os.path.join(WIKI, "index.md")
OK_REPORT = os.path.join(C15, "build-5-report-ok.yaml")

failures = 0


def check(label, ok, detail=""):
    global failures
    if not ok:
        failures += 1
    print("%s  %s%s" % ("PASS" if ok else "FAIL", label, (" — " + detail) if detail else ""))


def py(args):
    for runner in (["uv", "run", "--quiet"], ["python3"]):
        try:
            return subprocess.run(runner + args, capture_output=True, text=True)
        except FileNotFoundError:
            continue
    raise SystemExit("neither uv nor python3 is available")


print("phase 1 — --web-census over build-3-web-census/ vs the hand-written oracle")
oracle = json.load(open(ORACLE, encoding="utf-8"))
r = py([FACTS, "--web-census", FIXTURE])
data = json.loads(r.stdout)
root = os.path.realpath(FIXTURE)
per = {os.path.relpath(k, root): v for k, v in data["webEntries"].items()}
unp = sorted(os.path.relpath(k, root) for k in data["webUnparsed"])
check("counts equal the oracle", data["counts"] == oracle["counts"], json.dumps(data["counts"]))
check("per-file entries equal the oracle", per == oracle["perFile"], json.dumps(per, sort_keys=True))
check("the unparsed set equals the oracle", unp == sorted(oracle["unparsed"]), json.dumps(unp))
line = py([FACTS, "--web-census", FIXTURE, "--web-census-line"]).stdout.strip()
check("--web-census-line equals the oracle line", line == oracle["line"], line)
r = py([FACTS, "--web-census", os.path.join(FIXTURE, "no-such-dir")])
check("a missing directory exits 2 (never reads as zero)", r.returncode == 2, "exit %d" % r.returncode)

print("\nphase 2 — the persist gate recounts web_cited_entries: by string equality")
DIRS = [os.path.join(PARA, "projects"), os.path.join(PARA, "areas"), os.path.join(PARA, "resources")]
gate_dirs = []
for d in DIRS:
    gate_dirs += ["--dir", d]
gate_dirs += ["--exclude", os.path.join(PARA, "resources", "wiki"), "--root", PARA]
web_line = py([FACTS, "--web-census"] + DIRS + [WIKI, "--web-census-line"]).stdout.strip()
bare_line = py([FACTS, "--census", WIKI, "--census-exclude", INDEX, "--census-line"]).stdout.strip()
report = open(OK_REPORT, encoding="utf-8").read()
report = "\n".join(l for l in report.split("\n") if not l.startswith("  bare_path_sources:"))
anchor = "  attestation_census: {pages_total: 1, fresh: 0, stale: 0, unattested_pre_adoption: 1}\n"
if anchor not in report:
    raise SystemExit("build-5-report-ok.yaml anchor moved — fix the harness")


def rendered(web):
    return report.replace(anchor, anchor + '  bare_path_sources: "%s"\n  web_cited_entries: "%s"\n' % (bare_line, web))


def run_gate(text):
    fd, path = tempfile.mkstemp(suffix=".yaml")
    os.write(fd, text.encode("utf-8"))
    os.close(fd)
    r = py([GATE, "check", "--report", path, "--mode", "full"] + gate_dirs + ["--wiki-dir", WIKI, "--wiki-exclude", INDEX])
    os.unlink(path)
    try:
        return r.returncode, json.loads(r.stdout)
    except Exception:
        return r.returncode, {"stderr": r.stderr.strip()}

code, out = run_gate(rendered(web_line))
check("the instrument's line is ACCEPTED", code == 0 and out.get("status") == "ok", json.dumps(out))
off = re.sub(r"^(\d+)", lambda m: str(int(m.group(1)) + 1), web_line)
code, out = run_gate(rendered(off))
check("an off-by-one is REJECTED, by its own reason",
      code == 1 and "web_cited_entries: rendered line does not match the recount" in (out.get("reason") or ""),
      json.dumps(out.get("reason")))
code, out = run_gate(rendered(web_line).replace('  web_cited_entries: "%s"\n' % web_line, ""))
check("a missing web_cited_entries: in full mode is REJECTED",
      code == 1 and "key missing: flag_for_human.web_cited_entries" in (out.get("reason") or ""),
      json.dumps(out.get("reason")))

print("\n%s" % ("%d expectation(s) FAILED" % failures if failures else "all expectations hold"))
sys.exit(1 if failures else 0)
