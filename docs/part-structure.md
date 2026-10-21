# CIS137 Textbook: 12-Chapter Structure (Proposed, awaiting approval)

**Course:** CIS137: Artificial Intelligence Fundamentals
**Structure:** 12 chapters organized into 4 thematic Parts
**Pacing:** Schedule-neutral. Instructors may use the book in 9-, 12-,
14-, or 16-week courses without changing chapter content.
**Audience:** students in Phoenix College's bachelor's pathway in
information technology (a first- or second-year elective the program
recommends first), plus anyone in a first AI course.
**Prerequisite:** None. Chapters teach from zero. No programming is
assumed anywhere in the book.
**Last revised:** 2026-10-21 (proposal, awaiting Mr. Vega's approval:
HQ Decision D12. Merged from both 2026-10-21 sessions' drafts. The
title becomes "Authoritative" on his ruling.)

This document is the single authoritative plan for chapter order,
scope, and outcome coverage.

---

## Design Rationale

This plan synthesizes three sources:

1. **Official MCCCD competencies and course outline**
   (docs/CIS137_CLOs.md): six competencies, five outline sections.
   Every competency and every outline point maps to a chapter.
2. **The certificate context** (docs/mcccd/index.html): CIS137 is the
   first course of the Foundations of Applied Artificial Intelligence
   CCL. CIS144 (agentic AI, analytics) and CIS218 (integration,
   deployment) follow it. The book points ahead and never teaches
   their content.
3. **The textbook family structure:** 12 chapters in 4 Parts, the
   pattern proven by CIS215 and CIS133, with the five pedagogy
   upgrades (resumable spine, fading, cumulative retrieval, Fix It
   blocks, subgoal labels) built in from chapter 1.

**Key design decisions:**

* The four Parts follow MCCCD's outline sections in order. Sections I
  through IV each become a Part. Section V (the final project) joins
  Section IV in Part IV because the project is where tool selection
  pays off.
* Section I carries six outline points and two competencies, so it
  gets three chapters. Chapter 2 exists because competency 1
  (evaluate AI output for accuracy) runs through sections I-V, and
  students cannot judge output until they know, in plain terms, what
  a model does with their words and why it invents things.
* Section II (prompt engineering) gets one chapter per outline point
  pair: basics and types, effectiveness strategies, iterative
  refinement. Prompting is the skill students use in every later
  chapter, so it comes before the regulation and ethics Part.
* Section III (regulation and ethics) splits accuracy and bias (the
  testable half) from governance, privacy, and content ownership (the
  rules half), with business evaluation and tech trends in a third
  chapter that also carries competency 4 (the current state of AI).
* Chapter 12 is the project chapter. It synthesizes competencies 1,
  3, 4, 5, and 6 through a scenario solution, a presentation, and a
  reflection, exactly as outline section V lists them. It stays
  schedule-neutral: the chapter supplies the project, the course
  layer supplies the dates.
* Tool names and vendor features live in refreshable callouts. MLOs,
  competencies, and glossary definitions never name a vendor, so the
  book outlives any one product.
* No chapter contains executable code. Worked examples are prompts and
  sample responses in `text` fences, captured from real runs and
  labeled with the fact that AI output varies. The discipline gate for
  this book is the ethics, policy, law, and research gate from the
  family rubric: sourced claims, internally consistent lab packets,
  and tasks that admit more than one defensible answer when judgment
  is the target.
* The five pedagogy upgrades are planned per chapter from the start
  (table under The Resumable Spine): one spine block, the fading mode,
  a candidate Fix It theme, and the retrieval reach-backs. Chapters 1-4
  stay fully worked, chapters 5-8 carry one completion prompt each, and
  chapters 9-12 one problem-first prompt each.

**Rigor band (ruled 2026-10-21, mirrors CLAUDE.md):** CIS137 sits
between AI literacy and AI engineering. Students finish as the human in
the loop. Each chapter block below carries a Rigor step naming what a
literacy course would stop at and what the chapter asks instead. Every
Skills Lab Part 3 yields an artifact a manager could act on. The
student-facing contract is `book/fluency-contract.md`, transcluded
into the home page and linked from chapter 1. When the Canvas phase
opens, the course home page quotes the same contract.

