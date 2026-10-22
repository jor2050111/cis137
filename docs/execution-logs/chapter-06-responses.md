# Chapter 6 captured responses

**Tool:** Claude (Anthropic), Sonnet, run through the Claude Code CLI
in print mode with no tools and a plain-assistant system prompt
(`tools/capture_sample.sh` for one turn, `tools/capture_conversation.sh`
for one conversation of several turns). This is a command-line harness,
not a consumer chat app. Prompt 14 is the one exception: it ran the
same harness, flags, and system prompt with a second model (Claude
Haiku), through the chapter's helper `cap-06.sh haiku`, to stand in for
"Tool B" in Section 6.3. Both models come from one vendor, so plan a
re-capture of Prompts 12 and 14 from two core-roster tools before
publication.
**Captured:** 2026-10-21 by the chapter 6 writer session.
**Rule:** every sample response in `book/chapters/chapter-06.md` is
copied from this log, trimmed only with `[...]` in the chapter, never
edited. A later pass may re-capture any prompt from a core-roster tool
(ChatGPT, Gemini, Copilot) and replace the sample, logging the new
tool and date here.

Prompts are numbered in the order they were sent. Every capture is
logged, including the ones the chapter does not show. Refinement
sequences: the landscaping versions (Prompts 1-3) and the league text
versions (Prompts 4-7) were each sent as fresh conversations, because
each version should start clean and a prompt card must work on its
own. The cybersecurity club sequence (Prompt 8) was sent as one
conversation with `tools/capture_conversation.sh`, because Section 6.2
teaches follow-ups in one conversation, and Prompts 9 and 10 then ran
the folded prompt fresh. A one-word smoke test of the capture tool
("Reply with the single word: ready") ran before Prompt 1. It is not a
chapter capture and is not shown anywhere.

Word counts below come from `wc -w` on the saved response. Email
bodies are counted from the greeting line through the last line before
the sign-off.

## Prompt 1 (Section 6.1 worked example: the landscaping email, version 1 (fresh conversation))

```text
You are the office manager at a small landscaping company in Mesa, Arizona. Write an email to our residential clients about the switch to our winter watering schedule. Facts: On November 1, we switch every client's irrigation timer to the winter schedule. Your crew will make the change at your regular monthly visit, so you do not need to do anything. Plants that went in during the last 60 days stay on the summer schedule until your crew lead checks them. Questions go to the office at 480-555-0163. Keep it friendly.
```

Response:

```text
**Subject:** Your winter watering schedule starts November 1

Hi there,

Cooler mornings are on the way, and your lawn and plants need less water than they did this summer. On November 1, we switch every client's irrigation timer to our winter schedule.

**You don't need to do anything.** Your crew will make the change at your regular monthly visit.

One exception: any plants that went in during the last 60 days stay on the summer schedule until your crew lead checks them. Young plants are still building roots, so they get a little extra care before they move to the winter schedule.

If you have questions, call the office at 480-555-0163. We're happy to help.

Thanks for letting us care for your yard.

Warmly,
[Your name]
Office Manager
[Company name]
480-555-0163
```

Observation: Body (from "Hi there," through "Thanks for letting us care for your yard.") is 115 words by wc -w, so it passes the under-120 criterion. Two sentences add reasons the prompt never gave: "Cooler mornings are on the way, and your lawn and plants need less water than they did this summer." and "Young plants are still building roots, so they get a little extra care before they move to the winter schedule." The sign-off holds two placeholders, "[Your name]" and "[Company name]". The 60-day exception survived. Score against the chapter's five criteria: 3 of 5 (fails 2, nothing added, and 4, ready to send). The phone number is a fictional 555 number.

## Prompt 2 (Section 6.2 worked example: the landscaping email, version 2, one change (the sign-off line), fresh conversation)

