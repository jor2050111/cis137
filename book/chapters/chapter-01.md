# Chapter 1: What Artificial Intelligence Is

You used artificial intelligence (AI) before breakfast. Your phone turned a mumbled voice note into text. Your email app moved a scam message to Junk before you could read it. Your map app routed you around a stalled truck. None of those tools asked you to type a question. Then the chat assistants arrived, and AI became something you talk to.

Every one of those systems makes a decision that used to be yours. This course puts you on the other side of that line. By the end of it you will know how these tools work and how to ask them for what you need. You will know how to catch them when they are wrong, and how to use them in ways you can defend. Copperwind IT Services, a fictional Phoenix company you will meet later in this chapter, has hired you to help it make exactly those calls.

This chapter builds the vocabulary. You will sort AI into three types by where its behavior comes from. You will follow the milestones that led from the first programs to today's chat assistants. You will survey the kinds of tools you will meet and create your first account. Then you will hold your first conversation and save it, because the log you keep is the habit this whole course runs on. No prior experience is expected anywhere in this chapter.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** None. This chapter starts from zero.
* **Deliverables:** Skills Lab 1A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **1.1 (Analyze):** Differentiate rule-based systems, machine learning, and generative AI by where each one's behavior comes from and what each can and cannot do (Section 1.1)
* **1.2 (Analyze):** Organize the milestones of AI into three eras by where each system's behavior came from, and use the pattern of the AI winters to judge a current claim about AI (Section 1.2)
* **1.3 (Apply):** Set up an account on a generative AI tool, hold a first conversation that follows the course's safety rule, and record the exchange in a prompt log (Sections 1.3-1.4)

### This chapter aligns with the following Course Learning Outcomes

* **CLO 2 (Analyze):** Differentiate the major types of Artificial Intelligence (AI).
* **CLO 4 (Analyze):** Analyze the current state of AI and its impact on society, including strengths and weaknesses.

---

## 1.1 One Word, Many Machines

"Artificial intelligence" sounds like one thing. It is not. **Artificial intelligence (AI)** is a family of techniques for getting computers to do tasks that normally need human judgment: recognizing a face, sorting mail, writing a paragraph, choosing a move. The techniques differ in one way that matters more than any other. Where does the behavior come from? Three answers to that question give you the three types this chapter sorts.

### Rule-Based Systems

A **rule-based system** follows instructions a person wrote out in advance. If this, then that. A parking garage gate that opens when a paid ticket is scanned is one. So is payroll software that pays time-and-a-half after 40 hours in a week. So is a library system that charges a fine the day a book goes overdue.

Where does AI begin on that list? This book draws the line at judgment. Call a rule-based system AI when its rules stand in for a judgment a person would otherwise make: a diagnosis, a routing decision, a credit decision. A gate, an overtime calculation, or a fine schedule follows rules but replaces no judgment, so this book calls those not AI. Reasonable people draw the line in different places. In this course, apply the test and say why.

The rules era produced **expert systems**, programs that captured a specialist's knowledge as hundreds or thousands of if-then rules. A medical expert system of the 1970s could suggest a diagnosis from a list of symptoms, because engineers had turned doctors' knowledge into the rules it followed. That is judgment encoded as rules, and it is AI by this book's test.

Rule-based systems have one great strength. Every decision traces back to a rule a person can read. When the system is wrong, you can find the rule and fix it. They also have one great weakness. The rule writer has to foresee every case. A scam text that avoids the word "prize" sails past a rule that looks for it.

Here is the payroll question put to a chat assistant:

```text
Payroll software pays time-and-a-half for every hour over 40 in a week. Is that artificial intelligence? Answer in three sentences.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
No, not by itself. Payroll software that pays time-and-a-half after 40 hours follows a fixed rule that a programmer wrote in advance, so it does exactly what it was told and nothing more. Artificial intelligence usually means a system that learns patterns from data or makes judgments in situations its programmers did not spell out step by step, and this overtime calculation does neither.
```

The assistant drew the same line this section draws, in its own words: a fixed rule written in advance, no learning, and no judgment the programmers did not spell out. Notice the hedge in the first two words, "not by itself." Hold onto that. Section 1.4 teaches you to read a response in three passes, and small hedges like that one are where the second pass earns its keep.

### Machine Learning

A **machine learning** system is not given the rules. It is given examples, and it works out the patterns on its own. The examples are its **training data**. The result is a **model**, a set of learned patterns the system uses to decide about something it has never seen before. A spam filter trained on millions of messages that people marked as junk learns what junk tends to look like. Nobody wrote the rule. The model learned to weigh hundreds of small clues, such as certain words, links, and senders, and to combine them into a score.

