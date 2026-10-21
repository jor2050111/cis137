# CIS137 Textbook: 12-Chapter Structure (Proposed, awaiting approval)

**Course:** CIS137: Artificial Intelligence Fundamentals
**Structure:** 12 chapters organized into 4 thematic Parts
**Pacing:** Schedule-neutral. Instructors may use the book in 8-, 12-,
14-, or 16-week courses without changing chapter content.
**Prerequisite:** None. Chapters teach from zero.
**Status:** Proposed 2026-10-21 (HQ Decision 3). Becomes authoritative
when Mr. Vega approves it. Edit this file, then `zensical.toml`,
`docs/CIS137_CLOs.md`, and `book/index.md` together.
**Last revised:** 2026-10-21

This document is the single plan for chapter order, scope, and outcome
coverage.

---

## Design Rationale

This plan synthesizes three sources:

1. **The official competencies and course outline**
   (docs/CIS137_CLOs.md): every competency and every outline section
   maps to a chapter.
2. **The certificate context** (docs/mcccd/index.html): CIS137 is the
   first course of the Foundations of Applied AI CCL, so the book
   builds the habits CIS144 and CIS218 reuse (judging output,
   prompting, ethics, choosing tools, the project pattern) and stops
   short of agents, analytics, and deployment.
3. **The textbook family structure:** 12 chapters in 4 Parts, the
   pattern proven by CIS133 and CIS215, with the five pedagogy upgrades
   built in from chapter 1.

**Key design decisions:**

* The four Parts follow the first four outline sections in the
  district's order. The fifth section (the final project) becomes
  Chapter 12 inside Part IV, so the project sits beside the tool
  selection skills it exercises.
* Outline section I carries six topics across three chapters. Chapter
  1 takes the tools overview and the milestones (and gets students
  into the tools on day one). Chapter 2 is new coverage the outline
  implies but does not name: how generative models produce output and
  where they fail. Competency 1 (evaluate accuracy) is attached to
  every outline section, so the book teaches the failure modes before
  the prompting Part. Chapter 3 takes research, creative applications,
  human vs. AI content, and the ethical use principles.
* Prompt engineering gets three chapters, one per pair of outline
  topics, because competency 3 is the hands-on core of the course and
  the base for CIS218's advanced prompt engineering.
* Privacy and content ownership come from the official description,
  not the outline. They join global governance in Chapter 8 so the
  regulatory material sits in one place.
* Chapter 12 is primary for no CLO and supports all six. It exists to
  run the project pattern (scenario, solution, presentation,
  reflection) that all three certificate courses end with.
* Tool names and vendor features live in refreshable callouts, never
  in MLOs, CLO blocks, or glossary definitions. The tool roster is HQ
  Decision 1.

**Bloom's rule for every MLO (course-configured, mirrors CLAUDE.md):**
the MLO band is Apply through Evaluate, matching the district verbs.
Early chapters lean on Apply and Analyze. Evaluate enters in Chapter 2
(judging output) and dominates Parts III and IV. Remember and
Understand appear only as steps inside a chapter. Every MLO uses a
measurable action verb. Never write "understand," "know," or "learn"
as the verb.

**Pedagogy upgrades (built in from chapter 1):** one spine block per
chapter (U1), fading across thirds (U2: chapters 1-4 fully worked,
chapters 5-8 one completion prompt each, chapters 9-12 one
problem-first prompt each), cumulative retrieval from chapter 2 (U3),
one Fix It per chapter with a real captured bad output (U4), and
subgoal-labeled flagship prompts (U5). The spine organization is HQ
Decision 4. This plan names it Kestrel Row Books, the recommendation.

---

## Part I: Foundations of AI and Generative Tools (Chapters 1-3)

**Theme:** what AI is, how generative tools behave, and how to use them well from day one
**Learning arc:** Differentiate the kinds of AI -> Explain how generative models work and fail -> Apply responsible-use principles to research and creative work
**Outcome alignment:** CLO II, CLO I (begun), CLO V (begun), CLO IV (introduced)
**Bloom's focus:** Apply and Analyze, with Evaluate entering in Chapter 2

### Chapter 1: What Artificial Intelligence Is

**Subtitle:** DIFFERENTIATE the major types of AI and open your first tools
**Outcome(s):** CLO II (primary), CLO IV (supporting)
**Outline section(s):** I.A (AI tools overview), I.B (Milestones)

**Content:**

* What counts as AI: rule-based systems, machine learning, deep
  learning, and generative AI, with one plain example of each
