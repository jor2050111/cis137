# Chapter 1: What Artificial Intelligence Is

You used AI before breakfast. Your phone unlocked when it saw your face. Your email app moved a scam message to Junk before you could read it. Your map app routed you around a stalled truck. None of those tools asked you to type a question. Then the chat assistants arrived, and AI became something you talk to.

Every one of those systems makes a decision that used to be yours. This course puts you on the other side of that line. By the end of it you will know how these tools work and how to ask them for what you need. You will know how to catch them when they are wrong, and how to use them in ways you can defend. Copperwind IT Services, a fictional Phoenix company you will meet at the end of this chapter, has hired you to help it make exactly those calls.

This chapter builds the vocabulary. You will sort AI into three types by where its behavior comes from. You will follow the milestones that led from the first programs to today's chat assistants. You will survey the kinds of tools you will meet and create your first account. Then you will hold your first conversation and save it, because the log you keep is the habit this whole course runs on. No prior experience is expected anywhere in this chapter.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** None. This chapter starts from zero.
* **Deliverables:** Skills Lab 1A deliverable, Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **1.1 (Analyze):** Differentiate rule-based systems, machine learning, and generative AI by where each one's behavior comes from and what each can and cannot do (Section 1.1)
* **1.2 (Analyze):** Organize the milestones of AI into three eras, from hand-written rules to learned patterns to generated content, and connect each era to the tools it produced (Section 1.2)
* **1.3 (Apply):** Set up an account on a generative AI tool, hold a first conversation that follows the course's safety rule, and record the exchange in a prompt log (Sections 1.3-1.4)

### This chapter aligns with the following Course Learning Outcomes

* **CLO 2 (Analyze):** Differentiate the major types of Artificial Intelligence (AI).
* **CLO 4 (Analyze):** Analyze the current state of AI and its impact on society, including strengths and weaknesses.

---

## 1.1 One Word, Many Machines

"Artificial intelligence" sounds like one thing. It is not. **Artificial intelligence (AI)** is a family of techniques for getting computers to do tasks that normally need human judgment: recognizing a face, sorting mail, writing a paragraph, choosing a move. The techniques differ in one way that matters more than any other. Where does the behavior come from? Three answers to that question give you the three types this chapter sorts.

### Rule-Based Systems

A **rule-based system** follows instructions a person wrote out in advance. If this, then that. A thermostat schedule is one. So is tax software that applies the standard deduction when your itemized total comes out lower. So is the ticket router at an IT company that sends any subject line containing "VPN" to the network team. Nobody would call the thermostat intelligent, but the tax software and the router sit at the simple end of AI's history, and the next section shows why.

The rules era produced **expert systems**, programs that captured a specialist's knowledge as hundreds or thousands of if-then rules. A medical expert system of the 1970s could suggest a diagnosis from a list of symptoms, because doctors had written the rules it followed.

Rule-based systems have one great strength. Every decision traces back to a rule a person can read. When the system is wrong, you can find the rule and fix it. They also have one great weakness. The rule writer has to foresee every case. A scam email that avoids the word "urgent" sails past a rule that looks for it.

### Machine Learning

A **machine learning** system is not given the rules. It is given examples, and it works out the patterns on its own. The examples are its **training data**. The result is a **model**, a set of learned patterns the system uses to decide about something it has never seen before. A spam filter trained on millions of messages that people marked as junk learns what junk tends to look like. Nobody wrote the rule "messages with these forty words in this order are junk." The model found it.

Machine learning powers the face unlock, the "Because you watched" row, the fraud alert on your card, and the photo app that finds every picture of your dog. It handles cases no one wrote a rule for, and it improves as the data grows. It also learns whatever the data shows, including the mistakes and the bias in that data. Chapter 7 takes that problem seriously. And when a model is wrong, there is often no single rule to point at, which makes it harder to explain.

**Deep learning** is machine learning that uses a **neural network**, a model built from many layers of simple units that each pass a signal to the next. Deep networks are what finally made computers good at seeing and hearing, and they are the foundation of the third type.

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

Notice what the assistant did. It did not answer yes or no. It answered "it depends on the type," which is the same distinction this section draws. The table below puts the three types side by side so you can make that distinction yourself.

