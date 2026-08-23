---
title: 'Build #B5-9 — the enforcement kit (registry, moment, surface — the promise three releases of shipped prose already make)'
status: 'BUILT 2026-07-30 — F1–F10 + registration landed as briefed; verified at rest per the Verification section (package-lint A/B/C/E PASS with C8 live + three temp-copy negatives each FAILing correctly; C6 stale-SHA FAIL observed then re-stamped PASS; Group E bipartite frontmatter@5 ↔ all six consumers incl. vlt-dispatch first ack; test-cost-manifest 7/7 green after the substrate re-home; vitals fixture runs hand-verified in both modes with green-silence, vitals-unavailable, and loud-wire-error cases; settings-merge demo idempotent with the vault-local hook byte-identical; strict-YAML fence PASS with counter_unknown_metric; single-home greps clean; scrub clean; no commit — release rides the arc level). Deliberate deviations, numbered: (1) the SessionStart-hook idempotency key is the bare script path `vlt-vitals.py`, not the full `vlt-vitals.py --strip` invocation string — the at-rest merge demo caught that quoting between path and flags defeats the longer substring; the command-path key intent is kept, made robust. (2) package-lint C8 imports WIRE_REQUIRED_FIELDS from the asset alongside METRICS (the parse-dont-re-declare posture extended to the wire field list), and its py_compile writes the .pyc to a throwaway temp path so the check cannot shed the __pycache__ cruft group A polices. (3) test-cost-manifest EXPECTED_FALLBACKS grew by the two new canonical keys (tripwires, lint_reports) — the assertion follows the F3 rows per the brief clause that assertion text may follow renames; the truth table did not shrink. (4) boundary ruling the brief left implicit: a missing {log} is a reader FAILURE (vitals unavailable — fails loud per the false-healthy-strip clause), while an absent registry stays a plain denominated zero (a fresh vault before seeding), and a wire whose metric is underivable on this vault (e.g. no dated dispatch header above an open row) evaluates ok-with-reason, never a silent trip.'
module_code: 'vlt'
created: '2026-07-30'
derives_from:
  - 'inbox/2026-07-06-091003-enforcement-kit-derive-first.md (A5-19: changes 1–8 minus the two Arc-3 re-homed pieces; latent bugs 1–3; the derive-first invariant; the blocked_on rider; M0 evidence debt)'
  - 'inbox/2026-07-26-142500-boundary-classifier-five-verdicts-and-an-unmeasurable-metric.md (A5-7: shape 3, the never-rung streak; shape 2 ruled NOT-BLOCKING, stays field/owner)'
  - 'inbox/2026-07-29-120004-lint-report-block-is-never-persisted.md (A5-18: the persistence home, ruled here under the derive-first rule)'
roadmap: 'skills/reports/inbox-evolution-arc5-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-07-29): B5-9 = A5-19 + A5-7 + A5-18, ships last; extends B5-1''s substrate, never lays a second one (pre-ideation ruling 1); A5-7 streak + A5-18 persistence RIDE the kit (grouping); A5-7 shape 2 NOT-BLOCKING (evidence-debt disposition); POST-HOC DEFAULT cited (cross-filing ruling 1, 2026-07-30); 091003 M0 + parked Arc-3 rulings re-read pinned to this brief (spike section) — discharged below.'
risk: 'moderate — the arc''s biggest build: one convention bump (frontmatter 4→5, six-consumer walk incl. vlt-dispatch joining), first-ever vault-side hook/settings.json provisioning, a substrate re-home that cost-manifest must survive (harness 7/7), and a new package-lint check (C8). Every write moment is human-gated or module-owned; no vault-grown state is touched destructively.'
---

# Build #B5-9 — the enforcement kit

Vault state lives in prose, so nothing can count, trigger, or trip — and since v0.6.0 the
shipped surface *promises* the mechanism that would fix that: `vlt-lint` twice defers
escalation to "a tripwire concern (the enforcement kit)" (now
`skills/vlt-lint/references/checks.md:17` and `:64` after the B5-8 re-cut), and
`conventions/frontmatter.md:231` holds an `enforcement_counter:` slot "optional until the
enforcement kit lands." This build lands it: the **registry** (`_agent/tripwires.yaml`),
the **moment** (a SessionStart health strip), and the **surface** (a computed Tripped-wires
section in `vlt-dispatch ledger`) — with the **vitals derivations extending B5-1's shared
measurement substrate**, never laying a second one (pre-ideation ruling 1). Riding the kit
per the grouping ruling: A5-7's never-rung classifier streak becomes a derived, denominated
display line, and A5-18's lint report block gets its persistence home. The `blocked_on`
rider ships as part of the ledger-surface work, per the filing's own fold-in and the parked
Arc-3 question designated to this brief.

