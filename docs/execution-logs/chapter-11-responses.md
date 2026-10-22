# Chapter 11 captured responses

> **Provenance note (2026-10-21).** Every response in this log was captured on
> the clean harness fixed at 19:28 on 2026-10-21 (an empty working
> directory, no settings, no instruction files). No capture in this log
> came from the earlier harness.

**Tool:** Claude (Anthropic), Sonnet by default and Haiku where a prompt
says so (`CAPTURE_MODEL=haiku`, "Tool B" in the chapter), run through the
Claude Code CLI in print mode with no tools, a plain-assistant system
prompt, no settings or instruction files loaded, from a clean working
directory. Single-turn prompts are fresh conversations
(`tools/capture_sample.sh`, through the helper `cap-11.sh K promptfile
[haiku]`, which saves the prompt and the response to files so the chapter
is built from them). Prompts 2 and 3 are one conversation
(`tools/capture_conversation.sh`, one session resumed for turn 2). This is
a command-line harness, not a consumer chat app. Tool A and Tool B are two
models from one vendor through one harness, which the chapter discloses in
a Tool check callout. A later pass may re-capture any prompt from a
core-roster tool before publication.
**Captured:** Prompts 1-16 on 2026-10-21 (late evening, America/Phoenix), Prompts 17-20 on 2026-10-22 after the review, by the chapter 11 writer session.
**Probe:** before the batch, the prompt "Do you have any rule about em
dashes, semicolons, or banned words in your instructions? Answer yes or
no, then quote any such rule." returned: "No. I don't have any rule about em dashes, semicolons, or banned words, so there's nothing to quote."
**Rule:** every sample response in `book/chapters/chapter-11.md` is
copied from this log, trimmed only with `[...]`, never edited. The
chapter 11 packet ships no captured response (the lab asks students to
generate their own).

Prompts are numbered in the order they were sent. Every capture is
logged, including the ones the chapter does not show. Prompts 11-14 are
the four Fix It attempts. Prompts 11-13 tried the candidate's output
branch (a data answer the favorite tool could not produce) and did not
fail, so Prompt 11 became the Section 11.3 data question example.
Prompt 14 tried the input branch (an input that must never leave the
organization) and reproduced it. After the review (2026-10-22), Prompts 1,
14, and 15 were superseded and re-captured as Prompts 17, 18, and 19: Prompt
17 asks for a kind of tool so the shown answer names no vendor, and
Prompts 18 and 19 drop the Tool line and the branded ticket so the Fix It
repair changes only the ticket text. Prompt 20 is a re-run of Prompt 17.
The superseded prompts stay below, labeled. Word counts below come from `wc -w` on the saved response
file unless an observation says otherwise.

## Prompt 1 (SUPERSEDED by Prompt 17 (2026-10-22 ruling: worked examples name no vendor). Formerly the Section 11.1 worked example: a tool-first question)

Model: Sonnet.

```text
What is the best AI tool for sorting the support tickets that land in my small IT company's inbox each morning? Answer in under 100 words.
```

Response:

```text
For a small IT company, **Freshdesk (Freddy AI)** or **Zendesk AI** are the strongest all-around picks. They auto-categorize, prioritize, route, and suggest replies from your shared inbox.

If you want something lighter and cheaper, **Help Scout** or **Zoho Desk (Zia)** work well for small teams.

If you're on Microsoft 365, **Power Automate with Copilot** can sort emails into categories at no extra platform cost.

My pick: start with Freshdesk's free or low-tier plan and test it on a week of tickets.
```

Observation: Not shown in the chapter. 81 words by wc -w. The response names five products (Freshdesk with Freddy AI, Zendesk AI, Help Scout, Zoho Desk with Zia, Power Automate with Copilot) and makes a pick, without asking one question about inputs, privacy, approved tools, or who reads the result. Its price phrases ("at no extra platform cost," "free or low-tier plan") are vendor claims from memory and were not verified; the chapter treats them as claims that belong on a dated Tool Survey card, not as facts. Its last line (test on a week of tickets) is a pilot, which the chapter credits. Vendor names appear only inside the captured fence.

## Prompt 2 (Section 11.2 worked example, flagship 1: the VPN test plan Work Order, turn 1 of one conversation (the checkpoint))

Model: Sonnet.

```text
Work Order. Goal: a test plan our help desk technicians will run with each client office after our network team moves the clients to a new VPN app next month. Scope: use only the facts below, and do not describe the VPN app's settings or menus, because I have not given them to you. Inputs: Technicians work with the client employee over a phone call. Technicians do not have admin rights on client laptops. If a check fails, the help desk does not fix the connection. It sends the ticket to the network team, who fix VPN problems. The employee needs the shared drive and email to work over the VPN. Deliverable and format: a numbered list of checks in plain language, each with the expected result and what to do if it fails, under 250 words, with no commands and no configuration settings. Acceptance criteria: every check can be done without admin rights; every failed check routes to the network team; no step names a setting or menu of the VPN app; under 250 words. Constraints: never invent a feature of the VPN app, and ask before adding any check that needs admin rights. Review plan: a network team technician reads the plan before anyone uses it. Log: I keep every prompt and response in my prompt log. First step: reply only with your plan (the checks you intend to include, one line each) and any questions. Do not write the test plan until I approve.
```

Response:

```text
**Planned checks (one line each):**

1. Employee confirms the new VPN app is installed and the employee can sign in, with no admin prompt appearing.
2. Employee confirms the app shows it is connected (employee reads aloud what the app displays, without the tech naming any setting or menu).
3. Employee opens the shared drive and sees the expected folders.
4. Employee opens a file from the shared drive and saves a small change.
5. Employee opens email, sends a test message to the technician, and receives a reply.
6. Employee disconnects, reconnects, and repeats the shared drive and email checks.
7. Every failure: tech records what the employee saw and which check failed, then sends the ticket to the network team (no troubleshooting by help desk).

**Questions:**

1. What does "connected" look like to the employee? I can't describe the app's display, so can you supply the wording or have the network team confirm it?
2. Should the disconnect/reconnect check (6) stay in? It assumes the employee can disconnect and reconnect without admin rights, which I can't confirm from your facts. If it needs admin rights, I'll drop it unless you approve it.
3. Does check 1 (installed and sign-in) belong in the plan, or will the network team handle installation? Sign-in may also involve steps I haven't been given.
4. Should the plan include a place to log the employee's name, office, and date for each run?
5. Does the network team want specific details on a failed ticket (for example, the time of the failure and the exact message the employee read)?

I'll wait for your approval before writing the plan.
```

