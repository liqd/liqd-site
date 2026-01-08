/**
 * Simple test to verify login functionality
 */
import { test, expect } from '@playwright/test'
import { loginToAdmin } from './helpers.js'

test('should be able to login to admin', async ({ page }) => {
  // Try to login
  await loginToAdmin(page, 'admin', 'password')

  // Check if we're logged in by checking the URL
  const currentUrl = page.url()
  console.log('Current URL after login:', currentUrl)

  // Should be on admin dashboard or pages
  expect(currentUrl).toMatch(/\/admin\//)
  expect(currentUrl).not.toMatch(/\/login/)

  // Take a screenshot to verify
  await page.screenshot({ path: 'test-results/login-success.png', fullPage: true })

  // Check if we can see admin content (like "Pages" link or dashboard)
  // Try different selectors for Wagtail admin
  const adminContentSelectors = [
    'text=Pages',
    'text=Dashboard',
    '[href*="/admin/pages"]',
    'a[href*="pages"]',
    '.wagtail-userbar',
    '[class*="wagtail"]'
  ]

  for (const selector of adminContentSelectors) {
    const element = page.locator(selector).first()
    if (await element.count() > 0) {
      console.log(`Found admin content with selector: ${selector}`)
      break
    }
  }

  // If we're on /admin/ and not on /login/, we're logged in
  const isLoggedIn = currentUrl.includes('/admin/') && !currentUrl.includes('/login')
  expect(isLoggedIn).toBeTruthy()

  console.log('Login successful! Current URL:', currentUrl)
})
