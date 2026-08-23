---
title: 'Build #21 — history-writes (make the module write its own history honestly)'
status: |
  BUILT 2026-07-17 — all nine fixes (F1–F9) shipped; unit-verified at rest; one commit.
  Deliverables: F1 extraction.md base — version 2→3, last_updated→2026-07-17, `vlt-track` named
  as the one module-shipped op in *Personalized extraction*, false clause deleted at both :47
  and :121, replaced with the per-partner-retired/per-op-live statement (base for shipped, overlay
  for vault-local). F2 consumer walk — vlt-extract/vlt-lint/vlt-track all re-acked extraction@2→3
  (bipartite-consistent, zero @2 pins remain); vlt-track self-authorization reconciled at the
  former :98 block. F3 vlt-mint — stale :141 `.decision-log.md`→`_agent/mint/decision-log.md`;
  new "### The mint decision log — entry schema + supersession idiom" subsection (kind schema +
  supersedes/superseded_by idiom, single-homed). F4 new asset
  `vlt-mint/assets/decision-log-template.md` (header + read-order + schema + idiom + placeholder-only
  worked example). F5 vlt-setup:237 seeds the log header-only from the template when absent, never
  clobbers. F6 vlt-upgrade — general write-path rule as Reconcile item 7 (trigger + `vlt-mint`
  pointer, no imported mechanics) + F6 exit gate in Verify + `decision-log-write` in migrations_run.
  F7 upgrade-ledger header states strict-oldest-first read order. F8 human-gated
  `decision-log-reconcile` migration with the pre-schema honesty surface + migrations_run enum. F9
  derive-first invariant sentence + sibling pointer at the Step-1 snapshot/ledger seam.
  VERIFIED: extraction@ bipartite re-check (all @3, none @2, version 3); false clause absent from
  the shipped surface (only dev-artifact reports mention it); only the legit legacy
  `.decision-log.md` migration mention survives in vlt-mint; template carries no live vault paths;
  package-lint A/B/C PASS (D skipped — not the release build); no stray per-skill `.decision-log.md`
  in the tree.
  DELIBERATE DEVIATIONS:
  (1) F2 also lightly reconciled vlt-track's Verify firewall line (former :113) — "the calling
  partner's op carries the gated sanction" → "base for `vlt-track` itself, a gated overlay mint for
  a domain op's own extension". The brief scoped the vlt-track text reconciliation to the :96/:98
  block; :113 asserted the same now-corrected reading (a literal reader would think plain vlt-track
  use needs a gated mint), so it is reconciled in the same clause family to avoid re-seeding the
  exact misread the build removes. In-scope-in-spirit; recorded because it is beyond the literal
  brief site.
  (2) F6 placement: the general write-path rule landed as Reconcile **item 7** (after the Provision
  hand-off) rather than as a new "## Step". Rationale: a new top-level Step would force renumbering
  Step 4/5 (widely referenced) and inserting item 6 would break the in-prose "Step-6 provision"
  references at :46/:135. Item 7 satisfies the brief's trigger + exit-gate + pointer with sites in
  Step 3 (item 7), the post-flight migrations_run enum, and Verify — no existing reference disturbed.
  (3) Both `decision-log-write` (F6) and `decision-log-reconcile` (F8) were added to the
  migrations_run enum (the brief named migrations_run as an F6 site and specified the F8 value).
module_code: 'vlt'
created: '2026-07-17'
derives_from:
  - 'inbox/2026-07-17-090000-extraction-grant-authorizes-nobody.md (A3-14 — extraction naming gate: name vlt-track in base, delete the false clause; extraction@2→3)'
  - 'inbox/2026-07-17-090500-upgrade-rulings-never-reach-the-decision-log.md (A3-15 — decision-log write path, entry schema + template + seed, bespoke supersession idiom, general upgrade-ruling write path, Fix C ledger read-order)'
  - 'inbox/2026-07-12-114940-sayari-060-upgrade-field-evidence.md (A3-11 §4a — the derive-first invariant, stated once)'
