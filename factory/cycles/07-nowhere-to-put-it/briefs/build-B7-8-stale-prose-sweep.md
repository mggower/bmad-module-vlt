---
title: 'Build #B7-8 — the stale-prose sweep (shipped prose catches up with what the arc made true)'
status: 'BUILT 2026-08-15 — all three F-sites landed per brief; deviations: none. Verification: (1) grep "cannot fire" in spec.md → exactly 2 hits, :14 and :92, both carrying the conditional "while adoption is zero" form, no permanent-form assertion remains; (2) git grep "council + lint-full" -- skills/ → zero hits on the tracked shipped surface (untracked skills/reports/ dev artifacts still quote the string, as expected); (3) vlt-upgrade/SKILL.md :105/:112 agree on the "created … — N days" vocabulary, "declared since" gone from the file, proxy stated at :112 per vault-operating-contract.md:263; (4) spec_notification_missing design note present in the Enforcement paragraph (spec.md:90), placeholder paths only; (5) handshake untouched — spec.md version: 2 and consumers: unchanged, last_updated bumped to 2026-08-15, no depends_on ack moved; package-lint Group E PASS is the check of record; (6) uv run tools/package-lint.py --expect-version 0.9.1 → exit 0, A/B/C/D/E all PASS; (7) uv run tools/test-package-lint.py → 21/21 green, CASE_FLOOR 21, tools/ diff empty (R2 not triggered); (8) no .decision-log.md on disk; scrub clean — no personal/vault-local content in the three edited shipped files.'
module_code: 'vlt'
created: '2026-08-15'
derives_from:
  - 'inbox/2026-08-14-142625-spec-blind-spot-statement-stale-after-adoption.md (A7-6 — both stale sites, spec.md:92 + :14; the forward-looking spec_notification_missing path warning)'
  - 'skills/reports/arc7-A4-sizing-audit.md (amendment-A4 fix list — N1 lands here; F-list items :17/:235/:238/:243 and the A7-7/A7-12 sites verified consumed by B7-3/B7-5/B7-6 at HEAD; the vlt-upgrade:112 created:-proxy watch dispositioned here)'
roadmap: 'skills/reports/inbox-evolution-arc7-roadmap.md'
rulings: 'roadmap §Ideation rulings + §Post-ideation amendments (2026-08-15): B7-8 grouping row (two spec.md sites, conditional form, prose clarification — NO spec bump); A7-6 class-sweep pin (one sweep shared with count-since-N, run last against the arc''s finished state); amendment A4 (sizing before B7-3, fixes here); evidence-debt disposition (A7-6''s vault-side counts NOT BLOCKING, attach to acceptance); brief-time designation (B7-8 carries the spec_notification_missing warning; the check itself is not Arc-7 scope)'
risk: 'low — prose-only edits across three shipped files; no convention version bump, no consumer walk, no release-gate check added or changed (no fixture case, CASE_FLOOR stays 21)'
---

# Build #B7-8 — the stale-prose sweep

The arc's last build, deliberately: the sweep runs against B7-1..B7-7's finished state (the
build-23 precedent the pin cited). It closes A7-6 — `spec.md`'s blind-spot statement asserts a
*permanent* property (`deferral_metric` "cannot fire … its only attainable value is 'fine'")
that the `adoption_first_instance:` stamp is designed to invalidate per-vault, at two sites that
must move together — and discharges the fixing half of amendment A4's split: the sizing audit
(`skills/reports/arc7-A4-sizing-audit.md`) ran before B7-3 and its fix list was deliberately
left to this build. Re-grounding at HEAD shows most of that list already consumed by earlier
Arc-7 builds (recorded below so nothing is re-fixed); what remains is three files of prose.

All rejected alternatives in the parent filing and the audit's excluded borderlines are settled
— do not re-litigate. In particular the audit's exclusion list (self-healing
`adoption_first_instance: null` comments; `frontmatter.md:121`'s no-`.base` claim;
`vault-operating-contract.md:86`'s two tool-infrastructure folders — re-verified true at HEAD;
`vlt-lint/SKILL.md:11`'s cadence advice) exists precisely so this build does not re-sweep them.

## Audit fix-list disposition at HEAD (re-grounded 2026-08-15, branch `arc7-v0.10.0` @ `0720ee3`)