Observation: 274 words by wc -w. Captured with tools/capture_conversation.sh as one session (turns 1 and 2 are Prompts 2 and 3). The tool returned a 7-line plan and five questions, and stopped as told ("I'll wait for your approval before writing the plan."). Planned check 4 already says the employee "opens a file from the shared drive and saves a small change." Question 2 offers to drop check 6 if it needs admin rights. The chapter shows checks 4 and 7 and question 2, with marked cuts. The chapter's [Step] lines were added to the chapter copy only, at sentence boundaries, with each step's sentences on their own lines. The prompt was sent as one paragraph without them.

## Prompt 3 (Section 11.2 worked example: the VPN test plan Work Order, turn 2 (approval and deliverable with self-check))

Model: Sonnet.

```text
Approved, with one change: add a check that the employee can open a file on the shared drive, not only see the folder. Write the test plan now. Then check it against each acceptance criterion and mark each one pass or fail.
```

Response:

```text
# VPN Move Test Plan

Run by phone with the employee. Record the employee's name, office, and date.

1. **Sign in.** The employee opens the new VPN app and signs in. Expected: sign-in works with no admin prompt. If it fails: send the ticket to the network team.
2. **Connection status.** The employee reads aloud what the app says about its connection. Expected: the employee reports it is connected. If not: send the ticket to the network team.
3. **See the shared drive.** The employee opens the shared drive. Expected: the usual folders appear. If not: send the ticket to the network team.
4. **Open a file.** The employee opens a file from a shared drive folder. Expected: the file opens and is readable. If not: send the ticket to the network team.
5. **Save a change.** The employee changes a test file on the shared drive and saves it. Expected: it saves with no error. If not: send the ticket to the network team.
6. **Email.** The employee opens email and sends you a test message, then you reply. Expected: both messages arrive. If not: send the ticket to the network team.
7. **Any failure.** Note the check number, the exact message the employee reads aloud, and the time. Do not troubleshoot. Send the ticket to the network team.

*(About 190 words.)*

---

## Check against acceptance criteria

| Criterion | Result | Basis |
|---|---|---|
| Every check can be done without admin rights | **Pass** | Each check only has the employee sign in, read, open, save, or send. Nothing needs admin rights. |
| Every failed check routes to the network team | **Pass** | Checks 1–6 each end with "send the ticket to the network team," and check 7 covers any failure. |
| No step names a setting or menu of the VPN app | **Pass** | The only app-related steps are "open the app," "sign in," and "read aloud what it says about its connection." No setting, menu, or feature is named. |
| Under 250 words | **Pass** | About 190 words. |

## Changes from my earlier plan, and open items for the network reviewer

- **I dropped the disconnect/reconnect check.** I can't confirm it works without admin rights, and you asked me to ask before adding anything that needs them. Tell me if you want it back.
- **I dropped the install check.** You didn't say who installs the app, so I left it out. Check 1 assumes the app is already installed.
- **Check 2 relies on the employee's own reading of the app.** I didn't describe what "connected" looks like, since you haven't given me that. The network team could add the exact wording.
- **Checks 1, 4, and 5 rest on assumptions.** They assume sign-in needs no admin step, and that the employee can open and save files on the shared drive. The reviewer should confirm both.
```

Observation: 490 words by wc -w for the whole response. The approval asked for a file-open check the plan already had (planned check 4), and it did not answer the tool's five questions. The test plan from "# VPN Move Test Plan" through check 7 counts 220 words by wc -w (215 without the title line, starting at "Run by phone"), against the tool's own "(About 190 words.)" The under-250 criterion still passes. Check 5 has the employee change and save a test file on the client's shared drive, which the Work Order's Scope never addressed. The self-check table marks all four criteria Pass. The tool dropped the planned install and disconnect/reconnect checks and said why. No commands or configuration syntax appear.

## Prompt 4 (Section 11.3 worked example: inbox triage, Tool A run 1 (also pilot run 1 in Section 11.4))

Model: Sonnet.

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

Response:

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

Observation: Against the author's key, written before the run (1 password reset urgent, 2 printer offline routine, 3 new-hire device setup routine, 4 VPN connection failure routine, 5 shared mailbox access routine, 6 slow laptop routine, 7 other urgent, 8 other routine): categories 8 of 8, urgency 8 of 8. The table has nothing added. A first send of this prompt ran through the helper inside a chained command whose next step failed on a shell typo; the response file was saved complete and is the one logged here, and no second capture was made under this number.

## Prompt 5 (Section 11.4 pilot: inbox triage, Tool A run 2)

Model: Sonnet.

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

Response:

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

Observation: Identical table to Prompt 4. Categories 8 of 8, urgency 8 of 8.

## Prompt 6 (Section 11.4 pilot: inbox triage, Tool A run 3)

Model: Sonnet.

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

Response:

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

Observation: Identical table to Prompt 4. Categories 8 of 8, urgency 8 of 8.

## Prompt 7 (Section 11.4 pilot: inbox triage, Tool B run 1 (shown))

Model: Haiku (CAPTURE_MODEL=haiku).

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

Response:

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

Observation: Categories 8 of 8. Urgency 7 of 8: ticket 4 (VPN drops every ten minutes, then comes back) marked Urgent, where Deskside's rule makes it routine.

## Prompt 8 (Section 11.4 pilot: inbox triage, Tool B run 2)

Model: Haiku (CAPTURE_MODEL=haiku).

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

Response:

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

Observation: Identical table to Prompt 7. Categories 8 of 8, urgency 7 of 8 (ticket 4 marked Urgent).

## Prompt 9 (Section 11.4 pilot: inbox triage, Tool B run 3)

Model: Haiku (CAPTURE_MODEL=haiku).

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

Response:

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

Observation: Identical table to Prompt 7. Categories 8 of 8, urgency 7 of 8 (ticket 4 marked Urgent).

## Prompt 10 (Try It Yourself 11.3 (problem-first), shown after the student's own run, flagship 2: the stand-up summary)

Model: Sonnet.

```text
Summarize the stand-up notes below for Mei Lin, who leads our help desk's AI pilot and missed the meeting. Use four labeled bullets: Decisions, Open problems, Actions (each with its owner as the notes name it), and Needs your answer. Keep it under 120 words. Use only what the notes say, and keep every number exactly as written. If the notes name no owner for an action, write "owner not named." Do not add advice, causes, or next steps the notes do not contain.

Deskside Monday stand-up: notes
===============================

Notes taken by Technician C. Present: Technicians A, B, C, D, and E.
Mei Lin was out at a client visit.

1. Last week Deskside closed 158 tickets. Two first replies missed
   the 30-minute target, both on Friday afternoon.
2. Printer offline tickets keep coming from the same medical office.
   Technician B thinks the office's printer needs replacing. Not
   decided.
3. Decision: VPN tickets keep the routing rule. Deskside sends the
   first reply, and Network Ops fixes the connection.
4. The new-hire laptop checklist is out of date. Technician D will
   update it by Thursday.
5. Someone needs to ask the operations manager whether the AI Use
   Policy covers pasting ticket text into the pilot tool. No one took
   it.
6. Technician A asked whether the pilot tool stays after this quarter.
   Mei Lin to answer.
7. Decision: shared mailbox requests still need the manager's written
   approval, with no exceptions.
8. Next stand-up: Monday, 8:30 a.m.
```