Machine learning powers the voice note that becomes text, the receipt photo that becomes an expense line, the fraud alert on your card, and the photo app that finds every picture of your dog. It handles cases no one wrote a rule for, and it improves when it is retrained on more data. It also learns whatever the data shows, including the mistakes and the bias in that data. Chapter 7 takes that problem seriously. And when a model is wrong, there is often no single rule to point at, which makes it harder to explain.

**Deep learning** is machine learning that uses a **neural network**, a model built from layers of simple connected units, each passing a signal to the next. A network with many layers is deep, which is where the name comes from. Deep networks are what finally made computers good at seeing and hearing, and they are the foundation of the third type.

### Generative AI

**Generative AI** produces new content, such as text, images, audio, or video, in response to a request. The request is a **prompt**. The models behind chat assistants are **large language models (LLMs)**, deep learning models trained on enormous amounts of text to predict which words come next. Chapter 2 opens that box. For now, hold onto the one idea that matters: a generative model is a machine learning model with a new job. The spam filter sorts. The chat assistant makes.

Here is a question a practitioner would ask a chat assistant, and the answer it gave:

```text
Is a spam filter artificial intelligence? Answer in three sentences.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Yes, most spam filters count as artificial intelligence, because they use machine learning to decide whether a message is spam. They learn from large numbers of emails that people have marked as spam or not spam, then apply the patterns they find to new messages. A simple filter that only blocks a fixed list of words would be basic rule-based automation, and some people would not call that AI.
```

Notice what the assistant did. It said yes, then qualified the answer by type: a filter that learns is AI, and a fixed word list may not be. That is the same distinction this section draws, and it is the same line the payroll answer drew from the other side. The table below puts the three types side by side so you can make that distinction yourself.

| Question | Rule-based system | Machine learning | Generative AI |
| --- | --- | --- | --- |
| Where the behavior comes from | Rules a person wrote | Patterns learned from training data | Patterns learned from data, used to produce new content |
| What it is good at | Predictable, explainable decisions | Recognizing patterns in cases no one wrote a rule for | Drafting, summarizing, translating, and making images on request |
| What breaks it | A case the rule writer did not foresee | Data that is thin, skewed, or wrong | Questions about facts it never saw or cannot look up |
| How you check it | Read the rule that fired | Test it on cases with known answers | Verify every claim in the output |

The same job can be built three ways. Compare how each type would handle a spam filter, and watch where the human work moves:

```text
[Step 1: decide where the filter's judgment comes from]
RULE-BASED        a person writes: IF subject contains "ACCOUNT SUSPENDED" THEN Junk
MACHINE LEARNING  the model studies millions of labeled messages, then scores new ones
GENERATIVE AI     a chat assistant reads the message and writes out why it looks like a scam

[Step 2: decide what happens when a new kind of scam appears]
RULE-BASED        someone writes a new rule, or the scam gets through
MACHINE LEARNING  the model needs new labeled examples, then it adapts
GENERATIVE AI     the assistant may catch it from the language, or may be fooled by it

[Step 3: decide how you will check the decision]
RULE-BASED        read the rule that fired
MACHINE LEARNING  look at the score and the examples the message resembled
GENERATIVE AI     read the explanation, then verify every claim in it
```

Each step down the diagram, the human does less work up front and more work checking the result. That trade runs through this entire course.

### Narrow and General

One more distinction protects you from a lot of marketing. **Narrow AI** is built for one job or a cluster of related jobs. The photo app that finds your dog cannot sort your mail. The spam filter cannot write a poem. A chat assistant covers many topics, and a multimodal one handles images and audio too, so it can look general. It is not. It cannot reliably plan a long task on its own, check its own facts, or learn a new job it was never trained for, the way a person can. **Artificial general intelligence (AGI)** is the hypothetical system that could do all of that across any task it was handed. No system meets that bar today.

When a product claims to be "general" or "intelligent," ask what task it was built for and what it cannot do. Ask it every time.

### Try It Yourself 1.1: Sort the Machines 🛠️

**Predict:** Here are six systems:

* (a) a calculator app
* (b) a fitness tracker that scores how well you slept
* (c) a tool that writes a cover letter from your resume
* (d) an elevator that stops at the floors people pressed, in order
* (e) a music app's weekly mix built from your listening
* (f) a grammar checker that suggests rewrites

Before you look back at the table, predict which type each one is, or whether it is AI at all.

**Run:** Classify each system using the table's first row: where does its behavior come from? Apply the judgment test to any rule-based candidate. Write one line per system naming the type and the clue that decided it.

