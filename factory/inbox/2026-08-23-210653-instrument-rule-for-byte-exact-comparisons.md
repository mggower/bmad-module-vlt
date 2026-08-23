# State an instrument rule for byte-exact comparisons — a wrapped diff can report identical for differing files

- **filed:** 2026-08-23 (GitHub issue opened 2026-08-23T21:06:53Z)
- **origin:** `mggower/bmad-module-vlt#8`
- **origin vault:** vlt-core
- **kind:** candidate
- **module_version:** 0.14.0
- **rail_contract:** 1
- **acceptance vault:** any vault whose shell environment installs a command-rewriting hook — that is where the failure reproduces. A vault without one cannot verify the fix, only that the rule reads sensibly.
- **materialized by:** `inbox-capture` GitHub intake (Arc 11 capture run, 2026-08-23). Body
  below is the issue payload as filed, unedited. Grounding lives in the arc roadmap, not here.
- **labels at materialization:** `vault-filed`, `vault-accepted`, `field:candidate`

---

### what_happened

A shipped op's verdict was a byte-exact comparison, and the tool it reached for lied in the
dangerous direction. During a base-vs-baseline divergence check, the shell `diff` the op
invoked had been transparently rewritten by a token-optimizing command wrapper installed at
the environment level (in this vault's case the `rtk` CLI hook, but the class is what
matters). The wrapper printed a summarized `[ok] Files are identical` for two files that
genuinely differed. Checksums and `python3 difflib` both showed the divergence correctly.

The failure direction is what makes this worth a module rule rather than a local workaround.
A false *differs* costs a second look. A false *identical* arrives as health and closes the
question — it is indistinguishable from a clean run, so nothing downstream ever revisits it.
For a divergence check, "no divergence" is exactly the answer that gets believed and acted on.

This vault has worked around it for three consecutive upgrades, bypassing the wrapper by hand
each time. The module states no instrument discipline anywhere, so each session re-derives the
workaround from its own prior records rather than reading a rule.

A second, subtler half surfaced when the rule was written down locally: because the wrapper
rewrites **every** command transparently, an op can invoke `shasum`, be silently rewritten,
and then record — truthfully, as far as its author knows — that it "verified with sha
hashing" while a wrapper actually ran. A record of the instrument *named* is not a record of
the instrument *run*. Any rule the module ships needs both halves, or it verifies intent.

### evidence

Observed behavior, quoted: the wrapped `diff` returns `[ok] Files are identical` for a pair
of files differing by one line. `md5`/`shasum` and `python3 difflib` on the same pair both
report the difference.

Generalized locations where a module-shipped act's verdict *is* a byte comparison:

- base-vs-baseline convention divergence (`_meta/conventions/{name}.md` vs the stock baseline
  copy under `_agent/conventions/.baseline/`)
- skill-asset manifest verification (the `.skill-manifest` hash walk)
- a migration's data-equality check — proving content moved without changing (e.g. a
  registry or tripwire file parsed on both sides and asserted equal)

The first two are `vlt-upgrade` pre-flight/post-flight; `vlt-lint`'s base-divergence check is
the third consumer. None of the three states which instrument to use.

Detail held vault-side, available on request: the dated local record of the three bypasses and
the council review of the local rule's wording.

### provenance_guess

**A guess — not verified against module source.** Most likely this is an absence rather than a
defect in any one file: no shipped convention's declared scope covers instrument selection.
`write-verification.md` is the nearest rival and does not fit — it governs write-side
attestation, and a divergence verdict is not a write. The natural homes would be the operating
contract's *Honest reporting* section (which already carries the general form: "a transcription
of the record is testimony about the record, not the record" — this is that rule applied to an
instrument class), with the concrete obligation cited from `vlt-upgrade`'s divergence steps and
`vlt-lint`'s base-divergence check.

Proposed generic shape, offered as a starting point rather than a specification:

> An act whose verdict **is** a byte-exact comparison uses an **unwrapped** instrument — no
> filtering, summarizing, or token-optimizing layer between the bytes and the verdict —
> confirms the instrument actually ran unwrapped, and names in its record which one ran.
> Reading a diff to orient or to show a human what moved is ordinary use and is untouched.

Naming the property (*unwrapped*) rather than a tool matters: the wrapper in question is one
instance, and a future one should inherit the rule without an edit.

### kind

candidate

### origin_vault

vlt-core

### acceptance_vault

Any vault whose shell environment installs a command-rewriting hook — that is where the
failure reproduces. A vault without one cannot verify the fix, only that the rule reads
sensibly.

### module_version

0.14.0

### rail_contract

1


---

## Pre-materialization issue thread — `mggower/bmad-module-vlt#8` (carried verbatim)

_Both comments predate materialization; the second explicitly asks capture to carry both
instances. Recorded here so the thread is not lost — neither is an `amended`-label
consumption (the label was never applied to #8)._

### Comment 2026-08-23T21:33:18Z (mggower)

Triaged 2026-08-23, grounded against module source @ `283fe5d` (v0.14.0). **Accepted.** Verified: the proposed home exists and already carries this rule's family — `vault-operating-contract.md` *Honest reporting*, whose "a transcription of the record is testimony about the record, not the record" is the general form this candidate instantiates for instrument selection. Site check: `vlt-upgrade` base-vs-baseline and `vlt-lint`'s convention-base-divergence check both name no comparison instrument (confirmed); one grounding correction — the skill-asset manifest walk *does* specify its instrument (an in-process hashing script), so only this filing's second half (confirming the instrument actually ran unwrapped) applies to that site. Both halves of the proposed rule are retained. Materializes into the factory inbox at the next capture run; routes to Arc 11 ideation.

### Comment 2026-08-23T21:55:12Z (mggower)

Second field instance from vlt-core, 2026-08-23, same wrapper class, different verb: during a scoped lint, the wrapped `find` returned all 147 wiki pages for a `-newermt` scoping query; a direct `os.stat` comparison put the true count at 0 wiki / 0 research / 2 sessions / 4 PARA. Scope was taken from `os.stat` and the discrepancy recorded in the run's `coverage_caps`. The vault-local rule as minted scopes to byte-exact verdicts and does **not** reach a scoping query — so if this candidate lands upstream, its trigger may want to be "any instrument whose output a verdict rests on", not "byte-exact verdicts". Recorded pre-materialization so capture carries both instances.

