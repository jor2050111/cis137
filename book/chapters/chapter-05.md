# Chapter 5: Strategies That Make Prompts Work

A two-person landscaping crew in Mesa asks a chat assistant for a fall post and gets a list of services the crew may not offer. A dental office asks one to answer a patient's text and gets a cheerful yes that nobody at the office approved. Neither prompt had a typo. Each one left the model to guess, and a model that guesses writes the likely thing, not the true one.

Chapter 4 named the five parts of a prompt: Role, Task, Context, Format, and Constraints. This chapter gives you nine named strategies that fill those parts with more care. It also gives you two checklists that tell you whether a strategy worked. You will see each strategy in a captured run, often as a before-and-after pair. Then you will score the results with a checklist instead of a hunch. That is how you evaluate artificial intelligence (AI) output on a deadline, and it is how you prove that a change helped.

Copperwind IT Services needs both skills now. Mei Lin has three weak marketing prompts that keep producing copy she cannot publish, and the Deskside team's prompt library needs its next version. Skills Lab 5A hands you both jobs. You will leave with the Prompt Strategy Checklist, the Output Checklist, a Prompt Repair sheet, and library v2.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** Chapters 1 through 4
* **Deliverables:** Skills Lab 5A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **5.1 (Apply):** Apply named strategies from the Prompt Strategy Checklist to raise the quality of a prompt's output, and record them in the prompt card's Strategies used field (Sections 5.1-5.3)
* **5.2 (Analyze):** Examine a weak prompt with the Prompt Strategy Checklist to find the missing strategy behind its worst failure, and repair it one change at a time (Section 5.4)
* **5.3 (Evaluate):** Judge an output against the Output Checklist, and attribute the difference between two runs to the strategy that caused it (Sections 5.3-5.4)

### This chapter aligns with the following Course Learning Outcomes

* **CLO 3 (Apply):** Demonstrate effective prompting strategies to improve AI outputs.
* **CLO 1 (Evaluate):** Evaluate AI-generated responses for accuracy.

---

## 5.1 Specificity, Context, and Examples

A **strategy** is a named move you add to a prompt to raise the quality of what comes back. Each one has a test you can run on the prompt before you send it. Tips like "be clear" are not strategies, because you cannot check a prompt against them. "Does the prompt supply every fact the output needs?" is a test you can check.

This chapter uses nine strategies, and together they make the **Prompt Strategy Checklist**. Each strategy strengthens one of the five parts of a prompt from Chapter 4. The packet file `prompt-strategy-checklist.md` holds the same table with a blank column for your own examples.

| # | Strategy | The test you run on your prompt | The part it strengthens |
| --- | --- | --- | --- |
| 1 | Specificity and context | Does it supply every fact, name, and number the output needs? | Context |
| 2 | Examples (few-shot) | If the output must match a house style, does it show one to three samples? | Format |
| 3 | Output structure | Does it name the shape the next step needs: table, list, template, or length? | Format |
| 4 | Step-by-step reasoning request | If the job applies rules, does it ask for each check on its own line before the answer? | Task |
| 5 | Decomposition | If the job has stages, does each stage get its own prompt and its own check? | Task |
| 6 | Persona and audience framing | Does it say whose voice to use and who will read the result? | Role, Context |
| 7 | Grounding (supply the source, answer only from it) | Does it hand over the source, limit the answer to it, and say what to do when the source is silent? | Context, Constraints |
| 8 | Clarifying questions first | If you are unsure what you need, does it ask the model to ask before it writes? | Task |
| 9 | Negative constraints and guardrails | Does it forbid the additions you cannot accept, such as prices, promises, or advice? | Constraints |

You will not use all nine on every prompt. A two-line reminder text needs none of the reasoning strategies. The checklist is a diagnosis tool. You run down it, mark what the prompt uses and what it lacks, and add only what the job needs.

### Specificity and Context

The first strategy carries the most weight: the more the model knows, the less it invents. Chapter 2 explained why. A model fills every gap with likely text, and likely is not the same as true. Here is the landscaping crew's first prompt:

```text
Write a social media post for our landscaping company about our fall services.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
**Fall Services Post**

Fall is the best time to set your lawn up for spring. Here's what we're booking now:

* Leaf cleanup and removal
* Aeration and overseeding
* Fall fertilizer for strong roots
* Gutter and bed cleanout
* Pruning, trimming, and mulching
* Bulb planting for spring color
[...]
Our fall schedule fills fast. Call [phone], visit [website], or message us to get a free quote.
[...]
I didn't have your company name, location, or any offers, so those are placeholders. If you tell me about a seasonal discount, your service area, or your brand voice (friendly, professional, funny), I can tailor the post.
```

The tool was honest about its placeholders, which helps. It still wrote a list of six services from the typical fall menu, plus a free quote. The crew never said it offers any of them. Every item is a claim a homeowner would believe. Now the same job with the strategy applied. Send the prompt without the [Step] lines. They show the decision behind each part.

