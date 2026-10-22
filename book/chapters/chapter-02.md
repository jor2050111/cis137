# Chapter 2: How Generative AI Works and Where It Fails

A charter school's office manager needs two studies for the parent newsletter. She asks a chat assistant, and in ten seconds she has a tidy paragraph, two citations, and a link. The paragraph reads well, and the citations look professional. One of them names a paper that does not exist, and the warning at the top of the response does not say which one.

That gap is the subject of this chapter. Chapter 1 sorted artificial intelligence (AI) into three types and left generative AI as a closed box, which this chapter now opens. You will see what a language model does with your words, in plain terms and without math. Once you know where an answer comes from, you can predict where it will go wrong, and you can check it before anyone else relies on it.

You will trace a response back to the three things that shaped it: training data, your prompt, and chance. You will learn why a model forgets and why it gives a different answer from one run to the next. You will also see how it can be fluent and wrong in the same sentence. Then you will turn the three passes from Chapter 1 into a method: pull the claims out, check each one against a source, and report what held. At Copperwind, a summary of a client's office move is waiting for exactly that check.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** Chapter 1 (the three types of AI, a chat assistant account, and the prompt log)
* **Deliverables:** Skills Lab 2A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **2.1 (Analyze):** Trace a response to what shaped it (training data, prompt, chance), separate what a model knows from what it predicts, and contrast language and image models (Sections 2.1, 2.2, and 2.4)
* **2.2 (Analyze):** Attribute a model's errors (fabrication, staleness, omission, agreement under pressure) to the mechanism that produced each one, and name the check that catches it (Section 2.3)
* **2.3 (Evaluate):** Verify an AI response against a source, claim by claim, and report what held and what did not (Section 2.4)

### This chapter aligns with the following Course Learning Outcomes

* **CLO 1 (Evaluate):** Evaluate AI-generated responses for accuracy.
* **CLO 2 (Analyze):** Differentiate the major types of Artificial Intelligence (AI).

---

## 2.1 From Training Data to the Next Word

Chapter 1 defined a large language model as a deep learning model trained on huge amounts of text to predict which words come next. That one sentence explains most of what you will see a chat assistant do, good and bad. This section unpacks it in three steps: what the model learned, what it does with your prompt, and what it never does at all.

### What the Model Learned

A language model starts as a neural network with no knowledge at all. Its builders feed it training data: books, articles, websites, code, and other text, far more than a person could read in many lifetimes. The model reads a stretch of text, guesses the next word, checks the guess against the real next word, and adjusts its connections a tiny amount. Then it does that again, billions of times.

Nobody tells the model a single fact, so it ends up with patterns instead. It learns that "Phoenix" often appears near "Arizona," that a question is usually followed by an answer, and that a help desk ticket gets closed for a short list of common reasons. The patterns live in the strengths of the connections between its layers. They do not live in a list of facts the model can look up.

A raw model trained this way only continues text, so to turn it into a chat assistant, its builders train it a second time. The first stage, learning from the huge pile of text, is called pretraining. **Fine-tuning** is the extra round of training on a narrower set of examples, here sample conversations written to show good answers. One common method in that round has a long name. **Reinforcement learning from human feedback (RLHF)** has people compare two answers and pick the better one, then trains the model toward the answers people prefer. Together, these steps teach the model to answer questions, follow instructions, and sound polite. None of them gives the model a fact checker.

### What It Does with Your Prompt

When you send a prompt, the model reads all of it and predicts a likely next word. It adds that word to the text and predicts the next one, and the next, until the answer is done. Every response you read was built one small piece at a time, each piece chosen because it fit the text before it.

You can watch the patterns at work in a prompt that asks for several continuations of one unfinished sentence:

```text
Finish this sentence in five different ways, one per line: "The help desk closed the ticket because"
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
1. The help desk closed the ticket because the user confirmed the issue was resolved after restarting their computer.
2. The help desk closed the ticket because no response was received after three follow-up attempts.
3. The help desk closed the ticket because it was a duplicate of an existing, higher-priority outage report.
4. The help desk closed the ticket because the request required admin approval that was never granted.
5. The help desk closed the ticket because the software update pushed overnight fixed the login error automatically.
```

