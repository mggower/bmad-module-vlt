# Build-1 reader protocol — the mismatch fix moves the prose side and never writes frontmatter

The at-rest instrument for `briefs/build-1-own-writes-read-back.md` acceptance check (3) Writer (F3; Q4).
It is **agent-run**: the writer is prose (`fix-and-file.md` Step 3), so no script implements it; the
protocol is the named instrument and its evidence is two hashes and a line count, recorded below.
The Cycle 15 build-6/7 reader-protocol idiom.

## Given

- The shipped text at a **stated commit**: `skills/vlt-lint/references/fix-and-file.md` Step 3, the
  *Sources-vs-prose* bullet (the writer), and `references/checks.md` *Sources-vs-prose agreement*
  (the direction's single home) — read as shipped, never from memory of the rule.
- The fixture page `build-1-writer-page.md` (three quoted-wikilink `sources:` entries; a prose
  `## Sources` citing two of them), copied to a scratch directory outside the repo before any edit.
- The finding, as a full sweep would hand it to Step 3:
  `sources_vs_prose_mismatches: ["writer-page: frontmatter sources: entry _agent/research/writer-page-gamma missing from the prose Sources section"]`.

## Produce

1. **Before:** `shasum -a 256` over the page's frontmatter block — the bytes from the first line
   through the closing `---` line inclusive (`sed -n '1,/^---$/p'` from line 2, or
   `awk 'NR==1||!done{print} /^---$/&&NR>1{done=1}'`) — and `wc -l` over the `## Sources` section's
   list items.
2. **Apply the finding** exactly as the shipped Step 3 bullet says, in a fresh agent context given only
   the Given above (never this file's run record).
3. **After:** the same two measurements over the edited copy.

## Evidence

- The frontmatter hash **before == after** (the property: frontmatter byte-identical).
- The prose list count **after == before + 1**, the added line rendered in the section's existing form
  (`- [[_agent/research/writer-page-gamma]]`); no prose citation removed.
- Plus the grep-negative of the brief's §Verification 4 over `skills/vlt-lint/` (recorded in the BUILT
  record): no sentence describes a write **into** frontmatter `sources:` on the mismatch path.

**Failability:** run step 2 again with `fix-and-file.md` at the **pre-build commit**
(`git show v0.18.0:skills/vlt-lint/references/fix-and-file.md`), whose Step 3 bullet still carried the
three frontmatter-side sentences (*"member of the existing `sources:` list"*, *"If `sources:` is absent,
create it"*, *"Re-parse the frontmatter"*). A reader that follows that text has a legal frontmatter write
available and may take it — the property is then not guaranteed by the text, which is the defect A16-2
filed. The shipped text closes the route: the only side that moves is prose.

## Run record — 2026-09-16, build-1 working tree (F1–F11 applied on `388bf81`)

A fresh agent (a subagent given only §Given) copied the page to `mktemp -d`, read the shipped Step 3
bullet and `checks.md:16`, and applied the finding.

- **Frontmatter sha256, before:** `851f5dcf2d1e21c2787ce6790f65b936d88f26b74aec9699494874fa8622ceca`
- **Frontmatter sha256, after:**  `851f5dcf2d1e21c2787ce6790f65b936d88f26b74aec9699494874fa8622ceca` — **equal**.
- **Prose `## Sources` list items:** 2 → **3**; the one added line, in the section's existing form:

```
+- [[_agent/research/writer-page-gamma]]
```

- **Which side moves, in the agent's words:** *"the prose section is the side that moves — I relied on 'add the
  frontmatter `sources:` entries the page's prose `## Sources` section omits **to the prose section**' together
  with 'frontmatter is the source of truth and is the side that does not move' and 'This step never writes into
  frontmatter `sources:`' (fix-and-file.md:12; checks.md:16 says the same)."*
- **Grep-negative (brief §Verification 4):** the three exact patterns return 0 over `skills/vlt-lint/`; the
  `never writes into frontmatter` sentence returns exactly 1 (recorded in the BUILT record).

**Observation from the agent, not acted on (an owner call, carried in the BUILT record as note (4)):** the Step 3
preamble (`fix-and-file.md:7`, *bump `last_updated` on any page you substantively edit*) and the attester
paragraph (`:18`, write `verified_by`/`verified_at` on a substantively edited file) both instruct frontmatter
writes, while the mismatch bullet demands the frontmatter block be byte-identical after the edit. The agent
followed the bullet's explicit rule and bumped nothing. A reader who obeyed the preamble instead would change
the frontmatter hash and trip the bullet's own *defect this step caused* clause — the over-reporting direction,
never a silent `sources:` write. Whether a mismatch fix is a *substantive edit* for the preamble, and whether the
invariant should therefore be the `sources:` list rather than the whole block, is the question this leaves to
acceptance (3)'s discharge.