| Audit item | Site (audit-time) | State at HEAD | Lands in B7-8? |
|---|---|---|---|
| Class 1 #1 | `frontmatter.md:17` threshold baseline | **CONSUMED by B7-3** — now reads "2 prose/behavior drift findings **since 2026-08-15**, or the 3rd convention minted **beyond the 9 shipped at that baseline**" (`frontmatter.md:17`); 9 conventions verified shipped | No |
| Class 2 N3 | `frontmatter.md:235` template `<numeric tripwire>` | **CONSUMED by B7-3** — template now "a number, or a short prose threshold a vault can evaluate from its own state" (`frontmatter.md:236`) | No |
| Class 2 N2 | `frontmatter.md:238`/`:243` null/absent conflation | **CONSUMED by B7-3** — three-value semantics stated at both the template comment (`frontmatter.md:240`) and the Adoption-axis paragraph (`frontmatter.md:244`) | No |
| Class 2 (a)#5 | `frontmatter.md:218` knowledge-gap "cue for the Researcher" | **CONSUMED** (B7-3/B7-5) — now "a topic the vault is thin on" (`frontmatter.md:218`), with the address rule at `:222` | No |
| Class 2 (a)#6 | `vlt-mint/SKILL.md:144` "ack covers its own workflow assets" | **CONSUMED by B7-6** — now the workflow-assets-as-named-consumers rule (`vlt-mint/SKILL.md:149`) | No |
| Class 2 (a)#3/#4 | `frontmatter.md:36` rule 4 / `vlt-ingest:147` template | **CONSUMED by B7-3/B7-6** (A7-9/A7-10, their own builds) — rule 4 carries the split + form + normalization + coexistence (`frontmatter.md:32`) | No |
| Class 2 (a)#1/#2 | `spec.md:92` + `:14` | **HOLD verbatim** — the A7-6 sites, untouched | **Yes — F1** |
| Class 2 N1 | `vlt-setup/SKILL.md:295` "council + lint-full" | **HOLDS, trivially shifted to `:305`** — still enumerates two of three workflows | **Yes — F2** |
| Watch | `vlt-upgrade/SKILL.md:112` `created:`-proxy | **HOLDS at `:112`** (+ the schema twin at `:105`) | **Yes — F3** (see disposition 2) |

New-stale-prose sweep over the seven built Arc-7 builds' own prose, run at HEAD (recorded so
verification can replay it): version pins all current (`frontmatter@7` ×7 incl. the
`vlt-lint-full.js` header ack, `decision-log@2` ×3, zero stray `@5`/`@6`/`@1` pins); no stale
case counts (`CASE_FLOOR = 21` at `tools/test-package-lint.py:229`, no prose asserting 18/20);
no other "cannot fire"-class permanent assertions outside `spec.md` (the `vlt-lint`
blind-spot texts at `checks.md:29`/`:49` are *structurally* permanent by construction — the
correct kind); the two `frontmatter.md` interim postures naming "the seam build" are **correct,
not stale** (B7-4 is unbuilt — do not touch them, or anything else in the dispatch
addressee/roster seam). **The sweep's one new find is N1 (F2). Nothing else lands.**

## Brief-time dispositions

1. **The `spec_notification_missing` path warning lands in `spec.md`'s Enforcement paragraph
   (`:90`), as prose — no bump.** The roadmap designates B7-8 to "carry the warning to whoever
   builds the deferred check"; the roadmap itself archives at closeout, and the deferred
   machinery's single description — the place that builder will actually read — is `spec.md:90`.
   A sentence constraining a check that does not exist changes no rule any consumer follows
   today, so per the version-handshake rule it is a prose clarification: `version: 2` holds, no
   consumer walk. (Alternative rejected: leaving it only in the watch register — a dev artifact
   a future field builder never sees.)
2. **The `created:`-proxy watch LANDS here, in its minimal form** (the audit recorded it as a
   watch and left the disposition to this brief). Grounds: the operating contract's
   honest-reporting rule already governs it — *"A proxy that stays is stated as one, beside the
   finding it produces"* (`vault-operating-contract.md:263`; rule-card row
   `vault-rule-card.md:53` names "proxies" explicitly). `vlt-upgrade:112` reports "declared
   since `created:`" — claiming a declaration date on the signal of a file-birth date — without
   stating the proxy. The fix is the contract's own first option: **narrow the claim to what the
   signal establishes** (report "created", not "declared since") and state the proxy once in the
   prose. No mechanism, no new field, no retrofit handling — the audit's grading ("not an
   instance now; the exact shape that becomes one") stands, and the watch closes because the
   prose stops over-claiming. No handshake implication: the report vocabulary is `vlt-upgrade`'s
   own surface; `frontmatter.md:244` points at the report without restating its strings, and the
   contract is deliberately not handshaked.