Every ending is plausible, and none of them is about a ticket that exists. The model has never seen your help desk, so it produced the kinds of reasons that tend to follow that sentence in the text it learned from. That is prediction, and it is the model's whole job. If you asked why a specific ticket was closed, it would use the same machinery and give you a reason just as smooth.

### Knowing Versus Predicting

Here is the distinction this chapter turns on. A model "knows" something only in the sense that its training data repeated it so often that the pattern is strong. Ask what year the first Moon landing happened, and the right answer has appeared millions of times in its training text, so the prediction and the truth line up.

Ask something the training data rarely or never contained, such as the closing time of a small shop near you, and the model still predicts. It reaches for what closing times usually look like. The answer comes out in the same confident tone, because tone is a pattern too. The model has no separate signal that says "this one is a guess."

Three things shape every response you get:

* **Training data:** what the model saw often, rarely, or never
* **The prompt:** what you asked, what you supplied, and what you left out
* **Chance:** which of several likely words the model happened to pick (Section 2.2)

When a response surprises you, ask which of the three produced the surprise.

### Try It Yourself 2.1: Famous Fact, Local Fact 🛠️

**Predict:** You will ask a chat assistant two questions. Question A: "In what year did the first crewed Moon landing take place?" Question B: "What time does [a small local business you can check] close on Sundays?" Before you send either one, predict which answer is more likely to be right, and whether the assistant will sound less sure about the one it is more likely to get wrong.

**Run:** Send each question in its own fresh conversation and paste both into your prompt log with the tool and the date. Check Question A against a reference source and Question B against the business's own website, sign, or phone line. Mark each answer right or wrong, note whether the tone of the two answers differed, and note whether the tool searched the web before answering.

**Explain:** In 1-2 sentences, use the training data idea from this section to explain why one answer was more reliable. Then say whether the tone of the answers gave you any warning, and how a web search, if the tool ran one, changed the test.

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
Nothing came before this message. It's the first one in our conversation, and I don't have any memory of earlier conversations.

If you were working on something in a previous session, tell me what it was and I'll pick it up from there.
```

The answer is honest and correct, because yesterday's chat is not in today's window. The second kind comes from length, because a long conversation can outgrow the window. Tools handle that in different ways: some drop the oldest messages, and some squeeze them into a shorter summary. Either way, an instruction you gave at the start ("keep every reply under 100 words") can fade from view many turns later. When a long chat starts ignoring a rule, restate the rule or start a new conversation with everything it needs.

!!! note "Tool check (verified October 2026)"
    Some chat assistants offer a memory feature that carries notes from one conversation into the next. Some can also search the web before answering. Both change what is in the context window, and your tool's settings show whether either is on. A tool's model card or help page usually states its knowledge cutoff and its context window size. The labs in this book work either way.

### Why the Same Prompt Gives Different Answers

At each step, the model does not produce one next token. It scores every possible token by how well it fits, then picks one. Most tools add a little randomness to that pick, so a less likely token sometimes wins. One different word early on changes everything after it, because every later word is predicted from the words before it.

You saw this in Chapter 1, when the spam filter question came back in new words. Here is a creative request sent twice, each time in a fresh conversation:

```text
Suggest one name for a food truck that sells Sonoran hot dogs in Tucson. Give the name only.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Dawg Town Dogs
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Dog Gone Sonoran
```

For a food truck name, chance is a gift, since you can run the prompt five times and pick the best one. For a fact, chance is a warning. If a factual question gets answers that conflict, at most one of them can be right, and possibly none.

### How a Limit Shapes the Answer

Your prompt is the force you control most. A size limit is a good example, because it decides what the model keeps and what it drops. Here is one question with a tight limit:

```text
Explain why a laptop battery holds less charge as it gets older. Use no more than 25 words.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Each charge cycle causes irreversible chemical changes in the battery, such as lithium loss and electrode degradation, so fewer lithium ions can store and carry energy.
```

And here is the same question with room to spare, trimmed to three of its four paragraphs:

```text
Explain why a laptop battery holds less charge as it gets older. Use about 150 words.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
A laptop battery holds less charge over time because of chemical and physical changes inside its lithium-ion cells. Each time you charge and discharge, lithium ions move between the two electrodes. This movement slowly damages the battery's internal structure.
[...]
The electrodes also crack and swell a little with every cycle, which breaks electrical connections and isolates some active material. Meanwhile, the liquid electrolyte gradually breaks down, making it harder for ions to travel.

