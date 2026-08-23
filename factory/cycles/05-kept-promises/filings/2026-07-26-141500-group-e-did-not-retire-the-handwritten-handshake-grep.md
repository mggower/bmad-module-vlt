# Defect: build-23's gate shipped, but the ritual it was built to retire is still being written by hand

_Filed 2026-07-26 by the closing registrar during the Arc 3 `arc-closeout` run, from factory-side
evidence at v0.8.0 (`557347f`). Build-23's **process-adoption** acceptance clause was exercised twice
by Arc 4 and **FAILED both times**. This filing is the contradiction routed back as field signal per
the discharge rubric. **Defect in the factory's own dev tooling** (`.claude/skills/build-brief/`),
not in shipped module source._

## The clause, and what happened

Build-23 shipped `package-lint` Group E (handshake-bipartite, structure-map SSoT, stray-pin) so that
the handshake check would be owned by a mechanical gate rather than re-written by each builder. Its
acceptance clause states the proof precisely:

> the next arc's first build that touches a convention `version:`, a `consumers:` list, or the
> structure map runs `package-lint` Group E as its handshake verification **instead of** a
> hand-written `grep "<name>@"`, and the brief/commit shows Group E — not the self-confirming grep —
> as the check of record (the process-adoption proof: the self-confirming grep every build 19–22
> wrote by hand **stops being written** because the gate now owns the check).
> (`skills/reports/inbox-evolution-arc3-roadmap.md`, build-23 ledger item)

The trigger fired twice in Arc 4. The grep did not stop being written.

- **A4-3** (`wiki-supersession` `1 → 2`, four consumers re-acked — the first Arc-4 build to move a
  convention `version:`). Verification check **1**, titled *Handshake bipartite*, is
  `grep -rn "wiki-supersession@" skills/` plus a manual `consumers:` cross-read
  (`skills/reports/build-A4-3-contradiction-drain.md:469-471`). Group E appears only at check **9**,
  hedged: *"Groups A/B/C/E PASS (E is the mechanical net for the handshake in check 1)"* (`:494`).
  The grep is the check of record; Group E is described as the net *behind* it — an inversion of the
  clause.
- **A4-5** (new convention `consult@1`, two new acks — a `consumers:` movement). Check **4**,
  *Handshake bipartite (the standing ritual)* — note the builder's own word for it — is a manual
  `consumers:` ↔ `depends_on:` cross-read plus `git diff`; check **5** is
  `grep -rn "consult@" skills/` (`skills/reports/build-A4-5-consult-channel.md:615-620`).

**The gate itself is not at fault.** Group E ran and passed on all five Arc-4 builds
(`A/B/C/E PASS` recorded in every build commit; `A/B/C/E PASS, D PASS` at the release commit
`557347f`), and A4-5's design section correctly names it as the authority — *"Bipartite consistency
is verified at rest by `package-lint` Group E (`tools/package-lint.py:351-382`, which globs the
conventions dir, so the new file is picked up with no tool change)"* (`:571`). The machinery works.
What failed is **adoption of the process**.

## Root cause — the brief scaffold instructs the old ritual and has never heard of Group E

Every Arc-4 builder followed the scaffold correctly. The scaffold is stale:

- `.claude/skills/build-brief/references/brief-anatomy.md:94-95` — the standing per-build ritual is
  stated as *"**Handshake bipartite re-check** — if any convention `version:` moved, verify every
  consumer listed ↔ every ack current (CLAUDE.md version-handshake rule)."* It names **no tool**, so
  each builder invents one, and the obvious invention is a grep.
- `.claude/skills/build-brief/references/brief-anatomy.md:96` — *"**Packaging lint** — the mid-arc
  `package-lint.py` **A/B/C** run"*. Group E did not exist when this line was written; build-23 added
  it and **never updated the scaffold**. The brief template literally does not know Group E exists.

So the clause asked builders to stop doing something their own instructions still told them to do.
This is the same failure shape the arc has now filed three times — a mechanism ships, and the
surface that would cause anyone to use it is left untouched (cf. `adoption_first_instance:` carried
by zero of seven conventions at capture run 3; `revisit_after:` absent from `vlt-ingest`'s write
path). **The enforcement arc's own dev tooling has the enforcement arc's disease.**

## Why this matters more than a stale doc line