**Bloom's rule for every MLO (course-configured, mirrors CLAUDE.md):**
MCCCD's competency verbs run Apply through Evaluate. MLOs ladder to
those levels: Apply and Analyze in Parts I and II, Analyze and Evaluate
in Parts III and IV, Create in the Chapter 12 project. Remember and
Understand appear only as steps inside a chapter, never as an MLO
level. Every MLO uses a measurable action verb. Never write
"understand," "know," or "learn" as the verb.

---

## Part I: Foundations of AI and Generative Tools (Chapters 1-3)

**Theme:** what AI is, how generative tools produce their output, and how to use them with judgment from the first day
**Learning arc:** Differentiate the types -> Explain the mechanism and its limits -> Use the tools with judgment
**Outcome alignment:** CLO 2, CLO 1 (begun), CLO 4 (introduced), CLO 5 (introduced)
**Bloom's focus:** Apply and Analyze

### Chapter 1: What Artificial Intelligence Is

**Subtitle:** DIFFERENTIATE the major types of AI and meet the tools you will use
**Outcome(s):** CLO 2, CLO 4
**Outline section(s):** I.A (AI tools overview), I.B (Milestones)
**Rigor step:** A literacy course would recognize AI. This chapter asks for a classification with a stated test, a logged first conversation read in three passes, and a pilot recommendation for Copperwind.

**Content:**

* AI as a family of techniques, not one thing: rule-based systems, machine learning, deep learning, generative AI
* Narrow AI versus general AI, and why every tool you can use today is narrow
* Milestones: the Turing test, expert systems, the machine learning turn, deep learning, transformers, and the chat assistant era
* The generative tool landscape: chat assistants, image generators, research tools, and the AI already inside everyday apps
* Creating a first account and holding a first conversation safely (what never to type into a tool)
* Copperwind IT Services, the fictional company that threads the book, and the student's role in it

**Prior-course parallel:** gap. CIS137 is new in 2026 and has no prior
Phoenix College build.
**Prerequisite bridge:** new content. The course has no prerequisite.

### Chapter 2: How Generative AI Works and Where It Fails

**Subtitle:** EXPLAIN what a model does with your words, then judge what comes back
**Outcome(s):** CLO 1, CLO 2
**Outline section(s):** I.A (the models behind the tools), III.A (Accuracy, introduced)
**Rigor step:** A literacy course says AI can be wrong. This chapter asks for the mechanism in plain terms (training data, tokens, context, randomness) and a fact-check against a source file. No attention or embedding math.

**Content:**

* Training data, patterns, and prediction: a language model in plain terms
* Tokens, context windows, and why the model forgets
* Why the same prompt gives different answers
* Hallucination: confident, fluent, and wrong
* The verify habit: claims, numbers, names, and citations you check before you trust
* Knowledge cutoffs and sycophancy: why "are you sure?" is not a check
* Image and multimodal models at a glance

**Prior-course parallel:** gap.
**Prerequisite bridge:** builds only on Chapter 1.

### Chapter 3: Research, Creative Work, and Responsible Use

**Subtitle:** USE AI for research and creative work without losing your judgment or your integrity
**Outcome(s):** CLO 1, CLO 5
**Outline section(s):** I.C (Research), I.D (Creative applications), I.E (Human vs. AI content), I.F (Ethical use principles)
**Rigor step:** A literacy course discusses responsible use. This chapter asks for a research brief with checked sources, a creative asset, a disclosure statement, and a privacy check.

**Content:**

* AI as a research partner: summarizing, brainstorming, and finding leads, then checking them against real sources
* Creative applications: text, images, audio, and video, and where each helps
* Human versus AI content: signals, detectors and their failure rates, disclosure
* Ethical use principles: honesty, attribution, consent, privacy, and harm
* Academic integrity and the college's AI expectations (course-layer policy stays in callouts)
* Content ownership questions introduced, deepened in Chapter 8

**Prior-course parallel:** gap.
**Prerequisite bridge:** builds on Chapters 1-2.

**Part I milestone:** students can tell the major types of AI apart,
explain why a generative model invents things, hold a productive
conversation with a chat assistant, and check what it tells them.

---

## Part II: Prompt Engineering (Chapters 4-6)

**Theme:** get better output by asking better, then refining
**Learning arc:** Build the prompt -> Apply the strategies -> Refine in loops
**Outcome alignment:** CLO 3 (primary), CLO 1 (applied)
**Bloom's focus:** Apply and Analyze, with Evaluate entering in Chapter 6

### Chapter 4: Prompt Basics and Prompt Types

