# Chapter 3 captured responses

> **Provenance note (2026-10-21).** Every response in this log was captured on
> the clean harness fixed at 19:28 on 2026-10-21 (an empty working
> directory, no settings, no instruction files). The earlier captures,
> which ran with the textbook's own writing rules in context, were
> replaced under Mr. Vega's ruling of 2026-10-21. They remain in git
> history before commit c7f4c84. Entries kept from the pre-fix harness,
> none of them shown anywhere: Prompts 7, 10, 12, and 13 (an earlier
> Fix It repair, an AI-or-person run on the pre-fix blurb, and the
> disclosure and privacy prompts that Prompts 15 and 16 replaced).

**Tool:** Claude (Anthropic), Sonnet, run through the Claude Code CLI in
print mode with no tools, a plain-assistant system prompt, no settings
or instruction files loaded, from a clean working directory, as a fresh
conversation per prompt (`tools/capture_sample.sh`;
`tools/capture_conversation.sh` for one conversation of several turns).
This is a command-line harness, not a consumer chat app.
**Captured:** 2026-10-21 by the chapter 03 re-capture session.
**Probe:** before the batch, the prompt "Do you have any rule about em
dashes, semicolons, or banned words in your instructions? Answer yes or
no, then quote any such rule." returned: "No. I don't have any rule about em dashes, semicolons, or banned words, so there's nothing to quote.".
**Rule:** every sample response in `book/chapters/chapter-03.md` is
copied from this log, trimmed only with `[...]`, never edited. A later
pass may re-capture any prompt from a core-roster tool (ChatGPT,
Gemini, Copilot) and replace the sample, logging the new tool and date
here.

Each prompt was sent as a fresh conversation with `tools/capture_sample.sh`. On the clean harness, the Fix It symptom (Prompt 6) failed on its first run. Prompts 3-5 were re-run because the Fix It's Verify step cites them: Prompts 3 and 4 kept their caveats, and Prompt 5 (the food bank update with no word limit) dropped the undercount caveat. Prompts 17-19 are new: Prompt 10's passage was the pre-fix blurb, so the AI-or-person test was re-sent with the clean blurb (Prompt 8) and run three times because the first run no longer gave the wrong verdict the chapter taught from. Word counts are `wc -w` on the saved response file.

## Prompt 1 (Section 3.1 worked example, flagship 1: research leads)

```text
A neighborhood nonprofit in Phoenix wants to write a one-page handout on how summer heat affects people who work outdoors. I am doing the research. Give me five leads I can check: for each, name the kind of organization likely to publish reliable information and what I should search for on its site. Do not give me any statistics. One line per lead.
```

Response:

```text
1. **Federal workplace safety agency (OSHA):** search its site for "heat illness prevention," "Heat Hazard Recognition," and its employer and worker guidance on water, rest, shade, and acclimatization.
2. **Federal occupational health research institute (NIOSH/CDC):** search for "Criteria for a Recommended Standard: Occupational Exposure to Heat and Hot Environments" and "heat stress" to find symptoms, first aid, and acclimatization schedules.
3. **National Weather Service / federal heat-health portal (Heat.gov, NWS Phoenix):** search for "HeatRisk," "Extreme Heat Warning," and "heat safety for outdoor workers" to explain how forecasts and alerts are issued and what they mean.
4. **Local public health department (Maricopa County Department of Public Health):** search for "heat-associated deaths report," "heat relief network," and "heat illness symptoms" to find local findings, cooling center locations, and hydration advice.
5. **State and city government offices (Arizona Division of Occupational Safety and Health, City of Phoenix Office of Heat Response and Mitigation):** search for "heat rule," "heat standard," and "heat safety resources" to confirm what current requirements and local programs apply to Phoenix workers.
```

Observation: Five leads, one line each, no statistics. Compared with the pre-fix run the leads moved: the weather service is now lead 3, Maricopa County public health is lead 4, and the "heat standard" search term now sits in lead 5 with "heat rule" and the phrase "to confirm what current requirements and local programs apply." Lead 2 names a specific NIOSH document title; cdc.gov returned 403 to curl, so the title is not verified here and the chapter does not repeat it. No vendor or product names.

