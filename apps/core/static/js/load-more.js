/* global $ */
$(function () {
  var count = 2
  var url = buildUrl()
  $('.load-more').on('click', function (event) {
    event.preventDefault()
    loadProjects(count, url)
    count++
  })
  function loadProjects (pageNumber, url) {
    $.ajax({
      url: url + count,
      type: 'GET',
      success: function (html) {
        $('.item-list').append(html)
        $.ajax({
          url: url + (count + 1),
          type: 'GET',
          error: function (xhr, status, errorThrown) {
            if (xhr.status === 404) {
              $('.load-more').hide()
            }
          }
        })
        return false
      }
    })
    return false
  }
  function buildUrl () {
    if (window.location.search === '') {
      return '?page='
    } else {
      return window.location.search + '&page='
    }
  }
})
