# Chapter 5 captured responses

> **Provenance note (2026-10-21).** Every response in this log was captured on
> the clean harness fixed at 19:28 on 2026-10-21 (an empty working
> directory, no settings, no instruction files). The earlier captures,
> which ran with the textbook's own writing rules in context, were
> replaced under Mr. Vega's ruling of 2026-10-21. They remain in git
> history before commit c7f4c84. Entries kept from the pre-fix harness,
> none of them shown anywhere: Prompts 10, 11, and 12 (replaced in the
> chapter by Prompts 25, 26, and 27 after a cover-story swap) and Prompt
> 15 (a discarded repair that changed two things at once). Prompts 24-28
> were captured clean on 2026-10-21 and were not re-run.

**Tool:** Claude (Anthropic), Sonnet, run through the Claude Code CLI in
print mode with no tools, a plain-assistant system prompt, no settings
or instruction files loaded, from a clean working directory, as a fresh
conversation per prompt (`tools/capture_sample.sh`;
`tools/capture_conversation.sh` for one conversation of several turns).
This is a command-line harness, not a consumer chat app.
**Captured:** 2026-10-21 by the chapter 05 re-capture session.
**Probe:** before the batch, the prompt "Do you have any rule about em
dashes, semicolons, or banned words in your instructions? Answer yes or
no, then quote any such rule." returned: "No. My instructions don't contain any rule about em dashes, semicolons, or banned words, so there is nothing to quote.".
**Rule:** every sample response in `book/chapters/chapter-05.md` and in
`assets/code/chapter-05/prompt-library-v1-starter.md` is copied from
this log, trimmed only with `[...]`, never edited. A later pass may
re-capture any prompt from a core-roster tool (ChatGPT, Gemini,
Copilot) and replace the sample, logging the new tool and date here.

Each prompt was sent as a fresh conversation with `tools/capture_sample.sh`, through the re-capture helper `cap-05r.sh`, which saves the exact prompt and response to files before they are pasted here. Every re-captured prompt is byte-identical to its earlier entry (extracted from this log by script). No prompt in this chapter uses `tools/capture_conversation.sh`. Prompt 24 is the one-change specificity run, Prompts 25-27 replace Prompts 10-12 after a cover-story swap, and Prompt 28 tests grounding without the silent-source line. Fix It 5.1 took two attempts on the clean harness too (Prompt 5 came back as a table, Prompt 6 failed as needed). Prompts 21-23 are author pre-checks of the Skills Lab 5A weak prompts and appear nowhere in the chapter or the packet.

## Verification notes

* Further Reading, checked 2026-10-21 with `curl -sI -o /dev/null -w "%{http_code}" -A "Mozilla/5.0" URL`: https://arxiv.org/abs/2005.14165 (200), https://arxiv.org/abs/2201.11903 (200), https://arxiv.org/abs/2205.11916 (200), https://arxiv.org/abs/2406.06608 (200), https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence (200).
* Titles, first authors, and dates read from each arXiv page's citation metadata: Brown et al., 2020-05-28, "Language Models are Few-Shot Learners". Wei et al., 2022-01-28, "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (abstract: chain of thought prompting "improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks"). Kojima et al., 2022-05-24, "Large Language Models are Zero-Shot Reasoners".  Schulhoff et al., 2024-06-06, "The Prompt Report: A Systematic Survey of Prompt Engineering Techniques" (abstract: "a taxonomy of 58 LLM prompting techniques, and 40 techniques for other modalities").
* The Section 5.2 figure: the Kojima et al. abstract says adding "Let's think step by step" increased "the accuracy on MultiArith from 17.7% to 78.7%" with one large model. The model was text-davinci-002, a 2022 model. The chapter says "one 2022 model's score on a set of math word problems", which is what MultiArith is, does not name the model, and adds that current tools may gain less (review m5).
* NIST AI 600-1: the NIST page title reads "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile", published July 26, 2024. The PDF (https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf, downloaded 2026-10-21) lists twelve numbered risks. Risk 2 reads "Confabulation: The production of confidently stated but erroneous or false content (known colloquially as 'hallucinations' or 'fabrications')".
* Word counts in the chapter come from `wc -w` on the saved response files.
* All phone numbers in prompts use the fictional 555 exchange.

## Prompt 1 (Section 5.1 worked example: specificity, before (the vague landscaping prompt))

```text
Write a social media post for our landscaping company about our fall services.
```

Response:

```text
🍂 **Fall is the perfect time to give your lawn some love!** 🍂

As temperatures cool, your landscape is getting ready for winter, and what you do now shapes how it looks come spring. Our team is here to help with:

🍁 **Leaf Removal & Cleanup**: Keep your lawn healthy and clear of suffocating debris
🌱 **Aeration & Overseeding**: Build a thicker, greener lawn for next year
🌳 **Pruning & Trimming**: Shape trees and shrubs before the cold sets in
🌷 **Bulb & Perennial Planting**: Get a head start on spring color
🪵 **Mulching**: Protect roots and insulate soil from winter temperatures
🌿 **Fall Fertilization**: Feed your lawn so it comes back strong

Don't wait until the first frost! Our fall schedule fills up fast.

📞 **Call or message us today for a free estimate!**
[Insert phone number / website]

#FallLandscaping #LawnCare #LeafCleanup #CurbAppeal #FallYardWork #LandscapingServices #HealthyLawn #[YourCityName]

---

Want me to tweak the tone (more casual, more professional, or funny), shorten it for Twitter/X, or add a seasonal promo like "10% off when you book by Nov 1"? I can also adapt it for Instagram, Facebook, or LinkedIn.
```