| | Rule-based system | Machine learning | Generative AI |
| --- | --- | --- | --- |
| Where the behavior comes from | Rules a person wrote | Patterns learned from training data | Patterns learned from data, used to produce new content |
| What it is good at | Predictable, explainable decisions | Recognizing patterns in cases no one wrote a rule for | Drafting, summarizing, translating, and making images on request |
| What breaks it | A case the rule writer did not foresee | Data that is thin, skewed, or wrong | A request it answers fluently and wrongly |
| How you check it | Read the rule that fired | Test it on cases with known answers | Verify every claim in the output |

The same job can be built three ways. Compare how each type would handle a spam filter, and watch where the human work moves:

```text
[Step 1: decide where the filter's judgment comes from]
RULE-BASED        a person writes: IF subject contains "WIRE TRANSFER" THEN Junk
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

One more distinction protects you from a lot of marketing. **Narrow AI** does one job, or a cluster of closely related jobs, and nothing else. The face unlock cannot sort your mail. The spam filter cannot write a poem. **Artificial general intelligence (AGI)** is the hypothetical system that could match human ability across any task it was handed. It does not exist. Every tool you can use today is narrow, and that includes the chat assistant that seems to do everything. It does one thing, which is generate language, and it applies that one thing to many topics.

When a product claims to be "intelligent," ask what task it was built for. That question sorts hype from capability faster than any other.

### Try It Yourself 1.1: Sort the Machines 🛠️

**Predict:** Here are six systems. (a) A calculator app. (b) A face unlock. (c) A tool that writes a cover letter from your resume. (d) An elevator that stops at the floors people pressed, in order. (e) A music app's weekly mix built from your listening. (f) A translation app. Before you look back at the table, predict which type each one is, or whether it is AI at all.

**Run:** Classify each system using the table's first row: where does its behavior come from? Write one line per system naming the type and the clue that decided it.

**Explain:** Pick the system you were least sure about. In 1-2 sentences, name the two types it could be and say what you would need to know about how it was built to decide.

### Quick Check 1.1 ✅

1. A tax program applies a rule a legislature wrote. A credit card company's fraud alert fires on a pattern the system learned from past fraud. Name the type of each, and name the one question that tells them apart.
2. A friend says a chat assistant is "general AI because it can talk about anything." Correct the claim in two sentences using the terms narrow AI and task.
3. Explain how a machine learning model can make a mistake that no programmer ever wrote.

---

## 1.2 Milestones: Three Eras of AI

The field is about 75 years old, and it has promised more than it delivered more than once. You can read its history as three eras, each defined by where behavior came from. Knowing the eras does two things for you. It explains why the tools on your phone work the way they do. And it gives you a pattern for judging today's claims, because every era began with a breakthrough, a wave of excitement, and a correction.

| Year | Milestone | Era |
| ---- | --------- | --- |
| 1950 | Alan Turing publishes "Computing Machinery and Intelligence" and proposes an imitation game, later called the Turing test | Rules |
| 1956 | A summer workshop at Dartmouth College names the field "artificial intelligence" | Rules |
| 1966 | ELIZA, a program that followed scripted rules, holds typed conversations that convince some users it understood them | Rules |
| 1970s-1980s | Expert systems encode specialist knowledge as if-then rules, and funding falls twice when results lag the promises | Rules |
| 1997 | Deep Blue defeats world chess champion Garry Kasparov by searching millions of positions with scoring rules a team programmed | Rules, at full scale |
| 2011 | Watson wins at Jeopardy! with a mix of learned statistics and hand-built rules | Learning |
| 2012 | AlexNet, a deep neural network, wins the ImageNet image recognition contest by a wide margin | Learning |
| 2016 | AlphaGo defeats Lee Sedol, a top Go player, at a game many experts thought was decades away for computers | Learning |
| 2017 | The transformer architecture appears in the paper "Attention Is All You Need" and becomes the design behind today's language models | Generating |
| 2020 | GPT-3 shows that a large enough language model can write fluent text on almost any request | Generating |
| 2022 | ChatGPT is released to the public in November, and AI chat becomes an everyday tool | Generating |
| 2023 onward | Multimodal models handle text, images, and audio in one tool, and AI features appear inside office software, search, and phones | Generating |

### The Three Eras

The **rules era** ran from the 1950s into the 1990s. Behavior was written by hand, and the ceiling was how many rules a team could write and maintain. Deep Blue is the era's high point: a world champion beaten by brute search and programmed judgment, not by learning.

The **learning era** took over in the 2000s and accelerated in 2012, when a deep neural network crushed the competition at recognizing images. Three things came together: far more data, far faster hardware, and better network designs. Spam filters, recommendations, and face unlock all come from this era.

The **generating era** began in 2017 with the transformer, a network design that could track relationships across long stretches of text. Scaled up, transformers became the large language models behind chat assistants. The era reached the public in November 2022.

The eras overlap, and no era retires the one before it. Rule-based systems still run payroll, traffic lights, and ticket routers. Machine learning still sorts your mail. Each new era added a type of AI to the toolbox. It did not empty the toolbox.

### Winters and Excitement

Twice, in the 1970s and again around 1990, funding and interest collapsed in what the field calls an **AI winter**. The pattern was the same both times. A breakthrough arrived. Researchers and companies promised that human-level intelligence was close. Results lagged. Money left. Expert systems, the pride of the 1980s, turned out to be expensive to maintain and brittle outside their narrow domains, and the market for them fell apart.

This matters to you because the pattern is a reading tool. When you see a claim about what AI will do next year, ask which era's evidence it rests on and what happened the last time that claim was made. This chapter does not settle whether today's era will see a winter of its own. Chapter 9 gives you the evidence to weigh that question.

### Try It Yourself 1.2: Three Eras, One Inbox 🛠️

**Predict:** Imagine the task "sort my email into Urgent, Later, and Junk." Before you write anything, predict how a system from each era would approach the task, and which era's system would need the most human work before it could start.

**Run:** Write one sentence per era describing how its system would sort the inbox and what it would need from a person first: rules, labeled examples, or a request.

**Explain:** Which era's approach does your own email app most likely use today? In 1-2 sentences, name the clue that told you and the one question you would ask the vendor to confirm it.

### Quick Check 1.2 ✅

1. Place these in order and name the era of each: AlexNet wins ImageNet, the Dartmouth workshop, the transformer paper.
2. Deep Blue beat the world chess champion in 1997. Explain why it still belongs to the rules era even though the result stunned the world.
3. Describe the pattern of an AI winter in two sentences, then state one reason the pattern matters to a business deciding whether to buy an AI tool today.

---

## 1.3 The Generative Tool Landscape

The generating era put AI into a chat window, and the window is now everywhere. Before you create an account, it helps to know the kinds of tools you will meet and what each one is for. The kinds are stable. The names change every few months, so this book keeps names in callouts your instructor can refresh, and the lessons stay the same.

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

"Free" can also mean something less obvious. On many tools, your conversations may be used to train future models unless you turn that setting off. Some tools let people at the vendor review conversations. Chapter 8 teaches you to read a tool's data policy and find the settings. Until then, one rule covers you.

### The One Rule Before You Type

!!! warning
    Never enter these into an AI tool: a password, a student ID, or a Social Security number. Never enter personal information about you or anyone else (address, health, finances, phone number). Never enter a classmate's work or an employer's confidential data. Treat every prompt as a note you are posting on a public bulletin board. If you would not post it there, do not type it here.

The rule is strict on purpose. The tool may store what you type, people may review it, and it may become training data for the next model. Later chapters refine the rule with the vendor's own policy in hand. Chapter 1 asks you to follow it without exceptions.

### Try It Yourself 1.3: The AI You Already Use 🛠️

**Predict:** Count the apps on your phone's home screen. Predict how many of them have at least one AI feature, and which of the five kinds that feature belongs to.

**Run:** Open each app's settings or help page and look for words like "smart," "suggested," "summary," or "assistant." List every AI feature you find and sort each one into one of the five kinds from this section.

**Explain:** Which feature surprised you most? In 1-2 sentences, name the type of AI from Section 1.1 you think powers it and what evidence would confirm your guess.

### Quick Check 1.3 ✅

1. A coworker wants one tool to write a first draft of a newsletter and another to find and cite three sources on a topic. Name the kind of tool for each job.
2. Explain the difference between a tool being free and a tool being private, in two sentences.
3. You are about to paste a customer's email into a chat assistant to draft a reply. Name two things you would remove first and say why.

---

## 1.4 Your First Conversation

Time to use one. This section walks through creating an account, sending a first prompt, reading the response the way a practitioner reads it, and saving the exchange. The saving matters most. Every lab in this course asks for your prompts and the responses you got, because the record is how you and your instructor can tell what the tool did and what you did.

### Creating an Account

!!! note "Tool check (verified October 2026)"
    Pick a chat assistant from your course roster. Go to its website and choose the sign-up option. Use the email address your syllabus tells you to use. If the sign-up asks for your age, answer truthfully, because vendors set age rules and the course roster respects them. Verify your email, and if the tool offers to use your conversations for training, decline for now. Find the free-tier limit in the help pages and write it down, so you are not surprised when you hit it during a lab.

### The Prompt and the Response

Your first prompt should ask for something you can check. Here is one built in four parts, with each part labeled so you can see the decision behind it:

```text
[Step 1: say who you are, so the model picks the right level]
I am a student in my first course about artificial intelligence.
[Step 2: name one task with a size, so you can tell if it did it]
Explain what a chat assistant is in four short sentences
[Step 3: name the audience, so the words match the reader]
a new student can follow.
[Step 4: ask for a check, so the conversation has a next turn]
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

