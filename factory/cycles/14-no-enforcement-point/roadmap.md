---
title: 'Cycle 14 — no enforcement point'
status: 'OPEN — captured 2026-08-26, 7 filings grounded against module source at v0.16.1. Not yet ideated. **This cycle carries Cycle 13''s closeout gate**: Cycle 13 shipped v0.16.1 and then FAILED acceptance check (2) on live field evidence; it is closed to capture (ship day is the capture boundary) and cannot close until a Cycle 14 build repairs the guard. **A14-1 is that repair and is the cycle''s gating entry.** Scope was owner-ruled at capture (2026-08-26): defects and blockers from Cycles 12–13 only, net-new capability deferred — see §Owner ruling — debt-clearing scope.'
module_code: 'vlt'
created: '2026-08-26'
updated: '2026-08-26 (opened by inbox-capture; GitHub intake materialized 5 issues; 7 filings captured and graded; 1 filing deferred by owner ruling; Cycle 12''s six bounded tails recorded as bound-landed)'
derives_from:
  - 'factory/inbox/2026-08-26-164500-reduce-guard-residue-rule-defeated-by-a-scanner-that-cites-its-rule.md'
  - 'factory/inbox/2026-08-26-164501-page-scanner-under-returns-outbound-links-and-manufactures-an-orphan.md'
  - 'factory/inbox/2026-08-26-164502-html-escaped-scanner-return-fails-an-exact-comparison.md'
  - 'factory/inbox/2026-08-26-123144-reclassify-sources-vs-prose-mismatches-out-of-fix-now.md'
  - 'factory/inbox/2026-08-26-123153-lint-mandates-strict-yaml-persist-with-no-yaml-library.md'
  - 'factory/inbox/2026-08-26-125529-recognized-type-names-no-owning-convention.md'
  - 'factory/inbox/2026-08-26-141418-layer-3-open-entry-vs-closed-verified-by-roster.md'
predecessor: 'factory/cycles/13-trusted-returns/roadmap.md (Cycle 13 — SHIPPED v0.16.1 @ `c18c591` 2026-08-26; OPEN and GATE-SHUT for acceptance, closed to capture, cannot close without a Cycle 14 repair)'
intent: >
  Cycle 13 shipped a guard on the premise that a rule stated in a prompt and enforced nowhere
  does not bind. The guard then failed in the field within hours, for the same reason: its own
  enforcement point had to parse scanner-returned free text in order to decide whether to trust
  a scanner-returned claim. Cycle 14 opens on the generalized form. Every entry here names a
  rule the module genuinely states and a place that is supposed to enforce it, and in each case
  the enforcement point is missing, unreachable, or lacks the one input that would let it
  decide — the reduce that cannot read a page, a fix_now class whose auto-fix procedure never
  names it, a strict-YAML mandate with no parser, an entry condition whose vocabulary has no
  named owner, an open writer set meeting a closed attester roster. This is a deliberate
  debt-clearing cycle: it takes the blockers the last two releases left open and adds no new
  capability.
---

## The through-line

Cycle 12 asked what a claim rests on. Cycle 13 asked what the *reduce* rests on and answered it
for one case — then watched the answer break in the field on 2026-08-26, refuted on a named
subject by the first live post-upgrade sweep. Cycle 14 is what that failure generalizes to.

The shape, stated once: **the module states a rule, and names a place responsible for it, and
that place cannot carry out the judgment the rule requires.** Not because the rule is wrong, and
not because the enforcement was forgotten — in every one of the seven captures below, both halves
were written deliberately and both are individually defensible. The defect is the *seam*.

Seven filings, three seams:

**The scan → reduce seam (A14-1, A14-2, A14-3).** `vlt-lint-full.js` fans out to LLM scanners and
reduces their returns with exact, careful JavaScript. The reduce has the arithmetic; it does not
have the page. All three of this sweep's false findings come from the reduce performing precise
work over a value it has no way to verify — prose (A14-1), an enumeration (A14-2), an encoding
(A14-3). The workflow's filesystem-free design (`vlt-lint-full.js:36-38`) is the structural
reason: it is what keeps the fan-out clean and it is what makes verification impossible from
inside. Cycle 13's own §Carried forward already named the general answer (*every agent-returned
value that is mechanically checkable at the reduce is checked there*) and deferred it once.
The field has now paid for that deferral three times in one sweep.

**The stated-mandate seam (A14-4, A14-5).** A promise written into a schema or a reference with
nothing shipped that could keep it. `sources_vs_prose_mismatches` sits in the `fix_now:` slot —
the slot meaning *safe to apply serially without judgment* — and the auto-fix procedure it would
be applied by never mentions it (A14-4). `report.md` requires the persisted report parse as
strict YAML "whole, in both homes" and the module ships nothing that emits it and nothing that
checks it (A14-5). Both are the Cycle 13 premise one layer out from the workflow: an instruction
at a site with no enforcement point.

**The roster seam (A14-6, A14-7).** Two shipped governance surfaces that each answer correctly
and answer differently. Layer 3's entry condition requires "a recognized `type:`" and never names
the recognizing convention, while `frontmatter.md` ships a non-exhaustive list and
`extraction.md` ships a closed set that excludes one of the other's canonical values (A14-6). The
contract declares the Layer-3 writer set explicitly open, and `write-verification.md` closes the
attester set to write ops — so a write the contract calls legal cannot satisfy the condition of
its own legality (A14-7). Both are 0.16.0 residue: that release moved Layer 3's boundary from
location to attestation and walked three of the four legs to their homes. The two that did not
move are exactly these.

