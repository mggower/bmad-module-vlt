#!/usr/bin/env python3
"""vlt vitals reader — the enforcement kit's derive-only instrument (build B5-9).

THE SHARED MEASUREMENT SUBSTRATE (arc-5 pre-ideation ruling 1) lives HERE.
Re-homed from tools/cost-manifest.py by B5-9 so both consumers — the factory
instrument and an installed vault — read one substrate; cost-manifest.py
imports these functions and never re-declares them. Installed to
{root}/.claude/hooks/ (module-owned code home — Arc-3 decide-once ruling 1,
beside the workflows force-reinstall precedent): overwritten on every
install/update, never vault-edited.

Stdlib-only, read-only, derive-only: NO mutable stored counters anywhere —
every figure is derived fresh from existing vault records (091003's recorded
design invariant). The canonical metric vocabulary is the METRICS table below:
registry wires and convention `enforcement_counter:` values must name these
ids and no others (the enforcement kit's one vocabulary).

Modes:
  (default)  print the full vitals report — every metric with its value, the
             derive-only banner, and each registry wire's state.
  --strip    print AT MOST ONE LINE: tripped wires (and wire errors) only;
             nothing at all when green; `vitals unavailable (<reason>)` on any
             read/parse failure — never an empty healthy-looking line.

Exit: 0 = vitals derived (tripped or green); 1 = reader failure (the strip
prints `vitals unavailable` and the hook stays loud, not silent-green).
"""

import argparse
import datetime
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Tolerant {log} header parser, per the contract's declared machine-read
# grammar (vault-operating-contract.md "The {log} — chronological record"):
#   ## [YYYY-MM-DD HH:MM] <type> (<partner>) | <summary> [→ <artifacts>]
# Tolerances (A5-19's residual probe: strict parsing drops ~5% of real
# headers; the contract mandates parsers be case-insensitive and
# paren-tolerant of history): case-insensitive type; paren optional. The
# trailing "|" stays required so a non-header "## " line cannot match.
# ---------------------------------------------------------------------------
LOG_HEADER_RE = re.compile(
    r"^##\s*\[([^\]]+)\]\s*([A-Za-z][A-Za-z0-9_-]*)\s*(?:\(\s*([^)]*?)\s*\))?\s*\|",
    re.IGNORECASE,
)
# Fallback shape seen in real logs: the bracket swallowed type and partner —
# `## [2026-07-18 track (chess-coach)] | …`. The type must start with a letter,
# so a well-formed `[YYYY-MM-DD HH:MM]` bracket can never match this one.
LOG_HEADER_FALLBACK_RE = re.compile(
    r"^##\s*\[([^\]\s]+(?:\s+[^\]\s]+)*?)\s+([A-Za-z][A-Za-z0-9_-]*)\s*(?:\(\s*([^)]*?)\s*\))?\s*\]\s*\|",
    re.IGNORECASE,
)
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")


def parse_log_entries(text):
    """Parse {log} text -> list of entries, file order (the log is append-only).

    Each entry: {"date": "YYYY-MM-DD" or None, "type": lowercased str,
    "partner": lowercased str or None, "start": char offset of the header}.
    Derive-only: no thresholds, no judgments.
    """
    entries = []
    offset = 0
    for line in text.splitlines(keepends=True):
        m = LOG_HEADER_RE.match(line) or LOG_HEADER_FALLBACK_RE.match(line)
        if m:
            date_m = DATE_RE.search(m.group(1))
            partner = m.group(3)
            entries.append(
                {
                    "date": date_m.group(0) if date_m else None,
                    "type": m.group(2).lower(),
                    "partner": partner.strip().lower() if partner and partner.strip() else None,
                    "start": offset,
                }
            )
        offset += len(line)
    return entries


