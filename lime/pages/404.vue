<script setup>
useSeoMeta({
  title: 'Not found',
  description: 'The requested page does not exist in the Lime Skills field guide.',
  robots: 'noindex, nofollow'
})
</script>

<template>
  <section class="page-wrap error-page" aria-labelledby="not-found-title">
    <p class="eyebrow">error / 404</p>
    <h1 id="not-found-title">That page went<br /><span>off the map.</span></h1>
    <p>The route you followed does not exist in this field guide. Return to the index or browse the source repository.</p>
    <div class="hero-actions">
      <NuxtLink class="button button-primary" to="/">return to the index <span aria-hidden="true">↗</span></NuxtLink>
      <a class="text-link" href="https://github.com/Haruki9767/lime-skills" target="_blank" rel="noopener noreferrer">browse the source ↗</a>
    </div>
  </section>
</template>
