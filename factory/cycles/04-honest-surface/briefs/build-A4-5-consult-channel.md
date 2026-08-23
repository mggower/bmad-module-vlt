---
title: 'Build A4-5 — the consult channel (the bus grows its synchronous mode, and the rule that makes it exercised by construction)'
status: 'BUILT 2026-07-26 — all eight F-sites landed: consult.md (new, `checked` on day one, no deferral), vlt-consult.js (new engine), vlt-dispatch''s `consult` mode + six-site arity, vlt-lint''s `consult_missing` check + `authority_scan:` denominator, the contract''s pointer/sitting/timings clauses, spec.md''s version-free Reading-list pointer, and both vlt-setup install enumerations. Verification 1–12 + 14(partial: D pending) + 15 PASS; check 13 PARTIAL for the pre-existing reason only (3 unparseable template lines, all present byte-identical at HEAD, both new keys parse clean — not a regression). Check 9 ran the real engine four times against a temp fixture: `answer` (schema-valid, partner''s own voice), degraded structured note on an unreadable partner (no invented answer), `insufficient-context` on a thin payload (explicitly refused to guess, named three missing items), and `wrong-partner` (empty answer, routed back). `agent_count: 1` on every run — depth-1 held structurally. Check 11 B1: all four findings confirmed by reading; vlt-upgrade untouched. RELEASE NOT RUN — the dual bump, `--expect-version 0.8.0` gate, commit, ff-merge, tag and push are held for the owner via `vlt-release`; the tree is dirty and uncommitted. Deviations/notes: (1) the engine payload gained `partnersPath` and `today` beyond F4''s named arg list — F4''s own prompt spec requires reading the summoned partner''s `identity.md`/`thread.md` and dating a `thread.md` write, which is unreachable without a `{partners}` path, and workflow scripts may not call `Date`; both are optional-guarded and the required-field guard is exactly F4''s four. (2) `vlt-dispatch:17`''s "same machine" claim was kept as ruled but made honest with one parenthetical — the sentence literally asserts every mode emits `- [ ]` drained by the pickup loop, which is false for a pre-checked consult; the claim survives, its overreach does not. (3) The trigger-rule sentence was NOT reproduced in `consult.md` or `vlt-dispatch`, though F1 item 2 quotes it verbatim while calling it pointed-at — verification check 10 requires it appear once in shipped source, and check 10 won; both sites now point without quoting. (4) `vlt-lint` appends `consult@1` at the end of `depends_on:` where `vlt-dispatch` puts it first — position is not semantic; this minimizes diff churn.'
module_code: 'vlt'
created: '2026-07-26'
derives_from:
  - 'inbox/2026-07-25-132141-partner-consult-synchronous-channel.md (A3-22 — the whole filing: the `consult` mode, the governance pairing, the five named risks. Its two zero-machinery prose items shipped in A4-1 and are NOT re-shipped here.)'
roadmap: 'skills/reports/inbox-evolution-arc4-roadmap.md'
rulings: 'Arc-3 roadmap §Ideation rulings — A3-18..A3-23 (2026-07-25): A3-22 → A4-5, one filing, last in ship order; ODQ #8 → NOT WITHOUT THE PAIRING (a handshaked `{conventions}/consult.md` + a `vlt-lint` check ship in the same build; a brief may sequence convention-then-mechanism but may not ship the mode with the pairing merely "planned"); ODQ #9 → the two prose items shipped independently and sooner (A4-1, done); B1 upgrade-preserve-path → ATTACHED precondition; the four-site registration surface is named, not discovered; `dialogue`/`convene`/`summon` deferred by the filing and not reopened.'
risk: 'moderate — the arc''s largest build: a new dispatch mode, a new workflow asset, a NEW handshaked convention (`consult@1`, two consumers acking in-build), a new lint check, and the release. It bumps no existing convention `version:` and triggers no re-ack of any existing handshake; the only consumer walk is the new convention''s own two acks. The `dispatch.md` shape change is the B1 preserve-path precondition, discharged in F3.'
---

# Build A4-5 — the consult channel

## Intent

Arc 4's last build makes real a sentence the module already ships. A4-1 landed the contract's
authority boundary — *a partner never speaks in another partner's voice; **it consults**, or it
cites* (`vault-operating-contract.md:226`) — together with read-and-cite as the documented default
and its trigger rule, *spawn another partner only when the interaction should be remembered*
(`:228`). Both are live prose today naming a mechanism the vault does not have: there is no way for
one partner to consult another. `vlt-dispatch`'s three modes are all write-and-wait, and
`vlt-review-council` is a panel of fixed lenses, not a partner answering as itself. The field
consequence (A3-22, filed from `vlt-sayari`) is the failure the prose forbids: the caller guesses,
or a human hand-carries the question between two sessions.