```text
You are the office manager at a small landscaping company in Mesa, Arizona. Write an email to our residential clients about the switch to our winter watering schedule. Facts: On November 1, we switch every client's irrigation timer to the winter schedule. Your crew will make the change at your regular monthly visit, so you do not need to do anything. Plants that went in during the last 60 days stay on the summer schedule until your crew lead checks them. Questions go to the office at 480-555-0163. Keep it friendly. Sign it "The Office Team" and leave no blanks or placeholders to fill in.
```

Response:

```text
**Subject:** Your winter watering schedule starts November 1

Hello,

As the weather cools, your landscape needs less water. On November 1, we switch every client's irrigation timer to our winter schedule. This keeps your plants healthy and your water bill lower through the cooler months.

You do not need to do anything. Your crew will make the change at your regular monthly visit.

One exception applies. Plants that went in during the last 60 days stay on the summer schedule until your crew lead checks them. New plants have shallow roots and still need the extra water, so we want to see them in person before we cut back.

Have a question about your timer or your plants? Call the office at 480-555-0163. We are happy to help.

Thank you for trusting us with your yard.

Warmly,
The Office Team
```

Observation: The one change worked on its target: the sign-off reads "The Office Team" and no placeholder remains. The body ("Hello," through "Thank you for trusting us with your yard.") is 128 words by wc -w, so the length criterion now fails. More reasons were added than in version 1: "This keeps your plants healthy and your water bill lower through the cooler months." and "New plants have shallow roots and still need the extra water, so we want to see them in person before we cut back." Score: 3 of 5 (fails 1, length, and 2, nothing added). Same total as version 1, different failures.

## Prompt 3 (Section 6.2 worked example, flagship 1: the landscaping email, version 3, one change (the constraint line), fresh conversation)

```text
You are the office manager at a small landscaping company in Mesa, Arizona. Write an email to our residential clients about the switch to our winter watering schedule. Facts: On November 1, we switch every client's irrigation timer to the winter schedule. Your crew will make the change at your regular monthly visit, so you do not need to do anything. Plants that went in during the last 60 days stay on the summer schedule until your crew lead checks them. Questions go to the office at 480-555-0163. Keep it friendly. Sign it "The Office Team" and leave no blanks or placeholders to fill in. Use only the facts above, and do not add reasons, benefits, or watering advice of your own.
```

Response:

```text
**Subject:** Winter watering schedule starts November 1

Hello,

On November 1, we switch every client's irrigation timer to our winter watering schedule.

You do not need to do anything. Your crew will make the change at your regular monthly visit.

One exception: plants that went in during the last 60 days stay on the summer schedule until your crew lead checks them.

Questions? Call the office at 480-555-0163. We're always happy to help.

Thank you for being part of our community of clients.

Warm regards,
The Office Team
```

Observation: Body ("Hello," through "Thank you for being part of our community of clients.") is 76 words by wc -w. Every fact traces to the prompt. The only lines not in the fact list are courtesy lines ("We're always happy to help." and "Thank you for being part of our community of clients."), which state no fact about the service. No placeholders. The 60-day exception survived. Score: 5 of 5. The chapter step labels were added to the chapter copy only, at sentence boundaries. The prompt was sent without them.

## Prompt 4 (Fix It 6.1 background: the league text, version 1 (fresh conversation; described in the chapter, not shown))

```text
Write a text message to the parents in our youth soccer league. Facts: Because of the heat forecast, every Saturday game this weekend starts at 7 a.m. instead of 9 a.m. Fields and opponents stay the same. Each player should bring two full water bottles. If the forecast drops below 100 degrees by Friday at 6 p.m., we will switch back to 9 a.m. and text you again.
```

Response:

```text
Heads up, soccer families: because of the heat forecast, every Saturday game this weekend starts at 7 a.m. instead of 9 a.m. Fields and opponents stay the same.

Please send each player with two full water bottles.

If the forecast drops below 100 degrees by Friday at 6 p.m., we will switch back to 9 a.m. and text you again. Until you hear from us, plan on 7 a.m.

See you Saturday!
```

