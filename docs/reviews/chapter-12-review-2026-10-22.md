# Review: Chapter 12, The AI Application Project (Opus, read-only)

Reviewed 2026-10-22 against `review_brief_part4.md`. No file edited.

## What I ran and opened

* `check_course_structure.py`: OK, 0 errors. `check_sentence_length.py`: 435 sentences, average 14.1, longest 34, 0 flagged. `check_style.py` (chapter plus every packet file, including `toolkit-starter/`): 0 hits. `check_samples_vs_log.py`: 9 sample blocks, 0 lines not in log. The packet ships no capture, so no packet file was passed.
* My own fence walk (script in scratchpad `walk12.py`): every `text` fence in the chapter, with `[Step]` lines stripped, matches a log fence as contiguous segments separated only by `[...]`. Head and tail cuts are all marked. No unmarked middle cut. Prompts match the log prompts byte for byte.
* Word counts re-run with `wc -w` on `caps-12/r*.txt`: r2 263, r6 644, r7 137, r8 120, r9 244. Every count the prose quotes matches.
* Fix It counts against the log excerpt: Run 1 is 21 + 2 + 1 unsure = 24, Run 2 is 22 + 2 + 0 = 24. Wi-Fi labeled Hardware is 2 + 1 = 3. The two wrong labels in Run 2 are one Wi-Fi to Hardware and one Account to Other, so "the one confusion" is contradicted. 10 + 15 = 25 minutes. All prose claims hold.
* Log header carries the probe answer ("No. I don't have any rule ...").
* Mata v. Avianca: downloaded the CourtListener PDF myself (200), `pdftotext`. Both quotes appear verbatim on page 1. The \$5,000 penalty (jointly and severally) and the letters to plaintiff Roberto Mata and to "each judge falsely identified as the author" appear in the Conclusion on page 34. The date is June 22, 2023, and the case number is 22-cv-1461 (PKC). The paragraph holds (two nits below).
* Further Reading: all four URLs return 200 with a browser user agent. The NIST page shows "Published July 26, 2024." The W3C page carries "speakers describe pertinent visual information" and "Provide material ahead of time." Digital.gov carries the Plain Writing Act sentence.
* CIS144 and CIS218 descriptions in the conclusion match `docs/mcccd/cis144-course-outline.html` ("agentic systems and AI driven data analytics") and `cis218-course-outline.html` ("design, integration, and deployment"). The conclusion names both courses and teaches neither.
* `cmp` on the toolkit-starter copies against their source packets: prompt-card (ch4/5/6), output-checklist (ch5, ch11), audit-report (ch7), ai-use-policy (ch8), use-evaluation (ch9), and refinement-log (ch6) are all byte-identical. The Part IV templates differ from the ch10 and ch11 packets (finding M2).
* Vendor grep (chapter and packet): no vendor name anywhere. No Tool check callout. The chapter states no vendor fact, so G1's vendor clause is not triggered.
* Agents guard: no code, no configuration syntax, no API, framework, or deployment content. No captured response contains code. The Work Orders are runbooks, test plans, and checklists, managed from the human-in-the-loop seat.

## BLOCKER

None.

## MAJOR

**M1. Copperwind Jobs A-C contradict chapter 10's `fair-test-tasks.txt`.** (`capstone-brief-copperwind.txt` lines 73-97, against `assets/code/chapter-10/fair-test-tasks.txt`)

* Job A is a different printer ticket (front desk, intake forms) and gives none of the three Deskside printer steps that chapter 10 supplies. With no steps given, the "adds no other step" check cannot be scored, and the job invites the invented-step failure the pilot already caught.
* Job C conflicts with chapter 10's facts. Its start date is "next month," where chapter 10 has Monday, December 7, 2026. It leaves out app approval, the "no text-message codes" line, and the ten backup codes. It also rewords the standing promise, which chapter 10 gives "word for word" as "No one from Copperwind will ever ask you for your password or for a sign-in code." Chapter 12 gives it as "No one at Copperwind will ever ask for the code."
* Job B is a different client update (the F13 backup service, where chapter 10 has the December laptop rollout).