This build adds the **fourth channel of the same bus** — `vlt-dispatch consult`: synchronous,
depth-1, the summoned partner answering as itself and remembering that it did — **plus** the
governance pairing that ideation ruled inseparable from it (ODQ #8): a handshaked
`{conventions}/consult.md` declaring artifact preconditions, and a `vlt-lint` check that catches an
artifact claiming out-of-authority domain with no consult record. The pairing is not decoration. It
is the arc's answer to the shipped-but-unexercised scar the whole roadmap is built around: **a
required consult is exercised by construction**, so this convention is the first the module has
shipped at `enforcement_stage: checked` on the day it lands, rather than `declared` with a
tripwired deferral.

Closes A3-22 (Arc-3 roadmap `:1543-1622`, GAP CONFIRMED, the batch's only *candidate*).

**All rejected alternatives in the parent filing are settled — do not re-litigate.** `dialogue`
(A↔B for N turns), `convene` (true party-mode) and `summon` (the answer goes to the human, caller
overhears) are deferred by the filing and were not reopened at ideation; the first two are later
*compositions* of this primitive and the third reduces to running the other partner's skill
directly. The naive reading of `vlt-dispatch:21` ("`identity.md`/`thread.md` are per-partner and
off-limits") does **not** block a stateful consult — capture verified the rebuttal (`:1562-1568`):
`:21` forbids a partner *pushing into another's* memory, and in a consult the summoned partner is
the one running, so it writes its own, exactly as the drain loop already prescribes at `:225`.
Single-writer holds. Do not re-derive this at build time; it is settled.

**Evidence debt, binding on the writing.** vlt-sayari was **not** read during grounding (ruled NOT
BLOCKING). The Navigator/Engineer friction is taken as filed. No F-site and no acceptance check
below may assert anything about vlt-sayari's live state.

## Brief-time dispositions

Ideation left A4-5 three questions (Arc-3 roadmap `:2869-2871`): the payload shape, the
convention's preconditions, and the five named risks (the fifth — B1 durability — is a
precondition, not a question; it is discharged in F3). Each is ruled here. Rulings 1–3 answer the
named questions; 4–10 are the calls the brief must make to write the F-sites, each bounded to
mechanism and none reopening a ruling.

**1. The engine is a workflow asset, not prose in the SKILL.** `skills/vlt-setup/assets/workflows/vlt-consult.js`,
installed to `{project-root}/.claude/workflows/` — the SKILL's `consult` section is the
conversational front that resolves the payload and invokes it. This is not a new pattern: it is the
module's own doctrine, stated at `vlt-review-council/SKILL.md:51` — *"**Re-implement the panel in
prose** — the workflow is the one engine; this SKILL invokes it, it does not hand-spawn lenses."*
Two things follow that prose cannot deliver: the **typed return union is enforced** (a JSON schema
on the `agent()` call, the same mechanism as `vlt-review-council.js:92-103`'s `VERDICT`), so
`insufficient-context` is a first-class return the model cannot prose its way around; and
**depth-1 is structural** — the workflow spawns exactly one agent, and a spawned agent cannot
re-enter it (`workflow()` nesting is one level and the summoned partner is not running a workflow
at all). Rejected: a prose "spawn the partner via the Agent tool" instruction in the SKILL — it
re-implements the engine in prose, cannot force the union, and makes depth-1 an honor system,
which is precisely the confabulated-authority risk.

**2. The payload — fat, and it carries the caller's boundary.** Required fields, mirroring
`vlt-review-council.js:20-28`'s `subject` idiom (which capture already named as the pattern to
copy, `:1575-1577`, correcting the filing's line to `vlt-review-council/SKILL.md:35`):
`from-slug`, `to-slug`, `question`, and **`groundIn`** — the **live absolute paths** the summoned
partner must read (never a plugin-cache copy; the council learned this the hard way,
`vlt-review-council.js:22-23`). Plus `why` — one line naming *what the caller is trying to finish*
and *which part of it is outside its authority*. `why` is the anti-confabulation field: it is what
lets the summoned partner return `wrong-partner` or `insufficient-context` accurately instead of
producing a plausible opinion about a question it was never really asked.

**3. The convention's precondition is bounded to `{specs}` artifacts.** `{conventions}/consult.md`
declares: **a spec whose `consumers:` name a partner other than its `owner` — i.e. a contract one
partner writes to bind another's domain — requires a consult record for each such consumer before
it is filed.** Rationale for the bound, and it is load-bearing: "claims out-of-authority domain" is
not mechanically detectable in general prose, but a spec already carries a **machine-readable
authority axis** — `owner` (one partner slug) and `consumers` (partner slugs), both in
`{conventions}/spec.md:45-46`. Bounding v1 to `{specs}` gives the check a real denominator and a
real finding instead of a heuristic that fires on wiki prose. The honest limit goes **in the rule
itself** (A4-4's precedent, `vault-operating-contract.md:268`): a partner claiming another's domain
in an ordinary wiki page or session note is **invisible to this check by construction** — the rule
reduces the class, it does not close it. Rejected: widening to any agent-zone artifact (no
authority axis to derive from → an unimplementable check, which is how a convention ends up
`declared` forever — the scar this build exists to answer).

**4. The consult record is derived, not stored.** The record **is** the dated `consult:` block in
`_agent/dispatch.md`; the artifact cites it. No new frontmatter key on specs, no `consulted:`
field, no counter. This mirrors the deferred `spec_notification_missing` check exactly
(`{conventions}/spec.md:81` — "a `version` bump with no matching relay entries in the dispatch
record") and keeps derive-first unbent for the fifth build running. The lint check greps the
dispatch record for a `consult:` block naming the `(spec-path, consumer-slug)` pair. Applied
consciously: this is a derivation from a **record**, not from the residue of the process being
checked — the boundary clause at `vault-operating-contract.md:256` is satisfied, because the
consult block is *written by the consult*, an event, not inferred from its leavings.

**5. Rejected: a spec.md `version:` bump.** The precondition is stated **once**, in `consult.md`;
`{conventions}/spec.md` gains a **Reading list pointer only** (F8) — a version-free pointer, per
`tools/package-lint.py:322-348` E3, which fails any `name@version` token outside `depends_on:`.
Reasoning: the obligation is consult.md's to own, and a `1 → 2` bump on `spec.md` would drag a
**four-consumer re-ack** (`vlt-mint`, `vlt-dispatch`, `vlt-upgrade`, `vlt-lint` —
`{conventions}/spec.md:12`) one build after A4-3 already paid that price on `wiki-supersession`.
CLAUDE.md's handshake rule is explicit that prose clarifications don't bump; a pointer is the
thinnest possible prose clarification. Flagged for the builder: if the pointer as written reads as
*imposing* a rule rather than *pointing at* one, rewrite the pointer — do not bump the version.

**6. A consult is NOT a hand-off, and it does not move the wheel.** The contract's sitting unit
(`vault-operating-contract.md:213`) says a hand-off *"ends one sitting and begins another"* — so
left unstated, every consult would fork a second session note and the caller would lose the wheel
mid-thought, which is the exact friction the filing reports. Ruled: **no work transfers in a
consult, so no sitting boundary is crossed** — the caller keeps the wheel and owns the single
session note; the summoned partner writes **no** session note and no `{log}` session entry. This is
one clause in the contract's *Sessions, sittings, and hand-offs* (F7), where the sitting unit is
single-homed. It also supplies the cleanest statement of what the mode is: the filing's own framing,
*a consult is a `relay` whose drain happens immediately, in-process, with the answer returned to the
caller instead of left on the board*.

**7. The `{log}` line keeps ONE partner tag — the caller.** The filing proposes a line "tagged with
**both** partners (novel: every existing log line has a single author)". Ruled **against**, and the
deviation is deliberate: `vault-operating-contract.md:125` defines `(<partner>)` as *the active
partner for the operation*, and in a consult that is unambiguously the caller — the summoned partner
is not at the wheel (disposition 6). A dual tag would change the contract's canonical log format
and break its own published grep patterns (`:142`, `grep "^## \[.*(researcher)"`). The consulted
partner is named in the **summary**, which is greppable and loses nothing:
`## [YYYY-MM-DD HH:MM] dispatch (<from-slug>) | consult: <from> → <to> — <question gist> → <return-type>`.
Attribution of the *answer* does not live in the log anyway — it lives in the attributed block
(disposition 8) and in the dispatch consult record, both of which name both partners. Recorded as a
deviation from the filing because the filing flagged the dual tag as novel; novel was a flag, not a
mandate.

**8. The raw answer is surfaced verbatim, attributed, in its own block — before the caller uses
it.** Adopted from the filing unchanged. This is the human-out-of-the-loop mitigation: two agents
converging on consensus is visible only if the human sees what the second one actually said, not a
digest of it. The caller's own use of the answer comes **after** the block, in the caller's voice.
A digested partner voice is an unattributed claim — which is what `vault-operating-contract.md:226`
already forbids.

**9. `thread.md` is written only when the consult changed the summoned partner's stance.** Adopted
from the filing (its `thread.md`-rot mitigation), and consistent with the contract's own framing of
`## Thread` as prunable attention that is *supposed to fade* (`:190`). An unbounded append per
consult would rot the one file the contract says must stay light. The summoned partner writes its
**own** memory (single-writer holds — `vlt-dispatch:21`, `:225`); the caller never writes it.

**10. Boundary erosion — read-only except its own memory; `needs-work` exits through `relay`.**
Adopted from the filing. *Consult answers; relay assigns.* The summoned partner may read anything it
is entitled to read and write **only** its own `thread.md` (per 9); if the answer implies work, the
typed return is `needs-work` and the caller fires the existing async `relay` path. This keeps two
writers out of one turn — the invariant `vlt-dispatch:21` exists to protect.

## F1 — NEW: `skills/vlt-setup/assets/governance/_meta/conventions/consult.md`

**Current state.** The conventions directory holds seven files —
`extraction.md`, `frontmatter.md`, `spec.md`, `wiki-consolidation.md`, `wiki-index.md`,
`wiki-supersession.md`, `write-verification.md`. There is no consult convention; the word
"consult" appears in shipped governance only at `vault-operating-contract.md:226` (A4-1's
prohibition) and `:228` (read-and-cite), both naming a mechanism that does not exist.

**The exact change.** Add `consult.md`, modelled on `spec.md`'s shape (frontmatter → overlay note →
class definition → rules → Enforcement → Reading list). Frontmatter, per
`{conventions}/frontmatter.md:223-242`:

```yaml
version: 1
consumers: [vlt-dispatch, vlt-lint]
enforcement_stage: checked
enforcement_checked_by: vlt-lint
enforcement_moment: lint run
adoption_first_instance: null        # no first live instance yet — declared, not yet adopted
```

**`enforcement_stage: checked`, and therefore NO deferral block.** A `checked` stage requires a
mechanical check plus a named owner and moment (`frontmatter.md:240`) — F6 is the check, `vlt-lint`
the owner, the lint run the moment. All three exist on the day this ships, so `deferral_metric` /
`deferral_threshold` / `review_after` are **absent by correctness**, not omission: a deferral
declares machinery that hasn't landed, and this build lands it. (`vlt-lint:80`'s
`declared_untripwired` finding fires on `declared` without a deferral — not on `checked`.)
`adoption_first_instance: null` is honest and is the third value A4-2's `convention_adoption:`
reporting already renders (*declared, no first instance yet*).

Body content — the rules, each stated once:

1. **What a consult is.** A synchronous, depth-1, cross-partner question in which the summoned
   partner answers **as itself** and remembers that it did. Distinguish it from the three
   neighbours the vault already has, by their real difference: a **relay** routes and waits (the
   answer lands on the board later); a **hand-off** transfers the work and the wheel (a new sitting
   — `vault-operating-contract.md:213`); a **council** is fixed lenses in parallel with no
   cross-talk, returning a verdict, not a partner (`vlt-review-council/SKILL.md:10`, `:41`). A
   consult transfers **nothing** — the caller keeps the wheel and gets an attributed answer back.
2. **The trigger rule, pointed at, not restated:** *spawn another partner only when the interaction
   should be remembered* — single-homed at `vault-operating-contract.md:228`. Read-and-cite remains
   the documented default; a consult is the exception that must earn itself.
3. **The precondition (the rule this convention exists to declare).** A `{specs}` artifact whose
   `consumers:` name a partner other than its `owner` requires a **consult record** for each such
   consumer **before it is filed**. A spec written to bind another partner's domain without ever
   asking that partner is exactly the manufactured authority `vault-operating-contract.md:226`
   forbids, in durable form.
4. **What a consult record is** — a dated `consult:` block in `_agent/dispatch.md` naming
   `(from-slug, to-slug)`, the artifact path it grounded in, and the typed return. Derived, never
   stored (disposition 4): no frontmatter key, no counter. The mechanics of *how* the block is
   written are `vlt-dispatch`'s single home — **point at them, do not restate them.**
5. **The honest limit, stated in the rule itself** (A4-4's precedent at
   `vault-operating-contract.md:268`): the precondition is bounded to `{specs}`, so a partner
   claiming another's domain in an ordinary wiki page, research note or session note is
   **invisible to this rule and its check by construction**. The rule reduces the class; it does
   not close it.
6. **Overlay note** — copy `spec.md:22`'s verbatim shape (pristine base, local additions in
   `{overlays}/consult.overlay.md`, append-only).
7. **Reading list** — `vault-operating-contract.md` (the authority boundary and the trigger rule
   this convention operationalizes), `spec.md` (the artifact class the precondition applies to),
   `frontmatter.md` (the enforcement declaration). **Version-free pointers only** — a `consult@1`
   or `spec@1` token outside a `depends_on:` fails `package-lint` E3 (`tools/package-lint.py:322-348`).

**Why.** ODQ #8, RULED: the mechanism does not ship unaccompanied by its governance pairing. This
is that pairing's declarative half.

**Named tension, resolved and recorded.** A4-2 and A4-4 each **rejected** a new convention file
(`reporting.md`, `source-fidelity.md`) as *a fifth declared-and-unexercised surface*. A4-5 ships one
anyway, and the difference is exactly the thing those builds were protecting: those rules had no
check and would have landed `declared`; this one lands `checked`, with its check in the same build,
by ruling. If the builder finds itself writing a deferral block into this file, that is the signal
the pairing has come apart — stop, and re-read ODQ #8.

## F2 — `skills/vlt-setup/SKILL.md:144` (grounding addition — the enumerated governance copy list)

**Current state.** `:144` enumerates the shipped governance files by name:
*"For each of: `_meta/vault-operating-contract.md`,
`_meta/conventions/{frontmatter,wiki-index,wiki-supersession,wiki-consolidation,extraction,spec,write-verification}.md`,
`_meta/personas/{architect,skeptic,pragmatist,historian,moderator}.md` — if the file already exists
in the vault, **skip it** … otherwise copy it in."*

**The exact change.** Add `consult` to the brace list. Nothing else on the install path needs
touching: the `.baseline/` stash at `:147` is generic ("copy each **shipped** convention"), and the
skill-asset manifest at `:149` is computed from the shipped tree.

**Why.** A grounding addition the capture did not name — this is a **completeness list that drifts**
(CLAUDE.md standing rule), and it is the only site where a new convention file must be hand-registered.
Missed, `consult.md` ships in the repo and never reaches a vault, and every acceptance check below
fails silently in the field while every at-rest check passes.

**Out of scope at this site.** Do not convert the enumeration to a glob. It is a real
completeness-list hazard, but rewriting setup's install semantics is not this build's remit; file
it if it bites again.

## F3 — `skills/vlt-dispatch/SKILL.md` — the `consult` mode (the mechanism)

**Current state (all sites re-verified 2026-07-26; the file is byte-unchanged since build-15
`3795d86`, so every A3-22 capture citation holds exactly):**

- `:11` — *"It is **one record with a drain** (`_agent/dispatch.md`) read through **three modes**"*;
  modes at `:13-15`.
- `:17` — *"All three modes are **the same machine**: every mode emits the **identical pointer
  line** … drained by the **identical grep-and-check loop**."*
- `:21` — *"the Librarian never *pushes* into another partner's private memory
  (`identity.md`/`thread.md` are per-partner and off-limits)"* + *"**Two writers, cleanly
  separated**"*.
- `:49-63` — **Mode dispatch**; `:53` resolves an explicit subcommand, `:54-61` the bare-invocation
  menu.
- `:73` — the `daily` watermark reader: *"relay blocks carry no watermark and are ignored here"*.
- `:146-197` — the `relay` mode (the structural sibling to copy: who-fires, inputs/validation,
  idempotency, block format, report).
- `:207-208` — `ledger`'s open-item greps (`grep -c '^- \[ \]'`, `grep -cF '[ ] \`<slug>\`'`).
- `:219-228` — the pickup loop, single-homed here.
- `:230-239` — the per-mode `{log}` lines; `:241-260` — the per-mode `Verify` block.

**The exact change — a new `## Mode: `consult`` section**, placed after `relay` and before
`ledger` (the write modes together; `ledger` stays the read-only closer). Sections, mirroring
`relay`'s anatomy:

- **What it is.** *A consult is a `relay` whose drain happens immediately, in-process, with the
  answer returned to the caller instead of left on the board.* Synchronous, **depth-1 hard** — a
  summoned partner answers or refuses-and-names; **it never summons**. Read-only except its own
  memory (disposition 10). *Consult answers; relay assigns.*
- **Who fires it.** A partner mid-turn, when it needs another's domain **to finish its current
  move** and the interaction should be remembered (the trigger rule —
  `vault-operating-contract.md:228`, pointed at, not restated). A human may invoke it directly for
  debugging, exactly as `relay` allows at `:156`. **Never unprompted** — dispatch's standing rule
  at `:45` holds for this mode too: there is no background consult.
- **Inputs and validation.** `from-slug`, `to-slug`, `question`, `groundIn` (live absolute paths),
  `why` (disposition 2). **Liveness (light)** — same as relay `:162`: confirm `to-slug` matches a
  live `vlt-agent-{to-slug}`; if not, say so and stop, never spawn. **`from-slug ≠ to-slug`** — a
  partner does not consult itself. **Secret hygiene** — same as every other mode (`:47`, `:163`).
- **Invoke the engine.** Call `workflow('vlt-consult', { fromSlug, toSlug, question, groundIn, why,
  skillsPath })` (F4). The SKILL **does not hand-spawn the partner** — the same single-engine
  discipline `vlt-review-council/SKILL.md:51` states for the panel.
- **The typed return union** — `answer` | `insufficient-context` | `wrong-partner` (with a
  `→ slug`) | `needs-human` | `needs-work`. State plainly that **`insufficient-context` is a
  first-class, praised return**: a thin payload producing an invented opinion is strictly worse than
  no mechanism, because read-and-cite cannot impersonate.
- **Surface the answer raw, attributed, in its own block** (disposition 8), then the caller's use of
  it, in the caller's own voice.
- **Route the return.** `needs-work` → the caller fires the existing `relay` path with the handoff
  doc it writes; `wrong-partner` → the caller may consult the named slug (still depth-1 from the
  caller — this is a second consult by the *caller*, never a chained one by the summoned partner);
  `needs-human` → surface and stop.
- **Write the consult block.** Append to `_agent/dispatch.md`. The header shape **is the mode
  signal** (as `daily/…` and `relay:` are at `:109` and `:182`):

  ```
  ## [YYYY-MM-DD HH:MM] consult: <from-slug> → <to-slug> — <return-type>
  - [x] `to-slug` Partner Name — <question gist> → <artifact or path grounded in> ✓ answered YYYY-MM-DD
  ```

  **Written pre-checked (`- [x]`)** — a consult never waited, so it is traffic, not a queue item
  (the filing's own reading, adopted). State that consequence explicitly at this site: a consult
  block **never** appears in the `ledger` board and never in a partner's open slice, **by
  construction** — the greps at `:207-208` count `- [ ]` only.
- **The trail, and its bound.** Three sites, and only three: the pre-checked block above; one
  `{log}` line tagged with the **caller** (disposition 7); and the summoned partner's own
  `thread.md` — **only when the consult changed its stance** (disposition 9). No session note from
  the summoned partner: **a consult is not a hand-off and crosses no sitting boundary**
  (disposition 6, single-homed in the contract at F7 — point at it here, do not restate it).
- **Report.** Brief, like relay's `:191-197`: who was consulted, the return type, and — on
  `insufficient-context` / `wrong-partner` / `needs-human` — what is missing, plainly.

**Also at this file, in the existing sections:**

- **`:49-63` Mode dispatch** — add `consult` to the subcommand list at `:53` and to the
  bare-invocation menu at `:56-59` (one line, matching the existing three: *"**consult** — ask
  another partner a question and get an attributed answer back now *(usually fired by a partner
  mid-turn)*."*).
- **`:73` — the B1-critical guard.** The `daily` watermark reader currently says *"relay blocks
  carry no watermark and are ignored here."* Extend it to name **relay and consult blocks** both.
  Missed, a `daily` run parses a `consult:` header looking for `routed through line N`.
- **`:230-239` Log** — add the consult line to the two existing formats:
  `## [YYYY-MM-DD HH:MM] dispatch (<from-slug>) | consult: <from> → <to> — <gist> → <return-type>`.
- **`:241-260` Verify** — add a `**`consult`:**` block: recipient slug live, exactly one
  `consult:` block appended, its pointer written **checked**, the raw answer surfaced attributed,
  no `daily/` read, no wiki write, no second partner spawned by the summoned one, the `{log}` entry
  appended tagged with the **caller**, no secret in the question or the gist.
- **Frontmatter `depends_on:` at `:3`** — `["spec@1"]` → `["consult@1", "spec@1"]` (the new
  convention's ack; F1 lists `vlt-dispatch` in `consumers:`).

**Why.** The mechanism half of ODQ #8's pairing, and the mode the contract's `:226` already names.

**B1 upgrade-preserve-path check — the ATTACHED precondition, discharged here.** Ideation attached
this as *"named in the brief, not discovered at implementation"* (Arc-3 roadmap `:2849-2854`).
Re-grounded 2026-07-26, four findings, all four already handled above or benign:

1. **`_agent/dispatch.md` is agent-zone and is never written by the install path.** `vlt-setup`
   never creates or touches it (grep of `skills/vlt-setup/` returns only governance-prose mentions);
   `vlt-upgrade` never rewrites it. Durability is by **location** — the contract's own principle at
   `vault-operating-contract.md:93`. **No merge script, no preserve-path code change is needed.**
2. **Forward-compatibility, old reader → new record.** An un-upgraded `vlt-dispatch` reading a
   record containing `consult:` blocks: `ledger`'s `- [ ]` greps (`:207-208`) skip pre-checked
   lines, and the `daily` watermark scan (`:73`) ignores non-`daily/` headers. It degrades to
   *invisible*, never to *wrong*. This is the reason the pre-checked ruling is load-bearing beyond
   its own semantics.
3. **New reader → old record:** nothing to migrate. The record is append-only; a vault with no
   consult blocks simply has none. **No backfill.**
4. **`vlt-upgrade/SKILL.md:74`'s re-point rule** ("re-point any *open* dispatch pointers from the
   old path to the new one" on a relocation migration) is **unaffected**: consult pointers are
   never open. Verify by reading, and state it in the brief's verification (check 11) rather than
   editing `vlt-upgrade` — no change is needed there.

## F4 — NEW: `skills/vlt-setup/assets/workflows/vlt-consult.js` (the engine)

**Current state.** Two workflow assets ship — `vlt-review-council.js` (183 lines) and
`vlt-lint-full.js` (291 lines). Both are copied to `{project-root}/.claude/workflows/` by
`vlt-setup/SKILL.md:158-161` and are **module-owned: overwritten on every install/update**.

**The exact change.** Add `vlt-consult.js`, modelled closely on `vlt-review-council.js`:

- `export const meta = { name: 'vlt-consult', description, whenToUse, phases: [{ title: 'Consult',
  detail: 'spawn the summoned partner; it answers as itself or names what it cannot answer' }] }` —
  a **pure literal**, no computed values.
- **Parse `args` on intake.** Copy `vlt-review-council.js:32-37` verbatim in substance — the runtime
  delivers `args` as a JSON **string** in every invocation form. This is a CLAUDE.md standing rule
  and the module has been bitten by it; the comment explaining *why* travels with the code.
- **Guard the required fields** (`fromSlug`, `toSlug`, `question`, `skillsPath`) and return a
  structured `{ error, received }` object on a miss, exactly as `:43-48` does.
- **One `agent()` call, schema-forced.** The `CONSULT_RETURN` schema is the typed union:
  `returnType` (enum: `answer` | `insufficient-context` | `wrong-partner` | `needs-human` |
  `needs-work`), `answer` (the raw text, in the summoned partner's own voice), `wrongPartner`
  (slug, set only for that return type), `missing` (array — what the payload lacked, set for
  `insufficient-context`), `stanceChanged` (boolean — whether the consult moved the summoned
  partner's position, which is what gates its `thread.md` write per disposition 9), and
  `groundedIn` (array — the paths it actually read, so the caller can see whether the answer rests
  on the payload or on nothing).
- **The prompt** instructs the spawned agent to: read the summoned partner's SKILL at
  `{skillsPath}/vlt-agent-{toSlug}/SKILL.md` and its `identity.md`/`thread.md`, **become that
  partner** and answer **in its own voice**; read every `groundIn` path from the **live** tree;
  answer only from its own domain; **never summon another partner** (depth-1, stated in the prompt
  as a hard rule); return `insufficient-context` rather than guessing; and write **nothing** except
  — where `stanceChanged` — its own `thread.md`.
- **Degrade gracefully**, as the council does at `:145-155`: if the partner's SKILL cannot be read,
  return a structured note rather than an invented answer.
- **No `Math.random()` / `Date.now()` / argless `new Date()`** — they throw in workflow scripts;
  the caller passes any date the block needs.

**Why.** Disposition 1 — the engine is a workflow so the union is enforced and depth-1 is
structural.

**Registration consequence.** `vlt-setup/SKILL.md:155-156` enumerates the two shipped workflows in
prose; add a third bullet (see F5). The copy step at `:160` is a glob and needs no edit.

## F5 — `skills/vlt-setup/SKILL.md:155-156` (grounding addition — the workflow enumeration)

**Current state.** `:155-156` names the two shipped workflows in prose:
*"- **`vlt-review-council.js`** — the review-council panel engine … - **`vlt-lint-full.js`** — the
fan-out wiki health-check …"*

**The exact change.** Add:
*"- **`vlt-consult.js`** — the synchronous partner→partner consult engine (`vlt-dispatch`'s
`consult` mode invokes it)."*

**Why.** Second half of the same drift hazard as F2. The copy itself is a glob (`:160`), so the
asset *would* install — but the prose that documents the install would assert two engines while
three ship, and this file is what a reader trusts about what the module installs.

## F6 — `skills/vlt-lint/SKILL.md` — the check (the pairing's enforcement half)

**Current state.**

- `:4` — `depends_on: ["frontmatter@4", "wiki-index@2", "wiki-supersession@2", "extraction@3",
  "write-verification@1", "spec@1"]`.
- `:43` — the governance checks stay in the SKILL's own jurisdiction: *"the PARA attestation scan …
  **the governance checks** … stay yours; fill those report slots from your own pass"* (the
  `vlt-lint-full` workflow sweeps `{wiki}` only).
- `:79-86` — the tier-2 governance checks, each with the same anatomy (what it validates, what it
  flags, **Never auto-fix**). `:86` is the `spec_candidate` check and is the structural sibling to
  copy — it also reads `_agent/dispatch.md`, and it counts *"**≥2 relay entries in
  `_agent/dispatch.md` pointing at the same path**"*.
- `:160-188` — the `flag_for_human` report keys; `:181` / `:186` are the two denominator lines
  A4-3 and A4-4 added (`contradiction_scan:`, `entity_scan:`).
- `:200-202` — the two reporting paragraphs that point at the honest-reporting rule without
  restating it.

**The exact change.**

1. **A new tier-2 governance check**, placed immediately after `:86`'s `spec_candidate` (they share
   a subject and a source of truth):

   > **Consult preconditions** (governance check; both modes) — for each `{specs}` artifact whose
   > `consumers:` name a partner other than its `owner`, confirm a **consult record** exists for
   > each such consumer: a `consult:` block in `_agent/dispatch.md` naming that
   > `(spec-path, consumer-slug)` pair. Flag (`consult_missing`) a spec that binds another
   > partner's domain with no consult record for that partner. The rule and its bound live at
   > `{conventions}/consult.md` — read them there. **Derived from the record, no stored counter**
   > (the `spec_candidate` posture at `:86`). **Never auto-fix** — a missing consult is closed by
   > *having the consult*, not by lint writing anything.

2. **Its structural blind spot, stated in the check's own text** (A4-4's shape at `:74`): the check
   sees `{specs}` only — a partner claiming another's domain in a wiki page, research note or
   session note is invisible to it **by construction**. That sentence is what the report's
   denominator must say.

3. **Report slots** (`:160-188`, beside the other governance keys):

   ```yaml
   authority_scan: <S specs compared; T binding a partner other than their owner>   # denominator + blind spot: out-of-authority claims outside {specs} are invisible by construction — a bare zero below is not health
   consult_missing: [<spec — binds <consumer-slug>, no consult record>, ...]
   ```

4. **A reporting paragraph** after `:202`'s entity-collision paragraph, in the same form: *"You
   compose that line yourself"* (a governance check, so it is the SKILL's own fact in both modes —
   `:43`), and *"Per the operating contract's honest-reporting rule — read it there."* **Do not
   restate the rule.**

5. **`:86` — a one-clause guard on the `spec_candidate` count.** It counts *relay* entries pointing
   at a path; make it read **relay entries** explicitly so a `consult:` block grounding in the same
   path can never be miscounted as a relay notification. This is a real hazard: a spec consulted
   twice before filing would otherwise self-promote itself as a spec candidate.

6. **`:4` `depends_on:`** — add `"consult@1"` (F1 lists `vlt-lint` in `consumers:`).

**Why.** ODQ #8's enforcement half, and what makes `consult.md` land at `enforcement_stage: checked`
rather than becoming the scar's fifth instance.

**One producer, named deliberately.** A4-3 and A4-4 both learned that a report-key change landing in
one producer means a full-mode sweep silently omits the key. It **does not apply here**:
`vlt-lint:43` puts the governance checks in the SKILL's own jurisdiction in both modes, and the
`vlt-lint-full` workflow sweeps `{wiki}` only — it never reads `{specs}` or the dispatch record.
`vlt-lint-full.js` is **not** touched by this build. Stated rather than assumed, because the last
two builds' instinct is the opposite.

**Honest-reporting conformance — the arc's fifth conformer.** `authority_scan:` carries the
population and names the blind spot in the same breath as the count, per
`vault-operating-contract.md:250-254`. No bespoke wording, no second home for the rule.

## F7 — `vault-operating-contract.md` — the pointer and the sitting clause

**Current state.**

- `:226` — A4-1's authority boundary: *"A partner **consults**, or it cites."* Names the act; points
  at no mechanism (correctly — `build-A4-1-linkage-polarity.md:415-418` deferred the mechanism
  sentence to this build by name).
- `:228` — read-and-cite as the documented default, carrying the trigger rule *"spawn another
  partner only when the interaction should be remembered."*
- `:213` — the sitting unit: *"A hand-off to another partner **ends one sitting and begins
  another**."*
- `:230` — *"**Two handoff timings — synchronous payload vs. durable doc.**"*

**The exact change — two sentences and one clause, no restatement of any mechanism:**

1. **At `:226`/`:228`** — one pointer sentence: the consult act now has a mechanism,
   `vlt-dispatch`'s `consult` mode, governed by `{conventions}/consult.md`; **mechanics live
   there.** This is precisely the "mechanism sentence" A4-1 held for this build.
2. **At `:213`, the sitting clause (disposition 6)** — *a consult is **not** a hand-off: no work and
   no wheel transfer, so it crosses no sitting boundary. The caller keeps the wheel and owns the
   single session note; the consulted partner writes none.* This must land at the sitting unit's
   single home, not in `vlt-dispatch`.
3. **At `:230`** — the two-timings paragraph describes **hand-offs**, and a consult is not one. Do
   **not** rewrite it into "three timings." Add one adjacent sentence distinguishing them: both
   hand-off timings *transfer work*; a consult transfers none and returns an attributed answer to a
   caller who never left the wheel.

**Handshake / registration.** The operating contract is **deliberately NOT handshaked** (CLAUDE.md
standing rule: single-home + pointers). This adds **no** ack obligation anywhere. Bump the file's
frontmatter `last_updated:` to the build date.

**Out of scope at this site.** Do not restate the payload, the return union, the block shape or the
trail here. `vlt-dispatch` owns the mode's mechanics and `consult.md` owns the rule — the same
division `:232` already holds for the relay reflex.

## F8 — `{conventions}/spec.md` — a Reading-list pointer (prose only, no bump)

**Current state.** `spec.md:83-87` is the Reading list, three entries. The file is `version: 1`
with four consumers (`:12`).

**The exact change.** Add one Reading-list entry: `consult.md` — the consult precondition that
applies to a spec binding a partner other than its owner. **Version-free pointer** — no `consult@1`
token (`package-lint` E3, `tools/package-lint.py:322-348`).

**Why / what is deliberately NOT done.** Disposition 5: **`spec.md`'s `version:` does not move and
its four consumers do not re-ack.** The obligation belongs to `consult.md`; a pointer is a prose
clarification, and CLAUDE.md's handshake rule is explicit that those don't bump. If the pointer as
written reads as *imposing* an obligation rather than *pointing at* one, rewrite the pointer.

## Registration

**Not `None.` — this build has the arc's only real registration surface.**

- **`skills/vlt-setup/assets/module-help.csv:11`** (the `DP` row) — the description opens *"one
  routing record (\_agent/dispatch.md) with a drain, **three modes**"* and enumerates them; the
  `args` column reads `"{mode: daily | relay | ledger; bare call → menu}"`. Both become **four**
  modes / `{mode: daily | relay | consult | ledger; bare call → menu}`, with one clause for
  `consult` matching the register of the other three. **Canonical 13-column header
  (`preceded-by,followed-by`) is intact and must stay; every free-text field stays quoted**
  (CLAUDE.md standing rule) — the row already quotes `display-name`, `description`, `args` and
  `outputs`; keep them quoted after the edit, and re-check the field count is 13 after any comma
  edit. The `outputs` column also names the record's traffic (*"open/picked-up items across daily +
  relay traffic"*) — extend it to name consult traffic.
- **The four-site dispatch arity surface** (ideation named it so it is not discovered at
  implementation — Arc-3 roadmap `:2883-2885`): `vlt-dispatch/SKILL.md:4` (frontmatter
  `description`, "three modes"), `:56` (the bare-call menu), `:120` (the `_agent/dispatch.md`
  file-header blurb, "read through three modes" — note this is the **record's own header**, not a
  log line), and `module-help.csv:11` above. **Grounding addition:** two more in-body sites say
  *three* and move with them — `:11` (the Overview's mode list intro) and `:17` (*"All three modes
  are the same machine"*, which stays **true** of consult: it emits the same pointer line into the
  same record — say four, keep the claim). Six sites, one arity.
- **New workflow asset** — `vlt-consult.js` (F4), enumerated at `vlt-setup/SKILL.md:155-156` (F5).
  No `module-help.csv` row: help rows register **skills**, not workflows.
- **New convention** — `consult.md` (F1), enumerated at `vlt-setup/SKILL.md:144` (F2).

**Consumer walk — exactly two acks, both new, both in this build.** `consult@1` is a **new**
convention, so nothing re-acks: `vlt-dispatch` (`:3`) and `vlt-lint` (`:4`) each add `"consult@1"`
to `depends_on:`, and `consult.md`'s `consumers: [vlt-dispatch, vlt-lint]` must match exactly.
**No existing convention `version:` moves in A4-5** — not `spec.md` (F8), not `frontmatter.md`, not
`wiki-supersession.md`. Bipartite consistency is verified at rest by `package-lint` Group E
(`tools/package-lint.py:351-382`, which globs the conventions dir, so the new file is picked up with
no tool change).

## Out of scope (dispositioned)

- **`dialogue`, `convene`, `summon`** — deferred by the filing, not reopened at ideation. Later
  *compositions* of this primitive; field traffic is single-question and the roundtable already
  exists as `vlt-review-council`.
- **Depth > 1 (a summoned partner consulting onward)** — rejected as a rule (disposition 1), not
  deferred. It is the boundary-erosion risk with extra steps.
- **The two deferred `vlt-lint` spec checks** (`spec_schema_violation`,
  `spec_notification_missing` — `{conventions}/spec.md:81`) — untouched. Their tripwire is
  unrelated and does not fire on this build.
- **Widening the consult precondition beyond `{specs}`** — rejected for v1 (disposition 3); the
  bound and its honest limit are stated in the rule itself. Re-files as a fresh filing if the field
  produces an out-of-authority claim outside `{specs}` that anyone could have caught.
- **A dual-partner `{log}` tag** — rejected (disposition 7); the contract's log format is unchanged.
- **`vlt-lint-full.js`** — untouched, deliberately (F6's "one producer" note).
- **`vlt-upgrade`** — untouched; the B1 finding is that no change is needed (F3, finding 4).
  Verified by reading, not by editing.
- **Partner SKILLs and `vlt-mint/assets/partner-agent-template.md`** — untouched. A partner's Beat-2
  line (`vlt-agent-librarian/SKILL.md:25` and siblings) names the *drain*, which consult does not
  use; the summoned partner receives the consult protocol in the engine's prompt (F4), exactly as a
  council lens receives its persona instruction. **This is the single-home posture, not an
  omission:** a partner *names* a reflex and points at its mode; it never restates the mechanics
  (`vault-operating-contract.md:232`). If the builder finds itself editing four partner files to
  make consult work, the engine's prompt is under-specified — fix the prompt.
- **Converting `vlt-setup:144`'s enumeration to a glob** — F2's out-of-scope note.
- **vlt-sayari verification** — unreadable from this machine (evidence debt, ruled not-blocking).

## Verification (unit, at rest — lifecycle step 5)

1. **Arity agreement (grep).** `grep -rn "three modes" skills/` returns **nothing** in
   `vlt-dispatch/SKILL.md` or `module-help.csv`; `grep -rn "four modes" skills/vlt-dispatch/SKILL.md
   skills/vlt-setup/assets/module-help.csv` returns the expected six sites (`:4`, `:11`, `:17`,
   `:56`, `:120`, csv `:11`). Reports under `skills/reports/` are history and may keep saying three.
2. **Mode-list agreement (grep).** Every enumeration of the mode set names all four in the same
   order (`daily` / `relay` / `consult` / `ledger`): `vlt-dispatch:4`, `:13-15`+new, `:53`, `:56-59`,
   `:120`, csv `:11` `description` **and** `args`.
3. **CSV integrity.** `module-help.csv` header is the canonical 13 columns
   (`module,skill,display-name,menu-code,description,action,args,phase,preceded-by,followed-by,required,output-location,outputs`);
   the `DP` row still parses to exactly 13 fields and every free-text field is quoted. Parse it with
   Python's `csv` module, not by eye.
4. **Handshake bipartite (the standing ritual).** `consult.md` `consumers: [vlt-dispatch, vlt-lint]`
   ↔ `vlt-dispatch:3` and `vlt-lint:4` each pin `consult@1`. No other `depends_on:` line in the repo
   changed: `git diff` shows exactly two `depends_on:` edits.
5. **No stray pins (grep).** No `consult@1` token anywhere outside those two `depends_on:` lines —
   `grep -rn "consult@" skills/` returns exactly two hits plus `consult.md`'s own frontmatter
   (`version: 1`, which is not a pin token).
6. **Enforcement frontmatter.** `consult.md` carries `version:`, `consumers:`,
   `enforcement_stage: checked`, `enforcement_checked_by: vlt-lint`, `enforcement_moment`, and
   `adoption_first_instance: null`, with **no** deferral keys. All keys flat (no nested
   `enforcement:` map — `frontmatter.md:225`). This is what `vlt-lint:80`'s meta-check will read in
   the field.
7. **Install-path enumerations.** `vlt-setup:144`'s brace list contains `consult`; `:155-156` lists
   three workflows. Grep both.
8. **Workflow script sanity.** `vlt-consult.js` starts with a literal `export const meta`; parses
   `args` defensively at the top (`typeof a === 'string'` → `JSON.parse`); contains no
   `Date.now(`, `Math.random(`, or argless `new Date(`; and `node --check` (or an equivalent parse)
   passes.
9. **Engine end-to-end, against real code.** Run the `vlt-consult` workflow once against a temp
   fixture — a throwaway `vlt-agent-*` SKILL and a temp file to ground in — and confirm: it returns
   a schema-valid object; a payload with an unreadable partner path returns the degraded structured
   note rather than an invented answer; and a deliberately thin payload returns
   `insufficient-context` rather than a confident answer. **This is the confabulated-authority
   mitigation under test** — do not skip it. (Real script run against a temp fixture, per lifecycle
   step 5.)
10. **Single-home audit (grep).** The trigger rule (*"should be remembered"*) appears **once** in
    shipped source, at `vault-operating-contract.md:228`. The consult precondition appears **once**,
    in `consult.md`. The block/payload/return mechanics appear **once**, in `vlt-dispatch`. No
    restatement in the contract, in `spec.md`, or in any partner SKILL.
11. **B1 re-check, by reading (F3).** Confirm at rest: `vlt-setup` still never writes
    `_agent/dispatch.md`; `vlt-upgrade:74`'s re-point rule concerns **open** pointers only and
    consult pointers are written checked; `vlt-dispatch:73` now ignores relay **and** consult blocks;
    `vlt-dispatch:207-208`'s greps count `- [ ]` only. Record the four readings in the BUILT status.
12. **`spec_candidate` cannot miscount (read).** `vlt-lint:86` counts **relay** entries explicitly;
    a `consult:` block pointing at the same path does not increment it.
13. **Report-block validity.** The `vlt-lint` Step-5 fenced block still parses as strict YAML with
    the two new keys added. *(Known pre-existing break at `sources_vs_prose_mismatches:`, recorded
    by A4-2 as check 7 PARTIAL and left byte-unchanged — if it is still there, this check is
    PARTIAL for the same reason and that is not a regression. Do not fix it here; its disposition
    sits with capture.)*
14. **Packaging lint — the release gate** (see Release below): `uv run tools/package-lint.py
    --expect-version 0.8.0` exits **0**. Groups A/B/C/E carry the cruft, CSV, structure-map and
    handshake nets; **D is live for this build** because it is the release.
15. **Scrub.** No personal or vault-local content in any changed shipped file; worked examples use
    placeholder paths (`_agent/specs/{date}-{owner}-to-{consumer}-{slug}.md` style) — the consult
    block example must use placeholder slugs and paths, never a real vault's. No `.decision-log.md`
    left in the working tree.

## Release (this IS the release build)

A4-1 through A4-4 are committed and **unreleased** — the owner held the version to arc end. A4-5
carries the release for all five.

1. **Dual version bump — both strings, same commit:** `.claude-plugin/marketplace.json` `"version"`
   and `skills/vlt-setup/assets/module.yaml` `module_version` (currently `0.7.0` at
   `module.yaml:4`) → **`0.8.0`**. A minor bump: five builds, a new dispatch mode, a new shipped
   convention, a new workflow asset, new lint findings — additive, no removals, no vault migration.
2. **Branch + commits.** Work on `arc4-v0.8.0` (or the branch already carrying A4-1..A4-4); **one
   commit for this build**, per the standing rule.
3. **The gate:** `uv run tools/package-lint.py --expect-version 0.8.0` — **tag only on exit 0**, and
   **record its PASS summary line in the release commit message** so a skipped lint is visible in
   history.
4. **Then** ff-merge to `main`, tag `v0.8.0`, push main + tag.
5. **`vlt-release`** runs this choreography as one gated sequence — prefer it over doing the steps
   by hand.
6. **Do not** archive the Arc-4 roadmap or discharge any ledger entry here. Acceptance rides the
   next ordinary vlt-core upgrade (the owner runs it); `arc-closeout` is a separate lifecycle step
   with its own gates.

## Acceptance (live — appended to the roadmap ledger)

On the next ordinary vlt-core upgrade (0.7.0 → 0.8.0) and the sittings and first full lint that
follow:

1. **The whole surface reaches the field** — the installed vault carries
   `_meta/conventions/consult.md` (at `version: 1`, `enforcement_stage: checked`,
   `adoption_first_instance: null`), `.claude/workflows/vlt-consult.js`, a `vlt-dispatch` offering
   four modes, and a help registry whose `DP` row says four. Any vault-local
   `consult.overlay.md` (if one is later grown) is untouched and no new
   `convention_base_divergence` appears (B1 posture). *Failure signature: the convention is in the
   repo but not in `_meta/conventions/` — the `vlt-setup:144` enumeration was missed.*
2. **A real consult runs, end to end** — one partner consults another mid-turn and the caller
   **keeps the wheel**: the sitting yields **one** session note (the caller's), the consulted
   partner writes none, and the raw answer appears **attributed, in its own block**, before the
   caller's use of it. *Failure signature: two session notes for one sitting (the consult was
   treated as a hand-off), or the answer arriving already digested into the caller's voice.*
3. **The record shows consult traffic, and the board does not** — `_agent/dispatch.md` gains a
   `consult: <from> → <to>` block whose pointer is written **checked (`- [x]`)**, and the same
   run's `ledger` mode does **not** list it as open. The `{log}` line is tagged with the **caller**
   and names the consulted partner in its summary. *Failure signature: a consult sitting open in a
   partner's slice forever — the pre-checked rule regressed.*
4. **The refusals are real, not decorative** — within the first sittings, at least one consult
   returns something other than `answer` (`insufficient-context`, `wrong-partner`, `needs-human`, or
   `needs-work`) and the caller routes it correctly (`needs-work` exits through `relay`, not through
   the consulted partner doing the work). **Non-blocking if every consult in the window legitimately
   answers**, but a run of consults that *only ever* return `answer` is the confabulated-authority
   signature and must be inspected, not assumed healthy.
5. **The bound holds on memory** — the consulted partner's `thread.md` gains an entry **only** where
   the consult changed its stance; a consult that merely confirmed what it already held leaves the
   prunable file untouched. *Failure signature: one `thread.md` line per consult — the rot the bound
   exists to prevent.*
6. **The check is live and exercised by construction** — the first full `vlt-lint` after upgrade
   emits `authority_scan:` and `consult_missing:`, and the check is **testable on real state**: a
   `{specs}` artifact binding a partner other than its owner either shows a consult record or
   surfaces as `consult_missing`. **Non-blocking if the vault has no such spec in the window** —
   but the absence must render as `authority_scan:` with its denominator (*S specs compared; 0
   binding another partner*), **never as silence**. *Failure signature: a bare zero, or the slots
   missing entirely.*
7. **The report is honest about what it cannot see** — `authority_scan:` names the blind spot beside
   the count (out-of-authority claims outside `{specs}` are invisible by construction), with no bare
   zero on either fidelity slot. A3-22 discharged by conformance to A4-2's general honest-reporting
   rule as its **fifth conformer**, not by bespoke wording.
8. **Nothing else moved** — `convention_drift:` is empty (only `consult@1` is new; no existing
   convention re-acked), `spec.md` is still `version: 1` with its four consumers, and the
   `spec_candidate` check does not fire on a spec whose only extra dispatch traffic is consults.
9. **Second-vault check, non-blocking** — if vlt-sayari becomes readable, confirm the four modes and
   both report slots installed there, and that the Navigator→Engineer friction the filing describes
   now has a channel. A3-22's evidence is one vault, taken as filed and never verified factory-side;
   the fix does not wait on it, and nothing here may assert what vlt-sayari's state was.
10. **The release itself** — installed `module.yaml` reports `0.8.0`, the marketplace manifest agrees,
    and the tag `v0.8.0` exists on `main` with the `package-lint` PASS line in its release commit.
