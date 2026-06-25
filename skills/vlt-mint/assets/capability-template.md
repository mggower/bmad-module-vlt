# Capability scaffold

A **Capability** is the first-class object for anything a partner can do. It has **two weights**, and the owner declares only **one** thing — `write_scope` — from which weight, home, and council-class all *derive*:

- **`write_scope: own-zone` → light.** A partner-owned markdown file at `{partners}/{name}/capabilities/{slug}.md` — frontmatter is the object, body is the partner's application. Writes only the partner's own zone. Council-none. May be **self-grown live** (no full mint ceremony). This is the featherweight default — the "missing middle" between a `## Self` note and a registered op skill.
- **`write_scope: <a shared lane>` (e.g. `wiki`) → heavy.** Backed by a **registered operation skill** (the existing `operation-skill-template`); the capability file is just a `procedure: { skill: vlt-{op} }` pointer. Must be owned by that lane's rightful partner. May be council-gated.

**Ownership = location.** A light capability belongs to exactly one partner and lives in that partner's zone — no cross-partner writes (single-writer discipline holds by construction). The `slug` is an **addressing handle** (referenceable, migratable, headless-callable), not primarily a typed command — a partner surfaces its capabilities **contextually** (data, not a fixed menu).

---

## Light capability file — `{partners}/{name}/capabilities/{slug}.md`

```markdown
---
slug: {slug}                       # addressing handle, unique within the owner (e.g. track)
name: {Human Name}
description: {one-line — what shows when the partner surfaces it}
owner: {name}                      # the owning partner (= file location for light caps)
write_scope: own-zone              # THE one declared field — own-zone (light) | a named shared lane (heavy)
weight: light                      # DERIVED from write_scope (own-zone → light); never hand-set
council_class: none                # DERIVED (light + additive → none); never hand-set
provenance: vault-grown            # shipped | vault-grown (usually implied by location)
family: { name: {family}, inherits: [{invariant-ids}] }   # OPTIONAL — present only if opted into a family
---

## Application
{The partner's specific procedure — how THIS partner applies the idea. Outcome-driven.
 A light capability reads/transforms/emits and writes ONLY the owner's own zone
 (its thread.md, its in-flight deliverables) — never a shared lane.}
```

**Heavy capability file** (pointer form — the op skill carries the body):

```markdown
---
slug: {slug}
name: {Human Name}
description: {one-line}
owner: {name}
write_scope: {lane}                # e.g. wiki — a shared lane → heavy
weight: heavy
council_class: gated               # heavy/lane-writing → gated (unless owned by the lane's rightful owner & additive)
procedure: { skill: vlt-{op} }     # XOR with a body — the registered op skill is the body
provenance: shipped
---
```

(An operation skill **is** a heavy capability with a `skill:` procedure — the same object, just the heavy weight.)

**Loop profile** (only for a *longitudinal-loop* op, e.g. `vlt-track`). A shared loop op is **persona-neutral and profile-driven** — *one verb, many subjects*. The wearing partner declares its parameterization here, in the body of its heavy pointer; the op reads it on activation and hardcodes none of it. Add this section under the heavy pointer's frontmatter:

```markdown
## Loop profile
- root: _agent/<area>/<subject?>/      # agent-zone working root — the running log(s) live here
- target: <PARA area>/<subject?>/      # where the polished protocol lands (the extraction target)
- subject-model: single | multi        # multi → scoped under a slug, e.g. {dog}; single → one subject, no nesting
- data-streams: <file(s) the log beat appends to, and what each holds>
- log-tag: <this partner's slug for the {log} line, e.g. dog-trainer>
- non-negotiable-gate: <this partner's named method gate — re-asserted at the write, e.g. least-intrusive / never past the evidence>
```

"Wear `vlt-track`" = add a `capabilities/track.md` heavy pointer (`procedure: { skill: vlt-track }`) carrying a filled Loop-profile block — **not** mint a duplicate loop op. The partner's gated mint must also have opted into the `extraction.md` personalized-extraction widening (the op writes PARA via personalized extraction). See `skills/vlt-track/SKILL.md`.

---

## Family contract — `_agent/capabilities/families/{family}.md`

A **family** (Model B) is the only cross-partner capability object: a thin contract of **invariants** every instance must obey, with each partner's **body fully its own**. Opt-in — a one-off needs no family. Changing an invariant is **gated** (cross-partner blast radius) and fires the propagation check; changing a body touches nobody else.

```markdown
---
family: {family}
description: {one-line — the shared shape, e.g. "a partner keeps a live read on something it owns, over time"}
instances: [{partner}, ...]        # derived/maintained — who has an instance
---

## Invariants  (every {family} instance MUST honor these)
- {invariant-id} — {rule, e.g. append-only — never overwrites prior observations}
- own-zone-only — writes only the owner's own zone, never a shared lane
- {invariant-id} — {e.g. dated-observation — every run emits a dated observation entry}
```

The invariants are **also where the lane-safety rule lives**, so the contract earns its keep. `vlt-lint`'s capability guard checks every instance honors its family's invariants and that each capability's declared `write_scope` matches what its body actually writes.
