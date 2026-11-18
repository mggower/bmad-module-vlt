<%*
// New task file for a zone task folder (Templater). Reads the folder it was created in:
// takes the key prefix from the files already there and the next free number,
// asks for a title and a sub-area, renames the file to KEY-slug, and writes the frontmatter.
// A session does not use this file: it writes the task by hand (task-board.md, Add a task).
const folder = tp.file.folder(true);
let prefix = null;
let max = 0;
for (const f of app.vault.getMarkdownFiles()) {
  if (f.parent.path !== folder) continue;
  const m = f.basename.match(/^([A-Z]{2,3})-(\d{3})-/);
  if (!m) continue;
  prefix = prefix ?? m[1];
  max = Math.max(max, Number(m[2]));
}
if (!prefix) prefix = await tp.system.prompt("Key prefix for this folder (two or three capitals)");
const key = `${prefix}-${String(max + 1).padStart(3, "0")}`;
const title = (await tp.system.prompt(`${key}: task title`)) || tp.file.title;
const sub = (await tp.system.prompt("Sub-area (one of the zone README's subs:)", "area")) || "area";
const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").split("-").slice(0, 7).join("-");
await tp.file.rename(`${key}-${slug}`);
const today = tp.date.now("YYYY-MM-DD");
-%>
---
type: record
created: <% today %>
last_updated: <% today %>
title: "Task — <% title.replace(/"/g, "'") %>"
summary: "<% title.replace(/"/g, "'") %>"
key: <% key %>
status: idea
sub: <% sub %>
theme:
---
# <% title %>

What is wanted and why.

## Done when

- 

## <% today %>

(owner) Filed.
