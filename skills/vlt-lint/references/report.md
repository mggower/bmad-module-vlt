# vlt-lint — reference: Step 5 — the structured report (+ Tips)

Read on reaching Step 5. The fenced report block is strict YAML as a whole — emitted fenced in-session and **persisted as the plain `.yaml` file** (`vlt-lint` Step 6) — same content, no fence; keep it parsing whole in both homes.

## Step 5: Emit the structured report

Produce a parseable report (stable keys, so a dashboard can consume it), opening with the mode/scope line. Use a fenced block:

```yaml
mode: scoped            # scoped | full
scope_since: 2026-04-19 15:00    # or: full
files_checked: 10       # pages an agent/this run actually SCANNED (not merely listed/globbed)
files_cached: 0         # pages whose extracted facts were reused under an unchanged key — adjudicated this run, NOT scanned (see files_checked); full mode via the workflow only
files_listed: 10        # pages discovered in scope (full mode via the workflow reports both — files_checked + files_cached < files_listed signals a coverage cap)
fix_now:
  orphans: [<page>, ...]
  missing_targets: [<page → target>, ...]
  index_drift: [<what was fixed>, ...]
  frontmatter_drift: [<page: summary missing/over-length | topic string→list | category typo repointed>, ...]
  unmarked_supersessions_fixed: [<page: claim>, ...]
  sources_vs_prose_mismatches: [<page: frontmatter sources vs prose Sources diverge>, ...]
flag_for_human:
  category_no_match: [<page: category 'X' matches no index H2 — needs a category decision>, ...]
  convention_drift: [<convention@version → consumer acks @N (stale) | <consumer> unacknowledged | <consumer> dangling/not-installed>, ...]
  enforcement_missing: [<convention | overlay §section: no valid enforcement frontmatter>, ...]
  deferral_invalid: [<convention | overlay §section: deferral missing metric | threshold | review_after>, ...]
  deferral_expired: [<convention | overlay §section: deferral past review_after YYYY-MM-DD>, ...]
  declared_untripwired: [<convention | overlay §section: stage declared, no complete deferral>, ...]
  counter_unknown_metric: [<convention | overlay §section: enforcement_counter names no canonical or registry-declared metric id>, ...]
  overlay_rule_undeclared: [<overlay §section: rule-shaped section, no per-section declaration>, ...]
  convention_meta_missing: [<convention: missing version and/or consumers keys>, ...]
  para_missing_attestation: [<para-file: vault type + author agent|hybrid, no attestation — excludes the operational-record class; informational where created predates convention adoption>, ...]
  unattested_write: [<page (created YYYY-MM-DD) — informational where created predates convention adoption>, ...]
  attestation_stale: [<page: last_updated > verified_at — quiet tier-1 re-run>, ...]
  attestation_census: {pages_total: N, fresh: N, stale: N, unattested_pre_adoption: N}   # full mode — the denominated wiki-wide census (checks.md, Attestation findings); never omitted in full mode (a zero-page wiki renders the denominated empty form {pages_total: 0, ...}); informational — nothing owed per se
  para_status_unknown: [<para-file: status 'X' outside the <type> enum — informational where created predates convention adoption>, ...]
  para_type_unknown: [<para-file: type 'X' outside the recognized set — informational where created predates convention adoption>, ...]
  para_author_unknown: [<para-file: author 'X' outside human|agent|hybrid — informational where created predates convention adoption>, ...]
  para_writer_unauthorized: [<para-file: writer 'X' not in nearest declaring ancestor's writers: [...] — informational where created predates convention adoption>, ...]
  review_due: [<page — review_after YYYY-MM-DD past>, ...]
  research_zone: <M notes scanned; N carry revisit_after:>   # candidacy-pass denominator — a bare zero below is not health
  linkage_ripe: [<research-note — no absorption linkage: cited ∪ inbound wikilink ∪ shared sources>, ...]
  revisit_due: [<research-note — revisit_after YYYY-MM-DD past>, ...]
  governance_memory: <G governance findings checked against the log; A adjudicated, U undisposed; X log entries unclassifiable (no ref key)>   # read-before-flag denominator — the pre-key tail is surfaced, never silently swept
  convention_base_divergence: [<convention: base differs from .baseline — lift to overlay or upstream | baseline_missing | annotated (adjudicated YYYY-MM-DD <kind>) where a live log entry disposes it>, ...]
  local_conventions: <N local convention(s): <names>>   # sanctioned local conventions (no baseline + live mint entry) — an inventory line, not a finding; zero renders as the denominated zero
  overlay_issues: [<overlay: duplicates base heading 'X' (not append-only) | overlay_orphan (no base convention)>, ...]
  capability_issues: [<partner/slug: lane_violation (light cap writes a shared lane) | scope_mismatch (write_scope ≠ actual writes) | weight_mismatch | skill_missing (dangling heavy pointer)>, ...]
  family_issues: [<family: invariant_violation (instance breaches X) | instance_missing (listed instance has no capability)>, ...]
  dispatch_profile_invalid: [<_agent/dispatch-profile.md: <failing line — duplicate slug | no/multiple (default) | capture stream resolves to no directory>>, ...]   # absent file = no findings (single-principal default)
  personalized_extraction_issues: [<artifact: method_not_in_sources (general claim not traced to wiki sources:) | method_in_personalization (personalization_sources carries method, not state) | method_in_grounding (grounding: entry — or a body claim resting only on one — carries method, not evidence/relations)>, ...]
  stale: [<page — reason>, ...]
  contradiction_scan: <P pages compared; D documented, U carrying no disposition; S surfaced-but-declined this run>   # denominator + the stated bound — a bare zero below is not health
  contradictions: [<page-a vs page-b: claim>, ...]                    # surfaced this run, no callout yet
  contradictions_open: [<page-a vs page-b: claim>, ...]               # documented, disposition open — documentation IS the resolution
  contradictions_deferred: [<page-a vs page-b: claim — closes when X | backlog item>, ...]   # documented, disposition adjudicable — NOT health
  contradictions_undispositioned: [<page-a vs page-b: claim>, ...]    # documented before the disposition convention, or without one — unclassifiable, stated as such
  entity_scan: <P pages compared in Q clusters + R callout-seeded pairs; single-mention substitutions are invisible by construction; unmarked split pairs are not compared>   # denominator + blind spot — a bare zero below is not health
  entity_collisions: [<page-a vs page-b: <name> — <attribute A> vs <attribute B> (suspected source substitution | callout-seeded)>, ...]
  authority_scan: <S specs compared; T binding a partner other than their owner>   # denominator + blind spot: out-of-authority claims outside {specs} are invisible by construction — a bare zero below is not health
  consult_missing: [<spec — binds <consumer-slug>, no consult record>, ...]
  consult_retroactive: [<spec — consult for <consumer-slug> dated YYYY-MM-DD, after created YYYY-MM-DD>, ...]
  spec_candidate: [<handoff-doc — signal re-relay (2 same-key handoff entries) | dated revision record; new | signal changed (item updated); owner <partner>; M prior declines honored>, ...]   # loud entries only: new candidates + standing candidates whose signal changed (Step 2's repeat partition)
  spec_candidate_standing: <N standing candidate(s) — previously filed, open backlog item, signal unchanged: <paths>>   # the quiet line — derived from {backlog} open items, never prior reports; renders (denominated zero included) whenever _agent/handoffs/ is non-empty; no line when it is empty
  thin_pages: [<page>, ...]
  malformed_frontmatter: [<page: what is wrong>, ...]   # frontmatter absent/unparseable or a page-schema break the field-level frontmatter_drift does not cover; an attestation-only complaint (→ unattested_write) and a claimed-missing OPTIONAL field (→ not a finding) are excluded at the reduce, never listed here
opportunities:
  high_value_gaps: unmeasured     # no producer exists (the fan-out computes no gap candidates) — render the literal, never [] and never omit: an empty list would claim "measured, none found"
  near_duplicates: [<page-a + page-b (signal)>, ...]
  source_gaps: [<topic — source type that would help>, ...]
fixes_applied: [<summary>, ...]
backlog_filed: [<merge item>, ...]
rulings_recorded: [<finding — ruling appended YYYY-MM-DD>, ...]   # write-through events (Step 3) — empty when no lint-time ruling was recorded
coverage_caps: [<what was NOT exhaustively checked — budget stop / near-dup cap / cluster cap>, ...]   # full-mode workflow only; empty when the sweep was exhaustive
cost_accounting: {phases: [...], ...}   # full mode via the workflow — verbatim from the workflow return; inline/scoped runs render the literal: not instrumented (inline run)
churn_since_last_full: <N of T pages changed since YYYY-MM-DD (instrument: <name>) | unmeasured (no prior full report) | not measured (scoped run)>
lint_cache: <scanned N / cached M of T pages (fingerprint <fp>, written YYYY-MM-DD, rejected R of P records read) | cold (<reason>, rejected R of P records read) | not used (scoped run)>   # facts reused under an unchanged page digest + ruleset fingerprint — never verdicts; additive to coverage_caps, never a replacement
```

