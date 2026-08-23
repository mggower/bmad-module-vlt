---
title: 'Build #B10-7 — the rail amendment channel (a captured issue stops being write-only:
  the owner-applied amended label routes post-capture comments into the factory, the triage
  verdict vocabulary becomes queryable labels, and the issue forms arrive triage-ready)'
status: 'BUILT 2026-08-22 — all six F-sites landed on arc10-v0.14.0: field-contract.md
  gains the amended/needs-info/declined:<reason> rows, the amendment verb in the state flow,
  the label-additions-additive evolution clause, the non-enumerative label intro, the
  retired shared-form parentheticals, and the sharpened provenance_guess; the shared
  field-pattern-candidate.yml is deleted and per-kind field-pattern.yml/field-candidate.yml
  land with true label pairs, single-option kind dropdowns, contract-ordered ids, and the
  A14 affirmative-move sentence (literal @mggower) replacing the B10-1 interim note in all
  three forms; config.yml bootstrap goes non-enumerative and provisions the seven new
  labels; github-intake.md gains the "## 6. Amendment leg" (consume-on-read, comment-
  granular dated appends, archived-filing + no-filing holds, no stale-shape gate,
  joins-the-un-captured-set) plus the owner-verb clause in "does not own"; inbox-capture
  SKILL.md step list widens by "amendment leg"; issue-triage is A13-clean (re-applied
  vault-accepted struck, sweep routes to the intake leg), decline ops labeled
  (declined + one declined:<reason>), hold-with-question drafts needs-info; vlt-lifecycle.md
  gains the amendment-observable row and pluralizes the off-disk note.
  Verification: form YAML all parse, ids contract-ordered, labels true, kind single-option
  (real pyyaml run); "amendment channel is planned" 0 in .github/, "re-applied
  vault-accepted" 0 in .claude/skills/, @mggower present in all three forms; label
  vocabulary in exactly the five expected homes, meanings cited to the contract table;
  seam check 0 new .claude/ refs in shipped surface; six-case desk-check (a)-(f) all PASS;
  package-lint A/B/C/E PASS (D skipped, not a release build); no .decision-log.md; scrub
  clean (only the pre-existing repo slug + the ruled @mggower mention).
  Deviations/notes: (1) the "even labels" grep is 0 over live surfaces (skills/ shipped
  files, .github/, .claude/skills/) — residual hits are historical records only (this
  brief, the arc roadmap, and closed-arc archives in gitignored skills/reports/, which
  document the fix and are never rewritten). (2) contract line-number cites downstream
  were refreshed for the shifted anchors (evolution rule :15-21, field table :29-38,
  origin :49-52, label set :56-78, state flow :73-78) in github-intake.md and
  issue-triage SKILL.md. (3) the amendment leg adds a third hold case not spelled in
  disposition 4: a captured+amended issue with no origin: hit anywhere (label drift,
  captured-but-never-materialized) is reported held — no append target exists.'
module_code: 'vlt'
created: '2026-08-22'
derives_from:
  - 'inbox/2026-08-21-150500-captured-issues-accept-comments-the-intake-never-reads.md
    (A10-8 — the field contract''s state flow has no amendment verb; a captured issue is a
    write-only surface for its filer across the whole open window; proven live on issue #1''s
    2026-08-21 comment, which reached the factory only by owner mention)'
  - 'inbox/2026-08-21-181500-rail-triage-arc-surface-candidates.md (A10-15 C1 + C2 —
    C1: the label table admits only accept/decline as triage outcomes; needs-info, duplicate,
    and the decline-reason taxonomy live in comment prose, invisible to gh queries.
    C2: the shared pattern/candidate form cannot branch labels and no form field invites
    file:line grounding. Owner-ruled into B10-7 2026-08-22; C3 held for Arc 11.)'
