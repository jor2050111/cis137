# Chapter 11: Matching AI Tools to Scenarios

Mei Lin's pilot ends this quarter. Before it does, she has to tell Copperwind's owner what the company adopts for the next year: which jobs get an AI tool, which tools, and under what rules. A Deskside technician has an answer ready before she asks. "We already have the pilot tool. Use it for everything." It is the fastest answer in the building, and it starts in the wrong place.

Most teams pick tools that way: the familiar tool first, the problem second. This chapter reverses the order. Chapter 10 gave you the fair test, the Comparison Matrix, and the Tool Survey, so you know what the tools on your list can do. Chapter 9 gave you the Use Evaluation and the pilot. Now artificial intelligence (AI) tools meet specific jobs. You will define the problem before you name a tool, direct a tool through a job with a written brief, and decide with a measured pilot. Sometimes the decision is "no AI here," and that is a finished answer, not a failure.

You will build three tools you keep: the Requirements Sheet, the Work Order, and the Selection Decision. Each one works on a Copperwind job and on your own IT project, such as a home lab, a club project, a course project, or a task at work. The Work Order is how you manage an AI assistant from the human-in-the-loop seat when it works through several steps for you. The Skills Lab hands you four of Mei Lin's scenarios: three that may suit a tool and one where the answer may be no.

## Module Overview 🧭

* **Estimated time:** 5-6 hours
* **Prerequisites:** Chapter 10 (the fair test, the Comparison Matrix, and the Tool Survey) and Chapter 9 (the Use Evaluation, the pilot, and the Memo). Also the five parts of a prompt and the Output Checklist from Part II, the Accuracy Audit from Chapter 7, the AI Use Policy from Chapter 8, and the prompt log from Chapter 1
* **Deliverables:** Skills Lab 11A deliverable (four scenario decisions, a Selection Decision, and a Memo to Mei Lin), Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **11.1 (Evaluate):** Judge whether a stated problem needs an AI tool at all, from a Requirements Sheet written before any tool is named (Sections 11.1, 11.3)
* **11.2 (Evaluate):** Justify the tool chosen for a scenario from the Tool Survey, with a Work Order that directs it through the job and acceptance criteria that validate the result (Sections 11.2-11.3)
* **11.3 (Evaluate):** Recommend adopt, extend the pilot, decline, or no AI here in a Selection Decision backed by a measured pilot (Section 11.4)

### This chapter aligns with the following Course Learning Outcomes

* **CLO 6 (Evaluate):** Select appropriate AI solutions to address specific problems.
* **CLO 3 (Apply):** Demonstrate effective prompting strategies to improve AI outputs.
* **CLO 1 (Evaluate):** Evaluate AI-generated responses for accuracy.

---

## 11.1 The Problem Before the Tool

Here is the technician's idea asked of a chat assistant, the way many tool choices start:

```text
What kind of AI tool is best for sorting the support tickets that land in my small IT company's inbox each morning? Answer in under 100 words.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
A large language model (LLM)-based classifier is your best fit. Unlike rigid rule-based filters, it reads the ticket's actual wording, so it can categorize (hardware, network, account access), assign urgency, and flag outages even when customers describe problems vaguely.
[...]
```

Count what the answer needed to know and never asked. How many tickets arrive? What do requesters type into them? Which tools does the company already approve, and what do those tools keep? Who reads the sorted result? The response asked none of that. It picked a type in its first sentence and, in the paragraph cut above, went on to name products, all in 84 words. Product names and prices from a tool's memory belong nowhere until you check them, and Chapter 10 says where they go then: on a dated Tool Survey card. The cut paragraph does end with good advice, a human review step for anything marked urgent. The answer may suit some company. It cannot be shown to suit yours, because it never learned what yours needs.

### The Requirements Sheet

A **Requirements Sheet** is a one-page definition of a job, written before any tool is named, so the problem can choose the tool. Its seven fields come in this order:

1. **The problem**, in one sentence.
2. **Who is affected**: the people who live with the problem and the people who use the result.
3. **Inputs**: what goes in, and what never goes in.
4. **Output required**: its shape, length, and audience.
5. **Must-pass criteria**: the checks the result cannot ship without.
6. **Constraints**: cost, privacy, time, and accessibility.
7. **The no-AI option**: what doing the job without AI costs.

Two fields do work that no earlier tool did. "What never goes in" brings the AI Use Policy section of the same name to the top of the job, before anyone pastes anything. The **no-AI option** is the way a person would do the job with no AI tool, priced in minutes, so every tool has a baseline to beat. If no tool beats it, the sheet has made the decision. Here is the sheet for Deskside's morning inbox, the first of Mei Lin's scenarios:

| Field | Deskside morning triage |
| --- | --- |
| The problem | Technicians open the morning's tickets in the order they arrived, so an urgent lockout can wait behind a printer question. |
| Who is affected | The 5 Deskside technicians, and every client waiting on a first reply inside the 30-minute target |
| Inputs | In: ticket subjects and first lines. Never: client names, requester names, signatures, or a password a requester typed |
| Output required | A table of ticket number, category, and urgency, for the technician on the morning shift |
| Must-pass criteria | Every ticket gets one of Deskside's six categories or "other." Urgency follows Deskside's rule: urgent means the person cannot work at all right now. Nothing is added. |
| Constraints | Cost: no new spending before the owner approves. Privacy: only a tool on the AI Use Policy's approved list. Time: done in a few minutes, before the first-reply clock matters. Accessibility: a plain table a screen reader can read |
| The no-AI option | A technician reads and sorts by hand, about 15 minutes a morning by Deskside's estimate, and no data leaves Copperwind |

The same sheet fits your own work. On a home lab project, the problem might read "My server rebuild steps live in my head, so a rebuild takes a whole weekend." The no-AI option there is writing the checklist yourself from your last rebuild notes, in about an hour.

### Scenario Alignment

**Scenario alignment** is matching what a scenario requires to what a tool does well and is allowed to do, line by line, from the Requirements Sheet and the Tool Survey. Each line of the sheet points to a place on a Tool Survey card:

