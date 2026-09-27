# Review Checklist

## Evidence

- [ ] User brief, PRD, design file, and constraints were read.
- [ ] Target, mode, stack, framework choice, routes, and changed-file scope are recorded.
- [ ] Visual findings cite a screenshot, DOM observation, or rendered URL when possible.
- [ ] Source findings cite `path:line`.
- [ ] Low-confidence observations are labeled rather than asserted.

## Visual and responsive

- [ ] First viewport states the product and primary action clearly.
- [ ] One visual anchor is stronger than supporting decoration.
- [ ] Sections have distinct jobs; cards are justified by content.
- [ ] Color, type, material, and style choices have a brief-specific rationale and user approval.
- [ ] Glass, gradients, and skeuomorphic details preserve contrast and have fallbacks.
- [ ] Hover, focus, active, loading, error, empty, permission, retry, and 404 states are coherent.
- [ ] Unknown routes return an actual HTTP 404 where direct/server checks apply.
- [ ] Check 320px, 768px, 1024px, and desktop; no unintended horizontal overflow.
- [ ] Motion is purposeful, interruptible, performant, and reduced-motion aware.

## Accessibility

- [ ] Keyboard navigation and visible focus work.
- [ ] Names/labels exist for controls and form fields.
- [ ] Contrast is sufficient in default and interactive states.
- [ ] Color is not the only state signal.
- [ ] Images have meaningful or intentionally empty alt text.
- [ ] Semantic headings, landmarks, and error messages are coherent.
- [ ] `prefers-reduced-motion` is honored for animation and smooth scrolling.
- [ ] Zoom, reflow, touch targets, and screen-reader behavior were considered.

## Code hygiene, error handling, and logic

- [ ] pnpm scripts, linter, typecheck, tests, and build were run when available.
- [ ] No unverified unused imports/exports or orphaned styles/assets were removed.
- [ ] Routes and links resolve; forms have success and failure paths.
- [ ] Async loading, cancellation, retries, and stale state are reasonable.
- [ ] React boundaries/async handling or Vue error handlers/async handling cover relevant failures.
- [ ] Error telemetry is structured and sanitized; no secrets, cookies, tokens, or sensitive bodies are exposed.
- [ ] No console errors, hydration mismatch, broken asset, or runtime exception was introduced.
- [ ] Existing API contracts, backend config, dependencies, and design tokens remain intact unless approved.
- [ ] Diff is limited to requested scope and has no accidental generated files or secrets.

## Post-build quality handoff

- [ ] Current `seo-production-audit` skill was searched/read and its relevant checks were applied.
- [ ] Current `web-engineer` skill was searched/read and its relevant checks were applied.
- [ ] Authorized SEO, accessibility, security, privacy/policy, and logic findings were fixed.
- [ ] Both handoff checks and the anti-slop scan were re-run after fixes.

## Final review

- [ ] Re-run mechanical anti-slop scan after edits.
- [ ] Re-run original failing or relevant quality commands.
- [ ] Inspect the final diff as a reviewer.
- [ ] Verify intended files and routes exist and are complete.
- [ ] Report what was verified, what was not, and any user decision still required.
