---
title: 'Build #10 (Round 2) — 0.3.0 upgrade hardening: the three field-surfaced defects'
status: 'BUILT — acceptance batched into the deferred ledger'
module_code: 'vlt'
created: '2026-06-24'
derives_from:
  - 'inbox/2026-06-24-123000-upgrade-0.3.0-field-notes.md (defects #1–3)'
  - 'skills/reports/inbox-evolution-roadmap.md (Round 2 capture + phasing row)'
phase: 'Round 2 — stop the bleeding (post-acceptance robustness)'
---

# Build #10 — Round 2: 0.3.0 upgrade hardening

## The finding that defines this build

The full roadmap (build-3→9) shipped and the **first real `vlt-upgrade`** ran on `vlt-core`
(0.2.0 → 0.3.0, own-the-apply) — discharging the deferred acceptance ledger *in anger*. Exercising
the durability machinery on a live, evolved vault is exactly what it was built to make safe, and it
worked (all 4 local mints preserved, zero destruction). It also did what a real run always does:
**surfaced three concrete defects the unit-tests couldn't** — two coherence/hygiene bugs the module
shipped, and one brittleness the upgrade tripped on. All three are confirmed against current module
source. They are low-risk, well-specified, and Phase-A-shaped ("stop the bleeding") — so they bundle
into one build.

A fourth signal — `vlt-track` as an upstream candidate — is **out of scope for this build** (it is a
real op-skill design that threads the build-7 capability-object + personalized-extraction strands, not
a defect fix). Captured as a Round 2 candidate in the roadmap; ideated/built separately.

