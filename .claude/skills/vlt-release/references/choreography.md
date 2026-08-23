# Release choreography

The vlt release as eight strictly-ordered gates. Run from the factory repo root
(`{project-root}`). Each stage is a hard gate: on the first failure, print what failed and
**stop** — nothing in a later stage runs. Never tag or push anything if any earlier gate
did not pass. `X.Y.Z` is the release version the owner gave on activation; `cycleN-vX.Y.Z`
is this cycle's release branch (e.g. `cycle11-v0.15.0`; branches before the rename were
`arcN-vX.Y.Z`).

This file is self-contained — don't assume SKILL.md is still in context.

---

## Stage 1 — Pre-flight

Gate: the tree is in a releasable state and this cycle's work is actually done.

- **Branch.** `git rev-parse --abbrev-ref HEAD` must be `cycleN-vX.Y.Z`. If the owner says
  this run *starts* the release and you are on a clean `main`, create it:
  `git switch -c cycleN-vX.Y.Z`. Never release from a dirty tree and never from `main`
  directly.
- **Clean tree.** `git status --porcelain` — must be empty at pre-flight (the version bump
  hasn't been made yet; it lands in stage 3). Any unexpected modification stops the run
  for the owner to explain.
- **All briefs BUILT.** The open cycle roadmap (read `factory/CYCLE` for the open cycle's
  `NN-<slug>`; the roadmap is `factory/cycles/<that>/roadmap.md`) lists the builds this
  release ships. For each, read `factory/cycles/<that>/briefs/build-*.md`
  frontmatter `status:` — every one must be BUILT (or a shipped-equivalent state the owner
  confirms). A brief still in an earlier state stops the run.
- **One-commit-per-build (advisory).** `git log main..HEAD --oneline` should map 1:1 onto
  the roadmap's build list (one commit per build). This is advisory — report any mismatch
  and let the owner rule; do not hard-stop on it alone.

## Stage 2 — Handshake bipartite check

Gate: no consumer skill ships a stale acknowledgment of a governance convention. A release
must never ship a stale ack.

```bash
uv run .claude/skills/vlt-release/scripts/handshake-check.py
```

Require **exit 0**. The script asserts, in both directions, that every convention's
`consumers:` pin it at its current `version:` and every `depends_on: ["name@version"]`
names a real convention at its current version whose `consumers:` list the skill. Any
non-zero exit prints the specific mismatch(es) — this is a **hard stop**. (Silence here is
the pass; the first time it ever fires, the gate paid for itself.)

## Stage 3 — Version bump + changelog entry

Gate: both version strings equal `X.Y.Z` and agree with each other, and `CHANGELOG.md`
carries the `X.Y.Z` entry.

Edit both to `X.Y.Z`:

- `.claude-plugin/marketplace.json` → `plugins[0].version`
- `skills/vlt-setup/assets/module.yaml` → `module_version`

Then prepend a `## vX.Y.Z — YYYY-MM-DD` entry to `CHANGELOG.md`, authored per the shape the
file itself carries: the `**Cycle N**` line collected from the release-commit subject about to
be written (entries before the rename carry `**Arc N**`), one bullet per build collected from
each open-cycle brief's `title:` (`factory/cycles/<open cycle>/briefs/build-*.md`) in
this release, and a `Changed paths:` line from `git diff --name-only <prev-tag>` — the tag
against the **working tree**, not `<prev-tag>..HEAD` — under the filter `CHANGELOG.md`
already uses.

**The working tree is the right basis, and `..HEAD` is wrong.** The version bump you just
made is uncommitted at this point, and it touches `.claude-plugin/marketplace.json` and
`skills/vlt-setup/assets/module.yaml` — both of which **pass the filter** (the first by name,
the second as `skills/vlt-setup`). A `..HEAD` diff omits them, so the entry would under-report
its own release's surface. Every retro entry in `CHANGELOG.md` includes
`.claude-plugin/marketplace.json` for exactly this reason: the bump is part of the tagged
diff. (Only `CHANGELOG.md` itself is excluded, by the filter, as repo housekeeping.)

If both version strings already equal `X.Y.Z` and the entry is already present (a prior
attempt landed them), proceed unchanged — do **not** write a second entry; Group D asserts
exactly one and would fail it. If the two version strings **disagree with each other**, stop —
a half-applied bump from a previous run needs the owner's eyes before proceeding.

## Stage 4 — Lint gate

Gate: the packaging lint passes with tag intent asserted.

```bash
uv run tools/package-lint.py --expect-version X.Y.Z
```

Require **exit 0**. Capture the final summary line **verbatim** — it is the text that goes
in the release commit. The script prints it as:

```
package-lint: A/B/C/E PASS, D PASS — vlt X.Y.Z
```

On exit ≠ 0: print the failure output and **stop**. Do not revert the version bump — a
clean bump is fine to leave on the branch for the next attempt. Nothing is committed,
tagged, or pushed.

## Stage 5 — Release commit

Gate: the bump is committed with the verbatim PASS line in the message.

Stage the bump and commit. Message shape follows the 0.6.0 exemplar (`git show a117f4f`;
its title says `Arc N` — releases since the rename say `Cycle N`):
title `vlt X.Y.Z — Cycle N: <cycle name> (builds …)` and the captured lint PASS line as its own
paragraph, annotated with the invocation and exit — e.g. `package-lint: A/B/C/E PASS, D PASS
— vlt X.Y.Z (uv run tools/package-lint.py --expect-version X.Y.Z, exit 0)`.

**No body paragraph naming what ships.** What ships is single-homed in the Stage-3 changelog
entry, and the commit points at it by carrying the same version.

**Commit-message rules (owner's standing git rules — non-negotiable):**

- Simple `-m` flags only, one per paragraph. Never heredocs, never `$(cat <<'EOF' …)`,
  never command substitution.
- Never a `Co-Authored-By:` or any signing/trailer line.

```bash
git add .claude-plugin/marketplace.json skills/vlt-setup/assets/module.yaml CHANGELOG.md
git commit -m "vlt X.Y.Z — Cycle N: <cycle name> (builds …)" \
  -m "package-lint: A/B/C/E PASS, D PASS — vlt X.Y.Z (uv run tools/package-lint.py --expect-version X.Y.Z, exit 0)"
```

## Stage 6 — Ship (ff-merge + tag)

Gate: `main` fast-forwards to the cycle branch cleanly, then the tag lands on the merge
result.

```bash
git switch main
git merge --ff-only cycleN-vX.Y.Z
git tag -a vX.Y.Z -m "<the release commit's subject line, verbatim>"
```

`--ff-only` must succeed as a **true fast-forward**. If it refuses (main has diverged),
**stop and report** — do not create a merge commit, do not force anything. The tag is cut
only after a clean fast-forward.

The tag is **annotated**, not lightweight. This was practised through `v0.6.0` and then
lapsed for four consecutive tags — precisely because it lived in habit rather than in this
file. It lives here now.

## Stage 7 — Push (the one outward-facing move)

Gate: explicit owner confirmation, and the push carries only the shipped public surface.

This is the only outward-facing act and the only second question the skill asks. Before
pushing:

- Show the owner exactly what will go out: `main` and the tag `vX.Y.Z`, to
  `github.com/mggower/bmad-module-vlt`. Confirm the remote with `git remote -v`.
- Remind: this is a **public repo**; the push carries the shipped surface (`skills/`,
  `.claude-plugin/`, `tools/`, `.github/`, README, LICENSE) plus the tracked factory record
  (`factory/`, `.claude/`) — machine/personal specifics stay in gitignored files
  (`CLAUDE.local.md`, `_bmad/`, `.claude/settings.local.json`).
- **Never push `full-history`.** The full dev history is local-only. Push explicit
  refspecs only; never `--all`, never `--mirror`, never the `full-history` branch. If the
  current `main` unexpectedly carries the full dev history (sanity-check its length and
  shape against the known clean public history), **refuse and report** rather than push.

Push **only on explicit confirmation**:

```bash
git push origin main
git push origin vX.Y.Z
```

## Stage 8 — Post-stamp

Gate: the record reflects the shipped release and points at what's next.

- Update the open cycle roadmap's frontmatter `status` (via `factory/CYCLE` →
  `factory/cycles/<that>/roadmap.md`) to the SHIPPED form. Exemplar to match:
  `factory/cycles/03-enforcement/roadmap.md` (its `status:` records
  `vX.Y.Z SHIPPED <date> (builds …), @ <sha>, tagged vX.Y.Z`).
- Remind the owner to sync project memory (the cycle roadmap memory topic) with the shipped
  state — builds/release landed.
- End the report with the **Next lifecycle move** (routing contract —
  `.claude/skills/vlt-lifecycle.md`): live acceptance is batched to the next `vlt-upgrade`
  run on a live vault, **an owner action** — name it as the move. Once that upgrade
  evidence exists, `acceptance-discharge` discharges the cycle's deferred ledger. This
  skill's job ends at the push + stamp.
