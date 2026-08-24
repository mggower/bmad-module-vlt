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
design invariant). The enforcement kit's one vocabulary is two-homed (B10-4):
the canonical METRICS table below (module-owned) plus the vault's declarative
`local_metrics:` section in the {tripwires} registry (vault-grown — the
registry header owns that schema). Registry wires and convention
`enforcement_counter:` values must name an id from one of those two homes and
no other. The reader itself stays module-owned, overwrite-on-update; nothing
vault-authored is ever imported or executed — local metrics are DECLARED
(bounded count/size/age kinds), never code.

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
    "wiki": "resources/wiki/",
    "index": "resources/wiki/index.md",
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
# THE CANONICAL METRIC VOCABULARY (disposition 5 — the one vocabulary,
# module-owned half). id -> one-line definition. Registry wires and
# `enforcement_counter:` values must name an id from this table OR from the
# registry's own `local_metrics:` declarations (the {tripwires} header owns
# that schema — B10-4); `vlt-lint`'s counter_unknown_metric flag and
# package-lint C8 both key off this table (they parse it, never re-declare
# it). Vault-local additions to THIS table remain illegal — the durable home
# is the registry's `local_metrics:` section.
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
    "pages_with_review_after": (
        "pages under {wiki} + {research} whose frontmatter carries `review_after:` — "
        "the eligible population `expired_pages` is judged against (its honest denominator)"
    ),
    "classifier_streak": (
        "consecutive most-recent readable classifier verdicts in "
        "_agent/mint/decision-log.md that are `non-boundary:` (denominated: of M "
        "classifier records; K entries carry no readable verdict)"
    ),
    "log_bytes": (
        "byte size of the live {log} (display-only size vital + the `log-mass` "
        "wire; archived segments under {archive} excluded — vitals measure "
        "wake-read mass)"
    ),
    "backlog_bytes": (
        "byte size of the live {backlog} (display-only size vital; archived "
        "segments under {archive} excluded — vitals measure wake-read mass)"
    ),
    "oldest_drainable_section_days": (
        "days since the run-header date of the oldest drain-eligible "
        "_agent/dispatch.md run block — fully closed `daily/`/`relay` block "
        "that is not its source's newest watermark carrier; `consult:` blocks "
        "exempt; 0 when none (display + wire)"
    ),
    "index_bytes": "byte size of {index} (display-only size vital)",
    "partner_memory_bytes": (
        "total bytes of per-partner identity.md + thread.md + reflexes.md + "
        "capabilities/ under {partners} (display-only size vital)"
    ),
}

WIRE_REQUIRED_FIELDS = ["id", "metric", "threshold", "owner", "moment", "surface_text", "review_after"]
THRESHOLD_RE = re.compile(r"^\s*(>=|<=|==|>|<|≥|≤)\s*(\d+)\s*$")

# Local metrics (B10-4): the registry's declarative vault-local vocabulary —
# bounded count/size/age kinds ({tripwires} header owns the schema). A derive
# beyond these kinds routes upstream (a new canonical metric or a new kind),
# never into a hand-edit of this module-owned reader.
LOCAL_METRIC_KINDS = {"file_count", "bytes", "days_since_newest", "frontmatter_key_count"}
LOCAL_METRIC_LOCATOR = {
    "file_count": "glob",
    "bytes": "path",
    "days_since_newest": "glob",
    "frontmatter_key_count": "glob",
}
LOCAL_METRIC_REQUIRED = ["id", "kind", "definition"]


def _parse_flat_entry_list(text, section):
    """Parse one top-level `<section>:` list of flat maps (stdlib YAML-subset —
    the registry's own style; nothing nested)."""
    entries = []
    current = None
    in_section = False
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if re.match(rf"^{re.escape(section)}:\s*$", raw):
            in_section = True
            continue
        if in_section and not raw.startswith(" ") and not raw.startswith("-"):
            in_section = False  # left the section (another top-level key)
        if not in_section:
            continue
        m = re.match(r"^\s*-\s+([A-Za-z_][\w-]*):\s*(.*)$", raw)
        if m:
            current = {m.group(1): m.group(2).strip().strip("'\"")}
            entries.append(current)
            continue
        m = re.match(r"^\s+([A-Za-z_][\w-]*):\s*(.*)$", raw)
        if m and current is not None:
            current[m.group(1)] = m.group(2).strip().strip("'\"")
    return entries


