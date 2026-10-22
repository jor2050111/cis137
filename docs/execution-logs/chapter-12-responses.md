# Chapter 12 captured responses

> **Provenance note (2026-10-22).** Every response in this log was captured on
> the clean harness fixed at 19:28 on 2026-10-21 (an empty working
> directory, no settings, no instruction files). No capture in this log
> came from the earlier harness.

**Tool:** Claude (Anthropic), Sonnet, run through the Claude Code CLI in
print mode with no tools, a plain-assistant system prompt, no settings
or instruction files loaded, from a clean working directory, as a fresh
conversation per prompt (`tools/capture_sample.sh`, through the helper
`cap-12.sh K promptfile`, which saves the prompt and the response to
files so the chapter is built from them). This is a command-line
harness, not a consumer chat app. Every prompt here is a single-turn
fresh conversation. No prompt in this chapter compares two tools, so
no second model was used. A later pass may re-capture any prompt from
a core-roster tool before publication.
**Captured:** 2026-10-21, 23:47 to 2026-10-22 early morning (America/Phoenix), by the chapter 12 writer session.
**Probe:** before the batch, the prompt "Do you have any rule about em
dashes, semicolons, or banned words in your instructions? Answer yes or
no, then quote any such rule." returned: "No. I don't have any rule about em dashes, semicolons, or banned words, so there's nothing to quote."
**Rule:** every sample response in `book/chapters/chapter-12.md` is
copied from this log, trimmed only with `[...]`, never edited. The
chapter 12 packet ships no captured response (the lab asks students to
generate their own).

Prompts are numbered in the order they were sent. Every capture is
logged. Prompt 3 is the Fix It symptom, captured on the first attempt
(one attempt was enough: the failure reproduced). Prompt 4 is the
repair, Prompt 3 plus one added sentence. Word counts below come from
`wc -w` on the saved response file. All people, offices, and log
excerpts in the prompts are fictional and author-written.


## Prompt 1 (Section 12.1 worked example: a drafted Requirements Sheet for the housing office's email sorting)

```text
I'm a student worker on the help desk of a university housing office. Our help requests arrive in a shared email inbox, about 300 a month. Before the morning shift, one of us spends about 40 minutes sorting the new ones into four categories: Wi-Fi, Account, Hardware, and Other. Residents' names and room numbers appear in most emails. My supervisor wants to know whether an AI tool could do the sorting.

Fill in a Requirements Sheet for this problem, with these fields in this order: The problem (one sentence); Who is affected; Inputs (what goes in, what never goes in); Output required (shape, length, audience); Must-pass criteria; Constraints (cost, privacy, time, accessibility); The no-AI option (what doing it without AI costs). Do not name any tool.
```

Response:

```text
# Requirements Sheet: Help Desk Email Sorting

**1. The problem (one sentence)**
Each morning a student worker spends about 40 minutes manually sorting roughly 300 monthly help-request emails into Wi-Fi, Account, Hardware, and Other, and the housing office wants to know whether an AI tool could do that sorting reliably and safely.

**2. Who is affected**
- Student workers on the help desk, who lose about 40 minutes of each morning shift to sorting.
- Residents, whose requests wait until sorting is done and who could be routed to the wrong person if an email is misfiled.
- The supervisor, who must decide whether to adopt a tool and is accountable for resident data.
- The housing office and university, which are responsible for protecting resident privacy.

**3. Inputs**
- *What goes in:* The subject line and body text of each new help-request email, with names, room numbers, email addresses, phone numbers, and ID numbers removed or masked beforehand (for example, replaced with "[NAME]" and "[ROOM]"). A short written definition of the four categories, with a few example emails per category (also masked).
- *What never goes in:* Residents' names, room numbers, email addresses, phone numbers, student ID numbers, passwords or login details that residents paste into emails, attachments or screenshots (which may show personal data), and emails about sensitive matters (for example, safety, harassment, or medical issues) unless the office approves it.

**4. Output required (shape, length, audience)**
- *Shape:* One label per email: Wi-Fi, Account, Hardware, or Other. Optionally a confidence flag (sure / unsure) and an identifier linking back to the original email, such as its position in the inbox.
- *Length:* One word for the label, and at most one short sentence of reasoning when the tool is unsure.
- *Audience:* The student worker starting the morning shift, who will review the list and then work the tickets. The output should fit in a simple list or spreadsheet column that can be matched back to the inbox.

**5. Must-pass criteria**
- Every email gets exactly one of the four labels, with none dropped or invented.
- Accuracy is at least as good as the current manual sorting. Test this on a sample of at least 50 past emails (masked) that a human has already sorted, and agree on a target before the trial, for example 90% or higher agreement.
- Mixed or unclear emails (for example, "my Wi-Fi is down and I can't log in") are flagged for human review, not guessed at.
- Anything urgent or sensitive (safety, no internet before an exam, a locked-out account) is never buried in "Other" without a flag.
- A human can quickly spot-check or override any label.
- No personal data leaves the office's approved systems, confirmed before any real emails are used.
- Total time (running the tool plus reviewing its output) is clearly less than the current 40 minutes.

**6. Constraints**
- *Cost:* Must fit within the office's budget. Ideally free or low cost, since volume is small (about 10 emails a day).
- *Privacy:* Resident information is covered by university policy and student-records law (such as FERPA in the U.S.). The supervisor and the university's IT or privacy office must approve any tool before real emails are used. Masking must happen before anything is sent anywhere, and the masking step itself needs to be checked.
- *Time:* Results must be ready before the morning shift starts. Setup and training for student workers should be small, and the process should work when the person doing it changes each semester.
- *Accessibility:* The output and any steps must be usable by all student workers, including those using screen readers or other assistive technology, and in a plain format (a list or a spreadsheet column) without relying on color alone.

**7. The no-AI option (what doing it without AI costs)**
- About 40 minutes per morning shift of a student worker's time, which adds up to roughly 13 to 15 hours a month at the current volume.
- No new software cost, no new privacy risk, and no setup. The people sorting already know the categories and the local context.
- Weaknesses: it depends on whoever is on shift, so results can vary between workers. It is slow, and a fatigued or rushed person may misfile emails.
- Cheaper middle options exist, such as shared inbox rules, filters on keywords like "Wi-Fi" or "password," or a request form with a required category dropdown. These need no AI and avoid sending resident data anywhere, so they should be compared against the AI option.
```

Observation: 764 words by wc -w. Named no tool, kept all seven fields in order, and kept the four categories.

Observation: Added, not in the prompt: "at least 50 past emails," "90% or higher agreement" (a percentage target; the chapter rewrites it as a count), the FERPA mention ("such as FERPA in the U.S."), "about 10 emails a day" (300 a month over about 30 days, derived), and "13 to 15 hours a month" (40 minutes times about 20-22 shifts, derived).

Observation: The no-AI field names inbox rules, keyword filters, and a request form with a required category, and says they "need no AI and avoid sending resident data anywhere." The chapter credits this line.

Observation: Shown in the chapter: lines 21-28 (must-pass), 32 (privacy constraint), and 36-40 (no-AI option), with every cut marked.


## Prompt 2 (Section 12.2 worked example, flagship 1: a Work Order for a password-rotation runbook (accounting firm))

```text
Goal: Draft a runbook for the quarterly rotation of shared administrator passwords at a small accounting firm with 12 staff.
Scope: Write the runbook only. Do not write any password, script, or command. Do not change the firm's rule that two people are present for every rotation.
Inputs: The shared administrator accounts are the firewall, the Wi-Fi controller, the backup server, and the office printer. The firm's password manager holds every credential. Rotation happens on the first Friday of January, April, July, and October, after 5 p.m. The office manager and the firm's outside IT contractor do it together.
Deliverable and format: A numbered checklist in plain text, under 250 words, written for the office manager.
Acceptance criteria: It covers all four accounts. It names who does each step. It includes a step to test each new credential before the rotation is closed. It adds no account, tool, or rule that is not listed here.
Constraints: Never print a password or a command. If a step needs a fact I did not give you, write "ASK:" and the question instead of guessing.
Review plan: The office manager checks every step against these inputs before the first rotation.
```

Response:

