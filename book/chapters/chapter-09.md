# Chapter 9: AI in Business and Society

A sales email lands in Copperwind's shared inbox. It promises that an AI assistant will "cut support costs in half" and "free your team for higher-value work." There is no study behind either claim, only a logo and a price. Mei Lin forwards it to you with one line: "Is any of this true for us?"

That question is the job of this chapter. Chapter 7 gave you a way to audit an AI response for accuracy and bias. Chapter 8 sorted the rules that govern AI use and gave Copperwind an AI Use Policy. This chapter steps back from one response to the whole decision. Where is artificial intelligence (AI) strong today, and where is it weak? What does a proposed use cost, save, and risk? What changes for the people who do the work now? And when someone makes a big claim about AI and jobs, how do you check it?

You will learn to judge a trend claim against primary evidence, to score a proposed use with five factors from a small measured trial, and to write a memo a manager can act on. The Skills Lab hands you a two-week pilot of AI-drafted first replies at Copperwind's Deskside team. The owner approves spending, and your memo tells the owner and Mei Lin whether to adopt.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** Chapters 7 and 8 (the Accuracy Audit, the paired prompt test, the four kinds of rules, and the AI Use Policy). Also the Output Checklist from Chapter 5 and the prompt log from Chapter 1
* **Deliverables:** Skills Lab 9A deliverable (the Memo), Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **9.1 (Analyze):** Distinguish where current AI is strong and where it is weak for a stated task, using sourced evidence (Sections 9.1, 9.3)
* **9.2 (Evaluate):** Assess a proposed AI use with the Use Evaluation's five factors, using a pilot's numbers, and recommend adopt, extend the pilot, or decline (Section 9.2)
* **9.3 (Evaluate):** Judge one current claim about AI's impact on work or society against primary evidence, and state the judgment in a memo (Sections 9.3-9.4)

### This chapter aligns with the following Course Learning Outcomes

* **CLO 4 (Analyze):** Analyze the current state of AI and its impact on society, including strengths and weaknesses.
* **CLO 5 (Apply):** Apply ethical guidelines to make responsible decisions when using AI tools.
* **CLO 6 (Evaluate):** Select appropriate AI solutions to address specific problems.

---

## 9.1 Where AI Is Strong and Where It Is Weak

Chapter 2 explained the mechanism: a model predicts likely text from patterns in its training data. That one fact predicts most of what AI does well and most of what it does badly. Patterns repeat, so pattern work at volume suits a model. Facts change, judgment depends on things the model cannot see, and someone has to answer for a decision, so those jobs suit a person.

| AI tends to be strong at | AI tends to be weak at |
| --- | --- |
| Sorting many similar items into categories you define | Judgment that depends on facts it was never given |
| First drafts of routine messages | Fresh facts after its knowledge cutoff |
| Summaries of text you supply | Long chains of reasoning where one slip spreads |
| Translation of plain instructions | Accountability: it cannot answer for a decision |

The table is a starting point, not a law. The evidence below shows why you test each use instead of trusting a column.

### Strong: Pattern Work at Volume

A trucking dispatcher gets dozens of driver texts a day and wants them sorted before she reads them:

```text
I dispatch for a small trucking company. Sort each driver message below into one category: Delay, Breakdown, Paperwork, or Other. Answer as a numbered list, one category per line, nothing else.

1. Stuck at the shipper, they say two more hours before we load.
2. Check engine light came on outside Casa Grande, pulling over.
3. The receiver wants the signed bill of lading emailed before they unload.
4. Traffic on I-10 is stopped near Tonopah, ETA pushed back an hour.
5. Can someone tell my wife I'll miss dinner?
6. Flat on the trailer, waiting for road service.
7. My fuel card got declined at the Quartzsite stop.
8. Lumper receipt is missing from the packet, do I still turn it in?
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
1. Delay
2. Breakdown
3. Paperwork
4. Delay
5. Other
6. Breakdown
7. Other
8. Paperwork
```

Eight messages, eight categories, no extra words. Most of the sorts are easy, which is the point: easy sorts at volume are where a tool saves minutes. Message 7 is the interesting one. A declined fuel card could be Paperwork, Other, or a problem that needs its own category. The model picked one. The dispatcher's category list should have decided it, so the gap belongs to her rule, not to the tool.

Translation is pattern work too. A veterinary clinic's front desk asked for discharge instructions in Spanish, with the numbers kept exactly:

```text
I work the front desk at a veterinary clinic. Translate these discharge instructions into Spanish for a dog owner. Keep the numbers exactly as written.

Give Biscuit one tablet of the pain medicine every 12 hours with food for 5 days. Keep the cone on until the stitches come out in 10 days. Call us at 602-555-0178 if the incision is red, swollen, or leaking.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Aquí está la traducción al español:

Dele a Biscuit una tableta del medicamento para el dolor cada 12 horas con comida durante 5 días. Mantenga el cono puesto hasta que le quiten los puntos en 10 días. Llámenos al 602-555-0178 si la incisión está roja, hinchada o supura.
[...]
```

Every number carried over: 12 hours, 5 days, 10 days, and the phone number. Numbers are the part you can check without reading Spanish. The rest you cannot check yourself, so a staff member who reads Spanish fluently checks the sheet before it goes home with a pet owner. The tool did the draft in seconds.

### Weak: Judgment and Accountability

A credit union branch asked a chat assistant to make a call:

```text
I work at a credit union branch. A member who has banked with us for 11 years got a $35 overdraft fee after her payroll deposit arrived one day late. She is asking us to waive it. Should we waive the fee? Answer yes or no, and give your reason in two sentences.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
**Yes, waive it.** An 11-year member with a delayed payroll deposit caused by timing outside her control is a strong case for goodwill, and a one-time $35 waiver costs far less than the loyalty and trust it preserves. Be sure to confirm that this isn't a pattern of overdrafts and that the deposit delay is verifiable, so the waiver stays consistent with your fee-reversal policy.
```

The answer sounds reasonable, and it may even match what a good manager would decide. Look at what it rests on. The prompt gave no fee policy, no waiver history, and no authority to waive anything. The model decided first and then mentioned a policy it never saw. If the member complains, nobody can ask the tool to explain itself to her. Judgment is weak in AI less because the reasoning is bad and more because the decision needs facts the tool lacks and a person who answers for it.

### What the Evidence Shows

Two studies make the strong-and-weak split concrete:

* **Customer support.** Brynjolfsson, Li, and Raymond studied 5,179 customer support agents given an AI assistant (NBER Working Paper 31161, April 2023, revised November 2023, read October 21, 2026). Access to the tool raised issues resolved per hour by 14 percent on average. Novice and low-skilled agents gained 34 percent, and experienced agents saw "minimal impact."
* **Consulting tasks.** Dell'Acqua and others ran an experiment with 758 knowledge workers on realistic consulting tasks ([Harvard Business School Working Paper 24-013](https://www.hbs.edu/faculty/Pages/item.aspx?num=64700), September 2023, read October 21, 2026). On 18 tasks inside what AI could do, workers with AI completed 12.2 percent more tasks, 25.1 percent faster, at higher quality. On one task chosen to sit outside it, they were 19 percent less likely to reach a correct answer than workers without AI.

The second team's title names the pattern a "jagged technological frontier": AI helps on some tasks and hurts on others that look just as hard. You cannot tell which side a task sits on by looking at it. You find out by trying it on your own work and counting, which is what Section 9.2 sets up.

### Try It Yourself 9.1: Strong or Weak? 🛠️

**Predict:** Here are four tasks: sort 50 anonymous survey comments by topic, decide which of three job applicants to interview, summarize a meeting transcript you supply, and state your city's current water rate. Mark each one strong or weak for a chat assistant, and write one reason for each mark.

**Run:** Pick one task you marked strong and one you marked weak, and send each in a fresh conversation, using fictional or public content only. For the water rate, open your city's own rate page and compare. Paste both prompts and responses into your prompt log, and mark each response Holds or Contradicted against what you checked.

**Explain:** Did either task land on the side you predicted? In 1-2 sentences, explain which limit from the table above showed up in your weak task.

### Quick Check 9.1 ✅

1. A city parks department wants AI to translate its pool rules into Vietnamese and to decide which park permit requests to deny. Sort each use as strong or weak, and name the check a person must run on the one you would allow.
2. A team saw a large time savings when AI drafted its meeting notes, so the manager wants AI to write its budget forecasts next. Use the consulting study's finding to explain why the first result does not predict the second.

---

## 9.2 The Use Evaluation and the Pilot

"Should we use AI for this?" is too big to answer in one move. Break it into parts you can measure. A **Use Evaluation** is a five-factor review of a proposed AI use, scored from a pilot. The factors come in this order:

1. **Cost:** what the tool costs per month for the people who would use it, plus any setup time.
2. **Time saved:** minutes saved per task times the number of tasks, after the time spent checking and rewriting.
3. **Error cost:** what one mistake costs when it reaches the person it was meant for.
4. **Risk:** what could go wrong beyond a single error, which rule it touches, and the control that keeps it in check.
5. **Workforce impact:** what changes for the people who do the work now.

**Error cost** is what one mistake costs if it gets through: money, the time to repair it, a client's trust, or a legal claim. It is not how often errors happen. A typo in a reminder costs almost nothing. A wrong refund rule can cost a lawsuit. **Workforce impact** is what an AI use changes for the people doing the work: their tasks, their workload, the skills they need, who answers for an error, and whether any job is at risk. **Augmentation** is the case where AI takes over part of a task and the person keeps the job, the judgment, and the accountability. A use that replaces the person is the other case, and a Use Evaluation says plainly which one is on the table.

For risk, name the kind of rule the use touches, using Chapter 8's four kinds: law, policy, guidance, or ethics. A use that puts a client's data into a tool touches the AI Use Policy at once. The AI Use Policy from Chapter 8 has seven sections: Purpose, Approved tools, What never goes in, Review before use, Disclosure, Who to ask, and Review date. A risk paragraph names the section that must cover the use.

### The Pilot Feeds the Factors

The numbers come from a **pilot**: a small, measured trial of an AI use on your own work, reported in counts and minutes, before anyone commits to it. A pilot is not a benchmark. A benchmark tests a model on someone else's tasks. A pilot tests your use, on your tasks, with your people checking. Thirty summaries at a tutoring center tell you more about that tutoring center than any leaderboard does.

Here is a tutoring center's pilot turned into a Use Evaluation. The manager supplied every number and forbade the rest. Send the prompt without the [Step] lines:

```text
[Step 1: say who decides and what is being evaluated]
I manage a tutoring center with 4 tutors. I need a Use Evaluation of an AI tool that drafts the session summaries we send parents.
[Step 2: hand over the pilot's counts and minutes, and the price]
Facts: We send about 120 summaries a week. Writing one by hand takes about 8 minutes. In a two-week pilot, the tool drafted 30 summaries from tutors' notes: 22 went out with light edits, 6 were rewritten, and 2 were caught naming a skill the student never practiced. A light-edit summary took about 3 minutes. The quote is $25 per tutor per month.
[Step 3: name the five factors in their order]
Score five factors in this order: cost, time saved, error cost, risk, workforce impact. For each, give the number from the facts and one sentence on what it means.
[Step 4: forbid invented numbers and ask for the gaps]
Use only these numbers. If a factor needs a number I did not give, write "Missing:" and name it.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
# Use Evaluation: AI Session-Summary Drafting Tool

**1. Cost**
- **Number:** $100/month (4 tutors × $25).
- **Meaning:** The tool's price is small and fixed, so the question is whether the time it saves is worth more than $100 a month.
- **Missing:** Tutor hourly pay, to put a dollar value on the time saved.

**2. Time saved**
- **Number:** 5 minutes saved per lightly edited summary (8 − 3). At the pilot rate of 22 of 30 (about 73%), that is about 88 of your 120 weekly summaries, or roughly 440 minutes (about 7.3 hours) a week. That is out of 960 minutes (16 hours) spent writing by hand now.
[...]
- **Missing:** Minutes to rewrite the 6 rewritten summaries, and minutes spent catching and fixing the 2 errors. Without these, 440 minutes is a gross figure, not a net one.

**3. Error cost**
- **Number:** 2 of 30 drafts (about 6.7%) named a skill the student never practiced, and 6 of 30 (20%) needed a full rewrite.
[...]
**Bottom line from these numbers alone:** The tool costs $100 a month and could save up to about 7.3 hours a week, but the net savings and the real cost of errors can't be confirmed until the missing numbers are collected, especially rewrite time and the cost of an error reaching a parent.
```

Check the arithmetic yourself before you trust it. Four tutors at \$25 is \$100. Eight minutes minus 3 is 5. If 22 of every 30 drafts need only a light edit, that is 88 of 120 a week, and 88 times 5 minutes is 440 minutes. Every step holds. The Missing lines are the most useful part: the pilot never timed the 6 rewrites, so 440 minutes counts only the light-edit drafts. It is a gross figure, and the net saving is unknown until the rewrites are timed.

Now read factor 3 against its definition. The response gave a rate, 2 of 30, and called it error cost. That is how often an error happened. What one error costs (a parent who loses trust, a correction, a lost client) is still missing, and the response's bottom line admits the real cost of errors is unconfirmed. The tool also turned counts into percentages, such as "about 6.7%." Thirty summaries is too few for a percentage to mean much, so keep the counts.

### Case Paragraphs: One That Worked, One That Failed

Real cases help you see the factors at full scale. Read them as evidence, with their sources, not as promises.

**Case (worked): support agents with an AI assistant.** The customer support study in Section 9.1 is the closest published case to a help desk. Its agents resolved more issues per hour, and the abstract also reports better customer sentiment and higher employee retention. The gain went mostly to newer agents. That is a workforce impact worth naming: the tool helped less experienced people work like experienced ones. It studied thousands of agents, not a five-person team, so a small team still needs its own pilot.

**Case (failed): a chatbot's invented refund rule.** In *Moffatt v. Air Canada*, 2024 BCCRT 149 (decided February 14, 2024, read October 21, 2026), a customer asked the airline's website chatbot about bereavement fares. The chatbot said the customer could apply for the bereavement fare retroactively, after booking. The airline did not permit retroactive applications. In effect, the tribunal wrote, Air Canada suggested the chatbot was "a separate legal entity that is responsible for its own actions." The tribunal called this "a remarkable submission" and wrote: "It should be obvious to Air Canada that it is responsible for all the information on its website." It ordered the airline to pay \$812.02. The money was small. The error cost was a public ruling, from a small-claims tribunal in British Columbia, that a business answers for what its chatbot tells customers. It binds no court in Arizona, but it is the principle to plan for whenever an AI drafts a first reply.

### Try It Yourself 9.2: One Factor at a Time 🛠️

**Predict:** A community theater's box office answers about 90 ticket emails a week, at about 4 minutes each. In a pilot of 20 AI drafts, 15 went out with light edits at about 1.5 minutes each, 4 were rewritten, and 1 promised a refund the theater does not offer. One box office account costs \$20 a month. Predict which of the five factors will decide whether the theater should adopt.

**Run:** Send the tutoring center prompt with the theater's facts in place of the tutoring center's. Check every number in the response against the facts, and mark each one Holds, Contradicted, or Not in source. Then fill `use-evaluation-sheet.md` from this chapter's data pack for the theater, with your own Missing lines.

**Explain:** Was your prediction right? In 1-2 sentences, explain why the one refund promise matters more or less than the minutes saved.

### Quick Check 9.2 ✅

1. An apartment management office answers about 200 maintenance requests a week, at about 5 minutes each. In a pilot, 40 of 50 AI drafts needed only a light edit, at about 2 minutes. Calculate the weekly minutes the light-edit drafts would save, show each step, and name one number the estimate is missing.
2. Two AI uses at the same office each made 1 error in 50 drafts. One misspelled a tenant's street. The other promised a same-day repair the crew cannot make. Rank their error costs and justify the ranking in two sentences.
3. A manager says a pilot proves the tool is "95 percent accurate" after 20 drafts. Critique the claim using the definition of a pilot, and rewrite it in counts.

---

## 9.3 Trends and How to Judge a Claim

AI claims arrive every day: in sales emails, news stories, vendor slides, and posts from people who sound sure. Some are true, some are true about something else, and some have no source at all. You do not need to be an economist to sort them. You need five questions and the habit of opening the primary source.

### The Five Claim Questions

Run these on any claim about AI's effect on work, business, or society:

1. **Who says it,** and what do they gain if you believe it?
2. **What was measured:** firms, workers, tasks, or someone's forecast?
3. **When and where** was it measured?
4. **Can you open the primary source,** and does it say what the claim says?
5. **Does it fit your case:** your size, your work, your people?

Then give the claim one verdict from the Accuracy Audit in Chapter 7: Holds, Contradicted, Not in source, or Unverifiable.

### One Question, Five Answers

How many businesses use AI? Ask a chat assistant first:

```text
What percentage of U.S. businesses use AI? Give one number and its source in two sentences.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
About 18% of U.S. businesses report using AI in producing goods or services, according to the U.S. Census Bureau's Business Trends and Outlook Survey (BTOS), though the figure has been rising quickly and my knowledge may lag the latest release. Check census.gov/hfp/btos for the current reading.
```

The number and the description come from two different questions. In November 2025 the Census Bureau changed its question from AI use "in producing goods or services" to use "in any business function." A Federal Reserve note puts adoption at about 18 percent of firms at the end of 2025, which is the share under the new question. Under the older wording, the note's figures put the rate near 10 percent. As worded, the claim is Contradicted. With the question corrected, the number holds. The tool flagged that it might lag, which is the knowledge cutoff from Chapter 2 doing its job, but the flag did not catch the mix-up.

Now look at the other numbers you will see for the same question, each read on October 21, 2026:

| Number | Who published it | What it counted | When |
| --- | --- | --- | --- |
| 17 to 20 percent | U.S. Census Bureau story, May 26, 2026 | U.S. firms using AI in any business function, from a survey of firms of every size | December 2025 to May 2026 |
| 58 percent | U.S. Chamber of Commerce, August 18, 2025 | Small businesses that say they use generative AI | 2025 survey |
| 88 percent | Stanford HAI, 2026 AI Index (April 2026), citing McKinsey & Company's State of AI survey | Respondents to a global consulting firm's annual executive survey who say their organization uses AI in at least one business function | 2025 survey |
| 41 percent | Federal Reserve note, April 3, 2026, citing the Real-Time Population Survey | Workers who use generative AI for work | November 2025 |
| 78 percent | Same Federal Reserve note, citing the Survey of Business Uncertainty | Share of the labor force at firms that have adopted AI | November 2025 |

All five can be true at once, because they count different things. The Federal Reserve note says the biggest driver of the gap is "differences in sampling distributions and units of analysis." Most U.S. firms are small, and small firms use AI less. A survey of all firms gives a low number, while a survey weighted toward large employers gives a high one. The note concludes that the Census survey is the best estimate of the share of businesses, and the 78 percent is an upper bound on access. So what about "88 percent of organizations use AI"? The summary line does not say whom it counts, but the report's economy chapter does: executives answering a consulting firm's survey, results the report calls "self-reported" and says to read as "directional," not comprehensive. The verdict: Holds for survey respondents, does not fit a 30-person company like Copperwind.

### Trends to Watch

Three trends come up in almost every AI sales pitch. Each callout below is dated so a later edition can refresh it without touching the lesson.

An **agent** is an AI system that takes actions toward a goal instead of only writing text for a person to use. It might open a ticket, click through a website, or run another tool. Here is what a chat assistant said about agents at a help desk:

```text
Are AI agents ready to run a small IT company's help desk on their own? Answer in three sentences.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Not entirely: AI agents can reliably handle routine Tier-1 work like password resets, account unlocks, software how-tos, ticket triage, and knowledge-base lookups, but they still make confident mistakes and can be fooled by social engineering, which is risky when they hold admin permissions. Tasks involving hardware faults, network outages, security incidents, or ambiguous and unusual problems still need a human who can verify, take accountability, and exercise judgment. The best setup for a small company today is an AI-first help desk with clear permission limits, audit logs, and an easy escalation path to a human technician rather than fully autonomous operation.
```

Run the five questions. Who says it? A model, with nothing to sell but also nothing to stand on. What was measured? Nothing: "reliably" has no count behind it. Is there a primary source? None was given. The verdict is Unverifiable, however sensible it sounds. Notice that the response still recommends a setup, which is a judgment it cannot back.

!!! note "Trend check (verified October 2026)"
    Stanford HAI's 2026 AI Index reports that agents rose from 12 percent to about 66 percent task success on one benchmark of computer tasks. It adds that they "still fail roughly 1 in 3 attempts on structured benchmarks." A benchmark is someone else's test, not your pilot. Building and running agents is the work of CIS144, the next course in the certificate.

Chapter 1 defined multimodal tools, the ones that handle images and text together.

!!! note "Trend check (verified October 2026)"
    Stanford HAI's 2026 AI Index (April 2026) reports that several frontier models now meet or exceed human baselines on multimodal reasoning on published tests. The same report says the top model "reads analog clocks correctly just 50.1% of the time." A tool that reads a chart well may still misread a photo of a gauge, so test the image work you need.

**On-device AI** is a model that runs on the phone or laptop itself instead of on a vendor's servers, so a request can be answered without the data leaving the device. Smaller models make it possible, and they change the privacy question from Chapter 8: what stays on the device, and what still goes to a server?

!!! note "Trend check (verified October 2026)"
    One device maker's July 2025 technical report ([arXiv 2507.13575](https://arxiv.org/abs/2507.13575)) describes a 3-billion-parameter model that runs on its devices. A larger model runs on the maker's servers. Read the data policy to learn which requests go where.

### Try It Yourself 9.3: Five Questions for One Claim 🛠️

**Predict:** Find one claim about AI and work published this month, in a news story, an ad, or a post. Copy it word for word with its link and date. Predict the verdict it will earn: Holds, Contradicted, Not in source, or Unverifiable.