Observation: 72 words by wc -w against an under-50 criterion. All four facts are present, including the switch-back rule. It adds "Until you hear from us, plan on 7 a.m." and "See you Saturday!", plus the greeting "Heads up, soccer families:". Score against the three league criteria (under 50 words, all four facts, the switch-back rule present): 2 of 3 (fails length).

## Prompt 5 (Fix It 6.1 symptom: the league text, version 2, which changed two things at once (a 45-word limit and "No greeting and no sign-off"), fresh conversation)

```text
Write a text message to the parents in our youth soccer league. Keep it under 45 words. Facts: Because of the heat forecast, every Saturday game this weekend starts at 7 a.m. instead of 9 a.m. Fields and opponents stay the same. Each player should bring two full water bottles. If the forecast drops below 100 degrees by Friday at 6 p.m., we will switch back to 9 a.m. and text you again. No greeting and no sign-off.
```

Response:

```text
Heat alert: This Saturday's games all start at 7 a.m., not 9 a.m. Fields and opponents are unchanged. Please send each player with two full water bottles. If Friday's 6 p.m. forecast falls below 100 degrees, we'll return to 9 a.m. and text you.
```

Observation: 44 words by wc -w. All four facts and the switch-back rule are present. No greeting and no sign-off. Score: 3 of 3. The log row cannot say which of the two added lines produced the cut.

## Prompt 6 (Fix It 6.1 repair: version 2a, which is version 1 plus only "No greeting and no sign-off" (one change), fresh conversation)

```text
Write a text message to the parents in our youth soccer league. Facts: Because of the heat forecast, every Saturday game this weekend starts at 7 a.m. instead of 9 a.m. Fields and opponents stay the same. Each player should bring two full water bottles. If the forecast drops below 100 degrees by Friday at 6 p.m., we will switch back to 9 a.m. and text you again. No greeting and no sign-off.
```

Response:

```text
Heat forecast: all Saturday games this weekend move from 9 a.m. to 7 a.m. Fields and opponents stay the same. Please send each player with two full water bottles.

If the forecast drops below 100 degrees by Friday at 6 p.m., we'll switch back to 9 a.m. and text you again.
```

Observation: 51 words by wc -w, one over the under-50 criterion. All four facts and the switch-back rule are present. No greeting and no sign-off. So the no-greeting line alone cut 72 words to 51 but did not meet the limit.

## Prompt 7 (Fix It 6.1 verify: version 2a re-run, identical prompt, fresh conversation)

```text
Write a text message to the parents in our youth soccer league. Facts: Because of the heat forecast, every Saturday game this weekend starts at 7 a.m. instead of 9 a.m. Fields and opponents stay the same. Each player should bring two full water bottles. If the forecast drops below 100 degrees by Friday at 6 p.m., we will switch back to 9 a.m. and text you again. No greeting and no sign-off.
```

Response:

```text
Due to the heat forecast, all Saturday games this weekend start at 7 a.m. instead of 9 a.m. Fields and opponents stay the same. Please send each player with two full water bottles. If the forecast drops below 100 degrees by Friday at 6 p.m., we'll switch back to 9 a.m. and text you again.
```

Observation: 55 words by wc -w. All four facts present, no greeting or sign-off. Two runs of version 2a gave 51 and 55 words, both over 50. Version 2 (Prompt 5) is version 2a plus the 45-word limit sentence at the same position, so its prompt text is identical to "version 2a plus the limit." The chapter logs it that way.

## Prompt 8 (Section 6.2 worked example: follow-ups in one conversation, three turns, `tools/capture_conversation.sh`)

One conversation, session id `c6f03e08-a749-4292-b6ab-93173c5e3eee`, resumed for turns 2 and 3 so the model saw the earlier turns.

Turn 1:

```text
Write a 100-word post inviting students to the first meeting of our community college's cybersecurity club. Facts: Thursday, September 10, at 3:30 p.m. in Room B-114. No experience needed. At the first meeting, teams will try to crack a practice password list on club laptops.
```

Response 1:

```text
Join the Cybersecurity Club!

Curious how attackers break into accounts? Come find out, and learn how to stop them.

Our first meeting is Thursday, September 10, at 3:30 p.m. in Room B-114. You don't need any experience. If you can show up, you can take part.

Here is what we'll do. Teams will try to crack a practice password list on club laptops. You'll see how weak passwords fall fast and why strong ones hold up.

Bring a friend, bring your curiosity, and bring your questions. We'll supply the laptops and the challenge.

Hope to see you there!
```

Turn 2:

```text
Shorter: under 60 words. And take out anything I did not give you.
```

Response 2:

```text
Join the Cybersecurity Club!

Our first meeting is Thursday, September 10, at 3:30 p.m. in Room B-114. No experience needed. Teams will try to crack a practice password list on club laptops.

Come see how it works.

(Word count: 38)
```

Turn 3:

```text
Good. Now make it sound more casual, for a social media post.
```

Response 3:

```text
Cybersecurity Club kicks off Thursday, Sept. 10, at 3:30 p.m. in Room B-114! 🔐

No experience needed. Teams will try to crack a practice password list on club laptops.

Come hang out and give it a shot.
```

Observation: Turn 1 ran 98 words by wc -w with its title line (94 without it) and added lines the facts never gave ("Curious how attackers break into accounts?", "You'll see how weak passwords fall fast and why strong ones hold up.", "We'll supply the laptops and the challenge."). Turn 2 (narrow plus correct) cut the additions and reported "(Word count: 38)". wc -w gives 37 for the post above that line, so the tool's count is off by one. Turn 3 (restyle) kept turn 2's facts, added an emoji and the line "Come hang out and give it a shot." The turn 3 post depends on turns 1 and 2: the words "make it sound more casual" alone do not say what to keep. Thursday, September 10, 2026 checked as a Thursday (Python datetime).

## Prompt 9 (Section 6.2 worked example: the folded prompt (the three turns combined into one prompt), fresh conversation)

```text
Write a casual social media post, under 60 words, inviting students to the first meeting of our community college's cybersecurity club. Facts: Thursday, September 10, at 3:30 p.m. in Room B-114. No experience needed. At the first meeting, teams will try to crack a practice password list on club laptops. Use only these facts.
```

Response:

```text
Cybersecurity Club kicks off Thursday, Sept. 10 at 3:30 p.m. in Room B-114! 🔐

No experience needed. We'll split into teams and try to crack a practice password list on club laptops.

Come curious, bring a friend, and see how fast weak passwords fall.

#CybersecurityClub
```

Observation: 45 words by wc -w (the hashtag counts as one). All four facts present. It adds "Come curious, bring a friend, and see how fast weak passwords fall." and "#CybersecurityClub", plus the emoji, even with "Use only these facts." in the prompt. The conversation's turn 2 could cut additions it could see. The folded prompt has to prevent them.

## Prompt 10 (Try It Yourself 6.3 (completion): the folded prompt with the gap filled by "Do not add hashtags, emoji, or any line that is not one of the facts.", fresh conversation)

```text
Write a casual social media post, under 60 words, inviting students to the first meeting of our community college's cybersecurity club. Facts: Thursday, September 10, at 3:30 p.m. in Room B-114. No experience needed. At the first meeting, teams will try to crack a practice password list on club laptops. Use only these facts. Do not add hashtags, emoji, or any line that is not one of the facts.
```

Response:

```text
Cybersecurity club's first meeting is Thursday, September 10, at 3:30 p.m. in Room B-114. No experience needed. Teams will try to crack a practice password list on club laptops. Come join us!
```

Observation: 32 words by wc -w. No hashtag and no emoji. All four facts present. It still adds one line that is not a fact: "Come join us!" The post also reads less casual than Prompt 9's. Score against the TIY's three criteria (under 60 words, all four facts, nothing added): 2 of 3.

## Prompt 11 (prompt-library-v2-starter.md, card 1 (Password reset reply): the card's last run with its example input, fresh conversation. The card's bracket labels were not sent.)

