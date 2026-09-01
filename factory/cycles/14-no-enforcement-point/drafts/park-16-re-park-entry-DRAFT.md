# DRAFT — park #16's superseding entry: a RE-PARK, held for retirement

**Owner-ruled 2026-09-01: re-park, not a deviation** — *"we are holding for retirement."*
*(Supersedes the earlier `deviation` draft, deleted. That draft was written when the vault's position
was that the ruling stood; it no longer is.)*

**Where this goes:** `{field-vault}`'s `_agent/mint/decision-log.md`, appended through
`vlt-lint`'s **write-through** during a full sweep (`fix-and-file.md:20` — the ruling must be made on
a governance finding *during* the sweep). Never a hand edit.

⚠ **A full sweep is required, and it is cheap now.** Scoped mode scopes by file mtime and those 27
files have not changed, so they would fall outside the scoped set and the finding would not surface.
The sidecar is warm and no release has intervened, so expect ~1 rescan plus the index and cluster
passes — roughly **27–31 dispatches against the 172 a cold sweep costs.** ⚠ Take it **before** any
release: a release moves `module_version` and the cache goes cold.

## The two halves — both required

`decision-log.md`, *Supersession idiom*: the superseding entry carries `supersedes:`, **and** the
superseded entry is marked **in place**. Append-only — the old entry is annotated, never rewritten.

### Half 1 — mark the existing park in place

On `## [2026-08-26] parked-interim — partner-sitting writes to Layer 3 left unattested…`
(`decision-log.md:1255`), add:

```
- superseded_by: [2026-09-01] parked-interim — partner-sitting Layer 3 writes, held for the retirement of the verified_by roster
- superseded_date: 2026-09-01
- superseded_reason: the upstream ruling this park waited on (#16) landed and answered only the artifact-class half, explicitly refusing the partner-sitting reading the park rests on; the park is neither pending #16 any longer nor conceding it, so it re-parks against the retirement filing that supersedes the rule
```

### Half 2 — the new entry

```markdown
## [2026-09-01] parked-interim — partner-sitting Layer 3 writes, held for the retirement of the `verified_by` roster
- kind: parked-interim
- ref: conventions/write-verification.md
- supersedes: [2026-08-26] parked-interim — partner-sitting writes to Layer 3 left unattested, held pending the `verified_by` roster ruling
- verdict: parked (user-ruled — panel not fielded: <WHY — see note>) — the ruling landed on one half and refused the other; the vault holds for retirement rather than falsifying a field or conceding a rule it has filed against
```

⚠ **On the `<WHY>`.** Your reasoning — *"we are holding for retirement"* — is the **park's substance**
and belongs in the body below, where it is the load-bearing sentence. The provenance `why` answers a
narrower question: **why the panel was not fielded.** `decision-log.md:56` requires it and will not
accept a blank. Both existing parks use this form, and it applies unchanged:

> *a park changes no boundary and edits no rule — it records a hold. There is no governed change for
> a panel to rule on; the user accepted the parking offer in-session, which is this kind's ordinary
> gate.*

**Write it in your own words at write time; do not paste that sentence.**

Body:

> **What changed, and why this is a new park rather than the old one continuing.** Upstream filing
> #16 asked the module to reconcile Layer 3's open entry condition with `write-verification.md`'s
> closed `verified_by` roster, and named two candidate directions: widen the value set, or narrow the
> jurisdiction. The module chose **narrow**, and narrowed **by artifact class only** — v5 exempts the
> Layer-3 operational-record class (`charter | record | register`) and **explicitly refuses** the
> partner-sitting reading: *"a partner sitting is not a jurisdiction … A Layer-3 knowledge artifact
> written in a sitting is in jurisdiction like any other."* The question this park waited on has been
> answered on one half and **refused** on the other. A park pending a ruling cannot survive the
> ruling; this entry records that, and records that the vault is **not** conceding the refused half.
>
> **What the vault is holding, and what it is holding FOR.** The affected files remain **unattested**
> and in jurisdiction. They are **not** backfilled, stamped, or re-authored, and the hold is not an
> exception being carried indefinitely — **it is held for the retirement of the roster clause**, filed
> upstream as a supersession on the grounds that the authorization question the roster was standing in
> for is now answered by `para_writer_unauthorized` over the same population. The tier-1 checklist is
> still being run: the substance the pair stands for is done and reported; only the marker is
> withheld, because no legal value names the writer.
>
> **Why not the alternatives.** Stamping any rostered op remains a false provenance claim — and the
> module has now written that judgment into the convention itself (`write-verification.md:55` v5:
> *"fusing permission to provenance is the write-path failure this exemption exists to prevent"*).
> Ruling the files human-authored is false where `author: agent` is correct. Recording the set as a
> permanent scoped exception (`kind: deviation`) was considered and **declined**: it would concede a
> rule the vault has filed to retire, and it would take the finding off `vlt-upgrade`'s park-review
> surface at exactly the moment the vault wants it visible.
>
> **Measured at re-park time.** ⚠ RE-MEASURE BEFORE WRITING. As of the 2026-09-01 sweep: **27** files
> in jurisdiction, *"count unchanged"*; 29 unattested `author: agent|hybrid` Layer-3 files outside
> `{wiki}`, of which 2 are exempt under the v5 class carve-out.
>
> **The growth rate, recorded so it stays a decision.** The set grows whenever a partner writes a
> Layer-3 document outside a shipped write op — ordinary sanctioned work for every partner on the
> roster. The hold does not stop that.
>
> **Filing reference.** The retirement filing
> (`2026-09-01-170000-supersession-the-verified-by-roster-is-superseded-by-the-authorization-net`),
> sibling to the PARA `type:` retirement (`2026-09-01-160000`); both route to the same ideation.
> Upstream #16 stays open as the original question's record. ⚠ **Post the retirement filing through
> `vlt-feedback` so this park references a live tracker issue**, as #15 and #16 do.
>
> **Standing instruction.** When the retirement lands, **re-derive the unwind against the rules in
> force at unwind time.** Do not replay any sequence implied by this entry, and in particular do not
> assume the unwind is a backfill sweep — whether the 27 files are stamped by their writers, left as a
> pre-retirement tier, or handled another way is exactly what the retirement decides.
