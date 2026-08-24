---
title: 'Build #7 — the instrument rule (a wrapped comparison can report "identical" for
  differing files; the record must name the instrument that actually ran)'
status: 'BUILT 2026-08-24 — F1 the instrument rule landed as the new bolded paragraph
  at vault-operating-contract.md:351 (after the boundary clause :349, before Grounding
  sufficiency :353): D3 trigger verbatim (mechanically derived from an external
  instrument''s output — comparison, count, enumeration), both halves numbered,
  unwrapped-as-property, name-in-the-record, false-clean direction, ordinary-use /
  reasoned-verdict exclusions, no tool or vault named; F2 pointer clauses appended at
  vlt-upgrade SKILL.md:37 (full pointer) and :38 (second-half clause); F3 pointer clause
  at vlt-lint checks.md:43 (no finding-class change); F4 rule-card section-map row now
  "Denominators, blind spots, proxies, instruments — open before reporting any count or
  deriving a verdict from an instrument''s output" + derived_from re-stamped
  sha256:57df3488f721c98188ed1e05f11324639fdd80431d5a1f014b8f4345327b3666 (derived
  2026-08-24), card 6,957 bytes of 8,000. Verification-1: read verdict PASS — both
  halves present at D3 width with both exclusions, pointers name the contract section
  without restating mechanics; single-home sweep `grep -rn "unwrapped" skills/`
  returned exactly 4 hits — checks.md:43, vault-operating-contract.md:351,
  SKILL.md:37, SKILL.md:38 (the home + the three pointer clauses, nothing else).
  Verification-2 scrub: the only rtk|vlt-core hit across the four F-files is the
  pre-existing SKILL.md:89 vlt-core (build-8''s A11-8 scope, untouched) — zero new
  hits. Verification-3: `uv run tools/package-lint.py` → "package-lint: A/B/C/E PASS,
  D SKIPPED — vlt 0.14.0", exit 0 (C6 fresh, Group E clean; git diff confirms no
  conventions/ frontmatter touched, so Verification-4 discharged by the same run).
  Deviations/notes: (1) no deviations — all four F-sites landed as briefed, the F1
  paragraph verbatim from the brief''s draft (all load-bearing elements intact); (2)
  in-spirit extra evidence: this session''s own shell carries a command-rewriting hook,
  so every verification instrument was re-run unwrapped and is named — /usr/bin/grep
  and /usr/bin/find (the sweep, scrub, and .decision-log.md checks above are the
  unwrapped runs). No .decision-log.md existed to delete; one commit.'
module_code: 'vlt'
created: '2026-08-24'
derives_from:
  - 'factory/inbox/2026-08-23-210653-instrument-rule-for-byte-exact-comparisons.md
    (A11-7 — the instrument rule, both halves; issue #8 incl. the 2026-08-23T21:55:12Z
    second-instance comment the D3 widening answers)'
roadmap: 'factory/cycles/11-reachability/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-24): build-7 bullet (home = the operating
  contract''s Honest reporting + pointers from the two consumer sites; contract
  deliberately NOT handshaked); D3 (trigger = the bounded middle — any verdict
  mechanically derived from an external instrument''s output: comparison, count, or
  enumeration; both halves stand; narrow and wide phrasings rejected on the record);
  E5 SPLIT (a) ship-verifiable single-home + pointers check GATES closeout, (b)
  field-contingent wrapped-incident catch does not gate.'
risk: 'low — prose-only edits, no convention version: bump, no consumer walk (the
  operating contract is deliberately un-handshaked: single-home + pointers); the one
  priced release-gate cost is package-lint C6 (rule-card sha256 re-stamp, well under
  RULE_CARD_BUDGET).'
---

# Build #7 — the instrument rule

