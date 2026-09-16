---
title: 'Build #1 — read your own writes back: after this ships, a vault owner running `vlt-lint` or `vlt-track` sees the module read its own writes back, instead of a lint that mislocates the heading it was sent for, a sweep that writes a form its own checker rejects, and a slot whose key contradicts its description'
status: 'BUILT 2026-09-16 — on `cycle16-v0.18.1`, F1–F11 landed: `wiki-index.md` states the stub heading in prose at `:80` (`last_updated` 2026-09-16, no `version:` move); `fix-and-file.md:12` loses its three frontmatter-write sentences; `lint-page-facts.py` gains `bare_sources()`, the `--census <dir> [--census-exclude] [--census-line]` entry point and the `--pages` `bareSources`/`sourcesUnparsed` maps; `vlt-lint-full.js` gains the optional `bareSources` arg row, the by-name intake refusal, disposition 3 (`barePathFormClaim`), the narrowed invariant comment, the slot comment and the absent-cap; `lint-report-check.py` gains `--wiki-dir`/`--wiki-exclude`, the sibling import of the census, the recount compare (`bare_path_sources: rendered line does not match the recount`), full-mode usage error 2 and a `census` verdict field; `report.md` gains the `bare_path_sources:` fence line (`# full mode only`), the *Bare-path census reporting* paragraph and the persist-gate clause; `checks.md:15` gains exclusion (c), the narrowed escape sentence, the census and its legal response (R3); `SKILL.md:71` and `full-scale.md` steps 1/3/4 carry the third fact and the census run; the slot is `write-gate` at `capability-template.md:68`, `vlt-track:15`/`:38`, `vlt-upgrade:81`, `module-help.csv:17`; fixtures `build-1-stub-heading-harness.py` + `build-1-wiki-index.overlay.md`, `build-1-census-harness.mjs` + `build-1-wiki/` (29 synthesized pages + an excluded index) + `build-1-expected-census.json`, `build-1-reader-protocol.md` + `build-1-writer-page.md`; Cycle 15 build-5 oracle re-derived (18 top-level / 75 key paths), `build-5-report-ok.yaml` gains the recount line, the shape harness passes `--wiki-dir` to the gate. VERIFICATION: (1) stub harness 8/8 PASS over the shipped file; over `v0.18.0` bytes 6/8 FAIL (reader A and B on base and overlay, the long-form index case, the stated-twice row; the bare index passes coincidentally). (2) census harness: every expectation PASS shipped (phase 1 oracle `57 entries across 23 of 29 pages` deep-equal + the line, one function both callers; phase 2 cases A(a)–(j), B(a)–(c), E, C, D, F; phase 3 gate ok / failed off-by-one / scoped ok / exit 2); over `v0.18.0` workflow 5 FAIL (A(a) the fragment reaches the slot, A(h), B(b) no cap, C and D not refused). (3) warm-safety: `scanFingerprint` `fe29c6f398d02c6b1cdf` on both trees; `git diff v0.18.0 --stat` over the three scanner-read conventions empty; `PAGE_SCAN`/`pageScanPrompt`/`SCANNER_CONVENTIONS` 0 diff lines; `scanModel` default intact (now `:207`); `// depends_on:` unchanged. (4) writer grep-negative over `skills/vlt-lint/`: the three exact patterns 0 hits; `never writes into frontmatter` exactly 1; the loose `write.*frontmatter .sources:.` pattern hits `full-scale.md:20` and `checks.md:16` line-wise — read, neither describes a mismatch-path frontmatter write. (5) slot greps: `non-negotiable-gate` in exactly `vlt-track/SKILL.md:38` + `vlt-upgrade/SKILL.md:81`, both accepted/pre-rename clauses; `write-gate` in the template = 1; persona `non-negotiable\b` counts 2/2/2/2 unchanged from `v0.18.0`; `module-help.csv` 13 columns, 18 rows, Group B PASS. (6) Cycle 15 regression: build-2/3/4 harnesses all expectations hold, build-5 39/39 rows; `grep -c ''## Stubs'' wiki-index.md` = 2. (7) gate live shape: census harness phase 3. (8) `package-lint --expect-version 0.18.0` A/B/C/E PASS (D at release). (9) R2 n/a; R3 stated at `checks.md:15`; R4 n/a. (10) scrub: synthesized pages, placeholder paths only. Reader protocol (acceptance (3), at rest): a fresh agent over the shipped Step 3 — frontmatter sha256 `851f5dcf…ceca` before == after, prose list 2 → 3, the added line `- [[_agent/research/writer-page-gamma]]` (run record in the protocol file). No `.decision-log.md` on disk. Deviations/notes: (1) Cycle 15 `build-4-expected-facts.json` extended with the two new keys (hand-verified: `seattle-seahawks` 1, the rest 0, `sourcesUnparsed` []) — its harness deep-compares the whole `--pages` output, so F4 additive keys broke it; the harness code is unchanged. (2) `build-5-shape-harness.py` row 7a literal 74 → 75 key paths; `--wiki-dir` passed to the gate call and the bare-`python3` probe only — the walker takes no such flag. (3) `package-lint` forced two wording moves off the brief text: `checks.md:15` F8 phrase `frontmatter@14 consumer` → `{conventions}/frontmatter.md consumer` (Group E stray-pin), and `SKILL.md` Step 6 trimmed to 11,970 bytes (Group C 12,000-byte router budget; `v0.18.0` sat at 11,984) — the census clause shortened, one `report.md`-homed parenthetical and one `full-scale.md`-homed clause replaced by pointers. (4) NOTED, not built: the fresh agent observed that Step 3 preamble (`fix-and-file.md:7`, bump `last_updated` on a substantive edit) and the attester paragraph (`:18`) instruct frontmatter writes while the F3 bullet demands a byte-identical frontmatter block; it followed the bullet. Owner call at acceptance (3): whether a mismatch fix is a substantive edit for the preamble — if so the invariant is the `sources:` list, not the whole block; meanwhile the failure direction is over-reporting (a tripped clause, never a silent `sources:` write).'
module_code: 'vlt'
created: '2026-09-16'
derives_from:
  - 'factory/inbox/2026-09-03-124500-stub-heading-is-stated-inside-a-fence-so-a-faithful-section-scan-reads-located-no.md (A16-1 — the heading-inside-a-fence gap, directions 1 (convention-side, Q1 (a)) and 3 (the convention-side fixture, Q2); the filing''s second observation is REFUTED at capture and builds nothing)'
  - 'factory/inbox/2026-09-03-124600-lint-sources-reconciliation-writes-the-retired-bare-path-form.md (A16-2 — direction 1 the writer states the form (Q4), direction 2 the checker''s posture: census line, class leaves `malformed_frontmatter` (Q3 (a)); direction 3 is the vault''s (Q5 LEAVE))'
  - 'factory/inbox/2026-09-09-184840-rename-the-loop-profile-slot-non-negotiable-gate-to-write-gate.md (A16-8 — all four residual-scope items, with the alias indefinite (Q20) and no upgrade offer (Q21))'
