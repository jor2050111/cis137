# Contributing to the CIS137 Textbook

This book is an open educational resource for CIS137 at Phoenix
College. Colleagues and readers are welcome to point out what is wrong
and what could be better. There are two ways in. Most people only need
the first.

## 1. File a ticket (no setup, the fast path)

Open the [new issue chooser](https://github.com/jor2050111/cis137/issues/new/choose)
and pick a form:

* **Correction**: a fact, a step, a term, a link, or a sample is wrong.
* **Suggestion**: nothing is wrong, but a passage, lab, example, or
  figure could be clearer or stronger.
* **Question**: a passage is unclear and you are not sure which of the
  two it is.

Each form asks for the same four things: where in the book, what the
problem is, the fix you would print, and the source that backs it. The
source is the field that lets a fix ship without a second round.

Issues on this repository are public. Never name a student, paste
student work, or describe a student in a way that identifies them. That
holds for the ticket, every comment on it, and any file you attach.

What happens next: a new ticket carries `needs-triage`. Mr. Vega reads
it and moves it to `accepted`, `declined` (the closing comment says
why), or `needs-source`. Once the change is live on the site, the
ticket closes as `shipped`.

## 2. Propose an edit (fork and pull request)

If you want to make the change yourself:

1. Fork the repository and create a branch.
2. Edit the Markdown in `book/`. Only `book/` publishes. `docs/` holds
   authoring references and stays off the site.
3. Build the site locally to see your change. The README has the
   commands.
4. Run the checks listed at the end of this page.
5. Open a pull request that says what changed and why, with the source.

Nothing deploys from a pull request. The site rebuilds only when a
change lands on `main`.

## The five rules every change follows

### Rule 1. Synced files are never hand-edited

These files are copies of a canonical set that the whole textbook
family shares. The next sync overwrites them:

* `book/stylesheets/colors.css` and `book/stylesheets/brand.css`
* `book/javascripts/a11y.js`
* `book/skills-lab-rubric.md`
* `docs/style-guide-core.md`
* `.github/workflows/docs.yml`
* `.markdownlint.json`, `.vscode/settings.json`, `.gitignore`, and
  `requirements-docs.txt`
* `tools/check_output_comments.py`, `tools/check_sentence_length.py`,
  and `tools/run_chapter_code.py`

If your change belongs in one of them, file a ticket and say so. The
canonical copy lives outside this repository.

### Rule 2. Every sample response is a logged capture, never edited

Each prompt and sample response in the book came from a real run of a
named tool, and the run is logged in `docs/execution-logs/`. A capture
may be trimmed to the lines the lesson needs, with `[...]` marking a
cut. Nothing else in it changes, not even a typo.

To change a sample: run the prompt again, paste the new capture, add it
to the chapter's log, and name the tool and the date in the pull
request. Never write a response by hand.

### Rule 3. The style law

The writing rules live in `docs/style-guide-core.md` (family-wide) and
`docs/style-guide.md` (this book). The short version:

* Second person ("you"), active voice, sentences under 35 words.
* No em dashes. End the sentence, or use a comma, a colon, or
  parentheses. Never a hyphen in their place.
* No semicolons.
* No filler and no AI-tell vocabulary. The banned list is in the style
  guide, and `tools/check_style.py` scans for it.
* "Industry-relevant," never `real-world`. The one exception is MCCCD
  text quoted verbatim.
* Heading levels never skip.

### Rule 4. Schedule neutrality

Chapter content never names weeks, due dates, exams, or term labels.
Instructors map the chapters onto a 9-, 12-, 14-, or 16-week course in
their own course layer, so the book has to fit all of them.

### Rule 5. The license

Contributions ship under the book's license, CC BY-NC-SA 4.0 (the full
text is in [LICENSE](LICENSE)). Opening a pull request means you agree
to that. Quote third-party text only where its own license allows it,
and cite it where it appears. Official MCCCD course text stays the
district's.

## Checks to run before a pull request

From the repository root, with `NN` as the two-digit chapter number:

```bash
python3 tools/check_course_structure.py book/chapters/chapter-NN.md
python3 tools/check_style.py book/chapters/chapter-NN.md
python3 tools/check_sentence_length.py book/chapters/chapter-NN.md
python3 tools/check_samples_vs_log.py book/chapters/chapter-NN.md docs/execution-logs/chapter-NN-responses.md
python3 tools/check_key_terms.py book/chapters/chapter-NN.md book/glossary.md
python3 tools/check_readability.py
```

A clean run prints no hits and exits 0. The readability script scores
the whole book and takes no arguments.

## Where the answer keys are

Instructor answer keys are not in this repository. Ask Mr. Vega
directly if you teach the course and need them.
