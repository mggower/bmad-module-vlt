# `vlt-lint` re-litigates every adjudicated governance divergence, forever — it is the only governance-touching op outside the decision-log loop

**Filed from:** module repo — a design brainstorming session (`_output/brainstorming/brainstorming-session-2026-07-26-1207.md`), not a live-vault incident.
**Found by:** ideating "does vlt need an Architect partner?" The partner question dissolved under its own constraints; this defect is what was left standing underneath it.
**Severity:** medium — no wrong output, no data loss. It produces **permanent, unresolvable noise** in a governance check and re-imposes the same human adjudication on every sweep. Its cost is that a check nobody can ever bring to zero stops being read.
**Confidence:** **high on the mechanism, no field evidence for the friction.** The mechanism is a source read (below) and is not in dispute. The claim that it *actually annoys people in a live vault* is **inferred, not observed** — no vault has reported it. Treat the friction claim as a hypothesis; the structural gap is a fact.

**Provenance note (unusual for this inbox):** this is a module-side filing, not a field filing. It is filed here only so the next `inbox-capture` picks it up. Nothing in it rests on live-vault evidence, and it should not be captured as though it does.

---

## 1. The defect

Three ops mutate or observe vault-local governance. Two of them are wired into `_agent/mint/decision-log.md`. One is not.

| Op | Writes the decision log | Reads it |
|---|---|---|
| `vlt-mint` | yes — owns the entry schema (`vlt-mint:68-84`) | yes |
| `vlt-upgrade` | yes — `:85` *"Upgrade-time rulings — write them through (never the ledger alone)"*; reconcile scan at `:77` | yes |
| **`vlt-lint`** | **no** | **no** |

`grep -n "decision-log\|decision log\|mint/" skills/vlt-lint/SKILL.md` → **0 matches.**

`vlt-lint` emits governance findings that are inherently long-lived and frequently *deliberate*:

- `convention_base_divergence` — base differs from `.baseline/` (`vlt-lint:81`)
- `baseline_missing` (same line)
- `overlay_not_append_only` / `overlay_orphan` (`vlt-lint:82`)
- capability `write_scope` mismatch and family-invariant violations (contract:205)

`:81` says of base divergence: **"Never auto-fix — a human decides overlay-vs-upstream."** The human decides. **Nowhere does that decision get recorded in a form lint can find on the next run** — so the next sweep asks again, and every sweep after that, unchanged, forever.

This is a *memory* gap, not a detection gap. Detection works correctly; that is the point. Lint is innate immunity — it recognizes the anomaly shape and has zero recall between exposures.

## 2. Why the gap exists (and why it is nobody's mistake)

The decision-log entry heading is `## [YYYY-MM-DD] <kind> — <one-line subject>` (`vlt-mint:75`). That is **human-readable prose, chronologically ordered**. It was designed to be *read as history*, never to be *queried by subject*. There is no stable key on an entry that a finding like *"base `frontmatter.md` differs from `.baseline/`"* could match against.

So even a lint that wanted to check "has this been ruled on?" has nothing to grep. The gap is a missing key, not a missing intention.

## 3. Relationship to `2026-07-17-090500-upgrade-rulings-never-reach-the-decision-log.md`

**That filing is this one's direct predecessor, and its fix is what makes this one cheap.** It established that a ruling is a *decision* (decision log), not an *upgrade action* (ledger), and its fix shipped: the `kind:` taxonomy including `upgrade-ruling`, the write-through at `vlt-upgrade:85`, the `supersedes:`/`superseded_by:` idiom at `vlt-mint:84`, and the reconcile migration at `vlt-upgrade:77`.

**This is not a re-file of it.** That filing connected `vlt-upgrade` to the log. This one observes that **the same argument applies verbatim to `vlt-lint` and was never extended to it** — a lint-time ruling on a base divergence is a decision by exactly the reasoning of §3 of that filing, and it currently has no home at all. Not the wrong home; **no home.**

## 4. Exact change to ship

**A. `skills/vlt-mint/SKILL.md:72-80` — add a machine key to the entry schema.**
A `ref:` field naming the *governed object*, so an entry is findable by subject and not only by date:

```markdown
## [YYYY-MM-DD] <kind> — <one-line subject>
- kind: mint | capability-change | convention-edit | stage-promotion | upgrade-ruling | retirement
- ref: <governed object>    # e.g. conventions/frontmatter.md | overlays/extraction.overlay.md | capabilities/families/<name>
- verdict: <…>
```

