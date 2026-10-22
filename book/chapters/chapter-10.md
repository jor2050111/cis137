# Chapter 10: Surveying and Comparing AI Platforms

A Deskside technician at Copperwind has an opinion about AI tools. "Just use the one everybody uses," he tells you. "It's the best." Another technician swears by a different one. Neither has tried both on the same ticket. Mei Lin has heard the argument three times this month, and she has a deadline. The pilot ends this quarter, and she must tell the owner which tools Copperwind adopts for next year, for which jobs, and why.

Her ask to you, the AI adoption assistant, is specific. She wants a Comparison Matrix for three help desk tasks. The first is a reply to a printer-offline ticket. The second is a four-bullet summary of a short client update, and the third is a plain explanation of two-step sign-in for a client's staff. She wants every tool tested the same way, and she wants the scores in counts. "Best" is not a score.

A literacy course stops at a list of tools. This chapter asks for more. You will survey artificial intelligence (AI) platforms by type and record each one on a card. You will judge tools against six stated criteria, and you will run the same test across tools so the comparison means something. Then you will keep the survey current, because tools change their plans, prices, and policies every month. Everything you build works on Copperwind's tasks and on your own IT projects.

## Module Overview 🧭

* **Estimated time:** 5-6 hours
* **Prerequisites:** Chapters 1 and 6 (the tool landscape, the types of AI, and comparing one prompt in two tools). Chapters 7, 8, and 9 (the Accuracy Audit, reading a data policy, and the pilot). Also the Output Checklist from Chapter 5 and the prompt log from Chapter 1.
* **Deliverables:** Skills Lab 10A deliverable (three Comparison Matrices, a Tool Survey card for each tool tested, and a note to Mei Lin), Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **10.1 (Evaluate):** Judge an AI platform against the six comparison criteria for a stated task, using evidence from a fair test (Sections 10.2-10.3)
* **10.2 (Evaluate):** Defend a ranking of two or more platforms on one task with a Comparison Matrix built from the same prompt, inputs, and criteria, scored in counts (Section 10.3)
* **10.3 (Evaluate):** Assess a Tool Survey card for currency and completeness, and decide when the tool must be tested again (Sections 10.1, 10.4)

### This chapter aligns with the following Course Learning Outcomes

* **CLO 6 (Evaluate):** Select appropriate AI solutions to address specific problems.
* **CLO 2 (Analyze):** Differentiate the major types of Artificial Intelligence (AI).

---

## 10.1 The Landscape by Type

Chapter 1 sorted generative tools into five kinds. The kinds still hold, and this chapter gives them the names you will write on a card. A **platform** is an AI product together with the service behind it. That means the tool you use, the plans it sells, the data policy that governs it, and the places it runs (a browser, a phone app, an office suite). You compare platforms, not logos, because two people using the "same" tool on different plans may get different limits and different data terms.

Here are the five types, in the order the card lists them:

* **General assistant:** a chat assistant built for any task, from drafting to explaining. Most are multimodal now.
* **Research tool:** answers with citations you can open, as Chapter 3 showed.
* **Image or media tool:** makes or edits pictures, audio, or video.
* **AI inside an office suite:** the assistant built into the email, document, and spreadsheet apps a team already uses.
* **Specialized tool:** built for one job, such as writing code, transcribing calls, or sorting tickets.

A platform sells its service in tiers. A **tier** is one plan level of a platform, such as free, paid, or business, each with its own price, limits, and often its own data terms. Chapter 1 defined the free tier. The tier matters for the matrix, because a tool's business tier may promise not to train on your input while its free tier does.

!!! note "Tool check (verified October 2026)"
    The course roster by type, from `docs/tool-roster.md`, with names checked on each vendor's own pages on October 22, 2026. General assistants: ChatGPT (OpenAI), Gemini (Google), Microsoft Copilot (Microsoft), and Claude (Anthropic, optional, and 18+ under its Consumer Terms). Research tools: Perplexity (Perplexity AI) and Gemini Notebook (Google, formerly NotebookLM). AI inside an office suite: Microsoft 365 Copilot or Copilot Chat, depending on what your school or work license includes. Image or media tools: the image feature inside a core assistant, or the image generator your syllabus names. Your syllabus names the tools you create accounts on.

### Two Type Questions

A survey asks two questions about every tool. The first is the job: which of the five types is it? The second comes from Chapter 1: what type of AI is behind it? Where does its behavior come from? The answer tells you how it fails. A rule-based feature fails the same way every time, and you can read the rule. A machine learning feature that sorts or predicts can be wrong in ways no rule explains. A generative feature can write a fluent sentence nobody said.

A plumbing contractor's office manager asked a chat assistant to sort the features in her scheduling software:

```text
I manage the office at a plumbing contractor. Our scheduling software lists the six features below. For each one, say whether it is most likely rule-based, machine learning that sorts or predicts but does not generate, or generative AI, and give the clue in one short sentence. If the description cannot tell you, say so.

1. Sends "We got your request" to every customer who emails us.
2. Suggests a job category (leak, drain, or water heater) from the customer's description.
3. Drafts a reply to a customer's email for our dispatcher to edit.
4. Moves any invoice unpaid for 60 days to a "Follow up" list.
5. Predicts how long a job will take from past jobs of the same kind.
6. Writes a summary of the technician's notes for the invoice.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
1. **Rule-based.** The same fixed response goes to every email, with no judgment involved.

2. **Machine learning (sorts/predicts).** It assigns text to one of a few set categories, which is classification. (It could be a simple keyword rule, so the description can't fully confirm ML, but "suggests" from free-text description points to a classifier.)

3. **Generative AI.** It produces new written text tailored to each email.

4. **Rule-based.** A fixed threshold (60 days unpaid) triggers a fixed action.
[...]
6. **Generative AI.** It writes new summary text from the technician's notes.
```

