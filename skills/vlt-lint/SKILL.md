---
name: vlt-lint
description: Health-check the vault wiki and fix safe structural problems. Use when the user says 'lint the vault', 'health check the wiki', 'find orphan pages', 'check for contradictions', or 'audit the notes', and proactively after several ingestions (the `lint-debt` tripwire — `{tripwires}` — is the counter behind this phrase). Defaults to scoped mode (files changed since the last lint); 'full lint' / '--full' sweeps everything; 'full lint, re-scan <slug>' first evicts that page's cached facts so the sweep re-derives it.
depends_on: ["frontmatter@14", "wiki-index@2", "wiki-supersession@2", "extraction@9", "write-verification@5", "spec@2", "consult@1", "decision-log@4"]
---

# vlt-lint

## Overview

A wiki that grows without maintenance becomes a liability — orphan pages, stale claims superseded by newer sources, contradictions accumulating unresolved. Lint is preventive care: find problems before they compound, fix the safe structural ones, flag the rest, and file merge candidates to the backlog for `vlt-ingest` to resolve. It is the Librarian's upkeep tool — run it after every 5–10 ingestions or at the start of a research push. Its report is **structured and parseable** (so a dashboard can read it), not free prose. Reads the vault only. Runs interactively or headless.

## On Activation

Load config from `{project-root}/_bmad/config.yaml` and `{project-root}/_bmad/config.user.yaml` (root level and the `vlt` section). If the module isn't set up (no `vlt` config or `_meta` governance in this project), tell the user `vlt-setup` can configure it.

The vault is this project — resolve paths relative to `{project-root}` through the `vault_structure` map (override wins, else the shipped default). Logical names used (default, relative to the project root): `wiki` → `resources/wiki/`, `index` → `resources/wiki/index.md`, `research` → `_agent/research/`, `sessions` → `_agent/sessions/`, `log` → `_agent/log.md`, `backlog` → `_agent/backlog.md`, `conventions` → `_meta/conventions/`, `overlays` → `_agent/conventions/` (vault-local convention overlays + the stock `.baseline/`), `partners` → `_agent/partners/` (each carries a `capabilities/` folder), `capabilities` → `_agent/capabilities/` (family contracts under `families/`). Below, `{wiki}` etc. mean the resolved path. Note the **active partner** for the log tag and backlog attribution. Before applying any fix, JIT-read `{conventions}/frontmatter.md`, `{conventions}/wiki-supersession.md`, and `{conventions}/wiki-index.md` — read each together with its `{overlays}/{name}.overlay.md` if present, honoring the overlay's appended rules (the latter governs every index check and fix below) — and any **local convention** naming this skill in its `consumers:` (the operating contract, *Durability across upgrades*).

## Step 0: Determine scope

Pick one mode at the top of the run and announce it (with the scoping timestamp and file count, e.g. "Scoped lint — since 2026-04-19 15:00 — 7 wiki pages + 3 research notes").

**Scoped (default)** — only files changed since the last lint:

```bash
grep "^## \[.*\] lint" {log} | tail -1
```

Extract the `[YYYY-MM-DD HH:MM]` timestamp and **validate it parses as a real datetime.** If there's no prior `lint` entry, or the timestamp is missing/malformed, fall back to **full mode** and say so — there's no reliable incremental baseline. With a valid timestamp, build the candidate set by filesystem mtime (always including `{index}`, since index drift is cheap to check regardless):

```bash
find {wiki} {research} {sessions} {projects} {areas} {resources} -type f -name "*.md" -newermt "YYYY-MM-DD HH:MM"
```

**The one exclusion, applied at selection time:** drop the `{wiki}` subtree under `{resources}` from that result. It is the Layer-2 Librarian-only zone and its pages are the *wiki page* population, not the PARA one — removed **by name at population time, never as an exception inside a check** (the operating contract, Layer 2, is the canonical statement). What survives under `{projects}`/`{areas}`/`{resources}` is the **PARA file population** the `para_*` checks judge.

Two "since last lint" definitions exist **by design**: this step scopes by **file mtime** (which files to read); the `lint-debt` wire counts **ingest ops** from `{log}` headers (how much work has piled up). They can legitimately disagree; neither redefines the other.

**Full** — only when the user says "full lint" / "lint everything" / `--full`. `full lint, re-scan <slug>` (one or more slugs) is full mode with those pages evicted from the findings cache before the sidecar read — the mechanic is `references/full-scale.md` step 2. Read every page in `{wiki}` (and `{research}` for deeper checks), **and every file under `{projects}`/`{areas}`/`{resources}` outside the `{wiki}` subtree** — the PARA file population. At scale that PARA set is derived by the **same predicate already single-homed at `references/full-scale.md` step 1** (the `crossLayerSlugs` derivation, which globs the PARA keys with the nested `{wiki}` subtree carved out) — read it there; it is not restated here.

Below, "every wiki page" means the scoped set in scoped mode, or the whole wiki in full mode. Likewise **"every PARA file"** means the PARA members of the scoped set in scoped mode, or the whole PARA population above in full mode — this is the population every `para_*` finding judges (`references/checks.md`).

**Full mode at scale.** When full mode would cover **more than ~30 pages**, read `references/full-scale.md` — the fan-out workflow protocol. Scoped runs and small full sweeps stay inline and never open it.

## Step 1: Read the selected files