```text
[Step 1: say who is asking and who will read it]
I run a small landscaping company in Mesa, Arizona. The post is for our neighborhood social media page, which is read mostly by homeowners who already know us.
[Step 2: name the job and its size]
Write a social media post of 60 to 80 words announcing our fall services.
[Step 3: hand over every fact the model would otherwise invent]
Facts: (1) fall overseeding with winter rye for Bermuda lawns, booking now for October 15 through November 15, (2) irrigation timer resets for cooler weather, (3) we are a two-person crew, so book early, (4) call or text 480-555-0186 to book.
[Step 4: forbid what you did not supply]
Do not add prices, discounts, or services that are not listed.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Fall is the best time to give your lawn some attention. We're now booking fall overseeding with winter rye for Bermuda lawns, with work running October 15 through November 15. We'll also reset your irrigation timer for cooler weather.

We're a two-person crew, so book early to get the date you want. Call or text 480-555-0186 to reserve your spot.

(Word count: 64)
```

Every fact traces to the prompt, and nothing new appears. The tool reports 64 words, and a word counter gives 60 for the body. Both sit inside the range, but the tool's count is still a claim you check. Notice that Step 4 is strategy 9, a guardrail, riding along with strategy 1. Strategies often travel in pairs. Supply the facts, then forbid the rest.

### Examples (Few-Shot)

Some jobs need a house style that is hard to describe and easy to show. A public library branch sends one-line text reminders for its events. Here is the request with no samples:

```text
Our public library branch sends short text-message reminders about events. Write the reminder for this event: a seed library swap, Thursday at 6 p.m. in the community room, free, and people should bring seeds in labeled envelopes.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Seed Library Swap this Thursday at 6 p.m. in the Community Room. Free! Bring seeds in labeled envelopes to share and take home new ones. See you there!
```

It reads well, but it is 28 words with two exclamation points, and it adds a promise ("take home new ones") the branch did not make. Now the same request with two reminders the branch sent last month:

```text
Our public library branch sends short text-message reminders about events. Here are two we sent last month:

Tue 4pm | Teen Game Club | Room B | Free, no sign-up
Sat 10am | Toddler Story Time | Children's area | Free, no sign-up

Write the reminder for this event in the same style: a seed library swap, Thursday at 6 p.m. in the community room, free, and people should bring seeds in labeled envelopes.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Thu 6pm | Seed Library Swap | Community room | Free, bring seeds in labeled envelopes
```

Chapter 4 labels examples as Format, because they show the shape of the answer. Two samples did what a paragraph of style rules would struggle to do. The tool copied the order, the short day and time, the bars, and the plain ending, and it dropped the extra promise. Two or three samples are usually enough. Make them differ in the details you want the model to vary, and match in the shape you want it to keep.

### Try It Yourself 5.1: Count What It Invents 🛠️

**Predict:** Pick a one-line prompt you sent this month for class or work, with nothing private in it. Predict how many details in its response you never supplied.

**Run:** Send the one-line prompt in a fresh conversation, then mark and count every detail you did not supply. Add the facts the job needs and one sentence that forbids the rest, and send it fresh. Count again. In your copy of `prompt-strategy-checklist.md`, fill the "Your example" cell for strategy 1 with both counts and the one fact that made the biggest difference.

**Explain:** Compare your first count with your prediction. In 1-2 sentences, explain why the count dropped, or why it did not.

### Quick Check 5.1 ✅

1. A coworker's prompt reads, "Write a thank-you note to our volunteers." Rewrite it with strategy 1, adding three facts the note needs and one sentence that forbids invented details.
2. A city recreation center wants its weekly class listings in one fixed style. Decide whether to describe the style in words or show two past listings, and justify your choice with the library reminder result.

---

## 5.2 Structure, Reasoning, and Decomposition

The strategies in this section shape how the answer is built. Strategy 3 decides the output's shape. Strategies 4 and 5 decide how the model works through a job that has more than one step.

### Output Structure

Output structure is the Format part of a prompt doing its job: a table with named columns, a numbered list, a template to fill, or a word limit. The test is simple. Where does the output go next? A group text, a spreadsheet row, a form field, and a printed flyer all need different shapes. A prompt that never says where the output goes leaves the model to pick a shape, and it often picks one that looks complete.

### Fix It 5.1: The Build Night Update 🔧

The secretary of a college robotics club needed to tell members that Thursday's build night had moved. She posts club news in the members' group text.

**Symptom:** The prompt gave every fact:

```text
Let the members of our college robotics club know that Thursday's build night moved from 5 p.m. to 6:30 p.m. It is in the same room, and everyone should bring safety glasses.
```

Here is the response it gave (captured from a chat assistant, October 2026):

