---
title: 'Build #B10-6 — the report contract (structured reports persist verbatim as dated plain-.yaml files under walker-exempt report dirs: the upgrade post-flight report gains a durable home, schema-derived emission makes mandatory report lines unskippable, and the unfillable high_value_gaps slot reports unmeasured honestly)'
status: 'BUILT 2026-08-22 — all six F-sites landed on branch arc10-v0.14.0, no deviations.
  E2/E1 re-verified at build time: vlt-upgrade had zero persist instructions pre-edit,
  the lint-debt counter derives from the {log} Step-6 entry (vlt-lint/SKILL.md:72), and
  vlt-lint-full.js is byte-untouched (absent from git diff --stat). Verification: greps
  (1)-(6) all PASS — -lint.yaml at vlt-lint/SKILL.md:72 with no shipped .md lint-report
  write remaining; upgrade-reports in exactly the F-site set (vlt-upgrade SKILL :120/:143,
  contract :48/:316, vlt-setup SKILL :195/:343, full-scale.md:7), each a row or pointer;
  coexistence clauses at F2 and the F4 rule sentence; high_value_gaps renders the literal
  unmeasured at report.md:61 and the identifier has no producer site tree-wide; A3 re-check
  clean (only negated-read/exempt-row/provisioning hits); ledger Report: line present and
  the every-line-required completeness sentence covers it. A10-14 desk-check red-then-green:
  the hand-saved 0.13.0 block FAILS the schema-key verify with missing =
  [manifest_write_divergence], extra = []; a schema-complete synthetic block PASSES.
  Persist dry-run against a scratch fixture vault: schema walked top-to-bottom (17 keys),
  dated plain .yaml written with lazy dir creation, parsed back whole, key set matches the
  schema in order. C6: rule card re-derived (contract changes added nothing identity-bearing
  or act-blocking; section map already points at Path resolution + Hygiene/Decay contracts),
  derived_from sha256 re-stamped bd06909a…, last_updated 2026-08-22, budget re-checked.
  package-lint: A/B/C/E PASS, D SKIPPED (not a release build). Handshake: no version:
  moved, no consumers: changed, Group E PASS unchanged. No .decision-log.md in the tree.'
module_code: 'vlt'
created: '2026-08-22'
derives_from:
  - 'inbox/2026-08-21-124500-upgrade-reports-need-a-durable-vault-home.md (A10-4 — the upgrade''s full Step-4 post-flight report persists nowhere while lint''s equivalent persists verbatim; the report is acceptance evidence, carries owner rulings, and the lost-ephemeral-report class already cost ruling 4c a three-arc slip)'
  - 'inbox/2026-08-21-124800-report-yaml-in-markdown-legibility.md (A10-5 — the persisted report shape: YAML fenced inside a .md wrapper that carries essentially nothing else; the format question ruled jointly with A10-4 at Q3)'
  - 'inbox/2026-08-21-150213-high-value-gaps-declared-field-has-no-producer.md (A10-11 — report.md declares high_value_gaps for full mode but no producer exists anywhere; the slot can only misread as "no gaps" or "measured, none found"; owner-ruled into B10-6 2026-08-22)'
  - 'inbox/2026-08-21-164445-step4-report-omits-manifest-write-divergence-line.md (A10-14 — the 0.13.0 Step-4 report omitted the mandatory manifest_write_divergence: line; emitter-honesty defect, B10-1 check (5) FAILED on it; owner-ruled into B10-6 2026-08-22)'
roadmap: 'skills/reports/inbox-evolution-arc10-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-21): build-B10-6 grouping bullet (binds: Q3a, Q3b, E1, E2); Q3a (general rule + census — report-emitting verbs persist their report verbatim to a dated file under a config path, symmetric with lint; retention row declared same build per Arc 8 retention-at-birth); Q3b (plain .yaml under the report dirs with a declared lint-walker exclusion; the acceptance-instrument variant presented, NOT adopted — left to this brief); roundtable A12 (the walker exclusion is declared by extending the existing operating-contract Decay-contracts + zone-map rows — new report paths get rows in the same tables, never a new list; this brief states the legacy-.md coexistence posture: existing files stay legal, no backfill sweep); roundtable A1 (owner-ruled interim evidence posture: the owner hand-saved the 0.13.0 Step-4 report to a dated file — B10-6 retires the posture and its E2 census names that file as a migration input); roundtable A7 (no vault_structure key is minted this arc — C6-b''s merge-config strip makes key-minting unsafe until that debt clears; the qualifying-key predicate is single-homed in full-scale.md and B10-6''s exclusion edits that home); E1 (consumer census of the current .md shape, re-derived against live source at brief time, walked before the .yaml cut, incl. verifying the lint-debt counter derives from the session log); E2 (verb census — which verbs report-and-discard vs report-and-persist — is the build''s first act, and the rule applies everywhere it hits); capture addendum 2026-08-22 (owner-ruled: A10-11 → B10-6, the brief rules produce/retire/unmeasured; A10-14 → B10-6, the unskippable-mandatory-lines clause lands alongside the persist/format rulings; no joint moved).'
risk: 'low-moderate — no convention version: moves anywhere (no handshake bump, no consumer walk), but the operating contract gains two table rows + one rule sentence, so package-lint C6 fires: the rule card is re-derived and its derived_from sha256 re-stamped in the same build. Multi-skill prose edits (vlt-lint, vlt-upgrade, vlt-setup) + one report-schema value-contract change (high_value_gaps renders unmeasured — additive honesty, slot name/position stable per the B10-2 precedent). No workflow edit (vlt-lint-full.js untouched — no ask or read-list change, R4-fanout not triggered), no new package-lint check (E4 untouched), no new skill (no registration), not a release build (the version bump rides the release build of its cut).'
---

