# CIS137 Tool Roster (proposal, awaiting Mr. Vega's ruling)

**Status:** PROPOSED 2026-10-21. HQ Decision "Tool roster." Nothing in
an MLO, a competency, or a glossary definition depends on this file.
Chapter callouts (`!!! note "Tool check"`) name tools from this roster
and carry the month they were last verified.

MCCCD's course note is the only hard requirement: "CIS137 will require
students to create accounts to multiple generative AI tools." The
book's labs are written so that any two tools from the core set work.

## Why a roster at all

Tool names date faster than the competencies. The roster lives here,
in one file, so a future edit can swap a tool without touching a
chapter's lesson. Every chapter callout that names a tool points back
here.

## Proposed core set (students create accounts on at least two)

| Tool | Vendor | Why it is on the list | Verify before the first offering |
| ---- | ------ | --------------------- | -------------------------------- |
| ChatGPT | OpenAI | The most widely used chat assistant, so students will meet it at work. Free tier. | Free-tier limits, minimum age (13 with consent per OpenAI's terms at the time of writing), data-training opt-out location |
| Gemini | Google | Students already hold Maricopa Google accounts. Free tier. A district-managed version may carry stronger data protections. | Whether MCCCD enables Gemini for student Workspace accounts, the age rule for personal versus Education accounts |
| Copilot | Microsoft | Free with a Microsoft account, and the AI most students will find inside Windows and Office at work. | Free-tier limits, age rule, which "Copilot" the callout means (the consumer chat, not the Microsoft 365 add-on) |

Three vendors give the comparison chapters (10 and 11) something to
compare. Two accounts are enough for every lab.

## Proposed supporting set (optional, named in callouts where useful)

| Tool | Vendor | Role in the book |
| ---- | ------ | ---------------- |
| Claude | Anthropic | A fourth chat assistant for the comparison labs (18+ per Anthropic's terms at the time of writing) |
| Perplexity | Perplexity AI | A research tool that cites sources, used in Chapter 3 (research) and Chapter 7 (accuracy audits) |
| NotebookLM | Google | A source-grounded research tool: students load their own documents and ask questions of them |
| One image generator | Adobe Firefly, Microsoft Designer, or the image feature inside a core assistant | Chapter 3 (creative applications) and Chapter 11 (a flyer image). Pick one with a free tier and a clear training-data policy |

## Policies the roster has to respect

* **Age.** Community college sections may include dual-enrollment
  students under 18. Every lab must work with a tool that admits
  students aged 13 and up with consent, or the course layer must
  provide an alternative. Confirm each vendor's current rule before
  the first offering.
* **Data.** Chapter 1 teaches the rule before the first prompt: never
  enter a password, a student ID, a Social Security number, a
  classmate's personal information, or an employer's confidential
  data into a tool. Chapter 8 teaches students to read the vendor's
  data policy and find the training opt-out.
* **District guidance.** This session could not verify whether MCCCD
  publishes an approved-tools list or AI guidance for coursework.
  Mr. Vega should confirm before the roster is final.
* **Cost.** Every tool on the roster has a free tier as of this
  writing. No lab requires a paid plan.
* **Accessibility.** Each core tool is a web app that works with a
  keyboard and a screen reader. Re-check before the first offering.

## Callout template (copy into chapters)

```text
!!! note "Tool check (verified October 2026)"
    This exercise works in any chat assistant from the course roster.
    The steps below show [tool]. Menu names change, so if yours looks
    different, look for the same action under a nearby label.
```
