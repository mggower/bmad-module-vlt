#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml"]
# ///
"""Cycle 15 build-5 at-rest harness — acceptance checks (1)-(5) of
`briefs/build-5-persisted-report.md` (+ rows (7a)–(7e), build-7's `para_writer_scan:` line — `briefs/build-7-roster-closure-retired.md` F6), run against the shipped persist gate
(`skills/vlt-lint/scripts/lint-report-check.py`) and walker (`lint-para-facts.py`).

Every specimen is a MUTATION of `build-5-report-ok.yaml` (or of the shipped `report.md` fence,
fed through `--schema`). The failable proof: each planted defect flips exactly its own row —
the unmutated report passes, and the mutated-fence cases move the verdict in both directions
((2b) a removed key stops being mandated, (2c) an added key starts being). There is no pre-build
script to run this against; the gate refusing the pre-build fence (`171feb8`'s `report.md`,
17 top-level keys, below the floor) is recorded in the BUILT status, not here.

Run: uv run --quiet factory/cycles/15-nothing-reads-it-back/fixtures/build-5-shape-harness.py
Exit 0 when every row passes; 1 otherwise. Writes only under a temp dir it removes.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
GATE = os.path.join(REPO, "skills", "vlt-lint", "scripts", "lint-report-check.py")
WALKER = os.path.join(REPO, "skills", "vlt-lint", "scripts", "lint-para-facts.py")
REPORT_MD = os.path.join(REPO, "skills", "vlt-lint", "references", "report.md")
PARA = os.path.join(HERE, "build-5-para")
OK_REPORT = os.path.join(HERE, "build-5-report-ok.yaml")
SCHEMA_ORACLE = os.path.join(HERE, "build-5-expected-schema.json")
FACTS_ORACLE = os.path.join(HERE, "build-5-expected-para-facts.json")
DIRS = ["--dir", os.path.join(PARA, "projects"), "--dir", os.path.join(PARA, "areas"),
        "--dir", os.path.join(PARA, "resources"), "--exclude", os.path.join(PARA, "resources", "wiki"),
        "--root", PARA]

# the preserved specimens (brief §Acceptance: `specimens: 4/9`)
FRAGMENT_QUOTED = 'research_zone: "145 notes scanned; 24 carry revisit_after:"'
FRAGMENT_UNQUOTED = "research_zone: 145 notes scanned; 24 carry revisit_after:"  # A15-7, line 102
ROLLUP_27 = ("27 PARA files carry a vault type: + author: agent|hybrid with no attestation pair - "
             "ADJUDICATED [2026-08-26] parked-interim (ref: conventions/write-verification.md; upstream "
             "filing #16, open). Count unchanged from the 2026-08-27 sweep. Disposed, not undisposed")  # A15-8 (a)
SAME_N_FORM = "same 2 no-frontmatter files as para_type_unknown above"  # grounding addition (iii)
PROSE_WHERE_EMPTY = "NO FINDINGS, and the zero is not health this run: no container declares writers"  # (iii)

ENTRY_A = '    - "projects/c1/notes-unattested-a.md: vault type project + author agent, no attestation"\n'
ENTRY_B = '    - "projects/c1/notes-unattested-b.md: vault type project + author agent, verified_by without verified_at — not attested"\n'
ENTRY_C = '    - "resources/r1/hybrid-draft.md: vault type resource + author hybrid, no attestation"\n'
THREE = ENTRY_A + ENTRY_B + ENTRY_C

TMP = tempfile.mkdtemp(prefix="build-5-harness-")
ROWS = []


def read(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def write(name, text):
    path = os.path.join(TMP, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return path


def mutate(text, old, new, count=1):
    assert text.count(old) == count, ("mutation site not found exactly %d×: %r" % (count, old[:60]))
    return text.replace(old, new)


def gate(report, mode="full", schema=None, kind="report", python=None, env=None):
    cmd = [python or sys.executable, GATE, "check", "--report", report, "--kind", kind]
    if kind == "report":
        cmd += ["--mode", mode] + DIRS
    if schema:
        cmd += ["--schema", schema]
    p = subprocess.run(cmd, capture_output=True, text=True, env=env)
    try:
        out = json.loads(p.stdout)
    except ValueError:
        out = {"status": "<no json>", "stderr": p.stderr.strip()}
    return p.returncode, out


def row(check, label, passed, detail=""):
    ROWS.append((check, label, passed, detail))


def expect(check, label, cond, detail):
    row(check, label, bool(cond), detail)


OK = read(OK_REPORT)


def reason_has(out, clause):
    return clause in out.get("reason", "")


# ---------------------------------------------------------------- (1) parse
def check_1():
    code, out = gate(write("1a.yaml", mutate(OK, FRAGMENT_QUOTED, FRAGMENT_UNQUOTED)))
    expect("1", "a: A15-7 fragment unquoted → parse:, exit 1", code == 1 and out.get("reason", "").startswith("parse:"), out.get("reason", "")[:70])
    code, out = gate(OK_REPORT)
    expect("1", "b: the same line double-quoted → ok", code == 0 and out["status"] == "ok", json.dumps(out))
    code, out = gate(write("1c.yaml", OK + '\n---\nmode: "full"\n'))
    expect("1", "c: a two-document stream → parse:", code == 1 and out.get("reason", "").startswith("parse:"), out.get("reason", "")[:70])
    # d: the .json render under bare python3 with uv absent from PATH, and no yaml import
    data = yaml.safe_load(OK)
    json_path = write("1d-lint.json", json.dumps(data, ensure_ascii=False, indent=1) + "\n")
    bare_path = "/usr/bin:/bin"
    py3 = shutil.which("python3", path=bare_path)
    uv_present = shutil.which("uv", path=bare_path)
    probe = (
        "import sys, runpy, json\n"
        "sys.argv = [%r, 'check', '--report', %r, '--mode', 'full'] + %r\n"
        "try:\n    runpy.run_path(%r, run_name='__main__')\nexcept SystemExit as e:\n    code = e.code\n"
        "sys.stderr.write('YAML_IMPORTED=%%s EXIT=%%s\\n' %% ('yaml' in sys.modules, code))\n"
    ) % (GATE, json_path, DIRS, GATE)
    p = subprocess.run([py3 or "python3", "-c", probe], capture_output=True, text=True, env={"PATH": bare_path})
    out = {}
    try:
        out = json.loads(p.stdout)
    except ValueError:
        pass
    expect("1", "d: .json render → ok under bare python3 (uv absent from PATH), no yaml import",
           py3 and not uv_present and out.get("status") == "ok" and "YAML_IMPORTED=False EXIT=0" in p.stderr,
           "python3=%s uv=%s %s" % (py3, uv_present, p.stderr.strip()[-60:]))


# ---------------------------------------------------------------- (2) the fence is the schema
def check_2():
    p = subprocess.run([sys.executable, GATE, "schema"], capture_output=True, text=True)
    oracle = read(SCHEMA_ORACLE)
    expect("2", "a: shipped fence parse == build-5-expected-schema.json (deep-equal AND byte-equal)",
           p.returncode == 0 and json.loads(p.stdout) == json.loads(oracle) and p.stdout == oracle,
           "top_level=%s keys=%s" % (json.loads(p.stdout).get("top_level"), len(json.loads(p.stdout).get("keys", {}))))
    fence = read(REPORT_MD)
    # (b) as briefed removes the TOP-LEVEL fixes_applied: — which drops the fence to 17 keys, below the
    # floor disposition 1 sets at this commit's count (18): the floor refuses it, by design (a retirement
    # lowers the floor in the same build). Recorded as a row; the removal direction is proven on a nested key.
    fence_no_fixes = write("2b-report.md", mutate(fence, "fixes_applied: [<summary>, ...]\n", ""))
    no_fixes = mutate(OK, 'fixes_applied:\n  - "NONE — no auto-fixable finding this run"\n', "")
    code, out = gate(write("2b.yaml", no_fixes), schema=fence_no_fixes)
    expect("2", "b: fence minus the top-level fixes_applied → the floor refuses the fence (exit 2, 17 < 18) — deviation (1)",
           code == 2 and "floor" in out.get("reason", ""), out.get("reason", ""))
    fence_no_thin = write("2b2-report.md", mutate(fence, "  thin_pages: [<page>, ...]\n", ""))
    no_thin = mutate(OK, "  thin_pages: []\n", "")
    code_ship, out_ship = gate(write("2b2.yaml", no_thin))
    code_mut, out_mut = gate(write("2b2.yaml", no_thin), schema=fence_no_thin)
    expect("2", "b': fence minus flag_for_human.thin_pages via --schema → the no-thin_pages report fails under the shipped fence, passes under the mutated one",
           code_ship == 1 and reason_has(out_ship, "key missing: flag_for_human.thin_pages") and code_mut == 0, "shipped=%s mutated=%s" % (out_ship.get("reason"), out_mut.get("status")))
    fence_owner = write("2c-report.md", mutate(fence, "fixes_applied: [<summary>, ...]\n", "fixes_applied: [<summary>, ...]\nowner_notes: [<note>, ...]\n"))
    code, out = gate(OK_REPORT, schema=fence_owner)
    expect("2", "c: fence plus owner_notes → ok report fails key missing: owner_notes", code == 1 and reason_has(out, "key missing: owner_notes"), out.get("reason", ""))
    fence_bad = write("2d-report.md", mutate(fence, "fixes_applied: [<summary>, ...]\n", "fixes_applied: [<summary>, ...]\nthis line is not a key\n"))
    code, out = gate(OK_REPORT, schema=fence_bad)
    expect("2", "d: a fence line matching no rule → exit 2 schema_unreadable", code == 2 and out.get("status") == "schema_unreadable", out.get("reason", ""))
    lines = fence.split("\n")
    i = lines.index("```yaml")
    j = lines.index("```", i + 1)
    truncated = "\n".join(lines[: j - 5] + lines[j:])
    code, out = gate(OK_REPORT, schema=write("2e-report.md", truncated))
    expect("2", "e: a fence truncated below the floor → exit 2", code == 2 and "floor" in out.get("reason", ""), out.get("reason", ""))


# ---------------------------------------------------------------- (3) presence + type, never closure
def check_3():
    code, out = gate(write("3a.yaml", mutate(OK, 'fixes_applied:\n  - "NONE — no auto-fixable finding this run"\n', "")))
    expect("3", "a: fixes_applied deleted (A15-8 b) → key missing: fixes_applied", code == 1 and reason_has(out, "key missing: fixes_applied"), out.get("reason", ""))
    code, out = gate(write("3b.yaml", mutate(OK, 'backlog_filed:\n  - "NONE — nothing filed this run"\n', "")))
    expect("3", "b: backlog_filed deleted (A15-8 c) → key missing: backlog_filed", code == 1 and reason_has(out, "key missing: backlog_filed"), out.get("reason", ""))
    code, out = gate(write("3c.yaml", mutate(OK, 'opportunities:\n  high_value_gaps: "unmeasured"\n  near_duplicates: []\n  source_gaps: []\n', "")))
    expect("3", "c: opportunities deleted (grounding ii) → key missing: opportunities, children not re-reported",
           code == 1 and out.get("reason") == "key missing: opportunities", out.get("reason", ""))
    code, out = gate(write("3d.yaml", mutate(OK, 'fixes_applied:\n  - "NONE — no auto-fixable finding this run"\n', 'fixes_applied: "5 fixes applied"\n')))
    expect("3", "d: fixes_applied a string → wrong type (got scalar, expected list)", code == 1 and reason_has(out, "wrong type: fixes_applied (got scalar, expected list)"), out.get("reason", ""))
    scoped = mutate(OK, 'mode: "full"', 'mode: "scoped"')
    code, out = gate(write("3e.yaml", mutate(scoped, 'cost_accounting: {phases: [], not_instrumented: "fixture"}', "cost_accounting: not instrumented (inline run)")), mode="scoped")
    expect("3", "e: the retired scoped literal for cost_accounting → wrong type (got scalar, expected map)", code == 1 and reason_has(out, "wrong type: cost_accounting (got scalar, expected map)"), out.get("reason", ""))
    code, out = gate(write("3f.yaml", mutate(OK, '  spec_candidate_standing: "0 standing candidate(s) — _agent/handoffs/ empty"\n', "")))
    expect("3", "f: spec_candidate_standing absent (the retired no-line rule) → key missing", code == 1 and reason_has(out, "key missing: flag_for_human.spec_candidate_standing"), out.get("reason", ""))
    no_census = mutate(OK, "  attestation_census: {pages_total: 1, fresh: 0, stale: 0, unattested_pre_adoption: 1}\n", "")
    code_s, out_s = gate(write("3g-scoped.yaml", mutate(no_census, 'mode: "full"', 'mode: "scoped"')), mode="scoped")
    code_f, out_f = gate(write("3g-full.yaml", no_census), mode="full")
    expect("3", "g: attestation_census absent → scoped passes; full → key missing",
           code_s == 0 and code_f == 1 and reason_has(out_f, "key missing: flag_for_human.attestation_census"), "scoped=%s full=%s" % (out_s.get("status"), out_f.get("reason")))
    code, out = gate(write("3h.yaml", mutate(OK, 'backlog_filed:\n  - "NONE — nothing filed this run"\n', "backlog_filed:\n")))
    expect("3", "h: backlog_filed with no value (null) → key missing", code == 1 and reason_has(out, "key missing: backlog_filed"), out.get("reason", ""))
    extra = mutate(OK, "rulings_recorded: []\n", 'rulings_recorded: []\ninstrument_findings: []\nscope_note: "fixture"\n')
    extra = mutate(extra, "  thin_pages: []\n", "  thin_pages: []\n  overlay_walk: []\n")
    code, out = gate(write("3i.yaml", extra))
    expect("3", "i: three extra keys at two depths → ok, extra_keys lists them",
           code == 0 and sorted(out.get("extra_keys", [])) == ["flag_for_human.overlay_walk", "instrument_findings", "scope_note"], json.dumps(out.get("extra_keys")))


# ---------------------------------------------------------------- (4) per-file: membership, duplicates, count
def check_4():
    code, out = gate(write("4a.yaml", mutate(OK, THREE, '    - "%s"\n' % ROLLUP_27)))
    expect("4", "a: the 27-file rollup as sole entry → not a member AND count: rendered 1, walk finds 3",
           code == 1 and reason_has(out, "not a member: para_missing_attestation ←") and reason_has(out, "count: para_missing_attestation rendered 1, walk finds 3"), out.get("reason", "")[:120])
    code, out = gate(write("4b.yaml", mutate(OK, "  para_author_unknown: []\n", '  para_author_unknown:\n    - "%s"\n' % SAME_N_FORM)))
    expect("4", "b: 'same N no-frontmatter files as … above' in para_author_unknown → not a member", code == 1 and reason_has(out, "not a member: para_author_unknown ← same 2 no-frontmatter files as para_type_unknown above"), out.get("reason", ""))
    code, out = gate(write("4c.yaml", mutate(OK, "  para_writer_unauthorized: []\n", '  para_writer_unauthorized:\n    - "%s"\n' % PROSE_WHERE_EMPTY)))
    expect("4", "c: a prose sentence where [] belongs → not a member: para_writer_unauthorized", code == 1 and reason_has(out, "not a member: para_writer_unauthorized ←"), out.get("reason", ""))
    code, out = gate(write("4d.yaml", mutate(OK, THREE, ENTRY_A + ENTRY_B)))
    expect("4", "d: three entries minus one → count: rendered 2, walk finds 3 (and nothing else)",
           code == 1 and out.get("reason") == "count: para_missing_attestation rendered 2, walk finds 3", out.get("reason", ""))
    code, out = gate(write("4e.yaml", mutate(OK, ENTRY_C, '    - "resources/wiki/page.md: a page from the carved-out subtree"\n')))
    expect("4", "e: an entry naming the carved-out wiki page → not a member", code == 1 and reason_has(out, "not a member: para_missing_attestation ← resources/wiki/page.md"), out.get("reason", ""))
    code, out = gate(write("4f.yaml", mutate(OK, ENTRY_B, ENTRY_A)))
    expect("4", "f: the same file twice → duplicate", code == 1 and reason_has(out, "duplicate: para_missing_attestation ← projects/c1/notes-unattested-a.md"), out.get("reason", ""))
    code, out = gate(OK_REPORT)
    expect("4", "g: the exact three, each <relpath>: <text> → ok", code == 0 and out.get("walk") == {"P": 9, "M": 3, "D": 5}, json.dumps(out))  # D added by build-7
    scoped_one = mutate(mutate(OK, 'mode: "full"', 'mode: "scoped"'), THREE, ENTRY_A)
    code, out = gate(write("4h.yaml", scoped_one), mode="scoped")
    expect("4", "h: mode scoped with one well-formed entry → ok (membership only, no count)", code == 0, json.dumps(out)[:80])
    code, out = gate(write("4i.yaml", mutate(OK, "9 files walked", "8 files walked")))
    expect("4", "i: para_scan edited by one character → para_scan: rendered line does not match the walk",
           code == 1 and out.get("reason") == "para_scan: rendered line does not match the walk", out.get("reason", ""))
    p = subprocess.run([sys.executable, WALKER] + DIRS + ["--out", "-"], capture_output=True, text=True)
    walk = json.loads(p.stdout)
    m = set(walk["missing_attestation"])
    pop = set(walk["population"])
    not_in_m = {"projects/c1/record.md", "areas/a1/standing-charter.md", "projects/c1/notes-attested.md", "areas/a1/human-note.md"}
    in_m = {"projects/c1/notes-unattested-a.md", "projects/c1/notes-unattested-b.md", "resources/r1/hybrid-draft.md"}
    expect("4", "j: the walk — record/charter-typed/attested/human NOT in M; two agent + one hybrid unattested ARE; nothing from resources/wiki/",
           not (not_in_m & m) and in_m == m and not any(x.startswith("resources/wiki/") for x in pop) and walk == json.loads(read(FACTS_ORACLE)),
           "P=%d M=%d oracle=%s" % (walk["counts"]["P"], walk["counts"]["M"], walk == json.loads(read(FACTS_ORACLE))))


# ---------------------------------------------------------------- (5) fails loudly: the ritual and the record
def check_5():
    lint_reports = os.path.join(TMP, "lint-reports")
    os.makedirs(lint_reports)
    scratch_dir = os.path.join(TMP, "scratch")
    os.makedirs(scratch_dir)
    failing = mutate(OK, THREE, '    - "%s"\n' % ROLLUP_27)
    failing = mutate(failing, FRAGMENT_QUOTED, FRAGMENT_QUOTED)  # the fragment rides inside the block (quoted here; unquoted below)
    scratch = os.path.join(scratch_dir, "attempt-1.yaml")
    with open(scratch, "w", encoding="utf-8") as fh:
        fh.write(failing)
    code, out = gate(scratch)
    expect("5", "a: attempt 1 over the scratch copy → failed, and NO file under {lint_reports}",
           code == 1 and out.get("status") == "failed" and os.listdir(lint_reports) == [], "%s | dir=%s" % (out.get("reason", "")[:50], os.listdir(lint_reports)))
    # attempt 2 fails too (the harness stands in for a SKILL that re-rendered the same defect) → the failed-run record
    block = mutate(failing, FRAGMENT_QUOTED, FRAGMENT_UNQUOTED)  # the A15-7 fragment, unquoted, inside the embedded block
    if not block.endswith("\n"):
        block += "\n"
    record = (
        'status: failed\n'
        'reason: "shape — %s"\n'
        'files_listed: 1\nfiles_checked: 1\nfiles_cached: 0\n'
        'lint_cache: "scanned 1 / cached 0 of 1 pages (fingerprint fixture, written 2026-09-02, rejected 0 of 0 records read, evicted 0 by request)"\n'
        'next: "re-render from the returned workflow object, not re-sweep"\n'
        'unvalidated_report: |\n%s'
    ) % (out.get("reason", "").replace('"', "'"), "".join("  " + l + "\n" for l in block.split("\n")[:-1]))
    rec_scratch = os.path.join(scratch_dir, "attempt-2-failed.yaml")
    with open(rec_scratch, "w", encoding="utf-8") as fh:
        fh.write(record)
    code, out2 = gate(rec_scratch, kind="failed")
    parsed = yaml.safe_load(read(rec_scratch))
    roundtrip = parsed.get("unvalidated_report") == block
    if code == 0:
        shutil.move(rec_scratch, os.path.join(lint_reports, "2026-09-02-1200-lint-failed.yaml"))
    expect("5", "b: the failed-run record (fragment unquoted inside unvalidated_report: |) → check --kind failed ok; parses whole; embedded block round-trips byte-identical",
           code == 0 and out2.get("status") == "ok" and roundtrip and "shape — " in parsed.get("reason", ""), "roundtrip=%s %s" % (roundtrip, json.dumps(out2)))
    names = os.listdir(lint_reports)
    expect("5", "c: no -lint.yaml for that stamp — only the -lint-failed.yaml landed",
           names == ["2026-09-02-1200-lint-failed.yaml"], str(names))
    row("5", "d: the log-line rule is prose — the field leg of check (6)", True, "recorded, not graded here")


# ---------------------------------------------------------------- (7) build-7: the write-posture line (para_writer_scan:)
WRITER_LINE = '  para_writer_scan: "9 judged; 5 under a declaring ancestor; 4 passed on open posture (instrument: scripts/lint-para-facts.py)"\n'


def check_7():
    p = subprocess.run([sys.executable, GATE, "schema"], capture_output=True, text=True)
    schema = json.loads(p.stdout)
    expect("7", "a: the shipped fence (para_writer_scan: nested under flag_for_human) deep-equals the re-derived oracle — 18 top-level, 74 key paths",
           p.returncode == 0 and schema == json.loads(read(SCHEMA_ORACLE)) and schema["top_level"] == 18 and len(schema["keys"]) == 74
           and schema["keys"]["flag_for_human.para_writer_scan"] == {"type": "scalar", "per_file": False, "full_mode_only": False},
           "top_level=%s keys=%s" % (schema.get("top_level"), len(schema.get("keys", {}))))
    code, out = gate(write("7b.yaml", mutate(OK, WRITER_LINE, "")))
    expect("7", "b: para_writer_scan: absent → key missing: flag_for_human.para_writer_scan (both modes; scoped too)",
           code == 1 and reason_has(out, "key missing: flag_for_human.para_writer_scan"), out.get("reason", ""))
    code_s, out_s = gate(write("7b-scoped.yaml", mutate(mutate(OK, WRITER_LINE, ""), 'mode: "full"', 'mode: "scoped"')), mode="scoped")
    expect("7", "b': the same in scoped mode → key missing (never omitted)", code_s == 1 and reason_has(out_s, "key missing: flag_for_human.para_writer_scan"), out_s.get("reason", ""))
    code, out = gate(write("7c.yaml", mutate(OK, "4 passed on open posture", "5 passed on open posture")))
    expect("7", "c: O off by one (D untouched) → para_writer_scan: rendered line does not match the walk, and nothing else",
           code == 1 and out.get("reason") == "para_writer_scan: rendered line does not match the walk", out.get("reason", ""))
    code, out = gate(OK_REPORT)
    p = subprocess.run([sys.executable, WALKER] + DIRS + ["--writer-line"], capture_output=True, text=True)
    expect("7", "d: equal to the walker's --writer-line → ok (walk P 9 / M 3 / D 5)",
           code == 0 and out.get("walk") == {"P": 9, "M": 3, "D": 5} and p.stdout.strip() == "9 judged; 5 under a declaring ancestor; 4 passed on open posture (instrument: scripts/lint-para-facts.py)",
           "%s | %s" % (json.dumps(out.get("walk")), p.stdout.strip()))
    old_fence = subprocess.run(["git", "-C", REPO, "show", "fc44027:skills/vlt-lint/references/report.md"], capture_output=True, text=True).stdout
    code_old, out_old = gate(OK_REPORT, schema=write("7e-report.md", old_fence))
    expect("7", "e: the red leg — the ok report under fc44027's fence → ok with para_writer_scan reported EXTRA (the pre-build fence never mandated it)",
           code_old == 0 and "flag_for_human.para_writer_scan" in out_old.get("extra_keys", []), json.dumps(out_old.get("extra_keys")))


def main():
    try:
        for fn in (check_1, check_2, check_3, check_4, check_5, check_7):
            fn()
    finally:
        shutil.rmtree(TMP, ignore_errors=True)
    width = max(len(r[1]) for r in ROWS)
    failed = 0
    for check, label, passed, detail in ROWS:
        failed += not passed
        print("(%s) %-*s  %s  %s" % (check, width, label, "PASS" if passed else "FAIL", "" if passed else "← " + detail))
    print("\nbuild-5 shape harness: %d rows, %d failed" % (len(ROWS), failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
