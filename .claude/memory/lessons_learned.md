# Lessons learned

Pitfalls met in earlier sessions. Check here before repeating an approach.

- **YouTube is blocked** in cloud sessions by the network policy. Find the title with a web search on the video ID, then ask the owner for the transcript or description.
- **The owner's external drive is unreachable** from cloud sessions. Search Google Drive first; otherwise ask the owner to upload the file or run a local session (`claude remote-control` in the repo folder).
- **Chapter `README.md` files have paragraphs of many kilobytes on one line.** Do not pipe them through `rev`, `cut` and friends in long chains (one such command hung until killed); slice them with a short Python script.
- **A new example has no answer key**: run `python3 tools/run_examples.py --only <stem> --update` once, then the plain check.
- **After a pull request is merged**, restart the working branch from `origin/master` before new work. The push is then a fast-forward; force pushes are denied in `.claude/settings.json` and must not be worked around.
- **Studies cited from memory** (author, year, journal) should be said to be from memory in the reply, so the owner knows they were not looked up.