Those three passes take under a minute, and you will run them on every response for the rest of this book. They are the beginning of the skill MCCCD lists first among this course's competencies: evaluating AI-generated responses for accuracy.

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

### Fix It 1.1: The Prompt That Asked for Everything 🔧

A classmate wanted a quick overview of AI history for a five-minute study group and typed the first thing that came to mind.

**Symptom:** The prompt was one line:

```text
Tell me about the history of AI.
```

The response ran about 560 words under eight headings, from "Early ideas (before 1956)" to "Recurring themes," and ended by offering to write more. Here is how it began and how it ended:

```text
# A Brief History of AI

Artificial intelligence has moved through about 75 years of big promises, disappointments, and breakthroughs. Here is an overview of the main chapters.

## Early ideas (before 1956)
People have imagined thinking machines for centuries, but the modern story begins with computing. In 1950, mathematician Alan Turing published "Computing Machinery and Intelligence," which asked whether machines can think and proposed what became known as the Turing Test.
[...]
If you'd like, I can go deeper on any period, explain how neural networks work, or focus on a particular area like robotics, chess, or language models.
```

Nothing in it was wrong. It was also useless for a five-minute study group, and the classmate had no idea which of the 560 words mattered.

**Diagnose:** Before you change a word of the prompt, name the cause in one sentence. What did the prompt leave out that the tool had to guess? Count the missing parts: how much, for whom, and in what shape.

