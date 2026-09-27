<script setup>
import { computed, nextTick, ref, watch } from "vue";
import { skills } from "~/data/skills.js";
import { useScrollAnimations } from "~/composables/useScrollAnimations.js";

const pageRoot = ref(null);
const { refresh } = useScrollAnimations(pageRoot);
const query = ref("");
const filteredSkills = computed(() => {
  const normalizedQuery = query.value.trim().toLocaleLowerCase();
  return skills.filter((skill) =>
    `${skill.name} ${skill.kicker} ${skill.description}`
      .toLocaleLowerCase()
      .includes(normalizedQuery),
  );
});

watch(filteredSkills, async () => {
  await nextTick();
  refresh();
});

const siteUrl = String(useRuntimeConfig().public.siteUrl).replace(/\/+$/, "");
const canonicalUrl = `${siteUrl}/`;

useSeoMeta({
  title: "Focused tools for better web work",
  description:
    "Four reusable Lime Skills for coordinating, designing, engineering, and auditing web projects.",
  ogTitle: "Lime Skills — focused tools for better web work",
  ogDescription: "Four reusable Lime Skills for better web projects.",
  ogUrl: canonicalUrl,
  twitterTitle: "Lime Skills — focused tools for better web work",
  twitterDescription: "Four reusable Lime Skills for better web projects.",
});

useHead({ link: [{ rel: "canonical", href: canonicalUrl }] });
</script>

<template>
  <div ref="pageRoot" class="page-wrap home-page">
    <div class="scroll-progress" data-scroll-progress aria-hidden="true"></div>

    <section class="hero" aria-labelledby="page-title">
      <div class="hero-layout">
        <div class="hero-copy">
          <h1 id="page-title" class="hero-title">
            <span class="hero-line-mask"
              ><span class="hero-line" data-intro-line>From brief</span></span
            >
            <span class="hero-line-mask"
              ><span class="hero-line hero-line--pink" data-intro-line
                >to browser.</span
              ></span
            >
          </h1>
          <p class="hero-lede" data-intro-copy>
            A focused toolkit for better web work.
          </p>
          <div class="hero-actions" data-intro-items>
            <a class="button button-primary" href="#skills"
              >Explore skills <span aria-hidden="true">↓</span></a
            >
          </div>
        </div>
      </div>
    </section>

    <section id="skills" class="skills-section" aria-labelledby="skills-title">
      <div class="section-heading" data-scroll-reveal="up">
        <div>
          <h2 id="skills-title">Find your<br /><em>next move.</em></h2>
        </div>
        <label class="search-box">
          <span class="search-icon" aria-hidden="true">⌕</span>
          <span class="sr-only">Filter skills</span>
          <input
            v-model="query"
            type="search"
            placeholder="Filter the index"
            aria-controls="skill-results"
          />
          <span class="search-count">{{
            String(filteredSkills.length).padStart(2, "0")
          }}</span>
        </label>
      </div>

      <div id="skill-results" class="skill-grid" aria-live="polite">
        <NuxtLink
          v-for="(skill, index) in skills"
          v-show="filteredSkills.includes(skill)"
          :key="skill.slug"
          :to="`/${skill.slug}`"
          class="skill-card"
          :class="`skill-card--${index + 1}`"
          :data-card-order="index"
        >
          <div class="card-top">
            <span class="card-arrow" aria-hidden="true">↗</span>
          </div>
          <p class="card-kicker">{{ skill.kicker }}</p>
          <h3>{{ skill.name }}</h3>
          <p class="card-description">{{ skill.description }}</p>
        </NuxtLink>
      </div>
      <p v-if="!filteredSkills.length" class="empty-state" role="status">
        No skill matches “{{ query.trim() }}”. Try a broader term.
      </p>
    </section>

    <section id="about" class="about-section" aria-labelledby="about-title">
      <div class="about-heading" data-scroll-reveal="left">
        <p class="eyebrow">The method</p>
        <h2 id="about-title">A working<br /><span>rhythm.</span></h2>
      </div>
      <div class="about-body" data-scroll-reveal="right">
        <p>
          These skills protect the parts of web work that disappear when speed
          becomes the only metric: clear decisions, honest evidence, humane
          interfaces, and a clean handoff.
        </p>
      </div>
    </section>
  </div>
</template>
