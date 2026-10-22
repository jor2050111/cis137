# Chapter 8: Governance, Privacy, and Content Ownership

A leasing agent at an apartment management office wants a late-rent notice to sound kinder. She pastes the notice, with the tenant's name and unit number, into a free chat assistant on her personal account. Did she break a law? Her company's rules? The tool's own terms? Or something nobody wrote down, a duty to the tenant who never agreed to it? Those are four different questions, and each one has a different answer and a different person who enforces it.

Chapter 3 gave you five ethical use principles, and Chapter 1 gave you one rule about what never goes into a tool. This chapter adds the rules other people write about artificial intelligence (AI): legislatures, regulators, standards bodies, and the vendors whose tools you use. You will read the primary documents yourself, including the EU AI Act, the NIST AI Risk Management Framework, and a vendor's data policy. Then you will write a policy that other people can follow. These rules change fast. One of the biggest changed in July 2026, so every status in this chapter carries the document it came from and the date it was read.

At Copperwind, the job is concrete. Two Deskside technicians still draft client emails on personal chat accounts, and nothing in writing says what anyone may type into a tool. Mei Lin has asked you to draft the Copperwind AI Use Policy for the operations manager to sign. The Skills Lab hands you her brief.

## Module Overview 🧭

* **Estimated time:** 4-5 hours
* **Prerequisites:** Chapters 1 and 3 (the one rule, the five ethical use principles, disclosure, and the privacy check), Chapter 2 (knowledge cutoff), and Chapters 4-6 (the five parts of a prompt and checkable criteria)
* **Deliverables:** Skills Lab 8A deliverable (the Copperwind AI Use Policy and a note to the operations manager), Quick Checks

## Learning Objectives 🎯

By the end of this chapter, you will be able to:

* **8.1 (Analyze):** Categorize a rule about an AI use as law, policy, guidance, or ethics, and place an AI use in the EU AI Act's risk tiers and NIST AI RMF functions (Section 8.1)
* **8.2 (Analyze):** Examine a vendor's data policy and terms of use to determine what it keeps, trains on, and deletes, and relate FERPA, HIPAA, and copyright to a case (Sections 8.2-8.3)
* **8.3 (Evaluate):** Recommend an AI Use Policy that the people in an organization can follow, and justify each of its rules by the kind of rule behind it (Section 8.4)

### This chapter aligns with the following Course Learning Outcomes

* **CLO 5 (Apply):** Apply ethical guidelines to make responsible decisions when using AI tools.
* **CLO 4 (Analyze):** Analyze the current state of AI and its impact on society, including strengths and weaknesses.

---

## 8.1 Four Kinds of Rules and the Global Map

People say "the AI rules" about four different things, and mixing them up causes real mistakes. A manager who thinks a framework is a law spends money on the wrong problem. A technician who thinks a company policy is only advice ignores it. **Governance** is the system of rules, roles, and checks that decides how AI may be used and who answers for the result. Every governance question starts by asking which kind of rule you are looking at.

The **four kinds of rules** are law, policy, guidance, and ethics. Law is binding, with penalties, and a legislature or a regulator makes it. Policy is an organization's own rules for its people. Guidance is a framework or standard an organization chooses to follow, such as the NIST AI RMF. Ethics is the set of principles behind the other three.

| Kind | Who makes it | Who must follow it | What happens if it is broken | One example |
| --- | --- | --- | --- | --- |
| Law | A legislature or a regulator | Everyone it covers | Penalties, such as fines or court orders | The EU AI Act bans emotion-reading systems in workplaces and schools, with fines for banned practices of up to 35 million euros or 7 percent of worldwide yearly turnover (Article 99) |
| Policy | An organization | Its own people | Discipline, lost access, or a lost job | A credit union branch lets staff use one approved chat assistant, on a work account only |
| Guidance | A standards body, an agency, or an international group | Whoever chooses to adopt it | Nothing by itself, unless a contract or a law points to it | The NIST AI RMF's four functions |
| Ethics | People and professions, over time | Everyone, by conscience | Lost trust | Chapter 3's five principles: honesty, attribution, consent, privacy, and harm |

The lines between them can move. Guidance becomes binding when a contract requires it. A law can also reward it. Colorado's 2024 AI act, for example, gave a defense to companies that followed a designated AI risk management framework and fixed the violations they found. (Source: the bill summary for SB24-205, Colorado General Assembly, read October 21, 2026.) That act is being rewritten, as you will see below. So ask two questions of any rule: what kind is it today, and what points to it?

### Try It Yourself 8.1: Sort the Rules 🛠️

**Predict:** Here are four rules a tutoring center might face. (1) "Tutors may not use AI to write feedback on student essays," from the center's handbook. (2) The NIST AI RMF's advice to map an AI system's risks before you use it. (3) A state statute that fines businesses for undisclosed chatbots. (4) "Tell people when a machine helped." Predict which one is hardest to sort, and why.

**Run:** Open `rules-sorting-sheet.md` from this chapter's data pack. Fill one row per rule: the kind, the source, who made it, and what happens if it is broken. Use the four definitions at the top of the sheet, not a chat assistant.

**Explain:** Was your prediction right? In 1-2 sentences, explain which column of the sheet decided your hardest case.

### The EU AI Act and Its Risk Tiers

The **EU AI Act** is Regulation (EU) 2024/1689, the European Union's law on AI, adopted on June 13, 2024 and published in the EU's Official Journal on July 12, 2024. It sorts AI uses into risk tiers. A **risk tier** is a level of possible harm that a law assigns to a kind of AI use, with duties that grow as the risk grows. The Act also reaches beyond Europe. Article 2(1)(c) covers providers and deployers outside the EU when the AI system's output is used in the EU.

Here are the tiers as the consolidated text on EUR-Lex reads (version of July 27, 2026, read October 21, 2026):

