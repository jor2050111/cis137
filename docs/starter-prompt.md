# Starter prompt: build the Phoenix College CIS137 textbook, then its Canvas course

This file is the brief for one Claude Code session that works only on
CIS137. Run the session from `/Users/vega/Documents/code/textbooks/cis137`.
Once the repo is scaffolded, move this file to `docs/starter-prompt.md`
so the root matches the family layout. `HANDOFF.md` carries the history
from then on.

## Mission

Build the OER textbook for CIS137, Artificial Intelligence Fundamentals
(3 credits), as the next member of the Phoenix College textbook family,
to the standard of the two latest books, `cis133` and `cis215`. When the
book is complete and a CIS137 Canvas shell exists, build the Canvas
course from the book with the V2 playbook.

Next year Phoenix College plans to offer the whole Foundations of
Applied Artificial Intelligence certificate (CCL 5364N: CIS137, CIS144,
CIS218). Write CIS137 as the first course of that sequence. Build only
CIS137 now.

## Read first, in this order

1. `docs/mcccd/index.html` (or `docs/mcccd/README.md`): the official
   MCCCD outline and competencies for CIS137, the CIS144 and CIS218
   outlines, the certificate page, and a reading of what CIS137 must set
   up for the next two courses. Official text is verbatim. The source
   markdown is in `docs/mcccd/source/`.
2. `../README.md` and `../template/NEW-TEXTBOOK-SETUP.md`: the family
   layout and the three-stage setup (interview, instantiate, verify).
3. The exemplars. Read these in full: `../cis133/CLAUDE.md`,
   `../cis133/docs/CIS133_CLOs.md`, `../cis133/templates/chapter-template.md`,
   `../cis133/book/chapters/chapter-01.md`, and the same four files in
   `../cis215/`. Digest the other chapters with a script or a subagent.
   Do not read 24 chapters end to end.
4. `../TEXTBOOK-QUALITY-RUBRIC-V2.md` (publication gates G1 to G7 and
   the fifteen criteria) and `../PEDAGOGY-UPGRADE-PLAYBOOK-V1.md` (the
   five upgrades). Build the upgrades in from chapter 1. They are not a
   later pass.
5. `../CANVAS-COURSE-BUILD-PLAYBOOK-V2.md`: Canvas phase only. Skim it
   now and read it in full before that phase.

All global law loads from `~/.claude/CLAUDE.md` and the claude-config
rules: pedagogy, voice, the em dash policy, banned vocabulary, Flesch
60-70, the 50/50 rubric, HQ habits, subagent delegation. Follow it. Do
not restate it in the new `CLAUDE.md` beyond what the template already
carries.

## Interview answers already settled

| Setup question | Answer |
| --- | --- |
| Course ID | CIS137 |
| Official title | Artificial Intelligence Fundamentals |
| One-sentence description (draft, confirm with Mr. Vega) | Learn how AI models work, write prompts that get better answers, judge AI output for accuracy, and use AI tools responsibly. |
| Audience | Community college students in their first AI course. No programming assumed. |
| Prerequisites | None. MCCCD suggests college-level reading (RDG100) and writing (ENG101) but does not require them. Chapters teach from zero. |
| Primary tools | Generative AI tools. MCCCD requires accounts on multiple tools. The roster is Decision 1 below. |
| Chapters and Parts | Default 12 chapters in 4 Parts. Propose the mapping to the five outline sections (Decision 3). |
| CLO source | `docs/mcccd/cis137-course-outline.html`: six competencies, five outline sections, with the section references after each competency. |
| Repo name | `cis137`. Local folder, GitHub repo, and Pages subpath all match. Site: https://jor2050111.github.io/cis137/ |
| Task list ID | `cis137-<term><yy>`. The term is Decision 2. |
| Bloom's targets | Introductory course. MCCCD's verbs run Apply through Evaluate (evaluate, differentiate, demonstrate, analyze, apply, select). MLOs ladder to those. Remember and Understand appear only as steps inside a chapter. |
| Flesch band | 60-70 |

## Decisions to put to Mr. Vega before chapter 2

File each as an HQ Decisions record with Detail, Options, and a
Recommendation. Urgency is Blocking only when writing cannot continue.

1. **Tool roster.** Which generative AI tools students create accounts
   on: free tiers, age and data policies, district guidance. Recommend a
   roster.
