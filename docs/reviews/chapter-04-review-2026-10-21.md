# Review: Chapter 4, Prompt Basics and Prompt Types (Opus reviewer)

Reviewed 2026-10-21, read-only. Files read in the brief's order. No repo file edited.

## Checker results (run from the repo root)

| Checker | Result |
| --- | --- |
| `check_samples_vs_log.py` | 11 sample fences, 0 lines not in log |
| `check_course_structure.py` | OK, 0 errors |
| `check_sentence_length.py` | 394 sentences, avg 14.7, longest 34, 0 flagged |
| `check_style.py` (chapter + packet) | 0 hits |
| `check_readability.py` | chapter-04 Flesch 75.0 (ch3 71.4, ch1 72.4) |
| Further Reading (curl, this review) | all 5 URLs 200, titles match the entries |
| Vendor grep (chapter + packet) | 0 vendor names |

By-eye comparison of all 11 samples with the log: every sample is a verbatim
copy trimmed only with `[...]`. Numbers checked against the log: 216, 269
characters (Prompts 2, 3), 40 and 45 words (Prompts 12, 14), "33 lines"
(Prompt 7 is 33 lines), four numbered steps and three notes (Prompt 10),
three question wordings with two lessons and one draft (Prompts 7-9).
"Grew by a quarter" (216 to 269) is 24.5 percent, fine.

## BLOCKER

None.

## MAJOR