**Subtitle:** BUILD prompts from role, task, context, format, and constraints
**Outcome(s):** CLO 3
**Outline section(s):** II.A (Prompt basics), II.B (Prompt types)
**Rigor step:** A literacy course types a question. This chapter asks for prompts built from named parts and read back against the prompt.

**Content:**

* What a prompt is and what the model does with it
* The five parts of a prompt: role, task, context, format, constraints
* Prompt types: instruction, question, completion, role play, and example-led (few-shot)
* Zero-shot versus few-shot prompting
* Custom instructions and system-style prompts (tool-specific steps in callouts)
* Reading output against the prompt: did it do what you asked?

**Prior-course parallel:** gap.
**Prerequisite bridge:** builds on Chapters 1-2 (the first conversation, the verify habit).

### Chapter 5: Strategies That Make Prompts Work

**Subtitle:** APPLY the strategies that raise output quality: specificity, examples, structure, and step-by-step reasoning
**Outcome(s):** CLO 3, CLO 1
**Outline section(s):** II.C (Effectiveness strategies)
**Rigor step:** A literacy course knows tips exist. This chapter asks students to apply named strategies and measure the difference with a checklist.

**Content:**

* Specificity and context: the more the model knows, the less it invents
* Examples: show, do not only tell
* Output structure: tables, lists, templates, and word limits
* Step-by-step reasoning requests and task decomposition
* Personas and audience framing
* Grounding: supply the source text and ask the model to answer only from it
* Having the model ask clarifying questions before it answers
* Negative constraints and guardrails
* Judging the result against a checklist (CLO 1 applied)

**Prior-course parallel:** gap.
**Prerequisite bridge:** builds on Chapter 4.

### Chapter 6: Iterative Refinement

**Subtitle:** REFINE prompts in loops: test, compare, revise, and record what worked
**Outcome(s):** CLO 3, CLO 1
**Outline section(s):** II.D (Iterative refinement)
**Rigor step:** A literacy course tries again. This chapter asks for criteria written before the first run, versioned prompts, and a log a colleague can reuse.

**Content:**

* Why first drafts fail: the refinement loop
* Writing evaluation criteria before the first run
* Follow-up prompts: narrow, expand, correct, restyle
* Comparing one prompt across two tools
* Prompt templates and a personal prompt library
* Versioning prompts in the prompt log
* Documenting prompts so a colleague can reuse them
* Knowing when to stop: good enough versus perfect

**Prior-course parallel:** gap.
**Prerequisite bridge:** builds on Chapters 4-5.

**Part II milestone:** students build a prompt from its parts, raise
its output quality with named strategies, refine it across iterations,
and keep a documented prompt library.

---

## Part III: AI Regulation and Ethics (Chapters 7-9)

**Theme:** judge AI output and AI use against standards of accuracy, fairness, law, and business value
**Learning arc:** Test accuracy and bias -> Read the rules -> Weigh the impact
**Outcome alignment:** CLO 1, CLO 4, CLO 5 (primary), CLO 6 (introduced)
**Bloom's focus:** Analyze and Evaluate

### Chapter 7: Accuracy and Bias

**Subtitle:** EVALUATE AI output for accuracy and detect bias with a repeatable method
**Outcome(s):** CLO 1, CLO 5
**Outline section(s):** III.A (Accuracy), III.B (Bias)
**Rigor step:** A literacy course worries about bias. This chapter asks for an audit with a method (claims extracted, paired prompts, findings reported in counts). No computed precision or recall.

**Content:**

* An accuracy audit: extract the claims, check each against a source, score the output
* Where errors come from: training data, prompt ambiguity, reasoning gaps, dated knowledge
* Bias: where it enters (data, labels, design, use) and how it shows up in output
* Testing for bias: paired prompts and counterfactual checks
* Fairness as a decision, not a setting
* Reporting findings so a colleague can act on them

**Prior-course parallel:** gap.
**Prerequisite bridge:** builds on Chapter 2 (the verify habit) and Chapter 5 (the checklist).

### Chapter 8: Governance, Privacy, and Content Ownership

**Subtitle:** ANALYZE the rules that govern AI use: laws, frameworks, privacy, and who owns what
**Outcome(s):** CLO 5, CLO 4
**Outline section(s):** III.C (Global governance)
**Rigor step:** A literacy course mentions laws. This chapter asks students to read primary documents (the NIST AI RMF, the EU AI Act tiers, a vendor data policy) and write a policy others can follow.

