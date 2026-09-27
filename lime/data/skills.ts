export type Skill = {
  slug: string
  name: string
  kicker: string
  description: string
  purpose: string
  color: string
  number: string
  useWhen: string[]
  workflow: string[]
  path: string
}

export const skills: Skill[] = [
  {
    slug: 'guidance', number: '01', name: 'Guidance', kicker: 'project coordination', color: 'acid',
    description: 'The routing layer for meaningful web work. It keeps scope, architecture, handoffs, and delivery understandable.',
    purpose: 'Start here when a change crosses skills, architecture, agents, or deployment. Guidance classifies the work, protects boundaries, and keeps the project moving in reversible checkpoints.',
    useWhen: ['Adding a feature or changing architecture', 'Switching agents or coordinating specialists', 'Writing migrations, handoffs, or deployment plans'],
    workflow: ['Discover and route to the right skill', 'Classify frontend, backend, or hybrid scope', 'Build the skeleton before refinement', 'Verify, document, and hand off'], path: '/guidance/'
  },
  {
    slug: 'web-design', number: '02', name: 'Web Design', kicker: 'visual direction + interaction', color: 'mint',
    description: 'A practical design system for distinctive, usable interfaces that do not collapse into generic AI defaults.',
    purpose: 'Use it to give a website a clear point of view while protecting hierarchy, accessibility, responsive behavior, motion, and user intent.',
    useWhen: ['Creating or redesigning a website', 'Choosing Vue or React deliberately', 'Reviewing visual quality and anti-slop signals'],
    workflow: ['Clarify preferences and constraints', 'Scan existing work or define a thesis', 'Implement with states and accessible motion', 'Hand off to SEO and engineering'], path: '/web-design/'
  },
  {
    slug: 'web-engineer', number: '03', name: 'Web Engineer', kicker: 'quality + trust boundaries', color: 'white',
    description: 'The engineering review layer for framework choices, accessibility, security, privacy readiness, and launch quality.',
    purpose: 'Use it before and after implementation to inspect the real project, research authoritative practices, and fix evidence-backed issues without silently expanding scope.',
    useWhen: ['Auditing or building a web project', 'Checking auth, APIs, forms, and business logic', 'Preparing CI, policies, and production launch'],
    workflow: ['Discover stack, routes, and data flows', 'Research current primary sources', 'Audit SEO, accessibility, security, and logic', 'Verify with fresh evidence before shipping'], path: '/web-engineer/'
  },
  {
    slug: 'seo-production-audit', number: '04', name: 'SEO Production Audit', kicker: 'discoverability + indexability', color: 'acid',
    description: 'A production-minded audit for metadata, crawl controls, structured data, accessibility boundaries, and route readiness.',
    purpose: 'Use it after implementation or whenever search visibility matters. It turns every public route into a clear, crawlable, evidence-backed experience.',
    useWhen: ['Launching a public site', 'Reviewing titles, canonicals, OG cards, or sitemap', 'Checking route status, headings, alt text, and indexability'],
    workflow: ['Discover framework, domain, and route classes', 'Audit metadata on every public page', 'Check crawling, content, images, and forms', 'Run launch checks and report remaining issues'], path: '/seo-production-audit/'
  }
]

export const getSkill = (slug: string) => skills.find((skill) => skill.slug === slug)