**Why the three seams are one cycle and not three.** Cycle 13's diagnosis — *a rule stated where
it cannot bind* — was written about a schema description read by an LLM. Every entry here is that
same sentence with a different pair of surfaces substituted in. A14-7 is the governance-side twin
of A14-1: in one, JavaScript trusts a claim it cannot check; in the other, a partner must produce
an attestation it cannot legally hold. Fixing them as seven unrelated patches is available and is
what "instances only" means; the roadmap records that the option exists and that ideation, not
capture, rules on it.

## Owner ruling — debt-clearing scope (2026-08-26)

Ruled at capture, before grounding, and recorded here because it shaped what this run covered.

**The ruling:** Cycle 14 carries forward the **defects and blockers** from Cycles 12 and 13 only.
Lingering issues from the last two releases are closed out **before** any net-new capability
opens. Capture applied it as an admission test, not as a grading input — every filing this run
touched was still fully grounded.

**Admitted (7):** A14-1..A14-3 (the three defects the Cycle 13 discharge run filed), A14-4
(`kind: defect`), A14-6 and A14-7 (both blocking a live `{field-vault}` `parked-interim`), and
A14-5 — filed as `kind: candidate` but **owner-reclassified as a blocker at capture**: the module
mandates a machine-readable artifact and ships no means to produce it, on an environment class
(PEP 668) that is now the default rather than the exception.

