# Build-6 reader protocol — the type judgment is vocabulary membership, not folder

The at-rest instrument for `briefs/build-6-type-prohibition-retired.md` check (3) (and the failability
leg of check (4)). It is **agent-run**: no script implements the recognized set (disposition 6 — the
set has no machine-readable home yet; build-5's owed `candidate`). The protocol is the named instrument;
its evidence is the produced table diffed against the hand-written oracle
`build-6-expected-findings.json` (written FIRST, before any run).

## Given

- The shipped text at a **stated commit**: `{conventions}/extraction.md` *`type:` mapping by target
  folder* (the recognized-set paragraph, `:84`), `vlt-lint/references/checks.md:19` (the `para_*`
  population + `para_type_unknown`'s predicate and legal response), and `{conventions}/frontmatter.md:71`
  (the canonical `type:` list — the fourth leg's home).
- The fixture tree `build-6-para/` with `{projects}` → `projects/`, `{areas}` → `areas/`,
  `{resources}` → `resources/`, `{wiki}` → `resources/wiki/`, `{overlays}` → `_agent/conventions/`.
- Two overlay states: **present** (read `_agent/conventions/extraction.overlay.md` as the vault's
  declared schema) and **absent** (read the tree as if that file did not exist).

## Produce

1. **The population** — run the shipped walker, which is the population's instrument
   (`checks.md:19` — *"the walk `scripts/lint-para-facts.py` performs"*):
   `uv run --quiet skills/vlt-lint/scripts/lint-para-facts.py --dir projects --dir areas --dir resources --exclude resources/wiki --root . --line`
   from inside `build-6-para/`. Record `P`. The `{wiki}` page must be in no list.
2. **The finding table** — for each file in P, read its `type:` and answer, **from the shipped text
   only** (never from memory of the rule): is the value in the recognized set as `extraction.md:84`
   states it — leg 1 the PARA artifact types, leg 2 the operational-record class, leg 3 the overlay's
   declared schema (present state only), leg 4 the values `frontmatter.md:71` names? A value in none
   of the four → `finding: true` and the legal-response case per `checks.md:19` ((a) vault-grown →
   declare; (b) misspelling/near-miss → correct; (c) otherwise → relocate out of PARA). Otherwise
   `finding: false` and the admitting leg.
3. Repeat step 2 under the other overlay state.

## Evidence

The two produced tables + `P`, deep-equal to the oracle's `overlay_present` / `overlay_absent` /
`population`. **Failability:** run steps 1–2 again with the text at the **pre-build commit**
(`ed0d96b` — `git show ed0d96b:<path>` for the three files); the produced table must equal the
oracle's `pre_build` block, which differs from the shipped tables on `research`,
`wiki`-in-`projects/` and `note` (all three fire under the retired case (b)) and on `resourse`'s
case letter. A reader that produces the shipped table from the pre-build text has not read the rule.

## Run record — 2026-09-02, build-6 working tree (F1–F5 applied on `faa9cb4`)

**Step 1 (walker, overlay-independent):** `9 files walked under {projects}/{areas}/{resources},
{wiki} subtree carved out … 0 carry author agent|hybrid with no attestation` — `P: 9`; the population
list is the nine non-wiki files; `resources/wiki/a-page.md` appears in no list.

**Step 2, shipped text, overlay PRESENT** (fourth leg read at `frontmatter.md:71`: `wiki`, `research`,
`session`, `note`, `project`, `area`, `resource`, `moc`, `idea`, `charter`, `record`, `register`;
overlay declares `dispatch-brief` only):

| file | `type:` | judgment |
|---|---|---|
| `resources/briefs/sub-a/2026-09-01-090000-issue.md` | `research` | no finding — leg 4 |
| `resources/wiki/a-page.md` | `wiki` | not in P (carved out by name) |
| `projects/a-note.md` | `wiki` | no finding — leg 4 |
| `areas/session-log.md` | `note` | no finding — leg 4 |
| `projects/p/charter.md` | `charter` | no finding — leg 2 |
| `areas/plan.md` | `area` | no finding — leg 1 |
| `areas/declared.md` | `dispatch-brief` | no finding — leg 3 |
| `resources/undeclared.md` | `dispatch-note` | **fires** — case (a) |
| `resources/banana.md` | `banana` | **fires** — case (c) |
| `resources/resourse.md` | `resourse` | **fires** — case (b) |

**Step 3, shipped text, overlay ABSENT:** identical except `areas/declared.md` → **fires**, case (a).
`P: 9` both states.

**Failability, `ed0d96b` text** (closed set = legs 1–3 only; `checks.md:19` case (b) = module-canonical
non-PARA `wiki|research|session|note|idea` → retype or relocate; overlay present):
`research` → **fires** (b); `projects/a-note.md` `wiki` → **fires** (b); `areas/session-log.md` `note` →
**fires** (b); `resourse` → fires under **(c)** (the old text has no near-miss case); `charter`, `area`,
`dispatch-brief` no finding; `dispatch-note`, `banana` fire (a)/(c); `P: 9`. **Differs from the shipped
table on exactly the oracle's `pre_build` rows** — the instrument reads the rule.

**Comparison:** both shipped tables and the pre-build table deep-equal the oracle (the check script
run is recorded in the brief's BUILT status).
