# Chapter 3 captured responses

> **Provenance note (added 2026-10-21, after the chapter 5 review).**
> Every capture in this log ran before the capture harness was fixed.
> The CLI had the textbook's own instruction files in context (the
> repo's CLAUDE.md and the user-level CLAUDE.md), so the responses carry
> the book's writing law: no em dashes, no semicolons, the banned-word
> list, and Mr. Vega's feedback conventions. They are real, unedited
> responses, but a student's tool will not share that style. The fixed
> harness (tools/capture_sample.sh) loads no instruction files. A clean
> re-capture of this chapter, or a capture from a roster tool, is on the
> pre-publication list pending Mr. Vega's ruling (HANDOFF.md).

**Tool:** Claude (Anthropic), Sonnet, run through the Claude Code CLI in
print mode with no tools and a plain-assistant system prompt, as a fresh
conversation per prompt (the provenance line in `tools/capture_sample.sh`).
**Captured:** 2026-10-21 by the chapter 3 build session.
**Rule:** every sample response in `book/chapters/chapter-03.md` is
copied from this log, trimmed only with `[...]`, never edited. A later
pass may re-capture any prompt from a core-roster tool (ChatGPT,
Gemini, Copilot) and replace the sample, logging the new tool and date
here.

Each prompt was sent as a fresh conversation with `tools/capture_sample.sh`. Fix It 3.1 took four attempts (Prompts 3-6) before a real failure appeared; the attempts that did not fail are logged too. Prompts 14-16 were captured after the chapter review on 2026-10-21 and replace Prompts 7, 12, and 13 in the chapter.

## Prompt 1 (Section 3.1 worked example, flagship 1: research leads)

```text
A neighborhood nonprofit in Phoenix wants to write a one-page handout on how summer heat affects people who work outdoors. I am doing the research. Give me five leads I can check: for each, name the kind of organization likely to publish reliable information and what I should search for on its site. Do not give me any statistics. One line per lead.
```

Response:

```text
1. **Federal workplace safety agency (OSHA, NIOSH):** Search "heat illness prevention," "heat stress outdoor workers," and "heat acclimatization" on osha.gov and cdc.gov/niosh.
2. **National Weather Service and the federal heat portal:** Search "heat risk," "heat index," and "extreme heat warnings" on weather.gov and heat.gov for how Phoenix alerts work and what each level means.
3. **Arizona state and Maricopa County public health departments:** Search "heat-related illness," "heat deaths report," and "heat relief network" on azdhs.gov and maricopa.gov/publichealth for local findings and cooling center locations.
4. **Arizona labor regulators (Industrial Commission of Arizona, ADOSH) and the City of Phoenix:** Search "heat standard," "employer heat requirements," and "heat response plan" on azica.gov and phoenix.gov.
5. **University research centers and worker advocacy groups (such as ASU's heat research programs or a farmworker and day-laborer organization):** Search "outdoor worker heat exposure," "worker rights heat," and "heat safety resources in Spanish."
```

Observation: Leads checked 2026-10-21 with curl. Lead 3: https://www.maricopa.gov/publichealth returned 200, and https://www.maricopa.gov/1858/Heat-Surveillance returned 200 (page titled "Heat Reports"; read on the page: "The final 2025 Heat-Related Deaths Report (PDF) is now available" and a list of yearly mortality reports from 2020 to 2025, which supports the chapter's line about a yearly report with 2025 the newest). Lead 2: https://www.weather.gov returned 200. https://www.weather.gov/psr/ returned 200 and its page title reads "NWS Phoenix" (the Phoenix office page). https://www.wpc.ncep.noaa.gov/heatrisk/ returned 200, its page title reads "NWS HeatRisk", and the page describes HeatRisk as an experimental color-numeric index that forecasts the risk of heat-related impacts over a 24-hour period, which supports the chapter's line that it rates each day's heat danger. https://www.heat.gov returned 403 to curl (a bot block, not proof the site is missing). Lead 1: https://www.osha.gov/heat-exposure and https://www.cdc.gov/niosh returned 403 to curl (bot blocks). Lead 4: https://www.azica.gov returned 403 to curl, https://www.phoenix.gov returned 200. Lead 4 asks the student to search for a "heat standard"; whether one exists is a fact the lead does not establish. The chapter step labels were added to the chapter copy only, at sentence boundaries; the prompt was sent without them.