roadmap: 'skills/reports/inbox-evolution-arc3-roadmap.md'
rulings: 'roadmap §Ideation rulings A3-7..A3-17 (2026-07-17), build-21 row + §Owner rulings capture-run-2 (gate 3 = "under": name vlt-track, keep the naming gate) + decide-once rulings (supersession bespoke-now-converge-later; misattribution root gets a GENERAL write path; A3-14 + A3-15 its first two instances)'
risk: 'moderate — one convention rule change (extraction@2→3) triggers a 3-consumer walk; the rest is skill prose + one new mint asset + a seed step, no other version moves. Not the release build; the module 0.6.0→0.7.0 bump rides the arc''s last build.'
---

# Build #21 — history-writes

The module tells the wiki never to silently overwrite a claim and tells specs never to
supersede silently — while its own canonical governance record, the mint decision log, has no
supersession concept at all, and while a shipped skill (`vlt-track`) is told to refuse the very
op the module ships it to perform because a base clause insists "no skill shipped with the
module uses it." This build makes the module write its own history honestly. It closes three
threads that share one root — *vault-local or upgrade-time history narrated wrongly, or not at
all, in module source*:

- **A3-14** — the extraction convention names no shipped op, so `vlt-track:96`'s
  "must already be sanctioned by its own gated mint" is unsatisfiable-by-construction for the
  one op the module itself ships. Gate 3 ruled *under*: keep the per-op naming gate, name
  `vlt-track` in the **base**, delete the false clause. A rule change → `extraction@2→3` +
  consumer walk.
- **A3-15** — upgrade-time and mint-time rulings terminate at the upgrade ledger or the report
  and never reach the mint decision log, which has no entry schema, no template, no seed, and
  no supersession idiom. This build gives it all four and defines the **general rule** the
  misattribution root demanded: an upgrade-time ruling propagates to the decision log **and**
  any governing prose whose assertions it changes — never the ledger alone.
- **A3-11 §4a** — every Step-1 enumeration in `vlt-upgrade` is disk-derived by construction,
  but the **derive-first** invariant is enacted and nowhere stated, so nothing stops a future
  session reading the prior ledger as the preserve checklist. State it once.

All rejected alternatives in the parent filings are settled — do not re-litigate. In
particular: A3-14's §4 "delete the naming requirement as a relic" is **refused** (grounding
C6: the module never had a registry table; the naming clause is live original v0.3.0 design —
deleting it would repeal live design, not retire a relic); A3-15's Fix A "put the whole rule in
`vlt-upgrade`" is **refused** as single-home violation (entry mechanics live in `vlt-mint`);
Fix C's "ship it newest-first" is **refused** (contradicts the load-bearing append-only
invariant at `vlt-upgrade:104`). The accepted shapes are below.

## Brief-time dispositions

These resolve the four questions the roadmap deliberately left to build-21's brief
(§"Questions deliberately left to brief time" → build-21: Q9, Q10, Q20, Q22), plus the live
home the Q21 ruling requires.

