# Grounding at Brief Time

Capture already ground each filing's claims against module source once. This is a **second**
grounding, and it exists because source moves between capture and brief: a later build in the
same cycle may have already changed a site the capture cited, so a `file:line` that was accurate
at capture is stale by the time you brief. Re-verify every site the brief will touch against
the module source **as it exists right now** — never trust the capture's cited line, and never
reason from the roadmap's line numbers (they drift; the roadmap is append-only and re-edited
across the cycle's life).

This is not `inbox-capture`'s grounding repeated. Capture graded a *filing's claims* into a
roadmap. This grounds the *roadmap's already-graded findings* into a buildable brief, and its
distinctive output is the **grounding correction** — the two-place record you write when
source has moved on since capture.

## For every site the brief will cite

- **Re-derive the real `file:line`.** Grep/read the actual file the capture pointed at; find
  where the relevant text lives now. Confirm the change the F-site will describe is still the
  right one against current text.
- **Classify the outcome:**
  - **HOLDS** — the site is where the capture said (or trivially shifted); use the fresh
    `file:line` in the F-site. No correction needed.
  - **MOVED / SUPERSEDED** — a later build changed this site (or already shipped part of what
    the capture asked for). This needs a **grounding correction** (below): the capture's
    premise is partly stale, and the brief's scope changes accordingly. Cite what shipped and
    where, and state what's actually left to do.
  - **EXPANDED** — grounding reveals the change belongs at *more* sites than the capture named
    (a convention now has a fifth consumer the capture predates). Add the site to the brief as
    a **grounding addition** and say why it's in scope beyond the filing's letter.

## The grounding correction (two places, always both)

When a site has MOVED/SUPERSEDED such that the roadmap's own note is now wrong, record it in
**both** places — the brief and the roadmap — so the roadmap doesn't keep asserting a stale
premise to the next reader:

1. **In the brief** — mark the affected F-site as a grounding correction, inline: what the
   roadmap/capture assumed, what current source actually shows, and how scope shifts. (The
   precedent is `build-18-durability-cluster.md`'s F3: build-16 had made `vlt-research` a
   `frontmatter@3` consumer, so the roadmap's "vlt-research is a non-consumer today" note was
   stale and research joined the overlay-aware sweep — the F-site says so, marked
   *"grounding correction — now in scope"*.)
2. **In the roadmap** — a short **superseding note** in the roadmap's status/capture section,
   pointing at what shipped and marking the earlier note superseded (the precedent is the
   Arc 3 roadmap's status section carrying exactly such "…is superseded — research joined F3"
   notes). This is an append; never rewrite or delete the original grounded capture — the
   roadmap's capture body is append-only across the cycle's life.

## When a correction is really a block

Most corrections are the brief's to make — source moved, scope tightens, you write it down and
proceed. But if the fresh grounding **contradicts an ideation ruling** (not just a capture
note) — the ruling assumed a state that no longer holds, so following it would build the wrong
thing — that is the owner's to re-rule, not the brief's to reinterpret. Stop and return
`blocked` with the contradiction as the `reason`. Re-deciding a ruling is ideation's job.

Once every site the brief will touch is re-grounded (HOLDS with fresh lines, or corrected with
its two-place record), proceed to `references/brief-anatomy.md` to author the brief.
