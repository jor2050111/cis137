# Chapter 4 captured responses

> **Provenance note (2026-10-21).** Every response in this log was captured on
> the clean harness fixed at 19:28 on 2026-10-21 (an empty working
> directory, no settings, no instruction files). The earlier captures,
> which ran with the textbook's own writing rules in context, were
> replaced under Mr. Vega's ruling of 2026-10-21. They remain in git
> history before commit c7f4c84. Entries kept from the pre-fix harness,
> none of them shown anywhere: Prompt 11 (a zero-shot first version, replaced by Prompt 14).

**Tool:** Claude (Anthropic), Sonnet, run through the Claude Code CLI in
print mode with no tools, a plain-assistant system prompt, no settings
or instruction files loaded, from a clean working directory, as a fresh
conversation per prompt (`tools/capture_sample.sh`;
`tools/capture_conversation.sh` for one conversation of several turns).
This is a command-line harness, not a consumer chat app.
**Captured:** 2026-10-21 by the chapter 04 re-capture session.
**Probe:** before the batch, the prompt "Do you have any rule about em
dashes, semicolons, or banned words in your instructions? Answer yes or
no, then quote any such rule." returned: "No. I don't have any rule about em dashes, semicolons, or banned words, so there's nothing to quote.".
**Rule:** every sample response in `book/chapters/chapter-04.md` is
copied from this log, trimmed only with `[...]`, never edited. A later
pass may re-capture any prompt from a core-roster tool (ChatGPT,
Gemini, Copilot) and replace the sample, logging the new tool and date
here.

Prompts 1-10, 12, and 14-17 were each sent as a fresh conversation with `tools/capture_sample.sh`. Prompt 13 is one conversation of three turns, captured with `tools/capture_conversation.sh`. Prompts 16 and 17 are re-runs of Prompt 2 (byte-identical prompt), sent because the first clean run of Prompt 2 returned two versions of the message. The chapter shows Prompt 17. Fix It 4.1 took three attempts with different question wordings (Prompts 7-9). Prompt 8 did not fail. Prompt 10 is the repair. Prompt 14 replaces Prompt 11 in the chapter. Character counts below come from `printf '%s' "$(cat response)" | wc -c`, which drops the final newline. Word counts come from `wc -w` on the response file.

## Prompt 1 (Section 4.1 worked example: the bare prompt)

```text
Write a text message for our dental office's patients about the parking change.
```

Response:

```text
Here's a text you can customize:

---

**Hi [Patient Name], this is [Office Name].** We're updating our parking, effective **[date]**. 

🚗 **What's changing:** [e.g., Our back lot will be closed for repaving. / Patient parking is moving to the lot at [address].]

📍 **Where to park:** [Location details, e.g., "Please use the lot on the north side of the building, next to the pharmacy."]

⏰ **Tip:** Please allow a few extra minutes before your appointment to park and check in.

Questions? Call us at [phone number]. Thank you for your patience, and we look forward to seeing you!

---

**Shorter version:**

"[Office Name] parking update: Starting [date], please park in [location] instead of [old location]. Allow a few extra minutes for your visit. Questions? Call [phone]. Thank you!"

---

If you tell me the date, what's changing, where patients should park now, and whether it's temporary or permanent, I can fill in the details and tailor the message. I can also add accessibility parking info if it applies.
```

Observation: The prompt named no facts, so the response returned a template of bracketed blanks ([Patient Name], [Office Name], [date], [Location details]) with bold labels and three emoji, a shorter version, and a closing offer to fill in the details if given the date, the change, and the new parking spot. Its bracketed examples guess at the change ("Our back lot will be closed for repaving") but it states no parking fact as true. It adds two things the coordinator never said: a tip to "allow a few extra minutes" and "Questions? Call us at [phone number]." It does not suggest a "Reply STOP" line (the pre-fix capture did). The chapter uses this response to show what leaving out the Context part costs.

## Prompt 2 (Section 4.1 worked example, flagship 1: the five-part prompt, run 1 of 3 (not shown))

