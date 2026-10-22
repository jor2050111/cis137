# Chapter 2: How Generative AI Works and Where It Fails

A charter school's office manager needs two studies for the parent newsletter. She asks a chat assistant, and in ten seconds she has a tidy paragraph, two citations, and two links. The paragraph reads well, and the citations look professional. One of the links goes nowhere, and nothing on the page tells her which one.

That gap is the subject of this chapter. Chapter 1 sorted artificial intelligence (AI) into three types and left generative AI as a closed box, which this chapter now opens. You will see what a language model does with your words, in plain terms and without math. Once you know where an answer comes from, you can predict where it will go wrong, and you can check it before anyone else relies on it.

You will trace a response back to the three things that shaped it: training data, your prompt, and chance. You will learn why a model forgets, why it gives a different answer every time, and why it can be fluent and wrong in the same sentence. Then you will turn the three passes from Chapter 1 into a method: pull the claims out, check each one against a source, and report what held. At Copperwind, a summary of a client's office move is waiting for exactly that check.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** Chapter 1 (the three types of AI, a chat assistant account, and the prompt log)
* **Deliverables:** Skills Lab 2A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **2.1 (Analyze):** Trace a response back to the three things that shaped it (training data, the prompt, and chance), and distinguish what a model knows from what it predicts (Sections 2.1-2.2)
* **2.2 (Analyze):** Classify a model's errors as fabrication, staleness, omission, or agreement under pressure, and explain why each one happens (Section 2.3)
* **2.3 (Evaluate):** Verify an AI response against a source, claim by claim, and report what held and what did not (Section 2.4)

### This chapter aligns with the following Course Learning Outcomes

* **CLO 1 (Evaluate):** Evaluate AI-generated responses for accuracy.
* **CLO 2 (Analyze):** Differentiate the major types of Artificial Intelligence (AI).

---

## 2.1 From Training Data to the Next Word

Chapter 1 defined a large language model as a deep learning model trained on huge amounts of text to predict which words come next. That one sentence explains most of what you will see a chat assistant do, good and bad. This section unpacks it in three steps: what the model learned, what it does with your prompt, and what it never does at all.

### What the Model Learned

A language model starts as a neural network with no knowledge at all. Its builders feed it training data: books, articles, websites, code, and other text, far more than a person could read in many lifetimes. The model reads a stretch of text, guesses the next word, checks the guess against the real next word, and adjusts its connections a tiny amount. Then it does that again, billions of times.

Nobody tells the model a single fact, so it ends up with patterns instead. It learns that "Phoenix" often appears near "Arizona," that a question is usually followed by an answer, and that a help desk ticket gets closed for a short list of common reasons. The patterns live in the strengths of the connections between its layers, the layers that pass signals from one to the next. They do not live in a list of facts the model can look up.

A raw model trained this way only continues text, so to turn it into a chat assistant, its builders train it a second time. **Fine-tuning** is that extra round of training on a narrower set of examples, here sample conversations and people's ratings of which answers were helpful. Fine-tuning teaches the model to answer questions, follow instructions, and sound polite. It does not give the model a fact checker.

### What It Does with Your Prompt

When you send a prompt, the model reads all of it and predicts a likely next word. It adds that word to the text and predicts the next one, and the next, until the answer is done. Every response you read was built one small piece at a time, each piece chosen because it fit the text before it.

You can watch the patterns at work in a prompt that asks for several continuations of one unfinished sentence:

```text
Finish this sentence in five different ways, one per line: "The help desk closed the ticket because"
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
The help desk closed the ticket because the user confirmed the printer was working again.

The help desk closed the ticket because no one responded to three follow-up requests.

The help desk closed the ticket because the issue duplicated an open outage report.

The help desk closed the ticket because the password reset fixed the login error.

The help desk closed the ticket because the problem belonged to the network team, who opened a new one.
```

Every ending is plausible, and none of them is about a ticket that exists. The model has never seen your help desk, so it produced the kinds of reasons that tend to follow that sentence in the text it learned from. That is prediction, and it is the model's whole job. If you asked why a specific ticket was closed, it would use the same machinery and give you a reason just as smooth.

### Knowing Versus Predicting

Here is the distinction this chapter turns on. A model "knows" something only in the sense that its training data repeated it so often that the pattern is strong. Ask what year the first Moon landing happened, and the right answer has appeared millions of times in its training text, so the prediction and the truth line up.

Ask something the training data rarely or never contained, such as the closing time of a small shop near you, and the model still predicts. It reaches for what closing times usually look like. The answer comes out in the same confident tone, because tone is a pattern too. The model has no separate signal that says "this one is a guess."