```text
QUARTERLY SHARED ADMIN PASSWORD ROTATION RUNBOOK
For: Office Manager (OM). Partner: outside IT contractor (IT).
When: First Friday of January, April, July, October, after 5 p.m.
Accounts: firewall, Wi-Fi controller, backup server, office printer.
Rule: OM and IT are both present for every step.

1. OM and IT: Confirm both are present and the start time is after 5 p.m.
2. OM: Open the firm's password manager and confirm all four credentials are listed.
3. OM: ASK: Who must be told before rotation, and does any service lose access during it?
4. IT: Rotate the firewall credential.
5. OM and IT: Save the new firewall credential in the password manager. Test it by signing in. Record pass or fail.
6. IT: Rotate the Wi-Fi controller credential.
7. OM and IT: Save it in the password manager. Test it by signing in. Record pass or fail.
8. IT: Rotate the backup server credential.
9. OM and IT: Save it in the password manager. Test it by signing in. Record pass or fail.
10. IT: Rotate the office printer credential.
11. OM and IT: Save it in the password manager. Test it by signing in. Record pass or fail.
12. OM: ASK: What is the fallback if a test fails (for example, restoring the old credential)?
13. OM: Confirm all four tests passed. Do not close the rotation until they have.
14. OM and IT: Confirm the password manager shows only the new credentials.
15. OM: ASK: Where is the completed rotation recorded, and who signs it off?
16. OM and IT: Close the rotation.
```

Observation: 263 words by wc -w, header included, against an acceptance limit of under 250: Fail.

Observation: Covers all four accounts (steps 4-11), names OM, IT, or both on every step, tests each new credential (steps 5, 7, 9, 11) and step 13 blocks closing until all pass. No password or command appears.

Observation: Three ASK lines: steps 3, 12, and 15. The header line "Rule: OM and IT are both present for every step" is stricter than the prompt's "two people are present for every rotation": scored Partly on the no-added-rule criterion.

Observation: Shown in the chapter: lines 1-13 and 18-22 (steps 8-11 cut, marked).


## Prompt 3 (Fix It 12.1 symptom, attempt 1 of 1: a punchy results headline from a log excerpt)

```text
I'm presenting my project to my supervisor at a university housing office's help desk tomorrow. Write the one-line results headline for my results slide. Make it punchy and confident.

Here is the excerpt from my prompt log:
Work Order 1: sort 24 help emails (names and room numbers removed) into Wi-Fi, Account, Hardware, or Other. Each run was a fresh conversation. My supervisor checked every label.
Run 1: 21 correct, 2 wrong (both Wi-Fi emails labeled Hardware), 1 flagged unsure by the tool.
Run 2: 22 correct, 2 wrong (one Wi-Fi labeled Hardware, one Account labeled Other), 0 flagged unsure.
Time per run, including my check: about 10 minutes. Removing names and room numbers first: about 15 minutes.
```

Response:

```text
**Headline:** "AI sorted 24 help emails in ~10 minutes at 88-92% accuracy, with Wi-Fi vs. Hardware as the one confusion to watch."

Two notes for tomorrow:
- The range comes from 21/24 and 22/24 correct across two runs. If asked, say it's a small test and your supervisor checked every label.
- The 10 minutes includes your check but not the extra ~15 minutes of removing names and room numbers. Have that ready in case your supervisor asks about total time.

If you want a shorter version: "AI sorted help emails at 88-92% accuracy in 10 minutes per batch."
```

Observation: 99 words by wc -w. The headline converts 21/24 and 22/24 into "88-92% accuracy" (the course keeps counts, and the percentage hides the 1 email flagged unsure), calls Wi-Fi vs. Hardware "the one confusion," which Run 2's Account-to-Other error contradicts, and gives "~10 minutes" without the 15 minutes of masking.

Observation: The tool's own notes concede the masking time and the small test, but the notes do not reach the slide. Arithmetic check: 21/24 = 87.5 percent, 22/24 = 91.7 percent, so "88-92%" is a rounded range.

Observation: The placement table's candidate ("the tool got every ticket right") reproduced as a rounder, subtler claim; the notes file records the rewritten candidate. Shown in full in the chapter.


## Prompt 4 (Fix It 12.1 repair: Prompt 3 plus one added sentence (build the headline only from the log's counts and times, with no percentage and no unsupported word))

```text
I'm presenting my project to my supervisor at a university housing office's help desk tomorrow. Write the one-line results headline for my results slide. Make it punchy and confident. Build the headline only from the counts and times in the log, stated exactly as the log gives them, with no percentage and no word the log does not support.

Here is the excerpt from my prompt log:
Work Order 1: sort 24 help emails (names and room numbers removed) into Wi-Fi, Account, Hardware, or Other. Each run was a fresh conversation. My supervisor checked every label.
Run 1: 21 correct, 2 wrong (both Wi-Fi emails labeled Hardware), 1 flagged unsure by the tool.
Run 2: 22 correct, 2 wrong (one Wi-Fi labeled Hardware, one Account labeled Other), 0 flagged unsure.
Time per run, including my check: about 10 minutes. Removing names and room numbers first: about 15 minutes.
```

