/* global $ */

$(function () {
  const $menu = $('#main-menu')
  const $menuContainer = $menu.find('.header__menu-list')
  const $introScreen = $('.intro-screen')
  const $window = $(window)
  let prevScrollTop = $window.scrollTop()
  const windowHeight = $window.height()
  const windowWidth = $window.width()
  let menuIsVisible = true

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

    if ($introScreen.length && scrollTop >= windowHeight / 100 * 80) {
      $menu.addClass('header--past-intro')
    } else if ($introScreen.length && scrollTop < windowHeight / 100 * 80) {
      $menu.removeClass('header--past-intro')
    }

    prevScrollTop = scrollTop
  }

  $window.on('scroll', scrollHandler)
})
