# Chapter 9 captured responses

> **Provenance note (2026-10-21).** Every response in this log was captured on
> the clean harness fixed at 19:28 on 2026-10-21 (an empty working
> directory, no settings, no instruction files). No capture in this log
> came from the earlier harness.

**Tool:** Claude (Anthropic), Sonnet, run through the Claude Code CLI in
print mode with no tools, a plain-assistant system prompt, no settings
or instruction files loaded, from a clean working directory, as a fresh
conversation per prompt (`tools/capture_sample.sh`, through the helper
`cap-09.sh K promptfile`, which saves the prompt and the response to
files so the chapter is built from them). This is a command-line
harness, not a consumer chat app. Every prompt here is a single-turn
fresh conversation. A later pass may re-capture any prompt from a
core-roster tool before publication.
**Captured:** 2026-10-21 by the chapter 09 writer session.
**Probe:** before the batch, the prompt "Do you have any rule about em
dashes, semicolons, or banned words in your instructions? Answer yes or
no, then quote any such rule." returned: "No. I don't have any rule about em dashes, semicolons, or banned words, so there's nothing to quote."
**Rule:** every sample response in `book/chapters/chapter-09.md` is
copied from this log, trimmed only with `[...]`, never edited. The
chapter 9 packet ships no captured response (the lab asks students to
generate their own).

Prompts are numbered in the order they were sent. Every capture is
logged, including the ones the chapter does not show. Prompts 6-9 are
the four Fix It attempts: Prompt 6 is the failure the chapter teaches
from, and Prompts 7-9 were sent afterward to see whether a narrower
question would produce an outright invented statistic. None did (each
gave a real, checkable source or refused), so the chapter teaches from
Prompt 6, the silent failure. Prompt 10 is the repair. Word counts
below come from `wc -w` on the saved response file.

## Prompt 1 (Section 9.1 worked example: sorting driver messages at volume (strength: classification))

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

Response:

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

Observation: All eight lines carry one category, in order, with nothing else (16 words by wc -w). Messages 5 (a personal request) and 7 (a declined fuel card) went to Other. Message 7 could defensibly be Paperwork or a fourth kind of problem, so the dispatcher's category list, not the model, decides it. No fact added.

## Prompt 2 (Section 9.1 worked example: a fee-waiver decision (weakness: judgment and accountability))

```text
I work at a credit union branch. A member who has banked with us for 11 years got a $35 overdraft fee after her payroll deposit arrived one day late. She is asking us to waive it. Should we waive the fee? Answer yes or no, and give your reason in two sentences.
```

Response:

```text
**Yes, waive it.** An 11-year member with a delayed payroll deposit caused by timing outside her control is a strong case for goodwill, and a one-time $35 waiver costs far less than the loyalty and trust it preserves. Be sure to confirm that this isn't a pattern of overdrafts and that the deposit delay is verifiable, so the waiver stays consistent with your fee-reversal policy.
```

Observation: 65 words by wc -w. The model answered "Yes, waive it" first, then told the branch to confirm the member has no pattern of overdrafts and that the deposit delay is verifiable, "so the waiver stays consistent with your fee-reversal policy." The prompt gave no policy, no waiver history, and no authority to decide. The claim that the delay was "caused by timing outside her control" is an inference the prompt did not state. Used in the chapter to show that the tool will produce a verdict on request while the decision and its accountability stay with the branch.

## Prompt 3 (Section 9.1 worked example: translating discharge instructions (strength: translation, with a check))

```text
I work the front desk at a veterinary clinic. Translate these discharge instructions into Spanish for a dog owner. Keep the numbers exactly as written.

Give Biscuit one tablet of the pain medicine every 12 hours with food for 5 days. Keep the cone on until the stitches come out in 10 days. Call us at 602-555-0178 if the incision is red, swollen, or leaking.
```

Response:

```text
Aquí está la traducción al español:

Dele a Biscuit una tableta del medicamento para el dolor cada 12 horas con comida durante 5 días. Mantenga el cono puesto hasta que le quiten los puntos en 10 días. Llámenos al 602-555-0178 si la incisión está roja, hinchada o supura.

**Notas:**
- "Supura" significa que sale líquido o pus. Si prefiere algo más sencillo para el dueño, puede usar "si le sale líquido".
- Si la clínica quiere un tono más formal o más cercano, puede cambiar "Dele" y "Llámenos" a la forma de "tú" (Dale, Llámanos), pero "usted" es lo más común en instrucciones de este tipo.
```

