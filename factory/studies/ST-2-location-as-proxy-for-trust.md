---
id: 'ST-2'
slug: 'location-as-proxy-for-trust'
title: 'PARA location is used as a proxy for trust, and the evolution loop can process defects but not obsolescence'
status: 'standing'
opened: '2026-08-25'
opened_by: 'owner problem-solving session'
session: '_output/problem-solution-2026-08-25.md (gitignored — provenance only)'
causes:
  - 'RC1 (structural): PARA membership is made to carry a trust claim that the trust: field already carries. Correct when written; redundant since Cycle 11 build-6 extended the para_* nets across the whole PARA population; and already broken in shipped code, since extraction.md:60 justifies the trust: reviewed entry level as a human-initiated curation step while vlt-track runs it on a cadence loop and vlt-query runs headless.'
  - 'RC2 (process): every input to the loop is a filing, and a filing describes something that broke. Nothing can express "this protection is now redundant." Eleven cycles retired zero rules while adding many. RC2 is why RC1 survived four corrections.'
cited_by:
  - 'factory/inbox/2026-08-25-111322-para-location-is-used-as-a-proxy-for-trust.md'
  - 'factory/platform/roadmap.md §P-15 (the retirement rail — the RC2 fix, built 2026-08-25)'
  - 'factory/platform/roadmap.md §P-14 (the study register — this register exists because of this study'"'"'s §Why this study is here)'
superseded_by: ''
---

# ST-2 — Location is used as a proxy for trust

**Written 2026-08-25** from the owner problem-solving session of the same day, back-filled into
the register at its creation (platform P-14). Grounded against shipped source at v0.15.0.

## Why this study is here

`ST-1` diagnosed this ground correctly on 2026-08-20, lived in gitignored `_output/`, and was
distilled into a filing that carried the symptom. Five days and two releases later the owner
re-derived the same answer — per-domain declared posture — **without reference to having
proposed it before.** That convergence is good evidence the answer is right and equally good
evidence that the loop dropped it the first time. The study register was stood up so this does
not happen a third time.

## The presenting symptom, and the tell

`vlt-brief`'s scheduled digest has nowhere legal to land. Tracker **#11** has been open across
three cycles with zero comments. Underneath it, PARA in the primary field vault is empty and
everything lives in `_agent/`, "deeply nested, unreachable, unorganized" in the owner's words.

**The tell is that two field vaults fail the same clause in opposite directions.** `app-vault`
falsified frontmatter to pass the door (57 PARA files, **0 of 56 attested**); `{field-vault}`
abandoned the layer entirely. Falsification looked like a discipline problem; abandonment looked
like a gap problem; each was filed and fixed on its own terms, and neither reading reached the
shared mechanism. **A rule that produces both pathologies is mis-specified, not
under-enforced.**

## The counter-example that dissolves the premise

`{wiki}` sits **inside** the browsable layer, is written **only** by an agent, contains
documents that are honestly agent-authored — and produces **zero friction**. It is protected by
its own **discipline** (single writer, convention set, attestation, an index), not by a
prohibition on agent writes.

The problem is absent exactly where a zone has authoring discipline, and present where the
module substituted a location rule for one. **The module already ships a working proof of the
model it refuses to apply to PARA.**

## Root cause 1 (structural) — location is a proxy for trust

PARA membership is made to carry a **trust claim** that the `trust:` field already carries
explicitly. When the contract was authored the proxy was **necessary**: the honest fields had no
enforcement, so location was the only protection available. It is now false and redundant —
`trust:` is a real field, `para_missing_attestation` / `para_author_unknown` /
`para_status_unknown` are real nets, and **Cycle 11's build-6 extended them across the entire
PARA population** with `{wiki}` excluded by name.

The proxy is also **provably broken in shipped code**: `extraction.md:60` justifies the
`trust: reviewed` entry level as *"the act of extraction is a human-initiated curation step"* —
yet `vlt-track` runs extraction on a cadence loop and `vlt-query` runs headless
(`vlt-query/SKILL.md:10`). The human-initiation premise the whole location rule rests on is
already fiction.

**Consequence:** honest agents are excluded from human territory by a rule whose stated purpose
(*authorship-honesty*) their honesty already satisfies. Falsification and abandonment are the
only two available responses.

### The goal mismatch — the highest-leverage statement available

The contract's **stated** goal for Layer 3 is *authorship-honesty*. Its **structural** goal —
revealed by what the rules actually do — is *keep agents out of human territory*. Those are
different goals, and the structure serves the second while the prose claims the first. Every
symptom in this session is the gap between them.

### The friction gradient runs backwards

Operational sludge flows into `_agent/` unimpeded; the polished digest addressed to a person is
the illegal artifact. **The module is most restrictive toward exactly the content that most
serves its user** — which is the mechanism behind both "PARA folders remain empty" and "content
is deeply nested and unreachable."

