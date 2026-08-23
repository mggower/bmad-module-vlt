# Defect: lint's contradiction model has one axis where it needs two — documentation *is* the drain, and it reads as health

_Filed 2026-07-25 by the Librarian from **`vlt-core`**, surfaced during a full `vlt-lint --full` sweep
(130 wiki pages) that returned **25 unhandled + 63 handled** contradictions. Owner asked "do we have a
mechanism for resolving these?" — the answer turned out to be no, and the reason is structural rather
than a missing feature. This is a **defect/design gap**, not a candidate._

## The finding

Every other `vlt-lint` finding class has a **drain** — a named next owner and a state transition that
ends in the finding being *gone*. Contradictions have one state transition (undocumented → documented)
and it is **terminal, and framed as success**.

| Finding class | Drain (shipped) |
| --- | --- |
| near-duplicates / merges | `{backlog}` `maintenance` item → **`vlt-ingest`** resolves under the consolidation discipline |
| index drift, frontmatter drift | auto-fixed in Step 3 |
| `review_due` | surfaced → human runs the documented three-outcome review |
| convention/capability/family drift | flagged → human reconciles, then bumps the ack |
| **contradictions** | **documented in both pages, and that is the end of the road** |

## Grounding notes (factory-side, checked 2026-07-25 against v0.7.0 source)

- `skills/vlt-lint/SKILL.md:69` — "**Contradictions** — … Document in both pages' Contradictions/Open
  Questions; note which source is more recent/authoritative, but never silently pick a winner."
  A *documentation* instruction. No backlog filing, no next owner, no revisit trigger.
- `skills/vlt-lint/SKILL.md:101` — the do-not-auto-apply list treats the two classes differently in the
  same sentence: "**page merges (file to backlog — see Step 4)**" versus "**contradiction resolutions
  (document both, flag)**". Merges get an explicit drain named inline; contradictions get a full stop.
- `skills/vlt-lint/SKILL.md` Step 4 is titled *File maintenance backlog items* and its body is
  near-duplicates only. Contradictions are never eligible for it.
- `skills/vlt-lint/SKILL.md:150` — `contradictions_handled: [...]  # already documented — surfaced, not
  vanished (**a managed disagreement is a feature**)`. This is the load-bearing line: once a callout
  exists, the finding moves to a bucket whose stated meaning is *health*.
- `wiki-supersession.md` and `wiki-consolidation.md:73` both cover conflicting claims, but only
  **write-side** — at ingest/merge time, by the writer holding the source. Neither addresses a
  contradiction that a **sweep** surfaces later, when no source is in hand and no writer is mid-flow.

So the write-side discipline is complete and correct; the **sweep-side** has no counterpart.

## Why "documented" is the wrong terminal state

`vlt-lint:175` says *"Contradictions are features, not bugs — a well-documented disagreement beats
false certainty."* That is **true for one kind of contradiction and false for another**, and the
report shape cannot tell them apart:

- **Genuinely open** — two credible sources disagree and the vault should hold both. Documentation
  *is* resolution. (Example from this sweep: whether Erhardt-Perkins is a high- or low-mental-load
  system — Patriots-implementation voices vs scheme-theory voices genuinely split.)
- **Adjudicable** — one side is simply *wrong*, or one page is stale, and a bounded act closes it.
  Documentation is a **deferral wearing the costume of a feature**.

Both land in `contradictions_handled` and are counted as health.

### The proof, from this vault's own data

The clearest evidence is that **the same defect class appears on both sides of the handled/unhandled
line**, decided only by whether someone happened to write a callout:

- **Counted `handled`:** the *Brian Schottenheimer / Brian Flores* name collision — a **YouTube
  auto-caption substituting a plausible real name**. It is documented, therefore "handled", therefore
  reads as a managed disagreement. It is not one: it is an unresolved factual error, and `vlt-core`'s
  backlog carries an open `knowledge-gap` item to fix it ("Name the Seahawks' 2026 offensive
  coordinator"). The *report* says health; the *backlog* says open. Nothing reconciles them.
- **Counted unhandled:** *Jonah Jackson vs Alaric Jackson* on `los-angeles-rams` vs
  `nfl-2026-offense-rankings` — **the identical failure mode**, from the same show's captions. It sits
  in `contradictions` only because no one has written its callout yet. The moment someone does, it
  graduates to "feature."

A classification where writing a sentence converts a factual error into a documented feature is not
tracking what it claims to track.

### The silent-zero shape, again

`contradictions_handled: 63` (against 25 unhandled, on 130 pages) is a number that **only ever grows**
and is reported as a positive. There is no signal anywhere that distinguishes 63 healthy managed
disagreements from 63 deferred adjudications. This is the same shape as
`inbox/2026-07-13-092341-spec-convention-has-no-advocate.md` and
`inbox/2026-07-25-144500-revisit-after-has-no-adoption-path.md`: **an absence/terminal-state branch
whose silence is indistinguishable from success.** Third instance of the arc's own scar, in a third
mechanism.

## Field consequence (what actually happened here)

On this sweep I flagged all 25 and did **not** document them, because documenting 25 contradictions
across ~50 pages is a large, low-reversibility write and the skill offered no signal about which
deserved it. That hesitation is itself diagnostic: **the instruction's cost scales with vault size
while its value does not**, because the output is the same terminal state either way. A 130-page
vault makes "document all of them" expensive enough to skip, and skipping is invisible in the report.

Triaging them by hand (owner-requested, not skill-directed) produced four buckets the skill has no
vocabulary for: **11** fixable now from the vault's own pages (stale cross-references, a misfiled
section heading, prose left behind its own `[!superseded]` callout), **4** needing external evidence
(one is a **food-safety** claim — medium-rare guidance on non-intact beef contradicting the page that
defines the intact-whole-muscle rule), **8** genuine framing differences, **2** needing a one-line
source check. Only the middle two buckets are what `:175` describes.

## Candidate shapes (for the capture to weigh — not rulings)

1. **Split the bucket.** Report `contradictions_open` (genuinely disputed, documentation *is* the
   resolution) separately from `contradictions_deferred` (adjudicable; someone must act). Cheapest
   change; makes the health claim honest without new machinery.
2. **Give the adjudicable half a drain.** Let Step 4 accept contradictions, not just merges — a
   `{backlog}` `maintenance` item routed to `vlt-ingest` (needs a source) or the owning partner
   (fixable from the vault). Mirrors the near-duplicate chain exactly, which is already proven.
3. **Make documentation carry a disposition.** The callout records *which kind* it is and, when
   adjudicable, what would close it — the same move `review_after:`'s three-outcome review makes for
   staleness. Turns a terminal state into a tracked one.
4. **Cap the documentation instruction.** `:69` currently reads as unbounded; at scale it is
   routinely skipped. Either bound it (document the top N by severity) or make it explicitly a
   judgment call, so skipping is a stated outcome rather than silent under-delivery.

Shapes 1 and 2 are complementary — 1 makes the report honest, 2 gives the newly-visible half an owner.

## Honest limits of this filing

- **One vault, one sweep.** `vlt-core` at 130 wiki pages. The 63/25 split is a single measurement;
  I do not know whether a smaller vault feels this at all. The mechanism is size-sensitive by nature,
  so a 30-page vault may have no complaint.
- **The four-bucket triage is mine, not the module's.** I produced it by hand after the sweep, at the
  owner's prompting. It is offered as evidence that the distinctions *exist and are actionable*, not
  as a proposed taxonomy — the shapes above deliberately don't adopt it wholesale.
- **Nothing is broken today.** Every contradiction found was correctly *found*; the cluster pass
  works well (it caught a cross-page food-safety conflict I would not have). This is a
  **disposition/visibility** defect, not a detection defect.
- **The `handled` framing is defensible in isolation.** "A managed disagreement is a feature" is a
  genuinely good instinct and I would not want it removed — the defect is that it is applied to a
  bucket that also contains things nobody managed.
- **Provenance guess, marked as a guess:** I suspect this class was never drained because
  contradictions were designed write-side first (where the writer *does* hold the source and *can*
  adjudicate), and the sweep-side case inherited the write-side's vocabulary without inheriting its
  preconditions. Unverified — I have not read the relevant design history.

## Provenance

- Vault: `vlt-core` (0.7.0, factory machine), 130 wiki pages / 98 research notes.
- Surfaced by: `vlt-lint --full` 2026-07-25 15:05 — see that `{log}` entry and the follow-on triage in
  the same session.
- Related open `vlt-core` backlog item, **not yet filed here**: "Consider a source-provenance rule for
  the auto-caption transcript family", flagged in-vault as a module-feedback candidate and now firing
  for a third time — that caption failure mode is the *source* of two contradictions cited above. It
  is a separate signal (ingest-side grounding, not lint disposition) and awaits its own filing.
- Natural home: **Arc 4**, alongside the adoption-facet work — same silent-zero family.
