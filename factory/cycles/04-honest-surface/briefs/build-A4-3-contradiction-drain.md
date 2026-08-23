---
title: 'Build #A4-3 — the contradiction drain (a bucket named `handled` that also holds things nobody handled)'
status: 'BUILT 2026-07-26 (unit-verified at rest). All eight F-sites landed as briefed. F1: `## Contradiction Callouts (with a disposition)` added between *Stale Claim Markers* and *Reading list*, `version: 1 → 2`, `consumers:` unchanged, contract pointer appended to the reading list. F2/F3/F4/F5/F7 in `vlt-lint/SKILL.md` (`:69`, `:111`, Step 4 second template + routing sentence, Step 5 four-line split + prose, `:186` tip) — `contradictions_handled:` RETIRED, not aliased. F6 in `vlt-lint-full.js`: `CLUSTER_FINDINGS` three arrays + required list, cluster prompt split-by-recorded-Disposition, reduce emits the three keys. F8: all four consumers pinned `wiki-supersession@2` (`vlt-ingest:136` and `vlt-extract:47` bodies reconciled; `vlt-track` ACK-ONLY — reconciliation found nothing to change, its `:42`/`:69`/`:96` supersession refs are proto/loop artifacts unaffected by a wiki contradiction format, a verified conformance not an oversight).
  THREE DELIBERATE DEVIATIONS, all tightenings toward the brief''s own verification checks: (1) F6.1 — the brief asked each schema description to "state the read"; the first pass also restated the `open`/`adjudicable` SEMANTICS in the descriptions, which verification 5 (single-home) forbids. Rewritten to describe the READ only ("classify by reading that line, never by judging the disagreement yourself"); the cluster agent classifies by a literal string and needs no vocabulary. (2) F5 — added one clause to the *Contradiction reporting* prose stating the SKILL composes `contradiction_scan:` itself even in full mode (workflow is read-only, `P`/`S` are the run''s own facts). The brief ruled this at F6.4 and verification 4 requires "the SKILL says it composes it", but no F-site text carried it. Placed in Step 5 rather than Step 0''s `:43` list to avoid restating that list. (3) OBSERVED, NOT CHANGED — F1''s reading-list line makes `vault-operating-contract.md` appear TWICE in that list (it was already its first entry, as the operating constitution). Kept exactly as briefed; the two entries point at different things (the constitution vs. *Honest reporting*), but a follow-up may want to merge them.
  VERIFICATION (all 12 checks): 1 handshake bipartite — four `@2` acks across shipped `SKILL.md`, zero `@1` (`skills/reports/` hits are gitignored dev artifacts + this brief, out of the shipped surface); `consumers:` names exactly those four. 2 only `wiki-supersession.md` moved `version:`. 3 zero `contradictions_handled`/`handled_contradictions` in the shipped surface. 4 both producers spell the three keys identically; `contradiction_scan:` in the SKILL only. 5 `adjudicable` DEFINED once (`wiki-supersession.md`); every other hit is a use or pointer; the callout block lives in exactly one shipped file. 6 honest-reporting wording only at `vault-operating-contract.md:252`; derive-first boundary clause only at `:256`; `vlt-lint:84` byte-unchanged (0 diff hits). 7 `node --check` exits 0, parse-on-intake untouched (0 `JSON.parse` diff hits). 8 Step 5 fence well-formed for touched lines; the pre-existing `sources_vs_prose_mismatches:` break is byte-unchanged (0 diff hits) — PRE-EXISTING, not fixed, not regressed. 9 `uv run tools/package-lint.py` → A/B/C/E PASS, D SKIPPED (not the release build, no `--expect-version`). 10 scrub clean — no vault-local/personal content in any added line. 11 dry-read Steps 2→3→4→5 coherent: surfaced at `:69` → callout with disposition → `:111` flags and routes → Step 4 template + `**Filed:**` back-write → every Step 5 slot fillable from what Steps 2–4 produce; no slot fillable only by a state nothing writes. 12 zero `.decision-log.md` in the working tree.
  NOT DONE (as briefed): no backfill, no vault-side migration, no new backlog `kind`, no frontmatter key, no version bump (A4-3 of five; version held to arc end).'
module_code: 'vlt'
created: '2026-07-26'
derives_from:
  - 'inbox/2026-07-25-160239-contradictions-have-no-drain.md (A3-20 — shapes 1+2+3 adopted, shape 4 as a stated-outcome bound; the four-bucket triage is NOT a taxonomy)'
roadmap: 'skills/reports/inbox-evolution-arc4-roadmap.md'
rulings: 'Arc-3 roadmap §Ideation rulings — A3-18..A3-23 (2026-07-25): A3-20 is its own build (five builds, one filing each; briefed apart from A4-4 despite sharing `vlt-lint`); routing, not eligibility — a second item template plus two pointers, and a disposition for the report''s handled/unhandled split; the silent-zero class gets ONE general honest-reporting rule (written by A4-2, cited here, never re-worded); verification-by-residue is a boundary clause on derive-first; A3-20''s one-vault/one-sweep evidence debt is NOT BLOCKING, carried as context.'
risk: 'moderate — a convention RULE change (`wiki-supersession` 1 → 2) with a four-consumer walk in the same build, plus a report-key retirement (`contradictions_handled`) that moves in lockstep across `vlt-lint/SKILL.md` and the `vlt-lint-full.js` workflow asset. No new skill, no new backlog `kind`, no schema key.'
---

