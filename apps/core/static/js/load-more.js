/* global $ */
$(function () {
  var count = 2
  var url = buildUrl()
  var numPages = $('.load-more').first().attr('data-page-total')
  $('.load-more').on('click', function (event) {
    event.preventDefault()
    loadProjects(count, url)
  })
  function loadProjects (pageNumber, url) {
    $.ajax({
      url: url + count,
      type: 'GET',
      success: function (html) {
        $('.item-list').append(html)
        count++
        if(count > numPages) {
          $('.load-more').hide()
        }
      }
    })
  }
  function buildUrl () {
    if (window.location.search === '') {
      return '?page='
    } else {
      return window.location.search + '&page='
    }
  }
})
