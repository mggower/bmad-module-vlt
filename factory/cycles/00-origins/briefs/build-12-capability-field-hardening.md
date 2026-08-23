---
title: 'Build #12 — Capability field-hardening (shared-lane definition, source-type front-end, prep/interpret split)'
status: 'BUILT 2026-07-03 — unit-verified at rest; live acceptance rides the next vlt-core upgrade'
module_code: 'vlt'
created: '2026-07-03'
derives_from:
  - 'inbox/2026-06-27-160109-light-capability-source-type-frontend.md (A2-1)'
  - 'inbox/2026-06-27-162915-heavy-source-prep-interpret-split.md (A2-2)'
roadmap: 'skills/reports/inbox-evolution-arc2-roadmap.md'
risk: 'low — doc/guidance-only, zero migration, no version-handshake'
---

# Build #12 — Capability field-hardening

Both filings come from one event: the vault's first light capability (Librarian's
`ingest-youtube`) minted and then run in production. The build-7 model held; this build
ships the boundary definitions and the one orchestration pattern that field use surfaced.
All edits are prose/guidance. **No version-handshake anywhere in this build:** the operating
contract is not handshaked (held out in build-4), `capability-template.md` is a template not
a convention, and vlt-lint's change is check-wording, not a `depends_on` change.

## Part 1 — Define "shared lane"; rule the `sources/` deposit lane-safe (A2-1b)

**Single home = the contract's *Capabilities* section** (`vault-operating-contract.md:195`
area). Add the definition + ruling:

> A **shared lane** is a *synthesized, single-writer* lane — the wiki above all. `sources/`
> is not one: it is the immutable raw-input tray the user already writes freely, with no
> single-writer owner to contend with. **Depositing a *new* raw-input file into `sources/`
> is lane-safe and own-zone-compatible** — it does not promote a light capability to heavy.
> Modifying an existing source, or writing any synthesized lane, is out.

Mirror sites (short line + pointer, no restated mechanics — single-home discipline):
- `capability-template.md:30` and the `own-zone-only` family invariant at `:80` — append
  "(a *new-file* deposit to `sources/` is permitted — see the contract's *Capabilities*
  section for what counts as a shared lane)".
- `vlt-lint/SKILL.md:66` (lane-safety guard) — reword so the guard doesn't false-positive:
  a light-cap lane violation is a write to a **synthesized/single-writer lane or another
  partner's zone**; a **new-file deposit to `sources/`** is permitted and is **not** a
  `capability_lane_violation` or `capability_scope_mismatch`. Genuine violations (wiki
  write, existing-source modification, foreign zone) still flag.

