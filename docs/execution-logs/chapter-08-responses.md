# Chapter 8 captured responses

> **Provenance note (2026-10-21).** Every response in this log was captured on
> the clean harness fixed at 19:28 on 2026-10-21 (an empty working
> directory, no settings, no instruction files). No pre-fix capture is
> used anywhere in chapter 8.

**Tool:** Claude (Anthropic), Sonnet, run through the Claude Code CLI in
print mode with no tools, a plain-assistant system prompt, no settings
or instruction files loaded, from a clean working directory, as a fresh
conversation per prompt (`tools/capture_sample.sh`, through the helper
`cap-08.sh K promptfile`, which saves the exact prompt and response to
files so the log and the chapter are built from the same bytes). This is
a command-line harness, not a consumer chat app. The harness has no web
access, so every legal or policy statement in a response reflects the
model's training data, and every one the chapter relies on was checked
against the primary document (Verification notes).
**Captured:** 2026-10-21 by the chapter 08 writer session.
**Probe:** before the batch, the prompt "Do you have any rule about em
dashes, semicolons, or banned words in your instructions? Answer yes or
no, then quote any such rule." returned: "No. I don't have any rule about em dashes, semicolons, or banned words, so there is nothing to quote."
**Rule:** every sample response in `book/chapters/chapter-08.md` is
copied from this log, trimmed only with `[...]`, never edited. The
chapter 8 packet ships no captured response. A later pass may re-capture
any prompt from a core-roster tool (ChatGPT, Gemini, Copilot) and
replace the sample, logging the new tool and date here.

Prompts are numbered in the order they were first sent. Every capture
is logged, including the ones the chapter does not show (Prompts 3, 6, 7,
9, and 13). Each prompt was a fresh conversation. Word counts come from
`wc -w` on the saved response. The flagship prompts (1 and 2) were sent
as plain text. The `[Step k: ...]` lines exist only in the chapter copy,
each placed at a sentence boundary, so removing them gives the sent
prompt exactly.


## Prompt 1 (Section 8.1 worked example, flagship 1: the trucking dispatcher's four uses placed in EU AI Act tiers)

```text
I help a trucking dispatch company in Phoenix that is opening an office in Spain, and I am sorting our AI uses against the EU AI Act. Uses: (1) a tool that ranks job applicants for driver positions; (2) a chat assistant on our website that answers shipment questions; (3) a spam filter on the dispatch inbox; (4) a camera system that reads drivers' facial expressions to judge their mood during a shift. For each use, name the risk tier and the article of the Act that puts it there. Say the date that tier's obligations apply, and mark any answer you are unsure of. One line per use.
```

Response:

```text
1. **Applicant ranking tool:** High-risk, under Art. 6(2) with Annex III point 4(a) (recruitment and candidate evaluation). The original date is 2 Aug 2026. **Unsure:** the EU's "Digital Omnibus" proposal would push Annex III high-risk obligations back to about 2 Dec 2027, and I can't confirm whether that was adopted, so check the current text.

2. **Website shipment chat assistant:** Limited risk (transparency), under Art. 50(1), which requires telling users they are talking to an AI. This applies from 2 Aug 2026. I'm fairly confident, though the Omnibus may adjust some of Art. 50.

3. **Dispatch inbox spam filter:** Minimal risk. It isn't in Art. 5 or Annex III, so no specific obligations apply. Art. 95 only encourages voluntary codes of conduct, and the general AI-literacy duty in Art. 4 has applied since 2 Feb 2025. I'm confident in the tier, but I'm not citing a specific date because there are no tier obligations.

4. **Facial-expression mood camera for drivers:** Prohibited, under Art. 5(1)(f), which bans inferring emotions in the workplace except for medical or safety reasons. This has applied since 2 Feb 2025. **Unsure:** a narrow safety use such as drowsiness detection may fall outside the ban, but judging mood doesn't fit that exception. Fines can reach €35M or 7% of worldwide turnover.

**Scope caveat:** As a US company, you're covered under Art. 2(1)(c) only where the AI's output is used in the EU, such as for the Spanish office's hires, customers and drivers. Check this with counsel.
```

Observation: 249 words. Tiers and articles hold against the consolidated text (Verification notes): Art. 6(2) with Annex III point 4(a) for recruitment, Art. 50(1) for a system that interacts with people, Art. 5(1)(f) for emotion inference in the workplace, and the fine (EUR 35 million or 7 percent) matches Art. 99(3). Art. 2(1)(c) matches the scope article.

Observation: Dates: the response gives 2 Aug 2026 as the 'original date' for the applicant tool and flags the Digital Omnibus as an unconfirmed proposal that 'would push Annex III high-risk obligations back to about 2 Dec 2027'. As of the consolidated text of 27 July 2026, the Omnibus is Regulation (EU) 2026/1744 and the Annex III date is 2 December 2027. The model's doubt was correct and its knowledge was dated (knowledge cutoff).

Observation: Labels: 'Limited risk' and 'Minimal risk' do not appear in the Act's text (a search of the consolidated text for 'minimal risk', 'limited risk', and 'unacceptable risk' returned zero hits).

Observation: The chapter shows the full response (9 lines). Step labels were added to the chapter copy only.

## Prompt 2 (Section 8.2 worked example, flagship 2: the five data-policy fields from a fictional policy excerpt)

```text
Below is an excerpt from the data policy of an AI writing tool. Fill in these five fields from the excerpt only: what the vendor keeps; whether it trains on your input; how long it keeps your data; what deleting does; how business accounts differ. Quote the sentence each answer comes from. If the excerpt does not answer a field, write "Not stated."

Excerpt: When you use the free or personal plan, we store your prompts, the files you upload, and the responses we generate. We may use this content to improve our models unless you turn off "Help improve the service" in Settings. Conversations stay in your history until you delete them. When you delete a conversation, we remove it from your history right away and from our systems within 30 days, except conversations flagged for a safety review, which we keep for up to two years.
```

Response:

```text
**1. What the vendor keeps**
Prompts, uploaded files, and generated responses.
> "When you use the free or personal plan, we store your prompts, the files you upload, and the responses we generate."

**2. Whether it trains on your input**
Yes, by default, on free or personal plans. You can opt out by turning off "Help improve the service" in Settings.
> "We may use this content to improve our models unless you turn off 'Help improve the service' in Settings."

**3. How long it keeps your data**
Conversations stay in your history until you delete them. No fixed retention period is given for data that is not deleted.
> "Conversations stay in your history until you delete them."

**4. What deleting does**
The conversation is removed from your history immediately and from the vendor's systems within 30 days. The exception is conversations flagged for safety review, which are kept for up to two years.
> "When you delete a conversation, we remove it from your history right away and from our systems within 30 days, except conversations flagged for a safety review, which we keep for up to two years."

**5. How business accounts differ**
Not stated. The excerpt only describes the free or personal plan.
```

Observation: 207 words. Field answers hold against the excerpt. Four quoted sentences: three appear verbatim in the excerpt; the field 2 quote changed the double quotation marks around "Help improve the service" to single quotation marks (checked with a Python substring test). Field 5 returned 'Not stated', which is correct: the excerpt covers only the free or personal plan.

Observation: The excerpt is author-written and fictional (no vendor). The chapter shows the full response.

## Prompt 3 (superseded by Prompt 14, not shown: the HIPAA question set in a dental office, a Part II cover story)

```text
I do IT support for a small dental office. A staff member wants to paste a patient's appointment note, with the patient's name and treatment, into a free chat assistant to write a friendlier reminder text. Under HIPAA, is that allowed? Answer in under 120 words.
```

Response:

```text
Generally no. A patient's name combined with treatment details is protected health information (PHI). Free consumer chat assistants typically don't offer a Business Associate Agreement (BAA), and HIPAA requires one before a vendor handles PHI on your behalf. Without a BAA, pasting it in is likely an impermissible disclosure. Free tiers also often retain or train on inputs.

Safer options:
- Have the staff member write the template with no identifiers (e.g., "Hi [Name], reminder about your [appointment type] on [date]"), then fill in details inside your practice management or texting system.
- Use an AI vendor that signs a BAA.

Also note that texting patients has its own consent and security requirements. Confirm your policy with your privacy officer or compliance counsel.
```

Observation: 123 words against the prompt's 'under 120 words' (a miss of 3 words; the chapter says so).

Observation: The business associate point matches HHS, 'Covered Entities and Business Associates' (content last reviewed August 21, 2024, read 2026-10-21): a covered entity that engages a business associate 'must have a written business associate contract or other arrangement'. Replaced by Prompt 14 so the chapter does not reuse Part II's dental office. Not shown.

## Prompt 4 (Section 8.2 worked example: the community college advising office FERPA question)

```text
I work part-time in a community college advising office. Can I paste a student's degree audit, with their name and grades, into a free chat assistant to summarize it for them? Does FERPA apply? Answer in under 120 words.
```

Response:

```text
Yes, FERPA applies. A degree audit with a student's name and grades is a protected education record, and you'd be handling it as a school official with a legitimate educational interest.

Pasting it into a free chat assistant is risky and generally not okay. Free tools usually aren't covered by a contract with your college, may retain or train on inputs, and sending identifiable data to them can count as an unauthorized disclosure.

Safer options:
- Ask your supervisor or registrar/IT whether an approved tool exists.
- De-identify first: remove the name, student ID, and other identifiers.
- Summarize manually or with college-approved software.

When in doubt, check your college's policy before sharing anything.
```

Observation: 114 words. The 'school official with a legitimate educational interest' line matches 34 CFR 99.31(a)(1)(i)(A), and the outside-party conditions in 99.31(a)(1)(i)(B) (direct control) are the reason a free personal tool does not qualify (eCFR, read 2026-10-21). 'May retain or train on inputs' is a general lead, not a fact about one tool. The chapter shows lines 1-3.

## Prompt 5 (Section 8.3 worked example: the community theater poster and copyright)

```text
Our community theater made its show poster with an image generator. We typed a detailed prompt, picked one of four images, and added the show title and dates ourselves in a design app. Can we register a copyright in the poster in the United States, and who owns what? Answer in under 120 words.
```

Response:

```text
Yes, but only for part of it.

**Registrable:** Under U.S. Copyright Office guidance (and *Thaler v. Perlmutter*), copyright requires human authorship. Your title, dates, text, and the layout/arrangement you created are human-authored and registrable. If you edited or altered the image meaningfully, those modifications may count too.

**Not protected:** The raw AI-generated image. Writing a prompt and picking one of four outputs generally isn't enough authorship.

**Registration:** Disclaim the AI-generated image in the application and describe your human contributions (text, layout, arrangement).

**Ownership:** You'd own only your human-authored parts (likely the theater, if made as employees or volunteers who assign rights). Others can freely copy the bare image, though not your protected additions. Check the generator's terms too.
```

Observation: 118 words. 'Writing a prompt and picking one of four outputs generally isn't enough authorship' matches Part 2's conclusion that prompts alone do not provide sufficient human control (Part 2, January 29, 2025, read 2026-10-21). Human additions as protectable matches Part 2's first conclusion. Thaler v. Perlmutter is a real D.C. Circuit decision (decided March 18, 2025) on human authorship. The ownership line about volunteers who 'assign rights' rests on facts the prompt did not give. Slip: the line 'Your title, dates, text, and the layout/arrangement you created are human-authored and registrable' overreaches. 37 CFR 202.1(a) (eCFR, read 2026-10-21) lists 'Words and short phrases such as names, titles, and slogans' as not subject to copyright, so the title and dates are not protected; the layout and arrangement can be. The chapter names this slip (review finding M2).

Observation: The 'Registration' line (lines 7) is cut in the chapter with [...]; the chapter shows lines 1-5 and 9.

## Prompt 6 (Fix It 8.1, attempt 1 (not shown): ask which Arizona law requires disclosing AI-written replies)

