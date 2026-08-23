# Eight releases, no changelog — and the practice already runs, it just has no output file

_Filed 2026-07-31 from a **factory-side ideation session** (not a field vault) — a
`bmad-brainstorming` run over "release changelog for each vlt release, adopted into
`vlt-release`." Four techniques: failure analysis, persona journey, constraint mapping,
reversal inversion. Full session:
`_output/brainstorming/brainstorming-session-2026-07-30-changelog.md` (gitignored).
Grounding is this repo, read-only._

_**Amended 2026-07-31** after the owner asked whether the history could be retro-filled. It can
— more cleanly than the session's own reasoning assumed. See **Retro-fill** below; it corrects
the "floor, not backfill" recommendation and the F15 risk that produced it._

## The claim

Eight tags have shipped (`v0.3.0`…`v0.9.0`, plus `v0.3.1`) and **no `CHANGELOG*` file exists
anywhere in the repo**. The public surface records that versions happened and nothing about
what they contain — the module that enforces honest surfaces on its vaults publishes none of
its own release history.

The second, sharper claim: **the authoring work is already done.** Every build brief carries a
`title:` — one authored sentence written at brief time by someone who understood the change:

> `title: 'Build #B5-3 — exact facts (the lint asks LLM scanners for exactly-computable facts
> and declares a report slot no check fills; …)'`

That is a changelog entry. It has been one for ~30 builds. Nothing collects them. So this is not
a proposal to *start* a changelog practice — it is a proposal to give the one already running an
output file.

## Grounding

- `git tag` → `v0.3.0 v0.3.1 v0.4.0 v0.5.0 v0.6.0 v0.7.0 v0.8.0 v0.9.0`; `ls CHANGELOG*` → no
  matches.
- `.claude/skills/vlt-release/references/choreography.md` — eight stop-on-failure gates. Stage 3
  is the dual version bump, Stage 4 the lint gate (`--expect-version X.Y.Z`), Stage 5 the
  release commit carrying the verbatim PASS line, Stage 6 ff-merge + `git tag`.
- `.gitignore` — `.claude/`, `skills/reports/`, `inbox/`, `docs/`, `_output/` are all local-only.
  **`vlt-release` is itself gitignored**: it is factory tooling that writes a public artifact.
  `tools/` is tracked and public.
- `tools/package-lint.py` (623 lines) — Groups A–E; **Group D is tag intent** (`check_group_d`,
  :402: asserts both version strings equal `--expect-version`).
- `skills/reports/archive/build-*.md` — 30 briefs (builds 1–23 less 17, A4-1..5, B5-1..9), each
  with an authored `title:` and a `status:` recording BUILT + numbered deviations.
- Tag→build mapping is carried by the release-commit titles themselves (`git log -1 --format=%s`
  per tag): `v0.5.0` = Arc 2, `v0.6.0` = builds 14+15+16+18, `v0.7.0` = 19+20+21+22+23,
  `v0.8.0` = A4-1..A4-5, `v0.9.0` = B5-1..B5-9. `v0.3.0` is the exception — a single
  "initial public release" commit naming no builds.
- Release commit `f3b343d` (0.9.0) — nine builds, one commit, one prose body paragraph. Every
  release shares the shape; the per-build commits survive underneath (`c1a4f9b`, `2f19251`,
  `43795fa`), just unindexed.
- `skills/vlt-upgrade/SKILL.md` Step 1 — the divergence snapshot is **path-keyed** (local mints,
  overlays, base divergence, skill-asset SHA divergence). Step 5 writes `_agent/upgrade-ledger.md`.

## Why it matters

Four costs, and one of them is already being paid every arc.

**1. The version↔build index exists nowhere in one piece.** "Which release shipped B5-3, and was
that before or after lint Group E?" is answered today by `git log | grep`, and only because the
commit titles happen to be unusually rich. `arc-closeout` and `acceptance-discharge` both
reconstruct this from roadmap `status:` prose. That's the cost already being paid.