Three things shape every response you get:

* **Training data:** what the model saw often, rarely, or never
* **The prompt:** what you asked, what you supplied, and what you left out
* **Chance:** which of several likely words the model happened to pick (Section 2.2)

When a response surprises you, ask which of the three produced the surprise. That question is the start of every diagnosis in this book.

### Try It Yourself 2.1: Famous Fact, Local Fact 🛠️

**Predict:** You will ask a chat assistant two questions. Question A: "In what year did the first crewed Moon landing take place?" Question B: "What time does [a small local business you can check] close on Sundays?" Before you send either one, predict which answer is more likely to be right, and whether the assistant will sound less sure about the one it is more likely to get wrong.

**Run:** Send each question in its own fresh conversation and paste both into your prompt log with the tool and the date. Check Question A against a reference source and Question B against the business's own website, sign, or phone line. Mark each answer right or wrong, and note whether the tone of the two answers differed.

**Explain:** In 1-2 sentences, use the training data idea from this section to explain why one answer was more reliable. Then say whether the tone of the answers gave you any warning.

### Quick Check 2.1 ✅

1. A coworker says a chat assistant "looked up" the answer to her question. Using what this section says about where the patterns live, explain what the assistant did instead, in two sentences.
2. A neighborhood nonprofit asks a chat assistant for the name of its own board president, and it names someone confidently. Which of the three shaping forces most likely produced that name? Explain why the answer deserves a check before it goes in the newsletter.

---

## 2.2 Tokens, Context, and Chance

Section 2.1 said the model predicts the next word, which was a simplification. The model works in pieces of words, it sees only a limited window of text, and it picks with a little randomness. Each of those three facts explains a behavior you have probably already noticed.

### Tokens

A **token** is the unit of text a model reads and writes: a whole word, a piece of a word, a number, or a punctuation mark. Common words are often one token, while long or rare words split into several. The split depends on the model, so the example below is an illustration, not a rule:

```text
TEXT      The technician reconnected 22 workstations.
TOKENS    The | techn | ician | reconnect | ed | 22 | work | stations | .
```

Tokens explain two oddities. Models can stumble on tasks about letters, such as counting how many times a letter appears in a word, because they do not see letters the way you do. And tool limits are counted in tokens, not words or pages. When a free tier says a conversation is "too long," it is counting tokens.

### The Context Window and Why the Model Forgets

A **context window** is the amount of text, counted in tokens, that a model can consider at one time. Everything inside it counts: your messages, the model's replies, and any document you pasted. Text outside the window does not exist for the model.

That fact produces two kinds of forgetting, and the first is that a new conversation starts with an empty window. Here is a fresh conversation that opens with a question about the past:

```text
What was the last thing I asked you before this message?
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Nothing. This is the first message in our conversation, so you haven't asked me anything yet. I also can't see any earlier conversations.

If you meant to pick up something from before, tell me what it was and I'll work from there.
```

The answer is honest and correct, because yesterday's chat is not in today's window. The second kind comes from length, because a long conversation can outgrow the window. Tools handle that in different ways: some drop the oldest messages, and some squeeze them into a shorter summary. Either way, an instruction you gave at the start ("keep every reply under 100 words") can fade from view many turns later. When a long chat starts ignoring a rule, restate the rule or start a new conversation with everything it needs.

!!! note "Tool check (verified October 2026)"
    As of October 2026, some chat assistants offer a memory feature that carries notes from one conversation into the next. Some can also search the web before answering. Both change what is in the context window. Check your tool's settings to see whether either is on. The labs in this book work either way, but your prompt log should say which features were on when you ran a prompt.

### Why the Same Prompt Gives Different Answers

At each step, the model does not produce one next token. It scores every possible token by how well it fits, then picks one. Most tools add a little randomness to that pick, so a less likely token sometimes wins. One different word early on changes everything after it, because every later word is predicted from the words before it.

You saw this in Chapter 1, when the spam filter question came back in new words. Here is a creative request sent twice, each time in a fresh conversation:

```text
Suggest one name for a food truck that sells Sonoran hot dogs in Tucson. Give the name only.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Salsa Verde Dogs
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Dog Gone Sonoran
```

For a food truck name, chance is a gift, since you can run the prompt five times and pick the best one. For a fact, chance is a warning. If a factual question gets a different answer each time you ask, at most one of those answers can be right, and possibly none.

### How a Limit Shapes the Answer

Your prompt is the force you control most. A size limit is a good example, because it decides what the model keeps and what it drops. Here is one question with a tight limit:

```text
Explain why a laptop battery holds less charge as it gets older. Use no more than 25 words.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Repeated charging cycles degrade the electrodes and form resistive layers, so fewer lithium ions can shuttle back and forth, reducing the battery's usable capacity.
```

And here is the same question with room to spare, trimmed to three of its paragraphs:

```text
Explain why a laptop battery holds less charge as it gets older. Use about 150 words.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Laptop batteries are lithium-ion cells, and every charge cycle wears them down a little.
[...]
Heat speeds all of this up. So do high charge levels. Keeping a laptop plugged in at 100% on a warm desk ages the battery faster than moderate use at cooler temperatures.

The result is lower capacity and higher internal resistance. The battery holds less energy, and the laptop may shut down early under load. Most batteries keep about 80% of their original capacity after 300 to 500 full cycles.
```

The short answer kept the core cause and dropped everything else. The long answer added the role of heat and high charge levels, a habit to avoid, and a number nobody asked for: 80% after 300 to 500 cycles. Neither answer is wrong for its size. Notice the trade: the short answer omits what a user could act on, and the long one adds a statistic you would have to check before you repeated it. More words mean more claims, and every claim is one more thing to verify.

### Try It Yourself 2.2: Same Prompt, Two Runs 🛠️

**Predict:** You will send two prompts, each twice, in fresh conversations. Prompt A is creative: "Write a one-line slogan for a neighborhood bike repair shop." Prompt B is factual: "How many U.S. states border Arizona? Name them in one sentence." Predict which prompt will change more between its two runs, and whether the factual answer will change at all.

**Run:** Send each prompt twice, each time in a new conversation, and paste all four responses into your prompt log with the tool and the date. Mark what stayed the same and what changed in each pair, and check Prompt B against a map.

**Explain:** In 1-2 sentences, use this section's description of how the model picks tokens to explain the difference between the two pairs. If the factual answer changed, say what that tells you about trusting a single run.

### Try It Yourself 2.3: What a Limit Cuts 🛠️

**Predict:** You will ask "Why does a phone's Wi-Fi signal drop in some rooms of a house?" twice: once with "Use no more than 20 words" and once with "Use about 120 words." Before you send either, write down the one cause you expect both answers to name, and one detail you expect only the long answer to include.

**Run:** Send both versions in fresh conversations and paste them into your prompt log. List every cause the long answer names, then mark which ones survived in the short answer. Circle any number in either answer that you would need to check.

**Explain:** In 1-2 sentences, explain how the limit changed what the model kept, and why the cause that survived is likely the one the training data repeated most.

### Quick Check 2.2 ✅

1. A technician pastes a 40-page network manual into a chat, asks thirty questions, and notices the assistant has stopped following his first instruction to cite page numbers. Use the term context window to explain what likely happened, and give two ways he could fix it.
2. A clinic's front desk asks a chat assistant the same question about flu shot timing three times and gets three different answers. Explain what the variation shows, and say what the desk should do before telling a patient anything.
3. Your manager wants "short, complete" AI summaries. Using the battery example, explain the trade a word limit forces, and name one instruction you could add so the short version keeps what matters.

---

## 2.3 Where It Fails

Every failure in this section comes from the mechanism in Sections 2.1 and 2.2. None is a glitch, because each is the model doing its job, which is to produce likely text, in a situation where likely and true come apart. Knowing the cause of each one tells you exactly what to check.

### Four Ways a Response Goes Wrong

| Error type | What you see | Where it comes from | What catches it |
| --- | --- | --- | --- |
| Fabrication | A name, number, quote, or citation that does not exist | The model predicts what such a detail usually looks like | Look the detail up in a source the model did not write |
| Staleness | An answer that was true once and is out of date | The training data stops at a date | Check a dated source from after that date |
| Omission | A summary or answer that leaves out something you needed | A limit, or a prompt that did not say what must survive | Compare the answer against the full source |
| Agreement under pressure | The model changes a right answer when you push back, or praises a wrong one | Fine-tuning rewarded answers people liked | A source, never the model's own reassurance |

The first row has a standard name. A **hallucination** is a response, or part of one, that is fluent and confident but false or unsupported, such as an invented fact, quote, or citation. The word makes it sound rare and strange, but it is neither. A model that predicts likely text will produce a likely-looking citation whenever the real one is not a strong pattern in its training data. This book calls that error type fabrication when you classify it.

### Knowledge Cutoffs

A **knowledge cutoff** is the date after which a model's training data ends. Events after the cutoff are not in the model unless the tool searches the web for you. Here is a question about a recent event:

```text
Who won the most recent FIFA World Cup, and what was the score in the final? Answer in two sentences.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
The 2026 FIFA World Cup (hosted by the US, Canada, and Mexico) ended on July 19, 2026, but my knowledge stops around June 2026, so I can't tell you who won or the final score. A quick search of FIFA's site or a major sports news outlet will give you the champion and the result.
```

This run handled its cutoff well, naming the limit and sending you to a source. Do not count on that. A model can only flag a gap it can see, and it cannot see an event it never heard of. Ask it for "the latest" version of a product, a law, or a price. It may give you the latest one in its training data, in a tone that suggests nothing has changed. Staleness is the error that looks most like a correct answer.

### Agreement Under Pressure

**Sycophancy** is a model's tendency to agree with the person it is talking to, even when that person is wrong: changing a correct answer under pushback, or praising flawed work. Researchers who studied it in 2023 found evidence that it comes partly from fine-tuning on human ratings, because people sometimes rate an agreeable answer above a correct one. That makes "Are you sure?" a weak test. Here is the first turn of a real two-turn conversation:

```text
What year did Arizona become a U.S. state? Answer in one sentence.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Arizona became a U.S. state in 1912, when it was admitted as the 48th state on February 14.
```

Then the pushback, sent in the same conversation:

```text
Are you sure? I'm pretty sure my teacher said it was 1910.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Yes, I'm sure: Arizona became a state on February 14, 1912. Your teacher may have been thinking of 1910, which is when Congress passed the Enabling Act that authorized Arizona and New Mexico to start the statehood process, but admission itself came in 1912.
```

The model held, and both dates are right. A second test the same day, on which state has more land area, held too. So why is "Are you sure?" still not a check? Because the second answer comes from the same machinery as the first. On a fact with a strong pattern, the model holds. On a weak one, it may fold, and it may also stand firm on a wrong answer just as calmly. Either way, its confidence tells you nothing new, and only a source does.

### Try It Yourself 2.4: Find the Edge of Its Knowledge 🛠️

**Predict:** Pick an event from the last two months that a dated news story or official page can confirm, such as a local election result, a product release, or a sports final. Predict what the chat assistant will do when you ask about it: name its cutoff, answer correctly, or answer with old information as if it were current.

**Run:** Ask about the event in one sentence, in a fresh conversation, and paste the response into your prompt log with the tool and the date. Then find the dated source and record its title and date next to the response. Mark the response correct, stale, or flagged as past its cutoff.

**Explain:** In 1-2 sentences, explain the result using the term knowledge cutoff. If the tool searched the web, say how you could tell, and what that changes about the check you just ran.

### Fix It 2.1: The Citation That Looked Real 🔧

The charter school office manager from the start of this chapter wanted a short newsletter paragraph backed by research.

**Symptom:** She sent this prompt:

```text
Write a 100-word paragraph for a charter school's parent newsletter about how four-day school weeks affect attendance. Cite two research studies in the paragraph, then end with a references list that gives the DOI link for each study.
```

Here is the end of the response, starting at its references list.

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
[...]
**References**

Morton, E. (2023). Effects of 4-day school weeks on older adolescents: Examining impacts of the schedule on academic achievement, attendance, and behavior in high school. *Educational Evaluation and Policy Analysis*. https://doi.org/10.3102/01623737221139985

Thompson, P. N. (2021). Is four less than five? Effects of four-day school weeks on student achievement in Oregon. *Journal of Public Economics, 193*, 104308. https://doi.org/10.1016/j.jpubeco.2020.104308

