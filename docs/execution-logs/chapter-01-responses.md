# Chapter 1 captured responses

**Tool:** Claude (Anthropic), run through the Claude Agent SDK as a
plain chat assistant with no tools and no memory between prompts.
**Captured:** 2026-10-21 by the chapter 1 build session.
**Rule:** every sample response in `book/chapters/chapter-01.md` is
copied from this log, trimmed only with `[...]`, never edited. A later
pass may re-capture any prompt from a core-roster tool (ChatGPT,
Gemini, Copilot) and replace the sample, logging the new tool and date
here.

Each prompt was sent as a fresh conversation.

## Prompt 1 (Section 1.4 worked example, flagship 2)

```text
I am a student in my first course about artificial intelligence. Explain what a chat assistant is in four short sentences a new student can follow. Then ask me one question to check whether I understood.
```

Response:

```text
A chat assistant is a computer program you talk to by typing in everyday language. It is powered by an AI model that learned patterns in language from huge amounts of text. It uses those patterns to write replies that answer your questions, explain ideas, or help you draft something. Because it predicts likely words instead of looking up guaranteed facts, it can sound confident even when it is wrong.

Quick check: In your own words, why should you double-check important information that a chat assistant gives you?
```

## Prompt 2 (Fix It 1.1 symptom: the vague prompt)

```text
Tell me about the history of AI.
```

Response (full, 31 lines):

```text
# A Brief History of AI

Artificial intelligence has moved through about 75 years of big promises, disappointments, and breakthroughs. Here is an overview of the main chapters.

## Early ideas (before 1956)
People have imagined thinking machines for centuries, but the modern story begins with computing. In 1950, mathematician Alan Turing published "Computing Machinery and Intelligence," which asked whether machines can think and proposed what became known as the Turing Test.

## The birth of the field (1956)
The term "artificial intelligence" was coined by John McCarthy for a summer workshop at Dartmouth College in 1956. Researchers like Marvin Minsky, Claude Shannon, Allen Newell, and Herbert Simon were optimistic that human-level machine intelligence was only a generation or two away. Early programs could prove math theorems, play checkers, and even hold simple conversations (like ELIZA, a 1960s chatbot built by Joseph Weizenbaum).

## The first "AI winter" (1970s)
Progress was slower than promised. Computers were weak, problems turned out to be harder than expected, and governments cut funding after critical reports, such as the Lighthill Report in the UK (1973). This period of reduced interest and money is called an "AI winter."

## Expert systems and a second winter (1980s to early 1990s)
AI came back through expert systems, programs that captured the knowledge of human specialists as hand-written "if-then" rules. Companies spent billions on them. But the systems were expensive to maintain and broke easily outside their narrow areas, and the market collapsed, leading to a second winter.

## The rise of machine learning (1990s to 2000s)
Instead of writing rules by hand, researchers increasingly let computers learn patterns from data. Milestones included IBM's Deep Blue defeating world chess champion Garry Kasparov in 1997 and IBM's Watson winning at Jeopardy! in 2011. Machine learning quietly started powering things like spam filters, search engines, and product recommendations.

## The deep learning revolution (2010s)
Three things came together: much more data, much faster hardware (especially GPUs), and improved neural network techniques. In 2012, a deep neural network called AlexNet dramatically won an image recognition contest, and deep learning took off. In 2016, Google DeepMind's AlphaGo beat champion Lee Sedol at the game of Go, which many had thought was decades away. In 2017, researchers at Google introduced the transformer architecture, which became the foundation for modern language models.

## The generative AI era (2020s)
Large language models like GPT-3 (2020) showed that systems trained on huge amounts of text could write, summarize, and answer questions. Image generators followed, and in November 2022 the release of ChatGPT brought AI chat to the general public and reportedly reached 100 million users within a couple of months. Since then, AI tools that write text, create images, generate code, and act as assistants have spread quickly, along with serious debates about accuracy, bias, copyright, jobs, safety, and regulation.

## Recurring themes
- **Hype and correction:** Big expectations have repeatedly been followed by disappointment, then by real progress.
- **From rules to learning:** The field shifted from hand-coded rules toward systems that learn from data.
- **Data and computing power matter:** Many breakthroughs came as much from more data and faster hardware as from new ideas.

If you'd like, I can go deeper on any period, explain how neural networks work, or focus on a particular area like robotics, chess, or language models.
```