1. **Lines 297-299: the few-shot commentary contradicts its own capture.**
   The prose says "The zero-shot version made the same offer, so the
   examples did not cause it," and "That is a job for the Constraints
   part." But Example 1 in the prompt models an offer ("Want us to swap
   it next visit?"), and the response copies that exact pattern ("Want us
   to take a look at it next visit?"). The prompt also already carried a
   Constraint, Step 4's "Use only these facts.", and it did not stop the
   offer. So the evidence supports neither "examples did not cause it"
   nor "a Constraint fixes it." Fix: say both runs offered, Example 1
   models an offer so the examples may have reinforced it, and "Use only
   these facts" did not catch it because an offer is not a fact. Then
   say a Constraint has to name the behavior ("Do not offer any service
   or repair"). Either capture that run or leave it as the open question
   TIY 4.3 or RQ 3 tests.

2. **Lines 100-104: TIY 4.1's Predict is never tested by its Run.**
   Predict asks which part the student would skip in a hurry and what
   the model would guess in its place. Run has them write all five parts
   and send the full prompt. The hurried version is never sent, and
   Explain asks a different question (which part was followed most
   closely). The brief requires a Predict the Run tests. Fix: change
   Predict to "Predict which of your five lines the response will follow
   least closely, and why," which the existing Run and Explain then test.
   Or add one Run step that sends the prompt without the part they
   predicted skipping.

3. **Line 504 (Q&A 2) depends on a run Part 2 does not require.** Q2
   says "Using your Part 2 Task 2 log entries, explain when a question is
   the right type and what it cost on your job." Part 2 Task 2 (line 490)
   sends the chosen type and the runner-up, and neither has to be a
   question. A student who compared instruction with few-shot has no log
   evidence for Q2, so the Analysis criterion cannot be met as written.
   Fix: in Part 2 Task 2, add "If neither type is a question, send the
   job a third time as a question." Or reword Q2 to cite whichever
   losing type the student ran.

4. **Line 21: MLO 4.3 says "Use examples and standing instructions," and
   no performance task has the student use standing instructions.** TIY
   4.3 is few-shot only, and the lab has a few-shot card but no
   standing-instruction or custom-instruction task. Standing instructions
   appear only on paper (QC 4.3 Q2, RQ 4). That is a traceability gap
   (rubric C4) on an Apply verb. Fix: either cut "and standing
   instructions" from MLO 4.3, or add one step to TIY 4.3 or Lab Part 2.
   For example: open a chat with standing instructions, ask two Deskside
   questions, and record whether the rules held on both.

## MINOR

1. **Lines 382 and 407: the back-reference points to a line the 4.1
   trim removed.** Section 4.4 says "Look back at the bare prompt's draft
   in Section 4.1 ... suggested a 'Reply STOP' line." The 4.1 sample
   (lines 47-51) cuts that bullet with `[...]`, so the student cannot
   find it. Also, Prompt 1's "Questions? Call us" was template text
   written because Context was missing, so it is weak evidence for what
   the Constraints part guards against. The card's Notes line ("offered
   ... 'reply STOP'") overstates a suggestion as an offer. Fix: keep the
   "Reply STOP" bullet in the 4.1 trim, and soften line 382 to "a
   failure the bare prompt hinted at."

2. **Line 446 contradicts line 329.** Line 329 says "Most chat tools run
   with one," and Key Concepts says "every tool runs a system prompt you
   usually cannot see." "Every" is an overclaim. Fix: "most tools."

3. **Line 329 and the glossary's system prompt entry blur a real
   distinction.** Opening a chat with standing instructions is a user
   message, not a system prompt. Tools give system-level text different
   priority and persistence. Calling it "a system-style prompt" invites
   the misconception. Fix: "works like a system prompt for that
   conversation, though the model still reads it as your message." Make
   the same change in the glossary entry.

4. **Line 329: a production disclosure stated book-wide in one
   chapter.** "The samples in this book were captured with a short
   system prompt ..." is true today (log header, lines 3-5), but it goes
   stale on any core-roster re-capture, which the log itself plans. The
   writer flagged this too (notes item 2). Fix: say "in this chapter,"
   or move the sentence to a book-level note the assembler words once.

5. **Line 297: the Min and others (2022) claim is stated beyond its
   scope.** The abstract (checked this review) covers classification and
   multiple-choice tasks only, and the chapter applies it to the voice
   of a text message. Fix: add "on classification and multiple-choice
   tasks," and keep the lesson as an inference. The same scope fix
   applies to line 536.

6. **Line 537: the Ouyang and others description conflates two
   methods.** The paper used demonstrations for supervised fine-tuning
   and rankings for RLHF (abstract checked this review). Chapter 2
   defines RLHF as comparing two answers. "Fine-tuned a model on
   people's demonstrations and rankings, the RLHF method from Chapter 2"
   blends them. Fix: "fine-tuned a model on people's example answers,
   then used their rankings (the RLHF method from Chapter 2) ..."

7. **Flesch 75.0 is above the 60-70 band.** Chapter 3 was approved at
   71.4. The writer stopped after two passes on purpose (notes item 1).
   Needs Mr. Vega's ruling or a light pass on Sections 4.1, 4.4, and 4.5,
   which the writer reports at 79-80.

8. **Line 418: TIY 4.4 says "On your prompt card," but no card holds this
   prompt.** TIY 4.1 filled an anatomy card, not a prompt card. TIY 4.3's
   card holds a different prompt (the few-shot one), and the dental
   option has no student card. The artifact has no home. Fix: "Open a
   fresh copy of `prompt-card-template.md` for this prompt, fill Name,
   Job, and Prompt, then write two or three criteria in Good output looks
   like."

9. **Line 495: Lab Part 3 does not tie the cards to the six packet
   tickets.** "Covering at least three different ticket types" lets a
   student count TIY 4.5's monitor card, which the chapter half-built in
   Fix It 4.1, as one of the graded cards. Fix: "covering at least three
   of the six ticket types in `deskside-ticket-samples.txt`." Make the
   same change in the worksheet.

10. **Closing maxims and small-sample generalizations.** Several
    paragraphs end on an aphorism: line 144 ("a likely word is not always
    right"), 236 ("it fails often enough to cost you," from two of three
    runs), 297 ("glad to see copied, line by line"), 382 ("cheap
    insurance"), and 386 ("a lucky message ... a tool"). Chapter 3 does
    this less. Fix: cut two or three of them, or end on the concrete
    finding (line 236: "two of three wordings failed on this ticket").

11. **Lines 130-136: the completion example is an instruction wrapped
    around a completion.** The type table (line 122) says you send "The
    start of the text," but the sample opens with "Complete this message
    ... Add no more than two sentences." MLO 4.2 asks students to
    differentiate types, so the hybrid needs one sentence. Fix: note that
    a chat assistant needs the one-line instruction, because only a raw
    model just continues text (Chapter 2, Section 2.1).

12. **Lines 89-93 and 400-407: the model five-part response never says
    who sent it.** The text has no office name, because Context supplied
    none and the Constraint forbade adding facts. The chapter calls it a
    clean pass ("dropped the greeting, which a patient may or may not
    miss") and uses it as the model card. A text from an unknown number
    is a real defect, and it is the best Context-test lesson in the
    chapter. Fix: add one sentence naming the miss, and add an
    `[office name]` slot to the card's Context part.

## NIT

1. **Line 54:** "did not invent the parking change" is followed by "It
   even guessed at the kind of change." Reword to "did not invent the
   details."
2. **Lines 75-83:** the flagship labels read `[Step 1 (Role): ...]`,
   which differs from the `[Step k: ...]` form in CLAUDE.md. The checker
   passes. Confirm the variant is adopted for Part II.
3. **Line 19:** "Build" is a Create verb in
   `docs/blooms-taxonomy-reference.md` (line 113), but the MLO is tagged
   Apply. The brief allows a verb above its tag, so this is a tag/verb
   mismatch, not a violation.
4. **Line 21:** MLO 4.3 bundles three verbs (use, check, record). It
   would measure more cleanly with one main verb.
5. **Line 475:** "Five provided files" is accurate only if you exclude
   the README. Chapter 3 says "Provided files" with no count.
6. **Line 108 (QC 4.1 Q1):** "the new field schedule pasted below" with
   nothing pasted makes a missing Context a second defensible answer
   beside the missing Constraints. The answer key should accept it, or
   the item should drop "pasted below."
7. **Line 126:** "The first two types cause the most trouble, because
   people mix them up" is unsourced. Soften to "In this chapter's runs."
8. **Sections 4.1 and 4.4:** a front desk texting patients about parking
   and appointments echoes Chapter 1 RQ 4 (a family clinic's front desk,
   parking, reminder texts). This is not a Chapter 2 or 3 reuse, so it is
   outside the brief's rule, but it is close.
9. **Artifact rule, Part 3:** Lab Part 3 produces library v1 and the
   manager-ready note. The Prompt Anatomy card and the Prompt Type picker
   are produced in Parts 1-2. The lab as a whole covers the Artifacts
   line. If the rule means Part 3 alone, the assembler should rule on
   it.

## Areas that passed

* **Samples (area 2):** all 11 are verbatim copies of the log. No
  invented URL or number.
* **Fix It 4.1 (area 4):** the failure is real, and the title does not
  name the diagnosis. Diagnose holds back the answer. The repair changes
  exactly one thing, and Verify reports the leftover invented 12:30 p.m.
  cutoff honestly.
* **Shared names (area 7):** the five parts, the five prompt types, the
  card fields in order, library v1, and the Prompt Strategy Checklist
  and Output Checklist names in Looking Ahead are all verbatim. Mei
  Lin's ask is quoted verbatim, and "approved pilot tool" matches
  Chapter 2 line 516. No dependency on saved work.
* **Glossary (area 11):** all 8 Key Terms resolve. All are on Chapter
  4's ownership list, and all are vendor-free.
* **Packet (area 9):**
  * Every named file exists, and every task has a worksheet slot.
  * No answers leak into the packet. The answer notes live only in the
    writer's notes.
  * The privacy plan comes before the first prompt.
  * The phone numbers use 555-01xx, and the packet names no vendor.
  * The README carries the fiction disclaimer and the license.
* **Rigor (area 8):** the remove-one-part test and the
  read-back-by-part table clear the Rigor step. No code, math, or
  training appears.
* **Further Reading:** 5 entries, all live. The descriptions match the
  abstracts, except minor items 5 and 6.

## Verdict

Chapter 4 is close to ready for the professor's review, with no
blockers. Every sample matches the log, all four checkers pass, the
Fix It is honest, and the Part II shared names are verbatim. Fix three
things before he reads it:

1. Rewrite the few-shot commentary (lines 297-299). It credits the
   added offer to nothing and recommends a Constraint the prompt already
   had, while Example 1 models the very offer the response copied.
2. Repair the lab chain so Q&A 2 always has a question-type run to cite.
3. Close the two Predict/MLO gaps: TIY 4.1's untested Predict, and MLO
   4.3's "standing instructions," which no performance task assesses.

The Flesch 75.0 still needs his ruling.

Findings by severity: BLOCKER 0, MAJOR 4, MINOR 12, NIT 9.