**Deferred (1):** `factory/inbox/2026-08-26-123151-lint-full-inline-args-payload-costs-the-caller-84kb.md`
(tracker **#13**) — a request for a new `argsPath` invocation route for `vlt-lint-full`. Net-new
capability; it stays in `factory/inbox/` un-captured and is **not** in this cycle's
`derives_from:`. Its issue is labeled `captured` on the tracker because the intake materialized
it this run; that label records materialization, not admission to this roadmap.

⚠ **The deferral is not clean, and ideation must see why.** Cycle 13 §Carried forward item 1
records that fixing the paraphrased-verbatim field "costs a SKILL-side per-page arg on the
`pageHashes` precedent (`:47-49`) — and that arg moves the joint against tracker **#13**'s payload
cost." The same is true of A14-2's and A14-3's mechanical-verification directions and of the
general posture. **Any resolution that gives the reduce ground truth needs a payload route, and
#13 is that route.** If ideation takes the posture, #13 stops being net-new and becomes a
dependency; the owner would then re-admit it by ruling. Capture does not pre-empt that — it
records the joint so the ruling is made with it in view.

## Capture — 7 filings (grounded against module source 2026-08-26, at v0.16.1 @ `c18c591`)

Every `file:line` below was re-derived this run against working-tree source; none was taken from
a filing on faith. Where a filing's own `provenance_guess` was checked and held, that is stated —
three of the four rail filings guessed their sites exactly, which is unusual and is worth the
record.

### A14-1. The reduce-side guard is defeated by a scanner that cites the rule it applies (2026-08-26) — `factory/inbox/2026-08-26-164500-reduce-guard-residue-rule-defeated-by-a-scanner-that-cites-its-rule.md`

**⚠ This is the cycle's gating entry.** Cycle 13's acceptance check (2) is ship-verifiable, GATES
its closeout, and is FAILED by owner ruling on this filing's evidence. Cycle 13 has no discharge
path left — (2) is refuted, not waiting — so only a shipped repair moves it, and Cycle 13 is
closed to capture. **Cycle 13 cannot close until a Cycle 14 build lands this.**

**CONFIRMED — the guard, the predicates, and the defeat mechanism.** Both dispositions end in the
same conjunction. `attestationOnlyComplaint()` at `vlt-lint-full.js:612-617` and
`inventedRequirement()` at `:623-628` each require, as their final term, `claim.residue === ''`.
`parseClaim()` at `:594-604` normalizes the claim text (`:591` `normalizeClaim`, lowercase +
non-alphanumeric collapse), consumes every recognized frontmatter key longest-first from
`KNOWN_FRONTMATTER_BY_LENGTH` (`:579`), and returns whatever survives the `CLAIM_FILLER` strip
(`:591`) as `residue`.

A scanner that **cites the rule it is applying** defeats the conjunction on two independent legs
at once, and the citation is the cause of both:

- the quoted rule text leaves prose the filler list does not cover, so `residue !== ''`; and
- the quoted rule names `type:` and `author:`, both real members of `PAGE_REQUIRED_FRONTMATTER`
  (`:569`), so `fieldsNamed(claim, PAGE_REQUIRED_FRONTMATTER).length === 0` is also false.

Either leg alone suppresses the guard. The discharge run reproduced this at rest against shipped
source: the 2026-08-25 bare form yields `residue=""` and is REFUSED; the 2026-08-26 rule-citing
form yields `named=[verified_by, verified_at, author, type]` and a non-empty residue, and is not
refused. **Nothing about the pages changed — only the scanner's phrasing did.**

**GAP CONFIRMED — the comment at `:559-561` is now false as written.** It states the guards "never
fire on a claim they cannot positively identify — the failure direction is over-reporting, never
swallowing a genuine schema break." The first half is the residue rule and it holds. The claim
the comment makes about *safety* is the one the field refuted: over-reporting is indeed the
failure direction, and that is precisely why the guard silently stops working the moment a
scanner gets more verbose. A guard whose population is "the subset whose wording happened to be
terse" has no stable population at all. Whatever build takes this must correct the comment or
retire the claim — a shipped comment asserting a safety property the field has refuted is the
same defect one level further out.

**Residual scope, stated honestly.** The filing's own diagnosis is the durable one and capture
does not improve on it: the enforcement point *parses scanner-returned free text in order to
decide whether to trust a scanner-returned claim*. Any fix that keeps that shape is a
better-tuned parser, and the next rephrasing finds the next hole. Cycle 13's §Carried forward
item 2 (the general posture) is the named alternative. **Which of the two Cycle 14 takes is
ideation's ruling, not capture's** — but note the asymmetry: the narrow fix reopens Cycle 13's
gate sooner, and the general fix is the only one that also answers A14-2 and A14-3.

**Cites `ST-5`** (`factory/studies/ST-5-specimens-have-no-owner.md`). Cycle 13's roadmap carries
the standing correction unchanged, and this filing sharpens it rather than restating it: the
instrument for check (2) was the *recorded returns*, and those returns were themselves an
unrepresentative subset — every one of them bare-form, which is exactly the subset the guard
handles. The instrument could not observe the failure mode the check was written to catch. That
is ST-5's second cause (*an instrument authored from the fix's shape cannot observe what the
fix's author did not anticipate*) with a new and unusually clean specimen: the substitution that
made the check pass is visibly *why* it passed.

*Not carried, deliberately (restated from Cycle 13 so a later reader does not read it as an
oversight):* the prompt-side prohibitions at `vlt-lint-full.js:159`/`:168` that the guard makes
redundant are **kept** as defence in depth. They remain correct and cheap, and a scanner that
honours them produces less work for the guard.

### A14-2. The page scanner under-returns outbound links, and one miss manufactured an orphan (2026-08-26) — `factory/inbox/2026-08-26-164501-page-scanner-under-returns-outbound-links-and-manufactures-an-orphan.md`

**CONFIRMED — the consumption path.** The reduce normalizes the agent's returned
`outbound_links` at `vlt-lint-full.js:354`, builds the inbound map from it at `:363`, and computes
`orphans` at `:377` as the scans with no inbound entry. `outbound_links` is agent-returned
(`:158`, `required` at `:148`); nothing between the scanner and `:363` verifies it. The filing's
field measurement — 11 of 146 pages under-returning, 23 dropped instances, exactly 1 wiki→wiki,
manufacturing the sweep's only orphan — is consistent with this path.

**CONFIRMED — the severity bound, in the direction the filing states.** A dropped link lowers an
inbound count and can therefore fabricate an orphan; it cannot raise one, so it cannot hide a
true orphan. `missing_targets` at `:385` iterates the returned links, so a dropped link is never
iterated and cannot fabricate a missing target. Both halves hold.

**Sharpened — the filing understates its own blast radius on two counts.**

1. *`missing_targets` is not "undamaged in direction" — it is silently under-inclusive.* A
   dropped link that pointed at nothing is a real missing target that goes unreported. The filing
   is right that the class gains no false positives; it is wrong that the class is undamaged. The
   false-negative direction is the one nobody notices.
2. *There is a third consumer the filing does not mention.* `near_duplicates` reads
   `outbound_links` at `:397` (the hub-excluded link sets) and again at `:452-455` (the shared-link
   count and the direct-citation test, gated on `NEAR_SHARED_MIN` at `:396`). Dropped links
   suppress shared-link signals, so under-returned pages are under-detected as near-duplicates.
   Three consumers inherit the incompleteness, not one.

**PROVENANCE CORRECTION — candidate direction 1 is not implementable where the filing puts it.**
The filing proposes that "the reduce (or a cheap non-agent pass) can count them itself." It
cannot: `vlt-lint-full.js:36-38` states the division explicitly — *"the SKILL has filesystem
access, this script has none."* The workflow never sees page bytes. A mechanical `[[...]]`
extraction must run SKILL-side and arrive as an argument, on the `pageHashes` precedent at
`:47-49`. **That is the #13 payload joint** (§Owner ruling above), and it applies to candidate 2
as well, since a cross-check needs the same mechanical count. Capture does not rule the direction
out — it corrects where the work lands and names the cost the filing did not know about.

Candidate 3 (ask the scanner to return links more carefully) is named **to be rejected** by the
filing itself, on the grounds that prompt-side fixes failing is the entire premise of Cycle 13.
Capture agrees and records it so ideation does not re-derive the rejection.

### A14-3. An HTML-escaped scanner return failed the reduce's exact comparison (2026-08-26) — `factory/inbox/2026-08-26-164502-html-escaped-scanner-return-fails-an-exact-comparison.md`

**CONFIRMED — the comparison and its deliberate strictness.** `category_no_match` at
`vlt-lint-full.js:670` tests `!h2set.has(s.category)`, and the comment at `:668-669` states the
binding is "case-sensitive by design: no trimming, no case folding." A scanner returning
`Energy &amp; Clean Tech` for a page carrying `Energy & Clean Tech` fails a `Set.has()` against
the un-escaped heading. The filing's field result — the sweep's only `category_no_match`, and
false — follows directly.

**CONFIRMED — the filing's framing of the fix.** The exactness is not the bug. Loosening the
comparison (candidate 3) retires a class of true drift finding in order to work around a
transport defect, and leaves the transport defect live for every other exactly-compared field.
The filing names this to be rejected; capture agrees.

**Sharpened — both sides of the comparison traverse an agent, and the filing only noticed one.**
`h2set` is built at `:643` from `indexScan.h2_headings` — the **index scanner's** returned value,
not a mechanically parsed heading list. So the exposure is symmetric, and the two sides are not
equally severe:

- a `&amp;` on the **page** side produces one false finding (what the field hit);
- a `&amp;` on the **index** side produces a false `category_no_match` for **every page in that
  category at once**, because the entire `h2set` member is wrong.

The fan-out-wide failure is the one that has not fired yet. Any repair that normalizes only the
page-side `category` leaves the worse half live.

**GAP CONFIRMED — this is the second face of A13-1 Finding 2, and the filing identifies it
correctly.** `PAGE_SCAN` marks fields *verbatim* in schema descriptions (`:158` for
`outbound_links` — *"verbatim; do not normalize"*; `:162` for `summary`), and Cycle 13 established
that a schema description is an instruction, not an enforcement point. Cycle 13's §Carried forward
item 1 is the **paraphrase** face of that finding; this is the **re-encoding** face. The comment
at `:543` states the design posture — *"Verdicts computed from verbatim extractions (B5-3) — the
scanner reads, JS does the arithmetic"* — and that posture is sound. Nothing enforces the word
*verbatim* in it.

### A14-4. `sources_vs_prose_mismatches` sits in `fix_now:` and its fix direction deletes real provenance (2026-08-26) — `factory/inbox/2026-08-26-123144-reclassify-sources-vs-prose-mismatches-out-of-fix-now.md` (`origin: mggower/bmad-module-vlt#12`)

**CONFIRMED — the classification.** The class is in the `fix_now:` block in both homes: the report
schema at `skills/vlt-lint/references/report.md:21`, and the emitted report at
`vlt-lint-full.js:665` (inside the `fix_now:` object opened at `:652`; `flag_for_human:` opens at
`:667`).

**CONFIRMED — the fix direction and its asymmetry.** `skills/vlt-lint/references/checks.md:16`
states the legal response as *"reconcile the prose section to frontmatter `sources:` — frontmatter
is the source of truth."* Applied where prose cites sources frontmatter omits — the direction the
filing measured as dominant — that instruction deletes real citations. The filing's field
evidence (26 then 25 instances across two consecutive full sweeps on ~146 pages, **zero**
auto-applied, both runs declining the whole class for the same recorded reason) is a 0%
application rate against a slot whose meaning is *safe to apply serially without judgment*.

**GAP CONFIRMED, and sharper than the filing knew — the class has no auto-fix procedure at all.**
`skills/vlt-lint/references/fix-and-file.md` Step 3 is the auto-fix list: index drift, frontmatter
/ Bases-field drift, broken wikilinks, formatting, unmarked supersession/stale callouts. It does
**not** name `sources_vs_prose` anywhere; a `grep` for the token across `skills/vlt-lint/` returns
exactly two hits, `report.md:21` and `checks.md:16` — the slot and the check, never the procedure.
So the class occupies a `fix_now:` slot whose Step-3 procedure gives a fixer nothing to execute,
and the only stated direction lives in the check catalogue. This strengthens the filing rather
than changing it: the misclassification is not merely mis-tiered, it is **unimplemented**, and
the two full-sweep declines are what an unimplemented `fix_now` class looks like from the field.

**Residual scope.** The filing's own preference order survives grounding intact and capture
enshrines it as the material, not as a ruling:

1. Give the check a **second legal response** — *add the missing entries to frontmatter* — and
   route by direction: prose ⊂ frontmatter is auto-fixable, frontmatter ⊂ prose is
   `flag_for_human`. Keeps the cheap half automatic. Costs an edit at `checks.md:16`, a Step-3
   entry in `fix-and-file.md` that does not exist today, and a report-slot decision.
2. Failing that, move the whole class to `flag_for_human` and drop the `fix_now:` slot.

**Open design question, carried verbatim, not resolved here:** the filing argues that
*"frontmatter is the source of truth"* needs a qualifier — *"it is authoritative about what the
page claims to rest on, not about what the page actually cites, and the check currently reads it
as the latter."* That is a claim about `write-verification.md`'s tier-1 item, not only about the
lint check, and its blast radius was not measured by the filing or by this grounding.

*The filing's `provenance_guess` — that the classification was set from the check's
**detectability** (one-file-checkable → tier 1 → amortizable into writes) rather than from its
**remediability** — is a diagnosis capture could not confirm or refute from source. It is
recorded as the filer's reasoning, unverified.*

### A14-5. `vlt-lint` mandates a strict-YAML report persist and ships no way to satisfy it (2026-08-26) — `factory/inbox/2026-08-26-123153-lint-mandates-strict-yaml-persist-with-no-yaml-library.md` (`origin: mggower/bmad-module-vlt#14`)

**CONFIRMED — both mandates, quoted exactly as the filing quotes them.**
`skills/vlt-lint/SKILL.md:74` requires the persist: *"write the Step-5 report block **verbatim** to
`{lint_reports}/YYYY-MM-DD-HHMM-lint.yaml` — plain YAML, the block's content without the fence."*
`skills/vlt-lint/references/report.md:3` requires the strictness: *"The fenced report block is
strict YAML as a whole … keep it parsing whole in both homes."* Neither site names a mechanism.

**PROVENANCE CORRECTION — the shipped design needs no serializer, and that relocates the gap.**
The filer inferred a missing YAML *emitter*. The report is not serialized from a data structure:
Step 5 (`report.md:5-7`) has the **agent** author the fenced block directly, and Step 6 persists
that block **verbatim**. So the shipped path never calls a YAML library, and the PEP 668 failure
the filer hit was in their own hand-rolled workaround, not in a shipped code path.

What is genuinely missing is the other half, and it is worse: **nothing validates the claim.**
"Keep it parsing whole in both homes" is a property asserted at `report.md:3` with no site that
checks it, and — as the filing correctly observes — on a PEP 668 machine the vault cannot even
check it by hand. The report is LLM-authored YAML containing free-text findings with em-dashes,
colons inside values, quoted strings and arrows: exactly the content where naive emission breaks
and "it looked fine" is not verification. **This is the cycle's through-line at the report seam** —
a stated rule with no enforcement point — and it is why the owner reclassified a `candidate` as a
blocker.

**GAP CONFIRMED — and a shipped constraint the filing could not have known.** `machine_tools` in
`skills/vlt-setup/assets/module.yaml` currently declares exactly one vault-side tool assumption:
`gh`, needed by `vlt-feedback`. The same block carries a writer clause: *"a module build that adds
a shipped tool assumption adds its row here in the same build."* So the filing's option 2 (ship an
emitter) and any validation step that assumes a YAML parser are **not free** — each adds a
machine-tool assumption and owes a `machine_tools` row in the same build, and `vlt-setup`'s
dependency probe reports but never gates, so a vault without it degrades rather than fails.

