# Give a shipped write op a route to the decision log — the writer roster admits no discovery site

origin: mggower/bmad-module-vlt#6

- **filed:** 2026-08-21 (GitHub issue opened 15:02:14Z via the vlt-feedback rail)
- **origin vault:** app-vault · **module_version:** 0.12.0 · **rail_contract:** 1 · **kind:** candidate
- **materialized:** 2026-08-22 by the factory intake (github-intake)

---

### what_happened

`decision-log.md`'s Writers roster is a closed list of three ceremonies, and it has no route for a
shipped write op that legitimately discovers a governance deviation mid-run.

The roster:

> **Writers** — every one appends in the schema above and points here for the shape (single-home):
> - `vlt-mint`'s ceremonies — gated mints, stage promotions, the self-grow one-liner.
> - `vlt-upgrade`'s write-through — upgrade-time rulings.
> - `vlt-lint`'s write-through — lint-time rulings on governance findings.

with `consumers: [vlt-mint, vlt-upgrade, vlt-lint]` in frontmatter to match.

An **ingest** is a natural discovery site for a governance deviation: it is the op that actually tries
to write a page under the conventions and therefore the op that hits a rule which cannot be satisfied.
When that happens mid-ingest and the user rules on it in-session, the ruling exists and has to go
somewhere. `vlt-ingest` is not on the roster — and, checked against the shipped tree, `vlt-ingest`
never references the decision log at all. So there is no shipped route: not a write path, and not a
hand-off to one.

The convention is also silent on what a **non-writer** op should do on discovering a deviation. That
silence is the gap. Filing this as `candidate` rather than `defect` deliberately: nothing shipped is
self-contradictory, and "only ceremonies write, everyone else hands off" is a perfectly defensible
design — it just isn't stated, and no hand-off mechanism is named.

### evidence

Shipped state:

- `_meta/conventions/decision-log.md` — Writers section names three ops; `consumers:` names the same
  three.
- `skills/vlt-ingest/` — no reference to the decision log anywhere in the shipped skill.
- No text in the convention describing what an op outside the roster does with a ruling it surfaces.

Observed in practice: two entries in a real vault's decision log were appended during ingest runs,
both recording user-direct rulings taken in-session when the ingest surfaced a convention that could
not be satisfied as written. The vault noted the roster mismatch inline in the second entry rather
than pretending conformance. The entries themselves are well-formed and correctly keyed — the writes
look right; it is the roster that does not admit them.

### provenance_guess

**A guess — please ground it.** Two resolutions, and the choice is a design call:

1. **Widen the roster** — admit `vlt-ingest` (and any shipped write op) as a writer, updating the
   Writers section and `consumers:`, with a `version:` bump and the consumer walk.
2. **State the hand-off** — keep the roster closed and say explicitly that a non-writer op which
   surfaces a deviation routes the ruling to a ceremony, naming the mechanism. This needs an actual
   named route, or it recreates the gap in prose form.

v0.12.0's `local_consumers:` work suggests a possible third shape: the same registration pattern
applied to the writer roster, so an op earns write authority by a checked registration rather than by
being hardcoded. Noting it as an option, not a recommendation — the roster is described as "the
handshake protects" it, so widening it may be load-bearing in ways not visible from the field.

Related, same file: the `kind:` vocabulary gap filed separately. Same shape — a closed enumeration
with no value for a legitimate real case — different field and different consumer. They would likely
be fixed in one build.

### kind

candidate

### origin_vault

app-vault

### acceptance_vault

Any vault where an ingest hits a convention that cannot be satisfied as written. Expected after fix:
the ruling has one stated home, reachable from the op that discovered it.

### module_version

0.12.0

### rail_contract

1
