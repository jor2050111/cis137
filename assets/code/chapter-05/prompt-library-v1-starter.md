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
* Notes (what to watch, what it gets wrong): The October run added a subject line the Format part did not ask for. Delete it if your ticket system adds its own. Check the phone number in every run.

Sample output from the last run (captured from a chat assistant, October 2026). Your output will differ:

```text
Subject: Re: Locked out of email

Hi Marcus,

Sorry about the lockout. We can get you back in quickly.

For your security, we reset passwords only after we confirm who is asking. Please call our Deskside line at 602-555-0149. A technician will verify your identity and walk you through the reset on the call.

We never send passwords by email, and we will never ask you to send us yours.

Talk soon,

The Deskside team
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
* Notes (what to watch, what it gets wrong): The October run added bold step titles and asked for a screenshot. Its check for an expired password told the client to sign in to another work site, which may not fit every client. Read the checks against what the client's setup allows.

Sample output from the last run (captured from a chat assistant, October 2026). Your output will differ:

```text
Hi Keisha,

Thanks for reaching out. Let's get you connected so you can finish your day.

Please try these in order:

1. **Check your password.** Sign in to your email or another work site. If it asks you to reset your password, an expired password is the most likely cause. Update it, then try the VPN again.
2. **Switch networks.** Some home Wi-Fi networks block VPN traffic. Connect your phone's hotspot to your computer and try again.
3. **Update the VPN app.** Open the app's menu or settings, look for "Check for updates," install any update, and restart the app.

If none of those work, what exact words does the error message show? A screenshot is even better.

Thanks,
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
* Notes (what to watch, what it gets wrong): The October run added items the request did not ask for, such as permissions for the role, a standard image, and an asset tag, and it put an OS update item under Hardware. Strike any item the client did not ask for before the technician starts.

Sample output from the last run (captured from a chat assistant, October 2026). Your output will differ:

```text
**New-Hire Setup Checklist: Jordan Reyes (Part-Time Receptionist)**
Start date: Monday, November 2

**Accounts**
1. Create Jordan's email account.
2. Grant Jordan access to the shared front-desk mailbox.
3. Create Jordan's scheduling software account.
4. Set the account permissions for a part-time receptionist.

**Software**
5. Install the scheduling software on the laptop.
6. Add Jordan's email account to the mail client on the laptop.
7. Add the shared front-desk mailbox to the mail client.
8. Sign in to the scheduling software and confirm it loads.

**Hardware**
9. Prepare the laptop with the current OS updates and the client's standard image.
10. Create Jordan's user profile on the laptop.
11. Test sending and receiving from both Jordan's mailbox and the shared front-desk mailbox.
12. Label the laptop and record its asset tag and assigned user.
13. Confirm that no new phone is needed, since Jordan will use the existing desk phone.
```