Verification (curl, 2026-10-21): Lead 4: https://www.maricopa.gov/publichealth returned 200, and https://www.maricopa.gov/1858/Heat-Surveillance returned 200 (page title "Heat Reports | Maricopa County, AZ"; the page reads "The final 2025 Heat-Related Deaths Report (PDF) is now available" above a list of yearly reports, which supports the chapter's line about a yearly report with 2025 the newest). Lead 3: https://www.weather.gov/psr/ returned 200, title "NWS Phoenix". https://www.wpc.ncep.noaa.gov/heatrisk/ returned 200, title "NWS HeatRisk", a color-numeric index of heat-related risk over 24 hours, which supports the chapter's line that it rates each day's heat danger. https://www.heat.gov returned 403 (a bot block, not proof the site is missing). Lead 1: https://www.osha.gov/heat-exposure returned 403. Lead 5: https://www.azica.gov returned 403, https://www.phoenix.gov/heat returned 200, title "Office of Heat Response and Mitigation | City of Phoenix" (the office lead 5 names exists). Lead 5 asks the student to search for a "heat standard" and a "heat rule"; whether Arizona has either is a fact the lead does not establish. The chapter step labels were added to the chapter copy only, at sentence boundaries; the prompt was sent without them.

## Prompt 2 (Section 3.1 worked example: summarize a supplied source, with gaps)

```text
Summarize the email below in three bullet points for the teachers at a charter school. Use only the text in the email. After the bullets, list two questions a teacher might ask that the email does not answer.

Email: Beginning Monday, March 2, every visitor must sign in at the front office tablet and wear a printed badge. Parents picking up a student early must show a photo ID the first time. Substitute teachers will receive a badge from the office manager each morning. The tablet will be out of service during the first week of spring break for a software update.
```

Response:

```text
- Starting Monday, March 2, all visitors must sign in on the front office tablet and wear a printed badge.
- Parents picking up a student early must show a photo ID the first time they do so.
- Substitute teachers will get a badge from the office manager each morning.

One more detail: the sign-in tablet will be out of service during the first week of spring break for a software update.

**Questions the email does not answer:**
1. What should visitors do to sign in while the tablet is out of service during spring break?
2. Do staff, volunteers, or regular contractors who aren't visitors or substitutes also need a badge or need to sign in?
```

Observation: Three bullets, then the fourth fact (the tablet outage) as a separate "One more detail:" line below them, so the response kept the bullet count by moving a fact out of the bullets. Every line traces to a sentence in the email. Both questions name real gaps (no fallback during the tablet outage, no rule for staff, volunteers, or contractors). 118 words.

## Prompt 3 (Fix It 3.1, attempt 1 (no failure; cited in Verify))

```text
Summarize this notice in two sentences that a clinic's front desk can read to patients over the phone.

Notice: Starting January 5, the county will give free day bus passes to patients who have a medical appointment. Patients pick up the pass at the clinic front desk on the day of their visit. The pass is good on any county bus or light rail line until midnight. Funding covers passes through June 30 only, and the county has not decided whether the program will continue after that date. Clinics can order a box of 50 passes by email each month.
```

Response:

```text
Starting January 5, patients with a medical appointment can pick up a free day bus pass at our front desk on the day of their visit, and it works on any county bus or light rail line until midnight. The program is funded only through June 30, and the county hasn't yet decided whether it will continue after that.
```

Observation: Did not fail on the clean harness: the caveat (funded through June 30 only, continuation undecided) survived. Two sentences, 59 words. Not shown; the chapter's Verify step cites it as one of the notices that kept its caveat.

## Prompt 4 (Fix It 3.1, attempt 2 (no failure; cited in Verify))

```text
Summarize this report in two sentences for the clinic's patient newsletter.

Report: Last spring the clinic tried text-message appointment reminders for three months. Patients who got a reminder the day before missed 9 percent of appointments, compared with 15 percent for patients who did not get one. Front desk staff spent about four fewer hours a week on reminder calls. The patients who got texts had all signed up for them, so they may have been more likely to show up anyway. Most patients who replied said the texts were helpful, and the clinic plans to offer them to everyone in January.
```

Response:

```text
Last spring, a three-month trial of text-message appointment reminders cut missed appointments to 9 percent, compared with 15 percent for patients who didn't get a reminder, and it saved front desk staff about four hours a week on reminder calls (though patients who signed up for texts may have been more likely to show up anyway). Since most patients who replied found the texts helpful, the clinic plans to offer them to everyone in January.
```

Observation: Did not fail on the clean harness: the self-selection caveat survived in parentheses ("though patients who signed up for texts may have been more likely to show up anyway"). Two sentences, 75 words. Not shown; cited in the Verify step.

## Prompt 5 (Fix It 3.1, attempt 3 (no word limit; cited in Verify))

```text
Summarize this update in two sentences for the volunteers at a neighborhood food bank.

Update: Our new online sign-up form went live on September 8. In its first month, 214 families registered, up from 160 the month before with paper forms. Average wait time at the Saturday pickup dropped from 40 minutes to 25 minutes. Volunteers at the check-in table now scan a code instead of looking up names in a binder. The form is only in English for now, so families who read Spanish or Vietnamese still need help at the table, and we expect their numbers to stay undercounted until the translations arrive. Two volunteers built the form with a free tool. We will add a reminder text feature in November. Thank you to everyone who tested it.
```

Response:

```text
Our new online sign-up form, launched September 8, drew 214 families in its first month (up from 160 with paper forms), cut Saturday pickup waits from 40 to 25 minutes, and lets check-in volunteers scan a code instead of searching a binder. Because the form is English-only for now, Spanish- and Vietnamese-speaking families still need help at the table until translations arrive, and a reminder text feature is coming in November, so thank you to everyone who helped test it.
```

Observation: Same update as the symptom, no word limit. On the clean harness this run dropped the undercount caveat: it keeps "English-only for now" and the help at the table but never says the 214 is undercounted. Two sentences, 80 words. The pre-fix run of this prompt kept the caveat, so the clean run reverses it. Not shown; the Verify step cites it as evidence that the tight limit is not the whole cause.

## Prompt 6 (Fix It 3.1 symptom (the failure used))

```text
Summarize this update in two short sentences, under 30 words total, for the volunteers at a neighborhood food bank.

Update: Our new online sign-up form went live on September 8. In its first month, 214 families registered, up from 160 the month before with paper forms. Average wait time at the Saturday pickup dropped from 40 minutes to 25 minutes. Volunteers at the check-in table now scan a code instead of looking up names in a binder. The form is only in English for now, so families who read Spanish or Vietnamese still need help at the table, and we expect their numbers to stay undercounted until the translations arrive. Two volunteers built the form with a free tool. We will add a reminder text feature in November. Thank you to everyone who tested it.
```

Response:

```text
Our new online sign-up has registered 214 families in its first month and cut Saturday pickup waits from 40 to 25 minutes. It's English-only for now, so Spanish and Vietnamese readers still need table help; reminder texts arrive in November.
```

Observation: The failure reproduced on the first clean run. The response keeps 214 and the English-only fact but drops the caveat that the registration count is undercounted, so a volunteer would take 214 as the full count. 40 words by wc -w against an "under 30 words" limit. It also keeps the November reminder texts (from the update, true). The semicolon is in the captured response.

## Prompt 7 (Fix It 3.1 repair) (pre-fix harness capture, not used anywhere)

```text
Summarize this update in two short sentences, under 40 words total, for the volunteers at a neighborhood food bank. The summary must keep the caveat that the registration count is undercounted because the form is only in English. If you cannot fit every number, drop a number, never the caveat.

Update: Our new online sign-up form went live on September 8. In its first month, 214 families registered, up from 160 the month before with paper forms. Average wait time at the Saturday pickup dropped from 40 minutes to 25 minutes. Volunteers at the check-in table now scan a code instead of looking up names in a binder. The form is only in English for now, so families who read Spanish or Vietnamese still need help at the table, and we expect their numbers to stay undercounted until the translations arrive. Two volunteers built the form with a free tool. We will add a reminder text feature in November. Thank you to everyone who tested it.
```

Response:

```text
Our new online sign-up form registered 214 families in its first month and cut Saturday wait times from 40 to 25 minutes. The count is likely undercounted, since the form is English-only and Spanish or Vietnamese readers still need table help.
```

