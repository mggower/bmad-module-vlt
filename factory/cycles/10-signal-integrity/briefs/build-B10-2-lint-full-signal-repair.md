---
title: 'Build #B10-2 — the lint-full signal repair: the fan-out scanners get the rules they enforce (write-verification joins the read list with a tri-state Gap B, coexistence posture and callout form made explicit, the cross-layer set derived from the structure map, and the fan-out currency rule lands in its home)'
status: 'BUILT 2026-08-21 — all eight F-sites landed; unit-verified at rest. Verification record: (1) node --check clean; (2) handshake bipartite: package-lint Group E PASS (write-verification consumers: gained vlt-lint-full.js, ack gained write-verification@3, same build); (3) package-lint A/B/C/E PASS (D skipped, no --expect-version — release gate is B10-5); (4) tri-state coherent: sources_vs_prose_mismatch has zero occurrences, sources_vs_prose is in required + property block + prompt + the reducer filter (=== ''diverge''), report slot sources_vs_prose_mismatches unchanged and matches report.md:20/checks.md:15; (5) marker currency: every per <convention>@N marker matches disk (frontmatter@9 x2, wiki-supersession@2 x3, write-verification@3 x2); (6) single-home: predicate text only in full-scale.md, checks.md:13 carries the pointer, the supplement''s retirement clause is in the shipped text, R4-fanout full text in the ack header + one-line pointer in full-scale.md step 2; (8) fixture dry-run green: 4-page temp wiki read against the built prompts — no-prose page unambiguously no_prose_section (conformant, excluded by the reducer), mixed wikilink/bare-path sources: unambiguously never a finding (coexistence clause), bullet-form "superseded" note unambiguously still an unmarked supersession (callout-form clause, both prompts agree), [[some-handoff]] resolves via the supplement glob; step-1 derivation run by hand against a fixture config.yaml (default map + vault-grown bases:) yields exactly research, sessions, specs, partners, capabilities, bases + the supplement''s four; (9)(10)(11) n/a per brief; (12) scrub clean, no .decision-log.md; (13) parse-on-intake block byte-identical (git diff shows no hunk touching it). F8 AUDIT TABLE (re-derived against the built file — R4-fanout''s retroactive first run): pageScanPrompt (:172-175) enforces frontmatter@9 (validity, rule 4 + coexistence) + wiki-supersession@2 (stale/supersession/callout form) + write-verification@3 (Gap B tri-state), reads frontmatter + wiki-supersession + wiki-index + write-verification — GREEN after F2, wiki-index = read-without-ask, kept (disposition 5); index ask (:269-272) enforces wiki-index@2 structural-map rule, reads wiki-index — GREEN; cluster ask (:304-307) restates wiki-supersession@2 disposition vocabulary + documented-form, reads none (mechanical classification) — GREEN after F4 (markers + callout-form clause, no read — disposition 4); pair ask (:358-360) enforces none (proper-noun attribute comparison), reads none — GREEN; thin (schema desc :126) enforces none, criteria self-contained, class homed at checks.md:21 — GREEN. Deliberate deviations, numbered: (1) sources_vs_prose_detail gained a one-line description ("populated only when sources_vs_prose is diverge") — the brief said the field "stays" with no edit named; the description encodes disposition 1''s populated-only-on-diverge contract in the schema the scanner actually sees. No other deviations. Ship-verifiable acceptance checks 1-4 discharged at rest this session (check 5 field-contingent, rides the owner''s first >30-page full sweep on vlt-core after the v0.13.0 upgrade). One commit.'
module_code: 'vlt'
created: '2026-08-21'
derives_from:
  - 'inbox/2026-08-21-100500-lint-scanner-prompts-skip-rule4-coexistence-and-callout-vs-bullet.md (A10-2 — the coexistence-posture and callout-vs-bullet instructions absent from pageScanPrompt; the B5-3 seam class: model judgment where an explicit instruction should sit)'
  - 'inbox/2026-08-21-144554-lint-fan-out-gap-b-asked-unconditionally-misfires-without-write-verification.md (A10-7 — write-verification absent from convRead, the Gap B ask carries no no-prose-section carve-out, 22/25 findings false on a 56-page wiki; plus the general fan-out audit; origin mggower/bmad-module-vlt#3, captured)'
  - 'inbox/2026-08-21-101000-crosslayerslugs-omits-handoffs-bases-and-areas.md (A10-3 — the crossLayerSlugs assembly instruction''s vague parenthetical missed _agent/handoffs/, _agent/bases/, areas/; derive-from-the-map is the fix direction the capture grounded)'