**Explain:** Pick the system you were least sure about. In 1-2 sentences, name the two types it could be and say what you would need to know about how it was built to decide.

### Quick Check 1.1 ✅

1. A hospital's scheduling program books the first open slot for every request. A radiology program flags X-rays that look like fractures after studying thousands of labeled images. Name the type of each, and name the one question that tells them apart.
2. A friend says a chat assistant is "general AI because it can talk about anything." Correct the claim in two sentences. Name the task it was built for and one thing it cannot do.
3. Explain how a machine learning model can make a mistake that no programmer ever wrote.

---

## 1.2 Milestones: Three Eras of AI

The field is about 75 years old, and it has promised more than it delivered more than once. You can read its history as three eras, each defined by where behavior came from. Knowing the eras does two things for you. It explains why the tools on your phone work the way they do. And it gives you a pattern for judging today's claims, because twice a breakthrough brought a wave of promises and then a correction.

| Year | Milestone |
| ---- | --------- |
| 1950 | Alan Turing publishes "Computing Machinery and Intelligence" and proposes an imitation game, later called the Turing test |
| 1956 | The Dartmouth summer workshop, proposed the year before under the name "artificial intelligence," launches the field |
| 1966 | ELIZA, a program that followed scripted rules, holds typed conversations that convince some users it understood them |
| 1970s | Early promises stall, critics report that progress lags, and funding is cut: the first AI winter |
| 1980s | Expert systems encode specialist knowledge as if-then rules and sell widely, then the market collapses by the early 1990s: the second AI winter |
| 1997 | Deep Blue defeats world chess champion Garry Kasparov by searching about 200 million positions per second with scoring rules a team programmed |
| 2011 | Watson wins at Jeopardy! with a mix of learned statistics and hand-built rules |
| 2012 | AlexNet, a deep neural network, wins the ImageNet image recognition contest by a wide margin |
| 2014 | Generative adversarial networks show that a network can learn to produce new images, not only recognize them |
| 2016 | AlphaGo defeats Lee Sedol, a top Go player, at a game many experts thought was at least a decade away for computers |
| 2017 | The transformer architecture appears in the paper "Attention Is All You Need" and becomes the design behind today's language models |
| 2020 | GPT-3 shows that a large enough language model can write fluent text on almost any request |
| 2022 | ChatGPT is released to the public in November, and chat assistants become everyday tools |
| 2023 onward | Multimodal models handle text, images, and audio in one tool, and AI features appear inside office software, search, and phones |

### The Three Eras

The **rules era** ran from the 1950s into the 1990s. Behavior was written by hand, and the ceiling was how many rules a team could write and maintain. Alan Turing opened the era in 1950 with the **Turing test**, an imitation game: a machine passes if a person conversing with it by text cannot reliably tell it from a human. Deep Blue is the era's high point: a world champion beaten by brute search and programmed judgment, not by learning. Learning ideas existed from the 1950s too, but they did not win until data and hardware caught up.

The **learning era** took over in the 2000s and accelerated in 2012, when a deep network won the ImageNet contest by a margin nobody expected. The ingredients had been piling up for a decade. The web supplied the data, graphics chips supplied the speed, and new network designs made use of both. Speech-to-text, recommendations, and fraud alerts all come from this era.

The **generating era** began in 2017 with the transformer, a network design that could track relationships across long stretches of text. Scaled up, transformers became the large language models behind chat assistants. The era reached the public in November 2022.

The eras overlap, and no era retires the one before it. Rule-based systems still run payroll, traffic lights, and ticket routers. Machine learning still sorts your mail. Each new era added a type of AI to the toolbox.

### Winters and Excitement

Twice, in the 1970s and again around 1990, funding and interest collapsed in what the field calls an **AI winter**. The pattern was the same both times. A breakthrough arrived. Researchers and companies promised that human-level intelligence was close. Results lagged. Money left. Expert systems, the pride of the 1980s, cost a fortune to maintain and failed as soon as a case fell outside the rules someone had written. Companies stopped buying them, and the money left again.

This matters to you because the pattern is a reading tool. When you see a claim about what AI will do next year, ask which era's evidence it rests on and what happened the last time that claim was made. This chapter does not settle whether today's era will see a winter of its own. Chapter 9 gives you the evidence to weigh that question.

### Try It Yourself 1.2: Three Eras, One Inbox 🛠️

**Predict:** Imagine the task "sort my email into Urgent, Later, and Junk." Before you write anything, predict how a system from each era would approach the task, and which era's system would need the most human work before it could start.

