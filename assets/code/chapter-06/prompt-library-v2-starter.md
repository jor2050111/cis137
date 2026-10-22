# Copperwind Shared Prompt Library, v2 starter

Three finished cards for Copperwind's Deskside team, written by the
course author in the prompt card format. Each card already has its
Strategies used line, which is what makes this library v2. Use your own
library if you built one in Chapter 5, or start from these cards.

How to read a card:

* The bracket labels in the Prompt field mark the five parts of a
  prompt. The last runs were sent without the labels.
* Card 2 carries two `[Context]` labels. The first sets the reader, and
  the second holds the grounded checks. Its Format part begins with the
  word "Format:", which the last run sent as written.
* `{ticket text}` is a slot. Replace it with the ticket, including its
  quotation marks, after you remove any names, usernames, or account
  details.
* Last run names the date of a real run with the card's example input.
  The output of that run sits under each card. The tool and the full
  record are in the textbook author's capture log, which is not in the
  data pack.
* The process facts inside each prompt (the call-back step, the three
  VPN checks, the approval rule) are fictional Copperwind procedures
  written for this course.

---

## Card 1

* Name: Password reset reply
* Job (what this prompt is for): Reply to a client employee who is locked out or asks for a password reset, telling them what happens next without asking for their password.
* Prompt (full text, with [Role] [Task] [Context] [Format] [Constraints] labeled):

    ```text
    [Role] You are a Deskside support technician at a managed IT services company, writing to an employee at one of our client companies. [Task] Write a reply to the ticket below that tells the person what happens next with their password reset. [Context] Our process: we verify identity by calling the person back at the phone number we have on file, and then we send a temporary password that must be changed at the first sign-in. Ticket: {ticket text} [Format] Keep the reply under 120 words, in plain text, with a greeting, two or three short numbered steps, and a sign-off from "Deskside Support." [Constraints] Never ask for the current password or any sign-in code. Do not promise a time. Use only the process above.
    ```

* Example input: "Hi, I got locked out after too many tries this morning and I have a client call at 2. Can you reset it?"
* Good output looks like (two or three criteria):
    * the call-back step comes first
    * it asks for no password and no code
    * it promises no time
* Strategies used (Chapter 5):
    * specificity and context
    * output structure
    * negative constraints and guardrails
* Last run (tool, date): a chat assistant from the course roster, October 21, 2026 (Prompt 11 in the textbook author's capture log, not in the data pack)
* Notes (what to watch, what it gets wrong): The last run added a line asking the person to keep their phone nearby. That line is harmless, but check every added line against the process. Watch for a promised time, such as "within the hour," when a ticket mentions a deadline.

Sample output from the last run (captured from a chat assistant, October 2026). Your output will differ:

```text
Hi there,

Thanks for reaching out. We can get you back in. Here is what happens next:

1. We call you back at the phone number we have on file to verify your identity. Please keep that phone nearby.
2. Once you're verified, we send you a temporary password.
3. Sign in with the temporary password. You will be asked to choose a new one right away.

We will never ask for your current password or any sign-in code, so please don't share those with anyone.

Deskside Support
```

---

## Card 2

* Name: VPN connection failure reply
* Job (what this prompt is for): Walk a non-technical client employee through Deskside's first three checks when the VPN will not connect.
* Prompt (full text, with [Role] [Task] [Context] [Format] [Constraints] labeled):

    ```text
    [Role] You are a Deskside support technician at a managed IT services company. [Context] The reader is an office worker at a client company, not a technical person. [Task] Write a reply to the ticket below that walks them through our first checks for a VPN connection failure. [Context] Use only these checks, in this order: 1. Open any website to confirm the internet works without the VPN. 2. Quit the VPN app completely, open it again, and sign in. 3. If it still fails, reply to this email with the exact words of the error message. Ticket: {ticket text} [Format] Format: under 100 words, plain text, a one-line greeting, the three checks as numbered steps, and a sign-off from "Deskside Support." [Constraints] Do not add any other troubleshooting steps, and do not promise when it will be fixed.
    ```

* Example input: "The VPN won't connect from home. It just spins and then says something failed. I need the shared drive today."
* Good output looks like (two or three criteria):
    * the three checks appear in order and no others
    * it is under 100 words
    * it promises no fix time
* Strategies used (Chapter 5):
    * grounding (supply the source, answer only from it)
    * persona and audience framing
    * output structure
* Last run (tool, date): a chat assistant from the course roster, October 21, 2026 (Prompt 12 in the textbook author's capture log, not in the data pack)
* Notes (what to watch, what it gets wrong): The last run added an example website to check 1. That is harmless, but it is an addition, so read check 1 before you send.

Sample output from the last run (captured from a chat assistant, October 2026). Your output will differ:

```text
Hi,

Let's start with three quick checks.

1. Open any website, such as a news site. This confirms your home internet works without the VPN.
2. Quit the VPN app completely, open it again, and sign in.
3. If it still fails, reply to this email with the exact words of the error message.

Those exact words help us see what went wrong.

Deskside Support
```

---

## Card 3

* Name: Shared mailbox access reply
* Job (what this prompt is for): Reply to a client employee who asks for access to a shared mailbox, asking for whatever the ticket is missing.
* Prompt (full text, with [Role] [Task] [Context] [Format] [Constraints] labeled):

    ```text
    [Role] You are a Deskside support technician at a managed IT services company. [Context] A client employee has asked for access to a shared mailbox. Our rule: we add someone to a shared mailbox only after their manager approves it in writing. [Task] Before you draft anything, check the ticket for two facts: the name of the mailbox, and whether a manager has approved. If either fact is missing, write a short reply that asks only for what is missing. If both are there, write a reply under 80 words that says we will add them once we confirm the approval with their manager. [Format] Here is an example of a good reply that asks for what is missing: "Thanks for your request. Which shared mailbox do you need, for example billing@ or frontdesk@? Also, please ask your manager to reply to this email to approve the access." Ticket: {ticket text} Sign off as "Deskside Support." [Constraints] Do not promise a time.
    ```

* Example input: "Can I get into the shared inbox? I'm covering for a coworker next week."
* Good output looks like (two or three criteria):
    * asks only for the missing facts
    * promises no time
    * signed "Deskside Support."
* Strategies used (Chapter 5):
    * clarifying questions first
    * examples (few-shot)
    * negative constraints and guardrails
* Last run (tool, date): a chat assistant from the course roster, October 21, 2026 (Prompt 13 in the textbook author's capture log, not in the data pack)
* Notes (what to watch, what it gets wrong): The last run copied the example reply word for word. That fits a ticket that is missing both facts. When the ticket names a mailbox, check that the reply does not still ask which mailbox.

Sample output from the last run (captured from a chat assistant, October 2026). Your output will differ:

```text
Thanks for your request. Which shared mailbox do you need, for example billing@ or frontdesk@? Also, please ask your manager to reply to this email to approve the access.

Deskside Support
```
