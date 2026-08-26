---
title: 'Build #1 — reduce-side guards (the full-lint reduce stops believing the page scanner on two claims it can check itself, and the frontmatter-validity class finally gets a definition, a legal response and a report slot)'
status: 'BRIEFED 2026-08-26 — build via bmad-workflow-builder in a fresh session. On completion, rewrite this line to a BUILT record naming what landed per F-site, the verification output as real numbers/text (never adjectives), and numbered deliberate deviations `(1)…(2)…`; delete any `.decision-log.md` in the tree; one commit for the build.'
module_code: 'vlt'
created: '2026-08-26'
derives_from:
  - 'factory/inbox/2026-08-26-075130-attestation-misroute-survives-the-jurisdiction-narrowing.md (A13-1 Finding 1 — the attestation misroute, recurred; Finding 5 — the invented requirement; Finding 3 — the reduce-trusts-the-boolean mechanism at :609. Findings 4 and 7 are ruled OUT by Q1 and carried; Finding 2 establishes that build-1 of Cycle 12 shipped correct text, so no re-wording is in scope.)'
roadmap: 'factory/cycles/13-trusted-returns/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-26): Q1 FIRST TWO ONLY — Findings 1 + 5 ship, Finding 4 carried, so no SKILL-side arg, no joint, Q2 moot · Q3 FIX THE KNOWN INSTANCES — the general reduce-side posture is BACKLOGGED to a future cycle, named not omitted · Q4 THE INSTRUMENT IS THE REAL CORPUS AND IT GATES — the six pages that failed 2026-08-25, tagged ship-verifiable; a fixture built only over the changed surfaces does NOT satisfy it · Q5 v0.16.1 RIDING THIS BUILD ALONE · Roundtable waived (owner) on joint moved: none · spike: none. Plus the brief-time grounding ruling (roadmap §Grounding corrections — build-1): HOME IT, GUARD IT.'
risk: 'low-moderate — no convention `version:` moves and no consumer walk is owed (the workflow''s `depends_on:` pins are untouched), and the change is additive-guard rather than behavioral-removal. But it edits the **release-gated** `vlt-lint-full.js` reduce, it **narrows a live finding class** whose population has been wrong on two consecutive field runs, and it is the release build, so the `--expect-version 0.16.1` gate and both version strings ride it. The load-bearing risk is a guard that is too broad and swallows a genuine schema break — which is what acceptance check (2) exists to catch.'
---

# Build #1 — reduce-side guards

## Intent

Cycle 12's build-1 tried to stop the full-lint page scanner from reporting a missing attestation
pair as two other kinds of finding. It wrote the prohibition into the schema descriptions the
scanning agent reads. The text it wrote is **correct and remains correct** (A13-1 Finding 2 —
`vlt-lint-full.js:159` and `:168`, both re-verified at HEAD). The field reported the defect
again anyway, unchanged in shape, on the very next sweep.

The reason is `:609`: the reduce admits **any** scan whose `frontmatter_valid` is `false` and
prints the free-text `frontmatter_issue` verbatim, inspecting nothing. The prohibition was
stated in the one place in the pipeline that cannot enforce it. `unmarked_supersessions` has the
same posture at `:576` — `collect()`, unfiltered.

This build closes the two instances that are decidable **without page content**, so the workflow
needs no new data and no new args:

1. **The attestation misroute** (Finding 1) — six entries on 2026-08-25, twenty on 2026-08-24,
   hand-folded both times.
2. **The invented requirement** (Finding 5) — `ashwagandha: missing review_after`, a field that
   is optional; the same line of code carried it.

Brief-time grounding then established a third fact the capture had not: **`malformed_frontmatter`
is the module's only undocumented finding class** — one occurrence, no check definition, no legal
response, no report slot. So the class gets a home in this build, which is also what R3 obliges
the moment a build narrows a class.

**All rejected alternatives in the parent filing and in ideation are settled — do not
re-litigate.** Specifically closed: the filing's own "terminal class" diagnosis (superseded by
A13-1 Finding 3); re-wording `:159`/`:168` (Finding 2 — the wording is already right); Finding 4
and the SKILL-side arg (Q1, carried); the general reduce-side posture (Q3, backlogged); pulling
tracker #13's args route in (Q2, moot).

## Brief-time dispositions

