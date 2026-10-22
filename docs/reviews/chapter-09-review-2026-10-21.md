# Review: Chapter 9, AI in Business and Society (read-only, Opus reviewer)

Reviewed 2026-10-21 against review_brief_part3.md. No file edited.
Sources re-fetched independently with a browser user agent into
`scratchpad/rev09src/` (all 200): NBER w31161, HBS 24-013, the CRT
decision iframe text, the FEDS Note, the Census story, the Canaries page,
the Reuters Institute DNR 2026 summary, the IEA report and executive
summary, Pew, the 2026 AI Index landing page, its Economy chapter page,
and the full 2026 AI Index PDF, the Chamber release, arXiv 2507.13575,
both Goldman Sachs pages, and the WEF Future of Jobs Report 2025 PDF.

Checkers: `check_samples_vs_log.py` 10 blocks, 0 lines not in log.
`check_course_structure.py` OK, 0 errors. `check_sentence_length.py`
426 sentences, longest 34, 0 flagged. `check_style.py` (chapter and packet)
0 hits. The sample checker only tests that shown lines exist in the log.
It does not catch unmarked omissions, so I also walked each block line
by line (see B2).

## BLOCKER

**B1. The Fix It's Repair and Verify endorse a false claim about the WEF report (lines 319, 336, 339; log Prompt 6 and Prompt 10 notes, verification bullet "World Economic Forum").**
The chapter (via the repaired response it praises) says the WEF report
covers "all causes of change, not AI alone, so they don't meet your
AI-specific requirement." The Verify then concludes the memo "can no
longer say 'eliminated,' because no checked source supports that word."
The same WEF PDF, in its "Technological change" passage (the
macrotrend section, plain-text line ~2321 of `pdftotext`), says: "trends
in AI and information processing technology are expected to create 11
million jobs, while simultaneously displacing 9 million others, more
than any other technology trend." So the report does carry an
AI-specific displacement forecast for 2025-2030. The repaired response's
headline ("I don't know of a credible source that forecasts how many
jobs AI will eliminate over the next five years") is itself a fluent,
unflagged miss of the document the Diagnose tells students to open. A
student who follows the Diagnose will find the 9 million and conclude
the book is wrong. This is an unsupported source-linked claim (G1 fail).
The symptom itself is real and proven (the 92 million is churn from all
macrotrends, and the response pinned it on "automation and technological
change"). Only the repair narrative breaks.
Fix: keep Prompt 6 as the symptom. It gets stronger, because the model
skipped the AI-specific figure sitting in the same report and reached for
the headline. Rewrite Repair and Verify: (a) name the report's own
AI-specific line (9 million displaced, 11 million created, by employer
expectation, gross, 2025-2030). (b) Mark the repaired response's WEF
sentence Contradicted in the Verify, so the Fix It shows a second
check. (c) Change the last two sentences of Verify to something like
"Her memo can say 'exposed' with the Goldman Sachs source, or
'employers expect AI to displace about 9 million jobs and create about
11 million worldwide by 2030' with the WEF source. It cannot say AI will
eliminate 92 million." Also correct the log's Prompt 10 observation
("which matches the check of Prompt 6") and add the 9 million quote to
the WEF verification bullet.

**B2. An unmarked cut in the flagship Use Evaluation sample (lines 176-178; log Prompt 4).**
Under "**2. Time saved**" the chapter shows the Number line and then the
Missing line. The log has a "- **Meaning:** If the pilot holds,
light-edit drafts could cut nearly half of your weekly summary-writing
time, before subtracting the cost of failures." line between them. It
was removed with no `[...]`. The brief rules any difference beyond a
`[...]` trim a BLOCKER. The checker cannot see it.
Fix: insert `[...]` between the Number and Missing lines, or restore the
Meaning line.

## MAJOR

**M1. The Air Canada case overstates the ruling's legal reach (line 196).**
"...a public ruling that a business answers for what its chatbot tells
customers, and that ruling applies to every first reply an AI drafts."
The decision is a British Columbia Civil Resolution Tribunal small-claims
decision (CRT iframe: "Collection Small Claims Decisions", "Decision type
Final Decision"). It binds no court or business in Arizona. Students
learned in Chapter 8 to tell law from policy, guidance, and ethics, and
this sentence reads as a binding legal rule (G1: "distinguish law,
policy, ethics, and guidance"). The writer's notes say the case is "not
... law that binds Copperwind", but the prose says otherwise.
Fix: "The money was small. The error cost was a public ruling, from a
small-claims tribunal in British Columbia, that a business answers for
what its chatbot tells customers. It binds no court in Arizona, but it
is the principle to plan for whenever an AI drafts a first reply."

**M2. "The number holds" misreads the BTOS question change (line 244; log Prompt 5).**
The response says "About 18% of U.S. businesses report using AI in
producing goods or services." The FEDS Note puts about 18 percent at
year-end 2025, which is after the November 2025 revision to "any of its
business functions." Under the old "producing goods or services"
question, the note says the rate "had grown by 68 percent (3.9
percentage points) over the prior year." That puts the old-question rate
near 10 percent (my arithmetic from the note's two figures, so treat the
exact value as derived). So the response pairs the new number with the
old definition. The claim as worded does not hold. This is the same
real-number, wrong-claim failure the Fix It teaches, and the chapter
passes it as "the number holds, the wording is dated."
Fix: "The number and the description come from two different questions.
About 18 percent is the share under the November 2025 question, AI use
'in any business function.' Under the older 'producing goods or
services' wording the note's figures put the rate near 10 percent. As
worded, the claim is Contradicted. With the question corrected, the
number holds." Update the log observation to match.

## MINOR

**m1. The 88 percent line is left Unverifiable when the population is one click away (lines 252, 256; QC 9.3 item 1).**
The AI Index Economy chapter page says "up to 88% of surveyed
organizations," and the full PDF, section 4.3 "Corporate AI Adoption,"
says the figure is the share "of respondents [who] reported that their
organization uses AI in at least one business function," drawn from
"McKinsey & Company's annual State of AI surveys," global, self-reported,
and "directional rather than comprehensive." The chapter's own Question
4 asks students to open the primary source. The writer's notes flag that
this was not opened.
Fix: in the table, "Respondents to a global executive survey (McKinsey)
who say their organization uses AI in at least one function." In the
paragraph, give the verdict "Holds for survey respondents, does not fit
a 30-person company." That is a stronger lesson than Unverifiable. The
naming rule probably calls for "a global consulting firm's survey."

**m2. The misinformation row measures concern, not misinformation, and not AI (line 358).**
The DNR figure is stated concern about "fake news" online in general.
The row sits under a definition that ties misinformation to generative
AI (line 352), and its "What it measured" column gives only the sample.
Fix: "What it measured: people's stated concern about what is real
online, 97,520 people in 48 markets. Not how much misinformation
exists, and not AI-made content."

**m3. The Canaries interpretation drops the authors' causal caveat (line 362).**
The authors write that the findings are "early, descriptive indicators
... rather than causal estimates." The sentence "That is augmentation
showing up in payroll data" reads as causal.
Fix: "That pattern fits augmentation, though the authors call their
findings early, descriptive indicators, not proof of cause."

**m4. "440 minutes is the most the tool could save" is not a true upper bound (line 186).**
The 6 rewrites and 2 caught drafts could cost more time, or less, than 8
minutes each. The response's own wording is right: "a gross figure, not
a net one."
Fix: "so 440 minutes counts only the light-edit drafts. It is a gross
figure, and the net saving is unknown until the rewrites are timed."

**m5. The Fix It repair bundles four asks into "one change" (lines 319-323).**
The added sentence asks for an AI-specific source, its publisher, title,
and date, what the number does not measure, and the model's confidence.
That fits the spec ("require a checkable source and the model's doubt"),
but Chapter 6's Fix It taught "a revision that changed two things at
once," and a careful student will see the tension. The Verify does not
try to credit any single ask.
Fix: add one sentence saying the change is one requirement (a source the
reader can open, plus its limits), so the result is credited to that one
sentence as a whole. Or trim the added sentence to the source requirement
and the doubt.

**m6. A benchmark claim sits outside a dated callout (line 279).**
"Several frontier models now meet or exceed human baselines on
multimodal reasoning" is a benchmark result stated as plain prose, with
no date and no "someone else's test" caveat. The drift guard says
sourced evidence and pilots, not benchmarks, and the spec puts trends in
refreshable callouts.
Fix: move it into the following Trend check callout with "on published
tests" and the 2026 AI Index name, or cut it and let the clock-reading
callout carry the multimodal trend.

**m7. A prose count does not match its list (line 446).**
"Three things miss," then four items: the word count, the unsourced
Risk and Workforce paragraphs, the additions, and "Error cost gives a
rate again."
Fix: "Four things miss," or fold the error-cost point into the opening
sentence.

**m8. The glossary definition of workforce impact differs from the chapter's (glossary-additions-09.md line 23 vs. chapter line 145).**
The glossary adds "and whether any job is at risk." The chapter
definition stops at "who answers for an error."
Fix: make the two match. Adding the clause to the chapter suits the
augmentation-versus-replacement sentence that follows it.

## NIT

* n1. Line 357: the Pew figure (January 15, 2025, fieldwork fall 2024)
  is the oldest row in a table framed as current. Whether Pew has
  published a newer teen survey is unverified. Worth a check before
  publication.
* n2. Line 287: the on-device callout cites v1 (July 2025). arXiv shows
  v3, revised August 27, 2025. "July 2025" is still the submission date,
  so this is fine. Consider a 2026 source for an October 2026 trend
  callout.
* n3. Line 339: the GS report page byline reads "By Jan Hatzius and
  others." The authors Briggs and Kodnani appear in the title
  parenthetical and on the firm's article. The claim holds. "Shows that
  title, with Briggs and Kodnani named in it" would be exact.
* n4. Questions & Analysis Q1 asks students to quote their Use
  Evaluation sheet, not a prompt-log entry. Q2 cites the logged audit.
  This probably satisfies "cite their own log." Adding "and the prompt
  log entry behind it" to Q1 would close the gap.
* n5. Closing-maxim lines: 93 ("A person still owns what the owner
  reads."), 315 ("It reads like the best kind of answer."), and 396.
  Trim one or two.
* n6. Line 118 quotes "jagged technological frontier." The HBS abstract
  says "jagged technology frontier" (the title says "Technological").
  Either works. Cite the title if keeping the quote marks.

## Checks that passed

* G1 figures verified as stated: NBER 31161 (5,179 agents, 14 percent,
  34 percent, "minimal impact," sentiment and retention, April 2023,
  revised November 2023, QJE 140(2)). HBS 24-013 (758 workers, 18 tasks,
  12.2 percent, 25.1 percent, 19 percent, September 2023). Moffatt
  (February 14, 2024, para 2, the para 27 quotes, para 28, $812.02 at
  para 44). The FEDS Note (Allen, April 3, 2026, 18, 41, and 78
  percent, "sampling distributions and units of analysis," best source
  and upper bound). The Census story (May 26, 2026, 17 to 20 percent,
  37 percent at 250 or more employees, under 20 percent at four or
  fewer, the November revision). Canaries (revised August 12, 2026, 19
  percent, ages 22-25, "no evidence of widespread...," reduced hiring,
  "flat or rising," ADP through June 2026). Pew (26 percent, 13
  percent, 1,391 teens, fall 2024). DNR 2026 (62 percent, up 4pp,
  97,520, 48 markets, June 16, 2026). IEA (415 TWh, about 1.5 percent,
  about 945 TWh by 2030, AI the most important driver, April 10, 2025).
  AI Index (88 percent, 12 to about 66 percent on OSWorld, 1 in 3,
  50.1 percent). The Chamber (58 percent, August 18, 2025). GS (title,
  26 March 2023, 300 million exposed). WEF (92 million, 170 million,
  78 million net, over 1,000 employers, the five drivers, January
  2025).
* Every sample line appears in the log, apart from the omission in B2.
  Both flagship prompts minus their [Step] lines equal Prompts 4 and 12.
  Step labels sit on sentence boundaries. The probe answer is in the
  log header. Word counts hold (325 for the memo, 279 for the repair).
* Arithmetic holds: tutoring center ($100, 5 minutes, 88 summaries, 440
  minutes, 960 minutes) and the QC 9.2 key (480 minutes).
* Anatomy: 3 MLOs (Distinguish at Analyze, Assess and Judge at
  Evaluate), each bound to sections. The CLO block is verbatim. 5 TIY, 4
  Quick Checks, 1 Fix It (the title does not name the diagnosis, the
  Diagnose holds back the answer). 5 Retrieval items, reaching back to
  Chapters 7 and 5 as the table lists. The rubric block, 4 Review
  Questions, 6 Further Reading links (all 200), and Looking Ahead are
  present. 10 worked examples. Only `text` fences. TIY 9.5 is
  problem-first, and the chapter has no completion prompt.
* Packet: every named file exists. Every task has a worksheet slot. No
  answer leaks. No captured response ships. The privacy plan comes
  first. No vendor is named. Pilot numbers match the Part III Copperwind
  facts exactly: 5 and 3 technicians, 160 tickets a week, 30 minutes,
  Monday to Friday 7 a.m. to 6 p.m., 6 minutes by hand, 40/31/7/2,
  about 2 minutes, \$30 per user per month, the hire "either way," the
  two caught steps, the VPN routing rule, owner and operations manager
  by role.
* Shared names (the Accuracy Audit verdicts, the four kinds of rules,
  the seven AI Use Policy sections, the Use Evaluation factors in order,
  the Memo fields) are used verbatim. Cover stories are new. The
  glossary additions are within ownership and vendor-free.

## Verdict

Chapter 9 is close but not ready for the professor. Its sourcing is
mostly excellent: nearly every figure and date matched the document I
opened. The structure, packet, Copperwind facts, and voice are clean.
But the chapter about checking what a source says fails that check in
its own Fix It, and the Fix It is the chapter's centerpiece. The three
most important fixes:

1. Rewrite the Fix It Repair and Verify (B1). The WEF report does give
   an AI-specific forecast (9 million displaced, 11 million created by
   2030), so the praised repair response and the "no checked source
   supports that word" conclusion are wrong against the document the
   Diagnose sends students to.
2. Restore or mark the dropped Meaning line in the flagship Use
   Evaluation sample (B2).
3. Correct the two characterizations that misstate what a source says
   or binds: the Air Canada sentence that makes a BC small-claims ruling
   apply "to every first reply an AI drafts" (M1), and the BTOS "number
   holds" verdict that pairs the post-revision 18 percent with the
   pre-revision question (M2).

Counts: BLOCKER 2, MAJOR 2, MINOR 8, NIT 6.
