---
build: 6
slug: declared-typed-subtree
cycle: 14-no-enforcement-point
kind: hot-fix repair build
briefed: 2026-09-01
built: null
release: v0.17.2 (planned)
status: 'WITHDRAWN 2026-09-01, owner-ruled, before any code was written. Superseded by
  `factory/inbox/2026-09-01-160000-supersession-the-para-type-enum-is-locations-last-proxy-for-trust.md`
  — the first use of P-15''s `supersession` class. **This brief was a perimeter patch on a root cause
  the factory diagnosed on 2026-08-25** (`ST-2`, `status: standing`): it proposed a NEW mechanism for
  the vault to declare a typed subtree, and it **explicitly scoped OUT the `{wiki}` unification** —
  the half that would have made the change a category rather than an allowlist entry. That scoping
  ruling is what converted it into pass five. `ST-2` RC2 names the mechanism exactly: *"the repo''s
  own governance quality biases toward perimeter patches … they make the minimal patch the rational
  move every time — which is exactly how a root cause survives four cycles."* **Retained unbuilt as
  the worked negative**: the grounding in §1 and §3 is sound and is reproduced in the supersession
  filing; what is wrong is the SHAPE of the ask. Nothing was committed; no version moved; no
  handshake was performed; `extraction.md` stays at `version: 9`. Its 6 acceptance checks are struck
  on the cycle ledger. **Do not build from this file.**'
---

# Build 6 (repair) — a declared typed subtree — ⚠ WITHDRAWN, RETAINED AS A WORKED NEGATIVE

> ⚠ **WITHDRAWN 2026-09-01 before any code was written.** This build asked for a **new mechanism**
> where the honest ask was a **retirement**. Read
> `factory/inbox/2026-09-01-160000-supersession-the-para-type-enum-is-locations-last-proxy-for-trust.md`
> instead. Everything below is preserved as written — including the minimal-scope ruling in §2 that
> is the error, so the next reader can see what a perimeter patch looks like from the inside while it
> still feels like discipline. **Do not build from this file.**

*A hot-fix, so this is a **record of an owner-ruled direction**, not a full brief: the direction was
ruled before the build opened. It is briefed rather than merely recorded because it changes a
convention rule and moves a shipped check's population, which `build-brief` §9 requires acceptance
checks for.*

## 1. The defect

`extraction.md:84`, shipped by **build-3** at `e42429d` (v0.17.0), closes the PARA `type:` set and
states its escape:

> A module-canonical but **non-PARA** `type:` (`wiki`, `research`, `session`, `note`, `idea`) sitting
> in a PARA folder is therefore a **mis-typed or mis-placed artifact** … the response is to retype it
> to the target folder's `type:`, or to relocate it to that type's home zone — **never to declare
> module vocabulary as vault-grown overlay schema.**

`checks.md:19` restates the response as three cases and gives the prohibition its reason: declaring
module vocabulary *"would make the vault assert local authorship of a module-level answer."*

**The reason is correct. Its population is not.** The prohibition is written globally, and a vault
that wants to say *"this one shelf holds this one kind"* asserts nothing about the module-level
answer — yet is refused by the same sentence that correctly refuses a global redefinition.

**The measured harm** (`{field-vault}`, filing §Field evidence): `resources/briefs/` holds **9 files
across 3 subscriptions** (5 at park time, 8 on 2026-08-31, **9** on the 2026-09-01 sweep — it moves) carrying `type: research`, which is the accurate word for a dated,
single-pass, `trust: raw` periodical snapshot — the exact artifact `extraction.md:28-30` defines a
research note to be. Both stated responses require writing something false: `type: resource`
contradicts that definition, and relocating to `{research}` reverses a logged `capability-change` and
destroys per-subscription containment. The population **grows by one file per subscription per
cadence** and has already moved 5 → 8.

**The inversion, which is the reason this is a defect and not a preference.** The overlay escape stays
open for *vault-grown* vocabulary. So a vault typing the same artifacts `dispatch-brief` is conformant
today, and a vault using the module's own accurate word is permanently not. **The rule is strictest
against vaults that use the vocabulary correctly** — which inverts the purpose of a
recognized-vocabulary rule.