**Run:** Write one sentence per era describing how its system would sort the inbox and what it would need from a person first: rules, labeled examples, or a request. Then check your three sentences against the Step 1 and Step 2 rows of the spam filter diagram in Section 1.1, and mark each prediction right, partly right, or wrong.

**Explain:** Which era's approach does your own email app most likely use today? In 1-2 sentences, name the clue that told you and the one question you would ask the vendor to confirm it.

### Quick Check 1.2 ✅

1. A friend's note-taking app learned to read their handwriting after they corrected its guesses for a week. Which era's approach is that, and which clue in the description decided it?
2. Deep Blue beat the world chess champion in 1997. Explain why it still belongs to the rules era even though the result stunned the world.
3. Describe the pattern of an AI winter in two sentences, then state one reason the pattern matters to a business deciding whether to buy an AI tool today.

---

## 1.3 The Generative Tool Landscape

The generating era put AI into a chat window, and the window is now everywhere. Before you create an account, it helps to know the kinds of tools you will meet and what each one is for. The kinds are stable. The names change every few months, so this book keeps names in callouts that can be refreshed, and the lessons stay the same.

### Five Kinds of Tools

* A **chat assistant** is a tool you talk to in plain language. It drafts, summarizes, explains, brainstorms, and answers questions. It is the main tool of this course.
* An **image generator** produces a picture from a text prompt, and most will also edit a picture you upload.
* A **research tool** answers a question with citations to sources you can open and check. It combines web search with generation, and Chapter 3 shows you how to use one without trusting it blindly.
* AI inside the apps you already use: the autocomplete in your keyboard, the meeting summary in your video-call app, the photo editor that removes a stranger from your vacation shot. You rarely choose to use this AI. It is just there.
* Specialized tools write code, clone voices, or produce video. This book names them so you recognize them. It does not teach them.

Many tools now cross these lines. A **multimodal** tool handles more than one kind of input or output, such as text and images and audio in one conversation. Most chat assistants are multimodal today, which is why the five kinds blur in practice while the jobs stay distinct.

!!! note "Tool check (verified October 2026)"
    Your course syllabus names the tools you create accounts on, drawn from the course roster. This book never requires one specific product. Every exercise that says "a chat assistant" works in any chat assistant on the roster, and every lab that needs an image or a cited source says which kind of tool to use. If a menu in your tool does not match a step in this book, look for the same action under a nearby label.

### What "Free" Means

Most tools offer a **free tier**, a version you can use at no cost with limits: a cap on messages per day, a smaller or slower model, fewer features. Paid tiers lift those limits. This course needs only free tiers. Every lab is written to fit inside them.

"Free" can also mean something less obvious. As of October 2026, many vendors' policies allow your conversations to be used to train future models unless you turn that setting off, and some allow people at the vendor to review conversations. Chapter 8 teaches you to read a tool's policy itself and find the settings. Until then, one rule covers you.

### The One Rule Before You Type

Never enter these into an AI tool: a password, a student ID, or a Social Security number. Never enter personal information about you or anyone else (address, health, finances, phone number). Never enter a classmate's work or an employer's confidential data. Treat every prompt as a note you are posting on a public bulletin board.

!!! warning "The one rule"
    If you would not post it on a public bulletin board, do not type it into an AI tool.

The rule is strict on purpose. The tool may store what you type, people may review it, and it may become training data for the next model. Later chapters refine the rule with the vendor's own policy in hand. Chapter 1 asks you to follow it without exceptions.

### Try It Yourself 1.3: The AI You Already Use 🛠️

**Predict:** Pick five apps on your phone or computer. Predict how many of them have at least one AI feature, and which of the five kinds that feature belongs to.

**Run:** Open each app's settings or help page and look for words like "smart," "suggested," "summary," or "assistant." List every AI feature you find and sort each one into one of the five kinds from this section.

**Explain:** Which feature surprised you most? In 1-2 sentences, name the type of AI from Section 1.1 you think powers it and what evidence would confirm your guess.

### Quick Check 1.3 ✅

1. A coworker wants one tool to write a first draft of a newsletter and another to find and cite three sources on a topic. Name the kind of tool for each job.
2. Explain the difference between a tool being free and a tool being private, in two sentences.
3. Your manager asks you to paste a customer's email into a chat assistant to draft a reply. Using the rule, say what you would do instead, or what you would have to remove and confirm before you did it.

---

## 1.4 Your First Conversation

Time to use one. This section walks through creating an account, sending a first prompt, reading the response the way a practitioner reads it, and saving the exchange. The saving matters most. Every lab in this course asks for your prompts and the responses you got, because the record is how you and your instructor can tell what the tool did and what you did.

