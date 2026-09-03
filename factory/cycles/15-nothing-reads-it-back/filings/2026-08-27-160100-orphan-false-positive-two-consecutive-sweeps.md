# The orphan check manufactured a false positive on two consecutive sweeps

_Filed 2026-08-27 from the first full `{field-vault}` sweep after the v0.16.2 upgrade
(`{lint_reports}/2026-08-27-1104-lint.yaml`, `instrument_findings`). Evidence read-only._

## The claim

The orphan check returned a page as an orphan while an inbound wikilink to it exists on disk —
**for the second sweep running**, on a different page each time. The sweep's own note:

> orphans false positive (1 of 1 — the slot is truly empty). `katsuo-dashi` was returned as an
> orphan, but `chicken-soup` carries an inbound `[[katsuo-dashi]]` link (and so does the index).
> Same scanner-omission class the 2026-08-26 sweep measured on `fantasy-football-evaluation` —
> **two consecutive sweeps, one false orphan each**.

## Specimen manifest

| Sweep | False orphan | Inbound link that exists |
|---|---|---|
| 2026-08-26 | `fantasy-football-evaluation` | (recorded in that sweep's `instrument_findings`) |
| 2026-08-27 | `katsuo-dashi` | `chicken-soup`, plus the index |

**1 of 1 in each sweep — a 100% false-positive rate on a slot whose true content is empty.**

## Relationship to existing signal — this is a SECOND field instance, not a new class

`factory/inbox/2026-08-26-164501-page-scanner-under-returns-outbound-links-and-manufactures-an-orphan.md`
already filed this class, and it was **captured as A14-2 in Cycle 14 and deliberately not built**
(the cycle's four builds took A14-1/3, A14-8, A14-6/7, A14-4/5). This filing does not re-open the
diagnosis; it adds the **recurrence datum** the capture could not have: it happens on **every**
full sweep observed since, on a different page each time, so it is a steady-rate defect rather than
a one-off.

## Why it matters

Orphan is a `fix_now` class whose legal response is to add a link or delete the page. A false
orphan therefore invites an edit to a page that is correctly linked. The rate is low in absolute
terms and 100% in relative terms: every orphan this instrument has reported across two sweeps has
been wrong, so the slot currently carries no trustworthy signal at all.

## Candidate direction

Grounded already in A14-2's filing — the page scanner under-returns outbound links, so the inbound
set computed from them is short by whatever it missed. Build it, or state that the orphan slot is
advisory until it is built.

⚠ **THIRD consecutive sweep, 2026-09-01** — `fantasy-platform-read-access` refused again, same
reason (a real inbound `[[fantasy-platform-read-access]]` from `fantasy-football-evaluation.md`, and it
is listed in the index). The filing's title says *two*; the count is now **three**, across two module
versions (0.16.2 and 0.17.1) and both a cold and two warm sweeps. Capture should read the title as
stale rather than as the measurement.