**`files_checked` counting rule (Gap B):** count a page as *checked* only if it was actually read/scanned this run — distinct from `files_listed` (discovered in scope). A page whose extracted facts were **reused from the findings cache** was not scanned this run and is **not** counted as checked — it is counted in `files_cached`, and `files_checked + files_cached < files_listed` is still a coverage cap, exactly as `files_checked < files_listed` was. When the fan-out workflow hits a budget or coverage cap, `coverage_caps` names what was skipped — **surface that; never report a capped sweep as exhaustive.** For a large full-mode sweep, you may additionally offer an HTML rendering if the host has a renderer — otherwise skip it.

**Contradiction reporting.** The three documented slots are **derived from each callout's recorded `Disposition:`**, never from the existence of a callout — a callout with no disposition is `undispositioned`, never defaulted into either real bucket. `contradiction_scan:` carries the denominator and the run's stated bound: how many contradictions were surfaced and deliberately **not** documented (`S`), so a skipped triage is visible rather than silent. **You compose that line yourself** even in full mode — `P` and `S` are this run's own facts (what was compared, what you declined to document) and the fan-out workflow is read-only, so it fills the three documented slots but never the scan line. Per the operating contract's honest-reporting rule — read it there; this line does not restate it.

**Entity-collision reporting.** A conflict reported in `entity_collisions:` is **not** also reported in `contradictions:` — one finding, one slot (the precedence rule stated in Step 2). `entity_scan:` carries the population actually compared — pages, clusters, and callout-seeded pairs in full mode (from the workflow's returned `entity_scan_facts` and any pair-cap it surfaces) — **and** names the blind spot beside it: a substitution that entered once and was never contradicted cannot be seen by a cross-page check, and a cluster-bounded sweep did not compare every pair — callout-marked pairs are the stated exception, compared by the seeded second pass; an unmarked split pair remains invisible. **You compose that line yourself** in both modes, as with `contradiction_scan:`. Per the operating contract's honest-reporting rule — read it there.

**Consult-precondition reporting.** `authority_scan:` carries the population the check actually ran against — how many `{specs}` artifacts were compared, and how many of those bind a partner other than their `owner` — **and** names the blind spot beside it: an out-of-authority claim made anywhere other than a spec has no authority axis to derive from and cannot be seen by this check. A vault with no cross-binding spec renders as `authority_scan: <S specs compared; 0 binding another partner>`, **never as silence**. **You compose that line yourself** — this is a governance check, so it is this SKILL's own fact in both modes (the fan-out workflow sweeps `{wiki}` only and never reads `{specs}` or the dispatch record). Per the operating contract's honest-reporting rule — read it there.

**Findings-cache reporting.** `lint_cache:` states what the run reused and what it was reused *under*: the two counts against the listed total, and the fingerprint the records were adjudicated under. It is **additive** — `coverage_caps:` keeps every cap it would have carried and nothing is removed to make a cached run look cleaner. **A cold run says so and says why** (no prior cache; fingerprint changed; sidecar unreadable), so the first full run after an upgrade is a stated cold run rather than a discovered one. Scoped runs render the literal `not used (scoped run)`. Compose the line from the **workflow's returned counts only**, never from what was passed in. `rejected R of P records read` carries the workflow's returned `cache_rejected` against its `cache_records_read`: how many sidecar records the workflow's reader filter discarded as schema-mismatched, against how many it read. It is **rendered on both the warm and the cold branch and is never omitted, including zero** — an absent field reads as *not measured* — and **`rejected 0` on a cold run means no records were read, not that the cache is healthy**; the pair to look for is a warm run's `cached M > 0` with `rejected 0`. Per the operating contract's honest-reporting rule — read it there.

**Governance-memory reporting.** `governance_memory:` carries the read-before-flag's denominator — how many long-lived governance findings were checked against the decision log, how many came back `adjudicated` vs `undisposed`, and how many log entries were `unclassifiable` (no `ref:` key, or pre-schema) — so the pre-key tail is surfaced, never silently swept. `rulings_recorded:` names each write-through this run performed. **You compose both lines yourself** in both modes — the decision log is a vault-zone read the fan-out workflow never performs (it sweeps `{wiki}` only), so these are this SKILL's own facts. Per the operating contract's honest-reporting rule — read it there.

## Tips

- **An *open* contradiction is a feature, not a bug** — a well-documented disagreement between two credible sources beats false certainty. Say so loudly, don't quietly pick one. **An *adjudicable* one is a deferral wearing that costume:** one side is wrong or stale, a bounded act would close it, and it belongs in the backlog with what would close it. The disposition on the callout is what tells them apart — never the fact that someone wrote a callout.
- **Suggest sources, not just fixes** — the best lint output is often a list of specific source types that would fill a gap.
- **Don't over-clean** — fix the clear-cut structural issues, flag the content decisions, and leave the judgment calls to the human.
- **Trust scoped mode** — full-vault linting gets expensive as the wiki grows; trust the scoping unless there's a reason to distrust `{log}`.
