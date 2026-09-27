<script setup>
import { computed, ref } from 'vue'
import { skills } from '~/data/skills.js'
import { useScrollAnimations } from '~/composables/useScrollAnimations.js'

const pageRoot = ref(null)
useScrollAnimations(pageRoot)

const query = ref('')
const filteredSkills = computed(() => {
  const normalizedQuery = query.value.trim().toLocaleLowerCase()
  return skills.filter((skill) => `${skill.name} ${skill.kicker} ${skill.description}`.toLocaleLowerCase().includes(normalizedQuery))
})

const siteUrl = String(useRuntimeConfig().public.siteUrl).replace(/\/+$/, '')
const canonicalUrl = `${siteUrl}/`

useSeoMeta({
  title: 'A field guide for better web work',
  description: 'Four reusable Lime Skills for coordinating, designing, engineering, and auditing web projects.',
  ogTitle: 'Lime Skills — a field guide for better web work',
  ogDescription: 'Four reusable Lime Skills for better web projects.',
  ogUrl: canonicalUrl,
  twitterTitle: 'Lime Skills — a field guide for better web work',
  twitterDescription: 'Four reusable Lime Skills for better web projects.'
})

useHead({ link: [{ rel: 'canonical', href: canonicalUrl }] })
</script>

<template>
  <div ref="pageRoot" class="page-wrap">
    <div class="scroll-progress" data-scroll-progress aria-hidden="true"></div>
    <section class="hero" aria-labelledby="page-title">
      <div class="hero-copy" data-reveal>
        <p class="eyebrow"><span class="status-dot" aria-hidden="true"></span> maintained / open source / 04 modules</p>
        <h1 id="page-title">Make the next<br /><span>web thing</span> better.</h1>
        <p class="hero-lede">A small, opinionated toolkit for agents and humans who care about how a project gets from brief to browser.</p>
        <div class="hero-actions">
          <a class="button button-primary" href="#skills">Explore the skills <span aria-hidden="true">↓</span></a>
          <a class="text-link" href="https://github.com/Haruki9767/lime-skills" target="_blank" rel="noopener noreferrer">read the source ↗</a>
        </div>
      </div>
      <aside class="hero-aside" aria-label="Repository summary" data-reveal>
        <div class="signal-line"><span>repo</span><strong>lime / skills</strong></div>
        <div class="signal-line"><span>stack</span><strong>platform-neutral</strong></div>
        <div class="signal-line"><span>license</span><strong>MIT</strong></div>
        <div class="aside-rule" aria-hidden="true"></div>
        <p>Use the modules in sequence for a full web build—or reach for the one that matches the problem in front of you.</p>
      </aside>
    </section>

    <section id="skills" class="skills-section" aria-labelledby="skills-title">
      <div class="section-heading" data-reveal>
        <div><p class="eyebrow">01 / the index</p><h2 id="skills-title">Four ways to<br /><em>stay intentional.</em></h2></div>
        <label class="search-box"><span aria-hidden="true">⌕</span><span class="sr-only">Filter skills</span><input v-model="query" type="search" placeholder="filter the index" aria-controls="skill-results" /></label>
      </div>
      <div v-if="filteredSkills.length" id="skill-results" class="skill-grid">
        <NuxtLink v-for="skill in filteredSkills" :key="skill.slug" :to="`/${skill.slug}`" class="skill-card">
          <div class="card-top"><span>{{ skill.number }}</span><span class="arrow" aria-hidden="true">↗</span></div>
          <p class="card-kicker">{{ skill.kicker }}</p>
          <h3>{{ skill.name }}</h3>
          <p>{{ skill.description }}</p>
          <span class="card-path">{{ skill.path }}</span>
        </NuxtLink>
      </div>
      <p v-else class="empty-state" role="status">No skill matches “{{ query.trim() }}”. Try a broader term.</p>
    </section>

    <section id="about" class="about-section" aria-labelledby="about-title">
      <div class="about-label" data-reveal><p class="eyebrow">02 / the method</p><span class="vertical-line" aria-hidden="true"></span><span>brief → browser</span></div>
      <div class="about-copy" data-reveal><h2 id="about-title">Not a prompt dump.<br /><span>A working rhythm.</span></h2><p>These skills are designed to be read, routed, and re-read. They protect the parts of web work that disappear when speed becomes the only metric: clear decisions, honest evidence, humane interfaces, and a clean handoff.</p><a class="text-link" href="https://github.com/Haruki9767/lime-skills" target="_blank" rel="noopener noreferrer">see everything on github ↗</a></div>
    </section>
  </div>
</template>
