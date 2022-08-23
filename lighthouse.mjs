import { join } from 'path'
import { writeFileSync, mkdirSync, existsSync } from 'fs'
import { launch } from 'chrome-launcher'
import lighthouse from 'lighthouse'

const serverUrls = [
  {
    pageName: 'Landing Page',
    url: ''
  },
  {
    pageName: 'Acadamy Index Page',
    url: '/liquid-academy'
  }
]

// add urls you want to locally test here
const localUrls = [
  {
    pageName: 'Landing Page',
    url: ''
  }
]

class LightHouseWrapper {
  currentDateTime = new Date().toISOString()
  reportFolder = join(process.cwd(), `reports/${this.currentDateTime}`)
  chrome = null
  baseUrl = 'https://stage.liqd.net'
  urls = serverUrls

  async auditSite (local = false) {
    if (local) {
      this.baseUrl = 'http://localhost:8006'
      this.urls = localUrls
    }
    await this.setup()
    const options = await this.getBrowserConfig()
    await this.triggerLightHouseAuditAndGetResults(options)
    await this.teardown()
  }

  async triggerLightHouseAuditAndGetResults (options) {
    for (let index = 0; index < this.urls.length; index++) {
      const runnerResult = await lighthouse(
        this.baseUrl + this.urls[index].url,
        options
      )
      const reportHtml = await runnerResult.report
      await writeFileSync(
        `${this.reportFolder}/${this.urls[index].pageName.trim()}.html`,
        reportHtml
      )
    }
  }

  async setup () {
    await this.makeReportDirectory()
    this.chrome = await launch({ chromeFlags: ['--headless'] })
  }

  async makeReportDirectory () {
    try {
      if (!(await existsSync(`${this.reportFolder}`))) {
        await mkdirSync(`${this.reportFolder}`, { recursive: true })
      }
    } catch (err) {
      console.error(err)
    }
  }

  async teardown () {
    await this.chrome.kill()
  }

  async getBrowserConfig () {
    const options = {
      logLevel: 'info',
      output: 'html',
      port: this.chrome.port
    }
    return options
  }
}

;(() => {
  const lighthouse = new LightHouseWrapper()
  ;(async () => {
    await lighthouse.auditSite(process.argv.splice(2)[0] === 'local')
  })()
})()
