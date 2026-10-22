# Chapter 4: Prompt Basics and Prompt Types

One of Copperwind's Deskside technicians has a prompt that turns a tense password ticket into a calm, clear reply in seconds. She built it over a month of trial and error, and it lives in her chat history, so when she is out sick, nobody else can find it. Mei Lin has seen the same pattern on both support teams. A good prompt is a work tool, and right now Copperwind keeps its best tools in places no one else can reach.

Part I of this book taught you how artificial intelligence (AI) tools work and how to check what they hand back. Part II teaches you to direct them, starting with the prompt itself, which this chapter takes apart. You will build prompts from five named parts and match each job to the type of prompt that fits it. Then you will read every response against the prompt that produced it, part by part, so you can say which part earned its place.

You will finish with four tools you keep: a Prompt Anatomy card, a Prompt Type picker, the prompt card format, and the first version of a prompt library. The Skills Lab hands you six Deskside tickets and Mei Lin's request for that library.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** Chapters 1-3 (the prompt log, the three passes, and the verify habit)
* **Deliverables:** Skills Lab 4A deliverable (prompt library v1 and a note to Mei Lin), Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **4.1 (Apply):** Build a prompt from its five parts for a stated job, and label each part (Section 4.1)
* **4.2 (Analyze):** Differentiate the five prompt types by the job each one fits, and justify the type you choose for a job against the other types (Section 4.2)
* **4.3 (Apply):** Use examples and standing instructions for a recurring job, check the response against each part of the prompt, and record the prompt as a prompt card (Sections 4.3-4.4)

### This chapter aligns with the following Course Learning Outcomes

* **CLO 3 (Apply):** Demonstrate effective prompting strategies to improve AI outputs.

---

## 4.1 The Five Parts of a Prompt

Chapter 2 showed you what a model does with a prompt: it reads everything in the context window and predicts likely text, one token at a time. That has a plain consequence for you as the writer. Whatever you leave out, the model fills with what is likely, and what is likely is not what you know about your own job.

Here is a front desk coordinator at a small dental office, in a hurry:

```text
Write a text message for our dental office's patients about the parking change.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Here's a draft you can fill in:

**Text message (about 300 characters):**

Hi [First Name], this is [Office Name]. Starting [date], patient parking has moved to [new location/lot]. The old lot at [old location] will be closed. Look for our signs at the entrance. Questions? Call us at [phone number]. See you soon!
[...]
**Details to confirm before sending:**
- Effective date, and whether the old lot closes the same day
- Exact location of the new parking (a street address or cross street helps)
[...]
- Whether you want to add "Reply STOP to opt out," which many text platforms require
```

This run did not invent the details. Instead it returned a template, and every bracket marks a fact the coordinator knew and did not say. It even guessed at the kind of change ("parking has moved") and listed the details to confirm. A template is not a text she can send. Chapter 1's Fix It repaired a vague prompt by supplying how much, for whom, and in what shape, and this section gives those repairs names.

### Five Parts, Five Tests

The **five parts of a prompt** are Role, Task, Context, Format, and Constraints. Each part answers one question that the model would otherwise answer with a guess. A prompt does not need all five every time, but you should know which ones you left out, and why.

| Part | What it tells the model | One-line test |
| --- | --- | --- |
| Role | Whose knowledge, habits, and voice to borrow | Could you name the job title the model is playing? |
| Task | The one action and the one thing it produces | Does the prompt hold one verb and one deliverable? |
| Context | The facts, audience, and situation it cannot guess | Could a stranger do the job with only these facts? |
| Format | The shape of the output: length, layout, structure | Could you sketch the output's shape before you send? |
| Constraints | The limits: what must not happen and what must survive | Does the prompt say what the model must not do? |

Format and Constraints are easy to blur. Format is the shape the reader sees, such as "one message, under 300 characters." Constraints are the rules about content and behavior, such as "add no facts" or "do not ask patients to reply." A useful habit: if breaking the rule would make the output the wrong size or layout, it belongs in Format. If breaking it would make the output wrong or unsafe, it is a Constraint.

### The Same Message, Built from Parts

Here is the coordinator's request rebuilt from all five parts. Send the prompt without the [Step] lines. They show you the decision behind each part.

```text
[Step 1 (Role): pick whose habits the model should borrow]
You are the front desk coordinator at a small family dental office.
[Step 2 (Task): one verb, one deliverable, one audience]
Write a text message to patients who have appointments next week.
[Step 3 (Context): hand over every fact the model cannot guess]
The office parking lot will be repaved Monday through Wednesday, March 9 to 11. On those days, patients can park free in the church lot across the street on Cedar Avenue. Our entrance and hours do not change.
[Step 4 (Format): set the shape the patient will see]
Send one message, under 300 characters, in plain text with no emojis.
[Step 5 (Constraints): rule out the moves you cannot afford]
Do not add any facts that are not in this prompt, and do not ask patients to reply.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Parking lot repaving Monday through Wednesday, March 9 to 11. On those days, park free in the church lot across the street on Cedar Avenue. Our entrance and hours stay the same. See you at your appointment next week.
```