roadmap: 'factory/cycles/16-closed-loops/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-09-16), build-1 `binds:` Q1 (a) convention-side, Q2 SHIP the fixture, Q3 (a) census line + class drop, Q4 SHIP the writer repair, Q5 LEAVE the 55, Q20 INDEFINITE alias, Q21 CHANGELOG notice only, D5 ONE-OFF fixture, E1 NOT BLOCKING, E2 DISCHARGED BY Q3 (a) (attached here), E3 OBLIGATION ON THE BRIEF (read, §Brief-time disposition 9); roundtable A9 (the line''s shape and gate; the reduce-side enforcement point), A10 (build 1 ships alone first, v0.18.x), A17 (notice text in §8; the A16-8 notice says delete the apology, old key accepted indefinitely), obsolescence beat build-1 row; the A9/A10 constraint in the build-1 bullet'
risk: 'low-moderate — no convention `version:` moves and no consumer walk is owed (`wiki-index.md` takes a prose clarification; `frontmatter@14` is untouched); the one moderate-risk site is the fan-out reduce (`vlt-lint-full.js`), where a third refusal disposition narrows the `unclassified` escape member — bounded to a byte-derived page fact and exercised by an at-rest harness proven failable against v0.18.0. The release must leave every cache-key input byte-identical (A9/A10) — verified at rest, §Verification 3.'
---

# Build #1 — read your own writes back

## Intent

Three at-rest fixes inside `vlt-lint`, `vlt-mint`, `vlt-track` and `vlt-upgrade`, each a loop whose
only reader was the hand that wrote it (roadmap §The through-line; captures A16-1, A16-2, A16-8):

- **A16-1** — the stub-registry read's input, `wiki-index.md` §The Stubs section, states the heading it
  wants matched only *inside* a fenced example, so a faithful section scan terminates on the very line it
  was sent to read and reports `located: no`. The convention says the heading outside the fence (Q1 (a)),
  and the read gets a fixture on the convention's side of the seam (Q2, D5 one-off).
- **A16-2** — the lint's own sweep wrote 55 `sources:` entries in a form the convention had retired, the
  fix mechanics at `fix-and-file.md:12` still half-describe that write, and the checker flagged one of the
  55 because rule 4's legality is indexed on write date, which no byte carries. The writer loses its
  frontmatter-write residue (Q4); the bare-path class leaves `malformed_frontmatter` and surfaces as one
  denominated, script-derived, gate-checked census line (Q3 (a), A9). The 55 stay the vault's (Q5).
- **A16-8** — the loop-profile slot's key (`non-negotiable-gate`) contradicts its own description (*method
  gate, re-asserted at the write*); five wearers re-explain the mismatch inside their profiles. The key
  becomes `write-gate`, the old key stays accepted indefinitely (Q20), the relocation scan accepts both,
  and the CHANGELOG notice tells wearers to delete the apology (A17).

This build is **v0.18.1, alone** (roundtable A10): it must touch none of the findings cache's key inputs
so that Cycle 15's build-2 (6) *first warm release* watch gets its one chance — §Verification 3 proves it
at rest; §Acceptance (5) carries it.

**All rejected alternatives in the parent filings are settled — do not re-litigate.** In particular: the
`[[wikilink]]`-stubs tolerance A16-1's second observation asked for (refuted at capture — the live index
conforms to `wiki-index.md:88`); the procedure-side fence-aware read (Q1 (b), rejected — "a workaround for
a document that should just say the heading"); a reduce-side refusal by name for the bare-path class (Q3
(b), rejected — the class is unobservable at rest, so it is not a per-page finding at all); a one-release
alias sunset (Q20); a human-gated wearer-rename offer (Q21); an owner-ruled backfill exception for the 55
(Q5).

## Brief-time dispositions

The roadmap left exactly three questions to this brief (§Questions deliberately left to brief time,
build-1 row); dispositions 1–3 answer them. Dispositions 4–11 record the judgment calls the grounding pass
and the F-sites forced.

1. **The census line's exact report field — `flag_for_human.bare_path_sources`, a scalar, `# full mode
   only`, pasted verbatim from the script.** It sits directly after `attestation_census:` in `report.md`'s
   fence (the idiom Q3 (a) cites), typed scalar, and carries the marker so `lint-report-check.py`'s grammar
   mandates it in full mode and permits its absence in scoped mode (A9: *scoped mode's denominator changes
   every run*). Of A9's two offered scoped-mode forms — the marker, or the `not instrumented (scoped run)`
   literal `scanner_return_rejected` renders — the marker is chosen: `scanner_return_rejected` is a
   both-modes key that needs a literal to stay typed; `attestation_census` is the full-mode-only precedent
   and is absent in scoped mode, and the census follows it. The value is the **whole line the script
   prints**, three-term as ruled plus the instrument clause the `para_scan:` idiom already carries:
   `N entries across P of M pages — sources: scalars unquoted and ending .md (instrument: scripts/lint-page-facts.py --census)`.
   The wording names the **form**, never legality — the fact bytes carry is that an entry is an unquoted
   scalar ending `.md`; whether it was written before or after 2026-08-15 is exactly what nobody can read.
2. **The reduce-side drop mechanism — a third refusal disposition, keyed on a script-derived page fact
   and the returned verdict's field list, under the A9/A10 constraint.** `PAGE_SCAN`, `pageScanPrompt`,
   `SCANNER_CONVENTIONS` and the `scanModel` default are **not edited**. The scanner keeps returning what it
   returns; the reduce refuses one exact shape: `frontmatter_defect === 'unclassified'` **and**
   `frontmatter_defect_fields` is exactly `['sources']` **and** the new byte-derived map `bareSources[slug]`
   is an integer `> 0`. A bare-path complaint arrives `unclassified` (`vlt-lint-full.js:1067` today, and the
   filing's own fragment — *"unclassified frontmatter defect: YAML rule 1 & rule 4 violation"* with
   `sources` its field); it is refused because the page's `sources:` list, read from bytes, carries the
   form the census already counts — so refusing removes a **duplicate of a denominated fact**, never a
   fact (disposition 1's asymmetry, not disposition 2's). Nothing about complaint wording enters the test.
   The existing helper `whollyWithin` **cannot express this** — it rejects any list naming a page-required
   key, and `sources` is one (`PAGE_REQUIRED_FRONTMATTER`, `:917`) — so the predicate is written out
   (F5). The escape member's invariant ("`unclassified` … always reports", `:892-893`, `:1067`,
   `checks.md:15`) is **narrowed, and every site that states it says so** — a byte-gated exception is not
   a wording exception, and the failure direction stays over-reporting: a page whose `sources:` is not a
   parseable list has no `bareSources` entry and its complaint reports (disposition 4).
3. **Cycle 15 build-3 check (4)'s `grep -c '## Stubs' wiki-index.md` moves from 1 to 2 — expected, noted,
   not a regression.** Q1 (a) states the heading in prose at `:80` as an inline code span; the fenced
   example at `:83` keeps its copy. The count is 2 by construction; §Acceptance (1) carries the new
   expectation so a later reader does not "discover" a doubled heading. This is the one place the heading
   is stated twice on purpose: prose (the rule) and example (the illustration) — `report.md:17` and
   `checks.md:13` point at the convention and restate nothing.
4. **`bareSources` is an optional byte-fact arg, not a cache-key term, and a non-list `sources:` yields
   no entry.** It rides beside `pageLinks`/`summaryLengths` in the args contract (`vlt-lint-full.js:87-99`):
   `{slug: int}`, derived by `scripts/lint-page-facts.py` from the page's bytes, recomputed every run,
   **never a cache-key term** (D4's reasoning — the reduce re-runs over cached scans with fresh facts).
   Unlike the two required maps it is **optional**: absent → the third disposition is inert and the reduce
   names it on `coverage_caps` (*`bareSources absent — bare-path `sources:` complaints report unrefused`*);
   present-and-wrong-type (the map, or an entry for a listed page) → refused pre-dispatch by name, the
   `pageLinks[<slug>]` grammar. Optional because the three Cycle 15 harnesses build their args without it
   and must keep passing (regression, §Verification 6), and because absence degrades in the honest
   direction. **A page whose `sources:` is not a list** (a scalar, a block scalar, an unparseable block) is
   **absent from the map** — the script reports it under `sourcesUnparsed: [slug]` — so a complaint about
   such a page can never be refused as "the census has it": the census counts only what it could parse.
5. **The census walks the directory itself; the gate recounts by the same function.** `lint-page-facts.py`
   gains a second entry point, `--census <wiki-dir> [--census-exclude <path> …]`, which walks `*.md` under
   the directory recursively (the `lint-para-facts.py` walk idiom, `:192-233`), skips excluded paths (the
   SKILL passes `{index}`), and prints the line of disposition 1 (`--census-line`) or the JSON
   `{bareSources, sourcesUnparsed, counts: {N, P, M}}`. The `--pages` mode gains the same per-page map in
   its existing JSON output (`bareSources`, `sourcesUnparsed`) for the reduce. **One function,
   `bare_sources(text)`, both callers.** `lint-report-check.py` imports the script by sibling path (as it
   imports the walker, `:311-316`), takes `--wiki-dir <path>` and repeatable `--wiki-exclude <path>`, and
   compares the report's `bare_path_sources:` scalar **by string equality** to the recount — the
   `para_scan:` idiom (`:291-296`), reason `bare_path_sources: rendered line does not match the recount`.
   Under `--mode full`, `--wiki-dir` is **required** (usage error 2 without it, like a missing `--dir`);
   under `--mode scoped` it is ignored. M is the walked count; P and N are what the `--census` walk finds;
   the SKILL's `files_listed` is a different number by design (it excludes unreadable pages the census
   still walks) and the two are never compared.
6. **The bare-path form, stated once, in the script's docstring.** A `sources:` **entry** is an item of the
   frontmatter `sources:` key's YAML sequence — block form (`- <value>` lines following the key) or flow
   form (`[a, b]` on the key line). An entry is **bare-path form** iff its value, after a trailing
   ` #comment` is stripped, does not begin with `"` or `'`, does not begin with `[[`, and ends with `.md`.
   Everything else — quoted wikilinks, URLs, quoted paths, entries without `.md` — is not counted. Only
   the `sources:` key counts: `grounding:`, `personalization_sources:`, `artifacts:` and any prose
   `## Sources` section are never read (the fixture plants each as a control). The frontmatter block is the
   one `lint-page-facts.py` already delimits (`frontmatter_lines`, `:103-115`).