**Content:**

* Law, policy, guidance, and ethics: four different things
* Global governance: the EU AI Act's risk tiers, the NIST AI Risk Management Framework, the OECD AI Principles, state laws, and sector rules (each dated and sourced, rubric gate G1)
* Privacy: what you enter, what the vendor keeps, and what to never share
* FERPA and HIPAA touchpoints for students and small organizations
* Content ownership: copyright, training data, AI-generated work, and the United States Copyright Office guidance
* Reading a vendor's terms of use and data policy
* Workplace and classroom AI policies, and writing one for an organization

**Prior-course parallel:** gap.
**Prerequisite bridge:** builds on Chapter 3 (ethical use principles).

### Chapter 9: AI in Business and Society

**Subtitle:** ANALYZE the current state of AI, its strengths and weaknesses, and its impact on work
**Outcome(s):** CLO 4, CLO 5, CLO 6
**Outline section(s):** III.D (Business evaluation), III.E (Tech trends)
**Rigor step:** A literacy course repeats trends. This chapter asks for a sourced evaluation of a business use with costs, risks, and workforce impact, and a judgment on one current claim.

**Content:**

* Where AI is strong, where it is weak, and why the gap matters
* Business evaluation: cost, time saved, error cost, risk, and workforce impact
* A simple framework for evaluating a proposed AI use
* Case studies of adoption that worked and adoption that failed
* Tech trends to watch: agents, multimodal models, on-device AI (refreshable callouts)
* Society: jobs, education, misinformation, access, and energy
* Pointing ahead to CIS144 (agentic AI, analytics) and CIS218 (integration, deployment)

**Prior-course parallel:** gap.
**Prerequisite bridge:** builds on Chapters 7-8.

**Part III milestone:** students audit an AI output for accuracy and
bias, place an AI use under the right law or framework, and evaluate a
proposed business use with costs, risks, and workforce impact named.

---

## Part IV: Selecting and Applying AI Tools (Chapters 10-12)

**Theme:** pick the right tool for the problem, apply it, and show your work
**Learning arc:** Survey the platforms -> Match tools to scenarios -> Deliver and reflect
**Outcome alignment:** CLO 6 (primary), CLO 1, CLO 3, CLO 4, CLO 5 (synthesized)
**Bloom's focus:** Evaluate and Create

### Chapter 10: Surveying and Comparing AI Platforms

**Subtitle:** COMPARE AI platforms with criteria that matter: capability, cost, privacy, and fit
**Outcome(s):** CLO 6, CLO 2
**Outline section(s):** IV.A (Platform survey), IV.B (Tool comparison)
**Rigor step:** A literacy course lists tools. This chapter asks for a comparison matrix built from the same test across platforms, with stated criteria.

**Content:**

* The platform landscape by type: general assistants, research tools, image and media tools, AI inside office suites, and specialized tools
* Comparison criteria: capability, accuracy on your task, cost, privacy and data policy, accessibility, integration
* Building a comparison matrix
* Running the same task across platforms and scoring the results
* Keeping a survey current when tools change monthly
* Free tiers, paid tiers, and enterprise versions (refreshable callouts)

**Prior-course parallel:** gap.
**Prerequisite bridge:** builds on Chapter 1 (the landscape) and Chapter 7 (scoring output).

### Chapter 11: Matching AI Tools to Scenarios

**Subtitle:** SELECT and apply the right AI solution for a specific problem, then defend the choice
**Outcome(s):** CLO 6, CLO 3, CLO 1
**Outline section(s):** IV.C (Scenario alignment), IV.D (Practical assignments)
**Rigor step:** A literacy course picks the familiar tool. This chapter asks for the problem defined first, a matched tool, a measured pilot, and a recommendation memo, including when the answer is no AI.

**Content:**

* From problem to requirements: what the scenario needs
* Scenario alignment: matching needs to tool strengths
* Practical assignments: email triage, meeting summary, marketing draft, data question, flyer image
* When the answer is "no AI here"
* Piloting and measuring a choice before committing to it
* Prompt plus tool plus verification: the complete workflow
* Writing a recommendation memo

**Prior-course parallel:** gap.
**Prerequisite bridge:** builds on Chapters 4-6 and 10.

### Chapter 12: The AI Application Project

