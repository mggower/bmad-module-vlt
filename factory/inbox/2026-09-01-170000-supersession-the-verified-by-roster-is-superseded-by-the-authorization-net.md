# `class: supersession` — the `verified_by` roster is superseded by the authorization net it was standing in for

_Filed 2026-09-01 from **`{field-vault}`**, on the re-derivation of live parked interim **#16**
(`ref: conventions/write-verification.md`). **Cites `ST-2`** — location as proxy for trust,
`status: standing`. **Sibling of `2026-09-01-160000`** (the PARA `type:` enum), which names this
instance and routes it here. Both retirements belong to one ideation and two builds._

⚠ **This is a `supersession` filing** (`factory/inbox/README.md`). It asks for a **retirement**, and
it carries both required halves. It is what park **#16** re-parks against: #16's original question
*was* answered, narrowly and by artifact class, and the substantive half was **refused** rather than
resolved — so the park cannot honestly claim to be pending #16 any longer, and it is not conceding
the rule either. **The vault is holding for retirement.**

---

## Half 1 — the rule now redundant

**Site:** `skills/vlt-setup/assets/governance/_meta/conventions/write-verification.md:47`
(`version: 5`).

> **`verified_by` value set:** the `verified_by` value set is this file's `consumers:` **that are
> write ops**, plus write-op `local_consumers:` registrants … The roster is **membership and
> ceiling**, never an automatic grant.

**What it was standing in for: authorization.** The roster restricts *who may mark a file verified*,
so that the mark cannot be claimed by something with no standing to claim it. When it was written
there was no other way to ask whether a writer was entitled to write where it wrote — so the
attestation field carried the authorization question as a passenger.

**Why it is redundant now.** Layer 3's entry condition is **open** by design — the operating contract
states the two named dispositions *"are the shipped set, **not** a closed one: another verb filing an
honest, attested document under the condition above is legal."* The roster is the one clause that
contradicts that openness: a partner authoring a Layer-3 knowledge artifact during a sanctioned
sitting satisfies **every** leg of the entry condition except attestation, because **no legal value
in the set names it.** Its only options are to write something false or to carry an open finding
forever — and `{field-vault}` has carried the finding, honestly, on **27 files**, since 2026-08-26.

---

## Half 2 — the mechanism that supersedes it

**`para_writer_unauthorized`**, `skills/vlt-lint/references/checks.md:20`, shipped **Cycle 12
build-5**. The check's own opening clause states its purpose in the exact terms this filing needs:

> the **write-posture** net, **the authorization question a location rule could never answer.**

**It enforces the same claim.** For each file in the `para_*` population it walks up to the nearest
declaring ancestor container, reads that container's human-gated `writers:` list, and joins the
file's writer identities against it — admitting on any match. **That is the authorization question,
asked directly, per container, against a list a human ratified.** The roster asks a blunter version
of it (*is the marker on an approved list of ops?*) at a field that `write-verification.md:55` says
is **"a self-marker, not a quality grade."**

**Same population, exactly.** `checks.md:20` runs the net over *"each file in the `para_*` population
above"* — files under `{projects}`, `{areas}`, `{resources}`, `{wiki}` removed at population time —
in **both modes**. That is the identical file set the roster's attestation requirement governs. No
population is left uncovered by the retirement.

## ⚠ The proof the supersession is already shipped, and is currently unreachable

**`para_writer_unauthorized` reads `verified_by:` as a PARTNER SLUG.** Its identity-resolution list,
verbatim from `checks.md:20`:

> `author: human` → `human`, `author: agent` → `agent`, **`author: hybrid` → `human`** … and the
> attestation **`verified_by:` → that partner slug**.

**`write-verification.md:47` makes a partner slug illegal in that field.** So the authorization net
ships with a resolution leg **that no conformant vault can ever exercise**. It was built for a world
in which partners attest their own Layer-3 writes; the roster is what keeps that world from
existing.

**This is not an inference about intent — it is two shipped clauses that cannot both be satisfied.**
The net names a value the convention forbids. One of them has to move, and the net is the one doing
the work the roster was standing in for.

⚠ **And Cycle 14 build-5 named this disease while writing another instance of it.**
`write-verification.md:55` v5 reads *"fusing permission to provenance is the write-path failure this
exemption exists to prevent"* — a correct principle, shipped in the same file, four lines from the
roster that fuses permission to provenance by restricting *who may mark* to a list of *what may
write*.

---

## What the retirement is, precisely

**Retire the roster's closure at `write-verification.md:47`** — the clause that limits `verified_by`
to write ops and write-op registrants.

⚠ **The attestation pair is NOT retired, and this filing does not ask for that.**
`verified_by:`/`verified_at:` stay required on Layer-3 knowledge artifacts; `para_missing_attestation`
keeps its job. What changes is **which values are legal in the field** — a partner that ran tier-1
may name itself, which is what a self-marker means. **Retiring a restriction is not retiring the
field.**

⚠ **Nor does this ask for authorization to be dropped.** It asks for it to be answered **once**, by
the net built to answer it, instead of twice — badly at the attestation field and properly at the
container. Where no ancestor declares `writers:`, `checks.md:20` already rules the posture **`open`
and the file PASSES**; that default is the honest one and this filing does not disturb it.

**The residual question capture must rule rather than assume:** whether an unrostered attester needs
*any* floor (e.g. must name an identity the vault has minted) or whether the container `writers:`
join is the whole of it. The vault's read is the latter — `writers:` is human-gated, so the human
already holds the gate — but that is a ruling, not a fact.

---

## Field evidence

- **27** Layer-3 files outside `{wiki}` carry `author: agent|hybrid` with no attestation pair, across
  six partners' domains. Count re-verified on the 2026-09-01 sweep: *"count unchanged."*
- **Zero** partner-sitting-written Layer-3 documents in this vault are attested, **and under the
  current value set none can be.**
- The tier-1 pass **is being run** — the park records that *"the substance the pair stands for is done
  and reported; only the marker is withheld."* The work happens; the field cannot record it.
- The alternatives were considered and refused at park time, and the module later **ratified the
  refusal**: stamping a rostered op is a false provenance claim (`write-verification.md:55` v5), and
  ruling the files human-authored is false where `author: agent` is correct.

## Grounding against current module source (v0.17.1)

`write-verification.md:47`, `:55` (`version: 5`) · `vlt-lint/references/checks.md:20`
(`para_writer_unauthorized`, its purpose clause and its identity-resolution list) · `:19` (the
`para_*` population, both modes) · `vault-operating-contract.md:66-68` (Layer 3's entry condition and
its explicitly open disposition set), `:70` (the write-posture resolver) ·
`factory/studies/ST-2-location-as-proxy-for-trust.md` (`status: standing`) · upstream filing **#16**
(open) · sibling `factory/inbox/2026-09-01-160000-…`.

_Ship-verifiable at rest: the retirement is gradeable against shipped convention source plus a
fixture exercising `para_writer_unauthorized`'s `verified_by:`-as-partner-slug leg — the leg that
cannot fire today. The field half (a partner attesting its own Layer-3 write, and the net admitting
or refusing it against a declared `writers:`) rides the first sweep after the repair._