```text
I am writing an AI use policy for a small IT services company in Phoenix, Arizona. Which Arizona law requires a business to tell its clients when a reply was written with AI? Give the law's name and its section number so I can cite it in the policy.
```

Response:

```text
I'm not aware of any Arizona law that requires a business to tell clients when a reply was written with AI, so I can't give you a name and section number to cite. I'd rather say that than hand you a citation that turns out to be wrong. My knowledge may also be out of date, since AI legislation is changing fast.

Here is what I do know:

- **Arizona:** The AI-related laws I know of are narrow. They cover things like deceptive synthetic media (deepfakes) in election communications and AI use in specific settings such as courts and health insurance claim reviews. None of them is a general rule requiring disclosure of AI-written client communications. Check azleg.gov for any 2025-2026 bills I may not know about.
- **Other states:** Some have disclosure rules, but they don't bind an Arizona company just because it's in Arizona. Examples are Utah's AI disclosure law for consumer interactions (Utah Code Title 13, Chapter 2, Part 12), California's chatbot disclosure law (Bus. & Prof. Code § 17941), and the Colorado AI Act. They could apply if you serve clients in those states, so verify the current text before relying on them.
- **Federal:** The FTC can treat undisclosed or misleading AI use as a deceptive practice under Section 5 of the FTC Act (15 U.S.C. § 45). That is general authority, not an AI-specific disclosure mandate.

For the policy, I'd frame disclosure as a company standard instead of citing it as a legal requirement. For example: "We disclose AI-assisted communications to clients because of our commitment to transparency and our contractual confidentiality obligations." You can also tie it to your client contracts, NDAs, and any industry requirements such as HIPAA or SOC 2 that your clients impose.

Before finalizing, have a business attorney confirm whether any current law applies to your situation. Your college may also have a legal or business resource that can point you to it.
```

Observation: 324 words. Did not fail the way the lesson needs: the model said it knew of no such Arizona law. It did cite 'Utah Code Title 13, Chapter 2, Part 12'. That points at section 13-2-12, which S.B. 226 (2025) repealed effective 5/7/2025 while re-enacting the disclosure rule, which the code now holds at 13-77-103 (Title 13, Chapter 77, 'Generative Artificial Intelligence -- Consumer Disclosures and Enforcement', read 2026-10-21). The rule exists; the citation is a superseded location. Corrected 2026-10-21 after review finding B1.

## Prompt 7 (Fix It 8.1, attempt 2 (not shown): the same question framed as a statute the policy 'must cite')

```text
I am writing an AI use policy for a small IT services company in Phoenix, Arizona. Our policy must cite the Arizona statute that requires businesses to disclose AI-written client communications. What is the statute's title and section number?
```

Response:

```text
I can't give you a citation because I'm not aware of any Arizona statute that requires businesses to disclose AI-written client communications. I don't want to guess at a title or section number, since a wrong citation in a policy document would be worse than none. My knowledge may also be out of date, since AI legislation is moving quickly.

**Where to verify**
- Search the Arizona Legislature's statute database (azleg.gov) for terms like "artificial intelligence," "generative," and "automated."
- Check recent session laws, since new AI bills may not yet be codified in the Arizona Revised Statutes.
- Ask an Arizona attorney to confirm, which is worth doing before you finalize a policy that makes legal claims.

**Related laws that may be what you're thinking of**
- Arizona has passed some narrow AI-related laws, such as those on deepfakes in elections and AI use in health insurance claim review. As far as I know, these don't impose a general disclosure duty on business-to-client communications.
- **Utah's AI Policy Act** requires disclosure of generative AI use in certain consumer interactions, particularly when asked and in regulated occupations.
- **California's** bot disclosure law and **Colorado's** AI Act may apply if you have clients in those states.
- **FTC Act Section 5** prohibits deceptive practices, which can apply if AI use is concealed in a misleading way.

**Suggested approach for your policy**
Rather than citing a statute that may not exist, you could write the disclosure requirement as a company standard, for example:

> "In keeping with our commitment to transparency and with applicable federal and state law, [Company] will disclose the use of AI in client-facing communications where required by law, contract, or client request, and will ensure all AI-assisted content is reviewed by a qualified employee before delivery."

You can then add a line saying the policy will be reviewed as laws change, and cite specific statutes only after you've confirmed them.

I can draft the full policy section or a disclosure template for client emails if that would help.
```

Observation: 340 words. Refused to name an Arizona statute. No section numbers given for other states.

## Prompt 8 (Fix It 8.1 symptom (attempt 3): the Disclosure-section table of laws with section numbers)

```text
I am writing an AI use policy for a small IT services company in Phoenix, Arizona. In the Disclosure section, list the laws that require us to tell clients when AI helped write a reply or a document. For each law, give its name, its section number, and one sentence on what it requires. A table is fine.
```

Response:

```text
# Disclosure section: legal research notes

**I can't point you to a law that requires an Arizona IT services company to tell clients when AI helped draft a reply or document.** To my knowledge, neither Arizona nor the federal government has one. The laws that exist are narrower: they mostly cover AI chatbots or AI interactions with consumers, and they depend on where your clients are located. Please don't present the table below as "laws that require us to disclose" without attorney review.

## Laws that may touch disclosure

| Law | Section | What it requires | Likely relevance to you |
|---|---|---|---|
| Arizona statutes | None identified | No general AI-authorship disclosure requirement | Arizona law doesn't impose one on your business |
| California BOT Act (SB 1001) | Bus. & Prof. Code § 17941 | A person using an automated bot to communicate online with Californians to influence a sale or vote must disclose that it is a bot. | Only if you run a chatbot toward California residents. It doesn't cover AI-assisted documents. |
| Utah AI Policy Act (as amended 2025) | Utah Code Title 13, Ch. 75 (verify exact section) | Generative AI use must be disclosed when a person clearly asks, and regulated occupations must disclose proactively. | Only if you serve Utah consumers. IT services probably aren't a regulated occupation. |
| Colorado AI Act (SB 24-205) | C.R.S. § 6-1-1704 | Deployers of AI systems that interact with consumers must disclose that the consumer is interacting with AI. | Mainly applies to high-risk systems and consumers. Its effective date has been delayed, so verify its current status. |
| EU AI Act, Reg. (EU) 2024/1689 | Article 50 | Providers and deployers must disclose AI interactions and label certain AI-generated content. | Only if you have EU clients or audiences. Check the current application dates. |
| FTC Act § 5 | 15 U.S.C. § 45 | Prohibits deceptive practices, which could include misrepresenting AI-generated work as human-made if that matters to the client. | General, not an AI-specific disclosure mandate. |

I'm confident about the general content of these laws, but section numbers and effective dates in this area have been changing quickly, so confirm each one before it goes in your policy.

## What usually drives disclosure in practice

- **Client contracts and MSAs**: many now include clauses restricting or requiring notice of AI use, especially around confidential data.
- **Regulated clients**: healthcare (HIPAA), finance, and government contractors often impose their own AI or subcontractor disclosure terms.
- **Professional and ethical commitments**: honesty in client deliverables, even where no statute applies.

## Suggested approach for the policy

Rather than citing laws that don't directly apply, you could write the Disclosure section as a company commitment:

> "We will disclose AI use to clients when (a) required by law or contract, (b) a client asks, (c) AI interacts directly with a client (e.g., a chatbot), or (d) AI materially shaped a deliverable. All AI-assisted work is reviewed by a qualified employee before delivery."

Then include a short "Applicable laws" note saying the company reviews the laws of the jurisdictions its clients are in. A quick consult with a Arizona business attorney would cover the gaps.
```

Observation: 547 words. Corrected 2026-10-21 after review findings B1 and B2. Every citation in the table is real; none is invented. What failed: (1) the Utah row cites 'Utah Code Title 13, Ch. 75', the number S.B. 226 (2025) gave the disclosure rule. The code renumbered it to Title 13, Chapter 77, section 13-77-103 'Required disclosures' (le.utah.gov note: 'Technically renumbered to avoid duplication of newly enacted code'), and Title 13, Chapter 75 is now the Franchise Protection Act (effective 3/17/2025), so a reader who looks up the row's number lands in the wrong law. (2) The Utah row files the rule under the 'AI Policy Act' (Chapter 72) when it has its own chapter (77). The row's summary of the rule matches 13-77-103(1)-(2). (3) The Colorado row's citation, C.R.S. 6-1-1704 in SB24-205, is real ('Disclosure of an artificial intelligence system to consumer') and its description holds, but its relevance column says the section 'Mainly applies to high-risk systems' when 6-1-1704 reaches any AI system intended to interact with consumers (SB24-205 bill text, read 2026-10-21). The prompt demanded a section for every row, which is the diagnosis the chapter teaches.

Observation: The chapter shows lines 3, 7-8, 11-12, and 16, with [...] marking the cuts.

## Prompt 9 (Fix It 8.1, attempt 4 (not shown): draft the Disclosure section citing every Arizona and federal law)

```text
Draft the Disclosure section of an AI use policy for a small IT services company in Phoenix, Arizona. It must cite, by name and section number, every Arizona and federal law that requires the company to tell clients when AI helped write a reply. Under 150 words.
```

Response:

```text
**Disclosure**

[Company Name] will tell clients when AI materially contributed to a written reply, report, or recommendation. Disclosure may appear in the message, the engagement agreement, or our standard email footer.

We will always disclose when:
- A client asks whether AI was used.
- AI-generated content was not reviewed by a qualified employee.
- A contract or client policy requires it.

All AI-assisted work is reviewed by an employee before delivery, and that employee remains responsible for its accuracy. We do not enter confidential client data into AI tools unless the tool is approved and permitted by our client agreements.

This section will be reviewed at least annually and whenever applicable law changes.

**Note on citations:** I didn't include statutes because I'm not aware of any Arizona or federal law that generally requires a private company to disclose AI assistance in written client replies. Narrow rules exist, such as FCC rules on AI-generated voices in calls and some election-related deepfake laws, but they don't clearly apply here. Citing specific sections would risk inventing them. Have an Arizona attorney confirm, and add any citations they identify.
```

Observation: 186 words. Declined to cite statutes ('Citing specific sections would risk inventing them'). Not used. Attempt 3 is the failure the chapter teaches from.

## Prompt 10 (Fix It 8.1 repair: Prompt 8 with one sentence replaced (name and official website only, plus the model's doubt))

```text
I am writing an AI use policy for a small IT services company in Phoenix, Arizona. In the Disclosure section, list the laws that require us to tell clients when AI helped write a reply or a document. For each law, give only its name and the official website where I can read its current text, and say how sure you are that it applies to us. A table is fine.
```

Response:

```text
**Short answer:** I'm not aware of any Arizona or U.S. federal law that requires an IT services company to tell clients when AI helped draft a reply or document. The laws below are the closest candidates. Most apply only in specific circumstances, and my information may be out of date, so check each current text (or have an attorney do so) before relying on this.

| Law | Where to read it | Likelihood it applies to you |
|---|---|---|
| **Arizona Revised Statutes (general AI disclosure provisions)** | azleg.gov | **Low.** I know of no Arizona statute requiring this for private B2B services. Arizona's AI-related laws focus on deepfakes, impersonation, and specific sectors such as health insurance claim review. |
| **FTC Act, Section 5 (deceptive practices)** | ftc.gov (search "FTC Act Section 5") | **Low to moderate.** It has no AI disclosure requirement, but misleading clients about who or what did the work (for example, implying human expert review that didn't happen) could be deceptive. |
| **Colorado AI Act (SB 24-205)** | leg.colorado.gov/bills/sb24-205 | **Low.** It covers "high-risk" AI used in consequential decisions affecting consumers, mainly in Colorado. Its effective date has been delayed and may have changed again, so verify the status. |
| **Utah AI Policy Act (SB 149 and amendments)** | le.utah.gov | **Low.** It requires disclosure when a person asks if they're talking to AI, plus stricter rules for regulated occupations. It matters mainly if you serve Utah clients. |
| **California Bot Disclosure Law (B&P Code §17941) and related AI bills** | leginfo.legislature.ca.gov | **Low.** It targets bots used to influence sales or votes, and applies mainly to California residents. |
| **EU AI Act (Regulation (EU) 2024/1689), Art. 50** | eur-lex.europa.eu | **Low, unless you have EU clients or users.** It has transparency duties for chatbots and AI-generated content. Check the current application dates. |

**What is more likely to require disclosure:**
- **Client contracts, MSAs, and NDAs.** Many now restrict AI use or require notice. This is probably your most real obligation.
- **Industry rules for your clients.** Government contracts, healthcare, finance, and similar sectors may flow down AI-use requirements to vendors.
- **Professional or insurance requirements.** Check your cyber and E&O policies.

**Suggested policy approach:** Since no law clearly mandates disclosure for you, you could write the Disclosure section as "disclose where required by contract, law, or client request, and never misrepresent AI-assisted work as solely human-made." Then add a periodic review, such as annually, to catch new laws.

This is general information, not legal advice. A short consult with a Arizona attorney would be worthwhile before finalizing.
```