# Build #B10-6 — the report contract

Arc 10's through-line names this pair "evidence that evaporates": the upgrade's full
Step-4 post-flight report — acceptance evidence by Arc 9's own rules, carrier of owner
rulings — persists nowhere (`vlt-upgrade/SKILL.md` has no persist instruction; only the
digest ledger survives, `SKILL.md:120-143`), while lint's equivalent persists verbatim
(`vlt-lint/SKILL.md:72`). The v0.13.0 discharge ran on a hand-carried transcript the
owner saved by hand (`skills/reports/2026-08-21-vlt-core-upgrade-0.13.0-step4-report.md`
— the A1 interim posture, the last transcript-regime run) — and that very specimen
carries the arc's other emitter-honesty defect: it omits the mandatory
`manifest_write_divergence:` line (A10-14, B10-1 check (5) FAILED). One layer down, the
same misread class: `report.md:61` declares `high_value_gaps` with no producer anywhere
in the tree (A10-11), so the slot can only lie by omission.

This build lands Q3's ruled contract whole: the **E2 verb census first**, the **E1
consumer walk** (done at brief time, §E1 below — the build re-verifies it), then the
**general persist rule** — structured report-emitting verbs persist their report verbatim
as a dated plain-`.yaml` file under a walker-exempt report dir, retention rows declared
in the same act — applied everywhere the census hits: `vlt-upgrade` gains its durable
report home, `vlt-lint`'s persist switches shape, mandatory lines become structurally
unskippable, and the unfillable slot becomes honest.

All rejected alternatives in the parent filings and the rulings are settled — do not
re-litigate. In particular: the `.md`-wrapper status quo and every priced middle shape
(minimal-frontmatter+one-fence, `.yaml` sidecar + `.md` pointer) — Q3b ruled plain
`.yaml`; a new walker-exclusion list — A12 ruled extend-the-existing-tables, never a new
list; any backfill sweep of legacy `.md` reports — A12's coexistence posture; reading
prior reports for any derivation — A3's records-never-reports rule stands (B10-3 shipped
it; reports stay walker-exempt, which is Q3b's own premise).

**`binds:` roster (from the roadmap bullet, per the standing rule): Q3a, Q3b, E1, E2 —
plus the capture addendum's two owner rulings (A10-11 in, A10-14 in) and roundtable
A1/A7/A12 as amended above.** The bullet carries the roster explicitly; the addendum
rulings are dated 2026-08-22; nothing was reconstructed.

**Naming note (two R4s):** the roundtable's **R4** is the *fan-out currency rule*; the
brief-anatomy's standing **R4** is the *enumeration-widening rule* (§Verification). This
build touches no `vlt-lint-full.js` ask or convention read list, so R4-fanout's audit
re-run is not triggered; where this brief says R4 unqualified it means the anatomy's rule.

## E2 — the verb census (grounded at brief time; the build's first act re-verifies it)

Q3a/E2: which verbs report-and-discard vs report-and-persist. Grounded against HEAD
(`a3ec505`, tree clean):

| Verb | Report surface | Verdict | Rule hits? |
| --- | --- | --- | --- |
| `vlt-lint` | Step-5 structured report ("structured and parseable", `SKILL.md:11`; schema `references/report.md`) | **persists** verbatim (`SKILL.md:72`) — as fenced-YAML-in-`.md` today | **Yes** — shape cut to `.yaml` (F2) |
| `vlt-upgrade` | Step-4 post-flight report ("parseable summary", `SKILL.md:89-112`) | **discards** — only the Step-5 ledger digest persists (`SKILL.md:120-143`); grep confirms zero persist instructions for the report | **Yes** — gains the persist (F1) |
| `vlt-setup` | end-of-run provisioning report (`SKILL.md:342`) | prose bullet summary, not a structured block; its durable halves already live on disk (the manifest, `config.yaml`, seeded files) | No — census-recorded report-and-discard (disposition 5) |
| `vlt-decay` | "report what moved per file" (`SKILL.md:13`, `references/rotate.md:29`, `drain.md:3`) | prose; the durable record is the `{log}` `decay` line + archive watermarks | No — census-recorded |
| `vlt-groom` | no report surface (zero report/summary mentions in `SKILL.md`) | acts record per the groom's own watermarks | No — census-recorded |
| other verbs (`vlt-mint`, `vlt-dispatch`, `vlt-feedback`, `vlt-ingest`, `vlt-extract`, `vlt-research`, `vlt-track`, …) | no structured report block (the `yaml` fences in ingest/extract/research/track are note-frontmatter templates, not reports) | their durable records are their own artifacts (decision log, dispatch record, tracker issues, notes) | No — census-recorded |

Census entries per roundtable A6, already accounted: B10-1's `absorbed:`/diverged output
rides the Step-4 report (`vlt-upgrade/SKILL.md:106` — shipped) and so is covered by F1's
persist; B10-4's metric home is a declarative registry (`tripwires.yaml`), not a report —
its brief recorded its Q3 disposition, nothing owed here.