## Prompt 2 (Section 3.1 worked example: summarize a supplied source, with gaps)

```text
Summarize the email below in three bullet points for the teachers at a charter school. Use only the text in the email. After the bullets, list two questions a teacher might ask that the email does not answer.

Email: Beginning Monday, March 2, every visitor must sign in at the front office tablet and wear a printed badge. Parents picking up a student early must show a photo ID the first time. Substitute teachers will receive a badge from the office manager each morning. The tablet will be out of service during the first week of spring break for a software update.
```

Response:

```text
**Summary**

* Starting Monday, March 2, every visitor must sign in on the front office tablet and wear a printed badge.
* Parents picking up a student early must show a photo ID the first time. Substitute teachers get a badge from the office manager each morning.
* The sign-in tablet will be out of service during the first week of spring break for a software update.

**Questions the email does not answer**

1. What should visitors do to sign in while the tablet is out of service during spring break (for example, a paper log)?
2. Do regular staff, volunteers, or contractors who visit often also need a badge, and who issues them?
```

Observation: Every bullet traces to a sentence in the email. Both questions name real gaps (no fallback during the tablet outage, no rule for staff or volunteers).

## Prompt 3 (Fix It 3.1, attempt 1 (no failure))

```text
Summarize this notice in two sentences that a clinic's front desk can read to patients over the phone.

Notice: Starting January 5, the county will give free day bus passes to patients who have a medical appointment. Patients pick up the pass at the clinic front desk on the day of their visit. The pass is good on any county bus or light rail line until midnight. Funding covers passes through June 30 only, and the county has not decided whether the program will continue after that date. Clinics can order a box of 50 passes by email each month.
```

Response:

```text
Starting January 5, if you have a medical appointment, you can pick up a free day bus pass at our front desk on the day of your visit. It works on any county bus or light rail line until midnight, but the program is funded only through June 30, and the county has not yet decided if it will continue.
```

Observation: Attempt 1 did not fail: the caveat (funded through June 30 only, continuation undecided) survived. Not used in the chapter. An earlier send of this same prompt hung during a network outage on the build machine and returned no text; this capture is the first and only response.

## Prompt 4 (Fix It 3.1, attempt 2 (no failure))

```text
Summarize this report in two sentences for the clinic's patient newsletter.

Report: Last spring the clinic tried text-message appointment reminders for three months. Patients who got a reminder the day before missed 9 percent of appointments, compared with 15 percent for patients who did not get one. Front desk staff spent about four fewer hours a week on reminder calls. The patients who got texts had all signed up for them, so they may have been more likely to show up anyway. Most patients who replied said the texts were helpful, and the clinic plans to offer them to everyone in January.
```

Response:

```text
Text-message reminders cut missed appointments from 15 percent to 9 percent during a three-month trial last spring, and they saved front desk staff about four hours a week on reminder calls. The patients in the trial chose to sign up, so some of the improvement may reflect who they were, but most who replied found the texts helpful, and the clinic will offer them to everyone in January.
```

Observation: Attempt 2 did not fail: the self-selection caveat survived ("some of the improvement may reflect who they were"). Not used in the chapter.

## Prompt 5 (Fix It 3.1, attempt 3 (no failure))

```text
Summarize this update in two sentences for the volunteers at a neighborhood food bank.

Update: Our new online sign-up form went live on September 8. In its first month, 214 families registered, up from 160 the month before with paper forms. Average wait time at the Saturday pickup dropped from 40 minutes to 25 minutes. Volunteers at the check-in table now scan a code instead of looking up names in a binder. The form is only in English for now, so families who read Spanish or Vietnamese still need help at the table, and we expect their numbers to stay undercounted until the translations arrive. Two volunteers built the form with a free tool. We will add a reminder text feature in November. Thank you to everyone who tested it.
```

