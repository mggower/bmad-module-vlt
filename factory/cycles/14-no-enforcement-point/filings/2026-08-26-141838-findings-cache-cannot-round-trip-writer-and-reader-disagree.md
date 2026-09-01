# The findings cache cannot round-trip — the writer and the reader disagree, and no instrument can see it

**Filed:** 2026-08-26 · **Vault:** `{field-vault}` · **Module:** v0.16.1
**Instrument:** a second full-mode `vlt-lint` sweep, run deliberately as the acceptance test for
Cycle 12 build-2 check (5) and **cancelled before completion** — the verdict was reached without
needing the sweep to finish.
**Filed by:** the factory session, from a `{field-vault}` session's relayed report, **not** through
the `vlt-feedback` rail — so this filing carries no `origin:` header and is not rail-materialized.
Do not re-file it upstream: a rail copy would materialize a second time (the `origin:` header is
the only idempotency key, and this filing has none). Every claim below was re-verified factory-side
against shipped module source and against the live sidecar on disk before filing.
**Bears on:** Cycle 12 build-2 acceptance check (5) — this filing **refutes** it.

## What happened

The test conditions were as favourable as they can be: **146 wiki pages, 0 of 146 changed** since
the prior full sweep at 2026-08-26 10:46 (instrument: `python3 os.path.getmtime`, unwrapped),
byte-identical corpus, same `module_version`, same conventions, **no release in between**.

**146 pages queued for a fresh scan. 0 served from the cache.**

This is the corrected bound Cycle 12's b2(5) was re-bounded to hours earlier — two consecutive full
runs under the same ruleset fingerprint — and the mechanism failed it. Two independent defects,
**either one alone sufficient to guarantee a permanent 100% miss rate.**

## Defect 1 — the sidecar schema mismatch: the spec tells the writer to produce what the reader rejects

**The reader's contract** (`skills/vlt-setup/assets/workflows/vlt-lint-full.js`):

- `:243` — `cachedScans.filter((c) => c && c.slug && c.key && c.scan)`. A record must carry **all
  three** of `slug`, `key`, `scan` or it is dropped at load.
- `:344` — `cacheBySlug.get(p.slug).scan`. The scan must be **wrapped**, not inline.
- `:242` — `runKey = ${pageHashes[slug]}|${scanFingerprint}|${rulesetFingerprint}`.

**What the spec tells the SKILL to write** (`skills/vlt-lint/references/full-scale.md`, step 5, the
findings-cache sub-bullet): *"one record per page adjudicated this run — the workflow's returned
`fresh_scans`, plus the reused records that are still valid."*

**`fresh_scans` is the wrong shape.** At `:293` the workflow pushes the agent's **raw PAGE_SCAN
return** (`freshScans.push(r)` where `r = part[k]`), and `:723` returns that array unmodified. Those
objects carry no `key` and are not wrapped in a `scan` field. **Following the spec literally
produces a file the reader discards in its entirety.**

**On disk, that is exactly what happened.** `_agent/lint-cache.yaml` holds 146 records in the flat
scan shape — `slug:` plus the PAGE_SCAN fields inline (`available`, `title`, `outbound_links`, …).
`grep -c "^    key:"` returns **0**.

**The root cause is the spec, not the writer's execution.** The key *is* derivable SKILL-side —
`:722` returns `cache_fingerprint` as exactly `${scanFingerprint}|${rulesetFingerprint}`, so the
correct record is `{slug, key: "${pageHashes[slug]}|${cache_fingerprint}", scan: <the fresh_scans
entry>}`. **That derivation appears nowhere in the spec.** It has to be reverse-engineered from the
workflow source by every implementer.

**Sharpening the field report did not make:** the sidecar stores `fingerprint:` **once at the top
level** (`_agent/lint-cache.yaml:1`, `"bda9b0752f5e85c51743|980d749d9acf418e"`) and stores **no
per-page digest anywhere**. So the file cannot express the reader's key even in principle — the
writer kept the run-level half of `runKey` and dropped the per-page half entirely. A reader fix
alone cannot rescue an existing sidecar; the written shape is lossy, not merely mis-nested.

## Defect 2 — `rulesetFingerprint` has no single-homed deterministic algorithm