**1. The attestation-complaint predicate is a positive test on the *claimed defect*, not a
keyword blacklist.** Ideation left "the exact predicate" to this brief. Rule: a scan is
**refused entry** to `malformed_frontmatter` when its `frontmatter_issue` names *only*
attestation fields. Implement as a normalized match over `verified_by` / `verified_at` (case- and
punctuation-insensitive; both the paired and single forms) where **no other schema field from
`:148` is also named**. The conjunction matters: a page that is genuinely malformed *and* also
unattested must still be reported, so the test is "attestation and nothing else," never
"mentions attestation."

*Reasoning: the six real entries all read as bare "missing `verified_by`/`verified_at`". A
blacklist on the token alone would swallow a legitimate compound break, which is the
over-broad-guard risk this build's acceptance check (2) is written to catch.*

**2. The required-field validation is a set membership test against `:148`, and the guard is
"claimed-missing field ∉ required-set".** A `frontmatter_issue` of the form "missing `X`" where
`X` is not in `required` (`:148` — the fourteen-name list, re-verified at HEAD) is **not a
finding** and is refused entry. `review_after` is in the schema's `required` list as a *returned
value* but is **optional in the wiki page schema** — the two are different contracts, and this
build must not conflate them.

*Binding on the builder: the authority for "is this field required of a page" is the wiki
frontmatter schema (`{conventions}/frontmatter.md`), NOT `PAGE_SCAN.required` at `:148` — which
governs what the AGENT must return, not what a PAGE must carry. `ashwagandha` is precisely this
confusion, made by a scanner. Do not reproduce it in the guard. Where the two disagree, the page
schema governs; state in the code comment which one is being read and why.*

**3. Refused entries are not silently dropped — they route to the attestation surface.** A scan
refused under disposition 1 carries a real fact (the page is unattested). That fact already has a
home: `unattested_write` (`:588`) and the `attestation_census` (`:554`), both computed
independently from `attested()` (`:546`) over the same returned values. So the refusal needs no
re-routing — the fact is *already* reported through the correct slot, and refusing the duplicate
is exactly what stops the double-report. **Verify this rather than assume it** (Verification 3):
the six pages must appear in the attestation surface after the guard, not vanish.

*A scan refused under disposition 2 carries no fact at all — the requirement does not exist — and
is simply dropped. That asymmetry is deliberate and is stated in the code comment.*

**4. `unmarked_supersession` gets the same guard, at `:576`.** Finding 1's sixth entry
(`execution-to-judgment-shift`) landed there, not in `malformed_frontmatter`. `collect()` at
`:542` is generic and shared, so the guard is applied at the **call site** (`:576`), never inside
`collect()` — changing `collect()` would silently alter every other class that uses it.

**5. R1 — Interim posture: not applicable.** This build ships no rule ahead of its mechanism; the
guard and its documentation land together in the same build.

**6. Retirement disposition — a retirement is NAMED and DEFERRED, not silently survived.**
*(Platform P-15.)* The prohibitions this build's guard makes redundant are the prompt-side
sentences at `:159` and `:168`. **They are deliberately NOT retired here** — they remain correct,
they are cheap, and a scanner that honours them produces less work for the guard. Defence in
depth is the intended posture, stated so a later reader does not read the survival as an
oversight.

The live retirement candidate is different and larger: **`malformed_frontmatter` itself.** Once
the guard lands, the class's genuine population is "schema breaks that are not attestation and
not invented" — which may be fully covered by the documented `frontmatter_drift` (`:573-575`).
**Ruled: deferred to a later build, not taken here.** Retiring a shipped finding class is a
behavioral removal that needs a measured population before it is safe, and this build's own
acceptance produces exactly that measurement (check 2 records what genuinely reaches the class).
The disposition names the successor: **the Cycle 13+ build that takes Q3's general posture also
takes this retirement, informed by this build's field numbers.** Recorded in the roadmap's
Carried-forward section in the same run.

## F1 — `vlt-lint-full.js:609`, the `malformed_frontmatter` reduce

**Current state**, re-verified at HEAD (`c2d66af`):

```js
    malformed_frontmatter: scans.filter((s) => s.frontmatter_valid === false).map((s) => `${s.slug}: ${s.frontmatter_issue || 'invalid'}`),
```

Admits every scan whose boolean is `false`; prints the free-text reason unread.