**Residual scope, re-ordered by grounding.** The filing's option 1 was written as "specify the
JSON-subset emission strategy." Grounding narrows and redirects it:

1. **A validation beat**, not an emitter — the gap is the unchecked claim. Whether it can be
   satisfied without a parser is genuinely open (JSON-subset emission is self-validating by
   construction only if something checks the construction).
2. **State the no-dependency requirement explicitly** in `report.md` and specify JSON-subset
   emission — every scalar a JSON string, lists as `- <json>`, nested maps by indentation. Pure
   documentation, zero `machine_tools` cost, and it makes every vault's output identical instead
   of independently invented. Available immediately.
3. **Allow `.json` as an alternative persist.** The report's consumers are machines; JSON is
   trivially emittable and trivially checkable everywhere, and the fenced in-session block can
   stay YAML for human reading. Note this touches the "both homes" rule at `report.md:3` directly.
4. Ship an emitter as a skill asset — **costs a `machine_tools` row**; ranked last for that reason,
   which is a reversal of the filing's own ordering.

### A14-6. Layer 3's entry condition requires "a recognized `type:`" and names no owning convention (2026-08-26) — `factory/inbox/2026-08-26-125529-recognized-type-names-no-owning-convention.md` (`origin: mggower/bmad-module-vlt#15`)

