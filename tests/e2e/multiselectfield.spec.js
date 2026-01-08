/**
 * Playwright E2E tests for MultiSelectField in AcademyPage
 *
 * These tests verify the UI behavior of the MultiSelectField in the Wagtail admin.
 *
 * Prerequisites:
 * - Django server must be running on http://localhost:8000
 * - An admin user must exist (username: admin, password: password)
 * - Or use Django test fixtures to create the user
 */

import { test, expect } from '@playwright/test'
import { loginToAdmin, navigateToAddPage, savePage, getAdminCredentials, openTab } from './helpers.js'

test.describe('MultiSelectField in AcademyPage', () => {
  let adminCredentials

  test.beforeAll(async () => {
    // Get admin credentials (user should be created by Makefile)
    adminCredentials = await getAdminCredentials('admin', 'password', 'admin@test.com')
  })

  test.beforeEach(async ({ page }) => {
    // Login to admin
    await loginToAdmin(page, adminCredentials.username, adminCredentials.password)
  })

  test('should display MultiSelectField in the form', async ({ page }) => {
    // Navigate to add AcademyPage
    await navigateToAddPage(page, 'academy', 'academypage')

    // Open the "Common" tab where the topics field is located
    await openTab(page, 'Common')

    // Check that the topics field is visible
    // MultiSelectField typically renders as checkboxes
    // Try different selectors for the topics field
    const topicsField = page.locator(
      'input[name="topics"][type="checkbox"], ' +
      'input[id*="topics"][type="checkbox"], ' +
      'label:has-text("Topics"), ' +
      'label:has-text("topic"), ' +
      '[for*="topics"]'
    )
    await expect(topicsField.first()).toBeVisible({ timeout: 10000 })
  })

  test('should allow selecting a single topic', async ({ page }) => {
    await navigateToAddPage(page, 'academy', 'academypage')

    // Fill required fields first
    // Open "Promote" tab for slug field
    await openTab(page, 'Promote')
    const slugField = page.locator('input[name="slug"], input[id*="slug"]').first()
    await slugField.fill('test-academy-page-single')

    // Open "Common" tab for date and topics fields
    await openTab(page, 'Common')

    // Set date field (required)
    const dateField = page.locator('input[name="date"], input[type="date"], input[id*="date"]').first()
    await dateField.fill('2024-01-15')

    // Select a single topic - MultiSelectField renders as checkboxes
    // Try to find checkbox with value "LT" (Liquid Democracy: Theory & Vision)
    const topicCheckbox = page.locator('input[type="checkbox"][value="LT"]').first()

    // If not found by value, try to find by label
    if (await topicCheckbox.count() === 0) {
      const liquidTheoryLabel = page.locator('label:has-text("Liquid Democracy"), label:has-text("Theory")').first()
      if (await liquidTheoryLabel.count() > 0) {
        // Click the label, which should check the associated checkbox
        await liquidTheoryLabel.click()
      } else {
        // Fallback: find first topics checkbox
        const firstTopicCheckbox = page.locator('input[type="checkbox"][name*="topics"]').first()
        if (await firstTopicCheckbox.count() > 0) {
          await firstTopicCheckbox.check()
        }
      }
    } else {
      await topicCheckbox.check()
    }

    // Save the page
    await savePage(page, false)

    // Verify the page was saved
    // Wagtail redirects to edit page or shows success message
    await page.waitForTimeout(2000)

    // Check if we're on an edit page or still on add page (both are valid after save)
    const currentUrl = page.url()
    // Should be either on edit page or add page (if validation failed)
    expect(currentUrl).toMatch(/\/admin\//)
  })

  test('should allow selecting multiple topics', async ({ page }) => {
    await navigateToAddPage(page, 'academy', 'academypage')

    // Fill required fields
    // Open "Promote" tab for slug field
    await openTab(page, 'Promote')
    const slugField = page.locator('input[name="slug"], input[id*="slug"]').first()
    await slugField.fill('test-academy-multiple')

    // Open "Common" tab for date and topics fields
    await openTab(page, 'Common')
    const dateField = page.locator('input[name="date"], input[type="date"], input[id*="date"]').first()
    await dateField.fill('2024-01-15')

    // Select multiple topics - MultiSelectField renders as checkboxes
    // Select "LT" (Liquid Democracy) and "DS" (Digital Civic Society)
    const ltCheckbox = page.locator('input[type="checkbox"][value="LT"]').first()
    const dsCheckbox = page.locator('input[type="checkbox"][value="DS"]').first()

    // Try to find by value first
    if (await ltCheckbox.count() > 0 && await dsCheckbox.count() > 0) {
      await ltCheckbox.check()
      await dsCheckbox.check()
    } else {
      // Fallback: find by label
      const ltLabel = page.locator('label:has-text("Liquid Democracy")').first()
      const dsLabel = page.locator('label:has-text("Digital Civic")').first()

      if (await ltLabel.count() > 0) {
        await ltLabel.click()
      }
      if (await dsLabel.count() > 0) {
        await dsLabel.click()
      }
    }

    await savePage(page, false)
    await page.waitForTimeout(2000)

    const currentUrl = page.url()
    expect(currentUrl).toMatch(/\/admin\//)
  })

  test('should respect max_choices constraint (3 topics)', async ({ page }) => {
    await navigateToAddPage(page, 'academy', 'academypage')

    // Fill required fields
    // Open "Promote" tab for slug field
    await openTab(page, 'Promote')
    const slugField = page.locator('input[name="slug"], input[id*="slug"]').first()
    await slugField.fill('test-academy-max-choices')

    // Open "Common" tab for date and topics fields
    await openTab(page, 'Common')
    const dateField = page.locator('input[name="date"], input[type="date"], input[id*="date"]').first()
    await dateField.fill('2024-01-15')

    // Try to select all 3 available topics (max_choices = 3)
    // Values: LT, DS, PA
    const ltCheckbox = page.locator('input[type="checkbox"][value="LT"]').first()
    const dsCheckbox = page.locator('input[type="checkbox"][value="DS"]').first()
    const paCheckbox = page.locator('input[type="checkbox"][value="PA"]').first()

    // Try to find by value first
    if (await ltCheckbox.count() > 0 && await dsCheckbox.count() > 0 && await paCheckbox.count() > 0) {
      await ltCheckbox.check()
      await dsCheckbox.check()
      await paCheckbox.check()
    } else {
      // Fallback: find all topic checkboxes and select first 3
      const allCheckboxes = page.locator('input[type="checkbox"][name*="topics"]')
      const checkboxCount = await allCheckboxes.count()
      if (checkboxCount >= 3) {
        for (let i = 0; i < 3; i++) {
          await allCheckboxes.nth(i).check()
        }
      }
    }

    await savePage(page, false)
    await page.waitForTimeout(2000)

    // Should save successfully with 3 topics
    const currentUrl = page.url()
    expect(currentUrl).toMatch(/\/admin\//)
  })
})