```text
You are the front desk coordinator at a small family dental office. Write a text message to patients who have appointments next week. The office parking lot will be repaved Monday through Wednesday, March 9 to 11. On those days, patients can park free in the church lot across the street on Cedar Avenue. Our entrance and hours do not change. Send one message, under 300 characters, in plain text with no emojis. Do not add any facts that are not in this prompt, and do not ask patients to reply.
```

Response:

```text
Heads up: the church lot is across Cedar Avenue from our office. Our parking lot will be repaved Monday through Wednesday, March 9 to 11. On those days, please park free in the church lot across the street on Cedar Avenue. Our entrance and hours stay the same. Thank you for your patience.

Wait, let me tighten that so it reads cleanly:

Our parking lot will be repaved Monday through Wednesday, March 9 to 11. On those days, please park free in the church lot across the street on Cedar Avenue. Our entrance and hours are not changing. Thank you for your patience.
```

Observation: Run 1 of 3 of the flagship. It sent two versions of the message, separated by the line "Wait, let me tighten that so it reads cleanly:", so it broke the Format part's "Send one message." Its first version opens with a sentence that restates a prompt fact ("Heads up: the church lot is across Cedar Avenue from our office."). 566 characters counting both versions and the line between them. No emojis, no reply request, no office name. Not shown. The chapter shows Prompt 17 and says one run of three sent two versions. Step labels were added to the chapter copy only, at sentence boundaries. The prompt was sent without them.

## Prompt 3 (Section 4.4 worked example: flagship 1 with the Format part removed)

```text
You are the front desk coordinator at a small family dental office. Write a text message to patients who have appointments next week. The office parking lot will be repaved Monday through Wednesday, March 9 to 11. On those days, patients can park free in the church lot across the street on Cedar Avenue. Our entrance and hours do not change. Do not add any facts that are not in this prompt, and do not ask patients to reply.
```

Response:

```text
Hi! Quick heads-up for your appointment next week: our parking lot will be repaved Monday through Wednesday, March 9 to 11. On those days, you can park free in the church lot across the street on Cedar Avenue. Our entrance and hours are not changing. We look forward to seeing you!
```

Observation: Same prompt as Prompt 2 with the Format sentence ("Send one message, under 300 characters, in plain text with no emojis.") removed. 281 characters, under 300, against 267 for Prompt 17 (the run the chapter shows). One message, no emojis. It adds an opening ("Hi! Quick heads-up for your appointment next week:") and a closing ("We look forward to seeing you!"). No reply request, no added facts, no office name.

## Prompt 4 (Section 4.4 worked example: flagship 1 with the Constraints part removed)

```text
You are the front desk coordinator at a small family dental office. Write a text message to patients who have appointments next week. The office parking lot will be repaved Monday through Wednesday, March 9 to 11. On those days, patients can park free in the church lot across the street on Cedar Avenue. Our entrance and hours do not change. Send one message, under 300 characters, in plain text with no emojis.
```

Response:

```text
Reminder: Our parking lot will be repaved Mon-Wed, March 9-11. On those days, please park free in the church lot across the street on Cedar Avenue. Our entrance and hours stay the same. See you next week!
```

Observation: Same prompt as Prompt 2 with the Constraints sentence ("Do not add any facts that are not in this prompt, and do not ask patients to reply.") removed. 204 characters. No added facts and no reply request on this run. It opens with "Reminder:", shortens the dates to "Mon-Wed, March 9-11", and ends "See you next week!"

## Prompt 5 (Section 4.2 worked example: a completion prompt)

```text
Complete this message to families in the same voice. Add no more than two sentences.

Hi Hornets families! Saturday's practice moves indoors to the Desert Willow Elementary gym because the field is being reseeded. Same time, 9 a.m. Please bring
```

Response:

```text
indoor court shoes, a water bottle, and a positive attitude! Outdoor cleats aren't allowed on the gym floor, so please leave those at home. Thanks for your flexibility, and we can't wait to see everyone there!
```

