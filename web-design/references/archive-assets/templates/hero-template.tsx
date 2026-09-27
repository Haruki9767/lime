// Starting-point hero component for the "premium landing" pattern.
// Adapt copy, image/video source, nav links, and accent color per project.
// DO NOT introduce gradients — solid overlay + solid accent color only.

import Image from 'next/image'
import { MagnifyingGlass, InstagramLogo, XLogo, LinkedinLogo } from '@phosphor-icons/react'
// Install with: npm install @phosphor-icons/react
// Pick one weight (regular/light) project-wide; reserve `weight="fill"` for active states only.

type NavLink = { label: string; href: string }

interface HeroProps {
  brand: string
  navLinks: NavLink[]
  headline: string
  subhead?: string
  backgroundImageSrc?: string // use this OR backgroundVideoSrc, not both
  backgroundVideoSrc?: string
  eyebrowLabel?: string
  eyebrowDetail?: string
  eyebrowDescription?: string
  ctaLabel?: string
  ctaHref?: string
}

export default function Hero({
  brand,
  navLinks,
  headline,
  subhead,
  backgroundImageSrc,
  backgroundVideoSrc,
  eyebrowLabel,
  eyebrowDetail,
  eyebrowDescription,
  ctaLabel,
  ctaHref,
}: HeroProps) {
  return (
    <section className="relative mx-auto max-w-7xl overflow-hidden rounded-3xl shadow-2xl">
      {/* Background: image or looping muted video. Never a gradient. */}
      {backgroundVideoSrc ? (
        <video
          className="absolute inset-0 h-full w-full object-cover"
          src={backgroundVideoSrc}
          autoPlay
          loop
          muted
          playsInline
        />
      ) : backgroundImageSrc ? (
        <Image
          src={backgroundImageSrc}
          alt=""
          fill
          priority
          className="object-cover"
        />
      ) : null}

      {/* Solid dark scrim for text contrast — flat opacity, not a gradient */}
      <div className="absolute inset-0 bg-black/40" />

      <div className="relative z-10 flex min-h-[640px] flex-col justify-between p-8 md:p-12">
        {/* Top bar */}
        <div className="flex items-center justify-between">
          <span className="rounded-full bg-white/90 px-4 py-1.5 text-sm font-semibold text-black">
            {brand}
          </span>
          <nav className="hidden items-center gap-8 text-sm font-medium text-white md:flex">
            {navLinks.map((link) => (
              <a key={link.href} href={link.href} className="hover:text-white/70">
                {link.label}
              </a>
            ))}
            <button aria-label="Search" className="cursor-pointer hover:text-white/70">
              <MagnifyingGlass size={18} weight="regular" />
            </button>
          </nav>
        </div>

        {/* Headline block */}
        <div className="max-w-2xl">
          <h1 className="text-5xl font-extrabold leading-[0.95] tracking-tight text-white md:text-7xl">
            {headline}
          </h1>
          {subhead && (
            <p className="mt-3 text-lg font-light text-white/90 md:text-xl">
              {subhead}
            </p>
          )}
          {ctaLabel && ctaHref && (
            <a
              href={ctaHref}
              className="mt-6 inline-block rounded-md bg-white px-6 py-3 text-sm font-semibold text-black"
            >
              {ctaLabel}
            </a>
          )}
        </div>

        {/* Bottom eyebrow/caption block */}
        {eyebrowLabel && (
          <div className="flex items-end gap-4 text-white">
            <div>
              <p className="text-sm font-semibold">{eyebrowLabel}</p>
              {eyebrowDetail && (
                <p className="text-xs text-white/70">{eyebrowDetail}</p>
              )}
            </div>
            {eyebrowDescription && (
              <>
                <div className="h-10 w-px bg-white/40" />
                <p className="max-w-xs text-xs text-white/70">
                  {eyebrowDescription}
                </p>
              </>
            )}
          </div>
        )}

        {/* Optional social row — swap/remove per project */}
        <div className="flex justify-end gap-4 text-white">
          <a href="#" aria-label="Instagram" className="cursor-pointer hover:text-white/70">
            <InstagramLogo size={18} weight="regular" />
          </a>
          <a href="#" aria-label="X" className="cursor-pointer hover:text-white/70">
            <XLogo size={18} weight="regular" />
          </a>
          <a href="#" aria-label="LinkedIn" className="cursor-pointer hover:text-white/70">
            <LinkedinLogo size={18} weight="regular" />
          </a>
        </div>
      </div>
    </section>
  )
}