1. **§4a is one sentence at the snapshot/ledger seam; no lint check (Q9).** Place the
   derive-first invariant at `vlt-upgrade` Step 1 where the snapshot and the opening ledger
   entry touch (the current line 42 seam, under the "always, from the living vault" heading),
   because that is exactly where the conflation is available to make — a session writing the
   ledger half could reach for the prior ledger as its inventory. One sentence naming the
   failure it prevents ("*the preserve set is derived from the live vault every run — never
   read from the prior ledger entry, which records what a past upgrade found, not what this one
   must protect*"). **No new lint check:** the behavior is already correct-by-construction
   (`:34`, `:38` derive from disk); a check would police a negative that no shipped code
   violates — the gap is a *stated* rule, not an *enforced* one, and over-building it into lint
   is the over-engineering grounding warned against.

2. **Derive-first is stated at this layer with a pointer, not hoisted to a new arc-wide home
   (Q10).** Single-home argues for one statement; but the two live instances are different
   concrete rules over different mechanics — the enforcement-counter derive-first (counters
   derive from event records, not a stored tally) and this preserve-set derive-first (the
   inventory derives from the live vault, not the prior ledger). Forcing a shared abstract home
   now is premature abstraction — the same posture the same ideation session ruled for
   supersession ("bespoke now, converge later"). So: state it at the `vlt-upgrade` seam and add
   a one-line pointer naming it as the same **derive-first discipline** the enforcement counters
   follow. Two concrete homes, cross-linked; no third abstract one this build.

3. **Do not invert the upgrade posture this build (Q20 / Fix D).** The filing offered "refuse
   to proceed on unaccounted-for gated convention edits" explicitly *as a question, not a
   recommendation*. It inverts the net's stated posture (`vlt-upgrade:102` — "does not
   auto-merge either") and would change the contract at `:102`/`:129`. Build-21's write-path
   work does not require the refusal posture, and A3-15's ruled scope names the write path, the
   supersession idiom, and the general write-path rule — **not** Fix D. Deferred (see Out of
   scope); the current detect-and-report posture stands.

4. **The migration prompts, human-gated; it never auto-sweeps or auto-writes (Q22).** The
   §5 migration surfaces decision-log entries recording a gated convention edit with no
   accounted-for superseding entry, for a human to reconcile — mirroring the overlay-subsumption
   pass (`vlt-upgrade:67`, human-gated, `migrations_run`) and the "do not auto-restore anything"
   constraint at `:64`/`:66`. **Honesty bound (grounding, A3-15 §5):** entries predating this
   build's entry schema carry no `kind` field, so they cannot be mechanically classified — the
   migration scopes cleanly only over post-schema entries; pre-schema entries get a one-time
   "cannot classify — review manually" surface, never a silent skip and never an auto-write.

5. **The supersession-convergence debt gets a live home this build (Q21, already ruled
   "bespoke now, converge later").** The decision log ships its **own** supersession idiom here
   (F3), mirroring `wiki-supersession.md`'s page-level frontmatter block and `spec.md:63`'s
   "Never silent — the same visibility principle." The governance-wide convergence (wiki + spec
   + decision log as three consumers of one supersession convention) is recorded as a **named
   debt with a live home** — appended to the roadmap's Deferred-acceptance/carry-forward
   surface so `arc-closeout` carries it forward, never parked in a closable note (A3-13's
   lesson: a surfaced defect whose deferral nothing tracks is its own failure).

## F1 — `extraction.md` base: name the shipped op, kill the false clause, bump the rule

**Current state.** `skills/vlt-setup/assets/governance/_meta/conventions/extraction.md`:
- `:11-12` — `version: 2`, `consumers: [vlt-extract, vlt-lint, vlt-track]`.
- `:47` — the *Scope of the allowance* paragraph contains "*This is **not** a standing license,
  and **no skill shipped with the module uses it** — the general `vlt-extract` draws on the
  wiki only.*" The bolded clause is false: `vlt-track` is a shipped op that uses personalized
  extraction (`vlt-track:96`, `:113`).
- `:121` — the flow parenthetical repeats it independently: "*No shipped op uses this; a domain
  op opts in per its gated mint — see* Personalized extraction *above.*"

**The exact change (gate-3 shape, roadmap `:1491-1508`).**
- Add a **module-shipped named op** to the *Personalized extraction* section: `vlt-track` is
  named in the base as the one shipped op sanctioned to use personalized extraction (it is
  module-shipped and cannot rely on a vault-local overlay for its own authorization — the
  surviving core of A3-14 C5). Vault-local ops continue to be named via the overlay route
  (`vlt-mint:131`), unchanged.
- **Delete the false clause at both `:47` and `:121`.** Replace with an explicit, correct
  statement: *per-**partner** authorization was retired at 0.3.0; per-**op** naming remains
  live — a shipped op is named in the base, a vault-local op in the overlay.* Two enforcement
  sites, not one — the fix must touch `:47` **and** `:121` (grounding: both assert it
  independently).
- **Bump `version: 2 → 3`.** Naming an op is a rule change (gate 3; `vlt-mint:139` — prose
  clarification alone would not bump, but naming an op does, and the two ship together, so one
  coordinated bump). Update `last_updated`.

**Why.** `vlt-track:98`/`:113` enforce "the calling partner's op carries the gated
personalized-extraction sanction" — unsatisfiable-by-construction for `vlt-track` itself while
the base names zero shipped ops. Gate 3 ruled the naming gate stays live and `vlt-track` is
named in the base.

**Out of scope at this site:** A3-14 §4.5 (annotate `consumers:` semantics in every convention
file) — rejected as completeness-drift across 8 files (grounding C8); the "`consumers:` is a
handshake map, not an authorization" negative, if stated at all, is a single pointer at
`vlt-mint:136`, not build-21 work (no filing folded here asks for it).

## F2 — `extraction@3` consumer walk + `vlt-track` text reconciliation

**Current state.** All three consumers pin `extraction@2`:
- `skills/vlt-extract/SKILL.md:4` — `depends_on: ["extraction@2", "wiki-supersession@1", "frontmatter@4", "write-verification@1"]`
- `skills/vlt-lint/SKILL.md:4` — `depends_on: ["frontmatter@4", "wiki-index@2", "wiki-supersession@1", "extraction@2", "write-verification@1", "spec@1"]`
- `skills/vlt-track/SKILL.md:4` — `depends_on: ["extraction@2", "wiki-supersession@1"]`

**The exact change (the base-edit ceremony, `vlt-mint:136-141`).** Walk every listed consumer;
for each, make the matching edit if its text encodes the changed rule, then bump its
`depends_on` `extraction@2` → `extraction@3`. Reconciliation may legitimately conclude "no edit
needed" — the ack bump still records a human verified it.
- **`vlt-track`** — text reconciliation **is** needed here: `:96` and the block after
  ("*must already be sanctioned by its own gated mint … If you are running a loop for a partner
  whose op was never granted the widening, **stop***") reads as though `vlt-track`'s own
  authorization comes only through a *calling partner's* overlay mint. Now that `vlt-track` is
  named in the **base**, reconcile that language so it does not read as forbidding the shipped
  op from its own base-granted sanction. Keep the calling-partner gate for the *personalization
  target* (a domain op still needs its own gated mint to extend the section for its own
  landing zone); the reconciliation narrows to `vlt-track`'s self-authorization, not the
  partner-op gate. Bump `:4` to `extraction@3`.
- **`vlt-extract`** — draws on the wiki only, does not use `personalization_sources`; verify
  no text change needed, bump `:4` ack.
- **`vlt-lint`** — its personalized-extraction check (method/general claim in a log) is
  unchanged by naming a shipped op; verify, bump `:4` ack. A `vlt-lint` ack covers its
  `vlt-lint-full.js` workflow asset (`vlt-mint:140`) — confirm that asset encodes no clause the
  rule change touches.

**Exit gate (mandatory, `vlt-mint:141`).** The build cannot close while any `consumers:` skill
still pins `extraction@2`. Verify bipartite-consistent: every consumer in `extraction.md:12` ↔
every ack at `@3`.

**Why.** CLAUDE.md version-handshake rule: a convention rule change bumps `version:` and
re-acks every consumer in the same build.

## F3 — `vlt-mint`: decision-log entry schema + bespoke supersession idiom + fix the stale path

**Current state.** `skills/vlt-mint/SKILL.md`:
- `:141` — the *Edit a convention* Step-4 exit-gate line ends "*it only records the mint +
  council verdict in `.decision-log.md`*" — a **stale pre-relocation path**. Every other site
  in the skill says `_agent/mint/decision-log.md` (`:59, :61, :66, :95, :108, :112, :131, :157,
  :159`). `:141` is the `convention edit` kind's own recording instruction — precisely the kind
  A3-15's repeal is about — and it names the clobber-prone location `:61` retired and
  `vlt-upgrade:47`/`:74` exist to destroy. A vault following `:141` literally writes to the
  file the module spends three sites deleting (grounding, A3-15 ⚠ defect 1).
- The skill defines *where* the log lives (`:61`) and *that* entries are recorded (`:95`,
  `:108`, `:131`, `:157`) but **no entry schema and no supersession concept** exist anywhere in
  module source (grounding, A3-15 ⚠ defect 2 + Fix B).

**The exact change.**
- **Fix `:141`:** `.decision-log.md` → `_agent/mint/decision-log.md`. Small edit, directly in
  the blast radius of the exact kind this build hardens.
- **Define the entry schema** (single-home: `vlt-mint` owns entry mechanics — this is where
  `:59`, `:61`, `:66`, `:95` already live). A minimal structured entry: `kind:` (mint / capability
  change / convention edit / stage promotion / **upgrade ruling** / retirement), date, the verdict +
  reasoning, and — for a `convention edit` — the convention + version delta. The `kind:` field
  is what makes the F8 migration mechanically scopable going forward.
- **Add the decision-log's own bespoke supersession idiom** — when a later ruling supersedes an
  earlier logged decision, the new entry carries a supersession pointer and the superseded entry
  is marked, never silently overwritten. Mirror the two shipped idioms verbatim in spirit:
  `wiki-supersession.md:50-55` (page-level frontmatter: `superseded_by` / `superseded_date` /
  `superseded_reason`) and `spec.md:63` ("*Never silent — the same visibility principle as
  `wiki-supersession.md`*"). This is **bespoke to the decision log** this batch (Q21 ruling);
  the governance-wide convergence is the named debt in disposition 5.

**Why.** A3-15 GAP CONFIRMED: the module has a fully-developed supersession idiom deployed
twice, applied to the decision log zero times; and the log has no schema, "*which is the
structural reason the gap exists*." The `vlt-core` ledger firewall ruling
(`upgrade-ledger.md:48`) had nowhere to land a superseding entry.

**Registration/handshake note:** none — this is skill prose + a new asset (F4). The decision
log is not a versioned convention; no `version:`/`consumers:` moves here (A3-15 handshake note).

## F4 — NEW asset: `vlt-mint/assets/decision-log-template.md`

**Current state.** `skills/vlt-mint/assets/` holds `capability-template.md`,
`operation-skill-template.md`, `partner-agent-template.md` — **no decision-log template**
(grounding, A3-15 Fix B). The log is created ad hoc by whichever mint runs first, with no
header and no defined entry shape.

**The exact change.** Add `skills/vlt-mint/assets/decision-log-template.md`: a header block
plus one worked entry demonstrating the F3 schema and the supersession idiom. The header
**states the read order** (append-only ⇒ strict oldest-first) so a reader knows what a
well-ordered file looks like — the same treatment F7 gives the upgrade ledger. Use placeholder
paths only (`_agent/mint/…`, `{partners}/{name}/…`), never a live install's artifact paths
(CLAUDE.md publishing rule; build-15/18 precedent).

**Why.** "*There is no shipped artifact to ship the discipline in*" (A3-15 Fix B). The template
is the shipped home for the schema F3 defines and the seed F5 lays down.

## F5 — `vlt-setup`: seed the decision log from the template

**Current state.** `skills/vlt-setup/SKILL.md:237` — "*Ensure the mint institutional-memory
zone `_agent/mint/` exists … Create it if absent; never clobber existing contents.*" It ensures
the **directory** but never seeds the log (grounding, A3-15 Fix B: "*`vlt-setup:237` ensures the
directory exists but never seeds the log*").

**The exact change.** At `:237`, when `_agent/mint/decision-log.md` is absent, seed it from the
F4 template (header only — the worked entry stays in the template as documentation, not seeded
as real history). Preserve the existing never-clobber discipline: seed only when absent.

**Why.** So the log exists with a header and a defined shape from install-time, rather than
being conjured header-less by the first mint — "*that absence is what let a repeal have nowhere
to land*" (A3-15 Fix B).

## F6 — `vlt-upgrade`: the general upgrade-ruling write path (trigger + exit-gate + pointer)

**Current state.** `skills/vlt-upgrade/SKILL.md` treats the decision log as an object to
**preserve**, never to **write**: `:38` (confirm exists), `:74` (relocate a legacy file), `:135`
(Verify: "exists"). An upgrade-time user ruling terminates at the upgrade ledger (`:42`, `:104`)
or the post-flight report (`:81`), never the decision log (grounding, A3-15 CONFIRMED —
"*every path terminates at the ledger or the report*").

**The exact change (the decide-once "general write path" ruling, roadmap `:1694-1698`).** Define
the **general rule, once**, at `vlt-upgrade` (where upgrade-time rulings happen): *an
upgrade-time user ruling propagates to the mint decision log **and** to any governing prose
whose assertions it changes — never the ledger alone.* `vlt-upgrade` carries the **trigger**
(when a ruling is made during an upgrade), an **exit gate** (the upgrade cannot close while a
recorded gated ruling has no corresponding decision-log entry — well-formed wording matching
`vlt-mint:141`/`:159` precedent), and a **pointer** to `vlt-mint` for the entry *shape* (Fix A
split: `vlt-mint` owns the entry mechanics, `vlt-upgrade` owns trigger + gate + pointer, sites
`:65`, `:95` `migrations_run`, `:135`). Do **not** import entry mechanics into `vlt-upgrade`
(single-home; A3-15 Fix A refused).

- **First two instances, named in the rule** (roadmap `:1698`): **A3-15** (the firewall ruling
  that should have superseded the decision log — `vlt-core/_agent/upgrade-ledger.md:48`) and
  **A3-14** (an upgrade/mint-time ruling that changes governing prose — `extraction.md` — must
  also reach the log). Cite both as the rule's first applications; the fixes remain separable,
  only A3-14 carries the `extraction@2→3` handshake (gate 3).

**Why.** The misattribution root: rulings recorded only in the ledger leave the governing prose
(and the decision log) asserting a stale reality. One rule, defined once, closes the class.

## F7 — `vlt-upgrade`: state the upgrade-ledger read order (Fix C)

**Current state.** `vlt-upgrade:104` — the ledger is "*append-only … never rewritten*"; the
header template at `:106-113` states the **write** discipline but never the resulting **read
order**, so a file that has drifted out of order (as `vlt-core`'s did — grounding, A3-15 Fix C)
announces nothing.

**The exact change.** Add one line to the ledger header template (`:108-110` block) stating the
read order: faithful append-only yields **strict oldest-first**; a file not in that order has
been hand-edited. **Reject** "ship it newest-first" (contradicts the load-bearing `:104`
invariant — A3-15 Fix C). This is the same treatment F4 gives the decision-log header.

**Why.** A3-15 Fix C, ACCEPTED as the filing's own alternative. Small, same-filing residual;
its only home is here. *(Scope note: the `vlt-core` ledger scramble itself is vault-local drift,
**not** a module defect — grounding rejected the filing's "aggravating factor" attribution. The
module fix is only the missing header statement.)*

## F8 — `vlt-upgrade`: human-gated migration for unaccounted gated convention edits

**Current state.** No migration scans the decision log for gated convention edits whose
superseding entries are missing (grounding, A3-15 §5: "*One found. Nobody has swept for
others.*").

**The exact change (Q22 disposition 4).** Add a migration in Step 3, mirroring the
overlay-subsumption pass (`:67`) exactly: it **surfaces** decision-log entries recording a
gated `convention edit` (or `upgrade ruling`) with no accounted-for superseding entry, for a
human to reconcile — **never auto-writes, never auto-restores** (consistent with `:64`/`:66`).
Record `decision-log-reconcile` (or similar) in `migrations_run` (`:96`) when it fires; follow
the standing relocation-migration discipline at `:72` if any move results. **Honesty bound:**
scopes cleanly only over post-F3-schema entries (they carry `kind:`); pre-schema entries get a
one-time "cannot classify — review manually" surface, `log()`-visible, never silent (CLAUDE.md
no-silent-caps posture).

**Why.** A3-15 §5 GAP CONFIRMED; the migration "*as specified cannot be mechanically scoped
today; it depends on the schema work, which orders the build*" — F3 supplies the schema, so the
migration ships in the same build but honest about the pre-schema tail.

## F9 — `vlt-upgrade` Step 1: the derive-first invariant, stated once (A3-11 §4a)

**Current state.** `vlt-upgrade:30` — "*## Step 1 — Pre-flight (always, from the living
vault)*"; `:32` "*while the vault is intact — its snapshot is the restore source*"; `:34`/`:38`
derive every enumeration from disk; `:42` "*Write this snapshot to a working note and append the
opening half of a ledger entry*." The behavior is correct-by-construction; a
`grep -rni "derive-first|prior ledger|from disk"` across the shipped surface returns **zero
hits** (grounding, A3-11 §4a) — the rule is enacted, never stated.

**The exact change (dispositions 1 + 2).** Add **one sentence** at the `:42` snapshot/ledger
seam: the preserve set is derived from the live vault every run — never read from the prior
ledger entry, which records what a *past* upgrade found, not what *this* one must protect. Add a
one-line pointer naming it the same **derive-first discipline** the enforcement counters follow
(the sibling instance). No lint check; no arc-wide abstract home this build.

**Why.** A3-11 §4a, the only live material in that filing: within 2 days of the 07-09 sayari
upgrade the vault grew 4 light capabilities, 1 minted skill, and a family — none in any ledger
inventory; nothing stated stops a future session reading the prior ledger as the preserve
checklist. This is the derive-first invariant at a second layer.

## Registration

The `extraction@2→3` consumer walk (F2) is the only registration-surface event: it re-acks
three consumers and is exit-gated at `vlt-mint:141`. No new skill, no new workflow, no
`module-help.csv` row (the decision-log template F4 is an asset, not a callable op). **No module
`module_version` bump** — build-21 is not the release build; the 0.6.0→0.7.0 bump rides the
arc's last build. The convention `version:` bump (extraction 2→3) is independent of the module
version.

## Out of scope (dispositioned)

- **Fix D — upgrade refuses to proceed on unaccounted gated edits (Q20).** Deferred — inverts
  the `:102`/`:129` contract; offered as a question, not in A3-15's ruled scope. Arc-4 candidate.
- **Governance-wide supersession convention (wiki + spec + decision log as three consumers).**
  Deferred per Q21 ruling ("bespoke now, converge later"); recorded as a named carry-forward
  debt (disposition 5) so `arc-closeout` carries it — not built here.
- **A3-14 §4.5 — annotate `consumers:` semantics per convention file.** Rejected: completeness-
  drift across 8 files (grounding C8). At most a single pointer at `vlt-mint:136`, not folded here.
- **A3-14 delete-the-naming-clause (§4).** Refused (gate 3): live original v0.3.0 design, not a
  relic.
- **`vlt-track:16` inline-loop-profile drift / A3-11 §3.** Belongs to A3-17 → build-22; filed as
  a build-11 field defect (`inbox/2026-07-17-100000`).
- **`vlt-core` ledger heading-order scramble.** Vault-local drift, not a module defect
  (grounding, A3-15 Fix C); the module fix is only F7's header statement.

## Verification (unit, at rest)

- **Handshake bipartite re-check (F1/F2):** `grep -n "extraction@" skills/*/SKILL.md
  skills/*/assets/*.js` — every consumer in `extraction.md:12` pins `extraction@3`, none pins
  `@2`; `extraction.md` `version: 3`. Every consumer listed ↔ every ack current.
- **False-clause gone:** `grep -rn "no skill shipped with the module uses it\|No shipped op uses
  this" skills/` → zero hits; the corrected per-op/per-partner statement present at both former
  sites; `vlt-track` named in the base *Personalized extraction* section.
- **Stale path gone (F3):** `grep -rn "\.decision-log\.md" skills/vlt-mint/SKILL.md` → only the
  legitimate relocation-migration mention (the *legacy* `.decision-log.md` being moved), never a
  live write target; `:141` now writes `_agent/mint/decision-log.md`.
- **New asset + seed (F4/F5):** `skills/vlt-mint/assets/decision-log-template.md` exists,
  carries the schema + supersession idiom + read-order header, placeholder paths only;
  `vlt-setup:237` seeds from it when absent, never clobbers.
- **Write path + migration (F6/F8):** dry-read `vlt-upgrade` Steps 1/3/5 for the general
  rule, the exit gate, the `vlt-mint` pointer (no imported entry mechanics), and the
  human-gated migration with its pre-schema honesty surface; `migrations_run` enum (`:96`)
  carries the new value.
- **Derive-first sentence (F9):** present at the `:42` seam with the sibling pointer;
  `grep -rni "derive-first\|prior ledger" skills/vlt-upgrade/SKILL.md` now returns it.
- **Read-order statements (F4/F7):** both the decision-log template header and the upgrade-
  ledger header template state oldest-first; neither says newest-first.
- **Scrub:** no personal/vault-local content or live artifact paths in any changed shipped file;
  worked examples use placeholder paths (CLAUDE.md publishing rules).
- **No packaging-lint version gate this build** (D/`--expect-version` is the release gate);
  a mid-arc A/B/C `package-lint.py` run is fine to confirm structure but does not gate the
  commit.

Not the release build — no `--expect-version` gate, no dual version-string bump; the module
version bump rides the arc's last build.

## Acceptance (live — appended to the roadmap ledger)

Rides the next ordinary `vlt-core` (and/or `vlt-sayari`) upgrade:

- **A3-14 downstream (vlt-sayari, gate-2 non-vacuous):** at sayari's next upgrade past this
  build, `extraction.overlay.md:13` (which names `vlt-track`) becomes **base-subsumed** — the
  build-18 overlay-subsumption pass should fire and offer to retire that now-redundant overlay
  section. A real overlay that *could* have failed (a ~pre-fix section), correctly detected —
  valid discharge evidence, not engineered.
- **A3-15 write path:** the first live upgrade that makes a gated ruling writes a real
  supersession-bearing entry to `_agent/mint/decision-log.md` (not the ledger alone), and the
  seeded log carries the template header on a fresh install. The `vlt-core` firewall ruling
  (`upgrade-ledger.md:48`) gets its superseding decision-log entry when next reconciled.
- **F8 migration:** on a live decision log with a pre-existing unaccounted gated edit, the
  migration surfaces it human-gated (never auto-writes) and honestly flags pre-schema entries it
  cannot classify.
- **A3-11 §4a:** the derive-first sentence is present and a post-upgrade session preserves
  disk-derived local growth (capabilities/mints/families) without consulting the prior ledger as
  its checklist — observable on the next sayari-style "grew-4-capabilities-since-last-upgrade"
  run.

## Next lifecycle move

A **fresh builder session** implements this brief via `bmad-workflow-builder` (lifecycle
step 5). Exit obligations for that session: rewrite this brief's `status:` to a **BUILT**
record with numbered deliberate deviations; delete any `.decision-log.md` left in the working
tree (CLAUDE.md standing rule); **one commit** for the build (`vlt build-21 — history-writes`).
Unit-verify at rest per the Verification section — the `extraction@3` bipartite re-check is the
load-bearing ritual (a convention `version:` moved).
