import {throttle} from './helpers'

$(function() {
  const $menu = $('#main-menu')
  const $menuContainer = $menu.find('.header__menu-list')
  const $window = $(window)
  const menuHeight = $menu.height()
  let prevScrollTop = $window.scrollTop()
  let menuIsVisible = true

  function scrollHandler() {
    let scrollTop = $window.scrollTop()

    if (scrollTop > prevScrollTop && scrollTop >= 100 && menuIsVisible) {
      $menuContainer.addClass('header__menu-list--invisible')
      menuIsVisible = false
    } else if (prevScrollTop > scrollTop && !menuIsVisible) {
      $menuContainer.removeClass('header__menu-list--invisible')
      menuIsVisible = true
    }
    prevScrollTop = scrollTop
  }

  $window.on('scroll', throttle(scrollHandler, 300, {trailing: true}))
})
