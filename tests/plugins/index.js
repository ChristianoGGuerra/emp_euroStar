/*
AutomationStart Berlins 20-21 NOV. 2023
Automation for Accessibility – A Real Challenge
Thiago Machado & Christiano Guerra
*/

module.exports = (on, config) => {
    return {
      ...config,
      fixturesFolder: './fixtures',
      specPattern: './specs/**/*.cy.js',
      screenshotsFolder: './screenshots',
      videosFolder: './videos',
      supportFile: './support/e2e.js',
    };
  };