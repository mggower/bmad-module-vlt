# Wiki `sources:` should ship as wikilinks — rule 4's bare-path default makes the source layer unreachable from the pages that depend on it

_Filed 2026-08-14 from **vlt-core**, which overrode this locally via `frontmatter.overlay.md` after a
review council upheld the routing unanimously. Evidence is vlt-core, and the local override is running.
Classification: **candidate** — a proposed change to a shipped default, with one design constraint that
must ship with it._

## The claim

`frontmatter.md:36`, YAML rule 4:

> **Non-graph list fields use bare paths/basenames, not wikilinks.** A list that is an audit trail
> rather than a link graph (e.g. a session log's `artifacts:`) holds plain vault-relative paths. Do not
> wrap these in `[[...]]` — the audit trail is not a wikilink graph. (`sources:` likewise holds plain
> page references unless a specific schema says otherwise.)

The rule is right about audit trails and, we think, wrong about `sources:` **on a wiki page**. A wiki
page's `sources:` is not an audit trail — it is a **link graph**. The page's claims are answerable to
the sources that produced them, and a reader following a claim back to its origin is the entire point
of keeping the field. In Obsidian the bare-path form renders as inert text, so in practice the source
layer is unreachable from every page that depends on it. An audit trail nobody can traverse is not
serving as an audit trail.

The proposal: **wikilinked `sources:` becomes the shipped default for the wiki-page schema**, leaving
rule 4 governing genuine audit trails — a session log's `artifacts:` above all. The distinction rule 4
should draw is whether a reader is meant to **traverse** the list or merely to **verify** it.

## What vlt-core shipped locally, and why it was legal without a base edit

Rule 4 ends "unless a specific schema says otherwise," which the council read as a **delegation slot the
base cut in its own text**. The unanimous test for occupying such a slot — worth writing into the
contract's overlay section, since it is currently derived rather than stated:

> An overlay may occupy a base carve-out where **(a)** the base names the carve-out in its own words and
> **(b)** the overlay names the exact schema and scopes narrowly.

The local form, for reference:

```yaml
sources:
  - "[[sources/articles/2026-06-19T115833-0400-which-nfl-breakouts,-nosedives-will-continue-in-2026-season?]]"
```

Three details, each of which cost something to get right:

- **Double-quoted** — base rule 1 applied, not a new rule; a bare leading `[` opens a YAML flow sequence.
- **Full path, not basename** — basenames are a collision surface that grows with the collection.
- **`.md` dropped** — consistent with base rule 1's own extension-less example, `superseded_by: "[[page-slug]]"`.

Also worth shipping: **only `[`, `]`, `#`, `^`, `|` are wikilink-reserved.** `?` is not, and five
`sources/articles/` basenames in vlt-core carry one. The first draft of the local rule silently dropped
a trailing `?` from its own flagship example and produced a dead link — a mistake any adopter will make
once, so the shipped rule should say this positively rather than leaving it to be rediscovered.

## The design constraint that must ship with it

**Research notes also carry `sources:`.** If only the wiki-page schema converts, the bare-path/wikilink
mismatch is **permanent by design** — not a migration window that a backfill closes.

The specific casualty is `vlt-lint`'s `linkage_ripe` shared-source leg
(`vlt-lint/references/checks.md:59`), which excludes a research note from the graduation queue when
"the note and a wiki page share an entry in `sources:`". Under naive string equality a wikilinked entry
never matches a bare-path one, so the leg silently stops firing. `checks.md:57` names this failure class
itself, in the neighbouring leg:

> a blind spot in an absorption test is a false positive (a note called ripe that was in fact absorbed).

So the cost is not cosmetic: research notes get reported as graduation-ripe when a wiki page has already
absorbed them, and the check's measured "≈0% false-positive" calibration quietly stops holding.

Two ways to close it, and an upstream version needs one of them:

1. **A normalization clause** — any comparison of `sources:` entries strips wikilink brackets and any
   `.md` extension before matching. This is what vlt-core shipped, because it survives the two forms
   coexisting forever.
2. **Convert both schemas together**, so the forms never diverge. Cleaner, but it makes the change
   larger and still wants the clause as a defence against the next divergence.

## Provenance guess — marked as a guess

Rule 4 reads like it was written from the `artifacts:` case — a genuine audit trail where the
no-wikilinks instinct is exactly right — and `sources:` was swept in by resemblance, both being
lists-of-paths. The parenthetical hedge ("unless a specific schema says otherwise") suggests the author
already sensed `sources:` was a weaker fit than `artifacts:`. **Inference from the rule's wording; I
have not read the module's history.**

## What acceptance should check

That `linkage_ripe` still excludes an absorbed research note when the wiki page citing it is on the
wikilink form and the note is on bare paths. That is the leg that breaks, it breaks silently, and it
breaks in the direction of a false positive rather than a visible error.
