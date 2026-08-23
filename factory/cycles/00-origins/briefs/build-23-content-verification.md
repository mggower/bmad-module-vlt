---
title: 'Build #23 — content-verification (give the release gate eyes: the module cannot see itself)'
status: 'BUILT 2026-07-18 — F1–F3 added check_group_e (E1/E2/E3) to tools/package-lint.py; F4 appended the honest-limit sentence to vlt-lint:74. Group E PASSES clean; all five seed-tests ring (E1 stale/unacknowledged/dangling, E2 missing-key + path-mismatch reproducing A3-10, E3 stray-pin naming file:line). DEVIATION: the brief F4 parenthetical cites `roadmap :1682` — NOT shipped into vlt-lint (the roadmap is a gitignored dev artifact a vault reader cannot see; scrub / placeholder-paths discipline). The pointer-vs-ack RULE is shipped in prose instead; the literal `roadmap :1682` cite lives only in the E3 failure message inside tools/package-lint.py (dev-side, maintainer-facing). Release (v0.7.0) pending owner go.'
module_code: 'vlt'
created: '2026-07-18'
derives_from:
  - 'inbox/2026-07-13-092341-spec-convention-has-no-advocate.md (A3-12 — the de-facto unlisted consumer: vlt-upgrade:75 recited spec.md with no depends_on; build-15''s own verification grep searched for the ack, not the consumption)'
  - 'inbox/2026-07-17-090000-extraction-grant-authorizes-nobody.md (A3-14 — prose asserts a fact about the shipped surface ("no skill shipped uses it") that nothing re-reads; false since v0.4.0)'
  - 'inbox/2026-07-12-114910-dev-zone-contract-graduation.md (A3-10 — the contract structure map hand-transcribes an SSoT that declares itself never-hand-transcribed, and drifted)'
  - 'inbox/2026-07-11-114226-research-note-graduation-queue.md (A3-7 — vlt-research acked frontmatter@3 while emitting a scalar the convention forbids: the ack verified the pin, never the content)'
  - 'inbox/2026-07-17-100000-loop-profile-drift.md (A3-17 — acceptance discharged against a non-adopting population; the class instance, ruled OUT of this build — see Out of scope)'
roadmap: 'skills/reports/inbox-evolution-arc3-roadmap.md'
rulings: 'roadmap §Ideation rulings A3-7..A3-17 (2026-07-17): checks-verify-shape-never-content is a NEW item with its OWN build (:1676), deliberately last so its shape benefits from watching builds 19–22''s own verification passes (:1628); NOT folded into build-17''s event-record machinery (these are absences), NOT a lint extension by default — the build decides its checks'' homes; carries no numbered question — its scoping is the brief''s whole job (:1741). Pointer-vs-ack line (:1682): a site that must change when the rule changes is a consumer and acks; a site that survives any rule change unedited is a pointer and never acks.'
risk: 'low — the primary surface is tools/package-lint.py (dev-side release gate, non-shipped, no own-the-apply copy). No convention version moves; no consumer walk. The one shipped edit (vlt-lint honesty clause) is truth-in-documentation, not a new vault check. Release build: bumps both version strings 0.6.0 → 0.7.0.'
---

# Build #23 — content-verification

Arc 3's eleven run-2 filings share one root, stated in the roadmap's revised spine
(`roadmap §Part 2`, `:85-123`): **the module's checks verify the shape of a declaration,
never its content**, so the module's own self-descriptions rot without anything noticing.
The handshake was bipartite-consistent while a consumer emitted a scalar the convention
forbade (A3-7); a skill recited a convention's mechanics with no `depends_on` and the
verification grep — searching for the *ack*, not the *consumption* — never saw it (A3-12);
convention prose asserted "no skill shipped uses it," false since v0.4.0 and falsified by
the very commit that shipped the check depending on it (A3-14); a hand-transcribed map
drifted from an SSoT that declares itself never-hand-transcribed (A3-10).