**CONFIRMED — the entry condition and the missing pointer.**
`skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md:66` states Layer 3's boundary
as an entry condition requiring "an honest `author:`", "a `trust:` rung the writer is entitled to
set (**the trust ladder in `extraction.md`**)", "a recognized `type:`", and "the write-verification
attestation pair (**`write-verification.md`**)". Three legs carry an inline home. The `type:` leg
carries none. The filing's central claim is exact.

**CONFIRMED — the two conventions genuinely disagree, on a named value.**
`conventions/frontmatter.md:71`: *"The `type:` list is **non-exhaustive.** Canonical values include
`wiki`, `research`, `session`, `note`, `project`, `area`, `resource`, `idea`, and the PARA
container files `charter`, `record`, `register` … New artifact classes may introduce new `type:`
values without a contract edit."*
`skills/vlt-lint/references/checks.md:19`, `para_type_unknown`: the recognized set is *"the artifact
types `project|area|resource|moc`, the container types `charter|record|register`, and any
vault-declared schema in `{overlays}/extraction.overlay.md`."*
`research` is **canonical** under the first and **outside the recognized set** under the second. A
file carrying it is simultaneously well-formed and a loud finding. Confirmed as filed.

**CONFIRMED — the precedent, and it is stronger than the filing argues.** The by-name `{wiki}`
exclusion appears twice, and the canonical statement is in the **contract** itself
(`vault-operating-contract.md:65`, Layer 2): the `{wiki}` subtree *"is **removed from any PARA
population at selection time**, by name, never as an exception applied inside a check or a
resolver"* — with `checks.md:19` implementing it. The filing calls this "hard-coded to that one
case"; grounding confirms it and adds that the hard-coding is written into the contract as a
named singleton, not as a list with one member. A vault landing a second agent-lane subtree at a
browsable `{resources}` address has no general form of the move.

**Sharpened — the filing's option 4 is not a new ruling; it is already the shipped text.**
`checks.md:19` states `para_type_unknown`'s legal response as *"declare the vault-grown type as
overlay schema (declare-at-birth, `extraction.md`), retype to the shipped vocabulary, or relocate
the file out of PARA."* So "overlay-declare it, every time" is what the module already says. What
is missing is only that `contract:66`'s entry condition never points a reader at the convention
that says it. **The residual scope may therefore be a pointer, not a vocabulary decision** — a
materially cheaper cycle than the filing's four-option framing implies. Ideation should test that
reading first, because if it holds, options 1 and 3 are re-scoped from "widen the set" to "were we
right the first time."

**Sharpened — the sibling net has the same shape and no escape hatch at all.**
`para_author_unknown` (same line, `checks.md:19`) closes `author:` to `human|agent|hybrid` with no
overlay route. If ideation rules that closed sets need a general declaration mechanism, that net
is in the population and the filing does not mention it.