⚠ **The vault has already refused this class of move once, and the module ratified the refusal.**
Park #16 declined to stamp a rostered `verified_by` on a file that op did not write; build-5 then
shipped `write-verification.md:55` v5 — *"fusing permission to provenance is the write-path failure
this exemption exists to prevent."* Falsifying `type:` to close `para_type_unknown` is the same act as
falsifying `verified_by:` to close `para_missing_attestation`.

## 2. The direction — minimal, and what it deliberately is not

**Add a third legal case: a vault may declare a *typed subtree*.** The declaration names a subtree
under a PARA zone and the single `type:` its files carry; files in that subtree are judged against the
**declaration**, not the PARA artifact set.

**Three properties are load-bearing and must survive the build:**

1. **Scoped, never global.** Declaring `research` for `{briefs}` makes `type: research` legal **in that
   subtree and nowhere else** in the PARA population. The prohibition keeps its real population — a
   vault still cannot redefine a module word module-wide — and loses only its overreach.
2. ⚠ **It is LOOSER than v9, by exactly one declared value per declared subtree, and the brief says so
   plainly.** An earlier framing of this direction as *stricter* was **wrong** and is corrected in the
   filing: `checks.md:19` already flags any `type:` outside the recognized set, so a stray `type: wiki`
   under `{briefs}` is **not** invisible today. What makes the loosening safe is **scope and
   durability** — one value, one named subtree, recorded in the overlay where `vlt-upgrade` surfaces
   it — not added strictness. Do not re-argue this as a tightening in the built record.
3. **The declaration is the enforcement point.** The owner's position is *any designated type should
   be legal as long as it is consistent and intentional*. `intentional` is not observable; a
   declaration is. The declaration **is** the intention, and conformance to it is the consistency.
   This is the cycle's own thesis applied to the cycle's own defect.

### Out of scope — stated so the build does not drift into it

⚠ **Unifying `{wiki}` into the mechanism is OUT.** `{wiki}` is removed from the `para_*` population
**at selection time** (`extraction.md:84`, `checks.md:19`) — a different mechanism from an
in-population declared type, governing **146 files** in `{field-vault}` alone. Converting it would
change lint's selection behaviour at that scale for no defect anyone has reported. `{wiki}` stays a
by-name selection-time removal in this build.

**The general form — one mechanism covering both, `{wiki}` as its shipped first instance rather than
its exception — is the filing's own candidate direction and belongs to Cycle 15 ideation.** This build
buys the field its legal vocabulary back; it does not redesign the population rule. The filing stays
**live in `factory/inbox/`** after this ships, carrying the general direction.

Also out: the two secondary questions the filing raises for capture (whether the prohibition survives
at all under a declaration; whether the declaration's home is the overlay, the structure map, or
both). This build answers the second narrowly — **the overlay**, because that is where declare-at-birth
already lives and because a vault-local shelf has no entry in the module's default structure map — and
leaves the general question open.

## 3. Sites — grounded, to be confirmed at build

| # | site | change |
|---|---|---|
| 1 | `skills/vlt-setup/assets/governance/_meta/conventions/extraction.md:84` | Add the typed-subtree declaration to the closed set; rewrite the final sentence's prohibition with the subtree qualifier |
| 2 | `.../conventions/extraction.md` (declare-at-birth locus, near `:84`) | State the declaration's **shape** — subtree path + the single `type:` — and that it is scoped to that subtree |
| 3 | `.../conventions/extraction.md:11` | `version: 9` → `10` |
| 4 | `skills/vlt-lint/references/checks.md:19` | Case **(b)** gains the third response; the parenthetical recognized-set restatement gains the declaration. ⚠ `:19` says the set is *"defined in `extraction.md` … which is its single home; named here for the reader only"* — **keep it a pointer, do not restate the declaration's mechanics** |
| 5 | `skills/vlt-extract/SKILL.md:4`, `vlt-lint/SKILL.md:4`, `vlt-track/SKILL.md:4`, `vlt-query/SKILL.md:4` | `extraction@9` → `extraction@10` |