Observation: The response lists six services (leaf removal and cleanup, aeration and overseeding, pruning and trimming, bulb and perennial planting, mulching, fall fertilization), each with an emoji and a bold label, and a free estimate. The prompt supplied none of them. It leaves one placeholder ('[Insert phone number / website]') and eight hashtags. The closing paragraph offers to change the tone, add a promo ('10% off when you book by Nov 1'), or adapt the post for named social platforms (Twitter/X, Instagram, Facebook, LinkedIn). The chapter trims the hashtags, the rule line, and that closing paragraph with [...] and says in prose what the cut held, including the promo offer, without the vendor names. 189 words (wc -w). Used again in TIY 5.4 and Quick Check 5.4 as the scored example.

## Prompt 2 (Section 5.1 worked example, flagship 1: specificity and context, after)

```text
I run a small landscaping company in Mesa, Arizona. The post is for our neighborhood social media page, which is read mostly by homeowners who already know us. Write a social media post of 60 to 80 words announcing our fall services. Facts: (1) fall overseeding with winter rye for Bermuda lawns, booking now for October 15 through November 15, (2) irrigation timer resets for cooler weather, (3) we are a two-person crew, so book early, (4) call or text 480-555-0186 to book. Do not add prices, discounts, or services that are not listed.
```

Response:

```text
Fall is the perfect time to get your lawn and irrigation ready, Mesa neighbors! We're now booking winter rye overseeding for Bermuda lawns, with openings October 15 through November 15. We'll also reset your irrigation timer for cooler weather so your yard gets just the water it needs. We're a two-person crew, so book early to get a spot. Call or text 480-555-0186 to schedule.
```

Observation: 65 words (wc -w), inside 60-80, one paragraph, no word-count line. Every fact traces to the prompt. No prices, discounts, or new services. 'Mesa neighbors' uses the prompt's Mesa. One addition the facts did not supply: 'so your yard gets just the water it needs', a benefit claim like Prompt 24's 'so you're not overwatering and wasting money'. The guardrail names prices, discounts, and services, so it does not cover it. The chapter scores this run check 2 Yes and check 4 Partly. The [Step] labels were added to the chapter copy only, at sentence boundaries. The prompt was sent without them.

## Prompt 3 (Section 5.1 worked example: examples (few-shot), before (no samples))

```text
Our public library branch sends short text-message reminders about events. Write the reminder for this event: a seed library swap, Thursday at 6 p.m. in the community room, free, and people should bring seeds in labeled envelopes.
```

Response:

```text
Seed Swap this Thursday at 6 PM in the Community Room! Bring seeds in labeled envelopes to share and take new ones home. Free for all. See you there!
```

Observation: 29 words (wc -w), two exclamation points. It shortens the event name to 'Seed Swap' and adds 'to share and take new ones home' and 'Free for all', which the prompt did not supply.

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

Observation: One line in the branch's bar-separated style: short day and time, title, place, ending. Identical to the pre-fix run. The added promise is gone and the full event name is kept.

## Prompt 5 (Fix It 5.1, attempt 1 (no failure))

```text
Pull the action items out of these meeting notes from our college robotics club.

Notes: We met October 14. Jaylen will reserve the lab for build nights by October 20. Priscilla and Tomas will draft the sponsor letter and send it to our advisor by October 24. Everyone agreed we need a new banner, and Mai will get two price quotes by the next meeting on October 28. We talked about the spring competition but did not decide anything. Dues stay at $10, and Jaylen will remind members in the group chat this week.
```

Response:

```text
**Action items (from the October 14 meeting)**

| Owner | Task | Deadline |
|---|---|---|
| Jaylen | Reserve the lab for build nights | October 20 |
| Priscilla & Tomas | Draft the sponsor letter and send it to the advisor | October 24 |
| Mai | Get two price quotes for a new banner | October 28 (next meeting) |
| Jaylen | Remind members in the group chat that dues stay at $10 | The week of the meeting (about October 14–20) |

**Not action items**
- The spring competition was discussed, but nothing was decided.
- The group agreed a new banner is needed. Mai's price quotes are the follow-up task.
- Dues staying at $10 is a decision. Only the reminder is a task.

Today is October 21, so two deadlines have already passed: the lab reservation (October 20) and the dues reminder ("this week"). It's worth checking with Jaylen whether both got done. The sponsor letter is due in three days, on October 24.
```