Every sort matches the clues in the descriptions. Item 2 is the useful one. The tool admits a keyword rule could do the same job, so the description alone cannot settle it. The vendor's documentation can. Apply Chapter 1's judgment test too: items 1 and 4 follow rules but replace no judgment, so by this book's test they are not AI at all. For the survey, the type of AI decides the check. The generative features (3 and 6) get the Accuracy Audit, because they can add claims. The category suggestion needs a count of wrong categories, the way a pilot counts errors.

### The Tool Survey Card

You record each platform on one card. The **Tool Survey** is your set of Tool Survey cards, one per tool, kept as the index of every AI tool you use or might use. Each card has eight fields, in this order:

* **Name:** the product and the tier you use.
* **Type:** general assistant, research tool, image or media tool, AI inside an office suite, or specialized tool.
* **What it is for:** the jobs you would give it.
* **Tier and cost:** the plan and its price, with the date you checked.
* **Data policy:** two lines, with the date and where you read it.
* **Access:** how you sign in, and any age or district rule.
* **Last tested:** the task, the date, and the matrix score.
* **Notes:** what to watch, what it gets wrong, and when to test again.

The template is `tool-survey-card-template.md` in this chapter's data pack. Copperwind's survey starts with the tools Deskside might adopt. Yours starts with the tools your own IT project already uses. If you keep a home lab, that may be a general assistant you ask about server settings and the AI summary feature in your note app. Both get a card, because both see your work.

### Try It Yourself 10.1: Your First Card 🛠️

**Predict:** Pick one tool you can use today, from the roster or from your own IT project. Before you open any vendor page, predict two answers for its free tier: does it train on your input by default, and what does its next tier cost?

**Run:** Fill `tool-survey-card-template.md` for that tool. Read the Tier and cost and Data policy lines from the vendor's own pages, and write the page title, the URL, and today's date. Under Type, name the tool type and, in one line of Notes, the type of AI behind its main feature. Leave Last tested as "not yet." The filled card is the artifact you keep: it is the first card in your Tool Survey.

**Explain:** Which prediction missed? In 1-2 sentences, explain why a card needs the date beside a price and a policy line.

### Quick Check 10.1 ✅

1. A museum gift shop's point-of-sale system flags any sale over \$500 for a manager's approval, and it also suggests which items to reorder from last year's sales. Classify each feature by the type of AI behind it, and name the check each one needs.
2. A coworker's card reads "Name: the AI assistant. Type: AI. Tier and cost: free." Rewrite the three fields so a colleague could act on them, and say what is still missing.

---

## 10.2 The Six Criteria

"Which tool is best?" has no answer until you name the task and the tests. The Comparison Matrix in Section 10.3 uses six criteria, always in this order. Each one is there because a tool can win on the others and still fail a team.

### Capability and Accuracy

Capability asks whether the tool did the task. A museum gift shop manager wanted a tool to read a photo of a handwritten inventory sheet. The free tier she tried would not take the photo, so the tool scored a fail before anyone checked a word. Score capability with the task's own checks, the way Chapter 5's Output Checklist scores a response: right task, right shape.

Accuracy on your task asks how many of the tool's claims hold, counted with the Accuracy Audit from Chapter 7. "On your task" is the point. A small accounting firm read that one tool tops a public test of reasoning. Then it audited ten of the tool's drafted client letters against its own records and found 3 contradicted dates. Chapter 9 drew this line. A benchmark is someone else's test. Your counts come from your work.

### Cost and Privacy

Cost is the tier and its price on the date you checked, times the people who need it. Copperwind's pilot tool quotes \$30 per user per month. For five Deskside technicians, that is \$150 a month. Write the date beside the number, because prices move.

Privacy and data policy asks what the tool keeps and whether it trains on your input, from your reading of the data policy in Chapter 8. A university housing office handles records that FERPA may cover (Chapter 8). A free tier that trains on chats by default fails this criterion for that office, however good its drafts are. The same vendor's business tier may pass. Score the tier, not the brand.

### Accessibility and Integration

**Accessibility**, as a selection criterion, asks whether the people who must use the tool can use it: with a screen reader, with only a keyboard, and on the devices they have. A city animal shelter's volunteer coordinator uses a screen reader. One tool she tried gave her an unlabeled send button that her screen reader announced only as "button." A tool she cannot operate scores zero for her, whatever its accuracy. The W3C's standard for accessible web content is WCAG 2.2, a W3C Recommendation dated December 12, 2024 (read October 21, 2026). It sets the bar for keyboard use in Success Criterion 2.1.1, which begins "All functionality of the content is operable through a keyboard interface" and then lists narrow exceptions. You can test the basics yourself in five minutes. Many vendors also publish an Accessibility Conformance Report, and the U.S. government's Section508.gov explains how buyers should read one.

**Integration** asks whether the tool fits where the work happens: the office suite, the ticket system, the browser. A car dealership's service desk writes every repair note in its service system. A browser tool means copying each note out and each draft back in. Every paste costs a minute and invites a privacy slip, such as a customer's phone number pasted along with the note. An assistant inside the suite the advisors already use may win on integration while it loses on accuracy, and the matrix keeps both findings in view.

### Criteria a Tool Suggests