| Requirements Sheet line | Where the Tool Survey card answers it |
| --- | --- |
| Inputs: what never goes in | Data policy (what it keeps, and whether it trains on your input) |
| Output required | Last tested (did it produce this shape on your task?) |
| Constraints: cost | Tier and cost, with the date checked |
| Constraints: privacy | Data policy, plus the AI Use Policy's Approved tools section |
| Constraints: accessibility | Access and Notes, plus the accessibility column of its Comparison Matrix |
| Constraints: time | Last tested, until your own pilot gives you minutes |

Alignment can end with no match. When every candidate fails a must-pass line, or the no-AI option beats them all on cost and risk, the aligned answer is no AI here.

### Try It Yourself 11.1: A Requirements Sheet Before Any Tool 🛠️

**Predict:** Pick one job from your own IT project, such as documenting a home lab rebuild, writing a club's setup guide for new members, or planning a ticket system move at work. Keep anything private out of it. Predict which of the seven fields will be hardest to fill without naming a tool.

**Run:** Fill `requirements-sheet-template.md` from this chapter's data pack for that job, all seven fields, without naming a tool anywhere on the sheet. Price the no-AI option in minutes. Next to each Constraints line, write the Tool Survey card field you will check it against. The filled Requirements Sheet is the artifact you keep.

**Explain:** Was your prediction right? In 1-2 sentences, say what made that field hard, and whether pricing the no-AI option changed your view of the job.

### Quick Check 11.1 ✅

1. A city animal shelter's volunteer coordinator wants "an AI tool" to answer adoption questions by email. Write the Problem field and both columns of the Inputs field of her Requirements Sheet.
2. A plumbing contractor's office manager says the right tool is "the one my nephew uses." The job handles customers' home addresses. Using scenario alignment, name the two Tool Survey card fields you would check first, and justify each in one sentence.

---

## 11.2 The Work Order: Directing a Tool Through a Job

A one-line prompt suits a one-step job. Many IT jobs have several steps: plan the checks, draft them, check the draft, and fix what failed. Some tools can carry several of those steps on their own. An **agent-style tool** is an AI tool that works through several steps of a job on your behalf, such as reading your files, drafting, and revising. A person sets the goal and accepts or rejects the result. Chapter 9 defined an agent as a system that takes actions toward a goal. This chapter puts you in the manager's seat, not the builder's.

The brief you hand such a tool is a **Work Order**. Its eight fields come in this order:

1. **Goal:** what the finished job does, and for whom.
2. **Scope:** what the tool may touch, and what it may not.
3. **Inputs:** what you paste or upload, after your privacy check.
4. **Deliverable and format:** a runbook, a test plan, a checklist, configuration notes, or a summary, with its shape and length.
5. **Acceptance criteria:** the must-pass checks, with the checklist that runs them.
6. **Constraints:** what the tool must never do, and what it must ask before doing.
7. **Review plan:** who checks what, and when.
8. **Log:** every prompt, run, and decision, in the prompt log.

**Acceptance criteria** are the must-pass checks a deliverable has to meet before a person accepts it, each paired with the checklist that runs it: the Output Checklist or the Accuracy Audit. They come from the Requirements Sheet's must-pass criteria. The five parts of a prompt sit inside the Work Order. Goal holds the Task, Inputs holds the Context, Deliverable and format holds the Format, and the Constraints field holds the Constraints. A Role line can open the Goal when the voice matters.

The same Work Order governs code and configuration jobs on your own IT projects, such as a script or a router change an assistant drafts for you. This book prints no code and no configuration syntax, so its Work Orders ask for runbooks, test plans, checklists, configuration notes, and summaries in plain words. Reviewing code or configuration that a tool wrote takes methods of its own, and those belong to CIS144 and CIS218.

### A Work Order With a Checkpoint

Network Ops is moving Copperwind's clients to a new VPN app next month, and Deskside needs a test plan to run with each client office afterward. The Work Order's last line tells the tool to stop after its plan. That stop is a checkpoint, a point where the tool waits for a person's approval before it does the work. Send the prompt without the [Step] lines:

```text
[Step 1: state the goal, so the tool knows what done means]
Work Order. Goal: a test plan our help desk technicians will run with each client office after our network team moves the clients to a new VPN app next month.
[Step 2: fence the scope and hand over the facts]
Scope: use only the facts below, and do not describe the VPN app's settings or menus, because I have not given them to you. Inputs: Technicians work with the client employee over a phone call. Technicians do not have admin rights on client laptops. If a check fails, the help desk does not fix the connection. It sends the ticket to the network team, who fix VPN problems. The employee needs the shared drive and email to work over the VPN.
[Step 3: set the deliverable and the checks it must pass]
Deliverable and format: a numbered list of checks in plain language, each with the expected result and what to do if it fails, under 250 words, with no commands and no configuration settings. Acceptance criteria: every check can be done without admin rights; every failed check routes to the network team; no step names a setting or menu of the VPN app; under 250 words.
[Step 4: set the limits and name the reviewer]
Constraints: never invent a feature of the VPN app, and ask before adding any check that needs admin rights. Review plan: a network team technician reads the plan before anyone uses it. Log: I keep every prompt and response in my prompt log.
[Step 5: make the tool stop at a checkpoint]
First step: reply only with your plan (the checks you intend to include, one line each) and any questions. Do not write the test plan until I approve.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
**Planned checks (one line each):**

[...]
4. Employee opens a file from the shared drive and saves a small change.
[...]
7. Every failure: tech records what the employee saw and which check failed, then sends the ticket to the network team (no troubleshooting by help desk).
[...]
2. Should the disconnect/reconnect check (6) stay in? It assumes the employee can disconnect and reconnect without admin rights, which I can't confirm from your facts. If it needs admin rights, I'll drop it unless you approve it.
[...]
I'll wait for your approval before writing the plan.
```

The plan is the cheapest place to catch a problem, because nothing has been written yet. The tool asked five questions, and the one shown above shows it read the Constraints: it offered to drop a check instead of guessing about admin rights. Read the plan against the Work Order before you approve it. The author's approval, sent in the same conversation, missed something:

```text
Approved, with one change: add a check that the employee can open a file on the shared drive, not only see the folder. Write the test plan now. Then check it against each acceptance criterion and mark each one pass or fail.
```

