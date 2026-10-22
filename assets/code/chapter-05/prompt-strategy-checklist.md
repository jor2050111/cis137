# Prompt Strategy Checklist

Use this checklist to diagnose a prompt before you send it, or after a
response fails. Run down the nine strategies in order. Mark each one
Used, Missing, or Not needed for this job. Add only the strategies the
job needs, and add them one at a time so you can tell which one helped.

Each strategy strengthens one of the five parts of a prompt: Role,
Task, Context, Format, and Constraints.

| # | Strategy | The test you run on your prompt | The part it strengthens | Used, Missing, or Not needed | Your example |
| --- | --- | --- | --- | --- | --- |
| 1 | Specificity and context | Does it supply every fact, name, and number the output needs? | Context |  |  |
| 2 | Examples (few-shot) | If the output must match a house style, does it show one to three samples? | Format |  |  |
| 3 | Output structure | Does it name the shape the next step needs: table, list, template, or length? | Format |  |  |
| 4 | Step-by-step reasoning request | If the job applies rules, does it ask for each check on its own line before the answer? | Task |  |  |
| 5 | Decomposition | If the job has stages, does each stage get its own prompt and its own check? | Task |  |  |
| 6 | Persona and audience framing | Does it say whose voice to use and who will read the result? | Role, Context |  |  |
| 7 | Grounding (supply the source, answer only from it) | Does it hand over the source, limit the answer to it, and say what to do when the source is silent? | Context, Constraints |  |  |
| 8 | Clarifying questions first | If you are unsure what you need, does it ask the model to ask before it writes? | Task |  |  |
| 9 | Negative constraints and guardrails | Does it forbid the additions you cannot accept, such as prices, promises, or advice? | Constraints |  |  |

## How to use it

* Fill the "Your example" column as you practice. One line per
  strategy is enough: the prompt you changed, and what changed in the
  response.
* A strategy marked Not needed is a decision, not a gap. A two-line
  reminder text needs no step-by-step reasoning request.
* Strategies often travel in pairs. Strategy 1 supplies the facts, and
  strategy 9 forbids everything else.
* Record the strategies a prompt uses in the Strategies used field of
  its prompt card.