7. **`vlt-track/SKILL.md:15`'s framing changes with the key; `module-help.csv:17` follows it.** Capture
   left `:15` "considered with" the rename; the sentence is the conflation itself — *"brings the voice and
   the non-negotiable"* names the method gate by the persona-section word. It becomes *"brings the voice
   and the write-gate"*, with one clause stating that the write-gate is *often, not always* the partner's
   non-negotiable (the football-analyst profile shows them coinciding; the career-strategist profile shows
   them apart — both from the capture, neither named in shipped text). The persona sections `## Your
   non-negotiable` (three shipped partners, the mint template, contract `:246`) are a **different concept
   and are not touched** — that distinction is the point of the rename. `module-help.csv:17` repeats the
   `:15` phrase in `vlt-track`'s description (grounding addition, F9) and takes the same one-word edit,
   quoted as it already is.
8. **The alias is a sentence, not a parser.** No shipped reader parses loop-profile keys (capture: `grep`
   over `vlt-lint/` and `vlt-setup/assets/hooks/` returns nothing; `vlt-track:38` binds by description).
   So "accepts `non-negotiable-gate`" is one clause at `vlt-track:38` and one list item at
   `vlt-upgrade:81` — no code, no lint finding, no `capability_issues` member. A later cycle that adds a
   profile-key reader inherits the alias from those two sentences.
9. **E3 — Cycle 15 carry 9 read before scoping the reduce edit.** The carry (C15 roadmap, discharge
   passes 2–3 and the operator frictions list): `fix_now.sources_vs_prose_mismatches` was refused wholesale
   by the Librarian on three consecutive full sweeps (7, then 2 entries; `carbon-steel-seasoning`,
   `nfl-2026-draft-first-round` on the second), each refusal evicting the page's cache record; `{backlog}`
   carries a standing human ruling on four pages — a **tier question** (does the class belong at `fix_now`
   at all). It touches the **same reduce** as Q3 but a **different slot**: the sources-vs-prose verdict
   split (`:1076`) and its `fix_now` routing are **not edited here** — this build's reduce edit is confined
   to `malformed_frontmatter`, and its writer edit (F3) removes a residue without moving the tier. The
   interaction is named, not built: F3's grep-negative (§Verification 4) makes the writer's direction
   unambiguous, which is the precondition any tier ruling on the carry needs; the ruling itself stays an
   owner filing (Cycle 15 carry 9, still unfiled).
10. **R1 — Interim posture: not applicable.** Every rule this build states ships with its mechanism in
    the same release: the census line with its script and gate; the class drop with its reduce
    disposition; the heading statement with its fixture; the alias with the two sentences that are its
    whole mechanism.
11. **Retirement (P-15) — substantive, three retirements and one deliberate non-retirement, per the
    obsolescence beat's build-1 row:** (i) the bare-path `sources:` form **leaves `malformed_frontmatter`'s
    finding population** — `checks.md:15`'s catalog of what the slot reports narrows and names the census
    as the form's only surface; the reduce refuses it (F5); (ii) `fix-and-file.md:12`'s frontmatter-write
    residue is **deleted, not re-caveated** (F3) — the three sentences that only made sense for a write
    `checks.md:16` says never happens; (iii) Cycle 15 build-3 check (4)'s `grep -c '## Stubs'` = 1 is
    **obsoleted** (disposition 3). **Deliberate non-retirement:** `non-negotiable-gate` survives as an
    accepted spelling **indefinitely** (Q20) — recorded here so no later cycle "discovers" a second
    spelling and files it. Not retired and still standing, by design: the `vlt-lint-full.js:297/:299`
    prompt-side statements (untouched under A9/A10 — the capture-don't-interrupt item files only if a
    build takes the forbidden route; this one does not).

## F-sites

Every site re-grounded 2026-09-16 against the working tree at `601b09b`, which is byte-identical to
`v0.18.0` for every file below (`git diff --stat v0.18.0 -- <paths>` empty). Line numbers are current.

### F1 — `skills/vlt-setup/assets/governance/_meta/conventions/wiki-index.md` — the heading stated outside the fence (Q1 (a))

**Current state — HOLDS.** `:78` `## The Stubs section`; `:80` *"A page may link to a concept with no page
yet. Catalog these under a trailing section so the gap is visible:"*; `:82` ```` ```markdown ```` opens;
`:83` `## Stubs (linked, not yet written)`; `:86` fence closes; `:88` the backtick-slug rule. The heading is
stated nowhere outside the fence. Frontmatter `version: 2`, `consumers: [vlt-ingest, vlt-lint,
vlt-lint-full.js]` (`:10-11`). **Not a scanner-read convention** (`SCANNER_CONVENTIONS`,
`vlt-lint-full.js:290`), so its bytes are not a cache-key input.

**Change — one sentence at `:80`, prose only.** Replace the `:80` sentence with:

> A page may link to a concept with no page yet. Catalog these under a trailing section whose heading is
> **`## Stubs (linked, not yet written)`** — the heading text is stated here, in this sentence, and a reader
> takes it from here; the fenced block below is an example of the section, not the statement of its
> heading:

The fence and its contents (`:82-86`) are unchanged. `last_updated:` (`:4`) is bumped to the build date.
**No `version:` bump, no consumer re-ack** — a prose clarification (CLAUDE.md, version-handshake rule).