### Creating an Account

1. Pick a chat assistant from your course roster and open its website.
2. Choose the sign-up option, and use the email address your syllabus tells you to use. If you are under 18, use the tool your syllabus names for students under 18.
3. If the sign-up asks for your age, answer truthfully. Vendors set age rules, and the course roster respects them.
4. Verify your email. If the tool offers to use your conversations for training, decline for now.
5. Find the free-tier limit in the tool's help pages and write it down in your prompt log, so you are not surprised when you hit it during a lab.

!!! note "Tool check (verified October 2026)"
    Menu names change. If a step above does not match what you see, look for the same action under a nearby label, and ask in the course discussion if it is not there.

### The Prompt and the Response

Your first prompt should ask for something you can check. Here is one built in three parts, with each part labeled so you can see the decision behind it. Send the prompt without the [Step] lines. They are for you, not the model.

```text
[Step 1: say who you are, so the model picks the right level]
I am a student in my first course about artificial intelligence.
[Step 2: name one task with a size and an audience, so you can tell whether it did it]
Explain what a chat assistant is in four short sentences a new student can follow.
[Step 3: ask for a check, so the conversation has a next turn]
Then ask me one question to check whether I understood.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
A chat assistant is a computer program you talk to by typing in everyday language. It is powered by an AI model that learned patterns in language from huge amounts of text. It uses those patterns to write replies that answer your questions, explain ideas, or help you draft something. Because it predicts likely words instead of looking up guaranteed facts, it can sound confident even when it is wrong.

Quick check: In your own words, why should you double-check important information that a chat assistant gives you?
```

Now read the response the way a practitioner reads it, in three passes:

1. **Did it do what I asked?** Count the sentences: four. Look for the question: there it is. The prompt's size and shape were honored.
2. **Is each claim true?** Check the four sentences against Section 1.1. A program you type to, powered by a model that learned patterns from text, which uses them to write replies: all consistent with what you read. The fourth sentence is the one to remember.
3. **What did it add that I did not ask for?** The warning in sentence four. You never asked whether the assistant could be wrong. It volunteered that, and it happens to be true. Generated text often adds things, and not all of them will be true. Chapter 2 is about that sentence and what to do with it.

Those three passes take under a minute, and you will run them on every response for the rest of this book. They are the beginning of the skill Maricopa Community Colleges lists first among this course's competencies: evaluating AI-generated responses for accuracy.

### The Same Question, Asked Again

Here is the spam filter question from Section 1.1, sent again to a chat assistant on the same day:

```text
Is a spam filter artificial intelligence? Answer in three sentences.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Yes, a spam filter is a form of artificial intelligence, because it makes decisions that normally take human judgment, such as deciding whether an email is junk. Most modern filters use machine learning, which means they learn patterns from thousands of examples of spam and legitimate messages instead of following only hand-written rules. It is a narrow kind of AI that does one task well and cannot do anything beyond sorting messages.
```

Same verdict, different words, and a third sentence the first run never offered. Run the three passes. Did it do what was asked? Three sentences, yes. Is each claim true? Check "cannot do anything beyond sorting messages" against Section 1.1: that is narrow AI, and the claim holds. What did it add? The narrow point, unasked and useful. Two runs of one prompt will never match word for word. That is why every sample in this book is labeled as a sample, and why your prompt log records what you got, not what the book got.

### Saving the Exchange: Your Prompt Log

A **prompt log** is a plain text or Markdown file where you record each prompt you send, the tool you sent it to, the date, the response you received, and your notes on it. Keep one for this course from today. The format is simple:

```text
Prompt 1 (chat assistant, [date])
PROMPT:
I am a student in my first course about artificial intelligence. [...]
RESPONSE:
A chat assistant is a computer program you talk to [...]
NOTES:
Did what I asked. Four sentences and a question. Sentence four is the
one to remember.
```

Copy the prompt and the response exactly as they appeared. Do not fix the tool's wording, and do not paraphrase. The log is evidence, and evidence you edited is no longer evidence. Every Skills Lab in this book is built from entries like this one.

### Try It Yourself 1.4: Ask It What It Is 🛠️

**Predict:** You will ask the assistant which type of AI it is, using the three types from Section 1.1. Predict its answer, and predict whether it will name one type or more than one.

**Run:** Send this prompt, then paste the prompt and the response into your prompt log with the tool and the date:

```text
Which type of AI are you: a rule-based system, a machine learning model, or generative AI? Answer in two sentences.
```

