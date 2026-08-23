---
title: 'Inbox Evolution Roadmap — Arc 7: nowhere to put it'
status: 'CLOSED 2026-08-17. **This arc is archived — do not append.** v0.10.0 SHIPPED 2026-08-15 (builds B7-1..B7-8) @ b117d81, tagged v0.10.0 (be60f0b) and pushed. Acceptance discharged 2026-08-17 off the vlt-core 0.9.1→0.10.0 upgrade (2026-08-15 19:23) + the first post-upgrade full lint (2026-08-16) + the owner-run `vlt-dispatch ledger` (2026-08-17); gate passed on ship-verifiable checks only. Headline: B7-6 check (3) closed the A4-4 clause (5) Jackson-pair debt after FOUR arcs — the first inherited debt retired rather than re-carried. Still open elsewhere: five released standing watches (B7-2 (4) work-vault manifest containment, B7-4 (4) first local convention, B7-4 (5) first dispatch roster, B7-7 (5) the council-fielded leg, B7-8 (3) promotion instance), B7-4s ⚠ owner-review flag as inherited debt to Arc 8, the new filing 2026-08-17-140000-handoff-shape-has-no-form-for-an-inline-payload, three lint-surfaced module-feedback candidates, two drift residues, and the inherited C6-c + B5-3..B5-9 + pre-Arc-5 register + R3 (declared Arc 7, built Arc 8) — authoritative list in the Closeout record section. Superseded status line follows: acceptance discharge run 1 completed 2026-08-17 against the vlt-core 0.9.1→0.10.0 upgrade (2026-08-15 19:23) + the post-upgrade full lint (2026-08-16). B7-1, B7-3 and B7-6 fully DISCHARGED — B7-6 check (3) closed the four-arc A4-4 clause (5) debt (carrier 160949 archivable). B7-5 fully DISCHARGED later the same day on the owners `vlt-dispatch ledger` run — the arcs last open ship-verifiable check. B7-2/B7-4/B7-7/B7-8 are SPLIT: ship-verifiable halves discharged, field-contingent tails open (work-vault manifest containment, first local convention, first dispatch roster, the council-fielded gated mint, B7-8 (3)s promotion instance) — all released to the watch register. ACCEPTANCE COMPLETE for gating purposes; next move is `arc-closeout`, carrying B7-4s still-undischarged ⚠ owner-review flag'
module_code: 'vlt'
created: '2026-08-15'
updated: '2026-08-15'
derives_from:
  - 'inbox/2026-08-01-143000-lint-fixture-stale-against-three-builds.md'
  - 'inbox/2026-08-02-080528-merge-config-strips-vault-structure.md'
  - 'inbox/2026-08-03-100710-skill-manifest-scope-lost-references-and-scripts.md'
  - 'inbox/2026-08-08-123610-dispatch-hardcodes-single-user-addressee-model.md'
  - 'inbox/2026-08-14-142624-stock-deferral-dates-expire-with-no-vault-side-review-form.md'
  - 'inbox/2026-08-14-142625-spec-blind-spot-statement-stale-after-adoption.md'
  - 'inbox/2026-08-14-154422-lint-full-fan-out-is-blind-to-convention-overlays.md'
  - 'inbox/2026-08-14-154423-no-legal-home-for-a-vault-originated-new-convention.md'
  - 'inbox/2026-08-14-154424-wiki-sources-should-ship-as-wikilinks.md'
  - 'inbox/2026-08-14-154425-ingest-wiki-template-placeholder-teaches-a-form.md'
  - 'inbox/2026-08-14-180949-relay-requires-a-path-for-traffic-that-has-no-doc.md'
  - 'inbox/2026-08-14-181000-knowledge-gap-addressed-to-a-rail-with-no-recipient.md'
  - 'inbox/2026-08-14-182143-mint-mandates-a-council-it-has-no-fallback-for.md'
predecessor: 'skills/reports/archive/inbox-evolution-arc6-roadmap.md (Arc 6 — CLOSED, build B6-1 shipped v0.9.1 @ e930a40)'
intent: >
  Arc 6 closed on the first all-green ledger since Arc 2 and carried three un-captured filings
  forward. Ten more arrived in the twelve days after it shipped — from vlt-core, from a second
  consumer install, from a new team vault, and from the factory's own working tree. They read as
  one story: a vault does the legitimate thing the module told it to do, produces something real
  — a convention override, a new rule subject, a cross-user handoff, a deferral review, a
  pathless question, a hand-widened manifest, a path override, a substituted council verdict —
  and the module has nowhere to put it. Either the receiving mechanism was never built, or it
  was built to an enumeration that has since narrowed, or the prose that promises it went stale
  and now argues against looking. Arc 6 proved the factory can ship a clean release; Arc 7 is
  about what the field hands back.
---

> **This arc is archived — CLOSED 2026-08-17. Do not append.** Read it for history; the
> authoritative hand-off is the *Closeout record* section at the end. New signal goes to
> `inbox/` and is captured into the next open arc roadmap, never here.

## The through-line

Thirteen filings, four sources, one shape: **the module declares something and the mechanism that
would carry it isn't there.**

The declaration/mechanism gap comes in three flavours, and the arc is easiest to read as three
strands that share a root.

**Strand 1 — the vault's own output has no landing zone (A7-4, A7-5, A7-8, A7-11, A7-12, A7-13).**
Six filings each end at the same wall: a vault did exactly what the module asks, produced a real
artifact, and found no sanctioned home for it. A team vault needs a second addressee and dispatch
has none of the module's three extension seams (A7-4). A vault reaches a shipped deferral's
`review_after` and all three roads out are blocked by other rules (A7-5). A vault originates a
convention subject the module never shipped and every landing zone is a lint finding — except the
wrong one, which is silent (A7-8). A third of real relay traffic has no doc to point at, so it is
unkeyed and the anti-spam guard it should have hit is silently inert (A7-11). A backlog item is
addressed to a partner through a rail with no recipient and no drain (A7-12). A gated mint cannot
field its council and the module names neither the stall nor the substitute (A7-13). In every one
the vault improvised something reasonable; in none did the module ask it to record that it had.

**Strand 2 — the durability nets have scope holes, and each one reports success (A7-2, A7-3, A7-1).**
`merge-config.py` destroys any module variable absent from the answers payload and prints
`"status": "success"` (A7-2). The skill-asset manifest's scope is an enumeration, so eight governing
files walked out from under the divergence net when a refactor moved them, and a hand-widened
manifest is narrowed back on every re-run (A7-3). The factory's own lint harness cannot prove three
of its five groups can pass, because its fixture is stale against three builds (A7-1). This is the
module's own standing rule — *lists that claim completeness drift* — firing three times inside the
machinery built to catch drift. A7-3 and A7-2 are the same failure at two altitudes: a durability-path
step that destroys or de-protects vault-local state and reports success. A7-1 is why neither was
caught: nothing in the release gate exercises the classes they belong to.

**Strand 3 — shipped prose asserting things that stopped being true (A7-6, A7-9, A7-10, A7-12).**
`spec.md` tells its reader a metric structurally cannot fire; adoption is no longer zero, so the
disclaimer now argues against checking (A7-6). Frontmatter rule 4 sweeps wiki `sources:` in with
audit trails, making the source layer untraversable in the tool the vault actually runs (A7-9), and
`vlt-ingest`'s template hides the form the convention constrains (A7-10). `frontmatter.md`'s
`knowledge-gap` line addresses work to the Researcher, a sentence that predates dispatch existing
(A7-12). Each is small; the class is not — the enforcement kit's credibility rests on its
disclaimers being as current as its counters, and four shipped statements are older than the
mechanisms around them.

**The root the three share.** Arc 5 built the promises and Arc 6 made the factory honest about its
own releases. What neither did was give the *vault* a way to answer back. Every seam the module has
for vault-originated content — the overlay, the `adoption_first_instance` stamp, the local mint, the
capability — was designed for the additive case against an existing module-owned subject. Six of
these filings are the non-additive case arriving for the first time, and three are what happens when
the module's own self-description is the thing that drifted. The arc's question is whether the answer
is a family of narrow fixes or one designed **receiving surface**; that is ideation's call, and the
filings deliberately do not presume it.

**Cross-filing dependencies the owner should know before grouping:**

- **A7-9 → A7-10** — A7-10 is explicitly contingent: *"this rides whatever build takes 2026-08-14-154424.
  If that candidate is declined, this one is moot and should be archived with it."* They must be
  ruled together.
- **A7-9 → A7-7** — the wikilink `sources:` form is exactly the overlay rule that today produces
  false positives in the overlay-blind fan-out. A7-7's suggested acceptance case *is* A7-9's local
  override. Fixing A7-9 upstream without A7-7 removes the demonstration but not the class.
- **A7-11 ↔ A7-12** — same mint, applied together, and A7-12's fix routes work onto the rail A7-11
  repairs. Neither makes sense shipped alone.
- **A7-2 ↔ A7-3** — both argue for widening what `vlt-upgrade`'s pre-flight snapshots (config,
  and the shipped surface by structure rather than enumeration). Whether that is one build is an
  ideation ruling.
- **A7-1 gates the rest** — every build in this arc that adds or changes a lint check inherits a
  harness that cannot prove a clean baseline. Sequencing A7-1 early buys the arc a working gate;
  sequencing it late means each build re-negotiates the same 9/11.
- **A7-13 ↔ `2026-07-16-153000-new-partner-fields-one-lens`** (captured in Arc 3, still active) —
  panel *availability* vs panel *composition*. A fix for either leaves the other standing; the
  filing flags them as same-direction, not duplicates.
- **A7-5, A7-8, A7-12 all touch `frontmatter.md`** — currently at `version: 5` with six consumers.
  A7-12's local fix was already a 5→6 base edit with a full consumer walk. If two of these ship in
  one arc, the version handshake wants planning, not three sequential bumps.

## Capture — 13 filings (grounded against module source at `e930a40` / working tree, 2026-08-15)

Grading vocabulary per `references/grounding-methodology.md`. Every `file:line` below was re-derived
from current source, not taken from the filing.

---

### A7-1. The package-lint fixture is stale against three builds (2026-08-01) — `2026-08-01-143000-lint-fixture-stale-against-three-builds.md`

**CONFIRMED, at current HEAD.** Ran `uv run tools/test-package-lint.py` in the working tree:
**9/11 green**, cases **1** and **7** red, and the failure set is exactly the three the filing names:

```
FAIL group C — rule-card missing: skills/vlt-setup/assets/governance/_meta/vault-rule-card.md
FAIL group C — enforcement kit: vitals reader missing: skills/vlt-setup/assets/hooks/vlt-vitals.py
FAIL group E — structure map: cannot read module.yaml vault_structure.default: 'vault_structure'
```

The filing measured 6/8 at `f3b343d`; B6-1's three Group-D cases took it to 9/11 without touching the
inherited failures. Both readings are correct for their moment — the denominator moved, the red cases
did not.

**GAP CONFIRMED, and it is wider than a stale fixture.** The filing's deeper claim grounds out:
groups C6, C7 and C8 have **no positive case and no negative case** in the harness. C7 (router
integrity) passes vacuously — the fixture builds no `references/` directories, so there is nothing to
orphan. Three release-gate assertions are exercised only against the real repo tree, which is the tree
they were authored from.

**Note the coupling nobody has stated yet:** the fixture's missing `vault_structure.default` (group E)
is the *same key* whose destruction A7-2 files, and the fixture's absent `references/` (group C7) is
the *same directory class* whose loss A7-3 files. Three filings, three different mechanisms, one
under-modelled fixture.

**Residual scope.** The filing's own candidate shape is intact and unshrunk: seed the four gaps
(rule-card + `derived_from:` sha256, minimal `vlt-vitals.py` with a parseable `METRICS` table,
tripwires seed whose metric ids resolve, `vault_structure.default` agreeing with the fixture
contract), then restore case 1's exit-0 assertion as the load-bearing baseline. The filing's framing
of *why* — "a rule that can only be observed passing on the artifact it was authored from is not yet
tested" — is the ruling worth enshrining, ahead of the four specific seeds.

**Provenance, verified.** The filing's attribution table is right on all three rows: `package-lint.py`
group C6 (rule-card freshness) is B5-7's, C8 (enforcement kit) is B5-9's, E2 (structure-map SSoT) is
the B5-8/B5-9 era. None widened the fixture.

---

### A7-2. `merge-config.py` destroys the `vault_structure` block and reports success (2026-08-02) — `2026-08-02-080528-merge-config-strips-vault-structure.md`

**CONFIRMED — and reproduced at rest.** The filing marked its mechanism as a guess and asked capture
to re-ground it. It was right to; the guess is wrong in a way that **widens the defect**.

The filing guessed *"a fixed set of scalar keys from `module.yaml`"* or *"a missing branch for a
variable whose shape is `{prompt:, default: <map>, example:}`"*. Neither holds:

- `merge_config()` at `skills/vlt-setup/scripts/merge-config.py:271-278` — **anti-zombie: it deletes
  the entire existing `vlt:` section outright**, with no read of what it is about to destroy.
- `:281-285` — it then rebuilds that section as `extract_module_metadata()` (`:182-191`, exactly
  `name`/`description`/`version`/`default_selected` — the four keys the field run saw in `module_keys`)
  **plus `answers.get("module", {})` and nothing else**. There is no fallback to the prior config and
  no fallback to `module.yaml`'s own `default:` map.
- `apply_result_templates()` (`:194-221`) handles map-valued answers correctly — it passes any value
  without a `result:` template straight through. The map shape was never the problem.

So the real rule is: **any module variable absent from `answers["module"]` is destroyed silently.**
`vault_structure` is merely the one with 18 keys and a vault-local override in it.

**Reproduced** against a scratch fixture (a config carrying `vault_structure` with a local
`dog_training_root:`):

| answers payload | result |
|---|---|
| `{"module": {"other_var": "z"}}` — `vault_structure` absent | block **destroyed**; `"status": "success"`; `module_keys` = the 4 metadata keys + `other_var` |
| `{"module": {"vault_structure": {...}}}` — correct nesting | block preserved **including** `dog_training_root:` |

**PROVENANCE CORRECTION — the module-side prose is right and the field run's payload was not.**
`skills/vlt-setup/SKILL.md:75` already states the contract: *"The `module` object **always carries
`vault_structure`** — the full default map read from `./assets/module.yaml` (`vault_structure.default`)
with any user overrides merged on top."* The field run's answers JSON put `vault_structure` at the
payload's **top level**, outside `"module"`, so the script never saw it. That is a caller error against
a documented rule — which relocates the defect rather than dissolving it:

1. **The script is destructive by construction** for any unanswered variable, with no preservation
   and no fallback. A prose instruction is the only thing standing between a correct run and data
   loss on the durability path.
2. **`"status": "success"` cannot distinguish merged from dropped.** `module_keys` (`:399`) is a bare
   key list of what was *written*; nothing reports what was *removed*. The filing's second ask — a
   loud line in the JSON result — is the minimum honest fix and is independent of the first.
3. **The prose lives in the consumer, not the script.** `merge-config.py --help` does not carry the
   `"module"`-nesting requirement; the only statement of it is in `vlt-setup/SKILL.md:75`, which
   `vlt-upgrade`'s Step-3.6 hand-off reaches by reference.

**Confirmed unchanged:** the impact reasoning. `vault_structure` has no baseline, no manifest entry
and no divergence check — `vlt-upgrade`'s Step-1 pre-flight (`vlt-upgrade/SKILL.md:33-40`) covers
conventions, skill assets, governance, mints and capabilities, and not `config.yaml`. The 17 keys
where default == override keep working; only a key with no shipped default eventually surfaces as a
broken path.