**Repair:** Rewrite the prompt with the three missing parts supplied:

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

**Copperwind IT Services** is a fictional managed IT services provider in Phoenix. It has about 30 employees, two support teams called Deskside and Network Ops, and roughly 40 client companies across the Valley. Copperwind is deciding how to use generative AI across its teams, and it has hired you as its AI adoption assistant. Mei Lin leads the effort, and her first brief to you ships in the course data pack as `assets/code/chapter-01/copperwind-ai-inventory.txt`. You will return to Copperwind in every chapter, and each chapter gives you everything that chapter needs, so you never have to find an earlier file.

### Try It Yourself 1.5: Copperwind's First Prompt 🛠️

**Predict:** You will ask a chat assistant to write a four-sentence staff note for Mei Lin, using only the facts in a short prompt. Predict whether the response will add any detail you did not supply, and if so, what kind.

**Run:** Send this prompt, then paste the prompt and the response into your prompt log:

```text
Copperwind IT Services is a managed IT services company in Phoenix with about 30 employees and two support teams, Deskside and Network Ops. Mei Lin is leading a pilot to see how the teams could use generative AI. Write a four-sentence note from Mei Lin to all staff announcing the pilot. Do not add any facts that are not in this message.
```

**Explain:** Mark every phrase in the response that was not in your prompt, and count them. In 1-2 sentences, explain how a tool that obeys the four-sentence rule can still add things, and what that means for a note Mei Lin will send to thirty people.