def parse_wires(text):
    """Parse the tripwires registry's `wires:` list (stdlib YAML-subset).

    Returns (wires, errors): wires = list of flat dicts; errors = loud
    per-wire problem strings (missing required fields — never a silent skip).
    """
    wires = _parse_flat_entry_list(text, "wires")
    errors = []
    for w in wires:
        missing = [f for f in WIRE_REQUIRED_FIELDS if not w.get(f)]
        if missing:
            errors.append(
                f"wire `{w.get('id', '(no id)')}`: missing required field(s) {', '.join(missing)}"
            )
    return wires, errors


def parse_local_metrics(text):
    """Parse the registry's optional `local_metrics:` section (B10-4).

    Returns (defs, errors): defs = validly-declared entries only; errors =
    loud per-entry problem strings (missing fields, unknown kind, missing
    locator, an id shadowing the canonical table, a duplicate id — never a
    silent skip; the evaluate_wire posture extended). Zero declarations is
    the normal state, not an error.
    """
    raw_defs = _parse_flat_entry_list(text, "local_metrics")
    defs, errors = [], []
    seen = set()
    for d in raw_defs:
        probs = []
        missing = [f for f in LOCAL_METRIC_REQUIRED if not d.get(f)]
        if missing:
            probs.append(f"missing required field(s) {', '.join(missing)}")
        kind = d.get("kind")
        if kind and kind not in LOCAL_METRIC_KINDS:
            probs.append(
                f"unknown kind `{kind}` (legal kinds: {', '.join(sorted(LOCAL_METRIC_KINDS))} — "
                "a derive beyond them routes upstream)"
            )
        locator = LOCAL_METRIC_LOCATOR.get(kind)
        if locator and not d.get(locator):
            probs.append(f"kind `{kind}` requires a `{locator}:` locator field")
        if kind == "frontmatter_key_count":
            if not d.get("key"):
                probs.append("kind `frontmatter_key_count` requires a `key:` frontmatter-key field")
            elif not re.match(r"^[A-Za-z_][\w-]*$", d["key"]):
                probs.append(
                    f"malformed `key:` `{d['key']}` (want a bare key token, e.g. review_after) — "
                    "a malformed key must not silently count zero"
                )
        if d.get("id") in METRICS:
            probs.append(
                "shadows a canonical metric id — the canonical table stays "
                "authoritative for its own names"
            )
        if d.get("id") in seen:
            probs.append("duplicate local metric id")
        if probs:
            errors.append(f"local metric `{d.get('id', '(no id)')}`: " + "; ".join(probs))
        else:
            seen.add(d["id"])
            defs.append(d)
    return defs, errors


def _resolve_locator(spec, smap):
    """Expand `{key}` structure-map logical names in a locator; the result is
    a vault-relative path/glob. An unknown `{key}` is left in place — the
    caller treats a remaining brace as unresolvable (derives None, reason
    stated)."""
    return re.sub(
        r"\{([A-Za-z_][\w-]*)\}",
        lambda m: smap[m.group(1)].rstrip("/") if m.group(1) in smap else m.group(0),
        spec,
    )