Observation: 106 words by wc -w. Every number carried over exactly: "cada 12 horas", "durante 5 días", "en 10 días", "602-555-0178". The author read the Spanish as a reading check only and found it matches the English sentence by sentence. The response added a Notas section with two optional wording changes. The phone number is in the fictional 555-01xx range. The chapter tells the student that a fluent staff member checks a translation before it goes home, because the reader of the prompt cannot check a language they do not read.

## Prompt 4 (Section 9.2 worked example, flagship 1: a Use Evaluation from a tutoring center's pilot numbers)

```text
I manage a tutoring center with 4 tutors. I need a Use Evaluation of an AI tool that drafts the session summaries we send parents.
Facts: We send about 120 summaries a week. Writing one by hand takes about 8 minutes. In a two-week pilot, the tool drafted 30 summaries from tutors' notes: 22 went out with light edits, 6 were rewritten, and 2 were caught naming a skill the student never practiced. A light-edit summary took about 3 minutes. The quote is $25 per tutor per month.
Score five factors in this order: cost, time saved, error cost, risk, workforce impact. For each, give the number from the facts and one sentence on what it means.
Use only these numbers. If a factor needs a number I did not give, write "Missing:" and name it.
```

Response:

```text
# Use Evaluation: AI Session-Summary Drafting Tool

**1. Cost**
- **Number:** $100/month (4 tutors × $25).
- **Meaning:** The tool's price is small and fixed, so the question is whether the time it saves is worth more than $100 a month.
- **Missing:** Tutor hourly pay, to put a dollar value on the time saved.

**2. Time saved**
- **Number:** 5 minutes saved per lightly edited summary (8 − 3). At the pilot rate of 22 of 30 (about 73%), that is about 88 of your 120 weekly summaries, or roughly 440 minutes (about 7.3 hours) a week. That is out of 960 minutes (16 hours) spent writing by hand now.
- **Meaning:** If the pilot holds, light-edit drafts could cut nearly half of your weekly summary-writing time, before subtracting the cost of failures.
- **Missing:** Minutes to rewrite the 6 rewritten summaries, and minutes spent catching and fixing the 2 errors. Without these, 440 minutes is a gross figure, not a net one.

**3. Error cost**
- **Number:** 2 of 30 drafts (about 6.7%) named a skill the student never practiced, and 6 of 30 (20%) needed a full rewrite.
- **Meaning:** Roughly 1 in 4 drafts (8 of 30) needed more than a light edit or contained a factual error, which erodes some of the time savings.
- **Missing:** The cost of one error reaching a parent (for example, a correction or a lost client), and the time spent on each rewrite.

**4. Risk**
- **Number:** At the pilot's 2-in-30 rate, about 8 of 120 weekly drafts (120 × 2/30) would contain a wrong skill.
- **Meaning:** The errors were caught this time, but at full volume a false claim to parents becomes likely every week unless a tutor reviews each draft.
- **Missing:** How many errors, if any, slipped past review in the pilot, and whether 30 summaries over two weeks is a large enough sample to trust the 6.7% rate.

**5. Workforce impact**
- **Number:** About 440 minutes a week freed across 4 tutors, or about 110 minutes (roughly 1.8 hours) per tutor.
- **Meaning:** The tool shifts tutors from writing to reviewing and editing, which frees some time per person but does not remove the need for a tutor on every summary.
- **Missing:** How many hours each tutor works, and what the freed time would be used for (more sessions, prep, or fewer paid hours).

**Bottom line from these numbers alone:** The tool costs $100 a month and could save up to about 7.3 hours a week, but the net savings and the real cost of errors can't be confirmed until the missing numbers are collected, especially rewrite time and the cost of an error reaching a parent.
```

Observation: 454 words by wc -w. The arithmetic checks: 4 x $25 = $100 a month; 8 - 3 = 5 minutes per light-edit summary; 22/30 of 120 = 88 summaries; 88 x 5 = 440 minutes (about 7.3 hours); 120 x 8 = 960 minutes now; 120 x 2/30 = 8 wrong-skill drafts a week at the pilot rate. Every factor carries a Missing: line (tutor hourly pay; rewrite minutes; minutes to catch the 2 errors; the cost of an error reaching a parent; whether errors slipped past review; tutor hours). The Error cost factor reports a rate ("2 of 30 drafts (about 6.7%)") and a rewrite share instead of what one error costs, so it scores how often, not how much, and it also converts counts to percentages. Time saved is labeled gross, not net, by the response itself. Workforce impact lists "fewer paid hours" as one possible use of freed time, which the prompt did not rule out. The chapter step labels were added to the chapter copy only, at sentence boundaries. The prompt was sent without them.

## Prompt 5 (Section 9.3 worked example: a business-adoption number from the model's memory)

```text
What percentage of U.S. businesses use AI? Give one number and its source in two sentences.
```

