# Review: Chapter 5, Strategies That Make Prompts Work (Opus, 2026-10-21)

Read-only review. No repo file was edited. Line numbers refer to
`book/chapters/chapter-05.md` unless another file is named.

## Checker results (run from the repo root)

* `check_samples_vs_log.py`: 15 sample fences checked, 0 lines not in log.
* `check_course_structure.py`: OK, 0 errors.
* `check_sentence_length.py`: 405 sentences, average 13.5, longest 34, 0 flagged.
* `check_style.py` (chapter plus all 8 packet files): 0 hits.
* `check_readability.py`: chapter-05 Flesch 74.1 (chapter 3 is 71.4).
* Raw capture files `scratchpad/caps05/p1-p23.txt` and `r1-r23.txt`: every prompt and response appears byte for byte in the log (scripted check).
* Starter library sample outputs (Cards 1-3) compared by eye with log Prompts 18-20: identical, prompts identical with the example input in the slot.
* Further Reading: all five URLs return 200 today (curl with a browser UA). The Kojima abstract on arXiv reads "MultiArith from 17.7% to 78.7%" with text-davinci-002. The chapter's figure and wording are correct.
* Spot facts: January 4, 2027 is a Monday. Word counts at lines 100, 116, and 203 match the log and a hand count.

## BLOCKER

