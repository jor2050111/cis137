# Chapter 11 Data Pack: Skills Lab 11A Files

Starter files for Skills Lab 11A: Four Scenarios for Mei Lin, and the
sheets the chapter's Try It Yourself exercises use. Students open these
in any text editor and never retype their contents.

## Contents

| File | Type | Used in |
| ---- | ---- | ------- |
| `skills-lab-11a-worksheet.md` | Markdown worksheet (the submission file) | All lab parts |
| `requirements-sheet-template.md` | Markdown template for the Requirements Sheet | Try It Yourself 11.1 and 11.4, lab Part 1 |
| `work-order-template.md` | Markdown template for the Work Order | Try It Yourself 11.2 and 11.3, lab Parts 2 and 3 |
| `selection-decision-template.md` | Markdown template for the Selection Decision | Try It Yourself 11.4 and 11.5, lab Part 3 |
| `monday-standup-notes.txt` | Plain text, the Deskside Monday stand-up notes | Try It Yourself 11.3 |
| `deskside-inbox-day.txt` | Plain text, 12 ticket subjects and first lines from one morning | Lab Parts 1 and 2 |
| `deskside-tickets.csv` | Comma-separated table, a synthetic sample of 80 of the four weeks' tickets, 6 columns | Lab Parts 1 and 2 |
| `priya-outreach-brief-3.txt` | Plain text, Priya Sharma's flyer request | Lab Parts 1 and 2 |
| `disputed-invoice-case.txt` | Plain text, the fourth scenario: a client's disputed invoice with Mei Lin's note | Lab Parts 1 and 3 |
| `output-checklist.md` | Markdown checklist (copied from the Chapter 5 pack) | Lab Part 2 |
| `use-evaluation-sheet.md` | Markdown sheet (copied from the Chapter 9 pack) | Lab Part 3 |
| `memo-template.md` | Markdown template (copied from the Chapter 9 pack) | Lab Part 3 |

## File details

**skills-lab-11a-worksheet.md** holds a heading and answer slots for
every task in Parts 1-3, starting with the privacy plan students write
before their first prompt, and both Questions & Analysis items.
Students type answers under each task, rename the file
`skills-lab-11a-lastname.md`, and submit that one file.

**requirements-sheet-template.md**, **work-order-template.md**, and
**selection-decision-template.md** are blank templates with their
fields in a fixed order and a one-line note under each field. Each one
works for a Copperwind job and for a student's own IT project. They go
in the student's Toolkit.

**monday-standup-notes.txt** is the note-taker's record of one Deskside
stand-up. Technicians are named by letter only.

**deskside-inbox-day.txt** lists 12 tickets with client names,
requester names, and signatures removed, plus Deskside's categories,
its urgency rule, and its VPN routing rule. Read every line before
pasting any of it into a tool.

**deskside-tickets.csv** has one row per ticket and these columns:

| Column | Type | Meaning |
| ------ | ---- | ------- |
| `ticket_id` | text | DS-001 to DS-080 |
| `week` | whole number, 1-4 | The week the ticket was closed |
| `category` | text | One of Deskside's six ticket categories |
| `client_type` | text | The kind of client office, never its name |
| `first_reply_minutes` | whole number | Minutes from the ticket's arrival to Deskside's first reply |
| `handle_minutes` | whole number | Technician minutes spent on the ticket in all |

The table is a synthetic sample of 80 of the four weeks' tickets, not
all of them (Deskside closes about 160 a week). The sample
over-represents slow first replies, so the owner's question has
something to find. It is built by
`assets/code/_generators/gen_deskside_tickets.py` with seed 137, and
rebuilds byte for byte. It holds no client names, requester names, or
account details.

**priya-outreach-brief-3.txt** is Priya's request for one flyer: the
session topic, the audience, two facts she insists on, what the
picture should do, and the disclosure line.

**disputed-invoice-case.txt** holds a client's email disputing an
invoice, what Copperwind's records show, and what a technician wants to
send. It contains fictional payment details on purpose.

**output-checklist.md**, **use-evaluation-sheet.md**, and
**memo-template.md** are copied unchanged from the Chapter 5 and Chapter
9 packs, so this lab needs no earlier file.

The pack ships no AI response. Students generate every response the lab
asks for live in a tool from the course roster.

## Source and license

Written for CIS137 by the course author. Copperwind IT Services is a
fictional company created for this textbook. All names, clients, and
records are synthetic. Any resemblance to a real company or person is
coincidental.

Copyright 2026 Jorge Vega, Phoenix College. Licensed under CC BY-NC-SA
4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/).
