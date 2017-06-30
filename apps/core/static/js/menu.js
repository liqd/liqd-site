/* global $ */

import {throttle} from "./helpers";
import {initDistort} from "liquid-logo";

$(function () {
  const $menu = $('#main-menu')
  const $menuContainer = $menu.find('.header__menu-list')
  const $window = $(window)
  const webGL = initDistort('header-canvas', {interactive: false, width: 60, height: 50})
  let prevScrollTop = $window.scrollTop()
  let windowHeight = $window.height()
  let menuIsVisible = true

  function lerp (start, end, amt){
    return (1-amt)*start+amt*end
  }

  function scrollHandler () {
    let scrollTop = $window.scrollTop()

    if (scrollTop > prevScrollTop && scrollTop >= 100 && menuIsVisible) {
      $menuContainer.addClass('header__menu-list--invisible')
      menuIsVisible = false
    } else if (prevScrollTop > scrollTop && !menuIsVisible) {
      $menuContainer.removeClass('header__menu-list--invisible')
      menuIsVisible = true
    }
    prevScrollTop = scrollTop
    const opacity = lerp(0, 1, scrollTop / windowHeight)
    webGL.setAlpha(opacity)
  }

  $window.on('scroll', throttle(scrollHandler, 300, {trailing: true}))
})
