---
title: 'Lifecycle-skills audit (2026-07-17) — remaining action items'
status: 'OPEN — map+routing done 2026-07-17; Items 1 (rubric upgrade) and 3 (config paths, with corrected reality: _bmad/config.toml) executed 2026-07-17 later session; Items 2, 5, 6 executed 2026-07-17 third session (lifecycle-status + ideation-scaffold built, status-line capped per ruling (b)); Items 4 (owner/vault-side) and 7 (watch) pending'
module_code: 'vlt'
created: '2026-07-17'
context: >
  Audit of the five factory lifecycle skills (inbox-capture, build-brief, vlt-release,
  acceptance-discharge, arc-closeout) against the handoff-2026-07-12 briefs and the live
  arc-3 record. Three owner-reported pains confirmed: no flow documentation, no next-step
  routing, and acceptance-discharge dead-ends. This doc holds everything the audit found
  that was NOT executed on 2026-07-17. These are factory-process items — they do not ride
  the module release lifecycle and need no inbox filing; work them directly.
---

# Lifecycle-skills audit — remaining action items

## Already done (2026-07-17, for the record)

- **Lifecycle map created:** `.claude/skills/vlt-lifecycle.md` — single home for the
  loop-with-owners table, the observable-state → position → next-move table, blocked-outcome
  routes, and the routing contract.
- **Routing contract wired into all five skills:** each SKILL.md carries a Lifecycle
  position pointer; each headless JSON gained a `"next"` field; each report/handoff section
  now ends with a mandatory **Next lifecycle move** (inbox-capture's stale
  `bmad-module-builder` pointer replaced with ideation → `build-brief`; build-brief's
  handoff now names the builder session and its exit obligations; acceptance-discharge's
  Report gained outcome-derived routing rules; arc-closeout routes to `inbox-capture` or
  the gate-specific route out; vlt-release stage 8 names the owner's upgrade as the move).
- **`.claude/skills/vlt-release/.decision-log.md` removed** (standing-rule violation);
  content relocated to `skills/reports/handoff-2026-07-12/briefs/build-record-vlt-release.md`
  (it held real owner rulings — moved, not destroyed).

---

## Item 1 — acceptance-discharge evidence-rubric upgrade (HIGHEST value) — ✅ DONE 2026-07-17

All four sub-changes landed: 1a BLOCKED (unreachable) as a fourth verdict (trigger required
on STILL-OPEN annotations; no trigger → BLOCKED, routes like FAILED with filing); 1b
pass-through tripwire (event-of-the-kind occurred unfired, or second unfired run → mandatory
reachability re-exam, re-annotating STILL-OPEN forbidden); 1c subject-match bullet on
DISCHARGED (substitution stated + owner-ruled; headless leaves open); 1d Discovery
enumerates all CLAUDE.local.md vaults and accepts upgrade-ledger entries, relayed inbox
filings, and post-upgrade vault activity as legal evidence — run ends only when no source
of any kind exists. SKILL.md stage table + headless JSON gained `blocked`; the lifecycle
map's "rubric doesn't yet name this" caveat removed. Acceptance (the arc-3 ledger re-run
under the new rubric) rides the next `acceptance-discharge` invocation — it will also
surface the owner's pending build-15 refutation ruling.

**File:** `.claude/skills/acceptance-discharge/references/evidence-rubric.md` (+ Discovery
in its SKILL.md for 1d). Four sub-changes; all are already documented as live process
defects in the arc-3 roadmap's status line (capture run 2, 2026-07-17).

**1a. Add a fourth verdict: BLOCKED (unreachable).** Today's taxonomy is
DISCHARGED / STILL-OPEN / FAILED, and only FAILED routes anywhere. STILL-OPEN assumes the
discharging event will eventually occur. The build-15 consumer-lock tail proved the fourth
class: an event no shipped surface can produce. Rubric change: a STILL-OPEN annotation must
record the discharging event AND its trigger (owner action / vault-side first use / dated
clock); if no trigger exists, the grade is BLOCKED (unreachable) and it routes like FAILED —
draft an inbox filing, feed capture. (The lifecycle map already states this rule prose-side
with a "rubric doesn't yet name this" caveat — remove that caveat when this lands.)

