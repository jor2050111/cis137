# Review: Chapter 10, Surveying and Comparing AI Platforms (Opus, read-only)

Reviewed 2026-10-22 against `review_brief_part4.md`. No file was edited.
Line numbers refer to `book/chapters/chapter-10.md` unless another file is named.

## What I ran and opened

* `check_samples_vs_log.py`: 9 sample blocks, 0 lines not in log. `check_course_structure.py`: OK, 0 errors. `check_sentence_length.py`: 473 sentences, average 14.1, longest 34, 0 flagged. `check_style.py` on the chapter and every packet file: 0 hits. Readability: Flesch 72.5 (ch 6 73.4, ch 7 68.0, ch 8 64.7, ch 9 67.6).
* Hand walk of every fence: a script checked each `[...]`-delimited segment of each chapter fence for a contiguous match in its log fence, plus unmarked top and bottom cuts. All 13 response and prompt fences pass. The two flagship prompts, with `[Step]` lines removed, equal the logged prompts (whitespace-normalized). Every log response is byte-identical to `caps-10/rK.txt`. `mK.txt` confirms Sonnet = Tool A (1, 2, 3, 5, 8, 9) and Haiku = Tool B (4, 6, 7, 10). `wc -w` on the capture files reproduces every word count in prose (74, 75, 71, 64, 134, 141, 110, 376). Probe line is in the log header and matches `caps-10/probe.txt`.
* Vendor pages, opened by me on 2026-10-22 (WebFetch and the built-in browser): gemini.google/subscriptions; Gemini Apps Privacy Hub (support.google.com/gemini/answer/13594961); "Manage & delete your activity in Gemini Apps" (answer/13278892); help.openai.com "Data controls in ChatGPT" and "What is ChatGPT Plus?"; microsoft.com Copilot business pricing; microsoft.com/en-us/microsoft-365/premium; support.microsoft.com "Privacy FAQ for Microsoft Copilot" and the new "Microsoft Copilot for individuals" pages (overview, privacy-controls, activity-history); claude.com/pricing; privacy.claude.com "Is my data used for model training?"; anthropic.com/news/updates-to-our-consumer-terms; anthropic.com/legal/consumer-terms; perplexity.ai/pro; notebooklm.google/plans (301 to notebook.google/plans). Further Reading: all five links return 200 today, and the WCAG 2.2 header still reads "W3C Recommendation 12 December 2024".

## BLOCKER

**B1. Line 369: the Microsoft training fact comes from a page that says it no longer applies to the current Copilot app, and the current app's page says the opposite.**
The callout says Microsoft uses consumer Copilot conversations for AI training "except for certain categories of users or users who have opted out" and stores them 18 months, citing "Privacy FAQ for Microsoft Copilot." That page now opens with: "An updated version of the Microsoft Copilot app for web, desktop, and mobile devices is available as of August 18, 2026. The information in this article applies only to the older version of the Microsoft Copilot app." The current-app page ("Microsoft Copilot for individuals: your activity history," support.microsoft.com/en-us/privacy/microsoft-copilot/activity-history) states: "Prompts, responses, and your file contents when using the Microsoft Copilot app aren't used to train foundation models." A student filling the Data policy line from this callout would record a training default that is wrong for the app they actually use. The callout also drops the FAQ's own exclusion of "any Microsoft 365 consumer users or Copilot conversations integrated within Microsoft 365 consumer apps." It says only organizational accounts are excluded, right after naming Microsoft 365 Premium, the consumer plan that exclusion covers.
Fix: re-read the "Microsoft Copilot for individuals" page set (overview, privacy controls, activity history) and the "Copilot in Microsoft 365 apps for home" page. State the current-app training line with its title and date. If the old FAQ stays, say it covers only the pre-August 18, 2026 app. Re-check the 18-month retention line against the new pages. It is not on the activity-history page I read (unverified for the new app).

## MAJOR