# Build #A4-3 — the contradiction drain

## Intent

Every `vlt-lint` finding class has a **drain** — a named next owner and a state transition that ends
in the finding being gone. Contradictions have one transition (undocumented → documented) and it is
terminal and framed as success. The result is a bucket, `contradictions_handled:`, whose stated
meaning is health and which in the field held an unresolved factual error alongside genuine
scholarly disagreement, separated only by whether someone wrote a callout (A3-20's evidentiary core,
unrebutted at capture).

This build closes that with **routing and disposition, not eligibility**. Grounding at capture
established that Step 4's catch-all already admits the class (`vlt-lint:105` at capture, `:115`
today: *"and any other maintenance worth doing later"*), and the backlog vocabulary already carries
the kinds needed (`maintenance` | `knowledge-gap`, `vault-operating-contract.md:238`). What is
missing is (a) a **recorded disposition** on the documentation itself, (b) a **second item template
plus two pointers** so the adjudicable half reaches an owner, (c) a **report split** that derives
from (a) instead of from the mere existence of a callout, and (d) an honest bound on an instruction
that is unbounded today and was consequently skipped entirely (25 flagged, 0 documented on the
sweep that produced the filing).

It closes A3-20's third instance of the arc's silent-zero scar **by conformance**, not by a bespoke
fix: the general honest-reporting rule was written by A4-2 and lives at
`vault-operating-contract.md:250-256`. This build cites it and does not word its own version.

**All rejected alternatives in the parent filing are settled — do not re-litigate.** In particular:
the filing's four-bucket hand triage (11 fixable-now / 4 need-external-evidence / 8 genuine framing
/ 2 source-check) is **evidence that the distinctions exist and are actionable, not a proposed
taxonomy** — the ruling carries that instruction explicitly, and no F-site below adopts it. The
"contradictions are features" instinct is deliberately kept, not removed. Detection is not broken;
this is disposition and visibility only.

**Briefed apart from A4-4 (source fidelity), by capture's explicit instruction.** The Jonah/Alaric
pair is one symptom with two independent causes; entity substitution at ingest is A4-4's subject and
is out of scope here (§Out of scope).

## Brief-time dispositions

