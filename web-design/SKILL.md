---
name: web-design
description: Design and build distinctive, usable, accessible web interfaces while detecting AI-generated visual patterns, preserving user intent, handling errors, and choosing React or Vue deliberately. Use when creating, redesigning, polishing, or reviewing websites and frontend applications.
---

# Web Design

Create web interfaces with a clear, product-specific visual point of view—not an interchangeable AI template. Balance distinctive taste with usability, accessibility, performance, maintainability, and the user’s actual brief. Inspect existing work before changing it. Use [`../guidance/references/final-questions.md`](../guidance/references/final-questions.md) to queue any missing, in-scope design decisions and present them together at the end; do not ask about design when visuals are untouched.

## Operating modes

Choose the mode before acting:

- **Create:** Build a new project or experience from an approved brief and visual direction.
- **Redesign:** Change an existing experience only after the user approves the direction, scope, and references.
- **Review/fix:** Inspect an existing website for web-design quality and AI-slop signals, then change only the approved scope.

If the user is using this skill for the first time to create a project from scratch, skip the initial existing-interface AI-slop scan because there is no existing interface to inspect. Still run the scan and quality review after the first implementation pass. For an existing project, always start by inspecting both its web-design quality and AI-slop signals.

## Scope-filtered design preferences

Ask only about a missing preference that materially affects visual work actually in scope: the product/audience and primary job, existing brand/font rules, visual direction or references, layout/content constraints, responsive/accessibility/motion needs, or permission for a material design/dependency/structure change. Do not ask users to answer every item as a prerequisite. Reuse the brief and repository; preserve established visual identity when no redesign is requested.

Queue missing questions during discovery and present one concise, consolidated batch under **Questions for you** at the end, after safe independent work and verification. If an unapproved direction blocks design implementation, leave that visual slice unchanged while completing unrelated authorized work. Ask earlier only when no useful safe work can proceed or the change crosses a consequential boundary. Never invent brand claims, factual content, or a custom visual direction that requires approval; follow preferences already given without asking again.

## First pass: design and AI-slop scan

For an existing project, inspect the rendered interface and source before editing. Look for clusters of unexamined defaults: generic purple/blue gradients, identical rounded glass cards, centered hero plus two CTAs plus three-card grid, default fonts and palettes, repeated shadows/radii, generic copy, template dashboards, excessive symmetry, decorative blobs, icon repetition, dead code, broken routes, and motion without reduced-motion handling.

Treat a signal as a finding only when it is unsupported by the brief, repeated as a default, harms hierarchy/usability/accessibility, or conflicts with the design system. A gradient, glass surface, skeuomorphic detail, brutalist treatment, or any other style is not inherently bad. Confirm intent and evidence before calling it AI slop.

## Create a distinct visual direction

After the user approves the brief, write a short visual thesis before coding. Define a small visual grammar: type roles, spacing/grid, color roles, shape and material rules, imagery/icon behavior, elevation, motion, content tone, and signature moments. Make the direction feel specific to the product through hierarchy, content, terminology, and a few memorable choices—not novelty on every component.

Prefer a **simple yet excellent** style: strong hierarchy, readable typography, restrained color, clear actions, coherent spacing, and purposeful detail. Use glassmorphism, skeuomorphism, gradients, maximalism, brutalism, or other treatments only when the user prefers them or the product’s content/interaction benefits from them. For glass, protect contrast and provide a solid/high-contrast fallback; for skeuomorphism, ensure the metaphor improves recognition or affordance instead of becoming decoration.

Do not imitate a reference site or create a pixel clone. Use references to extract principles, then create an original system. Preserve existing brand and architecture unless the user explicitly approves change.

## React or Vue decision

Do not choose by popularity alone. Prefer the project’s healthy existing stack, component library, deployment pipeline, testing conventions, and team expertise.

- **Prefer React** when the project benefits from its library/ecosystem breadth, an existing React codebase/design system, substantial third-party React integrations, or a strategic React Native path. For a new app, choose a current recommended React framework and deliberately own routing, data fetching, rendering, and deployment decisions; do not use deprecated Create React App.
- **Prefer Vue** when the project benefits from an integrated, progressive framework, standard HTML/CSS/JavaScript templates, Single-File Components, incremental adoption, or a cohesive official ecosystem. For a full application, use Vue 3 with the current recommended tooling; for small enhancements, Vue can be incrementally added.
- **For SEO/content sites**, compare SSR/SSG and time-to-content in the actual framework architecture. For rich client applications, compare data flow, route complexity, performance budgets, and testing. For a small enhancement to existing HTML, prefer the least disruptive option.
- **When uncertain**, prototype the highest-risk route safely when possible and compare implementation complexity, accessible behavior, production-like performance, deployment, and maintainability. If the choice still changes the outcome, queue the specific question for the final batch; do not ask about stack choice when no stack change is in scope. There is no universal winner.

Record the decision and rejected alternative in the project notes.

## Build requirements

Always include:

- a custom, on-brand 404 page that clearly explains the problem and offers useful recovery such as home, search, navigation, retry, or related links;
- actual HTTP 404 semantics for unknown routes/resources at the server, SSR, edge, or hosting layer; use 410 for permanently removed resources and redirects for moved content where appropriate;
- loading, empty, validation, unauthorized/forbidden, offline/transient, and server-error states where relevant;
- resilient error handling: React error boundaries plus explicit async/event handling, or Vue error handlers/errorCaptured plus explicit async/route handling; keep fallback UI separate from safe telemetry;
- sanitized, structured error logging with correlation/release context and no secrets, tokens, cookies, raw bodies, or sensitive personal data;
- clear focus, keyboard, contrast, responsive, zoom, and screen-reader behavior;
- progressive enhancement and a safe fallback when JavaScript, advanced CSS, smooth scrolling, transparency, or motion preferences are unavailable.

Make error UI actionable and preserve unaffected content where possible. Do not render a not-found-looking page with a 200 status for direct requests or crawlers. Test deep links, refreshes, unknown routes, API errors, retries, and fallback failures.

## Motion and feeling

Prefer smooth, calm interaction and a sense of continuity, but never make motion a requirement for comprehension. Use smooth scrolling only for CSSOM/navigation-triggered scrolling, preserve normal anchor behavior, and honor `prefers-reduced-motion: reduce` with instant scrolling or a static/less-motion alternative. Avoid parallax and unnecessary scroll-linked movement; provide a site-wide motion control when the experience has substantial non-essential animation. Preserve visible focus and do not move focus confusingly after navigation.

Use motion to communicate state, hierarchy, and spatial relationships. Avoid applying the same fade/slide to every element. Test keyboard, reduced motion, touch, low-power devices, zoom, and screen readers.

## Workflow

1. **Inspect and scope.** Identify mode, target, audience, stack, existing visual rules, constraints, routes, and authorization. Determine which design questions actually affect the requested visual changes; queue only missing material choices.
2. **Discover.** For existing projects, inspect route map, entrypoints, styles/tokens, assets, scripts, tests, rendered desktop/mobile states, and current error/loading/empty behavior. Search for the current `web-design`, `web-engineer`, and `seo-production-audit` skills; read their current `SKILL.md` files instead of relying on cached copies.
3. **Scan existing work.** Skip this step only for a first-time from-scratch project. Otherwise run `scripts/scan_slop_signals.py`, investigate signals in source and rendered output, and report confidence.
4. **Research.** Check current official framework, browser, W3C, MDN, and project-specific best practices. Read `references/best-practices.md` and record source/version caveats.
5. **Plan the direction.** Form a visual thesis and plan framework, font roles, component grammar, responsive behavior, error states, motion rules, and accessibility floor from the brief and existing system. Keep an unapproved material direction out of implementation; include any needed approval in the final question batch after other safe work is verified.
6. **Implement.** Build the approved experience. Use simple, purposeful styling; keep components and states maintainable; add the custom 404 and robust error handling; do not silently add dependencies or change backend/API contracts.
7. **Verify locally.** Run the project’s pnpm lint, typecheck, tests, build, and scanner where available. Check routes, direct navigation, 404 status, error/empty/loading states, responsive layouts, keyboard/focus, contrast, reduced motion, and console errors.
8. **Quality handoff.** After the web experience is implemented, read and apply the current `seo-production-audit` skill and then the current `web-engineer` skill. Run their relevant SEO, accessibility, security, privacy/policy, dependency, and logic checks. Fix findings within scope, keep unapproved material changes blocked, and re-run affected checks.
9. **Final review.** Re-run the slop scan and project checks after fixes. Inspect the diff, verify files and routes, confirm no secrets or generated artifacts were added, report pass/fail/not-tested evidence, and put only unresolved questions about touched visual work in one final batch. Never claim final quality without evidence.

## Required handoff order

The post-build handoff is mandatory for created or materially changed websites:

1. `seo-production-audit`: check discoverability, route/indexability, metadata, crawl controls, structured data, performance/accessibility boundaries, and evidence limits.
2. `web-engineer`: check framework/package-manager consistency, security and business logic, server-side authorization, privacy/cookie/terms readiness, accessibility scope, CI, and launch risks.
3. Fix authorized findings, then re-run both relevant checks and the web-design scan.

If a skill is missing from the local skill directory, repository, or configured skills, record that it was searched for and unavailable; do not pretend it ran.

## References

Read only when needed:

- `references/best-practices.md` — researched framework, design, error, motion, accessibility, and style guidance.
- `references/anti-slop-catalog.md` — detailed visual and code signals.
- `references/design-direction-worksheet.md` — brief, taste, visual thesis, framework, and approval worksheet.
- `../guidance/references/final-questions.md` — applicability filter, question timing, and final verification protocol.
- `references/review-checklist.md` — verification, error-state, accessibility, and logic checks.
- `references/archive-assets/` — optional calibration material; never copy or execute blindly.
- `scripts/scan_slop_signals.py` — heuristic triage scanner, not proof.

## Final checklist

Before stopping, verify that only preferences relevant to the actual visual scope were used or queued; the user was not asked to repeat information; no custom direction was invented without approval; the existing-project scan was performed or intentionally skipped only for first-time creation; the visual direction is product-specific; React/Vue choice is documented when a stack choice was in scope; custom 404 and actual status semantics exist where required; loading/empty/error/retry states work; error telemetry is sanitized; smooth motion respects reduced motion and focus; `seo-production-audit` and `web-engineer` were searched/read and their relevant checks applied after implementation; findings were fixed or documented; tests/build/scanner pass or limitations are explicit; in-scope failures were rechecked; remaining questions are consolidated at the end; and no secrets or unauthorized scope changes were introduced.