**Grounding note for the build:** sites 1–3 are confirmed by direct read at v0.17.1. Site 2's exact
insertion point is **not** pinned to a line — `:84` states the closed set inline and the
declare-at-birth rule is cited rather than sited. **Locate it at build time**; do not assume a
heading exists.

## 4. The version-handshake ruling

**`extraction.md` 9 → 10 — a RULE CHANGE, not a prose clarification.** It changes which files
`para_type_unknown` reports, which is a shipped check's population. Same test build-5 applied to its
own `extraction` 8→9 bump.

**Consumers, from `extraction.md:12`:** `[vlt-extract, vlt-lint, vlt-track, vlt-query]` — **4 re-acks**,
all in this build. Verify **bipartite-consistent both directions**: every consumer listed carries a
current ack, and every skill acking `extraction@10` appears in `consumers:`.

**No other convention moves.** `frontmatter.md` (14) is untouched — it governs the base/agent lane and
`:84` already states it *"does not answer here"*. `write-verification.md` (5) is untouched — attestation
is an orthogonal axis (`write-verification.md:55`, *Jurisdiction boundary*).

**`vault-operating-contract.md` is NOT edited**, so `vault-rule-card.md`'s `derived_from:` sha256 does
**not** re-stamp (C6). ⚠ If the build finds it must touch the contract, that is a **scope breach** —
stop and re-rule, do not absorb it.

**E7 (in-prose pins):** `grep -rn "extraction@9" skills/ | grep -v depends_on` returns **zero** today,
so no in-prose recitation needs restating. Re-run after the edit; E7 gates at the release.

## 5. Verification at rest (before release)

- **V1** — `extraction.md:84` states the declaration as a member of the closed set, and the
  prohibition's final sentence carries the subtree qualifier.
- **V2** — the scoping property is textual, not implied: the file says in words that a declaration
  legalizes its value **in that subtree only**.
- **V3** — `grep -rn "never to declare module vocabulary\|never overlay-declare module vocabulary" skills/`
  returns **both** sites (`extraction.md`, `checks.md:19`) and **both** carry the qualifier. A repair
  that lands on one and not the other reproduces the two-memberships defect build-5 just fixed.
- **V4** — handshake bipartite-consistent both directions on `extraction@10`; 4 consumers, 4 acks.
- **V5** — `checks.md:19` remains a **pointer**: `grep` shows the declaration's mechanics stated in
  `extraction.md` only. Single-home discipline.
- **V6** — `uv run tools/package-lint.py --expect-version 0.17.2` exits **0**; record the PASS line in
  the release commit.
- **V7** — `PAGE_SCAN` unchanged (E6): this build edits convention prose and touches no scanner
  schema. Measure with package-lint's own `_E6_NODE_EXTRACTOR`, never a source char count.

## 6. Acceptance checks

*Per cycle ruling **D3 as amended**: a **bounded** check is ship-verifiable and it **GATES**. Each
names the seam it crosses (**R1**).*

**(1) `[ship-verifiable]` — at rest — GATES.** Both prohibition sites carry the subtree qualifier and
say the scoping in words — `extraction.md:84` and `checks.md:19`, verified by V3's grep returning two
hits and a read of each. **It can fail:** one site qualified and the other not. *Seam:* module source
agreement across two files. *Evidence:* grep output + both rewritten sentences verbatim.

**(2) `[ship-verifiable]` — at rest — GATES.** The declaration's mechanics are stated in
`extraction.md` and **nowhere else**; `checks.md:19` cites without restating. **It can fail:** a second
statement of the shape anywhere in `skills/`. *Seam:* single-home discipline. *Evidence:* V5 grep.

**(3) `[ship-verifiable]` — at the release gate — GATES.** `extraction@10` bipartite-consistent both
directions across exactly 4 consumers, and `package-lint --expect-version 0.17.2` exits 0 with both
version strings bumped and **E7 clean**. *Seam:* convention → consumer ack. *Evidence:* the handshake
count + the PASS summary line in the release commit.