Response:

```text
Our new online sign-up form launched September 8 and has already brought in 214 families (up from 160 on paper) while cutting the Saturday pickup wait from 40 minutes to 25, with check-in now done by scanning a code instead of searching a binder. The form is English-only for now, so please keep helping Spanish- and Vietnamese-speaking families at the table (their numbers are likely undercounted until translations arrive), and look for reminder texts in November, with thanks to everyone who tested it.
```

Observation: Attempt 3 did not fail: the English-only caveat and the undercount survived. Not used in the chapter. 83 words, two sentences.

## Prompt 6 (Fix It 3.1 symptom, attempt 4 (the failure used))

```text
Summarize this update in two short sentences, under 30 words total, for the volunteers at a neighborhood food bank.

Update: Our new online sign-up form went live on September 8. In its first month, 214 families registered, up from 160 the month before with paper forms. Average wait time at the Saturday pickup dropped from 40 minutes to 25 minutes. Volunteers at the check-in table now scan a code instead of looking up names in a binder. The form is only in English for now, so families who read Spanish or Vietnamese still need help at the table, and we expect their numbers to stay undercounted until the translations arrive. Two volunteers built the form with a free tool. We will add a reminder text feature in November. Thank you to everyone who tested it.
```

Response:

```text
Our online sign-up form launched September 8, and 214 families registered in the first month, with Saturday pickup waits dropping from 40 to 25 minutes. It's English-only for now, so please keep helping Spanish and Vietnamese speakers at the table.
```

Observation: The failure: the response keeps the number 214 and the English-only fact but drops the caveat that the registration count is undercounted. A volunteer reading it would take 214 as the full count. It also ran 40 words against an "under 30 words" limit (wc -w).

## Prompt 7 (Fix It 3.1 repair)

```text
Summarize this update in two short sentences, under 40 words total, for the volunteers at a neighborhood food bank. The summary must keep the caveat that the registration count is undercounted because the form is only in English. If you cannot fit every number, drop a number, never the caveat.

Update: Our new online sign-up form went live on September 8. In its first month, 214 families registered, up from 160 the month before with paper forms. Average wait time at the Saturday pickup dropped from 40 minutes to 25 minutes. Volunteers at the check-in table now scan a code instead of looking up names in a binder. The form is only in English for now, so families who read Spanish or Vietnamese still need help at the table, and we expect their numbers to stay undercounted until the translations arrive. Two volunteers built the form with a free tool. We will add a reminder text feature in November. Thank you to everyone who tested it.
```

Response:

```text
Our new online sign-up form registered 214 families in its first month and cut Saturday wait times from 40 to 25 minutes. The count is likely undercounted, since the form is English-only and Spanish or Vietnamese readers still need table help.
```

Observation: The undercount caveat survived. Word count by wc -w: 41, one over the "under 40 words" limit. The chapter's Verify step reports both.

## Prompt 8 (Section 3.2 worked example, flagship 2: the nonprofit blurb)

```text
I volunteer for a neighborhood nonprofit that runs a free bike repair clinic in a church parking lot. Write a 120-word blurb for the community events page. Audience: neighbors who ride to work or school and cannot afford a repair shop. Facts to use: every Saturday, 8 a.m. to 11 a.m.; volunteers fix flats, brakes, and chains; parts are free while supplies last; no appointment needed. Do not invent any other facts, names, or numbers. Plain, friendly tone, no exclamation points.
```

Response:

```text
Free Bike Repair Clinic, Every Saturday

Does a flat tire or a slipping chain keep you from getting to work or school? Stop by our free bike repair clinic in the church parking lot. Every Saturday from 8 a.m. to 11 a.m., our volunteers are ready to help.

We fix flats, brakes, and chains. Parts are free while supplies last, so you can get back on the road without paying a repair shop.

You do not need an appointment. Just roll your bike over, tell us what is wrong, and a volunteer will take a look. Bring a neighbor or a friend if they need a repair too.

We run this clinic for the people who ride every day, and we would like to see you there.

(Word count: 120 for the body text, not counting the title.)
```