**Cites `ST-2`** (`factory/studies/ST-2-location-as-proxy-for-trust.md`). Its RC1 is the cause this
filing sits downstream of, and the filing's own account of *why this bites now* is RC1's
repair-residue: 0.16.0 replaced the location test with an attestation-based entry condition, and
under the retired location rule an agent-lane `type:` could never reach the PARA population
because agent-lane *files* never did. Capture states only what is new — the `type:` leg is the one
of four that did not move with the boundary — and does not re-derive ST-2's diagnosis. Append this
capture to ST-2's `cited_by:`.

**Live blocking instance.** `{field-vault}` holds a live `kind: parked-interim` against this
filing rather than resolving it locally by overlay, on the stated grounds that a local overlay
would be a vault answering a module-level question. Cycle 13's discharge run confirms it
reproduced exactly in the 0.16.1 sweep — 5 `type: research` briefs, matching the parked entry to
the file — and that v0.16.1 moved nothing here.

**Open design questions, carried verbatim, not resolved here.** The filing states four usable
rulings (frontmatter's list governs and the closed set narrows to a status-enum concern; the
closed set is authoritative and frontmatter's non-exhaustiveness is scoped to the agent lane; a
general carve-out mechanism generalizing the by-name exclusion to a declared list; or ruled
working-as-designed). It explicitly declines to choose: *"This is an ask for a ruling, not a
proposed answer. Any of these is usable; the current silence is not."*

### A14-7. Layer 3's open entry condition meets `write-verification.md`'s closed `verified_by` roster (2026-08-26) — `factory/inbox/2026-08-26-141418-layer-3-open-entry-vs-closed-verified-by-roster.md` (`origin: mggower/bmad-module-vlt#16`)

**CONFIRMED — every cited site, at the exact line the filing guessed.** This filing's
`provenance_guess` was checked against working-tree source and holds on all four:

- `vault-operating-contract.md:66` — Layer 3's entry condition, and the openness clause: the two
  shipped dispositions *"are the shipped set, **not** a closed one: another verb filing an honest,
  attested document under the condition above is legal."*
- `conventions/write-verification.md:47` — the closure: *"the `verified_by` value set is this
  file's `consumers:` **that are write ops**, plus write-op `local_consumers:` registrants … The
  roster is **membership and ceiling**, never an automatic grant."* `consumers:` at `:12` is
  `[vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-lint-full.js]`.
- `conventions/write-verification.md:53-54` — §Scope rule (self-marker), which puts the resulting
  files in jurisdiction: lint flags *"files carrying vault frontmatter (`type:
  wiki|research|project|area|resource` with `author: agent|hybrid`) and no attestation"*, exempting
  only `daily/`, raw `sources/` deposits, and human-authored PARA files.
- `conventions/extraction.md:188` — the container-file carve-out, *"operational records, not
  knowledge artifacts … they carry **no** pair"* — restated canonically at
  `vault-operating-contract.md:70`. The precedent the filing names is real: the module has already
  ruled one class of Layer 3 file **out of attestation jurisdiction** rather than inventing a value
  for it.

**CONFIRMED — the contradiction is live and the failure direction is the dishonest one.** The
contract declares the writer set open; `:47` closes the attester set to write ops. A partner
authoring a Layer 3 document during an ordinary sitting satisfies honest `author:`, an entitled
`trust:` rung and a recognized `type:` (subject to A14-6), then reaches §Attestation and finds no
value it may honestly hold — every roster member names an op that did not write the file. The
§Scope rule then places the file in jurisdiction and flags it, with no route to clear the flag.
The filing's observation that the cheaper of the two available responses is the dishonest one
(fake a provenance claim, or leave the finding permanently open) is a correct reading of the
shipped text.

**Sharpened — a third route exists in the source that the filing's two options miss, and it
narrows the gap without closing it.** `:47` admits *"write-op `local_consumers:` registrants"*, and
`local_consumers:` is a **vault-written** declared field (`frontmatter.md:294`, `:296`). So a
vault-minted partner **can** already hold a legal `verified_by` value — by registering as a
write-op local consumer. That route does not rescue the filing's population, for two reasons worth
stating precisely because they change what a fix must do:

1. the write-op qualifier binds the whole set (`:47` says so explicitly), and a partner writing in
   a facilitated sitting is not an op — registering one would be a false declaration, not a fix; and
2. nothing in the bundle tells a partner the route exists or when it applies.

So the honest statement is not "no route exists" but **"the only route requires the writer to be
something it is not, and is undiscoverable besides."**

**GAP CONFIRMED — the field measurement, and what it does and does not establish.** The filing
measured, before filing: 27 Layer 3 files outside the wiki subtree carrying `author: agent|hybrid`
with no pair, across six partners' domains; 5 carrying the pair, **all five written by an operation
skill**; zero partner-sitting-written Layer 3 documents attested, and none able to be. The
population spans the module's own shipped partner roster and vault-minted partners alike, over
~10 weeks of sanctioned work — so it is not one careless partner. Cycle 13's discharge run
independently confirms the 27 reproduced in the 0.16.1 sweep. Capture notes the limit: the counts
are `{field-vault}`-local and establish that the class is large and ordinary there; they do not
establish a rate for vaults generally, and the filing does not claim they do.

**Residual scope.** Both filing directions survive grounding; the precedent asymmetry is the
material fact for ideation:

1. **Widen the value set** — admit a partner identifier, or a sentinel meaning "verified in-sitting
   by the authoring partner." Keeps every Layer 3 artifact attested; weakens the field's current
   meaning (an op name, checkable against a roster) and owes a story for what the new value is
   checked against. Note this interacts with `local_consumers:` above rather than replacing it.
2. **Narrow the jurisdiction** — exempt partner-sitting writes in §Scope rule the way container
   files already are. **Has shipped precedent** (`extraction.md:188`), is honest about what the pair
   records today (that a *write op* ran its checklist), and is the cheaper edit. Cost: a real class
   of Layer 3 artifact stops being covered by any structural check.

Either direction changes a **rule** in `write-verification.md` and therefore bumps `version:` from
`3` and re-acks all five consumers in the same build (the version-handshake rule; the file is
currently unbumped at `3` with 5 consumers). A jurisdiction narrowing that only edits §Scope rule
is still a rule change, not a prose clarification. Ideation should price this in — Cycle 13 shipped
with no convention bump and no re-ack owed, and this cycle will not.

**Open design question, carried verbatim, not resolved here.** The filing flags its own
classification: *"Filed as a `defect` rather than a `pattern` because this instance blocks a
concrete write today; the maintainer may prefer to reclassify."*

**⚠ Cross-filing — a second instance of one shape, and a study candidate.** The filing names the
link itself: *"this may be the same shape as the open filing about the decision log's Writers
roster having no route for a shipped write op that legitimately discovers a deviation mid-run.
Both are **a closed roster meeting an actor the surrounding rules authorize.**"* That filing is
`factory/inbox/2026-08-21-150214-decision-log-writer-roster-admits-no-discovery-site.md`
(`origin: mggower/bmad-module-vlt#6`), captured into Cycle 10. Grounding confirms both are live
and the shape is the same. A14-6 is arguably a third instance in the vocabulary register rather
than the writer register.