roadmap: 'skills/reports/inbox-evolution-arc10-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-21): build-B10-7 grouping bullet (binds: D5);
  D5 (Round 4 — amendments reach the factory by the owner-applied re-triage label: `amended`
  admits a comment, intake gains one extra query leg, the amendment appends to the existing
  filing and never re-materializes; A15''s cost discipline holds — an unadmitted comment
  costs the factory nothing; the contract-text obligation ships with it; no comment-scan is
  built); roundtable A13 (the "re-applied `vault-accepted`" alternative is struck — that
  label''s defined-once meaning is the materialization trigger; contract scope explicitly
  includes the new `amended` label row and the "Seven labels" count fix); roundtable A14
  (the issue templates state the filer''s affirmative move — comment **and @mention the
  owner**; GitHub''s notification is the trigger, the label stays the owner''s admission;
  supersedes the interim honesty note that rode B10-1 — this build finds and retires that
  note); capture addendum 2026-08-22 (owner-ruled: A10-15 C1+C2 → B10-7 — the contract
  amendment additionally widens the triage verdict vocabulary and evolves the forms toward
  triage-ready filings, under its existing evolution-rule check; joint moved: none).'
risk: 'low — no governance-bundle edit (the field contract is a skill reference, not
  `_meta/`: package-lint C6 does not fire, no rule-card re-derive), no convention `version:`
  moves (no handshake bump, no Group-E consumer walk beyond the standing PASS), no workflow
  edit, no new skill (no registration), no new package-lint check (E4 untouched), not a
  release build. The risk that exists is contract-drift risk across the rail''s
  derive-surfaces (three shipped + four factory-side files edited in one build) — priced by
  the verification greps — and the public-surface scrub (issue forms and the contract are
  public bytes).'
---

# Build #B10-7 — the rail amendment channel

Arc 10's through-line names A10-8 "a deaf ear": the rail's first live exercise found its
first structural hole. The field contract's state flow
(`skills/vlt-feedback/references/field-contract.md:67-69`) runs
`vault-filed → vault-accepted → captured` (or `→ declined`) with no amendment verb, and the
factory intake (`.claude/skills/inbox-capture/references/github-intake.md:19-20`) queries
admitted-**open** issues while excluding any issue whose `origin:` token already exists
under `inbox/` — correct idempotence that makes every captured issue a write-only surface
for its filer until archival, a window that lasts arcs. Proven live: the substantive
2026-08-21 comment on issue #1 reached the factory only because the owner mentioned it
in-session. D5 ruled the cheap shape — an owner-applied `amended` label, one intake query
leg, append-never-re-materialize — and the addendum ruling folded in A10-15's C1+C2: the
same contract table and the same forms gain the queryable triage-verdict vocabulary and
triage-ready filing fields, all additive under one evolution-rule check.

The build touches **both sides of the factory/shipped seam**: the contract, the issue
forms, and the template chooser are shipped/public surface; the intake mechanics, the
triage skill, and the lifecycle map are gitignored factory surface. Both halves land in
this one build, so neither side ever describes a channel the other doesn't have.

All rejected alternatives in the parent filings and the rulings are settled — do not
re-litigate. In particular: the **comment-scan with watermark** (D5 rejected it — per-run
scan cost plus a stored watermark; no watch on amendments-going-unnoticed was adopted);
**re-applied `vault-accepted`** as the admission signal (A13 struck it — that label's
defined-once meaning is the materialization trigger, and a re-application is invisible to
the existing query shape); any **mandatory factory read of unadmitted comments** (A15's
cost discipline governs amendments too).

**`binds:` roster (from the roadmap bullet, per the standing rule): D5 — plus roundtable
A13/A14 as amendments to the bullet, and the capture addendum's owner ruling (A10-15
C1+C2 in, C3 held).** The bullet carries the roster explicitly; nothing was reconstructed.

## Brief-time dispositions

Ideation ruled the channel's shape (D5) and the fold (addendum). What follows are the
questions those rulings deliberately left open, ruled here. This brief was authored in an
autonomous run (no owner in-session); each disposition below is a clerk judgment recorded
per the headless contract, owner review welcome at build or acceptance time.

