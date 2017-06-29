import {throttle} from './helpers'

$(function () {
  const $canvas = $('.home-logo__canvas')
  const $window = $(window)
  const windowHeight = $window.height()

  let scrollPos

  function lerp (start, end, amt){
    return (1-amt)*start+amt*end
  }

  $window.on('scroll', throttle(function () {
    scrollPos = $window.scrollTop()
  }, 100))

  function render () {
    const opacity = lerp(1, 0, scrollPos / windowHeight)
    $canvas[0].style.opacity = opacity

    requestAnimationFrame(render)
  }

  requestAnimationFrame(render)
})