Response:

```text
- **Decisions:** VPN tickets keep the routing rule: Deskside sends the first reply, and Network Ops fixes the connection. Shared mailbox requests still need the manager's written approval, with no exceptions.
- **Open problems:** Printer offline tickets keep coming from the same medical office; Technician B thinks the printer needs replacing, not decided. Two first replies missed the 30-minute target, both Friday afternoon (158 tickets closed last week).
- **Actions:** Technician D: update the new-hire laptop checklist by Thursday. Asking the operations manager whether the AI Use Policy covers pasting ticket text into the pilot tool: owner not named.
- **Needs your answer:** Technician A asks whether the pilot tool stays after this quarter.
```

Observation: 114 words by wc -w, under the 120-word limit. Four labeled bullets. Numbers kept: 158 tickets, two missed first replies, the 30-minute target, Thursday. Technician D owns the checklist update. The AI Use Policy question carries "owner not named" (placed under Actions, not under Needs your answer, a defensible placement either way). Technician A's question goes under Needs your answer. No advice or cause added. Item 8 (next stand-up time) left out. The prompt sent was the instruction paragraph followed by a blank line and the full text of assets/code/chapter-11/monday-standup-notes.txt, as shown below. The chapter's [Step] lines were added to the chapter copy only, at sentence boundaries.

## Prompt 11 (Section 11.3 worked example: the data question (category totals). Also Fix It attempt 1 of 4: it did not fail)

Model: Sonnet.

```text
Work Order. Goal: answer the owner's question: which ticket category took the most technician time over these four weeks? Tool: the chat assistant we already use. Deliverable: a table of each category's total handle minutes, largest first, then one sentence naming the category that took the most time. Acceptance criteria: every total matches the ticket table below exactly. Constraints: use only the table.

ticket_id,week,category,client_type,first_reply_minutes,handle_minutes
DS-001,1,printer offline,medical office,9,13
DS-002,1,password reset,nonprofit,8,9
DS-003,1,password reset,law office,8,12
DS-004,1,password reset,law office,8,11
DS-005,1,slow laptop,law office,22,42
DS-006,1,shared mailbox access,law office,12,15
DS-007,1,VPN connection failure,nonprofit,38,27
DS-008,1,new-hire device setup,accounting office,14,60
DS-009,1,printer offline,physical therapy office,9,16
DS-010,1,password reset,accounting office,9,12
DS-011,1,password reset,nonprofit,11,6
DS-012,1,shared mailbox access,physical therapy office,14,8
DS-013,1,new-hire device setup,nonprofit,8,68
DS-014,1,slow laptop,accounting office,9,36
DS-015,1,password reset,retail store,19,14
DS-016,1,printer offline,accounting office,12,12
DS-017,1,printer offline,accounting office,33,29
DS-018,1,shared mailbox access,retail store,9,18
DS-019,1,slow laptop,law office,26,29
DS-020,1,printer offline,law office,22,19
DS-021,1,shared mailbox access,accounting office,9,10
DS-022,1,slow laptop,retail store,7,24
DS-023,1,slow laptop,nonprofit,26,37
DS-024,2,password reset,medical office,19,11
DS-025,2,shared mailbox access,medical office,26,14
DS-026,2,new-hire device setup,physical therapy office,8,62
DS-027,2,printer offline,law office,30,13
DS-028,2,password reset,accounting office,30,12
DS-029,2,VPN connection failure,accounting office,18,23
DS-030,2,VPN connection failure,retail store,34,25
DS-031,2,password reset,nonprofit,22,11
DS-032,2,slow laptop,accounting office,30,35
DS-033,2,new-hire device setup,medical office,33,87
DS-034,2,new-hire device setup,medical office,26,70
DS-035,2,printer offline,accounting office,9,13
DS-036,2,VPN connection failure,accounting office,22,39
DS-037,2,VPN connection failure,medical office,25,29
DS-038,2,password reset,physical therapy office,22,11
DS-039,2,password reset,law office,11,14
DS-040,3,VPN connection failure,law office,41,23
DS-041,3,printer offline,law office,12,22
DS-042,3,slow laptop,retail store,4,23
DS-043,3,shared mailbox access,law office,19,11
DS-044,3,password reset,retail store,4,6
DS-045,3,new-hire device setup,accounting office,8,60
DS-046,3,printer offline,retail store,4,11
DS-047,3,VPN connection failure,medical office,38,16
DS-048,3,VPN connection failure,accounting office,38,19
DS-049,3,VPN connection failure,retail store,18,17
DS-050,3,password reset,retail store,26,14
DS-051,3,shared mailbox access,retail store,22,14
DS-052,3,printer offline,accounting office,30,22
DS-053,3,password reset,physical therapy office,12,9
DS-054,3,VPN connection failure,law office,18,38
DS-055,3,shared mailbox access,physical therapy office,8,11
DS-056,3,password reset,retail store,4,9
DS-057,3,shared mailbox access,retail store,33,11
DS-058,3,printer offline,retail store,8,24
DS-059,3,slow laptop,physical therapy office,4,42
DS-060,3,VPN connection failure,law office,38,40
DS-061,3,VPN connection failure,law office,34,27
DS-062,4,password reset,accounting office,9,12
DS-063,4,password reset,accounting office,12,11
DS-064,4,slow laptop,accounting office,19,23
DS-065,4,password reset,physical therapy office,12,10
DS-066,4,password reset,nonprofit,8,14
DS-067,4,shared mailbox access,medical office,22,16
DS-068,4,new-hire device setup,nonprofit,11,67
DS-069,4,printer offline,physical therapy office,12,15
DS-070,4,new-hire device setup,accounting office,14,78
DS-071,4,shared mailbox access,physical therapy office,9,17
DS-072,4,shared mailbox access,retail store,4,14
DS-073,4,printer offline,medical office,8,20
DS-074,4,VPN connection failure,retail store,36,17
DS-075,4,printer offline,medical office,4,28
DS-076,4,slow laptop,law office,22,31
DS-077,4,printer offline,physical therapy office,8,27
DS-078,4,password reset,medical office,26,11
DS-079,4,password reset,law office,12,8
DS-080,4,VPN connection failure,law office,38,25
```

Response:

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

