# factory/method — how the evolution loop works

Process documentation for the factory itself. The loop's authoritative homes, in reading
order for a newcomer:

1. **`CLAUDE.md`** (repo root) — the eight-step evolution lifecycle and the standing
   rules, stated once.
2. **`.claude/skills/vlt-lifecycle.md`** — the lifecycle map: which skill owns each
   step, observable repo state → position → next move, and every blocked route out.
   `lifecycle-status` walks it read-only.
3. **`factory/CYCLE`** + **`factory/cycles/`** — the record itself: the pointer to the
   open cycle, and one directory per cycle (roadmap, briefs, filings). A closed cycle's
   directory simply stops changing.
4. **`factory/platform/roadmap.md`** — the off-cadence channel for factory-side tooling
   work (anything `vlt-upgrade` doesn't deliver to vaults).
5. **`skills/vlt-feedback/references/field-contract.md`** — the feedback rail's
   contract: how a live vault's defect becomes a labeled issue, a filing, and a build.

Documents living here:

- `cycles-were-arcs.md` — the forward-only rename record: cycles 1–10 were called arcs.
- `vault-resident-architecture-spec.md` — the vault-resident architecture (what lives
  in a vault vs. the module), from the module's design era.

This index is a subset-with-pointers, deliberately — read the directory for anything
newer than this list.
