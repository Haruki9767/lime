<script setup>
import { computed, ref } from 'vue'
import { getSkill } from '~/data/skills.js'
import { useScrollAnimations } from '~/composables/useScrollAnimations.js'

const repositoryUrl = 'https://github.com/Haruki9767/lime-skills'
const route = useRoute()

definePageMeta({
  validate: (candidateRoute) => Boolean(getSkill(String(candidateRoute.params.slug)))
})

const skill = computed(() => getSkill(String(route.params.slug)))
if (!skill.value) {
  throw createError({ statusCode: 404, statusMessage: 'Skill not found' })
}

const pageRoot = ref(null)
useScrollAnimations(pageRoot)

const siteUrl = String(useRuntimeConfig().public.siteUrl).replace(/\/+$/, '')
const canonicalUrl = computed(() => `${siteUrl}/${encodeURIComponent(String(route.params.slug))}`)
const seoTitle = computed(() => skill.value?.name || 'Skill not found')
const seoDescription = computed(() => skill.value?.description || 'The requested Lime Skill could not be found.')

useSeoMeta({
  title: seoTitle,
  description: seoDescription,
  ogTitle: computed(() => skill.value ? `${skill.value.name} — Lime Skills` : 'Skill not found — Lime Skills'),
  ogDescription: seoDescription,
  ogUrl: canonicalUrl,
  twitterTitle: computed(() => skill.value ? `${skill.value.name} — Lime Skills` : 'Skill not found — Lime Skills'),
  twitterDescription: seoDescription
})

useHead(() => ({ link: [{ rel: 'canonical', href: canonicalUrl.value }] }))
</script>

<template>
  <div v-if="skill" ref="pageRoot" class="page-wrap detail-page">
    <div class="scroll-progress" data-scroll-progress aria-hidden="true"></div>
    <NuxtLink class="back-link" to="/">← all skills</NuxtLink>
    <section class="detail-hero" data-reveal>
      <p class="eyebrow">{{ skill.number }} / {{ skill.kicker }}</p>
      <h1>{{ skill.name }}</h1>
      <p class="detail-intro">{{ skill.description }}</p>
      <span class="detail-path">source: {{ skill.path }}</span>
    </section>
    <section class="detail-content">
      <div data-reveal><p class="eyebrow">why it exists</p><p class="purpose">{{ skill.purpose }}</p></div>
      <div class="detail-columns" data-reveal><div><h2>Reach for it when</h2><ul><li v-for="item in skill.useWhen" :key="item">{{ item }}</li></ul></div><div><h2>Core rhythm</h2><ol><li v-for="(item, index) in skill.workflow" :key="item"><span>{{ String(index + 1).padStart(2, '0') }}</span>{{ item }}</li></ol></div></div>
    </section>
    <a class="button button-primary" :href="`${repositoryUrl}/tree/main${skill.path}`" target="_blank" rel="noopener noreferrer" data-reveal>read the full skill ↗</a>
  </div>
</template>
