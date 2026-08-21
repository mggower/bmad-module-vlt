#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Dispatch lane check for the vlt module (build B9-1) — the denominator
reproducibility instrument.

Factory-side, standalone, runnable at rest: this script embeds two fixture
dispatch records in the shipped block/pointer grammar and asserts, per pointer
line, the lane the counting rules derive (`skills/vlt-dispatch/references/
ledger.md`, *Counting rules*; lane semantics and the era datum:
`references/relay.md`, *Backward compatibility*). It is the fixture-backed
check of record for the derivation `ledger` executes prose-side — two readers
of the same record must agree, and this script is the reader that cannot
squint.

Fixtures carry placeholder slugs and paths only (`_agent/handoffs/{date}-
{owner}-to-{consumer}-{slug}.md` style) — no vault-local content.

The derivation (one lane per pointer line, in this order):

  1. path-keyed  — the line carries a key-path: a trailing link (wikilink or
     plain path) whose WRITTEN target sits under the handoff zone
     (`_agent/handoffs/` or `_agent/specs/`). A LOCATION test — no disk read.
     Any other wikilink is payload. A path-keyed pointer is ordinary traffic,
     except: a shape-annotated `handoff` whose written zone path is missing
     from the disk model is a finding (the EXISTENCE test, wikilink semantics,
     extension-optional: `path` or `path.md`).
  2. legacy lane — un-annotated (no shape in the block header or the
     pointer-leading annotation) and not path-keyed.
  3. proto-`deliver` lane — shape-annotated, not path-keyed, block-dated
     before the era (the first `deliver` pointer in this record), and its
     shape's key requirement is unmet as written (an annotated `handoff` with
     no key-path — a `ref` is payload, never the key; an `ask`/`answer`/
     `deliver` with no `ref`). A shape-annotated pre-era pointer whose key is
     present is ordinary traffic, not lane traffic. In a record containing no
     `deliver` pointer at all, every shape-annotated pathless key-failing
     pointer is proto-`deliver` traffic.
  4. findings    — every other key-requirement failure.

Shape detection reads the block header and the pointer-leading annotation
only — a shape annotation quoted in body prose is payload (and never sets the
era). Scope: `relay:` blocks only; `consult:`/`daily` traffic is out of scope.