| Tier | What falls in it | One example from the Act | Where the Act says so | Applies from (as of October 2026) |
| --- | --- | --- | --- | --- |
| Prohibited practices | Uses the Act bans | Inferring the emotions of people at work or in school, except for medical or safety reasons | Article 5(1)(f) | February 2, 2025 (two bans added in 2026 apply from December 2, 2026) |
| High-risk systems | Systems listed in Annex III, and AI that is, or is a safety part of, a product regulated under Annex I | AI used to recruit or select people, including to filter applications and evaluate candidates | Article 6 and Annex III, point 4(a) | December 2, 2027 for Annex III, and August 2, 2028 for Annex I |
| Transparency duties | Systems that interact with people or generate content | A system that talks with people must tell them they are talking with AI | Article 50 | August 2, 2026 (December 2, 2026 for content-marking by systems already on the market) |
| Everything else | Uses outside the three tiers above | A spam filter | None of the three tiers' duties | Not applicable |

You will often see the last two rows called "limited risk" and "minimal risk," as in the sample response below. Those labels do not appear in the Act's text, so cite the article, not the label.

The dates in the last column are not the dates the Act was passed with. On July 8, 2026, the EU adopted Regulation (EU) 2026/1744, called the Digital Omnibus on AI, and it was published on July 24, 2026. It moved the high-risk dates later and added two bans. Before it, the original Article 113 set August 2, 2026 for the Annex III high-risk rules. A policy written in 2025 that copied those dates is now wrong, and nobody had to break a rule to make it wrong.

### Asking for a Tier, Then Checking It

Here is a trucking dispatcher with a reason to care. Notice that the prompt asks for the article, because the article is what you will check. Send the prompt without the [Step] lines:

```text
[Step 1: say who is asking and why the Act matters to them]
I help a trucking dispatch company in Phoenix that is opening an office in Spain, and I am sorting our AI uses against the EU AI Act.
[Step 2: list the uses one at a time, so each gets its own answer]
Uses: (1) a tool that ranks job applicants for driver positions; (2) a chat assistant on our website that answers shipment questions; (3) a spam filter on the dispatch inbox; (4) a camera system that reads drivers' facial expressions to judge their mood during a shift.
[Step 3: ask for the article, which is what you will check]
For each use, name the risk tier and the article of the Act that puts it there.
[Step 4: ask for dates and for doubt, because the dates change]
Say the date that tier's obligations apply, and mark any answer you are unsure of. One line per use.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
1. **Applicant ranking tool:** High-risk, under Art. 6(2) with Annex III point 4(a) (recruitment and candidate evaluation). The original date is 2 Aug 2026. **Unsure:** the EU's "Digital Omnibus" proposal would push Annex III high-risk obligations back to about 2 Dec 2027, and I can't confirm whether that was adopted, so check the current text.

2. **Website shipment chat assistant:** Limited risk (transparency), under Art. 50(1), which requires telling users they are talking to an AI. This applies from 2 Aug 2026. I'm fairly confident, though the Omnibus may adjust some of Art. 50.

3. **Dispatch inbox spam filter:** Minimal risk. It isn't in Art. 5 or Annex III, so no specific obligations apply. Art. 95 only encourages voluntary codes of conduct, and the general AI-literacy duty in Art. 4 has applied since 2 Feb 2025. I'm confident in the tier, but I'm not citing a specific date because there are no tier obligations.

4. **Facial-expression mood camera for drivers:** Prohibited, under Art. 5(1)(f), which bans inferring emotions in the workplace except for medical or safety reasons. This has applied since 2 Feb 2025. **Unsure:** a narrow safety use such as drowsiness detection may fall outside the ban, but judging mood doesn't fit that exception. Fines can reach €35M or 7% of worldwide turnover.

**Scope caveat:** As a US company, you're covered under Art. 2(1)(c) only where the AI's output is used in the EU, such as for the Spanish office's hires, customers and drivers. Check this with counsel.
```

Check it against the Act, one article at a time. The tiers hold: Annex III, point 4(a) covers recruitment, Article 50(1) covers a system that talks with people, and Article 5(1)(f) bans emotion inference at work. The fine it quotes matches Article 99. The dates are where it slips. It gives August 2, 2026 for the applicant tool, the date in the Act as first published. Then it flags its own doubt: the Digital Omnibus was a proposal it could not confirm. That doubt was the most useful line in the response. As of October 2026 the Omnibus is law, and the date is December 2, 2027. This is Chapter 2's knowledge cutoff at work. Notice the labels, too. "Limited risk" and "Minimal risk" are not the Act's words.

The scope line matters for Phoenix. Article 2(1)(c) is real, and it is why the Spanish office changes the answer. A dispatcher with no EU hires, customers, or drivers would read the Act for ideas, not as a law it must follow.

### Try It Yourself 8.2: Check a Tier Yourself 🛠️

**Predict:** A tutoring center that also runs online courses in Ireland uses three AI tools. One scores placement tests to decide which course level a student may enter. One chat assistant answers questions about class times. One tool flags possible cheating during online exams. Predict the tier of each.

**Run:** Send the trucking prompt with the tutoring center's three uses in place of the dispatcher's four. Then open the Act on EUR-Lex (Further Reading) and find Annex III, point 3, which covers education. Mark each line of the response Holds, Contradicted, or Not in source, and quote the Annex point or article that decided it.

**Explain:** Was your prediction right? In 1-2 sentences, explain which date in the response you would not copy into a policy without checking Article 113.

### Frameworks and Principles: NIST and the OECD

The **NIST AI Risk Management Framework (NIST AI RMF)** is a voluntary framework from the U.S. National Institute of Standards and Technology for managing the risks of AI. NIST released it as AI 100-1 on January 26, 2023. The document calls itself "voluntary, rights-preserving, non-sector-specific, and use-case agnostic." Its core has four functions:

| Function | What it asks (from AI 100-1) | A Copperwind example |
| --- | --- | --- |
| Govern | Build a culture of risk management, with policies, roles, and accountability. NIST calls it cross-cutting, so it runs through the other three | The operations manager signs an AI Use Policy and names who answers questions |
| Map | Establish the context, so you know what the system is for and who it could affect | List each AI use, the data it touches, and the clients it reaches |
| Measure | Analyze, assess, and track the risks you mapped, with numbers or careful judgment | Count how many AI-drafted replies needed a fix before sending |
| Manage | Spend effort on the mapped and measured risks, and plan how to respond when something goes wrong | Decide who reviews a reply, and what happens after an error reaches a client |

