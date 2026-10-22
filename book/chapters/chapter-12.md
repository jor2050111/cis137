# Chapter 12: The AI Application Project

Mei Lin sends a short message on a Monday morning. The pilot ends this quarter. She has to tell the owner what Copperwind adopts for the next year: which jobs get an AI tool, which tools, under what rules, and how anything new gets piloted. "Present it to me first," she writes. "If I can't defend a line of it, it doesn't go to the owner."

This chapter is the project. You already hold every tool it needs. Chapter 10 gave you the fair test, the Comparison Matrix, and the Tool Survey. Chapter 11 gave you the Requirements Sheet, the Work Order, and the Selection Decision. Part III gave you the Accuracy Audit, the AI Use Policy, and the Use Evaluation. A literacy course would end here with a reflection. This one ends with artificial intelligence (AI) work delivered. You build a solution someone can use and a trail a colleague can retrace. You present it to the person who decides, with an Ethics Statement that says who answers for the result.

You choose one of two options, and they carry equal weight. The Copperwind capstone is Mei Lin's year-ahead recommendation. The other option is an IT project of your own: a home lab, a club project, a course project, or a task at work. Both use the same artifacts and the same rubric. Either way, you finish the course holding a Toolkit, with a README that says which tools you will use next week and how.

## Module Overview 🧭

* **Estimated time:** The project runs across the whole chapter, so plan by part. Sections 12.1-12.4 with their Try It Yourself exercises take about 4-5 hours. Skills Lab 12A Part 1 takes about 2-3 hours, Part 2 about 4-6 hours, and Part 3 about 4-5 hours
* **Prerequisites:** Chapters 10 and 11 (the fair test, the Comparison Matrix, the Tool Survey, the Requirements Sheet, the Work Order, and the Selection Decision). Also Chapters 7-9 (the Accuracy Audit, the Audit Report, the AI Use Policy, and the Use Evaluation) and the prompt library from Part II. This chapter's packet ships a starter copy of every template, so you need no saved file
* **Deliverables:** Skills Lab 12A deliverable (the project), your Toolkit folder, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **12.1 (Create):** Design an AI solution for a scenario from a Requirements Sheet, Work Orders, and a Tool Survey, with its Verification Trail (Sections 12.1-12.2)
* **12.2 (Evaluate):** Defend a recommendation to a stakeholder with evidence from the Verification Trail and an honest statement of its limits (Section 12.3)
* **12.3 (Evaluate):** Judge the solution's privacy, ownership, bias, disclosure, and accountability in an Ethics Statement (Section 12.4)

### This chapter aligns with the following Course Learning Outcomes

* **CLO 1 (Evaluate):** Evaluate AI-generated responses for accuracy.
* **CLO 3 (Apply):** Demonstrate effective prompting strategies to improve AI outputs.
* **CLO 4 (Analyze):** Analyze the current state of AI and its impact on society, including strengths and weaknesses.
* **CLO 5 (Apply):** Apply ethical guidelines to make responsible decisions when using AI tools.
* **CLO 6 (Evaluate):** Select appropriate AI solutions to address specific problems.

---

## 12.1 Choose the Scenario, Define Done

A **capstone** is the final project that pulls a course's skills into one delivered piece of work for a real decision. This one has two doors:

| Option | Who decides | What you deliver |
| --- | --- | --- |
| The Copperwind capstone | Mei Lin, who carries it to the owner | The year-ahead recommendation: which jobs get an AI tool, which tools, under what rules, with a pilot plan |
| Your own IT project | A supervisor, a club officer, a teammate, or your instructor | A text deliverable a person can check: a runbook, a test plan, a build checklist, configuration notes, or a migration plan |

Pick the option where you have something at stake and data you are allowed to share. Your own project qualifies when four things hold. It is a job you are doing now. Someone other than you will act on the result. The deliverable is text a person can check. And at least two parts can go to an AI tool through a Work Order, while at least one part stays with a person. The privacy rule is the one you have used all course: nothing identifying goes into a tool, and nothing you do not have the right to share.

Every project has a **stakeholder**: a person who decides on your result or has to live with it. Name the one who decides, then list the others it affects. For the Copperwind option, Mei Lin decides what goes to the owner, and the five Deskside technicians live with the result. For a home lab, the stakeholder might be the roommate who shares the network.

### Done Means the Requirements Sheet Passes

Chapter 11 wrote the Requirements Sheet before naming any tool. In the project it does a second job: it is your definition of done. Its seven fields run in this order: The problem, Who is affected, Inputs, Output required, Must-pass criteria, Constraints, and The no-AI option. When every must-pass criterion passes, you are done. When one fails, you are not, however good the output looks.

A student worker on a university housing office's help desk chose her own project. Help emails arrive in a shared inbox, and sorting them each morning takes her about 40 minutes. She asked a chat assistant to draft the sheet:

