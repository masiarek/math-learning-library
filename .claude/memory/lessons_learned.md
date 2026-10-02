# Lessons learned

Pitfalls met in earlier sessions. Check here before repeating an approach.

- **Wikipedia, Math is Fun and the Stanford Encyclopedia are blocked** by the network policy too, like YouTube. Describe such a page from memory, say so on the page, and add a "how sure" column where the claims matter.
- **YouTube is blocked** in cloud sessions by the network policy. Find the title with a web search on the video ID, then ask the owner for the transcript or description.
- **The owner's external drive is unreachable** from cloud sessions. Search Google Drive first; otherwise ask the owner to upload the file or run a local session (`claude remote-control` in the repo folder).
- **Chapter `README.md` files have paragraphs of many kilobytes on one line.** Do not pipe them through `rev`, `cut` and friends in long chains (one such command hung until killed); slice them with a short Python script.
- **A new example has no answer key**: run `python3 tools/run_examples.py --only <stem> --update` once, then the plain check.
- **After a pull request is merged**, restart the working branch from `origin/master` before new work. The push is then a fast-forward; force pushes are denied in `.claude/settings.json` and must not be worked around.
- **Studies cited from memory** (author, year, journal) should be said to be from memory in the reply, so the owner knows they were not looked up.
- **The Polish summaries use „ and a plain " as closing quote.** When editing one with a Python script, wrap the match strings in triple quotes; a double-quoted string ends at the first ".
- **The container's Python rejects an f-string whose expression reuses the outer quote** (`f"{"#"}"` is a SyntaxError). Use the other quote type inside.
- **A universe for the model checker must contain the witness set.** The two-cycle a = {b}, b = {a} satisfies foundation on its own; it fails only once the pair {a, b} is a point. Build the set the exercise names into the universe before claiming an axiom fails.