Deferred (filing's own lean, kept): no declared `deposits:` frontmatter field at n=1 —
revisit if a second source-type front-end lands.

## Part 2 — Capability-template: the `scripts/` sibling + the "source-type front-end" name (A2-1c + A2-1a)

In `capability-template.md` (light-capability half):
1. **Tooling sibling note:** a light capability may carry a `capabilities/scripts/<tool>`
   (or `assets/`) sibling for reusable tools its profile invokes — the folder shape is
   `capabilities/<slug>.md` + `capabilities/scripts/…`. Lane rules unchanged (the tool runs
   mechanically; persistent writes stay scratch + raw-input deposit).
2. **Name the pattern** (one short named block, so it's reached-for, not re-invented):
   > **Source-type front-end (light).** To teach an existing ingest/verb a new *input
   > form*: mint a light capability owned by the verb's partner — an own-zone profile that
   > fetches + normalizes the new form into the text the verb already eats (plus a
   > `scripts/` sibling for tooling). It writes only scratch + a raw-input deposit; the
   > canonical write stays with the unchanged verb skill. Council-none, upgrade-safe, no
   > skill proliferation.

In `vlt-mint/SKILL.md` (the `add a capability` kind, `:35`/`:107` area) — the one-line
verb-not-subject reconciliation (grounding shrank A2-1a to this; the stale "registry row"
guidance is vault-local memory, not module source):
> Same verb, new **source type** → a light capability profile in the owning partner's zone
> (the *source-type front-end* pattern — see `capability-template.md`). No registry row;
> only the heavy weight registers a CSV row.

## Part 3 — vlt-ingest: the prep/interpret split for heavy sources (A2-2)

**Home decision (the build's one real design call): the pattern's mechanics live in
`vlt-ingest/SKILL.md`**, as a new "Heavy sources — the prep/interpret split" section. No
new pattern-catalog artifact: the module's precedent is that an orchestration pattern lives
in the skill that runs it (vlt-lint's fan-out lives in `vlt-lint/SKILL.md:39`), and at n=1
module-side pattern a catalog is YAGNI. The capability template points here (below).

Section content (absorb the filing's pattern + three invariants near-verbatim):
- **When:** threshold-gated, not always-on — mirror vlt-lint's "only earns its overhead at
  scale" framing. Inline up to roughly what one context can read *and still interpret
  freshly* (~15k words of normalized text / a ~1.5h transcript); above that, split.
- **Shape:** a **prep sub-agent** does the mechanical stages (fetch → normalize/clean →
  deposit the source-of-record to `sources/` → run the credential scan) and returns a
  **neutral navigational brief**: section map, locations, verbatim located quotes, flags —
  never the raw body, never an interpretation. The **invoking partner** then runs the
  unchanged ingest steps on fresh context, reading *selectively* into the deposited source
  at the brief's locations for only the passages it will canonicalize.
- **Three invariants (verbatim):** (1) **single-writer holds** — prep agents deposit and
  report; the canonical wiki write stays the verb skill's (same architecture as
  `vlt-lint-full`: read-only finders, one serial writer — say so explicitly); (2) **the
  brief is a map, not the territory** — the partner verifies each located quote against the
  deposited source before ingesting; (3) **neutral map, not a digest** — a pre-interpreted
  digest primes and quietly corrupts the fresh reading that is the split's entire point.
- **Sequencing:** the re-ingest check (cheap `{log}` grep) runs **up front**, gating the
  fetch; the credential scan runs **in the prep agent** (it needs the cleaned text).
- **Generality note:** applies to any heavy input — long transcript, long PDF, multi-page
  crawl. (Composition with a many-sources batch fan-out is real but stays unshipped: the
  batch pattern is vault-grown and n=1 — deferred, noted in the roadmap.)

**Capability-template pointer (one line, in the source-type front-end block):** a front-end
wrapping a *heavy* input should default to the prep/interpret split — see `vlt-ingest`'s
*Heavy sources* section — so the next front-end (PDF, crawl) inherits the map-not-digest
discipline.

## Out of scope
- Absorbing `batch-ingest-fanout` upstream (vault-local, single-vault evidence — deferred).
- A `deposits:` declared field (deferred, n=1).
- Promoting source-type front-end to a Model-B family (premature; would be the first real
  exercise of build-7's family machinery when a second front-end lands — noted in roadmap).

## Verification (unit, at rest)
- Grep: contract, template, and vlt-lint agree on the shared-lane definition; template and
  mint narrative both name the source-type front-end; vlt-ingest section carries all three
  invariants + threshold; no `version:`/`depends_on` touched anywhere.
- Negative check: vlt-lint guard wording still flags wiki-writes/foreign-zone/existing-source
  modification for light caps.

## Acceptance (live, next vlt-core upgrade — ledger in the Arc 2 roadmap)
- vlt-core's existing `ingest-youtube` cap (which deposits to `sources/transcripts/`) passes
  `vlt-lint` clean; a genuinely lane-violating light cap still flags.
- A heavy-source ingest (>threshold) run via the split produces a wiki entry whose quotes
  verify against the deposited source; the partner context never slurps the raw body.
