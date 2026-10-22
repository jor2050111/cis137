# CIS137 Textbook: HANDOFF

**Last updated:** 2026-10-22, late afternoon (revision list worked, gates re-run on 6a33f7b: 96.8, Publication-ready candidate, all eight gates pass; awaiting Mr. Vega's Part IV review and the outside OER review)
**Repo:** https://github.com/jor2050111/cis137
**Live site:** https://jor2050111.github.io/cis137/
**Task list:** cis137-fall27 (`export CLAUDE_CODE_TASK_LIST_ID=cis137-fall27`; the term is HQ Decision "First offering term")
**HQ:** Project recu4GSoXTE381m4m, Context recQcWyyt9Sj7Gr5r, Task recTFTaVUmjkeeoOP, Decisions D10-D15 (ids in the Stand-down section)
**Brief:** `docs/starter-prompt.md` (moved from the root once the scaffold matched the family layout)

## What was done (2026-10-21, afternoon): merge of the two sessions' work

The CIS137 Planning session took over by Mr. Vega's ruling (comment on
HQ task recTFTaVUmjkeeoOP, 2026-10-21). It compared the cis137-build
versions at HEAD with its own drafts at 6401a24 and kept the best of
both:

* `docs/CIS137_CLOs.md`: the cis137-build version stays the base
  (Arabic CLO numbers that match MCCCD and every other file, the
  chapter alignment table, the certificate context). Added from the
  Planning draft: the outline-section-to-competency crosswalk, the
  verbatim "real-world" note, and the schedule-neutrality note on the
  first term (D11).
* `docs/part-structure.md`: the cis137-build chapter plan and
  Copperwind spine stay (they match chapter 1 and the D13
  recommendation). Added from the Planning draft: a per-chapter
  upgrade placement table (spine block, fading mode, Fix It candidate,
  reach-backs), a pedagogy-upgrades bullet in the rationale, and
  content bullets for chapters 2, 5, 6, 8, 9, 10, 11, and 12
  (knowledge cutoffs, grounding, evaluation criteria before the first
  run, OECD principles, Copyright Office guidance, FERPA and HIPAA
  touchpoints, case studies, keeping a survey current, piloting, the
  capstone option). The title says "Proposed, awaiting approval" until
  D12 is ruled.
* `book/index.md`: the cis137-build page stays (9-week mapping,
  Sources & Permissions). Shorter sentences in the About and Part
  blurbs lifted Flesch from 52.5 to 57.3. The verbatim CLO lines keep
  it under 60. Added the "AI inside everyday apps" row and the
  sentence that says the syllabus names the roster.
* Law cleanup for a prompt-based book: `CLAUDE.md` (worked-example
  rules replace the code rules, kebab-case data files, no leftover
  "None (chapters teach from zero)" phrases in running prose),
  `README.md` (chapter count, roster accounts, checklist), the style
  guide and the chapter template (the sample label drops its
  semicolon), and the two templates' token leftovers.
* Chapter 1 checker hits cleared: six 35+ word sentences split, the
  three sample labels now read "Sample response (captured from a chat
  assistant, October 2026). Your output will differ:", and the
  glossary's "rather" is gone. Sentence checker 0 flagged, structure
  checker 0 errors, build clean, chapter Flesch 71.6.
* `assets/code/chapter-01/README.md` no longer tells students that
  item E is not AI and that item G is the policy risk. That README
  ships inside the data pack. An instructor answer key belongs in
  co-professor, not in this public repo, and is not yet written.
* Further Reading: the Dartmouth proposal link (http) returns 200 with
  application/pdf. The https form of that host does not respond, so
  the http link stays.
* Review: an Opus review of chapter 1 ran after these fixes. Its
  findings and what was done with them are in the entry that follows
  this one. The Codex CLI review still fails on the configured model
  as of 2026-10-21.

Open for Mr. Vega: rulings on D10-D15 and his edits to chapter 1 (his
version becomes the law for chapters 2-12). Ruled 2026-10-21: the
Planning session's two duplicate HQ records (Context recgSbFUS6NYamahA,
Project recnMAC0PeEgIBfiL) are deleted, and the Stand-down section at
the bottom of this file stays as history.

## What was done (2026-10-22, late afternoon): the ranks 5-8 revision list and the post-revision evaluation

Mr. Vega's instruction: work the ranks 5-8 revision list in the
evaluation record unattended, then re-run the gates on the new commit
and report. Commit 6a33f7b (revisions), two Opus writers from one brief
(`revision_brief.md` in the Planning session's scratchpad, with the
coordinator's ruling on every item), verified here.

**Rulings recorded in the law files.** `CLAUDE.md` and
`docs/part-structure.md`: Evaluate enters early in chapter 2 (the
verify habit) and chapter 5 (the Output Checklist), so MLOs 2.3 and
5.3 keep their tags. `docs/style-guide.md`: historical milestones in
chapter 1's table and in a captured sample may name products as
history. `templates/chapter-template.md`: Key Concepts carry 5-7
bullets.

**Edits.** Chapter 3's MLO 3.3 binds Section 3.2. Chapter 10's MLO
10.3 names the type-of-AI classification (CLO 2). Chapter 1's analysis
item 1 quotes a marked line from the student's log, and its Fix It
symptom carries the capture label. Try It Yourself 3.5 and 8.4 carry
fallbacks. Lab 2A carries the "no earlier file" line. Chapter 2's
Looking Ahead runs three sentences. "Chatbot" became "chat assistant"
in chapters 8 and 9 (the Moffatt quotations keep the tribunal's word).
Chapter 10 says "a case from October 2026" and "the course tool
roster." Chapter 12's Review Question 1 is a Create item, Try It
Yourself 12.5's Predict names the Tool Survey field that rules a tool
out, the Toolkit README row reads "Prompt library (v3, or the v2
starter)," and chapter 6's library README ships in the Toolkit starter
(17 files). READMEs in chapters 6 and 12 name the captured-output
exception, `_generators/README.md` points at `tools/build_data_pack.sh`,
and chapter 1's Turing entry links the canonical DOI (Crossref record
confirms it; the publisher page blocks every client) with the free
copy in prose. Chapter 1's Section 1.4 gained a Tool check naming the
author's test setup as the source of every sample.

**Gates re-run on 6a33f7b.** Record:
`../evaluations/cis137-2026-10-22-v2-post-revision-scored-rubric.md`,
manifest beside it (81 occurrences, 57 unique, 100 percent coverage,
no broken or unresolved URL). Weighted index 96.8, Publication-ready
candidate. All eight gates pass. axe: zero violations on all 32
page-size pairs, locally and live. The record lists what remains
beside the label: chapter 10's Flesch ruling, the vendor-fact refresh
cadence, the dated figures, the roster-tool re-capture decision, and
Mr. Vega's own Part IV review.

## What was done (2026-10-22, afternoon): the shared-theme accessibility fix, every book

Mr. Vega's instruction: fix the shared-theme accessibility defects in
`../shared`, re-sync every book, re-run axe on CIS137, and report.

**What the five axe rules were.** Footer link contrast 1.28:1 (the
theme paints the copyright links with the page link color through
`html .md-footer-meta.md-typeset a:not(:focus, :hover)`), admonition
link contrast 4.1:1 on tinted bodies, wide-table scroll regions with
no keyboard access, the header's drawer and search labels carrying
`aria-label` without a role, and the search dialog's two icon buttons
with no name plus its combobox input without `aria-expanded` and
`aria-controls`. The dialog lives in an open shadow root.

