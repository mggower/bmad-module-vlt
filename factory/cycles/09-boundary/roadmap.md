---
title: 'Inbox Evolution Roadmap — Arc 9: the boundary arc'
status: 'CLOSED 2026-08-21. Shipped v0.12.0 2026-08-21 (release commit 336d90b, tag v0.12.0 on the public remote; builds B9-1..B9-4 + factory-only B9-5). Acceptance discharged over two passes 2026-08-21: the owner vlt-core 0.11.0→0.12.0 upgrade (vault commit 029ee39) + post-upgrade ledger run + blind vault audit (15/15) discharged the [v0.12.0 run] partition; the app-vault rail runs (issues #2/#3) discharged E1/E3 and B9-5(3)s first live materialization. The closeout-gating B8-2(4) re-check is GREEN — the two-arc debt retired. OWNER RULING 2026-08-21: B9-6 and B9-7 FOLD TO ARC 10 UNBUILT (Dispute 3 release-forward; Arc 3→build-17→Arc 5 precedent) — v0.13.0 was not shipped by this arc; S3/S2 ride with them. Still open elsewhere: see the Closeout record — Carried forward past Arc 9 (10 entries: the fold, E2, the lint-cycle + vitals + Stage-5-terminal + rail-degrade watches, the PARA posture, the lane-check grammar note, 8 uncaptured 2026-08-21 filings, the inherited registers). This arc is archived — do not append.'
module_code: 'vlt'
created: '2026-08-20'
updated: '2026-08-21'
successor: 'Arc 10 (not yet opened) — inherits A9-1 in full, plus S1, Q6, Q7, D7, E5, E6 and four brief-time questions (Round 1, 2026-08-20)'
derives_from:
  - 'inbox/2026-08-18-121417-vault-grown-consumers-have-no-durable-registration.md'
  - 'inbox/2026-08-19-130120-feedback-loop-is-single-machine-github-issues-as-remote-rail.md'
  - 'inbox/2026-08-19-155515-tripwire-metrics-have-no-durable-vault-local-home.md'
  - 'inbox/2026-08-20-093000-para-write-path-single-door-wrong-shape.md'
  - 'inbox/2026-08-18-094459-activation-ritual-omits-overlays-fleet-rules-land-as-per-partner-reflexes.md'
  - 'inbox/2026-08-18-101612-proto-deliver-era-test-names-no-datum-and-handoff-ref-slips-its-key-rule.md'
predecessor: 'skills/reports/archive/inbox-evolution-arc8-roadmap.md (Arc 8 — CLOSED 2026-08-18, builds B8-1..B8-5 shipped v0.11.0 @ 86efd48)'
intent: >
  Arc 9 is the boundary arc — narrowed by ideation (Round 1, 2026-08-20) to the boundaries the
  module can fix without first going to the field. Every filing here says the same thing about
  a different line the module drew: the boundary is in the wrong place, or on the wrong axis,
  or drawn where no mechanism can enforce it. The consumer-registration filing says the
  base/overlay boundary sends vault-local additions to a zone the enforcement machinery cannot
  see. The tripwire-metrics filing says the module-owned/vault-owned boundary through
  `.claude/hooks/` cuts a vocabulary in half. The activation filing says that same overlay zone
  is never *read* at the moment rules must bind. The dispatch-ledger filing says two adjacent
  rules claim the same pointers with no precedence between them. And the feedback-rail filing
  says the module's own front door is drawn at a filesystem path only one machine can reach —
  the ingress the others had to route around, and the reason two of the six filings nearly
  never arrived.

  The sixth filing, A9-1 (PARA's single write-path has the wrong shape), was the arc's original
  headline and is **no longer in this arc**. Ideation ruled it out to Arc 10 because it is the
  only filing whose brief cannot be written from module source: its S1 harvest obligation
  requires reading two live vaults before any contract text exists. Its thesis — that Layer 3's
  boundary is drawn by *location* when it should be drawn by *authorship* — remains the deepest
  reading of this arc's through-line, and Arc 10 inherits it whole. Arc 9 pays a second
  `frontmatter` handshake bump for the split, knowingly.
---

## The through-line

**Every boundary in this arc fails the same way: it is enforceable exactly where it does not
need to be, and unenforceable exactly where it does.**

Read the filings as one argument. *(roundtable A19, 2026-08-20: **five in-arc filings**, not
four — this section still opened on A9-1/PARA as the leading exhibit after Round 1 moved it to
Arc 10. A9-1's paragraph below is **carried here for the argument only**; it is Arc 10's.)*

`vault-operating-contract.md:61` draws Layer 3 by **location** — `projects/`, `areas/`,
`resources/` are human territory, and partners "never write directly into it." The PARA
filing proves at scale that agents did not stop writing; they routed through the single
sanctioned door (`vlt-extract`) and falsified the fields at it. A location boundary that
work must cross gets crossed. Meanwhile `vlt-lint` has been catching the crossings since day
one (`checks.md:16`, `para_missing_attestation`) — and governance never named the door lint
was already watching.

The consumer-registration filing is the same shape one layer up. The base/overlay boundary
is drawn by **file location** too: pristine bases in `{conventions}`, vault-local additions
in `{overlays}`. But the coherence check (`checks.md:36`) and the enforcement-doctrine
meta-check (`checks.md:37`) both walk `{conventions}/*.md` **only**. So the zone the
durability model sends vault-local rules to is the one zone no checker opens. The module's
own doctrine — *no boundary without a bell* — is unsatisfiable for any rule that lands where
the durability model puts it.

The activation filing (A9-5, capture run 2) closes that loop from the read side. The contract
already rules at `vault-operating-contract.md:100` that "**Any reader of a convention reads the
base, then applies its overlay if one exists**" — but the activation ritual
(`vault-operating-contract.md:167`) never reads a convention, so the overlay never surfaces at
the moment a partner starts writing. **A9-2 says nothing checks the overlay zone; A9-5 says
nothing reads it either.** The same zone, missed from both directions.

The dispatch-ledger filing (A9-6, capture run 2 — Arc 8's bound inherited debt) is the arc's
thesis at the smallest possible scale: two **adjacent bullets**, `ledger.md:25` and
`ledger.md:26`, draw a boundary through the same population of pointers, and neither states
which one wins. Not a missing rule — **two rules, one line apart, with no precedence between
them.**

The tripwire-metrics filing (materialized from issue #1) is that same unsatisfiability in
code rather than prose: `{tripwires}` is vault-grown and durable, the metric vocabulary it
must name is module-owned and clobbered, and the boundary between them runs straight through
a single dependency.

And the feedback-rail filing is why this arc exists at all. Two of these four filings
originate on machines with no route into `inbox/`; one of them reached the factory only
because an agent bypassed the module entirely and opened a GitHub issue with no shape
governance, no sensitivity gate, and no lifecycle linkage. **The front door is itself a
location boundary drawn where most of the field cannot reach it.**

**The convergence worth naming.** Filing 1's Finding 5 and the tripwire-metrics filing are
the *same defect* reached from opposite ends. Finding 5: no bell in `{overlays}` can ever
ring, partly because a wire's `metric` must name an id in `.claude/hooks/vlt-vitals.py` and
adding one means editing a shipped module file. Issue #1: that file is overwritten every
upgrade, so the edit does not survive. Neither filing knew about the other. **Either fix
alone leaves the other half broken** — a durable local metric home with no overlay-reachable
checker still rings no bell, and an overlay-walking checker with no durable local metric
still has nothing to key on. Ideation should treat them as one joint, not two builds.

**Where this arc inherits from.** Arc 8 handed forward B8-2 (4) as **bound** inherited debt
(the proto-`deliver` era test naming no datum), whose re-check is `[ship-verifiable]` from
birth and therefore **gates** Arc 9's closeout. **Its filing is captured here as A9-6**
(capture run 2). Ruling 4c's three lint-surfaced module-feedback candidates were **never
filed** — Arc 8 recorded the bound as MISSED, and there is nothing in `inbox/` to capture.
Capture cannot manufacture a filing that does not exist: **they remain owed by the owner, not
by capture**, and should be raised at ideation rather than waiting on a third capture run.

---

## Capture — 6 filings (grounded against module source 2026-08-20)

*A9-1..A9-4 captured in run 1; A9-5..A9-6 appended in run 2 the same day — see the capture
narrative for why run 1 missed them.*

### A9-1. PARA's single write-path has the wrong shape (2026-08-20) — `inbox/2026-08-20-093000-para-write-path-single-door-wrong-shape.md`

The largest filing in the arc, and the only one that arrives with its own roundtable already
run. Its body and its roundtable section disagree in places; **the roundtable section is
authoritative where they conflict, by the filing's own instruction**, and grounding below
respects that.

**GAP CONFIRMED — the four sites that carry the location rule all agree, and none names an
authorship axis.**

- `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md:61` — "**Layer 3 —
  PARA (`projects/`, `areas/`, `resources/`):** Human-curated knowledge. Artifacts arrive
  here only through the extraction workflow… Partners read from PARA but **never write
  directly into it.**"
- `…/vault-operating-contract.md:63` — "**The hard rule:** Partners write only to `_agent/`
  and `_meta/`… PARA folders are human territory."
- `…/conventions/extraction.md:45` — "**This does not open a second PARA write-path.**"
- `skills/vlt-agent-creative/SKILL.md:14` — "extraction is the *one* sanctioned way a partner
  writes into PARA; you honor that boundary and never open a second one."
- `skills/vlt-extract/SKILL.md:11` — "It reaches the wiki **only**."

Five sites, one rule, zero authorship vocabulary. The filing's C1 (re-draw Layer 3 by
authorship) has no shipped counterpart to amend — it is new contract text, not an edit.

**CONFIRMED — K1, and it is sharper than the filing states.** `skills/vlt-lint/references/checks.md:16`
ships `para_missing_attestation`: "a PARA file carrying vault `type:` + `author: agent|hybrid`
with no attestation (**the out-of-path-write net — a real finding from day one**)." The
parenthetical is in the shipped text. The module has been operating a named net for a class of
write its constitution says cannot occur, and has done so since the check was written.

**CONFIRMED — K1b, verbatim.** The legal response shipped at `checks.md:16` is "the owning
writer re-runs its verify pass and attests." `…/conventions/write-verification.md:47` declares
the `verified_by` value set as "the three write ops (`vlt-ingest`, `vlt-extract`,
`vlt-research`) plus `vlt-lint`" — a flat closed enumeration with no delegation clause. An
out-of-path writer is none of the four. **The finding's only lawful remedy is unreachable by
the only agents that can trigger it.** (Note the direct dependency on A9-2 Finding 1, which
is about the *same sentence* at the *same line*.)

**CONFIRMED, and materially understated — K14's "single `vault_structure` entry."**
`skills/vlt-setup/assets/module.yaml:44-61` is the canonical default map. Moving the wiki out
of `_agent/` touches **two** entries, not one: `wiki: _agent/wiki/` (line 45) **and**
`index: _agent/wiki/index.md` (line 46). More consequentially, **the PARA folders are not in
`vault_structure` at all** — `projects/`, `areas/`, `resources/` appear nowhere in the map;
they are hardcoded prose in the contract (`:61`), in `extraction.md:26`, in
`frontmatter.md:159`, and in `vlt-agent-creative/SKILL.md:18` ("The PARA targets you make
into are `projects/`, `areas/`, `resources/` at the project root"). So "retire `resources/`"
has **no designed parameter to change** — it is prose surgery across at least four files plus
a `type:` mapping. K14's mechanical claim holds for *moving the wiki*; it does not hold for
*retiring `resources/`*. Ideation should not budget these as one small edit.

**CONFIRMED — the `type:` mapping is a third site K14 must touch.**
`…/conventions/frontmatter.md:164` — "`type:` mapped to target folder: `projects/` →
`project`; `areas/` → `area`; `resources/` → `resource`." Retiring `resources/` retires a
`type:` value, which is frontmatter schema, which is a `frontmatter@8 → @9` bump and a walk
of every consumer (`frontmatter.md:12` lists seven-plus consumers).

**CONFIRMED, with the mechanical cause located — K4's eight forked `status:` vocabularies.**
The filing diagnoses "`status:` is on the artifact, not the project." Grounding adds *why the
vocabulary itself forked*. Wiki pages and research notes get an **enumerated** field
(`frontmatter.md:97` and `:131`, both `status: draft | in-progress | complete`). PARA
artifacts get **prose inside an angle-bracket placeholder**: `extraction.md:94` —
`status: <varies by type — project: in-progress, area: ongoing, resource: complete>`. That is
not an enumeration a writer can copy; it is an instruction to derive one. Three vaults derived
three different ones. **The fork is a schema-shape defect, not merely a modeling gap** — and
it means K4's remedy has a second half the filing does not name: whatever container model
lands, the per-type PARA `status:` must become an enumeration like every other zone's.

**CONFIRMED, and it ships in module source — K9's inline-vocabulary-comment hazard.** The
filing cites a `vlt-sayari` areas file whose `status:` reads `digested   # digested | draft`.
Grounding found the module shipping the pattern in exactly one place, and it is the worst
possible place: **`skills/vlt-mint/assets/capability-template.md:23`** —
`provenance: vault-grown            # shipped | vault-grown (usually implied by location)`.
A *template* is copied verbatim by construction. One shipped instance, in an asset whose
whole purpose is to be duplicated into vaults. K9 is not a style note; it is a live defect
with a single known site.

**PROVENANCE CORRECTION — the body's headline, already self-corrected by K11, and grounding
agrees with K11.** The body reads the `sources:` entries pointing at PARA siblings and
external repos as falsified provenance. `extraction.md:106` says "`sources:` lists the wiki
pages that fed the extraction… The wiki, not any source beneath it, is the provenance layer."
There is no field for a project-to-project edge and none for an external-evidence reference.
The writers used the only list that existed. **This grades as a missing edge type, not a
breach** — which is exactly K11's ruling, and it does not weaken C4: `grounding:` is still the
repair, it is just repairing an *absence* rather than punishing a *lie*. Ideation should carry
K11's framing, not the body's, into any build brief — the body's "compliance theater" language
would misdescribe the field's behavior in shipped text.

**CONFIRMED — the `vlt-deliver` name collision.** `vault-operating-contract.md:262` — relay
"carries **doc-less `ask`/`answer`/`deliver` traffic**." `deliver` is a relay kind. The name is
unavailable, as the filing states. (Moot under R-a/K2 anyway — the write-time verb was
withdrawn — but the collision is real if a verb name is revisited.)

**CONFIRMED as available — K2's harvest machinery.** Arc 8 shipped both halves the K2 revision
depends on: `skills/vlt-groom/` (approval-gated pass over partner memory) and
`skills/vlt-decay/` (mechanical decay verbs — `rotate`/`drain`, retention-at-birth). Neither
carries a project-close trigger today; K2/K7 propose adding one. This is an extension of
shipped machinery, not new machinery — a genuinely cheaper build than the body's C3 implied.

**NOT GROUNDED — deliberately.** K12 (multi-user trust model) is owner-ruled out of scope at
filing time and does not enter capture. Recorded here only so it is not re-discovered as a
defect. K13's instruction ("read the model out of `app-vault`'s two index files and
`vlt-sayari`'s 210 before writing any contract text") is a **build-time obligation on the
harvest**, not a capture-time act — this run did not read those vaults, and the brief must.

**Residual scope after grounding.** The filing's own roundtable already retired C2 (posture
was the wrong axis), C3's write-time gate (R-a), and the verb-name question. What remains is
larger than the body's five-component list and differently shaped:

1. Re-draw Layer 3 by authorship (C1) — new contract text, five recitation sites to recast.
2. Model the PARA container on the **bounded/unbounded** axis (K3/K6/K10) — harvested from
   the field, not designed (K13).
3. `grounding:` as a separate provenance field (C4) — `frontmatter@8 → @9`, plus the
   project-to-project relation K11 identifies as the actually-missing edge.
4. Enumerate PARA `status:` per type, closing the `extraction.md:94` placeholder defect.
5. Harvest trigger on container close (K2/K7), riding `vlt-groom`/`vlt-decay`.
6. The lint family (C5) — **the filing's own hard constraint is that this ships in the same
   build as any widening**, and grounding endorses it: `para_missing_attestation` already
   demonstrates what an unenforceable rule decays into.
7. The wiki move + `resources/` retirement (R-d/K14) — larger than one parameter, see above.
8. Fix `capability-template.md:23` (K9) — one line, no dependencies, buildable immediately.

**Open design questions carried verbatim (do not resolve here).** The body's five are largely
dispositioned by its own roundtable table; what remains genuinely open, per that table plus
grounding:

- K16 (watch) — "Every time content crosses the agent/human boundary, an attestation check
  becomes a census." Seen twice (`para_missing_attestation` at 56/56). Moving the wiki into
  human-browsable space will mass-produce `attestation_stale`. **Third instance is predictable;
  design for it now.**
- The body's watch item — "`grounding:` is a candidate laundering channel for method claims —
  the same failure `extraction.md` already anticipates for `personalization_sources:`."
  Grounding confirms the precedent is live and already enforced: `checks.md` ships the
  *Personalized-extraction firewall* check with `method_not_in_sources` and
  `method_in_personalization`. **The `grounding:` field should inherit that check family
  rather than invent one** — a capture-level observation, not a resolution.
- Whether `areas/` retiring-into-ideation-home (K3) survives contact with the harvest (K13).

---

### A9-2. A vault-grown op has no durable way to register as a convention consumer (2026-08-18) — `inbox/2026-08-18-121417-vault-grown-consumers-have-no-durable-registration.md`

Filed against a real upgrade reconcile, and honest about what did **not** go wrong: the
filing explicitly retracts its own vault's backlog claim that the upgrade would silently
revert the edits. The machinery worked. The defect is that it had to.

**GAP CONFIRMED — Finding 1, the base names no carve-out.**
`…/conventions/write-verification.md:47` declares the `verified_by` value set as a flat closed
enumeration: "the three write ops (`vlt-ingest`, `vlt-extract`, `vlt-research`) plus
`vlt-lint`." No delegation clause, no extension mechanism, no carve-out language anywhere in
the *Attestation* section (`:42-47`). `consumers:` at `:12` is the matching four names. The
filing's reading is exact.

**CONFIRMED — Finding 3, and it is a single-home violation stated against the files' own
declared division of labor.** `…/conventions/frontmatter.md:75` opens the section: "This
section defines only the **fields**; the checklist, fail-open rule, scope rule, and audit
contract live in `write-verification.md`." Eight lines later, `frontmatter.md:82` says: "The
legal value set is the three write ops plus `vlt-lint`." A value set is contract, not field
schema. **The file violates the sentence it opens with.** `write-verification.md:44` states
the reciprocal division ("The fields… are defined in `frontmatter.md` — referenced here, not
redefined. This file owns the contract around them"). Both files agree on who owns what; one
of them restates anyway. The fix is a pointer, and it is small.

**CONFIRMED — Finding 2, both halves, from shipped text.**
- `skills/vlt-lint/references/checks.md:36` — the coherence check runs "For each
  `{conventions}/*.md` carrying a `version:` and `consumers:`". Overlays live at
  `{overlays}` = `_agent/conventions/` (`module.yaml:55`), a different path.
- `checks.md:42` — overlays "are **deliberately unversioned** vault-local additions carrying
  no handshake axis; an overlay addition is invisible to the version handshake by design."

So an overlay-registered consumer is never walked, and the stale-ack alarm — which keys off
the base `consumers:` roster — will never fire for it. The filing's live proof is worth
preserving in the brief: `vlt-sweep` was pinning `frontmatter@7` against a base at
`version: 8` (`frontmatter.md:11` confirms `version: 8`), a genuine stale-ack finding
detectable **only** because the name still sat in the base roster the vault was about to
revert.

**CONFIRMED, and mechanically clean — the preferred fix (`local_consumers:`).**
`…/conventions/frontmatter.md:276` (*Vault-writable declared fields*) is the member set's
declared single home and today holds exactly two: `adoption_first_instance:` and
`review_after:`. The section states the mechanism is live — "the divergence surfaces
(`vlt-lint`'s base-divergence check and `vlt-upgrade`'s pre-flight) exclude the declared
fields, and the upgrade's base refresh carries a locally-written value forward (both-moved
collisions are surfaced, never silently merged)." The base-divergence check at `checks.md`
confirms the exclusion and, per single-home discipline, **carries no list of its own** —
it reads `frontmatter.md`'s section. **So adding `local_consumers:` requires editing exactly
one list**, and the consuming nets follow for free. The section also states its own price:
"Declaring a further field vault-writable is a base rule change: it bumps this file's
`version:` and walks every consumer" — i.e. `frontmatter@8 → @9` and a full re-ack.

That price is worth flagging to ideation as a **joint with A9-1**, which independently needs
`frontmatter@8 → @9` for `grounding:`. **One bump can carry both if they are sequenced
together; two bumps if they are not.**

**CONFIRMED — Finding 4, one enforcement declaration per file.**
`…/conventions/frontmatter.md:255` — *Enforcement declaration (convention files)* — is a set
of flat, file-level frontmatter keys (`enforcement_stage:`, `deferral_metric:`,
`deferral_threshold:`, `review_after:`, `adoption_first_instance:`). There is no
per-section addressing anywhere in the schema. An overlay accretes sections; the declaration
does not. The filing's claim that the next genuinely rule-shaped overlay section "cannot be
declared honestly at all" follows directly from the schema shape.

**CONFIRMED — Finding 5, and this is the arc's structural centre.**
- `checks.md:37` — the enforcement-doctrine meta-check validates "every `{conventions}/*.md`
  file's enforcement frontmatter." Overlays are not walked, so `deferral_expired`,
  `declared_untripwired`, and `deferral_invalid` cannot fire on an overlay-hosted rule.
- The same line ships `counter_unknown_metric` — "an `enforcement_counter:` present but naming
  no id in the vitals reader's canonical metric table — `.claude/hooks/vlt-vitals.py`, **the
  enforcement kit's one vocabulary**."
- `skills/vlt-setup/assets/hooks/vlt-vitals.py:189` — "THE CANONICAL METRIC VOCABULARY
  (disposition 5 — the one vocabulary)"; `:194` `METRICS = {…}`; `:283` `if metric_id not in
  METRICS: return "error", f"unknown metric id …"`.

Both escape routes are closed exactly as the filing says. **See A9-3 — that filing closes the
loop on why the remaining route (edit the shipped file) is not a route either.**

**PROVENANCE NOTE — the bonus instrument note is correctly self-classified.** The filing calls
the `diff` → `rtk diff` shell-hook wrapping "not a module defect," and grounding agrees: it is
a local shell hook, not module source. The *derived* recommendation is module-scoped and
buildable, though: if any shipped doc instructs a base-vs-baseline comparison, it should
specify a checksum or a real line differ, because a wrapped `diff` fails toward "no
divergence" — the dangerous direction. Worth a grep at brief time; not grounded in this run.

**Residual scope after grounding.**

1. A delegation clause in `write-verification.md` §Attestation (Finding 1) — this is the same
   sentence A9-1's K1b needs changed, from a different direction. **Joint.**
2. `frontmatter.md:82` → pointer, not restatement (Finding 3). Small, no version bump (prose
   clarification removing a duplicated rule, per the version-handshake rule).
3. `local_consumers:` added to the *Vault-writable declared fields* member set
   (`frontmatter.md:276`) — one list edit, `frontmatter@8 → @9`, full consumer re-ack.
4. Per-section enforcement addressing for overlays (Finding 4) — schema change, larger.
5. An overlay-reachable bell (Finding 5) — **jointly gated with A9-3**; neither half works
   alone.

**Open design questions carried verbatim.** The filing resolved its own design and offers
`local_consumers:` as "a proposal, not panel consensus" — raised by the architect lens,
unreviewed by the other three. Two questions it leaves genuinely open:

- Is an overlay `consumers:` line legal at all under the operating contract's carve-out test?
  vlt-core's council **split** — the architect argued legality on monotonicity, the skeptic
  and historian read the contract's test as unsatisfied. The vault adopted the extension on
  the owner's ruling and **recorded the legality as unsettled**. A module cannot leave a live
  install there; ideation must rule.
- If `local_consumers:` lands, does the overlay path stay legal as a fallback, or is it
  closed?

---

### A9-3. Vault-local tripwire metrics have no durable home (2026-08-19) — `inbox/2026-08-19-155515-tripwire-metrics-have-no-durable-vault-local-home.md`

**Materialized by hand from `mggower/bmad-module-vlt#1`** (opened 2026-08-19T15:55:15Z, still
OPEN at capture, **no labels**), per the capture instruction in A9-4. This is the intake
prototype the feedback-rail proposal asked for — see A9-4 for what the exercise proved.