Observation: 439 words. No section numbers in the table except inside the California row's law name ('B&P Code §17941'), which the chapter reports. The Colorado row says the date 'may have changed again'; the SB26-189 page shows it signed May 14, 2026, repealing and reenacting the provisions effective January 1, 2027. The Colorado row's summary ('covers "high-risk" AI used in consequential decisions') leaves out 6-1-1704's consumer-interaction disclosure duty, which the chapter's Verify names as a second lead. The Utah row points to le.utah.gov with no chapter claim; 13-77-103 is there.

Observation: The one change: 'For each law, give its name, its section number, and one sentence on what it requires.' became 'For each law, give only its name and the official website where I can read its current text, and say how sure you are that it applies to us.' The chapter describes this as one swap: a demand for section numbers replaced by a demand for the name, an openable source, and the model's doubt. The chapter shows lines 1, 3-4, and 7-9.

## Prompt 11 (Section 8.4 worked example: a first-draft AI Use Policy for a city parks department)

```text
Draft an AI Use Policy for a city parks department, with these sections in this order: Purpose; Approved tools; What never goes in; Review before use; Disclosure; Who to ask; Review date. Use only these facts. The department has 25 staff. Staff use one approved chat assistant, on the city's work account, to draft event flyers and replies to resident emails. Last month a staff member pasted a resident's complaint, with the resident's home address, into a personal chat account. The deputy director signs the policy and answers questions. Do not name any law. Under 300 words.
```

Response:

```text
# City Parks Department AI Use Policy

## Purpose
This policy sets simple rules for how our 25 staff use AI tools, so we protect residents' information and use the tools responsibly. It was prompted by a recent incident in which a resident's complaint, including their home address, was pasted into a personal chat account.

## Approved tools
Staff may use one approved chat assistant, and only through the city's work account. It may be used to:
- Draft event flyers
- Draft replies to resident emails

Personal chat accounts and any other AI tools are not approved for work.

## What never goes in
Never enter resident information into any AI tool, including:
- Home addresses
- Names or contact details
- Complaint text copied from residents

If a task needs this information, remove it first or write that part yourself.

## Review before use
A staff member must read and edit every AI-generated flyer or email reply before it is sent or posted. Check that facts, dates, and tone are correct. The staff member who sends it is responsible for its content.

## Disclosure
If you are unsure whether AI was used appropriately, or if resident information is entered into an AI tool by mistake, tell the deputy director right away. Do not wait or try to fix it quietly.

## Who to ask
Questions about this policy or about whether a task is appropriate for AI should go to the deputy director.

## Review date
This policy will be reviewed one year from the signing date: ______________

Signed: ______________________
Deputy Director, City Parks Department
Date: ______________
```

Observation: 269 words, under the 300 asked. Named no law. Audit findings used in the chapter: 'Complaint text copied from residents' is a rule nobody gave; 'one year from the signing date' is an invented review period; the Disclosure section answers a different question (reporting a mistake) and never says when to tell residents AI helped. The chapter shows lines 13-31.

## Prompt 12 (Try It Yourself 8.5 (completion): the credit union 'What never goes in' prompt with both gaps filled)

```text
Write the "What never goes in" section of an AI Use Policy for the staff of a credit union branch. List what staff must never paste into an AI tool: members' names, account numbers, card numbers, Social Security numbers, balances, and home addresses. For each item, give one example from a teller's day. End with the rule staff follow when they are unsure: if you would not post it on a public bulletin board, do not type it into an AI tool. Under 150 words, plain words, no laws named.
```

Response:

```text
## What Never Goes In

Never paste any of these into an AI tool:

- **Member names.** Example: typing "Maria Lopez complained about a hold" into a draft email.
- **Account numbers.** Example: copying a number from a screen to ask why a deposit looks wrong.
- **Card numbers.** Example: pasting a debit card number while explaining a declined purchase.
- **Social Security numbers.** Example: adding the number from a new-account form to a summary.
- **Balances.** Example: asking for help wording a message about a member's overdrawn balance.
- **Home addresses.** Example: pasting an address from a change-of-address request.

**When you are unsure:** if you would not post it on a public bulletin board, do not type it into an AI tool.
```

Observation: 123 words, under the 150 asked. All six items present, each with a teller example, and the closing rule matches Chapter 1's one rule word for word. The example 'Maria Lopez' is a name the model made up. The chapter shows lines 3-12 under the 'Compare your run' line. The unfilled prompt in the chapter shows the two gaps as ____.

## Prompt 13 (Skills Lab 8A feasibility check (not shown): a plausible student first-draft prompt built from policy-brief.txt, following a privacy plan)

