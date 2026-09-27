<script setup>
import { computed, ref } from "vue";
import { getSkill, skills } from "~/data/skills.js";
import { useScrollAnimations } from "~/composables/useScrollAnimations.js";

const repositoryUrl = "https://github.com/Haruki9767/lime-skills";
const route = useRoute();

definePageMeta({
  validate: (candidateRoute) =>
    Boolean(getSkill(String(candidateRoute.params.slug))),
});

const skill = computed(() => getSkill(String(route.params.slug)));
if (!skill.value) {
  throw createError({ statusCode: 404, statusMessage: "Skill not found" });
}

const pageRoot = ref(null);
useScrollAnimations(pageRoot);

const currentIndex = computed(() =>
  skills.findIndex((item) => item.slug === skill.value.slug),
);
const nextSkill = computed(
  () => skills[(currentIndex.value + 1) % skills.length],
);
const siteUrl = String(useRuntimeConfig().public.siteUrl).replace(/\/+$/, "");
const canonicalUrl = computed(
  () => `${siteUrl}/${encodeURIComponent(String(route.params.slug))}`,
);
const seoTitle = computed(() => skill.value?.name || "Skill not found");
const seoDescription = computed(
  () =>
    skill.value?.description || "The requested Lime Skill could not be found.",
);

useSeoMeta({
  title: seoTitle,
  description: seoDescription,
  ogTitle: computed(() =>
    skill.value
      ? `${skill.value.name} — Lime Skills`
      : "Skill not found — Lime Skills",
  ),
  ogDescription: seoDescription,
  ogUrl: canonicalUrl,
  twitterTitle: computed(() =>
    skill.value
      ? `${skill.value.name} — Lime Skills`
      : "Skill not found — Lime Skills",
  ),
  twitterDescription: seoDescription,
});

useHead(() => ({ link: [{ rel: "canonical", href: canonicalUrl.value }] }));
</script>

<template>
  <div v-if="skill" ref="pageRoot" class="page-wrap detail-page">
    <div class="scroll-progress" data-scroll-progress aria-hidden="true"></div>
    <div class="detail-topline">
      <NuxtLink class="back-link" to="/#skills" data-intro-items
        >← all modules</NuxtLink
      >
      <span class="detail-position"
        >FIELD GUIDE <b>/</b> {{ skill.number }} OF 04</span
      >
    </div>

    <section class="detail-hero" aria-labelledby="detail-title">
      <div class="detail-hero-label" data-intro-kicker>
        <p class="eyebrow">{{ skill.kicker }}</p>
        <span>Module {{ skill.number }}</span>
      </div>
      <div class="detail-hero-main">
        <h1 id="detail-title" class="detail-title">
          <span class="hero-line-mask"
            ><span class="hero-line" data-intro-line>{{
              skill.name
            }}</span></span
          >
        </h1>
        <p class="detail-intro" data-intro-copy>{{ skill.description }}</p>
        <a
          class="text-link detail-source"
          :href="`${repositoryUrl}/tree/main${skill.path}`"
          target="_blank"
          rel="noopener noreferrer"
          data-intro-items
          >Read the full skill ↗</a
        >
      </div>
      <aside class="detail-stamp" aria-label="Module number" data-intro-rail>
        <span class="stamp-label">LIME / FIELD GUIDE</span>
        <strong>{{ skill.number }}</strong>
        <span class="stamp-caption">{{ skill.kicker }}</span>
      </aside>
    </section>

    <section class="detail-content" aria-label="How to use this module">
      <div class="detail-purpose" data-scroll-reveal="left">
        <p class="eyebrow">Why it exists</p>
        <p class="purpose">{{ skill.purpose }}</p>
        <span class="purpose-rule" aria-hidden="true"></span>
      </div>
      <div class="detail-columns" data-scroll-reveal="right">
        <div>
          <p class="eyebrow">Use it when</p>
          <h2>Reach for it</h2>
          <ul>
            <li v-for="item in skill.useWhen" :key="item">{{ item }}</li>
          </ul>
        </div>
        <div>
          <p class="eyebrow">The sequence</p>
          <h2>Core rhythm</h2>
          <ol>
            <li v-for="(item, index) in skill.workflow" :key="item">
              <span>{{ String(index + 1).padStart(2, "0") }}</span
              >{{ item }}
            </li>
          </ol>
        </div>
      </div>
    </section>

    <NuxtLink
      class="detail-next"
      :to="`/${nextSkill.slug}`"
      :aria-label="`Next module: ${nextSkill.name}`"
    >
      <span class="detail-next-label">NEXT IN THE FIELD GUIDE</span>
      <span class="detail-next-title">{{ nextSkill.name }}</span>
      <span class="detail-next-arrow" aria-hidden="true">↗</span>
    </NuxtLink>
  </div>
</template>