**2. The upgrading owner's actual question is unanswerable.** At `vlt-upgrade` time the question
is not "what shipped" but *"which of my divergences does this release rewrite?"* — overlays,
minted `vlt-agent-*`, hand-edited skill assets. Step 1's snapshot is path-keyed, so a per-entry
`changed_paths:` list could be intersected with it directly (*"3 of your 7 hand-edits are in
files this release rewrites"*). Nothing today can produce that intersection.

**3. Skipped-version upgrades have no migration signal.** A second vault upgrading 0.7.0 → 0.11.0
has no way to learn that one of the skipped versions required a `vlt-setup` re-run. Which forces
a question vlt has never answered publicly: **what is a breaking change in vlt?** A convention
`version:` bump? A `vault_structure` default path move? A removed skill? That taxonomy doesn't
exist, and its absence is what makes the semver on the tags decorative.

**4. The public repo reads as inert.** Nine tags, no entries. For a fresh installer the cadence
of a changelog is the signal, more than its content.

## The shape that survived constraint-mapping

Recorded here as the session's output, not as a build ruling — grouping/scope are the roadmap's
to settle.

**One public file, one factory index, and no new gate.**

- **`CHANGELOG.md`** at repo root, tracked (shipped surface), newest-first. Per entry:
  `## vX.Y.Z — DATE — Arc N: <arc name>`, then `sha:`, `requires:`, `changed_paths:`, then one
  prose paragraph compressed from that release's build `title:` fields.
- **Backfill the history; floor only at `v0.3.0`.** The session originally recommended a floor at
  the first release that ships this, with everything below it collapsed into one reconstructed
  block. **That was over-cautious — see Retro-fill.** The corrected shape: real entries for
  `v0.4.0` onward, and a single `v0.3.0` entry labelled brief-sourced.
- **No new gate.** `--expect-version X.Y.Z` already means "I intend to tag X.Y.Z"; Group D just
  learns one more artifact that must agree. Stage 3 widens from "dual version bump" to "version
  bump + changelog entry"; Stage 4's invocation is unchanged and audits three artifacts instead
  of two; Stage 5 adds `CHANGELOG.md` to the same commit. **Eight gates stay eight.**
- **Stage 5 gets smaller, not bigger.** The release commit's "what ships" body paragraph is
  dropped — the entry is now that fact's single home (single-home discipline). Title and the
  verbatim lint PASS line stay.
- **Stage 6 tags annotated:** `git tag -a vX.Y.Z -m "<entry prose paragraph>"`. One home, two
  renders; GitHub's releases page gets real content for free.
- **Group D grows five assertions,** all mechanical and all able to fail honestly — top entry's
  version equals `--expect-version` (the gate you cannot pass by doing nothing); bipartite
  tag↔entry above the floor (`handshake-check.py`'s exact shape); `changed_paths` ⊆
  `git diff --name-only <prev-tag>..HEAD` on the shipped surface (which makes the entry
  **verifiable against the tree**); a forbidden-token scrub grep; `sha` well-formed and
  `requires:` present.

**Why enforcement must live in `tools/`, not the skill.** `.claude/` is gitignored — no vault, no
contributor, no fresh clone ever sees `vlt-release`. Only `tools/package-lint.py` is public. The
skill *runs* the rule; the tool *is* the rule. This is exactly how the existing lint gate already
works: Stage 4 is three lines of prose pointing at a public script.

**One upstream change.** `build-brief`'s exit gate gains a line: the brief `title:` is
public-facing changelog prose — scrub-clean, no vault-local paths, readable to someone outside
the factory. Nothing else upstream moves.

## Retro-fill — the whole history is recoverable, and it is collection, not reconstruction

The session's F15 risk ("retro-generation poisons the well") assumed backfilling meant
reconstructing nine builds out of a squashed release commit. **That assumption is wrong for seven
of the eight tags.** Two independent sources survive: the per-build commits on `main`, and the
briefs in `skills/reports/archive/` — 30 of them, each carrying an authored `title:`.

| Releases | Surviving evidence | Fidelity |
|---|---|---|
| `v0.5.0` – `v0.9.0` (5 tags) | per-build commits on `main` **and** briefs | high — prose from `title:`, `changed_paths` from the real diff |
| `v0.3.1`, `v0.4.0` | release commits + briefs 10 and 11; build-10's own commit was squashed, build-11's survives (`299e70b`) | good |
| `v0.3.0` | **one commit** — `8c0955f "vlt v0.3.0 — initial public release"`. No per-build commits; briefs 1–9 exist | brief-sourced only |

`changed_paths:` is computable from a real diff for **every** tag regardless of commit
granularity, because the tags themselves are real. Only the *prose* attribution degrades, and only
at `v0.3.0`.

So the honest cut is a floor at `v0.4.0` with one labelled `v0.3.0` entry — **one caveat block
instead of eight**. F15 is downgraded from a design risk to a single footnote.

**Open question the retro-fill exposes (owner's to settle).** Arc 1 is recorded as builds 3–11
spanning **three** releases (`v0.3.0`, `v0.3.1`, `v0.4.0`), while build-7 is recorded as having
shipped in `v0.3.0`. Which builds landed in the initial public release is not derivable from
`main` — its history was collapsed at publication. The archived Arc 1 roadmap or the owner settles
it. Two consequences: the `v0.3.0` entry's build list depends on the answer, and this is a
**sharper instance of arc ≠ release than Arc 3** (three releases in one arc, not two).

## Scope property: this build has almost no field surface

Worth naming because it is unusual for this module. `vlt-release` and `build-brief` are gitignored
factory tooling; the only public surface touched is the new `CHANGELOG.md` and the Group D
additions in `tools/package-lint.py`. **No shipped `vlt-*` skill changes, and nothing reaches a
vault.**

So every acceptance check here would be **ship-verifiable** — verifiable at rest by running the
lint against the repo — and **none field-contingent**. It gates arc closeout cleanly with no
dependency on an upgrade run, which makes it a cheap rider on any arc rather than a build that
has to wait for field evidence.

The exception is exactly the piece already split off: the deferred `vlt-upgrade` consumption
(intersecting `changed_paths` with the Step-1 divergence snapshot, and the ledger copy) touches a
shipped skill and *is* field-contingent. Keeping it separate preserves this property.

## The tension this design routes around rather than solves

**A tag is immutable; acceptance is revisable.** Release is lifecycle step 6, acceptance step 7.
An entry written at tag time is a permanent public claim, but its acceptance may FAIL weeks later
— A4-4(5) did, and is now two-arc inherited debt. These can contradict, and the immutable one
wins by default.

The cut: **the public entry never mentions acceptance.** The revisable verdict lives factory-side,
in a gitignored `release-index.md` carrying `build → version → sha → arc → acceptance state`
alongside build IDs and field-contingent tails — all of which the public file cannot carry anyway
(the briefs and roadmaps it would cite are gitignored; the links would 404 for everyone but the
owner). Named here, **not proposed for this build.** Its real payoff is later: if that index
exists, `arc-closeout` and `acceptance-discharge` read *it* instead of parsing roadmap prose —
a reduction to one reader rather than the addition of a third.

## Deferred, named so they aren't lost

- **Breaking-change taxonomy + `requires:`.** The key ships empty until the taxonomy exists. This
  is the largest unbuilt idea in the session and the one that would make the semver honest.
- **`vlt-upgrade` consumption** — intersect `changed_paths` with the Step-1 divergence snapshot;
  copy the installed version's entry into `_agent/upgrade-ledger.md` so the vault records what it
  took, not just that it upgraded. Separate build: `vlt-upgrade` is shipped, `vlt-release` isn't.
- **Factory `release-index.md`** and the `arc-closeout` / `acceptance-discharge` collapse onto it.
- **`inbox` filings gain `first-bad-version:`.** A changelog is what makes that field fillable,
  and "worked in 0.8.0, broken in 0.9.0" is a far better filing than a symptom description. This
  closes the lifecycle edge from step 6 (release) back to step 1 (field notes), which is currently
  missing.
