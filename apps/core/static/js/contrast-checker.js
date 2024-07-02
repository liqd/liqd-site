function luminance (r, g, b) {
  const a = [r, g, b].map(function (v) {
    v /= 255
    return v <= 0.03928
      ? v / 12.92
      : Math.pow((v + 0.055) / 1.055, 2.4)
  })
  return a[0] * 0.2126 + a[1] * 0.7152 + a[2] * 0.0722
}

function contrast (rgb1, rgb2) {
  const lum1 = luminance(rgb1[0], rgb1[1], rgb1[2])
  const lum2 = luminance(rgb2[0], rgb2[1], rgb2[2])
  const brightest = Math.max(lum1, lum2)
  const darkest = Math.min(lum1, lum2)
  return (brightest + 0.05) / (darkest + 0.05)
}

function hexToRgb (value) {
  // converts hex string to array of integers, representing r,g and b values.
  // example: [54, 89, 122]
  const val = value.replace('#', '')
  const rgbVals = []
  for (let i = 0; i < val.length;) {
    const step = Math.floor(val.length / 3)
    rgbVals.push(parseInt(val.slice(i, i + step), 16))
    i = i + step
  }
  return rgbVals
}

function getDarker (color1, color2) {
  // compares two colors and returns the darker of both
  const rgb1 = hexToRgb(color1)
  const rgb2 = hexToRgb(color2)
  const sumRgb1 = rgb1.reduce((a, b) => a + b)
  const sumRgb2 = rgb2.reduce((a, b) => a + b)
  return sumRgb1 < sumRgb2
    ? rgb1
    : rgb2
}

// finding all elements which contrast should be checked
const elementsToBeChecked = document.querySelectorAll('[data-contrast-checking]')
const brighterFgHex = '#fbfbfb'
const darkerFgHex = '#060606'

if (elementsToBeChecked.length > 0) {
  const bgColors = JSON.parse(elementsToBeChecked[0].getAttribute('data-contrast-checking'))

  if (bgColors.every(i => i !== '')) {
    // compare darker colors (bg colors) from backend
    const darkerBgColor = getDarker(bgColors[0], bgColors[1])

    // converts the two textcolor options to rgb values (black and white)
    const brighterFgColor = hexToRgb(brighterFgHex)
    const darkerFgColor = hexToRgb(darkerFgHex)

    // calculate contrast. Results are floating numbers.
    const contrastRatioBright = contrast(brighterFgColor, darkerBgColor)
    const contrastRatioDark = contrast(darkerFgColor, darkerBgColor)

    // compare contrast ratios. Higher value wins.
    const textcolor = contrastRatioBright > contrastRatioDark
      ? brighterFgHex
      : darkerFgHex

    // set inline style text color
    elementsToBeChecked.forEach(element => { element.style.color = textcolor })
  }
}
