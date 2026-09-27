<script setup lang="ts">
useHead({
  titleTemplate: (title) => title ? `${title} — Lime Skills` : 'Lime Skills — a field guide for better web work',
  meta: [
    { name: 'description', content: 'A compact field guide to the reusable Guidance, Web Design, Web Engineer, and SEO Production Audit skills in the skills repository.' },
    { name: 'theme-color', content: '#0b0f0c' },
    { property: 'og:site_name', content: 'Lime Skills' },
    { property: 'og:type', content: 'website' },
    { name: 'twitter:card', content: 'summary' }
  ],
  link: [{ rel: 'canonical', href: 'https://lime.isroot.in/' }]
})
</script>

<template>
  <div class="site-shell">
    <header class="site-header">
      <NuxtLink class="brand" to="/" aria-label="Lime Skills home"><span class="brand-mark">[</span>lime skills<span class="brand-mark">]</span></NuxtLink>
      <nav class="site-nav" aria-label="Primary navigation">
        <a href="#skills">Index</a>
        <a href="#about">About</a>
        <a href="https://github.com/Haruki9767/skills" target="_blank" rel="noreferrer">GitHub ↗</a>
      </nav>
    </header>
    <main id="main-content"><NuxtPage /></main>
    <footer class="site-footer">
      <p class="footer-note">Made for the messy middle between idea and shipped.</p>
      <div class="footer-links">
        <a href="https://github.com/Haruki9767/skills" target="_blank" rel="noreferrer">repo / github ↗</a>
        <a href="https://lime.is-a.dev" target="_blank" rel="noreferrer">lime.is-a.dev ↗</a>
      </div>
      <span class="footer-stamp">© {{ new Date().getFullYear() }} / MIT</span>
    </footer>
  </div>
</template>
