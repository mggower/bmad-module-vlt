# Evidence Rubric

Discovery has handed you: the open cycle roadmap, its list of unchecked `- [ ]` ledger items,
and the evidence sources that carry this cycle's acceptance (upgrade-ledger entries, relayed
evidence filings in `factory/inbox/`, post-upgrade vault activity — across every vault
Discovery enumerated). Now grade each item.

**The vault is read-only without exception.** You read whatever a ledger item names to gather
evidence; you write nothing into the vault. If evidence reveals a defect, that is module
signal — it files into `factory/inbox/` (see FAILED below), it is never fixed, cleaned, or
annotated in place.

## Stage 2 — Evidence & Verdict (per item)

Each ledger item names its own observable evidence — an upgrade-ledger key
(`migrations_run:`, `header_migrated:`, `skill_manifest_missing`, …), a file that must exist,
a lint result, a behavior that happens at next-use. **Read only what the item names.** Don't
go spelunking the vault beyond the item's stated evidence; don't re-derive the whole upgrade.

Grade each item as exactly one of:

### DISCHARGED — evidence found, check passes
Tick the checkbox (`- [ ]` → `- [x]`) and append a dated one-line evidence note to that item
in the roadmap, in the style of Arc 2's build-13 note (`factory/cycles/02-capability-hardening/roadmap.md`,
the build-13 discharge line): the *evidence* + the *date*, one line, with an exact citation
(`file:line`, a ledger key, or a lint count). Not "looks fine" — the specific fact that
settles it.

- **Subject-match is mandatory.** If the check names its evidence subject (a specific
  partner, wearer, vault, or file) and the evidence found is about a *different* subject,
  the item is not silently DISCHARGED. State the substitution explicitly in the discharge
  note and get an owner ruling that the substitute is acceptable — acceptance passing on
  substitutes without saying so is how a named subject's gap survives unexamined (the
  Arc 3 exemplar: a check named dog-trainer + health-coach, was discharged against
  chess-coach + a second vault's wearer, and the named subjects' dry tail went unnoticed).
  In headless mode: leave the item open and surface the proposed substitution in the report.
- **Vacuous discharge is a real, statable outcome.** When an item's condition can't fire
  because the precondition never existed in this vault (e.g. a subsumption item that offers to
  retire an overlay, run against a vault that has no overlays), discharge it and say so:
  *"vacuous — no overlay existed to subsume."* Comfortable and explicit beats silently
  ticking or silently leaving open.

### STILL-OPEN — needs first-exercise evidence that hasn't occurred
The item requires an event that hasn't happened yet (e.g. "next mint exercises the consumer
lock," "first post-upgrade write op honors the overlaid rule," a design-stage evidence debt
like an M0 audit or two measured lint cycles). Leave it unchecked. Annotate it with the exact
event that will discharge it **and the trigger that produces that event** — an owner action,
a vault-side first use, or a dated clock. A tail you cannot name a trigger for is not
STILL-OPEN; it is BLOCKED (below). **Never tick on "should be fine"** — a first-exercise
tail is only discharged by the first exercise.