```text
Here's a draft you can send as is:

**Subject:** Thursday build night moved to 6:30 p.m.

Hi everyone,

Thursday's build night now starts at **6:30 p.m.** instead of 5 p.m. We're meeting in the same room.

Please bring your safety glasses. You won't be able to work on the builds without them.

See you Thursday!
[...]
```

The cut lines held a note about adding recipients in Bcc. Every fact in the draft is right. Now picture pasting it into a group text.

**Diagnose:** Before you touch the prompt, list everything the secretary must delete or retype before this message fits a group text. Then decide which of the five parts of a prompt would have told the tool where the message was going.

**Repair:** The prompt never said where the message would go, so the tool guessed an email. It added a subject line, bold markup, a greeting, and a wrapper line in front. The content was right and the shape was wrong. That is a missing Format part, which is strategy 3 on the checklist. Add a Format part and change nothing else:

```text
Let the members of our college robotics club know that Thursday's build night moved from 5 p.m. to 6:30 p.m. It is in the same room, and everyone should bring safety glasses. Format: one plain-text message for our club's group text, under 30 words, with no subject line and no bold or other formatting. Reply with the message only.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Heads up: Thursday's build night moved from 5 p.m. to 6:30 p.m. Same room. Please bring your safety glasses. See you there!
```

What changed: one thing. The prompt gained a Format part, and the request above it stayed word for word.

**Verify:** Count the words: 22, under the limit. There is no subject line, no bold, and no line in front, so the secretary can paste it as is. Check the facts: the new time, the same room, and the glasses are all there. "See you there!" is a flourish, not a fact. One more thing changed that the repair did not aim at. The first draft's added rule ("You won't be able to work on the builds without them") is gone, because a 30-word message left no room for it. Do not count that as proof the Format part prevents additions. It took two tries to get this failure. A first prompt about pulling action items from meeting notes came back as a table without being asked, so a missing Format part does not always fail. That is why you check every time.

### Try It Yourself 5.2: Shape It for Where It Goes 🛠️

**Predict:** Choose a message you send often that lands somewhere with a fixed shape, such as a group text, a form field, a spreadsheet row, or a calendar invite. Predict the shape a chat assistant will choose if your prompt has no Format part.

**Run:** Send your request without a Format part, then add only a Format part and send it fresh. Copy `prompt-card-template.md` and fill four fields for the version that worked: Name, Job, Prompt (with `[Format]` labeled), and Good output looks like. Make at least one of your two or three criteria about shape.

**Explain:** Did the tool's first shape match your prediction? In 1-2 sentences, explain where its guess came from.

### Step-by-Step Reasoning Requests

When a job applies rules to cases, ask the model to show each check before it gives the answer. Strategy 4 does two things for you. Research on large models found that asking for intermediate steps raised accuracy on reasoning tasks. In one 2022 study, adding "Let's think step by step" raised one model's score on a set of math word problems from 17.7 percent to 78.7 percent. The second benefit matters more to you. Written checks give you something to verify line by line.

A youth sports league assigns practice fields by three rules. The coordinator asks about three requests:

```text
Our youth sports league assigns practice fields. Rules: (1) Field 2 has no lights, so every practice there must end by 6:30 p.m. (2) Teams under age 8 practice for 45 minutes, and older teams practice for 75 minutes. (3) Two teams cannot use the same field at the same time.

Requests for Wednesday:
A. U10 Hawks, Field 2, starting 5:30 p.m.
B. U7 Comets, Field 1, starting 5:45 p.m.
C. U12 Rockets, Field 1, starting 6:30 p.m.

Which requests can we approve as written? Check each request against each rule, one rule at a time, and show each check on its own line. Then give the final answer.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
[...]
**Request A: U10 Hawks, Field 2, 5:30 p.m. start (ends 6:45 p.m.)**
- Rule 1 (Field 2 ends by 6:30): Fails. 5:30 + 75 minutes = 6:45 p.m., which is 15 minutes past the cutoff.
- Rule 2 (duration): Applied correctly, 75 minutes for U10.
- Rule 3 (no overlap): Passes. No other team is on Field 2.
[...]
**Final answer:**
- Approve B (U7 Comets) and C (U12 Rockets) as written.
- Do not approve A (U10 Hawks) as written. It runs 15 minutes past the Field 2 cutoff. To fix it, start the Hawks by 5:15 p.m. on Field 2, or move them to Field 1 at a time that avoids the Comets (5:45 to 6:30) and the Rockets (6:30 to 7:45).
```

Request A is the trap. It starts well before 6:30, and only the end time breaks the rule. You can check that line yourself in ten seconds: 5:30 plus 75 minutes is 6:45. The cut lines check B and C the same way, including the point that B ending at 6:30 and C starting at 6:30 do not overlap. Keep one limit in mind. The written steps are text the model produced, not a window into how it works. A neat chain of checks can still hold a wrong step, so verify each line the way you would verify any claim.