**Lead not closed:** the filing flags the 0.8.0 → 0.9.0 ledger entry ("map reconstructed, local
`dog_training_root:` kept") as possible evidence of a prior strip. Not verifiable from module source —
it is vault-side evidence. Left open, marked as a lead, not a finding.

---

### A7-3. The skill-asset manifest scope is an enumeration, so `references/` and `scripts/` are outside the divergence net (2026-08-03) — `2026-08-03-100710-skill-manifest-scope-lost-references-and-scripts.md`

**CONFIRMED on every claim, including its own self-correction.**

- **The spec**: `skills/vlt-setup/SKILL.md:150` defines the manifest by enumeration —
  *"`SKILL.md` + everything under each skill's `assets/`, plus the installed `.claude/workflows/*.js`"*
  — and on the same line declares it *"module-owned: overwrite it to the current shipped versions on
  every install/update."* Both halves verbatim.
- **The consumer**: `skills/vlt-upgrade/SKILL.md:37` computes `skill_asset_divergence` *"for each file
  the manifest records"*. Scope loss is therefore silent by construction — no SHA, no diff, no report
  line — and the same line names the promise it breaks: *"the net that turns a local skill-asset edit
  into a surfaced divergence instead of a silent clobber."*
- **The directories**: `find skills -type d` returns exactly `skills/vlt-dispatch/references`,
  `skills/vlt-lint/references`, `skills/vlt-setup/scripts` (3 `.py`), plus the two `assets/` dirs
  (`vlt-mint`, `vlt-setup`). The eight `references/*.md` and three `scripts/*.py` are the whole
  uncovered set. `vlt-lint/references/checks.md` alone is ~25K of governing lint prose.
- **The provenance split, which the filing corrected against its own backlog entry and is right**:
  `references/` first appears in `43795fa` (Arc 5 back half), released as **v0.9.0** (`f3b343d`) —
  so the regression landed at 0.9.0, not 0.9.1; the work vault merely observed it upgrading
  0.8.0 → 0.9.1 in one hop. `skills/vlt-setup/scripts/*.py` first appears in `8c0955f` (v0.3.0),
  predating the build-18 manifest spec entirely — so `scripts/` is an **original gap**, never a
  regression. Same one-line fix, different blame, and the filing is right that capture should keep
  them distinguishable.

**GAP CONFIRMED with a second-order finding the filing states and is worth enshrining:** the
hand-widened manifest (40 → 55 entries, ruled in the work vault's decision log) **does not survive** —
the module-owned overwrite posture narrows it back to 40 on any `vlt-setup` re-run. So the current
resting state is a documented vault ruling that the module silently reverts, which is worse than
either extreme. This is the module's own *lists that claim completeness drift* rule firing inside the
durability machinery.

**Open design question, carried verbatim (do not resolve here):**

> On capture, decide explicitly whether `scripts/` inclusion is in the same build or split — it is the
> same one-line spec change, but it is a *new* protection, not a restored one.

Also carried, unresolved: whether the manifest should be **computed by a script** (`verify-skill-manifest.py`,
already flagged in the 2026-07-12 handoff as "prose where a script should be") rather than by prose
instruction, and whether a **manifest-entry-count-didn't-shrink** check belongs in the upgrade report.

---

### A7-4. `vlt-dispatch` hardcodes a single-user addressee model (2026-08-08) — `2026-08-08-123610-dispatch-hardcodes-single-user-addressee-model.md`

**CONFIRMED, every structural claim, and the classification (design gap, not defect) is right — the
module behaves exactly as designed.**

- **The hardcoded topology**: `skills/vlt-dispatch/SKILL.md:30-44`. The `vault_structure` logical
  names it resolves are `log`, `backlog`, `conventions`, `archive` — four. Then four more locations
  fixed in prose, three of them explicitly *"not in the structure map"*: `daily/` (human capture zone),
  `_agent/dispatch.md` (the routing record), `_agent/handoffs/`, and `{specs}`. No roster, no
  per-user inboxes.
- **Zero extension seams**: `grep -rn overlay skills/vlt-dispatch/` returns **nothing** — no
  convention-overlay read anywhere in the skill or its four `references/` files, while `vlt-ingest`
  (`SKILL.md:26`), `vlt-lint` (`SKILL.md:17`) and `vlt-track` all state the base+overlay merge read.
  No agent-zone behavior-file read, no `customize.toml`.
- **The stated boundary**: `skills/vlt-upgrade/SKILL.md:48`, verbatim — *"skills have no overlay
  mechanism, so a local skill edit is the user's to re-apply."* The re-apply treadmill is real.
- **The precedent the filing points at is exact**: `skills/vlt-track/SKILL.md:16` — the loop profile
  is read from the invoking partner's `capabilities/track.md` and the skill *"hardcodes none of it"*;
  `:31-40` enumerates what gets bound (`{root}`, `{target}`, subject model, data streams, log tag,
  non-negotiable gate) and `:41` names the headless fallback. That is a working, shipped instance of
  the designed-parameter-read pattern this filing asks for.

**Residual scope note.** The filing's diagnosis — dispatch welds *vault-population policy* into
module-owned *mechanism*, and the four modes / two-writer discipline / relay idempotency are correctly
frozen while the addressee model is not — survives grounding intact. Nothing here shrank.

**One thing capture can add.** A7-11 and A7-12 are also dispatch-shaped and also about what the record
can carry (a shape facet, an address rule). If a routing profile is built, three filings want to know
its scope, and A7-11's `ref` key and A7-12's address rule are the kind of thing that either lands in
the profile or deliberately does not. Group with care.

**Open ideation questions, carried verbatim:**

> (a) profile home: `{overlays}/`-adjacent vs agent zone; (b) one vault-wide profile vs per-partner
> `capabilities/dispatch.md` files; (c) v1 parameter scope (roster + inbox destinations + relay
> addressing — more?); (d) which vocabulary, if any, belongs in a convention instead; (e) state the
> generalized designed-read pattern in the contract now, or wait for a second instance.

The filing also pre-rejects one shape and asks that the rejection stand: **not** a generic
skill-overlay/extension mechanism — the `vlt-upgrade:48` veto should hold. Its full decision matrix
lives in a vault-side session artifact (`_output/problem-solution-2026-08-08.md`) that is **not
readable from the factory**; the filing's summary is the only account capture has.

---

### A7-5. Stock deferral dates expire with no vault-side review form (2026-08-14) — `2026-08-14-142624-stock-deferral-dates-expire-with-no-vault-side-review-form.md`

**CONFIRMED at module source — these are the factory's dates, shipped to every install.**
All three shipped conventions carry `review_after: 2026-08-17`:

| convention | line | stage | version |
|---|---|---|---|
| `governance/_meta/conventions/frontmatter.md` | `:18` | `checked` | 5 |
| `governance/_meta/conventions/spec.md` | `:16` | `declared` | 2 |
| `governance/_meta/conventions/wiki-consolidation.md` | `:16` | `declared` | 1 |

The filing's stage/metric table matches the source exactly. **Two days from today** every vault
running 0.9.1 begins reporting `deferral_expired` on the same three conventions.

**All three roads confirmed blocked:**

1. **Edit the base** → `vlt-lint/references/checks.md:41` flags `convention_base_divergence` for any
   base differing from its `.baseline/`, excluding **only** the `adoption_first_instance:` line. A
   `review_after` edit flags, every run.
2. **Overlay** → `checks.md:42` (`overlay_not_append_only`) plus the operating contract's append-only
   rule. `review_after` is an existing base field; there is no overlay form for changing one.
3. **Promote the stage** → `frontmatter.md:238` is explicit: *"Stage promotions (`declared → checked →
   enforced`) happen through the mint ceremony … never through lint,"* and `spec.md:90` names the two
   unbuilt lint checks (`spec_schema_violation`, `spec_notification_missing`) the promotion waits on.
   A vault cannot build module machinery.

**GAP CONFIRMED, and it is the reachability shape the filing names.** This is the same class as
`2026-07-29-120001-adoption-stamp-unreachable-beyond-mint` (captured Arc 5, still active): an axis
declared with a reporter whose *writer* sits somewhere the instance cannot reach. Here the unreachable
act is the **review** itself.

**One grounding addition the filing did not make.** `spec.md` and `wiki-consolidation.md` both ship
`adoption_first_instance: null` (`:17` in each) — so the stamp vlt-core carries on `spec.md` is
precisely the *authorized vault-local carry-forward* the divergence diff excludes. The module already
has exactly one field of the shape the filing's narrowest candidate asks for. That precedent is the
strongest argument in the filing and it is only implicit there.

**PROVENANCE — the filing's guess, unresolved from module source.** It suspects the three dates were
set as one uniform ~3-week horizon at the 0.9.0/0.9.1 builds rather than derived per-convention.
Capture did not chase this through the build briefs; it is answerable from `skills/reports/archive/`
if ideation wants it, and the answer changes only *which* candidate is right, not whether the gap
exists.

**Field data offered, not a recommendation** (the filing is explicit the dates are the module's to
set), carried forward for whoever does the review:

- **`wiki-consolidation@1`** — expiring on a clean record; the metric has read 0 on every sweep;
  nothing has ripened.
- **`spec@2`** — metric now attainable, reads 0 honestly. See A7-6.
- **`frontmatter@5`** — **half the metric is unevaluable from inside a vault.** The threshold
  (`:17`) is *"2 drift findings, or the 3rd new convention"*; the baseline count the second half
  counts from is recorded nowhere a vault can read. The filing flags this as a general property of
  **count-since-N metrics in shipped frontmatter**, not a one-off — worth an ideation ruling of its
  own.

**Candidate shapes, carried unranked as the filing offered them:** overlay-writable `review_after` as
an authorized vault-local carry (the `adoption_first_instance` precedent); per-convention dates derived
from each metric rather than one shared horizon; a distinct finding class for *expired, module-owned*;
or simply saying the quiet part in the declaration — that a shipped deferral's expiry is reviewed
upstream and a vault's only move is to file.

---

### A7-6. `spec.md`'s blind-spot statement is stale after adoption (2026-08-14) — `2026-08-14-142625-spec-blind-spot-statement-stale-after-adoption.md`

**CONFIRMED at module source, and there are TWO stale sites, not one.** The filing names the
*Enforcement* paragraph; grounding found the same assertion duplicated in the frontmatter comment:

- `governance/_meta/conventions/spec.md:92` — *"at zero adoption the `deferral_metric` cannot fire …
  its only attainable value is 'fine' … it measures notification discipline once specs exist, never
  adoption itself."*
- `governance/_meta/conventions/spec.md:14` — the inline comment on `deferral_metric:` itself:
  *"# at zero adoption this cannot fire — see Enforcement, the blind-spot statement."*

Any fix must touch both or the correction half-lands. The second site is the more dangerous one: it
sits four lines above the reader's eye in the frontmatter block.

**PROVENANCE CORRECTION worth stating precisely.** The shipped `spec.md` still carries
`adoption_first_instance: null` (`:17`) — which means **the statement is still true of the shipped
artifact and false in the field.** The filing's evidence (two live specs, one version bump, notified
via `_agent/dispatch.md:88,132`, metric = 0 for the right reason) is vlt-core state and cannot be
verified from module source; capture takes it as reported and notes it is vault-side. That does not
weaken the finding — it sharpens it. The defect is **prose asserting a permanent property that a
frontmatter field is designed to invalidate**, so the statement goes stale in every vault at a
different moment, and the shipped default is exactly where it looks most correct.

**The fix the filing proposes is the right shape** and costs nothing: the conditional form —
*while adoption is zero this cannot fire; once a spec exists it measures notification discipline,
never adoption itself* — is true in both regimes and never goes stale.

**One forward-looking finding worth pulling out of the filing's body**, because it is about a check
that does not exist yet and will be cheaper to get right than to fix: vlt-core's one notified bump
relayed against the **handoff path**, not the `_agent/specs/` path, because at bump time only the
handoff existed. A mechanical `spec_notification_missing` keyed on the spec path would score that
bump as un-notified — **a false positive on the exact history the check is being built to measure.**
Whoever builds that deferred check needs this.

**Carried, unaudited** (the filing marks it a guess and says so): if the class is *prose asserting a
permanent property a frontmatter field can invalidate*, `spec.md` may not be the only instance. No
audit was performed here either — an audit sweep is a plausible small build, not a capture act.

---

### A7-7. `vlt-lint-full.js` is blind to convention overlays (2026-08-14) — `2026-08-14-154422-lint-full-fan-out-is-blind-to-convention-overlays.md`

**CONFIRMED against module source** (the filing grepped the *installed* copy; re-derived here against
the shipped SSoT, `skills/vlt-setup/assets/workflows/vlt-lint-full.js` — same result, and the line
numbers hold):

- `grep -c overlay` → **0**. Not one occurrence in 30K of workflow.
- `:22` — `conventionsPath: string // LIVE abs path to {conventions}`; `:62` — `const conventionsPath = a.conventionsPath`.
- `:77-78` — the required-args guard names `pages`, `indexPath`, `conventionsPath` only. No overlays
  path is accepted, so none can reach the per-page scanner prompt (`:142`) or the index linter.
- `:95` — the scanner schema returns `frontmatter_valid: { type: 'boolean' }`, so an overlay-compliant
  page lands as a real finding, not a soft note. The filing's second failure mode is the one that bites.

**The invariant it breaks, verbatim from source:** `vault-operating-contract.md:100` — *"Any reader of
a convention reads the base, then applies its overlay if one exists. The convention is the base file
plus its overlay, merged on read."* And `vlt-lint/SKILL.md:17` implements it faithfully for the
skill's own path — *"read each together with its `{overlays}/{name}.overlay.md` if present, honoring
the overlay's appended rules"* — which is precisely what makes the fan-out's silence a break rather
than an omission: **the same skill honors the rule in one mode and cannot in the other.**

**GAP CONFIRMED and WIDER than filed.** The other two shipped workflows are equally overlay-blind:
`grep -c overlay` returns **0** for `vlt-consult.js` and **0** for `vlt-review-council.js`. Whether
either has cause to read a convention is a build question, but the filing's class — *workflow assets
never received the overlay-merge contract* — is a three-file class, not a one-file defect.

**The governance point stands and is the sharper half.** `vlt-lint/SKILL.md:4` carries
`depends_on: ["frontmatter@5", …]`, and `frontmatter.md`'s base-edit ceremony holds that *"a consumer's
ack covers its own workflow assets (e.g. `vlt-lint-full.js`)."* The ack therefore asserts a
reconciliation that never happened. **An ack that covers assets by declaration rather than by
inspection drifts silently** — nothing re-reads the asset when the version is bumped. That is a
version-handshake finding, and this arc has three filings that would bump `frontmatter`.

**Acceptance shape, carried as filed** (it is better than "does it accept the argument"):

> A page compliant with an overlay rule that contradicts its base survives a full sweep with no
> finding.

Note this acceptance case is **A7-9's local override** — the two filings are the same demonstration
seen from opposite ends.

---

### A7-8. No legal home for a vault-originated new convention (2026-08-14) — `2026-08-14-154423-no-legal-home-for-a-vault-originated-new-convention.md`

**CONFIRMED — all three landing zones behave as the filing's table says.**

| landing zone | grounded outcome |
|---|---|
| fresh file in `{conventions}` | `baseline_missing` — `vlt-lint/references/checks.md:41`, flagged once per base file with no `.baseline/` counterpart |
| overlay with no base | `overlay_orphan` — `checks.md:42`, *"any overlay whose `{name}` has no corresponding base convention"* |
| appended to an unrelated base's overlay | **no finding** — confirmed by reading the check, not by absence of evidence |

**The third row is the finding.** `checks.md:42` fires `overlay_not_append_only` only on *"a section
heading that duplicates a base heading **verbatim**."* A novel heading — which is exactly the shape of
a new-subject rule — passes cleanly. The guard reads stronger than it is, so the one non-compliant
option is also the only silent one, which is why it gets chosen.

**The sharpest consequence CONFIRMED, and it is structural.** `frontmatter.md:245` is the
*Narrow-convention escape hatch* — a recorded scope decision whose tripwire is `frontmatter.md`'s own
`deferral_metric` at `:16`: *"prose/behavior drift lint findings + new conventions minted."* An
overlay-resident prose rule is invisible to **both** halves: nothing was minted into `{conventions}`,
and no prose-drift check exists. The one mechanism installed to detect a convention accumulating
foreign subjects cannot see an instance sitting inside the file it guards.

**And the file it landed in declares itself against exactly this.** `frontmatter.md:25`: *"This file
is the **single source of truth** for the frontmatter schemas across every note type the vault uses."*
A body-prose rule (*a paragraph is one unbroken line; a newline is a semantic break*) is not a
frontmatter schema. The vault recorded the placement as knowingly provisional rather than pretending
it fit — which is the honest move and also the evidence.

**Note the compounding with A7-5.** `frontmatter@5`'s deferral expires 2026-08-17 on a metric that is
*already* provably blind to the pressure it was installed to measure. The `review_after` review A7-5
says a vault cannot perform would, if performed, be reviewing a metric A7-8 shows is structurally
under-counting. They are the same convention's frontmatter, two lines apart.

**Suggested shape, carried unresolved:** a sanctioned **baseline-exempt local convention** — a
vault-originated file in a known location carrying its own enforcement declaration, explicitly exempt
from `baseline_missing`, read by consumers the way overlays are. The filing names the two properties
any answer must have — *(a)* exist without a stock counterpart and *(b)* be visible to the split
tripwire as a convention in its own right — and its acceptance bar insists on both halves:
*"a landing zone that is merely silent would reproduce today's outcome with better manners."*

---

### A7-9. Wiki `sources:` should ship as wikilinks (2026-08-14) — `2026-08-14-154424-wiki-sources-should-ship-as-wikilinks.md`

**CONFIRMED as a faithful reading of the shipped rule.** `frontmatter.md:36`, YAML rule 4, verbatim:

> **Non-graph list fields use bare paths/basenames, not wikilinks.** … (`sources:` likewise holds
> plain page references unless a specific schema says otherwise.)

Classification **candidate** is right — this is a proposed change to a shipped default, not a defect.
The argument grounds: a wiki page's `sources:` is a link graph (claims answerable to origins,
traversal is the point), an audit trail is not, and rule 4 currently sweeps both together. The
distinction the filing proposes rule 4 should draw — **traverse vs verify** — is the ruling to
enshrine if this is taken.

**The carve-out reading is legitimate and worth enshrining separately.** Rule 4's own tail — *"unless
a specific schema says otherwise"* — is a delegation slot the base cut in its own text. The vault's
unanimous test for occupying one is currently **derived, not stated**, and the filing asks for it in
the contract's overlay section:

> An overlay may occupy a base carve-out where **(a)** the base names the carve-out in its own words
> and **(b)** the overlay names the exact schema and scopes narrowly.

That is a durability-model rule of general use, independent of whether the `sources:` change ships.

**The three form details are all grounded in existing base rules**, not new inventions: double-quoting
is base rule 1 (`frontmatter.md:31`, *"YAML treats a leading `[` as a flow sequence"*); dropping `.md`
matches rule 1's own example (`superseded_by: "[[page-slug]]"`); full-path-not-basename is a collision
argument. The wikilink-reserved-character note (`[`, `]`, `#`, `^`, `|` are reserved; **`?` is not**)
is field-earned — a first draft silently dropped a trailing `?` and produced a dead link — and the
filing is right that a shipped rule should say it positively.

**The design constraint CONFIRMED, and it is the part that makes this more than a style change.**
`vlt-lint/references/checks.md:59` is the `linkage_ripe` shared-source leg — *"the note and a wiki
page share an entry in `sources:`"*. Research notes carry `sources:` too. Convert only the wiki-page
schema and, under naive string equality, a wikilinked entry never matches a bare-path one: the leg
**silently stops firing**, and the failure direction is a false positive — a research note reported
graduation-ripe that a wiki page has already absorbed. `checks.md:57` names this exact class one leg
above: *"a blind spot in an absorption test is a false positive."*

Two closes carried as the filing framed them, unranked: **(1)** a normalization clause (strip brackets
and `.md` before any `sources:` comparison — what vlt-core shipped, survives the two forms coexisting
forever), or **(2)** convert both schemas together (cleaner, larger, and still wants the clause as a
defence against the next divergence).

**Acceptance, carried as filed:** *`linkage_ripe` still excludes an absorbed research note when the
wiki page citing it is on the wikilink form and the note is on bare paths.*

---

### A7-10. `vlt-ingest`'s wiki template placeholder teaches a form (2026-08-14) — `2026-08-14-154425-ingest-wiki-template-placeholder-teaches-a-form.md`

**CONFIRMED, at both cited sites, and the filing's own self-correction is the honest reading.**

- `skills/vlt-ingest/SKILL.md:147` — the wiki-page frontmatter template emits
  `sources:\n  - <every source that has contributed>`. Form-neutral placeholder, verified.
- `skills/vlt-ingest/SKILL.md:26` — the binding is explicit and strong: *"Read the conventions you
  will obey before writing anything … read each together with its `{overlays}/{name}.overlay.md` if
  present … These govern every write; honor them exactly."*

So there is **no defect in the binding**, and the filing says so. An earlier reading in the same
session called this a treadmill (the op emitting a violation on every run, so the rule could never
converge); the filing checked it, found it overstated, and recorded the correction rather than
shipping the stronger claim. Capture endorses that grading — the residual risk is real but narrow:
**an agent copying the placeholder's shape rather than resolving it**, because a template inline in
the skill is the most concrete thing in context at write time.

**Dependency, carried verbatim and binding on ideation:**

> Nothing on its own — this rides whatever build takes `2026-08-14-154424`. If that candidate is
> declined, this one is moot and should be archived with it.

**The generalizable rule underneath**, which survives even if A7-9 is declined: *where a template's
field has a form the convention constrains, the template should show the form.* A placeholder that
hides it converts a convention rule into a per-run judgment call.

---

### A7-11. Relay requires a path for traffic that has no doc, and a pathless pointer is unkeyed (2026-08-14) — `2026-08-14-180949-relay-requires-a-path-for-traffic-that-has-no-doc.md`

**CONFIRMED at module source on both halves.**

- **The requirement**: `skills/vlt-dispatch/references/relay.md` *Inputs and validation* —
  *"Required: **`to-slug`** …, **`gist`** …, **`handoff-path`** (the stable path under
  `_agent/handoffs/` or `_agent/specs/`)."* Unconditional.