```text
You are a Deskside support technician at a managed IT services company, writing to an employee at one of our client companies. Write a reply to the ticket below that tells the person what happens next with their password reset. Our process: we verify identity by calling the person back at the phone number we have on file, and then we send a temporary password that must be changed at the first sign-in. Ticket: "Hi, I got locked out after too many tries this morning and I have a client call at 2. Can you reset it?" Keep the reply under 120 words, in plain text, with a greeting, two or three short numbered steps, and a sign-off from "Deskside Support." Never ask for the current password or any sign-in code. Do not promise a time. Use only the process above.
```

Response:

```text
Hi there,

Thanks for reaching out. We can get you back in. Here is what happens next:

1. We call you back at the phone number we have on file to verify your identity. Please keep that phone nearby.
2. Once you're verified, we send you a temporary password.
3. Sign in with the temporary password. You will be asked to choose a new one right away.

We will never ask for your current password or any sign-in code, so please don't share those with anyone.

Deskside Support
```

Observation: 88 words by wc -w (whole reply). States the call-back step first, asks for no password or code, promises no time, signs "Deskside Support". It adds one line the process did not give: "Please keep that phone nearby." and a warning not to share passwords with anyone. Passes the card's three Good output criteria.

## Prompt 12 (prompt-library-v2-starter.md, card 2 (VPN connection failure reply): the card's last run, and Section 6.3 Tool A. Fresh conversation. The card's bracket labels were not sent.)

```text
You are a Deskside support technician at a managed IT services company. The reader is an office worker at a client company, not a technical person. Write a reply to the ticket below that walks them through our first checks for a VPN connection failure. Use only these checks, in this order: 1. Open any website to confirm the internet works without the VPN. 2. Quit the VPN app completely, open it again, and sign in. 3. If it still fails, reply to this email with the exact words of the error message. Ticket: "The VPN won't connect from home. It just spins and then says something failed. I need the shared drive today." Format: under 100 words, plain text, a one-line greeting, the three checks as numbered steps, and a sign-off from "Deskside Support." Do not add any other troubleshooting steps, and do not promise when it will be fixed.
```

Response:

```text
Hi,

Let's start with three quick checks.

1. Open any website, such as a news site. This confirms your home internet works without the VPN.
2. Quit the VPN app completely, open it again, and sign in.
3. If it still fails, reply to this email with the exact words of the error message.

Those exact words help us see what went wrong.

Deskside Support
```

Observation: 65 words by wc -w. The three checks appear in order as numbered steps. It adds an example website ("such as a news site") and a closing reason line ("Those exact words help us see what went wrong."). No other troubleshooting step and no promised time. Passes the card's criteria. The greeting is "Hi," on its own line.

## Prompt 13 (prompt-library-v2-starter.md, card 3 (Shared mailbox access reply): the card's last run, fresh conversation. The card's bracket labels were not sent.)

```text
You are a Deskside support technician at a managed IT services company. A client employee has asked for access to a shared mailbox. Our rule: we add someone to a shared mailbox only after their manager approves it in writing. Before you draft anything, check the ticket for two facts: the name of the mailbox, and whether a manager has approved. If either fact is missing, write a short reply that asks only for what is missing. If both are there, write a reply under 80 words that says we will add them once we confirm the approval with their manager. Here is an example of a good reply that asks for what is missing: "Thanks for your request. Which shared mailbox do you need, for example billing@ or frontdesk@? Also, please ask your manager to reply to this email to approve the access." Ticket: "Can I get into the shared inbox? I'm covering for a coworker next week." Sign off as "Deskside Support." Do not promise a time.
```

Response:

```text
Thanks for your request. Which shared mailbox do you need, for example billing@ or frontdesk@? Also, please ask your manager to reply to this email to approve the access.

Deskside Support
```

Observation: The reply copies the prompt's example reply word for word and adds the sign-off. That fits this ticket, which is missing both facts. It is also the known risk of an example-led prompt, and the card's Notes say so.

