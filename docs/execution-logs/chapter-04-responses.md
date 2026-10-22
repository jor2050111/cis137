# Chapter 4 captured responses

**Tool:** Claude (Anthropic), Sonnet, run through the Claude Code CLI in
print mode with no tools and a plain-assistant system prompt, as a fresh
conversation per prompt (the provenance line in `tools/capture_sample.sh`).
Prompt 13 is one conversation of three turns, captured with
`tools/capture_conversation.sh`, which resumes one session so the model
sees the earlier turns (same system prompt and flags).
**Captured:** 2026-10-21 by the chapter 4 build session.
**Rule:** every sample response in `book/chapters/chapter-04.md` is
copied from this log, trimmed only with `[...]`, never edited. A later
pass may re-capture any prompt from a core-roster tool (ChatGPT,
Gemini, Copilot) and replace the sample, logging the new tool and date
here.

Prompts 1-12 and 14 were each sent as a fresh conversation with `tools/capture_sample.sh`. Fix It 4.1 took three attempts with different question wordings (Prompts 7-9). Prompt 8 did not fail; it is logged and not used. Prompt 10 is the repair. Prompt 14 replaces Prompt 11 in the chapter. Character counts below come from `printf '%s' "$(cat response)" | wc -c`, which drops the final newline.

## Prompt 1 (Section 4.1 worked example: the bare prompt)

```text
Write a text message for our dental office's patients about the parking change.
```

Response:

```text
Here's a draft you can fill in:

**Text message (about 300 characters):**

Hi [First Name], this is [Office Name]. Starting [date], patient parking has moved to [new location/lot]. The old lot at [old location] will be closed. Look for our signs at the entrance. Questions? Call us at [phone number]. See you soon!

**Shorter version (under 160 characters):**

[Office Name]: Starting [date], please park in [new location]. The [old lot] is closed. Questions? Call [phone number].

**Details to confirm before sending:**
- Effective date, and whether the old lot closes the same day
- Exact location of the new parking (a street address or cross street helps)
- Whether parking is free, validated, or time-limited
- Accessible parking location, if it changed
- Whether you want to add "Reply STOP to opt out," which many text platforms require
```

Observation: The prompt named no facts, so the response returned a template of bracketed blanks ([First Name], [date], [new location/lot]) and a list of details to confirm. It invented no parking facts. It offered "Questions? Call us" and suggested a "Reply STOP to opt out" line, both unrequested. The chapter uses this response to show what leaving out the Context part costs.

## Prompt 2 (Section 4.1 worked example, flagship 1: the five-part prompt)

```text
You are the front desk coordinator at a small family dental office. Write a text message to patients who have appointments next week. The office parking lot will be repaved Monday through Wednesday, March 9 to 11. On those days, patients can park free in the church lot across the street on Cedar Avenue. Our entrance and hours do not change. Send one message, under 300 characters, in plain text with no emojis. Do not add any facts that are not in this prompt, and do not ask patients to reply.
```

Response:

```text
Parking lot repaving Monday through Wednesday, March 9 to 11. On those days, park free in the church lot across the street on Cedar Avenue. Our entrance and hours stay the same. See you at your appointment next week.
```

Observation: 216 characters, under the 300 limit. No emojis. Every fact traces to the prompt (repaving, March 9 to 11, the church lot on Cedar Avenue, entrance and hours unchanged, appointments next week). It does not ask patients to reply. It drops the greeting entirely. Step labels were added to the chapter copy only, at sentence boundaries; the prompt was sent without them.

## Prompt 3 (Section 4.4 worked example: flagship 1 with the Format part removed)

```text
You are the front desk coordinator at a small family dental office. Write a text message to patients who have appointments next week. The office parking lot will be repaved Monday through Wednesday, March 9 to 11. On those days, patients can park free in the church lot across the street on Cedar Avenue. Our entrance and hours do not change. Do not add any facts that are not in this prompt, and do not ask patients to reply.
```

Response:

```text
Hi from your dental office. Our parking lot will be repaved Monday through Wednesday, March 9 to 11. On those days, you can park free in the church lot across the street on Cedar Avenue. Our entrance and hours stay the same. We'll see you at your appointment next week.
```