- **The compounding defect**: the same file's *"The idempotency rule — keyed on `(handoff-doc-path,
  recipient-slug)`"* — *"Before appending, grep the record for an existing relay pointer with this
  same `(handoff-path, to-slug)` pair."* A pathless pointer has nothing to grep on, so **failure mode
  #1 (spam — a partner re-firing the same notice each awakening), which relay's own text names, is
  unguarded for that traffic.** The guard's absence is indistinguishable from the guard passing. This
  is the more serious half and the grounding confirms it exactly as filed.

The traffic counts (40 relay pointers, 27 with a path, 13 without; ~8 `ask` + ~5 `answer`) are
vlt-core state and are taken as reported — not verifiable from module source, and not load-bearing on
the mechanism finding, which stands on the spec alone.

**The filing asked capture to check one thing specifically. Here is the answer.** It suspected the
`consult` mode may have masked the gap — *"consult is the synchronous question channel, so an
asynchronous question had no named home and landed on relay"* — and said that if right, the cleaner
fix might be a consult-adjacent async mode rather than a relay shape facet. **Grounded: the suspicion
is correct about the framing, and it argues for the relay facet, not a new mode.**

- `references/consult.md:7` — *"A consult is a `relay` whose drain happens immediately, in-process,
  with the answer returned to the caller instead of left on the board. Synchronous, **depth-1 hard**
  … **Consult answers; relay assigns.**"* So the module already models consult as *relay with an
  immediate drain* — an async question is structurally a relay, by the module's own definition.
- `skills/vlt-dispatch/SKILL.md:18` — *"All four modes are **the same machine**: every mode emits the
  identical pointer line into the identical record, drained by the identical grep-and-check loop."*
  A fifth mode would buy no new machinery; it would only re-cut the same record.
- `SKILL.md:22` names the key discipline directly: *"a **mode-appropriate** idempotency key makes
  re-runs safe (a per-source **watermark** for `daily`, the **handoff-doc path** for `relay`)."*
  The module already holds that the key is a per-mode design choice — which is exactly the seam the
  filing's `ref` proposal fits into.

**A relay-shape facet is therefore the shape most consistent with shipped design.** That is a
grounding finding, not a ruling — ideation still owns the call.

**Second site any fix must touch:** `SKILL.md:22`'s parenthetical names the relay key as
*"the handoff-doc path"*. Change the key in `references/relay.md` alone and the router's own overview
carries the old one. Single-home discipline says one of them points at the other.

**The local fix, carried as proposed (not adopted here):** relay declares a **`shape`** —
`handoff` (path required, contract unchanged) / `ask` (no path, `ref` required) / `answer` (path
optional, `ref` required and must be the originating ask's). `ref` is a short kebab slug that points
at nothing and **exists to key the pointer**; the idempotency key becomes `(handoff-path | ref, to-slug)`.
Two properties the filing asks be kept if taken: an `answer` reusing its `ask`'s `ref` **does not
collide** with it because the key includes the recipient (opposite directions, different `to-slug`),
and the change is **backward-compatible with no backfill** — an un-annotated header reads as
`handoff`. Also widened locally: *one relay = one pointer* admits a **batched `ask`** (one publisher,
several questions, one recipient, one moment).

**Receiver-side check the filing offers instead of trusting the write side:** *every relay pointer
resolves a key* — a path that exists on disk, or a `ref` present in the header. That catches the
unkeyed pointer, which is the failure that cannot be seen by reading.

---

### A7-12. `knowledge-gap` is addressed to a rail with no recipient (2026-08-14) — `2026-08-14-181000-knowledge-gap-addressed-to-a-rail-with-no-recipient.md`

**CONFIRMED at module source, with one scope correction.**

- **The address in the prose**: `governance/_meta/conventions/frontmatter.md:218` — *"`knowledge-gap`
  — a topic the vault is thin on; a cue for the Researcher."* A sentence that names a recipient.
- **The rail has none**: the backlog item schema at `:215-218` carries `kind` and `by:`; `by:` records
  who *filed*. No recipient field, no drain, no pickup loop — confirmed by reading the schema, not
  inferred.
- **The read is specified but unbounded**: `vault-operating-contract.md:169` (Beat 2 — Orient) is the
  filing's strongest evidence and it holds exactly. Every other read in that beat carries an explicit
  bound with a measured justification — `{index}` **section headings**, the **last 5** `{log}` entries,
  `## Thread` **only** — and the sentence even states the reason: *"The bounds are what keep a mature
  vault's orient from scaling with its age."* **`{backlog}` is the one item in the list with no
  bound** (*"the open items"*), and it is the one that grows monotonically. That is a clean, filed,
  independent finding — it survives even if the address rule is declined.
- **The Researcher names the kind**: `skills/vlt-agent-researcher/SKILL.md:25` — *"especially
  `knowledge-gap` items"*. The address is honored on the read side and unreachable on the write side.

**PROVENANCE CORRECTION — the consumer walk is a module-source list of 5, not 8.** The filing reports
*"All 8 partner SKILL.md files shared one boilerplate sentence."* Eight is the **vlt-core roster**
(3 shipped + 5 locally minted). The module ships **three** partner skills, and the boilerplate is at:

- `skills/vlt-agent-creative/SKILL.md:48` — *"**file it to `{backlog}` and say so in-flow**"* (`capability-gap`)
- `skills/vlt-agent-librarian/SKILL.md:47` — same reflex (`maintenance`)
- `skills/vlt-agent-researcher/SKILL.md:50` — same reflex (`knowledge-gap` / `capability-gap`)
- `skills/vlt-mint/assets/partner-agent-template.md:63` — the leak into every future minted partner,
  **confirmed**; and `:40` propagates the unbounded `{backlog}` orient read as well

The filing's own conclusion is strengthened by the correction, not weakened: *"a single-point edit
reached all of them, which suggests the module should own that sentence in one place rather than
copying it per partner"* — the module-side surface is 3 skills + 1 template, and single-home
discipline says the reflex belongs in the contract with three pointers.

**Consumer walk CONFIRMED at the two op-skill sites:**

- `vlt-lint/references/fix-and-file.md:29-43` — adjudicable contradictions route to backlog, splitting
  only on `maintenance` vs `knowledge-gap` (`:43`: *"`knowledge-gap` when closing it needs a source
  the vault doesn't have"*). No address axis.
- `vlt-ingest/SKILL.md:129` — the same split, and the skill itself calls this *"the write-side
  counterpart of `vlt-lint`'s Step 4"*, so the two must move together. Confirmed.

**The proposed rule and its three guards, carried as filed** (not adopted): *a noticed gap goes to
`{backlog}` only when the filing partner does not know whose turn it is; when it does, the gap is
relayed to that partner (`vlt-dispatch relay`, shape `ask`). The backlog is evolution intake, not a
shared to-do list — it holds the unassignable.* Guards: **(1)** binds every `kind`, not just
`knowledge-gap` — it is a rule about address, not subject; **(2)** self-addressed work is not a relay
(a partner does not relay to itself, else a literal reading produces librarian→librarian relays);
**(3)** migration is one-home — an item that acquires an owner is relayed **and struck** from `## Open`,
never left in both rails.

**The limit paragraph the filing asks be taken with the rule, carried verbatim in intent:** relay
**does not schedule work**. It buys an **address and a drain** — which the backlog has neither of —
and **not execution**. The filing measured 7 open pointers, oldest 27 days, and states that age tracks
time-since-last-summoned rather than neglect. *"If the module takes this rule, please take that
paragraph with it"* — because without it the obvious misreading is that moving items onto the bus
makes them happen, and the next person to measure a stale slice concludes the rail failed when it did
exactly what it claimed.

**Dependency: this ships with A7-11 or not at all** — the rule routes work onto the rail A7-11
repairs, and the `ask` shape it names does not exist until A7-11 lands.

**Standing vault divergence to weigh at acceptance**, disclosed by the filing: both fixes were applied
in vlt-core as **base edits** (`frontmatter` 5→6 with the full consumer walk), because an overlay can
only add and both change existing rules. vlt-core therefore carries a live `convention_base_divergence`
against `frontmatter.md` plus local edits to `vlt-dispatch`, `vlt-lint`, `vlt-ingest` and `vlt-mint`'s
template until the module accepts or rejects. `vlt-lint` will flag it, correctly, in the meantime.
Note this is a live instance of the A7-8 wall: *a change with no overlay form has only the base.*

**The consolidation pattern, worth recording as an observation:** the triage moved 23 addressed items
onto the rail as **9 asks**, because nine of them were the same act. *"A backlog accumulates items one
filing at a time, so it never sees that nine of them are one act."*

---

### A7-13. `vlt-mint` mandates a council it has no fallback for (2026-08-14) — `2026-08-14-182143-mint-mandates-a-council-it-has-no-fallback-for.md`

**CONFIRMED — the gate is unconditional and no branch exists.** Read `skills/vlt-mint/SKILL.md:92-102`
in full:

- `:92-95` — Step 2a is four numbered steps: stage in the live tree, **invoke** the council via
  `workflow('vlt-review-council', …)`, capture, act. There is **no branch** for the workflow being
  unavailable — step 2 assumes the invocation returns.
- `:99` — *"**Capture is mandatory, not optional.** Before the mint goes live, record the verdict
  **and its reasoning** … A gated change must carry its own rationale."* Verbatim as filed.
- `:102` — *"**Exit gate — Phase 2 → 3:** the council verdict is **resolved** … **and** every open
  user-decision is **ruled**."* The same line confirms the asymmetry the filing points at: council-none
  kinds *"clear this phase trivially"* while gated kinds have no cheap path at all.
- `:100` — the verdict vocabulary is `pass` / `revise` / `reject`. **There is no facet for how the
  verdict was reached.** A user-ruled substitute and a four-lens panel produce the same string, so the
  decision log — the permanent, upgrade-durable record — cannot distinguish them. That is the
  silent-by-construction half, and it grounds exactly.

**The "stall path is already almost built" claim CONFIRMED, and it is what makes this cheap.**
`vlt-mint/SKILL.md:57-66` specifies the gated-kind planning doc at `_agent/mint/{date}-{slug}.md`,
explicitly *"live/resumable"*, holding the current phase and a done/pending checklist; `:26` is the
activation-time *Resume an in-flight mint* scan. **The machinery to park a mint mid-Phase-2 and resume
it where a panel can run exists and is exercised — it simply is not named as the response to an
unavailable council.**

**PROVENANCE — the filing's guess, and grounding supports the refined version it offers.** It guesses
the gate assumed an interactive foreground session, but corrects itself: `vlt-mint` does contemplate
non-interactive use, and sibling ops name headless behavior. Grounding agrees with the refinement —
headless was reasoned about for the **council-none** paths (`:102`'s trivial clearance) and never
re-checked against the **gated** ones, where it is load-bearing.

**Scope note, and the filing draws it correctly itself:** the triggering condition (a background job
whose harness defaults workflow fan-out off) is **Claude-Code-side, not module source**, and the
filing explicitly declines to file it as module feedback. The module-side defect is the missing named
path, which any tool-restricted environment reaches.

**Open design question, carried verbatim — the filing does not presume to answer it and neither does
capture:**

> 1. **A user-ruled verdict is a legal verdict type for a gated kind** — with a *required* companion
>    field recording that the panel was not fielded and why … Cheap; keeps constrained environments
>    productive; risks normalizing the escape.
> 2. **The mint refuses to proceed** — Phase 2 becomes hard-blocking, the planning doc parks … Preserves
>    the gate's meaning exactly; costs a round trip.
> 3. A **degraded panel** — the moderator's four-part synthesis produced inline by the minting context
>    against the same `{personas}` lenses, explicitly labelled as single-context. Weaker than N
>    independent lenses and should be recorded as such, but it is a named path rather than an improvisation.

**Adjacent, not duplicate:** `inbox/2026-07-16-153000-new-partner-fields-one-lens.md` (captured in
Arc 3, held active) reports that the highest-stakes mint gets the thinnest panel *composition*. This
is panel *availability*. Same direction — *the council is the module's least-defended machinery* — and
a fix for either leaves the other standing. Worth grouping at ideation.

**Calibration disclosure, carried because acceptance should weigh it:** because the gate was
substituted rather than skipped, the mint shipped **base** convention edits (`frontmatter` 5→6 with a
full consumer walk). The quality of that substituted review is now load-bearing on A7-11, A7-12, and
a standing base divergence in vlt-core.

---

## Capture narrative — judgment calls this run made

- **New arc, not an amendment.** No roadmap in `skills/reports/` qualified as open: Arc 6 is CLOSED
  and archived (v0.9.1 @ `e930a40`). Arc 7 opened per the Discovery rule; ids are `A7-*`.
- **Scope: all 13 un-captured filings**, confirmed with the owner before grounding. The other 26 files
  in `inbox/` all appear in archived arc roadmaps and are held active pending acceptance, not
  un-captured. Three of the 13 are Arc 6's named carries (**C6-a** → A7-1, **C6-b** → A7-2,
  **C6-d** → A7-3), each recorded there as *awaiting `inbox-capture`*.
- **A7-2's mechanism was re-derived and reproduced**, not read. The filing marked its provenance as a
  guess and asked capture to check; the guess was wrong and the real rule is broader (any unanswered
  module variable, not just map-shaped ones). Reproduced on a scratch fixture in both the failing and
  the correct payload shape. Consequence: the caller-side error is real *and* the module-side defect
  is real; capture files both rather than closing the filing as operator error.
- **A7-11's open question was answered at capture, deliberately.** The filing named one thing it most
  wanted checked (relay facet vs a consult-adjacent async mode). Grounding produced a clear
  module-source answer, so it is recorded as a finding rather than passed through as an open question —
  the ruling still belongs to ideation.
- **Three filings' vault-side counts are taken as reported** (A7-6's two live specs, A7-11's 40/27/13
  relay split, A7-12's 85/33 backlog measurements). None are verifiable from module source, and none
  are load-bearing: each mechanism finding stands on the shipped spec alone. Flagged inline where it
  matters.
- **Two provenance corrections issued**: A7-12's consumer walk is 3 shipped partner skills + 1 mint
  template, not 8 files (8 is vlt-core's local roster); A7-2's failure mechanism is not a map-shape
  branch. A7-3's *own* correction (the `references/` loss landed at 0.9.0, not 0.9.1) was verified and
  is right.
- **Three findings were widened beyond what was filed**: A7-6 has a second stale site
  (`spec.md:14`, not just `:92`); A7-7's overlay blindness is a three-workflow class (`vlt-consult.js`
  and `vlt-review-council.js` are equally overlay-free); A7-11 has a second key-definition site
  (`vlt-dispatch/SKILL.md:22`) that any relay-key change must touch.
- **No design questions were resolved.** A7-3, A7-4, A7-5, A7-9 and A7-13 all carry open questions
  forward verbatim, per the grounding methodology. The through-line's "narrow fixes vs one designed
  receiving surface" framing is an observation about the batch, not a ruling.
- **Not blocking on anything.** No filing's core claim conflicts with an unshipped module change;
  nothing here needs an owner ruling before ideation.

## Ideation rulings — A7-1..A7-13 (owner-steered, 2026-08-15)

Rulings below are the owner's; briefs cite this section, never re-litigate. **Session OPEN — every
slot below is unfilled.** The unresolved question pool for this batch is the per-filing open-question
and carried-shape material in this roadmap's own *Capture* section (A7-3, A7-4, A7-5, A7-6, A7-8,
A7-9, A7-11, A7-13 each carry questions verbatim) plus the four cross-filing dependencies and the
arc-level framing question named in *The through-line*; each question ends this session either ruled
here, or explicitly left to brief time, per build. A slot left empty is honest — do not fill it with a
guess, and do not let a brief infer one.

**SESSION CLOSED 2026-08-15 — every slot below is filled:** four pre-ideation rulings, six cross-filing
rulings (plus one same-session amendment), grouping & order (**eight builds, B7-1..B7-8**, ship order
set), spikes (none opened; three read-before-brief obligations pinned), five evidence debts
dispositioned, and every remaining pool question designated to a named brief. **Three rulings were
owner-delegated to the clerk** and are recorded as owner-adopted per the Arc-5 delegation precedent
(itself citing the Arc-3 ship-order slot): the arc-level framing split, the count-since-N principle,
and the handshake-node ruling. Two more were the owner's stated gut with the clerk concurring (the
structural doctrine, the skill-overlay veto). All are marked **overturnable** where the clerk supplied
the reasoning; none of the seeded questions was answered on the owner's behalf without being put to
them first.

**One capture correction was issued this session** and is recorded at its slot: the `frontmatter.md`
base-edit set is **four filings, not three** — A7-9 changes YAML rule 4 and the capture's dependency
note omits it. The correction changed the arc's shape (it produced B7-3 as a dedicated bump build).

**Time-boxed item the owner should see first (not a ruling, a clock):** A7-5's three shipped
`review_after: 2026-08-17` dates expire **two days from this scaffold**. Every 0.9.1 install begins
reporting `deferral_expired` on `frontmatter@5`, `spec@2` and `wiki-consolidation@1` on that date,
whether or not this arc has ruled anything.

**Grouping & order** — **RULED 2026-08-15 (owner accepted the clerk's drafted grouping as-is;
clerk-drafts-owner-amends mode, per the Arc-3 and Arc-5 precedents).** **EIGHT builds over the
thirteen filings** — every filing has a home, and the draft was derived from the eleven rulings above
rather than proposed ahead of them. Numbering follows intended ship order at assignment, per the
Arc-3 convention (a build that later slips does not renumber). `B7-*` per the Arc-5 slug convention.

