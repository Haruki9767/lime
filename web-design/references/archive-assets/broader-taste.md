# Broader Taste — UI/UX, Motion, and Design-System Craft

This skill defines a specific hero pattern (see `visual-reference.md`). This file layers in general craft guidance pulled from adjacent skills so the rest of the site — not just the hero — reads as premium. Consult it after the hero is built, while doing the nav/sections/footer and any interactivity.

## From `ui-ux-pro-max` — professional polish checklist

Run this checklist before calling any page done. These are the details that separate "AI template" from "agency build":

**Icons & visual elements**
- No emoji as UI icons — use **Phosphor Icons** (`@phosphor-icons/react` for React/Next.js) as the default icon set for this skill, not Lucide/Heroicons — its weight variants (thin/light/regular/bold/fill/duotone) match the editorial, high-end tone of the reference layouts better than single-weight icon sets
- Pick one Phosphor weight for the whole project (typically `regular` or `light` for nav/UI chrome, `fill` reserved for active/selected states) and stay consistent — don't mix weights arbitrarily
- One consistent icon set and size per project (fixed viewBox, e.g. `w-6 h-6` everywhere)
- Verify brand/logo SVGs against a real source rather than guessing paths

**Interaction**
- Every clickable element gets `cursor-pointer` and a visible hover state (color/opacity/border change — not a layout-shifting scale transform)
- Transitions: 150–300ms, never instant, never sluggish (>500ms)
- Visible focus states for keyboard navigation

**Contrast & modes**
- Light mode text: minimum slate-900-equivalent for body copy, never below slate-600 for muted text
- Glass/translucent panels need enough opacity (`bg-white/80`+) to stay legible in light mode — `bg-white/10` reads as broken, not elegant
- Borders must be visible in both light and dark mode (avoid `border-white/10` in light contexts)

**Layout**
- Floating navbars get real edge spacing (e.g. `top-4 left-4 right-4`), not flush to the viewport edge
- Fixed nav height is always accounted for in content padding
- One consistent max-width container across the whole site (`max-w-7xl` or similar) — don't mix container widths per section
- Test at 320px, 768px, 1024px, 1440px; no horizontal scroll on mobile

**Accessibility**
- Alt text on every image (including hero backgrounds — empty `alt=""` is fine only when the image is purely decorative and the headline conveys the same info)
- Labels on all form inputs
- Never use color as the only differentiator (e.g. error states need an icon/text too)
- Respect `prefers-reduced-motion` for any animation added below

If deeper style/palette/typography exploration is needed (picking a full color system, font pairing, or landing-page section structure for a specific industry), consult the `ui-ux-pro-max` skill directly — it has a searchable database (`search.py`) across style, color, typography, and landing-page-structure domains. Use it for that decision-making layer; this skill still owns the final visual identity rules (no gradients, hero pattern) regardless of what it suggests.

## From GSAP — motion for scroll-driven premium feel

The reference hero images are static, but the sites they're drawn from typically pair that hero with subtle scroll-driven motion further down the page. Use GSAP (not CSS-only) once motion needs to be scroll-linked or sequenced:

- **Entrance animations on scroll**: use `ScrollTrigger.batch()` to fade/slide-in cards or sections as they enter the viewport (`onEnter` → `opacity/y` tween with a small stagger). This is the single highest-impact motion pattern for a landing page — apply it to feature grids, testimonial rows, and portfolio items.
- **Hero itself**: keep hero entrance motion simple and fast (a single fade/slide-up on the headline block on page load is enough — don't scroll-trigger the very first viewport, since it's visible immediately).
- **Parallax accents** (optional, use sparingly): a slow `scrub`-linked transform on the background image (subtle `y` or `scale` drift) can reinforce the "premium" feel, but keep the movement small (under 10% of element size) so it doesn't fight the solid-scrim/no-gradient rule by introducing visual noise.
- Always: `gsap.registerPlugin(ScrollTrigger)` once, respect `prefers-reduced-motion` by checking it and skipping/softening motion, remove `markers: true` before shipping, and clean up with `useGSAP()` (React) so triggers don't leak across route changes in Next.js.
- For sequenced multi-step reveals (e.g. headline → subhead → CTA staggering in on load), use a `gsap.timeline()` rather than separate uncoordinated tweens — see the `gsap-timeline` and `gsap-core` skills for syntax.

Don't over-animate: one clear entrance pattern used consistently beats five different scroll effects competing for attention. This mirrors the restraint principle in `visual-reference.md`.

## From Figma — when a design file exists first

If the user has a Figma file for this project (a link, or they mention "the Figma design"), prefer translating that file into code over inventing a fresh layout, even within this skill's visual constraints:

- Use the `figma-design-to-code` skill's workflow for pulling real design context (`get_design_context`) rather than eyeballing a screenshot — it returns structured layout/token data plus a screenshot, which keeps spacing and type sizes exact instead of approximated.
- Pull actual color/spacing/type tokens via `get_variable_defs` and reuse them as the site's design tokens (Tailwind theme values) instead of hardcoding hex/px values inferred from a screenshot — this keeps the codebase in sync if the Figma file is updated later.
- If the Figma file already defines a component library (buttons, nav, cards), check for Code Connect mappings first (`get_code_connect_map`) so generated code reuses the project's real components instead of re-implementing visually-similar-but-divergent ones.
- Still enforce this skill's rules on top of whatever the Figma file contains: if the Figma design uses a gradient, flag it to the user and propose a solid-color alternative rather than silently reproducing it — the no-gradient rule in this skill is a stated hard constraint, not a style default to defer to source files.
- For net-new design work (no existing Figma file, user just wants code), don't create a Figma file as an intermediate step — go straight to code using this skill's templates. Only loop through Figma when a file already exists or the user explicitly wants the design authored there first.

## Summary: layering order

1. `visual-reference.md` — the hero pattern (structural, non-negotiable)
2. This file's UI/UX checklist — craft/polish pass, applies everywhere on the site
3. GSAP motion — added once static layout is correct, for scroll sections below the hero
4. Figma — only enters the loop if a design file already exists or is explicitly requested