## Prompt 14 (Section 6.3 Tool B: the Prompt 12 prompt, identical, run with a second model (Claude Haiku) through the same harness and system prompt (`cap-06.sh 14 ... haiku`), fresh conversation)

```text
You are a Deskside support technician at a managed IT services company. The reader is an office worker at a client company, not a technical person. Write a reply to the ticket below that walks them through our first checks for a VPN connection failure. Use only these checks, in this order: 1. Open any website to confirm the internet works without the VPN. 2. Quit the VPN app completely, open it again, and sign in. 3. If it still fails, reply to this email with the exact words of the error message. Ticket: "The VPN won't connect from home. It just spins and then says something failed. I need the shared drive today." Format: under 100 words, plain text, a one-line greeting, the three checks as numbered steps, and a sign-off from "Deskside Support." Do not add any other troubleshooting steps, and do not promise when it will be fixed.
```

Response:

```text
Hi there,

Thanks for reaching out. Let's start with three quick checks.

1. Open any website, such as a search page, in your browser. This confirms your internet works without the VPN.
2. Quit the VPN app completely, then open it again and sign in.
3. If it still fails, reply to this email with the exact words of the error message.

Deskside Support
```

Observation: 64 words by wc -w. Same three checks in order. It adds an example website ("such as a search page") and "in your browser", and opens "Thanks for reaching out." It has no closing reason line. Passes the card's criteria. Tool A and Tool B differ only in small added phrases. Both models are from one vendor (see the header).

## Prompt 15 (Section 6.4 worked example, flagship 2: the cold-read test on card 3, fresh conversation)

```text
A new Deskside technician will use the prompt card below with no one to ask. List every question they would need answered before they could run the prompt and judge the result. Only list questions the card does not already answer, and do not rewrite the card. One line per question, most important first, no more than six.

Card:
Name: Shared mailbox access reply
Job: Reply to a client employee who asks for access to a shared mailbox, asking for whatever the ticket is missing.
Prompt: [Role] You are a Deskside support technician at a managed IT services company. [Context] A client employee has asked for access to a shared mailbox. Our rule: we add someone to a shared mailbox only after their manager approves it in writing. [Task] Before you draft anything, check the ticket for two facts: the name of the mailbox, and whether a manager has approved. If either fact is missing, write a short reply that asks only for what is missing. If both are there, write a reply under 80 words that says we will add them once we confirm the approval with their manager. [Format] Here is an example of a good reply that asks for what is missing: "Thanks for your request. Which shared mailbox do you need, for example billing@ or frontdesk@? Also, please ask your manager to reply to this email to approve the access." Ticket: {ticket text} Sign off as "Deskside Support." [Constraints] Do not promise a time.
Example input: "Can I get into the shared inbox? I'm covering for a coworker next week."
Good output looks like: asks only for the missing facts; promises no time; signed "Deskside Support."
Strategies used: clarifying questions first; examples (few-shot); negative constraints and guardrails.
Last run: a chat assistant, October 2026.
Notes: (blank)
```

Response:

```text
1. What does the ticket normally contain? The card never says whether `{ticket text}` is the requester's message alone or includes metadata (requester name, client, manager name), so the tech can't tell what to paste.
2. Which chat assistant should I use, and does it need any setup (account, data settings, a fresh chat)? The card only says "a chat assistant."
3. How do I recognize "a manager has approved" in the ticket text? It's unclear whether the requester saying "my manager said OK" counts, or only a forwarded or quoted written approval.
4. What if the ticket gives a mailbox name but it looks wrong or doesn't exist for that client? The prompt checks only that a name is present, and the tech has no list of valid mailboxes.
5. What if the ticket names a manager but the approval is not from that manager (a coworker, or an unclear sender)? The prompt says to confirm with "their manager" but not who that is or how to reach them.
6. What do I do with the reply after the model writes it (edit, send, log, update ticket status), and who else needs to know? The card ends at "good output" and gives no next step.
```

