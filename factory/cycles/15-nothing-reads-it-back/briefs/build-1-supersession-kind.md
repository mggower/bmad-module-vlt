---
title: 'Build #1 — a `supersession` kind on the feedback rail: after this ships, a vault owner filing a retirement gets an issue that says it is one — findable by label, routed by its own form, and checked by triage against the body — instead of a candidate whose real class survives only in a note nothing machine-readable can read'
status: 'BRIEFED 2026-09-02 — build via bmad-workflow-builder in a fresh session. The builder rewrites this line to a BUILT record: `BUILT <date> — <what landed>; <verification result>. Deviations/notes: (1) … (2) …` with numbered deliberate deviations (precedent: Cycle 14 build-5), deletes any `.decision-log.md`, one commit for the build. Not the release build — no version bump here (rides build-7 / v0.18.0).'
module_code: 'vlt'
created: '2026-09-02'
derives_from:
  - 'factory/inbox/2026-09-01-183000-rail-kind-set-has-no-value-for-a-supersession.md (A15-15 — the whole filing: the `kind` value set, the label row, the composer, the fourth form, the tracker label; sites 5–7 as corrected by roundtable A10)'
roadmap: 'factory/cycles/15-nothing-reads-it-back/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-09-01/02): Q6 (one act, no split, additive-only, no `rail_contract` bump); E3 as amended (widening a closed value set is additive when no existing value''s meaning changes — build-1 writes that into the rule); S-3 named-not-consumed (the fourth form inherits the `@mention` line verbatim); roundtable A9 (ordering sentence struck; #17/#18 re-kinded by an owner act, checked here) + A10 (site 5 phantom; site 6 = intake materializer; site 7 = `config.yml`; two optional additive payload fields); obsolescence beat: none found; instrument beat property for build-1.'
risk: 'low — additive vocabulary; no handshaked convention moves (the field contract is versioned by `rail_contract`, ruled unbumped by E3); no consumer walk; one new repo-side file (`.github/`, never copied into vaults); a `module-help.csv` row edit that must keep package-lint Group B quoting.'
specimens: '2/2 — observed: tracker issues #17 and #18 (the class''s first two live instances, both mis-kinded `candidate`); preserved: both are the subjects of check (3), and #17''s materialized body is the seed of the check (4) fixture.'
---

# Build #1 — a `supersession` kind on the feedback rail

## Intent

The module has four filing classes and its transport carries three. `factory/inbox/README.md:71-93`
defines `supersession` (platform P-15) with two mandatory halves no other class requires; the field
contract's `kind` row (`skills/vlt-feedback/references/field-contract.md:42`) still reads
`defect | pattern | candidate`, its label table (`:68-79`) has no fourth classification row, and the
three issue forms each hard-code one kind. The class's first two live instances — tracker **#17**
and **#18**, this cycle's A15-12 and A15-13 — went up as `field:candidate` with an apologetic note
in the body that no label filter, form router, triage check, or intake reads.

This build widens the vocabulary **in one act across every surface that names it** (Q6) so that a
retirement is a retirement everywhere the rail looks: the contract's value set and label table, the
`vlt-feedback` composer and its help row, a fourth issue form, the tracker's label bootstrap, and
the factory intake's materializer — which now writes the `class: supersession` opening-line marker
that `inbox-capture`'s grounding keys on. The two mandatory halves ship as two **optional, additive
payload fields** (`superseded_rule`, `superseding_mechanism`), required when `kind: supersession`,
so triage and the intake have something structured to read rather than prose to interpret.

**Additive-only, by ruling and by the contract's own rule:** no `rail_contract` bump, no filed
issue invalidated (E3). The ordering sentence ideation first wrote ("first because the class must
exist before the beat") is **struck** (A9) — the beat was the roundtable, which preceded every
build; what remains real is an owner act after this build lands (§Brief-time dispositions 6).

All rejected alternatives in the parent filing are settled — do not re-litigate: no fifth class, no
change to what the three existing kinds mean, no change to the README's two mandatory halves, no
shared dropdown (there is none to widen), no split across channels.

**The property this build's acceptance protects** (roadmap §Instrument beat, stated without the
fix): *a filing whose body says `kind: supersession` reaches the tracker under a label, a form
route, and a materialized `class:` opening line that a filter, a router, triage, and capture each
read as a retirement without opening prose — and a body/label disagreement is flagged, never
defended.*