Run the three passes from Chapter 1. Did it do what was asked? One message, 216 characters, no emojis, no request to reply. Is each claim true? Every fact matches the prompt. What did it add? Nothing new, and it dropped the greeting, which a patient may or may not miss. Now look for what it left out: the text never says who sent it. The Context part named no office, and the Constraint forbade adding facts, so the model could not fill the gap. A text about parking from an unknown number is a real defect, and it fails the Context test. The Context part did the heavy lifting here, because it replaced every bracket in the first draft with a fact the coordinator supplied. Section 4.4 shows you how to test what the other parts bought.

!!! note "Tool check (verified October 2026)"
    Any chat assistant on the course roster works for every exercise in this chapter. Your syllabus names the current roster. Some tools offer prompt templates or suggested prompts. Treat them as starting points and label their parts the same way.

### Try It Yourself 4.1: Fill Your Prompt Anatomy Card 🛠️

**Predict:** Pick a message you write often, such as a club reminder, a shift-swap request, or a note to a customer. Before you send the prompt, predict which of your five lines the response will follow least closely, and why.

**Run:** Open `assets/code/chapter-04/prompt-anatomy-card.md` from the course data pack and save a copy. In its "Your prompt" column, write one line for each part of a prompt for your message. Check each line against its one-line test. Assemble the five lines into one prompt, send it, and paste the prompt and the response into your prompt log. Your filled card is the artifact you keep.

**Explain:** Compare the response with your card, part by part. In 1-2 sentences, name the part whose line the response followed most closely, and the part you would rewrite before you reuse the card.

### Quick Check 4.1 ✅

1. Label each part in this prompt, then name the one part it leaves out: "Act as the scheduling coordinator for a youth sports league. Draft an email to the league's coaches announcing the new field schedule. Use three bullet points and keep it under 120 words."
2. A coworker sends a chat assistant a paragraph and the words "Make this better." Write the Task line and the Format line the prompt needs, for a paragraph that will go on a landscaping company's website.
3. Apply the Context test to this prompt for a public library branch: "Write a sign telling patrons about the new rules for the study rooms." Write the two facts a stranger would need before the prompt could pass.

---

## 4.2 Prompt Types and the Jobs They Fit

A **prompt type** is the form a request takes, which tells the model what kind of response you want. Five types cover most of the work you will do: instruction, question, completion, role play, and example-led (few-shot). The type is a choice, like choosing between an email and a phone call, and the parts from Section 4.1 work inside any of them.

| Type | What you send | The job it fits | What comes back | Watch for |
| --- | --- | --- | --- | --- |
| Instruction | A command with a Task: "Write...", "List...", "Rewrite..." | You need a finished thing you can use | The thing itself | A missing Context part, which the model fills with guesses |
| Question | A question: "What...?", "Why...?", "How...?" | You need to understand something | An explanation | Asking a question when you needed the thing |
| Completion | The start of the text, for the model to finish | You have the opening and the voice, and need the rest | A continuation in your voice | The model fills gaps with likely details |
| Role play | A role for the model and a scene to play | You need practice, such as rehearsing a hard conversation | Turns in character | The model playing your side too |
| Example-led (few-shot) | Finished examples, then the new case | You need many outputs in one shape or voice | A new item that copies the examples | It copies habits you did not mean to teach |

In this chapter's runs, the first two types caused the most trouble, because they are easy to mix up. Fix It 4.1 shows what happens when a question goes out where an instruction was needed. Section 4.3 covers the example-led type in full, and the other two are below.

### Completion: Start It, Let It Finish

A completion prompt hands over the beginning of a text, and it fits when you have the voice and the first facts and want the model to carry on. A chat assistant needs one line of instruction in front of the text, such as "Complete this message." Only a raw model, the kind Chapter 2 described in Section 2.1, simply continues whatever it is given. Here is a youth sports league coordinator with a message half written:

```text
Complete this message to families in the same voice. Add no more than two sentences.

Hi Hornets families! Saturday's practice moves indoors to the Desert Willow Elementary gym because the field is being reseeded. Same time, 9 a.m. Please bring
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
water bottles, cleats or sneakers, and a healthy dose of Hornet energy. We can't wait to see everyone there!
```

The voice matched and the length held, but look at what came after "Please bring." The coordinator never said what to bring, so the model picked likely items. Cleats are a likely item for outdoor practice, and a poor one for a gym floor. When you stop mid-sentence, supply the facts first or check every item the model chose.

### Role Play: Rehearse Before It Counts

A role play prompt gives the model a part to play and asks it to stay in it, and the job it fits is practice. The president of a community college's Cybersecurity Club is about to ask student government for travel money, and she wants to face the hard questions first:

```text
You are the treasurer of a community college's student government. I am the president of the college's Cybersecurity Club. I will ask you for $400 to send four members to a regional capture-the-flag competition. Stay in character. Ask me the two hardest questions a treasurer would ask about this request, then stop and wait for my answers. Do not answer for me.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Thanks for coming in. I've read your request, and I have two questions before I can bring this to the board.

**Question 1: Where does the $400 go, line by line, and what is the club putting in?**
[...]
**Question 2: What does the student body get back, and how do you choose who goes?**
Student government money belongs to every student, not just club members. How were these four members selected, and is the process open to anyone in the club? What will you deliver after the event? Think of a presentation, a workshop, a recruiting push, or a write-up. How will you show the board that $400 produced something beyond a trip for four people?

I'll wait for your answers.
```

The model stayed in the role and stopped where it was told to stop. Its two questions each bundle several smaller ones, and that is useful practice in itself. The line "Do not answer for me" is a Constraint, and it matters most in role play. Without it, a model may write both sides of the scene, and then you get a script to read instead of a conversation to practice.

### Fix It 4.1: The Monitor Ticket 🔧

A Deskside technician at Copperwind had a client's ticket open and wanted a reply she could paste into it. The ticket names no person and holds nothing private, so it passes Chapter 1's rule, and she used Copperwind's approved pilot tool.

**Symptom:** She typed what was on her mind:

```text
What would a good reply to this ticket look like?

Ticket from a client's office manager: "Since this morning my second monitor stays black. The laptop only sees one screen. I already unplugged the cable and plugged it back in. I have a client meeting at 2 p.m. and need both screens. Can someone help?"
```

Here is the response it gave (captured from a chat assistant, October 2026):

```text
A good reply acknowledges the 2 p.m. deadline, gives her a few quick things to try in order, and offers a fast fallback if they fail. She has already reseated the cable, so don't make her repeat that.

**Sample reply**

Subject: Re: Second monitor not detected (let's get this fixed before 2 p.m.)

Hi [Name],
[...]
**Why this works**

- **It leads with the deadline.** She told you what matters, so you show her you heard it.
[...]
**Things to adjust**
[...]
```

The full response ran 33 lines. The troubleshooting steps in its sample reply were sound, but it was not something she could send. Count what she would have to cut before the client sees it.

**Diagnose:** Before you change the prompt, name in one sentence what the model treated the first line as asking for, and what kind of thing it handed back as a result.

**Repair:** The first line was a question. A question asks for an explanation, and the answer to "what would a good reply look like?" is a description of a good reply, with an example tucked inside a lesson. The model answered the question it was asked. The technician needed an instruction with a Task: one verb and one deliverable. Change the question to an instruction, and leave the ticket alone:

```text
Write the reply to this ticket that I will send to the client.

Ticket from a client's office manager: "Since this morning my second monitor stays black. The laptop only sees one screen. I already unplugged the cable and plugged it back in. I have a client meeting at 2 p.m. and need both screens. Can someone help?"
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
**Subject:** Re: Second monitor stays black

Hi [Name],

Thanks for the details. We want you ready well before 2 p.m. Try these steps in order and stop as soon as the screen comes back:
[...]
If the screen is still black after these steps, reply with the make and model of your laptop and monitor, or call us at [phone number]. We can connect remotely and fix it with you on the line. Please let us know by 12:30 p.m. so we have time to work through it.
[...]
Thanks,
[Your name]
[Company] Help Desk

---

Notes for you before you send:
[...]
- The 12:30 p.m. cutoff is my guess. Adjust it to your team's availability.
```

What changed: one thing. The first line is now an instruction with a Task, and the ticket text is word for word the same.

**Verify:** Check the response against the Task. It is a reply from the subject line to the signature, with four numbered steps (cut above) and nothing in front of it, and the lesson and the "Why this works" section are gone. Three short notes follow the line, and the last one admits a guess: the model added a 12:30 p.m. deadline that nobody at the help desk set. The type change did not catch that, because the prompt still has no Constraints part. Adding one is the next change, made in its own run so you can tell which change did the work. Three question wordings were tried for this lesson, and two came back as lessons. The third, "How should I reply to this ticket?", came back as a draft. Two of three wordings failed on this ticket.

### Try It Yourself 4.2: One Job, Two Types 🛠️

**Predict:** Pick a job you have this week that needs a finished piece of writing, such as a reply, a sign, or a list of steps. Predict which type will give you something you can use as it comes back, and what the question type will return instead.

**Run:** Send the job twice, each in a fresh conversation: once as a question, and once as the type you predicted would win. Keep the facts in both prompts the same. Paste both prompts and responses into your prompt log. Then open `assets/code/chapter-04/prompt-type-picker.md`, save a copy, and add a row in its "Your jobs" table: the job, the type that won, the runner-up, and a one-line reason. That row is the artifact you keep.