def parse_block_map(lines, section_path):
    """Extract a flat `key: value` block map nested under section_path.

    A deliberately narrow YAML-subset reader (stdlib-only) for the two
    installer-materialized shapes the substrate needs: `vlt.vault_structure`
    in a vault's _bmad/config.yaml and `vault_structure.default` in
    module.yaml. Walks indentation; skips blanks/comments; strips quotes.
    Returns {} if the section is absent.
    """
    depth = 0
    section_indent = -1
    result = {}
    in_target = False
    for raw in lines:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        stripped = raw.strip()
        if in_target:
            if indent <= section_indent:
                break
            m = re.match(r"^([A-Za-z_][\w-]*):\s*(\S.*)$", stripped)
            if m:
                result[m.group(1)] = m.group(2).strip().strip("'\"")
            continue
        if indent <= section_indent:
            # left the section we were descending through
            depth = 0 if indent == 0 else depth
            section_indent = -1 if indent == 0 else section_indent
        want = section_path[depth]
        if stripped == f"{want}:" or stripped.startswith(f"{want}:"):
            if depth == len(section_path) - 1:
                in_target = True
                section_indent = indent
            else:
                depth += 1
                section_indent = indent
    return result


# Shipped structure-map defaults for the keys the vitals derivations read —
# a minimal mirror of module.yaml `vault_structure.default` (the SSoT) for
# the installed-vault case, where module.yaml is not on disk. An installed
# vault's config.yaml normally carries the full materialized map, so these
# only cover a hand-pruned config. The factory consumer (cost-manifest.py)
# passes module.yaml's parsed map instead, so the SSoT stays authoritative
# where it exists.
DEFAULT_STRUCTURE_MAP = {
    "wiki": "_agent/wiki/",
    "index": "_agent/wiki/index.md",
    "research": "_agent/research/",
    "sessions": "_agent/sessions/",
    "specs": "_agent/specs/",
    "log": "_agent/log.md",
    "backlog": "_agent/backlog.md",
    "partners": "_agent/partners/",
    "capabilities": "_agent/capabilities/",
    "conventions": "_meta/conventions/",
    "overlays": "_agent/conventions/",
    "personas": "_meta/personas/",
    "contract": "_meta/vault-operating-contract.md",
    "upgrade_ledger": "_agent/upgrade-ledger.md",
    "archive": "_archive/",
    "tripwires": "_agent/tripwires.yaml",
    "lint_reports": "_agent/lint-reports/",
}

# The dispatch record's home is deliberately hardcoded, not a structure-map
# key — Arc-3 decide-once ruling 4 (the record is dispatch's own agent-zone
# artifact; the contract documents the fixed home).
DISPATCH_REL = "_agent/dispatch.md"
DECISION_LOG_REL = "_agent/mint/decision-log.md"


def resolve_structure_map(vault_root, default_map=None):
    """Resolve a vault's structure map: vault config first, defaults for any
    missing key (config-override wins).

    default_map=None uses the embedded shipped defaults above; the factory
    instrument passes module.yaml's canonical map instead. Returns
    (map, fallback_keys). Raises FileNotFoundError if the vault has no
    _bmad/config.yaml at all (not a vlt install — a hard error, never a
    silent all-defaults guess).
    """
    config = vault_root / "_bmad" / "config.yaml"
    if not config.is_file():
        raise FileNotFoundError(
            f"no _bmad/config.yaml under {vault_root} — not an installed vault"
        )
    vault_map = parse_block_map(
        config.read_text(encoding="utf-8", errors="replace").splitlines(),
        ["vlt", "vault_structure"],
    )
    defaults = dict(default_map) if default_map is not None else dict(DEFAULT_STRUCTURE_MAP)
    resolved, fallbacks = {}, []
    for key in sorted(set(defaults) | set(vault_map)):
        if key in vault_map:
            resolved[key] = vault_map[key]
        else:
            resolved[key] = defaults[key]
            fallbacks.append(key)
    return resolved, fallbacks