**Why.** A16-1's gap: the read `checks.md:13` prescribes has its input in a form that ends the scan on the
line it wants. Q1 ruled the convention was the ambiguous thing.

**Out of scope here.** `checks.md:13` and `report.md:17` already say *the heading as the convention states
it, overlay-merged* — untouched. The `[[wikilinks]]`-in-stubs tolerance is refuted, not built.

### F2 — `factory/cycles/16-closed-loops/fixtures/build-1-stub-heading-harness.py` + `build-1-wiki-index.overlay.md` — the convention-side fixture (Q2, D5)

**Current state.** No fixture exists on the convention side of the read; Cycle 15's pair
`fixtures/build-3-index-stubs.md` / `build-3-index-bare-stubs.md` grades the index side only (three slugs
under the long-form heading; the same three under bare `## Stubs`).

**Change — new harness, reads the shipped convention by path, never a copy.** The harness:

- **Reader A (fence-naive section scan — the read that broke):** from the line `## The Stubs section` to
  the next line matching `^## ` — *whatever it is, fenced or not* — take the first inline code span whose
  text begins `## ` and return the text after `## `. Under v0.18.0 bytes the scan ends at `:83` and finds
  no span → **none** (the failing read, reproduced). Under F1's bytes the span at `:80` is found first →
  `Stubs (linked, not yet written)`.
- **Reader B (fence-aware):** strip fenced blocks over the whole file first (the `strip_code` semantics of
  `lint-page-facts.py:80-96`, inline spans kept), then the same section scan. Under v0.18.0 → **none** (no
  prose statement exists); under F1 → the heading.
- **Overlay case:** merge the shipped base with `build-1-wiki-index.overlay.md` (base bytes, newline,
  overlay bytes — the merge order `full-scale.md` step 2 states) where the overlay appends one bullet to
  §The Stubs section (an append-only vault addition, e.g. a local stub-aging rule). Both readers still
  return the heading.
- **Index side, end to end:** apply the returned heading to the Cycle 15 index pair — `build-3-index-stubs.md`
  → `located: yes, 3 slugs`; `build-3-index-bare-stubs.md` → `located: no, 0 slugs` — using the collection
  rule at `checks.md:13` (backtick-wrapped slugs in list items up to the next `## `).
- **Failability:** `--convention <path>` runs the same table over another copy; the builder runs it over
  `git show v0.18.0:skills/vlt-setup/assets/governance/_meta/conventions/wiki-index.md` and records the
  FAIL count in the BUILT record (expected: both readers FAIL on the heading, index cases FAIL by
  consequence).

Exit 0 when every expectation holds, 1 otherwise; `uv run`, falling back to `python3`, no dependency.

**Why.** Q2: *it is the only check on the side that broke.* The instrument-beat property: *a fixture that
is a copy of the convention is not the instrument* — hence read-by-path.

### F3 — `skills/vlt-lint/references/fix-and-file.md:12` — the writer states the direction and never writes frontmatter (Q4)

**Current state — HOLDS.** `:12` opens prose-side (*"add the frontmatter `sources:` entries the page's
prose `## Sources` section omits, in the section's existing form"*) then carries three frontmatter-side
sentences: *"Each added entry is a **member of the existing `sources:` list** — never a new top-level
frontmatter key, and never a bare list item outside `sources:`. If `sources:` is absent, create it as a
list rather than writing loose items. **Re-parse the frontmatter after the edit**: a page whose frontmatter
no longer parses is a defect this step caused, not a finding it cleared."* `checks.md:16` (the direction's
single home) is unambiguous: the prose section is the side that moves.

**Change — replace the bullet body with:**

