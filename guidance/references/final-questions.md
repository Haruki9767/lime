# Final Questions Protocol

Use this protocol across Lime Skills whenever user input may be needed. The goal is to finish useful, authorized work without repeatedly interrupting the user.

## Core rule

1. **Inspect first.** Read the request, conversation, repository, and applicable project instructions. Reuse answers already provided; never ask the user to repeat them.
2. **Scope-filter.** A question is eligible only when its topic is directly touched by the requested work or is required to verify that work. If the task does not change or test that area, do not ask about it.
3. **Proceed safely.** Make reasonable, reversible assumptions from the existing project and user brief. Record material assumptions. Do not turn preferences into blockers when the existing implementation can be preserved.
4. **Queue, don't interrupt.** Keep unresolved questions in a short working list while working. Do not ask one question at a time. Finish all independent, authorized, safe work and run the relevant checks first.
5. **Ask once at the end.** After verification, present any remaining applicable questions together under **Questions for you**. Ask only questions whose answers change a next step, acceptance decision, or material outcome. If none remain, say no reply is needed.
6. **Protect blocked work.** Do not make a material, unsafe, irreversible, or unauthorized choice just to avoid asking. Pause only the affected slice, continue independent work, and include the blocked decision in the final question batch. Ask earlier only when no useful safe work can proceed without the answer or proceeding would cross a security, privacy, financial, legal, deployment, or destructive-change boundary; even then, ask one consolidated batch and never repeat answered questions.
7. **Close the loop.** If the user answers a queued question, apply the answer only to its relevant scope, then rerun checks affected by that choice. Report any failed checks with evidence; fix authorized failures and rerun them. Never imply a question itself is a failed test.

## Applicability filter

Use this table as a **question bank**, not as a form to send. Ask only what is missing, outcome-changing, and relevant to the specific slice being worked on.

| Work actually in scope | Ask only if needed | Do not ask when |
|---|---|---|
| Existing-site audit or code review | Target/scope only if unclear; live origin or route policy only when required for the requested live/page-specific check | The user supplied the repo and a structural review can proceed without live credentials, design preferences, or backend plans |
| New UI, redesign, or visual change | Audience/job, design direction, fonts/brand rules, references, accessibility constraints, and approval of a materially different direction | The task is design-preserving, backend-only, docs-only, or the user already gave the applicable choices |
| Existing UI bug fix | The smallest missing detail that changes expected behavior | The fix can be inferred from current behavior/tests and visual identity can be preserved |
| Framework, package, or dependency change | Compatibility constraints or a genuine unresolved conflict that changes the stack/lockfile | The existing stack is healthy and no framework/dependency choice is needed |
| Backend, API, data, auth, or deployment change | Only the missing contract/ownership, migration, provider, authorization, environment-variable names, rollout, or approval detail needed for that change | Those boundaries are not touched; never request secret values in chat |
| SEO/content/schema work | Audience, target markets, canonical origin, factual business data, or page intent only when needed for the specific copy, targeting, or schema being written | Work is a structural/technical audit, no new claims are authored, or the relevant facts already exist in authoritative sources |
| CI, release, commit, or push | Target branch/remote or release version only when not specified and the requested action requires it | The user explicitly requested the target action and the repository state makes its target unambiguous |
| Legal/privacy-sensitive choice or public/destructive action | The exact decision/authorization required for the affected action | No such change is being proposed or performed |

## Question handling

- Keep questions brief, grouped by topic, and numbered. State why each is needed and which step is blocked.
- Prefer a proposed safe default or a small set of choices where that genuinely resolves the decision. Do not ask broad questionnaires, hypothetical preferences, or generic “anything else?” questions.
- Do not bundle unrelated preferences merely because they appear in this table. Do not ask questions about untouched design, framework, backend, SEO, analytics, legal policy, or deployment areas.
- When approval is needed for one change, continue unrelated approved work and report the blocked portion clearly. Do not ask again for approval that the user already gave for the exact scope.
- In the final report, distinguish verified results, failed checks, not-tested items, assumptions, blocked work, and questions. State what you tested and the outcome before asking.

## Final response shape

Use only the sections that apply:

- **Done:** concise summary of completed work.
- **Verification:** commands/checks and pass/fail/not-tested results; fix and rerun in-scope failures first.
- **Limitations or blocked:** only actual unresolved items.
- **Questions for you:** one consolidated, scope-filtered list at the end. Omit the section when there are no applicable questions.
