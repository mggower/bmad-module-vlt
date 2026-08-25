---
id: 'S-3'
slug: 'github-notification-semantics'
status: 'harvested'
question: 'Does a repository watch actually notify a maintainer on comments to issues they have not participated in — and is there a filer-grantable "please look" mechanism, or is the permission model owner-only?'
opened: '2026-08-24'
opened_by: 'capture — Cycle 11 (A11-2, open question 1; the capture flagged it and deferred registration to P-2)'
timebox: 'read the current GitHub notification/subscription documentation AND confirm against real repo behavior — a docs-only answer does not close this spike'
verdict: 'reshape'
sources:
  - 'https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications (extracted 2026-08-24)'
  - 'https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications (extracted 2026-08-24)'
  - 'https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels (search excerpt 2026-08-24)'
  - 'https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms (search excerpt 2026-08-24)'
  - 'gh api (authenticated as the owner, read-only): GraphQL repository.viewerSubscription + per-issue viewerSubscription; REST /repos/mggower/bmad-module-vlt (org field), /subscribers, /collaborators, /issues?state=all, /issues/8/events, /user/subscriptions; REST /repos/.../subscription and /notifications (scope-walled — observed error)'
findings: 'inline below — see "Harvest (2026-08-24)"'
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

## Ideation ruling — Cycle 11, Round 1 (2026-08-24)

**Cycle 11 runs this spike; A11-2 itself defers to Cycle 12.** Owner-adopted at
`factory/cycles/11-reachability/roadmap.md`, *Ideation rulings → Spikes*. No Cycle 11
build binds `S-3` — every build bullet in that cycle reads `spike: none` — so the spike
is not blocking any brief this cycle. It runs so that Cycle 12 briefs A11-2 over a
**harvested** spike rather than rediscovering the question at brief time, which is the
register's stated purpose: visible at adoption, blocking at brief.

`status:` stays `proposed` until a read actually begins; the ladder describes a read in
progress, so stamping `running` in advance would name a state nobody is in. Whoever picks
it up moves it, inside the timebox above.

## Harvest (2026-08-24)

**Actor:** Claude, as the owner's sanctioned delegate (the owner delegated the run
in-session 2026-08-24). **Research tool:** Tavily (`tavily_search`/`tavily_extract`) ran
— no fallback, no degradation. **Live leg:** `gh` authenticated as the owner, read-only
throughout — no subscription state changed, no comments posted, no issues modified.

### Q1 — does a repo watch notify on comments to non-participated issues?

**Docs say yes, under the right watch setting.** Watching a repository "subscrib[es] you
to updates for activity in that repository"; the watch menu offers All Activity,
Participating and @mentions, Custom (select Issues/PRs/Releases/etc.), and Ignore.
"Participating and @mentions" covers only threads you opened, commented on, were
assigned to, subscribed to manually, or were @mentioned in (the about-notifications
auto-subscribe list) — third-party activity in untouched threads reaches you only via
All Activity or Custom→Issues.

**Live-confirmed state of the real repo (`mggower/bmad-module-vlt`):**

- **The owner is NOT watching the repo.** GraphQL `repository.viewerSubscription:
  UNSUBSCRIBED`; `subscribers_count: 0`; the repo is absent from the owner's
  `/user/subscriptions` (paginated, full list). The docs' "you automatically watch
  repositories you create" default is *not in effect here* — so a watch-based trigger
  fires **nothing today** until the watch is set (`viewerCanSubscribe: true` — it is
  one flip away, and the GraphQL mutation path works under the current token).