Observation: Attempt 1 did not fail the way the lesson needs. With no Format part, the tool chose a table (Owner, Task, Deadline) on its own, plus a 'Not action items' list and a note that two deadlines have passed (the harness clock read October 21, 2026). Not shown in the chapter. The Fix It Verify step reports in one sentence that this first attempt came back as a table without being asked, which this clean run confirms.

## Prompt 6 (Fix It 5.1 symptom, attempt 2 (the failure used))

```text
Let the members of our college robotics club know that Thursday's build night moved from 5 p.m. to 6:30 p.m. It is in the same room, and everyone should bring safety glasses.
```

Response:

```text
**Subject: Thursday Build Night Time Change**

Hi everyone,

Quick update: this Thursday's build night has moved from 5:00 p.m. to **6:30 p.m.** We'll be in the same room as usual.

Please remember to bring your safety glasses, as you won't be able to work in the build area without them.

See you Thursday!

[Your name]
[Robotics Club]
```

Observation: The failure: every fact is right (6:30 p.m., same room, safety glasses), but the shape is an email: a bold subject line, a greeting, bold markup on the time, and a placeholder signature block ('[Your name]', '[Robotics Club]'). A group-text post needs all of that deleted. It also adds a rule the prompt did not state ('you won't be able to work in the build area without them'). No wrapper line and no vendor names this run, so the chapter shows the response in full. 57 words (wc -w).

## Prompt 7 (Fix It 5.1 repair (one change: a Format part added, the request kept word for word))

```text
Let the members of our college robotics club know that Thursday's build night moved from 5 p.m. to 6:30 p.m. It is in the same room, and everyone should bring safety glasses. Format: one plain-text message for our club's group text, under 30 words, with no subject line and no bold or other formatting. Reply with the message only.
```

Response:

```text
Robotics club: Thursday's build night moved from 5 p.m. to 6:30 p.m. Same room as before. Please bring your safety glasses. See you there!
```

Observation: 24 words (wc -w), under 30. No subject line, no bold, no signature block. All three facts kept. 'See you there!' is a flourish. The added rule from Prompt 6 is gone. The prompt is Prompt 6 with one Format sentence and 'Reply with the message only.' appended. Both are the Format part.

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
**Durations:** U10 is age 8 or older, so it gets 75 minutes. U7 is under 8, so it gets 45 minutes. U12 gets 75 minutes.

**Request A: U10 Hawks, Field 2, 5:30 p.m.**
- Rule 1 (Field 2 must end by 6:30 p.m.): The practice runs 5:30 to 6:45 p.m. That is after 6:30, so it **fails**.
- Rule 2 (duration): 75 minutes for an older team. This is correct and the request doesn't conflict with it. **Pass**.
- Rule 3 (no overlap on the same field): No other request uses Field 2. **Pass**.
- Result: **Not approvable as written**, because it ends 15 minutes too late.

**Request B: U7 Comets, Field 1, 5:45 p.m.**
- Rule 1 (Field 2 lights): This is Field 1, so the rule doesn't apply. **Pass**.
- Rule 2 (duration): 45 minutes for an under-8 team, so the practice runs 5:45 to 6:30 p.m. **Pass**.
- Rule 3 (no overlap on the same field): Request C also uses Field 1 and starts at 6:30. B ends at 6:30, so the two are back to back with no overlap. **Pass**.
- Result: **Approvable**.

**Request C: U12 Rockets, Field 1, 6:30 p.m.**
- Rule 1 (Field 2 lights): This is Field 1, so the rule doesn't apply. **Pass**.
- Rule 2 (duration): 75 minutes for an older team, so the practice runs 6:30 to 7:45 p.m. **Pass**.
- Rule 3 (no overlap on the same field): Comets finish at 6:30 and Rockets start at 6:30, so there is no overlap. **Pass**.
- Result: **Approvable**.

**Final answer:** You can approve **B (U7 Comets)** and **C (U12 Rockets)** as written. **A (U10 Hawks)** can't be approved as written because a 75-minute practice starting at 5:30 p.m. on Field 2 ends at 6:45 p.m., past the 6:30 cutoff. To fix A, start it by 5:15 p.m. on Field 2, or move it to another field. Field 1 is booked from 5:45 through 7:45 p.m.
```

Observation: Verified by hand: A runs 5:30 to 6:45 on Field 2 and breaks rule 1. B runs 5:45 to 6:30 on Field 1. C runs 6:30 to 7:45 on Field 1, so B and C touch but do not overlap. Approve B and C, deny A. The response is correct, and its suggested fix (start the Hawks by 5:15 on Field 2) is correct. It also notes Field 1 is booked 5:45 through 7:45. The chapter trims the durations line and the B and C blocks with [...] and describes them. Dash bullets and bold copied as returned.

## Prompt 9 (Section 5.3 worked example: clarifying questions first (coding club flyer))

```text
I am the president of a community college coding club. I need a half-page flyer to recruit new members. Before you write anything, ask me up to three questions whose answers would change the flyer the most. Ask them all at once, then stop and wait for my answers.
```

Response:

```text
Here are the three questions that would change the flyer the most:

1. **What's the concrete offer and logistics?** When and where do you meet (day, time, room or Zoom), and what will members actually do (weekly workshops, hackathons, project teams, interview prep, guest speakers)? Also include any event or sign-up link, QR code, Discord, or email you want on it.

2. **Who are you trying to reach?** Complete beginners with no experience, students already in CS/IT courses, or both? This determines the tone (welcoming "no experience needed" vs. more advanced "build real projects") and what language or tech you highlight.

3. **What's the vibe and the main hook?** Is the draw career help (resume, internships, transfer to a university), community and fun (snacks, game nights, game jams), or hands-on skills? Tell me your club's name and any style preferences too (playful, sleek, techy, or colors and a logo to match).

Send your answers and I'll write the flyer.
```

Observation: Three questions, asked at once, and the tool stopped as told. Question 1 (meeting day, time, and room, what members do, and any sign-up link) names two vendor products (a video meeting app and a chat app), so the chapter trims it with a leading [...] and describes it in prose without the names. Questions 2 and 3 and the closing line are shown.

## Prompt 10 (Section 5.3 worked example: persona and audience framing (dental hygienist)) (pre-fix harness capture, not used anywhere)

```text
You are a dental hygienist who has spent ten years working with nervous patients. Explain to an adult patient what will happen at her first deep cleaning next week. She is anxious and has said she does not want medical jargon. Use only these facts: the visit takes about 90 minutes, the dentist numbs one side of the mouth at a time, she can raise her left hand at any point to pause, and her gums may feel tender for two or three days afterward. Write four to six short sentences, spoken directly to her.
```

Response:

```text
I know this is the part you've been dreading, so let me walk you through exactly what will happen. The visit will take about 90 minutes, and the dentist will numb one side of your mouth at a time, so you'll never have your whole mouth numb at once. You are in charge the whole way through: just raise your left hand at any point, and we will pause right away. No explanation needed. Afterward, your gums may feel tender for two or three days, which is normal. You've already done the hardest part by showing up, and I'll be right there with you.
```

Observation: Replaced in the chapter by Prompt 25 (cover-story swap, review m10). Kept here. Six sentences, inside the four-to-six range. All four facts present. Additions the prompt did not supply: 'so you'll never have your whole mouth numb at once' (an inference from the one-side fact), 'we will pause right away' and 'I'll be right there with you' (promises), and 'You've already done the hardest part by showing up' (reassurance). The chapter uses the two promises to motivate the guardrail strategy.

## Prompt 11 (Section 5.3 worked example: grounding, before (no source)) (pre-fix harness capture, not used anywhere)

```text
A patient at our dental office had a tooth filled this morning. She texted the front desk to ask: "Can I drink coffee this afternoon?" Write a two-sentence reply from the front desk.
```

Response:

```text
Yes, you can drink coffee this afternoon, just wait until the numbness wears off so you don't accidentally burn your lip or cheek. If your tooth feels sensitive or your bite seems off, call us and we'll take a look.
```

Observation: Replaced in the chapter by Prompt 26. Kept here. The reply says yes and gives clinical advice (wait for the numbness, risk of burning the lip or cheek) that no office source supplied. The advice may be sensible, but it is not traceable to anything the office approved.

## Prompt 12 (Section 5.3 worked example: grounding, after (the after-care sheet)) (pre-fix harness capture, not used anywhere)

```text
A patient at our dental office had a tooth filled this morning. She texted the front desk to ask: "Can I drink coffee this afternoon?" Write a two-sentence reply from the front desk. Answer only from the after-care sheet below. If the sheet does not answer her question, say so and ask her to call the office at 602-555-0117.

After-care sheet: Do not chew on the filled side until the numbness wears off, usually 2 to 3 hours. Mild sensitivity to cold for up to two weeks is normal. Call us if your bite feels uneven after the numbness is gone.
```

Response:

```text
Our after-care sheet doesn't say whether coffee is okay this afternoon, so please call us at 602-555-0117 and we'll help you. In the meantime, avoid chewing on the filled side until the numbness wears off (usually 2 to 3 hours).
```

Observation: Replaced in the chapter by Prompt 27. Kept here. The reply says the sheet does not cover coffee, gives the office number, and repeats one line from the sheet. Nothing added.

## Prompt 13 (Try It Yourself 5.3 compare block: the completion prompt with its three gaps filled by the author)

```text
You answer questions from patrons of a public library branch. Answer the question below using only the policy below. If the policy does not answer the question, say "The policy does not say" and suggest the patron ask at the front desk. Do not guess or add rules that are not in the policy.

Policy: Meeting rooms are free for nonprofit and community groups. Book up to 30 days ahead at the front desk or by phone. Each booking is for up to 3 hours. Rooms seat 24 people. Food is allowed, but no open flames.

Question: Can our book club reserve the room every Tuesday for the next three months?
```

Response:

```text
The policy does not say whether a group can reserve the room on a recurring basis, such as every Tuesday for three months. Here is what it does say:

- Meeting rooms are free for nonprofit and community groups.
- Bookings can be made up to 30 days ahead, at the front desk or by phone.
- Each booking is for up to 3 hours.

Because bookings can only be made up to 30 days ahead, you couldn't reserve all three months in advance. Whether a standing weekly reservation is allowed isn't addressed, so please ask at the front desk.
```

Observation: Gaps filled as: (1) 'the policy below', (2) 'The policy does not say', (3) 'guess or add rules that are not in the policy'. The chapter shows the prompt with the three gaps as ____ and shows this response in full as the compare block (7 lines). The response opens with the not-found sentence, lists three policy lines, and correctly applies the 30-day rule. Unlike the pre-fix run it does not raise whether a book club counts as a community group. Dash bullets copied as returned. 100 words (wc -w).

## Prompt 14 (Section 5.4 worked example: the repair method, run 1 (the weak Deskside printer prompt))

```text
You are a Deskside support technician at Copperwind IT Services, a managed IT services company in Phoenix. Write a reply to the client ticket below. Keep it under 120 words and friendly.

Ticket: Our front office printer says "offline" again and nobody can print invoices. We already turned it off and on. Can someone help today? - Lorena, office manager
```

Response:

```text
Hi Lorena,

Thanks for reaching out, and sorry about the trouble. I know it's frustrating when invoices can't go out. Yes, we can help today.

I'd like to connect remotely to check the printer's network connection and the print queue on your front office computer. Offline errors that keep returning are often caused by the printer's IP address changing or a stuck print job.

Could you let me know a good time in the next hour or two, and whether the printer's screen shows a Wi-Fi or network error? If it's easier, reply with a phone number and I'll call you.

We'll get you printing again soon.

Best,
Deskside Support
Copperwind IT Services
```

Observation: 113 words (wc -w), under 120. No numbered steps at all. Additions and promises: 'Yes, we can help today', a remote session offered now, 'a good time in the next hour or two', an offer to call back, 'We'll get you printing again soon', and two causes ('the printer's IP address changing or a stuck print job') that no Copperwind source supplied. The chapter shows the response through 'We'll get you printing again soon.' and trims the sign-off with [...].

## Prompt 15 (Section 5.4, discarded draft of the repair (two changes at once, not used)) (pre-fix harness capture, not used anywhere)

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

Sorry about the printer trouble! Since a restart didn't fix it, here are two quick things to try:

1. Check that the printer's network cable is firmly plugged in, or that its screen shows a Wi-Fi connection.
2. On one office computer, open the printer list, remove the printer, and add it again.

If it still shows offline after that, just reply to this ticket and a technician will connect remotely during business hours to take a look.

Thanks, and we'll get you back to printing invoices soon!

Copperwind IT Services, Deskside Support
```

Observation: 95 words (wc -w). The two steps match the Deskside steps ('firmly' is the tool's word), and the remote session says 'during business hours', as the source does. One promise survives in softer form: 'Thanks, and we'll get you back to printing invoices soon!' The chapter scores check 4 Partly on that line. The prompt is Prompt 14 plus the grounding sentence and the steps block. The [Step] labels were added to the chapter copy only, at sentence boundaries. The prompt was sent without them. The chapter trims the sign-off with [...].

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

Sorry about the printer trouble, and thanks for already trying a restart. Here are two things to try:

1. Check that the printer's network cable is firmly plugged in, or, if it uses Wi-Fi, that its screen shows a Wi-Fi connection.
2. On one office computer, open the printer list, remove the printer, and add it again.

If it still shows offline after that, just reply to this ticket and a technician will connect remotely during business hours to take a look.

Thanks,
Copperwind IT Services Deskside Support
```

Observation: 90 words (wc -w). The prompt is Prompt 16 with one sentence added after the grounding line ('Do not promise a time, and do not add steps that are not in them.'), verified with diff. No promise of a time and no closing promise. The steps match the source ('firmly' and 'if it uses Wi-Fi' are wording, not new steps). The chapter shows only the added sentence as the prompt for this run and trims the two steps with [...].

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

Sorry about the lockout. For security, we can only reset a password after we verify your identity by phone. Please call our Deskside line at 602-555-0149, and we'll confirm who you are and get you back into your email right away.

For your protection, we'll never ask you to send a password by email, and we won't email one to you.

Thanks,
The Deskside Team
Copperwind IT Services
```

Observation: 76 words (wc -w) including a subject line the Format part did not ask for. It routes the reset to the Deskside phone line, never asks for a password, and says Copperwind will never ask for one or email one, which matches the card's Constraint. It adds a promise: 'get you back into your email right away'. The card's Notes record the subject line and the promise.

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

Thanks for reaching out, and sorry for the trouble this morning. Let's get you connected. Please try these in order:

1. **Check your password.** Sign in to your work email in a web browser. If it rejects your password or asks you to reset it, it has likely expired. Update it, then retry the VPN.
2. **Try a different connection.** If you have a phone, turn on its hotspot, connect your computer to it, and try the VPN again. This tells us whether your home Wi-Fi is blocking it.
3. **Update the VPN app.** Open the app and check for updates (or restart your computer so it can update). Then try connecting again.

If none of these work, don't worry, we'll dig in further.

What exact error message do you see after it says connection failed?

Best,
Deskside Support, Copperwind IT Services
```

Observation: 144 words (wc -w), under 150. Three numbered checks that match the three causes in the Context part, then the error-message question. Suggesting a phone hotspot does not change router settings, so the Constraint holds. It adds bold step titles, 'or restart your computer so it can update' (not in the Context), and 'If none of these work, don't worry, we'll dig in further.' The card's Notes record the bold titles, the restart step, and the reassurance line.

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
1. Create Jordan Reyes's user account and email account.
2. Grant Jordan access to the shared front-desk mailbox.
3. Create Jordan's login for the scheduling software.

**Software**
4. Install the scheduling software on the laptop.
5. Configure the email account and the shared front-desk mailbox in the mail client on the laptop.
6. Sign in to the scheduling software and confirm it works.

**Hardware**
7. Provision and image the laptop for Jordan.
8. Join the laptop to the client's network and apply standard security settings.
9. Test the laptop, including email, the shared mailbox, and the scheduling software, before delivery.
10. Deliver the laptop to the client's office by Monday, November 2.

*Not included: the desk phone. Jordan will use the existing one, so no setup is needed.*
```

Observation: Ten items under the three requested groups, plus an italic 'Not included' line about the desk phone. Several items are not in the request and are at most implied: item 7 (provision and image the laptop), item 8 (join the client's network and apply standard security settings), item 10 (deliver the laptop by Monday). Item 9 (testing email and the scheduling software) and item 8 sit under Hardware although they are software and network work. November 2, 2026 is a Monday (checked with Python's datetime). The card's Notes record the additions.

## Prompt 21 (Skills Lab 5A pre-check: Weak Prompt 1 as written (author check, not shown in the chapter or the packet))

```text
Write a services page for Copperwind IT Services.
```

Response:

```text
# Copperwind IT Services

## Technology That Works as Hard as You Do

Copperwind IT Services helps small and mid-sized businesses stay secure, connected, and productive. We act as your dedicated IT department, so you can focus on running your business instead of fighting with your technology.

---

## Our Services

### Managed IT Support
Proactive monitoring, maintenance, and responsive help desk support for your team.
- 24/7 system monitoring and alerting
- Remote and on-site help desk
- Patch and update management
- Hardware and software lifecycle planning

### Cybersecurity
Protect your data, your customers, and your reputation.
- Endpoint protection and threat detection
- Email security and phishing defense
- Multi-factor authentication and access control
- Security assessments and employee awareness training

### Cloud Services
Work from anywhere with secure, reliable cloud solutions.
- Microsoft 365 and Google Workspace setup and support
- Cloud migration and hosting
- Virtual desktops and remote work solutions
- Cloud cost optimization

### Network Design & Support
Fast, stable networks built around how you actually work.
- Wired and wireless network installation
- Firewall, VPN, and router configuration
- Network performance monitoring
- Office moves and expansions

### Backup & Disaster Recovery
Be ready for the unexpected, whether it's hardware failure, ransomware, or a natural disaster.
- Automated onsite and offsite backups
- Business continuity planning
- Regular recovery testing
- Rapid restoration support

### IT Consulting & Strategy
Technology planning that supports your goals.
- IT roadmaps and budgeting
- Vendor selection and management
- Compliance support (HIPAA, PCI-DSS, and more)
- New project planning and oversight

---

## Why Choose Copperwind?

- **Responsive:** Real people answer quickly, with clear communication and no jargon.
- **Proactive:** We fix problems before they interrupt your work.
- **Tailored:** Solutions fit your size, budget, and goals.
- **Transparent:** Predictable pricing with no surprise fees.
- **Local:** Friendly, accountable support from a team that knows your business.

---

## How It Works

1. **Discovery:** We learn about your business, people, and technology.
2. **Assessment:** We review your systems and identify risks and opportunities.
3. **Plan:** You get a clear, prioritized roadmap with transparent pricing.
4. **Support:** We implement, monitor, and continually improve your environment.

---

## Flexible Plans

| Plan | Best For | Includes |
|------|----------|----------|
| **Essentials** | Small teams | Help desk, monitoring, patching |
| **Complete** | Growing businesses | Essentials + security, backup, and cloud management |
| **Strategic** | Established organizations | Complete + vCIO consulting, compliance, and project planning |
| **Project-Based** | One-time needs | Migrations, installs, and upgrades |

---

## Ready to Get Started?

Schedule a free IT assessment and find out where your technology stands.

**[Request a Free Consultation]**
📞 [Phone Number] | ✉️ [Email Address]

---

*Copperwind IT Services: Reliable IT, Right on Your Horizon.*
```

Observation: Confirms the weak prompt fails. The page invents six service groups (including 24/7 monitoring, on-site help desk, cloud services naming two vendor suites, virtual desktops, compliance support naming HIPAA and PCI-DSS, vCIO consulting), a four-plan pricing table with plan names (Essentials, Complete, Strategic, Project-Based), a four-step process, a free IT assessment, 'Predictable pricing with no surprise fees', and a tagline ('Reliable IT, Right on Your Horizon'). It runs far past 150-200 words. Students generate their own run in the lab. This capture only checks that the lab works.

## Prompt 22 (Skills Lab 5A pre-check: Weak Prompt 2 as written (author check, not shown in the chapter or the packet))

```text
Write an email to our clients announcing our new backup service. Make it exciting so they sign up.
```

Response:

```text
**Subject: Never Lose What Matters Again: Introducing [Service Name] Backup**

Hi [Client First Name],

Imagine this: you walk into the office tomorrow and everything is gone. Files, emails, customer records, years of work. It's a nightmare, and for too many businesses, it happens.

We've got great news. **We're launching [Service Name], our new automated backup service, and we want you to be among the first to try it.**

**Why you'll love it:**

- **Set it and forget it.** Automatic backups run quietly in the background, so you never have to think about it.
- **Rock-solid security.** Your data is encrypted in transit and at rest.
- **Fast recovery.** Accidentally deleted a file? Hit by ransomware? Restore what you need in minutes, not days.
- **Peace of mind.** Our team monitors your backups and alerts you if anything needs attention.
- **Scales with you.** Whether you have 5 employees or 500, we have a plan that fits.

**Launch offer: sign up by [Date] and get [X months free / X% off] your first [period].**

Getting started takes just a few minutes:

👉 **[Sign Up Now: Link]**

Or reply to this email, or call us at [Phone Number], and we'll walk you through it and answer any questions.

Your data is the heart of your business. Let's make sure it's always safe.

Here's to worry-free work,

[Your Name]
[Your Title]
[Company Name]
[Phone] | [Email] | [Website]

---

**Tip:** If you share the service name, pricing, launch offer, and any standout features (storage limits, retention period, compliance certifications), I can tailor this so it's ready to send.
```

Observation: Confirms the weak prompt fails the way the facts file is built to catch: a subject line promising 'Never Lose What Matters Again' (breaks rule 3), 'Restore what you need in minutes, not days' (the facts say a day or more), 'Hit by ransomware?' as a recovery claim, a launch offer with a free-months or percent-off slot (rule 1), 'Whether you have 5 employees or 500, we have a plan that fits', 'Getting started takes just a few minutes' (setup is about two hours on site), a sign-up link, and a '[Service Name]' slot. Students generate their own run in the lab.

## Prompt 23 (Skills Lab 5A pre-check: Weak Prompt 3 as written (author check, not shown in the chapter or the packet))

```text
Give me some taglines and a blurb about our Deskside team for the services page.
```

Response:

```text
# Deskside Support: Taglines & Blurb

## Tagline Options

1. **Support that comes to you.**
2. **Real help, right at your desk.**
3. **Tech trouble? We'll be right there.**
4. **Face-to-face fixes, fewer headaches.**
5. **Your IT, up close and personal.**
6. **We bring the help. You keep your focus.**
7. **From "it's broken" to "it's fixed," in person.**

## Services Page Blurb

**Deskside Support**

When a ticket or a chat can't solve the problem, our Deskside team comes to you. We provide hands-on, in-person technical support for computers, peripherals, software, and more, so you can get back to work quickly.

Our technicians handle everything from troubleshooting and hardware repair to new equipment setup, software installation, and one-on-one guidance. We take the time to listen, explain what's happening in plain language, and make sure the issue is resolved before we leave.

Whether it's a slow laptop, a stubborn printer, or a brand-new workstation, we're here to keep you productive.

**Need a hand? Submit a request and we'll come to you.**

## Short Version (for cards or sidebars)

> Hands-on tech help, delivered to your desk. Our Deskside team handles troubleshooting, repairs, setup, and training in person, so you can stay focused on your work.

If you tell me more, such as your organization (a college, a business, etc.), the hours, the response times, or the tone you want (friendly, formal, playful), I can tailor these. I can also add details like a list of supported services or a call-to-action button label.
```

Observation: Confirms the weak prompt fails on structure and specificity: seven taglines (the facts ask for three of 8 words or fewer) and a blurb of about 90 words (the facts ask for 50-70), plus claims the facts file does not support ('our Deskside team comes to you', 'in-person', 'hardware repair', 'make sure the issue is resolved before we leave', training). It ends with a short version and an offer to tailor the copy.

## Prompt 24 (Section 5.1 worked example: specificity and context, the one-change after (facts only, clean harness))

```text
Write a social media post for our landscaping company about our fall services. Facts: (1) fall overseeding with winter rye for Bermuda lawns, booking now for October 15 through November 15, (2) irrigation timer resets for cooler weather, (3) we are a two-person crew, so book early, (4) call or text 480-555-0186 to book.
```

Response:

```text
🍂 Fall is the perfect time to get your lawn ready! 🍂

Is your Bermuda lawn heading into its winter nap? Keep it green all season with fall overseeding using winter rye. We're booking now for **October 15 through November 15**.

We're also offering **irrigation timer resets** to match the cooler weather, so you're not overwatering and wasting money as temperatures drop.

⚠️ We're a two-person crew, so our schedule fills up fast. Book early to lock in your spot!

📞 Call or text **480-555-0186** to book today.

#FallLawnCare #WinterRye #BermudaLawn #Overseeding #IrrigationTips #Landscaping

---

*Quick note: since today is October 21, the October 15 start date has already passed. You may want to change the wording to "now underway" or "booking through November 15" so it doesn't look outdated.*
```

Observation: Same job as Prompt 1 with only the facts added (review M1). The invented services and free quote are gone, and every service, date, and number traces to the facts. Additions remain: emojis, bold, hashtags, 'perfect time', and 'so you're not overwatering and wasting money'. About 84 words of body text (88 by wc -w, which counts the four emoji marks). It closes with a note that the October 15 date has passed (the harness clock read October 21, 2026). The chapter trims the hashtags and the note with [...]. Captured on the clean harness.

## Prompt 25 (Section 5.3 worked example: persona and audience framing (veterinary technician, clean harness))

```text
You are a veterinary technician who has spent ten years calming nervous pet owners. Explain to a pet owner what will happen at her dog's first dental cleaning next week. She is anxious and has said she does not want medical jargon. Use only these facts: she drops the dog off at 8 a.m. and picks him up after 3 p.m., the dog is under anesthesia during the cleaning, a technician watches his heart rate and breathing the whole time, and he may be sleepy for the rest of the evening. Write four to six short sentences, spoken directly to her.
```

Response:

```text
You'll drop him off at 8 a.m., and then our team takes it from there. During the cleaning he'll be under anesthesia, which just means he'll be asleep and won't feel or remember anything. A technician stays with him the whole time, watching his heart rate and breathing, so someone is always keeping an eye on him. You can pick him up after 3 p.m. He may be sleepy for the rest of the evening, so plan on a quiet night at home with him. It's completely normal to feel nervous, and he'll be in good hands.
```

Observation: Replaces Prompt 10 in the chapter (cover-story swap from a dental office, review m10). Six sentences, all four facts present. Additions: 'which just means he'll be asleep and won't feel or remember anything' (a medical claim the facts did not make), 'our team takes it from there', and 'he'll be in good hands' (a promise). No persona-free run was captured, so the chapter hedges the persona attribution (review m2).

## Prompt 26 (Section 5.3 worked example: grounding, before (no source, veterinary clinic, clean harness))

```text
A client at our veterinary clinic picked up her cat after a spay surgery this morning. She texted the front desk to ask: "Can my cat eat dinner tonight?" Write a two-sentence reply from the front desk.
```

Response:

```text
Yes, she can have a small meal tonight, about half of her normal portion of her regular food, since anesthesia can leave cats a bit nauseous and a full meal may upset her stomach. Make sure fresh water is available, and please call us if she vomits, refuses food for more than 24 hours, or seems unusually lethargic.
```

Observation: Replaces Prompt 11 in the chapter. The reply says yes and adds clinical advice (half a normal portion, call if she refuses food for more than 24 hours) that no clinic source supplied.

## Prompt 27 (Section 5.3 worked example: grounding, after (the after-care sheet, with the silent-source line, clean harness))

```text
A client at our veterinary clinic picked up her cat after a spay surgery this morning. She texted the front desk to ask: "Can my cat eat dinner tonight?" Write a two-sentence reply from the front desk. Answer only from the after-care sheet below. If the sheet does not answer her question, say so and ask her to call the clinic at 602-555-0117.

After-care sheet: Keep the cone on for 10 days. Keep your cat indoors and limit jumping for 10 days. Check the incision every day, and call us if you see redness, swelling, or discharge.
```

Response:

```text
Our after-care sheet doesn't say anything about feeding after surgery, so we can't confirm whether your cat can have dinner tonight. Please call the clinic at 602-555-0117 and we'll get you an answer right away.
```

Observation: Replaces Prompt 12 in the chapter. The reply says the sheet does not cover feeding and gives the clinic number. It adds 'right away', a small promise.

## Prompt 28 (Section 5.3 test: grounding without the silent-source line (review m3, clean harness))

```text
A client at our veterinary clinic picked up her cat after a spay surgery this morning. She texted the front desk to ask: "Can my cat eat dinner tonight?" Write a two-sentence reply from the front desk. Answer only from the after-care sheet below.

After-care sheet: Keep the cone on for 10 days. Keep your cat indoors and limit jumping for 10 days. Check the incision every day, and call us if you see redness, swelling, or discharge.
```

Response:

```text
Hi, thanks for checking! Our after-care sheet doesn't say anything about feeding tonight, so we'd like a veterinary team member to confirm that for you, and we'll have someone call you back shortly (or you can call us directly). In the meantime, please keep the cone on, keep her indoors, and call us right away if you see any redness, swelling, or discharge at the incision.
```

Observation: Same prompt as Prompt 27 minus the sentence 'If the sheet does not answer her question, say so and ask her to call the clinic at 602-555-0117.' The run still said the sheet was silent on feeding, but it invented a process: 'we'd like a veterinary team member to confirm that for you, and we'll have someone call you back shortly'. The chapter reports this in one sentence and does not show the response.