A shipped op's verdict was a byte-exact comparison, and the wrapped `diff` it reached for
reported `[ok] Files are identical` for files that genuinely differed — a false *clean*,
the direction that closes the question and never gets revisited. A second field instance
(issue #8, 2026-08-23T21:55:12Z) showed the same wrapper class corrupting a *scoping
count* (`find -newermt` returning all 147 pages where `os.stat` put the truth at
0/0/2/4). No shipped convention's declared scope covers instrument selection — the rule
is an **absence**, and the filing vault has re-derived the workaround by hand for three
consecutive upgrades because there is nothing to read.

This build states the rule once, at its confirmed single home — the operating contract's
**Honest reporting** section, which already carries the general form ("a transcription of
the record is testimony about the record, not the record") — at **D3's ruled trigger
width** (the bounded middle: any verdict *mechanically derived from an external
instrument's output* — comparison, count, or enumeration), with **both halves** intact:
(1) use an **unwrapped** instrument (a property named, never a tool, so a future wrapper
inherits the rule); (2) confirm it **actually ran** unwrapped and name it in the record.
The two consumer sites whose verdicts are byte comparisons and which today name no
instrument (`vlt-upgrade` base-vs-baseline pre-flight; `vlt-lint`
`convention_base_divergence`) gain **pointers**, never restatements.

All rejected alternatives in the parent filing and the rulings are settled — do not
re-litigate. In particular: D3 rejected both the narrow "byte-exact" trigger (misses the
second field instance) and the wide "any instrument whose output a verdict rests on"
(vacuous by breadth — this cycle's own failure mode from the opposite side); the operating
contract is deliberately NOT handshaked (no `version:` bump, no re-ack — CLAUDE.md
standing rule, confirmed by D2's inventory row for build 7).

## Brief-time dispositions

The roadmap's *Questions deliberately left to brief time* section addresses **nothing to
build-7**. The dispositions below are the brief's own bounded calls, made where the
rulings left placement and mechanics to briefing; each cites the ruling it derives from.

1. **Placement within the home: a new bolded rule paragraph inside *Honest reporting*,
   after the boundary clause (`:349`), before *Grounding sufficiency* (`:351`).** The
   section's existing rules are bolded-lede paragraphs (`:343`, `:347`, `:349`); the
   instrument rule takes the same idiom, closing with the family tie the filing's
   provenance guess and the capture both named — this is the transcription-is-testimony
   rule (`:347`) applied to an instrument class. The section's standing single-home
   line (`:345` — "the rule is stated here and cited elsewhere. A check does not word
   its own version of it") already governs the new rule; no new single-home prose is
   written. *(Derives from the build-7 bullet's "home confirmed" + D3's "home confirmed,
   and it fits".)*

2. **The skill-asset manifest walk (`skills/vlt-upgrade/SKILL.md:38`) gets a one-clause
   second-half pointer — not a full pointer, and not silence.** D3 ruled the site "still
   takes **only the second half**" (it already names `verify-skill-manifest.py` and
   in-process hashing, so half 1 is satisfied by construction). But a rule a site *takes*
   should be reachable *from* the site — the cycle's own through-line — and the script is
   itself invoked through a shell that the same wrapper class can rewrite. F2 adds one
   clause at `:38` pointing at the rule's second half (confirm the script itself ran;
   contract, *Honest reporting*). This does not enlarge E5(a)'s check: the two ruled
   consumer sites still carry their pointers, and no site restates mechanics — the `:38`
   clause is itself a pointer. *(Derives from D3's per-site effect paragraph; grounded
   against current `:38`, which invokes the script via a shell command.)*

3. **Rule-card scope: section-map row refresh + sha256 re-stamp only — no new
   act-blocking line.** Editing the contract triggers package-lint **C6** (re-derive
   `_meta/vault-rule-card.md`, re-stamp `derived_from: … sha256:`). The instrument rule
   is **not** promoted to the card's act-blocking roster: the card's roster targets
   partner acts at activation, while this rule's operators are ops sessions
   (`vlt-upgrade`, `vlt-lint`) that reach the rule through the point-of-use pointers F2/F3
   ship — the Honest reporting family already lives on the card as a section-map row
   only, and this build keeps that posture, updating the row's summary so the map stays
   honest. *(Derives from the anatomy's "no bump owed is not no cost" pricing and the
   card's own identity-bearing/act-blocking criterion; build-2 F8 is the precedent.)*

4. **No pointer proliferation beyond the named sites.** D3's practical effect — "scoping
   and enumeration queries now carry the rule" — covers *behaviors*, not fixed sites;
   they are reached through the single home's trigger wording, and any enumeration of
   "every site that runs a query" would be a list claiming completeness (CLAUDE.md:
   such lists drift). The named-pointer set stays: `:37`, `checks.md:43`, and the `:38`
   second-half clause. *(Derives from D3 + the single-home discipline.)*

5. **The shipped rule names no vault and no tool.** The filing's wrapper is one instance
   (`rtk`, in the filing vault); the shipped text names the *property* (unwrapped — no
   filtering, summarizing, or command-rewriting layer between the output and the
   verdict) and the *class* (a transparent command-rewriting layer), never the tool or
   the vault — the filing's own drafting note, and the standing scrub rule.
   *(Derives from the filing's "naming the property rather than a tool matters" +
   CLAUDE.md Git & publishing.)*

**Interim posture (R1): not applicable beyond this line** — the rule's mechanism *is* its
reachability (the single-home statement plus the point-of-use pointers), and both ship in
this build. No detection net ships, by design: the post-hoc catch is E5(b),
field-contingent and non-gating; a vault with no command-rewriting hook complies
trivially.

## F-sites

### F1 — `vault-operating-contract.md` (the single home)

Path: `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md`.

**Current state (HOLDS, re-ground 2026-08-24 post-build-2):** `## Honest reporting — what
a check may claim` at `:341`. The section carries the denominator/blind-spot rule
(`:343`), the single-home posture line (`:345`), the proxy/transcription rule (`:347` —
"a transcription of the record is testimony about the record, not the record"), and the
derive-first boundary clause (`:349`). Nothing in the section — or anywhere in `skills/`
(`grep -rn "unwrapped" skills/` returns zero) — states an instrument discipline.

**The exact change:** insert one new bolded rule paragraph after `:349`, before
`## Grounding sufficiency` (`:351`), to this effect (builder may tighten wording; the
bracketed elements are load-bearing and must all survive):

> **The instrument rule — a verdict mechanically derived from an instrument's output
> uses an unwrapped instrument, and the record names the one that ran.** An act whose
> verdict is **mechanically derived from an external instrument's output** — a
> byte-exact comparison, a count, an enumeration — (1) uses an **unwrapped**
> instrument: no filtering, summarizing, or command-rewriting layer between the
> instrument's output and the verdict. *Unwrapped* names a property, never a tool — a
> future wrapper inherits the rule without an edit. And (2) confirms the instrument
> **actually ran** unwrapped, and names in the record which one ran — a record of the
> instrument *named* is not a record of the instrument *run*: a transparent wrapper
> rewrites the very command that claims to bypass it. The dangerous direction is the
> false clean — a wrapped comparison reporting "identical", a wrapped scoping query
> reporting "everything" — which arrives as health and closes the question. Reading a
> diff to orient, or to show a human what moved, is ordinary use and untouched; a
> verdict the agent *reasoned to* is outside the rule. This is the rule above applied
> to an instrument class: what the transcription rule says about records, this says
> about the tools that produce them.

Load-bearing elements: the D3 trigger verbatim in force (*mechanically derived from an
external instrument's output — comparison, count, or enumeration*); both halves numbered;
*unwrapped* defined as a property; the named-in-the-record obligation; the
false-clean direction; the ordinary-use / reasoned-verdict exclusions (the bound that
keeps the middle bounded); no tool or vault named.

**Why:** A11-7 — the absence confirmed at capture and at triage; D3's ruled width; the
home the capture, the triage comment, and the build-7 bullet all confirmed.

**Out of scope (this site):** no edit to `:343`–`:349`; no edit to *Grounding
sufficiency*; no `version:`/`consumers:` frontmatter (the contract is deliberately
un-handshaked — D2 row, CLAUDE.md standing rule).

### F2 — `vlt-upgrade` pre-flight (consumer pointer + the manifest walk's second half)

Path: `skills/vlt-upgrade/SKILL.md`.

**Current state (HOLDS, re-ground 2026-08-24 post-build-4):** the **Base convention
divergence** bullet at `:37` — "compare to its stock baseline
`{overlays}/.baseline/{name}.md`" — names no comparison instrument. The **Skill-asset
divergence** bullet at `:38` names its instrument (`scripts/verify-skill-manifest.py`,
in-process hashing) but nothing confirms the script itself ran unwrapped.

**The exact change, two clauses:**
- At `:37`, append a pointer clause to the bullet (natural seam: after the
  vault-writable-fields exclusion clause, or at the bullet's end): *"The comparison's
  verdict is instrument-derived: use an **unwrapped** instrument and name in the
  snapshot record which one ran — the operating contract's instrument rule (*Honest
  reporting*); read it there, never restate it here."*
- At `:38`, append the second-half clause per disposition 2: *"The script names its own
  instrument (in-process hashing); the contract's instrument rule still applies in its
  second half — confirm the script itself actually ran, unwrapped (*Honest
  reporting*)."*

**Why:** the two sites whose byte-comparison verdicts name no instrument are where the
field failure actually occurred (three consecutive upgrades, bypassed by hand); the
pointer is what makes the declared rule effectively reachable at the act — the cycle's
question. Pointer, never restatement — E5(a)'s single-home check.

**Out of scope (this site):** Step 4/Step 5 report and ledger surfaces (`:91` ff.) —
they record what pre-flight found; the record-the-instrument obligation lands in the
`:37` snapshot clause, not as new report keys. No new report schema.

### F3 — `vlt-lint` `convention_base_divergence` (consumer pointer)

Path: `skills/vlt-lint/references/checks.md`.

**Current state (trivially shifted; fresh line):** the capture and E5(a) cite `:42`; the
check now lives at **`:43`** (build-6 inserted the closing-net bullet above it) —
"**Convention base divergence** (durability safety net; both modes) … compare the two,
**excluding the lines of fields declared vault-writable** …". Content unchanged; it names
no comparison instrument. Not a grounding correction — a one-line drift, recorded here.

**The exact change:** append a pointer clause to the `:43` check (natural seam: after
the compare-the-two clause, alongside the existing point-don't-restate idioms this file
already uses): *"The comparison's verdict is instrument-derived — unwrapped instrument,
named in the run's record: the operating contract's instrument rule (*Honest
reporting*); point, don't restate."*

**Why:** the third grounded byte-comparison site naming no instrument; the lint check is
the lint-time half of the same detect-and-report net as F2's pre-flight (the check's own
closing note says so).

**Out of scope (this site):** no new finding class, no change to the check's flag
vocabulary or legal response — the pointer changes how the check's operator derives the
verdict, not what the check reports (so R3 is untouched). `report.md` unchanged.

### F4 — `vault-rule-card.md` (package-lint C6 — the derived artifact)

Path: `skills/vlt-setup/assets/governance/_meta/vault-rule-card.md`.

**Current state (HOLDS):** `derived_from: 'vault-operating-contract.md
sha256:63b76a6e… (derived 2026-08-24)'`; the section map's row — `| *Honest reporting —
what a check may claim* | Denominators, blind spots, proxies — open before reporting any
count |`. Card size 6,894 bytes; `RULE_CARD_BUDGET` 8,000 (`tools/package-lint.py:261`).

**The exact change:** after F1 lands, update the row's summary to carry the new rule's
subject — e.g. *"Denominators, blind spots, proxies, instruments — open before reporting
any count or deriving a verdict from an instrument's output"* — and restamp
`derived_from:` with the new contract sha256 + derived-date. **No new act-blocking
line** (disposition 3). Stay under budget — tens of bytes against ~1,100 of headroom.

**Why:** package-lint **C6** fails the release on a stale rule-card sha; the map row
would otherwise under-describe the section it points at.

## Registration

**None.** No new skill, workflow, or help row; no convention `version:` moved, so no
consumer walk / re-ack (the operating contract is deliberately un-handshaked — D2's
build-7 row: bump *none*). The one priced gate cost is **C6** (F4): rule-card
re-derivation + sha re-stamp, under `RULE_CARD_BUDGET`. No new `package-lint` check
ships (E4 untouched); no asset `// depends_on:` header changes (E5 untouched).

## Out of scope (dispositioned)

1. **A lint/detection net for wrapped instruments** — rejected by design: no mechanical
   check can see a transparent wrapper from inside the wrapped shell; the catch evidence
   is E5(b), field-contingent. (Also the D1-adjacent economics: A11-11 is this cycle's
   own finding that lint cost scales with corpus — the cheapest lint class is the one
   not added.)
2. **A11-2's person-name residue grep and any trigger-mechanism work** —
   build-8 brief-time scope (roundtable A12); A11-2 proper is Cycle-12, spike S-3
   harvested.
3. **The migration data-equality site the filing generalized** ("a registry or tripwire
   file parsed on both sides and asserted equal") — no such shipped site was grounded at
   capture (the capture's population is the three sites F1–F3 cover); a future
   migration's equality check reaches the rule through the single home. Not enumerated —
   disposition 4.
4. **Wording changes to the Honest reporting section's existing rules** (`:343`–`:349`)
   — already shipped; the new rule joins the family, edits nothing in it.
5. **`verify-skill-manifest.py` self-attestation** (the script proving it ran unwrapped,
   e.g. an environment fingerprint in its JSON) — a mechanism candidate for a future
   filing if E5(b) shows the `:38` clause insufficient; out of A11-7's ruled scope.

## Verification (unit, at rest — lifecycle step 5)

1. **Single-home + pointers read-check (the E5(a) instrument, R1-named):** an agent-run
   read of the amended contract section confirms **both halves** present at **D3's
   trigger width** with the ordinary-use/reasoned-verdict exclusions; then
   `grep -rn "unwrapped" skills/` returns the contract home plus the F2/F3 pointer
   clauses **only**, and each pointer names the contract section without restating the
   mechanics (no property definition, no both-halves recitation outside `:341` ff.).
   Record the grep output and the read verdict in the BUILT status.
2. **Scrub check:** `grep -rn "rtk\|vlt-core" skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md skills/vlt-upgrade/SKILL.md skills/vlt-lint/references/checks.md skills/vlt-setup/assets/governance/_meta/vault-rule-card.md`
   returns zero new hits from this build — no tool names, no vault names in shipped
   text. (Note: `skills/vlt-upgrade/SKILL.md:89` carries a pre-existing `vlt-core` hit —
   that is **build-8's A11-8 scope**, not this build's; it must not be edited here.)
3. **Packaging lint:** `uv run tools/package-lint.py` — A/B/C/E must PASS (D /
   `--expect-version` is the release gate, not per-build). **C6** is the load-bearing
   check: it fails on a stale rule-card sha and on a card over `RULE_CARD_BUDGET`;
   Group E is the handshake check of record and must stay clean (this build moves no
   `version:`, so any Group E failure means an accidental frontmatter touch — stop and
   fix).
4. **Handshake bipartite re-check:** covered by Group E in item 3 — no convention
   `version:` moved (verify by `git diff` showing no frontmatter changes under
   `governance/_meta/conventions/`).
5. **R3: not applicable** — no finding class added or changed (F3 changes the operator's
   instrument conduct, not the check's flag vocabulary or legal response).
6. **R4: not applicable** — no file added to any enumerated class.

No Release section — build-7 is not the release build; the v0.15.0 bump rides the
cycle's release build.

## Acceptance (live — appended to the roadmap ledger)

Two checks (= E5's ruled halves).

1. **`[ship-verifiable]` — GATES closeout (E5(a)):** the instrument rule lands at the
   operating contract's *Honest reporting* single home with **both halves** stated
   (unwrapped instrument; confirm-it-actually-ran-and-name-it-in-the-record) at **D3's
   ruled trigger width** (any verdict mechanically derived from an external instrument's
   output — comparison, count, or enumeration), the two consumer sites
   (`skills/vlt-upgrade/SKILL.md:37`, `skills/vlt-lint/references/checks.md:43` — the
   capture's `:42`, shifted one line by build-6) carry **pointers**, and **no site
   restates the mechanics**; the rule-card row + sha re-stamp ride the same build under
   C6. **Instrument (R1):** the brief's Verification-1 protocol — agent-run read of the
   amended section + the `grep -rn "unwrapped" skills/` single-home sweep + the
   `package-lint` A/B/C/E run (C6 freshness) — factory-side, runnable at rest.
   **Evidence:** the recorded read verdict, grep output, and lint PASS line in the
   brief's BUILT status.
2. **`[field-contingent]` — does not gate (E5(b)):** a real wrapped-instrument incident
   is actually caught by the rule — an ops session performing a base-divergence,
   manifest, or scoping derivation under a command-rewriting shell hook either bypasses
   the wrapper and **names the unwrapped instrument that ran** in its record, or
   catches a wrapper interception it would previously have believed. **Vault:**
   `{field-vault}` (readable; the only known vault whose shell installs a
   command-rewriting hook — the filing's own `acceptance_vault` clause: the failure
   reproduces nowhere else, and other vaults can verify only that the rule reads
   sensibly). **Event:** the first post-v0.15.0 `vlt-upgrade` or `vlt-lint` run in that
   vault whose pre-flight/divergence derivation executes under the hook — the upgrade
   itself is scheduled (the owner runs it), but a *caught incident* is a fault condition
   nothing schedules; unbounded — goes to the standing watch register at closeout.

## Builder exit obligations

Rewrite this brief's `status:` to the BUILT record with numbered deviations; record the
Verification-1 evidence (read verdict, grep output, lint PASS) in it; delete any
`.decision-log.md` from the working tree; one commit for the build. Do not touch
`skills/vlt-upgrade/SKILL.md:89` (build-8's scope).
