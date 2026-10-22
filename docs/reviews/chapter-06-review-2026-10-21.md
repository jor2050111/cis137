# Review: Chapter 6, Iterative Refinement (Opus reviewer, 2026-10-21)

Read-only review. No repo file was edited.

## Checker results (run from the repo root)

* `check_samples_vs_log.py`: 12 sample fences, 0 lines not in log.
* `check_course_structure.py`: OK, 0 errors.
* `check_sentence_length.py`: 438 sentences, average 13.8, longest 33, 0 flagged.
* `check_style.py` (chapter plus all nine packet files): 0 hits.
* `check_readability.py`: chapter 6 Flesch 73.4 (ch3 approved at 71.4).
* Manual scans: no em dashes in chapter or packet. The only semicolons sit
  inside the cold-read card's `text` fence (lines 479-480). No vendor name
  in the chapter or the packet. No "prepare for" or "workforce" framing.
* Further Reading: all four arXiv IDs re-fetched today. Titles match
  (2404.12272 Shankar, 2310.11324 Sclar, 2303.17651 Madaan, 2406.06608
  Schulhoff). The "76 points", "criteria drift", and "58 techniques"
  claims match the abstracts as quoted in the log.
* Hand word counts agree with the log: club turn 2 post 37 (line 287),
  TIY 6.3 sample 32 (line 334), landscaping v3 body 76 (line 186).
* Packet: all nine files the chapter names exist with those names,
  including `skills-lab-6a-worksheet.md` and `two-tool-comparison-sheet.md`.
  `prompt-card-template.md` is byte-identical to the chapter 4 and 5 copies.
* Glossary: the five Key Terms resolve to merged headwords. They are
  vendor-free and all five belong to chapter 6's ownership list.

## BLOCKER

None.

## MAJOR

