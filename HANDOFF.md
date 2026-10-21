# CIS137 Textbook: HANDOFF

**Last updated:** 2026-10-21 (Planning session: merge of both sessions' work, Opus review of chapter 1 folded in, chapter 1 awaiting Mr. Vega's edits)
**Repo:** https://github.com/jor2050111/cis137
**Live site:** https://jor2050111.github.io/cis137/
**Task list:** cis137-fall27 (`export CLAUDE_CODE_TASK_LIST_ID=cis137-fall27`; the term is HQ Decision "First offering term")
**HQ:** Project recu4GSoXTE381m4m, Context recQcWyyt9Sj7Gr5r, Task recTFTaVUmjkeeoOP, Decisions D10-D15 (ids in the Stand-down section)
**Brief:** `docs/starter-prompt.md` (moved from the root once the scaffold matched the family layout)

## What was done (2026-10-21, afternoon): merge of the two sessions' work

The CIS137 Planning session took over by Mr. Vega's ruling (comment on
HQ task recTFTaVUmjkeeoOP, 2026-10-21). It compared the cis137-build
versions at HEAD with its own drafts at 6401a24 and kept the best of
both:

* `docs/CIS137_CLOs.md`: the cis137-build version stays the base
  (Arabic CLO numbers that match MCCCD and every other file, the
  chapter alignment table, the certificate context). Added from the
  Planning draft: the outline-section-to-competency crosswalk, the
  verbatim "real-world" note, and the schedule-neutrality note on the
  first term (D11).
* `docs/part-structure.md`: the cis137-build chapter plan and
  Copperwind spine stay (they match chapter 1 and the D13
  recommendation). Added from the Planning draft: a per-chapter
  upgrade placement table (spine block, fading mode, Fix It candidate,
  reach-backs), a pedagogy-upgrades bullet in the rationale, and
  content bullets for chapters 2, 5, 6, 8, 9, 10, 11, and 12
  (knowledge cutoffs, grounding, evaluation criteria before the first
  run, OECD principles, Copyright Office guidance, FERPA and HIPAA
  touchpoints, case studies, keeping a survey current, piloting, the
  capstone option). The title says "Proposed, awaiting approval" until
  D12 is ruled.
* `book/index.md`: the cis137-build page stays (9-week mapping,
  Sources & Permissions). Shorter sentences in the About and Part
  blurbs lifted Flesch from 52.5 to 57.3. The verbatim CLO lines keep
  it under 60. Added the "AI inside everyday apps" row and the
  sentence that says the syllabus names the roster.
* Law cleanup for a prompt-based book: `CLAUDE.md` (worked-example
  rules replace the code rules, kebab-case data files, no leftover
  "None (chapters teach from zero)" phrases in running prose),
  `README.md` (chapter count, roster accounts, checklist), the style
  guide and the chapter template (the sample label drops its
  semicolon), and the two templates' token leftovers.
* Chapter 1 checker hits cleared: six 35+ word sentences split, the
  three sample labels now read "Sample response (captured from a chat
  assistant, October 2026). Your output will differ:", and the
  glossary's "rather" is gone. Sentence checker 0 flagged, structure
  checker 0 errors, build clean, chapter Flesch 71.6.
* `assets/code/chapter-01/README.md` no longer tells students that
  item E is not AI and that item G is the policy risk. That README
  ships inside the data pack. An instructor answer key belongs in
  co-professor, not in this public repo, and is not yet written.
* Further Reading: the Dartmouth proposal link (http) returns 200 with
  application/pdf. The https form of that host does not respond, so
  the http link stays.
* Review: an Opus review of chapter 1 ran after these fixes. Its
  findings and what was done with them are in the entry that follows
  this one. The Codex CLI review still fails on the configured model
  as of 2026-10-21.

Open for Mr. Vega: rulings on D10-D15 and his edits to chapter 1 (his
version becomes the law for chapters 2-12). Ruled 2026-10-21: the
Planning session's two duplicate HQ records (Context recgSbFUS6NYamahA,
Project recnMAC0PeEgIBfiL) are deleted, and the Stand-down section at
the bottom of this file stays as history.

## What was done (2026-10-21, later): Opus review of chapter 1 folded in

