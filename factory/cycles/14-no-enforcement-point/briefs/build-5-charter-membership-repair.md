---
build: 5
slug: charter-membership-repair
cycle: 14-no-enforcement-point
kind: hot-fix repair build
briefed: 2026-08-27
built: 2026-08-27
release: v0.17.1
status: 'BUILT + RELEASED. Owner-ruled hot-fix (2026-08-27) over the defect filed at
  `factory/inbox/2026-08-27-171000-operational-record-class-has-two-memberships.md` — a
  contradiction shipped by this cycle''s own build-3 in v0.17.0, hours earlier the same day.
  **Six sites repaired across four files** (one of them, `vault-operating-contract.md:66`, was NOT
  in the filing and was found only by the membership check this build builds). **Handshake: BOTH
  conventions bumped** — `write-verification.md` 4→5 (5 consumers re-acked) and `extraction.md` 8→9
  (4 consumers re-acked); ruling and reasoning in §3. `frontmatter.md` did NOT move (§3c).
  `vault-operating-contract.md` edited ⇒ `vault-rule-card.md`''s `derived_from:` re-stamped (C6).
  All gates green: package-lint A/B/C/E PASS (D PASS at the tag), `PAGE_SCAN` measured **3676**
  (unchanged — no content edit entered the schema), bipartite-consistent both directions on both
  moved conventions, 10/10 enumerating sites agree on `charter | record | register`, 0 `ST-N` in
  the shipped surface. **No deliberate deviations from the brief.**'
---

# Build 5 (repair) — the operational-record class has one membership

*A hot-fix, so this is a **record**, not a full brief: the direction was owner-ruled before the
build opened and was not re-derived here.*

## 1. The defect

`extraction.md` v8 named the Layer-3 **operational-record class** with two different memberships,
and the attestation exemption followed the narrower one. A `charter` file was therefore a
recognized PARA `type:` **and** outside the class that recognition places it in.

Direction, **owner-ruled 2026-08-27 and not re-opened here: `charter` BELONGS.** Two independent
long-standing sites (`extraction.md:84`, the recognized `type:` set; `:192`, the attestation
posture, which predates build-3) say so, as does `vault-operating-contract.md:70`. Build-3's new
`:190` was the lone outlier and `write-verification.md:55`'s exemption copied its short list.

**Field-measured consequence** (from the v0.17.0 upgrade post-flight on `{field-vault}`): of 29
unattested `author: agent|hybrid` Layer-3 files outside `{wiki}`, exactly 1 `record` file was
exempted and the 1 `charter` file was **not** — sitting in attestation jurisdiction despite being
an operational record.

### 1a. Why build-3's own check did not catch it — the blind spot this build closes

Build-3's acceptance check (4) asserted **three-surface agreement**: the class is *named* at four
surfaces and *defined* at exactly one (`extraction.md:190`, one grep hit). **Both halves were
true**, and the check was discharged as written. It tested **single-home-ness** — that only one
site *defines* the class — and never compared **members** between the naming sites and the
defining site. A class can have exactly one definition and still be named elsewhere with a
different member list; that is precisely this defect, and it sat in the check's blind spot.

This build's **membership-agreement check** (§4.1) is the missing comparison: it does not ask *how
many sites define the class*, it asks *do all sites that enumerate it name the same members*. That
is the enforcement point the cycle's through-line demands, applied to the cycle's own repair.

**It earned its keep immediately:** it found a **sixth** site the filing had not — the Layer-3
entry condition at `vault-operating-contract.md:66` — which a site-list copied from the filing
would have shipped still broken.

## 2. Sites changed — six, across four files