roadmap: 'skills/reports/inbox-evolution-arc10-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-21): build-B10-2 grouping bullet (binds: D1, D2, R4-fanout per roundtable A7/A8); D1 (ONE combined build — A10-2 + A10-7 + A10-3; A10-1 separate, B10-3); D2 as narrowed by roundtable A7 (crossLayerSlugs derives from resolved vault_structure keys + one interim supplement line naming _agent/handoffs/ alongside the PARA layers; no vault_structure key minted this arc under the C6-b strip; retirement clause in the shipped text; qualifying-key predicate single-homed in full-scale.md); roundtable A8 (the convRead edit ships its handshake same build — write-verification consumers: gains vlt-lint-full.js, the E5-parsed ack gains write-verification@3; restated prompt instructions carry per-convention@N markers); the roundtable''s R4 declaration (the fan-out currency rule; named home = the vlt-lint-full.js ack header block + one line in full-scale.md; this build''s audit is R4''s retroactive first run, not the fix itself).'
risk: 'low-moderate — the prompts of the live lint instrument change (behavioral risk rides the cheap scan model''s reading of new instructions), a PAGE_SCAN schema field changes shape (boolean → required enum, with its one reducer consumer updated in the same file), and a convention consumers: list gains a member with its same-build ack; no convention version: moves (membership is not a rule change), no contract edit (C6 untouched), no new package-lint check (E4 untouched), no release in this build (v0.13.0 cuts after B10-5).'
---

# Build #B10-2 — the lint-full signal repair

