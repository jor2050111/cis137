# Review: Chapter 2, How Generative AI Works and Where It Fails

Reviewer: Opus subagent, read-only. Date: 2026-10-21.
File reviewed: `book/chapters/chapter-02.md` (571 lines).

## Checker results (run from the repo root)

* `check_samples_vs_log.py`: 13 sample fences, 0 lines not in log.
* `check_course_structure.py`: OK, 0 errors.
* `check_sentence_length.py`: 400 sentences, average 15.2 words, longest 34, 0 flagged.
* `check_readability.py`: chapter-02 Flesch 69.9 (chapter 1 is 72.4).
* `check_key_terms.py` (with book/glossary.md): 7 Key Terms, 0 missing, 0 orphan bold terms.
* Greps: 0 em dashes, 0 prose semicolons, 0 banned words or filler, 0 vendor names, only `text` fences, no dash bullets.
* Packet: `copperwind-client-update.txt` is byte-identical to the Prompt 20 input in the log. The summary in `copperwind-ai-summary.txt` is identical to the Prompt 20 response. Every weekday in the client update matches its 2026 date.
* URLs (curl on 2026-10-21, my own run): all four Further Reading links return 200. arXiv API confirms the titles and first authors (Kalai, Sharma, Magesh). The Morton DOI in the Fix It returns 404, the Thompson DOI returns 302, and Morton's real DOI (10.3102/01623737221097420) returns 302. Crossref confirms Morton online 2022-06-20 and print 2023-03, volume 45, issue 1.
* By eye: every sample matches the log apart from `[...]` trims. Prompts 3-7 are logged FAILED ATTEMPTS that were re-sent as 8-12. Prompts 14 and 15 are documented two-turn captures (`claude -p`, then `--resume`, with session ids). I treated both as legitimate. I found no invented or edited response.

## BLOCKER

None.

## MAJOR

1. **Line 20, MLO 2.2: the verb is below its tag.** "Classify" is listed under Understand in the course's own `docs/blooms-taxonomy-reference.md` (lines 48 and 210), but the MLO is tagged Analyze. CLAUDE.md says Understand is never an MLO level. Fix: "**2.2 (Analyze):** Attribute a model's errors (fabrication, staleness, omission, agreement under pressure) to the mechanism that produced each one, and name the check that catches it (Section 2.3)." Attributing is an Analyze process.

2. **Line 344, Fix It Verify undercounts what the sample itself flagged.** The Verify step says the repaired paragraph "still contains one general claim ... that neither citation supports." The response's own doubt list (log lines 375-381) flags at least three paragraph claims: "some studies report small attendance gains," the appointments-and-errands explanation, and "Neither reports sharp attendance drops." The log also never records reading either paper's findings, so "neither citation supports" is unverified there. Crossref's abstract for Morton does settle it, and it gives a sharper lesson: Morton found "no detectable effect on ... attendance," so the citation contradicts the paragraph's framing of attendance gains. Fix: log the Crossref abstract check. Then rewrite Verify along these lines: "The repaired paragraph still carries claims the response itself could not tie to either study, and the Morton abstract reports no detectable effect on attendance at all. The repair made the failure visible. It did not make the paragraph true."

3. **Part 3 premise (lines 496, 518, and the summary file) breaks the course's own privacy rule without comment.** A Deskside technician pasted a client's full move update into a chat assistant. The update holds the client's budget, schedule, staff counts, VPN plans, and server-disposal plans. Mei Lin wants the summary forwarded, and no task asks whether the paste was allowed. Chapter 1's Q&A 1 flags this exact pattern as the pilot's main risk (item G: technicians drafting client email on their own accounts), and fluency habit 3 says "Protect what is not yours to share." Review Question 4 in this chapter applies the rule, so the omission reads as an oversight. Fix: give Mei Lin's note one line saying the technician used Copperwind's approved pilot tool. Or extend Task 5: "and whether pasting the client's update into the tool was within Copperwind's rule." Either way, add a sentence that the lab files are fictional, so students may paste them.