**Explain:** Compare the answer with Section 1.1. If the assistant named two types, explain in 1-2 sentences why both can be true at once. If it named one, say which type it left out and whether leaving it out was a mistake.

Compare your run with the answer one chat assistant gave in October 2026:

```text
I'm generative AI, specifically a large language model, which is a kind of machine learning model trained on huge amounts of text to produce new text. That means I'm not a rule-based system, because my responses come from patterns learned during training instead of from a list of hand-written rules.
```

### Fix It 1.1: The Prompt That Asked for Everything 🔧

A classmate wanted a quick overview of AI history for a five-minute study group and typed the first thing that came to mind.

**Symptom:** The prompt was one line:

```text
Tell me about the history of AI.
```

The response ran about 560 words under eight section headings, from "Early ideas (before 1956)" to "Recurring themes," and ended by offering to write more. Here is how it began and how it ended:

```text
# A Brief History of AI

Artificial intelligence has moved through about 75 years of big promises, disappointments, and breakthroughs. Here is an overview of the main chapters.

## Early ideas (before 1956)
People have imagined thinking machines for centuries, but the modern story begins with computing. In 1950, mathematician Alan Turing published "Computing Machinery and Intelligence," which asked whether machines can think and proposed what became known as the Turing Test.
[...]
If you'd like, I can go deeper on any period, explain how neural networks work, or focus on a particular area like robotics, chess, or language models.
```

Nothing in it was wrong. It was also useless for a five-minute study group, and the classmate had no idea which of the 560 words mattered.

**Diagnose:** Before you change a word of the prompt, name the cause in one sentence. What did the prompt leave out that the tool had to guess?

**Repair:** The prompt left out three things: how much, for whom, and in what shape. Rewrite it with all three supplied:

```text
List five milestones in the history of artificial intelligence, one per line, with the year first. Write for a community college student who has never studied AI. Stop after five lines.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
1950: Alan Turing asks "Can machines think?" and proposes a test for machine intelligence.
1956: Researchers meet at Dartmouth College and give the new field the name "artificial intelligence."
1997: IBM's Deep Blue computer beats world chess champion Garry Kasparov.
2012: A deep learning system called AlexNet wins an image recognition contest and sparks the modern AI boom.
2022: ChatGPT launches and puts AI chat assistants in the hands of millions of everyday people.
```

State what changed: the prompt now says how many (five), for whom (a new student), and in what shape (one line each, year first, then stop).

**Verify:** Count the lines: five. Check each year against the Section 1.2 table: all five match. Then notice what the repair cost you. The AI winters and the transformer paper are gone, because you asked for five milestones and the tool chose which five. A constraint trades coverage for usability, and you are the one who chooses the trade. Chapter 4 turns this repair into a method.

### Meet Copperwind

Copperwind IT Services is a fictional managed IT services provider in Phoenix. It has about 30 employees, two support teams called Deskside and Network Ops, and roughly 40 client companies across the Valley. Copperwind is deciding how to use generative AI across its teams, and it has hired you as its AI adoption assistant. Mei Lin leads the effort, and her first brief to you ships in the course data pack as `assets/code/chapter-01/copperwind-ai-inventory.txt`. You will return to Copperwind in every chapter, and each chapter gives you everything that chapter needs, so you never have to find an earlier file.

### Try It Yourself 1.5: Copperwind's First Prompt 🛠️

**Predict:** You will ask a chat assistant to write a four-sentence staff note for Mei Lin, using only the facts in a short prompt. Predict whether the response will add any detail you did not supply, and if so, what kind.

**Run:** Send this prompt, then paste the prompt and the response into your prompt log:

```text
Copperwind IT Services is a managed IT services company in Phoenix with about 30 employees and two support teams, Deskside and Network Ops. Mei Lin is leading a pilot to see how the teams could use generative AI. Write a four-sentence note from Mei Lin to all staff announcing the pilot. Do not add any facts that are not in this message.
```

**Explain:** Mark every phrase in the response that was not in your prompt, and count them. In 1-2 sentences, explain how a tool that obeys the four-sentence rule can still add things, and what that means for a note Mei Lin will send to thirty people.

Compare your run with the note one chat assistant wrote from the same prompt in October 2026. Count its additions too:

```text
Hi everyone,

I'm excited to share that Copperwind IT Services is starting a pilot to explore how we could use generative AI in our work. I'm leading the pilot, and its goal is to see how both our Deskside and Network Ops teams could put generative AI to use. This is a chance for us to learn together about what these tools can do for the way we support our customers. If you have questions or ideas, please reach out to me anytime.

Mei Lin
```