Could a chat assistant just hand you the criteria? Here is what one said:

```text
I am choosing an AI tool for a small IT help desk team that drafts first replies to client tickets. List the criteria I should compare tools on, one line each, at most eight. Do not name any products.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
1. **Draft accuracy:** How often replies are technically correct and actually address the client's issue with minimal editing.
2. **Ticketing integration:** Native or easy connection to your help desk/PSA system so drafts appear inside the existing workflow.
3. **Knowledge grounding:** Ability to draw on your own documentation, past tickets, and runbooks rather than generic answers.
[...]
5. **Data privacy and security:** Handling of client data, retention and training policies, encryption, and compliance (e.g., SOC 2, GDPR).
6. **Human review controls:** Draft-only mode, approval steps, and clear flagging of low-confidence or risky responses.
7. **Cost and scalability:** Per-seat or usage pricing that fits a small team and holds up as ticket volume grows.
[...]
```

It is a sensible list. Accuracy, integration, privacy, and cost all appear. Three of its items (grounding, review controls, and tone, cut above) are checks you could run inside capability for this task. One criterion is missing from all eight lines: accessibility. A list that leaves out the people who cannot use the tool will pick a tool some of your team cannot use. Treat the tool's list as a lead. The six criteria stay fixed, so a matrix for one task can sit beside a matrix for another.

### Try It Yourself 10.2: The Checks for Your Task 🛠️

**Predict:** Pick one task from your own IT project, such as a runbook for a quarterly password rotation, a test plan for a VPN change, or a build checklist for a home lab server. Predict which of the six criteria will be hardest to make checkable for that task.

**Run:** Open `comparison-matrix-template.md` and fill only its top part: the task in one sentence, and the "How you check it" line for each of the six criteria. Make each line a test with a pass or a count. Two examples: "every step matches my server's notes, counted with the Accuracy Audit," and "I can send a prompt and copy the response using only the keyboard." This checks table is the artifact you keep: it is the top of your first Comparison Matrix.

**Explain:** Which line was hardest to make checkable? In 1-2 sentences, explain whether your prediction held and what made that criterion hard.

### Quick Check 10.2 ✅

1. A community garden's volunteer lead picks a tool because it scored highest on a public test. Name the two criteria that test cannot score for the garden, and say how the lead would score each one.
2. A small accounting firm's tool passes capability and accuracy, but it trains on chats by default and the firm's staff would paste client tax records. Decide whether the tool fails the matrix or only one column, and justify your answer.
3. Write the "How you check it" line for accessibility for a team of four, one of whom uses a screen reader and two of whom work mostly on phones.

---

## 10.3 The Fair Test and the Comparison Matrix

Chapter 6 compared one prompt in two tools with five rules: the same prompt, the same input, fresh conversations, the same day, and the same criteria. The fair test keeps all five and turns them into a record a manager can check. The **fair test** is the same task, the same prompt, the same inputs, and the same criteria for every tool compared, each run as a fresh conversation, scored with counts.

The record goes on a **Comparison Matrix**, a table whose rows are tools and whose columns are the six criteria. The columns run in this order:

1. **Capability:** did it do the task?
2. **Accuracy on your task:** the Accuracy Audit counts.
3. **Cost:** the tier and price on the date checked.
4. **Privacy and data policy:** what it keeps, and whether it trains on your input.
5. **Accessibility:** it works with a screen reader and a keyboard, on the devices your people use.
6. **Integration:** it fits where the work happens.

One matrix covers one task. A tool that wins the printer reply may lose the summary. The same holds on your own IT project. A matrix comparing two assistants on a test plan for a VPN change uses one prompt, your own change notes as the input, and the same six columns.

Two rules keep a matrix honest:

* **Counts, never a leaderboard.** Each cell holds a count or a short finding with its evidence. Do not add the columns into one score. A privacy fail is not offset by three extra holds.
* **Runs and readings stay apart.** Capability and accuracy come from runs. Cost, privacy, accessibility, and integration come from reading pages and trying the tool. The matrix says which is which.

### Try It Yourself 10.3: Task 1, Problem-First 🛠️

**Predict:** Open `fair-test-tasks.txt` and read Task 1, the printer-offline ticket, and its four checks. Predict which check a tool is most likely to fail.

**Run:** Write your own prompt for Task 1. Send it word for word to two tools from your roster, each in a fresh conversation, on the same day. A good result passes these checks:

* It uses only the three Deskside steps, in order, and adds no other step.
* It promises no time, not even the 2 p.m. pickup.
* It runs under 100 words.
* It is signed "Deskside Support."

Score capability as checks passed out of 4. Then run the Accuracy Audit on each reply against the ticket and the steps, and write the counts. Fill the capability and accuracy cells of both rows in a copy of `comparison-matrix-template.md`. The two filled rows are the artifact you keep.

**Explain:** Compare your runs with the sample below. In 1-2 sentences, explain whether the difference between your two rows came from the tools or from chance between runs, and what a second run would show.

Here is one reasonable prompt for the task. Send the prompt without the [Step] lines:

```text
[Step 1: name the writer and the reader]
You are a Deskside support technician at a managed IT services company. The reader is an office worker at a client company, not a technical person.
[Step 2: name the job and paste the input exactly]
Write a first reply to this ticket: "The printer by the front window shows offline on my computer, but the person at the next desk can still print to it. I need to print shipping labels before the 2 p.m. pickup."
[Step 3: hand over the only steps the reply may use]
Use only these Deskside steps, in this order: (1) Check that the printer's network cable is plugged in, or that its screen shows a Wi-Fi connection. (2) On one office computer, open the printer list, remove the printer, and add it again. (3) If it still shows offline, reply to this ticket, and a technician will connect remotely during business hours.
[Step 4: set the shape and the limits the checks will score]
Format: under 100 words, plain text, the three steps numbered, signed "Deskside Support." Do not promise a time, and do not add any other steps.
```