1. **Lines 186 and 334: "nothing added" is scored two different ways.**
   Landscaping v3 scores 5 of 5 even though it adds "We're always happy to
   help." and "Thank you for being part of our community of clients."
   Criterion 2 reads "Every fact matches the fact list, and nothing is
   added," and its check is "Mark each sentence against the facts in the
   prompt." Both sentences fail that check. But in TIY 6.3, "Come join us!"
   fails "nothing added," and it is the same kind of courtesy line. A
   student who follows the chapter's own scoring cannot reproduce both
   results. The writer's notes call v3's pass "a judgment call," and
   Section 6.4 and QC 6.4 item 1 depend on it. **Fix:** write the courtesy
   exception into the criterion before the first run (line 58: "No added
   claim about the service. Greetings and courtesy lines are allowed."),
   and score "Come join us!" by that same rule. Simplest version: keep the
   landscaping wording, and make TIY 6.3's criterion "no added claim," so
   that the sample's remaining miss is the loss of casual tone. The other
   option is to score v3 at 4 of 5 and use the courtesy line as the
   "faster by hand" stop example (line 441), which the chapter already
   does.

2. **Line 305: the commentary contradicts the captured conversation.**
   The prose says the fresh run "added a line and a hashtag that the
   conversation had trimmed away." The conversation's final post (turn 3,
   lines 279-285, log Prompt 8) already has an added invitation line ("Come
   hang out and give it a shot.") and the same 🔐 emoji. Only the hashtag
   is new. So the chapter's claim that follow-ups produced the cleaner
   post is not true of the post they produced. TIY 6.3's Predict (line 316)
   builds on that framing. **Fix:** say what the captures show. "The fresh
   run kept the facts and passed the length. Like the conversation's final
   post, it added an invitation line and an emoji, and it also added a
   hashtag. Turn 2 cut additions the model could see, and turn 3's restyle
   let new ones back in. A folded prompt has to block them before they
   appear."

3. **Line 578 (Q&A 1) plus Part 2 Task 3 (line 565): the graded question
   asks for evidence the lab does not collect.** Q&A 1 asks the student to
   prove that the biggest-gain version's change, not chance, caused its
   gain "using your Part 2 Task 3 re-run." But Task 3 re-runs only the
   *best* version. The biggest gain often comes early (for example, v2
   adding the backup-code caveat), and that version is never re-run. The
   student then has no evidence to cite, on the item that carries the most
   rubric weight. **Fix:** in Part 2 Task 3, add "Also re-run the version
   with your biggest gain if it is not your best version." Or rewrite Q&A
   1 so it cites the best version's two runs, and asks what those runs can
   and cannot say about the earlier gain. Mirror the change in the
   worksheet (lines 113-119 and 191-198).

## MINOR

1. **Lines 208-244, Fix It 6.1: the "failure" is in the log, not in the
   output, and the Symptom gives away most of the diagnosis.** The
   captured v2 response passes all three criteria. CLAUDE.md defines this
   book's Fix It as "a prompt that fails and its REAL captured output." The
   placement table names this theme ("a revision that changed two things
   at once"), so it may stand by design, but the professor should rule on
   it. The Symptom line also opens "Version 2 added two lines to version
   1," and the log row repeats both changes, which nearly answers the
   Diagnose question. **Fix:** describe the Symptom as what she sees next
   month ("she wants the greeting back and cannot tell what it will cost"),
   and leave the two-changes reading for Diagnose. Two smaller fixes: say
   why the prompt asks for "under 45" when the criterion is "under 50" (a
   buffer), and change "51 words, one over the limit" (line 244). Under 50
   means 49 at most, so 51 is two over. "Two words over" or "just over"
   would fix it.

2. **Line 411 and the Tool check at 413-414: the disclosure is honest, but
   the conclusion goes further than the evidence.** The callout correctly
   says both samples came from one vendor's two models. But the prose then
   draws a cause from them: "a tight prompt with the facts supplied left
   two tools little room to differ." Two models from one vendor, run
   through the same harness with the same system prompt, may agree because
   they are close relatives, not because the prompt was tight. The callout
   also leaves out that the runs used a test setup rather than two chat
   apps. Chat apps add their own instructions, and that is a main source
   of tool-to-tool difference. The log header (lines 10-12) says to
   re-capture Prompts 12 and 14 from two core-roster tools before
   publication. **Fix:** hedge the sentence ("Here the two models agreed
   closely. These two share a vendor, so that may say as much about them
   as about the prompt.") and add to the callout: "...through the same test
   setup, not two chat apps." Keep the re-capture on the pre-publication
   list.

3. **Line 411: the comparison commentary leaves out one of Tool B's
   additions.** "Each tool added an example website to check 1, and Tool A
   added a closing reason line." Tool B also added "Thanks for reaching
   out." and "in your browser" (line 393, log Prompt 14 observation).
   **Fix:** "...Tool A added a closing reason line, and Tool B added a
   thank-you opener."

4. **Lines 63, 433, 439, 525: "good enough" means two different things.**
   The glossary and line 433 say "in a fresh run." The first stop rule
   (line 439) says "in a fresh run and in a re-run." The landscaping good
   enough line (line 63) asks for one fresh run, and v3 is never re-run
   (the log has no re-run of Prompt 3). Yet the lab requires a re-run (line
   565). **Fix:** pick one rule. The stronger one, "in a fresh run and a
   re-run," fits line 198 and the lab. Then update the definition, line 63,
   and the summary bullet, or note that the owner would re-run v3 before
   she trusts it.

5. **Lines 462-482: the cold-read card is not the card in the starter
   file.** The prose says the test ran on "the shared mailbox card from
   `prompt-library-v2-starter.md`." The chapter's copy has "Notes: (blank)",
   a short Last run line, and no field parentheticals. The shipped card 3
   has a filled Notes line, the "(Chapter 6 execution log, Prompt 13)" Last
   run, and the template's field labels (log Prompt 15 observation admits
   the drift). A student who runs TIY 6.5 on card 3 pastes a different
   card. **Fix:** say "an earlier draft of the shared mailbox card, before
   its Notes line was written," or re-capture with the shipped card.

6. **Line 324, TIY 6.3: "Log it as version 3" assumes version numbers the
   chapter never gave.** The club example never numbers the conversation
   or the folded prompt. **Fix:** label the folded prompt "version 2" at
   line 287, and say the conversation counts as version 1, or drop the
   number ("log it as the next version").

7. **Review Questions 3 and 4 (lines 602, 604) reuse the chapter's own
   cover stories.** Q3's community college club officer echoes the
   cybersecurity club in 6.2. Q4's youth sports league volunteer echoes
   Fix It 6.1's youth soccer league coordinator. The brief asks for new
   cases. Across Part II, the landscaping owner and a youth sports league
   also appear in chapters 4, 5, and 6 (grep: ch4 lines 108-135 and
   262-278, ch5 line 217), which works against the "varied cover stories"
   rule. **Fix:** move Q3 and Q4 to new settings (a food truck's daily
   specials post, a clinic's reminder text). Then decide whether the
   recurring landscaping owner is a deliberate Part II thread. If so, say
   so once.

8. **Lines 7, 549, 571: who is the library v3 for?** The chapter calls it
   "the Deskside prompt library," and the README is written for "a
   Deskside technician who never saw your work." The card that "finishes
   it" is Priya's outreach newsletter card, which her volunteers run (brief
   line 13, Part 3 Task 1 "warn a volunteer"). A Deskside README that lists
   a newsletter card will confuse both groups. This is the chapter's
   headline deliverable, so the gap matters. **Fix:** call v3 "Copperwind's
   shared prompt library." Have the README name two kinds of user
   (Deskside technicians and outreach volunteers), and have "How to pick a
   card" route each one.

9. **Packet README lines 46-49 and starter lines 15-17 point students to
   `docs/execution-logs/chapter-06-responses.md`.** That file is not in the
   student data pack, and it names the vendor. Every starter Last run line
   ("a chat assistant from the course roster ... Prompt 11") cites a file
   that a Copperwind colleague, or a student, cannot open. Inside a library
   that is meant to work on its own, that is a dead reference. **Fix:** say
   "the textbook author's capture log (not in the data pack)," or drop the
   Prompt numbers from the cards and keep them only in the packet README.
   One provenance point covers the whole book: every capture went through
   a command-line harness (log header lines 3-7), yet each one is labeled
   "captured from a chat assistant." Approved chapter 3 does the same, so
   the professor should rule once for the book.

10. **`skills-lab-6a-worksheet.md` lines 162-163 and 195-196: hard wraps
    break a file name and a word.** `` `prompt-
    library-v2-starter.md` `` renders as "prompt- library-v2-starter.md",
    and "re-
    run" renders as "re- run". **Fix:** rewrap those lines so the inline
    code span and the word "re-run" each stay on one line.

11. **Line 11: the time estimate is likely low (unverified).** The lab asks
    for at least four logged versions, a follow-up, a re-run, a second
    tool, a card, a README, a cold read with a fix, a note, and two Q&A
    answers. All of that comes on top of five TIYs and the reading. **Fix:**
    pilot the lab once, or raise the estimate to 5-6 hours.

## NIT

1. Flesch 73.4 sits above the 60-70 band. The writer flagged it, and the
   checker counts list numerals as sentences. Approved chapters run 71-75,
   so this needs one book-level ruling, not a chapter fix.
2. Line 150 says "The checklist strategy is a negative constraint." The
   shared name is "negative constraints and guardrails," so use it
   verbatim. Line 133 calls the missing signer "missing context." That
   holds, but Constraints would also fit, so a one-word hedge would help.
3. Starter card 2 (line 55) labels `[Context]` twice and reads
   "[Format] Format: under 100 words". Drop the duplicate word "Format:",
   or explain that the second `[Context]` holds the grounded checks.
4. MLO 6.2 binds to Section 6.3, but 6.3 teaches tool comparison, not
   relating gains to changes. Bind it to 6.2 only. MLO 6.3 joins "judge"
   and "publish" in one objective. That is acceptable, but "judge" carries
   the level.
5. Line 346: add "on few-shot tasks" to the Sclar claim. The 76-point
   swing came from LLaMA-2-13B on few-shot classification tasks.
6. Line 571: if the student swaps "library README" for "prompt card" in
   the cold-read prompt, it still says "run the prompt and judge the
   result." Give the README version in full, or say "and 'use the library'
   for 'run the prompt'."

## Areas that passed

* MLOs: three objectives, at Apply, Analyze, and Evaluate. The verbs come
  from `docs/blooms-taxonomy-reference.md`, and each MLO carries section
  bindings. The CLO 3 and CLO 1 block is verbatim. CLO 1 is assessed
  through the accuracy criterion (line 47, lab Part 1 Task 2).
* Five TIYs, each Predict a real commitment. Each TIY names its artifact
  in the Run step. Exactly one completion prompt (6.3): a `____` gap
  inside a `text` fence, "Fill the gap from this chapter's diagnosis" in
  the Run step, and the filled prompt captured as log Prompt 10.
* Four Quick Checks, with one Understand item (QC 6.3 item 1). Five
  Retrieval items, with reach-backs to Chapter 4 and Chapter 2 as the
  placement table lists. The chapter 2 reach-back ("three things that
  shape every response") is confirmed at ch2 line 74.
* Two flagships (landscaping v3 and the cold read) have step labels on
  sentence boundaries and the "send without the [Step] lines" note. The
  chapter has 11 worked examples.
* Rigor step met: criteria before the first run, one-change versions, a
  fair two-tool comparison, a README tested by a cold read, and a note
  to Mei Lin. No code, math, or metrics. The chapter clearly asks more
  than a literacy course would.
* Privacy plan comes before the first prompt (Part 1 Task 1). Priya's
  cell number is marked private in the brief. No packet file leaks an
  answer. The instructor key stays in the writer's notes only. The lab's
  graded item (the newsletter) is never a teaching example.
* Shared names verbatim: the five parts, the card fields in order, the
  seven loop steps, the four Refinement Log fields, and v1/v2/v3.
  Copperwind facts match the Part structure (VPN, password reset, shared
  mailbox, Mei Lin's ask, Priya's fresh brief). Ch2 and ch3 cover stories
  are not reused. The ch3 newsletter was voice-clone scams, and this one
  is two-step sign-in.

## Verdict

Chapter 6 is close to ready for the professor's review. It clears its
Rigor step, every checker passes, every sample matches the log, all nine
packet files exist, and a student who finishes the lab holds a working
library: a criteria sheet, a log with one change per row, a two-tool
sheet, a slotted card, and a README tested by a cold read. A colleague
could use it once its audience is named. The same-vendor disclosure in
Section 6.3 is honest. It needs one more clause about the test setup and
a hedge on the conclusion drawn from it, and the re-capture should stay
on the pre-publication list. The three fixes that matter most:
(1) score "nothing added" one way across the chapter (landscaping v3's
courtesy lines and TIY 6.3's "Come join us!"),
(2) correct line 305, which credits the follow-up conversation with a
cleanup its own captured turn 3 does not show, and
(3) make Q&A 1 answerable by re-running the biggest-gain version, or by
rewriting the question around the re-run the lab collects.

Findings: 0 BLOCKER, 3 MAJOR, 11 MINOR, 6 NIT.