> **Sources-vs-prose (`sources_vs_prose_mismatches` only)** — add the frontmatter `sources:` entries the
> page's prose `## Sources` section omits **to the prose section**, in the section's existing form.
> **Add only; never remove a prose citation to make the two sides agree. This step never writes into
> frontmatter `sources:`** — frontmatter is the source of truth and is the side that does not move
> (`checks.md`, *Sources-vs-prose agreement*, the direction's single home); each prose line added cites the
> frontmatter entry's path, rendered as the section already renders its entries. **Re-read the page after
> the edit: its frontmatter block is byte-identical to before** — a changed frontmatter is a defect this
> step caused, not a finding it cleared. The `flag_for_human` half (`sources_vs_prose_unresolved`) is
> **not** auto-fixed — the direction test and both legal responses live at `checks.md`, *Sources-vs-prose
> agreement*.

The three frontmatter-side sentences are **deleted** (retirement (ii)); nothing states rule 4's form here
because no frontmatter write exists on this path to need it.

**Why.** A16-2 direction 1 — *the enforcement point for rule 4's form is the writer, and only the writer*;
the residue is the surviving half of the pre-`5122aa1` direction that produced the 55.

### F4 — `skills/vlt-lint/scripts/lint-page-facts.py` — the bare-path fact and the census (Q3 (a), A9)

**Current state — grounding correction (the roundtable's premise is stale).** A9 records that the script
*"already parses the frontmatter block and rule 4's form, `:43`"*. It does not: `:42-44` is a docstring
remark that a quoted `"[[path]]"` `sources:` entry is a **link** (frontmatter scanned like body text for
`[[ ]]`); the script delimits the frontmatter block (`frontmatter_lines`, `:103-115`) and parses only the
`summary:` scalar (`:150-172`). No `sources:` entry is read, and no form is classified. The ruling — the
census is *computed script-side by `lint-page-facts.py`* — stands; the script gains the parser this build.
Recorded in the roadmap as a superseding note under Q3.

**Change.**

- `bare_sources(text)` → `(count: int | None, unparsed: bool)` per disposition 6, over the frontmatter
  block only. `None`/`unparsed=True` when `sources:` is absent-as-a-list (a scalar value, a block-scalar
  indicator, no closing delimiter). `sources: []` → `0`.
- `--pages` mode: the JSON gains `"bareSources": {slug: int}` (only pages with a parsed list) and
  `"sourcesUnparsed": [slug, …]`. `pageLinks`/`summaryLengths`/`unreadable`/`pages` unchanged.
- `--census <dir>` (+ repeatable `--census-exclude <path>`): walks `*.md` recursively (the
  `lint-para-facts.py:192-233` idiom — `os.walk`, sorted, excluded subtrees pruned, unreadable files
  counted in M with no entries), and emits `{bareSources, sourcesUnparsed, counts: {N, P, M}}`; with
  `--census-line`, prints disposition 1's line only. `--pages` and `--census` are mutually exclusive.
- Docstring: the FORM statement of disposition 6, the *facts never verdicts* sentence extended — *the
  script reports a form; legality under rule 4 is write-dated and no byte carries it, which is why this is
  a census and never a per-page verdict* — and the two callers named (the SKILL's Step 1/5 run; the gate's
  recount).

**Why.** Q3 (a) and A9: script-side, never from scanner returns; the enforcement point for the class drop
(F5) needs the per-page fact; the gate (F6) needs the recount.

### F5 — `skills/vlt-setup/assets/workflows/vlt-lint-full.js` — the reduce-side enforcement point (Q3 (a), A9, disposition 2)

**Current state — HOLDS.** Args contract rows `:87-99` (`pageLinks`, `summaryLengths`); intake guard
`:156-170` (present-and-wrong-type refused by name; absent entries not refused); `PAGE_REQUIRED_FRONTMATTER`
`:917` names `sources`; `whollyWithin` `:934-937`; dispositions 1 and 2 `:944-953`;
`refusedFrontmatterClaim` `:954`; the invariant comment `:890-897` ("`unclassified` … never refused by
either disposition"); the slot `:1064-1070` with its comment `:1067`; `SCANNER_CONVENTIONS` `:290`,
`pageScanPrompt` `:296-299`, `PAGE_SCAN` `:222-250`, `scanFingerprint` `:315-316`, `scanModel` default
`:183` — **all four untouched by this build.**

**Change — confined to the args contract, the intake guard, the guard block and the slot.**

- Args row after `summaryLengths` (`:99`): `bareSources: {slug: int} (optional)` — derived from bytes by
  `lint-page-facts.py`; NOT a cache-key term; absent → the bare-path refusal is inert and `coverage_caps`
  says so; present-and-wrong-type (the map, or an entry for a listed page: not a non-negative integer)
  → refused pre-dispatch by name (`bareSources[<slug>]`). Also the header's `pageLinks`/`summaryLengths`
  paragraph (`:59-62`) names the third fact in one clause.
- Intake (`:160-170` idiom): `wrongTypeSlots` entries for `bareSources` / `bareSources[<slug>]`; `const
  bareSources = isPlainObject(a.bareSources) ? a.bareSources : null` (null = absent, distinct from `{}`).
- Guard block (`:938-954`): a third disposition —
  ```js
  // Disposition 3 — the bare-path form (Cycle 16 build-1, Q3 (a)). A complaint that a sources: entry is
  // in the unquoted `.md` form is refused ONLY when the page's own bytes carry that form (bareSources,
  // derived by lint-page-facts.py) — the form is counted once, denominated, on bare_path_sources:, and
  // its legality is write-dated, which no byte carries. Like disposition 1 this removes a DUPLICATE of a
  // fact the report carries elsewhere; unlike it, the fact is byte-derived, never a scanner return.
  // Wording never enters the test: the verdict kind and the bare field list are machine-shaped.
  const barePathFormClaim = (s) =>
    bareSources !== null && s.frontmatter_defect === 'unclassified' &&
    Array.isArray(s.frontmatter_defect_fields) && s.frontmatter_defect_fields.length === 1 &&
    s.frontmatter_defect_fields[0] === 'sources' &&
    Number.isInteger(bareSources[s.slug]) && bareSources[s.slug] > 0
  const refusedFrontmatterClaim = (s) => attestationOnlyComplaint(s) || inventedRequirement(s) || barePathFormClaim(s)
  ```
  The invariant comment (`:890-897`) is rewritten to state the narrowing: `unclassified` always reports
  **except** the one byte-gated shape above; `malformed_block` is never refused; the failure direction
  stays over-reporting because a page with no parsed `sources:` list has no `bareSources` entry.
- Slot comment (`:1064-1067`): names the third disposition.
- `coverage_caps`: when `bareSources === null`, push *`bareSources absent — bare-path sources: complaints
  report unrefused; bare_path_sources: is the SKILL's census, unaffected`*.
- `// depends_on:` (`:11`) **unchanged** — no convention moved. **`scanFingerprint` unchanged by
  construction** (prompt and schema untouched) — §Verification 3 measures it.

**Why.** A9: the drop *has no reduce-side enforcement point as ruled* — a bare-path complaint arrives
`unclassified`, which the reduce never refuses; the point must be keyed on script-derived page facts and
never a new scanner verdict kind, so `PAGE_SCAN` stays byte-identical.

### F6 — `skills/vlt-lint/scripts/lint-report-check.py` — the recount gate (A9)

**Current state — HOLDS.** `SCAN_KEY`/`WRITER_SCAN_KEY` `:93-94`; the string-equality loop `:291-296`;
walker import by sibling path `:311-316`; `cmd_check` `:335-381` (`--mode`/`--dir` required for a report);
reason vocabulary in the docstring `:55-59`; `SCHEMA_FLOOR = 18` `:85` (a floor — stays).

**Change.** `CENSUS_KEY = "bare_path_sources"`; args `--wiki-dir` and repeatable `--wiki-exclude`;
under `--mode full` a missing `--wiki-dir` is usage error 2 (like a missing `--dir`); `load_page_facts()`
imports `lint-page-facts.py` by sibling path and calls its census walk; the equality loop gains the census
key against the recount line (the key may be absent under `--mode scoped`; when present in scoped mode it
is checked only if `--wiki-dir` was given, else ignored — scoped mode composes no census); reason
`bare_path_sources: rendered line does not match the recount`; docstring's WHAT `check` VERIFIES and
REASON VOCABULARY lists gain one row each. The verdict object gains `"census": {N, P, M}` beside `walk`.

**Why.** A9: *an inline map's children are not validated (`report.md:9` rule 2), so without this the census
is a self-reported number.* The scalar is compared whole, like `para_scan:`.

### F7 — `skills/vlt-lint/references/report.md` — the key, its paragraph, the gate paragraph

**Current state — HOLDS.** Fence `:11-86`; `attestation_census:` `:39` (`# full mode only`); `para_scan:`
`:40`; *Persist-gate reporting* `:104` names the two string-equality compares.

**Change.**

- Fence, new line directly after `:39`:
  `  bare_path_sources: <N entries across P of M pages — sources: scalars unquoted and ending .md (instrument: scripts/lint-page-facts.py --census)>   # full mode only — the denominated bare-path census over {wiki} (checks.md, Malformed frontmatter, exclusion (c)); pasted from the script's --census-line verbatim; Step 6 recounts and compares this string; legality is write-dated and not derivable — never a per-page finding`
- New paragraph after *Write-posture reporting* (`:100`): **Bare-path census reporting.** — pasted
  verbatim from `scripts/lint-page-facts.py --census {wiki} --census-exclude {index} --census-line`, full
  mode only, both numbers from the walk; the line's job is *never rises* — its baseline and floor are the
  vault's to know (a vault carrying pre-adoption entries has a floor above zero under rule 4's no-backfill
  clause, and a fall is not evidence of repair, since a substantive edit adopts the form legally); a rise
  between two full sweeps names a writer that emitted the form after adoption. Per the honest-reporting
  rule — read it there.
- *Persist-gate reporting* (`:104`): one clause — *and, in full mode, the `bare_path_sources:` scalar
  equal by string equality to the recount `scripts/lint-page-facts.py --census` prints for `{wiki}`*.

**Why.** *Nothing else states the key set; a line added here is a line validated there* (`:9`).

### F8 — `skills/vlt-lint/references/checks.md:15` — exclusion (c), the census, the legal response (R3)

**Current state — HOLDS.** `:15` (Malformed frontmatter): *"Two exclusions, enforced at the reduce …"*,
(a) and (b), then *"A defect the scanner cannot classify is returned as `unclassified` and always
reports"*. `:13` (stub read), `:16` (sources direction), `:17` (attestation census idiom — the capture's
`:18` sits inside this bullet; trivially shifted) — untouched.

**Change — inside `:15`.** *"Two exclusions"* → *"Three exclusions"*; add **(c) the bare-path form** —
an `unclassified` verdict whose field list is exactly `sources`, on a page whose frontmatter `sources:`
list, read from bytes by `scripts/lint-page-facts.py`, carries at least one entry in the unquoted `.md`
form — is refused: the form is **counted once, denominated, on the full-mode `bare_path_sources:` census
line** (`report.md`), never listed per page, because rule 4's legality is indexed on write date
(`{conventions}/frontmatter.md` rule 4, *Coexistence posture*) and no byte carries it — a per-page flag on
this class could only be arbitrary. The escape sentence narrows: *`unclassified` always reports, with the
one byte-gated exception (c); a page whose `sources:` is not a parseable list has no byte fact and its
complaint reports.* **The bare-path census (full mode):** one denominated line over `{wiki}`, script-side.
**Legal response (the census line):** informational and denominated; the number's job is *never rises* —
a rise between full sweeps names a writer emitting the form after adoption, and the writer is the
enforcement point (`fix-and-file.md` Step 3 never writes frontmatter `sources:`; every other writer is a
`frontmatter@14` consumer acked to rule 4); post-adoption entries are the vault's to repair by hand at the
owner's cadence, never by sweep (rule 4's no-backfill clause).