**CONFIRMED — all three legs of the "jointly unsatisfiable" argument, verbatim.**

1. `skills/vlt-setup/assets/tripwires.yaml:1-14` (header) — "The canonical metric vocabulary
   is the METRICS table in `.claude/hooks/vlt-vitals.py` — a wire's `metric` must name an id
   from that table and no other (an unknown id is a loud per-wire error, never a silent
   skip)." `skills/vlt-setup/SKILL.md:182` — the registry is "**skip-if-present with
   merge-by-id**… **Local thresholds win; local wires are never dropped or rewritten** — the
   registry is vault-grown state."
2. `skills/vlt-setup/assets/hooks/vlt-vitals.py:283` — `if metric_id not in METRICS: return
   "error", f"unknown metric id \`{metric_id}\` — not in the canonical table"`.
3. `skills/vlt-setup/SKILL.md:181` — "This file is **module-owned, not user-authored —
   overwrite it on every install/update**, exactly like the workflows above… **the vault never
   edits it**."

Durable registry, clobbered vocabulary, hard dependency between them. The issue's framing is
exact and needs no correction.

**CONFIRMED — the severity self-assessment is honest.** The issue grades itself
*degraded-loud*, not silent-green, and that holds: the orphaned wire returns `error`
(`vlt-vitals.py:283`) and `vlt-lint` ships `counter_unknown_metric` (`checks.md:37`). What is
silent is the **clobber**, and what it destroys is a derive function that must be rewritten
rather than re-pointed. Grounding endorses the distinction — it matters for build sizing,
because direction 3 (make the loss legible) is genuinely cheaper than 1 or 2 and is not a fix.

**NOT INDEPENDENTLY GROUNDED — the B7-2 manifest analysis and the Step-3/Step-3.6 ordering
trap.** Both are claims about `vlt-upgrade`'s internals that this run did not verify against
`skills/vlt-upgrade/`. They are carried as **stated, unverified** — the second-order trap in
particular (a reconcile re-applying a local edit before the manifest write, causing the
modified SHA to be recorded as stock) is a serious claim that deserves its own grounding pass
**at brief time**, not a capture-time assumption. Flagged for the brief.

**The joint with A9-2, restated because it is the arc's load-bearing dependency.** A9-2's
Finding 5 needs a metric id it can add durably; A9-3 needs a durable place to add one. The
issue's own direction 1 ("a vault-local metrics module… agent-zone, never overwritten — **the
same fate split the conventions overlay already uses**") reaches for the overlay pattern
independently — while A9-2 is simultaneously demonstrating that the overlay pattern has no
bell. **Ideation should rule on these together or the arc ships half a mechanism.**

**Open design questions carried verbatim.** The issue explicitly declares "not a strong
preference between these" and offers three directions in rough order of pattern-match:
(1) a vault-local metrics module `vlt-vitals.py` optionally imports; (2) declarative local
metrics inline in the registry (`derive: {kind: file_count, zone: …}`) for common
count/size/age shapes; (3) at minimum, make the loss legible — diff before overwrite, report
in the Confirm summary, plus a `vlt-upgrade` note. The filer offers a PR for whichever
direction the owner prefers. **Do not resolve here.**

---

### A9-4. The feedback loop is single-machine (2026-08-19) — `inbox/2026-08-19-130120-feedback-loop-is-single-machine-github-issues-as-remote-rail.md`

A design-stage proposal, owner-requested, with its evidence debts declared up front. It is the
only filing in this arc about the loop itself rather than the module's contents.

**GAP CONFIRMED — there is no shipped filing rail, at all.**
- `.github/` **does not exist** in this repo. No issue templates, no labels defined.
- `skills/vlt-setup/assets/module.yaml` declares no feedback-repo URL (the config block at
  `:36-62` holds `vault_structure` and nothing feedback-shaped).
- `skills/` contains no `vlt-feedback` or `vlt-file-feedback` skill — **provenance confirmed:
  the `vlt-file-feedback` the filing describes is vault-local to vlt-core, a local mint, not
  module source.** The filing states this correctly; recording it so no future reader mistakes
  it for a shipped skill.
- `inbox/README.md` confirms the substrate side: filings are "one dated markdown note
  (`YYYY-MM-DD-HHmmss-slug.md`)" landing in a directory. `inbox/` is gitignored (project
  `CLAUDE.md`, *Git & publishing*), so **there is no git-native remote route into it** — the
  filing's diagnosis that issues must sit *beside* the repo is structurally correct, not
  merely convenient.

**CONFIRMED by exercise — and the exercise found what the filing predicted.** This run
materialized issue #1 by hand as A9-3, exactly as the filing's capture note instructed. Three
observations from doing it, which are worth more than the proposal's paper design:

1. **The attribution debt is live, not theoretical.** Issue #1's GitHub author is `mggower`
   (the module owner's own account), while the origin vault is app-vault on the work machine.
   Author ≠ origin vault, confirmed on n=1. The materialized filing had to state the origin
   vault in a hand-written header field because **nothing in the issue carries it**.
2. **Labels are not merely undefined — the issue carries none.** `field:defect` /
   `vault-filed` do not exist, so a factory-side "list open `vault-filed` issues" intake step
   has nothing to query today. The intake half of the proposal is blocked on the repo-side
   half; they are ordered, not parallel.
3. **The scrub gate would have passed trivially here, which is a weak data point and the
   filing says so.** Issue #1 is machinery-only content — no vault paths, no personal-domain
   material. The filing's declared debt ("untested against real personal-domain signal") is
   unrelieved by this exercise. Ideation should not read the prototype as scrub-gate evidence.

**CONFIRMED — the proposal's three seams are genuine seams.** Grounding finds each part
lands on a surface that exists and is otherwise untouched: (1) `.github/ISSUE_TEMPLATE/` is
greenfield; (2) a `vlt-feedback` skill is a new skill directory with a declared transport URL
in `module.yaml` (which already carries module-level config and is the natural home);
(3) the factory-side intake touches `inbox-capture`'s Discovery stage and `arc-closeout`'s
Stage 5 archival — **exactly two lifecycle seams**, as the filing claims. Everything keyed off
inbox files stays untouched because the materialized artifact *is* an inbox file. The claim
that this is minimally invasive holds.

**Note on the `origin:` stamp.** The proposal specifies materialized filings carry
`origin: <repo>#<n>`. A9-3 was written with that stamp by hand this run. If the intake step
ships, that header field becomes machine-written and should be specified once, in one home —
`inbox/README.md` is the obvious candidate, and it currently describes the filename convention
but no frontmatter/header shape at all.

**Open design questions carried verbatim — the filing's four declared evidence debts.**

- **Shared-vault attribution:** GitHub author ≠ origin vault; the template's origin-vault field
  is the answer on paper, unproven in practice. *(Grounding upgrade: now confirmed as a real
  mismatch on the one live case, per observation 1 above — the debt is no longer hypothetical,
  but the remedy is still unproven.)*
- **Scrub-gate efficacy:** untested against real personal-domain signal; issue #1 is one
  favorable data point.
- **`gh` auth variance on the work machines:** assumed available/authenticated; not verified by
  any module machinery. *(This run's `gh issue view` succeeded from the factory machine only.)*
- **Community/noise traffic:** a public tracker admits non-vault filers; label partitioning is
  a design, not evidence.

**vlt-core posture, owner-ruled at filing (carried, not re-litigated):** one rail — vlt-core
files via `vlt-feedback` like every other vault; the local mint is retired by explicit owner
act post-ship. Distinct name → no upgrade collision; durability posture untouched.

**Provenance guess, carried as a guess (the filing marks it so):** the gap is a design omission
at the factory level — ingress never separated from substrate when the module went public —
not a defect in any shipped build. Grounding agrees: no build ever claimed a remote rail, and
`inbox/README.md`'s lifecycle prose describes a filesystem-local loop throughout, without ever
asserting reachability.

---

### A9-5. The activation ritual omits `{overlays}` (2026-08-18) — `inbox/2026-08-18-094459-activation-ritual-omits-overlays-fleet-rules-land-as-per-partner-reflexes.md`

Classified by its filer as a **pattern**, not a defect, and grounding agrees with that
classification: the single missing read is real, but the filing's larger claim is about where
fleet-wide rules *condense* when no fleet-wide rung exists.

**GAP CONFIRMED — the ritual reads no convention, so it can surface no overlay.**
`…/vault-operating-contract.md:167` (*Activation ritual — two beats*) enumerates both beats
exhaustively. Beat 1 reads the rule-card, the partner's SKILL.md persona, its
`{partners}/<partner>/identity.md`, and its `{partners}/<partner>/reflexes.md`. Beat 2 reads
`{index}` section headings, the last 5 `{log}` entries, the `{backlog}` `## Open` count + last
5, the partner's `## Thread`, its dispatch slice, and its `capabilities/` folder. **`{overlays}`
appears in neither beat**, and neither does any `{conventions}` file.

**The sharpening that matters — the module already has the rule, and it cannot fire.**
`…/vault-operating-contract.md:100` states: "**Any reader of a convention reads the base, then
applies its overlay if one exists.** The convention is the base file *plus* its overlay, merged
on read." That rule is **conditional on reading a convention** — it binds at JIT-read time. The
activation ritual reads no convention, so a write made outside an op that happens to name a
convention JIT-pair is unprotected. **This is not a missing rule; it is a correct rule keyed to
an event that does not occur at the moment it is needed.** The filing's own field evidence is
the proof: two partners violated the same overlay on the same day, the second *after* reading
a log entry recording the first's correction, self-catching only because a late verification
step happened to JIT-read the overlay. The filing states plainly that the catch was luck of
sequence.

**CONFIRMED — no fleet-wide always-loaded rung exists.** Grounding walked the always-loaded
surface. There are exactly two rungs loaded unconditionally at activation:

- `_meta/vault-rule-card.md` — loaded **first** (`vault-operating-contract.md:167`), "the
  identity-bearing and act-blocking rules derived from this contract."
- `{partners}/<partner>/reflexes.md` — "**always-loaded (read in Beat 1)** … one line per rule,
  hard-capped" (`vault-operating-contract.md:199`).

One is module-shipped and per-vault-identical; the other is **per-partner**. There is nothing
vault-scoped-and-fleet-wide between them. The filing's gradient claim — that fleet-relevant
rules condense as N per-partner copies because the middle rung is absent — follows directly
from that shape, and it is the same *verb-not-subject* smell the module already names for
skills, applied to rules.

**PROVENANCE CORRECTION — the reflex cap is vault-declared, not a module constant.** The filing
cites "the reflex cap (30/partner)". `vault-operating-contract.md:199` says the cap "its
falsifier, and its enforcement posture are declared in **the file's own frontmatter**". So `30`
is **vlt-core's declared value**, not a shipped number. This does not weaken the budget
argument — a per-partner cap spent on non-partner-specific rules is wasteful at any value — but
a brief must not write `30` into shipped text as though the module set it.

**CONFIRMED, and it eliminates one of the filing's two candidate homes.** The filing guesses the
fix lands "in Beat 1 or the rule-card load." **The rule-card is not available.**
`skills/vlt-setup/SKILL.md:146` — the rule-card "is **module-owned — overwrite it on every
install/update** … because it must track the *shipped* contract, never a vault's edit of it."
A vault-local overlay rule appended there is destroyed at the next upgrade. **That is A9-3's
defect exactly** — a vault-local addition landing in a module-owned file that setup clobbers —
reached from a fourth independent direction. Ideation should treat the rule-card as ruled out
and the surviving candidates as (a) a `{overlays}` read added to Beat 1, or (b) the fleet-wide
rung the filing floats.

**Residual scope after grounding.** Smaller than the filing implies for the read half, larger
for the rung half:

1. Add a `{overlays}` read to Beat 1 (or the rule-card load, now ruled out) — a contract edit
   at `:167`. The filing notes overlays are small and append-only by declaration (one 4KB file
   in vlt-core), so the boot cost is bounded but **non-zero and unmeasured**.
2. A fleet-wide always-loaded rule rung — a genuine design call, and **the filing says so**:
   "that is a design call the factory owns."

**Open design questions carried verbatim.**

- Beat 1 read vs. fleet-wide rung: the filing offers both and resolves neither. It explicitly
  marks its provenance guess as a guess: "**All of the above is a guess**; the grounded claim is
  only: two same-day field violations, a self-catch that was luck of sequence, and no shipped
  read that would have prevented either."
- **Its declared interaction with two other filings, carried as the filer stated it:** this is
  "the *read-side* of" `2026-08-14-154423-no-legal-home-for-a-vault-originated-new-convention`'s
  *residence-side* gap, and it interacts with the 2026-07-29 boot-cost filings — "any new
  always-loaded read spends the budget those filings measure." **Ideation must weigh the read
  against that measured budget, not add it blind.**

---

### A9-6. The proto-`deliver` era test names no datum (2026-08-18) — `inbox/2026-08-18-101612-proto-deliver-era-test-names-no-datum-and-handoff-ref-slips-its-key-rule.md`

**Arc 8's bound inherited debt, now captured.** Acceptance check B8-2 (4) FAILED against the
first post-0.11.0 `vlt-dispatch ledger` run on vlt-core. Its re-check is `[ship-verifiable]`
from birth and **gates Arc 9's closeout** (Arc 8's roadmap, *Carried forward past Arc 8*, item
1). Arc 8 captured the *symptom* in its ledger and routed the filing forward; this is its
capture.

**CONFIRMED — Gap 1, the era test names no datum.**
`skills/vlt-dispatch/references/relay.md:28` (*Backward compatibility (no backfill)*): "A
shape-annotated **pathless** pointer written **before `deliver` existed** is **proto-`deliver`
traffic** … tolerated as written, drained normally, exempt from the key check, reported by
`ledger` as a denominated count … **never as a finding**." The phrase "before `deliver` existed"
appears once and is never qualified anywhere in the file. Module ship, vault upgrade, and
first-`deliver`-in-record are all readings the text permits. The filing's observation that the
run's own two verdicts are **mutually inconsistent under any single datum** — calling a
2026-08-17 15:12 pointer post-era while rendering an older 2026-08-15 pointer as a finding — is
a coherence argument that needs no vault access to check, and it holds.

**CONFIRMED — Gap 2, `ref` on a `handoff` is undefined.**
`relay.md:41` (*The idempotency rule*): "The key is per shape: a `handoff` keys on its **doc
path** exactly as it always has; an `ask`, `answer`, or `deliver` keys on its **`ref`**."
`relay.md:32` (*Inputs and validation*): "**`handoff-path`** … is **required** for `handoff`";
"**`ref`** is **required** for `ask`, `answer`, and `deliver`." So on a `handoff`, `ref` is
neither required nor forbidden nor assigned a meaning. **Six pointers change lane on a
sentence nobody wrote.**

**GAP CONFIRMED — and grounding found a third gap the filing does not name.** The filing frames
the failure as two underspecified rules. Reading `ledger.md` shows the run's behaviour is also
licensed by a **direct overlap between two adjacent bullets, with no precedence rule**:

- `skills/vlt-dispatch/references/ledger.md:25` — "**Findings** — a *shape-annotated* pointer
  that fails its shape's key requirement: an `ask`/`answer`/`deliver` with no `ref`, **or an
  annotated `handoff` with no path on disk**."
- `skills/vlt-dispatch/references/ledger.md:26` — "**The legacy lines** … Shape-annotated
  **pathless** pointers written before `deliver` existed are proto-`deliver` traffic … **counts,
  never findings**."

A shape-annotated pathless `handoff` from before the era boundary satisfies **both** bullets
simultaneously: `:25` says render it as a finding, `:26` says never render it as a finding. The
bullets are **one line apart** and neither cites the other. **This is a rule conflict, not two
ambiguities** — and it explains the failure shape better than either gap alone does: a reader
applying `:25` first gets findings, a reader applying `:26` first gets a denominated count, and
both readers are obeying shipped text. Any fix that states the datum (candidate (a)) but leaves
`:25`/`:26` un-ordered leaves the conflict live. **Ideation should treat precedence as the
first ruling and the datum as the second.**

**CONFIRMED — the reproducibility claim's blind spot is real and correctly diagnosed.**
`ledger.md:28` (*Counting rules*) defines the **unit** rigorously — "The **unit is the pointer
line** … never the block" — and defines pathless via key-path resolution under the handoff zone,
with "Any other wikilink — research notes, wiki concepts — is payload and never counts as a
path." That is exactly the half the filing says reproduces correctly. **Nothing in the counting
rules addresses lane *membership*** (era boundary, handoff/`ref` interaction), which is the half
that failed. B8-2's check (3) verified the counting unit against a fixture and could not have
caught this, precisely as the filing argues.

**CONFIRMED — the blast radius is bounded, as filed.** Both lanes are "counts, never findings"
(`ledger.md:26`) and the proto lane is "exempt from the key check" (`relay.md:28`), so nothing
was mis-written into the vault. The cost is a ledger that reported a clean proto-`deliver` zero
while seven pointers sat in the lane it was denominating, and asked a maintainer to act on two
of them.

**Arc 8's second-order question, carried forward as bound.** Arc 8's hand-off states the
backward-compat exemption may be **over-broad** — read strictly it would have suppressed the
very finding whose repair discharged B8-1 (5) and B8-2 (5). **Arc 9 rules on the exemption's
*scope*, not only its datum.** Grounding adds that `relay.md:28` grants the exemption to two
lanes at once (un-annotated pathless *and* shape-annotated pathless), and the over-breadth
question applies to both.

**Open design questions carried verbatim — the filing's four candidate dispositions, explicitly
"not rulings":**

- **(a)** State the datum in `relay.md:28` — "the strongest candidate is per-record: 'before the
  first `deliver` pointer exists in this record', which is derivable at read time and needs no
  version knowledge."
- **(b)** State the handoff/`ref` interaction — "either a `ref` on a pathless `handoff` keys it
  (making six of the seven legal-as-written), or it does not (leaving them in the proto lane).
  One sentence either way; **the silence is the defect**."
- **(c)** Give `ledger` a reproducibility check of its own — "the denominated lanes agree with a
  stated derivation, not just with a grep."
- **(d)** "Consider whether the era rule should expire at all, or whether the proto lane simply
  drains away over time (it is already exempt from the key check)."

*(Grounding adds a fifth, from the `:25`/`:26` conflict above: **state which bullet wins.**
Recorded as a capture finding, not a ruling.)*

---

## Capture narrative — judgment calls made this arc (2026-08-20)

*This roadmap is the decision log; there is no separate `.decision-log.md`.*

1. **New arc, not an amendment.** No open roadmap existed in `skills/reports/` — Arc 8 shipped
   v0.11.0 on 2026-08-17 and closed 2026-08-18, and its roadmap is archived. Per Discovery's
   ship-day boundary rule, filings dated after Arc 8's ship belong to Arc 9. Arc number 9 =
   one past the highest existing arc.
2. **Scope: all uncaptured filings, owner-confirmed.** Three filings were uncaptured (verified
   by grepping each active `inbox/*.md` basename against `skills/reports/archive/`). The owner
   confirmed all three for this run; none deferred.
3. **A fourth filing was created during the run.** A9-4 carries an explicit capture-time
   instruction — "issue #1 should be materialized by hand at Arc 9 capture as the intake
   prototype" — recorded as a binding owner input from the 2026-08-19 problem-solving session.
   This run executed it: `gh issue view 1` fetched the body, and it was written to
   `inbox/2026-08-19-155515-tripwire-metrics-have-no-durable-vault-local-home.md` with an
   `origin: mggower/bmad-module-vlt#1` header, issue body unedited, then graded as A9-3. It is
   real uncaptured signal on its own merits, independent of the prototype role.
4. **A9-1's roundtable section was treated as authoritative over its own body,** per the
   filing's explicit instruction. Where grounding agreed with the body against the roundtable
   it said so (nowhere, this run); where the roundtable had already corrected the body (K11 vs
   the "falsified provenance" headline), grounding confirmed the correction rather than
   re-litigating it.
5. **Two claims were deliberately left ungrounded and are flagged as such**, rather than
   assumed: A9-3's B7-2-manifest analysis and its `vlt-upgrade` Step-3/Step-3.6 ordering trap.
   Both are claims about `vlt-upgrade` internals; verifying them properly is a brief-time act,
   and capture should not launder an unverified claim into a grounded one.
6. **K12 was not captured**, per its own owner ruling (multi-user trust model → vault-side
   question for app-vault's users). It is named in A9-1 only so it is not re-discovered.
7. **K13 was read as a build-time obligation, not a capture-time one.** This run did not read
   app-vault's or vlt-sayari's PARA trees; the harvest instruction is carried into the residual
   scope so the brief owes it.
8. **Arc 8's carry-forwards were not re-grounded.** B8-2 (4) (bound inherited debt, gating) and
   ruling 4c's three owner-filed candidates (defaulted to capture run 2) are named in the
   through-line for continuity. Their filings are separately uncaptured and belong to a later
   capture run — B8-2 (4)'s filing
   (`inbox/2026-08-18-101612-proto-deliver-era-test-names-no-datum-and-handoff-ref-slips-its-key-rule.md`)
   sits in `inbox/` and was **not** in this run's owner-confirmed scope.

### Capture run 2 (2026-08-20, same day) — and a correction to run 1

9. **Run 1's uncaptured-filing scan was wrong, and it under-reported by two.** Discovery in
   run 1 tested "is this filing captured?" by grepping each active `inbox/*.md` basename as
   free text against `skills/reports/archive/`. That produces **false positives**: a closed
   roadmap that merely *mentions* a filing — in an acceptance ledger, a carry-forward list, a
   root-cause note — matches the grep without ever having captured it. Two filings passed
   through that hole. Both are mentioned in Arc 8's roadmap; **neither is in its
   `derives_from`, and neither has a capture subsection anywhere.**
10. **The corrected test, used for run 2 and to be used hereafter.** A filing counts as
    captured iff it appears in some roadmap's **`derives_from:`** list **or** as a `### `
    capture-subsection heading. Both are the authoritative records the synthesis convention
    actually writes; free-text mention is not one. Under the corrected test the active inbox
    now has **zero** uncaptured filings.
11. **Run 1 also mis-stated the debt in its own routing line.** It closed by naming B8-2 (4)'s
    filing as owed to a run 2 — correct — *and* named ruling 4c's three lint-surfaced
    candidates alongside it, implying capture could pull them in. It cannot: Arc 8 recorded
    that bound as **MISSED**, meaning the filings were never written. **Corrected in the
    through-line and the routing line below** — those three are an owner action, not a capture
    backlog item.
12. **A9-6 was captured, not merely inherited.** Arc 8 grounded the *symptom* (the failed
    acceptance check) and routed the filing forward with "routes to the next `inbox-capture`."
    This run grounded the filing itself against `relay.md` and `ledger.md` as they ship today,
    which is what surfaced the `ledger.md:25`/`:26` precedence conflict neither Arc 8 nor the
    filing names.
13. **Two capture-time findings were added that no filing claims**, and both are labelled as
    grounding additions rather than filed claims: the `ledger.md:25`/`:26` rule conflict
    (A9-6) and the rule-card's unavailability as a host (A9-5). Capture may sharpen a claim's
    site; where it found something the filer did not, the roadmap says so explicitly so
    ideation can weigh it as this run's reading rather than field evidence.
14. **A9-5's reflex cap was corrected downward in confidence, not in substance.** The filing's
    "30/partner" is vlt-core's declared value, not a module constant
    (`vault-operating-contract.md:199` puts the cap in the file's own frontmatter). Recorded
    so no brief writes `30` into shipped text.

## Cross-filing joints (for ideation, not resolved here)

| Joint | Filings | Why it matters |
|---|---|---|
| **The overlay bell** | A9-2 Finding 5 ↔ A9-3 | Same defect from opposite ends. A durable local metric with no overlay-walking checker rings nothing; an overlay-walking checker with no durable metric has nothing to key on. **Neither half ships alone.** |
| **The `verified_by` sentence** | A9-1 K1b ↔ A9-2 Finding 1 | `write-verification.md:47` is the single line both filings need changed, for different reasons (out-of-path writers can't attest / vault-grown ops can't register). One edit, two filings. |
| **`frontmatter@8 → @9`** | A9-1 (C4 `grounding:`, `lifecycle:`) ↔ A9-2 (`local_consumers:`) ↔ A9-1 (retiring `type: resource`) | Three independent reasons to bump the same convention and re-ack seven-plus consumers. **Sequenced together = one bump; sequenced apart = three.** |
| **Ingress before intake** | A9-4 ↔ everything | Two of four filings originate on machines with no route into `inbox/`. Repo-side templates + labels must land before the factory-side intake step has anything to query. |
| **The overlay zone, unread and unchecked** | A9-2 Finding 5 ↔ A9-5 | A9-2: nothing *checks* `{overlays}`. A9-5: nothing *reads* it at activation. Same zone, two directions. A build that adds a bell without adding a read still leaves rules landing where partners never see them. |
| **The clobbered-host pattern** | A9-3 ↔ A9-5 ↔ A9-2 | Three separate vault-local additions with nowhere durable to live: a metric id (`vlt-vitals.py`), a fleet rule (`vault-rule-card.md`, `vlt-setup:146` — overwritten every update), a consumer registration (a pristine base). **Same defect, three hosts.** Worth asking whether one mechanism answers all three. |
| **Precedence, not just specification** | A9-6 | `ledger.md:25` and `ledger.md:26` are adjacent, overlapping, and unordered. Ruling the datum without ruling precedence leaves the conflict live. Ideation should order these two rulings. |
| **Boot-budget contention** | A9-5 ↔ the 2026-07-29 boot-cost filings | A9-5's own filer flags it: any new always-loaded read spends the budget those (already-captured, already-built) filings measured. A `{overlays}` read at Beat 1 is small but unmeasured. |
| **Location boundaries generally** | all five in-arc *(A19)* | The arc's thesis. Worth an explicit roundtable question: is the module's habit of drawing boundaries by *path* — and of siting durable state in module-owned files — the common root, and does any single build address it? |

---

## Ideation rulings — A9-1..A9-6 (owner-steered, 2026-08-20)

**Rulings below are the owner's; briefs cite this section, never re-litigate.** Session
**COMPLETE — filled 2026-08-20 over six owner-steered rounds.** Every slot is ruled. Two
rulings were **explicitly delegated to the clerk** by the owner and are marked as such (Q5's
repair shape; E1–E4's disposition). `build-brief` gates on this section being filled — it is.

**What each round settled.**

- **Round 1 — the arc's shape.** A9-1 leaves Arc 9 for **Arc 10** (it is the only filing whose
  brief cannot be written from module source); **no single durable-host mechanism** (the
  doctrine ships, the plumbing is per host); **A9-6 is build 1**.
- **Round 2 — the overlay cluster.** An overlay `consumers:` line is **not legal** (the base
  cuts no delegation); the route is **closed, not a fallback**; A9-5 takes **the fleet-wide
  rung only**; the cluster divides into **three builds** on a confirmed ordering constraint.
- **Round 3 — the gating build.** `:26` governs and `:25`'s population is **narrowed** so the
  overlap ceases to exist; the backward-compat exemption is **scoped to the key requirement**
  (discharging Arc 8's bound); `ref` on a `handoff` is **payload, never the key**; precedence
  becomes a **standing rule**.
- **Round 4 — the joints.** The `verified_by` value set **is** the consumer roster (one edit,
  two filings, one single-home violation removed); ingress divides into **rail then intake**;
  B9-1 gains the `resolving`/`on disk` clarification and its own **reproducibility instrument**.
- **Round 5 — sequencing.** Finding 4 **rides** the bell build; enforcement-ships-with-widening
  is **enshrined now** with an interim posture; ruling 4c is **re-bound with a hard gate**;
  build order **Y, ingress early**.
- **Round 6 — the tail.** **Two releases**; E1–E3 attach field-contingent and E4 becomes a
  watch; both spikes are **clerk-owned, factory-side**; the three standing rules land together
  in **B9-2**.

**One consequence is deliberately left OPEN for the roundtable** — D3's two-bump problem. See
*Roadmap roundtable*, joint 1.

Seeded from Arc 9 capture runs 1+2 (2026-08-20). Question numbering is the clerk's, for
reference in session only; it implies no ordering or priority.

### Grouping & order

**Arc scope, ruled Round 1 (2026-08-20): Arc 9 = A9-2, A9-3, A9-4, A9-5, A9-6. A9-1 is
excluded** — see *Capture's scope questions* below.

- **build-B9-1 — A9-6, the dispatch-ledger precedence conflict.** Ruled build 1, early and
  small (capture's scope question (c)). Independent of every other filing in the arc; touches
  `skills/vlt-dispatch/references/relay.md` and `.../ledger.md` only. Carries Arc 8's **bound,
  ship-verifiable, closeout-gating** re-check of B8-2 (4).

  *Scope, ruled Rounds 3–4 (2026-08-20) — **six items, all ruled**, plus a seventh added at
  the roundtable* *(roundtable A19: the lead-in said "four items, one unruled" while the list
  below held six — a brief written from the header alone would have scoped four and still read
  as compliant, in the one build whose declared purpose is that denominators be reproducible):*
  1. **Narrow `ledger.md:25`'s population** to exclude both legacy lanes (Q5). The overlap
     ceases to exist rather than being ordered.
  2. **Split `relay.md:28`'s dual grant** — exempt from the **key check** only; the lane is not
     finding-immune (Q4, discharging Arc 8's bound scope question). Applies to **both** lanes.
  3. **State the era datum** — "before the first `deliver` pointer exists in this record" —
     **including the no-`deliver`-at-all edge** (Q4).
  4. **`ref` on a `handoff` is payload, never the key** — one sentence at `relay.md:41`
     (Gap 2).
  5. **State both tests explicitly** (Round 4) — in `ledger.md`, "`resolving` under the handoff
     zone" is a **location** test and "no path **on disk**" is an **existence** test, and they
     are distinct. This clarifies what the module already does. ~~**no denominator moves.**~~
     **STRICKEN** *(roundtable A11, 2026-08-20 — Mary):* the claim is **unfalsifiable by the
     roadmap's own reading**, which says shipped text permits two constructions of `resolving`
     and that "two readers disagreeing on the denominator" is exactly what B8-2 (4) re-checks.
     Where two readings exist and **no incumbent behaviour has been measured**, "no denominator
     moves" names a baseline nobody has recorded — and the clerk's read is then adopted as
     incumbent **on assertion**, with the arc's one closeout-gating check verifying
     reproducibility **against the thing under repair**. **Replaced by an obligation:** B9-1's
     brief records, on the real vlt-core dispatch record, the **pre-fix denominator computed
     under both readings**, states which reading the fix adopts, and records **the measured
     delta**.
     *Unifying* them was rejected: it would change denominators on existing records — a
     behavior change with no filing behind it, in the build whose purpose is denominator
     reproducibility.
  6. **Candidate (c) — build the reproducibility check here** (Round 4). `ledger`'s denominated
     lanes verify **lane membership against a stated derivation**, not a grep. B8-2 (3)
     verified the counting *unit* against a fixture and structurally could not catch membership
     — the half that failed. This is the instrument that makes B8-2 (4)'s **ship-verifiable**
     tag mean something rather than discharging on a prose re-read; Arc 7's amendment A3 is the
     precedent.

     **⚠ THE "INHERITED C6-a FIXTURE DEBT" DOES NOT EXIST — CORRECTED.** *(roundtable A9,
     2026-08-20 — Amelia.)* C6-a was **captured as Arc 7's A7-1, built in B7-1**, and its filing
     sits in `inbox/archive/2026-08-01-143000-lint-fixture-stale-against-three-builds.md`;
     `uv run tools/test-package-lint.py` is **21/21 green** today. The roadmap was carrying a
     **discharged** debt forward. **The real obligation runs the other way and was unnamed:**
     `tools/package-lint.py:806-855` (`_e4_harness_coverage`, standing rule R2) *introspects* the
     check inventory by module-level callables matching `^(check_|_e\d+_)` — so **the moment
     element (6) lands as a gate check with no declaring case in `tools/test-package-lint.py`,
     E4 fails and the release gate blocks.** The fixture is not stale debt to work around; it is
     a **mandatory same-build deliverable**, and the brief prices that case as scope.

     **AND THE INSTRUMENT'S HOME IS RULED, NOT LEFT OPEN.** *(roundtable A10, 2026-08-20 —
     Amelia.)* The two available homes are **not interchangeable**: a self-verify paragraph in
     `ledger.md` (the shape its existing *Verify* section uses) is a **field** instrument that
     discharges only when a live vault runs `ledger`, while a factory-side check discharges **at
     rest**. The `[ship-verifiable]` tag on B8-2 (4) **is only true under the second.** So: **the
     instrument is factory-side and runnable at rest** — a fixture record plus a checker the
     builder runs against it; **a `ledger.md` *Verify* bullet alone does not satisfy element
     (6).** If the owner later prefers the field home, B8-2 (4) is re-tagged `[field-contingent]`
     in the same edit **and the arc has no gating check** — stated so the trade is visible rather
     than silent.

     **Accepted cost:** scope on the arc's smallest build.

  7. **Narrow `ledger.md:26`'s blanket immunity** *(roundtable A12, 2026-08-20 — Mary)*. Q4 and
     Q5 were ruled in the same round and **contradict each other in shipped text**: Q4 splits
     `relay.md:28`'s dual grant so the lane is exempt from the key check only and "remains
     eligible to be a finding for any unrelated reason", while Q5 elevates `ledger.md:26` — which
     carries the **same** blanket immunity, verbatim "reported as **counts, never findings**" —
     to governing. Items 1–2 amend `relay.md:28` and narrow `:25`, and **nothing touched `:26`'s
     blanket clause**: the arc would ship **Q4's cure on one file and Q4's disease on the other,
     with the diseased file ruled the winner.** Narrow `:26`'s "counts, never findings" to
     "**never a key-requirement finding**", mirroring Q4's split. The B8-2 (4) re-check's
     element (2) is extended to name **both** sites.

  *D5's precedence rule is **sited in B9-2** (Round 6); B9-1 is its **worked example, not its
  home**.* *(roundtable A19, 2026-08-20 — the bullet previously held D5 as an open "here or in
  its own build" question deferred to the wrong round, while the table and the Round-6 note gave
  it to B9-2. A `build-brief` run for B9-1, instructed to read "every ruling that names build
  N", could lawfully have pulled a governance edit **plus a handshake** into the arc's
  deliberately-smallest, closeout-gating build — defeating the stated reason it ships first.)*

- **build-B9-3 — A9-4 build A, the rail** (D4) — `.github/ISSUE_TEMPLATE/` + the label set +
  the `vlt-feedback` skill + the `module.yaml` transport URL, designed together as **one field
  contract**. The repo-side half is **not shipped surface** (no `skills/` presence, outside the
  own-the-apply copy surface, reaches no vault) and costs nothing in a release.
  **`binds:` D4 (build A), D6 (via A3), E1–E3, roundtable A13–A15, R1, R2.**

  **⚠ THE RAIL AS IDEATED DOES NOT REACH A VAULT — scope amended.** *(roundtable A13,
  2026-08-20 — the Agent Builder.)* "The `module.yaml` transport URL" **never arrives**:
  `module.yaml` is read only by `vlt-setup` (`SKILL.md:30,91`), and the only keys it exports
  into a vault's `config.yaml` are the four `_METADATA_KEYS` and **defined variables** —
  top-level keys whose value is a **dict** carrying `prompt`/`default`/`result`/`user_setting`
  (`scripts/merge-config.py`, `_VARIABLE_MARKER_KEYS`). **A flat `feedback_repo: <url>` scalar is
  neither, so `merge-config.py` silently drops it**, no shipped skill reads `module.yaml` at
  runtime, and `vlt-feedback` fires in a vault **with no transport.** → The transport URL is
  declared as a **defined variable** (a dict carrying at least `default:`), and the brief **names
  the `config.yaml` key `vlt-feedback` reads.**

  **Registration surface, omitted from the scope — added.** *(roundtable A14 — the Agent
  Builder.)* B9-3 invents a **shipped skill** and named only four items. It also owes
  `.claude-plugin/marketplace.json` `plugins[0].skills[]` **and** a quoted 13-field
  `module-help.csv` row. The first is caught late (package-lint **C5** fails the release on a
  `skills/vlt-*` dir absent from `skills[]`); **the second is not caught at all** —
  `check_group_b` validates header, field count and quoting and **never checks that each shipped
  skill has a row**. *A rail nobody's help surface lists is an ingress mechanism vaults cannot
  find, and lint exits 0.* (Standing rule **R2**.)

  **Two `[ship-verifiable]` checks, so the rail stops shipping ungated.** *(roundtable A14 —
  John; answers joint 6.)* (i) the issue-template field set and the `vlt-feedback` payload
  **agree**, verified by a real run against a fixture — the one failure the "design them
  together" ruling exists to prevent; (ii) `vlt-feedback` **detects and reports missing/unauthed
  `gh` with a named error** rather than failing obscurely. Both settle at the release gate.

  **A shaped artifact on transport failure — promoted from "the brief should consider" to
  scope.** *(roundtable A15 — Sally and Sophia, same finding from both ends.)* E3 discharges only
  on a run **from a work machine** — and the work machines are exactly the ones A9-4 says have no
  route into `inbox/`, so **if `vlt-feedback` fails there, the failure of the ingress cannot be
  filed through the ingress**, and a hand-opened issue carries **no labels and no origin vault**
  — precisely what capture proved about issue #1, and precisely what B9-5's "list open
  `vault-filed` issues" step is **structurally unable to query**. → On any transport failure,
  `vlt-feedback` writes the **fully-composed filing to a local file with the label names and
  origin-vault field pre-written, paste-ready**, and prints its path plus the manual route.

  **The field contract carries its own version stamp.** *(roundtable A15 — Victor.)* The sizing
  note that makes B9-3 look cheap is the same fact that breaks the contract: the two halves
  version by **different mechanisms at different rates** — the `vlt-feedback` half moves only
  when a vault runs `vlt-upgrade`; the `.github/` half is **unversioned repo HEAD** and changes
  for every filer at once — and the version-handshake covers neither. **A v0.12.0 install would
  keep filing against a template shape the factory has since re-cut, silently** — the exact drift
  D4 says splitting the halves would invite. → `vlt-feedback` writes the **contract version and
  `module_version` into the issue body**; repo-side templates are **additive-only**; B9-5's
  intake reads that stamp and **flags a stale-shape filing** instead of parsing it hopefully.

  **D6's test, run on the rail itself.** *(roundtable A3 — Victor.)* `vlt-feedback` **widens what
  may be written** — from a gitignored local directory that reaches nobody, to a **public tracker
  that reaches everybody, irreversibly** — and its only enforcement is a prose scrub-gate whose
  efficacy is explicitly untested (E2) and field-contingent. B9-3 therefore **records D6's
  result**: either the scrub gate becomes a real mechanism (a mandatory **rendered-payload
  preview the filer approves** before `gh issue create` — the approval-gate shape `vlt-groom`
  already ships), **or** B9-3 states an interim posture in shipped text (e.g. the rail is
  owner-machines-only until a gate exists).
- **build-B9-4 — A9-2 registration items** — `local_consumers:` added to the *Vault-writable
  declared fields* member set (`frontmatter.md:276`), the `frontmatter.md:82` → pointer fix
  (prose clarification, **no bump owed**), and Q3's `verified_by` value-set → consumer-roster
  edit (**`write-verification@2 → 3`**, re-acking all four consumers).
  **`binds:` Q1, Q2, Q3, D3/A22, D6 (via A3), roundtable A7, A18, R1.**

  **⚠ THREE BELLS, ADDED — the registration route would otherwise ship legal-and-invisible.**
  *(roundtable A7, 2026-08-20 — Sally, Dr. Quinn and Winston, three halves of one fault.)*

  1. **The overlay violation gets a name.** *(Sally.)* `vlt-lint` **already opens every**
     `{overlays}/{name}.overlay.md` in the *Overlay append-only* check (`checks.md:42`) — it
     inspects **section headings only**, so an overlay `consumers:` line passes clean. Add **one
     finding id** to that existing check: an overlay carrying a `consumers:`/handshake key flags
     **`overlay_consumers_illegal`**, legal response "register via `local_consumers:` in the
     base". Plus **one line in `vlt-upgrade`'s reconcile report** naming the retirement, so
     vlt-core's live owner-adopted line does not simply become illegal in silence. **No new
     walker, no new build.**
  2. **The exemption gets priced instead of granted.** *(Dr. Quinn.)* `local_consumers:` joining
     the *Vault-writable declared fields* set means its local value is **excluded** from
     `vlt-lint`'s base-divergence check and `vlt-upgrade`'s pre-flight — **that is the section's
     defining property.** So the fix as ideated converts a vault-local consumer registration from
     *detected-but-homeless* (today it trips `base_divergence`) into **legal-and-invisible**, with
     the only guard being prose. *That is this arc's thesis executed against the arc's own
     repair.* → Each `local_consumers:` entry must be **backed by a live `ref:`-keyed mint entry
     in `_agent/mint/decision-log.md`** — the sanctioning pattern `frontmatter.md` already
     requires of a vault-originated local convention — and an **unsanctioned entry is a
     `vlt-lint` finding.** Reuses a shipped mechanism; gives Q3's roster-ceiling mitigation a
     **mechanical** form.
  3. **The stale-ack alarm actually fires.** *(Winston.)* None of B9-4's ideated items **makes
     any checker read `local_consumers:`**. The *Convention coherence* check
     (`vlt-lint/references/checks.md`) walks `{conventions}/*.md` carrying `version:`/`consumers:`
     and reads **listed consumer** skills' `depends_on:` — a roster `local_consumers:` is not
     part of. v0.12.0 would ship a vault-grown op a lawful way to register and **still no
     stale-ack alarm** — the exact defect A9-2 Finding 2 filed, evidenced by `vlt-sweep` pinning
     `frontmatter@7` against a base at `version: 8`. → Extend *Convention coherence* to walk
     `local_consumers:` with the same stale/unacknowledged vocabulary as `consumers:`, and state
     the dangling test for a vault-local registrant. **One bullet in `checks.md`.**

  **D6's test, run on B9-4 itself.** *(roundtable A3 — John and Sally.)* B9-4 **is a widening** —
  a new vault-writable field whose values are arbitrary op names, plus a `verified_by` value set
  that becomes open-ended — shipped in the **same release** that enshrines D6. Without the bells
  above it would be **the arc's second build standing as the counter-example to the arc's own new
  rule.** With them, D6 is satisfied by a **named bell**; if any part slips, B9-4 states the
  interim posture in shipped text at `write-verification.md` instead (*"a `local_consumers:`
  registrant must be a write op; unenforced until the registration check ships"*) — and says
  which, at brief time.
- **build-B9-6 — A9-3 durable metric home + A9-2 Finding 5 (the overlay bell) + Finding 4**
  (per-section enforcement addressing, D3) — **S3-gated.** Carries a `frontmatter` bump; D3's
  ⚠ consequence is **RESOLVED at the roundtable — (i), two bumps, reason recorded (A22).**
  **`binds:` D2, D3/A22, Q9/A4–A6, S3, *The cluster's build division* item 2, the brief-time
  A9-3 direction question, roundtable A21.**
  *(roundtable A19: none of D2, Q9 or the cluster-division item **names B9-6**, so a briefer
  obeying `build-brief` Discovery literally — "every ruling that names build N" — would have
  missed the ordering constraint that ships the checker against a metric home that does not
  exist. Hence the `binds:` roster.)*

  **⚠ THE FILER'S FLOOR IS RE-ADMITTED.** *(roundtable A21, 2026-08-20 — Maya; owner ruled it
  lands.)* Issue #1 offered three directions and asked, "**at minimum, make the loss legible**" —
  a diff before overwrite and a line in the Confirm summary. Ideation ruled direction 3 "**not a
  fix**", which is correct **as a build choice for the D2 joint** — and it deleted the filer's
  floor rather than deferring it. Direction 3 is **additive and cheap**, and it is the only thing
  that helps the vault losing its derive function on **every upgrade between now and v0.13.0** —
  a release gated on a spike that may itself file a new defect. → **"Make the clobber legible at
  upgrade time" attaches to a v0.12.0 build as a floor**, and the brief-time question becomes
  choosing between directions 1 and 2 ***on top of it***, not instead of it.
- **build-B9-7 — A9-5 fleet-wide rung** — a vault-scoped `reflexes.md` sibling in the agent
  zone, pointer lines only. **S2-gated (re-scoped).**
  **`binds:` Q8 (+ roundtable A17, A21), D1, S2, R1.**
  **Scope additions at the roundtable (A17):** minting or amending an overlay **writes its rung
  pointer line in the same act**; a fleet-relevant reflex **promotes to the rung**; the brief
  carries a **falsifier** for the pointer shape; **S2's negative branch is pre-ruled** (Beat 1
  read reinstated as fallback, or a stated interim posture naming the unprotected moment).
  **R1 applies:** if the build touches `vault-operating-contract.md` it **re-derives
  `vault-rule-card.md`** and re-checks the 8,000-byte budget — a **second, independent C6 gate**
  in a different release from B9-2's.
- **build-B9-5 — A9-4 build B, the intake** (D4) — `inbox-capture` Discovery +
  `arc-closeout` Stage 5 + the `origin:` header single-home.
  **Ordered after B9-3** (structural: no labels exist to query until B9-3 lands).
  **`binds:` D4 (build B), E1–E4, roundtable A15, A16.**

  **⚠ B9-5 IS FACTORY-ONLY AND IN NO RELEASE.** *(roundtable A16, 2026-08-20 — the Agent
  Builder.)* **Every one of its three deliverables is untracked**: `.claude/` and `inbox/` are
  both gitignored (`.gitignore:10,15`, verified by `git check-ignore` on
  `inbox-capture/SKILL.md`, `arc-closeout/SKILL.md`, `inbox/README.md`). **B9-5 produces no
  commit, no release content and no package-lint coverage** — a factory-local edit reaching no
  vault and no git history. The release table and the v0.12.0 rationale are corrected
  accordingly.

  **The `origin:` header's single home moves into the shipped half.** *(roundtable A15 —
  Paige.)* Ideation sited it in `inbox/README.md` — **which `.gitignore` excludes from the repo
  entirely** (`git ls-files inbox/` returns nothing) — so the one **shipped** producer of that
  header, `vlt-feedback` in a field vault, **can never read its own contract's home**, and
  neither can any contributor arriving through the public rail. The other half of the same field
  contract lives in `.github/ISSUE_TEMPLATE/`, declared "not shipped surface" — outside
  `skills/`, the SHA manifest, package-lint and every handshake. **A three-site field contract
  whose single home is invisible to two of the three** — joint 2's fault reappearing in the
  ingress build. → **State the header shape once in `vlt-feedback`** (which produces it, ships
  into vaults and rides the skill-asset manifest); `inbox/README.md` and the issue template
  become **pointers**. The siting decision moves to **B9-3's brief**, with B9-5 citing it, so
  **one build owns the whole field contract.**

  **A decline state, and an idempotence key.** *(roundtable A15 — Victor and the Agent
  Builder.)* As ideated the arc gives the factory **an ingress with no decline state**: B9-5
  materializes open `vault-filed` issues into `inbox/`, and the moment a file lands there the
  lifecycle map's first row makes it uncaptured field signal that `inbox-capture` **must** ground
  and fold into the open arc — while GitHub issue templates apply their `labels:`
  **automatically**, so **any stranger filling in the form mints a mandatory, hand-grounded
  capture obligation for a one-person factory.** And nothing rules the label's **state
  transitions**: `arc-closeout` Stage 5 archives a filing only once its build shipped *and*
  passed acceptance, which routinely spans arcs, so a `vault-filed` issue stays open and labelled
  across arcs and **B9-5's Discovery re-materializes it on every intervening capture run.** →
  **(a)** materialization is triggered by an **owner-applied triage label** — the template's
  `vault-filed` marks **candidacy, not admission**; **(b)** a terminal **`declined`** disposition
  exists (issue closed with a reason, nothing written to `inbox/`); **(c)** a **capture-state
  label** (`vault-filed` → `captured`) is applied at materialization; **(d)** Discovery
  **excludes any issue whose `origin:` already appears under `inbox/` or `inbox/archive/`.**
- **build-B9-2 — the three standing rules** (Q9 doctrine / D5 precedence / D6 widening) —
  ~~one governance-bundle edit~~ → **three sitings under one build, split by audience**
  *(roundtable, Dispute 2, 2026-08-20 — Paige's siting, owner-ruled)*:
  **`binds:` Q9/A4–A6, D5, D6/A1–A2, roundtable Dispute 2, A11, R1.**
  - **D5 (precedence) → project `CLAUDE.md`, *Standing rules*.** Not shipped: its audience is the
    **factory**, and a vault may only file such a change (`vault-operating-contract.md:104`/`:105`).
    **No handshake.**
  - **Q9 (durable-host doctrine) → `vault-operating-contract.md`, *Durability across upgrades***
    (`:88-105`), shipped with a **real enforcement declaration** (`enforcement_stage: checked`,
    `enforcement_checked_by: vlt-upgrade`) per A5. **No bump — but R1 applies: re-derive
    `vault-rule-card.md` and re-stamp its `derived_from:` sha256 or package-lint C6 blocks the
    tag; act-blocking clauses claim card budget (5,937 / 8,000 today).**
  - **D6 (enforcement-ships-with-widening) → `frontmatter.md`, *Enforcement declaration*.**
    **Bumps `frontmatter.md` and re-acks all nine consumers — folded into B9-4's already-bought
    walk, so the arc pays two bumps, not three.**

  **One conformance line, from joint 5.** *(roundtable A11 — Sally.)* B9-1 and B9-2 ship in the
  same release, so the field meets D5's rule and its worked example together — **but nothing
  binds them**: B9-1's narrowing ships before D5's rule text is authored. → **B9-2's brief
  re-reads B9-1's shipped `ledger.md`/`relay.md` narrowing against the rule text as authored and
  cites it as the rule's worked example** (or fixes whichever diverged). A ship-verifiable check,
  not a re-brief.

**Build order — ruled Round 5, renumbered Round 6 (2026-08-20): ordering Y, "ingress early".
SEVEN builds.**

| # | Build | Filing | Gate | Release |
|---|---|---|---|---|
| **B9-1** | the dispatch-ledger repair | A9-6 | — (**gates closeout**) | v0.12.0 |
| **B9-2** | the three standing rules | Q9 / D5 / D6 | — | v0.12.0 |
| **B9-3** | the rail | A9-4 (D4 build A) | — | v0.12.0 |
| **B9-4** | consumer registration | A9-2 | — | v0.12.0 |
| **B9-5** | the intake | A9-4 (D4 build B) | after B9-3 | **factory-only — no release** *(A16)* |
| **B9-6** | durable metric + overlay bell + Finding 4 | A9-3 + A9-2 | **S3** | v0.13.0 |
| **B9-7** | the fleet-wide rung | A9-5 | **S2** | v0.13.0 |

*Why ordering Y.* It front-loads everything not spike-gated, so **S2 and S3 run in parallel
with real building** rather than stalling the arc — and it stands the remote filing rail up
**earliest**. That is not cosmetic: two of this arc's six filings originated on machines with
no route into `inbox/`, and every arc after this one benefits from the rail existing sooner.
Ordering Z (cluster-contiguous) reads cleanest but stacks both spike-gated builds mid-arc,
stalling the arc with unblocked work queued behind them.

*Why B9-2 is its own slot and not folded into B9-1* (Round 6). The owner ruled the three
standing rules land **together, early, in one governance edit** — at most one handshake, and
early enough to govern the arc's own later builds. The clerk sited them in **their own slot**
rather than in B9-1: B9-1 is deliberately the arc's **smallest** build and already carries six
scope items plus the closeout gate, and loading three standing rules and a possible handshake
onto it defeats the reason it ships first (capture's scope question (c)).

**Release contents — ruled Round 6 (2026-08-20). Two releases.**

**⚠ ARC CLOSEOUT BINDS TO v0.12.0.** *(roundtable, Dispute 3, 2026-08-20 — John's finding, owner
ruled.)* `arc-closeout` Stage 1's precondition is written against **one** release version per arc
("the tag for the arc's shipped version must exist"); Arc 9 declares two, and nothing said which
one closeout binds to — so **if S2 or S3 never closed, v0.13.0 would never ship, no tag would
exist, and the arc would be unclosable indefinitely with five builds already in the field.**
→ **Closeout gates on v0.12.0's tag.** **B9-6 and B9-7 are release-forward candidates**: if their
spike has not closed by a date the brief names, they **fold to Arc 10 unbuilt** and the arc
closes on v0.12.0's ledger. Precedent: **Arc 3 → build-17 → Arc 5**, already in module history.

**⚠ THE LEDGER PARTITIONS BY RELEASE, AND A v0.12.0 UPGRADE RUN IS AN OBLIGATION.** *(roundtable
A20, 2026-08-20 — John.)* The stated payoff for splitting the release is that **acceptance starts
earlier** — but the ledger was **not partitioned by release** and nothing obliged an upgrade run
at v0.12.0. If the owner upgrades vlt-core once, **0.11.0 → 0.13.0**, the split buys nothing it
was ruled in to buy while still costing two release choreographies. → The live-acceptance ledger
splits under **"Discharges on the v0.12.0 run"** / **"Discharges on the v0.13.0 run"**, and **a
vlt-core upgrade run at v0.12.0 is an obligation of the split, not an option.**

**⚠ E1 AND E3 NAME THEIR DISCHARGING EVENT, OR THEY ARE NOT DEBTS.** *(roundtable A20 —
Victor.)* Live acceptance is an owner `vlt-upgrade` run and the primary acceptance vault is
**`vlt-core`, on the factory machine** — the one install with a filesystem route into `inbox/`
and **the one place the rail's cross-machine assumptions cannot be exercised.** A debt whose
discharge requires an event nothing in the plan schedules is **precisely the shape that produced
the four-arc A4-4 (5) debt and ruling 4c's two-arc miss** — and this arc was shipping its most
consequential build with two of them. → E1's and E3's ledger entries **name their discharging
event explicitly — a successful `vlt-feedback` run from the work machine's app-vault** — bound as
an **owner action with a stated arc bound**, the same hard-gate mechanism A8 applies to ruling
4c. *A rail nobody has filed through from a second machine has not been accepted.* (Standing rule
**R5** in the record below.)

**Release-commit surface note** *(roundtable A16)*: `.github/` **is tracked** yet sits outside
`CLAUDE.md`'s enumerated release-commit surface (`skills/`, `.claude-plugin/`, `tools/`, README,
LICENSE). B9-3 extends that surface; the release commit will contain it.

- **v0.12.0 — B9-1..B9-4**, everything not spike-gated **that ships** (B9-5 is factory-only —
  see A16). Ships the arc's closeout-gating repair, the three standing rules, and **the rail**;
  **the intake lands factory-side in the same window** *(roundtable A16 — corrected from "the
  complete ingress loop as one usable thing", which B9-5's untracked deliverables cannot
  deliver)*. Field acceptance on the rail starts here rather than waiting on the arc.
  **This is the release arc closeout binds to** (Dispute 3).
- **v0.13.0 — B9-6, B9-7**, once S3 and S2 close.

*Why not one release:* the whole arc would wait on both spikes, and no field acceptance would
start until everything landed. *Why not the build-order split (B9-1..B9-3 / B9-4..B9-6):* it
puts the rail in the field in one release with **nothing consuming it** until the next.

*Both releases carry the standing release contract:* dual version bump
(`.claude-plugin/marketplace.json` `"version"` + `skills/vlt-setup/assets/module.yaml`
`module_version`), `uv run tools/package-lint.py --expect-version X.Y.Z` **exit 0 before
tagging**, and the PASS summary line in the release commit message.

#### Capture's scope questions — ruled Round 1 (2026-08-20)

**(a) Is the clobbered-host pattern (A9-2 / A9-3 / A9-5) one mechanism or three?**
→ **Not one mechanism.** See Q9.

**(b) Is A9-1 one arc-spanning build sequence or an arc of its own?**
→ **An arc of its own — Arc 10.** A9-1 leaves Arc 9 entirely.

*Owner's reasoning, on the clerk's read:* A9-1 is the only filing in the arc whose **brief
cannot be written yet**. S1 is an explicit read-the-field-before-writing-contract-text
obligation over two live vaults (`app-vault`'s two `projects/<slug>/index.md`, 33K and 10K;
`vlt-sayari`'s 210 candidate instances). Every other filing was groundable from module source
and capture already grounded it. Folding A9-1 in makes the whole arc wait on a harvest.

*Declared price of the split, accepted:* **two** `frontmatter@8 → @9` bumps and two
seven-plus-consumer walks instead of one — Arc 9 bumps for A9-2's `local_consumers:`, Arc 10
bumps again for A9-1's `grounding:` and the `type: resource` retirement. This was the only
cost the room could find, and it is paid knowingly. See D3.

*Consequential re-scoping — the following move to Arc 10 with A9-1 and are NOT ruled here:*
Q6 (`projects: workspace` posture), Q7 (`resources/` retirement + wiki move), D7
(`grounding:` inheriting the personalized-extraction firewall check family), S1 (the PARA
container harvest), E5 (the `grounding:` laundering watch), E6 (K16, the attestation-census
pattern), and four of the brief-time questions (`areas/`-as-ideation-home, per-type PARA
`status:` enumeration, the project-to-project relation, `capability-template.md:23`).
**Q3 survives in Arc 9** — it was a joint, and A9-2's half still needs it.

*Amendment owed — narrowed* *(roundtable A19, 2026-08-20)*: the `intent:` frontmatter **was**
re-written for the post-Round-1 arc, so that half is **discharged**; the prose a human reads
first (*The through-line*) was not, and is amended above. **What remains owed is only this:**
A9-1's paragraph moves to the Arc 10 roadmap when that opens. *(The note previously declared the
discharged obligation open and left the two undischarged ones reading as covered by it.)*

**(c) Does A9-6 ship early and small, or wait on the roundtable with everything else?**
→ **Early and small — build B9-1.** It gates closeout, it is bound, and it touches two
reference files nothing else in the arc touches. Shipping it late would expose the arc's one
gating check to schedule pressure — the failure mode Arc 8 hit with ruling 4c.

**Capture's unaccepted material, carried for the session — NOT rulings.** The capture recorded
these as its own reading; they are on the table as input, not as accepted groupings:

- Capture's three scope questions from the routing line: **(a)** is the clobbered-host pattern
  (A9-2 / A9-3 / A9-5) one mechanism or three builds? **(b)** is A9-1 one arc-spanning build
  sequence or an arc of its own? **(c)** does A9-6 ship early and small, or wait on the
  roundtable with everything else?
- Capture's residual-scope lists per filing (A9-1 items 1–8; A9-2 items 1–5; A9-5 items 1–2)
  are decomposition *material*, not proposed builds.

### Pre-ideation rulings the capture demanded

*Each of these was flagged during capture as needing an owner ruling before a brief can be
written.* **All ten are ruled** *(roundtable A19 — the lead-in still said "All unanswered").*

**Q1 — Is an overlay `consumers:` line legal at all, under the operating contract's carve-out
test?** (A9-2.) vlt-core's four-lens council **split**: the architect argued legality on
monotonicity; the skeptic and historian read `vault-operating-contract.md:101`'s own test as
unsatisfied. The vault adopted the extension on the user's ruling and **recorded the legality
as unsettled**. Capture's note: a module cannot leave a live install in that position.
→ **NOT LEGAL. Settle it in the base.** (Round 2, 2026-08-20.) The skeptic and historian are
upheld; the architect's dissent is recorded below.

*The test, quoted in full because capture cited it without quoting it.*
`vault-operating-contract.md:101`: "**An overlay may occupy a carve-out the base names in its
own words.** This is legal exactly where *(a)* the base rule itself cuts the delegation
('unless a specific schema says otherwise') and *(b)* the overlay names the exact schema it
occupies and scopes narrowly to it… **An overlay claiming a carve-out the base never cut is a
base-rule change in disguise and routes per the base-rule-change bullet below.**"

Test **(a)** asks whether the *base* cut a delegation. `write-verification.md:47` declares the
`verified_by` set as a flat closed enumeration and the whole *Attestation* section (`:42-47`)
carries no delegation clause, no extension mechanism, no carve-out language. **(a) is
unsatisfied on the plain text.** The architect's monotonicity argument reasons about (b)-shaped
harm and never engages (a) — **recorded as the dissent**, not as an error.

*Three consequences the ruling carries, each grounded this session:*

1. **The contract names the remedy in the same bullet.** An uncut-carve-out overlay "routes per
   the base-rule-change bullet" — `:105`: the change "is **generic** and belongs upstream (file
   it to the module)." **vlt-core's filing *is* the contract-compliant response.** The vault
   acted lawfully at the module level and unlawfully at the local level, simultaneously. The
   local adoption is retired when `local_consumers:` ships; no grandfather clause is granted.
2. **A second route exists and does not solve this one.** `vault-operating-contract.md:102` —
   a *sanctioned local convention* carries its own `version:`/`consumers:`, discovered by
   scanning `{conventions}`, explicitly "outside the version handshake." That is a legal home
   for a vault-grown op to declare **what it consumes**. A9-2's need is the reverse direction —
   registering against a **shipped base's** roster so the stale-ack alarm fires. Recorded so it
   is not rediscovered as a missed option.
3. **`local_consumers:` is the contract's own prescribed shape, not an invention.**
   `vault-operating-contract.md:104`, the designed-parameter-read veto: "**parameters yes** (a
   designed read, filed upstream if the skill lacks one), **content yes**…, **new behavior by
   mint**, **skill text no**." Making the consumer roster extensible by a vault-writable
   declared field is exactly *parameters yes, filed upstream*. This materially strengthens
   `local_consumers:` against its alternatives and should be cited in the brief.

**Q2 — If `local_consumers:` lands, does the overlay registration path stay legal as a
fallback, or is it closed?** (A9-2.) → **CLOSED. One route.** (Round 2, 2026-08-20.)
`local_consumers:` is the only registration path; the overlay route is not a fallback, because
under Q1 it was never open.

**⚠ Carried tension, taken to the roundtable.** The owner declined the
*closed-with-a-named-error* variant, so the arc as ideated ships a **boundary with no bell**:
nothing detects an overlay `consumers:` line and points the vault at `local_consumers:`.

**→ CLOSED AT THE ROUNDTABLE. The bell costs one finding id, not a mechanism.** *(roundtable
A7, 2026-08-20 — Sally; this **refutes joint 2's premise**, recorded as died at the table.)*
`vlt-lint` **already opens every `{overlays}/{name}.overlay.md`** in the *Overlay append-only*
check (`checks.md:42`, ids `overlay_not_append_only` / `overlay_orphan`) — that check inspects
**section headings only**, so an overlay `consumers:` line in frontmatter passes clean. **The
missing detector is one finding id inside a check already walking the exact file.** And the
stakes were higher than "no bell": Q1 consequence 1 retires vlt-core's live, owner-adopted
overlay `consumers:` line **with no grandfather clause**, so at v0.12.0 a real vault's extension
becomes illegal on disk with nothing reading it, nothing flagging it and no upgrade-time notice
— **the operator's entire experience of the ruling would be that nothing happens.** The full
three-part cure is in **B9-4's scope**; see there.

**Q3 — Does the base name a delegation carve-out for the `verified_by` value set, and in what
form?** (A9-1 K1b + A9-2 Finding 1 — the same sentence, `write-verification.md:47`, needed by
two filings for different reasons.) → **YES — AND THE VALUE SET *IS* THE CONSUMER ROSTER.**
(Round 4, 2026-08-20.) `:47`'s enumeration is replaced by a pointer: the `verified_by` value
set is `write-verification.md`'s `consumers:` plus `local_consumers:`.

*The grounding that produced this shape, found this session and not by capture.* The two sets
are **the same four names, written twice**:
- `write-verification.md:12` — `consumers: [vlt-ingest, vlt-extract, vlt-research, vlt-lint]`
- `write-verification.md:47` — "the three write ops (`vlt-ingest`, `vlt-extract`,
  `vlt-research`) plus `vlt-lint`"

`:47` is therefore **a single-home violation of exactly the shape A9-2's Finding 3 catches at
`frontmatter.md:82`** — capture found the pattern in one file and missed it in the other. The
carve-out did not need inventing; the duplication needed removing.

*What the one edit buys:* it deletes a duplicated enumeration; it gives A9-2's vault-grown op a
lawful attestation route the moment it registers; it satisfies Q1's test (a) by having the base
cut the delegation explicitly and narrowly.

**⚠ IT DOES *NOT* MAKE K1b "ALREADY-SOLVED" — CORRECTED.** *(roundtable A18, 2026-08-20 —
Maya.)* Ideation recorded this joint as discharged; **it is not.** Q3 buys a lawful attestation
route for **vault-minted write ops only**. The writer that produced app-vault's 0-of-56
unattested PARA files is **a partner writing in its own sitting** — `vlt-agent-creative` and kin
— **not a registered op**, and no `local_consumers:` line admits it. After B9-4 ships, **the
census still has no lawful response, which is the whole of K1b.** K1b's out-of-path **partner**
writer is recorded as **carried to Arc 10, not solved**. The "one edit, two filings" joint is
real for A9-2's half and **half-real** for A9-1's.

**Two caveats the brief must carry.**
1. **Per-consumer narrowing survives.** `:47` continues: "lint attests **narrowly** — it writes
   the pair only on files its own auto-fix touched… Lint never attests a file it merely read."
   The roster is *membership*; per-consumer scope stays stated where it applies.
2. **Over-admission is the one real risk.** A future consumer that *reads* the convention
   without writing would be admitted as a legal attester. All four write today, so the identity
   holds — but it is not guaranteed to. **Mitigation, ruled in:** the roster is the **ceiling**,
   and a `local_consumers:` registrant must be a **write op** to attest.

   **⚠ THE MITIGATION DID NOT COVER THE VECTOR IT WAS WRITTEN TO CLOSE — AMENDED.** *(roundtable
   A18, 2026-08-20 — Mary.)* The "same four names, written twice" identity is an **extensional
   coincidence at n=4, not an identity**: `consumers:` is version-handshake membership (who acks
   a version), `:47` is attestation authority (who may write `verified_by`). Making the
   coincidence definitional in shipped text means **any skill later added to `consumers:` for
   handshake reasons silently acquires attestation authority** — and the ruled mitigation
   constrains only the **local** extension, not additions to the **base** roster. **State the
   write-op qualifier on the whole set in shipped text**, not on local registrants alone:
   > *the `verified_by` value set is `write-verification.md`'s `consumers:` **that are write
   > ops**, plus write-op `local_consumers:`.*

   B9-4's brief cites the base roster **as constrained by that qualifier** when it re-acks.

**⚠ A handshake bump D3 has not been counting.** This is a base rule change to
`write-verification.md`: **`version: 2 → 3`, re-acking all four consumers.** That is a *second*
handshake, separate from `frontmatter@8 → @9`. Both land in the same build (A9-2's registration
build), which is efficient — but **the brief prices two handshakes, not one**, and verifies
bipartite consistency for both.

**Q4 — What is the backward-compat exemption's *scope*?** (A9-6, **bound by Arc 8**.) Arc 8's
hand-off requires Arc 9 to rule on the exemption's scope, not only its datum — read strictly it
would have suppressed the very finding whose repair discharged B8-1 (5) and B8-2 (5). Capture
adds that `relay.md:28` grants the exemption to **two** lanes at once, and the over-breadth
question applies to both. → **SCOPED TO THE KEY REQUIREMENT. Datum = candidate (a).**
(Round 3, 2026-08-20.) **Arc 8's bound is discharged by this ruling.**

*Where the over-breadth actually lives, located this session.* `relay.md:28` grants the lane
**two things in one sentence** and treats them as one grant: "exempt from the key check" **and**
"never as a finding". They are not one grant. The first is narrow and correct; the second is a
**blanket finding-immunity with nothing to do with keys** — and it is the half that would have
suppressed B8-1 (5)/B8-2 (5)'s finding.

*The ruling.* The exemption covers the **key requirement only**. A proto-`deliver` (or legacy
pre-shape) pointer stays exempt from the key check and stays a denominated count, and **remains
eligible to be a finding for any unrelated reason**. This is the narrowest cut that survives
Arc 8's objection without weakening either lane, and it applies to **both** lanes as capture
required. It composes with Q5: `:26` governs `:25` because both address the key requirement —
and *only* there.

*The datum.* Candidate (a): **"before the first `deliver` pointer exists in this record."**
Per-record, derivable at read time, requires no version knowledge — no defect found against it.

**Edge the brief must close, not leave to the reader: a record containing no `deliver` pointer
at all.** The natural reading makes every shape-annotated pathless pointer in that record
proto-`deliver` — the lane at its broadest exactly where evidence is thinnest. Defensible (the
feature demonstrably never ran in that record), but **it must be stated in `relay.md:28`**, not
inferred.

**Q5 — Which of `ledger.md:25` / `ledger.md:26` wins?** (A9-6, capture-added.) The two adjacent
bullets claim the same population with no precedence rule. Capture's warning, recorded in the
acceptance ledger: a re-check that states the datum but leaves these un-ordered will pass on
paper and fail in the field again. → **`:26` GOVERNS — and `:25`'s population is narrowed to
exclude both legacy lanes, so the overlap ceases to exist.** (Round 3, 2026-08-20.)

*Ruling provenance:* the owner leaned to this option and **explicitly delegated the call to the
clerk**; the clerk's lean was the same. Recorded as an owner ruling on a delegated call, with
the reasoning below on the record rather than asserted.

*Why `:26` and not `:25`.* `relay.md:28` already answers it categorically and capture never
cited it as an answer: the proto lane is "exempt from the key check, reported by `ledger` as a
denominated count …, **never as a finding**." `:26` is downstream of a rule `relay.md` states
without hedge. Ruling `:25` the winner would require amending `relay.md:28` as well.

*Why narrow the population rather than add a precedence sentence.* A precedence sentence is a
rule **about** rules — it works only if the reader holds both bullets and an ordering at once.
Narrowing `:25` means **a reader who reads only `:25` gets the right answer**: the fix lives
where the defect is, which is the module's own point-of-use discipline. An ordering sentence
leaves the overlap live in shipped text, and a rule whose only mechanism is "the reader
remembers" is the decay this arc exists to name. It is also the same failure shape B8-2 (4) is
a re-check for.

**⚠ RULING OWED — a fourth defect in the same two lines, found this session, not by capture and
not by the filing.** `:25` says "no path **on disk**"; `:26` says "**pathless**", which `:28`
defines as carrying no key-path "**resolving under the handoff zone**". Those are two different
tests — **location** vs **existence** — and the module never says so. A pointer with a written
path that does not exist is *no path on disk* but **not** pathless; a pointer with no link at
all is both. The module's own usage distinguishes them (it would not have written "on disk"
otherwise), but `resolving` does double duty and reads either way. **Under one reading the
bullets overlap on two populations, under the other on one — so a fix that states precedence
but leaves `resolving` ambiguous still leaves two readers disagreeing on the denominator**,
which is exactly what B8-2 (4) re-checks. Carried into B9-1's scope as an **unruled item**;
the clerk's read is that `resolving` means *syntactic location* and `on disk` means
*existence*, and that both should be said. **Ruled in Round 4, not assumed here.**

**Gap 2 — what does a `ref` on a `handoff` mean?** → **PAYLOAD, NEVER THE KEY.**
(Round 3, 2026-08-20.) One sentence, reusing `relay.md:26`'s own shipped vocabulary (a wikilink
in any shape's pointer is "payload, never the key"), preserving `relay.md:41`'s "a `handoff`
keys on its **doc path** exactly as it always has."

*Why not let it key.* Letting `ref` key a `handoff` gives one shape two possible keys — and
`:41`'s own warning is that key ambiguity "disables the spam guard **invisibly**: the guard's
absence is indistinguishable from the guard passing."

*Accepted cost.* The six pointers stay in the proto lane rather than becoming legal-as-written.
Both lanes are counts-never-findings and `vlt-decay` drains them, so the cost is near-zero —
and it is the direction candidate (d) gestures at.

**Q6 — `projects: workspace` as a shipped default vs opt-in.** (A9-1 body, flagged "not
assumed".) The filing's own roundtable ruled the posture axis **moot** (bounded/unbounded is
the axis) — the owner should confirm that disposition stands rather than let capture assume it.
→ **DEFERRED TO ARC 10** (Round 1, 2026-08-20) — A9-1-only; travels with the filing.

**Q7 — Does `resources/` retire, and does the wiki move into it?** (A9-1, R-d + K14.) Ruled in
the filing's roundtable; capture found the mechanical cost **materially understated** — not one
`vault_structure` entry but two (`wiki`, `index`), plus PARA paths that are not designed
parameters at all, plus a `type:` value retirement that forces `frontmatter@8 → @9`. Owner to
confirm the ruling **against the true cost**. → **DEFERRED TO ARC 10** (Round 1, 2026-08-20)
— A9-1-only; travels with the filing, and its true cost is Arc 10's to budget.

**Q8 — Beat 1 `{overlays}` read, fleet-wide rule rung, or both?** (A9-5.) The filing offers both
and resolves neither, explicitly marking its provenance guess as a guess. Capture **ruled out**
one of its two candidate homes: the rule-card is module-owned and overwritten every update
(`vlt-setup:146`). → **THE FLEET-WIDE RUNG ONLY.** (Round 2, 2026-08-20.) The Beat 1
`{overlays}` read is **not built this arc.**

*Shape:* a **vault-scoped sibling of `reflexes.md`**, living in the agent zone — durable by
construction, so it needs **no new durable-host mechanism** and is consistent with Q9. It
reuses a shipped shape rather than inventing one: `vault-operating-contract.md:199` already
defines the always-loaded rule layer as "one line per rule, hard-capped," with the cap, its
falsifier, and its enforcement posture declared **in the file's own frontmatter**. The rung is
that file, vault-scoped instead of per-partner.

*Why this over the read.* Beat 1 (`vault-operating-contract.md:167`) is the **identity** layer
— persona, `identity.md`, `reflexes.md`. An `{overlays}` read puts convention *content* at the
identity beat. The rung also directly answers A9-5's gradient claim: fleet-relevant rules stop
condensing as N per-partner copies, which **relieves** the per-partner cap rather than
competing with it.

*The single-home objection, and why it does not bite.* A rung line must be a **pointer**, not a
copy — "this vault overlays `frontmatter`; read it before writing frontmatter" — the tripwire
shape the module already uses. **The brief must state this explicitly**; a rung that restates
overlay rules is a single-home violation and would be the defect this ruling exists to avoid.

*Consequence for S2, recorded below:* S2 was scoped to measure the boot cost of a Beat 1
`{overlays}` read. That read is not being built. **S2 is re-scoped to measure the rung** —
which is also always-loaded and also spends the budget the 2026-07-29 filings measured.
Re-scoped, not discharged.

**⚠ THE RUNG HAD NO AUTHOR — FIXED.** *(roundtable A17, 2026-08-20 — Maya.)* B9-7's scope as
ideated is **the file and its cap only**, and **nothing in Arc 9 obliges anything to write a
line into it**: `vlt-mint`'s *Edit a convention* kind (`vault-operating-contract.md:106`) mints
an overlay with no rung obligation, and `vlt-groom` is scoped by its own SKILL.md to "one
partner, its three memory files", so it cannot promote a fleet-relevant reflex upward. The
filer's vault **had** the overlay for three days and still lost two partners to it; **a vault
with an empty rung and the overlay is in exactly that state**, and the ruling that removed the
Beat 1 read replaced it with a container nobody is required to fill. **Added to B9-7's scope:**
minting or amending an overlay **writes its rung pointer line in the same act** (a clause at
`vault-operating-contract.md:106`, where overlay routing already lives), and a fleet-relevant
reflex **promotes to the rung**. Two sentences; no new mechanism.

**A recorded alternative the session never wrote down: rung-as-digest.** *(roundtable A17 —
Carson.)* The rung as ruled is **pointer lines only** — an always-loaded instruction to perform
the JIT read that `vault-operating-contract.md:100` **already mandates and that A9-5's field
evidence shows failing**. The filing's proof is two partners violating the same overlay on the
same day, **the second after reading a log entry recording the first's correction**: a reminder
to go read the rule was already in context and did not bind. Q8 records why the rung beats the
read; it recorded **nothing about why a pointer beats a digest** — derived rule lines, cap and
falsifier declared in frontmatter, `reflexes.md` the precedent shape — and the single-home
objection it does answer applies to a **copy**, not to a **declared derivation**.
**Disposition: pointer stands** (the owner's Q8 ruling is not reopened), **and B9-7's brief
carries a falsifier** — what field observation would show a pointer line failing to bind the way
the log entry did.

**S2's NEGATIVE BRANCH IS RULED NOW.** *(roundtable A21, 2026-08-20 — Sophia's finding; owner
ruled it lands.)* A9-5's fix had exactly one surviving candidate home and a spike that could
veto it, **with nothing behind the veto**: capture ruled out the rule-card (clobbered), Q8 ruled
out the Beat 1 read, and S2 can return "too expensive" — at which point the filing with the most
direct live field evidence in the arc ships **nothing**, in the arc's last build, in the second
release, with no posture stated anywhere in shipped text. **The branch:**
- **If the rung exceeds the boot baseline, the Beat 1 `{overlays}` read is reinstated as B9-7's
  fallback.** It was ruled out on **design** grounds, not cost — so a cost veto does not carry
  it away.
- **If neither ships, B9-7's absence carries a stated interim posture in the operating
  contract** naming the unprotected moment. **The gap gets declared rather than staying silent.**

**Reflex-cap note, carried from capture:** the "30/partner" figure is **vlt-core's declared
value, not a module constant**. The rung's own cap is likewise declared in its frontmatter;
no brief writes a number into shipped text.

**Q9 — Does the arc adopt a single durable-host mechanism for vault-local additions?** (A9-2 /
A9-3 / A9-5 — capture's clobbered-host joint.) Three filings independently need a durable home
in three different module-owned files. → **NO SINGLE MECHANISM. State the doctrine; build per
host.** (Round 1, 2026-08-20.)

*The doctrine ships as governance* — and each filing takes the plumbing its substrate allows.

**⚠ THE DOCTRINE'S AXIS WAS WRONG — AMENDED AT THE ROUNDTABLE.** *(roundtable A4, 2026-08-20 —
Winston.)* As ideation worded it, "**a vault-local addition never lands in a module-owned
file**" is **falsified by the module's own shipped mechanism and by this arc's own fix**:
*Vault-writable declared fields* (`…/conventions/frontmatter.md`) exists **precisely so a vault
writes a local value into a shipped base convention file**, and `checks.md`'s base-divergence
bullet excludes those lines by design. B9-4's `local_consumers:` **is** a vault-local addition
landing in a module-owned file. Ship B9-2 as ideation worded it and **the governance bundle
outlaws the arc's own registration mechanism two builds later, in the same release.**

**Amended doctrine text — the axis is carve-out-vs-clobber, not module-owned-vs-not:**
> *A vault-local addition lands only where the base declares a carve-out for it — a
> vault-writable declared field, an overlay, a vault-scoped sibling. It never lands in a file
> the module overwrites on update.*

That wording keeps A9-3's host (`vlt-vitals.py`'s `METRICS`) and A9-5's host
(`_meta/vault-rule-card.md`) **illegal**, and B9-4's `local_consumers:` **legal**.

*The grounding the ruling rests on: the three hosts are not one defect.* Two of them are:
`.claude/hooks/vlt-vitals.py`'s METRICS table (A9-3) and `_meta/vault-rule-card.md` (A9-5) are
both module-owned and both explicitly **overwritten on every install/update**
(`skills/vlt-setup/SKILL.md:181` and `:146` respectively). The third is **not** — A9-2's host
is a pristine base reverted on reconcile, and **the module already ships the answer pattern
for it**: *Vault-writable declared fields* (`…/conventions/frontmatter.md:276`), a live
mechanism whose consuming nets (`vlt-lint`'s base-divergence check, `vlt-upgrade`'s pre-flight)
follow for free because they read that list rather than carrying their own. `local_consumers:`
is a one-line addition to a working mechanism, not a new one.

*And the surviving two differ mechanically:* A9-3's is a Python import into `METRICS`; A9-5's
is a markdown read at Beat 1. Same doctrine, different plumbing. **Designing one abstraction
over n=2 with incompatible substrates was ruled the wrong trade** — and it would rework A9-2's
already-clean fix for no gain.

**THE DOCTRINE SHIPS `checked`, NOT `declared` — its bell already exists.** *(roundtable A5,
2026-08-20 — Dr. Quinn; this **refutes joint 8's premise**, which the room recorded as died at
the table.)* The roundtable's own framing — "a doctrine with no detector" — was **false**. The
module already ships the exact detector, **in triplicate, covering all three named hosts**:
`vlt-upgrade` pre-flight emits **`skill_asset_divergence`** (the `.skill-manifest` walk
explicitly covers `.claude/hooks/vlt-vitals.py`), **`governance_divergence`** (the `_meta/`
bundle, hence `vault-rule-card.md`) and **`base_divergence`** (a hand-edited pristine base) —
the detect-and-report safety net at `skills/vlt-upgrade/SKILL.md:113`, which even **preserves
the clobbered content in the ledger**. The clobbered-host pattern is **not undetected; it is
detected every upgrade, reported, and given nowhere to go** — so the field's only legal response
today is to re-apply the edit and re-trigger the same report next upgrade. **A bell wired to no
exit.**

*So B9-2 writes the doctrine with a real enforcement declaration, not prose:*
`enforcement_stage: checked`, `enforcement_checked_by: vlt-upgrade`,
`enforcement_moment: pre-flight`, **naming those three report keys as its bell** — plus one
clause: **each of those three post-flight report lines instructs the reader to route the
addition to its durable host.** No new mechanism, and the doctrine stops being the one rule in
the arc that ships `declared`.

**AND A BIRTH-TIME OBLIGATION, so there is no host #4.** *(roundtable A6, 2026-08-20 — Dr.
Quinn.)* Q9 answers "what do we build for these three?" and never answered "what stops there
being a fourth?" The generator is still running and fully visible: `vlt-setup` declares
module-owned, overwrite-on-every-update files at `SKILL.md:146, :149, :151, :174, :181`, and
every future one is minted the same way — a build deciding a file is module-owned, with **no
obligation at that moment to say where the vault's version of that content goes**. Under Arc 9
as ideated, host #4 is discovered exactly as #1–#3 were: a vault edits it, an upgrade eats it,
someone files. One sentence attached to the doctrine:
> *A build that declares a file module-owned or overwrite-on-update must, in the same build,
> name where vault-local additions of that file's kind live — or state in shipped text that
> none exist.*

