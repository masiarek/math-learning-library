# The owner

How the owner of this library works, as learned from sessions. Update when a session shows something new.

- Writes short, fast messages, often from a phone; typos are normal. Read for intent, and ask only when two readings lead to different work.
- A photo of a book page with a short note ("add to learning") means: find where it belongs in the library and publish it.
- Does not want to check or click anything: every finished piece of work goes all the way to merged on `master` in the same session (see `CLAUDE.md`).
- Reads Polish; every new page carries `## Po polsku, w skrócie`.
- Asks "why is it useful" about advice: answer that directly, in plain words, before or alongside any page change.
- Values honesty about evidence: popular and AI-written summaries get a "how sure is each claim" table, not a copy.
- Keeps books as PDFs on an external drive (a Samsung T7) and some notes in Google Drive. Cloud sessions can reach Google Drive but not the drive.
- Interests beyond this library: learning how to learn (now its own repository, `learning-to-learn-library`, where such material goes), programming (*The Programmer's Brain*, *Deep Work*; asked how Rust handles sets), AI tools and workflows.
- Sends tables of contents and sample pages of books as photos, often several books in one sitting, and asks "how good is this book", "what chapters first", "why is it useful". Answer with a verdict and a reading order, and put the verdict in the matching reading guide.
- Dislikes that every book spells the same idea differently. Keep the cross-book symbol table in `GLOSSARY.md` (Symbols) and the chapter table in `13_Axioms_of_Set_Theory` up to date when a new book arrives.
- Sends symbol charts and symbol tables from the web, several in a sitting, asking "is it correct" or "any mistakes": check every tile, record the verdict in the reading guide's infographic paragraph, and keep the symbol index at the end of `GLOSSARY.md` complete so each symbol is findable here. Math Vault's table is the one found correct so far.
- Reads on a phone and taps names in tables: every table whose cells name a term or a page should link them. Glossary anchors exist for this.
- The same in prose: when a sentence names a chapter or lesson of this library ("the axioms of Zermelo–Fraenkel set theory"), the name should link to its page, not only a See also entry at the bottom.
- Wants the positive statement first. A page called "What is a set?" must open with the definition; the case against weaker definitions is a separate page ("good def and poor def"), cross-referenced both ways.
- Asks for katas: exercise pages where a program checks each claim before the proof is attempted (`04_Sets/set_katas`, `13_Axioms_of_Set_Theory/axiom_katas`). Extend those rather than adding exercises elsewhere.
- Cross-checks flashcards with other AI tools and sends a screenshot when they disagree. Say first who is right, with how sure, then fix the card and the page if ours was wrong.
- Downloads a book or manual and asks "anything new for the sets pages?": answer in three lists, what is new (and add it), what the pages already have, and what goes to the inbox.
- Sends daily meditation texts (Lebell's *The Art of Living*, numbered “n of 94”) with “help me to grow”: answer in chat with the one claim, why it is useful, a how-sure line per claim, and a small practice. Such a text is not a lesson here (nothing a program can check); if kept anywhere, it belongs with the Learning to Learn library.
- Sometimes wants to prove a theorem themselves: asks to be “guided in the right direction” and comes back with questions one at a time, each one level down (“how do you prove it is horizontal?”). Give the plan and the questions to answer, not the proof; point at the page only afterwards; and tell them when a question has reached a definition or a given, which is where a proof stops.
- Learned school mathematics under Polish names and reads German; asks how American course names (precalculus, calculus) map onto those curricula. `reading_guides/curriculum_map` holds the map, with companion pages in both languages; extend it rather than answering in chat.