```text
I'm a student worker on the help desk of a university housing office. Our help requests arrive in a shared email inbox, about 300 a month. Before the morning shift, one of us spends about 40 minutes sorting the new ones into four categories: Wi-Fi, Account, Hardware, and Other. Residents' names and room numbers appear in most emails. My supervisor wants to know whether an AI tool could do the sorting.

Fill in a Requirements Sheet for this problem, with these fields in this order: The problem (one sentence); Who is affected; Inputs (what goes in, what never goes in); Output required (shape, length, audience); Must-pass criteria; Constraints (cost, privacy, time, accessibility); The no-AI option (what doing it without AI costs). Do not name any tool.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
[...]
**5. Must-pass criteria**
- Every email gets exactly one of the four labels, with none dropped or invented.
- Accuracy is at least as good as the current manual sorting. Test this on a sample of at least 50 past emails (masked) that a human has already sorted, and agree on a target before the trial, for example 90% or higher agreement.
- Mixed or unclear emails (for example, "my Wi-Fi is down and I can't log in") are flagged for human review, not guessed at.
- Anything urgent or sensitive (safety, no internet before an exam, a locked-out account) is never buried in "Other" without a flag.
- A human can quickly spot-check or override any label.
- No personal data leaves the office's approved systems, confirmed before any real emails are used.
- Total time (running the tool plus reviewing its output) is clearly less than the current 40 minutes.
[...]
- *Privacy:* Resident information is covered by university policy and student-records law (such as FERPA in the U.S.). The supervisor and the university's IT or privacy office must approve any tool before real emails are used. Masking must happen before anything is sent anywhere, and the masking step itself needs to be checked.
[...]
**7. The no-AI option (what doing it without AI costs)**
- About 40 minutes per morning shift of a student worker's time, which adds up to roughly 13 to 15 hours a month at the current volume.
- No new software cost, no new privacy risk, and no setup. The people sorting already know the categories and the local context.
- Weaknesses: it depends on whoever is on shift, so results can vary between workers. It is slow, and a fatigued or rushed person may misfile emails.
- Cheaper middle options exist, such as shared inbox rules, filters on keywords like "Wi-Fi" or "password," or a request form with a required category dropdown. These need no AI and avoid sending resident data anywhere, so they should be compared against the AI option.
```

The draft named no tool and kept all seven fields in order. Its best line is the last one: inbox rules or a request form with a required category "need no AI and avoid sending resident data anywhere." That is the no-AI option doing its job, and the student will test it. The draft also proposed things nobody gave it. It suggested "at least 50 past emails" and "90% or higher agreement." This course keeps counts, so if she keeps that criterion it becomes "at least 45 of 50 labels match my supervisor's." It said resident information falls under student-records law "such as FERPA." Chapter 8 showed what FERPA covers, but whether these emails are education records is for the university's privacy office to rule. The draft itself says that office must approve any tool before real emails go in. A drafted sheet is a list of proposals. You keep, rewrite, or cut each one, and the sheet you keep is yours.

### Try It Yourself 12.1: Your Scenario, Your Definition of Done 🛠️

**Predict:** Choose your option. Before you write anything, predict which field of the Requirements Sheet will be hardest to fill without guessing, and why.

**Run:** Copy the `toolkit-starter/` folder from this chapter's data pack into a folder named `toolkit-lastname`, and do every fill from here on in that copy, so the starter stays clean. Open `toolkit-lastname/requirements-sheet-template.md` and fill all seven fields for your project, naming no tool, and write each must-pass criterion so a person can check it with a count or a yes or no. If you ask a chat assistant to suggest criteria, paste its draft into your prompt log and mark each suggestion Keep, Rewrite, or Cut. The filled Requirements Sheet is the artifact. It opens your Verification Trail.

**Explain:** Was the hardest field the one you predicted? In 1-2 sentences, explain which must-pass criterion would make you stop the project if it failed.

### Quick Check 12.1 ✅

1. A classmate proposes "use AI to make my resume better" as an own-project option. Apply the four conditions from this section, decide whether it qualifies, and if it does not, rewrite it into a project that does.
2. A must-pass criterion reads "The runbook is clear and accurate." Rewrite it as two criteria a stakeholder could check with a count or a yes or no.
3. The housing office's no-AI option (keyword rules in the inbox) costs nothing new and sends no resident data anywhere. Name the result from a test that would justify choosing an AI tool over it anyway, and justify your answer.

---

## 12.2 Build It: Work Orders and the Verification Trail

Building the solution is a loop you already know: write a Work Order, run it, check the result, log it. Chapter 11's Work Order has eight fields in this order: Goal, Scope, Inputs, Deliverable and format, Acceptance criteria, Constraints, Review plan, and Log. You sit in the human-in-the-loop seat. You set the goal, the limits, and the checks. The tool does the steps, and you decide whether the result passes. The same order directs a tool that takes several steps on its own, because the checks do not change when the tool does more.

### A Work Order, Run and Checked

The office manager of a small accounting firm took on an IT job of her own: a runbook for the quarterly rotation of the firm's shared administrator passwords. She sent her Work Order's fields as the prompt. The Log field stays out of the prompt, because the log is her job. Send the prompt without the [Step] lines:

```text
[Step 1: set the goal and fence the scope]
Goal: Draft a runbook for the quarterly rotation of shared administrator passwords at a small accounting firm with 12 staff.
Scope: Write the runbook only. Do not write any password, script, or command. Do not change the firm's rule that two people are present for every rotation.
[Step 2: hand over the inputs]
Inputs: The shared administrator accounts are the firewall, the Wi-Fi controller, the backup server, and the office printer. The firm's password manager holds every credential. Rotation happens on the first Friday of January, April, July, and October, after 5 p.m. The office manager and the firm's outside IT contractor do it together.
[Step 3: name the deliverable and the checks it must pass]
Deliverable and format: A numbered checklist in plain text, under 250 words, written for the office manager.
Acceptance criteria: It covers all four accounts. It names who does each step. It includes a step to test each new credential before the rotation is closed. It adds no account, tool, or rule that is not listed here.
[Step 4: set the limits and say who reviews]
Constraints: Never print a password or a command. If a step needs a fact I did not give you, write "ASK:" and the question instead of guessing.
Review plan: The office manager checks every step against these inputs before the first rotation.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

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
[...]
12. OM: ASK: What is the fallback if a test fails (for example, restoring the old credential)?
13. OM: Confirm all four tests passed. Do not close the rotation until they have.
14. OM and IT: Confirm the password manager shows only the new credentials.
15. OM: ASK: Where is the completed rotation recorded, and who signs it off?
16. OM and IT: Close the rotation.
```

