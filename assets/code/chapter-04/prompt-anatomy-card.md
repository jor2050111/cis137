# Prompt Anatomy Card

Use this card every time you build a prompt from scratch. Write one
line for each part in the "Your prompt" column, then check the line
against its one-line test. A prompt does not need all five parts every
time, but you should know which ones you left out, and why. Save a
copy for each prompt you build, and keep the blank card for next time.

| Part | What it tells the model | One-line test | Your prompt | Passes the test? |
| --- | --- | --- | --- | --- |
| Role | Whose knowledge, habits, and voice to borrow | Could you name the job title the model is playing? |  |  |
| Task | The one action and the one thing it produces | Does the prompt hold one verb and one deliverable? |  |  |
| Context | The facts, audience, and situation it cannot guess | Could a stranger do the job with only these facts? |  |  |
| Format | The shape of the output: length, layout, structure | Could you sketch the output's shape before you send? |  |  |
| Constraints | The limits: what must not happen and what must survive | Does the prompt say what the model must not do? |  |  |

## Format or Constraint?

* If breaking the rule would make the output the wrong size or
  layout, it belongs in Format.
* If breaking the rule would make the output wrong or unsafe, it is a
  Constraint.

## Before you send

* Every private detail is replaced by a slot, such as `[client name]`.
* The assembled prompt reads as one request, in the order Role, Task,
  Context, Format, Constraints.
* You know which parts you left out, and why.

## The prompt you assembled

Paste the full prompt here, with each part labeled in brackets:

