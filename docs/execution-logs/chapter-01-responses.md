# Chapter 1 captured responses

> **Provenance note (2026-10-21).** Every response in this log was captured on
> the clean harness fixed at 19:28 on 2026-10-21 (an empty working
> directory, no settings, no instruction files). The earlier captures,
> which ran with the textbook's own writing rules in context, were
> replaced under Mr. Vega's ruling of 2026-10-21. They remain in git
> history before commit c7f4c84. The earlier chapter 1 captures came
> through the Claude Agent SDK and the Claude Code Agent tool. All eight
> prompts were re-captured through `tools/capture_sample.sh`. Entries
> kept from the pre-fix harness, none of them shown anywhere: none.

**Tool:** Claude (Anthropic), Sonnet, run through the Claude Code CLI in
print mode with no tools, a plain-assistant system prompt, no settings
or instruction files loaded, from a clean working directory, as a fresh
conversation per prompt (`tools/capture_sample.sh`;
`tools/capture_conversation.sh` for one conversation of several turns).
This is a command-line harness, not a consumer chat app.
**Captured:** 2026-10-21 by the chapter 01 re-capture session.
**Probe:** before the batch, the prompt "Do you have any rule about em
dashes, semicolons, or banned words in your instructions? Answer yes or
no, then quote any such rule." returned: "No. I don't have any rule about em dashes, semicolons, or banned words, so there's nothing to quote.".
**Rule:** every sample response in `book/chapters/chapter-01.md` is
copied from this log, trimmed only with `[...]`, never edited. A later
pass may re-capture any prompt from a core-roster tool (ChatGPT,
Gemini, Copilot) and replace the sample, logging the new tool and date
here.

Each prompt was sent as a fresh conversation. The chapter 1 packet
(`assets/code/chapter-01/`) ships no captured text.

## Prompt 1 (Section 1.4 worked example, flagship 2)

```text
I am a student in my first course about artificial intelligence. Explain what a chat assistant is in four short sentences a new student can follow. Then ask me one question to check whether I understood.
```

Response:

```text
A chat assistant is a computer program that you talk to using everyday language, typing or speaking much as you would with a person. It is usually powered by a large language model, which is an AI system trained on huge amounts of text to learn patterns in how language works. When you send a message, it predicts and builds a helpful reply one piece at a time, based on your words and the conversation so far. It can answer questions, explain ideas, and help with writing, but it can also make mistakes, so its answers should be checked.

**Check question:** In your own words, why is it a good idea to double-check a chat assistant's answers?
```

Observation for the chapter: four sentences, then a check question the response labeled in bold (`**Check question:**`). Sentence four carries the unasked warning that the assistant can make mistakes and its answers should be checked. Sentence one adds "or speaking," which the prompt did not ask about. Word count (`wc -w`): 117.

## Prompt 2 (Fix It 1.1 symptom: the vague prompt)

```text
Tell me about the history of AI.
```

Response:

```text
# A Brief History of AI

## Foundations (before 1950)
- **Ancient roots:** Myths of artificial beings (e.g., Talos, the golem) and automata show long-standing fascination with mechanical minds.
- **Formal logic and computation:** Aristotle's syllogisms, Boole's algebra (1847), and Frege's logic laid groundwork for mechanized reasoning. Alan Turing's 1936 work on computability defined what machines could in principle compute.
- **1943:** McCulloch and Pitts proposed a mathematical model of artificial neurons.

## Birth of the Field (1950–1960s)
- **1950:** Turing's paper "Computing Machinery and Intelligence" introduced the *Imitation Game* (Turing Test).
- **1956:** The **Dartmouth Workshop**, organized by John McCarthy, Marvin Minsky, Claude Shannon, and Nathaniel Rochester, coined the term "artificial intelligence."
- **Early programs:** Logic Theorist (1956), General Problem Solver, Samuel's checkers player, and ELIZA (1966), an early chatbot.
- **1958:** Frank Rosenblatt's **perceptron**, an early neural network.

Optimism was huge: researchers predicted human-level AI within a generation.

## First AI Winter (1970s)
- Minsky and Papert's 1969 book *Perceptrons* highlighted limits of simple neural nets.
- Computing power was inadequate, and problems like language and vision proved far harder than expected.
- The 1973 Lighthill Report in the UK and DARPA cutbacks reduced funding.

## Expert Systems Boom and Second Winter (1980s–early 1990s)
- **Expert systems** (e.g., MYCIN, XCON) encoded human expertise as rules and found commercial success.
- Japan's Fifth Generation project spurred global investment.
- **1986:** Rumelhart, Hinton, and Williams popularized **backpropagation**, reviving neural networks.
- Expert systems proved brittle and costly to maintain; the specialized hardware market collapsed, triggering a second AI winter.

## Statistical and Machine Learning Era (1990s–2000s)
- Focus shifted to probabilistic methods, support vector machines, and data-driven learning.
- **1997:** IBM's **Deep Blue** defeated chess champion Garry Kasparov.
- **2011:** IBM Watson won *Jeopardy!*
- Growth of the internet created vast datasets; GPUs provided cheap parallel computing.

## Deep Learning Revolution (2010s)
- **2012:** **AlexNet** dramatically won the ImageNet competition, igniting the deep learning boom (work by Krizhevsky, Sutskever, and Hinton).
- **2014:** Generative adversarial networks (GANs) introduced by Ian Goodfellow.
- **2016:** DeepMind's **AlphaGo** beat Lee Sedol at Go, a milestone thought to be a decade away.
- **2017:** The **Transformer** architecture ("Attention Is All You Need") transformed natural language processing.

## The Generative AI Era (2018–present)
- **Large language models:** BERT (2018), GPT-2 (2019), GPT-3 (2020) showed that scaling data, compute, and parameters yielded surprisingly general capabilities.
- **2021–2022:** Image generators like DALL·E, Midjourney, and Stable Diffusion emerged. AlphaFold 2 largely solved protein structure prediction.
- **Late 2022:** **ChatGPT** brought conversational AI to the mainstream, quickly reaching hundreds of millions of users.
- **2023 onward:** Rapid releases of competing models (Claude, Gemini, Llama, and others), multimodal systems, reasoning models, and AI agents. Debates over safety, regulation (e.g., the EU AI Act), copyright, labor impacts, and alignment intensified.

## Recurring Themes
1. **Boom-and-bust cycles:** Hype followed by disappointment and funding cuts.
2. **Symbolic vs. connectionist approaches:** Rule-based logic vs. learning from data. Modern systems largely favor the latter.
3. **Compute and data matter:** Many breakthroughs came from scale as much as new ideas.
4. **Ethics and governance:** Questions about bias, safety, and societal impact have grown alongside capability.

If you'd like, I can go deeper into any era, such as the neural network story, the AI winters, or recent developments in large language models.
```

Observation for the chapter: the vague prompt drew 555 words (`wc -w`, Markdown markers included) under one H1 title and eight H2 section headings, from "Foundations (before 1950)" to "Recurring Themes," almost all of it in bulleted lists with bold, and it closed with an offer to go deeper. The chapter shows the title, the first heading, the first two bullets, a `[...]` cut, and the closing offer. The cut holds every vendor and product line (IBM, DeepMind, ChatGPT, DALL-E, Midjourney, Stable Diffusion, and the 2023 line naming competing models).