### Quick Check 1.4 ✅

1. Run the three passes on the payroll response in Section 1.1 and report what each pass finds.
2. A response is fluent, polite, and wrong about one date. Using one phrase from the chapter's first sample response in this section, explain why fluency tells you nothing about accuracy.
3. Your prompt log entry has the response but not the prompt. Explain what a reader loses, and why the log needs both.

---

## 1.5 Summary and Retrieval 💡

### Key Concepts

* AI is a family of techniques, not one thing, and the question that sorts them is where the behavior comes from. Rule-based systems follow rules a person wrote. Machine learning models learn patterns from training data. Generative AI uses learned patterns to produce new content from a prompt.
* A rule-based system counts as AI in this book when its rules stand in for a judgment a person would otherwise make. A gate, a fine schedule, or an overtime calculation follows rules and replaces no judgment, so it is not AI. Apply the test and say why.
* Every type trades something. Rules are explainable but brittle. Learned models handle the unforeseen but inherit their data's mistakes. Generative models draft and summarize on request but can be fluent and wrong at the same time, so you verify every claim.
* No tool you can use today is general AI. A chat assistant covers many topics, but it cannot reliably plan on its own, check its own facts, or learn a job it was never trained for. Treat "general" in a product claim as a claim to test.
* AI's history runs in three overlapping eras: rules (1950s-1990s), learning (2000s onward, accelerating in 2012), and generating (2017 onward, public in 2022). Twice the promises outran the results and funding collapsed in an AI winter. That pattern is a tool for reading today's claims.
* The generating era put AI into five kinds of tools: chat assistants, image generators, research tools, AI inside everyday apps, and specialized tools. Free tiers are enough for this course. One rule governs every prompt: never enter anything you would not post in public.
* Every response gets three passes: did it do what I asked, is each claim true, what did it add. Every exchange goes into a prompt log with the prompt, the tool, the date, the response, and your notes, copied exactly. Two runs of one prompt never match word for word, so the log records what you got.

### Key Terms

See course glossary for full definitions