**Subtitle:** CREATE an AI solution for a scenario, present it, and reflect on the ethics
**Outcome(s):** CLO 1, CLO 3, CLO 4, CLO 5, CLO 6
**Outline section(s):** V.A (Real-world scenario solution), V.B (Project presentation), V.C (Reflection and ethics)
**Rigor step:** A literacy course writes a reflection. This chapter asks for a delivered solution with a verification trail, a stakeholder presentation, and an ethics statement.

**Content:**

* Choosing a scenario and defining success: the Copperwind capstone option or the student's own organization
* Building the solution: tools, prompts, verification, and documentation
* Presenting the work: audience, evidence, and honesty about limits
* Reflection: what AI did well, what it got wrong, what you would do differently
* The ethics statement: privacy, ownership, bias, and disclosure
* Course conclusion: where CIS144 and CIS218 take you next

**Prior-course parallel:** gap.
**Prerequisite bridge:** synthesizes the entire book.

**Part IV milestone:** students compare platforms with explicit
criteria, select and apply a tool for a scenario, and deliver a
documented AI solution with a presentation and an ethics reflection.

---

## Schedule-Neutral Course Mapping

The four Parts define the skill sequence, not a calendar. An instructor
can assign one or more chapters per instructional unit and place the
Chapter 12 project where it fits the section. The same chapter files
support 9-, 12-, 14-, and 16-week courses. Course dates, exams,
submission windows, tool account deadlines, and project pacing belong
in instructor materials.

**Assessment structure:**

* Skills Labs (chapter deliverables): [weight]%
* Module quizzes: [weight]%
* AI application project (Chapter 12): [weight]%
* Weights live in the Canvas build. Confirm before syllabus
  publication.

---

## Outcome Coverage Matrix

| Outcome | Primary chapters | Supporting chapters | Coverage assessment |
| ------- | ---------------- | ------------------- | ------------------- |
| 1. Evaluate AI-generated responses for accuracy | Ch 2, Ch 7 | Ch 3, Ch 5, Ch 6, Ch 11, Ch 12 | Strong: begun in Part I, made rigorous in Ch 7, applied in every later lab |
| 2. Differentiate the major types of AI | Ch 1 | Ch 2, Ch 10 | Strong: dedicated opening chapter, revisited when platforms are surveyed |
| 3. Demonstrate effective prompting strategies | Ch 4, Ch 5, Ch 6 | Ch 11, Ch 12 | Strong: a three-chapter arc, then applied |
| 4. Analyze the current state of AI and its impact | Ch 9 | Ch 1, Ch 8, Ch 12 | Adequate: one primary chapter. Keep Ch 9's lab evidence-based, not opinion-based |
| 5. Apply ethical guidelines | Ch 3, Ch 8 | Ch 7, Ch 9, Ch 12 | Strong: introduced early, formalized in Part III, assessed in the project |
| 6. Select appropriate AI solutions | Ch 10, Ch 11 | Ch 9, Ch 12 | Strong: two dedicated chapters plus the project |

---

## District Outline Coverage Map

| MCCCD outline section | Chapter(s) |
| --------------------- | ---------- |
| I.A AI tools overview | Ch 1 (primary), Ch 2 (the models behind the tools), Ch 10 (survey) |
| I.B Milestones | Ch 1 |
| I.C Research | Ch 3 |
| I.D Creative applications | Ch 3 |
| I.E Human vs. AI content | Ch 3 |
| I.F Ethical use principles | Ch 3 (primary), Ch 8 (formalized) |
| II.A Prompt basics | Ch 4 |
| II.B Prompt types | Ch 4 |
| II.C Effectiveness strategies | Ch 5 |
| II.D Iterative refinement | Ch 6 |
| III.A Accuracy | Ch 7 (primary), Ch 2 (introduced) |
| III.B Bias | Ch 7 |
| III.C Global governance | Ch 8 |
| III.D Business evaluation | Ch 9 |
| III.E Tech trends | Ch 9 |
| IV.A Platform survey | Ch 10 |
| IV.B Tool comparison | Ch 10 |
| IV.C Scenario alignment | Ch 11 |
| IV.D Practical assignments | Ch 11 (primary), every Skills Lab |
| V.A Real-world scenario solution | Ch 12 |
| V.B Project presentation | Ch 12 |
| V.C Reflection and ethics | Ch 12 |

---

## Cross-Chapter Dependencies

**Strict prerequisites:**