**The fix, in `../shared` (textbooks commit 8edb0af).**
`stylesheets/brand.css` gained footer rules at specificity 0,4,2
(white on navy 900), a darker link color inside admonitions and
details in the light scheme (Canvas Blue hover tone, 6.0:1), and gold
focus rings for the elements the script makes focusable. A new
`javascripts/a11y.js` repairs the rendered DOM: it gives table scroll
regions a tab stop, a region role, and a label from the caption or
first header; turns the header toggle labels into keyboard-operable
buttons with `aria-expanded`; hides the overlay from assistive tech;
and, inside the search dialog's shadow root, names the icon buttons by
their icon class, labels the combobox and wires `aria-expanded` and
`aria-controls` to the results list, and gives the scrolling panels a
tab stop. The sync manifest carries the script to
`book/javascripts/a11y.js`, and each book's `zensical.toml` loads it
through `extra_javascript` (Zensical honors the key in its base
template).

**Rollout.** Synced to cis105, cis111, cis133, cis215, cis360, cis376,
cis137, and the template, each built clean as a smoke test with the
script on the page, each committed and pushed (one commit per repo).
The two archive folders were synced by `--all` and reverted, so they
stay frozen. bpc170 and bpc270 have no Zensical config yet and were
skipped.

**Verification on CIS137.** axe-core 4.14 through Playwright, 16
routes at 1280 by 900 and 375 by 812: zero violations on all 32
page-size pairs, every route 200, no overflow, no heading skips. The
live site was re-run after the deploy (result in the evaluation
record's second addendum). G4 is cleared on this state. A new
evaluation on a new reviewed commit is still required before the
Publication-ready label.

## What was done (2026-10-22, afternoon): gate remediation, G1 and G5 and the anchor setting

Mr. Vega's instruction: fix the G1 and G5 defects and the
`anchor_linenums` setting here, re-run the affected checks, and leave
the shared-theme accessibility fixes for his ruling. Commit fcc35fa.

* Chapter 8's Tool check: the Microsoft line now rests on "Microsoft
  Copilot for individuals: your activity history" and "Copilot in
  Microsoft 365 apps for home: your data and privacy" (read October
  22, 2026): the app updated on August 18, 2026 does not use prompts,
  responses, or file contents to train foundation models, the older
  FAQ covers only the app before that update, and retention for the
  new app is unverified. The callout's date line reads October 21 and
  22. The chapter 8 log carries the verification note.
* Chapter 8's Further Reading: the SB26-189 line no longer says the
  page links SB24-205. It says the summary names the 2024 act it
  replaces.
* Chapter 1's Further Reading: the Dartmouth proposal now links the
  AI Magazine 27(4), 2006 reprint by DOI (10.1609/aimag.v27i4.1904),
  which resolves in a browser to the AAAI page (curl is
  Cloudflare-blocked). The chapter 1 log carries the verification
  note and the archived copy of the original PDF.
* `zensical.toml`: `anchor_linenums = false`. The rebuilt site has no
  code-line anchor links; axe's link-name rule (2,662 nodes) is gone.

**Re-run results:** structure 0 errors, sentence length 0 flagged,
samples versus log clean, style 0 hits on chapters 1 and 8, Flesch
72.3 and 64.5, build clean. axe on all 16 routes now reports only the
five shared-theme rules (color-contrast 66 nodes, aria-prohibited-attr
64, button-name 64, scrollable-region-focusable 56, aria-required-attr
32), which wait for Mr. Vega's ruling because the fix touches every
book in the family. G1 and G5 are cleared on this state. G4 still
fails. A new evaluation is needed for the Publication-ready label.

## What was done (2026-10-22, midday): publication gates G1-G8 and the evaluation record

Mr. Vega's instruction: "Run the publication gates G1-G8 and write the
evaluation record now, unattended, while I review Part IV. Report what
passes, what fails, and what needs me."

**Reviewed state:** commit dcc886b (this repo), which added
`tools/build_data_pack.sh` so the student archive has a reproducible
build. Record: `../evaluations/cis137-2026-10-22-v2-scored-rubric.md`,
manifest `../evaluations/cis137-2026-10-22-v2-source-audit.csv`
(textbooks repo). Instrument: TEXTBOOK-QUALITY-RUBRIC-V2.md, Version
2.1.

**Result:** weighted index 81.0 of 100, the Strong draft band. Gates
G2, G3, G6, G7, G8 pass. G1, G4, G5 fail. Per-criterion vector
3, 4, 5, 4, 4, 4, 4, 5, 4, 2, 4, 4, 5, 5, 4.

**Method:** mechanical gates by script (CLO chain, rubric single
source, synced files, internal links, nav, license, artifacts,
editorial scans, glossary, structure, readability), the full source
protocol on 80 URL occurrences (56 unique) with three Opus auditors
and browser confirmation of five blocked pages, axe-core 4.14 through
Playwright on all 16 routes at two sizes, a clean build, the archive
build and integrity test, the generator re-run, and three Opus scorers
on the fifteen criteria, calibrated and assembled here.

**What fails and why:**

* G4: every page fails axe on the shared theme's footer contrast (1.28
  to 1, the same defect the July family evaluations recorded), table
  scroll regions with no keyboard access, three theme ARIA rules, and
  2,662 nameless code-line anchor links from `anchor_linenums = true`
  in `zensical.toml`.
* G1: chapter 8's Tool check (line 205) cites Microsoft's Privacy FAQ,
  which now covers only the pre-August 18, 2026 app and contradicts
  chapter 10's current line; chapter 8's Further Reading (line 572)
  says the Colorado bill page "links SB24-205 and its history," which
  it does not.
* G5: chapter 1's Dartmouth proposal link (line 516) points at a host
  that refuses connections.

**Everything else:** 140 shown sample blocks trace to clean-harness
logs with every cut marked, every log opens with the probe line, all
12 Fix Its are logged failures, all 12 packets are consistent, the
generator and the Toolkit copies reproduce byte for byte, the archive
passes, the license shows, the CLO chain verifies, and the
schedule-language scan found only case facts plus one soft phrase
("a case from this term," chapter 10 line 370).