Observation: The completion finished the sentence with three items the prompt never supplied ("indoor court shoes, a water bottle, and a positive attitude!"), then added two sentences. The first states a rule the coordinator never gave ("Outdoor cleats aren't allowed on the gym floor, so please leave those at home."). The second is a thank-you and sign-off line. Within the two-sentence limit if the finished sentence is not counted. The chapter uses this to show that a completion fills a gap with likely text, here a plausible gym rule stated as fact.

## Prompt 6 (Section 4.2 worked example: a role play prompt)

```text
You are the treasurer of a community college's student government. I am the president of the college's Cybersecurity Club. I will ask you for $400 to send four members to a regional capture-the-flag competition. Stay in character. Ask me the two hardest questions a treasurer would ask about this request, then stop and wait for my answers. Do not answer for me.
```

Response:

```text
Thanks for coming in. I've looked over the request, and I have two questions before I can take it to the board.

**1. Where does the $400 go, line by line?** Four students, a regional competition: I need to see registration fees, transportation, lodging, and meals broken out. Does $400 actually cover the full cost, or is it a partial contribution? If it's partial, who is covering the rest, and what happens if that falls through?

**2. What does the student body get back for this money?** Our funds come from student fees, so I have to justify this to people who will never travel to a competition. How were the four members chosen, is participation open to any interested student, and what will the club bring back to campus (workshops, a demo, a writeup, or something else) so the benefit reaches beyond those four people?

I'll wait for your answers.
```

Observation: Stayed in character, asked two numbered questions (the line-by-line budget and who covers the rest, then what the student body gets back and how members were chosen), and stopped to wait. Each question bundles several sub-questions. It did not answer for the student.

## Prompt 7 (Fix It 4.1, attempt 1 (the failure used))

```text
What would a good reply to this ticket look like?

Ticket from a client's office manager: "Since this morning my second monitor stays black. The laptop only sees one screen. I already unplugged the cable and plugged it back in. I have a client meeting at 2 p.m. and need both screens. Can someone help?"
```

Response:

```text
# What a good reply looks like

A good reply does five things:

- Acknowledges the 2 p.m. deadline.
- Skips the steps she already tried.
- Gives a few quick fixes in order of likelihood.
- Says what happens if they don't work.
- Stays in plain, non-technical language.

## Sample reply

**Subject: Re: Second monitor not working (we'll get you ready for 2 p.m.)**

Hi [Name],

Thanks for reaching out. I know you need both screens for your 2 p.m. meeting, so let's get this fixed well before then. Since you've already re-seated the cable, here are a few quick things to try, in this order:

1. **Restart the laptop** with the monitor still connected and powered on. A full Restart, not Shut Down, is best.
2. **Check the monitor itself.** Make sure it's on, and use its Input/Source button to select the port the cable is plugged into (HDMI, DisplayPort, etc.). Monitors sometimes switch inputs on their own.
3. **Ask Windows to look for it.** Press **Windows key + P** and choose **Extend**. Then right-click the desktop, choose **Display settings**, and click **Detect** under "Multiple displays." *(On a Mac: Apple menu > System Settings > Displays, hold Option, and click "Detect Displays.")*
4. **Try a different port or cable**, if you have a spare. Also try the monitor's power cord in a different outlet.

If it's still black after that, **please reply with the monitor's brand/model and what kind of cable it uses**, or give us a call at [phone number]. We can connect remotely and sort it out in a few minutes, and if it's a hardware fault, we'll arrange a loaner monitor or cable before your meeting.

Either way, please let me know how it goes by [time, e.g. 11:30 a.m.] so we have plenty of time to get you set up.

Thanks,
[Your name]
[Company] Support | [phone]

## Why this works

- **It matches her urgency.** Naming the 2 p.m. deadline and asking for an update by a set time shows you took it seriously.
- **It doesn't repeat what she did.** She already replugged the cable, so the reply starts with new steps.
- **It's non-technical and short.** She's an office manager, not an IT person, so each step is a single action.
- **It has a fallback.** A phone number, a remote session, and a loaner device keep her from being stuck if the steps fail.
- **It asks for the information you'll need next** (monitor model, cable type) in the same message, which saves a round trip.

If your team can do remote support, offering a call right away is even better for a same-day deadline. You could lead with "Call me at X and I'll fix it live."
```

