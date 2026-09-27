import { onBeforeUnmount, onMounted } from 'vue'

export function useScrollAnimations(rootRef) {
  let mediaQueryContext
  let disposed = false

  onMounted(async () => {
    if (!rootRef.value) return

    try {
      const [{ gsap }, { ScrollTrigger }] = await Promise.all([
        import('gsap'),
        import('gsap/ScrollTrigger')
      ])

      if (disposed || !rootRef.value) return

      gsap.registerPlugin(ScrollTrigger)
      mediaQueryContext = gsap.matchMedia()

      mediaQueryContext.add('(prefers-reduced-motion: no-preference)', () => {
        const select = gsap.utils.selector(rootRef.value)
        const revealItems = select('[data-reveal]')
        const cardGrid = select('.skill-grid')[0]
        const cards = select('.skill-card')
        const progressBar = select('[data-scroll-progress]')[0]

        revealItems.forEach((element) => {
          gsap.fromTo(element,
            { autoAlpha: 1, y: 14 },
            {
              immediateRender: false,
              autoAlpha: 1,
              y: 0,
              duration: 0.65,
              ease: 'power2.out',
              scrollTrigger: {
                trigger: element,
                start: 'top 90%',
                once: true
              }
            }
          )
        })

        if (cardGrid && cards.length) {
          const cardTimeline = gsap.timeline({
            defaults: { duration: 0.6, ease: 'power2.out' },
            scrollTrigger: { trigger: cardGrid, start: 'top 86%', once: true }
          })

          cardTimeline
            .addLabel('cards-enter', 0)
            .fromTo(cards,
              { autoAlpha: 0, y: 22 },
              { immediateRender: false, autoAlpha: 1, y: 0, stagger: 0.08 },
              'cards-enter'
            )
        }

        if (progressBar) {
          gsap.fromTo(progressBar,
            { scaleX: 0 },
            {
              scaleX: 1,
              ease: 'none',
              scrollTrigger: {
                trigger: document.body,
                start: 'top top',
                end: 'max',
                scrub: 0.35
              }
            }
          )
        }

        requestAnimationFrame(() => ScrollTrigger.refresh())
      }, rootRef.value)
    } catch {
      // Motion is an enhancement; content remains visible if GSAP cannot load.
    }
  })

  onBeforeUnmount(() => {
    disposed = true
    mediaQueryContext?.revert()
  })
}