Exit 0: every fixture pointer lands in its expected lane and the per-fixture
denominators match. Exit 1: any disagreement, named per case.
"""

import re
import sys

HANDOFF_ZONE = ("_agent/handoffs/", "_agent/specs/")
SHAPES = ("handoff", "ask", "answer", "deliver")

BLOCK_RE = re.compile(
    r"^## \[(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2})\] (relay|consult|daily)"
)
HEADER_SHAPE_RE = re.compile(
    r"\((handoff|ask|answer|deliver)(?::\s*([A-Za-z0-9][A-Za-z0-9-]*))?\)"
)
POINTER_RE = re.compile(r"^- \[[ xX]\]")
LEADING_SHAPE_RE = re.compile(
    r"^- \[[ xX]\]\s*\((handoff|ask|answer|deliver)"
    r"(?::\s*([A-Za-z0-9][A-Za-z0-9-]*))?\)"
)
TRAILING_LINK_RE = re.compile(r"→\s*(?:\[\[([^\]]+)\]\]|(\S+))\s*$")


def parse_pointers(record):
    """Yield one dict per pointer line in a relay: block, in record order."""
    pointers = []
    block = None  # (stamp, shape, ref, is_relay)
    for line in record.splitlines():
        m = BLOCK_RE.match(line)
        if m:
            stamp = m.group(1) + " " + m.group(2)
            kind = m.group(3)
            shape, ref = None, None
            if kind == "relay":
                sm = HEADER_SHAPE_RE.search(line)
                if sm:
                    shape, ref = sm.group(1), sm.group(2)
            block = (stamp, shape, ref, kind == "relay")
            continue
        if block and block[3] and POINTER_RE.match(line):
            stamp, shape, ref, _ = block
            lm = LEADING_SHAPE_RE.match(line)
            if lm:  # pointer-leading annotation governs this line
                shape, ref = lm.group(1), lm.group(2)
            tm = TRAILING_LINK_RE.search(line)
            target = (tm.group(1) or tm.group(2)) if tm else None
            key_path = (
                target
                if target and target.startswith(HANDOFF_ZONE)
                else None
            )
            pointers.append(
                {"stamp": stamp, "shape": shape, "ref": ref,
                 "key_path": key_path, "line": line}
            )
    return pointers


def on_disk(target, disk):
    """Existence test: wikilink semantics, extension-optional."""
    return target in disk or (target + ".md") in disk


def derive_lanes(pointers, disk):
    """Assign each pointer its lane per the stated derivation."""
    delivers = [p["stamp"] for p in pointers if p["shape"] == "deliver"]
    era = min(delivers) if delivers else None  # None: no-`deliver` edge
    lanes = []
    for p in pointers:
        if p["key_path"]:  # location test passed: path-keyed
            if p["shape"] == "handoff" and not on_disk(p["key_path"], disk):
                lanes.append("finding")  # existence test failed
            else:
                lanes.append("ordinary")
            continue
        if p["shape"] is None:
            lanes.append("legacy")
            continue
        # annotated, pathless: key requirement as written
        key_met = p["ref"] is not None if p["shape"] != "handoff" else False
        if key_met:
            lanes.append("ordinary")
        elif era is None or p["stamp"] < era:
            lanes.append("proto")
        else:
            lanes.append("finding")
    return lanes


# --- Fixture record 1: era present; one pointer per membership class -------

FIXTURE_1 = """\
## [2026-01-03 09:00] relay: partner-a → partner-b — 1 item
- [ ] `partner-b` Partner B — a note is waiting somewhere, no link written

## [2026-01-04 10:00] relay: partner-a → partner-b (ask: source-hunt) — 1 item
- [ ] `partner-b` Partner B — what would close it is a source the vault doesn't hold

## [2026-01-05 11:00] relay: partner-b → partner-a (ask) — 1 item
- [x] `partner-a` Partner A — a question fired with no ref at all

## [2026-01-06 12:00] relay: partner-a → partner-b (handoff) — 1 item
- [ ] `partner-b` Partner B — a handoff annotated but never linked

## [2026-01-07 13:00] relay: partner-a → partner-b (handoff: topic-pass) — 1 item
- [ ] `partner-b` Partner B — annotated handoff carrying a ref and no path

## [2026-01-08 09:30] relay: partner-b → partner-a — 1 item
- [ ] `partner-a` Partner A — superseded by the batch re-fire; the note quotes (deliver: topic-pass) in prose

## [2026-01-09 14:00] relay: partner-a → partner-b — 1 item
- [ ] `partner-b` Partner B — brief waiting → [[_agent/handoffs/2026-01-09-owner-to-consumer-topic-brief]]

## [2026-01-10 15:00] relay: partner-a → partner-b (deliver: topic-pass) — 1 item
- [ ] `partner-b` Partner B — the delivery, written inline; durable notes as wikilinks

## [2026-01-11 16:00] relay: partner-b → partner-a (answer) — 1 item
- [ ] `partner-a` Partner A — an answer fired post-era with no ref

## [2026-01-12 10:00] relay: partner-a → partner-b (handoff) — 1 item
- [ ] `partner-b` Partner B — doc waiting → [[_agent/handoffs/2026-01-12-owner-to-consumer-missing-doc]]

## [2026-01-13 11:00] relay: partner-b → partner-a (ask: follow-up-question) — 1 item
- [ ] `partner-a` Partner A — context in the wiki → [[wiki/concept-note]]