Planned check 4 already had the employee open a file. An approval written without a close read of the plan adds nothing, and here it also left the tool's five questions unanswered. Here is part of what came back:

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
# VPN Move Test Plan
[...]
4. **Open a file.** The employee opens a file from a shared drive folder. Expected: the file opens and is readable. If not: send the ticket to the network team.
5. **Save a change.** The employee changes a test file on the shared drive and saves it. Expected: it saves with no error. If not: send the ticket to the network team.
[...]
*(About 190 words.)*
[...]
| Criterion | Result | Basis |
|---|---|---|
| Every check can be done without admin rights | **Pass** | Each check only has the employee sign in, read, open, save, or send. Nothing needs admin rights. |
[...]
| Under 250 words | **Pass** | About 190 words. |
[...]
- **I dropped the disconnect/reconnect check.** I can't confirm it works without admin rights, and you asked me to ask before adding anything that needs them. Tell me if you want it back.
[...]
```

The tool marked all four criteria Pass. A self-check is a claim, so run the review plan on it. A word counter puts the test plan at 220 words with its title, not "about 190." The criterion still passes, but the evidence the tool gave for it was wrong. Check 5 has the employee change and save a file on the client's shared drive. The Scope field never said whether a check may change client files. The plan said so in check 4, and the approval let it through. The next version of the Work Order closes that gap with one line: the checks may open files and may not change them. The tool passed its own test, and the person's review still found two things to fix. That is why the Review plan names a person. The same eight fields direct a tool on your own project. Here is a Work Order for a home lab server rebuild:

| Field | Home lab server build checklist |
| --- | --- |
| Goal | A build checklist I can follow to rebuild my home lab server in one evening |
| Scope | May use my rebuild notes. May not suggest buying hardware or changing my home router |
| Inputs | My notes from the last rebuild, with every password and network address removed |
| Deliverable and format | A numbered checklist, one action per line, with a check at the end of each stage, under 300 words, in plain words with no commands |
| Acceptance criteria | Every step comes from my notes (Accuracy Audit: no claim Not in source). Every stage ends with a check (Output Checklist: right shape). Under 300 words |
| Constraints | Never include a password or an address. Ask before adding a step my notes do not have |
| Review plan | I read the plan before the draft, then follow the checklist on a test rebuild and mark each step |
| Log | Every prompt and response in my prompt log |

### Try It Yourself 11.2: A Work Order for Your Own Project 🛠️

**Predict:** Choose a job with several steps from your own IT project: a runbook, a test plan, a build checklist, configuration notes in plain words, or a migration plan. Predict which acceptance criterion the tool's first draft will fail.

**Run:** Fill `work-order-template.md` for the job, all eight fields. End it with the checkpoint line from the VPN example, and send it in a fresh conversation. Read the plan against your Work Order before you approve it or change it. Then score the deliverable against every acceptance criterion yourself, with a count or a quote, and paste every turn into your prompt log. The filled Work Order and its log entries are the artifacts you keep.

**Explain:** Was your prediction right? In 1-2 sentences, say whether the tool's own claims about its work, if it made any, matched your check.

### Quick Check 11.2 ✅

1. A museum gift shop manager types "Make our holiday inventory checklist." Rewrite the request as a Work Order's Goal, Scope, and two acceptance criteria, each with the checklist that runs it.
2. At its checkpoint, a university housing office's tool asks, "Should I include the guest policy?" Decide which Work Order field should have answered the question, and write the line.
3. Apply the review plan to the self-check line "Every check can be done without admin rights: Pass." Name what the network team reviewer should check, and choose the check in the shown test plan most likely to need a closer look.

---

## 11.3 Five Scenarios, Five Decisions

Mei Lin's list holds five jobs: the morning inbox, the Monday stand-up notes, the owner's data question, Priya Sharma's next flyer, and a client's disputed invoice. Each one gets a Requirements Sheet first, then a tool or no tool, then a measured result. This section runs short versions of each, and the Skills Lab runs the full files. Where a short version would answer a lab task, a cover story stands in.

### Inbox Triage

Sorting is the pattern work at volume that Chapter 9 found AI strong at, and the triage sheet in Section 11.1 asks for nothing a general assistant on the approved list cannot do. The Work Order's fields fold into one prompt. The eight tickets were written for this chapter, with no identifiers:

```text
You are sorting a small IT help desk's morning inbox. Put each ticket in one category: password reset, VPN connection failure, printer offline, new-hire device setup, slow laptop, shared mailbox access, or other. Then mark it urgent or routine. Urgent means the person cannot work at all right now. Answer as a table with three columns: ticket number, category, urgency. Add nothing else.

