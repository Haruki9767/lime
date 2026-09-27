<script setup>
import { computed } from 'vue'

const props = defineProps({
  error: { type: Object, default: () => ({}) }
})

const statusCode = computed(() => Number(props.error?.statusCode ?? 500))
const isNotFound = computed(() => statusCode.value === 404)
const message = computed(() => isNotFound.value
  ? 'The route you followed does not exist in this field guide. Head back to the index and pick another path.'
  : 'The field guide could not load this page. Return to the index and try again.')

useSeoMeta({ title: computed(() => isNotFound.value ? 'Not found' : 'Something went wrong'), robots: 'noindex' })
</script>

<template>
  <section class="page-wrap error-page" aria-labelledby="error-title">
    <p class="eyebrow">error / {{ statusCode }}</p>
    <h1 v-if="isNotFound" id="error-title">That page went<br /><span>off the map.</span></h1>
    <h1 v-else id="error-title">Something went<br /><span>off the map.</span></h1>
    <p>{{ message }}</p>
    <NuxtLink class="button button-primary" to="/">return to the index <span aria-hidden="true">↗</span></NuxtLink>
  </section>
</template>
