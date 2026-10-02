# Design Direction Worksheet

Use this worksheet after inspecting the brief and existing product. It is a **question bank**, not a mandatory intake form. Follow [`../../guidance/references/final-questions.md`](../../guidance/references/final-questions.md): select only unresolved questions that affect visual work actually in scope, queue them, complete safe independent work, and present them together at the end.

For a first-time from-scratch project, skip the existing-interface scan; for an existing project, inspect design quality and AI-slop signals first. If visuals are not part of the task, do not use this worksheet or ask its design questions.

## Candidate questions for visual work only

Ask only what repository evidence and the user’s brief do not already answer:

- What is the product/audience and primary user job if this changes content hierarchy or interaction?
- Which brand rules, PRD, design tokens, fonts, licensed assets, or Figma files are authoritative if a visual change needs them?
- What must remain unchanged: copy, routes, components, backend, dependencies, accessibility behavior, or APIs?
- Is a visual direction, layout, density, color, imagery, or motion preference missing and outcome-changing?
- Which responsive, browser, performance, accessibility, or reduced-motion requirement affects this implementation?
- Does the proposed direction materially change the existing experience enough to require approval?

Do not ask all prompts by default. Never ask about framework/version when the task does not change or create the stack; infer from the healthy existing project. If a preference was already supplied, do not ask again.

## Direction proposal

When a custom direction is in scope and can be proposed safely, present at most two options unless the user asks for exploration. For each option state:

- **Name and thesis:** one sentence tied to the product, not a generic aesthetic label.
- **Framework:** choice and rationale only if a new/changed framework is actually in scope.
- **Palette:** named colors and contrast intent when color is changing.
- **Typography:** roles, type scale, licensing/fallbacks when type is changing.
- **Layout:** alignment, dominant anchor, content rhythm, and responsive behavior.
- **Components:** what is intentionally repeated and what is reserved for hierarchy.
- **States:** loading, empty, validation, permission, error, retry, and custom 404 behavior where relevant.
- **Motion:** purposeful moments, focus behavior, and reduced-motion behavior where motion is in scope.
- **Risks:** relevant accessibility, performance, brand mismatch, or implementation cost.

If material approval is required, leave the unapproved visual slice unchanged, complete independent authorized work, run applicable checks, and include the approval request in the one final question batch. If the user's supplied design conflicts with an anti-slop heuristic, follow the user's design and document the exception unless it creates a concrete accessibility or logic defect.

## Non-cloning rule

References are for learning principles such as hierarchy, rhythm, contrast, and material treatment. Do not reproduce a reference image, layout, copy, logo, or distinctive composition pixel-for-pixel without permission and appropriate rights.