**The change.** Interpose the two guards from dispositions 1 and 2 between the filter and the
map. Both operate on `s.frontmatter_issue`; neither needs page content. Carry a comment naming
**why** the reduce checks a claim the prompt already prohibits — the prompt cannot enforce, and
Cycle 12 build-1 is the evidence.

**Why.** A13-1 Findings 1, 3 and 5. This single line carried both the attestation misroute and
the invented requirement across two consecutive full runs.

**Out of scope at this site:** `s.frontmatter_valid === true` scans are untouched; the guard
never *adds* an entry, only refuses one.

## F2 — `vlt-lint-full.js:576`, the `unmarked_supersessions` reduce

**Current state**, re-verified at HEAD:

```js
    unmarked_supersessions: collect('unmarked_supersession'),
```

`collect` is defined at `:542` and is shared by several classes.

**The change.** Apply disposition 1's attestation predicate at **this call site only**, filtering
the collected entries. **Do not modify `collect()` at `:542`** — it is generic and shared; a
guard inside it would silently narrow every other class built on it.

**Why.** A13-1 Finding 1's sixth entry (`execution-to-judgment-shift`) arrived here. `:168`'s
prompt-side prohibition is correct and was ignored, exactly as `:159`'s was.

## F3 — `skills/vlt-lint/references/checks.md`, the missing check definition (R3)

**Current state:** `grep -in "malformed" checks.md` → **no check definition for
`malformed_frontmatter` anywhere in the file.** The class is emitted by the workflow and defined
nowhere.

**The change.** Add the check entry alongside its siblings, carrying (a) the class's population —
frontmatter that is genuinely absent or structurally unparseable, or that breaks the page schema
in a way `frontmatter_drift` does not already cover; (b) the **two explicit exclusions** this
build ships, each with its reason and its correct destination — attestation-only complaints
(→ the attestation surface, `write-verification@3` Scope rule) and claimed-missing optional
fields (→ not a finding); and (c) the **legal response**, which R3 requires and which the class
has never had.

Mirror the form of the *Attestation findings* entry at `:16` and *Unmarked supersessions* at
`:35` — both state population, carve-outs and legal response in that order.

**Why.** R3: a build that changes a finding class states that class's legal response at the
check's own single home, in the same build. This build narrows the class, so the obligation
fires — and the class had no home at all.

## F4 — `skills/vlt-lint/references/report.md`, the missing slot

**Current state:** `grep -n "malformed" report.md` → **0**. The workflow returns a key the report
schema does not document. `frontmatter_drift` is documented at `:17`; `unattested_write` at
`:33`.

**The change.** Add the `malformed_frontmatter:` slot in the `fix_now:` block adjacent to
`frontmatter_drift:` at `:17`, in the file's established `[<page: what is wrong>, ...]` form,
with the exclusions noted inline as the sibling slots do.

**Why.** The undocumented key is the mechanical reason both field runs required a hand-fold: the
executor received entries for a class the report schema had nowhere to render. Documenting the
slot is what makes the guard's effect observable in a persisted report — and acceptance check (2)
reads that slot.

**Out of scope:** no other slot's population is touched; `frontmatter_drift` keeps its exact
population.

## Registration

**None.** No new skill, no new workflow, no `module-help.csv` row. No convention `version:`
moves, so no consumer walk and no re-ack is owed — `vlt-lint-full.js`'s `depends_on:` pins at
`:11` are **untouched**, and `vlt-lint/SKILL.md:4`'s pin vector is untouched.

**Priced anyway, per the "no bump owed is not no cost" rule:**
- **package-lint C6** — **not triggered.** This build does not edit
  `governance/_meta/vault-operating-contract.md`, so no `vault-rule-card.md` re-derivation is
  owed. *Verify this holds rather than assuming it: if any contract text is touched, C6 fires.*
- **package-lint E4** — **not triggered.** This build adds no new `package-lint` check, so no
  declaring case in `tools/test-package-lint.py` and no `CASE_FLOOR` bump is owed.
- **package-lint E5** — **not triggered.** The workflow's `// depends_on:` header at `:11` is not
  edited. The guard adds no convention read.

## Out of scope (dispositioned)

1. **Finding 4 — the paraphrased verbatim `summary`** (`:162` asks verbatim, `:545` measures the
   returned string). **Ruled out by Q1**; carried in the roadmap's Carried-forward section. Needs
   a SKILL-side per-page arg because the workflow has no filesystem access (`:36-37`).