`full-scale.md` step 2 enumerates the fingerprint's **inputs**, in order — the installed
`module_version`; the skill's `depends_on:` pin vector verbatim; the digest of each judged
convention **as merged with its overlay**; the digest of `references/checks.md` — and **specifies no
digest construction**: no separator, no hash algorithm, no encoding, no truncation, no canonical
member list.

**Consequence: two runs over an identical ruleset compute different values.** The 10:46 run recorded
`980d749d9acf418e`; an independent derivation over a *provably unchanged* ruleset produced
`66d27a0e6cd8fabe`. Both are 16 hex characters, so the truncation length was guessed alike and the
content was not.

`reusable()` at `:244-245` requires `rulesetFingerprint` non-empty **and** the composed key to match
exactly. So **the cache is structurally incapable of ever hitting across sessions** — which is the
only case it exists for. A within-session hit was never the feature.

**This also silently defeated the honest-reporting intent.** The prior report's `lint_cache:` line
attributed its cold run to a legitimate `module_version 0.16.0 → 0.16.1` crossing
(`_agent/lint-reports/2026-08-26-1046-lint.yaml:146`). That attribution is true and **masked the
fact that the mechanism would have missed regardless.** An honest line pointed at the wrong cause.

## The observation that let both defects persist — no instrument can see this failure

Not a third defect; the reason the first two were invisible.

The version-skew defence at `full-scale.md` step 4 narrows its refusal to `files_checked` **and**
`files_cached` **both** `0`. A run that cold-scans everything *because the cache is broken* has
`files_checked: 146` — full coverage, an honest report, no refusal. It is indistinguishable from a
healthy cold run.

**There is no check anywhere that a cache written by run N is readable by run N+1.** Every shipped
instrument reports the cache's *counts*, never its *round-trip*. Build-2's own acceptance proved the
mechanism on a two-run temp fixture inside one harness invocation — where the SKILL-side write step
never ran, because the harness stubbed it. The one seam that breaks in the field is the one the
at-rest instrument could not exercise. This class of failure can persist indefinitely.

## Candidate directions (not rulings)

1. **Move the wrapping into the workflow** — have it return write-ready `{slug, key, scan}` records
   instead of raw `fresh_scans`, so the read and write shapes **cannot drift apart again**.
   Preferred over amending the spec: it removes the derivation rather than documenting it.
2. Failing that, amend `full-scale.md` step 5 to state the record shape and the key derivation
   explicitly.
3. **Single-home the `rulesetFingerprint` algorithm as executable steps** (canonical member order,
   separator, digest algorithm, truncation) — or better, **move its computation into the workflow**
   so one implementation computes it rather than prose being re-derived per caller.
4. **Add a round-trip acceptance check**: write the sidecar, read it back, assert every record is
   reusable against an unchanged corpus. This is what the cancelled sweep was manually standing in
   for, and it is the check whose absence made both defects invisible.
5. **Widen the step-4 refusal predicate**, or add a distinct signal, so "cold because the cache
   could not be read" is distinguishable from "cold because the ruleset legitimately moved."

## Vault state

No writes, no fixes applied, no report persisted, no log line, no commit; working tree clean.
`lint-debt` is **not** reset — the vault still owes a completed full sweep. The 2026-08-26 10:46
report remains the current health picture and is hours old, so nothing is at risk from the
cancellation.

The cancelled run's SKILL-side passes all completed and **independently reproduce** the 10:46
results — the PARA scan (65 files; 27 missing-attestation matching the parked count; 31
no-frontmatter; 5 brief issues at `type: research`; both classes still adjudicated `parked-interim`
against issues #15/#16), the governance checks (all 9 conventions coherent including workflow-asset
acks; bases pristine vs baseline; 2 overlays clean; no expired deferrals; 21 capabilities lane-safe;
2 specs, 2 `consult_retroactive`, 0 `consult_missing`), and the research-zone candidacy pass (147
notes, 26 carrying `revisit_after:`, 0 `revisit_due`, 15 `linkage_ripe` at 10.2%, inside the
expected 8–14% band). **That reproduction is itself evidence:** the corpus genuinely had not
changed, which is what makes the 0-of-146 cache result conclusive rather than circumstantial.