This is the load-bearing piece. Everything else is a consequence of it.

**B. `skills/vlt-lint/SKILL.md:81-82` — read before flagging.**
For each governance finding, grep the decision log for a live (non-superseded) entry whose `ref:` matches. Report exactly one of three states, per the honest-limit rule already in force (contract:250, contract:258, and lint's own build-23 honest-limit):

- **`adjudicated`** — matching entry found; **cite it** (date + kind). Not silence — a *disposed* finding, visible but settled.
- **`undisposed`** — no entry; behaves exactly as today.
- **`unclassifiable`** — a pre-`ref:` entry that cannot be keyed. The pre-schema tail is already handled honestly for `kind:` at `vlt-mint:82`; this is the same treatment for the same reason, and **must not be silently swept**.

**C. `skills/vlt-lint/SKILL.md` — write through on a lint-time ruling.**
When a human rules on a governance finding during a sweep, append an entry in the shape `vlt-mint` owns — **pointer only, no restated mechanics** (single-home; the same discipline `vlt-upgrade:85` already follows). Append-only means a *changed* disposition is a new entry carrying `supersedes:`, with the prior marked in place — the existing idiom, unmodified.

**D. Declare this build's own enforcement bell** (`vlt-mint:42` boundary classifier — it applies here, since C creates a rule others obey). Conveniently the bell *is* the build: **checker** = `vlt-lint`, **moment** = every sweep, **counter** = undisposed governance findings. No tripwired deferral needed.

## 5. Migration for existing installs

Extend the reconcile pass that already exists at `vlt-upgrade:77` rather than adding a new one. For each current overlay, base divergence, and retired capability with no `ref:`-keyed entry: emit an `undisposed` line for the human to rule **once**. Idempotent by construction — an adjudicated item is skipped on re-run, matching the decision-log relocation precedent (*"a second run finds nothing to move"*, `vlt-mint:61`).

**Without this, the feature is empty on exactly the vaults that have the problem** and will read as broken for the first year.

## 6. Open question the capture must rule on (do not let this be decided by default)

The decision-log entry schema is single-homed in **`vlt-mint`'s SKILL.md — a skill, not a convention** — so it carries **no handshake axis**. Adding `vlt-lint` as a consumer makes it a contract between three ops.

- **(a) Leave it in `vlt-mint`; lint points at it.** Cheap, no handshake, matches the relay-when-done precedent (contract:232 — named at every site, mechanics in one home). Risk: three consumers depending on an unversioned format.
- **(b) Promote to `{conventions}/decision-log.md`** with `version:`/`consumers:`, re-acking consumers per build-4. Correct by handshake doctrine, **and** it gives a home to the carry-forward debt already tracked at `vlt-mint:84` — *"the governance-wide convergence of the three homes (wiki + spec + decision log under one supersession convention)."*

**Owner's stated instinct (2026-07-26): (b), promote from the start** — noting that discharging the `vlt-mint:84` debt makes (b) cheaper than it first appears. **Not yet a ruling**; deliberately left open for arc ideation. This choice determines the build's size.

## 7. Explicitly out of scope

Recorded so they are not silently absorbed:

- **No new partner.** An "Architect"/overseer was examined and declined: an unlaned overseer is illegal under ownership-equals-location (contract:203) and the never-speak-in-another's-voice rule (contract:226); `_meta/` is module-written and lint-guarded, so it cannot be a partner's lane; and an honestly-written persona collides with the Librarian's.
- **No new record.** The rationale home (`_agent/mint/decision-log.md`) and the state home (`_agent/upgrade-ledger.md`) both exist and are correctly partitioned. Adding a third violates single-home.
- **No capability family.** *"One-offs need no family"* (contract:205).
- **No inference of rationale.** Lint may **cite** a recorded ruling or **admit absence**. It must never reconstruct *why* a divergence happened from a diff — that is precisely the failure mode the 2026-07-17 filing documented in its §2, where a mint confidently fabricated a root cause and acted on it.

## 8. Carry-forwards surfaced by the same session (not part of this filing's fix)

- **A readiness signal for accumulated governance history** — thresholds (N upgrades, M overlays, K retirements) that file a `capability-gap` to the backlog. Revisit only if the above proves the need is real.
- **Separation of powers on the bus** — the Librarian owns `vlt-dispatch` *and* is its largest destination, so it is the one partner that can route work to itself. Raised, unresolved, deliberately untouched here.