She scored it against her acceptance criteria and the format and constraint lines, one at a time, with the evidence:

| Criterion | Result | Evidence |
| --- | --- | --- |
| Covers all four accounts | Pass | Steps 4-11 rotate and test each account in turn |
| Names who does each step | Pass | Every step opens with OM, IT, or both |
| Tests each new credential before closing | Pass | Steps 5, 7, 9, and 11 test, and step 13 says "Do not close the rotation until they have" |
| Adds no account, tool, or rule | Partly | The header restates the two-person rule as "every step," which is stricter than the firm's "every rotation" |
| Under 250 words | Fail | 263 words by a word counter, header included |
| No password or command | Pass | None appears |

Four pass, one partly passes, and one fails. The three ASK lines (steps 3, 12, and 15) are the most useful part, because each one marks a fact she never gave. A runbook with a guessed fallback plan would read just as smoothly and fail on the night it mattered. She answers the three questions and decides which two-person wording stands. The answers go into Inputs as version 2, and the length fix is version 3, each logged in a Refinement Log. At Copperwind, the same Work Order shape fits Job D in Mei Lin's brief: the checklist a technician runs before sending an AI-drafted first reply.

### The Verification Trail

A result nobody can retrace is a claim, not evidence. The **Verification Trail** is the project's evidence pack a colleague can retrace. It holds the Requirements Sheet, the Work Orders, the prompt log, the Audit Reports, the Refinement Logs, and the Selection Decision. Its README says where each lives and what was checked by a person. The test is simple. Could a colleague start from your headline number and reach the run behind it without asking you a question?

The README carries the most weight, because it records what a person checked. Here is how two rows of the office manager's README could read after her check:

| Piece | File name and where it lives | What it holds | What a person checked (who, when, against what) |
| --- | --- | --- | --- |
| Work Order 1 | `work-order-1-runbook.md`, in the project folder | The runbook Work Order and its scored first run | The office manager checked all 16 steps against the inputs: four checks pass, one partly, and the 250-word limit fails at 263 words |
| Prompt log | `prompt-log.md`, entries 1-2, in the project folder | The prompt and the response, pasted exactly, with the tool and the date | The office manager confirmed each entry matches what she sent and received |

Her README also has a "What nobody checked" line: whether the contractor's sign-in test works the same way on each of the four devices. Saying where the checking stopped makes the rest of the trail easier to trust.

### Try It Yourself 12.2: Your First Work Order 🛠️

**Predict:** Choose one job in your project that an AI tool could do. Predict which acceptance criterion its first run will fail.

**Run:** Fill `toolkit-lastname/work-order-template.md` for that job and send its fields as the prompt in a fresh conversation, leaving the Log field out of the prompt. Score each acceptance criterion Pass, Partly, or Fail, with a quote or a count as evidence. Paste the prompt, the response, and your scores into your prompt log. Then open `toolkit-lastname/verification-trail-readme-template.md` and fill the Work Order's row, including what you checked. Work Order 1 and the first row of your Verification Trail README are the artifacts.

**Explain:** Was your prediction right? In 1-2 sentences, explain which criterion a colleague would find hardest to check from your log alone, and what you would add so they could.

### Quick Check 12.2 ✅

1. A Work Order's acceptance criteria say only "Make it good." For the runbook job above, write two acceptance criteria to replace it, and name the checklist that runs each one: the Output Checklist or the Accuracy Audit.
2. A teammate's Verification Trail README lists every file but says nothing about what a person checked. Analyze what a colleague can retrace from it and what they cannot.
3. The runbook draft passed four of its checks, partly passed one, and failed the word limit. Decide whether the office manager should use it as is, fix and use it, or run a new version, and justify your choice with the failed check.

---

## 12.3 Present It: Evidence and Limits

The presentation is where a good project can undo itself. One line rounder than the log, and the person who decides stops trusting the rest. **The Presentation outline** keeps the talk tied to the trail. It has six parts, in this order:

1. **Audience:** who will hear it, what they decide, and what they already know.
2. **The recommendation first:** what you recommend, in one or two sentences.
3. **The evidence:** three to five lines, each with its count and its source in the Verification Trail.
4. **The limits:** what the log cannot support, such as numbers you did not collect and cases you did not test.
5. **The ask:** one action, with who takes it.
6. **Questions you expect:** each with where its answer lives in the trail, or "Not answered yet."

The recommendation comes first for the same reason it leads the Memo: a busy reader may hear only the opening. The limits protect the ask. A stakeholder who finds a gap you did not name will doubt the lines you did support. For the Copperwind option, Mei Lin is the audience, and the owner is the person she must then convince, so your outline has to survive being retold. Plan for everyone in the room, too. Describe what a slide shows out loud, and share your material ahead of time (the W3C checklist in Further Reading covers both).

### Questions You Expect

The housing office student recommended extending her pilot one more month. She asked a chat assistant what her supervisor would ask:

```text
I work on the help desk of a university housing office. Tomorrow I recommend to my supervisor that we extend our pilot of an AI tool that sorts help emails into Wi-Fi, Account, Hardware, or Other, for one more month, with every label checked by a person. My evidence: in two fresh runs on the same 24 emails, with names and room numbers removed, the tool labeled 21 and then 22 correctly. Each run took about 10 minutes with my check, plus about 15 minutes to remove names and room numbers first.

List the five questions my supervisor is most likely to ask. One line each, no answers.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
1. Is a sample of 24 emails, run twice, big enough to trust an accuracy of roughly 88–92%?
2. Were those 24 emails representative of our real volume, including messy, multi-issue, or unclear ones?
3. Does the time saved actually beat doing the sorting by hand, given 10 minutes of checking plus 15 minutes of removing names and room numbers?
4. What happens to student privacy when real emails go in, and is the tool approved for that data?
5. What will we measure during the extra month to decide whether to adopt, change, or drop it?
```

