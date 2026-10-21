# CIS137 Tool Roster (proposal, awaiting Mr. Vega's ruling)

**Status:** PROPOSED 2026-10-21, revised the same day with district
facts. HQ Decision D10 "Tool roster." Nothing in an MLO, a competency,
or a glossary definition depends on this file. Chapter callouts
(`!!! note "Tool check"`) name tools from this roster and carry the
month they were last verified.

MCCCD's course note is the only hard requirement: "CIS137 will require
students to create accounts to multiple generative AI tools." The
book's labs are written so that any two tools from the core set work.

## Why a roster at all

Tool names date faster than the competencies. The roster lives here,
in one file, so a future edit can swap a tool without touching a
chapter's lesson. Every chapter callout that names a tool points back
here.

## District facts (reported, not yet verified by this build)

A parallel session's web search on 2026-10-21 reported the following.
Verify each against the named page before the roster is final. None of
it is quoted in a chapter.

* help.maricopa.edu (SCC knowledge base article 139, about a year old)
  says all currently enrolled students get Microsoft 365 Copilot by
  signing in at m365.cloud.microsoft/apps with MEID@maricopa.edu.
  Paradise Valley's AI Tools page points students to
  copilot.microsoft.com with MEID credentials.
* A CGCC CTLA page (undated) says District ITS enabled Gemini,
  NotebookLM, and Workspace Studio for faculty and staff only, not yet
  for students, with guidelines in development with the AI Resource
  Center (ai.maricopa.edu).
* MCLI publishes faculty guidance on generative AI and academic
  misconduct.
* Age rules from secondary guides: ChatGPT 13+ with guardian
  permission under 18 (plus a teen mode), Gemini 13+ on a personal
  account, Copilot 13+, Claude 18+ with no consent route, Perplexity
  13+ with a parent accepting the terms. Verify against each vendor's
  current terms.

## Proposed core set (students create accounts on at least two)

| Tool | Vendor | Why it is on the list | Verify before the first offering |
| ---- | ------ | --------------------- | -------------------------------- |
| Microsoft 365 Copilot (through the student's MEID) | Microsoft | If the district fact holds, every enrolled student already has it, with district data protections and no personal account to create. It is also the AI most students will find inside Windows and Office at work. | The help.maricopa.edu claim, what the district license includes, which "Copilot" the callout means |
| ChatGPT | OpenAI | The most widely used chat assistant, so students will meet it at work. Free tier. A personal account. | Free-tier limits, minimum age and consent rule, data-training opt-out location |
| Gemini | Google | Students already hold Maricopa Google accounts, and the district may enable it for students later. Until then a personal Google account. Free tier. | Whether District ITS has enabled Gemini for student accounts, the age rule for personal accounts |

Three vendors give the comparison chapters (10 and 11) something to
compare. Two accounts are enough for every lab, and the district
Copilot login means a student under 18 or without a personal account
can still complete every lab.

## Proposed supporting set (optional, named in callouts where useful)

| Tool | Vendor | Role in the book |
| ---- | ------ | ---------------- |
| Claude | Anthropic | A fourth chat assistant for the comparison labs (18+ per the reported terms, so never required) |
| Perplexity | Perplexity AI | A research tool that cites sources, used in Chapter 3 (research) and Chapter 7 (accuracy audits) |
| NotebookLM | Google | A source-grounded research tool: students load their own documents and ask questions of them (faculty-only in the district as reported, so a personal account until that changes) |
| One image generator | Microsoft Designer, Adobe Firefly, or the image feature inside a core assistant | Chapter 3 (creative applications) and Chapter 11 (a flyer image). Pick one with a free tier and a clear training-data policy |

## Policies the roster has to respect

* **Age.** Community college sections may include dual-enrollment
  students under 18. Every lab must work with a tool that admits
  students aged 13 and up with consent, or the course layer must
  provide an alternative. The district Copilot login is that
  alternative if the reported fact holds.
* **Data.** Chapter 1 teaches the rule before the first prompt: never
  enter a password, a student ID, a Social Security number, a
  classmate's personal information, or an employer's confidential
  data into a tool. Chapter 8 teaches students to read the vendor's
  data policy and find the training opt-out.
* **District guidance.** Confirm the AI Resource Center's current
  guidance (ai.maricopa.edu) and the MCLI academic-misconduct guidance
  before the roster is final, and link the course layer to them.
* **Cost.** Every tool on the roster has a free tier or a district
  license as of this writing. No lab requires a paid plan.
* **Accessibility.** Each core tool is a web app that works with a
  keyboard and a screen reader. Re-check before the first offering.

## Callout template (copy into chapters)

```text
!!! note "Tool check (verified October 2026)"
    This exercise works in any chat assistant from the course roster.
    Your syllabus names the current roster. The steps below show one
    tool. Menu names change, so if yours looks different, look for the
    same action under a nearby label.
```