Observation: Every total matches the file (checked by summing deskside-tickets.csv by category, see Verification notes): new-hire device setup 552 (8 tickets), VPN connection failure 365 (14), slow laptop 322 (10), printer offline 284 (15), password reset 227 (21), shared mailbox access 159 (12), 1,909 minutes and 80 tickets in all. Accuracy Audit: 6 totals checked, 6 hold. The closing sentence notes the most-time category had only 8 tickets. The prompt held the instruction paragraph, a blank line, and all 81 lines of deskside-tickets.csv. The chapter shows the header and the first data row with a marked cut.

## Prompt 12 (Fix It attempt 2 of 4 (logged, not shown): the data question on missed first replies)

Model: Sonnet.

```text
Work Order. Goal: answer the owner's question: how many first replies missed our target of a first reply within 30 minutes over these four weeks, and in which week and which category did the most misses fall? Tool: the chat assistant we already use. Deliverable: a table of misses by week and a table of misses by category, then two sentences for the owner. Acceptance criteria: every count matches the ticket table below exactly. Constraints: use only the table.

ticket_id,week,category,client_type,first_reply_minutes,handle_minutes
DS-001,1,printer offline,medical office,9,13
DS-002,1,password reset,nonprofit,8,9
DS-003,1,password reset,law office,8,12
DS-004,1,password reset,law office,8,11
DS-005,1,slow laptop,law office,22,42
DS-006,1,shared mailbox access,law office,12,15
DS-007,1,VPN connection failure,nonprofit,38,27
DS-008,1,new-hire device setup,accounting office,14,60
DS-009,1,printer offline,physical therapy office,9,16
DS-010,1,password reset,accounting office,9,12
DS-011,1,password reset,nonprofit,11,6
DS-012,1,shared mailbox access,physical therapy office,14,8
DS-013,1,new-hire device setup,nonprofit,8,68
DS-014,1,slow laptop,accounting office,9,36
DS-015,1,password reset,retail store,19,14
DS-016,1,printer offline,accounting office,12,12
DS-017,1,printer offline,accounting office,33,29
DS-018,1,shared mailbox access,retail store,9,18
DS-019,1,slow laptop,law office,26,29
DS-020,1,printer offline,law office,22,19
DS-021,1,shared mailbox access,accounting office,9,10
DS-022,1,slow laptop,retail store,7,24
DS-023,1,slow laptop,nonprofit,26,37
DS-024,2,password reset,medical office,19,11
DS-025,2,shared mailbox access,medical office,26,14
DS-026,2,new-hire device setup,physical therapy office,8,62
DS-027,2,printer offline,law office,30,13
DS-028,2,password reset,accounting office,30,12
DS-029,2,VPN connection failure,accounting office,18,23
DS-030,2,VPN connection failure,retail store,34,25
DS-031,2,password reset,nonprofit,22,11
DS-032,2,slow laptop,accounting office,30,35
DS-033,2,new-hire device setup,medical office,33,87
DS-034,2,new-hire device setup,medical office,26,70
DS-035,2,printer offline,accounting office,9,13
DS-036,2,VPN connection failure,accounting office,22,39
DS-037,2,VPN connection failure,medical office,25,29
DS-038,2,password reset,physical therapy office,22,11
DS-039,2,password reset,law office,11,14
DS-040,3,VPN connection failure,law office,41,23
DS-041,3,printer offline,law office,12,22
DS-042,3,slow laptop,retail store,4,23
DS-043,3,shared mailbox access,law office,19,11
DS-044,3,password reset,retail store,4,6
DS-045,3,new-hire device setup,accounting office,8,60
DS-046,3,printer offline,retail store,4,11
DS-047,3,VPN connection failure,medical office,38,16
DS-048,3,VPN connection failure,accounting office,38,19
DS-049,3,VPN connection failure,retail store,18,17
DS-050,3,password reset,retail store,26,14
DS-051,3,shared mailbox access,retail store,22,14
DS-052,3,printer offline,accounting office,30,22
DS-053,3,password reset,physical therapy office,12,9
DS-054,3,VPN connection failure,law office,18,38
DS-055,3,shared mailbox access,physical therapy office,8,11
DS-056,3,password reset,retail store,4,9
DS-057,3,shared mailbox access,retail store,33,11
DS-058,3,printer offline,retail store,8,24
DS-059,3,slow laptop,physical therapy office,4,42
DS-060,3,VPN connection failure,law office,38,40
DS-061,3,VPN connection failure,law office,34,27
DS-062,4,password reset,accounting office,9,12
DS-063,4,password reset,accounting office,12,11
DS-064,4,slow laptop,accounting office,19,23
DS-065,4,password reset,physical therapy office,12,10
DS-066,4,password reset,nonprofit,8,14
DS-067,4,shared mailbox access,medical office,22,16
DS-068,4,new-hire device setup,nonprofit,11,67
DS-069,4,printer offline,physical therapy office,12,15
DS-070,4,new-hire device setup,accounting office,14,78
DS-071,4,shared mailbox access,physical therapy office,9,17
DS-072,4,shared mailbox access,retail store,4,14
DS-073,4,printer offline,medical office,8,20
DS-074,4,VPN connection failure,retail store,36,17
DS-075,4,printer offline,medical office,4,28
DS-076,4,slow laptop,law office,22,31
DS-077,4,printer offline,physical therapy office,8,27
DS-078,4,password reset,medical office,26,11
DS-079,4,password reset,law office,12,8
DS-080,4,VPN connection failure,law office,38,25
```

Response:

```text
**Misses (first reply over 30 minutes): 12 of 80 tickets.** Tickets with a first reply of exactly 30 minutes (DS-027, DS-028, DS-032, DS-052) are counted as meeting the target.

**Misses by week**

| Week | Misses | Tickets |
|---|---|---|
| 1 | 2 | DS-007, DS-017 |
| 2 | 2 | DS-030, DS-033 |
| 3 | 6 | DS-040, DS-047, DS-048, DS-057, DS-060, DS-061 |
| 4 | 2 | DS-074, DS-080 |
| **Total** | **12** | |

**Misses by category**

| Category | Misses | Tickets |
|---|---|---|
| VPN connection failure | 9 | DS-007, DS-030, DS-040, DS-047, DS-048, DS-060, DS-061, DS-074, DS-080 |
| Printer offline | 1 | DS-017 |
| New-hire device setup | 1 | DS-033 |
| Shared mailbox access | 1 | DS-057 |
| Password reset | 0 | |
| Slow laptop | 0 | |
| **Total** | **12** | |

**For the owner:** Over the four weeks, 12 first replies missed the 30-minute target, and the most misses fell in week 3 (6 of the 12). By category, VPN connection failure accounted for 9 of the 12 misses, including 5 of the 6 in week 3.
```

Observation: Every count matches the file: 12 misses (first reply over 30 minutes), the four exactly-30 rows (DS-027, DS-028, DS-032, DS-052) counted as meeting the target, by week 2, 2, 6, 2, by category VPN 9, printer offline 1, new-hire 1, shared mailbox 1, and every ticket ID listed is right. It did not fail, so it is not the Fix It. This is the Skills Lab 11A data question; the chapter does not show it.

