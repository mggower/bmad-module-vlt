# The feedback loop is single-machine — adopt GitHub issues as the module's remote filing rail

- **filed:** 2026-08-19
- **vault:** factory-owner session (signal originates from the work-machine vaults; see origin note)
- **kind:** design-stage-proposal (owner-requested, this session) — evidence debts declared below
- **surface:** the ingress side of the evolution loop — `inbox/` as front door, vlt-core's
  minted `vlt-file-feedback` skill, and the absence of any shipped filing rail
- **found by:** an app-vault agent routing around the gap — it filed
  mggower/bmad-module-vlt#1 directly, with no shipped support
- **full analysis:** `_output/problem-solution-2026-08-19.md` (this repo, gitignored) — the
  problem-solving session this filing condenses; owner rulings recorded there are binding inputs
  to capture, not guesses

## What happened

The module's only feedback ingress is a filesystem write into `inbox/` — reachable solely from
vlt-core, the one vault co-resident with this repo. The work vault and the shared team vault
(app-vault) have no rail; their path today is the owner-mediated relay branch in vlt-core's
`vlt-file-feedback` §4. On 2026-08-19 an app-vault agent bypassed the gap and filed a GitHub
issue (#1) that is capture-grade in everything but location and contract: no shape governance,
no sensitivity gate, no lifecycle linkage.

That skill's own out-of-scope ruling anticipated this: *"a future multi-machine story is a
factory design problem (a remote inbox), not a vault operation."* This filing is the factory
picking that question up.

## Diagnosis (condensed)

The inbox contract conflates two roles that going public/multi-machine pulled apart:
**capture substrate** (must stay local, private, gitignored — correctly so) and **ingress
endpoint** (must be reachable). Note that `inbox/` being gitignored means there is *no*
git-native remote route into it — issues sit beside the repo, which is exactly right: public
signal, private processing.

## Proposal (owner-ruled shape, this session)

Separate ingress from substrate. Issues are transport; **inbox stays SSoT**; capture is the
airlock. Three parts, each a natural build seam:

1. **Repo-side contract** — `.github/ISSUE_TEMPLATE/` forms (defect; pattern/candidate)
   encoding a **lean public shape**: what happened, generalized evidence (placeholder paths,
   no vault-local literals), provenance guess marked as a guess, classification, **origin
   vault** stated, where acceptance should run. Labels `field:defect|pattern|candidate` +
   `vault-filed`. Templates point at the shape's SSoT, never restate it.
2. **Shipped skill `vlt-feedback`** (owner-ruled name — not `vlt-file-feedback`) — ports the
   judgment core of the vlt-core mint (module-source routing test with hand-off-when-unsure,
   never auto-file, honest classification, duplicate guard via `gh issue list`) and adds a
   **scrub gate** checklist before posting (no vault paths, no personal-domain content, no
   third-party names; two-tier escape hatch: vault-side companion detail note, referenced not
   pasted). Transport `gh issue create` against a feedback-repo URL declared once in
   `module.yaml`. Degrades loudly when `gh` is absent/unauthed: emit paste-ready filing text,
   never silently drop, never fall back to filesystem paths.
3. **Factory intake + close-out** — capture materializes open `vault-filed` issues into
   `inbox/` files stamped `origin: <repo>#<n>`, then proceeds unchanged; archival closes the
   issue with a release pointer when the filing archives. Lifecycle is touched at exactly
   these two seams; everything keyed off inbox files is untouched.

**vlt-core posture (owner-ruled):** one rail — vlt-core files via `vlt-feedback` like every
other vault; the local mint is retired by explicit owner act post-ship (distinct name → no
upgrade collision; durability posture untouched).

**Capture note:** issue #1 should be materialized by hand at Arc 9 capture as the intake
prototype — it is real uncaptured signal (enforcement-kit tripwire-metrics durability) *and*
the pattern's first exercise.

## Evidence debts (declared up front, per the design-stage-proposal precedent)

- **Shared-vault attribution:** GitHub author ≠ origin vault; the template's origin-vault
  field is the answer on paper, unproven in practice.
- **Scrub-gate efficacy:** untested against real personal-domain signal; issue #1 is one
  favorable data point (machinery-only content scrubbed naturally).
- **`gh` auth variance on the work machines:** assumed available/authenticated; not verified
  by any module machinery.
- **Community/noise traffic:** a public tracker admits non-vault filers; label partitioning is
  a design, not evidence.

## Provenance guess (marked as a guess)

The gap is a design omission at the factory level (ingress never separated from substrate when
the module went public), not a defect in any shipped build — no build ever claimed a remote
rail. The nearest shipped artifact is the *ruling* in vlt-core's mint that assigned the
question to the factory, which had no factory-side carrier.
