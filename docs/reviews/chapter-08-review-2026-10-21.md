# Review: Chapter 8, Governance, Privacy, and Content Ownership (Opus, read-only)

Reviewed 2026-10-21. No file edited. Primary documents opened in this
review (my own fetches, not the writer's copies, except where noted):

* EUR-Lex consolidated text 02024R1689-20260727 and the OJ text of
  Regulation (EU) 2024/1689 (built-in browser), and Regulation (EU)
  2026/1744's own EUR-Lex page.
* leg.colorado.gov bill pages for SB24-205, SB25B-004, SB26-189 (curl
  with a browser user agent), plus the SB24-205 and SB26-189 bill PDFs
  (`/bill_files/47770/download`, `/bill_files/116189/download`).
* le.utah.gov: Title 13 Chapters 2 (Part 1 index), 72, 72a, 75, 76, 77,
  78; section 13-77-103; S.B. 226 (2025) enrolled PDF.
* copyright.gov/ai page; the writer's Part 2, Part 3, and Thaler text
  extracts (grep only); eCFR 37 CFR 202.1.
* NIST AI RMF page; the writer's AI 100-1 text (grep); oecd.ai
  principles page; studentprivacy.ed.gov "What is FERPA?"; HHS
  covered-entities page (browser).
* Vendor pages for the Tool check: OpenAI "Data controls in ChatGPT",
  Gemini Apps Privacy Hub, Microsoft "Privacy FAQ for Microsoft
  Copilot" (browser).

Tool runs (repo root): `check_samples_vs_log.py` 9 blocks, 0 lines not
in log; `check_course_structure.py` OK, 0 errors; `check_sentence_length.py`
466 sentences, avg 14.4, none flagged; `check_style.py` 0 hits. Log
header carries the probe answer.

## Confirmed claims (G1)

These hold against the primary documents as of 2026-10-21:

* EU AI Act: Regulation (EU) 2026/1744 "of 8 July 2026", OJ L 1744,
  24.7.2026, titled "(Digital Omnibus on AI)", is the one amending act
  (M1) in the consolidated text of 27.07.2026. Consolidated Art. 113:
  Chapters I-II from 2 Feb 2025 except new Art. 5(1)(ba), (bb), (1a),
  (1b) from 2 Dec 2026; Chapter III Sections 1-3 from 2 Dec 2027
  (Annex III) and 2 Aug 2028 (Annex I). Art. 111(4): pre-existing
  generators comply with Art. 50(2) by 2 Dec 2026. Art. 5(1)(f), Art.
  2(1)(c), Annex III points 3 and 4(a), Art. 99(3) (EUR 35 000 000 or
  7 %) all read as the chapter says. "Minimal risk" appears in neither
  the consolidated text nor the OJ text, and "limited risk" appears
  only as "limited risks" in a recital, not as a tier label, so line 66
  holds. Article 4 (AI literacy) still binds providers and deployers
  after M1, so the sample's Art. 4 line is not stale.
* Colorado: SB24-205 approved May 17, 2024, duties "on and after
  February 1, 2026", affirmative defense tied to a recognized framework.
  SB25B-004 approved August 28, 2025, moves requirements to June 30,
  2026. SB26-189 Governor signed 05/14/2026, "repeals and reenacts
  those provisions", consequential decisions include education,
  employment, housing, lending. Bill text Section 5: "this act takes
  effect January 1, 2027" and "applies to consequential decisions made
  on or after January 1, 2027."
* Utah: 13-75 is the "Franchise Protection Act (Effective 3/17/2025)";
  13-2-12 is gone from the Chapter 2 Part 1 index; S.B. 226 (2025)
  "REPEALS: 13-2-12 (Effective 05/07/25)". (But see B1.)
* Copyright Office page: Part 1 July 31, 2024; Part 2 January 29, 2025;
  Part 3 pre-publication May 9, 2025, "A final version of Part 3 will be
  published in the future." Thaler decision linked on the page. Part 2
  and Part 3 quotes and "Decided March 18, 2025" match the text
  extracts.
* NIST: "Released on January 26, 2023"; AI 600-1 July 26, 2024; "The AI
  RMF 1.0 is being revised as part of the White House AI Action Plan";
  the "voluntary, rights-preserving..." quote and "cross-cutting" are in
  AI 100-1.
* OECD: "47 adherents", "initially adopted in 2019 and updated in May
  2024", the five values-based principles as listed.
* FERPA: transfer at 18 or postsecondary entry; 20 U.S.C. § 1232g; 34
  CFR Part 99.
* HHS: "only if they transmit any information in an electronic form...",
  "must have a written business associate contract or other
  arrangement", "Content last reviewed August 21, 2024", decision tool
  linked.
* Tool check: every vendor statement in the callout matches the live
  pages (OpenAI setting name, temporary chats 30 days, managed
  workspaces not trained on by default; Gemini Privacy Notice "Last
  updated: October 13, 2026", 18-month default, reviewed chats up to
  three years, work or school accounts "may be subject to different
  data handling terms"; Microsoft opt-out, 18 months, Entra ID
  exclusion).

## BLOCKER

**B1. Line 406 (Fix It 8.1 Repair): the book tells students Utah's AI
disclosure rule was repealed. It was renumbered and is in force.**
The Repair says Title 13, Chapter 75 "is the Franchise Protection Act,
not an AI law" and that "The section that held Utah's generative AI
disclosure rule, 13-2-12, now reads 'Repealed 5/7/2025.'" Both facts are
literally true and together they mislead. S.B. 226 (2025 General
Session, enrolled copy on le.utah.gov) repealed 13-2-12 and in the same
bill enacted the disclosure rule as 13-75-101 to 13-75-106, effective
5/7/25. Because 13-75 was already taken, the codifiers moved it: Utah
Code Title 13, Chapter 77 is now "Generative Artificial Intelligence --
Consumer Disclosures and Enforcement (Effective 5/7/2025)", and section
13-77-103 "Required disclosures" carries the note "Technically
renumbered to avoid duplication of newly enacted code." 13-77-103(1)
requires a supplier to disclose generative AI when an individual
clearly asks, and (2) requires proactive disclosure in regulated
occupations for high-risk interactions. That is exactly what the
captured Utah row says. A student who reads the Repair concludes that
Utah dropped its rule, the reverse of the law. The same misreading is
in the log (Prompt 6 observation line 191, Prompt 8 observation line
268, Verification notes line 587) and in notes-08.md.
**Fix:** rewrite the Repair's Utah sentence along these lines: "The
Utah row's 'Chapter 75' is the number S.B. 226 gave the rule in 2025.
The code moved it, and it now sits at Title 13, Chapter 77, section
13-77-103 (le.utah.gov, read October 21, 2026). Title 13, Chapter 75 is
the Franchise Protection Act." Correct the three log observations and
the notes so Chapter 9 and Part IV writers do not inherit the error.

**B2. Fix It 8.1 no longer shows a real, proven failure.** The writer
brief's Fix It candidate is a response that "names a statute, act, or
section you then prove does not exist." Every citation in the Prompt 8
table exists. Utah: see B1 (the bill's number, since renumbered).
Colorado: C.R.S. § 6-1-1704 in SB24-205 (bill PDF) is titled
"Disclosure of an artificial intelligence system to consumer" and
requires a deployer of a consumer-facing AI system to disclose it,
which is what the row says. SB26-189 does not take effect until January
1, 2027 (see M1), and it reenacts part 17 with a 6-1-1704 of its own.
So the chapter frames a mostly accurate, well-hedged answer as a
failure, and the Repair "fixes" errors the model did not make. The real
errors in Prompt 8 are smaller: the Colorado row says the section
"Mainly applies to high-risk systems" when 6-1-1704 reaches any
consumer-facing AI system, and the Utah row files the disclosure rule
under the "AI Policy Act" (Chapter 72) when it lives in its own chapter
(77). **Fix:** either (a) recapture until a response names a citation
that does not exist (the spec's candidate), log the search, and teach
from that, or (b) keep Prompt 8 and rewrite Symptom, Diagnose, and
Repair around what failed: a citation that was the bill's number, not
the code's, and a relevance column that misstated scope. Under (b) the
diagnosis still holds (the prompt demanded a section for every row), but
the prose must stop calling the citations wrong.

## MAJOR

**M1. Lines 43, 142, 148, 406: Colorado's replacement is stated as done
when SB26-189 is not yet in effect.** Line 43 says the 2024 act "has
since been replaced." Line 142 says a policy citing it by section "would
now cite text that no longer stands." Quick Check 8.1 item 3 (line 148)
says Colorado "replaced its 2024 law before it took effect." Line 406
says SB26-189 "has since repealed and reenacted" the cited section.
SB26-189's Section 5 says the act "takes effect January 1, 2027" (with
a few subsections effective on passage) and "applies to consequential
decisions made on or after January 1, 2027." SB25B-004 set SB24-205's
requirements for June 30, 2026. Whether SB24-205's duties ran from June
30 to December 31, 2026 is unverified (I found no primary document
settling the interim, and secondary reports mention litigation the
chapter rightly avoids). As written, the chapter states a status the
documents do not support. **Fix:** say "SB26-189, signed May 14, 2026,
repeals and reenacts those provisions effective January 1, 2027." Change
line 142 to "A policy that cited the 2024 act by section will cite
rewritten text on January 1, 2027." Change Quick Check 8.1 item 3 to
"Colorado rewrote its 2024 law before its duties began" (SB26-189 was
signed before the June 30, 2026 start). Mark the interim question
unverified in the log.

**M2. Line 299: the commentary endorses the claim that the theater's
"title, dates" are registrable.** The sample says "Your title, dates,
text, and the layout/arrangement you created are human-authored and
registrable," and the chapter answers that "The title, dates, and
layout as human-made additions match its point that a person's own
expression stays protected." 37 CFR 202.1(a) (eCFR, read 2026-10-21)
lists "Words and short phrases such as names, titles, and slogans" as
"not subject to copyright." A show title and dates are not protected
expression. Only the selection and arrangement can be. This matters
beyond the example: lab Part 2 Task 3 asks what Copperwind "can and
cannot claim to own" in a flyer that will carry Copperwind's name, and
students will copy the chapter's reading. **Fix:** mark that line of
the sample as the slip it is: "The layout and arrangement are the
theater's own expression. The title and dates are not. Copyright
regulations exclude names, titles, and short phrases (37 CFR 202.1,
read October 21, 2026)." Add the check to the log's Prompt 5
observation.

## MINOR

**m1. Line 43: the Colorado defense is simplified past accuracy.** The
SB24-205 summary gives the affirmative defense only if the party
complies with a framework "that the act or the attorney general
designates" and also "takes specified measures to discover and correct
violations." **Fix:** "gave a defense to companies that followed a
designated AI risk management framework and fixed the violations they
found."

**m2. Fix It 8.1 Repair (lines 406-409): the "one change" changes
several things.** The new sentence drops the section number, drops the
one-sentence summary of what each law requires, adds a website, and
adds a confidence rating. It is one sentence, but the repair law asks
for one change. **Fix:** either keep "one sentence on what it requires"
in the repaired prompt, or say in the prose that the one sentence
swaps a demand for citations with a demand for sources and doubt, and
treat that as the single change.

**m3. Line 249: commentary points to text the student cannot see.**
"The safer option, a template with no identifiers, is Chapter 3's
privacy check in action" refers to the "Safer options" list, which the
shown sample trims (the chapter shows lines 1-3 only). **Fix:** show
the first "Safer options" bullet with a `[...]` after it, or cut the
sentence.

**m4. Retrieval item 3 (line 495): "say which one the parks department
draft got wrong" has two answers.** The audit (line 374) found two
failures: Disclosure answered the wrong question, and Review date
invented a period. **Fix:** "say which section the parks department
draft failed outright, and why."

**m5. Line 426 Verify: the Colorado check stops one step short.** It
confirms SB26-189 exists but does not note that the repaired row's
summary ("covers 'high-risk' AI used in consequential decisions")
misses SB24-205's general consumer-facing disclosure duty. With B2's
rewrite this becomes a teachable second lead. **Fix:** add one sentence
after the SB26-189 line, or drop it if B2 is resolved by recapture.

## NIT

**n1. Line 235 and the HIPAA glossary entry:** "They apply to health
care providers..." states coverage without HHS's electronic-transaction
condition, which line 249 then adds. The glossary entry keeps the
unconditioned version. **Fix:** add "that bill electronically" or
"most" to the glossary line, or let line 235 say "certain health care
providers."

**n2. Line 62:** "AI that serves as a safety part of regulated
products (Annex I)" omits Art. 6(1)'s second case, AI that is itself an
Annex I product needing third-party conformity assessment. **Fix:**
"AI that is, or is a safety part of, a product regulated under Annex I."

**n3. City parks department (Section 8.4, Retrieval 3, Review date QC)**
is on the Part III cover-story list, but Chapter 3 Review Question 2
(chapter-03.md line 542) already used "A city parks department intern."
**Fix:** rule it fine (Part III list) or swap to a library branch.

**n4. Line 68:** "The law changed under it." closes the paragraph as a
maxim. **Fix:** cut it. The preceding sentence carries the point.
Separately, *Thaler v. Perlmutter*'s Supreme Court petition status is
unverified (the chapter makes no claim about it, so no fix unless a
ruling issued).

## Other checks that passed

* Anatomy: three MLOs (Categorize, Examine at Analyze; Recommend and
  justify at Evaluate, all on the Bloom's list) with section bindings;
  CLO block verbatim; CLO 4 assessed by QC 8.1 item 3 and Q&A 2; five
  Try It Yourself blocks with committed predictions; four Quick
  Checks; five Retrieval items with Chapter 6 and Chapter 4
  reach-backs per the placement table; four Review Questions at the
  four levels on new cases; six Further Reading links, dated; heading
  icons match; only `text` fences; two flagship prompts with step
  labels at sentence boundaries; nine worked examples.
* Fading: TIY 8.5 is the one completion prompt, gaps only inside the
  `text` fence, Run says to fill from the chapter, Explain compares
  with Prompt 12, which is logged.
* Samples: every sample matches the log; quoted counts (269 words, 123
  words, "Three of the four match", the single-to-double quote change)
  match the log observations.
* Shared names: four kinds of rules and the seven AI Use Policy
  sections verbatim and in order; Copperwind facts match Part III canon
  (5 and 3 technicians, operations manager signs, Mei Lin's cell
  602-555-0177 marked private, the VPN rule, all clients in Arizona).
* Packet: every named file exists; worksheet has a slot for every task
  and both Q&A items; privacy plan precedes the first prompt; no
  answers leak; no vendor named; no AI response shipped.
* Voice: second person, no em dashes, no semicolons, no banned words,
  vendor names only inside the Tool check; voice and density close to
  Chapter 3.
* Glossary: all 13 Key Terms resolve in the additions file, all on the
  Chapter 8 ownership list, none restates an existing entry.

## Verdict

Not ready for the professor's review. The chapter's EU, NIST, OECD,
FERPA, HHS, Copyright Office, and vendor claims all hold against the
primary documents. The EU Digital Omnibus dates in particular are right
to the day. But the Fix It, the one place the chapter teaches students
to catch a tool's bad legal citation, rests on the book's own misreading:
Utah's disclosure rule was renumbered to 13-77-103, not repealed, and
Colorado's 6-1-1704 is a real section of a law whose replacement does
not take effect until January 1, 2027. The three most important fixes:
(1) correct the Utah facts in the Repair, the log, and the notes (B1);
(2) rebuild Fix It 8.1 around a failure that is real, by recapture or by
re-diagnosing Prompt 8 honestly (B2); (3) restate Colorado's status as
"signed May 14, 2026, effective January 1, 2027" everywhere it appears
(M1). Fix the title-and-dates copyright slip (M2) in the same pass,
because the lab sends students straight to that question.

Findings by severity: BLOCKER 2, MAJOR 2, MINOR 5, NIT 4.