The review (Opus, read-only, brief in the Planning session's scratchpad)
found 0 blockers, 8 majors, 27 minors, and 19 nits. What changed:

* MAJOR 1: the spam-filter commentary said the assistant "did not
  answer yes or no" while its own sample opens "Yes." Rewritten.
* MAJOR 2: "every tool is narrow" is now framed as a limit (no reliable
  planning, self-checking, or learning a new job) instead of a one-job
  rule that the multimodal paragraph contradicted. The glossary entries
  for narrow AI and AGI, Key Concepts, Retrieval item 2, Review Q3, and
  Lab Part 1 Task 3 match.
* MAJOR 3: the AI winters are no longer mapped onto the eras. The
  milestones table carries separate 1970s (first winter) and 1980s
  (expert systems, then the second winter) rows.
* MAJOR 4: the chapter states a test for rule-based system versus not
  AI (do the rules stand in for a judgment a person would otherwise
  make?) with a captured worked example, the payroll question (log
  Prompt 7). The lab accepts either answer when the test is applied.
* MAJOR 5: the teaching text no longer pre-answers the lab. The
  thermostat, tax deduction, VPN router, "WIRE TRANSFER" rule, face
  unlock, and "Because you watched" examples are replaced. In the
  packet, everyday system 10 is now a 1959 checkers program that
  learned by playing itself (Deep Blue stays in the chapter), and
  Copperwind item B is now a license-plate camera.
* MAJOR 6: the Era column is gone from the milestones table. Quick
  Check 1.2 Q1 and Lab Part 2 Task 1 ask students to place a milestone
  and defend a borderline case, not look one up.
* MAJOR 7: worked examples went from 4 to 8. New captures: the payroll
  question (Prompt 7) and the spam question run a second time (Prompt
  8, shown in Section 1.4 as "The Same Question, Asked Again" to teach
  why samples are samples). The logged responses to Try It Yourself
  1.4 and 1.5 appear after each Explain step as "Compare your run."
* MAJOR 8: the worksheet mirrors every chapter task word for word,
  with the pilot-risk line, the "your own prompt" slot, the two-label
  scheme (IN MY PROMPT or ADDED BY THE TOOL), and both Questions &
  Analysis questions. Headings read "Part 1, Task 1" so they no longer
  collide with section numbers.
* Minors applied: AI expanded on first use; the "forty words in this
  order" line; neural network defined by layers and deep by many
  layers; early learning ideas acknowledged inside the rules era; the
  1955 proposal versus 1956 workshop naming; the Section 1.4 subgoal
  labels sit on sentence boundaries (three steps) with "send it
  without the [Step] lines"; two sentences that paraphrased the
  captured Fix It response rewritten; colons instead of spaced hyphens
  in Further Reading; Elements of AI (University of Helsinki) replaces
  the vendor crash course; the three era terms added to the glossary
  and Key Terms, and the Turing test defined in prose; the comparison
  table's empty header cell named; three closing flourishes trimmed;
  Diagnose no longer gives away the three missing parts; TIY 1.2's Run
  step checks the prediction against the diagram; two Quick Check
  items raised to Apply; TIY 1.3 scoped to five apps; an under-18 line
  in the account steps; required steps moved out of admonitions into
  prose and a numbered list; the data-policy claims dated and hedged;
  Quick Check 1.3 Q3 no longer bends the rule; "Several systems can be
  argued two ways"; MLO 1.2 extended to the winter pattern so CLO 4
  has an MLO behind it, with Part 3 tagged to it; Review Q4 moved to
  a clinic case instead of repeating Lab Part 3 Task 2; the log's line
  count for Prompt 2 corrected.
* Not applied, for Mr. Vega: capture provenance (all eight samples are
  Claude through the Agent SDK or the Agent tool, not a roster
  product), the license (D15), and the remaining voice choices. Flesch
  is 72.2 after the additions, just above the band.
* Checkers after the pass: structure 0 errors, sentence length 0
  flagged, build clean, every labeled sample fence matched to the log
  by script, every Key Term resolves to a glossary headword.

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
Dropped and renamed "DUPLICATE, please delete". (Deleted later the
same day on Mr. Vega's ruling.) The task Status was
left as In progress for the Planning session to carry. No Decision
record was changed at stand-down.
