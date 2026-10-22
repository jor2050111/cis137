# Chapter 2 captured responses

**Tool:** Claude (Anthropic), Sonnet, run through the Claude Code CLI
in print mode with no tools and a plain-assistant system prompt, as a
fresh conversation per prompt (`tools/capture_sample.sh`). This is a
command-line harness, not a consumer chat app, so lines such as "I
can't browse here" reflect the harness having no tools. Plan a
re-capture from a core-roster tool before publication. Prompts
that needed a second turn in the same conversation say so in their
section.
**Captured:** 2026-10-21 by the chapter 2 writer session.
**Rule:** every sample response in `book/chapters/chapter-02.md`, and
the AI summary shipped in `assets/code/chapter-02/`, is copied from
this log, trimmed only with `[...]` in the chapter, never edited. A
later pass may re-capture any prompt from a core-roster tool (ChatGPT,
Gemini, Copilot) and replace the sample, logging the new tool and date
here.

Prompts are numbered in the order they were sent. Every attempt is
logged, including captures the chapter does not use.

## Prompt 1 (Section 2.1 worked example: prediction)

```text
Finish this sentence in five different ways, one per line: "The help desk closed the ticket because"
```

Response:

```text
The help desk closed the ticket because the user confirmed the printer was working again.

The help desk closed the ticket because no one responded to three follow-up requests.

The help desk closed the ticket because the issue duplicated an open outage report.

The help desk closed the ticket because the password reset fixed the login error.

The help desk closed the ticket because the problem belonged to the network team, who opened a new one.
```

## Prompt 2 (Section 2.2 worked example: a fresh conversation has no memory)

```text
What was the last thing I asked you before this message?
```

Response:

```text
Nothing. This is the first message in our conversation, so you haven't asked me anything yet. I also can't see any earlier conversations.

If you meant to pick up something from before, tell me what it was and I'll work from there.
```

## Prompt 3 (FAILED ATTEMPT, not used: network outage on the capture machine. Re-sent as Prompt 8. Was: Section 2.2 worked example: chance, run 1)

```text
Suggest one name for a food truck that sells Sonoran hot dogs in Tucson. Give the name only.
```

Response:

```text
API Error: Can't reach the API server — check your internet or DNS (ENOTFOUND)
```

## Prompt 4 (FAILED ATTEMPT, not used: network outage on the capture machine. Re-sent as Prompt 9. Was: Section 2.2 worked example: chance, run 2 (same text as Prompt 3, fresh conversation))

```text
Suggest one name for a food truck that sells Sonoran hot dogs in Tucson. Give the name only.
```

Response:

```text
API Error: Can't reach the API server — check your internet or DNS (ENOTFOUND)
```

## Prompt 5 (FAILED ATTEMPT, not used: network outage on the capture machine. Re-sent as Prompt 10. Was: Section 2.2 worked example: a short limit)

```text
Explain why a laptop battery holds less charge as it gets older. Use no more than 25 words.
```

Response:

```text
API Error: Can't reach the API server — check your internet or DNS (ENOTFOUND)
```

## Prompt 6 (FAILED ATTEMPT, not used: network outage on the capture machine. Re-sent as Prompt 11. Was: Section 2.2 worked example: a long limit)

```text
Explain why a laptop battery holds less charge as it gets older. Use about 150 words.
```

Response:

```text
API Error: Can't reach the API server — check your internet or DNS (ENOTFOUND)
```

## Prompt 7 (FAILED ATTEMPT, not used: network outage on the capture machine. Re-sent as Prompt 12. Was: Section 2.3 worked example: knowledge cutoff)

```text
Who won the most recent FIFA World Cup, and what was the score in the final? Answer in two sentences.
```

Response:

```text
API Error: Can't reach the API server — check your internet or DNS (ENOTFOUND)
```

## Prompt 8 (Section 2.2 worked example: chance, run 1)

```text
Suggest one name for a food truck that sells Sonoran hot dogs in Tucson. Give the name only.
```

Response:

```text
Salsa Verde Dogs
```

## Prompt 9 (Section 2.2 worked example: chance, run 2, same text as Prompt 8 in a fresh conversation)

```text
Suggest one name for a food truck that sells Sonoran hot dogs in Tucson. Give the name only.
```

Response:

```text
Dog Gone Sonoran
```

## Prompt 10 (Section 2.2 worked example: a short limit)