Three of the fan-out's four false-positive classes share one root shape: *the enforcing
agent was never handed, or never had encoded, the rule it enforces.* The Gap B ask
("whether the frontmatter `sources:` and the prose Sources section diverge") is asked
unconditionally while the governing conditional — "a page with no prose section is
conformant" — lives in `write-verification.md:38`, a convention the scanner's read list
(`convRead`, `vlt-lint-full.js:161-167`) never includes: 22 of 25 findings in the class
were false on a 56-page wiki (A10-7). Rule 4's coexistence posture ("existing bare-path
entries stay legal and there is **no backfill sweep**", `frontmatter.md:36`) and the
callout-vs-bullet distinction (a callout is the Obsidian `> [!type]` blockquote form,
`wiki-supersession.md:28-34`) are nowhere in `pageScanPrompt` — whether a legal state gets
flagged rides on a cheap scan model's faithful convention read, the exact seam class B5-3
closed for slug normalization (A10-2). And `crossLayerSlugs` is assembled from a vague
parenthetical (`full-scale.md:7`: glob `{research}` "and any agent-zone note location the
wiki conventionally `[[links]]` into") that the field showed missed three layers —
`_agent/handoffs/`, `_agent/bases/`, `areas/` — so valid cross-layer links false-positive
as missing targets (A10-3).

This build lands all three as one repair (D1): `convRead` gains `write-verification` with
the same-build handshake (A8); the Gap B ask and schema go tri-state so "no prose section"
is a first-class conformant answer, never folded into a boolean; the coexistence-posture
and callout-vs-bullet instructions become explicit prompt text with inline
`per <convention>@N` source markers (A8); the cross-layer set derives from the resolved
`vault_structure` map plus one explicit interim supplement line that carries its own
retirement clause (D2/A7); and A10-7's general audit runs — every fan-out ask checked
against the convention set its scanner receives — as the retroactive first run of the
fan-out currency rule, whose named home (the ack header block + one `full-scale.md` line)
ships in this same build.

All rejected alternatives in the parent filings and the rulings are settled — do not
re-litigate. In particular: splitting this into per-filing builds (D1 ruled one combined
build), a hard enumeration of cross-layer locations (D2 ruled derive-from-the-map — the
parenthetical's vagueness and a hard list's drift are both the disease), minting a
`vault_structure` key for `_agent/handoffs/` or the PARA layers this arc (A7 ruled it
unsafe until the C6-b merge-config strip clears; B10-10 mints), and A10-1's repeat-aware
report line (different instrument — `checks.md:47`, not the fan-out; B10-3 per D1/D3).

**`binds:` roster (from the roadmap bullet, per the standing rule): D1, D2 (as narrowed by
roundtable A7), R4-fanout (the roundtable's declared rule — interim carrier ends when this
build lands) — plus roundtable A7, A8 as in-bullet annotations.** The bullet carries the
roster explicitly; nothing was reconstructed.

**Naming note (two R4s):** the roundtable's **R4** is the *fan-out currency rule* (this
build's cargo); the brief-anatomy's standing **R4** is the *enumeration-widening rule*
(§Verification). This brief writes "R4-fanout" for the former wherever confusion is
possible.

## Brief-time dispositions

**✅ OWNER-REVIEWED 2026-08-23 (first-half review): all seven dispositions CONFIRMED —
dispositions 1 and 2 live-ruled with their field costs on record.** Disposition 1 (the
required tri-state enum): CONFIRMED; its description weight caused the 3,920→4,266
schema-size regression over the 4,096 classifier ceiling (the B10-2(5) non-executability
failure), repaired by B10-12 (trim + the standing ≤3,700 budget); the tri-state itself
field-proven 2026-08-23 (the 22-of-25 false class collapsed). Disposition 2 (+3, the
qualifying-key predicate): CONFIRMED as-shipped-with-known-costs; the residual seam is
sized and captured as A10-18 (index fails two directions, `sources/` absent from the
map, the `*.md` glob) — the fix is Arc 11's, at the predicate's single home
`full-scale.md:7`, per the clerk's own named-editable-classes design. Dispositions 4–7
batch-confirmed. Review record: the arc roadmap's first-half review section.

Autonomous run 2026-08-21 — the owner is not present; each call below is **clerk-resolved
(autonomous run 2026-08-21, owner review pending)** with its reasoning, bounded to what
the rulings deliberately left to this brief. (The roadmap's "Questions deliberately left
to brief time" section lists none for B10-2; the calls below are the shape-level decisions
the rulings' letter left open.)

1. **Tri-state shape: one required enum field, `sources_vs_prose`, replacing the
   boolean.** *Clerk-resolved.* The roadmap rules "the Gap-B ask/schema goes tri-state"
   without fixing the encoding. Chosen: replace `sources_vs_prose_mismatch: boolean`
   (`vlt-lint-full.js:115`) with `sources_vs_prose: {enum: ['match', 'diverge',
   'no_prose_section']}`, **added to the schema's `required` list** (the boolean was
   optional — an omitted answer silently read as "no mismatch"; a required enum forces the
   scanner to commit to one of three states, which is the point of tri-state). The
   `sources_vs_prose_detail` string stays, populated only on `diverge`. The report slot
   name `sources_vs_prose_mismatches` (populated only from `diverge`) is **unchanged** —
   `report.md:20` and `checks.md:15` keep working with no downstream rename, and
   `checks.md:15` already states both the no-prose-conformant rule and the legal response,
   so no new finding class is created (R3 satisfied by the existing home).
2. **The qualifying-key predicate (D2/A7's single-homed rule), exact wording.**
   *Clerk-resolved.* A key **qualifies** when its resolved value names a *directory* of
   walker-visible linkable notes — operationally: every directory-valued key of the
   resolved `vault_structure` map **except** the wiki's own (`wiki` — that is the page
   set, not cross-layer), governance (`conventions`, `overlays`, `personas`), cold storage
   (`archive` — outside live-read enumerations by the Arc 8 safety model), and report dirs
   (`lint_reports` — walker-exempt by design). File-valued keys are excluded by the
   directory test itself. Against today's default map (`module.yaml:44-61`) that yields
   `research`, `sessions`, `specs`, `partners`, `capabilities` — plus, correct by
   construction, any vault-grown directory key (`bases` was A10-3's named miss).
   Over-inclusion (e.g. `partners` skill files) is deliberately accepted: `crossLayerSlugs`
   only suppresses missing-target findings on exact normalized-basename matches, so the
   masking risk is a genuine wiki gap that happens to share a basename with an agent-zone
   file — rare and bounded — while under-inclusion is precisely the filed defect. The
   exclusion classes are written as named, editable classes because B10-6 (report-dir
   exclusion for new report paths) and B10-10 (PARA-key inclusion) each edit this home
   next (A7).
3. **The interim supplement line names `projects/`, `areas/`, `resources/`, and
   `_agent/handoffs/` — not `archive/`.** *Clerk-resolved.* A7 says "the PARA layers";
   PARA's fourth layer is the archive, which already resolves via the `archive` key and is
   excluded as cold storage (disposition 2) — a wiki link into cold storage *should*
   surface, not be suppressed. `resources/` is included even though B10-11 later retires
   it: the supplement is retired by B10-10 regardless, and until the move lands,
   `resources/` legally holds linkable notes.
4. **The cluster and pair asks get markers, not convention reads.** *Clerk-resolved
   (the F8 audit's first ruling, applied in-build).* The cluster prompt
   (`vlt-lint-full.js:298-302`) classifies documented disagreements by the callout's
   *literal* recorded `**Disposition:**` line — mechanical extraction, already
   instructed "never by judging" — and the pair prompt (`:352-354`) compares two pages
   over one proper noun with no convention rule in play. Neither performs conformance
   judgment against a convention text, so R4-fanout's add-to-convRead trigger does not
   fire; but the cluster prompt *restates* wiki-supersession's disposition vocabulary and
   its documented-disagreement concept, so per A8 it gains inline `per
   wiki-supersession@2` markers and the same one-line callout-form clause as the page
   scanner (a disagreement "documented" only in bullet/heading form is not documented —
   it belongs in `cross_page_contradictions`). Adding full convention reads to ~n cluster
   agents was declined: cost with no judgment for it to inform.
5. **The page scanner's `wiki-index` read is kept.** *Clerk-resolved.* The audit's
   reverse direction — a read without an enforcing ask (the scanner extracts `category:`
   verbatim; the category↔H2 comparison is computed downstream at `:389`) — is not
   R4-fanout's target (the rule guards asks-without-reads). Removing the read is a
   behavioral/cost change out of this build's scope; the F8 audit table records it as
   "read-without-ask, kept" so the call is visible.
6. **No `version:` bump for `write-verification.md`.** *Clerk-resolved (confirming the
   standing rule's letter).* Adding `vlt-lint-full.js` to `consumers:` is membership, not
   a rule change — the precedent is exact: `frontmatter.md:12`, `wiki-index.md:12`, and
   `wiki-supersession.md:12` all gained `vlt-lint-full.js` without bumping. Version stays
   3; the ack pins `write-verification@3`. Attestation-authority non-creep is already
   handled by the convention's own text — the `verified_by` value set binds to consumers
   "**that are write ops**" and explicitly says "a skill added to `consumers:` for
   handshake reasons alone acquires no attestation authority" (`write-verification.md:44`
   region) — so no additional carve-out is written.
7. **Interim posture (R1) — substantive.** The supplement line (F5) is a rule shipped
   ahead of its mechanism (the `vault_structure` PARA/handoffs keys arrive with B10-10).
   Its interim posture lives **in the shipped text itself**: the line states what it
   supplements, why no key exists yet (C6-b), and that the build minting the keys deletes
   it in the same act — the B9-4 precedent (slip-exposed interim postures live in shipped
   text), with the fold contingency (bound inherited debt, B8-2(4) mechanism) held by the
   roadmap's A7 record, not restated in shipped text. Separately, R4-fanout itself ends
   its own interim: until this build lands the rule binds via the roundtable record (the
   declared interim carrier); this build ships the rule's named home, closing that window.

## F-sites

All sites re-grounded 2026-08-21 against the working tree at `3d25cc4` (v0.12.0 +
B10-1; B10-1 touched neither the workflow, the conventions, nor `vlt-lint`'s references —
every capture-time site HOLDS, fresh lines below). The workflow exists in exactly one
copy: `skills/vlt-setup/assets/workflows/vlt-lint-full.js` (provisioned into a vault's
`.claude/workflows/` — `full-scale.md:5`); there is no second factory copy to keep in
step.

## F1 — `vlt-lint-full.js` ack header: the `write-verification@3` pin + R4-fanout's home

**Current state:** `skills/vlt-setup/assets/workflows/vlt-lint-full.js:11-15` — the
E5-parsed ack line and its explaining comment:

```js
// depends_on: ["frontmatter@9", "wiki-supersession@2", "wiki-index@2"]
// ^ the asset ack (B7-6): this workflow's prompts instruct agents to read these
//   conventions, so it is a listed consumer in its own right — the flat pins
//   above are its handshake acks, bumped on reconciliation like a skill's
//   depends_on:. The release gate (package-lint E5) parses this line.
```

**Change:** (a) the pin list gains `"write-verification@3"` (verified current:
`write-verification.md:11` `version: 3`):

```js
// depends_on: ["frontmatter@9", "wiki-supersession@2", "wiki-index@2", "write-verification@3"]
```

(b) The comment block gains R4-fanout's rule text — this block is the rule's **named
home** (roadmap §Roundtable review, "Rule declared"); word it as the rule, not a pointer:

```js
//   R4 (the fan-out currency rule): any ask in this file that enforces a
//   convention's rule adds that convention to convRead AND to the pins above
//   in the same edit; any edit to an ask or to the read list re-runs the
//   fan-out audit (every ask checked against the convention set its scanner
//   receives); restated convention instructions in prompts carry inline
//   `per <convention>@N` source markers, which consumer walks re-derive.
```

**Why:** roundtable A8 (the handshake ships in the same build as the `convRead` edit) and
the R4-fanout declaration (home = this block + one `full-scale.md` line, F5). The
E5 machinery already parses this line shape (`tools/package-lint.py:720`
`_DEPENDS_ON_LINE_RE`) and E1 already treats `vlt-lint-full.js` as a consumer name — no
lint change needed.

## F2 — `pageScanPrompt` + `convRead`: the read list and the three explicit instructions

**Current state:** `vlt-lint-full.js:161-168`. `convRead` (`:161-164`) is invoked in the
prompt for exactly `frontmatter`, `wiki-supersession`, `wiki-index` (`:167`). The prompt
carries the B7-6 rule-4 normalization instruction ("normalize both sides first per
frontmatter.md YAML rule 4 — strip surrounding quotes and [[ ]], strip a trailing .md,
compare on the vault-relative path"), asks Gap B unconditionally ("whether the
frontmatter sources: and the prose Sources section diverge (Gap B)"), and asks for
`unmarked_supersession` and `name_callout_targets` with no statement of what counts as a
callout. Absent: any read of `write-verification`, the coexistence posture, the
callout-form rule.

**Change (all in the two template literals at `:167-168`):**

1. **Read list** gains `${convRead('write-verification')}` (fourth in the list, so it
   rides the overlay-merge mechanics like the other three — `convRead` needs no change).
2. **Gap B goes conditional/tri-state**, replacing the current boolean ask. Target text
   (exact wording is the builder's; these clauses are load-bearing): *"for the
   sources-vs-prose comparison (Gap B), report `sources_vs_prose`: `no_prose_section`
   when the page carries no prose `## Sources` section — such a page is conformant (per
   write-verification@3, the wiki-page tier-1 item: frontmatter is the source of truth);
   `diverge` only when both exist and an entry in one is not traceable in the other;
   otherwise `match`."*
3. **Coexistence posture made explicit**, adjacent to the existing normalization
   instruction: *"a mixed state — wikilink-form and legacy bare-path `sources:` entries
   on one page or across pages — is conformant and never a finding: existing bare-path
   entries stay legal and there is no backfill sweep (per frontmatter@9 rule 4,
   coexistence posture)."*
4. **Callout form made explicit**, governing both `unmarked_supersession` and
   `name_callout_targets`, in both directions: *"a callout is only the Obsidian
   `> [!type]` blockquote form (per wiki-supersession@2): a supersession/staleness note
   written as a bullet, heading, or plain prose is NOT a marker — the claim it covers is
   still an unmarked supersession — and a bullet or heading questioning a name is NOT a
   name-verification callout (it yields no name_callout_targets entry)."*
5. **The existing rule-4 marker is normalized to A8's style:** "per frontmatter.md YAML
   rule 4" → "per frontmatter@9 rule 4". (Every restated instruction in the prompts must
   leave this build carrying a `per <convention>@N` marker whose version matches current
   source — verified versions: frontmatter@9, wiki-supersession@2, wiki-index@2,
   write-verification@3.)

**Why:** A10-7's root cause (the scanner was never handed the rule the ask enforces) and
A10-2's two seams (B5-3's class: model judgment where an explicit instruction should
sit). **Out-of-scope note:** the prompt's overall shape, chunking, model tiering, and the
parse-on-intake block (`:56-61`) are untouched — parse-on-intake must not regress
(standing rule).

## F3 — `PAGE_SCAN` schema + reducer: the tri-state field

**Current state:** `vlt-lint-full.js:115-116` —

```js
sources_vs_prose_mismatch: { type: 'boolean', description: 'GAP B — true if the frontmatter sources: list and the prose Sources section diverge (a URL in one not the other)' },
sources_vs_prose_detail: { type: 'string' },
```

`sources_vs_prose_mismatch` is **not** in the `required` list (`:99`). The one consumer is
the reducer at `:384`:

```js
sources_vs_prose_mismatches: scans.filter((s) => s.sources_vs_prose_mismatch).map((s) => `${s.slug}: ${s.sources_vs_prose_detail || 'frontmatter sources: vs prose Sources diverge'}`),
```

**Change (per disposition 1):**

- Replace the boolean property with
  `sources_vs_prose: { type: 'string', enum: ['match', 'diverge', 'no_prose_section'], description: 'GAP B — diverge only when the page has BOTH a frontmatter sources: list and a prose Sources section and an entry in one is not traceable in the other; no_prose_section when the page carries no prose Sources section (conformant per write-verification@3 — frontmatter is the source of truth); else match' }`.
- Add `sources_vs_prose` to the `required` array at `:99`. Remove the old key name
  entirely (no alias kept — the schema and its one consumer live in the same file).
- Reducer at `:384` filters `s.sources_vs_prose === 'diverge'`; the report slot name
  `sources_vs_prose_mismatches` and its entry format are unchanged.

**Why:** A10-7 fix site 2 — the boolean folds "no prose section" into "no mismatch" on a
good day and into a scanner's guess on a bad one; a required enum makes the conformant
state first-class and auditable (the tri-state counts are visible in raw scan output).

## F4 — cluster prompt: markers + the callout-form clause (audit-driven edit)

**Current state:** `vlt-lint-full.js:298-302` — the cluster ask instructs classification
"by the callout's recorded `**Disposition:**` line" and speaks of disagreements
"documented with a Contradictions section or callout", reading no convention and carrying
no source marker. The pair prompt (`:352-354`) has no convention content.

**Change (per disposition 4):** the cluster prompt's disposition-classification sentence
gains an inline `per wiki-supersession@2` marker, and one clause is added: *"a
disagreement recorded only as a bullet, heading, or plain prose — not an Obsidian
`> [!type]` callout — is NOT documented (per wiki-supersession@2); report it in
cross_page_contradictions."* No convention read is added to cluster or pair agents. The
pair prompt is untouched.

**Why:** A8's marker rule applied to the one other prompt that restates convention
vocabulary; direction-consistency with F2's callout-form clause (without it, the page
scanner and the cluster checker would disagree about what "documented" means).

## F5 — `full-scale.md` step 1: the derived cross-layer set, the predicate's single home, the supplement line, R4-fanout's second home

**Current state:** `skills/vlt-lint/references/full-scale.md:7` (step 1) — the assembly
instruction: "Also glob `{research}` (and any agent-zone note location the wiki
conventionally `[[links]]` into) for `*.md` basenames, normalized the same way page slugs
are — pass these as `crossLayerSlugs` so a valid cross-layer link isn't reported as a
missing target."

**Change:** replace that sentence (and only it — the stubs, overlay, and page-list
sentences around it are untouched) with the derivation + supplement. Target text (the
builder keeps the four bolded elements; wording may be smoothed):

> Build `crossLayerSlugs` by **derivation from the resolved `vault_structure` map** (the
> vault's `config.yaml` `vlt:` section — the *resolved* map, so vault-grown keys ride in
> automatically): a key **qualifies** when its resolved value names a *directory* of
> walker-visible linkable notes — every directory-valued key **except** the wiki's own
> (`wiki`), governance (`conventions`, `overlays`, `personas`), cold storage (`archive`),
> and report dirs (`lint_reports`). *(This predicate is single-homed here — other sites
> point at it, never restate it.)* Glob each qualifying key's directory for `*.md`
> basenames, normalized the same way page slugs are. **Interim supplement:** also glob
> `projects/`, `areas/`, `resources/`, and `_agent/handoffs/` — these hold linkable notes
> but have no `vault_structure` key today (key-minting waits on the merge-config
> `vault_structure` fix). **This supplement line is interim by design: the build that
> mints those keys into `vault_structure` deletes it in the same act.** Pass the union as
> `crossLayerSlugs` so a valid cross-layer link isn't reported as a missing target.

Plus **one line** at the end of step 2 (or as its own sentence after it) — R4-fanout's
second home: *"Fan-out currency (R4): any ask added to the workflow that enforces a
convention's rule adds that convention to its `convRead` and its `// depends_on:` ack in
the same edit — the rule's full text lives in the workflow's ack header."*

**Why:** A10-3 (the vague parenthetical missed three layers), D2 as narrowed by A7 (the
supplement names `_agent/handoffs/` alongside the PARA layers; retirement clause in the
shipped text; predicate single-homed here), and the R4-fanout home declaration.
**Out-of-scope notes:** the workflow's `crossLayerSlugs` intake (`:35-37`, `:78`, `:211`,
`:214`) is agnostic and correct — no workflow change for A10-3; the invoke line
(`full-scale.md:8`) passes the same args — unchanged; scrub check — the shipped text
names no vault or personal path (placeholder-path rule holds: these are layer names, not
a specific install's artifacts).

## F6 — `write-verification.md`: the consumer registration

**Current state:** `skills/vlt-setup/assets/governance/_meta/conventions/write-verification.md:12`
— `consumers: [vlt-ingest, vlt-extract, vlt-research, vlt-lint]`.

**Change:** append `vlt-lint-full.js` →
`consumers: [vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-lint-full.js]`.
No `version:` bump (disposition 6 — membership, not a rule change; mirrors
`frontmatter.md:12` / `wiki-index.md:12` / `wiki-supersession.md:12`, which already list
the workflow). No other edit to this file — the write-op qualifier on the `verified_by`
value set already prevents attestation-authority creep (disposition 6).

**Why:** the bipartite half of A8's handshake (F1 is the ack half); package-lint E1
verifies both directions.

## F7 — `checks.md:12`: the cross-layer description points at the map (grounding addition)

**Current state:** `skills/vlt-lint/references/checks.md:12` (Missing targets) describes
the cross-layer set as "(a `{research}` or agent-zone note the wiki legitimately
references)" — an inline enumeration that F5 makes stale (the set now includes PARA
layers and derives from the map).