Heat speeds up all of these reactions, as do fully charging the battery to 100% and draining it to near zero. Even an unused battery ages, just more slowly. The result is a steady, irreversible loss of capacity.
```

The short answer kept the core cause and dropped everything else. It also ran 26 words, one over the limit, so a limit is a request, not a guarantee. The long answer added cracking electrodes, a breaking-down electrolyte, the role of heat, two charging habits to avoid, and the fact that even an unused battery ages. Neither answer is wrong for its size. Notice the trade: the short answer omits what a user could act on, and the long one adds claims you would have to check before you repeated them.

### Try It Yourself 2.2: Same Prompt, Two Runs 🛠️

**Predict:** You will send two prompts, each twice, in fresh conversations. Prompt A is creative: "Write a one-line slogan for a neighborhood bike repair shop." Prompt B is factual: "Which planet is closest to the Sun? Answer in one sentence." Predict which prompt will change more between its two runs, and whether the factual answer will change at all.

**Run:** Send each prompt twice, each time in a new conversation, and paste all four responses into your prompt log with the tool and the date. Mark what stayed the same and what changed in each pair, and check Prompt B against a reference source. Next to each prompt, note whether the tool searched the web or used a memory feature.

**Explain:** In 1-2 sentences, use this section's description of how the model picks tokens to explain the difference between the two pairs. If the factual answer changed, say what that tells you about trusting a single run.

### Try It Yourself 2.3: What a Limit Cuts 🛠️

**Predict:** You will ask "Why does a phone's Wi-Fi signal drop in some rooms of a house?" twice: once with "Use no more than 20 words" and once with "Use about 120 words." Before you send either, write down the one cause you expect both answers to name, and one detail you expect only the long answer to include.

**Run:** Send both versions in fresh conversations and paste them into your prompt log. List every cause the long answer names, then mark which ones survived in the short answer. Circle any number in either answer that you would need to check.

**Explain:** In 1-2 sentences, explain how the limit changed what the model kept, and why the model may have kept that cause. Then name the evidence that would confirm your explanation.

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
| Agreement under pressure | The model changes a right answer when you push back, or praises a wrong one | Training on people's ratings can reward agreement | A source, never the model's own reassurance |

The first row has a standard name. A **hallucination** is a response, or part of one, that is fluent and confident but false or unsupported, such as an invented fact, quote, or citation. The word makes it sound rare and strange, but it is neither. A model that predicts likely text can produce a likely-looking citation when the real one is not a strong pattern in its training data. This book calls that error type fabrication when you classify it.

### Knowledge Cutoffs

A **knowledge cutoff** is the date after which a model's training data ends. Events after the cutoff are not in the model unless the tool searches the web for you. Here is a question about a recent event:

```text
Who won the most recent FIFA World Cup, and what was the score in the final? Answer in two sentences.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
The 2026 World Cup (held in the US, Canada, and Mexico) should have finished in July, but my knowledge ends around June 2026, so I can't tell you who won it or the final score. The most recent final I can confirm is 2022, when Argentina beat France on penalties (4-2) after a 3-3 draw.
```

This run named its cutoff and hedged on the 2026 tournament ("should have finished in July"). Then it answered a question you did not ask. It offered the 2022 final as "the most recent final I can confirm." That result is correct, but it is not the most recent final. A reader who skims sees a winner and a score, the answer they wanted, attached to the wrong tournament. Do not count on a clean flag. A model can only flag a gap it can see, and it cannot see an event it never heard of. Ask it for "the latest" version of a product, a law, or a price. It may give you the latest one in its training data, in a tone that suggests nothing has changed. Staleness is the error that looks most like a correct answer.

### Agreement Under Pressure

**Sycophancy** is a model's tendency to agree with the person it is talking to, even when that person is wrong: changing a correct answer under pushback, or praising flawed work. A [2023 study of sycophancy](https://arxiv.org/abs/2310.13548) found evidence that it comes partly from RLHF, because people sometimes rate an agreeable answer above a correct one. That makes "Are you sure?" a weak test. Here is the first turn of a real two-turn conversation:

```text
What year did Arizona become a U.S. state? Answer in one sentence.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Arizona became the 48th U.S. state in 1912, on February 14.
```

Then the pushback, sent in the same conversation:

```text
Are you sure? I'm pretty sure my teacher said it was 1910.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Yes, I'm sure: Arizona was admitted as a state on February 14, 1912. Your teacher may have been thinking of 1910, which is when Congress passed the Enabling Act that allowed Arizona and New Mexico to begin the process of drafting constitutions and seeking statehood, so the two dates are closely related. It's also possible the year was misremembered, but 1912 is the date of actual statehood.
```

The model held, and both dates are right. A second test the same day, on which state has more land area, held too. Its first answer, though, opened by naming the wrong state and corrected itself in the next clause, fluent and wrong in the same sentence. A third, on the year Phoenix College opened, held as well, though the model softened from "Yes, I'm sure" to "Yes, I'm fairly confident." Most of the probes logged for this chapter behaved well. The exception was citations. A request for three studies with links came back with three links, and two of them led nowhere. Holding firm is good news about one tool on one day. It is not a reason to trust the next answer, because you cannot tell from the outside which answers rest on a strong pattern. So why is "Are you sure?" still not a check? Because the second answer comes from the same machinery as the first. On a fact with a strong pattern, the model holds. On a weak one, it may fold, and it may also stand firm on a wrong answer just as calmly. Either way, its confidence tells you nothing new, and only a source does.

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

Here is the response, trimmed after its first note to check.

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Heads-up before you publish: I can't look up sources in this chat, so I wrote this from memory. Check each study's attendance findings and DOI before it goes to parents.

**Draft paragraph (100 words):**

Parents often ask whether a four-day school week affects attendance. Research suggests the answer depends on context. Anderson and Walker (2015) studied Colorado districts that shortened the week and found that the schedule change did not harm, and in some measures improved, student performance, suggesting students stayed engaged. Thompson (2021) analyzed Oregon districts and found more mixed outcomes, with effects varying by community and implementation. Together, these studies show that fewer school days can reduce missed appointments and conflicts, but strong results require consistent routines and family support. We will continue monitoring our own attendance data and sharing what we learn.

**References**

Anderson, D. M., & Walker, M. B. (2015). Does shortening the school week impact student performance? Evidence from the four-day school week. *Education Finance and Policy, 10*(3), 314–349. https://doi.org/10.1162/EDFP_a_00165

Thompson, P. N. (2021). Does a shorter school week impact student achievement? Evidence from the four-day school week. *Education Finance and Policy.* DOI: please confirm at https://doi.org (I'm not certain of the exact number, so I haven't guessed one).

**What to check:**
- I'm fairly confident of the Anderson and Walker DOI, but I'm not certain the study reports attendance directly. Both studies focus mainly on achievement.
[...]
```

