<script setup lang="ts">
import { skills } from '~/data/skills'

useSeoMeta({
  title: 'A field guide for better web work',
  description: 'Four reusable AI skills for coordinating, designing, engineering, and auditing web projects.',
  ogTitle: 'AI Skills — a field guide for better web work',
  ogDescription: 'Four reusable AI skills for better web projects.',
  ogUrl: 'https://lime.isroot.in/',
  twitterTitle: 'AI Skills — a field guide for better web work',
  twitterDescription: 'Four reusable AI skills for better web projects.'
})

const query = ref('')
const filteredSkills = computed(() => skills.filter((skill) => `${skill.name} ${skill.kicker} ${skill.description}`.toLowerCase().includes(query.value.toLowerCase())))
</script>

<template>
  <div class="page-wrap">
    <section class="hero" aria-labelledby="page-title">
      <div class="hero-copy">
        <p class="eyebrow"><span class="status-dot" aria-hidden="true"></span> maintained / open source / 04 modules</p>
        <h1 id="page-title">Make the next<br /><span>web thing</span> better.</h1>
        <p class="hero-lede">A small, opinionated toolkit for agents and humans who care about how a project gets from brief to browser.</p>
        <div class="hero-actions">
          <a class="button button-primary" href="#skills">Explore the skills <span>↓</span></a>
          <a class="text-link" href="https://github.com/Haruki9767/skills" target="_blank" rel="noreferrer">read the source ↗</a>
        </div>
      </div>
      <div class="hero-aside" aria-label="Repository summary">
        <div class="signal-line"><span>repo</span><strong>lime / skills</strong></div>
        <div class="signal-line"><span>stack</span><strong>platform-neutral</strong></div>
        <div class="signal-line"><span>license</span><strong>MIT</strong></div>
        <div class="aside-rule"></div>
        <p>Use the modules in sequence for a full web build—or reach for the one that matches the problem in front of you.</p>
      </div>
    </section>

    <section id="skills" class="skills-section" aria-labelledby="skills-title">
      <div class="section-heading">
        <div><p class="eyebrow">01 / the index</p><h2 id="skills-title">Four ways to<br /><em>stay intentional.</em></h2></div>
        <label class="search-box"><span aria-hidden="true">⌕</span><span class="sr-only">Filter skills</span><input v-model="query" type="search" placeholder="filter the index" /></label>
      </div>
      <div v-if="filteredSkills.length" class="skill-grid">
        <NuxtLink v-for="skill in filteredSkills" :key="skill.slug" :to="`/${skill.slug}`" class="skill-card" :class="`card-${skill.color}`">
          <div class="card-top"><span>{{ skill.number }}</span><span class="arrow" aria-hidden="true">↗</span></div>
          <p class="card-kicker">{{ skill.kicker }}</p>
          <h3>{{ skill.name }}</h3>
          <p>{{ skill.description }}</p>
          <span class="card-path">{{ skill.path }}</span>
        </NuxtLink>
      </div>
      <p v-else class="empty-state">No skill matches “{{ query }}”. Try a broader term.</p>
    </section>

    <section id="about" class="about-section" aria-labelledby="about-title">
      <div class="about-label"><p class="eyebrow">02 / the method</p><span class="vertical-line"></span><span>brief → browser</span></div>
      <div class="about-copy"><h2 id="about-title">Not a prompt dump.<br /><span>A working rhythm.</span></h2><p>These skills are designed to be read, routed, and re-read. They protect the parts of web work that disappear when speed becomes the only metric: clear decisions, honest evidence, humane interfaces, and a clean handoff.</p><a class="text-link" href="https://github.com/Haruki9767/skills" target="_blank" rel="noreferrer">see everything on github ↗</a></div>
    </section>
  </div>
</template>