3. **C6-c (the `vlt-release` Stage-7 backfill bullet) stays the owner's action item — out of
   B7-8 scope.** Status checked at HEAD: still absent from
   `.claude/skills/vlt-release/references/choreography.md` (no backfill bullet in Stage 7,
   `:139-150`). It is factory-side gitignored tooling, not shipped prose, the replacement text
   already exists verbatim (`skills/reports/archive/build-B6-1-changelog.md`, `status:`
   deviation (3)), and B6-1's build session was refused the edit twice by the environment's
   command classifier — a builder session would face the same guard. Sweeping it into a shipped-
   surface build would blur the build's public/dev boundary for no gain.
4. **No Release section.** B7-8 is last in ship order but B7-4 (owner-blocked) is unbuilt;
   whether v0.10.0 ships around B7-4 is the owner's release-time ruling, and the dual version
   bump + `--expect-version` gate ride the release build via `vlt-release`, not this brief.

## F1 — `spec.md`: the blind-spot statement goes conditional (both sites, together)

File: `skills/vlt-setup/assets/governance/_meta/conventions/spec.md` (the governance-bundle
SSoT — never a second copy).

**Current state.** Two sites assert the permanent form, re-grounded verbatim at HEAD:

- `:14` — the frontmatter comment on `deferral_metric:`: `# at zero adoption this cannot fire —
  see Enforcement, the blind-spot statement`. The capture's judgment holds: this is the more
  dangerous site, four lines above the reader's eye.
- `:92` — the Enforcement paragraph: *"at zero adoption the `deferral_metric` cannot fire — …
  presupposes a spec that exists, so its only attainable value is 'fine' — which means it
  measures **notification discipline once specs exist, never adoption itself**."*

The shipped base still carries `adoption_first_instance: null` (`:17`), so the statement is true
of the shipped artifact and false in any vault that has stamped adoption (vlt-core reportedly
has — taken as reported, vault-side; the evidence-debt ruling attaches it to acceptance, check
3). The defect class: prose asserting a permanent property a frontmatter field is designed to
invalidate, going stale in every vault at a different moment.

**Exact changes** (the filing's proposed conditional form, ruled "the right shape" at capture;
must touch both sites or the correction half-lands):

1. `:14` — replace the comment with:
   `# while adoption is zero this cannot fire — see Enforcement, the blind-spot statement`
2. `:92` — replace the sentence up to the em-dash before "The bound that fires" with:

   > **The deferral's blind spot, stated in its own text:** **while adoption is zero** the
   > `deferral_metric` cannot fire — "spec version bumps shipping without their relay entries"
   > presupposes a spec that exists, so until the first spec does, its only attainable value is
   > "fine". In both regimes it measures **notification discipline once specs exist, never
   > adoption itself** — adoption is the orthogonal `adoption_first_instance:` axis
   > (`frontmatter.md`, *Adoption axis*).

   The closing sentence (`review_after:` expiry as the adoption-independent bound, honest-
   reporting citation) stays verbatim.
3. `:90` — append the forward-looking design note to the Enforcement paragraph (disposition 1),
   placeholder paths only:

   > Design note for the deferred `spec_notification_missing` check, recorded ahead of its
   > build: a promotion-era `version` bump may have been relayed against the doc's
   > **pre-promotion path** (a handoff at `_agent/handoffs/{date}-{slug}.md`, promoted to
   > `{specs}/...` only afterwards — drained relay entries are not re-pointed by the relocation
   > migration), so notification matching must accept a relay entry referencing any of the
   > spec's historical paths; keying on the `{specs}` path alone scores exactly that history as
   > un-notified — a false positive on the class the check exists to measure.

4. Bump `last_updated:` (`:4`) to the build date. **Do not bump `version:`** — ruled at
   ideation (grouping row: "Prose clarification: no `spec` bump"); no `consumers:` walk, no
   `depends_on` acks move.

**Why:** A7-6, both grounded sites; the conditional form is true in both regimes and never goes
stale. **Out of scope at this site:** stamping `adoption_first_instance:` in the shipped base
(it is honestly `null` for the module — vault stamps are vault-local, excluded from the
divergence diff); building either deferred lint check (not Arc-7 scope, per the brief-time
designation).