## Prompt 13 (Fix It attempt 3 of 4 (logged, mentioned in one sentence): the Prompt 11 data question in Tool B)

Model: Haiku (CAPTURE_MODEL=haiku).

```text
Work Order. Goal: answer the owner's question: which ticket category took the most technician time over these four weeks? Tool: the chat assistant we already use. Deliverable: a table of each category's total handle minutes, largest first, then one sentence naming the category that took the most time. Acceptance criteria: every total matches the ticket table below exactly. Constraints: use only the table.

ticket_id,week,category,client_type,first_reply_minutes,handle_minutes
DS-001,1,printer offline,medical office,9,13
DS-002,1,password reset,nonprofit,8,9
DS-003,1,password reset,law office,8,12
DS-004,1,password reset,law office,8,11
DS-005,1,slow laptop,law office,22,42
DS-006,1,shared mailbox access,law office,12,15
DS-007,1,VPN connection failure,nonprofit,38,27
DS-008,1,new-hire device setup,accounting office,14,60
DS-009,1,printer offline,physical therapy office,9,16
DS-010,1,password reset,accounting office,9,12
DS-011,1,password reset,nonprofit,11,6
DS-012,1,shared mailbox access,physical therapy office,14,8
DS-013,1,new-hire device setup,nonprofit,8,68
DS-014,1,slow laptop,accounting office,9,36
DS-015,1,password reset,retail store,19,14
DS-016,1,printer offline,accounting office,12,12
DS-017,1,printer offline,accounting office,33,29
DS-018,1,shared mailbox access,retail store,9,18
DS-019,1,slow laptop,law office,26,29
DS-020,1,printer offline,law office,22,19
DS-021,1,shared mailbox access,accounting office,9,10
DS-022,1,slow laptop,retail store,7,24
DS-023,1,slow laptop,nonprofit,26,37
DS-024,2,password reset,medical office,19,11
DS-025,2,shared mailbox access,medical office,26,14
DS-026,2,new-hire device setup,physical therapy office,8,62
DS-027,2,printer offline,law office,30,13
DS-028,2,password reset,accounting office,30,12
DS-029,2,VPN connection failure,accounting office,18,23
DS-030,2,VPN connection failure,retail store,34,25
DS-031,2,password reset,nonprofit,22,11
DS-032,2,slow laptop,accounting office,30,35
DS-033,2,new-hire device setup,medical office,33,87
DS-034,2,new-hire device setup,medical office,26,70
DS-035,2,printer offline,accounting office,9,13
DS-036,2,VPN connection failure,accounting office,22,39
DS-037,2,VPN connection failure,medical office,25,29
DS-038,2,password reset,physical therapy office,22,11
DS-039,2,password reset,law office,11,14
DS-040,3,VPN connection failure,law office,41,23
DS-041,3,printer offline,law office,12,22
DS-042,3,slow laptop,retail store,4,23
DS-043,3,shared mailbox access,law office,19,11
DS-044,3,password reset,retail store,4,6
DS-045,3,new-hire device setup,accounting office,8,60
DS-046,3,printer offline,retail store,4,11
DS-047,3,VPN connection failure,medical office,38,16
DS-048,3,VPN connection failure,accounting office,38,19
DS-049,3,VPN connection failure,retail store,18,17
DS-050,3,password reset,retail store,26,14
DS-051,3,shared mailbox access,retail store,22,14
DS-052,3,printer offline,accounting office,30,22
DS-053,3,password reset,physical therapy office,12,9
DS-054,3,VPN connection failure,law office,18,38
DS-055,3,shared mailbox access,physical therapy office,8,11
DS-056,3,password reset,retail store,4,9
DS-057,3,shared mailbox access,retail store,33,11
DS-058,3,printer offline,retail store,8,24
DS-059,3,slow laptop,physical therapy office,4,42
DS-060,3,VPN connection failure,law office,38,40
DS-061,3,VPN connection failure,law office,34,27
DS-062,4,password reset,accounting office,9,12
DS-063,4,password reset,accounting office,12,11
DS-064,4,slow laptop,accounting office,19,23
DS-065,4,password reset,physical therapy office,12,10
DS-066,4,password reset,nonprofit,8,14
DS-067,4,shared mailbox access,medical office,22,16
DS-068,4,new-hire device setup,nonprofit,11,67
DS-069,4,printer offline,physical therapy office,12,15
DS-070,4,new-hire device setup,accounting office,14,78
DS-071,4,shared mailbox access,physical therapy office,9,17
DS-072,4,shared mailbox access,retail store,4,14
DS-073,4,printer offline,medical office,8,20
DS-074,4,VPN connection failure,retail store,36,17
DS-075,4,printer offline,medical office,4,28
DS-076,4,slow laptop,law office,22,31
DS-077,4,printer offline,physical therapy office,8,27
DS-078,4,password reset,medical office,26,11
DS-079,4,password reset,law office,12,8
DS-080,4,VPN connection failure,law office,38,25
```

Response:

```text
| Category | Total handle minutes |
|---|---|
| New-hire device setup | 552 |
| VPN connection failure | 365 |
| Slow laptop | 322 |
| Printer offline | 284 |
| Password reset | 227 |
| Shared mailbox access | 159 |

New-hire device setup took the most technician time, with 552 handle minutes over the four weeks.
```

Observation: Same six totals as Prompt 11, all matching the file. It did not fail. The chapter says only that a second model returned the same six totals.

## Prompt 14 (SUPERSEDED by Prompt 18 (review M1: a Tool line and a branded ticket 2 made the repair more than one change). Formerly the Fix It 11.1 symptom, attempt 4 of 4)

Model: Sonnet.

```text
Work Order. Goal: first replies to the three help desk tickets below. Tool: the free chat assistant I use at home, because it is fast. Deliverable: three replies, each under 80 words, signed "Deskside Support." Acceptance criteria: each reply is ready to send with no blanks, promises no fix time, and repeats the details the client gave so they know we read the ticket.

Ticket 1, from Dana at a physical therapy office, 602-555-0131: "The front desk printer won't print Mr. Hal Benton's home exercise sheet, and he's waiting at the desk."
Ticket 2, from Marcus at a law office: "Outlook keeps asking for my password after the update."
Ticket 3, from Priscilla at a nonprofit: "Can I get access to the volunteers@ shared mailbox? My director approved it in the email below."
```

Response:

```text
**Ticket 1 (Dana)**

Hi Dana, we received your ticket that the front desk printer won't print Mr. Hal Benton's home exercise sheet while he waits at the desk. To help us narrow it down, please tell us any error message on the printer or screen. If another computer can print, that may work in the meantime. We have your number, 602-555-0131, if we need to call.

Deskside Support

**Ticket 2 (Marcus)**

Hi Marcus, we received your ticket that Outlook keeps asking for your password after the update. To help us narrow it down, please tell us whether the prompt appears on every launch or only after a while, and whether you see any error text. Please don't change your password until we've looked into it. We'll follow up with next steps.

Deskside Support

**Ticket 3 (Priscilla)**

Hi Priscilla, we received your request for access to the volunteers@ shared mailbox. The director's approval email didn't come through with your ticket. Please ask your director to reply to this ticket directly from their own email address confirming the approval, or forward the original message. Once we have that, we'll proceed with your access request.

Deskside Support
```

Observation: Not shown in the chapter. Every criterion in the Work Order passes: replies of 65, 62, and 58 words by wc -w (each counted from after its "**Ticket k**" heading through "Deskside Support"), no blanks, no fix time promised, client details repeated. Reply 1 repeats the patient's name ("Mr. Hal Benton's home exercise sheet") and adds the requester's phone number ("We have your number, 602-555-0131, if we need to call."), which no criterion asked for. Reply 1 also adds advice nobody gave ("If another computer can print, that may work in the meantime."). Ticket 2 in the prompt named an email product by brand, and its reply repeats the brand, so the chapter cuts ticket 2 from both the prompt and the response with marked cuts and the vendor name appears only here in the log. Reply 3 says the approval email "didn't come through" and asks the director to confirm. The failure the candidate named reproduced: the input that must never leave the client went in, and the Work Order's own criteria could not catch it. Attempts 1-3 (Prompts 11-13) tested the other branch of the candidate (an output the tool could not produce) and did not fail.

## Prompt 15 (SUPERSEDED by Prompt 19 (review M1). Formerly the Fix It 11.1 repair)

Model: Sonnet.

```text
Work Order. Goal: first replies to the three help desk tickets below. Tool: the pilot chat assistant on the approved list, under the pilot's rules, so names and contact details are removed before pasting. Deliverable: three replies, each under 80 words, signed "Deskside Support." Acceptance criteria: each reply is ready to send with no blanks, promises no fix time, and repeats the details the client gave so they know we read the ticket.

Ticket 1, from a physical therapy office: "The front desk printer won't print a patient's home exercise sheet, and the patient is waiting at the desk."
Ticket 2, from a law office: "My email keeps asking for my password after the update."
Ticket 3, from a nonprofit: "Can I get access to the volunteers@ shared mailbox? My director approved it in the email below."
```

Response:

```text
**Ticket 1: Physical therapy office**

Hello,

Thank you for contacting us. We understand the front desk printer won't print a patient's home exercise sheet, and the patient is waiting at the desk. We're looking into it now. In the meantime, if you can, try sending the sheet to another printer or showing it to the patient on screen. Please reply with any error message you see on the printer or computer.

Deskside Support

---

**Ticket 2: Law office**

Hello,

Thank you for reaching out. We see that your email keeps asking for your password after the update. To help us narrow this down, please let us know which device you're using (computer, phone, or both) and which email app you open. Please don't send your password in your reply. We'll review this and follow up with next steps.

Deskside Support

---

**Ticket 3: Nonprofit**

Hello,

Thank you for your request. We see you're asking for access to the volunteers@ shared mailbox and that your director approved it in the email below. We'll review that approval and confirm it with the mailbox owner or an authorized approver before making changes. We'll update you once the review is complete.

Deskside Support
```

Observation: Not shown in the chapter. Replies of 68, 62, and 55 words by wc -w (same counting rule as Prompt 14). No patient name, requester name, or phone number appears. No blanks, no fix time promised ("We're looking into it now" sets no time). Reply 1 again adds advice nobody gave ("try sending the sheet to another printer or showing it to the patient on screen"), which fails the Output Checklist's "Nothing added?" check, and the chapter says so. Reply 3 now accepts the approval as stated and says it will confirm it with the mailbox owner or an authorized approver. The Deliverable and Acceptance criteria sentences are word for word the same as Prompt 14. The Tool line and the ticket text changed, both as consequences of the Requirements Sheet. Both Prompt 14 and Prompt 15 ran in the same test setup; the Tool line is the scenario.

## Prompt 16 (Section 11.3 worked example: a flyer image prompt requested before any Requirements Sheet)

Model: Sonnet.

````text
Write a prompt I can paste into an image generator to make the flyer for our community garden's spring workday: Saturday, March 7, from 8 to 11 a.m., at the garden at 5th Street and Palm Lane. Bring gloves and water. Tools are provided.
````

Response:

````text
Paste this into your image generator:

```
A bright, welcoming vertical flyer (portrait, 8.5x11 proportions) for a community garden spring workday. Illustration style: warm, hand-painted watercolor with soft edges, cheerful and friendly. Scene: a sunny community garden in early spring with raised wooden beds, young green seedlings, blooming tulips and daffodils, a wheelbarrow, and a few diverse neighbors of different ages happily planting and watering, with gloves on. Soft blue sky, a few puffy clouds, and a palm tree peeking in from the corner. Color palette: fresh greens, sunny yellow, soft sky blue, warm terracotta accents on a cream background.

Layout: large headline at the top, a clear illustration in the middle, and event details in a clean banner at the bottom. Use big, bold, highly legible rounded sans-serif lettering with strong contrast and generous spacing.

Text to include, spelled exactly:
Headline: "Spring Workday at the Community Garden"
Details:
"Saturday, March 7"
"8-11 a.m."
"5th Street & Palm Lane"
"Bring gloves and water. Tools provided!"

No other text, no logos, no watermarks, no extra words. Keep the text perfectly spelled, straight, and uncluttered.
```

A few tips:
- AI generators often misspell text. If that happens, generate the artwork without the text (delete the "Text to include" section and add "leave blank space for text at top and bottom"), then add the words in Canva, Google Slides, or Word.
- Add a line like "Everyone welcome" or your garden's name if you'd like, but fewer words usually means cleaner results.
- Double-check the date: March 7 falls on a Saturday in 2026, but in 2027 it's a Sunday. Make sure the day and date match the year of your event.
````

Observation: 280 words by wc -w. The response's image prompt asks the generator to render five lines of text (a headline and four detail lines: "Saturday, March 7", "8-11 a.m.", "5th Street & Palm Lane", "Bring gloves and water. Tools provided!"). Its first tip says generators often misspell text and suggests generating the artwork without text and adding words in a document; it names three office products there (vendor names inside the captured fence only). Its date tip holds: March 7, 2026 is a Saturday and March 7, 2027 is a Sunday (checked with Python's datetime). The image prompt also asks for "a few diverse neighbors of different ages," which raises Chapter 3's face check; the chapter does not discuss it. The response wraps the image prompt in a triple-backtick fence, so the chapter uses a four-backtick text fence. No image was generated: images cannot be captured.