### Decomposition

**Decomposition** means splitting a job with several stages into separate prompts, one stage each, and checking each result before you feed it into the next. Picture a volunteer coordinator with 40 survey comments. She might send one prompt to group the comments into themes and check the themes against the comments. Only then would she ask for a short memo from the themes she approved. One giant prompt would hide a bad theme inside a polished memo. Decomposition puts a checkpoint where the error would start. Skills Lab 5A uses it on a small scale when you repair one prompt before you write the card for it.

### Quick Check 5.2 ✅

1. You need the officers' names and email addresses from a page of meeting notes, pasted into a spreadsheet with three columns. Write the Format part of the prompt.
2. Analyze what the youth sports response's written checks let you verify that a one-line answer would not, and name the one thing the checks cannot prove.
3. A volunteer wants one prompt that reads 40 survey comments, finds themes, and writes a board memo. Break the job into stages with decomposition, and name what you check after each stage.

---

## 5.3 Persona, Grounding, and Guardrails

The last four strategies decide whose voice the model uses, which facts it may use, and what it must never add. They matter most when the output speaks for a business to the public.

### Persona and Audience Framing

Chapter 4's Role part names who the model plays. A **persona** is a Role described in enough detail (expertise, experience, and point of view) that it shapes what the model includes and how it sounds. Audience framing is the other half: say who will read the result and what that reader needs. Here a dental office uses both:

```text
You are a dental hygienist who has spent ten years working with nervous patients. Explain to an adult patient what will happen at her first deep cleaning next week. She is anxious and has said she does not want medical jargon. Use only these facts: the visit takes about 90 minutes, the dentist numbs one side of the mouth at a time, she can raise her left hand at any point to pause, and her gums may feel tender for two or three days afterward. Write four to six short sentences, spoken directly to her.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
I know this is the part you've been dreading, so let me walk you through exactly what will happen. The visit will take about 90 minutes, and the dentist will numb one side of your mouth at a time, so you'll never have your whole mouth numb at once. You are in charge the whole way through: just raise your left hand at any point, and we will pause right away. No explanation needed. Afterward, your gums may feel tender for two or three days, which is normal. You've already done the hardest part by showing up, and I'll be right there with you.
```

The persona bought the warm, calm voice and the plain words. The audience line bought the reassurance in the first sentence. Every fact is there. Read it a second time, though. "We will pause right away" and "I'll be right there with you" are promises, and the office never made them. A warm persona tends to reassure, and reassurance is where promises creep in. Strategy 9 handles that, later in this section.

### Grounding

**Grounding** means supplying the source the answer must come from and telling the model to answer only from it, including what to say when the source is silent. It is the strongest strategy for accuracy, because it turns "is this true?" into "is this in the source?", and you can check that. Here is a patient's question with no source:

```text
A patient at our dental office had a tooth filled this morning. She texted the front desk to ask: "Can I drink coffee this afternoon?" Write a two-sentence reply from the front desk.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Yes, you can drink coffee this afternoon, just wait until the numbness wears off so you don't accidentally burn your lip or cheek. If your tooth feels sensitive or your bite seems off, call us and we'll take a look.
```

The advice may be sensible. It is still the tool's advice, sent in the office's name, and nobody at the office approved it. Now the same question grounded in the office's own after-care sheet:

```text
A patient at our dental office had a tooth filled this morning. She texted the front desk to ask: "Can I drink coffee this afternoon?" Write a two-sentence reply from the front desk. Answer only from the after-care sheet below. If the sheet does not answer her question, say so and ask her to call the office at 602-555-0117.

After-care sheet: Do not chew on the filled side until the numbness wears off, usually 2 to 3 hours. Mild sensitivity to cold for up to two weeks is normal. Call us if your bite feels uneven after the numbness is gone.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Our after-care sheet doesn't say whether coffee is okay this afternoon, so please call us at 602-555-0117 and we'll help you. In the meantime, avoid chewing on the filled side until the numbness wears off (usually 2 to 3 hours).
```

The first reply said yes. The grounded reply said the sheet is silent and sent her to someone who can answer. That is the right result, even though it sounds less helpful. The silent-source line in the prompt did the work. Without it, a model told to "answer only from the sheet" may stretch the sheet's line about cold sensitivity into an answer about hot coffee.

### Try It Yourself 5.3: Fill the Grounding Gaps 🛠️

**Predict:** A book club wants to reserve a library meeting room every Tuesday for three months. The policy below never mentions repeat bookings. Predict whether a grounded prompt will get a yes, a no, or "the policy does not say."

**Run:** Fill the three gaps from the grounding rules in this section, then send the prompt. Save your filled prompt as a prompt card in your library, with Strategies used filled in.