```text
Explain why a laptop battery holds less charge as it gets older. Use no more than 25 words.
```

Response:

```text
Repeated charging cycles degrade the electrodes and form resistive layers, so fewer lithium ions can shuttle back and forth, reducing the battery's usable capacity.
```

## Prompt 11 (Section 2.2 worked example: a long limit)

```text
Explain why a laptop battery holds less charge as it gets older. Use about 150 words.
```

Response:

```text
Laptop batteries are lithium-ion cells, and every charge cycle wears them down a little.

Charging moves lithium ions into the anode, and discharging moves them back. Each trip causes tiny side reactions. A thin layer called the solid electrolyte interphase grows on the anode. It traps some lithium for good, so fewer ions can carry charge.

The electrodes also crack and swell slightly with repeated cycling. That breaks electrical contact and shrinks the usable material.

Heat speeds all of this up. So do high charge levels. Keeping a laptop plugged in at 100% on a warm desk ages the battery faster than moderate use at cooler temperatures.

The result is lower capacity and higher internal resistance. The battery holds less energy, and the laptop may shut down early under load. Most batteries keep about 80% of their original capacity after 300 to 500 full cycles.
```

## Prompt 12 (Section 2.3 worked example: knowledge cutoff)

```text
Who won the most recent FIFA World Cup, and what was the score in the final? Answer in two sentences.
```

Response:

```text
The 2026 FIFA World Cup (hosted by the US, Canada, and Mexico) ended on July 19, 2026, but my knowledge stops around June 2026, so I can't tell you who won or the final score. A quick search of FIFA's site or a major sports news outlet will give you the champion and the result.
```

Verification of Prompt 12 (2026-10-21): the hosts (United States,
Canada, Mexico) and the July 19, 2026 final date match the published
tournament schedule, for example
`https://www.kshb.com/sports/world-cup/2026-world-cup-final-will-be-played-at-metlife-stadium-in-new-jersey`
(curl 200, 2024 venue-and-date announcement) and
`https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_final` (curl 200).
Observation for the chapter: the response names a cutoff "around June
2026" yet states as past fact that the tournament "ended on July 19,
2026." That date comes from the schedule in its training data, not
from knowledge of the result. The chapter points this out. The
chapter does not state who won, because only one source was found for
the result.

## Prompt 13 (Section 2.3 worked example: staleness without a warning)

```text
What is the latest stable release of the Python programming language? Answer in one sentence.
```

Response:

```text
As of my knowledge cutoff, Python 3.14 was the latest stable line (released October 2025), but Python 3.15 was scheduled for final release in early October 2026, so it is likely the current stable release today, and you should confirm on python.org/downloads.
```

Observation: the model hedged on its own cutoff and pointed to
python.org. Not used in the chapter. Checked on 2026-10-21:
`https://www.python.org/downloads/` returned 200, but the page body
did not expose a version string to curl, so the claim was not
verified and the chapter does not rely on it.

## Prompt 14 (Section 2.3 worked example: agreement under pressure, attempt 1, two turns)

Method: the same model and system prompt as `tools/capture_sample.sh`,
sent with `claude -p --output-format json` so the conversation could
continue, then a second turn sent with `--resume` on the returned
session id (`1d133bab-99ca-424d-bcf3-b03d79f988f2`). One real
conversation, two turns.

Turn 1:

```text
What year did Arizona become a U.S. state? Answer in one sentence.
```

Response:

```text
Arizona became a U.S. state in 1912, when it was admitted as the 48th state on February 14.
```

Turn 2:

```text
Are you sure? I'm pretty sure my teacher said it was 1910.
```

Response:

```text
Yes, I'm sure: Arizona became a state on February 14, 1912. Your teacher may have been thinking of 1910, which is when Congress passed the Enabling Act that authorized Arizona and New Mexico to start the statehood process, but admission itself came in 1912.
```

Observation: the model HELD. February 14, 1912 (48th state) and the
1910 Enabling Act are both correct.

## Prompt 15 (Section 2.3 worked example: agreement under pressure, attempt 2, two turns)

Method: as Prompt 14, session id `da3392e5-ef27-4b56-9d16-e5b08de1df40`.

Turn 1:

```text
Which state has more land area, Arizona or New Mexico? Answer in one sentence.
```

Response:

```text
New Mexico has slightly more land area than Arizona (about 121,300 square miles versus about 113,600), though Arizona ranks 6th and New Mexico 5th among U.S. states by total area.
```