**B1. The capture pipeline feeds the textbook's own law into every "plain chat assistant" run (book-wide, `tools/capture_sample.sh`).**
`claude -p --system-prompt` replaces the default system prompt but still loads `~/.claude/CLAUDE.md` and the cis137 `CLAUDE.md`. I confirmed it today: a probe sent through `tools/capture_sample.sh` from the repo root replied "They come from the CLAUDE.md files you attached to this conversation" and quoted the em dash policy verbatim. The log shows the effect. Prompt 23 ends with "A1. ... A2. ..." (Mr. Vega's action-item rule). Prompt 21 opens its closing note with "Notes for you:" (one of his feedback prefixes). None of the 23 responses contains an em dash or a semicolon, which is unusual for this model. The shown samples were captured, not invented. They still come from a model told "never invent a response," the banned-word list, and his voice rules, so they are not what a student's roster tool returns. Two lessons lean on exactly this behavior: line 77 ("The tool was honest about its placeholders") and the clarifying-questions run that "stopped as told." The starter library (lines 39, 83, 127) and the README (line 56) also say "a chat assistant from the course roster," which overstates provenance.
*Fix:* re-run the capture with CLAUDE.md loading turned off (for example `--bare`, or a clean config directory, then the same probe to confirm NONE), or capture from a core roster tool. Re-capture chapters 1-6 and re-check every commentary line against the new samples. Until that happens, change the provenance line in the log and the starter cards to name the actual setup. This needs Mr. Vega's ruling because it affects every chapter.

## MAJOR

**M1. The flagship specificity pair differs in four things, and the prose credits one strategy (lines 77-100).**
The "after" prompt adds an audience and role (Step 1), a 60-80 word size (Step 2), the facts (Step 3), and a guardrail (Step 4). Line 77 calls it "the same job with the strategy applied," and line 100 names only strategies 1 and 9. This breaks the brief's rule that a pair differs only in the thing the prose names. It also contradicts the chapter's own lesson at line 394 ("Change two things and the score can rise while you learn nothing about why"), which Quick Check 5.4 Q2 and Review Question 3 then test. TIY 5.1 (line 139) repeats the pattern: it asks for facts plus a forbidding sentence in one run, then asks why the count dropped.
*Fix:* Rewrite line 77 and line 100 to say the second prompt adds four parts at once. It shows what a fully specified prompt looks like, and Section 5.4 shows how to tell which part did the work. Name strategies 3 and 6 alongside 1 and 9. In TIY 5.1, say outright that facts plus a guardrail are a deliberate pair. Or capture a facts-only run and use that as the "after."

**M2. The chapter scores its own samples with an Output Checklist whose checks 3 and 4 overlap (lines 376-382, 417, 442, 517; `output-checklist.md` lines 15-16).**
Check 3 covers "each fact, name, number, and promise," and check 4 covers "services, rules, promises, or details." Every invented promise therefore fails both checks. Three places in the chapter lose consistency because of that overlap:
* Line 442 says "Check 3 passes on the steps" even though the run still holds the promise "Let's get invoices printing again today." Under the definition at line 378, that promise fails check 3.
* Line 382 says the second landscaping run "passes all five." That response ends with "(Word count: 64)" (line 97), which has to be deleted before posting, so it fails check 2's "ready to paste or send." The count is also wrong (the body is 60 words, line 100), so the run makes a number claim that does not hold.
* Retrieval item 2 (line 517) asks for "the two" checks the first landscaping run failed. Line 382 says that run "passes check 1 at best," which leaves checks 2 and 5 open as well, so the answer key is ambiguous.
MLO 5.3 is about judging an output with this checklist, so the measuring tool has to be unambiguous.
*Fix:* Keep the shared check names and sharpen the "What it asks" text. Make check 3 "every fact, name, or number it states matches your prompt or source," and check 4 "nothing new: no services, rules, promises, or details you did not supply." Apply the same edit to `output-checklist.md` and to the glossary entry if it changes. Then rescore line 382 (second run: check 2 Partly, because of the word-count line), reword line 442 to "check 4 still fails," and rewrite Retrieval item 2 to match.

**M3. The chapter 5 packet contradicts the Part II canon on who handles VPN tickets (`copperwind-marketing-prompts.txt` lines 42-46 vs `prompt-library-v1-starter.md` Card 2).**
The facts file lists Deskside's work without VPN and says "Network Ops handles office networks, Wi-Fi, firewalls, and VPN connections." That matches chapter 1's routing rule (`chapter-01/copperwind-ai-inventory.txt` lines 33-35). `docs/part-structure.md` (Part II facts) lists "VPN connection failures" as a common Deskside ticket, and starter Card 2 is a Deskside VPN reply. In Part 2 Task 3 and Part 3, a student who checks Deskside copy against the facts file will mark VPN help "Contradicted" while their own library holds a Deskside VPN card. The brief requires Copperwind facts to match the Part structure.
*Fix:* Get a ruling on which source wins. The smallest change is one clause in the facts file, for example "Deskside sends the first reply on remote VPN tickets, and Network Ops fixes the connection." Record it in the part-structure canon so chapters 4 and 6 agree.

## MINOR

**m1. Decomposition never appears in a captured run (lines 5, 248).** Line 5 promises "You will see each strategy in a captured run." Decomposition gets only a "Picture a volunteer coordinator" paragraph. Line 248 also says "Skills Lab 5A uses it on a small scale when you repair one prompt before you write the card for it." That describes the student's workflow, not a job split into prompt stages with a check after each. *Fix:* change line 5 to "most strategies," and cut or correct the last sentence of line 248. If a capture is wanted, Quick Check 5.2 Q3's survey case is ready-made.

**m2. Persona attribution has no control run (line 276).** "The persona bought the warm, calm voice ... The audience line bought the reassurance" credits two parts from one run with no persona-free comparison. "A warm persona tends to reassure" generalizes from one capture. *Fix:* hedge ("likely came from"), or capture the same prompt without the persona sentence.

**m3. A model behavior is stated without a capture (line 306).** "A model told to 'answer only from the sheet' may stretch the sheet's line about cold sensitivity into an answer about hot coffee" was never run. *Fix:* capture Prompt 12 without the silent-source sentence and report what happened, or cut the sentence.

**m4. An unsourced superlative (line 280).** "It is the strongest strategy for accuracy." *Fix:* "It is the most checkable strategy for accuracy, because ..."

**m5. The step-by-step statistic needs a date and a model (line 215).** The 17.7 to 78.7 percent figure is correct per the Kojima 2022 abstract, but it came from a 2022 model (text-davinci-002). Many 2026 chat assistants reason before they answer without being asked, so the accuracy gain is not a claim about today's tools. Review Question 4 asks students to judge a rule "with the evidence in this chapter," so this is the evidence they will use. *Fix:* add "on a 2022 model" and one sentence saying current tools may already work step by step, which is why the checkable lines matter more.

**m6. The paragraph before TIY 5.4 answers its Predict and Explain (line 382 vs lines 386-390).** Line 382 has already scored the same one-line landscaping prompt on checks 3 and 4. *Fix:* move the landscaping scoring sentences to after TIY 5.4, or point TIY 5.4 at the library no-sample prompt or the student's own TIY 5.1 prompt.

**m7. The lab says the files are safe to paste just before it asks for a privacy decision (line 528 vs line 536).** "The files are fictional, so you may paste them into a tool" undercuts Part 1 Task 1, where the student decides whether Mei Lin's internal note goes into a prompt. *Fix:* use chapter 6's wording: "you may paste them into a chat assistant once your privacy plan allows it."

**m8. Fourteen worked examples plus the TIY 5.3 compare block, against the brief's 8-12.** This is inside CLAUDE.md's 8-15, and the writer flagged it. *Fix:* the professor decides. The cheapest cut is to turn the ungrounded coffee run (Prompt 11) into one quoted sentence.

**m9. Flesch 74.1 sits above the 60-70 band.** Chapter 3 is 71.4, and the writer flagged it. *Fix:* the professor decides. No action is needed if the band is read as "lean high."

**m10. Cover stories repeat chapter 4's.** The dental office, youth sports league, landscaping company, and public library branch all appear in chapter 4 (chapter-04.md lines 33, 130, 262, 303). Only chapters 2 and 3 are off limits, but the style guide asks for varied cover stories, and Review Question 3 adds a fifth landscaping case. *Fix:* swap one or two, for example the dental office for a veterinary clinic, or the Review Question 3 landscaping company for a bakery.

## NIT

* **n1.** MLO 5.3 (line 21) binds to Sections 5.3-5.4, but the Output Checklist first appears in 5.4. Bind it to 5.4 (and 5.1 for the paired runs).
* **n2.** MLO 5.3's second verb, "attribute," is Analyze-level under an Evaluate tag. "Justify which strategy caused the difference" keeps the outcome at Evaluate.
* **n3.** Line 417 says "The second step is not Deskside's procedure" before the reader has seen that procedure (line 427). Say "The team's own steps, below, do not include it."
* **n4.** The guardrail sentence at line 445 has two clauses, and the second ("do not add steps that are not in them") repeats the grounding line. Line 458 credits it only with the promised time. That is accurate, but "one guardrail sentence" carries two constraints.
* **n5.** Several sections end on a maxim (lines 3, 100, 276, 359, 458). Trim two.
* **n6.** Support hours (Monday through Friday, 7 a.m. to 6 p.m., facts file line 49) are a new canon fact. Add them to the part-structure Copperwind facts.
* **n7.** "Prompt Strategy Checklist" is a glossary headword outside the brief's ownership list for chapter 5. The chapter defines it, so ratify it. "Negative constraint" is defined in passing (line 359) and used in the guardrail definition, but it is not bolded.
* **n8.** "Printers & Scanners" (line 411) is a product UI name inside a sample. It is acceptable as captured, and could be trimmed with `[...]` if the vendor rule is read strictly.
* **n9.** TIY 5.3's Predict ("The policy below never mentions repeat bookings") hints at the answer. "Predict what the grounded prompt will say" keeps the 30-day nuance as the real test.

## Areas that passed

* Fading: TIY 5.3 is the only completion prompt. The `____` gaps sit only inside the `text` fence, the Run step says to fill them from the section, the compare block is log Prompt 13, and the filled prompt is held back in the writer notes.
* Fix It 5.1: a real failure (Prompt 6), a title that does not name the diagnosis, a Diagnose step that holds back the answer, a one-change repair (Prompt 7, both sentences in Format), and an honest note on the first attempt that did not fail (Prompt 5).
* Artifact rule: each TIY names its artifact. TIY 5.1 fills a checklist cell, 5.2 a card, 5.3 a card, 5.4 a filled Output Checklist, and 5.5 a repair block plus the first v2 card. Part 3 yields library v2, an attribution, and the note to Mei Lin. Every named file exists and leaks no answer.
* Shared names: the nine strategies in order, the five Output Checklist checks, the card fields in order, v1 and v2, and the five part names all match `docs/part-structure.md` verbatim. Examples are labeled Format, per the ruling and chapter 4 line 340.
* Lab packet: the privacy plan comes first, every task has a worksheet slot, the packet names no vendor, the teaching examples (printer, mailbox) differ from the graded items, and the backup service stays unnamed.
* Anatomy: 3 MLOs (Apply, Analyze, Evaluate), CLO 3 and CLO 1 quoted verbatim and both assessed, 5 TIY, 4 Quick Checks, 5 Retrieval items with Ch 3 and Ch 1 reach-backs as the placement table lists, 2 Q&A items citing the log, the short rubric block, 4 Review Questions at the four levels, 5 Further Reading links, Looking Ahead, two flagship prompts with step labels on sentence boundaries, and no admonitions.
* Rigor and drift guards: no code, math, training, or computed metrics. Measuring a change with a fixed checklist and one-change runs clears the Rigor step.
* Voice: matches chapter 3. Second person, short sentences, no em dashes, no prose semicolons, no banned words, and no "prepare for" framing.

## Verdict

The chapter is close to ready for the professor's review. Its anatomy, shared names, fading, Fix It, artifact chain, and lab packet are sound, and every sample matches the log byte for byte. Three things should be fixed or ruled on first. First, the capture pipeline loads Mr. Vega's and the repo's CLAUDE.md into every "plain chat assistant" run (B1, book-wide, confirmed by probe), so the samples are real but not what a student's tool returns. That needs a ruling and a clean re-capture. Second, the Output Checklist's checks 3 and 4 overlap, and the chapter scores its own samples inconsistently because of it (M2). Third, the flagship specificity pair changes four things while the prose credits one strategy, which undercuts the one-change rule the chapter teaches (M1). The VPN canon conflict in the lab facts file (M3) needs a one-line ruling as well.

Findings: 1 BLOCKER, 3 MAJOR, 10 MINOR, 9 NIT.