### Quick Check 1.4 ✅

1. List the three passes a practitioner makes over every response, in order.
2. A response is fluent, polite, and wrong about one date. Using one phrase from the chapter's sample response, explain why fluency tells you nothing about accuracy.
3. Your prompt log entry has the response but not the prompt. Explain what a reader loses, and why the log needs both.

---

## 1.5 Summary and Retrieval 💡

### Key Concepts

* AI is a family of techniques, not one thing, and the question that sorts them is where the behavior comes from. Rule-based systems follow rules a person wrote. Machine learning models learn patterns from training data. Generative AI uses learned patterns to produce new content from a prompt.
* Every type trades something. Rules are explainable but brittle. Learned models handle the unforeseen but inherit their data's mistakes. Generative models draft and summarize on request but can be fluent and wrong at the same time, so you verify every claim.
* All AI you can use today is narrow. It does one job, even when that job (generating language) applies to many topics. General intelligence that matches human ability across any task does not exist.
* AI's history runs in three overlapping eras: rules (1950s-1990s), learning (2000s onward, accelerating in 2012), and generating (2017 onward, public in 2022). Each era began with a breakthrough and a wave of promises, and twice the promises outran results and funding collapsed in an AI winter.
* The generating era put AI into five kinds of tools: chat assistants, image generators, research tools, AI inside everyday apps, and specialized tools. Free tiers are enough for this course. One rule governs every prompt: never enter anything you would not post in public.
* Every response gets three passes: did it do what I asked, is each claim true, what did it add. Every exchange goes into a prompt log with the prompt, the tool, the date, the response, and your notes, copied exactly.

### Key Terms

See course glossary for full definitions

