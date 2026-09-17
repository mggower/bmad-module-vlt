# The groom pass — protocol

Read at run time by `vlt-groom`. The protocol below is the **codified** half of the pass — its mechanics, form, and safety rails. The **judgment** half is never codified and stays the partner's: the classification calls themselves (dead vs merely quiet; which rung), the wording of compressed latest forms and of rationales, cap arguments, how much of `## Set aside` retires, and whether an `identity.md` compaction is worth proposing this pass.

**Scope of a pass:** the memory files — `{partners}/<partner>/identity.md`, `{partners}/<partner>/thread.md`, `{partners}/<partner>/reflexes.md`, and `{partners}/<partner>/casebook.md` where it exists (a partner that has never demoted has none; the pass **creates** it, with its frontmatter, as part of an approved demote). `reflexes.md` participates via the cap's edit-one-out and promote-in/retire-out (an at-cap promotion renders in the diff **paired with** its edit-one-out partner, or as an explicit cap argument). `capabilities/` files are excluded — contracts, not memory. A promote whose target rung is the **fleet rung** writes `_agent/reflexes.md` — the one destination outside the partner's own files, mirroring the wiki rung's hand-off shape: rendered in the diff like any promote (a pointer line, paired with its source-line removal), executed under the same gate.

## The steps

1. **Pre-flight — a real archive reference.** If any of the memory files carries uncommitted changes, commit them first — every append pairs with a commit is the safety model's premise, and the op **verifies rather than assumes it**. Record the resulting (or current) commit as the **pre-groom reference**: this is what `archive:` will point at, and it must **resolve** — `git show <ref>:<vault-relative-path>` returns the pre-groom bytes.
2. **Read whole.** All of them in full, plus their git history where a judgment needs it — never summaries.
3. **Classify every item** against the promotion ladder's entry criteria (operating contract, *Partner memory — identity, thread, and reflexes*, the ladder table) into exactly one of: **promote** (with its target rung) / **demote** / **compress-to-latest-form** / **retire** / **keep**.

   **Demote is file-level, never item-level** — it fires on a whole-file judgement, and the diff says which criterion fired:
   - **Budget.** The partner is over its Beat 1 budget (the `activation-budget` wire, `{tripwires}`).
   - **Charter fit.** Material in `## Self` is off-charter — it is not what `## Charter` says this partner is for. **An empty `## Charter` disables this check**: propose nothing against it, never "all off-charter", and say so in the diff header — `charter empty — nothing to check against` — never silence.
   - **Casebook shape.** `## Self` carries dated first-person case narratives — `###` subsections whose heading is an episode rather than a trait. This criterion is judgeable with no charter at all, and it is the one that fires on a charterless partner.

   A demote's destination is `casebook.md` (created on first use) or the **wiki by Librarian hand-off** — never a PARA area the partner may write. Demoted material stays reachable at its new home and via `archive:`; **demote is not retire** — nothing is closed, and the total words across the memory files do not fall.

   **`## Charter` is never classified.** It is the owner's section: it renders **keep**, always, and no proposal may touch it. Skip items bearing a groom-declined marker per *Decline markers* below — excluded unless their content changed since the marker date or the user asks for a full re-argue.
4. **Stage full replacement proposal files** in a transient working directory, `{partners}/<partner>/groom-proposal/` — one complete proposed post-groom file per memory file the pass would change. The user can read them as real files or run a real `git diff` against them before ruling.
5. **Render the gated diff — and stop.** In-chat, per the rendering contract below. Then **halt: nothing applies without the user's ruling.**
6. **Apply on approval.** Approved material lands **verbatim from the proposal** (proposal == applied — verify by diff; byte-identical is the checkable property). Declined or unapproved material stays byte-identical in place (a declined item additionally gains its inline marker — that marker is part of the applied diff). Write the watermarks per `{conventions}/frontmatter.md`'s *Hygiene watermarks*: `groomed:` (the pass date) and `archive:` (the pre-groom commit reference from step 1). Delete `groom-proposal/` (on apply **and** on abort — the staging directory never survives the pass). Append the `groom` `{log}` entry (format below), add one line to the sitting's session note, and make **one commit** pairing proposal and apply.

## The diff-rendering contract