2. **First offering term** for Phoenix College's CIS137. Run the
   `course-sections` skill first. The snapshot may already answer it.
   The term sets the task list ID and nothing in the book (schedule
   neutrality, rubric gate G2).
3. **Chapter count and Part structure.** Your proposal from the outline.
4. **The resumable spine** (pedagogy upgrade U1): the one fictional
   organization that threads the book.
5. **Canvas shell.** Does a CIS137 shell exist in Mr. Vega's Canvas
   enrollments? Check the Canvas API before assuming. If none exists,
   park the Canvas phase and say so in `HANDOFF.md`.

## Sequence

0. **HQ first.** Find or create the Project record for the CIS137 build
   and a task for the textbook. Claim it. Comment at every milestone,
   signed "Claude:". No student data, ever.
1. **Setup** per `NEW-TEXTBOOK-SETUP.md`. This folder already exists and
   holds `docs/mcccd/` and this file, so instantiate the template from
   inside `cis137` with a contents copy:

   ```bash
   cp -R ../template/. .
   rm NEW-TEXTBOOK-SETUP.md
   ```

   `cp -R ../template cis137` would nest a `template/` folder here. Then
   replace every token, sync the shared files, seed the Bloom's
   reference, create the repo, enable Pages, and build. The token grep
   must return nothing. Keep `docs/mcccd/` as it is.
2. **CLO reference.** Write `docs/CIS137_CLOs.md` in the CIS133 pattern:
   official competencies verbatim, elevated CLOs with Bloom's verbs, a
   CLO-to-chapter map, the full outline. Paste the elevated CLOs into the
   new `CLAUDE.md` quick reference and `book/index.md`.
3. **Chapter plan.** `docs/part-structure.md` and the nav in
   `zensical.toml`. Stop for approval.
4. **Chapter 1, end to end.** Every section of the locked chapter
   anatomy, the Skills Lab with the universal rubric, the checkers
   green. Stop for Mr. Vega's edits. His edited chapter is the law for
   the rest.
5. **Chapters 2 to 12.** Fan out to Opus subagents, three chapters per
   agent, one brief file, one output file each. Assemble, run the
   checkers (sentence length, structure, glossary, Flesch, output
   comments, code runs where any code exists), and get a Codex review
   before any chapter is called done.
6. **Publication gates** G1 to G7 from the rubric before the book is
   called ready. Record the evaluation in `../evaluations/`.
7. **Canvas phase**, only when the shell exists and Mr. Vega says go.
   Copy the toolchain from co-professor
   `01-teaching/05-cis133-web-development/canvas-pages/tools/` and
   re-point it. The Canvas build lives in co-professor under
   `01-teaching/<NN-cis137-...>/canvas-pages/`, not in this repo.

## Rules specific to this build

* Official MCCCD text stays verbatim wherever it is quoted, including
  "real-world" in outline section V.A and in CIS218 competency 5. Your
  own prose follows the banned list.
* Students use the tools from chapter 1. Lead every chapter with why the
  skill matters, then how. No "preparation for" framing.
* Tool names and vendor features will date faster than the
  competencies. Put them in callouts that can be refreshed, not in MLOs,
  competencies, or the glossary definitions.
* Stay inside CIS137. Agents, analytics pipelines, modeling, and
  deployment belong to CIS144 and CIS218. Point ahead to them without
  teaching them.
* Keep `HANDOFF.md` current. Commit and push at your own cadence.
* Delegation: calibrate chapter 1 yourself, fan out to `opus` subagents
  for chapters, use `sonnet` for mechanical checks, and Codex for
  review. As of 2026-10-21 `codex review` from the CLI fails on the
  configured model. Use the codex plugin commands or an Opus review
  until that is fixed, and say which one you used.
* When blocked, file a Decision. Never sit on a question.

## Done looks like

* `jor2050111/cis137` is public, Pages is live at
  https://jor2050111.github.io/cis137/, and the build has no issues.
* Twelve chapters with the locked anatomy and a Skills Lab each, a
  glossary, `docs/CIS137_CLOs.md`, checkers green, the rubric gates
  passed, `HANDOFF.md` current, HQ updated.
* Then, on Mr. Vega's go: the Canvas course built, verified
  byte-identical against Canvas, and left unpublished for his review.
