---
title: 'Build #9 — the vitals metric vocabulary (a fourth local-metric kind for content-filtered
  counts, and the staleness denominator promoted to a canonical metric)'
status: 'BUILT 2026-08-24 — F1: fourth bounded kind `frontmatter_key_count` in
  LOCAL_METRIC_KINDS + `glob` locator (LOCAL_METRIC_REQUIRED unchanged, comment block
  unworded); F2: kind-specific `key:` validation in parse_local_metrics (missing key +
  malformed token both loud per-entry); F3: `_frontmatter_has_key` helper beside
  `_read_frontmatter_review_after` (same bounded scan: leading `---`, lines[1:60], stop at
  closing `---`, presence `^{key}:\s*\S`, value never parsed) + the derive branch;
  F4: tripwires.yaml schema header documents the fourth kind + the `key` field (`:14-18`
  bound untouched, seed still ships no local_metrics); F5: `pages_with_review_after`
  promoted to canonical METRICS beside expired_pages, carriers counted inside the existing
  walk (no second scan), note denominator repaired ("of {carriers} pages carrying
  `review_after:` ({scanned} scanned); …"). NO CHANGELOG edit (notice stays staged in
  disposition 6 for the v0.15.0 release); NO lint edit. Verification: the E2(a) fixture
  harness (scratchpad, importlib against the shipped asset, temp fixture vault: 5 pages —
  2 wiki carriers incl. 1 expired, 1 frontmatter non-carrier, 1 bare page, 1 expired
  research carrier) ran ALL 18 ASSERTIONS GREEN — (1a-c) `wiki-review-after-carriers`
  (kind frontmatter_key_count, key review_after, glob {wiki}/**/*.md) parses with zero
  errors and derives 2 = the carrier count (filing 190100''s lost derive expressible at
  rest); (2a-d) `pages_with_review_after` derives 3 canonically, `expired_pages` 2, the
  note states the carrier denominator verbatim; (3a-c) render_report shows the canonical
  row, the local row denominated, and the repaired note; (4a-e) loud per-entry negatives —
  missing `key:`, malformed key token ("not a token!"), unknown kind (unchanged wording),
  and the id `pages_with_review_after` firing the SHADOW error (the newly canonical id
  refused locally); (5a-c) evaluate_wire accepts a wire on the canonical id and one on the
  local id. `uv run tools/package-lint.py` A/B/C/E PASS, D SKIPPED (expected — no
  --expect-version) with NO lint edit (the C8 no-trap claim exercised live). Single-home
  greps: `frontmatter_key_count` in skills/ hits only vlt-vitals.py + tripwires.yaml;
  `pages_with_review_after` in skills/+tools/ hits only vlt-vitals.py. No .decision-log.md
  on disk (a transient harness __pycache__ under assets/hooks/ was deleted; the harness
  now sets sys.dont_write_bytecode). Deviations: no deviations. Next: cycle ready for
  release (vlt-release v0.15.0), held for owner approval — versions/CHANGELOG/tag are the
  release runner''s, not this build''s.'
module_code: 'vlt'
created: '2026-08-24'
derives_from:
  - 'factory/inbox/2026-08-23-190100-local-metrics-kinds-cannot-express-a-content-filtered-count.md
    (A10-19 — the B10-4(4) BLOCKED routing: a content-filtered derive has no vault-local home;
    directions 2 + 3 as ruled at Q3; the issue-#1 amendment is captured with it as the same
    event''s vault-side telling)'
roadmap: 'factory/cycles/11-reachability/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-24): Q3 — directions 2 AND 3, direction 1
  REJECTED (a content predicate would open a query language inside a deliberately bounded
  declarative vocabulary); E2 — B10-4(4) attached to build-9, unblock condition corrected
  (unblocks when direction 2''s fourth kind SHIPS, not when Q3 is ruled), SPLIT per
  roundtable A7 into (a) ship-verifiable fixture declaration that GATES closeout and (b) the
  field-contingent live declaration that does not; roundtable A7 — build-9 includes a
  DA3-style field notice naming the fourth kind and the lost-derive case it exists for.
  binds: Q3, E2.'