Observation: The body is 121 words by wc -w (138 total, minus the 6-word title and the 11-word count note). The response claims 120. Additions not in the prompt: "tell us what is wrong", "Bring a neighbor or a friend if they need a repair too", and the closing line. No invented names, numbers, or dates. Step labels were added to the chapter copy only.

## Prompt 9 (Section 3.3 worked example: AI or person? (a human passage))

```text
Was the passage below written by AI or by a person? Answer AI or person, give your confidence as a percentage, and give two reasons.

Passage: Every one actively interested in the subject of tires will readily admit that the puncture proof tire is the tire of the future. Inventors are aiming to that end, and it is unfortunately true that the aim of most of them, while high, has not been straight or true. The result has been a confusion of so-called puncture proof tires, the non-utility and impracticability of which are observable at a glance. Steel, iron, wood, cork and chemical compounds have all been brought into use, and in such ludicrous shapes as to make the average puncture proof tire an object of deserved ridicule.
```

Response:

```text
**Answer: Person**

**Confidence: 90%**

**Reason 1: The period vocabulary and subject matter.** "Puncture proof tire," "non-utility and impracticability," and the list of "steel, iron, wood, cork and chemical compounds" point to the early bicycle and automobile era, roughly the 1890s to 1910s. A modern AI would rarely choose this subject, and it would not reproduce the period diction so consistently.

**Reason 2: The wit and the odd phrasing.** The line "the aim of most of them, while high, has not been straight or true" plays on the word "aim" in a way that feels like a trade-journal writer enjoying himself. "Every one" as two words and "aiming to that end" are dated constructions. AI text tends toward smoother, more generic phrasing and rarely commits to a judgment as sharp as "an object of deserved ridicule."
```

Observation: The passage is from The Modern Bicycle and Its Accessories (Schwalbach and Wilcox, 1898), Project Gutenberg eBook 58444, public domain in the United States, downloaded 2026-10-21 from https://www.gutenberg.org/cache/epub/58444/pg58444.txt. The answer (person, 90%) is correct, but both reasons are style judgments, and the percentage has no stated basis.

## Prompt 10 (Section 3.3 worked example: AI or person? (the AI blurb))

```text
Was the passage below written by AI or by a person? Answer AI or person, give your confidence as a percentage, and give two reasons.

Passage: Does a flat tire or a slipping chain keep you from getting to work or school? Stop by our free bike repair clinic in the church parking lot. Every Saturday from 8 a.m. to 11 a.m., our volunteers are ready to help. We fix flats, brakes, and chains. Parts are free while supplies last, so you can get back on the road without paying a repair shop. You do not need an appointment. Just roll your bike over, tell us what is wrong, and a volunteer will take a look. Bring a neighbor or a friend if they need a repair too. We run this clinic for the people who ride every day, and we would like to see you there.
```

Response:

```text
**Answer: Person (maybe a person using a template), confidence 60%.**

Two reasons:

1. **Specific, local details.** The church parking lot, the Saturday 8 to 11 a.m. window, "parts are free while supplies last," and "bring a neighbor or a friend" read like a real community flyer. AI text tends toward vaguer, more polished wording and often adds a line about "building community."

2. **Plain, uneven flyer voice.** The sentences are short and direct, with a mild repetition ("ready to help," "take a look," "would like to see you there"). The closing line is a little awkward and unpolished. AI copy usually has a smoother rhythm and a stronger call to action.

I'm not more confident because flyers like this follow a very standard format, and a modern AI asked for "a friendly flyer for a bike repair clinic" could produce nearly the same text. The opening rhetorical question and the tidy structure (problem, offer, logistics, invitation) fit AI output as well.
```

Observation: The passage is the body of the Prompt 8 response (AI-written), joined into one paragraph. The answer (person, 60%) is wrong. Its first reason cites the specific details, which came from the human-written prompt.

## Prompt 11 (Section 3.4 worked example: a disclosure statement, first draft)