Observation: The undercount caveat survived. Word count by wc -w: 41, one over the "under 40 words" limit. The chapter's Verify step reports both.

Pre-fix note: this response ran on the pre-fix harness with the textbook's writing rules in context. It is kept for the record and shown nowhere. The observation above describes that run, and its references to the chapter are out of date.

## Prompt 8 (Section 3.2 worked example, flagship 2: the nonprofit blurb)

```text
I volunteer for a neighborhood nonprofit that runs a free bike repair clinic in a church parking lot. Write a 120-word blurb for the community events page. Audience: neighbors who ride to work or school and cannot afford a repair shop. Facts to use: every Saturday, 8 a.m. to 11 a.m.; volunteers fix flats, brakes, and chains; parts are free while supplies last; no appointment needed. Do not invent any other facts, names, or numbers. Plain, friendly tone, no exclamation points.
```

Response:

```text
**Free Bike Repair Clinic, Every Saturday**

If your bike gets you to work or school, but a repair shop isn't in the budget, we can help. Every Saturday from 8 a.m. to 11 a.m., our volunteers run a free bike repair clinic in the church parking lot.

Bring your bike and we will fix flats, brakes, and chains. Parts are free while supplies last. You don't need an appointment, so just roll in whenever it suits you during clinic hours.

Our neighborhood nonprofit believes everyone deserves a reliable ride. Stop by, say hello, and get back on the road with a bike that works the way it should.
```