**Why.** Q3 (a) (the retirement's catalog site) and R3 (a finding class's legal response lives at the
check's single home).

### F9 — `skills/vlt-lint/SKILL.md:71` + `references/full-scale.md` steps 1, 3, 4 — the SKILL's two calls

**Current state — HOLDS.** `SKILL.md:71` the gate command (`--dir` ×3, `--exclude {wiki}`, `--root`);
`full-scale.md:7` step 1 runs `lint-page-facts.py --pages` and passes the two maps *as returned*; `:9`
step 3's args list; `:19` step 4's re-render list names the two maps.

**Change.** `SKILL.md:71`: append `--wiki-dir {wiki} --wiki-exclude {index}`; the sentence after it names
the census recount beside the walk. `full-scale.md:7`: pass the script's `bareSources` map as returned (a
third fact, same posture); **and** run `--census {wiki} --census-exclude {index} --census-line` for the
Step-5 `bare_path_sources:` line — pasted verbatim, full mode only. `:9`: `bareSources` joins the args
list (~146 more integers on the wrapper — negligible). `:19`: the re-render list names `bareSources`.

### F10 — `skills/vlt-mint/assets/capability-template.md:68`, `skills/vlt-track/SKILL.md:15`/`:38`, `skills/vlt-upgrade/SKILL.md:81`, `skills/vlt-setup/assets/module-help.csv:17` — the slot (A16-8)

**Current state — HOLDS at every capture site; one site added.** `capability-template.md:68`
`- non-negotiable-gate: <this partner's named method gate — re-asserted at the write, e.g. least-intrusive / never past the evidence>`.
`vlt-track/SKILL.md:15` *"**The calling partner brings the voice and the non-negotiable.**"*; `:38` *"the
**non-negotiable gate** — the calling partner's specific method gate, named in its profile … Apply it at
the design beat **and** re-assert it at the write"*. `vlt-upgrade/SKILL.md:81` the relocation scan's key
list `root` / `target` / `subject-model` / `data-streams` / `log-tag` / `non-negotiable-gate`.
**Grounding addition:** `module-help.csv:17` (`vlt-track`'s description) — *"bringing the voice and the
non-negotiable"* — repeats `:15`'s phrase. `grep -rn 'non-negotiable-gate' skills/` today: exactly those
three files (`capability-template.md`, `vlt-track/SKILL.md`, `vlt-upgrade/SKILL.md`). The persona
sections `## Your non-negotiable` (`vlt-agent-{librarian,creative,researcher}/SKILL.md:12`,
`partner-agent-template.md:27`) are the other concept — **untouched**. `vlt-track` `depends_on:
["extraction@10", "wiki-supersession@2"]` — no handshake involved.

**Change.**

- `:68` → `- write-gate: <this partner's named method gate — re-asserted at the write, e.g. least-intrusive / never past the evidence>` (description unchanged — it was already right).
- `vlt-track:38` → *"the **write-gate** (profile key `write-gate`; the pre-rename key `non-negotiable-gate`
  is accepted indefinitely — nothing parses the key, so no wearer need rename) — the calling partner's
  specific method gate, named in its profile …"* rest unchanged.
- `vlt-track:15` → *"**The calling partner brings the voice and the write-gate.** … the method must be
  least-intrusive; … must never run past the evidence. The write-gate is often — not always — the
  partner's own non-negotiable; the profile names it either way. The loop is the same; the partner colors
  it."*
- `vlt-upgrade:81` → `… / log-tag / write-gate (or its pre-rename spelling non-negotiable-gate — both recognized, indefinitely)`.
- `module-help.csv:17` → `bringing the voice and the write-gate` — the field stays double-quoted (CLAUDE.md
  csv rule); `merge-help-csv.py` is not touched.

**Why.** A16-8 residual scope 1–3 with Q20/Q21; disposition 7 for `:15` and the csv.

### F11 — Cycle 15 fixtures touched by this build (regression, not scope)

`fixtures/build-5-expected-schema.json` is **re-derived** (`lint-report-check.py schema >` it) because
F7 edits the fence — the harness's own instruction (`lint-report-check.py:65-66`); `build-5-report-ok.yaml`
gains the `bare_path_sources:` line whose value is the recount over `build-5-para/resources/wiki/`;
`build-5-shape-harness.py:79-81` passes `--wiki-dir <build-5-para>/resources/wiki` in full mode. Nothing
else in Cycle 15's fixtures is edited; `build-2/3/4` harnesses must pass unchanged (§Verification 6).

## Registration

**None.** No new skill, workflow or CSV row; no convention `version:` moves (`wiki-index@2` prose
clarification; `frontmatter@14` untouched) ⇒ no consumer walk, no re-ack. **Priced anyway:**

- **package-lint C6** — the operating contract is not edited; no rule-card re-derive.
- **package-lint E4** — no `package-lint` check is added; `tools/test-package-lint.py` is not touched.
- **package-lint E5/E7** — `vlt-lint-full.js`'s `// depends_on:` header and its body `per frontmatter@14`
  markers are untouched; `_e6_schema_size_budget` measures `PAGE_SCAN`, which does not move.
- **`SCHEMA_FLOOR`** (`lint-report-check.py:85`) stays 18 — it is a floor; the fence grows by one key.
- **Skill-asset manifest** — no shipped file is added or removed under `references/` or `scripts/`; the
  new fixtures are factory-side.

## Out of scope (dispositioned)

- **The vault's 55 post-adoption entries** — Q5 LEAVE; vault-side hand pass at the owner's cadence; the
  census line shows the count *stopped growing* (baseline `240 / 83 of 152`, floor ≈185 — E2/A9).
- **A report-shape change to log overridden `stub_discovery` reads** — E1 NOT BLOCKING; the E6 sixth owed
  filing (owner).
- **The `sources_vs_prose_mismatches` tier question** — Cycle 15 carry 9, read (disposition 9); an owner
  filing, not this build.
- **`vlt-lint-full.js:297/:299`'s prompt-side prohibition** — untouched under A9/A10; the
  capture-don't-interrupt item does not file.
- **A human-gated wearer-rename offer in `vlt-upgrade:79-84`** — Q21 rejected; notice only.
- **The wearers' apology parentheticals** (two on disk) — the vault's; the CHANGELOG notice says delete
  them (A17).
- **The partner persona `## Your non-negotiable` sections and contract `:246`** — the other concept;
  untouched by design.
- **A general convention-side-fixture rule** — D5 one-off; platform-ledger candidate, not this build.
- **`[[wikilink]]` stub identifiers** — A16-1's second observation, refuted at capture; no tolerance built.
- **`activation`/partner-memory work, `partner: none`, delegate** — builds 2 and 3.

## Verification (unit, at rest — lifecycle step 5)

1. **Stub-heading harness** — `uv run factory/cycles/16-closed-loops/fixtures/build-1-stub-heading-harness.py`
   exits 0 over the shipped convention (both readers, overlay case, index pair); the same harness with
   `--convention <v0.18.0 bytes>` exits 1 with both readers FAILING (record the counts in the BUILT record).
