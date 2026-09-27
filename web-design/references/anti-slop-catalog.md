# Anti-Slop Signal Catalog

Use this catalog as a hypothesis generator. Confirm signals against the brief, the rendered page, and the code before reporting them.

## P0: immediate usability or severe sameness

| Signal | Confirm with | Safer recommendation |
|---|---|---|
| Gradient text or purple-blue wash dominates the first viewport | Render plus CSS/source; check brand brief | Replace only when unapproved or harmful; use a reasoned solid palette, image, texture, or restrained approved gradient |
| Centered hero + generic CTA pair + three identical cards is the whole product story | IA and content requirements | Choose a structure that expresses the product's real job; preserve IA and copy |
| Text is unreadable over glass, image, or gradient | Contrast/rendered states | Increase contrast, add a solid scrim/panel, or change placement; do not rely on color alone |
| Core interaction, form, route, or responsive layout fails | Test, typecheck, browser, link and route checks | Fix behavior before aesthetic polish |

## P1: repeated generic defaults

- One radius, shadow, border, blur, or card shell applied to every hierarchy level.
- Default font stack or a familiar display font used without a product-specific rationale.
- Untouched component-library colors and spacing where the brief calls for identity.
- Repeated “Elevate,” “seamless,” “powerful,” “Get Started,” or vague marketing filler; report copy only when it harms understanding or is clearly placeholder text.
- Identical fade-up animation on every section, no reduced-motion branch, or motion that hides state changes.
- Every control using the same icon-in-rounded-square treatment, emoji, or mixed icon libraries.
- Uniform centered alignment, repeated three-column grids, or equal cards where content hierarchy is unequal.

## P2: polish and maintainability leads

- Tiny spacing inconsistencies, orphaned styles/assets, unused-looking exports, inconsistent focus rings, unexplained breakpoint exceptions, stale comments, or decorative labels.
- These remain leads until compiler, linter, route graph, tests, or runtime evidence confirms impact.

## Gradient review questions

1. Is the gradient required by the user's brand, PRD, or supplied design?
2. Does it carry meaning, establish hierarchy, or improve legibility?
3. Does it survive contrast, forced colors, reduced motion, and low-quality displays?
4. Is it localized to one intentional role rather than used as a universal decoration?
5. Does removing it materially reduce the design's intended identity?

## Fix principles

- Keep the user's copy, information architecture, and working behavior unless approved otherwise.
- Replace defaults with a specific rationale, not novelty for its own sake.
- Make one memorable move; keep supporting UI quiet and coherent.
- Prefer tokens over scattered one-off values.
- Verify screenshots at 320px, 768px, 1024px, and desktop when possible.
- Report `path:line` evidence and confidence for every actionable finding.