Observation: Same prompt as Prompt 2 with the Format sentence ("Send one message, under 300 characters, in plain text with no emojis.") removed. 269 characters, still under 300. It adds an opening greeting ("Hi from your dental office.") and a contraction. No emojis, no reply request, no added facts.

## Prompt 4 (Section 4.4 worked example: flagship 1 with the Constraints part removed)

```text
You are the front desk coordinator at a small family dental office. Write a text message to patients who have appointments next week. The office parking lot will be repaved Monday through Wednesday, March 9 to 11. On those days, patients can park free in the church lot across the street on Cedar Avenue. Our entrance and hours do not change. Send one message, under 300 characters, in plain text with no emojis.
```

Response:

```text
Hi, this is your dental office. Our parking lot will be repaved Monday through Wednesday, March 9 to 11. On those days, please park free in the church lot across the street on Cedar Avenue. Our entrance and hours stay the same. See you next week!
```

Observation: Same prompt as Prompt 2 with the Constraints sentence ("Do not add any facts that are not in this prompt, and do not ask patients to reply.") removed. 246 characters. No added facts and no reply request on this run. Adds a greeting and an exclamation point ("See you next week!").

## Prompt 5 (Section 4.2 worked example: a completion prompt)

```text
Complete this message to families in the same voice. Add no more than two sentences.

Hi Hornets families! Saturday's practice moves indoors to the Desert Willow Elementary gym because the field is being reseeded. Same time, 9 a.m. Please bring
```

Response:

```text
water bottles, cleats or sneakers, and a healthy dose of Hornet energy. We can't wait to see everyone there!
```

Observation: The completion finished the sentence with three items the prompt never supplied ("water bottles, cleats or sneakers, and a healthy dose of Hornet energy") and added one closing sentence. Two sentences total, within the limit. Cleats are an odd fit for an indoor gym; the chapter uses this to show that a completion fills a gap with likely text.

## Prompt 6 (Section 4.2 worked example: a role play prompt)

```text
You are the treasurer of a community college's student government. I am the president of the college's Cybersecurity Club. I will ask you for $400 to send four members to a regional capture-the-flag competition. Stay in character. Ask me the two hardest questions a treasurer would ask about this request, then stop and wait for my answers. Do not answer for me.
```

Response:

```text
Thanks for coming in. I've read your request, and I have two questions before I can bring this to the board.

**Question 1: Where does the $400 go, line by line, and what is the club putting in?**
Four members, one regional competition. Break down the registration fees, travel, lodging, and meals. Then tell me what the club is contributing from its own funds, fundraising, or sponsors, and whether you've applied for money from anywhere else, like a department, a competition sponsor, or the college. If we fund this in full and the real cost is $900, what happens to the other $500?

**Question 2: What does the student body get back, and how do you choose who goes?**
Student government money belongs to every student, not just club members. How were these four members selected, and is the process open to anyone in the club? What will you deliver after the event? Think of a presentation, a workshop, a recruiting push, or a write-up. How will you show the board that $400 produced something beyond a trip for four people?

I'll wait for your answers.
```

Observation: Stayed in character, asked two questions (budget breakdown and club contribution; return to the student body and selection), and stopped to wait. Each question bundles several sub-questions. It did not answer for the student.

## Prompt 7 (Fix It 4.1, attempt 1 (the failure used))

```text
What would a good reply to this ticket look like?

Ticket from a client's office manager: "Since this morning my second monitor stays black. The laptop only sees one screen. I already unplugged the cable and plugged it back in. I have a client meeting at 2 p.m. and need both screens. Can someone help?"
```

Response:

```text
A good reply acknowledges the 2 p.m. deadline, gives her a few quick things to try in order, and offers a fast fallback if they fail. She has already reseated the cable, so don't make her repeat that.

**Sample reply**

Subject: Re: Second monitor not detected (let's get this fixed before 2 p.m.)

Hi [Name],

Thanks for the details, and for already trying the cable. We'll get you ready for your 2 p.m. meeting. Try these in order and stop as soon as the screen comes back:

1. **Check the monitor itself.** Make sure it is powered on (look for a light) and set to the right input. Press the Input or Source button on the monitor and try each option (HDMI, DisplayPort, USB-C).
2. **Restart the laptop with the monitor still plugged in.** This fixes a lot of "detected one screen" problems.
3. **Force a detection.** Press the Windows key + P and pick "Extend" (on a Mac, open System Settings > Displays and click "Detect Displays"). If you're on Windows, you can also right-click the desktop, choose Display settings, and click "Detect" under Multiple displays.
4. **Try a different port or cable**, if you have one. Plug the cable into another port on the laptop, or into a docking station port if you use one.

If none of that works, reply with a good number to reach you, or call us at [phone]. We can connect remotely and sort it out in a few minutes. If it turns out to be a hardware issue, we'll set you up with a workaround for the meeting, such as a loaner monitor or a single-screen setup with screen sharing.

[Your name]
[Company / phone]

**Why this works**

- **It leads with the deadline.** She told you what matters, so you show her you heard it.
- **The steps are short, ordered, and plain-language.** An office manager shouldn't need to know what a display driver is.
- **It skips what she already did.** Asking her to re-plug the cable would annoy her.
- **It offers a clear next step.** A remote session or phone call is the real safety net, and she knows when to use it.
- **It includes a plan B for the meeting.** Even if the hardware is dead, she knows she won't be stranded at 2 p.m.

**Things to adjust**

- Tailor the steps to her operating system if your records show it (Windows vs. Mac).
- If your SLA allows, check the time and consider calling her right away instead of emailing. With a 2 p.m. deadline, a call may resolve it faster than a ticket thread.
- Also ask what changed this morning (a Windows update, a new dock, a moved desk). A recent update often points straight to a driver issue.
```

Observation: The failure the lesson needs. The prompt asked a question, and the response answered it as a question: an explanation of what a good reply does, then a sample reply with placeholders inside a lesson, then "Why this works" and "Things to adjust" sections. A technician cannot paste it into the ticket without cutting most of it out. The sample reply also offers a loaner monitor, which nobody at the help desk promised.

## Prompt 8 (Fix It 4.1, attempt 2 (no failure, not used))

```text
How should I reply to this ticket?

Ticket from a client's office manager: "Since this morning my second monitor stays black. The laptop only sees one screen. I already unplugged the cable and plugged it back in. I have a client meeting at 2 p.m. and need both screens. Can someone help?"
```

Response:

```text
Here's a draft you can send:

---

Subject: Re: Second monitor stays black

Hi [Name],

Thanks for the details, and for trying the cable already. We'll get you ready for your 2 p.m. meeting. Please try these in order. Most cases clear up by step 2.

1. Check that the monitor has power and the right input. Press its menu or input button and select the port your cable uses (HDMI, DisplayPort, or USB-C).
2. On the laptop, press the Windows key + P and choose "Extend." On a Mac, open System Settings, then Displays, then "Detect Displays."
3. Reseat the cable at both ends, including the laptop or docking station side. If you have a spare cable or port, try it.
4. Restart the laptop with the monitor still connected.

If it's still black after that, reply with the laptop model, whether you use a docking station, and whether the monitor's power light is on. Or call us at [number] and we'll connect remotely. Since you're on a deadline, we'll make this a priority.

[Your name]
[Company]

---

Two notes before you send:

* I assumed Windows is the likely platform and included the Mac step as a fallback. Remove whichever doesn't apply if you know the client's setup.
* Fill in the phone number. I left it blank on purpose, since I don't have your support line.

Consider adding a fallback line if the fix isn't quick, such as "If we can't get both screens working by 1:30, we'll help you set up the meeting on one screen so you're covered." That gives her a safety net and shows you're watching the clock.
```

Observation: Did not fail the way the lesson needs: the question "How should I reply" got a draft first, with two notes and a suggestion after it. Logged and not used.

## Prompt 9 (Fix It 4.1, attempt 3 (same failure as attempt 1, not used))

