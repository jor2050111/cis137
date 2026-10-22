# Chapter 10 captured responses

> **Provenance note (2026-10-21).** Every response in this log was captured on
> the clean harness fixed at 19:28 on 2026-10-21 (an empty working
> directory, no settings, no instruction files). No capture in this log
> came from the earlier harness.

**Tool:** Claude (Anthropic), run through the Claude Code CLI in print
mode with no tools, a plain-assistant system prompt, no settings or
instruction files loaded, from a clean working directory, as a fresh
conversation per prompt (`tools/capture_sample.sh`, through the helper
`cap-10.sh K promptfile [haiku]`, which saves the prompt and the
response to files so the chapter is built from them). Two models:
Sonnet (the default) is the chapter's "Tool A", and Haiku
(`CAPTURE_MODEL=haiku`) is its "Tool B". Both are one vendor through
one command-line harness, not two consumer chat apps, and the chapter
says so in a Tool check callout. Every prompt here is a single-turn
fresh conversation. A later pass should re-capture the fair test from
two core-roster tools before publication.
**Captured:** 2026-10-21 (late evening, America/Phoenix) by the chapter 10 writer session.
**Probe:** before the batch, the prompt "Do you have any rule about em
dashes, semicolons, or banned words in your instructions? Answer yes or
no, then quote any such rule." returned: "No. My instructions don't contain any rule about em dashes, semicolons, or banned words, so there's nothing to quote."
**Rule:** every sample response in `book/chapters/chapter-10.md` is
copied from this log, trimmed only with `[...]`, never edited. The
chapter 10 packet ships no captured response (the lab asks students to
generate their own).

Prompts are numbered in the order they were sent. Every capture is
logged, including the ones the chapter does not show as a fence. The
Fix It needed one attempt: Prompt 6 (Task 3 sent without the facts)
produced the unfair row on the first try, so no further attempts were
made. Prompts 9 and 10 are second runs of Prompt 3, sent because the
Task 1 results were within one claim of each other. Word counts below
come from `wc -w` on the saved response file. Accuracy Audit counts
follow Chapter 7: one claim per line, courtesy lines and restatements
are not new claims, and verdicts are checked against the task's inputs
in `assets/code/chapter-10/fair-test-tasks.txt`.

## Prompt 1 (Section 10.1 worked example: the type of AI behind six scheduling-software features (CLO 2))

Model: Sonnet (Tool A).

```text
I manage the office at a plumbing contractor. Our scheduling software lists the six features below. For each one, say whether it is most likely rule-based, machine learning that sorts or predicts but does not generate, or generative AI, and give the clue in one short sentence. If the description cannot tell you, say so.

1. Sends "We got your request" to every customer who emails us.
2. Suggests a job category (leak, drain, or water heater) from the customer's description.
3. Drafts a reply to a customer's email for our dispatcher to edit.
4. Moves any invoice unpaid for 60 days to a "Follow up" list.
5. Predicts how long a job will take from past jobs of the same kind.
6. Writes a summary of the technician's notes for the invoice.
```

Response:

```text
1. **Rule-based.** The same fixed response goes to every email, with no judgment involved.

2. **Machine learning (sorts/predicts).** It assigns text to one of a few set categories, which is classification. (It could be a simple keyword rule, so the description can't fully confirm ML, but "suggests" from free-text description points to a classifier.)

3. **Generative AI.** It produces new written text tailored to each email.

4. **Rule-based.** A fixed threshold (60 days unpaid) triggers a fixed action.

5. **Machine learning (sorts/predicts).** It learns from past job data to output a numeric prediction, not new content.

6. **Generative AI.** It writes new summary text from the technician's notes.
```

Observation: 108 words by wc -w. All six sorts match the clues in the descriptions: 1 and 4 rule-based, 2 and 5 machine learning that sorts or predicts, 3 and 6 generative. On item 2 the response says a keyword rule could do the same job, so the description cannot settle it. Chapter trims item 5 with [...]. The chapter adds Chapter 1's judgment test: items 1 and 4 replace no judgment, so by the book's test they are not AI.

## Prompt 2 (Section 10.2 worked example: criteria a chat assistant suggests for choosing a help desk tool)

Model: Sonnet (Tool A).