**Change:** the parenthetical becomes a pointer, not a list — e.g. "(a note in a
cross-layer location — the derived glob set of `full-scale.md` step 1)". One-phrase edit;
the rest of the bullet (stubs clause, legal response) is untouched.

**Why:** single-home discipline — A7 single-homes the predicate in `full-scale.md`; this
is the one other site that restates the set. In scope beyond the filings' letter as a
grounding addition (an enumeration the build's own change falsifies).

## F8 — the fan-out audit (A10-7's general check — R4-fanout's retroactive first run)

**Procedure:** after F1–F5 land, walk **every** `agent(...)` ask in `vlt-lint-full.js`
and record, per ask: the convention rules it enforces or restates → the convention set
its scanner receives (its `convRead` mentions) → verdict. Record the table in the BUILT
`status:` (or the commit message if too long — the status then points at it). The clerk's
provisional table, to be re-derived, not trusted:

| Ask | Enforces/restates | Reads (post-build) | Verdict |
|---|---|---|---|
| `pageScanPrompt` (`:167-168`) | frontmatter@9 (validity, rule 4 + coexistence), wiki-supersession@2 (stale/supersession/callout form), write-verification@3 (Gap B tri-state) | frontmatter, wiki-supersession, wiki-index, write-verification | green after F2; wiki-index = read-without-ask, kept (disposition 5) |
| index ask (`:263-267`) | wiki-index@2 (structural-map rule) | wiki-index | green |
| cluster ask (`:298-302`) | restates wiki-supersession@2 disposition vocabulary + documented-form | none (mechanical classification) | green after F4 (markers, no read — disposition 4) |
| pair ask (`:352-354`) | none (proper-noun attribute comparison) | none | green |
| `thin` (schema desc `:120`) | none — criteria self-contained; class homed at `checks.md:21` | n/a | green |

**Why:** A10-7's load-bearing capture — the audit subsumes A10-2's residual and is
R4-fanout's retroactive first run (the roadmap's R4 declaration says exactly this: the
audit is the first run, not the fix).

