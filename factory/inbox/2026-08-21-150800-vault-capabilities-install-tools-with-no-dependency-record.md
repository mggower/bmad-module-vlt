# Vault capabilities install machine-level tools with no dependency record — a vault ports, its toolchain doesn't

origin: (factory-observed; no issue — filed directly by the owner)

- **filed:** 2026-08-21 by the owner (via the factory clerk, owner-confirmed in-session),
  classification: **pattern candidate** for a future build (Arc 10+)
- **provenance:** the app-vault agent's post-run flag ("the transport failure path is
  untested — gh pre-flight was clean both times") led the owner to the general
  observation: several vlt-core capabilities have installed tools onto the machine
  (e.g. via uv/brew during capability exercise), and none of that is recorded anywhere
  durable — moving to a new computer ports the vault but silently strands its toolchain.

## The gap

A vault is designed to be durable and portable (git-carried, upgrade-safe, agent-zone
preserved) — but capability and mint ceremonies that install or assume machine-level tools
(`gh`, `uv`, parsers, converters) leave no manifest. The failure mode is deferred and
silent: everything works on the machine where the capability was minted; on a fresh
machine, capabilities fail at exercise time with no declared expectation to check against.
`vlt-feedback`'s named `gh-missing` error is the one shipped instance of a dependency
being checked-and-reported — done ad hoc, per-skill.

## Design material for capture (not resolved here)

- **Declare at birth** — the retention-at-birth pattern applied to tooling: a mint or
  capability ceremony that installs/assumes a tool records it at creation (capability
  frontmatter, or a vault-level dependency file in the agent zone). Retroactive census of
  existing capabilities would be a one-time migration.
- **Check at arrival** — `vlt-setup`/`vlt-upgrade` on a new machine reads the manifest and
  reports missing tools (report, not gate — the vault must stay usable degraded), the same
  named-error discipline `vlt-feedback` ships for `gh`.
- **Two layers to keep distinct:** module-level dependencies (what shipped skills assume —
  `gh`, `uv`; arguably module.yaml's to declare) vs vault-grown dependencies (what local
  capabilities added; agent-zone, durable, vault-writable). The durable-host doctrine
  covers the second: it needs a declared home, not prose.
- Related: A9-4's multi-machine theme (Arc 9) — vaults now provably move across machines
  faster than their toolchains.