* Narrow AI vs. the general AI of fiction, and predictive vs.
  generative systems
* Milestones that explain today's tools: the Turing test (1950), the
  Dartmouth workshop (1956), expert systems, Deep Blue (1997), the
  ImageNet moment (2012), transformers (2017), public chat assistants
  (2022)
* The tool landscape: chat assistants, research tools, image
  generators, and the assistants built into office suites (roster in
  a refreshable callout)
* Creating accounts safely and reading a tool's data settings
* The lab-log habit: recording every prompt, the tool, the date, and
  the response, which every later Skills Lab depends on
* Spine block: meet Kestrel Row Books and run its first three prompts

**Prior-course parallel:** gap. CIS137 has no previous Phoenix College
build. The chapter is new coverage.
**Prerequisite bridge:** new content. The course has no prerequisite.

### Chapter 2: How Generative AI Works and Where It Fails

**Subtitle:** EXPLAIN how a language model produces text and EVALUATE where it goes wrong
**Outcome(s):** CLO I (primary), CLO II (supporting)
**Outline section(s):** I (models, from the course description), I.E (Human vs. AI content, begun)

**Content:**

* Training data, tokens, and next-word prediction in plain language
* Why the same prompt gives different answers: randomness, context
  window, and conversation memory
* Hallucination: invented facts, quotes, citations, and numbers, and
  why the model sounds confident either way
* Knowledge cutoffs, sycophancy, and the limits of "ask it if it is
  sure"
* The verification habit: find the source, check the source, compare
  two tools
* Image models in brief: what they learn from and what they get wrong
* Spine block: fact-check an AI-written summary of a Kestrel Row
  author event against the provided source file

**Prior-course parallel:** gap. New coverage.
**Prerequisite bridge:** builds on Chapter 1 (the tools and the lab
log).

### Chapter 3: Research, Creative Work, and Responsible Use

**Subtitle:** APPLY responsible-use principles to research and creative tasks
**Outcome(s):** CLO V (primary), CLO I (supporting), CLO IV (supporting)
**Outline section(s):** I.C (Research), I.D (Creative applications), I.E (Human vs. AI content), I.F (Ethical use principles)

**Content:**

* AI as a research assistant: summaries, outlines, question
  generation, and research tools that cite sources
* Search engines vs. chat assistants vs. research tools, and when each
  fits
* Creative applications: drafting, brainstorming, images, and audio,
  with what each one is good and bad at
* Human vs. AI content: why detectors fail, how disclosure and
  labeling work, and what the course expects
* Ethical use principles: honesty and disclosure, responsibility for
  accuracy, privacy (what never goes into a prompt), attribution, and
  the human-in-the-loop rule
* Academic integrity and the college policy (callout, refreshable)
* Spine block: a research brief and one creative asset for Kestrel
  Row, each with a disclosure statement

**Prior-course parallel:** gap. New coverage.
**Prerequisite bridge:** builds on Chapters 1-2.

**Part I milestone:** students run the course tools with a lab log,
explain where a generated answer can go wrong, verify one, and attach
a disclosure statement to AI-assisted work.

---

## Part II: Prompt Engineering (Chapters 4-6)

**Theme:** get better output by designing, strengthening, and refining prompts
**Learning arc:** Build prompts from their core parts -> Apply strategies that raise quality -> Refine prompts through evaluate-and-revise cycles
**Outcome alignment:** CLO III (primary), CLO I (applied)
**Bloom's focus:** Apply and Analyze

### Chapter 4: Prompt Basics and Prompt Types

**Subtitle:** BUILD clear prompts from their core parts and choose the right type
**Outcome(s):** CLO III (primary), CLO I (supporting)
**Outline section(s):** II.A (Prompt basics), II.B (Prompt types)

**Content:**

* The anatomy of a prompt: task, context, input, output format, and
  constraints
* Specificity: why "write a post" and "write a 120-word post for
  first-time customers" get different results
* Prompt types matched to jobs: instruction, question, role,
  example-driven, and conversational follow-up
* Custom instructions and the difference between a standing
  instruction and a one-time prompt
* Common task patterns: summarize, extract, classify, draft,
  transform, brainstorm
* Spine block: a first prompt library for Kestrel Row's customer
  service inbox

**Prior-course parallel:** gap. New coverage.
**Prerequisite bridge:** builds on Chapters 1-3 (the lab log and the
verification habit).

### Chapter 5: Strategies That Make Prompts Work

