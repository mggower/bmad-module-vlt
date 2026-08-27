---
title: 'Cycle 14 — no enforcement point'
status: 'OPEN — captured 2026-08-26, **8 filings** grounded against module source at v0.16.1. **IDEATION COMPLETE** (four owner-steered rounds, every slot ruled): **4 builds, 2 releases** — b1 reduce-side (A14-1 + A14-3), b2 findings cache (A14-8), b3 governance (A14-6 + A14-7, 2 conventions / 15 re-acks **+ 7 in-prose pins the handshake gate cannot see; the roundtable found the true figure may be 3 conventions / 19 re-acks — settled at build-3''s brief**), b4 lint references (A14-4 + A14-5); **build-1 is released alone** because it **gates Cycle 13''s closeout**. Cycle-wide ruling D3, **as amended at the roundtable**: a **bounded** check (at rest, at the release gate, or on the next ordinary upgrade) is ship-verifiable and it GATES — an at-rest instrument is one sufficient bound, not the criterion. `ST-6` opened at D4. Scope was owner-ruled at capture — defects and blockers from Cycles 12–13 only, net-new deferred (tracker #13). **ROUNDTABLE COMPLETE 2026-08-26** — 32 amendments applied, 2 rules, 4 owner-ruled disputes (2 dissents on record), 0 open, 6 retirements; `build-brief`''s gate is satisfied. **RELEASE 1 SHIPPED 2026-08-27 — v0.16.2 @ `bd985a6`, tag `v0.16.2` (`594b958`), build-1 built at `ceb5cb2`; package-lint A/B/C/E PASS, D PASS.** Build-1''s 8 acceptance checks are ALL ship-verifiable and ALL GATE (D3-as-amended); **6 of 8 graded at rest, 6/6 PASS** — including **check (2), which re-grades Cycle 13''s refuted acceptance check on six real vault subjects: PASS. Cycle 13''s closeout gate is REOPENED.** Checks (6) and (7) bound to the first live full sweep after upgrade. **Next: two independent tracks — owner runs `vlt-upgrade` on `{field-vault}` for release-1 acceptance; and `brief build 2` toward release 2 (builds 2, 3, 4).** Predecessor Cycle 12 CLOSED 2026-08-26; Cycle 13 remains OPEN, now gate-open, awaiting its acceptance re-run.'
module_code: 'vlt'
created: '2026-08-26'
updated: '2026-08-26 (opened by inbox-capture; GitHub intake materialized 5 issues; 8 filings captured and graded; 1 deferred by owner ruling; Cycle 12''s six bounded tails ruled at the bound; **IDEATION COMPLETE — filled over four owner-steered rounds, every slot ruled: 4 builds, 2 releases, build-1 cut alone to reopen Cycle 13''s gate; ST-6 opened**; **ROUNDTABLE CONVENED + CONVERGED 2026-08-26 — full 13-voice roster, 32 amendments, 2 rules, 4 disputes ruled, 6 retirements, D5 confirmed**); **2026-08-27 — build-1 BRIEFED, BUILT @ `ceb5cb2` and RELEASED as v0.16.2 @ `bd985a6`, tag `v0.16.2` pushed to origin; 6/6 at-rest acceptance checks PASS incl. the Cycle 13 re-grade**; next: `vlt-upgrade` for acceptance + `brief build 2`)'
derives_from:
  - 'factory/inbox/2026-08-26-164500-reduce-guard-residue-rule-defeated-by-a-scanner-that-cites-its-rule.md'
  - 'factory/inbox/2026-08-26-164501-page-scanner-under-returns-outbound-links-and-manufactures-an-orphan.md'
  - 'factory/inbox/2026-08-26-164502-html-escaped-scanner-return-fails-an-exact-comparison.md'
  - 'factory/inbox/2026-08-26-123144-reclassify-sources-vs-prose-mismatches-out-of-fix-now.md'
  - 'factory/inbox/2026-08-26-123153-lint-mandates-strict-yaml-persist-with-no-yaml-library.md'
  - 'factory/inbox/2026-08-26-125529-recognized-type-names-no-owning-convention.md'
  - 'factory/inbox/2026-08-26-141418-layer-3-open-entry-vs-closed-verified-by-roster.md'
  - 'factory/inbox/2026-08-26-141838-findings-cache-cannot-round-trip-writer-and-reader-disagree.md'
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
that place is missing, unreachable, or cannot carry out the judgment the rule requires.**
*(roundtable A28, 2026-08-26 — restored to the `intent:` block's own trichotomy. The tidied
headline had dropped the **missing** case, which is the case the cycle is titled for: A14-4's
auto-fix procedure and A14-5's validator were never written, not written-and-unreachable. A brief
quoting the old sentence would scope A14-4 as re-wording an existing procedure rather than
authoring one.)* Not because the rule is wrong, and
not because the enforcement was forgotten — in every one of the eight captures below, the half
that was written was written deliberately and is individually defensible.
*(roundtable A27/A28, 2026-08-26: was "seven" and "both halves" — the capture holds eight, and
A14-4/A14-5/A14-8 are cases where the second half was never written at all.)* The defect is the *seam*.

Eight filings, three seams: *(roundtable A27, 2026-08-26)*

**The scan → reduce seam (A14-1, A14-2, A14-3).** `vlt-lint-full.js` fans out to LLM scanners and
reduces their returns with exact, careful JavaScript. The reduce has the arithmetic; it does not
have the page. All three of this sweep's false findings come from the reduce performing precise
work over a value it has no way to verify — prose (A14-1), an enumeration (A14-2), an encoding
(A14-3). The workflow's filesystem-free design (`vlt-lint-full.js:36-38`) is the structural
reason: it is what keeps the fan-out clean and it is what makes verification impossible from
inside. Cycle 13's own §Carried forward already named the general answer (*every agent-returned
value that is mechanically checkable at the reduce is checked there*) and deferred it once.
The field has now paid for that deferral three times in one sweep.

**The stated-mandate seam (A14-4, A14-5, A14-8).** A promise written into a schema or a reference with
nothing shipped that could keep it. `sources_vs_prose_mismatches` sits in the `fix_now:` slot —
the slot meaning *safe to apply serially without judgment* — and the auto-fix procedure it would
be applied by never mentions it (A14-4). `report.md` requires the persisted report parse as
strict YAML "whole, in both homes" and the module ships nothing that emits it and nothing that
checks it (A14-5). Both are the Cycle 13 premise one layer out from the workflow: an instruction
at a site with no enforcement point. **A14-8 is the seam's purest form and arrived after this
section was first written**: the findings cache's record shape is a contract stated in code on the
read side and in prose on the write side, meeting at a file on disk that nothing validates — so the
mechanism has never once worked, and no shipped instrument could see it.

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
an attestation it cannot legally hold. Fixing them as eight unrelated patches *(roundtable A27)* is available and is
what "instances only" means; the roadmap records that the option exists and that ideation, not
capture, rules on it.

## Owner ruling — debt-clearing scope (2026-08-26)

Ruled at capture, before grounding, and recorded here because it shaped what this run covered.

**The ruling:** Cycle 14 carries forward the **defects and blockers** from Cycles 12 and 13 only.
Lingering issues from the last two releases are closed out **before** any net-new capability
opens. Capture applied it as an admission test, not as a grading input — every filing this run
touched was still fully grounded.

**Admitted from the inbox at capture (7):** *(roundtable A27, 2026-08-26)* A14-1..A14-3 (the three defects the Cycle 13 discharge run filed), A14-4
(`kind: defect`), A14-6 and A14-7 (both blocking a live `{field-vault}` `parked-interim`), and
A14-5 — filed as `kind: candidate` but **owner-reclassified as a blocker at capture**: the module
mandates a machine-readable artifact and ships no means to produce it, on an environment class
(PEP 668) that is now the default rather than the exception.