* artificial intelligence (AI), rule-based system, expert system, machine learning, training data, model, deep learning, neural network, generative AI, prompt, large language model (LLM), narrow AI, artificial general intelligence (AGI) (Section 1.1)
* Turing test, AI winter (Section 1.2)
* chat assistant, image generator, research tool, multimodal, free tier (Section 1.3)
* prompt log (Section 1.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Name the three types of AI and, for each, say in one phrase where its behavior comes from.
2. Explain why no tool you can use today counts as general AI, even a chat assistant that answers questions on any topic.
3. List the three eras of AI in order and name one milestone from each.
4. State the one rule to follow before typing anything into an AI tool, and give two examples of what it forbids.
5. Describe the three passes you make over every response, and name the fields a prompt log entry needs so that someone else can check your work.

---

## 1.6 Skills Lab 1A: Map the AI Around You

**Goal:** Classify the AI in your life and at Copperwind by type, connect today's tools to the milestones that produced them, and hold a first documented conversation that you then check.

**Starter files:** Provided files in `assets/code/chapter-01/` from the course data pack: `skills-lab-1a-worksheet.md` (your answer file), `everyday-systems.txt` (12 systems to classify), and `copperwind-ai-inventory.txt` (Mei Lin's pilot brief and Copperwind's inventory of 8 systems). Download the data pack from Canvas, extract it, and work at the extracted `cis137` root. Open each file in any text editor. Never retype the file contents. Every AI response you need, you generate live in a chat assistant from your course roster and paste into the worksheet.

### Part 1: Foundation (Aligns with Objective 1.1)

Work in `skills-lab-1a-worksheet.md`, which has a numbered space for every answer below.

1. Classify each of the 12 systems in `everyday-systems.txt` as a rule-based system, machine learning, generative AI, or not AI. Fill in the worksheet's table with one line of reasoning per system, naming the clue that decided it.
2. Three of the systems can be argued two ways. Pick three, and for each one name both types it could be, state which you chose, and explain why in 2-3 sentences.
3. Choose any one system and explain in two sentences why it is narrow AI and not general AI.

### Part 2: Application (Aligns with Objectives 1.2 and 1.3)

1. Pick four milestones from the Section 1.2 table, at least one from each era. For each, name the era and one tool you can use today that descends from it, with one sentence on the connection.
2. Inventory the apps on your own phone or computer that carry at least one AI feature. List five or more. For each, name the feature, the kind of tool it belongs to (Section 1.3), and the type of AI you believe powers it.
3. Paste the prompt you sent in Try It Yourself 1.4 and the full response you received, with the tool and the date. Then write two sentences on whether the response agreed with the chapter's definitions and what, if anything, it added.

### Part 3: Extension (Aligns with Objectives 1.1 and 1.3)

Mei Lin's brief in `copperwind-ai-inventory.txt` asks you for three things. Deliver all three in the worksheet.

1. Sort items A through H by type: rule-based system, machine learning, generative AI, or not AI. One line of reasoning each, using only what the brief says about how each system works.
2. Recommend the two items on the list, or two new uses, that make the best first pilot, and explain why in plain language a technician would accept (about 100-150 words). Name one risk you see on the list that the pilot should settle first.
3. Generate the staff note Mei Lin asked for. Write your own prompt that supplies only facts from the brief and asks for a four-sentence note. Send it to a chat assistant, then paste the prompt and the response with the tool and the date. Then label every sentence of the response FROM MY PROMPT, FROM THE BRIEF, or INVENTED BY THE TOOL.

### Questions & Analysis 🤔

Answer both questions in the worksheet's final section. These answers carry significant rubric weight.

1. Item G in Mei Lin's inventory is a chat assistant two technicians use on their own accounts to draft client emails, and nobody reviewed it. Using the chapter's rule about what never goes into an AI tool, explain what Copperwind needs to find out about item G before the pilot starts. Cite the line in the brief that makes it a risk and say which type of AI it is.
2. Compare your Part 1 classification of system 5 (your phone keyboard's next-word suggestions) with your Part 3 classification of item D (autocomplete in Copperwind's ticket replies). Did you give them the same type? Justify your answer, and describe one thing you could observe about either system that would settle the question.

**Submission:** Submit your completed worksheet as one file named `skills-lab-1a-lastname.md`. Keep every numbered answer under its part heading. Include every prompt you sent, the tool and date, and every response you received, pasted exactly, with your Questions & Analysis answers clearly labeled at the end.

### Rubric: Skills Lab 1A

Every Skills Lab in this book is graded with the same rubric.
Bookmark the [Skills Lab Rubric](../skills-lab-rubric.md) page for
quick reference in later chapters.

--8<-- "skills-lab-rubric.md:rubric"

---

## 1.7 Review Questions 🔄️

1. **Understand:** Explain the difference between a rule-based system and a machine learning model to someone who has never heard either term, in no more than four sentences.

2. **Apply:** A small bakery wants one tool that answers customer questions about hours and allergens from a fixed list, and another that writes its weekly social media posts. For each job, name the type of AI you would choose and the kind of tool from Section 1.3, and give one reason for each choice.

3. **Analyze:** Chat assistants are often called "general" because they answer questions on any topic. Using the chapter's definition of narrow AI, analyze why a chat assistant still counts as narrow, and name one task a general intelligence could do that a chat assistant cannot.

4. **Evaluate:** Mei Lin's brief lists eight systems. Choose the two you would pilot first and the one you would leave alone, and defend each choice with one benefit and one risk drawn from the brief itself.

---

## Further Reading 📖

* [Computing Machinery and Intelligence (Turing, 1950)](https://courses.cs.umbc.edu/471/papers/turing.pdf) - The paper that asked whether machines can think and proposed the imitation game. Readable without any math.
* [A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence (1955)](http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf) - The short proposal that named the field and listed the problems its founders expected to solve in one summer.
* [Attention Is All You Need (2017)](https://arxiv.org/abs/1706.03762) - The transformer paper behind today's language models. Read the abstract, then notice how little of the design you need to use the tools well.
* [Stanford AI Index](https://hai.stanford.edu/ai-index) - An annual report of data on where AI research, business use, and policy stand. The place to check a claim about "the current state of AI."
* [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) - A free, plain-language introduction to how models learn from data, for the day you want to open the box Section 1.1 closed.

---

## Looking Ahead ⏩

You can now tell the three types of AI apart, place today's tools in their era, and hold a conversation you have saved and checked. Chapter 2 opens the box this chapter closed: what a language model does with your words, why it forgets, and why it invents. The verify habit you started in Section 1.4 becomes a method you can defend.