**All rejected alternatives in the parent filings are settled — do not re-litigate.** In
particular: **stored counters are rejected as a design invariant** ("no mutable stored
counters — derived or append-only state only" — 091003's recorded recursion-trap analysis);
the Warden partner, weekly bell-review, stored auto-created ledger rows, scheduled headless
runs, the no-go gate, and debt-aware ingest are all rejected/deferred behind their filed
triggers. The pre-hoc/post-hoc question is **RULED: POST-HOC DEFAULT** (roadmap
§Cross-filing rulings, 2026-07-30) — cited, never re-litigated; the kit is named there as
part of the post-hoc side ("B5-9 kit incoming"): it is the cheap-correction machinery the
ruling leans on, not a new pre-hoc gate. The strip is one line, tripped-wires-only, silent
when green — the attention budget is a hard constraint from the filing.

## Pinned pre-brief obligation — DISCHARGED

The roadmap's spike section pins the **091003 M0 + parked Arc-3 rulings re-read** to this
brief, before scoping. Discharged 2026-07-30:

- **091003 M0 (counter-accuracy audit + tripwire-hit data)** — re-read in full
  (`inbox/2026-07-06-091003-enforcement-kit-derive-first.md`, filing-status paragraph +
  §Provenance). The debt remains **unpayable until counters exist** — exactly the standing
  Arc-3 ruling ("re-read at build-17 brief time … the brief resolves the circularity rather
  than inherits it", Arc-3 archive §Evidence-debt dispositions). Resolution: this build is
  what makes the debt payable. The audit becomes **acceptance check 2's named field event**
  (below): after the kit ships, the owner hand-counts ingests-since-lint and open pointers
  once against the vitals output on vlt-core. The vault-local probe numbers in the filing
  (175/184 strict grammar conformance, the 4-pointer board) are 2026-07-06 snapshots — the
  audit re-derives fresh, never reuses them.
- **Parked Arc-3 rulings** — re-read at the archive
  (`skills/reports/archive/inbox-evolution-arc3-roadmap.md`): (a) build-17's remit is
  "unchanged **minus the two re-homed pieces**" (adoption facet → build-20's `frontmatter@4`,
  shipped v0.7.0; spec-advocacy cadence → build-19, shipped v0.7.0) — this brief scopes
  neither; (b) the two **parked questions re-open here**: `days_since_lint` seed-wire vs
  display-only, and the `blocked_on` shape — both ruled in Brief-time dispositions below,
  per the roadmap's questions-designated-to-B5-9 line; (c) the Arc-3 **cross-filing
  decide-once rulings still bind**: module-owned executable code lives at
  `{root}/.claude/hooks/` beside the workflows force-reinstall precedent (ruling 1);
  **lint/dispatch find, tripwires nag** — one finder per fact, one nagger overall
  (ruling 2); lint-as-moment-owner honesty ceiling until the lint-debt wire lands
  (ruling 3); the hardcoded `_agent/dispatch.md` read is accepted (ruling 4).

## Re-grounding (against the working tree 2026-07-30: HEAD `2f19251` + uncommitted B5-4..B5-8 edits)

Every A5-19/A5-7/A5-18 capture site re-verified. **Zero grounding corrections** — every
site HOLDS in substance; the B5-8 whale re-cut re-homed several lint/dispatch sites into
`references/` (documented in the roadmap's B5-8 BUILT record), so the fresh addresses below
supersede the capture's pre-recut line numbers without changing any premise:

- `module.yaml` `vault_structure.default` (`skills/vlt-setup/assets/module.yaml:39-59`)
  carries **no `tripwires:` entry** — HOLDS.
- No vitals script anywhere in `skills/`; `skills/vlt-setup/assets/` holds only
  `governance/`, `workflows/`, `module-help.csv`, `module.yaml` — HOLDS (latent bug 3
  intact: `vlt-setup/SKILL.md` has zero hook-install or `settings.json` capability; its
  only "overwrite on every run" outside workflows is the interop cache yaml at `:254`).
- The dangling referents: `vlt-lint` description "proactively after several ingestions"
  (`skills/vlt-lint/SKILL.md:3`, no counter behind it); "escalation of an aging queue is a
  tripwire concern, not lint's" (**moved by B5-8** → `skills/vlt-lint/references/checks.md:17`);
  "a **tripwire concern (the enforcement kit)**, not lint's" (**moved** → `checks.md:64`);
  `enforcement_counter: <optional until the enforcement kit lands; …>`
  (`conventions/frontmatter.md:231`) — all HOLD.
- `vlt-dispatch` `ledger` mode (**moved by B5-8** → `skills/vlt-dispatch/references/ledger.md`,
  whole file, 1,811 bytes) has no Tripped-wires section; read-only + "writes no `{log}`
  entry" confirmed (`ledger.md:3`, router `SKILL.md:82`); Verify block at `ledger.md:21-27` — HOLDS.
- Lint Step 0's two-definitions seam (latent bug 1): last-lint grep + `find … -newermt`
  mtime scoping at `skills/vlt-lint/SKILL.md:25-32`; Step 6 lint log entry (the counter
  reset by derivation) at `:62-70` — HOLDS.
- Contract `{log}` section (`vault-operating-contract.md:114-137`): canonical one-line
  grammar at `:118-122`, "Keep it parseable" at `:116`, paren "Omit only for a partner-less
  generic-agent operation" at `:124`, keep-the-shape for new types at `:123` — HOLDS
  (change 4 is the tighten-and-relabel residual, exactly as captured).
- Mint/council wire-rule hosts: boundary classifier at `vlt-mint/SKILL.md:42` (bell or
  complete tripwired deferral, per frontmatter.md — build-16's shipped form of change 7);
  Step 2a capture `:93-102`; convention-edit enforcement frontmatter `:138`; council
  verdict return `vlt-review-council/SKILL.md:43-46`. No non-convention
  deferral-registers-a-wire rule exists anywhere — HOLDS (the reconcile-the-two-forms
  demand from the capture is real; see disposition 7).
- A5-7 shape 3: classifier verdicts are recorded per mint (`vlt-mint:42` — planning doc for
  gated kinds, decision-log line for ceremony-free ones, `non-boundary: <why>` exemption);
  the decision-log entry schema is single-homed at `conventions/decision-log.md:33-47`
  (`kind: mint`, `ref:`); **nothing counts the verdicts** — HOLDS.
- A5-18: Step-5 report block single-homed at `skills/vlt-lint/references/report.md:9-45+`
  (strict-YAML whole fence, B5-3); **no write destination anywhere**; Step 6 writes only
  the `{log}` line and is **forbidden session notes** (`vlt-lint/SKILL.md:70`); contract
  `:57` permits ad-hoc `_agent/` artifacts; the derive-first boundary clause is at
  contract `:262` — HOLDS.
- Dependencies live, as captured: `review_after:` shipped (`frontmatter.md:117`,
  `checks.md:17` `review_due`) so `expired_pages` is derivable; `spec.md` shipped at v2.

**Grounding additions (in scope beyond the filings' letter, each inside a ruling):**

1. **The substrate is already laid and marked for this build** —
   `tools/cost-manifest.py:36-49`: "B5-9's enforcement-kit vitals EXTEND these functions;
   they never lay a second substrate. Homed in `tools/` for now — the
   module-owned-code-home question (A5-19 Q1) re-opens at B5-9's brief." The tolerant
   `{log}` parser is `:51-88`; the derive-only `{log}` derivations block is `:472-503`
   (ingest count already printed "even at zero"). F1 owns the re-home.
2. **B5-7's two named deferrals land here** (roadmap B5-7 BUILT record + its brief's
   out-of-scope §): `{log}` rollover/size-bell growth machinery, and the
   identity/capabilities pruning-vitals question — both are **size vitals**, display-only
   (disposition 8).
3. **`package-lint.py` precedent**: C6 (B5-7, derived-artifact freshness) and C7 (B5-8,
   router integrity) establish the deterministic-check-rides-the-build pattern
   (`tools/package-lint.py:226-315`); F10 adds C8 in the same Group-C home.
4. **`frontmatter.md` is at `version: 4`, consumers `[vlt-ingest, vlt-extract,
   vlt-research, vlt-lint, vlt-mint]`** (`frontmatter.md:11-12`); the `blocked_on` facet is
   a schema rule change, so this build runs the 4→5 walk — and `vlt-dispatch` joins the
   consumer list (it will *group by* the facet, encoding its vocabulary — the Arc-3
   pointer-vs-ack precedent makes it a consumer, not a pointer).
5. **`vlt-upgrade` needs no edit**: Step 6 (`vlt-upgrade/SKILL.md:83`) already hands
   provisioning to `vlt-setup` (reconfigure), which is where the hooks force-reinstall,
   the seed's skip-if-present/merge-by-id, and the idempotent `settings.json` merge live
   (F4) — verify-not-edit, the B5-7/B5-8 pattern.

## Brief-time dispositions

1. **A5-18's persistence home — RULED: a dated artifact under the agent zone, at a new
   structure-map path `lint_reports: _agent/lint-reports/`.** (The roadmap designates this
   question to this brief; A4-23's grounding framed the choice.) Every lint run — scoped
   and full — writes its Step-5 report block **verbatim** to
   `{lint_reports}/YYYY-MM-DD-HHMM-lint.md` (the block already carries `mode:` and the
   denominators, so a series is self-describing). Append-only: lint never prunes, edits,
   or re-reads-to-rewrite past reports; retention is the human's. The session-note-trailer
   option is **rejected**: `vlt-lint` is forbidden session notes (`vlt-lint/SKILL.md:70`),
   so that home would create a cross-surface obligation on the summoning partner — a rule
   with no owner at the moment it matters. Derive-first is satisfied, not strained:
   persisting a report is **recording an observation**, not storing derivable state
   (consistent with the contract's `:262` boundary clause); the vitals reader derives
   nothing *from* these reports in this build — they widen what a future dashboard can
   read, exactly as A5-19's capture noted ("non-blocking either way").
2. **A5-19 parked Q3, `days_since_lint` — RULED: display-only.** The filing's own
   recommendation, kept: two seed wires only (alert-fatigue budget, one strip line);
   `days_since_lint` renders in the ledger's vitals block and never trips. It promotes to
   a wire only after a time-based lint failure is actually observed — a vault-local
   registry edit needing no module change (wires are vault-grown state).
3. **A5-19 parked Q4, `blocked_on` shape — RULED: inline greppable facet, and
   `external-event` requires a companion date.** The facet rides the entry tag tuple —
   `(kind, by: <who>, blocked: user-decision | partner-bandwidth | external-event
   YYYY-MM-DD)` — on `{backlog}` items and (optionally) dispatch pointer lines; `ledger`
   groups by it, untagged rows rendering as their own bucket. Frontmatter over inline is
   rejected: backlog items and pointer lines have no frontmatter — they are checklist
   lines, and the facet must live where the item lives. The companion date dovetails with
   `review_after:` as the filing anticipated: an `external-event` block with no date is
   invalid (nothing could ever age it). Optional throughout; absence = untagged; zero
   backfill.
4. **A5-19 Q1 (module-owned code home) — SETTLED by the Arc-3 decide-once ruling, cited:
   `{root}/.claude/hooks/`,** beside the `.claude/workflows/` force-reinstall precedent —
   module owns it, overwrites on every install/update, vault never edits it. What this
   brief adds is the factory-side consequence under pre-ideation ruling 1: the substrate
   must be reachable by *both* consumers (the factory instrument and the installed vault),
   so it **re-homes as a shipped asset** (F1) and `cost-manifest.py` imports it — one
   parser, two callers, zero second substrates. This resolves the `cost-manifest.py:40`
   deliberately-open note.
5. **A5-19 Q2 (one metric vocabulary or two) — SETTLED, inherited:** shipped source
   pre-answered it in the filing's proposed direction (`frontmatter.md:231` — tripwire
   metric ids are "the only legal values" for `enforcement_counter:` once the kit lands;
   the capture rules a brief inherits that unless ideation overturns it — it didn't). The
   vitals reader's declared metric ids are the one canonical vocabulary; registry wires
   and `enforcement_counter:` values must name them. The lint-side net is
   `counter_unknown_metric` (F6) — a find, not a nag, per Arc-3 ruling 2.
6. **A5-7 shape 3 (report the never-rung streak) — RULED: a derived, denominated,
   display-only line.** `classifier_streak` derives from `_agent/mint/decision-log.md`:
   the count of consecutive most-recent classifier-bearing mint entries whose recorded
   answer is `non-boundary:`, rendered in the ledger vitals block as
   `classifier streak: N consecutive non-boundary verdicts (of M classifier records; K
   entries carry no readable verdict)` — count, denominator, and blind spot in the same
   breath, per the contract's *Honest reporting* rule (**cited, never re-worded** — the
   B5-3 paragraph at contract `:254-262` is the single home). Pre-`ref:`/pre-schema
   entries and gated mints whose verdict lives only in a planning doc are the K bucket —
   surfaced, never swept (the decision-log convention's two-tier tail, applied). Not a
   wire (seed budget), not a contract edit (the line *complies with* the rule; extending
   `:256` from count-surfaces to event-gates as rule text stays future-filing territory —
   A4-12's grounding called that a design ruling this build doesn't need). **Shape 2 (the
   discriminating probe) is RULED NOT-BLOCKING** for this build (roadmap evidence-debt
   disposition) — it remains a field/owner action; the streak line ships without it.
7. **Reconciling the two wire forms (the capture's explicit demand) — RULED: frontmatter
   deferrals are the per-convention wires; the registry holds vault-level wires; one
   finder per fact.** Build-16 already shipped change 7's rule for the convention case
   (`vlt-mint:42`/`:138` — a boundary mint declares its bell or a complete tripwired
   deferral in *frontmatter*), and `vlt-lint` already finds `deferral_invalid` /
   `deferral_expired` / `declared_untripwired` (`checks.md:37`). The registry serves
   metrics **belonging to no single convention** (lint debt, pointer age) — it never
   duplicates a frontmatter deferral, and the vitals reader never re-finds what lint
   finds (Arc-3 ruling 2: lint/dispatch find, **tripwires nag**). Change 7's residual is
   the **non-convention deferral**: a mint or council verdict that defers an enforcement
   leg *outside* any convention's frontmatter (the dispatch-failure-modes "until it
   bites" shape) MUST register a registry wire (F9). The registry is written only at
   these rare, human-gated moments; **no op ever writes counters.**
8. **B5-7's deferrals land as display-only size vitals.** `{log}` / `thread.md` /
   `{backlog}` / `{index}` / per-partner `identity.md`+capabilities byte sizes render in
   the ledger vitals block (they are already substrate derivations — B5-7's own
   disposition said "log/thread sizes are already cost-manifest derivations the
   enforcement kit can watch"). **No rollover, archival, or pruning machinery ships** —
   bounded reads (B5-7) made growth boot-harmless; a size that alarms someone becomes a
   vault-local wire, not module machinery.
9. **The vitals reader is Python (stdlib-only), one script, two modes.** The filing's
   grep/awk-shell preference loses to pre-ideation ruling 1: a shell reimplementation of
   the `{log}` parser would be the second substrate the ruling forbids (and the
   two-definitions bug class A5-19's latent bug 1 documents). One file,
   `vlt-vitals.py`: default mode prints the vitals report (all metrics + tripped-wire
   evaluation); `--strip` prints the ≤1-line session strip. Non-zero exit on any failure;
   the strip renders `vitals unavailable` on reader failure — **never an empty
   healthy-looking line** (a false-healthy strip is the failure shape the whole filing
   exists to kill). Python3-absent degrades to the hook printing nothing beyond its own
   error line — fails loud, not silent-green.
10. **The registry's spec-format sequencing note is satisfied as schema-in-header, not as
    a `{specs}` doc.** The filing's note ("the tripwires registry should adopt the spec
    convention's format once 091001 lands") predates `spec.md`'s shipped meaning: a spec
    is a prose cross-partner contract, and the registry is machine-read YAML — forcing it
    into `{specs}` would fork the registry from its readers. The seed carries its full
    schema + owner + derive-first rationale in its header comment (the machine-read
    grammar declared where the file lives), which is the note's intent.
11. **The strip's `settings.json` registration merges idempotently by command path and
    never clobbers vault-local hooks.** vlt-core's hand-wired dirty-tree SessionStart
    hook is the live case the merge must not destroy (filing latent bug 3's flag). F4
    specs the merge; acceptance check 1 exercises it against the real vault.

## F1 — the vitals reader: substrate re-home + extension (NEW `skills/vlt-setup/assets/hooks/vlt-vitals.py`; `tools/cost-manifest.py` follows)

**Current state:** the shared measurement substrate lives factory-side only — the marked
block at `tools/cost-manifest.py:36-49` (banner), the tolerant `{log}` parser
`:51-88` (`LOG_HEADER_RE` / `LOG_HEADER_FALLBACK_RE` / `parse_log_entries`), structure-map
resolution `:131-167`, and the derive-only `{log}` derivations `:472-503`. `tools/` is not
part of the own-the-apply copy surface, so no installed vault can run any of it.

**Change:** create `skills/vlt-setup/assets/hooks/vlt-vitals.py` — stdlib-only Python, the
**single home** of the substrate + the kit's vitals:

- **Move in** (from `cost-manifest.py`, verbatim in behavior): the tolerant `{log}` header
  parser with its documented tolerances (case-insensitive type, optional paren, required
  trailing `|`), and a minimal structure-map resolver (config-override wins, else the
  shipped defaults — `log`, `backlog`, plus the new `tripwires`/`lint_reports` keys; the
  hardcoded `_agent/dispatch.md` read stays hardcoded with a comment citing the Arc-3
  ruling-4 precedent).
- **Declare the canonical metric vocabulary** as a module-level table (id → derivation +
  one-line definition) — the ids `enforcement_counter:` and registry wires must use
  (disposition 5). Metrics: `ingests_since_lint` (count of `ingest` headers after the last
  `lint` header — **op-debt**, per the pinned definition; latent bug 1),
  `days_since_lint` (display-only), `open_pointers` and `oldest_open_pointer_days` (from
  `_agent/dispatch.md` unchecked `- [ ]` rows and the run header above each),
  `expired_pages` (frontmatter `review_after:` in the past, scanned over `{wiki}` +
  `{research}`), `classifier_streak` + its denominator/unreadable counts (disposition 6,
  derived from `_agent/mint/decision-log.md`), and the size vitals (disposition 8:
  `{log}`, `{backlog}`, `{index}`, `thread.md`, per-partner `identity.md` + capabilities
  dirs — bytes).
- **Registry evaluation:** read `{tripwires}` (absent registry = zero wires, said
  plainly, not an error — a fresh vault before seeding); validate each wire's required
  fields; evaluate each against its metric; unknown metric id in a wire = a loud per-wire
  error line, never a silent skip.
- **Two modes:** default prints the full vitals report (every metric with its value, the
  derive-only banner, each wire's state); `--strip` prints **at most one line** — tripped
  wires only (`⚠ lint-debt: 12 ingests since last lint (wire ≥ 10) · relay-overdue: …`),
  **nothing at all when green**, and `vitals unavailable (<reason>)` on any read/parse
  failure. Read-only throughout; non-zero exit on failure.

**`tools/cost-manifest.py` follows the re-home:** import the substrate from the asset
(path-relative import from the repo layout — the factory always has `skills/`), delete the
now-duplicated parser block, update the `:36-49` banner (the Q1 note resolves: "re-homed
to the shipped asset by B5-9; this tool is a consumer"), keep every mode's output shape so
`tools/test-cost-manifest.py` stays **7/7 green** (assertion text may follow renames, the
truth table may not shrink). The `{log}` derivations section may now also call the metric
table — same figures, one derivation.

**Why:** pre-ideation ruling 1 (one substrate, B5-9 extends), 091003 changes 1–2's vitals
half, dispositions 4–6, 8–9.

## F2 — the registry seed (NEW `skills/vlt-setup/assets/tripwires.yaml`)

**Current state:** does not exist; `skills/vlt-setup/assets/` holds `governance/`,
`workflows/`, `module-help.csv`, `module.yaml`.

**Change:** create the seed beside `module-help.csv` — deliberately **not** under
`assets/governance/` (the Governance-SSoT rule keeps that bundle to `_meta/` only, and
§2's copy step would never install a sibling; F4's provisioning step installs this seed —
the filing's own homing note, kept). Contents: a header comment carrying the schema
(`id, metric, threshold, owner, moment, surface_text, review_after` — all required), the
derive-first rationale (wires reference derived metrics; **no op ever writes counters**),
the canonical-vocabulary pointer at `vlt-vitals.py`'s metric table, and the write-moments
rule (mint/council deferral moments + deliberate human edits only). Two stock wires,
exactly the filing's: **`lint-debt`** (`ingests_since_lint ≥ 10`) and **`relay-overdue`**
(`oldest_open_pointer_days > 21`). No third wire (disposition 2).

**Why:** 091003 change 2; the alert-fatigue budget is a recorded constraint.

## F3 — the structure map (`skills/vlt-setup/assets/module.yaml:39-59`)

**Current state:** the canonical `vault_structure.default` map (`:44-59`) has no
`tripwires:` or lint-report entry.

**Change:** add two rows to the default map: `tripwires: _agent/tripwires.yaml` and
`lint_reports: _agent/lint-reports/`. This is the declared single source of truth —
`vlt-setup` materializes it into config; `package-lint` E2 keys off it (its agreement
check must pass with the new rows).

**Why:** 091003 change 1; disposition 1's home needs a resolvable logical path.

## F4 — provisioning: hooks, seed, settings (`skills/vlt-setup/SKILL.md`)

**Current state:** §2a (`:152-164`) installs the workflows with the force-reinstall
posture ("module-owned, not user-authored … overwrite them on every install/update",
`:163`); no hook-install or `settings.json` capability exists anywhere in the file; §4's
agent-zone seeding precedent (mint zone, seed-only-when-absent) is at `:239`; the final
report enumerates provisioned surfaces at `:280`.

**Change:** add **§2b — Install the enforcement kit** directly after §2a:

- Copy `./assets/hooks/vlt-vitals.py` → `{root}/.claude/hooks/` (create the dir if
  absent). **Force-reinstall**, mirroring §2a's wording — module-owned code, refreshed
  every setup/upgrade (the Arc-3 code-home ruling, cited in the step).
- Seed `{tripwires}` from `./assets/tripwires.yaml` — **skip-if-present with merge-by-id**:
  absent → copy whole; present → add only ship-seeded wires whose `id` is absent; **local
  thresholds win; local wires are never dropped or rewritten** (vault-grown state, the
  mint-zone never-clobber posture at `:239` applied). Note the merge result for the report.
- Register the SessionStart hook in `{root}/.claude/settings.json` by **idempotent JSON
  merge keyed on the command path** (the `vlt-vitals.py --strip` invocation): create the
  file/keys if absent, append the hook entry only if no existing entry carries that
  command, and **never touch unrelated hooks** — a vault-local SessionStart hook (vlt-core's
  dirty-tree hook is the live case) must survive byte-identical. Re-running is a no-op.
- Also create `{lint_reports}` (empty dir) if absent — same never-clobber line.
- Extend the `:280` report bullet: hooks installed/refreshed, registry seeded/merged/kept,
  hook registration added/already-present.

**Why:** 091003 change 3 + latent bug 3; disposition 11. `vlt-upgrade` **verified, not
edited** — its Step 6 (`vlt-upgrade/SKILL.md:83`) reconfigure hand-off runs this same
step, so hooks refresh and the seed-merge ride every upgrade (grounding addition 5); the
builder confirms this in Verification rather than editing `vlt-upgrade`.

## F5 — the `{log}` grammar tighten (`vault-operating-contract.md:114-137`)

**Current state:** the canonical one-line format is already declared verbatim
(`:118-122`); `:116` says "`vlt-lint` scopes off it; a future dashboard parses it. Keep it
parseable"; the paren is omittable only for partner-less generic operations (`:124`); new
types keep the shape (`:123`).

**Change (tighten-and-relabel, per the capture — NOT a new section):** (a) name the
section a **declared machine-read grammar** — mechanisms parse it (`vlt-lint` Step 0, the
vitals reader); (b) the partner paren is **mandatory for partner-run operations going
forward** (`:124` gains the forward rule; history is grandfathered); (c) **parsers must be
case-insensitive and paren-tolerant of history** (the filing's probe: strict parsing
silently drops ~5% of real headers — the tolerant-parser mandate the substrate already
implements). The operating contract is deliberately **not handshaked** — prose edit, no
version machinery. The B5-7 rule-card derives from the contract, so **C6 requires the
rule-card's `derived_from:` SHA to be re-stamped in the same build** (regenerate the hash
after the edit; the card's six rule rows don't change — this section is not one of them).

**Why:** 091003 change 4 residual + latent bug 2.

## F6 — lint: pins, live pointers, persistence, counter net (`skills/vlt-lint/SKILL.md` + `references/`)

**Current state:** description `:3` "proactively after several ingestions" (nothing
counts); Step 0 `:23-32` (last-lint grep + mtime `find`); Standing rules `:54-60`
(single-writer-in-the-SKILL among them); Step 6 `:62-70` (log entry; no session note).
References: `checks.md:17` and `:64` promise the tripwire concern; `checks.md:37` is the
enforcement doctrine meta-check; `report.md:9-45+` is the Step-5 fence (strict-YAML whole,
B5-3 — do not regress).

**Change:**

- **`:3` description:** append "…after several ingestions (the `lint-debt` tripwire —
  `{tripwires}` — is the counter behind this phrase)". The aspiration becomes enforced.
- **Step 0, one pinning line** (latent bug 1): "Two 'since last lint' definitions exist by
  design: this step scopes by **file mtime** (which files to read); the `lint-debt` wire
  counts **ingest ops** from `{log}` headers (how much work has piled up). They can
  legitimately disagree; neither redefines the other." The vitals reader carries the dual
  pin (F1's metric definition).
- **Step 6:** one line — "this entry is, by derivation, the `lint-debt` counter reset; no
  bookkeeping step exists anywhere" — plus the **persist beat** (disposition 1; the write
  lands here because **single-writer-in-the-SKILL** is a standing rule): "Write the Step-5
  report block **verbatim** to `{lint_reports}/YYYY-MM-DD-HHMM-lint.md` (both modes;
  append-only — never edit or prune past reports)." The log-entry shape at `:66-68` is
  unchanged.
- **`checks.md:17` and `:64`:** the two promises become live pointers — "a tripwire
  concern (**the enforcement kit — `{tripwires}` + the `ledger` Tripped-wires surface**),
  not lint's". No behavior change; the dangling referent resolves.
- **`checks.md:37` meta-check gains one flag:** `counter_unknown_metric` — an
  `enforcement_counter:` present but naming no id in the vitals reader's canonical metric
  table (disposition 5). Find, never nag; never-auto-fix untouched.
- **`report.md` fence gains `counter_unknown_metric: [...]`** beside the other enforcement
  keys (`:24-28`) — the fence must still parse whole as strict YAML.

**Why:** 091003 change 6; A5-18 (disposition 1); disposition 5; the dangling-referent
repair is the build's honesty core.

## F7 — the surface: Tripped wires in `ledger` (`skills/vlt-dispatch/references/ledger.md` + router)

**Current state:** `ledger.md` (whole file) is the read-only open board — grep, group,
present, Verify (`:21-27`); writes no `{log}` entry (`:3`, router `SKILL.md:82`).

**Change:** after the open-board presentation, add **"Tripped wires & vitals"**:

- Run the vitals reader (`{root}/.claude/hooks/vlt-vitals.py`); render each **tripped**
  wire as a row (wire id, current value vs threshold, owner slug, `surface_text`). A
  reader failure renders as a **warning row** (`⚠ vitals unavailable: <reason>`) — never
  omitted, never faked green. No tripped wires → one line saying so **with the wire count
  checked** ("0 of 2 wires tripped" — a denominated zero, per *Honest reporting*, cited).
- Below it, the **display-only vitals block** (pull, not push — this is the "everything
  else is pull" budget line): `days_since_lint`, the `classifier_streak` line with its
  denominator and unreadable-count (disposition 6's exact shape), `expired_pages`, and
  the size vitals (disposition 8).
- **Group open items by `blocked:` facet** where tagged (disposition 3): `user-decision`
  renders first as the owner's question list; untagged rows are their own bucket.
- **Verify** gains: still read-only; the rendered wires match a fresh vitals run.

The router (`skills/vlt-dispatch/SKILL.md:61`) ledger blurb gains three words ("…still
open, plus tripped wires"); `ledger` continues to write no `{log}` entry.

**Why:** 091003 change 5 + the rider's triage view; A5-7 shape 3's surface.

## F8 — the `blocked_on` rider: `frontmatter` 4→5 (`conventions/frontmatter.md` + carriers)

**Current state:** the backlog schema (single home, `frontmatter.md:200-221`) tuple is
`(kind, by: <partner|user>)` — no blocked facet; `version: 4`, `consumers: [vlt-ingest,
vlt-extract, vlt-research, vlt-lint, vlt-mint]` (`:11-12`); `enforcement_counter:` at
`:231` still says "optional until the enforcement kit lands". Dispatch pointer-line
shapes: `references/daily.md:40` / `relay.md:44-45`.

**Change:**

- **Backlog schema:** the tuple gains the optional facet —
  `(kind, by: <who>, blocked: user-decision | partner-bandwidth | external-event
  YYYY-MM-DD)` — with three lines of semantics: optional, absence = untagged (zero
  backfill); `external-event` **requires** its companion date (disposition 3); the facet
  is triage metadata, never a status (an item can be open and unblocked).
- **`:231`:** re-word to the landed form — "`enforcement_counter: <optional; when
  present, must name a metric id from the vitals reader's canonical table
  (`.claude/hooks/vlt-vitals.py`) — the enforcement kit's one vocabulary>`".
- **`version: 4` → `5`; `consumers:` gains `vlt-dispatch`.** The full walk (Registration
  below): all five existing consumers re-ack `frontmatter@5` (most as verified-no-edit);
  `vlt-lint` takes F6's `counter_unknown_metric` edits in the same walk; **`vlt-dispatch`
  acks `frontmatter@5` for the first time** and its `daily.md:40`/`relay.md:45` pointer
  line shapes note the optional facet may ride the paren.

**Why:** 091003 change 8 (the rider, whole); disposition 3; grounding addition 4.

## F9 — the wire rule at mint/council moments (`vlt-mint/SKILL.md` + `vlt-review-council/SKILL.md`)

**Current state:** the convention case already shipped as build-16's frontmatter deferral
(`vlt-mint:42`, `:138`); no rule covers a **non-convention** deferral; council verdict
return is `vlt-review-council/SKILL.md:43-46`.

**Change (disposition 7's residual, two sentences per site):** at `vlt-mint` Step 2a's
capture (`:93-102`) and at the council's Step 3 return (`:43-46`): a verdict that
**defers an enforcement leg with no convention frontmatter to carry the deferral**
(a "until it bites" deferral) MUST register a wire in `{tripwires}` — `id, metric,
threshold, review_after` required, metric from the canonical table — recorded in the same
human-gated moment as the verdict itself. The registry is written **only** at these
moments and by deliberate human edit; no op ever writes counters (the invariant, cited).

**Why:** 091003 change 7, reconciled per the capture's demand — no parallel vocabulary.

## F10 — package-lint C8: enforcement-kit packaging (`tools/package-lint.py`)

**Current state:** Group C carries C5 (`:211`), C6 rule-card freshness (`:280-315`,
`RULE_CARD_BUDGET :226`), C7 router integrity (`:234-278`, `ROUTER_BUDGETS :227`).

**Change:** add **C8 — enforcement-kit agreement**, homed in Group C (the summary-line
format holds): (a) `assets/tripwires.yaml` parses as YAML and every wire carries all
required fields; (b) every wire's `metric` id exists in `assets/hooks/vlt-vitals.py`'s
canonical metric table (parse the table, don't re-declare it); (c) `vlt-vitals.py`
compiles (`py_compile`); (d) `module.yaml`'s default map carries `tripwires` and
`lint_reports` rows. Each failure is a named FAIL; a temp-copy perturbation (e.g. a seed
wire naming a bogus metric) must FAIL in Verification — the C6/C7 the-check-can-fail
precedent.

**Why:** grounding addition 3; the kit's own promises get a deterministic factory net.

## Registration

**No new skill, no `module-help.csv` row** (the vitals reader is a hook asset, not a
skill; `ledger` is already registered). **One convention rule change:**
`frontmatter.md` **4→5** — the consumer walk in the same build (Group E is the check of
record): `vlt-ingest`, `vlt-extract`, `vlt-research`, `vlt-mint` re-ack `frontmatter@5`
(expected verified-no-edit; the reconciliation is still recorded by the ack);
`vlt-lint` re-acks `@5` carrying F6's `counter_unknown_metric`; **`vlt-dispatch` joins
`consumers:` and acks `frontmatter@5`** (first ack — its `depends_on` currently reads
`["consult@1", "spec@2"]`). No other convention bumps: the contract edit (F5) is
deliberately unhandshaked; `decision-log.md` is read by the streak derivation but its
rules don't change (the reader consumes the existing schema — pointer, not ack, per the
Arc-3 precedent).

## Out of scope (dispositioned)

- **A5-7 shape 2 (discriminating probe)** — ruled NOT-BLOCKING (roadmap evidence-debt
  disposition); remains a field/owner action; the streak ships without it.
- **Stored counters, in any form** — rejected design invariant (091003); do not
  re-litigate. Plan B for a genuinely underivable counter (append-only events file) is
  not needed by any metric in this build.
- **Stored auto-created ledger rows / scheduled headless runs / no-go gate / debt-aware
  ingest** — deferred behind the filing's own explicit triggers (two consecutive
  unactioned trips; a tripped wire >7 days old at first render; escalation tiers);
  none has fired.
- **`vlt-ingest`** — deliberately untouched (091003 change 9: no write op is modified).
- **`{log}` rollover/archival machinery and identity/capabilities pruning** — the B5-7
  deferrals land as **size vitals only** (disposition 8); acting on a size is vault-local.
- **Extending contract `:256` rule text to event-gates** — not needed for the streak line
  (disposition 6); future-filing territory.
- **`days_since_lint` as a seed wire** — ruled display-only (disposition 2).
- **`enforcement_counter:` backfill onto existing conventions** — the key stays optional;
  stamping counters onto the five stock conventions is a mint-ceremony act, not this
  build's (stage promotions go through mint, never lint or a build).
- **A5-18 trend/series semantics (comparing run N to N−1)** — persistence lands the
  series; consuming it is the future dashboard's, exactly as `contract:116` frames it.
- **`vlt-upgrade` edits** — verified-not-edited (grounding addition 5); the wholesale
  `_agent/`-never-touched posture already protects a vault's registry and lint-reports.

## Verification (unit, at rest)

1. **`package-lint.py` A/B/C/E PASS** on the tree — C8 live — **and** three temp-copy
   negatives each FAIL correctly: a seed wire naming a bogus metric id (C8b); a
   syntax-broken `vlt-vitals.py` (C8c); a deleted `tripwires` row in `module.yaml` (C8d).
2. **Group E bipartite** — `frontmatter@5` ↔ all six consumers' acks (including
   `vlt-dispatch`'s first). Group E is the check of record; a hand-written
   `grep "frontmatter@"` is not a substitute.
3. **C6 still PASSES after F5** — the rule-card `derived_from:` SHA re-stamped against
   the edited contract; a stale SHA must FAIL first (run before/after to see both).
4. **`test-cost-manifest.py` 7/7 green** after the substrate re-home; `cost-manifest.py`
   both modes run against the repo + a temp vault fixture with output figures unchanged
   for unchanged inputs.
5. **Vitals fixture run** — a temp vault with a seeded `{log}` (mixed-case types,
   paren-less headers, an old `lint` header + N later `ingest` headers), a dispatch file
   with open/closed rows, a decision log with `non-boundary:` runs, pre-schema entries,
   and a `review_after:`-expired page: every metric hand-verified; `--strip` renders the
   tripped `lint-debt` line; green fixture renders nothing; a mangled `{log}` renders
   `vitals unavailable`; exit codes checked. Idempotent seed-merge demo: run the F4 merge
   twice against a fixture `settings.json` carrying a fake vault-local hook — the local
   hook survives byte-identical, the strip hook appears exactly once.
6. **Strict-YAML fence** — `report.md`'s Step-5 fence parses whole via `yaml.safe_load`
   with `counter_unknown_metric` present (B5-3 not regressed).
7. **Single-home greps** — the metric table lives only in `vlt-vitals.py` (cost-manifest
   imports, never re-declares); the wire schema lives only in the seed header (mint/
   council/setup sites point); the tolerant parser exists in exactly one file; the
   `{lint_reports}` write instruction appears only in the lint router (single-writer).
8. **Dry-walks** — a `ledger` glance reads router + `ledger.md` + runs the reader,
   writes nothing; a scoped lint ends by persisting one dated report + one log line;
   the two `checks.md` pointers resolve to real surfaces.
9. **Scrub** — no personal/vault-local content in any changed shipped file; worked
   examples use placeholder paths.
10. **No `.decision-log.md`** in the working tree; **no commit** — release choreography
    rides the arc level (`vlt-release`); this is the arc's last planned build, so the
    release (both version strings + `--expect-version` gate) follows it as its own
    gated sequence, not inside this build.

## Acceptance (live — the same checks appended to the roadmap ledger)

**(1) [ship-verifiable] the kit reaches the field and self-exercises** — on the next
ordinary vlt-core upgrade (its reconfigure hand-off runs F4): (a) the installed vault
carries `.claude/hooks/vlt-vitals.py`, a seeded `_agent/tripwires.yaml` with the two
stock wires (vlt-core has no registry today, so the seed path is forced and can fail),
and an `_agent/lint-reports/` dir; (b) `{root}/.claude/settings.json` carries the strip
hook exactly once **and the pre-existing vault-local dirty-tree SessionStart hook
byte-identical** — the never-clobber merge's first live exercise; (c) the installed
`frontmatter.md` is `version: 5` with all six installed consumers acking `@5`
(`vlt-dispatch` included), the installed lint router carries the persist beat + the
Step-0 pin, `checks.md`'s two tripwire pointers resolve, and `ledger.md` carries the
Tripped-wires section; (d) run on vlt-core, `vlt-vitals.py` derives its figures with ≥3
hand-verified against independent `grep -c`/`wc -c`, and `--strip` output matches the
registry state. Grep/run-checkable; bounded — the upgrade happens anyway.

**(2) [field-contingent] the wires live and the M0 debt discharges** — producing vault:
**vlt-core** (factory-readable; the owner runs sessions and lints on ordinary cadence).
(a) The first interactive session after the upgrade renders the strip correctly for the
vault's true state (a tripped line matching a hand-run of the reader, or silence when
green — owner spot-check); (b) the first lint after the upgrade **persists its report
block** to `_agent/lint-reports/` (the first persisted lint report in the vault's
history — A5-18's payoff) and its Step-6 log entry resets `ingests_since_lint` by
derivation on the next vitals run; (c) **the 091003 M0 counter-accuracy audit** — the
owner hand-counts ingests-since-last-lint and open dispatch pointers once and compares
against the vitals output; agreement discharges the debt, a discrepancy files back as a
defect (either outcome closes the audit — it could fail); (d) the first `ledger` glance
shows the denominated classifier-streak line and the blocked-facet grouping renders
(untagged bucket at minimum). Non-gating at closeout; tripwire-*hit* data (a wire
tripping on real debt) is noted when it occurs but is not required — a healthy vault
never tripping is a pass, not a vacuous one, because clause (d)'s denominated zero and
clause (a)'s hand-check prove the machinery can see.