Tool A's reply:

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Hello,

Since your coworker can still print, the printer itself is likely fine. Please try these steps in order:

1. Check that the printer's network cable is plugged in, or that its screen shows a Wi-Fi connection.
2. On one office computer, open the printer list, remove the printer, and add it again.
3. If it still shows offline, reply to this ticket, and a technician will connect remotely during business hours.

Deskside Support
```

Tool B's reply, same prompt, same day, fresh conversation:

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Subject: Re: Printer by front window showing offline

Hello,

Thank you for reporting this. Please try these steps in order:

1. Check that the printer's network cable is plugged in, or that its screen shows a Wi-Fi connection.
2. On one office computer, open the printer list, remove the printer, and add it again.
3. If it still shows offline, reply to this ticket, and a technician will connect remotely during business hours.

Deskside Support
```

Both replies pass all four checks. Each uses the three steps word for word, in order, promises no time, and is signed correctly. Tool A runs 74 words and Tool B runs 75, counting its subject line. The difference shows up in the audit. Tool A adds a claim: "the printer itself is likely fine." The ticket says a coworker can print, which holds. That the printer is fine is a guess nobody at Deskside made, and it could lead the reader to skip step 1. Mark it Not in source. Tool B's "Thank you for reporting this" is courtesy, not a claim.

One run is a lead. The results are close, so each tool got a second fresh run of the same prompt. Tool A came back at 71 words with the guess again, now stated flatly:

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Hello,

Since your coworker can still print, the printer itself is working. Please try these steps:
[...]
```

Tool B came back at 64 words with no added claim. Two runs each, the same pattern. Here are the two rows:

| Tool | Capability | Accuracy on your task | Cost | Privacy and data policy | Accessibility | Integration |
| --- | --- | --- | --- | --- | --- | --- |
| Tool A | 4 of 4 checks, both runs | 5 claims checked, 4 hold, 1 not in source, both runs | Same vendor and setup as Tool B | Same as Tool B | Not tested (command line) | Not tested (command line) |
| Tool B | 4 of 4 checks, both runs | 3 claims checked, 3 hold, both runs | Same vendor and setup as Tool A | Same as Tool A | Not tested (command line) | Not tested (command line) |

On Task 1, Tool B ranks ahead by one Not in source claim, repeated in two runs. The finding says nothing about the summary or the sign-in task, and the last four columns cannot separate these two tools at all.

!!! note "Tool check (verified October 2026)"
    Tool A and Tool B in this chapter are two models from the same vendor, run through the textbook author's command-line test setup, not two chat apps. That is why their cost, privacy, accessibility, and integration cells carry no finding. Your matrix compares roster tools from different vendors, so all six columns will carry findings. Your syllabus names the roster.

### Reading a Row

A filled matrix still needs judgment. Three habits turn it into a decision:

* **A must-pass failure decides alone.** Some criteria a team cannot live without, such as privacy for client records or accessibility for a teammate who uses a screen reader. A tool that fails one is out for that task. Strong counts elsewhere do not buy it back.
* **A small gap is a lead.** One claim or one check apart, in one run each, is not a ranking. Run again, as the Task 1 runs above did.
* **Say what the matrix cannot see.** Three tasks on one day say nothing about a year of tickets, a busy Monday, or a vendor's next update. Chapter 9's pilot measures those, in counts and minutes, on your own work.

The matrix answers "which tool, for this task, today." The Use Evaluation from Chapter 9 answers "is the use worth it." Mei Lin needs both.

### Fix It 10.1: The Sign-In Row 🔧

A Deskside technician builds the matrix for Task 3, the two-step sign-in explanation. He runs the task in Tool A and in Tool B, each in a fresh conversation on the same day, and scores both rows.

**Symptom:** Tool B looks far worse. His fair test record holds the two prompts he sent. Tool A got this one:

```text
Explain two-step sign-in to the office staff at one of our client companies. Most of them are not technical, so use plain words and explain any technical word in the same sentence. Keep it under 150 words. Facts: Starting Monday, December 7, 2026, every staff email account uses two-step sign-in. After you type your password, you approve the sign-in in the authenticator app on your work phone, or you type the six-digit code the app shows. We do not use text-message codes. When you set it up, you get ten backup codes. Keep them somewhere safe, not in your email. If you lose your phone, call Deskside during support hours, Monday to Friday, 7 a.m. to 6 p.m. Include this line word for word: "No one from Copperwind will ever ask you for your password or for a sign-in code."
```

Tool B got this one:

```text
Explain two-step sign-in to the office staff at one of our client companies. Most of them are not technical, so use plain words and explain any technical word in the same sentence. Keep it under 150 words.
```

Here is the response it gave (captured from a chat assistant, October 2026):

```text
Two-step sign-in, also called two-factor authentication, adds a second check to your password. After you type your password, the system sends a short code to your phone or asks you to approve a prompt in an app. You then enter that code or tap approve. This protects your account even if someone learns your password, because they would also need your phone. Keep your phone nearby when you log in. Never share the code with anyone, even if they say they are from IT or the company. If you get a code you did not request, do not enter it, and report it to the IT help desk right away.
```

His two rows, scored against the facts in `fair-test-tasks.txt`. The audit counts every claim, glosses included. A clause that explains a term counts when it adds a fact the facts do not carry, such as "also called two-factor authentication."

| Tool | Capability | Accuracy on your task |
| --- | --- | --- |
| Tool A | 4 of 4 checks | 9 claims checked, 7 hold, 1 not in source, 1 unverifiable |
| Tool B | 2 of 4 checks | 8 claims checked, 2 hold, 1 contradicted, 5 not in source |

Tool B's reply says the system "sends a short code to your phone," and the facts say "We do not use text-message codes." That is the contradicted claim. It also leaves out the start date, the backup codes, and the standing promise. He writes "Tool A for sign-in explanations" in his note to Mei Lin.

**Diagnose:** Before you touch the matrix, list everything the two rows had in common and everything that differed. Then name, in one sentence, what the accuracy column is measuring.

**Repair:** The task, the day, the fresh conversations, and the checks were the same. The prompts were not. Tool A's prompt carried the facts: the date, the app, no text codes, the backup codes, support hours, and the promise. Tool B's did not, so Tool B wrote what two-step sign-in usually looks like, and the usual version includes text codes. The column measured which prompt held the facts, not which tool explains better. The repair changes one thing: Tool B gets Tool A's prompt, word for word, in a fresh conversation. Tool A's row, the task, and the checks stay as they were:

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
**Two-step sign-in is coming to your work email on Monday, December 7, 2026.** Starting then, you will need two things to sign in: your password and a quick approval. After you type your password, you either approve the sign-in in the authenticator app (a phone app that confirms it is really you) on your work phone, or you type the six-digit code the app shows. We do not use text-message codes.

When you set this up, you will receive ten backup codes, which you can use if you can't reach your phone. Keep them somewhere safe, not in your email.

If you lose your phone, call Deskside during support hours: Monday to Friday, 7 a.m. to 6 p.m.

No one from Copperwind will ever ask you for your password or for a sign-in code.
```

