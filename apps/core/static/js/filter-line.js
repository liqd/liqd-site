/* global $ */

$(function () {
  let $triggers = $('.filter-line__current')

  $triggers.on('click', function () {
    let $this = $(this)
    let $list = $this.next()

    $list.toggleClass('filter-line__list--active')
    $this.toggleClass('filter-line__current--active')
  })
})