As of October 21, 2026, NIST's AI RMF page says the framework "is being revised as part of the White House AI Action Plan." The page also lists a Generative AI Profile (NIST-AI-600-1, released July 26, 2024). Version 1.0 is still the one to cite until NIST publishes a revision.

The **OECD AI Principles** are the Organisation for Economic Co-operation and Development's principles for trustworthy AI. Countries adopted them in May 2019 and updated them in May 2024. As of October 21, 2026, the OECD lists 47 adherents. Five values-based principles head the list:

* Inclusive growth, sustainable development and well-being
* Human rights and democratic values, including fairness and privacy
* Transparency and explainability
* Robustness, security and safety
* Accountability

For a company, they are guidance. For the countries that adhere, they are a commitment that shapes the laws those countries write.

### State Laws and Sector Rules in the United States

This section reads one U.S. state law closely and points to two older federal laws for particular sectors. Colorado shows how fast a state law can move. Here is its record on the Colorado General Assembly's bill pages, read October 21, 2026:

* **SB24-205,** approved May 17, 2024, set duties for developers and deployers of "high-risk" AI systems, starting February 1, 2026.
* **SB25B-004,** approved August 28, 2025, moved those requirements to June 30, 2026.
* **SB26-189,** signed May 14, 2026, repeals and reenacts those provisions effective January 1, 2027. The new text covers "automated decision-making technology" used in consequential decisions, such as employment, housing, and lending.

The 2024 act's duties were delayed once, then rewritten before they began. A policy that cited the 2024 act by section will cite rewritten text on January 1, 2027. The sector laws are older and steadier: FERPA for student records and HIPAA for health information. Section 8.2 takes them up, and Section 8.3 takes up copyright.

### Quick Check 8.1 ✅

1. A trucking dispatcher in Phoenix has no EU customers, hires, or drivers. Its owner asks whether the EU AI Act's high-risk rules apply to its applicant-ranking tool. Use Article 2(1)(c) to decide, and name the kind of rule the Act becomes for this owner.
2. A credit union branch's handbook says, "Follow the NIST AI RMF for every AI tool." Categorize the handbook line and the framework as kinds of rules, and explain what changed when the handbook adopted the framework.
3. In July 2026 the EU moved its high-risk dates later, and Colorado rewrote its 2024 law before its duties began. Analyze what these two changes say about the current state of AI regulation, and name the habit a policy writer needs because of it.

---

## 8.2 Privacy: What You Enter and What the Vendor Keeps

Chapter 1's one rule told you what never goes into a tool. That rule still stands. This section adds the other half: what happens to what you do enter. That answer lives in documents the vendor writes, and they differ by tool and by plan.

**Personal data** is any information that identifies a person or can be linked to one: a name, an address, an account number, a face, a voice. Most of what you are tempted to paste into a tool at work contains some. A ticket has a client employee's name and email. A late-rent notice has a tenant's unit number.

Two vendor documents tell you what happens to it. A **data policy** is the vendor's statement of what it collects when you use its tool, what it does with that data, how long it keeps it, and how you can delete it. Some vendors call it a privacy notice or a privacy policy, and they often add help pages on data controls. **Terms of use** are the contract you accept to use a tool. They say what you may do with it and what the vendor may do with your content and with the output. Accepting them makes them binding on you.

Both documents usually split into two versions. Consumer terms cover free and personal plans. Business terms cover work, school, and enterprise accounts, and they often promise more. So the same tool can be fine for one task on a work account and wrong for it on a personal one.

### Reading a Data Policy's Fields

The `data-policy-reading-sheet.md` in this chapter's data pack has six fields: what the vendor keeps, whether it trains on your input, retention, deletion, consumer versus business terms, and human review. A chat assistant can help you pull fields out of a policy you paste in, which is grounding from Chapter 5. Here is that job on an excerpt from a fictional tool's policy. Send the prompt without the [Step] lines:

```text
[Step 1: say what the text is]
Below is an excerpt from the data policy of an AI writing tool.
[Step 2: name the fields you need, in a fixed order]
Fill in these five fields from the excerpt only: what the vendor keeps; whether it trains on your input; how long it keeps your data; what deleting does; how business accounts differ.
[Step 3: ask for the evidence, so you can check each answer]
Quote the sentence each answer comes from.
[Step 4: give the model a way to say the text is silent]
If the excerpt does not answer a field, write "Not stated."

Excerpt: When you use the free or personal plan, we store your prompts, the files you upload, and the responses we generate. We may use this content to improve our models unless you turn off "Help improve the service" in Settings. Conversations stay in your history until you delete them. When you delete a conversation, we remove it from your history right away and from our systems within 30 days, except conversations flagged for a safety review, which we keep for up to two years.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

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

Check each quote against the excerpt. Three of the four match word for word. The quote under field 2 changed the double quotation marks around the setting's name to single ones, a small edit, but a quote is supposed to be exact. The answers hold. The most useful line is the last one: "Not stated." The excerpt covers only the free plan, so you cannot tell from it whether a business account trains on your work. A policy writer who filled that field from memory would be guessing. Notice field 4, too. Deleting does not always delete. Flagged conversations stay for up to two years.

!!! note "Tool check (verified October 2026)"
    Where the core roster tools' data controls lived on October 21, 2026, by each vendor's own pages. ChatGPT (OpenAI, "Data controls in ChatGPT" help page): open Settings, then Data controls, and turn off "Improve the model for everyone." Temporary chats are not used to train models and may be kept up to 30 days. OpenAI says it does not train on Business, Enterprise, or Edu workspace content by default. Gemini (Google, Gemini Apps Privacy Hub, notice last updated October 13, 2026): Gemini Apps Activity holds the Keep Activity setting and the auto-delete period, 18 months by default. Chats that human reviewers read are kept up to three years, even after you delete your activity. Work and school accounts may have different terms. Microsoft Copilot (Microsoft, "Privacy FAQ for Microsoft Copilot"): you can opt out of model training on your conversations, which are stored for 18 months by default. That FAQ does not cover Microsoft 365 Copilot signed in with a work or school (Entra ID) account. Menus change, so look for the same setting under a nearby label.

### Try It Yourself 8.3: Read Your Own Tool's Policy 🛠️

**Predict:** Pick a chat assistant you have an account on. Before you open anything, predict two answers: does it train on your input by default, and how long does it keep a chat you never delete?

**Run:** Open the vendor's own data policy and data-controls pages, not a news story about them. Fill one `data-policy-reading-sheet.md` for your plan, with the page title, URL, and date for each field. Write "Not stated" where the pages are silent.

**Explain:** Compare the sheet with your predictions. In 1-2 sentences, explain which field you would most want a colleague to check before your tool goes into an AI Use Policy.

### FERPA and HIPAA Touchpoints

Two federal sector laws come up whenever students or patients appear in a prompt. You do not need to master either one. You need to recognize when one applies, and then follow the rules of the organization that holds the records.

**FERPA** is the Family Educational Rights and Privacy Act, a federal law that gives parents, and then students, rights over education records. According to the Department of Education's Student Privacy Policy Office (studentprivacy.ed.gov, read October 21, 2026), those rights pass to the student at age 18 or when the student enters a postsecondary school. The statute is 20 U.S.C. § 1232g, and the regulations are 34 CFR Part 99. Here is the question a community college student worker might ask:

```text
I work part-time in a community college advising office. Can I paste a student's degree audit, with their name and grades, into a free chat assistant to summarize it for them? Does FERPA apply? Answer in under 120 words.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Yes, FERPA applies. A degree audit with a student's name and grades is a protected education record, and you'd be handling it as a school official with a legitimate educational interest.