These are fair questions. Now place each one against the trail. Question 1 turns her counts into "roughly 88–92%," which she never wrote. She answers in counts and puts the small sample under The limits. Question 5 is answered if her ask names what the extra month will measure. Questions 2, 3, and 4 are "Not answered yet." Her log never says how the 24 emails were chosen. It has no by-hand time for those same 24 emails. And the privacy office has not yet approved real emails going in. She can time a by-hand sort before the talk. The other two go under The limits, stated plainly.

### Fix It 12.1: The Results Slide 🔧

The same student needs one headline for her results slide.

**Symptom:** She pasted her log excerpt and asked for something punchy:

```text
I'm presenting my project to my supervisor at a university housing office's help desk tomorrow. Write the one-line results headline for my results slide. Make it punchy and confident.

Here is the excerpt from my prompt log:
Work Order 1: sort 24 help emails (names and room numbers removed) into Wi-Fi, Account, Hardware, or Other. Each run was a fresh conversation. My supervisor checked every label.
Run 1: 21 correct, 2 wrong (both Wi-Fi emails labeled Hardware), 1 flagged unsure by the tool.
Run 2: 22 correct, 2 wrong (one Wi-Fi labeled Hardware, one Account labeled Other), 0 flagged unsure.
Time per run, including my check: about 10 minutes. Removing names and room numbers first: about 15 minutes.
```

Here is the response it gave (captured from a chat assistant, October 2026):

```text
**Headline:** "AI sorted 24 help emails in ~10 minutes at 88-92% accuracy, with Wi-Fi vs. Hardware as the one confusion to watch."

Two notes for tomorrow:
- The range comes from 21/24 and 22/24 correct across two runs. If asked, say it's a small test and your supervisor checked every label.
- The 10 minutes includes your check but not the extra ~15 minutes of removing names and room numbers. Have that ready in case your supervisor asks about total time.

If you want a shorter version: "AI sorted help emails at 88-92% accuracy in 10 minutes per batch."
```

It reads well, it sounds sure, and every number in it comes from somewhere. Only the headline goes on the slide.

**Diagnose:** Put the headline beside the log excerpt. For each number and each claim in the headline, find the log line it rests on. Which pieces have a line that says the same thing, and which do not?

**Repair:** Three pieces have no line behind them. "88-92% accuracy" turns two counts into a percentage, and it hides the 1 email the tool flagged unsure. "The one confusion to watch" is wrong, because Run 2 also put an Account email in Other. And "in ~10 minutes" leaves out the 15 minutes of removing names first. The tool's own notes say so, but the notes never reach the slide. The repair adds one sentence after "Make it punchy and confident." That sentence makes one requirement (the log is the only source), so any change in the headline is credited to it. That is the one change:

```text
Build the headline only from the counts and times in the log, stated exactly as the log gives them, with no percentage and no word the log does not support.
```

The log excerpt below it stayed the same.

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
**21 and 22 of 24 help emails labeled correctly in two runs, about 10 minutes per run**