| # | Site | Change |
|---|---|---|
| 1 | `skills/vlt-setup/assets/governance/_meta/conventions/extraction.md:190` | The class's **definition site**. `record`/`register` → `charter`, `record`, `register`; the class predicate rewritten (see below). |
| 2 | `skills/vlt-setup/assets/governance/_meta/conventions/write-verification.md:55` | The **attestation exemption** (*Scope rule*). `type:` is `record` or `register` → `charter`, `record` or `register`. |
| 3 | `skills/vlt-lint/references/checks.md:17` | `para_missing_attestation`'s **Population carve-out** — where the rule actually binds. `type: record` or `type: register` → `type: charter`, `type: record` or `type: register`. (The carve-out already covered a *container-sited* `charter.md` by filename; it did not cover a `type: charter` file sited outside a container, which the class definition explicitly admits.) |
| 4 | `skills/vlt-lint/references/checks.md:17` | Same finding's **Legal response** — retype to the class (`type: record`/`register`) → (`type: charter`/`record`/`register`). |
| 5 | `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md:66` | **Not in the filing — found by the membership check.** The Layer-3 **entry condition**: the class `(type: record`/`register)` carries no attestation pair → `(type: charter`/`record`/`register)`. |
| 6 | `skills/vlt-setup/assets/governance/_meta/vault-rule-card.md:11` | `derived_from:` sha256 re-stamped to `8f8a7116…` — consequence of #5; package-lint **C6** hashes the contract. |

### 2a. The class predicate, rewritten rather than merely widened

`:190` defined the class as *"dated, append-shaped, attributed per entry"*. A **charter is not
append-shaped** — it is the stable frame (outcome, scope, definition-of-done, human-gated). Simply
prepending `charter` to that predicate would have retired one contradiction and shipped another.

The repaired definition states the property that actually unites all three — **an operational
record, not a knowledge artifact; attributed in its own body rather than by an attestation pair;
carrying no `verified_by:`/`verified_at:`** — and then names the shape difference explicitly:
`record`/`register` are additionally dated and append-shaped, `charter` is the stable frame, *"a
**shape difference within one class**, never a membership difference"*. This is almost certainly
the seam the original drift opened along, so it is now stated rather than left to be re-derived.

### 2b. Deliberately NOT changed

- `extraction.md:45` and `vault-operating-contract.md:66`'s second clause name the **container
  maintenance surface** — *dated, attributed appends to a container's `record.md`/`register.md`*.
  A charter is human-gated and not appended to, so `record`/`register` there is **correct**, not
  drift. The membership check carries an explicit exclusion for this shape, with that reasoning in
  the script comment, so a future run does not "fix" it.
- `frontmatter.md:71` and `:173` already named all three correctly. No edit ⇒ no bump (§3c).
- `vault-operating-contract.md:70` already named all three correctly.

## 3. The version-handshake ruling

### 3a. `write-verification.md` 4 → 5 — RULE CHANGE (mandated, not ruled)

Its **jurisdiction genuinely narrows**: a partner may now legally leave a `charter` file
unattested where yesterday it could not. Behaviour visible to every consumer changes. Bumped
4 → 5; **all 5 consumers re-acked in the same build** — `vlt-ingest`, `vlt-extract`,
`vlt-research`, `vlt-lint`, `vlt-lint-full.js`.

### 3b. `extraction.md` 8 → 9 — RULE CHANGE (my ruling; the delegated call)

The case for calling it a **prose correction**: `:84` and `:192`, in the *same file at the same
version*, already state the three-member membership; `:190` was an incomplete restatement, so the
file's net rule content arguably never excluded `charter`.

**I ruled it a rule change and bumped.** Three reasons, the third decisive:

1. **`:190` is the class's designated definition site** — *"cited there, defined here"*. The
   convention itself appoints that line as the answer, and `write-verification.md` and `checks.md`
   both cite it rather than `:84`. What the definition site says **is** the rule; a consumer that
   read the appointed home got a different answer yesterday than it gets today. That is movement,
   not clarification.
2. **The consequent behaviour of consumers changes.** `vlt-lint` (via `checks.md:17`) carves a
   different population out of `para_missing_attestation` after this build than before. A
   convention edit that moves a shipped check's population is not prose.
3. **The standing instruction is to bump under genuine uncertainty**, and this is genuinely
   arguable — which is exactly the condition the rule names. An unnecessary bump costs 4 re-acks
   and one release; a missed one is the failure mode this repo has been bitten by, and it is the
   failure mode *this very build is repairing*. Ruling the ambiguous case in favour of the cheap
   error is the only defensible direction here.

