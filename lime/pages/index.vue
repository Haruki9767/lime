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
  title: "A field guide for better web work",
  description:
    "Four reusable Lime Skills for coordinating, designing, engineering, and auditing web projects.",
  ogTitle: "Lime Skills — a field guide for better web work",
  ogDescription: "Four reusable Lime Skills for better web projects.",
  ogUrl: canonicalUrl,
  twitterTitle: "Lime Skills — a field guide for better web work",
  twitterDescription: "Four reusable Lime Skills for better web projects.",
});

useHead({ link: [{ rel: "canonical", href: canonicalUrl }] });
</script>

<template>
  <div ref="pageRoot" class="page-wrap home-page">
    <div class="scroll-progress" data-scroll-progress aria-hidden="true"></div>

    <section class="hero" aria-labelledby="page-title">
      <div class="hero-meta" data-intro-kicker>
        <span
          ><i class="status-dot" aria-hidden="true"></i> field guide / 001</span
        >
        <span class="hero-meta-right">open source <b>·</b> four modules</span>
      </div>

      <div class="hero-layout">
        <div class="hero-copy">
          <p class="hero-overline" data-intro-copy>
            Good work is a route, not a prompt.
          </p>
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
            A small, opinionated toolkit for agents and humans who care about
            how a project gets from brief to browser.
          </p>
          <div class="hero-actions" data-intro-items>
            <a class="button button-primary" href="#skills"
              >Explore the skills <span aria-hidden="true">↓</span></a
            >
            <a
              class="text-link"
              href="https://github.com/Haruki9767/lime-skills"
              target="_blank"
              rel="noopener noreferrer"
              >Read the source ↗</a
            >
          </div>
        </div>

        <nav
          class="module-rail"
          aria-label="Explore the four Lime Skills"
          data-intro-rail
        >
          <div class="module-rail-head">
            <span>Run of show</span>
            <span>01 — 04</span>
          </div>
          <NuxtLink
            v-for="skill in skills"
            :key="skill.slug"
            class="module-link"
            :to="`/${skill.slug}`"
            data-intro-rail-item
          >
            <span class="rail-number">{{ skill.number }}</span>
            <span class="rail-name">{{ skill.name }}</span>
            <span class="rail-arrow" aria-hidden="true">↗</span>
          </NuxtLink>
          <div class="module-rail-foot">
            <span>BRIEF</span
            ><span class="rail-connector" aria-hidden="true"></span
            ><span>BROWSER</span>
          </div>
        </nav>
      </div>

      <a class="scroll-cue" href="#skills" data-intro-items>
        <span class="scroll-cue-mark" aria-hidden="true">↓</span>
        <span>Scroll to open the index</span>
        <span class="scroll-cue-index">01 / 03</span>
      </a>
    </section>

    <section id="skills" class="skills-section" aria-labelledby="skills-title">
      <div class="section-bar">
        <span>01 / The index</span>
        <span>Choose a lever. Move the work.</span>
      </div>
      <div class="section-heading" data-scroll-reveal="up">
        <div>
          <p class="eyebrow">Four focused modules</p>
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
          <span class="card-watermark" aria-hidden="true">{{
            skill.number
          }}</span>
          <div class="card-top">
            <span class="card-index">MODULE {{ skill.number }}</span>
            <span class="card-arrow" aria-hidden="true">↗</span>
          </div>
          <p class="card-kicker">{{ skill.kicker }}</p>
          <h3>{{ skill.name }}</h3>
          <p class="card-description">{{ skill.description }}</p>
          <span class="card-path"
            >{{ skill.path }} <span aria-hidden="true">→</span></span
          >
        </NuxtLink>
      </div>
      <p v-if="!filteredSkills.length" class="empty-state" role="status">
        No skill matches “{{ query.trim() }}”. Try a broader term.
      </p>
    </section>

    <section id="about" class="about-section" aria-labelledby="about-title">
      <div class="about-heading" data-scroll-reveal="left">
        <p class="eyebrow">02 / The method</p>
        <h2 id="about-title">
          Not a prompt dump.<br /><span>A working rhythm.</span>
        </h2>
      </div>
      <div class="about-body" data-scroll-reveal="right">
        <p>
          These skills protect the parts of web work that disappear when speed
          becomes the only metric: clear decisions, honest evidence, humane
          interfaces, and a clean handoff.
        </p>
        <div
          class="workflow-line"
          aria-label="The work moves from brief to browser"
        >
          <span>Brief</span><i aria-hidden="true"></i><span>Direction</span
          ><i aria-hidden="true"></i><span>Build</span><i aria-hidden="true"></i
          ><span>Browser</span>
        </div>
        <a
          class="text-link"
          href="https://github.com/Haruki9767/lime-skills"
          target="_blank"
          rel="noopener noreferrer"
          >See everything on GitHub ↗</a
        >
      </div>
    </section>
  </div>
</template>