All three are meant to be the same three help desk tasks Mei Lin set in Part IV. A student who carries a chapter 10 matrix into the recommendation will find different inputs.

* **Fix:** replace Jobs A-C with chapter 10's three tasks verbatim: the inputs, the Deskside steps, the standing promise, and the "A good ..." checks. Keep Jobs D and E.

**M2. The Part IV templates in `toolkit-starter/` are not the chapter 10 and 11 packet files.** (`toolkit-starter/comparison-matrix-template.md`, `tool-survey-card-template.md`, `requirements-sheet-template.md`, `work-order-template.md`, `selection-decision-template.md`)

The field names and order are verbatim, but the chapter 12 copies are thin one-line forms. They drop structure the earlier packets teach:

* chapter 10's fair test record and per-criterion check table
* chapter 11's inputs table and acceptance-criteria table with "Checked with" and evidence columns
* chapter 11's Selection Decision pilot table with review minutes

A student ends the course with two different versions of the same template, and the Toolkit is the course deliverable. (The writer flagged this in notes-12.md for assembly.)

* **Fix:** now that both packets exist, copy the chapter 10 and 11 files into `toolkit-starter/` byte for byte. Then update the README line "use the shared field lists" to "copied unchanged from their chapter packets."

## MINOR

**m1. The scoring table mixes in rows that are not acceptance criteria.** (Line 144-153) The prose says "She scored it against her acceptance criteria." Two of the six rows are not acceptance criteria: "Under 250 words" comes from Deliverable and format, and "No password or command" comes from Constraints. The pass and fail tally then counts them as criteria.

* **Fix:** "She scored it against her acceptance criteria and the format and constraint lines, one at a time."

**m2. The commentary claims more than the log shows.** (Line 378) "The tool sorts at volume well" is not supported. The log covers 24 emails in two runs, and this paragraph teaches exactly that habit.

* **Fix:** "The tool sorted 24 emails with 21 and then 22 right, and it can be wrong without warning."

**m3. The chapter disagrees about who checks each label.** Line 378 says "her supervisor now reads every label." The Ethics facts (line 402) say "The student worker on shift checks every label ... My supervisor approves the process." The Fix It excerpt (line 231) says "My supervisor checked every label."

* **Fix:** make line 378 match the Ethics facts, with the supervisor checking during the pilot and the worker on shift checking afterward.

**m4. Quick Check 12.3 item 1 echoes the Copperwind pilot with merged counts.** (Line 333) The numbers mirror the Copperwind pilot (40 drafts, 2 invented steps). But "38 of 40 checked drafts were usable" folds the 7 rewrites into "usable." That contradicts the canon split (31 light edits, 7 rewritten, 2 caught), and it models the very rounding the section teaches against.

* **Fix:** use the canon counts ("31 sent with light edits, 7 rewritten, 2 caught with an invented step"), or move the item to a cover story with different numbers.

**m5. Two MLOs pack two verbs.** (Lines 19 and 21) MLO 12.1 has "Design ... and build," and MLO 12.3 has "Judge ... and assemble." `docs/blooms-taxonomy-reference.md` Rules: "One verb per objective." Also, "assemble" is not in the Evaluate verb list. Both MLOs come verbatim from the writer brief's suggestions, so this is a ruling for Mr. Vega.

* **Fix (suggested):** 12.1 becomes "Design an AI solution ... with its Verification Trail." 12.3 becomes "Judge ... in an Ethics Statement." The Toolkit moves into 12.1's deliverable or the lab text.

**m6. The two capstone briefs are not on equal footing.** `capstone-brief-own-project.txt` has a section "The same artifacts as the Copperwind option" and states the two-part privacy rule. `capstone-brief-copperwind.txt` lists neither the artifacts (Requirements Sheet, Tool Survey cards, two or more Work Orders, Verification Trail, Presentation outline, Ethics Statement, Toolkit) nor the shared rule in those words. It has only its specific "What never goes into a prompt" list.

