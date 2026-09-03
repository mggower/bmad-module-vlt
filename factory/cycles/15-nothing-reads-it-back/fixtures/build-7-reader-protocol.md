# Build-7 reader protocol — the attester is judged by name, never carried by the `author:` leg

The at-rest instrument for `briefs/build-7-roster-closure-retired.md` check (3) (and the walker half
of check (4)). It is **agent-run**: `para_writer_unauthorized` is a governance check the SKILL judges
from `checks.md:20`; no executable renders the verdict — the walker (`scripts/lint-para-facts.py`)
emits *facts* (`writers`, `declaring_ancestor`, `counts.D`) and the reader applies the join. The
protocol is the named instrument; its evidence is the produced table diffed against the hand-written
oracle `build-7-expected-findings.json` (written FIRST, before any run). Specimens `0/27` —
`build-7-para/README.md` says why.

## Given

- The shipped text at a **stated commit**: `vlt-lint/references/checks.md:20` (the
  `para_writer_unauthorized` net — the nearest-declaring-ancestor walk, the join, the `open` default,
  sub-container inheritance), the operating contract's resolver (`vault-operating-contract.md:68`,
  *The three layers and the hard write boundaries*), and `{conventions}/write-verification.md`
  §Attestation (the `verified_by` value set, v6).
- The fixture tree `build-7-para/` with `{projects}` → `projects/`, `{areas}` → `areas/`,
  `{resources}` → `resources/`, `{wiki}` → `resources/wiki/`.

## Produce

1. **The population and the facts** — run the shipped walker from inside `build-7-para/`:
   `uv run --quiet skills/vlt-lint/scripts/lint-para-facts.py --dir projects --dir areas --dir resources --exclude resources/wiki --root . --out -`
   (and again under bare `python3` — byte-identical), then `--line` and `--writer-line`. Record
   `counts: {P, M, D}`, each file's `writers` / `declaring_ancestor`, and the two lines. The `{wiki}`
   page must be in no list.
2. **The verdict table** — for each file in P, from the shipped text only (never from memory of the
   rule): resolve the list (`declaring_ancestor`'s `writers`; none → `open`, PASS, no row fires);
   resolve the writer of record — **where `verified_by:` is present, that identity by name; where
   absent, the `author:` leg (`human` → human, `agent` → agent, `hybrid` → human)**; a file resolving
   neither is left to the honesty nets; then judge: the list admits the identity iff it names it, or
   names `agent` and the identity is agent-kind (an op or a partner slug), or names `human` and the
   identity is human. `finding: true` iff not admitted.
3. **Failability** — repeat step 2 with the text at the **pre-build commit** (`git show
   fc44027:skills/vlt-lint/references/checks.md`, `…/vault-operating-contract.md`): the any-match join
   over `{author identity, verified_by slug}`.

## Evidence

Step 1's facts, counts and `--writer-line` deep-equal the oracle's `walker` / `counts` /
`missing_attestation` / `writer_line`; step 2's table deep-equals `shipped`; step 3's table deep-equals
`pre_build`, and the two tables **differ** (on `areas/gamma/ratified.md` at minimum). A reader that
produces the shipped table from the pre-build text has not read the rule.

## Run record — 2026-09-02, build-7 working tree (F1–F9 applied on `5eb90b5`)

**Step 1 (walker, `uv run` and `python3` byte-identical):** `counts: {P: 15, M: 1, D: 13}`;
`missing_attestation: [projects/alpha/unattested.md]`; `--line` = `15 files walked … 1 carry author
agent|hybrid with no attestation …`; `--writer-line` = `15 judged; 13 under a declaring ancestor; 2
passed on open posture (instrument: scripts/lint-para-facts.py)`. `writers` read in flow form
(`alpha`, `gamma`) and block form (`beta`); every `alpha/` file incl. `sub/deep.md` resolves
`projects/alpha/charter.md`; both `delta/` files resolve `null`; `resources/wiki/page.md` in no list.
Deep-equal to the oracle's `walker` / `counts` / `missing_attestation` / `writer_line` (the compare
script's four `True`s are in the brief's BUILT status).

**Step 2, shipped text** (`checks.md:20`: *"Where `verified_by:` is present, the attester is the
writer of record: the file passes iff the list admits that identity — `agent` admits every agent-kind
identity, a specific slug admits only itself — and the `author:` leg neither rescues nor refuses it …
Where no `verified_by:` is present, the `author:` leg is judged alone"*):

| file | list | writer of record | verdict |
|---|---|---|---|
| `projects/alpha/charter.md` | `[human, librarian]` | `human` (hybrid, no attester) | pass |
| `projects/alpha/draft.md` | `[human, librarian]` | `librarian` (attester) | pass |
| `projects/alpha/note.md` | `[human, librarian]` | `banana` (attester) | **fires** — named by no entry; no `agent` declared |
| `projects/alpha/agent-note.md` | `[human, librarian]` | `librarian` (attester) | pass |
| `projects/alpha/sub/deep.md` | `[human, librarian]` (inherited) | `researcher` (attester) | **fires** — inheritance |
| `projects/alpha/human.md` | `[human, librarian]` | `human` | pass |
| `projects/alpha/unattested.md` | `[human, librarian]` | `agent` (author leg, no attester) | **fires** — and in M (two nets, one file) |
| `areas/beta/charter.md` | `[human, agent]` | `human` | pass |
| `areas/beta/any.md` | `[human, agent]` | `banana` (attester) | pass — `agent` admits any agent-kind identity (the residual, Q5) |
| `areas/beta/hybrid-op.md` | `[human, agent]` | `vlt-extract` (attester) | pass |
| `areas/gamma/charter.md` | `[human]` | `human` | pass |
| `areas/gamma/ratified.md` | `[human]` | `librarian` (attester) | **fires** — D-E: hybrid → human neither rescues nor refuses |
| `areas/gamma/plain.md` | `[human]` | `human` | pass |
| `resources/delta/open-note.md` | open | — | pass, counted in `O` |
| `resources/delta/human-note.md` | open | — | pass, counted in `O` |
| `resources/wiki/page.md` | — | — | not in P (carved out by name) |

Four fire (`note.md`, `sub/deep.md`, `unattested.md`, `ratified.md`); deep-equal to the oracle's
`shipped`.

**Step 3, `fc44027` text** (*"join the file's writer identities against that list, admitting on
**any** match … and the attestation `verified_by:` → that partner slug"*; contract: *"admitted when
**any** of its identities is in that list"*): identities per file are `{author identity, verified_by
slug}`; `ratified.md` = `{human, librarian}` vs `[human]` → **passes** (the author leg carries it);
every other row as in step 2 (`note.md` `{agent, banana}` fires; `sub/deep.md` `{agent, researcher}`
fires; `unattested.md` `{agent}` fires; `any.md`/`hybrid-op.md` pass on `agent`/`human`). Three fire.
Deep-equal to the oracle's `pre_build`; **differs from the shipped table on exactly
`areas/gamma/ratified.md`** — the instrument reads the rule.
