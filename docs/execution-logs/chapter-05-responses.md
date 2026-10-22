# Chapter 5 captured responses

**Tool:** Claude (Anthropic), Sonnet, run through the Claude Code CLI in
print mode with no tools and a plain-assistant system prompt, as a fresh
conversation per prompt (the provenance line in `tools/capture_sample.sh`).
**Captured:** 2026-10-21 by the chapter 5 build session.
**Rule:** every sample response in `book/chapters/chapter-05.md` and in
`assets/code/chapter-05/prompt-library-v1-starter.md` is copied from
this log, trimmed only with `[...]`, never edited. A later pass may
re-capture any prompt from a core-roster tool (ChatGPT, Gemini,
Copilot) and replace the sample, logging the new tool and date here.

Each prompt was sent as a fresh conversation with `tools/capture_sample.sh`, through the session helper `cap-05.sh`, which saves the exact prompt and response to files before they are pasted here. No prompt in this chapter uses `tools/capture_conversation.sh`. Fix It 5.1 took two attempts (Prompts 5 and 6). Prompt 15 is a discarded draft that changed two things at once, kept and labeled. Prompts 21-23 are author pre-checks of the Skills Lab 5A weak prompts and appear nowhere in the chapter or the packet.

## Verification notes

* Further Reading, checked 2026-10-21 with `curl -sI -o /dev/null -w "%{http_code}" -A "Mozilla/5.0" URL`: https://arxiv.org/abs/2005.14165 (200), https://arxiv.org/abs/2201.11903 (200), https://arxiv.org/abs/2205.11916 (200), https://arxiv.org/abs/2406.06608 (200), https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence (200).
* Titles, first authors, and dates read from each arXiv page's citation metadata: Brown et al., 2020-05-28, "Language Models are Few-Shot Learners". Wei et al., 2022-01-28, "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (abstract: chain of thought prompting "improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks"). Kojima et al., 2022-05-24, "Large Language Models are Zero-Shot Reasoners".  Schulhoff et al., 2024-06-06, "The Prompt Report: A Systematic Survey of Prompt Engineering Techniques" (abstract: "a taxonomy of 58 LLM prompting techniques, and 40 techniques for other modalities").
* The Section 5.2 figure: the Kojima et al. abstract says adding "Let's think step by step" increased "the accuracy on MultiArith from 17.7% to 78.7%" with one large model. The chapter says "one model's score on a set of math word problems", which is what MultiArith is, and does not name the model.
* NIST AI 600-1: the NIST page title reads "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile", published July 26, 2024. The PDF (https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf, downloaded 2026-10-21) lists twelve numbered risks. Risk 2 reads "Confabulation: The production of confidently stated but erroneous or false content (known colloquially as 'hallucinations' or 'fabrications')".
* Word counts in the chapter come from `wc -w` on the saved response files.
* All phone numbers in prompts use the fictional 555 exchange.

## Prompt 1 (Section 5.1 worked example: specificity, before (the vague landscaping prompt))

```text
Write a social media post for our landscaping company about our fall services.
```

Response:

```text
**Fall Services Post**

Fall is the best time to set your lawn up for spring. Here's what we're booking now:

* Leaf cleanup and removal
* Aeration and overseeding
* Fall fertilizer for strong roots
* Gutter and bed cleanout
* Pruning, trimming, and mulching
* Bulb planting for spring color

Cooler weather lets grass recover and roots grow deep. A few hours of work now means a greener yard in March.

Our fall schedule fills fast. Call [phone], visit [website], or message us to get a free quote.

#FallLawnCare #Landscaping #[YourCity] #LeafCleanup #LawnAeration

---

**Shorter version (for Instagram or X):**

Your lawn's best growing season starts in fall. We handle leaf cleanup, aeration, overseeding, fertilizing, and mulching so spring looks great. Book your free quote today: [phone] or [website].

---

I didn't have your company name, location, or any offers, so those are placeholders. If you tell me about a seasonal discount, your service area, or your brand voice (friendly, professional, funny), I can tailor the post.
```

Observation: The response lists six services (leaf cleanup, aeration and overseeding, fall fertilizer, gutter and bed cleanout, pruning and mulching, bulb planting) and a free quote, none of which the prompt supplied. It labels its own placeholders ([phone], [website]) and says it lacked the company name and location. The chapter trims the hashtags, the 'Cooler weather' paragraph, and the shorter version with [...]. Used again in TIY 5.4 and Quick Check 5.4 as the scored example.

## Prompt 2 (Section 5.1 worked example, flagship 1: specificity and context, after)