risk: 'low-moderate — two assets edited (vlt-vitals.py + tripwires.yaml), no convention
  version: moves (neither asset is handshaked; the registry header owns the local_metrics
  schema and is updated in the same build), no consumer walk; the moderate half is that a
  canonical METRICS addition ships to every vault''s vitals surface at once — bounded by
  package-lint C8 importing METRICS from the asset (no re-declaration anywhere, verified at
  brief time), so nothing else must agree.'
---

# Build #9 — the vitals metric vocabulary

A10-19 is the B10-4(4) BLOCKED grade walking the module's own sanctioned route: the
registry's stated bound (`tripwires.yaml:14-18` — "a derive beyond those kinds has no
vault-local home; its route is an upstream filing for a new canonical metric or a new
kind") was honored by the field vault, which **refused to fabricate** its lost
content-filtered derive (`pages_with_review_after`, the count of wiki pages whose
frontmatter carries `review_after:`) as a `file_count` over `{wiki}/**/*.md`. This build
ships both halves the Q3 ruling ordered: **direction 2**, a fourth bounded kind
(`frontmatter_key_count`) so a content-filtered count has a vault-local home — the class
fix, and the mechanism whose shipping unblocks B10-4(4); and **direction 3**, promoting
`pages_with_review_after` to the canonical `METRICS` table and repairing the
`expired_pages` note's denominator — the instance fix, near-free because the hook's
existing loop already computes the predicate. It also stages the **field notice**
(roundtable A7, the DA3 CHANGELOG-notice precedent): E2(b)'s discharging event is a vault
*declaring* the kind, and a declaration cannot come from a vault that was never told the
route exists.

All rejected alternatives in the parent filing and the rulings are settled — **do not
re-litigate**. In particular: direction 1 (a `matching:`/`frontmatter_key:` content
predicate on `file_count`) is REJECTED at Q3 and must not reappear as an implementation
convenience; the "superseded local instrumentation" install-report question is carried
context in the capture, deliberately not this build's scope; and vault-local additions to
the canonical `METRICS` table remain illegal (`vlt-vitals.py:199-201`).

## Brief-time dispositions

The roadmap's §Questions-left-to-brief-time names no build-9 questions; the dispositions
below are the design calls the ruled directions leave to the brief, each grounded in the
binding record. Recorded per the headless contract — every judgment call this run made is
inline here.

1. **The fourth kind is named `frontmatter_key_count`.** Q3's own candidate name ("a
   fourth bounded kind (`frontmatter_key_count` or similar): `glob` locator plus a `key:`
   field, one named semantic"). The semantic, stated once: *count of files matching
   `glob` whose YAML frontmatter carries the key named by `key:` with a non-empty value*.
   One named semantic, no predicate language — the bound the direction-1 rejection
   protects.

2. **The `key:` requirement homes as kind-specific validation in `parse_local_metrics`,
   NOT in `LOCAL_METRIC_REQUIRED`.** The roadmap's phrase "the required-field validation"
   (build-9 bullet) is discharged the way the existing locator requirement is: a
   kind-conditional check (`vlt-vitals.py:323-325` is the pattern — `kind X requires a
   `Y:` field`). Adding `key` to `LOCAL_METRIC_REQUIRED` (`:253`) would wrongly demand it
   of the three existing kinds. `LOCAL_METRIC_REQUIRED` is unchanged.

3. **Presence semantics, bounded.** A page "carries" the key iff a frontmatter line
   matches `^{key}:\s*\S` inside the `---` block (scan discipline mirrors
   `_read_frontmatter_review_after`, `:480-496`: file starts with `---`, first 60 lines,
   stop at the closing `---`). The **value is never parsed or judged** — the kind counts
   carriers; judging values would be the query language the ruling rejected. The `key:`
   token itself is validated at parse time (`^[A-Za-z_][\w-]*$`) so a malformed
   declaration errors loudly rather than silently counting zero.