**No study in `factory/studies/` holds this cause.** `ST-1`'s primary cause is adjacent —
*permission fused to provenance in one verb* — but it is about one verb's shape, not about closed
rosters meeting authorized actors, and reading A14-7 as ST-1 would flatten the distinction. Per
`factory/studies/README.md` *(Opening a study / Citable, never blocking)* this is recorded as a
**study candidate**: the cause is bigger than any of the three filings, and whether `ST-6` is
opened is the author's call and gates nothing. Naming it here so the third instance does not
re-derive it from scratch.

## Carried forward from Cycle 13 — live, grounded, un-built

Recorded in `factory/cycles/13-trusted-returns/roadmap.md` §Carried forward (ruled OUT of the
patch, not dropped) and orphaned by the v0.16.1 release under the ship-day capture boundary,
exactly as that section's ⚠ routing question predicted. They open here. **All three are defect or
posture work; none is net-new capability, so all three are admitted under §Owner ruling.**

1. **Finding 4 — the paraphrased verbatim field.** `vlt-lint-full.js:162` asks for the frontmatter
   `summary:` value *verbatim*; the agent returns a paraphrase and `:545` measures it faithfully,
   so the reported character count is wrong (`kettl` 168 vs an actual 156; `l-theanine` 162 vs
   159). **The blast radius is wider than `summary`** — every schema field marked verbatim is
   unguarded by the same argument, which A14-3 has now demonstrated on a second field with a
   different mechanism. Fixing it needs the real frontmatter value, which the workflow cannot read
   (`:36-38`), so it costs a SKILL-side per-page arg on the `pageHashes` precedent (`:47-49`) —
   **the #13 joint** (§Owner ruling).
