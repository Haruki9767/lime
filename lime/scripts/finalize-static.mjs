import { readFile, rm, writeFile } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'

const prerenderedNotFound = fileURLToPath(new URL('../.output/public/404/index.html', import.meta.url))
const pagesNotFound = fileURLToPath(new URL('../.output/public/404.html', import.meta.url))
const unusedSpaFallback = fileURLToPath(new URL('../.output/public/200.html', import.meta.url))

const vueRenderedNotFound = await readFile(prerenderedNotFound, 'utf8')
const staticNotFound = vueRenderedNotFound
  .replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi, '')
  .replace(/<link\b(?=[^>]*\brel=["']modulepreload["'])[^>]*>/gi, '')

if (!staticNotFound.includes('That page went') || /<script\b/i.test(staticNotFound)) {
  throw new Error('The prerendered Vue 404 did not produce a safe no-JavaScript GitHub Pages fallback.')
}

await writeFile(pagesNotFound, staticNotFound)
await rm(unusedSpaFallback, { force: true })
console.log('Prepared the script-free GitHub Pages 404 from prerendered Vue markup and removed the unused 200.html shell.')