```text
You answer questions from patrons of a public library branch. Answer the question below using only ____. If the policy does not answer the question, say "____" and suggest the patron ask at the front desk. Do not ____.

Policy: Meeting rooms are free for nonprofit and community groups. Book up to 30 days ahead at the front desk or by phone. Each booking is for up to 3 hours. Rooms seat 24 people. Food is allowed, but no open flames.

Question: Can our book club reserve the room every Tuesday for the next three months?
```

**Explain:** Compare your response with the one below. In 1-2 sentences, explain which of your three filled gaps produced the answer's first sentence, and whether your run said the same.

Compare your run with the response one chat assistant gave to the filled prompt in October 2026:

```text
The policy does not say whether a group can set up a standing weekly reservation, so please ask at the front desk.

Here is what the policy does say:

- Bookings can be made up to 30 days ahead, so you could not reserve all three months of Tuesdays at once.
[...]
The policy does not say whether your book club counts as a community group, so the front desk can confirm that too.
```

### Clarifying Questions First

Sometimes you do not know what the model needs until it asks. Strategy 8 tells it to ask before it writes. The president of a community college coding club tried it:

```text
I am the president of a community college coding club. I need a half-page flyer to recruit new members. Before you write anything, ask me up to three questions whose answers would change the flyer the most. Ask them all at once, then stop and wait for my answers.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
[...]
2. **Who are you trying to reach, and what will they worry about?** Complete beginners who think they "can't code," students already in CS or IT classes looking for projects and a portfolio, or both? Tell me which, plus any fear you want to defuse (no experience needed, no cost, low time commitment).

3. **What does the club actually do that would make someone show up?** Examples: weekly build nights, hackathons, project teams, interview prep, guest speakers from local employers, transfer or internship help. Pick the top two or three. If you have a club name, a tagline, or a school color or logo requirement, add that too.

Once you answer, I'll write the half-page flyer.
```

The cut first question asked what a reader should do after reading the flyer, with the meeting's date, time, and place. All three questions point at facts only the president has. Answer them in your next message, and you have built a strategy 1 prompt together. Use this strategy when the job is new to you. Skip it when you already know the facts, because the questions cost a turn.

### Negative Constraints and Guardrails

A negative constraint tells the model what not to do. A **guardrail** is a negative constraint aimed at a specific harm you can name in advance: a price, a promise, medical or legal advice, or a client's name. "Do not add prices, discounts, or services that are not listed" was a guardrail in the landscaping prompt. The hygienist prompt needed one too: "Do not promise anything the office has not promised, such as how fast staff will respond." Write guardrails from the failures you have seen. The persona run showed you the promise, so the guardrail names promises. A guardrail you cannot trace to a likely failure only makes the prompt longer.

### Quick Check 5.3 ✅

1. A hardware store wants a chat assistant to answer return questions from its posted return policy. Write the grounding sentence and the line that tells the model what to say when the policy is silent.
2. The hygienist response promised "I'll be right there with you." Decide whether the office could send it as written, and write the one guardrail that would prevent the promise.

---

## 5.4 The Output Checklist and the Repair Method

Strategies are half the skill. The other half is proving a strategy helped. For that you need a fixed way to judge a response, so that two runs get the same test.

### The Output Checklist

The **Output Checklist** is five checks you run on every response before you use it. Mark each one Yes, Partly, or No, and quote the line that decided it.

1. **Did it do the task?** The job the prompt asked for, at the size it asked for.
2. **Right shape?** The format the next step needs, ready to paste or send.
3. **Every claim traceable?** Each fact, name, number, and promise traces to your prompt or your source.
4. **Nothing added?** No services, rules, promises, or details you did not supply.
5. **Tone fits the audience?** The voice suits the reader you named.

The checklist grows out of Chapter 1's three passes. Checks 1 and 2 are the first pass, check 3 is the second, and check 4 is the third. Check 5 is new, because a prompt that names an audience can miss it. Score the landscaping crew's first run and it passes check 1 at best. Its six services and its free quote fail checks 3 and 4. The second run passes all five. The packet file `output-checklist.md` gives you the form.

### Try It Yourself 5.4: Score Before You Trust 🛠️

**Predict:** You will send the one-line landscaping prompt from Section 5.1 yourself. Predict which of the five checks your response will fail.

**Run:** Send the prompt in a fresh conversation. Fill a copy of `output-checklist.md` for the response, with Yes, Partly, or No on each check and the line you quoted to decide it.

**Explain:** Compare your marks with your prediction. In 1-2 sentences, explain why check 3 could not pass when the prompt supplied no facts.

### The Repair Method

When a prompt fails, repair it in three moves. Diagnose with the Prompt Strategy Checklist, change one thing, and compare the scores. One change per run is the rule that lets you say what helped. Change two things and the score can rise while you learn nothing about why. Chapter 6's refinement loop builds that rule into a full method with versions and a log.