2. **The general reduce-side posture** — *every mechanically-checkable agent return is checked at
   the reduce.* **Ruled out by Q3**, backlogged to a future cycle by name.
3. **Tracker #13, the file-based args route.** Q2 moot — no arg is added here. Still
   `vault-filed`, not `vault-accepted`; it is candidacy, not admitted signal.
4. **Re-wording `:159` / `:168`.** A13-1 Finding 2: the text is already correct. Deliberately
   retained as defence in depth (disposition 6).
5. **Retiring `malformed_frontmatter`.** Deferred by disposition 6 to the build that takes Q3's
   posture, informed by this build's measured population. Named, not silently survived.
6. **`sources_vs_prose_mismatches` misclassification** (tracker #12) and **the YAML-library
   assumption** (tracker #14). Both `vault-filed` candidacy, neither accepted; they belong to
   Cycle 13's first full capture batch, not to this patch.
7. **`frontmatter_drift`'s population** (`:573-575`) — untouched. It is the sibling this build's
   deferred retirement would eventually fold into, which is a reason to leave it exactly as it is
   now.

## Verification (unit, at rest)

1. **The two-guard harness run, over the real returns.** Load the shipped workflow source with
   stubbed `agent`/`parallel`/`phase`/`log`/`budget` and `args` delivered as a **JSON string**
   (the standing runtime rule). Feed scripted scan results reproducing the six real 2026-08-25
   entries — five with `frontmatter_valid: false` + attestation-only `frontmatter_issue`, one
   with an `unmarked_supersession` attestation complaint — plus **three negative controls**: a
   genuine schema break (`title` missing), a **compound** break (malformed *and* unattested,
   per disposition 1), and a genuine unmarked supersession. Record the resulting
   `malformed_frontmatter`, `unmarked_supersessions`, `unattested_write` and
   `attestation_census` arrays **verbatim**.
2. **`collect()` is unchanged and its other consumers are unaffected.** Diff `:542` (must be
   byte-identical) and confirm every other `collect('…')` call site returns what it returned
   before, on the same fixture.
3. **The refused facts still land** (disposition 3). On the fixture, the six refused pages appear
   in `unattested_write` and are counted in `attestation_census.unattested_pre_adoption` — the
   guard removes a duplicate, never a fact.
4. **Greps for cross-file agreement.** `grep -rn "malformed_frontmatter" skills/` now returns the
   emitting line **plus** the `checks.md` definition **plus** the `report.md` slot — the class is
   homed. `grep -c "depends_on" ` on the workflow and `vlt-lint/SKILL.md` unchanged.
5. **Packaging lint** — `uv run tools/package-lint.py` A/B/C/E during the build; the
   `--expect-version 0.16.1` D gate at release (§Release).
6. **R2 — fixture extension: not applicable.** No release-gate check is added or changed.
7. **R3 — legal response: satisfied by F3**, which states the class's legal response at its single
   home for the first time.
8. **R4 — enumeration widening: not applicable.** This build adds no file to any enumerated class
   (no new asset, no new always-loaded partner file, no new skill asset). It adds one key to a
   report *schema*, which is a slot definition, not a file enumeration.
9. **Scrub** — no personal or vault-local content in any changed shipped file; no vault-local
   artifact paths in the `checks.md` / `report.md` prose (placeholders only). Confirm the six page
   slugs used in the harness live **only** in the brief and the factory record, never in a shipped
   file.
10. **No `.decision-log.md`** anywhere in the working tree at completion.

## Release

This build is the last (and only) build in **v0.16.1**.

- Bump **both** version strings: `.claude-plugin/marketplace.json` `"version"` and
  `skills/vlt-setup/assets/module.yaml` `module_version`, both to `0.16.1`.
- Add the `CHANGELOG.md` entry for v0.16.1, dated the day the tag is cut — **re-stamp the heading
  date if the release slips past the authoring date** (package-lint D checks the version, not the
  date; this bit Cycle 12's build-2, deviation 7).
- Pre-tag gate: `uv run tools/package-lint.py --expect-version 0.16.1` — **tag only on exit 0**,
  and record the PASS summary line in the release commit message.
- Then ff-merge to `main`, tag `v0.16.1`, push main + tag. Work on branch `cycle13-v0.16.1`.
- **The release is not performed by the builder** unless the owner says so — hold for the owner
  per the standing choreography (`vlt-release`).

## Acceptance (live — appended to the roadmap ledger)

Four checks — **three ship-verifiable (all gate closeout), one field-contingent (does not
gate)**. Q4 governs check (2) and is binding: the instrument is the real corpus.

**(1) `[ship-verifiable]` — GATES closeout.** The guards behave on the reproduced real returns —
over the Verification-1 fixture, the five attestation-only entries and the one attestation
`unmarked_supersession` are **refused** (absent from `malformed_frontmatter` and
`unmarked_supersessions`), while **all three negative controls survive**: the genuine schema
break, the **compound** break (malformed *and* unattested — disposition 1's conjunction), and the
genuine unmarked supersession all still report. Instrument: the Verification-1 harness against
the shipped workflow source, factory-side and at rest, `args` as a JSON string. Evidence: the four
arrays recorded verbatim in the BUILT `status:`.

**(2) `[ship-verifiable]` — GATES closeout. This is Q4's check and it is graded against the real
corpus.** Re-run the page scanner over the **six real pages that failed on 2026-08-25** —
`bistec-encebollado`, `k-curve-career-divergence`, `kettl`, `llm-wiki-pattern`, `obsidian-bases`
(the five `malformed_frontmatter` entries) and `execution-to-judgment-shift` (the
`unmarked_supersessions` entry) — and confirm **zero** of the six reach either class, while the
attestation surface still carries them. Instrument: a single-agent reader probe (matching the
full-lint scan model) over **copies of those six pages taken from `{field-vault}` read-only**,
plus the shipped guard applied to the returns; the vault is never written. Evidence: the returned
JSON and the post-guard arrays, verbatim in the BUILT `status:`.

*Binding, per Q4 and stated so a builder cannot satisfy this cheaply: **a fixture constructed to
exercise only the surfaces this build changes does NOT satisfy this check**, alone or in
addition. Cycle 12 build-1's at-rest probe passed on exactly such a fixture while the field
failed, because it could not observe leakage into a slot it did not model. The six real pages are
the instrument because they are the population that actually broke.*

**(3) `[ship-verifiable]` — GATES closeout.** The class is homed and the release gate survives —
`grep -rn "malformed_frontmatter" skills/` returns **three** hits (the emitter, the `checks.md`
definition with its legal response, the `report.md` slot) where it returned **one** before;
`collect()` at `:542` is byte-identical; the workflow's `depends_on:` at `:11` and
`vlt-lint/SKILL.md:4`'s pin vector are unchanged; and
`uv run tools/package-lint.py --expect-version 0.16.1` exits **0** with both version strings
reading `0.16.1`. Instrument: the Verification-4 greps plus `package-lint`'s own A/B/C/D/E run,
at rest. Evidence: the grep outputs verbatim and the PASS summary line.

**(4) `[field-contingent]` — does not gate.** The defect is gone in anger, and the hand-fold with
it — on the next full-mode `vlt-lint` run on `{field-vault}` after upgrading to v0.16.1, **no**
entry in `malformed_frontmatter` or `unmarked_supersessions` is an attestation complaint, **no**
entry is a claimed-missing optional field, and the report's `fixes_applied:` block records **no
hand-fold of misrouted attestation entries** — against a corpus that produced twenty such folds on
2026-08-24 and six on 2026-08-25. **Event:** the owner runs `vlt-lint --full` on `{field-vault}`
after upgrading it to v0.16.1. **Performer:** the owner (standing rule — the factory never writes
to a vault). **Vault:** `{field-vault}` only — it is the sole install with the 146-page wiki and
the two-run history that produced this defect's baseline. **Bound:** the first full lint after the
v0.16.1 upgrade, no later than Cycle 13's first full capture batch.

*Stated honestly at brief time, and the reason this is the ONLY field-contingent check here: it
measures the same thing as check (2) but in anger. Check (2) carries the gate precisely so this
one does not have to — the Cycle 12 lesson (a build's central promise riding entirely on an
ungated field check) applied at brief time rather than after a failure. If this check fails while
(2) passed, the guard is right and the corpus moved; that is a new filing, not a re-carry.*

*Bound note: this check's bound names **Cycle 13's first full capture batch**, not "Cycle 13's
`inbox-capture`" — the narrow patch capture that opened this cycle deliberately does not trigger
bounds (roadmap §Owner ruling — narrow-capture carve-out, 2026-08-26).*
