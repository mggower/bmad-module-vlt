# Partner memory has no promotion ladder or staleness contract — corrections land on knowledge already written down

_Filed 2026-08-17 from **vlt-core**, classification: **candidate**. Prompted by a partner's own
in-thread complaint and converged out of a dedicated ideation session
(`_agent/artifacts/brainstorming/brainstorm-partner-thread-pruning-2026-08-17/` — memlog holds the
full 44-idea set), then prototyped the same day as a manual groom pass on the career-strategist
partner. Grounding measured against vlt-core at b00db0a and module source at b117d81. Owner elected
to file (2026-08-17)._

## The claim

The partner memory model (`identity.md` + `thread.md`) has a write path but no promotion path and
no staleness contract. Everything a partner learns is appended to the thread or the bond regardless
of what *kind* of thing it is — a durable rule, a revisable read, an episodic narrative, a closed
item — and nothing ever moves a lesson to the layer where it would actually bind. The observed
failure is not volume (that is the 2026-08-16 sibling filing, below); it is **enforcement and
staleness**: a partner corrected three times in one sitting, every correction landing on something
already recorded in its own files, and reads revised by stacking new versions atop old ones so
sessions load superseded claims alongside live ones.

Distinct from `2026-08-16-093429-append-only-agent-files-have-no-decay-contract.md`: that filing is
**volume/decay** (files grow without bound; its "tend" verb covers thread mass). This one is
**routing/enforcement** — a thread can be small and still stale, duplicated against the wiki, or
holding rules in a form that demonstrably does not bind. Related, deliberately not merged: the
sibling's fix (rotation/compaction) would shrink these files without fixing a single mis-filed rule.

## Grounding (vlt-core, career-strategist partner "Rook", 4 days / 5 sittings old)

- **The triggering event, in the partner's own thread** (pre-groom, `git show 1acfbbc` in vlt-core):
  *"Three times in one sitting I broke a rule that was already recorded in my own files"* — the
  narrative-defensibility bar (recorded in `## Bond` three days earlier), a loop-profile constraint
  (read that same sitting), an error corrected twice in a ledger file. Its own diagnosis: *"a
  recorded lesson protects against the form it was recorded in and nothing else."*
- **Revision stacking:** one standing read (EM→IC fork) existed as an 08-13 original plus two 08-14
  revisions plus a "set aside" tombstone — four versions loaded every sitting for one live claim.
- **Misrouted content classes, measured by the prototype groom:** of 48.1K of partner memory,
  ~17.6K survived as live (63% cut). What left: closed/resolved items, revision histories, worked
  content duplicating its single home (`positioning/positioning.md` carried the worked read; the
  thread restated it), and ~21 rules phrased as narrative that compressed to one line each.
- **Prototype evidence** (vlt-core b00db0a): the groom produced `reflexes.md` — an always-loaded
  ≤30-line antibody file of one-line rules — plus latest-form-only reads with falsifiers, and
  git-as-archive (an `archive:` frontmatter pointer to the pre-groom commit) instead of duplicating
  retired text. No annals duplication was needed; every append already pairs with a commit.
- **The wiring gap:** there is no template slot for a reflex layer. The prototype smuggled the load
  instruction into `identity.md` ("read `reflexes.md` in the same breath") because the memory-partner
  skill flow reads only `identity.md` + `thread.md` at first breath.
- **The partner's own analysis, worth capturing verbatim** (it is in the live thread's "Waiting on"):
  its three same-sitting recurrences are **three different classes** — (a) *mechanically checkable*
  (a lint finding closes it), (b) *checkable at the moment of the move, not at activation* (prose
  lessons lose to context by write time; the divergence-stamp precedent solved this shape once),
  (c) *possibly irreducible judgment* (reaching for the wrong evidence because the clean artifact
  was easier to write about). Its warning: **(a) is the easiest to fix and (c) is where the damage
  is.** A single mechanism will not reach all three.

## Why it matters

- The failure is user-facing and trust-eroding in exactly the wrong direction: the partner model's
  premise is memory, and here memory produced *repeated* corrections on *recorded* knowledge — worse
  than forgetting, because the user pays to maintain files that then don't bind.
- The write path's economics run backward: appending to the thread is free; filing to the right
  home (skill profile, wiki, always-loaded rule) costs effort. Knowledge pools in the wrong store.
  The thread also violates the module's own single-home convention with no lint coverage, since
  partner files sit outside `vlt-lint`'s wiki scope.
- Every memory partner in every vault grows this; heavy use accelerates it. Rook hit it at four
  days under a job-search workload.

## Candidate dispositions (for capture to rule — not pre-empted here)

- **(a) A typed promotion ladder in the partner-memory convention.** remark → thread → standing
  read → identity trait → reflex/profile → wiki, each rung with entry criteria, each file declaring
  which rungs it may hold. The heuristic that worked in prototype: any line phrased as an
  instruction to future-self ("always", "every time", "never", "unasked") is rule-layer material by
  definition — grep-detectable.
- **(b) A reflex layer in the partner template.** A capped always-loaded `reflexes.md` (one line
  per rule, hard cap in its own frontmatter) scaffolded at mint, loaded at first breath alongside
  identity. This is the fix for the partner's class (b): rules survive as reflexes where narratives
  demonstrably don't.
- **(c) Thread lifecycle rules shipped at birth.** Latest-form-only reads (revise by replacement;
  history is git's job via an `archive:` frontmatter pointer), falsifiers that *retire* a read when
  fired (the "what would change my mind" field exists in practice but nothing wires it), closed
  items leave the file.
- **(d) Correction as a typed signal.** A user correction that maps to already-recorded knowledge
  is a filing defect, not new content — handled in the moment (fix the home, delete the duplicate,
  log a pointer), counted per sitting as the health metric. Corrections-per-sitting is the natural
  regression test for whatever ships.
- **(e) A groom op, upstream not minted.** A scheduled or triggered pass producing an
  approval-gated diff (bond material is intimate; never silently deleted) that promotes, compresses
  to latest-form, and retires against git-as-archive. Prototyped manually once; the manual pass is
  cheap enough that this can wait for a second data point.
- **(f) Partner files enter lint scope** for staleness, duplication-with-wiki, and
  rule-phrased-as-narrative findings.

Preference, weakly held: **(b)+(c) at the template** (they fix new partners at birth and ride
git-as-archive, which the prototype validated), **(d)** as the cheap behavioral rule and metric,
with **(a)** as the durable convention and **(e)/(f)** as machinery that can follow. Honest caveat
from the partner's own three-class analysis: (b)+(c) reach classes (a) and (b); class (c) —
judgment errors wearing new costumes — may be irreducible, and capture should not let the easy
fixes claim otherwise.

## Provenance guess (marked as a guess)

Likely origin: the memory-partner design solved *continuity* (identity/thread survive across
sessions) and *write safety* (single-writer, commit-paired) with the memory's internal economy out
of frame — same posture-age pattern as the sibling filing and the boot-whale arc. The template
predates the vault's later single-home and enforcement-declaration discipline, so partner memory
never inherited either. A guess; factory capture should re-ground it.