**Explain:** Was your prediction right? In 1-2 sentences, explain what the losing type returned and when that type would have been the right choice.

### Quick Check 4.2 ✅

1. A public library branch wants its new desk volunteers to practice telling a patron about a lost-item fee. Choose the prompt type, and justify your choice against the instruction type in two sentences.
2. Rewrite this question as an instruction with a Task, for a dental office: "Can you tell me what a good out-of-office message says?"
3. A landscaping company's estimate letters must open with the same fixed sentence the owner wrote. Decide between a completion prompt and an instruction prompt that quotes the sentence. Defend your choice with one risk of the other type.

---

## 4.3 Standing Instructions and Examples

Some jobs come back every day. For those, you can teach the model the shape you want once, with examples, and you can set rules that last a whole conversation. This section covers both.

### Zero-Shot and Few-Shot

**Zero-shot prompting** means asking for an output with no examples of it. Every prompt so far in this chapter was zero-shot. **Few-shot prompting** means including a few finished examples of the output you want, then the new case. It is the example-led prompt type from Section 4.2. A 2020 paper made it famous by showing that a large model could pick up a new task from a few examples placed in the prompt (Further Reading).

Here is the owner of a small landscaping company. Her crew texts each customer when a visit is done. First, the zero-shot version:

```text
Write a text message to a landscaping customer saying today's visit is done. Facts: the customer's name is Dana. We mowed and edged the front and back yards and trimmed the hedges. The drip line by the back fence is leaking.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Hi Dana, today's visit is done. We mowed and edged the front and back yards and trimmed the hedges. One thing to flag: the drip line by the back fence is leaking. Want us to take a look at it on our next visit? Thanks!
```

It is correct and polite, and it does not sound like her. It also offers a follow-up visit that nobody asked it to offer. Now the few-shot version, with two texts the owner wrote herself. Send the prompt without the [Step] lines.

```text
[Step 1: name the job in one line]
Write a text message to a landscaping customer saying today's visit is done.
[Step 2: show the shape and voice with finished examples]
Match the style of these two texts our owner wrote.

Example 1: "Hi Marcus, all done for today. Mowed, edged, and blew off the patio. Heads up: one sprinkler head by the mailbox is cracked. Want us to swap it next visit? Rosa"

Example 2: "Hi Joan, finished up. Trimmed the oleanders and cleared the side yard. Your back gate wasn't latching, so we tied it shut for now. Rosa"
[Step 3: hand over the new case's facts, apart from the examples]
Now write one for this visit. Customer: Dana. We mowed and edged the front and back yards and trimmed the hedges. The drip line by the back fence is leaking.
[Step 4: keep the examples' facts out of the new text]
Use only these facts.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Hi Dana, all done for today. Mowed and edged the front and back yards and trimmed the hedges. Heads up: the drip line by the back fence is leaking. Want us to take a look at it next visit? Rosa
```

The examples taught the shape: "all done for today," clipped phrases with no "we," a "Heads up:" line, and no "Thanks!" The response is 40 words against the zero-shot version's 45. It also signed the text "Rosa," which is right only if Rosa is the one who sends it. Examples teach everything they contain, including habits you did not mean to teach. A 2022 study of classification and multiple-choice tasks found that the shape of the examples (their format and the kind of text in them) drove results more than whether the example answers were correct. A text message is a different kind of task, so treat that finding as a reason to pick examples you would be glad to see copied.

Now look at the offer, "Want us to take a look at it next visit?" Dana's facts held no offer. The zero-shot version made a similar offer, so the model leans toward one on its own. Example 1 also models an offer ("Want us to swap it next visit?"), so the examples may have reinforced it. The prompt already carried a Constraint, "Use only these facts," and it did not catch the offer, because an offer is not a fact. An added offer is a promise the crew may not want to make. To stop it, a Constraint has to name the behavior. Here is the same few-shot prompt with one sentence added at the end, "Do not offer any service or repair.":

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Hi Dana, all done for today. Mowed and edged the front and back yards and trimmed the hedges. Heads up: the drip line by the back fence is leaking. Rosa
```

The offer is gone, and the voice from the examples stayed. "Use only these facts" did not stop it, and "Do not offer any service or repair" did, on this run. A Constraint works when it names the exact move you want to rule out.

### Standing Instructions

Some rules should hold for every request in a conversation, not just one, and you can set them at the start. A volunteer at a public library branch's front desk opened a conversation this way, then asked two patron questions in the same chat:

```text
For the rest of this conversation, follow these standing instructions. I volunteer at the front desk of a public library branch. Write every answer for patrons who are new to computers: short sentences, no jargon, no more than five numbered steps, and end by telling them they can ask at the desk for help. Reply only with the word Ready to this message.
```

The tool answered "Ready." Then came the first patron question, "How do I attach a photo to an email on my phone?"

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Here is how to attach a photo to an email on your phone.

1. Open your email app. Tap the button to write a new message.
[...]
3. Tap "Photos" or "Gallery" to see your pictures.
4. Tap the photo you want. Then tap "Done," "Choose," or the check mark.
5. Type the person's email address. Tap the send button.

You will see the photo in your message before you send it.

If any step looks different on your phone, you can ask at the desk for help.
```

