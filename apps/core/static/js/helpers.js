/* globals $ */
// taken from underscore, http://underscorejs.org/docs/underscore.html
function _now () {
  return Date.now || function () {
    return new Date().getTime()
  }
}

const _isHome = $('body').hasClass('homepage')
export function isHome () {
  return _isHome
}

export function throttle (func, wait, options) {
  let context, args, result
  let timeout = null
  let previous = 0
  if (!options) options = {}
  const later = function () {
    previous = options.leading === false ? 0 : _now()
    timeout = null
    result = func.apply(context, args)
    if (!timeout) context = args = null
  }
  return function () {
    const now = _now()
    if (!previous && options.leading === false) previous = now
    const remaining = wait - (now - previous)
    context = this
    args = arguments
    if (remaining <= 0 || remaining > wait) {
      if (timeout) {
        clearTimeout(timeout)
        timeout = null
      }
      previous = now
      result = func.apply(context, args)
      if (!timeout) context = args = null
    } else if (!timeout && options.trailing !== false) {
      timeout = setTimeout(later, remaining)
    }
    return result
  }
}

export function debounce (func, wait, immediate) {
  let timeout, args, context, timestamp, result

  const later = function () {
    const last = _now() - timestamp

    if (last < wait && last >= 0) {
      timeout = setTimeout(later, wait - last)
    } else {
      timeout = null
      if (!immediate) {
        result = func.apply(context, args)
        if (!timeout) context = args = null
      }
    }
  }

  return function () {
    context = this
    args = arguments
    timestamp = _now()
    const callNow = immediate && !timeout
    if (!timeout) timeout = setTimeout(later, wait)
    if (callNow) {
      result = func.apply(context, args)
      context = args = null
    }

    return result
  }
}