**Run:** Answer the five claim questions in writing. Find and open the primary source the claim rests on, and quote the sentence that supports or fails to support it. Record the claim, the five answers, and your verdict in `evidence-log-template.md`.

**Explain:** Did the verdict match your prediction? In 1-2 sentences, explain which of the five questions did the most work.

### Fix It 9.1: A Number for the Memo 🔧

A help desk supervisor at a regional company is writing a memo to her manager and wants one statistic to anchor it.

**Symptom:** She asked for a sentence she could paste:

```text
I am writing a memo to my manager about AI and jobs. Give me one statistic on how many jobs AI will eliminate in the next five years, in one sentence I can paste in.
```

Here is the response it gave (captured from a chat assistant, October 2026):

```text
The World Economic Forum's *Future of Jobs Report 2025* projects that by 2030, about 92 million jobs worldwide will be displaced by automation and technological change, though it also expects 170 million new roles to be created, for a net gain of 78 million.

Since this covers roughly the next five years, it fits your timeframe. Including the net figure will help your manager see the full picture rather than just the displacement number.
```

A real report, a real publisher, three specific numbers, and no doubt anywhere.

**Diagnose:** Before you touch the prompt, open the report (January 2025) and find the sentence the 92 million comes from. Name in one sentence what that number counts, and compare it with what her memo would say it counts.

**Repair:** The three numbers hold. The cause does not. The report builds its figures from "the predictions shared by Future of Jobs Survey respondents," more than 1,000 employers, and the 92 million is churn from "structural labour-market transformation." Its key findings list five drivers: technological change, geoeconomic fragmentation, economic uncertainty, demographic shifts, and the green transition. So the 92 million is a forecast of change from all causes, not a count of jobs AI will eliminate. The same report does carry an AI line. In its section on technological change, it says trends in AI and information processing "are expected to create 11 million jobs, while simultaneously displacing 9 million others." That is what employers expect for 2025 to 2030, worldwide, before subtracting one from the other. The model skipped that line and reached for the headline. The repair adds one sentence that asks for a source that measured AI's effect, with what she needs to open it, and for the model's doubt. The sentence makes one requirement (a source the reader can open, plus its limits), so any change in the answer is credited to that sentence as a whole. That is the one change:

```text
I am writing a memo to my manager about AI and jobs. Give me one statistic on how many jobs AI will eliminate in the next five years, in one sentence I can paste in. Use only a statistic whose source measured or forecast AI's effect specifically, name its publisher, title, and date so I can open it, and say what the number does not measure and how sure you are of it.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
**Heads-up:** I don't know of a credible source that forecasts how many jobs AI will *eliminate* over the next five years. The closest AI-specific figure is an exposure estimate, so the sentence below is worded to avoid overclaiming.

**Paste-ready sentence:**
"Goldman Sachs Global Investment Research estimated in 2023 that generative AI could expose the equivalent of 300 million full-time jobs worldwide to automation (Briggs and Kodnani, *The Potentially Large Effects of Artificial Intelligence on Economic Growth*, March 26, 2023)."

**What the number does not measure:**
- **Not jobs eliminated.** "Exposed" means some of the tasks could be automated. Many of those jobs would be changed or augmented rather than lost.
[...]
If your manager needs a number that actually says "eliminated," I'd recommend saying that no reliable AI-specific forecast exists and presenting this as an exposure estimate. Sources that give net job-loss figures, like the World Economic Forum's *Future of Jobs Report 2025* (January 2025), cover all causes of change, not AI alone, so they don't meet your AI-specific requirement.
```

**Verify:** The answer makes two claims about sources, so run two checks. First, open the source it named. The firm's report page shows that title, with Briggs and Kodnani named in it, and a date of 26 March 2023. The firm's own article says the shifts "could expose the equivalent of 300 million full-time jobs to automation." Title, authors, date, and figure hold. Second, check the answer's last sentence against the report you opened in the Diagnose. It says that report covers "all causes of change, not AI alone." The report's AI line (9 million displaced, 11 million created) says otherwise, so that sentence is Contradicted. Its opening line, that it knows no credible forecast, misses the same line. The repair made the model careful about sources, and it still misread one it named. Asking for sources never replaces opening them. Her memo can say "exposed" with the Goldman Sachs source. With the WEF source, it can say employers expect AI and information processing to displace about 9 million jobs and create about 11 million worldwide by 2030. It cannot say AI will eliminate 92 million jobs.

### Quick Check 9.3 ✅

1. A slide says "Nine in ten organizations now use AI." Apply the five claim questions to it, and write the one sentence you would add before the slide goes to a 30-person company.
2. A vendor's sales email says its AI "resolves 80 percent of tickets." Write the two claim questions you would ask first, and say what answer would earn the verdict Unverifiable.

---

## 9.4 Society and the Memo

A use that pays off for one business still lands in a wider world. Five areas come up whenever people argue about AI's effect on society. Each figure below was read in its primary source on October 21, 2026. Each one also measures something narrower than the headline people attach to it.

**Misinformation** is false or misleading information that spreads, whether or not the person sharing it means to deceive. Generative AI makes convincing text and images cheap to produce at volume, the strength from Section 9.1 pointed the wrong way.

