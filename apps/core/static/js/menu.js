/* global $ */

import { isHome } from './helpers'
import { initDistort } from 'liquid-logo'

$(function () {
  const $menu = $('#main-menu')
  const $menuContainer = $menu.find('.header__menu-list')
  const $introScreen = $('.intro-screen')
  const $window = $(window)
  const webGL = initDistort('header-canvas', { interactive: false, width: 120, height: 100 })
  const $brandLabel = $('.header__brand-label')
  let prevScrollTop = $window.scrollTop()
  const windowHeight = $window.height()
  const windowWidth = $window.width()
  let menuIsVisible = true
  let labelIsVisible = true

  function lerp (start, end, amt) {
    return (1 - amt) * start + amt * end
  }

  function scrollHandler () {
    const scrollTop = $window.scrollTop()

    if (windowWidth > 576) {
      if (scrollTop > prevScrollTop && scrollTop >= 100 && menuIsVisible) {
        $menuContainer.addClass('header__menu-list--invisible')
        menuIsVisible = false
      } else if (prevScrollTop > scrollTop && !menuIsVisible) {
        $menuContainer.removeClass('header__menu-list--invisible')
        menuIsVisible = true
      }
    }

    if (isHome()) {
      const opacityGL = lerp(0, 1, scrollTop / windowHeight)
      webGL.setAlpha(opacityGL)
      if (labelIsVisible && scrollTop > 20) {
        labelIsVisible = false
        $brandLabel.css({ display: 'none' })
      } else if (!labelIsVisible && scrollTop <= 20) {
        $brandLabel.css({ display: 'inline-block' })
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

  $window.on('scroll', scrollHandler)
})