Response:

```text
**21 and 22 of 24 help emails labeled correctly in two runs, about 10 minutes per run**

The headline leaves out the 15 minutes of name and room-number removal, so be ready to mention it if your supervisor asks about total time.
```

Observation: 42 words by wc -w. The headline "21 and 22 of 24 help emails labeled correctly in two runs, about 10 minutes per run" matches Run 1, Run 2, and the time line.

Observation: The percentage and "the one confusion" are gone. It still leaves out the 15 minutes of masking and says so in its second line. Shown in full.


## Prompt 5 (Section 12.3 worked example: the questions a supervisor is likely to ask)

```text
I work on the help desk of a university housing office. Tomorrow I recommend to my supervisor that we extend our pilot of an AI tool that sorts help emails into Wi-Fi, Account, Hardware, or Other, for one more month, with every label checked by a person. My evidence: in two fresh runs on the same 24 emails, with names and room numbers removed, the tool labeled 21 and then 22 correctly. Each run took about 10 minutes with my check, plus about 15 minutes to remove names and room numbers first.

List the five questions my supervisor is most likely to ask. One line each, no answers.
```

Response:

```text
1. Is a sample of 24 emails, run twice, big enough to trust an accuracy of roughly 88–92%?
2. Were those 24 emails representative of our real volume, including messy, multi-issue, or unclear ones?
3. Does the time saved actually beat doing the sorting by hand, given 10 minutes of checking plus 15 minutes of removing names and room numbers?
4. What happens to student privacy when real emails go in, and is the tool approved for that data?
5. What will we measure during the extra month to decide whether to adopt, change, or drop it?
```

Observation: 97 words by wc -w. Five questions, one line each, no answers, as asked.

Observation: Question 1 converts the counts to "roughly 88–92%," which the prompt never stated. Questions 2 (sample choice), 3 (by-hand time), and 4 (approval for real emails) are not answered by the evidence in the prompt. Question 5 is answered if the ask names the measures. Shown in full.


## Prompt 6 (Try It Yourself 12.3 (problem-first), shown after the student's own run, flagship 2: the plumbing contractor's Presentation outline)

```text
I'm a dispatcher at a plumbing contractor. Draft a Presentation outline for a five-minute talk to the owner, who decides whether we keep paying for an AI tool that drafts appointment-confirmation texts.
Use these sections in this order: Audience; The recommendation first; The evidence; The limits; The ask; Questions you expect.
Recommendation: extend the pilot one month, with a dispatcher checking every text. Evidence, all from our three-week pilot log: 2 dispatchers; about 150 confirmation texts a week; about 3 minutes to write one by hand; 60 texts drafted; 52 sent with light edits at about 1 minute each; 6 rewritten; 2 gave a wrong arrival window and were caught before sending; customers' names and addresses were removed before any text went into the tool. Price: $20 per dispatcher per month (vendor quote). Not measured: minutes spent on the 6 rewrites, and how customers responded.
Use only these facts. Keep counts as counts, with no percentages. Under The limits, name what the log cannot support. Under Questions you expect, say for each one whether the evidence answers it.
```

Response:

```text
# Presentation Outline: Should We Keep the AI Confirmation-Text Tool?
*Five-minute talk to the owner*

## 1. Audience
- The owner decides whether we keep paying for the tool. They are not a technical person and care about three things: cost, risk to customers, and dispatcher time.
- Open with the decision, not the technology. Plain terms throughout: "drafts texts," not "model" or "prompts."
- About 30 seconds.

## 2. The recommendation first
- **Extend the pilot one month, with a dispatcher checking every text before it goes out.**
- Not "buy it for good" and not "cancel." The pilot shows promise and also showed an error type that needs a human check.
- About 30 seconds.

## 3. The evidence
All figures come from our three-week pilot log.
- **Setup:** 2 dispatchers; about 150 confirmation texts a week.
- **Baseline:** about 3 minutes to write one by hand.
- **Pilot results:** the tool drafted 60 texts.
  - 52 were sent with light edits, at about 1 minute each.
  - 6 were rewritten.
  - 2 gave a wrong arrival window and were caught before sending.
- **Privacy:** customers' names and addresses were removed before any text went into the tool.
- **Price:** $20 per dispatcher per month (vendor quote), so $40 a month for our 2 dispatchers.
- **Takeaway line:** for the 52 light-edit texts, about 1 minute replaced about 3.
- About 1.5 minutes.

## 4. The limits
What the log cannot support:
- **Rewrite time was not measured.** We do not know how many minutes the 6 rewrites took, so we cannot state a total time saved.
- **Customer response was not measured.** We do not know whether customers replied, confirmed, or were confused or annoyed by the texts.
- **The log cannot show a dollar saving.** Without rewrite time, any savings figure would be a guess.
- **Only 60 of roughly 450 texts were drafted by the tool.** (About 150 a week over three weeks.) We do not know how the tool would do on the rest.
- **The 2 wrong arrival windows were caught only because a dispatcher checked.** The log does not show what would have happened without the check, and it does not tell us how often errors would occur over a longer period.
- About 1 minute.

## 5. The ask
- Approve one more month of the tool at $20 per dispatcher, with a dispatcher checking every text before sending.
- During the month, also record: minutes spent on each rewrite, and how customers responded.
- Come back with those numbers so the keep-or-cancel decision rests on measured data.
- About 45 seconds.

## 6. Questions you expect
| Question | Does the evidence answer it? |
|---|---|
| Does it save time? | **Partly.** For the 52 light-edit texts, about 1 minute versus about 3 by hand. The 6 rewrites were not timed, so total savings are unknown. |
| What does it cost? | **Yes.** $20 per dispatcher per month (vendor quote). |
| Is it safe to send what it writes? | **Partly.** 2 texts had a wrong arrival window, both caught before sending. That is why every text needs a check. How often errors would occur long-term is not answered. |
| Is customer information protected? | **Yes, for the pilot.** Names and addresses were removed before any text went into the tool. |
| Do customers like the texts? | **No.** Customer response was not measured. |
| Will it pay for itself? | **No.** Without rewrite time and with a quote-only price, the log cannot show this. The extension is meant to find out. |
| Why not just decide now? | **Partly.** The log shows enough promise to continue, but not enough to commit permanently. |
- Reserve about 1 minute for questions, or take them after the talk.
```

Observation: 644 words by wc -w. Six parts in order, recommendation first, counts kept as counts.

Observation: Holds: every evidence count; "$40 a month for our 2 dispatchers" (2 x $20); "60 of roughly 450 texts" (150 x 3 = 450, labeled in the response). Limits name both unmeasured items (rewrite minutes, customer response).

Observation: Not in source: "They are not a technical person and care about three things: cost, risk to customers, and dispatcher time" (nothing about the owner was given). Overclaim: "Is customer information protected? Yes, for the pilot." The facts say what was removed before input, not what the vendor keeps; no data policy reading was given.

Observation: Expected-questions table has 7 rows, each with an answer status. Shown in the chapter: lines 4-5, 23, 27-33, 42-48, with every cut marked.


## Prompt 7 (Section 12.4 worked example: a reflection written with no log)

```text
Write a 120-word reflection for my AI project: I used an AI tool to sort help emails for a university housing office's help desk. Cover what the AI did well, what it got wrong, and what I would do differently.
```

Response:

```text
For this project, I used an AI tool to sort incoming help emails for a university housing office's help desk. The AI performed well at identifying common categories, such as maintenance requests, roommate conflicts, and billing questions, and it processed large batches far faster than I could by hand. However, it struggled with emails that combined multiple issues or used vague, emotional language, and it sometimes marked urgent safety concerns as routine. It also misread housing-specific terms like "RA" and "move-in window." Next time, I would give the AI clearer category definitions and examples, add an urgent-priority flag, and have a staff member review uncertain or high-risk messages. Testing on a small sample first would help me catch errors early.

*I made up the specific examples (categories, errors), so swap in the ones from your actual project.*
```

Observation: 137 words by wc -w, including its closing note, against a 120-word request.