**Subtitle:** APPLY proven strategies to raise output quality
**Outcome(s):** CLO III (primary), CLO I (supporting)
**Outline section(s):** II.C (Effectiveness strategies)

**Content:**

* Role and audience framing
* Examples in the prompt (few-shot) and when they help
* Asking for steps, reasons, or a plan before the answer
* Constraints and output formats: tables, lists, word limits, tone
* Grounding: supplying the source text and asking the model to answer
  only from it
* Decomposition: splitting a big task into prompts that build
* Having the model ask clarifying questions first
* Spine block (first faded block, completion prompt): repair three
  weak Kestrel Row marketing prompts and measure the difference with a
  checklist

**Prior-course parallel:** gap. New coverage.
**Prerequisite bridge:** builds on Chapter 4.

### Chapter 6: Iterative Refinement

**Subtitle:** REFINE prompts through evaluate-and-revise cycles
**Outcome(s):** CLO III (primary), CLO I (primary in the lab)
**Outline section(s):** II.D (Iterative refinement)

**Content:**

* The refinement loop: run, evaluate against criteria, diagnose,
  revise
* Writing evaluation criteria before the first run
* Versioning prompts and keeping a prompt log
* Comparing the same prompt across two tools
* When to refine and when to start over
* Defining "good enough" and stopping
* Spine block (completion prompt): refine the Kestrel Row newsletter
  prompt across at least three versions with a log and a final
  evaluation

**Prior-course parallel:** gap. New coverage.
**Prerequisite bridge:** builds on Chapters 4-5.

**Part II milestone:** students write a prompt with all five parts,
strengthen it with named strategies, and refine it across versions
with written criteria and a log.

---

## Part III: AI Regulation and Ethics (Chapters 7-9)

**Theme:** judge AI output and AI systems with evidence, rules, and ethical frameworks
**Learning arc:** Evaluate accuracy and bias -> Analyze governance, privacy, and ownership -> Analyze AI's place in business and society
**Outcome alignment:** CLO I, CLO IV, CLO V (primary), CLO II (supporting)
**Bloom's focus:** Analyze and Evaluate

### Chapter 7: Accuracy and Bias

**Subtitle:** EVALUATE AI output for accuracy and bias with a repeatable method
**Outcome(s):** CLO I (primary), CLO V (supporting), CLO IV (supporting)
**Outline section(s):** III.A (Accuracy), III.B (Bias)

**Content:**

* Kinds of error: factual, reasoning, omission, fabricated sources,
  and stale information
* Confidence is not correctness: reading tone vs. reading evidence
* Verification methods: triangulation, primary sources, calculators,
  and asking for the source then checking it
* Where bias comes from: training data, labeling, and the prompt
  itself
* Testing for bias with controlled prompts (change one detail, compare
  the outputs)
* Fairness in plain terms and documenting an evaluation
* Spine block: audit a provided set of AI responses about Kestrel Row
  hiring and marketing for accuracy and bias

**Prior-course parallel:** gap. New coverage.
**Prerequisite bridge:** builds on Chapter 2 (failure modes) and
Chapter 6 (evaluation criteria).

### Chapter 8: Governance, Privacy, and Content Ownership

**Subtitle:** ANALYZE the rules that govern AI use, personal data, and ownership
**Outcome(s):** CLO V (primary), CLO IV (supporting)
**Outline section(s):** III.C (Global governance), plus the course description's privacy and content ownership concerns

**Content:**

* The governance landscape: the EU AI Act's risk tiers, United States
  federal actions and state laws, the NIST AI Risk Management
  Framework, and the OECD AI Principles (each dated and sourced,
  rubric gate G1)
* Law vs. policy vs. guidance, and why the difference matters
* Privacy: what tools do with what you paste, data-protection
  settings, and personal information that never belongs in a prompt
* FERPA and HIPAA touchpoints for students and small organizations
* Content ownership: copyright and AI-generated work, the United
  States Copyright Office guidance, and tool terms of service
* Writing an organizational AI use policy
* Spine block: draft the Kestrel Row AI use policy (privacy,
  disclosure, ownership) grounded in the named frameworks

**Prior-course parallel:** gap. New coverage.
**Prerequisite bridge:** builds on Chapter 3 (ethical use principles)
and Chapter 7.

### Chapter 9: AI in Business and Society

**Subtitle:** ANALYZE the current state of AI, its strengths and weaknesses, and its impact
**Outcome(s):** CLO IV (primary), CLO II (supporting), CLO V (supporting)
**Outline section(s):** III.D (Business evaluation), III.E (Tech trends)