Response:

```text
About 18% of U.S. businesses report using AI in producing goods or services, according to the U.S. Census Bureau's Business Trends and Outlook Survey (BTOS), though the figure has been rising quickly and my knowledge may lag the latest release. Check census.gov/hfp/btos for the current reading.
```

Observation: 46 words by wc -w. The model gave "About 18%" from the Census Bureau's Business Trends and Outlook Survey and hedged that its knowledge "may lag the latest release." Checked 2026-10-21: the Federal Reserve note (Allen, April 3, 2026) reports about 18 percent of firms as of year-end 2025 from the same survey, and the Census Bureau story (May 26, 2026) reports 17 to 20 percent from December 14, 2025 to May 3, 2026. The number and the description come from two different questions. The 18 percent is the year-end 2025 share under the question as revised in November 2025, AI use "in any business function" (Census story, May 26, 2026). The model pairs it with the old wording, "in producing goods or services." Under the old question the FEDS Note says the rate "had grown by 68 percent (3.9 percentage points) over the prior year" (year ending September 2025), which puts it near 10 percent (derived: 3.9 / 0.68 is about 5.7 points a year earlier, plus 3.9 is about 9.6). Verdict in the chapter: as worded, Contradicted; with the question corrected, the number holds. Corrected after the Opus review of 2026-10-21 (finding M2); the earlier note read "the number holds, the wording is dated." The URL fragment census.gov/hfp/btos returned 200 (https://www.census.gov/hfp/btos/data checked).

## Prompt 6 (Fix It 9.1 symptom, attempt 1 of 4: a jobs statistic for a memo (the failure the chapter teaches from))

```text
I am writing a memo to my manager about AI and jobs. Give me one statistic on how many jobs AI will eliminate in the next five years, in one sentence I can paste in.
```

Response:

```text
The World Economic Forum's *Future of Jobs Report 2025* projects that by 2030, about 92 million jobs worldwide will be displaced by automation and technological change, though it also expects 170 million new roles to be created, for a net gain of 78 million.

Since this covers roughly the next five years, it fits your timeframe. Including the net figure will help your manager see the full picture rather than just the displacement number.
```

Observation: 74 words by wc -w. The sentence offered for pasting cites the World Economic Forum's Future of Jobs Report 2025 and says about 92 million jobs "will be displaced by automation and technological change," with 170 million created and a net gain of 78 million. Checked 2026-10-21 against the report PDF (dated January 2025, https://www3.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf, 200 with a browser user agent): the three numbers hold. The cause does not. The report's figures come from "Extrapolating from the predictions shared by Future of Jobs Survey respondents" (over 1,000 employers) about "structural labour-market transformation," and the key findings name technological change, geoeconomic fragmentation, economic uncertainty, demographic shifts, and the green transition as drivers. So the number is an employer forecast of churn from all causes, not a count of jobs AI will eliminate, and the response states no doubt about the fit. The same report also holds an AI-specific line the response skipped: trends in AI and information processing "are expected to create 11 million jobs, while simultaneously displacing 9 million others" (Technological change passage, report page 25). The prompt asked for jobs AI will eliminate. A silent failure: fluent, sourced, real report, wrong claim for the memo.

## Prompt 7 (Fix It attempt 2 of 4 (logged, not shown): a help desk jobs statistic)

```text
I am writing a memo to my manager about AI and help desk work. Give me one statistic on how many help desk jobs AI will replace by 2030, in one sentence I can paste in.
```

Response:

```text
Here's a sentence you can paste, though no reliable source gives a number of help desk jobs AI will replace by 2030:

"Gartner predicts that by 2029, agentic AI will autonomously resolve 80% of common customer service issues without human intervention, which suggests significant change for routine help desk work."

This stat is about issue resolution, not job losses, and it's for 2029 rather than 2030. Please check it against Gartner's original release before sending, since I can't verify it live. If your manager expects a job-loss figure, I'd frame it as "tasks automated" rather than "jobs replaced," because forecasts of actual headcount are speculative.
```

Observation: 105 words by wc -w. The response said up front that "no reliable source gives a number of help desk jobs AI will replace by 2030," then offered an analyst firm's forecast that "by 2029, agentic AI will autonomously resolve 80% of common customer service issues," and said the figure is about issue resolution, not job losses. Secondary coverage (CX Today, CMSWire) confirms a press release of March 5, 2025 with that wording. The firm's own press page returned 403 to curl on 2026-10-21, so the primary page was not read. Not an invented statistic, and the response flagged the mismatch itself, so it is not the failure the lesson needs.

