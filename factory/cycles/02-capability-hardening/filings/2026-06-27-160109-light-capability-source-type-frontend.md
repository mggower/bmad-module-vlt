# Light capability, first instantiation — and the "source-type front-end" pattern

_Filed from the `vlt-core` vault after minting the Librarian's `ingest-youtube` capability (2026-06-27). This is **not** a convention/skill edit — it is the **first real use of the light-capability path** the module already ships, plus the doc-drift and pattern-capture that surfaced. The vault-grown capability content stays local; what's filed here is what the **module** should change or absorb._

## Problem statement + evidence

The user wanted to point the vault at a YouTube URL and ingest video insights the same way articles are ingested. A validated 3-stage pipeline already existed (yt-dlp fetch → ~10-line VTT cleanup → structure + `vlt-ingest`). The mint question was purely *shape*: a new skill, an edit to `vlt-ingest`, or something lighter.

It resolved to **`add a capability` → light** (own-zone, council-none), owned by the Librarian — the **vault's first light capability** and the first use of any partner's `capabilities/` folder. That makes this a useful stress-test of whether the shipped light-capability model actually holds up in practice. It does — but three things are worth shipping back.

## Finding 1 — `mint-verb-not-subject` guidance is stale against the light/heavy model (DOC FIX)

The standing principle "same verb on a new subject = parameterize via a **per-partner profile + a gated registry row**" predates the light/heavy capability model. The light-capability model **supersedes the "registry row" half**: a light capability **registers nothing** in `module-help.csv` — the **capability file *is* the per-source-type profile**, surfaced contextually on the owning partner's activation (Beat 2).

This is a live trap for the next person who reaches for "verb not subject": they'll look for a registry row that shouldn't exist. **Ship:** reconcile the `mint-verb-not-subject` framing wherever it appears in module docs (the mint skill's narrative and any persona/contract reference) so it reads: *new source type on an existing verb → a **light capability profile** in the owning partner's zone (no registry row); only the **heavy** weight registers a CSV row.*

## Finding 2 — the `sources/` deposit vs "own-zone only" needs an explicit ruling (CONTRACT/TEMPLATE CLARIFICATION)

The light-capability contract says light caps "write only the partner's own zone … **never a shared lane**." This capability's only persistent write is depositing a **new file into `sources/transcripts/`** — Layer-1 raw input. Strictly, `sources/` is neither the partner's `_agent/partners/<p>/` zone nor a synthesized lane.

The ruling I made (and documented in the capability body + decision log): **depositing a new raw-input file is lane-safe and stays own-zone-compatible**, because `sources/` is the immutable input tray the *user* already writes freely — it has **no single-writer owner to contend with**, and the cap never *modifies* an existing source. The protected "shared lanes" are the **synthesized** layers (the wiki), where `vlt-ingest` remains sole writer.

The module should make this explicit rather than leaving each minter to re-derive it. **Ship:** one line in `capability-template.md` (and the contract's *Capabilities* section) clarifying that **"never a shared lane" means never a *synthesized/single-writer* lane (the wiki); appending a new raw-input file to `sources/` is permitted** and does not promote a light cap to heavy. Without this, `vlt-lint`'s capability guard (write_scope vs actual writes) and future minters will keep hitting the same ambiguity.

## Finding 3 — capture the "source-type front-end" as a named pattern (PATTERN ABSORPTION)

This mint produced a clean, reusable shape worth naming in the module so it's reached-for, not re-invented:

> **Source-type front-end (light).** To teach an existing ingest/verb a new *input form*, mint a light capability owned by the verb's partner: an own-zone **profile** file (`capabilities/<slug>.md`) that **fetches + normalizes** the new form into the text the verb already eats, plus a **`scripts/` sibling** for any reusable tool the profile invokes. The front-end writes only scratch + a raw-input deposit; the canonical write stays with the unchanged verb skill. Council-none, upgrade-safe, no skill proliferation.

This also establishes the **folder shape** for light caps that carry tooling: `capabilities/<slug>.md` + `capabilities/scripts/<tool>`. The `capability-template.md` currently shows only the bare `.md`; a one-line note that a light cap **may carry an `assets/`/`scripts/` sibling for tools it invokes** would seed the next one correctly.

## Exact module-side changes to ship

1. **`mint-verb-not-subject` reconciliation** (Finding 1) — wherever the verb-not-subject principle is stated in module artifacts, replace "per-partner profile + gated registry row" with the light-capability realization (profile file, no CSV row for light; CSV only for heavy).
2. **`capability-template.md`** (Findings 2 + 3) — (a) clarify "shared lane" = synthesized/single-writer lane; raw-input `sources/` deposit is allowed for a light cap; (b) note that a light cap may carry a `scripts/`/`assets/` sibling for tools it invokes.
3. **Contract *Capabilities* section** (Finding 2) — mirror the "shared lane" clarification so the contract and template agree (single-home).
4. *(Optional)* **`vlt-ingest` / mint narrative** — reference the "source-type front-end" pattern as the canonical way to extend ingest to a new input form.

## Upgrade/migration path for existing installs

All four are **doc/clarification changes** to shipped conventions/skills — **no migration, no data touch, no version-handshake** (they don't change a rule consumers must follow; they remove ambiguity and stale guidance). An install that pulls the upgrade simply gets clearer light-capability guidance. Vault-grown light capabilities already live in the agent zone and survive upgrades by construction, so nothing local is at risk.

## Latent issue surfaced

`vlt-lint`'s capability guard checks "declared `write_scope` matches what the body actually writes." With the `sources/`-deposit ruling unwritten, a correct light cap that deposits to `sources/` could read as a write_scope violation. Finding 2's clarification is also what keeps that lint check honest — worth confirming the guard's logic treats a raw-input deposit as own-zone-compatible (not a synthesized-lane write) when this ships.

## Open design questions (module-wide)

- Should `sources/` deposits by a light cap be **declared** (e.g. a `deposits: sources/transcripts/` field) rather than left implicit, so the lint guard can verify them mechanically instead of by prose ruling? Leaning no (YAGNI — one cap so far), but flag it if a second source-type front-end lands.
- Is "source-type front-end" worth promoting to a first-class **family** once a second one exists (e.g. a podcast-RSS or a Twitter-thread front-end)? Premature now; the shared invariant ("fetch+normalize into the verb's input, write only scratch + raw-input deposit") is a candidate family contract when instances accumulate.

---
_Vault-side record: `_agent/mint/decision-log.md` (2026-06-27 entry); capability at `_agent/partners/librarian/capabilities/ingest-youtube.md`._