1. "Locked out after three tries, can't get into anything, and I have a client at 9."
2. "The front desk printer shows offline again."
3. "New paralegal starts Monday and needs a laptop ready."
4. "VPN keeps dropping every ten minutes, then comes back."
5. "Can I get access to the billing@ mailbox? My manager said OK."
6. "Laptop takes 15 minutes to boot. It's been like this all week."
7. "Nobody in our office can reach the internet."
8. "Can you send me last month's invoice?"
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
| Ticket | Category | Urgency |
|---|---|---|
| 1 | Password reset | Urgent |
| 2 | Printer offline | Routine |
| 3 | New-hire device setup | Routine |
| 4 | VPN connection failure | Routine |
| 5 | Shared mailbox access | Routine |
| 6 | Slow laptop | Routine |
| 7 | Other | Urgent |
| 8 | Other | Routine |
```

Score it against a key a technician wrote before the run, because the person's sort is the standard. Categories match on 8 of 8 tickets, and urgency on 8 of 8. Ticket 7 has no category of its own, so Other is right, and an office with no internet is urgent. Ticket 4 is the judgment call. The VPN drops but comes back, so the person can still work, and Deskside's rule makes it routine. One run is a lead, not a result, and Section 11.4 runs the pilot.

### Try It Yourself 11.3: The Stand-Up Summary, Problem-First 🛠️

**Predict:** Open `monday-standup-notes.txt` from this chapter's data pack. Mei Lin missed the meeting. Predict which item a chat assistant is most likely to get wrong in a summary for her: a number, an owner, or an item that needs her answer.

**Run:** Write a Work Order for the summary in `work-order-template.md`, then turn it into your own prompt and send it with the notes in a fresh conversation. The notes are fictional, so you may paste them. A good result meets these criteria:

* Four labeled parts: decisions, open problems, actions with their owners, and what needs Mei Lin's answer.
* Every number matches the notes.
* No owner is invented. An action with no owner says so.
* Nothing is added: no advice or cause the notes do not hold.
* It stays under 120 words.

Paste your prompt and the response into your prompt log, and score each criterion pass or fail with a quote or a count. Your Work Order and its scored result are the artifacts you keep. On your own project, the same Work Order summarizes a club's or a project team's meeting notes.

**Explain:** Compare your run with the sample below. In 1-2 sentences, explain which criterion your prompt handled better or worse, and why.

Here is one reasonable prompt for the task. The full text of `monday-standup-notes.txt` followed it in the same message. Send the prompt without the [Step] lines:

```text
[Step 1: name the reader and the job]
Summarize the stand-up notes below for Mei Lin, who leads our help desk's AI pilot and missed the meeting.
[Step 2: set the deliverable's shape and length]
Use four labeled bullets: Decisions, Open problems, Actions (each with its owner as the notes name it), and Needs your answer. Keep it under 120 words.
[Step 3: write the acceptance criteria as instructions]
Use only what the notes say, and keep every number exactly as written. If the notes name no owner for an action, write "owner not named."
[Step 4: forbid what a summary tends to add]
Do not add advice, causes, or next steps the notes do not contain.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
- **Decisions:** VPN tickets keep the routing rule: Deskside sends the first reply, and Network Ops fixes the connection. Shared mailbox requests still need the manager's written approval, with no exceptions.
- **Open problems:** Printer offline tickets keep coming from the same medical office; Technician B thinks the printer needs replacing, not decided. Two first replies missed the 30-minute target, both Friday afternoon (158 tickets closed last week).
- **Actions:** Technician D: update the new-hire laptop checklist by Thursday. Asking the operations manager whether the AI Use Policy covers pasting ticket text into the pilot tool: owner not named.
- **Needs your answer:** Technician A asks whether the pilot tool stays after this quarter.
```

All five criteria pass. The four parts are there, and 158, two, and 30 minutes match the notes. The policy question carries "owner not named," nothing is added, and the summary runs 114 words. One placement is a judgment call. The unowned policy question sits under Actions, but someone has to assign it, and that someone is probably Mei Lin. A reader could defend either bullet. The tool also left out the next stand-up time, a fair cut for this reader.

### The Data Question

The owner asked which kind of ticket takes the most technician time. Copperwind's answer lives in `deskside-tickets.csv`, a synthetic sample of 80 of the four weeks' tickets in six columns, with a client type but no client names. The Requirements Sheet's must-pass line is strict: every total matches the file. Its Inputs line lets the table go into the chat assistant Copperwind already uses, which is on the approved list, because the table holds no names. Here is a short Work Order (four of the eight fields), as sent. The table's 81 lines followed it, and the cut below marks where:

```text
Work Order. Goal: answer the owner's question: which ticket category took the most technician time over these four weeks? Tool: the chat assistant we already use. Deliverable: a table of each category's total handle minutes, largest first, then one sentence naming the category that took the most time. Acceptance criteria: every total matches the ticket table below exactly. Constraints: use only the table.

ticket_id,week,category,client_type,first_reply_minutes,handle_minutes
DS-001,1,printer offline,medical office,9,13
[...]
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
| Rank | Category | Tickets | Total handle minutes |
|---|---|---|---|
| 1 | new-hire device setup | 8 | 552 |
| 2 | VPN connection failure | 14 | 365 |
| 3 | slow laptop | 10 | 322 |
| 4 | printer offline | 15 | 284 |
| 5 | password reset | 21 | 227 |
| 6 | shared mailbox access | 12 | 159 |

The 80 tickets are all accounted for, and the totals add up to 1,909 minutes.

New-hire device setup took the most technician time over the four weeks, at 552 handle minutes, even though it had only 8 tickets.
```

Run the Accuracy Audit against the file. Sorting the table by category in a spreadsheet and adding each group gives the same six totals, the same ticket counts, and 1,909 minutes in all. That is 6 totals checked and 6 that hold. The tool also caught the point the owner needs: password reset has the most tickets, and new-hire setup takes the most time. The spreadsheet sort is the no-AI option and the check at once, so the tool saved the writing, not the counting. A second model in the author's test setup returned the same six totals. Now run the cost test. The counting is a tie, because a person sorts the file either way, so review time decides. If writing two sentences for the owner takes less time than reading and checking the tool's answer, the no-AI option wins this job.

!!! note "Tool check (verified October 2026)"
    Where the core roster tools take a table or a file, read on each vendor's own page on October 21, 2026. ChatGPT (OpenAI, "Uploading files and audio to ChatGPT"): spreadsheet uploads (XLSX, XLS, CSV, TSV) on Free and paid plans. CSV files and spreadsheets have "a size limit of approximately 50 MB, depending on the size of each row." Uploads are capped at 80 files every 3 hours, and "Free users are limited to 3 file uploads per day." Gemini (Google, "Upload & analyze files in Gemini Apps"): documents and spreadsheets, up to 10 files in one prompt and up to 100 MB for most file types, with rolling limits. The page warns that a file too large may get a response that "misses connections or details." Microsoft Copilot Chat (Microsoft Learn, "Frequently asked questions about Microsoft Copilot Chat," updated October 19, 2026): uploads of Word docs, Excel files, and PDFs, under "standard access and file upload limits." That page states no size. Uploaded files are stored in the user's OneDrive for Business and, under enterprise data protection, are not used to train the model. Copilot Chat is the version for work or school accounts. The personal app follows different terms (Chapter 10's Tool check). Limits change, so check the page before a lab that needs an upload.

### Fix It 11.1: Three Quick Replies 🔧

A Deskside technician has three tickets waiting before 9 a.m. He opens the free chat assistant he uses at home, because it is fast, and writes a short Work Order in a hurry (three of the eight fields, on purpose). It has no Tool line, since a tool needs no telling which tool it is. Both runs below came from the author's test setup, so neither one can test a switch away from his home tool.

**Symptom:** Here is his Work Order:

```text
Work Order. Goal: first replies to the three help desk tickets below. Deliverable: three replies, each under 80 words, signed "Deskside Support." Acceptance criteria: each reply is ready to send with no blanks, promises no fix time, and repeats the details the client gave so they know we read the ticket.

Ticket 1, from Dana at a physical therapy office, 602-555-0131: "The front desk printer won't print Mr. Hal Benton's home exercise sheet, and he's waiting at the desk."
Ticket 2, from Marcus at a law office: "My email keeps asking for my password after the update."
Ticket 3, from Priscilla at a nonprofit: "Can I get access to the volunteers@ shared mailbox? My director approved it in the email below."
```

Here is the response it gave (captured from a chat assistant, October 2026):

```text
**Ticket 1: Dana**

Hi Dana,

We got your ticket: the front desk printer won't print Mr. Hal Benton's home exercise sheet, and he's waiting at the desk. We're looking at it now and will call you at 602-555-0131. In the meantime, if another printer in the office is available, try sending the sheet there so he isn't kept waiting.

Deskside Support
[...]
```

Every acceptance criterion in his Work Order passes. Each reply runs under 80 words (58, 61, and 55 by a word counter), is ready to send, promises no fix time, and repeats the client's details.

**Diagnose:** Before you touch the Work Order, name the decision he made before anyone defined the problem. Then read reply 1 and list what it repeats that never needed to leave the client's office.

**Repair:** He chose the tool first and pasted what he had. No Requirements Sheet existed, so nobody wrote down what never goes in. Ticket 1 came from a physical therapy office and named a patient, the kind of client Chapter 8 flagged as a HIPAA touchpoint. Any AI Use Policy built in Chapter 8 lists a patient's name and a requester's direct line under What never goes in. Reply 1 proves the data went in. It repeats "Mr. Hal Benton's home exercise sheet" and says it "will call you at 602-555-0131," which the criterion invited, because it said to repeat the client's details. The repair is to write the Requirements Sheet first and let it choose. Its privacy constraint points away from his home tool to the pilot tool on the approved list. That switch belongs to the Selection Decision, and this run cannot test it. Its Inputs line sets the one change in the prompt: the ticket text, with names and contact details removed. Every other word of the Work Order stays the same:

```text
Work Order. Goal: first replies to the three help desk tickets below. Deliverable: three replies, each under 80 words, signed "Deskside Support." Acceptance criteria: each reply is ready to send with no blanks, promises no fix time, and repeats the details the client gave so they know we read the ticket.

Ticket 1, from a physical therapy office: "The front desk printer won't print a patient's home exercise sheet, and the patient is waiting at the desk."
Ticket 2, from a law office: "My email keeps asking for my password after the update."
Ticket 3, from a nonprofit: "Can I get access to the volunteers@ shared mailbox? My director approved it in the email below."
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
**Ticket 1: Physical therapy office**

Hello,

Thank you for reaching out. We understand the front desk printer won't print a patient's home exercise sheet, and the patient is waiting at the desk. We're looking at this now as a priority. In the meantime, if possible, please try printing from another computer or send the sheet to a different printer. Please reply with any error message you see.

Deskside Support
[...]
```

**Verify:** Run the Work Order's criteria again, and add the sheet's must-pass line: no patient, requester, or contact detail in any reply. All three replies stay under 80 words (64, 59, and 56), carry no blanks, and promise no fix time, and none holds a name or a phone number. Then run the Output Checklist, because the sheet does not replace it. Both versions of reply 1 add printing advice no one gave ("please try printing from another computer" here), so "Nothing added?" fails in each. The repair fixed what went in. The next Work Order needs "nothing added" as an acceptance criterion, which is a refinement-loop change for its own log row.

### The Flyer Image

Priya's flyer request stays for the Skills Lab, so a community garden stands in here. Its coordinator wants a flyer for the spring workday. Here is the request, sent before anyone wrote a Requirements Sheet:

```text
Write a prompt I can paste into an image generator to make the flyer for our community garden's spring workday: Saturday, March 7, from 8 to 11 a.m., at the garden at 5th Street and Palm Lane. Bring gloves and water. Tools are provided.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

````text
[...]
Text to include, spelled exactly:
Headline: "Spring Workday at the Community Garden"
Details:
"Saturday, March 7"
"8-11 a.m."
"5th Street & Palm Lane"
"Bring gloves and water. Tools provided!"
[...]
A few tips:
[...]
- Double-check the date: March 7 falls on a Saturday in 2026, but in 2027 it's a Sunday. Make sure the day and date match the year of your event.
````

The image prompt asks the generator to draw five lines of text, and all four details are among them. Chapter 3 showed that generators often produce letters that look like words and are not. A later tip in the same response, cut above (log Prompt 16), says generators often misspell text and suggests making the art without text and adding the words in a document. That is the better split. The cut part of the image prompt also asks for "a few diverse neighbors," which needs Chapter 3's face check, and Priya's brief bans real-looking faces. Its date tip holds, too: March 7 is a Saturday in 2026 and a Sunday in 2027, so the flyer needs its year. A Requirements Sheet written first would have settled the split. If the flyer will also go out by email, as Priya's does, some readers will use a screen reader. For the emailed version, WCAG 2.2 success criterion 1.4.5, Images of Text, asks for real text wherever the technology allows it (W3C Recommendation, December 12, 2024, read October 21, 2026). The W3C's own summary is "Use text instead of pictures of text." So the image generator makes the picture only, with no text, and the words go into the document as real text, with alt text and a disclosure line. On your own project, the same split serves a club's event flyer.

### When the Answer May Be No

The disputed invoice is the Skills Lab's fourth scenario, so this section works a different case. Three tests decide whether a job goes to any AI tool:

* **The input test:** must something from "What never goes in" go in for the job to work?
* **The decision test:** does the output commit someone to a decision that a tool cannot answer for?
* **The cost test:** does the no-AI option beat every candidate on time and risk?

One yes can sometimes be fixed. You remove the names, or a person makes the decision and the tool drafts around it. A fix stops working when removing the forbidden input removes the job, or when the decision the person must make is the whole job. When the yes answers stack up and no fix remains, the answer is no AI here. That differs from "decline." Decline says this tool failed this job. No AI here says this job should not go to any AI tool, and it names the reasons, so the next person with a shiny tool can read them. A worked case shows the tests in use. A plumbing contractor's office gets a warranty claim: a customer's photos of a leaking water heater the company installed, plus the payment record for the job. The office manager asks whether a tool could decide the claim.

| Test | Yes or no | Reason |
| --- | --- | --- |
| The input test | Yes | The claim rests on the photos of the customer's home and the payment record |
| The decision test | Yes | Approving the claim commits the company to a repair at its own cost |
| The cost test | Yes | A person reads one claim against the warranty terms and the install record in about 15 minutes |

* **Decision:** no AI here.
* **Why:** Removing the photos and the payment record removes the evidence the claim rests on, and the approval is the whole job. A tool may draft a generic "claim received" notice with no customer details, as a separate job.

### Try It Yourself 11.4: Where the Answer Is No 🛠️

**Predict:** Pick a job from your own work or IT project that involves someone's account, payment, or personal details. If you have none to share, use this one. A car dealership's service desk gets an email from a customer disputing a repair charge, with the card number and a phone number in it. Predict which of the three tests will decide it.

**Run:** Fill the Inputs, Constraints, and no-AI option fields of `requirements-sheet-template.md` for the job. Run the three tests in writing, with a yes or no and one reason each. Then fill the Decision, Why, and Rules that apply fields of `selection-decision-template.md`. The Requirements Sheet lines and the Selection Decision lines are the artifacts you keep.

**Explain:** Was your prediction right? In 1-2 sentences, explain whether any slice of the job could still go to a tool, and what would have to be true first.

Here is where the five scenarios stand after this section's runs:

| Scenario | The sheet line that decided it | Tool, by type | Measured result |
| --- | --- | --- | --- |
| Inbox triage | Must-pass: Deskside's urgency rule | A general assistant on the approved list | 8 of 8 categories and 8 of 8 urgency, one run |
| Stand-up summary | Must-pass: no owner invented | A general assistant | 5 of 5 criteria, 114 words |
| Data question | Must-pass: every total matches the file | A general assistant, or no AI if review takes longer than writing (the cost test is close) | 6 of 6 totals hold |
| Flyer | Output required: readable by a screen reader, facts exact | An image generator for the picture only, and the document for the words | The first image prompt asked for 5 lines of drawn text |
| Plumbing warranty claim | Inputs: photos and a payment record | None | No AI here, with three yes answers |
| Disputed invoice | Decided by your three tests | Decided in Skills Lab 11A | Decided in Skills Lab 11A |
| Your IT project | The line you wrote in Try It Yourself 11.1 | Your choice, from your Tool Survey | Your counts |

### Quick Check 11.3 ✅

1. A small accounting firm wants a chat assistant to total each client's deductible expenses from pasted bank statements. Run the three tests, and decide whether the job gets a tool, a tool with a fix, or no AI here.
2. A car dealership's service desk wants an image generator to make a coupon flyer with three prices on it. Write the acceptance criterion its image prompt must carry, and say where the prices go instead.

---

## 11.4 The Pilot and the Selection Decision

One good run is a lead. The pilot from Chapter 9 turns it into evidence: the same Work Order, several fresh runs, scored with counts and minutes. The triage prompt from Section 11.3 ran three times in Tool A and three times in Tool B, each a fresh conversation, the fair test from Chapter 10. Here is one of Tool B's runs:

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
| Ticket | Category | Urgency |
|---|---|---|
| 1 | Password reset | Urgent |
| 2 | Printer offline | Routine |
| 3 | New-hire device setup | Routine |
| 4 | VPN connection failure | Urgent |
| 5 | Shared mailbox access | Routine |
| 6 | Slow laptop | Routine |
| 7 | Other | Urgent |
| 8 | Other | Routine |
```

| Candidate | Run | Categories matching the key | Urgency matching the key |
| --- | --- | --- | --- |
| Tool A | 1 | 8 of 8 | 8 of 8 |
| Tool A | 2 | 8 of 8 | 8 of 8 |
| Tool A | 3 | 8 of 8 | 8 of 8 |
| Tool B | 1 | 8 of 8 | 7 of 8 (ticket 4 marked urgent) |
| Tool B | 2 | 8 of 8 | 7 of 8 (ticket 4 marked urgent) |
| Tool B | 3 | 8 of 8 | 7 of 8 (ticket 4 marked urgent) |

Both tools put every ticket in the right category in all six runs. The difference is one ticket. Tool B marked the dropping VPN urgent every time, and the person on that ticket can still work. A miss that repeats is easier to manage than a random one, because the reviewer knows where to look. It also points the cheaper way: a routine ticket flagged urgent costs a few minutes, and an urgent ticket marked routine can miss the 30-minute target. The pilot is still small. Three runs of eight tickets is 24 sorts per tool, on tickets written for this chapter, not a real morning. The author's runs did not time a technician's review, so review minutes are missing.

!!! note "Tool check (verified October 2026)"
    Tool A and Tool B in this section are two models from one vendor, run through the textbook author's test setup, not two chat apps. Tools from different vendors on your course roster may differ more than these two did. Your syllabus names the roster.

### The Selection Decision

A **Selection Decision** is the record of which tool a job gets, or whether it gets one at all, backed by a measured pilot. Its seven fields come in this order: Requirements Sheet, Candidates, Pilot, Use Evaluation, Decision, Why, and Rules that apply. The Decision is one of four: adopt, extend the pilot, decline, or no AI here. The Why is two sentences a colleague could check. Here it is for the morning inbox:

| Field | Deskside morning triage |
| --- | --- |
| Requirements Sheet | The triage sheet in Section 11.1, attached |
| Candidates | Tool A and Tool B from the Tool Survey, and the no-AI option (a technician sorts by hand, about 15 minutes) |
| Pilot | The triage prompt, 3 fresh runs per tool on 8 chapter tickets, scored against a technician's key. Tool A: 8 of 8 categories and 8 of 8 urgency in every run. Tool B: 8 of 8 and 7 of 8 in every run |
| Use Evaluation | Cost: missing, since no price was checked for either tool. Time saved: missing, since review minutes were not timed. Error cost: an urgent ticket marked routine can miss the 30-minute target. Risk: ticket text going into a tool. Workforce impact: technicians keep the first read and every reply |
| Decision | Extend the pilot |
| Why | Tool A matched the key in all 3 runs, but 8 written tickets are not a real morning, and no review was timed. A one-week pilot on real mornings with names removed, with review minutes timed, decides between Tool A and the no-AI option. |
| Rules that apply | What never goes in (names, signatures, and typed passwords). Approved tools (Tool A must be on the list). Review before use (a technician reads every sorted table) |

The Decision field is where "no AI here" sits beside adopt, extend, and decline, as an equal outcome. On your home lab project, a Selection Decision might read "Decision: adopt for drafting the checklist. Why: three runs each passed all three acceptance criteria, and reviewing a draft took less time than writing the checklist from notes." Every number in it would come from your own log. The Selection Decision also feeds the Memo from Chapter 9. Its Decision becomes the Memo's first sentence, and its Use Evaluation lines become the factor paragraphs. Its missing numbers go under what we do not know. This goes in your Toolkit: the Requirements Sheet, the Work Order, and the Selection Decision templates are the three tools from this chapter you will use on every job that follows.

### Try It Yourself 11.5: Three Runs and a Decision 🛠️

**Predict:** Take a Work Order you wrote in this chapter, from Try It Yourself 11.2 or 11.3. Predict how many of three fresh runs will pass every acceptance criterion.

**Run:** Send the Work Order three times, each in a fresh conversation, in one tool or two from your roster. Score each run against every acceptance criterion, and time your review of each run in minutes. Then fill `selection-decision-template.md`, with a Decision and a Why a colleague could check. The filled Selection Decision is the artifact you keep.

**Explain:** Was your prediction right? In 1-2 sentences, name the number in your pilot that decided your Decision.

### Quick Check 11.4 ✅

1. A community garden's coordinator piloted a reminder-text Work Order. All 3 runs passed every criterion, and review took about 1 minute each. Writing the text by hand takes about 4 minutes, and she sends 2 texts a month. Write her Selection Decision's Decision and Why.
2. A Why line reads "Tool A is great and the team likes it." Critique the line, and rewrite it from the triage pilot's counts.

---

## 11.5 Summary and Retrieval 💡

### Key Concepts

* Define the problem before you name a tool. The Requirements Sheet's seven fields run from the problem to the no-AI option, and it is written before any tool is named.
* Scenario alignment matches each line of the Requirements Sheet to a Tool Survey card field. When no candidate meets the must-pass lines, the aligned answer is no AI here.
* The Work Order directs an AI assistant or agent-style tool through a job with eight fields, from the Goal to the Log. A checkpoint makes the tool stop for approval, and the Review plan names the person who checks.
* A tool's self-check is a claim. Acceptance criteria are checked by a person, with the Output Checklist or the Accuracy Audit.
* Three tests decide when the answer is no AI here: the input test, the decision test, and the cost test.
* A pilot runs the same Work Order several times in fresh conversations, scored in counts and minutes. The Selection Decision records the candidates, the pilot, the Use Evaluation, and one of four decisions, with a Why a colleague can check.

### Key Terms

See course glossary for full definitions

* Requirements Sheet, no-AI option, scenario alignment (Section 11.1)
* agent-style tool, Work Order, acceptance criteria (Section 11.2)
* Selection Decision (Section 11.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Name the seven fields of the Requirements Sheet in order, and say which field gives every tool a baseline to beat.
2. Name the eight fields of the Work Order in order, and say which field the VPN test plan's Scope gap belonged to.
3. Name the four outcomes a Selection Decision can record, and explain how "decline" differs from "no AI here."
4. From Chapter 9: Name the Use Evaluation's five factors in order, and explain why a pilot is not a benchmark.
5. From Chapter 7: Name the four steps of the Accuracy Audit in order, and the verdict a total earns when it matches the file.

---

## 11.6 Skills Lab 11A: Four Scenarios for Mei Lin

**Goal:** Solve three of Mei Lin's Copperwind scenarios with the matched tool, each with a Requirements Sheet, a Work Order, a run, and a scored result. Decide the fourth, the disputed invoice, with reasons. Then deliver a Selection Decision from a measured pilot and a Memo telling Mei Lin which scenarios get a pilot next, which get a tool now, and which get none.

**Starter files:** Provided files in `assets/code/chapter-11/` from the course data pack. Your answer file is `skills-lab-11a-worksheet.md`. The four scenario files are `deskside-inbox-day.txt` (12 ticket subjects and first lines), `deskside-tickets.csv` (a synthetic sample of 80 of the four weeks' tickets, in 6 columns). The other two are `priya-outreach-brief-3.txt` (Priya's flyer request), and `disputed-invoice-case.txt` (the fourth scenario). The sheets you fill are `requirements-sheet-template.md`, `work-order-template.md`, and `selection-decision-template.md`. The sheets from earlier chapters ship here too: `output-checklist.md`, `use-evaluation-sheet.md`, and `memo-template.md`. Download the data pack from Canvas, extract it, and work at the extracted `cis137` root. Open each file in any text editor and never retype its contents. The lab files are fictional, so you may paste them into a chat assistant once your privacy plan allows it. You first met Copperwind in Chapter 1, and this lab gives you everything it needs, so you do not need any earlier file. For Candidates, use your Tool Survey from Chapter 10 if you have one, or list two roster tools with their type and the data policy line you read.

### Part 1: Foundation (Aligns with Objective 11.1)

Work in `skills-lab-11a-worksheet.md`, which has a space for every task below. Read all four scenario files in full before you write anything.

1. Before you send any prompt, write your privacy plan in two columns: what from the four scenario files may go into a tool, and what stays out of every prompt. Give the reason for each item that stays out, and quote the line of the file it came from.
2. Fill a `requirements-sheet-template.md` for each of the four scenarios: the inbox triage, the data question, the flyer, and the disputed invoice. Write all seven fields of each before you name any tool. The owner's data question is: how many first replies missed the target of a first reply within 30 minutes over the four weeks, and which category had the most misses?
3. Run the three tests from Section 11.3 on each scenario, with a yes or no and one reason each. For the disputed invoice, decide whether it gets a tool, a tool with a fix, or no AI here, and name the Requirements Sheet fields that decided it.

### Part 2: Application (Aligns with Objectives 11.1 and 11.2)

1. For the triage, the data question, and the flyer, choose a tool from your candidates. Justify each choice in two sentences with scenario alignment, naming the Requirements Sheet line each candidate meets or fails. For the flyer, say which tool does the picture and which does the words.
2. Before you run the triage, write your own key: the category and urgency you give each of the 12 tickets in `deskside-inbox-day.txt`, using Deskside's rules in the file.
3. Write a Work Order for each of the three scenarios in `work-order-template.md`, all eight fields, and send each in a fresh conversation. Paste every prompt and response with the tool and the date. For the flyer, generate the picture if your roster tool can, and run Chapter 3's image checks (text in the picture, faces, logos, and accuracy) on it.
4. Score each result against its acceptance criteria with a count or a quote. Score the triage against your key. Run the Accuracy Audit on every number in the data question's answer by sorting `deskside-tickets.csv` yourself in a spreadsheet, and report the counts. Run the Output Checklist on the flyer's words, alt text, and disclosure line.

### Part 3: Extension (Aligns with Objectives 11.2 and 11.3)

1. Pilot one of your three scenarios. Run its Work Order three times, each in a fresh conversation, in one tool or in two. Score every run against every acceptance criterion, and time your review of each run in minutes.
2. Fill `selection-decision-template.md` for the piloted scenario, with `use-evaluation-sheet.md` behind its Use Evaluation lines. Choose adopt, extend the pilot, decline, or no AI here, and write a Why a colleague could check. Fill a second Selection Decision for the disputed invoice, with its Decision, Why, and Rules that apply.
3. Write the Memo to Mei Lin in `memo-template.md`, under 400 words. Put the piloted scenario's decision in the first sentence, with a clause pointing to the scenario lines. Give one paragraph per factor for the piloted scenario, from its Use Evaluation. After Workforce impact, add a "Scenario lines" paragraph with one line for each other scenario: its decision and the Requirements Sheet line that decided it. A scenario you did not pilot can be recommended only as "pilot next" or "no AI here." End with what we do not know and one next step.

### Questions & Analysis 🤔

Answer both questions in the worksheet's final section. These answers carry significant rubric weight.

1. Quote the line of your privacy plan and the Requirements Sheet field that most shaped your decision on the disputed invoice. Then quote one scored acceptance criterion from your prompt log for another scenario. Explain how your invoice decision differs from your decision on that scenario, using the three tests.
2. Quote the scores and review minutes of your three pilot runs from your prompt log. Explain whether three runs were enough for your Selection Decision, and name the result in a longer pilot that would change it.

**Submission:** Submit your completed worksheet as one file named `skills-lab-11a-lastname.md`. Keep every answer under its task heading, with your filled Requirements Sheets, Work Orders, Selection Decisions, and Memo pasted into their sections. Include every prompt you sent, the tool and date, and every response you received, pasted exactly, with your Questions & Analysis answers clearly labeled at the end. Keep copies of your three templates. They are working tools for your next job.

### Rubric: Skills Lab 11A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria, five
levels from Mastery to Not Evident. The criteria are Technical
Accuracy and Efficiency, Output Quality, Documentation Quality, and
Analysis, Interpretation, and Response to QUESTION(s). The criteria
and levels are the same everywhere. Your instructor sets the point
values in your course. Check the syllabus and the Canvas rubric
attached to this lab for the values that apply to you.

---

## 11.7 Review Questions 🔄️

1. **Understand:** Explain to a coworker, in no more than three sentences, why a Requirements Sheet is written before any tool is named.

2. **Apply:** A university housing office wants a chat assistant to draft a move-out checklist for residents from its housing contract. Write the Work Order's Scope, two acceptance criteria (each with the checklist that runs it), and the Review plan.

3. **Analyze:** A small accounting firm piloted two tools on a Work Order that summarizes client emails. Tool A passed every criterion in 3 of 3 runs, with about 2 minutes of review each. Tool B passed in 2 of 3 runs, failing once by adding a deadline the email never stated, with about 1 minute of review each. Analyze what the pilot shows and what it cannot show, and name the Use Evaluation factor it leaves empty.

4. **Evaluate:** A city animal shelter wants an agent-style tool to read new intake records and post adoption listings to its website with no staff review. Decide adopt, extend the pilot, decline, or no AI here. Defend your decision with the Work Order's Review plan and the three tests from Section 11.3, and name the one change that would most change your answer.

---

## Further Reading 📖

* [AI Risk Management Framework (National Institute of Standards and Technology)](https://www.nist.gov/itl/ai-risk-management-framework): The home page of the NIST AI RMF, published January 2023. Its MAP function asks an organization to document a system's intended purpose and setting before deciding to proceed, which is the Requirements Sheet's job at the scale of a whole organization.
* [Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence): NIST's July 2024 profile for generative AI. Its list of risks includes data privacy and "Human-AI Configuration," which covers over-reliance on a tool, the reason a Work Order names a human reviewer.
* [Understanding Success Criterion 1.4.5: Images of Text (W3C)](https://www.w3.org/WAI/WCAG22/Understanding/images-of-text.html): The W3C's explanation of the rule behind the flyer decision in Section 11.3. It says, in brief, "Use text instead of pictures of text."

---

## Looking Ahead ⏩

You can now define a problem before naming a tool, direct a tool through a job with a Work Order, and decide with a measured pilot, including when the answer is no AI. Chapter 12 puts all of it to work in one project. You will deliver a solution with a Verification Trail, present it to a stakeholder, and write an Ethics Statement, and your Requirements Sheet, Work Orders, and Selection Decision come with you.