2. **The general posture (Cycle 13 Q3's "true fix").** *Every agent-returned value that is
   mechanically checkable at the reduce is checked there.* The durable answer to A14-1, A14-2,
   A14-3 and carry 1 at once; larger than a patch. Cycle 13's discharge run recorded that **the
   evidence for taking it is materially stronger than it was on 2026-08-26 morning** — three of
   that sweep's four false findings came from the reduce trusting scanner-returned text.
3. **Retiring `malformed_frontmatter` itself** — named and deferred by Cycle 13 build-1's
   brief-time disposition 6, per P-15 (a retirement is named, never silently survived). Once the
   guard works, the class's genuine population is "schema breaks that are not attestation and not
   invented," which may be fully covered by the documented `frontmatter_drift`
   (`vlt-lint-full.js:573-575`). Not taken in build-1 because retiring a shipped finding class is a
   behavioral removal needing a **measured** population first — and Cycle 13's check (2) was to be
   that measurement. **It FAILED, so the measurement does not exist**: whatever build takes this
   must produce it, and the successor named by Cycle 13 is the build that takes carry 2.

## Cycle 12's six bounded tails — the bound landed on this run

Cycle 12 shipped v0.16.0 and its acceptance left six field-contingent checks open, each bounded to
**"Cycle 13's `inbox-capture`"**. Cycle 13's capture was a narrow patch capture that explicitly did
not trigger the attachment (Cycle 13 §Owner ruling — narrow-capture carve-out), and Cycle 13 is now
closed to capture without ever running a full batch. **This run is that batch, so the bound lands
here, today.**

None of the six is a defect, so under §Owner ruling none is admitted as Cycle 14 build scope. They
are recorded because their bounds are now due and three of them carry explicit no-re-carry text.

| tail | the check, in one line | status at the bound |
|---|---|---|
| b2(5) | the `churn`-ratio saving is real at live churn | unmet — needs a second live full sweep at low churn |
| b3(6) | `trust: raw` becomes representable and present in PARA (`ST-2`'s own test) | unmet — the `vlt-brief` shelf is parked pending A14-6 |
| b3(7) | a partner resolves a `{resources}`-write legality question from the rewritten bundle without escalating | unmet |
| b3(9) | a vault declares `writers:` on a container it had framed in prose | unmet — **no-re-carry** |
| b4(5) | a real park is recorded through the new `vlt-feedback` step | **arguably met** — see below |
| b4(6) | the next `vlt-upgrade` renders a **non-empty** `parked_interims_review:` | unmet, and coupled to b4(5) |

**b4(5) may in fact have discharged, and this run is the first evidence.** Its check is that a real
park is recorded through the new step, triggered by *"the owner's next `vlt-feedback` filing of a
blocker the vault holds an interim against."* Cycle 13's discharge run records **two live
`kind: parked-interim` entries against issues #15 and #16** — which are A14-6 and A14-7, filed
through the rail and materialized by this run's intake. The brief's own honest caveat was that
*"nothing in the plan schedules a new upstream blocker"*; two arrived anyway. **Capture does not
grade acceptance checks** — that is `acceptance-discharge`'s job against Cycle 12's ledger — but
the evidence now exists and the discharge run should be pointed at it. b4(6) is coupled and
becomes gradeable on the next `vlt-upgrade`.

**b3(9), b4(5) and b4(6) carry explicit no-re-carry text** (Cycle 12's A56 lesson): if unmet at the
bound, each *"routes to an owner ruling on whether the mechanism is graded on the at-rest evidence
alone — **not to a re-carry**."* That ruling is now due. It belongs to `acceptance-discharge` or
`cycle-closeout` over Cycle 12's ledger, **not to this cycle's ideation**, and it is named here so
the bound is not silently missed a second time.

## Also carried, not a filing

**`{field-vault}` overlay staleness, surfaced by the 0.16.1 upgrade** (Cycle 13 §Next lifecycle
move, item 4). `vault-operating-contract.overlay.md` §D's parenthetical names Layer-3 territory as
*"`{projects}` and `{areas}`"*; `{resources}` has been Layer 3 since 0.15.0. Report-only and
correctly not fixed by the upgrade — an overlay is vault-owned and append-only. **This is a
vault-side owner action, not module work**, and it is recorded here only so it is not lost.

**Owner action outstanding from Cycle 13** (unchanged, restated so it does not fall through): the
`{field-vault}` session had not run `vlt-feedback` for the 2026-08-26 sweep at the time Cycle 13's
roadmap was written. This run's intake shows #12–#16 did arrive on the rail and are now
materialized, so that action is at least partly discharged; A14-1..A14-3 remain factory-filed and
deliberately carry no `origin:` header — **do not re-file them upstream** (a rail copy would
materialize a second time; the `origin:` header is the only idempotency key).

## Open design questions — the batch's, not resolved by capture

Carried here so ideation sees them together rather than one filing at a time.

1. **Instances or posture?** A14-1, A14-2, A14-3 and Cycle 13 carry 1 are four faces of one seam.
   Repairing them individually reopens Cycle 13's gate soonest; taking Cycle 13 carry 2's general
   posture answers all four and the next one. The owner ruled at capture that this is
   **ideation-steered with the full cost in view**, not pre-ruled here.
2. **Does the posture re-admit #13?** Every mechanical-verification direction in this cycle needs
   ground truth the workflow structurally cannot fetch (`vlt-lint-full.js:36-38`), which means a
   SKILL-side per-page arg, which moves the joint against #13's ~84KB payload cost. If the posture
   is taken, #13 is a dependency, not net-new — and re-admitting it is an owner ruling.
3. **A14-6: pointer or vocabulary?** If `contract:66`'s missing pointer is the whole defect, the
   cycle is a one-line edit plus a handshake. If the two conventions must be reconciled, it is a
   vocabulary decision with `para_author_unknown` in the population too.
4. **A14-7: widen or narrow?** Narrowing has shipped precedent (`extraction.md:188`) and is
   cheaper; widening keeps structural coverage. Either bumps `write-verification.md` from
   `version: 3` and re-acks five consumers in the same build.
5. **Is "a closed roster meeting an authorized actor" a pattern worth naming once?** Three live
   instances (A14-7, the Cycle-10 decision-log Writers roster filing, and arguably A14-6). No study
   holds the cause; opening `ST-6` gates nothing and is the author's call.
6. **A14-4's qualifier.** Whether *"frontmatter is the source of truth"* needs re-scoping is a
   claim about `write-verification.md`'s tier-1 item, not only about a lint slot. Blast radius
   unmeasured.

## Next lifecycle move

**Owner-steered ideation** (`ideation-scaffold`, then the rulings section of this roadmap). The
grouping, order and scope rulings this cycle needs are named in §Open design questions above;
question 1 is the one that determines the cycle's size and should be ruled first, because
questions 2 and 6 depend on it.

Two constraints ideation must carry, both already grounded:

- **A14-1 gates Cycle 13's closeout.** Whatever build takes it should be ordered first and
  released first; Cycle 13 cannot close until it ships and its check (2) is re-graded.
- **A14-7 (and a widening reading of A14-6) forces a convention `version:` bump and a same-build
  re-ack of all five `write-verification.md` consumers.** Cycle 13 shipped with no bump owed; this
  cycle will not, and `build-brief` gates on the handshake being bipartite-consistent.

Per `factory/platform/spikes/README.md`, the Spikes section of ideation must be populated (P-2's
self-acceptance rides on a cycle running ideation with it filled). **No spike was opened by this
capture** — every claim in all seven filings was groundable against module source in the working
tree, and no grounding hit an external unknown.

After ideation rules, each ruled build goes to `build-brief` (`brief build N`). The roadmap
roundtable (`roadmap-roundtable`) runs over the filled rulings before the first brief, or is
waived by an explicit owner ruling recorded in this roadmap — `build-brief` gates on the record,
and silence is not a waiver.