Builds 19–22 fixed each **instance**. This build gives the **class** a bell. Watching those
four builds' own verification passes (the ruling's stated reason for ordering build-23 last)
made the target sharp: **every one of builds 19–22 ran a bipartite-handshake grep that
searched for the ack string it had just written** (`grep "spec@"`, `grep "frontmatter@"`,
`grep "extraction@"`) — the exact self-confirming shape A3-12 names, rescued only by an
adjacent by-hand walk. And the counter-pattern that already works — build-22 F3's classifier
keying off the *pristine incoming source* rather than the polluteable declaration, build-14
B1's `merge-help-csv.py` keying off bundled source — points at the fix: **derive truth from
the authoritative surface, don't trust the declaration about it.**

The module-as-a-whole is validated exactly once, pre-tag, by `tools/package-lint.py` (groups
A–D). That is where the module can be made to *see itself* before it ships. Build-23 adds a
**Group E — self-description integrity** to that gate: a mechanical bipartite-handshake check
(retiring the self-confirming grep at its source), a structure-map-vs-SSoT agreement check
(A3-10's class), and a stray-pin net for a de-facto consumer's strongest recite-signal
(A3-12's class). The one shipped-surface edit states the honest limit of the vault-side
coherence check, so it stops implying a conformance guarantee it never made.

All rejected alternatives in the parent filings are settled — do not re-litigate. In
particular: the individual instances (A3-7/A3-10/A3-12/A3-14/A3-16/A3-17) are **already
shipped-fixed in builds 19–22** and are cited here only as the class this build generalizes,
never re-opened.

## Brief-time dispositions

Build-23 "carries no numbered question — its scoping is the brief's whole job" (`roadmap
:1741`). These dispositions ARE that scoping; each is grounded in the run-2 evidence and the
ruled homes-are-the-build's-call latitude (`:1676-1678`).

1. **Home = the dev-side release gate (`tools/package-lint.py`), not the shipped vault-side
   `vlt-lint`.** The class is about the *module's* self-descriptions rotting; the module is
   validated as a whole only at `package-lint` time (pre-tag, whole-tree). A vault-side check
   catches drift only *after* it ships. This is the literal answer to "the module cannot see
   itself," is fully mechanical (static analysis, no AI-judgment, no flakiness), and touches
   a non-shipped surface (`tools/` is tracked+public documentation of the release contract
   but is **not** part of the own-the-apply copy surface — CLAUDE.md), so it bumps no version
   and walks no consumers. The ruling's "not a lint extension by default" is honored: the
   default (a `vlt-lint` extension) is deliberately declined.

2. **Group E is three checks: E1 handshake-bipartite (hard), E2 structure-map SSoT (hard),
   E3 stray-pin (hard).** All three PASS on the current tree (builds 19–20 closed the live
   drifts), so Group E institutionalizes guarantees rather than fixing breaks — the correct
   posture for a gate (it must be green the moment it ships, or it can't gate its own
   release). See F1–F3.

3. **The full de-facto-consumer detector (A3-12's exact shape) is NOT fully mechanizable, and
   the brief says so rather than shipping a noisy check.** A3-12's `vlt-upgrade:75` recited
   `spec.md`'s heuristic in *prose* with no pin token — distinguishing that from a legitimate
   pointer is the pointer-vs-ack judgment (`:1682`), which is a human call, not a grep. E3
   catches the one high-precision, zero-false-positive recite-signal (a `name@version` pin
   token appearing outside `depends_on:`); the residual prose-recital class is closed by
   **doctrine**, not a check — the F4 honesty clause makes the pointer-vs-ack line explicit
   at the coherence check's own site. This mirrors build-21 F9's judgment that a check
   policing a negative no shipped code violates is not worth its false positives — but unlike
   F9, build-23 ships real bells for the mechanizable slices, because "state the rule without
   a bell" is the very disease this arc named.

4. **A3-14's general "negative-claim about the shipped surface" detector is out of scope as a
   standalone check** — detecting arbitrary factual assertions in prose is an NLP problem, not
   a lint. Its instance is fixed (build-21 deleted `extraction.md:47`/`:121`), and its
   residual is mitigated two ways already in this build: E1's bipartite report makes the
   specific extraction-style contradiction (prose says "nobody uses it" while `consumers:`
   names three) *visible* to a human reading the gate output, and F4's doctrine states that
   claims about the shipped surface must be derivable, not asserted. Dispositioned, not
   dropped silently — see Out of scope.

5. **The vault-side conformance spot-check is the named second cut**, not this build. Extending
   `vlt-lint:74` to re-read each installed consumer's *body* against the convention's rules is
   inherently AI-judgment (higher false-positive, flakier) and would catch vault-local minted
   reciters — a lower-frequency surface with no field evidence of drift yet. Deferred with a
   live home (Out of scope), per A3-13's lesson that deferral without tracking is its own
   failure.

## F1 — `package-lint.py` Group E1: handshake bipartite completeness (hard check)

**Current state.** The version handshake is validated **only** at vault runtime, by
`vlt-lint/SKILL.md:74` (Convention coherence), and — critically — at **dev/release time by
nothing**. Every build in this arc hand-grepped it instead: `build-19-spec-followup.md`
Verification ran `grep -rn "spec@" skills/*/SKILL.md` (searches for the ack it just wrote);
`build-20-graduation-queue.md` ran the same for `frontmatter@`; `build-21-history-writes.md`
for `extraction@`. `build-19:140-141` even *diagnoses* the failure ("its grep searched for
the *ack*, not the *consumption*") while `:304` repeats the pattern. `package-lint.py`
`check_group_c` (`tools/package-lint.py:151`) already parses `module.yaml` and
`marketplace.json` and cross-checks agreement, but does not read the convention↔consumer
handshake at all.

Ground truth at brief time (re-verified 2026-07-18 — all HOLDS):
- Conventions carrying `version:`+`consumers:` (`skills/vlt-setup/assets/governance/_meta/conventions/*.md`):
  `extraction@3` → `[vlt-extract, vlt-lint, vlt-track]`; `frontmatter@4` →
  `[vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-mint]`; `spec@1` →
  `[vlt-mint, vlt-dispatch, vlt-upgrade, vlt-lint]`; `wiki-consolidation@1` → `[vlt-ingest]`;
  `wiki-index@2` → `[vlt-ingest, vlt-lint]`; `wiki-supersession@1` →
  `[vlt-ingest, vlt-lint, vlt-extract, vlt-track]`; `write-verification@1` →
  `[vlt-ingest, vlt-extract, vlt-research, vlt-lint]`.
- Acks (`skills/*/SKILL.md` `depends_on:`): all seven conventions are currently
  **bipartite-consistent** (every listed consumer acks at the current version; every acker is
  listed; no dangling entry). Verified by hand against the lists above.

**The exact change.** Add `check_group_e(root)` to `tools/package-lint.py` and wire it into
`main()`'s `results` dict (`:220-225`) as `results["E"] = ("self-description integrity",
check_group_e(root))`, printed by the existing loop (`:230-239`). E1 is one of three failure
lists Group E aggregates. E1's logic:

- Glob `skills/vlt-setup/assets/governance/_meta/conventions/*.md`; for each, parse the
  `version:` and `consumers:` frontmatter (reuse the `yaml` import already loaded at `:37`).
  Skip a file lacking both (that omission is `vlt-lint:75`'s `convention_meta_missing`
  jurisdiction at vault time; Group E's remit is the handshake, not enforcement frontmatter —
  do not duplicate it here).
- Glob `skills/vlt-*/SKILL.md`; parse each `depends_on:` list into `{name: version}`.
- **FAIL** (append one message per defect, matching `vlt-lint:131`'s vocabulary so the two
  homes read alike):
  - **stale** — a listed consumer whose `depends_on` pins an older version than the
    convention's current `version:` (`<consumer> acks <name>@<N> but convention is @<M>`).
  - **unacknowledged** — a listed consumer with no `depends_on` entry for the convention
    (`<consumer> is a listed consumer of <name>@<M> but does not ack it`).
  - **dangling** — a `consumers:` entry naming a skill directory that does not exist under
    `skills/` (`<name>@<M> lists <consumer> which is not installed`).

**Why.** This is the dev-side twin of `vlt-lint:74`, run before every tag, and it **retires
the self-confirming grep every sibling build wrote by hand** — the fix derives the answer
from both sides of the handshake and compares them, rather than confirming that a string it
expects is present. It closes the *listed-but-drifted* sub-class of A3-12 (a consumer that
falls out of sync) permanently at the gate.

**Out of scope at this site.** E1 does **not** catch A3-12's actual instance — an *unlisted*
reciter (`vlt-upgrade:75`, which was in neither list) — because a skill in neither the
`consumers:` nor an `depends_on` is invisible to a bipartite comparison. That residual is
E3's high-precision slice plus F4's doctrine; say so in the F4 disposition, not here.

## F2 — `package-lint.py` Group E2: structure-map ↔ SSoT agreement (hard check)

**Current state.** `skills/vlt-setup/assets/module.yaml:41-59` declares itself the
**SINGLE SOURCE OF TRUTH for the structure map** (comment `:41`: "CANONICAL default map";
`:42-43`: "vlt-setup reads this (never a hand-transcribed markdown table)"). The contract at
`skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md:31-45` carries a
hand-transcribed table of the same map, and its own note (`:47`) says the path-value column
"mirror[s] `module.yaml`'s `vault_structure.default` … don't hand-transcribe it." A3-10's
finding: the table nonetheless drifted (it lacked the `specs` row until build-19 added it at
F3) — a completeness list that fell behind an SSoT, exactly the standing rule's warning.
Nothing checks the mirror.

Ground truth at brief time (re-verified 2026-07-18 — HOLDS, currently in agreement):
- `module.yaml vault_structure.default` keys (`:45-59`): `wiki, index, research, sessions,
  specs, log, backlog, partners, capabilities, conventions, overlays, personas, contract,
  upgrade_ledger, archive` (15).
- Contract table rows (`vault-operating-contract.md:31-45`): the same 15 logical names, same
  path values in the middle column. **In agreement** — build-19 F3 closed the drift.

**The exact change.** E2, a second failure list inside `check_group_e`:

- Parse `module.yaml` `vault_structure.default` into `{key: path}` (the file is already
  loaded by `check_group_c` at `:154`; either re-read it or thread the parsed object — a
  re-read keeps Group E self-contained and is cheap).
- Parse the contract's structure-map table. It is the pipe-table under the
  `## Path resolution — the structure map` heading; each data row is
  `` | `key` | `path` | description | ``. Extract `key` (first cell, backtick-stripped) and
  `path` (second cell, backtick-stripped) for every row whose first cell is a backticked
  logical name. Anchor the parse on the heading + the table's header/separator rows so prose
  pipes elsewhere in the file are not mis-read.
- **FAIL** on any disagreement: a key in one and not the other
  (`structure map: <key> in <source> but not <other>`), or a matching key whose path value
  differs (`structure map: <key> path <a> (contract) != <b> (module.yaml)`).

**Why.** A3-10's class: a hand-transcribed completeness list drifting from its declared SSoT.
Deriving both sides and diffing is the "authoritative source, not the declaration" pattern;
it makes the map's own `:47` promise ("don't hand-transcribe it") enforced instead of merely
stated.

**Out of scope at this site.** E2 checks only the structure map against its one declared SSoT.
Generalizing to "every completeness list in the module" is not mechanizable (most lists have
no machine-readable SSoT); do not attempt it — the standing single-home/point-at-the-map rule
governs the rest by review.

## F3 — `package-lint.py` Group E3: stray-pin net (hard check)

**Current state.** A `name@version` pin token (`spec@1`, `frontmatter@4`) is the module's
strongest machine-detectable signal of convention *consumption* — you write it only to pin.
It legitimately lives in exactly one place: a skill's `depends_on:` list. A3-12's residual
(a skill reciting a convention it doesn't ack) has no general mechanical detector, but its
*strongest* signal does: a pin token appearing in a SKILL.md **body** (outside `depends_on:`)
is a near-certain de-facto-consumption tell with near-zero false positives.

Ground truth at brief time (re-verified 2026-07-18): `grep -rnE "\b[a-z-]+@[0-9]+\b"
skills/*/SKILL.md` returns pin tokens **only** on `depends_on:` lines — no stray body pins
today. E3 PASSES on the current tree.

**The exact change.** E3, a third failure list inside `check_group_e`:

- For each `skills/vlt-*/SKILL.md`, scan every line that is **not** the `depends_on:` line for
  a `name@version` token matching a known convention name (the set parsed in E1) followed by
  `@<digits>`. Match on the convention-name-anchored form, not a bare `\w+@\d+`, so an email
  address or an unrelated `foo@2` cannot trip it.
- **FAIL**: `<skill>:<line> recites the pin <name>@<N> outside depends_on: — a de-facto
  consumption signal; add it to depends_on: and the convention's consumers:, or rewrite the
  reference as a version-free pointer (pointer-vs-ack: roadmap :1682)`.

**Why.** Closes the one high-precision slice of A3-12 that a grep *can* own, and does it the
right way — the failure message names the pointer-vs-ack ruling so the builder/maintainer
resolves it as a judgment (register as consumer, or de-pin to a pointer), never by rubber-
stamping. The broader prose-recital residual is F4's doctrine.

**Out of scope at this site.** E3 does not attempt to detect prose that *describes* a
convention's mechanics without using a pin token (A3-12's literal instance) — that is the
pointer-vs-ack judgment, not a grep (disposition 3). No heuristic body-scan; the false-
positive cost is not worth it.

## F4 — `vlt-lint/SKILL.md`: the coherence check's honest limit (shipped edit)

**Current state.** `vlt-lint/SKILL.md:74` (Convention coherence) validates the pin: it reads
each listed consumer's `depends_on` and confirms the version matches. It never re-reads the
consumer's *body* to confirm the body actually conforms to the convention's rules — the exact
gap A3-7 fell through (vlt-research acked `frontmatter@3` while `:65` emitted a scalar the
convention forbade). `:101` already gestures at the limit ("lint must never bump the integer
itself, or it would rubber-stamp conformance it didn't verify") but the check's own bullet
at `:74` states no limit, so a reader takes "coherence" to mean conformance.

**The exact change.** Two small, single-home edits — no new check, no version move:

- At `vlt-lint:74`, append one sentence to the Convention coherence bullet stating the scope
  boundary explicitly: the check verifies the **pin** (that each listed consumer acks the
  current `version`), **not** that a consumer's body conforms to the convention's rules —
  content-conformance is out of this check's jurisdiction. Cite the pointer-vs-ack line so a
  skill that recites a convention's mechanics is understood to owe an ack, and a skill that
  merely points is not a consumer (`{conventions}` pointer-vs-ack; roadmap `:1682`). Keep it
  to one or two sentences — single-home, no restatement of `:101`'s auto-fix rationale
  (point at it if needed).
- Confirm `:101`'s existing clause still reads coherently beside the new limit sentence (it
  does — `:101` is about *why lint doesn't auto-fix* drift; `:74`'s new sentence is about
  *what the check does not inspect*). No edit to `:101` required unless the wording collides.

**Why.** Truth-in-documentation: the shipped surface must not imply a conformance guarantee it
does not provide — that implication is itself an instance of the arc's class (a self-
description asserting more than the code delivers). It also names, at the vault-side check's
own site, where the *dev-side* net for this class lives (package-lint Group E), so a future
maintainer reading `vlt-lint:74` learns the two-home division.

**Out of scope at this site.** No conformance spot-check is added to `vlt-lint` (disposition
5 — named second cut). No convention `version:` moves; F4 changes a skill's prose, not a
convention rule, so per `vlt-mint:139` (prose clarification does not bump) there is no
handshake and no consumer walk.

## Registration

**None.** The primary surface (`tools/package-lint.py`) is dev-side release tooling, not a
shipped skill/workflow/convention — it registers nothing in `module-help.csv`,
`marketplace.json`, or any convention `consumers:` list. The F4 edit is a prose clarification
to an existing skill: no new capability, no version bump, no consumer walk (`vlt-mint:139`).

## Out of scope (dispositioned)

- **Vault-side conformance spot-check** (extend `vlt-lint:74` to re-read each installed
  consumer's body against the convention rules) — **deferred, named second cut** (disposition
  5). AI-judgment-heavy, higher false-positive; targets vault-local minted reciters, a
  surface with no field evidence of drift yet. Live home: this bullet + the next arc roadmap's
  carry-forward, not a note in a closable tree (A3-13's lesson).
- **A3-14 general negative-claim detector** ("no shipped X uses Y" prose re-verified against
  the tree) — **rejected as a standalone check** (disposition 4): detecting arbitrary factual
  prose assertions is NLP, not lint. Instance fixed (build-21, `extraction.md:47`/`:121`);
  residual mitigated by E1's visible bipartite report + F4's doctrine.
- **A3-17 acceptance-ledger vacuity** (an acceptance check dischargeable against a non-
  adopting population) — **out of this build; already ruled as a dev-lifecycle principle**
  (roadmap Gate 2 / Q28, `:1440-1454`: "a discharge must name an instance that could have
  failed — no vacuous discharge"). It governs the acceptance-discharge tooling
  (`.claude/skills/acceptance-discharge`, gitignored dev surface), not module source; a build
  brief has no shipped F-site for it. Named here so it is not re-raised as build-23's.
- **A3-16 instructions-outlive-their-model** (`vlt-mint:152` self-registration) —
  **judgment-heavy, out of scope**; instance fixed in build-22 (F3 classifier hardening). No
  general mechanical detector of "an instruction whose model has changed" exists; the
  durability-net posture (builds 6/18/22) is the standing answer.

## Verification (unit, at rest — lifecycle step 5)

Run before any commit. Because build-23 modifies the release gate itself, its own release
(§8) exercises the new Group E — the strongest possible unit test.

- **Group E currently PASSES.** `uv run tools/package-lint.py` prints `PASS group E —
  self-description integrity` with no E1/E2/E3 failures on the clean tree. (If it FAILs on the
  current tree, a real drift exists that builds 19–22 missed — investigate before proceeding;
  do not weaken the check to make it green.)
- **E1 catches a seeded stale ack.** Temporarily flip one `depends_on` entry (e.g.
  `vlt-lint`'s `spec@1` → `spec@0`) in a temp copy / working edit and confirm Group E FAILs
  with a `stale` message naming vlt-lint and spec; revert. Do the same for an
  **unacknowledged** case (drop the entry) and a **dangling** case (add a bogus name to a
  convention's `consumers:`).
- **E2 catches a seeded map drift.** Temporarily delete the `specs` row from the contract
  table (or change a path value) in a temp copy and confirm Group E FAILs naming `specs`;
  revert. This reproduces the exact A3-10 defect and proves the bell rings on it.
- **E3 catches a seeded stray pin.** Add `frontmatter@4` to a SKILL.md body line (not
  `depends_on:`) in a temp copy and confirm Group E FAILs naming the file:line; revert.
- **E3 does not false-positive.** Confirm the clean tree yields zero E3 hits (pin tokens live
  only on `depends_on:` lines today — grep to confirm the baseline before trusting the check).
- **F4 single-home grep.** The new `vlt-lint:74` limit sentence exists; it does not restate
  `:101`'s auto-fix rationale (points at it or stands independent); `grep -n "conform"
  skills/vlt-lint/SKILL.md` shows the limit stated once, not duplicated.
- **Handshake bipartite re-check** — **N/A**: no convention `version:` moved this build
  (F4 is prose). Confirm by grep that no `{conventions}/*.md` `version:` changed.
- **Group A cruft** — no `.decision-log.md` / `__pycache__` left by the Python work
  (`sys.dont_write_bytecode` is already set at `tools/package-lint.py:41`; confirm none
  landed). `node --check` — N/A (no workflow edited).
- **Scrub** — no personal/vault-local content in any changed file; `package-lint.py` and the
  `vlt-lint` edit use logical names / placeholder forms only.

## Release (release build — v0.7.0)

Build-23 is the **last build of Arc 3's v0.7.0** (builds 19–23; build-17 trails to a later
version, evidence-blocked per roadmap `:1631-1633`). It carries the release:

- **Dual version bump 0.6.0 → 0.7.0:** `.claude-plugin/marketplace.json` `"version"` **and**
  `skills/vlt-setup/assets/module.yaml` `module_version` (CLAUDE.md release rule; both
  strings, same commit).
- **Pre-tag gate:** `uv run tools/package-lint.py --expect-version 0.7.0` — **tag only on
  exit 0.** This run exercises build-23's own new Group E alongside A/B/C/D; record the PASS
  summary line (all of A/B/C/D/E PASS, D asserting 0.7.0) in the release commit message.
- **Sequence:** commit (one commit for the build) → `uv run tools/package-lint.py
  --expect-version 0.7.0` PASS → ff-merge `arc3-v0.7.0` → `main` → tag `v0.7.0` → push main +
  tag. Use the `vlt-release` skill to run this as one gated sequence.
- If the owner re-sequences the release (e.g. cuts v0.7.0 without build-23, or pulls build-17
  in), the version bump moves with the last build — this section assumes the roadmap's stated
  19–23 grouping.

## Acceptance (live — appended to the roadmap ledger)

Behavioral checks riding the next vlt-core / vlt-sayari upgrade to 0.7.0:

- **The gate rings on real drift, not just seeds.** The next arc's first build that touches a
  convention `version:`, a `consumers:` list, or the structure map runs `package-lint`
  Group E as its handshake verification **instead of** a hand-written `grep "<name>@"` — and
  the brief/commit shows Group E, not the self-confirming grep, as the check of record. (This
  is the process-adoption proof: the self-confirming grep stops being written because the gate
  now owns the check.)
- **A non-vacuous catch.** Group E FAILs at least once on a genuine mid-development drift
  (a consumer walk missed a re-ack, or a map row lagged an SSoT edit) before that drift can be
  tagged — caught at the gate, not in a later field filing. If v0.7.0 → next-version dev
  produces no such drift, the discharge is **vacuous by construction** (Gate 2 / Q28,
  roadmap `:1440`) and must be recorded as such, not silently passed — an explicit owner note
  that no qualifying drift arose, never a substitute instance.
- **F4 in the field.** A maintainer or minted partner reading `vlt-lint:74` in an installed
  vault understands the coherence check verifies the pin, not conformance, and knows the dev-
  side net (package-lint Group E) exists — evidenced by a field interaction (an upgrade note,
  a mint council reference, or an inbox filing) that cites the limit correctly rather than
  re-filing "the handshake passed but the body drifted" as a new defect.