| Build | Filings | Subject & notes |
|---|---|---|
| **B7-1** | A7-1 | **The harness.** Opens the arc. Seeds the four fixture gaps (rule-card + `derived_from:` sha256, minimal `vlt-vitals.py` with a parseable `METRICS` table, tripwires seed whose metric ids resolve, `vault_structure.default` agreeing with the fixture contract) and restores case 1's exit-0 assertion as the load-bearing baseline. **First application of the structural doctrine** — the fixture is built *from* the structure contract, not hand-listed. Ships first: *"sequencing it late means each build re-negotiates the same 9/11."* The ruling worth enshrining ahead of the four seeds is the filing's own: *a rule that can only be observed passing on the artifact it was authored from is not yet tested.* |
| **B7-2** | A7-2 + A7-3 | **The durability nets.** The doctrine's second application, at two altitudes. A7-3: the skill-asset manifest derived by walking the shipped tree, covering **both** `references/` (regression, landed v0.9.0 / `f3b343d`) and `scripts/` (original gap, `8c0955f` / v0.3.0) per the same-build ruling, with the provenance kept distinguishable in the brief. A7-2: `merge_config()` becomes preserve-unless-answered instead of rebuild-from-answers, **and reports what it removed** (the second ask is independent and is the minimum honest fix either way). **Depends on B7-1** — groups C7 and E cannot be proven against today's fixture. |
| **B7-3** | A7-5 + A7-8 + A7-9 + A7-12 (**base edits only**) | **`frontmatter@6`.** The single 5→6 bump, one six-consumer re-ack, bipartite consistency verified in-build. Ships **rules, not mechanisms**: the vault-writable-field declaration (A7-5), the baseline-exempt local convention declaration (A7-8), rule 4's traverse-vs-verify split (A7-9), the address rule with its three guards (A7-12). Also applies the count-since-N principle to `frontmatter@5`'s own threshold. **Precedes all three mechanism builds**; its acceptance checks are about the handshake, not behavior. |
| **B7-4** | A7-5 + A7-8 + A7-4 (**mechanism**) | **The seam.** The designed receiving surface the framing ruling scoped: the divergence diff honors declared vault-writable base fields (generalizing `adoption_first_instance:` — and per the doctrine, by declaration rather than by growing the hard-coded exclusion list at `checks.md:41`); consumers read vault-originated local conventions the way they read overlays, visible to the split tripwire; and `vlt-dispatch` gets a designed-parameter read on the shipped `vlt-track` pattern. **The veto stands** — no generic skill-overlay mechanism; A7-4 may still resolve to *"apply the `vlt-track` pattern"* rather than new machinery. Cites B7-3's rules. |
| **B7-5** | A7-11 + A7-12 (**mechanism**) | **Relay & address.** The `shape` facet (`handoff`/`ask`/`answer`) and `ref` key, with the idempotency key becoming `(handoff-path \| ref, to-slug)` — **updating both key-definition sites** (`references/relay.md` and `vlt-dispatch/SKILL.md:22`, one pointing at the other per single-home). The contract takes ownership of the file-it-to-`{backlog}` reflex with **four pointers** (3 partner skills + `vlt-mint`'s template). Carries the **limit paragraph** verbatim in intent (*relay buys an address and a drain, not execution*) and the severable unbounded-`{backlog}` Beat-2 fix at `vault-operating-contract.md:169` (plus the same leak at `partner-agent-template.md:40`). Backward-compatible, no backfill. |
| **B7-6** | A7-7 + A7-9 + A7-10 (**mechanism**) | **The overlay contract.** All three workflow assets (`vlt-lint-full.js`, `vlt-consult.js`, `vlt-review-council.js`) become **first-class handshake nodes** and gain the merged-on-read contract, per the class ruling; a workflow with no convention read today satisfies it at the point it would read one. A7-9's wikilink `sources:` form ships with the **normalization clause** protecting `linkage_ripe`'s shared-source leg (`checks.md:59`) — *"a blind spot in an absorption test is a false positive."* A7-10 rides here, per its binding contingency. Wire the node check into `package-lint.py`. |
| **B7-7** | A7-13 | **The council fallback.** A named path for an unavailable council, built over the park-and-resume machinery that **already exists** (`vlt-mint/SKILL.md:57-66`, `:26`) and *"simply is not named as the response."* Plus a **verdict-provenance facet** — `:100`'s `pass`/`revise`/`reject` vocabulary today cannot distinguish a four-lens panel from a user-ruled substitute in the permanent decision log. Brief re-reads `inbox/2026-07-16-153000-new-partner-fields-one-lens.md` (Arc 3, active): availability vs composition, *"a fix for either leaves the other standing."* |
| **B7-8** | A7-6 | **The stale-prose sweep.** `spec.md`'s **two** stale sites (`:92` Enforcement *and* `:14`'s frontmatter comment — *"any fix must touch both or the correction half-lands"*), rewritten in the conditional form that is true in both regimes. Prose clarification: **no `spec` bump**. Carries the **shared audit** — count-since-N metrics (ruled above) and prose asserting a permanent property a frontmatter field can invalidate — over the same surface in one sweep. Last: the sweep benefits from watching B7-1..B7-7's own verification passes (the build-23 precedent). |

**Ship order — SET 2026-08-15: `B7-1 → B7-2 → B7-3 → B7-4 → B7-5 → B7-6 → B7-7 → B7-8` as numbered.**
Hard constraints inside that order, so a reshuffle can be checked against them: **B7-1 before B7-2**
(fixture); **B7-3 before B7-4, B7-5 and B7-6** (rules before mechanisms — and B7-3 is the arc's only
`frontmatter` bump); **B7-5 and B7-6 both after B7-3** but interchangeable with each other; **B7-7 and
B7-8 float** — neither gates anything, and B7-8 is deliberately last. B7-4 is the arc's largest design
and the most likely to slip; it does not gate B7-5 or B7-6.

**→ AMENDED 2026-08-15 — two additions to scope, no change to the order.** **B7-1 additionally carries
R2** (any build changing a release-gate check extends the fixture in the same build, enforced
mechanically via a case-count shrink check and a no-fixture-case lint failure) — it is the build that
owns the harness and it ships first. **B7-3 additionally carries R1** (a rule shipped ahead of its
mechanism states its interim posture in the same build), which includes A7-5's field-facing interim
sentence. **One act moves earlier than any build:** the count-since-N / stale-prose **class count**
runs before B7-3 is briefed (amendment A4). See *Post-ideation amendments*.

Capture's material bearing on grouping, carried as **capture's material, unaccepted** — the capture
made no grouping proposal, and none of the following is one:

- **Four dependencies the capture states as binding or near-binding** (*The through-line*,
  §*Cross-filing dependencies*): **A7-9 → A7-10** (A7-10 is explicitly contingent — *"if that
  candidate is declined, this one is moot and should be archived with it"*; they must be ruled
  together); **A7-11 ↔ A7-12** (*"neither makes sense shipped alone"* — A7-12's rule routes work
  onto the rail A7-11 repairs, and the `ask` shape it names does not exist until A7-11 lands);
  **A7-2 ↔ A7-3** (both widen what `vlt-upgrade`'s pre-flight snapshots — *"whether that is one
  build is an ideation ruling"*); **A7-9 → A7-7** (A7-7's suggested acceptance case *is* A7-9's local
  override — fixing A7-9 upstream without A7-7 removes the demonstration but not the class).
- **A7-1 as an early-sequencing candidate:** *"every build in this arc that adds or changes a lint
  check inherits a harness that cannot prove a clean baseline … sequencing it late means each build
  re-negotiates the same 9/11."*
- **A7-4 / A7-11 / A7-12 are all dispatch-shaped:** *"if a routing profile is built, three filings
  want to know its scope … Group with care."*
- **A7-13 ↔ `inbox/2026-07-16-153000-new-partner-fields-one-lens.md`** (captured Arc 3, still
  active): panel *availability* vs panel *composition*, *"same direction … worth grouping at
  ideation."*
- **A7-5, A7-8, A7-12 all touch `frontmatter.md`** (`version: 5`, six consumers): *"if two of these
  ship in one arc, the version handshake wants planning, not three sequential bumps."*
- **A7-1's own coupling observation:** the fixture's missing `vault_structure.default` is the same key
  A7-2 files, and its absent `references/` is the same directory class A7-3 files — *"three filings,
  three different mechanisms, one under-modelled fixture."*

**Pre-ideation rulings the capture demanded** — the capture states it is **not blocking on anything**
(*"nothing here needs an owner ruling before ideation"*). No slot is therefore gated. The questions
the capture nevertheless flagged as ideation's to answer before grouping can settle are seeded below,
unanswered:

1. **The arc-level framing question** (*The through-line*, stated as an observation about the batch
   and explicitly **not** a ruling): is the answer to the six no-landing-zone filings (A7-4, A7-5,
   A7-8, A7-11, A7-12, A7-13) **a family of narrow fixes, or one designed receiving surface**?
   **→ RULED 2026-08-15: SPLIT — one designed seam over A7-5 + A7-8 (+ A7-4), narrow fixes for
   A7-11, A7-12, A7-13.** Owner delegated this slot to the clerk (*"no strong opinion, I defer to
   your lean"*); recorded as owner-adopted, per the Arc-5 delegation precedent (which itself cites
   the Arc-3 ship-order slot). Rationale on record, so a brief can test it rather than inherit it:
   the six do not divide the way the through-line's prose groups them. **A7-5, A7-8 and A7-4 are the
   real class** — each is a vault holding legitimate content (a performed review, a novel convention
   subject, a population policy) with no sanctioned place to put it, and all three answer to the
   *same* seam question: where does vault-originated content legally live, and how does a module-owned
   reader see it? They already share one precedent — `adoption_first_instance:` as the authorized
   vault-local carry the divergence diff excludes (A7-5, A7-8) — and one shipped pattern, `vlt-track`'s
   designed-parameter read (A7-4). **A7-11, A7-12 and A7-13 are not that class**: A7-11 is a missing
   idempotency key on an existing rail, A7-12 an address rule plus a stale sentence, A7-13 a missing
   branch over park-and-resume machinery that already exists. Nothing in the three is vault-originated
   *content*; each is a mechanism the module owns and under-specified, each is cheap, and capture has
   already grounded the shape most consistent with shipped design for all three. Coupling them to a
   surface design would hold three cheap, well-grounded fixes behind the arc's largest open question.
   **Consequences this ruling carries into grouping:** the seam group is one design question and
   should not be split across builds that each invent their own answer; A7-4 may still resolve to
   *"apply the existing `vlt-track` pattern"* rather than new machinery, and the ruling does not
   prejudge that; the narrow three remain governed by their own binding dependency (A7-11 ↔ A7-12).
   **Overturnable** — if the seam design collapses to nothing at brief time, the three fall back to
   narrow fixes without disturbing anything else.
2. **A7-3, verbatim:** *"decide explicitly whether `scripts/` inclusion is in the same build or split
   — it is the same one-line spec change, but it is a new protection, not a restored one."*
   **→ RULED 2026-08-15 (owner): SAME BUILD, BOTH INCLUDED.** One spec change at
   `vlt-setup/SKILL.md:150` covers `references/` (the regression that landed at **v0.9.0** / `f3b343d`)
   and `scripts/` (an **original gap** predating the build-18 manifest spec, first appearing at
   `8c0955f` / v0.3.0). **The blame stays distinguishable in the brief's prose** — the filing was right
   that capture should keep them separable, and this ruling merges the fix, not the provenance. The
   brief states both origins explicitly so the changelog and the acceptance checks can tell a restored
   protection from a new one.
3. **A7-5, flagged as wanting a ruling of its own:** `frontmatter@5`'s threshold is a **count-since-N
   metric** whose baseline count is recorded nowhere a vault can read — the filing flags this as *"a
   general property of count-since-N metrics in shipped frontmatter, not a one-off."*
   **→ RULED 2026-08-15: PRINCIPLE NOW, SIZING BY AUDIT — a shipped deferral metric must be evaluable
   from vault-readable state alone, and a metric that counts from a baseline ships that baseline in
   its own frontmatter.** Owner delegated this slot to the clerk (*"unsure, defer to your lean"*);
   recorded as owner-adopted per the same delegation precedent. This is deliberately **both** of the
   two shapes put to the owner, and the split is the point: the *rule* needs no audit to justify — a
   metric a vault cannot evaluate is the proxy-check failure Arc 5 already ruled against (*"a check
   must be able to state what it actually measures"*, A5 pre-ideation ruling 3) — while the *fix* has
   unknown extent, and Arc 5's recorded counter-lesson is build-20's sized-by-assumption failed clause.
   So the principle is written once here and cited; **the audit sizes the work and shares one sweep
   with A7-6's sibling class** (see the Spike-obligations slot), since both sweep the same surface:
   shipped convention frontmatter making claims that its own fields can invalidate or that a vault
   cannot check. Applies to every shipped convention, not just `frontmatter@5`. **Overturnable** if the
   sweep shows `frontmatter@5` is the only instance — a class of one is a fix, not a doctrine.
   **→ AMENDED 2026-08-15 by post-ideation amendment A4** — sizing and fixing split; the count runs
   before B7-3 is briefed, which is what makes this overturn clause executable. See
   *Post-ideation amendments*.
4. **A7-7's governance half:** `frontmatter.md`'s base-edit ceremony holds that *"a consumer's ack
   covers its own workflow assets"* — capture's finding is that **an ack that covers assets by
   declaration rather than by inspection drifts silently**. Is that a version-handshake ruling for
   this arc (three filings would bump `frontmatter`), or a build's business?
   **→ RULED 2026-08-15: WORKFLOW ASSETS BECOME FIRST-CLASS NODES IN THE HANDSHAKE GRAPH.** Owner
   delegated this slot to the clerk (*"unsure, defer to your lean"*); recorded as owner-adopted per
   the same delegation precedent. An asset covered *by* a consumer's ack is invisible to the build-4
   bipartite check (every consumer listed ↔ every ack current), so nothing mechanical can ever catch
   its drift — which is exactly what happened. The rejected alternative was *"re-acking requires
   inspecting the asset"*: that is a prose promise about an act, unverifiable after the fact, and it
   fails the same test the arc is applying everywhere else (A7-2 reports `"status": "success"` for a
   destroyed block; A7-3 trusts an enumeration; A7-1 cannot prove its own baseline). Naming the asset
   makes staleness a **missing ack** — a state, checkable — instead of a silence. **The brief owns the
   mechanical form** (a `depends_on` header comment in the `.js`, or an explicit asset list on the
   consumer's frontmatter) and should wire the check into `package-lint.py` so the release gate
   carries it; note that couples to **A7-1**, whose group C7 fixture builds no `references/` and
   therefore proves nothing today. **Scope: all three overlay-blind workflows** become nodes
   (`vlt-lint-full.js`, `vlt-consult.js`, `vlt-review-council.js`) — per capture's widening, this is a
   three-file class. This ruling is about **visibility of the ack**; whether each workflow must
   actually *implement* the overlay-merge read is A7-7's build question, not this slot's.

**Cross-filing decide-once rulings** — **ALL SIX RULED 2026-08-15.** Candidates the capture surfaced as the same
question arriving in more than one filing; each ends this session ruled once here, or explicitly
pushed to a named build:

- **The `frontmatter` bump plan** (A7-5, A7-8, A7-12; base at `version: 5`, six consumers; A7-12's
  vlt-core fix was already a 5→6 base edit with a full consumer walk) — one coordinated bump and one
  consumer walk, or sequential? **→ RULED 2026-08-15 (owner): ONE COORDINATED 5→6 BUMP.** Whichever
  build lands first opens `frontmatter@6`; every rule change from A7-5, A7-8 and A7-12 that touches
  the base rides that one bump, and **one** consumer walk re-acks all six consumers. Follows the
  build-16 precedent (`frontmatter@3` batch — *"one coordinated bump, one consumer walk — NOT split"*).
  **Binding consequences for grouping and for the briefs:** (1) the `frontmatter@6` opener inherits the
  full base-edit set, so no later Arc-7 build may bump `frontmatter` again — a rule change arriving
  after the opener ships either rides it or waits for Arc 8; (2) the ruling **crosses the framing
  split above** — A7-5 and A7-8 sit in the seam group and A7-12 in the narrow three, so the opener's
  ship order must be settled at grouping, not left to fall out; (3) per the version-handshake rule, the
  opening build verifies bipartite consistency (every consumer listed ↔ every ack current) in the same
  build; (4) A7-7's finding bites here — the ack *covers workflow assets by declaration*, and this
  bump re-acks `vlt-lint`, whose `vlt-lint-full.js` is overlay-blind. See the pre-ideation slot,
  question 4.
  **→ AMENDED 2026-08-15, same session — the set is FOUR filings, not three.** Discovered while
  drafting grouping and put to the owner: **A7-9 is also a `frontmatter.md` base edit** — the
  traverse-vs-verify distinction changes YAML **rule 4** at `frontmatter.md:36`. The capture's
  cross-filing dependency note names only A7-5, A7-8 and A7-12; that list is incomplete, and this
  amendment is the correction (recorded here rather than in the capture, which is closed).
  **→ RULED 2026-08-15 (owner): A DEDICATED `frontmatter@6` BUILD.** One build carries **all four**
  base rule changes (A7-5, A7-8, A7-9, A7-12) plus the single six-consumer re-ack and the bipartite
  consistency verification; the **mechanisms** ship in their own builds and **cite** the rules rather
  than re-litigating them. Chosen over making the seam build the opener because the four edits sit on
  both sides of the framing split — A7-5/A7-8 in the seam group, A7-12 in the narrow three, A7-9 with
  the overlay work — so any build-hosted bump drags unrelated filings across the split. **The known
  cost, stated so the briefs plan for it: this deliberately separates rule from mechanism.** Each
  mechanism brief must cite the `frontmatter@6` build's ruled rule text as its contract, and the
  `frontmatter@6` build ships rules whose mechanisms do not yet exist — which is legal (a `declared`-
  stage rule is a real rule) but means its own acceptance checks are about the *handshake*, not about
  behavior. Ship order must put it ahead of all three mechanism builds.
  **→ AMENDED 2026-08-15 by post-ideation amendment A1** — the no-later-bump clause now carries a
  named reopen condition, and B7-3 inherits R1's interim-posture requirement. See
  *Post-ideation amendments*.
- **The authorized vault-local carry-forward precedent** (A7-5, A7-8): `adoption_first_instance:` is
  the one field the divergence diff already excludes — *"the module already has exactly one field of
  the shape the filing's narrowest candidate asks for."* Does that precedent generalize (an
  overlay-writable `review_after`, a baseline-exempt local convention), or stay a one-off?
  **→ RULED 2026-08-15 BY CONSEQUENCE: IT GENERALIZES.** Not put to the owner separately — the A7-5
  ruling below (overlay-writable `review_after` on this precedent) decides it, since a second instance
  of a one-off is a category. Recorded here so the seam group's brief inherits it as a stated rule
  rather than re-deriving it: **a base field may be declared vault-writable, and a declared one is
  excluded from `convention_base_divergence` the way `adoption_first_instance:` already is.** The open
  half, carried to the seam brief: the exclusion list is today a **hard-coded field name** in
  `vlt-lint/references/checks.md:41`, so generalizing it means either a growing enumeration — the
  exact class this arc is prosecuting three times over — or a declaration the base file carries about
  itself. **Flag it as a candidate instance of the enumeration-vs-structure ruling below.**
- **The single-home reflex sentence** (A7-12): the file-it-to-`{backlog}` boilerplate is copied across
  3 shipped partner skills + `vlt-mint`'s partner template — *"single-home discipline says the reflex
  belongs in the contract with three pointers."*
  **→ RULED 2026-08-15 (owner): THE CONTRACT OWNS IT, FOUR POINTERS.** The reflex moves to the
  operating contract; `vlt-agent-creative/SKILL.md:48`, `vlt-agent-librarian/SKILL.md:47`,
  `vlt-agent-researcher/SKILL.md:50` and `vlt-mint/assets/partner-agent-template.md:63` each carry a
  short pointer and no restated mechanics. **The template pointer is the load-bearing one** — it is
  the leak into every future minted partner, and the only one that fixes instances that do not exist
  yet. Note the same template propagates the unbounded `{backlog}` orient read at `:40`, which is
  A7-12's severable Beat-2 finding; the brief should touch both in one pass since it is editing the
  file anyway. Applies the standing single-home rule; no handshake implication (the contract is
  deliberately not handshaked — single-home + pointers is its mechanism).
- **The overlay-merge contract for workflow assets** (A7-7, widened at capture): `vlt-lint-full.js`,
  `vlt-consult.js` and `vlt-review-council.js` all return `grep -c overlay` → **0** — *"a three-file
  class, not a one-file defect."* Ruled as a class, or fixed where it bites?
  **→ RULED 2026-08-15 (owner): AS A CLASS — all three receive the contract.** The operating
  contract's invariant (`vault-operating-contract.md:100` — *"the convention is the base file plus its
  overlay, merged on read"*) binds **every workflow asset that reads a convention**, not just the one
  where the break was observed. Pairs with the handshake ruling above (pre-ideation 4): the same three
  files become named nodes, so a workflow that acquires a convention read later cannot acquire it
  overlay-blind and unacked. **Brief-time latitude, stated so the ruling isn't read as busywork:** a
  workflow with no convention read today satisfies the contract by carrying the merged-read requirement
  at the point it would read one — the ruling forbids a *blind* read, it does not mandate a read. The
  acceptance case is A7-7's, carried as filed: *a page compliant with an overlay rule that contradicts
  its base survives a full sweep with no finding* — and note that case **is** A7-9's local override,
  so the two filings demonstrate each other.
- **Enumeration-vs-structure on the durability nets** (A7-2, A7-3, and A7-1's fixture): three
  instances of the module's own standing rule — *lists that claim completeness drift* — firing inside
  the machinery built to catch drift. One doctrine ruling, or three fixes?
  **→ RULED 2026-08-15: DOCTRINE — a durability net defines its protected surface STRUCTURALLY, never
  by enumeration.** Owner's gut (*"my gut says #1 durability nets are structural"*) with the clerk
  concurring; recorded as the owner's. **The rule:** a mechanism whose job is to protect or preserve a
  set of files/keys derives that set by walking the tree or reading a declaration the protected thing
  carries about itself — it does not carry a list. A net that must carry a list carries a **shrink
  check** as well, because a silently narrowing list is indistinguishable from a passing one.
  **Rationale on record:** this is the module's own standing rule turned on its own machinery, and the
  arc found it failing four times — `vlt-setup/SKILL.md:150`'s manifest enumeration (A7-3),
  `merge-config.py`'s rebuild-from-answers (A7-2, which is enumeration by *omission* — anything
  unnamed is destroyed), `test-package-lint.py`'s fixture (A7-1, an enumeration of what the harness
  imagines the tree contains), and the divergence-exclusion field list (recorded above). Four
  instances is a class by any threshold the repo uses. **Known applications, each still needing its
  build's brief to size it:** the skill-asset manifest → walk the shipped tree; `merge_config()` →
  preserve-unless-answered rather than rebuild-from-answers, and **report what it removed** (A7-2's
  second ask is independent of the first and is the minimum honest fix either way); the lint fixture →
  built from the real structure contract, not hand-listed; the exclusion list → a declaration the base
  convention carries. **What the doctrine does not do:** it does not require any of these rewritten in
  one build, and it does not forbid an enumeration that is *generated* and verified — a computed list
  is a structure read with a cache.