**M1. Line 369: the Gemini line leaves out the training default, which is the fact the card asks for.**
"With Keep Activity on, Google uses your activity ... including training generative AI models" is accurate, but it is conditional. Google's own help page answers the default directly: "If you're 18 or over, Keep Activity is on by default" ("Manage & delete your activity in Gemini Apps," support.google.com/gemini/answer/13278892, read 2026-10-22). TIY 10.1's Predict asks "does it train on your input by default," and the callout cannot settle it for this tool. The writer's log says the Privacy Hub "does not say in one sentence whether Keep Activity starts on," which is true of that page only.
Fix: add the default with its source, for example: "Keep Activity is on by default for users 18 or over ('Manage & delete your activity in Gemini Apps')." Consider also adding the Privacy Hub's 72-hour line for chats with Keep Activity off. Small detail, but it is exactly what "what it keeps" asks for.

**M2. Lines 45 and 369: the Perplexity and NotebookLM deferrals are refuted today, and the callouts still use a product name the vendor has dropped.**
Both pages render as readable text in a normal browser. perplexity.ai/pro shows Pro at "$17 /month when billed annually" and Max at "$167 /month when billed annually" (the monthly price is unverified; I did not toggle the page). notebooklm.google/plans returns 301 to notebook.google/plans, titled "Gemini Notebook Plans." It lists a standard plan, "Gemini Notebook in Google AI Plus / Pro / Ultra," and Workspace and Cloud editions. Its data line reads: "When you use Gemini Notebook as an individual, your data is not used for training unless you share feedback." Line 45 still lists "NotebookLM (Google)" as a roster research tool. Line 369 says its plan page "did not load." A student following the chapter's own lesson (names move, date every fact) would find the callout stale on day one.
Fix: put both tools' tier, price, and data lines in the 10.4 callout with titles and the date. Rename the 10.1 roster entry "Gemini Notebook (Google, formerly NotebookLM)", or whatever `docs/tool-roster.md` rules. Flag the roster file for the same update (out of scope for this chapter, but it feeds every Part IV callout).

**M3. Lines 333 and 344: the Fix It's "7 of 8 tie after repair" rests on a claim-scoring ruling applied two ways.**
Tool A (Prompt 5, log line 170): "ten backup codes, which are one-time passcodes for emergencies" is ruled an in-sentence definition and not audited. Tool B (Prompt 7, log line 208): "ten backup codes, which you can use if you can't reach your phone" is audited as a claim, Not in source. Both are relative clauses glossing the same term. Neither is in the facts ("one-time" is not there either). Under either consistent ruling the result is not a tie:
* If both are definitions, Tool B scores 7 of 7 hold and Tool A 7 of 8.
* If both are claims, Tool A scores 9 checked, 7 hold, 2 Not in source, and Tool B 8 checked, 7 hold, 1 Not in source.
The other Task 3 counts hold up. The unfair row's 7 claims (2 hold, 1 contradicted, 4 not in source) sum correctly, and the contradicted "sends a short code to your phone" against "We do not use text-message codes" is right. The Task 1 rows are also right: Tool A 5 checked, 4 hold, 1 Not in source in both runs ("likely fine," then "is working"). Tool B is 3 of 3 in both runs, and the word counts match.
Fix: pick one ruling for glosses and rescore both Task 3 rows. Then either rewrite 333-344 to report the result honestly ("Tool B ahead by one claim, one run each, so a lead that needs a second run"), which also strengthens the "one run is a lead" lesson, or move the line the writer drew. Update the log observations and notes-10.md to match.

**M4. Line 366: a vendor fact in prose.**
"The address of one roster research tool's plans page redirected to a page under a new product name" is a dated vendor fact outside a Tool check callout. It names no vendor, but G1 places the fact type, not just the name, inside a callout. It also disagrees with line 369, which says the same tool's page "did not load as readable text."
Fix: keep the lesson sentence generic in prose ("Even names move: a plans page can redirect to a new product name"), and put the dated specifics in the 10.4 callout with M2's update.

## MINOR

**m1. Line 369, Anthropic.** "That page does not state the default" is accurate for the Privacy Center article I read (updated March 16, 2026). But the student is left unable to fill the card, and Anthropic's own announcement gives facts the card needs. It says: "If you're a new user, you can select your preference in the signup process." It gives retention of five years "if you allow us to use your data for model training," otherwise "our existing 30-day data retention period." It also says the change covers only "Claude Free, Pro, and Max plans," with commercial plans excluded. The training-default question stays unverified from a primary page. Fix: add the signup choice, the two retention periods, and the plan scope with the source title, and tell the student to read their own setting.