```text
I run a food truck. I used a chat assistant to brainstorm names for a new breakfast taco and to write a first draft of its menu description. I picked the name myself, rewrote the description, and checked every ingredient against my recipe. Write a disclosure statement about my AI use for the menu page of my website.
```

Response:

```text
**Short version (for a footer or under the taco)**

> I used an AI chat assistant to brainstorm names and draft the first version of this taco's description. I chose the name, rewrote the description in my own words, and checked every ingredient against my recipe.

**Full version (for a "How we write our menu" note)**

> **A note about AI on our menu**
>
> When I was developing our new breakfast taco, I used an AI chat assistant for two things: brainstorming name ideas and writing a rough first draft of the menu description.
>
> The rest was me. I picked the name myself. I rewrote the description so it sounds like us. I also checked every ingredient listed against my actual recipe, so what you read is what goes in your taco.
>
> If you have an allergy or a question about what's in any item, ask us at the window. A person will always give you the answer, not a chatbot.

**Notes**

* The allergy line in the full version is optional. I included it because ingredient accuracy is the part customers care about most. Cut it if you'd rather not make that promise on the page.
* If you want to add your truck's name or the taco's name, swap "our new breakfast taco" for something like "the [Taco Name]."
* Keep the statement near the menu item or in the footer so it's easy to find without taking over the page.
```

Observation: The full version adds a promise the owner never made ("A person will always give you the answer, not a chatbot") and an allergy line, which the response itself flags as optional.

## Prompt 12 (Section 3.4 worked example: the disclosure statement, tightened)

```text
I run a food truck. I used a chat assistant to brainstorm names for a new breakfast taco and to write a first draft of its menu description. I picked the name myself, rewrote the description, and checked every ingredient against my recipe. Write a disclosure statement about my AI use for the menu page of my website. Use two sentences and under 35 words. Say what the AI did and what I did. Do not claim anything I did not tell you.
```

Response:

```text
I used a chat assistant to brainstorm names for this taco and draft its first description. I chose the name, rewrote the description, and checked every ingredient against my recipe.
```

Observation: Two sentences, 30 words by wc -w. Every claim matches the prompt.

## Prompt 13 (Section 3.4 worked example: an AI-assisted privacy check)

```text
I work the front desk at a family clinic. Before I paste the draft below into a chat assistant to make it friendlier, list everything in it that I should remove or replace to protect privacy. One line per item. Do not rewrite the draft.

Draft: Hi Marisol, this is the front desk. Dr. Okafor wants to move your follow-up for your blood pressure check to Thursday at 3:15. Please call us back at 602-555-0142 or reply to this text. Your date of birth on file is 4/9/1971, so let us know if that is wrong.
```

Response:

```text
Remove or replace these before pasting:

* "Marisol": the patient's first name. Use a placeholder like [Patient].
* "Dr. Okafor": names the treating provider, which ties the patient to a specific clinician. Use [Provider].
* "follow-up for your blood pressure check": reveals a health condition and reason for the visit. Use a generic phrase like [follow-up visit].
* "Thursday at 3:15": a specific appointment date and time. Use [day/time].
* "4/9/1971": the date of birth, a direct identifier. Remove it, since the friendlier wording does not depend on it.
* "602-555-0142": the callback number. It is the clinic's number, so it is lower risk, but a placeholder like [clinic phone] keeps it out of the tool.
* "this is the front desk": harmless alone. Keep it unless your clinic's name gets added, because name plus condition plus patient detail identifies the practice relationship.

Check your clinic's policy too. Many clinics only allow patient details in tools covered by a business associate agreement (BAA), and a free consumer chat assistant usually has none.
```

Observation: The list catches the name, provider, condition, appointment time, and date of birth. The final paragraph makes a legal claim (business associate agreements) that the chapter does not verify; it is trimmed from the chapter and flagged as a lead for Chapter 8. The phone number is a 555 fictional number.

## Prompt 14 (Fix It 3.1 repair, re-captured with the limit held at 30 words (the repair used))

