---
name: vlt-release
description: Runs the vlt release choreography as one gated sequence — pre-flight, handshake, dual version bump, lint gate, commit, ff-merge, tag, push. Use when the user says 'release vlt X.Y.Z' or 'run the release'.
---

# vlt-release

## Overview

This skill runs the module's Release step as one gated sequence that either completes or
stops cleanly — nothing committed downstream, nothing tagged, nothing pushed, on any
failure. Act as the module's release conductor. Release is a seven-move ritual otherwise
held together by prose (branch → version bump + changelog entry → pre-tag lint → PASS line
in the commit → ff-merge → annotated tag → push); only the lint was ever mechanized, and every pre-lint
tag shipped a packaging defect that cost a full lifecycle round-trip. Here the whole
sequence is one thing: each stage is a hard gate, and a failure halts the run with a clear
report while nothing later executes.

This is an owner-present act by definition — there is no `--headless` mode. The skill asks
exactly two things: the release version (up front) and final push confirmation (before the
one outward-facing move). Everything else runs.

**Lifecycle position:** step 7 (Release) of the loop mapped in
`.claude/skills/vlt-lifecycle.md` — see it for the full flow and the routing contract.
Every report this skill emits ends with a **Next lifecycle move** line (stage 8 carries it).
The same line is **restamped into the open cycle roadmap's foot** in the run that moves the
position — the chat report alone does not discharge it *(the map's standing rule; platform
P-13)*.

## Conventions

- Bare paths (e.g. `references/choreography.md`) resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory.
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{skill-name}` resolves to the skill directory's basename.

Skill-internal script and reference paths below are written from `{project-root}` (the
factory repo root) because the choreography runs shell commands from there —
`.claude/skills/vlt-release/...`.

## On Activation

Load available config from `{project-root}/_bmad/config.toml` and `config.user.toml` if
present; this skill needs nothing beyond `user_name`/`communication_language` if set.

Establish the release version `X.Y.Z` before anything else — ask the owner if they didn't
give it in the invocation. Deciding the version number is always owner input, never
inferred. Then route to `references/choreography.md` and run its stages **strictly in
order**. Each stage is a gate; the first failure stops the run with a clear report and
NOTHING later executes. Do not batch stages, do not run ahead, do not "fix and continue"
past a gate without the owner ruling on it.

## Stages

| # | Stage | Gate |
|---|-------|------|
| 1 | Pre-flight | On the cycle branch, clean tree, every cycle brief BUILT, commits map 1:1 (advisory) |
| 2 | Handshake | `handshake-check.py` exits 0 — no stale acks |
| 3 | Version bump + changelog | Both version strings set to X.Y.Z and CHANGELOG.md carries the vX.Y.Z entry |
| 4 | Lint gate | `package-lint.py --expect-version X.Y.Z` exits 0; capture the PASS line |
| 5 | Release commit | Bump committed with the verbatim PASS line in the message |
| 6 | Ship | True ff-merge to `main`, **annotated** tag `vX.Y.Z` |
| 7 | Push | Owner-confirmed push of `main` + tag; never `full-history` |
| 8 | Post-stamp | Roadmap SHIPPED stamp; memory-sync reminder; point at acceptance |

The full procedure — exact commands, exact gate conditions, exact commit-message shape —
is in `references/choreography.md`. It is self-contained; run it from there.