4. **CLO 2 is claimed but never assessed (lines 23-26).** The alignment block quotes CLO 2 (Differentiate the major types of AI). No MLO, Quick Check, lab task, Retrieval item, or Review Question asks the student to tell types of AI apart. The closest content is the "Images and Other Modes" subsection, which has no assessment. Rubric C4 needs every link in the chain. Fix: add one assessed item. For example, a Quick Check 2.4 item: "Compare how a language model and an image generator each produce output, and name one failure each one's mechanism predicts." Or add that clause to MLO 2.1 and cite Section 2.4.

## MINOR

1. **Line 228: "whenever" overclaims.** "A model that predicts likely text will produce a likely-looking citation whenever the real one is not a strong pattern." In Prompts 16 and 17 of the chapter's own log, the model refused to invent links. Fix: "can produce."

2. **Line 312: "the one detail the model could not know."** The same response gave a correct Thompson DOI, so the claim contradicts the sample. Fix: "the one detail the model could not reliably recall."

3. **Line 226: the table states the cause of sycophancy flatly.** The table says "Fine-tuning rewarded answers people liked." Line 248 hedges ("partly"), as the 2023 study does. Fix: "Training on people's ratings can reward agreement."

4. **Line 157 and TIY 2.2 Prompt B (line 193).** "At most one of those answers can be right" fails on the very fact the TIY chooses. Colorado touches Arizona only at the Four Corners point, so "four states" and "five states" are both defensible answers. A changed answer may then reflect a definition, not chance. Fix: change line 157 to "If a factual question gets answers that conflict ..." Then either pick an unambiguous fact or have students note the Four Corners question in the Run step.

5. **Rigor Band: the field's own vocabulary is missing.** The chapter never names pretraining or reinforcement learning from human feedback (RLHF), the field's terms for the two training stages. It folds ratings-based training into "fine-tuning" (lines 40, 248). It also never says where knowledge cutoffs are published (model cards and vendor docs). The Rigor Band asks for the field's real vocabulary and primary documents, defined on first use. Fix: name RLHF once in Section 2.1 with a plain definition and a glossary entry. In the line 133 Tool check, point to the tool's model card or help page as the place to find its cutoff.

6. **Lines 133 and 499: required steps sit inside admonitions.** "Your prompt log should say which features were on" and "note that in your worksheet next to each prompt" are both requirements. The worksheet header already says this. Fix: move the requirement into the Starter files paragraph and the TIY Run steps, and keep the callouts informational.

7. **TIY 2.1 (lines 84-88) assumes the tool cannot search.** The district core tool on the roster may ground its answers in web search by default (unverified). If it does, the local-business question comes back right and the Predict loses its point. TIY 2.4 handles this in its Explain step. TIY 2.1 does not. Fix: add "note whether the tool searched the web" to the Run step and one clause to the Explain step.

8. **Most failure claims rest on assertion, not captures.** Of the logged failure probes, the World Cup prompt flagged its cutoff, Arizona held twice, the Python prompt hedged, two citation prompts declined, and the Fix It response warned. Silent staleness and folding under pressure are described but never shown. Fix: add one sentence telling students that most of the logged probes behaved well, and why that does not make the response trustworthy. Better, capture a fold on a weak-pattern fact.

9. **Line 241 and the log: an unverified sample.** The World Cup response states as past fact that the final "ended on July 19, 2026," which is after the cutoff it names, so it read a schedule as a result. The log checks neither the date nor the hosts. Fix: add a verification note to Prompt 12. Optionally, have the commentary point out the asserted post-cutoff fact.

10. **Line 205: TIY 2.3 Explain asks for an unverifiable claim.** "Why the cause that survived is likely the one the training data repeated most" cannot be checked, because no student can see the training data. Fix: "explain why the model may have kept that cause, and what evidence would confirm your explanation."

11. **README line 34 names the vendor and model in a student-facing pack file.** "Claude (Anthropic), Sonnet" sits outside a Tool check callout. The chapter 1 pack names no vendor. Fix: write "a chat assistant from the course roster" and point to log Prompt 20 for the tool.