The roadmap left A4-3 two questions (Arc-3 roadmap, *Questions deliberately left to brief time*:
ODQ #5 and ODQ #6). Both are ruled here, with the consequential calls that fall out of them.

**1. ODQ #5 — which shapes ship: 1 + 2 + 3, with 3 as the mechanism.**
The filing offered four shapes and rated 1+2 complementary. Grounding makes 3 the load-bearing one
and the other two its consequences:

- **Shape 3 (the callout carries a disposition) is the mechanism.** Without a recorded disposition
  there is nothing for a report split to read, and the split would have to be inferred from the
  existence of a callout — which is exactly the inference the build exists to kill.
- **Shape 1 (split the bucket) is its report consequence**, and is therefore *derived*, not stored.
- **Shape 2 (give the adjudicable half a drain) is its routing consequence** — an item that is now
  labelled adjudicable needs an owner, and Step 4 already admits it.
- **Shape 4 is ruled separately at disposition 3** — adopted, but not as the filing's "top N by
  severity".

Nothing here is a new eligibility rule. This is the ruling's "routing, not eligibility" applied.

**2. Where the split's truth lives: on the page, in the callout — derived, never counted.**
The report reads each documented contradiction's recorded disposition off the page and tallies. No
stored counter, no new frontmatter key, no `frontmatter@5`. This is derive-first held straight
(A4-1's precedent, and the same call SPIKE-2 forced there).

It is also the **boundary clause on derive-first** applied, and the clause names this exact hazard:
today's report infers *managed* from the residue of the documenting process (a callout exists ⇒ the
disagreement is managed). The disposition is **recorded by whoever documents the contradiction**, so
the check reads a state, not a leaving. The clause lives at `vault-operating-contract.md:256` and is
read there, not restated (A4-2 relocated it out of `vlt-lint` for exactly this reason; `vlt-lint:84`
is a pointer and stays one).

**3. ODQ #6 — `vlt-lint:69` is bounded, as a STATED OUTCOME, not a numeric cap.**
The filing offered "top N by severity, or an explicit judgment call so skipping becomes a stated
outcome". **Ruled: the second.** A top-N bound requires a severity ordering, and the only severity
ordering in evidence is the Librarian's four-bucket hand triage — which the ruling forbids adopting
as a taxonomy. Inventing a different one at brief time would be pre-generalizing from one sweep,
against the arc's standing ruling on that.

Concretely: documenting is an explicit judgment call bounded by cost, and **the run reports what it
declined to document**. The 25/0 skip stops being invisible without anyone deciding which 25 mattered.
This is build-23's `vlt-lint:74` honest-limit posture extended, and it conforms to the general
honest-reporting rule rather than wording a new one.

**4. `contradictions_handled:` is RETIRED, replaced by a three-valued split.**
Not renamed, not kept alongside — retired. Its name is the defect the filing names: *"a
classification where writing a sentence converts a factual error into a documented feature."* Keeping
it as a compatibility slot would keep the health claim in the report. The three values are
`contradictions_open` (documented, disposition `open` — documentation *is* the resolution; the only
slot that may read as health), `contradictions_deferred` (documented, disposition `adjudicable` —
carries what would close it and its backlog ref; **not** health), and
`contradictions_undispositioned` (documented before this convention landed, or documented without a
disposition — the honest third value).

The third value is deliberate and mirrors A4-2's `convention_adoption:` shape: the honest answer to
"we cannot classify these" is a named third state, never silence and never a default into either
real bucket. **No backfill sweep ships** — see disposition 6.

**5. The contradiction callout is specified for the first time, in `wiki-supersession.md`, at the
cost of `version: 1 → 2` and a four-consumer walk.**
Grounding addition (§F1): **no shipped file specifies how a contradiction is documented.**
`vlt-lint:69` says *"Document in both pages' Contradictions/Open Questions"*; `vlt-ingest:134` names
`**Contradictions / Open Questions**` as a page section; `vlt-extract:47` reads *"a Contradictions
section"*. Three skills reference a shape that exists nowhere. `wiki-supersession.md` covers
contradiction only as a **reason value** on the supersession callout (`:40`, `contradicted`) — the
capture's "write-side only" reading holds, but there is less there than "covers conflicting claims"
suggests.

Since the shape must be written anyway to carry a disposition, it is written **once**, in the
convention that owns visible-knowledge-change, and the three skills point at it. The alternative —
stating the callout in `vlt-lint` only — was rejected: `vlt-ingest` writes contradictions too
(`:136`), so lint-local mechanics would be restated at the write site within one build, breaking
single-home discipline.

**The handshake cost is accepted and named up front, not discovered at implementation.** A new
required callout format is a **rule change**, not a prose clarification: `wiki-supersession` goes to
`version: 2` and **all four listed consumers re-ack in this same build** — `vlt-ingest`, `vlt-lint`,
`vlt-extract`, `vlt-track` (CLAUDE.md version-handshake rule; the consumer walk is named in
§Registration and verified bipartite in §Verification).

**6. No backfill, and no vault-side migration.**
Existing documented contradictions are **not** swept and re-dispositioned by this build or by the
first lint run after it. They render `undispositioned`, which is the true statement about them. A
backfill would mean a judgment pass over every documented contradiction in a mature vault —
precisely the unbounded, low-reversibility write disposition 3 just ruled must be a stated judgment
call. The count drains as pages are touched. (Same posture as A4-2's deliberate non-stamping of the
five `checked`-stage conventions: the report's third value covers them honestly.)

**7. No new backlog `kind`.**
`maintenance` (fixable from the vault's own pages) and `knowledge-gap` (needs external evidence) are
already defined at `vault-operating-contract.md:238` and `frontmatter.md:214-217`, and the filing's
own routing split — *"routed to `vlt-ingest` (needs a source) or the owning partner (fixable from the
vault)"* — maps onto them exactly. Capture said the vocabulary already supports it with no new type;
grounding confirms.

**8. The "features, not bugs" tip is kept and qualified, not removed.**
The filing states plainly it does not want the instinct removed; the defect is that it is applied to
a bucket that also contains things nobody managed. With the bucket split, the tip becomes true of
the bucket it names (F7).

## F1 — `{conventions}/wiki-supersession.md`: the contradiction callout, carrying a disposition

**Current state.** `skills/vlt-setup/assets/governance/_meta/conventions/wiki-supersession.md`:

- `:11-15` — `version: 1`, `consumers: [vlt-ingest, vlt-lint, vlt-extract, vlt-track]`,
  `enforcement_stage: checked`, `enforcement_checked_by: vlt-lint`, `enforcement_moment: lint run`.
- `:26-46` — *Claim-Level Supersession (Inline)*, whose callout carries
  `**Reason:** updated | contradicted | refined | retracted` (`:35`) with `contradicted` defined at
  `:40` as *"a new source directly conflicts with the old claim; both may still have merit."*
- `:48-63` — *Page-Level Supersession*; `:65-75` — *Stale Claim Markers*; `:77-82` — *Reading list*.
- **There is no contradiction-documentation format anywhere in the file, or anywhere in the shipped
  surface** (grounding addition — see §Grounding corrections & additions).

**The exact change.** Add one section, **after *Stale Claim Markers* (`:75`) and before *Reading
list* (`:77`)** — it is the third marker class, and the file's existing order runs claim-level →
page-level → stale:

```markdown
## Contradiction Callouts (with a disposition)

A contradiction is **two credible claims that cannot both hold** — across two pages, within one
page, or between a `{research}` note and the wiki. It is documented in **both** pages'
`## Contradictions / Open Questions` section, and never silently resolved by picking a winner.

Documentation alone is not a resolution. Every contradiction callout carries a **disposition** —
which kind it is, and, when it is adjudicable, what would close it:

​```markdown
> [!contradiction] <short claim> (YYYY-MM-DD)
> **This page:** <what this page claims>
> **[[other-page]]:** <what the other page claims>
> **Recency/authority:** <which source is more recent or more authoritative — stated, not acted on>
> **Disposition:** open | adjudicable
> **Closes when:** <adjudicable only — the bounded act that would settle it>
> **Filed:** <adjudicable only — the `{backlog}` item this was filed as>
​```

**Disposition values:**
- `open` — two credible sources genuinely disagree and the vault should hold both. **Documentation
  is the resolution**; there is nothing further to do and nothing to file. A well-documented
  disagreement beats false certainty.
- `adjudicable` — one side is simply wrong, or one page is stale, and a **bounded act** closes it.
  Documentation is a deferral, not a resolution: `**Closes when:**` names the act, and the
  contradiction is filed to `{backlog}` (`maintenance` when the vault's own pages settle it,
  `knowledge-gap` when it needs external evidence).

Choosing between them is judgment work and belongs to whoever holds the context — the writer at
ingest time, or the human at sweep time. **A callout with no `Disposition:` is not an error**;
callouts predating this convention have none, and checks report them as their own third value
rather than defaulting them into either bucket (`vault-operating-contract.md`, *Honest reporting*).
No sweep backfills them.
```

Then bump the frontmatter: `:11` `version: 1` → `version: 2`. The `consumers:` list at `:12` is
**unchanged** (all four are already listed and all four re-ack — see §Registration).

Add one line to the *Reading list* (`:77-82`), after the `wiki-consolidation.md` entry:

```markdown
- `vault-operating-contract.md` — *Honest reporting*: what a check may claim about a disposition it cannot read
```

**Why.** Shape 3 of the filing, and the mechanism disposition 1 rules load-bearing. Single-home:
this is the only place the callout's shape and the disposition vocabulary are stated; F2, F3, F4 and
`vlt-ingest` point at it and restate nothing.

**Out of scope at this site.** The `[!superseded]` reason value `contradicted` (`:40`) is
**unchanged** — it marks a claim that a *new source* replaced or challenged during a write, which is
a different event from two standing claims that disagree. Do not merge the two callouts; do not
cross-reference them beyond what the section text above already says.

## F2 — `vlt-lint:69`: the contradictions check gets a pointer, a route, and a stated bound

**Current state.** `skills/vlt-lint/SKILL.md:69` (Step 2, Tier 2), verbatim:

> - **Contradictions** — incompatible claims across two pages, self-contradictions within a page, or `{research}` findings that conflict with the wiki. Document in both pages' Contradictions/Open Questions; note which source is more recent/authoritative, but never silently pick a winner.

*(Grounding: this line is the one A3-20 site whose number is unchanged since capture — see
§Grounding corrections & additions.)*

**The exact change.** Replace `:69` with:

> - **Contradictions** — incompatible claims across two pages, self-contradictions within a page, or `{research}` findings that conflict with the wiki. Document in both pages' `## Contradictions / Open Questions` **using the contradiction callout with its disposition** (`{conventions}/wiki-supersession.md`, *Contradiction Callouts* — the format and the `open`/`adjudicable` vocabulary live there, not here); note which source is more recent/authoritative, but never silently pick a winner. A contradiction dispositioned **`adjudicable`** is filed to `{backlog}` in Step 4 — that is its drain, exactly as a merge candidate's is. **Documenting is a bounded judgment call, not an obligation:** on a large sweep, documenting every contradiction found is a heavy, low-reversibility write, so document what earns it and **report the rest as declined, with the count** (Step 5 `contradictions:` plus the `contradiction_scan:` line) — a silent skip is under-delivery the report cannot see (`vault-operating-contract.md`, *Honest reporting*).

**Why.** Three of the filing's four shapes land on this one line: the pointer to the callout (shape
3, the disposition's home), the route to Step 4 (shape 2, the drain the filing showed merges get
inline and contradictions do not), and the stated-outcome bound (shape 4 per disposition 3 —
`:69` is unbounded today and was skipped entirely on a 130-page sweep).

**Out of scope at this site.** No severity ordering, no top-N, no adoption of the four-bucket
triage. The check's *detection* behaviour is unchanged — capture and the filing both state detection
works (the cluster pass caught a cross-page conflict a human would not have).

## F3 — `vlt-lint:111`: the do-not-auto-apply list stops being asymmetric

**Current state.** `skills/vlt-lint/SKILL.md:111` (Step 3), verbatim — **grounding correction: the
capture cites `:101`; A4-1 and A4-2 shifted this line to `:111`, text byte-unchanged**:

> Do **not** auto-apply: page deletions (flag), contradiction resolutions (document both, flag), page merges (file to backlog — see Step 4), or **convention-coherence drift** (flag — a stale `depends_on` ack must be cleared by a human reconciling the consumer against the convention and then bumping the ack; lint must never bump the integer itself, or it would rubber-stamp conformance it didn't verify).

**The exact change.** Replace the contradiction clause only, leaving the rest of the sentence
byte-identical:

- from: `contradiction resolutions (document both, flag)`
- to: `contradiction resolutions (document both **with a disposition**, flag; file the `adjudicable` ones to backlog — see Step 4)`

**Why.** This is the sentence the filing put its finger on: *"merges get an explicit drain named
inline; contradictions get a full stop"* — one sentence, two classes, treated differently. After the
change the two clauses are symmetric and the asymmetry the filing named is gone at its own site.
Auto-**resolution** stays forbidden, unchanged — the drain routes to a human or a partner, never to
lint.

## F4 — `vlt-lint` Step 4: the second item template and the routing sentence

**Current state.** `skills/vlt-lint/SKILL.md:113-121` — **grounding correction: the capture cites
`:105`/`:108`/`:111`; A4-1 and A4-2 shifted them to `:115`/`:118`/`:121`, text byte-unchanged**:

- `:115` — *"For each near-duplicate/merge candidate (and any other maintenance worth doing later), append a `maintenance` item to `{backlog}` under `## Open`, then **mention it in-flow** (capture is cheap and never silent):"*
- `:117-119` — the fenced merge item template.
- `:121` — *"The merge itself is resolved later by `vlt-ingest` under the consolidation discipline — lint finds, ingest resolves."*

The catch-all at `:115` **already admits contradictions** — the capture's ⚠️ correction, which is
what makes this build routing rather than eligibility. What is missing is a template and a named
resolver: `:118` and `:121` are both merge-shaped.

**The exact change.** Keep `:115` and the merge template `:117-119` exactly as they are. After the
merge template, add a second template and extend the routing sentence:

```markdown
For each contradiction dispositioned **`adjudicable`** (Step 2 / `{conventions}/wiki-supersession.md`), append its item too — `maintenance` when the vault's own pages settle it, `knowledge-gap` when it needs a source the vault doesn't have:

​```
- [ ] Adjudicate <page-a> vs <page-b>: <the claim in conflict> (maintenance|knowledge-gap, by: <partner>) — closes when: <the bounded act from the callout>
​```

Record the filed item back in the callout's `**Filed:**` line, so the page and the backlog agree.

The merge itself is resolved later by `vlt-ingest` under the consolidation discipline — lint finds, ingest resolves. An adjudicable contradiction resolves the same way when it needs a source (`vlt-ingest`, holding the new source, applies the supersession rules); when the vault's own pages already settle it, the owning partner resolves it in ordinary work. Either way the callout's disposition is updated or the callout removed when the contradiction is gone — **that is the state transition contradictions previously lacked.**
```

**Why.** Shape 2. `:121`'s replacement gives the class the two things every other finding class has:
a named next owner and a transition that ends in the finding being *gone*.

**Out of scope at this site.** No escalation of an aging contradiction queue — that is a **tripwire
concern (the enforcement kit), not lint's**, mirroring the `review_due` line at `:62` and the
graduation-queue line at `:96`. Lint files; the kit escalates. Do not add a nag.

## F5 — `vlt-lint` Step 5: the report split and its denominator

**Current state.** `skills/vlt-lint/SKILL.md:160-161` — **grounding correction: the capture cites
`:150` for `contradictions_handled`; A4-1 and A4-2 shifted it to `:161`, text byte-unchanged**:

```yaml
  stale: [<page — reason>, ...]
  contradictions: [<page-a vs page-b: claim>, ...]          # unhandled — no callout yet
  contradictions_handled: [<page-a vs page-b: claim>, ...]  # already documented — surfaced, not vanished (a managed disagreement is a feature)
  thin_pages: [<page>, ...]
```

**The exact change.** Replace the two contradiction lines (`:160-161`) with four, keeping `stale:`
and `thin_pages:` and their positions untouched:

```yaml
  contradiction_scan: <P pages compared; D documented, U carrying no disposition; S surfaced-but-declined this run>   # denominator + the stated bound — a bare zero below is not health
  contradictions: [<page-a vs page-b: claim>, ...]                    # surfaced this run, no callout yet
  contradictions_open: [<page-a vs page-b: claim>, ...]               # documented, disposition open — documentation IS the resolution
  contradictions_deferred: [<page-a vs page-b: claim — closes when: X | backlog: <item>>, ...]   # documented, disposition adjudicable — NOT health
  contradictions_undispositioned: [<page-a vs page-b: claim>, ...]    # documented before the disposition convention, or without one — unclassifiable, stated as such
```

`contradictions_handled:` is **removed**, not aliased (disposition 4).

Add one line of prose under the fence, adjacent to the existing `files_checked` counting rule at
`:172`, in the same register:

> **Contradiction reporting.** The three documented slots are **derived from each callout's recorded `Disposition:`**, never from the existence of a callout — a callout with no disposition is `undispositioned`, never defaulted into either real bucket. `contradiction_scan:` carries the denominator and the run's stated bound: how many contradictions were surfaced and deliberately **not** documented (`S`), so a skipped triage is visible rather than silent. Per the operating contract's honest-reporting rule — read it there; this line does not restate it.

**Why.** Shape 1, derived from shape 3 (disposition 2). The denominator and the declined count are
this build's conformance to the general rule A4-2 wrote — the arc's third silent-zero instance
closes by conforming, not by a bespoke fix (the ruling's explicit consequence for scoping).

**Out of scope at this site.** No dashboard/HTML rendering change (`:172`'s optional rendering offer
is untouched). The **pre-existing** strict-YAML fence break at `sources_vs_prose_mismatches:`
(`:138`, recorded PARTIAL at A4-2 verification 7) is **not** fixed here and must not be regressed —
its disposition stays with capture (`inbox/2026-07-25-193000-report-slot-with-no-check.md`).

## F6 — `vlt-lint-full.js`: the workflow emits the same split

**Current state (grounding addition — the capture did not name this file).**
`skills/vlt-setup/assets/workflows/vlt-lint-full.js` produces the report slots the SKILL's Step 5
declares, so the key retirement in F5 cannot land in the SKILL alone:

- `:105-114` — `CLUSTER_FINDINGS` schema: `required: ['cross_page_contradictions', 'handled_contradictions']`, with `handled_contradictions` described as *"GAP B — disagreements in this cluster that ARE already documented…"*.
- `:230-232` — the cluster-agent prompt: *"…and SEPARATELY list disagreements that ARE already documented with a Contradictions section or callout (handled — Gap B…)."*
- `:270-272` — the reduce: `contradictions: flat('cross_page_contradictions').concat(collect('within_page_contradictions'))` and `contradictions_handled: flat('handled_contradictions')`.
- `:88` — the per-page schema's `within_page_contradictions` (feeds `contradictions:`; unchanged).

**The exact change.**

1. `CLUSTER_FINDINGS` (`:105-114`): replace `handled_contradictions` with three arrays —
   `documented_open`, `documented_adjudicable`, `documented_undispositioned` — and set
   `required: ['cross_page_contradictions', 'documented_open', 'documented_adjudicable', 'documented_undispositioned']`.
   Each description states the read: the agent reads the callout's `**Disposition:**` line and
   classifies by it; **a callout with no disposition goes to `documented_undispositioned` and is
   never guessed into `open` or `adjudicable`.**
2. The cluster prompt (`:230-232`): replace the "SEPARATELY list disagreements that ARE already
   documented (handled — Gap B)" clause with an instruction to split documented disagreements by
   their recorded `Disposition:` into the three arrays, stating explicitly that an absent
   disposition means `undispositioned` — **do not infer one**. Keep the unhandled clause unchanged.
3. The reduce (`:270-272`): replace the `contradictions_handled:` line with
   `contradictions_open: flat('documented_open')`,
   `contradictions_deferred: flat('documented_adjudicable')`,
   `contradictions_undispositioned: flat('documented_undispositioned')`. `contradictions:` is
   unchanged.
4. The `contradiction_scan:` denominator is **not** emitted by the workflow — the SKILL composes it,
   because `P`/`S` are the run's own facts (`files_checked` and what this run declined to document),
   and the workflow is read-only and does not document anything. The SKILL fills it, exactly as it
   already fills `para_missing_attestation`, the governance checks, and the candidacy pass (`:43`).

**Why.** Single report shape, two producers — they must agree or a full-mode sweep silently emits a
retired key. `vlt-lint`'s ack covers its own workflow assets (`vlt-lint:74`), so this adds **no**
extra handshake entry.

**Out of scope at this site.** No change to chunking, budget guards, model tiering, `clusterCap`, or
the coverage-cap reporting; no `{research}` zone for the workflow (still the named second-cut work,
`vlt-lint:43`). The args-parse-on-intake contract is untouched.

## F7 — `vlt-lint:186`: the tip is qualified, not removed

**Current state.** `skills/vlt-lint/SKILL.md:186` (Tips) — **grounding correction: the capture cites
`:175`; A4-1 and A4-2 shifted it to `:186`, text byte-unchanged**:

> - **Contradictions are features, not bugs** — a well-documented disagreement beats false certainty. Say so loudly, don't quietly pick one.

**The exact change.**

> - **An *open* contradiction is a feature, not a bug** — a well-documented disagreement between two credible sources beats false certainty. Say so loudly, don't quietly pick one. **An *adjudicable* one is a deferral wearing that costume:** one side is wrong or stale, a bounded act would close it, and it belongs in the backlog with what would close it. The disposition on the callout is what tells them apart — never the fact that someone wrote a callout.

**Why.** The filing states the instinct is good and explicitly does not want it removed; the defect
is that it is applied to a bucket that also holds things nobody managed. With the bucket split, the
tip becomes true of the bucket it now names. The closing clause is the shape-3 rationale in one line
at the site most likely to be read casually.

## F8 — the consumer walk: `vlt-ingest`, `vlt-extract`, `vlt-track`, `vlt-lint`

`wiki-supersession` moves to `@2` (F1), so **every listed consumer re-acks in this build**, and the
ack means the consumer was reconciled against the changed convention (`vlt-lint:111`) — not just
that an integer moved.

**`vlt-ingest/SKILL.md`**

- `:4` — `depends_on:` `"wiki-supersession@1"` → `"wiki-supersession@2"`.
- `:136` — currently: *"**Supersession (required).** …apply the `[!superseded]` / `[!stale]` / page-level patterns from `{conventions}/wiki-supersession.md`. Never silently overwrite; document both sides of a genuine, unresolved contradiction rather than picking a winner."* Extend the final clause to point at the callout and its disposition: documenting both sides now means writing the contradiction callout **with its disposition** per that same convention — `open` when the writer is holding two credible sources that genuinely disagree, `adjudicable` when the writer can see the bounded act that would close it but is not the one to do it (in which case it is filed to `{backlog}`, the write-side counterpart of lint's Step 4). **Restate no mechanics** — one clause plus the pointer.
- `:134` — the page-section list already names `**Contradictions / Open Questions**`; **unchanged**.

**`vlt-extract/SKILL.md`**

- `:4` — `"wiki-supersession@1"` → `"wiki-supersession@2"`.
- `:47` — currently: *"**Carry forward caveats.** When a source page carries marked contradictions (`[!superseded]`/`[!stale]`, or a Contradictions section), note that caveat in the artifact…"* Add one clause: an `open` contradiction is carried as a genuine caveat ("sources disagree"); an `adjudicable` one is a **known unresolved error** and is carried as that, not as a balanced disagreement. Pointer only, no restated vocabulary.
- `:46` (surface contradictions, don't resolve silently) — **unchanged**.

**`vlt-track/SKILL.md`**

- `:4` — `"wiki-supersession@1"` → `"wiki-supersession@2"`. **Ack-only**: `:42`, `:69` and `:96`
  reference supersession callouts for proto/loop artifacts and are unaffected by a wiki
  contradiction format. Record in the build's `status:` that reconciliation found nothing to change
  here — an ack with no body edit is a verified conformance, not an oversight.

**`vlt-lint/SKILL.md`**

- `:4` — `"wiki-supersession@1"` → `"wiki-supersession@2"`. Its body reconciliation is F2/F3/F4/F5.

## Registration

**None.** No new skill, no new workflow, no new dispatch mode — so `module-help.csv` is untouched and
its 13-column canonical header is not in play. No new backlog `kind` (disposition 7), no new
frontmatter key, no `frontmatter` version move.

**One consumer walk, named:** `wiki-supersession` `version: 1 → 2` (F1) ⇒ re-ack in
`vlt-ingest`, `vlt-lint`, `vlt-extract`, `vlt-track` (F8), all in this build, verified
bipartite-consistent (§Verification 1–2). No other convention's `version:` moves.

**Not the release build** — this is A4-3 of five; the owner is holding the version to arc end
(A4-1's build-time call, carried by A4-2). No `marketplace.json` / `module.yaml` bump here, and
`--expect-version` is not run.

## Out of scope (dispositioned)

- **Entity substitution at ingest (the auto-caption class).** → **A4-4**, briefed apart by capture's
  explicit instruction. The Jonah/Alaric pair is A3-20's *evidence* and A3-21's *subject*; this build
  fixes how such a finding is dispositioned, not why the vault holds a wrong name. A page fixed by
  A4-4 is a contradiction that drains through this build's route — that is the intended interaction,
  not a dependency.
- **The four-bucket triage as a taxonomy** (11 fixable-now / 4 external-evidence / 8 framing /
  2 source-check). → **Rejected as scope**, per the ruling's explicit instruction and the filing's own
  honest limit. `open`/`adjudicable` is a two-value disposition, not a bucket scheme; the triage
  remains evidence that the distinction is actionable.
- **Backfilling existing documented contradictions.** → **Deliberately not done** (disposition 6);
  they render `undispositioned`.
- **Escalating an aging contradiction backlog.** → **Tripwire concern (the enforcement kit), not
  lint's** — same posture as `review_due` (`vlt-lint:62`) and the graduation queue (`:96`).
- **A `contradictions` counter, key, or stored state.** → **Rejected** — derive-first, disposition 2.
- **`vlt-query:33` (rank contradictions, don't bury them) and `vlt-agent-librarian:37-38`.** →
  **Untouched.** Neither is a `wiki-supersession` consumer; both *point at* the behaviour rather than
  restating mechanics, so a rule change leaves them correct (the "points, doesn't recite" test at
  `vlt-lint:74`).
- **The `[!superseded]` `contracted`/`contradicted` reason value.** → **Unchanged** (F1
  out-of-scope note): a source replacing a claim is a different event from two standing claims
  disagreeing.
- **`sources_vs_prose_mismatches:` (the declared report key no check fills).** → **Stays with
  capture** — A4-2 dispositioned it: honesty half closed by the general rule, missing-check half is a
  wiki-side question for capture to rule (`inbox/2026-07-25-193000-report-slot-with-no-check.md`).
- **Giving `vlt-lint-full.js` a `{research}` zone.** → **Named second-cut work** (`vlt-lint:43`),
  not this build.

## Verification (unit, at rest)

1. **Handshake bipartite.** `grep -rn "wiki-supersession@" skills/` returns exactly four hits, all
   `@2` (`vlt-ingest`, `vlt-lint`, `vlt-extract`, `vlt-track`); `wiki-supersession@1` returns **zero**.
   Cross-check the other direction: `wiki-supersession.md:12`'s `consumers:` names exactly those four
   and each is installed.
2. **No other convention moved.** `git diff` shows a `version:` change in
   `conventions/wiki-supersession.md` only; no other `version:`/`consumers:` line in
   `governance/_meta/conventions/*.md` is touched.
3. **Retired key is gone everywhere.** `grep -rn "contradictions_handled\|handled_contradictions" skills/`
   returns **zero** hits across the SKILL and the workflow asset.
4. **The two producers agree.** The contradiction slots in `vlt-lint/SKILL.md` Step 5 and the object
   assembled in `vlt-lint-full.js`'s reduce carry the same three key names, spelled identically;
   `contradiction_scan:` appears in the SKILL only (F6.4) and the SKILL says it composes it.
5. **Single-home.** `grep -rn "adjudicable" skills/` shows the **vocabulary defined once**, in
   `conventions/wiki-supersession.md`; every other hit is a use or a pointer, never a restated
   definition. Likewise the callout block appears in exactly one file.
6. **No restated honest-reporting rule.** The wording *"a count whose only attainable value"* /
   *"must state what it cannot see"* appears **only** in `vault-operating-contract.md:252`; F5's prose
   points at it. Same check for the derive-first boundary clause (`:256`) — `vlt-lint:84` stays a
   pointer and is byte-unchanged by this build.
7. **The workflow still parses and still parses its args.** `node --check
   skills/vlt-setup/assets/workflows/vlt-lint-full.js` exits 0; the parse-on-intake block at the top
   of the file is unchanged (CLAUDE.md standing rule).
8. **The Step 5 fence.** The `yaml` fence in Step 5 is well-formed for the lines this build touches.
   The pre-existing `sources_vs_prose_mismatches:` break (`:138`) is **byte-unchanged** — record it as
   pre-existing (A4-2 verification 7's PARTIAL), never as fixed and never as newly broken.
9. **Packaging lint.** `uv run tools/package-lint.py` — Groups A/B/C/E PASS (E is the mechanical net
   for the handshake in check 1). `--expect-version` is **not** run: not the release build.
10. **Scrub.** No vault-local or personal content in any changed shipped file — no `vlt-core`, no
    Schottenheimer/Flores, no Jonah/Alaric, no real page slugs from the field sweep. The F1 callout
    example uses placeholder text (`<short claim>`, `[[other-page]]`), never a live artifact path
    (CLAUDE.md worked-examples rule).
11. **Dry-read for coherence.** Read `vlt-lint` Steps 2 → 3 → 4 → 5 end-to-end as one flow: a
    contradiction surfaced at `:69` reaches a callout with a disposition, an `adjudicable` one reaches
    Step 4's template, and Step 5's slots can be filled from what Steps 2–4 actually produced. No slot
    is fillable only by a state nothing writes (the `sources_vs_prose_mismatches` failure mode).
12. **No `.decision-log.md`** anywhere in the working tree when the build finishes (CLAUDE.md).

## Acceptance (live — appended to the roadmap ledger)

Rides the next ordinary `vlt-core` upgrade plus the first full `vlt-lint` sweep after it. Carried as
context, not as a tail: **A3-20's evidence is one vault, one sweep (130 pages), and the mechanism is
size-sensitive by nature** — a smaller vault may have no contradictions at all, and that is not a
failure of this build (ruled NOT BLOCKING at ideation).

1. **Both pointers reach the field.** After upgrade the installed `vlt-lint` routes contradictions
   at Step 4 and points at the callout convention (F2), and the do-not-auto-apply line names the
   drain symmetrically with merges (F3). The asymmetry the filing found in a single sentence is gone
   from the installed text.
2. **The drain actually runs.** On the first post-upgrade full sweep, at least one contradiction
   dispositioned `adjudicable` is filed to `{backlog}` — `maintenance` or `knowledge-gap`, mentioned
   in-flow, naming what would close it — and appears in the report's `backlog_filed:`. **Failure
   signature:** a sweep reporting entries in `contradictions_deferred` with an empty `backlog_filed`
   (the disposition landed, the drain did not).
3. **The split is real and derived, not inferred.** The report emits `contradictions_open` /
   `contradictions_deferred` / `contradictions_undispositioned` and **no** `contradictions_handled`,
   and each classified entry traces to a `**Disposition:**` line written on the page — spot-check
   three entries against their callouts. **Expect the bulk of the prior 63 `handled` to land
   `undispositioned` on the first sweep** — they predate the convention; that is the honest answer
   and is not a failure. A first sweep that classifies all 63 into `open`/`adjudicable` **is** the
   failure signature: something guessed.
4. **The bound is stated, so the skip is visible.** `contradiction_scan:` carries pages compared,
   documented count, undispositioned count, and the count this run **declined** to document; no bare
   zero appears on any contradiction slot. The 25-flagged/0-documented skip that produced the filing
   would now be legible in the report as a stated outcome (A3-20 shape 4 discharged by conformance to
   the general honest-reporting rule, not by a bespoke fix).
5. **Report and backlog stop disagreeing.** At least one documented contradiction for which the
   vault's backlog already carries an open item now reads `deferred` rather than health — the two
   surfaces agree where they previously contradicted each other (this is the Schottenheimer-class
   property; **non-blocking if that specific pair has since been resolved**, the property under test
   is report↔backlog agreement, not the pair).
6. **Handshake and durability in the field.** The installed
   `_meta/conventions/wiki-supersession.md` is at `version: 2` with its four consumers, all four
   installed skills pin `@2`, the sweep's `convention_drift:` is empty, and any vault-local
   `wiki-supersession.overlay.md` is untouched with no new `convention_base_divergence` finding
   (B1 durability posture).
7. **Second-vault check, non-blocking.** If `vlt-sayari` becomes readable, confirm the three slots
   and the denominator render there too. A vault with **no** contradictions must still emit
   `contradiction_scan:` with its denominator rather than a silent empty report — the honest-limit
   (one vault, one sweep) is context; the fix does not wait on a second vault.
