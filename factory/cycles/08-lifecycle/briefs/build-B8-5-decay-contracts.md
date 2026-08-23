---
title: 'Build #B8-5 — the decay contracts: rotate/drain verbs, retention-at-birth, and the mass/age wires (the agent zone finally gets a decomposer — every accumulating record gains a declared exit)'
status: 'BUILT 2026-08-17 — vlt-decay shipped (SKILL.md + references/rotate.md + references/drain.md; rotate + drain verbs, tend by pointer to vlt-groom, invoked-only citing vlt-groom''s trigger model, type `decay` named); Decay-contracts table landed in the operating contract (after the safety model, A13 sentence closing it) with contract :36/:122 updated and :37/:41/:44/:47 reaffirmed; log-mass (log_bytes >= 262144) + drain-due (oldest_drainable_section_days > 45) wires appended to the seed with the bar sentence verbatim and the count wording updated; oldest_drainable_section_days derived in vlt-vitals.py beside the dispatch block, log_bytes/backlog_bytes definitions gained the live-only clause; R-9/R-11 widened (checks.md:47 relay-count + decline read, vlt-upgrade:80) to read the {archive}-mirrored siblings; vlt-lint:72 and daily.md:63 reaffirmed-with-clause, ledger.md live-record denominator clause added; registered (marketplace skills[], quoted 13-col csv row DC, README 16). Verification: fixture rotate PASS (ingests_since_lint 2→2, days_since_lint 77→77, Step-0 baseline identical, log_bytes 404→308, archive+tail byte-identical to pre-rotation, second rotate no-op, never-linted refuses loudly with nothing moved); fixture drain PASS (open_pointers 2→2, oldest_open 7→7, per-slug greps identical, newest daily/ per source + consult block retained, ## Open byte-identical, oldest_drainable 108→0, widened live+archive reads reproduce pre-drain counts, second drain no-op); wires PASS (4 wires render, parse_wires zero errors, trip states correct either side of both thresholds, merge-by-id gains exactly log-mass+drain-due with local threshold >= 20 and local wire intact); greps PASS ("two stock wires" zero hits, bar sentence present, metric id defined once, :441-443 discharge comment present + diff-clean, frontmatter.md/consult.md diffs empty, no depends_on on vlt-decay); package-lint A/B/C/E PASS with Group E zero handshake motion. Deviations/notes: (1) THE RELEASE STEP WAS NOT RUN — no version bump, no --expect-version lint, no tag: the release is separately gated on owner approval; acceptance check 5 is deferred-to-release. (2) The decay table carries four exempt rows beyond the brief''s enumerated list ({specs}, {capabilities} + partner capabilities/, {conventions}/{personas}/{contract}, {index} folded into the wiki row) so Verification 4''s structure-table walk actually closes. (3) ledger.md:38''s example "0 of 2 wires tripped" updated to "0 of 4" — a stale-count reconciliation outside F7''s list (the B7-8 posture). (4) README "15" appeared at four sites, not two — all four updated to 16, and the roster table''s Hygiene row widened to include vlt-decay (it heads a completeness-claiming list). (5) Rule-card re-derived (sha256 + its Hygiene map row now names the Decay contracts table) — the contract changed and C6 gates on the hash. (6) drain.md cites vlt-dispatch''s ledger reference by prose, not by references/ path — the C7 router-integrity check reads a references/ token as an own-skill route.'
module_code: 'vlt'
created: '2026-08-17'
derives_from:
  - 'inbox/2026-08-16-093429-append-only-agent-files-have-no-decay-contract.md (A8-1 — the no-decay-contract gap: dispositions (a)–(d) + the traveling non-goals; the rotate/drain half of the three-verb taxonomy; the mass/age trigger)'