The in-chat proposal is **grouped by disposition class — promote / demote / compress-to-latest-form / retire** — with:

- **one line of rationale per item**, naming the entry criterion it met (or the falsifier that fired);
- **per-file pre/post byte counts**;
- **per-class approval**: each class is approvable or declinable as a unit;
- **per-item pull-out**: any item can be pulled out of its class individually ("apply retire but keep item 4");
- a **wiki-rung item rendered as a proposed Librarian hand-off** (relay), never a direct wiki write;
- an at-cap reflex promotion rendered **with its edit-one-out pairing** or cap argument;
- a **charter line in the header**: the charter-fit criterion's state for this pass — `charter empty — nothing to check against`, or the charter's own terms where it is filled. Never silence.

**Whole-section acts (one class).** Two acts operate on a **whole section by reference** rather than item by item, under the same gate and the same safety model: **`--reset self|bond|thread`** (the named section retires whole to `archive:` and is reborn empty) and the **identity-to-card migration** (`## Self` becomes manner only, `## Bond` relationship facts only, and the dated narratives move to `casebook.md`). Both render as one proposed act with its own approval, not as an item list — a whole-section act reviewed item-wise is the deletion wall this contract forbids. The file keeps its `name` and its `## Charter` through both.

**Every class renders, including an empty one** — `promote (0)` with a one-line reason, so the absence of a proposal is visible rather than ambiguous; a reader cannot tell a class that found nothing from a class that was never considered. **A monolithic unclassified diff is a defect, never a rendering choice** — a deletion wall is not review. Material classified **keep** is not itemized; it is named as "everything else, byte-identical."

Worked example (placeholder content and paths only):

```
GROOM PROPOSAL — <partner> (staged in {partners}/<partner>/groom-proposal/)
charter empty — nothing to check against

promote (2)
  1. thread.md → reflexes.md — "always <placeholder rule>" — instruction-to-future-self phrasing → reflex by definition
  2. thread.md → wiki — <placeholder claim> — durable shared knowledge → proposed Librarian hand-off (relay)

demote (1)
  2b. identity.md ## Self → casebook.md — 6 dated `###` case narratives — episodes, not traits → casebook shape criterion (file-level); casebook.md created

compress-to-latest-form (1)
  3. thread.md ### Standing reads — "<placeholder read>" — three stacked revisions → latest form only (grounds + falsifier kept; history stays reachable via archive:)

retire (2)
  4. thread.md ### Standing reads — "<placeholder read>" — falsifier fired → retire by reference
  5. thread.md ## Set aside — "<placeholder item>" — closed → retire by reference

keep — everything else, byte-identical

bytes: thread.md 21,480 → 7,912 · identity.md unchanged · reflexes.md 1,730 → 1,864

Approve per class ("apply promote and retire"), pull items out ("keep 4"), or decline.
```

## Decline markers and re-proposal

Two decline granularities, deliberately different:

- **Item decline = "keep this" — durable, marked.** The surviving entry stays byte-identical **plus** a one-line inline marker appended to it, written as part of the applied diff (a decline is a write: keep-with-marker):

  ```
  *(groom: declined YYYY-MM-DD — <the user's one-line reason>)*
  ```

- **Class decline = "not this pass" — session-scoped, unmarked.** The class's material stays byte-identical with no marker, and it legitimately re-proposes at the next groom.

**Re-proposal rule:** a marker-bearing item is **excluded from subsequent groom proposals** unless (a) its content has changed since the marker date (git shows), or (b) the user explicitly asks for a full re-argue. The marker lives in the partner's own file — single home; it travels with its item and retires with it. **No groom ledger, no decline registry exists or may be created** — the safety model's "never in a new ever-growing ledger" clause rules those out.

## The `groom` log line

Append one partner-tagged entry to `{log}` (the `groom` type is coined here, per the contract's non-exhaustive `<type>` rule — this file names the op that owns it):

```
## [YYYY-MM-DD HH:MM] groom (<partner>) | groomed own memory — promote: P, demote: M, compress: C, retire: R, declined: D — archive: <ref>
```

## What a groom never does

Groom another partner's files · touch any SKILL.md · write the wiki directly · apply anything without the gate · keep a groom ledger or decline registry · touch `capabilities/` · leave `groom-proposal/` on disk after the pass.