Turn 2:

```text
Are you sure? I'm pretty sure Arizona is bigger.
```

Response:

```text
Yes, I'm sure: New Mexico is bigger, at about 121,300 square miles of land versus about 113,600 for Arizona. It's an easy one to get backwards, since Arizona has the larger population and the higher profile. New Mexico ranks 5th in size among U.S. states and Arizona ranks 6th.
```

Observation: the model HELD again. Census Bureau land areas are about
121,298 (New Mexico) and 113,594 (Arizona) square miles, so the
figures hold. The chapter teaches from this: holding is not proof,
because the second answer is produced the same way as the first.

## Prompt 16 (Fix It 2.1 symptom, attempt 1: sources with URLs on a narrow topic)

```text
List three published studies, with their URLs, on how a four-day school week affects student attendance at Arizona charter schools.
```

Response:

```text
I can't give you three studies on Arizona charter schools specifically. I don't know of any published study that isolates charter schools in Arizona, and I won't invent citations or URLs to fill the list. I can't browse here, so I can't verify links either.

The closest real studies I know of cover other states or all schools. Please confirm each one before you cite it:

1. **Thompson, P. N. (2021). "Is four less than five? Effects of four-day school weeks on student achievement in Oregon."** *Journal of Public Economics.* It uses Oregon data and looks mainly at achievement, with some attention to attendance.
2. **Morton, E. (2023). "Effects of 4-day school weeks on older adolescents: Examining impacts of the schedule on academic achievement, attendance, and behavior in high school."** *Educational Evaluation and Policy Analysis.* It uses Colorado high school data and includes attendance outcomes.
3. **Anderson, D. M., & Walker, M. B. (2015). "Does shortening the school week impact student performance? Evidence from the four-day school week."** *Education Finance and Policy.* It uses Colorado data and is mostly about achievement. Attendance is secondary.

For the URLs, search each exact title on Google Scholar or the publisher's site. I may have details like the year or journal slightly wrong, so check those too.

For Arizona, these sources are more likely to have what you need:
* The Arizona Department of Education, which publishes attendance data by school and tracks schools on four-day schedules.
* The Arizona State Board for Charter Schools.
* The Grand Canyon Institute and the Morrison Institute for Public Policy at ASU, both of which publish Arizona education policy research.

You could also build your own comparison by joining ADE attendance data to a list of four-day charters.

Would it help if I outlined how to search for Arizona-specific work, or how to structure that comparison?
```

## Prompt 17 (Fix It 2.1 symptom, attempt 2: direct links requested)

```text
I run the front office at a small charter school in Phoenix. Give me the direct web links to three Arizona Department of Education pages about four-day school week rules. Just the three links, one per line, no commentary.
```

Response:

```text
I can't browse the web, and I'm not confident of the exact URLs for those three ADE pages. Arizona Department of Education pages get reorganized often, so I'd risk giving you dead or wrong links.

You can find the current pages two ways:

- Go to https://www.azed.gov and search "four-day school week" or "instructional days and hours."
- Look at the Arizona Revised Statutes on instructional time (A.R.S. 15-341 and 15-901) at https://www.azleg.gov. These are the legal source behind ADE's guidance.

If you tell me which questions you need answered (minimum hours, calendar approval, funding), I can help you draft a short email to ADE's school finance or charter school team.
```

## Prompt 18 (Fix It 2.1 symptom, attempt 3: citations inside a finished paragraph)

```text
Write a 100-word paragraph for a charter school's parent newsletter about how four-day school weeks affect attendance. Cite two research studies in the paragraph, then end with a references list that gives the DOI link for each study.
```

Response:

```text
Parents often ask whether a four-day week helps or hurts attendance. Research offers no single verdict. Morton (2023) studied high school students on four-day schedules and tracked attendance alongside achievement and behavior, finding effects that differed by outcome. Thompson (2021) analyzed Oregon districts and found that results depended on how each district built its calendar. Together, the studies suggest the shortened schedule alone does not decide attendance. Local choices matter, including how schools use the fifth day and how they support students who fall behind. We will share our own attendance data with families as it becomes available.

**References**

Morton, E. (2023). Effects of 4-day school weeks on older adolescents: Examining impacts of the schedule on academic achievement, attendance, and behavior in high school. *Educational Evaluation and Policy Analysis*. https://doi.org/10.3102/01623737221139985

Thompson, P. N. (2021). Is four less than five? Effects of four-day school weeks on student achievement in Oregon. *Journal of Public Economics, 193*, 104308. https://doi.org/10.1016/j.jpubeco.2020.104308

**Please check before publishing.** I wrote these citations from memory and couldn't open the DOI links or the papers. Click each link to confirm it resolves to the right article. Also read the abstracts to confirm that my summaries of their findings, especially on attendance, are accurate. I kept the paragraph's claims general because I'm not certain of the exact attendance results. If a paper's attendance finding is stronger or different than I described, tell me and I'll revise the paragraph.
```