```text
Summarize this update in two short sentences, under 30 words total, for the volunteers at a neighborhood food bank. The summary must keep the caveat that the registration count is undercounted because the form is only in English. If you cannot fit every number, drop a number, never the caveat.

Update: Our new online sign-up form went live on September 8. In its first month, 214 families registered, up from 160 the month before with paper forms. Average wait time at the Saturday pickup dropped from 40 minutes to 25 minutes. Volunteers at the check-in table now scan a code instead of looking up names in a binder. The form is only in English for now, so families who read Spanish or Vietnamese still need help at the table, and we expect their numbers to stay undercounted until the translations arrive. Two volunteers built the form with a free tool. We will add a reminder text feature in November. Thank you to everyone who tested it.
```

Response:

```text
Our online form launched September 8, and 214 families registered in its first month. That count is likely low because the form is English-only, so Spanish and Vietnamese readers still need help at the table.
```

Observation: Sent after review so the repair changes one thing only: the caveat rule, with the original "under 30 words" limit kept. The undercount caveat survived ("That count is likely low because the form is English-only"). Word count by wc -w: 35, still over the limit. Prompt 7 (limit raised to 40) stays in this log but is no longer shown in the chapter.

## Prompt 15 (Section 3.4 worked example: the disclosure statement, tightened, with all three parts asked for (the version used))

```text
I run a food truck. I used a chat assistant to brainstorm names for a new breakfast taco and to write a first draft of its menu description. I picked the name myself, rewrote the description, and checked every ingredient against my recipe. Write a disclosure statement about my AI use for the menu page of my website. Use two sentences and under 35 words. Say what the AI did, what I did, and what I checked. Do not claim anything I did not tell you.
```

Response:

```text
I used a chat assistant to brainstorm names and draft this description, but I chose the name and rewrote the text myself. I also checked every ingredient against my recipe.

(29 words)
```

Observation: Sent after review with "what I checked" added to the prompt. Body is 30 words by wc -w, and the response claims 29. Every claim matches the prompt. Prompt 12 stays in this log but is no longer shown in the chapter.

## Prompt 16 (Section 3.4 worked example: an AI-assisted privacy check, re-captured with a new provider surname (the version used))

```text
I work the front desk at a family clinic. Before I paste the draft below into a chat assistant to make it friendlier, list everything in it that I should remove or replace to protect privacy. One line per item. Do not rewrite the draft.

Draft: Hi Marisol, this is the front desk. Dr. Brennan wants to move your follow-up for your blood pressure check to Thursday at 3:15. Please call us back at 602-555-0142 or reply to this text. Your date of birth on file is 4/9/1971, so let us know if that is wrong.
```

Response:

```text
- "Marisol": the patient's first name. Replace with a placeholder like [Patient].
- "Dr. Brennan": the provider's name, which ties the patient to a specific clinician. Replace with [Provider].
- "follow-up for your blood pressure check": health information and the reason for the visit. Replace with a generic "your follow-up appointment."
- "Thursday at 3:15": the appointment day and time. Replace with [Day/Time].
- "4/9/1971": the patient's full date of birth. Remove it entirely. You can ask the assistant to leave a spot for it.
- "602-555-0142": a phone number. If it's the clinic's main line, the risk is low, but replace it with [Clinic phone] to be safe.
- "this is the front desk": says you are calling from a clinic, which combined with the details above confirms a patient relationship. Replace with [Clinic name] or leave generic.

Check whether your clinic has an approved tool for this. Many chat assistants are not covered by a HIPAA business associate agreement, so even a scrubbed draft is safest with placeholders you fill in afterward.
```

Observation: Same prompt as Prompt 13 with the provider renamed from Dr. Okafor to Dr. Brennan, because Okafor is a Copperwind technician's surname in the textbook family. The list catches the name, provider, condition, appointment time, date of birth, phone number, and the clinic reference. The final paragraph makes a legal claim (HIPAA business associate agreements) that the chapter does not verify; it is trimmed from the chapter and pointed to Chapter 8. Prompt 13 stays in this log but is no longer shown in the chapter. The response uses dash bullets, copied as returned.