The headline leaves out the 15 minutes of name and room-number removal, so be ready to mention it if your supervisor asks about total time.
```

**Verify:** Check the new headline against the trail, one piece at a time. "21 and 22 of 24 help emails labeled correctly in two runs" matches Run 1 and Run 2. "About 10 minutes per run" matches the time line. The percentage and the "one confusion" are gone. The headline still leaves out the 15 minutes, and the tool says so. A one-line headline cannot carry everything, so the student adds the full cost (about 25 minutes per batch) to The evidence and the 2 wrong labels per run beside it. Her README row for Work Order 1 points to both runs, so her supervisor can retrace every number on the slide.

### Try It Yourself 12.3: The Outline, Problem-First 🛠️

A plumbing contractor's dispatcher ran a three-week pilot of an AI tool that drafts appointment-confirmation texts. The contractor has 2 dispatchers and sends about 150 confirmation texts a week. Writing one by hand takes about 3 minutes. The tool drafted 60 texts: 52 went out with light edits at about 1 minute each, 6 were rewritten, and 2 gave a wrong arrival window and were caught before sending. Customers' names and addresses were removed before any text went into the tool. The vendor quotes \$20 per dispatcher per month. The pilot did not time the 6 rewrites or record how customers responded. The dispatcher recommends extending the pilot one month, with a dispatcher checking every text.

**Predict:** Predict which part of the Presentation outline a chat assistant is most likely to get wrong: The evidence, The limits, or Questions you expect.

**Run:** Get a chat assistant to draft the Presentation outline for the dispatcher's five-minute talk to the owner, who decides whether to keep paying. Write your own prompt. A good result meets these criteria:

* It has the six parts in order, with the recommendation first.
* Every evidence line traces to the facts above, with none added, and counts stay counts.
* The limits name at least the two things the pilot did not measure.
* The ask is one action, with who decides.
* Each expected question says whether the evidence answers it.

Paste your prompt and the response into your prompt log, and score each criterion pass or fail with a quote or a count. Then fill `toolkit-lastname/presentation-outline-template.md` for the dispatcher, fixing every failure. That filled outline is the artifact, and it is the model for your project's outline.

**Explain:** Compare your run with the sample below. In 1-2 sentences, explain which criterion your prompt handled better or worse, and why.

Here is one reasonable prompt for the task. Send the prompt without the [Step] lines:

```text
[Step 1: name the speaker, the audience, and the decision]
I'm a dispatcher at a plumbing contractor. Draft a Presentation outline for a five-minute talk to the owner, who decides whether we keep paying for an AI tool that drafts appointment-confirmation texts.
[Step 2: fix the outline's six parts in order]
Use these sections in this order: Audience; The recommendation first; The evidence; The limits; The ask; Questions you expect.
[Step 3: hand over the recommendation and the evidence, with its source]
Recommendation: extend the pilot one month, with a dispatcher checking every text. Evidence, all from our three-week pilot log: 2 dispatchers; about 150 confirmation texts a week; about 3 minutes to write one by hand; 60 texts drafted; 52 sent with light edits at about 1 minute each; 6 rewritten; 2 gave a wrong arrival window and were caught before sending; customers' names and addresses were removed before any text went into the tool. Price: $20 per dispatcher per month (vendor quote). Not measured: minutes spent on the 6 rewrites, and how customers responded.
[Step 4: set the limits on what it may claim]
Use only these facts. Keep counts as counts, with no percentages. Under The limits, name what the log cannot support. Under Questions you expect, say for each one whether the evidence answers it.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
[...]
## 1. Audience
- The owner decides whether we keep paying for the tool. They are not a technical person and care about three things: cost, risk to customers, and dispatcher time.
[...]
- **Price:** $20 per dispatcher per month (vendor quote), so $40 a month for our 2 dispatchers.
[...]
## 4. The limits
What the log cannot support:
- **Rewrite time was not measured.** We do not know how many minutes the 6 rewrites took, so we cannot state a total time saved.
- **Customer response was not measured.** We do not know whether customers replied, confirmed, or were confused or annoyed by the texts.
- **The log cannot show a dollar saving.** Without rewrite time, any savings figure would be a guess.
- **Only 60 of roughly 450 texts were drafted by the tool.** (About 150 a week over three weeks.) We do not know how the tool would do on the rest.
- **The 2 wrong arrival windows were caught only because a dispatcher checked.** The log does not show what would have happened without the check, and it does not tell us how often errors would occur over a longer period.
[...]
## 6. Questions you expect
| Question | Does the evidence answer it? |
|---|---|
| Does it save time? | **Partly.** For the 52 light-edit texts, about 1 minute versus about 3 by hand. The 6 rewrites were not timed, so total savings are unknown. |
| What does it cost? | **Yes.** $20 per dispatcher per month (vendor quote). |
| Is it safe to send what it writes? | **Partly.** 2 texts had a wrong arrival window, both caught before sending. That is why every text needs a check. How often errors would occur long-term is not answered. |
| Is customer information protected? | **Yes, for the pilot.** Names and addresses were removed before any text went into the tool. |
[...]
```

The limits are the strongest part. Both unmeasured items are there, and "60 of roughly 450" is arithmetic the outline shows (about 150 a week over three weeks). The one sum it added, "\$40 a month for our 2 dispatchers," holds. Two lines go past the facts. The Audience line says the owner is "not a technical person" and cares about "three things," and the facts said nothing about the owner. And "Is customer information protected? **Yes, for the pilot.**" claims more than the log shows. The log says what went into the tool. It says nothing about what the vendor keeps, because nobody read the data policy. The honest answer is "Partly." The full response runs 644 words, which a five-minute talk can use as notes but not as a script.

### Quick Check 12.3 ✅

1. A slide reads: "The tool handled our tickets with near-perfect accuracy." The log says 40 drafts were checked: 31 sent with light edits, 7 rewritten, and 2 caught with an invented step. Rewrite the line from the counts, and say which part of the outline the 2 belong in as well.
2. Your stakeholder asks, "Will this pay for itself?" Your trail never timed the rewrites. Write the answer you give, and name the part of the outline where that gap already belonged.

---

## 12.4 Reflect: The Ethics Statement and the Toolkit

The project ends with three pieces of reflection: what you learned from the log, what the work owes the people it touches, and what you keep. Each one is written from your files, not from memory.

### Reflection From the Log

A reflection answers three questions: what AI did well, what it got wrong, and what you would do differently. Memory is a poor source for all three. Here is what a chat assistant wrote when the housing office student gave it no log:

```text
Write a 120-word reflection for my AI project: I used an AI tool to sort help emails for a university housing office's help desk. Cover what the AI did well, what it got wrong, and what I would do differently.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
For this project, I used an AI tool to sort incoming help emails for a university housing office's help desk. The AI performed well at identifying common categories, such as maintenance requests, roommate conflicts, and billing questions, and it processed large batches far faster than I could by hand. However, it struggled with emails that combined multiple issues or used vague, emotional language, and it sometimes marked urgent safety concerns as routine. It also misread housing-specific terms like "RA" and "move-in window." Next time, I would give the AI clearer category definitions and examples, add an urgent-priority flag, and have a staff member review uncertain or high-risk messages. Testing on a small sample first would help me catch errors early.

*I made up the specific examples (categories, errors), so swap in the ones from your actual project.*
```

Her categories were Wi-Fi, Account, Hardware, and Other. The draft's "maintenance requests, roommate conflicts, and billing questions" and its misread "RA" never happened, and its own last line admits it made them up. It also ran 137 words by a word counter, its note included, against a 120-word request. Now the same request, with the log excerpt pasted in:

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

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
The AI sorted emails more accurately than the inbox's keyword rules. It got 21 of 24 correct in Run 1 and 22 of 24 in Run 2, compared with 17 of 24 for the keywords, which sent seven emails to Other. In Run 1 it flagged one email as unsure. However, it made mistakes: it labeled Wi-Fi emails as Hardware in both runs (three times total), and in Run 2 it labeled an Account email as Other. Run 2 flagged nothing unsure despite two errors. Next time, I would keep my supervisor checking every label, and I would review the masking more carefully, since I missed a room number in email 17 on my first pass (caught by my supervisor).
```

Every count holds, including the total of three Wi-Fi emails labeled Hardware (two in Run 1, one in Run 2), and it runs exactly 120 words. Its sharpest line is one she might have missed: "Run 2 flagged nothing unsure despite two errors." That is a weakness of current AI worth naming in any presentation. The tool sorted 24 emails with 21 and then 22 right, and it can be wrong without warning. The last sentence is different in kind. "What I would do differently" is a decision, and the log cannot make it. The draft's choices are sensible, but she keeps them only if she means them. A full reflection also says what changed for the people doing the work. Here, sorting time turned into masking, checking, and logging time, and a person still checks every label: her supervisor during the pilot, and the student worker on shift after it.

### The Ethics Statement

Chapter 3 gave you five principles, the disclosure statement, and the privacy check. Chapter 7 gave you the paired prompt test, and Chapter 8 gave you the data policy reading, the Copyright Office's guidance, and the AI Use Policy. The **Ethics Statement** pulls them into one page for one project, in five sections, in this order:

* **Privacy:** what went into a tool, what did not, and why.
* **Ownership:** what you and the organization can claim, and the licenses involved.
* **Bias:** the paired prompt tests you ran, or the risk you named and why it was not tested.
* **Disclosure:** who was told that AI helped, where, and how.
* **Accountability:** who answers for the result.

It is not a promise of good intentions. Each line points to a file or a log entry a colleague could open. The housing office student listed her facts and asked for a draft:

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

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
[...]
**Privacy**
Before any email went into the tool, I removed residents' names and room numbers. On my first pass I missed one room number, and my supervisor caught it before the first run, so no identifying details were processed. I used the chat assistant on my university account, and I read its data policy on October 2: chats on university accounts are not used to train the model.

**Ownership**
I wrote the category definitions (Wi-Fi, Account, Hardware, Other) and the prompt. The tool wrote the labels for the 24 emails. The design of the sorting scheme is mine, while the individual label outputs came from the tool.

**Bias**
I did not run a paired prompt test, so I have not checked for differences in how the tool treats different groups of residents. Some residents write in Spanish, and I have not checked whether their emails land in Other more often than English-language emails. Until that check is done, this is a known gap and a possible source of unfair sorting.
[...]
**Accountability**
The student worker on shift checks every label before an email is forwarded, so a person reviews each tool decision. My supervisor approves the process, and I am responsible for the prompt, the category definitions, and the data preparation.
```

Most of it is faithful, and the Bias section names the gap honestly, which is what the section asks when no test was run. Three lines need her attention. "So no identifying details were processed" claims more than the facts: she removed names and room numbers, and an email can carry other identifiers, such as a phone number. Ownership says who wrote what but names no license, because she never gave it the tool's terms of use. And the last clause of Accountability, "I am responsible for the prompt, the category definitions, and the data preparation," is not in her facts. It may be true. It is still hers to write, because accountability is the one section a tool cannot answer for.

**Case: who answers when an AI tool is wrong.** In *Mata v. Avianca, Inc.*, No. 22-cv-1461 (S.D.N.Y. June 22, 2023, read October 21, 2026), two lawyers and their firm filed a court paper that cited opinions that did not exist. Its fake quotes and citations came from an AI chat tool. They kept standing by the fake opinions after the court questioned them. The judge wrote that "there is nothing inherently improper about using a reliable artificial intelligence tool for assistance." He also wrote that "existing rules impose a gatekeeping role on attorneys to ensure the accuracy of their filings." The court imposed a \$5,000 penalty and ordered letters to the client and to each judge falsely named as the author of a fake opinion. It is one federal trial court's order in one case. The rule it relied on first, Rule 11 of the Federal Rules of Civil Procedure, is about signing court papers, not about AI. That is the point for your Accountability section: it names a person or a role, never the tool. At Copperwind, it names the technician who sends each reply and the operations manager who signs the AI Use Policy.

### Try It Yourself 12.4: One Section, From Your Files 🛠️

**Predict:** Open `toolkit-lastname/ethics-statement-template.md` and pick the section your project is weakest on. Predict whether a chat assistant drafting that section would add a claim your files cannot support.

**Run:** Write that section yourself from your prompt log and your files, naming the file or log entry behind each claim. Then list your facts for a chat assistant and ask it to draft the same section in a fresh conversation. Mark each of its sentences Holds or Not in source against your files, and paste both versions into your prompt log. Your own section goes into `toolkit-lastname/ethics-statement-template.md`, and it is the artifact.

**Explain:** Was your prediction right? In 1-2 sentences, explain which sentence in that section you would never let a tool write for you, and why.

### Assembling the Toolkit

The **Toolkit** is your personal AI toolkit, with a README. It holds the Tool Survey, the prompt library v3, and the Requirements Sheet and Work Order templates. It also holds the Output Checklist and the Audit Report, the AI Use Policy, the Use Evaluation, the Selection Decision, and the Ethics Statement. It is the course deliverable, and it is built to be used on Monday.

| Item | Where you built it | Open it when |
| --- | --- | --- |
| Tool Survey | Chapter 10 | You are choosing a tool, or a tool's tier or policy changed |
| Prompt library v3 | Chapters 4-6 | A job repeats and a tested prompt already exists |
| Requirements Sheet and Work Order | Chapter 11 | A new job arrives, before any tool is named |
| Output Checklist and Audit Report | Chapters 5 and 7 | Any output is about to be used |
| AI Use Policy | Chapter 8 | You are unsure what may go into a tool |
| Use Evaluation and Selection Decision | Chapters 9 and 11 | Someone asks whether to adopt |
| Ethics Statement | Chapter 12 | A project is about to be shared or used |

The `toolkit-starter/` folder in this chapter's data pack holds a clean copy of every template, including the Refinement Log your library cards use and a starter prompt library. You copied it to `toolkit-lastname` in Try It Yourself 12.1, and every fill since then went into that copy. The starter stays clean for the next project. Your Comparison Matrices feed the Last tested line of each Tool Survey card. The README's most practical line is "Which tools I will use next week." On a home lab, that line might read: "A general assistant from my Tool Survey drafts the test plan for my VPN change. I check it with the Output Checklist."

### Try It Yourself 12.5: Next Week's Tools 🛠️

**Predict:** Predict how many tools from your Tool Survey you will use in the next seven days, and for which jobs.

**Run:** Open `toolkit-lastname/toolkit-readme-template.md`. Fill the "Which tools I will use next week" table: each tool from your survey, the job, and the Toolkit file you will open first. Then fill "What never goes into a tool" with two examples from your own work. Those README lines are the artifact.

**Explain:** Compare your count with your prediction. In 1-2 sentences, name a tool you left off the table and the Toolkit file that told you to leave it off.

### Quick Check 12.4 ✅

1. A student's Accountability section reads: "The AI tool is responsible for the accuracy of its outputs." Critique it using the court case in this section, and rewrite it for a home lab build checklist.
2. A Toolkit README lists ten files but gives no dates anywhere. Judge what a colleague cannot tell from it, and name the two lines you would add first.

---

## 12.5 Summary and Retrieval 💡

### Key Concepts

* The capstone delivers one AI solution for a real decision, through either of two equal options: the Copperwind capstone or your own IT project. Both use the same artifacts.
* The Requirements Sheet is the definition of done. A drafted sheet is a list of proposals you keep, rewrite, or cut, and the no-AI option is tested like any other.
* A Work Order sets the goal, the limits, and the checks, and the tool does the steps. ASK lines mark the facts you never gave, and every run is scored against the acceptance criteria.
* The Verification Trail lets a colleague retrace any result. Its README says where each piece lives and what a person checked, including where the checking stopped.
* The Presentation outline puts the recommendation first, ties every evidence line to the trail, and puts what the log cannot support under The limits.
* A reflection comes from the log. The Ethics Statement covers privacy, ownership, bias, disclosure, and accountability, and accountability always names a person.
* The Toolkit is what you keep: every template, your filled artifacts, and a README that names the tools you will use next week.

### Key Terms

See course glossary for full definitions

* capstone, stakeholder (Section 12.1)
* Verification Trail (Section 12.2)
* Ethics Statement, Toolkit (Section 12.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Name the five sections of the Ethics Statement in order, and say what the Bias section holds when no test was run.
2. List the six parts of the Presentation outline in order, and say where a claim the log cannot support belongs.
3. Name the pieces of the Verification Trail, and the one thing its README must say about each piece besides where it lives.
4. From Chapter 10: Name the six criteria of the Comparison Matrix in order, and the four things a fair test keeps the same for every tool.
5. From Chapter 8: Name the seven sections of the AI Use Policy in order, and the four kinds of rules.

---

## 12.6 Skills Lab 12A: The AI Application Project

**Goal:** Deliver an AI solution for one scenario, the Copperwind capstone or your own IT project, with its Verification Trail, a presentation to its stakeholder, an Ethics Statement, and the Toolkit you keep.

**Starter files:** Provided files in `assets/code/chapter-12/` from the course data pack: `skills-lab-12a-worksheet.md` (your answer file). The briefs are `capstone-brief-copperwind.txt` (Mei Lin's brief for the year-ahead recommendation) and `capstone-brief-own-project.txt` (what qualifies, the privacy rule, and the same artifacts for your own IT project). The `toolkit-starter/` folder holds one clean copy of every Toolkit template, including this chapter's four (`verification-trail-readme-template.md`, `ethics-statement-template.md`, `presentation-outline-template.md`, and `toolkit-readme-template.md`), plus a starter prompt library. Download the data pack from Canvas, extract it, and work at the extracted `cis137` root. Open each file in any text editor and never retype its contents. The Copperwind files are fictional, so you may paste them into a chat assistant once your privacy plan allows it. Files from your own project follow the privacy rule in its brief. You first met Copperwind in Chapter 1, and this lab gives you everything it needs, so you do not need any earlier file.

### Part 1: Foundation (Aligns with Objective 12.1)

Work in `skills-lab-12a-worksheet.md`, which has a space for every task below.

1. Copy `toolkit-starter/` into a folder named `toolkit-lastname`, if you have not already, and do every fill in this lab in that copy. Choose your option and read its brief in full. If you choose your own IT project, write the three lines its brief asks for: the job, the stakeholder by role, and what will never go into a tool. Get your instructor's approval before you start Part 2.
2. Before you send any prompt, write your privacy plan in two columns: what may go into a tool, and what stays out of every prompt. Give the reason for each item that stays out.
3. Fill `toolkit-lastname/requirements-sheet-template.md` for your project, naming no tool. Write each must-pass criterion so a person can check it with a count or a yes or no.
4. Fill `toolkit-lastname/tool-survey-card-template.md` for each tool you will consider, at least two, with every line that can change dated.

### Part 2: Application (Aligns with Objectives 12.1 and 12.2)

1. Write and run at least two Work Orders from `toolkit-lastname/work-order-template.md`. For the Copperwind option, choose two of Jobs A-D in the brief. Run each Work Order in a fresh conversation at least twice, and score each run against its acceptance criteria with counts.
2. Check each Work Order's best result with the checklist its acceptance criteria name. For any output that states facts, run the Accuracy Audit and fill `toolkit-lastname/audit-report-template.md`. When a run fails a criterion, change one thing, run again, and record it in `toolkit-lastname/refinement-log-template.md`.
3. Fill `toolkit-lastname/selection-decision-template.md` for each job, with a Decision of adopt, extend the pilot, decline, or no AI here. For the Copperwind option, decide Job E without putting it into any tool, and give your reasons. For your own project, name the part of the job that stays with a person, and why.
4. Fill `toolkit-lastname/verification-trail-readme-template.md` for your project: every piece, where it lives, and what a person checked. Complete "How to retrace one result" and "What nobody checked."

### Part 3: Extension (Aligns with Objectives 12.1, 12.2, and 12.3)

1. Fill `toolkit-lastname/presentation-outline-template.md` for your stakeholder (Mei Lin, for the Copperwind option), with every evidence line naming its Verification Trail file and log entry. Give the presentation in the format your instructor sets.
2. Test one claim from your presentation against your log, the way Fix It 12.1 did. Quote the claim and the log lines behind it, mark it Holds or not, and rewrite it from the counts if it fails.
3. Write a reflection of at most 200 words from your log. Name two things AI did well and two it got wrong, each with its log entry, one thing that changed for the people who do the work, and what you would do differently.
4. Write your Ethics Statement in `toolkit-lastname/ethics-statement-template.md`, all five sections, naming the file or log entry behind each claim.
5. Assemble your Toolkit in `toolkit-lastname`. Save your best Work Order prompt as a prompt card from `prompt-card-template.md`, and add it to `prompt-library-v2-starter.md` so your library holds it. Then fill `toolkit-readme-template.md`, including "Which tools I will use next week."

### Questions & Analysis 🤔

Answer both questions in the worksheet's final section. These answers carry significant rubric weight.

1. Quote the presentation claim you tested in Part 3 Task 2 and the prompt log entries behind it. Explain whether it held, and how the result changed The limits in your outline.
2. Quote the Decision line you are least sure of from your Selection Decisions, and the run counts behind it from your log. Judge whether that decision should stand, and name the Ethics Statement section that bears on it most.

**Submission:** Submit your completed worksheet as one file named `skills-lab-12a-lastname.md`. Keep every answer under its task heading, with your filled templates pasted into their sections. Include every prompt you sent, the tool and date, and every response you received, pasted exactly, with your Questions & Analysis answers clearly labeled at the end. Submit your Toolkit folder, `toolkit-lastname`, as a second deliverable (as a zip file if your course site asks for one).

### Rubric: Skills Lab 12A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria, five
levels from Mastery to Not Evident. The criteria are Technical
Accuracy and Efficiency, Output Quality, Documentation Quality, and
Analysis, Interpretation, and Response to QUESTION(s). The criteria
and levels are the same everywhere. Your instructor sets the point
values in your course. Check the syllabus and the Canvas rubric
attached to this lab for the values that apply to you.

---

## 12.7 Review Questions 🔄️

1. **Understand:** Explain to a teammate, in no more than three sentences, why a Verification Trail's README must say what a person checked and not only where each file lives.

2. **Apply:** A museum gift shop's manager wants a chat assistant to draft her weekly reorder notes from her sales notes. Write the Acceptance criteria and Review plan fields of the Work Order for this job.

3. **Analyze:** A community garden volunteer's slide says "AI wrote our watering schedule and saved us hours." Her log shows three runs, one schedule used after her edits, and no times recorded. Analyze which parts of the claim her log supports, and say where each unsupported part belongs in her Presentation outline.

4. **Evaluate:** A car dealership's service desk wants an AI tool to send customers their repair estimate by text, with no person reading the text first. Its pilot found 2 wrong totals in 80 drafts. Decide whether to adopt, extend the pilot, decline, or say no AI here. Defend your decision with the Accountability section of an Ethics Statement and the court case in Section 12.4, and name the one change that would most change your answer.

---

## Further Reading 📖

* [Mata v. Avianca, Inc., Opinion and Order on Sanctions (U.S. District Court, Southern District of New York)](https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0_3.pdf): The full order of June 22, 2023, from the case in Section 12.4. Its first page states the gatekeeping rule, and the conclusion lists the sanctions.
* [Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence): NIST's companion to the AI RMF for generative AI, published July 26, 2024. It names risks of generative AI and actions an organization can take, which makes it a strong source for an Ethics Statement.
* [Making Events Accessible: Checklist for Meetings, Conferences, Training, and Presentations (W3C Web Accessibility Initiative)](https://www.w3.org/WAI/teach-advocate/accessible-presentations/): A checklist for presenters, including describing visual information aloud and providing slides ahead of time.
* [Plain Language Guide Series (Digital.gov)](https://digital.gov/guides/plain-language): The U.S. government's guides to writing for a specific audience, under the Plain Writing Act of 2010. Use it on your outline before you present.

---

## Course Conclusion: Where You Go from Here

You started this course asking a chat assistant what it was. You finish it holding a Toolkit. It has a survey of the tools you tested, a prompt library with logs, and the templates that turn a problem into a Work Order. It has the checklists that test what comes back, a policy, an evaluation sheet, a decision record, and an Ethics Statement. Every piece is a file you can open next week, at school or on an IT project of your own.

The Toolkit carries the five habits of the human in the loop:

1. Keep a log. The prompt log and the Verification Trail.
2. Verify before you trust. The Output Checklist and the Accuracy Audit.
3. Protect what is not yours to share. The privacy plan, the AI Use Policy, and the Privacy section of the Ethics Statement.
4. Choose by criteria. The Requirements Sheet, the Comparison Matrix, and the Selection Decision.
5. Know when to say no. The no-AI option and the "no AI here" decision.

Mei Lin will walk into the owner's office with a recommendation she can defend, because every line traces to a run someone checked.

The certificate goes further from here. CIS144 focuses on agentic systems and AI-driven data analytics: tools that take actions and work with data. CIS218 focuses on designing, integrating, and deploying AI solutions. Both build on the seat you now hold. A tool that acts on its own still needs someone to write the order, set the checks, and answer for the result.