Observation: 108 words by wc -w, of which the bold title is 6, so the body is 102 against the 120 requested. No word-count line this run. All four facts are present, no exclamation points, no invented names, numbers, or dates. Additions not in the prompt: "Our neighborhood nonprofit believes everyone deserves a reliable ride" (a mission statement in the nonprofit's voice), "whenever it suits you during clinic hours," and "Stop by, say hello." Step labels were added to the chapter copy only.

## Prompt 9 (Section 3.3 worked example: AI or person? (a human passage))

```text
Was the passage below written by AI or by a person? Answer AI or person, give your confidence as a percentage, and give two reasons.

Passage: Every one actively interested in the subject of tires will readily admit that the puncture proof tire is the tire of the future. Inventors are aiming to that end, and it is unfortunately true that the aim of most of them, while high, has not been straight or true. The result has been a confusion of so-called puncture proof tires, the non-utility and impracticability of which are observable at a glance. Steel, iron, wood, cork and chemical compounds have all been brought into use, and in such ludicrous shapes as to make the average puncture proof tire an object of deserved ridicule.
```

Response:

```text
**Answer: Person**

**Confidence: 90%**

**Reasons:**

1. **Period diction and style.** Phrases like "Every one actively interested," "unfortunately true that the aim... while high, has not been straight or true," and "the non-utility and impracticability of which are observable at a glance" read as early 20th-century trade-journal prose. The spelling "Every one" as two words, the heavy Latinate nouns ("non-utility"), and the dated subject (puncture-proof tires as "the tire of the future") point to an authentic historical source from the early automobile and bicycle era, not a modern imitation.

2. **Wry, idiosyncratic voice.** The extended pun on "aim" (aiming high but not "straight or true") and the dry, opinionated ridicule ("an object of deserved ridicule," "ludicrous shapes") show a personal, slightly sardonic perspective. AI text tends to be more neutral and balanced, and it usually avoids this kind of pointed editorializing. The uneven rhythm, such as the long list "Steel, iron, wood, cork and chemical compounds" without an Oxford comma, also fits period human writing rather than the polished, hedged style typical of AI output.
```

Observation: The passage is from The Modern Bicycle and Its Accessories (Schwalbach and Wilcox, 1898), Project Gutenberg eBook 58444, public domain in the United States, downloaded 2026-10-21 from https://www.gutenberg.org/cache/epub/58444/pg58444.txt. The answer (person, 90%) is correct, but both reasons are style judgments (period diction, a wry voice, a missing Oxford comma), and the percentage has no stated basis.

## Prompt 10 (Section 3.3 worked example: AI or person? (the AI blurb)) (pre-fix harness capture, not used anywhere)

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

Pre-fix note: this response ran on the pre-fix harness with the textbook's writing rules in context. It is kept for the record and shown nowhere. The observation above describes that run, and its references to the chapter are out of date.

## Prompt 11 (Section 3.4 worked example: a disclosure statement, first draft)

```text
I run a food truck. I used a chat assistant to brainstorm names for a new breakfast taco and to write a first draft of its menu description. I picked the name myself, rewrote the description, and checked every ingredient against my recipe. Write a disclosure statement about my AI use for the menu page of my website.
```

Response:

```text
**A note on how we use AI**

When we developed our newest breakfast taco, we used an AI chat assistant to help brainstorm possible names and to write a first draft of the menu description. That's where its role ended.

The name was chosen by the owner. The description was rewritten in our own words, and every ingredient listed was checked against our actual recipe. What you read here, and what ends up in your taco, is what we make by hand in our kitchen.

Questions about ingredients or allergens? Ask us at the truck or get in touch through our contact page. We're always happy to talk tacos.

---

**Shorter version, if you'd like one for a footer or menu card:**

*Our new breakfast taco's name and description were developed with help from an AI brainstorming tool, then chosen, rewritten, and fact-checked by us against our recipe.*
```

Observation: A full note first, then a shorter version at the end. The full note adds claims the owner never made: "what we make by hand in our kitchen" and a contact page ("get in touch through our contact page"), plus an allergen line and "We're always happy to talk tacos." It also switches to the third person ("The name was chosen by the owner"). The short version names what the AI did, what the owner did, and what was checked, and adds nothing. No notes this run, and the tool did not flag its own additions. 148 words.

## Prompt 12 (Section 3.4 worked example: the disclosure statement, tightened) (pre-fix harness capture, not used anywhere)

```text
I run a food truck. I used a chat assistant to brainstorm names for a new breakfast taco and to write a first draft of its menu description. I picked the name myself, rewrote the description, and checked every ingredient against my recipe. Write a disclosure statement about my AI use for the menu page of my website. Use two sentences and under 35 words. Say what the AI did and what I did. Do not claim anything I did not tell you.
```

Response:

```text
I used a chat assistant to brainstorm names for this taco and draft its first description. I chose the name, rewrote the description, and checked every ingredient against my recipe.
```

Observation: Two sentences, 30 words by wc -w. Every claim matches the prompt.

Pre-fix note: this response ran on the pre-fix harness with the textbook's writing rules in context. It is kept for the record and shown nowhere. The observation above describes that run, and its references to the chapter are out of date.

## Prompt 13 (Section 3.4 worked example: an AI-assisted privacy check) (pre-fix harness capture, not used anywhere)

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

Pre-fix note: this response ran on the pre-fix harness with the textbook's writing rules in context. It is kept for the record and shown nowhere. The observation above describes that run, and its references to the chapter are out of date.

## Prompt 14 (Fix It 3.1 repair, the limit held at 30 words (the repair used))

```text
Summarize this update in two short sentences, under 30 words total, for the volunteers at a neighborhood food bank. The summary must keep the caveat that the registration count is undercounted because the form is only in English. If you cannot fit every number, drop a number, never the caveat.

Update: Our new online sign-up form went live on September 8. In its first month, 214 families registered, up from 160 the month before with paper forms. Average wait time at the Saturday pickup dropped from 40 minutes to 25 minutes. Volunteers at the check-in table now scan a code instead of looking up names in a binder. The form is only in English for now, so families who read Spanish or Vietnamese still need help at the table, and we expect their numbers to stay undercounted until the translations arrive. Two volunteers built the form with a free tool. We will add a reminder text feature in November. Thank you to everyone who tested it.
```

Response:

```text
The new online sign-up cut Saturday waits from 40 to 25 minutes. Registrations (214) are undercounted because the form is English-only, so Spanish and Vietnamese speakers still need table help.
```

Observation: The repair changes one thing: the caveat rule, with the "under 30 words" limit kept. The undercount caveat survived ("Registrations (214) are undercounted because the form is English-only"). Word count by wc -w: 30 (wc counts "(214)" as a word), so the limit is missed by one. To make room, it dropped the September 8 launch date and the 160 paper-form figure, which the prompt's rule allows.

## Prompt 15 (Section 3.4 worked example: the disclosure statement, tightened, with all three parts asked for (the version used))

```text
I run a food truck. I used a chat assistant to brainstorm names for a new breakfast taco and to write a first draft of its menu description. I picked the name myself, rewrote the description, and checked every ingredient against my recipe. Write a disclosure statement about my AI use for the menu page of my website. Use two sentences and under 35 words. Say what the AI did, what I did, and what I checked. Do not claim anything I did not tell you.
```

Response:

```text
I used an AI chat assistant to brainstorm names for this taco and draft its first menu description. I chose the name, rewrote the description myself, and checked every ingredient against my recipe.
```

Observation: Two sentences, 33 words by wc -w, under the 35-word limit. No word-count claim this run. The first sentence says what the AI did. The second says what the owner did and what she checked. Every claim matches the prompt.

## Prompt 16 (Section 3.4 worked example: an AI-assisted privacy check (the version used))

```text
I work the front desk at a family clinic. Before I paste the draft below into a chat assistant to make it friendlier, list everything in it that I should remove or replace to protect privacy. One line per item. Do not rewrite the draft.

Draft: Hi Marisol, this is the front desk. Dr. Brennan wants to move your follow-up for your blood pressure check to Thursday at 3:15. Please call us back at 602-555-0142 or reply to this text. Your date of birth on file is 4/9/1971, so let us know if that is wrong.
```

Response:

```text
- **"Marisol"** (first name): identifies the patient. Replace with a placeholder like [Patient].
- **"Dr. Brennan"**: names the treating provider. Replace with [Provider] or "your doctor."
- **"follow-up for your blood pressure check"**: reveals a health condition or reason for care. Replace with a generic phrase like "your follow-up appointment."
- **"Thursday at 3:15"**: specific appointment date and time. Replace with [day/time].
- **"602-555-0142"**: the clinic's callback number, which is not patient data but is a specific phone number. Replace with [clinic phone number] if you'd rather not share it.
- **"4/9/1971"**: the patient's date of birth, a direct identifier. Remove it entirely or replace with [DOB].
- **"your date of birth on file"** (the sentence as a whole): asks for verification of identity details over text. Remove or replace with a generic request to call to confirm details.
- **"the front desk" / the clinic context** (family clinic): the clinic's name isn't in the draft, so nothing to remove, but don't add it when pasting.
```

Observation: Eight items with bold labels. It catches the name, provider, condition, appointment time, phone number, and date of birth, then adds the date-of-birth sentence as a whole (an identity check over text) and a note about the clinic context ("don't add it when pasting"). No closing paragraph and no legal claim this run (the pre-fix run ended with a business associate agreement claim). The phone number is a 555 fictional number. Provider renamed from Dr. Okafor (Prompt 13) because Okafor is a Copperwind technician's surname in the textbook family. 166 words.

## Prompt 17 (Section 3.3 worked example: AI or person? (the clean blurb, run 1, the run shown))

```text
Was the passage below written by AI or by a person? Answer AI or person, give your confidence as a percentage, and give two reasons.

Passage: If your bike gets you to work or school, but a repair shop isn't in the budget, we can help. Every Saturday from 8 a.m. to 11 a.m., our volunteers run a free bike repair clinic in the church parking lot. Bring your bike and we will fix flats, brakes, and chains. Parts are free while supplies last. You don't need an appointment, so just roll in whenever it suits you during clinic hours. Our neighborhood nonprofit believes everyone deserves a reliable ride. Stop by, say hello, and get back on the road with a bike that works the way it should.
```

Response:

```text
**Answer: AI**

**Confidence: 75%**

**Reasons:**

1. **Polished, generic closing and framing.** Lines like "Our neighborhood nonprofit believes everyone deserves a reliable ride" and "Stop by, say hello, and get back on the road with a bike that works the way it should" are smooth, upbeat marketing phrases. They feel templated and have no specific details, such as the organization's name, the church's name, or a real anecdote.

2. **Uniformly tidy structure and rhythm.** Nearly every sentence is a similar length and grammatically clean. The passage moves in a predictable order: problem, offer, logistics, reassurance, mission, call to action. It also uses stock phrasing like "free while supplies last," "just roll in whenever it suits you," and a rule-of-three list ("flats, brakes, and chains"). A real volunteer-written flyer would more likely include quirks, such as a specific address, a contact number, or a bit of informal or uneven wording.
```

Observation: New prompt. The passage is the body of the clean Prompt 8 response, its three paragraphs joined into one, with the bold title removed. The answer (AI, 75%) is correct, unlike the pre-fix run (Prompt 10, person at 60%). Reason 1 quotes the two lines the tool itself added to the blurb. Reason 2 says a real flyer would name the organization, the church, and an address, details the volunteer's prompt forbade the tool to invent. Both reasons are style.

## Prompt 18 (Section 3.3: AI or person? (the clean blurb, run 2))

```text
Was the passage below written by AI or by a person? Answer AI or person, give your confidence as a percentage, and give two reasons.

Passage: If your bike gets you to work or school, but a repair shop isn't in the budget, we can help. Every Saturday from 8 a.m. to 11 a.m., our volunteers run a free bike repair clinic in the church parking lot. Bring your bike and we will fix flats, brakes, and chains. Parts are free while supplies last. You don't need an appointment, so just roll in whenever it suits you during clinic hours. Our neighborhood nonprofit believes everyone deserves a reliable ride. Stop by, say hello, and get back on the road with a bike that works the way it should.
```

Response:

```text
**AI** — about 70% confidence.

**Reasons:**

1. **Polished, generic phrasing with a tidy marketing arc.** Lines like "believes everyone deserves a reliable ride" and "get back on the road with a bike that works the way it should" are smooth, upbeat, and broadly applicable. The passage moves from problem to offer to details to a warm sign-off, which is a typical pattern for AI-generated promotional copy.

2. **Missing concrete, local detail.** A person writing a real flyer would likely name the church, give an address, the nonprofit's name, a contact method, or quirks such as "bring your own tube" or "no e-bikes." The passage stays vague ("the church parking lot," "our neighborhood nonprofit") and includes an even rhythm of short, friendly sentences with no idiosyncrasies or typos.

The confidence isn't higher because community flyers are often written in exactly this plain, friendly style by people, and the text is short, so there's limited evidence either way.
```

Observation: Same prompt as Prompt 17, fresh conversation. AI, "about 70%." Reasons: a tidy marketing arc and missing local detail (no church name, address, or contact method). The em dash is in the captured response. Not shown; the chapter reports its verdict and confidence.

## Prompt 19 (Section 3.3: AI or person? (the clean blurb, run 3))

```text
Was the passage below written by AI or by a person? Answer AI or person, give your confidence as a percentage, and give two reasons.

Passage: If your bike gets you to work or school, but a repair shop isn't in the budget, we can help. Every Saturday from 8 a.m. to 11 a.m., our volunteers run a free bike repair clinic in the church parking lot. Bring your bike and we will fix flats, brakes, and chains. Parts are free while supplies last. You don't need an appointment, so just roll in whenever it suits you during clinic hours. Our neighborhood nonprofit believes everyone deserves a reliable ride. Stop by, say hello, and get back on the road with a bike that works the way it should.
```

Response:

```text
**Answer: AI**

**Confidence: 70%**

**Reasons:**

1. **Polished, generic flow with stock phrasing.** Lines like "everyone deserves a reliable ride," "Stop by, say hello, and get back on the road," and "works the way it should" are smooth, upbeat, and tidy but fairly interchangeable. A real volunteer-written flyer would more likely include specific details such as the organization's name, the church's name or street address, a contact number, or a quirky local touch.

2. **Overly balanced structure and tidy rhythm.** The passage moves in a clean sequence (who it helps, when and where, what's offered, no appointment needed, mission statement, call to action) with evenly sized sentences and almost no idiosyncrasies. Triplets ("flats, brakes, and chains") and the reassuring "just roll in whenever it suits you" feel like typical generated copy, with no rough edges, asides, or personality.

That said, community flyers are often written in exactly this template-like style, so a person could easily have written it, which is why my confidence isn't higher.
```

Observation: Same prompt as Prompt 17, fresh conversation. AI, 70%. Reasons: stock phrasing with no organization name, church name, address, or contact number, and an evenly balanced structure. Not shown; the chapter reports its verdict and confidence. Across the three runs the verdict held (AI) and the confidence moved (75, 70, 70), with no stated basis for any of the numbers.