```text
I run a small landscaping company in Mesa, Arizona. The post is for our neighborhood social media page, which is read mostly by homeowners who already know us. Write a social media post of 60 to 80 words announcing our fall services. Facts: (1) fall overseeding with winter rye for Bermuda lawns, booking now for October 15 through November 15, (2) irrigation timer resets for cooler weather, (3) we are a two-person crew, so book early, (4) call or text 480-555-0186 to book. Do not add prices, discounts, or services that are not listed.
```

Response:

```text
Fall is the best time to give your lawn some attention. We're now booking fall overseeding with winter rye for Bermuda lawns, with work running October 15 through November 15. We'll also reset your irrigation timer for cooler weather.

We're a two-person crew, so book early to get the date you want. Call or text 480-555-0186 to reserve your spot.

(Word count: 64)
```

Observation: Every fact traces to the prompt. No prices, discounts, or new services. The tool reports 64 words. wc -w on the two body paragraphs gives 60 (63 for the whole response, minus the three tokens of the '(Word count: 64)' line). Both sit inside 60-80. The [Step] labels were added to the chapter copy only, at sentence boundaries. The prompt was sent without them.

## Prompt 3 (Section 5.1 worked example: examples (few-shot), before (no samples))

```text
Our public library branch sends short text-message reminders about events. Write the reminder for this event: a seed library swap, Thursday at 6 p.m. in the community room, free, and people should bring seeds in labeled envelopes.
```

Response:

```text
Seed Library Swap this Thursday at 6 p.m. in the Community Room. Free! Bring seeds in labeled envelopes to share and take home new ones. See you there!
```

Observation: 28 words (wc -w), two exclamation points, and an added clause ('to share and take home new ones') that the prompt did not supply.

## Prompt 4 (Section 5.1 worked example: examples (few-shot), after (two samples))

```text
Our public library branch sends short text-message reminders about events. Here are two we sent last month:

Tue 4pm | Teen Game Club | Room B | Free, no sign-up
Sat 10am | Toddler Story Time | Children's area | Free, no sign-up

Write the reminder for this event in the same style: a seed library swap, Thursday at 6 p.m. in the community room, free, and people should bring seeds in labeled envelopes.
```

Response:

```text
Thu 6pm | Seed Library Swap | Community room | Free, bring seeds in labeled envelopes
```

Observation: One line in the branch's bar-separated style: short day and time, title, place, ending. The added promise is gone.

## Prompt 5 (Fix It 5.1, attempt 1 (no failure))

```text
Pull the action items out of these meeting notes from our college robotics club.

Notes: We met October 14. Jaylen will reserve the lab for build nights by October 20. Priscilla and Tomas will draft the sponsor letter and send it to our advisor by October 24. Everyone agreed we need a new banner, and Mai will get two price quotes by the next meeting on October 28. We talked about the spring competition but did not decide anything. Dues stay at $10, and Jaylen will remind members in the group chat this week.
```

Response:

```text
| Owner | Action | Due |
|---|---|---|
| Jaylen | Reserve the lab for build nights | Oct 20 |
| Priscilla and Tomas | Draft the sponsor letter and send it to the advisor | Oct 24 |
| Mai | Get two price quotes for a new banner | Oct 28 (next meeting) |
| Jaylen | Remind members in the group chat that dues stay at $10 | "This week" (week of Oct 14) |

**Not action items:**
- Dues stay at $10. This is a decision, and the only task is the reminder above.
- The spring competition came up, but nothing was decided, so no one owns a task. You may want to put it on the Oct 28 agenda.

**Timing flag:** Today is Oct 21, so Jaylen's Oct 20 lab reservation deadline has already passed. The notes don't say whether it got done. His group chat reminder was also due the week of the meeting, so it may be done or overdue. A quick check with Jaylen would settle both.
```

Observation: Attempt 1 did not fail the way the lesson needs. With no Format part, the tool chose a table (Owner, Action, Due) on its own, plus notes and a timing flag. Not used in the chapter except as the one-sentence note in the Fix It Verify step that a first attempt came back as a table without being asked.

## Prompt 6 (Fix It 5.1 symptom, attempt 2 (the failure used))

```text
Let the members of our college robotics club know that Thursday's build night moved from 5 p.m. to 6:30 p.m. It is in the same room, and everyone should bring safety glasses.
```

Response:

```text
Here's a draft you can send as is:

**Subject:** Thursday build night moved to 6:30 p.m.

Hi everyone,

Thursday's build night now starts at **6:30 p.m.** instead of 5 p.m. We're meeting in the same room.

Please bring your safety glasses. You won't be able to work on the builds without them.

See you Thursday!

I haven't sent this to anyone. I don't have your member list, so you'll need to add the recipients. Since this is going to a group, put the addresses in Bcc to keep members' emails private. If you post it in Slack or Discord instead, the same text works. You could add the room name there for anyone who forgets.
```