Here is a Deskside prompt from Copperwind, written before the team had a library:

```text
You are a Deskside support technician at Copperwind IT Services, a managed IT services company in Phoenix. Write a reply to the client ticket below. Keep it under 120 words and friendly.

Ticket: Our front office printer says "offline" again and nobody can print invoices. We already turned it off and on. Can someone help today? - Lorena, office manager
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
[...]
Two quick checks while we get to you:

1. Look at the printer's screen or menu for a Wi-Fi or network icon. Tell us if it shows disconnected.
2. On one computer, open Printers & Scanners and see if the printer is set to "Use Printer Offline." If so, uncheck it.

I can also connect remotely this afternoon and fix it directly. Reply with a good time and the printer's model, and we'll get you printing today.
[...]
```

Score it. Checks 1, 2, and 5 pass: it is a short, friendly reply. Checks 3 and 4 fail. The second step is not Deskside's procedure, and "this afternoon" and "printing today" are promises no technician made. Run the strategy checklist and the gap is strategy 7: the prompt gave the model no source, so it wrote a likely procedure. The one change is to hand over the team's steps and limit the reply to them. Send the prompt without the [Step] lines:

```text
[Step 1: set the role, the job, and its size]
You are a Deskside support technician at Copperwind IT Services, a managed IT services company in Phoenix. Write a reply to the client ticket below. Keep it under 120 words and friendly.
[Step 2: paste the input the reply answers]
Ticket: Our front office printer says "offline" again and nobody can print invoices. We already turned it off and on. Can someone help today? - Lorena, office manager
[Step 3: tie the reply to the team's own source]
Answer only from the Deskside team's steps below.
[Step 4: supply that source in full]
Deskside steps for a printer that shows offline: (1) Check that the printer's network cable is plugged in, or that its screen shows a Wi-Fi connection. (2) On one office computer, open the printer list, remove the printer, and add it again. (3) If it still shows offline, reply to this ticket, and a technician will connect remotely during business hours.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Hi Lorena,

Sorry about the printer trouble. Let's get invoices printing again today. Since the power cycle didn't clear it, try these two checks:

1. Look at the printer. Make sure its network cable is plugged in, or that its screen shows a Wi-Fi connection.
2. On one office computer, open the printer list, remove the printer, and add it again.
[...]
```

The steps now match the team's procedure, and the remote session moved to "during business hours," as the source says. Check 3 passes on the steps. Check 4 still fails on one line: "Let's get invoices printing again today." The ticket asked for today, and the model answered the ticket's wish. Grounding fixed the procedure but did not stop the promise. So the next run adds one guardrail sentence after the grounding line and changes nothing else:

```text
Do not promise a time, and do not add steps that are not in them.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Hi Lorena,

Sorry about the offline printer. Let's get invoices moving again. Please try these steps:
[...]
If it still shows offline after that, reply to this ticket. A technician will then connect remotely during business hours to take a look.
```

All five checks pass. Because each run changed one thing, you can attribute each gain. Grounding fixed the invented step, and the guardrail removed the promised time. One caution from Chapter 2 still applies. Two runs of one prompt differ by chance, so a single good run is evidence, not proof. Run a card more than once before the whole team relies on it.

### The Repair Sheet and Library v2

The packet file `prompt-repair-sheet.md` records each repair in five fields: the weak prompt, the checklist diagnosis, the one change, the repaired prompt, and the result against the Output Checklist. One sheet block per run keeps the evidence together.

Chapter 4 ended with library v1: three to five Deskside cards in the prompt card format. Its Strategies used field stayed empty for this chapter to fill. Library v2 is the same library with that field filled on every card, so a teammate can see why each prompt works. Use your own library if you built one, or the starter `prompt-library-v1-starter.md`, which holds three finished Deskside cards. The printer card's line would read:

```text
* Strategies used (Chapter 5): grounding (the Deskside printer steps, answer only from them), negative constraints and guardrails (no promised time)
```

### Try It Yourself 5.5: Repair One Deskside Prompt 🛠️

**Predict:** A technician sends this prompt for a common ticket:

```text
Write a reply to this ticket: I can't see the shared billing mailbox in my email since yesterday. - billing clerk at a client office
```

The team knows two facts the prompt leaves out. Copperwind adds shared mailbox access only after the client's office manager approves it in writing. New access can take up to an hour to appear. Predict which of the nine strategies the prompt most needs.

**Run:** Send the prompt as written and score the response with the Output Checklist. Diagnose with the Prompt Strategy Checklist, make one change, and send the repaired prompt fresh. Score it, and fill one block of `prompt-repair-sheet.md`. Then write the repaired prompt as a prompt card with Strategies used filled. That card is the first card of your library v2.