```text
I work on a help desk. What should a good reply to this ticket say?

Ticket from a client's office manager: "Since this morning my second monitor stays black. The laptop only sees one screen. I already unplugged the cable and plugged it back in. I have a client meeting at 2 p.m. and need both screens. Can someone help?"
```

Response:

```text
A good reply does four things: it acknowledges the 2 p.m. deadline, gives short self-service steps in plain language, asks for the details you need if those fail, and offers a fallback so she isn't stuck.

**Sample reply**

Subject: Re: Second monitor is black (we'll get this fixed before 2 p.m.)

Hi [Name],

Thanks for the details. Reseating the cable was a good first step, and it rules out a loose connection.

Since you have a 2 p.m. meeting, here are the fastest checks. Stop as soon as the screen comes back.

1. **Force a screen search.** On Windows, press the Windows key + P and choose "Extend." On a Mac, open System Settings > Displays and hold Option to show "Detect Displays."
2. **Check the monitor itself.** Confirm the power light is on, then use the monitor's menu button to make sure the input matches the cable (HDMI, DisplayPort, or USB-C).
3. **Restart the laptop** with the monitor still plugged in and powered on.

If none of those work, please reply with:

* The laptop model and how the monitor connects (HDMI, USB-C, or a docking station)
* Whether the monitor's power light is on
* Anything that changed recently (updates, moved desk, new cable)

You can also call us at [number]. We can connect remotely and often fix this in a few minutes.

If we can't solve it by 1:00 p.m., we'll arrange a backup so you can present confidently. That could be a loaner cable or monitor, or a quick setup to share your screen from one display.

[Your name]
[Company] Help Desk

**Why this works**

* **Empathy and urgency first.** Naming the 2 p.m. meeting shows you read the ticket and sets your priority.
* **Credit what she already tried.** It builds trust and avoids repeating the cable step.
* **Three steps maximum.** A non-technical reader will follow a short list, not a long one.
* **Specific data requests.** "Laptop model, connection type, power light" gets you what you need in one round trip.
* **Fallback with a time.** The 1:00 p.m. cutoff gives you room to escalate or dispatch a loaner.

**Internal triage notes**

* Likeliest causes: wrong input source, a display setting reset by an overnight update, a failed cable or adapter, or a dead dock.
* If a dock is involved, check for a pending firmware or driver update.
* Tag the ticket high priority because of the deadline, and set a reminder to follow up around 12:30 p.m.
```

Observation: The same failure as Prompt 7 (an explanation, a sample reply inside a lesson, "Why this works," and internal triage notes). Not used, because Prompt 7 uses the exact wording of the lesson.

## Prompt 10 (Fix It 4.1 repair)

```text
Write the reply to this ticket that I will send to the client.

Ticket from a client's office manager: "Since this morning my second monitor stays black. The laptop only sees one screen. I already unplugged the cable and plugged it back in. I have a client meeting at 2 p.m. and need both screens. Can someone help?"
```

Response:

```text
**Subject:** Re: Second monitor stays black

Hi [Name],

Thanks for the details. We want you ready well before 2 p.m. Try these steps in order and stop as soon as the screen comes back:

1. **Wake the display.** On Windows, press the Windows key + P and choose "Extend." On a Mac, open System Settings, then Displays, and click "Detect Displays." Laptops often drop a second screen after sleep or an update, and this brings it back.
2. **Check the monitor.** Confirm it is powered on. Then press its menu button and select the input that matches your cable (HDMI, DisplayPort, or USB-C). A monitor on the wrong input shows a black screen.
3. **Swap what you can.** If you have a spare cable or a second port on the laptop, try them. A failed cable is a common cause.
4. **Restart with everything connected.** Turn the monitor on and plug it in, then restart the laptop.

If the screen is still black after these steps, reply with the make and model of your laptop and monitor, or call us at [phone number]. We can connect remotely and fix it with you on the line. Please let us know by 12:30 p.m. so we have time to work through it.

If we can't solve it before the meeting, we will help you set up a backup. One option is to join from the laptop alone and share your screen from there.

Thanks,
[Your name]
[Company] Help Desk

---

Notes for you before you send:
- I filled no names, phone number, or signature. Those are placeholders.
- I guessed at the OS, so the draft covers both Windows and Mac. Cut one if you know which it is.
- The 12:30 p.m. cutoff is my guess. Adjust it to your team's availability.
```