1. **The widened label set is: `amended`, `needs-info`, and a five-member
   `declined:<reason>` family** ✅ **OWNER-RULED 2026-08-23 — CONFIRMED** (with
   disposition 2), label names included — the set bootstrapped on the feedback repo
   under this ruling. (`declined:out-of-scope`, `declined:working-as-designed`,
   `declined:upstream`, `declined:superseded`, `declined:duplicate`). Derivation: the
   taxonomy is lifted verbatim from where it already operates in prose —
   `.claude/skills/issue-triage/SKILL.md:86-90` (out-of-scope / working-as-designed /
   upstream / superseded / duplicate-of-`#n`) — which is exactly A10-15 C1's complaint
   (prose invisible to `gh` queries). `duplicate` ships as a decline reason, not a
   standalone state: the filing's "duplicate (of an issue or an existing filing)" shape is
   in practice a decline with a pointer, and the closing comment still names `#n` or the
   filing path. `needs-info` is the one non-terminal addition: it marks a pending question
   to the filer while the issue **keeps** `vault-filed` (candidacy continues to cost the
   factory nothing); it is removed, or simply superseded by a verdict label, when the
   owner rules. No `amended`-equivalent exists for pre-capture issues — see disposition 5.
2. **The "Seven labels" count fix (A13) is resolved by removing the count, not
   incrementing it.** ✅ **OWNER-RULED 2026-08-23 — CONFIRMED**: the table stays the
   complete definition; only the self-counting claim goes (the lists-claim-completeness
   rule). `field-contract.md:54` becomes non-enumerative ("The labels of the
   field contract, defined once, here" or equivalent), and `config.yml:6`'s "the seven
   labels" likewise. Reasoning: this build takes the set from seven to fourteen and C1's
   own trajectory shows the set will move again — a literal count is the
   "lists that claim completeness drift" failure (CLAUDE.md standing rule; the inbox
   README already retired its own count for the same reason, `inbox/README.md:38-40`).
   The table itself remains the complete definition; only the self-counting claim goes.
3. **Label additions do not bump `rail_contract` — and the evolution rule now says so.**
   The rule at `field-contract.md:15-19` today covers payload fields only. The build adds
   the label clause: adding a label is additive (no bump); renaming a label, removing one,
   or changing a label's meaning bumps. This is A10-15's "one `rail_contract`
   evolution-rule check (label additions additive) covers the whole set" — every change in
   this build (new labels, new form files, sharpened field description, retired shared
   form) is additive under it, so `rail_contract` stays `1`. The `provenance_guess`
   sharpening (disposition 6) is a guidance sharpening, not a meaning change — the field
   remains an explicitly-marked guess the factory grounds; no bump.
4. **Amendment append mechanics — consume-on-read, decoration-free, comment-granular.**
   The intake's new leg queries `captured`+`amended` open issues; per hit it locates the
   filing by the `origin:` token (the step-3 search, unchanged, including `inbox/archive/`),
   fetches the issue's comments, appends each comment **not already recorded in the
   filing** (matched by comment timestamp+author against existing amendment headers) as a
   dated `## Amendment — <repo>#<n> comment <ISO-timestamp> (<author>)` section carrying
   the comment body verbatim, then **removes the `amended` label** (`gh issue edit
   --remove-label amended`). Consume-on-read keeps the leg idempotent with no watermark
   and no stored state (the label is the watermark; the owner re-applies it to admit a
   later comment batch). The stale-shape gate does **not** apply to amendment comments —
   comments are not payloads; the appended text is raw field signal that Capture grounds
   like any filing body. The appended amendment **joins the run's un-captured set**: the
   filing re-enters capture for its amendment section only, under whatever capture posture
   prevails (mid-arc addendum posture included).
5. **Amendments touch captured-open issues only.** An admitted comment on an issue that is
   `vault-accepted` but not yet materialized needs no channel — materialization hasn't
   happened, and the next intake run reads the issue fresh; if the comment matters before
   then, the owner can simply wait to apply `amended` until after capture. An `amended`
   label found on an issue whose `origin:` token lives only in `inbox/archive/` (the
   filing already shipped and passed acceptance, issue normally closed at archive) is
   **reported as "amendment on an archived filing — held for owner hand-handling"**, never
   auto-appended to closed history: post-archive signal is new signal, and whether it
   becomes a fresh filing is the owner's call.
6. **Triage-ready forms (C2) = per-kind split + a sharpened `provenance_guess`.** The
   shared `field-pattern-candidate.yml` is replaced by `field-pattern.yml` and
   `field-candidate.yml`, each carrying its true label pair at filing time (mirroring the
   defect form's shape, single-option `kind` dropdown) — the "cannot branch labels" caveat
   and its two contract-table parentheticals (`field-contract.md:60-61`) retire. No new
   payload field is added: rather than a separate line-refs field, the existing optional
   `provenance_guess` (contract `:31` and all three forms) has its description sharpened
   to invite `path:line` references where the filer has them, still explicitly a guess the
   factory grounds. Reasoning: the factory's archaeology is grounding, and grounding wants
   line refs in the provenance slot it already reads; a ninth field would split one
   concern across two homes.
7. **The A14 @mention is literal.** ✅ **OWNER-RULED 2026-08-23 — KEEP LITERAL for this
   release, with a named follow-up filed.** The trigger must be a real handle or the
   amendment channel's notification is a permanent no-op; the no-new-coupling argument
   was verified against the tree (the repo slug is already hardcoded at `:14` in all
   three forms, `config.yml:27`, and throughout the label bootstrap block). Residue
   accepted on record: a personal handle in the public shipped surface, and a
   single-person trigger that breaks silently if the handle changes — bounded because
   `.github/` is never part of the own-the-apply copy surface. **Follow-up filed:**
   `inbox/2026-08-23-110913-amendment-trigger-should-not-be-a-personal-handle.md` —
   move the trigger to the repo's watch/subscription (or a repo-owned target), Arc 11
   candidate. A prose "@mention the owner" notifies nobody — the
   GitHub notification A14 names as the trigger requires a real handle. The template
   sentence therefore names `@mggower` literally, which introduces no new coupling: both
   forms already hardcode the repo slug in their contract links
   (`field-defect.yml:14`, `field-pattern-candidate.yml:13`), so a repo move already
   edits these files.
8. **Interim posture (R1): not applicable.** Both halves of the channel (shipped contract
   text + factory mechanics) ship in this one build; no rule lands ahead of its mechanism.
   (The one sequencing seam — the public templates describe the channel before the next
   release publishes them — is the ordinary release cadence, not an interim posture: until
   the release, the public templates still carry the honest B10-1 interim note.)

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

## F-sites

### F1 — `skills/vlt-feedback/references/field-contract.md` — the contract gains the amendment verb, the widened vocabulary, and the label evolution clause

**Current state (re-grounded 2026-08-22, branch `arc10-v0.14.0` @ 8879869 — HOLDS as
captured):**
- `:12` — `rail_contract: 1`.
- `:15-19` — the evolution rule, payload fields only.
- `:31` — the `provenance_guess` field row ("explicitly marked as a guess; the factory
  grounds every claim before capture").
- `:52-55` — the label-set intro: "Seven labels, defined once, here."
- `:57-65` — the seven-row label table; `:60-61` carry the shared-form parentheticals
  ("The shared pattern/candidate form cannot branch labels — the `kind` field in the body
  is authoritative.").
- `:67-69` — the state flow: "`vault-filed → vault-accepted → captured`, or `vault-filed
  → declined`."

**The change:**
- `:54` — the count goes non-enumerative (disposition 2).
- The label table gains rows (applied-by / meaning, matching the existing form):
  - **`amended`** — applied by the owner, on a `captured` open issue. Admits post-capture
    comment(s): the factory intake appends them to the existing filing (never
    re-materializes — the `origin:` header stays the idempotency key) and removes this
    label; the issue stays `captured`. An unadmitted comment reaches nothing.
  - **`needs-info`** — applied by the owner at triage. A question to the filer is pending
    (asked in a comment); the issue keeps `vault-filed` (candidacy, still costing the
    factory nothing) until the owner rules.
  - **`declined:<reason>`** — applied by the owner alongside `declined`; reasons:
    `out-of-scope`, `working-as-designed`, `upstream`, `superseded`, `duplicate`. Makes
    the decline corpus machine-scopable; the closing comment still states the reason (and
    any `#n` / filing pointer) in prose.
- `:60-61` — both shared-form parentheticals retire (the forms are per-kind after F2);
  `field:pattern` / `field:candidate` rows read "template (pattern/candidate form) or
  owner triage", mirroring the defect row.
- `:67-69` — the state flow gains the amendment verb, e.g.: "`vault-filed →
  vault-accepted → captured`, or `vault-filed → declined`. On a `captured` issue, owner
  applies `amended` → the intake appends the admitted comment(s) to the existing filing
  and clears the label → still `captured`." Plus the one-sentence filer-facing truth the
  templates point at: comments reach the factory only via the `amended` admission.
- `:15-19` — the evolution rule gains the label clause (disposition 3).
- `:31` — `provenance_guess` content sharpened to invite `path:line` refs where known
  (disposition 6), still "explicitly marked as a guess".

**Why:** A10-8's contract-text obligation (D5), A13's two explicit scope items, A10-15
C1, and the evolution-rule check the addendum ruling names. This file is the single home
all six other F-sites derive from — it changes first.

### F2 — `.github/ISSUE_TEMPLATE/` — per-kind forms, the affirmative-move note, sharpened provenance

**Current state (re-grounded — HOLDS):**
- `field-defect.yml:17` and `field-pattern-candidate.yml:19` — the identical B10-1
  interim honesty sentence: "Note: comments added after an issue is labeled `captured`
  reach the factory only if the owner admits them by hand — an amendment channel is
  planned; until it ships, assume a comment on a captured issue is not read."
- `field-pattern-candidate.yml:7` — `labels: ["vault-filed"]` (cannot branch); `:14-17` —
  the cannot-branch explanation; `:41-50` — the two-option `kind` dropdown.
- `field-defect.yml:33-38` / `field-pattern-candidate.yml:35-40` — the `provenance_guess`
  textareas.
- Both files' header comments (`:1-4`) state ADDITIVE-ONLY and point at the contract.

**The change:**
- **Retire the interim note in every form (A14's "find and retire" — this is the found
  instance, both files)**, replaced by the affirmative-move sentence, e.g.: "To amend
  after an issue is labeled `captured`: add a comment with the new evidence **and
  @mention @mggower** — the notification is the trigger for a look; the owner applying
  the `amended` label is what admits the comment into the factory. An unadmitted comment
  is not read." (Exact wording the builder's; the three load-bearing elements are the
  comment, the literal @mention, and the label-as-admission.)
- **Split the shared form**: `field-pattern-candidate.yml` is deleted; `field-pattern.yml`
  (`labels: ["vault-filed", "field:pattern"]`) and `field-candidate.yml`
  (`labels: ["vault-filed", "field:candidate"]`) land, each mirroring the defect form's
  fixed single-option `kind` dropdown and per-kind `description:` text, all eight payload
  field ids unchanged and in contract order. Header comments carry the same
  ADDITIVE-ONLY + single-source-of-truth text.
- All three forms' `provenance_guess` descriptions sharpened per disposition 6 (invite
  `path:line` refs; still a guess).

**Why:** A14 (supersession of the interim note), A10-15 C2 (triage-ready filings,
labels-true-at-filing). Out-of-scope, per-site: no new payload field (disposition 6); the
forms' repo-slug hardcoding stands as-is (pre-existing, disposition 7).

### F3 — `.github/ISSUE_TEMPLATE/config.yml` — the label bootstrap block

**Current state (re-grounded — HOLDS):** `:5-15` — "the seven labels of the field
contract" comment + seven idempotent `gh label create --force` lines.

**The change:** the count wording goes non-enumerative (disposition 2); seven new
`gh label create` lines land (colors builder's choice, descriptions in the existing
"Field contract: …" style): `amended`, `needs-info`, `declined:out-of-scope`,
`declined:working-as-designed`, `declined:upstream`, `declined:superseded`,
`declined:duplicate`. The block stays a run-once-before-the-release-tag owner bootstrap,
idempotent via `--force`.

**Why:** the labels must exist on the tracker before any form or triage run can apply
them; this block is where the roster is provisioned (its only home — the contract defines
meaning, this file provisions).

### F4 — `.claude/skills/inbox-capture/references/github-intake.md` (+ one clause in `SKILL.md`) — the amendment leg (factory side)

**Current state (re-grounded — HOLDS):** steps 1–5 at `:16-83` (query `:19-20` is
`--label vault-accepted --state open`; idempotence exclusion `:44-55`; materialize
`:57-71`; transition `:72-83`); "What this file does not own" `:85-95`.
`.claude/skills/inbox-capture/SKILL.md:52-60` — the Discovery paragraph's step list
"(query, stale-shape gate, idempotence exclusion, materialization, `captured` transition
— the mechanics live there)".

**The change:** a new numbered step (natural slot: after step 5, e.g. "## 6. Amendment
leg") carrying disposition 4's mechanics verbatim in this file's cite-the-contract style:
the `--label captured --label amended --state open` query, locate-by-`origin:`-token
(step 3's search, reused, decoration-tolerant, `inbox/archive/` included), the
comment-granular dated append shape, consume-on-read label removal, the
no-stale-shape-gate note, the appended-amendment-joins-this-run's-un-captured-set rule,
and the archived-filing hold (disposition 5). The label's meaning is cited to the
contract's new row, never restated. `SKILL.md`'s step-list parenthetical widens by one
item ("amendment leg"). The "What this file does not own" section gains the owner half:
applying `amended` is an owner triage verb, performed on GitHub — the intake only
consumes it.

**Why:** D5's mechanics half. This is the gitignored side of the seam — shipped into no
vault, but the channel does not exist until it lands.

### F5 — `.claude/skills/issue-triage/SKILL.md` — the A13 residue, the verdict label ops, the retired arc-work sentence

**Current state (re-grounded — grounding addition; the capture predates these exact
lines):**
- `:52-55` — the amendment sweep still says "the Arc 10 D5 ruling: `amended`, or
  re-applied `vault-accepted`" — **stale against A13**, which struck the second
  alternative; and "The admit-path mechanics belong to build B10-7 — when it ships, its
  rules govern; until then this sweep just makes admitted comments visible."
- `:81-82` — "Only the contract's label set exists (`field-contract.md:54-69`); this
  skill widens nothing."
- `:86-90` — decline: reasons "in comment prose, not labels", ending "Widening the label
  vocabulary would be a contract change — arc-roadmap work, not this skill's."
- `:91-93` — hold: "no label change … optionally a drafted question comment".

**The change:**
- `:52-55` — drop "or re-applied `vault-accepted`" and the until-then clause; the sweep
  now surfaces `captured`+`amended` issues and routes them: consumption is the intake's
  (`github-intake.md`'s new leg), cited not restated.
- `:86-90` — decline's label ops become `--add-label declined --add-label
  "declined:<reason>"` with the reason set cited to the contract table; the prose reason
  in the closing comment stays (labels scope, prose explains). The "arc-roadmap work"
  sentence retires — this build is that work.
- `:91-93` — hold: when a question comment is drafted, the drafted ops include
  `--add-label needs-info` (issue keeps `vault-filed`); a plain hold stays label-free.
- `:81-82` stays true by construction (the skill still widens nothing — the contract
  widened).
- The batch-gate and apply sections (`:94-108`) need no structural change — label
  operations were always part of the rendered exact ops.

**Why:** A10-15 C1's consumer, and the A13 strike landing everywhere the struck
alternative was written down.

### F6 — `.claude/skills/vlt-lifecycle.md` — the map learns the amendment observable

**Current state (re-grounded — grounding addition):** `:33` — the one rail row
("An open `vault-filed` issue … carries neither `vault-accepted` nor `captured`" →
`issue-triage`); `:47-49` — "The untriaged-rail row is the table's **one off-disk
observable** — it needs `gh`."

**The change:** one new row after `:33`: "An open `captured` issue on the transport repo
carries `amended` (via `gh`) | Admitted amendment pending | run `inbox-capture` (the
amendment leg consumes it)". The `:47` note pluralizes ("the rail rows are the table's
off-disk observables — they need `gh`"), unknown-state degrade wording unchanged.

**Why:** the map claims derive-first first-match completeness over lifecycle positions;
an admitted-but-unconsumed amendment is a new observable position, and leaving it out
recreates A10-8 one layer up (an admission the routing table never routes).

## Registration

**None.** No new skill (no `marketplace.json` `skills[]` entry, no `module-help.csv`
row), no new workflow, no convention `version:` bump (the field contract carries no
handshake by design — it is single-home + derive, like the operating contract), so no
consumer re-ack walk. "No bump owed" pricing: **C6 not fired** (no `_meta/` governance
edit — the field contract lives in `skills/vlt-feedback/references/`, outside the
rule-card derivation); **E4 not fired** (no new package-lint check); **E5 untouched**
(no asset-header ack changes). The build's real "consumer walk" is informal: the seven
derive-surfaces of the rail (contract, three forms, chooser, intake, triage skill,
lifecycle map) walked in one build — priced in Verification.

## Out of scope (dispositioned)

- **A10-15 C3 (public-voice rule single-homing)** — held for Arc 11 by the same owner
  ruling that folded C1+C2 in (capture addendum, 2026-08-22).
- **The comment-scan / watermark alternative** — rejected by D5; not softened here. No
  watch on amendments-going-unnoticed was adopted (D5's closing line).
- **When a captured issue's comment window ends** (close-at-archive shuts the thread
  silently) — Carson's roundtable out-of-scope item, owed its own `inbox/` filing; not
  this build's.
- **A vault-side amend mode in `vlt-feedback`** (the skill composing/scrubbing an
  amendment comment) — not ruled anywhere; the filer's move is the template-stated
  comment + @mention, and A15's cost discipline argues against new mandatory machinery.
  Deliberately not built; a field filing can propose it.
- **Amendments on closed/archived issues** — held for owner hand-handling (disposition
  5), not a channel.
- **A `rail_contract` bump** — none owed: every change is additive under the evolution
  rule this build itself extends to labels (disposition 3).
- **Comments landing between `vault-accepted` and materialization** — no channel needed
  (disposition 5); materialization-time comment reading stays unbuilt.
- **`arc-closeout` Stage 5** (`closeout-checklist.md:116-129`, close-at-archive) —
  untouched: `amended` on an archived filing is F4's hold-for-hand-handling report, and
  the close mechanics don't change.

## Verification (unit, at rest — lifecycle step 6)

1. **Contract-coherence greps.** No "Seven labels"/"seven labels" anywhere
   (`grep -rn "even labels" skills/ .github/ .claude/skills/` → 0); the struck A13
   alternative is gone (`grep -rn "re-applied .vault-accepted" .claude/skills/` → 0); the
   B10-1 interim note is gone from both/all forms
   (`grep -rn "amendment channel is planned" .github/` → 0) and the affirmative-move
   sentence with the literal `@mggower` is present in all three forms; `amended`,
   `needs-info`, and all five `declined:` reasons each appear in exactly the expected
   homes (contract table, config.yml bootstrap, issue-triage verdict ops, intake leg —
   and nowhere restated with divergent meaning).
2. **Form validity + shape.** All three form files parse as YAML
   (`uv run python -c "import yaml,glob; [yaml.safe_load(open(f)) for f in glob.glob('.github/ISSUE_TEMPLATE/*.yml')]"`);
   `field-pattern-candidate.yml` absent; each form's field `id:` list equals the
   contract's eight ids in order; each form's `labels:` carries `vault-filed` + its true
   `field:*` label; each `kind` dropdown is single-option and matches its form.
3. **Both-sides seam check.** The shipped half never points into `.claude/`
   (`grep -rn "\.claude/" skills/vlt-feedback/ .github/` → 0 new hits), and the factory
   half cites the contract for every shape (spot-read F4/F5 edits: label meanings cited,
   not restated).
4. **State-flow desk-check (six cases).** Walk the contract's flow text + F4's leg
   against: (a) comment on captured issue, no label → intake blind, zero cost (A15
   holds); (b) owner applies `amended` → next run appends dated section, removes label,
   issue stays `captured`; (c) `amended` re-applied after a later comment → only the new
   comment appends (timestamp match); (d) `amended` on an issue whose origin token is in
   `inbox/archive/` only → reported held, nothing appended; (e) decline verdict → ops
   render `declined` + one `declined:<reason>` + comment-first ordering (issue-triage
   apply order unchanged); (f) hold-with-question → `needs-info` drafted, `vault-filed`
   retained. Record the six verdicts in the BUILT status.
5. **Packaging lint** — `uv run tools/package-lint.py` groups **A/B/C/E** PASS (D /
   `--expect-version` is the release gate, not this build's). Handshake: no `version:`
   moved, no `consumers:` changed — Group E PASS unchanged is the check of record.
6. **Scrub** — the changed shipped files (`field-contract.md`, three forms, `config.yml`)
   carry no personal or vault-local content beyond the pre-existing public repo slug and
   owner handle (public by construction); worked shapes use placeholder paths
   (`<repo>#<n>`, `{date}-{slug}` style).
7. **R3: not applicable** — no lint/dispatch finding class is added or changed (intake
   and triage report entries are run-report rows, not finding classes with legal-response
   homes).
8. **R4: not applicable** — no file joins any vital- or manifest-enumerated class: the
   new form files live in `.github/` (outside the own-the-apply copy surface and every
   vault enumeration; verified — nothing in `skills/` or `tools/` enumerates
   `ISSUE_TEMPLATE` contents), and the factory-side edits are gitignored.
9. **No `.decision-log.md`** left in the working tree at finish.

Not a release build — no version bump here; the bump rides its cut's release build.

## Acceptance (live — appended to the roadmap ledger)

**(1) `[ship-verifiable]`** — the rail's text agrees with itself across all seven
derive-surfaces: the contract carries the `amended`/`needs-info`/`declined:<reason>` rows,
the amendment verb in the state flow, the label-additions-additive evolution clause, and
no label count; the three per-kind forms parse, carry true labels, contract-ordered ids,
the sharpened `provenance_guess`, and the A14 affirmative-move sentence with the B10-1
interim note gone; `config.yml`'s bootstrap block provisions the full roster
non-enumeratively; the factory intake carries the consume-on-read amendment leg; the
triage skill is A13-clean with labeled verdict ops; the lifecycle map routes the
amendment observable. Discharged at rest by the brief's verification greps + six-case
desk-check, recorded in the BUILT status.

**(2) `[ship-verifiable]`** — the tracker matches the contract at release: the owner runs
the (idempotent) bootstrap block before the release tag and `gh label list` shows all
fourteen labels; after the release push, the issue chooser at
`github.com/mggower/bmad-module-vlt/issues/new/choose` offers the three per-kind forms
(the shared form gone) and a test-render of each shows the affirmative-move note.
Performer: the owner; bounded by the release that ships this build (an event already
scheduled).

**(3) `[field-contingent]`** — the first live amendment cycle closes the deaf ear;
discharging event named: **the owner applies `amended` to a captured open issue carrying
an un-folded comment, then runs the next `inbox-capture`** (performer: the owner + the
factory clerk; venue: the public tracker + this repo — no vault read needed; the tracker's
open issues #1–#7 make a qualifying comment a natural near-term event, and the owner can
legally seed one). Pass = the comment appends to the origin filing as a dated amendment
section verbatim, the `amended` label is removed in the same run, the issue stays
`captured` with no re-materialization (no second `origin:` file), and the appended
section joins that run's un-captured set for grounding. Fail = a re-materialized
duplicate, an append the run never grounds, a label left standing (the leg re-firing
forever), or a comment reaching the factory with no label (the A15 cost discipline
broken in the other direction).

**(4) `[field-contingent]`** — the widened verdict vocabulary is used and queryable;
discharging event named: **the next `issue-triage` batch containing at least one
non-accept verdict** (performer: the owner at the batch gate; venue: the public tracker —
untriaged signal arrives on its own cadence, or the owner's own next factory-observed
filing routes via the rail). Pass = a decline lands as `declined` + exactly one
`declined:<reason>` label with the prose reason still in the closing comment (and
`gh issue list --label "declined:<reason>" --state closed` finds it), and/or a
hold-with-question lands `needs-info` with `vault-filed` retained. Fail = a decline
reason existing only in prose again, a `declined:` label with no terminal `declined`, or
`needs-info` displacing `vault-filed`.