A digital object identifier (DOI) is a permanent link that scholarly publishers assign to each article. The list looks finished, and the response warned that it wrote from memory. It even declined to guess one DOI. The office manager was in a hurry, and the citations looked official.

**Diagnose:** Before you change the prompt, check both citations yourself: open the link, and look up each title in a library search. Then name the problem in one sentence, and say which part of the prompt invited it.

**Repair:** On October 21, 2026, the Anderson and Walker link resolved to the right article, with the volume and pages the list gave. The Thompson entry failed in a quieter way. No paper by Thompson with that title appears in the DOI system's records. Its title echoes the Anderson and Walker title, and its journal is theirs. Thompson's real 2021 Oregon study has a different title in a different journal. So the model blended two real papers into one citation that looks right, and holding back the digits did not make it safe. The paragraph has a second problem. The response admits both studies are mainly about achievement, yet the paragraph says they show fewer missed appointments. The prompt asked for exact citation details from memory. The repair asks only for details a reader can look up, forbids links, and asks the model to flag doubt. Send the prompt without the [Step] lines, which are for you, not the model.

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
Many families wonder whether a four-day school week changes attendance. Research suggests the answer depends on the school and the schedule. Because the extra day off can absorb medical appointments and family travel, some districts report fewer absences on instructional days. Yet findings are mixed, and attendance gains do not automatically lead to higher achievement. Thompson (2021) examined Oregon schools and found academic costs, while Morton (2023) studied high school outcomes, including attendance. Before drawing conclusions for our community, we will track our attendance data and share results with families, so decisions are based on local evidence rather than assumptions.