Pasting it into a free chat assistant is risky and generally not okay. Free tools usually aren't covered by a contract with your college, may retain or train on inputs, and sending identifiable data to them can count as an unauthorized disclosure.
```

The regulations back it. Under 34 CFR 99.30, a school needs written consent before it discloses personally identifiable information from education records, except under the conditions in 99.31. The condition the response names, a school official with a legitimate educational interest, is 99.31(a)(1). That same section lets an outside party count as a school official only if the school controls how it uses the records. A free chat assistant on a personal account meets none of that. The response's line that free tools "may retain or train on inputs" is a lead, not a fact about any one tool. Your reading sheet holds that fact.

**HIPAA** is the Health Insurance Portability and Accountability Act, a federal law whose rules protect health information. They apply to certain health care providers, health plans, and clearinghouses (covered entities), and to the businesses that work for them (business associates). Here is an IT support question from a physical therapy office:

```text
I do IT support for a small physical therapy office. A staff member wants to paste a patient's appointment note, with the patient's name and treatment, into a free chat assistant to write a friendlier reminder text. Under HIPAA, is that allowed? Answer in under 120 words.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
**Generally no, not with a free chat assistant.**

A patient's name combined with treatment information is protected health information (PHI). A physical therapy office is a covered entity, and sharing PHI with a vendor requires a signed Business Associate Agreement (BAA). Free consumer chat tools don't offer BAAs, and they may retain or use inputs, so pasting the note would likely be an impermissible disclosure.

**Safer options:**
- Remove all identifiers (name, date, details) and use a generic template, adding specifics afterward.
[...]
```

Check it against HHS's page on covered entities and business associates (last reviewed August 21, 2024, read October 21, 2026). The contract point holds: a covered entity that engages a business associate "must have a written business associate contract or other arrangement." The safer option, a template with no identifiers, is Chapter 3's privacy check in action. One claim goes further than HHS does. The response says flatly that "A physical therapy office is a covered entity." HHS adds a condition. A provider is covered "only if they transmit any information in an electronic form in connection with a transaction for which HHS has adopted a standard." Whether this office does is its own fact to confirm, and HHS links a question-and-answer decision tool for exactly that.

Copperwind has medical and physical therapy offices among its clients, so this question will reach a Deskside technician. Whether Copperwind itself counts as a business associate depends on its contracts with those clients. That question belongs to the operations manager, not to a chat assistant.

### Quick Check 8.2 ✅

1. A data policy reads: "We may use your content to improve our services unless you opt out. Content from business plans is never used for training." Fill the training and consumer-versus-business fields of the reading sheet from it, and name one field it leaves "Not stated."
2. A receptionist at a veterinary clinic asks whether HIPAA stops her from pasting a pet owner's name and phone number into a chat assistant. Use HHS's definition of a covered entity to decide whether HIPAA is the rule that settles it, and name the kind of rule that still does.
3. A coworker says, "I deleted the chat, so the client's data is gone." Using the fictional policy excerpt and the Tool check above, examine whether that claim holds, and say what your reading sheet should record.

---

## 8.3 Who Owns What

Ownership questions come in three parts. Who owns the material a model was trained on? Who owns what the model produces for you? And what did you agree to when you accepted the tool's terms? Chapter 3 named the umbrella question, content ownership. This section gives you the law under it.

**Copyright** is the legal right of the author of an original work to control copies, adaptations, and public uses of it. In the United States, copyright requires a human author. The Copyright Office's guidance and one federal appeals court both say so.

### What the Copyright Office Says

The U.S. Copyright Office is issuing a report, Copyright and Artificial Intelligence, in parts. As of October 21, 2026, its AI page lists three:

* **Part 1 (July 31, 2024)** covers digital replicas, meaning AI copies of a real person's voice or likeness.
* **Part 2 (January 29, 2025)** covers whether AI output can be copyrighted. Its conclusions: copyright protects "the original expression in a work created by a human author," even when the work also has AI-made material. It does not extend to purely AI-generated material. Whether a person contributed enough is decided case by case. And "prompts alone" do not give a user enough control to be the author, "given current generally available technology."
* **Part 3 (pre-publication version, May 9, 2025)** covers training AI on copyrighted works. It finds that several stages of building a model use copyrighted works in ways that touch the owners' rights. Whether that is excused as fair use depends on the case. The report says some uses are likely transformative, while some commercial uses that compete with the original works go "beyond established fair use boundaries." The Office says a final version will follow.

The reports are guidance from the agency that registers copyrights. Courts decide individual cases, including the fair use questions Part 3 discusses.

**A case to know.** In *Thaler v. Perlmutter*, decided March 18, 2025, the U.S. Court of Appeals for the D.C. Circuit upheld the Copyright Office's refusal to register an image that its owner said an AI system created on its own. The court held that the Copyright Act requires human authorship. The decision is posted on the Copyright Office's AI page.

### A Poster, Checked Against the Report

A community theater asks about its show poster:

```text
Our community theater made its show poster with an image generator. We typed a detailed prompt, picked one of four images, and added the show title and dates ourselves in a design app. Can we register a copyright in the poster in the United States, and who owns what? Answer in under 120 words.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
Yes, but only for part of it.