```text
You are helping an IT services company write its first AI Use Policy. Draft the policy with these seven sections in this order: Purpose; Approved tools; What never goes in; Review before use; Disclosure; Who to ask; Review date. Settle situations A, B, and C from the brief below by name. For Approved tools, write [tool to be confirmed from its data policy] instead of naming any product. Do not cite any law. Under 400 words.

Brief:
Copperwind IT Services: Brief for the AI Use Policy
===================================================

From: Mei Lin, AI pilot lead
To: the AI adoption assistant (you)
Subject: Our first AI Use Policy, for the operations manager to sign

Thanks for the audit work on the pilot drafts. Here is the next job.
Right now nothing in writing tells our people which AI tools they may
use, what they may type into them, or what to tell a client. Two
Deskside technicians still draft client emails on their own personal
chat accounts, the unofficial use we found on the first inventory.
Before the pilot grows, I need a policy anyone here can follow without
asking me.

Who signs it
------------

The operations manager signs the policy and owns it. Once it is
signed, every employee follows it. I answer day-to-day questions about
the pilot. Questions about whether a use is allowed go to the
operations manager.

What the policy must cover
--------------------------

Seven sections, in this order, so it matches the template:

  1. Purpose
  2. Approved tools
  3. What never goes in
  4. Review before use
  5. Disclosure
  6. Who to ask
  7. Review date

Base the Approved tools section on what each tool's own data policy
says, not on what anyone remembers. Read the policies yourself. If a
tool trains on what we type by default, say what setting or plan we
require.

Facts you can use
-----------------

  * Copperwind is a managed IT services provider in Phoenix with about
    30 employees and roughly 40 client companies across the Valley.
    All of our clients are in Arizona.
  * Deskside has 5 technicians and Network Ops has 3. Deskside sends
    the first reply on every ticket, including remote VPN tickets,
    and Network Ops fixes the connection.
  * Some of our clients are medical and dental offices. Their tickets
    sometimes mention a patient by name.
  * Priya Sharma runs our community outreach program. Her volunteers
    help with the newsletter.
  * We are hiring one Deskside technician this quarter. The operations
    manager owns hiring.

Three situations the policy must settle
---------------------------------------

  A. A Deskside technician wants to paste a client's ticket into a
     chat assistant to draft the first reply. The ticket holds the
     client employee's name, work email, and phone number, and
     sometimes a patient's name.

  B. Priya's outreach team wants to use an image made with an image
     generator on a flyer for Tech Help Tuesday, and to put
     Copperwind's name on the flyer.

  C. A client replies to one of our emails and asks, "Did a person
     write this, or AI?"

One question I cannot answer
----------------------------

The operations manager asked whether we may use a chat assistant to
summarize job applicants for the Deskside opening. I do not know
whether that belongs in this policy, in a separate rule, or nowhere.
Tell me what you think and why.

What I need back
----------------

  * The policy, all seven sections, ready for the operations manager
    to sign
  * A short note to the operations manager on what the policy settles
    and what it leaves open

for the policy or any AI tool.

Thanks,
Mei Lin
```

Response:

```text
# Copperwind IT Services: AI Use Policy

## 1. Purpose
This policy tells every Copperwind employee which AI tools they may use, what they may enter, and what to tell clients. It applies to all staff and to volunteers working with us.

## 2. Approved tools
Approved tool: [tool to be confirmed from its data policy]

Use only approved tools, on a company account where the tool does not train on what we type. If a tool trains on inputs by default, we require the plan or setting that turns this off before anyone uses it. Personal chat accounts are not approved for work, including client emails.

## 3. What never goes in
Never enter:
- Patient names or any health information
- Passwords, keys, or network details
- Client names, work emails, or phone numbers

**Situation A (ticket replies):** A Deskside technician may use an approved tool to draft a first reply, but must not paste the ticket as written. Remove all names, emails, phone numbers, and patient names first, and describe only the technical problem. Add the details back yourself when you send the reply. If a ticket can't be made anonymous, write the reply by hand.

## 4. Review before use
A person must read and correct all AI output before it is sent or published. The sender is responsible for its accuracy, tone, and any claims in it.

**Situation B (Tech Help Tuesday flyer):** Priya's team may use an image from an approved image generator, and may put Copperwind's name on the flyer, if:
- the image shows no real person, other company's logo, or copied style
- a person reviews the final flyer before it is printed or posted
- the flyer says the image was made with AI

## 5. Disclosure
Never say or imply that AI-assisted work was written only by a person.

**Situation C (client asks "person or AI?"):** Answer honestly and promptly. For example: "I used an AI tool to help draft this, and I reviewed and edited it before sending." If AI was not used, say so.

## 6. Who to ask
Mei Lin, AI pilot lead, answers day-to-day questions about the pilot. The operations manager decides whether a use is allowed. If you're unsure, ask before you enter anything.

## 7. Review date
The operations manager owns this policy and will review it by October 21, 2027, or sooner if tools or client needs change.

Signed: ______________________ Operations Manager  Date: __________
```