**m2. Line 45, "18+ under its reported terms."** The Consumer Terms (effective Oct 8, 2025) state it directly: "You must be at least 18 years old or the minimum age required to consent ... whichever is higher." "Reported" reads as hearsay. Fix: "18+ under its Consumer Terms."

**m3. Line 369, Microsoft 365 Copilot Business.** The pricing page shows "Originally starting from \$21.00 now starting from \$18.00 ... user/month, paid yearly." The \$18 is a promotional price. Fix: "from \$18 (promotional, listed down from \$21)".

**m4. Lines 45 and 369, Microsoft tiers.** The callouts give no free consumer Copilot tier, though the roster's general assistant is Microsoft Copilot. Line 45's "Microsoft 365 Copilot, where a school or work account includes it" blurs the paid Microsoft 365 Copilot license with the Copilot Chat that work and school accounts get. The district license is still unverified (notes line 48). Fix: name the free consumer tier with its source, and say "Microsoft 365 Copilot or Copilot Chat, depending on what your school or work license includes."

**m5. Lines 292-313, Fix It Symptom and Diagnose.** The Diagnose asks the student to "compare what each row was sent," but the Symptom prints only Tool B's prompt. Tool A's prompt first appears in the Repair. The student cannot do the Diagnose step from the page. Separately, "compare what each row was sent" points straight at the answer. Fix: print both prompts in the Symptom as "his fair test record," and recast the Diagnose to hold back: "Before you touch the matrix, list everything the two rows had in common and everything that differed. Then name, in one sentence, what the accuracy column is measuring."

**m6. Line 204, TIY 10.3 Explain.** "whether the difference between your two rows came from the tools or from your prompt": both tools got the same prompt, so the live alternative is run-to-run variation, not the prompt. Fix: "came from the tools or from chance between runs, and what a second run would show."

**m7. Line 128, WCAG quote.** SC 2.1.1 is quoted as a complete sentence ending in a period, but the sentence continues "without requiring specific timings for individual keystrokes, except where ..." (log line 297). Fix: end the quote with "interface ..." or quote it whole.

**m8. Lines 344 and 333, verdict choice.** Tool A's "a stranger who learns your password still cannot get in" is called "a promise Deskside never made" but scored Not in source. Chapter 7 (line 43) defines Unverifiable to include predictions and promises. Fix: either score it Unverifiable, or say in one clause why it stays Not in source (a security record could settle it). Do this alongside M3's rescoring.

**m9. TIY 10.5 (lines 435-437) on the starter card.** The Tool A card's Name ("Tool A, the textbook author's test setup") and its vendor lines can never be fixed, because Tool A is not a product. A reviewer will flag them, and the COMPLETE/CURRENT sort breaks on them. Fix: tell students to mark Tool A's vendor lines "not a product, skip," or run the review on their own TIY 10.1 card and use the Tool A card only as the model of a Last tested line.

**m10. Lines 208-217 and 318, model prompts for lab tasks.** The chapter prints a working prompt for Task 1 and for Task 3 (with the facts). Students can paste both into Lab Part 2, so only Task 2 tests prompt writing (notes line 63 says this was deliberate). Not an answer leak in the scoring sense, because the runs and counts are still the student's, but a ruling for Mr. Vega. Option: have the lab say students may reuse the chapter's prompts for Tasks 1 and 3 and must write Task 2's themselves, so the choice is open rather than accidental.

## NIT

* **n1. Line 276.** The note says the cost, privacy, accessibility, and integration cells "are blank." The table fills them with "Same vendor and setup ..." and "Not tested (command line)." Say "carry no finding."
* **n2. Line 12.** The Prerequisites bullet lacks its closing period.
* **n3. `tool-survey-starter.md` line 26.** The Notes leave out the type of AI behind the main feature, which the template's Notes guidance asks for. "A guess about the cause" would read more exactly as "a guess that the printer itself is fine."
* **n4. Lines 130, 273, 286.** Short closers ("The matrix shows both." "That is the whole finding." "Mei Lin needs both.") cluster near the maxim line. Each is fine alone. Vary one.
* **n5. Line 124.** FERPA is named without a source. Chapter 8 covers it with 20 U.S.C. § 1232g and 34 CFR Part 99, so add "(Chapter 8)" to point at the sourced treatment rather than citing again.

## Checks that pass