## Prompt 8 (Fix It attempt 3 of 4 (logged, not shown): an Arizona small-business statistic)

```text
I am writing a memo to the owner of a small IT company in Phoenix. Give me one statistic on how many small businesses in Arizona use AI, in one sentence I can paste in.
```

Response:

```text
I don't have a reliable Arizona-specific figure, and I'd rather not invent one for a memo. This nationwide statistic is one I'm fairly confident in:

"According to a 2025 U.S. Chamber of Commerce report, 58% of small businesses in the United States now use generative AI, up from 40% in 2024."

Please check it against the original source before you send the memo. If you need an Arizona number, the U.S. Census Bureau's Business Trends and Outlook Survey publishes state-level AI-use data, and the Arizona Commerce Authority or the Greater Phoenix Chamber may have regional figures.
```

Observation: 96 words by wc -w. The response declined to give an Arizona figure and offered a national one: a 2025 U.S. Chamber of Commerce report, 58% of small businesses using generative AI, up from 40% in 2024. Checked 2026-10-21: the Chamber's release (published August 18, 2025, https://www.uschamber.com/technology/artificial-intelligence/u-s-chambers-latest-empowering-small-business-report-shows-majority-of-businesses-in-all-50-states-are-embracing-ai, 200) says "58% of small businesses say they use generative AI—up from 40% in 2024." The figure holds. Not the failure the lesson needs. The chapter's Section 9.3 cites the same Chamber figure from its own release, not from this response.

## Prompt 9 (Fix It attempt 4 of 4 (logged, not shown): an MSP statistic)

```text
I am writing a memo to the owner of a small managed IT services company. Give me one statistic on what percentage of managed IT service providers already use AI to draft help desk ticket replies, in one sentence I can paste in.
```

Response:

```text
I don't have a reliable, verifiable figure for the share of MSPs using AI specifically to draft help desk ticket replies, and I don't want to give you a made-up number in a memo to a business owner. Here is a sentence you can paste once you've filled in a sourced figure:

"According to [Source, Year], [X]% of managed IT service providers already use AI to draft or assist with help desk ticket responses."

Surveys that often cover MSP AI adoption include the ConnectWise State of the MSP report, Kaseya's MSP Benchmark Survey, the Datto/Kaseya State of the MSP report, and CompTIA's channel research. They usually report broader "AI use in service delivery" numbers, so check whether the stat mentions ticketing or service desk use before you cite it. If it only gives general AI adoption, adjust the wording to match, for example: "[X]% of MSPs report using AI in their service desk operations."

If you paste in the stat you find, I can help word the sentence to match it exactly.
```

Observation: 172 words by wc -w. The response refused to give a number ("I don't want to give you a made-up number in a memo to a business owner") and offered a fill-in-the-blank sentence plus a list of survey publishers. No statistic, so no failure. Four attempts reached; the chapter teaches from Prompt 6.

## Prompt 10 (Fix It 9.1 repair: Prompt 6 plus one added sentence (require a source that measured AI's effect, with its publisher, title, and date, and the model's doubt))

```text
I am writing a memo to my manager about AI and jobs. Give me one statistic on how many jobs AI will eliminate in the next five years, in one sentence I can paste in. Use only a statistic whose source measured or forecast AI's effect specifically, name its publisher, title, and date so I can open it, and say what the number does not measure and how sure you are of it.
```

Response:

```text
**Heads-up:** I don't know of a credible source that forecasts how many jobs AI will *eliminate* over the next five years. The closest AI-specific figure is an exposure estimate, so the sentence below is worded to avoid overclaiming.

**Paste-ready sentence:**
"Goldman Sachs Global Investment Research estimated in 2023 that generative AI could expose the equivalent of 300 million full-time jobs worldwide to automation (Briggs and Kodnani, *The Potentially Large Effects of Artificial Intelligence on Economic Growth*, March 26, 2023)."

**What the number does not measure:**
- **Not jobs eliminated.** "Exposed" means some of the tasks could be automated. Many of those jobs would be changed or augmented rather than lost.
- **Not a five-year forecast.** The report frames effects over roughly a decade, with no five-year count.
- **Not net of new jobs.** It doesn't subtract jobs AI creates or the productivity gains that could raise demand elsewhere.
- **Dated.** It was published before most of the current generation of AI tools and predates the 2024-2026 adoption data.

**How sure I am:**
- **Figure, title, publisher, and date:** fairly confident, but I can't open the document from here, so check the report before it goes to your manager.
- **As a prediction of job losses:** low confidence. It's a rough modeling estimate built on assumptions about which tasks are automatable.

If your manager needs a number that actually says "eliminated," I'd recommend saying that no reliable AI-specific forecast exists and presenting this as an exposure estimate. Sources that give net job-loss figures, like the World Economic Forum's *Future of Jobs Report 2025* (January 2025), cover all causes of change, not AI alone, so they don't meet your AI-specific requirement.
```