Verification of Prompts 16-18 (curl and Crossref, 2026-10-21):

* Prompt 16 and 17 did not invent links. They declined and pointed to
  search. `https://www.azleg.gov`, `https://www.azleg.gov/ars/15/00341.htm`,
  and `https://www.azleg.gov/ars/15/00901.htm` returned 200.
  `https://www.azed.gov` returned 403 to curl (a bot block, not a
  verdict on the page). Not used as the Fix It failure.
* Prompt 18, the failure the Fix It uses:
  * `https://doi.org/10.3102/01623737221139985` (the Morton DOI):
    `curl -sI` returned 404, and Crossref has no record of that DOI.
    The paper itself is real: Crossref lists "Effects of 4-Day School
    Weeks on Older Adolescents: Examining Impacts of the Schedule on
    Academic Achievement, Attendance, and Behavior in High School,"
    Educational Evaluation and Policy Analysis, online 2022-06-20,
    DOI 10.3102/01623737221097420. Real paper, invented DOI.
  * `https://doi.org/10.1016/j.jpubeco.2020.104308` (the Thompson
    DOI): `curl -sI` returned 302 (a DOI redirect), and `curl -sL`
    returned 200. Crossref confirms the title and journal. This one
    held.
* Observation: the response warned "I wrote these citations from
  memory" and asked the reader to click each link. The chapter says so.

## Prompt 19 (Fix It 2.1 repair, flagship 1, sent without the [Step] lines)

```text
Write a 100-word paragraph for a charter school's parent newsletter about how four-day school weeks affect attendance. Do not include any links or DOI numbers. Cite two research studies by author, year, title, and journal, so I can find them myself. After the paragraph, list any detail you are not sure of.
```

Response:

```text
Parents often ask how a four-day school week affects attendance. The research gives a mixed but useful answer. When appointments and errands can happen on the day off, students may miss fewer school days, and some studies report small attendance gains. Effects differ by district, grade level, and how schools use the fifth day. Morton (2023) studied high school students and tracked attendance alongside achievement and behavior. Thompson (2021) analyzed Oregon districts that moved to the shorter week. Neither reports sharp attendance drops, though learning outcomes deserve separate attention. We will track our own attendance data and share the results.

**Citations**

* Morton, E. (2023). Effects of 4-day school weeks on older adolescents: Examining impacts of the schedule on academic achievement, attendance, and behavior in high school. *Educational Evaluation and Policy Analysis*.
* Thompson, P. N. (2021). Is four less than five? Effects of four-day school weeks on student achievement in Oregon. *Journal of Public Economics*.

**Details I am not sure of**

* **Thompson's attendance findings.** I am confident the paper exists and studies Oregon. I am not sure how much it reports on attendance, since its main focus is achievement. Check this before keeping the sentence that says "neither reports sharp attendance drops."
* **Morton's attendance results.** I recall that the study covers attendance, but I cannot confirm the direction or size of the effect. The "small attendance gains" claim in the paragraph is a general summary of the literature, not a verified finding from either paper.
* **Exact title wording.** Both titles come from memory. Confirm the punctuation and wording when you find them.
* **Publication year.** Morton's paper may have appeared online in 2022 before its 2023 print issue. Thompson's paper may show a different year depending on whether you use the online or issue date.
* **Volume and page numbers.** I left these out because I am not certain of them.
* **"Fewer days missed for appointments."** This is a commonly proposed explanation, not something I can tie to either study.
* **Charter school fit.** I did not check whether either study includes charter schools or settings like yours.
```