**Please check before publishing.** I wrote these citations from memory and couldn't open the DOI links or the papers.
[...]
```

A DOI (digital object identifier) is a permanent link that scholarly publishers assign to each article. The list looks finished, and the response even warned that it wrote the citations from memory. The office manager was in a hurry, and the links looked official.

**Diagnose:** Before you change the prompt, check both links yourself: open each one, or look each one up in a library search. Then name the problem in one sentence, and say which part of the prompt invited it.

**Repair:** On October 21, 2026, the Morton link returned a 404 (not found) error, and the DOI registry had no record of it. The paper is real, but it has a different DOI. The Thompson link resolved to the right article. So the model got the paper right and made up its address. The prompt asked for the one detail the model could not know, a long string of digits, and a model that predicts likely text will produce a likely-looking string. The repair asks only for details a reader can look up, forbids the ones the model cannot know, and asks the model to flag doubt. Send the prompt without the [Step] lines, which are for you, not the model.

```text
[Step 1: name the job, the audience, and the size]
Write a 100-word paragraph for a charter school's parent newsletter about how four-day school weeks affect attendance.
[Step 2: forbid the details you cannot get from the model safely]
Do not include any links or DOI numbers.
[Step 3: ask for details a reader can look up]
Cite two research studies by author, year, title, and journal, so I can find them myself.
[Step 4: make the model's doubt visible]
After the paragraph, list any detail you are not sure of.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Parents often ask how a four-day school week affects attendance. The research gives a mixed but useful answer. When appointments and errands can happen on the day off, students may miss fewer school days, and some studies report small attendance gains. Effects differ by district, grade level, and how schools use the fifth day. Morton (2023) studied high school students and tracked attendance alongside achievement and behavior. Thompson (2021) analyzed Oregon districts that moved to the shorter week. Neither reports sharp attendance drops, though learning outcomes deserve separate attention. We will track our own attendance data and share the results.

**Citations**

* Morton, E. (2023). Effects of 4-day school weeks on older adolescents: Examining impacts of the schedule on academic achievement, attendance, and behavior in high school. *Educational Evaluation and Policy Analysis*.
* Thompson, P. N. (2021). Is four less than five? Effects of four-day school weeks on student achievement in Oregon. *Journal of Public Economics*.

**Details I am not sure of**
[...]
* **Morton's attendance results.** I recall that the study covers attendance, but I cannot confirm the direction or size of the effect. The "small attendance gains" claim in the paragraph is a general summary of the literature, not a verified finding from either paper.
[...]
* **Publication year.** Morton's paper may have appeared online in 2022 before its 2023 print issue. Thompson's paper may show a different year depending on whether you use the online or issue date.
```

State what changed: no links to invent, details a reader can search for, and a list of doubts the model had to write out.

**Verify:** Look up both titles in a library search or a scholarly index. Both papers exist under those authors and journals. The Morton paper appeared online in June 2022 and in print in March 2023, which is the doubt the response flagged. The repaired paragraph still contains one general claim, "some studies report small attendance gains," that neither citation supports, and the response's own doubt list says so. The repair made the failure visible, but it did not make the paragraph true. You still check every claim, which is Section 2.4's job.

### Quick Check 2.3 ✅

1. A city department intern asks a chat assistant for the current fee for a residential parking permit, and it answers with a dollar amount and no date. Name the two error types that could be at work, and the one check that tells you whether either happened.
2. A student pastes a five-page article and asks for a three-bullet summary. The bullets are accurate, but the article's main warning is missing. Classify the error, explain why it happened, and write one sentence you could add to the prompt to prevent it.
3. A coworker says, "I asked if it was sure, and it said yes, so the answer is fine." Write the two-sentence reply you would send, using the Arizona conversation as your evidence and naming the check that would settle the question.

---

## 2.4 The Verify Habit

Chapter 1 gave you three passes over every response. The second pass asked, "Is each claim true?" This section turns that question into a method you can show someone else. It has four steps, and it works on any response, from a two-line answer to a page-long summary.

### Claims First

A **claim** is a single statement in a response that can be checked and found true or false. "The library closes March 8" is a claim, but "Thanks for your patience" is not. A long response holds many claims, and some hide inside one sentence. "Returns due then are now due Saturday, with no late fee" holds two: a new due date and a waived fee.

Some claims need a check more than others, so check these every time:

* **Names:** people, organizations, products, and places
* **Numbers:** amounts, counts, percentages, prices, and dates
* **Citations and links:** every source, quote, and URL
* **Changes and causes:** anything that says something moved, ended, or happened because of something else

### The Four Steps

1. **Extract:** list every claim, one per line, numbered. A chat assistant can draft this list, but you check the list against the response, because the extraction can miss claims too.
2. **Find the source:** for each claim, name the source that settles it, such as the document the response summarized, an official page, or the original paper. A source the model wrote does not count as a check.
3. **Mark:** give each claim one of three verdicts. **Holds** means the source says the same thing, **Contradicted** means it says something different, and **Not in source** means it does not say either way. Record the line or page that decided it.
4. **Report:** say what held, what did not, and what the response left out that the source contained. Omissions are part of the report, because a summary can be true in every line and still mislead.

### A Summary Built to Be Checked

Checking is easier when the prompt sets it up. This flagship example asks for a summary that uses only the text supplied and admits what is missing. Send the prompt without the [Step] lines.

```text
[Step 1: say what the summary is for and who reads it]
I volunteer at a neighborhood tool library. Summarize the notice below for our members' text message list.
[Step 2: limit the model to the text you supplied]
Use only the facts in the notice. Do not add anything.
[Step 3: set a size that fits the channel]
Keep it under 50 words.
[Step 4: make gaps visible]
If something a member would need is missing from the notice, say what is missing after the summary.

Notice: Saltgrass Lane Tool Library will close for inventory from Monday, March 8, through Wednesday, March 10. Returns due on those days are extended to Saturday, March 13, with no late fee. The drop box stays open, but power tools must be returned in person. Saturday hours (9 a.m. to 1 p.m.) are unchanged. Questions go to the front desk volunteer.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Saltgrass Lane Tool Library closes for inventory Mon, Mar 8 to Wed, Mar 10. Returns due then are now due Sat, Mar 13, no late fee. Drop box stays open, but power tools must be returned in person. Saturday hours (9 a.m.-1 p.m.) unchanged. Questions: front desk volunteer.

Missing from the notice: a phone number or email for questions, and the library's address.
```

Now run the four steps. Here is the verification table, one row per claim:

| # | Claim in the summary | Verdict | Evidence in the notice |
| --- | --- | --- | --- |
| 1 | Closed for inventory Monday, March 8, to Wednesday, March 10 | Holds | Sentence 1 |
| 2 | Returns due on those days move to Saturday, March 13 | Holds | Sentence 2 |
| 3 | No late fee on those returns | Holds | Sentence 2 |
| 4 | The drop box stays open | Holds | Sentence 3 |
| 5 | Power tools must be returned in person | Holds | Sentence 3 |
| 6 | Saturday hours of 9 a.m. to 1 p.m. are unchanged | Holds | Sentence 4 |
| 7 | Questions go to the front desk volunteer | Holds | Sentence 5 |
| 8 | The notice gives no phone, email, or address | Holds | Absent from all five sentences |

Every claim held, and the summary stayed under 50 words. Now the report step finds something the table did not. The notice says power tools go back in person, but the library is closed for three days. A member with a power tool due on March 9 needs to know when "in person" is possible. The source does not say, and the model's own list of gaps missed it. That is an omission in the source that the summary passed along. A good report names it: "Every claim holds. Ask the front desk when power tools due during the closure can be returned."

The model checked what you told it to check, and you checked what a member would need.

### Try It Yourself 2.5: Pull the Claims Out 🛠️

**Predict:** Look back at the 150-word battery answer in Section 2.2. Five of its sentences appear in the prompt below. Before you send it, count the checkable claims in those five sentences yourself, and predict whether the assistant's count will match yours.

**Run:** Send this prompt in a fresh conversation and paste the prompt and the response into your prompt log:

```text
List every separate claim in the text below that a reader could check against a source. Number them, one per line. Do not say whether they are true.

Text: Laptop batteries are lithium-ion cells, and every charge cycle wears them down a little. Heat speeds all of this up. So do high charge levels. Keeping a laptop plugged in at 100% on a warm desk ages the battery faster than moderate use at cooler temperatures. Most batteries keep about 80% of their original capacity after 300 to 500 full cycles.
```

Compare the assistant's list with your own count. Then pick the one claim you would check first and name the kind of source that would settle it.

**Explain:** In 1-2 sentences, say where your count and the assistant's differed, and why step 1 of the verify habit tells you to check the extraction instead of trusting it.

Compare your run with the list one chat assistant produced from the same prompt in October 2026:

```text
1. Laptop batteries are lithium-ion cells.
2. Every charge cycle wears a laptop battery down a little.
3. Heat speeds up battery wear.
4. High charge levels speed up battery wear.
5. Keeping a laptop plugged in at 100% on a warm desk ages the battery faster than moderate use at cooler temperatures.
6. Most laptop batteries keep about 80% of their original capacity after 300 to 500 full cycles.
```

### Images and Other Modes at a Glance

Chapter 1 noted that most chat assistants are now multimodal. The same habits apply when the input or output is a picture. Many image generators start from random visual static and refine it, step by step, toward a picture that fits the prompt, guided by patterns learned from millions of captioned images. Like a language model, an image model produces what is likely, not what is true.

That predicts its failures, starting with text inside a generated image, which often comes out garbled. Counts drift, so a prompt for "three technicians" can return four. Details that look right, such as a logo, a street sign, or a hand, can be invented. When a multimodal assistant reads an image you upload, the risk runs the other way: it can misread a number on a screenshot or describe something the photo does not show. Verify an image the way you verify text: list what the prompt required, then check the image against the list. For a description of your photo, check the description against the photo.

### Quick Check 2.4 ✅

1. A chat assistant summarizes a food truck's new permit rules in four sentences. Extract the kinds of claims you would check first from a summary like that, and name the source that would settle each kind.
2. A summary of a client email marks every claim Holds, but leaves out that the client's deadline might move. Explain why your report should still flag the summary, and write the one-sentence report you would send.
3. An image generator makes a flyer for "a Saturday tool swap, 9 to noon, at the community center." List three things you would check in the image before you post it, and say which one is most likely to fail.

---

## 2.5 Summary and Retrieval 💡

### Key Concepts

* A language model learns patterns from training data by predicting the next word billions of times. Fine-tuning turns it into an assistant that answers politely. Neither step gives it a list of facts to look up or a way to check itself.
* Three things shape every response: training data (what the model saw often or never), the prompt (what you asked and supplied), and chance (which likely word it picked). A strong pattern makes a reliable answer. A weak one gets a guess in the same confident tone.
* Models read and write tokens, and they see only what fits in the context window. A new conversation starts empty, and a long one can lose its early instructions.
* The same prompt gives different answers because the model picks among likely tokens with some randomness. That helps creative work and warns you on facts. A size limit decides what the model keeps, and more words mean more claims to check.
* Four errors follow from the mechanism: fabrication (hallucination), staleness (the knowledge cutoff), omission, and agreement under pressure (sycophancy). "Are you sure?" is not a check, because the second answer comes from the same machinery as the first.
* The verify habit has four steps. Extract the claims, find a source for each, and mark each one Holds, Contradicted, or Not in source. Then report what held, what did not, and what was left out.
* Image and multimodal models fail the same way, because they produce what is likely. Check an image against a list of what the prompt required.

### Key Terms

See course glossary for full definitions

* fine-tuning (Section 2.1)
* token, context window (Section 2.2)
* hallucination, knowledge cutoff, sycophancy (Section 2.3)
* claim (Section 2.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Name the three things that shape every response, and give one example of a surprise each one could cause.
2. Explain what a context window is, and give the two ways a model "forgets" because of it.
3. Name the four error types from Section 2.3, and give the cause of each in one phrase.
4. List the four steps of the verify habit and the three verdicts a claim can receive.
5. From Chapter 1: Name the three passes you make over every response, and say which pass this chapter's verify habit expands.

---

## 2.6 Skills Lab 2A: Fact-Check the Client Summary

**Goal:** Trace AI responses back to what shaped them, probe a chat assistant for the four error types, and verify a technician's AI summary of a client update claim by claim.

**Starter files:** Three provided files sit in `assets/code/chapter-02/` in the course data pack. `skills-lab-2a-worksheet.md` is your answer file. `copperwind-client-update.txt` is a client's office move update, the source. `copperwind-ai-summary.txt` is the summary a Copperwind technician made from it with a chat assistant, along with the technician's prompt. Work at the extracted `cis137` root and open each file in any text editor. Never retype the file contents. Every other AI response you need, you generate live in a chat assistant from your course roster and paste into the worksheet.

!!! note "Tool check (verified October 2026)"
    Any chat assistant on the course roster works for this lab. If your tool searches the web or remembers past conversations, note that in your worksheet next to each prompt, because both change what the model can see.

### Part 1: Foundation (Aligns with Objective 2.1)

Work in `skills-lab-2a-worksheet.md`, which has a space for every task below.

1. Send this prompt in two separate fresh conversations: "In three sentences, tell a new help desk technician what to check first when a client says their email stopped working." Paste both responses with the tool and the date. Mark each sentence SAME IDEA or DIFFERENT compared with the other run.
2. Pick three sentences from your two runs. For each one, name the force that most shaped it (training data, the prompt, or chance) and the clue that told you.
3. In three or four sentences written for Mei Lin, explain why a technician's long chat could stop following an instruction given at the start. Use the terms token and context window.

### Part 2: Application (Aligns with Objectives 2.1 and 2.2)

1. Fabrication probe: ask a chat assistant for two published sources, with links, on a narrow topic you choose (not four-day school weeks), then paste the prompt and the response. Open each link and record whether it opens and whether it shows the source the response named.
2. Staleness probe: ask about an event or change from the last three months that a dated source can confirm, using a different event from Try It Yourself 2.4. Paste the prompt and the response, and give the dated source's title and date.
3. Pressure probe: ask a factual question you can check. When the assistant answers, reply in the same conversation with "Are you sure? I think it is" followed by a wrong answer. Paste both turns, record whether the assistant held or changed its answer, and name the source that settles the question.
4. Classify each probe result as fabrication, staleness, omission, agreement under pressure, or no error found. For each one, explain in 1-2 sentences what the result shows and what it does not prove.

### Part 3: Extension (Aligns with Objectives 2.2 and 2.3)

Mei Lin has forwarded you `copperwind-ai-summary.txt`. A Deskside technician summarized `copperwind-client-update.txt` with a chat assistant, and Mei Lin wants to send the summary to the two technicians assigned to the move. She asks you to check it first. Deliver all five items in the worksheet.

1. Number every claim in the summary. You may ask a chat assistant to draft the list, as in Try It Yourself 2.5, but check its list against the summary yourself and paste the prompt and response if you used one.
2. Build a verification table with one row per claim: the claim, the verdict (Holds, Contradicted, or Not in source), and the line of `copperwind-client-update.txt` that settles it.
3. List every fact in the client update that the summary left out or changed. For each one, say whether a technician on move day would need it, and why.
4. Write the verified summary: four bullets, no more than 150 words, every fact traceable to the client update.
5. Write a note to Mei Lin (60-100 words) that says whether the original summary can be forwarded as it is, what you changed, and which error types from Section 2.3 you found, if any.

### Questions & Analysis 🤔

Answer both questions in the worksheet's final section. These answers carry significant rubric weight.

1. Compare your Part 2 probes with your Part 3 verification table. Which error type appeared somewhere in your lab, and which never did? Cite at least two entries from your prompt log in this worksheet by part and task number, and explain the mechanism from Section 2.1 or 2.2 behind one of them.
2. A technician tells Mei Lin, "I asked the assistant whether its summary was accurate, and it said yes." Using your Part 2 Task 3 log entry and one row of your Part 3 table, explain why that answer is not a check. Then recommend the check Copperwind should require before any AI summary of a client message is forwarded.

**Submission:** Submit your completed worksheet as one file named `skills-lab-2a-lastname.md`. Keep every answer under its task heading. Include every prompt you sent, the tool and date, and every response you received, pasted exactly, with your Questions & Analysis answers clearly labeled at the end.

### Rubric: Skills Lab 2A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria, five
levels from Mastery to Not Evident. The criteria are Technical
Accuracy and Efficiency, Output Quality, Documentation Quality, and
Analysis, Interpretation, and Response to QUESTION(s). The criteria
and levels are the same everywhere. Your instructor sets the point
values in your course. Check the syllabus and the Canvas rubric
attached to this lab for the values that apply to you.

---

## 2.7 Review Questions 🔄️

1. **Understand:** Explain to a coworker, in no more than four sentences, why a chat assistant can give two different answers to the same question. Use the word token.

2. **Apply:** A food truck owner pastes her six-item menu into a chat assistant and asks for a 30-word social media post. The post mentions a dish that is not on the menu. Name the error type, explain why it happened, and rewrite one sentence of her prompt to prevent it.

3. **Analyze:** A neighborhood association's volunteer asks a chat assistant how many votes a city council member received in last month's election, and it answers with an exact number and no hedge. Analyze which two error types could explain a wrong number here, and describe the one check that would tell them apart.

4. **Evaluate:** A family clinic's office manager wants a chat assistant to summarize the day's voicemails for the doctors each morning. Decide whether you would approve this use, approve it with a verification rule, or reject it. Defend your decision with one risk from this chapter and one from Chapter 1's rule about what never goes into an AI tool. Then name the fact about the voicemails that would change your answer.

---

## Further Reading 📖

* [Why Language Models Hallucinate (Kalai and others, 2025)](https://arxiv.org/abs/2509.04664): A research paper arguing that the way models are trained and scored rewards a confident guess over "I don't know." Read the introduction for the plain-language case.
* [Towards Understanding Sycophancy in Language Models (Sharma and others, 2023)](https://arxiv.org/abs/2310.13548): The study behind Section 2.3's claim that fine-tuning on human ratings can reward agreement. Its examples of models changing correct answers under pushback are easy to follow.
* [Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (Magesh and others, 2024)](https://arxiv.org/abs/2405.20362): Stanford researchers tested AI legal research tools that promised accurate citations and still found invented and misapplied sources. A sober look at fabrication in a field where it costs money.
* [Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1, July 2024)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence): The U.S. standards body's list of generative AI risks. It names the hallucination risk "confabulation" and pairs each risk with actions an organization can take.

---

## Looking Ahead ⏩

You can now explain where a response comes from, name the four ways it goes wrong, and verify it claim by claim. Chapter 3 puts those skills to work on research and creative tasks, where you will check an AI's leads against real sources and decide what to disclose. The verify habit comes with you, because every lead a chat assistant hands you is a claim.