* artificial intelligence (AI), rule-based system, expert system, machine learning, training data, model, deep learning, neural network, generative AI, prompt, large language model (LLM), narrow AI, artificial general intelligence (AGI) (Section 1.1)
* Turing test, rules era, learning era, generating era, AI winter (Section 1.2)
* chat assistant, image generator, research tool, multimodal, free tier (Section 1.3)
* prompt log (Section 1.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Name the three types of AI and, for each, say in one phrase where its behavior comes from. Then state the test this book uses to decide whether a rule-based system counts as AI.
2. Explain why no tool you can use today counts as general AI, and name two things a chat assistant cannot do that a general intelligence could.
3. List the three eras of AI in order and name one milestone from each.
4. State the one rule to follow before typing anything into an AI tool, and give two examples of what it forbids.
5. Describe the three passes you make over every response, and name the fields a prompt log entry needs so that someone else can check your work.

---

## 1.6 Skills Lab 1A: Map the AI Around You

**Goal:** Classify the AI in your life and at Copperwind by type, connect today's tools to the milestones that produced them, and hold a first documented conversation that you then check.

**Starter files:** Provided files in `assets/code/chapter-01/` from the course data pack: `skills-lab-1a-worksheet.md` (your answer file), `everyday-systems.txt` (12 systems to classify), and `copperwind-ai-inventory.txt` (Mei Lin's pilot brief and Copperwind's inventory of 8 systems). Download the data pack from Canvas, extract it, and work at the extracted `cis137` root. Open each file in any text editor. Never retype the file contents. Every AI response you need, you generate live in a chat assistant from your course roster and paste into the worksheet.

### Part 1: Foundation (Aligns with Objective 1.1)

Work in `skills-lab-1a-worksheet.md`, which has a space for every task below.

1. Classify each of the 12 systems in `everyday-systems.txt` as a rule-based system, machine learning, generative AI, or not AI. Give one line of reasoning per system, naming the clue that decided it. Where a rule-based system could also be called not AI, apply the chapter's judgment test and say which way you went.
2. Several systems can be argued two ways. Pick three. For each one, name both types it could be, state which you chose, and explain why in 2-3 sentences.
3. Choose any one system and explain in two sentences why it is not general AI.

### Part 2: Application (Aligns with Objectives 1.2 and 1.3)

1. Pick four milestones from the Section 1.2 table, at least one from each era. For each one give the milestone, the era you place it in, one tool you can use today that descends from it, and one sentence on the connection. Then defend one borderline case (Deep Blue or Watson) in two sentences.
2. List five or more apps on your phone or computer that carry at least one AI feature. For each one, name the feature, the kind of tool it belongs to (Section 1.3), and the type of AI you believe powers it.
3. Paste the prompt you sent in Try It Yourself 1.4 and the full response you received, with the tool and the date. Then write two sentences on whether the response agreed with the chapter's definitions and what, if anything, it added.

### Part 3: Extension (Aligns with Objectives 1.1, 1.2, and 1.3)

Mei Lin's brief in `copperwind-ai-inventory.txt` asks you for three things. Deliver all three in the worksheet.

1. Sort items A through H by type: rule-based system, machine learning, generative AI, or not AI. One line of reasoning each, using only what the brief says about how each system works.
2. Recommend the two items on the list, or two new uses, that make the best first pilot, and explain why in plain language a technician would accept (about 100-150 words). Name one risk you see on the list that the pilot should settle before it starts.
3. Write your own prompt that supplies only facts from the brief and asks for a four-sentence note from Mei Lin to all staff. Include at least two facts from the brief that the Try It Yourself 1.5 prompt did not use. Send it to a chat assistant, then paste the prompt and the response with the tool and the date. Mark every sentence of the response IN MY PROMPT or ADDED BY THE TOOL.

### Questions & Analysis 🤔

Answer both questions in the worksheet's final section. These answers carry significant rubric weight.

1. Two technicians use item G in Mei Lin's inventory on their own accounts to draft client emails, and nobody reviewed it. Using the chapter's rule about what never goes into an AI tool, explain what Copperwind needs to find out about item G before the pilot starts. Cite the line in the brief that makes it a risk, and say which type of AI it is.
2. Compare your Part 1 classification of system 5 (your phone keyboard's next-word suggestions) with your Part 3 classification of item D (autocomplete in Copperwind's ticket replies). Did you give them the same type? Justify your answer, and describe one thing you could observe about either system that would settle the question.

**Submission:** Submit your completed worksheet as one file named `skills-lab-1a-lastname.md`. Keep every answer under its task heading. Include every prompt you sent, the tool and date, and every response you received, pasted exactly, with your Questions & Analysis answers clearly labeled at the end.

### Rubric: Skills Lab 1A

Every Skills Lab in this book is graded with the same rubric.
Bookmark the [Skills Lab Rubric](../skills-lab-rubric.md) page for
quick reference in later chapters.

--8<-- "skills-lab-rubric.md:rubric"

---

## 1.7 Review Questions 🔄️

1. **Understand:** Explain the difference between a rule-based system and a machine learning model to someone who has never heard either term, in no more than four sentences.

2. **Apply:** A small bakery wants one tool that answers customer questions about hours and allergens from a fixed list, and another that writes its weekly social media posts. For each job, name the type of AI you would choose and the kind of tool from Section 1.3, and give one reason for each choice.

3. **Analyze:** Chat assistants are often called "general" because they answer questions on any topic. Using the chapter's definition of narrow AI, analyze why a chat assistant still counts as narrow, and name one thing a general intelligence could do that a chat assistant cannot.

4. **Evaluate:** A family clinic's front desk wants to try two AI uses. One is a chat assistant that answers patient questions about hours and parking. The other drafts appointment reminder texts from the day's schedule. Using the chapter's rule about what never goes into an AI tool, decide which use you would pilot first and which you would hold. Defend each decision with one benefit and one risk, and name the one fact that would change your answer.

---

## Further Reading 📖

* [Computing Machinery and Intelligence (Turing, 1950)](https://courses.cs.umbc.edu/471/papers/turing.pdf): The paper that asked whether machines can think and proposed the imitation game. Readable without any math.
* [A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence (1955)](http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf): The short proposal that named the field and listed the problems its founders expected to solve in one summer.
* [Attention Is All You Need (2017)](https://arxiv.org/abs/1706.03762): The transformer paper behind today's language models. Read the abstract, then notice how little of the design you need to use the tools well.
* [Stanford AI Index](https://hai.stanford.edu/ai-index): An annual report of data on where AI research, business use, and policy stand. The place to check a claim about "the current state of AI."
* [Elements of AI](https://www.elementsofai.com/): A free, plain-language course from the University of Helsinki on what AI is and how it learns. No math or programming required. For the day you want to open the box Section 1.1 closed.

---

## Looking Ahead ⏩

You can now tell the three types of AI apart, place today's tools in their era, and hold a conversation you have saved and checked. Chapter 2 opens the box this chapter closed: what a language model does with your words, why it forgets, and why it invents. The verify habit you started in Section 1.4 becomes a method you can defend.
