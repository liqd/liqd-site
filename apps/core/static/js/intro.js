/* globals $ */
import { throttle } from './helpers'

// Homepage entry animation: a video inside a shape that morphs while scrolling.
// Circle -> rounded square -> fullscreen. Once the shape is fullscreen the page
// keeps scrolling normally (the pinned section scrolls away). The text lives in
// its own sections above and below the pinned video, so it is never covered.
//
// This is a framework-free (vanilla JS) implementation of the scroll-driven
// mask, so no extra animation dependency is required.

// Speed of the typewriter effect in ms per letter. Lower = faster.
const TYPE_SPEED = 40

// Split the title into per-letter spans and type them out one after another
// with a blinking cursor. Words are wrapped in their own span so line wrapping
// stays intact.
function revealTitle (head, reduceMotion) {
  if (!head) {
    return
  }

  const title = head.querySelector('h1')
  head.classList.add('is-revealed')

  if (!title || reduceMotion) {
    return
  }

  const text = title.textContent
  // Keep the full title as the accessible name so screen readers announce it
  // even while the letters are still visually hidden by the typewriter effect.
  title.setAttribute('aria-label', text.trim())
  title.textContent = ''
  const letters = []

  text.split(/(\s+)/).forEach((token) => {
    if (!token) {
      return
    }
    if (/^\s+$/.test(token)) {
      title.appendChild(document.createTextNode(' '))
      return
    }

    const word = document.createElement('span')
    word.className = 'intro__letter-word'

    token.split('').forEach((char) => {
      const letter = document.createElement('span')
      letter.className = 'intro__letter'
      letter.textContent = char
      word.appendChild(letter)
      letters.push(letter)
    })

    title.appendChild(word)
  })

  if (!letters.length) {
    return
  }

  const cursor = document.createElement('span')
  cursor.className = 'intro__cursor'
  cursor.setAttribute('aria-hidden', 'true')
  title.insertBefore(cursor, title.firstChild)

  letters.forEach((letter, i) => {
    window.setTimeout(() => {
      letter.classList.add('is-typed')
      letter.after(cursor)
    }, TYPE_SPEED * (i + 1))
  })
}

export function initIntro () {
  const intro = document.querySelector('.intro')
  if (!intro) {
    return
  }

  const shape = intro.querySelector('.intro__shape')
  const sticky = intro.querySelector('.intro__sticky')
  const head = intro.querySelector('.intro__head')
  const video = intro.querySelector('.intro__video')
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches

  revealTitle(head, reduceMotion)

  // Autoplay is required for the effect; set muted explicitly and retry on
  // canplay because some browsers block autoplay until the media is ready.
  if (video) {
    video.muted = true
    const play = () => {
      const promise = video.play()
      if (promise && typeof promise.catch === 'function') {
        promise.catch(() => {})
      }
    }
    play()
    video.addEventListener('canplay', play, { once: true })
  }

  // Let the navigation fade in after the intro has settled.
  const header = document.getElementById('navbar-main')
  if (header) {
    window.setTimeout(() => {
      header.style.opacity = 1
    }, 870)
  }

  if (!shape || !sticky || reduceMotion) {
    intro.classList.add('intro--reduced')
    return
  }

  const MOBILE_BREAKPOINT = 768
  // start/mid are factors of the smaller viewport side. The max caps the shape
  // on desktop only, where the viewport can get large; mobile is small enough.
  const SIZE = {
    mobile: { start: 0.64, mid: 0.86, maxStart: Infinity, maxMid: Infinity },
    desktop: { start: 0.46, mid: 0.68, maxStart: 620, maxMid: 760 }
  }
  const MORPH_SPLIT = 0.5 // circle -> rounded square, then -> fullscreen

  let viewportWidth = 0
  let viewportHeight = 0
  let sectionTop = 0
  let scrollRange = 1
  let startSize = 0
  let midSize = 0

  const clamp = (value, min, max) => Math.min(Math.max(value, min), max)
  const lerp = (start, end, amount) => start + (end - start) * amount

  function measure () {
    // Use the rendered sticky box instead of the viewport so the video fills it
    // exactly (avoids 100vh vs. window.innerHeight mismatches, e.g. mobile
    // browser bars) and the morph ends exactly when the section unpins.
    viewportWidth = sticky.clientWidth
    viewportHeight = sticky.clientHeight

    const rect = intro.getBoundingClientRect()
    sectionTop = rect.top + window.scrollY
    scrollRange = Math.max(intro.offsetHeight - sticky.offsetHeight, 1)

    const base = Math.min(viewportWidth, viewportHeight)
    const size = SIZE[viewportWidth < MOBILE_BREAKPOINT ? 'mobile' : 'desktop']

    startSize = Math.min(base * size.start, size.maxStart)
    midSize = Math.min(base * size.mid, size.maxMid)
  }

  function render () {
    const scrolled = window.scrollY - sectionTop
    const progress = clamp(scrolled / scrollRange, 0, 1)

    let width
    let height
    let radius

    if (progress <= MORPH_SPLIT) {
      const t = progress / MORPH_SPLIT
      width = lerp(startSize, midSize, t)
      height = width
      radius = lerp(50, 18, t)
    } else {
      const t = (progress - MORPH_SPLIT) / (1 - MORPH_SPLIT)
      width = lerp(midSize, viewportWidth, t)
      height = lerp(midSize, viewportHeight, t)
      radius = lerp(18, 0, t)
    }

    // The video starts at the bottom edge (half visible) and moves up to the
    // centre while it grows to fullscreen.
    const shapeCenterY = lerp(viewportHeight, viewportHeight / 2, progress)

    shape.style.width = `${width}px`
    shape.style.height = `${height}px`
    shape.style.top = `${shapeCenterY}px`
    shape.style.borderRadius = `${radius}%`

    // The title scrolls up with the page and is fully out of the viewport by
    // the time the video reaches fullscreen (its bottom edge reaches the top).
    if (head) {
      const titleShift = (head.offsetTop + head.offsetHeight) * progress
      head.style.transform = `translate(-50%, calc(-50% - ${titleShift}px))`
    }
  }

  function onResize () {
    measure()
    render()
  }

  measure()
  render()

  window.addEventListener('scroll', throttle(render, 16), { passive: true })
  window.addEventListener('resize', onResize)
  window.addEventListener('load', onResize)

  if (window.ResizeObserver) {
    const observer = new ResizeObserver(onResize)
    observer.observe(intro)
    observer.observe(sticky)
  }
}

$(initIntro)