**Explain:** Was your prediction the change you made? In 1-2 sentences, attribute the difference between your two scores to your change, and say what run would make you more confident.

### Quick Check 5.4 ✅

1. Score the first Deskside printer response on checks 3 and 4, quoting one line for each mark.
2. A teammate repaired a prompt by adding grounding, a word limit, and a persona at once, and the score rose from two checks to five. Analyze what the repair sheet can and cannot conclude about why, and describe the runs that would settle it.

---

## 5.5 Summary and Retrieval 💡

### Key Concepts

* A strategy is a named move with a test you can run on a prompt. The Prompt Strategy Checklist holds nine of them, and each one strengthens a part of the prompt Chapter 4 named. Use it to diagnose, and add only what the job needs.
* Specificity and context come first: the more the model knows, the less it invents. Pair them with a guardrail that forbids the rest. Examples (few-shot) teach a house style faster than a description can.
* Output structure fixes the shape. Ask where the output goes next, and write the Format part for that place. A missing Format part does not always fail, so check every response.
* Step-by-step reasoning requests give you checks to verify line by line, though the written steps are not proof of how the model worked. Decomposition puts a checkpoint between stages.
* A persona shapes voice and content, and audience framing names the reader. Grounding supplies the source, limits the answer to it, and says what to do when the source is silent. It turns "is this true?" into "is this in the source?"
* The Output Checklist scores every response on five checks: did it do the task, right shape, every claim traceable, nothing added, and tone fits the audience. Quote the line behind each mark.
* The repair method is diagnose, change one thing, and compare. One change per run is what lets you attribute a gain, and library v2 records the strategies on every card.

### Key Terms

See course glossary for full definitions