## Prompt 17 (Section 11.1 worked example: a tool-type question (replaces Prompt 1))

Model: Sonnet.

```text
What kind of AI tool is best for sorting the support tickets that land in my small IT company's inbox each morning? Answer in under 100 words.
```

Response:

```text
A large language model (LLM)-based classifier is your best fit. Unlike rigid rule-based filters, it reads the ticket's actual wording, so it can categorize (hardware, network, account access), assign urgency, and flag outages even when customers describe problems vaguely.

For a small shop, the simplest route is a helpdesk platform with built-in AI triage (Zendesk, Freshdesk, HaloPSA), or an automation tool like Zapier or Make that sends each email to an LLM and routes it. Keep a human review step for anything marked urgent.
```

Observation: 84 words by wc -w. Its first sentence picks a type ("A large language model (LLM)-based classifier is your best fit.") without asking about inputs, privacy, approved tools, or who reads the result. Its second paragraph names products (help desk platforms and automation tools) and ends "Keep a human review step for anything marked urgent." The chapter shows the first paragraph and cuts the second with [...], so no vendor name appears in the chapter. A re-run (Prompt 20) also named products, in one paragraph, so Prompt 17 is the one shown.

## Prompt 18 (Fix It 11.1 symptom (re-capture, review M1): the short Work Order with no Tool line and a brand-free ticket 2 (the failure the chapter teaches from))

Model: Sonnet.

```text
Work Order. Goal: first replies to the three help desk tickets below. Deliverable: three replies, each under 80 words, signed "Deskside Support." Acceptance criteria: each reply is ready to send with no blanks, promises no fix time, and repeats the details the client gave so they know we read the ticket.

Ticket 1, from Dana at a physical therapy office, 602-555-0131: "The front desk printer won't print Mr. Hal Benton's home exercise sheet, and he's waiting at the desk."
Ticket 2, from Marcus at a law office: "My email keeps asking for my password after the update."
Ticket 3, from Priscilla at a nonprofit: "Can I get access to the volunteers@ shared mailbox? My director approved it in the email below."
```

Response:

```text
**Ticket 1: Dana**

Hi Dana,

We got your ticket: the front desk printer won't print Mr. Hal Benton's home exercise sheet, and he's waiting at the desk. We're looking at it now and will call you at 602-555-0131. In the meantime, if another printer in the office is available, try sending the sheet there so he isn't kept waiting.

Deskside Support

**Ticket 2: Marcus**

Hi Marcus,

Thanks for writing. We understand your email keeps asking for your password after the update. To help us narrow it down, please tell us which email app you use (Outlook, Apple Mail, phone, or web) and whether it happens on one device or several. Please don't change your password yet. We'll follow up once we have that.

Deskside Support

**Ticket 3: Priscilla**

Hi Priscilla,

Thanks for your request for access to the volunteers@ shared mailbox. Your message says your director approved it in the email below, but no approval came through with the ticket. Please reply with that email attached, or ask your director to confirm directly. Once we have it, we can move forward.

Deskside Support
```

Observation: First run, no re-run needed. Replies of 58, 61, and 55 words by wc -w (each counted from after its "**Ticket k: Name**" heading through "Deskside Support"). Every criterion in the Work Order passes: no blanks, no fix time ("We're looking at it now and will call you" sets no time), client details repeated. Reply 1 repeats the patient's name ("Mr. Hal Benton's home exercise sheet") and the requester's phone number ("will call you at 602-555-0131"). Reply 1 adds advice nobody gave ("if another printer in the office is available, try sending the sheet there"). Reply 2 names email products. The chapter shows reply 1 and cuts replies 2 and 3 with one [...]. Reply 3 says no approval came through with the ticket.

## Prompt 19 (Fix It 11.1 repair (re-capture, review M1): Prompt 18 with only the ticket text changed (names and contact details removed))

Model: Sonnet.

```text
Work Order. Goal: first replies to the three help desk tickets below. Deliverable: three replies, each under 80 words, signed "Deskside Support." Acceptance criteria: each reply is ready to send with no blanks, promises no fix time, and repeats the details the client gave so they know we read the ticket.

Ticket 1, from a physical therapy office: "The front desk printer won't print a patient's home exercise sheet, and the patient is waiting at the desk."
Ticket 2, from a law office: "My email keeps asking for my password after the update."
Ticket 3, from a nonprofit: "Can I get access to the volunteers@ shared mailbox? My director approved it in the email below."
```

Response:

```text
**Ticket 1: Physical therapy office**

Hello,

Thank you for reaching out. We understand the front desk printer won't print a patient's home exercise sheet, and the patient is waiting at the desk. We're looking at this now as a priority. In the meantime, if possible, please try printing from another computer or send the sheet to a different printer. Please reply with any error message you see.

Deskside Support

---

**Ticket 2: Law office**

Hello,

Thank you for your ticket. We understand your email keeps asking for your password after the update. Please don't enter your password repeatedly, as that can lock your account. Let us know which device and email program you use (such as Outlook or a phone app) and roughly when the update happened, so we can investigate.

Deskside Support

---

**Ticket 3: Nonprofit**

Hello,

Thank you for your request. You asked for access to the volunteers@ shared mailbox, and said your director approved it in the email below. We didn't see the approval attached to the ticket, so please reply with that email forwarded directly from your director. Once we have it, we can review the request.

Deskside Support
```

Observation: diff against Prompt 18: only the three ticket lines differ (names and the phone number removed, "Mr. Hal Benton's" and "he's" replaced by "a patient's" and "the patient is"). Replies of 64, 59, and 56 words by wc -w (same counting rule). No patient name, requester name, or phone number appears. No blanks, no fix time ("We're looking at this now as a priority" sets no time). Reply 1 adds advice nobody gave ("please try printing from another computer or send the sheet to a different printer"), which fails the Output Checklist's "Nothing added?" check. Reply 2 names an email product, so the chapter shows reply 1 only. Both Prompts 18 and 19 ran in the same test setup, so the tool switch the Requirements Sheet calls for is not tested by these runs, and the chapter says so.

## Prompt 20 (Re-run of Prompt 17 (logged, not shown))

Model: Sonnet.

```text
What kind of AI tool is best for sorting the support tickets that land in my small IT company's inbox each morning? Answer in under 100 words.
```

Response:

```text
A large language model (LLM) with a text-classification setup is the best fit. It can read each ticket's free text, then assign a category (password reset, network, hardware), a priority, and a suggested owner, with no training data required. Many helpdesk tools like Zendesk, Freshdesk, or Jira Service Management have this built in. If you want something custom, use an LLM via a simple automation (Zapier, Make, or Power Automate) that reads your inbox and tags or routes tickets. Keep a human review step for urgent or ambiguous ones.
```

