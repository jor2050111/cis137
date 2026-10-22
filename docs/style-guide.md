# CIS137 Textbook Style Guide

This file holds the course-specific layer only. The canonical shared
writing law lives at `../shared/style-guide-core.md` in the textbooks
workspace. The sync script copies it into this repo as
`docs/style-guide-core.md`. Read the core first. Never edit the synced
copy, and never restate core rules here. When this file and the core
disagree, this file wins for CIS137 only.

## Audience and Tone Calibration

Calibrate the core's tone invariants for community college students in
their first AI course.

* **Assumed background:** no prior experience with AI tools and no
  programming. MCCCD suggests college-level reading (RDG100) and
  writing (ENG101) but does not require them. Basic computer literacy
  (a browser, a text editor, saving a file) is walked through in
  Chapter 1 and assumed afterward. Many students will already have
  used a chat assistant casually. Treat that as a starting point, not
  a skill: the book teaches the judgment they have not practiced.
  Most readers are in Phoenix College's bachelor's pathway in
  information technology (CIS137 is a recommended first elective), so
  cover stories and lab artifacts can assume IT professionals in
  training. The floor still sits at zero. See the Rigor Band section
  of CLAUDE.md and `book/fluency-contract.md`.
* **Register:** collegial and professional. Students are practitioners
  using AI at work and at school now, not people preparing to. Never
  frame a skill as "preparation for the real world." Say
  "industry-relevant" when the point is needed.
* **Reading level:** Flesch Reading Ease 60-70, leaning toward the top
  of the band (settled in the starter prompt, 2026-10-21). AI
  vocabulary is syllable-heavy, so write "AI" after the first full
  mention in a chapter, prefer "model" to "large language model" once
  the term is defined, and keep sentences short.
* **Bridging rule:** the course has no prerequisite. Reference earlier
  chapters by number in one sentence ("Chapter 2 explained why a
  model invents citations") and never reteach them. Callbacks to the
  Copperwind spine are welcome. Dependencies on earlier saved work are
  banned.

## Bloom's-Level Emphasis for CIS137

The shared framework lives in `docs/blooms-taxonomy-reference.md`
(seeded at setup). Record here how this course weights the six levels.

* **Primary levels:** Apply, Analyze, and Evaluate. MCCCD's competency
  verbs are evaluate, differentiate, demonstrate, analyze, apply, and
  select, and every MLO ladders to one of them.
* **Occasional levels:** Create, in the Chapter 12 project and in
  Skills Lab Part 3 extensions that ask for a recommendation memo or a
  prompt library.
* **Avoided levels:** Remember and Understand as MLO levels. They
  undershoot the competencies. They appear as steps inside a chapter
  (a Quick Check that asks for a definition, a Review Question tagged
  Understand) and never as an objective.
* **Distribution across the book:** Parts I and II lean on Apply and
  Analyze. Parts III and IV lean on Analyze and Evaluate. Chapter 12
  reaches Create through an honest task, not a label.

## Conventions for Prompts, Responses, and Tools

Language and tool rules the core delegates to the course guide.

* **Code fence identifiers:** `text` for every prompt, every sample
  response, every transcript excerpt, and every diagram. The book has
  no executable code, so no `python`, `html`, `bash`, or other
  language fence appears in a chapter. The structure checker fails on
  one.
* **Prompt and response layout:** a worked example shows the prompt in
  one `text` fence, then a one-line label ("Sample response (captured
  from a chat assistant, October 2026). Your output will differ:"),
  then the response in a second `text` fence. Trim a long response
  with `[...]` on its own line. Flagship examples carry `[Step k: ...]`
  decision labels inside the prompt fence.
* **Real output only:** every sample response and every Fix It output
  is captured from a real run of a tool on the roster. Record the
  tool, the date, and the full response in
  `docs/execution-logs/chapter-NN-responses.md`. Never invent, edit,
  or "improve" a response. If a response is too long, trim it and mark
  the cut.
* **Naming scheme:** prompts in a log are labeled `Prompt 1`,
  `Prompt 2`, and so on, in the order sent. Starter files use
  kebab-case (`support-reply-brief.txt`). Lab deliverables are named
  `skills-lab-Na-lastname.md`.
* **Version targets:** none. Web-based tools update without version
  numbers. Tool-specific steps live in a `!!! note "Tool check"`
  admonition that names the month it was verified, so a later edit
  can refresh the callout without touching the lesson.
* **Capitalization table:**

| Term | Correct | Incorrect |
| ---- | ------- | --------- |
| artificial intelligence | AI (after first full mention) | A.I., Ai |
| generative AI | generative AI | Generative AI (mid-sentence), GenAI |
| large language model | large language model (LLM) | Large Language Model |
| chat assistant | chat assistant | chatbot (reserve for the pre-LLM era), AI chat |
| prompt engineering | prompt engineering | prompt-engineering, Prompt Engineering |
| hallucination | hallucination | confabulation, "making stuff up" in a definition |
| machine learning | machine learning | Machine Learning, ML (define before using) |
| the EU AI Act | the EU AI Act | the AI Act (first mention), EU AI act |
| NIST AI RMF | NIST AI Risk Management Framework (NIST AI RMF) | NIST framework |
| vendor and product names | the vendor's own capitalization, only inside Tool check callouts and docs/tool-roster.md. Named exception (ruled at the 2026-10-22 evaluation): historical milestones in Chapter 1's milestone table and in a captured sample that lists milestones may name the product as history, because the history needs the names and no claim about the product's quality is made | any vendor name in an MLO, a competency, or a glossary definition |

## Artifact Pack and Example-Domain Conventions

* **Example domains:** the Copperwind IT Services spine (an MSP
  deciding how to adopt generative AI: help desk replies, client
  communication, internal documentation, hiring, and marketing) claims
  one block per chapter. Varied cover stories fill the rest: a family
  clinic's front desk, a charter school's office, a food truck's
  social media, a neighborhood nonprofit, a student's own coursework.
  Scenarios show people with agency, never only as harm recipients.
* **Provided files:** every Skills Lab opens files from
  `assets/code/chapter-NN/` in the course data pack: scenario briefs,
  transcripts to evaluate, source packets, worksheets, and prompt
  logs. Students download one zip from Canvas, extract it, and work at
  the extracted `cis137` root. Each folder has a README that names
  every file, its purpose, its source, and its fictional status.
* **Rules for new starter files:** a transcript file a student is
  asked to evaluate must be a real captured response, logged with its
  tool and date. A source packet must be internally consistent and
  must support more than one defensible position when the task asks
  for judgment. Fictional organizations get a name-collision search
  before use and carry the Copperwind disclaimer in the README.
* **What students never hand-type:** scenario briefs, source packets,
  and transcripts. The exception is the prompt itself: students type
  their own prompts into a tool, because writing the prompt is the
  skill.
* **What the pack never ships:** a response the student is supposed to
  generate. Labs that need AI output have the student produce it live
  in a tool from the roster callout, then paste it into the log.
