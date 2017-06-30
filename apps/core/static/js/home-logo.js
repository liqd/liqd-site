import {isHome, throttle} from "./helpers";
import {initDistort} from "liquid-logo";

$(function () {
  if (!isHome()) {
    return false
  }

  const $window = $(window)
  const windowHeight = $window.height()
  const webGL = initDistort('canvas-home')

  let scrollPos

  function lerp (start, end, amt){
    return (1-amt)*start+amt*end
  }

  $window.on('scroll', throttle(function () {
    scrollPos = $window.scrollTop()
    const opacity = lerp(1, 0, scrollPos / windowHeight)
    webGL.setAlpha(opacity)
  }, 100, {trailing: true}))
})
