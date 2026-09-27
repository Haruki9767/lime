<script setup lang="ts">
defineProps<{ error: { statusCode?: number; message?: string } }>()
useSeoMeta({ title: 'Not found', robots: 'noindex' })
</script>

<template>
  <main class="page-wrap error-page">
    <p class="eyebrow">error / 404</p>
    <h1>That page went<br /><span>off the map.</span></h1>
    <p>The route you followed does not exist in this field guide. Head back to the index and pick another path.</p>
    <NuxtLink class="button button-primary" to="/">return to the index <span>↗</span></NuxtLink>
  </main>
</template>