4. **E2(a)'s fixture declares under a NON-shadowing id — the direction-2/3 interaction,
   made explicit.** Direction 3 makes `pages_with_review_after` a canonical id, and a
   local declaration shadowing a canonical id is a loud error by design (`:326-330`). So
   the fixture expressing "the known lost content-filtered derive" (filing 190100's case)
   declares the same *semantics* under a distinct id (e.g. `wiki-review-after-carriers`:
   kind `frontmatter_key_count`, `key: review_after`, `glob: "{wiki}/**/*.md"`), proving
   the class route can state the instance the kind exists for. The shadow case — a
   declaration literally named `pages_with_review_after` erroring loudly — is exercised as
   its own fixture case, because the new canonical id newly widens the shadow net's
   population.

5. **E2(b)'s discharging event, sharpened so it stays performable.** A7 rules "(b) the
   live declaration (unchanged)". Grounded note: after this build, the literal lost
   metric arrives **canonically** at the vault's 0.15.0 upgrade (received, never
   declared — the Q3 record's own "moot, not discharged" analysis of direction 3), and
   the literal id becomes a shadow error locally. The event that remains performable, and
   the one E2(b) means, is **the vault's first genuine `local_metrics:` declaration of
   kind `frontmatter_key_count`** — the class route used live. Ledger check 3 states it
   this way. This sharpens the event's wording, not the ruling.

6. **The field notice's channel is the v0.15.0 CHANGELOG entry, its text staged
   verbatim here.** The DA3 precedent (Cycle 10 roadmap, Obligations created #1,
   owner-ruled 2026-08-23: notice lands in the release notes / CHANGELOG entry authored
   by `vlt-release` Stage 3; no pinned tracker issue). Build-9 itself edits no
   CHANGELOG line — the entry does not exist until release — so the notice is **staged**
   in §8 of this brief, the release-time obligation is recorded there, and ledger check 2
   (ship-verifiable) verifies it landed at the release gate. Notice text (verbatim, to be
   included in the v0.15.0 entry):

   > **New in the enforcement kit — a home for content-filtered counts.** `local_metrics:`
   > gains a fourth bounded kind, `frontmatter_key_count` (count of files matching `glob`
   > whose frontmatter carries `key:`), so a derive like *pages carrying `review_after:`*
   > — the exact class a vault previously had to refuse to declare (it had no legal home;
   > see issue #1) — is now declarable in `{tripwires}` without hand-editing the reader.
   > The lost instance itself, `pages_with_review_after`, also arrives as a canonical
   > metric with this release: it is derived for every vault automatically and now
   > denominates `expired_pages` honestly. If your vault refused a content-filtered
   > declaration under the old bound, the route exists now.

7. **Interim posture (R1): not applicable** — nothing ships ahead of its mechanism. The
   vocabulary (kind + canonical metric) and its mechanism (validation + derive branches)
   land in the same build and commit; the notice trails the mechanism by design (it
   announces something already shipped in the same version).

## F-sites

All capture-time sites re-grounded 2026-08-24 against the working tree at build-8's
commit (`86a05e8`): **every site HOLDS** — no grounding corrections owed, no superseding
notes written. The roadmap's clerk no-trap note also re-verified: `tools/package-lint.py`
imports `METRICS` from the asset (`package-lint.py:386`; doc `:33-34`, `:357-358`) and
compiles the reader — never re-declares — so a new canonical metric and a new kind ride
in with **no lint edit**.

### F1 — `skills/vlt-setup/assets/hooks/vlt-vitals.py:247-253` — the kind vocabulary (direction 2)

**Current state:** the B10-4 comment block (`:247-250`) states the bound and the upstream
route; `LOCAL_METRIC_KINDS = {"file_count", "bytes", "days_since_newest"}` (`:251`);
`LOCAL_METRIC_LOCATOR = {"file_count": "glob", "bytes": "path", "days_since_newest":
"glob"}` (`:252`); `LOCAL_METRIC_REQUIRED = ["id", "kind", "definition"]` (`:253`).

**Change:** add `"frontmatter_key_count"` to `LOCAL_METRIC_KINDS` and
`"frontmatter_key_count": "glob"` to `LOCAL_METRIC_LOCATOR`. `LOCAL_METRIC_REQUIRED`
unchanged (disposition 2). The comment block's route sentence stays accurate as written
(kinds remain bounded — now four); do not reword it.

**Why:** Q3 direction 2 — the class fix; the mechanism whose shipping unblocks B10-4(4)
(E2's corrected unblock condition).

### F2 — `skills/vlt-setup/assets/hooks/vlt-vitals.py:300-339` — `parse_local_metrics` validation

**Current state:** per-entry loud-error validation: missing required fields (`:314`),
unknown kind (`:318-321`), kind-required locator (`:323-325`), canonical-id shadow
(`:326-330`), duplicate id (`:331-332`).

**Change:** after the locator check, add the kind-specific `key:` validation: for kind
`frontmatter_key_count`, a missing `key:` is a per-entry error (mirror the locator
message form: ``kind `frontmatter_key_count` requires a `key:` frontmatter-key field``),
and a `key:` value not matching `^[A-Za-z_][\w-]*$` is a per-entry error (a malformed key
must not silently count zero — the never-a-silent-skip posture, `:304-307`). No parser
change: `_parse_flat_entry_list` (`:256-281`) already passes arbitrary flat fields
through, `key:` included (verified at brief time).

**Why:** the roadmap bullet's "required-field validation" leg, homed per disposition 2/3.

### F3 — `skills/vlt-setup/assets/hooks/vlt-vitals.py:376-435` + a helper beside `:480` — the derive branch

**Current state:** `derive_local_metrics` (`:376`) resolves the kind's locator field
(`:386-394`) and branches on kind: `file_count` (`:396`), `bytes` (`:398-405`),
`days_since_newest` (`:406+`). Frontmatter helpers: `_read_frontmatter_date` (`:353`),
`_read_frontmatter_review_after` (`:480-496`) — both bounded scans, no YAML parse.

**Change:** (a) a new generic helper `_frontmatter_has_key(path, key)` beside
`_read_frontmatter_review_after`, same scan discipline (returns False on unreadable file
/ no leading `---`; scans `lines[1:60]` to the closing `---`; True iff a line matches
`^{key}:\s*\S` — disposition 3). (b) a new branch in `derive_local_metrics`:

```python
elif kind == "frontmatter_key_count":
    values[mid] = sum(
        1 for f in vault_root.glob(spec)
        if f.is_file() and _frontmatter_has_key(f, d["key"])
    )
```

No suffix filter — the declared `glob` is the population; a file without frontmatter
simply isn't a carrier. The existing unresolved-`{key}`-locator guard (`:389-394`) and
the read-only/derive-only posture (`:377-380` docstring) cover the new branch unchanged.

**Why:** direction 2's mechanism — without this branch the kind would be a declared
vocabulary with no effective derive, this cycle's own disease.

### F4 — `skills/vlt-setup/assets/tripwires.yaml:32-52` — the schema header (the registry owns the schema)

**Current state:** the LOCAL METRICS schema block documents `kind` with the three bounded
kinds (`:38-44`), the `glob / path` locator line (`:45-47`), and `definition` (`:48-49`).
The bound statement lives at `:14-18` and is **not** touched (the route it names was
walked; kinds remain bounded).

**Change:** in the `kind` list, add the fourth kind in the sibling style:

```
#                   frontmatter_key_count — count of files matching `glob` whose
#                                       frontmatter carries the key named by
#                                       `key:` (presence with a non-empty value;
#                                       the value itself is never parsed)
```

and beside the locator line, document the extra field:

```
#   key         — frontmatter_key_count only: the frontmatter key whose
#                 carriers are counted (a bare key token, e.g. review_after)
```

**Why:** the roadmap bullet's "plus the schema header in
`skills/vlt-setup/assets/tripwires.yaml` (the registry header owns that schema)" — the
consumer surfaces (`vlt-mint/SKILL.md:99`, `vlt-dispatch/references/ledger.md:39`) point
at this header and restate nothing (verified at brief time — no kind enumeration exists
anywhere else; no sweep needed).

**Out of scope at this site:** the seed still ships NO `local_metrics:` (`:52`) — the
section stays the vault's to grow; the WRITE MOMENTS and merge-durability text
(`:54-70`) is untouched.

### F5 — `skills/vlt-setup/assets/hooks/vlt-vitals.py:203-243` + `:617-634` — the canonical promotion (direction 3)

**Current state:** `METRICS` (`:203-243`) carries `expired_pages` at `:214-216` ("pages
under {wiki} + {research} whose frontmatter `review_after:` is in the past"). The
`expired_pages` derivation (`:617-630`) walks `{wiki}` + `{research}`, `scanned` counts
every page, `ra = _read_frontmatter_review_after(page)` and `ra is not None` **is** the
key-carrier predicate (the Q3 grounding correction: the hook already reads content —
only the local-metrics evaluator doesn't). The note (`:632-634`) reads:
`f"{scanned} pages scanned; a page without `review_after:` is evergreen and cannot
expire"` — `scanned` is the **wrong denominator** for judging staleness coverage (the
capture's sharpening: the stated denominator is all pages, not the eligible population).

**Change:** (a) add to `METRICS`, directly after the `expired_pages` entry:

```python
"pages_with_review_after": (
    "pages under {wiki} + {research} whose frontmatter carries `review_after:` — "
    "the eligible population `expired_pages` is judged against (its honest denominator)"
),
```

(b) in the loop, count carriers beside `scanned` (`carriers += 1` inside the
`ra is not None` branch), then after the loop:

```python
metrics["pages_with_review_after"] = carriers
```

(c) repair the note's denominator:

```python
notes["expired_pages"] = (
    f"of {carriers} pages carrying `review_after:` ({scanned} scanned); a page "
    "without the key is evergreen and cannot expire"
)
```

No new scan, no second walk — the number was already in hand inside a loop that already
runs (Q3's near-free finding). Rendering needs no edit: `render_report` iterates
`METRICS` (`:736-742`), so the new metric auto-renders denominated by its definition;
`render_strip` renders tripped wires only (`:788-811`) — untouched. The shadow net
(`:326-330`) and `evaluate_wire`'s canonical-or-local legality (`:447-451`) pick the new
id up from `METRICS` membership automatically.

**Why:** Q3 direction 3 — the instance fix, and the honest-reporting repair: without the
carrier count, `expired_pages: 0` cannot distinguish *nothing is stale* from *nothing
carries the key* (the M0 audit's exact 2026-07 complaint, per the filing).

**Out of scope at this site:** `vlt-dispatch/references/ledger.md:39`'s display-only
vitals block is a subset-with-defaults listing (CLAUDE.md: point-at-the-map beats
enumeration) — the new metric renders in the vitals report regardless; do not append it
to the ledger's illustrative list.

### F6 — the field notice (roundtable A7; no working-tree file edited by the builder)

**Current state:** no v0.15.0 CHANGELOG entry exists; `vlt-release` Stage 3
(`.claude/skills/vlt-release/references/choreography.md:49-73`) authors it at release
time from the working tree's briefs.

**Change (obligation, not an edit):** the notice text staged in disposition 6 **must be
included in the v0.15.0 CHANGELOG entry** when `vlt-release` Stage 3 authors it — the
DA3 mechanism exactly (Cycle 10: "the notice text must be included there, and DA3
retires with it"). This brief's §8 carries the obligation where the release runner will
read it; ledger check 2 makes skipping it visible at the gate.

**Why:** E2(b)'s discharging event is a vault declaring the kind; a declaration cannot
come from a vault never told the route exists (D1's not-knowing failure mode applied to
the field contract — the A7 amendment's own words).

## Registration

**None.** No new skill or workflow; `module-help.csv` untouched; no convention
`version:` moves (neither `vlt-vitals.py` nor `tripwires.yaml` is a handshaked
convention — the registry header owns the `local_metrics:` schema and is updated in this
same build, F4). Priced non-handshake gates: **C8** is the check that touches this
build's surfaces (tripwires parses; wire metrics resolve against the imported `METRICS`;
the reader compiles) — it needs no edit and must pass; **C6** untouched (no
operating-contract edit); **E4** untouched (no new package-lint check); **E5** untouched
(no asset `depends_on:` header involved — `vlt-vitals.py` carries none).

## Out of scope (dispositioned)

1. **Direction 1 — a content predicate / `matching:` filter on `file_count`** — REJECTED
   at Q3; not an implementation fallback either (disposition 1's semantic is
   presence-only for this reason).
2. **The "superseded local instrumentation" install-report line** (the filing's carried
   context, the silent-supersession contributing pattern) — deliberately not a second
   filing by the filing's own choice; capture honored it; ideation did not promote it.
   File it from the field if it bites again.
3. **A shipped seed wire on the new metric** — the alert-fatigue budget is a hard
   constraint ("add a further wire only when a real failure earns it",
   `tripwires.yaml:72-74`); `pages_with_review_after` ships as a metric, not a wire.
4. **`vlt-dispatch/references/ledger.md:39` display list** — not widened (F5's per-site
   note; subset-with-defaults listings don't drift).
5. **B10-4 parts 2 and 3** — ride the E2 carry unchanged (the roadmap's Carried-in item
   2); nothing here builds them.
6. **A11-2 / the personal-handle trigger and every other Cycle-12 deferral** — untouched
   per the Round-1 deferral rationale.

## Verification (unit, at rest — lifecycle step 5)

1. **The fixture harness — the E2(a) instrument (R1: named here, at tag time).** A
   factory-side Python harness in the scratchpad (the package-lint C8 import pattern:
   `importlib.util.spec_from_file_location` against the shipped
   `skills/vlt-setup/assets/hooks/vlt-vitals.py` — the real asset, never a copy) run
   against a temp fixture vault: a structure map with `wiki`/`research` rows, a fixture
   `tripwires.yaml` whose `local_metrics:` declares `wiki-review-after-carriers` (kind
   `frontmatter_key_count`, `key: review_after`, `glob: "{wiki}/**/*.md"`, one-line
   `definition`), and fixture wiki pages of which a known subset carry `review_after:`
   (at least one expired, at least one page with no frontmatter at all). Recorded
   assertions, each one that could fail:
   - `parse_local_metrics` returns the declaration with **zero errors**;
     `derive_local_metrics` returns exactly the carrier count — **filing 190100's lost
     derive is expressible and derives correctly at rest** (E2(a) verbatim);
   - `derive_metrics` returns `pages_with_review_after` == the same carrier count and
     `expired_pages` == the expired count, and `notes["expired_pages"]` states the
     carrier denominator (the repaired wording, F5c);
   - `render_report` renders the new canonical row and the local row denominated;
   - negative cases error **loudly, per entry**: a declaration missing `key:`; a
     malformed `key:` token; an unknown kind (unchanged behavior); an id
     `pages_with_review_after` firing the **shadow** error (disposition 4 — the newly
     canonical id is refused locally);
   - `evaluate_wire` accepts a fixture wire whose `metric: pages_with_review_after`
     (canonical legality) and one referencing the local id (local legality).
   Evidence: the recorded case results in this brief's BUILT status.
2. **Compile + packaging lint:** `uv run tools/package-lint.py` mid-cycle **A/B/C/E**
   run passes (C8 re-imports the edited asset and re-parses the edited seed — the
   no-trap claim exercised live, not trusted). D/`--expect-version 0.15.0` is the
   release gate (§8), not this build's.
3. **Single-home greps:** `grep -rn "frontmatter_key_count" skills/` hits **only**
   `vlt-vitals.py` and `tripwires.yaml` (no restated enumeration grew anywhere);
   `grep -rn "pages_with_review_after" skills/ tools/` hits only `vlt-vitals.py`
   (aids-while-editing; the recorded checks are 1 and 2).
4. **Handshake bipartite re-check: not triggered** — no `version:`/`consumers:`/
   structure-map change; Group E still runs green inside verification 2's A/B/C/E.
5. **R2 (fixture extension): not applicable** — no release-gate check added or changed.
6. **R3 (legal response):** the new per-entry validation errors join the existing
   local-metric loud-error class, whose legal response — fix the declaration per the
   registry header's schema — homes at the check's own single home, the `tripwires.yaml`
   header, updated in this same build (F4). No lint/dispatch finding class is added.
7. **R4 (enumeration widening): not applicable** — the build adds no file to any
   enumerated class (it adds a metric to the very table that IS the enumeration, at its
   single home).
8. **Scrub:** no personal or vault-local content in either edited asset or the staged
   notice — the notice names issue #1 (public tracker) and no vault; fixture content
   lives in the scratchpad, never the tree; no `.decision-log.md` left on disk.

## Release (build-9 is the last build of v0.15.0 — held for owner approval)

The release is **not** the builder's act. On owner approval, `vlt-release` runs the
choreography: dual version bump to `0.15.0` (`.claude-plugin/marketplace.json`
`"version"` + `skills/vlt-setup/assets/module.yaml` `module_version`), Stage-3 CHANGELOG
`## v0.15.0 — <date>` entry — **which MUST include the field-notice text staged in
disposition 6 verbatim (roundtable A7 via the DA3 mechanism; ledger check 2 gates on
it)** — then `uv run tools/package-lint.py --expect-version 0.15.0` (tag only on exit 0,
PASS line in the release commit message), ff-merge to `main`, tag `v0.15.0`, push main +
tag.

## Acceptance (live — appended to the roadmap ledger)

Three checks (checks 1 and 3 = E2's ruled halves per roundtable A7; check 2 = the A7
field-notice obligation).

1. **`[ship-verifiable]` — GATES closeout (E2(a)):** a fixture `local_metrics:`
   declaration expressing the known lost content-filtered derive (filing 190100's case —
   pages whose frontmatter carries `review_after:`) validates and derives correctly at
   rest under build-9's fourth kind, declared under a non-shadowing id (the literal
   `pages_with_review_after` now being canonical, the shadow net refusing it loudly is
   itself a checked case) — the discharge route proven expressible before the field is
   asked to use it; alongside it, direction 3 holds at rest: `pages_with_review_after`
   derives canonically and the `expired_pages` note states the carrier denominator.
   Instrument (R1): the brief's Verification-1 fixture harness — a factory-side Python
   run importing the shipped `vlt-vitals.py` asset against a temp fixture vault, positive
   and loud-negative cases enumerated in the brief. Evidence: the recorded case results
   in the brief's BUILT status.
2. **`[ship-verifiable]` — GATES closeout (the A7 field notice):** the v0.15.0 CHANGELOG
   entry includes the staged notice text naming the fourth kind and the lost-derive case
   it exists for (the DA3 CHANGELOG-notice mechanism — the notice is how E2(b)'s
   declaring event becomes possible at all). Instrument (R1): a read of `CHANGELOG.md`'s
   `## v0.15.0` entry at the release gate (the release is scheduled — the cycle's own
   one-release ruling — so the check is bounded); evidence: the notice text present in
   the shipped entry.
3. **`[field-contingent]` — does not gate (E2(b)):** a live vault actually declares a
   content-filtered derive — the first genuine `local_metrics:` declaration of kind
   `frontmatter_key_count` in a live vault, validating and deriving on that vault's own
   vitals surface (the class route used live; the literal lost instance arrives
   canonically at upgrade, so the event is the class's next need, not the old id —
   brief disposition 5). Vault: `{field-vault}` (readable; the vault whose honest
   refusal filed 190100). Event: unbounded by construction — a declaration is a rare
   human-gated registry write that nothing schedules; B10-4(4) discharges on it, and
   B10-4 parts 2 and 3 ride the same carry; goes to the standing watch register at
   closeout.