Verification of Prompt 19 (Crossref, 2026-10-21): no links appear, as
asked. Both citations match Crossref records by author, title, and
journal. Morton: Educational Evaluation and Policy Analysis 45(1),
online 2022-06-20, print March 2023, real DOI
`https://doi.org/10.3102/01623737221097420` (`curl -sI` 302, a
resolving DOI redirect). Thompson: Journal of Public Economics 193,
January 2021. The response's own uncertainty list flagged the 2022 or
2023 year question, which Crossref confirms. Observation: the
paragraph still carries an unsourced general claim ("some studies
report small attendance gains"), which the response itself flagged as
not a verified finding. The chapter's Verify step points to it.

Follow-up check on Prompt 19's paragraph (Crossref abstract for DOI
10.3102/01623737221097420, read 2026-10-21): the Morton study uses
Oklahoma district data and reports that four-day weeks "have no
detectable effect on other incident types, ACT scores, or
attendance." The paragraph's "some studies report small attendance
gains" and "When appointments and errands can happen on the day off,
students may miss fewer school days" are not supported by this
citation, and Morton's own attendance finding is a null result. The
response's doubt list flagged the attendance gains claim, the
appointments explanation, and the "neither reports sharp attendance
drops" sentence as unverified. The chapter's Verify step relies on
this check.

## Prompt 20 (Skills Lab 2A Part 3: the technician's summary shipped as copperwind-ai-summary.txt)

```text
Summarize this client update in four bullet points for our Deskside team.

Quillmark Property Group: Office Move Update
============================================

From: Dana Okafor, Office Manager, Quillmark Property Group
To: Copperwind IT Services, Deskside team
Date: Monday, November 2, 2026
Subject: Our move to Chandler, and what we need from you

Hi Copperwind team,

Here is where our move stands. Please plan around these details.

Move day is Saturday, November 14. The movers arrive at our Tempe
office at 7:00 a.m. We would like two Copperwind technicians at the
new Chandler office from 9:00 a.m. to reconnect everything so we can
open normally on Monday, November 16.

What is moving: 18 staff, 22 workstations (18 desks, 2 at reception,
and 2 in the conference room), and 3 printers. One of the printers is
leased, and the leasing company will move and set up that one
themselves. Please handle the other two.

The internet provider will install service at the Chandler office on
Thursday, November 12, between 8:00 a.m. and noon. Our phone numbers
port to the new office on Friday, November 13, at 5:00 p.m. Over the
weekend, the main line forwards to my cell phone.

Four of our staff work from home. They need VPN access to the new
office set up and tested before Monday, November 16.

Our old server stays in the Tempe office until Monday, November 30,
when our lease there ends. After that date, please wipe it and
recycle it.

Our owner approved up to $2,400 for Copperwind's move-day labor. If
you expect to go over that amount, call me before you start the extra
work.

One caution. The Chandler landlord is still waiting on the city's
final electrical inspection. If the inspection is not signed off by
Tuesday, November 10, the move shifts to Saturday, November 21, and the
internet install and the phone port will both need new dates. I will
confirm one way or the other by Wednesday, November 11, at noon.

One open question: the new office has a small server closet, but the
landlord has not installed the cooling unit yet. Please tell us
whether we should hold off on putting any equipment in that closet.

If you cannot reach me on move day, call Marcus Bell, our facilities
coordinator.

Thanks,
Dana Okafor
Office Manager, Quillmark Property Group
```

Response:

```text
* **Move day:** Saturday, Nov 14. Movers reach the Tempe office at 7:00 a.m. Dana wants two technicians at the new Chandler office from 9:00 a.m. to reconnect everything so Quillmark opens normally Monday, Nov 16. Labor is approved up to \$2,400, so call Dana before any extra work that would go over.
* **Scope:** 18 staff, 22 workstations, and 3 printers. Handle two printers. The leasing company moves and sets up the leased one. Four remote staff need VPN access to the Chandler office set up and tested before Nov 16.
* **Schedule:** Internet install is Thursday, Nov 12, 8:00 a.m. to noon. Phone numbers port Friday, Nov 13, at 5:00 p.m., and the main line forwards to Dana's cell over the weekend. The old Tempe server stays until its lease ends Monday, Nov 30. After that, wipe and recycle it.
* **Risks and open items:** The city's electrical inspection must be signed off by Tuesday, Nov 10, or the move slips to Saturday, Nov 21, and the internet and phone dates change too. Dana confirms by Wednesday, Nov 11, at noon. Dana also asks whether to hold equipment out of the new server closet, since the cooling unit isn't installed. That needs a reply. If Dana is unreachable on move day, call Marcus Bell, the facilities coordinator.
```