**Content:**

* Evaluating AI for an organization: cost, value, risk, and workforce
  impact
* Case studies of adoption that worked and adoption that failed
* Society: work, education, misinformation, energy and environment,
  and accessibility gains
* Trends read critically: multimodal models, reasoning models,
  on-device models, and agents (pointed ahead to CIS144, not taught)
* Strengths and weaknesses as a balanced summary, with evidence
* Spine block (first problem-first prompt): an evidence-based memo on
  whether Kestrel Row should adopt an AI customer-service assistant

**Prior-course parallel:** gap. New coverage.
**Prerequisite bridge:** builds on Chapters 1, 7, and 8.

**Part III milestone:** students audit AI output for accuracy and
bias, draft a policy grounded in named frameworks, and write an
evidence-based evaluation of an AI adoption decision.

---

## Part IV: Selecting and Applying AI Tools (Chapters 10-12)

**Theme:** choose the right tool for the problem and prove it with a project
**Learning arc:** Survey and compare platforms -> Match tools to scenarios -> Deliver, present, and reflect on a project
**Outcome alignment:** CLO VI (primary), CLO I, CLO III, CLO V (applied), CLO IV (reflection)
**Bloom's focus:** Evaluate, with Apply and Analyze in service of it

### Chapter 10: Surveying and Comparing AI Platforms

**Subtitle:** COMPARE AI platforms with consistent criteria
**Outcome(s):** CLO VI (primary), CLO II (supporting)
**Outline section(s):** IV.A (Platform survey), IV.B (Tool comparison)

**Content:**

* Platform categories: general chat assistants, research and search
  tools, image and media generators, assistants embedded in office
  suites, and specialized tools
* Comparison criteria: accuracy, sources, privacy and data handling,
  cost and limits, accessibility, and integration
* Running the same test prompt across tools and recording results
* Building a comparison matrix
* Keeping a survey current when tools change monthly
* Spine block (problem-first): a platform comparison matrix for three
  tasks Kestrel Row needs

**Prior-course parallel:** gap. New coverage.
**Prerequisite bridge:** builds on Chapters 1, 6, and 7.

### Chapter 11: Matching AI Tools to Scenarios

**Subtitle:** SELECT the right AI solution for a specific problem and justify it
**Outcome(s):** CLO VI (primary), CLO III, CLO I, CLO V (applied)
**Outline section(s):** IV.C (Scenario alignment), IV.D (Practical assignments)

**Content:**

* A selection method: define the problem, the constraints, and the
  success criteria before touching a tool
* Mapping problem types to tool types
* When not to use AI, and when a human must stay in the loop
* Piloting and measuring a choice
* Practical assignments: short scenarios drawn from marketing,
  finance, operations, and customer experience (the certificate's
  domains)
* Documenting a recommendation a manager can act on
* Spine block (problem-first): solve three Kestrel Row scenarios with
  the matched tool and justify each choice

**Prior-course parallel:** gap. New coverage.
**Prerequisite bridge:** builds on Chapters 4-6 and 10.

### Chapter 12: The AI Application Project

**Subtitle:** DELIVER an AI solution to a scenario, PRESENT it, and REFLECT on its ethics
**Outcome(s):** CLO VI, CLO III, CLO I, CLO V, CLO IV (all supporting, by design)
**Outline section(s):** V.A (Real-world scenario solution), V.B (Project presentation), V.C (Reflection and ethics)

**Content:**

* Choosing a scenario: the Kestrel Row capstone option or the
  student's own organization
* The project plan: problem, tool selection, prompt design, evaluation
  criteria, and ethics review
* Building the deliverable and keeping the evidence (prompt log,
  outputs, verification)
* Presenting the work: structure, demonstration, evidence, limits
* Reflection and ethics: what the tool did well, where it failed, what
  a responsible rollout needs
* Course Conclusion: where CIS144 and CIS218 take these skills
* Spine block: the Kestrel Row capstone option

**Prior-course parallel:** gap. New coverage.
**Prerequisite bridge:** synthesizes the book.

**Part IV milestone:** students compare platforms with consistent
criteria, select and justify a tool for a scenario, and deliver,
present, and reflect on an AI application project.

---

## Schedule-Neutral Course Mapping