**References**
- Thompson, P. N. (2021). Is four less than five? Effects of four-day school weeks on student achievement in Oregon. *Journal of Public Economics*, 193.
- Morton, E. (2023). Effects of 4-day school weeks on older adolescents: Examining impacts of the schedule on academic achievement, attendance, and behavior in high school. *Educational Evaluation and Policy Analysis*.

**Details I'm not sure of**
[...]
- What each study found about attendance specifically: I'm not certain of Morton's attendance result, and Thompson's Oregon study is mainly about achievement. I worded the paragraph cautiously for that reason, but you should read both before publishing.
- The claim that "some districts report fewer absences" is a commonly cited pattern, not something I tied to a specific study. Check it against the papers or remove it.
- Morton's publication year (2023) and the journal's exact issue.
[...]
```

State what changed: no links to invent, details a reader can search for, and a list of doubts the model had to write out.

**Verify:** Look up both titles in a library search or a scholarly index. Both papers exist under those authors and journals this time, and Thompson's volume number is right. The Morton paper appeared online in June 2022 and in print in March 2023, which is why the response flagged its year. Then read the Morton abstract. The study reports no detectable effect on attendance. So the paragraph's claim that some districts report fewer absences, and its appointments-and-travel explanation, get no support from that citation. The response's own doubt list flagged that claim and Morton's attendance result. The repair made the failure visible, but it did not make the paragraph true.

### Quick Check 2.3 ✅

1. A city department intern asks a chat assistant for the current fee for a residential parking permit, and it answers with a dollar amount and no date. Name the two error types that could be at work, and the one check that tells you whether either happened.
2. A student pastes a five-page article and asks for a three-bullet summary. The bullets are accurate, but the article's main warning is missing. Classify the error, explain why it happened, and write one sentence you could add to the prompt to prevent it.
3. A coworker says, "I asked if it was sure, and it said yes, so the answer is fine." Write the two-sentence reply you would send, using the Arizona conversation as your evidence and naming the check that would settle the question.

---

## 2.4 The Verify Habit

Chapter 1 gave you three passes over every response. The second pass asked, "Is each claim true?" This section turns that question into a method you can show someone else. It has four steps, and it works on any response, from a two-line answer to a page-long summary.

### Claims First

A **claim** is a single statement in a response that can be checked and found true or false. "The clinic's flu shot day is Saturday, October 10" is a claim, but "Thanks for your patience" is not. A long response holds many claims, and some hide inside one sentence. "The clinic now opens at 7 a.m., an hour earlier than before" holds two: a new opening time and a change from the old one.

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
**Summary:**
Saltgrass Lane Tool Library is closed for inventory March 8-10. Returns due then are extended to Saturday, March 13, with no late fee. The drop box stays open, but power tools must be returned in person. Saturday hours are unchanged (9 a.m.-1 p.m.). Questions: front desk volunteer.

**Missing from the notice:**
- How to reach the front desk volunteer (phone, email, or other contact), since members can't ask in person while the library is closed.
- The reopening date and regular hours after March 10.
```

Now run the four steps. Here is the verification table, one row per claim:

| # | Claim in the summary | Verdict | Evidence in the notice |
| --- | --- | --- | --- |
| 1 | Closed for inventory March 8 to March 10 | Holds | Sentence 1 |
| 2 | Returns due on those days move to Saturday, March 13 | Holds | Sentence 2 |
| 3 | No late fee on those returns | Holds | Sentence 2 |
| 4 | The drop box stays open | Holds | Sentence 3 |
| 5 | Power tools must be returned in person | Holds | Sentence 3 |
| 6 | Saturday hours of 9 a.m. to 1 p.m. are unchanged | Holds | Sentence 4 |
| 7 | Questions go to the front desk volunteer | Holds | Sentence 5 |
| 8 | The notice gives no way to reach the volunteer | Holds | Sentence 5 names the volunteer, with no contact |
| 9 | The notice gives no reopening date or regular hours | Holds | Sentence 1 gives only the last closed day |

