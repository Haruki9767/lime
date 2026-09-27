import { nextTick, onBeforeUnmount, onMounted } from "vue";

export function useScrollAnimations(rootRef) {
  let mediaQueryContext;
  let refreshScrollTriggers = () => {};
  let disposed = false;

  onMounted(async () => {
    await nextTick();
    if (!rootRef.value) return;

    try {
      const [{ gsap }, { ScrollTrigger }] = await Promise.all([
        import("gsap"),
        import("gsap/ScrollTrigger"),
      ]);

      if (disposed || !rootRef.value) return;

      gsap.registerPlugin(ScrollTrigger);
      mediaQueryContext = gsap.matchMedia();
      refreshScrollTriggers = () => ScrollTrigger.refresh();

      mediaQueryContext.add(
        "(prefers-reduced-motion: no-preference)",
        () => {
          const select = gsap.utils.selector(rootRef.value);
          const introKicker = select("[data-intro-kicker]");
          const introLines = select("[data-intro-line]");
          const introCopy = select("[data-intro-copy]");
          const introItems = select("[data-intro-items]");
          const rail = select("[data-intro-rail]");
          const revealItems = select("[data-scroll-reveal]");
          const cardGrid = select(".skill-grid")[0];
          const cards = select(".skill-card");
          const progressBar = select("[data-scroll-progress]")[0];

          const intro = gsap.timeline({ defaults: { ease: "power3.out" } });
          if (introKicker.length) {
            intro.fromTo(
              introKicker,
              { autoAlpha: 0, y: 20, immediateRender: false },
              { autoAlpha: 1, y: 0, duration: 0.55 },
              0,
            );
          }
          if (introLines.length) {
            intro.fromTo(
              introLines,
              { yPercent: 125, rotateX: -10, immediateRender: false },
              { yPercent: 0, rotateX: 0, duration: 0.9, stagger: 0.14 },
              0.08,
            );
          }
          if (introCopy.length) {
            intro.fromTo(
              introCopy,
              { autoAlpha: 0, y: 26, immediateRender: false },
              { autoAlpha: 1, y: 0, duration: 0.62, stagger: 0.1 },
              0.28,
            );
          }
          if (introItems.length) {
            intro.fromTo(
              introItems,
              { autoAlpha: 0, y: 22, immediateRender: false },
              { autoAlpha: 1, y: 0, duration: 0.58, stagger: 0.1 },
              0.48,
            );
          }
          if (rail.length) {
            intro.fromTo(
              rail,
              { autoAlpha: 0, x: 48, immediateRender: false },
              { autoAlpha: 1, x: 0, duration: 0.8 },
              0.22,
            );
          }
          revealItems.forEach((element) => {
            const bounds = element.getBoundingClientRect();
            if (bounds.top < window.innerHeight * 0.82 && bounds.bottom > 0) {
              gsap.set(element, { autoAlpha: 1, x: 0, y: 0 });
              return;
            }

            const direction = element.dataset.scrollReveal;
            const fromX =
              direction === "left" ? -52 : direction === "right" ? 52 : 0;
            const fromY = direction === "up" ? 72 : 24;

            gsap.fromTo(
              element,
              { autoAlpha: 0.12, x: fromX, y: fromY, immediateRender: false },
              {
                autoAlpha: 1,
                x: 0,
                y: 0,
                ease: "none",
                scrollTrigger: {
                  trigger: element,
                  start: "top 92%",
                  end: "top 54%",
                  scrub: 0.7,
                  invalidateOnRefresh: true,
                },
              },
            );
          });

          if (cardGrid && cards.length) {
            const cardTimeline = gsap.timeline({
              scrollTrigger: {
                trigger: cardGrid,
                start: "top 92%",
                end: "top 48%",
                scrub: 0.9,
                invalidateOnRefresh: true,
              },
            });

            cardTimeline.fromTo(
              cards,
              {
                autoAlpha: 0,
                y: 92,
                rotation: (index) => (index % 2 ? 2.5 : -2.5),
                scale: 0.96,
                immediateRender: false,
              },
              {
                autoAlpha: 1,
                y: 0,
                rotation: 0,
                scale: 1,
                stagger: 0.16,
                ease: "power2.out",
              },
              0,
            );
          }

          if (progressBar) {
            gsap.fromTo(
              progressBar,
              { scaleX: 0, immediateRender: false },
              {
                scaleX: 1,
                ease: "none",
                scrollTrigger: {
                  trigger: document.body,
                  start: "top top",
                  end: "max",
                  scrub: 0.45,
                },
              },
            );
          }

          requestAnimationFrame(() => {
            if (!disposed) ScrollTrigger.refresh();
          });
          document.fonts?.ready?.then(() => {
            if (!disposed) ScrollTrigger.refresh();
          });
        },
        rootRef.value,
      );
    } catch (error) {
      if (import.meta.dev)
        console.warn("[lime] Scroll animations could not initialize:", error);
      // Motion is an enhancement; the Vue-rendered content stays available without GSAP.
    }
  });

  onBeforeUnmount(() => {
    disposed = true;
    refreshScrollTriggers = () => {};
    mediaQueryContext?.revert();
  });

  return {
    refresh: () => refreshScrollTriggers(),
  };
}