Read `{index}` first for the overview, then each selected page in full, noting topics, claims (and sources), outbound links, source count, and `last_updated`. Then read each selected **PARA file** — its frontmatter (`type:`, `author:`, `trust:`, `status:`, the attestation pair) and, at or above it, any container `charter.md` and its `writers:` — the inputs the `para_*` checks judge; the population itself is walked by `scripts/lint-para-facts.py` — run it here in both modes (`uv run --quiet "$SKILL/scripts/lint-para-facts.py" --line` with Step 6's `--dir`/`--exclude`/`--root` arguments; bare `python3` also works) and keep its `--line` output for Step 5's `para_scan:`.

## The step sequence (read each reference at the step that uses it)

- **Step 0 — scope** (above, router-only): pick scoped/full and announce it — the selection covers **both** the wiki page population and the PARA file population (`{projects}`/`{areas}`/`{resources}` outside `{wiki}`); a run with nothing in scope since the last lint ends here.
- **Step 1 — read** (above, router-only): `{index}` first, then each selected page, then each selected PARA file.
- **Step 2 — checks**: the two-tier catalog (structural, judgment/corpus, governance, research candidacy) — read `references/checks.md` (both modes).
- **Steps 3+4 — fix and file**: auto-fix safe issues, attest, file backlog items — read `references/fix-and-file.md`.
- **Step 5 — report**: the structured fence + reporting rules + Tips — read `references/report.md`.
- **Step 6 — persist, then log** (below, router-only): the persist gate over the report, then the `{log}` line.

## Standing rules (act-blocking; mechanics live in the references)

- **Never auto-fix a tier-2 or governance finding** — every one is `flag_for_human` or a backlog filing (the catalog: `references/checks.md`).
- **Never auto-apply:** page deletions (flag), contradiction resolutions (document both **with a disposition**, flag; the `adjudicable` ones are filed **or relayed, by address**, per `references/fix-and-file.md`), page merges (file to backlog), or **convention-coherence drift** (flag — a stale `depends_on` ack must be cleared by a human reconciling the consumer against the convention and then bumping the ack; lint must never bump the integer itself, or it would rubber-stamp conformance it didn't verify).
- **Single-writer safety lives here in the SKILL, never in parallel finders** — the fan-out workflow is read-only; fixes and backlog writes apply serially here (`references/full-scale.md`).
- **Lint never stamps `adoption_first_instance:`** — the stamp is the authorized ceremonies' (`vlt-mint`, Step 4).
- **Write-through records a human's ruling only** — lint never decides (`references/fix-and-file.md`).

## Step 6: Persist the report, then append to the log

**Persist first (both modes) — three moves, in order.** (1) Write the Step-5 block — fence stripped, **content-verbatim** — to a scratch path **outside the vault** (`mktemp`). (2) Run the persist gate over it:

```bash
uv run --quiet "$SKILL/scripts/lint-report-check.py" check --report <scratch> --mode <full|scoped> --dir {projects} --dir {areas} --dir {resources} --exclude {wiki} --root {project-root}
```

It parses the block back strictly, validates it against `references/report.md`'s fence (presence, type, per-file entries against its own `scripts/lint-para-facts.py` walk), prints one JSON verdict and **writes nothing**. (3) On `status: ok`, `mv` the scratch file to `{lint_reports}/YYYY-MM-DD-HHMM-lint.yaml` (plain YAML, the default) **or** `…-lint.json` (the JSON-subset rendering, `references/report.md` — **not a second authoring act**). **The validated bytes are the bytes that land** — `mv`, never a second write. With `uv` absent, render the `.json` home and run the gate under bare `python3` (the `.yaml` home needs `uv` for the script's inline `pyyaml`); the gate is never skipped. Either home is append-only — never edit, prune, or re-read-to-rewrite past reports; retention is the human's — lint reports are never wake-read (the operating contract's *Decay contracts* table). Pre-existing reports in `{lint_reports}` — either format, `.md` included — stay as they are: legal, never converted, swept or validated. Write **no** session note — the summoning partner owns the session log (operating contract § session-ownership). A full-mode sweep also rewrites the findings cache `_agent/lint-cache.json` via `scripts/lint-cache.py` (`references/full-scale.md`) — **not** a report: never under `{lint_reports}`, never wake-read; deleting it costs only a cold run.

**Then append the log line — only after `status: ok`** — a partner-tagged entry to `{log}`:

```
## [YYYY-MM-DD HH:MM] lint (<partner>) | <mode> — checked N files — orphans: X, contradictions: Y, gaps: Z, fixes: <summary>, backlog: M filed
```

`<mode>` is `scoped since <timestamp>` or `full`. This entry is, **by derivation, the `lint-debt` counter reset** — no bookkeeping step exists anywhere.

**Failed full-mode run (B10-12):** a full-mode sweep refused upstream at `references/full-scale.md` step 4 (the version-skew defence, or the pre-dispatch slot-type refusal — both predicates live there, never restated here) — it persists a `…-lint-failed.yaml` (or `…-lint-failed.json`) failed-run record and writes **no** log line here, so `lint-debt` is **not** reset. The mechanics live in `full-scale.md`; this step just does not run for a refused sweep.

**Failed persist gate (build-5):** on `status: failed` at move (2), re-render **once** from the same Step-5 facts against the check's `reason` and re-run the check — **never a re-sweep**. A second failure persists `{lint_reports}/YYYY-MM-DD-HHMM-lint-failed.yaml` (or `.json`) — the failed-run record with `reason: shape — …` and the block under `unvalidated_report: |`, itself checked (`--kind failed`) through the same ritual; field list and legal response at `references/report.md`, *Persist-gate reporting*. **No log line writes** and `lint-debt` does not reset (the B10-12 rule). Surface the `reason` and the record's path; the in-session block is the owner's copy. **Never a `-lint.yaml` that failed the gate.**