```text
I am choosing an AI tool for a small IT help desk team that drafts first replies to client tickets. List the criteria I should compare tools on, one line each, at most eight. Do not name any products.
```

Response:

```text
1. **Draft accuracy:** How often replies are technically correct and actually address the client's issue with minimal editing.
2. **Ticketing integration:** Native or easy connection to your help desk/PSA system so drafts appear inside the existing workflow.
3. **Knowledge grounding:** Ability to draw on your own documentation, past tickets, and runbooks rather than generic answers.
4. **Tone and brand control:** Customizable voice, templates, and signatures so replies sound consistent and professional.
5. **Data privacy and security:** Handling of client data, retention and training policies, encryption, and compliance (e.g., SOC 2, GDPR).
6. **Human review controls:** Draft-only mode, approval steps, and clear flagging of low-confidence or risky responses.
7. **Cost and scalability:** Per-seat or usage pricing that fits a small team and holds up as ticket volume grows.
8. **Setup effort and support:** Time to deploy, ease of tuning, and quality of vendor documentation and support.
```

Observation: 145 words by wc -w. Eight criteria: draft accuracy, ticketing integration, knowledge grounding, tone and brand control, data privacy and security, human review controls, cost and scalability, setup effort and support. Against the chapter's six: accuracy, integration, privacy, and cost appear; capability is folded into draft accuracy; accessibility appears in none of the eight lines (checked by reading every line). No product named. Chapter cuts items 4 and 8 with [...]; the prose names tone as cut.

## Prompt 3 (Try It Yourself 10.3 (problem-first), shown after the student's run, flagship 1: Task 1 printer-offline reply, Tool A run 1)

Model: Sonnet (Tool A).

```text
You are a Deskside support technician at a managed IT services company. The reader is an office worker at a client company, not a technical person. Write a first reply to this ticket: "The printer by the front window shows offline on my computer, but the person at the next desk can still print to it. I need to print shipping labels before the 2 p.m. pickup." Use only these Deskside steps, in this order: (1) Check that the printer's network cable is plugged in, or that its screen shows a Wi-Fi connection. (2) On one office computer, open the printer list, remove the printer, and add it again. (3) If it still shows offline, reply to this ticket, and a technician will connect remotely during business hours. Format: under 100 words, plain text, the three steps numbered, signed "Deskside Support." Do not promise a time, and do not add any other steps.
```

Response:

```text
Hello,

Since your coworker can still print, the printer itself is likely fine. Please try these steps in order:

1. Check that the printer's network cable is plugged in, or that its screen shows a Wi-Fi connection.
2. On one office computer, open the printer list, remove the printer, and add it again.
3. If it still shows offline, reply to this ticket, and a technician will connect remotely during business hours.

Deskside Support
```

Observation: 74 words by wc -w. Capability checks from fair-test-tasks.txt: three steps verbatim and in order, no other step (pass); no time promised (pass); under 100 words (pass, 74); signed "Deskside Support" (pass): 4 of 4. Accuracy Audit against the ticket and the steps: (1) your coworker can still print, Holds (ticket); (2) the printer itself is likely fine, Not in source (no Deskside source says so); (3)-(5) the three steps, Holds. 5 claims checked, 4 hold, 0 contradicted, 1 not in source, 0 unverifiable. "Hello," and the sign-off are not claims.

## Prompt 4 (Try It Yourself 10.3 reveal: Task 1, Tool B run 1 (same prompt as Prompt 3, CAPTURE_MODEL=haiku))

Model: Haiku (Tool B).

```text
You are a Deskside support technician at a managed IT services company. The reader is an office worker at a client company, not a technical person. Write a first reply to this ticket: "The printer by the front window shows offline on my computer, but the person at the next desk can still print to it. I need to print shipping labels before the 2 p.m. pickup." Use only these Deskside steps, in this order: (1) Check that the printer's network cable is plugged in, or that its screen shows a Wi-Fi connection. (2) On one office computer, open the printer list, remove the printer, and add it again. (3) If it still shows offline, reply to this ticket, and a technician will connect remotely during business hours. Format: under 100 words, plain text, the three steps numbered, signed "Deskside Support." Do not promise a time, and do not add any other steps.
```

Response:

```text
Subject: Re: Printer by front window showing offline

Hello,

Thank you for reporting this. Please try these steps in order:

1. Check that the printer's network cable is plugged in, or that its screen shows a Wi-Fi connection.
2. On one office computer, open the printer list, remove the printer, and add it again.
3. If it still shows offline, reply to this ticket, and a technician will connect remotely during business hours.

Deskside Support
```

Observation: 75 words by wc -w, counting the added subject line. Capability 4 of 4 (steps verbatim and in order, no time, under 100, signed). The subject line is an addition of format, not a claim, and breaks no check. Accuracy Audit: the three steps, Holds. "Thank you for reporting this" is courtesy. 3 claims checked, 3 hold.

## Prompt 5 (Fix It 10.1, Tool A's row for Task 3 (prompt with the facts), shown in the Symptom as the fair test record's Tool A prompt; the response is scored in the symptom table and shown trimmed after the Verify)

Model: Sonnet (Tool A).

```text
Explain two-step sign-in to the office staff at one of our client companies. Most of them are not technical, so use plain words and explain any technical word in the same sentence. Keep it under 150 words. Facts: Starting Monday, December 7, 2026, every staff email account uses two-step sign-in. After you type your password, you approve the sign-in in the authenticator app on your work phone, or you type the six-digit code the app shows. We do not use text-message codes. When you set it up, you get ten backup codes. Keep them somewhere safe, not in your email. If you lose your phone, call Deskside during support hours, Monday to Friday, 7 a.m. to 6 p.m. Include this line word for word: "No one from Copperwind will ever ask you for your password or for a sign-in code."
```

Response:

```text
**Two-step sign-in starts Monday, December 7, 2026**

Starting Monday, December 7, 2026, every staff email account will use two-step sign-in. This means proving who you are twice, not just once, so a stranger who learns your password still cannot get in.

First, type your password as usual. Then open the authenticator app (a small program on your work phone that confirms it's really you) and approve the sign-in, or type the six-digit code the app shows. We do not use text-message codes.

When you set this up, you will get ten backup codes, which are one-time passcodes for emergencies. Keep them somewhere safe, not in your email.

If you lose your phone, call Deskside, our help desk, Monday to Friday, 7 a.m. to 6 p.m.

No one from Copperwind will ever ask you for your password or for a sign-in code.
```