Bumped 8 → 9; **all 4 consumers re-acked** — `vlt-extract`, `vlt-lint`, `vlt-track`, `vlt-query`.

### 3c. `frontmatter.md` — does NOT move, and why

It moved 13 → 14 in v0.17.0 *"in coordination, no independent rule movement"*. Here it is not
edited **at all**: `:71` and `:173` already name `charter`, `record`, `register` correctly, and
both explicitly defer the PARA population's closed set to `extraction.md`. A convention that
carries no edit and whose rule content is unchanged has nothing to hand its consumers; bumping it
would spend 8 re-acks to announce a change that did not occur, and would train the next reader
that a version bump means "a neighbour moved" rather than "this rule moved". It stays at **14**.

### 3d. `vault-operating-contract.md` — edited, deliberately NOT handshaked

Per the standing rule the contract uses single-home + pointers instead of `version:`/`consumers:`.
Its edit is discharged instead by re-stamping `vault-rule-card.md`'s `derived_from:` sha256
(site #6), which package-lint **C6** verifies by machine.

### 3e. E7 — the in-prose pin gate did its job

`vlt-lint-full.js` recites `write-verification@4` in prose at `:684` (a code comment on the
attestation constants), outside the `// depends_on:` header E5 owns. Bumping the convention would
have left that recitation stale and **E7 would have failed the release** — the check working as
designed. Re-stated to `@5` alongside the header. `extraction` is not recited in any workflow body
and `vlt-lint-full.js` does not ack it, so extraction's bump owed no in-prose repair.

## 4. Verification — results

### 4.1 Membership agreement across every enumerating site — the new check

Script: `scratchpad/membership.py` (a factory-side at-rest instrument, not shipped). It scans the
governance bundle and `vlt-lint`'s references for every line that enumerates ≥2 class members in a
class/`type:` context, excludes the container-maintenance shape (§2b), and asserts every remaining
enumeration names exactly `{charter, record, register}`.

**Before the repair it FAILED on 3 sites** (`extraction.md:190`, `write-verification.md:55`,
`vault-operating-contract.md:66`) — including the one the filing had missed. **After:**

```
OK  extraction.md:84                members=['charter','record','register']
OK  extraction.md:190               members=['charter','record','register']
OK  extraction.md:192               members=['charter','record','register']
OK  write-verification.md:55        members=['charter','record','register']
OK  vlt-lint/references/checks.md:17  members=['charter','record','register']
OK  vlt-lint/references/checks.md:19  members=['charter','record','register']
OK  frontmatter.md:71               members=['charter','record','register']
OK  frontmatter.md:173              members=['charter','record','register']
OK  vault-operating-contract.md:66  members=['charter','record','register']
OK  vault-operating-contract.md:70  members=['charter','record','register']

enumerating sites compared: 10
MEMBERSHIP AGREEMENT: all 10 enumerations name ['charter', 'record', 'register']
```

Grep confirmation: `grep -rn "record.*register\|register.*record" skills/ .claude-plugin/ |
grep -vi charter` returns **no** class enumeration — every surviving hit is the maintenance
surface or unrelated prose.

### 4.2 Bipartite consistency — both directions, both moved conventions

- **`extraction@9`** — `consumers: [vlt-extract, vlt-lint, vlt-track, vlt-query]`. Forward: all 4
  ack `extraction@9`. Reverse: the set of files acking `extraction@` is exactly those 4 SKILL.md —
  no un-listed acker. ✅
- **`write-verification@5`** — `consumers: [vlt-ingest, vlt-extract, vlt-research, vlt-lint,
  vlt-lint-full.js]`. Forward: all 5 ack `@5`. Reverse: the set acking `write-verification@` is
  exactly those 5 — no un-listed acker. ✅
- Stray-old-pin sweep: `grep -rn "extraction@8\|write-verification@4" skills/ .claude-plugin/` →
  **none**. ✅

### 4.3 Other gates

| Gate | Result |
|---|---|
| `uv run tools/package-lint.py` | `A/B/C/E PASS` — includes **C6** (rule-card digest) and **E7** (in-prose pins) |
| **E6** `PAGE_SCAN`, measured with `_E6_NODE_EXTRACTOR` | **3676** — identical to the pre-build measurement; budget 3700. No content edit entered the schema, as intended (all six sites are prose/frontmatter). Other schemas unchanged: `INDEX_SCAN` 823, `CLUSTER_FINDINGS` 1630, `PAIR_FINDINGS` 376. |
| `node --check` on all three workflow assets | PASS (only `vlt-lint-full.js` was touched) |
| `ST-N` ids in the shipped surface | **0** — not reintroduced |

## 5. Acceptance checks

*Per cycle ruling **D3 as amended** (bounded ⇒ ship-verifiable ⇒ **it GATES**) and rule **R1**
(each ship-verifiable check names the seam its instrument crosses).*

1. **`[ship-verifiable — GATES]`** Every site in the shipped surface that enumerates the
   operational-record class names exactly `charter | record | register`. **Instrument:** the
   membership check (§4.1), re-run at rest against shipped source at the v0.17.1 tag.
   **Seam crossed:** factory script → shipped governance bundle + `vlt-lint` references, at rest.
   *(Graded at build: **PASS**, 10/10.)*
2. **`[ship-verifiable — GATES]`** Both moved conventions are bipartite-consistent in both
   directions and no consumer still pins `extraction@8` or `write-verification@4`.
   **Instrument:** package-lint **E1** (handshake-bipartite) + **E5** + the stray-pin grep.
   **Seam crossed:** convention frontmatter ↔ consumer `depends_on:`, including the asset-node
   half. *(Graded at build: **PASS**.)*
3. **`[ship-verifiable — GATES]`** `vault-rule-card.md`'s `derived_from:` sha256 equals the shipped
   contract's digest. **Instrument:** package-lint **C6**. **Seam crossed:** derived artifact →
   its source contract. *(Graded at build: **PASS**.)*
4. **`[ship-verifiable — GATES]`** No workflow body recites a stale convention pin.
   **Instrument:** package-lint **E7**. **Seam crossed:** workflow prose ↔ that file's own
   `// depends_on:` header. *(Graded at build: **PASS**.)*
5. **`[field-contingent — does NOT gate]`** On `{field-vault}`, after the v0.17.1 upgrade, the
   next full `vlt-lint` sweep reports the `charter` file **out** of `para_missing_attestation`
   jurisdiction — the unattested Layer-3 count outside `{wiki}` falls from 28-in-jurisdiction to
   **27**, with both the `record` and the `charter` file exempted. **Event:** the owner runs
   `vlt-upgrade` to 0.17.1 then one `vlt-lint --full`. **Performer:** the owner. **Tagged
   field-contingent** because it needs a live vault's corpus and an owner-initiated sweep; nothing
   in the build or release causes it. *(This is the check that measures the defect's actual harm
   being undone, on the very file that surfaced it.)*
6. **`[field-contingent — does NOT gate]`** `{field-vault}`'s `write-verification.md` park
   resolves **fully** on the 0.17.1 upgrade — the partial resolution recorded on the 2026-08-27
   discharge run was blocked by exactly this contradiction. **Event:** the post-upgrade
   `parked_interims_review` shows the park unparked, not re-parked. **Performer:** the owner.

## 6. Release

**v0.17.1** — dual version bump (`.claude-plugin/marketplace.json` + `module.yaml`), CHANGELOG
entry stating the repair in rule terms for `vlt-upgrade`'s `governance_rule_changes:` verbatim
read, `uv run tools/package-lint.py --expect-version 0.17.1` green including group D, release
commit on `main`, annotated tag `v0.17.1`. **Not pushed — the push is owner-gated.**

The CHANGELOG additionally records that the first full lint after this release is **cold by
construction** (both convention digests move, so the ruleset fingerprint moves) — the **third**
forced cold sweep of 2026-08-27.