The answer used five steps and short sentences, and it ended with the desk line. The second patron question, about making text bigger, got an answer that followed every rule too. The volunteer typed the rules once and got them on every answer.

Two features make this kind of rule permanent. **Custom instructions** are text you save in a tool's settings that the tool adds to every conversation you start, or to every conversation in one workspace. A **system prompt** is a set of instructions the tool or app sends to the model before your first message, usually out of your sight, to set the assistant's role and rules. Most chat tools run with one. The samples in this chapter were captured with a short system prompt that tells the model to act as a plain chat assistant. When you open a chat with standing instructions, as the volunteer did, your opening works like a system prompt for that conversation, though the model still reads it as your message. Tools give their own system prompt more weight, and it does not fade the way an early message in a long chat can.

Standing rules have two limits. First, Chapter 2 showed that a long conversation can push early instructions out of view, so restate the rules when a long chat starts ignoring them. Second, custom instructions are stored with your account. Chapter 1's rule applies to them exactly as it applies to a prompt, so never save a client's name, an account number, or anything private there.

!!! note "Tool check (verified October 2026)"
    Many chat assistants let you save standing instructions in their settings, under names such as custom instructions or personalization. Your tool's help pages say whether it has the feature and where it lives. When the feature is on, the model sees those instructions in every conversation, including your lab work.

### Try It Yourself 4.3: Teach It Your Voice 🛠️

**Predict:** Choose a short message you send often, and write two finished examples of it in your own words, with nothing private in them. Predict which of your habits the few-shot run will copy, and one habit in your examples that you would not want it to copy.

**Run:** Send the request zero-shot in one fresh conversation, then few-shot with your two examples in another, using the landscaping prompt's four steps. Paste both into your prompt log. Then open `assets/code/chapter-04/prompt-card-template.md`, save a copy, and fill its Name, Job, and Prompt fields with your few-shot prompt. Label the examples `[Format]`, because they show the shape you want. In the Notes field, write one line on what the examples changed. Those fields are the artifact you keep.

**Explain:** Did the few-shot run copy the habit you hoped to avoid? In 1-2 sentences, explain how you would change one example to stop it.

### Quick Check 4.3 ✅

1. A youth sports league sends nearly the same rain-out text about twenty times a season. Decide whether the coordinator should use a zero-shot or a few-shot prompt, and justify the choice in two sentences.
2. A coworker's custom instructions read: "I work at Copperwind. My main client is a property manager, account 44817, contact Lena Park." Apply Chapter 1's rule, and rewrite the instructions so they keep what is useful and drop what does not belong.
3. Both of your few-shot examples end with "See you soon!" Predict what the next output will do, and write the change to one example that tests your prediction.

---

## 4.4 Reading the Output and Writing the Card

Chapter 1's three passes ask whether the response did what you asked. With named parts, you can ask a sharper question: what did each part contribute? Read the response against the prompt one part at a time, and record what each part requested and what the response delivered. For the dental office prompt in Section 4.1, that reading looks like this:

| Part | What it asked | What the response did |
| --- | --- | --- |
| Role | Front desk coordinator at a dental office | Plain, friendly office voice, no clinical terms |
| Task | One text to patients with appointments next week | One text, ending "See you at your appointment next week" |
| Context | Repaving dates, the church lot on Cedar Avenue, entrance and hours unchanged | All four facts, nothing else |
| Format | One message, under 300 characters, plain text, no emojis | 216 characters, plain text, no emojis |
| Constraints | No added facts, no request to reply | No added facts, no request to reply |

### The Remove-One-Part Test

A part that the response obeyed may not have done any work, because the model might have behaved the same way without it. To find out, remove one part, send the prompt fresh, and compare. Here is the dental prompt with the Format sentence removed:

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Hi from your dental office. Our parking lot will be repaved Monday through Wednesday, March 9 to 11. On those days, you can park free in the church lot across the street on Cedar Avenue. Our entrance and hours stay the same. We'll see you at your appointment next week.
```

This version ran 269 characters, so it still fit the 300-character limit, but it added a greeting and grew by a quarter. On this run, the Format part bought a tighter message, not a rescue. Next, with the Constraints sentence removed and the Format sentence back in place:

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Hi, this is your dental office. Our parking lot will be repaved Monday through Wednesday, March 9 to 11. On those days, please park free in the church lot across the street on Cedar Avenue. Our entrance and hours stay the same. See you next week!
```