The four Parts define the skill sequence, not a calendar. An instructor
can assign one or more chapters per instructional unit and place the
project where it fits the section. The same chapter files support 8-,
12-, 14-, and 16-week courses. Course dates, exams, submission windows,
and project pacing belong in instructor materials.

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
| I. Evaluate responses for accuracy | Ch 2, Ch 7 | Ch 3, Ch 6, Ch 11, Ch 12, every lab | Strong: taught early, practiced in every Skills Lab |
| II. Differentiate the types of AI | Ch 1 | Ch 2, Ch 9, Ch 10 | Adequate: one dedicated chapter, reinforced when platforms are surveyed |
| III. Demonstrate prompting strategies | Ch 4, Ch 5, Ch 6 | Ch 3, Ch 11, Ch 12 | Strong: three-chapter arc, applied through Part IV |
| IV. Analyze the state of AI and its impact | Ch 9 | Ch 1, Ch 7, Ch 8, Ch 12 | Strong: dedicated chapter plus the milestones thread and the project reflection |
| V. Apply ethical guidelines | Ch 3, Ch 8 | Ch 7, Ch 9, Ch 11, Ch 12 | Strong: principles in Part I, frameworks in Part III, applied in the project |
| VI. Select appropriate AI solutions | Ch 10, Ch 11 | Ch 12 | Strong: two-chapter arc that the project exercises |

---

## District Outline Coverage Map

| District outline section | Chapter(s) |
| ------------------------ | ---------- |
| I.A. AI tools overview | Ch 1 |
| I.B. Milestones | Ch 1 |
| I.C. Research | Ch 3 |
| I.D. Creative applications | Ch 3 |
| I.E. Human vs. AI content | Ch 3 (primary), Ch 2 (begun) |
| I.F. Ethical use principles | Ch 3 |
| II.A. Prompt basics | Ch 4 |
| II.B. Prompt types | Ch 4 |
| II.C. Effectiveness strategies | Ch 5 |
| II.D. Iterative refinement | Ch 6 |
| III.A. Accuracy | Ch 7 (primary), Ch 2 (introduced) |
| III.B. Bias | Ch 7 |
| III.C. Global governance | Ch 8 |
| III.D. Business evaluation | Ch 9 |
| III.E. Tech trends | Ch 9 |
| IV.A. Platform survey | Ch 10 |
| IV.B. Tool comparison | Ch 10 |
| IV.C. Scenario alignment | Ch 11 |
| IV.D. Practical assignments | Ch 11 (primary), every Skills Lab |
| V.A. Real-world scenario solution | Ch 12 |
| V.B. Project presentation | Ch 12 |
| V.C. Reflection and ethics | Ch 12 |

---

## Cross-Chapter Dependencies

**Strict prerequisites:**

* Chapter 2 requires Chapter 1 (the tools and the lab log)
* Chapters 4-6 run in sequence (prompt parts, then strategies, then
  refinement)
* Chapter 7 requires Chapter 2 (failure modes) and Chapter 6
  (evaluation criteria)
* Chapter 8 requires Chapter 3 (ethical use principles)
* Chapter 11 requires Chapter 10 (comparison criteria)
* Chapter 12 synthesizes the book

**Knowledge assumed across all chapters:**

* None from prior courses. The course has no prerequisite.
* Basic computer literacy (opening a browser, creating an account,
  saving a file) is walked through in Chapter 1, then assumed.

**Spine independence (pedagogy upgrade U1):** every spine block ships
its own starter file in its own `assets/code/chapter-NN/` folder. A
chapter may call back to an earlier Kestrel Row moment ("you first met
the inbox in Chapter 4"). It never depends on a student's saved work
from an earlier chapter.

---

## The Spine: Kestrel Row Books (recommendation, HQ Decision 4)

A fictional independent bookstore and cafe with two Phoenix-area
stores and an online shop, about thirty staff, and six working groups
that need AI help: marketing, events, customer service, operations,
hiring, and the owner's office. The name returned no collisions in a
web search on 2026-10-21. Every data README carries the fictional
disclaimer. Why a bookstore: it puts accuracy (invented quotes and
ISBNs), content ownership (cover art, author rights), privacy
(customer data), and bias (hiring, recommendations) in one small
organization, and its sales and inventory data give CIS144 and CIS218
a place to continue. Cover stories elsewhere in each chapter stay
varied (a clinic, a youth soccer league, a city department, a student
club) so the spine claims one block per chapter, not the book.

---

## Prerequisite-to-CIS137 Bridge Map

Not applicable. CIS137 has no prerequisite course. Every chapter
builds only on earlier chapters of this book.
