# Conventions

House rules for writing a page here. Readers browsing lessons do not need this file; it is for whoever is about to add one.

## The shape of a lesson

```
01_Precision/
  significant_figures/
    README.md                        the lesson
    examples/
      significant_figures.py         the program
      significant_figures.out        its recorded output
```

One idea per folder. The folder name is the idea, in `lower_snake_case`, and it becomes a permanent URL — so name it for what it teaches, not for where it currently sits in the reading order.

## The page

Open with the title, then two lines that let a reader decide in five seconds whether this is their page:

```markdown
# Significant figures

**Level:** 101 · for anyone who took a science class

**One line:** Rounding is the action; significant figures are the rule that decides where the action has to stop.
```

`**Level:**` is `101` / `201` / `301` / `reference`, then `·`, then who it is for. The one-line summary states the *claim*, not the topic — "significant figures are not rounding" is a one-liner; "an introduction to significant figures" is a table-of-contents entry.

Do not hard-wrap paragraphs. Write each paragraph as one long line and let the editor soft-wrap; Markdown collapses single newlines anyway, so wrapped and unwrapped prose render identically and unwrapped diffs are readable.

## Output is generated, never typed

Mark the spot and let the tool fill it:

```markdown
<!-- output:significant_figures -->
<!-- /output -->
```

`tools/run_examples.py` runs the program and pastes what it actually printed, with a provenance line above the fence. Inside the markers is generated; outside is yours. The stem is bare — no path — so example stems must be unique repo-wide, which the tool enforces.

There is a second kind, `<!-- source:stem -->`, which pastes the program itself. Use it when the code *is* the lesson and a hand-copied fence could silently drift from the file CI runs.

```bash
python3 tools/run_examples.py            # verify + refill
python3 tools/run_examples.py --update   # record current output as the answer key
python3 tools/run_examples.py --check    # write nothing, fail on drift (CI)
python3 tools/run_examples.py --only X   # touch example X and nothing else
```

Use `--only` when someone else is working in the tree: a full `--update` re-records every key and would adopt whatever their half-finished example happens to print.

## The program

**Stdlib only.** No exceptions. A reader must be able to run any page with the `python3` already on their machine, and CI has no install step to prove it.

**Deterministic.** No clocks, no randomness, no network, no filesystem. The output is an answer key, so it has to be the same on every machine forever. If an example genuinely needs randomness, seed it explicitly in the file.

**Written to be read aloud.** These programs are teaching instruments: numbered sections, aligned columns, and prose in the print statements. A reader should be able to understand the output without the page, and the page without the output — the two reinforce, neither substitutes.

**A short snippet in the prose puts its output in a trailing comment**, on the line that prints it, so the whole thing survives a copy-paste:

```python
f"{3200002:.2g}"   # '3.2e+06'
```

## Links

Link a folder by naming its `README.md` — `[label](some_folder/README.md)`, never `[label](some_folder/)`. The bare form works on GitHub and on the built site and fails everywhere else, including any local Markdown viewer, because MkDocs leaves it unrewritten.

A repo path in backticks should be a link, not bare code text: put the backticks in the label and a real relative path in the href.

Mark external links with `↗` so a reader knows they are leaving.

## Nav order

Sidebar reading order lives in `NAV_ORDER` in `mkdocs_hooks.py`, keyed by folder path. **Never set order by renaming files to `01_`, `02_`** — a filename is a permanent URL, and inserting one lesson would move every page after it. Unlisted pages sort alphabetically at the bottom, so adding a page needs no edit there.

## Before you commit

```bash
python3 tools/run_examples.py --check
uv run --group docs mkdocs build --strict
```

Both are what CI runs. `--strict` fails on a broken internal link, which is the failure most likely to reach the published site unnoticed.