def _read_frontmatter_date(path):
    """First dated frontmatter key (created/date/last_updated) — never mtime
    (git operations and copies corrupt mtimes; the vault's records are dated
    by convention). Returns YYYY-MM-DD or None."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    if not text.startswith("---"):
        return None
    found = {}
    for line in text.split("\n")[1:60]:
        if line.strip() == "---":
            break
        m = re.match(r"^(created|date|last_updated):\s*[\"']?(\d{4}-\d{2}-\d{2})", line.strip())
        if m and m.group(1) not in found:
            found[m.group(1)] = m.group(2)
    for key in ("created", "date", "last_updated"):
        if key in found:
            return found[key]
    return None


def derive_local_metrics(vault_root, smap, defs, today=None):
    """Derive every validly-declared local metric by `kind` (read-only,
    derive-only — the same posture as the canonical derivations). Returns
    (values, notes): values[id] = int or None (unresolvable locator —
    stated, the underivable posture, not an error)."""
    today = today or datetime.date.today()
    values, notes = {}, {}
    for d in defs:
        mid = d["id"]
        kind = d["kind"]
        locator_field = LOCAL_METRIC_LOCATOR[kind]
        spec = _resolve_locator(d[locator_field], smap)
        if "{" in spec:
            values[mid] = None
            notes[mid] = (
                f"locator `{d[locator_field]}` names an unknown structure-map key — underivable"
            )
            continue
        try:
            if kind == "file_count":
                values[mid] = sum(1 for f in vault_root.glob(spec) if f.is_file())
            elif kind == "bytes":
                target = vault_root / spec
                if target.is_file():
                    values[mid] = target.stat().st_size
                elif target.is_dir():
                    values[mid] = _dir_bytes(target)
                else:
                    values[mid] = None
                    notes[mid] = f"{spec} absent — underivable (no record yet)"
            elif kind == "frontmatter_key_count":
                values[mid] = sum(
                    1 for f in vault_root.glob(spec)
                    if f.is_file() and _frontmatter_has_key(f, d["key"])
                )
            elif kind == "days_since_newest":
                newest = None
                matched = 0
                for f in vault_root.glob(spec):
                    if not f.is_file():
                        continue
                    matched += 1
                    m = DATE_RE.search(f.name)
                    date_str = m.group(0) if m else _read_frontmatter_date(f)
                    if date_str is None:
                        continue
                    try:
                        fdate = datetime.date.fromisoformat(date_str)
                    except ValueError:
                        continue
                    if newest is None or fdate > newest:
                        newest = fdate
                if newest is None:
                    values[mid] = None
                    notes[mid] = (
                        f"no dated file matches {spec} ({matched} matched; dates come from "
                        "dated names or frontmatter, never mtime) — underivable"
                    )
                else:
                    values[mid] = (today - newest).days
        except (OSError, ValueError) as e:
            values[mid] = None
            notes[mid] = f"locator `{d[locator_field]}` unreadable ({e}) — underivable"
    return values, notes


def evaluate_wire(wire, metrics, local_ids=frozenset()):
    """Evaluate one wire against the derived metrics.

    Returns (state, detail): state in {"tripped", "ok", "error"}. A wire's
    metric is legal iff it names a canonical METRICS id or one of the
    registry's validly-declared `local_metrics:` ids (B10-4). An unknown
    metric id is a LOUD error, never a silent skip; a metric whose value is
    underivable (None) evaluates ok with the reason stated.
    """
    metric_id = wire.get("metric")
    if metric_id not in METRICS and metric_id not in local_ids:
        return "error", (
            f"unknown metric id `{metric_id}` — not in the canonical table or the "
            "registry's `local_metrics:` declarations"
        )
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


def _frontmatter_has_key(path, key):
    """True iff the file's YAML frontmatter carries `key:` with a non-empty
    value (presence only — the value is never parsed or judged; the bounded
    scan discipline of _read_frontmatter_review_after)."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    if not text.startswith("---"):
        return False
    key_re = re.compile(rf"^{re.escape(key)}:\s*\S")
    for line in text.split("\n")[1:60]:
        if line.strip() == "---":
            break
        if key_re.match(line.strip()):
            return True
    return False


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
        dispatch_text = dispatch.read_text(encoding="utf-8", errors="replace")
        open_count = 0
        oldest_days = None
        current_date = None
        for line in dispatch_text.splitlines():
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

        # oldest_drainable_section_days (build B8-5): the decay contract's age
        # facet. Eligibility mirrors `vlt-decay`'s drain verb exactly (so a
        # performed drain always clears the `drain-due` wire): a run block is
        # drain-eligible iff it is a `daily/…` or `relay` block (`consult:`
        # blocks are permanently exempt), it is fully closed (≥1 pointer line,
        # no `- [ ]`), and it is NOT its source's newest `daily/<source>` block
        # (that block carries the source's `routed through line N` watermark).
        blocks = []  # (kind, source_or_None, date_str_or_None, closed)
        cur = None
        for line in dispatch_text.splitlines():
            hb = re.match(r"^##\s*\[([^\]]*)\]\s*(\S+)", line)
            if hb:
                head = hb.group(2)
                if head.startswith("daily/"):
                    kind, source = "daily", head
                elif head.startswith("relay"):
                    kind, source = "relay", None
                elif head.startswith("consult"):
                    kind, source = "consult", None
                else:
                    kind, source = "other", None
                dm = DATE_RE.search(hb.group(1))
                cur = {
                    "kind": kind,
                    "source": source,
                    "date": dm.group(0) if dm else None,
                    "pointers": 0,
                    "open": 0,
                }
                blocks.append(cur)
                continue
            if cur is not None and re.match(r"^-\s*\[( |x|X)\]", line):
                cur["pointers"] += 1
                if re.match(r"^-\s*\[ \]", line):
                    cur["open"] += 1
        newest_daily_idx = {}  # source -> index of its newest daily block
        for i, b in enumerate(blocks):
            if b["kind"] == "daily" and b["source"]:
                newest_daily_idx[b["source"]] = i  # file order: last wins
        oldest_drainable = 0
        for i, b in enumerate(blocks):
            if b["kind"] not in ("daily", "relay"):
                continue
            if b["pointers"] == 0 or b["open"]:
                continue  # empty or still-live block — not drainable
            if b["kind"] == "daily" and newest_daily_idx.get(b["source"]) == i:
                continue  # the source's watermark carrier — never drained
            d = _days_since(b["date"], today)
            if d is not None and d > oldest_drainable:
                oldest_drainable = d
        metrics["oldest_drainable_section_days"] = oldest_drainable
    else:
        metrics["open_pointers"] = 0
        metrics["oldest_open_pointer_days"] = 0
        metrics["oldest_drainable_section_days"] = 0
        notes["open_pointers"] = "no _agent/dispatch.md — dispatch has never run (a zero of zero rows)"

    # expired_pages + pages_with_review_after over {wiki} + {research} (one
    # walk — the carrier count is the eligible population expired_pages is
    # judged against, its honest denominator).
    expired = 0
    scanned = 0
    carriers = 0
    for zone_key in ("wiki", "research"):
        zone = vault_root / smap[zone_key].rstrip("/")
        if not zone.is_dir():
            continue
        for page in sorted(zone.rglob("*.md")):
            scanned += 1
            ra = _read_frontmatter_review_after(page)
            if ra is not None:
                carriers += 1
                d = _days_since(ra, today)
                if d is not None and d > 0:
                    expired += 1
    metrics["expired_pages"] = expired
    metrics["pages_with_review_after"] = carriers
    notes["expired_pages"] = (
        f"of {carriers} pages carrying `review_after:` ({scanned} scanned); a page "
        "without the key is evergreen and cannot expire"
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

    # Size vitals (display-only). Disposition 8's "no rollover machinery" deferral was
    # discharged by field evidence (filing 2026-08-16, Arc 8); decay machinery ships
    # separately — these vitals stay display-only.
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
    vault before seeding), never an error. Returns
    (wires, local_defs, wire_errors, local_errors, note)."""
    reg = vault_root / smap["tripwires"]
    if not reg.is_file():
        return [], [], [], [], (
            f"no registry at {smap['tripwires']} — zero wires (a fresh vault before `vlt-setup` seeds it)"
        )
    text = reg.read_text(encoding="utf-8", errors="replace")
    wires, wire_errors = parse_wires(text)
    local_defs, local_errors = parse_local_metrics(text)
    return wires, local_defs, wire_errors, local_errors, None


def render_report(vault_root, smap, fallbacks):
    metrics, notes, partner_rows = derive_metrics(vault_root, smap)
    wires, local_defs, wire_errors, local_errors, reg_note = load_registry(vault_root, smap)
    local_values, local_notes = derive_local_metrics(vault_root, smap, local_defs)
    metrics.update(local_values)  # local ids can never shadow canonical ones (validated)
    local_ids = {d["id"] for d in local_defs}
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
    if local_defs or local_errors:
        # Denominated sibling block (B10-4): registry-declared local metrics.
        # Zero declarations and zero errors renders nothing at all.
        out.append("")
        out.append(f"{len(local_defs)} local metric(s) (registry-declared):")
        for err in local_errors:
            out.append(f"- ⚠ LOCAL METRIC ERROR: {err}")
        for d in local_defs:
            value = local_values.get(d["id"])
            shown = "n/a" if value is None else f"{value:,}"
            line = f"- `{d['id']}` ({d['kind']}): **{shown}** — {d['definition']}"
            if d["id"] in local_notes:
                line += f" [{local_notes[d['id']]}]"
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
        state, detail = evaluate_wire(w, metrics, local_ids)
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
    wires, local_defs, wire_errors, local_errors, _reg_note = load_registry(vault_root, smap)
    local_values, _local_notes = derive_local_metrics(vault_root, smap, local_defs)
    metrics.update(local_values)
    local_ids = {d["id"] for d in local_defs}
    parts = []
    for err in local_errors:
        parts.append(f"local metric error — {err}")
    for err in wire_errors:
        parts.append(f"wire error — {err}")
    for w in wires:
        state, detail = evaluate_wire(w, metrics, local_ids)
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
