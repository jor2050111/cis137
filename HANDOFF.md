# CIS137 Textbook: HANDOFF

**Last updated:** 2026-10-21 (stand-down: chapter 1 draft committed, hand-over to the CIS137 Planning session)
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

## Stand-down (2026-10-21)

Mr. Vega ruled on 2026-10-21 that his session "CIS137 Planning" is the
dedicated CIS137 build session and that this session (cis137-build)
stands down. His words, relayed by the session that started this one:
"I want that other session to compare your version to it's own and
continue with the best of both notes." Everything below exists so that
comparison can happen. Nothing was deleted: no files, no HQ records, no
branches. Every change in the working tree was committed and pushed.

### (a) Exact state of work in progress

* **Chapter 1 draft:** `book/chapters/chapter-01.md`, 458 lines,
  unreviewed by Mr. Vega. Complete anatomy N.1-N.7: 3 MLOs (Analyze,
  Analyze, Apply), CLO block (CLO 2, CLO 4), five Try It Yourself
  blocks numbered 1.1-1.5 in reading order, four Quick Checks, Fix It
  1.1 in Section 1.4 (the vague "Tell me about the history of AI"
  prompt and its 560-word response, repaired to a five-line prompt),
  two flagship examples with `[Step k:]` labels (the three-way spam
  filter diagram in 1.1 and the four-part first prompt in 1.4), five
  Retrieval Practice items, Skills Lab 1A "Map the AI Around You"
  with the rubric transclusion, four Review Questions, five Further
  Reading links, Looking Ahead. Copperwind is introduced in Section
  1.4 before Try It Yourself 1.5 and carries Skills Lab Part 3.
* **Checker results at stand-down:** `tools/check_course_structure.py`
  0 errors. `zensical build --clean` no issues. Flesch 71.0 (chapter),
  68.2 combined, index.md 52.5 (below band, not yet addressed).
  **Known hits NOT fixed because the stand-down came first:**
  `check_sentence_length.py` flags six sentences at 35+ words (lines
  5, 104, 194, 364, 413, 458). Three prose semicolons sit in the
  "Sample response (captured from a chat assistant, October 2026; your
  output will differ):" labels at lines 60, 239, 317 (replace the
  semicolon with a period). `book/glossary.md` line 39 uses "rather"
  (banned filler) in the generative AI definition. No Codex or Opus
  review has run. No source manifest exists yet.
* **Glossary:** `book/glossary.md`, 21 chapter 1 terms in the CIS133
  definition-list format. Every Key Term in chapter 1 resolves to a
  headword (checked by script).
* **Data pack:** `assets/code/chapter-01/` holds `README.md`,
  `everyday-systems.txt` (12 systems), `copperwind-ai-inventory.txt`
  (Mei Lin's brief, items A-H), `skills-lab-1a-worksheet.md`. No
  instructor answer key has been written for the 12 systems.
* **Execution log:** `docs/execution-logs/chapter-01-responses.md`.
  Six prompts captured 2026-10-21 from Claude (Anthropic) run through
  the Claude Agent SDK (Sonnet) as a plain chat assistant with no
  tools and no memory between prompts. The chapter quotes them
  verbatim with `[...]` trims. Re-capture from a core-roster tool if
  Mr. Vega prefers, and update the log and the chapter labels.
* **Nav and home page:** chapter 1 is uncommented in `zensical.toml`
  and linked from `book/index.md` Getting Started. Pages deploys of
  the earlier commits succeeded (run 39639719824); the deploy of the
  stand-down commits was not checked.
* **Further Reading URLs** checked with curl on 2026-10-21: the UMBC
  copy of Turing's paper (200, replaced the Oxford Academic link that
  returned 403), the Dartmouth proposal PDF (200), arXiv 1706.03762
  (200), the Stanford AI Index (200), the Google ML Crash Course
  (200). The MCCCD course URL in `book/index.md` returns a Cloudflare
  403 to curl and needs a browser check for the source manifest.
  ai.maricopa.edu also returned 403 to curl (used only in the roster).
* **Not started:** chapters 2-12, subagent briefs, the publication
  gates, the Canvas phase. `README.md` still says 0 of 12 chapters
  and leaves the license as a TODO (HQ D15). The one-sentence course
  description in `zensical.toml`, `README.md`, `CLAUDE.md`, and
  `book/index.md` is a draft the starter prompt asked to confirm.

### (b) Cross-session messages received today, and what was done

These exist only in this session's transcript, so they are recorded
here in full substance.

**From "CIS137 Planning" (after the collision), five points:**

1. *Files.* It overwrote `book/index.md`, `docs/CIS137_CLOs.md`, and
   `docs/part-structure.md` at 10:01 and reported restoring them at
   10:03 from b6e509c. In fact this session's commit 6401a24 at
   10:02:43 had already swept its versions into HEAD, so its checkout
   was a no-op. This session restored its own versions from b6e509c
   in commit 732d575. The Planning session's drafts remain in history
   at 6401a24 (see section c).