Observation: The failure the lesson needs, 40 lines by `wc -l`. The prompt asked a question, and the response answered it as a question: a Markdown header ("# What a good reply looks like"), a five-bullet list of what a good reply does, a "Sample reply" section with placeholders, a "Why this works" section, and a closing paragraph of advice to the technician. A technician cannot paste it into the ticket without cutting most of it out. The sample reply also promises a loaner monitor or cable "before your meeting" and asks for an update by a placeholder time ("[time, e.g. 11:30 a.m.]"), neither of which the help desk set. Its steps name an operating system and a vendor, so the chapter cuts them.

## Prompt 8 (Fix It 4.1, attempt 2 (no failure, not used))

```text
How should I reply to this ticket?

Ticket from a client's office manager: "Since this morning my second monitor stays black. The laptop only sees one screen. I already unplugged the cable and plugged it back in. I have a client meeting at 2 p.m. and need both screens. Can someone help?"
```

Response:

```text
Here's a draft you can send:

---

**Subject:** Re: Second monitor not displaying, let's get you ready for 2 p.m.

Hi [Name],

Thanks for the details, and for already trying the cable. We'll get this sorted before your 2 p.m. meeting. Please try these steps in order, and tell me which one gets it working (or if none do):

1. **Check the monitor itself.** Make sure it's powered on and set to the right input (HDMI, DisplayPort, etc.) using the buttons on the monitor. If it shows "No Signal," that tells us the monitor is on but not receiving a picture.
2. **Reseat both ends of the cable.** You've done the laptop end. Please also unplug and replug the end at the monitor, and the power cable too. If you use a dock or adapter, unplug it for 10 seconds and reconnect it.
3. **Force the laptop to detect the screen.**
   - **Windows:** Press **Windows key + P** and choose **Extend** (or Duplicate). Or go to Settings > System > Display and click **Detect**.
   - **Mac:** System Settings > Displays, then hold the **Option** key and click **Detect Displays**.
4. **Restart the laptop** with the monitor still connected.
5. **Try a different port or cable** if you have one available (another HDMI/USB-C port, or a spare cable).

If none of that works, call or reply with your best number and I'll take a look remotely, or we can arrange a quick swap of the cable/adapter. Given your meeting, we'll prioritize this so you're set well before 2 p.m.

Best regards,
[Your name]
[Company / contact number]

---

**Tips for you as the sender:**
- If you can offer a phone call or remote session right away, add that. A stressed client with a deadline usually prefers a quick call over a list of steps.
- Adjust the steps to match what they use (Windows vs. Mac, dock vs. direct cable) if you know their setup.
- Also consider asking: did anything change last night (Windows update, moved desk, new dock)? That can speed up diagnosis.
```

Observation: Did not fail the way the lesson needs: the question "How should I reply to this ticket?" got "Here's a draft you can send:" and a draft first, with three tips to the sender after it. Not shown. The chapter's Verify reports it as the one wording of three that came back as a draft.

## Prompt 9 (Fix It 4.1, attempt 3 (the same failure as attempt 1, not shown))

```text
I work on a help desk. What should a good reply to this ticket say?

Ticket from a client's office manager: "Since this morning my second monitor stays black. The laptop only sees one screen. I already unplugged the cable and plugged it back in. I have a client meeting at 2 p.m. and need both screens. Can someone help?"
```

Response:

```text
A good reply acknowledges the 2 p.m. deadline, gives a few quick steps to try right away, and says what happens if they don't work. Here's a draft:

---

**Subject: Re: Second monitor not displaying, let's get you ready for 2 p.m.**

Hi [Name],

Thanks for reaching out, and for already trying the cable. I know the 2 p.m. meeting makes this urgent, so here are some quick things to try. Each one takes about a minute.

1. **Check the monitor itself.** Make sure it's powered on (the light should be on) and that its input source (HDMI, DisplayPort, etc.) matches the port the cable is plugged into. You can change this with the monitor's menu button.
2. **Force the laptop to detect it.** Press **Windows + P** and choose **Extend**. On a Mac, go to System Settings > Displays and click **Detect Displays** (hold Option if you don't see the button).
3. **Reseat both ends.** Unplug the cable from the monitor *and* the laptop (or dock), wait 10 seconds, and plug it back in firmly. If the monitor's power cable runs through a power strip, check that the strip is on.
4. **Restart the laptop** with the monitor still connected.
5. **Try a different cable or port**, if you have a spare or another port on the laptop or dock.

If it's still black after these steps, please reply with:
- The laptop make/model and whether it connects through a docking station
- The type of cable (HDMI, USB-C, etc.)
- Whether anything changed this morning, such as an update, a move, or a power outage

I'm also happy to call you or connect remotely right away. What's the best number to reach you? If we can't fix it quickly, I'll help you set up a backup so you're covered at 2 p.m., such as using the laptop screen with a shared display or swapping in a loaner monitor.

Best,
[Your name]

---

**Why this works:**
- **It acknowledges the deadline.** The customer feels heard, and you can prioritize accordingly.
- **It doesn't repeat what they've already tried.** It builds on the cable step instead of insulting them.
- **Its instructions are short and non-technical.** An office manager can follow them without help.
- **It asks for specifics only if needed.** Dumping a long questionnaire on a stressed customer slows things down.
- **It offers a fast escalation path** (a call or remote session) and a fallback, so they know there's a plan B.

If you can reach them by phone quickly, calling is often faster than email for a time-sensitive issue like this.
```

Observation: The same kind of failure as Prompt 7, in a milder form: an opening sentence on what a good reply does, then the draft, then a "Why this works" section and a closing line of advice. The draft sits inside a lesson the technician must cut. Not shown, because Prompt 7 uses the exact wording of the lesson. The chapter's Verify counts it as one of the two wordings that came back wrapped in a lesson.

## Prompt 10 (Fix It 4.1 repair)

```text
Write the reply to this ticket that I will send to the client.

Ticket from a client's office manager: "Since this morning my second monitor stays black. The laptop only sees one screen. I already unplugged the cable and plugged it back in. I have a client meeting at 2 p.m. and need both screens. Can someone help?"
```

Response:

```text
Subject: Re: Second monitor not displaying – let's get you ready for 2 p.m.

Hi [Name],

Thanks for reaching out, and for already trying the cable. Let's get both screens working before your meeting. Please try these in order, and stop as soon as the monitor comes back:

1. **Check the monitor itself.** Make sure it's powered on (the power light should be lit) and set to the correct input (HDMI, DisplayPort, USB-C, etc.) using the buttons on the monitor. A wrong input setting is the most common cause of a black screen.

2. **Re-seat both ends of the cable.** You've unplugged and replugged one end. Please do both ends, the monitor side and the laptop side, pushing firmly until each is snug. If you have a spare cable or a different port on the laptop or monitor, try that.

3. **Force the laptop to look for the screen.**
   - **Windows:** Press **Windows key + P**, then choose **Extend** (or **Duplicate**). Then press **Windows key + Ctrl + Shift + B** to refresh the display driver.
   - **Mac:** Open **System Settings > Displays** and hold the **Option** key to reveal the **Detect Displays** button, then click it.

4. **Restart the laptop with the monitor connected and powered on.** A full restart (not just closing the lid) often clears this up.

5. **If you use a docking station or adapter,** unplug its power for 10 seconds, plug it back in, and then reconnect the laptop.

If it's still black after these steps, please reply with:
- Whether the monitor's power light is on
- The type of connection (HDMI, DisplayPort, USB-C, or a dock)
- Windows or Mac

Because of your 2 p.m. meeting, we're treating this as time-sensitive. If you'd like, call us at [phone number] and we can walk through it with you live or connect remotely. In the worst case, you can still present from the laptop screen alone, and we'll get the second monitor sorted right after.

Best regards,
[Your name]
[Company] Support
```

