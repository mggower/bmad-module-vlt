# PARA uses location as a proxy for trust — the honest partner is the one that gets stuck

_Filed 2026-08-25 by the owner. Evidence: `{field-vault}`'s `vlt-brief` blocked across three
cycles (tracker #11, open, zero comments); the Arc 9 A9-1 grounding correction from `app-vault`
(57 PARA files, **0 of 56 attested**); a full read of the shipped contract, `extraction.md`,
`vlt-extract`, `vlt-query`, `vlt-track` and the `para_*` checks at v0.15.0/HEAD. Classification:
**defect — structural**, fifth appearance of one cause. Provenance: owner problem-solving session
2026-08-25, recorded in full as **`factory/studies/ST-2-location-as-proxy-for-trust.md`** — cite
the study for the derivation, the rejected packages, and the settled owner rulings; this filing
states the claim and its grounding, not the analysis behind it. (`ST-1` is the 2026-08-20
re-derivation of the same ground, back-filled from the artifact that stranded in gitignored
`_output/` — the loss this register exists to prevent.)_

## The defect

Layer 3's boundary is **declared** as authorship-honesty (contract `:66`) and **implemented** as a
location prohibition with named exceptions (contract `:68`, rule-card `:26`). Partner content
reaches PARA through exactly two surfaces, and both presuppose that agent output arriving in
human-browsable space has already passed through a human or the wiki:

- **extraction** — a *graduation* surface: wiki-sourced, `author: hybrid`, `trust: reviewed`
- **container maintenance** — an *annotation* surface: dated attributed appends to an existing
  `record.md` / `register.md`

There is no **authorship** surface. A partner authoring a new, standalone, human-facing document
that is honestly `author: agent` and honestly `trust: raw` has no legal placement anywhere in PARA.
That is not an edge case — it is what every scheduled digest, generated report, and recurring
deliverable *is*.

The only way to place such a document where humans browse is to relabel it `author: hybrid` /
`trust: reviewed`. That is an authorship-honesty violation, and authorship-honesty is the *stated*
boundary of the layer. **The contract's honesty rule and its write rule point in opposite
directions, and the honest partner is the one that gets stuck.**

### The proxy is redundant

PARA membership is being made to carry a trust claim that the `trust:` field already carries
explicitly. That proxy was **correct when written** — the honest fields had no enforcement behind
them, so location was the only protection available. It stopped being necessary when Cycle 11's
build-6 extended `para_missing_attestation` / `para_author_unknown` / `para_status_unknown` across
the whole PARA population with `{wiki}` excluded by name.

`extraction.md:53-60` already reserves **every trust level above `raw`** to the human. A surface
admitting honest `author: agent` / `trust: raw` documents would therefore not weaken the human's
curation monopoly at all.

### The proxy is also already broken in shipped code

`extraction.md:60` justifies the `trust: reviewed` entry level on the grounds that *"the act of
extraction is a human-initiated curation step."* That premise is false for any cadence-driven or
headless run — and `vlt-track` runs extraction on a loop, while `vlt-query` explicitly *"runs
interactively or headless"* (`vlt-query/SKILL.md:10`). The human-initiation fiction the location
rule rests on does not hold today.

### Two vaults, one rule, opposite pathologies

- **`app-vault`** — 57 files in `projects/`, all carrying extraction frontmatter, **0 of 56
  attested**. Agents were never blocked; they routed through the one door by falsifying the fields
  at it.
- **`{field-vault}`** — PARA largely **empty**. Agents honestly decline the door, so everything
  accumulates in `_agent/`, leaving content deeply nested, unreachable and unorganized.

Falsification and abandonment are not two problems and not discipline failures. They are what
agents do when **honest labeling has no legal destination**. A rule that produces both is
mis-specified, not under-enforced.

### The counter-example is inside the module

`{wiki}` sits inside the human-browsable layer, is written exclusively by an agent, holds honestly
agent-authored documents — and produces no friction whatsoever. It is protected by **its own
discipline** (single writer, convention set, attestation, an index), not by a prohibition on agent
writes. PARA is protected by prohibition. The problem is absent exactly where a zone has authoring
discipline and present where the module substituted a location rule for one.

### Why this is the fifth appearance

Each prior pass moved the fence; none opened a door.

| Pass | Shipped |
|---|---|
| Arc 9 (A9-1) | Deferred; v0.12.0 shipped a CHANGELOG posture note only |
| Arc 10 (B10-10) | The container model — legalized the *append* surface |
| Cycle 11 (Q1) | `resources/` granted parity — into the same two doors |
| Cycle 11 (build-6) | The honesty nets extended across PARA — **beside** the prohibition, not in place of it |

Build-6 is the tell. It shipped the enforcement that makes the location rule redundant, and the
rule survived, because **the evolution loop has no way to process obsolescence**: every input is a
filing, and a filing describes something that *broke*. Nothing can express *"this protection is now
superseded,"* since obsolescence produces no field pain — only friction that reads as normal
governance. The roundtable hunts *rules ahead of mechanisms* and has no beat for the reverse.
Eleven cycles have retired zero rules while adding many.

**That process gap is a platform-channel concern (factory skills, not shipped surface) and is filed
separately. It is named here because it is the reason this defect recurred four times, and capture
should not treat this filing as a clause repair.**

## The fix direction

Not a third named surface — that is the fifth pass wearing this filing as cover, and it feeds the
same allowlist accretion (`vlt-track` named in the base at `extraction.md:47`; containers as a
second surface; `resources/` parity). Four exceptions, zero categories.

**Re-attach the protection from location to trust level, then let each domain declare its own
posture:**

1. **Retire the ≥2-wiki-page gate** (`vlt-extract/SKILL.md:38`, `vlt-agent-creative/SKILL.md:37`).
   It appears in no convention and no check — prose-only ceremony, and the most-cited authoring
   bottleneck in the module. **No handshake cost.**
2. **Make PARA's entry condition honest, attested frontmatter** rather than a named surface —
   contract `:66`/`:68`, rule-card `:26`; correct the `extraction.md:60` human-initiation premise;
   bump `extraction.md` 6 → 7 and re-ack `vlt-extract`, `vlt-lint`, `vlt-track`.
3. **Demote extraction to a disposition** — the verb that produces graduated, wiki-traceable
   `trust: reviewed` artifacts, chosen for that guarantee rather than endured as the only way in.
   The Creative keeps extraction; it stops owning the turnstile. (Retiring the skill outright was
   considered and rejected: the bottleneck is the clause, not the skill; retirement would cost the
   Creative its only write and four conventions their acks while `extraction.md` survives anyway
   through `vlt-track`.)
4. **Give `vlt-query` a PARA destination.** It already produces the artifact class in question —
   multi-page synthesis, `sources:` list, `author: agent`, `trust: raw` — and files it to
   `{research}` (`vlt-query/SKILL.md:46`) only because that is the sole legal home for a raw
   agent-authored document.
5. **Declare stewardship per domain** — a `writers:` declaration on the container `charter.md`
   (human-gated, already shipped by B10-10), with a **module-fixed floor** so `{wiki}` stays
   Librarian-only in every vault. The wiki then ceases to be a carve-out *by name* and becomes an
   instance of the general rule — precedence by elimination, per the Arc 9 D5 standing rule.
6. **Extend `vlt-lint` with an authorization check** joining each write against its domain's
   declared writers — the enforcement a prohibition could never actually perform.

### Owner rulings already made (2026-08-25)

- **`trust: raw` is accepted** in human-browsable space. Honest raw agent content may sit in PARA.
- **The only truly human-only zones are `daily/`, `new/`, `sources/`.** (`_vault/` is listed
  human-only at contract `:76` and was omitted from that list — disposition open.)
- **`vlt-extract` is demoted, not retired.**

### Open questions for ideation

- **Undeclared-location default** — open to honest writes, or closed? (Provisionally *open*, by the
  `trust: raw` ruling; confirm explicitly rather than defaulting into it.)
- **MOC prohibition** (contract `:190`) — recommended: survives as a **content-type** rule
  independent of zone posture, since it protects human *endorsement*, not human *territory*.
- **`_vault/`** — confirm its disposition.
- **Ship-verifiable vs field-contingent tagging** — the retirement of a load-bearing rule should
  **gate** closeout (the A4-4(5) lesson).

### Sequencing hazards (both surfaced during analysis, both belong in the roundtable's joint-hunt)

- **Rule ahead of mechanism.** Step 2 above legalizes writes while step 6 supplies the
  authorization net. Between them, writes are legal but authorization is uncheckable. Ship them in
  one release, or declare an explicit interim posture in the roadmap.
- **Legalizing relocates nothing.** The field symptom is content *already* buried in `_agent/`.
  Making future writes legal moves no existing file. Without an owner-gated relocation pass
  (a `vlt-groom`-shaped proposal the human ratifies), PARA occupancy will barely move and a correct
  change will read at acceptance as a failed one.

### The sharpest acceptance test

`trust: raw` is currently **unrepresentable** in PARA. If no `raw` content appears there after the
entry-condition change, the change did not take — regardless of what the contract says. That
failure would point at partner SKILL restatements, since the prohibition is restated in several
skills (`vlt-agent-creative:14`, `vlt-extract:13`, `vlt-review-council:51`, `vlt-upgrade:159`), not
only in the contract.

**Field pilot:** `vlt-brief`'s next scheduled issue files to `{resources}/briefs/` at honest
`author: agent` / `trust: raw` — no relabeling, no pointer-container indirection, no bespoke
carve-out. One live run exercises the whole chain, and closes tracker #11.
