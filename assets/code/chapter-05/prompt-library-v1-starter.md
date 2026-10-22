# Prompt Library v1 Starter: Copperwind Deskside

Three finished prompt cards for Copperwind's Deskside team, in the
standard prompt card format. Use these if you did not build your own
library in Chapter 4. If you did, you may use yours instead.

Each card's Prompt has a slot for the input. Paste the ticket or
request into the slot before you send it. Every sample output below is
a real capture: the card's prompt with its example input in the slot,
sent once in a fresh conversation on the textbook author's test setup
(not a roster product). The tool and date are in the author's capture
log, which is not in the data pack.

This is library v1, so the Strategies used field is still empty.
Chapter 5 fills it.

## Card 1: Password reset reply

* Name: Password reset reply
* Job (what this prompt is for): Answer a client who asks Deskside to reset a password, without breaking Copperwind's identity check.
* Prompt (full text, with [Role] [Task] [Context] [Format] [Constraints] labeled):

    ```text
    [Role] You are a Deskside support technician at Copperwind IT Services, a managed IT services company in Phoenix.
    [Task] Write a reply to the client ticket below about a password reset.
    [Context] Copperwind resets a client's password only after the person calls the Deskside line at 602-555-0149 and confirms who they are. Ticket: [paste the ticket here]
    [Format] A short email reply, under 100 words, with a greeting and a sign-off from the Deskside team.
    [Constraints] Never ask for a password or include one in the reply.
    ```

* Example input: I'm locked out of my email after too many tries. Can you reset my password and send me the new one? - Marcus, front desk at a client law office
* Good output looks like (two or three criteria):

    * Routes the reset to a phone call on the Deskside line, where the person confirms who they are
    * Never asks for a password and never includes one
    * Under 100 words, with a greeting and a sign-off from the Deskside team

* Strategies used (Chapter 5):
* Last run (tool, date): the textbook author's test setup (not a roster product), October 21, 2026. Tool and date in the author's capture log, which is not in the data pack
* Notes (what to watch, what it gets wrong): The October run added a subject line the Format part did not ask for, and it promised to get the client back in "right away." Delete the subject line if your ticket system adds its own, and strike any promise of a time. Check the phone number in every run.

Sample output from the last run (captured from a chat assistant, October 2026). Your output will differ:

```text
Subject: Re: Locked out of email

Hi Marcus,

Sorry about the lockout. For security, we can only reset a password after we verify your identity by phone. Please call our Deskside line at 602-555-0149, and we'll confirm who you are and get you back into your email right away.

For your protection, we'll never ask you to send a password by email, and we won't email one to you.

Thanks,
The Deskside Team
Copperwind IT Services
```

## Card 2: VPN connection failure, first reply

* Name: VPN connection failure, first reply
* Job (what this prompt is for): Send a client a first reply when the VPN will not connect from home, with checks they can try before a technician steps in.
* Prompt (full text, with [Role] [Task] [Context] [Format] [Constraints] labeled):

    ```text
    [Role] You are a Deskside support technician at Copperwind IT Services, a managed IT services company in Phoenix.
    [Task] Write a first reply to the client ticket below about a VPN connection that will not connect.
    [Context] Most VPN failures at our clients come from an expired password, a home Wi-Fi network that blocks the VPN, or a VPN app that needs an update. Ticket: [paste the ticket here]
    [Format] A friendly reply under 150 words with up to three numbered checks the client can try, then one line asking what the error message says.
    [Constraints] Do not tell the client to change any settings on their home router.
    ```

* Example input: The VPN won't connect from home since this morning. It just spins and then says connection failed. I'm working from home today. - Keisha, bookkeeper at a client firm
* Good output looks like (two or three criteria):

    * Up to three numbered checks that match the three common causes in the Context part
    * Ends with one line asking what the error message says
    * Tells the client nothing about changing home router settings

* Strategies used (Chapter 5):
* Last run (tool, date): the textbook author's test setup (not a roster product), October 21, 2026. Tool and date in the author's capture log, which is not in the data pack
* Notes (what to watch, what it gets wrong): The October run added bold step titles and a line saying "we'll dig in further." Its update check also told the client to restart the computer, which the Context part never mentions. Read the checks against what the client's setup allows.

Sample output from the last run (captured from a chat assistant, October 2026). Your output will differ:

```text
Hi Keisha,

Thanks for reaching out, and sorry for the trouble this morning. Let's get you connected. Please try these in order:

1. **Check your password.** Sign in to your work email in a web browser. If it rejects your password or asks you to reset it, it has likely expired. Update it, then retry the VPN.
2. **Try a different connection.** If you have a phone, turn on its hotspot, connect your computer to it, and try the VPN again. This tells us whether your home Wi-Fi is blocking it.
3. **Update the VPN app.** Open the app and check for updates (or restart your computer so it can update). Then try connecting again.

If none of these work, don't worry, we'll dig in further.

What exact error message do you see after it says connection failed?

Best,
Deskside Support, Copperwind IT Services
```

## Card 3: New-hire device setup checklist

* Name: New-hire device setup checklist
* Job (what this prompt is for): Turn a client's new-hire request into a setup checklist for the technician who prepares the laptop.
* Prompt (full text, with [Role] [Task] [Context] [Format] [Constraints] labeled):

    ```text
    [Role] You are a Deskside support technician at Copperwind IT Services, a managed IT services company in Phoenix.
    [Task] Turn the new-hire request below into a setup checklist for the technician who will prepare the laptop.
    [Context] Request: [paste the request here]
    [Format] A numbered checklist, one action per line, grouped under Accounts, Software, and Hardware.
    [Constraints] Include only items the request asks for or clearly implies.
    ```

* Example input: New hire starts Monday, November 2: Jordan Reyes, part-time receptionist. Needs a laptop, an email account, access to the shared front-desk mailbox, and the scheduling software. Jordan will use the existing desk phone. - Office manager at a client property management office
* Good output looks like (two or three criteria):

    * Every item traces to the request, or is clearly implied by it
    * One action per line, grouped under Accounts, Software, and Hardware
    * Keeps the start date and the person's role from the request

* Strategies used (Chapter 5):
* Last run (tool, date): the textbook author's test setup (not a roster product), October 21, 2026. Tool and date in the author's capture log, which is not in the data pack
* Notes (what to watch, what it gets wrong): The October run added items the request did not ask for, such as imaging the laptop, joining it to the client's network with standard security settings, and delivering it, and it put software tests under Hardware. Strike any item the client did not ask for before the technician starts.

Sample output from the last run (captured from a chat assistant, October 2026). Your output will differ:

```text
**New-Hire Setup Checklist: Jordan Reyes (Part-Time Receptionist)**
Start date: Monday, November 2

**Accounts**
1. Create Jordan Reyes's user account and email account.
2. Grant Jordan access to the shared front-desk mailbox.
3. Create Jordan's login for the scheduling software.

**Software**
4. Install the scheduling software on the laptop.
5. Configure the email account and the shared front-desk mailbox in the mail client on the laptop.
6. Sign in to the scheduling software and confirm it works.

**Hardware**
7. Provision and image the laptop for Jordan.
8. Join the laptop to the client's network and apply standard security settings.
9. Test the laptop, including email, the shared mailbox, and the scheduling software, before delivery.
10. Deliver the laptop to the client's office by Monday, November 2.

*Not included: the desk phone. Jordan will use the existing one, so no setup is needed.*
```
