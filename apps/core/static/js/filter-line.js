/* global $ */

$(function () {
  const $triggers = $('.filter-line__current')
  const $window = $(window)
  const windowWidth = $window.width()

  $triggers.on('click', function () {
    const $this = $(this)
    const $list = $this.next()

    if (windowWidth > 768) {
      $list.addClass('filter-line__list--active')
      $this.addClass('filter-line__current--active')

      // make sure only one event is set
      $window.off('click.filter-hide')
      $window.on('click.filter-hide', function (e) {
        const $target = $(e.target)
        if (!$target.parents('.filter-line').length) {
          $list.removeClass('filter-line__list--active')
          $this.removeClass('filter-line__current--active')
          // remove event when not needed anymore
          $window.off('click.filter-hide')
        }
      })
    } else {
      const $modal = buildModal($list)
      $modal.insertAfter($list)
    }
  })

  function buildModal ($list) {
    const $modal = $('<div class="filter-line__modal"></div>')
    const $close = $('<button class="filter-line__modal-close h4">Schließen</button>')

    $modal.append($close)
    $modal.append($list.clone())

    $close.one('click', function () {
      $modal.remove()
    })

    return $modal
  }
})
