# State the digest form for pageHashes — an unspecified key term silently runs every full lint cold

origin: mggower/bmad-module-vlt#20

- **filed:** 2026-09-16 (GitHub issue opened 22:17:15Z via the vlt-feedback rail)
- **origin vault:** vlt-core · **module_version:** 0.18.1 · **rail_contract:** 1 · **kind:** defect
- **acceptance_vault:** any vault with an existing `_agent/lint-cache.json` sidecar and enough wiki pages to cross the fan-out threshold (~30); acceptance needs two consecutive full sweeps with no release between, the second reusing the first's records. A vault with no prior sidecar cannot reproduce it — the first sweep is legitimately cold either way, which is part of why this hid.

## what_happened

A full-mode `vlt-lint` sweep taken right after the 0.18.0 → 0.18.1 upgrade went **100% cold** — 0 of 144 sidecar records reused, 152 pages queued for a fresh scan instead of ~20 — with nothing that should invalidate the cache having moved.

The cause is a specification gap, not the upgrade. `references/full-scale.md` step 2 pins the digest form for `convention_digests` to the byte — *"**truncation** the first **16 hex characters**, lowercase"* — precisely so that "an executor that follows them lands on the same value every run, which is the property that failed."

**Step 1 gives `pageHashes` no form at all.** It names an instrument (`shasum -a 256`) and stops. Both halves of the cache key are per-run executor output; only one of them has a specified form. So an executor that emits the full 64-character sha256 — the literal output of the named instrument — mismatches a sidecar written by one that truncated, on every page, and every sweep runs cold forever.

What makes it worth a build rather than a doc edit is that **no instrument can see it**. The cold run is indistinguishable from a healthy one at every surface the module offers:

- `files_checked: 152 / files_cached: 0` is a *legal* rendering — it is exactly what a genuinely cold sweep prints, and `lint_cache:`'s cold branch has vocabulary for it.
- `cache_miss_terms` correctly reports `page_bytes` for all 144 — but `page_bytes` misses are **churn, not cold**, and step 5 instructs the SKILL to render the cold reason "from the other two". A 100% `page_bytes` miss rate therefore reads as "the whole wiki changed", which is a story a vault can honestly tell.
- Nothing compares the *form* of the incoming digest against the stored one. A 64-char term and a 16-char term are both strings; they simply never compare equal.

## evidence

The reader's key, module source `skills/vlt-setup/assets/workflows/vlt-lint-full.js:427`:

```js
const runKey = (slug) => `${pageHashes[slug] || ''}|${scanFingerprint}|${rulesetFingerprint}`
```

`pageHashes[slug]` is the **first** term. Its form is unspecified at `skills/vlt-lint/references/full-scale.md` step 1.

**Minimal triggering fragment.** One page. The sidecar record's stored key:

```
key: 8410d5ed45c6b19c|5e24495f339c96ff1dfd|72a78bcb85f08e7b69
     ^^^^^^^^^^^^^^^^ 16 chars
```

What the spec's named instrument returns for the same bytes:

```
8410d5ed45c6b19c7f5fa80c848d6210060d911e0fba3f2bbcfb16e70f7132f0
^^^^^^^^^^^^^^^^ the stored value is this prefix
```

**The ruleset provably did not move**, so this is not a legitimate cold sweep: all three scanner-read convention digests matched the sidecar's stored `components` exactly; `scan_model` was unchanged (`haiku`); and the scanner surface was byte-identical across the upgrade (`pageScanPrompt` + `PAGE_SCAN` md5 `e54b7990…` / `2b84caff…` at both 0.18.0 and 0.18.1).

**Specimen manifest — the complete set: all 144 records missed, 100%, no exceptions.** The set is total by construction (the mismatch is in a term every key carries), so its members are exactly the sidecar's 144 slugs, re-derivable with:

```
uv run --quiet skills/vlt-lint/scripts/lint-cache.py read --vault-root {vault} \
  | python3 -c "import json,sys; [print(r['slug']) for r in json.load(sys.stdin)['records']]"
```

After truncating the digest to 16 characters and re-running, **132 of 152 pages matched on the `page_bytes` term** — the remaining 20 being genuine churn plus 8 pages absent from the sidecar. That delta is the defect's whole cost: ~130 needless scanner dispatches per full sweep, indefinitely.

## provenance_guess

A guess — ground it before building.

- `skills/vlt-lint/references/full-scale.md` step 1, the `pageHashes` sentence: add the form clause step 2 already carries for `convention_digests` (instrument, encoding, truncation).
- **The spec already knows this is owed.** Step 3's parenthetical defers the whole-derivation executable *"gated on the `pageHashes` digest-form filing."* This is that filing.
- Hardening beyond the doc fix, since a doc fix is what failed here before: have `vlt-lint-full.js` refuse a `pageHashes` entry that does not match `/^[0-9a-f]{16}$/` at the same pre-dispatch gate that already refuses wrong-typed slots by name. The gate exists; the digest form is simply not among the things it checks. A spec sentence binds only executors that read it, and the reader is the only place the two executors actually meet.
- Related but distinct: the Cycle 14 filing *"the findings cache cannot round-trip — the writer and the reader disagree"* fixed the record **shape** and `rulesetFingerprint`'s algorithm, specifying the key as `${pageHashes[slug]}|${cache_fingerprint}` — and never pinned the form of `pageHashes[slug]`. This is that residue. Issue #13 touches `pageHashes` only as payload bulk and does not address its form.

**Sharper than filed — pin the form, never the tool.** Step 1 does not merely omit a truncation rule; it explicitly licenses a different instrument: *"`shasum -a 256` over each page file is the expected instrument, but the rule names a property, not a tool."* So conformant executors may legally diverge on the digest **algorithm** for `runKey`'s first term, not only on its truncation. That rules out pinning the tool as the fix — it would contradict the operating contract's instrument rule — and leaves the reader-side refusal as the only thing that actually closes the gap. Note also `skills/vlt-setup/assets/workflows/vlt-lint-full.js:420`, which comments that "two conformant executors cannot disagree about it" — said of the **third** key term. The **first** term is exactly where they can, and that comment is a natural site for the refusal to land beside.

*(Refinement grounded against module source factory-side and recorded in the Cycle 16 roadmap, commit `7270266`.)*

## kind

defect

## origin_vault

vlt-core

## acceptance_vault

Any vault with an existing `_agent/lint-cache.json` sidecar and enough wiki pages to cross the fan-out threshold (~30). Acceptance needs two consecutive full sweeps with no release between: the second must reuse the first's records. A vault with no prior sidecar cannot reproduce it — the first sweep is legitimately cold either way, which is part of why this hid.

## module_version

0.18.1

## rail_contract

1


