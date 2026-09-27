# Design Direction Worksheet

Use this worksheet after the brief is understood and before coding a custom direction. For a first-time from-scratch project, it replaces the existing-interface scan; for an existing project, complete the anti-slop review first.

## Ask before changing direction

- What is the product, audience, primary action, and requested mode?
- Which framework/version should be used—existing stack, React, Vue, or permission to recommend? What rendering/hosting constraints apply?
- Which PRD, brand rules, tokens, fonts, assets, or Figma files are authoritative?
- What must remain unchanged: copy, routes, components, backend, dependencies, favicon, accessibility behavior, or APIs?
- Are gradients, glassmorphism, skeuomorphism, or other styles preferred, allowed, or forbidden? Where and why?
- Name two or three interfaces the user likes and what they like about them.
- What should the result feel like, and what should it explicitly avoid?
- What are the accessibility, responsive, browser, performance, and reduced-motion expectations?
- Is the scope a surgical pass, one page, a component, or a broad redesign?

## Direction proposal

Present at most two options unless the user asks for exploration. For each option state:

- **Name and thesis:** one sentence tied to the product, not a generic aesthetic label.
- **Framework:** choice, rendering mode, and why it fits the project.
- **Palette:** 4–6 named colors with contrast intent and gradient/material policy.
- **Typography:** roles, type scale, line length, licensing/fallbacks, and why it fits the subject.
- **Layout:** alignment, dominant anchor, content rhythm, and responsive behavior.
- **Components:** what is intentionally repeated and what is reserved for hierarchy.
- **States:** loading, empty, validation, permission, error, retry, and custom 404 behavior.
- **Motion:** one or two purposeful moments, smooth-scroll policy, focus behavior, and reduced-motion behavior.
- **Risks:** accessibility, performance, brand mismatch, or implementation cost.

Ask the user to approve one option or provide corrections before coding. If their supplied design conflicts with an anti-slop heuristic, follow the user's design and document the exception unless it creates a concrete accessibility or logic defect.

## Non-cloning rule

References are for learning principles such as hierarchy, rhythm, contrast, and material treatment. Do not reproduce a reference image, layout, copy, logo, or distinctive composition pixel-for-pixel without permission and appropriate rights.
