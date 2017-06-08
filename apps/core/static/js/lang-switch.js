$(function () {
  const $langSwitch = $('#lang-switch')
  const $langActive = $langSwitch.find('.lang-switch__active')
  const $langList = $langSwitch.find('.lang-switch__list')

  $langActive.on('click', (e) => {
    $langList.toggleClass('lang-switch__list--active')
  })
})