Observation: The failure: every fact is right (6:30 p.m., same room, safety glasses), but the shape is an email: a wrapper line, a bold subject line, bold markup on the time, a greeting, and a closing note about Bcc and other chat apps. A group-text post needs all of that deleted. It also adds a rule the prompt did not state ('You won't be able to work on the builds without them'). The chapter trims the final paragraph (the Bcc note, which also names two vendor chat products) with [...] and says what the cut held.

## Prompt 7 (Fix It 5.1 repair (one change: a Format part added, the request kept word for word))

```text
Let the members of our college robotics club know that Thursday's build night moved from 5 p.m. to 6:30 p.m. It is in the same room, and everyone should bring safety glasses. Format: one plain-text message for our club's group text, under 30 words, with no subject line and no bold or other formatting. Reply with the message only.
```

Response:

```text
Heads up: Thursday's build night moved from 5 p.m. to 6:30 p.m. Same room. Please bring your safety glasses. See you there!
```

Observation: 22 words (wc -w), under 30. No subject line, no bold, no wrapper line. All three facts kept. 'See you there!' is a flourish. The added rule from Prompt 6 is gone. The prompt is Prompt 6 with one Format sentence and 'Reply with the message only.' appended. Both are the Format part.

## Prompt 8 (Section 5.2 worked example: step-by-step reasoning request (youth sports fields))

```text
Our youth sports league assigns practice fields. Rules: (1) Field 2 has no lights, so every practice there must end by 6:30 p.m. (2) Teams under age 8 practice for 45 minutes, and older teams practice for 75 minutes. (3) Two teams cannot use the same field at the same time.

Requests for Wednesday:
A. U10 Hawks, Field 2, starting 5:30 p.m.
B. U7 Comets, Field 1, starting 5:45 p.m.
C. U12 Rockets, Field 1, starting 6:30 p.m.

Which requests can we approve as written? Check each request against each rule, one rule at a time, and show each check on its own line. Then give the final answer.
```

Response:

```text
**Durations (Rule 2):**
- U10 Hawks: age 8 or older, so 75 minutes
- U7 Comets: under 8, so 45 minutes
- U12 Rockets: age 8 or older, so 75 minutes

**Request A: U10 Hawks, Field 2, 5:30 p.m. start (ends 6:45 p.m.)**
- Rule 1 (Field 2 ends by 6:30): Fails. 5:30 + 75 minutes = 6:45 p.m., which is 15 minutes past the cutoff.
- Rule 2 (duration): Applied correctly, 75 minutes for U10.
- Rule 3 (no overlap): Passes. No other team is on Field 2.

**Request B: U7 Comets, Field 1, 5:45 p.m. start (ends 6:30 p.m.)**
- Rule 1 (Field 2 lights): Not applicable. This is Field 1.
- Rule 2 (duration): Applied correctly, 45 minutes for U7.
- Rule 3 (no overlap): Passes. The Comets use Field 1 from 5:45 to 6:30, and the Rockets start at 6:30. Back-to-back is not an overlap.

**Request C: U12 Rockets, Field 1, 6:30 p.m. start (ends 7:45 p.m.)**
- Rule 1 (Field 2 lights): Not applicable. This is Field 1.
- Rule 2 (duration): Applied correctly, 75 minutes for U12.
- Rule 3 (no overlap): Passes. The Comets finish at 6:30, the moment the Rockets begin.

**Final answer:**
- Approve B (U7 Comets) and C (U12 Rockets) as written.
- Do not approve A (U10 Hawks) as written. It runs 15 minutes past the Field 2 cutoff. To fix it, start the Hawks by 5:15 p.m. on Field 2, or move them to Field 1 at a time that avoids the Comets (5:45 to 6:30) and the Rockets (6:30 to 7:45).
```

Observation: Verified by hand: A runs 5:30 to 6:45 on Field 2 and breaks rule 1. B runs 5:45 to 6:30 on Field 1. C runs 6:30 to 7:45 on Field 1, so B and C touch but do not overlap. Approve B and C, deny A. The response is correct, and its suggested fix (start the Hawks by 5:15 on Field 2) is correct. The chapter trims the durations block and the B and C checks with [...] and describes them.

## Prompt 9 (Section 5.3 worked example: clarifying questions first (coding club flyer))

```text
I am the president of a community college coding club. I need a half-page flyer to recruit new members. Before you write anything, ask me up to three questions whose answers would change the flyer the most. Ask them all at once, then stop and wait for my answers.
```

Response:

```text
Three questions, and each one changes the flyer a lot:

1. **What is the one thing you most want a new member to do after reading it?** For example, come to the first meeting on a specific date, time, and room, scan a QR code to join a Discord or sign-up form, or email an advisor. Please include the logistics (when, where, and how to reach you) so I can print them accurately.

2. **Who are you trying to reach, and what will they worry about?** Complete beginners who think they "can't code," students already in CS or IT classes looking for projects and a portfolio, or both? Tell me which, plus any fear you want to defuse (no experience needed, no cost, low time commitment).

3. **What does the club actually do that would make someone show up?** Examples: weekly build nights, hackathons, project teams, interview prep, guest speakers from local employers, transfer or internship help. Pick the top two or three. If you have a club name, a tagline, or a school color or logo requirement, add that too.

Once you answer, I'll write the half-page flyer.
```

Observation: Three questions, asked at once, and the tool stopped as told. Question 1 (what readers should do next, with the logistics) names a vendor chat product, so the chapter trims it with a leading [...] and describes it in prose.

## Prompt 10 (Section 5.3 worked example: persona and audience framing (dental hygienist))

```text
You are a dental hygienist who has spent ten years working with nervous patients. Explain to an adult patient what will happen at her first deep cleaning next week. She is anxious and has said she does not want medical jargon. Use only these facts: the visit takes about 90 minutes, the dentist numbs one side of the mouth at a time, she can raise her left hand at any point to pause, and her gums may feel tender for two or three days afterward. Write four to six short sentences, spoken directly to her.
```

Response:

```text
I know this is the part you've been dreading, so let me walk you through exactly what will happen. The visit will take about 90 minutes, and the dentist will numb one side of your mouth at a time, so you'll never have your whole mouth numb at once. You are in charge the whole way through: just raise your left hand at any point, and we will pause right away. No explanation needed. Afterward, your gums may feel tender for two or three days, which is normal. You've already done the hardest part by showing up, and I'll be right there with you.
```

Observation: Six sentences, inside the four-to-six range. All four facts present. Additions the prompt did not supply: 'so you'll never have your whole mouth numb at once' (an inference from the one-side fact), 'we will pause right away' and 'I'll be right there with you' (promises), and 'You've already done the hardest part by showing up' (reassurance). The chapter uses the two promises to motivate the guardrail strategy.

## Prompt 11 (Section 5.3 worked example: grounding, before (no source))

```text
A patient at our dental office had a tooth filled this morning. She texted the front desk to ask: "Can I drink coffee this afternoon?" Write a two-sentence reply from the front desk.
```

Response:

```text
Yes, you can drink coffee this afternoon, just wait until the numbness wears off so you don't accidentally burn your lip or cheek. If your tooth feels sensitive or your bite seems off, call us and we'll take a look.
```

Observation: The reply says yes and gives clinical advice (wait for the numbness, risk of burning the lip or cheek) that no office source supplied. The advice may be sensible, but it is not traceable to anything the office approved.

## Prompt 12 (Section 5.3 worked example: grounding, after (the after-care sheet))

```text
A patient at our dental office had a tooth filled this morning. She texted the front desk to ask: "Can I drink coffee this afternoon?" Write a two-sentence reply from the front desk. Answer only from the after-care sheet below. If the sheet does not answer her question, say so and ask her to call the office at 602-555-0117.

After-care sheet: Do not chew on the filled side until the numbness wears off, usually 2 to 3 hours. Mild sensitivity to cold for up to two weeks is normal. Call us if your bite feels uneven after the numbness is gone.
```

Response:

```text
Our after-care sheet doesn't say whether coffee is okay this afternoon, so please call us at 602-555-0117 and we'll help you. In the meantime, avoid chewing on the filled side until the numbness wears off (usually 2 to 3 hours).
```

Observation: The reply says the sheet does not cover coffee, gives the office number, and repeats one line from the sheet. Nothing added.

## Prompt 13 (Try It Yourself 5.3 compare block: the completion prompt with its three gaps filled by the author)

```text
You answer questions from patrons of a public library branch. Answer the question below using only the policy below. If the policy does not answer the question, say "The policy does not say" and suggest the patron ask at the front desk. Do not guess or add rules that are not in the policy.

Policy: Meeting rooms are free for nonprofit and community groups. Book up to 30 days ahead at the front desk or by phone. Each booking is for up to 3 hours. Rooms seat 24 people. Food is allowed, but no open flames.

Question: Can our book club reserve the room every Tuesday for the next three months?
```

Response:

```text
The policy does not say whether a group can set up a standing weekly reservation, so please ask at the front desk.

Here is what the policy does say:

- Bookings can be made up to 30 days ahead, so you could not reserve all three months of Tuesdays at once.
- Each booking is for up to 3 hours.
- Rooms are free for nonprofit and community groups, and they seat 24 people.
- You can book at the front desk or by phone.

The policy does not say whether your book club counts as a community group, so the front desk can confirm that too.
```

Observation: Gaps filled as: (1) 'the policy below', (2) 'The policy does not say', (3) 'guess or add rules that are not in the policy'. The chapter shows the prompt with the three gaps as ____ and shows this response as the compare block, trimmed with [...]. The response opens with the not-found sentence, correctly applies the 30-day rule, and flags a second gap (whether a book club counts as a community group). The response uses dash bullets, copied as returned.

## Prompt 14 (Section 5.4 worked example: the repair method, run 1 (the weak Deskside printer prompt))

```text
You are a Deskside support technician at Copperwind IT Services, a managed IT services company in Phoenix. Write a reply to the client ticket below. Keep it under 120 words and friendly.

Ticket: Our front office printer says "offline" again and nobody can print invoices. We already turned it off and on. Can someone help today? - Lorena, office manager
```

Response:

```text
Hi Lorena,

Thanks for the details. Sorry the printer is holding up invoices. Power cycling was the right first move, and "offline" usually means the printer lost its connection to the network or to the computers.

Two quick checks while we get to you:

1. Look at the printer's screen or menu for a Wi-Fi or network icon. Tell us if it shows disconnected.
2. On one computer, open Printers & Scanners and see if the printer is set to "Use Printer Offline." If so, uncheck it.

I can also connect remotely this afternoon and fix it directly. Reply with a good time and the printer's model, and we'll get you printing today.

Best,
Deskside Support, Copperwind IT Services
```

Observation: 119 words (wc -w), under 120. Additions: step 2 ('Printers & Scanners', 'Use Printer Offline') is not a Copperwind procedure, and 'I can also connect remotely this afternoon' and 'we'll get you printing today' are promises. The chapter trims the greeting and opening paragraph and the sign-off with [...].

## Prompt 15 (Section 5.4, discarded draft of the repair (two changes at once, not used))

```text
You are a Deskside support technician at Copperwind IT Services, a managed IT services company in Phoenix. Write a reply to the client ticket below. Keep it under 120 words and friendly.

Ticket: Our front office printer says "offline" again and nobody can print invoices. We already turned it off and on. Can someone help today? - Lorena, office manager

Use only the Deskside team's steps below. Do not add steps, times, or promises that are not in them.

Deskside steps for a printer that shows offline: (1) Check that the printer's network cable is plugged in, or that its screen shows a Wi-Fi connection. (2) On one office computer, open the printer list, remove the printer, and add it again. (3) If it still shows offline, reply to this ticket, and a technician will connect remotely during business hours.
```

Response:

```text
Hi Lorena,

Sorry the printer is acting up again. Here are two quick things to try:

1. Check that the printer's network cable is plugged in snugly, or that its screen shows a Wi-Fi connection.
2. On one office computer, open the printer list, remove the printer, and add it again.

If it still shows offline after that, just reply to this ticket. A technician will connect remotely during business hours to take a look.

Thanks,
Deskside Support
Copperwind IT Services
```

Observation: This run added grounding and a guardrail sentence in one change. It passed all five Output Checklist checks, but it changed two things at once, so it could not show which change did the work. It was replaced by Prompts 16 and 17, one change each. Not used in the chapter. Kept here, labeled, under the log rule that every attempt stays in the log.

## Prompt 16 (Section 5.4 worked example, flagship 2: the repair method, run 2 (one change: grounding))

```text
You are a Deskside support technician at Copperwind IT Services, a managed IT services company in Phoenix. Write a reply to the client ticket below. Keep it under 120 words and friendly.

Ticket: Our front office printer says "offline" again and nobody can print invoices. We already turned it off and on. Can someone help today? - Lorena, office manager

Answer only from the Deskside team's steps below.

Deskside steps for a printer that shows offline: (1) Check that the printer's network cable is plugged in, or that its screen shows a Wi-Fi connection. (2) On one office computer, open the printer list, remove the printer, and add it again. (3) If it still shows offline, reply to this ticket, and a technician will connect remotely during business hours.
```

Response:

```text
Hi Lorena,

Sorry about the printer trouble. Let's get invoices printing again today. Since the power cycle didn't clear it, try these two checks:

1. Look at the printer. Make sure its network cable is plugged in, or that its screen shows a Wi-Fi connection.
2. On one office computer, open the printer list, remove the printer, and add it again.

If it still shows offline after that, just reply to this ticket. A technician will connect remotely during business hours and take it from there.

Thanks,
Deskside Team
Copperwind IT Services
```

Observation: 92 words (wc -w). The two steps now match the Deskside steps, and the remote session says 'during business hours', as the source does. One promise survives: 'Let's get invoices printing again today.' The prompt is Prompt 14 plus the grounding sentence and the steps block. The [Step] labels were added to the chapter copy only, at sentence boundaries. The prompt was sent without them.

## Prompt 17 (Section 5.4 worked example: the repair method, run 3 (one change: a guardrail sentence))

```text
You are a Deskside support technician at Copperwind IT Services, a managed IT services company in Phoenix. Write a reply to the client ticket below. Keep it under 120 words and friendly.

Ticket: Our front office printer says "offline" again and nobody can print invoices. We already turned it off and on. Can someone help today? - Lorena, office manager

Answer only from the Deskside team's steps below. Do not promise a time, and do not add steps that are not in them.

Deskside steps for a printer that shows offline: (1) Check that the printer's network cable is plugged in, or that its screen shows a Wi-Fi connection. (2) On one office computer, open the printer list, remove the printer, and add it again. (3) If it still shows offline, reply to this ticket, and a technician will connect remotely during business hours.
```

Response:

```text
Hi Lorena,

Sorry about the offline printer. Let's get invoices moving again. Please try these steps:

1. Check that the printer's network cable is plugged in, or that its screen shows a Wi-Fi connection.
2. On one office computer, open the printer list, remove the printer, and add it again.

If it still shows offline after that, reply to this ticket. A technician will then connect remotely during business hours to take a look.

Thanks,
Deskside Team, Copperwind IT Services
```

Observation: 80 words (wc -w). The prompt is Prompt 16 with one sentence added after the grounding line ('Do not promise a time, and do not add steps that are not in them.'), verified with diff. 'today' is gone. 'Let's get invoices moving again' is a flourish, not a time. The chapter shows only the added sentence as the prompt for this run and trims the middle of the response with [...].

## Prompt 18 (Packet: prompt-library-v1-starter.md, Card 1 (password reset reply), sample output)

```text
[Role] You are a Deskside support technician at Copperwind IT Services, a managed IT services company in Phoenix.
[Task] Write a reply to the client ticket below about a password reset.
[Context] Copperwind resets a client's password only after the person calls the Deskside line at 602-555-0149 and confirms who they are. Ticket: I'm locked out of my email after too many tries. Can you reset my password and send me the new one? - Marcus, front desk at a client law office
[Format] A short email reply, under 100 words, with a greeting and a sign-off from the Deskside team.
[Constraints] Never ask for a password or include one in the reply.
```

Response:

```text
Subject: Re: Locked out of email

Hi Marcus,

Sorry about the lockout. We can get you back in quickly.

For your security, we reset passwords only after we confirm who is asking. Please call our Deskside line at 602-555-0149. A technician will verify your identity and walk you through the reset on the call.

We never send passwords by email, and we will never ask you to send us yours.

Talk soon,

The Deskside team
Copperwind IT Services
```

Observation: 78 words (wc -w) including a subject line the Format part did not ask for. It routes the reset to the Deskside phone line, never asks for a password, and adds 'we will never ask you to send us yours', which matches the card's Constraint. The card's Notes record the subject line.

## Prompt 19 (Packet: prompt-library-v1-starter.md, Card 2 (VPN connection failure first reply), sample output)

```text
[Role] You are a Deskside support technician at Copperwind IT Services, a managed IT services company in Phoenix.
[Task] Write a first reply to the client ticket below about a VPN connection that will not connect.
[Context] Most VPN failures at our clients come from an expired password, a home Wi-Fi network that blocks the VPN, or a VPN app that needs an update. Ticket: The VPN won't connect from home since this morning. It just spins and then says connection failed. I'm working from home today. - Keisha, bookkeeper at a client firm
[Format] A friendly reply under 150 words with up to three numbered checks the client can try, then one line asking what the error message says.
[Constraints] Do not tell the client to change any settings on their home router.
```

Response:

```text
Hi Keisha,

Thanks for reaching out. Let's get you connected so you can finish your day.

Please try these in order:

1. **Check your password.** Sign in to your email or another work site. If it asks you to reset your password, an expired password is the most likely cause. Update it, then try the VPN again.
2. **Switch networks.** Some home Wi-Fi networks block VPN traffic. Connect your phone's hotspot to your computer and try again.
3. **Update the VPN app.** Open the app's menu or settings, look for "Check for updates," install any update, and restart the app.

If none of those work, what exact words does the error message show? A screenshot is even better.

Thanks,
Deskside Support, Copperwind IT Services
```

Observation: 124 words (wc -w), under 150. Three numbered checks that match the three causes in the Context part, then the error-message question. Suggesting a phone hotspot does not change router settings, so the Constraint holds. It adds bold step titles and asks for a screenshot. The card's Notes record both.

## Prompt 20 (Packet: prompt-library-v1-starter.md, Card 3 (new-hire device setup checklist), sample output)

```text
[Role] You are a Deskside support technician at Copperwind IT Services, a managed IT services company in Phoenix.
[Task] Turn the new-hire request below into a setup checklist for the technician who will prepare the laptop.
[Context] Request: New hire starts Monday, November 2: Jordan Reyes, part-time receptionist. Needs a laptop, an email account, access to the shared front-desk mailbox, and the scheduling software. Jordan will use the existing desk phone. - Office manager at a client property management office
[Format] A numbered checklist, one action per line, grouped under Accounts, Software, and Hardware.
[Constraints] Include only items the request asks for or clearly implies.
```

Response:

```text
**New-Hire Setup Checklist: Jordan Reyes (Part-Time Receptionist)**
Start date: Monday, November 2

**Accounts**
1. Create Jordan's email account.
2. Grant Jordan access to the shared front-desk mailbox.
3. Create Jordan's scheduling software account.
4. Set the account permissions for a part-time receptionist.

**Software**
5. Install the scheduling software on the laptop.
6. Add Jordan's email account to the mail client on the laptop.
7. Add the shared front-desk mailbox to the mail client.
8. Sign in to the scheduling software and confirm it loads.

**Hardware**
9. Prepare the laptop with the current OS updates and the client's standard image.
10. Create Jordan's user profile on the laptop.
11. Test sending and receiving from both Jordan's mailbox and the shared front-desk mailbox.
12. Label the laptop and record its asset tag and assigned user.
13. Confirm that no new phone is needed, since Jordan will use the existing desk phone.
```

Observation: Thirteen items under the three requested groups. Several are not in the request and are at most implied: item 4 (permissions for a part-time receptionist), item 9 (OS updates and 'the client's standard image'), item 12 (asset tag). Item 9 sits under Hardware although it is software work. November 2, 2026 is a Monday (checked with Python's datetime). The card's Notes record the additions.

## Prompt 21 (Skills Lab 5A pre-check: Weak Prompt 1 as written (author check, not shown in the chapter or the packet))

```text
Write a services page for Copperwind IT Services.
```

Response:

```text
# Copperwind IT Services

**Managed IT for Phoenix businesses. Two teams, one point of contact.**

Your technology should work so your people can. Copperwind IT Services handles the computers, networks, and accounts behind your business. You call one number, and the right team picks up.

## Our Services

### Deskside Support

Our Deskside team looks after the people and devices on your staff.

* **Help desk:** Call, email, or open a ticket. A technician answers and tracks the request to completion.
* **Onboarding and offboarding:** New hires get set-up laptops and accounts on day one. Departing staff lose access the same day.
* **Device management:** We patch, update, and replace computers, printers, and phones on a schedule.
* **Software and licensing:** We install, update, and track the applications your team uses.
* **On-site visits:** When a problem needs hands, a technician comes to you.

### Network Operations

Our Network Ops team keeps your connections running and your data protected.

* **Network design and setup:** Wired, wireless, and remote access built for the size of your office.
* **Monitoring and alerts:** We watch your network and fix many problems before you notice them.
* **Security basics:** Firewalls, multi-factor authentication, email filtering, and staff awareness tips.
* **Backup and recovery:** Regular backups, tested restores, and a written plan for the day something fails.
* **Cloud and email:** Microsoft 365 and Google Workspace setup, migration, and administration.

## How We Work

1. **Assess.** We review your devices, network, accounts, and risks. You get a plain-language report.
2. **Plan.** We agree on priorities, a budget, and a schedule. No surprises.
3. **Support.** Your help desk, monitoring, and maintenance begin. We check in on a regular cadence.
4. **Improve.** Each quarter we review tickets and trends, then recommend changes that reduce repeat problems.

## Why Copperwind

* **Local.** We are based in Phoenix and can be at your door when you need us.
* **Clear.** We explain problems in everyday language and tell you what a fix costs before we start.
* **Documented.** Every change is written down, so anyone on our team can pick up where another left off.
* **Accountable.** You always know who owns your request and where it stands.

## Who We Serve

Copperwind works with small and mid-sized organizations that need dependable IT without hiring a full department. Offices, clinics, nonprofits, and professional firms all fit.

## Get Started

Ready to talk? Request a free technology review. We will look at your current setup and tell you what is working, what is at risk, and what to fix first.

**[Request a free review]** | **[Call or email our team]**

---

*Notes for you: I kept the page free of prices, hours, response-time promises, and phone numbers, since I do not know yours. Add those before publishing. I can also adjust the tone, shorten it for a landing page, or add a service-tier comparison table if you would like.*
```

Observation: Confirms the weak prompt fails: the page invents services (on-site visits, cloud and email administration naming two vendor suites, a free technology review), a four-step process, and promises ('tell you what a fix costs before we start'). Students generate their own run in the lab. This capture only checks that the lab works.

## Prompt 22 (Skills Lab 5A pre-check: Weak Prompt 2 as written (author check, not shown in the chapter or the packet))

```text
Write an email to our clients announcing our new backup service. Make it exciting so they sign up.
```

Response:

```text
**Subject:** Your data, protected automatically. Meet [Service Name]

Hi [First Name],

Imagine losing every file on your computer tomorrow. Now imagine getting it all back in minutes.

That's what [Service Name] does. Today we're launching our new backup service, built to keep your business running no matter what happens.

**What you get**

* **Automatic daily backups.** Set it once and forget it. No manual steps, no missed files.
* **Fast recovery.** Restore a single file or a whole system in minutes, not days.
* **Secure, encrypted storage.** Your data stays protected in transit and at rest.
* **Ransomware protection.** Clean copies of your data stay out of an attacker's reach.
* **Real people on your side.** Our team monitors your backups and fixes problems before you notice them.

**Launch offer**

Sign up by [date] and get [offer, e.g., your first 30 days free / 20% off your first year / free setup].

**Getting started takes about 10 minutes**

1. Reply to this email or call us at [phone number].
2. We'll set up [Service Name] for you.
3. You're protected.

[Button: Protect My Data]
[Link to sign-up page]

Hardware fails. Mistakes happen. Threats keep growing. A good backup means none of it can take your business down.

Questions? Just reply to this email. I'm happy to walk you through it.

Best,
[Your Name]
[Title], [Company Name]
[Phone] | [Email]

---

**Alternate subject lines:**

* What would you do if your files disappeared tomorrow?
* New from [Company Name]: backups that protect themselves
* Launch offer inside: protect your data for [offer]

**A few notes:**

* Fill in the bracketed items with your real details. Specific numbers (recovery time, storage amount, price) make the email more convincing than general claims.
* Only list features the service delivers. Clients remember a broken promise longer than a good pitch.
* If you can, add a short customer story or a statistic about data loss. It makes the stakes concrete.

If you send me the service name, pricing, and key features, I can tailor this version and tune the tone for your audience.
```

Observation: Confirms the weak prompt fails the way the facts file is built to catch: 'Restore a single file or a whole system in minutes', 'Ransomware protection', 'Automatic daily backups' (the facts say nightly), a launch offer, and 'none of it can take your business down'. Students generate their own run in the lab.

## Prompt 23 (Skills Lab 5A pre-check: Weak Prompt 3 as written (author check, not shown in the chapter or the packet))

```text
Give me some taglines and a blurb about our Deskside team for the services page.
```

Response:

```text
**Taglines**

1. Your people, back to work.
2. Real help, right at your desk.
3. Fast fixes. Friendly faces.
4. Technology that stays out of your way.
5. We come to you. We fix it. You keep working.
6. The first call when something breaks.

**Blurb**

Our Deskside team keeps your people productive. When a laptop stalls, a printer quits, or a new hire needs a setup, a technician comes to you. We explain what went wrong in plain language and fix it right the first time. We also handle the routine work that prevents tomorrow's problems: new-device setup, software updates, and account support. You get one friendly team that knows your office and your people by name.

**Short version (for a service card)**

Hands-on tech support at your desk. We set up devices, solve problems, and keep your team working.

I left out specifics like response times, hours, and service area because I don't have them. Add those and the copy gets stronger.

A1. Send me your company name and a few real details (response time, coverage area), and I'll fold them in.
A2. Tell me the tone you want (warmer, more formal, more playful) and I'll rework the taglines.
```

Observation: Confirms the weak prompt fails on structure and specificity: six taglines and a blurb of no stated length, plus claims the facts file does not support ('a technician comes to you', 'fix it right the first time'). The response ends with two lines labeled A1 and A2, copied as returned.
