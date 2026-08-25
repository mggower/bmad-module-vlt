# A ruling answered by a release never reaches the issue that asked for it

_Filed 2026-08-25 by the owner, on field evidence from `{field-vault}` (verified against the
tracker, not recalled). Classification: **defect — feedback rail**. Related: the PARA
location-as-trust-proxy filing of the same date._

## The defect

`{field-vault}` filed a ruling request upstream as tracker issue **#11** (a partner's
human-facing artifact had no legal home in a browsable zone), parked its own work as a
deliberate reversible interim, and waited on the ruling.

Cycle 11 **answered it** — v0.15.0's build-2 rewrote the contract clauses the issue was about.
The answer shipped as **contract text only**. Issue #11 received no comment and no close; it
remains **OPEN with zero comments**.

Two consequences, both live:

- **The tracker misreports candidacy.** A vault (or a person) checking whether a question is
  still open gets the wrong answer indefinitely. The rail's whole value is that issue state is
  readable as project state.
- **The answer is undiscoverable from where the question was asked.** The filer must already
  know a release happened, and must read the contract diff to learn their issue was addressed.

Note the ruling that shipped did **not** in fact resolve the filer's operation (see the
companion filing) — but that is a separate matter. Even had it fully resolved it, the issue
would still be open, because **nothing in the loop closes an issue that a release answered.**

## Where the gap is

`cycle-closeout` Stage 5 closes the issue behind a filing when that filing **retires** — its
build shipped and its clauses passed acceptance. That path works for a **materialized** filing
(one that arrived as an issue and became an inbox file with an `origin:` header).

This issue was never materialized. It arrived as a **ruling request**, was answered by a
build that came from a *different* capture path, and so was never bound to a filing that could
retire and carry it closed. The rail has a close mechanism for *filings*; it has none for
*questions answered by a ruling*.

## The fix direction

Give a ruling the same terminal obligation a filing has: **an upstream question is not
discharged until its issue is answered in the issue.**

Candidate shapes, for ideation to choose between:

- **Bind at capture.** When `inbox-capture` or `issue-triage` folds a tracker question into a
  roadmap entry, record the issue number on that entry. Closeout then closes every bound issue
  whose entry shipped and passed acceptance — the existing Stage 5 mechanism, extended from
  filings to bound questions.
- **Bind at ruling.** When an owner ruling answers a tracker question, the ruling records the
  issue number, and the release that carries it comments the ruling text onto the issue.
- **Sweep at closeout.** Closeout enumerates open issues older than the cycle and asks whether
  any were answered by it — a net, not a binding.

Preference is for **binding over sweeping**: a sweep is a list that will drift, and the standing
rule here is that lists claiming completeness fall behind.

This is plausibly **P-10's** territory (the one-way roadmap → tracker sync) rather than a new
item — the sync already writes milestones, build issues and stage labels from the roadmap, and
"close the issues this cycle answered" is the same direction of travel. Ideation should rule
whether it extends P-10 or stands alone.

## Immediate action, independent of the fix

Close **#11** with the ruling text, noting that the ruling changed the boundary without opening
the folder, and that the filer's operation is carried forward in the companion PARA filing.