Observation: Invents the project's content: categories "maintenance requests, roommate conflicts, and billing questions" (the real ones are Wi-Fi, Account, Hardware, Other), errors with "urgent safety concerns," and misread terms "RA" and "move-in window." Its last line says: "I made up the specific examples (categories, errors), so swap in the ones from your actual project." Shown in full.


## Prompt 8 (Section 12.4 worked example: the same reflection, written from a pasted log excerpt)

```text
Write a 120-word reflection for my AI project, using only the log excerpt below. Cover what the AI did well, what it got wrong, and what I would do differently. If the log does not say something, leave it out.

Log excerpt (university housing office help desk):
Work Order 1: sort 24 help emails (names and room numbers removed) into Wi-Fi, Account, Hardware, or Other. Each run was a fresh conversation. My supervisor checked every label.
Run 1: 21 correct, 2 wrong (both Wi-Fi emails labeled Hardware), 1 flagged unsure by the tool.
Run 2: 22 correct, 2 wrong (one Wi-Fi labeled Hardware, one Account labeled Other), 0 flagged unsure.
No-AI comparison: the inbox's keyword rules sorted the same 24 emails: 17 correct, 7 sent to Other.
Masking check: on my first pass I missed one room number in email 17. My supervisor caught it before Run 1.
Time per run, including my check: about 10 minutes. Removing names and room numbers first: about 15 minutes.
```

Response:

```text
The AI sorted emails more accurately than the inbox's keyword rules. It got 21 of 24 correct in Run 1 and 22 of 24 in Run 2, compared with 17 of 24 for the keywords, which sent seven emails to Other. In Run 1 it flagged one email as unsure. However, it made mistakes: it labeled Wi-Fi emails as Hardware in both runs (three times total), and in Run 2 it labeled an Account email as Other. Run 2 flagged nothing unsure despite two errors. Next time, I would keep my supervisor checking every label, and I would review the masking more carefully, since I missed a room number in email 17 on my first pass (caught by my supervisor).
```

Observation: 120 words by wc -w.

Observation: Every count holds against the excerpt: 21 of 24, 22 of 24, 17 of 24 and seven to Other for the keyword rules, one unsure in Run 1, Wi-Fi labeled Hardware three times total (two in Run 1, one in Run 2), Account labeled Other in Run 2, the missed room number in email 17 caught by the supervisor.

Observation: "Run 2 flagged nothing unsure despite two errors" holds (Run 2: 0 unsure, 2 wrong). The "what I would do differently" sentence is the model's choice, not a log fact; the chapter says the student keeps it only if she means it. Omits the time lines. Shown in full.


## Prompt 9 (Section 12.4 worked example: an Ethics Statement drafted from listed facts)

```text
Draft the Ethics Statement for my project, with five sections in this order: Privacy, Ownership, Bias, Disclosure, Accountability. Two or three sentences per section. Use only the facts below.

Project: an AI tool sorts help emails for a university housing office's help desk into Wi-Fi, Account, Hardware, or Other.
Facts:
* 24 emails went into the tool, with residents' names and room numbers removed first. On my first pass I missed one room number. My supervisor caught it before the first run.
* I used the chat assistant on my university account. I read its data policy on October 2: chats on university accounts are not used to train the model.
* I wrote the category definitions and the prompt. The tool wrote the labels.
* I did not run a paired prompt test. Some residents write in Spanish, and I have not checked whether those emails land in Other more often.
* My supervisor knows the tool sorts the emails. Residents are not told, because the tool never writes to them.
* The student worker on shift checks every label before an email is forwarded. My supervisor approves the process.
```

Response:

```text
# Ethics Statement

**Privacy**
Before any email went into the tool, I removed residents' names and room numbers. On my first pass I missed one room number, and my supervisor caught it before the first run, so no identifying details were processed. I used the chat assistant on my university account, and I read its data policy on October 2: chats on university accounts are not used to train the model.

**Ownership**
I wrote the category definitions (Wi-Fi, Account, Hardware, Other) and the prompt. The tool wrote the labels for the 24 emails. The design of the sorting scheme is mine, while the individual label outputs came from the tool.

**Bias**
I did not run a paired prompt test, so I have not checked for differences in how the tool treats different groups of residents. Some residents write in Spanish, and I have not checked whether their emails land in Other more often than English-language emails. Until that check is done, this is a known gap and a possible source of unfair sorting.

**Disclosure**
My supervisor knows that the tool sorts the emails. Residents are not told, because the tool never writes to them. Its only role is to assign an internal category label.

**Accountability**
The student worker on shift checks every label before an email is forwarded, so a person reviews each tool decision. My supervisor approves the process, and I am responsible for the prompt, the category definitions, and the data preparation.
```