| # | Defect | Grounded state in module source | Provenance |
|---|---|---|---|
| **1** | Contract Beat 2 dropped the dispatch-slice drain read; the bus silently stalls | Confirmed — `vault-operating-contract.md:164` reads `index/log/backlog/thread/capabilities` with **no** dispatch slice, while `:221` (relay-when-done reflex) explicitly depends on "the recipient … drains it via the ordinary pickup loop on its next orient." | **build-4 coherence gap** — build-4 (`92b53d6`) added the relay reflex (`:189`) but its Beat 2 read was only `index/log/backlog/thread`; it **never wired** the corresponding drain read. build-7 (`d2f52fc`) added `capabilities/` to Beat 2 **purely additively** — it displaced nothing. (vlt-core read it as "capabilities took the slot" because its *installed* 0.2.0 had filing #9 applied locally first.) |
| **2** | 10 gitignored `.decision-log.md` ride a filesystem merge-copy into the installed vault; one clobbered the vlt-mint relocation stub | Confirmed — 10 `.decision-log.md` on disk under `skills/`; `.gitignore` carries `**/.decision-log.md` so they're absent from the *repo* but present in the *working tree* → a filesystem copy (own-the-apply) grabs them. | Build-time authoring cruft. The relocation discipline (build-6, §A1) explicitly warns against writing to `vlt-mint/.decision-log.md`; the module shipping these undermines it. |
| **3** | `merge-help-csv.py` aborts on an unquoted-comma row instead of surviving it; vlt-mint writes such rows | Confirmed — build-3's read-guard (`merge-help-csv.py:113–119`) *detects* the mis-split row but **raises `ValueError`** (aborts the whole merge before the local-mint preserve step); write-side, vlt-mint / help-row authoring emits free-text fields unquoted. | Write-side root cause + read-side intolerance. The build-3 guard was a *detector*; field use shows it must become a *survivor*. |

---

## Part 1 — Defect #1: restore the dispatch-slice drain to Beat 2

**The bug.** The contract promises a working partner-to-partner bus: a publisher fires the
relay-when-done reflex (`:221`), which appends an open pointer into the recipient's dispatch slice,
and "the recipient then drains it via the ordinary pickup loop **on its next orient**." But Beat 2 —
the orient (`:164`) — never tells the partner to read its dispatch slice. So relayed hand-offs are
appended and never picked up. The bus stalls silently; the only symptom is work that quietly never
arrives (exactly the Health-Coach→Chef stall that filing #9 was built to cure).

**The fix (single edit to `vault-operating-contract.md` Beat 2, `:164`).** Add the partner's open
dispatch slice to the Beat 2 read list, **alongside** the capabilities read (both coexist — build-7
is not touched), and add its mutation-license note. Wording to match house phrasing (literal
`_agent/dispatch.md`, since dispatch has no `{logical-name}` in the structure map — consistent with
how `:221` already refers to it):

- **Beat 2 read-list addition** — after the `capabilities/` clause, add: *"…and the partner's open
  slice of `_agent/dispatch.md` (relayed hand-offs and routed items waiting on it — drained via the
  ordinary pickup loop; see *Sessions, sittings, and hand-offs*, below)."*
- **Mutation-license note** (re-graft of what vlt-core restored) — a short sentence flagging that the
  dispatch-slice drain is **the one orient read that may mutate shared state**: draining checks an
  item off `_agent/dispatch.md`. It is deliberate (the partner acts on the item), never a silent
  activation side-effect. This is the single exception to "Beat 2 reads are read-only orientation."

**Single-home discipline held.** Beat 2 only *names* the drain and points at the hand-offs section +
`vlt-dispatch`'s pickup loop; it does not restate pickup mechanics (those stay owned by
`vlt-dispatch`, per `:221`'s existing single-home rule). Single-writer holds: draining (checking an
item off) is the recipient acting on its own slice via the pickup loop, not a write across the
single-writer line.

**Why provenance matters for the capture.** The field note (vlt-core's view) blames build-7's
capabilities read for "taking the slot." The module truth is that build-4 shipped the relay reflex
without ever wiring its Beat 2 pickup read — build-7 is innocent (additive). Same fix; the roadmap
records the correct provenance so the coherence machinery's own gap is named honestly (a relay
*reflex* shipped without its *pickup* read is precisely a convention→consumer coherence miss inside
the contract that build-4 introduced).

**vlt-core fold-back.** vlt-core re-grafted exactly this as its one intentional governance divergence
(recorded in its upgrade ledger). Once the module ships the fix, vlt-core's divergence folds back to
zero on its next upgrade (base now matches the local edit → the divergence detector reports clean).

---

## Part 2 — Defect #2: keep `.decision-log.md` build cruft out of the installed surface

**The bug.** `.decision-log.md` files are build-time authoring metadata (BMad `phase: build`
records). They're gitignored (`**/.decision-log.md`) so they never enter the *repo* — but they live
in the *working tree*. `vlt-upgrade`'s own-the-apply does a **filesystem** merge-copy from a reachable
module source (the working tree), so it copied all 10 into the live vault. One clobbered vlt-core's
`vlt-mint/.decision-log.md` **relocation stub** (the "mint history moved to `_agent/mint/` — don't
write here" pointer that build-6 §A1 created) — the exact failure mode the stub warns about.

**The fix (two layers — both, defense in depth):**
1. **Remove them from the working tree.** `git rm` is a no-op (they're untracked/ignored); delete the
   10 files from disk so a working-tree copy can't grab them. Verify none carry irreplaceable content
   first (they're build records — superseded by the roadmap + briefs, which are the durable authoring
   memory). This stops the bleeding for any copy-from-working-tree apply *today*.
2. **Copy-exclude at the apply seam.** A deleted file reappears the moment a future build writes a new
   `.decision-log.md`. So `vlt-upgrade`'s own-the-apply merge-copy (and any future installer/copy
   path) must **exclude `.decision-log.md`** from what it drags into a vault — a named exclude, not
   reliance on the tree being clean. This makes the guarantee structural: build cruft can never reach
   a vault even if a fresh one is authored.

**Artifacts:** delete 10 `skills/**/.decision-log.md`; add the copy-exclude to `vlt-upgrade/SKILL.md`'s
apply step (and note it for any installer-driven path). The `.gitignore` rule already does its job for
the *repo* — this defect is specifically about the *filesystem-copy* surface, which gitignore doesn't
govern.

**Confirms the stub's value.** This is the relocation stub earning its keep: the discipline that says
"don't write mint history into a clobber-prone skill dir" is exactly what got clobbered. Fixing the
source (don't ship the cruft) closes the loop the stub was insurance against.

---

## Part 3 — Defect #3: make CSV registration survive (and stop writing) unquoted-comma rows

**The bug.** vlt-core's live `_bmad/module-help.csv` had two rows (`vlt-agent-health-coach`,
`vlt-lint`) whose free-text fields contained commas but weren't quoted → the row mis-split into too
many columns. `merge-help-csv.py`'s build-3 read-guard (`:113–119`) **detects** this and **raises
`ValueError`**, aborting the whole merge *before* the local-mint preserve step (build-6 B1) can run —
so registration was blocked until the rows were hand-fixed. The build-3 guard was authored as a
*detector* (better than silent mis-merge); field use shows it must become a *survivor* (an upgrade
must not be blockable by one bad field). The root cause is write-side: vlt-mint and skill help-row
authoring emit free-text fields without quoting.

**The fix (both sides — owner-confirmed defense in depth):**

- **Write-side — always quote free-text fields.** Wherever a `module-help.csv` row is authored —
  `vlt-mint` (partner mints + op-skill registration) and any skill's own help-row authoring — emit
  the free-text columns (`description`, `args`/scope, `produces`) **always quoted**, regardless of
  whether they currently contain a comma (always-quote is simpler and drift-proof than
  quote-if-comma). Prevents new bad rows at the source. *Audit all current authoring sites* — grep the
  skills for `module-help.csv` writes and the merge-help CSV-writing path (`merge-help-csv.py:195`
  already uses `csv.writer`, which quotes correctly — the gap is the *hand-authored* rows vlt-mint
  emits as text).
- **Read-side — skip/repair instead of abort.** Change the `:113–119` guard from `raise ValueError`
  to **surface the offending row(s) and continue**: report the mis-split row (name + raw content) in
  the merge output, and either (a) skip just that row (preserving every well-formed row + the
  local-mint preserve step), or (b) best-effort repair by re-joining the overflow columns back into
  the last free-text field. Skip is the safe floor; repair is the nicer behavior. Either way **the
  upgrade is never blocked by one bad field** — the build-6 B1 preserve logic runs on the rest.

**Why both.** Write-side stops the disease (no new bad rows); read-side cures the patients already
infected (existing installs whose CSV was written by an older vlt-mint). Neither alone is sufficient:
write-side leaves every already-written row a landmine; read-side leaves vlt-mint forever emitting
rows that *only* survive because the reader tolerates them.

**Artifacts:** `vlt-mint/SKILL.md` (help-row authoring → always-quote), any other skill that authors a
help row, `merge-help-csv.py:113–119` (guard → skip/repair + report).

**Sibling of build-3.** Build-3 hardened the *read* side of this same CSV against mis-split (the
detector). Build-10 completes it: the *write* side stops producing the mis-split, and the read side
graduates from detector to survivor.

---

## Build order

1. **Defect #2 first (cheapest, unblocks clean future applies).** Delete the 10 working-tree cruft
   files + add the `vlt-upgrade` copy-exclude. Pure hygiene, no behavioral coupling.
2. **Defect #3 (write-side then read-side).** Quote at authoring, then soften the guard. Order within:
   write-side first (so a fresh run produces clean rows), read-side second (so old rows survive).
3. **Defect #1 last (the prose edit that wants the most care).** The Beat 2 + mutation-license edit —
   one contract file, but it's the load-bearing constitution, so do it deliberately and re-read the
   surrounding beats for flow.

No interdependencies between the three — order is by cheapness/risk, not necessity.

## Migration

- **#1:** none — idempotent text edit to the shipped contract; existing vaults pick it up on their
  next `vlt-setup` refresh / `vlt-upgrade`. vlt-core's local re-graft auto-reconciles to zero
  divergence once base matches.
- **#2:** none for vaults already upgraded (vlt-core already removed the 10 + restored its stub). For
  future applies, the copy-exclude is preventive. No data migration.
- **#3:** none — write-side affects only newly-authored rows; read-side is backward-compatible (it
  only *adds* tolerance). Existing well-formed CSVs are unaffected.

## Acceptance checks (append to the Deferred ledger; verify on the next vlt-core upgrade or a fresh install)

- [ ] **#1** — A relayed hand-off (publisher fires `vlt-dispatch relay`) is **picked up by the
  recipient on its next orient** without prompting; the recipient's Beat 2 visibly reads + drains its
  `_agent/dispatch.md` slice; the drain checks the item off (the one sanctioned Beat-2 mutation).
- [ ] **#1** — build-7's `capabilities/` read and the restored dispatch read **coexist** in Beat 2
  (both fire; neither displaced).
- [ ] **#2** — A fresh `vlt-upgrade` own-the-apply (or install) drags **zero** `.decision-log.md`
  into the vault; the vlt-mint relocation stub survives intact.
- [ ] **#3** — vlt-mint mints a partner/op whose description contains a comma → the written
  `module-help.csv` row is **quoted**; `merge-help-csv.py` parses it cleanly.
- [ ] **#3** — `merge-help-csv.py` fed a pre-existing **unquoted-comma** row **does not abort**:
  it reports the row and skips/repairs it, and the build-6 B1 local-mint preserve still runs on the
  rest.

## Out of scope (this build)

- **`vlt-track` upstreaming** — Round 2 candidate #4. A real op-skill design (longitudinal-loop hand:
  design protocol → log progress → review/adjust; caller supplies profile + voice) that threads the
  **build-7 capability-object** strand and the **build-8 personalized-extraction firewall**. Now that
  0.3.0 ships the invariant-based firewall, `vlt-track` fits as a domain op that opts into the
  widening per its mint. **Ideate + build separately** (its own brief), if the owner elects to
  upstream it. Decision deferred per Round 2 steering.

