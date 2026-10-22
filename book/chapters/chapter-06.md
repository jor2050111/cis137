# Chapter 6: Iterative Refinement

The owner of a small landscaping company, whom you may have met in Chapter 4, asks a chat assistant for a client email. The first draft is close, so she types "make it better." The second draft is longer and friendlier, and it promises something her crews do not do. She tries twice more. Twenty minutes later she has four drafts and no way to say which one was best, or why. The next month she starts from a blank chat.

Chapter 4 named the five parts of a prompt, and Chapter 5 gave you the Prompt Strategy Checklist and the Output Checklist. This chapter turns those tools into a method. You will use artificial intelligence (AI) the way a careful practitioner improves anything: decide what good looks like before the first try, change one thing at a time, and write down what happened. A first draft that misses is normal. A tenth draft you cannot explain is the real problem.

You will write criteria before you run a prompt, then run the refinement loop and keep a Refinement Log. You will learn when a follow-up in the same conversation fits and when a fresh run does. Then you will test one prompt in two tools and decide when a prompt is good enough. You will finish by documenting the result so a colleague can use it. At Copperwind, that last step completes the shared prompt library Mei Lin asked for. Deskside technicians and Priya Sharma's outreach volunteers will both use it, and Priya's newsletter prompt is the card that finishes it.

## Module Overview 🧭

* **Estimated time:** 5-6 hours
* **Prerequisites:** Chapters 4 and 5 (the five parts of a prompt, the prompt card, the Prompt Strategy Checklist, and the Output Checklist), plus the prompt log from Chapter 1
* **Deliverables:** Skills Lab 6A deliverable (prompt library v3), Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **6.1 (Apply):** Construct evaluation criteria for a prompt's job before the first run, and score each version of the prompt against them (Section 6.1)
* **6.2 (Analyze):** Investigate a weak prompt through the refinement loop, changing one thing per version, and relate each gain or loss in the Refinement Log to the change that caused it (Section 6.2)
* **6.3 (Evaluate):** Judge when a prompt is good enough from its scores in fresh runs and in two tools, and publish it in a library a colleague can reuse (Sections 6.3-6.4)

### This chapter aligns with the following Course Learning Outcomes

* **CLO 3 (Apply):** Demonstrate effective prompting strategies to improve AI outputs.
* **CLO 1 (Evaluate):** Evaluate AI-generated responses for accuracy.

---

## 6.1 Criteria First

First drafts fail for three reasons. The prompt leaves out something you know, so the model fills the gap with likely text (Chapter 2). The prompt asks for something the model handles poorly, and a strategy from the Prompt Strategy Checklist would help. Or you never decided what a good draft looks like, so no draft can pass. The first two you fix in the prompt. The third you fix before you write the prompt at all.

"Make it better" shows the third failure. Better how? Shorter, warmer, more accurate? The model cannot tell, so it guesses, and you cannot score its guess either. You need a target that both of you could hit.

That target is a set of **evaluation criteria**: the checkable tests you write before the first run to decide whether an output does its job. "Sounds professional" is a hope. "Under 120 words" is a criterion, because you can count. So is "the 60-day exception appears," because you can find it or not.

### What Makes a Criterion Checkable

Good criteria share four traits:

* **Checkable:** each one passes or fails on evidence you can point to, such as a count, a quote, or a yes or no.
* **Tied to the job:** each one comes from what the reader needs, not from what a nice draft usually has.
* **Few:** three to six is enough, because ten criteria turn every run into an audit.
* **Ranked:** the must-pass criteria, the ones the output cannot ship without, are marked.

The Output Checklist from Chapter 5 gives you a starting set: did it do the task, right shape, every claim traceable, nothing added, tone fits the audience. Make each one specific to the job. "Right shape" becomes "under 120 words, no blanks to fill." "Every claim traceable" and "nothing added" become "every fact matches the fact list, with no added claim." That last kind of criterion is your accuracy check, and every Criteria sheet you write should carry one.

Why before the first run? A draft pulls your standards toward itself. Researchers who watched people grade AI output named the effect criteria drift: grading outputs helps people define criteria, so the criteria shift as they read (Shankar and others, 2024, in Further Reading). Some drift is learning, so you may change a criterion later. Write the change down as a criteria change, with the date and the reason. Never edit the criteria quietly so that the latest draft passes.

### The Criteria Sheet