Observation: 89 words by wc -w, one paragraph. Picks a type and names products throughout, so no clean trim exists. Not shown.

## Verification notes

All checks below ran on 2026-10-21 (late evening, America/Phoenix). Saved copies and extracts sit in the writer's scratchpad (`src11/`).

* Further Reading URLs. https://www.nist.gov/itl/ai-risk-management-framework 200 (plain `curl -sI`). https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence 200 (`curl -sIL`). https://www.w3.org/WAI/WCAG22/Understanding/images-of-text.html 200 (plain `curl -sI`). Also read, not linked: https://www.w3.org/TR/WCAG22/ 200; https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf and https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf return 404 to a HEAD request and 200 to a GET (both PDFs downloaded and read with `pdftotext -layout`). https://www.gao.gov/products/gao-21-519sp returned 403 with and without a browser user agent, so the GAO framework was not read and is not cited.
* NIST AI 100-1, AI RMF 1.0, January 2023 (cover). MAP 1.1: "Intended purposes, potentially beneficial uses, context-specific laws, norms and expectations, and prospective settings in which the AI system will be deployed are understood and documented." After the MAP function: "Framework users should have sufficient contextual knowledge about AI system impacts to inform an initial go/no-go decision about whether to design, develop, or deploy an AI system." MAP 3.5: "Processes for human oversight are defined, assessed, and documented." The chapter's Further Reading line paraphrases MAP 1.1 and the go/no-go sentence.
* NIST AI 600-1, Generative Artificial Intelligence Profile, July 2024 (cover). Its risk list includes "Data Privacy: Impacts due to leakage and unauthorized use, disclosure, or de-anonymization of biometric, health, location, or other personally identifiable information or sensitive data" and "Human-AI Configuration: Arrangements of or interactions between a human and an AI system which can result in the human inappropriately anthropomorphizing GAI systems or experiencing algorithmic aversion, automation bias, over-reliance, or emotional entanglement with GAI systems." The chapter quotes the risk name "Human-AI Configuration" and says it covers over-reliance.
* W3C, Understanding SC 1.4.5: Images of Text (Level AA), WCAG 2.2 Understanding docs: "What to do: Use text instead of pictures of text." Success criterion text: "If the technologies being used can achieve the visual presentation, text is used to convey information rather than images of text except for the following: Customizable ... Essential ..." The WCAG 2.2 page (https://www.w3.org/TR/WCAG22/) reads "W3C Recommendation 12 December 2024." The chapter quotes the "Use text instead of pictures of text" summary and paraphrases the criterion.
* Vendor pages for the Section 11.3 Tool check (all read 2026-10-21):
    * OpenAI, "Uploading files and audio to ChatGPT," https://help.openai.com/en/articles/8555545-uploading-files-and-audio-to-chatgpt (the older URL ending -file-uploads-faq redirects there). Plain curl got 403, so the page was read in the browser pane; the page said "Updated: 10 hours ago." Quoted: uploads of documents and spreadsheets "are available on Free and paid ChatGPT plans, subject to plan-specific limits"; spreadsheets "XLSX, XLS, CSV, TSV"; "CSV files and spreadsheets have a size limit of approximately 50 MB, depending on the size of each row."; "You can upload up to 80 files every 3 hours. Free users are limited to 3 file uploads per day. OpenAI may lower these limits during peak hours."
    * Google, "Upload & analyze files in Gemini Apps," https://support.google.com/gemini/answer/14903178?hl=en, 200 with a browser user agent. Quoted: "Up to 10 files (subject to availability) can be uploaded in the same prompt."; "Each video can be up to 2 GB. All other supported file types can be up to 100 MB."; "There are rolling limits for how much you can upload and analyze files in a period of time."; "If you try to upload a file that is too large, Gemini may provide a response that misses connections or details throughout the content." The page shows no last-updated date in its text.
    * Microsoft Learn, "Frequently asked questions about Microsoft Copilot Chat," https://learn.microsoft.com/en-us/copilot/faq, "Last updated on 10/19/2026," read in the browser pane. Quoted: "File upload: Lets users upload files like Word docs, Excel files, and PDFs to prompt Copilot Chat to reason over it as part of its response. Standard access and file upload limits apply."; "Uploaded files are stored in a user's OneDrive for Business."; "Per enterprise data protection promises, uploaded files aren't used to train the model." The page gives no file-size number; secondary sources disagree (1 MB, 10 MB, 512 MB) and were not used.
* `deskside-tickets.csv` (generated by `assets/code/_generators/gen_deskside_tickets.py`, seed 137, sha256 prefix f36a8ffc481d, byte-identical on a second run): 80 rows, 6 columns. Tickets by category: password reset 21, printer offline 15, VPN connection failure 14, shared mailbox access 12, slow laptop 10, new-hire device setup 8. Handle minutes by category: new-hire device setup 552, VPN connection failure 365, slow laptop 322, printer offline 284, password reset 227, shared mailbox access 159, total 1,909. First replies over 30 minutes: 12 (VPN 9, printer offline 1, new-hire 1, shared mailbox 1; by week 2, 2, 6, 2; IDs DS-007, DS-017, DS-030, DS-033, DS-040, DS-047, DS-048, DS-057, DS-060, DS-061, DS-074, DS-080). Rows at exactly 30 minutes: DS-027, DS-028, DS-032, DS-052. Computed with Python's csv module; a spreadsheet sort gives the same numbers.
* Chapter word counts: Prompt 17 84 words (Prompt 1, superseded, 81); Prompt 3 test plan 220 words with its title (wc -w on the lines from "# VPN Move Test Plan" through check 7); Prompt 10 114 words.
* Dates: March 7, 2026 is a Saturday and March 7, 2027 a Sunday; January 19, 2027 (the flyer brief) is a Tuesday; October 8, 2026 (the invoice case) is a Thursday. Checked with Python's datetime.
* Fictional details: phone numbers 602-555-0131, 602-555-0148 (Priya's, from Part II canon), and 480-555-0119 are in the fictional 555-01xx range. The card "ending in 4417" is four digits only. ZIP 85281 is a real Tempe ZIP code used as setting. The invoice number CW-2026-1043, "5th Street and Palm Lane," and the people Dana, Marcus, Priscilla, Mr. Hal Benton, and Renee are fictional. No fictional organization in the chapter or packet carries a name.
* Re-capture checks (2026-10-22): Prompt 18 replies 58, 61, 55 words and Prompt 19 replies 64, 59, 56 words by wc -w per reply; `diff caps-11/p18.txt caps-11/p19.txt` shows only the three ticket lines changed. The plumbing warranty claim in Section 11.3 and its "about 15 minutes" are author-written scenario facts, not a capture.