This run added no facts and asked for no reply, even without the rule. So did the Constraints part buy nothing? Look back at the bare prompt's draft in Section 4.1. Its template included "Questions? Call us," and it suggested a "Reply STOP" line, so it hinted at the failure this rule prevents. One run without the rule went fine, but the rule stays on the card because the next run may not.

### The Prompt Card

A **prompt card** is a one-page record of a reusable prompt. It holds what the prompt is for, the full text with its parts labeled, a sample input, what good output looks like, and when it was last run. Every card uses the same fields, in this order:

* Name
* Job (what this prompt is for)
* Prompt (full text, with the five parts labeled in brackets, such as `[Role]`)
* Example input
* Good output looks like (two or three criteria)
* Strategies used (Chapter 5 fills this field)
* Last run (tool, date)
* Notes (what to watch, what it gets wrong)

Here is the dental office prompt as a card:

```text
Name: Parking change text
Job: Tell patients with appointments next week about a parking change
Prompt: [Role] You are the front desk coordinator at a small family dental office. [Task] Write a text message to patients who have appointments next week. [Context] [office name] [paste the change: dates, where to park, what stays the same] [Format] Send one message, under 300 characters, in plain text with no emojis. [Constraints] Do not add any facts that are not in this prompt, and do not ask patients to reply.
Example input: [office name] is the office's name. Lot repaved March 9 to 11. Park free in the church lot on Cedar Avenue. Entrance and hours unchanged.
Good output looks like: (1) every fact from the input and no others, (2) under 300 characters, (3) no request to reply
Strategies used: (blank until Chapter 5)
Last run: chat assistant, October 2026 (see the prompt log)
Notes: Drops the greeting. Without [office name], the text does not say who sent it. The bare version of this request suggested a "call us" line and a "Reply STOP" line, so keep the Constraints line.
```

Notice the bracketed slot in the Context part. A card holds the parts that stay the same from job to job, and the slot shows where each new job's facts go. That slot is also how a card keeps Chapter 1's rule: client names and private details go in at send time, never into the card itself.

A **prompt library** is a shared set of prompt cards that a team keeps, runs, and improves. Mei Lin's ask is exactly this: a library the Deskside team can share, with a standard card and a log, so a technician's good prompt does not live only in that technician's chat history. Version 1 of a library is small on purpose: three to five cards, each run once and read back against its prompt. Chapter 5 adds the strategies behind each card, and Chapter 6 adds the refinement logs and a README.

### Try It Yourself 4.4: What Each Part Bought 🛠️

**Predict:** Use your prompt from Try It Yourself 4.1, or the dental office prompt if you prefer. Predict which part, if you removed it, would change the response the most, and what the change would be.

**Run:** Send the full prompt in one fresh conversation. Then remove the part you picked and send the rest in another. Paste both into your prompt log, and fill a five-row table like the one above for the full run. Open a fresh copy of `prompt-card-template.md` for this prompt and fill Name, Job, and Prompt. Then write two or three criteria in the "Good output looks like" field, based on what the removed part bought. Those criteria are the artifact you keep.

**Explain:** Was the part you removed the one that mattered most? In 1-2 sentences, explain why a part that changed nothing on this run might still belong on the card.

### Try It Yourself 4.5: Card the Monitor Ticket 🛠️

**Predict:** The repaired prompt in Fix It 4.1 has a Task and a Context, and nothing else. Predict whether adding a Constraints line will stop the invented 12:30 p.m. deadline, and what else the model might add in its place.

**Run:** Open a fresh copy of `prompt-card-template.md`. Build a card for Copperwind's Deskside team from the repaired prompt: add the missing parts, label all five, and replace the ticket text with the slot `[paste the ticket]`. Fill Example input with the monitor ticket from Fix It 4.1, which holds nothing private. Run the card once with that input in a fresh conversation, paste the prompt and the response into your prompt log, and fill Last run and Notes. Leave Strategies used blank. The finished card is the artifact you keep.

**Explain:** Did the response invent a deadline or a promise this time? In 1-2 sentences, name the part that made the difference, and the one field on your card a colleague would need most.

### Quick Check 4.4 ✅

1. A card's "Good output looks like" field lists three criteria: a reply under 120 words, names the client's deadline, and promises nothing the ticket did not ask for. The response runs 95 words, names the deadline, and offers a loaner laptop. Score the response against each criterion, and name the part of the prompt you would change.
2. A teammate's card for a youth sports league's schedule email has an empty Example input field. Write a usable Example input for it, and one "Good output looks like" criterion that the example lets you test.
3. A prompt says "Use a table with three columns," and the response comes back as a bulleted list. Analyze which part the model ignored, and describe how the remove-one-part test could show whether another part caused the problem.

---

## 4.5 Summary and Retrieval 💡

### Key Concepts