## Registration

**None.** No new skill, workflow, or `module-help.csv` row; no convention `version:`
bump ⇒ no consumer re-ack walk beyond the single new registration this build itself
ships (F1 + F6, verified bipartite by package-lint Group E). Priced per the "no bump is
not no cost" rule: **C6** untouched (no operating-contract edit); **E4** untouched (no
new package-lint check ⇒ no `test-package-lint.py` case owed); **E5** touched — the ack
header edit (F1) is exactly the surface E5 parses, and Group E is the check of record for
it.

## Out of scope (dispositioned)

- **A10-1's repeat-aware report line** — deferred to B10-3 (D1: different instrument,
  `checks.md:47`, not the fan-out).
- **Minting `vault_structure` keys for `_agent/handoffs/` / the PARA layers** — deferred
  to B10-10 (A7: unsafe under the C6-b merge-config strip; the supplement line is the
  interim, its retirement is B10-10's bound cleanup).
- **B10-6's report-dir exclusion and B10-10's PARA inclusion edits to the predicate
  home** — theirs by design (A7); this build only establishes the home.
- **Giving the workflow a `{research}`-zone fan-out** — the named second-cut in
  `full-scale.md:9`; untouched.
- **Convention reads for cluster/pair agents** — rejected (disposition 4: mechanical
  classification, cost with no judgment to inform).
- **Removing the page scanner's `wiki-index` read** — rejected for this build
  (disposition 5: read-without-ask is not R4-fanout's target; recorded in the audit).
- **`report.md` / report-slot renames** — not needed (disposition 1: the slot name and
  entry format are stable; only the schema-internal field changes).
- **`checks.md:15`'s Gap B legal response** — already states the no-prose-conformant rule
  and the reconcile response; no edit (R3 satisfied by the existing home).
- **`para_missing_attestation`** — the structural slot the SKILL fills stays as-is;
  adding `write-verification` to `convRead` does not move PARA attestation into the
  workflow's jurisdiction (it sweeps `{wiki}` only).
- **The vlt-lint SKILL invoke line (`full-scale.md:8`)** — unchanged; the args contract
  is stable, only step 1's assembly of `crossLayerSlugs` changes.

## Verification (unit, at rest — lifecycle step 5)

1. **Syntax:** `node --check skills/vlt-setup/assets/workflows/vlt-lint-full.js` (the
   build-16/20 ritual).
2. **Handshake bipartite re-check:** `uv run tools/package-lint.py` **Group E** is the
   check of record (E1 consumers↔pins both directions, E5 asset-ack parse) — the
   `write-verification` `consumers:` gains `vlt-lint-full.js` and the ack gains
   `write-verification@3` in the same build; do **not** substitute a hand-written
   `grep "write-verification@"` as the recorded verification.
3. **Packaging lint:** the mid-arc `package-lint.py` **A/B/C/E** run passes (D /
   `--expect-version` is the release gate at B10-5, not here; no version bump in this
   build).
4. **Tri-state coherence greps (same file):** `sources_vs_prose_mismatch` has zero
   occurrences in the workflow post-build; `sources_vs_prose` appears in the schema
   `required` list, the property block, the prompt, and the `:384` reducer filter
   (`=== 'diverge'`); the report slot name `sources_vs_prose_mismatches` still matches
   `report.md:20`.
5. **Marker currency grep:** every `per <convention>@N` marker in the workflow matches
   the convention's current `version:` on disk (frontmatter@9, wiki-supersession@2,
   write-verification@3) — an *aid-while-editing* grep plus one recorded pass; Group E
   does not check prompt markers (they are A8's consumer-walk surface, re-derived by
   B10-4/B10-11's walks).
6. **Single-home greps:** the qualifying-key predicate text appears only in
   `full-scale.md`; `checks.md:12` carries the pointer, not an enumeration; the
   supplement line's retirement clause is present in the shipped `full-scale.md` text;
   R4-fanout's text appears in the ack header block and its one-line pointer form in
   `full-scale.md`.
7. **F8 audit recorded:** the per-ask table re-derived against the built file and
   recorded in the BUILT status (R4-fanout's retroactive first run).
8. **Fixture dry-run (behavioral, at rest):** a temp fixture wiki (3–4 pages: one with
   no prose Sources section, one with a legal mixed wikilink/bare-path `sources:` state,
   one with a bullet-form "superseded" note, one linking `[[some-handoff]]` into a fake
   `_agent/handoffs/`) — exercise what is exercisable without the workflow runtime:
   verify by *reading* the built prompts against each fixture that the instructed answer
   is unambiguous (no live agent run owed at rest; the live run is the field-contingent
   check), and run the step-1 derivation by hand against a fixture `config.yaml`
   `vault_structure` (default map + one vault-grown `bases:` key) confirming the
   qualifying set is `research, sessions, specs, partners, capabilities, bases` + the
   supplement's four.
9. **Fixture extension (R2): not applicable** — no release-gate check added or changed.
10. **Legal response (R3): not applicable beyond the existing home** — no new finding
    class; `checks.md:15` already carries the class's legal response.
11. **Enumeration widening (brief-anatomy R4): not applicable** — no file is added to any
    enumerated class; this build *replaces* an enumeration with a derivation (F5), which
    is the rule's spirit applied in reverse, and the one downstream restatement is
    re-pointed (F7).
12. **Scrub:** no personal or vault-local content in any changed shipped file (F5's
    supplement names generic layer dirs, not an install's artifact paths; the fixture
    stays in temp, out of the tree). **No `.decision-log.md` left in the working tree.**
13. **Parse-on-intake regression guard:** `vlt-lint-full.js:56-61` (the JSON-string args
    parse) is byte-identical pre/post build.

## Acceptance (live — appended to the roadmap ledger)

Five checks; 1–4 ship-verifiable (gate closeout), 5 field-contingent.

1. **`[ship-verifiable]`** — the handshake is bipartite-consistent: `write-verification@3`
   `consumers:` lists `vlt-lint-full.js` and the workflow's `// depends_on:` header acks
   `write-verification@3`; **package-lint Group E PASS** is the discharge (at rest, this
   session or the v0.13.0 release gate).
2. **`[ship-verifiable]`** — the tri-state landed whole: the boolean field is gone, the
   required enum is in the schema, the prompt instructs the three states with the
   no-prose-conformant conditional, and the reducer populates
   `sources_vs_prose_mismatches` only from `diverge` (Verification 4's greps +
   `node --check`); discharged at rest.
3. **`[ship-verifiable]`** — the three explicit instructions are present with current
   markers: coexistence posture (`per frontmatter@9 rule 4`), callout-vs-bullet in both
   directions (`per wiki-supersession@2`, page scanner **and** cluster ask), Gap B
   conditional (`per write-verification@3`) — and every marker version matches the
   convention's `version:` on disk (Verification 5); discharged at rest.
4. **`[ship-verifiable]`** — the derivation shipped with its interim honest: `full-scale.md`
   step 1 derives from resolved `vault_structure` keys with the qualifying-key predicate
   single-homed there, the supplement line names `projects/`, `areas/`, `resources/`,
   `_agent/handoffs/` **and carries its own in-file retirement clause**; `checks.md:12`
   points rather than enumerates; R4-fanout's rule text stands in the ack header block
   with its one-line pointer in `full-scale.md`; the F8 audit table is recorded in the
   BUILT status; discharged at rest by greps + the recorded audit.
5. **`[field-contingent]`** — the repaired signal is quiet where the field was loud.
   Discharging event: **the owner's first full-mode `vlt-lint` sweep (>30 pages, the
   fan-out path) on vlt-core after the v0.13.0 upgrade** (performer: the owner; vault:
   vlt-core; evidence reaches the factory via the persisted `{lint_reports}` file — lint
   already persists verbatim, no interim posture needed). Pass = (a)
   `sources_vs_prose_mismatches` contains no page whose only "defect" is having no prose
   Sources section (the 22-of-25 false class collapses); (b) `missing_targets` contains
   no valid link into `_agent/handoffs/`, `areas/`, `projects/`, `resources/`, or a
   vault-grown key's directory; (c) no new false-positive class from the added
   instructions — a legal mixed `sources:` state is unflagged while a bullet-form
   supersession note still (correctly) surfaces as unmarked. Fail = any of the three
   classes persists, or a fixed class returns under a new name.

## Next lifecycle move

A **fresh builder session** implements this brief via `bmad-workflow-builder`. Builder
exit obligations: rewrite `status:` to a BUILT record with numbered deliberate deviations
(and the F8 audit table), delete any `.decision-log.md`, one commit for the build. After
B10-2: brief B10-3 (table order; B10-4 is unblocked by B10-1 but sits after B10-3).