**1b. Add a staleness/pass-through tripwire on tails.** The observable that proved
build-15's tail unreachable was a pass-through event: the 2026-07-16 Chess Coach mint ran
the exact flow and never touched the convention ("its tripwire reads clean forever at zero
specs"). Rubric change: when an event *of the discharging kind* has occurred without firing
the check, or a tail survives its second discharge run unfired, mandatorily re-examine
reachability rather than re-annotating STILL-OPEN.

**1c. Subject-match on DISCHARGED.** Capture run 2 finding (2): build-11's acceptance
check NAMED dog-trainer + health-coach but was discharged against chess-coach + sayari's
Navigator — acceptance passed on substitutes, silently, because DISCHARGED requires an
evidence citation but not that the evidence's subject match the check's named subject.
Rubric change: if the evidence's subject differs from the check's named subject, the
substitution must be stated explicitly in the discharge note and owner-ruled (headless:
leave open, surface it). The roadmap notes this defect "plausibly explains build-15's dry
spec tail identically" — reach beyond vlt-track.

**1d. Widen the evidence model to match practice.** Discovery assumes ONE vault (from
CLAUDE.local.md) and one upgrade-ledger entry, and stops if no entry exists. Actual arc-3
discharge spanned two vaults (vlt-core ledger + vlt-sayari evidence *via relayed inbox
filing*, `inbox/2026-07-12-114940-…`), and the 07-17 second pass ran with no new upgrade —
"vault activity is the evidence." Changes: Discovery enumerates ALL vaults CLAUDE.local.md
names; legal evidence sources include upgrade-ledger entries, relayed evidence filings in
`inbox/`, and post-upgrade vault activity; "no upgrade yet" only ends the run when no
evidence source of any kind exists.

**Acceptance:** re-run of the arc-3 ledger under the new rubric reproduces the 07-17
verdicts, and the build-15 tail comes out BLOCKED-with-filing (or DISCHARGED per the
owner's pending ruling on the refutation) rather than hand-edited prose.

## Item 2 — ideation rulings scaffold — ✅ DONE 2026-07-17 (third session)

Built as `.claude/skills/ideation-scaffold/` (skill, not a build-brief reference — the
routing contract wanted it invokable and blocked-routable on its own). It appends a dated
empty rulings section to the open roadmap matching the 2026-07-06 section's shape (the
parse target build-brief's Discovery/Readiness already understand), seeds it with the
questions capture flagged (never answers), and carries the clerk-not-advisor caution in
its Overview. Lifecycle map updated: step-3 skill cell, the Awaiting-ideation next-move
cell, and build-brief's missing-rulings blocked route all name it. Headless supported;
blocked when nothing is unideated or an unfilled skeleton already exists. First live
exercise: the pending arc-3 run-2 ideation.

Original item, for the record:

**Gap:** step 3 (Ideate) is deliberately owner-led, but there is no artifact shape or
recording scaffold — and `build-brief` hard-gates on rulings existing, so the one
unformalized step gatekeeps the formalized one. When build-brief returns
`blocked: ideation missing`, nothing tells the owner what a sufficient rulings record
looks like. The handoff (§1.2.5) prescribed exactly this: scaffold the *recording*, never
the deciding.

**Shape (suggested):** a small `ideation-scaffold` skill (or a reference inside
build-brief) that, given the open roadmap, produces the empty rulings skeleton for the
owner to fill in session: grouping/order table naming builds; decide-once cross-filing
rulings; spike obligations with SPIKE OPEN/CLOSED status; "questions deliberately left to
brief time"; evidence-debt dispositions. It must match what build-brief's Readiness gate
and Discovery already parse (SKILL.md Discovery bullets + Readiness gate — build these two
from the same spec). Routing contract applies: its next move is `brief build N`.

**Caution:** do not automate the decisions; owner steering is a feature (handoff ruling).

## Item 3 — config-path fixes across all five skills — ✅ DONE 2026-07-17 (audit's "reality" corrected)

**Correction:** actual reality is `_bmad/config.toml` + `_bmad/config.user.toml` (verified
on disk; `_bmad/_config/` holds installer manifests, not config). So arc-closeout and
build-brief were already right — build-brief's legacy `_bmad/bmb/config.yaml` fallback also
points at a real file and was kept. Fixed the three `.yaml` skills (acceptance-discharge,
inbox-capture, vlt-release) to the same `.toml` string; all five now agree.

Original (mis-grounded) finding, for the record:

- `acceptance-discharge/SKILL.md` — says `_bmad/config.yaml` / `config.user.yaml`
- `inbox-capture/SKILL.md` — says `_bmad/config.yaml` / `config.user.yaml`
- `vlt-release/SKILL.md` — says `_bmad/config.yaml` / `config.user.yaml`
- `arc-closeout/SKILL.md` — says `_bmad/config.toml` / `config.user.toml` (right format,
  wrong directory)
- `build-brief/SKILL.md` — says `_bmad/config.toml` + legacy `_bmad/bmb/config.yaml`
  (verify whether the legacy path is real before keeping it)

Harmless today (each needs only `user_name`/`communication_language`) but it's five skills
diverging on one fact — fix all five to the same string in one pass.

## Item 4 — second-vault inbox rail: mint it (or re-rule)

`skills/reports/handoff-2026-07-12/briefs/brief-vlt-core-inbox-rail.md` is BRIEFED,
un-executed. Sayari's module signal is still relayed manually "on the vault's behalf."
The rail is the stated prerequisite for frontmatter@4's acceptance landing on the
work-machine vault (handoff §2.3.3). This is a **vault-side mint** (a vlt-core capability
via `vlt-mint`), not factory source — execute in the vault per the brief, or explicitly
re-rule that manual relay is the standing convention and retire the brief.

## Item 5 — roadmap status-line state store — ✅ DONE 2026-07-17 (third session, owner ruled (b))

Owner ruled option (b): cap `status:` to ~3 sentences, history lives in the ledger.
Applied to the arc-3 roadmap: the ~4,700-char line replaced with a 3-sentence summary
after verifying every claim was already homed per-item in the ledger annotations or the
Status & next step bullets (deduplicated, nothing destroyed — restructure recorded as a
dated bullet in the roadmap's Status section, which also states the standing shape for
future status lines). Option (a) rejected as unneeded: `lifecycle-status` derives from
disk observables and never parses the status line.

Original item, for the record:

The arc-3 roadmap's frontmatter `status:` has become the de-facto lifecycle state store —
a ~1,500-word single YAML line (`inbox-evolution-arc3-roadmap.md:3`). This is the arc-3
disease in the factory's own state: state living in prose, so nothing can count, trigger,
or trip. The lifecycle map's "Where am I?" table now derives position from disk, which
removes the *navigation* burden — but the status line still accumulates unboundedly.

**Options to rule on:** (a) a structured status block (keyed frontmatter fields per build:
`acceptance:` map with per-item state) that skills read/write mechanically; (b) keep prose
but cap it — move discharge history into the ledger section (where the per-item annotations
already live) and keep `status:` to ~3 lines; (c) accept as-is. Recommendation: (b) is
cheap and honest; (a) only if a `lifecycle-status` derive skill (below) wants to parse it.

## Item 6 — `lifecycle-status` derive skill — ✅ DONE 2026-07-17 (third session; defer-note overridden by owner invocation)

Built as `.claude/skills/lifecycle-status/`. Read-only with an explicit zero-writes
guarantee in its Overview (design rationale stated so no future session makes it fix what
it finds). Load-bearing choice: it never restates the map's observable-state table — it
reads `vlt-lifecycle.md` fresh each run, so map edits propagate with no skill change.
Evaluates every row (positions coexist; first-match is per-track ordering), overlays
blocked states with the map's route out, ends with Next lifecycle move; headless JSON
carries `positions[]` + `flags[]` + `next`. The map's "Where am I?" intro now points at it.

Original item, for the record:

A tiny read-only skill that walks the lifecycle map's observable-state table against disk
and reports every active position + next move (the map notes positions can coexist —
acceptance track and capture track run independently). Pure derive-first dogfooding; zero
writes. Defer until the map's table proves itself by hand first — if the by-hand table is
sufficient, this never needs to exist (defer-until-it-bites).

## Item 7 (watch, not work) — builder-session obligations have no bell

The build step's exit obligations (status → BUILT with numbered deviations, delete
`.decision-log.md`, one commit) are now *stated* at the build-brief handoff and in the
lifecycle map, but still only *checked* at vlt-release pre-flight — a late bell. If a
builder session misses one again, the fix is a small "build intake/exit" checklist skill
or a pre-flight-style script run at build end. Don't build it before it bites again.

---

**Suggested execution order:** 1 → 3 (trivial, same files) → 2 → 4 (owner/vault-side) →
5 (ruling) → 6/7 (deferred). Item 1 first: it is the live pain, and the owner's pending
ruling on the build-15 refutation (arc-3 roadmap, capture run 2, reversal #1) should be
made with the new rubric in hand.
