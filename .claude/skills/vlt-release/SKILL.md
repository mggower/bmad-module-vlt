---
name: vlt-release
description: Runs the vlt release as one gated sequence — pre-flight, version bump, changelog, lint gate, commit, ff-merge, tag, push. Use when the user says 'release vlt X.Y.Z' or 'run the release'.
---

# vlt-release

Releases the plugin. Each stage is a gate: the first failure stops the run with a clear report, and nothing later executes. The owner is present throughout; there is no headless mode. The skill asks two things: the version (up front, never inferred) and confirmation before the push.

Run every command from the repo root.

## Stages

1. **Pre-flight.** On a release branch (not `main`), with a clean tree (`git status --porcelain` prints nothing). `uv run --with pytest pytest tests/ -q -p no:cacheprovider` passes. Stop on either failure.
2. **Version bump.** Set `X.Y.Z` in `.claude-plugin/marketplace.json` (`plugins[0].version`) and in the `version:` line of every `kits/*/kit.yaml`. All kits carry the plugin's version.
3. **Changelog.** `CHANGELOG.md` gets a `## vX.Y.Z — <date>` section at the top: what changed, by kit, and for each changed kit file a line a vault owner can act on when `vlt-pull` offers it. Show the entry to the owner before going on.
4. **Lint gate.** `python3 tools/package-lint.py --expect-version X.Y.Z`. It must exit 0. Keep its last line (`PASS: 8 checks`) verbatim. On any `FAIL`, stop; do not fix and continue without the owner's word.
5. **Release commit.** Commit the bump and the changelog entry. The message body carries the lint's PASS line verbatim, so a skipped lint is visible in history.
6. **Ship.** `git checkout main && git merge --ff-only <branch>`; stop if it is not a fast-forward. Then an annotated tag: `git tag -a vX.Y.Z -m "vX.Y.Z"`.
7. **Push.** Ask the owner. On yes: `git push origin main` and `git push origin vX.Y.Z`. Never push `full-history`. The `private` remote is pushed only if the owner says so.
8. **Close the loop.** For each tracker issue this release answers, draft a closing comment naming the version and what changed, show it, and post it on the owner's approval (the field contract's voice rule: `kits/core/files/resources/playbooks/feedback-field-contract.md`). Move the inbox filings the release resolved to `factory/shipped/vX.Y.Z/` with `git mv`, and commit.

## Report

What was released, the PASS line, the tag, what was pushed, which issues were answered, and which filings moved.