* **Fix:** add the same artifact list to the Copperwind brief. Open its privacy section with the shared rule: nothing identifying goes into a tool, and nothing you do not have the right to share.

**m7. The own-project brief widens the chapter's first condition.** (`capstone-brief-own-project.txt` line 14) "or will do this term" contradicts the chapter's first condition, "It is a job you are doing now" (line 42), and it leans against G2's term-label rule.

* **Fix:** delete "or will do this term."

**m8. The Toolkit workflow lets filled and clean copies collide.**

* TIY 12.1 and 12.2 and lab Part 1 Tasks 3-4 and Part 2 Tasks 1-3 have students fill templates inside `toolkit-starter/`.
* Part 2 Task 4 and Part 3 Tasks 1 and 4 fill the root copies of the chapter 12 templates, which also exist inside the starter.
* TIY 12.5 and Part 3 Task 5 then copy `toolkit-starter/` into `toolkit-lastname`.

Clean and filled copies collide, and a student cannot tell which file is the "clean copy of every template" the chapter promises (line 448).

* **Fix:** in Part 1 Task 1 (and TIY 12.1), copy `toolkit-starter/` to `toolkit-lastname/` first, and do every fill in that copy. Name one location for the four chapter 12 templates.

**m9. A cold-start Toolkit has no prompt library.** The chain, line 436, and `toolkit-readme-template.md` list "prompt library v3." But `toolkit-starter/` ships only `prompt-card-template.md`, and no chapter 12 task produces a card. A student with no saved files ends with an empty library row, while the conclusion says the Toolkit holds "a prompt library with logs."

* **Fix:** ship chapter 6's `prompt-library-v2-starter.md` (or a v3 starter) in `toolkit-starter/`. Alternatively, add a lab line: save the best Work Order prompt as a prompt card.

**m10. Inline-code file names break across lines in the worksheet.** (`skills-lab-12a-worksheet.md` lines 65-66, 101-102, 180-181) The spans are split after a hyphen, so they render as "work-order- template.md", "toolkit- starter/...", and "toolkit- readme-template.md". File names must be exact.

* **Fix:** keep each code span on one line.

**m11. The conclusion closes on maxims.** (Lines 582 and 584) "Copperwind is better for it." is a closing maxim, and the student has not delivered anything yet. "That person is you." is another. Both are banned.

* **Fix:** cut the first. End the conclusion on "...answer for the result."

## NIT

**n1. The Mata paragraph has two small slips.** (Line 424)

* The filing was an "Affirmation in Opposition," not a brief. Fix: "filed a court paper."
* The order imposes sanctions "pursuant to Rule 11, or, alternatively, its inherent authority" (page 34). "The rule it applied, Rule 11" is accurate enough. "The rule it relied on first" would be exact.

**n2. The README example has three columns, the template four.** (Line 163) The chapter's example rows have three columns. `verification-trail-readme-template.md` has four: it adds "What it holds" and reads "File name and where it lives."

* **Fix:** match the template.

**n3. "Changes one thing" covers several changes.** (Line 155) The office manager "answers the three questions, decides which two-person wording stands, and fixes the length in a second version that changes one thing." Answering the ASK lines changes the Inputs, so this reads as several changes in one version.

* **Fix:** "the answers go into Inputs as version 2, and the length fix is version 3, each logged in a Refinement Log."

**n4. The Comparison Matrix is in the starter but not the README.** `toolkit-readme-template.md` has no Comparison Matrix row, although `toolkit-starter/` ships the template. That is consistent with the chain's Toolkit list, but students will wonder where it goes.

* **Fix:** add a row, or a line saying the matrix feeds the Tool Survey's "Last tested."

**n5. Chapters 10 and 12 phrase FERPA differently.** Chapter 10 line 124 says the housing office "handles student records that FERPA protects." Chapter 12 line 80 rightly leaves that ruling to the privacy office.