2. **Census + drop harness** — `factory/cycles/16-closed-loops/fixtures/build-1-census-harness.mjs`
   (the `build-4-return-harness.mjs` shape, importing `vlt-lint-full-shim.mjs`): phase 1 runs
   `lint-page-facts.py --census build-1-wiki/ --census-exclude build-1-wiki/index.md` for real and
   deep-compares to the hand-written oracle `build-1-expected-census.json` (per-page map + counts + the
   line); phase 2 loads the shipped workflow through the shim with planted `scan:` returns and asserts
   `malformed_frontmatter` per the case table in §Acceptance (2); `--workflow <v0.18.0 js>` runs the same
   table and must FAIL on every refusal case (the planted complaints reach the slot there).
3. **Warm-safety** — `node factory/cycles/15-nothing-reads-it-back/fixtures/build-4-return-harness.mjs --fingerprint`
   over the built `vlt-lint-full.js` prints the **same** `scanFingerprint` as over `git show v0.18.0:…`
   (record both); `git diff v0.18.0 --stat -- skills/vlt-setup/assets/governance/_meta/conventions/{frontmatter,wiki-supersession,write-verification}.md`
   is empty; `grep -n "scanModel === undefined ? 'haiku'" vlt-lint-full.js` matches at its current line.
4. **Writer grep-negative** — over `skills/vlt-lint/` (SKILL, `references/`, `scripts/`): no sentence
   describes a write **into** frontmatter `sources:` on the mismatch path — patterns (case-insensitive):
   `member of the existing .sources:. list`, `If .sources:. is absent, create it`, `Re-parse the frontmatter
   after the edit`, `write.*frontmatter .sources:.` outside a *never*-clause. Each returns 0 hits; the
   `never writes into frontmatter` sentence at F3 returns exactly 1.
5. **Slot greps** — `grep -rn 'non-negotiable-gate' skills/` returns exactly two files
   (`vlt-track/SKILL.md`, `vlt-upgrade/SKILL.md`) and each hit sits in an *accepted*/*pre-rename* clause;
   `grep -c 'write-gate' skills/vlt-mint/assets/capability-template.md` = 1;
   `grep -c 'non-negotiable\b' skills/vlt-agent-*/SKILL.md skills/vlt-mint/assets/partner-agent-template.md`
   unchanged from v0.18.0 (the persona concept survives); `module-help.csv` passes `package-lint`
   Group B (quoting, 13 columns).
6. **Cycle 15 regression** — `build-2-key-harness.mjs`, `build-3-type-harness.mjs`,
   `build-4-return-harness.mjs`, `build-5-shape-harness.py` all exit 0 against the built tree (the last
   after F11's oracle re-derive and `--wiki-dir`); `grep -c '## Stubs' wiki-index.md` = **2** (disposition 3).
7. **Gate, live shape** — `lint-report-check.py check --mode full … --wiki-dir build-1-wiki --wiki-exclude build-1-wiki/index.md`
   over a report carrying the oracle line → `ok`; the same report with `55 entries` edited to `54 entries`
   → `failed`, reason `bare_path_sources: rendered line does not match the recount`; `--mode scoped` with
   the key absent → `ok`; `--mode full` without `--wiki-dir` → exit 2.
8. **Handshake** — nothing moved; the check of record is `package-lint` Group E (run it; do not compose
   a grep). Packaging lint A/B/C/E mid-build; D at release (§Release).
9. **R2/R3/R4** — R2 not applicable (no release-gate check added). **R3 stated** — the census line's
   legal response at `checks.md:15` (F8), its single home. **R4 not applicable** — no shipped file is added
   to any enumerated class (skill assets unchanged; fixtures are factory-side under
   `factory/cycles/16-closed-loops/fixtures/`, outside every vault enumeration).
10. **Scrub** — no personal or vault-local content in any changed shipped file or in the fixtures: the
    `build-1-wiki/` pages are **synthesized** (slugs may match the capture's recovered manifest; bodies,
    titles and summaries are generic; `sources:` paths are placeholder `_agent/research/<slug>-note.md`
    forms — the specimen preserved is the per-page count, never a vault page's bytes). The `title:` above
    passes the same scrub.

## Release

This build is **v0.18.1** (roundtable A10 — build 1 alone, first). Branch `cycle16-v0.18.1`. Bump **both**
version strings — `.claude-plugin/marketplace.json` `"version": "0.18.1"` and
`skills/vlt-setup/assets/module.yaml` `module_version: 0.18.1`. Pre-tag gate:
`uv run tools/package-lint.py --expect-version 0.18.1` — tag only on exit 0, its PASS summary line in the
release commit message. Then ff-merge to `main`, tag `v0.18.1`, push main + tag (`vlt-release` runs the
choreography). `CHANGELOG.md` gains a `## v0.18.1 — <date>` section with the build line derived from
`title:` and the notice text below.

**Notice text — authored here, ships with this release (A17; this build is not collated by a later one).**

> **Field notice — the loop-profile slot is now `write-gate`.** `vlt-mint`'s capability template names the
> loop-profile method-gate slot `write-gate`; **the old key `non-negotiable-gate` is accepted
> indefinitely** — nothing parses the key, there is no sunset, and a wearer renames at leisure or never.
> A profile carrying an explanatory parenthetical about the old key's name (*"the slot is named
> non-negotiable-gate in the template …"*) should **delete the parenthetical** — the mismatch it apologized
> for no longer exists. `vlt-upgrade`'s loop-profile relocation scan recognizes both spellings.
>
> **Field notice — bare-path `sources:` entries are a census, not a per-page finding.** A wiki page whose
> frontmatter `sources:` carries entries in the unquoted `.md` form no longer appears under
> `malformed_frontmatter` for that form; a full sweep instead renders one line,
> `bare_path_sources: N entries across P of M pages …`, computed from bytes by `scripts/lint-page-facts.py`
> and checked by the persist gate against its own recount. The line's job is **never rises** — entries
> written before 2026-08-15 stay legal under `frontmatter.md` rule 4's no-backfill clause, so a vault's
> floor is above zero and a fall is not evidence of repair. Entries the lint's own sweep wrote after
> adoption are the vault's to repair by hand, at the owner's cadence. The Librarian's mismatch fix
> (`fix-and-file.md` Step 3) never writes frontmatter `sources:` — the prose section is the side that moves.
>
> **Field notice — the stub heading is stated in prose.** `{conventions}/wiki-index.md` §The Stubs section
> now states `## Stubs (linked, not yet written)` outside its fenced example. No vault action; a vault
> whose index already carries the long-form heading is unaffected, and `stub_discovery:` should read
> `located: yes` on the first sweep after this release.
>
> **The first full lint after this release is WARM by construction** — no scanner-read convention, scan
> prompt, scan schema or scan-model default moved (the persist gate and the reduce moved; neither is a
> cache-key input). A cold `lint_cache:` line after the v0.18.1 upgrade is a finding — file it.

## Acceptance (live — appended to the roadmap ledger)

`specimens: 56/61` — A16-1 **1/1** (the convention site bytes + the field index's six-slug heading; the
Cycle 15 index pair carries the heading, the harness reads the site by path); A16-2 **55/55 as the
per-page manifest** (the 22 pages × their entry counts, recovered at capture, become `build-1-wiki/`'s
per-page `sources:` counts; **bytes preserved for 1** — the filing's `dutch-oven-braising` line and its
report fragment are the planted return in the drop harness); A16-8 **0/5** (five wearers observed; no
wearer bytes reach this brief — the at-rest checks are greps over module source, and the wearer check is
field-contingent by nature).

Five `[ship-verifiable]` checks (**GATE**) and one `[field-contingent]` watch. Each ship-verifiable check
names its instrument and answers the adversary question (P-20); the roundtable's instrument-beat
properties for build-1 (*Stub read*, *Census*, *Writer*, *Slot*) are the properties below, reconciled — none
substituted.