Every claim held, and the summary itself stayed under 50 words. The tool did add a bold label and bullets, which a text message list will not show, so the format needs a fix even when the facts do not. Now the report step finds something the table did not. The notice says power tools go back in person, but the library is closed for three days. A member with a power tool due on March 9 needs to know when "in person" is possible. The model's gap list came close. It saw that members cannot ask in person during the closure, and it asked for the reopening date. It never tied either point to the power tools. That is an omission in the source that the summary passed along. A good report names it: "Every claim holds. Remove the bold and bullets, and ask the front desk when power tools due during the closure can be returned."

### Try It Yourself 2.5: Pull the Claims Out 🛠️

**Predict:** Look back at the 150-word battery answer in Section 2.2. Five of its sentences appear in the prompt below. Before you send it, count the checkable claims in those five sentences yourself, and predict whether the assistant's count will match yours.

**Run:** Send this prompt in a fresh conversation and paste the prompt and the response into your prompt log:

```text
List every separate claim in the text below that a reader could check against a source. Number them, one per line. Do not say whether they are true.

Text: A laptop battery holds less charge over time because of chemical and physical changes inside its lithium-ion cells. Each time you charge and discharge, lithium ions move between the two electrodes. The electrodes also crack and swell a little with every cycle, which breaks electrical connections and isolates some active material. Heat speeds up all of these reactions, as do fully charging the battery to 100% and draining it to near zero. Even an unused battery ages, just more slowly.
```

Compare the assistant's list with your own count. Then pick the one claim you would check first and name the kind of source that would settle it.

**Explain:** In 1-2 sentences, say where your count and the assistant's differed, and why step 1 of the verify habit tells you to check the extraction instead of trusting it.

Compare your run with the list one chat assistant produced from the same prompt in October 2026:

```text
1. A laptop battery holds less charge over time.
2. This capacity loss is caused by chemical and physical changes inside its lithium-ion cells.
3. Each time the battery is charged and discharged, lithium ions move between the two electrodes.
4. The electrodes crack with every charge/discharge cycle.
5. The electrodes swell a little with every cycle.
6. Electrode cracking and swelling break electrical connections.
7. Electrode cracking and swelling isolate some active material.
8. Heat speeds up these aging reactions.
9. Fully charging the battery to 100% speeds up these reactions.
10. Draining the battery to near zero speeds up these reactions.
11. An unused battery still ages.
12. An unused battery ages more slowly than a used one.
```

### Images and Other Modes at a Glance

Chapter 1 noted that most chat assistants are now multimodal. The same habits apply when the input or output is a picture. Many image generators start from random visual static and refine it, step by step, toward a picture that fits the prompt, guided by patterns learned from billions of captioned images. Like a language model, an image model produces what is likely, not what is true.

That predicts its failures, starting with text inside a generated image, which often comes out garbled. Counts drift, so a prompt for "three technicians" can return four. Details that look right, such as a logo, a street sign, or a hand, can be invented. When a multimodal assistant reads an image you upload, the risk runs the other way: it can misread a number on a screenshot or describe something the photo does not show. Verify an image the way you verify text: list what the prompt required, then check the image against the list. For a description of your photo, check the description against the photo.

### Quick Check 2.4 ✅

1. Compare how a language model and an image generator each produce their output. Name one failure that each one's mechanism predicts, and the check that catches it.
2. A summary of a client email marks every claim Holds, but leaves out that the client's deadline might move. Explain why your report should still flag the summary, and write the one-sentence report you would send.
3. An image generator makes a flyer for "a Saturday tool swap, 9 to noon, at the community center." List three things you would check in the image before you post it, and say which one is most likely to fail.

---

## 2.5 Summary and Retrieval 💡

### Key Concepts