**Registrable:** Under U.S. Copyright Office guidance (and *Thaler v. Perlmutter*), copyright requires human authorship. Your title, dates, text, and the layout/arrangement you created are human-authored and registrable. If you edited or altered the image meaningfully, those modifications may count too.

**Not protected:** The raw AI-generated image. Writing a prompt and picking one of four outputs generally isn't enough authorship.
[...]
**Ownership:** You'd own only your human-authored parts (likely the theater, if made as employees or volunteers who assign rights). Others can freely copy the bare image, though not your protected additions. Check the generator's terms too.
```

Check it against Part 2. "Writing a prompt and picking one of four outputs generally isn't enough authorship" matches the report's conclusion on prompts. The response slips on one line: "Your title, dates, text, and the layout/arrangement you created are human-authored and registrable." The layout and arrangement are the theater's own expression. The title and dates are not. Copyright regulations exclude "names, titles, and slogans" and other short phrases (37 CFR 202.1(a), read October 21, 2026). The response cites *Thaler v. Perlmutter* for the human-authorship rule, and the case says so. The line about volunteers who "assign rights" is a guess the facts do not support, since the theater never said who made what. Its last sentence is the best one: check the generator's terms. Those terms are where the vendor says what you may do with the image.

Terms of use are the vendor's policy for its users, and accepting them turns that policy into a contract you are bound by. Read the section on content or output before you put a generated image under your organization's name. A Copyright Office report cannot tell you what a vendor's contract allows.

### Try It Yourself 8.4: Who Owns Your Piece? 🛠️

**Predict:** Pick something you made with AI help in this course, such as a newsletter item, an image, or a reply. Predict which parts of it the Copyright Office's Part 2 conclusions would treat as yours.

**Run:** Send the theater prompt with your piece described in place of the poster. Mark each claim in the response Holds, Contradicted, or Not in source, checked against the Part 2 conclusions in this section. Then open your tool's terms of use and find the section on output. Quote one sentence from it.

**Explain:** Did the response agree with your prediction? In 1-2 sentences, explain why the terms of use can settle a question the Copyright Office report cannot.

### Quick Check 8.3 ✅

1. A community theater's volunteer writes a 20-word prompt, picks one of three generated logos, and changes nothing. The board wants to register the logo. Apply Part 2's conclusions to decide what the theater can claim, and say what it would need to add to claim more.
2. A coworker says, "The Copyright Office ruled that training AI on books is illegal." Examine that claim against Part 3 and rewrite it so it is accurate.

---

## 8.4 Writing the AI Use Policy

Every rule in this chapter lands somewhere: in a policy a person can follow on a busy Tuesday. An **AI Use Policy** is an organization's written rules for how its people use AI tools. In this book it has seven sections, in this order: Purpose, Approved tools, What never goes in, Review before use, Disclosure, Who to ask, and Review date. The template is `ai-use-policy-template.md` in this chapter's data pack.

You already follow one kind of AI use policy. Your course syllabus states the AI expectations for your class, and Chapter 3 said the syllabus wins when it and this book differ. A workplace policy works the same way. It is the organization's own rule, and it can be stricter than any law.

### Seven Sections, Four Kinds of Rules

Each section answers one question, and each one leans on a kind of rule you can name:

| Section | The question it answers | The kind of rule it usually rests on | Where its facts come from |
| --- | --- | --- | --- |
| Purpose | Why does this policy exist, and who must follow it? | Policy, with the ethics behind it | The organization's own reasons |
| Approved tools | Which tools, on which plan, with which settings? | Policy, built on each vendor's terms of use | Your reading of each data policy |
| What never goes in | What may no one type into any tool? | Law (FERPA, HIPAA, where they apply), policy, and Chapter 1's one rule | The data the organization handles |
| Review before use | What must a person check before output goes out? | Policy and guidance (the NIST AI RMF's Manage function) | Chapters 1 and 5: the three passes and the Output Checklist |
| Disclosure | When do we tell readers that AI helped, and what do we say? | Ethics (honesty), policy, and law where a law applies | Chapter 3's disclosure statement |
| Who to ask | Which role answers questions? | Policy (the Govern function) | The organization chart |
| Review date | When will this policy be checked again? | Policy | How fast the rules above change |

Label each rule in your draft with its kind: [law], [policy], [guidance], or [ethics]. A label makes a reviewer ask the right question. For a [law] rule, the question is which law, read on what date. For a [policy] rule, it is who decided it.

### A First Draft, Audited

A city parks department needs a policy after a bad paste. Its deputy director asks a chat assistant for a first draft:

```text
Draft an AI Use Policy for a city parks department, with these sections in this order: Purpose; Approved tools; What never goes in; Review before use; Disclosure; Who to ask; Review date. Use only these facts. The department has 25 staff. Staff use one approved chat assistant, on the city's work account, to draft event flyers and replies to resident emails. Last month a staff member pasted a resident's complaint, with the resident's home address, into a personal chat account. The deputy director signs the policy and answers questions. Do not name any law. Under 300 words.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
[...]
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
[...]
```

Audit it section by section against the question each section answers. "What never goes in" is mostly right, and it adds one line nobody gave, "Complaint text copied from residents." That is a new rule the deputy director must decide, not a fact. "Review date" invents "one year from the signing date." The Disclosure section fails outright. It answers a different question, what to do after a mistake, and never says when to tell residents that AI helped write a reply. The draft ran 269 words, named no law, and read well. A reader who checked only for polish would sign it. The audit catches it because each section has a question to answer.

### Fix It 8.1: The Disclosure Table 🔧

You are drafting the Disclosure section of Copperwind's policy, and you want the laws behind it.

**Symptom:** The prompt asked for a table:

```text
I am writing an AI use policy for a small IT services company in Phoenix, Arizona. In the Disclosure section, list the laws that require us to tell clients when AI helped write a reply or a document. For each law, give its name, its section number, and one sentence on what it requires. A table is fine.
```

Here is the response it gave (captured from a chat assistant, October 2026):

```text
[...]
**I can't point you to a law that requires an Arizona IT services company to tell clients when AI helped draft a reply or document.** To my knowledge, neither Arizona nor the federal government has one. The laws that exist are narrower: they mostly cover AI chatbots or AI interactions with consumers, and they depend on where your clients are located. Please don't present the table below as "laws that require us to disclose" without attorney review.
[...]
| Law | Section | What it requires | Likely relevance to you |
|---|---|---|---|
[...]
| Utah AI Policy Act (as amended 2025) | Utah Code Title 13, Ch. 75 (verify exact section) | Generative AI use must be disclosed when a person clearly asks, and regulated occupations must disclose proactively. | Only if you serve Utah consumers. IT services probably aren't a regulated occupation. |
| Colorado AI Act (SB 24-205) | C.R.S. § 6-1-1704 | Deployers of AI systems that interact with consumers must disclose that the consumer is interacting with AI. | Mainly applies to high-risk systems and consumers. Its effective date has been delayed, so verify its current status. |
[...]
I'm confident about the general content of these laws, but section numbers and effective dates in this area have been changing quickly, so confirm each one before it goes in your policy.
[...]
```

It opens with a careful disclaimer and closes with a warning to confirm every section number. The table between them looks like legal research, with a name, a section, and a summary in every row. It could go straight into the policy as written.

**Diagnose:** Before you touch the prompt, open the Utah row on the Utah Legislature's site (le.utah.gov) and the Colorado row on the Colorado General Assembly's site (leg.colorado.gov). For each row, write down what you find at the place the row sends you. Then name, in one sentence, what the prompt made the model supply for every row.

**Repair:** Here is what the two sites showed on October 21, 2026. Utah's disclosure rule is real and in force, and the row's summary of it is close. But "Chapter 75" is the number S.B. 226 gave the rule in 2025. The code moved it to avoid a duplicate number, and it now sits at Title 13, Chapter 77, section 13-77-103, "Required disclosures." Title 13, Chapter 75 is the Franchise Protection Act, so a reader who looks up the row's number lands in the wrong law. The row also files the rule under the "AI Policy Act," which is Chapter 72, when the rule has a chapter of its own. The Colorado row's section is real too. In SB24-205, section 6-1-1704 is titled "Disclosure of an artificial intelligence system to consumer," and the row's description of it holds. Its relevance column does not. It says the section "Mainly applies to high-risk systems," but 6-1-1704 reaches any AI system intended to interact with consumers.

None of these citations is invented. Each one is real and still sends you to the wrong place or misstates what the law covers. The model hedged ("verify exact section"), but the prompt demanded a section number for every row, so it supplied one from training data the codes have since moved past. The repair replaces one sentence of the prompt. That sentence swaps a demand for section numbers with a demand for the law's name, a source the reader can open, and the model's doubt, and that swap is the single change. Everything else stays the same:

```text
For each law, give only its name and the official website where I can read its current text, and say how sure you are that it applies to us.
```

Sample response (captured from a chat assistant, October 2026). Your output will differ:

```text
**Short answer:** I'm not aware of any Arizona or U.S. federal law that requires an IT services company to tell clients when AI helped draft a reply or document. The laws below are the closest candidates. Most apply only in specific circumstances, and my information may be out of date, so check each current text (or have an attorney do so) before relying on this.
[...]
| Law | Where to read it | Likelihood it applies to you |
|---|---|---|
[...]
| **Colorado AI Act (SB 24-205)** | leg.colorado.gov/bills/sb24-205 | **Low.** It covers "high-risk" AI used in consequential decisions affecting consumers, mainly in Colorado. Its effective date has been delayed and may have changed again, so verify the status. |
| **Utah AI Policy Act (SB 149 and amendments)** | le.utah.gov | **Low.** It requires disclosure when a person asks if they're talking to AI, plus stricter rules for regulated occupations. It matters mainly if you serve Utah clients. |
| **California Bot Disclosure Law (B&P Code §17941) and related AI bills** | leginfo.legislature.ca.gov | **Low.** It targets bots used to influence sales or votes, and applies mainly to California residents. |
[...]
```

**Verify:** The new table gives a website for each row, not a section number, and rates each law's fit for an Arizona company. One section number slipped back in, in the California row's name, so the repair narrowed the risk without removing it. Now follow the leads. The Utah row sends you to le.utah.gov with no chapter claim, and Title 13, Chapter 77 there holds section 13-77-103. The Colorado row says the date "may have changed again." The Colorado General Assembly's page shows SB26-189, signed May 14, 2026, which repeals and reenacts those provisions effective January 1, 2027. The Colorado row still describes the law as covering "high-risk" AI in consequential decisions, which leaves out SB24-205's separate duty in 6-1-1704 to tell consumers they are talking with an AI system. That gap is a second lead, and only the bill text settles it. The lesson holds for every row: a model's legal citations can be real and still send you to the wrong place or misstate the scope, so you open the code. For Copperwind's Disclosure section, write the rule as [policy] and [ethics], and cite a law only after you have read it on the legislature's own site.

### Try It Yourself 8.5: What a Teller Never Types 🛠️

**Predict:** You will draft the "What never goes in" section for a credit union branch. Predict which item the tool's examples will get least right for a teller's day.

**Run:** Fill the two gaps from this chapter, then send the prompt in a fresh conversation. Fill the first gap with the kinds of personal data a teller handles, from Section 8.2. Fill the second with Chapter 1's one rule.

```text
Write the "What never goes in" section of an AI Use Policy for the staff of a credit union branch. List what staff must never paste into an AI tool: ____. For each item, give one example from a teller's day. End with the rule staff follow when they are unsure: ____. Under 150 words, plain words, no laws named.
```

Check the result against three criteria: every item you listed appears, each example fits a teller's day, and the closing rule matches Chapter 1's.

**Explain:** Compare your run with the sample below. In 1-2 sentences, explain what your gaps made the model produce that it could not have guessed.

Compare your run with the response one chat assistant gave in October 2026. Its first gap held "members' names, account numbers, card numbers, Social Security numbers, balances, and home addresses." Its second held Chapter 1's rule:

```text
[...]
Never paste any of these into an AI tool:

- **Member names.** Example: typing "Maria Lopez complained about a hold" into a draft email.
- **Account numbers.** Example: copying a number from a screen to ask why a deposit looks wrong.
- **Card numbers.** Example: pasting a debit card number while explaining a declined purchase.
- **Social Security numbers.** Example: adding the number from a new-account form to a summary.
- **Balances.** Example: asking for help wording a message about a member's overdrawn balance.
- **Home addresses.** Example: pasting an address from a change-of-address request.

**When you are unsure:** if you would not post it on a public bulletin board, do not type it into an AI tool.
```

All six items appear, each with an example a teller would recognize, and the closing rule is Chapter 1's word for word. It ran 123 words. One example invents a member's name, "Maria Lopez," as the thing not to type. That is fine in a policy, as long as the name is fictional and nobody mistakes it for a real member.

### Quick Check 8.4 ✅

1. A tutoring center's draft policy says under Disclosure: "Report any AI mistake to the director." Decide whether the section answers its question, and rewrite it in two sentences that do.
2. A draft rule reads "Staff must follow HIPAA when using AI [law]." Judge whether the rule and its label work for an apartment management office, and write the line the office should use instead.
3. Write the Review date section for the parks department in two sentences. Name one event that should trigger an early review, using a change this chapter described.

---

## 8.5 Summary and Retrieval 💡

### Key Concepts

* Governance starts with the four kinds of rules. Law binds and carries penalties, policy is an organization's own rules, guidance is a framework an organization chooses, and ethics is the principles behind the other three. Ask what kind a rule is today and what points to it.
* The EU AI Act sorts uses into risk tiers: prohibited practices (Article 5), high-risk systems (Article 6 and Annex III), and transparency duties (Article 50). As of October 2026, Regulation (EU) 2026/1744 moved the Annex III high-risk date to December 2, 2027. Cite the article and the dated text, never a remembered date.
* The NIST AI RMF is voluntary guidance with four functions: Govern, Map, Measure, and Manage. The OECD AI Principles set five values that 47 adherents had signed on to as of October 2026. U.S. state laws such as Colorado's change quickly, so read the bill page before you cite one.
* A vendor's data policy and terms of use say what it keeps, whether it trains on your input, how long it keeps data, and what deleting does. Consumer and business terms differ. "Not stated" is a finding.
* FERPA covers education records, and HIPAA covers health information held by covered entities and their business associates. Recognize when one applies, and follow the record holder's rules.
* Under the Copyright Office's 2025 guidance, prompts alone do not make you an author. Your own additions can be protected. Training on copyrighted works is a fair use question that courts decide case by case.
* An AI Use Policy has seven sections in order: Purpose, Approved tools, What never goes in, Review before use, Disclosure, Who to ask, and Review date. Label each rule with its kind, and cite a law only after you have read it.

### Key Terms

See course glossary for full definitions

* governance, four kinds of rules, EU AI Act, risk tier, NIST AI Risk Management Framework (NIST AI RMF), OECD AI Principles (Section 8.1)
* personal data, data policy, terms of use, FERPA, HIPAA (Section 8.2)
* copyright (Section 8.3)
* AI Use Policy (Section 8.4)

### Retrieval Practice

Answer from memory before checking back through the chapter.

1. Name the four kinds of rules in order, and give one example of each from this chapter.
2. Name the EU AI Act's three tiers of duties and the article for each, and explain why a date you remember is not safe to cite.
3. Name the seven sections of an AI Use Policy in order, and say which section the parks department draft failed outright, and why.
4. From Chapter 6: Explain what makes a criterion checkable, and rewrite "the policy is clear" as a criterion you could check.
5. From Chapter 4: Name the five parts of a prompt, and say which part holds "Do not name any law" in the parks department prompt.

---

## 8.6 Skills Lab 8A: The Copperwind AI Use Policy

**Goal:** Draft the Copperwind AI Use Policy for the operations manager to sign. Build it from your own reading of the tools' data policies and the four kinds of rules, and add a note on what it settles and leaves open.

**Starter files:** Provided files in `assets/code/chapter-08/` from the course data pack: `skills-lab-8a-worksheet.md` (your answer file), `policy-brief.txt` (Mei Lin's brief), `rules-sorting-sheet.md`, `data-policy-reading-sheet.md`, and `ai-use-policy-template.md`. Download the data pack from Canvas, extract it, and work at the extracted `cis137` root. Open each file in any text editor and never retype its contents. The lab files are fictional, so you may paste them into a chat assistant once your privacy plan allows it. You first met Copperwind in Chapter 1, and this lab gives you everything it needs, so you do not need any earlier file.

### Part 1: Foundation (Aligns with Objective 8.1)

Work in `skills-lab-8a-worksheet.md`, which has a space for every task below. Read `policy-brief.txt` in full before you write anything.

1. Before you send any prompt, write your privacy plan in two columns: what from the brief may go into a tool, and what stays out of every prompt. Give the reason for each item that stays out.
2. Fill `rules-sorting-sheet.md` for situations A, B, and C and the operations manager's question about applicant summaries. Write one row per rule, and name its kind, its source with the date you read it, and what the policy must say because of it. At least one row must be a law and one must be guidance, each read in its primary document.
3. Place the applicant-summary use under the EU AI Act's risk tiers, citing the article or Annex point. Then decide in two sentences whether the Act binds Copperwind, citing Article 2 and a fact from the brief. Name the NIST AI RMF function the operations manager's question calls for, and say why.

### Part 2: Application (Aligns with Objective 8.2)

1. Read the data policy pages of two tools from your course roster. Fill one `data-policy-reading-sheet.md` for each, with the page title, URL, and date for every field. Write "Not stated" where the pages are silent.
2. In a fresh conversation, ask a chat assistant to fill the same six fields for one of those tools from what it knows, with no pages pasted in. Paste the prompt and the response with the tool and the date. Mark each field Holds, Contradicted, or Not in source against your reading sheet.
3. Apply the touchpoints to the brief in two short paragraphs. For situation A, say what a patient's name in a ticket means under HIPAA, citing HHS's page with its date. For situation B, say what Copperwind can and cannot claim to own in the flyer image, citing the Copyright Office's Part 2 with its date.

### Part 3: Extension (Aligns with Objectives 8.2 and 8.3)

1. Draft the Copperwind AI Use Policy in `ai-use-policy-template.md`, with all seven sections in order. Settle situations A, B, and C by name, and label every rule [law], [policy], [guidance], or [ethics]. You may ask a chat assistant for a first draft. If you do, paste the prompt and the response, and mark every line you kept, changed, or cut. Name no law you have not read yourself.
2. Test the policy cold. In a fresh conversation, paste your policy and ask the chat assistant to answer situations A, B, and C as a new Deskside technician who has only the policy. Paste the prompt and the response. Mark each answer MATCHES or DIFFERS from what you meant, then fix one gap the test found and quote the changed line.
3. Write a note to the operations manager (100 to 150 words). Say what the policy settles, what it leaves open (including where the applicant-summary question belongs), and when it should be reviewed and why.

### Questions & Analysis 🤔

Answer both questions in the worksheet's final section. These answers carry significant rubric weight.

1. Quote one row from your Part 2 Task 2 marks where the chat assistant's account of a vendor's policy did not hold against your reading sheet. If every row held, quote the row you were least sure of. Explain what your Approved tools section would have said if you had trusted the chat assistant, and quote the line your own reading put there instead.
2. Quote one rule from your policy with its kind label. Using its row in your `rules-sorting-sheet.md` and the primary document it rests on (with its date), argue that the label is right. Then say what in your policy would have to change if that document changed, the way the EU AI Act's dates changed in July 2026.

**Submission:** Submit your completed worksheet as one file named `skills-lab-8a-lastname.md`. Keep every answer under its task heading, with your filled sheets and your policy pasted into their sections. Include every prompt you sent, the tool and date, and every response you received, pasted exactly, with your Questions & Analysis answers clearly labeled at the end.

### Rubric: Skills Lab 8A

This lab is graded with the standard
[Skills Lab Rubric](../skills-lab-rubric.md): four criteria, five
levels from Mastery to Not Evident. The criteria are Technical
Accuracy and Efficiency, Output Quality, Documentation Quality, and
Analysis, Interpretation, and Response to QUESTION(s). The criteria
and levels are the same everywhere. Your instructor sets the point
values in your course. Check the syllabus and the Canvas rubric
attached to this lab for the values that apply to you.

---

## 8.7 Review Questions 🔄️

1. **Understand:** Explain the difference between a policy and guidance to a new coworker in no more than three sentences, using the NIST AI RMF as your example.

2. **Apply:** A tutoring center's tutors want to paste students' essays, with names and grades, into a chat assistant for feedback ideas. Write the center's "What never goes in" section in three items and a closing rule, and label each item with its kind of rule.

3. **Analyze:** An apartment management office's leasing agent pasted a tenant's late-rent notice, with the tenant's name and unit number, into a free chat assistant on her personal account. The office has no AI policy. Analyze which of the four kinds of rules the paste may have broken, and name the document you would read to settle each one.

4. **Evaluate:** A credit union branch's draft AI Use Policy says, under Approved tools, "Staff may use any AI tool that has a free plan." Judge this rule against what Section 8.2 showed about consumer and business terms, and recommend a replacement rule. Name the one fact about a tool that would change your recommendation.

---

## Further Reading 📖

* [Regulation (EU) 2024/1689, the EU AI Act, consolidated text of July 27, 2026 (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727): The Act as amended by Regulation (EU) 2026/1744, read October 21, 2026. Read Article 5 (prohibited practices), Article 50 (transparency), Annex III (high-risk uses), and Article 113 (the dates).
* [AI Risk Management Framework (NIST)](https://www.nist.gov/itl/ai-risk-management-framework): NIST's page for AI 100-1 (January 26, 2023), the Generative AI Profile, and the revision under way, read October 21, 2026. The four functions are in Section 5 of the PDF.
* [OECD AI Principles (OECD.AI)](https://oecd.ai/en/ai-principles): The principles adopted in May 2019 and updated in May 2024, with the list of 47 adherents, read October 21, 2026.
* [SB26-189, Automated Decision-Making Technology (Colorado General Assembly)](https://leg.colorado.gov/bills/sb26-189): The 2026 law that repeals and reenacts Colorado's 2024 AI act effective January 1, 2027, signed May 14, 2026, read October 21, 2026. The page links SB24-205 and its history.
* [Copyright and Artificial Intelligence (U.S. Copyright Office)](https://www.copyright.gov/ai/): The Office's report in parts, Part 2 (January 29, 2025) and the Part 3 pre-publication version (May 9, 2025), with the *Thaler v. Perlmutter* decision, read October 21, 2026.
* [Student Privacy Policy Office: FERPA (U.S. Department of Education)](https://studentprivacy.ed.gov/ferpa): The FERPA regulations at 34 CFR Part 99 and the Department's guidance, read October 21, 2026. HHS's HIPAA pages for professionals, cited in Section 8.2, are the matching source for health information.

---

## Looking Ahead ⏩

You can now sort a rule by its kind, read a vendor's policy, and write a policy that people can follow. Chapter 9 weighs whether an AI use is worth it at all. You will evaluate a proposed Copperwind use with costs, risks, and workforce impact, and the AI Use Policy you wrote here is one of the things that decision must respect.