- **The pre-rejected shape A7-4 asks stand:** *not* a generic skill-overlay/extension mechanism — the
  `vlt-upgrade/SKILL.md:48` veto (*"skills have no overlay mechanism"*) should hold. Confirm or
  overturn — **→ RULED 2026-08-15: THE VETO STANDS.** Owner's gut (*"my gut says veto stands"*) with
  the clerk concurring; recorded as the owner's. No generic skill-overlay or skill-extension mechanism
  is opened in this arc. A7-4's answer must be a **designed parameter read** on the shipped
  `vlt-track` pattern (`vlt-track/SKILL.md:16,31-40` — the loop profile read from the invoking
  partner's `capabilities/track.md`, the skill *"hardcodes none of it"*, with `:41`'s named headless
  fallback), not a new extension layer. **This is the seam group's outer boundary**: the seam may
  make module-owned readers read vault-declared *parameters* and vault-declared *content*; it may not
  make skills themselves locally patchable. **Clerk's recommendation, NOT a ruling** — the owner was
  not asked this and should rule it at the seam brief: record the veto's *reasoning* in the operating
  contract, not just the veto, so the next dispatch-shaped filing does not re-propose the shape a
  fourth time. Three filings this arc are dispatch-shaped and the re-apply treadmill A7-4 documents is
  real; a veto whose cost is visible and whose rationale is not invites re-litigation.

**Spike obligations** — **RULED 2026-08-15: NO spikes opened.** The capture flagged no external-source
unknowns in this batch. Three read-before-brief obligations are pinned instead, so they cannot be
lost. Pins are a mechanical consequence of the grouping table, not separate decisions:

- **A7-4's decision matrix is unreadable from the factory** — the filing's full matrix lives in a
  vault-side session artifact (`_output/problem-solution-2026-08-08.md`); *"the filing's summary is
  the only account capture has."* **→ PINNED to B7-4's brief, and it is an OWNER ACTION**: the factory
  cannot read it, so the owner supplies the matrix (or rules the filing's summary sufficient) before
  B7-4 is briefed. B7-4 is the arc's largest design and the matrix is the only record of the
  alternatives already weighed in the field — briefing without it re-does that work blind.
  **→ SUPERSEDED 2026-08-15 (B7-4 brief, disposition 1): the artifact is unrecoverable.**
  `_output/problem-solution-2026-08-08.md` does not exist anywhere in vlt-core (no `_output/`
  directory; no matching artifact under `_agent/artifacts/`) — and the filing itself locates the
  session at the **team-vault install, not vlt-core**, so the pin pointed at a vault that never
  held it. The owner directed the build cycle to complete without further input; the B7-4 brief
  re-derives the decision space from the filing's summary + the shipped `vlt-track` precedent and
  carries a prominent ⚠ owner-review flag on the reconstruction (see
  `skills/reports/build-B7-4-the-seam.md`, dispositions 1/6/7).
- **A7-5's provenance question, unresolved at capture** — whether the three `review_after` dates were
  set as one uniform ~3-week horizon rather than derived per-convention is *"answerable from
  `skills/reports/archive/` if ideation wants it,"* and the answer changes *which* candidate is right,
  not whether the gap exists. **→ PINNED to B7-3's brief** (the build that owns the dates). Cheap — an
  archive read, no external source. **Not blocking**: A7-5's shape is already ruled, so the answer
  affects the date-setting, not the mechanism.
- **A7-6's unaudited class** — *"if the class is prose asserting a permanent property a frontmatter
  field can invalidate, `spec.md` may not be the only instance. No audit was performed … an audit
  sweep is a plausible small build, not a capture act."* **→ PINNED to B7-8**, which carries it as
  **one sweep shared with the count-since-N audit** (pre-ideation ruling 3) — both traverse the same
  surface: shipped convention frontmatter making claims a vault cannot check or a field can
  invalidate. B7-8 is last precisely so the sweep runs against the arc's finished state.
  **→ AMENDED 2026-08-15 by post-ideation amendment A4** — the pin splits: the **count** runs before
  B7-3 is briefed (it depends on nothing), the **fixes** stay in B7-8. See *Post-ideation amendments*.

**Evidence-debt dispositions** — **RULED 2026-08-15, all five dispositioned:**

- **A7-2's open lead** — the vlt-core 0.8.0 → 0.9.0 ledger entry (*"map reconstructed, local
  `dog_training_root:` kept"*) as possible evidence of a prior strip; *"not verifiable from module
  source … left open, marked as a lead, not a finding."* **→ ATTACHES to B7-2; NOT BLOCKING.** The
  mechanism is confirmed and reproduced at rest, so the lead can only add a prior instance, never
  change the fix. Worth chasing at acceptance because a confirmed prior strip would tell the field how
  much silent loss already happened.
- **Three filings' vault-side counts taken as reported** — A7-6's two live specs, A7-11's 40/27/13
  relay split, A7-12's 85/33 backlog measurements. **→ NOT BLOCKING on any build.** None is
  load-bearing — each mechanism finding stands on the shipped spec alone — and capture flagged them
  inline. They attach to **acceptance** for B7-5 and B7-8: the relay split and backlog counts are the
  natural before/after measure of whether the `ask` shape and the address rule actually drained
  anything.
- **A7-12's standing vlt-core base divergence** — both fixes shipped there as **base** edits
  (`frontmatter` 5→6 plus local edits to `vlt-dispatch`, `vlt-lint`, `vlt-ingest`, `vlt-mint`'s
  template), so vlt-core carries a live, correct `convention_base_divergence` until the module accepts
  or rejects. **→ ATTACHES to B7-3**, the build that accepts or rejects those base edits. Note the
  shape: **vlt-core is running a preview of B7-3 and B7-5**, so its experience is the arc's best
  field evidence — and its divergence finding is *correct until B7-3 ships*, which the brief should
  say out loud so nobody "fixes" it early. Capture's own note holds: this is a live instance of the
  A7-8 wall — *a change with no overlay form has only the base.*
- **A7-13's calibration disclosure** — the gate was substituted rather than skipped, so *"the quality
  of that substituted review is now load-bearing on A7-11, A7-12, and a standing base divergence in
  vlt-core."* **→ ATTACHES to B7-7; NOT BLOCKING, but it is an input to B7-3 and B7-5.** The rules
  those two builds ship were reviewed by a substituted council, which is exactly the provenance gap
  B7-7 exists to close. Their briefs should re-derive rather than inherit the substituted verdict's
  conclusions.
- **The inherited A4-4 clause (5) FAILED debt** — carried forward for a **fourth** arc (carrier filing
  `inbox/2026-07-25-160949-auto-caption-name-substitution.md` stays active); Arc 5 attached it to a
  build (B5-2) under the A4-1 inherited-debt-ships-early precedent and it still did not clear.
  **→ RULED 2026-08-15 (owner): ATTACHES to B7-6 AS ITS OWN SCOPE ITEM** — not as a rider. B7-6 is
  already in the lint-full/workflow-asset machinery, which is the closest surface, and naming it a
  scope item rather than an attachment is the deliberate correction to three arcs of riding along and
  losing to the host build's scope. **B7-6's brief must give it its own acceptance check**, and the
  carrier filing stays in the active inbox until that check passes.
  **→ AMENDED 2026-08-15 by post-ideation amendment A3** — that check must be tagged
  **ship-verifiable** and is mandatory to the arc gate; the untagged mandate is what let three arcs
  close around it. See *Post-ideation amendments*.

**Questions deliberately left to brief time** — **RULED 2026-08-15: designated per build; each brief
owns its questions, none stays cross-cutting.** Designations follow mechanically from the grouping
table. Every question below is the filing's own, carried verbatim in intent and **unanswered** — the
designation says *who decides*, never *what*:

- **B7-2 — A7-3:** whether the manifest should be **computed by a script** (`verify-skill-manifest.py`, named
  in the 2026-07-12 handoff as *"prose where a script should be"*) rather than by prose instruction;
  and whether a **manifest-entry-count-didn't-shrink** check belongs in the upgrade report.
  — *(B7-2's brief; the structural doctrine already forecloses the prose-instruction form, so the open half is the shrink-check's home.)*
- **B7-4 — A7-4, five questions verbatim:** *(a)* profile home — `{overlays}/`-adjacent vs agent zone;
  *(b)* one vault-wide profile vs per-partner `capabilities/dispatch.md`; *(c)* v1 parameter scope
  (roster + inbox destinations + relay addressing — more?); *(d)* which vocabulary, if any, belongs in
  a convention instead; *(e)* state the generalized designed-read pattern in the contract now, or wait
  for a second instance. — *(B7-4's brief rules all five; the veto ruling above bounds (a)–(c), and (e) is the one that could still become an arc-level rule.)*
- **B7-3/B7-4 — A7-5, four candidate shapes carried unranked:** overlay-writable `review_after` as an authorized
  vault-local carry; per-convention dates derived from each metric; a distinct finding class for
  *expired, module-owned*; or stating in the declaration that a shipped deferral's expiry is reviewed
  upstream and a vault's only move is to file.
  **→ RULED 2026-08-15 (owner): OVERLAY-WRITABLE `review_after`, as an authorized vault-local carry**,
  on the `adoption_first_instance:` precedent — the one field the divergence diff already excludes
  (`vlt-lint/references/checks.md:41`). This makes A7-5 **the seam group's first instance** under the
  framing ruling above, and the ruling is therefore load-bearing on A7-8: whatever mechanism carries
  an overlay-writable base field here is the same mechanism a baseline-exempt local convention will
  want. The brief must state the general form, not a `review_after` special case.
  **Two things this ruling does NOT do, recorded so no brief assumes otherwise:**
  1. **It does not beat the clock.** The three `review_after: 2026-08-17` dates expire in two days;
     no Arc-7 build ships by then. Every 0.9.1 install will report `deferral_expired` on
     `frontmatter@5`, `spec@2` and `wiki-consolidation@1` in the interim, and under this ruling that
     report is *correct* — the vault now has a legal move, it just doesn't have it yet.
     **Interim posture RULED 2026-08-15 (owner): LET THE FINDING STAND.** No date-only patch release,
     no rider on B7-1. The `deferral_expired` findings that appear on 2026-08-17 are true statements
     about a real gap, and suppressing them ahead of the fix would be the module telling a vault a
     comfortable thing — the precise failure this arc's Strand 3 is prosecuting. B7-3 sets the dates
     when it sets everything else.
  2. **It does not perform the review.** An overlay-writable field gives a vault somewhere to record
     a review's outcome; who reviews a module-owned deferral, and on what cadence, is untouched. The
     filing's field data on the three conventions (`wiki-consolidation@1` expiring on a clean record,
     `spec@2` honest-zero, `frontmatter@5` half-unevaluable per the count-since-N ruling above) is
     carried for whoever does it.
- **B7-8 — A7-6's forward-looking finding:** a mechanical `spec_notification_missing` keyed on the spec path
  would score vlt-core's one notified bump (relayed against the **handoff** path) as un-notified —
  *"a false positive on the exact history the check is being built to measure."* Whoever builds that
  deferred check needs this. — *(B7-8 carries the warning to whoever builds the deferred check; the check itself is not Arc-7 scope.)*
- **B7-3/B7-4 — A7-8's suggested shape, carried unresolved:** a sanctioned **baseline-exempt local convention**,
  with the filing's two mandatory properties — *(a)* exists without a stock counterpart, *(b)* visible
  to the split tripwire as a convention in its own right — and its bar: *"a landing zone that is
  merely silent would reproduce today's outcome with better manners."* — *(B7-3 rules the declaration form, B7-4 the mechanism; the two-property bar binds both.)*
- **B7-6 — A7-9, two closes carried unranked:** *(1)* a normalization clause (strip brackets and `.md` before
  any `sources:` comparison) or *(2)* convert both schemas together. Plus the separable carve-out rule
  for the contract's overlay section (*an overlay may occupy a base carve-out where the base names it
  and the overlay names the exact schema and scopes narrowly*), which is *"of general use, independent
  of whether the `sources:` change ships."* — *(B7-6's brief rules the two closes; the carve-out rule is severable and lands in the contract regardless.)*
  **→ AMENDED 2026-08-15 by post-ideation amendment A2** — B7-6's decline latitude covers the
  `sources:` **form** and A7-10's template only, never rule 4's traverse-vs-verify split, which B7-3
  ships irreversibly. See *Post-ideation amendments*.
- **B7-6 — A7-10's generalizable rule**, which survives even if A7-9 is declined: *where a template's field
  has a form the convention constrains, the template should show the form.* — *(B7-6's brief; survives even if A7-9's form change is declined at brief time.)*
- **B7-5 — A7-11:** the `shape` facet (`handoff`/`ask`/`answer`) and `ref` key as proposed, with the two
  properties the filing asks be kept (an `answer` reusing its `ask`'s `ref` does not collide;
  backward-compatible with no backfill), the batched-`ask` widening, and the receiver-side check
  (*every relay pointer resolves a key*). Second site any key change must touch:
  `vlt-dispatch/SKILL.md:22`. — *(B7-5's brief; capture's grounding already found the relay facet the shape most consistent with shipped design, which is a finding, not a ruling.)*