**Deferred from the inbox (1) — NOT one of the eight captures:** `factory/inbox/2026-08-26-123151-lint-full-inline-args-payload-costs-the-caller-84kb.md`
(tracker **#13**) — a request for a new `argsPath` invocation route for `vlt-lint-full`. Net-new
capability; it stays in `factory/inbox/` un-captured and is **not** in this cycle's
`derives_from:`. Its issue is labeled `captured` on the tracker because the intake materialized
it this run; that label records materialization, not admission to this roadmap.

*(roundtable A27, 2026-08-26 — the arithmetic above is accidentally consistent with the wrong set.
**7 + 1 = 8 does not account for the eight captures.** The deferred one (#13) is not among them;
**A14-8 is admitted and uncounted here** (it arrived via Cycle 12's b2(5) tail, not the inbox
admission test); and the three Cycle 13 carry-forwards are admitted separately at §Carried forward.
**Eight captures, eleven admitted items.**)*

⚠ **The deferral is not clean, and ideation must see why.** Cycle 13 §Carried forward item 1
records that fixing the paraphrased-verbatim field "costs a SKILL-side per-page arg on the
`pageHashes` precedent (`:47-49`) — and that arg moves the joint against tracker **#13**'s payload
cost." The same is true of A14-2's and A14-3's mechanical-verification directions and of the
general posture. **Any resolution that gives the reduce ground truth needs a payload route, and
#13 is that route.** If ideation takes the posture, #13 stops being net-new and becomes a
dependency; the owner would then re-admit it by ruling. Capture does not pre-empt that — it
records the joint so the ruling is made with it in view.

## Capture — 8 filings (grounded against module source 2026-08-26, at v0.16.1 @ `c18c591`)

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
`parseClaim()` at `:593-603` normalizes the claim text (`:584` `normalizeClaim`, lowercase +
non-alphanumeric collapse), consumes every recognized frontmatter key longest-first from
`KNOWN_FRONTMATTER_BY_LENGTH` (`:580`), and returns whatever survives the `CLAIM_FILLER` strip
(`:589`) as `residue`.

*(roundtable A29, 2026-08-26 — four cites corrected against working-tree source. As written the
entry gave `:591` for **both** `normalizeClaim` and `CLAIM_FILLER`, asking one line to carry two
constants, and `:579` for `KNOWN_FRONTMATTER_BY_LENGTH` (that line is its comment). Small in
itself; **not small in a build whose scope is "retire these exact lines"**, under a header
asserting every cite was re-derived. Build-1's brief re-derives every `file:line` at brief time.)*

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

**⚠ SUPERSEDED 2026-08-26 by D4 — `ST-6` IS OPEN and holds this cause.** *(roundtable A36,
2026-08-26; Dr. Quinn)*. Read
`factory/studies/ST-6-closed-rosters-meet-authorized-actors.md` — registered in
`factory/studies/README.md`, opened this session, written from the pre-repair state — **not this
paragraph's candidate framing.** The paragraph below is kept for provenance only, and it matters
because **E5 orders build-3's brief to write A14-6/A14-7 from this very section.**

**No study in `factory/studies/` holds this cause.** `ST-1`'s primary cause is adjacent —
*permission fused to provenance in one verb* — but it is about one verb's shape, not about closed
rosters meeting authorized actors, and reading A14-7 as ST-1 would flatten the distinction. Per
`factory/studies/README.md` *(Opening a study / Citable, never blocking)* this is recorded as a
**study candidate**: the cause is bigger than any of the three filings, and whether `ST-6` is
opened is the author's call and gates nothing. Naming it here so the third instance does not
re-derive it from scratch.

### A14-8. The findings cache cannot round-trip — the writer and the reader disagree, and no instrument can see it (2026-08-26) — `factory/inbox/2026-08-26-141838-findings-cache-cannot-round-trip-writer-and-reader-disagree.md`

*Captured the same day the cycle opened, from a `{field-vault}` session run deliberately as Cycle
12 b2(5)'s acceptance test. It joins the opening Capture rather than a mid-cycle addendum: this
cycle's batch has not been ideation-ruled or roundtable-stamped, so the addendum posture does not
apply. **It refutes b2(5), which was graded FAILED in Cycle 12's ledger the same day** — the
authoritative record is `factory/cycles/12-proxy-claims/roadmap.md` §Owner ruling — the six bounded
tails at their bound.*

**CONFIRMED — Defect 1, the sidecar schema mismatch, and the root cause is the spec.**
The reader requires `{slug, key, scan}`: `vlt-lint-full.js:243` filters
`cachedScans.filter((c) => c && c.slug && c.key && c.scan)` and `:344` dereferences
`cacheBySlug.get(p.slug).scan`. The spec tells the SKILL to write something else —
`skills/vlt-lint/references/full-scale.md` step 5, findings-cache sub-bullet: *"one record per page
adjudicated this run — the workflow's returned `fresh_scans`."* But `fresh_scans` is the array of
**raw PAGE_SCAN returns** (`:293` pushes the agent's `r` unmodified; `:723` returns it as-is), which
carry no `key` and are not wrapped. **Following the spec literally produces a sidecar the reader
discards whole.** On disk: `_agent/lint-cache.yaml` holds 146 flat records and
`grep -c "^    key:"` returns **0**.

The key is derivable — `:722` returns `cache_fingerprint` as exactly
`${scanFingerprint}|${rulesetFingerprint}`, and `:242`'s `runKey` is
`${pageHashes[slug]}|${scanFingerprint}|${rulesetFingerprint}`, so the correct record is
`{slug, key: "${pageHashes[slug]}|${cache_fingerprint}", scan: <entry>}`. **That derivation is
nowhere in the spec** and must be reverse-engineered from workflow source by every implementer.

**Sharpened — the written sidecar is lossy, not merely mis-nested.** It stores `fingerprint:` once
at the top level (`_agent/lint-cache.yaml:1`) and **no per-page digest anywhere**, so it cannot
express the reader's key even in principle. A reader-side fix alone cannot rescue an existing
sidecar; the file has to be rewritten. Worth knowing before anyone proposes tolerating the flat
shape.

**CONFIRMED — Defect 2, `rulesetFingerprint` has no deterministic algorithm.** `full-scale.md`
step 2 enumerates the inputs in order — `module_version`; the skill's `depends_on:` pin vector
verbatim; each judged convention's digest **as merged with its overlay**; the digest of
`references/checks.md` — and specifies **no digest construction**: no separator, no hash algorithm,
no encoding, no truncation, no canonical member list. Two runs over an identical ruleset therefore
compute different values; the field observed `980d749d9acf418e` against an independent
`66d27a0e6cd8fabe` over a provably unchanged ruleset. Since `reusable()` (`:244-245`) requires
`rulesetFingerprint` non-empty **and** an exact key match, **the cache is structurally incapable of
hitting across sessions — the only case it exists for.**

**GAP CONFIRMED — the failure is invisible to every shipped instrument, and that is the durable
finding.** The version-skew defence (`full-scale.md` step 4) refuses only when `files_checked`
**and** `files_cached` are **both** `0`. A run that cold-scans everything *because the cache is
broken* reports `files_checked: 146` — full coverage, honest report, no refusal — and is
indistinguishable from a healthy cold run. **Nothing checks that a cache written by run N is
readable by run N+1.** Every instrument reports the cache's *counts*, never its *round-trip*.

**This is the cycle's through-line, and A14-8 is its cleanest instance.** A contract stated in one
place (the reader's filter, in code) and restated as prose in another (the spec's write
instruction), with **no enforcement point where the two meet**. The seam is a file on disk that
nothing validates. Defect 2 is the same shape at one remove: an algorithm *described* for each
caller to re-derive rather than single-homed as executable steps — the `ST-3` cause (governance has
no machine-addressable projection) reappearing as a fingerprint with no machine-addressable
definition.

**Cites `ST-5`, and sharpens it with the cleanest specimen the register has.** Build-2's
ship-verifiable checks (1)–(3) proved the cache on a two-run temp fixture **inside one harness
invocation, where the SKILL-side write step never ran because the harness stubbed it**. The one
seam that breaks in the field is precisely the one the at-rest instrument could not exercise —
ST-5's second cause, exactly. And the compounding half: **the field check that would have caught it
was b2(5), tagged field-contingent and therefore non-gating** — ST-5's third cause (*one tag
resolves a check's blocking power from its grading modality*). Cycle 12 shipped a mechanism that
has never once worked, on a green ship-verifiable ledger. Append this capture to ST-5's `cited_by:`.

**Residual scope.** Five directions, the field's own, re-ordered by grounding:

1. **Move the wrapping into the workflow** — return write-ready `{slug, key, scan}` records instead
   of raw `fresh_scans`, so read and write shapes cannot drift apart again. Preferred over
   documenting the derivation: it removes the seam rather than describing it.
2. **Move `rulesetFingerprint`'s computation into the workflow**, or single-home it as executable
   steps (canonical member order, separator, digest, truncation). Same argument.
3. **A round-trip acceptance check** — write the sidecar, read it back, assert every record is
   reusable against an unchanged corpus. This is what the cancelled sweep manually stood in for,
   and its absence is what made both defects invisible. **Ship-verifiable at rest**, so it can gate.
4. Amend `full-scale.md` step 5 to state the record shape and key derivation explicitly — the
   fallback if 1 is not taken.
5. **Widen the step-4 refusal predicate** (or add a distinct signal) so "cold because the cache was
   unreadable" is distinguishable from "cold because the ruleset legitimately moved."

**Note for ideation — this one is cheap and it is not on the #13 joint.** Unlike A14-1..A14-3 and
Cycle 13 carry 1, nothing here needs the reduce to read page bytes. `pageHashes` already crosses the
seam (`:47-49`), the workflow already returns `cache_fingerprint`, and every fix is a shape or a
single-homing. It is the one entry in this cycle that can be taken without ruling question 2 first.

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

## Cycle 12's six bounded tails — the bound landed on this run, and was ruled

Cycle 12 shipped v0.16.0 and its acceptance left six field-contingent checks open, each bounded to
**"Cycle 13's `inbox-capture`"**. Cycle 13's capture was a narrow patch capture that explicitly did
not trigger the attachment (Cycle 13 §Owner ruling — narrow-capture carve-out), and Cycle 13 is now
closed to capture without ever having run a full batch. **This run is that batch, so the bound
landed here.**

**The tails were ruled in the same session, against evidence re-gathered from `{field-vault}` at
the bound rather than from the ledger's last-known state.** The authoritative record — grades,
reasoning, and the superseded ledger notes — is single-homed at
`factory/cycles/12-proxy-claims/roadmap.md` §Owner ruling — the six bounded tails at their bound
(2026-08-26). It is **not** restated here. Outcome only:

| tail | the check, in one line | outcome at the bound |
|---|---|---|
| b2(5) | the `churn`-ratio saving is real at live churn | **FAILED** — the corrected bound was tested the same day and refuted; filed and captured as **A14-8** |
| b3(6) | `trust: raw` representable-and-present in PARA (`ST-2`'s own test) | **DISCHARGED on substance** (owner ruling) — the ledger's evidence note was stale |
| b3(7) | a partner resolves a `{resources}`-write legality question without escalating | **STILL OPEN** — needs owner observation; no disk evidence either way |
| b3(9) | a vault declares `writers:` on a container it had framed in prose | **CLOSED by owner ruling** — A33's notification sufficient, no re-carry |
| b4(5) | a real park recorded through the new `vlt-feedback` step | **DISCHARGED** — two parks, both against rail-filed blockers |
| b4(6) | the next `vlt-upgrade` renders a non-empty `parked_interims_review:` | **DISCHARGED** — first live non-empty render |

**Five of the six do not enter Cycle 14 as build scope** — none of those five is a defect, and
§Owner ruling admits only defects and blockers. **b2(5) is the exception: it FAILED**, and the
defects behind it enter as **A14-8**. Cycle 12's field-contingent ledger stands at **7 of 11
discharged, 1 FAILED**, and holds no no-re-carry item.

**Three things this cycle inherits from the ruling, none of them build scope:**

1. **A14-6's filing is stale against its own vault, and its capture should be read knowing that.**
   Tracker #15 describes moving the `vlt-brief` shelf to a `{resources}` address as prospective;
   the shelf has been at `resources/briefs/` since before the 2026-08-26 10:46 lint, which
   enumerates all five issues by path in `para_type_unknown`. The defect A14-6 reports is
   unaffected — the two conventions still disagree — but the framing *"moving the shelf today
   would put files into the PARA population"* is past tense, and the files are already there under
   a recorded park.
2. **b3(7) interacts with A14-6 and A14-7.** Both are live parks against the same bundle, so a
   partner attempting a `{resources}` write today may legitimately escalate — which would not be a
   failure of the rewritten bundle but of the two vocabularies it is waiting on. b3(7) is
   effectively ungradeable until those two rule.
3. **The b3(9) population problem is `ST-5` material.** A field-contingent check whose discharging
   population was a *single vault artifact* was not gradeable in the field on the day it was
   written. Named in the Cycle 12 ruling; carried here so the instrument work has the third
   instance.

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

## Ideation rulings — A14-1..A14-8 (owner-steered, 2026-08-26)

**Rulings below are the owner's; briefs cite this section, never re-litigate.** Session
**COMPLETE — filled 2026-08-26 over four owner-steered rounds. Every slot is ruled.**
`build-brief` gates on this section being filled — it is.

**What each round settled.**

- **Round 1 — the cycle's size.** The reduce-side posture is taken **where it needs no new
  inputs**: A14-1's claim return is **restructured** and A14-3's seam **entity-decoded**, while
  A14-2 and the `summary` paraphrase — the only two faces needing real page bytes — are deferred.
  Tracker **#13 stays deferred** as a consequence. And **an at-rest instrument now means the check
  GATES** (D3) — the cycle-level answer to what let b2(5) ship a mechanism that never worked.
- **Round 2 — the governance pair.** A14-6 is a **pointer**, not a vocabulary fight: the closed set
  governs the PARA population and `contract:66` names it, at zero handshake cost. A14-7 narrows
  jurisdiction **by artifact class**, extending `extraction.md:188`'s shipped principle rather than
  adding a writer-shaped axis.
- **Round 3 — the costs.** **Two conventions move in one build**, by *elimination* not precedence
  (15 re-acks). A14-8 **removes both seams** rather than documenting them, with an in-session
  correction to what "move the fingerprint into the workflow" can actually mean. The
  `malformed_frontmatter` retirement **defers a third time — but ships its measurement**.
- **Round 4 — the shape.** `.json` becomes a legal persist because **`json` is stdlib and `yaml` is
  not**, which is what makes A14-5's claim checkable at all. **Four builds, two releases**, build-1
  cut alone so Cycle 13's gate reopens without waiting on a 15-re-ack handshake. **`ST-6` opens
  now**, written from the pre-repair state.

Seeded from the Cycle 14 capture run (2026-08-26, 8 filings). Question numbering is the clerk's,
for in-session reference only; it implies no ordering or priority.

**Two constraints the capture established that ideation inherits rather than decides:**

- **A14-1 gates Cycle 13's closeout.** Cycle 13 shipped v0.16.1 and FAILED acceptance check (2)
  by owner ruling on live field evidence; it is closed to capture and has no discharge path left.
  Only a shipped repair moves it. Whatever build takes A14-1 is the one that reopens Cycle 13.
- **A14-7 — and A14-6 under a widening reading — forces a convention `version:` bump and a
  same-build re-ack of every consumer.** `write-verification.md` is at `version: 3` with 5
  consumers. Cycle 13 shipped with no bump owed; this cycle will not. See D2.

### Grouping & order

**Ruled Round 4 (2026-08-26): four builds, two releases. Order 1 → (2, 3, 4).**

**Release plan.** **Release 1 = build-1 alone.** It is the only thing that reopens Cycle 13's
closeout gate, and cutting it alone keeps that repair off the critical path of build-3's
15-re-ack handshake. **Release 2 = builds 2, 3, 4** together.

*Cycle-wide, ruled: **every check every brief writes obeys D3** — **as amended at the roundtable
(A17): a BOUNDED check (at rest, at the release gate, or on the next ordinary upgrade) is
ship-verifiable and it GATES; an at-rest instrument is one sufficient bound, not the criterion.**
Every brief additionally states, per ship-verifiable check, **which seam its named instrument
actually crosses** (R1). And **the first full lint after either release is COLD by construction**
(build-1 moves `scanFingerprint`, build-2 rewrites the record shape, build-3 moves two convention
digests, build-4 moves `checks.md`'s) — briefs state it up front so it is never discovered as a
regression. ⚠ **The two-release plan therefore costs TWO cold full sweeps, not one** (roundtable
A26) — accepted knowingly as the price of reopening Cycle 13's gate early; see §Next lifecycle move
for where `{field-vault}` should pay its owed sweep.*

- **build-1 — reduce-side: A14-1 (the guard) + A14-3 (the encoding).** ⚠ **Gates Cycle 13's
  closeout.** Replaces the free-text claim with a structured `PAGE_SCAN` return (retiring the
  residue rule at `:593-603` and both predicates' `residue === ''` conjunction), and entity-decodes
  the category seam on **both** sides (`s.category` and `h2set` at `:643`). Carries the
  `malformed_frontmatter` **population measurement** per Q8.
  - `binds:` Q1, Q7, Q8, **E4**, D1, D3, D5 *(roundtable A20 — E4 is the cycle's only
    build-discharged debt and was the only E absent from a `binds:` list)*
  - `spike:` none

  **⚠ `attestationOnlyComplaint()` has TWO call sites, not one** *(roundtable A2, 2026-08-26 —
  verified in session; `:664` appears nowhere in the capture or the rulings)*. `:701`
  (`malformed_frontmatter`, via `refusedFrontmatterClaim` at `:630`) is the one Q1 structures.
  **`:664` filters `unmarked_supersession` — an array of free-text strings Q1 does NOT structure**,
  and the comment at `:659-663` records why the guard is there: *"A13-1 Finding 1's sixth entry (an
  attestation complaint) arrived here after the same prompt-side prohibition was ignored."*
  As ruled, build-1 either leaves the whole `parseClaim`/`CLAIM_FILLER` machinery standing for
  `:664` — so Q7's "the comment goes with the guard" is **false** and the residue rule is not
  retired — **or deletes it and silently regresses A13-1 Finding 1. Neither is a decision anyone has
  made. The brief must rule `:664` explicitly**: structure `unmarked_supersession` too, keep the
  parser scoped to `:664` alone, or retire the guard with its reason on record. **Q7's retirement of
  `:559-561` is conditional on that ruling.**

  **Retirement list, completed and named (P-15)** *(roundtable A37, 2026-08-26)*. Retires with the
  residue rule: `parseClaim` (`:593-603`), `fieldsNamed` (`:605`), `KNOWN_FRONTMATTER_BY_LENGTH`
  and its `:579` comment (`:580`), `normalizeClaim` (`:584`), `claimWords` (`:585`), `CLAIM_FILLER`
  (`:589`), and **the `frontmatter_issue` free-text schema slot itself (`:163`)** — each exists only
  to parse prose the structured return no longer sends. **`PAGE_REQUIRED_FRONTMATTER` and
  `PAGE_OPTIONAL_FRONTMATTER` SURVIVE** — they carry a live second role at `:563-568`, and the
  opposite error (deleting them by association) was equally available from the old text. A
  ship-verifiable check greps that none of the retired symbols survives.

  ⚠ **SUPERSEDED IN PART — grounding correction at brief time (2026-08-26, `build-brief`)**, recorded
  per `grounding-at-brief-time.md`'s two-place rule. Re-derived against working-tree source at
  v0.16.1 (`c18c591`), the file being `skills/vlt-setup/assets/workflows/vlt-lint-full.js`, 724 lines:
  - **`CLAIM_FILLER` is at `:591`, not `:589`** — `:586-590` is the residue-rule comment. (A29
    corrected four cites in this region and this one survived the pass.)
  - **`parseClaim` is at `:594-604`, not `:593-603`** — `:592-593` is its comment. (Q1 ruling 1
    already carried `:594-604`; §Grouping's list carried `:593-603`. The former is right.)
  - **`KNOWN_FRONTMATTER_BY_LENGTH`'s comment spans `:578-579`**, not `:579` alone.
  - **`PAGE_REQUIRED_FRONTMATTER` / `PAGE_OPTIONAL_FRONTMATTER` have NO live *code* role today** —
    `:563-568` is a **comment block**, and every code reference to the two sets is inside the
    machinery A37 retires (`:577`, `:614-615`, `:625-626`). Their survival is therefore something
    build-1 must **make true**, not merely preserve: the brief rules that the rewritten dispositions
    classify `frontmatter_defect_fields` against these sets directly (set containment replacing
    `fieldsNamed`). **Grounding addition:** `KNOWN_FRONTMATTER` (`:577`) is dead once `:580` goes and
    joins the retirement list as an eighth symbol; `ATTESTATION_FRONTMATTER` (`:576`) survives.
  - **`:664` RULED** (A2's third option): the guard is **retired**, because once the predicate takes
    a structured record it cannot be applied to a free-text string at all. Structuring
    `unmarked_supersession` is refused on **measured** grounds — `PAGE_SCAN` closes at **3688 of
    3700** after the ruled repair — and would flip the deferred `:168` dissent into a ruling, which
    is ideation's act. `:559-561`'s retirement (Q7) is therefore unconditional. Compensations on
    record: `:168` KEPT (A-R1), an R1 interim posture, and a gating acceptance check that **measures**
    the A13-1 Finding 1 exposure and decides §Carried forward item 9.
  - **Schema budget re-measured with package-lint's own `_E6_NODE_EXTRACTOR`**: baseline **3598**
    (A1 confirmed); the brief's ruled shape lands at **3688 ≤ 3700**, paid for by retiring
    `frontmatter_valid` (`:159`) **whole** as well as `frontmatter_issue` (`:163`).
  - **Scope is otherwise unchanged.** Brief:
    `factory/cycles/14-no-enforcement-point/briefs/build-1-structured-claim-return.md`.

  **⚠ RETIRES `:159`; KEEPS `:168` — owner ruling, roundtable 2026-08-26** *(roundtable A-R1)*.
  `:159`'s prohibition (208 chars) becomes **unexpressible by construction** once the disposition is
  an enum — the enum's range excludes the route rather than forbidding it in prose — and **its 208
  characters are load-bearing against the E6 ceiling (A1)**. **`:168` is KEPT and becomes
  load-bearing again**: Q1 leaves `unmarked_supersession` free-text and build-1 removes its
  reduce-side guard at `:664`, so `:168` is **not defence in depth — it is the only depth.**
  **DISSENT ON RECORD (Victor, Amelia):** `vlt-lint-full.js:551-557` states that Cycle 12 build-1
  shipped exactly that prohibition and *"the very next two full sweeps reported the defect
  unchanged"*, and D1 rules in this same cycle that a schema description is never an enforcement
  point — so keeping one as an enforcement layer is a contradiction the cycle ships against itself.
  **The dissent is deferred, not resolved: `:168` survives only as long as `:664` does, and the
  moment `unmarked_supersession` is structured the dissent becomes the ruling.**

  **⚠ Also carries the check that re-grades CYCLE 13's acceptance check (2)** *(roundtable A21,
  2026-08-26)*. The sole justification for cutting build-1 alone is that it reopens Cycle 13's gate
  — **and no ruling asked for a check that actually re-grades it.** Cycle 13's (2) was refuted **at
  rest** on shipped source, so its re-grade is at-rest, bounded, ship-verifiable and **GATES**.
  Without it, **release 1 could ship and Cycle 13 still not close.**

  **Touches** `vlt-lint-full.js` **and `skills/vlt-lint/references/checks.md`** *(roundtable A38,
  2026-08-26)* — `checks.md:15` carries **the same refuted over-reporting safety claim** in the
  vault-facing catalogue and additionally documents the conjunction/residue mechanism build-1
  removes. Q7 retires the claim at `:559-561` and would leave the shipped, vault-read copy asserting
  it. No new cost: `checks.md`'s digest already moves the ruleset fingerprint and build-1 is cold by
  construction.

- **build-2 — the findings cache: A14-8.** Workflow returns write-ready `{slug, key, scan}` records
  **for every page adjudicated this run — fresh AND reused** *(roundtable A6)*; fingerprint
  **composition** moves into the workflow (components still computed SKILL-side — see Q6's
  in-session correction); the round-trip check ships and **gates**. Touches `vlt-lint-full.js` and
  `full-scale.md` (**`full-scale.md` is shared with build-4 — one brief owns the file, the other
  cites it**, roundtable A8).
  - `binds:` **Q1**, Q6, D3 *(roundtable A4 — Q1 was missing and it defines the object build-2 caches)*
  - `spike:` none

  **⚠ NOT "independent of build-1 in substance" — it DEPENDS on it** *(roundtable A4, 2026-08-26)*.
  The `scan` payload build-2 wraps **is** build-1's structured `PAGE_SCAN` return, and
  `scanFingerprint` (`:232-233`, derived from `pageScanPrompt(...) + JSON.stringify(PAGE_SCAN)`) is
  a **key component** build-1 moves. A brief working build-2 from `Q6, D3` alone would build its
  fixture against the **pre-build-1 schema** and ship a gating check proving the wrong shape
  round-trips. **Interface, stated rather than assumed:** build-1's `PAGE_SCAN` change invalidates
  every release-1-era sidecar record, and **build-2's composition move MUST keep `scanFingerprint`
  a term of the composed key** — the SKILL supplies only the ruleset-side components. Nothing in the
  record said so, and the brief-time question ("list or pre-joined string") makes dropping it
  available. A ship-verifiable check asserts a record keyed under a different `PAGE_SCAN` is **not**
  reusable.

  **⚠ Q6.1 as ruled fixes only HALF the sidecar** *(roundtable A6, 2026-08-26)*. `:723` returns
  fresh records only; `:248`'s `reused` surfaces solely as the count `files_cached`; and
  `full-scale.md` step 5 tells the SKILL to write back *"the reused records that are still valid"* —
  where validity is `key === runKey(slug)` and `runKey` embeds `scanFingerprint`, **a
  workflow-internal value the SKILL structurally cannot compute** (`:36-38`). So *"the read shape
  and the written shape cannot drift apart again"* is true of **a warm run's fresh records only**.
  The workflow must return records for every adjudicated page so the SKILL never re-derives
  reusability it cannot compute.

  **⚠ The round-trip fixture must be THREE runs and its writer must be executable** *(roundtable
  A5, 2026-08-26)*. Two independent faults. (a) A two-run fixture (cold → warm) **cannot observe
  reused-half loss**: if run 2 drops the reused records the sidecar empties and the check still
  passes — a **third** run is what fails. The fixture is **cold → warm → warm**, asserting record
  count and per-record reusability are stable across runs 2 and 3. (b) A14-8's own capture records
  why b2(5) shipped broken: *"a two-run temp fixture inside one harness invocation, where the
  SKILL-side write step never ran because the harness stubbed it."* **After Q6 the write side is
  still SKILL-side prose** — `:719-723` says *"This workflow stays READ-ONLY — it returns the
  records, the SKILL persists them"* — so a JS round trip grades workflow-return → workflow-consume
  and **stubs exactly the seam that broke.** The brief must either move the sidecar **write** into a
  shipped script so the round trip runs end-to-end, **or** record that the SKILL-side serialize/merge
  step is **not covered** and tag a second check for it. **A round trip that stubs the writer does
  not discharge A14-8 and must not be tagged ship-verifiable under D3.**

  **⚠ Q5's format reasoning applies to the sidecar too** *(roundtable A7b, 2026-08-26)*.
  `_agent/lint-cache.yaml` is hand-emitted by an LLM and hand-read by the SKILL on the same PEP 668
  machines — **the identical property Q5 rules on for the report — and build-2's check GATES on it
  round-tripping.** Two rulings in one cycle reach opposite conclusions about the same problem on
  two files, and **the one that gates got the harder format.** The brief rules whether
  `_agent/lint-cache.{yaml,json}` follows Q5's `.json` permission.

  **⚠ Returns a `cache_rejected:` count** *(roundtable A39, 2026-08-26)* — the number of records
  discarded by the `:243` filter, rendered in the report. `full-scale.md` step 2 **already mandates**
  that *"a missing, unparseable or schema-mismatched sidecar is a cold run, **stated in the
  report**"* — this cycle's through-line verbatim, with no enforcement point, and it is what failed
  in the field. The round-trip check gates the **module at rest**; it cannot observe a **vault**
  whose sidecar is schema-mismatched. This costs no new argument and is **not** the step-4 widening
  Q6 declined — that refusal predicate stays as ruled.

- **build-3 — governance: A14-6 (the `type:` vocabulary) + A14-7 (the `verified_by` roster).** The
  handshake build. `write-verification.md` 3 → 4 (5 re-acks) + `frontmatter.md` 13 → 14 (10
  re-acks) + the `contract:66` pointer (no bump). **15 re-acks, one bipartite-consistency check.**
  `extraction.md` does **not** move — **but see A15: D2's own grounding may force it to.**
  - `binds:` Q3, Q4, D2, D3, D4, E3, E5
  - `spike:` none

  **⚠ ALSO TOUCHES `vlt-lint-full.js` — this is the THIRD build in that file, and the first to
  re-enter it after release 1 has shipped** *(roundtable A3, 2026-08-26 — found independently by
  nine voices; the block named no files at all)*. The workflow is a listed `consumers:` entry of
  **both** bumped conventions, so build-3 must edit **the `:11` `depends_on:` ack line — which
  package-lint **E5** parses, and the release fails if it is missed** — plus **seven in-prose
  version citations** at `:158`, `:159`, `:164`, `:168`, `:215`, `:571`, `:573`.
  **Nothing catches those seven.** Verified in session: package-lint's **E3** stray-pin check scans
  `skills/vlt-*/SKILL.md` and `skills/vlt-*/references/*.md` and **deliberately excludes
  `vlt-setup/assets/**`** (`tools/package-lint.py:736-739`, comment verbatim). So build-3 can bump
  both conventions, re-ack all 15, **pass the gate green, and ship seven stale citations to every
  vault. The handshake's enforcement point cannot see the sites that restate the rule — this cycle
  is named for that.**
  Worse than staleness: **`:159`, `:164` and `:168` are the workflow's restatements of §Scope rule —
  the rule Q4 amends** — so they are **content re-checks, not version-string bumps**, and by this
  cycle's own D1 they are unenforced copies of a moving rule. And **`:158`/`:159`/`:164`/`:168` sit
  inside `PAGE_SCAN`**, so any edit to them re-enters A1's 102-char budget and moves
  `scanFingerprint`. **Build-3 rebases onto build-1's rewrite of that file (several of these lines
  build-1 rewrites or retires first), writes its re-ack against post-build-1 source rather than
  v0.16.1, and re-runs E5 AND E6.** Ordered after build-2 so `PAGE_SCAN` settles once before the
  re-ack pass reads it.

  **⚠ Also touches `skills/vlt-lint/references/checks.md:17`** *(roundtable A11b, 2026-08-26)*.
  `checks.md:17` carries `para_missing_attestation`'s **"Population carve-out"**, restating the
  container exemption in the check's own words — **it is where §Scope rule actually binds.** Q4 adds
  a second exempt class and neither build-3 nor build-4 adds it there. Ship that and **the
  convention exempts a class the shipped net still flags with no route to clear it — A14-7's exact
  shape relocated one file over.** The convention states the jurisdiction; the check is where it binds.

- **build-4 — lint references: A14-4 (`sources_vs_prose` misclassification) + A14-5 (the persist
  mandate).** A14-4 adds the second legal response and the direction routing, **and the Step-3
  procedure entry that does not exist today**; A14-5 rewrites `report.md:3`'s both-homes sentence
  and permits `.json`.
  - `binds:` Q5, D3, E1, E2
  - `spike:` none

  **⚠ "Paired because both land in `report.md`" is FALSE — the persist mandate does not live there**
  *(roundtable A8, 2026-08-26 — found independently by five voices)*. **Touches:**
  `skills/vlt-lint/references/report.md`; **`skills/vlt-lint/SKILL.md:74`** — the persist step's
  **single home** (*"write the Step-5 report block **verbatim** to
  `{lint_reports}/YYYY-MM-DD-HHMM-lint.yaml` — plain YAML"*), of which `report.md:3` is only a
  restatement, so permitting `.json` in the restatement **inverts the pointer** and leaves the
  executing skill mandating the other format; **`skills/vlt-lint/SKILL.md:76`** and
  **`references/full-scale.md` step 4** (`-lint-failed.yaml`, a second report class that stays
  YAML-only and un-checkable — **Q5's argument buys it nothing**); **`skills/vlt-setup/SKILL.md:194`**
  (provisions the directory as *"plain `.yaml`"*); **`references/full-scale.md:13`**, where
  `churn_since_last_full` locates the previous full report **"by its dated filename"** — **a
  `.json`-persisting vault is invisible to that discovery and renders `unmeasured (no prior full
  report)` forever, a silent wrong number rather than an error**; and **`references/fix-and-file.md`
  Step 3** for A14-4's missing procedure entry. **`full-scale.md` is shared with build-2** — one
  brief owns the file, the other cites it.
  ⚠ Note a `.json` persist is **not a verbatim copy of the fenced block — it is a translation**, a
  second authoring act `SKILL.md:74`'s word *verbatim* forbids. The brief says which act emits which
  home, or **the cycle ships a permission with no emission point.**

  **⚠ SHIPS THE VALIDATION BEAT — gating** *(roundtable A10, 2026-08-26)*. The capture's own
  top-ranked direction for A14-5 was *"(1) a **validation beat**, not an emitter — the gap is the
  unchecked claim."* Q5 adopts (2) and (3) and says `.json` *"is what **lets** it carry a gating
  at-rest check under D3."* **"Lets" is not "does": D3 binds every check a brief writes; it does not
  require one to exist.** As ruled, build-4 could ship a rewritten `report.md:3` and no parse check
  — **a restated rule with no enforcement point, in the cycle named "no enforcement point", curing a
  filing whose defect is a stated rule nothing checks.** Build-4 ships a check that **parses a
  persisted report whole**; at rest ⇒ ship-verifiable ⇒ it **GATES**.
  Brief-time, added: **if `.yaml` remains a legal persist the check must cover it** (which costs a
  `machine_tools` row) **or the mandate is explicitly scoped to `.json`**; and whether the
  failed-run record and the `churn_since_last_full` lookup accept both extensions.

**Deliberately NOT in this cycle, and where each went:** A14-2 (outbound-link enumeration) and
Cycle 13 carry-forward 1 (`summary` paraphrase) — the two faces needing real page bytes, deferred
by Q1 to the build that takes the args route; tracker **#13** — stays deferred per Q2, and becomes
that build's dependency; the `malformed_frontmatter` **retirement** — deferred per Q8, with its
measurement attached to build-1; the step-4 refusal predicate widening — declined in Q6;
**A14-4's *"frontmatter is the source of truth"* qualifier (E2)** — scoped out unmeasured, **filed
to `factory/inbox/` by the owner as a `pattern`** so a later capture grounds it, and carried at
closeout as a deferred question *(roundtable A32)*.

⚠ **A14-2 is captured but UNBUILT, and its filing STAYS in `factory/inbox/` at closeout**
*(roundtable A23, 2026-08-26; John)*. A14-2 is in this cycle's `derives_from:` **with no build and
no ledger clause**, and `cycle-closeout`'s Stage-5 move criterion passes it **vacuously**:
condition 1 (*"every clause traceable to that filing is discharged"*) is trivially true over **zero**
clauses, and condition 2 — the checklist's own warning bound — **cannot bind where there is no
build**. **A literal closeout would `mv` an unrepaired defect out of the active inbox into
`14-no-enforcement-point/filings/`.** Stage 5's criterion does not apply to a filing with no build,
and **clause 1 must not be read vacuously over zero clauses.**

### Pre-ideation rulings the capture demanded

- **Q1 — instances, or the posture?** A14-1, A14-2, A14-3 and Cycle 13 carry-forward 1 are four
  faces of one seam: the reduce performing exact work over agent-returned values it cannot verify.
  Repairing them individually reopens Cycle 13's gate soonest; taking Cycle 13 carry-forward 2's
  general posture (*every agent-returned value that is mechanically checkable at the reduce is
  checked there*) answers all four and the next one. **The capture flagged this as the ruling that
  determines the cycle's size, and noted Q2 and Q6 depend on it.**
  → **RULED Round 1 (2026-08-26): structure the return; defer the ground-truth args.**
  Take the posture **where it needs no new inputs**, on a distinction neither the filings nor the
  capture drew: for two of the four faces the reduce does not need to *verify* the return, because
  the return can be shaped so there is nothing to parse.
  1. **A14-1 — replace the free-text claim with a structured `PAGE_SCAN` return** (an enum plus a
     field list; exact shape settled at brief time). The residue rule at `:594-604` and the
     `claim.residue === ''` conjunction in both predicates (`:612-617`, `:623-628`) exist **only**
     because the scanner returns prose; given structure they have no reason to exist. **This is the
     A14-1 repair, and it is what reopens Cycle 13's gate.**
  2. **A14-3 — decode HTML entities at the seam, on BOTH sides.** `h2set` (`:643`) is agent-returned
     too, so the index side is exposed and its failure is category-wide; both values are already in
     hand, so this costs no new argument. The exact comparison's strictness is **not** softened (D5).
  3. **A14-2 and Cycle 13 carry-forward 1 (`summary`) are OUT of this cycle's reduce work** — they
     are the only two faces needing real page bytes, and therefore the only two that force the args
     question. Not dropped; deferred to the build that takes the args route.
  *Consequence, stated so no brief re-derives it: the general posture is **partially** taken, and
  Cycle 13 carry-forward 2 stays live for the deferred half.*

  ⚠⚠ **AMENDED — the enum MUST carry an unclassified member, or build-1 ships a fresh instance of
  `ST-6`'s own cause inside the build that reopens Cycle 13's gate** *(roundtable A35, 2026-08-26;
  Maya)*. The mechanism Q1 retires is **fail-OPEN by construction**: `:603` returns anything
  unrecognized as `residue`, and the entry **reports**. A closed enum is **fail-CLOSED by
  construction** — a scanner meeting a genuine schema break outside the enum's roster must **mis-file
  it under a member that fits badly, or drop it.** That **inverts the invariant Q7 explicitly rules
  must survive the move** (*"the failure direction is over-reporting, never swallowing a genuine
  schema break"*). And it is **a closed roster meeting an actor the surrounding rules authorize —
  the exact cause D4 opened `ST-6` to name, shipped by the same cycle that names it.**
  **The enum carries an explicit unclassified member with a free-text detail slot, and an
  unclassified disposition REPORTS rather than being refused.** Shipped precedent, already in the
  file: `sources_vs_prose`'s third member `no_prose_section` (`:164`). *The over-reporting failure
  direction is a property of the escape member, not of the fields list — and it is what build-1's
  own acceptance must test rather than inherit as an assurance (Q7).*
  ⚠ Note the budget interaction: this member is **inside** A1's 102-char ceiling and must be costed
  with the rest of the return.

- **Q2 — does the posture re-admit tracker #13?** Every mechanical-verification direction needs
  ground truth the workflow structurally cannot fetch (`vlt-lint-full.js:36-38`), i.e. a SKILL-side
  per-page arg on the `pageHashes` precedent (`:47-49`) — which moves the joint against #13's ~84KB
  inline-args payload cost. #13 was **deferred as net-new at capture by owner ruling**; if the
  posture is taken it becomes a **dependency**, and re-admitting it is an owner ruling. Depends on Q1.
  → **RESOLVED by Q1 (Round 1, 2026-08-26): #13 stays deferred, not re-admitted.** Q1 took the
  half of the posture that needs no new arguments, so the joint does not move this cycle and #13
  remains net-new. It stays un-captured in `factory/inbox/` and out of this cycle's `derives_from:`.
  **It becomes a dependency the moment the deferred half (A14-2, `summary`) is taken** — that build
  cannot be briefed without ruling #13 first.

- **Q3 — A14-6: pointer, or vocabulary?** If the whole defect is that `vault-operating-contract.md:66`
  never names the convention that owns "a recognized `type:`", the fix is a pointer plus a handshake.
  If the two conventions must be reconciled (`frontmatter.md:71` non-exhaustive incl. `research`, vs
  `checks.md:19`'s closed set), it is a vocabulary decision — and `para_author_unknown` is in the
  population too, with no overlay escape at all. **The capture recommends testing the pointer reading
  first**, because `checks.md:19` already ships "declare the vault-grown type as overlay schema" as a
  stated legal response, which is the filing's own option 4.
  → **RULED Round 2 (2026-08-26): pointer only — the closed set governs the PARA population.**
  `extraction.md` / `checks.md:19` owns what "recognized" means **for the PARA population**, and
  `vault-operating-contract.md:66`'s entry condition is edited to **name it**, exactly as the other
  three legs already name theirs inline. `frontmatter.md:71`'s non-exhaustiveness is scoped so it
  no longer answers for that population.
  **Why this is cheap, on record:** the operating contract is **deliberately not handshaked**
  (single-home + pointers — `CLAUDE.md`), so the `contract:66` edit bumps nothing and re-acks
  nobody. And "declare the vault-grown type as overlay schema (declare-at-birth)" is **already**
  `checks.md:19`'s stated legal response — this ruling signposts an answer the module already
  gives rather than inventing one. The filing's own option 4 was never a new rule.
  **Not taken:** widening the recognized set, and generalizing the `{wiki}` by-name exclusion into
  a declared list. Both remain available if a second agent-lane subtree ever forces the question;
  neither is needed to close this filing.
  ⚠ **`para_author_unknown` is untouched and still closed to `human|agent|hybrid` with no overlay
  escape.** Named so a later reader does not read its survival as an oversight. **How
  `frontmatter.md` is scoped is D2's question**, not settled here. *(roundtable, 2026-08-26: **and
  its owning convention is likewise unnamed — the same defect A14-6 repairs for `type:`.** Recorded
  so the third cycle does not rediscover it.)*

  ⚠ **AMENDED — the pointer's TARGET is not settled, and it is not free** *(roundtable A13,
  2026-08-26; Paige, Maya, Sally)*. The ruling names the owner as *"`extraction.md` / `checks.md:19`"*
  — **two files** — and D2 then rules `extraction.md` does not move. Grounding splits them:
  `extraction.md` states a target-folder→`type:` mapping (`:72-82`, incl. `moc` at `:82`) and the
  container types (`:184-186`), but **never states a closed recognized set, never uses the word
  "recognized"**, and its declare-at-birth sentence (`:118`) declares a vault-grown type's `status:`
  vocabulary, **not the type**. Pointing `contract:66` there **requires adding the closed-set
  statement — a rule change, `extraction.md` 7 → 8, 4 consumers — which D2 forbids.** Pointing at
  `checks.md:19` instead points the module's most load-bearing boundary at a file with **no
  frontmatter, no `version:`, no `consumers:`** (verified `checks.md:1`) — **making a lint check
  *define* a governance term instead of implementing one, and putting the entry condition beyond
  every handshake.** The contract's other three legs each point at a handshaked convention; this one
  would not. **Build-3's brief rules the target explicitly. If it is `extraction.md`, D2's
  "`extraction.md` does NOT move" is void and the cycle is 3 conventions / 19 re-acks.**

  ⚠ **AMENDED — the shipped legal response does not cover the blocked population** *(roundtable
  A14, 2026-08-26; Sally, Maya)*. The ruling rests on `checks.md:19` already shipping the answer.
  Grounded: its legal response is *"declare the **vault-grown** type as overlay schema…"* — and the
  field's blocked files carry **`type: research`, which `frontmatter.md:71` lists as
  MODULE-CANONICAL, not vault-grown.** So option A does not apply by its own words, option B
  (retype) discards a canonical classification, option C (relocate) evicts the shelf. **The module
  does not already give an answer for this population**, and the same holds for `note` and `idea`.
  Worse: A14-6's park was filed on the stated grounds that a local overlay would be **a vault
  answering a module-level question** — and this ruling's practical effect is *yes, overlay it*,
  which would have the vault **assert local authorship of module vocabulary. That is the precise
  thing it parked to avoid.** Build-3 therefore also amends `checks.md:19`'s `para_type_unknown`
  legal response to cover **a module-canonical type outside the PARA set** (admit it to the set, or
  state that overlay-declaration covers module-canonical values — and say which), **and the park
  gets a written unpark trigger: an acceptance check that the vault can execute the stated response
  without declaring module vocabulary as its own.**

- **Q4 — A14-7: widen the value set, or narrow the jurisdiction?** Widening admits a partner
  identifier or an in-sitting sentinel — keeps every Layer 3 artifact attested, weakens the field's
  meaning, and owes a story for what the value is checked against. Narrowing exempts partner-sitting
  writes in §Scope rule the way container files already are (`extraction.md:188`) — **has shipped
  precedent**, is honest about what the pair records today, is the cheaper edit, and costs structural
  coverage of a real class. Either bumps `write-verification.md` from `version: 3`.
  → **RULED Round 2 (2026-08-26): narrow the jurisdiction — by ARTIFACT CLASS, not by writer.**
  `write-verification.md` §Scope rule is amended so that the class of Layer 3 file that is an
  **operational record rather than a knowledge artifact** carries no attestation pair — extending
  `extraction.md:188`'s **existing principle** (restated canonically at `contract:70`) to cover
  partner-sitting writes, rather than adding a writer-shaped axis to a list of exemptions that are
  otherwise about *what the file is*.
  **Why by class and not by writer, on record:** §Scope rule's existing exemptions — `daily/`, raw
  `sources/` deposits, human-authored Layer 3 files — are all statements about the artifact.
  "Written during a partner sitting" is a statement about provenance, and fusing permission to
  provenance is `ST-1`'s named primary cause. The class principle is already shipped, already
  reasoned, and already carries a worked instance.
  **Not taken:** widening the `verified_by` value set. Recorded with its reason — it preserves
  structural coverage but weakens what the field means (an op name, checkable against a roster) and
  owes a story for what a partner identifier or in-sitting sentinel would be checked against.
  **Cost accepted knowingly:** a real class of Layer 3 artifact stops being covered by any
  structural check. The filing said so and the ruling accepts it.
  ⚠ **The `local_consumers:` route stays as-is** (`write-verification.md:47`, `frontmatter.md:296`)
  — a vault-minted partner that genuinely *is* a write op can still register and hold a legal
  value. This ruling does not remove that; it removes the need to pretend to be one.
  **Bumps `write-verification.md` 3 → 4 and re-acks all 5 consumers — see D2.**

  ⚠⚠ **AMENDED — the class test needs a MECHANICAL DISCRIMINATOR, named in the ruling, or the
  ruling reverts** *(roundtable A11, 2026-08-26 — found independently by five voices; the room's
  single strongest finding after the schema budget)*. The precedent this ruling extends is not a
  class judgment. **`extraction.md:188` is RATIONALE, not a predicate** — it is a label attached to
  three filenames; the shipped carve-out is enforced mechanically and by name at `checks.md:17`
  (*"container files (`charter.md`/`record.md`/`register.md`) under a `{projects}`/`{areas}`/
  `{resources}` container directory"*). §Scope rule's jurisdiction today is likewise a **mechanical
  frontmatter test** (`type: wiki|research|project|area|resource` with `author: agent|hybrid`, minus
  three location exemptions) — **which is exactly why `extraction.md:188` was cheap.**
  *"An operational record rather than a knowledge artifact"* is **neither a frontmatter fact nor a
  path fact.** `write-verification.md:13-15` declares `enforcement_checked_by: vlt-lint` — **so the
  rule's own declared enforcement point has no input that decides it, and neither does the partner
  deciding whether to attest.** A14-7's population carries `type: project|area|resource|research`
  with `author: agent|hybrid`, **indistinguishable from the artifacts that must stay covered**; the
  only thing separating the two populations is **the writer**, which Q4 correctly refused on `ST-1`.
  **In the cycle named "no enforcement point", build-3 would ship a rule with no enforcement point**
  — and the partner's journey dead-ends one step **later** than before: it used to have no honest
  `verified_by`; now it would have no way to know whether it needs one, and lint no way to agree.
  **The exemption MUST be expressible in the frontmatter §Scope rule already reads — a `type:`
  value, a declared field, or a location — and build-3's brief NAMES it. If no such discriminator
  exists, Q4 reopens and the fallback is the not-taken widening.** If the discriminator is a new
  `type:` value it is declared in `extraction.md` and re-opens A13's scope; if a new declared field,
  it rides the `frontmatter.md` 13 → 14 bump already owed. **Build-3's brief-time question is
  promoted from "the exact wording" to the discriminator, and is BLOCKING.**

  ⚠ **AMENDED — the TRANSITION is ruled here, not left to the field** *(roundtable A12,
  2026-08-26; Sally)*. Whatever discriminator A11 forces, **no existing file carries it** — so on
  the day build-3 ships, the 27 measured files are still in jurisdiction, still flagged, and still
  hold only the two responses the filing called illegitimate. Verified: `checks.md:17`'s
  `unattested_write` is *"informational, not a violation, for files whose `created` predates
  convention adoption"* — **`para_missing_attestation` carries no such pre-adoption clause.**
  **A narrowing that legalizes only files not yet written is not a repair for the vault that filed
  it.** Build-3 either satisfies the discriminator retroactively for files already on disk (stating
  how) **or ships a pre-adoption informational posture for `para_missing_attestation` matching
  `checks.md:17`'s clause**, and its acceptance names what happens to the measured population. The
  **type distribution of those 27 across §Scope rule's jurisdiction list is unmeasured** — measure
  it, or the exemption's reach is unknown.

  ⚠ **AMENDED — the CONTRACT's entry condition still demands the pair, and D2 forbids bumping it**
  *(roundtable A12b, 2026-08-26; Amelia)*. The pair is not merely a lint net — it is **a term of
  `contract:66`'s Layer-3 entry condition**: *"Content that carries it is in; content that does not
  is out, wherever it sits."* `:70`'s existing carve-out names container files **by class and
  nothing else**. After build-3, a partner-written operational record in `{resources}` would be
  exempt from the finding **while the contract still says it is "out" of Layer 3** — **the batch
  would resolve A14-7's two-surface disagreement by creating a new one, the same shape, one file
  over.** So `vault-operating-contract.md` gains the A14-6 pointer at `:66` **and** the Q4 class
  carve-out (widening `:70`'s operational-record sentence, or qualifying `:66`'s attestation-pair
  leg) — **still no bump, the contract is deliberately not handshaked** — and **build-3's acceptance
  checks that the contract and `write-verification.md` state the same exemption.**

- **Q5 — A14-5: which direction, given the `machine_tools` cost?** The capture re-ordered the
  filing's own list: (1) a **validation beat** — the gap is the unchecked "parses whole in both
  homes" claim, not a missing emitter; (2) state the no-dependency requirement + JSON-subset emission
  in `report.md` (pure documentation, zero cost); (3) allow `.json` as an alternative persist (touches
  the both-homes rule directly); (4) ship an emitter — **costs a `machine_tools` row in the same
  build** per that block's writer clause, which is why it ranks last here and first in the filing.
  → **RULED Round 4 (2026-08-26): allow a `.json` persist, and document the emission strategy.**
  `report.md` gains (a) an explicit **no-dependency** requirement with the JSON-subset emission
  strategy stated — every scalar a JSON string, lists as `- <json>`, nested maps by indentation —
  and (b) **`.json` as a legal alternative persisted format**, the fenced in-session block staying
  YAML for human reading.
  **The reason for this direction over the filing's own first choice, on record:** a `.json` persist
  makes the *"parses whole in both homes"* claim **checkable with `python3 -m json.tool` against an
  already-declared tool**, which is what lets it carry a **gating at-rest check under D3**.
  ⚠ **AMENDED — the ORIGINAL rationale rested on a false premise and is struck** *(roundtable A9 /
  owner Ruling 4, 2026-08-26; Maya, verified in session by the moderator)*. The ruling as filled read
  *"`json` is Python **stdlib** and `yaml` is not — that asymmetry is the whole ruling … at zero
  `machine_tools` cost"*, resting on the capture's statement that `machine_tools` *"currently
  declares exactly one vault-side tool assumption: `gh`."* **That is false against working-tree
  source.** `skills/vlt-setup/assets/module.yaml` declares **four** — `gh`, **`uv`**, **`python3`**,
  `git` — and **`uv`'s declared purpose is literally *"vlt-setup / vlt-upgrade merge + manifest
  scripts (PEP 723 inline deps)"***, which is the mechanism for obtaining a `yaml` dependency on a
  PEP 668 machine **without a new row**. **The stdlib asymmetry the ruling turned on does not
  exist.** The `.json` direction **STANDS on the corrected reason above** (owner ruling); recorded
  because the not-taken option 4 (ship an emitter) **was ranked last for a `machine_tools` cost it
  does not incur**, and a later cycle re-opening this must know that. Documentation alone leaves the
  claim unenforced, which is the exact defect this cycle is named for; an emitter asset would
  enforce it but owes a `machine_tools` row.
  ⚠ **This rewrites `report.md:3`'s "both homes" sentence** — it must be restated, not appended to,
  or the bundle asserts one format while permitting two.

- **Q6 — A14-8: fix the shapes, or remove the seam?** The field named five directions. The capture's
  reading is that (1) moving the record wrapping **into the workflow** and (2) moving
  `rulesetFingerprint`'s computation into the workflow are strictly better than documenting either,
  because they remove the derivation rather than describing it. Also open: (5) whether the step-4
  refusal predicate widens so "cold because unreadable" is distinguishable from "cold because the
  ruleset moved."
  → **RULED Round 3 (2026-08-26): remove both seams; leave the step-4 predicate alone.**
  1. **The workflow returns write-ready `{slug, key, scan}` records** instead of raw `fresh_scans`
     (`:723`), so the read shape (`:243`, `:344`) and the written shape cannot drift apart again.
  2. **The fingerprint is composed in the workflow.** ⚠ **Correction to the capture's reading,
     issued in session:** the capture said moving `rulesetFingerprint`'s *computation* into the
     workflow was strictly better. That is only half available — the fingerprint's inputs include
     each convention's digest **as merged with its overlay** and `checks.md`'s digest, and the
     workflow cannot read files (`:36-38`), so the SKILL must compute the component digests
     regardless. **What moves is the composition** — canonical member order, separator, digest and
     truncation — with the SKILL passing components and the workflow assembling them. That still
     kills the defect (one implementation composes), and it is a narrower move than the capture
     described. A brief must not scope it as "compute the fingerprint in the workflow."
  3. **The round-trip check ships and GATES** (D3: at-rest instrument ⇒ ship-verifiable): write the
     sidecar, read it back, assert every record is reusable against an unchanged corpus.
  **Not taken: (5), widening the step-4 refusal predicate.** Recorded with its reason — the
  round-trip check is a *direct* instrument for the failure the predicate would only *infer*, and
  under D3 it gates, so the invisibility is closed at its source. Available if the round-trip check
  proves insufficient.
  ⚠ **The existing sidecar cannot be migrated.** It stores `fingerprint:` once at top level and no
  per-page digest, so it cannot express the reader's key even in principle — the first run after
  this build is COLD by construction, and the brief should say so rather than let it read as a
  regression.

  ⚠ **AMENDED — the composition move kills only HALF the defect** *(roundtable A7, 2026-08-26;
  Builder)*. Defect 2 was grounded as *"no separator, no hash algorithm, no encoding, no truncation,
  no canonical member list."* Moving **composition** single-homes separator, member order and
  truncation. It does **not** touch **hash algorithm or encoding** — those belong to the component
  digests Q6 explicitly leaves SKILL-side, and `full-scale.md` step 2 states them with **no
  instrument, no merge order, and no digest algorithm.** (Contrast step 1, which for `pageHashes` at
  least names `shasum -a 256` and a property.) **Two conformant executors still produce different
  fingerprints from identical rulesets — exactly the field's `980d749d9acf418e` vs
  `66d27a0e6cd8fabe`, which the grounding never attributed to the composition half.** So: **the
  component digests must be single-homed as executable steps in `full-scale.md` step 2 in the same
  build** — named instrument, merge order (base then overlay), encoding, truncation — **or the
  fingerprint stays non-deterministic and only its composition is fixed.**

  ⚠ **AMENDED — step 2's ordering clause is RETIRED with the move, not left beside it** *(roundtable
  A40, 2026-08-26; Victor)*. `full-scale.md` step 2 specifies the fingerprint as *"a digest over,
  **in this order**: …"*. Once composition moves into the workflow, **that clause describes an
  algorithm the SKILL no longer performs.** Left standing beside the workflow's implementation it
  **re-creates A14-8's exact shape — one contract in code, one in prose, nothing where they meet.**
  It is replaced by a **component-list contract** (what the SKILL passes), never amended to sit
  alongside.

- **Q7 — A14-1's false safety comment.** `vlt-lint-full.js:559-561` asserts the guards *"never fire
  on a claim they cannot positively identify — the failure direction is over-reporting, never
  swallowing a genuine schema break."* The field refuted the safety property. Whatever build takes
  A14-1 must **correct the comment or retire the claim** — a shipped comment asserting a refuted
  property is the same defect one level out. Ruling needed on which.
  → **RESOLVED by Q1 (Round 3, 2026-08-26): the comment goes with the guard.** Q1 replaces the
  free-text claim with a structured return, which removes the residue rule the comment describes —
  so `:559-561` is not corrected, it is **retired along with the mechanism it documents**. The
  build states the new invariant in its place. *Recorded because the honest half of the old comment
  must survive the move: the failure direction is over-reporting, never swallowing a genuine schema
  break, and that property must hold of the structured return too — it is a claim the round-trip of
  Q1's own acceptance should test, not an inherited assurance.*

- **Q8 — Cycle 13 carry-forward 3, the `malformed_frontmatter` retirement.** Its named successor is
  the build that takes Q1's general posture. It was deferred because retiring a shipped finding class
  needs a **measured** population first — and Cycle 13's check (2), which was to be that measurement,
  **FAILED**. So the measurement does not exist and the taking build must produce it. Ruling needed
  on whether the retirement rides this cycle at all.
  → **RULED Round 3 (2026-08-26): defer again — but attach the measurement to A14-1's build.**
  The retirement does **not** ride this cycle. Q1 changes the class's genuine population a second
  time (a structured return alters what can reach `malformed_frontmatter` at all), so retiring it
  now would be a behavioral removal on grounds that are not merely unmeasured but **about to
  change**. **The correction to the pattern:** A14-1's build carries an acceptance check that
  *produces the measurement* — what genuinely reaches the class once the structured return ships —
  so the successor build inherits real numbers instead of a third deferral with nothing behind it.
  *This is the third cycle this retirement has been carried; the deferral is only defensible
  because it now ships with the instrument that ends it.*

  ⚠ **AMENDED — J1 answered, and the real fault is elsewhere** *(roundtable A19, 2026-08-26)*.
  **The room went looking for the circularity the roadmap itself flagged and did not find it**
  (Winston, conceding on the evidence; Amelia concurring): Q8 measures the **post-repair**
  population, which is the population a retirement decision actually needs — measuring the
  pre-repair one would be the error. **Three real faults replace it:**
  1. **It must be able to FAIL.** `brief-anatomy.md:245-247` binds both tags to *"a discharging
     instance must be one that could have failed"*, and `tools/package-lint.py:56-59` already ships
     the principle (*"a gate check with no fixture case is itself a lint failure"*). **A population
     count has no failing state and would discharge on the act of counting.** The check therefore
     **asserts a stated bound** on the class's post-repair population, not merely reports a number.
  2. **It is a SPECIMEN SET, never a bare count.** `ST-5`'s direct evidence is the 20 → 2 → 2 → 0
     trace in which the filing's phrase *"18 entries"* is precisely what left the briefer nothing to
     build from. **Inheriting a cardinality would reproduce ST-5 one section below the citation.**
     The measurement is **slug plus the minimal triggering fragment for every page reaching the
     class**, materialized in `factory/cycles/14-no-enforcement-point/`.
  3. **Its two halves are DIFFERENT instruments and the brief must say so.** Pre-change: the
     persisted `{lint_reports}` archive already holds `malformed_frontmatter:` entries across
     multiple full sweeps — **a real corpus needing no new sweep** (Carson). Post-change: only a
     live sweep produces it, because **build-1 changes the return's shape, so pre-change recorded
     returns are free-text the post-change schema cannot emit** (Maya, Amelia) — and no wiki corpus
     ships in this repo. **Under D3-as-corrected (bounded, not at-rest) the check is BOUNDED and
     therefore GATES**, bounded to the first full `{field-vault}` sweep after release 1.

### Cross-filing decide-once rulings

- **D1 — the `verbatim` enforcement question, decided once.** `PAGE_SCAN` marks fields *verbatim* in
  schema descriptions (`:158`, `:162`) and Cycle 13 established a schema description is an
  instruction, not an enforcement point. Two faces are live: **paraphrase** (Cycle 13 carry-forward 1,
  `summary`) and **re-encoding** (A14-3, `category`, HTML entities). A third surface is exposed and
  has not fired: `h2set` is built from the *index scanner's* returned `h2_headings` (`:643`), so a
  `&amp;` on the index side falsifies **every page in that category at once**. Decide the enforcement
  posture once across all three rather than per-field.
  → **RESOLVED by Q1 (Round 3, 2026-08-26): structure or normalize at the seam; never rely on the
  word `verbatim`.** The posture, stated once for all three surfaces: a field the reduce works on
  exactly is either **returned in a machine-checkable shape** (A14-1's claim → structured) or
  **normalized on intake at the seam** (A14-3's encoding → entity-decoded, on **both** sides, since
  `h2set` at `:643` is agent-returned and its failure is category-wide). **The word `verbatim` in a
  schema description is documentation, never an enforcement point, and no build may treat it as
  one.** The third surface — the **paraphrase** face (`summary`, `:162` → `:545`) — cannot be
  closed by either move without real frontmatter, so it is deferred with A14-2 per Q1. *The posture
  is ruled whole here even though it is applied in two cycles: the deferred build inherits it
  rather than re-deciding it.*

- **D2 — the handshake scope for this cycle, decided once.** Q4 bumps `write-verification.md`
  (`version: 3`, 5 consumers) under either direction. Q3 under a widening reading touches
  `frontmatter.md` (`version: 13`) and/or `extraction.md` (`version: 7`, 4 consumers). Rule the total
  bump-and-re-ack set once, in one build, so the bipartite-consistency check is satisfied in a single
  edit rather than re-derived per build. `build-brief` gates on it.
  → **RULED Round 3 (2026-08-26): two conventions move, in ONE build. Elimination, not precedence.**
  - **`write-verification.md` 3 → 4**, re-acking all **5** consumers
    (`vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-lint-full.js`) — forced by Q4's §Scope
    rule amendment.
  - **`frontmatter.md` 13 → 14**, re-acking all **10** consumers
    (`vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-mint, vlt-dispatch, vlt-setup, vlt-groom,
    vlt-query, vlt-lint-full.js`) — `:71`'s non-exhaustiveness is **scoped** so its `type:` list
    governs the base/agent lane and explicitly does **not** answer for the PARA population.
  - **`vault-operating-contract.md:66`** gains the pointer. **No bump** — the contract is
    deliberately not handshaked.
  - **`extraction.md` does NOT move** (stays `version: 7`): Q3 takes no widening, and Q4 extends
    `extraction.md:188`'s principle by **citing** it from `write-verification.md` §Scope rule, not
    by editing it.
  **Total: 2 conventions, 15 re-acks, one bipartite-consistency check, one build.**
  **Why elimination and not the cheaper precedence statement, on record:** `CLAUDE.md`'s
  *precedence by elimination* rule makes a precedence statement **the fallback**, legal only where
  the populations cannot be cut apart. Here they cut cleanly — the PARA population versus
  everything else — so narrowing `frontmatter.md`'s population is the indicated move. The 10
  re-acks are the price of not leaving a canonical value that is simultaneously well-formed and a
  loud finding, resolvable only by reading a third file.

  ⚠⚠ **AMENDED — the narrowing FALSIFIES a sentence in the one convention D2 forbids moving**
  *(roundtable A15, 2026-08-26; Builder, Amelia, Sally)*. The container types are grounded by a
  **circular pointer pair**: `frontmatter.md:71` names `charter|record|register` pointing at
  `extraction.md`, and **`extraction.md:188` closes with *"The three `type:` values … ride
  `frontmatter.md`'s declared non-exhaustive `type:` list — named here, no contract edit owed."***
  Container files sit under `{projects}`/`{areas}`/`{resources}` and are in the `para_*` population.
  **Scoping `:71` out of the PARA population makes `:188`'s grounding sentence false the moment
  build-3 lands, in the very population where those three values are used.** Repairing it edits
  `extraction.md` — a rule change: **`version: 7 → 8`, 4 consumers. 15 re-acks become 19, and D2's
  own cost line is wrong.** *(Compounding, same site: `:188` is also the precedent Q4 extends, and
  A11 finds it is rationale rather than predicate.)*
  **Build-3's brief settles the number before it is written.** If the owner will not pay 19, **the
  alternative is the precedence statement D2 rejected — and that trade is re-put with the true
  number in view**, since D2 chose elimination over precedence partly on cost. *(Owner Ruling 2,
  2026-08-26: the four-build shape holds and this is absorbed as a brief-time scoping fact; the
  re-pricing is not waived.)*

  ⚠ **AMENDED — the cut is asymmetric: it opens `moc` in the other direction** *(roundtable A16,
  2026-08-26; Amelia)*. `checks.md:19`'s recognized set includes **`moc`**, and **`frontmatter.md`
  never mentions `moc` — zero hits in the file.** Narrowing `:71` so it does not answer for the PARA
  population leaves `moc` **recognized by a shipped lint check and named in no convention** — the
  ambiguity is not eliminated, it **changes direction**. The same edit therefore **adds `moc` to
  `:71`'s canonical list**, inside the 13 → 14 bump already owed.

  ⚠ **AMENDED — the re-ack surface is larger than the bipartite check can see** *(roundtable A3,
  2026-08-26; Caravaggio, Builder, Paige, Carson, Maya, Amelia, John, Victor)*. **15 re-acks is the
  `depends_on:` surface. `vlt-lint-full.js` additionally recites the two conventions by version at
  SEVEN in-prose sites** (`:158`, `:159`, `:164`, `:168`, `:215`, `:571`, `:573`). Verified:
  `handshake-check.py` reads only `version:`/`consumers:` and the flat `depends_on`; package-lint
  **E5** parses only `:11`; and **E3's stray-pin net deliberately excludes `vlt-setup/assets/**`**
  (`tools/package-lint.py:736-739`). **So the bipartite check passes green while seven stale
  citations ship to every vault — three of which (`:159`, `:164`, `:168`) restate the very §Scope
  rule Q4 amends, making them wrong rather than merely old.** **Build-3 greps `write-verification@3`
  and `frontmatter@13` across `skills/`, updates every hit, and its verification NAMES the grep** —
  the bipartite verification is manual for those seven. **Total: 15 re-acks + 7 prose pins, one
  bipartite check, one manual grep.**

  ⚠ **Recorded as a RETIREMENT under P-15** *(roundtable, 2026-08-26; Amelia)*: `frontmatter.md:71`'s
  open-vocabulary clause **ceases to govern the PARA population**; `checks.md:19`'s closed set
  supersedes it there. **Named, not silently survived** — D2 performed the narrowing and did not
  record it as a retirement.

- **D3 — the ship-verifiable / field-contingent tagging posture for this cycle.** ⚠ **The capture
  and the Cycle 12 ruling both flag this as the cycle's most consequential procedural decision.**
  b2(5) was tagged field-contingent, therefore did not gate, and v0.16.0 shipped a findings cache
  **that has never once worked** on a green ship-verifiable ledger (A14-8; `ST-5` causes 2 and 3
  compounding). A14-8's round-trip check is gradeable **at rest**, so nothing forces it to be
  field-contingent. Precedent for the correction exists: B7-6 retired the four-cycle A4-4(5) debt
  precisely by tagging it ship-verifiable so it gated. Rule the posture once, for every check this
  cycle writes.
  → **RULED Round 1 (2026-08-26): an at-rest instrument ⇒ the check is ship-verifiable and it
  GATES.** `field-contingent` is reserved for checks that **genuinely cannot be graded before
  shipping** — never for checks that are merely more convincing in the field. This binds **every
  check every brief in this cycle writes**; `build-brief` reads it as a cycle-level constraint, not
  a per-check judgment. Rationale on record: B7-6's correction (which retired the four-cycle
  A4-4(5) debt by tagging it ship-verifiable so it gated) promoted from a one-off to a standing
  rule, aimed at the mechanism that let b2(5) through.
  **Immediate application:** A14-8's round-trip check is gradeable at rest and therefore **GATES**.

  ⚠⚠ **AMENDED — D3 was written on the WRONG AXIS, and as drafted it makes FEWER checks gate, not
  more** *(roundtable A17, 2026-08-26 — reached independently by Winston and Mary; corroborated by
  Quinn, John, Amelia, Maya)*. The shipped criterion is **boundedness**, not at-rest gradability.
  `build-brief/references/brief-anatomy.md:203-210` defines `[ship-verifiable]` as **three** species
  — *"dischargeable **at rest, at the release gate, or on the next ordinary upgrade**. **Bounded**:
  an event that is going to happen anyway will settle it"* — and `[field-contingent]` as the
  **unbounded**: *"nothing in the build, the release, or the upgrade causes it."* **D3's phrasing
  ("field-contingent is reserved for checks that genuinely cannot be graded before shipping") pushes
  the upgrade-bounded species — which GATES today — into field-contingent, where it stops gating.**
  And the check it costs is **E4's** (see Q8). **The operative sentence is therefore restated:**
  → *"A check whose discharging event is **bounded** — at rest, at the release gate, or on the next
  ordinary upgrade — is **ship-verifiable and it GATES**. `field-contingent` is reserved for the
  genuinely **unbounded**, per `brief-anatomy.md:203-210`. **An at-rest instrument is one sufficient
  bound, not the criterion.**"*

  ⚠ **AMENDED — D3 binds the TAG; it does not bind INSTRUMENT ADEQUACY, which is what actually
  failed** *(roundtable A17b, 2026-08-26; John, Builder, Amelia)*. Verified: b2(5)'s shipped text
  (`12-proxy-claims/roadmap.md:2807-2816`) bound its event to *"the owner runs `vlt-lint --full` …
  **twice** after upgrading"* — a field event with no at-rest instrument available, **correctly
  tagged** under the shipped definition. **Under D3, b2(5) is STILL field-contingent and STILL
  non-gating: the rule does not reach the failure it cites as its whole motivation.** What failed
  was its sibling — **an at-rest instrument that stubbed the seam and was believed.** D3's
  antecedent is also the briefer's discretionary output, so *not writing an instrument* is a route
  out of the gate. **Two clauses close both:**
  1. *"Where a check's subject is gradeable at rest by an instrument buildable inside the build's
     own scope, the brief **must build it**. Declining is a written justification in the brief,
     never a tag choice."*
  2. *"Every brief states, **per ship-verifiable check, which seam its named instrument actually
     crosses**"* — see **R1** in the Roundtable review record.

  ⚠ **AMENDED — the routing sentence was not true as written; the P-N already exists** *(roundtable
  A18, 2026-08-26; Amelia's grounding, correcting Quinn's reading)*. The closing note read as if
  `ST-5`'s fix were unrouted. It is **already on the platform ledger as P-18 Tier C — "gating
  honesty (`ST-5` C8/C9)"** (`factory/platform/roadmap.md:697-701`), **precondition-blocked behind
  P-18 Tier A** (*"Tier A must first produce one cycle of real manifests"*), and **P-18's in-cycle
  repair lane (`:703-705`) names ruling D3 directly.** So: **no new P-N opens.** D3 is the
  cycle-scoped stand-in for P-18 Tier C and **expires when Tier C lands**; a Tier C build must read
  this ruling. D3 is **re-ruled per cycle, never inherited as precedent** — the honest statement is
  that the lifecycle fix is *deferred by a stated precondition*, not merely unwritten.

  ⚠ **NOT taken, recorded with its reason** *(roundtable, 2026-08-26; John's obsolescence finding)*.
  John argued D3 should be **cut to a pointer** at `brief-anatomy.md:242-243` (*"Do not use the tag
  to dodge rigor … Tagging a ship-verifiable check field-contingent to get it out of the gate is the
  vacuous-discharge failure wearing a new hat"*) — i.e. that D3 is that shipped prohibition re-said
  one cycle down, **a rule restated where it already lives, which adds no enforcement point.** The
  room agrees the observation is correct and that **D3 must never restate the definition** (it now
  cites it, per A17). It is kept as a **cycle-scoped tagging instruction applying the shipped
  definition** because the two new clauses above are genuinely new. **Dissent recorded: a pointer
  plus the instrument-adequacy clause would have been the smaller, single-homed move.**

- **D4 — is "a closed roster meeting an actor the surrounding rules authorize" a named pattern?**
  Three live instances: A14-7 (`verified_by` roster vs the contract's open writer set), the Cycle-10
  decision-log Writers-roster filing (`origin: mggower/bmad-module-vlt#6`, still in the inbox), and
  arguably A14-6 in the vocabulary register rather than the writer register. **No study holds this
  cause** — `ST-1` is adjacent but bottoms out in one verb's shape. Opening `ST-6` gates nothing and
  is the author's call (`factory/studies/README.md`, *Citable, never blocking*); the ruling here is
  whether this cycle patches the instances or names the cause first.
  → **RULED Round 4 (2026-08-26): open `ST-6` now, while all three instances are grounded and in
  hand.** It gates nothing and blocks nobody (`factory/studies/README.md`, *Citable, never
  blocking*), and the register's own documented failure mode is **a cause re-derived because nobody
  thought to look** — which has already happened twice (ST-1 → ST-2 at five days; the 2026-08-24
  session → ST-2's RC2 at one day).
  **Not a reason to defer:** that Q3 and Q4 repair two of the three instances this cycle. A study's
  test is the **cause**, not the fix (`README.md`, *What does not earn an entry*) — a cause whose
  repair already shipped still passes if naming it would change how a later cycle reads a problem
  it has not met yet. **The study is written from the pre-repair state; the repairs are recorded in
  its `cited_by:`.**

- **D5 — the named-to-be-rejected directions, recorded so no brief re-derives them.** A14-2's
  candidate 3 (ask the scanner to return links more carefully) and A14-3's candidate 3 (loosen the
  category comparison) were each named to be rejected **by their own filings**, and the capture
  agreed: the first is the prompt-side fix whose failure is Cycle 13's entire premise; the second
  retires real drift findings to work around a transport defect. Confirm as standing, or reopen.
  → ⚠ **Sharpened by Q1 — the two can be misread as contradictory, and the distinction is
  load-bearing.** Q1 rules that A14-1's claim return is **restructured**, which a careless brief
  could read as A14-2's rejected candidate 3 ("ask the scanner to return links more carefully").
  They are different acts: **changing what the schema asks for, so the answer arrives in a
  machine-checkable shape, is not the same as asking the scanner to try harder at the same
  free-text task.** The first removes the parse; the second is the prompt-side plea whose failure
  is Cycle 13's entire premise. **Both rejections stand.**
  → **CONFIRMED as sharpened (owner, at the roundtable, 2026-08-26): both rejections stand.**
  *(roundtable A-D5, 2026-08-26 — the slot read "(owner to confirm as sharpened)" while the
  frontmatter, this section's header, and §Next lifecycle move all asserted "every slot is ruled",
  and **build-1 `binds:` D5**. `build-brief` gates on the section being filled and would have read
  an unconfirmed slot as filled. Victor tested the beat here and returned a negative on record:
  both re-confirmed rejections are of directions **never built**, so **a rejection of an unshipped
  direction has no site to retire** — D5 adds no retirement and the Q1 sharpening is a genuine
  distinction, not a preserved prohibition.)*

### Spikes

**Register read 2026-08-26** (`factory/platform/spikes/`; mechanics single-homed at its `README.md`).
**No `proposed` or `running` entries — this batch inherits no open spike.** The capture opened none:
every claim in all eight filings was groundable against module source in the working tree, and no
grounding hit an external unknown.

- `S-1` (para-container-harvest) — **consumed** (verdict `proceed`; Cycle 9 → consumed Cycle 10).
- `S-2` (projection-baseline) — **consumed** (verdict `proceed`; Cycle 3).
- `S-3` (github-notification-semantics) — **harvested, unconsumed** (verdict `reshape`, run
  2026-08-24, owner-delegated; opened for Cycle 11 A11-2, which deferred to Cycle 12). `harvested`
  is the state the gates accept, so it is available to any build that wants it. Listed here so it is
  not rediscovered at brief time — **not** a claim that this batch needs it.

**Spikes this batch newly demands: NONE (ruled Round 4, 2026-08-26).** Every build above carries
`spike: none`. No grounding in this cycle hit an external unknown — all eight filings grounded
against module source in the working tree — and none of the four builds reads an external source.
*No register file changes as a result of this session; `S-3` stays `harvested`, unconsumed.*
*(Register hygiene, per `factory/platform/spikes/README.md`: **every spike disposition made**
here (open a spike, kill one, rule a build `spike: none`) is written back to the register file in
the same session; status and `verdict:` live there, never only in roadmap prose.)*
*(roundtable A30, 2026-08-26 — the section ended in an orphaned fragment with a dangling
close-paren and no subject; the lost opener is the clause that makes the register authoritative
over roadmap prose, and `build-brief` gates on this section.)*

### Evidence-debt dispositions

*Ruled Round 4 (2026-08-26) — each debt attached to a build or ruled not-blocking. Two constrain a
brief's text (E2, E5); one is discharged by a build (E4).*

- **E1 — A14-4's root-cause guess is unverified.** The filing argues the `fix_now` classification was
  set from the check's *detectability* rather than its *remediability*. Capture could neither confirm
  nor refute this from source; it is recorded as the filer's reasoning. A fix does not depend on it.
  → **NOT BLOCKING (Round 4). Attached to build-4 as context, not as a premise.** The fix — a second
  legal response routed by divergence direction — stands or falls on the measured 0% application
  rate across two full sweeps, which is grounded. **No brief may assert the
  detectability-vs-remediability account as a finding**; it is the filer's reasoning, unverified.

- **E2 — A14-4's qualifier has an unmeasured blast radius.** The filing argues *"frontmatter is the
  source of truth"* needs re-scoping — authoritative about what a page *claims to rest on*, not what
  it *actually cites*. That is a claim about `write-verification.md`'s tier-1 item, not only about a
  lint slot. Neither the filing nor the grounding measured how far it reaches.
  → **SCOPED OUT of this cycle (Round 4), and named so it is not lost.** Build-4 rewrites the
  **lint check's** fix direction only; it does **not** touch `write-verification.md`'s tier-1 item.
  Rationale: build-3 already moves `write-verification.md` 3 → 4, and folding an unmeasured
  re-scoping of *"frontmatter is the source of truth"* into that bump would put an unbounded claim
  inside a 15-re-ack handshake. **If the qualifier is real it is a filing, not a footnote** —
  measure the blast radius first.
  ⚠ **AMENDED — it is routed, or it evaporates** *(roundtable A32, 2026-08-26; Mary)*. E2 prescribes
  the remedy and **names nobody to measure it and nothing to file it**, and its item is **missing
  from §Grouping & order's "Deliberately NOT in this cycle, and where each went"** — the roadmap's
  purpose-built destination. `closeout-checklist.md:74` is unambiguous: *"anything left off here is
  silently dropped."* **The one entry in the batch whose disposition is "this deserves its own
  filing" was the one entry with no route to becoming one** — and the cycle it would land in is the
  cycle that has just bumped `write-verification.md`, and will be least inclined to reopen it.
  **Routed: the owner files it to `factory/inbox/` as a `pattern` against `write-verification.md`'s
  tier-1 item**, so a later capture grounds it. Listed in "where each went" and carried at closeout
  as a deferred question. **Not a build in this cycle.**

- **E3 — A14-7's counts are single-vault.** 27 unattested / 5 attested / 0 partner-sitting-attested
  are `{field-vault}`-local. They establish the class is large and ordinary there; they establish no
  rate for vaults generally, and the filing does not claim they do.
  → **NOT BLOCKING (Round 4). Attached to build-3.** The counts establish the class is large and
  ordinary in one vault, which suffices for a jurisdiction narrowing — the ruling turns on what the
  attestation pair *means*, not on how many files lack it. **The brief must not cite 27 as a general
  rate**, and the acceptance check must not be written as if it were.
  ⚠ **AMENDED — E3 forbade the only framing build-3 had and left a hole where the check was**
  *(roundtable A33, 2026-08-26; Mary)*. With both halves ruled out, what survives at rest for
  build-3 is: version strings bumped, 15 acks current, package-lint E1 bipartite-consistent,
  `contract:66` contains a pointer. **Every one is satisfied by build-3's own diff — they grade
  whether the edit was TYPED, never whether the narrowing WORKS**, and only E1 can fail at all.
  **So the cycle's largest and most irreversible build — 15 re-acks and a permanent coverage loss
  accepted knowingly at Q4 — would gate on bookkeeping.** The substance claim **is** gradeable at
  rest against a fixture. **What replaces the count:** build-3's brief names an **at-rest fixture
  PAIR** — a Layer-3 file bearing `author: agent`, no attestation pair, **of the operational-record
  class the amended §Scope rule exempts** (per A11's discriminator), **plus a control of the
  knowledge-artifact class that must still flag**. The gating check is that the first yields no
  finding **and the control does**. The 27 appear in the brief only as the observation that
  motivated the ruling — never as a rate, never as a check.

- **E4 — Cycle 13 carry-forward 3 has no population measurement.** See Q8: the measurement was to be
  Cycle 13 check (2), which FAILED. Retiring `malformed_frontmatter` without one is a behavioral
  removal on unmeasured grounds.
  → **RESOLVED by Q8 (Round 3).** *(roundtable A31, 2026-08-26 — Q8 is stamped Round 3.)* Build-1 carries an acceptance check that **produces** the
  measurement.
  ⚠ **AMENDED — PARTIALLY resolved; the debt is BOUND, not discharged** *(roundtable A19,
  2026-08-26; Mary, Amelia, Maya, John)*. E4's debt is *"retiring `malformed_frontmatter` without a
  measurement is a behavioral removal on unmeasured grounds"* — **and build-1 does not retire it.**
  Q8 defers the retirement a **third** time to a successor build §Grouping & order does not
  schedule. **A build that produces a datum does not discharge a debt owed by the build that acts on
  it.** So: build-1 carries a check that **could fail** (Q8 amendment 1), the measurement is a
  **specimen set** recorded with its corpus size and date in build-1's `status:`, and **the debt
  itself transfers, with the number attached, to the build that takes the retirement** — recorded at
  closeout as a Stage-2 carry-forward with a **named successor cycle** (`closeout-checklist.md:67`
  is the slot for a standing metric). **A bare count does not discharge E4.**

- **E5 — A14-6's own filing is stale against its vault.** Tracker #15 describes moving the
  `vlt-brief` shelf to a `{resources}` address as prospective; the shelf has been at
  `resources/briefs/` since before the 2026-08-26 10:46 lint, which enumerates all five issues in
  `para_type_unknown`. **The reported defect is unaffected** — the two conventions still disagree —
  but a brief quoting the filing's framing would assert a false premise about vault state.
  → **BLOCKING for build-3's brief (Round 4).** The brief writes A14-6 from **the capture's grounded
  text and the vault's current state**, never from tracker #15's prose. The shelf is at
  `resources/briefs/`, five issues, enumerated in `para_type_unknown` by the 2026-08-26 10:46 lint.
  **The reported defect is unaffected** — the two conventions still disagree — but a brief repeating
  the filing's prospective framing asserts a false premise in the one build whose subject is which
  convention tells the truth.
  ⚠ **AMENDED — vault-current state grounds the BRIEF; no vault path reaches the SHIPPED edit**
  *(roundtable A34, 2026-08-26; Paige)*. Build-3's deliverables are shipped governance
  (`write-verification.md`, `contract:66`), and **a class-based exemption is exactly the kind of
  rule that reaches for a worked instance — the only worked instance in front of the brief is a live
  vault's.** Per `CLAUDE.md`'s worked-examples rule (build-15/build-18 precedent), the shipped edit
  uses placeholders (`{resources}`, `{field-vault}`), never a specific install's artifact paths.

### Questions deliberately left to brief time

*Per-build, not cross-cutting. Ruled Round 4 (2026-08-26) — these are deliberately unresolved and
`build-brief` decides them with the source in front of it.*

- **build-1** — the exact shape of the structured claim return (an enum over disposition kinds plus
  a named-fields list, versus a discriminated union), and its cost against `PAGE_SCAN`'s size
  budget: `JSON.stringify(PAGE_SCAN).length ≤ 3700` is a **hard release gate** measured by
  package-lint Group E6 (`tools/package-lint.py:900`). ⚠ **`PAGE_SCAN` measures 3598 in the working
  tree at v0.16.1 — 102 characters of headroom, not the ~477 the old "3223 at Cycle 12's baseline"
  figure implied (3223 is the PRE-Cycle-12 value; Cycle 12 build-1 took it to 3598).** The ruled
  structured return costs ~218 with empty description strings (+54 if the two fields join
  `required:` at `:148`); deleting the `frontmatter_issue` property it replaces returns ~98. **Net:
  over budget before one word of description is written.** The brief must name the description bytes
  it retires to pay for it — Ruling 1 retires `:159` (208 chars) for exactly this — and must
  **re-measure with package-lint's own `_E6_NODE_EXTRACTOR`, never from a source char count.**
  Build-1 is released alone, so it has no sibling to absorb the trim.
  *(roundtable A1, 2026-08-26 — measured in session by four voices independently and re-run by the
  moderator.)*
  Also: how build-1's acceptance check measures the `malformed_frontmatter` population (Q8).
- **build-2** — whether the SKILL passes fingerprint components as a list or a pre-joined string,
  and what the round-trip check's fixture is. Also: the migration sentence — the existing sidecar
  cannot be migrated (no per-page digest), so the first run is cold by construction.
- **build-3** — the exact wording of `write-verification.md` §Scope rule's class-based exemption,
  and whether it cites `extraction.md:188` or restates the principle (single-home discipline says
  cite).
- **build-4** — whether the `sources_vs_prose` direction routing lives in `checks.md` or in
  `fix-and-file.md` Step 3, and whether `.json` becomes the default persist or an alternative.

## Carried forward past Cycle 14

*(roundtable A22, 2026-08-26; John, Winston. **Cycle 14 had no such section**, and its survivals
lived in five scattered places — a sub-bullet of §Grouping & order, Q2, Q8, a ⚠ inside Q3, and the
evidence-debt list. `cycle-closeout` Stage 2's collector would have had to reconstruct all of them
from prose: the exact condition `closeout-checklist.md:74` calls "silently dropped."*
**And the rail is worse than it looks:** `closeout-checklist.md:74-75` asserts *"the next cycle's
`inbox-capture` re-lists them … anything left off is silently dropped"* — while
`inbox-capture/SKILL.md:97-100` says reading a prior cycle's closed roadmap is *"useful … but
**never required**"*, and its New-cycle path ingests nothing from the predecessor. **The carry rail
is prose on the sending end and OPTIONAL on the receiving end.** Cycle 13's carries survived only
because a human read them across. **So Cycle 14 writes its deferrals down at ideation time rather
than leaving closeout to reconstruct them — and every one carries a BOUND**, on the Cycle-12-tails
precedent, because a deferral with no bound is what carried `malformed_frontmatter` to three cycles
and A4-4(5) to four.)*

1. **A14-2 — the outbound-link ENUMERATION.** Deferred by Q1. **Bound: Cycle 15's `inbox-capture`.**
   Its filing **stays in `factory/inbox/`** (A23). *Corrected premise it inherits (A-Ruling 3): the
   deferred faces need the page's **text**, not merely "page bytes" — a per-page **scalar** is not
   the #13 route.*
2. **Cycle 13 carry-forward 1 — the `summary` paraphrase.** Deferred by Q1. **Bound: Cycle 15's
   `inbox-capture`.** ⚠ **Carson's route, recorded so the successor does not re-derive the
   deferral:** `:545` consumes `s.summary` **only** as `.trim()` and `.length` — it never reads the
   string — so a SKILL-side `{slug: summary_len}` map on the `pageHashes` precedent (`:47`, `:99`)
   closes it for ~146 integers. Likewise a mechanical `[[…]]` **count** feeds the **already-shipped**
   `partialShortfall` response at `:371-377`, killing A14-2's false orphan at a few KB. *(Owner
   Ruling 3, 2026-08-26: not taken this cycle — build-1 is the release-1 critical path and already
   over its schema budget — but the premise is corrected and the routes are named.)*
3. **Cycle 13 carry-forward 2 — the general reduce-side posture.** Partially taken by Q1; **stays
   live for the deferred half.** Bound with items 1–2.
4. **Tracker #13 (the `argsPath` route).** Not re-admitted (Q2). ⚠ **Bound: Cycle 15's
   `inbox-capture`** — at that capture #13 is re-admitted by owner ruling **or the deferral is
   re-ruled with its reason on record.** *(Without a bound, §Owner ruling's admission test re-defers
   it as net-new at every future capture on identical grounds — the loop itself.)*
5. **The `malformed_frontmatter` RETIREMENT (Cycle 13 carry-forward 3).** Third deferral, Q8.
   **Successor: the build that takes carry-forward 2.** Carries build-1's **specimen set** (not a
   count) as a Stage-2 standing metric; **E4 transfers with it, BOUND not discharged** (A19).
6. **`para_author_unknown`** — still closed to `human|agent|hybrid`, no overlay escape, **and its
   owning convention likewise unnamed** — the same defect A14-6 repairs for `type:`. Untouched (Q3).
7. **E2 — A14-4's *"frontmatter is the source of truth"* qualifier.** Scoped out unmeasured;
   **owner files it to `factory/inbox/` as a `pattern`** (A32).
8. **Inherited from Cycle 12's never-delivered hand-off** (A25): **b3(7)** (re-read on release 2's
   acceptance run), **A12-4**, **A12-5's module side**, **A11-11 d4 + A12-1's cause-fix instrument**.
9. **The `:168` dissent** (Victor, Amelia) — `:168` survives only as long as `:664` does; **when
   `unmarked_supersession` is structured, the dissent becomes the ruling.**
10. **`{field-vault}` overlay staleness** — vault-side owner action, unchanged (§Also carried).


## Deferred acceptance ledger

*Per-build `- [ ] **build-N (<slug>, briefed <date>):** …` bullets, appended by `build-brief`; form
per `factory/cycles/13-trusted-returns/roadmap.md` §Deferred acceptance ledger. Created 2026-08-26
with build-1's append — the section did not exist, and every brief in this cycle gates against it.
**Cycle ruling D3 as amended (roundtable A17) governs every bullet: BOUNDED ⇒ ship-verifiable ⇒ it
GATES**; per rule **R1** each ship-verifiable check names which seam its instrument crosses.
Also to be recorded here by build-3's brief: **Cycle 12's b3(7)**, inherited unread and landing on
release 2's acceptance run (roundtable A25).*

- [ ] **build-1 (structured-claim-return, briefed 2026-08-26):** brief
  `factory/cycles/14-no-enforcement-point/briefs/build-1-structured-claim-return.md`. **Eight checks
  — all `[ship-verifiable]`, all GATE; none field-contingent.** Release 1, cut alone; ⚠ **the first
  full lint after it is COLD by construction** (`scanFingerprint` moves — `:232-233`), never a cache
  regression.
  **(1) `[ship-verifiable]` — at rest — GATES:** the defeat mechanism is gone and the escape reports
  — over the V1 harness against shipped source, the attestation-only case is refused **whether or not
  `_detail` carries the 2026-08-26 rule-citing text**, the invented-requirement case is dropped, and
  all five controls survive (genuine break, compound break, `unclassified`, `malformed_block`,
  genuine unmarked supersession) — instrument: the V1 harness, stubbed
  `agent`/`parallel`/`phase`/`log`/`budget`, `args` as a JSON string, factory-side at rest;
  seam: **scan → reduce**; evidence: the four arrays verbatim in the BUILT `status:`.
  **(2) `[ship-verifiable]` — at rest — GATES: ⚠ THIS RE-GRADES CYCLE 13's ACCEPTANCE CHECK (2)**
  (roundtable A21) — the six subjects of `13-trusted-returns/roadmap.md:468-477`, re-scanned with the
  **post-build** `PAGE_SCAN` and prompt and run through the shipped rewritten reduce, reach **neither**
  `malformed_frontmatter` nor `unmarked_supersessions`, while `unattested_write` /
  `attestation_census` still carry them — instrument: a single-agent reader probe over **read-only
  copies of those six pages** from `{field-vault}` (never written) plus the shipped reduce, at rest;
  seam: **page bytes → scanner → reduce**, end-to-end, the only check here that crosses the agent;
  **binding, carried verbatim from Cycle 13's (2): a fixture built to exercise only the surfaces this
  build changes does NOT satisfy this check**; evidence: returned JSON + post-reduce arrays verbatim.
  **Without this check release 1 could ship and Cycle 13 still not close.**
  **(3) `[ship-verifiable]` — at rest — GATES:** the retirement landed whole and the survivors live —
  `grep -n "parseClaim\|fieldsNamed\|KNOWN_FRONTMATTER\|normalizeClaim\|claimWords\|CLAIM_FILLER\|frontmatter_issue\|frontmatter_valid" skills/`
  returns **zero**; the three surviving constant sets are **referenced from the rewritten predicates**,
  not merely defined; `node --check` parses; `:168` and `:550-557` byte-identical to v0.16.1 —
  instrument: the V3 greps + `node --check`; seam: **source agreement across the shipped tree** (named
  as such, not dressed as behavioural); evidence: grep outputs verbatim.
  **(4) `[ship-verifiable]` — at the release gate — GATES:** `JSON.stringify(PAGE_SCAN).length ≤ 3700`
  re-measured by **package-lint's own `_E6_NODE_EXTRACTOR`** (never a source char count; baseline
  3598, ruled shape 3688), and `uv run tools/package-lint.py --expect-version X.Y.Z` exits **0** with
  both version strings bumped — instrument: package-lint Groups E and D; seam: **source literal →
  runtime serialization**; evidence: the measured length + the PASS summary line in the release commit.
  **(5) `[ship-verifiable]` — at rest — GATES:** the category seam is closed on **both** sides and no
  looser — page-side and index-side `&amp;` forms each produce no `category_no_match`, numeric refs
  decode, and all three controls still flag (different category, case difference, leading space; D5
  — strictness not softened) — instrument: the V2 fixture against the shipped reduce; seam: **index
  scanner → reduce** and **page scanner → reduce**; evidence: the six `category_no_match` arrays.
  **(6) `[ship-verifiable]` — bounded to the first full `{field-vault}` sweep after release 1 —
  GATES:** the Q8/E4 `malformed_frontmatter` measurement, **as a specimen set with a bound it can
  fail** — **zero** post-repair specimens are attestation-only complaints, **zero** are
  claimed-missing documented-optional fields, and **every** remaining specimen is adjudicated one by
  one against its page as a genuine schema break (the cardinality is recorded, and is **not** the
  check); deliverable: slug + **minimal triggering fragment** per page, with corpus size and date,
  materialized under `factory/cycles/14-no-enforcement-point/` and summarized in the BUILT `status:`
  — instruments, **two and different** (A19): the persisted `{lint_reports}` archive for the
  pre-change baseline (no new sweep needed), and a **live** full sweep post-change (this build changes
  the return's shape, so pre-change recorded returns are free text the new schema cannot emit, and no
  wiki corpus ships in this repo); seam: **live page corpus → scanner → reduce** at 146-page scale;
  event: the owner runs `vlt-lint --full` on `{field-vault}` after upgrading to release 1;
  performer: the owner; vault: `{field-vault}` only. ⚠ **E4 is BOUND by this check, not discharged**
  — the debt transfers with the number to the build that takes the retirement (§Carried forward 5).
  **(7) `[ship-verifiable]` — bounded to the same sweep as (6) — GATES:** the `:664` retirement's
  exposure, measured not assumed — **no** `unmarked_supersessions` entry in that sweep is an
  attestation-only complaint and `fixes_applied:` records **no** hand-fold of a misrouted attestation
  entry, against a baseline where all three entries of the 2026-08-26 sweep were false and one was
  exactly this — instrument: the same live sweep read against the `{lint_reports}` archive baseline;
  seam: **prompt instruction (`:168`) → scanner return → reduce**, the one seam this build knowingly
  leaves with no reduce-side enforcement point; event/performer/vault: as (6). **If it fails, the
  `:168` dissent (Victor, Amelia) becomes the ruling and `unmarked_supersession` is structured by the
  successor build — this number exists to make that decision** (§Carried forward 9).
  **(8) `[ship-verifiable]` — at rest — GATES:** the vault-facing catalogue no longer asserts the
  refuted claim — `checks.md:15` carries **no** conjunction/residue prose and **no** over-reporting
  *guarantee*, describes the structured verdict and its two exclusions, states that an `unclassified`
  defect always reports, and keeps the class's legal response (R3); `checks.md:14` states the
  entity-decoded, still-exact category binding; `grep -rn "residue\|Both exclusions are conjunctions"
  skills/` returns **zero** — instrument: the V3 greps + a read of the two lines, at rest; seam:
  **module source → vault-read documentation**; evidence: grep output + the two rewritten lines.

## Roundtable review — A14-1..A14-8, the four-build batch (2026-08-26)

**Convened** over the filled Ideation rulings, before any brief, per `.claude/skills/vlt-lifecycle.md`
step 4. **`build-brief` gates on this section.** Session file:
`_output/party-mode/2026-08-26-cycle14-roadmap-roundtable-session.md`. Keepsake:
`_output/party-mode/2026-08-26-cycle14-roadmap-roundtable.html`.

**Roster — all 13 installed voices convened, none excused (owner call).** Discovered fresh by glob,
never recalled: Mary (analyst), Winston (architect), Builder, Amelia (dev), John (PM), Paige (tech
writer), Sally (UX), Carson (brainstorming), Dr. Quinn (problem-solving), Maya (design thinking),
Victor (innovation/disruption), Caravaggio (presentation), Sophia (storytelling). The owner named no
prior worries, so the roadmap's own five joints (§Next lifecycle move) were carried verbatim into
every persona prompt and are answered inline there.

**Six findings landed independently in four or more lanes** — the stale schema budget, the second
call site at `:664`, three-builds-in-`vlt-lint-full.js`, build-4's misplaced persist mandate, Q4's
missing discriminator, and D3's wrong axis. The moderator re-verified the three most consequential
in session (`PAGE_SCAN` = 3598 via package-lint's own `_E6_NODE_EXTRACTOR`; `attestationOnlyComplaint`
at `:630`/`:664`; `machine_tools` = four tools).

### Amendments applied (32)

| # | What it cures | Where it landed |
|---|---|---|
| **A1** | schema budget stale by 375 chars — build-1's ruled repair does not fit the hard E6 gate | §Questions left to brief time → build-1 |
| **A2** | `attestationOnlyComplaint`'s **second** call site at `:664` — unnamed anywhere in the batch | §Grouping → build-1 |
| **A3** | **build-3 also edits `vlt-lint-full.js`**; 7 in-prose pins E3 deliberately cannot see; 3 of them restate the rule Q4 amends | §Grouping → build-3; D2 |
| **A4** | build-2 `binds:` += Q1; "independent in substance" → **depends**; the interface stated | §Grouping → build-2 |
| **A5** | round-trip fixture: **three** runs, and the writer must be executable or the seam is uncovered | Q6 ruling 3 → build-2 |
| **A6** | Q6.1 covers **fresh AND reused** records | Q6 ruling 1 → build-2 |
| **A7** | component digests single-homed as executable steps, or half of Defect 2 survives | Q6 ruling 2 |
| **A8** | build-4's real file surface (`SKILL.md:74` is the persist home, not `report.md`) + `full-scale.md:13`'s silent wrong number | §Grouping → build-4 |
| **A9** | Q5's rationale rested on a **false premise** (`machine_tools` = 4, not 1; `uv` *is* the PEP 723 route) | Q5 |
| **A10** | build-4 **ships** the validation beat — "lets" is not "does" | §Grouping → build-4 |
| **A11** | Q4's class exemption needs a **mechanical discriminator** `vlt-lint` can evaluate, or reverts | Q4 |
| **A12** | the **transition** for the existing 27; and `contract:66` still demands the pair | Q4 |
| **A13** | Q3's pointer **target** is unsettled — and neither candidate is free | Q3 |
| **A14** | the shipped legal response excludes the blocked population (`research` is module-canonical, not vault-grown); park gets an unpark trigger | Q3 |
| **A15** | D2's narrowing **falsifies `extraction.md:188`** → 19 re-acks, not 15 | D2 |
| **A16** | `moc` recognized by a check and named in no convention | D2 |
| **A17** | **D3 rebuilt on BOUNDEDNESS** — as drafted it made fewer checks gate, not more | D3 |
| **A18** | D3's routing was untrue — **P-18 Tier C already exists**, precondition-blocked | D3 |
| **A19** | Q8/E4: the check must be able to **fail**, be a **specimen set** not a count, two instruments | Q8; E4 |
| **A20** | build-1 `binds:` += E4 (the only build-discharged debt, absent from every `binds:`) | §Grouping → build-1 |
| **A21** | **build-1 carries the check that re-grades Cycle 13 (2)** — release 1's whole purpose, unasked-for | §Grouping → build-1 |
| **A22** | a **`## Carried forward past Cycle 14`** section — 10 items, each with a bound | new section |
| **A23** | A14-2's filing pinned in the inbox against a **vacuous** Stage-5 move | §Grouping → where each went |
| **A24** | **two cycles open, `factory/CYCLE` holds one line** — the headless hazard | §Next lifecycle move |
| **A25** | "Cycle 12 can close" → **CLOSED**; its never-delivered hand-off inherited | §Next lifecycle move |
| **A26** | **two** cold sweeps, not one; the owed sweep moves to after release 2 | §Next lifecycle move |
| **A27/A28** | "seven filings" → eight (3 sites) + the admission arithmetic + the through-line's dropped **missing** case | §The through-line; §Owner ruling |
| **A35** | Q1's enum is **fail-CLOSED** where the mechanism it replaces was fail-OPEN — a fresh `ST-6` instance inside the gate-reopening build | Q1 ruling 1 |
| **A36** | §A14-7's "no study holds this cause" paragraph, superseded the same session by D4 | §Capture → A14-7 |
| **A37/A38** | build-1's retirement list completed (7 symbols + the 2 that must survive); `checks.md:15`'s second copy of the refuted claim | §Grouping → build-1 |
| **A39/A40** | `cache_rejected:` gives step 2's mandate its enforcement point; step 2's ordering clause retired with the composition move | Q6 |
| **A29–A34** | four drifted cites; §Spikes' truncated sentence; E4's round; E2 routed; E3's replacement fixture pair; E5's placeholder rule | various |

### Rules (2)

- **R1 — every brief states, per ship-verifiable check, WHICH SEAM its named instrument actually
  crosses.** *Home: `build-brief` (`references/brief-anatomy.md`, the tag section).* **Interim
  posture:** the home edit is a platform-channel change and cannot ship in this cycle, so R1 is
  **declared here and binds every Cycle 14 brief** via D3's amended text. It is the clause that
  reaches b2(5), which D3 alone does not (A17b).
- **R2 — P-18 Tier B's opening trigger gets an observer.** Its stated condition — *"a build with no
  prior failure behind it reaches brief-time and reaches for a synthetic fixture unchallenged"* —
  **is met by builds 3 and 4 and names no site obliged to evaluate it.** *Home:
  `factory/platform/roadmap.md` P-18.* **Interim posture:** if build-3's or build-4's brief reaches
  for a synthetic fixture, the brief records it in `status:` and it is named at closeout.
  **Observation duty, never a gate.**

### Disputes — owner-ruled live, dissents on record

- **`:159`/`:168`** — three-way split. **RULED: retire `:159`, keep `:168`.** `:159`'s route becomes
  unexpressible under an enum and its 208 chars are load-bearing against E6; `:168` guards
  `unmarked_supersession`, which Q1 does not structure and whose reduce-side guard build-1 removes —
  **not defence in depth, the only depth.**
  **DISSENT (Victor, Amelia):** `vlt-lint-full.js:551-557` records that prohibition as
  **field-refuted** (Cycle 12 shipped it; the next two sweeps reported the defect unchanged), and D1
  rules this same cycle that a schema description is never an enforcement point. **Deferred, not
  resolved — carried at item 9 of §Carried forward.**
- **Cycle scope** — **RULED: the four-build / two-release shape HOLDS**; the added surface is
  brief-time scoping, not a re-cut. **Builder's 19-re-ack re-pricing is NOT waived** (A15).
- **Carson's per-page scalars** — **RULED: Q1's deferral STANDS**, build-1 is the critical path and
  over budget. **The premise is corrected on the record** and both cheap routes are named for the
  successor (§Carried forward items 1–2).
- **Q5's premise** — **RULED: the `.json` direction STANDS on a corrected reason.** The
  stdlib-asymmetry argument is struck as factually false (A9).
- **D3 as a pointer** (John) — **NOT taken**; kept as a cycle-scoped tagging instruction that now
  *cites* rather than restates. **Dissent recorded** at D3.

### Obsolescence beat (P-15) — MANDATORY, and it ran

**Every persona ran it; every one returned an answer. Four retirements found, three negatives
returned explicitly.** This is the first cycle in eleven to retire anything — and the file already
knew: `vlt-lint-full.js:551-557` records the `:159`/`:168` prohibition as field-refuted eleven lines
above the guard built to supersede it.

**Retirements landed:**
1. **`vlt-lint-full.js:159`** — superseded by build-1's structured `PAGE_SCAN` return (the enum's
   range excludes the route rather than forbidding it in prose). **Landed:** build-1's block.
2. **The residue-rule apparatus** — `parseClaim` (`:593-603`), `fieldsNamed` (`:605`),
   `KNOWN_FRONTMATTER_BY_LENGTH` + its comment (`:580`/`:579`), `normalizeClaim` (`:584`),
   `claimWords` (`:585`), `CLAIM_FILLER` (`:589`), and **the `frontmatter_issue` free-text slot
   (`:163`)**. The roadmap named two of these; the room named all seven, plus the two symbols that
   must **survive**. **Landed:** build-1's block (A37).
3. **`checks.md:15`** — the same refuted safety claim in the **vault-facing** catalogue, which Q7
   would have left standing. **Landed:** build-1's block (A38).
4. **`full-scale.md` step 2's *"a digest over, in this order"* ordering clause** — superseded by
   build-2's in-workflow composition; left standing it re-creates A14-8's exact shape.
   **Landed:** Q6 (A40).
5. **`frontmatter.md:71`'s open-vocabulary clause, for the PARA population** — D2 performed this
   narrowing and did not record it as a retirement. **Landed:** D2, named.
6. **§A14-7's "no study holds this cause" paragraph** — superseded the same session by D4's opening
   of `ST-6`, and it sits in the section E5 orders build-3's brief to write from. **Landed:** A14-7
   (A36).

**Negatives returned explicitly, so the beat is answered rather than silent:**
- **`vlt-lint-full.js:168` — NOT superseded** (Winston, Carson, Paige, Sophia; owner-ruled). Kept,
  with dissent.
- **Every shipped `verbatim:` marker — NOT retirable** (Victor, having checked `:152`–`:171`). Each
  is an instruction about what the scanner must *return*; no build displaces one. *"Retiring markers
  wholesale would be the tidiness, not the retirement."*
- **D5's two re-confirmed rejections — nothing to retire** (Victor). Both are of directions **never
  built**; a rejection of an unshipped direction has no site.
- **`full-scale.md` step 4's version-skew refusal — NOT superseded** (Amelia, Caravaggio, Paige). It
  detects a stale vault-local workflow copy, a failure the round-trip check cannot observe. **Q6's
  decline stands on a real distinction.** *(Victor's related finding — that step **2** is the other
  silencer and IS made redundant — landed instead as the `cache_rejected:` amendment, A39.)*
- **`report.md:3` — rewritten by Q5, not retired.** The strictness survives; only the format
  monopoly goes.

### Out of scope, filed rather than debated (capture-don't-interrupt)

- **E2's *"frontmatter is the source of truth"* qualifier** → `factory/inbox/` as a `pattern`
  against `write-verification.md`'s tier-1 item (owner action; A32).
- **Three `cited_by:` appends** — `ST-1` (Q4 rests on *permission fused to provenance* by name),
  `ST-3` (A14-8 attributes Defect 2 to it by name), and `ST-6` (its own **instance 2**, the
  2026-08-21 decision-log filing still in the inbox — whose later capture would otherwise re-derive
  the cause D4 opened `ST-6` to prevent). *(`ST-2` and `ST-5` already carry their Cycle 14 entries.)*

**OPEN DISPUTES: none.** All four were owner-ruled live; two dissents are on record and one is
carried as a live item.

## Next lifecycle move

**Two independent tracks — neither waits on the other.**

1. **Release-1 acceptance:** the owner runs `vlt-upgrade` on `{field-vault}`, then
   `run acceptance discharge`. Build-1's checks **(6)** and **(7)** are bound to that first live
   full sweep; the other six are graded at rest and PASS.
2. **Toward release 2:** **`brief build 2`** (`build-brief`), then builds 3 and 4 — build-3 ordered
   after build-2 so `PAGE_SCAN` settles once before the re-ack pass reads it (A3).

⚠ **Before running `acceptance-discharge` or `cycle-closeout` against CYCLE 13, hand-point
`factory/CYCLE` at `13-trusted-returns` and restore it immediately after** — two cycles are open
and the pointer holds one line (A24, restated at the foot of this roadmap). Never run either headless
while that is true.

*(Superseded 2026-08-27: this line previously routed to `brief build 1`. **Build-1 is BRIEFED, BUILT
@ `ceb5cb2`, and RELEASED as v0.16.2 @ `bd985a6`, tag `v0.16.2` pushed to origin.** Its check (2)
re-graded Cycle 13's refuted acceptance check on six real vault subjects: **PASS — Cycle 13's
closeout gate is REOPENED.**)*

---

**Historical — the routing that stood until release 1.** ✅ **The roundtable CONVENED 2026-08-26 and its record is
above** (§Roundtable review — A14-1..A14-8, the four-build batch): 32 amendments applied, 2 rules
declared, 4 disputes owner-ruled live with 2 dissents on record, **no OPEN disputes**, and the
obsolescence beat run to 6 retirements and 5 explicit negatives. `build-brief`'s gate is satisfied.
Build-1 first (it alone reopens Cycle 13's gate), then builds 2, 3, 4 — **build-3 ordered after
build-2 so `PAGE_SCAN` settles once before the re-ack pass reads it** (A3).
*(Superseded: this line previously routed to `convene the roundtable`.)*

**The joints worth putting in front of the room**, named here so the session starts from them.
*(All five were put to the room 2026-08-26 and are answered below and in the Roundtable review
record. J1 was CONCEDED — it is not circular; J2 was partially conceded and re-aimed; J3, J4 and J5
were confirmed and are amended above.)*

1. **Build-1 carries the Cycle 13 gate and a measurement it has never taken.** Q8 attaches the
   `malformed_frontmatter` population measurement to the same build that changes the population.
   The room should test whether that is circular.
   → **ANSWERED: NOT circular** *(Winston, conceding after hunting for it; Amelia concurring)*.
   Q8 measures the **post-repair** population, which is the population a retirement decision needs;
   measuring pre-repair would be the error. **The faults are elsewhere** — it must be able to fail,
   it must be a specimen set not a count, and its two halves are different instruments (A19).
2. **Build-3 is 15 re-acks across two conventions in one build**, ruled by elimination over the
   cheaper precedence statement (D2). The room should test whether the `frontmatter.md` narrowing
   really cuts the populations apart, or whether it relocates the ambiguity.
   → **ANSWERED: the cut HOLDS, and it relocates the ambiguity twice over.** `{research}` defaults
   to `_agent/research/`, **outside PARA** (`module.yaml:47`), so the populations do cut apart
   (Amelia, checking the worst case; Winston concurring). **But** the narrowing falsifies
   `extraction.md:188`'s grounding sentence (**19 re-acks, not 15**) and leaves **`moc`** recognized
   by a shipped check and named in no convention — both amended into D2 (A15, A16). **And 15 was
   never the true surface: seven in-prose pins are invisible to the handshake gate** (A3).
3. **Builds 1, 2 AND 3 all edit `vlt-lint-full.js`, across two releases** — the joint as written
   named two. *(roundtable A3/A4: the interface is now stated in build-2's block, build-3's true
   surface is named in its own, and build-3 is the first to re-enter the file after release 1 has
   shipped.)*
4. **The deferred half is a promise, not a plan.** A14-2 and the `summary` paraphrase are out on
   the argument that they need real page bytes; nothing schedules the build that takes them, and
   tracker #13 is its unruled dependency (Q2).
5. **D3 is a cycle-scoped rule standing in for a lifecycle change.** `ST-5`'s own fix — splitting
   grading modality from blocking power — was noted and routed to the platform ledger. The room
   should say whether a cycle-level rule is enough or whether P-N should open now.
   → **ANSWERED: no new P-N — it already exists as P-18 Tier C, precondition-blocked** (A18). And
   the room found D3 itself was written on the wrong axis and, as drafted, **made fewer checks gate,
   not more** — restated on **boundedness** per `brief-anatomy.md:203-210`, plus an
   instrument-adequacy clause, because **D3 did not even reach b2(5)** (A17, A17b).

After the review, each ruled build goes to `build-brief` (`brief build 1`, and so on). Build-1 is
released alone; builds 2–4 ride the second release.

**Also open, outside this cycle's scope** *(roundtable A25/A24/A26, 2026-08-26 — this paragraph was
stale by one commit and acting on the stale half fires a real hazard)*:

**Cycle 12 is CLOSED — it closed 2026-08-26 at `bb3a2d8`, after this cycle's capture ran**, and
this roadmap's own frontmatter already said so while this paragraph still read *"Cycle 12 can
close."* **The cost is concrete: Cycle 12's closeout wrote a hand-off Cycle 14 never took delivery
of**, because the hand-off's stated mechanism (*"the next cycle's `inbox-capture` re-lists them"*)
**cannot fire — Cycle 14's capture ran BEFORE Cycle 12 closed. Cycle 14 is the last reader these
items get.** Inherited now, none of it build scope:
- **b3(7)** — released as a standing watch with the instruction *"re-read it after Cycle 14
  build-3, against a bundle that is no longer waiting on itself."* **That lands on release 2's
  acceptance run** and is recorded in this cycle's ledger.
- **A12-4, A12-5's module side, and A11-11 direction 4 + A12-1's cause-fix instrument** — re-listed
  unchanged in this cycle's carry-forwards at closeout. *(Cycle 12's own section labelled the last
  two "the two items most at risk of being silently dropped."*)

⚠⚠ **TWO cycles are open and `factory/CYCLE` holds ONE line.** Cycle 13 is OPEN, gate-shut, and
un-pointed; `factory/CYCLE` reads `14-no-enforcement-point`. **Both cycle-scoped skills resolve
their target from that file** (`cycle-closeout/SKILL.md:60-61`, `acceptance-discharge/SKILL.md:66-68`).
So after release 1 lands build-1, run naively: **`acceptance-discharge` would write Cycle 13's
check-(2) evidence onto CYCLE 14's ledger, and `cycle-closeout` would close Cycle 14 and — at
Stage 4 — reset `factory/CYCLE` to `none`, un-opening Cycle 14 while builds 2/3/4 are unbuilt.**
Both skills' `-H` modes skip the confirming question entirely. **Before running either against
Cycle 13, hand-point `factory/CYCLE` at `13-trusted-returns` and restore it immediately after.
Never run either headless while two cycles are open.** *(There is no three-open state — Cycle 12 is
closed. Two is already one more than the pointer can express.)*

⚠ **The two-release plan costs TWO cold full sweeps, not one, and the roadmap priced neither.**
`scanFingerprint` is derived from `pageScanPrompt(...) + JSON.stringify(PAGE_SCAN)` (`:232-233`) and
reuse is an exact key match — so **build-1 forces a cold sweep at release 1, and builds 2/3/4 force
a second at release 2.** Accepted knowingly as the price of reopening Cycle 13's gate early.
**`{field-vault}` still owes a completed full sweep — pay it on the SECOND sweep after release 2,
not "the first sweep after release 1"** (the old advice named the most expensive possible slot, days
before a second forced cold run). **Build-2's cache repair cannot be field-confirmed until two
consecutive sweeps under an unchanged ruleset**, which release 2's own contents defer past.