## F2 — `vlt-setup/SKILL.md`: the Confirm line stops enumerating workflows

**Current state.** `skills/vlt-setup/SKILL.md:305` (audit-time `:295`, trivially shifted): the
per-vault Confirm bullet reads *"the **dynamic workflows** (`.claude/workflows/*.js` — council +
lint-full) installed/refreshed"*. §2a (`:162-174`) installs **three** — `vlt-review-council.js`,
`vlt-lint-full.js`, `vlt-consult.js` (`:166-168`), via "copy every `*.js`" (`:172`) — and B7-6
made all three named handshake nodes. The skill's own honest-surface report line fell behind the
consult addition: audit item N1, and exactly the lists-that-claim-completeness drift.

**Exact change.** In `:305`, replace `(`.claude/workflows/*.js` — council + lint-full)` with a
point-at-the-map form carrying no enumeration:
*"the **dynamic workflows** (`.claude/workflows/*.js` — every workflow §2a ships)
installed/refreshed"*. Per the structural doctrine (standing rule: prefer point-at-the-map over
enumerations when fixing stale lists) — §2a is the single home of the roster, and a fourth
workflow can never re-stale this line.

**Why:** audit N1. **Out of scope at this site:** the §2a roster itself (`:166-168` is correct
and is the map being pointed at); the copy-every-`*.js` mechanics (`:172`, already structural).

## F3 — `vlt-upgrade/SKILL.md`: the adoption line stops over-claiming its proxy

**Current state.** Two sites in one file, re-grounded:

- `:105` — the result-JSON schema: `declared, no first instance yet (declared since YYYY-MM-DD —
  N days)`.
- `:112` — the prose: *"an explicit `null` reports **declared, no first instance yet (declared
  since `created:` — N days)**, deriving the date from the convention file's own `created:`
  frontmatter"*.

"Declared since" claims a declaration date; the signal is the file's birth date. Exact today
only because every axis-carrying convention was born with the axis; an axis retrofitted onto an
older convention would misdate. The audit graded it a watch; disposition 2 lands the minimal fix
under `vault-operating-contract.md:263` (narrow the claim / state the proxy). No other shipped
file renders this vocabulary (swept: the only "declared since" hits are these two lines).

**Exact changes** (both sites, same vocabulary — cross-file agreement is the verification grep):

1. `:105` — the schema variant becomes:
   `declared, no first instance yet (created YYYY-MM-DD — N days)`
2. `:112` — reword the matching clause to: *"an explicit `null` reports **declared, no first
   instance yet (created `YYYY-MM-DD` — N days)**, the date read from the convention file's own
   `created:` frontmatter and reported in that vocabulary — `created:` is a **proxy** for the
   axis's declaration date (exact while an axis is born with its file; stated as a proxy per the
   operating contract's honest-reporting rule) — so a long-lived null is readable at the only
   cadence that reports the axis"*. The rest of the sentence (`axis not declared`, the
   three-values rationale, never-omitted-when-empty, report-never-gate) stays as is.

**Why:** the watch's disposition (brief-time disposition 2). **Out of scope at this site:** any
declaration-date field or retrofit mechanism (no retrofit exists; if one ever does, the stated
proxy is the tripwire that surfaces it); `frontmatter.md:244`'s pointer (it names no strings —
verified, no edit needed).

## Registration

**None.** Prose edits only: no new skill or workflow, no `module-help.csv` row, no convention
`version:` bump ⇒ no consumer walk / re-ack (F1's no-bump is an ideation ruling; F2/F3 touch
skill report prose, not convention rules).

## Out of scope (dispositioned)

- **B7-4's territory** — the dispatch addressee/roster seam, the divergence-diff
  generalization, the `baseline_missing` exemption. Untouched; the two `frontmatter.md` interim
  postures naming "the seam build" are correct while B7-4 is unbuilt — **not** stale prose.
- **The two deferred `spec.md` lint checks** — not Arc-7 scope (brief-time designation); F1(3)
  is the warning for their eventual builder, nothing more.
- **C6-c** — stays the owner's paste (disposition 3).
- **Audit items consumed by B7-3/B7-5/B7-6** — verified fixed at HEAD (table above); re-fixing
  is forbidden.
- **The audit's excluded borderlines** — settled by the audit's own exclusion list; not
  re-swept.
- **`vlt-lint` blind-spot texts** (`checks.md:29`/`:49`, `report.md:49-72`) — permanent *by
  construction* claims about what a check structurally cannot see; the correct kind of
  permanence, not the A7-6 class.
- **Rule-card sha re-derive (C6)** — not owed: no `vault-operating-contract.md` edit in this
  build (F3 *cites* the contract, it does not change it). If the builder finds itself editing
  the contract, that is outside this brief — stop and report.

## Verification (unit, at rest)

- **Greps for the fixes and their agreement:**
  - `grep -n "cannot fire" skills/vlt-setup/assets/governance/_meta/conventions/spec.md` → both
    hits carry the conditional "while adoption is zero" form; no permanent-form assertion
    remains; `:14` and `:92` agree.
  - `grep -rn "council + lint-full" skills/` → zero hits.
  - `grep -n "declared since\|created YYYY" skills/vlt-upgrade/SKILL.md` → `:105` and `:112`
    carry the same "created" vocabulary; "declared since" gone.
  - `grep -c "spec_notification_missing" skills/vlt-setup/assets/governance/_meta/conventions/spec.md`
    → the design note present in the Enforcement paragraph.
- **Handshake untouched:** `spec.md` `version: 2` and `consumers:` unchanged; no `depends_on`
  ack moves anywhere. **Check of record: `package-lint` Group E** (mid-arc A/B/C/E run) —
  confirming `frontmatter@7` / `spec@2` / `decision-log@2` all bipartite-consistent and no
  stray pins; a hand-written handshake grep is not a substitute.
- **Packaging lint:** `uv run tools/package-lint.py` A/B/C/E green (D/`--expect-version` is the
  release gate, per disposition 4). C6 (rule-card sha) passes untouched — the contract is not
  edited.
- **Fixture (R2):** no release-gate check added or changed → no new fixture case;
  `uv run tools/test-package-lint.py` still 21/21, `CASE_FLOOR` stays 21.
- **Scrub:** the three edited shipped files carry no personal/vault-local content; F1(3)'s
  worked example uses placeholder paths (`_agent/handoffs/{date}-{slug}.md`, `{specs}/...`).
- **Builder exit obligations:** rewrite this `status:` to a BUILT record with numbered
  deviations; delete any `.decision-log.md`; one commit for the build.

## Acceptance (live — appended to the roadmap ledger)

1. **[ship-verifiable]** the sweep's fixes coherent at rest — `spec.md` conditional at both
   sites (`:14` comment + Enforcement paragraph agreeing; no permanent-form "cannot fire"
   assertion in the shipped surface) with the `spec_notification_missing` path-warning design
   note present and `version: 2` unmoved; `vlt-setup`'s Confirm line points at §2a with no
   workflow enumeration; `vlt-upgrade`'s adoption vocabulary "created — N days" identical at
   `:105`/`:112` with the proxy stated; `package-lint` A/B/C/E green, Group E confirming
   `frontmatter@7`/`spec@2`/`decision-log@2` bipartite-consistent with zero stray pins; harness
   21/21, `CASE_FLOOR` 21 (no gate check touched). Dischargeable at rest, re-confirmed at the
   arc's release gate.
2. **[ship-verifiable — next ordinary upgrade, either vault]** delivery — installed `spec.md`
   carries the conditional form at both sites + the design note (and, in an adoption-stamped
   vault, the base text no longer contradicts the vault's stamped state), installed `vlt-setup`
   / `vlt-upgrade` carry the report-line edits, and the first post-upgrade run's
   `convention_adoption` line renders the "created — N days" vocabulary for any null axis;
   grep-checkable, bounded.
3. **[field-contingent]** A7-6's vault-side evidence, per the ideation evidence-debt attachment
   (counts taken as reported attach to B7-8 acceptance) — vlt-core's reported state
   corroborated at its 0.10.0 upgrade: the stamped `adoption_first_instance` renders **adopted**
   on its adoption line while the shipped base stays honestly `null`, and the recorded
   promotion-era bump (relayed against the handoff path) survives as the worked instance the
   deferred check's builder will key on; producing vault: **vlt-core only** (owner-run; the
   factory cannot read it — evidence arrives as the owner's pasted upgrade report / ledger
   entry); corroboration only, never the fixes' discharge; if unread by closeout it goes to the
   watch register, not the gate.