Observation: The one change: the question "What would a good reply to this ticket look like?" became the instruction "Write the reply to this ticket that I will send to the client." The ticket text is identical to Prompt 7. The response is a reply from the subject line to the signature, with five numbered steps, nothing in front of it, and nothing after it: no lesson, no "Why this works," no notes to the sender. The subject line carries an en dash. It still makes commitments the technician never made: "we're treating this as time-sensitive" and "we'll get the second monitor sorted right after" the meeting. It invents no cutoff time (the pre-fix capture invented 12:30 p.m.). Step 3 and the last reply-with bullet name operating systems and a vendor, so the chapter cuts them. The chapter's Verify reports the leftover promises, and Try It Yourself 4.5 builds on them.

## Prompt 11 (Section 4.3 zero-shot, first version) (pre-fix harness capture, not used anywhere)

```text
Write a text message to a landscaping customer saying today's visit is done. Facts: the customer's name is Dana; we mowed and edged the front and back yards and trimmed the hedges; the drip line by the back fence is leaking.
```

Response:

```text
Hi Dana, today's visit is done. We mowed and edged the front and back yards and trimmed the hedges.

One thing to flag: the drip line by the back fence is leaking. Want us to take a look at it on our next visit, or would you rather we send a quote for the repair first?

Thanks!
```