* **Artifact rule (check 1).** Every TIY names its artifact in the Run step: 10.1 the first card, 10.2 the checks table, 10.3 two filled rows, 10.4 the finished two-row matrix, 10.5 the reviewed survey. The student's own IT project appears in every section (lines 93, 157, 184, 387). Lab Part 3 yields three matrices, the cards, and the Mei Lin note. The templates carry the chain's verbatim field names in order: eight card fields, and six criteria with the chain's parentheticals. No answers sit in the packet. The README carries the canon disclaimer and the license. No vendor is named in the packet.
* **Agents guard (check 2).** No code, configuration syntax, API, or framework content anywhere, captured fences included.
* **Samples vs log (check 4).** Clean, as above. No invented or edited text found. Every number the prose calls checked is in the log.
* **Fair-test discipline.** Every compared pair used the same prompt (Prompts 3, 4, 9, 10 identical, and 5 and 7 identical, checked), fresh single-turn conversations, the same day, and the same checks. The prose attributes the Task 1 difference to the tool and discloses one vendor through one harness in a callout. M3 is a scoring-consistency problem, not a fairness breach in the runs.
* **Anatomy (check 6).** Three Evaluate MLOs (Judge, Defend, Assess) with section bindings. The CLO block is verbatim, CLO 2 is assessed by TIY 10.1 and Quick Check 10.1 item 1, and CLO 6 throughout. There are 5 TIY, 4 Quick Checks at Apply or above, 1 Fix It with a real first-try failure, and 5 Retrieval items with "From Chapter 8:" and "From Chapter 6:" (both answerable: the seven policy sections in ch 8 line 324, the four traits in ch 6 line 40). Q&A has 2 items citing the log, the rubric block is short, the Review Questions are tagged U/A/An/E on new cases, Further Reading has 5 links (all 200), and Looking Ahead is present. Only `text` fences, 9 worked examples, two flagships with step labels at sentence boundaries, and no required step inside an admonition.
* **Fading (check 7).** TIY 10.3 is problem-first. There is no completion prompt.
* **Rigor band (check 8).** Cleared. The comparison comes from the same test with stated criteria and counts, never a total, with runs and readings kept apart. A bachelor's IT student leaves with a card template, a matrix template, and re-test triggers they can use on a home lab or work project next week.
* **Shared names, cohesion, glossary (checks 9 and 12).** The fair test definition is verbatim. The six criteria appear in order. Copperwind facts hold (\$30 per user, 5 Deskside technicians, so \$150; support hours 7-6; the standing promise; December 7, 2026 is a Monday). Cover stories are all from the Part IV list. The 7 glossary additions are vendor-free, sit inside chapter 10's ownership list, and do not restate existing headwords. Toolkit is used once, unbolded.
* **G2.** No week, due date, or term is named. There are no benchmark or leaderboard claims, and line 118 and Quick Check 10.2 item 1 use a public test only as the counterexample.

## The Flesch question, for Mr. Vega

My recommendation: accept 72.5. It sits 2.5 points above the band, in the easy direction, for a no-prerequisite course whose guide says to lean toward the top of the band. It matches the Part II precedent he already ruled on (ch 6 at 73.4). The rigor lives in the matrix, the counts, and the lab, not in sentence length, which is where CLAUDE.md puts it. Merging sentences to pull the score down would cost clarity in the passages that carry the method (the six criteria, the fair test record). If he wants it nearer 70, the honest lever is the vendor fixes above. They add syllable-heavy dated callout text, which will likely lower the score a point without touching the teaching prose (a guess, not measured).

## Verdict

Nearly ready, but not ready for the professor's review until the callouts are fixed. The teaching (fair test, matrix, survey, artifacts, packet) is sound and the captures are clean. The vendor facts are where the chapter breaks its own lesson. The three most important fixes:

1. Replace the Microsoft training line with the current-app page, which now says the Copilot app does not train foundation models on prompts, responses, or files, and restore the Microsoft 365 consumer exclusion (B1).
2. Add Gemini's on-by-default Keep Activity for users 18 or over, and the now-readable Perplexity and Gemini Notebook plan and data facts, renaming NotebookLM in the roster callout (M1, M2, M4).
3. Apply one gloss-scoring ruling to both Task 3 rows and rewrite the Fix It's "tie" to match the recount (M3, with m8).

Counts: BLOCKER 1, MAJOR 4, MINOR 10, NIT 5.