* A model fills whatever a prompt leaves out with whatever is likely. The five parts of a prompt (Role, Task, Context, Format, Constraints) name the usual gaps, and each part comes with a one-line test. A bare prompt can return a template full of blanks, one bracket for every missing fact.
* Format sets the shape the reader sees, and Constraints set the rules about content and behavior. If breaking a rule changes the size or layout, it is Format. If breaking it makes the output inaccurate or unsafe, it is a Constraint.
* The five prompt types are instruction, question, completion, role play, and example-led (few-shot), and you choose among them by the job. A question requests an explanation, so asking one when you need a finished draft returns a lesson you have to cut down.
* Zero-shot prompts include no examples, and few-shot prompts include a few finished ones. Examples teach shape and voice, and they also teach habits you never intended to teach, so choose examples you would be glad to see copied.
* Standing instructions set rules for a whole conversation. Custom instructions save them in a tool's settings, and most tools run a system prompt you usually cannot see. Chapter 1's rule applies to anything you save.
* Read a response against its prompt part by part, then use the remove-one-part test to discover what each part contributed. A part that changed nothing on one run can still guard against a failure you have already observed.
* A prompt card records a reusable prompt in standard fields, with slots where each new job's facts go, so private details never live on the card. A prompt library is a team's shared collection of cards, and version 1 holds three to five.

### Key Terms

See course glossary for full definitions