12. **The Part 3 answer key lives only in the session scratchpad** (`notes-02.md`, item 6). The log says it was "handed to the assembling session." Fix: save it to instructor materials before this session's scratchpad is gone.

13. **Lines 523-524: the 150-word cap forces cuts the tasks do not ask students to explain.** The original summary is 219 words, and Task 3 asks students to restore facts that were left out. Students must therefore drop facts. Fix: add to Task 5, "name anything you cut to fit the limit and why."

14. **Voice: closers and triplets read as machine-made.** An aphorism closes nearly every subsection (lines 80, 157, 189, 244, 272, 344, 416), and three-part lists stack up (lines 7, 342, 463, 571). Chapter 1 does this less often. Fix: cut about half of the closers, and break up two of the triplets.

## NIT

1. Line 360: the claim examples quote the tool library notice 30 lines before the reader sees it. Use a fresh example, or move them after line 390.
2. Line 312: "the DOI registry had no record." Crossref is a registration agency, and doi.org is the resolver. Write "the DOI system had no record of it."
3. Line 38: the appositive "the layers that pass signals from one to the next" restates Chapter 1 and reads awkwardly. Cut it.
4. Line 133: "As of October 2026" repeats the callout heading. Cut it.
5. Line 447: image models train on billions of captioned images, not "millions."
6. Line 7: "a different answer every time" overclaims. Write "a different answer from one run to the next."
7. Line 248: link the 2023 study inline. It appears only in Further Reading.
8. Log header: the samples come from a CLI harness with a custom system prompt and no tools, not a consumer chat app. Phrases like "I can't browse here" reflect that harness. The same is true of chapter 1, and Claude is on the supporting roster, so the label is defensible. Plan the core-roster re-capture.
9. "DOI" is defined inline (line 308) but has no glossary entry. Optional.

## Area notes (no finding)

* Anatomy: 3 MLOs with section bindings. The CLO block is verbatim. There are 5 TIY blocks with real Predict commitments, 4 Quick Checks (one Understand item, 2.1 #1), and one Fix It 2.1 with a real captured failure and a Diagnose that holds back the answer. Retrieval has 5 items ending with a "From Chapter 1:" reach-back, which matches the placement table. Lab parts are tagged to MLOs. Part 3 yields an actionable verified summary and a note to Mei Lin. Both Q&A items cite the log. The short rubric block is present. There are 4 Review Questions (Understand, Apply, Analyze, Evaluate) on new cases, 4 verified Further Reading links, and a Looking Ahead. Heading icons are exact. There are 11 worked examples. Both flagship prompts carry step labels on sentence boundaries.
* Rigor step met: the mechanism in plain terms plus a fact-check against a source file. Drift guards hold: no math, code, attention, or embeddings.
* Packet: every named file exists. Every task has a worksheet slot. The starter files leak no answers. The summary is a logged capture. The source is internally consistent and supports more than one defensible forwarding verdict. Teaching examples do not reuse lab facts.
* Callbacks to Chapter 1 (the spam filter re-run, "most chat assistants are multimodal," the three passes) all check out against chapter-01.md.
* Glossary: all 7 Key Terms resolve. Definitions are vendor-free and do not restate Chapter 1 entries.

## Verdict

Chapter 2 is close to ready for the professor's review. The checkers pass, every sample traces verbatim to a documented capture, the URLs and the DOI failure are verified, and the anatomy and rigor step are met. The voice is near chapter 1's, with somewhat more aphoristic closers. Fix three things first. (1) Re-verb MLO 2.2: "Classify" is an Understand verb under an Analyze tag. (2) Rewrite the Fix It Verify step. The repaired paragraph carries several unsupported claims, not one, and the Morton abstract reports no detectable attendance effect. Log that check. (3) Resolve the Part 3 privacy contradiction. A technician pasted a client's full update into a chat assistant, the exact risk Chapter 1 taught, and no task asks about it. Close behind is the unassessed CLO 2 claim in the alignment block.

Findings: BLOCKER 0, MAJOR 4, MINOR 14, NIT 9.