## Build record (2026-06-24 — BUILT, unit-verified)

- **#2 (first, hygiene):** deleted all 10 working-tree `skills/**/.decision-log.md` (`phase: build`
  cruft; git status stayed clean — they were already `**/.decision-log.md`-ignored). Added a
  **copy-exclude** sub-bullet to `vlt-upgrade/SKILL.md` Step 2 own-the-apply: exclude
  `.decision-log.md` from everything copied (`rsync --exclude` / cp filter), with the why (a stray one
  would overwrite the vlt-mint relocation stub).
- **#3 (both sides):** **read-side** — `merge-help-csv.py` `read_csv_rows` now returns
  `(header, well_formed, malformed)` and **skips** mis-split rows instead of `raise`-ing; new
  `describe_malformed()` names each dropped row by its surviving `skill` column; `main` prints a loud
  stderr WARNING per bad row and adds `malformed_rows_skipped` to the result JSON. **Write-side** —
  `vlt-mint/SKILL.md` Step 4 gained an **always-quote** rule for every `module-help.csv` row write
  (free-text columns always double-quoted, drift-proof). Verified: a malformed local-mint row no
  longer aborts the merge (exit 0), is reported by skill, and the good local mint is still preserved;
  the fresh-install (blind) path is unregressed (13/13 rows, 0 malformed). Shipped
  `assets/module-help.csv` audited clean (vlt-core's bad `vlt-lint` row was a local edit, not shipped).
- **#1 (contract + consumers — scope expanded by owner ruling):** grounding revealed the **partner
  SKILLs + partner-template also enumerate Beat 2 and all omitted the dispatch slice** — the build-4
  gap manifesting in the consumers, not just the contract. Owner chose the **full fix (5 files)**:
  contract Beat 2 read-list + a standalone **mutation-license note** ("the one orient read that may
  mutate shared state"), plus the dispatch-slice drain added to all 3 partner SKILLs + the
  partner-template, in each partner's voice (name + point at the contract — matching how each already
  handles `capabilities`). Contract is **not** version-handshaked (build-4 held it out; not a
  convention with a baseline) → no version bump / consumer re-ack needed.
- **vlt-core fold-back:** the contract fix means vlt-core's one intentional governance divergence
  (its local Beat-2 re-graft) folds to zero on its next upgrade.

## Open questions

- **#1 mutation-license placement** — inline in the Beat 2 paragraph, or as a short standalone note
  right after Beat 2 (parallel to the Cold-start / Partner-invoked notes that already follow it)?
  Lean: standalone note, to keep the Beat 2 read-list sentence scannable.
- **#3 read-side: skip vs. repair** — ship skip (safe floor) only, or skip + best-effort re-join
  repair? Lean: skip + report for build-10 (repair is a follow-on if a real row ever needs salvaging
  rather than re-minting).
- **#2 copy-exclude scope** — exclude only `.decision-log.md`, or a broader "dev-cruft glob" (e.g.
  also `.DS_Store`, editor temp files) at the apply seam? Lean: name `.decision-log.md` now; widen
  only if another cruft class actually rides a copy.