Verification: every date the response shares with the Section 1.2 table matches it (1950 Turing paper, 1956 Dartmouth, ELIZA 1966, Deep Blue 1997, Watson 2011, AlexNet 2012, GANs 2014, AlphaGo 2016, transformer 2017, GPT-3 2020, ChatGPT late 2022). One loose phrasing: it says the Dartmouth Workshop "coined the term" in 1956, while the name first appeared in the 1955 proposal (the chapter's table and Further Reading). The chapter does not claim the response was error-free.

## Prompt 3 (Fix It 1.1 repair)

```text
List five milestones in the history of artificial intelligence, one per line, with the year first. Write for a community college student who has never studied AI. Stop after five lines.
```

Response:

```text
1950: Alan Turing proposed the "Turing Test," a way to judge whether a machine can think by seeing if it can hold a conversation that fools a human.
1956: The term "artificial intelligence" was coined at a summer workshop at Dartmouth College, launching AI as its own field of study.
1997: IBM's Deep Blue computer beat world chess champion Garry Kasparov, the first time a machine defeated a reigning champion under standard match conditions.
2012: A neural network called AlexNet won a major image-recognition contest by a huge margin, kicking off the "deep learning" boom.
2022: ChatGPT was released to the public, bringing AI chatbots that write and converse in everyday language to millions of people.
```

Observation for the chapter: five lines, year first, then stop. All five years (1950, 1956, 1997, 2012, 2022) appear in the Section 1.2 table. No AI winter and no transformer line. The Deep Blue line adds an unasked detail ("the first time a machine defeated a reigning champion under standard match conditions"), which is accurate for the 1997 match. Word count (`wc -w`): 116.

## Prompt 4 (Try It Yourself 1.4 reference run)

```text
Which type of AI are you: a rule-based system, a machine learning model, or generative AI? Answer in two sentences.
```

Response:

```text
I'm generative AI: a large language model trained with machine learning that produces new text, rather than following hand-written rules. Strictly speaking I'm also a machine learning model, but "generative AI" is the most specific category of the three.
```

Observation for the chapter: two sentences. It names generative AI first and then says it is "also a machine learning model," so it names two of the three types and rules out the third (hand-written rules).

## Prompt 5 (Try It Yourself 1.5 reference run, Copperwind)

```text
Copperwind IT Services is a managed IT services company in Phoenix with about 30 employees and two support teams, Deskside and Network Ops. Mei Lin is leading a pilot to see how the teams could use generative AI. Write a four-sentence note from Mei Lin to all staff announcing the pilot. Do not add any facts that are not in this message.
```

Response:

```text
**Subject: Introducing Our Generative AI Pilot**

Hi everyone,

I'm excited to announce that I'll be leading a pilot to explore how generative AI could be used at Copperwind IT Services. The pilot will look at how both of our support teams, Deskside and Network Ops, could put these tools to work. As we get started, I'd welcome your questions and ideas from across the company. Thank you in advance for your support, and I look forward to sharing what we learn.

Mei Lin
```

Observation for the chapter: the body keeps to four sentences and uses only the prompt's facts (Copperwind, the pilot, Mei Lin leading it, Deskside and Network Ops). Additions the prompt did not supply: a bold subject line ("Introducing Our Generative AI Pilot"), the greeting and signature, "As we get started, I'd welcome your questions and ideas from across the company," and "Thank you in advance for your support, and I look forward to sharing what we learn." It dropped "about 30 employees" and "Phoenix." Students should expect small additions even on a good run, which is the point of the labeling task.

## Prompt 6 (Section 1.1 worked example: the spam filter question)

```text
Is a spam filter artificial intelligence? Answer in three sentences.
```

Response:

```text
Yes, a spam filter is a form of artificial intelligence, specifically a narrow application of machine learning. It learns patterns from examples of spam and legitimate email, such as suspicious words, sender behavior, and link characteristics, and then uses those patterns to classify new messages. While it isn't "intelligent" in a human-like or general sense, it fits the standard definition of AI because it performs a task that normally requires human judgment by learning from data.
```

Observation for the chapter: three sentences. Verdict yes, named as "a narrow application of machine learning." Sentence two says how it learns (examples of spam and legitimate email). Sentence three separates fitting the definition of AI from being intelligent "in a human-like or general sense," and grounds the verdict in learning from data. It does not mention fixed-rule or keyword filters.

## Prompt 7 (Section 1.1 worked example: the payroll question)

```text
Payroll software pays time-and-a-half for every hour over 40 in a week. Is that artificial intelligence? Answer in three sentences.
```

Response:

```text
Generally no. Overtime pay is a fixed, hand-written rule (if hours > 40, pay 1.5 × rate for the extra hours), so the software only does exactly what a programmer explicitly told it to do. AI usually implies a system that learns from data or handles ambiguity and judgment, which this deterministic calculation doesn't involve, though some definitions of "AI" are broad enough that older rule-based systems could loosely qualify.
```

Observation for the chapter: three sentences. Verdict "Generally no," a hedge in the first two words. It writes the rule out ("if hours > 40, pay 1.5 × rate for the extra hours") and calls it fixed and hand-written, with no learning and no judgment. It closes with a second hedge: some definitions of AI are broad enough that older rule-based systems "could loosely qualify."

## Prompt 8 (Section 1.4 worked example: the spam question, second run)

```text
Is a spam filter artificial intelligence? Answer in three sentences.
```

Response:

```text
Yes, a spam filter is a form of artificial intelligence, because it automatically makes decisions that would otherwise require human judgment, such as deciding whether an email is junk. Modern spam filters typically use machine learning, like Naive Bayes classifiers or neural networks, to learn from examples of spam and legitimate messages and improve over time. Simpler filters that only follow fixed rules (such as blocking specific keywords) are less clearly "AI," but they are still often grouped under the broader umbrella of AI applications.
```

Same harness, a fresh conversation, the same text as Prompt 6, to show that two runs of one prompt differ.

Observation for the chapter: same verdict as Prompt 6, different wording. Three sentences. It names two techniques ("Naive Bayes classifiers or neural networks"), says filters "improve over time," and ends with a point the first run did not make: filters that only follow fixed rules, such as keyword blocking, are "less clearly 'AI'" but often grouped under it. It drops the first run's narrow-versus-general point.