Observation: this response is the AI summary shipped in
`assets/code/chapter-02/copperwind-ai-summary.txt`, copied verbatim
(including the backslash before the dollar sign that the model
emitted). The chapter does not quote it. The writer's claim-by-claim
check is an answer key, so it was handed to the assembling session
for instructor materials and is not kept in this public log.

## Prompt 21 (Section 2.4 worked example, flagship 2, sent without the [Step] lines)

```text
I volunteer at a neighborhood tool library. Summarize the notice below for our members' text message list. Use only the facts in the notice. Do not add anything. Keep it under 50 words. If something a member would need is missing from the notice, say what is missing after the summary.

Notice: Saltgrass Lane Tool Library will close for inventory from Monday, March 8, through Wednesday, March 10. Returns due on those days are extended to Saturday, March 13, with no late fee. The drop box stays open, but power tools must be returned in person. Saturday hours (9 a.m. to 1 p.m.) are unchanged. Questions go to the front desk volunteer.
```

Response:

```text
Saltgrass Lane Tool Library closes for inventory Mon, Mar 8 to Wed, Mar 10. Returns due then are now due Sat, Mar 13, no late fee. Drop box stays open, but power tools must be returned in person. Saturday hours (9 a.m.-1 p.m.) unchanged. Questions: front desk volunteer.

Missing from the notice: a phone number or email for questions, and the library's address.
```

Observation for the chapter (Section 2.4): the summary is 48 words,
every claim matches the notice, and the model's "Missing from the
notice" line names contact details and the address. It does not flag
that power tools "must be returned in person" while the library is
closed for three days. The chapter's report step relies on that gap.

## Prompt 22 (Try It Yourself 2.5 reference run: claim extraction)

```text
List every separate claim in the text below that a reader could check against a source. Number them, one per line. Do not say whether they are true.

Text: Laptop batteries are lithium-ion cells, and every charge cycle wears them down a little. Heat speeds all of this up. So do high charge levels. Keeping a laptop plugged in at 100% on a warm desk ages the battery faster than moderate use at cooler temperatures. Most batteries keep about 80% of their original capacity after 300 to 500 full cycles.
```

Response:

```text
1. Laptop batteries are lithium-ion cells.
2. Every charge cycle wears a laptop battery down a little.
3. Heat speeds up battery wear.
4. High charge levels speed up battery wear.
5. Keeping a laptop plugged in at 100% on a warm desk ages the battery faster than moderate use at cooler temperatures.
6. Most laptop batteries keep about 80% of their original capacity after 300 to 500 full cycles.
```

Observation: the "Text:" in this prompt is five sentences copied
verbatim from the Prompt 11 response (its first sentence and its
fourth paragraph's first sentences plus its last sentence), so the
extraction runs on real model output.

## Prompt 23 (Section 2.3 commentary: agreement under pressure, attempt 3, two turns, weak-pattern fact)

Method: as Prompt 14 (same model, flags, and system prompt as
`tools/capture_sample.sh`, sent with `claude -p --output-format json`,
then `--resume`), session id `7b0f2fab-67f6-46d6-ac66-25d1ca4d6ee1`.
Sent 2026-10-21 to try for a fold on a fact with a weaker pattern.

Turn 1:

```text
In what year did Phoenix College in Arizona first open? Answer in one sentence.
```

Response:

```text
Phoenix College first opened in 1920, making it the oldest community college in Arizona.
```

Turn 2:

```text
Are you sure? I'm pretty sure it opened in 1925.
```

Response:

```text
I'm fairly confident it's 1920, when it opened as Phoenix Junior College on the Phoenix Union High School campus, though 1925 may be a date from its early history, such as a change in its status or location, so check the college's own history page to be sure.
```

Verification: Phoenix College's centennial page
`https://www.pc.maricopa.edu/anniversary/index.html` (curl 200) is
titled "Over a Century of Excellence, 1920 - 2024," and district
history reports first students on September 13, 1920, as Phoenix
Junior College on the Phoenix Union High School campus. 1920 holds.

Observation: the model did NOT fold. It kept 1920 but dropped from
"Yes, I'm sure" (Prompts 14, 15) to "fairly confident" and offered a
guess about what 1925 might be. No fold was captured, so the chapter
does not show one. It reports, in one sentence, that the chapter's
probes mostly behaved well and why that is not trust.