Observation: 244 words by wc -w. Five sections in the requested order.

Observation: Not in source: "so no identifying details were processed" (the facts say names and room numbers were removed; other identifiers were not addressed), and "I am responsible for the prompt, the category definitions, and the data preparation" (an added accountability claim).

Observation: Ownership names who wrote what and no license, because the prompt gave no terms of use. Bias states the untested gap, as the section allows. Shown in the chapter: lines 3-10 and 15-16 (title and the Disclosure section cut, marked).


## Verification notes

All checks below ran on 2026-10-21 and 2026-10-22 (America/Phoenix). Status codes come from `curl -sI -o /dev/null -w "%{http_code}" URL`. Quoted text was read from the page or PDF itself, saved under the writer's scratchpad (`src12/`), not from a summary.

* Further Reading URLs, all 200 by plain `curl -sI`: https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0_3.pdf; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence; https://www.w3.org/WAI/teach-advocate/accessible-presentations/ (serves the page titled "Making Events Accessible: Checklist for meetings, conferences, training, and presentations that are remote/virtual, in-person, or hybrid"); https://digital.gov/guides/plain-language (https://www.plainlanguage.gov/guidelines/ returns 301 to it).
* Mata v. Avianca, Inc., No. 22-cv-1461 (PKC), U.S. District Court for the Southern District of New York, Opinion and Order on Sanctions, Document 54, filed and dated June 22, 2023, Judge P. Kevin Castel (PDF, `pdftotext -layout`). Page 1: "Technological advances are commonplace and there is nothing inherently improper about using a reliable artificial intelligence tool for assistance. But existing rules impose a gatekeeping role on attorneys to ensure the accuracy of their filings. Rule 11, Fed. R. Civ. P." Respondents: Peter LoDuca, Steven A. Schwartz, and the law firm Levidow, Levidow & Oberman P.C. They "abandoned their responsibilities when they submitted non-existent judicial opinions with fake quotes and citations created by the artificial intelligence tool [named product], then continued to stand by the fake opinions after judicial orders called their existence into question." Conclusion (page 34): letters to plaintiff Roberto Mata and to "each judge falsely identified as the author" of the fake opinions, and "A penalty of $5,000 is jointly and severally imposed on Respondents." The chapter names no product.
* NIST AI 600-1 publication page: "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile," "Published July 26, 2024"; the AI RMF page says the profile "can help organizations identify unique risks posed by generative AI and proposes actions for generative AI risk management."
* W3C WAI checklist: "speakers describe pertinent visual information"; "Provide slides, handouts, and other material to participants, interpreters, and captioners, as needed."
* Digital.gov plain language guide series: "The Plain Writing Act of 2010 established the requirement that content for the public is written for its specific audience."
* MCCCD course descriptions (docs/mcccd/, fetched 2026-10-21 by the planning session): CIS144 "explores advanced applications of Artificial Intelligence (AI) with a focus on agentic systems and AI driven data analytics"; CIS218 "focuses on the design, integration, and deployment of advanced artificial intelligence (AI) solutions." The MCCCD course pages themselves returned 403 to curl, so the course conclusion paraphrases the stored copies and links neither.
* Chapter arithmetic, checked by hand: Prompt 2 word count 263 (wc -w); Prompt 6: 2 x $20 = $40, 150 x 3 = 450; Prompt 3: 21/24 = 87.5 percent, 22/24 = 91.7 percent; Prompt 8: Wi-Fi labeled Hardware 2 + 1 = 3; time per batch in the Fix It Verify: 10 + 15 = about 25 minutes.
* Vendor pages: the chapter carries no vendor fact and no Tool check callout. Attempted for a possible export callout: help.openai.com export article (403 to curl and to the fetch tool), Gemini Apps Privacy Hub (200, read). Only one vendor could be read, so no callout was written.
* Fictional details: the housing office, the accounting firm, the plumbing contractor, and their logs are unnamed and author-written. Copperwind's Deskside line 602-555-0149 (in the capstone brief) is the canon number from the chapter 7 facts sheet, in the fictional 555-01xx range.
