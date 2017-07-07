/* globals $ */
import {isHome} from "./helpers";
import {initDistort} from "liquid-logo";

$(function () {
  if (!isHome()) {
    return false
  }

  const $window = $(window)
  const windowHeight = $window.height()
  const webGL = initDistort('canvas-home', {
    height: windowHeight * 0.8
  })

  let scrollPos

  function lerp (start, end, amt) {
    return (1 - amt) * start + amt * end
  }

  $window.on('scroll', function () {
    scrollPos = $window.scrollTop()
    const opacity = lerp(1, 0, scrollPos / (windowHeight * 0.8))
    webGL.setAlpha(opacity)
  })
})