- **Every existing tracker issue is thread-subscribed anyway.** All 11 issues are
  owner-filed (the vault files through the owner's account), and per-issue GraphQL
  `viewerSubscription: SUBSCRIBED` on every one probed — so comments on *existing* rail
  issues notify the owner regardless of the repo watch. The uncovered case is precisely
  a **third-party-opened issue** — the case the templates' trigger sentence exists for.
- **Not observed live: an actual notification firing.** Two hard blockers, both
  recorded: (a) no third-party event has ever occurred on this repo — there is nothing
  historical to observe; (b) the owner's `gh` token scopes are `gist, read:org, repo,
  workflow` — REST `/repos/.../subscription` and `/notifications` returned 404 demanding
  the `notifications` scope (observed error), and the delegate did not run
  `gh auth refresh` (that alters the owner's auth state). GraphQL reads subscription
  state fine under `repo` scope.

### Q2/Q3 — filer-grantable "please look", or owner-only?

- **Manual labels/assignment are owner-only in practice.** Docs: "Anyone with triage
  access to a repository can apply and dismiss labels." Live: the sole collaborator is
  the owner (admin); the repo has **no organization behind it** (`organization: none`) —
  no triage grants exist, so a filer can neither label nor assign.
- **Template-applied labels ARE filer-reachable.** Issue-form `labels:` keys apply
  automatically at creation regardless of the filer's permission (docs,
  syntax-for-issue-forms); all three shipped templates already carry them
  (`field-*.yml:7`, live), and label events at creation were observed on issue #8. So a
  "please look" **at filing time** can ride the template; there is **no filer label path
  on an existing thread**.
- **On an existing thread the only filer-grantable attention is an @mention** — it
  notifies regardless of watch state (participating/@mentions semantics). But a
  **repo-owned non-person mention target does not exist for this repo**: team mentions
  require an organization, and the repo is under a personal account (live). Question 2's
  team/CODEOWNERS direction is dead as the repo stands; a bot account would be a new
  moving part, not a configuration.

### Verdict: `reshape` — semantics settled, the demonstration leg remains

Both legs ran (docs + live probes), and they settle the *semantics*: watch with All
Activity or Custom→Issues is the mechanism, the permission model is owner-only except
template-applied labels and @mentions, and no non-person mention target exists. But the
spike's inherited bound — *a real observed notification (or its absence) settles it* —
is unmet: no notification was observed, and none could be (no third-party event exists;
the notifications inbox is scope-walled). The residual is no longer a read; it is an
**act-and-observe** that coincides with A11-2's own acceptance evidence ("a replacement
ships only if the notification demonstrably fires"). Re-cut question for Cycle 12's
A11-2 brief:

> With the owner's watch set to All Activity or Custom→Issues (currently UNSUBSCRIBED —
> the one precondition this harvest surfaced), does a notification observably arrive for
> an issue opened by a non-collaborator, and for their comment on a thread the owner has
> not participated in? (Needs a second account or a real third-party filer; observation
> via the inbox UI, or via API after granting the `notifications` scope.)

### Cycle 12 ideation ruling (2026-08-25) — no successor spike

Cycle 12's ideation ruled this spike's `reshape` residual **does not get a successor `S-N`**
(`factory/cycles/12-proxy-claims/roadmap.md` §Ideation rulings, Spikes). Reasons on the
record there; in short: the residual is an **act-and-observe**, not a read, so it falls
outside this register's boundary — and the harvest itself says it *"coincides with A11-2's
own acceptance evidence."* It therefore becomes **A11-2's field-contingent acceptance
check**, and `status:` stays `harvested` (which `build-brief`'s gate accepts) until A11-2's
brief cites it, at which point `build-brief` moves it to `consumed` and fills `consumed_by:`.

**A11-2 + E4 are built in Cycle 12** on the semantics this harvest settled.

### Post-harvest addendum (2026-08-24, owner act)

Minutes after this harvest, the owner flipped the repo watch to **All Activity** — the
one precondition the harvest surfaced (`viewerSubscription: UNSUBSCRIBED`) is now met.
The re-cut residual above stands unchanged, but its parenthetical precondition is
already satisfied: what remains for Cycle 12's A11-2 brief is only the observation leg
(a real third-party event demonstrably notifying).
