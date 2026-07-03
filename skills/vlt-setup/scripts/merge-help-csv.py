#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Merge module help entries into shared _bmad/module-help.csv.

Reads a source CSV with module help entries and merges them into a target CSV.
Uses an anti-zombie pattern: existing rows matching the source module code are
removed before appending fresh rows.

Merge-not-replace (durability, build-6 / filing #8 B1): the anti-zombie strip
is destructive to LOCALLY-MINTED partners — a vault that minted its own
`vlt-agent-*` skills carries help rows that the *bundled* source CSV can never
contain, so a blind strip-and-reappend deregisters them on every upgrade.
When --live-skills-dir is provided, a row whose skill is absent from the source
but whose skill DIR still exists live is treated as a local mint and PRESERVED;
a row whose dir is gone is a true zombie and still dropped. Without
--live-skills-dir the behavior is the original blind anti-zombie strip (correct
for a fresh install, where there are no local mints to protect).

Legacy cleanup: when --legacy-dir and --module-code are provided, deletes old
per-module module-help.csv files from {legacy-dir}/{module-code}/ and
{legacy-dir}/core/. Only the current module and core are touched.

Exit codes: 0=success, 1=validation error, 2=runtime error
"""

import argparse
import csv
import json
import sys
from io import StringIO
from pathlib import Path

# Canonical CSV header for module-help.csv (BMad schema: columns 9-10 are
# preceded-by/followed-by; vlt shipped after/before pre-0.5.0 — see LEGACY_HEADER).
HEADER = [
    "module",
    "skill",
    "display-name",
    "menu-code",
    "description",
    "action",
    "args",
    "phase",
    "preceded-by",
    "followed-by",
    "required",
    "output-location",
    "outputs",
]

# The known-old vlt header (identical columns/positions, columns 9-10 named
# after/before). A live vault installed pre-0.5.0 carries it forever unless
# migrated here, because the merge prefers the target's existing header. Data
# rows are positionally identical, so migration = rename the header in place.
LEGACY_HEADER = HEADER[:8] + ["after", "before"] + HEADER[10:]


def canonicalize_header(header: list[str]) -> tuple[list[str], bool]:
    """Rename the known-old header variant to canonical; anything else passes through.

    Returns (header, migrated). Only the exact 13-column after/before form is
    rewritten — an unknown header is never blindly rewritten.
    """
    if header == LEGACY_HEADER:
        return list(HEADER), True
    return header, False


def parse_args():
    parser = argparse.ArgumentParser(
        description="Merge module help entries into shared _bmad/module-help.csv with anti-zombie pattern."
    )
    parser.add_argument(
        "--target",
        required=True,
        help="Path to the target _bmad/module-help.csv file",
    )
    parser.add_argument(
        "--source",
        required=True,
        help="Path to the source module-help.csv with entries to merge",
    )
    parser.add_argument(
        "--live-skills-dir",
        help=(
            "Path to the live skills directory (e.g. .claude/skills/). When set, "
            "enables merge-not-replace: a target row whose skill is absent from the "
            "source but whose skill dir still exists here is preserved as a local mint "
            "(rather than stripped by the anti-zombie pass)."
        ),
    )
    parser.add_argument(
        "--legacy-dir",
        help="Path to _bmad/ directory to check for legacy per-module CSV files.",
    )
    parser.add_argument(
        "--module-code",
        help="Module code (required with --legacy-dir for scoping cleanup).",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print detailed progress to stderr",
    )
    return parser.parse_args()


def read_csv_rows(
    path: str,
) -> tuple[list[str], list[list[str]], list[tuple[int, list[str]]]]:
    """Read CSV file returning (header, well_formed_rows, malformed_rows).

    Returns empty header/rows/malformed if file doesn't exist.

    A mis-split row — an unquoted comma inside a field makes csv.reader split the
    row into the wrong number of columns — is SKIPPED and collected, not raised.
    build-3 raised a ValueError here, which aborted the entire merge on a single
    bad field written by an older vlt-mint (so one malformed row could block an
    upgrade's whole registration step, including the local-mint preserve). The
    read-side fix (build-10/R2-3) graduates that detector to a survivor: skip the
    offending row, hand it back to the caller to report loudly, and let every
    well-formed row — and the preserve step — proceed. The write-side fix
    (vlt-mint always-quotes free-text fields) stops new bad rows at the source;
    this tolerance survives the ones already on disk.
    """
    file_path = Path(path)
    if not file_path.exists():
        return [], [], []

    with open(file_path, "r", encoding="utf-8", newline="") as f:
        content = f.read()

    reader = csv.reader(StringIO(content))
    rows = list(reader)

    if not rows:
        return [], [], []

    header, data_rows = rows[0], rows[1:]

    expected = len(header)
    well_formed: list[list[str]] = []
    malformed: list[tuple[int, list[str]]] = []
    for line_no, row in enumerate(data_rows, start=2):  # +2: 1-based, past the header line
        if row and len(row) != expected:
            malformed.append((line_no, row))
        else:
            well_formed.append(row)

    return header, well_formed, malformed


def describe_malformed(
    path: str, malformed: list[tuple[int, list[str]]]
) -> list[dict]:
    """Build actionable records for skipped mis-split rows.

    The `skill` column (index 1) sits before every comma-prone free-text field
    (description / args / outputs), so it survives an over-split — we can always
    name which entry was dropped.
    """
    described = []
    for line_no, row in malformed:
        skill = row[1].strip() if len(row) > 1 and row[1].strip() else "?"
        described.append(
            {"path": path, "line": line_no, "skill": skill, "columns": len(row)}
        )
    return described


def extract_module_codes(rows: list[list[str]]) -> set[str]:
    """Extract unique module codes from data rows."""
    codes = set()
    for row in rows:
        if row and row[0].strip():
            codes.add(row[0].strip())
    return codes


def filter_rows(rows: list[list[str]], module_code: str) -> list[list[str]]:
    """Remove all rows matching the given module code."""
    return [row for row in rows if not row or row[0].strip() != module_code]


def filter_rows_preserving_local(
    rows: list[list[str]],
    module_code: str,
    source_skills: set[str],
    live_skills_dir: str,
    verbose: bool = False,
) -> tuple[list[list[str]], int, list[str]]:
    """Anti-zombie strip that PRESERVES locally-minted rows (merge-not-replace).

    A target row matching ``module_code`` is dropped only when it is either
    (a) a shipped skill (its skill name appears in the source/bundled rows — it
    will be re-appended fresh), or (b) a true zombie (its skill dir no longer
    exists under ``live_skills_dir``). A row whose skill is absent from the
    source but whose dir still exists live is a local mint and is KEPT.

    Returns (kept_rows, removed_count, preserved_skill_names).
    """
    skills_root = Path(live_skills_dir)
    kept: list[list[str]] = []
    removed = 0
    preserved: list[str] = []
    for row in rows:
        if not row or row[0].strip() != module_code:
            kept.append(row)
            continue
        skill = row[1].strip() if len(row) > 1 else ""
        if skill and skill in source_skills:
            # Shipped row — drop now; the source will re-append the fresh version.
            removed += 1
            continue
        if skill and (skills_root / skill).is_dir():
            # Local mint: absent from the bundle but its skill dir is live. Keep it.
            kept.append(row)
            preserved.append(skill)
            continue
        # True zombie: not shipped and no live dir. Drop (original anti-zombie intent).
        removed += 1
    if verbose and preserved:
        print(
            f"Preserved {len(preserved)} local-mint row(s): {sorted(preserved)}",
            file=sys.stderr,
        )
    return kept, removed, preserved


def write_csv(path: str, header: list[str], rows: list[list[str]], verbose: bool = False) -> None:
    """Write header + rows to CSV file, creating parent dirs as needed."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if verbose:
        print(f"Writing {len(rows)} data rows to {path}", file=sys.stderr)

    with open(file_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)


def cleanup_legacy_csvs(
    legacy_dir: str, module_code: str, verbose: bool = False
) -> list:
    """Delete legacy per-module module-help.csv files for this module and core only.

    Returns list of deleted file paths.
    """
    deleted = []
    for subdir in (module_code, "core"):
        legacy_path = Path(legacy_dir) / subdir / "module-help.csv"
        if legacy_path.exists():
            if verbose:
                print(f"Deleting legacy CSV: {legacy_path}", file=sys.stderr)
            legacy_path.unlink()
            deleted.append(str(legacy_path))
    return deleted


def main():
    args = parse_args()

    # Read source entries
    source_header, source_rows, source_malformed = read_csv_rows(args.source)
    if not source_rows:
        print(f"Error: No data rows found in source {args.source}", file=sys.stderr)
        sys.exit(1)

    # Determine module codes being merged
    source_codes = extract_module_codes(source_rows)
    if not source_codes:
        print("Error: Could not determine module code from source rows", file=sys.stderr)
        sys.exit(1)

    if args.verbose:
        print(f"Source module codes: {source_codes}", file=sys.stderr)
        print(f"Source rows: {len(source_rows)}", file=sys.stderr)

    # Read existing target (may not exist)
    target_header, target_rows, target_malformed = read_csv_rows(args.target)
    target_existed = Path(args.target).exists()

    # Surface any mis-split rows skipped on read (R2-3). Loud unconditionally —
    # a dropped row means a help entry won't register; if it is a local mint, its
    # registration is lost until the source field is re-quoted (or it is re-minted).
    malformed_skipped = describe_malformed(args.source, source_malformed) + \
        describe_malformed(args.target, target_malformed)
    for m in malformed_skipped:
        print(
            f"WARNING: skipped malformed row — {m['path']} line {m['line']} "
            f"(skill {m['skill']!r}, {m['columns']} columns): likely an unquoted "
            f"comma in a free-text field. The row is NOT registered. Re-quote the "
            f"field and re-run, or re-mint the skill.",
            file=sys.stderr,
        )

    if args.verbose:
        print(f"Target exists: {target_existed}", file=sys.stderr)
        if target_existed:
            print(f"Existing target rows: {len(target_rows)}", file=sys.stderr)

    # Header migration (installer-interop, build-13): rename the known-old
    # after/before header to canonical preceded-by/followed-by. Runs before any
    # row handling below (rows are positionally identical under both headers).
    # Target migration is the one that fixes a live vault (target-header-wins);
    # a legacy source header (stale bundle) is canonicalized silently.
    target_header, header_migrated = canonicalize_header(target_header)
    source_header, _ = canonicalize_header(source_header)
    if header_migrated:
        print(
            f"Migrated legacy module-help.csv header in place "
            f"(after,before -> preceded-by,followed-by): {args.target}",
            file=sys.stderr,
        )

    # Use source header if target doesn't exist or has no header
    header = target_header if target_header else (source_header if source_header else HEADER)

    # Anti-zombie: remove existing rows for each source module code. With
    # --live-skills-dir, locally-minted rows (absent from the bundle, dir still
    # live) are preserved instead of stripped (merge-not-replace, build-6/B1).
    source_skills = {row[1].strip() for row in source_rows if len(row) > 1 and row[1].strip()}
    filtered_rows = target_rows
    removed_count = 0
    preserved_skills: list[str] = []
    for code in source_codes:
        if args.live_skills_dir:
            filtered_rows, removed, preserved = filter_rows_preserving_local(
                filtered_rows, code, source_skills, args.live_skills_dir, args.verbose
            )
            removed_count += removed
            preserved_skills += preserved
        else:
            before_count = len(filtered_rows)
            filtered_rows = filter_rows(filtered_rows, code)
            removed_count += before_count - len(filtered_rows)

    if args.verbose and removed_count > 0:
        print(f"Removed {removed_count} existing rows (anti-zombie)", file=sys.stderr)

    # Append source rows
    merged_rows = filtered_rows + source_rows

    # Write result
    write_csv(args.target, header, merged_rows, args.verbose)

    # Legacy cleanup: delete old per-module CSV files
    legacy_deleted = []
    if args.legacy_dir:
        if not args.module_code:
            print(
                "Error: --module-code is required when --legacy-dir is provided",
                file=sys.stderr,
            )
            sys.exit(1)
        legacy_deleted = cleanup_legacy_csvs(
            args.legacy_dir, args.module_code, args.verbose
        )

    # Output result summary as JSON
    result = {
        "status": "success",
        "target_path": str(Path(args.target).resolve()),
        "target_existed": target_existed,
        "module_codes": sorted(source_codes),
        "rows_removed": removed_count,
        "rows_added": len(source_rows),
        "local_mints_preserved": sorted(preserved_skills),
        "total_rows": len(merged_rows),
        "legacy_csvs_deleted": legacy_deleted,
        "malformed_rows_skipped": malformed_skipped,
        "header_migrated": header_migrated,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
