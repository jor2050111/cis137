# Chapter 6 captured responses

> **Provenance note (2026-10-21).** Every response in this log was captured on
> the clean harness fixed at 19:28 on 2026-10-21 (an empty working
> directory, no settings, no instruction files). The earlier captures,
> which ran with the textbook's own writing rules in context, were
> replaced under Mr. Vega's ruling of 2026-10-21. They remain in git
> history before commit c7f4c84. Entries kept from the pre-fix harness,
> none of them shown anywhere: Prompt 15 (the first cold-read capture,
> on a draft of card 3, replaced in the chapter by Prompt 18 before the
> fix).

**Tool:** Claude (Anthropic), Sonnet, run through the Claude Code CLI in
print mode with no tools, a plain-assistant system prompt, no settings
or instruction files loaded, from a clean working directory, as a fresh
conversation per prompt (`tools/capture_sample.sh`;
`tools/capture_conversation.sh` for one conversation of several turns).
This is a command-line harness, not a consumer chat app. Prompt 14 is
"Tool B" in Section 6.3: the same harness, flags, and system prompt
with a second model, Claude Haiku (`CAPTURE_MODEL=haiku`, through the
helper `cap-06r.sh 14 ... haiku`). Both models come from one vendor, so
Prompts 12 and 14 are re-captured from two core-roster tools before
publication (the roster re-capture waits for publication, per Mr.
Vega's ruling of 2026-10-21).
**Captured:** 2026-10-21 by the chapter 06 re-capture session.
**Probe:** before the batch, the prompt "Do you have any rule about em
dashes, semicolons, or banned words in your instructions? Answer yes or
no, then quote any such rule." returned: "No. My instructions don't contain any rule about em dashes, semicolons, or banned words, so there is nothing to quote."
**Rule:** every sample response in `book/chapters/chapter-06.md` and in
`assets/code/chapter-06/prompt-library-v2-starter.md` is copied from
this log, trimmed only with `[...]`, never edited. A later pass may
re-capture any prompt from a core-roster tool (ChatGPT, Gemini,
Copilot) and replace the sample, logging the new tool and date here.

Prompts are numbered in the order they were first sent. Every capture
is logged, including the ones the chapter does not show. Refinement
sequences: the landscaping versions (Prompts 1-3, 17) and the league
text versions (Prompts 4-7, 19-21) were each sent as fresh
conversations, because each version should start clean and a prompt
card must work on its own. The cybersecurity club sequence (Prompt 8)
was sent as one conversation with `tools/capture_conversation.sh`,
because Section 6.2 teaches follow-ups in one conversation, and
Prompts 9 and 10 then ran the folded prompt fresh. Prompts 19-22 are
new in the re-capture: two re-runs of the league version 2, a new
one-change version 3, and the cold read on the corrected card 3. The harness CLI knows today's date, which
surfaced once (Prompt 8, turn 1).

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

Hello,

As the weather cools down here in the Valley, your lawn and plants need less water, so on **November 1** we're switching every client's irrigation timer to our winter watering schedule.

**You don't need to do anything.** Your crew will make the change during your regular monthly visit.

One small exception: any plants that went in during the last 60 days will stay on the summer schedule until your crew lead has a chance to check them. Newer plants are still getting established, and we want to make sure they're getting just the right amount of water before we cut back.

If you have any questions, give our office a call at **480-555-0163**. We're always happy to help.

Thank you for letting us take care of your yard. Enjoy the cooler weather!

Warm regards,

[Your Name]
Office Manager
[Company Name]
Mesa, Arizona
```

Observation: Body (from "Hello," through "Enjoy the cooler weather!") is 133 words by wc -w, so it fails the under-120 criterion. Two sentences add reasons the prompt never gave: "As the weather cools down here in the Valley, your lawn and plants need less water, so on **November 1** we're switching..." and "Newer plants are still getting established, and we want to make sure they're getting just the right amount of water before we cut back." The sign-off holds two placeholders, "[Your Name]" and "[Company Name]", and adds "Mesa, Arizona". The date and phone number are bolded with Markdown asterisks. The 60-day exception survived. Score against the chapter's five criteria: 2 of 5 (fails 1, length, 2, nothing added, and 4, ready to send). The phone number is a fictional 555 number.

## Prompt 2 (Section 6.2 worked example: the landscaping email, version 2, one change (the sign-off line), fresh conversation)

```text
You are the office manager at a small landscaping company in Mesa, Arizona. Write an email to our residential clients about the switch to our winter watering schedule. Facts: On November 1, we switch every client's irrigation timer to the winter schedule. Your crew will make the change at your regular monthly visit, so you do not need to do anything. Plants that went in during the last 60 days stay on the summer schedule until your crew lead checks them. Questions go to the office at 480-555-0163. Keep it friendly. Sign it "The Office Team" and leave no blanks or placeholders to fill in.
```

Response:

```text
**Subject:** Your Winter Watering Schedule Starts November 1

Hello,

As the weather cools down here in Mesa, it's time to adjust how much water your landscape needs. On November 1, we're switching every client's irrigation timer to our winter watering schedule.

You don't need to do anything. Your crew will make the change at your regular monthly visit.

One exception: any plants that went in during the last 60 days will stay on the summer schedule until your crew lead has a chance to check them. Newer plants are still getting established and often need extra water, so we want to make sure they're ready before we scale back.

If you have any questions, please call our office at 480-555-0163. We're always happy to help.

Thank you for letting us care for your landscape. Enjoy the cooler days ahead!

Warmly,
The Office Team
```

Observation: The one change worked on its target: the sign-off reads "The Office Team" and no placeholder remains. The body ("Hello," through "Enjoy the cooler days ahead!") is 131 words by wc -w, so the length criterion still fails (version 1 was 133). The added reasons are still there: "it's time to adjust how much water your landscape needs" and "Newer plants are still getting established and often need extra water, so we want to make sure they're ready before we scale back." Score: 3 of 5 (fails 1, length, and 2, nothing added). Criterion 4 moved, the two other failures did not.

## Prompt 3 (Section 6.2 worked example, flagship 1: the landscaping email, version 3, one change (the constraint line), fresh conversation)

```text
You are the office manager at a small landscaping company in Mesa, Arizona. Write an email to our residential clients about the switch to our winter watering schedule. Facts: On November 1, we switch every client's irrigation timer to the winter schedule. Your crew will make the change at your regular monthly visit, so you do not need to do anything. Plants that went in during the last 60 days stay on the summer schedule until your crew lead checks them. Questions go to the office at 480-555-0163. Keep it friendly. Sign it "The Office Team" and leave no blanks or placeholders to fill in. Use only the facts above, and do not add reasons, benefits, or watering advice of your own.
```

Response:

```text
**Subject:** Your Winter Watering Schedule Starts November 1

Hello,

We hope you're enjoying the season! We're writing to let you know that on November 1, we're switching every client's irrigation timer to our winter watering schedule.

You don't need to do anything. Our crew will make the change at your regular monthly visit.

One note: any plants that went in during the last 60 days will stay on the summer schedule until your crew lead has had a chance to check them.

If you have any questions, please call the office at 480-555-0163. We're always happy to help.

Thank you for being a valued client!

Warm regards,
The Office Team
```

Observation: Body ("Hello," through "Thank you for being a valued client!") is 97 words by wc -w, down from 131 with no word limit in the prompt. Every fact traces to the prompt ("Our crew" for the facts' "Your crew" keeps the meaning). The lines not in the fact list are courtesy lines ("We hope you're enjoying the season!", "We're always happy to help.", and "Thank you for being a valued client!"), which make no claim about the service, and criterion 2 allows them. No placeholders. The 60-day exception survived ("One note:"). Score: 5 of 5. The chapter step labels were added to the chapter copy only, at sentence boundaries. The prompt was sent without them.

## Prompt 4 (Fix It 6.1 background: the league text, version 1 (fresh conversation; described in the chapter, not shown))

```text
Write a text message to the parents in our youth soccer league. Facts: Because of the heat forecast, every Saturday game this weekend starts at 7 a.m. instead of 9 a.m. Fields and opponents stay the same. Each player should bring two full water bottles. If the forecast drops below 100 degrees by Friday at 6 p.m., we will switch back to 9 a.m. and text you again.
```

Response:

```text
Heads up, soccer families: because of the heat forecast, all Saturday games this weekend are moving from 9 a.m. to 7 a.m. Fields and opponents are the same. Please send your player with two full water bottles.

If the forecast drops below 100 degrees by Friday at 6 p.m., we'll switch back to 9 a.m. and text you again. Otherwise, see you at 7!
```

Observation: 64 words by wc -w against an under-50 criterion. All four facts are present, including the switch-back rule. It adds the greeting "Heads up, soccer families:" and the closer "Otherwise, see you at 7!". Score against the three league criteria (under 50 words, all four facts, the switch-back rule present): 2 of 3 (fails length).

## Prompt 5 (Fix It 6.1 symptom: the league text, version 2, which changed two things at once (a 45-word limit and "No greeting and no sign-off"), fresh conversation)

```text
Write a text message to the parents in our youth soccer league. Keep it under 45 words. Facts: Because of the heat forecast, every Saturday game this weekend starts at 7 a.m. instead of 9 a.m. Fields and opponents stay the same. Each player should bring two full water bottles. If the forecast drops below 100 degrees by Friday at 6 p.m., we will switch back to 9 a.m. and text you again. No greeting and no sign-off.
```

Response:

```text
Due to the heat forecast, all Saturday games this weekend start at 7 a.m. instead of 9 a.m. Fields and opponents are unchanged. Please send each player with two full water bottles. If the forecast drops below 100 degrees by Friday 6 p.m., we'll return to 9 a.m. and text you.
```

Observation: 51 words by wc -w, so it still fails the under-50 criterion (under 50 means 49 at most) and misses its own 45-word limit by 6. All four facts and the switch-back rule are present. No greeting and no sign-off. Score: 2 of 3 (fails length). The version cut 13 words from version 1, and the log row cannot say which of the two added lines made the cut. Re-runs: Prompts 19 and 20.

## Prompt 6 (Fix It 6.1 repair: version 2a, which is version 1 plus only "No greeting and no sign-off" (one change), fresh conversation)

```text
Write a text message to the parents in our youth soccer league. Facts: Because of the heat forecast, every Saturday game this weekend starts at 7 a.m. instead of 9 a.m. Fields and opponents stay the same. Each player should bring two full water bottles. If the forecast drops below 100 degrees by Friday at 6 p.m., we will switch back to 9 a.m. and text you again. No greeting and no sign-off.
```

Response:

```text
Because of the heat forecast, all Saturday games this weekend will start at 7 a.m. instead of 9 a.m. Fields and opponents are unchanged. Please make sure each player brings two full water bottles. If the forecast drops below 100 degrees by Friday at 6 p.m., we'll switch back to the 9 a.m. start and text you again.
```

Observation: 58 words by wc -w, over the under-50 criterion. All four facts and the switch-back rule are present. No greeting and no sign-off. So the no-greeting line alone cut 64 words to 58.

## Prompt 7 (Fix It 6.1 verify: version 2a re-run, identical prompt, fresh conversation)

```text
Write a text message to the parents in our youth soccer league. Facts: Because of the heat forecast, every Saturday game this weekend starts at 7 a.m. instead of 9 a.m. Fields and opponents stay the same. Each player should bring two full water bottles. If the forecast drops below 100 degrees by Friday at 6 p.m., we will switch back to 9 a.m. and text you again. No greeting and no sign-off.
```

Response:

```text
Because of the heat forecast, all Saturday games this weekend will start at 7 a.m. instead of 9 a.m. Fields and opponents are unchanged. Please make sure each player brings two full water bottles. If the forecast drops below 100 degrees by Friday at 6 p.m., we'll switch back to the 9 a.m. start and text you again.
```

Observation: 58 words by wc -w, and word for word the same text as Prompt 6. Two runs of version 2a gave 58 and 58, both over 50. Version 2 (Prompt 5) is version 2a plus the 45-word limit sentence at the same position, so its prompt text is identical to "version 2a plus the limit." The chapter logs it that way, as version 2b (runs: 51, 50, 51).

## Prompt 8 (Section 6.2 worked example: follow-ups in one conversation, three turns, `tools/capture_conversation.sh`)

One conversation, session id `b473f9cb-355b-4b10-8c41-1fb61b8cecbe`, resumed for turns 2 and 3 so the model saw the earlier turns.

Turn 1:

```text
Write a 100-word post inviting students to the first meeting of our community college's cybersecurity club. Facts: Thursday, September 10, at 3:30 p.m. in Room B-114. No experience needed. At the first meeting, teams will try to crack a practice password list on club laptops.
```

Response 1:

```text
Curious about cybersecurity? Join our community college's Cybersecurity Club for our first meeting on Thursday, September 10, at 3:30 p.m. in Room B-114! No experience is needed, so whether you're a total beginner or already love tech, you're welcome here. We'll kick things off with a hands-on challenge: working in teams, you'll try to crack a practice password list using club laptops. It's a fun, friendly way to learn how attackers think and how to defend against them. Meet new people, build real skills, and see what the club is all about. Bring a friend, and we'll see you there!

Quick note: September 10 has already passed this year (it's October 21, 2026). If you're posting now, double-check the date.
```

Turn 2:

```text
Shorter: under 60 words. And take out anything I did not give you.
```

Response 2:

```text
Join our community college's Cybersecurity Club for our first meeting! It's Thursday, September 10, at 3:30 p.m. in Room B-114. No experience needed. At the first meeting, teams will try to crack a practice password list on club laptops. We hope to see you there!
```

Turn 3:

```text
Good. Now make it sound more casual, for a social media post.
```

Response 3:

```text
Ever wanted to crack some passwords? 🔐 The cybersecurity club's first meeting is Thursday, Sept. 10, at 3:30 p.m. in Room B-114. No experience needed! Teams will take on a practice password list on club laptops. Come hang out and give it a shot!
```

Observation: Turn 1 ran 100 words by wc -w for the post itself, plus a one-line "Quick note" warning that "September 10 has already passed this year (it's October 21, 2026)", which comes from the harness knowing the date. The post added lines the facts never gave ("It's a fun, friendly way to learn how attackers think and how to defend against them.", "Meet new people, build real skills, and see what the club is all about."). Turn 2 (narrow plus correct) cut the additions and ran 45 words, but kept one closing line the officer never gave, "We hope to see you there!" Turn 3 (restyle) ran 44 words, kept turn 2's facts, and added a question opener ("Ever wanted to crack some passwords?"), an emoji, and "Come hang out and give it a shot!" The turn 3 post depends on turns 1 and 2: the words "make it sound more casual" alone do not say what to keep. Thursday, September 10, 2026 checked as a Thursday (Python datetime).

## Prompt 9 (Section 6.2 worked example: the folded prompt (the three turns combined into one prompt), fresh conversation)

```text
Write a casual social media post, under 60 words, inviting students to the first meeting of our community college's cybersecurity club. Facts: Thursday, September 10, at 3:30 p.m. in Room B-114. No experience needed. At the first meeting, teams will try to crack a practice password list on club laptops. Use only these facts.
```

Response:

```text
Cybersecurity club kicks off this Thursday, Sept. 10, at 3:30 p.m. in Room B-114! 🔐

No experience needed. We'll split into teams and try to crack a practice password list on club laptops. Come hang out, learn something new, and see how fast you can break in.

Hope to see you there!
```

Observation: 52 words by wc -w. All four facts present. It adds "Come hang out, learn something new, and see how fast you can break in." and "Hope to see you there!", plus the emoji, even with "Use only these facts." in the prompt. No hashtag on this run. The conversation's turn 2 could cut additions it could see. The folded prompt has to prevent them.

## Prompt 10 (Try It Yourself 6.3 (completion): the folded prompt with the gap filled by "Do not add hashtags, emoji, or any line that is not one of the facts.", fresh conversation)

```text
Write a casual social media post, under 60 words, inviting students to the first meeting of our community college's cybersecurity club. Facts: Thursday, September 10, at 3:30 p.m. in Room B-114. No experience needed. At the first meeting, teams will try to crack a practice password list on club laptops. Use only these facts. Do not add hashtags, emoji, or any line that is not one of the facts.
```

Response:

```text
Cybersecurity club's first meeting is Thursday, September 10, at 3:30 p.m. in Room B-114. No experience needed! Teams will try to crack a practice password list on club laptops. Come hang out and give it a shot.
```

Observation: 37 words by wc -w. No emoji and no hashtag. All four facts present. Prompt 9's added claim ("see how fast you can break in") is gone. It adds "Come hang out and give it a shot.", an invitation, which the TIY criteria allow, though the gap sentence itself forbade "any line that is not one of the facts." With "No experience needed!" and that closer, the post still reads casual. Score against the TIY's four criteria (under 60 words, all four facts, no added claim with greetings and invitations allowed, casual tone): 4 of 4.

## Prompt 11 (prompt-library-v2-starter.md, card 1 (Password reset reply): the card's last run with its example input, fresh conversation. The card's bracket labels were not sent.)

```text
You are a Deskside support technician at a managed IT services company, writing to an employee at one of our client companies. Write a reply to the ticket below that tells the person what happens next with their password reset. Our process: we verify identity by calling the person back at the phone number we have on file, and then we send a temporary password that must be changed at the first sign-in. Ticket: "Hi, I got locked out after too many tries this morning and I have a client call at 2. Can you reset it?" Keep the reply under 120 words, in plain text, with a greeting, two or three short numbered steps, and a sign-off from "Deskside Support." Never ask for the current password or any sign-in code. Do not promise a time. Use only the process above.
```

Response:

```text
Hello,

Thanks for reaching out. I'm sorry about the lockout, and I can help get you back in.

1. We'll call you back at the phone number we have on file to verify your identity. Please keep your phone nearby and answer calls from us.
2. Once you're verified, we'll send you a temporary password.
3. When you sign in with it, you'll be prompted to choose a new password right away.

We won't ask you for your current password or any sign-in codes at any point.

Deskside Support
```

Observation: 89 words by wc -w (whole reply). States the call-back step first, asks for no password or code, promises no time, signs "Deskside Support". It adds lines the process did not give: "I'm sorry about the lockout, and I can help get you back in." and "Please keep your phone nearby and answer calls from us." Passes the card's three Good output criteria.

## Prompt 12 (prompt-library-v2-starter.md, card 2 (VPN connection failure reply): the card's last run, and Section 6.3 Tool A. Fresh conversation. The card's bracket labels were not sent.)

```text
You are a Deskside support technician at a managed IT services company. The reader is an office worker at a client company, not a technical person. Write a reply to the ticket below that walks them through our first checks for a VPN connection failure. Use only these checks, in this order: 1. Open any website to confirm the internet works without the VPN. 2. Quit the VPN app completely, open it again, and sign in. 3. If it still fails, reply to this email with the exact words of the error message. Ticket: "The VPN won't connect from home. It just spins and then says something failed. I need the shared drive today." Format: under 100 words, plain text, a one-line greeting, the three checks as numbered steps, and a sign-off from "Deskside Support." Do not add any other troubleshooting steps, and do not promise when it will be fixed.
```

Response:

```text
Hi, sorry the VPN is giving you trouble. Let's try these in order:

1. Open any website, such as a news site, to confirm your home internet is working without the VPN.
2. Quit the VPN app completely, open it again, and sign in.
3. If it still fails, reply to this email with the exact words of the error message.

Thanks,
Deskside Support
```

Observation: 64 words by wc -w. The three checks appear in order as numbered steps. The greeting line adds an apology ("Hi, sorry the VPN is giving you trouble."), check 1 adds an example website ("such as a news site"), and "Thanks," sits before the sign-off. No other troubleshooting step and no promised time. Passes the card's criteria.

## Prompt 13 (prompt-library-v2-starter.md, card 3 (Shared mailbox access reply): the card's last run, fresh conversation. The card's bracket labels were not sent.)

```text
You are a Deskside support technician at a managed IT services company. A client employee has asked for access to a shared mailbox. Our rule: we add someone to a shared mailbox only after their manager approves it in writing. Before you draft anything, check the ticket for two facts: the name of the mailbox, and whether a manager has approved. If either fact is missing, write a short reply that asks only for what is missing. If both are there, write a reply under 80 words that says we will add them once we confirm the approval with their manager. Here is an example of a good reply that asks for what is missing: "Thanks for your request. Which shared mailbox do you need, for example billing@ or frontdesk@? Also, please ask your manager to reply to this email to approve the access." Ticket: "Can I get into the shared inbox? I'm covering for a coworker next week." Sign off as "Deskside Support." Do not promise a time.
```

Response:

```text
Thanks for your request. Which shared mailbox do you need, for example billing@ or frontdesk@? Also, please ask your manager to reply to this email to approve the access.

Deskside Support
```

Observation: 31 words by wc -w. The reply copies the prompt's example reply word for word and adds the sign-off, the same text as the pre-fix run. That fits this ticket, which is missing both facts. It is also the known risk of an example-led prompt, and the card's Notes say so.

## Prompt 14 (Section 6.3 Tool B: the Prompt 12 prompt, identical, run with a second model (Claude Haiku) through the same harness and system prompt (`cap-06r.sh 14 ... haiku`), fresh conversation)

```text
You are a Deskside support technician at a managed IT services company. The reader is an office worker at a client company, not a technical person. Write a reply to the ticket below that walks them through our first checks for a VPN connection failure. Use only these checks, in this order: 1. Open any website to confirm the internet works without the VPN. 2. Quit the VPN app completely, open it again, and sign in. 3. If it still fails, reply to this email with the exact words of the error message. Ticket: "The VPN won't connect from home. It just spins and then says something failed. I need the shared drive today." Format: under 100 words, plain text, a one-line greeting, the three checks as numbered steps, and a sign-off from "Deskside Support." Do not add any other troubleshooting steps, and do not promise when it will be fixed.
```

Response:

```text
Hi there,

Thanks for reaching out about the VPN. Please try these checks in order:

1. Open any website, such as a news site, to confirm your internet connection works without the VPN.
2. Quit the VPN app completely, open it again, and sign in.
3. If it still fails, reply to this email with the exact words of the error message.

Regards,
Deskside Support
```

Observation: 65 words by wc -w. Same three checks in order. It opens "Hi there," and "Thanks for reaching out about the VPN.", adds the same example website as Tool A ("such as a news site"), and closes "Regards,". Passes the card's criteria. Tool A and Tool B differ only in the opener and closer lines. Both models are from one vendor (see the header).

## Prompt 15 (pre-fix harness capture, not used anywhere: Section 6.4 worked example, flagship 2: the cold-read test on card 3, fresh conversation)

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

Observation: Six questions, as limited. Questions 1, 3, 4, and 5 are about the card (what goes in the ticket slot, what counts as approval, a wrong mailbox name, approval from the wrong person). Questions 2 and 6 belong in the library README (which tool and setup, what to do with the reply). The card text in the prompt matches card 3 in `prompt-library-v2-starter.md` as drafted at capture time, with "Notes: (blank)" and a shortened Last run line. The chapter step labels were added to the chapter copy only, at sentence boundaries. The prompt was sent without them. After the 2026-10-21 review this capture was replaced in the chapter by Prompt 18, which used the card exactly as it ships. This one stays in the log.

## Prompt 16 (Skills Lab 6A feasibility check: a plausible student version 1 from priya-newsletter-brief-2.txt, fresh conversation. Not used in the chapter or the packet.)

```text
You write for a community newsletter from an IT services company. Write a 120 to 160 word item, with a short headline, about two-step sign-in for email accounts: you sign in with your password, and then you type a short code from your phone. The readers are neighbors and small-business owners, many over 60, and some read English as a second language, so use plain words and short sentences. Invite them to the next free Tech Help Tuesday: Tuesday, December 15, 2026, from 10 a.m. to noon, in the community room at the neighborhood library branch. Bring the phone you use every day. Include this sentence word for word: "No one from Copperwind will ever ask you for your password or for a sign-in code."
```

Response:

```text
**Two Steps Keep Your Email Safer**

A password alone is not always enough. Thieves can steal or guess passwords. That is why we suggest two-step sign-in.

Here is how it works. First, you sign in with your password. Then your email asks for a short code. The code comes to your phone. You type it in, and you are done.

A thief may know your password. But a thief does not have your phone. So your account stays safe.

It takes only a few extra seconds each time. Many people find it easy after the first few days.

No one from Copperwind will ever ask you for your password or for a sign-in code.

**Come to Tech Help Tuesday**

Want help turning this on? Join our next free Tech Help Tuesday.

- **Date:** Tuesday, December 15, 2026
- **Time:** 10 a.m. to noon
- **Place:** Community room, neighborhood library branch

Please bring the phone you use every day. We will help you, one step at a time. No question is too small.
```

Observation: 172 words by wc -w including both bold headlines, and 166 without the first headline, over the 120 to 160 limit. The backup-code caveat is missing. It adds claims that are not in the brief ("It takes only a few extra seconds each time. Many people find it easy after the first few days."), though no numeral or statistic. Priya's promise sentence appears word for word. The bullet list has three items, written with hyphen markers and bold labels. So a plain version 1 fails at least two criteria a student would write from the brief (length and the caveat), and the lab's loop has real work to do. Not used in the chapter or the packet.

## Prompt 17 (Section 6.2: re-run of landscaping version 3 (identical to Prompt 3), fresh conversation with tools/capture_sample.sh, for the good enough line's re-run)

```text
You are the office manager at a small landscaping company in Mesa, Arizona. Write an email to our residential clients about the switch to our winter watering schedule. Facts: On November 1, we switch every client's irrigation timer to the winter schedule. Your crew will make the change at your regular monthly visit, so you do not need to do anything. Plants that went in during the last 60 days stay on the summer schedule until your crew lead checks them. Questions go to the office at 480-555-0163. Keep it friendly. Sign it "The Office Team" and leave no blanks or placeholders to fill in. Use only the facts above, and do not add reasons, benefits, or watering advice of your own.
```

Response:

```text
**Subject: Your Irrigation Timer Is Switching to the Winter Schedule on November 1**

Hello,

We wanted to give you a quick heads-up: on November 1, we switch every client's irrigation timer to the winter watering schedule.

You don't need to do anything. Your crew will make the change at your regular monthly visit.

One note: any plants that went in during the last 60 days will stay on the summer schedule until your crew lead checks them.

If you have any questions, please call the office at 480-555-0163. We're always happy to help.

Thank you for being one of our clients!

Warm regards,
The Office Team
```

Observation: Body ("Hello," through "Thank you for being one of our clients!") is 88 words by wc -w. Every fact matches the list, the 60-day exception survived, no placeholders. The lines not in the fact list are courtesy ("We wanted to give you a quick heads-up:", "We're always happy to help.", and "Thank you for being one of our clients!"), allowed by criterion 2. The subject line is bold Markdown. Score: 5 of 5, so version 3 meets the good enough line in a fresh run and a re-run.

## Prompt 18 (superseded by Prompt 22, clean capture not shown: the cold-read test re-captured with card 3 pasted exactly as it ships in prompt-library-v2-starter.md (fields as the shipped Markdown list, the Prompt field's indented text fence included, sample output excluded), fresh conversation)

````text
A new Deskside technician will use the prompt card below with no one to ask. List every question they would need answered before they could run the prompt and judge the result. Only list questions the card does not already answer, and do not rewrite the card. One line per question, most important first, no more than six.

Card:
* Name: Shared mailbox access reply
* Job (what this prompt is for): Reply to a client employee who asks for access to a shared mailbox, asking for whatever the ticket is missing.
* Prompt (full text, with [Role] [Task] [Context] [Format] [Constraints] labeled):

    ```text
    [Role] You are a Deskside support technician at a managed IT services company. [Context] A client employee has asked for access to a shared mailbox. Our rule: we add someone to a shared mailbox only after their manager approves it in writing. [Task] Before you draft anything, check the ticket for two facts: the name of the mailbox, and whether a manager has approved. If either fact is missing, write a short reply that asks only for what is missing. If both are there, write a reply under 80 words that says we will add them once we confirm the approval with their manager. [Format] Here is an example of a good reply that asks for what is missing: "Thanks for your request. Which shared mailbox do you need, for example billing@ or frontdesk@? Also, please ask your manager to reply to this email to approve the access." Ticket: {ticket text} Sign off as "Deskside Support." [Constraints] Do not promise a time.
    ```

* Example input: "Can I get into the shared inbox? I'm covering for a coworker next week."
* Good output looks like (two or three criteria):
    * asks only for the missing facts
    * promises no time
    * signed "Deskside Support."
* Strategies used (Chapter 5):
    * clarifying questions first
    * examples (few-shot)
    * negative constraints and guardrails
* Last run (tool, date): a chat assistant from the course roster, October 21, 2026 (Prompt 13 in the textbook author's capture log, not in the data pack)
* Notes (what to watch, what it gets wrong): The last run copied the example reply word for word. That fits a ticket that is missing both facts. When the ticket names a mailbox, check that the reply does not still ask which mailbox.
````

Response:

```text
1. Does a claim in the ticket like "my manager said it's fine" count as written approval, or must the approval come from the manager directly (for example, a reply or forward)?
2. What is the pass/fail standard for a result: should I expect the example reply word for word when both facts are missing, and what should a one-fact-missing reply look like?
3. Which tool and settings should I run it in (the last run used an unnamed "chat assistant from the course roster"), and do I paste the ticket over `{ticket text}` or add it below the card?
4. Are "billing@" and "frontdesk@" real mailboxes for this client, or only placeholders that could mislead the requester?
5. Should the reply greet the employee by name, and if the ticket has no name, what do I use?
6. Do I send the reply as written, or does someone review it first, and does it go by email or as a ticket note?
```

Observation: Six questions. Questions 1, 2, and 4 are card fixes (what counts as written approval, what a reply should look like when one fact is missing, whether the example mailboxes are real). Questions 3 and 6 are mostly README fixes (which tool and settings, whether someone reviews the reply and where it goes), though question 3 also asks where the ticket text goes. Question 5 (greet by name) is a reply convention for the README. Question 3 quotes the card's old Last run line ("a chat assistant from the course roster"), which was inaccurate: the run came from the author's test setup, not a roster product. The re-capture corrected the three Last run lines in the starter, so card 3 as shipped changed, and the cold read was run again on the shipped card as Prompt 22. This clean capture is not shown anywhere. The step labels were never sent.

## Prompt 19 (Fix It 6.1 symptom re-run: version 2 (identical to Prompt 5), fresh conversation)

```text
Write a text message to the parents in our youth soccer league. Keep it under 45 words. Facts: Because of the heat forecast, every Saturday game this weekend starts at 7 a.m. instead of 9 a.m. Fields and opponents stay the same. Each player should bring two full water bottles. If the forecast drops below 100 degrees by Friday at 6 p.m., we will switch back to 9 a.m. and text you again. No greeting and no sign-off.
```

Response:

```text
Because of the heat, all Saturday games this weekend start at 7 a.m. instead of 9. Fields and opponents are unchanged. Please send each player with two full water bottles. If the forecast drops below 100 degrees by Friday at 6 p.m., we'll return to 9 a.m. and text you.
```

Observation: 50 words by wc -w, so it fails under-50 by one. All four facts present ("instead of 9" drops the "a.m."). No greeting and no sign-off.

## Prompt 20 (Fix It 6.1 symptom re-run: version 2 (identical to Prompt 5), second re-run, fresh conversation)

```text
Write a text message to the parents in our youth soccer league. Keep it under 45 words. Facts: Because of the heat forecast, every Saturday game this weekend starts at 7 a.m. instead of 9 a.m. Fields and opponents stay the same. Each player should bring two full water bottles. If the forecast drops below 100 degrees by Friday at 6 p.m., we will switch back to 9 a.m. and text you again. No greeting and no sign-off.
```

Response:

```text
Because of the heat forecast, all Saturday games this weekend start at 7 a.m. instead of 9 a.m. Fields and opponents are unchanged. Please send two full water bottles with each player. If the forecast drops below 100 degrees by Friday 6 p.m., we'll return to 9 a.m. and text you.
```

Observation: 51 words by wc -w. All four facts present. No greeting and no sign-off. Three runs of version 2 (Prompts 5, 19, 20): 51, 50, 51, none under 50.

## Prompt 21 (Fix It 6.1 verify: version 3, which is version 2b with one change ("Keep it under 40 words." in place of "Keep it under 45 words."), fresh conversation)

```text
Write a text message to the parents in our youth soccer league. Keep it under 40 words. Facts: Because of the heat forecast, every Saturday game this weekend starts at 7 a.m. instead of 9 a.m. Fields and opponents stay the same. Each player should bring two full water bottles. If the forecast drops below 100 degrees by Friday at 6 p.m., we will switch back to 9 a.m. and text you again. No greeting and no sign-off.
```

Response:

```text
Because of the heat forecast, all Saturday games this weekend start at 7 a.m., not 9. Fields and opponents are unchanged. Please send two full water bottles with each player. If Friday's 6 p.m. forecast is under 100°, we'll return to 9 a.m. and text you.
```

Observation: 46 words by wc -w, under 50. All four facts and the switch-back rule present. No greeting and no sign-off. This is version 2b (Prompt 5's text) with one change, the limit sentence tightened from 45 to 40 words. Score: 3 of 3.

## Prompt 22 (Section 6.4 worked example, flagship 2: the cold-read test on card 3 exactly as it ships in the updated prompt-library-v2-starter.md (corrected Last run line, sample output excluded), fresh conversation)

````text
A new Deskside technician will use the prompt card below with no one to ask. List every question they would need answered before they could run the prompt and judge the result. Only list questions the card does not already answer, and do not rewrite the card. One line per question, most important first, no more than six.

Card:
* Name: Shared mailbox access reply
* Job (what this prompt is for): Reply to a client employee who asks for access to a shared mailbox, asking for whatever the ticket is missing.
* Prompt (full text, with [Role] [Task] [Context] [Format] [Constraints] labeled):

    ```text
    [Role] You are a Deskside support technician at a managed IT services company. [Context] A client employee has asked for access to a shared mailbox. Our rule: we add someone to a shared mailbox only after their manager approves it in writing. [Task] Before you draft anything, check the ticket for two facts: the name of the mailbox, and whether a manager has approved. If either fact is missing, write a short reply that asks only for what is missing. If both are there, write a reply under 80 words that says we will add them once we confirm the approval with their manager. [Format] Here is an example of a good reply that asks for what is missing: "Thanks for your request. Which shared mailbox do you need, for example billing@ or frontdesk@? Also, please ask your manager to reply to this email to approve the access." Ticket: {ticket text} Sign off as "Deskside Support." [Constraints] Do not promise a time.
    ```

* Example input: "Can I get into the shared inbox? I'm covering for a coworker next week."
* Good output looks like (two or three criteria):
    * asks only for the missing facts
    * promises no time
    * signed "Deskside Support."
* Strategies used (Chapter 5):
    * clarifying questions first
    * examples (few-shot)
    * negative constraints and guardrails
* Last run (tool, date): the textbook author's test setup (not a roster product), October 21, 2026 (Prompt 13 in the textbook author's capture log, not in the data pack)
* Notes (what to watch, what it gets wrong): The last run copied the example reply word for word. That fits a ticket that is missing both facts. When the ticket names a mailbox, check that the reply does not still ask which mailbox.
````

Response:

```text
1. What goes in the `{ticket text}` slot: the requester's message only, or also the ticket's subject, requester name, notes, and prior replies? (Approval or mailbox details may sit outside the message body.)
2. What counts as "approved in writing" for the check? A manager's reply on the ticket, a forwarded email, a chat message, or the requester just saying "my manager said OK"?
3. What should the reply say when the ticket names a mailbox and a manager approval, but the approval looks unverifiable or comes from someone who may not be the requester's manager?
4. When only one fact is missing, what exactly should the reply contain, since the example covers only the both-missing case? (Reminder to ask only for the missing fact, not repeat the other.)
5. Which AI tool and model should the technician run it in, and do they need a fresh chat each time? (The last run was in the author's own test setup, not a roster product.)
6. After running it, who sends the reply, and what must be checked first? (Edit the draft, confirm the mailbox exists, check the requester's identity and client, then send or log it in the ticket.)
```

Observation: Six questions. Questions 1-4 are card fixes (what goes in the ticket slot, what counts as written approval, what to do when an approval looks unverifiable or comes from the wrong person, what a reply should say when only one fact is missing). Questions 5 and 6 belong in the README (which tool and whether to use a fresh chat, who checks and sends the reply). Question 2 quotes the loophole "my manager said OK". The chapter shows 1, 2, 5, and 6 with a [...] cut, in a four-backtick text fence because the card holds a three-backtick fence. The step labels were added to the chapter copy only, at sentence boundaries. The prompt was sent without them.

## Verification notes

* Further Reading URLs, `curl -sI -o /dev/null -w "%{http_code}"` on 2026-10-21: https://arxiv.org/abs/2310.11324 200, https://arxiv.org/abs/2404.12272 200, https://arxiv.org/abs/2406.06608 200, https://arxiv.org/abs/2303.17651 200. Titles, first authors, and dates read from each abstract page's citation meta tags the same day: Sclar, Choi, Tsvetkov and others, 2023-10-17, "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design" (abstract: up to 76 accuracy points of difference from formatting changes in few-shot settings, and format performance "only weakly correlates between models"). Shankar, Zamfirescu-Pereira, Hartmann and others, 2024-04-18, "Who Validates the Validators?" (abstract: "criteria drift: users need criteria to grade outputs, but grading outputs helps users define criteria"). Schulhoff, Ilie, Balepur and others, 2024-06-06, "The Prompt Report" (abstract: a taxonomy of 58 LLM prompting techniques and 33 vocabulary terms). Madaan, Tandon, Gupta and others, 2023-03-30, "Self-Refine" (abstract: the same model drafts, gives feedback on its draft, and revises, across 7 tasks, with about 20 percent absolute average improvement). The arXiv export API returned "Rate exceeded" once and was not used.
* Dates: Thursday, September 10, 2026 and Tuesday, December 15, 2026 checked with Python datetime. November 1, 2026 is a Sunday, and the chapter names no weekday for it.
* Phone numbers in prompts and packet files use the fictional 555-01xx range.
* Word counts: `wc -w` on the saved responses, as reported in each observation, recomputed for every clean capture on 2026-10-21.
* Dates: the clean re-capture ran on 2026-10-21 (MST), so the starter cards' Last run lines keep "October 21, 2026".
