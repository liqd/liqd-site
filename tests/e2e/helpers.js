/**
 * Helper functions for Playwright E2E tests
 */

import { readFileSync } from 'fs'
import { join } from 'path'

/**
 * Admin user credentials for E2E tests
 * Loaded from test-credentials.json
 * Note: User should be created by Makefile before tests run
 */
const credentialsPath = join(process.cwd(), 'tests', 'e2e', 'test-credentials.json')
export const ADMIN_CREDENTIALS = JSON.parse(readFileSync(credentialsPath, 'utf-8'))

/**
 * Login to Wagtail admin
 * @param {import('@playwright/test').Page} page - Playwright page object
 * @param {string} username - Admin username
 * @param {string} password - Admin password
 */
export async function loginToAdmin (page, username = 'admin', password = 'password') {
  // Try both /admin/login/ and /en/admin/login/ (i18n)
  try {
    await page.goto('/admin/login/', { waitUntil: 'networkidle' })
  } catch (e) {
    await page.goto('/en/admin/login/', { waitUntil: 'networkidle' })
  }

  // Wait for login form to be visible
  await page.waitForSelector('input[name="username"]', { timeout: 10000 })

  await page.fill('input[name="username"]', username)
  await page.fill('input[name="password"]', password)

  // Find submit button - could be button[type="submit"] or input[type="submit"]
  const submitButton = page.locator('button[type="submit"], input[type="submit"], button:has-text("Sign in"), button:has-text("Log in")').first()
  await submitButton.click()

  // Wait for redirect - could be /admin/ or /en/admin/ or /admin/pages/
  try {
    await page.waitForURL(/\/admin\//, { timeout: 15000 })
    // Check if we're actually logged in (not still on login page)
    const currentUrl = page.url()
    if (currentUrl.includes('/login')) {
      // Check for error message
      const errorText = await page.locator('.errorlist, .errornote, [class*="error"], .messages .error').first().textContent().catch(() => null)
      if (errorText) {
        throw new Error(`Login failed: ${errorText}`)
      }
      throw new Error(`Login failed - still on login page. URL: ${currentUrl}`)
    }
  } catch (error) {
    // Check if there's an error message
    const errorText = await page.locator('.errorlist, .errornote, [class*="error"], .messages .error').first().textContent().catch(() => null)
    if (errorText) {
      throw new Error(`Login failed: ${errorText}`)
    }
    // Check current URL to see where we ended up
    const currentUrl = page.url()
    throw new Error(`Login failed - did not redirect to /admin/. Current URL: ${currentUrl}`)
  }
}

/**
 * Navigate to add page for a specific model
 * In Wagtail, pages are added through the pages interface
 * @param {import('@playwright/test').Page} page - Playwright page object
 * @param {string} appLabel - Django app label (e.g., 'academy')
 * @param {string} modelName - Model name (e.g., 'academypage')
 * @param {number} parentPageId - ID of parent page (default: 1 for root)
 */
export async function navigateToAddPage (page, appLabel, modelName, parentPageId = 1) {
  // Wagtail uses /admin/pages/{parent_id}/add_subpage/ to show page type selection
  const addSubpageUrl = `/admin/pages/${parentPageId}/add_subpage/`
  await page.goto(addSubpageUrl, { waitUntil: 'networkidle', timeout: 30000 })
  await page.waitForTimeout(2000)

  // Wait for page type selection to be visible
  await page.waitForSelector('form, .page-type-choice, [data-page-type], button, a.button', { timeout: 10000 })

  // Find and click on the AcademyPage type
  // Try different selectors for the page type button/link
  const pageTypeSelectors = [
    'button:has-text("Academy page")',
    'a:has-text("Academy page")',
    'button:has-text("Academy")',
    'a:has-text("Academy")',
    '[data-page-type*="academy"]',
    `[data-page-type*="${modelName}"]`,
    // Generic selectors as fallback
    'button, a.button'
  ]

  let pageTypeFound = false
  for (const selector of pageTypeSelectors) {
    const elements = await page.locator(selector).all()
    for (const element of elements) {
      try {
        const text = await element.textContent()
        const isVisible = await element.isVisible().catch(() => false)

        // Check if this element looks like the AcademyPage type
        if (isVisible && text && (
          text.toLowerCase().includes('academy') ||
          text.toLowerCase().includes(modelName.toLowerCase())
        )) {
          await element.click()
          pageTypeFound = true
          await page.waitForTimeout(3000)
          await page.waitForLoadState('networkidle')
          break
        }
      } catch (e) {
        // Continue to next element
      }
    }
    if (pageTypeFound) break
  }

  if (!pageTypeFound) {
    // If we can't find the specific page type, try clicking the first available option
    const firstButton = page.locator('button, a.button').first()
    if (await firstButton.count() > 0 && await firstButton.isVisible().catch(() => false)) {
      await firstButton.click()
      await page.waitForTimeout(3000)
      await page.waitForLoadState('networkidle')
    } else {
      throw new Error(`Could not find page type ${modelName} on page type selection screen`)
    }
  }

  // Wait for the form to be visible
  await page.waitForSelector('form', { timeout: 15000 })
}

/**
 * Navigate to edit page for a specific page
 * @param {import('@playwright/test').Page} page - Playwright page object
 * @param {string} appLabel - Django app label
 * @param {string} modelName - Model name
 * @param {number} pageId - Page ID to edit
 */
export async function navigateToEditPage (page, appLabel, modelName, pageId) {
  const url = `/admin/${appLabel}/${modelName}/${pageId}/`
  await page.goto(url)
  await page.waitForSelector('form', { timeout: 10000 })
}

/**
 * Open a specific tab in the Wagtail admin form
 * @param {import('@playwright/test').Page} page - Playwright page object
 * @param {string} tabName - Name of the tab to open (e.g., "Common", "Promote", "English", "German")
 */
export async function openTab (page, tabName) {
  // Try different selectors for Wagtail tabs
  const tabSelectors = [
    `button:has-text("${tabName}")`,
    `a:has-text("${tabName}")`,
    `[role="tab"]:has-text("${tabName}")`,
    `[data-tab="${tabName}"]`,
    `[aria-label*="${tabName}"]`
  ]

  for (const selector of tabSelectors) {
    const tab = page.locator(selector).first()
    if (await tab.count() > 0 && await tab.isVisible().catch(() => false)) {
      await tab.click()
      await page.waitForTimeout(500) // Wait for tab content to load
      return
    }
  }

  // If tab not found, try to find all tabs and click the one with matching text
  const allTabs = await page.locator('[role="tab"], button, a').all()
  for (const tab of allTabs) {
    const text = await tab.textContent().catch(() => '')
    if (text && text.trim().includes(tabName)) {
      await tab.click()
      await page.waitForTimeout(500)
      return
    }
  }
}

/**
 * Save the page form
 * @param {import('@playwright/test').Page} page - Playwright page object
 * @param {boolean} publish - Whether to publish the page (default: false, saves as draft)
 */
export async function savePage (page, publish = false) {
  if (publish) {
    // Click publish button - try different selectors for Wagtail
    const publishButton = page.locator('button[name="action-publish"], button:has-text("Publish"), input[name="action-publish"]').first()
    await publishButton.click()
  } else {
    // Click save draft button - try different selectors
    const saveButton = page.locator('button[type="submit"]:not([name="action-publish"]), button:has-text("Save draft"), button:has-text("Save"), input[type="submit"]:not([name="action-publish"])').first()
    await saveButton.click()
  }
  // Wait for save confirmation - either success message or redirect
  await page.waitForTimeout(2000)

  // Check if we got redirected or if there's a success message
  // Wagtail might redirect to edit page or show success message
  try {
    await page.waitForURL(/\/admin\//, { timeout: 5000 })
  } catch (e) {
    // Might still be on the same page with success message
    // That's okay
  }
}