* five parts of a prompt (Section 4.1)
* prompt type (Section 4.2)
* zero-shot prompting, few-shot prompting, custom instructions, system prompt (Section 4.3)
* prompt card, prompt library (Section 4.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Name the five parts of a prompt in order, and give the one-line test for any two of them.
2. Name the five prompt types, and match each one to a job it fits.
3. Explain the remove-one-part test, and say what it tells you that reading the response alone cannot.
4. From Chapter 2: Name the three things that shape every response, and say which one the five parts of a prompt give you control over.
5. From Chapter 1: State the one rule about what never goes into an AI tool, and explain how a slot such as `[paste the ticket]` on a prompt card helps a team keep it.

---

## 4.6 Skills Lab 4A: The Deskside Prompt Library

**Goal:** Build version 1 of the prompt library Mei Lin asked for. Deliver three to five prompt cards for Copperwind's common Deskside tickets, each run once and read back against its prompt, and a note telling her which card to try first.

**Starter files:** Provided files sit in `assets/code/chapter-04/` in the course data pack. `skills-lab-4a-worksheet.md` is your answer file. `deskside-ticket-samples.txt` holds Mei Lin's request and six client tickets, one for each common ticket type. `prompt-card-template.md` is the card format, `prompt-anatomy-card.md` lists the five parts and their tests, and `prompt-type-picker.md` is the job-to-type table. Download the data pack from Canvas, extract it, and work at the extracted `cis137` root. Open each file in any text editor. Never retype the file contents. The tickets are fictional, so you may paste them into a chat assistant. Every AI response you need, you generate live in a chat assistant from your course roster and paste into the worksheet.

You first met Copperwind in Chapter 1. This lab gives you everything it needs, so you do not need any earlier file.

### Part 1: Foundation (Aligns with Objective 4.1)

Work in `skills-lab-4a-worksheet.md`, which has a space for every task below. Read `deskside-ticket-samples.txt` in full before you write a prompt.

1. Before you send any prompt, write your privacy plan in two columns. In the first, list what a prompt card may carry. In the second, list each kind of detail in the tickets that must stay out of every card, and the slot that replaces it (such as `[client name]`). Name the rule from Chapter 1, or the principle from Chapter 3, behind each item that stays out.
2. Choose one ticket. On a copy of `prompt-anatomy-card.md`, write one line for each of the five parts of a prompt that drafts a reply to it. Mark whether each line passes its one-line test, and fix any line that fails.
3. Assemble the five lines into one prompt, paste the ticket in place of its slot, and send it. Paste the prompt and the response with the tool and the date.

### Part 2: Application (Aligns with Objectives 4.2 and 4.3)

1. Fill three rows of `prompt-type-picker.md` for three different Deskside jobs drawn from the tickets. At least one job must need something other than a reply, such as a checklist for the technician, an explanation of an error, or practice for a call with an upset client. For each row, give the type you chose, the runner-up type, and one line on why the chosen type wins.
2. Pick one of the three jobs. Send it once as your chosen type and once as the runner-up, each in a fresh conversation, with the same facts in both. If neither type is a question, send the job a third time as a question. Paste every prompt and response. State which response a technician could use as it came back, and quote the line that shows it.
3. Read your Part 1 Task 3 response against its prompt. Build a five-row table with one row per part: what the part asked, what the response did, and whether it held or missed.
4. Open a fresh conversation with standing instructions for the Deskside team: who the answers are for, the tone, the length or shape, and one rule every answer must follow. Then ask two Deskside questions drawn from the tickets, in the same conversation. Paste all three turns, and record whether each rule held on both answers.

### Part 3: Extension (Aligns with Objectives 4.1 and 4.3)

1. Build library v1: three to five prompt cards in the `prompt-card-template.md` format, covering at least three of the six ticket types in `deskside-ticket-samples.txt`. Every card labels its five parts and uses slots in place of private details. At least one card is few-shot, with two examples you wrote yourself. Leave Strategies used blank, because Chapter 5 fills it.
2. Run each card once in a fresh conversation, using its Example input. Paste each prompt and response, and fill the card's Last run field. Score each response against the card's "Good output looks like" criteria, marking each criterion met, partly met, or not met.
3. Write a note to Mei Lin (100 to 150 words). Name the card the Deskside team should try first and why, citing its run. Then name the one check a technician must make before sending any reply that came from the library.

### Questions & Analysis 🤔

Answer both questions in the worksheet's final section. These answers carry significant rubric weight.

1. Find the card whose run missed a "Good output looks like" criterion, or came closest to missing one. Quote the criterion and the response line from your log. Name the part of the prompt that should have prevented the miss, and write the one change you would make to the card.
2. A technician tells Mei Lin, "I don't need cards. I just ask the assistant questions." Using your Part 2 Task 2 log entries, explain when a question is the right type and what it cost on your job. Then explain what a card gives a colleague that a chat history does not.

**Submission:** Submit your completed worksheet as one file named `skills-lab-4a-lastname.md`. Keep every answer under its task heading. Include every prompt you sent, the tool and date, and every response you received, pasted exactly, with your Questions & Analysis answers clearly labeled at the end.

### Rubric: Skills Lab 4A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria, five
levels from Mastery to Not Evident. The criteria are Technical
Accuracy and Efficiency, Output Quality, Documentation Quality, and
Analysis, Interpretation, and Response to QUESTION(s). The criteria
and levels are the same everywhere. Your instructor sets the point
values in your course. Check the syllabus and the Canvas rubric
attached to this lab for the values that apply to you.

---

## 4.7 Review Questions 🔄️

1. **Understand:** Explain the difference between the Format part and the Constraints part to a new coworker, in no more than three sentences, with one example of each.

2. **Apply:** A public library branch is starting a laptop checkout. Laptops go out for three hours, patrons need a library card in good standing, and laptops cannot leave the building. Write a prompt for a sign at the checkout desk, with all five parts labeled in brackets.

3. **Analyze:** A landscaping crew lead built a few-shot prompt for estimate follow-up texts. All three of his examples mention a ten percent discount for booking that week. The new text offered the same discount to a customer who was never promised one. Analyze why it happened, and name the part of the prompt you would change and how.

4. **Evaluate:** A dental office manager wants to save custom instructions for the whole front desk. They would hold the office's address, hours, and tone, the names of its three dentists, and a rule to keep every message under 300 characters. Decide whether you would approve the plan, approve it with changes, or reject it. Defend your decision with one benefit and one risk, and name the one item that, if added to the instructions, would change your answer.

---

## Further Reading 📖

* [Language Models are Few-Shot Learners (Brown and others, 2020)](https://arxiv.org/abs/2005.14165): The paper that showed a large model could take on a new task from a few examples written into the prompt, with no extra training. Its Figure 2.1 shows zero-shot, one-shot, and few-shot prompts side by side.
* [Rethinking the Role of Demonstrations: What Makes In-Context Learning Work? (Min and others, 2022)](https://arxiv.org/abs/2202.12837): The study behind Section 4.3's warning about examples. On classification and multiple-choice tasks, it found that the format of the examples and the kind of text in them mattered more than whether the example answers were correct.
* [Training Language Models to Follow Instructions with Human Feedback (Ouyang and others, 2022)](https://arxiv.org/abs/2203.02155): One reason chat assistants follow instructions as well as they do. The authors fine-tuned a model on people's example answers, then used their rankings (the RLHF method from Chapter 2), so that it followed a user's intent.
* [The Prompt Report: A Systematic Survey of Prompt Engineering Techniques (Schulhoff and others, 2024)](https://arxiv.org/abs/2406.06608): A survey that lists a shared vocabulary of 33 terms and a taxonomy of 58 text prompting techniques. It is a useful map of how researchers name the ideas in this Part of the book.
* [Effective Prompts for AI: The Essentials (MIT Sloan Teaching and Learning Technologies)](https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/): A university guide that recommends supplying context, being specific, and building on the conversation. It includes short examples of a simple prompt and a richer one.

---

## Looking Ahead ⏩

You can now build a prompt from five parts, choose its type, and record it as a card a colleague can run. Chapter 5 adds the strategies that raise output quality, collected in the Prompt Strategy Checklist, and the Output Checklist for judging what comes back. Your cards gain the Strategies used field that this chapter left blank.
