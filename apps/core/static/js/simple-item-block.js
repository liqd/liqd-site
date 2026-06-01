/* global $ */

/**
 * Simple Item block: selection toggles title typography (aria-pressed).
 */
$(function () {
  $('[data-simple-item-block]').each(function () {
    const $block = $(this)
    const $buttons = $block.find('[data-simple-item-button]')

    if (!$buttons.length) {
      return
    }

    const selectButton = ($button) => {
      $buttons.each(function () {
        const $current = $(this)
        const isSelected = $current.is($button)
        $current
          .attr('aria-pressed', isSelected ? 'true' : 'false')
          .toggleClass('simple-item-block__item--selected', isSelected)
      })
    }

    $buttons.on('click', function () {
      selectButton($(this))
    })

    $buttons.on('keydown', function (event) {
      const $current = $(this)
      const index = $buttons.index($current)
      let nextIndex = null

      switch (event.key) {
      case 'ArrowDown':
      case 'ArrowRight':
        nextIndex = (index + 1) % $buttons.length
        break
      case 'ArrowUp':
      case 'ArrowLeft':
        nextIndex = (index - 1 + $buttons.length) % $buttons.length
        break
      case 'Home':
        nextIndex = 0
        break
      case 'End':
        nextIndex = $buttons.length - 1
        break
      default:
        return
      }

      event.preventDefault()
      const $next = $buttons.eq(nextIndex)
      selectButton($next)
      $next.focus()
    })
  })
})
