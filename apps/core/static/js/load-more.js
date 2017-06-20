/* global $ */
$(function () {
  var count = 2
  $('.load-more').on('click', function (event) {
    event.preventDefault()
    loadProjects(count)
    count++
  })
  function loadProjects (pageNumber) {
    $.ajax({
      url: '?page=' + count,
      type: 'GET',
      success: function (html) {
        $('.project-list').append(html)
        $.ajax({
          url: '?page=' + (count + 1),
          type: 'GET',
          error: function (xhr, status, errorThrown) {
            if (xhr.status === '404') {
              $('.load-more').hide()
            }
          }
        })
      }
    })
    return false
  }
})