Word count of the response body: about 560 words.

## Prompt 3 (Fix It 1.1 repair)

```text
List five milestones in the history of artificial intelligence, one per line, with the year first. Write for a community college student who has never studied AI. Stop after five lines.
```

Response:

```text
1950: Alan Turing asks "Can machines think?" and proposes a test for machine intelligence.
1956: Researchers meet at Dartmouth College and give the new field the name "artificial intelligence."
1997: IBM's Deep Blue computer beats world chess champion Garry Kasparov.
2012: A deep learning system called AlexNet wins an image recognition contest and sparks the modern AI boom.
2022: ChatGPT launches and puts AI chat assistants in the hands of millions of everyday people.
```

## Prompt 4 (Try It Yourself 1.4 reference run)

```text
Which type of AI are you: a rule-based system, a machine learning model, or generative AI? Answer in two sentences.
```

Response:

```text
I'm generative AI, specifically a large language model, which is a kind of machine learning model trained on huge amounts of text to produce new text. That means I'm not a rule-based system, because my responses come from patterns learned during training instead of from a list of hand-written rules.
```

## Prompt 5 (Try It Yourself 1.5 reference run, Copperwind)

```text
Copperwind IT Services is a managed IT services company in Phoenix with about 30 employees and two support teams, Deskside and Network Ops. Mei Lin is leading a pilot to see how the teams could use generative AI. Write a four-sentence note from Mei Lin to all staff announcing the pilot. Do not add any facts that are not in this message.
```

Response:

```text
Hi everyone,

I'm excited to share that Copperwind IT Services is starting a pilot to explore how we could use generative AI in our work. I'm leading the pilot, and its goal is to see how both our Deskside and Network Ops teams could put generative AI to use. This is a chance for us to learn together about what these tools can do for the way we support our customers. If you have questions or ideas, please reach out to me anytime.

Mei Lin
```

Observation for the chapter: the response obeyed the four-sentence
limit and the no-new-facts rule, but "the way we support our
customers" and "reach out to me anytime" are additions the prompt did
not supply. Students should expect small additions even on a good
run, which is the point of the labeling task.

## Prompt 6 (Section 1.1 worked example: the spam filter question)

```text
Is a spam filter artificial intelligence? Answer in three sentences.
```

Response:

```text
Yes, most spam filters count as artificial intelligence, because they use machine learning to decide whether a message is spam. They learn from large numbers of emails that people have marked as spam or not spam, then apply the patterns they find to new messages. A simple filter that only blocks a fixed list of words would be basic rule-based automation, and some people would not call that AI.
```

## Prompt 7 (Section 1.1 worked example: the payroll question)

**Tool:** Claude (Anthropic), Sonnet, run through the Claude Code Agent
tool as a plain chat assistant with no tools, instructed to reply only
as a consumer chat assistant would. **Captured:** 2026-10-21 by the
CIS137 Planning session.

```text
Payroll software pays time-and-a-half for every hour over 40 in a week. Is that artificial intelligence? Answer in three sentences.
```

Response:

```text
No, not by itself. Payroll software that pays time-and-a-half after 40 hours follows a fixed rule that a programmer wrote in advance, so it does exactly what it was told and nothing more. Artificial intelligence usually means a system that learns patterns from data or makes judgments in situations its programmers did not spell out step by step, and this overtime calculation does neither.
```

## Prompt 8 (Section 1.4 worked example: the spam question, second run)

**Tool and capture:** same as Prompt 7. Sent as a fresh conversation,
the same text as Prompt 6, to show that two runs of one prompt differ.

```text
Is a spam filter artificial intelligence? Answer in three sentences.
```

Response:

```text
Yes, a spam filter is a form of artificial intelligence, because it makes decisions that normally take human judgment, such as deciding whether an email is junk. Most modern filters use machine learning, which means they learn patterns from thousands of examples of spam and legitimate messages instead of following only hand-written rules. It is a narrow kind of AI that does one task well and cannot do anything beyond sorting messages.
```

Observation for the chapter: same verdict as Prompt 6, different
wording, plus a third sentence (narrow AI) the first run did not offer.
