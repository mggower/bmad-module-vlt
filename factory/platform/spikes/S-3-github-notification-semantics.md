---
id: 'S-3'
slug: 'github-notification-semantics'
status: 'proposed'
question: 'Does a repository watch actually notify a maintainer on comments to issues they have not participated in — and is there a filer-grantable "please look" mechanism, or is the permission model owner-only?'
opened: '2026-08-24'
opened_by: 'capture — Cycle 11 (A11-2, open question 1; the capture flagged it and deferred registration to P-2)'
timebox: 'read the current GitHub notification/subscription documentation AND confirm against real repo behavior — a docs-only answer does not close this spike'
verdict: ''
sources: []
findings: ''
consumed_by: []
legacy_id: ''
---

# S-3 — GitHub notification semantics for the amendment trigger

**Opened by the register's first act 2026-08-24** (platform P-2), materializing the flag
Cycle 11's capture wrote against A11-2: *"an external unknown: per lifecycle step 3 this
gets a spike before the brief (verify against GitHub's current notification semantics,
not memory; register it per P-2's spike register when that lands)."* It has landed; this
is that registration. **Nothing about A11-2's scope is ruled here** — whether a build
binds this spike is ideation's call.

## The question, in the form a real source must answer

A11-2 wants to replace a personal `@`-handle — shipped literally in all three issue
templates at `.github/ISSUE_TEMPLATE/{field-pattern,field-candidate,field-defect}.yml:17`
— with a trigger that names nobody. Two candidate mechanisms, and the choice turns
entirely on behavior nobody in the factory has verified:

1. **Repo-level watch/subscription.** Does watching a repository actually deliver a
   notification when a *third party* comments on an issue the maintainer never opened,
   commented on, or was assigned? Under which watch setting ("All Activity" vs
   "Participating and @mentions" vs custom)? This is the load-bearing question: if the
   answer is no, the whole watch-based direction dies.
2. **A repo-owned mention target.** Is there a mention target that is not a person — a
   team, a bot account, a `CODEOWNERS`-derived route — usable on a public repo with no
   organization behind it?
3. **Filer-grantable attention.** Can a filer (not the owner) apply a label or otherwise
   raise a flag, or is the permission model owner-only? If owner-only, the amendment
   admission path stays owner-gated by construction, which is the current posture anyway.

## The bound this spike inherits

A11-2 carries a preserved constraint that also fixes this spike's standard of proof:
**the trigger must remain real, not prose — a replacement ships only if the notification
demonstrably fires.** So this spike is not closed by reading documentation. Documentation
sets the expectation; a real observed notification (or its absence) settles it. A read
that only reaches the docs reports `verdict: reshape` with what it learned, not
`proceed`.

## Why it is `proposed` and not `running`

The register's rule: visible at adoption, blocking at brief. This entry exists so Cycle
11's ideation sees the question while it is still shaping scope — not so that anyone runs
it before the owner has ruled whether a build depends on it.
