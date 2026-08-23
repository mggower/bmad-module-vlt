# Defect: the spec convention ships with no advocacy path — nothing in the vault's flow ever points at it

_Filed 2026-07-13 from `vlt-core` (owner-observed, during the Arc 3 acceptance-discharge run).
This is a **design gap / defect in build-15's shipped surface**, not a candidate: the convention
is well-specified and unreachable in practice._

## The observation

`_agent/specs/` in vlt-core has been empty for the five days since the 0.6.0 upgrade
(2026-07-08 17:45). Build-15's acceptance tail is dry not because the mechanism is broken but
because **nothing in the vault's normal operation ever prompts anyone to use it**. The
convention defines the spec class exhaustively — home, schema, supersession, notification,
consumer lock — and then has no moment of its own.

Traced through the shipped source, the spec class is touched by exactly two skills, and
**neither can originate one**:

- `vlt-dispatch/SKILL.md:41` — the spec zone is "governed by `{conventions}/spec.md`; `relay`
  points at these too, **never authors them**." Dispatch is the scribe for the *pointer*.
- `vlt-mint/SKILL.md:11` — the kind list (add/migrate/retire a capability, family ops, new
  partner, persona self-edit, convention edit, retirement) has **no "author a spec" kind**.
  vlt-mint's only spec contact is the **consumer lock** (`:108`), which constrains a mint that
  makes a partner consume an *already-existing* spec.

The only place the promotion trigger lives is a prose rule in the operating contract
(`vault-operating-contract.md:227`, "the third boundary" — a durable cross-partner doc that
*revises over time* has outgrown `_agent/handoffs/` and is a spec). It is a rule with no
enforcement surface, no reflex, and no skill that recites it. A partner writing its third
revision of a handoff doc will never be asked the question.

Net: **every load-bearing spec mechanism is downstream of a spec existing.** The consumer lock
fires at mint time *on an existing spec*. The push-MUST relay fires on a `version` bump *of an
existing spec*. Creation — the one step that gates all of them — is the only step with no home.

## The sharp edge: the deferral tripwire cannot fire

`spec.md`'s own frontmatter declares:

```yaml
enforcement_stage: declared
deferral_metric: "spec version bumps shipping without their relay entries"
deferral_threshold: "1 — any such bump promotes the deferred lint checks to next-mint priority"
review_after: 2026-08-17
```

The tripwire watches a failure mode **of specs in use**. In a vault with zero specs, the metric
reads clean *forever* — not because the convention is healthy, but because it was never
exercised. The declared-stage safety net measures adoption failure as success. This is the
silent-zero problem, and it is precisely why acceptance has stayed dry without anything looking
wrong: the ledger's build-15 tail and the convention's own tripwire are both waiting on an event
that nothing in the system will ever cause.

`review_after: 2026-08-17` is the only thing that would eventually surface it — as a freshness
bell about a *stale document*, not as "this convention has never been used."

## Why the general form matters beyond specs

The frontmatter@3 enforcement-declaration model (build-16) lets a convention ship `declared`
with a tripwired deferral. That model implicitly assumes **the convention's subject matter
occurs**. It has no notion of an *adoption* metric — a convention whose class-count is zero long
after ship is a distinct, undetected state from one whose rules are being followed. Any future
convention that declares a class rather than constrains an existing flow will inherit this same
hole. Worth weighing at capture: does `frontmatter.md`'s enforcement declaration need an
adoption/first-instance facet alongside its violation facet?

## Directions for the capture to weigh (not a chosen fix)

- **A reflex at the handoff write path** — the third-boundary question asked where handoffs are
  actually written, so a partner revising a handoff doc a second time is prompted to reclassify.
  Cheapest, and it sits exactly where the boundary is crossed. (`vlt-dispatch`'s relay reflex is
  the nearest existing surface — but note the "never authors them" firewall is deliberate, so the
  prompt would have to route back to the owning partner, not let dispatch write.)
- **A `vlt-lint` check** — `spec_candidate`: a doc in `_agent/handoffs/` with more than one
  revision (or more than one relay pointer against the same path) is a spec that hasn't been
  promoted. This is a *detection* answer, and it composes with the two already-deferred checks
  (`spec_schema_violation`, `spec_notification_missing`) — all three land together, and `vlt-lint`
  joins `spec.md`'s `consumers:` as that file already anticipates.
- **A vlt-mint kind (`author a spec` / `promote a handoff to a spec`)** — gives creation a home
  and a decision-log entry, at the cost of ceremony on a class the convention deliberately keeps
  unceremonious. Weakest fit on its own, since it still requires someone to *think of* invoking
  it — it answers "how" but not "who advocates."
- **The adoption-metric question above** — likely the most general fix, and the one that would
  have caught this without a human noticing.

## Grounding notes (factory-side, checked 2026-07-13 against v0.6.0 source)

- Kind list + consumer lock: `skills/vlt-mint/SKILL.md:11`, `:108`.
- Never-authors firewall: `skills/vlt-dispatch/SKILL.md:41`; relay reflex incl. the spec
  version-bump clause: `:154`.
- Third boundary (the only promotion trigger in the shipped surface):
  `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md:227`.
- Convention itself: `skills/vlt-setup/assets/governance/_meta/conventions/spec.md` — frontmatter
  (enforcement block above), *Home* (lazy dir creation), *Mint-time consumer lock*, *Enforcement*.
- Arc 3 roadmap: build-15's ledger item — upgrade-side discharged 2026-07-12, **STILL-OPEN**
  consumer-lock + live-spec-bump relay. This filing is the explanation for that tail, and it
  should be read as **blocking build-15's acceptance close**, not as a parallel nice-to-have.

## Provenance

- Vault: `vlt-core`, 0.6.0 (upgraded 2026-07-08). `_agent/specs/` empty as of 2026-07-13.
- Surfaced during the acceptance-discharge run that re-checked Arc 3's first-exercise tails; the
  owner's framing: *"the convention will be overlooked if there is no process in place to advocate
  for it — this is why verification has so far been dry."*
- Natural home: Arc 3 (it gates build-15's acceptance) or the build-17 enforcement-kit brief,
  which already trails on vault-side slice evidence and is the closest existing owner of
  "declared conventions need teeth."
