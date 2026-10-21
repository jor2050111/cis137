# CIS137 Textbook: HANDOFF

**Last updated:** 2026-10-21 (scaffold, CLO reference, Part structure proposal)
**Repo:** https://github.com/jor2050111/cis137
**Live site:** https://jor2050111.github.io/cis137/
**Task list:** cis137-fall27 (`export CLAUDE_CODE_TASK_LIST_ID=cis137-fall27`; the term is HQ Decision "First offering term")
**HQ:** Project recu4GSoXTE381m4m, Context recQcWyyt9Sj7Gr5r, task record in the Tasks table (see the HQ Decisions filed 2026-10-21)
**Brief:** `docs/starter-prompt.md` (moved from the root once the scaffold matched the family layout)

## What was done (2026-10-21): scaffold and course references

* Read the MCCCD context pack (`docs/mcccd/`), the family README and
  setup guide, the CIS133 and CIS215 exemplars (CLAUDE.md, CLOs,
  chapter template, chapter 1), the quality rubric V2.1, the pedagogy
  playbook V1.1, and the CIS133 pedagogy spec (Copperwind canon).
* HQ first: no CIS137 project or task existed. Created the Project,
  the CIS137 Context (Course), and the build task (claimed, In
  progress, delegated by Mr. Vega).
* Instantiated the template in place (`cp -R ../template/. .`),
  removed the setup guide, replaced every token (grep returns
  nothing), synced the shared files, seeded the Bloom's reference,
  built the venv (Zensical 0.0.46 plus textstat).
* Wrote `docs/CIS137_CLOs.md`: the six official competencies verbatim
  with MCCCD's section references, RBT-tagged CLOs that keep the
  official wording, a CLO-to-chapter map, chapter alignment blocks,
  the full outline, and the certificate context.
* Wrote `docs/part-structure.md`: 12 chapters in 4 Parts that follow
  the outline sections in order, with the design rationale, coverage
  matrices, dependencies, and the spine proposal. Awaiting approval.
* Filled the course-configured sections of `CLAUDE.md` (Flesch band,
  Bloom's rule, worked-example length, load pattern, naming, tool
  targets, terminology, quick-reference CLOs) and added the Pedagogy
  Upgrade Law section with the checker contract.
* Wrote `docs/style-guide.md` (course layer), `docs/tool-roster.md`
  (proposal), `book/index.md` (home page with verbatim CLOs), and the
  glossary header in the CIS133 definition-list format.
* Adapted the CIS133 chapter template to prompt-and-response worked
  examples (`templates/chapter-template.md`) and the CIS133 structure
  checker to this book (`tools/check_course_structure.py`: 5 TIYs per
  chapter, no executable-language fences). Copied the readability
  checker.
* Checked the Maricopa schedule snapshot (no CIS137 section for
  Phoenix College) and the Canvas API (no CIS137 shell among 54
  teacher enrollments).

## Decisions filed in HQ (2026-10-21), each with a recommendation

1. Tool roster (recommendation in `docs/tool-roster.md`)
2. First offering term (recommendation: Fall 2027, task list
   `cis137-fall27`; nothing in the book depends on it)
3. Chapter count and Part structure (recommendation:
   `docs/part-structure.md` as written)
4. The resumable spine (recommendation: Copperwind IT Services,
   student as AI adoption assistant, Mei Lin leads)
5. Canvas shell (none exists; recommendation: request
   `pc.dev.cis137.vega`, park the Canvas phase)
6. Book license (recommendation: CC BY-NC-SA 4.0, displayed on the
   home page before publication; rubric gate G6)

## Pending

* Mr. Vega's rulings on the six Decisions. Chapter 1 proceeds on the
  recommendations and is flagged as such.
* The one-sentence course description in the setup table is a draft
  the starter prompt asked to confirm with Mr. Vega. It is in
  `zensical.toml`, `README.md`, `CLAUDE.md`, and `book/index.md`.

## Next steps

1. Chapter 1 end to end (every section of the locked anatomy, the
   Skills Lab with the transcluded rubric, the five upgrades, the
   checkers green). Stop for Mr. Vega's edits. His version is the law
   for chapters 2-12.
2. Chapters 2-12: fan out to Opus subagents, three chapters per agent,
   one brief file, one output file each. Assemble, run the checkers,
   get a review (Codex plugin or Opus; the CLI `codex review` fails
   on the configured model as of 2026-10-21).
3. Publication gates G1-G8. Record the evaluation in
   `../evaluations/`.
4. Canvas phase only when a shell exists and Mr. Vega says go. The
   Canvas build lives in co-professor under
   `01-teaching/<NN-cis137-...>/canvas-pages/`, not here.

## How to continue

```bash
cd /Users/vega/Documents/code/textbooks/cis137
export CLAUDE_CODE_TASK_LIST_ID=cis137-fall27
.venv/bin/zensical build --clean          # must report no issues
python3 tools/check_course_structure.py --all
python3 tools/check_sentence_length.py book/chapters/chapter-01.md
.venv/bin/python tools/check_readability.py
```

Read `CLAUDE.md`, then `docs/part-structure.md`, then
`docs/CIS137_CLOs.md`. Every sample AI response in a chapter is
captured from a real run and logged in `docs/execution-logs/`.