Observation: The one change: the question "What would a good reply to this ticket look like?" became the instruction "Write the reply to this ticket that I will send to the client." The ticket text is identical to Prompt 7. The response is a reply from the subject line to the signature, with no explanation before it and no "Why this works" section. After a separator it adds three short notes to the sender. It still adds a commitment the technician never made ("Please let us know by 12:30 p.m."), and its own notes call that cutoff a guess. The chapter's Verify step reports both.

## Prompt 11 (Section 4.3 worked example: zero-shot, first version (not used))

```text
Write a text message to a landscaping customer saying today's visit is done. Facts: the customer's name is Dana; we mowed and edged the front and back yards and trimmed the hedges; the drip line by the back fence is leaking.
```

Response:

```text
Hi Dana, today's visit is done. We mowed and edged the front and back yards and trimmed the hedges.

One thing to flag: the drip line by the back fence is leaking. Want us to take a look at it on our next visit, or would you rather we send a quote for the repair first?

Thanks!
```

Observation: Every fact traces to the prompt. It adds an offer the prompt did not include (look at the leak next visit, or send a quote) and a "Thanks!" sign-off. Three short paragraphs. Not used: the prompt's facts were joined with semicolons, which the book's prose law avoids, so the prompt was rewritten with periods and sent fresh as Prompt 14.

## Prompt 12 (Section 4.3 worked example, flagship 2: few-shot)

```text
Write a text message to a landscaping customer saying today's visit is done. Match the style of these two texts our owner wrote.

Example 1: "Hi Marcus, all done for today. Mowed, edged, and blew off the patio. Heads up: one sprinkler head by the mailbox is cracked. Want us to swap it next visit? Rosa"

Example 2: "Hi Joan, finished up. Trimmed the oleanders and cleared the side yard. Your back gate wasn't latching, so we tied it shut for now. Rosa"

Now write one for this visit. Customer: Dana. We mowed and edged the front and back yards and trimmed the hedges. The drip line by the back fence is leaking. Use only these facts.
```

Response:

```text
Hi Dana, all done for today. Mowed and edged the front and back yards and trimmed the hedges. Heads up: the drip line by the back fence is leaking. Want us to take a look at it next visit? Rosa
```

Observation: The response copies the examples' shape: one paragraph, "all done for today," a "Heads up:" line, an offer phrased as a question, and the owner's name as the sign-off. The offer ("Want us to take a look at it next visit?") is not among Dana's facts. Both zero-shot runs (Prompts 11 and 14) made a similar offer, so the chapter does not credit the offer to the examples. 40 words by wc -w. Every work fact traces to the prompt. Step labels were added to the chapter copy only, at sentence boundaries; the prompt was sent without them.

## Prompt 13 (Section 4.3 worked example: standing instructions, one conversation of three turns)

Turn 1:

```text
For the rest of this conversation, follow these standing instructions. I volunteer at the front desk of a public library branch. Write every answer for patrons who are new to computers: short sentences, no jargon, no more than five numbered steps, and end by telling them they can ask at the desk for help. Reply only with the word Ready to this message.
```

Response 1:

```text
Ready
```

Turn 2:

```text
How do I attach a photo to an email on my phone?
```

Response 2:

```text
Here is how to attach a photo to an email on your phone.

1. Open your email app. Tap the button to write a new message.
2. Look for a small paperclip or picture icon. Tap it. (On an iPhone, you may need to tap inside the message first. Then tap the small arrow and choose "Insert Photo.")
3. Tap "Photos" or "Gallery" to see your pictures.
4. Tap the photo you want. Then tap "Done," "Choose," or the check mark.
5. Type the person's email address. Tap the send button.

You will see the photo in your message before you send it.

If any step looks different on your phone, you can ask at the desk for help.
```

Turn 3:

```text
How do I make the text bigger on my phone?
```

Response 3:

```text
Here is how to make the text bigger on your phone. The steps are a little different for each kind of phone.

1. Open the "Settings" app. It has a gear icon.
2. On an iPhone, tap "Display & Brightness," then tap "Text Size." On an Android phone, tap "Display," then tap "Font size."
3. Slide the bar to the right. The words get bigger as you slide.
4. Look at the sample words on the screen. Stop when they are easy to read.
5. Press the back button or go back to your home screen. Your choice is saved.

If you do not see these names, look for a search bar at the top of Settings. Type the word "text" or "font."

You can ask at the desk for help.
```

Observation: One conversation, captured with `tools/capture_conversation.sh` (session 28d356df-46d6-4165-ba76-5f0b91526d10), because the lesson is whether instructions set in turn 1 still hold in later turns. Both later answers use short sentences and five numbered steps, and both end by sending the patron to the desk. Response 2 names a phone brand in step 2; the chapter trims that line with `[...]` so the prose names no vendor. Response 3 also names phone brands and is not shown.

## Prompt 14 (Section 4.3 worked example: zero-shot (the version used))

```text
Write a text message to a landscaping customer saying today's visit is done. Facts: the customer's name is Dana. We mowed and edged the front and back yards and trimmed the hedges. The drip line by the back fence is leaking.
```

Response:

```text
Hi Dana, today's visit is done. We mowed and edged the front and back yards and trimmed the hedges. One thing to flag: the drip line by the back fence is leaking. Want us to take a look at it on our next visit? Thanks!
```

Observation: Same request as Prompt 11 with the facts written as sentences instead of a semicolon list. 45 words by wc -w, one paragraph. Every fact traces to the prompt. It adds an offer the prompt did not include ("Want us to take a look at it on our next visit?") and a "Thanks!" sign-off. It uses "We" and full sentences, where the owner's examples in Prompt 12 use clipped phrases.

## Verification notes

* Further Reading, checked 2026-10-21 with `curl -sI -o /dev/null -w "%{http_code}" -A 'Mozilla/5.0' -L URL`: https://arxiv.org/abs/2005.14165 (200), https://arxiv.org/abs/2202.12837 (200), https://arxiv.org/abs/2203.02155 (200), https://arxiv.org/abs/2406.06608 (200), https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/ (200).
* Descriptions checked against each page's abstract on 2026-10-21. Brown and others (2020): GPT-3, tasks and few-shot demonstrations "specified purely via text interaction with the model," without fine-tuning. Min and others (2022): "randomly replacing labels in the demonstrations barely hurts performance"; the label space, the input text, and the overall format drive results. Ouyang and others (2022): fine-tuning on labeler demonstrations and rankings (RLHF) made models better at following a user's intent. Schulhoff and others (2024): "a detailed vocabulary of 33 vocabulary terms, a taxonomy of 58 LLM prompting techniques." MIT Sloan Teaching and Learning Technologies page title "Effective Prompts for AI: The Essentials"; it recommends providing context, being specific, and building on the conversation.
* Tool check in Section 4.3, checked 2026-10-21: https://support.google.com/gemini/answer/15637730 returned 200 with the page title "Get personalization in Gemini Apps" (a roster tool with a personalization feature). https://help.openai.com/en/articles/8096356-custom-instructions-for-chatgpt returned 403 to curl (a bot block, not proof the page is missing). The callout therefore names feature types generically ("custom instructions or personalization") and makes no claim about which roster tools have them.
* Brown and others (2020), Figure 2.1: the chapter's Further Reading line says the figure shows zero-shot, one-shot, and few-shot prompts side by side. Checked 2026-10-21 in the PDF (https://arxiv.org/pdf/2005.14165, pdftotext pages 5-9): Section 2 defines few-shot, one-shot, and zero-shot "(see Figure 2.1 for an illustration)", and the text states "Figure 2.1 shows the four methods using the example of translating English to French" (fine-tuning plus the three prompt settings).
* No response in this log contains a URL, a citation, or a statistic that the chapter repeats as fact.