2. *HQ duplicates.* It created a second Context (recgSbFUS6NYamahA)
   and a second Project (recnMAC0PeEgIBfiL) before finding this
   session's records, renamed both "DUPLICATE, please delete", and
   archived the project. Only Mr. Vega deletes HQ records. Nothing
   was done to them here.
3. *Bug report.* `CLAUDE.md` line 7 held a literal mangled regex
   backreference (`\1**Certificate:**...\n`) and the Primary Tools
   line was missing, from a lambda-based replacement in this session's
   fill script. Fixed in 732d575: the Primary Tools line is restored
   and the Certificate line follows it.
4. *District facts from its web search (unverified by this session):*
   help.maricopa.edu (SCC KB article 139) says all enrolled students
   get Microsoft 365 Copilot via MEID@maricopa.edu at
   m365.cloud.microsoft/apps, and PVCC's AI Tools page points to
   copilot.microsoft.com with MEID credentials. A CGCC CTLA page says
   District ITS enabled Gemini, NotebookLM, and Workspace Studio for
   faculty and staff only, with guidelines in development at the AI
   Resource Center (ai.maricopa.edu). MCLI publishes faculty guidance
   on generative AI and academic misconduct. Age rules from secondary
   guides: ChatGPT 13+ with guardian permission under 18, Gemini 13+
   on a personal account, Copilot 13+, Claude 18+ with no consent
   route, Perplexity 13+ with a parent accepting the terms. Folded
   into `docs/tool-roster.md` under "District facts (reported, not
   yet verified)" and into HQ D10's Detail and Recommendation (Copilot
   through the student's MEID becomes the one guaranteed tool).
5. *Alternative spine:* "Kestrel Row Books," a fictional independent
   bookstore and cafe (two Phoenix-area stores plus an online shop; its
   web search on 2026-10-21 found no name collisions). It puts invented
   quotes and ISBNs (accuracy), cover-art ownership (copyright),
   customer data (privacy), and hiring (bias) in one small
   organization, and its sales data gives CIS144 and CIS218 somewhere
   to continue. Added as option B on HQ D13 (this session's
   recommendation stayed Copperwind). Its per-chapter spine blocks are
   in `git show 6401a24:docs/part-structure.md` and in that session's
   scratchpad at
   `/private/tmp/claude-501/-Users-vega/14842cef-2247-4d17-b111-816bd27daec9/scratchpad/cis137-parallel-drafts/`.

**From the session that started this one (relaying Mr. Vega):** the
stand-down ruling quoted at the top of this section. This section and
the two commits are the response.

### (c) Comparing the two versions

The Planning session's drafts of the three files live at commit
6401a24. This session's versions are at HEAD. Compare with:

```bash
git show 6401a24:docs/part-structure.md
git show 6401a24:docs/CIS137_CLOs.md
git show 6401a24:book/index.md
git diff 6401a24 HEAD -- docs/part-structure.md docs/CIS137_CLOs.md book/index.md
```

Differences noticed in passing, for the comparison: the Planning
session numbers the CLOs with Roman numerals (CLO I-VI) while this
session uses MCCCD's own Arabic numbers (CLO 1-6) so outline sections
(Roman) and competencies (Arabic) never collide. Its CLO document says
no MLO is tagged Create and that Chapter 12 is primary for no CLO.
Its home page maps to an 8-week course (the family documents say 9-)
and drops the Sources & Permissions section. It adds an "office-suite
assistants" row to the tool table. This session's `CLAUDE.md`, chapter
template, chapter 1, HQ Decisions, and this HANDOFF all use the Arabic
numbering, so a switch to Roman needs a sweep across those files.

### (d) HQ records this session created

| Record | ID |
| ------ | -- |
| Project: CIS137 textbook and Canvas build | recu4GSoXTE381m4m |
| Context: CIS137 (Course) | recQcWyyt9Sj7Gr5r |
| Task: Build the CIS137 textbook (In progress, assignee Claude, delegated by Mr. Vega) | recTFTaVUmjkeeoOP |
| D10: tool roster | recZkdNwJ82lco6dE |
| D11: first offering term | reczXLgPTQBc6OPxN |
| D12: chapter plan | rectiIQLXMNValu0q |
| D13: resumable spine | recMI08ZOEjtqD1Cq |
| D14: Canvas shell | receSuoL6KpnnLNUB |
| D15: book license | rec1pXkMYJvlyFhAA |

The two records the Planning session created (Context
recgSbFUS6NYamahA, Project recnMAC0PeEgIBfiL) are already marked
Dropped and renamed "DUPLICATE, please delete". The task Status was
left as In progress for the Planning session to carry. No Decision
record was changed at stand-down.
