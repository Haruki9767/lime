<script setup>
import { nextTick } from "vue";

const repositoryUrl = "https://github.com/Haruki9767/lime-skills";
const title = "Lime Skills — a field guide for better web work";
const router = useRouter();

useHead({
  titleTemplate: (pageTitle) =>
    pageTitle ? `${pageTitle} — Lime Skills` : title,
  meta: [
    {
      name: "description",
      content:
        "A compact field guide to reusable skills for coordinating, designing, engineering, and auditing web projects.",
    },
    { name: "theme-color", content: "#08080a" },
    { property: "og:site_name", content: "Lime Skills" },
    { property: "og:type", content: "website" },
    { name: "twitter:card", content: "summary" },
  ],
});

function scrollToRouteDestination(destination) {
  if (destination.hash) {
    let targetId = destination.hash.slice(1);
    try {
      targetId = decodeURIComponent(targetId);
    } catch {
      // Keep the literal hash if a URL contains malformed percent-encoding.
    }

    const target = document.getElementById(targetId);
    if (target) {
      const behavior = window.matchMedia("(prefers-reduced-motion: reduce)")
        .matches
        ? "auto"
        : "smooth";
      target.scrollIntoView({ behavior, block: "start" });
      return;
    }
  }

  const root = document.documentElement;
  const previousScrollBehavior = root.style.scrollBehavior;
  root.style.scrollBehavior = "auto";
  window.scrollTo({ top: 0, left: 0, behavior: "auto" });
  requestAnimationFrame(() => {
    root.style.scrollBehavior = previousScrollBehavior;
  });
}

router.afterEach((to, from, failure) => {
  if (!import.meta.client || failure || to.fullPath === from.fullPath) return;

  void (async () => {
    await nextTick();
    await new Promise((resolve) =>
      requestAnimationFrame(() => requestAnimationFrame(resolve)),
    );
    await nextTick();
    scrollToRouteDestination(to);
  })();
});
</script>

<template>
  <div class="site-shell">
    <a class="skip-link" href="#main-content">Skip to content</a>
    <header class="site-header">
      <NuxtLink class="brand" to="/" aria-label="Lime Skills home">
        <span class="brand-mark">[</span>lime skills<span class="brand-mark"
          >]</span
        >
      </NuxtLink>
      <nav class="site-nav" aria-label="Primary navigation">
        <NuxtLink to="/#skills">Index</NuxtLink>
        <NuxtLink to="/#about">About</NuxtLink>
        <a :href="repositoryUrl" target="_blank" rel="noopener noreferrer"
          >GitHub ↗</a
        >
      </nav>
    </header>
    <main id="main-content"><NuxtPage /></main>
    <footer class="site-footer">
      <p class="footer-note">
        Made for the messy middle between idea and shipped.
      </p>
      <div class="footer-links">
        <a :href="repositoryUrl" target="_blank" rel="noopener noreferrer"
          >repo / github ↗</a
        >
        <a
          href="https://lime.is-a.dev"
          target="_blank"
          rel="noopener noreferrer"
          >lime.is-a.dev ↗</a
        >
      </div>
      <span class="footer-stamp">© {{ new Date().getFullYear() }} / MIT</span>
    </footer>
  </div>
</template>
