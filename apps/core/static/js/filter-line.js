/* global $ */

$(function () {
  let $triggers = $('.filter-line__current')
  let $window = $(window)
  let windowWidth = $window.width()

  $triggers.on('click', function () {
    let $this = $(this)
    let $list = $this.next()

    if (windowWidth > 768) {
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
    } else {
      let $modal = buildModal($list)
      $modal.insertAfter($list)
    }
  })

  function buildModal ($list) {
    let $modal = $('<div class="filter-line__modal"></div>')
    let $close = $('<button class="filter-line__modal-close">&times;</button>')

    $modal.append($close)
    $modal.append($list.clone())

    $close.one('click', function () {
      $modal.remove()
    })

    return $modal
  }
})