## Brief-time dispositions

Ideation left no question to brief time for this build (roadmap §Questions deliberately left to
brief time names builds 2, 4, 5 only). The dispositions below are the judgment calls this headless
run made inside the rulings' letter, each recorded so the builder does not re-decide them.

### 1. Where the two new fields sit in the payload order — immediately after `kind`

The contract's field table is normative for section order (`field-contract.md:33-35`: the composer
emits *"one `### <field_id>` section per field, in this order"*). The intake parses sections **by
id** (`github-intake.md:61`), not by position, so inserting two rows mid-table breaks no existing
issue's parse; every issue filed so far has eight sections and simply lacks the two optional ones.
**Ruling:** `superseded_rule` and `superseding_mechanism` go directly after `kind` — a
conditionally-required pair reads next to the field that conditions it — with `Required` = *"when
`kind` is `supersession`; otherwise absent"*. Appending them at the tail was the alternative; rejected
because a reader of a supersession issue would find its two halves after the version stamps.

### 2. What "holds materialization when both halves are unidentifiable" means — either half missing holds

A10's words are *"holds materialization when both halves are unidentifiable"*. The README is
stricter and older: a supersession *"carries **both halves** or it is not one"* (`README.md:80-81`).
**Ruling:** the intake holds a `kind: supersession` issue for hand-handling when **either**
`### superseded_rule` or `### superseding_mechanism` is absent or empty — read A10 as *"when the two
halves cannot both be identified"*, which is the only reading consistent with the class definition
it cites. A held issue gets the same treatment as a stale-shape one (`github-intake.md:35-42`):
reported by name, no label change, no hopeful materialization. It is never materialized as a
`candidate` — that is the exact failure the filing describes.

### 3. Form field types and the fourth form's `kind` dropdown

