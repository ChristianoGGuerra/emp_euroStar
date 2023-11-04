/*
AutomationStart Berlins 20-21 NOV. 2023
Automation for Accessibility – A Real Challenge
Thiago Machado & Christiano Guerra
*/

const { defineConfig } = require("cypress");

module.exports = defineConfig({
  env: {
    baseUrl: 'http://localhost:8000/address/'
  },
  watchForFileChanges: false,
  reporter: 'cypress-mochawesome-reporter',
  reporterOptions: {
    charts: true,
    reportPageTitle: 'AutomationStar - Automation for Accessibility - Local',
    embeddedScreenshots: true,
    inlineAssets: true,
    saveAllAttempts: false,
    reportDir: 'results/conference',
  },
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
      require('cypress-mochawesome-reporter/plugin')(on);
      return require('./plugins/index.js') (on, config);
    },
    specPattern: './specs/**/*.cy.js',
    supportFile: './support/e2e.js',
  },
});