## [2026-01-13 12:00] consult: partner-a → partner-b — 1 item
- [ ] `partner-b` Partner B — pre-checked consult traffic, out of scope
"""

DISK_1 = {
    "_agent/handoffs/2026-01-09-owner-to-consumer-topic-brief.md",
    # 2026-01-12-owner-to-consumer-missing-doc deliberately absent
}

EXPECTED_1 = [
    ("legacy-unannotated-pathless", "legacy"),
    ("pre-era-ask-with-ref-ordinary", "ordinary"),
    ("pre-era-ask-no-ref-proto", "proto"),
    ("pre-era-annotated-handoff-no-path-proto", "proto"),
    ("pre-era-handoff-ref-is-payload-proto", "proto"),
    ("body-prose-annotation-trap-legacy", "legacy"),
    ("path-keyed-extensionless-wikilink-ordinary", "ordinary"),
    ("era-deliver-with-ref-ordinary", "ordinary"),
    ("post-era-answer-no-ref-finding", "finding"),
    ("existence-finding-not-pathless", "finding"),
    ("payload-wikilink-outside-zone-ordinary", "ordinary"),
]

DENOMINATORS_1 = {"legacy": 2, "proto": 3}

# --- Fixture record 2: no `deliver` pointer at all (the no-`deliver` edge) --

FIXTURE_2 = """\
## [2026-02-02 09:00] relay: partner-a → partner-b (handoff) — 1 item
- [ ] `partner-b` Partner B — annotated handoff, no path, in a record with no deliver

## [2026-02-03 10:00] relay: partner-b → partner-a (ask) — 1 item
- [ ] `partner-a` Partner A — an unkeyed ask in a record where deliver never ran

## [2026-02-04 11:00] relay: partner-a → partner-b (ask: open-question) — 1 item
- [ ] `partner-b` Partner B — a properly keyed ask stays ordinary traffic

## [2026-02-05 12:00] relay: partner-b → partner-a — 1 item
- [ ] `partner-a` Partner A — un-annotated and pathless, the legacy lane
"""

DISK_2 = set()

EXPECTED_2 = [
    ("no-deliver-edge-handoff-no-path-proto", "proto"),
    ("no-deliver-edge-ask-no-ref-proto", "proto"),
    ("no-deliver-edge-ask-with-ref-ordinary", "ordinary"),
    ("no-deliver-edge-unannotated-legacy", "legacy"),
]

DENOMINATORS_2 = {"legacy": 1, "proto": 2}


def check_fixture(name, record, disk, expected, denominators):
    failures = []
    pointers = parse_pointers(record)
    if len(pointers) != len(expected):
        failures.append(
            f"{name}: parsed {len(pointers)} relay pointers, "
            f"expected {len(expected)} (scope or grammar drift)"
        )
        return failures
    lanes = derive_lanes(pointers, disk)
    for (case, want), got, p in zip(expected, lanes, pointers):
        if got != want:
            failures.append(
                f"{name} / {case}: derived '{got}', expected '{want}'"
                f"  [{p['line'].strip()}]"
            )
    for lane, want in denominators.items():
        got = lanes.count(lane)
        if got != want:
            failures.append(
                f"{name} / denominator {lane}: counted {got}, expected {want}"
            )
    return failures


def main():
    failures = []
    failures += check_fixture(
        "fixture-1", FIXTURE_1, DISK_1, EXPECTED_1, DENOMINATORS_1)
    failures += check_fixture(
        "fixture-2", FIXTURE_2, DISK_2, EXPECTED_2, DENOMINATORS_2)
    total = len(EXPECTED_1) + len(EXPECTED_2)
    if failures:
        for f in failures:
            print(f"FAIL {f}")
        print(f"dispatch-lane-check: {len(failures)} disagreement(s) "
              f"across {total} cases")
        return 1
    print(f"dispatch-lane-check: PASS — {total} cases across 2 fixture "
          f"records agree with the stated derivation "
          f"(fixture-1 lanes: legacy {DENOMINATORS_1['legacy']}, "
          f"proto {DENOMINATORS_1['proto']}; fixture-2 no-deliver edge: "
          f"legacy {DENOMINATORS_2['legacy']}, proto {DENOMINATORS_2['proto']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
