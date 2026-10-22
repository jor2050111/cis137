# Review: Chapter 3, Research, Creative Work, and Responsible Use

Reviewer: Opus subagent, read-only. Date: 2026-10-21.
Chapter: `book/chapters/chapter-03.md` (560 lines). No repo file edited.

## Checker results (run from the repo root)

| Check | Result |
| --- | --- |
| `check_samples_vs_log.py` | 10 sample fences, 0 lines not in log |
| `check_course_structure.py` | OK, 0 errors |
| `check_sentence_length.py` | 384 sentences, avg 14.9, longest 34, 0 flagged |
| `check_readability.py` (extra) | ch03 Flesch 70.9 (ch01 72.4, ch02 69.9) |
| Em dash, prose semicolon, banned word, dash bullet, vendor-name scans (my script, fences stripped) | 0 hits |
| Log vs raw captures (`scratchpad/caps/pN.txt`, `rN.txt`) | all 13 prompts and 13 responses byte-identical to the log |
| Chapter prompt fences vs log prompts | every prompt matches its log entry once `[Step]` lines are removed. Line 221 (image prompt, never sent) and 417 (author's table) are not samples |
| Further Reading (curl, browser UA, today) | all 5 return 200 with the expected page titles |
| Source facts (`scratchpad/src/`) | Liang: 7 detectors, 91 TOEFL essays, 61.22% avg FPR, near-perfect on US 8th grade. Weber-Wulff: 12 public + 2 commercial tools, all below 80%, "neither accurate nor reliable." Copyright Office Part 2: "prompts alone." Gutenberg 58444: 1898, passage verbatim. All confirmed |
| Lead checks re-run today | Maricopa "Heat Reports" page lists the 2025 Heat-Related Deaths Report. WPC page title "NWS HeatRisk." Both claims at lines 80-81 hold |
| Lab dates | Oct 20 2026, Nov 17 2026, Sep 8 2026 are Tuesdays. Mar 2 2026 is a Monday. All consistent |

## BLOCKER

None. Every sample matches the log, and the log matches the raw captures.

## MAJOR

1. **Lines 502, 511-512: the lab runs the privacy check and the Ruth decision after the prompts are sent.** Part 2 Task 1 tells students to supply facts from the brief, which carries Ruth Alvarado's full name and her grandson's name. The privacy check comes later, in Part 3 Task 2, as "the privacy check for every prompt you sent in this lab." The Ruth ruling comes in Part 3 Task 3. That is the exact failure the chapter condemns at line 413 ("The check came after the leak") and line 461 ("before the paste, never after"). The lab grades the habit backwards. Fix: add a Part 1 Task 0 (or open Part 2 with a task) that has students write the two-column plan and decide how Ruth's story will be handled before the first prompt. Turn Part 3 Task 2 into a reconciliation: the plan, what went in, any difference, and the principle behind each item kept out. Add a matching worksheet slot.

2. **Lines 152-168: the Fix It repair changes two things at once, and the log shows the second change may be the real fix.** The repair adds the caveat rule and also raises the limit from 30 to 40 words (line 166 says so). Prompt 5 in the log (same update, no word limit) kept the caveat. So the evidence points to the tight limit as the cause, and the chapter cannot show the caveat rule did the work. Chapter 6's planned Fix It is literally "a revision that changed two things at once" (part-structure line 504), so this chapter models the anti-pattern without naming it. Fix, best option: re-capture the repair with the limit held at "under 30 words" plus the caveat rule, and log it. Fallback: keep it, and add two sentences to Verify. They should say the repair changed two things, that a no-limit run kept the caveat (cite the attempt), and that Chapter 6 shows how to test one change at a time.

3. **Lines 363-376 (log lines 217-233): the food truck sample cuts the top of the response without a `[...]` marker, and the commentary hides what the cut held.** The response opened with a short version that already met the three-part rule. It ended with a note in which the tool flagged the allergy line itself: "Cut it if you'd rather not make that promise on the page." The chapter shows only the full version and then says the disclosure "is no longer honest." The prose at 376 does mention the cut. Still, a reader comes away thinking the first draft failed, while the log shows the tool offered a clean option and labeled its own addition. That misstates what the sample did (brief area 3), and the unmarked leading cut breaks the trim protocol (area 2). Fix: put `[...]` before `**Full version` and show the tool's note line. Then reframe: the tool offered two versions and flagged the promise itself, but the owner still has to choose, and the tightened prompt removes the choice. Or show the short version and teach "pick the version that adds nothing."

4. **Line 21: MLO 3.2 promises a skill the chapter says no one has.** It reads "Distinguish human-made from AI-made content by evidence and disclosure instead of detectors." Section 3.3 teaches that you usually cannot tell by looking (line 264), and that neither a detector nor a chat assistant can. An assessor cannot measure "distinguish." The binding is also off: "decide what a disclosure must say" is taught in 3.4 (line 355), not in 3.2-3.3. Fix, for example: "**3.2 (Analyze):** Analyze a claim that content is AI-made by judging which evidence (process records, disclosure, content credentials, detector scores) can support it, and decide what a disclosure must say (Sections 3.3-3.4)." Then recheck the Part 2 and Part 3 tags.

5. **Lines 130, 132, 150: the Fix It gives away its diagnosis before Diagnose.** The heading says "The Caveat That Vanished." The intro sentence says the update "carried a warning about its own numbers." The Diagnose prompt itself says "that loss." A student only has to repeat the setup. Fix: retitle (for example "The Summary That Read Well"). Cut "The update she pasted carried a warning about its own numbers." Reword Diagnose to "name in one sentence what a volunteer would now believe that the update did not say, and whether that matters more than the missed word limit."

## MINOR

1. **Lines 55 and 168: authoring residue in student prose.** "Here is a research prompt from a cover story" uses style-guide jargon that students will not recognize. "This build needed four different prompts" refers to the authoring session. Fix: "Here is a research prompt from a neighborhood nonprofit." And "Getting this failure took four tries with different prompts, so a clean run proves little."
2. **Line 268: the 1898 passage is quoted without attribution, in the chapter that teaches attribution.** Fix: "from *The Modern Bicycle and Its Accessories* (1898), now in the public domain."
3. **Lines 287-289: the second AI-or-person prompt is never shown.** The log (Prompt 10) sent only the blurb body, joined into one paragraph, without the title and the "(Word count: 120...)" line, which would have given it away. A student re-running it from the chapter would paste the whole blurb. Fix: show the prompt fence, or add "with the title and the word-count line removed."
4. **Line 319: "They can be stripped out when a file is copied" is wrong as written.** A plain file copy keeps embedded metadata. Re-saving, re-encoding, many platform uploads, and screenshots strip it. Fix: "when a file is re-saved, uploaded to some sites, or screenshotted." Also date the vendor-behavior claim "Some tools now attach" ("As of October 2026, some tools attach...").
5. **Line 238: "The line between a helpful narration and a deepfake is the person's consent" oversimplifies.** A narration in a generic synthetic voice is not a deepfake at all. A consented clone can still mislead listeners if it is not disclosed. Fix: "What makes a deepfake harmful is a real person shown doing what they never did, without their consent and without telling the audience. Section 3.4 takes up consent and honesty."
6. **Line 380: the tightened disclosure prompt asks only for "what the AI did and what I did."** That is two of the three parts the chapter just required (line 355). The model added the check on its own, and line 388 credits the prompt. Fix: add "and what I checked" to the prompt and re-capture, or say at line 388 that the tool kept the check even though the prompt did not ask for it.
7. **Line 502: the claim-marking scheme cannot catch a sourced claim that was distorted.** The marks are "the brief, Source A, B, or C, a lead, or NOT SOURCED." A draft that says "a third of our neighbors got these calls" would be marked "Source A," yet it breaks Source A's own caveat ("They do not tell us how common these calls are"). That is the Fix It skill, and the lab never tests it. Fix: add a third mark, CHANGED FROM SOURCE, or a line in Part 2 Task 2: "confirm every caveat in Sources A-C that applies to a claim you kept."
8. **Line 498: "names the one caveat in Source B" assumes a single answer.** Source B carries at least two (caller ID can be faked, a code word works only as a second check). Fix: "names the caveat in Source B you judge most likely to be dropped, and says why." That also admits more than one defensible answer (gate C14).
9. **Line 500: the Part 2 tag "Objectives 3.1 and 3.2" is thin on 3.2.** Part 2 drafts, sources, revises, and checks an image. None of that weighs evidence of AI authorship or settles disclosure content (Q&A 2 does). After the MLO 3.2 rewrite in Major 4, retag Part 2 "3.1 and 3.3" (attribution, the image check), or add one 3.2 task.
10. **Lines 428-429: the admonition carries a required step, and its wording is stale.** "Read both before your first lab" is an instruction (style law: admonitions never carry required steps), and students have already done Labs 1A and 2A. Fix: make it informational ("Your syllabus states...the syllabus wins") and move any required reading into Module Overview or the lab steps.
11. **Line 479: the "From Chapter 2" reach-back goes against the placement table.** Part-structure line 501 lists reach-backs for chapter 3 as "Ch 1," and the law spaces them at about N-2 and N-4. Fix: replace item 4 with a Chapter 1 item, or keep it and update the table, recording why.
12. **Lines 433 and 461: the copyright claim needs its scope and status.** The report's conclusion is "given current generally available technology," and it is agency guidance, not statute or a court ruling (gate G1 asks the prose to separate law from guidance). Line 461 also tacks copyright onto the privacy-check bullet. Fix at 433: "concluded that, with current technology, prompts alone..." and "The report is the Office's guidance, and courts decide individual cases." At 461, split copyright into its own bullet.
13. **Log line 31: lead 2's verification records only HTTP 200s.** Rubric C1 step 4 says a 200 proves reachability, not support. I confirmed today that the WPC page title is "NWS HeatRisk." Still, the log should record what was read on each page (title, what supports the line 81 claim), as it does for lead 3.
14. **Lines 345-349: the five-principles list is not parallel.** Honesty, Privacy, and Harm use "**Term.** Question." Attribution and Consent use "**Term**, definition. Question." Fix: one shape for all five, for example "**Attribution** (giving credit to...). Did I...?"
15. **Voice: the triplets and closing-flourish lines read as machine-made in places.** Triplets at lines 5, 180, 184, and 339. Section-ending maxims at 48, 83, 120, 168, 388, and 426. Chapter 1 does some of this, but chapter 3 does it more often. Fix: break some triplets into two sentences of different length, and end two or three subsections on the content instead of a maxim.
16. **Readability: Flesch 70.9 sits just above the 60-70 band.** Chapter 1 (approved) reads 72.4, so this matches the model. Flag it for Mr. Vega's ruling and do not merge sentences to chase it.
17. **Log header (lines 3-6): the samples came from a Claude CLI capture, not a core-roster tool.** The style guide says samples come "from a real run of a tool on the roster," and the roster lists Claude as 18+ only. This is book-wide (chapter 1's log says the same), not a chapter 3 defect. Carry it as an open item for re-capture before publication.
18. **Lines 467-468: Key Terms lists "research tool" and "image generator."** They are Chapter 1 terms that are neither bolded nor redefined here. Fix: drop them, or check that check_key_terms accepts carried terms by design.
19. **Line 215: "the claim is not true" rests on a one-word gap that depends on the counter.** wc -w gives 121, but "8 a.m. to 11 a.m." counts differently across tools. Fix: "a word counter gives 121. Close, but the tool's claim is a guess you checked, not a fact."

## NIT

1. Line 7: "four tools you can use on any task" names four artifacts (a brief, a piece, a statement, a check). Say "four pieces of work."
2. Line 32: "It cannot promise that those places exist or say what it claims" reads as broken. Use "or that they say what it claims."
3. Lines 417-425: the two-column example leaves out the phone number the tool flagged, adds "the clinic's tone guidelines" (never mentioned before), and wraps the first cell across two lines, which makes the columns hard to read.
4. README lines 37-41: the fictional disclaimer adds words to the canon's verbatim text ("stories," "including every person named..."). Use the canon sentence, then add the extra line.
5. Line 397: "Dr. Okafor" shares a surname with the Copperwind technician Amara Okafor. That is harmless in a clinic cover story, but a different surname avoids confusion across the book family.
6. Lines 142-146: the Fix It symptom output has no capture label ("The response was:"). Chapter 1 does the same, but "The response (captured from a chat assistant, October 2026) was:" costs nothing.
7. Line 540: "its one forbidding rule" is awkward. Use "the one rule that forbids invented facts."
8. Line 551: "Its discussion section explains why every tool scored below 80 percent" is unverified. The paper reports that result. Whether the discussion explains *why* is a stretch. Use "reports why the authors call the tools neither accurate nor reliable."
9. Copperwind shows up only in the intro and the lab. No teaching-section touch exists. That is allowed, but chapter 1 placed its spine in a TIY as well.
10. Line 503: Part 2 Task 2 demands Priya's second fact word for word but never checks the first (date, time, place). Add "and confirm the first fact's date, time, and place match the brief."

## Area-by-area notes

* **Factual accuracy:** detector statistics, the copyright conclusion, C2PA, the passage provenance, the Maricopa and NWS lead checks, and the Further Reading metadata all verify (see the table). The issues are Minor 4, 5, 12, and 19.
* **Samples vs log:** clean, including against the raw capture files. The only trim defect is Major 3's unmarked leading cut.
* **Commentary vs samples:** accurate except Major 3 and Minor 6.
* **Anatomy:** three MLOs (Apply, Analyze, Apply) with section bindings. The CLO block is verbatim. 5 TIYs whose Predicts commit to a test the Run checks. 4 Quick Checks (3.2 Q1 is the one Understand-level item). One Fix It with a real capture. 5 Retrieval items with reach-backs. Lab parts tagged, two Q&A items that cite the log, the short rubric block matching the template, RQs at U/A/An/E on new cases, 5 verified Further Reading links, Looking Ahead in 3 sentences. Heading icons exact, `text` fences only, 10 worked examples, two flagships (lines 57, 188) with 4 step labels each on sentence boundaries.
* **Rigor band:** clears the Rigor step (research brief with checked sources, creative asset, disclosure, privacy check). It stays inside the drift guards (no code, math, training, or metrics). It asks more than a literacy course: lead verification records, caveat preservation, primary studies and a federal agency report, and a manager-ready packet with a cover note. Major 1 is the main threat to the rigor claim, because the lab currently rewards a check made after the fact.
* **Lab packet:** all three named files exist with exact names. Every task has a worksheet slot. No answers leak. The packet is internally consistent (dates, the people named, the five deliverables). Source A and Source B disagree mildly on code words, so more than one position is defensible. The teaching examples do not reuse lab facts. The pack ships no transcripts to evaluate, so no capture requirement applies.
* **Glossary:** all 15 Key Terms resolve (13 in `glossary-additions-03.md`, plus "research tool" and "image generator" in `book/glossary.md`). The definitions name no vendor and do not overlap `glossary-additions-02.md`.

## Verdict

The chapter is close, and it is ready for the professor's review once the five Major items are fixed. None is a blocker. Its evidence is the strongest part: every sample matches the log and the raw captures byte for byte, and every statistic and source claim I checked holds. The anatomy, the glossary, and the style scans are clean. The three most important fixes:

1. Move the privacy check and the decision about Ruth's story to before the first prompt in Skills Lab 3A. Right now the lab grades the after-the-leak method that Section 3.4 condemns.
2. Fix the Fix It. The repair changes two things at once, and the log suggests the raised word limit (not the caveat rule) restored the caveat. Also remove the giveaways in the title, the intro, and the Diagnose.
3. Restore an honest picture of the food truck sample. Mark the leading cut with `[...]`, and say that the tool offered a clean short version and flagged its own added promise. Along with this, rewrite MLO 3.2 so it no longer promises students can "distinguish" AI-made content, which the chapter says no one can.

Findings by severity: BLOCKER 0, MAJOR 5, MINOR 19, NIT 10.