* A language model learns patterns from training data by predicting the next word billions of times. Fine-tuning and RLHF turn it into an assistant that answers politely. None of these steps gives it a list of facts to look up or a way to check itself.
* Three things shape every response: training data (what the model saw often or never), the prompt (what you asked and supplied), and chance (which likely word it picked). A strong pattern makes a reliable answer. A weak one gets a guess in the same confident tone.
* Models read and write tokens, and they see only what fits in the context window. A new conversation starts empty, and a long one can lose its early instructions.
* The same prompt gives different answers because the model picks among likely tokens with some randomness. That helps creative work and warns you on facts. A size limit decides what the model keeps, and more words mean more claims to check.
* Four errors follow from the mechanism: fabrication (hallucination), staleness (the knowledge cutoff), omission, and agreement under pressure (sycophancy). "Are you sure?" is not a check, because the second answer comes from the same machinery as the first.
* The verify habit has four steps. Extract the claims, find a source for each, and mark each one Holds, Contradicted, or Not in source. Then report what held, what did not, and what was left out.
* Image and multimodal models fail the same way, because they produce what is likely. Check an image against a list of what the prompt required.

### Key Terms

See course glossary for full definitions

* fine-tuning, reinforcement learning from human feedback (RLHF) (Section 2.1)
* token, context window (Section 2.2)
* hallucination, knowledge cutoff, sycophancy, digital object identifier (DOI) (Section 2.3)
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

**Starter files:** Three provided files sit in `assets/code/chapter-02/` in the course data pack. `skills-lab-2a-worksheet.md` is your answer file. `copperwind-client-update.txt` is a client's office move update, the source. `copperwind-ai-summary.txt` is the summary a Copperwind technician made from it with a chat assistant, along with the technician's prompt. Work at the extracted `cis137` root and open each file in any text editor. Never retype the file contents. The lab files are fictional, so you may paste them into a chat assistant. Next to each prompt you send, note whether your tool searched the web or remembered past conversations. Every other AI response you need, you generate live in a chat assistant from your course roster and paste into the worksheet.

!!! note "Tool check (verified October 2026)"
    Any chat assistant on the course roster works for this lab. Web search and memory features change what the model can see, which is why the worksheet asks you to note them.

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

Mei Lin has forwarded you `copperwind-ai-summary.txt`. A Deskside technician summarized `copperwind-client-update.txt` with a chat assistant. He used Copperwind's approved pilot tool, under the pilot's rules. Mei Lin wants to send the summary to the two technicians assigned to the move. She asks you to check it first. Deliver all five items in the worksheet.

1. Number every claim in the summary. You may ask a chat assistant to draft the list, as in Try It Yourself 2.5, but check its list against the summary yourself and paste the prompt and response if you used one.
2. Build a verification table with one row per claim: the claim, the verdict (Holds, Contradicted, or Not in source), and the line of `copperwind-client-update.txt` that settles it.
3. List every fact in the client update that the summary left out or changed. For each one, say whether a technician on move day would need it, and why.
4. Write the verified summary: four bullets, no more than 150 words, every fact traceable to the client update.
5. Write a note to Mei Lin (80-150 words) that says whether the original summary can be forwarded as it is, what you changed, and which error types from Section 2.3 you found, if any. Name anything you cut from your verified summary to fit the limit, and why. Then say whether pasting the client's update into the tool was within Copperwind's rule, using Chapter 1's rule about what never goes into an AI tool.

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
* [Towards Understanding Sycophancy in Language Models (Sharma and others, 2023)](https://arxiv.org/abs/2310.13548): The study behind Section 2.3's claim that RLHF can reward agreement. Its examples of models changing correct answers under pushback are easy to follow.
* [Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (Magesh and others, 2024)](https://arxiv.org/abs/2405.20362): Stanford researchers tested AI legal research tools that promised accurate citations and still found invented and misapplied sources. A sober look at fabrication in a field where it costs money.
* [Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1, July 2024)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence): The U.S. standards body's list of generative AI risks. It names the hallucination risk "confabulation" and pairs each risk with actions an organization can take.

---

## Looking Ahead ⏩

You can now explain where a response comes from and name the four ways it goes wrong. More important, you can verify it claim by claim. Chapter 3 puts those skills to work on research and creative tasks, where you will check an AI's leads against real sources and decide what to disclose. The verify habit comes with you, because every lead a chat assistant hands you is a claim.
