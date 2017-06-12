/* global $ */

$(function () {
  const $langSwitch = $('#lang-switch')
  const $langActive = $langSwitch.find('.lang-switch__active')
  const $langList = $langSwitch.find('.lang-switch__list')
  let isOpen = false

  $langActive.on('click', (e) => {
    if (!isOpen) {
      $langList.css({'display': 'block'})
      // trigger layout so transition works initially
      $langList.css('opacity')
      $langList.addClass('lang-switch__list--active')
    } else {
      $langList.removeClass('lang-switch__list--active')
      $langList.one('transitionEnd', () => $langList.removeAttr('style'))
    }
    // toggle variable
    isOpen = !isOpen
  })
})