* strategy, Prompt Strategy Checklist (Section 5.1)
* decomposition (Section 5.2)
* persona, grounding, guardrail (Section 5.3)
* Output Checklist (Section 5.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Name the nine strategies on the Prompt Strategy Checklist in order, and give the test for any three of them.
2. State the five checks of the Output Checklist, and name the two that the first landscaping response failed.
3. Explain why the repair method changes one thing per run, using the Deskside printer repair.
4. From Chapter 3: Explain the difference between a lead and a fact, and name the strategy from this chapter that keeps an answer inside a source you supply.
5. From Chapter 1: Describe the three passes you make over every response, and match each pass to the Output Checklist checks that grew out of it.

---

## 5.6 Skills Lab 5A: Repair the Marketing Prompts

**Goal:** Repair three weak Copperwind marketing prompts with the Prompt Strategy Checklist, score every run with the Output Checklist, and hand Mei Lin a v2 prompt library with evidence of which strategy paid off.

**Starter files:** Provided files in `assets/code/chapter-05/` from the course data pack. The lab uses `skills-lab-5a-worksheet.md` (your answer file) and `copperwind-marketing-prompts.txt` (Mei Lin's request, the three weak prompts, and the facts they may use). It also uses `prompt-strategy-checklist.md`, `output-checklist.md`, `prompt-repair-sheet.md`, `prompt-card-template.md`, and `prompt-library-v1-starter.md` (three finished Deskside cards). Download the data pack from Canvas, extract it, and work at the extracted `cis137` root. Open each file in any text editor and never retype the file contents. The files are fictional, so you may paste them into a tool. Every AI response you need, you generate live in a chat assistant from your course roster and paste into the worksheet. Send each run in a fresh conversation, so one run cannot shape the next.

You first met Copperwind in Chapter 1. This lab gives you everything it needs, so you do not need any earlier file. If you built your own library in Chapter 4, you may use it in place of the starter.

### Part 1: Foundation (Aligns with Objective 5.1)

Work in `skills-lab-5a-worksheet.md`, which has a space for every task below. Read `copperwind-marketing-prompts.txt` in full before you write a prompt.

1. Before you send any prompt, write your privacy plan in two lines: what from the file may go into a tool, and what will stay out of every prompt. Mei Lin's file includes one internal note. Decide whether it goes into a prompt, and give your reason in one sentence.
2. Send Weak Prompt 1 exactly as written. Paste the prompt and the response with the tool and the date. Score the response with the Output Checklist: Yes, Partly, or No on each check, with the line you quoted to decide it.
3. Choose the one strategy from the Prompt Strategy Checklist that would fix the response's worst failure, and add it using only facts from the file. Change nothing else, send the repaired prompt, and paste it with the response. Score it with the Output Checklist, and fill a `prompt-repair-sheet.md` block for the run.

### Part 2: Application (Aligns with Objectives 5.1 and 5.2)

1. For Weak Prompts 2 and 3, run each as written, paste it, and score it. Diagnose each one with the Prompt Strategy Checklist, marking every one of the nine strategies Used, Missing, or Not needed. Name the missing strategy behind the worst failure, and say why in one sentence.
2. Repair Weak Prompts 2 and 3 one change at a time. After each change, send the prompt fresh, paste the prompt and the response, score it, and fill a repair-sheet block. Stop when a run passes all five checks or after three changes, and say which happened.
3. List every claim in your final backup-service email. Mark each one against the facts in the file as Holds, Contradicted, or Not in source (Chapter 2's verdicts). Fix any claim that is not Holds by hand, and say what you changed.

### Part 3: Extension (Aligns with Objectives 5.2 and 5.3)

Mei Lin wants library v2 and the evidence behind it. Deliver all three tasks in the worksheet.

1. Build library v2. Fill the Strategies used field on each of the three starter cards (or your own v1 cards). Add your three final marketing prompts as new cards in the prompt card format, with every field filled.
2. Choose one starter card and one strategy it lacks. Run the card as written and then with that one strategy added, each in a fresh conversation. Score both runs with the Output Checklist, and attribute the difference in two or three sentences.
3. Write a note to Mei Lin (120 to 180 words). Name the strategy that paid off most across your repairs, and give the evidence: the scores before and after, and one quoted line from each run. Then name one card in your library the Deskside team should not use yet, and say what would make it ready.

### Questions & Analysis 🤔

Answer both questions in the worksheet's final section. These answers carry significant rubric weight.

1. Find the single change in your repair-sheet blocks that raised a score the most. Quote the before and after lines from your log that show the gain, and attribute it to the strategy. Then name one other cause from Chapter 2 that could explain a change between two runs, and describe the run that would rule it out.
2. Find the claim in your Part 2 Task 3 list that came closest to reaching Mei Lin unnoticed. Quote it from your log, name the Output Checklist check that caught it, and name the strategy that should have prevented it. If no strategy could have prevented it, argue why.

**Submission:** Submit your completed worksheet as one file named `skills-lab-5a-lastname.md`, with your library v2 pasted into Part 3 Task 1. Keep every answer under its task heading. Include every prompt you sent, the tool and date, and every response you received, pasted exactly, with your Questions & Analysis answers clearly labeled at the end. Save a separate copy of library v2 for your own use.

### Rubric: Skills Lab 5A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria, five
levels from Mastery to Not Evident. The criteria are Technical
Accuracy and Efficiency, Output Quality, Documentation Quality, and
Analysis, Interpretation, and Response to QUESTION(s). The criteria
and levels are the same everywhere. Your instructor sets the point
values in your course. Check the syllabus and the Canvas rubric
attached to this lab for the values that apply to you.

---

## 5.7 Review Questions 🔄️

1. **Understand:** Explain the difference between a persona and grounding to a coworker who has never written a prompt, in no more than three sentences, with an example of each.

2. **Apply:** A tax preparation office wants a one-paragraph email reminding clients which documents to bring to their appointment. Write the prompt using at least three strategies from the checklist, and label each strategy you used.

3. **Analyze:** A hiring coordinator at a landscaping company asked for a job posting and got one that listed a benefit the company does not offer. She added a persona, two sample postings, and a guardrail in one revision, and the benefit disappeared. Analyze what she can and cannot conclude about which strategy removed it, and design the runs that would tell her.

4. **Evaluate:** A manager wants every Deskside prompt to end with a step-by-step reasoning request "because it makes answers better." Judge the rule with the evidence in this chapter, and recommend which kinds of tickets should use the strategy and which should not.

---

## Further Reading 📖

* [Language Models Are Few-Shot Learners (Brown et al., 2020)](https://arxiv.org/abs/2005.14165): The paper that showed a large model could take on a new task from a few examples in the prompt, with no extra training. Read the abstract for where the term few-shot comes from.
* [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models (Wei et al., 2022)](https://arxiv.org/abs/2201.11903): A study showing that example prompts with written reasoning steps improved large models on arithmetic, commonsense, and symbolic reasoning tasks.
* [Large Language Models Are Zero-Shot Reasoners (Kojima et al., 2022)](https://arxiv.org/abs/2205.11916): The source of the 17.7 to 78.7 percent result in Section 5.2, from one added sentence: "Let's think step by step."
* [The Prompt Report: A Systematic Survey of Prompt Engineering Techniques (Schulhoff et al., 2024)](https://arxiv.org/abs/2406.06608): A survey that sorts 58 text prompting techniques and defines the field's vocabulary. Use it to look up a strategy by its research name.
* [Generative AI Profile, NIST AI 600-1 (National Institute of Standards and Technology, 2024)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence): The companion to the NIST AI Risk Management Framework (NIST AI RMF) for generative AI, published July 2024. It names twelve risks, including confabulation, its term for confident false content.

---

## Looking Ahead ⏩

You can now strengthen a prompt with named strategies and prove a change helped with a checklist. Chapter 6 turns the repair method into a loop. You will write your criteria before the first run, version every prompt, and finish the library a colleague can pick up and use.