The fourth form mirrors `field-candidate.yml` byte-for-byte in structure: `labels:` hard-coded to
`["vault-filed", "field:supersession"]`, a single-option `kind` dropdown (`options: [supersession]`),
and the two halves as **`textarea`, `required: true`** in this form (the form is supersession-only,
so the contract's conditional requirement is unconditional here). The existing three forms are **not
touched** — they carry no `kind` list to widen (Q6's grounding) and the two new fields are absent
from them by design (optional in the contract; meaningless for the other kinds).

### 4. The `@mention` line — inherited verbatim, S-3 met not consumed

`field-candidate.yml:17` (grounding correction — the roadmap's `:16` is the line above it) carries
the amend-after-capture instruction with a literal maintainer `@mention`. `S-3`
(`factory/platform/spikes/S-3-github-notification-semantics.md`, `harvested`, verdict `reshape`)
answers whether that mention can be replaced by a trigger naming nobody; ideation ruled no Cycle 15
build consumes it (§Spikes). **Ruling:** the fourth form inherits the line **verbatim**, so all four
forms say the same thing, with a **YAML comment** above it: `# The @mention below is S-3's open
question (factory/platform/spikes/S-3-*.md) — inherited unchanged; replacing it is A11-2's build,
not this one.` The spike's `consumed_by:` is **not** appended — the gate passed on `spike: none`,
and citing a register file's existence is not consuming its finding.

### 5. Label color and description for `field:supersession`

`config.yml:13-15` gives each classification label a distinct color and a one-clause description.
**Ruling:** `--color BFD4F2 --description "Field contract: retirement ask — a shipped protection made
redundant by a named mechanism"`. Color is unclaimed by any existing label in the block; the
description follows the block's `Field contract: <meaning>` form.

### 6. The owner act this build does not perform, and how it is checked

A9: **#17 and #18 are re-kinded by an owner act after build-1 lands** — body `kind:` →
`supersession` (the `### kind` section's value) **and** label `field:candidate` → `field:supersession`.
The body's `kind` is authoritative to triage (`issue-triage/SKILL.md:70-72`), so a label-only relabel
manufactures exactly the mismatch triage flags. Neither issue is re-materialized: both filings on disk
carry a hand-written `origin:` header (`factory/inbox/2026-09-01-160000-…`, `…-170000-…`), which is
the idempotency key. **The act is bound: before the v0.18.0 tag** (the owner runs the label bootstrap
in `config.yml` at the same sitting — the new label must exist before the re-label can apply).
Acceptance check (3) grades it.

### 7. Interim posture (R1) — not applicable

Nothing here ships a rule ahead of its mechanism. The conditional requirement on the two halves is
enforced at the two points it can be: the form (`required: true`) and the intake's hold (§2). The
composer is a prose skill and cannot enforce, but it never could for any field — that is the rail's
standing shape, not a new gap.

### 8. Retirement clause (P-15) — not applicable

The roundtable's obsolescence beat ruled **`Obsolescence: none found`** for this build (additive
vocabulary). Re-checked at brief time against every site enumerated in §F-sites: no prohibition,
check, or carve-out becomes redundant. The apologetic classification note in #17/#18's bodies is a
workaround, not a rule, and the owner act in §6 makes it moot without retiring anything.

### 9. The word seam: `class:` in a filing, `kind:` on the rail

The beat named this so no brief invents a third word. **`kind: supersession`** is the rail's value
(payload field, label, form); **`class: supersession`** is the inbox filing's opening-line marker
(`README.md:80`, `grounding-methodology.md:59`). The intake is the one place the two meet, and it maps
one to the other (F6). No other artifact uses either word for the other's surface.

## F-sites

Every `file:line` below was re-derived against the working tree at brief time (branch
`cycle15-v0.18.0`, tip `54ae147`). Grounding outcome per site is marked.

### F1 — `skills/vlt-feedback/references/field-contract.md` — the single home (HOLDS)

Four edits, all in the file that every other surface derives from:

1. **`:42` — the `kind` row.** Current: *"Honest classification: `defect` (shipped behavior is
   wrong), `pattern` (a recurring shape worth naming), or `candidate` (a "this should ship upstream"
   proposal)."* Add a fourth value **in the same sentence shape**: *"`supersession` (a shipped
   protection is now redundant because a named mechanism enforces what it stood in for — carries
   both halves below, or it is not one; the class is defined in the factory's
   `factory/inbox/README.md`)."* Keep it one clause; the halves are the two rows that follow.
2. **New rows after `:42`** (disposition 1):
   `| superseded_rule | when kind is supersession | The rule now redundant — its exact site (path:line) and what it was standing in for. |`
   `| superseding_mechanism | when kind is supersession | The mechanism that supersedes it — what shipped, where, and why its population covers the rule's. |`
   Text mirrors `README.md:83-86`'s two halves (a pointer-grade paraphrase, not the README's prose
   verbatim — the README stays the class's home).
3. **`:15-18` — the Evolution rule.** Append E3's amended ruling as one sentence after *"…changing a
   label's meaning bumps."*: **"Widening a closed value set (a `kind` value, a label family) is
   additive when no existing value's meaning changes."** This is the sentence E3 ruled build-1
   writes; a strict reader of the current text would read a value-set widening as *"changing a
   field's meaning"* and bump.
4. **`:72` — the label table.** Insert after the `field:candidate` row:
   `| field:supersession | template (supersession form) or filer/triage | Classification: retirement ask — a shipped protection is now redundant; the body carries both halves (superseded_rule, superseding_mechanism). |`
   The `:3-7` preamble (*"three surfaces"*) is about surfaces, not kinds — unchanged.

**Why:** this is the SSoT; every other F-site is a pointer or a derived surface. **Out of scope
here:** `rail_contract` stays `1` (`:12`) — E3.

### F2 — `skills/vlt-feedback/SKILL.md` — the composer (HOLDS, one cite corrected)

- **`:4` frontmatter `description`** — *"classify honestly (defect / pattern / candidate)"* →
  *"(defect / pattern / candidate / supersession)"*. Nothing else in the description moves.
- **`:51-53` — judgment core step 2** — add the fourth kind in the list's own idiom:
  *"`supersession` (a shipped protection is now redundant — name the rule and the mechanism; the
  contract's two conditional fields carry them)"*, and keep *"Don't inflate a preference into a
  defect."*
- **`:61-62` — compose** *(grounding correction: the roadmap's A10 enumeration cites `:56`, which is
  the duplicate-guard `gh issue list` line and names no kind; the compose instruction is `:61-62`)*.
  Current: *"Compose the full payload per the contract: one `### <field_id>` section per field, in the
  contract's order…"* This already follows the contract's table, so the two new fields ride
  automatically; add one clause so the conditional is explicit: *"— for `kind: supersession` the two
  conditional sections are mandatory, and a filing missing either is not composed."*
- **`:87-88` and `:101`** — `field:<kind>` is already generic; **verified, no edit**.
- The failure-path outbox (`:125-134`) writes *"every payload section"* — generic; **no edit**.

**Why:** the composer is the only writer that could emit the value; without this the vault-side
half of the rail cannot say `supersession` at all. `depends_on: ["decision-log@4"]` (`:3`) is
untouched — no convention moves.

### F3 — `skills/vlt-setup/assets/module-help.csv:18` — the help row (HOLDS)

Two fields on the `vlt-feedback` row: description *"classify honestly (defect / pattern / candidate)"*
→ *"(defect / pattern / candidate / supersession)"*; args
`"{note: …}|{kind: defect | pattern | candidate}"` → `"{note: …}|{kind: defect | pattern | candidate | supersession}"`.
Keep every free-text field quoted (package-lint Group B; CLAUDE.md). **Why:** the help surface is
the one enumeration of kinds a vault user sees before invoking the skill.

### F4 — `.github/ISSUE_TEMPLATE/field-supersession.yml` — the fourth form (NEW; repo-side, rides along)

Copy `field-candidate.yml` (76 lines) and change exactly:

- `:5-7` — `name: Field supersession`; `description: A live vault says a shipped protection is now
  redundant because a named mechanism enforces it. Follows the field contract.`;
  `labels: ["vault-filed", "field:supersession"]`.
- `:17` — the `@mention` line **verbatim**, preceded by the S-3 YAML comment (disposition 4).
- `:39-47` — the `kind` dropdown: `description: This form files supersessions (a retirement ask); the
  classification is fixed.`; `options: [supersession]`.
- **Insert after the `kind` block** (disposition 1's order), two `textarea` fields, both
  `required: true`: `id: superseded_rule` (label `superseded_rule`, description *"The rule now
  redundant — its exact site (path:line) and what it was standing in for."*) and
  `id: superseding_mechanism` (label `superseding_mechanism`, description *"The mechanism that
  supersedes it — what shipped, where, and why its population covers the rule's."*).
- The header comment (`:1-4`) keeps the ADDITIVE-ONLY notice and the SSoT pointer.

**Why:** each form hard-codes one kind and one label (Q6 grounding); a fourth kind is a fourth form.
`field-defect.yml` / `field-pattern.yml` / `field-candidate.yml` are **not edited**.

### F5 — `.github/ISSUE_TEMPLATE/config.yml:13-15` — the label bootstrap block (HOLDS)

Add, after `:15`:
`#   gh label create "field:supersession" --repo mggower/bmad-module-vlt --force --color BFD4F2 --description "Field contract: retirement ask — a shipped protection made redundant by a named mechanism"`
(disposition 5). The block is documentation of an idempotent owner act; the act itself runs at the
release sitting (§Acceptance (2)). **Why:** the tracker label is a site (Q6 site 3) and this block is
where every other rail label is defined for the bootstrap.

### F6 — `.claude/skills/inbox-capture/references/github-intake.md` §4 — the materializer (HOLDS; A10's site 6)

- **`:61`** — *"Parse the eight `### <field_id>` sections"* → *"Parse the `### <field_id>` sections
  (the contract's field table is the list — eight for every kind, ten for `supersession`)"* — the
  hard count was a restatement waiting to drift.
- **`:66-69` — the written header.** Add a bullet: **"when the payload's `kind` is `supersession`,
  the filing's opening line is `# \`class: supersession\` — <title>`** — the marker
  `factory/inbox/README.md:80` defines and `inbox-capture/references/grounding-methodology.md:57-59`
  keys on; without it a rail-filed retirement is graded as a candidate. The two halves are carried as
  their own sections (`## superseded_rule`, `## superseding_mechanism`) so the grounding's
  *verify-both-halves-separately* step (`grounding-methodology.md:64-67`) has them by name."
- **New hold (disposition 2), beside the stale-shape gate's idiom:** *"A `kind: supersession` payload
  missing either half — no `### superseded_rule` or `### superseding_mechanism` section, or an empty
  one — is **held for hand-handling** exactly as a stale-shape issue is: reported by name, no label
  change, never materialized under another class."*
- **Cite re-pointing (grounding EXPANDED):** every `field-contract.md:<lines>` cite in this file is
  already stale against the contract as it sits today and drifts further after F1. Re-point all of
  them to the post-edit lines: `:30` (state flow — currently `:73-78`, is `:81-86` today), `:57` and
  `:67` (origin header — currently `:49-52`, is `:53-57`), `:62` (field table — currently `:29-38`, is
  `:37-46`), `:91` and `:144` (label table — currently `:56-78`, is `:62-79`); `:38` (`:12`) and `:41`
  (`:15-21`) hold today but shift if F1 edit 3 adds a line — re-derive after the edit. *(Roundtable
  A10 named `:57, :61` as the drifting cites; grounding finds eight of ten stale — corrected in the
  roadmap.)*

**Why:** this is the one place the rail's `kind:` becomes the filing's `class:` (disposition 9); it
is the site that turns the promise's *"checked … against the body"* into something capture reads.

### F7 — `.claude/skills/issue-triage/SKILL.md` — the classification check (HOLDS; site 5 as corrected)

There is **no enum to widen** (A10 — site 5 was a phantom): `:70-72` compares the body's `kind`
against the `field:*` label generically and stays as written. Two edits:

- **`:70-72`** — append one sentence: *"For `kind: supersession`, also confirm both halves are present
  (`superseded_rule`, `superseding_mechanism`) — a missing half is a drafted `needs-info`, never a
  drafted re-kind to `candidate`."*
- **`:81`** — the cite `field-contract.md:56-78` → the post-F1 label-table lines (`:62-79` today).
  `:61`'s `:15-21` holds today; re-derive after F1 edit 3. *(Grounding correction: A10 cited
  `issue-triage/SKILL.md:52, :78` as the drifting cites — `:52` is the amendment sweep and `:78` is
  blank; the cites are at `:61` and `:81`.)*

### F8 — `factory/inbox/README.md:80` — one pointer sentence (HOLDS; grounding addition)

After *"marked `class: supersession` in its opening line"* (`:80-81`), add a pointer: *"(a retirement
filed through the remote rail arrives as `kind: supersession` and the factory intake writes this
marker — `.claude/skills/inbox-capture/references/github-intake.md` §4)"*. A pointer, not a
mechanic; single-home preserved. **Why:** the README is where a reader of a hand-written filing looks
for the class; without the pointer the rail route is invisible from the class's own home.

## Registration

**None.** No new skill (`skills/vlt-*` is unchanged in membership; package-lint C5 has nothing to
see); no new workflow. The `module-help.csv:18` edit is a row **edit**, not a registration — keep
it inside Group B's quoting canon. **No handshake owed:** no `governance/_meta` convention is
touched; `vlt-feedback`'s `depends_on` is unchanged; the field contract's own version
(`rail_contract: 1`) does not bump (E3). **No bump, and no hidden cost either:** C6 (operating
contract), E4 (new lint check), E5 (asset `// depends_on:`) are all untouched by this build.

## Out of scope (dispositioned)

- **A fifth class, or any change to the three existing kinds' meanings** — rejected by the filing and
  Q6; the additive-only rule (`field-contract.md:15-18`) is what keeps `rail_contract` at 1.
- **Replacing the `@mention` line with a nobody-named trigger** — A11-2's build; `S-3` is harvested
  and deliberately unconsumed this cycle (§Spikes). The fourth form inherits the line.
- **Re-kinding #17/#18** — an owner act after this build (disposition 6), not a build edit; the
  intake never re-materializes (hand-written `origin:` headers are the key).
- **The `para_author_unknown` closed enumeration** (Cycle 14 carry 6) — released; the next
  `supersession` candidate the owner may file through the rail this build completes.
- **`issue-triage`'s tracker sync (milestone/build issues)** — no label of the sync's stage set
  changes; the `captured` label-drift fix P-10 named rides Cycle 15's sync, not this build.
- **`vlt-feedback`'s park-recording section (`:107-123`)** — a supersession filing can park an
  interim like any other; nothing kind-specific is owed.
- **A machine parser for the intake** — the intake is a prose procedure executed by an agent
  (`github-intake.md:13`); this build does not script it. The materializer check below is therefore a
  reader protocol, named as such.

## Verification (unit, at rest — lifecycle step 5)

1. **Value-set agreement across every enumerating site** — for each of `defect`, `pattern`,
   `candidate` run `grep -rn -e '<value>' skills/vlt-feedback skills/vlt-setup/assets/module-help.csv
   .github/ISSUE_TEMPLATE .claude/skills/issue-triage .claude/skills/inbox-capture/references/github-intake.md`;
   every hit that names the value **as a kind** (not as a label-table row for its own label, not a
   form that files only that kind) must sit in a file that also names `supersession`. Expected sites
   naming all four: `field-contract.md` (`kind` row), `vlt-feedback/SKILL.md` (`:4`, `:51-53`),
   `module-help.csv:18`. Expected sites naming exactly one (their own): the four forms.
2. **Cite re-point** — `grep -rn 'field-contract.md:' .claude/skills/` and confirm every cited range
   opens on the section it names in the post-edit file (read each; ten cites across two files).
3. **Fourth form parses** — `python3 -c "import yaml,sys; yaml.safe_load(open('.github/ISSUE_TEMPLATE/field-supersession.yml'))"`
   exits 0; `labels` equals `["vault-filed","field:supersession"]`; the `kind` dropdown has exactly
   one option; `superseded_rule` and `superseding_mechanism` are `required: true`; field `id`s match
   the contract's field ids byte-for-byte. `diff field-candidate.yml field-supersession.yml` shows
   only the edits F4 names.
4. **Fixture pair for the materializer** (P-18 — built from the failure's shape): materialize two
   payload bodies into `factory/cycles/15-nothing-reads-it-back/fixtures/`:
   `build-1-supersession-payload-17.md` — #17's real body (`gh issue view 17 --json body`) re-shaped
   with `kind: supersession` and its two halves lifted from the filing's own §1/§2 into the two new
   sections (the specimen, not a synthesized stand-in); and `build-1-supersession-payload-missing-half.md`
   — the same with `### superseding_mechanism` deleted. Then run §4 of `github-intake.md` as a **reader
   protocol** (an agent executing the procedure over the fixture bodies, no `gh` call, writing to a
   scratch path, never to `factory/inbox/`): the first yields a filing whose line 1 begins
   `# \`class: supersession\`` and carries both `##` half sections; the second is **held** with the
   named reason and writes nothing. Record both outcomes in the BUILT `status:`.
5. **Package lint** — `uv run tools/package-lint.py` Groups **A/B/C/E** PASS (Group B is the one this
   build can break: the csv row edit). D / `--expect-version` is build-7's.
6. **Handshake** — nothing moved; **Group E** is still the check of record and must stay green (no
   hand-written grep as the recorded check).
7. **R3 (legal response)** — this build adds no finding class to lint/dispatch. The intake's new
   hold states its own response inline at F6 (*held for hand-handling; no label change*) beside the
   stale-shape gate whose idiom it borrows. `R3: satisfied at the hold's single home`.
8. **R4 (enumeration widening)** — this build adds one repo-side file
   (`.github/ISSUE_TEMPLATE/field-supersession.yml`) and two factory fixtures. **Declared outside
   every enumerated class:** `.github/` is never in the own-the-apply copy surface (CLAUDE.md
   §Git & publishing), no manifest or vital enumerates issue forms, and `fixtures/` is P-18's
   un-enumerated cycle directory. `R4: not applicable — declared exclusion, reasoning above.`
9. **Scrub** — the new form and the contract edits carry no vault-local or personal content; the
   form's `@mention` is the pre-existing public maintainer handle inherited verbatim (S-3's question,
   not this build's). Fixtures derived from #17 are already-public issue text.
10. **Cleanup** — no `.decision-log.md` left in the tree.

## Release

Not the release build. v0.18.0's bump, lint gate `--expect-version 0.18.0`, and tag ride build-7.
The CHANGELOG entry collects this brief's `title:` verbatim at that point.

## Acceptance (live — appended to the roadmap ledger)

**Five checks — four `[ship-verifiable]` (GATE), one `[field-contingent]`.** `specimens: 2/2`.

**(1) `[ship-verifiable]` — at rest — GATES.** *Every surface that names the rail's kind set names
`supersession`.* **Instrument:** Verification 1's per-value grep manifest, recorded as the list of
hits in the BUILT `status:`. **Adversary:** property — *no site the rail reads or a filer sees still
carries a three-value kind set*; passing-violating state — a site that names the kinds in a form a
grep for `supersession` beside `candidate` misses (the help row's `|`-separated args string; the
SKILL description's `/`-separated list). **Widened:** the instrument greps each **old** value
individually and requires every kind-naming hit to co-occur with `supersession` in the same file,
rather than grepping for the new value; the four single-kind forms are the enumerated exception.

**(2) `[ship-verifiable]` — at the release sitting — GATES.** *A retirement has its own route and its
own label on the live tracker.* **Instrument:** after the owner runs the `config.yml` bootstrap
block at the v0.18.0 release sitting, `gh label list --repo mggower/bmad-module-vlt --json name` contains
`field:supersession`, and `https://github.com/mggower/bmad-module-vlt/issues/new/choose` lists four
field-contract forms (a reader confirms; the rendered chooser is the only instrument GitHub offers
at rest). **Adversary:** property — *a filer choosing "supersession" lands on a form that can only
file one*; passing-violating state — the label exists and the chooser lists the form, but the form's
`labels:` line still says `field:candidate` (a copy-edit miss). **Widened:** Verification 3's parse
asserts the `labels:` value byte-for-byte; this check cites it as its second leg.

**(3) `[ship-verifiable]` — after the owner act, before the v0.18.0 tag — GATES** *(roundtable A9)*.
*#17 and #18 are re-kinded and triage sees no mismatch.* The owner re-kinds both (body `### kind` →
`supersession` **and** label → `field:supersession`) after build-1 lands. **Instrument:** for each
of #17, #18, `gh issue view <n> --repo mggower/bmad-module-vlt --json labels,body` and the comparison
`issue-triage/SKILL.md:70-72` specifies, applied directly (both issues are `captured`, so triage's
own queue excludes them — the check is the comparison, not a triage run); evidence = the two
`kind`/label pairs recorded in the ledger discharge note. **Adversary:** property — *the body's kind
and the label agree, and both say retirement*; passing-violating state — label re-applied, body
left `candidate` (the exact mismatch A9 warns of) — caught, since the instrument reads both; second
state — both re-kinded but the apologetic classification note still stands in the body, so a human
reader is told the value is a nearest fit. **Widened:** the instrument also asserts the body no
longer carries the classification-note paragraph (grep the body for "nearest fit" / "classification
note"); a stale note is a FAIL, not cosmetic.

**(4) `[ship-verifiable]` — at rest — GATES.** *A rail-filed supersession materializes as a
`class: supersession` filing, and a half-less one is held.* **Instrument:** Verification 4's fixture
pair and reader protocol; evidence = the scratch filing's first line and the hold's reported reason,
both quoted in the BUILT `status:`. **Adversary:** property — *capture grades a rail-filed retirement
as a retirement, never as a candidate*; passing-violating state — the marker is written on line 1
but `grounding-methodology.md:57-59` keys on a different spelling or position (e.g. the marker must
open the line, and the fixture output puts the title first). **Widened:** the instrument's assertion
is not "the marker appears" but "the produced line 1 is byte-equal to the shape
`factory/inbox/README.md:80` describes and matches what the two hand-written specimens on disk
(`2026-09-01-160000-…`, `…-170000-…`) open with" — the specimens are the oracle.

**(5) `[field-contingent]`** — *a vault files a real retirement through `vlt-feedback` and it arrives
right.* **Event:** the next `supersession` filing composed in a live vault — the named candidate is
Cycle 14 carry 6 (`para_author_unknown`'s closed `human|agent|hybrid`), which ideation released to
the rail this build completes. **Performer:** the owner, from `{field-vault}` (readable from the
factory machine). **Grades:** the issue carries `field:supersession`, both half sections non-empty,
and **no classification note** in the body; the next `inbox-capture` run materializes it with the
`class: supersession` opening line and grounds it under `grounding-methodology.md` §Grounding a
`supersession` filing. Unbounded by construction (nothing in the release causes a vault to retire a
rule); routes to the standing watch register at closeout if unfired.