The landscaping owner from the opening tries again, this time with a plan. She fills a Criteria sheet (`criteria-sheet-template.md` in this chapter's data pack) before she sends anything. Her job is an email telling residential clients that their irrigation timers switch to the winter schedule on November 1.

| # | Criterion | How she checks it | Must pass? |
| --- | --- | --- | --- |
| 1 | The body runs under 120 words | Count from the greeting through the last line before the sign-off | Yes |
| 2 | Every fact matches the fact list, with no added claim about the service. Greetings and courtesy lines are allowed. | Mark each sentence against the facts in the prompt, skipping greetings and thank-yous | Yes |
| 3 | The new-plantings exception survives | Find the 60-day line | Yes |
| 4 | Ready to send, with no blanks or placeholders | Look for square brackets | Yes |
| 5 | Plain words for a homeowner | No term a client would have to look up | No |

Her good enough line reads: "All four must-pass criteria pass in a fresh run and a re-run." Here is her version 1:

```text
You are the office manager at a small landscaping company in Mesa, Arizona. Write an email to our residential clients about the switch to our winter watering schedule. Facts: On November 1, we switch every client's irrigation timer to the winter schedule. Your crew will make the change at your regular monthly visit, so you do not need to do anything. Plants that went in during the last 60 days stay on the summer schedule until your crew lead checks them. Questions go to the office at 480-555-0163. Keep it friendly.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
**Subject:** Your winter watering schedule starts November 1

Hi there,

Cooler mornings are on the way, and your lawn and plants need less water than they did this summer. On November 1, we switch every client's irrigation timer to our winter schedule.

**You don't need to do anything.** Your crew will make the change at your regular monthly visit.

One exception: any plants that went in during the last 60 days stay on the summer schedule until your crew lead checks them. Young plants are still building roots, so they get a little extra care before they move to the winter schedule.
[...]
Warmly,
[Your name]
Office Manager
[Company name]
480-555-0163
```

She scores it against the sheet, one criterion at a time, with the evidence:

| # | Criterion | Result | Evidence |
| --- | --- | --- | --- |
| 1 | Under 120 words | Pass | 115 words |
| 2 | No added claim | Fail | "Cooler mornings are on the way" and "Young plants are still building roots" are not in the facts |
| 3 | Exception survives | Pass | The 60-day line is there |
| 4 | Ready to send | Fail | "[Your name]" and "[Company name]" |
| 5 | Plain words | Pass | No jargon |

Score: 3 of 5, with two must-pass criteria failed. The added reasons may even be true. That is not the test. Nobody at the company said them, and the email goes out under the company's name. Without criterion 2 written down first, those friendly lines would read as polish.

### Try It Yourself 6.1: Criteria Before the First Run 🛠️

**Predict:** Pick a short writing job you have this week, such as a reminder, a reply, or a post, with nothing private in it. Fill `criteria-sheet-template.md` with three to five criteria and mark the must-pass ones. Before you write the prompt, predict which criterion your version 1 will fail.

**Run:** Write version 1 using the five parts of a prompt and send it in a fresh conversation. Score every criterion pass or fail, with a quote or a count as evidence. Paste the prompt, the response, and your filled Criteria sheet into your prompt log. The Criteria sheet is the artifact you keep: it travels with this prompt into your library.

**Explain:** Was your prediction right? In 1-2 sentences, name the criterion that was hardest to check, and rewrite it so a classmate could check it the same way you did.

### Quick Check 6.1 ✅

1. A public library branch wants a prompt for overdue-book notices, and the clerk's only criterion is "sounds nice." Rewrite it as two checkable criteria, and say how you would check each one.
2. Use the landscaping criteria to score this sentence from a draft: "Our crews will switch your timer on November 1, and this month's visit is free." Name the criterion it fails and quote the evidence.
3. A coworker writes her criteria after reading three drafts, then picks the draft that matches them best. Analyze what her scores can no longer tell her, and say what her Criteria sheet should show instead.

---

## 6.2 The Refinement Loop and the Log

With criteria in hand, improving a prompt becomes a loop instead of a hunch. The **refinement loop** is the cycle for improving a prompt, and it runs in seven steps:

1. **Criteria:** write them before the first run.
2. **Run:** send the prompt.
3. **Score:** check the output against every criterion.
4. **Diagnose:** name the criterion that failed and its cause, and look in the Prompt Strategy Checklist for the fix.
5. **Change one thing:** edit one part of the prompt.
6. **Run again:** send the new version and score it.
7. **Stop when the criteria are met:** the good enough line on your Criteria sheet tells you when.

Each pass through the loop makes a new **version**: a numbered, saved copy of a prompt that differs from the one before it by a recorded change. The record is a **refinement log**, one row per version. Your Refinement Log (`refinement-log-template.md`) has four fields: version, the one change, score against the criteria, and keep or revert.

### Two Versions, One Change Each

The landscaping owner diagnoses version 1. The placeholders appeared because the prompt never said who signs the email, so the model left blanks. That is mostly missing context, though a Constraints line could fix it too. Version 2 adds one sentence at the end: `Sign it "The Office Team" and leave no blanks or placeholders to fill in.`

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Hello,

As the weather cools, your landscape needs less water. On November 1, we switch every client's irrigation timer to our winter schedule. This keeps your plants healthy and your water bill lower through the cooler months.
[...]
One exception applies. Plants that went in during the last 60 days stay on the summer schedule until your crew lead checks them. New plants have shallow roots and still need the extra water, so we want to see them in person before we cut back.
[...]
Warmly,
The Office Team
```

The change fixed its target. No placeholder remains, so criterion 4 passes. But the body grew to 128 words, and the model added more reasons than before: a lower water bill and shallow roots. Criterion 1 now fails, and criterion 2 still fails. The score is 3 of 5 again, the same total with a different set of failures. Here a total alone would mislead you, so the log names what failed.

Should she keep version 2? Yes. The change did what it was meant to do, and the new length failure comes from the added reasons, which criterion 2 already targets. Her diagnosis for version 3: the model treats "friendly" as a license to explain. The checklist strategy is negative constraints and guardrails. Here is version 3, which adds one sentence. Send the prompt without the [Step] lines:

```text
[Step 1: say whose voice the email speaks in]
You are the office manager at a small landscaping company in Mesa, Arizona.
[Step 2: name the job and the reader]
Write an email to our residential clients about the switch to our winter watering schedule.
[Step 3: hand over every fact the email may use]
Facts: On November 1, we switch every client's irrigation timer to the winter schedule. Your crew will make the change at your regular monthly visit, so you do not need to do anything. Plants that went in during the last 60 days stay on the summer schedule until your crew lead checks them. Questions go to the office at 480-555-0163.
[Step 4: set the tone and who signs, the version 2 change]
Keep it friendly. Sign it "The Office Team" and leave no blanks or placeholders to fill in.
[Step 5: forbid what version 2 added, the version 3 change]
Use only the facts above, and do not add reasons, benefits, or watering advice of your own.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

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

The body runs 76 words. Every fact matches the list, the exception survives, and nothing needs filling in. The two closing lines are courtesy, which criterion 2 allows, not claims about the service. Score: 5 of 5. Her Refinement Log now reads:

| Version | The one change | Score against the criteria | Keep or revert |
| --- | --- | --- | --- |
| v1 | First version | 3 of 5 (fails 2 and 4) | Keep as the base |
| v2 | Added who signs, and no placeholders | 3 of 5 (fails 1 and 2) | Keep: criterion 4 fixed |
| v3 | Added "use only the facts above," with no reasons or advice | 5 of 5 | Keep |

Each row names one change, so each gain belongs to one edit. Version 3 cut the length without a word limit, which suggests the length came from the added reasons. A log with one change per row lets you see that. Her good enough line also asks for a re-run, so she sent version 3 again in a fresh conversation, and it came back at 71 words with all five criteria met.

### Why One Change at a Time

Chapter 2 showed that the same prompt gives different answers from one run to the next. So a version can score better by chance, and a single run is a weak test of a small gain. Two habits protect you. Change one thing per version, so a real gain has one cause. When a gain is small or a score sits right at a limit, run the same version again in a fresh conversation before you mark it keep.

### Try It Yourself 6.2: One Change, Logged 🛠️

**Predict:** Take your version 1 and its scores from Try It Yourself 6.1. Pick the failed criterion that matters most and the strategy from the Prompt Strategy Checklist that targets it. Predict whether your one change will fix that criterion without breaking another.

**Run:** Write version 2 with one change, send it in a fresh conversation, and score it against the same Criteria sheet. Fill the v1 and v2 rows of `refinement-log-template.md`, including keep or revert. The two log rows are the artifact you keep.

**Explain:** Did any criterion move that you did not target? In 1-2 sentences, explain why, the way version 2's new length failure traced back to the added reasons.

### Fix It 6.1: The Version That Worked 🔧

A volunteer coordinator for a youth soccer league texts parents about schedule changes. Her criteria: under 50 words so it reads at a glance, all four facts, and the rule for switching back. Her version 1 covered the facts and ran 72 words. Version 2 passed, and she moved on.

**Symptom:** A month later she wants a warm greeting back for a holiday tournament text, and she cannot tell what it will cost her. She opens her version 2 prompt and its result:

```text
Write a text message to the parents in our youth soccer league. Keep it under 45 words. Facts: Because of the heat forecast, every Saturday game this weekend starts at 7 a.m. instead of 9 a.m. Fields and opponents stay the same. Each player should bring two full water bottles. If the forecast drops below 100 degrees by Friday at 6 p.m., we will switch back to 9 a.m. and text you again. No greeting and no sign-off.
```

Here is the response it gave (captured from a chat assistant, October 2026):

```text
Heat alert: This Saturday's games all start at 7 a.m., not 9 a.m. Fields and opponents are unchanged. Please send each player with two full water bottles. If Friday's 6 p.m. forecast falls below 100 degrees, we'll return to 9 a.m. and text you.
```

It ran 44 words with every fact in place, so it passed all three criteria. (The prompt asks for under 45 words to leave a small buffer under her 50-word criterion.) Her log row:

| Version | The one change | Score against the criteria | Keep or revert |
| --- | --- | --- | --- |
| v2 | Added "Keep it under 45 words" and "No greeting and no sign-off" | 3 of 3 | Keep |

**Diagnose:** Before you touch the prompt, read the row against the rule for a version, and name in one sentence the question about next month's text that this row cannot answer.

**Repair:** The row holds two changes, so the gain belongs to both and to neither. She cannot tell whether dropping the greeting saved the words or the limit did. The repair goes back to version 1 and adds only one of the two lines, "No greeting and no sign-off." It changes one thing. She calls it version 2a and runs it fresh:

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Heat forecast: all Saturday games this weekend move from 9 a.m. to 7 a.m. Fields and opponents stay the same. Please send each player with two full water bottles.

If the forecast drops below 100 degrees by Friday at 6 p.m., we'll switch back to 9 a.m. and text you again.
```

**Verify:** Count it: 51 words, two over the limit, since under 50 means 49 at most. A second fresh run of version 2a came back at 55. So dropping the greeting cut most of the length, from 72 to the low 50s, and the word limit carried the rest. Her old version 2 is version 2a plus the limit, so she relabels it version 2b, and its 44-word run becomes the next row. Now the log has two rows with one change each. Version 2a's greeting ban takes about 20 words off, and version 2b's word limit brings the text under 50. Next month, if she adds a greeting back, she knows the limit has to absorb it. Her one-change row could answer the question the two-change row could not.

### Follow-Ups or Fresh Runs

Everything so far used fresh runs, a new conversation for each version. The other way to refine is a follow-up: a new message in the same conversation that asks the model to revise what it just wrote. Follow-ups come in four common moves: narrow ("Shorter, under 60 words."), expand ("Add one sentence on parking."), correct ("Take out anything I did not give you."), and restyle ("Make it sound more casual.").

Here is one conversation with a community college's cybersecurity club officer. The first message asked for a 100-word post with four facts: Thursday, September 10, 3:30 p.m., Room B-114, no experience needed, and teams cracking a practice password list on club laptops. The first draft added lines such as "We'll supply the laptops and the challenge." Then came two follow-ups:

```text
Shorter: under 60 words. And take out anything I did not give you.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Join the Cybersecurity Club!

Our first meeting is Thursday, September 10, at 3:30 p.m. in Room B-114. No experience needed. Teams will try to crack a practice password list on club laptops.

Come see how it works.

(Word count: 38)
```

```text
Good. Now make it sound more casual, for a social media post.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Cybersecurity Club kicks off Thursday, Sept. 10, at 3:30 p.m. in Room B-114! 🔐

No experience needed. Teams will try to crack a practice password list on club laptops.

Come hang out and give it a shot.
```

Follow-ups are fast, and the model can see exactly what to cut. (It also miscounted: the post has 37 words, not 38.) The catch is that the final post depends on all three turns. "Make it sound more casual" alone does not say what to keep, so nobody can put that turn on a prompt card and get this post back. To keep the win, count the conversation as version 1, fold its follow-ups into one prompt as version 2, and run that fresh:

```text
Write a casual social media post, under 60 words, inviting students to the first meeting of our community college's cybersecurity club. Facts: Thursday, September 10, at 3:30 p.m. in Room B-114. No experience needed. At the first meeting, teams will try to crack a practice password list on club laptops. Use only these facts.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Cybersecurity Club kicks off Thursday, Sept. 10 at 3:30 p.m. in Room B-114! 🔐

No experience needed. We'll split into teams and try to crack a practice password list on club laptops.

Come curious, bring a friend, and see how fast weak passwords fall.

#CybersecurityClub
```

The fresh run kept the facts and passed the length. Like the conversation's final post, it added an invitation line and an emoji, and it also added a hashtag. Turn 2 cut additions the model could see, and turn 3's restyle let new ones back in. A folded prompt has to block them before they appear. Use each method for what it does well:

| Method | Fits when | Watch for | What the log records |
| --- | --- | --- | --- |
| Follow-ups in one conversation | You are exploring, or polishing a one-off message | The result depends on every earlier turn | Every turn, in order |
| Fresh run for each version | The prompt will go on a card and be reused | Slower, and the prompt must carry everything | Each version's full prompt |

The rule for the library: explore in follow-ups if you like, then fold the winning change into the prompt and confirm it with a fresh run before it goes on a card.

### Try It Yourself 6.3: Fold It Back 🛠️

**Predict:** The folded club prompt, version 2, added a claim the facts never gave ("see how fast weak passwords fall"), plus an emoji and a hashtag. You will close the gap at the end of the prompt with one sentence from the Constraints part. Predict whether one sentence can block all three without losing the casual tone.

**Run:** Fill the gap from this chapter's diagnosis, then send the prompt in a fresh conversation:

```text
Write a casual social media post, under 60 words, inviting students to the first meeting of our community college's cybersecurity club. Facts: Thursday, September 10, at 3:30 p.m. in Room B-114. No experience needed. At the first meeting, teams will try to crack a practice password list on club laptops. Use only these facts. ____
```

Score the result against four criteria: under 60 words, all four facts, no added claim (greetings and invitations are allowed), and a casual tone. Log it as version 3 in a Refinement Log row, with your sentence as the one change.

**Explain:** Compare your run with the sample below. In 1-2 sentences, explain whether your sentence did better or worse, and what the next version's one change would be.

Compare your run with the response one chat assistant gave in October 2026, when the gap held "Do not add hashtags, emoji, or any line that is not one of the facts.":

```text
Cybersecurity club's first meeting is Thursday, September 10, at 3:30 p.m. in Room B-114. No experience needed. Teams will try to crack a practice password list on club laptops. Come join us!
```

The hashtag, the emoji, and the added claim are gone, and the post runs 32 words. "Come join us!" is an invitation, which the criteria allow. The miss is the tone: the post now reads like a notice, not a casual post, so it scores 3 of 4. One constraint can cost another quality, and the log is where you see the trade.

### Quick Check 6.2 ✅

1. A log row reads "v4 | changed the role and cut the example | 4 of 5 | keep." Analyze what the row can and cannot tell a teammate, then rewrite it as two rows.
2. You are polishing a one-time thank-you note to a mentor. Decide whether to refine with follow-ups or with fresh runs, and justify your choice in two sentences.
3. A new version scored one criterion higher than the last, in a single run, and its word count sits one word under the limit. Decide what you do before you mark it keep, and explain why.

---

## 6.3 One Prompt, Two Tools

A prompt card records its last run with the tool and the date, because a prompt that works in one tool can behave differently in another. A team rarely uses one tool. A technician may run a card in whichever chat assistant is open, so the card should say what to expect. Researchers have measured how fragile this can be. One 2023 study found that small formatting changes to a prompt moved one model's accuracy by up to 76 points on few-shot tasks. How well a format worked for one model said little about how it would work for another (Sclar and others, in Further Reading).

### A Fair Comparison

A comparison is fair only when the prompt is the one thing that stays the same. Follow five rules:

* **Same prompt,** word for word. Rewording it "to suit" a tool means you are testing two prompts.
* **Same input,** pasted the same way.
* **Fresh conversations** in both tools, so nothing earlier steers either one.
* **Same day,** because tools change without notice.
* **Same criteria,** scored the same way, and a second run of each when a result is close.

The Two-Tool Comparison sheet (`two-tool-comparison-sheet.md`) holds the result: the scores side by side, the differences worth noting, and the lines that go on the card.

### The VPN Card in Two Tools

Here is a Deskside card from `prompt-library-v2-starter.md`, the VPN connection failure reply, sent with its example input. The card's bracket labels were left out, and Tool A's run comes first:

```text
You are a Deskside support technician at a managed IT services company. The reader is an office worker at a client company, not a technical person. Write a reply to the ticket below that walks them through our first checks for a VPN connection failure. Use only these checks, in this order: 1. Open any website to confirm the internet works without the VPN. 2. Quit the VPN app completely, open it again, and sign in. 3. If it still fails, reply to this email with the exact words of the error message. Ticket: "The VPN won't connect from home. It just spins and then says something failed. I need the shared drive today." Format: under 100 words, plain text, a one-line greeting, the three checks as numbered steps, and a sign-off from "Deskside Support." Do not add any other troubleshooting steps, and do not promise when it will be fixed.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Hi,

Let's start with three quick checks.

1. Open any website, such as a news site. This confirms your home internet works without the VPN.
2. Quit the VPN app completely, open it again, and sign in.
3. If it still fails, reply to this email with the exact words of the error message.

Those exact words help us see what went wrong.

Deskside Support
```

Tool B, a second model, same prompt, same day:

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Hi there,

Thanks for reaching out. Let's start with three quick checks.

1. Open any website, such as a search page, in your browser. This confirms your internet works without the VPN.
2. Quit the VPN app completely, then open it again and sign in.
3. If it still fails, reply to this email with the exact words of the error message.

Deskside Support
```

The comparison sheet, filled from the card's Good output looks like line:

| Criterion | Tool A | Tool B |
| --- | --- | --- |
| The three checks, in order, and no others | Pass | Pass |
| Under 100 words | Pass (65) | Pass (64) |
| No promised fix time | Pass | Pass |
| Total | 3 of 3 | 3 of 3 |

Both passed, and the differences are small. Each tool added an example website to check 1. Tool A added a closing reason line, and Tool B added a thank-you opener. None of those breaks a criterion, but each one is an addition, so the card's Notes should tell a technician to read check 1 before sending. One comparison is one data point. Here the two models agreed closely. These two share a vendor, so that may say as much about them as about the prompt. A looser prompt leaves each model more gaps to fill its own way.

!!! note "Tool check (verified October 2026)"
    The Tool A and Tool B samples above came from two models made by the same vendor, through the same test setup, not two chat apps. Tools from different vendors on your course roster may differ more than these two did, which is why the sheet asks for your own runs. Your syllabus names the roster.

### Try It Yourself 6.4: Same Card, Two Tools 🛠️

**Predict:** Choose one card, from your own library or from `prompt-library-v2-starter.md`. Predict which of its Good output looks like criteria is most likely to differ between two tools, and why.

**Run:** Send the card's prompt with its example input, word for word, in a fresh conversation in each of two tools from your roster on the same day. Score both runs and fill `two-tool-comparison-sheet.md`. Then write the card's Last run line and one Notes line for a teammate who uses the other tool. The filled sheet and the two card lines are the artifacts you keep.

**Explain:** Was your prediction right? In 1-2 sentences, explain whether the difference you found came from the tool or from a gap the prompt left open.

### Quick Check 6.3 ✅

1. A teammate compares two tools but rewords the prompt slightly for the second one "so it understands." Explain why the comparison no longer tests the tools, and what the teammate should do instead.
2. Tool A passes all four of a card's criteria. Tool B adds a claim in one run: a promise to call the client back. Decide what goes on the card's Last run and Notes lines, and whether you run anything again first.

---

## 6.4 Good Enough, Documented: the Library a Colleague Can Use

A prompt can always be a little better, and that is the trap. **Good enough** is the point where a prompt meets every must-pass criterion in a fresh run and a re-run, and another version is unlikely to repay the time it costs. Past that point, a quick human edit beats another version.

### When to Stop

Stop the loop when one of these is true:

* **The criteria are met** in a fresh run and in a re-run. That is the normal finish.
* **Two versions in a row gained nothing.** The prompt may be as good as this tool gets on this job.
* **The remaining fix is faster by hand.** The landscaping version 3 ends with "We're always happy to help." If the owner dislikes the line, deleting it takes three seconds. Version 4 would take ten minutes.
* **Prompting cannot fix the failure.** The facts are missing, or the job needs a decision a person must make. Say so and stop, which is the fifth habit in the fluency contract: know when to say no. "Perfect" is not on the list, because perfect has no criteria.

### From Prompt to Template

A prompt you reuse has two kinds of text: the parts that stay fixed and the parts that change each time. Turn the changing parts into slots, written in braces. The VPN card's ticket became `{ticket text}`. A newsletter prompt might take `{topic}` and `{facts for this issue}`. The fixed text is what you refined and logged. The slots tell a colleague exactly what to fill in. If they edit outside the slots, they are running a new version, and it deserves its own log row.

### What Library v3 Holds

Mei Lin's ask was a library the Deskside team can share, so a technician's good prompt does not live only in that technician's chat history. Priya's outreach volunteers will run cards from it too, so v3 is Copperwind's shared prompt library, with two kinds of user. A card alone is not enough for either group. Prompt library v3 holds three things:

* **The cards,** each with its Strategies used line filled
* **A Refinement Log for each card** you refined, so a colleague can see what was tried and why
* **A README,** the first page a colleague reads. It says what the library is for, who keeps it, and which cards serve Deskside technicians and which serve outreach volunteers. It also covers how to run and check a card, what never goes into a prompt, and how to propose a change

The template `library-readme-template.md` gives you those sections. The hard part is writing it for someone who was not there.

### The Cold-Read Test

How do you find what a stranger would not understand? Ask a fresh conversation to read the card cold, as a new teammate would. Here is that test run on the shared mailbox card, pasted exactly as it ships in `prompt-library-v2-starter.md`, without the sample output below it. Send the prompt without the [Step] lines:

````text
[Step 1: name the reader and the condition they work under]
A new Deskside technician will use the prompt card below with no one to ask.
[Step 2: ask for questions, not a rewrite]
List every question they would need answered before they could run the prompt and judge the result.
[Step 3: hold the tool to what the card leaves out]
Only list questions the card does not already answer, and do not rewrite the card.
[Step 4: set a shape you can sort]
One line per question, most important first, no more than six.

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

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
1. Who is "Deskside Support" signing off as: is the sign-off a team name only, or should the technician add their own name or ticket number?
2. What does the technician paste for {ticket text}: the whole thread, only the latest message, or the requester's name and email too?
3. Can the technician trust the model's check of the ticket? What do they do when the wording is vague, such as "my manager said it's fine" (verbal, not written) or a mailbox described but not named?
[...]
6. Does the reply go out as written, or must the technician check it against the three criteria first? If it fails, which part do they fix (edit the reply or rerun the prompt)?
```

Sort each question by where its answer belongs. Questions 2 and 3 are card fixes: say what goes in the slot, and say what counts as written approval. Question 3 is the sharpest, because a requester who writes "my manager said it's fine" could slip past the rule. Questions 1 and 6 are README fixes. How a technician signs a reply and what happens after the draft apply to every card, so they belong on the library's first page. (The two cut questions ask whether the reply should still list example mailboxes when only the approval is missing, and who the manager is when the ticket does not say. Both are card fixes.)

Treat the list as leads, the way Chapter 3 treated a chat assistant's research. The model predicted questions a newcomer might ask. A real colleague who tries the card is the better test, and the cold read gets you to that test with fewer gaps.

### Try It Yourself 6.5: The Cold Read 🛠️

**Predict:** Pick one card, from your own library or from `prompt-library-v2-starter.md`. Predict the first question a new teammate would ask before using it.

**Run:** Send the cold-read prompt above with your card pasted in place of the shared mailbox card. Mark each question CARD (fix it on the card) or README (it belongs on the library's first page). Write one new Notes line for the card and one numbered step for the "How to use a card" section of `library-readme-template.md`. The new Notes line and the README step are the artifacts you keep.

**Explain:** Did the list open with the question you predicted? In 1-2 sentences, explain why a cold read from a model is a lead and not proof that the card is clear.

### Quick Check 6.4 ✅

1. The landscaping version 3 passed all five criteria, but the owner dislikes "Thank you for being part of our community of clients." Decide whether she should run version 4, edit by hand, or stop, and justify your decision with the stop rules.
2. A cold read of a printer-offline card returns "Should I send the reply or have a senior tech review it first?" Decide whether the answer goes on the card or in the README, and write the line.
3. Turn the folded cybersecurity club prompt into a template a different club could reuse. Name two slots, and say which sentence must stay fixed and why.

---

## 6.5 Summary and Retrieval 💡

### Key Concepts

* First drafts fail when the prompt leaves out what you know, asks for something the model handles poorly, or aims at a target nobody wrote down. Evaluation criteria fix the third failure. Write three to six checkable criteria before the first run, mark the must-pass ones, and include one accuracy test.
* The refinement loop runs Criteria, Run, Score, Diagnose, Change one thing, Run again, and Stop when the criteria are met. Each pass makes a numbered version.
* The Refinement Log records each version, the one change, the score against the criteria, and the decision to keep or revert. Score each criterion by name, because the same total can hide different failures.
* Change one thing per version so each gain has one cause. Runs vary by chance, so re-run a close result before you credit the change.
* Follow-ups in one conversation are fast for exploring. A card needs a prompt that works alone, so fold the winning change in and confirm it with a fresh run.
* Compare tools fairly: same prompt word for word, same input, fresh conversations, same day, same criteria. Record what to expect on the card.
* A prompt is good enough when its must-pass criteria pass in a fresh run and a re-run, and the next version would cost more than a quick edit. Library v3 holds the cards, their logs, and a README a colleague can follow, tested with a cold read.

### Key Terms

See course glossary for full definitions

* evaluation criteria (Section 6.1)
* refinement loop, version, refinement log (Section 6.2)
* good enough (Section 6.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. List the seven steps of the refinement loop in order.
2. Name the four fields of a Refinement Log row, and explain why the second field holds exactly one change.
3. Explain when a follow-up in the same conversation fits and when a fresh run fits, and what you do before a follow-up's win goes on a card.
4. From Chapter 4: Name the five parts of a prompt, and name the prompt card field that holds the full prompt with those parts labeled.
5. From Chapter 2: Name the three things that shape every response, and explain which one makes a single run a weak test of a prompt change.

---

## 6.6 Skills Lab 6A: The Finished Prompt Library

**Goal:** Refine Priya Sharma's newsletter prompt against written criteria across at least three logged versions, and compare the final version in two tools. Then deliver prompt library v3, Copperwind's shared prompt library, with a README that Mei Lin's Deskside technicians and Priya's outreach volunteers can follow.

**Starter files:** Provided files in `assets/code/chapter-06/` from the course data pack: `skills-lab-6a-worksheet.md` (your answer file) and `priya-newsletter-brief-2.txt` (Priya's request). The sheets you fill are `criteria-sheet-template.md`, `refinement-log-template.md`, and `two-tool-comparison-sheet.md`. The formats are `prompt-card-template.md` and `library-readme-template.md`, and `prompt-library-v2-starter.md` holds three finished Deskside cards. Use your own library if you built one in Chapter 5, or the starter. Download the data pack from Canvas, extract it, and work at the extracted `cis137` root. Open each file in any text editor and never retype its contents. The lab files are fictional, so you may paste them into a chat assistant once your privacy plan allows it. You first met Copperwind in Chapter 1, and this lab gives you everything it needs, so you do not need any earlier file.

### Part 1: Foundation (Aligns with Objective 6.1)

Work in `skills-lab-6a-worksheet.md`, which has a space for every task below. Read `priya-newsletter-brief-2.txt` in full before you write anything.

1. Before you send any prompt, write your privacy plan in two columns: what from the brief may go into a tool, and what stays out of every prompt. Give the reason for each item that stays out.
2. Fill `criteria-sheet-template.md` for Priya's item before your first run. Write four to six criteria from the brief, each with how you will check it, and mark the must-pass ones. Include at least one accuracy criterion (every fact and number traces to the brief) and one for the caveat Priya says must survive. Then write your good enough line.
3. Write version 1 using the five parts of a prompt, labeled in brackets. Send it in a fresh conversation, and paste the prompt and the response with the tool and the date. Score every criterion with evidence (a quote or a count), and log the result as v1 in `refinement-log-template.md`.

### Part 2: Application (Aligns with Objectives 6.1 and 6.2)

1. Run the refinement loop for at least two more versions, each in a fresh conversation, each changing one thing. For each version, write the diagnosis first: the criterion that failed and the strategy from the Prompt Strategy Checklist you chose. Then paste the prompt and the response, score every criterion, and fill the log row with keep or revert.
2. In the conversation of your best version so far, send one follow-up (narrow, expand, correct, or restyle). Paste the follow-up and the response, and name the move. Decide whether its gain belongs in the prompt. If it does, fold it in as your next version, run that version fresh, and log it. If it does not, explain why in one sentence.
3. Re-run your best version in a fresh conversation and score it. State whether it met your good enough line both times. If it did not, run and log another version. Also re-run the version with your biggest gain if it is not your best version. Then write the final item for Priya from your best output, list every word you changed by hand, and give the final word count.

### Part 3: Extension (Aligns with Objectives 6.2 and 6.3)

1. Run your final version in a second tool from your roster, with the same input on the same day, and fill `two-tool-comparison-sheet.md`. State which tool goes on the newsletter card's Last run line and what its Notes must warn a volunteer about.
2. Write the newsletter card in the `prompt-card-template.md` format from your final version. Replace the parts that change each month with slots in braces, and fill Strategies used with names from the Prompt Strategy Checklist.
3. Assemble prompt library v3: the three cards from `prompt-library-v2-starter.md` (or your own v2 cards), your newsletter card, and your Refinement Log. Fill `library-readme-template.md` so a Deskside technician or an outreach volunteer who never saw your work could pick a card, run it, check it, and propose a change. Run the cold-read test from Section 6.4 on your README, with "library README" in place of "prompt card" and "use the library" in place of "run the prompt". Paste the prompt and the response, and make at least one fix it found.
4. Write a note to Mei Lin (100 to 150 words). Say what "good enough" meant for the newsletter prompt, which version you stopped at and why, and the log evidence behind that choice. Then name the card in the library her team should re-run first, and why.

### Questions & Analysis 🤔

Answer both questions in the worksheet's final section. These answers carry significant rubric weight.

1. Find the version in your Refinement Log with the biggest gain. Quote its row and the row before it from your log. Explain how you know that the one change caused the gain and not chance, using your Part 2 Task 3 re-run, and name any criterion the change made worse.
2. Using your Two-Tool Comparison sheet and your last two log rows, argue whether the newsletter card is good enough to publish in the library. Name the criterion that decided it, and the one result in a future run that would send you back into the loop.

**Submission:** Submit your completed worksheet as one file named `skills-lab-6a-lastname.md`. Keep every answer under its task heading, with your filled sheets, your card, and your library v3 pasted into their sections. Include every prompt you sent, the tool and date, and every response you received, pasted exactly, with your Questions & Analysis answers clearly labeled at the end. Keep a copy of your library v3 for yourself. It is a working tool you can keep using.

### Rubric: Skills Lab 6A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria, five
levels from Mastery to Not Evident. The criteria are Technical
Accuracy and Efficiency, Output Quality, Documentation Quality, and
Analysis, Interpretation, and Response to QUESTION(s). The criteria
and levels are the same everywhere. Your instructor sets the point
values in your course. Check the syllabus and the Canvas rubric
attached to this lab for the values that apply to you.

---

## 6.7 Review Questions 🔄️

1. **Understand:** Explain to a coworker, in no more than three sentences, why typing "try again" is not a step in the refinement loop.

2. **Apply:** A dental office's front desk wants a prompt that drafts appointment-confirmation texts from the day's schedule notes. Write four evaluation criteria, mark two as must-pass, and write the good enough line.

3. **Analyze:** A neighborhood bakery owner's log for a daily-specials post has four rows. Version 1 scored 3 of 5. Version 2 changed the audience line and scored 4 of 5 (keep). Version 3 added an example post and a word limit and scored 3 of 5 (keep). Version 4 cut the word limit and scored 5 of 5 (keep). Analyze which keep decisions the log supports and what is wrong with the version 3 row. Then say what the owner still cannot conclude about the example post.

4. **Evaluate:** A city recreation center's front desk lead has refined a pool-reminder text prompt through nine versions. The last four each scored 4 of 5, and every one failed the same criterion, "sounds like our center," which she cannot make checkable. Decide whether she should stop, keep going, or rewrite the criterion, and defend your decision with this chapter's stop rules. Name the one fact that would change your answer.

---

## Further Reading 📖

* [Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences (Shankar and others, 2024)](https://arxiv.org/abs/2404.12272): A study of people grading AI output. It names criteria drift, the finding that grading outputs changes the criteria people grade by. Read the abstract and the section on drift.
* [Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design (Sclar and others, 2023)](https://arxiv.org/abs/2310.11324): Shows that small formatting changes can swing results by large margins, and that the effect differs between models. It is the research case for one change at a time and for testing a prompt in more than one tool.
* [Self-Refine: Iterative Refinement with Self-Feedback (Madaan and others, 2023)](https://arxiv.org/abs/2303.17651): Researchers had a model draft, critique its own draft, and revise, and found the revised outputs preferred on average. Compare its automated loop with the human loop in this chapter, where you write the criteria.
* [The Prompt Report: A Systematic Survey of Prompt Engineering Techniques (Schulhoff and others, 2024)](https://arxiv.org/abs/2406.06608): A large survey that sorts 58 prompting techniques and defines the field's vocabulary. Use it as a reference when a technique name comes up that this book does not cover.

---

## Looking Ahead ⏩

You can now refine a prompt against written criteria, log every version, and hand a colleague a library they can trust. Part III turns the same discipline on AI output itself. Chapter 7 asks you to audit responses for accuracy and bias with a repeatable method, and your criteria and logs come with you.