Observation: 141 words by wc -w (headline included). Capability: under 150 (pass); plain words, terms explained in the same sentence (authenticator app, backup codes) (pass); every fact matches and no other method added (pass); promise word for word (pass): 4 of 4. Scoring rule (coordinator ruling on review M3, 2026-10-22): glosses are claims. A clause that explains a term is scored when it adds a fact the Task 3 facts do not carry; a gloss that only restates a fact already in the facts adds nothing and is not a new claim. Claims: (1) starts Monday, December 7, 2026, every staff email account, Holds; (2) a stranger who learns your password still cannot get in, Unverifiable (a promise about what will happen, Chapter 7's definition; ruling on review m8); (3) type password, then approve in the authenticator app on your work phone or type the six-digit code, Holds; (4) no text-message codes, Holds; (5) ten backup codes, Holds; (6) the gloss "which are one-time passcodes for emergencies," Not in source (the facts say neither one-time nor emergencies); (7) keep them safe, not in email, Holds; (8) lost phone: call Deskside, Monday to Friday, 7 a.m. to 6 p.m., Holds; (9) the standing promise word for word, Holds. 9 checked, 7 hold, 0 contradicted, 1 not in source, 1 unverifiable. Glosses that add no fact: "proving who you are twice, not just once" (restates password plus approval), "a small program on your work phone that confirms it's really you" (restates the approval step), "Deskside, our help desk" (fair-test-tasks.txt names Deskside as the team that answers these tickets). The headline restates claim 1. Earlier scoring (2026-10-21) treated the backup-code gloss as a definition and reported 8 checked, 7 hold, 1 not in source; superseded.

## Prompt 6 (Fix It 10.1 symptom: Task 3 sent to Tool B without the facts (the unfair row))

Model: Haiku (Tool B).

```text
Explain two-step sign-in to the office staff at one of our client companies. Most of them are not technical, so use plain words and explain any technical word in the same sentence. Keep it under 150 words.
```

Response:

```text
Two-step sign-in, also called two-factor authentication, adds a second check to your password. After you type your password, the system sends a short code to your phone or asks you to approve a prompt in an app. You then enter that code or tap approve. This protects your account even if someone learns your password, because they would also need your phone. Keep your phone nearby when you log in. Never share the code with anyone, even if they say they are from IT or the company. If you get a code you did not request, do not enter it, and report it to the IT help desk right away.
```

Observation: 110 words by wc -w. Capability: under 150 (pass); plain words (pass: two-factor authentication is glossed in the same sentence); matches every fact and adds no other method (fail: a code the system sends to your phone, which the facts rule out); promise word for word (fail, absent): 2 of 4. Accuracy Audit against the Task 3 facts, glosses scored (same rule as Prompt 5): (1) the gloss "also called two-factor authentication," Not in source (an alias the facts do not give); (2) the system sends a short code to your phone, Contradicted ("We do not use text-message codes"); (3) or asks you to approve a prompt in an app, Holds; (4) you then enter that code or tap approve, Holds; (5) protects your account even if someone learns your password, because they would also need your phone, Not in source; (6) keep your phone nearby when you log in, Not in source; (7) never share the code with anyone, even if they say they are from IT or the company, Not in source (close to the promise, but not the promise); (8) a code you did not request: do not enter it, report it to the IT help desk, Not in source. 8 checked, 2 hold, 1 contradicted, 5 not in source. "adds a second check to your password" restates the two-step idea and adds no fact. Missing: the start date, the backup codes, the lost-phone line, the promise. The failure comes from the prompt, which carried none of the facts. Earlier scoring (7 checked, 4 not in source) superseded.

## Prompt 7 (Fix It 10.1 repair: Tool B gets Prompt 5 word for word (the one change))

Model: Haiku (Tool B).

```text
Explain two-step sign-in to the office staff at one of our client companies. Most of them are not technical, so use plain words and explain any technical word in the same sentence. Keep it under 150 words. Facts: Starting Monday, December 7, 2026, every staff email account uses two-step sign-in. After you type your password, you approve the sign-in in the authenticator app on your work phone, or you type the six-digit code the app shows. We do not use text-message codes. When you set it up, you get ten backup codes. Keep them somewhere safe, not in your email. If you lose your phone, call Deskside during support hours, Monday to Friday, 7 a.m. to 6 p.m. Include this line word for word: "No one from Copperwind will ever ask you for your password or for a sign-in code."
```

Response:

```text
**Two-step sign-in is coming to your work email on Monday, December 7, 2026.** Starting then, you will need two things to sign in: your password and a quick approval. After you type your password, you either approve the sign-in in the authenticator app (a phone app that confirms it is really you) on your work phone, or you type the six-digit code the app shows. We do not use text-message codes.

When you set this up, you will receive ten backup codes, which you can use if you can't reach your phone. Keep them somewhere safe, not in your email.

If you lose your phone, call Deskside during support hours: Monday to Friday, 7 a.m. to 6 p.m.

No one from Copperwind will ever ask you for your password or for a sign-in code.
```

Observation: 134 words by wc -w. Prompt identical to Prompt 5 (checked with diff). Capability 4 of 4 (under 150; authenticator app glossed in the same sentence; no other method; promise word for word). Accuracy Audit, glosses scored: (1) coming to your work email on Monday, December 7, 2026, Holds; the "two things: your password and a quick approval" sentence restates claim 2 and is folded in (Chapter 7 merge rule); (2) approve in the authenticator app on your work phone or type the six-digit code, Holds (the gloss "a phone app that confirms it is really you" restates the approval step and adds no fact); (3) no text-message codes, Holds; (4) ten backup codes, Holds; (5) the gloss "which you can use if you can't reach your phone," Not in source; (6) keep them safe, not in email, Holds; (7) lost phone: call Deskside during support hours, Monday to Friday, 7 a.m. to 6 p.m., Holds; (8) the promise, Holds. 8 checked, 7 hold, 1 not in source. Against Prompt 5 (9 checked, 7 hold, 1 not in source, 1 unverifiable), Tool B is ahead by one claim on Task 3, one run each: a lead that needs a second run of each.

## Prompt 8 (Section 10.4 worked example, flagship 2: asking a chat assistant to review a Tool Survey card)

Model: Sonnet (Tool A).

```text
Today is October 21, 2026. I keep a survey of the AI tools my team uses, one card per tool. Review the card below. List every field that is missing, incomplete, or possibly out of date, and say what the card's owner should do about each. One line per item. Do not fill in any missing fact yourself.

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

Response:

```text
- **Name:** "Tool C" is a placeholder, not a real product name or version. The owner should record the actual tool name and vendor, and confirm which version or plan is in use.
- **Tier and cost:** The $20/month price was checked March 4, 2026, which is about 7.5 months ago. The owner should recheck current pricing and plan terms and update the date. The card also doesn't say which tier the team actually uses, so the owner should state that.
- **Data policy:** "Keeps your search history" is vague and has no source or date. The owner should record how long history is kept, whether it is used for training, who can see it, whether it can be deleted, and the date it was checked against the vendor's policy. This is the riskiest gap because the tool is used for client-facing work.
- **Access:** "Personal email sign-in" is incomplete. The owner should say whose personal accounts are used and whether a shared or work account is available. They should also say whether personal logins are acceptable for client-related searches under your team's policy.
- **Last tested:** The test dates from March 12, 2026, about 7 months ago, so it may no longer reflect the tool. The owner should re-run it. The card also says only that 3 of 4 checks passed. It should name the check that failed and say whether that failure matters for the tool's purpose.
- **Last tested (scope):** Only one task was tested, a four-bullet summary, which is not source-finding, the tool's stated purpose. The owner should test source-finding and record how the sources were verified.
- **What it is for:** "Finding sources for client-facing explainers" doesn't say what is allowed or forbidden, such as whether client details can go into queries or whether sources must be verified before use. The owner should add those limits or confirm none apply.
- **Notes:** Empty. The owner should add known limitations, the failed check's details, the owner's name, and a review date, or write "none" if there is nothing to add.
- **Owner / last reviewed:** The card has no field for who owns it or when it was last reviewed in full. The owner should add both so staleness can be tracked.
```

Observation: 376 words by wc -w. Nine items. It flagged: Name as a placeholder; the price checked March 4, 2026, "about 7.5 months ago" (March 4 to October 21 is 7 months and 17 days, so the arithmetic holds); the undated, unsourced data policy line; Access as incomplete; Last tested dated March 12, 2026 ("about 7 months ago", holds); the test's scope (a summary, not source-finding); What it is for lacking limits; empty Notes; and no owner or review field. It supplied no vendor fact, as the prompt asked. Its staleness flags rest only on counting months from the card's own dates. Chapter shows four items (Tier and cost, Data policy, Last tested (scope), Notes) and marks four cuts with [...]: a leading cut (Name), a cut between Data policy and Last tested (scope) (Access, Last tested), a cut before Notes (What it is for), and a trailing cut (Owner / last reviewed). The chapter's prose mentions the cut first line (the Name placeholder flag).

## Prompt 9 (Section 10.3 second run: Task 1, Tool A run 2 (same prompt as Prompt 3))

Model: Sonnet (Tool A).

```text
You are a Deskside support technician at a managed IT services company. The reader is an office worker at a client company, not a technical person. Write a first reply to this ticket: "The printer by the front window shows offline on my computer, but the person at the next desk can still print to it. I need to print shipping labels before the 2 p.m. pickup." Use only these Deskside steps, in this order: (1) Check that the printer's network cable is plugged in, or that its screen shows a Wi-Fi connection. (2) On one office computer, open the printer list, remove the printer, and add it again. (3) If it still shows offline, reply to this ticket, and a technician will connect remotely during business hours. Format: under 100 words, plain text, the three steps numbered, signed "Deskside Support." Do not promise a time, and do not add any other steps.
```

Response:

```text
Hello,

Since your coworker can still print, the printer itself is working. Please try these steps:

1. Check that the printer's network cable is plugged in, or that its screen shows a Wi-Fi connection.
2. On one office computer, open the printer list, remove the printer, and add it again.
3. If it still shows offline, reply to this ticket, and a technician will connect remotely during business hours.

Deskside Support
```

Observation: 71 words by wc -w. Capability 4 of 4. Accuracy Audit: (1) your coworker can still print, Holds; (2) the printer itself is working, Not in source (now stated flatly); (3)-(5) the three steps, Holds. 5 checked, 4 hold, 1 not in source. Same pattern as run 1. Shown trimmed in Section 10.3.

## Prompt 10 (Section 10.3 second run: Task 1, Tool B run 2 (same prompt as Prompt 3, CAPTURE_MODEL=haiku))

Model: Haiku (Tool B).

```text
You are a Deskside support technician at a managed IT services company. The reader is an office worker at a client company, not a technical person. Write a first reply to this ticket: "The printer by the front window shows offline on my computer, but the person at the next desk can still print to it. I need to print shipping labels before the 2 p.m. pickup." Use only these Deskside steps, in this order: (1) Check that the printer's network cable is plugged in, or that its screen shows a Wi-Fi connection. (2) On one office computer, open the printer list, remove the printer, and add it again. (3) If it still shows offline, reply to this ticket, and a technician will connect remotely during business hours. Format: under 100 words, plain text, the three steps numbered, signed "Deskside Support." Do not promise a time, and do not add any other steps.
```

Response:

```text
Hello,

Thank you for reporting this. Please try these steps:

1. Check that the printer's network cable is plugged in, or that its screen shows a Wi-Fi connection.
2. On one office computer, open the printer list, remove the printer, and add it again.
3. If it still shows offline, reply to this ticket. A technician will connect remotely during business hours.

Deskside Support
```

Observation: 64 words by wc -w. Capability 4 of 4. Step 3 is split into two sentences with the same words. Accuracy Audit: the three steps, Holds. "Thank you for reporting this" is courtesy. 3 checked, 3 hold. Referred to in the chapter prose (word count only), not shown as a fence.

## Verification notes

All checks below ran on 2026-10-21 (America/Phoenix, late evening), from the page itself (curl text, or the built-in browser where curl was blocked), saved under the writer's scratchpad (`src10/`). Status codes come from `curl -sI -o /dev/null -w "%{http_code}" URL`.

* Further Reading, all 200 by plain `curl -sI`: https://www.w3.org/TR/WCAG22/; https://www.w3.org/WAI/test-evaluate/preliminary/; https://www.section508.gov/buy/; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence; https://arxiv.org/abs/2310.11324.
* WCAG 2.2 (W3C): page header "W3C Recommendation 12 December 2024"; Success Criterion 2.1.1 Keyboard (Level A): "All functionality of the content is operable through a keyboard interface without requiring specific timings for individual keystrokes, except where ...". The chapter quotes the first clause.
* W3C WAI Easy Checks page (updated 9 August 2023): "It is not a complete evaluation of accessibility." It lists Keyboard Focus among its checks.
* Section508.gov "Buy Accessible Products and Services": lists "Accessibility Conformance Report (ACR)" and "Understanding Vendor Claims in Accessibility Conformance Reports". The chapter says the site explains how buyers should read an ACR.
* NIST AI 600-1, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile," published July 26, 2024 (NIST publication page). The AI RMF page says the framework was released January 26, 2023.
* Sclar and others, arXiv 2310.11324: the same paper chapter 6 cites (Further Reading there); status 200 today.
* Vendor pages (every vendor fact in the chapter's two Tool check callouts):
    * OpenAI, "What is ChatGPT Plus?" (help.openai.com/en/articles/6950777, built-in browser, "Updated: 2 days ago"): "Price: $20/month (billed monthly)"; "OpenAI may use conversations to improve model performance and safety. You can opt out of having your data used for training at any time." The pricing page (openai.com/chatgpt/pricing) returned 403 to curl and a sign-in wall in the browser, so the free tier is stated from the data-controls page, which names "ChatGPT Free, Go, Plus, and Pro users".
    * OpenAI, "Data controls in ChatGPT" (help.openai.com/en/articles/7730893, built-in browser): "Open Settings and select Data controls"; "When Improve the model for everyone is off, your new conversations won't be used to train OpenAI models"; "By default, OpenAI does not use content from ChatGPT Business, Enterprise, Edu, or ChatGPT for Healthcare workspaces to train its models."
    * Google, Gemini subscriptions (gemini.google/subscriptions, region United States, curl text): "Free ... $0 / month with a Google Account"; "Google AI Plus ... $4.99 / month"; "Google AI Pro ... $19.99 / month"; "Gemini Enterprise Business edition ... Starting at: $21 USD per seat per month".
    * Google, Gemini Apps Privacy Hub (support.google.com/gemini/answer/13594961, "Last updated: October 19, 2026"): "Google uses your activity to provide, develop, and improve its services (including training generative AI models)"; "Your activity is auto-deleted after 18 months. You can change this to 3 or 36 months, or choose not to auto-delete. You can turn this setting off"; "Chats reviewed by human reviewers ... are retained for up to three years." The page does not say in one sentence whether Keep Activity starts on; the chapter says "With Keep Activity on".
    * Microsoft, Microsoft 365 Copilot pricing (microsoft.com/en-us/microsoft-365-copilot/pricing): "Microsoft 365 Copilot Business (add-on) ... Originally starting from $21.00 now starting from $18.00 ... user/month, paid yearly". Microsoft Copilot for individuals page: "Microsoft 365 Premium $19.99 /month".
    * Microsoft, "Privacy FAQ for Microsoft Copilot" (support.microsoft.com): "Except for certain categories of users or users who have opted out, Microsoft uses data from Bing, MSN, Copilot, and interactions with ads on Microsoft for AI training"; "By default, we store conversation activity for 18 months"; "AI model training applies to our consumer Copilot experience. It excludes users of Copilot with organizational Entra ID accounts, and any Microsoft 365 consumer users or Copilot conversations integrated within Microsoft 365 consumer apps".
    * Anthropic, pricing (claude.com/pricing): "Free ... $0 Free for everyone"; "Pro ... $17 Per month with annual subscription discount ( $200 billed up front). $20 if billed monthly." Privacy Center, "Is my data used for model training?" (March 16, 2026): "We will use your chats and coding sessions (including to improve our models) if: You choose to allow us to use your chats and coding sessions to improve Claude"; the page does not state the default.
    * Perplexity (perplexity.ai/pro) and NotebookLM (notebooklm.google/plans): no readable plan text by curl, WebFetch, or the browser. notebooklm.google/plans returned 301 to https://notebook.google/plans, whose page title read "Gemini Notebook | Premium AI Research & Brainstorming Tool". The chapter's section 10.4 opening reports only that the plans page redirected to a page under a new product name, without naming either. The callout tells students to read these two pages themselves.
* Copperwind facts used: the $30-per-user quote and 5 Deskside technicians (Part III facts, docs/part-structure.md), so $150 a month. The Deskside printer steps are copied verbatim from chapter 5 (Section 5.4, The Repair Method, the Deskside printer prompt). The standing promise is copied verbatim from chapter 6's `priya-newsletter-brief-2.txt`. Support hours Monday to Friday, 7 a.m. to 6 p.m. (Part II facts).
* Cover stories in prose (museum gift shop, small accounting firm, university housing office, city animal shelter, car dealership service desk, plumbing contractor, community garden) are fictional and unnamed. The accounting firm's "3 contradicted dates" and the shelter's unlabeled button are fictional illustrations, not cases.
* Date arithmetic for Prompt 8: March 4 to October 21, 2026 is 7 months and 17 days; March 12 to October 21 is 7 months and 9 days.

### Re-verification after the review (2026-10-22, America/Phoenix, just after midnight)

Every vendor fact in both Tool check callouts was re-read on 2026-10-22 and the callouts now carry that date. Pages and the lines used:

* Microsoft, "Microsoft Copilot for individuals: your activity history" (support.microsoft.com/en-us/privacy/microsoft-copilot/activity-history, browser): "An updated version of the Microsoft Copilot app for web, desktop, and mobile devices is available as of August 18, 2026. If you haven't updated to or downloaded the new version of the Microsoft Copilot app, this article does not apply to you." and "Prompts, responses, and your file contents when using the Microsoft Copilot app aren't used to train foundation models." No retention period on this page.
* Microsoft, "Microsoft Copilot for individuals: your privacy controls and choices" (.../microsoft-copilot/privacy-controls): "If you use Microsoft Copilot and don't have a Microsoft 365 subscription, you might see advertising in Copilot." (the source for the free consumer use line). No retention period on this page.
* Microsoft, "Microsoft Copilot for individuals: your data, privacy, and responsible AI" (.../microsoft-copilot/overview): same August 18, 2026 applicability note; points to the two pages above. No training or retention line of its own.
* Microsoft, "Copilot in Microsoft 365 apps for home: your data and privacy" (.../privacy/copilot-in-microsoft-365-apps-for-home-your-data-and-privacy): applies to "a Microsoft 365 Personal, Family, Premium, or Pro plan"; "Prompts, responses, and your file contents when using Copilot in Microsoft 365 apps aren't used to train foundation models." No retention period.
* Microsoft, "Privacy FAQ for Microsoft Copilot" (curl text): "The information in this article applies only to the older version of the Microsoft Copilot app." Its training line ("Except for certain categories of users or users who have opted out ...") and its 18-month storage line therefore apply only to the pre-August 18, 2026 app. The 18-month line was not found on any of the four new pages, so the callout marks retention for the new app unverified. Review B1.
* Microsoft 365 Copilot pricing (curl text): "Originally starting from $21.00 now starting from $18.00 ... user/month, paid yearly"; "Copilot Chat is a web-grounded AI assistant included at no additional cost with eligible Microsoft 365 plans." Microsoft Copilot for individuals sales page: "Microsoft 365 Premium $19.99 /month".
* Google, "Manage & delete your activity in Gemini Apps" (support.google.com/gemini/answer/13278892, browser): "If you're 18 or over, Keep Activity is on by default." Review M1.
* Google, Gemini Apps Privacy Hub (answer/13594961, browser, last updated October 19, 2026): "Temporary chats and chats you have when Keep Activity is off are retained with your account for 72 hours"; the training and 18-month lines as before.
* Google, Gemini subscriptions page (curl text, United States): Free $0, Google AI Plus $4.99, Google AI Pro $19.99, Gemini Enterprise Business from $21 per seat per month (unchanged).
* Google, notebook.google/plans (browser; notebooklm.google/plans 301s here): heading "Gemini Notebook Plans"; plans "Gemini Notebook" (for personal projects, standard limits), "Gemini Notebook in Google AI Plus", "... in Google AI Pro", "... in Google AI Ultra"; "When you use Gemini Notebook as an individual, your data is not used for training unless you share feedback"; FAQ: "NotebookLM is now Gemini Notebook as of July 2026." Review M2. The page states no price of its own; the Google AI plan prices are on the Gemini subscriptions page.
* Perplexity, "Perplexity Pro" page (perplexity.ai/pro, browser, after declining optional cookies): Pro "$17 /month when billed annually"; Max "$167 /month when billed annually"; "Login or sign up for free". Monthly-billing prices not shown on the default view and not used. Review M2.
* Perplexity, "Data Collection at Perplexity" (intercom.help/perplexity-ai/en/articles/11564572, written March 3, 2026, browser): "For Free, Perplexity Pro and Perplexity Max users, AI Data Retention is enabled by default"; steps: Account settings, Preferences, the AI data retention toggle; "Perplexity Enterprise data is never used for AI training purposes."
* Anthropic, "Updates to Consumer Terms and Privacy Policy" (anthropic.com/news/updates-to-our-consumer-terms, published August 28, 2025, browser): "If you're a new user, you can select your preference in the signup process"; "We are also extending data retention to five years, if you allow us to use your data for model training"; "If you do not choose to provide your data for model training, you'll continue with our existing 30-day data retention period"; "These updates apply to users on our Claude Free, Pro, and Max plans ... They do not apply to services under our Commercial Terms". Review m1.
* Anthropic, Consumer Terms of Service (anthropic.com/legal/consumer-terms, effective Oct 8, 2025): "You must be at least 18 years old or the minimum age required to consent to use the Services in your location, whichever is higher." Review m2.
* Anthropic pricing and the Privacy Center training article (March 16, 2026): unchanged ("$20 if billed monthly"; "You choose to allow ..."; no default stated).
* OpenAI, "What is ChatGPT Plus?" and "Data controls in ChatGPT" (browser): the quoted lines are unchanged ("Price: $20/month"; "may use conversations to improve model performance and safety"; "Improve the model for everyone"; the Business, Enterprise, Edu default).
* WCAG 2.2 SC 2.1.1 is now quoted only up to "keyboard interface" and the prose says the criterion then lists exceptions (review m7).