Observation: Six questions, as limited. Questions 1, 3, 4, and 5 are about the card (what goes in the ticket slot, what counts as approval, a wrong mailbox name, approval from the wrong person). Questions 2 and 6 belong in the library README (which tool and setup, what to do with the reply). The card text in the prompt matches card 3 in `prompt-library-v2-starter.md` as drafted at capture time, with "Notes: (blank)" and a shortened Last run line. The chapter step labels were added to the chapter copy only, at sentence boundaries. The prompt was sent without them.

## Prompt 16 (Skills Lab 6A feasibility check: a plausible student version 1 from priya-newsletter-brief-2.txt, fresh conversation. Not used in the chapter or the packet.)

```text
You write for a community newsletter from an IT services company. Write a 120 to 160 word item, with a short headline, about two-step sign-in for email accounts: you sign in with your password, and then you type a short code from your phone. The readers are neighbors and small-business owners, many over 60, and some read English as a second language, so use plain words and short sentences. Invite them to the next free Tech Help Tuesday: Tuesday, December 15, 2026, from 10 a.m. to noon, in the community room at the neighborhood library branch. Bring the phone you use every day. Include this sentence word for word: "No one from Copperwind will ever ask you for your password or for a sign-in code."
```

Response:

```text
**Add a Second Lock to Your Email**

Your email holds a lot. It has bank notices, bills, and family photos. A password alone is not always enough to keep it safe.

Two-step sign-in adds a second lock. First, you type your password. Then your email asks for a short code. The code comes to your phone. You type it in, and you are in.

Why does this help? A thief may steal your password. But a thief does not have your phone. Without the code, the thief stays out.

Setting it up takes about ten minutes. We can help you do it.

No one from Copperwind will ever ask you for your password or for a sign-in code.

**Join us at Tech Help Tuesday.** It is free.

* Date: Tuesday, December 15, 2026
* Time: 10 a.m. to noon
* Place: Community room, neighborhood library branch

Bring the phone you use every day. We will set up two-step sign-in together, one step at a time. No question is too small.
```

Observation: 170 words by wc -w including the headline, and 163 without the headline, over the 120 to 160 limit. The backup-code caveat is missing. It adds a number that is not in the brief ("Setting it up takes about ten minutes."), which breaks Priya's no-numbers rule. Priya's promise sentence appears word for word. The bullet list has three items. So a plain version 1 fails at least two criteria a student would write from the brief, and the lab's loop has real work to do.

## Verification notes

* Further Reading URLs, `curl -sI -o /dev/null -w "%{http_code}"` on 2026-10-21: https://arxiv.org/abs/2310.11324 200, https://arxiv.org/abs/2404.12272 200, https://arxiv.org/abs/2406.06608 200, https://arxiv.org/abs/2303.17651 200. Titles, first authors, and dates read from each abstract page's citation meta tags the same day: Sclar, Choi, Tsvetkov and others, 2023-10-17, "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design" (abstract: up to 76 accuracy points of difference from formatting changes in few-shot settings, and format performance "only weakly correlates between models"). Shankar, Zamfirescu-Pereira, Hartmann and others, 2024-04-18, "Who Validates the Validators?" (abstract: "criteria drift: users need criteria to grade outputs, but grading outputs helps users define criteria"). Schulhoff, Ilie, Balepur and others, 2024-06-06, "The Prompt Report" (abstract: a taxonomy of 58 LLM prompting techniques and 33 vocabulary terms). Madaan, Tandon, Gupta and others, 2023-03-30, "Self-Refine" (abstract: the same model drafts, gives feedback on its draft, and revises, across 7 tasks, with about 20 percent absolute average improvement). The arXiv export API returned "Rate exceeded" once and was not used.
* Dates: Thursday, September 10, 2026 and Tuesday, December 15, 2026 checked with Python datetime. November 1, 2026 is a Sunday, and the chapter names no weekday for it.
* Phone numbers in prompts and packet files use the fictional 555-01xx range.
* Word counts: `wc -w` on the saved responses, as reported in each observation.