# ---------------------------------------------------------------------------
# THE CANONICAL METRIC VOCABULARY (disposition 5 — the one vocabulary).
# id -> one-line definition. Registry wires and `enforcement_counter:` values
# must name these ids; `vlt-lint`'s counter_unknown_metric flag and
# package-lint C8 both key off this table (they parse it, never re-declare it).
# ---------------------------------------------------------------------------
METRICS = {
    "ingests_since_lint": (
        "count of `ingest` {log} headers after the last `lint` header — OP-DEBT "
        "(the pinned definition; lint Step 0's file-mtime scoping is a different, "
        "co-legitimate 'since last lint'; neither redefines the other)"
    ),
    "days_since_lint": "days since the last `lint` {log} header's date (display-only)",
    "open_pointers": "unchecked `- [ ]` rows in _agent/dispatch.md",
    "oldest_open_pointer_days": (
        "days since the run-header date above the oldest still-open dispatch row"
    ),
    "expired_pages": (
        "pages under {wiki} + {research} whose frontmatter `review_after:` is in the past"
    ),
    "classifier_streak": (
        "consecutive most-recent readable classifier verdicts in "
        "_agent/mint/decision-log.md that are `non-boundary:` (denominated: of M "
        "classifier records; K entries carry no readable verdict)"
    ),
    "log_bytes": "byte size of {log} (display-only size vital)",
    "backlog_bytes": "byte size of {backlog} (display-only size vital)",
    "index_bytes": "byte size of {index} (display-only size vital)",
    "partner_memory_bytes": (
        "total bytes of per-partner identity.md + thread.md + reflexes.md + "
        "capabilities/ under {partners} (display-only size vital)"
    ),
}

WIRE_REQUIRED_FIELDS = ["id", "metric", "threshold", "owner", "moment", "surface_text", "review_after"]
THRESHOLD_RE = re.compile(r"^\s*(>=|<=|==|>|<|≥|≤)\s*(\d+)\s*$")


def parse_wires(text):
    """Parse the tripwires registry's `wires:` list (stdlib YAML-subset).

    Returns (wires, errors): wires = list of flat dicts; errors = loud
    per-wire problem strings (missing required fields — never a silent skip).
    """
    wires, errors = [], []
    current = None
    in_wires = False
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if re.match(r"^wires:\s*$", raw):
            in_wires = True
            continue
        if in_wires and not raw.startswith(" ") and not raw.startswith("-"):
            break  # left the wires: section
        if not in_wires:
            continue
        m = re.match(r"^\s*-\s+([A-Za-z_][\w-]*):\s*(.*)$", raw)
        if m:
            current = {m.group(1): m.group(2).strip().strip("'\"")}
            wires.append(current)
            continue
        m = re.match(r"^\s+([A-Za-z_][\w-]*):\s*(.*)$", raw)
        if m and current is not None:
            current[m.group(1)] = m.group(2).strip().strip("'\"")
    for w in wires:
        missing = [f for f in WIRE_REQUIRED_FIELDS if not w.get(f)]
        if missing:
            errors.append(
                f"wire `{w.get('id', '(no id)')}`: missing required field(s) {', '.join(missing)}"
            )
    return wires, errors


def evaluate_wire(wire, metrics):
    """Evaluate one wire against the derived metrics.

    Returns (state, detail): state in {"tripped", "ok", "error"}. An unknown
    metric id is a LOUD error, never a silent skip; a metric whose value is
    underivable (None) evaluates ok with the reason stated.
    """
    metric_id = wire.get("metric")
    if metric_id not in METRICS:
        return "error", f"unknown metric id `{metric_id}` — not in the canonical table"
    m = THRESHOLD_RE.match(wire.get("threshold", ""))
    if not m:
        return "error", f"unparseable threshold `{wire.get('threshold')}` (want e.g. `>= 10`)"
    op = {"≥": ">=", "≤": "<="}.get(m.group(1), m.group(1))
    bound = int(m.group(2))
    value = metrics.get(metric_id)
    if value is None:
        return "ok", f"{metric_id} underivable on this vault (no record yet) — not tripped"
    tripped = {
        ">=": value >= bound, "<=": value <= bound,
        ">": value > bound, "<": value < bound, "==": value == bound,
    }[op]
    return ("tripped" if tripped else "ok"), f"{metric_id} {value} {op} {bound}"


