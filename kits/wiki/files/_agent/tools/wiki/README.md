---
type: resource
created: 2026-11-18
last_updated: 2026-11-18
title: Tool — wiki
---
# wiki

`check.py` runs three structural checks on `resources/wiki/`:

1. every page carries the four attestation keys (`author`, `trust`, `verified_by`, `verified_at`);
2. a page with `superseded_by:` names a page that exists;
3. the index and the folder agree: every page has a row in `index.md`, and every row has a page.

```bash
python3 _agent/tools/wiki/check.py
```

It is also run by `python3 _agent/tools/checks/run.py`. It says in its last line what it does not look at: it cannot tell whether a claim is true or current.

**Used by:** `ingest.md`, `supersede.md`, `consolidate.md`. The rules it reads are in `_meta/wiki.md`.