- **Pass-through tripwire.** When an event *of the discharging kind* has already occurred
  without firing the check (the exact flow ran and never touched the surface under test —
  Arc 3's proof: a mint ran the full flow and the consumer-lock convention "reads clean
  forever at zero specs"), or a tail survives its **second** discharge run unfired,
  re-annotating STILL-OPEN is forbidden. Mandatorily re-examine reachability: can any
  shipped surface actually produce the discharging event? If not, the grade is BLOCKED.

### FAILED — evidence contradicts the check
Leave it unchecked. Annotate the item with what the evidence actually showed. Then **draft an
inbox filing** capturing the defect (naming shape `YYYY-MM-DD-HHmmss-slug.md`, content shape
per `{project-root}/factory/inbox/README.md`) — write the draft, show the owner, and file it on
confirmation. **The draft must carry a complete specimen manifest** — see the manifest rule
below; this stage is the last one that still holds the specimens. This is how the loop closes on a bad acceptance: the contradiction becomes new
field signal, not a silent gap. In headless mode, surface the drafted filing in the report and
leave filing to the owner (`status: blocked`).

### BLOCKED (unreachable) — the discharging event cannot occur
The item waits on an event that **no shipped surface can produce** — no owner action,
vault-side first use, or dated clock triggers it. This is not a waiting state, and it must
not be re-annotated as STILL-OPEN: waiting cannot discharge it. Leave it unchecked, annotate
it `BLOCKED (unreachable)` with *why* the event can't fire, and route it exactly like
FAILED — draft an inbox filing capturing the gap (same naming and content shape, **same
specimen-manifest obligation**, same owner-confirm step; headless: surface the draft,
`status: blocked`). The unreachable tail is
module signal — a design gap for `inbox-capture` to route into a build, after which the
shipped fix gives the tail a real trigger and a future discharge run can grade it honestly.

### The specimen manifest — FAILED and BLOCKED filings carry the set, never a count

*(Platform P-18 Tier A, 2026-09-01; cause `ST-5`, *specimens have no owner*.)* **You are standing
at the moment of maximum evidence, and it is the last one.** The report is open, the slugs are on
screen, the returned values are in front of you. By the time a briefer builds the instrument that
grades this defect, every one of those specimens is gone unless this filing carried it — the
Cycle 12 build-1 trace is 20 observed → 2 filed → **0 reaching the brief**, and the fixture built
in their absence passed at rest while the field failed twice.

So a filing this stage drafts for a **FAILED** or **BLOCKED (unreachable)** item carries a
complete specimen manifest: **the full set, every member named** (not a sample), plus the
**minimal triggering fragment** quoted from the evidence you are reading. The shape is
single-homed at `{project-root}/factory/inbox/README.md` — follow it there, don't restate it.

Two rules that bite here specifically:

- **A count is not a manifest.** If you write *"N entries"*, the set must appear too. Where the
  evidence genuinely does not carry the members (the report persisted a total and nothing else),
  say exactly that in the filing — an honest *"count only, members not recoverable from
  `<report>`"* is a usable fact; a bare number is a dead end.
- **This is not spelunking.** The standing instruction to read only what the item names still
  holds. The manifest comes from **the evidence you already opened to grade the item** — you are
  recording what is in front of you, not going to look for more.

### Split items — one checkbox, mixed sub-clauses
A per-build ledger item routinely bundles upgrade-side sub-clauses (dischargeable the moment
the upgrade runs — seeding, provision, convergence) with first-exercise sub-clauses (a mint, a
lint cycle, a relay that hasn't happened yet). A checkbox is one bit; the item isn't. Leave it
**unchecked** — a bundled item is DISCHARGED only when *every* sub-clause is — but append a
dated annotation that records the split explicitly: `Upgrade-side DISCHARGED <date> (<evidence
per sub-clause>); STILL-OPEN: <named first-exercise tails>`. Don't tick on the discharged half
and don't bury the open half — the annotation is what lets the next run (and `cycle-closeout`)
see exactly what acceptance is still waiting on.

## Stage 3 — Archive & Sync

### Archive accepted filings
A field filing moves `{project-root}/factory/inbox/<filing>.md` →
`{project-root}/factory/cycles/<open cycle>/filings/` only when **all** of that filing's
ledger items are DISCHARGED (lifecycle step 7: a filing archives only after its build has
shipped *and* passed acceptance). Use a plain `mv` — the move lands as an ordinary
working-tree change; this skill does not commit.

- **Early release is an owner call, never an assumption.** A filing whose only remaining items
  are STILL-OPEN first-exercise tails *may* be released early if the owner rules that the tail
  is a standing watch rather than a blocking debt — ask, don't decide. In headless mode, don't
  release early; leave the filing and note the tail.
- Map ledger items to filings via the roadmap's `derives_from:` / the item's build reference.
  If an item's filing ownership is ambiguous, say so rather than guessing which filing it
  gates.

### Sync the record
- **Roadmap frontmatter `status`:** if the overall cycle acceptance state changed, update the
  status line to reflect it (e.g. "acceptance pending" → "acceptance discharged except
  <named first-exercise tails>"). State the tails by name — a bare "discharged" hides what's
  still open.
- **Project memory:** per the `CLAUDE.local.md` obligation, durable cycle state lives in Claude's
  project memory and must stay in sync with the roadmap. Perform or explicitly remind the owner
  to update the cycle's memory entry to match the new ledger state.
- **Do not close the cycle.** Flipping the roadmap to closed/shipped and moving its filings is
  `cycle-closeout`'s job. This skill leaves the roadmap open with an accurate, current ledger.

## Report

Summarize, per item, the verdict and its one-line reason: how many DISCHARGED (with the
evidence that settled each, and any subject substitutions stated), how many STILL-OPEN (with
the event that will discharge each and its trigger), how many FAILED or BLOCKED (each with
its drafted filing). List filings archived and filings held. Name the first-exercise tails
explicitly so the owner sees exactly what acceptance is still waiting on.

**Restamp the cycle roadmap's foot** — its **last block**, below any earlier routing — with the **Next lifecycle move**, then end the report with
the same line (routing contract — `.claude/skills/vlt-lifecycle.md`), derived from the run's
aggregate outcome; a discharge run must never end on a bare state description. **The roadmap's
foot is the obligation; the chat report is a copy** *(platform P-13)*:

- **Every item checked or owner-carried** → next move is `cycle-closeout` ("close the cycle").
- **STILL-OPEN tails remain** → for each, name the discharging event AND who or what
  triggers it (an owner action, a vault-side first use, a dated clock) — then "re-run
  acceptance discharge once <soonest event> has occurred." (A tail with no trigger was
  already graded BLOCKED in Stage 2, not STILL-OPEN.)
- **FAILED or BLOCKED items** → their drafted filings route into the next `inbox-capture`
  run; say so.
- **No evidence source yet** → next move is the owner running `vlt-upgrade` on a field vault.

Headless: the same move goes in the JSON `next` field.