# ---------------------------------------------------------------------------
# Derivations (all read-only; every figure fresh from the record)
# ---------------------------------------------------------------------------


def _days_since(date_str, today):
    try:
        d = datetime.date.fromisoformat(date_str)
    except (TypeError, ValueError):
        return None
    return (today - d).days


def _read_frontmatter_review_after(path):
    """Return the `review_after:` date string from a file's frontmatter, or None."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    if not text.startswith("---"):
        return None
    lines = text.split("\n")
    for line in lines[1:60]:
        if line.strip() == "---":
            break
        m = re.match(r"^review_after:\s*[\"']?(\d{4}-\d{2}-\d{2})", line.strip())
        if m:
            return m.group(1)
    return None


def _dir_bytes(directory):
    if not directory.is_dir():
        return 0
    return sum(p.stat().st_size for p in directory.rglob("*") if p.is_file())


def derive_metrics(vault_root, smap, today=None):
    """Derive every canonical metric. Returns (metrics, notes, partner_rows).

    metrics: id -> int or None (underivable — stated, never silently zeroed).
    notes: per-metric honesty notes (absent records, blind-spot counts).
    partner_rows: per-partner size breakdown for the display block.
    """
    today = today or datetime.date.today()
    metrics, notes = {}, {}

    # {log}-derived: ingests_since_lint (op-debt) + days_since_lint.
    log_path = vault_root / smap["log"].rstrip("/")
    if not log_path.is_file():
        raise FileNotFoundError(f"{smap['log']} missing — the {{log}} is the substrate's primary record")
    log_text = log_path.read_text(encoding="utf-8", errors="replace")
    entries = parse_log_entries(log_text)
    last_lint_idx = None
    for i, e in enumerate(entries):
        if e["type"] == "lint":
            last_lint_idx = i
    after = entries if last_lint_idx is None else entries[last_lint_idx + 1:]
    metrics["ingests_since_lint"] = sum(1 for e in after if e["type"] == "ingest")
    if last_lint_idx is None:
        metrics["days_since_lint"] = None
        notes["days_since_lint"] = "no `lint` header in {log} — never linted (all ingests count)"
        notes["ingests_since_lint"] = "no `lint` baseline — every ingest header counts"
    else:
        metrics["days_since_lint"] = _days_since(entries[last_lint_idx]["date"], today)
        if metrics["days_since_lint"] is None:
            notes["days_since_lint"] = "last `lint` header carries no parseable date"
    metrics["log_bytes"] = len(log_text.encode("utf-8"))

    # Dispatch-derived: open_pointers + oldest_open_pointer_days. The path is
    # hardcoded per Arc-3 ruling 4 (see DISPATCH_REL above).
    dispatch = vault_root / DISPATCH_REL
    if dispatch.is_file():
        open_count = 0
        oldest_days = None
        current_date = None
        for line in dispatch.read_text(encoding="utf-8", errors="replace").splitlines():
            hm = re.match(r"^##\s*\[(\d{4}-\d{2}-\d{2})", line)
            if hm:
                current_date = hm.group(1)
                continue
            if re.match(r"^-\s*\[ \]", line):
                open_count += 1
                d = _days_since(current_date, today)
                if d is not None and (oldest_days is None or d > oldest_days):
                    oldest_days = d
        metrics["open_pointers"] = open_count
        metrics["oldest_open_pointer_days"] = oldest_days if open_count else 0
        if open_count and oldest_days is None:
            notes["oldest_open_pointer_days"] = "open rows found under no dated run header — age underivable"
            metrics["oldest_open_pointer_days"] = None
    else:
        metrics["open_pointers"] = 0
        metrics["oldest_open_pointer_days"] = 0
        notes["open_pointers"] = "no _agent/dispatch.md — dispatch has never run (a zero of zero rows)"

    # expired_pages over {wiki} + {research}.
    expired = 0
    scanned = 0
    for zone_key in ("wiki", "research"):
        zone = vault_root / smap[zone_key].rstrip("/")
        if not zone.is_dir():
            continue
        for page in sorted(zone.rglob("*.md")):
            scanned += 1
            ra = _read_frontmatter_review_after(page)
            if ra is not None:
                d = _days_since(ra, today)
                if d is not None and d > 0:
                    expired += 1
    metrics["expired_pages"] = expired
    notes["expired_pages"] = (
        f"{scanned} pages scanned; a page without `review_after:` is evergreen and cannot expire"
    )

    # classifier_streak from the mint decision log (disposition 6): streak of
    # consecutive most-recent READABLE classifier verdicts that are
    # `non-boundary:`; M = readable classifier records; K = entries with no
    # readable verdict (pre-schema, pre-ref, or verdict-in-planning-doc — the
    # decision-log convention's two-tier tail, surfaced, never swept).
    dlog = vault_root / DECISION_LOG_REL
    streak, m_records, k_unreadable = 0, 0, 0
    if dlog.is_file():
        text = dlog.read_text(encoding="utf-8", errors="replace")
        blocks = re.split(r"(?m)^## \[", text)[1:]  # file order = oldest first
        verdicts = []  # file-order list of "non-boundary" | "boundary"
        for block in blocks:
            has_kind = re.search(r"(?m)^-\s*kind:", block)
            is_mint = re.search(r"(?m)^-\s*kind:\s*mint\b", block)
            if not has_kind:
                k_unreadable += 1  # pre-schema — cannot be ruled out as a mint
                continue
            if not is_mint:
                continue  # a non-mint entry carries no classifier verdict by design
            if re.search(r"non-boundary:", block):
                verdicts.append("non-boundary")
            elif re.search(r"(?m)\bboundary:", block):
                verdicts.append("boundary")
            else:
                k_unreadable += 1  # gated mint whose verdict lives only in its planning doc, or pre-ref
        m_records = len(verdicts)
        for v in reversed(verdicts):
            if v == "non-boundary":
                streak += 1
            else:
                break
        metrics["classifier_streak"] = streak
        notes["classifier_streak"] = (
            f"of {m_records} classifier records; {k_unreadable} entries carry no readable verdict"
        )
    else:
        metrics["classifier_streak"] = 0
        notes["classifier_streak"] = "no _agent/mint/decision-log.md — 0 classifier records (a zero of zero)"

    # Size vitals (disposition 8 — display-only; no rollover machinery).
    for key, metric_id in (("backlog", "backlog_bytes"), ("index", "index_bytes")):
        p = vault_root / smap[key].rstrip("/")
        metrics[metric_id] = p.stat().st_size if p.is_file() else 0
        if not p.is_file():
            notes[metric_id] = f"{smap[key]} absent"
    partner_rows = []
    partners_dir = vault_root / smap["partners"].rstrip("/")
    total_partner = 0
    if partners_dir.is_dir():
        for pdir in sorted(p for p in partners_dir.iterdir() if p.is_dir()):
            n = sum(
                (pdir / f).stat().st_size
                for f in ("identity.md", "thread.md", "reflexes.md")
                if (pdir / f).is_file()
            ) + _dir_bytes(pdir / "capabilities")
            partner_rows.append((pdir.name, n))
            total_partner += n
    metrics["partner_memory_bytes"] = total_partner
    return metrics, notes, partner_rows


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

BANNER = (
    "Derive-only: no stored counters exist anywhere — every figure above is "
    "derived fresh from the vault's own records at read time (the enforcement "
    "kit's design invariant)."
)


def load_registry(vault_root, smap):
    """Read {tripwires}. Absent registry = zero wires, said plainly (a fresh
    vault before seeding), never an error. Returns (wires, wire_errors, note)."""
    reg = vault_root / smap["tripwires"]
    if not reg.is_file():
        return [], [], f"no registry at {smap['tripwires']} — zero wires (a fresh vault before `vlt-setup` seeds it)"
    wires, errors = parse_wires(reg.read_text(encoding="utf-8", errors="replace"))
    return wires, errors, None


def render_report(vault_root, smap, fallbacks):
    metrics, notes, partner_rows = derive_metrics(vault_root, smap)
    wires, wire_errors, reg_note = load_registry(vault_root, smap)
    out = ["# vlt vitals", ""]
    out.append(f"> {BANNER}")
    out.append("")
    out.append("## Metrics (the canonical vocabulary — the only legal wire / enforcement_counter ids)")
    out.append("")
    for metric_id, definition in METRICS.items():
        value = metrics.get(metric_id)
        shown = "n/a" if value is None else f"{value:,}" if isinstance(value, int) else str(value)
        line = f"- `{metric_id}`: **{shown}** — {definition}"
        if metric_id in notes:
            line += f" [{notes[metric_id]}]"
        out.append(line)
    if partner_rows:
        out.append("")
        out.append("Per-partner memory bytes (identity.md + thread.md + reflexes.md + capabilities/):")
        for name, n in partner_rows:
            out.append(f"  - {name}: {n:,}")
    out.append("")
    out.append(f"## Wires ({smap['tripwires']})")
    out.append("")
    if reg_note:
        out.append(f"- {reg_note}")
    for err in wire_errors:
        out.append(f"- ⚠ WIRE ERROR: {err}")
    tripped_count = 0
    for w in wires:
        state, detail = evaluate_wire(w, metrics)
        if state == "tripped":
            tripped_count += 1
            out.append(f"- ⚠ `{w['id']}` TRIPPED — {detail} (owner {w.get('owner')}): {w.get('surface_text')}")
        elif state == "error":
            out.append(f"- ⚠ `{w.get('id', '(no id)')}` ERROR — {detail}")
        else:
            out.append(f"- `{w['id']}` ok — {detail}")
    if wires:
        out.append("")
        out.append(f"{tripped_count} of {len(wires)} wires tripped.")
    if fallbacks:
        out.append("")
        out.append(f"(Structure-map keys resolved from shipped defaults, not the vault's config: {', '.join(fallbacks)}.)")
    return "\n".join(out)


def render_strip(vault_root, smap):
    """At most one line: tripped wires + wire errors only; empty string when green."""
    metrics, _notes, _rows = derive_metrics(vault_root, smap)
    wires, wire_errors, _reg_note = load_registry(vault_root, smap)
    parts = []
    for err in wire_errors:
        parts.append(f"wire error — {err}")
    for w in wires:
        state, detail = evaluate_wire(w, metrics)
        if state == "tripped":
            value = metrics.get(w["metric"])
            parts.append(f"{w['id']}: {value} {w.get('surface_text')} (wire {w.get('threshold')})")
        elif state == "error":
            parts.append(f"{w.get('id', '(no id)')}: wire error — {detail}")
    if not parts:
        return ""
    return "⚠ " + " · ".join(parts)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "vlt vitals reader — derives the enforcement kit's metrics from vault "
            "records and evaluates the tripwire registry. Read-only; derive-only."
        )
    )
    parser.add_argument("--strip", action="store_true", help="session strip: ≤1 line, tripped wires only, silent when green")
    parser.add_argument("--vault", metavar="PATH", default=".", help="vault root (default: cwd — hooks run at the project root)")
    args = parser.parse_args()

    vault_root = Path(args.vault).resolve()
    try:
        smap, fallbacks = resolve_structure_map(vault_root)
        if args.strip:
            line = render_strip(vault_root, smap)
            if line:
                print(line)
        else:
            print(render_report(vault_root, smap, fallbacks))
    except Exception as e:  # fail LOUD, never silent-green
        if args.strip:
            print(f"vitals unavailable ({e})")
        else:
            print(f"vlt-vitals: error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