A **birth-time obligation**, deliberately **not** a completeness-claiming host list (`CLAUDE.md`
warns those drift). Costs a future build one sentence.

**Home for the doctrine — RE-RULED AT THE ROUNDTABLE:**
`…/governance/_meta/vault-operating-contract.md`, in its ***Durability across upgrades***
section (`:88-105`). *(roundtable, Dispute 2, 2026-08-20.)* Q9's doctrine **genuinely is a vault
rule** — unlike D5 — and that section already houses overlays, local conventions and the
designed-parameter read. **Not "one governance edit, at most one handshake": B9-2 is now three
sitings under one build** (D5 → `CLAUDE.md`; Q9 → the contract; D6 → `frontmatter.md`).

**⚠ PRICED, NOT FREE.** *(roundtable, Dispute 2 + A9/A3 grounding — Amelia and Paige.)* "The
contract is deliberately not handshaked, so no bump is owed" is true and **is not the whole
cost**. `_meta/vault-rule-card.md` is a **derived** artifact pinning the contract's SHA-256
(`derived_from: … sha256:`), enforced by package-lint **C6** (`check_rule_card`,
`tools/package-lint.py:305-336`; harness case 12 is exactly "contract edited without
re-deriving the rule-card → C fails"). **Any contract edit re-derives the card and re-stamps its
digest, or C6 blocks the tag** the release contract requires. An act-blocking clause must also
earn a card row inside `RULE_CARD_BUDGET = 8000` bytes — **5,937 used today, 2,063 of headroom
shared, uncounted, with B9-7 in a different release, i.e. two independent C6 gates.**
***"No bump owed" is not "no cost."*** (Standing rule **R1**.)

*Dissent recorded (Dr. Quinn).* Siting Q9 in the contract still exempts it from the
`checks.md:37` enforcement-doctrine meta-check and the `frontmatter.md:257` bell obligation,
both of which walk `{conventions}` **only** — so the *cheaper* siting is the one that exempts
the arc's thesis rules from their own doctrine. **Quinn's objection is answered by A5**, which
gives the doctrine a real enforcement declaration keyed to `vlt-upgrade`'s existing detectors
rather than relying on the meta-check; Quinn accepted that as sufficient **for this rule**. The
dissent stands against the general principle that siting is a free choice.

*Standing rule (project `CLAUDE.md`): the governance bundle is the SSoT; never create a second
copy.*

**Q10 — Ruling 4c: the three lint-surfaced module-feedback candidates.** (Inherited, Arc 8 bound
**MISSED**.) Never filed, so capture could not pull them in; they are an owner action. Ruling
needed on whether they are re-bound to Arc 9, dropped, or re-dated.
→ **RE-BOUND TO ARC 9, WITH A HARD GATE.** (Round 5, 2026-08-20.)

*Terms.* Filer = **owner** (unchanged — Arc 8's ruling 4c, roundtable A15). Bound = **before
v0.12.0 is tagged** *(roundtable A8, 2026-08-20 — amended from "before Arc 9's release", which
Round 6's two-release split left naming something that does not exist; its two readings were
three builds and an unknown span of spike time apart, and **an ambiguous datum is how the first
two slips were recorded**)*. **The bound is `[ship-verifiable]` and is entered in the live-acceptance
ledger below so it GATES Arc 9 closeout.** This is the **B7-6 mechanism** — the one that
retired the four-arc A4-4 (5) Jackson-pair debt, where amendment A3 (tag it ship-verifiable so
it gates) was what made the difference. A third miss can no longer be recorded as a silence.

*Why the hard gate rather than the same soft bound.* **This bound has now slipped two arcs.**
Set by Arc 7's closeout, carried into Arc 8's ideation pool, bound by roundtable A15 to
"before Arc 8's release", **MISSED** — v0.11.0 shipped 2026-08-17 with nothing in `inbox/` —
and defaulted to Arc 9. Re-issuing the identical soft bound a third time repeats a shape that
has failed twice.

*Recoverability note, established this session.* The candidates' **content is not recoverable
from any roadmap.** Arc 8 records the source as "the owner's vault-side report"; no roadmap
carries the substance. **Capture cannot manufacture them and never could** — this is an owner
action in the strict sense.

**⚠ THE HARD GATE COULD NOT FAIL, AND THEREFORE WAS NOT A GATE — REPAIRED AT THE ROUNDTABLE.**
*(roundtable A8, 2026-08-20 — Mary, Carson, Sophia converging.)* As ideated it discharged on
"three dated filings existing in `inbox/`" with **no stated content**, so three files on any
subject ticked it; **its own recoverability caveat then supplied an escape** ("record the loss
rather than carry a fourth arc"), so non-discharge *also* closed the arc; and `inbox/` is
gitignored and factory-local, so nothing in a released artifact evidences either outcome. It
borrowed the **B7-6** mechanism's name without B7-6's property — B7-6 worked because the check
named a specific pair a reader could verify, and because it made the impossibility **a finding
that escalates**, not a way to close. Sophia named the missing beat: every other out-of-source
obligation in this arc got an instrument — A9-1's field content got S1, `vlt-upgrade`'s
internals got S3, the boot budget got S2 — while **the one artifact whose very existence is
unknown got a caveat and a deadline pointed at the end of the arc.**

**The gate as repaired — narrowed, not ordered:**
1. **A primary discharge route that is mechanical.** The candidates are **lint-surfaced**, so
   their content is *not* uniquely trapped in a vault-side report: **re-running the full
   `vlt-lint` pass on vlt-core resurfaces them.** Owner-run, vault-side, dischargeable without
   recovering the original report. *(Carson.)* This route was never on the table at ideation.
2. **A dated act at the arc's front, not its end.** The owner attempts to locate the vault-side
   report **before B9-1's brief** — not at closeout.
3. **Unrecoverability becomes a filing, not prose.** If the report is gone *and* the lint re-run
   comes back empty, **that unrecoverability is written as a dated filing into `inbox/`, and
   that filing discharges the gate.** The gate then discharges on three filings, or on one —
   **never on prose written at closeout about filings that do not exist.**
4. **The self-certifying escape is deleted.** "Closeout records the loss rather than carrying a
   fourth arc" is struck from the discharge condition; the recoverability caveat now applies
   **only if the lint re-run returns empty**, turning "the report is gone" from a declaration
   into a **checkable result**.

*Owner action raised at the roundtable (Mary): name the three candidates' subjects so the gate
binds to content rather than to a file count.* **DONE — see below.**

**⚠ THE "NOT RECOVERABLE" PREMISE IS FALSE — THE THREE CANDIDATES ARE NAMED ON DISK.**
*(roundtable A8, corrected 2026-08-21, owner-prompted.)* Arc 8 recorded the source as "the
owner's vault-side report" and Arc 9's capture inherited that as unrecoverability. **Arc 7's
Closeout record, carry-forward item 8, carries the substance** — strength-ordered as in the
owner's report:

1. **The naive `spec_candidate` relay count** firing **the same 6 false positives for a third
   consecutive run.**
2. **`vlt-lint-full.js` scanner prompts** not honoring `frontmatter` rule 4's **coexistence
   posture**, nor the **callout-vs-bullet distinction**.
3. **The fan-out's `crossLayerSlugs`** omitting **`_agent/handoffs/`, `_agent/bases/` and
   `areas/`.**

Source: `skills/reports/archive/inbox-evolution-arc7-roadmap.md`, *Closeout record* → "New field
signal awaiting `inbox-capture`" item 8. **What was lost was the pointer, not the content**:
Arc 8 carried the reference without the substance and Arc 9's capture propagated the loss. The
gate's discharge condition is therefore **narrowed to these three named subjects** — three
filings matching them, and nothing else ticks it. **Mary's condition is satisfied and the
lint-re-run route (A8 route 2) becomes a convenience rather than a rescue.**


### Cross-filing decide-once rulings

*Decisions that resolve the same question across two or more filings identically. Seeded from
the capture's cross-filing joints table.* **All are ruled** *(roundtable A19 — the lead-in still
said "all unanswered").*

**D1 — The overlay zone, unread and unchecked.** (A9-2 Finding 5 ↔ A9-5.) Nothing *checks*
`{overlays}`; nothing *reads* it at activation. Does one build close both directions, or do the
bell and the read separate? → **THEY SEPARATE.** (Round 2, 2026-08-20.) Ruled jointly with D2
as **three cluster builds** — see below. Note that under Q8 the *read* direction is not built
as an overlay read at all: the rung answers it via a pointer line, so D1's two directions were
never the same edit.

**D2 — The overlay bell ↔ durable metric joint.** (A9-2 Finding 5 ↔ A9-3.) Capture's finding:
neither half ships alone — a durable local metric with no overlay-walking checker rings nothing;
an overlay-walking checker with no durable metric has nothing to key on. → **UPHELD, AND THE
MECHANISM IS CONFIRMED.** (Round 2, 2026-08-20.) The bell and the metric ship in **one build**.

*The constraint, grounded this session:* extending the enforcement-doctrine meta-check
(`checks.md:37`) to walk `{overlays}` makes overlay-hosted rules eligible for
`deferral_expired` / `declared_untripwired` / `deferral_invalid` — **and immediately for
`counter_unknown_metric`**, because any `enforcement_counter:` on an overlay rule names a
vault-local metric and `vlt-vitals.py:283` hard-errors on ids absent from `METRICS`. **Ship the
checker without A9-3's durable metric home and it fails every rule it newly walks.** This is a
true ordering constraint, not a preference.

#### The cluster's build division — ruled Round 2 (2026-08-20)

**Three builds.**

1. **A9-2's registration items alone** — `local_consumers:` (`frontmatter.md:276`), the
   `frontmatter.md:82` → pointer fix, the `write-verification.md` delegation clause (Q3).
   Small, clean, no dependency on the other two.
2. **A9-3's durable metric home + A9-2 Finding 5 (the overlay-walking bell)** — one build,
   honoring the D2 ordering constraint. **Spike-gated: S3 blocks this brief only.**
3. **A9-5's fleet-wide rung** — separate. Spike S2 (re-scoped) attaches here.

*Why not fewer:* one cluster build would put the whole cluster behind S3 and behind A9-5's
design call. *Why not more:* splitting the bell from the metric re-opens the D2 failure the
ordering constraint exists to prevent.

**D3 — `frontmatter@8 → @9` sequencing.** (A9-1 `grounding:`/`lifecycle:` ↔ A9-2
`local_consumers:` ↔ A9-1 `type: resource` retirement.) Three independent reasons to bump the
same convention and re-ack its consumers. Sequenced together = one bump and one walk; sequenced
apart = three. → **RE-SCOPED BY ROUND 1, THEN RULED.** (Round 5, 2026-08-20.)

*What Round 1 changed.* A9-1 left the arc, so two of D3's three reasons went with it. **Arc 9's
handshake load is two bumps, both in the arc:**
- **`frontmatter@8 → @9`** — `local_consumers:` (A9-2) **plus Finding 4** (below), and
  `frontmatter.md:276` states the price itself: "Declaring a further field vault-writable is a
  base rule change: it bumps this file's `version:` and walks every consumer" — **nine
  consumers, not "seven-plus"** *(roundtable A22, 2026-08-20; `frontmatter.md:12`)*, and the
  ninth is **`vlt-lint-full.js`, an asset node whose ack is a `// depends_on:` header checked by
  package-lint **E5, not E1** (`tools/package-lint.py:56-75`) — a different edit surface on
  every walk.
- **`write-verification@2 → 3`** — Q3's value-set → consumer-roster edit; re-acks all four
  consumers. **A bump D3 had not been counting** until Round 4 grounded Q3.

Arc 10 bumps `frontmatter@9 → @10` for `grounding:` and the `type: resource` retirement. Three
handshakes across two arcs; the split's price, accepted in Round 1.

**Finding 4 RIDES the Arc 9 bump — folded into the bell build.** (A9-2 residual item 4,
per-section enforcement addressing for overlays.)

*Why it is not optional, grounded this session.* `frontmatter.md:255` — the *Enforcement
declaration* — is a set of **flat, file-level** frontmatter keys (`enforcement_stage:`,
`deferral_metric:`, `deferral_threshold:`, `review_after:`, `adoption_first_instance:`). An
overlay **accretes sections**; the declaration does not address sections. The moment the bell
build makes the meta-check walk `{overlays}` (D2/Finding 5), it validates **one file-level
declaration standing in for many independently-shaped sections** — and A9-2's own claim is that
the next genuinely rule-shaped overlay section "cannot be declared honestly at all." Shipping
the bell without Finding 4 would be a checker validating a declaration shape the filing says
cannot be honest.

*Accepted cost:* it enlarges the arc's already S3-gated build with a schema change. The
alternative — deferring with a stated interim posture — was rejected because it ships a checker
against approximations for a whole arc.

**⚠ UNRESOLVED CONSEQUENCE — for the roundtable, not assumed here.** This ruling puts **two
builds on the same convention file**: B9-4 changes `frontmatter.md` for `local_consumers:`, and
B9-6 changes it again for Finding 4. Under the version-handshake rule each rule change bumps
`version:` and re-acks every consumer in the same build — so as ordered this is **two bumps
(`@8 → @9`, then `@9 → @10`) and two nine-consumer walks** *(roundtable A22)*, which ideation
read as the exact cost D3 exists to avoid. Three resolutions were tabled: **(i)** accept two bumps as the price of
Finding 4 riding the bell; **(ii)** move Finding 4 into B9-4 so one bump carries both, and let
B9-6 depend on B9-4 having landed; **(iii)** merge B9-4 and B9-6.

**→ RESOLVED AT THE ROUNDTABLE — (i), two bumps, reason recorded.** *(roundtable A22,
2026-08-20.)* **Not resignation.** The room found the fact the ⚠ note omitted: **B9-4 ships in
v0.12.0 and B9-6 in v0.13.0.** Two bumps across two *releases* is not the duplicated walk D3
exists to prevent — that fault is **intra-build**. A single `frontmatter@9` shipped in v0.12.0
and again in v0.13.0 with different rule content would make the `version:` string stop
identifying what it versions: a worse defect than a second consumer walk.

*Why not the others.* **(ii)** moves a `frontmatter.md` schema widening into v0.12.0 while the
meta-check that enforces it stays in v0.13.0 — a widening a whole release ahead of its
enforcement, which **D6 forbids in the same release that enshrines D6**. **(iii)** drags
`local_consumers:` *and* `write-verification@2 → 3` behind S3 and out of v0.12.0, leaving
vlt-core's locally-adopted overlay `consumers:` line in a known-unlawful posture (Q1
consequence 1) for an extra release with no remedy shipped. **Only (i) composes.**

*Why an interim posture is not sufficient here specifically* (the room required this sentence,
because D6 — ruled the same round — elevates interim postures to standing doctrine): D6's
instrument is sufficient for **a checker validating declaration shape**, and insufficient for
**a rule widening what may be written**. Finding 4 is the second kind. The distinction is real
and it makes D6 sharper, not weaker.

*Dissent recorded (Carson).* Option **(iv)**, unlisted at ideation: defer Finding 4 to Arc 10's
**already-owed** `@9 → @10` bump (for `grounding:` and the `type: resource` retirement), taking
the two-arc total from three handshakes to two. Cheaper, and legal under D6. **The owner did not
take it** — the arc pays its second bump in-arc rather than mortgaging Arc 10's.

*Composed outcome with Dispute 2:* siting **D6 in `frontmatter.md`** folds D6's own handshake
into **B9-4's already-bought walk**. **The arc pays two bumps, not three.**

**D4 — Ingress before intake.** (A9-4.) Repo-side templates + labels must exist before the
factory-side intake step has anything to query; capture confirmed by exercise that issue #1
carries **no labels** today. Are the three parts one build or ordered builds?
→ **TWO BUILDS: the rail, then the intake.** (Round 4, 2026-08-20.)

- **Build A — the rail.** `.github/ISSUE_TEMPLATE/` + the label set + the `vlt-feedback` skill
  + the transport URL in `module.yaml`. **Designed together as one field contract**, because
  the template's fields and the skill's payload are the same contract; splitting them across
  briefs invites precisely the drift this arc exists to name.
- **Build B — the intake.** The factory-side step at the **two** lifecycle seams capture
  confirmed (`inbox-capture`'s Discovery stage, `arc-closeout`'s Stage 5 archival), plus the
  **`origin:` header single-home** — capture's candidate `inbox/README.md`, which today
  specifies a filename convention but no header shape at all.

*The ordering is structural, not preferential:* capture confirmed by exercise that issue #1
carries **no labels**, so a "list open `vault-filed` issues" step has nothing to query until
build A lands.

*Sizing note carried into the briefs:* **build A's repo-side half is not shipped surface.**
`.github/` does not live in `skills/`, is not part of the own-the-apply copy surface, and
reaches no vault — it costs nothing in a release. It is still briefed, because it is half of a
field contract.

**D5 — Precedence as a general posture.** (A9-6, generalizing.) Where two shipped rules overlap,
does the module state precedence explicitly as a standing practice, or fix instances as found?
→ **STANDING RULE, HOMED IN THE GOVERNANCE BUNDLE.** (Round 3, 2026-08-20.)

**Named home — RE-RULED AT THE ROUNDTABLE:** project **`CLAUDE.md`, *Standing rules***.
*(roundtable, Dispute 2, 2026-08-20.)* **Not the governance bundle.** Paige's finding, which the
room accepted: D5's rule is addressed to an audience **contractually forbidden to execute it**.
"Where two shipped rules address the same population, the overlap is eliminated by narrowing one
rule's population" can only be performed by **the factory** —
`vault-operating-contract.md:105` sends any change to a shipped base upstream ("it is
**generic** and belongs upstream") and `:104`'s designed-parameter-read veto forecloses the
vault-side route. Siting it in the vault-delivered bundle ships a **build-authoring rule to
readers who may only file it**. In `CLAUDE.md` it joins **single-home discipline** and **the
version handshake** — its own siblings. **Handshake cost: none** (`CLAUDE.md` is not a
handshaked convention). A vault-facing restatement, if ever wanted, is a **pointer, never a
copy**.

**Rule text (authored to compose with Q5, not to contradict it):** where two shipped rules
address the same population, the overlap is **eliminated by narrowing one rule's population**;
an explicit precedence statement is the **fallback**, used only where the populations genuinely
cannot be cut apart. *Prefer elimination; state precedence only when elimination is impossible.*

*Why the preference ordering matters:* D5 as bare "state precedence" would have licensed
exactly the option Q5 rejected. The rule as written makes B9-1's own repair the worked example
of the rule, rather than its counter-example.

**Version-handshake obligation:** if the rule lands in a bundle convention carrying
`version:`/`consumers:`, this is a **rule change** — it bumps that file's `version:` and re-acks
every consumer in the same build. The brief must determine which file and price it. If it lands
in the operating contract, the contract is **deliberately not handshaked** (single-home +
pointers) and no bump is owed.

**D6 — Enforcement-ships-with-widening.** (A9-1 C5, the filing's own hard constraint.) The
filing forbids shipping the PARA widening without the lint family. Owner to enshrine or vary.
→ **ENSHRINED NOW, AS A STANDING RULE, WITH A STATED INTERIM POSTURE.** (Round 5, 2026-08-20.)

**Rule (as amended at the roundtable):** a change that **widens what may be written — or that
states a new rule constraining what may be written** — ships in the **same build** as the
enforcement that catches its violations. A change whose enforcement cannot ship in the same
build states an interim posture in shipped text, or is withdrawn. *(roundtable A1,
2026-08-20.)*

*Why the scope widened.* As originally authored the rule bound **widenings only** — so it could
not reach any of the four bell-less boundaries **this arc itself creates**: Q9's durable-host
doctrine, D5's precedence rule, D6 itself, and Q8's pointer-only rung constraint. Every one is a
**narrowing or a new rule**, and every one ships in B9-2 or B9-7. The arc that indicts
`vault-operating-contract.md:61` for drawing a boundary "where no mechanism can enforce it"
would have shipped its own governing build as three boundaries with no bell, with the one rule
enshrined to prevent that scoped so it did not apply to them.

**Form of the interim posture — it is not prose.** *(roundtable A2, 2026-08-20.)* The interim
posture **is the shipped *Enforcement declaration*** (`frontmatter.md:255-276`):
`enforcement_stage: declared` plus the mandatory deferral triple
(`deferral_metric:` / `deferral_threshold:` / `review_after:`). That schema is precisely "the
rule exists ahead of its check, on the record, with an expiry" — and a posture written as prose
instead fires **none** of `declared_untripwired` / `deferral_invalid` / `deferral_expired`.
Written as prose, D6 would ship the arc's own headline doctrine (*no boundary without a bell*,
homed at `frontmatter.md:257`) in the one form that rings nothing.

**Every build in this arc that widens or newly constrains runs D6's test on itself and records
the result** — a named bell, or a declared posture with a `review_after:`. *(roundtable A3,
2026-08-20.)* B9-3 and B9-4 are both caught by this; see their scope lines.

**Named home — RULED AT THE ROUNDTABLE:** `…/governance/_meta/conventions/frontmatter.md`, in
its ***Enforcement declaration*** section. *(roundtable, Dispute 2, 2026-08-20 — Paige's
split-by-audience siting.)* Not a brief-time call any more: the rule *is* about the enforcement
declaration, so it belongs where that schema is defined. **Handshake: this is a rule change and
bumps `frontmatter.md`'s `version:` + re-acks all nine consumers — but B9-4 is already buying
that walk, so D6's handshake folds into it at no additional cost.** This is what makes the arc
pay **two bumps, not three** (see D3/A22).

**Why now rather than with A9-1.** Capture endorsed C5 on evidence — `para_missing_attestation`
is the shipped worked example of what an unenforceable rule decays into — and Arc 9 produced two
more instances of the general form in this session alone: Q2 shipped a boundary with no bell
(flagged for the roundtable), and D2's ordering constraint is this same principle applied to a
mechanism. Enshrining now **binds Arc 10** rather than re-arguing a settled constraint there.

**Interim posture (required, because the rule is enshrined an arc ahead of the build it
governs).** Until Arc 10's lint family ships, the PARA location rule stands **unwidened** —
`vault-operating-contract.md:61`/`:63` remain as written, and `para_missing_attestation`
remains the net. No partial widening is legal in the interim.

**→ ROUNDTABLE TESTED IT AND FOUND IT HALF-BUILT.** *(roundtable A21, 2026-08-20 — Maya's
finding, upheld in full; owner ruled it lands.)* The posture as written is **addressed to the
factory, not to the field**: "PARA stays unwidened, `para_missing_attestation` remains the net"
is an instruction to Arc 10's builders. Meanwhile app-vault's owner filed a `severity: high`
breach happening **now** — 57 files whose `sources:` no longer certifies provenance — and
**both** v0.12.0 and v0.13.0 ship with `vault-operating-contract.md:61`/`:63` and
`extraction.md` unchanged, so partners keep reciting the rule they are already breaching in
order to get work done. The posture protected the module's coherence and left the filer's vault
exactly where it was.

**A field-facing half is added, shippable in v0.12.0, widening nothing:** a short stated posture
(release changelog + the arc's carry-forward, exact siting a brief-time call) telling vaults
with agent-authored PARA content that **the finding is known**, that **overflow belongs under
`_agent/` rather than through a falsified `sources:`**, and that **the model lands in Arc 10.**

**D7 — Does `grounding:` inherit the personalized-extraction firewall checks?** (A9-1 C4 +
watch item.) Capture found the precedent live and enforced (`method_not_in_sources`,
`method_in_personalization`) and observed the new field should inherit that family rather than
invent one. → **DEFERRED TO ARC 10** (Round 1, 2026-08-20) — A9-1-only; travels with the
filing. Capture's observation (inherit the family, don't invent one) is carried intact.

### Spike obligations

*External unknowns that get a read-the-actual-source spike **before** the brief is written. Each
carries SPIKE OPEN until a dated SPIKE CLOSED record replaces it in this section.*

**S1 — The PARA container harvest (A9-1, K13). MOVED TO ARC 10** (Round 1, 2026-08-20) — it
travels with A9-1. Carried here verbatim so the Arc 10 roadmap inherits it intact, **not** as
an Arc 9 obligation. *Original entry:* **SPIKE OPEN.** K13's instruction is explicit and
capture deliberately did **not** discharge it: read the model out of `app-vault`'s two
`projects/<slug>/index.md` files (33K and 10K, carrying a charter, a bidirectional
cross-project dependency table, a Q-numbered decision/open-questions register, and a workplan)
and `vlt-sayari`'s 210 candidate instances, **before writing any contract text**. Capture's
framing: build one is a harvest, not a design; the cost of skipping is N incompatible private
schemas accreting in production. → **Arc 10's to own and date** (Round 1, 2026-08-20). Not an
Arc 9 obligation; recorded here only so the Arc 10 roadmap inherits the instruction verbatim.

**S2 — Boot-cost of a new always-loaded read (A9-5). SPIKE OPEN — RE-SCOPED Round 2
(2026-08-20).** Originally scoped to the Beat 1 `{overlays}` read. **Q8 ruled that read out**;
the fleet-wide rung is built instead. The rung is *also* always-loaded and *also* spends the
budget the 2026-07-29 boot-cost filings measured (`skills/reports/cost-baseline-2026-07-29.md`
is the factory-side baseline). **S2 now measures the rung**, against that baseline, before
**B9-7** is briefed. Re-scoped, **not discharged**.
→ **Owner: the clerk, factory-side. Due: before B9-7's brief** (Round 6, 2026-08-20). The
measurement is entirely in-repo — the baseline is `skills/reports/cost-baseline-2026-07-29.md`
and the rung's shape is ruled at Q8. A dated **SPIKE CLOSED** record replaces this entry.

**S3 — `vlt-upgrade` Step-3 / Step-3.6 ordering trap (A9-3). SPIKE OPEN — internal-source
grounding, not an external read.** Capture flagged this claim as **stated, unverified** and
declined to launder it: a reconcile that re-applies a local edit before the manifest write would
record the modified SHA as stock, silently blessing the edit. Also unverified: A9-3's B7-2
manifest analysis. Both need a real read of `skills/vlt-upgrade/` before any brief depends on
them. → **Owner: the clerk, factory-side. Due: before B9-6's brief** (Round 6, 2026-08-20).
Both claims are in-repo reads of `skills/vlt-upgrade/`; neither needs a live vault. A dated
**SPIKE CLOSED** record replaces this entry. **If the ordering trap is confirmed, it is a
defect in its own right and files to `inbox/` rather than being absorbed silently into B9-6.**

### Evidence-debt dispositions

*Each declared debt is attached to a build or ruled not-blocking.* **All six are dispositioned**
*(roundtable A19 — the lead-in still said "All unruled").*

**Disposition ruled Round 6 (2026-08-20) — owner deferred the call to the clerk.** E1–E3
attach to **B9-3 (the rail)** as **`[field-contingent]`** acceptance checks; E4 is released as
a standing watch. *Reasoning on the record:* all three testable debts sit **where their
mechanism lives** — the origin-vault field, the scrub gate, and the `gh` call are all inside
`vlt-feedback` and the templates, i.e. B9-3. B9-5's own checks are about ingest correctness,
not about whether the rail's assumptions held. E4 gets no build because no build can discharge
it. **Note plainly: none of the four is ship-verifiable, so under `build-brief` §9 none gates
closeout — B9-3 ships a rail whose four declared risks all discharge in the field.**

**E1 — Shared-vault attribution (A9-4).** GitHub author ≠ origin vault; the template's
origin-vault field is the answer on paper. **Capture upgraded this from hypothetical to
confirmed on n=1**: issue #1's author is the owner's account while the origin vault is
app-vault. Remedy still unproven. → **ATTACHED to B9-3, `[field-contingent]`.** Discharges on a
real cross-machine filing whose origin-vault field correctly names its vault.
**Discharging event named** *(roundtable A20)*: **a successful `vlt-feedback` run from the work
machine's app-vault**, bound as an **owner action** with a stated arc bound. Without a named
event this debt had no reachable discharge at all — `vlt-core` is on the factory machine, the one
place the rail's cross-machine assumptions cannot be exercised.

**E2 — Scrub-gate efficacy (A9-4).** Untested against real personal-domain signal. Capture's
note: issue #1 is machinery-only content, so the materialization exercise is **not** scrub-gate
evidence and should not be read as such. → **ATTACHED to B9-3, `[field-contingent]`.**
Discharges only on a filing carrying **real personal-domain signal**; the ledger entry must say
so, or the check will be ticked against another machinery-only filing and prove nothing.

**E3 — `gh` auth variance on the work machines (A9-4).** Assumed available/authenticated; not
verified by any module machinery. Capture's run succeeded from the factory machine only.
→ **ATTACHED to B9-3, `[field-contingent]`.** The one debt that can **hard-block the rail's
actual users**. Discharges on a successful `vlt-feedback` run **from a work machine**, not the
factory. ~~The brief should consider whether `vlt-feedback` detects and reports missing/unauthed
`gh` rather than failing obscurely.~~ → **PROMOTED FROM CONSIDERATION TO SCOPE** *(roundtable
A15, 2026-08-20)*: it is the only thing that makes E3 discharge **either way**. `vlt-feedback`
detects missing/unauthed `gh`, reports it by name, and emits the **fully-formed filing to a local
file with label names and origin-vault field pre-written, paste-ready.** **E3 now discharges on
*either* a successful work-machine run *or* a recovered failure artifact** — and its discharging
event is named per A20. Otherwise the failure of the ingress could not be filed through the
ingress, and a hand-opened issue carries no labels and no origin vault — **structurally
unqueryable by B9-5's Discovery.**

**E4 — Community/noise traffic on a public tracker (A9-4).** Label partitioning is a design, not
evidence. → **RELEASED as a standing watch** — no build can discharge it; it needs traffic to
arrive. Carried in the arc's carry-forward register at closeout, not in the acceptance ledger.

**E5 — DEFERRED TO ARC 10** (Round 1) — travels with A9-1. *Original entry:* A9-1's
`grounding:` laundering watch. The filing's own watch item: `grounding:` is a
candidate laundering channel for method claims, the same failure `extraction.md` anticipates for
`personalization_sources:`. → **Arc 10's to disposition** (Round 1, 2026-08-20).

**E6 — DEFERRED TO ARC 10** (Round 1) — travels with A9-1. *Original entry:* K16, the
attestation-census pattern (A9-1, watch). Every time content crosses the
agent/human boundary an attestation check becomes a census; seen twice
(`para_missing_attestation` at 56/56). Moving the wiki into human-browsable space is predicted
to mass-produce `attestation_stale`. The filing says design for the third instance now.
→ **Arc 10's to disposition** (Round 1, 2026-08-20).

### Questions deliberately left to brief time

**Confirmed and reassigned, Round 6 (2026-08-20).** Four of capture's nine travelled to Arc 10
with A9-1; two were **promoted out of brief time** by this session's rulings and now sit in
build scope; three remain genuinely brief-time.

**Moved to Arc 10 with A9-1** (Round 1) — not Arc 9 obligations, carried verbatim so the Arc 10
roadmap inherits them:
- whether `areas/`-as-ideation-home (K3) survives contact with the S1 harvest;
- enumerating PARA `status:` per type, closing the `extraction.md:94` placeholder defect
  (capture found this is a second half K4 does not name);
- the project-to-project relation K11 identifies as the actually-missing edge;
- fixing `skills/vlt-mint/assets/capability-template.md:23` (K9) — one line, no dependencies.
  **Flagged:** it is buildable immediately and independent of the harvest, so Arc 10's ideation
  should consider ruling it a drive-by rather than letting a one-line template fix wait on a
  two-vault harvest. Not ruled here — it is A9-1's, and A9-1 left.

**Promoted out of brief time by this session** — no longer open questions:
- A9-2's `frontmatter.md:82` → pointer fix — **in B9-4's scope**; graded a prose clarification,
  **no version bump owed**.
- A9-2's per-section enforcement addressing (Finding 4) — **ruled into B9-6** by D3, no longer
  a sizing question.

**Genuinely brief-time, confirmed as such:**
- **A9-3 / B9-6:** which of the issue's three directions the build takes — vault-local metrics
  module, declarative inline metrics, or make-the-loss-legible. The filer declared **no strong
  preference** and offered a PR. *Constraint the brief inherits from Q9:* direction 3
  ("make the loss legible") is **not a fix** and does not satisfy D2's joint — the overlay bell
  needs a durable id to key on, which only directions 1 or 2 provide. **S3 informs this choice.**
  **→ AMENDED: direction 3 is re-admitted as a FLOOR, not an alternative** *(roundtable A21,
  2026-08-20 — Maya; owner ruled it lands)*. "Make the clobber legible at upgrade time" attaches
  to a **v0.12.0** build; **the brief-time question is which of directions 1/2 lands *on top of
  it*.** It remains true that direction 3 does not satisfy D2 — and it is additive, cheap, and
  the only thing that helps the filer's vault between now and v0.13.0.
- **A9-4 / B9-5:** where the materialized-filing `origin:` header shape is single-homed —
  capture's candidate `inbox/README.md`, which today specifies a filename convention but no
  header shape at all. → **DISCHARGED before brief time** *(superseding note, B9-5 brief run
  2026-08-21)*: roundtable A15/Paige moved the single home into the shipped half and B9-3
  **built** it — the shape lives at `skills/vlt-feedback/references/field-contract.md:38-50`
  with `inbox/README.md:19-24` and both issue forms as pointers. B9-5's brief (disposition 1)
  cites the siting and adds only the intake-side reading; nothing was left to decide.
- **A9-2 / B9-4:** whether any shipped doc instructing a base-vs-baseline comparison should
  specify a checksum or a real line differ (the filing's bonus instrument note — a wrapped
  `diff` fails toward "no divergence", the dangerous direction). **Capture did not grep for
  instances; the brief owes the grep.**

## Roundtable review — A9-1..A9-6 ideation rulings (2026-08-20)

**CONVENED AND CLOSED. No OPEN disputes — `build-brief`'s gate is satisfied.**

**Roster convened (13, discovered fresh from `.claude/skills/bmad-agent-*` and
`bmad-cis-agent-*`; none excused):** Mary (analyst), Winston (architect), Amelia (dev), John
(PM), Paige (tech writer), Sally (UX), the Agent Builder, Carson (brainstorming), Dr. Quinn
(problem solver), Maya (design thinking), Victor (innovation), Caravaggio (visual
communication), Sophia (storyteller). **Owner's carried worry: none named — the room hunted
cold** against the eight joints ideation recorded. **51 findings returned; 12 clusters; 22
amendments, 5 standing rules, 4 owner rulings.** Session file:
`_output/party-mode/2026-08-20-arc9-roadmap-roundtable-session.md`. Keepsake:
`_output/party-mode/2026-08-20-arc9-roadmap-roundtable.html`.

**Three premises died at the table** — the review's most valuable output, because each was a
joint the room was convened to hunt and each turned out to be already answered by shipped code:

- **Joint 8's premise ("doctrine with no detector") — REFUTED (Dr. Quinn).** `vlt-upgrade`
  pre-flight already emits `skill_asset_divergence`, `governance_divergence` and
  `base_divergence` across all three clobbered hosts (`vlt-upgrade/SKILL.md:113`), preserving the
  clobbered content in the ledger. **A bell wired to no exit, not a missing bell.** → A5.
- **Joint 2's premise ("nothing detects an overlay violation") — REFUTED (Sally).** `vlt-lint`'s
  *Overlay append-only* check (`checks.md:42`) already opens every overlay file; it inspects
  section headings only. **One finding id, not a mechanism.** → A7.
- **The inherited C6-a fixture debt — DOES NOT EXIST (Amelia).** Discharged as Arc 7's A7-1 in
  B7-1; harness 21/21 green. The roadmap was carrying a **discharged** debt forward, and the real
  obligation ran the opposite way (E4 blocks the tag without a same-build harness case). → A9.

**Joint 5 largely dissolved** (Sally): B9-1 and B9-2 ship in the same release, so the field meets
D5's rule and its worked example together. What survived is a one-line conformance check → A11.

### Amendments applied (22) — each edited into the section it amends, marked `*(roundtable A#)*`

| # | Amendment | Landed at |
|---|---|---|
| **A1** | D6 re-scoped to bind new rules that constrain, not only widenings — else it cannot reach the four bell-less boundaries this arc itself creates | D6 |
| **A2** | D6's interim posture **is** `enforcement_stage: declared` + the deferral triple, not prose | D6 |
| **A3** | B9-3 and B9-4 each run D6's test on themselves and record the result | B9-3, B9-4 |
| **A4** | Q9's axis corrected to **carve-out-vs-clobber** — as worded it outlawed B9-4 two builds later | Q9 |
| **A5** | Q9 ships `enforcement_stage: checked` keyed to `vlt-upgrade`'s three existing report keys; each report line routes the addition to its durable host | Q9 |
| **A6** | Birth-time obligation: a build declaring a file module-owned names where vault-local additions of its kind live, or states none exist | Q9 |
| **A7** | Three bells for B9-4: `overlay_consumers_illegal` in the existing overlay check + upgrade reconcile line; mint-log backing for `local_consumers:`; *Convention coherence* extended to walk it | Q2, B9-4 |
| **A8** | Ruling 4c repaired: bound → **before v0.12.0 is tagged**; primary discharge → **re-run the lint pass**; locate attempt **before B9-1's brief**; unrecoverability becomes a **filing**; the self-certifying escape **struck** | Q10, ledger |
| **A9** | C6-a is discharged — struck; element (6) as a package-lint check needs a same-build harness case or **E4 blocks the tag** | B9-1, ledger |
| **A10** | Element (6)'s instrument is **factory-side, runnable at rest**; a `ledger.md` *Verify* bullet does not satisfy it | B9-1, ledger |
| **A11** | "No denominator moves" **stricken** → record the measured delta under both readings; B9-2's brief conforms B9-1's narrowing to D5 as authored | B9-1, B9-2 |
| **A12** | **Seventh** B9-1 scope item: narrow `ledger.md:26`'s blanket immunity to mirror Q4's split; element (2) names both sites | B9-1, ledger |
| **A13** | Transport URL declared as a **defined variable** — a flat scalar is silently dropped by `merge-config.py`, leaving `vlt-feedback` with no transport | B9-3 |
| **A14** | `marketplace.json` `skills[]` + a quoted 13-field CSV row; two `[ship-verifiable]` checks on the rail | B9-3 |
| **A15** | Rail: shaped paste-ready failure artifact; field-contract **version stamp**; **owner-applied** triage label + terminal `declined`; capture-state label; `origin:` idempotence vs `inbox/` **and** `archive/`; the header's single home moves into the shipped half | B9-3, B9-5, E3 |
| **A16** | **B9-5 is factory-only, in no release** (both its homes gitignored); v0.12.0's rationale corrected; `.github/` noted as extending the release-commit surface | release table, *Release contents* |
| **A17** | The rung gains an **author** (minting an overlay writes its pointer line); rung-as-digest recorded as a considered alternative; B9-7's brief carries a falsifier | Q8, B9-7 |
| **A18** | Q3's write-op qualifier stated on the **whole** set; **K1b is not "already-solved"** — its partner writer is carried to Arc 10 | Q3 |
| **A19** | Document shape: the terminal block no longer routes **backward to step 3**; three stale lead-ins corrected; D5's dual assignment removed from B9-1; `binds:` rosters added; through-line "four filings"→"five in-arc"; the *Amendment owed* note narrowed | many |
| **A20** | Ledger **partitions by release**; a v0.12.0 upgrade run is an **obligation**; E1/E3 name their discharging event | *Release contents*, ledger, E1, E3 |
| **A21** | Three field-facing items land in v0.12.0: direction 3 re-admitted as a **floor**; a field-facing PARA posture; **S2's negative branch pre-ruled** | Q8, D6, B9-6, brief-time |
| **A22** | D3 ruled **(i)**, reason recorded; **"seven-plus" → "nine consumers, ninth is an E5 asset node"** | D3 |

### Standing rules landed (5)

| # | Rule | Home |
|---|---|---|
| **R1** | **"No bump owed" is not "no cost."** An edit prices its *non-handshake* gates too: package-lint **C6** rule-card re-derivation + `RULE_CARD_BUDGET`, **E4** harness coverage for any new check, **E5** asset-node acks. | `.claude/skills/build-brief/SKILL.md` |
| **R2** | **A new shipped skill is not shipped until it is registered.** `marketplace.json` `skills[]` + a quoted 13-field `module-help.csv` row are scope items of the build that creates it. | `.claude/skills/build-brief/SKILL.md` |
| **R3** | **A ruling that names a build must be findable from that build.** Each build bullet carries a `binds:` roster of the ruling ids that govern it. | `.claude/skills/ideation-scaffold/SKILL.md` (lays it) + `build-brief` Discovery (reads it) |
| **R4** | **An append-only report's terminal routing line is authoritative.** Every lifecycle skill restamps it on exit; a stale one silently routes the next reader to the wrong step. | `.claude/skills/vlt-lifecycle.md` |
| **R5** | **A field-contingent debt names its discharging event and the vault it happens in**, or it is a wish. | `.claude/skills/build-brief/SKILL.md` §9 |

### Disputes — ruled live by the owner, dissents on record

- **DISPUTE 1 — D3, the two-bump problem** *(the joint ideation left OPEN)*. **RULED: (i), accept
  two bumps, reason recorded.** Carson's release-split fact turned it: B9-4 is v0.12.0 and B9-6 is
  v0.13.0, so two bumps is the handshake **working**, not the duplication D3 forbids. Amelia
  killed **(ii)** (widening a release ahead of its enforcement — violates D6) and **(iii)**
  (strands Q1's ruling an extra release). **Dissent (Carson):** option **(iv)** — ride Arc 10's
  already-owed `@9 → @10` bump — is cheaper across two arcs and now legal under D6; the owner
  declined to mortgage Arc 10's bump. **Composed with Dispute 2, the arc pays two bumps, not
  three.**
- **DISPUTE 2 — B9-2's siting.** **RULED: Paige's split by audience** — D5 → `CLAUDE.md` Standing
  rules; Q9 → the contract's *Durability across upgrades*; D6 → `frontmatter.md`'s *Enforcement
  declaration*. **Dissent (Dr. Quinn):** siting Q9 in the contract still exempts it from the
  `checks.md:37` meta-check and the `frontmatter.md:257` bell obligation, both `{conventions}`-only
  — the cheap siting is the one that escapes the doctrine. **Answered by A5** (a real enforcement
  declaration keyed to `vlt-upgrade`), which Quinn accepted **for this rule**; the dissent stands
  against the general principle that siting is a free choice.
- **DISPUTE 3 — closeout binding.** **RULED: binds to v0.12.0**, with B9-6/B9-7 as release-forward
  candidates that fold to Arc 10 unbuilt if their spike misses a named date. No dissent.
- **DISPUTE 4 — field-facing content in v0.12.0.** **RULED: all three land** — direction 3 as a
  floor; a field-facing PARA posture; S2's negative branch pre-ruled. Maya's charge (the interim
  posture was addressed to the factory, not the field) **upheld in full**. No dissent.

### Captured for `inbox/` — surfaced by the room, out of this roadmap's scope, not debated

1. **`check_group_b` never verifies that every shipped skill has a `module-help.csv` row** — a
   shipped skill can be invisible to the help surface with lint exiting 0 (the Agent Builder).
2. **A discharged debt (C6-a) was carried forward into a new arc's roadmap** — carry-forward
   hygiene defect in the closeout→capture seam (Amelia).
3. **`merge-config.py` silently drops non-variable top-level keys from `module.yaml`** — a
   silent-drop failure mode, the dangerous direction (the Agent Builder).

**Next lifecycle move:** **`brief build 1`** — `build-brief` for **B9-1**, the first build the
rulings name. No OPEN disputes gate it.

---

## Roadmap roundtable — the joints as taken to the room

*Convened 2026-08-20; the record above is the outcome. This section is the input the room
worked from, kept for provenance.*

**Joints this session created or left open, for the room to hunt.** These are not
re-litigations; each is a seam between rulings that are individually correct:

1. **D3's two-bump problem (OPEN, flagged in-session).** B9-4 and B9-6 both change
   `frontmatter.md`; under the version-handshake rule that is two bumps and two seven-plus
   consumer walks — the exact cost D3 exists to avoid. Three candidate resolutions are recorded
   at D3; **none is ruled.** This is the session's single largest unresolved joint.
2. **Q2's boundary with no bell (⚠ carried tension).** The overlay registration route is closed
   with **nothing detecting a violation** — the shape of the module's own *no boundary without
   a bell* doctrine, in the arc whose thesis is that unenforceable boundaries decay. Either the
   doctrine tolerates a documented-only boundary here for a stated reason, or a `vlt-lint`
   check is owed.
3. **D6's rule shipped an arc ahead of its mechanism.** Enshrined in B9-2 with a stated interim
   posture (PARA stays unwidened until Arc 10's lint family). **Test the posture** — this is
   precisely the fault pattern the review step exists to catch, and the owner's ruling stands
   unless the room finds the posture insufficient.
4. **Q3's over-admission risk.** Making the `verified_by` value set *be* the consumer roster
   holds only while every consumer is a write op. The mitigation ruled in (roster = ceiling;
   a `local_consumers:` registrant must be a write op) is prose, not a mechanism.
5. **B9-2 governs builds that come after it.** Three standing rules land early so they bind the
   arc — but B9-1 ships *before* B9-2 and is the worked example of D5's precedence rule. Does
   the arc's own first build predate the rule it exemplifies?
6. **E1–E4: a rail whose every declared risk is field-contingent.** B9-3 ships with four
   evidence debts, **none ship-verifiable**, so none gates closeout. Correct under
   `build-brief` §9 — but the room should say whether that is acceptable for an *ingress*
   mechanism the rest of the loop will depend on.
7. **Capture's own unclaimed findings.** Two findings in the roadmap are the clerk's reading,
   not field evidence (the `ledger.md:25`/`:26` conflict; the rule-card's unavailability as a
   host), plus three added this session (the `resolving`/`on disk` ambiguity; `:47` as a
   single-home violation; `relay.md:28`'s dual grant). **The room should weigh them as
   readings.**
8. **Location boundaries generally** — the arc's thesis question, carried from the joints table:
   is the module's habit of drawing boundaries by *path* the common root, and does any build
   address it? Q9 ruled *no single mechanism*; the room should test whether the doctrine alone
   is enough.

*A9-1 stated in its own text that the roundtable should not be waived. **A9-1 has left the arc
(Round 1)**, so that instruction travels to Arc 10 — but the eight joints above are Arc 9's own.*

## Live-acceptance ledger

*Populated at brief time — each build appends its acceptance checks here, tagged
**ship-verifiable** or **field-contingent**. Only ship-verifiable checks gate closeout.*

**⚠ THIS LEDGER PARTITIONS BY RELEASE** *(roundtable A20, 2026-08-20)*. Every entry below is
tagged **[v0.12.0 run]** or **[v0.13.0 run]** at brief time, and **a vlt-core upgrade run at
v0.12.0 is an obligation of the two-release split, not an option** — without it the split buys
none of the earlier acceptance it was ruled in to buy. **Arc closeout binds to v0.12.0**
(Dispute 3), so only entries tagged **[v0.12.0 run]** can gate it.

**Ideation-seeded, Round 5/6 (2026-08-20) — entered before any brief, because both are bounds
rather than build outcomes:**

- **Ruling 4c's three lint-surfaced module-feedback candidates — `[ship-verifiable]`, GATES
  Arc 9 closeout.** Filer: **owner**. Bound: **before v0.12.0 is tagged** *(roundtable A8 —
  amended from "before Arc 9's release", which the two-release split left indeterminate)*, and
  **added to that release's pre-flight so the gate fires at a moment that certainly happens
  rather than one contingent on two spikes.** **Discharges on** *(roundtable A8 — the gate as
  ideated could not fail and was therefore not a gate)*: **(1)** three dated filings in `inbox/`
  matching **the three named subjects** — the naive `spec_candidate` relay count's 6 repeat
  false positives; `vlt-lint-full.js` scanner prompts ignoring `frontmatter` rule 4's
  coexistence posture and the callout-vs-bullet distinction; `crossLayerSlugs` omitting
  `_agent/handoffs/`, `_agent/bases/` and `areas/` (recovered 2026-08-21 from Arc 7's Closeout
  record item 8 — **the content was never lost, only the pointer to it**); **or (2)** — primary mechanical route — **a re-run of the
  full `vlt-lint` pass on vlt-core that resurfaces them**, since the candidates are
  *lint-surfaced* and their content is therefore **not uniquely trapped in the vault-side
  report**; **or (3)** if the report is gone **and** the lint re-run returns empty, **a dated
  filing in `inbox/` recording that unrecoverability** — which is itself what discharges the
  gate. **A dated locate-attempt happens before B9-1's brief, not at closeout.** **This bound has slipped two
  arcs** (set Arc 7 closeout → bound by Arc 8 roundtable A15 to "before Arc 8's release" →
  MISSED at v0.11.0). Ruled Round 5 to carry the **B7-6 hard-gate mechanism** — the one that
  retired the four-arc A4-4 (5) debt — so a third miss cannot be recorded as a silence.
  **Recoverability caveat:** the candidates' content exists only in the owner's vault-side
  report. ~~no roadmap carries it.~~ **FALSE — corrected 2026-08-21:** Arc 7's Closeout record
  item 8 carries all three subjects verbatim; Arc 8 kept the pointer and dropped the substance,
  and this arc's capture inherited that error. ~~If that report is gone, closeout records the
  loss rather than carrying a fourth arc.~~ **STRUCK** *(roundtable A8)* — a self-certifying escape is how the
  first two slips were recorded, and it re-imported the soft bound this gate replaced. The
  caveat now applies **only if the lint re-run returns empty**, turning "the report is gone" from
  a **declaration** into a **checkable result** — and even then the outcome is a **filing**, not
  prose written at closeout about filings that do not exist.
  - ✅ **DISCHARGED 2026-08-21 via route (1)** — before the v0.12.0 tag, on the owner's
    go-ahead. Three dated filings in `inbox/`, content carried from Arc 7's Closeout record
    item 8 and grounded against module source at HEAD `86efd48` (v0.11.0):
    1. `inbox/2026-08-21-100000-spec-candidate-relay-count-six-repeat-false-positives.md` —
       still stands in narrowed form (the count remains cumulative with no per-run memory;
       the B5-4 decline path is the only suppression and did not stop the repeats in the field).
    2. `inbox/2026-08-21-100500-lint-scanner-prompts-skip-rule4-coexistence-and-callout-vs-bullet.md`
       — partially addressed (B7-6 added rule-4 normalization to the Gap B prompt); the
       coexistence posture and callout-vs-bullet distinction remain convention-read-dependent,
       not prompt-encoded.
    3. `inbox/2026-08-21-101000-crosslayerslugs-omits-handoffs-bases-and-areas.md` — still
       stands (`full-scale.md:7` assembles `crossLayerSlugs` from `{research}` plus a vague
       agent-zone parenthetical; `areas/` covered by no clause at all).
    The three-arc slip ends here; the filings await Arc 9/Arc 10 capture like any other inbox
    signal. This line is the pre-flight record for the v0.12.0 release gate.
- **The two spikes — `[ship-verifiable]`, gating their own builds, not the arc.** S3 closes
  before B9-6's brief; S2 (re-scoped) closes before B9-7's. Owner: the clerk, factory-side.
  **If S3 confirms the `vlt-upgrade` ordering trap, it files to `inbox/` as a defect in its own
  right** rather than being absorbed into B9-6.

**Pre-seeded, inherited from Arc 8 (bound):**

- **B8-2 (4) re-check — `[ship-verifiable]` from birth, GATES Arc 9 closeout.** The
  proto-`deliver` era test naming no datum (`relay.md:28`) and the undefined behaviour of a
  supplied `ref` on a pathless `handoff` (`relay.md:41`). Arc 9 also rules on the backward-compat
  exemption's *scope*, not only its datum. Filing:
  `inbox/2026-08-18-101612-proto-deliver-era-test-names-no-datum-and-handoff-ref-slips-its-key-rule.md`
  — **captured 2026-08-20 as A9-6** (capture run 2). Grounding added a third element the check
  must cover: the `ledger.md:25`/`:26` precedence conflict. **A re-check that states the datum
  but leaves the two bullets un-ordered will pass on paper and fail in the field again.**

  **Ideation (Round 3/4, 2026-08-20) assigned this to B9-1 and grew it to six elements**, two
  of which no filing claimed; **the roundtable added a seventh (A12)**. The re-check must cover
  **all seven** or it is not the check:
  (1) `ledger.md:25` narrowed to exclude both legacy lanes (Q5 — precedence eliminated, not
  ordered); (2) `relay.md:28`'s dual grant split so the exemption covers the **key requirement
  only** (Q4 — **this discharges Arc 8's bound scope question**); (3) the era datum stated as
  "before the first `deliver` pointer exists in this record", **including the no-`deliver`-at-all
  edge**; (4) `ref` on a `handoff` is **payload, never the key** (Gap 2); (5) the
  `resolving`-vs-`on disk` (location vs existence) ambiguity stated — **found in ideation, not
  by capture or the filing**; (6) candidate (c) built — `ledger`'s denominated lanes verify
  **lane membership against a stated derivation**, which is the instrument that makes this
  check's `[ship-verifiable]` tag mean something rather than discharging on a prose re-read.
  ~~**Element (6) touches the inherited C6-a fixture debt; the brief says which fixture it
  extends or creates.**~~ **CORRECTED** *(roundtable A9/A10, 2026-08-20)*: **C6-a is discharged**
  (Arc 7's A7-1, built B7-1; `tools/test-package-lint.py` **21/21 green**). The real obligation
  runs the other way — `_e4_harness_coverage` introspects the check inventory, so **element (6)
  landing as a `package-lint` check without a declaring case in `tools/test-package-lint.py`
  makes E4 fail and blocks the tag**; the brief prices that case as **scope**. And **element
  (6)'s instrument is factory-side and runnable at rest** — a `ledger.md` *Verify* bullet alone
  does not satisfy it, because the `[ship-verifiable]` tag is only true under a home that
  discharges at rest.

  **Element (2) is extended to name BOTH sites** *(roundtable A12)*: `relay.md:28`'s dual grant
  **and** `ledger.md:26`'s identical "counts, never findings" blanket immunity. Splitting one and
  leaving the other ships Q4's cure on one file and Q4's disease on the other, **with the
  diseased file ruled the winner by Q5.** A **seventh** scope item is added to B9-1 accordingly —
  so the re-check now covers **seven elements, not six.**

  ✅ **DISCHARGED 2026-08-21 (acceptance-discharge run)** — via B9-1 check (1), all seven
  elements: the shipped diff + cross-file greps (elements 1–5, 7; `4c4c8c4`) and the
  instrument (element 6): `uv run tools/dispatch-lane-check.py` re-run this session → PASS,
  15 cases / 2 fixtures, exit 0; red-then-green probe in the BUILT record. **The
  closeout-gating check is green.**

**Briefed builds:**

- [x] **build-B9-1 (dispatch-ledger-repair, briefed 2026-08-21)** — **[v0.12.0 run]**, brief
  `skills/reports/build-B9-1-dispatch-ledger-repair.md`. Three checks. **(1) `[ship-verifiable]`,
  GATES Arc 9 closeout — the B8-2 (4) re-check, all seven elements, discharged at rest:**
  elements (1)–(5)+(7) by the shipped diff and its cross-file greps (both blanket immunities
  replaced at `relay.md:28` **and** `ledger.md:26`; era datum stated once with the
  no-`deliver` edge; `:25` narrowed to exclude both lanes; `ref`-on-`handoff` payload
  sentence at `relay.md:41`; location-vs-existence stated at `ledger.md:28`); element (6) by
  `uv run tools/dispatch-lane-check.py` exit 0 against its fixture records **plus** the
  recorded red-then-green probe (per A10 factory-side/at-rest; per A9 no E4 case owed under
  the standalone-tool home — the priced package-lint deviation path is in the brief). This
  check discharges the pre-seeded B8-2 (4) entry above; the seven elements are defined there,
  not restated here. **(2) `[ship-verifiable]` — the A11 obligation stands discharged:** the
  brief records the pre-fix denominators on the real vlt-core dispatch record under both
  readings of `resolving` (legacy 15/15; annotated-pathless-pre-era 27/27 strict, 8/8 under
  the adopted key-failing membership; era 2026-08-18 10:21), the adopted readings (location
  for denominators, existence for the `handoff` finding), and the **measured delta: 0** (all
  22 written handoff-zone paths resolve under extension-optional wikilink semantics — the
  caveat that keeps the zero non-vacuous). **(3) `[field-contingent]`** — discharging event
  named per R5: **the owner's vlt-core upgrade to v0.12.0 (the A20 obligation) followed by a
  `vlt-dispatch ledger` run in ordinary use on vlt-core**; pass = the two denominated lines
  match the stated derivation over the live record, the seven 2026-08-15 pointers render
  inside the proto denominator (not findings, not zero), and no key-requirement finding is
  raised against either lane — the exact failure the pre-fix 0.11.0 run produced on this
  record.

  ✅ **ALL THREE DISCHARGED 2026-08-21 (acceptance-discharge run).** (1)+(2) at rest:
  instrument re-run PASS exit 0 this session; A11 record stands in the brief. (3) by the
  owner's post-upgrade `ledger` run on vlt-core (relayed in-session) **and independently
  re-derived read-only by a blind audit of `_agent/dispatch.md`**: 89 pointers, legacy 15,
  proto 8 (the seven 2026-08-15 `(handoff, ref:)` pointers + the 2026-08-17 15:12 ask —
  inside the denominator, not findings), era = first `deliver` 2026-08-18 10:21
  (`dispatch.md:322`), 0 live findings, every written handoff-zone path resolves
  (extension-optional case at `dispatch.md:418` exercised). *Audit note, not a defect: the
  instrument's fixture grammar does not parse the live record's richer annotation syntax
  raw — per A10 it is a fixture-record instrument; noted in the discharge report.*

- [x] **build-B9-2 (three-standing-rules, briefed 2026-08-21)** — **[v0.12.0 run]**, brief
  `skills/reports/build-B9-2-three-standing-rules.md`. Three checks. **(1)
  `[ship-verifiable]` — the three sitings landed as ruled, at rest** (Dispute 2's
  split-by-audience): D5's precedence bullet in project `CLAUDE.md` *Standing rules*
  (factory home, no handshake, citing B9-1 as the worked example); Q9's carve-out-vs-clobber
  doctrine + the A5 enforcement-declaration block (`enforcement_stage: checked`,
  `enforcement_checked_by: vlt-upgrade`, moment = post-flight divergence report) + the A6
  birth-time sentence in `vault-operating-contract.md` *Durability across upgrades*, with
  the rule card re-derived — **package-lint C6 PASS at the v0.12.0 gate is the discharging
  instrument** (card digest matches the edited contract, ≤ 8,000 bytes); D6's rule paragraph
  in `frontmatter.md` *Enforcement declaration* with `version: 8` deliberately untouched
  (the `@8 → @9` bump + nine-consumer walk fold into B9-4 per Dispute 2 / D3-A22 — the walk
  discharges under B9-4's checks); and `vlt-upgrade` Step 4's three divergence lines each
  routing to a durable host (A5's exit, grep-checkable). **(2) `[ship-verifiable]` — the
  A11 conformance record stands:** the brief records the re-read of B9-1's shipped
  `ledger.md:25/:26/:28` + `relay.md:28/:41` narrowing against D5 as authored — **CONFORMS**
  (overlap eliminated by population-narrowing, no precedence statement anywhere: D5's
  preferred branch), B9-1 cited in the rule text as worked example; discharged when the
  shipped D5 bullet carries the citation and the build-time re-verification agrees. **(3)
  `[field-contingent]`** — discharging event named per R5: **the owner's vlt-core upgrade
  to v0.12.0 (the A20 obligation run), on vlt-core**; pass = the post-flight report renders
  all three divergence keys in the shipped routing shape (never omitted when empty, per
  honest reporting) and any non-empty line carries its route-to-durable-host instruction
  rather than a bare re-apply/review; if all three render empty, only the render-shape half
  discharges — the exit's first live exercise rides the next real divergence (no vacuous
  "routing worked" tick against an empty report).

  ✅ **ALL THREE DISCHARGED 2026-08-21 (acceptance-discharge run).** (1)+(2) at rest: C6
  green inside `--expect-version 0.12.0` all-PASS (re-run this session, exit 0); A11
  conformance record stands. (3) **fully — including the routing half, not vacuously**: the
  post-flight report rendered all three divergence keys (`base_divergence: []`,
  `governance_divergence: []` rendered-when-empty per honest reporting), and
  `skill_asset_divergence` was **non-empty on first live exercise** —
  `vlt-agent-researcher/SKILL.md` routed to its durable host (capability-shelf read, owner
  ruling, ref-keyed decision-log entry `_agent/mint/decision-log.md:997`) rather than a
  standing re-apply; the vault's upgrade-ledger entry records "the standing re-apply
  treadmill ends" — the exit working on a real divergence in its first live run.

- [ ] **build-B9-3 (feedback-rail, briefed 2026-08-21)** — brief
  `skills/reports/build-B9-3-feedback-rail.md`. Four checks; (1)–(2) sit under the
  **"Discharges on the v0.12.0 run"** partition, (3)–(4) are field-contingent with named
  events per R5/A20. **(1) `[ship-verifiable]` — the rail is registered, agreed, and gated,
  at rest / at the v0.12.0 gate:** (a) package-lint C5 passes with `vlt-feedback` in
  `marketplace.json` `skills[]` **and** the FB `module-help.csv` row is present, quoted,
  13-field (explicit grep — lint never checks row presence, R2); (b) the contract-agreement
  fixture run recorded: `references/field-contract.md`'s field ids == both
  `.github/ISSUE_TEMPLATE/` forms' `id:` set == the composed payload's sections (A14 check
  (i)); (c) the `gh` degradation probe recorded: named `gh-missing` error + paste-ready
  failure artifact in `_agent/feedback-outbox/` with labels and origin-vault pre-written
  (A14 check (ii), amended E3); (d) all seven labels exist on the transport repo
  (`gh label list`, owner action bound **before the v0.12.0 tag**); (e) the D6 record
  stands — the mandatory rendered-payload preview-approval gate ships in `vlt-feedback`'s
  own protocol text (roundtable A3; brief disposition 1). **(2) `[ship-verifiable,
  v0.12.0 run]` — the transport arrives in a live vault:** on the owner's vlt-core upgrade
  to v0.12.0 (the A20 obligation run), `config.yaml`'s `vlt:` section carries
  `feedback_repo` (defaulted via merge-config's defined-variable path, A13), the live
  `module-help.csv` carries the FB row post-merge, and `vlt-feedback` + its reference are
  on disk. **(3) `[field-contingent]` — E1 + E3, one named event per A20/R5:** **a
  `vlt-feedback` run from the work machine's app-vault, performed by the owner, bound
  before Arc 9 closeout** — E1 discharges when the posted issue's origin-vault field
  correctly names app-vault while the GitHub author is the owner's account; E3 discharges
  on *either* that successful run *or* a recovered failure artifact. Vault: app-vault
  (vlt-core cannot produce this event). A missed bound is recorded at closeout as a miss,
  never a silence; neither gates closeout. **(4) `[field-contingent]` — E2 scrub-gate
  efficacy:** discharges **only** on a filing carrying real personal-domain signal whose
  posted payload shows the gate scrubbed or blocked it — a machinery-only filing must not
  tick this (capture's instruction). Event: the first personal-domain-adjacent filing from
  any live vault; unschedulable by nature and named as such.

  📋 **SPLIT 2026-08-21 (acceptance-discharge run): (1)+(2) DISCHARGED; (3)+(4)
  STILL-OPEN.** (1) at rest: C5 + FB row inside the all-PASS gate; contract-agreement and
  `gh` degradation runs in the BUILT record; all seven labels verified live (`gh label
  list`, 2026-08-21); preview gate in shipped text. (2) on the vlt-core upgrade, blind
  audit: `_bmad/config.yaml:29` `feedback_repo: mggower/bmad-module-vlt`;
  `_bmad/module-help.csv:26` FB row quoted; `vlt-feedback/SKILL.md` +
  `references/field-contract.md` on disk in the vault. STILL-OPEN as of the first
  discharge run: (3)+(4); **updated 2026-08-21 (second discharge pass): (3) DISCHARGED** —
  the owner's app-vault `vlt-feedback` runs produced issues #2 and #3 on the transport repo
  (authored by the owner's account, `origin_vault: app-vault`, `module_version: 0.12.0`,
  `rail_contract: 1`, `vault-filed`+`field:defect` auto-applied — E1's condition verbatim);
  E3 discharges on the success branch (`gh` pre-flight clean on the work machine, per the
  entry's either/or wording; the degrade path stays a standing watch, exercised at build
  only). **STILL-OPEN: (4)** E2 — first personal-domain-adjacent filing from any live
  vault (unschedulable, named; both live filings were machinery-only and correctly do not
  tick it). Does not gate closeout.

- [ ] **build-B9-4 (consumer-registration, briefed 2026-08-21)** — **[v0.12.0 run]**, brief
  `skills/reports/build-B9-4-consumer-registration.md`. Three checks. **(1)
  `[ship-verifiable]` — the two walks are bipartite-consistent and the route + bells
  shipped, at rest / at the v0.12.0 gate:** package-lint Group E PASS with all nine
  consumers at `frontmatter@9` (incl. `vlt-lint-full.js`'s `// depends_on:` header, E5's
  leg) and all four at `write-verification@3`; the single `@8 → @9` bump covers **both**
  rule changes (`local_consumers:` + B9-2's deferred D6 paragraph — the d8707bf obligation
  discharged); `write-verification.md:47` reads as roster + A18's write-op qualifier on the
  whole set with the narrow-attest text intact; `frontmatter.md:82` is a pointer; the
  vault-writable member set carries `local_consumers:` with mint-backing/ack/ceiling
  properties; all three A7 bells present with R3 legal responses
  (`overlay_consumers_illegal` in *Overlay append-only*; `local_consumer_unsanctioned` +
  the `local_consumers:` stale/unacknowledged/dangling walk in *Convention coherence*; the
  vlt-upgrade Step-4 retirement annotation); the A21 F7 floor (checksum-compare before the
  `vlt-vitals.py` overwrite — sha256/real differ, never bare `diff` — + three-outcome
  Confirm line) and the A21 F8 changelog PARA posture present in shipped text. Discharged
  by the `--expect-version 0.12.0` gate exit 0 plus the brief's recorded greps and fixture
  probes. **(2) `[ship-verifiable]` — the D6 self-test record stands:** B9-4 is a widening
  shipped with all three bells in the same build, no interim posture (brief disposition 6),
  or the BUILT record's numbered deviation names the slipped bell and the
  `write-verification.md` posture sentence shipped instead. **(3) `[field-contingent]`** —
  discharging event named per R5/A20: **the owner's vlt-core upgrade to v0.12.0 (the A20
  obligation run), on vlt-core — the one vault carrying the live owner-adopted overlay
  `consumers:` line, so the Q1-consequence-1 retirement is exercised exactly here.** Pass =
  the post-flight report renders the retirement annotation on that overlay's line (never
  silence); the next `vlt-lint` run flags `overlay_consumers_illegal` with its route; the
  owner's re-registration (`local_consumers:` entry + dated `ref:`-keyed mint entry,
  overlay line removed) clears it; the coherence walk then covers the registrant (the
  vlt-sweep stale-ack class becomes detectable rather than structurally invisible). The
  Confirm vitals line renders in the three-outcome shape; with no local vitals edit at
  upgrade time only the render-shape half discharges — no vacuous tick. **Plus an
  arc-closeout obligation, not a check: the carry-forward carries the disposition-4 PARA
  posture (A21's factory-side half).**

  📋 **SPLIT 2026-08-21 (acceptance-discharge run): (1)+(2) DISCHARGED; (3) upgrade-side
  DISCHARGED, two first-exercise tails STILL-OPEN.** (1)+(2) at rest: Group E inside the
  all-PASS gate; D6 satisfied by named bells, no interim posture. (3) upgrade-side, blind
  audit + upgrade-ledger: the retirement annotation rendered (pre-flight recorded both
  overlays carrying `consumers: [vlt-sweep]` with "retirement annotation due"; post-flight
  rendered it inline) and the owner ruled the retirement **in the same run** — `frontmatter.overlay.md:47-49`
  dated §C stub, `write-verification.overlay.md` retired whole, **no `consumers:` line on
  any overlay post-run** (so `overlay_consumers_illegal` is **vacuous — the precondition
  was lawfully eliminated before any lint run**; the finding id is installed in the vault's
  lint surface, `checks.md:42`); re-registration landed and cleared structurally —
  `local_consumers: [vlt-sweep]` in both live bases (frontmatter@9 `:13`,
  write-verification@3 `:13`), pins bumped (`vlt-sweep/SKILL.md:3`), both rulings ref-keyed
  in `_agent/mint/decision-log.md:989,:997`; vitals Confirm = silent-refresh outcome
  (hook byte-identical across live/asset/module, sha256 match) — **render-shape half only,
  per this check's own no-vacuous-tick clause**. STILL-OPEN tails: **(a)** first
  post-upgrade `vlt-lint` run exercising the `local_consumers:` coherence walk on the live
  registrant (trigger: owner's next lint cycle on vlt-core — last lint 5 days pre-upgrade);
  **(b)** the vitals overwrote-local-edits branch's first exercise (unbounded — watch, per
  the check's wording). Neither gates closeout.

- [x] **build-B9-5 (factory-intake, briefed 2026-08-21)** — **[factory-local — no release
  run]** *(A16: B9-5 ships in neither version; this bullet sits outside both release
  partitions by construction — its ship-verifiable checks discharge at rest on the factory
  machine and depend on no upgrade run, so they may gate closeout without touching Dispute
  3's v0.12.0 bound)*, brief `skills/reports/build-B9-5-factory-intake.md`. Three checks.
  **(1) `[ship-verifiable]` — the intake exists, is safe, and excludes correctly, at
  rest:** (a) all four file surfaces landed (`inbox-capture` Discovery step + headless
  `issues_materialized` key, the new `references/github-intake.md` mechanics reference,
  `arc-closeout` Stage 5's issue-close transition, the `inbox/README.md` archival clause)
  with the pointer-discipline grep clean (contract cited, never restated); (b) the
  recorded double Discovery dry-run against the real repo — `--label vault-accepted` empty
  **before** the issue-#1 backfill, issue #1 listed-then-**excluded** by the `origin:`
  token (matched decoration-tolerantly against the A9-3 filing's hand-written header)
  **after** it — plus the recorded stale-shape fixture probes (`rail_contract: 0` and
  no-stamp both route to hand-handling, never materialization; a conforming body parses to
  a well-formed temp filing). Discharges when the BUILT record carries the recorded runs.
  **(2) `[ship-verifiable]` — issue #1 reconciled:** `gh issue view 1` shows
  `field:defect,vault-filed,vault-accepted,captured`, state OPEN (A9-3 is captured, not
  archived); before/after in the BUILT record; owner action bound **in-build**. **(3)
  `[field-contingent]`** — first real end-to-end materialization, event named per R5/A20
  by **riding B9-3 check (3)'s already-bound event**: the issue produced by the owner's
  app-vault `vlt-feedback` run (bound before Arc 9 closeout) is owner-triaged
  `vault-accepted` and the next `inbox-capture` run materializes it — bare `origin:`
  header written, `captured` applied, issue left open, stamp check passed on a genuine
  `rail_contract: 1` body. Vaults: app-vault produces, the factory materializes. Does not
  gate. The Stage-5 terminal half (closing an archived filing's issue) first fires when a
  materialized filing archives — named, unbounded by nature, watched not gated.

  📋 **SPLIT 2026-08-21 (acceptance-discharge run): (1)+(2) DISCHARGED; (3) STILL-OPEN.**
  (1)+(2) at rest per the BUILT record's recorded runs; issue #1 re-verified live this
  session (`gh issue view 1`: OPEN, labels `vault-filed, vault-accepted, captured,
  field:defect`). STILL-OPEN as of the first discharge run: (3);
  **updated 2026-08-21 (second discharge pass): (3) DISCHARGED — first real end-to-end
  materialization ran.** The app-vault issues #2 (14:43:52Z) and #3 (14:45:54Z) were
  owner-triaged `vault-accepted` (owner-authorized in-session), and the intake ran per
  `github-intake.md` steps 1–5: stamp gate passed on genuine `rail_contract: 1` bodies,
  issue #1 correctly excluded by its `origin:` token (no re-materialization, no label
  drift), bare-header filings written (`inbox/2026-08-21-144352-…` and
  `inbox/2026-08-21-144554-…`), `captured` applied, both issues left open. The Stage-5
  terminal half (issue-close at archival) remains a named, unbounded watch — first fires
  when a materialized filing archives.

**Owner action, not a capture item:**

- **Ruling 4c — three lint-surfaced module-feedback candidates, bound MISSED (Arc 8).** Never
  filed, so nothing exists to capture. Owner-filed by design; raise at ideation.

---

**Next lifecycle move:** **`arc-closeout` is electable — or S3 first to decide B9-6/B9-7's
fate before closing.** Second discharge pass ran 2026-08-21: the app-vault rail runs
produced issues #2/#3 (E1 verbatim: owner-authored, `origin_vault: app-vault`, stamps
present, labels auto-applied; E3 on the success branch) — **the pre-closeout E1/E3 bound
is MET**; owner triage + the intake's first live materialization discharged B9-5 (3)
(issue #1 excluded correctly, filings `2026-08-21-144352`/`-144554` written, `captured`
applied). Ticked: B9-1, B9-2, B9-5. Open, non-gating: B9-3 (4) E2 (unschedulable watch);
B9-4 (3)(a) first post-upgrade lint cycle on vlt-core + (3)(b) vitals overwrote-branch
(watch). **All closeout-gating checks GREEN; the v0.12.0 tag exists — Dispute 3's
precondition holds.** Before or at closeout the owner rules: B9-6/B9-7 fold-to-Arc-10 vs
running S3/S2 now (S3 is clerk-owned — sayable as 'run spike S3'); the A9-4 filing's
early release over the E2 tail (rubric: owner call). 5 uncaptured filings sit in `inbox/`
for the next capture run — incl. the hand-folded #1-comment amendment posing B9-6's
narrow-vs-general scope choice, which argues for capturing **before** briefing B9-6.
*(Routing history: brief build 1 →
build B9-1 [BUILT @ 4c4c8c4] → brief build 2 → build B9-2 [BUILT @ d8707bf] → brief build
3 → build B9-3 [BUILT @ 2f1d757] → brief build 4 → build B9-4 [BUILT @ c813cb9] → release
staged → v0.12.0 RELEASED @ 336d90b → brief build 5 → build B9-5 [BUILT 2026-08-21, no
commit per A16] → this stamp, 2026-08-21.)*

*(Superseded stamp, kept for history:)* **build B9-5** — lifecycle step 6. The brief is written
(`skills/reports/build-B9-5-factory-intake.md`, BRIEFED 2026-08-21; its three acceptance
checks are in the Live-acceptance ledger above under the explicit **[factory-local — no
release run]** partition — (1)–(2) `[ship-verifiable]` at rest, (3) `[field-contingent]`
riding B9-3 check (3)'s bound event) — a **fresh builder session** implements it via
`bmad-workflow-builder`. Builder exit obligations: rewrite the brief `status:` to a BUILT
record with numbered deviations, delete any `.decision-log.md`, and — **per A16, deviating
from the standard ritual — NO commit**: all five F-surfaces plus the brief itself are
gitignored; the build ends with the BUILT record on disk. The build includes one in-build
owner action (brief §F5: the issue-#1 four-label backfill, before/after recorded).
Grounding corrections issued at B9-5 brief time: **0** (every roadmap premise HOLDS —
issue #1 OPEN/unlabeled verified live, the A9-3 filing's decorated `origin:` header at
`:4` reconciled by decoration-tolerant matching, brief disposition 2; siting precision
only: arc-closeout's Stage 5 lives in `references/closeout-checklist.md:84-113`, not
SKILL.md). The B9-5 brief-time question was found already discharged by A15/B9-3 —
superseding note written at §Questions deliberately left to brief time. **In parallel:
live acceptance** — the owner's vlt-core upgrade run to v0.12.0 (the A20 obligation; it
opens the **[v0.12.0 run]** partition), then `acceptance-discharge`. **Waiting:** B9-6 on
S3, B9-7 on S2 (v0.13.0). *(Routing history: brief build 1 → build B9-1 [BUILT @ 4c4c8c4]
→ brief build 2 → build B9-2 [BUILT @ d8707bf] → brief build 3 → build B9-3 [BUILT @
2f1d757] → brief build 4 → build B9-4 [BUILT @ c813cb9] → release staged → v0.12.0
RELEASED @ 336d90b (tag pushed; both pre-tag gates discharged — seven labels created,
ruling 4c's bound DISCHARGED via route (1), see the annotated ledger entry) → brief build
5 → this stamp, 2026-08-21.)*

*(Superseded stamp, kept for history:)* **build B9-4** — lifecycle step 6. The brief is written
(`skills/reports/build-B9-4-consumer-registration.md`, BRIEFED 2026-08-21; its three
acceptance checks are in the Live-acceptance ledger above — (1)–(2) `[ship-verifiable]`,
(3) `[field-contingent]` under the **[v0.12.0 run]** partition with its event named per
R5/A20) — a **fresh builder session** implements it via `bmad-workflow-builder`. Builder
exit obligations: rewrite the brief `status:` to a BUILT record with numbered deviations,
delete any `.decision-log.md`, one commit for the build. **B9-4 is v0.12.0's release
build**: after the BUILT record lands, the next move is **release v0.12.0** via
`vlt-release` (dual bump, `--expect-version 0.12.0` gate, PASS line in the commit), gated
on the two pre-tag owner actions — the B9-3 `gh label create` sequence and ruling 4c's
before-the-tag bound (brief §8). **The deferred-bump obligation from d8707bf is priced in
this brief** (disposition 1 / F1): one `frontmatter@8 → @9` bump covering both
`local_consumers:` and B9-2's D6 paragraph, nine-consumer re-ack incl. the
`vlt-lint-full.js` `// depends_on:` header. Grounding corrections issued at B9-4 brief
time: **0** (every roadmap premise HOLDS; line shifts only — B9-2's edits moved the
contract cites to `:117/:118/:120/:124` and the vault-writable member set to
`frontmatter.md:278`; fresh lines are in the brief's F-sites). The owed wrapped-`diff`
grep is discharged clean (brief disposition 2 — no shipped doc instructs a raw
base-vs-baseline `diff`; no retrofit owed). The two A21 v0.12.0 items are ruled in
(dispositions 3–4): the clobber-legibility floor lands at `vlt-setup` §2b/Confirm (F7),
the field-facing PARA posture in the v0.12.0 `CHANGELOG.md` entry (F8) + the arc
carry-forward at closeout. A18 recorded: K1b's partner-writer half is carried to Arc 10,
not solved here.
*(Routing history: brief build 1 → build B9-1 [BUILT 2026-08-21 @ 4c4c8c4] → brief build 2
→ build B9-2 [BUILT 2026-08-21 @ d8707bf] → brief build 3 → build B9-3 [BUILT 2026-08-21
@ 2f1d757] → brief build 4 → this stamp, 2026-08-21.)*

*(roundtable A19 / standing rule **R4**, 2026-08-20: this block previously routed the reader
**backward to lifecycle step 3** — instructing an `ideation-scaffold` run and re-posing three
scope questions Round 1 had already ruled — while the frontmatter and the roundtable section
said step 4. One artefact, two contradictory routing statements, and the reader trained to trust
the end of a document got the wrong one. The scope questions live, answered, under **Capture's
scope questions**.)*

---

## Closeout record (2026-08-21) — CLOSED, do not append

**Gate:** PASSED. v0.12.0 tagged and pushed (336d90b). Ledger: B9-1, B9-2, B9-5 ticked with
dated evidence; B9-3 and B9-4 remain `- [ ]` **honestly** — each open only on
`[field-contingent]` sub-clauses, which per the tagged-ledger rule move to the watch
register and do not gate. The tick count is not a measure of what the arc proved: B9-3 and
B9-4 discharged every at-rest, gate-time, and upgrade-side sub-clause; their boxes stay
open because their field tails do.

**Archive criteria applied (per-filing, Arc-3 rule):** A9-6's filing archived (all clauses
discharged, 2026-08-21, by acceptance-discharge). **Held active, own clauses live:** A9-1
(Arc 10 whole), A9-2 (B9-6 Finding 4/5 folded + the coherence-walk first exercise), A9-3
(B9-6 folded + the 2026-08-21 amendment), A9-4 (E2 watch), A9-5 (B9-7 folded). Their
issues mirror: #1 stays open. No filing archived under condition-2 this close.

**Carried forward past Arc 9** (authoritative — Arc 10's capture re-lists from here):

1. **B9-6 + B9-7 — FOLDED TO ARC 10 UNBUILT** (owner ruling 2026-08-21, in-session;
   Dispute 3's release-forward mechanism, Arc 3 → build-17 → Arc 5 precedent). v0.13.0 was
   not shipped by this arc. Spike obligations S3 (metric-home ordering) and S2 (rung
   re-scope) ride with them, clerk-owned. **Arc 10 ideation owes the narrow-vs-general
   ruling** posed by the A9-3 filing's 2026-08-21 amendment (the operating contract has no
   overlay mechanism — the durable-host doctrine's three hosts do not cover the file that
   states the doctrine; compounds with issue #2's divergence-net defect).
2. **E2 — scrub-gate efficacy** `[field-contingent]` standing watch: first
   personal-domain-adjacent filing through the rail; machinery-only filings must not tick
   it (both 2026-08-21 filings correctly did not).
3. **B9-4 (3)(a)** — first post-upgrade `vlt-lint` cycle on vlt-core exercises the
   `local_consumers:` coherence walk on the live registrant (trigger: owner's next lint
   run; near-term — last lint was 5 days pre-upgrade).
4. **B9-4 (3)(b)** — the vitals overwrote-local-edits Confirm branch, first exercise
   (unbounded watch; silent-refresh branch exercised 2026-08-21).
5. **Disposition-4 PARA posture** (A21's factory-side half) — carried per B9-4's ledger
   obligation; the field-facing half shipped in CHANGELOG v0.12.0.
6. **B9-5 Stage-5 terminal half** — issue-close at first materialized-filing archive
   (unbounded watch; will first fire when a materialized filing's build ships and passes).
7. **Rail degrade path untested in field** — `gh` pre-flight was clean on both app-vault
   runs, so the paste-ready outbox artifact has run only against build-time fixtures
   (app-vault agent's flag, 2026-08-21). Standing watch, not a debt.
8. **`tools/dispatch-lane-check.py` fixture-grammar note** — the instrument does not parse
   live-record annotation syntax (per A10 it is a fixture instrument; blind-audit note
   2026-08-21). Candidate if anyone points it at a live record.
9. **8 uncaptured 2026-08-21 filings in `inbox/`** await Arc 10 capture: the three
   ruling-4c recoveries (100000/100500/101000), the two report filings (124500/124800),
   the two rail-materialized defects (144352/144554 — issues #2/#3, `captured`), the
   comment-blindness defect (150500), the dependency-manifest candidate (150800). Plus the
   pre-Arc-9 held-active register in `inbox/` (unchanged by this arc).
10. **Inherited registers** (C6-c, B5-3..B5-9, pre-Arc-5, the Arc-7 standing watches) —
    carried through this arc unexercised; re-list from the archived roadmaps.

**This arc is archived — do not append.**