**Verify:** Score the new row the same way. It runs 134 words, explains "authenticator app" in the same sentence, adds no other sign-in method, and carries the promise word for word: 4 of 4 checks. The audit finds 8 claims, 7 hold, and 1 not in source. The gloss "which you can use if you can't reach your phone" states a use the facts never give. The "two things" sentence restates the approval claim, so it is folded into it, the merge rule from Chapter 7. The gloss on "authenticator app" restates the approval step, so it adds no fact.

Tool A's reply to the same prompt also scored 4 of 4, with 9 claims, 7 holding. Its first two sentences carry one of its misses:

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
**Two-step sign-in starts Monday, December 7, 2026**

Starting Monday, December 7, 2026, every staff email account will use two-step sign-in. This means proving who you are twice, not just once, so a stranger who learns your password still cannot get in.
[...]
```

"A stranger who learns your password still cannot get in" is Unverifiable, because it is a promise about what will happen, the kind no record can settle (Chapter 7). Tool A's other miss is a gloss in its cut lines: backup codes "which are one-time passcodes for emergencies," Not in source. Now the rows compare tools. On Task 3, Tool B is ahead by one claim, in one run each. His note to Mei Lin changes from "Tool A" to "Tool B slightly ahead on this task, one run each." One claim in one run is a lead, so the next step is a second run of each.

### Try It Yourself 10.4: Fill the Rest of the Row 🛠️

**Predict:** Take the two tools from Try It Yourself 10.3. Predict which of the last four criteria (cost, privacy and data policy, accessibility, integration) will separate them most.

**Run:** Fill those four cells for both rows. Cost and privacy come from the vendor's own pages, with the date: use the Tier and cost and Data policy lines of a Tool Survey card if you have one. For accessibility, send a prompt and copy the response using only the keyboard, then turn on your device's built-in screen reader and listen to one response. For integration, write where Copperwind's Deskside work happens (the ticket system, the email client, the browser) and whether each tool reaches it. Then write the matrix's "What the matrix shows" lines: the ranking with its counts, the criterion that decided it, and one thing the matrix cannot tell you. The finished two-row matrix for Task 1 is the artifact you keep.

**Explain:** Was your prediction right? In 1-2 sentences, explain whether the reading-based columns changed the ranking your runs gave you.

### Quick Check 10.3 ✅

1. A car dealership's service manager tests three tools on the same prompt. Tool C gets 9 of 10 claims holding, but she ran it the next morning after a vendor update. Decide whether her matrix is a fair test, and say what she must do before ranking Tool C.
2. A teammate adds the six columns into one total and reports "Tool A: 23 points, Tool B: 21 points." Critique the report, and rewrite the top line of it in counts and findings.
3. Use the Task 1 matrix rows in this section to write the two-sentence finding you would give Mei Lin, including what the rows cannot tell her.

---

## 10.4 The Tool Survey: Keeping It Current

A matrix is true on the day you ran it. Vendors change their plans, prices, data terms, and models without asking you, sometimes monthly. A card that was right in March can mislead a colleague in October. The Tool Survey is a living index, so it needs two habits: dates on every fact, and a rule for when to test again.

Even names move. A vendor can rename a product, and its old plans page can redirect to the new name. A card written before the change points a colleague at a name the vendor no longer uses. The callout below has a case from this term.

!!! note "Tool check (verified October 2026)"
    Tiers and data defaults, read on October 22, 2026, from each vendor's own pages (U.S. prices). Settings can differ by account, so read your own plan's settings too.

    ChatGPT (OpenAI): a Free plan, and Plus at \$20 a month ("What is ChatGPT Plus?"). OpenAI "may use conversations to improve model performance and safety." You can turn off "Improve the model for everyone" under Settings, then Data controls. OpenAI says it does not train on Business, Enterprise, or Edu workspace content by default ("Data controls in ChatGPT").

    Gemini (Google): Free at \$0, Google AI Plus at \$4.99 a month, Google AI Pro at \$19.99 a month, and Gemini Enterprise from \$21 per seat per month (Gemini subscriptions page). "If you're 18 or over, Keep Activity is on by default" ("Manage & delete your activity in Gemini Apps"). With it on, Google uses your activity to improve its services "including training generative AI models," and activity auto-deletes after 18 months by default. Chats you have with Keep Activity off are kept with your account for 72 hours (Gemini Apps Privacy Hub, updated October 19, 2026).

    Microsoft: the Microsoft Copilot app works with a personal Microsoft account, and people without a Microsoft 365 subscription may see ads ("Microsoft Copilot for individuals: your privacy controls and choices"). Microsoft 365 Premium costs \$19.99 a month. The Microsoft 365 Copilot Business add-on is listed from \$18 per user per month, paid yearly, a promotional price down from \$21 (Microsoft 365 Copilot pricing page). For the Copilot app updated on August 18, 2026: "Prompts, responses, and your file contents when using the Microsoft Copilot app aren't used to train foundation models" ("Microsoft Copilot for individuals: your activity history"). "Copilot in Microsoft 365 apps for home: your data and privacy" says the same for Copilot in Word, Excel, and the other home apps. The older "Privacy FAQ for Microsoft Copilot" now covers only the app before that update. Its 18-month storage line does not appear on the new pages, so treat retention for the new app as unverified. Work and school accounts follow separate terms.

    Claude (Anthropic): Free at \$0, and Pro at \$20 billed monthly (pricing page). New users choose the training setting at signup, so read your own Privacy Settings. Anthropic keeps chats five years if you allow training and 30 days if you do not. The change covers only the Free, Pro, and Max plans ("Updates to Consumer Terms and Privacy Policy," August 28, 2025). The Privacy Center article "Is my data used for model training?" (March 16, 2026) states no default.

    Perplexity: Free, plus Pro at \$17 a month and Max at \$167 a month, both billed annually (Perplexity Pro page). For Free, Pro, and Max users, "AI Data Retention is enabled by default." You can turn it off in Account settings, then Preferences ("Data Collection at Perplexity," March 3, 2026).

    Gemini Notebook (Google, formerly NotebookLM): the old NotebookLM plans address now redirects to a page headed "Gemini Notebook Plans." Its FAQ says "NotebookLM is now Gemini Notebook as of July 2026." It lists a standard plan for personal projects and higher limits inside Google AI Plus, Pro, and Ultra. "When you use Gemini Notebook as an individual, your data is not used for training unless you share feedback."

### Last Tested and the Review Date

Two parts of the survey keep it honest. On each card, the Last tested field says what the score rests on: which task, which date, which matrix. On the survey itself, a review date says when you will check every card again. Copperwind's starter survey reviews every three months.

Between reviews, some events mean a tool gets the fair test again right away:

* **The vendor changes the model or the plan you use.** The scores came from the old one.
* **The data policy or the terms change.** The privacy cell may flip.
* **The task changes.** A new ticket type is a new matrix.
* **Someone reports a failure.** One report is a lead worth a re-run.
* **Last tested is older than the review period.** The score has gone stale.

Here is how the Last tested line reads on the starter card for Tool A, written from the Task 1 matrix in Section 10.3:

* **Last tested:** Task 1 (printer-offline first reply), October 21, 2026. Capability 4 of 4 checks in both runs. Accuracy 5 claims checked, 4 hold, 1 not in source, in both runs

The same field works on your own IT project. Say you use an assistant on a home lab. Its card might read: "Last tested: build checklist for a home lab server, from my own setup notes, 12 steps checked, 11 hold, 1 contradicted (a port number)." A colleague reading either line knows what the score rests on, and how old it is.

Write the triggers that fit each tool in its Notes field. A card for the AI inside your note app might say "test again when the app updates its AI feature."

### Asking a Tool to Check a Card

Can a chat assistant review a card for you? It can see what is missing. It cannot see what changed at a vendor last week. Here is a card from a teammate's survey, sent for review. Send the prompt without the [Step] lines:

```text
[Step 1: give the date the check is measured from]
Today is October 21, 2026.
[Step 2: name what the card belongs to and the job]
I keep a survey of the AI tools my team uses, one card per tool. Review the card below. List every field that is missing, incomplete, or possibly out of date, and say what the card's owner should do about each.
[Step 3: set a shape you can act on]
One line per item.
[Step 4: keep the tool checking, not supplying]
Do not fill in any missing fact yourself.