**(4) `[ship-verifiable]` — bounded to a **SCOPED** `vlt-lint` run over the declared subtree —
GATES.** With `{briefs}` declared, the brief issues **leave `para_type_unknown`** (9 as of 2026-09-01 — **grade the population as measured at run time, never the number written here**) and the slot
reports them **not at all** — while a **control** file carrying a different non-PARA `type:` in the
same subtree **still reports**. ⚠ **The control is mandatory and the check fails without it**: a check
that only watches findings disappear cannot distinguish a working declaration from a disabled net —
which is [P-20]'s question asked at brief time rather than after. *Seam:* the declared subtree →
`para_type_unknown`. *Event:* the owner declares `{briefs}` in `{overlays}/extraction.overlay.md`,
then runs a **scoped** `vlt-lint` whose scoped set includes `resources/briefs/`. *Performer:* the
owner.
⚠⚠ **NO FULL SWEEP IS REQUIRED, and binding this to one would be a cost error.** `checks.md:19`
places the `para_*` closing nets — `para_type_unknown` among them — in **both modes**, and
`vlt-lint/SKILL.md:41` defines *"every PARA file"* as *"the PARA members of the scoped set in scoped
mode."* The 146-agent fan-out scans **`{wiki}`**; `resources/briefs/` is PARA, **outside** `{wiki}`
(`vlt-lint-full.js:812-814` — `para_missing_attestation` is *"a structural slot the SKILL fills"*, and
the same holds for `para_type_unknown`). A scoped run exercises this check **exactly**, at a fraction
of the dispatch cost. *(Corrected 2026-09-01: this check was first written bound to a full sweep. That
was wrong — the population it judges is not the fan-out's.)*

**(5) `[ship-verifiable]` — bounded to the same scoped run — GATES.** The loosening is **scoped**: a
file carrying `type: research` at a PARA address **outside** any declared subtree still reports
`para_type_unknown`. **It can fail:** the declaration leaked to the whole population. *Seam:*
declaration scope → check population. *Evidence:* the second control's finding. Extend the scoped set
to include that control's address; still no full sweep.

**(6) `[field-contingent]` — does NOT gate.** Park **#15** unwinds: re-derived against **v10** and
resolved by a superseding decision-log entry, with the vault executing a legal response
(**declare the subtree**) **without writing anything false**. ⚠ **This is the clause build-3's check
(6) has been unable to reach**, and it is tagged field-contingent because nothing in the build,
release or upgrade causes an owner to write a log entry. ⚠ **Do NOT pre-draft the unwind** — the v4
parked-interim rule requires re-derivation against the rules in force **at unwind time**, and a
pre-authorized sequence is the failure that broke park #11.

## 7. Release

**v0.17.2**, cut alone. Bump **both** version strings (`.claude-plugin/marketplace.json` `"version"`,
`skills/vlt-setup/assets/module.yaml` `module_version`). Run
`uv run tools/package-lint.py --expect-version 0.17.2` and **tag only on exit 0**, recording the PASS
summary line in the release commit. ff-merge to `main`, tag `v0.17.2`, push main + tag.

⚠ **Sequencing — and note what it does and does not constrain.** The owner's **second consecutive
`vlt-lint --full`** (build-2 (8)'s discharging event) must be taken **before** this release. The
reason is **not** this build's convention edit: the cache's ruleset fingerprint carries
`module_version` as one of its four slots (`full-scale.md` step 2), so **every release invalidates
every record by construction** — *"the first full run after any release is a COLD one."* Any release
forfeits the warm sweep, whatever it contains.

**But build-6's own checks impose no such constraint**, because none of them needs a full sweep — see
(4). If the second full sweep has not run when this build is ready, **the sweep still goes first**,
and that is build-2 (8)'s constraint, not build-6's.

⚠ **Delete any `**/.decision-log.md` build artifacts before the release commit** — `vlt-upgrade`'s
own-the-apply is a filesystem copy and cruft on disk ships into vaults.