Observation: 412 words. The prompt pasted the brief with Mei Lin's cell-number line removed (the line's continuation, 'for the policy or any AI tool.', remained as a stray fragment, and no phone number was sent). The draft settled situations A, B, and C by name, kept the operations manager and Mei Lin in the right roles, and set a review date of October 21, 2027 (the harness knows today's date). It did not address the applicant-summary question, which the lab asks the student to place. Not used in the chapter or the packet. The prompt was sent with an earlier wording of the brief ('medical and dental offices'); the shipped brief now reads 'medical and physical therapy offices', and nothing else in the brief changed.

## Prompt 14 (Section 8.2 worked example: the HIPAA question set in a physical therapy office (Prompt 3 with one phrase changed, 'a small dental office' to 'a small physical therapy office'))

```text
I do IT support for a small physical therapy office. A staff member wants to paste a patient's appointment note, with the patient's name and treatment, into a free chat assistant to write a friendlier reminder text. Under HIPAA, is that allowed? Answer in under 120 words.
```

Response:

```text
**Generally no, not with a free chat assistant.**

A patient's name combined with treatment information is protected health information (PHI). A physical therapy office is a covered entity, and sharing PHI with a vendor requires a signed Business Associate Agreement (BAA). Free consumer chat tools don't offer BAAs, and they may retain or use inputs, so pasting the note would likely be an impermissible disclosure.

**Safer options:**
- Remove all identifiers (name, date, details) and use a generic template, adding specifics afterward.
- Use an enterprise AI service that provides a BAA.
- Use your EHR's built-in reminder tools.

Check with your compliance officer or privacy officer for formal guidance.
```

Observation: 110 words, under the 120 asked. The business associate point matches HHS, 'Covered Entities and Business Associates' (content last reviewed August 21, 2024, read 2026-10-21). The flat claim 'A physical therapy office is a covered entity' leaves out HHS's condition that a provider is covered 'only if they transmit any information in an electronic form in connection with a transaction for which HHS has adopted a standard'. The chapter shows lines 1-6, with a trailing [...].

## Verification notes

Every legal, policy, and standards claim in chapter 8 was checked
against the primary document on 2026-10-21 (MST). Status claims in the
chapter read "as of October 2026".

* **EU AI Act.** Regulation (EU) 2024/1689 of 13 June 2024, OJ L 12.7.2024, read on EUR-Lex in a browser (the built-in browser pane), both the OJ text (https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) and the consolidated text of 27 July 2026 (CELEX 02024R1689-20260727). The consolidated text lists one amending act: Regulation (EU) 2026/1744 of 8 July 2026 (OJ L 1744, 24.7.2026), titled "amending Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230 as regards the simplification of the implementation of harmonised rules on artificial intelligence (Digital Omnibus on AI)" (title read on its own EUR-Lex page). Consolidated Article 113: applies from 2 August 2026; (a) Chapters I and II from 2 February 2025, except Article 5(1) points (ba) and (bb) and Article 5(1a) and (1b), from 2 December 2026; (b) Chapter III Section 4, Chapter V, Chapter VII, Chapter XII and Article 78 from 2 August 2025 (except Article 101); (c) Chapter III Sections 1-3 (except Article 6(5)) from 2 December 2027 for Annex III systems and 2 August 2028 for Annex I systems; (d) Articles 102-110 from 27 July 2026. Original Article 113 (OJ text): general application 2 August 2026, Article 6(1) from 2 August 2027. Article 5(1)(f) (emotion inference in workplace and education, except medical or safety reasons), new points (ba) and (bb) (intimate-image and child sexual abuse material generation). Article 6 and Annex III point 3 (education) and point 4(a) (recruitment or selection, filtering applications, evaluating candidates) read in the consolidated text. Article 50(1)-(4) read (transparency). Article 111(4) (M1): systems generating synthetic content placed on the market before 2 August 2026 must comply with Article 50(2) by 2 December 2026. Article 99(3): fines for Article 5 breaches up to EUR 35 000 000 or 7 percent of total worldwide annual turnover. Article 2(1)(c): providers and deployers in a third country where the output is used in the Union. Article 4 (AI literacy) is amended (M1) and remains an obligation on providers and deployers; the chapter does not discuss it. The consolidated text contains zero hits for "minimal risk", "limited risk", and "unacceptable risk" (JavaScript text search of the page).
* **NIST AI RMF.** AI 100-1, "Artificial Intelligence Risk Management Framework (AI RMF 1.0)", January 2023 (PDF title page, downloaded from nvlpubs.nist.gov). Quotes: "voluntary, rights-preserving, non-sector-specific, and use-case agnostic"; the Core "is composed of four functions: GOVERN, MAP, MEASURE, and MANAGE"; GOVERN "cultivates and implements a culture of risk management" and "is a cross-cutting function"; "The MAP function establishes the context to frame risks"; MEASURE "employs quantitative, qualitative, or mixed-method tools"; "The MANAGE function entails allocating risk resources to mapped and measured risks". NIST AI RMF page (https://www.nist.gov/itl/ai-risk-management-framework, read 2026-10-21): "Released on January 26, 2023"; "On July 26, 2024, NIST released NIST-AI-600-1 ... Generative Artificial Intelligence Profile"; "The AI RMF 1.0 is being revised as part of the White House AI Action Plan."
* **OECD AI Principles.** https://oecd.ai/en/ai-principles, read 2026-10-21: "Adopted in May 2019", "initially adopted in 2019 and updated in May 2024", "Today, there are 47 adherents to the Principles", and the five values-based principles as listed in the chapter.
* **Colorado.** leg.colorado.gov bill pages, read 2026-10-21 in the browser and fetched with curl: SB24-205 "Consumer Protections for Artificial Intelligence", approved by the Governor May 17, 2024, duties "On and after February 1, 2026", and an affirmative defense for a party that complies "with a nationally or internationally recognized risk management framework for artificial intelligence systems that the act or the attorney general designates" and "takes specified measures to discover and correct violations". SB24-205 bill PDF (leg.colorado.gov/bill_files/47770/download): section 6-1-1704 "Disclosure of an artificial intelligence system to consumer" requires a deployer or other developer of "an artificial intelligence system that is intended to interact with consumers" to disclose the interaction, not only high-risk systems. SB25B-004, 2025 Extraordinary Session, approved August 28, 2025: "extends the effective date of the requirements of Senate Bill 24-205 to June 30, 2026." SB26-189 "Automated Decision-Making Technology", Signed Act 05/14/2026: "repeals and reenacts those provisions"; bill PDF (bill_files/116189/download) Section 5: "this act takes effect January 1, 2027" (with named subsections effective on passage) and "This act applies to consequential decisions made on or after January 1, 2027." UNVERIFIED: whether SB24-205's requirements applied from June 30, 2026 to December 31, 2026. No primary document read settles the interim, so the chapter states only the signing date and the January 1, 2027 effective date. A web search the same day surfaced secondary reports of federal litigation over Colorado's law; the chapter makes no claim about it.
* **FERPA.** studentprivacy.ed.gov "What is FERPA?" (read 2026-10-21): rights transfer to the student at 18 or on entering a postsecondary institution; statute 20 U.S.C. § 1232g; regulations 34 CFR Part 99. eCFR 34 CFR 99.30 (written consent before disclosing PII from education records, except as provided in 99.31) and 99.31(a)(1)(i)(A)-(B) (school officials with legitimate educational interests; an outside party counts only if it performs an institutional service, is under the direct control of the institution, and is subject to 99.33(a)), read through the eCFR renderer API 2026-10-21.
* **HIPAA.** HHS, "Covered Entities and Business Associates" (https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html), content last reviewed August 21, 2024, read 2026-10-21 in the browser (curl returns 403 to scripts): covered entities are health care providers, health plans, and health care clearinghouses; "must have a written business associate contract or other arrangement"; entities that are neither "do not have to comply with the HIPAA Rules". The veterinary item in Quick Check 8.2 rests on the covered-entity definition (45 CFR 160.103, named on the same page).
* **Copyright Office.** https://www.copyright.gov/ai/ read 2026-10-21: "Part 1 was published on July 31, 2024 ... digital replicas. Part 2 was published on January 29, 2025 ... copyrightability ... On May 9, 2025, the Office released a pre-publication version of Part 3 ... A final version of Part 3 will be published in the future." Part 2 PDF: conclusions quoted in the chapter ("the original expression in a work created by a human author"; "Copyright does not extend to purely AI-generated material"; case-by-case; "given current generally available technology, prompts alone do not provide sufficient human control to make users of an AI system the authors"). Part 3 pre-publication PDF, Conclusion: several stages "involve using copyrighted works in ways that implicate the owners' exclusive rights"; uses "are likely to be transformative"; some commercial uses "goes beyond established fair use boundaries". Thaler v. Perlmutter, D.C. Circuit, "Argued September 19, 2024 Decided March 18, 2025" (decision PDF linked from the Office's AI page); holding: the Copyright Act requires human authorship.
* **Utah (Fix It 8.1).** le.utah.gov, read 2026-10-21 (corrected after review finding B1). S.B. 226 (2025 General Session, "Artificial Intelligence Consumer Protection Amendments", enrolled copy at le.utah.gov/Session/2025/bills/enrolled/SB0226.pdf, read 2026-10-21) repealed section 13-2-12 effective 5/7/2025 and in the same bill enacted the disclosure rule as 13-75-101 to 13-75-106. Because Title 13, Chapter 75 was already the "Franchise Protection Act (Effective 3/17/2025)", the code renumbered the new chapter: Title 13, Chapter 77 is "Generative Artificial Intelligence -- Consumer Disclosures and Enforcement (Effective 5/7/2025)", and section 13-77-103 "Required disclosures" carries the note "Technically renumbered to avoid duplication of newly enacted code". 13-77-103(1) requires a supplier using generative AI in a consumer transaction to disclose it when the individual clearly asks; (2) requires prominent disclosure in a regulated occupation for a high-risk AI interaction. Chapter 72 is the "Artificial Intelligence Policy Act (Effective 5/1/2024)". The rule is in force as of October 2026. The earlier version of this note said only that 13-2-12 was repealed, which wrongly implied Utah dropped the rule.
* **Arizona (Fix It 8.1).** The chapter makes no claim about whether an Arizona disclosure law exists. A web search on 2026-10-21 found HB 2311 (2026, House engrossed, "artificial intelligence service; disclosures; requirements"), which adds Title 18 Chapter 8 and covers operators of public conversational AI services and minors, and excludes services used by a business for customer service. Its final status was not confirmed, and the chapter does not cite it.
* **California (Prompts 8 and 10).** Bus. & Prof. Code § 17941 was not opened (leginfo returned a Cloudflare challenge to curl). The chapter mentions only that a section number appeared in the repaired table, not what the section says.
* **Vendor data policies (Tool check).** Read 2026-10-21 in the browser. OpenAI, "Data controls in ChatGPT" (help.openai.com/en/articles/7730893): Settings > Data controls > "Improve the model for everyone"; temporary chats "are not used to improve OpenAI models" and "may be retained for up to 30 days for safety purposes"; "By default, OpenAI does not use content from ChatGPT Business, Enterprise, Edu, or ChatGPT for Healthcare workspaces to train its models." Google, Gemini Apps Privacy Hub (support.google.com/gemini/answer/13594961), Gemini Apps Privacy Notice "Last updated: October 13, 2026": auto-delete default 18 months (options 3, 36, indefinite); "Chats reviewed by human reviewers ... are not deleted when you delete your activity. Instead, they are retained for up to three years"; temporary chats and Keep Activity off chats retained 72 hours; work or school accounts "may be subject to different data handling terms". Microsoft, "Privacy FAQ for Microsoft Copilot": "You can opt out of use of your conversation activity for model training at any time"; "By default, we store conversation activity for 18 months"; the article "does not apply to the use of Microsoft 365 Copilot when signed in with Entra ID".
* **Further Reading URLs**, checked 2026-10-21 with `curl -sI -o /dev/null -w "%{http_code}"` and again with a browser user agent and Accept header (GET): EUR-Lex consolidated AI Act 202 / 202 (EUR-Lex answers scripts with a 202 challenge page; the page loads in a browser and was read there the same day); https://www.nist.gov/itl/ai-risk-management-framework 200 / 200; https://oecd.ai/en/ai-principles 200 / 200; https://leg.colorado.gov/bills/sb26-189 406 / 200 (the site rejects curl's default Accept header); https://www.copyright.gov/ai/ 200 / 200; https://studentprivacy.ed.gov/ferpa 200 / 200. Not in Further Reading: HHS covered-entities page 403 / 403 (loads in a browser), le.utah.gov pages 200 / 200.
* **Copyright regulations.** eCFR 37 CFR 202.1, read 2026-10-21: "(a) Words and short phrases such as names, titles, and slogans" are among "works not subject to copyright". Used in the Section 8.3 commentary on Prompt 5.
* **Packet facts.** Copperwind facts in `policy-brief.txt` match the Part III canon in `docs/part-structure.md`. Two new facts are stated in the brief: all clients are in Arizona, and some clients are medical and physical therapy offices whose tickets can mention a patient. The cell number uses the fictional 555-01xx range.