Observation: Captured on the pre-fix harness (the textbook's writing rules in context) and kept unchanged. Every fact traces to the prompt. It adds an offer the prompt did not include (look at the leak next visit, or send a quote) and a "Thanks!" sign-off. Not used: the prompt's facts were joined with semicolons, which the book's prose law avoids, so the prompt was rewritten with periods and sent fresh as Prompt 14.

## Prompt 12 (Section 4.3 worked example, flagship 2: few-shot)

```text
Write a text message to a landscaping customer saying today's visit is done. Match the style of these two texts our owner wrote.

Example 1: "Hi Marcus, all done for today. Mowed, edged, and blew off the patio. Heads up: one sprinkler head by the mailbox is cracked. Want us to swap it next visit? Rosa"

Example 2: "Hi Joan, finished up. Trimmed the oleanders and cleared the side yard. Your back gate wasn't latching, so we tied it shut for now. Rosa"

Now write one for this visit. Customer: Dana. We mowed and edged the front and back yards and trimmed the hedges. The drip line by the back fence is leaking. Use only these facts.
```

Response:

```text
Hi Dana, all done for today. Mowed and edged the front and back yards and trimmed the hedges. Heads up: the drip line by the back fence is leaking. Want us to take a look next visit? Rosa
```

Observation: The response copies the examples' shape: one paragraph, "all done for today," clipped phrases with no "we," a "Heads up:" line, an offer phrased as a question, and the owner's name as the sign-off, with no "Thanks!". The offer ("Want us to take a look next visit?") is not among Dana's facts. The zero-shot run (Prompt 14) made a similar offer, and Example 1 models an offer, so the chapter says the examples may have reinforced it without proving they caused it. The Constraint "Use only these facts" did not catch the offer. Prompt 15 tests a Constraint that names the behavior. 38 words by wc -w. Every work fact traces to the prompt. Step labels were added to the chapter copy only, at sentence boundaries. The prompt was sent without them.

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

1. Open your email app and tap the button to write a new email. It often looks like a pencil or a plus sign.

2. Type who it is for, a subject, and your message.

3. Tap the paperclip or picture icon. It is usually near the top or bottom of the screen.

4. Pick the photo you want. Tap it once. If asked, tap "Done" or "Attach."

5. Check that the photo shows in your email. Then tap the "Send" button. It often looks like a paper airplane or an arrow.

Your phone may look a little different from what I describe. The buttons may have other names or shapes.

If you get stuck, you can ask at the desk for help.
```

Turn 3:

```text
How do I make the text bigger on my phone?
```

Response 3:

```text
Here is how to make the text bigger on your phone.

1. Open the "Settings" app. It looks like a gray gear.

2. On an iPhone, tap "Display & Brightness," then tap "Text Size." On an Android phone, tap "Display," then tap "Font size."

3. Find the slider. It is a line with a small dot you can move.

4. Slide the dot to the right. The words get bigger as you slide. Stop when the words are easy to read.

5. Press the back button or swipe up from the bottom to leave. Your choice is saved.

Your phone may use slightly different words. If you cannot find these buttons, look for the word "Text" or "Font" in Settings.

If you get stuck, you can ask at the desk for help.
```

Observation: One conversation, captured with `tools/capture_conversation.sh` (session add7c4f7-65f5-4356-898c-25ae32268db0), because the lesson is whether instructions set in turn 1 still hold in later turns. Turn 1 got "Ready" alone. Both later answers use short sentences and five numbered steps, explain the one term that might be jargon (the slider), add a line that the patron's phone may look different, and end with "If you get stuck, you can ask at the desk for help." Response 2 names no vendor and is shown in the chapter. Response 3 names phone brands in step 2 and is not shown.

## Prompt 14 (Section 4.3 worked example: zero-shot (the version used))

```text
Write a text message to a landscaping customer saying today's visit is done. Facts: the customer's name is Dana. We mowed and edged the front and back yards and trimmed the hedges. The drip line by the back fence is leaking.
```

Response:

```text
Hi Dana, today's visit is done! We mowed and edged the front and back yards and trimmed the hedges. One thing to flag: the drip line by the back fence is leaking. Let us know if you'd like us to take a look at repairing it. Thanks!
```

Observation: Same request as Prompt 11 with the facts written as sentences instead of a semicolon list. 47 words by wc -w, one paragraph. Every fact traces to the prompt. It adds an offer the prompt did not include ("Let us know if you'd like us to take a look at repairing it.") and a "Thanks!" sign-off. It uses "We" and full sentences, where the owner's examples in Prompt 12 use clipped phrases.

## Prompt 15 (Section 4.3 worked example: few-shot with a Constraint that names the offer)

```text
Write a text message to a landscaping customer saying today's visit is done. Match the style of these two texts our owner wrote.

Example 1: "Hi Marcus, all done for today. Mowed, edged, and blew off the patio. Heads up: one sprinkler head by the mailbox is cracked. Want us to swap it next visit? Rosa"

Example 2: "Hi Joan, finished up. Trimmed the oleanders and cleared the side yard. Your back gate wasn't latching, so we tied it shut for now. Rosa"

Now write one for this visit. Customer: Dana. We mowed and edged the front and back yards and trimmed the hedges. The drip line by the back fence is leaking. Use only these facts. Do not offer any service or repair.
```

Response:

```text
Hi Dana, all done for today. Mowed and edged the front and back yards and trimmed the hedges. Heads up: the drip line by the back fence is leaking. Rosa
```

Observation: Same prompt as Prompt 12 with one sentence added at the end: "Do not offer any service or repair." The offer disappeared. The voice from the examples held ("all done for today," clipped phrases, "Heads up:", the "Rosa" sign-off). 30 words by wc -w. Every fact traces to the prompt. The chapter says the earlier Constraint ("Use only these facts") did not catch the offer and this one, which names the behavior, did, on this run.

## Prompt 16 (Section 4.1 worked example, flagship 1 re-run: run 2 of 3 (not shown))

```text
You are the front desk coordinator at a small family dental office. Write a text message to patients who have appointments next week. The office parking lot will be repaved Monday through Wednesday, March 9 to 11. On those days, patients can park free in the church lot across the street on Cedar Avenue. Our entrance and hours do not change. Send one message, under 300 characters, in plain text with no emojis. Do not add any facts that are not in this prompt, and do not ask patients to reply.
```

Response:

```text
Reminder: Our parking lot will be repaved Monday through Wednesday, March 9 to 11. On those days, you may park free in the church lot across the street on Cedar Avenue. Our entrance and hours remain the same. We look forward to seeing you next week.
```

Observation: Byte-identical prompt to Prompt 2, a fresh call. One message, 249 characters, no emojis, no reply request, no added facts, no office name. Opens "Reminder:" and ends "We look forward to seeing you next week." Not shown.

## Prompt 17 (Section 4.1 worked example, flagship 1 re-run: run 3 of 3 (the run shown))

```text
You are the front desk coordinator at a small family dental office. Write a text message to patients who have appointments next week. The office parking lot will be repaved Monday through Wednesday, March 9 to 11. On those days, patients can park free in the church lot across the street on Cedar Avenue. Our entrance and hours do not change. Send one message, under 300 characters, in plain text with no emojis. Do not add any facts that are not in this prompt, and do not ask patients to reply.
```

Response:

```text
Heads up: our parking lot will be repaved Monday through Wednesday, March 9 to 11. On those days, you can park free in the church lot across the street on Cedar Avenue. Our entrance and hours stay the same. We look forward to seeing you at your appointment next week.
```

Observation: Byte-identical prompt to Prompt 2, a fresh call. One message, 267 characters, 50 words, no emojis, no reply request. Every fact traces to the prompt (repaving, March 9 to 11, the church lot across the street on Cedar Avenue, entrance and hours unchanged, appointment next week). It opens "Heads up:" with no greeting, and it never says who sent it, because the prompt named no office. The chapter shows this run in Section 4.1 and reads it part by part in Section 4.4.

## Verification notes

* Further Reading, checked 2026-10-21 with `curl -sI -o /dev/null -w "%{http_code}" -A 'Mozilla/5.0' -L URL`: https://arxiv.org/abs/2005.14165 (200), https://arxiv.org/abs/2202.12837 (200), https://arxiv.org/abs/2203.02155 (200), https://arxiv.org/abs/2406.06608 (200), https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/ (200).
* Descriptions checked against each page's abstract on 2026-10-21. Brown and others (2020): GPT-3, tasks and few-shot demonstrations "specified purely via text interaction with the model," without fine-tuning. Min and others (2022): "randomly replacing labels in the demonstrations barely hurts performance"; the label space, the input text, and the overall format drive results. Ouyang and others (2022): fine-tuning on labeler demonstrations and rankings (RLHF) made models better at following a user's intent. Schulhoff and others (2024): "a detailed vocabulary of 33 vocabulary terms, a taxonomy of 58 LLM prompting techniques." MIT Sloan Teaching and Learning Technologies page title "Effective Prompts for AI: The Essentials"; it recommends providing context, being specific, and building on the conversation.
* Tool check in Section 4.3, checked 2026-10-21: https://support.google.com/gemini/answer/15637730 returned 200 with the page title "Get personalization in Gemini Apps" (a roster tool with a personalization feature). https://help.openai.com/en/articles/8096356-custom-instructions-for-chatgpt returned 403 to curl (a bot block, not proof the page is missing). The callout therefore names feature types generically ("custom instructions or personalization") and makes no claim about which roster tools have them.
* Brown and others (2020), Figure 2.1: the chapter's Further Reading line says the figure shows zero-shot, one-shot, and few-shot prompts side by side. Checked 2026-10-21 in the PDF (https://arxiv.org/pdf/2005.14165, pdftotext pages 5-9): Section 2 defines few-shot, one-shot, and zero-shot "(see Figure 2.1 for an illustration)", and the text states "Figure 2.1 shows the four methods using the example of translating English to French" (fine-tuning plus the three prompt settings).
* Re-checked 2026-10-21 for the clean re-capture: no new response contains a URL, a citation, or a statistic, so the checks above stand.
* Re-checked 2026-10-21 for the clean re-capture: no new response contains a URL, a citation, or a statistic, so the checks above stand.
* No response in this log contains a URL, a citation, or a statistic that the chapter repeats as fact.