roadmap: 'skills/reports/inbox-evolution-arc8-roadmap.md'
rulings: >-
  roadmap §Ideation rulings (2026-08-17): grouping row B8-5 + roundtable A10 (tend
  resolves by pointer to B8-4's groom; derive-first reader enumeration + rotation-safety
  invariants + fixture check; prose reconciliation per surface; newborn sweep; per-vital
  archived-siblings ruling); pre-ideation ruling 1 + A12 (disposition 8 REOPENED; the
  vlt-vitals.py discharge comment is B8-4's carrier, B8-5 verifies present); pre-ideation
  ruling 2 + A11 (the decay-contract wire CLASS admitted; one canonical metric id per
  wire, mass and age never share one; count/thresholds at brief time; bar sentence stays,
  count wording updates same build); cross-filing ruling 1 as amended by A6 (the safety
  model's SHIPPED home — cited, never restated); cross-filing ruling 3 (A8-1/A8-3
  separation BINDING); cross-filing ruling 4 / A14 (lint-scope split: partner-file
  finding classes are (f)'s lint territory; mass/age is this build's sibling machinery —
  neither brief re-rules the split); cross-build rule A13 (no new accumulator without a
  stated decay contract); dispute D2 (owner-ruled: B8-4's brief is the decide-once home
  for the hygiene-execution idiom, interim default invoked-only; B8-5 adopts or records
  an owner-ruled divergence); A7 (any B8-5 frontmatter schema change carries its own
  explicitly-named bump — B8-3's bump is not assumed).
risk: >-
  moderate — the build touches the operating contract, the tripwire seed, the vitals
  reader, and the read-side derivations of three skills, and it is the arc's release
  build. It bumps NO convention version (disposition 6 below: no frontmatter.md edit, no
  consult.md edit — verified by design, Group E must show no handshake motion) and adds
  one skill, so the consumer-walk surface is registration (C5/help/README), not re-acks.
---

# Build #B8-5 — the decay contracts

Arc 8's charge is that the module's write discipline has no time axis. B8-1..B8-4 gave
finding classes legal responses, pathless deliveries a shape, partner memory contracts and
a groom op. B8-5 closes the arc where the arc's first filing opened it: **every remaining
operational accumulator in the agent zone gets a declared decay contract, and the two
mechanical decay verbs — rotate and drain — ship with the wire that rings when they are
due.** The trigger half was deliberately deferred at B5-9 ("disposition 8 — display-only");
the owner reopened it fully on this filing's field evidence (pre-ideation ruling 1), and
the tripwire seed's own bar ("add a third only when a real failure earns it") was ruled met
by the same filing (ruling 2/A11).

All rejected alternatives in the parent filing are settled — do not re-litigate. The
filing's non-goals travel into this brief **verbatim** and bind the build: **no in-place
LLM rewriting of records** (per the shipped safety model's gated-rewrite clause, read as
"no *ungated* in-place rewriting" — contract, *Hygiene and grooming*, third bullet); **no
binary compression** (archives stay readable markdown); **no new ever-growing hygiene
ledger** (state lives in the files' own watermarks); **agent-zone hygiene is a sibling of
`vlt-lint`, not folded into its wiki niche** (cross-filing ruling 4 makes this binding:
mass/age machinery is this build's; staleness/duplication finding classes on partner files
are disposition (f)'s lint territory — this brief does not touch that boundary).

The safety model is **cited, never restated**: the operating contract's *Hygiene and
grooming — the safety model* section (`vault-operating-contract.md:270-277`, shipped by
B8-3 per A6 clause (i)) governs every act below — retirement by reference, watermarks not
ledgers, mechanical acts council-free, and the derivability clause this brief's reader
table exists to discharge.

## Brief-time dispositions

The roadmap left to this brief: the disposition mix (a)–(d), the wire metrics/thresholds/
count, and (per A10/A13/D2) the reader invariants, prose reconciliations, newborn sweep,
per-vital ruling, and the execution idiom. Headless run — every call below is the
briefer's, recorded at the point it applies.

**1. Disposition mix — (a)+(b-partial)+(d) built; (c) already shipped; tend by pointer.**
- **(a) Retention-at-birth: ADOPTED, homed in the operating contract** as a **Decay
  contracts table** (F4) — one row per operational file class: its verb (or exemption with
  a one-line reason), its trigger, its archive destination, its watermark form. The
  contract is deliberately un-handshaked (single-home + pointers), so this creates **no
  version bump**. The table closes with A13 formalized as shipped text: *a new
  accumulating agent-zone file class enters this table in the act that creates it — no
  accumulator without a declared decay contract.* The filing's `retention:`-frontmatter
  sketch is **not** adopted: the primary accumulators (`{log}`, `_agent/dispatch.md`,
  `{backlog}`) carry no frontmatter by design, so a frontmatter key cannot cover the class
  it targets; a per-class table beside the safety model can (and avoids the `frontmatter.md`
  bump A7 would otherwise demand — see disposition 6). This satisfies A13's "formalized
  once B8-5 ships": the *form* is the table row, and it lives where the safety model lives.
- **(b) The verb taxonomy: rotate + drain ADOPTED, shipped as one new skill `vlt-decay`
  (F1). Tend is a POINTER** — A10 is binding: partner-memory tending resolves to B8-4's
  `vlt-groom` (the single home); this build ships **no second thread mechanism**. The
  decay table's partner-memory row is a pointer at `vlt-groom`, nothing more.
- **(c) The safety model: ALREADY SHIPPED — grounding correction.** The capture carried
  (c) as a candidate; B8-3 seated its shipped home (contract `:270-277`) and both
  watermark fields (`frontmatter.md:222-227`, `version: 8`). This build **cites** it and
  builds nothing for it.
- **(d) Trigger: ADOPTED as two wires + one new canonical metric** (disposition 2). The
  filing's "execution is a scheduled headless run" clause is **NOT adopted** — see
  disposition 3.

**2. Wire design — two wires in the admitted class; one metric id each; mass ≠ age (A11).**
The alert-fatigue budget, re-judged at brief time: the registry goes 2 → 4 wires. Each new
wire's trip is discharged by one cheap, mechanical, invoked act, and thresholds are set so
that at the filed field rates (~26K/week of `{log}` growth) each rings roughly quarterly —
the same cadence class as the two stock wires, not a new nag surface.
- **`log-mass`** — metric **`log_bytes`** (existing id — the roadmap's Sharpening 1: the
  mass vocabulary already exists; this wire is a registry entry, zero new metric code),
  threshold **`>= 262144`** (256K — just under the filed 259K-at-10-weeks pain point, so
  the first field trip is the adoption bell by design), owner `librarian`, moment
  `SessionStart strip + ledger`, `surface_text` phrased as the responding act per B8-1's
  ruled exception (a wire's legal response homes in `surface_text`): *"live {log} bytes —
  rotate the log (`vlt-decay`)"*, `review_after: 2027-02-28` (the threshold is
  n=1-evidenced; the wire schema's own required `review_after` is its recalibration hook).
- **`drain-due`** — metric **`oldest_drainable_section_days`** (**new** canonical id —
  the age facet the roadmap says is the unbuilt half of (d); F2 defines and derives it),
  threshold **`> 45`**, owner `librarian`, same moment, `surface_text`: *"days the oldest
  drainable dispatch section has sat closed on the live board — drain the board
  (`vlt-decay`)"*, `review_after: 2027-02-28`.
- **Not wired**: `backlog_bytes`, `index_bytes`, `partner_memory_bytes` stay display-only.
  Reasons on record: the backlog drain rides the same `drain` invocation the dispatch wire
  already summons (one bell per verb, not per file); the index is not an accumulator (lint
  repairs it in place); a partner-memory wire would nag toward scheduled grooming, against
  D2's invoked-only default and `vlt-groom`'s gate-needs-the-user design.
- Per A11, the seed header's **bar sentence stays verbatim** ("the alert-fatigue budget is
  a hard constraint") and the **count/ordinal wording updates in this build** (F3) — the
  bar now governs any *fifth* wire outside the decay class.

**3. Execution idiom — invoked-only ADOPTED (D2); no owner-ruled divergence exists or is
sought.** `vlt-groom`'s *Trigger model* (`vlt-groom/SKILL.md:23-25`) is the decide-once
home: *"Hygiene machinery may detect and suggest; only an invocation executes."*
`vlt-decay` cites it and conforms: wires and the ledger's vitals block **suggest**; a verb
runs only on explicit invocation. No scheduler, no tripwire-fired execution, no
upgrade-time auto-run. (The filing's weakly-held "scheduled headless run" preference is
thereby declined — recorded here as required, with D2 as the governing ruling.)

**4. Watermark form — content-derived cut points plus a one-line breadcrumb; no
frontmatter on the accumulators.** Rotate and drain are **content-idempotent**: rotate's
cut point is *everything strictly before the newest `lint` header* (re-run: nothing
precedes it → no-op); drain's is *block/item eligibility* (re-run: nothing eligible →
no-op). Progress state therefore needs no counter and no ledger — satisfying the safety
model's watermark clause in dispatch's own native idiom (a header-line watermark, exactly
"routed through line N" generalized): each verb leaves/updates **one breadcrumb line**
beneath the file's title, e.g. `> rotated through [2026-08-01 09:00] →
{archive}/_agent/log.md` — one line updated in place (mechanical hygiene metadata, not
record content), **never an appended series**. `frontmatter.md`'s `compacted-through:` /
`archive:` keys are **not written by this build**: they remain the watermark form for
frontmatter-bearing files (the groom's `groomed:`/`archive:` use stands); the judgment
that a cut point derivable from content needs no stored watermark is recorded here.
Consequence: `_agent/dispatch.md` still carries no frontmatter — `daily.md:63` is
**reaffirmed**, not falsified (F7).

**5. Per-size-vital ruling — archived siblings do NOT count, all four vitals, ruled in
this build (A10's exit-side clause).** `log_bytes`, `backlog_bytes`, `index_bytes`,
`partner_memory_bytes` each measure the **live file(s) only**. Grounds: cross-filing
ruling 2 as amended by A2 — *files retired to cold storage under the safety model are
outside live-read enumerations by design; vitals measure wake-read mass, not vault mass.*
This is the point of the verbs: the vital dropping after a rotation is the signal working.
F2 writes the ruling into the two METRICS definition strings a verb actually touches
(`log_bytes`, `backlog_bytes`); the ruling covers the other two identically with no code
change (they already read live paths only; groom retires by reference, creating no
sibling files).

**6. No convention version bump — verified by design (A7 discharged).** This build edits
**neither** `frontmatter.md` (disposition 1 and 4 route around it deliberately) **nor**
`consult.md` (disposition 7 makes consult blocks drain-exempt precisely so the
convention's "a `consult:` block in `_agent/dispatch.md`" sentences stay literally true).
A7 said not to assume B8-3's bump covers a B8-5 schema change; the discharge is that no
B8-5 schema change exists. `vlt-decay` **points** at the backlog `## Done` schema and the
safety model — it recites no convention mechanics — so it is **not** a `frontmatter.md`
consumer (the coherence check's own point-vs-recite test, `checks.md:36`) and joins no
`consumers:` list. Verification: Group E green with **zero handshake motion** in the diff.

**7. Drain eligibility — the scope cut that keeps every unbounded-window reader correct
without a convention edit.** A dispatch run block is **drain-eligible** iff ALL of:
(i) it is a `daily/…` or `relay` block — **`consult:` blocks are permanently
drain-exempt** (tiny by construction: one header + one pre-checked line; their evidentiary
window is unbounded — the consult-precondition check compares them against specs created
at any time — so retaining them is the derivability clause's "retained tail provably
contains the full derivation window" leg, costing bytes that round to nothing);
(ii) **every** pointer line in it is checked (`- [x]`) — an open row anywhere keeps the
whole block live; (iii) it is **not** the newest `daily/<source>` block for its capture
source (per principal stream) — that block carries the source's `routed through line N`
watermark, and removing it would reset the watermark to 0 and re-route the entire note as
duplicate open items; (iv) its run-header date is older than the drain age bar (45 days,
mirroring the wire so a drain always clears the wire it answers). Backlog: a drain moves
**all** `- [x]` items out of `## Done` (resolved is terminal; the section heading stays,
per the schema). `## Open` is never touched, byte-identical.

**8. Interim posture (R1) — two postures, both substantive.**
- **The upgrade window:** an existing vault upgrades into a registry whose `log-mass`
  wire may already be tripped (the primary field vault sits at ~259K ≥ 256K). That first
  trip is the **intended adoption bell**, not a defect: the legal response is the
  `surface_text`'s (invoke `vlt-decay`), or a deliberate local threshold raise —
  `tripwires.yaml`'s merge contract already rules LOCAL THRESHOLDS WIN, so a vault that
  prefers a fatter log edits its own wire and the seed never claws it back. No act runs
  automatically at upgrade time.
- **The newborn rule's window:** the decay table's "no accumulator without a declared
  contract" sentence ships as declared prose with **no mechanical check** (a lint case
  keying the table was already left "to a build that wants it" by cross-filing ruling 2's
  recorded text, and cross-filing ruling 4 keeps agent-zone mass out of lint's niche).
  Interim posture: factory-side, R4's required brief section + A13 are the net (every
  brief must disposition new file classes); vault-side, the table itself is the visible
  register a partner reads. Review with the first Arc-9 capture — if a no-contract
  accumulator ships past both nets, the mechanical check has earned itself.

## F-sites (all re-grounded against source at HEAD of `arc8-v0.11.0`, 2026-08-17 — four builds after capture)

### F1 — NEW skill `skills/vlt-decay/` (the two verbs)

**Current state:** does not exist. The verbs' would-be neighbors: `vlt-groom` owns partner
memory (tend, by pointer); `vlt-lint` owns the wiki lane (ruling 4 keeps this build out of
it); nothing owns agent-zone record mass.

**The change:** create `skills/vlt-decay/` — `SKILL.md` (router: overview, activation,
trigger model, standing rules, log line) + `references/rotate.md` + `references/drain.md`.
Mirror `vlt-groom`'s router shape (its SKILL.md is the freshest exemplar of the
activation/trigger/standing-rules form). Required content:

- **`SKILL.md`** — `name: vlt-decay`; **no `depends_on`** (disposition 6 — the skill
  points, never recites). `description` triggers: "rotate the log", "drain the dispatch
  board", "drain the backlog", "run vault decay/hygiene", plus the proactive clause naming
  the `log-mass`/`drain-due` wires (the `lint-debt` precedent in `vlt-lint`'s
  description). Overview names the two verbs and states tend's pointer: *partner memory
  is groomed, never drained — `vlt-groom` is that verb's single home.* **Trigger model —
  invoked-only**, citing `vlt-groom`'s Trigger model as the decide-once home (disposition
  3). **Safety model cited** (`{contract}`, *Hygiene and grooming — the safety model*),
  restated nowhere (the section's own instruction). Standing rules (act-blocking): never
  touch an open (`- [ ]`) row or any `consult:` block; never cross the newest `lint`
  header; never touch the newest `daily/<source>` block per source; never touch `## Open`;
  archives stay readable markdown, appended at the `{archive}`-mirrored path (contract
  `:65`); every run commits (append + archive move in one commit, the safety model's
  pairing); a verb with nothing eligible is a said-out-loud no-op, never an error. Log
  line: one partner-tagged `{log}` entry, **type `decay`** (legal: the contract's type set
  is declared non-exhaustive at `:130` — "name the op that owns one where it's defined";
  this SKILL.md is that naming site):
  `## [YYYY-MM-DD HH:MM] decay (<partner>) | rotate|drain: <what moved, in lines/bytes> → [[{archive}/...]]`
- **`references/rotate.md`** — `{log}` rotation: cut = every entry strictly before the
  newest `lint` header (found by the same grep lint Step 0 uses); **refuse loudly when no
  `lint` header exists** ("never linted — run `vlt-lint` first; rotation has no safe
  cut"): the whole file is then `ingests_since_lint`'s derivation window and any cut would
  corrupt it. Move the cut prefix by **appending** to `{archive}/_agent/log.md`
  (chronological order preserved; concatenation of archive + live tail reproduces the
  pre-rotation record byte-for-byte, minus the breadcrumb). Write/update the one-line
  breadcrumb (disposition 4). State the reader table (below) as the verb's own invariants.
- **`references/drain.md`** — dispatch drain per disposition 7's eligibility, moving
  whole blocks (header + rows travel together — never a row out from under its header) by
  appending to `{archive}/_agent/dispatch.md`; backlog drain moving `## Done`'s `[x]`
  items (with their `[resolved: <how>]` tails intact) to `{archive}/_agent/backlog.md`
  under a `## Done` heading; breadcrumbs in both live files. One invocation may run both
  drains; report what moved per file.

**The derive-first reader table (A10's mandate + the safety model's derivability clause —
each reader, its derivation, its rotation/drain-safety invariant; the builder ships these
as the verbs' own stated invariants and the fixture check in §7 proves them):**

| # | Reader (grounded) | Derives | Invariant that keeps it correct |
|---|---|---|---|
| R-1 | `vlt-vitals.py:334-353` — `ingests_since_lint` + `days_since_lint` | last `lint` header in `{log}`; `ingest` headers after it | Rotation cuts **strictly before the newest `lint` header**, so the live tail retains that header and every entry after it — both derivations are byte-for-byte unchanged. The refuse-when-never-linted rule covers the no-baseline case (a cut there would silently inflate the count into the "every ingest counts" fallback at `:348-349`). |
| R-2 | `vlt-vitals.py:354` — `log_bytes` | live `{log}` size | Drops on rotation **by design** (disposition 5: wake-read mass); archived sibling excluded — the definition string says so after F2. |
| R-3 | `vlt-lint/SKILL.md:26-29` — Step 0 scoped baseline (`grep "^## \[.*\] lint" {log} \| tail -1`; missing/malformed → announced **full-mode fallback**, the whale this arc exists to shrink) | newest `lint` header's timestamp | Same invariant as R-1: the newest `lint` header survives every rotation, so scoped mode's baseline is identical pre/post and no full-mode fallback is ever manufactured by hygiene. |
| R-4 | `vlt-vitals.py:358-381` — `open_pointers` + `oldest_open_pointer_days` | `- [ ]` rows under dated run headers in `_agent/dispatch.md` | Drain moves only **fully-closed** blocks (disposition 7 ii), whole (header + rows) — zero `[ ]` rows removed, no row orphaned from its date header; both counts identical. |
| R-5 | `vlt-dispatch/references/ledger.md:11-12` — the board's whole-record greps (total + per-slug `[ ] \`slug\``) | same rows as R-4 | Same invariant as R-4. |
| R-6 | `ledger.md:21-28` — pointer integrity + the two denominated legacy lanes | shape-annotated key failures; un-annotated-pathless and proto-`deliver` **counts** over the live record | Findings live only in open or terminal (checked-off-as-superseded) lines; a drained block is fully closed, so no *actionable* finding leaves the board. The legacy lanes are **counts, never findings** (`:26`): they are live-record denominators by definition, and a drain re-baselines them downward — F7 adds the one clause that says so, so B8-2's "reproducible by a second reader" property survives (both readers count the same live record). |
| R-7 | `vlt-dispatch/references/daily.md:11` — the per-source watermark baseline (`watermark[file]` from each source's **most recent** `daily/…` run header) | `routed through line N` | Disposition 7 (iii): the newest `daily/<source>` block per source (per principal stream) is **never drained**, even when fully closed and old — else the watermark resets to 0 and the next scoped run re-routes the whole note as duplicate open items. This is the single most load-bearing invariant in the build. |
| R-8 | `relay.md:39-49` — the idempotency grep on `(key, to-slug, principal)` | open / checked-latest / absent → no-op / re-notify / fresh | Blocks with an open pointer are ineligible (7 ii), so the no-op guard's evidence never drains. Draining a **checked** latest pointer changes the ladder's input from "checked → append fresh open pointer" to "absent → append fresh open pointer" — the **same behavior** (`:45,:47`). Stated as an invariant in `drain.md`; no code or prose change needed at `relay.md`. |
| R-9 | `checks.md:47` — `spec_candidate` (≥2 `relay:` entries at one path; declines recorded in `{backlog}` excluded) | relay-count over the record + decline read over the backlog | Both windows are unbounded, and drains genuinely shrink them → **the consumer widens to read the archive, this build** (the derivability clause's second leg): F5 amends the paragraph so the relay count and the honored-declines read each cover the record **"and its `{archive}`-mirrored sibling"**. |
| R-10 | `checks.md:48` + `{conventions}/consult.md:47,:57` — the consult-precondition check and its rule home | a `consult:` block naming the `(spec-path, consumer-slug)` pair, any age | Consult blocks are **permanently drain-exempt** (disposition 7 i) — the retained record provably contains the full derivation window forever; no check widening, **no `consult.md` edit, no bump**. The first-`consult:` adoption stamp (`vlt-dispatch/references/consult.md:77`) is additionally guarded by its own key semantics ("if the key already carries a date, leave it"), so even that grep cannot double-stamp. |
| R-11 | `vlt-upgrade/SKILL.md:80` — the proto-spec retrofit's relay-count (same derivation as R-9) — **grounding addition**: the roadmap's reader list predates this sweep finding it | relay entries per path | Widens exactly as R-9, same build (F6). |
| R-12 | Partner Beat-2 open-slice greps — `vlt-mint/assets/partner-agent-template.md:40` + the three shipped partners (`vlt-agent-{librarian,researcher,creative}/SKILL.md:25`) | each partner's open `[ ]` slug rows | Subsumed by R-4's invariant (only closed blocks drain). No edit. |
| R-13 | `vlt-vitals.py:444-446` — `backlog_bytes`; contract `:268` partner activation read; `frontmatter.md:245` mint's capability-gap filter | live backlog size; `## Open` items | `## Open` is byte-identical under any drain (disposition 7); `backlog_bytes` drops by design (R-2's reasoning). |

**Why:** the verbs are the filing's core ask; the table is what makes them shippable under
the safety model's derivability clause instead of a fresh R3-fault factory.

**Out of scope at this site:** no `sessions/`, `lint_reports/`, `daily/`, wiki-lane, or
partner-file verb (the table in F4 dispositions each); no scheduled execution (D2).

### F2 — `skills/vlt-setup/assets/hooks/vlt-vitals.py` (the age metric + the live-only clauses; the B8-4 comment verified)

**Current state:** METRICS at `:194-220`; size-vital ids at `:213-219`
(`partner_memory_bytes` already sums `reflexes.md` — B8-3's R4 widening landed;
**grounding correction**: the capture's `:213-218`/`:453` cites are one line and the
enumeration off after B8-3/B8-4 — current derivation loop at `:449-461`). The dispatch
derivation parses run headers + `- [ ]` at `:358-381`. **Pre-ideation ruling 1 / A12 / A9
verification duty DISCHARGED at re-ground:** the disposition-8 comment at `:441-443` now
reads *"Disposition 8's 'no rollover machinery' deferral was discharged by field evidence
(filing 2026-08-16, Arc 8); decay machinery ships separately — these vitals stay
display-only"* — self-contained (date + evidence, no factory path), exactly as B8-4's
carrier brief promised. **Present; this build re-verifies by grep and does not edit it**
(acceptance check 4).

**The change:**
1. Add METRICS id **`oldest_drainable_section_days`**: *"days since the run-header date
   of the oldest drain-eligible `_agent/dispatch.md` run block — fully closed `daily/`/
   `relay` block that is not its source's newest watermark carrier; `consult:` blocks
   exempt; 0 when none (display + wire)"*. Derivation beside the existing dispatch block
   (`:358-381`): split the record on `^## \[` headers; a block is closed iff it contains
   ≥1 pointer line and no `- [ ]`; classify block kind from the header (`daily/` prefix /
   `relay` / `consult:`); track the newest `daily/<source>` header per source and exclude
   it; the metric is the max `_days_since` over eligible headers, else 0. Stdlib-only,
   derive-only, tolerant of history — the file's own standing rules.
2. Amend two definition strings per disposition 5: `log_bytes` → *"byte size of the live
   `{log}` (display-only size vital + the `log-mass` wire; archived segments under
   `{archive}` excluded — vitals measure wake-read mass)"*; `backlog_bytes` gains the same
   live-only clause. `index_bytes`/`partner_memory_bytes` definitions unchanged (ruling
   recorded in this brief covers them; their derivations already read live paths only).

**Why:** the age facet is the unbuilt half of disposition (d) (roadmap Sharpening 1); the
metric id is what lets `drain-due` obey A11's one-canonical-id-per-wire rule; defining
eligibility identically to the drain verb guarantees a drain always clears the wire it
answers (no unclearable trip → no fatigue).

**Out of scope at this site:** no `dispatch_bytes` size vital (the age wire covers the
dispatch board's decay; adding a fifth size vital is a new display row nobody asked for);
`WIRE_REQUIRED_FIELDS` (`:222`) untouched (A4's ruling stands — wires take no new field).

### F3 — `skills/vlt-setup/assets/tripwires.yaml` (the two wires; the count wording)

**Current state:** two stock wires (`lint-debt` `:45-51`, `relay-overdue` `:53-59`);
B8-1's `surface_text` legal-response semantics in the header at `:21-23`; the count/bar
sentence at `:41-42`: *"The two stock wires (the filing's own pair — the alert-fatigue
budget is a hard constraint; add a third only when a real failure earns it):"*. Merge
contract at `:36-39` (merge-by-id; LOCAL THRESHOLDS WIN; local wires never dropped).

**The change:** append the `log-mass` and `drain-due` wires exactly as specified in
disposition 2 (all seven required fields each). Rewrite the count sentence per A11 — the
**bar clause survives verbatim, the ordinal updates**: *"The four stock wires (the
original pair plus the decay-contract pair, Arc 8 — the alert-fatigue budget is a hard
constraint; add a further wire only when a real failure earns it):"*. Nothing else in the
header moves; `WIRE_REQUIRED_FIELDS` unchanged, so an existing vault's registry merges
clean — the two new wires arrive by id, local wires and thresholds untouched.

**Why:** pre-ideation ruling 2 (the owner ruled A8-1 the earned failure; A11 admitted the
class and put count/thresholds here); B7-8's stale-prose lesson is why the ordinal updates
in the same diff as the wires.

### F4 — `vault-operating-contract.md` (the Decay contracts table + per-surface prose reconciliation)

**Current state:** hygiene-safety section at `:270-277` (B8-3); structure table rows —
`log` `:36` ("Append-only chronological operation record"), `backlog` `:37`, `overlays`
`:41`, `upgrade_ledger` `:44`, `archive` `:45`, `lint_reports` `:47`; archive mirroring
rule `:65`; `{log}` prose `:122` ("append-only record of every operation"); log grep
examples `:144-148`.

**The change:**
1. **New subsection immediately after `:277`** — **"Decay contracts — retention declared
   at birth"**: a table, one row per operational file class: *class / decay verb /
   trigger / destination / watermark*. Rows (each verb-covered or exempt-with-reason —
   the newborn sweep's shipped form):
   - `{log}` — **rotate** (`vlt-decay`) / `log-mass` wire / `{archive}/_agent/log.md` /
     breadcrumb line.
   - `_agent/dispatch.md` — **drain** (`vlt-decay`) / `drain-due` wire /
     `{archive}/_agent/dispatch.md` / breadcrumb; consult blocks and each source's newest
     watermark block permanently retained (the eligibility rule lives in `vlt-decay`,
     pointed at, not restated).
   - `{backlog}` — **drain** of `## Done` (`vlt-decay`) / rides the drain invocation /
     `{archive}/_agent/backlog.md` / breadcrumb; `## Open` never touched.
   - Partner memory (`identity.md`/`thread.md`/`reflexes.md`) — **groom** → `vlt-groom`
     (A10's pointer; the ladder + gate live there). `reflexes.md` additionally carries its
     decay contract at birth in its own schema (`frontmatter.md:218`).
   - Wiki + research — the wiki lane's own machinery (consolidation, supersession,
     graduation, `{archive}` retirement) — pointed at, exempt here.
   - `{sessions}` — exempt: naturally segmented per sitting (the foldering pattern the
     rotate verb mirrors); never whole-dir wake-read; ad-hoc retirement to `{archive}`
     remains available.
   - `{lint_reports}` — exempt: dated per-run files, never wake-read (disk-side, not
     wake-side mass); **retention remains the human's** (`vlt-lint` Step 6 — deliberately
     reaffirmed, F5).
   - `{upgrade_ledger}`, `{overlays}`, `{tripwires}` — exempt: slow, human-gated
     accumulators (one entry per upgrade / append-only local rules / rare wire edits);
     append-only declarations stand.
   - `{archive}` itself — exempt by definition: cold storage, outside every live-read
     enumeration (cross-filing ruling 2/A2), git-tracked, readable markdown.

   Close the subsection with A13 shipped: *"A new accumulating agent-zone file class
   enters this table in the act that creates it — no accumulator ships without a declared
   decay contract."*
2. **Structure-table row `:36`** — UPDATED: *"Append-only chronological operation record
   (live tail — rotates under *Decay contracts*)".* Append-only at-write stays asserted;
   the row stops implying the file is the whole of history.
3. **`:122`** — UPDATED with one clause: *"…the single place to answer 'what happened and
   when' (the live tail; rotated history sits at its `{archive}` mirror — *Decay
   contracts*)"*.
4. **Rows `:37`/`:41`/`:44`/`:47` — deliberately REAFFIRMED, unchanged**: their
   append-only/living declarations stay true; the decay table (not the row prose) now
   carries each class's exit or exemption. Recorded here so the per-surface
   reconciliation is a decision, not an omission.

**Why:** disposition 1 (retention-at-birth's home), the roadmap's prose-reconciliation
mandate ("every shipped sentence the verbs falsify — updated or deliberately reaffirmed,
per surface"), A13.

**Out of scope at this site:** no edit to the `<type>` list at `:130` (declared
non-exhaustive; `vlt-decay`'s SKILL.md is the naming site); no edit to the grep examples
at `:144-148` (they read the live record, which is exactly what they should read).

### F5 — `vlt-lint` (the reaffirmation + the R-9 widening)

**Current state:** `SKILL.md:72` — *"append-only — never edit, prune, or
re-read-to-rewrite past reports; retention is the human's"*. `references/checks.md:47` —
`spec_candidate` counts `relay:` entries in `_agent/dispatch.md` per path and excludes
candidates with a recorded decline in `{backlog}`.

**The change:**
1. `SKILL.md:72` — **deliberately reaffirmed with its reason attached** (one clause, so
   the sentence survives the arc as a citation instead of an orphan): *"…retention is the
   human's (lint reports are never wake-read — the operating contract's *Decay contracts*
   table records the exemption)"*.
2. `checks.md:47` — the R-9 widening (two touches in the one paragraph): the relay-entry
   count reads `_agent/dispatch.md` *"and its `{archive}`-mirrored sibling (drained relay
   history counts — a drain must not silently reset a candidacy signal)"*; the recorded-
   decline read covers `{backlog}` *"and its `{archive}`-mirrored sibling"* the same way.
   `checks.md:48` (consult preconditions) is **untouched** — R-10's drain-exemption keeps
   its record intact by construction.

**Why:** the derivability clause (contract `:277`) — widen the consumer in the same build
as the drain; the reconciliation mandate for `:72`.

**Boundary note (ruling 4/A14 honored):** these are read-scope amendments to two existing
governance checks, not new finding classes and not a lint-boundary move — mass/age
machinery stays in `vlt-decay`; no partner-file check is touched. **R3:** no finding
class's legal response changes.

### F6 — `vlt-upgrade/SKILL.md:80` (the retrofit's count — grounding addition)

**Current state:** the proto-spec retrofit counts *"relay entries in `_agent/dispatch.md`
pointing at the same path"* — the same derivation as R-9, found by this brief's reader
sweep (the roadmap's A10 list predates it).

**The change:** the same widening clause as F5.2 — the count covers the record and its
`{archive}`-mirrored sibling. One clause; the retrofit's human-gated offer semantics are
untouched.

### F7 — `vlt-dispatch` prose (reaffirm + the denominator clause)

**Current state:** `references/daily.md:63` — *"`_agent/dispatch.md` is a log-style agent
record (like `{log}`), not a 'note' — it carries no per-note frontmatter."*
`references/ledger.md:26-28` — the two legacy lanes as live-record counts.

**The change:**
1. `daily.md:63` — **reaffirmed, with the breadcrumb admitted**: append *"(a `vlt-decay`
   drain leaves at most a one-line breadcrumb beneath the title — still no frontmatter)"*.
2. `ledger.md:26` (the legacy-lanes paragraph) — one clause making R-6's re-baselining
   explicit: *"Counts are **live-record** counts: a `vlt-decay` drain moves closed legacy
   blocks to the archive and the denominator re-baselines — reproducibility means two
   readers of the same live record agree, not that the number never moves."*

**Why:** the reconciliation mandate; keeps B8-2's shipped reproducibility acceptance
meaningful across the first field drain.

**Out of scope at this site:** the seeded dispatch file header (`daily.md:58-60`) does not
name the drain — it enumerates the four modes of `vlt-dispatch`, and adding a
foreign-skill mention would start a completeness-claiming list (the standing drift rule);
the decay table + `vlt-decay`'s description carry discoverability.

### F8 — Registration surfaces (`vlt-decay`)

**Current state:** marketplace `skills[]` and README carry 15 skills (B8-4 added
`vlt-groom`); `module-help.csv` canonical 13-col header.

**The change:** add `vlt-decay` to `.claude-plugin/marketplace.json` `skills[]`; one
`module-help.csv` row (13 cols, `preceded-by,followed-by`, **every free-text field
quoted**); README skill count 15 → 16 in **both** count sites. Covered mechanically by
`package-lint` C5 + the csv checks.

## Registration

`vlt-decay` (F8): marketplace `skills[]` entry, quoted 13-col `module-help.csv` row,
README count 15 → 16 (both sites). **No convention version moved and no `consumers:` list
changed** (disposition 6), so there is no consumer walk and no re-ack — Group E must show
zero handshake motion.

## Out of scope (dispositioned)

- **Tend / any partner-memory mechanism** — A10: pointer to `vlt-groom`, period.
- **Partner-file lint finding classes** (staleness, duplication-with-wiki,
  rule-as-narrative) — cross-filing ruling 4: disposition (f)'s territory, not this
  build's; neither brief may re-cut that boundary.
- **Scheduled/background execution** — declined per D2 (disposition 3).
- **In-place LLM rewriting, binary compression, a hygiene ledger** — the filing's
  non-goals, traveling verbatim (Intent).
- **A `dispatch_bytes` size vital** — rejected (F2 out-of-scope note).
- **`sessions/`, `lint_reports/`, `daily/`, wiki-lane, `{upgrade_ledger}`, `{overlays}`,
  `{tripwires}`, `{archive}` verbs** — each exempted with its reason in the decay table
  (F4.1); `daily/` is additionally a human zone the module never writes.
- **A mechanical no-contract-accumulator check** — deferred with a named review
  (disposition 8, R1 second posture).
- **`compacted-through:`/`archive:` frontmatter writes by the new verbs** — not written
  (disposition 4); the fields remain the watermark form for frontmatter-bearing files.
- **Retroactive history rewriting of any record** — the verbs move content whole and
  unedited; nothing is reworded in flight (safety model, first bullet).
- **The dispatch seeded-header mode list** — untouched (F7 out-of-scope note).

## Verification (unit, at rest)

1. **Fixture rotate** (temp vault fixture: a `{log}` with pre-lint history, a `lint`
   header, `ingest` headers after it): run `vlt-vitals.py` and lint's Step-0 baseline grep
   before and after performing `references/rotate.md` against the fixture —
   `ingests_since_lint`, `days_since_lint`, and the scoped-baseline timestamp are
   **identical**; `log_bytes` drops; `{archive}/_agent/log.md` exists at the mirrored
   path and archive + live tail concatenate to the pre-rotation record (breadcrumb
   aside); a second rotate is a stated no-op, files byte-identical. Also: a fixture with
   **no** `lint` header → rotate refuses loudly, nothing moves.
2. **Fixture drain** (fixture dispatch: open + fully-closed `daily/` blocks across two
   sources including an old fully-closed newest-block, `relay` blocks open/closed, a
   `consult:` block; fixture backlog with `## Open` + `## Done`): pre/post —
   `open_pointers`, `oldest_open_pointer_days`, the board's total and per-slug greps
   **identical**; the newest `daily/` block per source and the `consult:` block retained;
   `oldest_drainable_section_days` drops below 45; `## Open` byte-identical; drained
   relay/consult-window reads per F5.2/F6 derive the same counts across live+archive as
   the pre-drain live record did; second drain no-ops.
3. **Wires**: full `vlt-vitals.py` run against the fixture renders 4 wires, the new
   metric row, and correct trip states either side of each threshold; `parse_wires`
   reports zero missing-field errors; a fixture vault carrying the old 2-wire registry
   merged per `vlt-setup`'s merge-by-id gains exactly the two new wires with local
   thresholds intact.
4. **Cross-file agreement greps**: `"two stock wires"` → zero hits in `skills/`; the bar
   sentence ("alert-fatigue budget is a hard constraint") still present verbatim;
   `oldest_drainable_section_days` present in METRICS, `tripwires.yaml`, and nowhere
   re-defined; the `:441-443` discharge comment present and unedited (`git diff` clean on
   those lines); the decay table names every structure-table row's class (walk the table
   at `:30-47` against it — the walk is the completeness check, not a memorized list);
   `frontmatter.md` diff **empty** and `consult.md` diff **empty** (disposition 6).
5. **Handshake bipartite re-check** — `package-lint` **Group E** (the check of record —
   never a hand-written grep): green, with no version motion and no consumers change
   expected.
6. **Packaging lint** — `package-lint.py` A/B/C/E green with `vlt-decay` registered (C5
   both directions, quoted csv row, README 16 in both count sites).
7. **Fixture extension (R2): not applicable** — no release-gate check is added or
   changed (Group E4's floor untouched).
8. **Legal response (R3):** no new or changed lint/dispatch finding class; the two wires
   carry their responses in `surface_text` per B8-1's ruled exception. Stated; nothing
   further owed.
9. **Enumeration widening (R4):** `vlt-decay` joins every surface that enumerates skills
   (marketplace `skills[]`, README counts, help csv — F8). The archived record files this
   build creates are **declared outside** live-read enumerations (cross-filing ruling
   2/A2's declared-exclusion clause — cold storage; vitals measure wake-read mass), the
   reasoning recorded in disposition 5. No vital enumeration widens.
10. **Scrub** — every changed shipped file carries no personal or vault-local content;
    all example paths placeholder-form (`{archive}/_agent/log.md` style).

## Release (this is the arc's release build)

v0.11.0 rides this build (five of five, per the ruled ship order): bump **both** version
strings (`.claude-plugin/marketplace.json` `"version"` and
`skills/vlt-setup/assets/module.yaml` `module_version`) to `0.11.0`; run
`uv run tools/package-lint.py --expect-version 0.11.0` and tag only on exit 0, recording
the PASS summary line in the release commit message; then the `vlt-release` choreography
(ff-merge `arc8-v0.11.0` → `main`, tag `v0.11.0`, push main + tag). The release commit
is this build's commit.

## Acceptance (live — the same checks appended to the roadmap ledger)

1. **[ship-verifiable]** Fixture rotate holds every `{log}` reader: `ingests_since_lint`,
   `days_since_lint`, and lint Step-0's scoped baseline identical pre/post; archive +
   live tail reproduce the pre-rotation record; never-linted fixture → loud refusal;
   second rotate no-ops (Verification 1).
2. **[ship-verifiable]** Fixture drain holds every dispatch/backlog reader: open-pointer
   counts, per-slug greps, and `oldest_open_pointer_days` identical; each source's newest
   `daily/` watermark block and every `consult:` block retained; `## Open` byte-identical;
   the widened `spec_candidate`/retrofit reads (live + archive) derive the pre-drain
   counts; `oldest_drainable_section_days` clears its wire; second drain no-ops
   (Verification 2).
3. **[ship-verifiable]** The registry ships 4 wires, each keying exactly one canonical
   metric id with mass (`log_bytes`) and age (`oldest_drainable_section_days`) on
   separate wires; the header's bar sentence intact verbatim with the count wording
   updated ("two stock wires" greps to zero across `skills/`); `WIRE_REQUIRED_FIELDS`
   unchanged; an existing 2-wire vault registry merges to exactly 4 with local
   thresholds winning.
4. **[ship-verifiable]** The contract carries the Decay contracts table covering every
   structure-table file class and every B8-1..B8-4 newborn (verb-covered or
   exempt-with-reason; `reflexes.md` cited to its at-birth contract, partner memory
   pointed at `vlt-groom`), plus the A13 sentence; every reconciliation surface shows its
   ruled state (contract `:36`/`:122` updated; `vlt-lint/SKILL.md:72` and `daily.md:63`
   reaffirmed-with-clause; `ledger.md` live-record clause present); `vlt-vitals.py`'s
   disposition-8 discharge comment verified present and unedited; `frontmatter.md` and
   `consult.md` diffs empty — no version bump anywhere (A7), `package-lint` Group E
   green with zero handshake motion.
5. **[ship-verifiable]** Release gate: `package-lint` A/B/C/E green with `vlt-decay`
   registered (C5, quoted csv row, README 16 both sites) and `--expect-version 0.11.0`
   exit 0, PASS line in the release commit.
6. **[field-contingent — vlt-core]** The adoption bell rings as designed: first
   post-upgrade wake trips `log-mass` (the vault sits past the threshold at filing); the
   maintainer invokes the rotation (or deliberately raises the local threshold — either
   is the legal response); after a performed rotation the strip goes green, the next
   scoped lint still runs **scoped** (no full-mode fallback), and `lint-debt`'s count
   matches its pre-rotation derivation.
7. **[field-contingent — vlt-core]** First live drain of the real dispatch record: board
   counts identical pre/post, every capture source's next scoped `daily` run routes only
   genuinely-new lines (no watermark reset, no duplicate items), and the ledger's legacy
   denominators re-render as live-record counts per the shipped clause with the drained
   blocks reachable at the archive mirror.