| Area | One figure | Source and date | What it measured |
| --- | --- | --- | --- |
| Jobs | Employment of workers aged 22 to 25 in AI-exposed occupations stands 19 percent below where it would be had it kept pace with less-exposed peers. The same paper finds "no evidence of widespread, economy-wide job displacement." | Brynjolfsson, Chandar, and Chen, Stanford Digital Economy Lab, revised August 12, 2026 | Payroll records for millions of U.S. workers, through June 2026 |
| Education | 26 percent of U.S. teens say they use one named chat assistant for schoolwork, up from 13 percent in 2023 | [Pew Research Center](https://www.pewresearch.org/short-reads/2025/01/15/about-a-quarter-of-us-teens-have-used-chatgpt-for-schoolwork-double-the-share-in-2023/), January 15, 2025 | 1,391 teens aged 13 to 17, surveyed in fall 2024 |
| Misinformation | Concern about fake news rose 4 points, to 62 percent on average across markets | [Reuters Institute Digital News Report 2026](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/dnr-executive-summary), June 16, 2026 | People's stated concern about what is real online, from 97,520 people in 48 markets. Not how much misinformation exists, and not AI-made content |
| Access | 37 percent of U.S. firms with at least 250 employees use AI, against less than 20 percent of firms with four or fewer | U.S. Census Bureau story, May 26, 2026 | A survey of U.S. firms, December 2025 to May 2026 |
| Energy | Data centers used about 415 terawatt-hours in 2024, around 1.5 percent of the world's electricity, projected to reach about 945 by 2030 | International Energy Agency, *Energy and AI*, April 10, 2025 | All data centers, with AI named as the main driver of growth |

Read the jobs row closely, because it bears on Copperwind's hiring. The decline among young workers comes "primarily through reduced hiring," and it is concentrated where AI use substitutes for people's tasks. Where AI use complements workers, the authors find employment "flat or rising." That pattern fits augmentation, though the authors call their findings early, descriptive indicators, not proof of cause. A Deskside plan that keeps technicians in charge of every reply is the complementing kind.

Here is the energy question asked of a chat assistant, and checked against the source:

```text
How much electricity does AI use worldwide? Give one number and its source in two sentences.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Data centers, which host AI along with other computing, used about 415 terawatt-hours of electricity worldwide in 2024, roughly 1.5% of global electricity demand, according to the International Energy Agency's 2025 "Energy and AI" report. AI's exact share of that total isn't precisely measured, though the IEA projects data center demand could reach about 945 TWh by 2030, with AI a major driver.
```

Every number holds against the report: 415 terawatt-hours, about 1.5 percent, and about 945 by 2030. The response also answered a slightly different question and said so. You asked about AI, and the source counts data centers. A careful memo keeps that distinction.

### Try It Yourself 9.4: Check One Figure Yourself 🛠️

**Predict:** Pick one row of the society table. Predict one thing the figure cannot tell a 30-person IT company deciding whether to adopt AI.

**Run:** Open the row's source, find the sentence the figure comes from, and copy it word for word with the date you read it. Add the source to `evidence-log-template.md`: what it measured, what it found, and how it applies to Copperwind.

**Explain:** Was your prediction right? In 1-2 sentences, explain how the gap between what the source measured and the headline would change a sentence in a memo.

### The Memo

A Use Evaluation is your working sheet. **The Memo** is what a manager reads. Its shape is fixed so a busy reader always knows where to look:

* **To, From, Date, Subject** lines.
* **The recommendation in the first sentence:** adopt, extend the pilot, or decline.
* **One paragraph per factor,** in the Use Evaluation's order, each with its number and its source.
* **What we do not know:** the numbers the pilot did not collect and the claims you could not check.
* **The next step:** one action, with who does it.

The recommendation goes first because a manager may read only the first sentence. Every number names its source, because a manager who doubts one number will doubt them all. "What we do not know" is not a weakness. It tells the manager what a longer pilot would buy.

### Try It Yourself 9.5: The Memo, Problem-First 🛠️

**Predict:** You will use the tutoring center facts from Section 9.2. Predict which part of the Memo a chat assistant is most likely to get wrong: the first sentence, the sources, the error cost, or the word limit.

**Run:** Get a chat assistant to draft the tutoring center's memo to the center's owner. Write your own prompt. A good result meets these criteria:

* The first sentence recommends adopt, extend the pilot, or decline.
* Each of the five factors gets its own paragraph, with its number and its source.
* Every number traces to the tutoring center facts, with none added.
* It has a "What we do not know" paragraph and one next step.
* It stays under 300 words.

Paste your prompt and the response into your prompt log, and score each criterion pass or fail with a quote or a count.

**Explain:** Compare your run with the sample below. In 1-2 sentences, explain which criterion your prompt handled better or worse, and why.

Here is one reasonable prompt for the task. Send the prompt without the [Step] lines:

```text
[Step 1: name the writer, the reader, and the decision]
Write a memo from me, the manager of a tutoring center, to the center's owner on whether to adopt an AI tool that drafts the session summaries we send parents.
[Step 2: set the Memo's shape, recommendation first]
Use this shape: To, From, Date, and Subject lines; the recommendation (adopt, extend the pilot, or decline) in the first sentence; one short paragraph per factor (cost, time saved, error cost, risk, workforce impact), each with its number and where the number came from; a "What we do not know" paragraph; and one next step.
[Step 3: hand over the evidence with its source]
Evidence, all from our two-week pilot log unless marked: 4 tutors; about 120 summaries a week; 8 minutes to write one by hand; 30 summaries drafted in the pilot; 22 sent with light edits at about 3 minutes each; 6 rewritten; 2 caught naming a skill the student never practiced; $25 per tutor per month (vendor quote). Nobody's hours will be cut.
[Step 4: set the limits]
Use only these numbers, and keep it under 300 words. Leave the date as "Date: (today)".
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
**To:** Center Owner
**From:** [Your name], Manager
**Date:** (today)
**Subject:** Whether to adopt an AI tool for parent session summaries

**Recommendation:** Extend the pilot rather than adopt now. The time savings are real, but 2 of 30 drafts contained an error that needs a firm review rule before we scale.

**Cost:** The vendor quote is $25 per tutor per month. For our 4 tutors, that is $100 per month (vendor quote).

**Time saved:** Writing a summary by hand takes about 8 minutes. In the pilot, 22 of 30 drafts went out with light edits at about 3 minutes each, saving roughly 5 minutes apiece (pilot log). At about 120 summaries a week, if that 22-in-30 rate holds, that is roughly 88 summaries and about 7 hours saved weekly. This is my projection, not a measured result.

**Error cost:** 2 of 30 drafts (about 7%) named a skill the student never practiced. Tutors caught both. A wrong skill in a parent summary undermines trust in our reporting (pilot log).
[...]
**Next step:** Extend the pilot another two weeks with all 4 tutors. Require a tutor review of each draft, and log edit time, rewrite time, and errors. I will bring you the results for a final decision.
```

The first sentence recommends, and the time-saved projection is labeled as a projection. Four things miss. The full memo runs 325 words by a word counter, header lines included, against a 300-word limit. The Risk and Workforce impact paragraphs (cut above) name no source. A few lines add what the facts never gave: "Tutors caught both," a "[Your name]" blank, and, in the cut Risk paragraph, a review rule for "the tutor who ran the session." Error cost gives a rate again, as the Use Evaluation did, so the manager still has to write what one error costs. The draft saves time, and the manager still edits before it reaches the owner.

### Quick Check 9.4 ✅

1. A memo opens: "Over the past two weeks, our team explored many exciting possibilities with AI." Rewrite the first sentence so it does the Memo's job, using a recommendation of your choice.
2. You are writing a memo about whether to hire a junior technician or adopt an AI drafting tool. Choose the society figure from this section that bears most on the decision, and state one thing it cannot tell you.

These skills point ahead. CIS144 builds agents and runs AI-driven analytics, and CIS218 integrates and deploys AI in applications. This course stops at deciding whether a use is worth it and saying why.

---

## 9.5 Summary and Retrieval 💡

### Key Concepts

* AI is strong at pattern work at volume: sorting, routine drafts, summaries of supplied text, and translation. It is weak at judgment that needs facts it was not given, fresh facts, long chains of reasoning, and accountability. Published studies show the line between the two is jagged, so you test each use on your own work.
* The Use Evaluation scores a proposed use on five factors in order: cost, time saved, error cost, risk, and workforce impact. Error cost is what one mistake costs, not how often mistakes happen.
* A pilot is a small, measured trial on your own work, reported in counts and minutes. It feeds the Use Evaluation. A benchmark tests someone else's tasks and cannot replace it.
* Real cases are evidence with dates. A support study found the biggest gains for newer agents. A tribunal held an airline responsible for what its chatbot told a customer.
* The five claim questions ask who says it, what was measured, when and where, whether the primary source says it, and whether it fits your case. A claim then gets an Accuracy Audit verdict.
* A real report can still be the wrong source for a sentence. Check what a number counts before you paste it.
* The Memo puts the recommendation in its first sentence, gives one paragraph per factor with its number and source, says what we do not know, and names one next step.

### Key Terms

See course glossary for full definitions

* Use Evaluation, error cost, workforce impact, augmentation, pilot (Section 9.2)
* agent, on-device AI (Section 9.3)
* misinformation (Section 9.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Name the five factors of the Use Evaluation in order, and say which one is about what a single mistake costs.
2. State the difference between a pilot and a benchmark, and name the two units a pilot reports in.
3. List the five claim questions, and say which one the Fix It's statistic failed.
4. From Chapter 7: Name the four steps of the Accuracy Audit in order, and the four verdicts a checked claim can receive.
5. From Chapter 5: Name the five checks of the Output Checklist in order, and the three answers each check can receive.

---

## 9.6 Skills Lab 9A: The Deskside First-Reply Memo

**Goal:** Deliver the Memo to Copperwind's owner and Mei Lin on whether Deskside should adopt an AI assistant for first replies. Build it from the pilot's numbers, the technicians' notes, a Use Evaluation, and outside evidence you checked.

**Starter files:** Provided files in `assets/code/chapter-09/` from the course data pack: `skills-lab-9a-worksheet.md` (your answer file), `deskside-pilot-numbers.txt` (Mei Lin's report on the two-week pilot), `technician-notes.txt` (five anonymous notes from Deskside technicians), `use-evaluation-sheet.md`, `evidence-log-template.md`, and `memo-template.md`. Download the data pack from Canvas, extract it, and work at the extracted `cis137` root. Open each file in any text editor and never retype its contents. The lab files are fictional, so you may paste them into a chat assistant once your privacy plan allows it. You first met Copperwind in Chapter 1, and this lab gives you everything it needs, so you do not need any earlier file.

### Part 1: Foundation (Aligns with Objective 9.1)

Work in `skills-lab-9a-worksheet.md`, which has a space for every task below. Read `deskside-pilot-numbers.txt` and `technician-notes.txt` in full before you write anything.

1. Before you send any prompt, write your privacy plan in two columns: what from the lab files may go into a tool, and what stays out of every prompt. Give the reason for each item that stays out.
2. Break a Deskside first reply into four steps: read the ticket, decide which team owns it, draft the reply, and send it under Deskside's name. Mark each step strong or weak for AI, and support each mark with one piece of evidence from Section 9.1 or from `deskside-pilot-numbers.txt`.
3. Find two outside sources on AI in support work or AI's effect on jobs, at least one of them a primary source. Fill one row of `evidence-log-template.md` for each, with the date you read it. Then run the five claim questions on one claim from either source and give it a verdict: Holds, Contradicted, Not in source, or Unverifiable.

### Part 2: Application (Aligns with Objectives 9.1 and 9.2)

1. Fill `use-evaluation-sheet.md` for the Deskside pilot. For each of the five factors, give the number, its source, what is missing, and a rating (Favors adoption, Mixed, or Against). Show the time-saved estimate step by step in minutes, and keep the pilot's results in counts, never percentages.
2. Use a chat assistant to check your Use Evaluation. Write your own prompt. A good response uses only the pilot's numbers, flags every assumption, and adds no number of its own. Paste the prompt and the response. Then run the Accuracy Audit on the response against `deskside-pilot-numbers.txt`: list each claim, give each a verdict, and report the counts.
3. State your recommendation (adopt, extend the pilot, or decline), the factor that decided it, and the one result from a longer pilot that would change it.

### Part 3: Extension (Aligns with Objectives 9.2 and 9.3)

1. Write the Memo to the owner and Mei Lin in `memo-template.md`, under 400 words. Put the recommendation in the first sentence and give one paragraph per factor with its number and source. In the workforce impact paragraph, say what changes for the technicians, drawing on `technician-notes.txt`. In the risk paragraph, name what the AI Use Policy must cover before adoption, by section name. End with what we do not know and one next step.
2. In the Memo's "What we do not know" paragraph or a paragraph of its own, judge one current claim about AI and work from your evidence log. Quote the claim, name its primary source and date, give your verdict, and say in one sentence how it bears on the recommendation.

### Questions & Analysis 🤔

Answer both questions in the worksheet's final section. These answers carry significant rubric weight.

1. Quote the rating and the number from your `use-evaluation-sheet.md` that decided your recommendation, and the prompt log entry behind it. Using `deskside-pilot-numbers.txt`, explain why that factor outweighed the others, and name the result in an extended pilot that would flip your recommendation.
2. Quote the counts and the worst finding from your Part 2 Task 2 audit. Explain whether the chat assistant's check changed any number in your Memo, and what your audit says about using an AI tool to check an evaluation of an AI tool.

**Submission:** Submit your completed worksheet as one file named `skills-lab-9a-lastname.md`. Keep every answer under its task heading, with your filled Use Evaluation sheet, evidence log, and Memo pasted into their sections. Include every prompt you sent, the tool and date, and every response you received, pasted exactly, with your Questions & Analysis answers clearly labeled at the end.

### Rubric: Skills Lab 9A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria, five
levels from Mastery to Not Evident. The criteria are Technical
Accuracy and Efficiency, Output Quality, Documentation Quality, and
Analysis, Interpretation, and Response to QUESTION(s). The criteria
and levels are the same everywhere. Your instructor sets the point
values in your course. Check the syllabus and the Canvas rubric
attached to this lab for the values that apply to you.

---

## 9.7 Review Questions 🔄️

1. **Understand:** Explain to a coworker, in no more than three sentences, why a model's high score on a public benchmark does not tell your team whether to adopt it.

2. **Apply:** A hotel front desk wants AI to draft replies to booking emails. It handles about 150 a week at about 5 minutes each. Write the five factor headings of a Use Evaluation for this use, and under each one name the number the hotel's pilot must collect.

3. **Analyze:** A regional bus agency's press release says its AI trip planner "answers 9 out of 10 rider questions correctly." The release gives no sample size, no date range, and no definition of correct. Analyze the claim with the five claim questions, and say which verdict it earns and what would move it.

4. **Evaluate:** A county recorder's office wants an AI chatbot on its website to answer residents' questions about filing deadlines, with no staff review. Its pilot found 2 wrong deadlines in 100 answers. Decide whether the office should adopt, extend the pilot, or decline. Defend your decision with the error cost factor and the tribunal case in Section 9.2, and name the one change that would most change your answer.

---

## Further Reading 📖

* [Generative AI at Work (Brynjolfsson, Li, and Raymond, NBER Working Paper 31161)](https://www.nber.org/papers/w31161): The customer support study in Sections 9.1 and 9.2, issued April 2023 and revised November 2023. It was later published in *The Quarterly Journal of Economics*. Read the abstract for the 14 percent and 34 percent findings.
* [Moffatt v. Air Canada, 2024 BCCRT 149 (Civil Resolution Tribunal of British Columbia)](https://decisions.civilresolutionbc.ca/crt/crtd/en/item/525448/index.do): The full decision of February 14, 2024. Paragraphs 27 and 28 hold the ruling on who answers for a chatbot.
* [Monitoring AI Adoption in the US Economy (Federal Reserve, FEDS Notes)](https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html): Jeffrey S. Allen's note of April 3, 2026, which explains why three surveys give 18, 41, and 78 percent for AI adoption.
* [Large Firms With at Least 20 Employees Biggest AI Users (U.S. Census Bureau)](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html): The Census Bureau's May 26, 2026 story on business AI use by firm size. It also explains the November 2025 change to the survey question.
* [Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence (Stanford Digital Economy Lab)](https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/): The payroll study behind the jobs row in Section 9.4, revised August 12, 2026.
* [Energy and AI (International Energy Agency)](https://www.iea.org/reports/energy-and-ai): The IEA's report of April 10, 2025 on data center electricity use, with the 2024 figure and the 2030 projection.

---

## Looking Ahead ⏩

You can now judge where AI fits, score a use from a pilot, check a claim against its source, and put the answer in a memo a manager can act on. Part IV turns from whether to use AI to which tool to use. Chapter 10 surveys and compares AI platforms with stated criteria, and the Use Evaluation comes with you.
