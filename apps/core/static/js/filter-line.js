/* global $ */

$(function () {
  let $triggers = $('.filter-line__current')
  let $window = $(window)

  $triggers.on('click', function () {
    let $this = $(this)
    let $list = $this.next()

    $list.addClass('filter-line__list--active')
    $this.addClass('filter-line__current--active')

    // make sure only one event is set
    $window.off('click.filter-hide')
    $window.on('click.filter-hide', function (e) {
      let $target = $(e.target)
      if (!$target.parents('.filter-line').length) {
        $list.removeClass('filter-line__list--active')
        $this.removeClass('filter-line__current--active')
        // remove event when not needed anymore
        $window.off('click.filter-hide')
      }
    })
  })
})
