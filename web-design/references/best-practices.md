# Web-Design Best Practices

Re-check these official sources when versions, browser behavior, or project constraints change. Use the practices as decision rules, not as a reason to impose a style.

## Framework choice

Keep a healthy existing stack unless a concrete requirement justifies migration. Prefer React when the project needs its library/ecosystem breadth, existing React systems, integrations, or React Native strategy; prefer Vue when an integrated, progressive framework, HTML/CSS/JavaScript templates, Single-File Components, and incremental adoption fit better. Compare SSR/SSG, SEO, bundle/performance budgets, routing/data choices, hosting, testing, accessibility, team skill, and maintenance. There is no universal winner; prototype the riskiest route when safe, then queue an outcome-changing stack question for the final batch only when a stack choice is actually in scope.

Sources:

- [React Installation](https://react.dev/learn/installation)
- [React: Build a React app from scratch](https://react.dev/learn/build-a-react-app-from-scratch)
- [Vue Introduction](https://vuejs.org/guide/introduction.html)
- [Vue Tooling](https://vuejs.org/guide/scaling-up/tooling.html)

## Distinctive design

Start from product, audience, content, brand personality, and task evidence. Write a visual thesis and define a small grammar for type, spacing, color, shape/material, imagery, iconography, elevation, motion, and content tone. Use hierarchy and product-specific states to create personality; do not blindly combine trendy gradients, glass cards, neon colors, generic dashboards, stock hero art, or interchangeable copy. Glassmorphism, skeuomorphism, gradients, and other styles are optional tools: use them only when the user prefers them or they communicate a real interaction, while preserving contrast and fallbacks.

Sources:

- [Nielsen Norman Group: Principles of Visual Design](https://www.nngroup.com/articles/principles-visual-design/)
- [Nielsen Norman Group: Glassmorphism](https://www.nngroup.com/articles/glassmorphism/)
- [Nielsen Norman Group: Design Systems 101](https://www.nngroup.com/articles/design-systems-101/)
- [W3C: Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- [W3C: Non-text Contrast](https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html)

## 404 and error handling

Return actual HTTP 404 for missing resources and use 410 for permanent removal; do not let an SPA’s branded fallback turn direct unknown routes into 200 responses. Make the custom 404 clear, on-brand, and helpful with navigation, search, home, retry, or related content. Handle loading, empty, validation, permission, network, and server-error states distinctly. Use React Error Boundaries for rendering failures plus explicit async/event handling; use Vue `app.config.errorHandler`/`errorCaptured` and explicit async/router handling. Keep fallback UI separate from sanitized telemetry and never log secrets, tokens, cookies, raw bodies, or sensitive personal data.

Sources:

- [MDN: 404 Not Found](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/404)
- [MDN: Window error event](https://developer.mozilla.org/en-US/docs/Web/API/Window/error_event)
- [MDN: Window unhandledrejection event](https://developer.mozilla.org/en-US/docs/Web/API/Window/unhandledrejection_event)
- [React Component error boundaries](https://react.dev/reference/react/Component)
- [React Suspense](https://react.dev/reference/react/Suspense)
- [Vue app.config.errorHandler](https://vuejs.org/api/application.html#app-config-errorhandler)
- [Vue async components](https://vuejs.org/guide/components/async)
- [Vue Suspense](https://vuejs.org/guide/built-ins/suspense.html)

## Motion and accessibility

Use motion to communicate hierarchy or state, not as decoration everywhere. Honor `prefers-reduced-motion: reduce`, provide a static or less-motion alternative, avoid unnecessary parallax/scroll-linked movement, and offer a user control for substantial non-essential animation. Use smooth scrolling only for navigation/CSSOM-triggered scrolling, preserve normal anchors, keep visible focus, and progressively enhance from semantic HTML and instant scrolling. Test keyboard, screen reader, focus, contrast, zoom, touch, and reduced motion.

Sources:

- [MDN: prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)
- [MDN: scroll-behavior](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-behavior)
- [W3C: Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)
- [W3C: Pause, Stop, Hide](https://www.w3.org/WAI/WCAG21/Understanding/pause-stop-hide.html)
- [W3C: Focus Visible](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html)

## Caveats

Official framework documentation describes capabilities, not a guarantee of lower cost or better outcomes. Framework choice does not determine accessibility, SEO, performance, or security. Glass, skeuomorphism, and other visual styles can fail when they reduce contrast, obscure hierarchy, or imply false affordances. WCAG and MDN guidance should be applied to the actual product and user preferences, not used to justify decorative motion or an unapproved redesign.