## Root cause 2 (process) — the loop can process defects, not obsolescence

The lifecycle is driven by **field filings**: defects, patterns, candidates. Every input
describes something that *broke*. There is no input class for *"a protection has been superseded
by a better one"* — because obsolescence produces no field pain, only unnecessary friction that
reads as normal governance.

The roundtable's own charter shows the asymmetry precisely: it hunts **rules ahead of
mechanisms** and has no counterpart beat for **mechanisms that have obsoleted their rules**. One
direction is checked; the reverse is not.

**Consequence:** protections accumulate and never retire. Five passes produced four exceptions
and zero categories, and the one build that *should* have triggered the retirement of the
location rule — build-6, shipping the honesty nets across PARA — instead reinforced it. The
nets landed **beside** the prohibition rather than **in place of** it.

**RC2 is why RC1 survived four attempts to fix it.**

## Contributing factors

1. **The ≥2-wiki-page gate is prose-only ceremony** — present at `vlt-extract/SKILL.md:38` and
   `vlt-agent-creative/SKILL.md:37`, absent from `extraction.md` and every lint check. The
   most-cited authoring bottleneck in the module is unenforced and self-imposed.
2. **`vlt-query`'s destination is hardcoded to the agent zone.** It already produces the exact
   artifact class in question — multi-page synthesis, `sources:` list, `author: agent`,
   `trust: raw` — and files it to `{research}` because no PARA destination is legal. The third
   surface exists as *behavior* and lacks only a legal address.
3. **The repo's own governance quality biases toward perimeter patches.** Single-home
   discipline, the version handshake, and precedence-by-elimination all raise the cost of a
   **structural** change relative to a **clause** change. Excellent disciplines — and they make
   the minimal patch the rational move every time, which is exactly how a root cause survives
   four cycles. *The minimal patch is the biased choice, not the neutral one.*
4. **Long feedback delay drives shadow-tree formation.** Blocked vaults build workarounds
   meanwhile, and the workaround becomes the observed normal.
5. **Two vaults failing in opposite directions masked a single cause** (above).
6. **Feedback-rail defects compound the delay** — a release that answers an issue without
   closing it, and a parked interim whose stated exit condition was silently invalidated by the
   ruling that answered it. Both reduce a vault's confidence that parking-and-filing works.

## System dynamics

- **Loop 1 — the agent-zone gravity well (reinforcing, vicious).** No legal PARA home → files
  to `_agent/` → PARA stays empty → PARA appears unused → less pressure to fix PARA write paths
  → more content to `_agent/`. A second arc rides on it: `_agent/` accretes → content becomes
  unreachable → the human can no longer browse to what they need → they ask an agent to
  retrieve it → more agent-mediated work. **The vault becomes progressively less navigable by
  its owner, and the module reads that as normal operation.**
- **Loop 2 — the honesty net (balancing, well-built, rarely fires).** Agent writes to PARA →
  lint tests honesty → violation surfaced → writer attests or the human rules. It seldom runs,
  because the prohibition upstream of it prevents the writes it is designed to police. Where it
  *did* run it correctly surfaced 0-of-56 unattested — working exactly as intended, on a
  population the prohibition had already driven into falsification.
- **Loop 3 — allowlist accretion (reinforcing, complexity-generating).** Legitimate need
  blocked → filing → cycle → **named exception** → the contract grows more specific → the next
  need matches no exception → filing. Each turn adds a special case and *reduces* the
  probability that a future need fits an existing category. **The module's standing response to
  "this op legitimately needs PARA" is allowlist accretion** — visible inside the contract text
  itself, not merely in the cycle history.

**Leverage ranking** (lowest → highest): add a third named surface (*pass five; feeds Loop 3*)
→ relabel the output (*falsification*) → flip PARA's default posture (*fixes Loop 1, leaves Loop
3*) → **move posture from module-global to vault-declared** (*changes who decides; drains Loop
3*) → **re-attach protection from location to trust level** (*retires RC1 outright; makes Loop 2
the real mechanism*). The two high-leverage interventions are complementary, not competing.

## Assumptions this study challenged

| Assumption | Status |
|---|---|
| "PARA is human territory" | **False as stated** — `{wiki}` is inside it and is agent-written |
| "Agent writes endanger human curation" | **Disproven in-module** — the wiki has been agent-written throughout with no curation loss |
| "`trust: reviewed` is PARA's entry level" | **Premise already broken** — justified by human-initiation, which cadence and headless ops violate today |
| "Extraction requires ≥2 wiki pages" | **Prose-only** — in no convention, no check. Ceremony |
| "Extraction is *the* artifact path" | **Assumed universal** — could be a disposition a domain adopts |
| "Loose artifacts at the layer root are legal" (`extraction.md:148`) | **True — and it cuts toward opening**: the layer is already less locked than the hard rule reads |

## What was recommended, and what the owner ruled

**Package C — "Declared Stewardship"** (72, against 62 for trust re-attachment alone, 60 for
full re-topology, and **44** for the third-named-surface patch). Package A wins only on cost,
speed, and reversibility — precisely the criteria that produced four prior passes — and scores
1 on both root causes and on derivability: it unblocks the digest and guarantees a sixth filing.

Settled owner rulings from the session:

| Ruling | Consequence |
|---|---|
| **`trust: raw` accepted in browsable space** | Honest raw agent content may sit in PARA; trust-filtered views are a follow-on, not a requirement |
| **Only `daily/`, `new/`, `sources/` are truly human-only** | `_vault/`'s disposition is **open** (contract `:76` still lists it human-only) |
| **`vlt-extract` demoted, not retired** | It becomes a quality standard, not a turnstile — the bottleneck is the clause, not the skill |
| **Package C selected** | Trust re-attachment **plus** declared per-domain stewardship |

**The sequencing is load-bearing:** the RC2 fix ships **before** the RC1 fix, because the RC1
fix *is a retirement* and the loop has no way to represent one. Shipping the rail afterwards
would make this analysis a one-off owner ruling instead of a repeatable capability — the exact
failure being fixed. *(That rail shipped as platform **P-15**, 2026-08-25, before Cycle 12's
roundtable.)*

**The load-bearing assumption:** that honest `trust: raw` / `author: agent` content is
acceptable to the human in browsable space. If the answer turns out to be no, the recommendation
**changes shape rather than collapsing** — author-blind placement with trust-filtered views
becomes mandatory rather than optional, and every other conclusion here stands.

## Where this differs from ST-1

`ST-1` named the cause as *one posture shipped as a universal invariant* plus *permission fused
to provenance in one verb*, and proposed a **second verb** with segregated `grounding:`
provenance. `ST-2` reaches the same territory from a different angle and lands somewhere
cheaper:

- **RC1 is a sharper statement of `ST-1`'s RC-A.** Not "the posture is hardcoded" but "location
  is standing in for a field that now exists and is enforced." That reframes the fix from
  *build a second verb* to **retire a redundant rule** — materially cheaper, and it is why this
  session's recommendation needs no new mechanism class.
- **RC2 is new, and it is the finding that justifies acting now rather than filing again.** The
  loop cannot see obsolescence, so this problem *cannot* arrive as a filing. Waiting for the
  field to file it is waiting for something the process is incapable of producing.
- **`ST-1`'s second verb is not refuted, only out-priced.** If trust re-attachment fails in the
  field, the second-verb design is still on the shelf and still coherent.

## Lessons that generalize

1. **When two instances fail the same rule in opposite directions, the rule is mis-specified.**
   A reusable diagnostic tell.
2. **Protections outlive their justification silently.** The location rule was correct when
   written and became redundant the moment the nets shipped — and nothing noticed, because
   nothing was watching for redundancy. **Shipping enforcement should trigger a retirement
   review of whatever prohibition that enforcement replaces.**
3. **A process that only accepts defect reports cannot retire anything.** Not a discipline
   failure — a **missing input class**, and it will keep producing perimeter patches until it is
   fixed.
4. **Location used as a proxy for a real field becomes falsification pressure.** The folder
   demanded a claim the content couldn't honestly make.
5. **The friction-gradient tell.** If governance is hardest on the content that most serves the
   user, the structure has drifted from the prose.
6. **Independent re-derivation is strong signal — and evidence of loss.**
7. **The module already contained its solution.** Enforcement, vehicle, artifact class, and a
   working proof of the discipline model were all shipped. The work was **retirement, not
   invention** — worth checking for *before* designing a mechanism.

## Traps recorded at writing

1. **Do not add a third named surface.** That is pass five wearing this analysis as cover.
2. **Do not file or capture the symptom.** The claim is *location is a proxy for trust*, not
   *the digest can't be written*.
3. **Do not retire `vlt-extract`.** Considered and rejected: the skill is not the bottleneck,
   and retiring it costs the Creative its only write plus four conventions their acks — while
   `extraction.md` survives anyway through `vlt-track`.
4. **Do not treat the minimal patch as the neutral choice.**
5. **Do not read roundtable conservatism as consensus.** Structural bias and agreement look
   identical from the inside.
6. **Do not ship trust re-attachment without its authorization net or a declared interim
   posture** — a rule ahead of its mechanism, in a plan written by someone who had just finished
   naming that failure mode.
7. **Do not judge success before the backlog relocates.** Legalising writes moves no existing
   file; judging occupancy too early makes a correct change read as a failure.

## The sharpest acceptance test

`trust: raw` is currently **unrepresentable** in PARA. If no `raw` content appears there after
the change, **it did not take** — regardless of what the contract now says. That failure would
point at the partner SKILL restatements, since the prohibition is restated in
`vlt-agent-creative:14`, `vlt-extract:13`, `vlt-review-council:51` and `vlt-upgrade:159`, not
only in the contract.