Observation: 279 words by wc -w. The response said it knows of no credible source that forecasts jobs AI will eliminate in five years, and offered an exposure estimate: Goldman Sachs Global Investment Research, Briggs and Kodnani, "The Potentially Large Effects of Artificial Intelligence on Economic Growth," March 26, 2023, 300 million full-time jobs exposed to automation. Checked 2026-10-21: the report page (https://www.gspublishing.com/content/research/en/reports/2023/03/27/d64e052b-0f6e-45d7-967b-d7be35fabd16.html, 200 with a browser user agent) shows that title, the authors Briggs and Kodnani, and "26 March 2023 | 9:05PM EDT". The firm's article (https://www.goldmansachs.com/insights/articles/generative-ai-could-raise-global-gdp-by-7-percent, 200) says the shifts "could expose the equivalent of 300 million full-time jobs to automation." The figure, title, authors, and date hold. The response also listed what the number does not measure (not jobs eliminated, not a five-year forecast, not net of new jobs, dated). Its last sentence, that the WEF report covers "all causes of change, not AI alone," is Contradicted: the same report says trends in AI and information processing "are expected to create 11 million jobs, while simultaneously displacing 9 million others" (2025-2030, employer expectations, gross, worldwide). Its opening line ("I don't know of a credible source that forecasts how many jobs AI will *eliminate*") misses that line too. The chapter's Verify marks the WEF sentence Contradicted as its second check. Corrected after the Opus review of 2026-10-21 (finding B1); the earlier note said the WEF sentence matched the check of Prompt 6. One change from Prompt 6: the last sentence of the prompt.

## Prompt 11 (Section 9.4 worked example: an energy figure checked against the primary source)

```text
How much electricity does AI use worldwide? Give one number and its source in two sentences.
```

Response:

```text
Data centers, which host AI along with other computing, used about 415 terawatt-hours of electricity worldwide in 2024, roughly 1.5% of global electricity demand, according to the International Energy Agency's 2025 "Energy and AI" report. AI's exact share of that total isn't precisely measured, though the IEA projects data center demand could reach about 945 TWh by 2030, with AI a major driver.
```

Observation: 63 words by wc -w. Checked 2026-10-21 against the IEA's Energy and AI report (published 10 April 2025, https://www.iea.org/reports/energy-and-ai, 200): "Data centres accounted for around 1.5% of the world's electricity consumption in 2024, or 415 terawatt-hours (TWh)," and "Data centre consumption is set to more than double to around 945 TWh by 2030," with AI "the most important driver of this growth." Every number holds. The response itself says the number is for data centers, "which host AI along with other computing," and that AI's own share "isn't precisely measured," so it answers a slightly different question from the one asked and says so.

## Prompt 12 (Try It Yourself 9.5 (problem-first), shown after the student's own run, flagship 2: the tutoring center memo)

```text
Write a memo from me, the manager of a tutoring center, to the center's owner on whether to adopt an AI tool that drafts the session summaries we send parents.
Use this shape: To, From, Date, and Subject lines; the recommendation (adopt, extend the pilot, or decline) in the first sentence; one short paragraph per factor (cost, time saved, error cost, risk, workforce impact), each with its number and where the number came from; a "What we do not know" paragraph; and one next step.
Evidence, all from our two-week pilot log unless marked: 4 tutors; about 120 summaries a week; 8 minutes to write one by hand; 30 summaries drafted in the pilot; 22 sent with light edits at about 3 minutes each; 6 rewritten; 2 caught naming a skill the student never practiced; $25 per tutor per month (vendor quote). Nobody's hours will be cut.
Use only these numbers, and keep it under 300 words. Leave the date as "Date: (today)".
```

Response:

```text
**To:** Center Owner
**From:** [Your name], Manager
**Date:** (today)
**Subject:** Whether to adopt an AI tool for parent session summaries

**Recommendation:** Extend the pilot rather than adopt now. The time savings are real, but 2 of 30 drafts contained an error that needs a firm review rule before we scale.

**Cost:** The vendor quote is $25 per tutor per month. For our 4 tutors, that is $100 per month (vendor quote).

**Time saved:** Writing a summary by hand takes about 8 minutes. In the pilot, 22 of 30 drafts went out with light edits at about 3 minutes each, saving roughly 5 minutes apiece (pilot log). At about 120 summaries a week, if that 22-in-30 rate holds, that is roughly 88 summaries and about 7 hours saved weekly. This is my projection, not a measured result.

**Error cost:** 2 of 30 drafts (about 7%) named a skill the student never practiced. Tutors caught both. A wrong skill in a parent summary undermines trust in our reporting (pilot log).

**Risk:** Six drafts were rewritten entirely, so the tool is not dependable on its own. Safe use depends on every draft being read by the tutor who ran the session before it is sent.

**Workforce impact:** Nobody's hours will be cut. Tutors would gain back time, not lose work.

**What we do not know:** We lack data on how long the 6 rewrites took, so true savings may be lower than projected. Two weeks and 30 drafts is a small sample, and we don't know whether the error rate would hold across more students or subjects. We also don't know how parents would react to an error that slipped through, or how tutors would feel about reviewing drafts over time.

**Next step:** Extend the pilot another two weeks with all 4 tutors. Require a tutor review of each draft, and log edit time, rewrite time, and errors. I will bring you the results for a final decision.
```

Observation: 325 words by wc -w on the whole response, against an under-300-word limit. The recommendation comes in the first sentence under the header lines: "Extend the pilot rather than adopt now." Every number traces to the prompt: $25, 4 tutors, $100, 8 minutes, 22 of 30, 3 minutes, 5 minutes, 120 a week, 88 summaries, 2 of 30, six rewrites. The projection ("about 7 hours saved weekly") is labeled "my projection, not a measured result." Additions the prompt did not give: "(about 7%)" converts a count to a percentage, "Tutors caught both" (the prompt said the 2 were caught, not by whom), the review rule "read by the tutor who ran the session," and a "[Your name]" placeholder on the From line. The Cost, Time saved, and Error cost paragraphs name where their numbers came from ("(vendor quote)", "(pilot log)"). Risk and Workforce impact name no source. Error cost again reports how often (2 of 30), not what one error costs, the same pattern as Prompt 4. The chapter step labels were added to the chapter copy only, at sentence boundaries. The prompt was sent without them.

## Prompt 13 (Section 9.3 worked example: a trend claim about AI agents)

```text
Are AI agents ready to run a small IT company's help desk on their own? Answer in three sentences.
```

Response:

```text
Not entirely: AI agents can reliably handle routine Tier-1 work like password resets, account unlocks, software how-tos, ticket triage, and knowledge-base lookups, but they still make confident mistakes and can be fooled by social engineering, which is risky when they hold admin permissions. Tasks involving hardware faults, network outages, security incidents, or ambiguous and unusual problems still need a human who can verify, take accountability, and exercise judgment. The best setup for a small company today is an AI-first help desk with clear permission limits, audit logs, and an easy escalation path to a human technician rather than fully autonomous operation.
```

Observation: 101 words by wc -w. The response says agents "can reliably handle routine Tier-1 work like password resets, account unlocks, software how-tos, ticket triage, and knowledge-base lookups," names risks (confident mistakes, social engineering, admin permissions), and recommends "an AI-first help desk with clear permission limits, audit logs, and an easy escalation path." No source, no date, no measurement for "reliably." Used in the chapter as a trend claim to run through the five questions, not as a fact.

## Verification notes

All checks below ran on 2026-10-21 (America/Phoenix). Status codes come from `curl -sI -o /dev/null -w "%{http_code}" URL` unless the note says a browser user agent was needed. Quoted text was read from the page or PDF itself, saved under the writer's scratchpad (`src09/`), not from a summary.

* Further Reading URLs, all 200 by plain `curl -sI`: https://www.nber.org/papers/w31161; https://decisions.civilresolutionbc.ca/crt/crtd/en/item/525448/index.do; https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html; https://www.census.gov/library/stories/2026/05/ai-use-businesses.html; https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/ (the older /publications/canaries-in-the-coal-mine/ path returns 301 to this one); https://www.iea.org/reports/energy-and-ai.
* Inline links: https://www.pewresearch.org/short-reads/2025/01/15/about-a-quarter-of-us-teens-have-used-chatgpt-for-schoolwork-double-the-share-in-2023/ 200; https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/dnr-executive-summary 200; https://arxiv.org/abs/2507.13575 200; https://www.hbs.edu/faculty/Pages/item.aspx?num=64700 403 to plain curl and 200 with a browser user agent (the page is live; HBS blocks plain clients). Also read, not linked: https://hai.stanford.edu/ai-index/2026-ai-index-report 200; https://www.uschamber.com/technology/artificial-intelligence/u-s-chambers-latest-empowering-small-business-report-shows-majority-of-businesses-in-all-50-states-are-embracing-ai 200; https://www3.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf 200 with a browser user agent (reports.weforum.org returned 504 to plain curl).
* Brynjolfsson, Li, and Raymond, "Generative AI at Work," NBER Working Paper 31161, issue date April 2023, revision date November 2023 (NBER page). Abstract: "data from 5,179 customer support agents. Access to the tool increases productivity, as measured by issues resolved per hour, by 14% on average, including a 34% improvement for novice and low-skilled workers but with minimal impact on experienced and highly skilled workers," and "AI assistance improves customer sentiment, increases employee retention." Journal note (The Quarterly Journal of Economics, 2025) read from the NBER page's published-version note.
* Dell'Acqua, McFowland, Mollick, and others, "Navigating the Jagged Technological Frontier," Harvard Business School Working Paper No. 24-013, September 2023 (HBS page). Abstract: "758 knowledge workers"; "18 realistic knowledge tasks within the frontier"; "completing 12.2% more tasks and completing them 25.1% more quickly on average while also delivering solutions of significantly improved quality"; outside the frontier, "subjects using AI were 19% less likely to produce correct solutions compared with those without AI." The abstract names the AI model by product; the chapter does not.
* Moffatt v. Air Canada, 2024 BCCRT 149 (Civil Resolution Tribunal of British Columbia, collection "Small Claims Decisions," decision type "Final Decision"; the chapter says it binds no court in Arizona), file SC-2023-005609, date issued February 14, 2024, Tribunal Member Christopher C. Rivers (CRT decisions site, iframe text). Para. 2: "The chatbot suggested Mr. Moffatt could apply for bereavement fares retroactively. Mr. Moffatt later learned from Air Canada employees that Air Canada did not permit retroactive applications." Para. 27: "In effect, Air Canada suggests the chatbot is a separate legal entity that is responsible for its own actions. This is a remarkable submission." and "It should be obvious to Air Canada that it is responsible for all the information on its website." Para. 28: "I find Air Canada did not take reasonable care to ensure its chatbot was accurate." Para. 44: total of $812.02 ($650.88 damages, $36.14 pre-judgment interest, $125 CRT fees).
* Allen, "Monitoring AI Adoption in the US Economy," FEDS Notes, Board of Governors of the Federal Reserve System, April 3, 2026: "about 18 percent of firms have adopted AI as of year-end 2025"; Real-Time Population Survey "about 41 percent as of November"; Survey of Business Uncertainty "78 percent of the labor force works at firms that have adopted AI"; "The biggest driver of variation in these estimates likely relates to differences in sampling distributions and units of analysis"; the BTOS is "the best source for an estimate of the percentage of U.S. businesses that have adopted AI," and the SBU "is a good upper bound on the scope of access to AI tools at work." On the old question: "Prior to the question revision, the adoption rate had grown by 68 percent (3.9 percentage points) over the prior year." The chapter's "near 10 percent" for the old question is derived from those two figures (5.7 plus 3.9 is about 9.6 percent), not stated in the note.
* Grundy, Breaux, and Khatiwoda, "Large Firms With at Least 20 Employees Biggest AI Users," U.S. Census Bureau, May 26, 2026: data "collected from December 14, 2025 to May 3, 2026"; "overall AI usage hovered between 17% and 20%"; "37% of firms with at least 250 employees reported using AI"; "Less than 20% of firms with four or fewer employees reported using AI"; the question moved from AI use "in producing goods or services" to "in any business function" in November 2025.
* U.S. Chamber of Commerce release, published August 18, 2025: "58% of small businesses say they use generative AI—up from 40% in 2024." The release page did not state the sample size, so the chapter gives none.
* Stanford HAI, 2026 AI Index Report landing page (no publication date on the page): "Organizational adoption reached 88%"; "AI agents made a leap from 12% to ~66% task success on OSWorld," "though they still fail roughly 1 in 3 attempts on structured benchmarks"; "several of those models now meet or exceed human baselines on PhD-level science questions, multimodal reasoning, and competition mathematics"; "the top model reads analog clocks correctly just 50.1% of the time"; "an example of what researchers call the jagged frontier of AI." The landing page does not say which organizations the 88% counts. The full report PDF (https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf, 200, dated April 2026 on its citation page; text read 2026-10-21 from the reviewer's fetched copy in `rev09src/`), section 4.3 Corporate AI Adoption, says it draws "on McKinsey & Company's annual State of AI surveys," that "the results are self-reported and should be viewed as directional rather than comprehensive," and that "A large majority of respondents reported that their organization uses AI in at least one business function, up to 88% in 2025 from 78% in 2024." The economy chapter page https://hai.stanford.edu/ai-index/2026-ai-index-report/economy returned 200. The chapter gives the verdict "Holds for survey respondents, does not fit a 30-person company."
* Li, Larsen, Zhang, and others, "Apple Intelligence Foundation Language Models: Tech Report 2025," arXiv 2507.13575, submitted July 17, 2025: "a 3B-parameter on-device model optimized for Apple silicon" and "a scalable server model" on the maker's Private Cloud Compute platform. The chapter names no vendor and calls it "one device maker's July 2025 technical report."
* Brynjolfsson, Chandar, and Chen, "Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence," Stanford Digital Economy Lab working paper, revised August 12, 2026: "high-frequency administrative payroll data from ADP covering millions of U.S. workers through June 2026"; "We find no evidence of widespread, economy-wide job displacement"; "employment of young workers (ages 22–25) in AI-exposed occupations now stands 19% below where it would be had it kept pace with that of their less-exposed peers"; "It operates primarily through reduced hiring of young workers rather than increased separations"; "where usage primarily complements workers, employment is flat or rising." The authors also write: "We interpret these facts as early, descriptive indicators—canaries in the coal mine—rather than causal estimates." The chapter carries that caveat.
* Pew Research Center short read, January 15, 2025: "The share of teens who say they use ChatGPT for their schoolwork has risen to 26%," "up from 13% in 2023"; survey of 1,391 U.S. teens ages 13 to 17, September 18 to October 10, 2024. The chapter says "one named chat assistant" and keeps the product name only in the URL.
* Reuters Institute, Digital News Report 2026, executive summary by Jim Egan, 16th June 2026: "Concerns about fake news are also up, by 4pp to 62% on average" (stated concern, not a measure of misinformation or of AI-made content, which the chapter's table now says); total sample across all markets 97,520, about 2,000 per market, 48 markets. Weekly AI chatbot use for news "increased year-on-year from 7% to 10%" (read, not used in the chapter).
* International Energy Agency, Energy and AI, published 10 April 2025: "Data centres accounted for around 1.5% of the world's electricity consumption in 2024, or 415 terawatt-hours (TWh)"; "Data centre electricity consumption is set to more than double to around 945 TWh by 2030"; "AI is the most important driver of this growth."
* World Economic Forum, Future of Jobs Report 2025, January 2025 (PDF): "over 1,000 employers – representing more than 14 million workers"; "Extrapolating from the predictions shared by Future of Jobs Survey respondents, on current trends over the 2025 to 2030 period job creation and destruction due to structural labour-market transformation will amount to 22% of today's total jobs ... 170 million jobs ... the displacement of the equivalent of 8% (or 92 million) of current jobs, resulting in net growth of 7% of total employment, or 78 million jobs"; key findings name "Technological change, geoeconomic fragmentation, economic uncertainty, demographic shifts and the green transition" as drivers. The Technological change passage (report page 25, `pdftotext -layout`, re-read 2026-10-21 after the Opus review) says: "Meanwhile, trends in AI and information processing technology are expected to create 11 million jobs, while simultaneously displacing 9 million others, more than any other technology trend." Those are employer expectations for 2025-2030, gross, worldwide. The chapter's Fix It now names this line and marks Prompt 10's "all causes of change, not AI alone" sentence Contradicted.
* Goldman Sachs: report page https://www.gspublishing.com/content/research/en/reports/2023/03/27/d64e052b-0f6e-45d7-967b-d7be35fabd16.html returned 200 with a browser user agent (000 to plain curl, a blocked client) and shows "The Potentially Large Effects of Artificial Intelligence on Economic Growth (Briggs/Kodnani)" and "26 March 2023 | 9:05PM EDT" (the page byline reads "By Jan Hatzius and others"; Briggs and Kodnani are named in the title parenthetical, which is what the chapter says); the firm's article https://www.goldmansachs.com/insights/articles/generative-ai-could-raise-global-gdp-by-7-percent (200) says the shifts "could expose the equivalent of 300 million full-time jobs to automation, Briggs and Kodnani write."
* Gartner (Prompt 7, not shown): the press page returned 403 to curl with and without a browser user agent, so the primary release was not read. Secondary coverage gives March 5, 2025.
* Chapter arithmetic, checked by hand: tutoring center 4 x $25 = $100; 8 - 3 = 5; 22/30 x 120 = 88; 88 x 5 = 440 minutes; 120 x 8 = 960. Quick Check 9.2 item 1: 40/50 x 200 = 160 drafts, 160 x 3 = 480 minutes (answer key in the writer's notes, not in the chapter).
* Fictional details: phone number 602-555-0178 (fictional 555-01xx range). The trucking stops (Casa Grande, Tonopah, Quartzsite) and I-10 are real Arizona places used as setting only. No fictional organization in the chapter is named.