Card:
* Name: Tool C (research tool, free plan)
* Type: research tool
* What it is for: finding sources for client-facing explainers
* Tier and cost: Free. Paid plan $20 a month (checked March 4, 2026)
* Data policy: Keeps your search history.
* Access: Personal email sign-in
* Last tested: Task 2 (four-bullet summary), March 12, 2026, 3 of 4 checks passed
* Notes:
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
[...]
- **Tier and cost:** The $20/month price was checked March 4, 2026, which is about 7.5 months ago. The owner should recheck current pricing and plan terms and update the date. The card also doesn't say which tier the team actually uses, so the owner should state that.
- **Data policy:** "Keeps your search history" is vague and has no source or date. The owner should record how long history is kept, whether it is used for training, who can see it, whether it can be deleted, and the date it was checked against the vendor's policy. This is the riskiest gap because the tool is used for client-facing work.
[...]
- **Last tested (scope):** Only one task was tested, a four-bullet summary, which is not source-finding, the tool's stated purpose. The owner should test source-finding and record how the sources were verified.
[...]
- **Notes:** Empty. The owner should add known limitations, the failed check's details, the owner's name, and a review date, or write "none" if there is nothing to add.
[...]
```

The review is useful. It found the undated data policy line, the stale price, the empty Notes, and the sharpest gap: the card's only test was a summary, not the job the tool is for. It flagged "possibly out of date" by counting months from the dates on the card, which is all it can do. It cannot tell you whether the price changed. Only the vendor's page can. Its first line (cut above) also flagged "Tool C" as a placeholder, which is fair, since a real card names the product. Use a tool's review for completeness. Do currency yourself, with the vendor's page open and today's date.

The Tool Survey goes in your Toolkit, the set of tools you keep, which Chapter 12 assembles. By the end of this course you should be able to say which tools you will use next week, and the survey is where that answer lives.

### Try It Yourself 10.5: Review a Card 🛠️

**Predict:** Take your card from Try It Yourself 10.1. Predict which field a reviewer will flag first, and whether that flag is about completeness or currency.

**Run:** Send the card-review prompt above with your card in place of the Tool C card. Mark each item the response lists COMPLETE (a missing or vague field you can fix now) or CURRENT (a fact that needs a vendor page and today's date). Fix every COMPLETE item, recheck every CURRENT item on the vendor's page, and write two re-test triggers in the card's Notes. Then open `tool-survey-starter.md`, copy your card into a blank slot, and fill the survey's review date. The Tool A card there is your model of a Last tested line. The reviewed survey, with its review date, is the artifact you keep.

**Explain:** Was the first flag the one you predicted? In 1-2 sentences, explain why a tool can check a card's completeness but not its currency.

### Quick Check 10.4 ✅

1. A university housing office's card for its general assistant shows a data policy line read 11 months ago, and the vendor announced a new plan last week. Decide whether the tool gets the fair test again now or at the next review, and justify your answer with the re-test triggers.
2. Write the Notes line, with two re-test triggers, for the AI summary feature in a ticket system that a small office network project uses.

---

## 10.5 Summary and Retrieval 💡

### Key Concepts

* A platform is a product plus its plans, data policy, and the places it runs. The Tool Survey sorts platforms into five types and records each on a card with eight fields, every fact dated.
* The type of AI behind a feature (rule-based, machine learning, or generative) tells you how it fails and which check it needs.
* The six criteria, in order, are capability, accuracy on your task, cost, privacy and data policy, accessibility, and integration. A tool can win five and still fail a team on the sixth.
* The fair test gives every tool the same task, prompt, inputs, and criteria, each in a fresh conversation, scored with counts. A different prompt per tool measures the prompts, not the tools.
* A Comparison Matrix holds one task. Its cells carry counts and findings, never a total, and it separates what came from runs from what came from reading.
* One run is a lead. Close results get a second fresh run before you rank.
* The survey stays current through dates on every fact, a review date, and re-test triggers. A tool can check a card for completeness. Only the vendor's page settles currency.

### Key Terms

See course glossary for full definitions

* platform, tier, Tool Survey (Section 10.1)
* accessibility, integration (Section 10.2)
* fair test, Comparison Matrix (Section 10.3)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Name the six criteria of the Comparison Matrix in order, and say which two come from runs.
2. Name the eight fields of a Tool Survey card in order, and the two fields that must carry a date.
3. State the fair test in one sentence, and name the one change that repaired the sign-in row in Fix It 10.1.
4. From Chapter 8: Name the seven sections of the AI Use Policy in order, and say which section a Tool Survey would feed.
5. From Chapter 6: Name the four traits of a checkable criterion.

---

## 10.6 Skills Lab 10A: The Help Desk Comparison Matrix

**Goal:** Build Copperwind's Comparison Matrix for three help desk tasks with the fair test across at least two roster tools. Fill a Tool Survey card for each tool, and write Mei Lin a note on which tool fits which task and what the matrix cannot tell her.

**Starter files:** Provided files in `assets/code/chapter-10/` from the course data pack. Your answer file is `skills-lab-10a-worksheet.md`, and `fair-test-tasks.txt` holds Mei Lin's three tasks, their inputs, and their checks. The sheets are `comparison-matrix-template.md`, `tool-survey-card-template.md`, and `tool-survey-starter.md` (one filled card and three blank ones). Download the data pack from Canvas, extract it, and work at the extracted `cis137` root. Open each file in any text editor and never retype its contents. The lab files are fictional, so you may paste them into a chat assistant once your privacy plan allows it. You first met Copperwind in Chapter 1, and this lab gives you everything it needs, so you do not need any earlier file.

### Part 1: Foundation (Aligns with Objective 10.1)

Work in `skills-lab-10a-worksheet.md`, which has a space for every task below. Read `fair-test-tasks.txt` in full before you write anything.

1. Before you send any prompt, write your privacy plan in two columns: what from the lab files may go into a tool, and what stays out of every prompt. Give the reason for each item that stays out.
2. Choose at least two tools from your roster. For each one, fill the Name, Type, What it is for, Tier and cost, Data policy, and Access fields of `tool-survey-card-template.md`. Read each vendor fact from the vendor's own page, and write its title, URL, and today's date.
3. Make three copies of `comparison-matrix-template.md`, one per task. In each, fill the task line and the "How you check it" line for all six criteria. Use the task's checks from `fair-test-tasks.txt` for capability.

### Part 2: Application (Aligns with Objectives 10.1 and 10.2)

1. Write one prompt per task. You may reuse the chapter's prompts for Tasks 1 and 3, and you must write Task 2's prompt yourself. Paste each prompt into its matrix's fair test record. Send it word for word to every tool, each in a fresh conversation, on the same day. Paste every prompt and response into your log with the tool and the date.
2. Score capability as checks passed, and run the Accuracy Audit on every response against the task's inputs. Write the counts in each matrix. Where two tools land within one claim or one check of each other, run each again in a fresh conversation and record both runs.
3. Fill the cost, privacy and data policy, accessibility, and integration cells for every tool. For accessibility, run the keyboard-only test and the screen reader test from Try It Yourself 10.4. For integration, name where Deskside's work happens and whether the tool reaches it.

### Part 3: Extension (Aligns with Objectives 10.2 and 10.3)

1. For each task, write the "What the matrix shows" lines: the ranking with its counts, the criterion that decided it, and one thing the matrix cannot tell you.
2. Finish a Tool Survey card for each tool you tested. Fill Last tested with the task, the date, and the matrix score, and write two re-test triggers in Notes. Add the cards to `tool-survey-starter.md` and fill its review date.
3. Add one card for a tool your own IT project uses or could use. Then write one line naming the tool you will use next week for that project and the criterion that decided it.
4. Write a note to Mei Lin (150 to 200 words). Say which tool fits which task, with the counts behind each choice. Name the criterion that most changed your view, and say what the matrix cannot tell her about a full year of use.

### Questions & Analysis 🤔

Answer both questions in the worksheet's final section. These answers carry significant rubric weight.

1. Quote the capability and accuracy cells from your matrix for the task where your tools were closest, and the log entries behind them. Explain whether a second run changed the ranking (or why your counts did not call for one), and what another run would need to show to change it.
2. Quote one cell your matrix filled from reading instead of running (cost, privacy, accessibility, or integration), with the vendor page line and date from your log. Argue how your note to Mei Lin would change if that line changed next month.

**Submission:** Submit your completed worksheet as one file named `skills-lab-10a-lastname.md`. Keep every answer under its task heading, with your three matrices and your Tool Survey cards pasted into their sections. Include every prompt you sent, the tool and date, and every response you received, pasted exactly, with your Questions & Analysis answers clearly labeled at the end. Keep a copy of your Tool Survey for yourself. It is a working tool you can keep using.

### Rubric: Skills Lab 10A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria, five
levels from Mastery to Not Evident. The criteria are Technical
Accuracy and Efficiency, Output Quality, Documentation Quality, and
Analysis, Interpretation, and Response to QUESTION(s). The criteria
and levels are the same everywhere. Your instructor sets the point
values in your course. Check the syllabus and the Canvas rubric
attached to this lab for the values that apply to you.

---

## 10.7 Review Questions 🔄️

1. **Understand:** Explain to a coworker, in no more than three sentences, why a Comparison Matrix holds one task instead of ranking tools for every job at once.

2. **Apply:** A plumbing contractor wants to compare two general assistants for drafting job estimates from technicians' notes. Write the fair test record for the matrix: the task, what goes in the prompt, the inputs, the runs, and the date rule.

3. **Analyze:** A university housing office's matrix shows Tool A at "10 claims checked, 10 hold" and Tool B at "10 claims checked, 8 hold." Tool A was tested on move-in emails and Tool B on maintenance replies. Analyze what the two rows can and cannot support, and name the one change that would make them comparable.

4. **Evaluate:** A small accounting firm's matrix for client reminder emails shows Tool A ahead on accuracy by 2 claims in two runs. Tool A's free tier trains on input by default, and Tool B's business tier does not, at \$25 per user per month for 6 staff. Recommend which tool the firm should adopt for this task, defend your choice with the matrix, and name the one finding that would change your answer.

---

## Further Reading 📖

* [Web Content Accessibility Guidelines (WCAG) 2.2 (W3C Recommendation)](https://www.w3.org/TR/WCAG22/): The W3C's standard for accessible web content, dated December 12, 2024. Success Criterion 2.1.1, Keyboard, is the test behind this chapter's keyboard-only check.
* [Easy Checks: A First Review of Web Accessibility (W3C Web Accessibility Initiative)](https://www.w3.org/WAI/test-evaluate/preliminary/): Simple checks anyone can run on a web page, including keyboard access. The page says plainly that it is not a complete evaluation.
* [Buy Accessible Products and Services (Section508.gov)](https://www.section508.gov/buy/): The U.S. government's guide for buyers, including how to read a vendor's Accessibility Conformance Report. Read it for the questions to ask a vendor about the accessibility column.
* [Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence): NIST's July 26, 2024 companion to the NIST AI RMF for generative AI. It lists risks and actions an organization can use when it chooses and checks a tool.
* [Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design (Sclar and others, 2023)](https://arxiv.org/abs/2310.11324): Small changes to a prompt's format can swing a model's results, and the effect differs between models. It is the research case for sending every tool the same prompt.

---

## Looking Ahead ⏩

You can now survey platforms by type, compare them with a fair test, and keep the survey current. Chapter 11 starts from the other end. You will define the problem before you name a tool, match a tool from your Tool Survey to each Copperwind scenario, and decide when the right answer is no AI at all.
