/* global $ */

import {isHome, throttle} from "./helpers";
import {initDistort} from "liquid-logo";

$(function () {
  const $menu = $('#main-menu')
  const $menuContainer = $menu.find('.header__menu-list')
  const $introScreen = $('.intro-screen')
  const $window = $(window)
  const webGL = initDistort('header-canvas', {interactive: false, width: 60, height: 50})
  const $brandLabel = $('.header__brand-label')
  let prevScrollTop = $window.scrollTop()
  let windowHeight = $window.height()
  let menuIsVisible = true
  let labelIsVisible = true

  function lerp (start, end, amt) {
    return (1 - amt) * start + amt * end
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

    if (isHome()) {
      const opacityGL = lerp(0, 1, scrollTop / windowHeight)
      const opacityLabel = lerp(1, 0, scrollTop / windowHeight)
      webGL.setAlpha(opacityGL)
      $brandLabel.css({'opacity': opacityLabel})
      console.log(opacityLabel);
      if (labelIsVisible && opacityLabel <= 0) {
        labelIsVisible = false
        $brandLabel.css({'display': 'none'})
      } else if (!labelIsVisible && opacityLabel > 0) {
        $brandLabel.css({'display': 'inline-block'})
        labelIsVisible = true
      }
    }

    if ($introScreen.length && scrollTop >= windowHeight / 100 * 80) {
      $menu.addClass('header--past-intro')
    } else if ($introScreen.length && scrollTop < windowHeight / 100 * 80) {
      $menu.removeClass('header--past-intro')
    }

    prevScrollTop = scrollTop
  }

  $window.on('scroll', throttle(scrollHandler, 300, {trailing: true}))
})