**The migration input (A1):** exactly one report predates the rule — the hand-saved
0.13.0 Step-4 report at
`skills/reports/2026-08-21-vlt-core-upgrade-0.13.0-step4-report.md` (factory-side,
verbatim per its provenance header). The census records it as the one pre-rule specimen:
it **stays where it is, unconverted** (the legacy-coexistence posture's factory-side
analog), remains the evidence of record for the still-open v0.13.0 discharge tails
(B10-4 (4)'s "A1 hand-saved Step-4 report" clause), and serves as this build's red
fixture for the A10-14 verify step (disposition 3). No vault-side backfill exists to do —
the report was never persisted vault-side.

## E1 — the consumer walk (re-derived against live source at brief time, per the A6 rewording)

Every consumer of the current `.md` report shape / `{lint_reports}`, walked before the
`.yaml` cut:

1. `vlt-lint/SKILL.md:72` — the **writer** ("write the Step-5 report block verbatim to
   `{lint_reports}/YYYY-MM-DD-HHMM-lint.md`"; append-only, never re-read). Edited (F2).
2. `vlt-lint/references/report.md:3` — the shape's framing ("fenced report block is
   strict YAML as a whole"). Edited (F3).
3. `vlt-lint/references/full-scale.md:7` — excludes report dirs from the
   `crossLayerSlugs` qualifying-key predicate by **key name** (`lint_reports`), never by
   file read. Extension-agnostic; edited only to widen the exclusion (F6, per A7).
4. `vlt-lint/references/checks.md:47` — states `{lint_reports}` **is not read** (B10-3's
   A3 clause). A negative consumer; unaffected, verified surviving.
5. `vlt-setup/SKILL.md:194` — creates the dir ("persists its dated Step-5 report blocks
   there"). Edited (F5).
6. Operating contract `:47` (zone-map row) + `:314` (Decay-contracts exempt row) — path
   docs; "dated per-run files" is extension-agnostic; rows extended per A12 (F4).
7. `module.yaml:61`, `vlt-vitals.py:153`, `package-lint.py:412` / C8(d),
   `test-package-lint.py:54`, `test-cost-manifest.py:66` — **key-name/path consumers
   only**; none reads report file contents or extensions. Unaffected.
8. **Factory-side acceptance readers** (added by B10-2..B10-4): the arc ledger's open
   tails B10-2 (5), B10-3 (3), B10-4 (4) name "the persisted `{lint_reports}` file" as
   evidence — worded extension-agnostically; a discharge over a post-B10-6 run reads
   `.yaml`, over a pre-B10-6 run reads `.md`; both remain legal evidence (coexistence).
   The hand-saved Step-4 file (B10-1 (5) / B10-4 (4) evidence) is §E2's migration input.
9. **The `lint-debt` counter — verified as E1 demands:** it derives from the `{log}`
   Step-6 entry, *not* from reports — `vlt-lint/SKILL.md:72`: "This entry is, **by
   derivation, the `lint-debt` counter reset** — no bookkeeping step exists anywhere."
   The cut cannot touch it.

**Walk verdict: no consumer anywhere parses the `.md` wrapper or depends on the fenced
form. The cut is safe.** (B10-3 is out of this census by construction — roundtable A3.)

## Brief-time dispositions

All numbered dispositions below are clerk-resolved (autonomous run 2026-08-22, owner
review pending) except where they merely apply a ruling verbatim.

1. **The acceptance-instrument question — ADOPTED.** ✅ **OWNER-RULED 2026-08-23 —
   ADOPTION CONFIRMED** (incl. the transport caveat: for the work-machine vault the
   factory cannot read, the owner hand-carries the persisted file itself, never a
   transcript). The A1 hand-save posture is retired as of this build's release.
   *(The question Q3 presented and
   deliberately did not adopt, left to this brief by the Round-6 brief-time list;
   clerk-resolved.)* Factory discharge reads the **persisted report file** as the
   evidence of record — never a hand-carried transcript. Reasoning: retiring the A1
   posture is this build's named obligation, and the persisted file is exactly the
   instrument the posture was standing in for — verbatim, dated, durable, and (post-F1)
   structurally complete, where a transcript is none of those; the factory already reads
   vlt-core directly for acceptance evidence (B10-5 (5)/(6)'s "read directly from
   vlt-core" precedent), so no new access posture is created. Transport caveat, stated
   at brief time per §9's vault-naming rule: for a vault the factory machine cannot read
   (the work-machine install), the owner hand-carries the **persisted file itself**, not
   a transcript — the file is the instrument either way. Scope note: this ruling changes
   factory discharge procedure and this brief's own acceptance wording; it edits no
   shipped text beyond F1's persist (which creates the instrument).
2. **A10-11 resolves to option 3 — make "unmeasured" expressible; no producer is built,
   the slot is not retired.** ✅ **OWNER-RULED 2026-08-23 — CONFIRMED** (with disposition
   3): the slot renders the literal `unmeasured`, never `[]`, never omitted; producer and
   retirement both declined; the workflow stays out of the fan-out. *(The addendum ruling routed the produce/retire/unmeasured
   choice here; clerk-resolved on the capture's own analysis.)* Implementing a producer
   would add a fan-out ask (new signal cost, R4-fanout audit, scan-model budget) for a
   speculative feature no filing asked to have — out of a signal-integrity build's
   character. Retiring deletes a declared, plausibly useful slot to fix an honesty bug.
   Option 3 is the module's standing posture applied (`report.md`'s own honest-reporting
   lines: "a bare zero is not health", never-omit-when-empty): the slot renders the
   literal `unmeasured` — never `[]`, never omitted — until some future build ships a
   producer. F3 carries the exact text. The workflow is untouched (the SKILL composes
   the line itself, exactly as it composes `contradiction_scan:` — keeping this build
   out of the fan-out and R4-fanout untriggered).
3. **A10-14's mechanism: schema-derived emission + persist-then-verify; the package-lint
   route is declined.** ✅ **OWNER-RULED 2026-08-23 — CONFIRMED**: the release-gate route
   is structurally blind to a field-time render (declined, no E4 cost); the structural fix
   is schema-walked emission plus persist-then-parse-and-verify with fix-and-re-persist
   stated inline, red-fixtured on the actual 0.13.0 omission. *(The addendum ruling landed the unskippable-mandatory-lines
   clause here; the filing offered schema-derived emission or a package-lint/fixture
   assertion; clerk-resolved.)* The report renders at field time — there is nothing at
   rest for the release gate to assert against, so a package-lint check cannot see the
   defect class (declined; no E4 cost). The structural fix rides the persist this build
   creates: Step 4 emits by **walking the schema block top-to-bottom, rendering every
   key** (never composing from memory — the 0.13.0 omission was exactly a from-memory
   composition), and after writing the dated `.yaml` the run **parses the persisted file
   and verifies its key set against the schema block** before the report is presented —
   a missing key is fixed and re-persisted, never shipped (the response stated inline at
   the check's home, F1). The hand-saved 0.13.0 report is the natural red fixture: run
   against the verify, it fails on the absent `manifest_write_divergence:` key
   (§Verification carries this desk-check).
4. **The upgrade-report home is the literal path `_agent/upgrade-reports/` — no
   `vault_structure` key is minted; the zone-map row carries its own interim clause.**
   ✅ **OWNER-RULED 2026-08-23 — CONFIRMED, and already DISCHARGED**: B10-10 cleared the
   merge-config debt, minted `upgrade_reports`, and rewrote this clause per its own
   retirement text. The call was correct at the time and its interim posture is retired —
   the concrete instance behind the owner's conditional reading of A7 (B10-10 disp. 3).
   *(Reconciles Q3a's "under a config path" with roundtable A7's arc-wide "no
   vault_structure key is minted this arc — C6-b's merge-config strip makes key-minting
   unsafe until that debt clears"; clerk-resolved.)* Precedents: B10-5 shipped the vault
   rung as literal `_agent/reflexes.md` with no structure-map key (same arc, same
   constraint, owner-reviewed), and the contract already documents literal-path homes
   (`_agent/dispatch.md`, Arc-3 ruling 4). A12 still demands rows in the existing
   tables, so the zone-map row lands with the literal path in the default column and a
   parenthetical interim clause carrying its own retirement — the B9-4/A7 pattern
   (slip-exposed interim postures live in shipped text): *"not yet a `vault_structure`
   key — key-minting waits on the merge-config `vault_structure` fix; the build that
   mints the key rewrites this clause in the same act"*. Mirrors `full-scale.md:7`'s
   shipped supplement line verbatim in spirit. Key-minting (and the C8(d)/vitals/test
   updates it would drag) is a declared follow-up for the C6-b fix, not this build's.
5. **The census population verdict: the persist rule hits structured parseable reports
   only.** ✅ **OWNER-RULED 2026-08-23 — CONFIRMED**: population = `vlt-lint` Step 5 +
   `vlt-upgrade` Step 4; prose summaries stay report-and-discard with their durable
   records named; the rule's "structured" qualifier keeps the population self-limiting
   rather than an enumeration that drifts. *(Q3a's "applies the rule everywhere it hits" needs the hit test stated;
   clerk-resolved.)* The rule's population is verbs that emit a **structured, parseable
   report** (stable keys, dashboard-consumable — lint's own definition, `SKILL.md:11`):
   `vlt-lint` Step 5 and `vlt-upgrade` Step 4, exactly. Prose end-of-run summaries
   (setup, decay, groom) are census-recorded **report-and-discard by design** — their
   durable state is fully on disk already (manifest/config/seeds; log lines + archive
   watermarks; groom watermarks), so persisting the prose would duplicate records
   without adding evidence. The census table (§E2) is the record; the rule sentence at
   its single home (F4) carries the "structured" qualifier so the population is
   self-limiting, not an enumeration.
6. **The persisted artifact is the YAML block verbatim; session prose stays
   session-side.** ✅ **OWNER-RULED 2026-08-23 — CONFIRMED**: the structured block is the
   report of record (what "parseable" and the acceptance instrument require); the prose
   half's durable content keeps landing in the ledger `Notes:` line; filename grammar
   mirrors lint's. *(Q3a says "persist their report verbatim"; the Step-4 emission is a
   YAML block plus surrounding owner-facing prose — the hand-save shows both;
   clerk-resolved.)* The report of record is the structured block — that is what
   "parseable" and the acceptance instrument need. The prose half's durable content
   already lands in the ledger's `Notes:` line by the existing "name the report's …
   entries here when non-empty" mechanism (`SKILL.md:138`). Lint is unchanged in this
   respect (its Step-5 block is already the whole report). Filename grammar mirrors
   lint's: `YYYY-MM-DD-HHMM-upgrade.yaml` / `YYYY-MM-DD-HHMM-lint.yaml`.
7. **Interim posture (R1): not applicable — with one boundary stated.** ✅ **OWNER-RULED
   2026-08-23 — CONFIRMED**; and as of B10-10's mint the one interim element (disp. 4's
   keyless literal path) is retired, so this build carries **zero live interim debt**. The general
   persist rule ships in the same build as both of its mechanisms (F1, F2), so nothing
   ships ahead of its mechanism. The one deliberately interim element — the keyless
   literal path (disposition 4) — carries its retirement clause in the shipped row text,
   the already-ruled pattern for slip-exposed interim postures.
8. **Legacy coexistence (A12, restated here as the ruling demands): existing `.md`
   report files stay legal, no backfill sweep** ✅ **OWNER-RULED 2026-08-23 — CONFIRMED**
   (both populations; rows stay extension-agnostic; nothing ever converts, edits, or
   prunes a prior report). One of three grandfathering rulings the owner confirmed this
   session — with legacy `status:` values (B10-10 disp. 7) and legacy `type: resource`
   files (B10-11 disp. 2) — confirming it as the module's standing posture, not three
   one-offs. Original text: — in `{lint_reports}` (vault-side) and
   for the factory-side hand-save alike. The Decay rows' "dated per-run files" wording
   already covers both extensions; F4's row edits keep it extension-agnostic. Forward
   writes are `.yaml` from this build's release on; nothing ever converts, edits, or
   prunes a prior report (the append-only clause at `vlt-lint/SKILL.md:72` stands).

## F-sites

### F1 — `skills/vlt-upgrade/SKILL.md` — Step 4 gains the persist + schema-derived emission + verify; Step 5 ledger gains the `Report:` line

**Current state:** Step 4 (`:89-112`) emits the report in-session only — "Report in a
parseable summary so the user sees exactly what changed" (`:91`), schema block
`:93-112` with per-line never-omit contracts (`manifest_write_divergence:` at `:106`:
"never omitted when empty"). No persist instruction exists anywhere in the file (grep:
zero hits — A10-4's grounding, re-verified at HEAD). Step 5 (`:120-143`) persists only
the digest ledger block (`:124-139`), whose completeness rule (`:141`) requires every
line in every entry.

**The exact change:**
- After the schema block (following the `convention_adoption` paragraph `:118` or
  directly after `:112` — builder's choice of seam), add the **persist instruction**,
  mirroring `vlt-lint/SKILL.md:72`'s form: write the Step-4 report block **verbatim** to
  `_agent/upgrade-reports/YYYY-MM-DD-HHMM-upgrade.yaml` — plain YAML, no fence, no
  wrapper; create the directory lazily on first persist (the `{upgrade_ledger}` "create
  it lazily" precedent, `:122`); append-only — never edit, prune, or re-read-to-rewrite
  past reports; retention is the human's — upgrade reports are never wake-read; the
  operating contract's *Decay contracts* table records the exemption (F4's row). Note
  the home is a literal path, not a structure-map key (disposition 4) — one clause, by
  pointer to the contract row.
- Add the **emission rule** (disposition 3), one sentence ahead of the schema block:
  the report is composed by walking this schema top-to-bottom and rendering **every**
  key in order — never from memory; a key with nothing to report renders its empty form
  (the per-line never-omit contracts stand).
- Add the **verify step** (disposition 3), after the persist: parse the persisted
  `.yaml` (it must parse whole) and verify its top-level key set matches this schema
  block's; a missing or extra key is fixed and re-persisted before the report is
  presented — the report is not done until the file verifies. This sentence is the
  failure mode's stated response (R3-spirit, at the check's home; this is an emission
  self-check, not a lint finding class — see Verification).
- Step 5 ledger block (`:124-139`): append one required line to the entry schema, after
  `- Notes:`: `- Report: <the persisted _agent/upgrade-reports/ filename | none (pre-persist upgrade)>`
  — the digest names its full report, so the ledger indexes the evidence. The `:141`
  completeness rule covers it automatically (every line required; "none" for historical
  reality only — post-this-build upgrades always have one).

**Why:** A10-4 (the gap itself — acceptance evidence, owner rulings, and the
lost-ephemeral-report class), A10-14 (the emitter-honesty defect made structurally
impossible), Q3a (the rule), disposition 1 (the persisted file becomes the factory's
acceptance instrument).

**Out of scope here:** the Step-4 prose paragraphs around the block (disposition 6 —
session-side; ledger `Notes:` carries the durable half); any change to the `:106` line's
own contract (it was always right — the emitter failed it).

### F2 — `skills/vlt-lint/SKILL.md:72` — the persist target becomes `.yaml`

**Current state:** `:72` — "Also **persist the report** (both modes): write the Step-5
report block **verbatim** to `{lint_reports}/YYYY-MM-DD-HHMM-lint.md` (append-only — …
the operating contract's *Decay contracts* table records the exemption)."

**The exact change:** the target becomes `{lint_reports}/YYYY-MM-DD-HHMM-lint.yaml` —
plain YAML, the block's content without the fence — plus one coexistence clause (A12,
disposition 8): pre-existing `.md` reports in `{lint_reports}` stay as they are — legal,
never converted or swept. Everything else on the line (verbatim, append-only, retention
the human's, never wake-read, the Decay-table pointer, no session note) survives
unchanged.

**Why:** Q3b's ruled shape, symmetric with F1.

### F3 — `skills/vlt-lint/references/report.md` — the shape framing + the `unmeasured` rendering

**Current state:** `:3` — "The fenced report block is strict YAML as a whole — keep it
parsing whole." `:61` — `high_value_gaps: [<concept>, ...]     # full mode` — the only
tree-wide occurrence of the identifier outside its declaration is nothing: the fan-out
workflow has no gap field in `PAGE_SCAN` (`vlt-lint-full.js:102-137`), no ask in
`pageScanPrompt` (`:173-174`), and computes none in the assemble step (`:368` ff —
`opportunities:` at `:422-424` carries only `near_duplicates`). A10-11's grounding,
re-verified at HEAD.

**The exact change:**
- `:3` gains the persist-shape clause: the block is emitted fenced in-session and
  **persisted as the plain `.yaml` file** (`vlt-lint` Step 6) — same content, no fence;
  keep it parsing whole in both homes.
- `:61` becomes:
  `high_value_gaps: unmeasured   # no producer exists (the fan-out computes no gap candidates) — render the literal, never [] and never omit: an empty list would claim "measured, none found"`
  Slot name and position stay stable (the B10-2/B10-3 slot-stability precedent); the
  `# full mode` annotation is subsumed by the new comment (the slot renders `unmeasured`
  wherever the `opportunities:` block renders, both modes — mode semantics of the block
  itself unchanged). The builder tunes wording; the load-bearing content is: literal
  `unmeasured`, never `[]`, never omitted, no producer named as existing.

**Why:** Q3b (`:3`); A10-11 via disposition 2 (`:61`).

**Out of scope here:** any workflow edit — the SKILL composes the line itself, exactly
as it composes `contradiction_scan:`/`entity_scan:` (the "You compose that line
yourself" pattern this file already states four times).

### F4 — `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md` — the rows and the rule (C6 fires)

**Current state:** zone map `:29-47` ends at the `lint_reports` row (`:47`: "Dated,
append-only persisted lint report blocks (`vlt-lint` Step 6)"); the mirror note `:49`
says path defaults mirror `vault_structure.default`. Decay-contracts table `:302-316`:
`{lint_reports}` exempt row at `:314`; the birth clause at `:318` ("A new accumulating
agent-zone file class enters this table in the act that creates it — no accumulator
ships without a declared decay contract").

**The exact change** (per A12 — extend the existing tables, never a new list):
- **Zone map:** one new row after `:47` — logical name column carries
  `_agent/upgrade-reports/` as a literal-path row (the `_agent/dispatch.md` /
  `_agent/reflexes.md` documented-literal precedent), "What lives there": "Dated,
  append-only persisted upgrade Step-4 reports (`vlt-upgrade` Step 4) — *not yet a
  `vault_structure` key: key-minting waits on the merge-config `vault_structure` fix;
  the build that mints the key rewrites this clause in the same act*" (disposition 4's
  interim clause, retirement in-text). The existing `:47` lint row's "report blocks"
  wording may be touched to "reports" (extension-agnostic) — cosmetic, builder's call.
- **Decay table:** one new sibling row beside `:314`:
  `| _agent/upgrade-reports/ | exempt — dated per-run files, never wake-read (disk-side, not wake-side mass); retention remains the human's (vlt-upgrade Step 4) | — | — | — |`
- **The rule's single home:** one sentence appended beside the `:318` birth clause: a
  **structured report-emitting** verb persists its report verbatim as a dated plain
  `.yaml` file under its report dir, declared in these tables in the act that creates it
  (retention-at-birth); report dirs are walker-exempt **by their rows here — never by a
  separate list**; legacy `.md` report files predating this rule stay legal, no backfill.
- **C6:** re-derive `_meta/vault-rule-card.md`, re-stamp `derived_from: … sha256:`,
  budget re-checked (`RULE_CARD_BUDGET`) — the contract is not handshaked but it is not
  free (brief-anatomy §5's standing price).

**Why:** Q3a's retention-row-same-build clause, Q3b's declared exclusion, A12's
never-a-new-list, disposition 4.

### F5 — `skills/vlt-setup/SKILL.md` — provision the new dir; report it

**Current state:** `:194` — "**Create `{lint_reports}`** (default `_agent/lint-reports/`,
empty dir) if absent — `vlt-lint` persists its dated Step-5 report blocks there. Same
never-clobber line…". The completion report at `:342` lists "`{lint_reports}` created /
present" among the enforcement-kit items.

**The exact change:** `:194` (or an adjacent sibling bullet) also creates
`_agent/upgrade-reports/` if absent — literal path, same never-clobber clause, one
pointer to the contract row (F4) rather than restated semantics; wording of the lint
half updated from "report blocks" to match F2's `.yaml` reality. `:342`'s provisioning
report gains "`_agent/upgrade-reports/` created / present" beside the `{lint_reports}`
item. (The upgrade also creates the dir lazily, F1 — setup-time creation just makes
fresh installs arrive complete; both paths are legal, neither clobbers.)

**Why:** symmetric provisioning with `{lint_reports}`; the durable home exists before
its first writer needs it.

### F6 — `skills/vlt-lint/references/full-scale.md:7` — the report-dir exclusion widens

**Current state:** the qualifying-key predicate (single-homed here per A7) excludes
"…cold storage (`archive`), and report dirs (`lint_reports`)".

**The exact change:** the report-dirs parenthetical widens to name both homes:
"report dirs (`lint_reports`; `_agent/upgrade-reports/` — a literal path, no key
today)". Strictly the keyless dir can never qualify (the predicate operates on resolved
keys), so this is a declared exclusion rather than a behavioral one — but A7's record
binds B10-6 to edit this home, and the declared exclusion keeps the predicate's stated
population honest when the key is later minted.

**Why:** roundtable A7 ("B10-6's exclusion … edit[s] that home"), Q3b's declared
exclusion made visible at the one site that walks vault dirs.

## Registration

**None.** No new skill, no new workflow, no `module-help.csv` row, no convention
`version:` move anywhere — the four conventions are untouched, so no handshake bump and
no consumer walk. Priced non-handshake costs (brief-anatomy §5): **package-lint C6**
fires on F4 (rule card re-derive + sha re-stamp + budget re-check, named in F4 and
Verification); **E4** does not fire (no new package-lint check — disposition 3 declined
that route); **E5** does not fire (`vlt-lint-full.js` is untouched; its `// depends_on:`
header and both `:173` markers stand as shipped by B10-4/B10-5).

## Out of scope (dispositioned)

- **A10-10 (wiki-index rule-vs-example contradiction)** — held for Arc 11 (owner,
  2026-08-22; the B10-6 stretch was explicitly declined). Not touched.
- **A10-12 / A10-13 (decision-log roster + `kind:` gaps)** — held for Arc 11, paired
  (owner, 2026-08-22). Not touched.
- **Minting `upgrade_reports` (or `lint_reports`-style) `vault_structure` keys** —
  deferred until the C6-b merge-config debt clears (roundtable A7, arc-wide);
  disposition 4's row clause carries the retirement in shipped text. The dragged surface
  (C8(d) row requirements, `vlt-vitals.py` map mirror, test fixtures) defers with it.
- **A package-lint / release-gate assertion on rendered reports** — rejected
  (disposition 3): reports render at field time; nothing exists at rest to assert.
- **A `high_value_gaps` producer** — rejected (disposition 2): a new fan-out ask for a
  feature nobody filed for; the honest `unmeasured` closes the defect. A future filing
  can propose the producer; when one ships, it replaces the literal.
- **Retiring the `high_value_gaps` slot** — rejected (disposition 2).
- **Backfill/conversion of any legacy `.md` report** (vault-side `{lint_reports}` files,
  the factory-side hand-save) — rejected per A12/disposition 8; coexistence is the
  ruled posture.
- **Persisting setup/decay/groom prose summaries** — census-ruled out of the rule's
  population (disposition 5).
- **The middle shapes** (frontmatter+fence contract; `.yaml` sidecar + `.md` pointer) —
  settled by Q3b; not re-litigated.
- **Any dashboard/tooling that consumes the persisted `.yaml` reports** — none exists;
  building one is nobody's current ask. The format makes it possible; that is the whole
  deliverable.
- **B10-1's `absorbed:` routing** — already shipped (`vlt-upgrade/SKILL.md:106`, per
  roundtable A6); F1 persists it along with everything else, no further work.
- **`vlt-lint-full.js`** — untouched entirely (no ask, no read list, no schema change);
  R4-fanout's audit re-run not triggered.

## Verification (unit, at rest)

- **Greps for cross-file agreement:** (1) `-lint.yaml` appears in `vlt-lint/SKILL.md:72`
  and nowhere does shipped text still direct a `.md` lint-report write;
  (2) `upgrade-reports` appears in exactly the F-site set (`vlt-upgrade/SKILL.md`,
  contract zone-map + Decay rows, `vlt-setup/SKILL.md`, `full-scale.md:7`) — each a
  pointer or its own row, no restated mechanics (single-home check);
  (3) the coexistence clause (existing `.md` files legal, no backfill) present at F2 and
  F4's rule sentence; (4) `high_value_gaps` renders `unmeasured` at `report.md:61` and
  the identifier still has no producer site (`grep -rn high_value_gaps skills/` = the
  schema line only); (5) A3 re-check: no shipped text directs reading `{lint_reports}`
  or `_agent/upgrade-reports/` for any derivation (the B10-3 grep, re-run with the new
  dir in the pattern); (6) `Report:` line present in the ledger entry schema and the
  `:141` completeness sentence still covers every line.
- **A10-14 desk-check (red-then-green):** replay the verify step (F1) against the
  hand-saved 0.13.0 report's YAML block — it must FAIL on the absent
  `manifest_write_divergence:` key (the red); against a schema-complete synthetic block
  it must pass (the green). Record both verdicts in the BUILT status.
- **Persist dry-run:** against a temp fixture vault dir, walk F1's instructions
  by hand once — emit a schema-derived block, write the dated `.yaml`, parse it back,
  verify the key set — recorded in the BUILT status (no script ships; the check is the
  SKILL's own procedure exercised once).
- **Handshake bipartite re-check:** no `version:` moved, no `consumers:` changed, no
  structure-map change (disposition 4 — deliberately none) — **package-lint Group E**
  is still run as the check of record and must PASS unchanged.
- **Packaging lint:** `uv run tools/package-lint.py` groups **A/B/C/E** PASS mid-arc
  (D/`--expect-version` is the release gate, not this build's — v0.13.0 shipped; this
  build rides the next cut). **C6 explicitly:** rule card re-derived, sha re-stamped,
  budget-checked (F4).
- **Fixture extension (R2): not applicable** — no release-gate check added or changed.
- **Legal response (R3): not applicable** — no lint finding class is added or changed
  (`unmeasured` is an opportunities-slot value contract, not a finding; the F1 verify
  is an emission self-check whose response — fix and re-persist before presenting — is
  stated inline at its home).
- **Enumeration widening (R4): substantive.** The build adds a file class
  (`_agent/upgrade-reports/` dated reports) to enumerated populations and widens each in
  the same act: the Decay-contracts table (F4 row), the zone map (F4 row), the
  `full-scale.md:7` report-dir exclusion (F6), and `vlt-setup`'s provisioning list (F5).
  Declared exclusions, not silent omissions: the dir is outside wake-read enumerations
  by design (disk-side mass — the `{lint_reports}` precedent, stated in its rows).
- **Scrub:** no personal or vault-local content in any changed shipped file; worked
  paths in shipped text are the literal defaults (`_agent/upgrade-reports/…`), never a
  specific install's artifacts. The factory-side hand-save is named only in this brief
  and the roadmap (gitignored), never in shipped text.
- **No `.decision-log.md`** left in the working tree; one commit for the build. The
  builder rewrites `status:` to a BUILT record with numbered deviations.

## Release

Not a release build — v0.13.0 shipped after B10-5; this build rides its cut's release
build (fold order per roundtable A1/A10 stands). No version strings move here.

## Acceptance (live — the same checks appended to the roadmap ledger)

Six checks.

1. **`[ship-verifiable]`** — the E2 census and E1 walk are on the record whole: the
   census table (structured emitters = lint Step-5 + upgrade Step-4; prose verbs
   recorded report-and-discard with their durable records named; the hand-saved 0.13.0
   file named as the one pre-rule specimen / migration input, unconverted) and the E1
   consumer walk (all nine entries re-verified, the `lint-debt` counter confirmed
   deriving from the `{log}` entry per `vlt-lint/SKILL.md:72`, no consumer of the `.md`
   wrapper found) are recorded in the brief and re-confirmed in the BUILT status.
   Discharged at rest.
2. **`[ship-verifiable]`** — the persist rule + `.yaml` cut landed coherently across
   every home: `vlt-lint/SKILL.md:72` persists `-lint.yaml` with the coexistence clause;
   `vlt-upgrade` Step 4 persists the schema-derived block verbatim to a dated
   `_agent/upgrade-reports/*.yaml` (dir created lazily) and the ledger schema carries
   the required `Report:` line; the contract gains both rows (zone map with the interim
   no-key clause carrying its own retirement, Decay exempt row) plus the
   persist-at-birth rule sentence beside `:318` — extending existing tables, never a
   new list; `full-scale.md:7`'s report-dir exclusion names the new dir;
   `vlt-setup` creates and reports both dirs; rule card re-derived + sha re-stamped
   (**C6 PASS**); **package-lint A/B/C/E PASS**. Discharged at rest by the brief's greps.
3. **`[ship-verifiable]`** — mandatory lines are structurally unskippable (A10-14): the
   schema-derived emission rule and the persist-then-parse-and-verify step are shipped
   in Step 4 with the fix-and-re-persist response inline, and the red-then-green
   desk-check is recorded in the BUILT status — the hand-saved 0.13.0 block FAILS the
   verify on its absent `manifest_write_divergence:` key; a schema-complete block
   passes. Discharged at rest.
4. **`[ship-verifiable]`** — `high_value_gaps` honesty (A10-11): `report.md:61` renders
   the literal `unmeasured` (never `[]`, never omitted), the identifier still has no
   producer site tree-wide, and `vlt-lint-full.js` is byte-untouched (R4-fanout not
   triggered). Discharged at rest by grep + `git diff --stat`.
5. **`[field-contingent]`** — the first upgrade under the contract persists honestly and
   the A1 posture retires; discharging event named: **the owner's next vlt-core upgrade
   (the release carrying B10-6, expected v0.14.x)** (performer: the owner; vault:
   vlt-core — factory-readable). Pass = a dated `_agent/upgrade-reports/*.yaml` exists,
   parses whole, carries the full schema key set **including `manifest_write_divergence:`
   (empty or not — A10-14's re-discharge evidence, per its filing)**, the ledger entry's
   `Report:` line names it, and the factory discharge run reads that file as the
   evidence of record with **no hand-carried transcript** (disposition 1's adopted
   instrument, first exercise). Fail = a missing/unparseable file, any absent mandatory
   key, or a discharge that needed a transcript.
6. **`[field-contingent]`** — the lint cut is live and legacy-coexistent; discharging
   event named: **the owner's first vlt-core `vlt-lint` run after that upgrade**
   (performer: the owner; vault: vlt-core; evidence: `{lint_reports}` read directly —
   this is the same event class as the already-open B10-2 (5) / B10-3 (3) tails, so one
   run can feed all three). Pass = the new report lands as `YYYY-MM-DD-HHMM-lint.yaml`
   (plain YAML, parses whole), every pre-existing `.md` report is untouched, and a
   full-mode report renders `high_value_gaps: unmeasured`. Fail = a fenced-`.md`
   persist, a legacy file converted/edited/pruned, or the slot rendering `[]`.