- **B7-5 — A7-12:** the address rule and its three guards (binds every `kind`; self-addressed work is not a
  relay; migration is one-home), the **limit paragraph** the filing asks be taken with the rule
  (*relay buys an address and a drain, not execution*), and the **independent, severable finding**
  that `{backlog}` is the only unbounded read in the operating contract's Beat 2 orient
  (`vault-operating-contract.md:169`). — *(B7-5's brief; the Beat-2 bound is severable and survives even if the address rule is declined.)*
- **B7-7 — A7-13, three options verbatim:** *(1)* a user-ruled verdict as a legal verdict type for a gated
  kind, with a required companion field recording that the panel was not fielded and why; *(2)* the
  mint refuses to proceed — Phase 2 hard-blocks and the planning doc parks; *(3)* a degraded panel,
  explicitly labelled single-context. Note the capture's finding that the park-and-resume machinery
  already exists (`vlt-mint/SKILL.md:57-66`, `:26`) and *"simply is not named as the response to an
  unavailable council"* — and that `:100`'s verdict vocabulary has **no facet for how the verdict was
  reached**. — *(B7-7's brief rules which of the three; the provenance facet is scoped in regardless,
  per the grouping table.)*

## Post-ideation amendments — RULED 2026-08-15 (owner)

The ideation session above closed 2026-08-15. A same-day **adversarial review of the closed plan**
(multi-persona round-table) found four faults in the *plan itself* — not in the capture, and not in
any ruling's substance — and produced three standing rules. The owner accepted the block and ruled
the one item the room left open (rule R3's home). Recorded here as the **single home**; the affected
slots above carry pointers, never restated mechanics. **No ruling above is reversed.** Every
amendment either adds a condition, splits one act into two, or fixes a tag.

**The finding the four faults share, stated once because every brief should carry it:** the arc's own
eight-build plan reproduces the three strands it was written to prosecute — a rule shipped ahead of
the mechanism that would honor it (**Strand 3**), a durability net that will silently narrow again
(**Strand 2**), and a true finding handed to a vault with no legal response (**Strand 1**). Each fault
came from a *locally correct* decision; the pathology sits at the joints between them, not in the
parts. That is why the repairs below are conditions and distinctions rather than a re-cut.

**A1. The `frontmatter@6` lockout gains a named reopen condition.** The one-coordinated-bump ruling
stands (build-16 precedent, one walk, one bipartite verification). What it *forbade* does not: *"no
later Arc-7 build may bump `frontmatter` again … either rides it or waits for Arc 8."* B7-4, B7-5 and
B7-6 are **briefed after B7-3 ships**, and briefs are where the design happens — so the rule as
written requires the arc's largest design to be fully anticipated by a build that precedes it. It
already bites: the authorized-vault-local-carry ruling names the generalization as *"a declaration the
base file carries about itself"*, which **is a new field in convention frontmatter**, i.e. a
`frontmatter` rule change B7-4 cannot request. **→ AMENDED: one bump, one consumer walk, and one
authorized amendment path.** A mechanism brief that demonstrates it needs a base rule or field
**reopens the `frontmatter@6` build** (re-cut before it ships, or a coordinated 6→7 with a full walk if
it has shipped) rather than deferring the mechanism to Arc 8. **→ AMENDED 2026-08-15 by A6 (below):
reopening after ship is a `frontmatter` 6→7 version bump with a full six-consumer walk and bipartite
verification — a mechanical, checkable state, NOT a "recorded event with a stated reason."** The
earlier wording was a prose promise about an act, unverifiable after the fact — the exact shape the
handshake ruling above already rejected when it threw out *"re-acking requires inspecting the asset."*
Making the reopen a bump also prices it correctly: a brief will not reach for it casually. This
applies the arc's own doctrine to its own plan: B7-3 is
inherently a *list* of anticipated rule changes, and *a net that must carry a list carries a shrink
check as well* — the reopen condition is that check.

**A2. A7-9 → A7-10 was ruled in two builds, and one direction is irreversible.** The capture marks the
dependency **binding** (*"they must be ruled together"*; A7-10 *"is moot and should be archived with
it"* if A7-9 is declined). The grouping puts A7-9's **rule** (rule 4's traverse-vs-verify split) in
B7-3 and its **form change** plus A7-10 in B7-6, whose brief *"rules the two closes"* — so B7-6 can
decline a form whose governing rule B7-3 has already shipped inside a version bump. **→ AMENDED:
B7-6's decline latitude is scoped to the `sources:` **form** and to A7-10's template change only. It
may not decline, narrow, or contradict rule 4's traverse-vs-verify split, which is B7-3's to ship and
B7-3's alone to revisit — via A1's reopen condition if it comes to that.** If B7-6's brief concludes
the form should not ship, it says so **and** states what rule 4's split then means with no form
behind it; that statement is R1's interim posture for this pair.

**A3. The A4-4 (5) inherited debt gets a mandated check *kind*, which is what actually failed.** The
disposition names it *"its own scope item, not a rider"* — the right instinct, and it does not create
capacity in B7-6 (the arc's second-largest build). But the mechanism of three arcs of loss is not
scope: it is that **only ship-verifiable checks gate arc closeout**, and the disposition mandates *an*
acceptance check without naming its kind. A field-contingent check can fail while the arc closes
around it — which is precisely the observed history. **→ AMENDED: B7-6's brief must give A4-4 (5) a
check tagged `ship-verifiable`, and that check is mandatory to the arc gate. If the clause cannot be
stated ship-verifiably, that impossibility is itself the finding** — the brief records it explicitly
and the debt is escalated rather than carried a fifth arc. **Optional, owner's call at brief time:**
move the item to **B7-7**, which floats and is small. The tag is the load-bearing half; the move is
cheap insurance.

**A4. B7-8's audit is split — sizing before B7-3, fixing in B7-8.** The count-since-N ruling is
*"PRINCIPLE NOW, SIZING BY AUDIT"*, marked **overturnable if the sweep shows a class of one**; the
sweep is pinned to B7-8, last, behind the build already flagged as most likely to slip. Two
consequences the pin did not intend: (1) B7-3 applies the principle to `frontmatter@5` **before** the
class is sized, inside the bump that (pre-A1) could not be reopened — so the overturn clause was
structurally unexecutable; (2) an unsized sweep parked last is the same shape as Arc 5's build-20
sized-by-assumption failure, the counter-lesson the ruling itself cites. **→ AMENDED: `sizing` and
`fixing` are two acts.** The **count** — grep the shipped conventions for both classes (count-since-N
metrics; prose asserting a permanent property a frontmatter field can invalidate) — is a read-only
sweep that depends on **nothing** in this arc and **runs before B7-3 is briefed**, so the principle
ships knowing whether it is a doctrine or a fix. The **fixes** stay in B7-8 against the arc's finished
state, which is what the pin's stated justification (*"benefits from watching B7-1..B7-7's own
verification passes"*) actually argued for. The pin's reasoning only ever covered the fixing half.

**Three standing rules, so the plan cannot repeat the strands.** Each has text and a home; R1 and R2
land in Arc 7, R3 is declared here and built in Arc 8.

- **R1 — against Strand 3 (rule ahead of mechanism).** *A build that ships a rule whose mechanism
  lands in a later build must state the **interim posture** in the same build: what a vault may
  legally do in the window, and whether findings generated in the window are correct.* **Home:**
  `build-brief` (a required brief section). **Binds immediately on B7-3**, and it also closes the gap
  the A7-5 interim-posture ruling left: *let the finding stand* tells the **factory** what to do and
  the field nothing. A7-5's fourth carried candidate — *state in the declaration that a shipped
  deferral's expiry is reviewed upstream and a vault's only move is to file* — was read as an
  alternative to the overlay-writable field. **It is not an alternative; it is that ruling's missing
  interim posture**, and B7-3 ships it as such. Without it, every 0.9.1 vault meets a true
  `deferral_expired` finding whose only available door is the base edit the module then has to
  reconcile — manufacturing the divergences B7-3 exists to accept.
- **R2 — against Strand 2 (nets that narrow).** *Any build that adds or changes a release-gate check
  extends the harness fixture in the same build.* **Mechanical, not prose**, per the structural
  doctrine: the harness carries a **case-count shrink check**, and **a gate check with no fixture case
  is itself a lint failure**. **Home:** `tools/package-lint.py` + `build-brief`'s verification section.
  **Wired in B7-1** — already open, already about the fixture, ships first. Without it the arc's own
  later builds (B7-2's manifest change, B7-6's handshake-node check) leave the fixture stale by
  closeout, and Arc 8's first filing is A7-1 again.
  **→ AMENDED 2026-08-15 by A7 (below): R2 ships its own legal response inline.** R2 introduces a
  finding class, and R3 forbids shipping a finding class with no stated legal response — so R2 as
  first written would have violated R3 inside the arc that declares R3. The response is trivial and
  must be stated at the check: *the legal response to a gate check with no fixture case is to add the
  fixture case, in the build that added the check.* **R2 is therefore R3's worked example rather than
  R3's first violation** — and the near-miss is recorded, not smoothed over, because it is the
  evidence for the objection R3 carries: a declared rule whose posture nobody writes is precisely the
  failure that objection predicted, and it nearly happened one turn after the declaration.
- **R3 — against Strand 1 (findings with no landing zone).** *No finding class ships without a stated
  legal response — every check names what a vault may legally do about it.* **Home:** a per-check
  field in `vlt-lint/references/checks.md`. **DECLARED in Arc 7, BUILT in Arc 8** — the retrofit
  touches every existing check and is not Arc-7 scope. **→ RULED 2026-08-15 (owner): the declaration
  stays in this roadmap rather than waiting for Arc 8's capture.** The owner ruled with the ladder
  argument: a `declared`-stage rule with a named home and a deferred build is a legal, shipped module
  posture, not a promise in the air. The contrary position is on record and is not frivolous —
  declaring a rule you cannot yet enforce is the disease this arc prosecutes — which is exactly why
  **R3 is itself subject to R1**: its Arc-8 build must carry an interim posture for the window, and
  **if that posture cannot be written, R3 is not ready and the declaration is withdrawn.** The rule
  tests its own author.

### Second amendment pass — A5–A8, RULED 2026-08-15 (owner)

A second adversarial pass was run over the amended plan, on the ground that **A1–A4 and R1–R3 had
been reviewed by nobody but the room that wrote them** — which is A7-13's own provenance gap (a
verdict carrying no facet for how it was reached) applied to this section. Four repairs; three of them
are R1 applications, which is itself evidence R1 was the right rule.

**A5. A finding this session found, agreed, and then lost — recorded so it cannot happen a third
time.** In the first pass the room confirmed a contradiction *inside B7-5's own scope*: the build
ships *"backward-compatible with **no backfill** — an un-annotated header reads as `handoff`"*
(capture `:610`) **and** the receiver-side check *"every relay pointer resolves a key — a path that
exists on disk, or a `ref` present in the header"* (capture `:615`). A7-11 reports **13 of 40 existing
pointers carry no path**. Those 13 default to `handoff`, `handoff` requires a path, and they have
none — **so the receiver check fires on all thirteen the day it ships.** Both halves are recorded in
this roadmap (`:610`, `:615`, and B7-5's brief-time designation); **the conflict between them was
not**, until now. **→ RULED: this is a binding brief-time conflict for B7-5**, to be resolved in the
brief and not discovered at acceptance — either the receiver check grandfathers un-annotated pointers,
or `handoff` tolerates a missing path as a legacy form, or the no-backfill property is given up. The
brief rules which; **it may not ship both properties unreconciled.**
**Recorded with its cause, because the cause is the arc's own subject:** the finding was raised,
agreed, and then lost when the session moved on to its next three items — *a finding riding along in a
larger scope and losing to the host* — which is the exact failure amendment A3 exists to correct, and
it happened **hours after A3 was written**. The transferable lesson is not about relay: **a consensus
item with no line in a file is not a consensus item.**

**A6. A1's reopen condition becomes mechanical.** Recorded at A1 above rather than restated here, per
single-home. In short: a post-ship reopen is a `frontmatter` **6→7 bump with a full consumer walk**,
not a "recorded event with a stated reason" — the original wording was an unverifiable prose promise
about an act, the shape the pre-ideation handshake ruling had already rejected.

**A7. R2 ships its own legal response inline.** Recorded at R2 above. R2 would otherwise have
introduced a finding class in Arc 7 that R3 — declared in the same section — forbids. It is now R3's
worked example instead of R3's first violation.

**A8. B7-5's second guard is scoped to the addressee model in force at ship time.** A7-12's guard 2 —
*self-addressed work is not a relay* — is written against today's single-user model. **B7-4 gives
dispatch a designed roster, precedes B7-5 in ship order, does not gate it, and is the build flagged
most likely to slip.** If B7-5 ships first and a roster arrives afterwards, *self-addressed* becomes
ambiguous in the multi-user case (same partner, different human): the guard as written reads yes, any
sane multi-user reading says no. **→ RULED (an R1 application): B7-5's brief states the guard's scope
against the addressee model in force at its ship time, and names explicitly what changes if B7-4
later widens that model.** Cheap now; a silent behavior change later.

## Live-acceptance ledger

*(populated per build by `build-brief` §9, tagged **ship-verifiable** or **field-contingent**;
only ship-verifiable checks gate arc closeout.)*

- [x] **build-B7-1 (harness-baseline, briefed 2026-08-15):** all five checks
  **[ship-verifiable]**, none field-contingent (factory-side build; nothing ships into or waits
  on a vault). (1) harness baseline restored and load-bearing — `uv run
  tools/test-package-lint.py` all cases green (expected 18/18), case 1 asserting whole-run
  exit 0 (PASS A/B/C/E, SKIPPED D) and case 9 exit 0 with D PASS; dischargeable at rest,
  re-confirmed at the arc's release gate. (2) R2's E4 harness-coverage check live at the gate —
  real-repo `package-lint` passes with E4 active, and the recorded mutation probe (an uncovered
  `check_`-named function turns group E red) shows it could have failed. (3) case-count shrink
  check live — recorded probe shows any count below `CASE_FLOOR` fails the harness loudly.
  (4) R2 observed binding in-arc — the first later Arc-7 build that adds/changes a gate check
  (B7-6's handshake-node check is already ruled; B7-2 if its net work touches the gate) ships
  its fixture case in the same build, E4 red-then-green recorded in that build's verification;
  bounded by the arc's own ruled builds. (5) the arc's pre-tag `--expect-version` gate run
  exits 0 with E4 in the run, PASS line in the release commit message.
  **DISCHARGED 2026-08-17** — (1) `uv run tools/test-package-lint.py` → `21/21 cases green`
  (cases 1 and 9 PASS; the 18-case expectation was raised in-arc by B7-2's cases 19/20 and
  B7-6's case 21). (2)(3) `tools/test-package-lint.py:229` `CASE_FLOOR = 21`, shrink guard at
  `:494`; `package-lint` group E PASS. (4) R2 observed binding twice in-arc — B7-2 shipped
  cases 19/20, B7-6 shipped case 21, each in the build that changed the gate. (5) `uv run
  tools/package-lint.py --expect-version 0.10.0` → exit 0, `A/B/C/E PASS, D PASS`; PASS line
  recorded in release commit `b117d81`.

- [ ] **build-B7-2 (durability-nets, briefed 2026-08-15):** four ship-verifiable checks, one
  field-contingent. (1) **[ship-verifiable]** durability-net gate check live and proven
  fallible — real-repo `package-lint` A/B/C/E passes with `check_durability_nets`
  inventoried; `test-package-lint` 20/20, `CASE_FLOOR` 20; recorded mutation probes show E4
  red without the covering cases and cases 19/20 each able to fail (this discharges B7-1
  check (4)'s "first later build" instance — R2 observed binding in-arc). (2)
  **[ship-verifiable]** merge-config preservation at rest — the A7-2 reproduction table
  inverted: absent-from-answers ⇒ block preserved + named in `module_keys_preserved`;
  mis-nested payload ⇒ non-destructive; zombie key ⇒ removed and named in
  `module_keys_removed`; fresh install ⇒ `module.yaml` defaults materialized
  (`module_keys_defaulted`). (3) **[ship-verifiable — next ordinary vlt-core upgrade]**
  post-upgrade `_bmad/config.yaml` still carries the full `vault_structure` map including
  its vault-local override key, with the run's result JSON showing no unreported removal;
  bounded — the 0.10.0 upgrade happens anyway (vlt-core, owner-run, evidence via pasted
  result JSON + ledger entry). (4) **[ship-verifiable — next ordinary upgrade, either
  vault]** the manifest re-written with structural scope: entries rise from the
  enumeration-era 40 to the full walk (all 8 `references/*.md`, all `scripts/*.py` incl.
  `verify-skill-manifest.py`, the workflows, the installed vitals hook), shrink report lists
  removals only for legitimately de-shipped files, the work vault's hand-widened 55-entry
  set strictly contained; provenance legible in the ledger note — restored (`references/`,
  regressed v0.9.0) vs new (`scripts/` since v0.3.0; hook since v0.9.0's enforcement kit).
  (5) **[field-contingent]** A7-2's attached lead — whether vlt-core's 0.8.0→0.9.0 ledger
  entry evidences a prior silent strip, graded by reading vlt-core's upgrade ledger/git
  history at acceptance; producing vault: **vlt-core only** (owner-run; the factory cannot
  read it — evidence arrives as the owner's paste); changes the field-loss narrative, never
  the fix; if unread by closeout it goes to the watch register, not the gate.
  **Upgrade-side DISCHARGED 2026-08-17; STILL-OPEN: the work-vault containment sub-clause of
  check (4).** (1) harness `21/21`, `CASE_FLOOR = 21` (raised past the check's 20/20 by B7-6's
  case 21); `package-lint` A/B/C/E PASS with `check_durability_nets` inventoried. (2) harness
  case 19 ("merge-config swapped for a rebuild-from-answers stub → C fails, preservation")
  PASS — the preservation table is gate-enforced, not merely asserted. (3) vlt-core
  `_agent/upgrade-ledger.md`, 0.9.1→0.10.0 entry (2026-08-15 19:23): post-provision diff of
  `_bmad/config.yaml` shows exactly one changed line (`version:`), `vault_structure` preserved
  whole **including the local `dog_training_root:` key**, `module_keys_removed: []` — the
  0.9.1 standing note closed. (4) vlt-core manifest rewritten by `verify-skill-manifest.py
  --write` to **60 entries**: all 8 `references/*.md`, all 4 `scripts/*.py` (incl.
  `verify-skill-manifest.py`), the 3 workflows + their asset copies, and
  `.claude/hooks/vlt-vitals.py`; **removed: none**. **STILL-OPEN:** the work vault's
  hand-widened 55-entry set being strictly contained — that vault has not upgraded and is not
  readable from the factory. Trigger: owner runs `vlt-upgrade` on the work-machine vault.
  (5) **DISCHARGED (negative)** — vlt-core's 0.8.0→0.9.0 ledger entry records "config bumped
  to 0.9.0 with `tripwires:` + `lint_reports:` structure keys (local `dog_training_root:`
  kept)": `vault_structure` survived that upgrade intact, so no prior silent strip is
  evidenced. The 0.9.1 run was the defect's first instance, not merely its discovery.
  **RELEASED AS A STANDING WATCH at arc close 2026-08-17 (owner batch ruling).** Recorded here
  rather than ticked — the work-vault containment sub-clause was never exercised, it was
  released. The parent check is tagged *either vault* and vlt-core discharged it; the residue
  needs the work-machine vault, which the factory cannot read. Carries forward past Arc 7.

- [x] **build-B7-3 (frontmatter-6, briefed 2026-08-15):** four ship-verifiable checks, one
  field-contingent — per the ruling, the checks are about the **handshake**, not behavior.
  (1) **[ship-verifiable]** `frontmatter@6` handshake closed and bipartite-consistent —
  `package-lint` Group E passes at rest and inside the arc's pre-tag `--expect-version` run:
  six consumers listed, six acks at @6, zero stray @5 pins in `skills/`. (2)
  **[ship-verifiable]** rules-with-postures shipped — the @6 base carries all four rule
  changes (rule 4 traverse-vs-verify split; vault-writable `review_after`; local-convention
  two-property rule; address rule + three guards + limit paragraph) and one R1
  interim-posture sentence per rule; readable at rest, re-confirmed on the next ordinary
  upgrade delivering the pristine base. (3) **[ship-verifiable — next ordinary upgrade,
  either vault]** deferral clock reset holds — post-upgrade lint reports zero
  `deferral_expired` across `frontmatter@6`/`spec@2`/`wiki-consolidation@1` (per-convention
  dates 2026-11-15 / 2026-10-15 / 2026-12-15), and the pre-upgrade window's findings were
  never suppressed (the lint-report trail still shows them — they were true). (4)
  **[ship-verifiable]** the class-1 fix — `frontmatter.md:17`'s threshold self-baselined and
  evaluable from vault-readable state alone; dischargeable at rest; the overturn record rides
  this check (condition met, conservative path taken, doctrine question presented to the
  owner at the v0.10.0 release as part of discharge). (5) **[field-contingent]** vlt-core's
  standing `frontmatter` base divergence resolves at its 0.10.0 upgrade — clears where B7-3
  adopted the previewed edits, re-flags correctly where the module's ruled text differs from
  vlt-core's local wording; producing vault: **vlt-core only** (owner-run; the factory cannot
  read it — evidence arrives as the owner's pasted upgrade report/lint findings + ledger
  entry); if unread by closeout it goes to the watch register, not the gate.
  **DISCHARGED 2026-08-17.** (1) the @6 handshake closed at ship and was **superseded in-arc**
  by `frontmatter@7` (B7-6); `package-lint` group E PASS confirms the successor
  bipartite-consistent (7 consumers incl. `vlt-lint-full.js`, zero stray `@5`/`@6` pins).
  (2) the four rule changes + R1 interim postures landed per the B7-3 brief's F1a–F1f record;
  the postures were retired on schedule by B7-4/B7-6, which is the design, not drift.
  (3) vlt-core lint `_agent/lint-reports/2026-08-16-1118-lint.md` — `deferral_expired: []`,
  with the three `review_after: 2026-08-17` dates refreshed by the 0.10.0 upgrade to
  frontmatter 2026-11-15 / spec 2026-10-15 / wiki-consolidation 2026-12-15; **nothing was
  suppressed** — the pre-upgrade `2026-08-14-1336-lint.md:19` reported them honestly as
  "3 days out, not yet due", and its note at `:93` named the expiry. (4) the class-1 fix is
  live: `frontmatter.md:17` reads "2 prose/behavior drift findings since 2026-08-15, or the
  3rd convention minted beyond the 9 shipped at that baseline" — self-baselined and evaluable
  from vault-readable state alone. **Overturn record:** condition met, conservative path
  taken, doctrine question **presented to the owner 2026-08-17 at discharge — ruled: no
  doctrine change, the conservative path stands.** (5) vlt-core's `frontmatter` base
  divergence resolved as designed — live v6 (the authorized 2026-08-14 address-rule mint,
  `95b51c8`) refreshed to shipped v7, which subsumes it; the only `convention_base_divergence`
  in the post-upgrade lint is a *new* post-upgrade authorized edit (the vlt-sweep
  consumers-roster addition), not the address rule.

- [ ] **build-B7-4 (the-seam, briefed 2026-08-15):** three ship-verifiable checks, two
  field-contingent. ⚠ Brief carries an owner-review flag (matrix reconstruction + two
  reserved-question rulings — dispositions 1/6/7) to be discharged at the v0.10.0 release.
  (1) **[ship-verifiable]** seam coherence at rest — the vault-writable member set
  single-homed (only `frontmatter.md` enumerates; `checks.md:41` + `vlt-upgrade` Step-1/2
  point), both interim trailers replaced with no rule-text change (`frontmatter` `version: 7`
  holds — the A1 reopen NOT invoked, no re-ack, zero stray pins), `package-lint` A/B/C/E green
  at rest and in the pre-tag run including C6 after the rule-card sha re-derive
  (red-then-green probe recorded); harness 21/21, `CASE_FLOOR` 21 (R2 not triggered). (2)
  **[ship-verifiable]** the mechanism desk-checks of record, each able to fail — the
  divergence-exclusion pair (declared field excluded / undeclared flags), the carry-forward
  table (vault-kept / shipped-lands / both-moved collision surfaced / adoption-stamp behavior
  reproduced), the local-convention truth table (minted → inventory line + no coherence false
  positive; unminted → `baseline_missing`), and the dispatch-profile cases (absent →
  byte-identical default; malformed → loud refusal; roster → `(for: …)` facet with the
  pair-inclusive `(key, to-slug, principal)` idempotency key; guard 2 pair-equality passing
  same-partner/different-principal, refusing same-pair). (3) **[ship-verifiable — next
  ordinary upgrade, either vault]** delivery + the generalized carry live on real state —
  installed surfaces carry the seam edits (grep-checkable); vlt-core's stamped
  `adoption_first_instance:` survives the 0.10.0 refresh via the generalized rule, and the
  post-flight report renders `local_conventions_intact` + `vault_writable_collisions` (both
  may honestly read empty); bounded — the upgrade happens anyway (owner-run; evidence via
  pasted report + ledger entry). (4) **[field-contingent]** the first sanctioned local
  convention — minted, no `baseline_missing`, no coherence false positive, counted by the
  split tripwire, honored by a consumer; producing vault: **vlt-core only** (owner-run; the
  factory cannot read it — evidence by owner paste; named candidate: re-homing vlt-core's
  A7-8 prose-line rule from the unrelated overlay into a minted local convention); if unread
  by closeout it goes to the watch register, not the gate. (5) **[field-contingent]** the
  first roster — a multi-principal vault declares `_agent/dispatch-profile.md` and routes a
  cross-principal relay (faceted, pair-keyed, guard 2 correct), the A7-4 workaround mint
  retiring at the vault's pace; producing vault: **the work-machine team vault only** (the
  filing's origin; the factory cannot read it; vlt-core is single-principal and structurally
  cannot produce this event) — evidence by owner paste; if unread by closeout it goes to the
  watch register, not the gate.
  **Ship-verifiable half DISCHARGED 2026-08-17; STILL-OPEN: both field-contingent tails
  (4) and (5), plus the brief's ⚠ owner-review flag.** (1) seam coherent at rest — the
  vault-writable member set is single-homed: only
  `governance/_meta/conventions/frontmatter.md` (*Vault-writable declared fields*) enumerates
  it; `vlt-lint/references/checks.md:41` and `vlt-upgrade/SKILL.md` point and carry no list.
  `frontmatter` `version: 7` holds (A1 reopen not invoked); `package-lint` A/B/C/E PASS;
  harness `21/21`, `CASE_FLOOR = 21`. (2) the four mechanism desk-checks are of record in the
  B7-4 brief (F1–F10, 16 shipped files, "landed as briefed"). (3) **delivery + the generalized
  carry proven live** — vlt-core 0.10.0 ledger entry: both stamps (`spec.md` 2026-06-13,
  `decision-log.md` 2026-07-30) carried into the refreshed bases under the frontmatter@7
  member set, `review_after:` taking incoming shipped values where the vault never wrote it,
  and **both new report keys rendered honestly empty** — `local_conventions_intact: none`,
  `vault_writable_collisions: none`. Confirmed on disk: installed `_meta/conventions/spec.md`
  carries `adoption_first_instance: 2026-06-13`, `decision-log.md` carries `2026-07-30`.
  **STILL-OPEN (4)** — the first sanctioned local convention has not been minted: the
  2026-08-16 lint reports `local_conventions: "0 local conventions — all 9 {conventions}
  files have stock baselines"`. Trigger: owner mints vlt-core's A7-8 prose-line rule (the
  named candidate) out of the overlay into a local convention. **STILL-OPEN (5)** — no
  roster: the lint reports `dispatch_profile_invalid: []` with no `_agent/dispatch-profile.md`
  (single-principal default). Trigger: the work-machine team vault declares a profile;
  structurally unproducible in vlt-core. **⚠ The brief's design-reconstruction owner-review
  flag (dispositions 1, 6/7, 8) remains undischarged** — it was to be discharged at the
  v0.10.0 release and was not; it carries into closeout.
  **RELEASED AS STANDING WATCHES at arc close 2026-08-17 (owner batch ruling).** Recorded here
  rather than ticked — tails (4) and (5) were never exercised, they were released. (4) waits on
  an owner mint; (5) is structurally unproducible in vlt-core and needs the work-machine team
  vault. Both carry forward past Arc 7. **The ⚠ owner-review flag also carries forward to Arc 8
  as an inherited owner-review debt** (owner ruling, this close) — the A7-4 decision matrix was
  unrecoverable and the brief's reconstruction stands unreviewed.

- [x] **build-B7-5 (relay-and-address, briefed 2026-08-15):** four ship-verifiable checks, one
  field-contingent. (1) **[ship-verifiable]** shape facet coherent at rest — relay.md carries
  the three shapes (`handoff`/`ask`/`answer`) with per-shape key requirements and the
  `(handoff-path | ref, to-slug)` key as single home; router `:14`/`:22`/`:54`, ledger check,
  and help row agree by pointer; `package-lint` A/B/C/E green (C7 budget held), Group E
  confirming `frontmatter@6` untouched and bipartite-consistent. (2) **[ship-verifiable]** the
  A5 reconciliation shipped — un-annotated-with-path reads `handoff`, un-annotated-pathless is
  legacy (exempt, rendered as ledger's denominated count line, never findings); findings only
  for shape-annotated key failures, legal response stated at the check; the brief's
  temp-fixture walkthrough (cases a–e, one finding) is the could-have-failed probe of record.
  (3) **[ship-verifiable]** single-home landed — the address-aware reflex lives only in the
  operating contract with four partner-side pointers + two op-skill routing pointers; the
  Beat-2 `{backlog}` bound (open count + last 5) identical at contract, three partner skills,
  and template; frontmatter.md:222's interim trailer replaced with no rule-text change
  (`version: 6` holds, no re-ack). (4) **[ship-verifiable — next ordinary vlt-core upgrade
  (0.10.0, owner-run)]** ruled text supersedes vlt-core's previewed local edits cleanly —
  post-upgrade `ledger` run reports pre-shape pathless pointers as the denominated legacy line
  (no false findings on legacy traffic) and locally-written keyed `ask`/`answer` pointers
  resolve; bounded — the upgrade happens anyway; evidence via owner-pasted ledger output +
  upgrade ledger entry (the factory cannot read vlt-core). (5) **[field-contingent]** the drain
  the mechanism promises — newly noticed addressed gaps travel as keyed `ask` relays rather
  than accumulating as addressed backlog items, measured against the filing baselines (relay
  split 40/27/13; backlog 85→62, `knowledge-gap` 33→10); producing vault: **vlt-core only**
  (owner-run; evidence by owner paste); graded per the limit paragraph (an undrained-but-keyed
  slice on a rarely-summoned partner is the rail working); if unread by closeout it goes to the
  watch register, not the gate.
  **FULLY DISCHARGED — four checks 2026-08-17, check (4) later the same day on the owner's
  `vlt-dispatch ledger` run. This was the arc's last open ship-verifiable check; closeout is
  now unblocked.** (1) shape facet coherent at rest — `package-lint` A/B/C/E PASS, group E
  bipartite-consistent; `vlt-dispatch/references/ledger.md:26` carries the legacy line as its
  single home. (2) the A5 reconciliation and its temp-fixture walkthrough (cases a–e, one
  finding) are of record in the B7-5 brief. (3) single-home landed — the Beat-2 `{backlog}`
  bound appears identically at `vault-operating-contract.md:173` plus the three program
  partners (`vlt-agent-librarian`, `vlt-agent-researcher`, `vlt-agent-creative`, each `:25`)
  and `vlt-mint/assets/partner-agent-template.md:40`. **STILL-OPEN (4)** — **no post-0.10.0
  `vlt-dispatch ledger` run has occurred.** The upgrade landed 2026-08-15 19:23 and a full
  lint ran 2026-08-16, but no ledger run: the only `pathless`/`pre-shape` mentions in vlt-core
  are pre-upgrade (`_agent/log.md:368`, `:370`, both 2026-08-14). The denominated legacy line
  is therefore unobserved on real traffic. Trigger: owner runs `vlt-dispatch ledger` on
  vlt-core — a single command, no new upgrade needed. **(4) DISCHARGED 2026-08-17b** — the
  owner ran `vlt-dispatch ledger` on vlt-core and pasted the output. The **denominated legacy
  line rendered in the shipped form** — "18 legacy unkeyed pointers (pre-shape) — exempt by
  design, no action" — and **produced zero findings on legacy traffic**, which is the A5
  reconciliation's whole promise. Keyed `ask`/`answer` pointers resolve: all 7 pointer-
  integrity findings are `handoff`-shape key failures, none ask/answer, and the three
  2026-08-16 asks (`hiring-pipeline-warning-narrowed`, `watermark-detection-resume-semantics`,
  the batched 2-ref) sit clean on the board. Board accuracy independently verified — the run's
  "14 open across the record" matches a fresh `grep -c '^- \[ \]' _agent/dispatch.md` → 14
  exactly. The wires and vitals rendered denominated ("1 of 2", "0 of 2"-idiom, `expired_pages
  0 (280 pages scanned)`), including the tripped `relay-overdue` row. *Caveat recorded, not
  charged against the check:* the legacy denominator could not be reproduced from the factory
  — a block-header-scope grep yields 37, a per-pointer-line grep yields 2, bracketing the
  run's 18; the rule "un-annotated **pathless** pointers" is ambiguous between block-header
  and per-pointer scope, and about whether a payload `[[wikilink]]` counts as a path. Arc-8
  capture candidate (ledger.md, *The legacy line*). (5) **DISCHARGED** — the drain is
  visible in the field. Post-upgrade relays carry the shape facet live:
  `_agent/dispatch.md:306` `(answer, ref: nfl-roster…)`, `:312` `(ask, ref: penny-liver…)`,
  `:315`–`:330` six keyed `(handoff, ref: …)` blocks, and three fresh 2026-08-16 `ask` relays
  (`:339` `hiring…`, `:342` `watermark…`, `:345` batched, 2 refs). Against the filing
  baselines: `knowledge-gap` open backlog items stand at **10** — exactly the filing's
  post-triage figure, **held** across two days while newly-noticed gaps left as keyed asks
  (the 2026-08-16 lint relays `schottenheimer-2026-role` and `herron-2009-aggression-range` to
  the researcher rather than filing them). Total open backlog 65 vs the filing's 62; the +3
  are maintenance items, none `knowledge-gap`. Gaps travelled; they did not accumulate.

- [x] **build-B7-6 (overlay-contract, briefed 2026-08-15):** five ship-verifiable checks,
  one field-contingent (explicitly non-gating). (1) **[ship-verifiable]** `frontmatter@7`
  handshake closed and bipartite-consistent **including asset nodes** — Group E at rest and
  in the pre-tag run: six skill consumers @7, `vlt-lint-full.js` listed in
  `frontmatter`/`wiki-supersession`/`wiki-index` `consumers:` and acking via its
  `// depends_on` header line, `vlt-consult.js` + `vlt-review-council.js` carrying explicit
  `depends_on: []`, zero stray pins; recorded probes show E5 able to fail (stale asset ack,
  stripped header) and E4 red-then-green on E5's introduction (R2 observed binding — the
  B7-1 check (4) instance for this build); harness 21/21, `CASE_FLOOR` 21. (2)
  **[ship-verifiable]** fan-out merged-on-read live — the recorded with/without fixture
  pair: an overlay-compliant page contradicting its base survives a full sweep with no
  finding when overlay args are passed (A7-7's case, carried as filed), and is flagged plus
  a `coverage_caps` no-overlay-args message when they are not. (3) **[ship-verifiable —
  GATES THE ARC (amendment A3)]** the inherited **A4-4 clause (5)** debt discharges at
  rest: the loss-shape fixture reproduction of record — greedy clustering demonstrably
  splits the callout-marked pair, yet shipped `vlt-lint-full.js` at HEAD returns the pair
  in `entity_collisions` marked `(callout-seeded)` with
  `entity_scan_facts.seeded_pairs_checked ≥ 1`, negative run clean; fails by construction
  on the pre-B5-2 shape and fails again if the overlay edits regress the pass; on pass the
  carrier filing 160949 becomes archivable per arc-closeout Stage 5 (fourth arc). (4)
  **[ship-verifiable]** the `sources:` form shipped coherently — rule 4 carries form +
  normalization clause + coexistence posture (interim trailer gone), `vlt-ingest` template
  shows the form, `checks.md` legs 1/3 + the Gap-B scanner prompt apply the normalization
  by pointer; desk-check of record: a wikilink-form wiki entry and its bare-path research
  twin normalize equal (A7-9's case — `linkage_ripe` still excludes the absorbed note
  across mixed forms). (5) **[ship-verifiable — next ordinary upgrade, either vault]**
  delivery — installed workflows carry header acks + overlay plumbing, installed
  `frontmatter.md` is @7 with the form, installed `vlt-ingest`/`vlt-lint` carry the
  walk edits; grep-checkable, bounded. (6) **[field-contingent — NON-GATING, watch
  register by design]** the named instance: vlt-core's first full lint post-0.10.0, the
  standing "Which Jackson?" callout's pair surfaces `(callout-seeded)` live; producing
  vault: **vlt-core only** (owner-run, owner-pasted report); corroboration of check 3's
  property, deliberately not the debt's discharge; re-targets the next standing callout or
  lapses without prejudice.
  **DISCHARGED 2026-08-17 — including check (3), the arc gate, and with it the four-arc
  A4-4 clause (5) debt.** (1) `frontmatter@7` handshake closed **including asset nodes** —
  `package-lint` group E PASS at rest and in the pre-tag `--expect-version 0.10.0` run;
  harness case 21 ("asset ack goes stale → E fails, stale asset; E1 stays silent on the .js
  entry") PASS is E5's could-have-failed probe, and its introduction is the R2 in-arc binding
  instance for this build; `21/21`, `CASE_FLOOR = 21`. (2) the with/without overlay fixture
  pair is of record in the B7-6 brief (F3 plumbing, exercised again inside the F9 run).
  (3) **ARC GATE — DISCHARGED.** The F9 loss-shape reproduction was **executed against the
  shipped workflow at this build's HEAD** (i.e. after the F3 overlay edits, so it also proves
  they did not regress the pass) and recorded in the brief's `status:`. The mechanism is
  intact at HEAD and independently confirmed this run:
  `skills/vlt-setup/assets/workflows/vlt-lint-full.js:330-360` (the seed map + seeded pair
  pass), `:360` the `(callout-seeded)` provenance suffix, `:424`
  `entity_scan_facts.seeded_pairs_checked`. One sanctioned deviation of record: F9 ran via a
  node harness supplying the runtime seam (args as a JSON string, deterministic mock at the
  `agent()` LLM boundary reading the real fixture files — clustering, seeded pass, provenance
  merge, intake and report assembly all the real shipped JS), the Workflow-tool route being
  unavailable to that builder session. **Carrier filing `2026-07-25-160949` is now archivable
  per arc-closeout Stage 5 — fourth arc, debt closed.** (4) the `sources:` form ships
  coherently — `frontmatter.md` rule 4 carries form + normalization + coexistence posture
  (`:36`, `:98`, `:104`), interim trailer gone. (5) delivery confirmed on installed state:
  vlt-core `_meta/conventions/frontmatter.md` is `version: 7` with the form, and
  `.claude/workflows/vlt-lint-full.js` carries the callout-seeded plumbing (5 hits).
  (6) **LAPSED without prejudice — owner-ruled 2026-08-17.** The first post-0.10.0 full lint
  did run (`2026-08-16-1118-lint.md`, 144 pages / 23 clusters, seeded pass live), but reports
  `0 callout-seeded pairs — the prior Jackson pair was closed by the 2026-08-15 roster pass`:
  the named subject was resolved before the check could fire. Non-gating by design; check (3)
  already carries the property at rest.

- [ ] **build-B7-7 (council-fallback, briefed 2026-08-15):** four ship-verifiable checks, one
  field-contingent. (1) **[ship-verifiable]** `decision-log@2` handshake closed and
  bipartite-consistent — Group E at rest and in the pre-tag run: three consumers listed
  (vlt-mint, vlt-upgrade, vlt-lint), three acks at @2, zero stray @1 pins; `frontmatter@7`
  untouched; `vlt-review-council.js` byte-identical, `depends_on: []` header ack intact.
  (2) **[ship-verifiable]** the named fallback coherent at rest — recorded desk-check of the
  four environment cases (council fielded / unavailable-unattended → park /
  unavailable-attended → user-ruled / self-substitution → nameable as illegal from the shipped
  text alone), each resolving to exactly one named path across Step 2a, the Phase-2 exit gate,
  the planning-doc vocabulary, and the resume scan; cross-file greps agree on the path names
  and the parked state string. (3) **[ship-verifiable]** provenance single-homed and honestly
  enforced — the three-form vocabulary (`council` / `council-degraded` / `user-ruled` +
  required why) lives only in `decision-log.md`'s *Verdict provenance* section, `vlt-mint`
  points and never restates, and the convention's Enforcement section states the
  write-side-only posture (no new finding class shipped — the R3 declaration); grep-checkable.
  (4) **[ship-verifiable — next ordinary upgrade, either vault]** delivery — installed
  `decision-log.md` @2 with the provenance section, installed `vlt-mint` carrying the fallback
  branch, exit-gate clause, planning-doc vocabulary, and the @2 ack; grep-checkable, bounded.
  (5) **[field-contingent]** the facet and fallback observed on real gated mints — the first
  post-0.10.0 council-capable gated mint records `(council — lenses: …)` from the workflow's
  own return, and the first constrained-session gated mint either parks-and-resumes or records
  `(user-ruled — panel not fielded: <why>)`; nothing before 0.10.0 can produce either event and
  no upgrade forces a gated mint; producing vault: **vlt-core only** (owner-run; the factory
  cannot read it — evidence arrives as the owner's pasted decision-log entry / planning-doc
  lines; vlt-core's 2026-08-14 substituted entry is the pre-facet exemplar for legibility,
  context never gate); if unread by closeout it goes to the watch register, not the gate.
  **Ship-verifiable half DISCHARGED 2026-08-17; STILL-OPEN: the `(council — lenses: …)` leg
  of check (5).** (1) `decision-log@2` handshake closed — three consumers, three acks
  (`vlt-mint/SKILL.md`, `vlt-upgrade/SKILL.md`, `vlt-lint/SKILL.md`, all `decision-log@2`),
  `package-lint` group E PASS, zero stray `@1` pins; `frontmatter@7` untouched.
  (2) the four-environment desk-check is of record in the B7-7 brief ("all F-sites landed as
  briefed; no deliberate deviations"). (3) provenance single-homed — the three-form vocabulary
  appears in exactly two shipped files: `governance/_meta/conventions/decision-log.md:49-55`
  (*Verdict provenance (v2)*, the single home) and `vlt-mint/SKILL.md:99`, which names the
  forms as the workflow's return values in one pointer sentence and restates no rule.
  (4) delivery confirmed on installed state: vlt-core `_meta/conventions/decision-log.md` is
  `version: 2` with the *Verdict provenance (v2)* section; installed `vlt-mint/SKILL.md`
  carries the fallback branch (`:105` user-ruled attended-only) and the amended Phase-2 exit
  gate (`:107`). (5) **PARTIALLY DISCHARGED — owner ruled the substitution acceptable
  2026-08-17.** No council-gated mint has run since 0.10.0 (the only post-upgrade mint,
  `vlt-sweep` 2026-08-15, is recorded `council-none`), but the shipped
  `(user-ruled — panel not fielded: <why>)` form **fired live post-0.10.0** at
  `_agent/mint/decision-log.md:925` — the overlay Rule B retirement, an upgrade-ruling rather
  than a mint. Owner accepted the substitution for the user-ruled leg. **STILL-OPEN:** the
  `(council — lenses: …)` leg, requiring the workflow's own return on a council-fielded gated
  mint. Trigger: the next council-gated mint in vlt-core; no upgrade forces one.
  **RELEASED AS A STANDING WATCH at arc close 2026-08-17 (owner batch ruling).** Recorded here
  rather than ticked — the `(council — lenses: …)` leg was never exercised, it was released.
  Carries forward past Arc 7.

- [ ] **build-B7-8 (stale-prose-sweep, briefed 2026-08-15):** two ship-verifiable checks, one
  field-contingent. (1) **[ship-verifiable]** the sweep's fixes coherent at rest — `spec.md`
  conditional at both sites (`:14` comment + Enforcement paragraph agreeing; no permanent-form
  "cannot fire" assertion left in the shipped surface) with the `spec_notification_missing`
  path-warning design note present and `version: 2` unmoved; `vlt-setup`'s Confirm line points
  at §2a with no workflow enumeration; `vlt-upgrade`'s adoption vocabulary "created — N days"
  identical at `:105`/`:112` with the proxy stated; `package-lint` A/B/C/E green, Group E
  confirming `frontmatter@7`/`spec@2`/`decision-log@2` bipartite-consistent with zero stray
  pins; harness 21/21, `CASE_FLOOR` 21 (no gate check touched); dischargeable at rest,
  re-confirmed at the arc's release gate. (2) **[ship-verifiable — next ordinary upgrade,
  either vault]** delivery — installed `spec.md` carries the conditional form at both sites +
  the design note (and, in an adoption-stamped vault, the base text no longer contradicts the
  vault's stamped state), installed `vlt-setup`/`vlt-upgrade` carry the report-line edits, and
  the first post-upgrade `convention_adoption` line renders the "created — N days" vocabulary
  for any null axis; grep-checkable, bounded. (3) **[field-contingent]** A7-6's vault-side
  evidence, per the evidence-debt attachment — vlt-core's reported state corroborated at its
  0.10.0 upgrade: the stamped `adoption_first_instance` renders **adopted** on its adoption
  line while the shipped base stays honestly `null`, and the recorded promotion-era bump
  (relayed against the handoff path) survives as the worked instance the deferred check's
  builder will key on; producing vault: **vlt-core only** (owner-run; the factory cannot read
  it — evidence arrives as the owner's pasted upgrade report / ledger entry); corroboration
  only, never the fixes' discharge; if unread by closeout it goes to the watch register, not
  the gate.
  **Both ship-verifiable checks DISCHARGED 2026-08-17; STILL-OPEN: the promotion-instance leg
  of the field-contingent check (3).** (1) the sweep's fixes are coherent at rest —
  `spec.md` carries the conditional form at both sites (`:14` key comment and the `:92`
  Enforcement paragraph, both reading "**while adoption is zero**"; no permanent-form "cannot
  fire" assertion remains) with the `spec_notification_missing` historical-paths design note
  present at `:90` and `version: 2` unmoved; `vlt-upgrade/SKILL.md:108` and `:115` agree on
  the "created `YYYY-MM-DD` — N days" vocabulary with the proxy stated (the brief's `:105`
  /`:112` line numbers drifted by three, same sites); `package-lint` A/B/C/E PASS with group E
  confirming `frontmatter@7`/`spec@2`/`decision-log@2` bipartite-consistent, zero stray pins;
  harness `21/21`, `CASE_FLOOR = 21`. (2) delivery confirmed twice over — installed
  `_meta/conventions/spec.md` carries the conditional at both sites plus the design note, and
  the vault's stamped `adoption_first_instance: 2026-06-13` no longer sits under contradicting
  base text; installed `vlt-upgrade/SKILL.md:108`/`:115` carry the edits; and the **first
  post-upgrade `convention_adoption` line rendered the new vocabulary live** — "consult —
  declared, no first instance yet (created 2026-07-26 — 20 days)", "wiki-consolidation —
  … (created 2026-06-01 — 75 days)". (3) **Adoption-render leg DISCHARGED** — the same ledger
  line reports `spec` **adopted** 2026-06-13 and `decision-log` **adopted** 2026-07-30 while
  the shipped bases ship honestly `null`, exactly A7-6's claim. **STILL-OPEN:** the
  promotion-era bump relayed against the pre-promotion handoff path surviving as the worked
  instance the deferred `spec_notification_missing` check will key on — not read this run;
  corroboration only, non-gating. Trigger: the deferred check's build, or an owner read of the
  health-coach→chef spec's relay history.
  **Residue noted, not a deviation:** `vlt-upgrade/SKILL.md:134` (the ledger-entry template
  comment) still reads a third wording — "declared, not yet (since created: — N days)" — not
  identical to `:108`/`:115`. The brief scoped exactly two sites, so this is out of B7-8's
  stated scope, but it is the same drift class the sweep exists to close. Candidate for Arc 8
  capture.
  **RELEASED AS A STANDING WATCH at arc close 2026-08-17 (owner batch ruling).** Recorded here
  rather than ticked — the promotion-instance leg was never exercised, it was released. It is
  corroboration only and non-gating by its own terms. Carries forward past Arc 7.

---

## Closeout record — Arc 7 CLOSED 2026-08-17

**What the tick count does and does not mean.** Four of eight ledger items are `- [x]`; the
other four carry ship-verifiable-discharged / tail-released splits. **The `[x]` count is not a
measure of what the arc proved.** Every *ship-verifiable* check in the arc discharged with
dated evidence; the four unticked boxes are held open by field-contingent tails that were
**released, never exercised** — per the gate's rule that only ship-verifiable checks gate
closeout. Read the per-item annotations, not the checkboxes.

**Acceptance evidence of record:** the vlt-core 0.9.1→0.10.0 upgrade (2026-08-15 19:23,
own-the-apply), the first post-upgrade full lint (`_agent/lint-reports/2026-08-16-1118-lint.md`),
the owner's post-0.10.0 `vlt-dispatch ledger` run (2026-08-17), and factory-side at-rest runs
(`test-package-lint` 21/21, `package-lint --expect-version 0.10.0` exit 0).

**The arc's headline result:** B7-6 check (3) discharged the **A4-4 clause (5) Jackson-pair
debt after four arcs** — the first time an inherited debt was closed rather than re-carried.
Amendment A3 (tag it ship-verifiable so it gates) was the mechanism; it worked. **This debt
does NOT carry forward.**

### Carried forward past Arc 7

*Released standing watches (owner batch ruling 2026-08-17 — never exercised, released):*

1. **B7-2 (4) work-vault manifest containment** — the work-machine vault's hand-widened
   55-entry set strictly contained by the structural walk. Trigger: `vlt-upgrade` on the work
   vault. Producing vault: work-machine only (factory cannot read it).
2. **B7-4 (4) the first sanctioned local convention** — minted, no `baseline_missing`, no
   coherence false positive, counted by the split tripwire, honored by a consumer. Trigger: an
   owner mint; named candidate is re-homing vlt-core's A7-8 prose-line rule out of the
   `frontmatter` overlay (Rule A) into a minted local convention.
3. **B7-4 (5) the first dispatch roster** — a multi-principal vault declares
   `_agent/dispatch-profile.md` and routes a cross-principal relay. Producing vault:
   work-machine team vault only; **structurally unproducible in vlt-core** (single-principal).
4. **B7-7 (5) the `(council — lenses: …)` leg** — a council-fielded gated mint recording the
   facet from the workflow's own return. The `(user-ruled — panel not fielded: …)` leg
   discharged on an owner-accepted substitution (the 2026-08-15 overlay Rule B retirement).
   Trigger: the next council-gated mint in vlt-core; no upgrade forces one.
5. **B7-8 (3) the promotion-instance leg** — the promotion-era `version` bump relayed against
   the pre-promotion handoff path, surviving as the worked instance the deferred
   `spec_notification_missing` check will key on. Corroboration only, non-gating by its terms.

*Inherited debt:*

6. **B7-4's ⚠ design-reconstruction owner-review flag** (owner ruling, this close: carry to
   Arc 8). The A7-4 vault-side decision matrix was unrecoverable, so the brief re-derived the
   decision space; dispositions 1, 6/7 and 8 stand **unreviewed**. It was to be discharged at
   the v0.10.0 release and was not. **First arc carried.**

*New field signal awaiting `inbox-capture`:*

7. `inbox/2026-08-17-140000-handoff-shape-has-no-form-for-an-inline-payload.md` — filed
   2026-08-17 off the ledger run. An **unsolicited delivery with an inline payload has no legal
   relay shape**, and `ledger.md`'s stated legal response for the resulting finding is
   *unperformable* (an R3 violation, in the arc that declared R3). Note the shape of the miss:
   the arc's own through-line reproduced **inside the build written to fix it**.
8. **Three module-feedback candidates from the 2026-08-16 full lint** (owner's vault-side
   report, strength-ordered there): the naive `spec_candidate` relay count firing the same 6
   false positives for a **third consecutive run**; `vlt-lint-full.js` scanner prompts not
   honoring `frontmatter` rule 4's coexistence posture nor the callout-vs-bullet distinction;
   the fan-out's `crossLayerSlugs` omitting `_agent/handoffs/`, `_agent/bases/` and `areas/`.
9. **Two small drift residues** — `vlt-upgrade/SKILL.md:134` still carries a third adoption
   wording ("declared, not yet (since created: — N days)"), outside B7-8's stated scope but the
   same drift class; and `ledger.md`'s *legacy line* does not say whether its unit is the relay
   block or the pointer line, nor whether a payload `[[wikilink]]` counts as a path — the count
   is therefore unverifiable by a second reader.

*Carried in from earlier arcs, still open (authoritative list — Arc 8 re-lists from here):*

10. **C6-c** — the Stage-7 bullet the owner must paste (open since Arc 6's close).
11. **The B5-3..B5-9 field-contingent watch register + the pre-Arc-5 carries**, including the
    `vlt-track` loop-profile watch item and the BMB drift to file upstream to BMAD-METHOD
    (owner). See the archived Arc 5 and Arc 6 closeout records.
12. **R3** — no finding class ships without a stated legal response: **declared Arc 7, built
    Arc 8** (owner ruled it stays on the ladder argument). Carry-forward 7 above is its first
    worked violation in the wild.

### Which filings moved under which criterion

Per Stage 5's per-filing rule (widened 2026-07-26): a filing archives when every clause
traceable to **that filing** is discharged **and** the build's remaining tails belong to a
**different** filing. Nine filings moved on that criterion — A7-1, A7-2, A7-5, A7-7, A7-9,
A7-10, A7-11, A7-12, plus the A4-4 carrier `2026-07-25-160949`. **Held live:** A7-3
(`2026-08-03-100710`, its own clause is carry-forward 1), A7-4 (`2026-08-08-123610`, its own
clause is carry-forward 3), A7-6 (`2026-08-14-142625`, its own clause is carry-forward 5),
A7-8 (`2026-08-14-154423`, its own clause is carry-forward 2), A7-13
(`2026-08-14-182143`, its own clause is carry-forward 4) — each stays active because *its own*
clause is a released watch, regardless of how much of its build discharged.

---

**Next lifecycle move (updated 2026-08-17, acceptance-discharge run 1, after the ledger run):**
**`arc-closeout`.** Every ship-verifiable check in the arc is now discharged — B7-5 check (4),
the last one open, closed on the owner's `vlt-dispatch ledger` run the same day. Four items are
ticked whole (B7-1, B7-3, B7-5, B7-6) and four carry ship-verifiable-discharged / tail-open
splits (B7-2, B7-4, B7-7, B7-8), which is the state closeout is designed to consume: it gates
on ship-verifiable checks only and releases the rest to the watch register. Two things go in
with it — **B7-4's ⚠ design-reconstruction owner-review flag**, still undischarged from the
v0.10.0 release, and the new filing
`inbox/2026-08-17-140000-handoff-shape-has-no-form-for-an-inline-payload.md`, which the ledger
run surfaced and which belongs to Arc 8's capture, not this arc's gate.
The field-contingent tails released to the watch register:
B7-2's work-vault manifest containment (trigger: `vlt-upgrade` on the work-machine vault),
B7-4 (4) the first sanctioned local convention (trigger: an owner mint) and (5) the first
dispatch roster (trigger: the team vault; unproducible in vlt-core), B7-7 (5)'s
`(council — lenses: …)` leg (trigger: the next council-gated mint), and B7-8 (3)'s
promotion-instance leg.

*(Superseded — the arc's original next move, kept for the record:)* **brief build B7-1** (`build-brief`) — ideation closed 2026-08-15 with eight
builds ruled and ship order set (`B7-1 → … → B7-8`). B7-1 (the harness, A7-1) opens the arc and gates
B7-2; B7-3 (`frontmatter@6`) gates B7-4, B7-5 and B7-6. **B7-1's brief additionally scopes R2**
(post-ideation amendments). Two obligations must be discharged before their builds are briefed, not at
brief time: the owner supplies A7-4's vault-side decision matrix before **B7-4**, and B7-3's brief
reads `skills/reports/archive/` for A7-5's date provenance. **A third, added 2026-08-15:** the
count-since-N / stale-prose **class count** (amendment A4) runs **before B7-3 is briefed** — a
read-only sweep of shipped convention frontmatter, blocking on nothing. Briefs cite the *Ideation
rulings* section **and the *Post-ideation amendments* section** and never re-litigate either.
