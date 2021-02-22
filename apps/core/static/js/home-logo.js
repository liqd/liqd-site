/* globals $ */
import { isHome } from './helpers'
import { initDistort } from 'liquid-logo'

$(function () {
  if (!isHome()) {
    return false
  }

  const $window = $(window)
  const windowHeight = $window.height()
  const $header = $('#navbar-main')
  const webGL = initDistort('canvas-home', {
    height: windowHeight
  })

  let scrollPos = $window.scrollTop()

  if (scrollPos <= 30) {
    setTimeout(function () {
      $header.css('opacity', 1)
    }, 1500)
    setTimeout(function () {
      $('.home-logo__lead').css('opacity', 1)
    }, 2500)
  } else {
    $header.css('opacity', 1)
    $('.home-logo__lead').css('opacity', 1)
  }

  function lerp (start, end, amt) {
    return (1 - amt) * start + amt * end
  }

  $window.on('scroll', function () {
    scrollPos = $window.scrollTop()
    const opacity = lerp(1, 0, scrollPos / windowHeight)
    webGL.setAlpha(opacity)
  })
})