The hand-written grep is **self-confirming**: it greps for the token the builder just wrote, in the
files the builder just edited. It cannot detect the failure Group E exists to catch — a convention
whose `consumers:` list names a skill that never acked, or an ack pointing at a convention that
moved. `tools/package-lint.py:351-382` derives both sides from the authoritative surfaces and
compares them, which is why its own docstring says it *"derives truth from the authoritative surface
and compares, rather than confirming a declaration about it — the fix the whole arc pointed at."*

Arc 4 got the right answer five times running, so nothing broke. But it got it from a check that
structurally cannot fail, while the check that can fail sat in a lower slot described as a
formality.

## Suggested shape (owner steers at ideation)

Small, factory-side, no shipped-module surface:

1. ~~`brief-anatomy.md:94-95` — name Group E as **the** handshake check of record, and state that a
   hand-written `grep "<name>@"` is not a substitute (it confirms a declaration; Group E derives).~~
   **✅ FIXED 2026-07-26** (owner-directed, at Arc 3's closeout). The ritual now names Group E as the
   check of record, states "do not compose your own," and explains why a grep is self-confirming.
   Also widened the trigger from *`version:` moved* to *`version:` moved, or `consumers:` or the
   structure map changed* — Group E covers all three (E1/E2/E3) and A4-5's case was a `consumers:`
   movement with no version bump, which the old wording did not name.
2. ~~`brief-anatomy.md:96` — correct `A/B/C` → `A/B/C/E` for the mid-arc run.~~ **✅ FIXED
   2026-07-26.**
3. **STILL OPEN — the only part `inbox-capture` should carry forward.** Should the verification
   template carry a **named slot** for the handshake check rather than leaving builders to compose
   one? The drift here was a builder filling an *unnamed obligation* with the cheapest available
   tool, and items 1–2 fix the naming without addressing the shape. Related open question: whether
   the same unnamed-obligation risk exists for the other standing rituals in §7 (scrub, workflow
   parse-on-intake, fence well-formedness), none of which names a tool either.

> **⚠ PARTIAL RESOLUTION — read before capturing.** Items 1 and 2 were fixed directly at Arc 3's
> closeout (2026-07-26) rather than routed through a build, because they are literal corrections to
> **factory dev tooling** (`.claude/skills/`, gitignored) with no shipped-module surface and no
> design content — the lifecycle's capture→ideate→brief→build path governs module source in
> `skills/`. **Item 3 was deliberately NOT fixed**: it is a design question about the template's
> shape, and pre-empting it with a partial fix is precisely how the `linkage_ripe` polarity inversion
> entered (a brief-time decision nobody ruled on). Capture item 3 only; do not re-brief 1–2.
>
> **The FAILED acceptance grade is unaffected.** Build-23's process-adoption clause was exercised
> twice and failed both times; that verdict stands as history and is recorded in the archived Arc-3
> roadmap. This fix means the *next* handshake-bumping build has correct instructions — it does not
> retroactively discharge the clause, and build-23 still closes on Arc 5's disposition of item 3.

## Honest limits

- Grounded entirely in factory artifacts (briefs, commits, `tools/package-lint.py`,
  `.claude/skills/build-brief/`). No vault evidence involved; this is a dev-process defect.
- Group E's **detection** power is still unexercised on real drift — no qualifying mid-development
  drift arose across builds 19–23 or A4-1…A4-5. That is build-23's separate *non-vacuous catch*
  clause, recorded as vacuous by construction across two versions per the Q28 owner note (2026-07-26),
  and it is **not** what this filing reports.
- The clause's third tail (*F4 in the field* — a maintainer citing `vlt-lint:74`'s
  pin-not-conformance limit correctly) is unrelated and remains an open watch.

## Provenance

- Arc 3 build-23 acceptance clause — `skills/reports/inbox-evolution-arc3-roadmap.md` (build-23
  ledger item), briefed in `skills/reports/build-23-content-verification.md`.
- Failing instances — `skills/reports/build-A4-3-contradiction-drain.md:469-471,494`;
  `skills/reports/build-A4-5-consult-channel.md:615-620` (with `:571` as the counter-evidence that
  the builder knew Group E was authoritative and wrote the grep anyway).
- Root cause — `.claude/skills/build-brief/references/brief-anatomy.md:94-96`.
- Gate implementation — `tools/package-lint.py:351-382` (`check_group_e`, `_e1_handshake`).