**Needs Mr. Vega:** the shared-theme fixes (they touch every book),
the Flesch ruling for chapter 10 (71.8) or a recorded band of 65-75,
the Dartmouth replacement (archived copy or the AI Magazine reprint),
a style-guide exception for historical product names in chapter 1's
milestone table, the Key Concepts bullet count (11 chapters at 7
against the template's 4-6), and a vendor-fact refresh cadence.

**Revision list after the gates (ranks 5-8 in the record):** section
3.2 bound to no MLO, MLOs 2.3 and 5.3 above the Part band, chapter
10's implicit CLO 2 link, chapter 1's analysis items not citing the
log, the Toolkit's v3 label over a v2 starter, TIYs 3.5 and 8.4
without a fallback, README provenance slips in chapters 6 and 12, the
stale zip recipe in `_generators/README.md`, chapter 10's citation of
the unpublished `docs/tool-roster.md`, "chatbot" twice, the missing
capture label at chapter 1 line 349, chapter 2's four-sentence Looking
Ahead, chapter 12's Review Question 1 at Understand, TIY 12.5's
self-confirming Predict, Lab 2A's missing "no earlier file" line, and
a Tool check in chapter 1 naming the command-line test setup behind
every sample.

## What was done (2026-10-22, morning): Part IV, chapters 10-12, and the book complete in draft

Mr. Vega approved chapters 1-9 as written and asked for Part IV
unattended, "keeping cohesiveness to the subject of part IV," with the
artifact rule back: the Try It Yourself activities and the labs give
students "practical artifacts, products, or tools" so they "finish the
course clearly identifying practical tools they can apply immediately
in not only their academic work but in their own IT projects as they
manage AI agents to work with them in developing IT solutions."

**Canon first (commit bbd6e97).** `CLAUDE.md` and
`docs/part-structure.md` record the reading of the agents guard: Part
IV teaches managing an AI assistant or agent-style tool from the
human-in-the-loop seat (a Work Order, acceptance criteria, a review, a
decision, a log), never building, orchestrating, or deploying one, and
prints no code. The "Part IV artifact chain" fixes the shared names
(the fair test, the Comparison Matrix, the Tool Survey card, the
Requirements Sheet, the Work Order, the Selection Decision, the
Verification Trail, the Ethics Statement, the Presentation outline,
the Toolkit), the Copperwind facts for Part IV, the student's-own-IT-
project thread, and the cover stories. Facts added by the writers were
ratified at assembly (the inbox sort time, the VPN app move, the
billing rules, the ticket sample's scope).

**Method, as in Part III.** One brief (`writer_brief_part4.md`), three
Opus writers on the clean harness, one read-only Opus review per
chapter (`docs/reviews/chapter-1N-review-2026-10-22.md`), every ruled
finding applied by its writer, assembled and verified here. Commit
50c0967.

**Chapter 10, Surveying and Comparing AI Platforms** (569 lines, Flesch
71.8, 10 captures, 9 shown). The landscape by type, the six criteria,
the fair test and the Comparison Matrix run on three help desk tasks
across two models from the author's test setup (disclosed), the Tool
Survey as a living index. The Fix It is an unfair comparison (one tool
got the facts, one did not), repaired by sending the same prompt. The
review (1 blocker, 4 majors) found the Microsoft training line sourced
to a page that no longer applies to the current Copilot app, a missing
Gemini default, two tools deferred that read fine in a browser (and
one renamed: NotebookLM is Gemini Notebook, roster updated), and a
Fix It tie that rested on scoring a gloss two ways. All fixed: every
vendor fact was re-read on October 22, 2026, the gloss rule is stated
above the table, and the tie became "Tool B ahead by one claim, one
run each."

**Chapter 11, Matching AI Tools to Scenarios** (619 lines, Flesch 69.7,
20 captures, 10 shown). The Requirements Sheet before the tool, the
Work Order as the way to direct an AI assistant through a multi-step
job (the VPN test plan with a checkpoint is the strongest passage in
the Part), five scenarios with their decisions, a worked no-AI
decision (the plumbing contractor's warranty claim), the pilot and the
Selection Decision. `deskside-tickets.csv` (80 rows, 6 columns) comes
from a seeded generator (`assets/code/_generators/gen_deskside_tickets.py`,
seed 137, byte-identical on rerun, sha256 prefix f36a8ffc481d). The
review (0 blockers, 7 majors) found the Fix It changing two things,
vendor names inside two captures, the invoice's no-AI answer announced
before the lab asked for it, and no worked no-AI decision. All fixed:
the Fix It was re-captured so only the ticket text changes, Prompt 1
was re-captured to name tool types, the flyer tip line is trimmed, and
the no-AI case was added.

**Chapter 12, The AI Application Project** (584 lines, Flesch 67.9, 9
captures, all shown). Choosing the scenario and defining done, Work
Orders and the Verification Trail, presenting with evidence and
limits, the Ethics Statement, and the Toolkit. The Fix It is a results
headline that rounds two counts into a percentage and hides an unsure
label, repaired by one requirement (the log is the only source). The
capstone has two equal options (Mei Lin's year-ahead recommendation,
or the student's own IT project) with the same privacy rule. The
packet's `toolkit-starter/` holds sixteen files: every template the
Toolkit lists, byte-identical to its chapter packet, plus chapter 6's
library v2 starter. Students copy it to `toolkit-lastname` before the
first fill. The chapter ends with "Course Conclusion: Where You Go
from Here," which names CIS144 and CIS218 from the stored MCCCD copies
and teaches neither. The review (0 blockers, 2 majors) found the
capstone brief out of sync with chapter 10's tasks and the starter
shipping thin copies of the Part IV templates. Both fixed.

**Checkers at the end:** structure 0 errors on twelve chapters,
sentence length 0 flagged, every shown sample in its log, 73 glossary
terms added across the book with no duplicates, every key term
resolving, style 0 hits on prose, no code or configuration syntax
anywhere in Part IV, Flesch 71.8, 69.7, 67.9 (book combined 69.9),
build clean, deploy verified. Instructor keys for Labs 10A-12A are in
co-professor.

**Rulings made at assembly:** one verb per MLO (chapters 11 and 12
reworded); glosses that add a fact are claims; "The Presentation
outline" follows "The Memo" (bold on first use, no glossary entry);
the Flesch band is settled by his approval of chapters 1-9 at 70-75.

**Publication refresh list (adds to Part III's):** every vendor fact in
the chapter 10 and 11 Tool check callouts (read October 22, 2026), the
roster-tool re-capture of chapter 10's fair test and chapter 11's
pilot and Fix It (two models from one vendor today), and the district
Copilot license for students (still unverified).

**The book is complete in draft:** twelve chapters, twelve packets,
twelve logs, eleven review reports, the glossary, the fluency
contract, and the Toolkit. What remains is Mr. Vega's Part IV review,
then the publication gates G1-G8 and the evaluation record in
`../evaluations/`, the Canvas phase when a shell exists (D14), and the
refresh list above.

## What was done (2026-10-21, overnight into 2026-10-22): Part III, chapters 7-9, complete for review

Mr. Vega's instruction at 22:50 MST: "Start Part III (chapters 7-9)
unattended with the same method. I will review Part II alongside."

**Canon first.** `docs/part-structure.md` gained "Part III shared
names" (the Accuracy Audit and its four verdicts, the Audit Report
fields, the paired prompt test, the four kinds of rules, the AI Use
Policy sections, the Use Evaluation's five factors, the Memo) and the
Copperwind facts for Part III (team sizes, 160 tickets a week, the
30-minute first-reply target, the two-week pilot's numbers, the
\$30-per-user quote, the operations manager and the owner by role, no
client portal, Arizona-only clients, medical and physical therapy
clients). Three writers used them verbatim in parallel.

**Method, as in Part II with the clean-harness lessons folded in.**
One brief (`writer_brief_part3.md` in the Planning session's
scratchpad): the rigor steps and drift guards, the primary-document
rule (read the current document before stating a status, date it,
write "as of October 2026"), the capture discipline (probe first and
log it, byte-identical prompt files, a three-run cap, teach from
variance), fading by chapter (completion prompts in 7 and 8,
problem-first in 9), the packets, and the glossary ownership. Three
Opus writers, one read-only Opus review per chapter
(`docs/reviews/chapter-0N-review-2026-10-21.md`), every ruled finding
applied by its writer, assembled and verified here. Commit a8ab9e1.

**Chapter 7, Accuracy and Bias** (619 lines, Flesch 68.0, 30 captures,
12 shown). The Accuracy Audit run on captured responses against a
supplied source, four error sources each with a capture, the paired
prompt test on fictional people with one detail varied, fairness as a
decision, the Audit Report. The Fix It is a paired test that varied
two details (a name and the years), repaired by holding the years so
only the name varies, with the six-run result reported as a lead and
never a verdict about a group. The lab audits two captured Copperwind
drafts (a services blurb, a job posting) against the facts sheet and
runs the student's own pair on two applicant files. Review (0
blockers, 4 majors, 14 minors, 6 nits): a miscount in the flagship
leasing pair, an overstatement of what Gender Shades shows, a Try It
Yourself that repeated chapter 2's exercise (replaced, now "Sort the
Verdicts," a completion prompt on the two new verdicts), and a missing
chance caveat in the Fix It. All applied. Estimated time 5-6 hours
(ruled).

**Chapter 8, Governance, Privacy, and Content Ownership** (580 lines,
Flesch 64.7, 14 captures, 9 shown). The four kinds of rules, the
global map read from the primary documents, privacy and the data
policy reading, FERPA and HIPAA touchpoints, copyright and the
Copyright Office's guidance, and the AI Use Policy. The writer read
the EU AI Act as consolidated on July 27, 2026: Regulation (EU)
2026/1744 of July 8, 2026 (the Digital Omnibus on AI) moved Annex III
high-risk duties to December 2, 2027 and Annex I to August 2, 2028,
with two new bans from December 2, 2026. Part IV writers must not use
the old August 2026 date. Review (2 blockers, 2 majors, 5 minors, 4
nits) confirmed every EU, NIST, OECD, FERPA, HHS, Copyright Office,
and vendor claim to the day, and found the Fix It built on a
misreading: Utah's disclosure rule was renumbered to 13-77-103, not
repealed, and Colorado's 6-1-1704 is real, with SB26-189 effective
January 1, 2027. The Fix It was rebuilt on the same capture around
what did fail (citations that are real but send the reader to the
wrong place or misstate scope), the invented-law candidate having
failed to reproduce in four clean attempts (placement table updated).
A copyright slip (a title and dates called registrable) is now named
as the slip it is, with 37 CFR 202.1(a). All applied.

**Chapter 9, AI in Business and Society** (562 lines, Flesch 67.6, 13
captures, 10 shown). Where AI is strong and weak with sourced
evidence, the Use Evaluation fed by a pilot, sourced cases (Moffatt v.
Air Canada, 2024 BCCRT 149, named as a British Columbia small-claims
decision that binds no court in Arizona), trends in dated callouts,
society with one sourced figure each, and the Memo. The Fix It is a
silent failure: a response that cites the WEF Future of Jobs Report
2025 for a claim the report does not make. Review (2 blockers, 2
majors, 8 minors, 6 nits) found the repair's own claim about that
report wrong against the PDF (the report does carry an AI-specific
line: 9 million displaced, 11 million created, by employer
expectation, 2025-2030), an unmarked cut in a sample fence, and two
misstatements of a source's reach. The Verify now runs two checks and
marks the repaired response's sentence Contradicted, which is the
lesson: asking a model for sources never replaces opening them. All
applied.

**Checkers at the end:** structure 0 errors on nine chapters, sentence
length 0 flagged, every shown sample in its log (chapters and
packets), 27 glossary terms merged with no duplicates, every key term
resolving, style 0 hits, Flesch inside the band on all three Part III
chapters (book combined 69.9), build clean, deploy verified, nav
enabled for Part III. Instructor keys for Labs 7A, 8A, and 9A are in
co-professor.

**Rulings made at assembly:** chapter 8's MLO 8.3 at Evaluate; the
veterinary clinic appears in chapters 5, 7, 8, and 9 (chapter 7 keeps
it as its flagship, the other mentions are single examples, left as
is); the three passes belong to chapter 1 (the canon line corrected).

**Publication refresh list (dated figures that will age):** the EIA
diesel price for the week of October 19, 2026 (chapter 7), the Pew
teen survey of January 2025 (chapter 9), the on-device source of July
2025 (chapter 9), the Colorado interim status between June 30 and
December 31, 2026 (unverified, chapter 8 makes no claim), the vendor
data-policy pages in chapter 8's Tool check, and the roster-tool
re-capture of every sample.

**Open for Mr. Vega:** his Part II review (ongoing) and his Part III
review, and the Flesch ruling for chapters 1-6 (Part III sits inside
the band without merging sentences, which argues the band is
reachable).

## What was done (2026-10-21, late evening): every sample in chapters 1-6 re-captured on the clean harness

Mr. Vega's ruling at 22:20 MST, verbatim: "Re-capture all six chapters'
samples on the clean harness now, have each writer re-check its
commentary against the new responses, then report. Roster-tool
re-capture waits for publication."

**Method.** One brief (`recapture_brief.md` in the Planning session's
scratchpad), six Opus writers in parallel, one per chapter. Each
writer probed the harness first and pasted the answer into its log
header ("No. I don't have any rule about em dashes, semicolons, or
banned words"), re-captured every shown prompt with byte-identical
prompt text (new numbers only where a lesson forced a new prompt),
rebuilt the log from the capture files, and re-read every sentence of
commentary against the new responses. 97 new clean captures: chapter
1 has 8, chapter 2 has 18, chapter 3 has 15, chapter 4 has 16, chapter
5 has 19 (plus the 5 already clean), chapter 6 has 21. Pre-fix entries
that nothing shows were kept and labeled on their headings. The old
captures remain in git history before commit c7f4c84.

**Tool changes (commit e7b739a).** `CAPTURE_MODEL` on both capture
tools for a second-model capture (chapter 6's Tool B is Haiku through
the same harness). `tools/check_samples_vs_log.py` now takes packet
files after the log and checks starter-library sample outputs and the
chapter 2 summary's "Response begins" block, and it reads fences of
any length. `tools/check_key_terms.py` ignores bold inside fences.

**What the clean model changed, by chapter.**

* Chapter 1: the Fix It failed and its repair worked on first clean
  runs. The payroll and spam commentary now matches the new hedges.
  The repair names two historical milestones by product name, as the
  old sample and the Section 1.2 table do, kept because cutting them
  would break the count-the-lines lesson.
* Chapter 2: the Fix It symptom is now a fabricated citation that
  blends two real papers (checked against Crossref, in the log). The
  repair's two citations and the Morton attendance finding were
  verified from Crossref records and the abstract. The lab summary was
  re-captured and now carries one real shift for students to find (the
  cap condition dropped). Try It Yourself 2.5 moved to a new Prompt 24.
  The World Cup and agreement-under-pressure lessons were rewritten.
* Chapter 3: the Fix It failed on the first clean run and the repair
  kept the caveat at exactly 30 words, one over "under 30", which the
  Verify says. The AI-or-person verdict lesson is now a variance
  lesson (all three clean runs said AI).
* Chapter 4: the flagship prompt was unstable (one run of three sent
  two versions, said once). The Fix It's leftover is now two invented
  promises instead of an invented cutoff time, and Try It Yourself 4.5
  builds on them. Removing Format changed almost nothing measurable
  on this run, and the chapter says so.
* Chapter 5: the Output Checklist scoring of the Deskside runs was
  recomputed (run 1 came back with no steps, two invented causes, and
  promises). The fully specified landscaping run now fails "nothing
  added". The starter library's outputs were rebuilt by script.
* Chapter 6: the Fix It's old symptom (a two-change version that
  passed) did not reproduce in three runs, so it was rebuilt as a
  sequence where version 2 still fails, the one-change rows explain
  why, and a version 3 passes. The starter library's outputs were
  rebuilt, its Last run lines corrected ("the textbook author's test
  setup"), and the cold read re-run on the shipped card.

**Checkers at the end:** structure 0 errors, sentence length 0
flagged, every shown sample in the log (chapters and packets), key
terms resolving, style 0 hits, Flesch 72.3, 69.8, 71.4, 74.6, 74.0,
73.4, build clean, deploy verified. The logs hold five em dashes in
chapter 2, one in chapter 3, and none elsewhere: on these prompts the
clean model's tells were Markdown headers, bold, emoji, offers, and
hedges more than dashes.

Instructor keys for Labs 2A, 4A, 5A, and 6A were refreshed in
co-professor from the writers' notes.

**Open for Mr. Vega:** the Flesch band (unchanged), the roster-tool
re-capture at publication (unchanged), whether Fix It 6.1's title
"The Version That Worked" should change now that version 3 is the one
that worked, and the unwritten key for chapter 1's twelve everyday
systems.

## What was done (2026-10-21, late night): chapters 4-6, Part II complete for review, and a capture-harness blocker

Mr. Vega approved chapters 1-3 as written and asked for Part II
unattended with a new rule: every Try It Yourself and every Skills Lab
in chapters 4-6 (and later 10-12) leaves the student holding a tool
they keep, chaining into the reusable prompt library the Part II
milestone promises. The rule is in CLAUDE.md (Rigor Band, Artifact
rule) and docs/part-structure.md ("Part II artifact chain," with the
shared names three parallel writers used verbatim: the five parts of a
prompt, the prompt card, the Prompt Strategy Checklist, the Output
Checklist, the refinement loop, library v1-v3).

**How Part II was built.** One brief (`writer_brief_part2.md` in the
Planning session's scratchpad), three Opus writers in parallel, every
sample captured and logged, one read-only Opus review per chapter
(reports in `docs/reviews/`), every ruled finding applied by its
writer, nothing declined. Rulings made at assembly: few-shot examples
are labeled under the Format part; `[Step k (Part): ...]` is an
accepted label form; Deskside sends the first reply on a remote VPN
ticket and Network Ops fixes the connection; support hours added to
the canon; the landscaping owner is a deliberate Part II thread.

**Chapter 4, Prompt Basics and Prompt Types.** 555 lines, 11 worked
examples, 15 captures. Artifacts: the Prompt Anatomy card, the Prompt
Type picker, the prompt card format, library v1 from six Deskside
tickets. Fix It: a question where an instruction was needed. Review
(0 blockers, 4 majors, 12 minors, 9 nits) caught few-shot commentary
that contradicted its capture, an untested Predict, a Q&A item without
the run it cited, and an MLO verb no task assessed. All fixed, with a
new capture showing the offer vanish once the Constraint named the
behavior.

**Chapter 5, Strategies That Make Prompts Work.** 619 lines, 14 worked
examples, 28 captures (23 before the harness fix, 5 after, the first
clean ones in the book). Artifacts: the Prompt Strategy Checklist, the
Output Checklist, the Prompt Repair sheet, library v2 (the v1 starter
ships three cards with logged outputs). Fix It: the right content in
the wrong shape, repaired with one Format part. Review (1 blocker, 3
majors, 10 minors, 9 nits) found the harness blocker below, a
specificity pair that changed four things while the prose credited
one, Output Checklist checks that overlapped so the chapter scored its
own samples two ways, and a VPN routing contradiction with chapter 1's
canon. All fixed: the pair is now one change (a clean capture), the
checks are sharpened in the chapter, the packet, and the glossary, and
the routing rule is in the canon.

**Chapter 6, Iterative Refinement.** 619 lines, 11 worked examples, 18
captures (one three-turn conversation). Artifacts: the Criteria sheet,
the Refinement Log, the Two-Tool Comparison sheet, the library README,
library v3 ("Copperwind's shared prompt library," two named user
groups). Fix It: a revision that changed two things at once, repaired
to one change. Review (0 blockers, 3 majors, 11 minors, 6 nits) caught
a criterion scored two ways, commentary that outran its capture, and a
graded question without the re-run it cited. All fixed; the v2 starter
now carries its logged sample outputs so it works on its own. The
two-tool comparison used two models from one vendor through the
harness, disclosed in a callout and on the re-capture list.

**The blocker (book-wide).** The chapter 5 review probed the capture
harness and found that the nested `claude -p` call auto-loaded the
repo's CLAUDE.md (from the working directory upward) and the user-level
CLAUDE.md (through settings). Every sample captured before 19:28 on
2026-10-21, in all six chapters, therefore carried the book's own
writing law: no em dashes, no semicolons, the banned-word list, Mr.
Vega's feedback prefixes ("Notes for you:", A1/A2). The samples are
real and unedited, but not what a student's tool returns. Both capture
tools now run from an empty directory with `--setting-sources ""` and
`--exclude-dynamic-system-prompt-sections`; a probe reports no rules
and uses em dashes freely (`--bare` would also work but reads no OAuth,
so it needs an API key this Mac does not have). Every chapter log
carries a dated provenance note naming which prompts predate the fix.
Chapter 5's fix-pass captures are the first clean ones.

**Checkers at the end of the day:** structure 0 errors on all six
chapters, sentence length 0 flagged, every sample fence matched to its
log, every starter-library output matched to its log, every Key Term
resolving, style scan 0 hits, build clean, Pages deploy verified.

**Open for Mr. Vega (Part II review):**

* His edits to chapters 4-6. Chapters 1-3 are approved.
* The re-capture ruling. Options: (a) re-capture all six chapters on
  the clean harness now (scriptable from the logs, then each writer
  re-checks its commentary against the new responses), (b) re-capture
  from a roster product with him before publication, (c) both, (a)
  first. Recommendation: (a) now, because clean samples change what
  some lessons say (a tool that uses em dashes and adds flourishes is
  the tool students will meet), and (b) at publication for the
  samples that matter most.
* Flesch sits above the band on every Part II chapter (74.8, about
  74, 73.0) and on chapters 1 and 3. The checker counts list numerals
  as sentences, and prompt-engineering prose runs plain. His ruling
  whether the band ceiling matters, or whether 70-75 is accepted for
  this book.
* Two-tool comparison in chapter 6: re-capture from two roster tools
  before publication.

## Next steps (after his Part II review)

1. Re-capture per his ruling, chapter by chapter, with the writers
   re-checking commentary; log the new tool and date per prompt.
2. Part III (chapters 7-9): same method, the artifact rule does not
   apply (it returns in Part IV), fading stays at completion prompts
   for chapters 7-8 and problem-first begins at chapter 9.
3. Part IV, then the publication gates G1-G8 and the evaluation
   record in `../evaluations/`.
4. Canvas phase when a shell exists (D14).

## What was done (2026-10-21, night): chapters 2 and 3, Part I complete for review

Mr. Vega approved chapter 1 as written, delegated D10-D15, and asked
for chapters 2 and 3 unattended, then a Part I review.

**How they were built.** One brief
(`writer_brief_part1.md`, in the Planning session's scratchpad; its
substance is the Rigor Band and Pedagogy Upgrade Law sections of
CLAUDE.md plus the chapter blocks in docs/part-structure.md) and one
Opus writer per chapter, in parallel. Every sample response is a real
capture made with `tools/capture_sample.sh` (Claude, Sonnet, through
the Claude Code CLI in print mode, no tools, plain-assistant system
prompt, one fresh conversation per prompt) and logged in full. A
network outage killed both writers mid-run; both were resumed from
their partial state, and the five failed attempts stay in chapter 2's
log labeled as such. Each chapter then had a read-only Opus review
(reports in `docs/reviews/`), and its writer applied the findings the
Planning session ruled in. Nothing was declined.

**Chapter 2, How Generative AI Works and Where It Fails.** 569 lines,
11 worked examples, 18 real captures (3 two-turn), Flesch 69.9. The
Fix It shows a real invented DOI (404 and absent from the DOI system)
beside a real one, repaired by forbidding links and asking for doubt,
with the Morton abstract logged from Crossref to show the paragraph's
attendance claim had no support. Skills Lab 2A: fact-check a
technician's AI summary of a fictional client's office move
(`copperwind-client-update.txt`, `copperwind-ai-summary.txt`, the
summary a logged capture that came back nearly accurate, so the lab
proves what held and reports what shifted or dropped). The review
(0 blockers, 4 majors, 14 minors, 9 nits) caught an Understand verb
under an Analyze tag, an undercounted Verify step, a lab premise that
pasted a client update without comment, and CLO 2 claimed but not
assessed. All fixed.

**Chapter 3, Research, Creative Work, and Responsible Use.** 560
lines, 10 worked examples, 16 real captures, Flesch 71.4. The Fix It
shows a summary that dropped its source's caveat (four attempts to get
a real failure, all logged) repaired with one change at the original
word limit. Detector claims rest on two 2023 studies with figures
checked against the PDFs. The AI-or-person test uses an 1898 public
domain passage. Skills Lab 3A: a newsletter packet for Priya Sharma
(`priya-newsletter-brief.txt`, `newsletter-sources.txt`) with a
privacy plan written before the first prompt, leads checked against
primary sources, a disclosure, and a reconciliation. The review
(0 blockers, 5 majors, 19 minors, 10 nits) caught the privacy check
running after the prompts, a repair that changed two variables, an
unmarked trim that hid the tool's own note, and an MLO that promised
students could distinguish AI-made content. All fixed.

**Assembly.** Glossary gains 22 terms through `tools/merge_glossary.py`
(no duplicates; chapter 3 owns "primary source" and "citation", chapter
2 owns "RLHF" and "DOI"). Chapters 2 and 3 are live in the nav.
`tools/check_style.py` now scans prose only, because captured
responses are evidence and are never edited to satisfy a word list.
`tools/check_samples_vs_log.py` and `tools/check_key_terms.py` are the
other two per-book checkers added today. Instructor answer keys and
judgment notes for Labs 1A-3A live in co-professor at
`01-teaching/11-cis137-ai-fundamentals/textbook-instructor-materials/`,
never in this public repo.

**Checkers at the end of the day:** structure 0 errors on all three
chapters, sentence length 0 flagged, every sample fence matched to its
log, every Key Term resolving, style scan 0 hits, build clean, Pages
deploy verified.

**Open for Mr. Vega (Part I review):**

* His edits to chapters 2 and 3. Chapter 1 is approved.
* Capture provenance: every sample in the book came from Claude
  through a command-line harness, not a roster product. Re-capture
  from a roster tool before publication is his call. The log format
  records tool and date so a re-capture is a swap, not a rewrite.
* Flesch sits just above the band on chapters 1 (72.4) and 3 (71.4),
  inside it on chapter 2 (69.9). The writers stopped merging sentences
  where it read worse. His call whether the band ceiling matters.
* The chapter 1 answer key for the 12 everyday systems is still not
  written (co-professor instructor file notes what exists).

## Next steps (after his Part I review)

1. Fold his Part I edits into the law if they change a pattern.
2. Part II (chapters 4-6): same method, three chapters, one brief,
   one writer each or three per agent as he prefers, fading begins in
   chapter 5 (completion prompt), reviews before anything is called
   done.
3. Parts III and IV, then the publication gates G1-G8 and the
   evaluation record in `../evaluations/`.
4. Canvas phase when a shell exists (D14).

## What was done (2026-10-21, evening): the fluency contract and the rigor band

Mr. Vega's rulings, in his session, after reading chapter 1:

* **A1, the rigor band.** CIS137 sits between AI literacy (the four
  "fluency" courses he has seen were too basic for a bachelor's IT
  student) and AI engineering or machine learning (not the aim).
  Students finish as the human in the loop: able to direct an AI
  tool, check its work, and decide when not to use it. The district's
  term "AI fluency" stays, and he expands on the CLOs under his
  academic freedom, in line with the district's intent. The contract
  goes up front: the book's home page, the Canvas course home page,
  and chapter 1.
* **A2, the audience.** With Mr. Tagart and Mr. Olson he expects
  CIS137 to be a first- or second-year elective in the bachelor's
  pathway in information technology, pushed as a first choice.
* **A3, the description.** Revised: "Learn how AI models work, direct
  them with prompts, audit what they produce, and select and defend AI
  solutions as the human in the loop."
* **A4, D13.** Closed as Copperwind IT Services.

What changed:

* New published page `book/fluency-contract.md` (the aim, the three
  bars with a six-row table, the five habits of the human in the loop,
  what comes next, how the contract reaches the grade, the course
  reading of each competency, who the course is for). Its snippet
  block is transcluded into `book/index.md` under "The Fluency
  Contract," and it sits second in the nav after Home.
* Chapter 1's introduction links to the contract in its second
  paragraph. Anatomy unchanged.
* `CLAUDE.md`: new "Rigor Band: The Fluency Contract" section (rules
  for every chapter writer: a Rigor step per chapter, a manager-ready
  Part 3 artifact per lab, real vocabulary and primary documents,
  drift guards for chapters 2, 7, 9, 10, and 11, floor at zero and
  ceiling through Part 3 and Mastery), the audience line, the Purpose
  line.
* `docs/part-structure.md`: a Rigor step line in all twelve chapter
  blocks, a rigor-band paragraph, the audience line, and the spine
  section now records the D13 ruling.
* `docs/CIS137_CLOs.md`: "Course Reading of Each Competency" table
  (official wording verbatim beside what this course asks for).
* `docs/style-guide.md`, `README.md`, `zensical.toml`: audience,
  description, nav, and tree updates.
* Canvas phase note: the course home page (Module 0) quotes the
  contract from `book/fluency-contract.md` when that phase opens.
* HQ: D13 answered. D16 filed as an answered Decision recording the
  rigor-band ruling so other agents can find it.

## What was done (2026-10-21, later): Opus review of chapter 1 folded in

The review (Opus, read-only, brief in the Planning session's scratchpad)
found 0 blockers, 8 majors, 27 minors, and 19 nits. What changed:

* MAJOR 1: the spam-filter commentary said the assistant "did not
  answer yes or no" while its own sample opens "Yes." Rewritten.
* MAJOR 2: "every tool is narrow" is now framed as a limit (no reliable
  planning, self-checking, or learning a new job) instead of a one-job
  rule that the multimodal paragraph contradicted. The glossary entries
  for narrow AI and AGI, Key Concepts, Retrieval item 2, Review Q3, and
  Lab Part 1 Task 3 match.
* MAJOR 3: the AI winters are no longer mapped onto the eras. The
  milestones table carries separate 1970s (first winter) and 1980s
  (expert systems, then the second winter) rows.
* MAJOR 4: the chapter states a test for rule-based system versus not
  AI (do the rules stand in for a judgment a person would otherwise
  make?) with a captured worked example, the payroll question (log
  Prompt 7). The lab accepts either answer when the test is applied.
* MAJOR 5: the teaching text no longer pre-answers the lab. The
  thermostat, tax deduction, VPN router, "WIRE TRANSFER" rule, face
  unlock, and "Because you watched" examples are replaced. In the
  packet, everyday system 10 is now a 1959 checkers program that
  learned by playing itself (Deep Blue stays in the chapter), and
  Copperwind item B is now a license-plate camera.
* MAJOR 6: the Era column is gone from the milestones table. Quick
  Check 1.2 Q1 and Lab Part 2 Task 1 ask students to place a milestone
  and defend a borderline case, not look one up.
* MAJOR 7: worked examples went from 4 to 8. New captures: the payroll
  question (Prompt 7) and the spam question run a second time (Prompt
  8, shown in Section 1.4 as "The Same Question, Asked Again" to teach
  why samples are samples). The logged responses to Try It Yourself
  1.4 and 1.5 appear after each Explain step as "Compare your run."
* MAJOR 8: the worksheet mirrors every chapter task word for word,
  with the pilot-risk line, the "your own prompt" slot, the two-label
  scheme (IN MY PROMPT or ADDED BY THE TOOL), and both Questions &
  Analysis questions. Headings read "Part 1, Task 1" so they no longer
  collide with section numbers.
* Minors applied: AI expanded on first use; the "forty words in this
  order" line; neural network defined by layers and deep by many
  layers; early learning ideas acknowledged inside the rules era; the
  1955 proposal versus 1956 workshop naming; the Section 1.4 subgoal
  labels sit on sentence boundaries (three steps) with "send it
  without the [Step] lines"; two sentences that paraphrased the
  captured Fix It response rewritten; colons instead of spaced hyphens
  in Further Reading; Elements of AI (University of Helsinki) replaces
  the vendor crash course; the three era terms added to the glossary
  and Key Terms, and the Turing test defined in prose; the comparison
  table's empty header cell named; three closing flourishes trimmed;
  Diagnose no longer gives away the three missing parts; TIY 1.2's Run
  step checks the prediction against the diagram; two Quick Check
  items raised to Apply; TIY 1.3 scoped to five apps; an under-18 line
  in the account steps; required steps moved out of admonitions into
  prose and a numbered list; the data-policy claims dated and hedged;
  Quick Check 1.3 Q3 no longer bends the rule; "Several systems can be
  argued two ways"; MLO 1.2 extended to the winter pattern so CLO 4
  has an MLO behind it, with Part 3 tagged to it; Review Q4 moved to
  a clinic case instead of repeating Lab Part 3 Task 2; the log's line
  count for Prompt 2 corrected.
* Not applied, for Mr. Vega: capture provenance (all eight samples are
  Claude through the Agent SDK or the Agent tool, not a roster
  product), the license (D15), and the remaining voice choices. Flesch
  is 72.2 after the additions, just above the band.
* Checkers after the pass: structure 0 errors, sentence length 0
  flagged, build clean, every labeled sample fence matched to the log
  by script, every Key Term resolves to a glossary headword.

## What was done (2026-10-21): scaffold and course references

* Read the MCCCD context pack (`docs/mcccd/`), the family README and
  setup guide, the CIS133 and CIS215 exemplars (CLAUDE.md, CLOs,
  chapter template, chapter 1), the quality rubric V2.1, the pedagogy
  playbook V1.1, and the CIS133 pedagogy spec (Copperwind canon).
* HQ first: no CIS137 project or task existed. Created the Project,
  the CIS137 Context (Course), and the build task (claimed, In
  progress, delegated by Mr. Vega).
* Instantiated the template in place (`cp -R ../template/. .`),
  removed the setup guide, replaced every token (grep returns
  nothing), synced the shared files, seeded the Bloom's reference,
  built the venv (Zensical 0.0.46 plus textstat).
* Wrote `docs/CIS137_CLOs.md`: the six official competencies verbatim
  with MCCCD's section references, RBT-tagged CLOs that keep the
  official wording, a CLO-to-chapter map, chapter alignment blocks,
  the full outline, and the certificate context.
* Wrote `docs/part-structure.md`: 12 chapters in 4 Parts that follow
  the outline sections in order, with the design rationale, coverage
  matrices, dependencies, and the spine proposal. Awaiting approval.
* Filled the course-configured sections of `CLAUDE.md` (Flesch band,
  Bloom's rule, worked-example length, load pattern, naming, tool
  targets, terminology, quick-reference CLOs) and added the Pedagogy
  Upgrade Law section with the checker contract.
* Wrote `docs/style-guide.md` (course layer), `docs/tool-roster.md`
  (proposal), `book/index.md` (home page with verbatim CLOs), and the
  glossary header in the CIS133 definition-list format.
* Adapted the CIS133 chapter template to prompt-and-response worked
  examples (`templates/chapter-template.md`) and the CIS133 structure
  checker to this book (`tools/check_course_structure.py`: 5 TIYs per
  chapter, no executable-language fences). Copied the readability
  checker.
* Checked the Maricopa schedule snapshot (no CIS137 section for
  Phoenix College) and the Canvas API (no CIS137 shell among 54
  teacher enrollments).

## Decisions filed in HQ (2026-10-21), all answered

Mr. Vega approved chapter 1 as written on 2026-10-21 and delegated
D10, D11, D12, D14, and D15 to Claude ("choose for me"). D13 he ruled
himself. D16 records the rigor band.

1. D10 Tool roster: adopted as written in `docs/tool-roster.md`.
   Verify district facts and vendor age rules before the first
   offering.
2. D11 First offering term: Fall 2027 working assumption, task list
   `cis137-fall27`. Nothing in the book depends on it.
3. D12 Chapter plan: `docs/part-structure.md` is Authoritative.
4. D13 Spine: Copperwind IT Services (Mr. Vega, A4).
5. D14 Canvas shell: none exists. Canvas phase parked. He requests
   `pc.dev.cis137.vega` when the course is scheduled.
6. D15 License: CC BY-NC-SA 4.0, shown on the home page, in the
   README, in every data-pack README, and in the site footer.
7. D16 Rigor band: the fluency contract (see the evening entry).

## Pending

* Mr. Vega's Part IV review (chapters 10-12). Chapters 1-9 are
  approved as written (2026-10-22).
* The outside OER review the rubric names as the next step after the
  Publication-ready label.
* The remaining items in the post-revision record: chapter 10's
  Flesch ruling, the vendor-fact refresh before each offering, the
  dated figures, and the roster-tool re-capture decision.
* Then the roster-tool re-capture, the vendor-fact refresh, and the
  Canvas phase when a shell exists (D14).
* The one-sentence course description was revised on Mr. Vega's A3
  ruling (2026-10-21) to carry the rigor band. It lives in
  `zensical.toml`, `README.md`, `CLAUDE.md`, and `book/index.md`.

## Next steps

1. Chapter 1 end to end (every section of the locked anatomy, the
   Skills Lab with the transcluded rubric, the five upgrades, the
   checkers green). Stop for Mr. Vega's edits. His version is the law
   for chapters 2-12.
2. Chapters 2-12: fan out to Opus subagents, three chapters per agent,
   one brief file, one output file each. Assemble, run the checkers,
   get a review (Codex plugin or Opus; the CLI `codex review` fails
   on the configured model as of 2026-10-21).
3. Publication gates G1-G8. Record the evaluation in
   `../evaluations/`.
4. Canvas phase only when a shell exists and Mr. Vega says go. The
   Canvas build lives in co-professor under
   `01-teaching/<NN-cis137-...>/canvas-pages/`, not here. The course
   home page quotes the fluency contract (`book/fluency-contract.md`)
   up front, per the 2026-10-21 ruling.

## How to continue

```bash
cd /Users/vega/Documents/code/textbooks/cis137
export CLAUDE_CODE_TASK_LIST_ID=cis137-fall27
.venv/bin/zensical build --clean          # must report no issues
python3 tools/check_course_structure.py --all
python3 tools/check_sentence_length.py book/chapters/chapter-01.md
.venv/bin/python tools/check_readability.py
```

Read `CLAUDE.md`, then `docs/part-structure.md`, then
`docs/CIS137_CLOs.md`. Every sample AI response in a chapter is
captured from a real run and logged in `docs/execution-logs/`.

## Stand-down (2026-10-21)

Mr. Vega ruled on 2026-10-21 that his session "CIS137 Planning" is the
dedicated CIS137 build session and that this session (cis137-build)
stands down. His words, relayed by the session that started this one:
"I want that other session to compare your version to it's own and
continue with the best of both notes." Everything below exists so that
comparison can happen. Nothing was deleted: no files, no HQ records, no
branches. Every change in the working tree was committed and pushed.

### (a) Exact state of work in progress

* **Chapter 1 draft:** `book/chapters/chapter-01.md`, 458 lines,
  unreviewed by Mr. Vega. Complete anatomy N.1-N.7: 3 MLOs (Analyze,
  Analyze, Apply), CLO block (CLO 2, CLO 4), five Try It Yourself
  blocks numbered 1.1-1.5 in reading order, four Quick Checks, Fix It
  1.1 in Section 1.4 (the vague "Tell me about the history of AI"
  prompt and its 560-word response, repaired to a five-line prompt),
  two flagship examples with `[Step k:]` labels (the three-way spam
  filter diagram in 1.1 and the four-part first prompt in 1.4), five
  Retrieval Practice items, Skills Lab 1A "Map the AI Around You"
  with the rubric transclusion, four Review Questions, five Further
  Reading links, Looking Ahead. Copperwind is introduced in Section
  1.4 before Try It Yourself 1.5 and carries Skills Lab Part 3.
* **Checker results at stand-down:** `tools/check_course_structure.py`
  0 errors. `zensical build --clean` no issues. Flesch 71.0 (chapter),
  68.2 combined, index.md 52.5 (below band, not yet addressed).
  **Known hits NOT fixed because the stand-down came first:**
  `check_sentence_length.py` flags six sentences at 35+ words (lines
  5, 104, 194, 364, 413, 458). Three prose semicolons sit in the
  "Sample response (captured from a chat assistant, October 2026; your
  output will differ):" labels at lines 60, 239, 317 (replace the
  semicolon with a period). `book/glossary.md` line 39 uses "rather"
  (banned filler) in the generative AI definition. No Codex or Opus
  review has run. No source manifest exists yet.
* **Glossary:** `book/glossary.md`, 21 chapter 1 terms in the CIS133
  definition-list format. Every Key Term in chapter 1 resolves to a
  headword (checked by script).
* **Data pack:** `assets/code/chapter-01/` holds `README.md`,
  `everyday-systems.txt` (12 systems), `copperwind-ai-inventory.txt`
  (Mei Lin's brief, items A-H), `skills-lab-1a-worksheet.md`. No
  instructor answer key has been written for the 12 systems.
* **Execution log:** `docs/execution-logs/chapter-01-responses.md`.
  Six prompts captured 2026-10-21 from Claude (Anthropic) run through
  the Claude Agent SDK (Sonnet) as a plain chat assistant with no
  tools and no memory between prompts. The chapter quotes them
  verbatim with `[...]` trims. Re-capture from a core-roster tool if
  Mr. Vega prefers, and update the log and the chapter labels.
* **Nav and home page:** chapter 1 is uncommented in `zensical.toml`
  and linked from `book/index.md` Getting Started. Pages deploys of
  the earlier commits succeeded (run 39639719824); the deploy of the
  stand-down commits was not checked.
* **Further Reading URLs** checked with curl on 2026-10-21: the UMBC
  copy of Turing's paper (200, replaced the Oxford Academic link that
  returned 403), the Dartmouth proposal PDF (200), arXiv 1706.03762
  (200), the Stanford AI Index (200), the Google ML Crash Course
  (200). The MCCCD course URL in `book/index.md` returns a Cloudflare
  403 to curl and needs a browser check for the source manifest.
  ai.maricopa.edu also returned 403 to curl (used only in the roster).
* **Not started:** chapters 2-12, subagent briefs, the publication
  gates, the Canvas phase. `README.md` still says 0 of 12 chapters
  and leaves the license as a TODO (HQ D15). The one-sentence course
  description in `zensical.toml`, `README.md`, `CLAUDE.md`, and
  `book/index.md` is a draft the starter prompt asked to confirm.

### (b) Cross-session messages received today, and what was done

These exist only in this session's transcript, so they are recorded
here in full substance.

**From "CIS137 Planning" (after the collision), five points:**

1. *Files.* It overwrote `book/index.md`, `docs/CIS137_CLOs.md`, and
   `docs/part-structure.md` at 10:01 and reported restoring them at
   10:03 from b6e509c. In fact this session's commit 6401a24 at
   10:02:43 had already swept its versions into HEAD, so its checkout
   was a no-op. This session restored its own versions from b6e509c
   in commit 732d575. The Planning session's drafts remain in history
   at 6401a24 (see section c).
2. *HQ duplicates.* It created a second Context (recgSbFUS6NYamahA)
   and a second Project (recnMAC0PeEgIBfiL) before finding this
   session's records, renamed both "DUPLICATE, please delete", and
   archived the project. Only Mr. Vega deletes HQ records. Nothing
   was done to them here.
3. *Bug report.* `CLAUDE.md` line 7 held a literal mangled regex
   backreference (`\1**Certificate:**...\n`) and the Primary Tools
   line was missing, from a lambda-based replacement in this session's
   fill script. Fixed in 732d575: the Primary Tools line is restored
   and the Certificate line follows it.
4. *District facts from its web search (unverified by this session):*
   help.maricopa.edu (SCC KB article 139) says all enrolled students
   get Microsoft 365 Copilot via MEID@maricopa.edu at
   m365.cloud.microsoft/apps, and PVCC's AI Tools page points to
   copilot.microsoft.com with MEID credentials. A CGCC CTLA page says
   District ITS enabled Gemini, NotebookLM, and Workspace Studio for
   faculty and staff only, with guidelines in development at the AI
   Resource Center (ai.maricopa.edu). MCLI publishes faculty guidance
   on generative AI and academic misconduct. Age rules from secondary
   guides: ChatGPT 13+ with guardian permission under 18, Gemini 13+
   on a personal account, Copilot 13+, Claude 18+ with no consent
   route, Perplexity 13+ with a parent accepting the terms. Folded
   into `docs/tool-roster.md` under "District facts (reported, not
   yet verified)" and into HQ D10's Detail and Recommendation (Copilot
   through the student's MEID becomes the one guaranteed tool).
5. *Alternative spine:* "Kestrel Row Books," a fictional independent
   bookstore and cafe (two Phoenix-area stores plus an online shop; its
   web search on 2026-10-21 found no name collisions). It puts invented
   quotes and ISBNs (accuracy), cover-art ownership (copyright),
   customer data (privacy), and hiring (bias) in one small
   organization, and its sales data gives CIS144 and CIS218 somewhere
   to continue. Added as option B on HQ D13 (this session's
   recommendation stayed Copperwind). Its per-chapter spine blocks are
   in `git show 6401a24:docs/part-structure.md` and in that session's
   scratchpad at
   `/private/tmp/claude-501/-Users-vega/14842cef-2247-4d17-b111-816bd27daec9/scratchpad/cis137-parallel-drafts/`.

**From the session that started this one (relaying Mr. Vega):** the
stand-down ruling quoted at the top of this section. This section and
the two commits are the response.

### (c) Comparing the two versions

The Planning session's drafts of the three files live at commit
6401a24. This session's versions are at HEAD. Compare with:

```bash
git show 6401a24:docs/part-structure.md
git show 6401a24:docs/CIS137_CLOs.md
git show 6401a24:book/index.md
git diff 6401a24 HEAD -- docs/part-structure.md docs/CIS137_CLOs.md book/index.md
```

Differences noticed in passing, for the comparison: the Planning
session numbers the CLOs with Roman numerals (CLO I-VI) while this
session uses MCCCD's own Arabic numbers (CLO 1-6) so outline sections
(Roman) and competencies (Arabic) never collide. Its CLO document says
no MLO is tagged Create and that Chapter 12 is primary for no CLO.
Its home page maps to an 8-week course (the family documents say 9-)
and drops the Sources & Permissions section. It adds an "office-suite
assistants" row to the tool table. This session's `CLAUDE.md`, chapter
template, chapter 1, HQ Decisions, and this HANDOFF all use the Arabic
numbering, so a switch to Roman needs a sweep across those files.

### (d) HQ records this session created

| Record | ID |
| ------ | -- |
| Project: CIS137 textbook and Canvas build | recu4GSoXTE381m4m |
| Context: CIS137 (Course) | recQcWyyt9Sj7Gr5r |
| Task: Build the CIS137 textbook (In progress, assignee Claude, delegated by Mr. Vega) | recTFTaVUmjkeeoOP |
| D10: tool roster | recZkdNwJ82lco6dE |
| D11: first offering term | reczXLgPTQBc6OPxN |
| D12: chapter plan | rectiIQLXMNValu0q |
| D13: resumable spine | recMI08ZOEjtqD1Cq |
| D14: Canvas shell | receSuoL6KpnnLNUB |
| D15: book license | rec1pXkMYJvlyFhAA |

The two records the Planning session created (Context
recgSbFUS6NYamahA, Project recnMAC0PeEgIBfiL) are already marked
Dropped and renamed "DUPLICATE, please delete". (Deleted later the
same day on Mr. Vega's ruling.) The task Status was
left as In progress for the Planning session to carry. No Decision
record was changed at stand-down.