* Chapter 2 requires Chapter 1 (the types of AI and the first conversation)
* Chapters 4-6 run in sequence (parts of a prompt, then strategies, then refinement)
* Chapter 7 requires Chapter 2 (the verify habit) and Chapter 5 (the output checklist)
* Chapter 8 requires Chapter 3 (ethical use principles)
* Chapter 10 requires Chapter 1 (the tool landscape) and Chapter 7 (scoring output)
* Chapter 11 requires Chapters 4-6 and Chapter 10
* Chapter 12 synthesizes the book

**Knowledge assumed across all chapters:**

* None from prior courses. The course has no prerequisite.
* Basic computer literacy (a browser, a text editor, saving files) is
  suggested by MCCCD but not required. Chapter 1 walks through
  account creation and saving a transcript, then assumes both.

---

## The Resumable Spine (pedagogy upgrade U1)

**Proposed organization:** Copperwind IT Services, the fictional
managed IT services provider in Phoenix that already threads CIS215,
CIS133, and CIS376 (canonical facts in those books' pedagogy specs:
about 30 employees, Deskside and Network Ops teams, eight named
technicians, roughly 40 client companies). CIS137 enters the same
universe from a new angle: **Copperwind is deciding how to use
generative AI across its teams, and it has hired you as its AI
adoption assistant.** Each chapter gives you one task in that effort:
classify the AI the company already uses, draft and verify support
replies, write the prompt library, audit a vendor's output, read the
tools' data policies, compare platforms for the help desk, and present
a recommendation. Each chapter ships its own starter file, so no
chapter depends on another chapter's saved work.

HQ Decision D13 "The resumable spine" was ruled on 2026-10-21:
Copperwind IT Services, because a managed services provider fits the
bachelor's-pathway IT audience. Option B (Kestrel Row Books, a
fictional bookstore) stays in git history at 6401a24 for the record.

### Per-chapter upgrade placement

Playbook Phase 2 asks for this plan before any chapter is written. The
Fix It column names a candidate theme. The real bug and its real
captured output are produced when the chapter is written, never
invented.

| Ch | Spine block (U1) | Fading (U2) | Fix It candidate (U4) | Reach-backs (U3) |
| -- | ---------------- | ----------- | --------------------- | ---------------- |
| 1 | Sort the AI Copperwind already runs (TIY 1.5, Lab Part 3) | full | a vague prompt that asks for everything | none |
| 2 | Fact-check an AI summary of a Copperwind client update against the source file | full | a confident response with an invented citation | Ch 1 |
| 3 | A research brief and one image for Priya Sharma's outreach newsletter, with disclosure | full | a summary that drops the one caveat its source carried | Ch 1 |
| 4 | A first prompt library for the Deskside reply inbox | full | a question where an instruction was needed (an explanation instead of a draft) | Ch 2, Ch 1 |
| 5 | Repair three weak Copperwind marketing prompts with a checklist | completion | a missing format constraint (the right content in the wrong shape) | Ch 3, Ch 1 |
| 6 | Refine the outreach newsletter prompt across versions with a log | completion | a revision that changed two things at once | Ch 4, Ch 2 |
| 7 | Audit AI responses about Copperwind hiring and marketing for accuracy and bias | completion | a paired-prompt bias test that varied two details | Ch 5, Ch 3 |
| 8 | Draft the Copperwind AI use policy from the tools' data policies | completion | a policy prompt that cites a law that does not exist | Ch 6, Ch 4 |
| 9 | An evidence-based memo: should the help desk adopt an AI assistant? | problem-first | a trend claim with no source behind it | Ch 7, Ch 5 |
| 10 | A platform comparison matrix for three help desk tasks | problem-first | an unfair comparison (a different prompt per tool) | Ch 8, Ch 6 |
| 11 | Three Copperwind scenarios solved with the matched tool, each justified | problem-first | a tool chosen before the problem was defined | Ch 9, Ch 7 |
| 12 | The Copperwind capstone option: a recommendation presented to Mei Lin | problem-first | a presentation claim the prompt log cannot support | Ch 10, Ch 8 |

Subgoal labels (U5) go on the two most complex prompts in every
chapter, chosen at writing time.

---

## Prerequisite-to-CIS137 Bridge Map

Not applicable. CIS137 has no prerequisite course. Every chapter builds
only on earlier chapters of this book. CIS144 lists CIS137 (or AIM100)
as its prerequisite, so this book is the bridge map for CIS144, not the
other way around.
