<script setup lang="ts">
import { getSkill } from '~/data/skills'

const route = useRoute()
const skill = computed(() => getSkill(String(route.params.slug)))
if (!skill.value) throw createError({ statusCode: 404, statusMessage: 'Skill not found' })

useSeoMeta({
  title: skill.value?.name || 'Skill not found',
  description: skill.value?.description || 'The requested AI skill could not be found.',
  ogTitle: skill.value ? `${skill.value.name} — AI Skills` : 'Skill not found — AI Skills',
  ogDescription: skill.value?.description,
  ogUrl: `https://lime.isroot.in/${route.params.slug}`
})
</script>

<template>
  <div v-if="skill" class="page-wrap detail-page">
    <NuxtLink class="back-link" to="/">← all skills</NuxtLink>
    <section class="detail-hero" :class="`detail-${skill.color}`">
      <p class="eyebrow">{{ skill.number }} / {{ skill.kicker }}</p>
      <h1>{{ skill.name }}</h1>
      <p class="detail-intro">{{ skill.description }}</p>
      <span class="detail-path">source: {{ skill.path }}</span>
    </section>
    <section class="detail-content">
      <div><p class="eyebrow">why it exists</p><p class="purpose">{{ skill.purpose }}</p></div>
      <div class="detail-columns"><div><h2>Reach for it when</h2><ul><li v-for="item in skill.useWhen" :key="item">{{ item }}</li></ul></div><div><h2>Core rhythm</h2><ol><li v-for="(item, index) in skill.workflow" :key="item"><span>0{{ index + 1 }}</span>{{ item }}</li></ol></div></div>
    </section>
    <a class="button button-primary" :href="`https://github.com/Haruki9767/skills/tree/main${skill.path}`" target="_blank" rel="noreferrer">read the full skill ↗</a>
  </div>
</template>