**(1) `[ship-verifiable]` Stub read.** *Property:* given only the shipped `wiki-index.md` bytes (and an
overlay-merged variant), a reader following `checks.md:13`'s procedure returns the heading string a human
reads from the convention's Stubs rule — `located: yes` on a long-form index, `located: no` on a bare
`## Stubs` — with no reference to fences. *Instrument:* `fixtures/build-1-stub-heading-harness.py` (F2),
reading the shipped file by path, both readers, the overlay fixture, the Cycle 15 index pair; failability
against `v0.18.0` bytes recorded. Also: `grep -c '## Stubs' wiki-index.md` = 2 (disposition 3 — the Cycle
15 build-3 (4) expectation, superseded). *Adversary:* a harness that carries the expected heading as its own
constant and a *copy* of the convention passes while the shipped convention says something else — hence
read-by-path, so a shipped-heading change fails the harness. Remaining state: a vault overlay that
*restates* a different `## …` span in §The Stubs section; both readers return the base statement first,
and a duplicated base heading is `overlay_issues` territory (`report.md:53`) — named, out of scope. **No
further passing-violating state found.**

**(2) `[ship-verifiable]` Census.** *Property:* every bare-form `sources:` entry on disk is counted exactly
once on one denominated line whose value equals an independent recount; no per-page finding is raised for
the form; a full sweep never increases it. *Instrument:* `fixtures/build-1-census-harness.mjs` +
`build-1-wiki/` + `build-1-expected-census.json` (F4/F5/F6): the 22 manifest pages (55 entries) plus
controls — a page with only quoted wikilinks, one with `sources: []`, one with URLs, one in **flow form**
`[a.md, b.md]` (counted), one whose `grounding:` list ends `.md` (not counted), one with a prose
`## Sources` list of `.md` lines and quoted frontmatter (not counted), one with `sources:` as a scalar
(`sourcesUnparsed`, absent from the map), an `index.md` (excluded) — oracle line
`57 entries across 23 of 29 pages …` (22 manifest pages + the flow-form page; 29 walked, the index
excluded — the hand count is **written before the script runs**); reduce cases: planted `unclassified/['sources']` on a manifest page → **refused**; the same
on the scalar-`sources:` page (no map entry) → **reports**; `unclassified/['sources']` with `bareSources`
absent → **reports** + cap line; `missing_required/['sources']` → **reports**; `unclassified/['sources',
'title']` → **reports**; `malformed_block/[]` → **reports**; `unclassified/[]` with detail prose naming
sources → **reports** (wording never enters). Gate: `ok` on the oracle line, `failed` on an off-by-one,
exit 2 without `--wiki-dir` in full mode (§Verification 7). Failability against `v0.18.0`'s workflow
(refusals reach the slot there). The "never increases" clause is (3)'s property at the writer, and in the
field the E2 check below. *Adversary:* passing-violating states hunted and **widened into the fixture**:
a flow-form list (would be missed by a `- ` regex — counted); a `.md` entry under a *different* key
(`grounding:`/`personalization_sources:` — a key-blind count would inflate N — not counted); a prose
`## Sources` list (not frontmatter — not counted); a page whose `sources:` cannot be parsed (a census that
silently counted 0 would let the reduce refuse a genuine complaint — the page is *absent from the map*,
so the complaint reports). Remaining state: a page carrying **both** a bare entry **and** a second,
genuine `sources:` defect that a scanner reports only as `unclassified/['sources']` is refused and the
second defect is swallowed until the page's next scan or edit — stated, accepted: the direction is a
duplicate-removal over a class the report already carries, and the alternative (never refuse) is the
arbitrary per-page flag Q3 (a) retired. **No further passing-violating state found.**

**(3) `[ship-verifiable]` Writer.** *Property:* a full sweep over a page whose prose `## Sources` section
lacks an entry frontmatter `sources:` carries leaves that page's **frontmatter byte-identical**.
*Instrument:* `fixtures/build-1-reader-protocol.md` (the Cycle 15 build-6/7 reader-protocol idiom): a
fresh agent is given `fix-and-file.md` Step 3 as shipped, the fixture page `build-1-writer-page.md` (three
quoted-wikilink `sources:` entries, a prose `## Sources` with two of them), and the finding
`sources_vs_prose_mismatches: [build-1-writer-page: …]`; the recorded evidence is `shasum -a 256` over the
frontmatter block before and after (equal) and the prose section's line count (+1); plus the grep-negative
of §Verification 4 over `skills/vlt-lint/`. *Adversary:* passing-violating state: the agent adds the prose
line in a form the section does not use (wikilink vs bare) — the property (frontmatter byte-identical)
holds and the form clause is secondary, accepted; a second state: `checks.md:16` or `full-scale.md` step 5
still carrying a direction-ambiguous sentence the agent follows instead of F3 — the grep-negative spans
all three files, so the state is unreachable on the shipped surface. **No further passing-violating state
found.**

**(4) `[ship-verifiable]` Slot.** *Property:* a loop profile carrying either key reaches the same gate in
`vlt-track` and the relocation scan recognizes both; the persona-level *non-negotiable* concept survives
untouched. *Instrument:* §Verification 5's greps, recorded verbatim in the BUILT record (the two-file
`non-negotiable-gate` result, the template count, the unchanged persona count vs `v0.18.0`, the csv Group
B pass). *Adversary:* a grep that demanded zero `non-negotiable` anywhere would pass only by breaking the
persona sections — hence the hyphenated key is grepped and the persona count is asserted **unchanged**;
a passing-violating state where `vlt-upgrade:81` lists both keys but the *shape* detection (a)/(b)
around it keys on the old spelling only — re-read `:81` end to end at build time: the key list is the
only spelling-bearing clause. **No passing-violating state found.**

**(5) `[ship-verifiable]` Warm-release chance (A9/A10) + the E2 census on upgrade evidence.**
*Property:* v0.18.1 moves none of the findings cache's key inputs, so Cycle 15 build-2 (6)'s watch has a
real chance; and the first post-upgrade full sweep on `{field-vault}` renders the census line with a value
equal to an **independent** recount. *Instrument, at rest:* §Verification 3 (fingerprint equality across
`v0.18.0`/`v0.18.1`, empty diff over the three scanner-read conventions, `scanModel` default line).
*Instrument, upgrade evidence (bounded — the owner's ordinary `vlt-upgrade` to 0.18.1 + the ordinary
post-upgrade full sweep on `{field-vault}`):* the persisted report's `bare_path_sources:` line, and a
recount by an **unwrapped instrument that is not the script** — an `awk` pass over each `{wiki}/*.md`
frontmatter block (between the first two `---` lines) counting `- ` items under `sources:` that are
unquoted and end `.md`, its one-liner recorded verbatim on discharge; expected near the A9 baseline
(`240 entries across 83 of 152 pages` at 2026-09-16 — the vault may have moved). *Adversary:* the
persisted line and the gate's recount come from **the same function** — equality between them proves the
paste, not the count; hence the discharge instrument is independent by construction. **No further
passing-violating state found.** (The warm `lint_cache:` line itself is Cycle 15 build-2 (6)'s discharge,
not re-entered here.)

**(F1) `[field-contingent]` Wearer parse.** A coaching-style wearer's profile parses under the new key
and under the old key with no explanatory note needed (the filing's own clause). *Event:* the next
`vlt-mint` of a `vlt-track` wearer, or an owner-run rename of an existing wearer's `capabilities/track.md`
on `{field-vault}` — whichever first; **performer:** the owner; **vault:** `{field-vault}` (any vault with a
wearer whose live non-negotiable is not its write-gate qualifies; `career-strategist` is the named case).
Watch, not gate.