* **Fix:** harmonize at assembly, in chapter 10's favor of caution.

**n6. "The Presentation outline" is bolded but has no glossary entry.** (Line 188) The writer followed chapter 9's "The Memo" precedent. This is Mr. Vega's call.

## Checks that passed (no finding)

* **Artifact rule.** Every TIY names its artifact in the Run step: the Requirements Sheet, Work Order 1 plus its Verification Trail README row, the filled Presentation outline, an Ethics Statement section, and the Toolkit README lines. Each section shows an own-IT-project case:
  * 12.1: housing office worker and home lab stakeholder
  * 12.2: accounting firm runbook
  * 12.3: housing office presentation
  * 12.4: housing ethics and the home lab README line

  Lab Part 3 produces the Presentation outline, claim test, reflection, Ethics Statement, and Toolkit, plus a piece Mei Lin can act on.
* **Fading.** Exactly one problem-first TIY (12.3), with the captured behavior shown after the Explain step. No completion prompt.
* **Fix It.** A real first-attempt failure, logged (Prompt 3). The title does not name the diagnosis, the Diagnose step holds back the answer, and the repair is one added sentence with the excerpt unchanged (Prompt 4). Verify retraces each piece.
* **Flagships.** Two flagships (Prompts 2 and 6), each with 4 `[Step]` lines at sentence boundaries and the "Send the prompt without the [Step] lines" note. 9 worked examples. Only `text` fences.
* **Retrieval.** 5 items, ending `From Chapter 10:` (shared names only) and `From Chapter 8:`.
* **Review Questions.** 4 items at Understand, Apply, Analyze, and Evaluate, on new cover stories from the Part IV list.
* **CLO block.** Verbatim. Every CLO is assessed: CLO 1 (Audit, Fix It, Part 3 Task 2), CLO 3 (Work Orders, TIY 12.3), CLO 4 (reflection, Part 3 Task 3), CLO 5 (Ethics Statement, Review Q4), CLO 6 (Selection Decision, Job E).
* **Copperwind facts.** The Copperwind facts in the brief match canon: team sizes 5 and 3, 160 tickets a week, the 30-minute target, support hours, the 40/31/7/2 pilot with the VPN-reinstall and portal steps, the \$30 quote, the seven policy sections, owner and operations manager by role, no client portal, Arizona-only clients, Deskside line 602-555-0149 (ch7 F11), backup service January 4, 2027 (ch7 F13), and the hire happening either way.
* **Glossary.** All five Key Terms resolve to the additions file. The definitions are vendor-free and on chapter 12's ownership list.
* **Rigor step.** Cleared: a delivered solution with a Verification Trail, a stakeholder presentation, and an Ethics Statement. The Toolkit README's "Which tools I will use next week" gives the student tools to use next week.

## Verdict

Chapter 12 is ready for Mr. Vega's review once the two packet-sync fixes land. The prose, the captures, the case, and the conclusion are sound:

* every fence walks clean against the log
* every count and word count in the Fix It and the commentary checks out
* the Mata paragraph matches the sanctions order
* the CIS144 and CIS218 lines match the stored MCCCD copies without teaching either course
* the agents guard holds, with no code or configuration anywhere

The problems sit in the packet's join to the rest of Part IV. The three most important fixes:

1. **Jobs A-C.** Replace them in `capstone-brief-copperwind.txt` with chapter 10's `fair-test-tasks.txt` tasks verbatim. Today the printer ticket lacks the Deskside steps, and the two-step facts and "standing promise" contradict chapter 10.
2. **Part IV templates.** Copy the chapter 10 and 11 packet templates into `toolkit-starter/` byte for byte, so the Toolkit ships one version of each.
3. **Toolkit workflow.** Have students copy `toolkit-starter/` to `toolkit-lastname/` before the first fill, so clean and filled templates stop colliding. Add a prompt-library starter so a cold-start Toolkit is complete.

Counts: BLOCKER 0, MAJOR 2, MINOR 11, NIT 6.
